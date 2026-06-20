References

## Soft symmetries of topological orders

Ryohei Kobayashi 1 and Maissam Barkeshli 2

1 School of Natural Sciences, Institute for Advanced Study, Princeton, NJ 08540, USA

2 Department of Physics and Joint Quantum Institute, University of Maryland, College Park, Maryland 20742, USA

(2+1)D topological orders possess emergent symmetries given by a group Aut br ( C ), which consists of the braided tensor autoequivalences of the modular tensor category C that describes the anyons. In this paper we discuss cases where Aut br ( C ) has elements that neither permute anyons nor are associated to any symmetry fractionalization but are still non-trivial, which we refer to as soft symmetries. We point out that one can construct topological defects corresponding to such exotic symmetry actions by decorating with a certain class of gauged SPT states that cannot be distinguished by their torus partition function. This gives a physical interpretation to work by Davydov on soft braided tensor autoequivalences. This has a number of important implications for the classification of gapped boundaries, non-invertible spontaneous symmetry breaking, and the general classification of symmetryenriched topological phases of matter. We also demonstrate analogous phenomena in higher dimensions, such as (3+1)D gauge theory with gauge group given by the quaternion group Q 8 .

## CONTENTS

| I.    | Introduction                                                        |   2 |
|-------|---------------------------------------------------------------------|-----|
| II.   | Global Symmetries of (2+1)D Topological Order                       |   2 |
|       | A. Review: Unitary modular tensor categories                        |   3 |
|       | B. 0-form symmetry: Braided tensor auto-equivalences                |   4 |
|       | C. Symmetry action on genus g surfaces                              |   5 |
|       | D. 2-group symmetry and H 3 (Aut( C ) , A ) class                   |   6 |
|       | E. Symmetry fractionalization                                       |   6 |
|       | F. Global symmetry G of quantum many-body system                    |   7 |
| III.  | Soft symmetry from gauged SPT defects                               |   8 |
|       | A. Review: gauged SPT defects                                       |   8 |
|       | B. Soft autoequivalence of finite gauge theory                      |   9 |
| IV.   | Lattice model                                                       |  12 |
|       | A. Quantum double model                                             |  12 |
|       | B. Trivial permutation action on anyons                             |  13 |
|       | C. Symmetry action on anyon junctions                               |  14 |
|       | D. Emergent symmetry and faithful action on genus g ≥ 2 surfaces    |  15 |
| V.    | Distinct gapped boundaries with identical condensed particles       |  16 |
|       | A. Application: Oblique SSB phase of Rep( G sf ) symmetry in (1+1)D |  17 |
| VI.   | Higher dimensions: Q 8 gauge theory in (3+1)D                       |  17 |
| VII.  | Discussion                                                          |  18 |
| VIII. | Acknowledgment                                                      |  19 |
| A.    | Symmetric representative of second cohomology H 2 ( BG sf ,U (1))   |  19 |
| B.    | (1+1)D SPT phases with genus ≥ 3 detection                          |  20 |

21

## I. INTRODUCTION

A fundamental question in quantum many-body physics is to understand the relationship between global symmetries and topological order, which is the subject of symmetry-enriched topological phases of matter [1-3]. The most well-known example of a such a relationship is how anyons of a topologically ordered state can carry fractional quantum numbers under a global symmetry, a phenomenon known as symmetry fractionalization, with prominent examples being the fractional electric charges in the fractional quantum Hall effect [4-6], or fractional spin in quantum spin liquids [7]. A more recently understood phenomenon relates to how discrete global symmetries can permute topologically distinct anyon types, which leads to the striking possibility of non-Abelian twist defects, even when the underlying topological phase only has Abelian anyons [8-11]. These play an important role in fault-tolerant topological quantum computation [12-15]; they have been experimentally demonstrated in quantum computers [16, 17] and a variety of experimental proposals have been suggested for realizing them in two-dimensional electron systems [18-23].

A longstanding question in this subject has been whether there can be symmetries that are neither fractionalized nor permute anyons, but nevertheless have a non-trivial action on the topological state. We refer to such symmetries as soft symmetries . In this paper, we demonstrate how soft symmetries can indeed arise. The key insight that we exploit is that in a (2+1)D topological phase described by G gauge theory, we can decorate a codimension-1 submanifold with a (1+1)D G -symmetry protected topological state ( G -SPT) before gauging G everywhere [24]. The result is an invertible codimension-1 topological defect that we refer to as a gauged SPT defect. Since the gauged SPT defect is invertible, it can be pumped across the entire system by a finite depth local unitary circuit and keeps the ground state subspace invariant. As such, we consider the corresponding circuit to be an emergent symmetry of the topological state. 1 As we will discuss, if the SPT cannot be detected by its torus partition function, then the resulting gauged SPT defect has the surprising property mentioned above, which we verify explicitly using exactly solvable two-dimensional lattice models of quantum doubles. The emergent symmetry that we find acts as the identity on the ground state subspace on a torus while acting non-trivially on the ground state subspace on higher genus surfaces.

Our result has a number of important implications for our fundamental understanding of topological order:

- With respect to the classification of gapped boundaries [25-30], our result demonstrates how there can be inequivalent gapped boundaries that have the same set of condensed anyons.
- The above in turn implies that there are two distinct (1+1)D gapped phases where a non-invertible Rep( G ) symmetry is spontaneously broken completely.
- With respect to our understanding of SETs, our results demonstrate how there can be subtle types of symmetries that can only be distinguished by their action on the ground state subspace on surfaces of genus g ≥ 2.

The results presented here also provide a physical interpretation of the soft braided tensor auto-equivalences discovered by Davydov in [31]. Our physical construction in terms of gauged SPT defects gives additional insights that we use to discover soft symmetries in (3+1)D topological orders.

This paper is organized as follows. In Sec. II we first review the algebraic theory of anyons and its autoequivalences, and introduce the algebraic description of soft symmetries. In Sec. III we introduce an example of a soft symmetry defect realized in finite gauge theory in (2+1)D. In Sec. IV we introduce a lattice model of the quantum double that has the soft symmetry. In Sec. V we discuss an implication of the soft symmetry for gapped boundaries of finite gauge theory, and discuss how it leads to the distinct SSB phases of Rep( G ) symmetry. In Sec. VI we discuss the analogue of soft symmetry in higher dimensions, focusing on Q 8 gauge theory in (3+1)D.

## II. GLOBAL SYMMETRIES OF (2+1)D TOPOLOGICAL ORDER

Our starting point is a unitary modular tensor category C , which is an algebraic framework to describe the universal fusion and braiding properties of anyons in (2+1)D topological orders. To set the notation, we briefly review the key data below. We refer the reader to Appendix E of [32] and Refs. [3, 33, 34] for a comprehensive account aimed at physicists. Methods to define this algebraic data in microscopic models were described in [35].

1 In our construction, we get a non-onsite emergent symmetry in general.

## A. Review: Unitary modular tensor categories

In the notation below, we follow the convention of [3, 36]. A UMTC [37, 38] C consists of a finite set of anyons { a } , obeying fusion rules

$$a \times b = \sum _ { c } N _ { a b } ^ { c } c , & & ( 1 ) \\ \intertext { a } a \times b = \sum _ { c } N _ { a b } ^ { c } c , & & ( 1 ) \\$$

where N c ab are non-negative integers. The theory contains linear vector spaces, referred to as 'fusion spaces,' V c ab , and their dual 'splitting spaces' V ab c , such that dim V c ab = dim V ab c = N c ab . The basis states in these spaces are diagrammatically depicted as:

$$( d _ { c } / d _ { a } d _ { b } ) ^ { 1 / 4 } \overset { ( d _ { c } / d _ { a } d _ { b } ) ^ { 1 / 4 } } { a } \overset { \mu } { \sim } b ^ { \mu } = \langle a , b ; c , \mu | \in V _ { a b } ^ { c } , \quad ( d _ { c } / d _ { a } d _ { b } ) ^ { 1 / 4 } \overset { a } { \sim } b ^ { \mu } = | a ; b ; c , \mu \rangle \in V _ { c } ^ { a b } , \quad ( 2 )$$

where µ = 1 , . . . , N c ab , d a is the quantum dimension of a , and the factors ( d c d a d b ) 1 / 4 are a normalization convention for the diagrams. The set of anyons contains the identity or vacuum charge 0, and each anyon a has a dual anti-particle ¯ a such that a × ¯ a = 0 + · · · .

The theory is defined by a consistent set of F and R symbols, which are unitary maps on the vector spaces:

$$\tilde { \ F _ { d } ^ { a b c } } \otimes & V _ { e } ^ { a b } \otimes V _ { d } ^ { e c } \rightarrow \bigotimes _ { f } V _ { d } ^ { a f } \otimes V _ { f } ^ { b c } , \\ & R _ { c } ^ { a b } \colon V _ { c } ^ { a b } \rightarrow V _ { c } ^ { a b } .$$

These are depicted graphically as

<!-- image -->

If we perform a basis transformation, referred to as a vertex basis gauge transformation, on the fusion and splitting states, F and R symbols transform:

$$\Gamma _ { c } ^ { a b } \cdot & \rightarrow \tilde { V } _ { c } ^ { a b } \rightarrow \tilde { V } _ { c } ^ { a b } \\ | a , b ; c , \mu \rangle & \rightarrow \sum _ { \nu } ( \Gamma _ { c } ^ { a b } ) _ { \mu \nu } | a , b ; c , \nu \rangle \\ ( F a c ) _ { \ e f } & \rightarrow \Gamma _ { c } ^ { a b } \Gamma e _ { c } ^ { c } ( F a c ) _ { \ e f } ( \Gamma _ { d } ^ { a f } ) ^ { - 1 } ( \Gamma _ { f } ) ^ { - 1 } \\ R _ { c } ^ { a b } & \rightarrow \Gamma _ { c } ^ { a b } R _ { c } ^ { a b } ( \Gamma _ { c } ^ { a b } ) ^ { - 1 } , \\ \intertext { s e c h } \intertext { s e d a t i o n a l d i n c i s } \intertext { c h e r s d e f } \intertext { s e d a t i o n a l d i n c i s } \intertext { p h e r s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \intertext { s e d a t i o n a l d i n c i s } \int$$

where we have suppressed additional indices in the transformation of the F and R symbols. The terminology 'gauge transformation' originates from the fact that the matrices { Γ ab c } redefine the F, R symbols of the modular tensor category, giving a different expression of the same theory, thus putting a redundancy in the presentation of the theory.

Properties of the UMTC that are invariant under the vertex basis gauge transformation include the topological twists θ a and the modular S matrix. A special role will be played by natural isomorphisms , which are vertex basis gauge transformations such that

$$( \Gamma _ { c } ^ { a b } ) _ { \mu \nu } = \frac { \gamma _ { a } \gamma _ { b } } { \gamma _ { c } } \delta _ { \mu \nu } ,$$

where γ a is a U (1) phase. These natural isomorphisms do not change the F and R symbols, and leaves all closed anyon diagrams with junctions invariant. Therefore the natural isomorphisms are regarded as trivial gauge transformations, putting a redundancy in the expressions of vertex basis gauge transformations.

## B. 0-form symmetry: Braided tensor auto-equivalences

We define an invertible map φ : C → C , which has an action on all of the data of the theory. φ is a braided tensor autoequivalence if the following is satisfied. It transforms the anyons as

$$a \rightarrow \varphi ( a ) = a ^ { \prime } ,$$

such that gauge invariant quantities are invariant under φ :

$$N _ { a ^ { \prime } b ^ { \prime } } ^ { c ^ { \prime } } & = N _ { a b } ^ { c } \\ S _ { a ^ { \prime } b ^ { \prime } } & = S _ { a b } \\ \theta _ { a ^ { \prime } } & = \theta _ { a } .$$

φ acts on the fusion and splitting spaces as a linear map: 2

$$\varphi \colon V _ { c } ^ { a b } & \to V _ { c ^ { \prime } } ^ { a ^ { \prime } b ^ { \prime } } , \\ \varphi ( | a , b ; c , \mu ) & = \sum _ { \nu } [ U _ { \varphi } ( a ^ { \prime } , b ^ { \prime } ; c ^ { \prime } ) ] _ { \mu \nu } | a ^ { \prime } , b ^ { \prime } ; c ^ { \prime } \nu \rangle$$

and it transforms the F and R symbols of the theory as follows:

$$\varphi ( R _ { c } ^ { a b } ) & = \tilde { R } _ { c ^ { \prime } } ^ { a ^ { \prime } b ^ { \prime } } \equiv U _ { \varphi } ( b ^ { \prime } , a ^ { \prime } ; c ^ { \prime } ) R _ { c ^ { \prime } } ^ { a ^ { \prime } b ^ { \prime } } U _ { \varphi } ^ { \dagger } ( a ^ { \prime } , b ^ { \prime } ; c ^ { \prime } ) \\ \varphi ( [ F _ { d } ^ { a b c } ] _ { e f } ) & = [ \tilde { F } _ { d ^ { \prime } } ^ { a ^ { \prime } b ^ { \prime } c ^ { \prime } } ] _ { e ^ { \prime } f ^ { \prime } } \equiv U _ { \varphi } ( a ^ { \prime } , b ^ { \prime } ; e ^ { \prime } ) U _ { \varphi } ( e ^ { \prime } , c ^ { \prime } ; f ^ { \prime } ) [ F _ { d ^ { \prime } } ^ { a ^ { \prime } b ^ { \prime } c ^ { \prime } } ] _ { e ^ { \prime } f ^ { \prime } } U _ { \varphi } ^ { \dagger } ( a ^ { \prime } , f ^ { \prime } ; d ^ { \prime } ) U _ { \varphi } ^ { \dagger } ( b ^ { \prime } , c ^ { \prime } ; f ^ { \prime } ) , \\$$

where again we have suppressed the additional indices. These transformations must by definition keep the F and R symbols invariant:

$$[ \tilde { F } _ { d ^ { \prime } } ^ { a ^ { \prime } b ^ { \prime } c ^ { \prime } } ] _ { e ^ { \prime } f ^ { \prime } } = [ F _ { d } ^ { a b c } ] _ { e f } ,$$

$$\tilde { R } _ { c ^ { \prime } } ^ { a ^ { \prime } b ^ { \prime } } = R _ { c } ^ { a b } .$$

$$[ F _ { d ^ { \prime } } ^ { a } b \, c ] _ { e ^ { \prime } f ^ { \prime } } & = [ F _ { d } ^ { a b } ] _ { c } \\ \tilde { R } _ { c ^ { \prime } } ^ { a ^ { \prime } b ^ { \prime } } & = R _ { c } ^ { a b } .$$

We can depict these transformations graphically by introducing a codimension-1 defect labeled by φ .

<!-- image -->

The invariance of F , Eq. 11, can be understood as a consequence of commutativity of the following diagram:

2 It is possible to generalize to anti-linear operations as well, as in [3].

<!-- image -->

The invariance of R , Eq. 12, can be derived by introducing additional data associated with G -crossed braiding of codefects, as described in Eq. 280 - 282 of [3].

It is natural to consider an equivalence relation on such maps, where two maps φ and φ ′ are equivalent if there is a continuous family of maps φ s for s ∈ [0 , 1], such that φ 0 = φ and φ 1 = φ ′ . Note that φ -1 s ◦ φ s ′ is a vertex basis gauge transformation that keeps the F -symbols invariant

$$\Gamma _ { e } ^ { a b } \Gamma _ { f } ^ { e c } [ F _ { d } ^ { a b c } ] _ { e f } ( \Gamma _ { d } ^ { a f } ) ^ { \dagger } ( \Gamma _ { f } ^ { b c } ) ^ { \dagger } = [ F _ { d } ^ { a b c } ] _ { e f } .$$

While such vertex gauge transformations are labeled by continuous unitary matrices on each fusion vertex, up to deformation they generate a finite group. In fact, considering maps φ up to continuous deformation is equivalent to considering them up to natural isomorphisms, due to Ocneanu rigidity [32, 39]. The rigidity states that the infinitesimal gauge transformation Γ ab c satisfying (13) can be expressed as a natural isomorphism

$$\Gamma _ { c } ^ { a b } = \frac { \gamma _ { a } \gamma _ { b } } { \gamma _ { c } } \quad \text {when } \Gamma _ { c } ^ { a b } \approx \text {id} _ { V _ { c } ^ { a b } } \text { and satisfies } ( 1 3 ) \, ,$$

where γ a , γ b , γ c are phase factors close to unity. Taking equivalence classes of braided tensor autoequivalences modulo natural isomorphisms defines a finite group, denoted Aut br ( C ), which is the group of braided auto-equivalences of C .

In this paper, we are interested in elements of Aut br ( C ) that do not permute anyons but which are nevertheless non-trivial, namely φ ∈ Aut br ( C ) satisfying the following two conditions:

- φ ( a ) = a for all anyons a .
- The U symbol { U φ ( a, b ; c ) } is not a natural isomorphism.

We refer to such transformations as soft symmetries and we denote the group of soft symmetries as Aut sf ( C ) ⊂ Aut br ( C ). In the mathematics literature they are referred to as soft braided tensor autoequivalences. We see that such transformations correspond to vertex basis gauge transformations that keep the F and R symbols invariant and which are not continuously deformable to the identity.

## C. Symmetry action on genus g surfaces

The U symbols characterize the action of [ φ ] ∈ Aut br ( C ) on the space of states on a closed genus g surface. We can pick an orthonormal basis of states on the genus g surface as

$$\bigotimes _ { j = 1 } ^ { g } | a _ { j } , \overline { a _ { j } } ; z _ { j } , \mu _ { j } \rangle | c _ { 1 \cdots j - 1 } , z _ { j } ; c _ { 1 \cdots j } , \nu _ { 1 \cdots j } \rangle , & & ( 1 5 )$$

FIG. 1. Labels and fusion decomposition defining an orthonormal basis for states on genus g surfaces. The ⊗ signifies the fact that the loops are non-contractible on the genus g surface.

<!-- image -->

with c 1 ··· g = 0 and c 1 = z 1 . This corresponds to the diagram shown in Fig. 1. The symmetry action on a state | ψ ⟩ is then

$$| \psi \rangle \rightarrow \varphi ( | \psi \rangle ) ,$$

with φ acting on the basis states to give:

$$\bigotimes _ { j = 1 } ^ { g } U _ { \varphi } ^ { - 1 } ( a _ { j } ^ { \prime } , \overline { a _ { j } ^ { \prime } } ; 0 ) [ U _ { \varphi } ( a _ { j } ^ { \prime } , \overline { a _ { j } ^ { \prime } } ; z _ { j } ^ { \prime } ) ] _ { \mu , j _ { 1 } , \mu _ { j } } [ U _ { \varphi } ( c _ { 1 \cdots j - 1 } ^ { \prime } ; z _ { j } ^ { \prime } ; c _ { 1 \cdots j } ^ { \prime } ) ] _ { \nu _ { 1 \cdots j } , \nu _ { 1 \cdots j } , | a _ { j } ^ { \prime } ; \overline { a _ { j } ^ { \prime } } ; z _ { j } ^ { \prime } , \mu _ { j } } ) | \langle c _ { 1 \cdots j - 1 } ^ { \prime } , z _ { j } ^ { \prime } ; c _ { 1 \cdots j } ^ { \prime } , \nu _ { 1 \cdots j } \rangle , \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ ]$$

with a sum over µ j and ν 1 ··· j implied.

For soft symmetries, the states on a genus g = 1 surface transform trivially:

$$\varphi ( | a , \bar { a } ; 0 \rangle ) = | a , \bar { a } ; 0 \rangle .$$

For the genus g = 2 surface, a soft symmetry transforms the states as

$$\varphi ( | a _ { 1 } , \overline { a _ { 1 } } ; z _ { 1 } , \mu _ { 1 } ^ { \prime } ) | a _ { 2 } , \bar { a } _ { 2 } ; \bar { z } _ { 1 } , \mu _ { 2 } ^ { \prime } ) & = \frac { [ U _ { \varphi } ( a _ { 1 } , \bar { a } _ { 1 } ; z _ { 1 } ) ] _ { \mu _ { 1 } ^ { \prime } , \mu _ { 2 } } [ U _ { \varphi } ( a _ { 2 } , \bar { a } _ { 2 } ; \overline { z } _ { 1 } ) ] _ { \mu _ { 2 } ^ { \prime } , \mu _ { 2 } } U _ { \varphi } ( z _ { 1 } , \bar { z } _ { 1 } ; 0 ) } { U _ { \varphi } ( a _ { 1 } , \bar { a } _ { 1 } ; 0 ) U _ { \varphi } ( a _ { 2 } , \bar { a } _ { 2 } ; 0 ) } | a _ { 1 } , \overline { a } _ { 1 } ; z _ { 1 } , \mu _ { 1 } \rangle | a _ { 2 } , \bar { a } _ { 2 } ; \bar { z } _ { 1 } \rangle \\$$

It is straightforward to verify that in general the symmetry action on every basis state is unchanged by a natural isomorphism. Therefore, the symmetry action only depends on the equivalence class [ φ ]. This implies that if a braided autoquivalence φ acts as the identity on the space of states on a torus while it acts non-trivially on surfaces of genus g ≥ 2, then it must be a non-trivial soft symmetry.

## D. 2-group symmetry and H 3 (Aut( C ) , A ) class

The group of braided tensor autoequivalences defines an element of a 3rd cohomology group, [ O 3 ] ∈ H 3 (Aut br ( C ) , A ), where A is a finite Abelian group defined by fusion of the Abelian anyons in C [3, 40]. Formulas to compute [ O 3 ] from the U -symbols were presented in [3]. Graphically, we can understand [ O 3 ] as a failure of associativity for fusing the codimension-1 sheets. Consider three symmetries [ φ 1 ], [ φ 2 ], [ φ 3 ] ∈ Aut br ( C ) and the junctions formed by fusing the sheets as φ 1 ◦ ( φ 2 ◦ φ 3 ) compared with ( φ 1 ◦ φ 2 ) ◦ φ 3 . As we deform from the first order to the second, an Abelian anyon O 3 ([ φ 1 ] , [ φ 2 ] , [ φ 3 ]) ∈ A is emitted from the resulting transition point in space-time. See Fig. 2 for an illustration. We see how [ O 3 ] can be viewed as an obstruction to associativity of the symmetry operations [3].

The data (Aut br ( C ) , A , [ O 3 ]) defines a 2-group Aut br ( C ) that acts on the UMTC C [3, 41]. An example of a theory with non-trivial [ O 3 ] was discussed in [3, 42], with generalizations where the symmetry is anti-unitary [43].

## E. Symmetry fractionalization

The existence of codimension-1 topological defects naturally leads to the possibility of codimension-2 junctions between different codimension-1 defects. In order to characterize the interaction between the anyon worldlines and these junctions, we need to introduce additional data, referred to as η -symbols [3]. These are depicted graphically as follows:

<!-- image -->

where φ , ϑ label two braided tensor autoequivalences.

By considering the fusion of 3 codimension-1 symmetry defects, Fig. 3 illustrates how η satisfies the equation

$$\eta _ { \varphi _ { 1 } ( x ) } ( \varphi _ { 2 } , \varphi _ { 3 } ) \eta _ { x } ( \varphi _ { 1 } , \varphi _ { 2 3 } ) = M _ { x , O _ { 3 } } \eta _ { x } ( \varphi _ { 1 } , \varphi _ { 2 } ) \eta ( \varphi _ { 1 2 } , \varphi _ { 3 } ) ,$$

where φ jk denotes φ i ◦ φ j , and M xa denotes the U (1) phase resulting from a double braid of x with an Abelian anyon a ∈ A . If [ O 3 ] is trivial in group cohomology H 3 (Aut br ( C ) , A ) twisted by the action of Aut br ( C ) on A , then there are inequivalent choices of the η symbols, which form a torsor over the twisted cohomology H 2 (Aut br ( C ) , A ).

The η -symbols are referred to as the symmetry fractionalization data of the theory, because they specify how the anyons carry fractional quantum numbers under the symmetry group elements. For example, they can be used to characterize the fractional electric charge of anyons in the FQH effect or fractional spin of spinons in quantum spin liquids [44]. Assuming the [ O 3 ] is trivial in H 3 (Aut br ( C ) , A ), the η symbols further determine an 't Hooft anomaly [ O 4 ] ∈ H 4 (Aut br ( C ) , U (1)) [3, 40, 45-47].

FIG. 2. A point junction of the three symmetry defects emits an Abelian anyon O 3 ( φ 1 , φ 2 , φ 3 ) ∈ A . This represents the 2-group structure formed by the 0-form symmetries and the Abelian anyons.

<!-- image -->

## F. Global symmetry G of quantum many-body system

Consider a microscopic quantum many-body system with a global 0-form symmetry group G . If the system forms a gapped phase with anyons described by a UMTC C , then the possible symmetry-enriched topological phases will be partially characterized by a group homomorphism from the microscopic (UV) symmetry to the emergent (IR) symmetry,

$$[ \rho ] \colon G \to A u t _ { b r } ( \mathcal { C } ) .$$

$$U _ { g } ( a , b ; c ) = U _ { \rho ( \mathfrak { g } ) } ( a , b ; c ) .$$

The group homomorphism [ ρ ] can be pulled back to determine a cohomology class [ ρ ] ∗ [ O 3 ] ∈ H 3 ( G, A ), which is an obstruction for the η symbols of G to satisfy associativity. Let us assume that [ ρ ] ∗ [ O 3 ] is trivial.

Symmetry fractionalization associated to junctions of codimension-1 symmetry defects of G are given by

$$\eta _ { x } ( g , \mathbf h ) = M _ { x , t ( g , \mathbf h ) } \eta _ { x } ( \rho ( g ) , \rho ( \mathbf h ) ) ,$$

For each g ∈ G , there will be a U -symbol where [ t ] ∈ H 2 ( G, A ). Therefore, the possible choices of symmetry fractionalization for G factor through those for Aut br ( C ), with an additional freedom specified by [ t ]. The above data can be viewed as specifying a 2-homomorphism from G , viewed as a 2-group G with trivial 1-form symmetry, to Aut br ( C ):

FIG. 3. The anyon x crossing through a pair of tri-junctions of symmetry defects. Initially x is crossing the three defects φ 1 , φ 2 , φ 3 , and finally x crosses a single defect φ 123 . There are two ways to arrive at the final configuration; passing x along the top or bottom of the picture. The phase factor for each path is represented by the thick blue arrow. Equating the phase factors for consistency results in (20).

<!-- image -->

$$\underline { \rho } \colon \underline { G } \to \underline { A u t _ { b r } ( \mathcal { C } ) } . \\ \\ \underline { \rho } \cdot \underline { G } = \underbrace { \underline { A u t _ { b r } ( \mathcal { C } ) } } _ { \longrightarrow } .$$

If [ ρ ] ∗ [ O 3 ] is non-trivial, then the theory is incompatible with an ordinary global G symmetry. Instead we must consider a system with a non-trivial 2-group symmetry G = ( G, A , [ ρ ] , [ ρ ] ∗ [ O 3 ]). In this sense [ ρ ] ∗ [ O 3 ] is an obstruction to having the symmetry be an ordinary group G .

As mentioned above, the symmetry fractionalization data determines an element [ O 4 ] ∈ H 4 (Aut br ( C ) , U (1)), which in the field theory literature is referred to as the 't Hooft anomaly. This induces an 't Hooft anomaly for G via the pullback [ O 4 ,G ] = [ ρ ] ∗ [ O 4 ] ×O 4 , rel [ t ], where O 4 , rel [ t ] is an additional contribution, referred to as a relative anomaly [46], determined by the choice [ t ], along with the η and U symbols for Aut br ( C ). General methods to compute these anomalies were discussed in [3, 40, 45-47].

Note that the complete invertible symmetry of a UMTC is a 3-groupoid, Aut br ( C ). 3 SETs with symmetry group G are completely distinguished by a 3-homomorphism ρ : G → Aut br ( C ). See [3, 40, 48] for additional details.

## III. SOFT SYMMETRY FROM GAUGED SPT DEFECTS

## A. Review: gauged SPT defects

Finite G topological gauge theory is defined by the following partition function on a space-time manifold M d +1 :

$$\text {gauge the theory is determined by the following partition function on a space-time manifold $M_{d+1}$.} \\ Z ( M _ { d + 1 } ) = \mathcal { N } ^ { - 1 } \sum _ { [ a ] \in \text {Hom} ( \pi _ { 1 } ( M _ { d + 1 } ) , G ) / G } e ^ { i \int _ { M _ { d + 1 } } \omega _ { d + 1 } } . \\ \text {Gauge field and the sum is over all gauge incomming constant non-trivial flat $G$ gauge fields} \ \omega _ { d + 1 } \in \mathcal { G }$$

Here a is a flat G gauge field and the sum is over all gauge inequivalent non-trivial flat G gauge fields. ω d +1 ∈ Z n ( BG,U (1)) is the Dijkgraaf-Witten twist [49], and we leave implicit the pullback to Z n ( M d +1 , U (1)) using a . In the following discussion, we assume that ω d +1 is trivial and we comment on non-trivial ω d +1 at the end.

The above TQFT generally has finite invertible symmetries generated by operators called gauged SPT defects [24, 50]. These symmetry defects are defined by the SPT topological response with support on the submanifolds where the defects are located. Namely, the topological defect in an n -dimensional submanifold M n embedded in ( d +1)D spacetime is defined as

$$e ^ { i \int _ { M _ { n } } \omega ( a ) } ,$$

3 This is referred to as a categorical 2-group in [40].

where ω ∈ Z n ( BG,U (1)) is the topological response of a G -SPT phase in n space-time dimensions [49, 51], and a is the G gauge field. From the perspective of the partition function, the above operator is a symmetry because it can be inserted in the sum in the partition function and the result is independent of smooth deformations of the location of M n ⊂ M d +1 , as long as they are away from other defects. From the lattice model perspective that we introduce in the subsequent section, the action of this gauged SPT operator can be understood as pumping the SPT phase through the space by the action of a finite depth local unitary quantum circuit.

The gauged SPT defects generally act on the codimension-2 magnetic defects of the G gauge theory that correspond to fluxes. For instance, the 0-form symmetry (26) with n = d acts on the magnetic fluxes by permuting codimension-2 topological defects. When the magnetic flux V [ g ] is labeled by the conjugacy class [ g ] with g ∈ G , the gauged SPT defect acts by the automorphism of symmetry defects as

$$V _ { [ g ] } ( M _ { d - 1 } ) \rightarrow V _ { [ g ] } ( M _ { d - 1 } ) = V _ { [ g ] } ( M _ { d - 1 } ) \times e ^ { i \int _ { M _ { d - 1 } } i _ { g } \omega } \ .$$

One can use a specific gauged SPT defect to define a soft auto-equivalence of G gauge theory in (2+1)D. When ∫ ω is trivial on a torus, the slant product of the cocycle ω ∈ Z 2 ( BG,U (1)) is trivial in cohomology. Therefore a gauged SPT defect with such an ω does not permute anyons and defines a soft auto-equivalence. Such a soft auto-equivalence was first found by Davydov in [31].

Here i g is the slant product defined through the circle compactification of the SPT response, i g ω := ∫ S 1 g ω . Note that when G is non-Abelian and ω ∈ Z n ( BG,U (1)) , i g ω ∈ Z n -1 ( BZ ( g ) , U (1)), where Z ( g ) ⊂ G is the centralizer of G . This reflects that the flat G gauge field on M n -1 × S 1 g must have the holonomy in Z ( g ) along any cycle of M n -1 . In (2+1)D gauge theories with d = 2, this action is understood as the permutation of anyons. See Fig. 4 (a).

The gauged SPT defects also act on the junctions of the magnetic defects. For instance, in (2+1)D gauge theories suppose we have an operator corresponding to a network of magnetic fluxes. Then the gauged SPT defect acts nontrivially on the junctions of two magnetic fluxes [ g ] , [ h ] ∈ Cl ( G ) into [ gh ], where Cl ( G ) denotes the set of conjugacy classes of G . The 0-form symmetry generated by the (1+1)D gauged SPT defect acts on this junction by a phase factor exp( iω ( g, h )), since the SPT response evaluates nontrivially at this junction of G defects. This implies that the symmetry operator acts on the junction of magnetic fluxes by a phase U ω given by

$$\mathcal { U } _ { \omega } ( [ g ] , [ h ] ; [ g h ] ) = e ^ { i \omega ( g , h ) } \ ,$$

which is valid when ω ( g, h ) is invariant under overall conjugation by group elements, ω ( g, h ) = ω ( kgk -1 , khk -1 ), so that the above action does not depend on the choices of the representatives in the conjugacy classes. See Fig. 4 (b).

When the gauged SPT defect does not permute anyons, the above phase factor U ω leaves the F symbols invariant, which follows from the cocycle condition of satisfied by ω . When the cocycle ω ∈ Z 2 ( BG,U (1)) is deliberately chosen such that the above phases U ω also leaves the R symbols invariant, we identify the phase U ω with the U symbol of the soft braided auto-equivalence,

$$U ( [ g ] , [ h ] ; [ g h ] ) = \mathcal { U } _ { \omega } ( [ g ] , [ h ] ; [ g h ] ) \ .$$

We will verify this formula explicitly in Sec. IV in the context of a lattice model and a particular example of a gauged SPT. Meanwhile, the junction of the SPT defects acts trivially on the magnetic fluxes, so we have η = 1.

In general, the gauged SPT defects with distinct dimensions combined with the magnetic defects of the G gauge theory form the algebraic structure of a higher fusion category. See [50] for detailed discussions.

Below, we will discuss a physical perspective of such soft auto-equivalences in detail.

## B. Soft autoequivalence of finite gauge theory

Suppose that the braided fusion category is given by a (2+1)D finite gauge theory C = Z (Vec( G )), where Z (Vec( G )) denotes the Drinfeld center of Vec( G ). Its simple anyons are labeled by a pair

$$( [ g ] , \pi ) \, ,$$

where [ g ] ∈ Cl ( G ) is a conjugacy class of G that specifies the magnetic flux, and π ∈ Rep( Z ( G )) is the irreducible representation that corresponds to the electric charge.

Then, a subgroup of the soft braided auto-equivalence Aut sf ( C ) has the structure of

$$O u t _ { s f } ( G ) \ltimes H _ { s f } ^ { 2 } ( B G , U ( 1 ) ) \subset A u t _ { s f } ( \mathcal { C } ) \ .$$

FIG. 4. The action of a gauged SPT defect on magnetic defects. (a): The 0-form symmetry generated by the gauged SPT defect acts on the magnetic defect by attaching the ( d -1)D gauged SPT defect to the magnetic defect. This can be understood as the twisted compactification of SPT with respect to the circle with holonomy g ∈ G . (b): The 0-form gauged SPT defect in ( d +1)D spacetime acts on a point junction of the ( d -1) magnetic defects by a phase factor given by the SPT cocycle. The figure shows the case of d = 2, where the (1+1)D SPT defect acts on the junction of two magnetic defects by a 2-cocycle ω ( g, h ).

<!-- image -->

- Out sf ( G ) is a subgroup of the outer automorphism Out( G ) that preserves the conjugacy class of any commuting pair g, h ∈ G . In [31], such outer automorphisms are referred to as doubly class preserving outer automorphisms. Given that the G gauge field on a torus is labeled by the commuting pair of groups, Out sf ( G ) corresponds to the symmetry that trivially acts on the torus Hilbert space. Hence this subgroup does not permute anyons. See [31, 52, 53] for examples of such outer automorphisms.
- H 2 sf ( BG,U (1)) is a subgroup of group cohomology H 2 ( BG,U (1)), given by a set of ω ∈ H 2 ( BG,U (1)) whose integral on a torus with any flat G gauge field becomes trivial, ∫ T 2 ω = 0 mod 2 π Z . The symmetry H 2 ( BG,U (1)) is generated by gauged SPT defects, and H 2 sf ( BG,U (1)) corresponds to the ones acting trivially on the torus Hilbert space.

Let us provide an example of finite gauge theory which has the soft symmetry. We consider the untwisted (2+1)D gauge theory with gauge group G = G sf , where G sf is a group with order 128, defined by the following group algebra involving order-2 elements p, q, r 1 , r 2 , x, y 1 , y 2 [31, 54],

$$p q ^ { - 1 } & = x , \\ r _ { 1 } r _ { 2 } r _ { 1 } ^ { - 1 } r _ { 2 } ^ { - 1 } & = x , \\ p r _ { 1 } p ^ { - 1 } r _ { 1 } ^ { - 1 } & = y _ { 1 } , \ \ p r _ { 2 } p ^ { - 1 } r _ { 2 } ^ { - 1 } = y _ { 2 } , \\ q r _ { 1 } q ^ { - 1 } r _ { 1 } ^ { - 1 } & = q r _ { 2 } q ^ { - 1 } r _ { 2 } ^ { - 1 } = 1 . \\$$

This group G sf is regarded as a central extension ( Z 2 ) 3 → G sf → ( Z 2 ) 4 , where ( Z 2 ) 3 is generated by { x, y 1 , y 2 } and ( Z 2 ) 4 is generated by { p, q, r 1 , r 2 } . Let n p , n q ∈ Z 1 ( G sf , Z 2 ) be the Z 2 cocycle such that n p ( g ) (resp. n q ( g )) for g ∈ G sf gives the mod 2 number of the element p (resp. q ) that appears in the expression of g in terms of the multiplication of generators p, q, r 1 , r 2 , x, y 1 , y 2 .

We then consider the codimension-1 gauged SPT defect generated by the (1+1)D G sf -SPT phase with the action given by a 2-cocycle

$$\omega _ { p q } = \pi ( n _ { p } \cup n _ { q } ) \in Z ^ { 2 } ( B G _ { s f } , U ( 1 ) ) \\$$

where the factor π originates from the 2 π periodicity of U (1). This generates the Z 2 0-form symmetry of the (2+1)D G sf gauge theory. With the above choice of cocycle representative of H 2 ( BG sf , U (1)), the action on the anyon junctions are given by the phase factor

$$\mathcal { U } _ { p q } ( ( [ g _ { 1 } ] , \pi _ { 1 } ) , ( [ g _ { 2 } ] , \pi _ { 2 } ) ; ( [ g _ { 3 } ] , \pi _ { 3 } ) ) = e ^ { i \omega _ { p q } ( g _ { 1 } , g _ { 2 } ) } , \\$$

where we label the anyon by the conjugacy class [ g j ] with g j ∈ G sf and the irreducible representation of the centralizer group π j ∈ Rep( Z ( g j )). Note that the above phase U pq does not depend on the choice of representatives of the conjugacy class. We will later see that this symmetry does not permute anyons. As required by (11), the symmetry action leaves the F symbol invariant, which is seen from the cocycle condition of group cohomology satisfied by U pq .

However, the above phase U pq presented in (34) does not leave the R symbols invariant. It transforms the R symbol into

$$R _ { ( [ g _ { 3 } , \pi _ { 3 } ) } ^ { ( ( g _ { 1 } , \pi _ { 1 } ) , ( [ g _ { 2 } ] , \pi _ { 2 } ) } \rightarrow \exp \left ( i ( \omega _ { p q } ( g _ { 1 } , g _ { 2 } ) - \omega _ { p q } ( g _ { 2 } , g _ { 1 } ) ) \right ) R _ { ( [ g _ { 3 } ] , \pi _ { 3 } ) } ^ { ( [ g _ { 1 } ] , \pi _ { 1 } ) , ( [ g _ { 2 } ] , \pi _ { 2 } ) }$$

In particular, when g 1 = p, g 2 = q the R symbol is transformed into -R , so it does not satisfy (12). Meanwhile, one can find another representative ω sf ∈ Z 2 ( BG sf , U (1)) in the same cohomology class as ω pq , i.e., [ ω sf ] = [ ω pq ] ∈ H 2 ( BG sf , U (1)) and symmetric as a function of g, h ; ω sf ( g, h ) = ω sf ( h, g ) for any g, h ∈ G sf . We will explicitly construct such a cocycle representative in Appendix A. With this new choice of 2-cocycle, the action on fusion vertices are given by

$$U _ { s f } ( ( [ g _ { 1 } ] , \pi _ { 1 } ) , ( [ g _ { 2 } ] , \pi _ { 2 } ) ; ( [ g _ { 3 } ] , \pi _ { 3 } ) ) = e ^ { i \omega _ { s f } ( g _ { 1 } , g _ { 2 } ) } ,$$

and this phase action leaves both F , R symbols invariant, being consistent with (11), (12). From now, we will use U sf as the data of the braided tensor auto-equivalence. This symmetry is regarded as the vertex basis gauge transformation with the matrices given by the phases Γ = U sf . The symmetry does not permute anyons, while as demonstrated below, this vertex gauge transformation is not a natural isomorphism. In other words, this Z 2 symmetry is a soft symmetry. Below, let us summarize the notable properties of this Z 2 symmetry:

- The Z 2 symmetry does not induce the permutation of anyons. To see this, recall that the SPT defects ω 2 acts on the magnetic flux [ g ] by attaching an electric charge given by the slant product i g ω 2 ∈ Rep( Z ( g )). The slant product is related to the torus partition function through i g ω 2 ( h ) = Z SPT ( T 2 ( g, h )), where T 2 ( g, h ) denotes a torus with the holonomy g, h ∈ G sf on each cycle. For the cocycle ω sf , the slant product is trivial since the torus partition function with any flat G sf gauge field becomes trivial, Z SPT = 1. For instance, if n p ( g ) = 1 on a torus T 2 ( g, h ), h needs to satisfy n q ( h ) = 0 due to ghg -1 h -1 = 1, so the integral of ω sf (which is identical to the integral of ω pq ) vanishes. This leads to the trivial permutation action by the symmetry.
- This Z 2 soft symmetry is faithful in the sense that it acts by a non-trivial operator on the Hilbert space supported on a genus g ≥ 2 surface. For instance, the action on the genus 2 surface with the anyon diagrams a 1 = [ p ] , a 2 = [ r 1 ] , z = [ x ] in Fig. 1 is given by

$$\tau _ { 1 } = [ p ; [ 2 , 2 ] = [ 1 , 2 ] ; [ x ] = 1 ] ; & \text {gives by} \\ \varphi _ { s f } ( | [ p ] ; [ p ] ; [ x ] ) | [ r _ { 1 } ] , [ r _ { 1 } ] ; [ x ] ) & = \frac { U _ { s f } ( [ p ] , [ p ] ; [ x ] ) U _ { s f } ( [ r _ { 1 } ] , [ r _ { 1 } ] ; [ x ] ) U _ { s f } ( [ x ] , [ x ] ; 0 ) } { U _ { s f } ( [ p ] , [ p ] ; 0 ) U _ { s f } ( [ r _ { 1 } ] , [ r _ { 1 } ] ; 0 ) } | [ p ] , [ p ] ; [ x ] | [ r _ { 1 } ] , [ r _ { 1 } ] ; [ x ] \\ & = \frac { \exp \left ( i ( \omega _ { s f } ( p , p x ) + \omega _ { s f } ( r _ { 1 } , r _ { 1 } x ) + \omega _ { s f } ( x , x ) ) \right ) } { \exp \left ( i ( \omega _ { s f } ( p , p ) + \omega _ { s f } ( r _ { 1 } , r _ { 1 } ) ) \right ) } | [ p ] , [ p ] ; [ x ] | [ r _ { 1 } ] , [ r _ { 1 } ] ; [ x ] \right ) \\ & = - | [ p ] , [ p ] ; [ x ] | [ r _ { 1 } ] , [ r _ { 1 } ] ; [ x ] \} \\ \intertext { which can be explicitly computed by using \omega _ { s f } presented in Appendix A. Since the above eigenvalue is invariant }$$

which can be explicitly computed by using ω sf presented in Appendix A. Since the above eigenvalue is invariant under the natural isomorphisms, this nontrivial invariant ( -1) implies that this soft Z 2 symmetry corresponds to a nontrivial braided tensor auto-equivalence which cannot be given by natural isomorphisms. In Sec. IV, this Z 2 symmetry will be realized in a non-Pauli stabilizer model of qubits. Therefore, this Z 2 symmetry gives a non-trivial logical gate of the stabilizer code that does not permute anyons.

- We have η = 1, meaning that the anyons do not carry fractional charge under the Z 2 symmetry.
- This Z 2 soft symmetry can be gauged. The Z 2 gauge field A for the soft symmetry is introduced by the action ∫ A ∪ ω sf , so the resulting gauge theory is the G sf × Z 2 gauge theory with the Dijkgraaf-Witten twist given by A ∪ ω sf ∈ H 3 ( B ( G sf × Z 2 ) , U (1)). Note that this theory is distinct from the untwisted G sf × Z 2 gauge theory. For instance, in the twisted gauge theory the magnetic defect of the Z 2 soft symmetry becomes non-invertible. This is because it corresponds to the endpoint of the (1+1)D gauged SPT, which carries the projective representation of G sf symmetry characterized by ω sf ∈ H 2 ( BG sf , U (1)).

While we discussed the soft symmetry in the untwisted G sf gauge theory, this soft Z 2 symmetry is present in G sf gauge theory with a Dijkgraaf-Witten twist ω 3 [49] as well, as long as the 2-cocycle ω sf is not expressed as a slant product of ω sf = i g ω 3 with some g ∈ G sf . When ω sf is the slant product, this SPT defect is bounded by the topological line operator of the magnetic flux. Concretely, suppose ˜ a is the dual gauge field for g ∈ G sf , meaning exp ( i ∫ ˜ a ) gives the line operator for the magnetic defect. We then have d ˜ a = i g ω 3 mod 2 π Z . 4 This means that the surface operator exp ( i ∫ ω sf ) is bounded by the g magnetic defect when i g ω 3 = ω sf mod 2 π Z . Since ω sf is a coboundary, exp ( i ∫ ω sf ) does not generate a faithful 0-form symmetry [50].

4 More precisely, we have d ˜ a = A ∗ ( i g ω 3 ) where A : M 3 → BG sf is the background G sf gauge field on the spacetime M 3 .

FIG. 5. The edges nearby a vertex v and face f .

<!-- image -->

Also, we note that (2+1)D finite gauge theories can have a 'softer' 0-form symmetry, which acts trivially on the Hilbert space of a genus &lt; g surface, but acts non-trivially on the genus g surface. Such a global symmetry can be generated by the gauged SPT defects, where the SPT can only be detected by its partition function on higher genus surfaces. Such examples are explicitly constructed in Appendix B. It would be interesting to see if such softer symmetry can also arise from the outer automorphisms of gauge groups.

## IV. LATTICE MODEL

## A. Quantum double model

The above Z 2 symmetry action on the G sf gauge theory can be explicitly demonstrated on the quantum double model [55]. The lattice model can be defined on generic triangulations of a 2d surface. For simplicity, let us consider a square lattice with seven qubits at each edge. One can describe the (2+1)D quantum double model with the gauge group G sf in this setup.

The local Hilbert space on each edge has | G sf | = 2 7 dimensions, whose basis states {| g ⟩} are labeled by group elements g ∈ G sf . The Hamiltonian is given by

with each term given by

$$H _ { G _ { s f } } = - \sum _ { v } A _ { v } - \sum _ { f } B _ { f }$$

$$A _ { v } = \frac { 1 } { | G _ { s f } | } \sum _ { g \in G _ { s f } } \overrightarrow { X } _ { N ( v ) } ^ { g } \overrightarrow { X } _ { E ( v ) } ^ { g } \overleftarrow { X } _ { W ( v ) } ^ { g ^ { - 1 } } \overleftarrow { X } _ { S ( v ) } ^ { - 1 } , \ \ B _ { f } = \delta _ { g _ { 0 1 } g _ { 1 3 } g _ { 2 3 } ^ { - 1 } g _ { 0 2 } ^ { - 1 } , 0 } \, .$$

Here we defined the Pauli X like operators as

$$\overrightarrow { X } ^ { g } \left | h \right \rangle & = \left | g h \right \rangle , \quad \overleftarrow { X } ^ { g ^ { - 1 } } \left | h \right \rangle = \left | h g ^ { - 1 } \right \rangle \, . \\ \intertext { a \text { pair } g \, = \, \left ( ( p , q , r _ { 1 } , r _ { 2 } ) , \left ( x , y _ { 1 } , y _ { 2 } \right ) \right ) \text { with } \left ( p , q , r _ { 1 } , r _ { 2 } \right ) \in \mathbb { Z } _ { 2 } ^ { 4 } , ( x , y _ { 1 } , y _ { 2 } ) \in \mathbb { Z } _ { 2 } ^ { 3 } , \, \text {satisfying} } \intertext { \text {law} } \text {when} \, \text { we express the local Hilbert space with seven qubits} \, \text { the above labels}$$

We label g ∈ G sf by a pair g = (( p, q, r 1 , r 2 ) , ( x, y 1 , y 2 )) with ( p, q, r 1 , r 2 ) ∈ Z 4 2 , ( x, y 1 , y 2 ) ∈ Z 3 2 , satisfying the group multiplication law (32). When we express the local Hilbert space with seven qubits, the above labels (( p, q, r 1 , r 2 ) , ( x, y 1 , y 2 )) are identified as the eigenvalues of the Pauli Z operators as

$$Z ^ { ( j ) } = ( - 1 ) ^ { \alpha _ { j } } \ \ ( 1 \leq j \leq 7 )$$

where { α j } = ( p, q, r 1 , r 2 , x, y 1 , y 2 ). The above quantum double model is regarded as a non-Pauli (Clifford) stabilizer model of qubits.

The symmetry R Z 2 is then represented as the product of CZ operators

$$\mathcal { R } _ { \mathbb { Z } _ { 2 } } = \prod _ { f = ( 0 1 2 3 ) } C ( Z _ { 0 1 } ^ { ( 1 ) } , Z _ { 1 3 } ^ { ( 2 ) } ) C ( Z _ { 0 2 } ^ { ( 1 ) } , Z _ { 2 3 } ^ { ( 2 ) } ) .$$

where the subscripts 01 , ... label the edges of a face (0123), see Fig. 5. C ( Z, Z ′ ) means the controlled-Z operator involving two Pauli Z operators Z, Z ′ . This operator on each face f is regarded as evaluating ω pq = π ( n p ∪ n q ) on a face,

$$\mathcal { R } _ { \mathbb { Z } _ { 2 } } = \prod _ { f = ( 0 1 2 3 ) } e ^ { i \omega _ { p q } ( 0 1 2 3 ) }$$

since ω pq (0123) = π ( n p (01) n q (13)+ n p (02) n q (23)). 5 Therefore, this operator corresponds to the action of the gauged SPT operator e i ∫ ω pq acting on the flat G sf gauge fields on a 2d space. R Z 2 remains unchanged on a closed surface if we use a different cocycle representative for ω . In particular, since we have [ ω pq ] = [ ω sf ] in cohomology H 2 ( BG sf , U (1)), the above R Z 2 can also be expressed as R Z 2 = ∏ f =(0123) e iω sf (0123) , which corresponds to an alternative way of decomposing the finite depth circuit R Z 2 into local unitaries.

One can define the operator R Z 2 in the form of (43) on generic triangulation in 2d equipped with branching structure, where the operator is expressed as

$$\mathcal { R } _ { \mathbb { Z } _ { 2 } } = \prod _ { \Delta = ( 0 1 2 ) } ( - 1 ) ^ { n _ { p } ( 0 1 ) n _ { q } ( 1 2 ) } \, ,$$

where the product is over 2-simplices of the space.

The operator R Z 2 commutes with the Hamiltonian within the Hilbert space satisfying B f = 1 for any faces. First of all, it is obvious that R Z 2 commutes with B f itself. Then, the action of R Z 2 on the X stabilizers are given by

$$\mathcal { R } _ { \mathcal { Z } _ { 2 } } ( \vec { X } _ { N ( v ) } ^ { g } \overrightarrow { X } _ { E ( v ) } ^ { g } \overleftarrow { X } _ { W ( v ) } ^ { - 1 } \overleftarrow { X } _ { S ( v ) } ^ { g ^ { \dagger } } ) \mathcal { R } _ { \mathcal { Z } _ { 2 } } ^ { \dagger } = ( \vec { X } _ { N ( v ) } ^ { g } \overrightarrow { X } _ { E ( v ) } ^ { g } \overleftarrow { X } _ { W ( v ) } ^ { - 1 } \overleftarrow { X } _ { S ( v ) } ^ { g ^ { - 1 } } ) \prod _ { e \subset J _ { W } } Z _ { e } ^ { ( 1 ) } \prod _ { e \subset f _ { n e } } Z _ { e } ^ { ( 2 ) }$$

where f ws (resp. f ne ) is the face bounded by two edges W ( v ) , S ( v ) (resp. N ( v ) , E ( v )). The above product of Pauli Z operators becomes trivial when B f = 1 is satisfied, so R Z 2 commutes with X terms of the Hamiltonian within this Hilbert space. This implies that R Z 2 generates an emergent Z 2 symmetry that preserves the ground state subspace.

## B. Trivial permutation action on anyons

The anyons of the quantum double model are created and moved using ribbon operators [55, 57]. Here we demonstrate that the Z 2 symmetry does not permute anyons by explicitly checking the symmetry action on closed ribbon operators.

Suppose we pick a conjugacy class C ∈ Cl ( G ) where Cl ( G ) denotes the set of conjugacy classes of G . We fix a representative r C ∈ C , and define Q C = { s i } as a set of group elements with | Q C | = | C | , such that for C = { c i } , s i is defined as an element satisfying c i = s i r C s i . Also, let us pick a conjugacy class D ∈ Cl ( Z ( r C )). The ribbon operator on a closed ribbon σ can be labeled by a pair { D,C } as [57]

$$K _ { \sigma } ^ { D C } = \sum _ { s \in Q _ { C } } \sum _ { k \in D } F _ { \sigma } ^ { s r _ { C } \bar { s } , s k \bar { s } }$$

which uses the building block of ribbon operators F h,g shown in Fig. 6. This operator F h,g generates the h ∈ G gauge transformation along the dual edges cutting the ribbon, and associated with the projection onto the holonomy g ∈ G along the ribbon.

Then, using an irrep R ∈ Rep( Z ( r C )) one can express the ribbon operators in the standard basis

$$K _ { \sigma } ^ { R C } = \frac { \dim ( R ) } { | Z ( r _ { C } ) | } \sum _ { D \in C l ( Z ( r _ { C } ) ) } \bar { \chi } _ { R } ( D ) K _ { \sigma } ^ { D C } \, ,$$

where C labels the magnetic flux, and R labels the electric charge attached to it. This corresponds to the closed string of the anyon labeled by a pair ( C,R ) as introduced in (30).

5 See e.g., [56] for the details of cup product on square and hypercubic lattices.

FIG. 6. The ribbon operator of the quantum double model. The operator F h,g generates the gauge transformation h ∈ G along the dual edges cutting the ribbon, associated with the projection onto the holonomy g ∈ G along the ribbon. This can be defined on a generic curve of the dual lattice, see [55, 57] for details.

<!-- image -->

One can check that the symmetry operator R Z 2 preserves the above closed ribbons K RC σ . For instance, let us take a conjugacy class C = [ p ] where p, q ∈ G sf is introduced in (32). In that case, the Z 2 symmetry acts on K R, [ p ] σ by attaching the string of Pauli Z (2) operators parallel to the ribbon σ ,

$$\mathbb { Z } ^ { 2 } + \text {operations} \, \text {param} \, \text {to the 1-bbon} \, & \text {,} \\ \mathcal { R } _ { \mathbb { Z } _ { 2 } } K _ { \sigma } ^ { R , [ p ] } \mathcal { T } _ { \mathbb { Z } _ { 2 } } ^ { \dagger } = \left ( \prod _ { e \in \sigma } Z _ { e } ^ { ( 2 ) } \right ) K _ { \sigma } ^ { R , [ p ] } \\$$

The string of Z (2) measures the holonomy of q ∈ G sf along the ribbon σ . Here, each ribbon K D, [ p ] σ involves a projection of holonomy onto some group element sks with k ∈ Z ( p ). Since sks must contain even number of q ∈ G sf in its expression (i.e., n q ( sks ) = 0 mod 2), the product of Z (2) must evaluate trivially after such projection. Therefore we have

$$\mathcal { R } _ { \mathbb { Z } _ { 2 } } K _ { \sigma } ^ { R , [ p ] } \mathcal { R } _ { \mathbb { Z } _ { 2 } } ^ { \dagger } = K _ { \sigma } ^ { R , [ p ] }$$

hence it preserves the closed ribbon operator. Similar logic is also valid for other choices of C ∈ Cl ( G sf ).

## C. Symmetry action on anyon junctions

Though the Z 2 symmetry does not permute anyons, the Z 2 symmetry acts on the junction of anyon line operators. Let us consider the closed network of the ribbon operators that involves the tri-junctions of the ribbons. This can be regarded as a network of magnetic fluxes, where we have the operator - → X g along each dual edge cutting the network. Three ribbon operators carrying the magnetic fluxes g, h, gh ∈ G sf can meet at a junction which is a single triangular face. See Fig. 7 (a) for an example.

Let us pick a set of dual edges on which the magnetic flux g ∈ G sf has an odd number of p ∈ G sf in its expression, i.e., n p ( g ) = 1 mod 2. This gives a set of closed curves σ p contained in the network. Let us similarly define a set of closed curves σ q for q ∈ G sf . See Fig. 7 (b). Then, the ribbon operator network K has to include the projector onto the holonomy satisfying n q ( g ) = 0 along each closed curve of σ p , and holonomy with n p ( g ) = 0 along each closed curve of σ q . Similar to the closed ribbon operators introduced in (46), such projections are necessary to make the gauge transformations along the closed network well-defined. With this in mind, the Z 2 action on the ribbon network is given in the form of

$$\text {form of} & \quad \mathcal { R } _ { \mathbb { Z } _ { 2 } } K \mathcal { R } _ { \mathbb { Z } _ { 2 } } ^ { \dagger } \, \alpha \left ( \prod _ { e \in \sigma _ { p } } Z _ { e } ^ { ( 2 ) } \prod _ { e \in \sigma _ { q } } Z _ { e } ^ { ( 1 ) } \right ) K = K , \\ \intertext { t h a t K has the projectors onto trivial holonomy in the last equation.  The x in the first }$$

where we used the fact that K has the projectors onto trivial holonomy in the last equation. The ∝ in the first equation means that the equation is valid only up to phase; we will shortly see that the phase is carried by each anyon junction in the network, and this phase corresponds to the symmetry action on the anyon junctions.

FIG. 7. The network of the ribbon operators, with the ribbons connected by the tri-junctions. (a): an example of the network where each ribbon carries magnetic flux labeled by the conjugacy class of G sf . (b): Closed curves σ p (resp. σ q ) are defined by picking up the ribbons carrying the magnetic flux with n p ( g ) = 1 (resp. n q ( g ) = 1.)

<!-- image -->

To fix the phase ambiguity of (50), let us consider the junction of magnetic fluxes g, h ∈ G sf into gh at a triangle (012). Most generally, the edge (01) supports an operator - → X sgs , edge (12) supports - → X tht , and edge (02) supports - → X ughu for some s, t, u ∈ G sf . Focusing on the operators nearby this junction, the action of R Z 2 can be expressed as

$$\text { for some } s , t ; \text { a } \in G _ { s f } \colon & \text { causing on the operators nearby this function, the action of } K _ { Z _ { 2 } } \text { can be expressed as} \\ & \mathcal { R } _ { Z _ { 2 } } K \mathcal { R } _ { Z _ { 2 } } ^ { \dagger } = \dots ( Z _ { ( 1 2 ) } ^ { ( 2 ) } ) ^ { n _ { p } ( g ) } \vec { X } ^ { s \vec { g } } ( Z _ { ( 0 1 ) } ^ { ( 1 ) } ) ^ { n _ { q } ( h ) } \vec { X } ^ { t \vec { t } } \vec { X } ^ { \ u g h \vec { u } } \dots \\ & = ( - 1 ) ^ { n _ { p } ( g ) n _ { q } ( h ) } \times \dots ( Z _ { ( 1 2 ) } ^ { ( 2 ) } ) ^ { n _ { p } ( g ) } ( Z _ { ( 0 1 ) } ^ { ( 1 ) } ) ^ { n _ { q } ( h ) } \vec { X } ^ { s \vec { g } } \vec { X } ^ { t \vec { t } } \vec { X } ^ { \ u g h \vec { u } } \dots \\ & = \exp ( i \omega _ { p q } ( g , h ) ) \times \dots ( Z _ { ( 1 2 ) } ^ { ( 2 ) } ) ^ { n _ { p } ( g ) } ( Z _ { ( 0 1 ) } ^ { ( 1 ) } ) ^ { n _ { q } ( h ) } \vec { X } ^ { s \vec { g } } \vec { X } ^ { t \vec { t } } \vec { X } ^ { \ u g h \vec { u } } \dots \\ \intertext { by moving the Pauli Z operator to the front of the expression, we get the phase factor exp ( i \omega _ { h } ) from each }$$

so by moving the Pauli Z operator to the front of the expression, we get the phase factor exp( iω pq ( g, h )) from each tri-junction of the magnetic fluxes. Such a phase factor arises from each junction, so the action on the ribbon network is given by

$$\mathcal { R } _ { \mathcal { Z } _ { 2 } } K \mathcal { R } _ { \mathcal { Z } _ { 2 } } ^ { \dagger } = \left ( \prod _ { j u n c t i o n s } \exp ( i \omega _ { p q } ( g , h ) ) \right ) K \, , \\ \intertext { o r $ v e n t j u c t i o n s $ of m a n t i c $ f u x e s $ . $ We note that $ t a n c i s $ [ \omega _ { p q } ] = [ \omega _ { s f } ] $ in cohomology }$$

where the product is over the junctions of magnetic fluxes. We note that since [ ω pq ] = [ ω sf ] in cohomology H 2 ( BG sf , U (1)), the above action on the closed ribbon network can be expressed as

$$\text {above action on the closed rbon network can be expressed as} \\ \mathcal { R } _ { \mathcal { Z } _ { 2 } } K \mathcal { R } _ { \mathcal { Z } _ { 2 } } ^ { \dagger } = \left ( \prod _ { j u n c t i o n s } \exp ( i \omega _ { s f } ( g , h ) ) \right ) K \, , \\ \intertext { t h e U s m o b y } \text {the U symbol of the symmetry fractional data provided in (36).}$$

This is consistent with the U symbol of the symmetry fractionalization data provided in (36).

## D. Emergent symmetry and faithful action on genus g ≥ 2 surfaces

Each ground state of the quantum double model on a genus g surface can be written as a superposition over gaugeequivalent flat G gauge field configurations on the 2d space. Different ground states correspond to gauge-inequivalent gauge field configurations. The operator R Z 2 acts on each configuration of the gauge field by a phase exp ( i ∫ ω sf ) . Since the integral gives a gauge invariant partition function of the SPT, this implies that R Z 2 acts on each state by a phase factor. Since the integral ∫ ω sf vanishes on the G sf gauge field on a torus, the symmetry operator R Z 2 acts as the identity operator on the ground state subspace on a torus.

FIG. 8. The holonomy of Z 2 gauge fields on a genus 2 surface on which ∫ ω sf is nontrivial.

<!-- image -->

Meanwhile, R Z 2 defines a non-trivial operator on the ground state subspace of a genus two surface. For instance, let us consider the genus two surface where each pair of cycles carries the G sf holonomy ( p, q ), ( r 1 , r 2 ). Since pqp -1 q -1 = r 1 r 2 r -1 1 r -1 2 = x , this defines a nontrivial G sf gauge field. See Fig. 8. The operator R Z 2 then evaluates to a ( -1) phase on the state with this G sf gauge field configuration. In general, the symmetry action on the Hilbert space is a diagonal matrix with elements 1 or -1 which are partition functions of the (1+1)D ω sf SPT with the given G sf background.

## V. DISTINCT GAPPED BOUNDARIES WITH IDENTICAL CONDENSED PARTICLES

The gapped boundary condition of (2+1)D finite G gauge theory is labeled by a pair ( K,ω ); the choice of a subgroup K ⊂ G and the 2nd group cohomology ω ∈ H 2 ( K,U (1)) [25]. Here we consider two distinct gapped boundaries of the untwisted G sf gauge theory labeled by ( G sf , 0) , ( G sf , ω sf ). These two gapped boundaries correspond to condensation of the magnetic particles, with or without the Z 2 symmetry operator ω sf support at the boundary. Since the defect ω sf does not permute anyons, the two gapped boundaries have the same set of condensed particles. In other words, these two gapped boundaries have the same Lagrangian algebra object L given by

$$\mathcal { L } = \bigoplus _ { [ g ] \in C l ( G _ { \text {sf} } ) } ( [ g ] , 1 )$$

However, the set of condensed particles does not uniquely determine the gapped boundary condition. The gapped boundary is characterized by the Lagrangian algebra, which takes the Lagrangian algebra object L and the multiplication morphism µ : L ⊗ L → L [58, 59]. Due to the nontrivial action of the defect ω sf on the fusion vertices of the magnetic defects, the above two gapped boundaries have the distinct multiplication morphism µ that leads to the distinct algebraic structure. 6

Let us comment about the characterization of the Lagrangian algebra in terms of modularity. It is known that the Lagrangian algebra object L satisfies the modularity condition; suppose we have L = ⊕ a Z 0 a a with simple anyons a and non-negative coefficients { Z 0 a } , then the coefficients of the Lagrangian algebra object satisfy SZ = Z, TZ = Z with modular S, T matrices [60]. These equations are derived by putting the gapped boundary on the torus, and studying the modular invariance of the corresponding boundary state [61]. However, since the above conditions do not rely on the multiplication morphism µ , this does not give a faithful characterization of the Lagrangian algebra; it does not distinguish the gapped boundaries ( G sf , 0) and ( G sf , ω sf ). Even before that, it is known that the above modularity condition is not a sufficient condition for the Lagrangian algebra object L [62]. One can extend the above modularity conditions to the higher-genus case by considering the gapped boundary at generic Riemann surface, and studying the invariance of the corresponding boundary state under mapping class groups [61]. 7 However, such family of conditions within the genus &lt; g still does not fully characterize the Lagrangian algebra. For instance, there are (1+1)D SPT phases with a certain finite group G ( g ) sf which cannot be detected on the genus &lt; g surface, but can be detected on genus g (see Appendix B). This leads to a pair of gapped boundaries of the G ( g ) sf gauge theory ( G ( g ) sf , 0) , ( G ( g ) sf , ω ) that cannot be distinguished from the boundary state with genus &lt; g .

6 We thank Sahand Seifnashri for helpful discussions on this point.

7 Here, the boundary state is constructed by considering the TQFT on Σ g × I where Σ g is the genus g surface and I is the interval, and then one end of the interval is filled with the gapped boundary. This defines a TQFT state on Σ g on the other end, which is the boundary state. Due to the topological nature of the gapped boundary, the boundary state has to be invariant under the mapping class group actions of Σ g .

## A. Application: Oblique SSB phase of Rep( G sf ) symmetry in (1+1)D

The (2+1)D topological order and its gapped boundary are used to describe the gapped phases in (1+1)D through the symmetry TQFT [63-67]. Namely, the (1+1)D gapped phase is regarded as a (2+1)D topological order on a thin interval, and then each end of the interval is realized by a gapped boundary. The topological operators on either side of the gapped boundary generates the global symmetry of the system.

Intriguingly, the almost identical pair of gapped boundaries described above leads to the two distinct spontaneous broken phases of Rep( G sf ) symmetry, where the symmetry is completely broken. One SSB phase is given by the interval of the (2+1)D G sf gauge theory sandwiched by the same gapped boundaries ( G sf , 0) , ( G sf , 0). The other SSB phase is given by the interval sandwiched by two distinct gapped boundaries ( G sf , 0) , ( G sf , ω pq ).

These two phases have the identical set of 0-form Rep( G sf ) symmetry operators and the same local (topological) operators. The 0-form symmetry operators are described by the electric Wilson line operators of the G sf gauge theory stretching parallel to the interval. Meanwhile, the local operators are described by the magnetic defects stretching between the ends of the interval. The Rep( G sf ) symmetry operator acts on the local operators by the mutual braiding between the electric Wilson lines and the magnetic flux. Each of the Rep( G sf ) symmetry defects nontrivially acts on at least one of the local operators, and the Rep( G sf ) is maximally broken in both phases.

Nevertheless, these two phases with fully broken Rep( G sf ) are distinct phases. In particular, if one SSB phase is continuously connected to the other by a deformation preserving Rep( G sf ) symmetry, it has to go through a phase transition. This can be most easily seen by gauging the Rep( G sf ) symmetry [68], then the path connecting the SSB phases becomes the path from a trivial to nontrivial SPT phase preserving the dual G sf symmetry. This has to experience a phase transition. 8 See [69] for explicit lattice models of distinct SSB phases of Rep( G sf ) symmetry.

## VI. HIGHER DIMENSIONS: Q 8 GAUGE THEORY IN (3+1)D

We have seen that there are soft global symmetries in (2+1)D topological orders that do not permute anyons, but nontrivially acts on the junction of the anyons. In this section, we discuss an analogue of soft symmetries of topological order in higher dimensions.

Typically, it becomes easier to find such non-permuting symmetries in higher dimensions. For instance, in a standard (3+1)D Z 2 gauge theory with a bosonic electric particle, there is a Z 2 0-form symmetry that corresponds to the (2+1)D Z 2 Levin-Gu SPT phase. This SPT has slant product which is trivial in cohomology, hence leads to the trivial permutation action on the magnetic fluxes. However, this Z 2 symmetry still has the nontrivial algebraic mixture with the magnetic fluxes and Wilson lines, which together forms a three-group symmetry. For instance, the junction of Z 2 0-form symmetry operators acts on the magnetic surface operator by attaching an electric Wilson line operator [50, 70].

Therefore, a nontrivial question is whether one can find a faithful 0-form symmetry action in (3+1)D topological order, which does not permute any topological operators, and forms trivial higher-group symmetry with other topological operators.

One can find such 0-form global symmetry in (3+1)D gauge theory of a quaternion group Q 8 . Let us consider the global symmetry that corresponds to the (2+1)D Q 8 SPT phase, classified by H 3 ( BQ 8 , U (1)) = Z 8 . This generates the faithful Z 8 symmetry of the Q 8 gauge theory. We will see that the Z 2 subgroup of this Z 8 symmetry has the trivial higher group structure with other topological operators, meaning that the Z 2 ⊂ Z 8 becomes a direct product with other symmetries of Q 8 gauge theory.

Let us take a Q 8 SPT phase that generates the Z 8 classification, labeled by ν = 1 ∈ Z 8 . We write the generators of Q 8 (quaternions) as i , j , k , satisfying i 2 = j 2 = k 2 = -1. Then, if we restrict the gauge group to the Z 4 subgroup { 1 , i , -1 , -i } , this ν = 1 SPT phase reduces to the Z 4 SPT that generates the H 3 ( B Z 4 , U (1)) = Z 4 classification [71]. Therefore, writing the topological response of the ν = 1 phase as ω ν =1 ∈ Z 3 ( BQ 8 , U (1)), its restriction to the Z 4 gauge field becomes ω ν =1 = 2 πi 4 a d ˆ a 4 , where a is the Z 4 gauge field for Z 4 = Z ( i ) = { 1 , i , -1 , -i } , and ˆ a is the lift to Z 16 . Its slant product with respect to i ∈ Q 8 is evaluated as

$$i _ { \mathbf i } ( \omega _ { \nu = 1 } ) = \frac { 2 \pi i } { 4 } \, \frac { d \hat { a } } { 4 }$$

Since this slant product is trivial in cohomology H 2 ( B Z 4 , U (1)), this ν = 1 phase does not induce permutation of the magnetic flux [ i ]. However, the above slant product leads to a subtle algebraic mixture among SPT defects, the magnetic fluxes and Wilson lines [50]. Suppose we have the junction of four SPT defects labeled by ν = 1 into ν = 4.

8 We thank Nat Tantivasadakarn for helpful discussions on this point.

FIG. 9. The junction of four ν = 1 defects into a ν = 4 defect. When the non-invertible magnetic surface operator [ i ] = [ j ] = [ k ] intersects with this junction, their intersection emits an electric charge carried by the 2d Wilson line of Q 8 gauge theory.

<!-- image -->

FIG. 10. The ν = 4 defect acts on the point junction of three magnetic fluxes by the phase factor.

<!-- image -->

If the magnetic surface operator labeled by the conjugacy class [ i ] intersects with this junction, the intersection has to emit a Z 4 electric Wilson line exp ( 2 πi 4 ∫ a ) carrying the charge of Z 4 = Z ( i ). Since only the 2d irreducible representation of Q 8 can carry the Z 4 charge under Z ( i ), one can say that this junction emits the 2d Wilson line of Q 8 . This is a non-invertible categorical symmetry that involves the junction of 0-form SPT defects, magnetic fluxes and the 2d non-invertible Wilson line. See Fig. 9 for illustrations. The whole discussion about the ν = 1 defect above is symmetric under permuting group elements among i , j , k .

Now let us restrict the 0-form symmetry to the Z 2 ⊂ Z 8 global symmetry generated by ν = 4 phase. 9 The slant product for any group element becomes trivial,

$$i _ { \mathbf i } ( \omega _ { \nu = 4 } ) = i _ { \mathbf j } ( \omega _ { \nu = 4 } ) = i _ { \mathbf k } ( \omega _ { \nu = 4 } ) = 0 .$$

This implies that the ν = 4 defect does not permute the topological operators, and becomes direct product with the symmetries of magnetic fluxes and Wilson lines. However, this ν = 4 symmetry still acts by phase factors on the point junction of the three magnetic surface operators, see Fig. 10. This is an analogue of the soft symmetry of (2+1)D topological orders.

̸

More generally, when G is a discrete subgroup of SU (2), one can always find a topological response ω ∈ Z 3 ( BG,U (1)) which is nontrivial in cohomology [ ω ] = 0, but its slant product with any group element g ∈ G becomes completely trivial i g ω = 0 at the cochain level [71]. This implies that this class of finite groups has an analogue of soft symmetry, whose only nontrivial feature is an action on the point junctions of magnetic surfaces by a phase factor.

## VII. DISCUSSION

In this paper we have demonstrated the existence of soft symmetries in (2+1)D and (3+1)D topological orders. In (2+1)D, these correspond to symmetries that are neither fractionalized nor permute the anyons, but which nevertheless have a non-trivial action on the topological ground state subspace on higher genus surfaces. In (3+1)D, they correspond to symmetries that do not permute any topological defects and define a completely trivial 3-group structure with the other topological defects, but nevertheless act non-trivially in the underlying topological quantum field theory.

9 Though this Z 2 ⊂ Z 8 symmetry is faithful, it acts on the Hilbert space in a quite subtle manner. In particular, its action on the Hilbert space at any mapping torus of T 2 becomes trivial. This Z 2 symmetry acts faithfully on the Hilbert space at e.g., a spherical manifold S 3 /Q 8 dubbed a prism manifold [71].

For the (2+1)D theory, we studied an explicit lattice model realization, where the soft symmetry is realized by pumping a gauged (1+1)D SPT through the system via a finite depth local unitary circuit. Such a circuit does not commute with the full Hamiltonian but keeps the ground state subspace invariant, and thus can be viewed as an emergent symmetry of the theory.

So far we have demonstrated how the quantum double lattice model possesses an operator that acts as a non-trivial unitary operator on the ground state subspace. As such, it defines an emergent non-onsite symmetry. A natural question is whether we can construct a lattice model in which it corresponds to an exact, on-site symmetry.

One possible method for achieving this on-site soft symmetry is to use the symmetry-enriched version of the Crane-Yetter-Walker-Wang construction presented in [47].

Ref. [47] provides the (3+1)D path integral state sum model and corresponding Hamiltonian of the (3+1)D bosonic invertible phase with G symmetry, with input being a UMTC and its G symmetry fractionalization data { U, η } . This (3+1)D theory has a surface SET phase on its (2+1)D boundary, described by the input UMTC enriched with G symmetry. It would be interesting to see if the construction of the path integral is also valid for the symmetry fractionalization data { U, η } for the soft symmetry discussed in this paper.

Once one can construct the (3+1)D SPT by the Walker-Wang model with the boundary realizing SET with the soft symmetry, we note that the bulk (3+1)D phase is necessarily topologically trivial, because there are no non-trivial Z 2 SPTs in (3+1)D [51, 72]. Since the bulk (3+1)D phase is topologically trivial, there should also be a symmetry-preserving topologically trivial boundary condition. Considering the system on a thin slab with the top boundary corresponding to our SET of interest and the bottom slab corresponding to the topologically trivial boundary condition should give us a (2+1)D lattice model where the Z 2 soft symmetry is an exact on-site symmetry. It would be interesting to explicitly construct such (2+1)D lattice models with on-site soft symmetries.

Also, the soft symmetries that we studied in this paper were in terms of gauged SPT defects. A natural question is whether there is a systematic method to find all possible soft symmetries. For example, as discussed in Sec. III B, there are also soft symmetries of G gauge theory corresponding to Out sf ( G ). It would be interesting to develop a physical construction for such soft symmetries that allows them to be implemented as a finite depth circuit.

Finally, it remains unknown if the generic soft symmetry has the H 3 obstruction characterized by [ O 3 ] = H 3 (Aut br ( C ) , A ). While the example of the soft symmetry provided in the main text does not have the H 3 obstruction, it remains unclear if the generic soft symmetries including the outer automorphism Out sf ( G ) carry the trivial H 3 obstruction or not. 10 See Refs. [3, 73] for examples of the outer automorphism in finite gauge theories with H 3 obstructions. This is an interesting question since it is often believed that the symmetry that does not permute anyons leads to trivial H 3 obstruction [3, 41].

## VIII. ACKNOWLEDGMENT

We thank Parsa Bonderson, Yu-An Chen, Meng Cheng, Yichul Choi, Po-Shen Hsin, Yoshiko Ogata, Abhinav Prem, Nathan Seiberg, Sahand Seifnashri, Nikita Sopenko, Nat Tantivasadakarn and Zhenghan Wang for useful discussions. We thank Meng Cheng, Nat Tantivasadakarn and Zhenghan Wang for comments on the draft. R.K. is supported by the U.S. Department of Energy (Grant No. DE-SC0009988) and the Sivian Fund. M.B. is supported by NSF DMR-2345644.

## Appendix A: Symmetric representative of second cohomology H 2 ( BG sf , U (1))

In the main text, we provided the representative of H 2 ( BG sf , U (1)) given by the following 2-cocycle

$$\omega _ { p q } ( g , h ) = \pi ( n _ { p } ( g ) n _ { q } ( h ) ) \ .$$

Here we explicitly construct a function χ : G sf → Z 2 such that

$$\omega _ { s f } ( g , h ) \colon = \omega _ { p q } ( g , h ) + \pi ( \chi ( g ) + \chi ( h ) - \chi ( g h ) ) \\$$

10 We note that [41] argued that the H 3 obstruction must be trivial when the symmetry does not permute anyons. Their argument assumes that the fusion multiplicities satisfy N ab c ∈ { 0 , 1 } for all fusion vertices, and that the F -symbol ( F abc d ) ef is always nonzero whenever the four relevant fusion spaces V ab e , V ec d , V af d , and V bc f are all nonempty. We note, however, that there are modular tensor categories in which certain F -symbols vanish even though this is not forbidden by the fusion rules; for example, F 111 1 vanishes in SU (2) 4 . Therefore, it is still unknown in general if H 3 obstruction is vanishing for soft symmetries. We thank Parsa Bonderson for bringing this point to our attention.

satisfies the following two properties:

- ω sf ( g, h ) is symmetric, i.e., ω sf ( g, h ) = ω sf ( h, g ) for any g, h ∈ G sf .
- ω sf ( g, h ) is invariant under overall conjugation by group elements, i.e., ω sf ( g, h ) = ω sf ( kgk -1 , khk -1 ) for any g, h, k ∈ G sf .

Note that ω sf gives another representative of H 2 ( BG sf , U (1)) with [ ω sf ] = [ ω pq ]. Let us explicitly construct such a function χ . For convenience, a group element g ∈ G sf is sometimes expressed as g = g A g B , where g A = p α q β r γ 1 1 r γ 2 2 and g B = x µ y ν 1 1 y ν 2 2 . We define a subset Γ A ⊂ G sf that consists of group elements Γ A = { p α q β r γ 1 1 r γ 2 2 } with generic choices of α, β, γ 1 , γ 2 . Let us similarly define the subgroup Γ B ⊂ G sf where Γ B = { x µ y ν 1 1 y ν 2 2 } .

We first fix χ ( g ) for the group elements g ∈ G sf expressed as g = kg A k -1 for some g A ∈ Γ A , k ∈ G sf . We set

$$\chi ( k g _ { A } k ^ { - 1 } ) = n _ { p } ( g _ { A } ) n _ { q } ( k ) + n _ { p } ( k ) n _ { q } ( g _ { A } ) \mod 2 .$$

Not all group elements g ∈ G sf admits an expression g = kg A k -1 (for instance, g = qy 1 does not). For a generic group element g ∈ G sf , we set χ ( g ) in the following fashion. For g A ∈ Γ A , we define a group Γ( g A ) ⊂ Γ B , which is the group generated by the elements γ k := kg A k -1 ( g A ) -1 for all possible choices of k ∈ G sf . Then, let us fix a choice of another subgroup ˜ Γ( g A ) ⊂ Γ B satisfying Γ( g A ) × ˜ Γ( g A ) = Γ B , Γ( g A ) ∩ ˜ Γ( g A ) = { id } .

Then, χ ( g ) with generic group element g ∈ G sf is defined as follows. We express g = kg A ˜ γk -1 with g A ∈ G sf , ˜ γ ∈ ˜ Γ( g A ) , k ∈ G sf . By definition, for a given g ∈ G sf the choice of g A , ˜ γ are uniquely fixed. We then set

$$\chi ( k g _ { A } \tilde { \gamma } k ^ { - 1 } ) = n _ { p } ( g _ { A } ) n _ { q } ( k ) + n _ { p } ( k ) n _ { q } ( g _ { A } ) \mod 2 .$$

For a given g ∈ G sf , one can explicitly check that the above χ ( g ) does not depend on the choice of k ∈ G sf .

Let us confirm that the properties of ω sf ( g, h ) are satisfied with the above choice of χ . Let us first check the symmetric property. We have

$$e ^ { i \omega _ { s f } ( g , h ) - i \omega _ { s f } ( h , g ) } = ( - 1 ) ^ { n _ { p } ( g ) n _ { q } ( h ) - n _ { q } ( g ) n _ { p } ( h ) + \chi ( g h ) - \chi ( h g ) } \ .$$

Let us write gh = k ( gh ) A ˜ γk -1 with ( gh ) A ∈ Γ A , ˜ γ ∈ ˜ Γ(( gh ) A ), k ∈ G sf . Then we get

$$\chi ( g h ) = n _ { p } ( ( g h ) _ { A } ) n _ { q } ( k ) + n _ { p } ( k ) n _ { q } ( ( g h ) _ { A } ) , \ \ \chi ( h g ) = n _ { p } ( ( g h ) _ { A } ) n _ { q } ( h k ) + n _ { p } ( h k ) n _ { q } ( ( g h ) _ { A } ) \, .$$

These can be rewritten as

$$\chi ( g h ) & = ( n _ { p } ( g ) + n _ { p } ( h ) ) n _ { q } ( k ) + n _ { p } ( k ) ( n _ { q } ( g ) + n _ { q } ( h ) ) , \\ \chi ( h g ) & = ( n _ { p } ( g ) + n _ { p } ( h ) ) ( n _ { q } ( h ) + n _ { q } ( k ) ) + ( n _ { p } ( h ) + n _ { p } ( k ) ) ( n _ { q } ( g ) + n _ { q } ( h ) )$$

Hence we have χ ( gh ) -χ ( hg ) = n p ( g ) n q ( h ) -n q ( g ) n p ( h ) mod 2. By plugging this to the expression of e iω sf ( g,h ) -iω sf ( h,g ) , one can see that ω sf ( g, h ) is symmetric.

Let us then verify the property ω sf ( g, h ) = ω sf ( kgk -1 , khk -1 ) for any g, h, k ∈ G sf . To see this, one can first immediately check that ω pq satisfies ω pq ( g, h ) = ω pq ( kgk -1 , khk -1 ). So one just needs to check

$$d _ { \chi } ( g , h ) = d _ { \chi } ( k g k ^ { - 1 } , k h k ^ { - 1 } ) \ .$$

From the definition of χ in (A4), for generic g, k ∈ G sf we have

$$\chi ( g ) - \chi ( k g k ^ { - 1 } ) = n _ { p } ( g ) n _ { q } ( k ) + n _ { p } ( k ) n _ { q } ( g ) \mod 2 .$$

Therefore we have

$$d \chi ( g , h ) - d \chi ( k g k ^ { - 1 } , k h k ^ { - 1 } ) = d n _ { p } ( g , h ) n _ { q } ( k ) + n _ { p } ( k ) d n _ { q } ( g , h ) = 0 \mod 2 .$$

This completes the proof of ω sf ( g, h ) = ω sf ( kgk -1 , khk -1 ).

## Appendix B: (1+1)D SPT phases with genus ≥ 3 detection

In this appendix, we construct the (1+1)D SPT phases which can be detected on a genus g surface, though cannot be detected on genus ≤ g -1.

We consider the group G ( g ) sf of order 2 g 2 +2 g -1 with g ≥ 2 which is the central extension Z g 2 -1 2 → G ( g ) sf → Z 2 g 2 . The generators of Z 2 g 2 are labeled by p j , q j with 1 ≤ j ≤ g , and generators of Z g 2 -1 2 are labeled by x j with 1 ≤ j ≤ g -1, and y jk , z jk with 1 ≤ j &lt; k ≤ g . The central extension is characterized by

$$[ p _ { 1 } , q _ { 1 } ] & = x _ { 1 } , \quad [ p _ { g } , q _ { g } ] = x _ { g - 1 } , \\ [ p _ { j } , q _ { j } ] & = x _ { j - 1 } x _ { j } ; \ 2 \leq j \leq g - 1 \\ [ p _ { j } , p _ { k } ] & = y _ { j k } ; \ j < k \\ [ p _ { j } , q _ { k } ] & = z _ { j k } ; \ j < k$$

where [ p, q ] = pqp -1 q -1 is a group commutator. Note that the above group G ( g ) sf with g = 2 corresponds to the group G sf discussed in the main text. Let us consider the SPT action ω ( g ) ∈ Z 2 ( BG ( g ) sf , U (1)) characterized by

$$\omega ^ { ( g ) } ( h , k ) = \pi ( n _ { p _ { 1 } } ( h ) \cup n _ { q _ { 1 } } ( k ) ) ,$$

where n p 1 ( h ) ∈ Z 1 ( BG ( g ) sf , U (1)) is the mod 2 number of p 1 that appears in the expression of h ∈ G ( g ) sf in terms of the product of group generators. Similar for n q 1 ( h ). This SPT phase is detected on a genus g surface with holonomy ( p j , q j ), 1 ≤ j ≤ g on each pair of cycles, while cannot be detected on closed oriented surfaces of genus &lt; g .

The above SPT phases lead to the 'softer' 0-form Z 2 symmetry of (2+1)D G ( g ) sf gauge theory with nontrivial action on genus g , generated by the gauged SPT defect.

- [1] X.-G. Wen, Quantum Field Theory of Many-Body Systems . Oxford Univ. Press, Oxford, 2004.
- [2] B. Zeng, X. Chen, D.-L. Zhou, X.-G. Wen, et al. , Quantum information meets quantum matter . Springer, 2019.
- [3] M. Barkeshli, P. Bonderson, M. Cheng, and Z. Wang, 'Symmetry fractionalization, defects, and gauging of topological phases,' Phys. Rev. B 100 (Sep, 2019) 115147, arXiv:1410.4540 .
- [4] R. B. Laughlin, 'Anomalous quantum hall effect: An incompressible quantum fluid with fractionally charged excitations,' Phys. Rev. Lett. 50 (May, 1983) 1395-1398. https://link.aps.org/doi/10.1103/PhysRevLett.50.1395 .
- [5] R. de Picciotto, M. Reznikov, M. Heiblum, V. Umansky, G. Bunin, and D. Mahalu, 'Direct observation of a fractional charge,' Nature 389 no. 6647, (1997) 162-164.
- [6] L. Saminadayar, D. Glattli, Y. Jin, and B. c.-m. Etienne, 'Observation of the e/3 fractionally charged laughlin quasiparticle,' Physical Review Letters 79 no. 13, (1997) 2526.
- [7] L. Savary and L. Balents, 'Quantum spin liquids: a review,' Reports on Progress in Physics 80 no. 1, (2017) 016502.
- [8] M. Barkeshli and X.-G. Wen, ' u (1) × u (1) ⋊ z 2 chern-simons theory and z 4 parafermion fractional quantum hall states,' Phys. Rev. B 81 (2010) 045323, arXiv:0909.4882 .
- [9] H. Bombin, 'Topological order with a twist: Ising anyons from an abelian model,' Phys. Rev. Lett. 105 (Jul, 2010) 030403, arXiv:1004.1838 .
- [10] M. Barkeshli and X.-L. Qi, 'Topological nematic states and non-abelian lattice dislocations,' Phys. Rev. X 2 (Aug, 2012) 031013. https://link.aps.org/doi/10.1103/PhysRevX.2.031013 .
- [11] M. Barkeshli, C.-M. Jian, and X.-L. Qi, 'Twist defects and projective non-abelian braiding statistics,' Phys. Rev. B 87 (Jan, 2013) 045130. https://link.aps.org/doi/10.1103/PhysRevB.87.045130 .
- [12] A. Lavasani and M. Barkeshli, 'Low overhead clifford gates from joint measurements in surface, color, and hyperbolic codes,' Physical Review A 98 no. 5, (2018) 052319.
- [13] B. J. Brown, K. Laubscher, M. S. Kesselring, and J. R. Wootton, 'Poking holes and cutting corners to achieve clifford gates with the surface code,' Physical Review X 7 no. 2, (2017) 021029.
- [14] M. B. Hastings and A. Geller, 'Reduced space-time and time costs using dislocation codes and arbitrary ancillas,' arXiv preprint arXiv:1408.3379 (2014) .
- [15] G. Zhu, M. Hafezi, and M. Barkeshli, 'Quantum origami: Transversal gates for quantum computation and measurement of topological order,' Physical Review Research 2 no. 1, (2020) 013285.
- [16] 'Non-abelian braiding of graph vertices in a superconducting processor,' Nature 618 no. 7964, (2023) 264-269.
- [17] M. Iqbal, A. Lyons, C. F. B. Lo, N. Tantivasadakarn, J. Dreiling, C. Foltz, T. M. Gatterman, D. Gresh, N. Hewitt, C. A. Holliman, J. Johansen, B. Neyenhuis, Y. Matsuoka, M. Mills, S. A. Moses, P. Siegfried, A. Vishwanath, R. Verresen, and H. Dreyer, 'Qutrit toric code and parafermions in trapped ions,' arXiv:2411.04185 [quant-ph] . https://arxiv.org/abs/2411.04185 .
- [18] M. Barkeshli and X.-L. Qi, 'Synthetic topological qubits in conventional bilayer quantum hall systems,' Phys. Rev. X 4 (Nov, 2014) 041035.
- [19] M. Barkeshli, Y. Oreg, and X.-L. Qi, 'Experimental proposal to detect topological ground state degeneracy,' arXiv:1401.3750 .
- [20] D. J. Clarke, J. Alicea, and K. Shtengel, 'Exotic non-abelian anyons from conventional fractional quantum hall states,' Nature Comm. 4 (2013) 1348, arXiv:1204.5479 .

- [21] N. H. Lindner, E. Berg, G. Refael, and A. Stern, 'Fractionalizing majorana fermions: Non-abelian statistics on the edges of abelian quantum hall states,' Phys. Rev. X 2 (Oct, 2012) 041002, arXiv:1204.5733 .
- [22] M. Cheng, 'Superconducting proximity effect on the edge of fractional topological insulators,' Phys. Rev. B 86 (Nov, 2012) 195126, arXiv:1204.6084 .
- [23] K. Agarwal, 'Quantum hall valley ferromagnets as a platform for topologically protected quantum memory,' Physical Review B 107 no. 12, (2023) 125163.
- [24] M. Barkeshli, Y.-A. Chen, S.-J. Huang, R. Kobayashi, N. Tantivasadakarn, and G. Zhu, 'Codimension-2 defects and higher symmetries in (3+1)d topological phases,' SciPost Physics 14 no. 4, (Apr., 2023) . http://dx.doi.org/10.21468/SciPostPhys.14.4.065 .
- [25] S. Beigi, P. W. Shor, and D. Whalen, 'The quantum double model with boundary: Condensations and symmetries,' Communications in Mathematical Physics 306 no. 3, (June, 2011) 663-694. http://dx.doi.org/10.1007/s00220-011-1294-x .
- [26] A. Kitaev and L. Kong, 'Models for gapped boundaries and domain walls,' Comm. Math. Phys. 313 no. 2, (2012) 351-373, arXiv:1104.5047 .
- [27] A. Kapustin and N. Saulina, 'Topological boundary conditions in abelian chern-simons theory,' Nucl. Phys. B 845 (2011) 393-435.
- [28] M. Levin, 'Protected edge modes without symmetry,' Physical Review X 3 no. 2, (May, 2013) , arXiv:1301.7355 [cond-mat.str-el] .
- [29] M. Barkeshli, C.-M. Jian, and X.-L. Qi, 'Classification of topological defects in abelian topological states,' Phys. Rev. B 88 (Dec, 2013) 241103(R).
- [30] I. Cong, M. Cheng, and Z. Wang, 'Hamiltonian and algebraic theories of gapped boundaries in topological phases of matter,' Communications in Mathematical Physics 355 (2017) 645-689.
- [31] A. Davydov, 'Bogomolov multiplier, double class-preserving automorphisms, and modular invariants for orbifolds,' Journal of Mathematical Physics 55 no. 9, (Sept., 2014) , arXiv:1312.7466 [math] . http://dx.doi.org/10.1063/1.4895764 .
- [32] A. Kitaev, 'Anyons in an exactly solved model and beyond,' Annals of Physics 321 no. 1, (Jan., 2006) 2-111. http://dx.doi.org/10.1016/j.aop.2005.10.005 .
- [33] P. H. Bonderson, Non-Abelian anyons and interferometry . California Institute of Technology, 2012.
- [34] S. H. Simon, Topological quantum . Oxford University Press, 2023.
- [35] K. Kawagoe and M. Levin, 'Microscopic definitions of anyon data,' Phys. Rev. B 101 (Mar, 2020) 115113. https://link.aps.org/doi/10.1103/PhysRevB.101.115113 .
- [36] P. Bonderson and J. K. Slingerland, 'Fractional quantum hall hierarchy and the second landau level,' Phys. Rev. B 78 (Sep, 2008) 125323.
- [37] G. Moore and N. Seiberg, 'Classical and quantum conformal field theory,' Comm. Math. Phys. 123 no. 2, (1989) 177-254.
- [38] Z. Wang, Topological Quantum Computation . American Mathematical Society, 2008.
- [39] P. Etingof, D. Nikshych, and V. Ostrik, 'On fusion categories,' 2017. https://arxiv.org/abs/math/0203060 .
- [40] P. Etingof, D. Nikshych, and V. Ostrik, 'Fusion categories and homotopy theory,' Quantum Topology 1 (2010) 209-273, arXiv:0909.3140 .
- [41] F. Benini, C. C´ ordova, and P.-S. Hsin, 'On 2-Group Global Symmetries and their Anomalies,' JHEP 03 (2019) 118, arXiv:1803.09336 [hep-th] .
- [42] L. Fidkowski and A. Vishwanath, 'Realizing anomalous anyonic symmetries at the surfaces of three-dimensional gauge theories,' July, 2017. http://dx.doi.org/10.1103/PhysRevB.96.045131 .
- [43] M. Barkeshli and M. Cheng, 'Time-reversal and spatial-reflection symmetry localization anomalies in (2+1)-dimensional topological phases of matter,' Phys. Rev. B 98 (Sep, 2018) 115129.
- [44] M. Cheng, M. Zaletel, M. Barkeshli, A. Vishwanath, and P. Bonderson, 'Translational symmetry and microscopic constraints on symmetry-enriched topological phases: A view from the surface,' Phys. Rev. X 6 (Dec, 2016) 041068. https://link.aps.org/doi/10.1103/PhysRevX.6.041068 .
- [45] S. X. Cui, C. Galindo, J. Y. Plavnik, and Z. Wang, 'On gauging symmetry of modular categories,' Comm. Math. Phys. 348 no. 3, (2016) 1043-1064.
- [46] M. Barkeshli and M. Cheng, 'Relative anomalies in (2+1)d symmetry enriched topological states,' SciPost Physics 8 no. 2, (Feb, 2020) . http://dx.doi.org/10.21468/SciPostPhys.8.2.028 .
- [47] D. Bulmash and M. Barkeshli, 'Absolute anomalies in (2+1)d symmetry-enriched topological states and exact (3+1)d constructions,' Physical Review Research 2 no. 4, (Oct., 2020) , arXiv:2003.11553 . http://dx.doi.org/10.1103/PhysRevResearch.2.043033 .
- [48] C. Jones, D. Penneys, and D. Reutter, 'A 3-categorical perspective on g-crossed braided categories,' arXiv:2009.00405 .
- [49] R. Dijkgraaf and E. Witten, 'Topological gauge theories and group cohomology,' Comm. Math. Phys. 129 (1990)
30. 393-429.
- [50] M. Barkeshli, Y.-A. Chen, P.-S. Hsin, and R. Kobayashi, 'Higher-group symmetry in finite gauge theory and stabilizer codes,' SciPost Physics 16 no. 4, (Apr., 2024) . http://dx.doi.org/10.21468/SciPostPhys.16.4.089 .
- [51] X. Chen, Z.-C. Gu, and X.-G. Wen, 'Classification of gapped symmetric phases in one-dimensional spin systems,' Phys. Rev. B 83 (Jan, 2011) 035107.
- [52] B. H. Neumann, 'Not quite inner automorphisms,' Bulletin of the Australian Mathematical Society 23 no. 3, (1981) 461-469.
- [53] F. Szechtman, 'n-inner automorphisms of finite groups,' Proceedings of the American Mathematical Society 131 no. 12,

(2003) 3657-3664.

- [54] F. Pollmann and A. M. Turner, 'Detection of symmetry-protected topological phases in one dimension,' Physical Review B 86 no. 12, (Sept., 2012) . http://dx.doi.org/10.1103/PhysRevB.86.125441 .
- [55] A. Kitaev, 'Fault-tolerant quantum computation by anyons,' Annals of Physics 303 no. 1, (Jan., 2003) 2-30. http://dx.doi.org/10.1016/S0003-4916(02)00018-0 .
- [56] Y.-A. Chen and S. Tata, 'Higher cup products on hypercubic lattices: Application to lattice models of topological phases,' Journal of Mathematical Physics 64 no. 9, (Sept., 2023) . http://dx.doi.org/10.1063/5.0095189 .
- [57] H. Bombin and M. A. Martin-Delgado, 'Family of non-abelian kitaev models on a lattice: Topological condensation and confinement,' Physical Review B 78 no. 11, (Sept., 2008) . http://dx.doi.org/10.1103/PhysRevB.78.115421 .
- [58] A. Davydov, M. Mueger, D. Nikshych, and V. Ostrik, 'The witt group of non-degenerate braided fusion categories,' 2011. https://arxiv.org/abs/1009.2117 .
- [59] J. Fuchs, C. Schweigert, and A. Valentino, 'Bicategories for boundary conditions and for surface defects in 3-d tft,' Communications in Mathematical Physics 321 no. 2, (May, 2013) 543-575. http://dx.doi.org/10.1007/s00220-013-1723-0 .
- [60] T. Lan, J. C. Wang, and X.-G. Wen, 'Gapped domain walls, gapped boundaries, and topological degeneracy,' Physical Review Letters 114 no. 7, (Feb., 2015) . http://dx.doi.org/10.1103/PhysRevLett.114.076402 .
- [61] J. Kaidi, Z. Komargodski, K. Ohmori, S. Seifnashri, and S.-H. Shao, 'Higher central charges and topological boundaries in 2+1-dimensional tqfts,' SciPost Physics 13 no. 3, (Sept., 2022) . http://dx.doi.org/10.21468/SciPostPhys.13.3.067 .
- [62] Y. Kawahigashi, 'A remark on gapped domain walls between topological phases,' Letters in Mathematical Physics 105 no. 7, (May, 2015) 893-899. http://dx.doi.org/10.1007/s11005-015-0766-x .
- [63] W. Ji and X.-G. Wen, 'Categorical symmetry and noninvertible anomaly in symmetry-breaking and topological phase transitions,' Phys. Rev. Res. 2 no. 3, (2020) 033417, arXiv:1912.13492 [cond-mat.str-el] .
- [64] D. S. Freed, G. W. Moore, and C. Teleman, 'Topological symmetry in quantum field theory,' (9, 2022) , arXiv:2209.07471 [hep-th] .
- [65] J. Kaidi, K. Ohmori, and Y. Zheng, 'Symmetry TFTs for Non-Invertible Defects,' (9, 2022) , arXiv:2209.11062 [hep-th] .
- [66] L. Bhardwaj, L. E. Bottini, D. Pajer, and S. Schafer-Nameki, 'Categorical landau paradigm for gapped phases,' 2023. https://arxiv.org/abs/2310.03786 .
- [67] L. Bhardwaj, L. E. Bottini, D. Pajer, and S. Schafer-Nameki, 'Gapped phases with non-invertible symmetries: (1+1)d,' 2024. https://arxiv.org/abs/2310.03784 .
- [68] L. Bhardwaj and Y. Tachikawa, 'On finite symmetries and their gauging in two dimensions,' Journal of High Energy Physics 2018 no. 3, (Mar., 2018) . http://dx.doi.org/10.1007/JHEP03(2018)189 .
- [69] R. Kobayashi and H. Watanabe, 'Projective representations, bogomolov multiplier, and their applications in physics,' 2025. https://arxiv.org/abs/2507.12515 .
- [70] P.-S. Hsin and A. Turzillo, 'Symmetry-enriched quantum spin liquids in (3 + 1)d,' Journal of High Energy Physics 2020 no. 9, (Sept., 2020) . http://dx.doi.org/10.1007/JHEP09(2020)022 .
- [71] M. Yu, 'Genus-one data and anomaly detection,' Physical Review D 105 no. 10, (May, 2022) . http://dx.doi.org/10.1103/PhysRevD.105.106007 .
- [72] A. Kapustin, 'Symmetry protected topological phases, anomalies, and cobordisms: beyond group cohomology,' arXiv preprint arXiv:1403.1467 (2014) .
- [73] L. Fidkowski and A. Vishwanath, 'Realizing anomalous anyonic symmetries at the surfaces of three-dimensional gauge theories,' Physical Review B 96 no. 4, (July, 2017) . http://dx.doi.org/10.1103/PhysRevB.96.045131 .