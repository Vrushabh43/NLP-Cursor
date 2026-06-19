"""NLP-based information extraction from LaTeX source.

Extracts equation meanings, symbol descriptions, and inter-equation
relations from the raw .tex content of arXiv papers.  All extraction
is purely rule-based (regex + heuristics) — no LLM or prompting is used.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any


# ---------------------------------------------------------------------------
# Common physics symbol fallback descriptions
# ---------------------------------------------------------------------------

_KNOWN_SYMBOLS: dict[str, str] = {
    "hbar": "reduced Planck constant",
    "psi": "wave function",
    "Psi": "wave function",
    "phi": "phase or field",
    "Phi": "field operator",
    "rho": "density matrix",
    "sigma": "Pauli matrix or cross-section",
    "Sigma": "summation or self-energy",
    "omega": "angular frequency",
    "Omega": "frequency or solid angle",
    "lambda": "eigenvalue or coupling constant",
    "Lambda": "cosmological constant or cutoff",
    "epsilon": "small parameter",
    "delta": "variation or Dirac delta",
    "Delta": "change or difference",
    "alpha": "fine-structure constant or parameter",
    "beta": "inverse temperature or parameter",
    "gamma": "decay rate or Euler-Mascheroni constant",
    "Gamma": "decay width or gamma function",
    "theta": "angle parameter",
    "Theta": "Heaviside step function",
    "tau": "proper time or time parameter",
    "kappa": "coupling constant",
    "mu": "chemical potential or index",
    "nu": "frequency or index",
    "xi": "correlation length or parameter",
    "pi": "ratio of circumference to diameter",
    "chi": "susceptibility or response function",
    "eta": "metric tensor or parameter",
    "nabla": "gradient operator",
    "infty": "infinity",
    "dagger": "Hermitian conjugate",
    "ell": "angular momentum quantum number",
    "partial": "partial derivative",
}

# Patterns to match "where $SYMBOL$ is/denotes ... DESCRIPTION"
_WHERE_CLAUSE_RE = re.compile(
    r"(?:where|here|with)\s+"
    r"(?:\$([^$]+)\$\s*"
    r"(?:is|denotes|represents|stands\s+for|equals|being|=)\s+"
    r"(?:the\s+|a\s+|an\s+)?"
    r"([^,$\n]{3,80}))",
    re.IGNORECASE,
)

# Broader pattern: "$SYMBOL$ is the DESCRIPTION"
_INLINE_DEF_RE = re.compile(
    r"\$([^$]{1,40})\$\s+"
    r"(?:is|denotes|represents|means|being)\s+"
    r"(?:the\s+|a\s+|an\s+)?"
    r"([^,$.\n]{3,80})",
    re.IGNORECASE,
)

# Pattern for "$SYMBOL \equiv EXPRESSION" style definitions
_EQUIV_DEF_RE = re.compile(
    r"\$([^$]{1,30})\s*\\equiv\s*([^$]{1,60})\$",
)

# Relation keywords near equation references
_DERIVATION_KEYWORDS = [
    (r"(?:from|using|by)\s+", "derived from"),
    (r"(?:substitut\w+)\s+.*?\s+(?:into|in)\s+", "obtained by substitution into"),
    (r"(?:generaliz\w+)\s+", "generalization of"),
    (r"(?:special\s+case)\s+", "special case of"),
    (r"(?:reduc\w+\s+to)\s+", "reduces to"),
    (r"(?:equivalent\s+to)\s+", "equivalent to"),
    (r"(?:leads?\s+to)\s+", "leads to"),
    (r"(?:combined?\s+with)\s+", "combined with"),
    (r"(?:follows?\s+from)\s+", "follows from"),
    (r"(?:implies|imply)\s+", "implies"),
    (r"(?:bound|upper\s+bound|lower\s+bound)", "bounds"),
    (r"(?:analog\w*|similar\s+to)\s+", "analogous to"),
]

# LaTeX greek letter commands (for symbol extraction from equations)
_GREEK_COMMANDS = {
    "alpha", "beta", "gamma", "delta", "epsilon", "varepsilon",
    "zeta", "eta", "theta", "vartheta", "iota", "kappa",
    "lambda", "mu", "nu", "xi", "pi", "rho", "sigma",
    "tau", "upsilon", "phi", "varphi", "chi", "psi", "omega",
    "Gamma", "Delta", "Theta", "Lambda", "Xi", "Pi",
    "Sigma", "Phi", "Psi", "Omega",
}

# Standard math operators — NOT required in symbol dict per assignment
_STANDARD_OPERATORS = {
    "sum", "int", "prod", "lim", "inf", "sup", "min", "max",
    "sin", "cos", "tan", "log", "ln", "exp", "det", "tr",
    "frac", "sqrt", "cdot", "times", "pm", "mp",
    "leq", "geq", "neq", "equiv", "approx", "sim",
    "rightarrow", "leftarrow", "Rightarrow", "Leftarrow",
    "forall", "exists", "in", "subset", "supset", "cup", "cap",
    "oplus", "otimes", "oint", "nabla", "partial",
    "overline", "underline", "hat", "tilde", "bar", "vec", "dot",
    "left", "right", "big", "Big", "bigg", "Bigg",
    "begin", "end", "text", "mathrm", "mathbf", "mathcal",
    "quad", "qquad", "hspace", "vspace",
    "langle", "rangle", "lvert", "rvert",
    "bm", "boldsymbol", "textit", "textbf",
    "label", "tag", "nonumber", "notag",
    "cases", "split", "aligned",
}


# ---------------------------------------------------------------------------
# Meaning extraction
# ---------------------------------------------------------------------------

def extract_meaning(
    tex: str,
    eq_start: int,
    eq_end: int,
    equation_latex: str,
) -> tuple[str, dict[str, str]]:
    """Extract a short description of what an equation expresses.

    Parameters
    ----------
    tex : str
        Full LaTeX source of the paper (comments stripped).
    eq_start : int
        Character position of ``\\begin{...}`` for this equation.
    eq_end : int
        Character position of ``\\end{...}`` for this equation.
    equation_latex : str
        The LaTeX content of the equation itself.

    Returns
    -------
    meaning : str
        A concise description of the equation's meaning.
    audit : dict[str, str]
        Audit trail entries for this extraction step.
    """
    audit: dict[str, str] = {}

    # --- Get preceding text (up to 600 chars before the equation) ---
    pre_start = max(0, eq_start - 600)
    pre_text = tex[pre_start:eq_start].strip()
    # Remove LaTeX commands for readability but keep inline math
    pre_clean = re.sub(r"\\(?:cite|footnote|ref|eqref)\{[^}]*\}", "", pre_text)
    pre_clean = re.sub(r"\\(?:label|textit|textbf)\{([^}]*)\}", r"\1", pre_clean)
    pre_clean = re.sub(r"\s+", " ", pre_clean).strip()

    # --- Get following text (up to 400 chars after the equation) ---
    post_text = tex[eq_end:eq_end + 400].strip()
    post_clean = re.sub(r"\\(?:cite|footnote|ref|eqref)\{[^}]*\}", "", post_text)
    post_clean = re.sub(r"\\(?:label|textit|textbf)\{([^}]*)\}", r"\1", post_clean)
    post_clean = re.sub(r"\s+", " ", post_clean).strip()

    meaning = ""

    # Strategy 1: Extract introducing sentence (last sentence before equation)
    # Split on sentence boundaries
    sentences = re.split(r"(?<=[.!?])\s+", pre_clean)
    if sentences:
        last_sentence = sentences[-1].strip()
        # Remove trailing punctuation like "namely," or ":"
        last_sentence = re.sub(r"[,:;]\s*$", "", last_sentence).strip()
        # Remove inline math for cleaner meaning
        candidate = re.sub(r"\$[^$]+\$", "", last_sentence).strip()
        candidate = re.sub(r"\s+", " ", candidate).strip()
        if len(candidate) > 15:
            meaning = candidate
            audit["extract_meaning_pre"] = (
                f"Extracted introducing sentence: '{meaning[:120]}'"
            )

    # Strategy 2: If pre-text is too short, check post-text for "which describes..."
    if len(meaning) < 15:
        desc_match = re.search(
            r"(?:which|this|that)\s+(?:is|describes?|expresses?|gives?|represents?|defines?)\s+"
            r"(?:the\s+|a\s+|an\s+)?([^.]{10,100})",
            post_clean, re.IGNORECASE,
        )
        if desc_match:
            meaning = desc_match.group(0).strip()
            audit["extract_meaning_post"] = (
                f"Extracted from post-equation text: '{meaning[:120]}'"
            )

    # Strategy 3: Named equation detection from pre-text
    if not meaning or len(meaning) < 10:
        name_patterns = [
            r"([\w\s-]+(?:equation|inequality|bound|formula|relation|identity|law|"
            r"theorem|condition|constraint|definition|decomposition|expansion|"
            r"principle|rule|series|limit|approximation))",
        ]
        for pat in name_patterns:
            m = re.search(pat, pre_clean, re.IGNORECASE)
            if m:
                name = m.group(1).strip()
                if 5 < len(name) < 80:
                    meaning = name
                    audit["extract_meaning_named"] = f"Detected named equation: '{name}'"
                    break

    # Fallback: use a trimmed version of the pre-text
    if not meaning or len(meaning) < 10:
        fallback = pre_clean[-150:].strip()
        fallback = re.sub(r"^.*?[.!?]\s+", "", fallback)  # start from last sentence
        fallback = re.sub(r"[,:;]\s*$", "", fallback).strip()
        if len(fallback) > 10:
            meaning = fallback
            audit["extract_meaning_fallback"] = (
                f"Used trimmed preceding text: '{meaning[:120]}'"
            )

    # Clean up the meaning
    meaning = re.sub(r"\$[^$]*\$", "", meaning).strip()  # remove inline math
    meaning = re.sub(r"\\[a-zA-Z]+\{?[^}]*\}?", "", meaning).strip()  # remove LaTeX cmds
    meaning = re.sub(r"\s+", " ", meaning).strip()
    meaning = meaning[:200]  # cap length

    if not audit:
        audit["extract_meaning"] = "No meaningful context found near equation"

    return meaning, audit


# ---------------------------------------------------------------------------
# Symbol extraction from equation LaTeX
# ---------------------------------------------------------------------------

def extract_symbols_from_latex(equation_latex: str) -> list[str]:
    """Extract physics variable/symbol names from an equation's LaTeX.

    Parameters
    ----------
    equation_latex : str
        Raw LaTeX content of the equation.

    Returns
    -------
    list[str]
        Sorted list of symbol keys (LaTeX command names without backslash,
        or single-letter variable names).  Standard math operators are excluded.
    """
    symbols: set[str] = set()

    # 1. Greek letters and special commands: \alpha, \Psi, \hbar, ...
    for m in re.finditer(r"\\([a-zA-Z]+)", equation_latex):
        cmd = m.group(1)
        if cmd in _GREEK_COMMANDS or cmd in _KNOWN_SYMBOLS:
            symbols.add(cmd)

    # 2. Calligraphic / hat / bar / tilde decorated symbols: \hat{H}, \mathcal{U}
    for m in re.finditer(
        r"\\(?:hat|tilde|bar|vec|dot|ddot|mathcal|mathbb|boldsymbol|bm)"
        r"\{([A-Za-z](?:_\{[^}]+\})?)\}",
        equation_latex,
    ):
        inner = m.group(1)
        # e.g., \mathcal{U} → "mathcal_U", \hat{H} → "hat_H"
        prefix = re.match(
            r"\\(hat|tilde|bar|vec|dot|ddot|mathcal|mathbb|boldsymbol|bm)",
            m.group(0),
        )
        if prefix:
            key = f"{prefix.group(1)}_{inner.split('_')[0]}"
            symbols.add(key)

    # 3. Single-letter variables (uppercase that are likely physics variables)
    #    Match standalone letters not part of \commands, like H, A, E, K, N, etc.
    #    Be conservative: only uppercase and select lowercase
    cleaned = re.sub(r"\\[a-zA-Z]+", " ", equation_latex)  # remove commands
    cleaned = re.sub(r"\{[^}]*\}", " ", cleaned)  # simplify braces
    for m in re.finditer(r"(?<![a-zA-Z])([A-Z])(?![a-zA-Z])", cleaned):
        letter = m.group(1)
        if letter not in {"I", "T"}:  # skip very common non-variable uses
            symbols.add(letter)

    # 4. Subscripted variables: d_{eff}, E_n, c_n^k, etc.
    for m in re.finditer(r"([a-zA-Z])_\{([a-zA-Z0-9,\\]+)\}", equation_latex):
        base = m.group(1)
        sub = m.group(2)
        # Clean subscript: remove \text{}, \mathrm{} wrappers
        sub_clean = re.sub(r"\\(?:text|mathrm|rm)\{([^}]*)\}", r"\1", sub)
        sub_clean = re.sub(r"\\", "", sub_clean)
        key = f"{base}_{{{sub_clean}}}"
        symbols.add(key)

    # Remove standard operators and very common tokens
    symbols -= _STANDARD_OPERATORS
    symbols -= {"", "0", "1", "2", "3", "n", "m", "k", "l", "i", "j", "t", "d"}

    return sorted(symbols)


# ---------------------------------------------------------------------------
# Symbol description extraction
# ---------------------------------------------------------------------------

def build_symbol_table(tex: str) -> dict[str, str]:
    """Build a global table of symbol → description from the full paper.

    Parameters
    ----------
    tex : str
        Full LaTeX source (comments stripped).

    Returns
    -------
    dict[str, str]
        Mapping from symbol key to description.
    """
    table: dict[str, str] = {}

    # Search for "where $X$ is ..." patterns
    for m in _WHERE_CLAUSE_RE.finditer(tex):
        sym_raw = m.group(1).strip()
        desc = m.group(2).strip()
        key = _latex_to_symbol_key(sym_raw)
        if key and desc and key not in table:
            table[key] = _clean_description(desc)

    # Search for "$X$ is/denotes the ..." patterns
    for m in _INLINE_DEF_RE.finditer(tex):
        sym_raw = m.group(1).strip()
        desc = m.group(2).strip()
        key = _latex_to_symbol_key(sym_raw)
        if key and desc and key not in table:
            table[key] = _clean_description(desc)

    # Search for "$X \equiv EXPR$" definitions
    for m in _EQUIV_DEF_RE.finditer(tex):
        sym_raw = m.group(1).strip()
        defn = m.group(2).strip()
        key = _latex_to_symbol_key(sym_raw)
        if key and defn and key not in table:
            # Store the LaTeX definition as description
            defn_clean = re.sub(r"\s+", " ", defn).strip()
            table[key] = f"defined as ${defn_clean}$"

    return table


def _latex_to_symbol_key(latex_fragment: str) -> str | None:
    """Convert a LaTeX math fragment to a symbol dictionary key.

    Parameters
    ----------
    latex_fragment : str
        Raw LaTeX like ``\\Psi(t)``, ``d_{eff}``, ``H_{\\infty}``.

    Returns
    -------
    str or None
        Symbol key (e.g., ``Psi``, ``d_{eff}``, ``H_{infty}``), or None
        if the fragment cannot be reduced to a meaningful key.
    """
    s = latex_fragment.strip()
    # Remove decorators: \bar{X} → X, \hat{X} → X, \overline{X} → X
    s = re.sub(r"\\(?:bar|hat|tilde|vec|overline|underline)\{([^}]+)\}", r"\1", s)
    # Remove function arguments: X(t) → X, X(0^+) → X
    s = re.sub(r"\([^)]*\)", "", s)
    # Remove bra-ket: |X⟩ → X
    s = re.sub(r"[|⟨⟩\\langle\\rangle]", "", s)
    s = s.strip()

    if not s:
        return None

    # \command → command
    if s.startswith("\\"):
        cmd = re.match(r"\\([a-zA-Z]+)", s)
        if cmd:
            rest = s[cmd.end():].strip()
            if rest and rest.startswith("_"):
                # e.g., \rho_I → rho_I
                sub = re.match(r"_\{?([^}]*)\}?", rest)
                if sub:
                    sub_clean = sub.group(1).replace("\\", "")
                    return f"{cmd.group(1)}_{{{sub_clean}}}"
            return cmd.group(1)

    # Single letter or subscripted: H, d_{eff}, E_n
    m = re.match(r"([A-Za-z])(?:_\{?([^}]*)\}?)?$", s)
    if m:
        base = m.group(1)
        sub = m.group(2)
        if sub:
            sub_clean = re.sub(r"\\(?:text|mathrm|rm)\{([^}]*)\}", r"\1", sub)
            sub_clean = sub_clean.replace("\\", "")
            return f"{base}_{{{sub_clean}}}"
        return base

    return None


def _clean_description(desc: str) -> str:
    """Clean and truncate a symbol description."""
    d = desc.strip()
    d = re.sub(r"\\cite\{[^}]*\}", "", d)
    d = re.sub(r"\$[^$]*\$", "", d)
    d = re.sub(r"\\[a-zA-Z]+\{?[^}]*\}?", "", d)
    d = re.sub(r"\s+", " ", d).strip()
    d = re.sub(r"[,;.]+$", "", d).strip()
    return d[:120]


def get_symbol_descriptions(
    equation_symbols: list[str],
    global_table: dict[str, str],
    tex: str,
    eq_start: int,
    eq_end: int,
) -> tuple[dict[str, str], dict[str, str]]:
    """Get descriptions for all symbols in an equation.

    Parameters
    ----------
    equation_symbols : list[str]
        Symbol keys extracted from the equation.
    global_table : dict[str, str]
        Global symbol-to-description table from the full paper.
    tex : str
        Full LaTeX source.
    eq_start : int
        Start position of the equation in *tex*.
    eq_end : int
        End position of the equation in *tex*.

    Returns
    -------
    symbols_dict : dict[str, str]
        Mapping of symbol key to description.
    audit : dict[str, str]
        Audit trail entries.
    """
    symbols_dict: dict[str, str] = {}
    audit: dict[str, str] = {}

    # Local context: text after the equation (where definitions often are)
    local_text = tex[eq_end:eq_end + 500]

    for sym_key in equation_symbols:
        desc = None

        # 1. Check local "where" clause first
        # Build a regex to find this symbol in the local text
        escaped = re.escape(sym_key).replace(r"\{", "{").replace(r"\}", "}")
        local_pattern = re.compile(
            rf"(?:\$[^$]*{escaped}[^$]*\$|{escaped})\s+"
            rf"(?:is|denotes|represents|being|≡|\\equiv)\s+"
            rf"(?:the\s+|a\s+|an\s+)?([^,$.\n]{{3,80}})",
            re.IGNORECASE,
        )
        m = local_pattern.search(local_text)
        if m:
            desc = _clean_description(m.group(1))
            if desc:
                audit[f"find_symbol_{sym_key}"] = (
                    f"Found local definition: {sym_key} = '{desc}'"
                )

        # 2. Check global symbol table
        if not desc and sym_key in global_table:
            desc = global_table[sym_key]
            audit[f"find_symbol_{sym_key}"] = (
                f"Found global definition: {sym_key} = '{desc}'"
            )

        # 3. Check known physics symbols fallback
        if not desc:
            # Try base name (e.g., for "rho_{I}" try "rho")
            base = sym_key.split("_")[0] if "_" in sym_key else sym_key
            if base in _KNOWN_SYMBOLS:
                desc = _KNOWN_SYMBOLS[base]
                audit[f"find_symbol_{sym_key}"] = (
                    f"Used known physics symbol: {sym_key} = '{desc}'"
                )

        if desc:
            symbols_dict[sym_key] = desc
        else:
            # Still include symbol with empty description
            symbols_dict[sym_key] = ""
            audit[f"find_symbol_{sym_key}"] = (
                f"No description found for symbol: {sym_key}"
            )

    return symbols_dict, audit


# ---------------------------------------------------------------------------
# Relation classification
# ---------------------------------------------------------------------------

@dataclass
class EquationInfo:
    """Container for equation data used in relation classification."""

    number: str
    latex: str
    symbols: list[str]
    label: str = ""
    position: int = 0
    section: str = ""


def _find_cross_references(
    tex: str,
    equations: list[EquationInfo],
    label_to_number: dict[str, str],
) -> dict[str, set[str]]:
    """Find textual cross-references between equations.

    Parameters
    ----------
    tex : str
        Full LaTeX source.
    equations : list[EquationInfo]
        All equations with their positions.
    label_to_number : dict[str, str]
        Mapping from LaTeX label to equation number.

    Returns
    -------
    dict[str, set[str]]
        For each equation number, the set of other equation numbers
        referenced in its surrounding text.
    """
    refs: dict[str, set[str]] = {eq.number: set() for eq in equations}

    for eq in equations:
        # Get surrounding text (300 chars before and after)
        start = max(0, eq.position - 300)
        end = min(len(tex), eq.position + 300)
        context = tex[start:end]

        # Find \eqref{label} references
        for m in re.finditer(r"\\eqref\{([^}]+)\}", context):
            label = m.group(1)
            if label in label_to_number:
                ref_num = label_to_number[label]
                if ref_num != eq.number:
                    refs[eq.number].add(ref_num)

        # Find (N) or Eq. (N) or equation (N) references
        for m in re.finditer(
            r"(?:Eq(?:uation)?\.?\s*)?(?:\(|\\eqref\{)(\d+[a-z]?|[A-Z]\d+)(?:\)|\})",
            context,
        ):
            ref_num = m.group(1)
            if ref_num != eq.number and any(e.number == ref_num for e in equations):
                refs[eq.number].add(ref_num)

    return refs


def _compute_symbol_similarity(eq_a: EquationInfo, eq_b: EquationInfo) -> float:
    """Compute Jaccard similarity of symbol sets between two equations.

    Parameters
    ----------
    eq_a, eq_b : EquationInfo
        The two equations to compare.

    Returns
    -------
    float
        Jaccard similarity in [0, 1].
    """
    set_a = set(eq_a.symbols)
    set_b = set(eq_b.symbols)
    if not set_a and not set_b:
        return 0.0
    intersection = set_a & set_b
    union = set_a | set_b
    return len(intersection) / len(union) if union else 0.0


def _detect_relation_keywords(
    tex: str,
    eq_a: EquationInfo,
    eq_b: EquationInfo,
    label_to_number: dict[str, str],
) -> str | None:
    """Search for relation-describing keywords between two equations.

    Parameters
    ----------
    tex : str
        Full LaTeX source.
    eq_a, eq_b : EquationInfo
        The two equations.
    label_to_number : dict[str, str]
        Label-to-number mapping.

    Returns
    -------
    str or None
        Relation description if keywords found, else None.
    """
    number_to_label = {v: k for k, v in label_to_number.items()}

    # Build patterns to find eq_b referenced near eq_a
    ref_patterns = [rf"\({re.escape(eq_b.number)}\)"]
    if eq_b.number in number_to_label:
        ref_patterns.append(
            rf"\\eqref\{{{re.escape(number_to_label[eq_b.number])}\}}"
        )

    # Search around eq_a's position
    start = max(0, eq_a.position - 100)
    end = min(len(tex), eq_a.position + 500)
    context = tex[start:end].lower()

    for ref_pat in ref_patterns:
        for keyword_pat, description in _DERIVATION_KEYWORDS:
            full_pat = keyword_pat + r".*?" + ref_pat.lower()
            if re.search(full_pat, context):
                return description
            # Also check reverse: ref before keyword
            full_pat_rev = ref_pat.lower() + r".*?" + keyword_pat
            if re.search(full_pat_rev, context):
                return description

    return None


def classify_relations(
    equations: list[EquationInfo],
    tex: str,
    label_to_number: dict[str, str],
) -> tuple[dict[str, dict[str, dict[str, str]]], dict[str, str]]:
    """Classify relations between all equation pairs in a paper.

    Parameters
    ----------
    equations : list[EquationInfo]
        All equations with metadata.
    tex : str
        Full LaTeX source.
    label_to_number : dict[str, str]
        Label-to-number mapping.

    Returns
    -------
    relations : dict
        Nested ``{eq_num: {other_num: {"grade": ..., "description": ...}}}``.
    audit : dict[str, str]
        Audit trail entries.
    """
    audit: dict[str, str] = {}

    # Step 1: Find textual cross-references
    cross_refs = _find_cross_references(tex, equations, label_to_number)

    # Step 2: Build relation dicts
    relations: dict[str, dict[str, dict[str, str]]] = {}
    eq_numbers = [eq.number for eq in equations]
    eq_by_number = {eq.number: eq for eq in equations}

    for eq in equations:
        relations[eq.number] = {}
        for other_num in eq_numbers:
            if other_num == eq.number:
                continue

            other_eq = eq_by_number[other_num]
            grade = "none"
            description = ""

            # Check 1: Direct textual cross-reference
            has_ref_a_to_b = other_num in cross_refs.get(eq.number, set())
            has_ref_b_to_a = eq.number in cross_refs.get(other_num, set())

            # Check 2: Keyword-based relation detection
            kw_desc = _detect_relation_keywords(
                tex, eq, other_eq, label_to_number
            )

            # Check 3: Symbol similarity
            sim = _compute_symbol_similarity(eq, other_eq)

            # Classification logic
            if (has_ref_a_to_b or has_ref_b_to_a) and kw_desc:
                grade = "strong"
                description = kw_desc
            elif has_ref_a_to_b or has_ref_b_to_a:
                grade = "strong"
                if has_ref_a_to_b:
                    description = "referenced in derivation"
                else:
                    description = "references this equation"
            elif kw_desc:
                grade = "potential"
                description = kw_desc
            elif sim > 0.4:
                grade = "potential"
                description = "shares significant mathematical symbols"
            elif sim > 0.25 and abs(
                eq_numbers.index(eq.number) - eq_numbers.index(other_num)
            ) <= 2:
                grade = "potential"
                description = "nearby equation with shared symbols"

            relations[eq.number][other_num] = {
                "grade": grade,
                "description": description,
            }

    # Audit summary
    strong_count = sum(
        1 for eq_rels in relations.values()
        for rel in eq_rels.values() if rel["grade"] == "strong"
    )
    potential_count = sum(
        1 for eq_rels in relations.values()
        for rel in eq_rels.values() if rel["grade"] == "potential"
    )
    total_pairs = sum(len(eq_rels) for eq_rels in relations.values())
    audit["classify_relations"] = (
        f"Classified {total_pairs} equation pairs: "
        f"{strong_count} strong, {potential_count} potential, "
        f"{total_pairs - strong_count - potential_count} none"
    )

    return relations, audit
