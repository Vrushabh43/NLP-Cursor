## Hardness of Quantum Distribution Learning and Quantum Cryptography

Taiga Hiroka 1,2 , Min-Hsiu Hsieh 1 , Tomoyuki Morimae 2,1

1

Hon Hai Research Institute, Taipei, Taiwan {taiga.hirooka,min-hsiu.hsieh}@foxconn.com 2 Yukawa Institute for Theoretical Physics, Kyoto University, Kyoto, Japan tomoyuki.morimae@yukawa.kyoto-u.ac.jp

## Abstract

The existence of one-way functions (OWFs) forms the minimal assumption in classical cryptography. However, this is not necessarily the case in quantum cryptography [Kretschmer 2021; Morimae and Yamakawa 2022; Ananth, Qian and Yuen 2022]. One-way puzzles (OWPuzzs) introduced by [Khurana and Tomer 2024] provide a natural quantum analogue of OWFs. The existence of OWPuzzs implies PP = BQP [Cavalar, Goldin, Gray, Hall, Liu, and Pelecanos 2025], while the converse remains an open question. In classical cryptography, the analogous problem - whether OWFs can be constructed from P = NP - is one of the most central open problems, and has long been studied from the viewpoint of hardness of learning. Hardness of learning in various frameworks (including PAC learning) has been connected to the existence of OWFs or to P = NP . In contrast, no such characterization previously existed for OWPuzzs. In this paper, we establish the first complete characterization of OWPuzzs based on the hardness of a well-studied learning model: distribution learning. Specifically, we prove that OWPuzzs exist if and only if proper quantum distribution learning is hard on average. A natural question that follows from our result is whether the worst-case hardness of proper quantum distribution learning can be derived from PP = BQP , because if this is the case and the worst-case to average-case hardness reduction within proper quantum distribution learning is achieved, it would imply OWPuzzs solely from PP = BQP ! However, we show that answering the question positively would be extremely difficult: if worst-case hardness of proper quantum distribution learning is PP -hard (in a black-box reduction), then SampBQP = SampBPP is derived solely from the infiniteness of the polynomial-time hierarchy, which solves a long-standing open problem in the field of quantum advantage. Despite that, we show that PP = BQP is equivalent to another standard and well-studied notion of hardness of learning, namely agnostic. We show that PP = BQP if and only if agnostic quantum distribution learning with respect to the KL divergence is hard. Finally, as a byproduct, we also obtain an interesting implication for quantum advantage: we show that hardness of agnostic quantum distribution learning with respect to the statistical distance against PPT Σ P 3 learner implies SampBQP = SampBPP . This provides the first construction of sampling-based quantum advantage from a hardness assumption on a standard and natural framework in learning theory. Moreover, hardness of agnostic learning is of the worst-case type, and therefore this result is the first construction of sampling-based quantum advantage solely from a worst-case hardness assumption.

̸

̸

̸

̸

̸

̸

̸

̸

̸

## Contents

| 1 Introduction   | 1 Introduction                                                              | 1 Introduction                                                                     |   1 |
|------------------|-----------------------------------------------------------------------------|------------------------------------------------------------------------------------|-----|
|                  | 1.1                                                                         | Our Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  |   2 |
|                  | 1.2                                                                         | Related Works . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  |   6 |
|                  | 1.3                                                                         | Technical Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   |   8 |
| 2                | Preliminaries                                                               | Preliminaries                                                                      |  11 |
|                  | 2.1                                                                         | Basic Notations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  |  11 |
|                  | 2.2                                                                         | Lemmas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   |  11 |
|                  | 2.3                                                                         | Complexity Classes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   |  12 |
|                  | 2.4                                                                         | Quantum Advantage Assumption . . . . . . . . . . . . . . . . . . . . . . . .       |  13 |
|                  | 2.5                                                                         | Cryptographic Primitives . . . . . . . . . . . . . . . . . . . . . . . . . . . .   |  14 |
| 3                | Average-Case Hardness of Proper Distribution Learning                       | Average-Case Hardness of Proper Distribution Learning                              |  15 |
|                  | 3.1                                                                         | Quantum Case . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   |  15 |
|                  | 3.2                                                                         | Classical Case . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . |  27 |
| 4                | Agnostic Distribution Learning with Respect to KL Divergence                | Agnostic Distribution Learning with Respect to KL Divergence                       |  28 |
|                  | 4.1                                                                         | Quantum Case . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   |  28 |
|                  | 4.2                                                                         | Classical Case . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . |  35 |
| 5                | Agnostic Quantum Distribution Learning with Respect to Statistical Distance | Agnostic Quantum Distribution Learning with Respect to Statistical Distance        |  36 |
|                  | 5.1                                                                         | Upper Bounds of Distribution Learning with Respect to Statistical Distance .       |  36 |
|                  | 5.2                                                                         | Quantum Advantage and Hardness of Agnostic Quantum Distribution Learning           |  37 |
|                  | 5.3                                                                         | Proof of Theorem 5.3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   |  39 |
| A                | Proof of Theorem 5.4                                                        | Proof of Theorem 5.4                                                               |  55 |
| B                | Proof of Theorem 5.9                                                        | Proof of Theorem 5.9                                                               |  56 |

## 1 Introduction

In classical cryptography, the existence of one-way functions (OWFs) is the minimal assumption [IL89]: OWFs are known to be existentially equivalent to a wide range of cryptographic primitives, including pseudorandom generators (PRGs) [HILL99], pseudorandom functions (PRFs) [GGM86], secret-key encryption (SKE) [GM84], message authentication codes (MACs) [GGM84], digital signatures [Rom90], and commitment schemes [Nao90]. Moreover, nearly all cryptographic primitives (including public-key encryption (PKE) and multiparty computation) imply OWFs.

In contrast, in quantum cryptography, OWFs would not necessarily be the minimal assumption [Kre21, MY22, AQY22]. Several quantum analogues of OWFs, PRGs, and PRFs have been introduced, such as pseudorandom unitaries (PRUs) [JLS18], pseudorandom state generators (PRSGs) [JLS18], one-way state generators (OWSGs) [MY22], one-way puzzles (OWPuzzs) [KT24], and EFI pairs [BCQ23]. They could be weaker than OWFs [Kre21, KQST23, LMW24, KQT24], yet they support a variety of important applications including private-key quantum money [JLS18], SKE [AQY22], MACs [AQY22], digital signatures [MY22], commitments [MY22, AQY22, Yan22], and multiparty computation [MY22, AQY22, BCKM21, GLSV21].

In particular, one-way puzzles (OWPuzzs) introduced by Khurana and Tomer [KT24] are a natural quantum analogue of OWFs, and one of the most fundamental quantum cryptographic primitives. A OWPuzz is a pair ( Samp , Vrfy ) of two algorithms. Samp is a quantum polynomial-time (QPT) algorithm that, on input the security parameter 1 n , outputs two classical bit strings, ans and puzz . Vrfy is an unbounded algorithm that, on input ( puzz , ans ′ ) , outputs ⊤ / ⊥ . Correctness requires that Vrfy accepts ( puzz , ans ) ← Samp (1 n ) with high probability. Security requires that no QPT adversary that receives puzz can output ans ′ such that ( puzz , ans ′ ) is accepted by Vrfy with high probability.

̸

The existence of OWPuzzs implies PP = BQP [CGG + 23]. On the other hand, in a recent breakthrough paper by Khurana and Tomer [KT25], OWPuzzs were constructed from PP = BQP in conjunction with an additional standard assumption in the field of quantum advantage [AA11, BMS16], which we refer to as the 'quantum advantage assumption' for simplicity 1 . Although the quantum advantage assumption has been intensively investigated for over a decade, and some partial progress has been made [BFNV19, Mov23], it remains unproven. Moreover, the assumption was a newly introduced one, devised specifically for this purpose, and has not been explored in other areas. As a result, the following question posed by [KT25] remains one of the most important open problems in quantum cryptography.

̸

̸

## Can OWPuzzs be constructed solely from PP = BQP ?

̸

This question serves as a quantum analogue of the long-standing open problem in classical cryptography [DH76]: Can OWFs be constructed from P = NP (or NP ̸⊆ BPP )? In the classical setting, OWFs and P = NP (or NP ̸⊆ BPP ) have been extensively studied through the lens of learning hardness [Val84, PV88, IL90, BFKL94, Reg05, NY15, HN23]. Impagliazzo and Levin [IL90] first constructed OWFs based on a specific type of learning hardness, and subsequent works [BFKL94, NR06, NY15, HN23] extended this approach to more standard and general learning models. In particular, OWFs can be constructed from the average-case hardness of proper PAC learning [Val84, BFKL94], while NP ⊈ BPP implies the worst-case hardness of proper PAC learning [PV88]. These characterizations suggest a promising pathway toward resolving the open problem of constructing OWFs from NP ̸⊆ BPP , namely, establishing the worst-case to average-case hardness reduction within proper PAC learning! Learning theory is closely connected to meta-complexity [Ko91, HN22, GKLO22, GK23], which is another compelling direction for

̸

1 This is so-called 'anti-concentration' and 'average-case # P -hardness'. For the definition, see Assumption 2.10.

addressing the open problem [Hir18, LP20, LP21, IRS21, LP23, HIL + 23, Hir23]. Therefore, characterizing OWFs with hardness of learning also deepens our understanding of OWFs in terms of meta-complexity.

Characterizing cryptographic primitives with hardness of learning has another important implication: it can offer valuable insights into identifying concrete hardness assumptions on which cryptographic primitives can be based. Indeed, well-known assumptions such as Learning Parity with Noise (LPN) and Learning with Errors (LWE) [BFKL94, Reg05] are rooted in the hardness of specific learning problems. Establishing foundations for quantum cryptographic primitives based on concrete mathematical hard problems remains one of the central goals in the field.

However, to the best of our knowledge, no such characterization with learning hardness has been established for OWPuzzs.

## 1.1 Our Results

In this paper, we establish, for the first time, complete characterizations of OWPuzzs and PP = BQP with hardness of learning.

̸

̸

In the classical setting, characterizing cryptographic primitives through the hardness of PAC learning has a long history [BFKL94, ABX08, Nan20]. In (classical) PAC learning, the learner receives samples (( x 1 , y 1 ) , ( x 2 , y 2 ) , ..., ( x T , y T )) , where x 1 , x 2 , ..., x T are independently sampled from a distribution D , y i = f ( x i ) , and f is a function computable in classical deterministic polynomial-time. The learner's goal is to output a hypothesis function h such that Pr x ←D [ f ( x ) = h ( x )] is small. A natural quantum analogue is that the function f is evaluated in deterministic QPT. However, OWPuzzs will not be properly characterized with hardness of such quantum PAC learning, because hardness of such quantum PAC learning is broken with access to a QCMA oracle, while OWPuzzs will not be broken with access to a QCMA oracle [Kre21]. On the other hand, OWPuzzs are broken with access to a PP oracle [CGG + 23]. Thus, to obtain a correct characterization of OWPuzzs, we must consider a learning model whose hardness is not broken by a QCMA oracle but broken by a PP oracle.

Our key idea is to focus on distribution learning [KMR + 94, HN23]. Distribution learning is a learning framework in which the learner receives samples from a distribution and must 'learn' the distribution. (For example, in proper distribution learning, the learner receives samples from a distribution with a hidden parameter, and the learner has to recover the parameter.) Unlike in PAC learning, distribution learning lacks an efficient verification, and therefore its hardness will not be broken with access to a QCMA oracle. On the other hand, because the power of PP is enough to estimate quantum probability distributions [FR99], hardness of quantum distribution learning should be broken with access to a PP oracle.

Moreover, distribution learning is among the most standard learning models, and has long been studied in the field of learning theory [Yat85, AW92, KMR + 94, DL01, DKK + 19, BKM20, HN23]. This makes it a natural and well-motivated candidate for exploring connections to OWPuzzs.

OWPuzzs and distribution learning. Our first main result is the complete characterization of OWPuzzs with hardness of distribution learning.

Theorem 1.1. OWPuzzs exist if and only if proper quantum distribution learning is average-case hard.

Proper quantum distribution learning is a quantum analogue of proper distribution learning introduced in [KMR + 94]. 2 Let D be a QPT algorithm that, on input a bit string z , outputs a bit string. In proper quantum distribution learning, the learner is given samples x 1 , ..., x t independently sampled from the distribution D ( z ) without knowing z , and has to output a hypothesis z ∗ such that SD ( D ( z ) , D ( z ∗ )) ≤ ϵ , where SD is the statistical distance. We consider the average-case hardness of this task, namely, z is sampled from a QPT algorithm S , and the probability (over S , D ( z ) , and the learner's algorithm) that the learner outputs z ∗ such that SD ( D ( z ) , D ( z ∗ )) ≤ ϵ should be small for any QPT learner.

2 The word proper means that the learner has to output a hypothesis that is inside of the learning class (which is {D ( z ) } z in the current case). If the learner can output any distribution that is close to the learning distribution, it is called improper.

̸

PP = BQP and distribution learning. In our first result above, Theorem 1.1, we have shown that average-case hardness of proper quantum distribution learning is equivalent to the existence of OWPuzzs. A natural question raised from this result is whether the worst-case hardness of proper quantum distribution learning is implied by PP = BQP . If this is the case, and if the worst-case to average-case hardness reduction within proper quantum distribution learning is achieved, OWPuzzs is obtained solely from PP = BQP ! Unfortunately, showing worst-case hardness of proper quantum distribution learning from PP = BQP seems to be extremely difficult. This is suggested from the following our second result.

̸

̸

Theorem 1.2. If the worst-case hardness of proper quantum distribution learning is PP -hard in a PPT-black box reduction, then PP ̸⊆ BPP Σ P 3 implies SampBQP = SampBPP .

̸

It is a long-standing open problem in the field of quantum advantage whether sampling-based quantum advantage is derived solely from the infiniteness of the polynomial-time hierarchy. (In fact, [AC17] showed that such a proof should be non-relativized.) Hence showing the worst-case hardness of proper quantum distribution learning from PP = BQP seems to be extremely challenging (at least in a black-box reduction).

̸

We are thus led to consider an alternative question: can PP = BQP be characterized with any standard hardness notion of distribution learning? Interestingly, PP = BQP can be characterized with another well-studied notion of hardness, namely, agnostic . We show the following result.

̸

̸

Theorem 1.3. PP = BQP if and only if agnostic quantum distribution learning with respect to the KL divergence is hard.

Let us explain what is agnostic quantum distribution learning. Let D be a QPT algorithm that takes a bit string z as input and outputs a bit string. In agnostic quantum distribution learning, the learner receives samples x 1 , ..., x T independently sampled from an unknown distribution T , which is not necessarily contained in {D ( z ) } z . The goal of the learner is to output a hypothesis z ∗ such that the KL divergence D KL ( T ‖ D ( z ∗ )) is close to the optimal value, min z D KL ( T ‖ D ( z )) . The hardness means that no QPT learner can, with high probability, output such a near-optimal z ∗ . Agnostic distribution learning has been well studied in the learning theory [Yat85, AW92, KMR + 94, DL01, DKK + 19, BKM20, HN23].

̸

In summary, we have characterized OWPuzzs and PP = BQP with two standard and well-studied hardness notions of distribution learning, namely, proper and agnostic, respectively. A natural and important question is whether these two notions of hardness can be connected. If such a connection could be established, it would lead to a construction of OWPuzzs solely from PP = BQP ! However, establishing this connection is extremely challenging and lies beyond the scope of the present paper. Even in the classical setting, only characterizing cryptographic primitives with hardness of learning has been considered a significant achievement [BFKL94, NR06, NY15, HN23], and, to date, no one has succeeded in connecting different notions of hardness except for a very recent partial progress in [HN23]. Therefore we believe that our first complete characterizations of OWPuzzs and PP = BQP with hardness of distribution learning constitute a meaningful contribution to the field of quantum cryptography, and represent an important first step toward the ultimate goal of constructing OWPuzzs from PP = BQP .

̸

̸

̸

̸

̸

As previously discussed, studying the connection between the hardness of learning and quantum cryptography has another important implication: it may provide valuable insights into identifying concrete hardness assumptions on which quantum cryptographic primitives can be based like Learning Parity with Noise (LPN) and Learning with Errors (LWE) assumptions [BFKL94, Reg05] in classical cryptography. Establishing quantum cryptographic primitives based on concrete mathematical hard problems is one of the central goals in the field. We hope that our characterizations of OWPuzzs with hardness of learning will contribute to the discovery of such concrete assumptions for quantum setting.

In addition to the main results above, we also obtain several interesting additional results, which we will explain in the following. Figure 1 also provides a summary of our results.

Sampling-based quantum advantage from hardness of learning. Sampling-based quantum advantage [AA11, BMS16] refers to the existence of a distribution that can be sampled by a QPT algorithm but not by any PPT algorithm. Sampling-based quantum advantage has been shown for several 'subuniversal' quantum computing models including random circuits [BFNV19], Boson sampling [AA11], IQP [BJS11, BMS16], and the one-clean-qubit model [FKM + 18, Mor17]. So far, sampling-based quantum advantage is obtained from the combination of two assumptions. One is PP ̸⊆ BPP NP . The other is a more complicated assumption, which we call 'quantum advantage assumption' for simplicity 3 . Although the quantum advantage assumption has been extensively studied for over a decade and some progress has been made [BFNV19, Mov23], the assumption itself remains unproven. Moreover, it is a newly introduced assumption devised specifically for this purpose, and has not been explored in any other areas. Therefore, an important open problem in the field is to derive sampling-based quantum advantage from a more standard and natural assumption.

We show the following two results.

Theorem 1.4. If the quantum advantage assumption holds and PP ̸⊆ BQP Σ P 3 , then agnostic quantum distribution learning with respect to the statistical distance is hard against QPT algorithms with access to a Σ P 3 oracle.

̸

Theorem 1.5. Suppose that agnostic quantum distribution learning with respect to the statistical distance is hard against PPT algorithms with access to a Σ P 3 oracle. Then, SampBQP = SampBPP .

̸

These two theorems mean that hardness of agnostic quantum distribution learning is implied by the quantum advantage assumption (plus PP ̸⊆ BQP Σ P 3 ), and implies SampBQP = SampBPP . (See also Figure 1.) This in particular means that sampling-based quantum advantage can be derived from potentially weaker and more natural assumption, namely, hardness of agnostic quantum distribution learning. As far as we know, this is the first time that sampling-based quantum advantage is derived from a hardness assumption on a standard and natural framework of learning. Moreover, hardness of agnostic learning is a worst-case hardness, and therefore our result shows (for the first time) that sampling-based quantum advantage can be derived solely from a worst-case hardness assumption. This is an important advantage, because in general showing worst-case hardness is easier than average-case hardness.

Relation between statistical distance and KL divergence. In this paper, we have studied two different notions of hardness of agnostic quantum distribution learning, namely, with respect to the statistical distance and to the KL divergence. It is natural to ask how they are related. We show the following.

3 That is so-called 'anti-concentration' and 'average-case # P -hardness'. See Assumption 2.10 for details.

Theorem 1.6. The hardness of agnostic quantum distribution learning with respect to the statistical distance implies that with respect to the KL divergence.

This result is actually obtained as a corollary of the following technical result, which is an upper bound of the complexity of agnostic quantum distribution learning with respect to the statistical distance.

Theorem1.7. If PP ⊆ BQP , then there exists a QPT algorithm which achieves agnostic quantum distribution learning with respect to the statistical distance.

̸

How about the opposite direction? Does the hardness of agnostic quantum distribution learning with respect to the KL divergence imply that with respect to the statistical distance? Showing it seems to be extremely difficult because from the following theorem, Theorem 1.8, 4 if the hardness of agnostic quantum distribution learning with respect to the statistical distance implies PP = BQP , then SampBQP = SampBPP can be obtained solely from the infiniteness of the polynomial-time hierarchy.

̸

̸

Theorem 1.8. If the hardness of agnostic quantum distribution learning with respect to the statistical distance is PP -hard in a PPT-black box reduction, then PP ̸⊆ BPP Σ P 3 implies SampBQP = SampBPP .

Classical results. Although our primary focus is on quantum learning, our proof techniques are also applicable to the classical setting, and in fact yield several new classical results. Our first result is the equivalence between the existence of OWFs and hardness of classical distribution learning.

Theorem 1.9. The following three conditions are equivalent:

1. OWFs exist.
2. Average-case hardness of proper classical distribution learning holds.
3. Average-case hardness of improper classical distribution learning holds.

The equivalence between 1 and 3 is actually known result [HN23], and the direction from 3 to 2 is trivial. (However, for the convenience of readers, here we have combined all results as a single theorem.) The direction from 2 to 1 is our new result, which is an improvement of the direction from 3 to 1 shown in [HN23]. The technique of [HN23] cannot be directly used to show 1 from 2, but here we introduce a new technique that overcomes the issue. Moreover, also for the direction from 3 to 1, we provide a simpler proof than that of [HN23]. In the classical setting, as Theorem 1.9 shows, proper and improper learning are equivalent. On the other hand, in the quantum case, we do not know how to show the equivalence of proper and improper learning, because PRFs are used to show 3 from 1 in the classical proof.

Our second classical result is the characterization of NP ⊈ BPP .

Theorem 1.10. The following three conditions are equivalent:

1. NP ⊈ BPP .
2. Hardness of agnostic classical distribution learning with respect to KL divergence holds.
3. Worst-case hardness of classical maximum likelihood estimation holds.

4 Theorem 1.2 is actually a corollary of Theorem 1.8

The equivalence between 2 and 3, and the direction from 1 to 3 were shown in [AW92]. Moreover, [AW92] cited a personal communication with Osamu Watanabe as the source of a proof of 1 from 3, but to the best of our knowledge, no explicit proof has appeared in the literature. In this paper, we provide such a proof and thereby complete the logical equivalence. In addition, we provide simpler proofs than those of [AW92].

Our final classical result is an upper bound of the complexity of agnostic classical distribution learning.

Theorem 1.11. There exists a PPT algorithm with access to a Σ P 3 oracle which achieves agnostic classical distribution learning with respect to the statistical distance.

In the field of classical learning, an upper bound of agnostic classical distribution learning with respect to the statistical distance was unknown.

## 1.2 Related Works

Distribution learning. The study of distribution learning has a long history and we cannot cover all results here. We only mention four related results.

[HN23] showed the equivalence between OWFs and the average-case hardness of several learning problems including distribution learning. Their proof for constructing OWFs from hardness of distribution learning can be directly used to construct OWPuzzs from hardness of quantum ditribution learning, but in that case we obtain OWPuzzs from hardness of improper learning. We use a completely different technique so that we can construct OWPuzzs from hardness of proper learning, which is stronger. On the other hand, their proof for showing hardness of distribution learning from OWFs cannot be used in our case, because their technique completely relies on classical properties. We therefore use another technique, but we do not know how to show hardness of improper learning from OWPuzzs.

[SSHE21, HIN + 23, PJSE24] considered distribution learning in the quantum regime. [HIN + 23] showed that specific families of quantum circuits are hard to learn under the LPN assumption. [SSHE21, PJSE24] showed existence of some quantum advantage in distribution learning task.

Quantum cryptography and hardness of learning quantum states. [BHHP24, HH24, FGSY25, PQS25] investigated relationships between quantum cryptography and hardness of learning quantum states with the motivation of basing quantum cryptographic primitives on hardness of learning. [FGSY25, HH24] showed the equivalence between the existence of OWSGs with pure-state outputs and average-case hardness of learning pure quantum states. [BHHP24] constructed OWSGs from hardness of obtaining classical descriptions of given pure states. [PQS25] introduced a hardness assumption what they call leaning stabilizers with noise and constructed EFIs from it.

̸

Quantum cryptography from concrete assumptions. The construction of OWPuzzs in [KT25] from quantum advantage assumption plus PP = BQP suggests several concrete assumptions for OWPuzzs implementable with sub-universal models such as random circuits and IQP.

̸

Quantum advantage and hardness of estimating quantum probability. [MSY25] showed that averagecase hardness of estimating quantum probability implies SampBQP = SampBPP , and therefore their hardness could also be considered as another assumption for sampling-based quantum advantage. However, our assumption, namely, hardness of agnostic quantum distribution learning, is worst-case hardness assumption, and therefore more advantageous than that of [MSY25].

̸

<!-- image -->

̸

Figure 1: A summary of results. Black lines are known results or trivial implications. Red lines are new in our work. avePQDL is average-case hardness of proper quantum distribution learning. worPQDL is worst-case hardness of proper quantum distribution learning. worQML is worst-case hardness of quantum maximum likelihood estimation. AgoQDL KL is hardness of agnostic quantum distribution learning with respect to the KL divergence. AgoQDL X Σ P 3 SD is hardness of agnostic quantum distribution learning with respect to the statistical distance against X = { PPT , QPT } learners with access to a Σ P 3 oracle. QAA stands for the quantum advantage assumption. The dotted line suggests that showing that implication seems to be difficult. (If it is shown, then SampBQP = SampBPP is derived from the infiniteness of the polynomial-time hierarchy.)

̸

Other characterizations of OWPuzzs. [CGGH25] and [HM24] showed the equivalence between the existence of OWPuzzs and hardness of estimating Kolmogorov complexity. These two papers and [KT25] also showed the equivalence between the existence of OWPuzzs and hardness of estimating quantum probability.

## 1.3 Technical Overview

In this subsection, we provide a high-level overview of the proofs of our main results.

Proof of Theorem 1.1. Let us first explain our proof of Theorem 1.1, which is the equivalence between OWPuzzs and average-case hardness of proper quantum distribution learning. We first explain how to construct OWPuzzs from average-case hardness of proper quantum distribution learning. To show it, we first assume average-case hardness of proper quantum distribution learning. This means that there exist a QPT algorithm S that samples a hidden parameter z , and a QPT algorithm D that takes z as input, and outputs a bit string x . The hardness of learning requires that, for any polynomial t and any QPT algorithm that receives x 1 , . . . , x t independently sampled from D ( z ) , it is hard to find z ∗ such that SD ( D ( z ∗ ) , D ( z )) is small.

We construct a OWPuzz, ( Samp , Vrfy ) , from such S and D as follows. Samp algorithm samples z from S and independently samples x 1 , . . . , x t from D ( z ) . It then outputs ans := z and puzz := { x i } i ∈ [ t ] . Next, Vrfy algorithm takes ans ∗ = h and puzz = { x i } i ∈ [ t ] as input. It first computes z ∗ such that

$$\Pr \left [ \{ x _ { i } \} _ { i \in [ t ] } \leftarrow \mathcal { D } ( z ^ { * } ) \right ] = \max _ { a } \Pr \left [ \{ x _ { i } \} _ { i \in [ t ] } \leftarrow \mathcal { D } ( a ) \right ] .$$

Then, Vrfy outputs 1 if D ( z ∗ ) is statistically close to D ( h ) , and outputs 0 if D ( z ∗ ) is statistically far from D ( h ) .

We can show that, D ( z ∗ ) and D ( z ) are statistically close with high probability over z ← S and x 1 , . . . , x t ←D ( z ) ⊗ t . Therefore, in order to output h such that 1 ← Vrfy ( { x i } i ∈ [ t ] , h ) , the adversary must produce h such that D ( h ) is close to D ( z ) . However, this is prohibited by the average-case hardness of proper quantum distribution learning. Therefore, the security of the OWPuzz follows.

Next, let us explain how to show average-case hardness of proper quantum distribution learning from OWPuzzs. [KT24, CGG24] showed that OWPuzzs imply non-uniform QPRGs (nuQPRGs). Therefore, it is sufficient to show average-case hardness of proper quantum distribution learning from nuQPRGs. A nuQPRG is a QPT algorithm Gen that takes an advice string µ ∈ [ n ] as input, and outputs n -bit strings. The security guarantees that there exists a µ ∗ ∈ [ n ] such that Gen ( µ ∗ ) is statistically far but computationally indistinguishable from the uniform distribution U n .

We show the average-case hardness of proper quantum distribution learning from nuQPRGs, Gen . We construct a pair ( S , D ) of QPT algorithms as follows. S samples µ ← [ n ] and b ←{ 0 , 1 } , and outputs ( µ, b ) . D takes ( µ, b ) as input, and outputs ( µ, x ) , where x ← U n if b = 1 , and x ← Gen ( µ ) if b = 0 . For the sake of contradiction, suppose that ( S , D ) is not average-case hard to learn. This means that there exists a QPT algorithm A , given samples ( µ, x 1 ) , ..., ( µ, x t ) independently sampled from D ( µ, b ) (with ( µ, b ) ←S ), that can output ( µ ∗ , b ∗ ) such that D ( µ ∗ , b ∗ ) is statistically close to D ( µ, b ) .

Because the first output of D ( µ, b ) is µ , the first output µ ∗ of A has to be equal to µ : otherwise, SD ( D ( µ, b ) , D ( µ ∗ , b ∗ )) cannot be small. Moreover, if µ is such that Gen ( µ ) is statistically far from the uniform distribution, A 's second output b ∗ has to be equal to b , because otherwise SD ( D ( µ, b ) , D ( µ, b ∗ )) cannot be small.

Therefore, from such A , we can construct a QPT algorithm B that breaks the security of Gen as follows. Let Good be the set of all µ ∈ [ n ] such that Gen ( µ ) is statistically far from U n . Our construction of B is as follows: On input x 1 , ..., x t independently sampled from Gen ( µ ∗ ) or U n , B runs A (( µ, x 1 ) , ..., ( µ, x t )) for all µ ∈ Good . B outputs 1(0) if A outputs 1(0) for all µ ∈ Good . As we have explained above, A outputs 1(0) for all µ ∈ Good with high probability if x 1 , ..., x t are sampled from U n ( Gen ), and therefore, B breaks the security of Gen .

However, one issue in the construction is that we do not know how to obtain Good in QPT. We therefore define another set Good ′ that is the set of all µ ∈ [ n ] such that Pr ( y 1 ,...,y t ) ← U ⊗ t n [1 ←A (( µ, y 1 ) , ..., ( µ, y t ))] is large. Such a set can be obtained in QPT, and therefore B can find it by itself. It is easy to verify that Good ⊆ Good ′ . Therefore, if we modify B as follows, B can correctly distinguish Gen and U n : B first computes the set Good ′ . On input x 1 , ..., x t independently sampled from Gen ( µ ∗ ) or U n , B runs A (( µ, x 1 ) , ..., ( µ, x t )) for all µ ∈ Good ′ . B outputs 1 if A outputs 1 for all µ ∈ Good ′ . B outputs 0 if A outputs 0 for at least one µ ∈ Good ′ .

̸

Proof of Theorem 1.3. Let us next explain our proof of Theorem 1.3, which is the equivalence between BQP = PP and hardness of agnostic quantum distribution learning with respect to KL divergence. Our key idea is to introduce the worst-case hardness of quantum maximum likelihood (QML) estimation as an intermediate object. Let D be a QPT algorithm that, on input a bit string z , outputs a bit string x . Worst-case hardness of QML means that there exists a bit string x such that no QPT learner given x can find z ∗ such that Pr[ x ←D ( z ∗ )] is close to max z Pr[ x ←D ( z )] . Intuitively, the worst-case hardness of QML is equivalent to the hardness of agnostic quantum distribution learning, but we focus on the former, because it is more convenient to show the equivalence to BQP = PP . 5

̸

̸

Hence our goal is to show the equivalence between the worst-case hardness of QML and BQP = PP . [HH24] already showed BQP = PP from the worst-case hardness of QML. Therefore the remaining task is to show the other direction.

̸

Let L be a language in PP = PostBQP . Then, there exists a QPT algorithm M such that Pr ( b,b ∗ ) ←M ( x ) [ b = 1 | b ∗ = 1] ≥ 2 3 for all x ∈ L , and Pr ( b,b ∗ ) ←M ( x ) [ b = 1 | b ∗ = 1] ≤ 1 3 for all x ̸∈ L . For the QPT algorithm M , we consider M ∗ ( x, c ) that runs ( b, b ∗ ) ←M ( x ) , and outputs x if b = c and b ∗ = 1 , and outputs ⊥ otherwise. Crucially, if x ∈ L , then Pr[ x ←M ∗ ( x, 1)] is much larger than Pr[ x ←M ∗ ( x, 0)] while if x ̸∈ L , then Pr[ x ←M ∗ ( x, 0)] is much larger than Pr[ x ←M ∗ ( x, 1)] . Therefore, if QML is easy in the worst-case setting, we can check if x ∈ L or x ̸∈ L in QPT by doing the maximum likelihood estimation of M ∗ .

Proof of Theorem 1.11 Theorem 1.11 is the construction of a PPT algorithm with access to a Σ P 3 oracle that can achieve agnostic classical distribution learning with respect to the statistical distance. Let T be an unknown algorithm that outputs classical bit strings, and let D be a known QPT algorithm that takes an n -bit string z as input, and outputs a classical bit string x . The learner receives x 1 , ..., x t independently sampled from T , and has to find z ∗ such that SD ( D ( z ∗ ) , T ) is small.

In order to make our explanation simpler, let us first assume that D 's input z is just a single bit. In this setting, access to an NP oracle, not a Σ P 3 oracle, is enough. Given x 1 , ..., x t independently sampled from T , the learner has to find b ∈ { 0 , 1 } such that T is statistically closer to D ( b ) than D ( b ⊕ 1) . How can we do that? By the definition of the statistical distance, there exists an unbounded algorithm Dis such that

$$| \Pr [ 1 \leftarrow \text {Dis} ( x ) \colon x \leftarrow \mathcal { D } ( 1 ) ] - \Pr [ 1 \leftarrow \text {Dis} ( x ) \colon x \leftarrow \mathcal { D } ( 0 ) ] | = \text {SD} ( \mathcal { D } ( 0 ) , \mathcal { D } ( 1 ) ) .$$

Given x 1 , ..., x t as input, which is independently sampled from T , the learner first estimates the value of Pr[1 ← Dis ( x ) : x ←T ] . It then outputs 0 (1) if the estimated value of Pr[1 ← Dis ( x ) : x ←T ] is closer to that of Pr[1 ← Dis ( x ) : x ←D (0)] ( Pr[1 ← Dis ( x ) : x ←D (1)] ). The reason why this learning algorithm works can be easily understood from the inequality

5 Although they are equivalent at the intuition level, showing the equivalence is non-trivial, and we carefully show their equivalence, which is also our technical contribution.

$$| \Pr [ 1 \leftarrow \text {Dis} ( x ) \colon x \leftarrow \mathcal { T } ] - \Pr [ 1 \leftarrow \text {Dis} ( x ) \colon x \leftarrow \mathcal { D } ( b ) ] | \leq \text {SD} ( \mathcal { T } , \mathcal { D } ( b ) ) .$$

This learning algorithm can be implemented with access to an NP oracle, because Dis is the algorithm that takes x as input and outputs b if x is more likely from D ( b ) , and such an algorithm can be implemented with the Stockmeyer theorem [Sto83]: a PPT algorithm with access to an NP oracle can approximate classical probability distributions. Hence, in this simplified setting, a PPT algorithm with access to an NP oracle can achieve agnostic distribution learning.

Next let us consider the actual case where D 's input z is an n -bit string. Again, from the definition of the statistical distance, there exists an unbounded algorithm Dis such that

$$| \Pr [ 1 \leftarrow \text {Dis} ( a , b , x ) \colon x \leftarrow \mathcal { D } ( a ) ] - \Pr [ 1 \leftarrow \text {Dis} ( a , b , x ) \colon x \leftarrow \mathcal { D } ( b ) ] | = \text {SD} ( \mathcal { D } ( a ) , \mathcal { D } ( b ) )$$

for all a and b . Given x 1 , ..., x t independently sampled from T , the learner first estimates the value of Pr[1 ← Dis ( a, b, x ) : x ←T ] for all a, b . The learner outputs a ∗ such that

$$| \Pr [ 1 \leftarrow D i s ( a ^ { * } , b , x ) \colon x \leftarrow \mathcal { T } ] - \Pr [ 1 \leftarrow D i s ( a ^ { * } , b , x ) \colon x \leftarrow \mathcal { D } ( a ^ { * } ) ] |$$

is small for all b . The reason why this learning algorithm works can be understood from the following inequality:

$$\text {SD} ( \mathcal { T } , \mathcal { D } ( a ) ) & \leq \text {SD} ( \mathcal { T } , \mathcal { D } ( b ) ) + \text {SD} ( \mathcal { D } ( a ) , \mathcal { D } ( b ) ) \\ & = \text {SD} ( \mathcal { T } , \mathcal { D } ( b ) ) + | \Pr [ 1 \leftarrow \text {Dis} ( a , b , x ) \, \colon x \leftarrow \mathcal { D } ( b ) ] - \Pr [ 1 \leftarrow \text {Dis} ( a , b , x ) \, \colon x \leftarrow \mathcal { D } ( a ) ] |$$

$$& = \text {SD} ( \mathcal { T } , \mathcal { D } ( b ) ) + | \Pr [ 1 \leftarrow \text {Dis} ( a , b , x ) \colon x \leftarrow \mathcal { D } ( b ) ] - \Pr [ 1 \leftarrow \text {Dis} ( a , b , x ) \colon x \leftarrow \mathcal { D } ( a ) ] | \\ & \leq \text {SD} ( \mathcal { T } , \mathcal { D } ( b ) ) + | \Pr [ 1 \leftarrow \text {Dis} ( a , b , x ) \colon x \leftarrow \mathcal { D } ( b ) ] - \Pr [ 1 \leftarrow \text {Dis} ( a , b , x ) \colon x \leftarrow \mathcal { T } ] | \quad ( 8 ) \\ & \quad + | \Pr [ 1 \leftarrow \text {Dis} ( a , b , x ) \colon x \leftarrow \mathcal { T } ] - \Pr [ 1 \leftarrow \text {Dis} ( a , b , x ) \colon x \leftarrow \mathcal { D } ( a ) ] | \\ & \leq 2 \text {SD} ( \mathcal { T } , \mathcal { D } ( b ) ) + | \Pr [ 1 \leftarrow \text {Dis} ( a , b , x ) \colon x \leftarrow \mathcal { T } ] - \Pr [ 1 \leftarrow \text {Dis} ( a , b , x ) \colon x \leftarrow \mathcal { D } ( a ) ] | , \\$$

which suggests that in order to minimize SD ( T , D ( a )) ,

$$| \Pr [ 1 \leftarrow D i s ( a , b , x ) \colon x \leftarrow \mathcal { T } ] - \Pr [ 1 \leftarrow D i s ( a , b , x ) \colon x \leftarrow \mathcal { D } ( a ) ] |$$

has to be minimized over a .

Finally, with a careful investigation, we show that the learning algorithm can be implemented with access to a Σ P 3 oracle. 6

̸

Proof of Theorem 1.5. In the following, we explain our proof of Theorem 1.5, which is SampBQP = SampBPP from hardness of agnostic quantum distribution learning with respect to the statistical distance against PPT Σ P 3 learner. Let T be an unknown algorithm that outputs classical bit strings, and let D be a known QPT algorithm that takes a bit string z as input and outputs a classical bit string x . The learner who receives x ←T has to find z ∗ such that D ( z ∗ ) is statistically close to T .

For the sake of contradiction, assume that SampBQP = SampBPP . Then, there exists a PPT algorithm C such that SD ( D ( z ) , C ( z )) is small for all z . Hence, given samples x 1 , . . . , x t from T , it is sufficient to find z ∗ such that C ( z ∗ ) is statistically close to T , which is agnostic classical distribution learning. From Theorem 1.11, it is possible with access to a Σ P 3 oracle.

6 We do not know whether Σ P 3 is optimal. This could be improved.

̸

Proof of Theorem 1.2. Theorem 1.2 states that if the worst-case hardness of proper quantum distribution learning is PP -hard (via a black-box reduction), then PP ⊈ BPP Σ P 3 implies SampBQP = SampBPP . In order to show it, assume that the worst-case hardness of proper quantum distribution learning can be reduced to the PP -hardness. Let us also assume that SampBQP = SampBPP . It is straightforward that the worstcase hardness of proper quantum distribution learning implies the hardness of agnostic quantum distribution learning with respect to the statistical distance. From the assumption of SampBQP = SampBPP , the latter implies the hardness of agnostic classical distribution learning with respect to the statistical distance. From Theorem 1.11, this is broken by a PPT algorithm with access to a Σ P 3 oracle. Therefore, PP ⊆ BPP Σ P 3 .

## 2 Preliminaries

## 2.1 Basic Notations

We introduce basic notations and mathematical tools used in this paper.

We use the standard notations of cryptography and quantum information. [ n ] denotes the set { 1 , 2 , ..., n } . negl is a negligible function. poly is a polynomial. QPT stands for quantum polynomial time, and PPT stands for classical probabilistic polynomial time. For an algorithm (or a Turing machine) A , y ←A ( x ) means that A runs on input x and outputs y . When we explicitly show that A uses randomness r , we write y ←A ( x ; r ) . The notation { y i } i ∈ [ N ] ←A ⊗ N ( x ) means that A is run on input x independently N times, and y i is the i th result. For any distribution D , a ← D means that a is sampled according to the distribution D . For any set S , a ← S means that a is sampled uniformly at random from S . We denote U n to mean a uniform distribution over { 0 , 1 } n . For two distributions D and E , we write SD ( D,E ) or SD ( x x ← D , x x ← E ) to mean the statistical distance between two distributions D and E , and we write D KL ( D ‖ E ) := ∑ a Pr[ a ← D ] log ( Pr[ a ← D ] Pr[ a ← E ] ) to mean the KL-divergence from D to E . If A is an algorithm that outputs bit strings, we often denote A by the output distribution of A when it is clear from the context.

## 2.2 Lemmas

We introduce lemmas, which we use in this paper.

Lemma 2.1. Let M,ϵ,δ &gt; 0 and let F M := { f : { 0 , 1 } ∗ → [0 , M ] } be a family of functions such that |F M | is finite. Let T be an integer such that

$$T \geq \frac { M ^ { 2 } } { \epsilon ^ { 2 } } | \log | \mathcal { F } _ { M } | + \log ( 1 / \delta ) | .$$

Let D be a distribution over { 0 , 1 } ∗ . We have

$$\Pr \left [ \left | \frac { 1 } { T } \sum _ { i \in [ T ] } f ( x _ { i } ) - \mathbb { E } _ { x \prec \mathcal { D } } [ f ( x ) ] \right | \leq \epsilon \text { for all } f \in \mathcal { F } _ { M } \colon \{ x _ { i } \} _ { i \in [ T ] } \leftarrow \mathcal { D } ^ { \otimes T } \right ] \geq 1 - \delta .$$

Here, { z i } i ∈ [ T ] ←D ⊗ T means that each z i is independently sampled from D .

Lemma 2.1 directly follows from Hoeffding's inequality and the union bound. Therefore, we omit the proof.

The following theorem guarantees that for all PPT algorithms D , which takes 1 n as input, and outputs a classical string x , there exists a PPT algorithm with access to an NP oracle that can estimate Pr[ x ←D (1 n )] within 1 / poly -multiplicative error for all x ∈ { 0 , 1 } ∗ and for all sufficiently large n ∈ N .

Theorem 2.2 ([Sto83]). For any polynomial ϵ , and any PPT algorithm D which takes 1 n as input, and outputs x ∈ { 0 , 1 } poly( n ) , there exists a PPT algorithm Estimate with access to an NP oracle such that, for all x ∈ { 0 , 1 } n , we have

$$\Pr \left [ \text {Estimate} ^ { N P } ( 1 ^ { n } , x ) - \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } ) ] \right | \leq \frac { \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } ) ] } { \epsilon ( n ) } \right ] \geq 1 - 1 / \epsilon ( n )$$

for all sufficiently large n ∈ N .

In this paper, we will use the following Theorem 2.3, which generalizes Theorem 2.2. The difference is that, in Theorem 2.3, the PPT algorithm D takes a classical bit string z ∈ { 0 , 1 } n in addition to the security parameter 1 n as input.

Theorem 2.3. For any polynomial ϵ , and for any PPT algorithm D that takes 1 n and z ∈ { 0 , 1 } n as input, and outputs x ∈ { 0 , 1 } poly( n ) , there exists a PPT algorithm Estimate with access to an NP oracle such that, for all ( z, x ) ∈ { 0 , 1 } n ×{ 0 , 1 } poly( n ) , we have

$$\Pr \left [ | \text {Estimate} ( 1 ^ { n } , z , x ) - \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , z ) ] | \leq \frac { \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , z ) ] } { \epsilon ( n ) } \right ] \geq 1 - 1 / \epsilon ( n )$$

for all sufficiently large n ∈ N .

Proof of Theorem 2.3. For an arbitrary PPT algorithm D , which takes 1 n and z ∈ { 0 , 1 } n as input, and outputs x ∈ { 0 , 1 } poly( n ) , we consider another PPT algorithm D ∗ that takes 1 n as input, and uniformly randomly samples z ←{ 0 , 1 } n and outputs ( z, D (1 n , z )) . From the construction of D ∗ , we have Pr[ x ←D (1 n , z )] = 2 n Pr[( z, x ) ←D ∗ (1 n )] . On the other hand, from Theorem 2.2, there exists a PPT algorithm with access to an NP oracle that can estimate Pr[( z, x ) ←D ∗ (1 n )] for all x ∈ { 0 , 1 } poly( n ) and z ∈ { 0 , 1 } n . Therefore, a PPT algorithm with access to an NP oracle can estimate Pr[ x ←D (1 n , z )] for all x ∈ { 0 , 1 } poly( n ) and z ∈ { 0 , 1 } n .

## 2.3 Complexity Classes

We introduce basic complexity classes, which we consider in this paper.

Definition 2.4 ([Aar05]). PostBQP is the class of language L ⊆ { 0 , 1 } ∗ for which there exist a polynomial p , and a QPT algorithm M , which takes x ∈ { 0 , 1 } ∗ as input and outputs ( b, b ∗ ) ∈ { 0 , 1 } × { 0 , 1 } such that for all x ∈ { 0 , 1 } ∗ , the following three conditios are satisfied:

1. Pr[ b ∗ = 1 : ( b, b ∗ ) ←M ( x )] ≥ 2 -p ( | x | ) .
2. If x ∈ L , then we have Pr[ b = 1 : ( b, 1) ←M ( x )] ≥ 2 3 .
3. If x / ∈ L , then we have Pr[ b = 1 : ( b, 1) ←M ( x )] ≤ 1 3 .

Definition 2.5. Σ P 3 is the class of language L ⊆ { 0 , 1 } ∗ for which there exist polynomials p , q , and r , and a deterministic polynomial time algorithm M , which takes x ∈ { 0 , 1 } ∗ , a ∈ { 0 , 1 } p ( | x | ) , b ∈ { 0 , 1 } q ( | x | ) , and c ∈ { 0 , 1 } r ( | x | ) such that, for all x ∈ { 0 , 1 } ∗ , the following two conditions are satisfied:

1. If x ∈ L , then there exists a ∈ { 0 , 1 } p ( | x | ) , such that for all b ∈ { 0 , 1 } q ( | x | ) , there exists c ∈ { 0 , 1 } r ( | x | ) such that we have M ( x, a, b, c ) = 1 .

2. If x / ∈ L , then for all a ∈ { 0 , 1 } p ( | x | ) , there exists b ∈ { 0 , 1 } q ( | x | ) such that for all c ∈ { 0 , 1 } r | x | , M ( x, a, b, c ) = 0 .

Definition 2.6. Σ PP 2 is the class of language L ⊆ { 0 , 1 } ∗ for which there exist polynomials p and q , and a deterministic polynomial time algorithm M with access to a PP oracle, which takes x ∈ { 0 , 1 } ∗ , a ∈ { 0 , 1 } p ( | x | ) , and b ∈ { 0 , 1 } q ( | x | ) such that for all x ∈ { 0 , 1 } ∗ , the following two conditions are satisfied:

1. If x ∈ L , then there exists a ∈ { 0 , 1 } p ( | x | ) , such that for all b ∈ { 0 , 1 } q ( | x | ) , we have M PP ( x, a, b ) = 1 .
2. If x / ∈ L , then for all a ∈ { 0 , 1 } p ( | x | ) , there exists b ∈ { 0 , 1 } q ( | x | ) such that M PP ( x, a, b ) = 0 .

Definition 2.7 (Sampling Problems [Aar14, ABK24]). A sampling problem is a collection of probability distributions { D x } x ∈{ 0 , 1 } ∗ , where each D x is a probability distribution over { 0 , 1 } p ( x ) for some fixed polynomial p .

Definition 2.8 (SampBQP [Aar14, ABK24]). SampBQP is a class of sampling problems { D x } x ∈{ 0 , 1 } ∗ for which there exists a uniform QPT algorithm Q such that for all x ∈ { 0 , 1 } ∗ and for all ϵ &gt; 0 , SD ( Q (1 ⌊ 1 /ϵ ⌋ , x ) , D x ) ≤ ϵ .

Definition 2.9 (SampBPP [Aar14, ABK24]). SampBPP is a class of sampling problems { D x } x ∈{ 0 , 1 } ∗ for which there exists a uniform PPT algorithm C such that for all x ∈ { 0 , 1 } ∗ and for all ϵ &gt; 0 , SD ( C (1 ⌊ 1 /ϵ ⌋ , x ) , D x ) ≤ ϵ .

## 2.4 Quantum Advantage Assumption

We introduce quantum advantage assumption.

Assumption 2.10 (Quantum Advantage Assumption [AA11, BMS16, KT25]). We say that quantum advantage assumption holds if both of the following two conditions are satisfied:

1. There exists a family C = {C n } n ∈ N of distributions such that for each n ∈ N , C n is a (uniform) QPT sampleable distribution over quantum circuits C , which takes 1 n as input, and outputs n -bit classical bit strings.
2. There exist polynomials p and γ such that:
3. (a) For all sufficiently large n ∈ N ,

$$\Pr \left [ \Pr [ x \leftarrow C ( 1 ^ { n } ) ] \geq \frac { 1 } { p ( n ) 2 ^ { n } } \colon C \leftarrow \mathcal { C } _ { n } , x \leftarrow \{ 0 , 1 \} ^ { n } \right ] \geq \frac { 1 } { \gamma ( n ) } .$$

- (b) For any oracle O satisfying that for all sufficiently large n ∈ N ,

$$\Pr \left [ | \mathcal { O } ( C , x ) - \Pr [ x \leftarrow C ( 1 ^ { n } ) ] | \leq \frac { \Pr [ x \leftarrow C ( 1 ^ { n } ) ] } { p ( n ) } \colon C \leftarrow \mathcal { C } _ { n } , x \leftarrow \{ 0 , 1 \} ^ { n } \right ] \geq \frac { 1 } { \gamma ( n ) } - \frac { 1 } { p ( n ) } ,$$

we have that P # P ⊆ BPP O .

## 2.5 Cryptographic Primitives

We introduce cryptographic primitives used in this paper.

Definition 2.11 (One-Way Functions (OWFs)). A function f : { 0 , 1 } ∗ → { 0 , 1 } ∗ that is computable in classical deterministic polynomial-time is a classically-secure one-way function (OWF) if for any PPT adversary A ,

$$\Pr [ f ( x ^ { \prime } ) = f ( x ) \colon x \leftarrow \{ 0 , 1 \} ^ { n } , x ^ { \prime } \leftarrow \mathcal { A } ( 1 ^ { n } , f ( x ) ) ] \leq \text {neg} ( n ) .$$

Definition 2.12 (Classical One-Way Puzzles (OWPuzzs) [KT24]). Let p be a polynomial. A classical one-way puzzle (OWPuzz) with ( 1 -1 p ( n ) ) -security is a pair ( Samp , Vrfy ) of algorithms with the following syntax:

- Samp (1 n ) → ( ans , puzz ) : It is a PPT algorithm that, on input 1 n , outputs two classical bit strings ( ans , puzz ) .
- Vrfy ( ans ′ , puzz ) →⊤ / ⊥ : It is an unbounded algorithm that, on input ( ans ′ , puzz ) , outputs ⊤ / ⊥ .

We require the following correctness and security.

## Correctness:

$$\Pr [ \top \leftarrow V r f ( \text {ans} , \text {puzz} ) \colon ( \text {ans} , \text {puzz} ) \leftarrow S a m p ( 1 ^ { n } ) ] \geq 1 - \text {neg} ( n ) .$$

Security: For any uniform PPT algorithm A ,

$$\Pr [ \top \leftarrow \text {Vrf} ( \mathcal { A } ( 1 ^ { n } , \mu z z ) , \mu z z ) \colon ( \text {ans, } \mu z z ) \leftarrow \text {Samp} ( 1 ^ { n } ) ] \leq 1 - \frac { 1 } { p ( n ) } .$$

We call OWPuzzs with negl ( n ) security as OWPuzzs for simplicity.

Theorem 2.13 ([CGG24]). For any polynomial p , classical OWPuzzs exist if and only if classical OWPuzzs with ( 1 -1 p ( n ) ) -security exist.

It is shown that classical OWPuzzs exist if and only if OWFs exist.

Theorem 2.14 ([KT24]). Classical OWPuzzs exist if and only if OWFs exist.

Definition 2.15 (One-Way Puzzles (OWPuzzs) [KT24]). Let p be a polynomial. A one-way puzzle (OWPuzz) with ( 1 -1 p ( n ) ) -security is a pair ( Samp , Vrfy ) of algorithms with the following syntax:

- Samp (1 n ) → ( ans , puzz ) : It is a QPT algorithm that, on input 1 n , outputs two classical bit strings ( ans , puzz ) .
- Vrfy ( ans ′ , puzz ) →⊤ / ⊥ : It is an unbounded algorithm that, on input ( ans ′ , puzz ) , outputs ⊤ / ⊥ .

We require the following correctness and security.

## Correctness:

$$\Pr [ \top \leftarrow V r f ( \text {ans} , \text {puzz} ) \colon ( \text {ans} , \text {puzz} ) \leftarrow S a m p ( 1 ^ { n } ) ] \geq 1 - \text {neg} ( n ) .$$

Security: For any uniform QPT algorithm A ,

$$\Pr [ \top \leftarrow \text {Vrf} ( \mathcal { A } ( 1 ^ { n } , \mu z z ) , \mu z z ) \colon ( \text {ans, } \mu z z ) \leftarrow \text {Samp} ( 1 ^ { n } ) ] \leq 1 - \frac { 1 } { p ( n ) } .$$

We call OWPuzzs with negl ( n ) security as OWPuzzs for simplicity.

Theorem 2.16 ([CGG24]). For any polynomial p , OWPuzzs exist if and only if OWPuzzs with ( 1 -1 p ( n ) ) -security exist.

Definition 2.17 (non-uniform QPRGs (nuQPRGs)). A non-uniform QPRG is a QPT algorithm Gen (1 n , µ ) that takes a security parameter 1 n and µ ∈ [ n ] as input, and outputs a classical bit string x ∈ { 0 , 1 } n . We require that there exists µ ∗ ∈ [ n ] such that the following two conditions hold:

## Statistically far:

$$S D ( \text {Gen} ( 1 ^ { n } , \mu ^ { * } ) , U _ { n } ) \geq 1 - \text {neg} ! ( n ) .$$

Here, U n is the uniform distribution over { 0 , 1 } n .

Computationally indistinguishable: For any QPT algorithm A and any polynomial t ,

$$\left | \Pr \left [ 1 \leftarrow \mathcal { A } ( 1 ^ { n } , \{ x _ { i } \} _ { i \in [ t ( n ) ] } ) \colon \{ x _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow \text {Gen} ( 1 ^ { n } , \mu ^ { * } ) ^ { \otimes t ( n ) } \right ]$$

$$- \Pr \left [ 1 \leftarrow \mathcal { A } ( 1 ^ { n } , \{ x _ { i } \} _ { i \in [ t ( n ) ] } ) \colon \{ x _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow U _ { n } ^ { \otimes t ( n ) } \right ] \right | \leq \text {neg} ( n ) .$$

It is known that OWPuzzs are existentially equivalent to nuQPRGs.

Theorem 2.18 ([KT24, CGG24]). OWPuzzs exist if and only if nuQPRGs exist.

## 3 Average-Case Hardness of Proper Distribution Learning

## 3.1 Quantum Case

We introduce average-case hardness of proper quantum distribution learning, and show that it is equivalent to the existence of OWPuzss. We first define average-case hardness of proper quantum distribution learning. Our formalism is based on [KMR + 94, HN23].

Definition 3.1 (Average-Case Hardness of Proper Quantum Distribution Learning). We say that averagecase hardness of proper quantum distribution learning holds if the following holds. There exist some polynomials ϵ and δ , a QPT algorithm S , which takes 1 n as input, and outputs z ∈ { 0 , 1 } n , and a QPT algorithm D , which takes 1 n and z ∈ { 0 , 1 } n as input, and outputs x ∈ { 0 , 1 } poly( n ) , such that, for all QPT algorithms A and any polynomial t ,

$$\Pr \left [ \text {SD} ( \mathcal { D } ( 1 ^ { n } , z ) , \mathcal { D } ( 1 ^ { n } , h ) ) \leq 1 / \epsilon ( n ) \, \colon \quad & \{ x _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow \mathcal { D } ( 1 ^ { n } , z ) ^ { \otimes t ( n ) } \, \right ] \leq 1 - 1 / \delta ( n ) \quad ( 2 6 ) \\ & \quad h \leftarrow \mathcal { A } ( 1 ^ { n } , \{ x _ { i } \} _ { i \in [ t ( n ) ] } )$$

for all sufficiently large n ∈ N . Here, { x i } i ∈ [ t ( n )] ←D (1 n , z ) ⊗ t ( n ) means that D (1 n , z ) is run t ( n ) times, and x i is the i th output.

Remark 3.2. In the above definition, we require that Equation (26) holds for all sufficiently large security parameters instead of for infinitely many security parameters . This is because we want to show its equivalence to OWPuzzs instead of infinitely-often OWPuzzs. If we use the 'for infinitely many security parameters' security, we obtain the equivalence to infinitely-often OWPuzzs in a similar proof.

Theorem 3.3. The following two conditions are equivalent:

1. OWPuzzs exist.
2. Average-case hardness of proper quantum distribution learning holds.

Theorem 3.3 follows from the following Lemmata 3.4 and 3.5.

Lemma 3.4. If average-case hardness of proper quantum distribution learning holds, then OWPuzzs exist.

- Lemma 3.5. If OWPuzzs exist, then average-case hardness of proper quantum distribution learning holds.

In the following, we give the proofs.

Proof of Lemma 3.4. From Theorem 2.16, it is sufficient to construct OWPuzzs with ( 1 -1 p ( n ) ) security for some polynomial p .

Assume that average-case hardness of proper quantum distribution learning holds. Then, there exist polynomials ϵ and δ , a QPT algorithm S , which takes 1 n as input, and outputs z ∈ { 0 , 1 } n , and a QPT algorithm D , which takes 1 n , and z ∈ { 0 , 1 } n as input, and outputs x ∈ { 0 , 1 } poly( n ) such that for any polynomial t , and any QPT algorithm A ,

$$\Pr \left [ \text {SD} ( \mathcal { D } ( 1 ^ { n } , z ) , \mathcal { D } ( 1 ^ { n } , h ) ) \leq 1 / \epsilon ( n ) \colon \quad & \{ x _ { i } \} _ { i \in [ t ( n ) ] } \hookrightarrow \mathcal { D } ( 1 ^ { n } , z ) ^ { \otimes t ( n ) } \, \right ] \leq 1 - 1 / \delta ( n ) \quad ( 2 7 )$$

for all sufficiently large n ∈ N . From S and D , we construct OWPuzzs ( Samp , Vrfy ) with 1 -1 9 δ ( n ) 2 security.

Before describing the construction of OWPuzzs, let us introduce notations and a claim, which we will use for showing correcntess and security. Let t ( n ) := 16 ϵ ( n ) 2 · n . Let us denote Eval to mean a deterministic unbounded-time algorithm that takes 1 n , and { x i } i ∈ [ t ( n )] as input, and outputs an arbitrary z ∗ such that

$$\Pr \left [ \{ x _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow \mathcal { D } ( 1 ^ { n } , z ^ { * } ) ^ { \otimes t ( n ) } \right ] = \max _ { a \in \{ 0 , 1 \} ^ { n } } \left \{ \Pr \left [ \{ x _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow \mathcal { D } ( 1 ^ { n } , a ) ^ { \otimes t ( n ) } \right ] \right \} .$$

Claim 3.6. For all z ∈ { 0 , 1 } n , we have

$$\Pr \left [ \text {SD} ( \mathcal { D } ( 1 ^ { n } , z ) , \mathcal { D } ( 1 ^ { n } , z ^ { * } ) ) \leq \frac { 1 } { 2 \epsilon ( n ) } \, \colon \quad \underset { z ^ { * } \leftarrow E \text { eval} ( 1 ^ { n } , \{ x _ { i } \} _ { i \in [ t ( n ) ] } ) } { \{ x _ { i } \} _ { i \in [ t ( n ) ] } } \leftarrow \mathcal { D } ( 1 ^ { n } , z ) ^ { \otimes t ( n ) } \, \right ] \geq 1 - 2 ^ { - n + 1 } \quad ( 2 9 )$$

for all n ∈ N .

We defer the proof of Claim 3.6 to the end of the proof. Our construction of OWPuzzs ( Samp , Vrfy ) with 1 -1 9 δ ( n ) 2 security is as follows.

Samp (1 n ) :

$$1 . \, \text {Run} \, z \leftarrow \mathcal { S } ( 1 ^ { n } ) .$$

2. Run { x i } i ∈ [ t ( n )] ←D (1 n , z ) ⊗ t ( n ) .
3. Output puzz := { x i } i ∈ [ t ( n )] and ans := z .

Vrfy ( puzz , ans ) :

1. Parse puzz = { x i } i ∈ [ t ( n )] and ans = z .
2. Compute z ∗ ← Eval (1 n , { x i } i ∈ [ t ( n )] ) .
3. Output ⊤ if

Otherwise, output ⊥ .

Correctness. First, let us show the correctness. From the construction of Vrfy ( { x i } i ∈ [ t ( n )] , z ) , it runs z ∗ ← Eval (1 n , { x i } i ∈ [ t ( n )] ) , computes SD ( D (1 n , z ∗ ) , D (1 n , z )) , and outputs ⊤ if SD ( D (1 n , z ∗ ) , D (1 n , z )) ≤ 3 2 ϵ ( n ) , and outputs ⊥ otherwise. On the other hand, from Claim 3.6, we have

$$\Pr \left [ \text {SD} ( \mathcal { D } ( 1 ^ { n } , z ^ { * } ) , \mathcal { D } ( 1 ^ { n } , z ) ) \leq 1 / 2 \epsilon ( n ) \colon \quad & \{ x _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow \mathcal { D } ( 1 ^ { n } , z ) ^ { \otimes t ( n ) } \ \right ] \geq 1 - 2 ^ { - n + 1 } \quad ( 3 1 ) \\ & z ^ { * } \leftarrow \text {Eval} ( 1 ^ { n } , \{ x _ { i } \} _ { i \in [ t ( n ) ] } )$$

for all n ∈ N . This implies that we have

$$\Pr [ \top \leftarrow \text {Vrfy(puzz, ans) } \colon ( \text {puzz, ans} ) \leftarrow \text {Samp(1^{n})} ] \geq 1 - \text {neg} ( n ) .$$

Security. Next, let us show the security. For contradiction, let us assume that the OWPuzz is not secure. This means that there exists a QPT algorithm B such that

$$\Pr \left [ \top \leftarrow V r f ( p u z , \text {ans} ^ { * } ) \colon \quad \begin{smallmatrix} ( p u z , \text {ans} ) \leftarrow \text {Samp} ( 1 ^ { n } ) \\ \text {ans} ^ { * } \leftarrow \mathcal { B } ( 1 ^ { n } , \text {puzz} ) \end{smallmatrix} \right ] \geq 1 - \frac { 1 } { 9 \delta ^ { 2 } ( n ) }$$

for infinitely many n ∈ N . Note that from the standard average argument, this implies that with probability at least 1 -1 3 δ ( n ) over z ←S (1 n ) and { x i } i ∈ [ t ( n )] ←D (1 n , z ) ⊗ t ( n ) , we have

$$\Pr { \left [ \top \leftarrow \text {Vrf} ( \{ x _ { i } \} _ { i \in [ t ( n ) ] } , h ) \colon h \leftarrow \mathcal { B } ( 1 ^ { n } , \{ x _ { i } \} _ { i \in [ t ( n ) ] } ) \right ] } \geq 1 - \frac { 1 } { 3 \delta ( n ) }$$

for infinitely many n ∈ N .

From B , we construct a QPT algorithm A that contradicts to Equation (27). A receives 1 n and { x i } i ∈ [ t ( n )] , which is sampled by { x i } i ∈ [ t ( n )] ← D (1 n , z ) ⊗ t ( n ) , where z ← S (1 n ) , runs h ← B (1 n , { x i } i ∈ [ t ( n )] ) , and outputs h . In the following, we analyze the A .

From Claim 3.6, with probability at least 1 -2 -n +1 over { x i } i ∈ [ t ( n )] ←D (1 n , z ) ⊗ t ( n ) , we have

$$\text {SD} ( \mathcal { D } ( 1 ^ { n } , z ) , \mathcal { D } ( 1 ^ { n } , z ^ { * } ) ) \leq \frac { 1 } { 2 \epsilon ( n ) } ,$$

where z ∗ is the output of Eval (1 n , { x i } i ∈ [ t ( n )] ) . Let Good n,z,ϵ be a set of { x i } i ∈ [ t ( n )] that satisfies the following two conditions:

$$SD ( \mathcal { D } ( 1 ^ { n } , z ^ { * } ) , \mathcal { D } ( 1 ^ { n } , z ) ) \leq \frac { 3 } { 2 \epsilon ( n ) } .$$

1. The output z ∗ of Eval (1 n , { x i } i ∈ [ t ( n )] ) satisfies

$$\text {SD} ( \mathcal { D } ( 1 ^ { n } , z ) , \mathcal { D } ( 1 ^ { n } , z ^ { * } ) ) \leq \frac { 1 } { 2 \epsilon ( n ) } .$$

2.

$$\Pr \left [ \top \leftarrow \text {Vrf} ( \{ x _ { i } \} _ { i \in [ t ( n ) ] } , h ) \colon h \leftarrow \mathcal { B } ( 1 ^ { n } , \{ x _ { i } \} _ { i \in [ t ( n ) ] } ) \right ] \geq 1 - \frac { 1 } { 3 \delta ( n ) } .$$

From the union bound, Equations (34) and (35) imply that

$$\Pr \left [ \{ x _ { i } \} _ { i \in [ t ( n ) ] } \in \text {Good} _ { n , z , \epsilon } \colon \quad & \stackrel { z \leftarrow \mathcal { S } ( 1 ^ { n } ) } { \{ x _ { i } \} _ { i \in [ t ( n ) ] } } \leftarrow \mathcal { D } ( 1 ^ { n } , z ) ^ { \otimes t ( n ) } \ \right ] \geq 1 - \frac { 2 } { 3 \delta ( n ) } .$$

We will use the following Claim 3.7, which we defer the proof of Claim 3.7 to the end of the proof.

Claim 3.7. For all { x i } i ∈ [ t ( n )] ∈ Good n,z,ϵ , if we have

$$\top \leftarrow V r f ( \{ x _ { i } \} _ { i \in [ t ( n ) ] } , h ) ,$$

$$\text {SD} ( \mathcal { D } ( 1 ^ { n } , h ) , \mathcal { D } ( 1 ^ { n } , z ) ) \leq \frac { 1 } { \epsilon ( n ) } .$$

From Claim 3.7, for all { x i } i ∈ [ t ( n )] ∈ Good n,z,ϵ , we have

$$\Pr \left [ \text {SD} ( \mathcal { D } ( 1 ^ { n } , z ) , \mathcal { D } ( 1 ^ { n } , h ) ) \leq \frac { 1 } { \epsilon ( n ) } \, \colon \, h \leftarrow \mathcal { B } ( 1 ^ { n } , \{ x _ { i } \} _ { i \in [ t ( n ) ] } ) \, \right ]$$

$$\geq & \Pr \left [ \top \leftarrow V r \text {f} ( \{ x _ { i } \} _ { i \in [ t ( n ) ] } , h ) \colon \ h \leftarrow \mathcal { B } ( 1 ^ { n } , \{ x _ { i } \} _ { i \in [ t ( n ) ] } ) \ \right ] \geq 1 - \frac { 1 } { 3 \delta ( n ) } .$$

Here, in the final inequality, we have used the definition of Good n,z,ϵ .

Equations (38) and (41) imply that

$$\Pr \left [ \text {SD} ( \mathcal { D } ( 1 ^ { n } , z ) , \mathcal { D } ( 1 ^ { n } , h ) ) \leq \frac { 1 } { \epsilon ( n ) } \colon \quad \{ x _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow \mathcal { D } ( 1 ^ { n } , z ) ^ { \otimes t ( n ) } \, \right ] \geq 1 - \frac { 1 } { \delta ( n ) } \quad ( 4 3 )$$

for infinitely many n ∈ N . This completes the proof.

Finally, we prove Claims 3.6 and 3.7. For showing Claim 3.6, we will use the following Claims 3.8 and 3.9.

Claim 3.8. If

then we have

then h satisfies

$$\text {SD} ( \mathcal { D } ( 1 ^ { n } , z ) , \mathcal { D } ( 1 ^ { n } , z ^ { * } ) ) > \frac { 1 } { 2 \epsilon ( n ) } ,$$

$$\S D ( \mathcal { D } ( 1 ^ { n } , z ) ^ { \otimes t ( n ) } , \mathcal { D } ( 1 ^ { n } , z ^ { * } ) ^ { \otimes t ( n ) } ) > 1 - 2 ^ { - \frac { t ( n ) } { 8 \epsilon ( n ) ^ { 2 } } + 1 } .$$

Claim 3.9. If SD ( D (1 n , z ) , D (1 n , z ∗ )) &gt; α , then

$$\Pr [ \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , z ) ] > \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , z ^ { * } ) ] \colon x \leftarrow \mathcal { D } ( 1 ^ { n } , z ) ] > \alpha .$$

Claims 3.8 and 3.9 follows from standard probabilistic argument. For clarity, we describe the proof of Claims 3.8 and 3.9 in the end of the proof.

Proof of Claim 3.6. Define

$$\text {Bad} _ { n , z , \epsilon } \colon = \left \{ z ^ { * } \colon \text {SD} ( \mathcal { D } ( 1 ^ { n } , z ) , \mathcal { D } ( 1 ^ { n } , z ^ { * } ) ) > \frac { 1 } { 2 \epsilon ( n ) } \right \} .$$

From Claim 3.8, for any z ∗ ∈ Bad n,z,ϵ , we have

$$\S D ( \mathcal { D } ( 1 ^ { n } , z ) ^ { \otimes t ( n ) } , \mathcal { D } ( 1 ^ { n } , z ^ { * } ) ^ { \otimes t ( n ) } ) > 1 - 2 ^ { - \frac { t ( n ) } { 8 \epsilon ( n ) ^ { 2 } } + 1 } .$$

From Claim 3.9, for any z ∗ ∈ Bad n,z,ϵ , we have

$$\Pr \left [ \Pr \left [ \{ x _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow \mathcal { D } ( 1 ^ { n } , z ) ^ { \otimes t ( n ) } \right ] > \Pr \left [ \{ x _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow \mathcal { D } ( 1 ^ { n } , z ^ { * } ) ^ { \otimes t ( n ) } \right ] \colon \{ x _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow \mathcal { D } ( 1 ^ { n } , z ) ^ { \otimes t ( n ) } \right ]$$

$$> 1 - 2 ^ { - \frac { t ( n ) } { 8 c ( n ) ^ { 2 } } + 1 } .$$

This implies that, for any z ∗ ∈ Bad n,z,ϵ , we have

$$\Pr { \left [ z ^ { * } \leftarrow \text {Eval} ( 1 ^ { n } , \{ x _ { i } \} _ { i \in [ t ( n ) ] } ) \colon \{ x _ { i } \} _ { i \in [ t ( n ) ] } \rightarrow \mathcal { D } ( 1 ^ { n } , z ) ^ { \otimes t ( n ) } \right ] } \leq 2 ^ { - \frac { t ( n ) } { 8 ( t ( n ) ) ^ { 2 } } + 1 }$$

Therefore, we have

$$\sum _ { z ^ { * } \in \text {Bad} _ { n , z , \epsilon } } \Pr [ z ^ { * } \leftarrow \text {Eval} ( 1 ^ { n } , \{ x _ { i } \} _ { i \in [ t ( n ) ] } ) \colon \{ x _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow \mathcal { D } ( 1 ^ { n } , z ) ^ { \otimes t ( n ) } ] \leq \sum _ { h \in \text {Bad} _ { n , z , \epsilon } } 2 ^ { - \frac { t ( n ) } { 8 \epsilon ( n ) ^ { 2 } } + 1 } \ \ ( 5 2 )$$

$$& \leq | \text {Bad} _ { n , z , \epsilon } | ^ { 2 } \frac { - \frac { t ( n ) } { 8 ( n ) ^ { 2 } } + 1 } { 8 ( n ) ^ { 2 } } \leq 2 ^ { n - \frac { t ( n ) } { 8 ( n ) ^ { 2 } } + 1 } \leq 2 ^ { - n + 1 } .$$

Therefore, we have

$$\Pr \left [ \text {SD} ( \mathcal { D } ( 1 ^ { n } , z ^ { * } ) , \mathcal { D } ( 1 ^ { n } , z ) ) \leq \frac { 1 } { 2 \epsilon ( n ) } \colon \quad _ { z ^ { * } \leftarrow \text {Eval} ( 1 ^ { n } , \{ x _ { i } \} _ { i \in [ t ( n ) ] } ) } ^ { \{ x _ { i } \} _ { i \in [ t ( n ) ] } } \right ] \geq 1 - 2 ^ { - n + 1 } \quad ( 5 4 )$$

for all n ∈ N .

Proof of Claim 3.7. If { x i } i ∈ [ t ( n )] ∈ Good n,z,ϵ , then, by definition, Eval (1 n , { x i } i ∈ [ t ( n )] ) outputs z ∗ such that

$$\text {SD} ( \mathcal { D } ( 1 ^ { n } , z ^ { * } ) , \mathcal { D } ( 1 ^ { n } , z ) ) < \frac { 1 } { 2 \epsilon ( n ) }$$

with probability 1 , and from the definition of Vrfy , Vrfy ( { x i } i ∈ [ t ( n )] , h ) outputs ⊥ for all h such that

$$\text {SD} ( \mathcal { D } ( 1 ^ { n } , h ) , \mathcal { D } ( 1 ^ { n } , z ^ { * } ) ) \geq \frac { 3 } { 2 \epsilon ( n ) } ,$$

where z ∗ is the output of Eval (1 n , { x i } i ∈ [ t ( n )] ) . Fromthetriangle inequality, this implies that Vrfy ( { x i } i ∈ [ t ( n )] , h ) outputs ⊥ for all h such that

$$\text {SD} ( \mathcal { D } ( 1 ^ { n } , h ) , \mathcal { D } ( 1 ^ { n } , z ) ) \geq \text {SD} ( \mathcal { D } ( 1 ^ { n } , h ) , \mathcal { D } ( 1 ^ { n } , z ^ { * } ) ) - \text {SD} ( \mathcal { D } ( 1 ^ { n } , z ^ { * } ) , \mathcal { D } ( 1 ^ { n } , z ) ) > \frac { 1 } { \epsilon ( n ) } .$$

Therefore, for all { x i } i ∈ [ t ( n )] ∈ Good n,z,ϵ , if Vrfy ( { x i } i ∈ [ t ( n )] , h ) outputs ⊤ , then we have

$$\text {SD} ( \mathcal { D } ( 1 ^ { n } , h ) , \mathcal { D } ( 1 ^ { n } , z ) ) \leq \frac { 1 } { \epsilon ( n ) } .$$

$$I _ { n } \coloneqq \text {SD} ( \mathcal { D } ( 1 ^ { n } , z ) , \mathcal { D } ( 1 ^ { n } , z ^ { * } ) ) .$$

Let G n be a set of x ∈ { 0 , 1 } ∗ such that

$$\Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , z ) ] > \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , z ^ { * } ) ] .$$

Let f be a function such that

$$f ( x ) = \left \{ \begin{array} { c c } 1 & \text {if } \ x \in \mathcal { G } _ { n } \\ 0 & \text {if } \ x \notin \mathcal { G } _ { n } . \end{array}$$

From Hoeffding inequality, we have

$$\Pr \left [ \sum _ { i \in [ t ( n ) ] } \frac { f ( x _ { i } ) } { t ( n ) } \leq \Pr [ x \in \mathcal { G } _ { n } \colon x \leftarrow \mathcal { D } ( 1 ^ { n } , z ) ] - \frac { I _ { n } } { 2 } \colon \{ x _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow \mathcal { D } ( 1 ^ { n } , z ) ^ { \otimes t ( n ) } \right ] \leq 2 ^ { - \frac { t ( n ) \cdot I _ { n } ^ { 2 } } { 2 } } .$$

From Hoeffding inequality, we also have

$$From H oelanding he q u a l s a n t h e v e & \quad \text {so have} \\ 2 ^ { - \frac { t ( n ) \cdot i } { 2 } } \, \geq \, & \Pr \left [ \, \sum _ { i \in [ t ( n ) ] } \frac { f ( x _ { i } ) } { t ( n ) } \geq \Pr [ x \in \mathcal { G } _ { n } \colon x \leftarrow \mathcal { D } ( 1 ^ { n } , z ^ { * } ) ] + \frac { I _ { n } } { 2 } \, \colon \{ x _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow \mathcal { D } ( 1 ^ { n } , z ^ { * } ) ^ { \otimes t ( n ) } \right ] \\ & = \Pr \left [ \, \sum _ { i \in [ t ( n ) ] } \frac { f ( x _ { i } ) } { t ( n ) } \geq \Pr [ x \in \mathcal { G } _ { n } \colon x \leftarrow \mathcal { D } ( 1 ^ { n } , z ) ] - \frac { I _ { n } } { 2 } \, \colon \{ x _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow \mathcal { D } ( 1 ^ { n } , z ^ { * } ) ^ { \otimes t ( n ) } \right ] . \\ \intertext { This implies that } 2 ^ { - \frac { t ( n ) \cdot i } { 2 } } \, \geq \, & \Pr \left [ \, \sum _ { i \in [ t ( n ) ] } \frac { f ( x _ { i } ) } { t ( n ) } \geq \Pr [ x \in \mathcal { G } _ { n } \colon x \leftarrow \mathcal { D } ( 1 ^ { n } , z ) ] - \frac { I _ { n } } { 2 } \, \colon \{ x _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow \mathcal { D } ( 1 ^ { n } , z ^ { * } ) ^ { \otimes t ( n ) } \right ] . \\$$

This implies that

$$\Pr \left [ \sum _ { i \in [ t ( n ) ] } \frac { f ( x _ { i } ) } { t ( n ) } \leq \Pr [ x \in \mathcal { G } _ { n } \colon x \leftarrow \mathcal { D } ( 1 ^ { n } , z ) ] - \frac { I _ { n } } { 2 } \colon \{ x _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow \mathcal { D } ( 1 ^ { n } , z ^ { * } ) ^ { \otimes t ( n ) } \right ] \geq 1 - 2 ^ { - \frac { t ( n ) \cdot 1 ^ { 2 } } { 2 } } .$$

Proof of Claim 3.8. Let Equations (62) and (65) imply that

$$\text {SD} ( \mathcal { D } ( 1 ^ { n } , z ) ^ { \otimes t ( n ) } , \mathcal { D } ( 1 ^ { n } , z ^ { * } ) ^ { \otimes t ( n ) } ) \geq 1 - 2 \cdot 2 ^ { - \frac { t ( n ) \cdot I _ { n } ^ { 2 } } { 2 } } .$$

Because I n = SD ( D (1 n , z ) , D (1 n , z ∗ )) &gt; 1 2 ϵ ( n ) , we have

$$\S D ( \mathcal { D } ( 1 ^ { n } , z ) ^ { \otimes t ( n ) } , \mathcal { D } ( 1 ^ { n } , z ^ { * } ) ^ { \otimes t ( n ) } ) \geq 1 - 2 \cdot 2 ^ { - \frac { t ( n ) \cdot I _ { n } ^ { 2 } } { 2 } } > 1 - 2 \cdot 2 ^ { - \frac { t ( n ) } { 8 ( n ) ^ { 2 } } } .$$

Proof of Claim 3.9. We have

$$\Pr [ \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , z ) ] > \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , z ^ { * } ) ] \colon x \leftarrow \mathcal { D } ( 1 ^ { n } , z ) ]$$

$$Pr [ \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , z ) ] > \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , z ^ { * } ) ] \colon x \leftarrow \mathcal { D } ( 1 ^ { n } , z ) ] \\ = \sum _ { x \colon \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , z ) ] > \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , z ^ { * } ) ] } \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , z ) ] \\ = \sum _ { x \colon \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , z ) ] > \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , z ^ { * } ) ] } ( \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , z ) ] - \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , z ^ { * } ) ] ) \\ + \sum _ { x \colon \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , z ) ] > \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , z ^ { * } ) ] } \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , z ^ { * } ) ] \\ \geq \sum _ { x \colon \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , z ) ] > \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , z ^ { * } ) ] } ( \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , z ) ] - \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , z ^ { * } ) ] ) \\ = \mathbb { S } ( \mathcal { D } ( 1 ^ { n } , z ) , \mathcal { D } ( 1 ^ { n } , z ^ { * } ) ) > \alpha .$$

Proof of Lemma 3.5. Suppose that OWPuzzs exist. Then, from Theorem 2.18, there exists a non-uniform QPRG, Gen . From Gen , we construct S and D , which is hard to learn on average, as follows.

S (1 n ) :

1. Sample

2. Sample

3.

Output

D (1 n , z ) :

$$1 . \, & \, \text {Parse} \, z = ( \mu , b ) . \\ 2 . \, & \, \text {If} \, b = 0 , \, \text {then run} \, \xi \leftarrow \, \text {Gen} ( 1 ^ { n } , \mu ) , \, \text {and output} \, x \colon = ( \xi , \mu ) . \\ 3 . \, & \, \text {If} \, b = 1 , \, \text {then run} \, \xi \leftarrow \, \{ 0 , 1 \} ^ { n } , \, \text {and output} \, x \colon = ( \xi , \mu ) .$$

For contradiction, suppose that there exist a QPT algorithm A and a polynomial t such that

$$\Pr \left [ \text {SD} ( \mathcal { D } ( 1 ^ { n } , ( \mu , b ) ) , \mathcal { D } ( 1 ^ { n } , ( \mu ^ { * } , b ^ { * } ) ) ) \leq 1 / n \colon \quad \{ \xi _ { i } , \mu _ { i } \} _ { [ t ] } \leftarrow \mathcal { D } ( 1 ^ { n } , ( \mu , b ) ) ^ { \otimes t ( n ) } \right ] \geq 1 - \frac { 1 } { n ^ { 1 0 0 } } \\ \left ( \mu ^ { * } , b ^ { * } \right ) \leftarrow \mathcal { A } ( 1 ^ { n } , \{ \xi _ { i } \} _ { i \in [ t ( n ) ] } , \mu ) \right )$$

µ

b

z

←

[

n

←{

]

.

0

,

1

}

µ, b

)

.

.

:= (

for infinitely many n ∈ N .

From A , we construct a QPT algorithm B that breaks the security of Gen . More formally, we construct a QPT algorithm B such that, for all µ ∈ [ n ] with

$$S D ( \text {Gen} ( 1 ^ { n } , \mu ) , U _ { n } ) \geq 1 - \text {neg} ! ( n ) ,$$

$$\left | \Pr \left [ 1 \leftarrow \mathcal { B } ( 1 ^ { n } , \{ \xi _ { i } \} _ { i \in [ t ( n ) ] } ) \colon \{ \xi _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow \text {Gen} ( 1 ^ { n } , \mu ) ^ { \otimes t ( n ) } \right ]$$

$$t ( n ) \Big | \Big | \geq \frac { 1 } { \text {poly} ( n ) }$$

$$- \Pr \left [ 1 \leftarrow \mathcal { B } ( 1 ^ { n } , \{ \xi _ { i } \} _ { i \in [ t ( n ) ] } ) \colon \{ \xi _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow U _ { n } ^ { \otimes t ( n ) } \right ] \right | \geq \frac { 1 } { \text {poly} ( n ) }$$

for infinitely many n ∈ N . Here, U n is a uniform distribution over { 0 , 1 } n .

For describing the algorithm B , let us introduce the following Check algorithm.

Check (1 n , µ ) :

1. Receive 1 n and µ ∈ [ n ] as input.
2. Run { X i ( j ) } i ∈ [ t ( n )] ← U ⊗ t ( n ) n for all j ∈ [ n 25 ] .
3. Run ( µ ′ , b µ ( j )) ←A (1 n , { X i ( j ) } i ∈ [ t ( n )] , µ ) for all j ∈ [ n 25 ] .
4. If b µ ( j ) = 1 for all j ∈ [ n 25 ] , then output ⊤ . Otherwise, output ⊥ .

Now, we give the construction of B .

B (1 n , { ξ i } i ∈ [ t ( n )] ) :

1. Receive 1 n and { ξ i } i ∈ [ t ( n )] as input.
2. For all µ ∈ [ n ] , run fl ag µ ← Check (1 n , µ ) .
3. For all µ ∈ [ n ] , run ( µ ∗ , b µ ) ←A (1 n , { ξ i } i ∈ [ t ( n )] , µ ) .
4. Output 0 if b µ = 0 and fl ag µ = ⊤ for some µ ∈ [ n ] . Otherwise, output 1 .

We have the following Claims 3.10 and 3.11.

Claim 3.10. For all µ ∈ [ n ] such that

$$S D ( \text {Gen} ( 1 ^ { n } , \mu ) , U _ { n } ) \geq 1 - \text {neg} ! ( n ) ,$$

we have

we have

$$\Pr \left [ 0 \leftarrow \mathcal { B } ( 1 ^ { n } , \{ \xi _ { i } \} _ { i \in [ t ( n ) ] } ) \colon \{ \xi _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow \text {Gen} ( 1 ^ { n } , \mu ) ^ { \otimes t ( n ) } \right ] \geq 1 - \frac { 1 } { n }$$

for infinitely many n ∈ N .

Claim 3.11. We have

$$\Pr { \left [ 1 \leftarrow \mathcal { B } ( 1 ^ { n } , \{ \xi _ { i } \} _ { i \in [ t ( n ) ] } ) \colon \{ \xi _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow U _ { n } ^ { \otimes t ( n ) } \right ] \geq 1 - \frac { 1 } { n } }$$

for infinitely many n ∈ N .

We defer the proof of Claims 3.10 and 3.11. From Claims 3.10 and 3.11, for all µ ∈ [ n ] such that

$$S D ( \text {Gen} ( 1 ^ { n } , \mu ) , U _ { n } ) \geq 1 - \text {neg} ! ( n ) ,$$

$$\Pr \left [ 1 \leftarrow \mathcal { B } ( 1 ^ { n } , \{ \xi _ { i } \} _ { i \in [ t ( n ) ] } ) \colon \{ \xi _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow U _ { n } ^ { \otimes t ( n ) } \right ]$$

$$- \Pr \left [ 1 \leftarrow \mathcal { B } ( 1 ^ { n } , \{ \xi _ { i } \} _ { i \in [ t ( n ) ] } ) \colon \{ \xi _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow \text {Gen} ( 1 ^ { n } , \mu ) ^ { \otimes t ( n ) } \right ] \geq 1 - \frac { 2 } { n } \quad ( 8 3 )$$

for infinitely many n ∈ N . This contradicts the security of Gen .

Now, we prove Claims 3.10 and 3.11. For showing them, we will use the following Claims 3.12 and 3.13. Claim 3.12. For all sufficiently large n ∈ N , if µ ∈ [ n ] satisfies

$$\Pr { \left [ b ^ { * } = 1 \, \colon \quad \{ \xi _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow U _ { n } ^ { \otimes t ( n ) } } \\ ( \mu ^ { * } , b ^ { * } ) \leftarrow \mathcal { A } ( 1 ^ { n } , \{ \xi _ { i } \} _ { i \in [ t ( n ) ] } , \mu ) \, \right ] \leq 1 - \frac { 1 } { n ^ { 5 } } ,$$

$$\Pr [ \top \leftarrow \text {Check} ( 1 ^ { n } , \mu ) ] \leq \frac { 1 } { n ^ { 1 0 } } .$$

Claim 3.13. For all µ ∈ [ n ] such that

$$S D ( \text {Gen} ( 1 ^ { n } , \mu ) , U _ { n } ) \geq 1 - \text {neg} ! ( n ) ,$$

$$\Pr \left [ b ^ { \prime } = 0 \, \colon \quad \begin{smallmatrix} \{ \xi _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow \text {Gen} ( 1 ^ { n } , \mu ) ^ { \otimes t ( n ) } \\ ( \mu ^ { \prime } , b ^ { \prime } ) \leftarrow \mathcal { A } ( 1 ^ { n } , \{ \xi _ { i } \} _ { i \in [ t ( n ) ] } , \mu ) \end{smallmatrix} \right ] \geq 1 - \frac { 1 } { n ^ { 8 0 } }$$

$$\Pr \left [ b ^ { \prime } = 1 \colon \quad \{ \xi _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow U _ { n } ^ { \otimes t ( n ) } \\ ( \mu ^ { \prime } , b ^ { \prime } ) \leftarrow \mathcal { A } ( 1 ^ { n } , \{ \xi _ { i } \} _ { i \in [ t ( n ) ] } , \mu ) \ \right ] \geq 1 - \frac { 1 } { n ^ { 8 0 } }$$

for infinitely many n ∈ N .

We defer the proof of Claims 3.12 and 3.13 in the end of the proof.

we have

then

we have

and Proof of Claim 3.10. From the construction of B , we have

$$& \Pr [ 0 \leftarrow \mathcal { B } ( 1 ^ { n } , \{ \xi _ { i } \} i \in [ t ( n ) ] ) \colon \{ \xi _ { i } \} i \in [ t ( n ) ] \, \leftarrow \, \text {Gen} ( 1 ^ { n } , \mu ) \otimes ^ { t ( n ) } ] \\ & \quad = \Pr \left [ \left ( \text {flag} _ { \mu ^ { * } } = \top \wedge b _ { \mu ^ { * } } = 0 \right ) \text {for some } \mu ^ { * } \in [ n ] \, \colon \quad \text {flag} _ { \mu ^ { * } } \, \mu \leftarrow \, \text {Check} ( 1 ^ { n } , \mu ^ { * } ) \text { for all } \mu ^ { * } \in [ n ] \\ & \quad \left [ \mu ^ { \prime } , b _ { \mu ^ { * } } \right ) \leftarrow \, \mathcal { A } ( 1 ^ { n } , \{ \xi _ { i } \} i \in [ t ( n ) ] , \mu ^ { * } ) \text { for all } \mu ^ { * } \in [ n ] \right ] \\$$

$$& \geq \Pr \left [ \left ( \text {flag} _ { \mu } = \top \wedge b _ { \mu } = 0 \right ) \colon \quad \text {flag} _ { \mu } \leftarrow \text {Check} ( 1 ^ { n } , \mu ) \\ & \quad \left ( \mu ^ { \prime } , b _ { \mu } \right ) \rightarrow \mathcal { A } ( 1 ^ { n } , \{ \xi _ { i } \} _ { i \in [ t ( n ) ] } , \mu )$$

$$& = \Pr ^ { \left [ b _ { \mu } = 0 \, \colon \quad \{ \xi _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow \, \text {Gen} ( 1 ^ { n } , \mu ) ^ { \otimes t ( n ) } \right ] } \, \cdot \, \Pr ^ { \left ( \top \right ) \leftarrow \, \text {Check} ( 1 ^ { n } , \mu ) \right ] } \, \left | \cdot \Pr [ \top \leftarrow \, \text {Check} ( 1 ^ { n } , \mu ) \right ]$$

$$= \Pr ^ { \left [ } b _ { \mu } = 0 \colon \quad & \begin{smallmatrix} \{ \xi _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow \text {Gen} ( 1 ^ { n } , \mu ) ^ { \otimes t ( n ) } \\ ( \mu ^ { \prime } , b _ { \mu } ) \leftarrow \mathcal { A } ( 1 ^ { n } , \{ \xi _ { i } \} _ { i \in [ t ( n ) ] } , \mu ) \end{smallmatrix} \end{smallmatrix}$$

$$\cdot \left ( \Pr \left [ b _ { \mu } = 1 \colon \begin{array} { c c } \{ \xi _ { i } \} _ { i \in \{ t ( n ) \} } & \leftarrow U _ { n } ^ { \otimes t ( n ) } \\ ( \mu ^ { \prime } , b _ { \mu } ) \leftarrow \mathcal { A } ( 1 ^ { n } , \{ \xi _ { i } \} _ { i \in \{ t ( n ) \} } , \mu ) \end{array} \right ] \right ) ^ { n ^ { 2 ^ { 5 } } }$$

On the other hand, from Claim 3.13, for all µ such that

$$S D ( \text {Gen} ( 1 ^ { n } , \mu ) , U _ { n } ) \geq 1 - \text {neg} ! ( n ) ,$$

$$\Pr \left [ b ^ { \prime } = 0 \, \colon \quad \{ \xi _ { i } \} _ { i \in \{ t ( n ) \} } \leftarrow \text {Gen} ( 1 ^ { n } , \mu ) ^ { \otimes t ( n ) } \, \right ] \geq 1 - \frac { 1 } { n ^ { 8 0 } }$$

$$\Pr \left [ b ^ { \prime } = 1 \colon \quad \{ \xi _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow U _ { n } ^ { \otimes t ( n ) } \\ ( \mu ^ { \prime } , b ^ { \prime } ) \leftarrow \mathcal { A } ( 1 ^ { n } , \{ \xi _ { i } \} _ { i \in [ t ( n ) ] } , \mu ) \ \right ] \geq 1 - \frac { 1 } { n ^ { 8 0 } }$$

for infinitely many n ∈ N . Therefore, for all µ such that

$$S D ( \text {Gen} ( 1 ^ { n } , \mu ) , U _ { n } ) \geq 1 - \text {neg} ! ( n ) ,$$

(

1

n

80

n

)

26

1

n

we have

and

we have Pr

[

0

←B

(1

n

,

{

ξ

for infinitely many n ∈ N .

Proof of Claim 3.11. For any n ∈ N , let Bad n be a set of µ such that the following inequality holds

$$\Pr { \left [ b ^ { * } = 1 \, \colon \quad \{ \xi _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow U _ { n } ^ { \otimes t ( n ) } } \\ ( \mu ^ { * } , b ^ { * } ) \leftarrow \mathcal { A } ( 1 ^ { n } , \{ \xi _ { i } \} _ { i \in [ t ( n ) ] } , \mu ) \, \right ] \leq 1 - \frac { 1 } { n ^ { 5 } } .$$

i

}

i

∈

[

t

n

(

)]

) :

{

ξ

i

}

i

∈

[

t

n

(

)]

←

Gen

n

(1

, µ

⊗

)

t

n

(

)

]

≥

1

-

≥

1

-

(99)

From the construction of B , we have

$$From the construction of \mathcal { B } , we have \quad \\ \Pr [ 0 \leftarrow \mathcal { B } ( 1 ^ { n } , \{ \xi _ { i } \} _ { i \in [ t ( n ) ] } ) \colon \{ \xi _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow \mathcal { U } ^ { \otimes t ( n ) } ] \\ = \Pr \left [ \left ( \flag _ { \mu ^ { * } } = T \wedge \beta _ { * } = 0 \right ) \text { for some } \mu ^ { * } \in [ n ] \colon \quad \text {flag} _ { \mu ^ { * } } \leftarrow \text {Check} ( 1 ^ { n } , \mu ^ { * } ) \text { for all } \mu ^ { * } \in [ n ] \\ ( \mu ^ { \prime } , \beta _ { * } ) \right ] \\ = \Pr \left [ \left ( \flag _ { \mu ^ { * } } = T \wedge \beta _ { * } = 0 \right ) \text { for some } \mu ^ { * } \in [ n ] \quad \colon \quad \left \{ \xi _ { i } \} _ { i \in [ t ( n ) ] } \right \} \cdot \mathcal { U } ^ { \otimes t ( n ) } \\ \quad \cdot \Pr \left [ \left ( \flag _ { \mu ^ { * } } = T \text { for some } \mu ^ { * } \in \text {Bad} _ { n } \\ \mu ^ { \prime } , \beta _ { * } \right ) \right \} \\ \quad \cdot \text {Pr} \left [ \left ( \flag _ { \mu ^ { * } } = T \wedge \beta _ { * } = 0 \right ) \text { for some } \mu ^ { * } \in [ n ] \right \} \colon \quad \left \{ \xi _ { i } \} _ { i \in [ t ( n ) ] } \right \} \cdot \text {U} _ { n } \\ \quad \cdot \text {Pr} \left [ \left ( \flag _ { \mu ^ { * } } = \perp \text { for all } \mu ^ { * } \in \text {Bad} _ { n } \right ) \quad \colon \quad \flag _ { \mu ^ { * } } \cdot \text {Check} ( 1 ^ { n } , \mu ^ { * } ) \text { for all } \mu ^ { * } \in [ n ] \\ \quad \cdot \text {In the following, we give the upper bound of Equations (103) and (104). We have } \\ \quad \text {Equation (103)}$$

In the following, we give the upper bound of Equations (103) and (104). We have

Equation (103)

$$( 1 0 5 )$$

$$& \quad \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \$$

$$\leq \sum _ { \mu ^ { * } \in \text {Bad} _ { n } } \Pr \left [ \ f { \mathbf \flag _ { \mu ^ { * } } = \top } \ \colon \ \ f { \mathbf \flag _ { \mu ^ { * } } \leftarrow \text {Check} ( 1 ^ { n } , \mu ^ { * } ) \ \right ] } \ \right ]$$

$$\leq | \text {Bad} _ { n } | \cdot \frac { 1 } { n ^ { 1 0 } } \leq \frac { 1 } { n ^ { 9 } } \leq \frac { 1 } { 2 n }$$

for all sufficiently large n ∈ N . Here, in the second inequality, we have used the union bound, and in the third inequality, we have used Claim 3.12 and the definition of Bad n .

We also have

Equation (104)

$$( 1 0 9 )$$

$$& \quad \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \$$

$$( 1 1 0 )$$

$$\leq & \Pr [ b _ { \mu ^ { * } } = 0 \text { for some } \mu ^ { * } \notin \text { Bad } _ { n } \colon \quad \{ \xi _ { i } \} _ { i \in [ t ( n ) ] } \hookrightarrow U _ { n } ^ { \otimes t ( n ) } \\ \leq & \Pr [ b _ { \mu ^ { * } } = 0 \text { for some } \mu ^ { * } \notin \mathcal { A } ( 1 ^ { n } , \{ \xi _ { i } \} _ { i \in [ t ( n ) ] } , \mu ^ { * } ) \text { for all } \mu ^ { * } \in [ n ] \ ]$$

$$\leq ( n - | \text {Bad} _ { n } | ) \cdot \frac { 1 } { n ^ { 5 } } \leq \frac { 1 } { n ^ { 4 } } \leq \frac { 1 } { 2 n }$$

for all sufficiently large n ∈ N . Here, in the third inequality, we have used that, for all µ ∗ / ∈ Bad n , we have

$$\Pr \left [ b ^ { * } = 0 \, \colon \quad \begin{array} { c } \{ \xi _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow U _ { n } ^ { \otimes t ( n ) } \\ ( \mu ^ { \prime } , b ^ { * } ) \leftarrow \mathcal { A } ( 1 ^ { n } , \{ \xi _ { i } \} _ { i \in [ t ( n ) ] } , \mu ^ { * } ) \end{array} \right ] \leq \frac { 1 } { n ^ { 5 } } .$$

Therefore, we have

we have

and

$$& \Pr \left [ \text {SD} ( \mathcal { D } ( 1 ^ { n } , ( \mu ^ { \prime } , b ) ) , \mathcal { D } ( 1 ^ { n } , ( \mu , 1 ) ) ) \leq 1 / n \colon \quad & \{ \xi _ { i } \} _ { i } \{ t ( n ) ] \leftarrow \mathcal { D } ( 1 ^ { n } , ( \mu , 1 ) ) ^ { \otimes t ( n ) } \right ) \\ & = \Pr \left [ b = 1 \colon \quad & \{ \xi _ { i } \} _ { i } [ t ( n ) ] \leftarrow \mathcal { U } _ { n } ^ { \otimes t ( n ) } \\ & \quad ( \mu ^ { \prime } , b ) \leftarrow \mathcal { A } ( 1 ^ { n } , \{ \xi _ { i } \} _ { i } \{ t ( n ) ] , \mu ) \right ] .$$

̸

Here, in the Equation (120), we have used the fact that D (1 n , ( µ, 0)) is far from D (1 n , ( µ ∗ , b ∗ )) for all µ ∗ = µ and b ∗ = 0 , and in the Equation (122), we have used the fact that D (1 n , ( µ, 1))) is far from D (1 n , ( µ ∗ , b ∗ )) for all µ ∗ = µ and b ∗ = 1 .

̸

̸

In the following, we show that for all ( µ, b ) ∈ [ n ] ×{ 0 , 1 } , we have

$$\Pr \left [ \text {SD} ( \mathcal { D } ( 1 ^ { n } , ( \mu , b ) ) , \mathcal { D } ( 1 ^ { n } , ( \mu ^ { \prime } , b ^ { \prime } ) ) ) \leq 1 / n \colon \quad \{ \xi _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow \mathcal { D } ( 1 ^ { n } , ( \mu , b ) ) ^ { \otimes t ( n ) } \ \right ] \geq 1 - \frac { 1 } { n ^ { 8 0 } } \ \ ( 1 2 3 )$$

̸

$$\Pr \left [ 0 \leftarrow \mathcal { B } ( 1 ^ { n } , \{ \xi _ { i } \} _ { i \in [ t ( n ) ] } ) \colon \{ \xi _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow U _ { n } ^ { \otimes t ( n ) } \right ] \leq \frac { 1 } { n }$$

for all sufficiently large n ∈ N .

Proof of Claim 3.12. From the construction of Check , we have

$$\Pr [ \top \leftarrow \text {Check} ( 1 ^ { n } , \mu ) ] = \left ( \Pr \left [ b ^ { * } = 1 \colon \quad \{ \xi _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow U _ { n } ^ { \otimes t ( n ) } \right ] \, \right ) \right ) ^ { n ^ { 2 5 } } . \quad ( 1 1 5 )$$

Therefore, if we have

then we have

$$\Pr { \left [ b ^ { * } = 1 \, \colon \quad \{ \xi _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow U _ { n } ^ { \otimes t ( n ) } } \\ \quad ( \mu ^ { * } , b ^ { * } ) \leftarrow \mathcal { A } ( 1 ^ { n } , \{ \xi _ { i } \} _ { i \in [ t ( n ) ] } , \mu ) \, \right ] \leq 1 - \frac { 1 } { n ^ { 5 } } ,$$

$$\Pr [ \top \leftarrow \text {Check} ( 1 ^ { n } , \mu ) ] \leq \left ( 1 - \frac { 1 } { n ^ { 5 } } \right ) ^ { n ^ { 2 5 } } \leq \frac { 1 } { n ^ { 1 0 } }$$

for all sufficiently large n ∈ N .

Proof of Claim 3.13. For all µ ∈ [ n ] such that

$$S D ( \text {Gen} ( 1 ^ { n } , \mu ) , U _ { n } ) \geq 1 - \text {neg} ! ( n ) ,$$

$$& \Pr \left [ \text {SD} ( \mathcal { D } ( 1 ^ { n } , ( \mu ^ { \prime } , b ) ) , \mathcal { D } ( 1 ^ { n } , ( \mu , 0 ) ) ) \leq 1 / n \colon \quad & \{ \xi _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow \mathcal { D } ( 1 ^ { n } , ( \mu , 0 ) ) ^ { \otimes t ( n ) } \right ] \\ & = \Pr \left [ b = 0 \colon \quad & \{ \xi _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow \text {Gen} ( 1 ^ { n } , \mu ) ^ { \otimes t ( n ) } \right ] \\$$

for infinitely many n ∈ N . By combining it with the above argument, we obatin the claim.

To show it, let Good n be a set of ( µ, b ) such that

$$\Pr \left [ \text {SD} ( \mathcal { D } ( 1 ^ { n } , ( \mu , b ) ) , \mathcal { D } ( 1 ^ { n } , ( \mu ^ { \prime } , b ^ { \prime } ) ) ) \leq 1 / n \colon \quad \{ \xi _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow \mathcal { D } ( 1 ^ { n } , ( \mu , b ) ) ^ { \otimes t ( n ) } \ \right ] \geq 1 - \frac { 1 } { n ^ { 8 0 } } . \ ( 1 2 4 )$$

We will show that | Good | = 2 n .

From Equation (74), we have

$$1 - \frac { 1 } { n ^ { 1 0 0 } } \leq \Pr \left [ \text {SD} ( \mathcal { D } ( 1 ^ { n } , ( \mu , b ) ) , \mathcal { D } ( 1 ^ { n } , h ) ) \leq 1 / n \colon \quad \{ \xi _ { i } , \mu \} _ { i \in [ t ( n ) ] } \leftarrow \mathcal { D } ( 1 ^ { n } , ( \mu , b ) ) ^ { \otimes t ( n ) } \right ] \\ h \leftarrow \mathcal { A } ( 1 ^ { n } , \{ \xi _ { i } \} _ { i \in [ t ( n ) ] } , \mu )$$

$$1 - \frac { 1 } { n ^ { 1 0 0 } } & \leq \Pr \left [ \text {SD} ( \mathcal { D } ( 1 ^ { n } , ( \mu , b ) ) , \mathcal { D } ( 1 ^ { n } , h ) ) \leq 1 / n \colon \quad \{ \xi _ { i } , \mu _ { i } \} [ t ( n ) ] \leftarrow \mathcal { D } ( 1 ^ { n } , ( \mu , b ) ) ^ { \otimes t ( n ) } \right ] \\ & = \sum _ { ( \mu , b ) \in \text {Good} _ { n } } \frac { 1 } { 2 n } \Pr \left [ \text {SD} ( \mathcal { D } ( 1 ^ { n } , ( \mu , b ) ) , \mathcal { D } ( 1 ^ { n } , ( \mu ^ { \prime } , b ^ { \prime } ) ) ) \leq 1 / n \colon \quad \{ \xi _ { i } \} [ t ( n ) ] \leftarrow \mathcal { D } ( 1 ^ { n } , ( \mu , b ) ) ^ { \otimes t ( n ) } \right ] \\ & + \sum _ { ( \mu , b ) \not = \text {Good} _ { n } } \frac { 1 } { 2 n } \Pr \left [ \text {SD} ( \mathcal { D } ( 1 ^ { n } , ( \mu , b ) ) , \mathcal { D } ( 1 ^ { n } , ( \mu ^ { \prime } , b ^ { \prime } ) ) ) \leq 1 / n \colon \quad \{ \xi _ { i } \} [ t ( n ) ] \leftarrow \mathcal { D } ( 1 ^ { n } , ( \mu , b ) ) ^ { \otimes t ( n ) } \right ] \\ & \leq \sum _ { ( 1 0 0 ) } \frac { 1 } { 2 n } + \sum _ { n } \frac { 1 } { 2 n } \left ( 1 - \frac { 1 } { 2 n } \right ) ^ { ( 1 2 0 ) }$$

$$\leq \sum _ { ( \mu , b ) \in \text {Good} _ { n } } \frac { 1 } { 2 n } + \sum _ { ( \mu , b ) \notin \text {Good} _ { n } } \frac { 1 } { 2 n } \left ( 1 - \frac { 1 } { n ^ { 8 0 } } \right )$$

$$= | \text {Good} _ { n } | \frac { 1 } { 2 n } + ( 2 n - | \text {Good} _ { n } | ) \, \frac { 1 } { 2 n } \left ( 1 - \frac { 1 } { n ^ { 8 0 } } \right ) = 1 - \frac { 1 } { n ^ { 8 0 } } + \frac { | \text {Good} _ { n } | } { 2 n ^ { 8 1 } }$$

for infinitely many n ∈ N .

This implies that

$$2 n - \frac { 2 } { n ^ { 1 9 } } \leq | \text {Good} _ { n } |$$

for infinitely many n ∈ N . Because | Good n | is an integer, this means that | Good n | = 2 n for infinitely many n ∈ N .

## 3.2 Classical Case

In this subsection, we apply the previous quantum results to the classical case.

Definition 3.14 (Average-Case Hardness of Proper Classical Distribution Learning [KMR + 94, HN23]). We say that average-case hardness of proper classical distribution learning holds if the following holds. There exist some polynomials ϵ and δ , a PPT algorithm S , which takes 1 n as input, and outputs z ∈ { 0 , 1 } n , and a PPT algorithm D , which takes 1 n and z ∈ { 0 , 1 } n as input, and outputs x ∈ { 0 , 1 } poly( n ) , such that, for all PPT algorithms A and any polynomial t ,

$$\Pr \left [ \text {SD} ( \mathcal { D } ( 1 ^ { n } , z ) , \mathcal { D } ( 1 ^ { n } , h ) ) \leq 1 / \epsilon ( n ) \, \colon \quad & \{ x _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow \mathcal { D } ( 1 ^ { n } , z ) ^ { \otimes t ( n ) } \, \right ] \leq 1 - 1 / \delta ( n ) \quad ( 1 3 1 ) \\ & \quad h \leftarrow \mathcal { A } ( 1 ^ { n } , \{ x _ { i } \} _ { i \in [ t ( n ) ] } )$$

for all sufficiently large n ∈ N .

## Definition 3.15 (Average-Case Hardness of Improper Classical Distribution Learning [KMR + 94, HN23]).

We say that average-case hardness of improper classical distribution learning holds if the following holds. There exist some polynomials ϵ and δ , a PPT algorithm S , which takes 1 n as input, and outputs z ∈ { 0 , 1 } n , and a PPT algorithm D , which takes 1 n and z ∈ { 0 , 1 } n as input, and outputs x ∈ { 0 , 1 } poly( n ) , such that, for all PPT algorithms A and any polynomial t ,

$$\Pr \left [ \text {SD} ( \mathcal { D } ( 1 ^ { n } , z ) , h ) \leq 1 / \epsilon ( n ) \colon \quad & \{ x _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow \mathcal { D } ( 1 ^ { n } , z ) ^ { \otimes t ( n ) } \ \right ] \leq 1 - 1 / \delta ( n ) \quad ( 1 3 2 ) \\ & h \leftarrow \mathcal { A } ( 1 ^ { n } , \{ x _ { i } \} _ { i \in [ t ( n ) ] } )$$

for all sufficiently large n ∈ N . Here, h is a description of a PPT algorithm.

Theorem 3.16. The following four conditions are equivalent:

1. OWFs exist.
2. Classical OWPuzzs exist.
3. Average-case hardness of proper classical distribution learning holds.
4. Average-case hardness of improper classical distribution learning holds.

Because its proof is similar to that of Theorem 3.3, we give only a sketch.

Proof sketch of Theorem 3.16. [HN23] shows the equivalence between (1) and (4) . (3) ⇐ (4) directly follows. (2) ⇐ (3) follows in the same way as Lemma 3.4. The difference is that we consider classical OWPuzzs instead of OWPuzzs. (1) ⇐ (2) follows from Theorem 2.14.

## 4 Agnostic Distribution Learning with Respect to KL Divergence

## 4.1 Quantum Case

In this section, we introduce hardness of agnostic quantum distribution learning with respect to KL divergence based on [AW92]. Then, we show that BQP = PP holds if and only if hardness of agnostic quantum distribution learning with respect to KL divergence holds.

̸

Definition 4.1 (Hardness of Agnostic Quantum Distribution Learning with Respect to KL Divergence). We say that hardness of agnostic quantum distribution learning with respect to KL divergence holds if the following holds: There exist some polynomials ϵ , δ and p , and a QPT algorithm D , which takes 1 n and z ∈ { 0 , 1 } n as input, and outputs x ∈ { 0 , 1 } p ( n ) such that the following two conditions are satisfied:

1. For all n ∈ N , z ∈ { 0 , 1 } n , and x ∈ { 0 , 1 } p ( n ) , we have

$$\Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , z ) ] \neq 0 .$$

̸

2. For any QPT algorithm A and any polynomial t , there exists an algorithm T , which takes 1 n as input and outputs x ∈ { 0 , 1 } p ( n ) such that

$$\Pr \left [ D _ { K L } ( \mathcal { T } ( 1 ^ { n } ) \left \| \mathcal { D } ( 1 ^ { n } , h ) \right ) \leq \text {Opt} _ { n } + 1 / \epsilon ( n ) \colon \begin{array} { c } \{ x _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow \mathcal { T } ( 1 ^ { n } ) ^ { \otimes t ( n ) } \\ h \leftarrow \mathcal { A } ( 1 ^ { n } , \{ x _ { i } \} _ { i \in [ t ( n ) ] } ) \end{array} \right ] \leq 1 - 1 / \delta ( n )$$

for infinitely many n ∈ N . Here, Opt n := min a ∈{ 0 , 1 } n { D KL ( T (1 n ) ‖ D (1 n , a )) } .

Definition 4.2 (Worst-Case Hardness of Quantum Maximum Likelihood Estimation). We say that worst-case hardness of quantum maximum likelihood estimation holds if the following holds. There exist some polynomials ϵ , δ and p , and a QPT algorithm D , which takes 1 n and z ∈ { 0 , 1 } n as input, and outputs x ∈ { 0 , 1 } p ( n ) such that, for any QPT algorithm A , there exists x ∈ { 0 , 1 } p ( n ) with max a ∈{ 0 , 1 } n Pr[ x ←D (1 n , a )] &gt; 0 such that

$$\Pr \left [ \frac { \max _ { a \in \{ 0 , 1 \} ^ { n } } \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , a ) ] } { \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , h ) ] } \leq 2 ^ { 1 / \epsilon ( n ) } \colon h \leftarrow \mathcal { A } ( 1 ^ { n } , x ) \right ] \leq 1 - 1 / \delta ( n )$$

for infinitely many n ∈ N .

̸

Remark 4.3. In the above definitions, we require that Equations (134) and (135) hold for infinitely many security parameters instead of for all sufficiently large security parameters . This is because we want to show its equivalence to PP = BQP instead of PP = ioBQP . If we use the 'for all sufficiently large security parameters' security, we obtain the equivalence to PP = ioBQP in a similar proof.

̸

Theorem 4.4. The following three conditions are equivalent:

̸

1. PP = BQP .
2. Hardness of agnostic quantum distribution learning with respect to KL divergence holds.
3. Worst-case hardness of quantum maximum likelihood estimation holds.

Theorem 4.4 follows from the following Lemmata 4.5 to 4.8.

̸

Lemma 4.5. If PP = BQP , then worst-case hardness of quantum maximum likelihood estimation holds.

Lemma 4.6. If PP = BQP , then worst-case hardness of quantum maximum likelihood estimation does not hold.

Lemma 4.6 follows from Lemma 4.2 in [HH24]. Therefore, we omit the proof and refer it to [HH24].

Lemma 4.7. If worst-case hardness of quantum maximum likelihood estimation holds, then hardness of agnostic quantum distribution learning with respect to KL divergence holds.

Lemma 4.8. If hardness of agnostic quantum distribution learning with respect to KL divergence holds, then worst-case hardness of quantum maximum likelihood estimation holds.

In the following, we give the proofs.

Proof of Lemma 4.5. For contradiction, assume that for any polynomial ϵ , δ and p , and any QPT algorithm D , which takes 1 n and z ∈ { 0 , 1 } n as input, and outputs x ∈ { 0 , 1 } p ( n ) , there exists a QPT algorithm A such that for all x ∈ { 0 , 1 } p ( n ) with max a ∈{ 0 , 1 } n Pr[ x ←D (1 n , a )] &gt; 0 , we have

$$\Pr \left [ \frac { \max _ { a \in \{ 0 , 1 \} ^ { n } } \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , a ) ] } { \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , h ) ] } \leq 2 ^ { 1 / \epsilon ( n ) } \colon h \leftarrow \mathcal { A } ( 1 ^ { n } , x ) \right ] \geq 1 - 1 / \delta ( n )$$

for all sufficiently large n ∈ N . Then, we show that, for any L ∈ PP , we have L ∈ BQP .

Because PP = PostBQP , for any L ∈ PP , there exist a polynomial q and a QPT algorithm B , which takes x as input, and outputs ( b, b ∗ ) ∈ { 0 , 1 } × { 0 , 1 } such that the following three conditions are satisfied:

̸

1. For all x ∈ { 0 , 1 } ∗ , Pr[ b ∗ = 1 : ( b, b ∗ ) ←B ( x )] ≥ 2 -q ( | x | ) .
2. For all x ∈ L
3. , we have
3. For all x / ∈ L , we have

$$\Pr _ { ( b , b ^ { * } ) \leftarrow \mathcal { B } ( x ) } [ b = 1 | b ^ { * } = 1 ] \geq \frac { 3 } { 4 } .$$

$$\Pr _ { ( b , b ^ { * } ) \leftarrow \mathcal { B } ( x ) } [ b = 1 | b ^ { * } = 1 ] \leq \frac { 1 } { 4 } .$$

From the QPT algorithm B , we construct the following QPT algorithm B ∗ .

B ∗ (1 n +1 , x, c ) :

1. Take 1 n +1 , x ∈ { 0 , 1 } n , and c ∈ { 0 , 1 } as input.
2. Run ( b, b ∗ ) ←B ( x ) .
3. Output ( x, 1) if b = c and b ∗ = 1 . Otherwise, output ⊥ .

From the construction of B ∗ , we have

$$\Pr \left [ ( x , 1 ) \leftarrow \mathcal { B } ^ { * } ( 1 ^ { | x | + 1 } , x , c ) \right ] = \Pr _ { ( b , b ^ { * } ) \leftarrow \mathcal { B } ( x ) } [ b = c \wedge b ^ { * } = 1 ]$$

for all x ∈ { 0 , 1 } ∗ and c ∈ { 0 , 1 } . Therefore, the following two conditions are satisfied:

1. For all x ∈ L , we have

$$\frac { \Pr \left [ ( x , 1 ) \leftarrow \mathcal { B } ^ { * ( | x | + 1 , x , 1 ) } \right ] } { \Pr \left [ ( x , 1 ) \leftarrow \mathcal { B } ^ { * ( | x | + 1 , x , 0 ) } \right ] } & = \frac { \Pr _ { ( b , b ^ { * } ) \leftarrow B ( x ) } [ b = 1 \wedge b ^ { * } = 1 ] } { \Pr _ { ( b , b ^ { * } ) \leftarrow B ( x ) } [ b = 0 \wedge b ^ { * } = 1 ] } \\ & = \frac { \Pr _ { ( b , b ^ { * } ) \leftarrow B ( x ) } [ b = 1 | b ^ { * } = 1 ] } { \Pr _ { ( b , b ^ { * } ) \leftarrow B ( x ) } [ b = 0 | b ^ { * } = 1 ] } \geq 3 .$$

2. For all x / ∈ L , we have

$$\frac { \Pr \left [ ( x , 1 ) \leftarrow \mathcal { B } ^ { * } ( 1 ^ { | x | + 1 } , x , 1 ) \right ] } { \Pr [ ( x , 1 ) \leftarrow \mathcal { B } ^ { * } ( 1 ^ { | x | + 1 } , x , 0 ) ] } & = \frac { \Pr _ { ( b , b ^ { * } ) \leftarrow \mathcal { B } ( x ) } [ b = 1 \wedge b ^ { * } = 1 ] } { \Pr _ { ( b , b ^ { * } ) \leftarrow \mathcal { B } ( x ) } [ b = 0 \wedge b ^ { * } = 1 ] }$$

$$= \frac { \Pr _ { ( b , b ^ { * } ) \leftarrow \mathcal { B } ( x ) } [ b = 1 | b ^ { * } = 1 ] } { \Pr _ { ( b , b ^ { * } ) \leftarrow \mathcal { B } ( x ) } [ b = 0 | b ^ { * } = 1 ] } \leq \frac { 1 } { 3 } .$$

On the other hand, we assume that worst-case hardness of quantum maximum likelihood estimation does not hold. This means that for any polynomial ϵ , δ and p , and any QPT algorithm D , which takes 1 n and z ∈ { 0 , 1 } n as input, and outputs x ∈ { 0 , 1 } p ( n ) , there exists a QPT algorithm A such that for all x ∈ { 0 , 1 } p ( n ) with max a ∈{ 0 , 1 } n Pr[ x ←D (1 n , a )] &gt; 0 , we have

$$\Pr \left [ \frac { \max _ { a \in \{ 0 , 1 \} ^ { n } } \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , a ) ] } { \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , h ) ] } \leq 2 ^ { 1 / \epsilon ( n ) } \colon h \leftarrow \mathcal { A } ( 1 ^ { n } , x ) \right ] \geq 1 - 1 / \delta ( n )$$

for all sufficiently large n ∈ N . Therefore, there exists a QPT algorithm A such that, for all x ∈ { 0 , 1 } n with max b ∈{ 0 , 1 } Pr [ ( x, 1) ←B ∗ (1 n +1 , ( x, b )) ] &gt; 0 ,

$$\Pr \left [ \frac { \max _ { b \in \{ 0 , 1 \} } \Pr [ ( x , 1 ) \leftarrow \mathcal { B } ^ { * } ( 1 ^ { n + 1 } , ( x , b ) ) ] } { \Pr [ ( x , 1 ) \leftarrow \mathcal { B } ^ { * } ( 1 ^ { n + 1 } , ( x , b ^ { * } ) ) ] } \leq 2 \colon ( x , b ^ { * } ) \leftarrow \mathcal { A } ( 1 ^ { n + 1 } , ( x , 1 ) ) \right ] \geq \frac { 5 } { 6 } \quad ( 1 4 5 )$$

for all sufficiently large n ∈ N .

This implies that A satisfies the following:

1. For all x ∈ L , we have

$$\Pr \left [ ( x , 1 ) \leftarrow \mathcal { A } ( 1 ^ { | x | } , x ) \right ] \geq \frac { 5 } { 6 } .$$

$$\Pr \left [ ( x , 1 ) \leftarrow \mathcal { A } ( 1 ^ { | x | } , x ) \right ] \leq \frac { 1 } { 6 } .$$

2. For all x / ∈ L , we have

This implies that L ∈ BQP .

Proof of Lemma 4.7. Let ϵ , δ , and p be some polynomials, and let D be a QPT algorithm given in Definition 4.2. From D , we construct a QPT algorithm D ∗ such that the following two conditions are satisfied:

1. For all n ∈ N , z ∈ { 0 , 1 } n and x ∈ { 0 , 1 } p ( n ) , we have

$$\Pr [ x \leftarrow \mathcal { D } ^ { * } ( 1 ^ { n } , z ) ] \neq 0 .$$

̸

2. For any QPT algorithm A and any polynomial t , there exists an algorithm T , which takes 1 n as input and outputs x ∈ { 0 , 1 } p ( n ) such that

$$\Pr \left [ D _ { K L } ( \mathcal { T } ( 1 ^ { n } ) \, \| \, \mathcal { D } ^ { * } ( 1 ^ { n } , h ) ) \leq \text {Opt} _ { n } + 1 / 2 \epsilon ( n ) \, \colon \quad & \stackrel { \{ x _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow \mathcal { T } ( 1 ^ { n } ) ^ { \otimes t ( n ) } } { h \leftarrow \mathcal { A } ( 1 ^ { n } , \{ x _ { i } \} _ { i \in [ t ( n ) ] } ) } \, \right ] \leq 1 - 1 / \delta ( n )$$

for infinitely many n ∈ N . Here, Opt n := min a ∈{ 0 , 1 } n { D KL ( T (1 n )) ‖ D ∗ (1 n , a ) } .

̸

Let us define C n as follows:

D (1 , z

Let m be a polynomial such that m ( n ) ≥ p ( n ) and for all z ∈ { 0 , 1 } n and for all x ∈ { 0 , 1 } p ( n ) with Pr[ x ←D (1 n , z )] = 0 , it holds that

$$\Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , z ) ] \geq 2 ^ { - m ( n ) } .$$

$$C _ { n } \coloneqq ( 2 ^ { - 1 / 2 \epsilon ( n ) } - 2 ^ { - 1 / \epsilon ( n ) } ) \cdot 2 ^ { - ( m ( n ) + 1 - p ( n ) ) } .$$

Now, from D , we give the construct of D ∗ as follows. ∗ n ) :

1. Run x ←D (1 n , z ) . Sample x ∗ ←{ 0 , 1 } p ( n ) .
2. Output x with probability 1 -C n , and output x ∗ with probability C n .

It is clear that D ∗ satisfies Equation (148). Next, for contradiction, let us assume that there exists a polynomial t and a QPT algorithm A such that for all algorithms T , which takes 1 n as input, and outputs x ∈ { 0 , 1 } p ( n ) , we have

$$\Pr \left [ D _ { K L } ( \mathcal { T } ( 1 ^ { n } ) \, \| \, \mathcal { D } ^ { * } ( 1 ^ { n } , h ) ) \leq \mathop O p _ { n } + 1 / 2 \epsilon ( n ) \, \colon \quad \stackrel { \{ x _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow \mathcal { T } ( 1 ^ { n } ) ^ { \otimes t ( n ) } } { h \leftarrow \mathcal { A } ( 1 ^ { n } , \{ x _ { i } \} _ { i \in [ t ( n ) ] } ) } \, \right ] \geq 1 - 1 / \delta ( n ) \, \left ( 1 5 2 \right )$$

for all sufficiently large n ∈ N . Here, Opt n := min a ∈{ 0 , 1 } n { D KL ( T (1 n )) ‖ D ∗ (1 n , a ) } . Then, we show that A satisfies

$$\Pr \left [ \frac { \max _ { a \in \{ 0 , 1 \} ^ { n } } \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , a ) ] } { \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , h ) ] } \leq 2 ^ { 1 / \epsilon ( n ) } \colon h \leftarrow \mathcal { A } ( 1 ^ { n } , x ) \right ] \geq 1 - 1 / \delta ( n )$$

for all x with max a ∈{ 0 , 1 } n Pr[ x ←D (1 n , a )] &gt; 0 and for all sufficiently large n ∈ N , which is a contradiction. For an arbitrary x ∈ { 0 , 1 } ∗ , we write T x to mean an algorithm that outputs x . Equation (152) implies that for all x ∈ { 0 , 1 } p ( n ) , with probability at least 1 -1 /δ ( n ) over h ←A (1 n , x ) , h satisfies

$$\frac { 1 } { 2 \epsilon ( n ) } \geq D _ { K L } ( \mathcal { T } _ { x } \left \| \mathcal { D } ^ { * } ( 1 ^ { n } , h ) \right ) - \text {Opt} _ { n }$$

$$= D _ { K L } ( \mathcal { T } _ { x } \| \mathcal { D } ^ { * } ( 1 ^ { n } , h ) ) - \min _ { a \in \{ 0 , 1 \} ^ { n } } D _ { K L } ( \mathcal { T } _ { x } \| \mathcal { D } ^ { * } ( 1 ^ { n } , a ) )$$

$$= \log \left ( \frac { 1 } { \Pr [ x \leftarrow \mathcal { D } ^ { * } ( 1 ^ { n } , h ) ] } \right ) - \min _ { a \in \{ 0 , 1 \} ^ { n } } \log \left ( \frac { 1 } { \Pr [ x \leftarrow \mathcal { D } ^ { * } ( 1 ^ { n } , a ) ] } \right )$$

$$= \max _ { a \in \{ 0 , 1 \} ^ { n } } \log \left ( \frac { \Pr [ x \leftarrow \mathcal { D } ^ { * } ( 1 ^ { n } , a ) ] } { \Pr [ x \leftarrow \mathcal { D } ^ { * } ( 1 ^ { n } , h ) ] } \right )$$

$$2 \epsilon ( n ) \\ = D _ { K L } ( \mathcal { T } _ { x } \| \mathcal { D } ^ { * } ( 1 ^ { n } , h ) ) - \min _ { a \in \{ 0 , 1 \} ^ { n } } D _ { K L } ( \mathcal { T } _ { x } \| \mathcal { D } ^ { * } ( 1 ^ { n } , a ) ) \\ = \log \left ( \frac { 1 } { \Pr [ x \leftarrow \mathcal { D } ^ { * } ( 1 ^ { n } , h ) ] } \right ) - \min _ { a \in \{ 0 , 1 \} ^ { n } } \log \left ( \frac { 1 } { \Pr [ x \leftarrow \mathcal { D } ^ { * } ( 1 ^ { n } , h ) ] } \right ) \\ = \max _ { \ } \log \left ( \frac { \Pr [ x \leftarrow \mathcal { D } ^ { * } ( 1 ^ { n } , a ) ] } { \Pr [ x \leftarrow \mathcal { D } ^ { * } ( 1 ^ { n } , a ) ] } \right )$$

for all sufficiently large n ∈ N .

This implies that h satisfies

$$2 ^ { 1 / 2 \epsilon ( n ) } \geq \frac { \max _ { a \in \{ 0 , 1 \} ^ { n } } \{ \Pr [ x \leftarrow \mathcal { D } ^ { * } ( 1 ^ { n } , a ) ] \} } { \Pr [ x \leftarrow \mathcal { D } ^ { * } ( 1 ^ { n } , h ) ] }$$

$$= \frac { \{ ( 1 - C _ { n } ) \max _ { a \in \{ 0 , 1 \} ^ { n } } \{ \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , a ) ] \} + C _ { n } \cdot 2 ^ { - p ( n ) } } { ( 1 - C _ { n } ) \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , h ) ] + C _ { n } \cdot 2 ^ { - p ( n ) } }$$

for all sufficiently large n ∈ N . This implies that, for all x ∈ { 0 , 1 } p ( n ) with max a ∈{ 0 , 1 } n { Pr[ x ←D (1 n , a )] } &gt; 0 , h satisfies

$$\Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , h ) ] \geq 2 ^ { - 1 / 2 \epsilon ( n ) } \max _ { a \in \{ 0 , 1 \} ^ { n } } \{ \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , a ) ] \} - \frac { 1 - 2 ^ { - 1 / 2 \epsilon ( n ) } } { 1 - C _ { n } } C _ { n } \cdot 2 ^ { - p ( n ) }$$

$$\geq 2 ^ { - 1 / 2 \epsilon ( n ) } \max _ { a \in \{ 0 , 1 \} ^ { n } } \{ \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , a ) ] \} - 2 \cdot C _ { n } \cdot 2 ^ { - p ( n ) }$$

$$= 2 ^ { - 1 / 2 \epsilon ( n ) } \max _ { a \in \{ 0 , 1 \} ^ { n } } \{ \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , a ) ] \} - ( 2 ^ { - 1 / 2 \epsilon ( n ) } - 2 ^ { - 1 / \epsilon ( n ) } ) \cdot 2 ^ { - m ( n ) } \quad ( 1 6 2 )$$

$$\geq 2 ^ { - 1 / 2 \epsilon ( n ) } \max _ { a \in \{ 0 , 1 \} ^ { n } } \{ \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , a ) ] \} - ( 2 ^ { - 1 / 2 \epsilon ( n ) } - 2 ^ { - 1 / \epsilon ( n ) } ) \max _ { a \in \{ 0 , 1 \} ^ { n } } \{ \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , a ) ] \} \}$$

$$= 2 ^ { - 1 / \epsilon ( n ) } \cdot \max _ { a \in \{ 0 , 1 \} ^ { n } } \{ \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , a ) ] \} .$$

Here, in the Equation (161), we have used 1 -C n ≥ 1 2 , and in the Equation (162), we have used the definition of C n , and in the Equation (163), we have used that max a ∈{ 0 , 1 } n { Pr[ x ←D (1 n , a )] } ≥ 2 -m ( n ) .

This implies that there exists a QPT A such that for all x ∈ { 0 , 1 } p ( n ) with max a ∈{ 0 , 1 } n Pr[ x ←D (1 n , a )] &gt; 0 , we have

$$\Pr \left [ \frac { \max _ { a \in \{ 0 , 1 \} ^ { n } } \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , a ) ] } { \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , h ) ] } \leq 2 ^ { 1 / \epsilon ( n ) } \colon h \leftarrow \mathcal { A } ( 1 ^ { n } , x ) \right ] \geq 1 - 1 / \delta ( n )$$

for all sufficiently large n ∈ N , which is a contradiction.

Proof of Lemma 4.8. Let ϵ , δ , and p be polynomials, and let D be a QPT algorithm given in Definition 4.1. From D , we show that there exist a polynomial t and a QPT algorithm D ∗ such that, for any QPT algorithm A , there exists x ∈ { 0 , 1 } t ( n ) · p ( n ) with max a ∈{ 0 , 1 } n Pr[ x ←D ∗ (1 n , a )] &gt; 0 such that

$$\Pr \left [ \frac { \max _ { a \in \{ 0 , 1 \} ^ { n } } \Pr [ x \leftarrow \mathcal { D } ^ { * } ( 1 ^ { n } , a ) \right ] } { \Pr [ x \leftarrow \mathcal { D } ^ { * } ( 1 ^ { n } , h ) ] } \leq 2 ^ { \frac { t ( n ) } { 2 \epsilon ( n ) } \colon h \leftarrow \mathcal { A } ( 1 ^ { n } , x ) } \right ] \leq 1 - 1 / \delta ( n )$$

for infinitely many n ∈ N .

There exists a polynomial m such that Pr[ x ←D (1 n , z )] ≥ 2 -m ( n ) for all x ∈ { 0 , 1 } p ( n ) and z ∈ { 0 , 1 } n . Let t ( n ) := ⌈ 1000 m 2 ( n ) ϵ 2 ( n ) ( n +log(2 δ ( n ))) ⌉ . Let us consider the following QPT algorithm D ∗ .

D ∗ (1 n , z ) :

1. Run x i ←D (1 n , z ) for all i ∈ [ t ( n )] .
2. Output x := { x i } i ∈ [ t ( n )] .

In the following, we will show that D ∗ satisfies Equation (166). For contradiction, let us assume that there exists a QPT algorithm A such that for all x ∈ { 0 , 1 } t ( n ) · p ( n ) with max a ∈{ 0 , 1 } n Pr[ x ←D ∗ (1 n , a )] &gt; 0 , we have

$$\Pr \left [ \frac { \max _ { a \in \{ 0 , 1 ^ { n } \} } \Pr [ x \leftarrow \mathcal { D } ^ { * } ( 1 ^ { n } , a ) ] } { \Pr [ x \leftarrow \mathcal { D } ^ { * } ( 1 ^ { n } , h ) ] } \leq 2 ^ { \frac { t ( n ) } { 2 ^ { t ( n ) } } } \colon h \leftarrow \mathcal { A } ( 1 ^ { n } , x ) \right ] \geq 1 - 1 / 2 \delta ( n )$$

for all sufficiently large n ∈ N . Then, we show that A contradicts the security of D .

For showing it, we use the following claim.

Claim 4.9. Let T be any algorithm that, on input 1 n , outputs a p ( n ) -bit string. For all sufficiently large n ∈ N , with probability at least 1 -1 /δ ( n ) over { x i } i ∈ [ t ( n )] ←T (1 n ) ⊗ t ( n ) and h ←A (1 n , { x i } i ∈ [ t ( n )] ) , we have

$$\mathbb { E } _ { x \leftarrow \mathcal { T } ( 1 ^ { n } ) } \left [ \log \left ( \frac { \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , z ) ] } { \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , h ) ] } \right ) \right ] \leq 1 / \epsilon ( n )$$

for all z ∈ { 0 , 1 } n .

We give the proof of Claim 4.9 in the end of the proof. From Claim 4.9, for all sufficiently large n ∈ N , with probability at least 1 -1 /δ ( n ) over { x i } i ∈ [ t ( n )] ←T (1 n ) ⊗ t ( n ) and h ←A (1 n , { x i } i ∈ [ t ( n )] ) , we have

$$1 / \epsilon ( n ) \geq \sum _ { x \in \{ 0 , 1 \} ^ { p ( n ) } } \Pr [ x \leftarrow \mathcal { T } ( 1 ^ { n } ) ] \left ( \log \left ( \frac { 1 } { \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , h ) ] } \right ) - \log \left ( \frac { 1 } { \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , z ) ] } \right ) \right )$$

$$= \sum _ { x \in \{ 0 , 1 \} ^ { p ( n ) } } \Pr [ x \leftarrow \mathcal { T } ( 1 ^ { n } ) ] \left ( \log \left ( \frac { \Pr [ x \leftarrow \mathcal { T } ( 1 ^ { n } ) ] } { \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , h ) ] } \right ) - \log \left ( \frac { \Pr [ x \leftarrow \mathcal { T } ( 1 ^ { n } ) ] } { \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , z ) ] } \right ) \right ) \quad ( 1 7 0 )$$

$$= D _ { K L } ( \mathcal { T } ( 1 ^ { n } ) \| \mathcal { D } ( 1 ^ { n } , h ) ) - D _ { K L } ( \mathcal { T } ( 1 ^ { n } ) \| \mathcal { D } ( 1 ^ { n } , z ) )$$

for all z ∈ { 0 , 1 } n . This implies that h satisfies

$$D _ { K L } ( \mathcal { T } ( 1 ^ { n } ) \, \| \, \mathcal { D } ( 1 ^ { n } , h ) ) \leq O p t _ { n } + 1 / \epsilon ( n )$$

for all sufficiently large n ∈ N . This contradicts the security of D .

Proof of Claim 4.9. From the definition of A , for all sufficiently large n ∈ N , with probability at least 1 -1 2 δ ( n ) over h ←A (1 n , { x i } i ∈ [ t ( n )] ) , we have

$$\frac { 1 } { t ( n ) } \sum _ { i \in [ t ( n ) ] } \log \left ( \frac { 1 } { \Pr [ x _ { i } \leftarrow \mathcal { D } ( 1 ^ { n } , h ) ] } \right ) + \max _ { a \in \{ 0 , 1 \} ^ { n } } \frac { 1 } { t ( n ) } \sum _ { i \in [ t ( n ) ] } \log \left ( \Pr [ x _ { i } \leftarrow \mathcal { D } ( 1 ^ { n } , a ) ] \right ) \leq \frac { 1 } { 2 \epsilon ( n ) } \ \ ( 1 7 3 )$$

for all x ∈ { 0 , 1 } t ( n ) · p ( n ) such that max a ∈{ 0 , 1 } n Pr[ x ←D ∗ (1 n , a )] &gt; 0 . Therefore, for all sufficiently large n ∈ N , with probability at least 1 -1 2 δ ( n ) over h ←A (1 n , { x i } i ∈ [ t ( n )] ) , for all z ∈ { 0 , 1 } n , we have

$$& \frac { 1 } { t ( n ) } \sum _ { i \in [ t ( n ) ] } \log \left ( \frac { 1 } { \Pr [ x _ { i } \leftarrow \mathcal { D } ( 1 ^ { n } , h ) \right ] } \right ) - \frac { 1 } { t ( n ) } \sum _ { i \in [ t ( n ) ] } \log \left ( \frac { 1 } { \Pr [ x _ { i } \leftarrow \mathcal { D } ( 1 ^ { n } , z ) ] } \right ) \\ & \leq \frac { 1 } { t ( n ) } \sum _ { i \in [ t ( n ) ] } \log \left ( \frac { 1 } { \Pr [ x _ { i } \leftarrow \mathcal { D } ( 1 ^ { n } , h ) ] } \right ) + \max _ { a \in \{ 0 , 1 \} } \frac { 1 } { t ( n ) } \sum _ { i \in [ t ( n ) ] } \log \left ( \Pr [ x _ { i } \leftarrow \mathcal { D } ( 1 ^ { n } , a ) ] \right ) \leq \frac { 1 } { 2 \epsilon ( n ) } .$$

On the other hand, from Lemma 2.1, with probability at least 1 -1 2 δ ( n ) over { x i } i ∈ [ t ( n )] ←T (1 n ) ⊗ t ( n ) ,

$$\left | \mathbb { E } _ { x \leftarrow \mathcal { T } ( 1 ^ { n } ) } \left [ \log \left ( \frac { 1 } { \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , z ) ] } \right ) \right ] - \frac { 1 } { t ( n ) } \sum _ { i \in \left [ t ( n ) \right ] } \log \left ( \frac { 1 } { \Pr [ x _ { i } \leftarrow \mathcal { D } ( 1 ^ { n } , z ) ] } \right ) \right | \leq \frac { 1 } { 4 \epsilon ( n ) } \quad ( 1 7 6 )$$

for all z ∈ { 0 , 1 } n at the same time. Here, we have used the fact that

$$\log \left ( \frac { 1 } { \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , z ) ] } \right ) \leq m ( n )$$

for all x ∈ { 0 , 1 } p ( n ) and z ∈ { 0 , 1 } n . From union bound, Equations (175) and (176) implies that, for all sufficiently large n ∈ N , with probability at least 1 -1 δ ( n ) , over { x i } i ∈ [ t ( n )] ← T (1 n ) ⊗ t ( n ) and h ←A (1 n , { x i } i ∈ [ t ( n )] ) , we have

$$\mathbb { E } _ { x \leftarrow \mathcal { T } ( 1 ^ { n } ) } \left [ \log \left ( \frac { 1 } { \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , h ) ] } \right ) \right ] - \mathbb { E } _ { x \leftarrow \mathcal { T } ( 1 ^ { n } ) } \left [ \log \left ( \frac { 1 } { \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , z ) ] } \right ) \right ] \leq \frac { 1 } { \epsilon ( n ) }$$

for all z ∈ { 0 , 1 } n . Therefore, with probability at least 1 -1 δ ( n ) over { x i } i ∈ [ t ( n )] ← T (1 n ) ⊗ t ( n ) and h ←A (1 n , { x i } i ∈ [ t ( n )] ) , we have

$$\mathbb { E } _ { x \leftarrow \mathcal { T } ( 1 ^ { n } ) } \left [ \log \left ( \frac { \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , z ) ] } { \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , h ) ] } \right ) \right ] \leq \frac { 1 } { \epsilon ( n ) }$$

n

$$\text {for all } z \in \{ 0 , 1 \} ^ { n } .$$

## 4.2 Classical Case

In this subsection, we apply the previous quantum results to the classical case.

Definition 4.10 (Hardness of Agnostic Classical Distribution Learning with respect to KL divergence [AW92]). We say that hardness of agnostic classical distribution learning with respect to KL divergence holds if the following holds. There exist some polynomial ϵ , δ and p , and a PPT algorithm D , which takes 1 n and z ∈ { 0 , 1 } n as input, and outputs x ∈ { 0 , 1 } p ( n ) such that the following two conditions are satisfied:

1. For all n ∈ N , z ∈ { 0 , 1 } n , and x ∈ { 0 , 1 } p ( n ) , we have

$$\Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , z ) ] \neq 0 .$$

̸

2. For any PPT algorithm A and any polynomial t , there exists an algorithm T , which takes 1 n as input and outputs x ∈ { 0 , 1 } p ( n ) , such that

$$\Pr \left [ D _ { K L } ( \mathcal { T } ( 1 ^ { n } ) \left \| \mathcal { D } ( 1 ^ { n } , h ) \right ) \leq \text {Opt} _ { n } + 1 / \epsilon ( n ) \, \colon \, \begin{array} { c } \{ x _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow \mathcal { T } ( 1 ^ { n } ) ^ { \otimes t ( n ) } \\ h \leftarrow \mathcal { A } ( 1 ^ { n } , \{ x _ { i } \} _ { i \in [ t ( n ) ] } ) \end{array} \right ] \leq 1 - 1 / \delta ( n )$$

for infinitely many n ∈ N . Here, Opt n := min a ∈{ 0 , 1 } n { D KL ( T (1 n ) ‖ D (1 n , a )) } .

Definition 4.11 (Worst-Case Hardness of Classical Maximum Likelihood Estimation). We say that worstcase hardness of classical maximum likelihood estimation holds if the following holds. There exist some polynomial ϵ , δ and p , and a PPT algorithm D , which takes 1 n and z ∈ { 0 , 1 } n as input, and outputs x ∈ { 0 , 1 } p ( n ) such that, for any PPT algorithm A , there exist x ∈ { 0 , 1 } p ( n ) with max a ∈{ 0 , 1 } n Pr[ x ←D (1 n , a )] &gt; 0 such that

$$\Pr \left [ \frac { \max _ { a \in \{ 0 , 1 \} ^ { n } } \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , a ) ] } { \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , h ) ] } \leq 2 ^ { \epsilon ( n ) } \colon h \leftarrow \mathcal { A } ( 1 ^ { n } , x ) \right ] \leq 1 - 1 / \delta ( n )$$

for infinitely many n ∈ N .

Theorem 4.12. The following three conditions are equivalent:

1. NP ⊈ BPP .
2. Hardness of agnostic classical distribution learning with respect to KL divergence holds.
3. Worst-case hardness of classical maximum likelihood estimation holds.

The proof of Theorem 4.12 is similar to Theorem 4.4. Therefore, we give only a sketch of the proof.

Proof sketch of Theorem 4.12. We can show that (2) ⇒ (3) and (2) ⇐ (3) in the same way as Lemma 4.7 and Lemma 4.8, respectively.

(3) ⇐ (1) follows in the same way as Lemma 4.5. We can show that BPP path ⊆ BPP if worstcase hardness of classical maximum likelihood estimation does not hold. BPP path ⊆ BPP implies NP ⊆ BPP .

(1) ⇐ (3) follows in the same way as Lemma 4.6 (For details, see Lemma 4.2 in [HH24].) [HH24] proves Lemma 4.6 by using Lemma A.3. (1) ⇐ (3) follows by using Theorem 2.2 instead.

## 5 Agnostic Quantum Distribution Learning with Respect to Statistical Distance

## 5.1 Upper Bounds of Distribution Learning with Respect to Statistical Distance

In this section, we introduce the agnostic distribution learning with respect to statistical distance. Then, we state that if PP = BQP (resp. NP ⊆ BPP ), then a QPT (resp. PPT) algorithm can achieve agnostic quantum (resp. classical) distribution learning with respect to statistical distance.

Definition 5.1 (Agnostic Distribution Learning with Respect to Statistical Distance [KMR + 94]). We say that an algorithm A achieves agnostic quantum (resp. classical) distribution learning with respect to statistical distance if the following holds: For any polynomial ϵ and δ , there exists a polynomial t such that for any QPT (resp. PPT) algorithm D , which takes 1 n and z ∈ { 0 , 1 } n as input, and outputs x ∈ { 0 , 1 } poly( n ) and an algorithm T , which takes 1 n as input and outputs x ∈ { 0 , 1 } poly( n ) , we have

$$\Pr \left [ \text {SD} ( \mathcal { D } ( 1 ^ { n } , h ) , \mathcal { T } ( 1 ^ { n } ) ) \leq ( 3 + 1 / \epsilon ( n ) ) \cdot \text {Opt} _ { n } + 1 / \epsilon ( n ) \colon \quad & \stackrel { \{ x _ { i } \} _ { i \in [ t ( n ) ] } } { h \to \mathcal { A } ( 1 ^ { n } , \{ x _ { i } \} _ { i \in [ t ( n ) ] } ) } \right ] \geq 1 - 1 / \delta ( n )$$

for all sufficiently large n ∈ N . Here, Opt n := min a ∈{ 0 , 1 } n SD ( D (1 n , a ) , T (1 n )) .

Remark 5.2. In our definition of agnostic distribution learning, the learner needs to output a hypothesis h such that SD ( D (1 n , h ) , T (1 n )) ≤ (3 + 1 /ϵ ( n )) · min a SD ( D (1 n , a ) , T (1 n )) + 1 /ϵ ( n ) . One might wonder why we consider (3 + 1 /ϵ ( n )) · min a SD ( D (1 n , a ) , T (1 n )) instead of min a SD ( D (1 n , a ) , T (1 n )) . This is because [BKM19] shows that no (even unbounded) algorithm can achieve a factor strictly smaller than 3 . Therefore, we consider SD ( D (1 n , h ) , T (1 n )) ≤ (3 + 1 /ϵ ( n )) · min a SD ( D (1 n , a ) , T (1 n )) + 1 /ϵ ( n ) in this work.

We show that a PPT algorithm with access to a Σ P 3 oracle achieves agnostic classical distribution learning with respect to statistical distance.

Theorem 5.3. There exists a PPT algorithm with access to a Σ P 3 oracle which achieves agnostic classical distribution learning with respect to statistical distance.

We also show that a PPT algorithm with access to a Σ PP 2 oracle achieves agnostic quantum distribution learning with respect to statistical distance.

Theorem 5.4. There exists a PPT algorithm with access to a Σ PP 2 oracle which achieves agnostic quantum distribution learning with respect to statistical distance.

We give the proof of Theorem 5.3 in Section 5.3. The proof of Theorem 5.4 is similar to that of Theorem 5.3. For clarity, we give the sketch of the proof in Appendix A. Theorems 5.3 and 5.4 imply the following Corollaries 5.5 and 5.6, respectively.

Corollary 5.5. If NP ⊆ BPP , then there exists a PPT algorithm which achieves agnostic classical distribution learning with respect to the statistical distance.

Corollary 5.6. If PP ⊆ BQP , then there exists a QPT algorithm which achieves agnostic quantum distribution learning with respect to the statistical distance.

Proof of Corollary 5.5. If NP ⊆ BPP , then we have Σ P 3 ⊆ BPP . Therefore, a PPT algorithm can simulate Σ P 3 oracle. Hence, from Theorem 5.3, a PPT algorithm can achieve agnostic classical distribution learning with respect to statistical distance assuming NP ⊆ BPP .

Proof of Corollary 5.6. This is the same as Corollary 5.5. If PP ⊆ BQP , then we have Σ PP 2 ⊆ BQP . Therefore, a QPT algorithm can simulate Σ PP 2 oracle. Hence, from Theorem 5.3, a QPT algorithm can achieve agnostic quantum distribution learning with respect to statistical distance assuming PP ⊆ BQP .

## 5.2 Quantum Advantage and Hardness of Agnostic Quantum Distribution Learning

In this section, we study relation between hardness of agnostic quantum distribution learning and samplingbased quantum advantage.

Assumption 5.7 (Hardness of Agnostic Quantum Distribution Learning against PPT with Σ P 3 Oracle). We say that hardness of agnostic quantum distribution learning against PPT with access to a Σ P 3 oracle holds if the following holds. There exist some polynomials ϵ and δ , and a QPT algorithm D , which takes 1 n and z ∈ { 0 , 1 } n as input, and outputs x ∈ { 0 , 1 } poly( n ) such that, for any PPT algorithm A with access to a Σ P 3 oracle and any polynomial t , there exist an algorithm T , which takes 1 n as input and outputs x ∈ { 0 , 1 } poly( n ) , such that

$$\Pr \left [ \text {SD} ( \mathcal { D } ( 1 ^ { n } , h ) , \mathcal { T } ( 1 ^ { n } ) ) \leq ( 3 + 1 / \epsilon ( n ) ) \cdot \text {Opt} _ { n } + 1 / \epsilon ( n ) \colon \quad & \stackrel { \{ x _ { i } \} _ { i } \in [ t ( n ) ] } { h \to \mathcal { A } ^ { \text {SP} } _ { 3 } ( 1 ^ { n } , \{ x _ { i } \} _ { i } \in [ t ( n ) ] ) } \right ] \leq 1 - 1 / \delta ( n )$$

for infinitely many n ∈ N . Here, Opt n := min a ∈{ 0 , 1 } n SD ( D (1 n , a ) , T (1 n )) .

Assumption 5.8 (PP-hardness of Agnostic Quantum Distribution Learning with Respect to Statistical Distance). We say that agnostic quantum distribution learning with respect to statistical distance is PP -hard in a PPT black-box reduction if there exist polynomials ϵ and δ , and a QPT algorithm D , which takes 1 n and z ∈ { 0 , 1 } n as input, and outputs x ∈ { 0 , 1 } poly( n ) , such that the following condition is satisfied: For any oracle O such that there exists a polynomial t such that for any algorithm T , which takes 1 n as input, and outputs x ∈ { 0 , 1 } poly( n ) ,

$$\Pr \left [ \text {SD} ( \mathcal { D } ( 1 ^ { n } , h ) , \mathcal { T } ( 1 ^ { n } ) ) \leq ( 3 + 1 / \epsilon ( n ) ) \cdot \text {Opt} _ { n } + 1 / \epsilon ( n ) \colon \quad & \stackrel { \{ x _ { i } \} _ { i } \} _ { i } \in [ t ( n ) ] } { h \leftarrow \mathcal { O } ( 1 ^ { n } , \{ x _ { i } \} _ { i } \{ t ( n ) \} ) } \right ] \geq 1 - 1 / \delta ( n ) \\$$

for all sufficiently large n ∈ N , we have PP ⊆ BPP O .

Our first result is that the hardness of learning is derived from the standard quantum advantage assumption (Assumption 2.10) plus PP ⊈ BQP Σ P 3 .

Theorem 5.9. PP ⊈ BQP Σ P 3 and quantum advantage assumption (Assumption 2.10) imply Assumption 5.7.

Remark 5.10. In the above Theorem, we established hardness against a PPT algorithm with access to a Σ P 3 oracle. The same hardness result holds even for a QPT algorithm with access to a Σ P 3 oracle.

We give the proof of Theorem 5.9 in Appendix B.

Our next result is that hardness of agnostic quantum distribution learning with respect to statistical distance implies sampling-based quantum advantage.

̸

## Theorem 5.11. Assumption 5.7 implies SampBQP = SampBPP .

Our third result is that showing PP -hardness of agnostic quantum distribution learning (in a black-box way) is difficult.

̸

Theorem 5.12. If agnostic quantum distribution learning with respect to statistical distance is PP -hard in a PPT black-box reduction (Assumption 5.8), then PP ⊈ BPP Σ P 3 implies SampBQP = SampBPP .

Proof of Theorem 5.11. For contradiction, suppose SampBQP = SampBPP . Then, we will show that Assumption 5.7 does not hold.

From the assumption of SampBQP = SampBPP , for any polynomial ϵ and any QPT algorithm D , which takes 1 n and z ∈ { 0 , 1 } n as input, and outputs x ∈ { 0 , 1 } poly( n ) , there exists a PPT algorithm C D ,ϵ that takes 1 n and z ∈ { 0 , 1 } n as input, and outputs x ∈ { 0 , 1 } poly( n ) such that

$$\text {SD} ( \mathcal { D } ( 1 ^ { n } , z ) , \mathcal { C } _ { \mathcal { D } , \epsilon } ( 1 ^ { n } , z ) ) \leq \frac { 1 } { 1 0 0 \epsilon ( n ) }$$

for all z ∈ { 0 , 1 } n and all n ∈ N . From Theorem 5.3, for any PPT algorithm C D ,ϵ (1 n , · ) , there exists a PPT algorithm A with access to a Σ P 3 oracle and a polynomial t such that for any algorithm T (1 n ) , which takes 1 n as input and outputs x ∈ { 0 , 1 } poly( n ) , we have

$$\Pr \left [ \, \text {SD} ( \mathcal { T } ( 1 ^ { n } ) , \mathcal { O } _ { \mathcal { D } , \epsilon } ( 1 ^ { n } , h ) ) \leq ( 3 + \frac { 1 } { 1 0 0 c ( n ) } ) \cdot \text {Opt} _ { n } ^ { * } + \frac { 1 } { 1 0 0 c ( n ) } \ \colon \ \begin{array} { c } \{ x _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow \mathcal { T } ( 1 ^ { n } ) ^ { \otimes t ( n ) } \\ h \leftarrow \mathcal { A } ^ { \Sigma _ { 3 } ^ { 1 } } ( 1 ^ { n } , \{ x _ { i } \} _ { i \in [ t ( n ) ] } ) \end{array} \right ] \geq 1 - 1 / \delta ( n )$$

for all sufficiently large n ∈ N . Here, Opt ∗ n := min a ∈{ 0 , 1 } n SD ( T (1 n ) , C D ,ϵ (1 n , a )) .

This implies that with probability at least 1 -1 δ ( n ) over { x i } i ∈ [ t ( n )] ←T (1 n ) ⊗ t ( n ) and h ←A Σ P 3 (1 n , { x i } i ∈ [ t ( n )] ) ,

$$\S D ( \mathcal { T } ( 1 ^ { n } ) , \mathcal { D } ( 1 ^ { n } , h ) ) \leq \S D ( \mathcal { T } ( 1 ^ { n } ) , \mathcal { C } _ { \mathcal { D } , \epsilon } ( 1 ^ { n } , h ) ) + \S D ( \mathcal { D } ( 1 ^ { n } , h ) , \mathcal { C } _ { \mathcal { D } , \epsilon } ( 1 ^ { n } , h ) )$$

$$\leq \left ( 3 + \frac { 1 } { 1 0 0 \epsilon ( n ) } \right ) \cdot \text {Opt} _ { n } ^ { * } + \frac { 2 } { 1 0 0 \epsilon ( n ) }$$

$$\leq \left ( 3 + \frac { 1 } { 1 0 0 \epsilon ( n ) } \right ) \cdot \left ( \text {Opt} _ { n } + \frac { 1 } { 1 0 0 \epsilon ( n ) } \right ) + \frac { 2 } { 1 0 0 \epsilon ( n ) }$$

$$\leq \left ( 3 + \frac { 1 } { \epsilon ( n ) } \right ) \cdot \text {Opt} _ { n } + \frac { 1 } { \epsilon ( n ) }$$

for all sufficiently large n ∈ N , where Opt n := min a ∈{ 0 , 1 } n { SD ( T (1 n ) , D (1 n , a )) } . Here, in the third inequality, we have used Opt ∗ n ≤ Opt n + 1 100 ϵ ( n ) .

This is a contradiction to Assumption 5.7.

Proof of Theorem 5.12. From Theorem 5.11, it is sufficient to prove that Assumption 5.8 and PP ⊈ BPP Σ P 3 imply Assumption 5.7. For contradiction, suppose that Assumption 5.7 does not hold, then we show that either Assumption 5.8 or PP ⊈ BPP Σ P 3 does not hold. For showing this, it is sufficient to show that if Assumption 5.7 does not hold, then Assumption 5.8 implies PP ⊆ BPP Σ P 3 .

Because we assume that Assumption 5.7 does not hold, for any polynomial ϵ and δ , there exists a PPT algorithm A with access to a Σ P 3 oracle such that Equation (184) does not hold for all sufficiently large n ∈ N . Furthermore, from Assumption 5.8, for any language L ∈ PP , there exists a PPT algorithm R such that the following two conditions are satisfied:

1. For all x ∈ L , we have
2. For all x / ∈ L , we have

for all sufficiently large n ∈ N .

Proof of Theorem 5.3. Let D be a PPT algorithm that takes 1 n and z ∈ { 0 , 1 } n as input, and outputs x ∈ { 0 , 1 } poly( n ) . Let ϵ and δ be polynomials. In the following, we show that there exists a polynomial t , and a PPT algorithm A with access to a Σ P 3 oracle such that, for all algorithms T , which takes 1 n and outputs x ∈ { 0 , 1 } poly( n ) , we have

$$\Pr \left [ \text {SD} ( \mathcal { D } ( 1 ^ { n } , h ) , \mathcal { T } ( 1 ^ { n } ) ) \leq ( 3 + 1 / \epsilon ( n ) ) \cdot \text {Opt} _ { n } + 1 / \epsilon ( n ) \colon \quad & \stackrel { \{ x _ { i } \} _ { i } \in [ t ( n ) ] } { h \to \mathcal { A } ^ { \text {SP} } _ { 3 } ( 1 ^ { n } , \{ x _ { i } \} _ { i } \in [ t ( n ) ] ) } \right ] \geq 1 - 1 / \delta ( n )$$

$$\Pr \left [ 1 \leftarrow \mathcal { R } ^ { \mathcal { A } ^ { \Sigma } _ { 3 } } ( x ) \right ] \geq \frac { 2 } { 3 } .$$

$$\Pr \left [ 1 \leftarrow \mathcal { R } ^ { \mathcal { A } ^ { \Sigma } _ { 3 } } ( x ) \right ] \leq \frac { 1 } { 3 } .$$

Then, by simulating R A Σ P 3 ( x ) , a PPT algorithm M with access to a Σ P 3 oracle can decide if x is in L or not. This implies that PP ⊆ BPP Σ P 3 .

## 5.3 Proof of Theorem 5.3

In this section, we give the proof of Theorem 5.3. For showing Theorem 5.3, we use the following Theorem 5.13, which we prove later.

Theorem 5.13. For any polynomial ϵ , any PPT algorithm D that takes 1 n and z ∈ { 0 , 1 } n as input and outputs x ∈ { 0 , 1 } poly( n ) , there exists a PPT algorithm Dis ϵ with access to an NP oracle, which takes 1 n , ℓ ∈ { 0 , 1 } n , m ∈ { 0 , 1 } n , and x ∈ { 0 , 1 } poly( n ) as input, and outputs b ∈ { 0 , 1 } , such that for all ( ℓ, m ) ∈ { 0 , 1 } n ×{ 0 , 1 } n with SD ( D (1 n , ℓ ) , D (1 n , m )) ≥ 1 /ϵ ( n ) , we have

$$\S D ( \mathcal { D } ( 1 ^ { n } , \ell ) , \mathcal { D } ( 1 ^ { n } , m ) )$$

$$\leq \left ( 1 + \frac { 1 } { 4 \epsilon ( n ) } \right ) \left | \Pr \left [ 1 \leftarrow \text {Dis} _ { \epsilon } ^ { \text {NP} } ( 1 ^ { n } , \ell , m , x ) \colon x \leftarrow \mathcal { D } ( 1 ^ { n } , \ell ) \right ] \right ]$$

$$- \Pr \left [ 1 \leftarrow \text {Dis} _ { \epsilon } ^ { \text {NP} } ( 1 ^ { n } , \ell , m , x ) \colon x \leftarrow \mathcal { D } ( 1 ^ { n } , m ) \right ] \right | + \frac { 1 } { 4 \epsilon ( n ) }$$

for all sufficiently large n ∈ N . Here, Opt n := min a ∈{ 0 , 1 } n SD ( T (1 n ) , D (1 n , a )) .

For simplicity, in the following, we often omit 1 n of T (1 n ) , D (1 n , a ) , and Dis NP ϵ (1 n , a, b, x ) . We set t ( n ) := 100 n 2 · ϵ ( n ) 2 ( n +log( δ ( n ))) . To construct A , for any polynomial-time computable function ω , let us consider the following deterministic polynomial-time algorithm M ω with access to an NP oracle.

M NP ω (1 n , a, b, { x i , r i (1) , r i (2) , r i (3) } i ∈ [ t ( n )] ) :

1. Run Dis NP ϵ ( a, b, x i ; r i (1)) for all i ∈ [ t ( n )] .

$$2 . \text { For all } i \in [ t ( n ) ] , \text { run } X _ { a , r _ { i } ( 2 ) } \leftarrow \mathcal { D } ( a ; r _ { i } ( 2 ) ) \text { and Dis} ^ { \text {NP} } _ { \epsilon } ( a , b , X _ { a , r _ { i } ( 2 ) } ; r _ { i } ( 3 ) ) .$$

3. Output 1 if

$$\left | \sum _ { i \in [ t ( n ) ] } \frac { \text {Dis} _ { \epsilon } ^ { \text {NP} } ( a , b , x _ { i } ; r _ { i } ( 1 ) ) } { t ( n ) } - \sum _ { i \in [ t ( n ) ] } \frac { \text {Dis} _ { \epsilon } ^ { \text {NP} } ( a , b , X _ { a , r _ { i } ( 2 ) } ; r _ { i } ( 3 ) ) } { t ( n ) } \right | \leq \omega ( n ) .$$

Otherwise, output 0 .

For any polynomial-time computable function ω , and ( a 1 , ..., a I ) ∈ { 0 , 1 } I with I ∈ N , let us define

$$\mathcal { L } _ { \omega , ( a _ { 1 } , \dots , a _ { l } ) }$$

$$& \mathcal { L } _ { \omega , ( a _ { 1 } , \dots , a _ { I } ) } \\ & \quad \vdots = \left \{ \{ x _ { i } , r _ { i } ( 1 ) , r _ { i } ( 2 ) , r _ { i } ( 3 ) \} _ { i \in [ t ( n ) ] } \in \{ 0 , 1 \} ^ { * } , n \in \mathbb { N } \colon \exists a \in \{ 0 , 1 \} ^ { n - 1 } \text { such that } \forall b \in \{ 0 , 1 \} ^ { n } , \text { we have}$$

(200)

$$1 \leftarrow \mathcal { M } _ { \omega } ^ { \text {NP} } ( 1 ^ { n } , a _ { 1 } \| \dots \| a _ { I } \| a , b , \{ x _ { i } , r _ { i } ( 1 ) , r _ { i } ( 2 ) , r _ { i } ( 3 ) \} _ { i \in [ t ( n ) ] } \right ) .$$

We have L ω,a 1 ‖ ... ‖ a I ∈ Σ NP 2 = Σ P 3 .

Now, we construct the PPT algorithm A with access to a Σ P 3 oracle.

A Σ P 3 (1 n , { x i } i ∈ [ t ( n )] ) :

1. Uniformly sample random strings { r i (1) , r i (2) , r i (3) } i ∈ [ t ( n )] .
2. For each index I ∈ [ n ] , determine the output bit out I as follows:
3. (a) Initialize p (1) = 1 2 .
4. (b) For j = 1 to n , do:
- i. For each β ∈ { 0 , 1 } , check whether

$$( \{ x _ { i } , r _ { i } ( 1 ) , r _ { i } ( 2 ) , r _ { i } ( 3 ) \} _ { i \in [ t ( n ) ] } , n ) \in \mathcal { L } _ { p ( j ) , o u t _ { 1 } \dots \dots | o u t _ { I - 1 } \beta } .$$

Let Q β = 1 if the above holds, and Q β = 0 otherwise.

- ii. If Q 0 = Q 1 = 1 and j &lt; n , then set p ( j +1) = p ( j ) -( 1 2 ) j +1 and continue to the next j .
- iii. If Q 0 = Q 1 = 0 and j &lt; n , then set p ( j +1) = p ( j ) + ( 1 2 ) j +1 and continue to the next j .
- iv. If Q b = 1 and Q b ⊕ 1 = 0 for some b ∈ { 0 , 1 } , then set out I = b and break the j -loop.
- v. If j = n , then set out I = 1 , and break the j -loop.

## 3. Output the string out 1 ‖ . . . ‖ out n .

We use the following Claim 5.14.

Claim 5.14. With probability at least (1 -1 /δ ( n )) over { x i } i ∈ [ t ( n )] ←T ⊗ t ( n ) and out ←A Σ P 3 (1 n , { x i } i ∈ [ t ( n )] ) , out satisfies

$$\left | \Pr \left [ 1 \leftarrow D i s _ { \epsilon } ^ { N P } ( { \text {out} } , b , x ) \colon x \leftarrow \mathcal { T } \right ] - \Pr \left [ 1 \leftarrow D i s _ { \epsilon } ^ { N P } ( { \text {out} } , b , x ) \colon x \leftarrow \mathcal { D } ( { \text {out} } ) \right ] \right ] \leq \text {Opt} _ { n } + \frac { 1 } { 2 \epsilon ( n ) }$$

for all b ∈ { 0 , 1 } n . Here, Opt n := min a ∈{ 0 , 1 } n SD ( T , D ( a )) .

We defer the proof of Claim 5.14.

For simplicity, in the following, let us denote ℓ to mean ℓ := argmin a ∈{ 0 , 1 } n { SD ( D ( a ) , T ) } so that Opt n = SD ( D ( ℓ ) , T ) . In the following, we show that, for the out such that Equation (203) holds for all b ∈ { 0 , 1 } n , we have

$$\S D ( \mathcal { T } , \mathcal { D } ( \text {out} ) ) \leq ( 3 + 1 / \epsilon ( n ) ) \cdot \text {Opt} _ { n } + 1 / \epsilon ( n ) .$$

First, let us consider the case where SD ( D ( ℓ ) , D ( out )) &lt; 1 /ϵ ( n ) . In this case, we have

$$S D ( \mathcal { T } , \mathcal { D } ( \text {out} ) ) \leq S D ( \mathcal { T } , \mathcal { D } ( \ell ) ) + S D ( \mathcal { D } ( \ell ) , \mathcal { D } ( \text {out} ) ) < \text {Opt} _ { n } + \frac { 1 } { \epsilon ( n ) } .$$

Here, in the first inequality, we have used triangle inequality.

Now, let us consider the case, where SD ( D ( ℓ ) , D ( out )) ≥ 1 /ϵ ( n ) . In this case, we have

$$\S D ( \mathcal { T } , \mathcal { D } ( \text {out} ) )$$

$$\leq & \, \text {SD} ( \mathcal { T } , \mathcal { D } ( \ell ) ) + \text {SD} ( \mathcal { D } ( \ell ) , \mathcal { D } ( \text {out} ) )$$

$$\leq \text {Opt} _ { n } + \frac { 1 } { 4 \epsilon ( n ) }$$

$$+ \left ( 1 + \frac { 1 } { 4 \epsilon ( n ) } \right ) \left | \Pr \left [ 1 \leftarrow D i s _ { \epsilon } ^ { \text {NP} } ( \text {out} , \ell , x ) \colon x \leftarrow \mathcal { D } ( \ell ) \right ] - \Pr \left [ 1 \leftarrow D i s _ { \epsilon } ^ { \text {NP} } ( \text {out} , \ell , x ) \colon x \leftarrow \mathcal { D } ( \text {out} ) \right ] \right | \right |$$

$$\leq \text {Opt} _ { n } + \frac { 1 } { 4 \epsilon ( n ) }$$

$$+ \left ( 1 + \frac { 1 } { 4 \epsilon ( n ) } \right ) \left | \Pr \left [ 1 \leftarrow D i s _ { \epsilon } ^ { N P } ( o u t , \ell , x ) \colon x \leftarrow \mathcal { D } ( o u t ) \right ] - \Pr \left [ 1 \leftarrow D i s _ { \epsilon } ^ { N P } ( o u t , \ell , x ) \colon x \leftarrow \mathcal { T } \right ] \right | \\ \\$$

$$+ \left ( 1 + \frac { 1 } { 4 \epsilon ( n ) } \right ) \left | \Pr \left [ 1 \leftarrow D i s _ { \epsilon } ^ { \text {NP} } ( \text {out} , \ell , x ) \colon x \leftarrow \mathcal { T } \right ] - \Pr \left [ 1 \leftarrow D i s _ { \epsilon } ^ { \text {NP} } ( \text {out} , \ell , x ) \colon x \leftarrow \mathcal { D } ( \ell ) \right ] \right | \ \ ( 2 1 2 )$$

$$\leq \text {Opt} _ { n } + \frac { 1 } { 4 \epsilon ( n ) } + \left ( 1 + \frac { 1 } { 4 \epsilon ( n ) } \right ) \left ( \text {Opt} _ { n } + \frac { 1 } { 2 \epsilon ( n ) } \right ) + \left ( 1 + \frac { 1 } { 4 \epsilon ( n ) } \right ) \text {Opt} _ { n }$$

$$\leq & \left ( 3 + \frac { 1 } { \epsilon ( n ) } \right ) \cdot \text {Opt} _ { n } + \frac { 1 } { \epsilon ( n ) } .$$

Here, in Equation (208), we have used Theorem 5.13, in Equation (210), we have used the triangle inequality, and in Equation (213), we have used SD ( T (1 n ) , D ( ℓ )) ≤ Opt n and out satisfies the following inequality

$$\left | \Pr \left [ 1 \leftarrow D i s ^ { N P } ( \text {out} , b , x ) \colon x \leftarrow \mathcal { T } \right ] - \Pr \left [ 1 \leftarrow D i s ^ { N P } ( \text {out} , b , x ) \colon x \leftarrow \mathcal { D } ( \text {out} ) \right ] \right ] \leq \text {opt} _ { n } + \frac { 1 } { 2 \epsilon ( n ) } \right ]$$

for all b ∈ { 0 , 1 } n . This completes the proof.

Now, let us show the Claim 5.14, which we deferred the proof. For showing it, we use the following Claim 5.15, which can be shown by the standard average argument. We defer the proof of Claim 5.15 in the end of the proof.

Claim 5.15. Let us denote X a,r i (2) to mean the output of D ( a ; r i (2)) . Let p ( n ) bethesize of { r i (1) , r i (2) , r i (3) } i ∈ [ t ( n )] . Let Good n be a set of { x i , r i (1) , r i (2) , r i (3) } i ∈ [ t ( n )] such that, for all I ∈ [ n ] and for all ( a 1 , ..., a I -1 ) ∈ { 0 , 1 } I -1 , the following two conditions hold.

1. If there exists ( a I , ..., a n ) ∈ { 0 , 1 } n -I +1 such that

$$\left | \Pr \left [ 1 \leftarrow \text {Dis} _ { \epsilon } ^ { \text {NP} } ( a _ { 1 } \| \dots \| a _ { n } , b , x ) \colon x \leftarrow \mathcal { T } \right ] - \Pr \left [ 1 \leftarrow \text {Dis} _ { \epsilon } ^ { \text {NP} } ( a _ { 1 } \| \dots \| a _ { n } , b , x ) \colon x \leftarrow \mathcal { D } ( a _ { 1 } \| \dots \| a _ { n } ) \right ] \right | \right | \\$$

$$\leq \text {Opt} _ { n } + \frac { I - 1 } { 2 n \cdot \epsilon ( n ) }$$

for all b ∈ { 0 , 1 } n , then there exists ( a I +1 , ..., a n ) ∈ { 0 , 1 } n -I +1 such that

$$\left | \sum _ { i \in [ t ( n ) ] } \frac { \text {D} i s _ { \epsilon } ^ { \text {NP} } ( a _ { 1 } \dots | a _ { n } , b , x _ { i } ; r _ { i } ( 1 ) ) } { t ( n ) } - \sum _ { i \in [ t ( n ) ] } \frac { \text {D} i s _ { \epsilon } ^ { \text {NP} } ( a _ { 1 } \dots | a _ { n } , b , X _ { a , r _ { i } ( 2 ) } ; r _ { i } ( 3 ) ) } { t ( n ) } \right | \leq \text {Opt} _ { n } + \frac { ( 4 I - 3 ) } { 8 n \cdot \epsilon ( n ) }$$

for all b ∈ { 0 , 1 } n .

2. If for all ( a I +1 , ..., a n ) ∈ { 0 , 1 } n -I +1 , there exists b ∈ { 0 , 1 } n such that

$$\left | \Pr \left [ 1 \leftarrow \text {Dis} _ { \epsilon } ^ { \text {NP} } ( a _ { 1 } \| \dots \| a _ { n } , b , x ) \colon x \leftarrow \mathcal { T } \right ] - \Pr \left [ 1 \leftarrow \text {Dis} _ { \epsilon } ^ { \text {NP} } ( a _ { 1 } \| \dots \| a _ { n } , b , x ) \colon x \leftarrow \mathcal { D } ( a _ { 1 } \| \dots \| a _ { n } ) \right ] \right | \right |$$

$$\geq \text {Opt} _ { n } + \frac { I } { 2 n \cdot \epsilon ( n ) } ,$$

then for all ( a I +1 , ..., a n ) ∈ { 0 , 1 } n -I +1 , there exists b ∈ { 0 , 1 } n such that

$$\left | \sum _ { i \in [ t ( n ) ] } \frac { \text {D} i s _ { \epsilon } ^ { \text {NP} } ( a _ { 1 } | \dots | a _ { n } , b , x _ { i } ; r _ { i } ( 1 ) ) } { t ( n ) } - \sum _ { i \in [ t ( n ) ] } \frac { \text {D} i s _ { \epsilon } ^ { \text {NP} } ( a _ { 1 } | \dots | a _ { n } , b , X _ { a , r _ { i } ( 2 ) } ; r _ { i } ( 3 ) ) } { t ( n ) } \right | \geq 0 \text {pt} _ { n } + \frac { ( 4 I - 1 ) } { 8 n \cdot \epsilon ( n ) } .$$

Then, we have

$$\Pr \left [ \{ x _ { i } , r _ { i } ( 1 ) , r _ { i } ( 2 ) , r _ { i } ( 3 ) \} _ { i \in [ t ( n ) ] } \in \text {Good} _ { n } \colon \quad \{ x _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow \mathcal { T } ^ { \otimes t ( n ) } \right ) \\ \{ r _ { i } ( 1 ) , r _ { i } ( 2 ) , r _ { i } ( 3 ) \} _ { i \in [ t ( n ) ] } \leftarrow \{ 0 , 1 \} ^ { p ( n ) } \right ] \geq 1 - 1 / \delta ( n ) .$$

Proof of Claim 5.14. Let Good n be a set of { x i , r i (1) , r i (2) , r i (3) } i ∈ [ t ( n )] defined in Claim 5.15. In the following, we show that, for all { x i , r i (1) , r i (2) , r i (3) } i ∈ [ t ( n )] ∈ Good n , A Σ P 3 (1 n , { x i } i ∈ [ t ( n )] ; { r i (1) , r i (2) , r i (3) } i ∈ [ t ( n )] ) outputs out := out 1 ‖ ... ‖ out n such that

$$\left | \Pr \left [ 1 \leftarrow D i s _ { \epsilon } ^ { N P } ( { \text {out} } , b , x ) \colon x \leftarrow \mathcal { T } \right ] - \Pr \left [ 1 \leftarrow D i s _ { \epsilon } ^ { N P } ( { \text {out} } , b , x ) \colon x \leftarrow \mathcal { D } ( { \text {out} } ) \right ] \right ] \leq \text {Opt} _ { n } + \frac { 1 } { 2 \epsilon ( n ) } \\$$

for all b ∈ { 0 , 1 } n . This can be shown by induction as follows.

First, we show that for the out 1 , there exists ( a 2 , ..., a n ) ∈ { 0 , 1 } n -1 such that

$$\left | \Pr \left [ 1 \leftarrow D i s _ { \epsilon } ^ { \text {NP} } ( \text {out} _ { 1 } \| a _ { 2 } \| \dots \| a _ { n } , b , x ) \colon x \leftarrow \mathcal { T } \right ] - \Pr \left [ 1 \leftarrow D i s _ { \epsilon } ^ { \text {NP} } ( \text {out} _ { 1 } \| a _ { 2 } \| \dots \| a _ { n } , b , x ) \colon x \leftarrow \mathcal { D } ( \text {out} _ { 1 } \| a _ { 2 } \| \dots \| a _ { n } ) \right ] \right ] \right |$$

$$\leq \text {Opt} _ { n } + \frac { 1 } { 2 n \cdot \epsilon ( n ) }$$

for all b ∈ { 0 , 1 } n . From the definition of Opt n , there exists a ∈ { 0 , 1 } n such that

$$\left | P r \left [ 1 \leftarrow D i s _ { \epsilon } ^ { N P } ( a , b , x ) \colon x \leftarrow \mathcal { T } \right ] \right ] - P r \left [ 1 \leftarrow D i s _ { \epsilon } ^ { N P } ( a , b , x ) \colon x \leftarrow \mathcal { D } ( a ) \right ] \right ] \right | \leq O p t _ { n } \quad ( 2 2 6 )$$

for all b ∈ { 0 , 1 } n . From the first item of Claim 5.15, this implies that there exists a ∈ { 0 , 1 } n such that

$$\left | \sum _ { i \in [ t ( n ) ] } \frac { \text {Dis} _ { \epsilon } ^ { \text {NP} } ( a , b , x _ { i } ; r _ { i } ( 1 ) ) } { t ( n ) } - \sum _ { i \in [ t ( n ) ] } \frac { \text {Dis} _ { \epsilon } ^ { \text {NP} } ( a , b , X _ { a , r _ { i } ( 2 ) } ; r _ { i } ( 3 ) ) } { t ( n ) } \right | \leq \text {Opt} _ { n } + \frac { 1 } { 8 n \cdot \epsilon ( n ) } \quad ( 2 2 7 )$$

for all b ∈ { 0 , 1 } n . From the construction of A Σ P 3 , for the out 1 ∈ { 0 , 1 } , there exists ( a 2 , ..., a n ) ∈ { 0 , 1 } n -1 such that

$$\text { such that } & & \left | \sum _ { i \in [ t ( n ) ] } \frac { \text {Dis} ^ { N P } ( \text {out} _ { 1 } \| a _ { 2 } \| \dots | a _ { n } , b , x _ { i } ; r _ { i } ( 1 ) ) } { t ( n ) } \\ & & - \sum _ { i \in [ t ( n ) ] } \frac { \text {Dis} ^ { N P } ( \text {out} _ { 1 } \| a _ { 2 } \| \dots | a _ { n } , b , X _ { \text {out} _ { 1 } \| a _ { 2 } \| \dots | a _ { n } , r _ { i } ( 2 ) ; r _ { i } ( 3 ) ) } { t ( n ) } \right | \leq \text {Opt} _ { n } + \frac { 3 } { 8 n \cdot \epsilon ( n ) } \quad ( 2 2 9 ) \\ \text {for all } & \subset ( 0 1 ) ^ { n } \sum \text {from the second item of Clime 5.15. this implies that } & \text {out} \ \text {the} \ \text {out} \ \text {the} \ \text {out} \ \text {is} \\$$

for all b ∈ { 0 , 1 } n . From the second item of Claim 5.15, this implies that, for such out 1 , there exists ( a 2 , ..., a n ) ∈ { 0 , 1 } n -1 such that Equation (224) holds for all b ∈ { 0 , 1 } n .

For induction, suppose that for the ( out 1 , ..., out I ) ∈ { 0 , 1 } I , there exists ( a I +1 , ..., a n ) ∈ { 0 , 1 } n -I such that

$$I _ { 1 }$$

$$\left | \Pr \left [ 1 \leftarrow D i s _ { \epsilon } ^ { \text {NP} } ( \text {out} _ { 1 } \dots \text {out} _ { I } / a _ { I + 1 } \dots | a _ { n } , b , x ) \colon x \leftarrow \mathcal { T } \right ] \\ \\ - \Pr \left [ 1 \leftarrow D i s _ { \epsilon } ^ { \text {NP} } ( \text {out} _ { 1 } \dots \text {out} _ { I } / a _ { I + 1 } \dots | \dots | a _ { n } , b , x ) \colon x \leftarrow \mathcal { D } ( \text {out} _ { 1 } \dots \text {out} _ { I } / a _ { I + 1 } \dots | \dots | a _ { n } ) \right ] \right | \leq \text {Opt} _ { n } + \frac { I } { 2 n \cdot \epsilon ( n ) }$$

$$( 2 3 1 )$$

for all b ∈ { 0 , 1 } n . From the first item of Claim 5.15, there exists ( a I +1 , ..., a n ) ∈ { 0 , 1 } n -I such that

$$| \sum _ { i \in [ t ( n ) ] } \frac { \ D i s _ { \epsilon } ^ { N P } ( \text {out} _ { 1 } \| \dots \| _ { t ( n ) } & \| a _ { n } \| _ { \ } a _ { n } , b , x ; r _ { i } ( 1 ) \\ & - \sum _ { i \in [ t ( n ) ] } \frac { \ D i s _ { \epsilon } ^ { N P } ( \text {out} _ { 1 } \| \dots \| _ { \ } o u t _ { 1 } \| _ { A _ { 1 } + 1 } \| \dots \| _ { a _ { n } } , b , x \text {out} _ { 1 } \| \dots \| _ { \ } o u t _ { 1 } \| _ { A _ { 1 } + 1 } \| \dots \| _ { a _ { n } } , r _ { i } ( 2 ) ; r _ { i } ( 3 ) ) } { t ( n ) } | \leq \text {Opt} _ { n } + \frac { 4 I + 1 } { 8 n \cdot \epsilon ( n ) } \\$$

for all b ∈ { 0 , 1 } n . From the construction of A Σ P 3 , for the ( out 1 , ..., out I +1 ) , there exist ( a I +2 , ..., a n ) ∈ { 0 , 1 } n -I -1 such that

$$\left | \sum _ { i \in [ t ( n ) ] } \frac { \ D i s ^ { \text {NP} } ( \text {out} _ { 1 } \| \dots \| \text {out} _ { 1 + 2 } \| \dots \| a _ { n } , b , x _ { i } ; r _ { i } ( 1 ) ) } { t ( n ) } \right | _ { \substack { ( 2 3 4 ) \\ - \sum _ { i \in [ t ( n ) ] } \frac { \ D i s ^ { \text {NP} } ( \text {out} _ { 1 } \| \dots \| \text {out} _ { 1 + 2 } \| \dots \| a _ { n } , b , X _ { \text {out} } \| \dots \| \text {out} _ { 1 } + \| a _ { 2 } \| \dots \| a _ { n } , r _ { i } ( 2 ) ; r _ { i } ( 3 ) ) } } \leq \text {Opt} _ { n } + \frac { 4 I + 3 } { 8 n \cdot \epsilon ( n ) } \\ \intertext { \quad } - \sum _ { i \in [ t ( n ) ] } \frac { \ D i s ^ { \text {NP} } ( \text {out} _ { 1 } \| \dots \| \text {out} _ { 1 + 2 } \| \dots \| a _ { n } , b , X _ { \text {out} } \| \dots \| \text {out} _ { 1 } + \| a _ { 2 } \| \dots \| a _ { n } , r _ { i } ( 2 ) ; r _ { i } ( 3 ) ) } { t ( n ) } \leq \text {Opt} _ { n } + \frac { 4 I + 3 } { 8 n \cdot \epsilon ( n ) } \\$$

for all b ∈ { 0 , 1 } n . From the second item of Claim 5.15, this implies that, for the out 1 , ..., out I +1 , there exists ( a I +2 , ..., a n ) ∈ { 0 , 1 } n -I -1 such that

$$\left | \Pr [ 1 \leftarrow D \text {is} _ { \epsilon } ^ { N P } ( \text {out} _ { 1 } \| \dots \| \text {out} _ { I + 1 } \| _ { A _ { 1 } + 2 } \| \dots \| a _ { n } , b , x ) \colon x \leftarrow \mathcal { T } \right ] \\ - \Pr [ 1 \leftarrow D \text {is} _ { \epsilon } ^ { N P } ( \text {out} _ { 1 } \| \dots \| \text {out} _ { I + 1 } \| _ { A _ { 1 } + 2 } \| \dots \| a _ { n } , b , x ) \colon x \leftarrow \mathcal { D } ( \text {out} _ { 1 } \| \dots \| \text {out} _ { I + 1 } \| _ { A _ { 1 } + 2 } \| \dots \| a _ { n } ) ] \right | \leq \opt _ { N } , + \frac { I + 1 } { 2 n \cdot \epsilon ( n ) } \\$$

for all b ∈ { 0 , 1 } n .

From induction, this implies that, for all { x i , r i (1) , r i (2) , r i (3) } i ∈ [ t ( n )] ∈ Good n , A Σ P 3 (1 n , { x i } i ∈ [ t ( n )] ; { r i (1) , r i (2) , r i (3) } i ∈ [ t ( n )] ) outputs out n := out 1 ‖ ... ‖ out n such that

$$\left | \Pr \left [ 1 \leftarrow D i s _ { \epsilon } ^ { N P } ( { \text {out} } , b , x ) \colon x \leftarrow \mathcal { T } \right ] - \Pr \left [ 1 \leftarrow D i s _ { \epsilon } ^ { N P } ( { \text {out} } , b , x ) \colon x \leftarrow \mathcal { D } ( { \text {out} } ) \right ] \right ] \leq \text {Opt} _ { n } + \frac { 1 } { 2 \epsilon ( n ) }$$

for all b ∈ { 0 , 1 } n . Because we have

$$\Pr \left [ \{ x _ { i } , r _ { i } ( 1 ) , r _ { i } ( 2 ) , r _ { i } ( 3 ) \} _ { i \in [ t ( n ) ] } \in \text {Good} _ { n } \colon \quad \{ x _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow \mathcal { \mathcal { T } } ^ { \otimes t ( n ) } \right ) \\ \{ r _ { i } ( 1 ) , r _ { i } ( 2 ) , r _ { i } ( 3 ) \} _ { i \in [ t ( n ) ] } \leftarrow \{ 0 , 1 \} ^ { p ( n ) } \right ] \geq 1 - 1 / \delta ( n ) ,$$

this completes the proof.

Proof of Claim 5.15. From Hoeffding's inequality, for each fixed ( a, b ) ∈ { 0 , 1 } n ×{ 0 , 1 } n , with probability at least 1 -2 · 2 ( -t ( n ) 32 n 2 · ϵ ( n ) 2 ) over { x i } i ∈ [ t ( n )] ←T ⊗ t ( n ) and { r i (1) , r i (2) , r i (3) } i ∈ [ t ( n )] ←{ 0 , 1 } p ( n ) , where p ( n ) is the size of { r i (1) , r i (2) , r i (3) } i ∈ [ t ( n )] , we have

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Therefore, from union bound, with probability at least 1 -1 /δ ( n ) over { x i } i ∈ [ t ( n )] ← T ⊗ t ( n ) and { r i (1) , r i (2) , r i (3) } i ∈ [ t ( n )] ←{ 0 , 1 } p ( n ) , we have

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

$$- \left ( \Pr \left [ 1 \leftarrow \text {Dis} _ { \epsilon } ^ { \text {NP} } ( a , b , x ) \colon x \leftarrow \mathcal { T } \right ] - \Pr \left [ 1 \leftarrow \text {Dis} _ { \epsilon } ^ { \text {NP} } ( a , b , x ) \colon x \leftarrow \mathcal { D } ( a ) \right ] \right ) \right ] \Big | \leq \frac { 1 } { 8 n \cdot \epsilon ( n ) } \quad ( 2 4 3 )$$

for all ( a, b ) ∈ { 0 , 1 } n ×{ 0 , 1 } n . Let Good n be a set of { x i , r i (1) , r i (2) , r i (3) } i ∈ [ t ( n )] such that Equation (243) holds for all ( a, b ) ∈ { 0 , 1 } n ×{ 0 , 1 } n . From Equation (243), for all { x i , r i (1) , r i (2) , r i (3) } i ∈ [ t ( n )] ∈ Good n and for all I ∈ [ n ] , if there exists a ∈ { 0 , 1 } n such that, for all b ∈ { 0 , 1 } n ,

$$\left | \Pr \left [ 1 \leftarrow \text {Dis} _ { \epsilon } ^ { \text {NP} } ( a , b , x ) \colon x \leftarrow \mathcal { T } \right ] - \Pr \left [ 1 \leftarrow \text {Dis} _ { \epsilon } ^ { \text {NP} } ( a , b , x ) \colon x \leftarrow \mathcal { D } ( a ) \right ] \right | \leq \text {Opt} _ { n } + \frac { I - 1 } { 2 n \cdot \epsilon ( n ) } , \ \ ( 2 4 4 )$$

then there exists a ∈ { 0 , 1 } n such that, for all b ∈ { 0 , 1 } n ,

$$\left | \sum _ { i \in [ t ( n ) ] } \frac { \text {Dis} _ { \epsilon } ^ { \text {NP} } ( a , b , x _ { i } ; r _ { i } ( 1 ) ) } { t ( n ) } - \sum _ { i \in [ t ( n ) ] } \frac { \text {Dis} _ { \epsilon } ^ { \text {NP} } ( a , b , X _ { a , r _ { i } ( 2 ) } ; r _ { i } ( 3 ) ) } { t ( n ) } \right | \leq \text {Opt} _ { n } + \frac { ( 4 I - 1 ) } { 8 n \cdot \epsilon ( n ) } .$$

From Equation (243), for all { x i , r i (1) , r i (2) , r i (3) } i ∈ [ t ( n )] ∈ Good n , and for all I ∈ [ n ] , if for all a ∈ { 0 , 1 } n , there exists b ∈ { 0 , 1 } n such that

$$\left | \Pr \left [ 1 \leftarrow \text {Dis} _ { \epsilon } ^ { \text {NP} } ( a , b , x ) \colon x \leftarrow \mathcal { T } \right ] - \Pr \left [ 1 \leftarrow \text {Dis} _ { \epsilon } ^ { \text {NP} } ( a , b , x ) \colon x \leftarrow \mathcal { D } ( a ) \right ] \right | \geq \text {Opt} _ { n } + \frac { I } { 2 n \cdot \epsilon ( n ) } , \ \ ( 2 4 6 )$$

then for all a ∈ { 0 , 1 } n , there exists b ∈ { 0 , 1 } n such that

$$\left | \sum _ { i \in [ t ( n ) ] } \frac { \text {Dis} _ { \epsilon } ^ { \text {NP} } ( a , b , x _ { i } ; r _ { i } ( 1 ) ) } { t ( n ) } - \sum _ { i \in [ t ( n ) ] } \frac { \text {Dis} _ { \epsilon } ^ { \text {NP} } ( a , b , X _ { a , r _ { i } ( 2 ) } ; r _ { i } ( 3 ) ) } { t ( n ) } \right | \geq \text {Opt} _ { n } + \frac { ( 4 I - 1 ) } { 8 n \cdot \epsilon ( n ) } .$$

This completes the proof.

Proof of Theorem 5.13 In the following, we give a proof of Theorem 5.13.

Proof of Theorem 5.13. In the following, we often omit 1 n of D (1 n , a ) , and Estimate ϵ (1 n , a, x ) .

Let ϵ be an arbitrary polynomial. Let Estimate NP ϵ be a PPT algorithm with access to an NP oracle given in Theorem 2.3 such that

$$\Pr \left [ \left ( 1 - \frac { 1 } { \epsilon ( n ) } \right ) \Pr [ x \leftarrow \mathcal { D } ( z ) ] \leq \text {Estimate} _ { \epsilon } ^ { \text {NP} } ( z , x ) \leq \left ( 1 + \frac { 1 } { \epsilon ( n ) } \right ) \Pr [ x \leftarrow \mathcal { D } ( z ) ] \right ] \geq 1 - \frac { 1 } { \epsilon ( n ) } \ \ ( 2 4 8 )$$

for all ( x, z ) ∈ { 0 , 1 } n ×{ 0 , 1 } n , where the probability is taken over the internal randomness of Estimate NP ϵ . From Estimate NP ϵ , we construct Dis NP ϵ as follows:

Dis NP ϵ ( ℓ, m, x ) :

$$1 . \text { Run } E _ { \ell } \leftarrow \text {Estimate} _ { 5 0 0 \epsilon } ^ { \text {NP} } ( \ell , x ) \text { and } E _ { m } \leftarrow \text {Estimate} _ { 5 0 0 \epsilon } ^ { \text {NP} } ( m , x ) .$$

2.

Output

1

if

E

ℓ

≥

(1 +

16

1

ϵ

(

n

)

)

E

m

. Otherwise, output

We will show that, when SD ( D ( ℓ ) , D ( m )) ≥ 1 ϵ ( n ) , we have

$$& \quad \text {SD} ( \mathcal { D } ( \ell ) , \mathcal { D } ( m ) ) \\ & \quad \leq \left ( 1 + \frac { 1 } { 4 \epsilon ( n ) } \right ) \left | \Pr \left [ 1 \leftarrow \text {Dis} _ { \epsilon } ^ { \text {NP} } ( \ell , m , x ) \colon x \leftarrow \mathcal { D } ( \ell ) \right ] - \Pr \left [ 1 \leftarrow \text {Dis} _ { \epsilon } ^ { \text {NP} } ( \ell , m , x ) \colon x \leftarrow \mathcal { D } ( m ) \right ] \right ] + \frac { 1 } { 4 \epsilon ( n ) } .$$

For showing this, let us define

$$\mathcal { S } _ { n } \coloneqq \left \{ x \in \{ 0 , 1 \} ^ { \text {poly} ( n ) } \colon \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , \ell ) ] \geq \left ( 1 + \frac { 1 } { 8 \epsilon ( n ) } \right ) \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , m ) ] \right \}$$

$$\mathcal { T } _ { n } \coloneqq \begin{cases} x \in \{ 0 , 1 \} ^ { \text {poly} ( n ) } \colon \left ( 1 + \frac { 1 } { 8 \epsilon ( n ) } \right ) \cdot \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , m ) ] > \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , \ell ) ] \geq \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , m ) ] \right ] \right \} \\ \end{cases}$$

$$\mathcal { U } _ { n } \coloneqq \{ x \in \{ 0 , 1 \} ^ { \text {poly} ( n ) } \colon \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , m ) ] > \Pr [ x \leftarrow \mathcal { D } ( 1 ^ { n } , \ell ) ] \} .$$

We use the following Claims 5.16 to 5.18, which we prove later.

Claim 5.16. For all x ∈ S n , we have

$$\Pr \left [ 1 \leftarrow D i s { \mathbf \Psi } ^ { \text {NP} } ( \ell , m , x ) \right ] \geq 1 - \frac { 1 } { 2 5 0 \epsilon ( n ) } .$$

Claim 5.17. For all x ∈ U n , we have

$$\Pr \left [ 1 \leftarrow D i s _ { \epsilon } ^ { \text {NP} } ( \ell , m , x ) \right ] \leq \frac { 1 } { 2 5 0 \epsilon ( n ) } .$$

Claim 5.18. For all D ( ℓ ) and D ( m ) such that SD ( D ( ℓ ) , D ( m )) ≥ 1 ϵ ( n ) we have

$$\sum _ { x \in \mathcal { S } _ { n } } \Pr [ x \leftarrow \mathcal { D } ( \ell ) ] - \Pr [ x \leftarrow \mathcal { D } ( m ) ] \geq \mathbb { S } D ( \mathcal { D } ( \ell ) , \mathcal { D } ( m ) ) - \frac { 1 } { 8 \epsilon ( n ) } .$$

0

.

From Claims 5.16 to 5.18, we have

$$\Pr { \left [ 1 \leftarrow \text {Dis} _ { \epsilon } ^ { \text {NP} } ( \ell , m , x ) \colon x \leftarrow \mathcal { D } ( \ell ) \right ] } - \Pr { \left [ 1 \leftarrow \text {Dis} _ { \epsilon } ^ { \text {NP} } ( \ell , m , x ) \colon x \leftarrow \mathcal { D } ( m ) \right ] }$$

$$= \sum _ { x \in \mathcal { S } _ { n } } ( \Pr [ x \leftarrow \mathcal { D } ( \ell ) ] - \Pr [ x \leftarrow \mathcal { D } ( m ) ] ) \cdot \Pr \left [ 1 \leftarrow \text {Dis} _ { \epsilon } ^ { \text {NP} } ( \ell , m , x ) \right ] \\$$

$$+ \sum _ { x \in \mathcal { T } _ { n } } ( \Pr [ x \leftarrow \mathcal { D } ( \ell ) ] - \Pr [ x \leftarrow \mathcal { D } ( m ) ] ) \cdot \Pr \left [ 1 \leftarrow \text {Dis} _ { \epsilon } ^ { N P } ( \ell , m , x ) \right ]$$

$$+ \sum _ { x \in \mathcal { U } _ { n } } ( \Pr [ x \leftarrow \mathcal { D } ( \ell ) ] - \Pr [ x \leftarrow \mathcal { D } ( m ) ] ) \cdot \Pr \left [ 1 \leftarrow \text {Dis} _ { \epsilon } ^ { N P } ( \ell , m , x ) \right ]$$

$$\geq \sum _ { x \in \mathcal { S } _ { n } } ( \Pr [ x \leftarrow \mathcal { D } ( \ell ) ] - \Pr [ x \leftarrow \mathcal { D } ( m ) ] ) \cdot \Pr \left [ 1 \leftarrow \text {Dis} _ { \epsilon } ^ { \text {NP} } ( \ell , m , x ) \right ]$$

$$+ \sum _ { x \in \mathcal { U } _ { n } } ( \Pr [ x \leftarrow \mathcal { D } ( \ell ) ] - \Pr [ x \leftarrow \mathcal { D } ( m ) ] ) \cdot \Pr \left [ 1 \leftarrow \text {Dis} _ { \epsilon } ^ { N P } ( \ell , m , x ) \right ]$$

$$\geq \sum _ { x \in \mathcal { S } _ { n } } ( \Pr [ x \leftarrow \mathcal { D } ( \ell ) ] - \Pr [ x \leftarrow \mathcal { D } ( m ) ] ) \cdot \left ( 1 - \frac { 1 } { 2 5 0 \epsilon ( n ) } \right )$$

$$+ \sum _ { x \in \mathcal { U } _ { n } } ( \Pr [ x \leftarrow \mathcal { D } ( \ell ) ] - \Pr [ x \leftarrow \mathcal { D } ( m ) ] ) \cdot \Pr \left [ 1 \leftarrow \text {Dis} _ { \epsilon } ^ { N P } ( \ell , m , x ) \right ]$$

$$& \geq \sum _ { x \in \mathcal { S } _ { n } } \left ( \Pr [ x \leftarrow \mathcal { D } ( \ell ) ] - \Pr [ x \leftarrow \mathcal { D } ( m ) ] \right ) \cdot \left ( 1 - \frac { 1 } { 2 5 0 \epsilon ( n ) } \right ) - \sum _ { x \in \mathcal { U } _ { n } } \Pr [ x \leftarrow \mathcal { D } ( m ) ] \cdot \Pr \left [ 1 \leftarrow \text {Dis} _ { \epsilon } ^ { \text {NP} } ( \ell , m , x ) \right ] \right ] \\$$

$$& \geq \sum _ { x \in \mathcal { S } _ { n } } \left ( \Pr [ x \leftarrow \mathcal { D } ( \ell ) \right ] - \Pr [ x \leftarrow \mathcal { D } ( m ) ] \right ) \cdot \left ( 1 - \frac { 1 } { 2 5 0 \epsilon ( n ) } \right ) - \frac { 1 } { 2 5 0 \epsilon ( n ) } \\$$

$$\geq & \left ( \text {SD} ( \mathcal { D } ( \ell ) , \mathcal { D } ( m ) ) - \frac { 1 } { 8 \epsilon ( n ) } \right ) \left ( 1 - \frac { 1 } { 2 5 0 \epsilon ( n ) } \right ) - \frac { 1 } { 2 5 0 \epsilon ( n ) } .$$

Here, in Equation (261), we have used that Pr[ x ←D ( ℓ )] -Pr[ x ←D ( m )] ≥ 0 for all x ∈ T n , in Equation (263), we have used Claim 5.16, and in Equation (266), we have used Claim 5.17, and in Equation (267), we have used Claim 5.18. This implies that

$$& \quad \text {SD} ( \mathcal { D } ( \ell ) , \mathcal { D } ( m ) ) \\ & \quad \leq \left ( 1 + \frac { 1 } { 4 \epsilon ( n ) } \right ) \left | \Pr \left [ 1 \leftarrow \text {Dis} _ { \epsilon } ^ { \text {NP} } ( \ell , m , x ) \colon x \leftarrow \mathcal { D } ( \ell ) \right ] - \Pr \left [ 1 \leftarrow \text {Dis} _ { \epsilon } ^ { \text {NP} } ( \ell , m , x ) \colon x \leftarrow \mathcal { D } ( m ) \right ] \right ] + \frac { 1 } { 4 \epsilon ( n ) } .$$

Proof of Claim 5.16. In the Dis NP ϵ ( ℓ, m, x ) algorithm, it runs Estimate NP 500 ϵ ( ℓ, x ) and Estimate NP 500 ϵ ( m,x ) . From union bound, with probability at least 1 -1 250 ϵ ( n ) over the internal randomness of Estimate NP 500 ϵ ( ℓ, x ) and Estimate NP 500 ϵ ( m,x ) , we have

$$\left ( 1 + \frac { 1 } { 5 0 0 \epsilon ( n ) } \right ) \Pr [ x \leftarrow \mathcal { D } ( \ell ) ] \geq \text {Estimate} _ { 5 0 0 \epsilon } ^ { \text {NP} } ( \ell , x ) \geq \left ( 1 - \frac { 1 } { 5 0 0 \epsilon ( n ) } \right ) \Pr [ x \leftarrow \mathcal { D } ( \ell ) ] \quad ( 2 7 0 )$$

and

$$\left ( 1 + \frac { 1 } { 5 0 0 \epsilon ( n ) } \right ) \Pr [ x \leftarrow \mathcal { D } ( m ) ] \geq \text {Estimate} _ { 5 0 0 \epsilon } ^ { \text {NP} } ( m , x ) \geq \left ( 1 - \frac { 1 } { 5 0 0 \epsilon ( n ) } \right ) \Pr [ x \leftarrow \mathcal { D } ( m ) ] .$$

From the definition of S n , for all x ∈ S n , we have

$$& \text {Estimate} _ { 5 0 0 \epsilon } ^ { \text {NP} } ( \ell , x ) \geq \left ( 1 - \frac { 1 } { 5 0 0 \epsilon ( n ) } \right ) \left ( 1 + \frac { 1 } { 8 \epsilon ( n ) } \right ) \text {Pr} [ x \leftarrow \mathcal { D } ( m ) ] \\ & \geq \frac { 5 0 \epsilon ( n ) - 1 } { 5 0 \epsilon ( n ) + 1 } \left ( 1 + \frac { 1 } { 8 \epsilon ( n ) } \right ) \text {Estimate} _ { 5 0 0 \epsilon } ^ { \text {NP} } ( m , x ) \geq \left ( 1 + \frac { 1 } { 1 6 \epsilon ( n ) } \right ) \text {Estimate} _ { 5 0 0 \epsilon } ^ { \text {NP} } ( m , x ) .$$

This completes the proof.

Proof of Claim 5.17. In the Dis NP ϵ ( ℓ, m, x ) algorithm, it runs Estimate NP 500 ϵ ( ℓ, x ) and Estimate NP 500 ϵ ( m,x ) . From union bound, with probability at least 1 -1 250 ϵ ( n ) over the internal randomness of Estimate NP 500 ϵ ( ℓ, x ) and Estimate NP 500 ϵ ( m,x ) , we have

$$\left ( 1 + \frac { 1 } { 5 0 0 \epsilon ( n ) } \right ) \Pr [ x \leftarrow \mathcal { D } ( \ell ) ] \geq \text {Estimate} _ { 5 0 0 \epsilon } ^ { \text {NP} } ( \ell , x ) \geq \left ( 1 - \frac { 1 } { 5 0 0 \epsilon ( n ) } \right ) \Pr [ x \leftarrow \mathcal { D } ( \ell ) ] \quad ( 2 7 4 )$$

and

$$\left ( 1 + \frac { 1 } { 5 0 0 \epsilon ( n ) } \right ) \Pr [ x \leftarrow \mathcal { D } ( m ) ] \geq \text {Estimate} _ { 5 0 0 \epsilon } ^ { \text {NP} } ( m , x ) \geq \left ( 1 - \frac { 1 } { 5 0 0 \epsilon ( n ) } \right ) \Pr [ x \leftarrow \mathcal { D } ( m ) ] .$$

From the definition of U n , for all x ∈ U n , we have

$$& \text {Estimate} _ { 5 0 0 \epsilon } ^ { \text {NP} } ( n , x ) \geq \left ( 1 - \frac { 1 } { 5 0 0 \epsilon ( n ) } \right ) \Pr [ x \leftarrow \mathcal { D } ( n ) ] > \left ( 1 - \frac { 1 } { 5 0 0 \epsilon ( n ) } \right ) \Pr [ x \leftarrow 1 \mathcal { D } ( \ell ) ] \\ & \geq \left ( \frac { 5 0 0 \epsilon ( n ) - 1 } { 5 0 0 \epsilon ( n ) + 1 } \right ) \text {Estimate} _ { 5 0 0 \epsilon \left ( \ell , x \right ) } ^ { \text {NP} } ( \ell , x ) .$$

This implies that

$$\left ( 1 + \frac { 1 } { 1 6 \epsilon ( n ) } \right ) \text {Estimate} _ { 5 0 0 \epsilon } ^ { \text {NP} } ( m , x ) > \text {Estimate} _ { 5 0 0 \epsilon } ^ { \text {NP} } ( \ell , x ) .$$

Therefore, the probability is at most 1 250 ϵ ( n ) that the following event occurs

$$E \text {estimate} _ { 5 0 0 \epsilon } ^ { N P } ( \ell , x ) \geq \left ( 1 + \frac { 1 } { 1 6 \epsilon ( n ) } \right ) \text {Estimate} _ { 5 0 0 \epsilon } ^ { N P } ( m , x ) .$$

Proof of Claim 5.18. We have

$$\S D ( \mathcal { D } ( m ) , \mathcal { D } ( \ell ) )$$

$$3 D ( D ( m ) , D ( \ell ) ) \\ & = \sum _ { x \in S _ { n } } ( \Pr [ x \leftarrow \mathcal { D } ( \ell ) ] - \Pr [ x \leftarrow \mathcal { D } ( m ) ] ) + \sum _ { x \in \mathcal { T } _ { n } } \left ( \Pr [ x \leftarrow \mathcal { D } ( \ell ) ] - \Pr [ x \leftarrow \mathcal { D } ( m ) ] \right ) \right ) \\ & < \sum _ { x \in S _ { n } } ( \Pr [ x \leftarrow \mathcal { D } ( \ell ) ] - \Pr [ x \leftarrow \mathcal { D } ( m ) ] ) + \frac { 1 } { 8 \epsilon ( n ) } \sum _ { x \in \mathcal { T } _ { n } } \Pr [ x \leftarrow \mathcal { D } ( m ) ] \\ & \leq \sum _ { x \in S } ( \Pr [ x \leftarrow \mathcal { D } ( \ell ) ] - \Pr [ x \leftarrow \mathcal { D } ( m ) ] ) + \frac { 1 } { 8 \epsilon ( n ) }$$

$$\leq \sum _ { x \in S _ { n } } ( \Pr [ x \leftarrow \mathcal { D } ( \ell ) ] - \Pr [ x \leftarrow \mathcal { D } ( m ) ] ) + \frac { 1 } { 8 \epsilon ( n ) }$$

Hence, we have

$$\sum _ { x \in \mathcal { S } _ { n } } \Pr [ x \leftarrow \mathcal { D } ( \ell ) ] - \Pr [ x \leftarrow \mathcal { D } ( m ) ] \geq \mathbb { S } D ( \mathcal { D } ( \ell ) , \mathcal { D } ( m ) ) - \frac { 1 } { 8 \epsilon ( n ) } .$$

Acknowledgements. TM is supported by JST CREST JPMJCR23I3, JST Moonshot R &amp; D JPMJMS2061-51-1, JST FOREST, MEXT QLEAP, the Grant-in Aid for Transformative Research Areas (A) 21H05183, and the Grant-in-Aid for Scientific Research (A) No.22H00522.

## References

- [AA11] Scott Aaronson and Alex Arkhipov. The computational complexity of linear optics. In Lance Fortnow and Salil P. Vadhan, editors, 43rd ACM STOC , pages 333-342. ACM Press, June 2011. (Cited on page 1, 4, 7, 13.)
- [Aar05] Scott Aaronson. Quantum computing, postselection, and probabilistic polynomial-time. Proceedings of the Royal Society A: Mathematical, Physical and Engineering Sciences , 461(2063):34733482, 2005. Published online 5 September 2005; Received 23 December 2004; Accepted 4 July 2005. (Cited on page 12.)
- [Aar14] Scott Aaronson. The equivalence of sampling and searching. Theor. Comp. Sys. , 55(2):281-298, August 2014. (Cited on page 13.)
- [ABK24] Scott Aaronson, Harry Buhrman, and William Kretschmer. A Qubit, a Coin, and an Advice String Walk into a Relational Problem. In Venkatesan Guruswami, editor, 15th Innovations in Theoretical Computer Science Conference (ITCS 2024) , volume 287 of Leibniz International Proceedings in Informatics (LIPIcs) , pages 1:1-1:24, Dagstuhl, Germany, 2024. Schloss Dagstuhl - Leibniz-Zentrum für Informatik. (Cited on page 13.)
- [ABX08] Benny Applebaum, Boaz Barak, and David Xiao. On basing lower-bounds for learning on worst-case assumptions. In 2008 49th Annual IEEE Symposium on Foundations of Computer Science , pages 211-220, 2008. (Cited on page 2.)
- [AC17] Scott Aaronson and Lijie Chen. Complexity-theoretic foundations of quantum supremacy experiments. CCC'17: Proceedings of the 32nd Computational Complexity Conference, 2017. (Cited on page 3.)
- [AQY22] Prabhanjan Ananth, Luowen Qian, and Henry Yuen. Cryptography from pseudorandom quantum states. In Yevgeniy Dodis and Thomas Shrimpton, editors, CRYPTO 2022, Part I , volume 13507 of LNCS , pages 208-236. Springer, Cham, August 2022. (Cited on page 1.)
- [AW92] Naoki Abe and Manfred K Warmuth. On the computational complexity of approximating distributions by probabilistic automata. Machine Learning , 9, 1992. (Cited on page 2, 3, 6, 28, 35.)

- [BCKM21] James Bartusek, Andrea Coladangelo, Dakshita Khurana, and Fermi Ma. One-way functions imply secure computation in a quantum world. In Tal Malkin and Chris Peikert, editors, CRYPTO 2021, Part I , volume 12825 of LNCS , pages 467-496, Virtual Event, August 2021. Springer, Cham. (Cited on page 1.)
- [BCQ23] Zvika Brakerski, Ran Canetti, and Luowen Qian. On the computational hardness needed for quantum cryptography. In Yael Tauman Kalai, editor, 14th Innovations in Theoretical Computer Science Conference, ITCS 2023, January 10-13, 2023, MIT, Cambridge, Massachusetts, USA , volume 251 of LIPIcs , pages 24:1-24:21. Schloss Dagstuhl - Leibniz-Zentrum für Informatik, 2023. (Cited on page 1.)
- [BFKL94] Avrim Blum, Merrick L. Furst, Michael J. Kearns, and Richard J. Lipton. Cryptographic primitives based on hard learning problems. In Douglas R. Stinson, editor, CRYPTO'93 , volume 773 of LNCS , pages 278-291. Springer, Berlin, Heidelberg, August 1994. (Cited on page 1, 2, 3, 4.)
- [BFNV19] Adam Bouland, Bill Fefferman, Chinmay Nirkhe, and Umesh Vazirani. On the complexity and verification of quantum random circuit sampling. Nature Physics , 15:159-163, 2019. (Cited on page 1, 4.)
- [BHHP24] John Bostanci, Jonas Haferkamp, Dominik Hangleiter, and Alexander Poremba. Efficient quantum pseudorandomness from hamiltonian phase states, 2024. (Cited on page 6.)
- [BJS11] Michael J. Bremner, Richard Jozsa, and Dan J. Shepherd. Classical simulation of commuting quantum computations implies collapse of the polynomial hierarchy. Proceedings of the Royal Society A: Mathematical, Physical and Engineering Sciences , 467:459-472, 2011. (Cited on page 4.)
- [BKM19] Olivier Bousquet, Daniel Kane, and Shay Moran. The optimal approximation factor in density estimation. In Alina Beygelzimer and Daniel Hsu, editors, Proceedings of the Thirty-Second Conference on Learning Theory , volume 99 of Proceedings of Machine Learning Research , pages 318-341. PMLR, 25-28 Jun 2019. (Cited on page 36.)
- [BKM20] Olivier Bousquet, Daniel Kane, and Shay Moran. The optimal approximation factor in density estimation, 2020. (Cited on page 2, 3.)
- [BMS16] Michael J. Bremner, Ashley Montanaro, and Dan J. Shepherd. Average-case complexity versus approximate simulation of commuting quantum computations. Physical Review Letters , 117:080501, 2016. (Cited on page 1, 4, 13.)
- [CGG + 23] Bruno Cavalar, Eli Goldin, Matthew Gray, Peter Hall, Yanyi Liu, and Angelos Pelecanos. On the computational hardness of quantum one-wayness, 2023. (Cited on page 1, 2, 7.)
- [CGG24] Kai-Min Chung, Eli Goldin, and Matthew Gray. On central primitives for quantum cryptography with classical communication. In Leonid Reyzin and Douglas Stebila, editors, CRYPTO 2024, Part VII , volume 14926 of LNCS , pages 215-248. Springer, Cham, August 2024. (Cited on page 8, 14, 15, 57.)

- [CGGH25] Bruno Pasqualotto Cavalar, Eli Goldin, Matthew Gray, and Peter Hall. A meta-complexity characterization of quantum cryptography. LNCS, pages 82-107. Springer, Cham, June 2025. (Cited on page 8.)
- [DH76] Whitfield Diffie and Martin E. Hellman. New directions in cryptography. IEEE Transactions on Information Theory , 22(6):644-654, 1976. (Cited on page 1.)
- [DKK + 19] Ilias Diakonikolas, Gautam Kamath, Daniel Kane, Jerry Li, Ankur Moitra, and Alistair Stewart. Robust estimators in high dimensions without the computational intractability, 2019. (Cited on page 2, 3.)
- [DL01] Luc Devroye and Gábor Lugosi. Combinatorial Methods in Density Estimation . Springer Nature, 2001. (Cited on page 2, 3.)
- [FGSY25] Bill Fefferman, Soumik Ghosh, Makrand Sinha, and Henry Yuen. The hardness of learning quantum circuits and its cryptographic applications, 2025. (Cited on page 6.)
- [FKM + 18] Keisuke Fujii, Hirotada Kobayashi, Tomoyuki Morimae, Harumichi Nishimura, Seiichiro Tani, and Shuhei Tamate. Impossibility of classically simulating one-clean-qubit model with multiplicative error. Physical Review Letters , 120:200502, 2018. (Cited on page 4.)
- [FR99] Lance Fortnow and John Rogers. Complexity limitations on quantum computation. Journal of Computer and System Sciences , 59(2):240-252, 1999. (Cited on page 2, 55.)
- [GGM84] Oded Goldreich, Shafi Goldwasser, and Silvio Micali. On the cryptographic applications of random functions. In G. R. Blakley and David Chaum, editors, CRYPTO'84 , volume 196 of LNCS , pages 276-288. Springer, Berlin, Heidelberg, August 1984. (Cited on page 1.)
- [GGM86] Oded Goldreich, Shafi Goldwasser, and Silvio Micali. How to construct random functions. Journal of the ACM , 33(4):792-807, 1986. (Cited on page 1.)
- [GK23] Halley Goldberg and Valentine Kabanets. Improved learning from kolmogorov complexity. In Proceedings of the 38th Computational Complexity Conference , CCC '23, Dagstuhl, DEU, 2023. Schloss Dagstuhl-Leibniz-Zentrum fuer Informatik. (Cited on page 1.)
- [GKLO22] Halley Goldberg, Valentine Kabanets, Zhenjian Lu, and Igor C. Oliveira. Probabilistic kolmogorov complexity with applications to average-case complexity. CCC '22, Dagstuhl, DEU, 2022. Schloss Dagstuhl-Leibniz-Zentrum fuer Informatik. (Cited on page 1.)
- [GLSV21] Alex B. Grilo, Huijia Lin, Fang Song, and Vinod Vaikuntanathan. Oblivious transfer is in MiniQCrypt. In Anne Canteaut and François-Xavier Standaert, editors, EUROCRYPT 2021, Part II , volume 12697 of LNCS , pages 531-561. Springer, Cham, October 2021. (Cited on page 1.)
- [GM84] Shafi Goldwasser and Silvio Micali. Probabilistic encryption. J. Comput. Syst. Sci. , 28:270-299, 1984. (Cited on page 1.)
- [HH24] Taiga Hiroka and Min-Hsiu Hsieh. Computational complexity of learning efficiently generatable pure states, 2024. (Cited on page 6, 9, 29, 36.)

- [HIL + 23] Shuichi Hirahara, Rahul Ilango, Zhenjian Lu, Mikito Nanashima, and Igor C. Oliveira. A duality between one-way functions and average-case symmetry of information. In Barna Saha and Rocco A. Servedio, editors, 55th ACM STOC , pages 1039-1050. ACM Press, June 2023. (Cited on page 2.)
- [HILL99] Johan Håstad, Russell Impagliazzo, Leonid A. Levin, and Michael Luby. A pseudorandom generator from any one-way function. SIAM Journal on Computing , 28(4):1364-1396, 1999. (Cited on page 1.)
- [HIN + 23] M. Hinsche, M. Ioannou, A. Nietner, J. Haferkamp, Y. Quek, D. Hangleiter, J.-P. Seifert, J. Eisert, and R. Sweke. One T gate makes distribution learning hard. Physical Review Letters , 130(24), June 2023. (Cited on page 6.)
- [Hir18] Shuichi Hirahara. Non-black-box worst-case to average-case reductions within NP. In Mikkel Thorup, editor, 59th FOCS , pages 247-258. IEEE Computer Society Press, October 2018. (Cited on page 2.)
- [Hir23] Shuichi Hirahara. Capturing one-way functions via NP-hardness of meta-complexity. In Barna Saha and Rocco A. Servedio, editors, 55th ACM STOC , pages 1027-1038. ACM Press, June 2023. (Cited on page 2.)
- [HM24] Taiga Hiroka and Tomoyuki Morimae. Quantum cryptography and meta-complexity. arXiv:2410.01369, 2024. (Cited on page 8, 57.)
- [HN22] Shuichi Hirahara and Mikito Nanashima. On worst-case learning in relativized heuristica. In 62nd FOCS , pages 751-758. IEEE Computer Society Press, February 2022. (Cited on page 1.)
- [HN23] Shuichi Hirahara and Mikito Nanashima. Learning in pessiland via inductive inference. In 64th FOCS , pages 447-457. IEEE Computer Society Press, November 2023. (Cited on page 1, 2, 3, 5, 6, 15, 27, 28.)
- [IL89] Russell Impagliazzo and Michael Luby. One-way functions are essential for complexity based cryptography (extended abstract). In 30th FOCS , pages 230-235. IEEE Computer Society Press, October / November 1989. (Cited on page 1.)
- [IL90] Russell Impagliazzo and Leonid A. Levin. No better ways to generate hard NP instances than picking uniformly at random. In 31st FOCS , pages 812-821. IEEE Computer Society Press, October 1990. (Cited on page 1.)
- [IRS21] Rahul Ilango, Hanlin Ren, and Rahul Santhanam. Hardness on any samplable distribution suffices: New characterizations of one-way functions by meta-complexity. Electron. Colloquium Comput. Complex. , TR21-082, 2021. (Cited on page 2.)
- [JLS18] Zhengfeng Ji, Yi-Kai Liu, and Fang Song. Pseudorandom quantum states. In Hovav Shacham and Alexandra Boldyreva, editors, CRYPTO 2018, Part III , volume 10993 of LNCS , pages 126-152. Springer, Cham, August 2018. (Cited on page 1.)
- [KMR + 94] Michael J. Kearns, Yishay Mansour, Dana Ron, Ronitt Rubinfeld, Robert E. Schapire, and Linda Sellie. On the learnability of discrete distributions. In 26th ACM STOC , pages 273-282. ACM Press, May 1994. (Cited on page 2, 3, 15, 27, 28, 36.)

- [Ko91] Ker-I Ko. On the complexity of learning minimum time-bounded turing machines. SIAM Journal on Computing , 20(5):962-986, 1991. (Cited on page 1.)
- [KQST23] William Kretschmer, Luowen Qian, Makrand Sinha, and Avishay Tal. Quantum cryptography in algorithmica. In Barna Saha and Rocco A. Servedio, editors, 55th ACM STOC , pages 1589-1602. ACM Press, June 2023. (Cited on page 1.)
- [KQT24] William Kretschmer, Luowen Qian, and Avishay Tal. Quantum-computable one-way functions without one-way functions. arXiv:2411.02554, 2024. (Cited on page 1.)
- [Kre21] William Kretschmer. Quantum Pseudorandomness and Classical Complexity. In Min-Hsiu Hsieh, editor, 16th Conference on the Theory of Quantum Computation, Communication and Cryptography (TQC 2021) , volume 197 of Leibniz International Proceedings in Informatics (LIPIcs) , pages 2:1-2:20, Dagstuhl, Germany, 2021. Schloss Dagstuhl - Leibniz-Zentrum für Informatik. (Cited on page 1, 2.)
- [KT24] Dakshita Khurana and Kabir Tomer. Commitments from quantum one-wayness. In Bojan Mohar, Igor Shinkar, and Ryan O'Donnell, editors, 56th ACM STOC , pages 968-978. ACM Press, June 2024. (Cited on page 1, 8, 14, 15.)
- [KT25] Dakshita Khurana and Kabir Tomer. Founding quantum cryptography on quantum advantage, or, towards cryptography from #P hardness. In Proceedings of the 57th Annual ACM Symposium on Theory of Computing , STOC '25, page 178-188, New York, NY, USA, 2025. Association for Computing Machinery. (Cited on page 1, 6, 7, 8, 13, 57.)
- [LMW24] Alex Lombardi, Fermi Ma, and John Wright. A one-query lower bound for unitary synthesis and breaking quantum cryptography. In Bojan Mohar, Igor Shinkar, and Ryan O'Donnell, editors, 56th ACM STOC , pages 979-990. ACM Press, June 2024. (Cited on page 1.)
- [LP20] Yanyi Liu and Rafael Pass. On one-way functions and kolmogorov complexity. In 61st FOCS , pages 1243-1254. IEEE Computer Society Press, November 2020. (Cited on page 2.)

̸

- [LP21] Yanyi Liu and Rafael Pass. On the possibility of basing cryptography on EXP = BPP . In Tal Malkin and Chris Peikert, editors, CRYPTO 2021, Part I , volume 12825 of LNCS , pages 11-40, Virtual Event, August 2021. Springer, Cham. (Cited on page 2.)
- [LP23] Yanyi Liu and Rafael Pass. One-way functions and the hardness of (probabilistic) timebounded Kolmogorov complexity w.r.t. samplable distributions. In Helena Handschuh and Anna Lysyanskaya, editors, CRYPTO 2023, Part II , volume 14082 of LNCS , pages 645-673. Springer, Cham, August 2023. (Cited on page 2.)
- [Mor17] Tomoyuki Morimae. Hardness of classically sampling the one-clean-qubit model with constant total variation distance error. Phys. Rev. A , 96:040302, Oct 2017. (Cited on page 4.)
- [Mov23] Ramis Movassagh. The hardness of random quantum circuits. Nature Physics , 19:1719-1724, 2023. (Cited on page 1, 4.)
- [MSY25] Tomoyuki Morimae, Yuki Shirakawa, and Takashi Yamakawa. Cryptographic characterization of quantum advantage. In Proceedings of the 57th Annual ACM Symposium on Theory of Computing , STOC '25, page 1863-1874, New York, NY, USA, 2025. Association for Computing Machinery. (Cited on page 6.)

- [MY22] Tomoyuki Morimae and Takashi Yamakawa. Quantum commitments and signatures without one-way functions. In Yevgeniy Dodis and Thomas Shrimpton, editors, CRYPTO 2022, Part I , volume 13507 of LNCS , pages 269-295. Springer, Cham, August 2022. (Cited on page 1.)
- [Nan20] Mikito Nanashima. Extending Learnability to Auxiliary-Input Cryptographic Primitives and Meta-PAC Learning. In Jacob Abernethy and Shivani Agarwal, editors, Proceedings of Thirty Third Conference on Learning Theory , volume 125 of Proceedings of Machine Learning Research , pages 2998-3029. PMLR, 09-12 Jul 2020. (Cited on page 2.)
- [Nao90] Moni Naor. Bit commitment using pseudo-randomness. In Gilles Brassard, editor, CRYPTO'89 , volume 435 of LNCS , pages 128-136. Springer, New York, August 1990. (Cited on page 1.)
- [NR06] Moni Naor and Guy N. Rothblum. Learning to impersonate. In Proceedings of the 23rd International Conference on Machine Learning , ICML '06, page 649-656, New York, NY, USA, 2006. Association for Computing Machinery. (Cited on page 1, 3.)
- [NY15] Moni Naor and Eylon Yogev. Bloom filters in adversarial environments. In Rosario Gennaro and Matthew J. B. Robshaw, editors, CRYPTO 2015, Part II , volume 9216 of LNCS , pages 565-584. Springer, Berlin, Heidelberg, August 2015. (Cited on page 1, 3.)
- [PJSE24] N. Pirnay, S. Jerbi, J. P. Seifert, and J. Eisert. An unconditional distribution learning advantage with shallow quantum circuits. arXiv:2411.15548, 2024. (Cited on page 6.)
- [PQS25] Alexander Poremba, Yihui Quek, and Peter Shor. The learning stabilizers with noise problem. arXiv:2410.18953, 2025. (Cited on page 6.)
- [PV88] Leonard Pitt and Leslie G. Valiant. Computational limitations on learning from examples. J. ACM , 35(4):965-984, oct 1988. (Cited on page 1.)
- [Reg05] Oded Regev. On lattices, learning with errors, random linear codes, and cryptography. In Harold N. Gabow and Ronald Fagin, editors, 37th ACM STOC , pages 84-93. ACM Press, May 2005. (Cited on page 1, 2, 4.)
- [Rom90] John Rompel. One-way functions are necessary and sufficient for secure signatures. In 22nd ACM STOC , pages 387-394. ACM Press, May 1990. (Cited on page 1.)
- [SSHE21] Ryan Sweke, Jean-Pierre Seifert, Dominik Hangleiter, and Jens Eisert. On the quantum versus classical learnability of discrete distributions. Quantum , 5:417, March 2021. (Cited on page 6.)
- [Sto83] Larry J. Stockmeyer. The complexity of approximate counting (preliminary version). In 15th ACM STOC , pages 118-126. ACM Press, April 1983. (Cited on page 10, 12.)
- [Val84] Leslie G. Valiant. A theory of the learnable. In 16th ACM STOC , pages 436-445. ACM Press, 1984. (Cited on page 1.)
- [Yan22] Jun Yan. General properties of quantum bit commitments (extended abstract). In Shweta Agrawal and Dongdai Lin, editors, ASIACRYPT 2022, Part IV , volume 13794 of LNCS , pages 628-657. Springer, Cham, December 2022. (Cited on page 1.)
- [Yat85] Yannis G. Yatracos. Rates of Convergence of Minimum Distance Estimators and Kolmogorov's Entropy. The Annals of Statistics , 13(2):768 - 774, 1985. (Cited on page 2, 3.)

## A Proof of Theorem 5.4

For showing Theorem 5.4, we will use the following Theorems A.1 and A.2.

Theorem A.1. For any QPT algorithm D that takes 1 n and z ∈ { 0 , 1 } n as input and outputs x ∈ { 0 , 1 } poly( n ) , there exists a deterministic polynomial-time algorithm Dis with access to a PP oracle, which takes 1 n , ℓ ∈ { 0 , 1 } n , m ∈ { 0 , 1 } n and x ∈ { 0 , 1 } poly( n ) , such that for all ( ℓ, m ) ∈ { 0 , 1 } n ×{ 0 , 1 } n , we have

$$\S D ( \mathcal { D } ( 1 ^ { n } , \ell ) , \mathcal { D } ( 1 ^ { n } , m ) )$$

$$& = \left | P r \left [ 1 \leftarrow D i s ^ { P P } ( 1 ^ { n } , \ell , m , x ) \colon x \leftarrow \mathcal { D } ( 1 ^ { n } , \ell ) \right ] - P r \left [ 1 \leftarrow D i s ^ { P P } ( 1 ^ { n } , \ell , m , x ) \colon x \leftarrow \mathcal { D } ( 1 ^ { n } , m ) \right ] \right | \, \left ( 2 8 6 \right )$$

for all sufficiently large n ∈ N .

Theorem A.2. For any QPT algorithm D that takes 1 n and z ∈ { 0 , 1 } n as input and outputs x ∈ { 0 , 1 } poly( n ) , there exists a PPT algorithm B with access to a PP oracle such that for all z ∈ { 0 , 1 } n , we have

$$\text {SD} ( \mathcal { D } ( 1 ^ { n } , z ) , \mathcal { B } ^ { \text {PP} } ( 1 ^ { n } , z ) ) = 0$$

for all sufficiently large n ∈ N .

Note that Theorems A.1 and A.2 directly follows from the following Lemma A.3. Therefore, we omit the proof of them.

Lemma A.3 ([FR99]). There exists a deterministic polynomial-time algorithm C with access to a PP oracle such that the following holds.

$$\mathcal { C } ^ { \mathbb { P } } ( 1 ^ { n } , \mathcal { C } , z ) = \Pr [ z \leftarrow \mathcal { D } ( 1 ^ { n } ) ] .$$

Here, D is a quantum polynomial-time algorithm that takes 1 n as input, and outputs z .

Proof of Theorem 5.4. The following proof is similar to that of Theorem 5.3.

Let Dis PP be a deterministic polynomial-time algorithm with access to a PP oracle given in Theorem A.1. For a QPT algorithm D , which takes 1 n and z ∈ { 0 , 1 } n as input, let B be a PPT algorithm with access to a PP oracle given in Theorem A.2 such that

$$\text {SD} ( \mathcal { D } ( 1 ^ { n } , z ) , \mathcal { B } ^ { \text {PP} } ( 1 ^ { n } , z ) ) = 0 .$$

We set t ( n ) := 100 n 2 · ϵ ( n ) 2 ( n +log( δ ( n ))) . Let us consider the following deterministic algorithm M ω with access to a PP oracle.

M PP ω (1 n , a, b, { x i , r i } i ∈ [ t ( n )] ) :

1. Run Dis PP ϵ ( a, b, x i ) for all i ∈ [ t ( n )] .

$$2 . \text { For all } i \in [ t ( n ) ] , \text { run } X _ { a , r _ { i } ( 2 ) } \leftarrow \mathcal { B } ^ { \text {PP} } ( a ; r _ { i } ) \text { and Dis} ^ { \text {PP} } ( a , b , X _ { a , r _ { i } } ) .$$

3. Output 1 if

$$\left | \sum _ { i \in [ t ( n ) ] } \frac { \text {DisP} \left ( a , b , x _ { i } \right ) } { t ( n ) } - \sum _ { i \in [ t ( n ) ] } \frac { \text {DisP} \left ( a , b , X _ { a , r _ { i } } \right ) } { t ( n ) } \right | \leq \text {Opt} _ { n } + \omega ( n ) .$$

Otherwise, output 0 .

For any function ω , and any a 1 , ..., a i ∈ { 0 , 1 } i with i ∈ N , let us define

$$\mathcal { L } _ { \omega , ( a _ { 1 } , \dots , a _ { i } ) }$$

$$\colon = \left \{ \{ x _ { i } , r _ { i } \} _ { i \in \{ t ( n ) \} } \in \{ 0 , 1 \} ^ { * } , n \in \mathbb { N } \colon \exists a \in \{ 0 , 1 \} ^ { n - i } \text { such that } \forall b \in \{ 0 , 1 \} ^ { n } , \text { we have }$$

$$1 \leftarrow \mathcal { M } _ { \omega } ^ { \text {PP} } ( 1 ^ { n } , ( a _ { 1 } , \dots , a _ { i } ) , a , b , \{ x _ { i } , r _ { i } \} _ { i \in [ t ( n ) ] } \right ) \Big \} .$$

Clearly, we have L ω, ( a 1 ,...,a i ) ∈ Σ PP 2 .

We consider the following PPT algorithm A with access to a Σ PP 2 oracle:

A Σ PP 2 (1 n , { x i } i ∈ [ t ( n )] ) :

1. Uniformly randomly sample { r i } i ∈ [ t ( n )] .
2. For all I ∈ [ n ] , run the following.
3. (a) Check if there exists a I +1 , ..., a n ∈ { 0 , 1 } n -I such that

$$\left | \sum _ { i \in [ t ( n ) ] } \frac { \text {Dis} _ { \epsilon } ^ { \text {PP} } ( \text {out} _ { 1 } , \dots , \text {out} _ { I - 1 } , 1 , a _ { I + 1 } , \dots , a _ { n } , b , x _ { i } ) } { t ( n ) } \right |$$

$$- \sum _ { i \in [ t ( n ) ] } \frac { \text {DDP} ( \text {out} _ { 1 } , \dots , \text {out} _ { I - 1 } , 1 , a _ { I + 1 } , \dots , a _ { n } , b , X _ { ( \text {out} _ { 1 } , \dots , \text {out} _ { I - 1 } , 1 , a _ { I + 1 } , \dots , a _ { n } ) _ { r _ { i } } ) } { t ( n ) } \Big |$$

$$\leq O p t _ { n } + \frac { 2 I - 1 } { 4 n \cdot \epsilon ( n ) }$$

for all b ∈ { 0 , 1 } n bycheckingthat ( { x i , r i } i ∈ [ t ( n )] , n ) is contained in L 2 I -1 4 n · ϵ ( n ) , ( out 1 ,..., out I -1 , 1) . (b) If so, set out I = 1 . Otherwise, set out I = 0 .

3. Output out 1 , ..., out n .

We can show that A Σ PP 2 satisfies

$$\Pr \left [ \text {SD} ( \mathcal { D } ( 1 ^ { n } , h ) , \mathcal { T } ( 1 ^ { n } ) ) \leq \left ( 3 + \frac { 1 } { \epsilon ( n ) } \right ) \cdot \text {Opt} _ { n } + \frac { 1 } { \epsilon ( n ) } \cdot \begin{array} { c c } \{ x _ { i } \} _ { i \in [ t ( n ) ] } \leftarrow \mathcal { T } ( 1 ^ { n } ) ^ { \otimes t ( n ) } \\ h \leftarrow \mathcal { A } ^ { \mathbb { E } } _ { 2 } P ^ { 1 } ( 1 ^ { n } , \{ x _ { i } \} _ { i \in [ t ( n ) ] } ) \end{array} \right ] \geq 1 - 1 / \delta ( n )$$

for all sufficiently large n ∈ N . Here, Opt n := min a ∈{ 0 , 1 } n { SD ( T (1 n ) , D (1 n , a )) } . The analysis is the same as Theorem 5.3, and thus we omit it.

## B Proof of Theorem 5.9

In the following, we show Theorem 5.9. For showing Theorem 5.9, let us introduce average-case hardness of quantum probability estimation secure against QPT algorithm with access to a Σ P 3 oracle as follows.

Definition B.1 (Average-case hardness of quantum probability estimation secure against QPT algorithm with Σ P 3 oracle). We say that average-case hardness of quantum probability estimation secure against QPT algorithm with access to a Σ P 3 oracle holds if the following holds: There exists a QPT algorithm S that takes 1 n as input and outputs x ∈ { 0 , 1 } n such that for all QPT algorithms A with access to a Σ P 3 oracle and constants c &gt; 0

$$\Pr _ { x \leftarrow \mathcal { S } ( 1 ^ { n } ) } \left [ \mathcal { A } ^ { \Sigma } 3 \left ( x \right ) - \Pr [ x \leftarrow \mathcal { S } ( 1 ^ { n } ) ] \right ] \leq \frac { \Pr [ x \leftarrow \mathcal { S } ( 1 ^ { n } ) ] } { n ^ { c } } \right ] \leq 1 - \frac { 1 } { n ^ { c } }$$

for infinitely many n ∈ N .

Proof of Theorem 5.9. The proof follows from [KT25, CGG24] and Lemma 3.5.

In the similar way as Theorem 5.1 of [KT25], we can show that Assumption 2.10 and P # P ⊈ BQP Σ P 3 implies Definition B.1. In the similar way as Theorem 5.2 of [KT25] 7 , we can show that Definition B.1 implies distributionally OWPuzzs secure against QPT algorithm with access to a Σ P 3 oracle. In the similar way as Theorem 29 of [CGG24], we can show that distributionally OWPuzzs secure against QPT with access to a Σ P 3 oracle implies nuQEFID secure against QPT algorithm with access to a Σ P 3 oracle. In the similar way as Lemma 3.5, we can show that nuQEFID secure against QPT algorithm with access to a Σ P 3 oracle implies average-case hardness of proper quantum distribution learning secure against QPT algorithm with access to a Σ P 3 oracle. Average-case hardness of proper quantum distribution learning secure against QPT algorithm with access to a Σ P 3 oracle directly implies Assumption 5.7.

7 See also Lemma 4.3 of [HM24].