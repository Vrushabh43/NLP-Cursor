## Unlocking early fault-tolerant quantum computing with mitigated magic dilution

Surabhi Luthra, 1, ∗ Alexandra E. Moylett, 2, † Dan E. Browne, 1 and Earl T. Campbell 2, 3

1 Department of Physics and Astronomy, University College London, London, WC1E 6BT, United Kingdom

2 Riverlane, St Andrews House, 59 St Andrews Street, Cambridge CB2 3BZ, United Kingdom

3 Department of Physics and Astronomy, University of Sheffield, Sheffield, S3 7RH, United Kingdom

(Dated: August 8, 2025)

As quantum computing progresses towards the early fault-tolerant regime, quantum error correction will play a crucial role in protecting qubits and enabling logical Clifford operations. However, the number of logical qubits will initially remain limited, posing challenges for resource-intensive tasks like magic state distillation. It is therefore essential to develop efficient methods for implementing non-Clifford operations, such as small-angle rotations, to maximise the computational capabilities of devices within these constraints. In this work, we introduce mitigated magic dilution (MMD) as an approach to synthesise small-angle rotations by employing quantum error mitigation techniques to sample logical Clifford circuits given noisy encoded magic states. We explore the utility of our approach for the simulation of the 2D Fermi-Hubbard model. We identify evolution time regimes where MMD outperforms state-of-the-art synthesis techniques in the number of noisy encoded magic states required for square lattices up to size 8 × 8. Moreover, we demonstrate that our method can provide a practical advantage that is quantified by a better-than-quadratic improvement in the resource requirements for small-angle rotations over classical simulators. This work paves the way for early fault-tolerant demonstrations on devices supporting millions of quantum operations, the so-called MegaQuOp regime.

## I. INTRODUCTION

Recent progress in experimental demonstrations of quantum error correction and logical computation [1-5] has encouraged research towards practical applications of early fault-tolerant quantum computers [6-9]. The Gottesman-Knill theorem [10] shows that universal quantum computation necessitates non-Clifford gates. Implementing these gates typically requires the preparation of magic states or non-stabiliser states where resourceintensive techniques such as magic state distillation [11] are used to improve their fidelity. Despite ongoing research in reducing the associated overhead of these factories [12-14], resource analysis of fault-tolerant implementations of large algorithms using magic state distillation require millions of physical qubits [15-18]. In the anticipated early fault-tolerant era, where useful magic state distillation factories cannot be accommodated due to physical qubit limitations, we investigate quantum error mitigation as a promising alternative.

Quantum error mitigation (QEM) is generally considered in the context of estimating the expectation value of an observable using a quantum circuit, for example in variational quantum eigensolvers [19] and statistical versions of phase estimation [20-24]. QEM methods improve the accuracy of the estimated expectation value by reducing the noise-induced bias in the circuit [25, 26]. This is done through post-processing of the measurement outcomes from an ensemble of circuit implementations and so is distinct from quantum error correction which reduces the logical error rate for each individual circuit run [26]. Consequently, most error mitigation techniques require additional sampling that increases with the noise in the circuit, resulting in asymptotically unfavourable scaling [26, 27].

[∗ zcaplut@ucl.ac.uk](mailto:zcaplut@ucl.ac.uk)

† Current address: Nu Quantum, 21 JJ Thompson Avenue, Cambridge, CB3 0FA, United Kingdom

Despite this, QEM techniques could thrive in the early fault-tolerant regime when applied at the logical level by focusing on their pre-asymptotic behaviour prior to the exponential scaling becoming impractical [6, 28]. As per the standard magic state model [11], we assume that logical Clifford operations are ideal; these may be implemented transversely depending on the error-correcting code and underlying hardware. Meanwhile, non-Clifford operations are subject to noise due to imperfect encoded magic states. Given this model, we leverage methods from QEM to simulate single-qubit Z -rotation gates in this work, which are an integral part of many quantum algorithms.

QEM ideas have previously been proposed to simulate circuits containing T gates such as in Ref. [27]. A singlequbit Z -rotation gate could then be realized by synthesising into error-corrected Clifford gates and encoded noisy T gates, for example, using the Ross-Selinger method [29]. This leads to a T -count (total number of T gates) that scales as O (log 2 (1 /ϵ synth )) with accuracy ϵ synth of the resultant rotation. The sampling overhead also increases dramatically with the inverse accuracy. This is counter-intuitive as magic resource theory [30-34] shows that a small-angle Z -rotation gate is a less powerful resource than a T gate, and yet they are more costly to implement. This perspective hints towards a much more efficient approach to QEM where small-angle Z -rotation gates have a low gate and sampling overhead assuming error-corrected Clifford gates with sufficiently low noise levels. This direction has been explored in the Noisy- Intermediate Scale Quantum (NISQ) setting [35] but not in the context of early fault-tolerant quantum computing.

In this paper, we introduce a framework that applies the quasiprobability method [31, 36] to explore the advantages of decomposing single-qubit Z -rotation gates into gates from the Clifford hierarchy [37]. A conceptual starting point is to consider the following two-step process: first, use magic state dilution [38] to convert a high magic resource into many low magic resources; and second, use quantum error mitigation to reduce any inherent noise or noise introduced in the dilution process. While each of these two steps could be cast as separate convex optimisation problems, it is more elegant and optimal to compress them. Therefore, rather than implementing these processes independently, our approach unifies them into a single optimisation problem, which we introduce as mitigated magic dilution (MMD). Specifically, we use convex optimisation to find the optimal sample complexity of performing small-angle single-qubit rotations from noisy encoded magic states.

There has been significant progress in the preparation of encoded magic states. For example, in Ref. [39], it was shown that encoded magic states can be prepared with a logical error rate of ∼ 0 . 4 × 10 -3 under the assumption of ideal single-qubit operations and depolarised two-qubit gates with 0 . 1% error rate using post-selection. Moreover, there are several improvements to the state preparation of non-stabiliser states for arbitrary smallangle rotations that could offer further advantages to the results presented in this paper, which we examine in Section V.

We compare our framework against a baseline classical approach where small-angle single-qubit rotations are decomposed into Clifford operations, similar to Refs. [3034]. Notably, we demonstrate a polynomial advantage, the magnitude of which depends on the quality of initial magic state preparation. We quantify this advantage in terms of the polynomial degree of magic resource saving of our method. For encoded magic states prepared with 1% dephasing noise, this saving is better than cubic, while for 0.1% dephasing noise we find a saving of degree approximately 11.43. Moreover, we show that our method can improve upon a state-of-the-art classical simulator, the sum-over-Cliffords stabilizer extent method [34], offering a 2.37 degree of magic resource saving.

To evaluate the practical benefits of this approach, we study the resource requirements to simulate the time evolution of the 2D Fermi-Hubbard model. The 2D Fermi-Hubbard model [40, 41] is of notable interest in the early fault-tolerant regime [6, 42] due to its importance in condensed matter physics (e.g., to understand high-temperature superconductivity [43] and the Mott metal-insulator transition [44]), as well as its simplicity arising from its highly regular lattice structure. Our analysis in Section IV demonstrates that MMD is a more resource-efficient method than direct gate synthesis, requiring fewer magic states in total. Moreover, the expected number of magic states per sample is significantly smaller, and therefore MMD is particularly amenable to early fault-tolerant devices.

Even when quantum computers have an asymptotic speedup over classical computing they can fail to have an in-practice speed-up for example problems of a relevant size [45], and so it is crucial to make such comparison. Here, we consider the example problem of a Fermi-Hubbard model with a 6 × 6 square lattice and evolution time t = 0 . 25 as a strong candidate for quantum advantage. We find that our MMD method requires a circuit with only 1037 non-Clifford gate teleportations (on average) and 5 . 34 × 10 6 samples. Even with error correction overheads, a sample per second is a conservative runtime estimate, taking a single quantum computer 62 days for all samples. For the same calculation, the sum-over-Cliffords stabilizer extent method would require a 5 . 18 × 10 17 seconds runtime, which would take 1 . 64 × 10 4 years to complete when assuming a million classical processors in parallel. Thereby, our MMD protocol facilitates a significant reduction in runtime over the the sum-over-Cliffords classical simulator for conservative time evolution and lattice sizes of interest. Combined with a Pauli-based model of computation [46], such an application would require logical error rates of approximately 1 part in a millon, the so-called MegaQuOp regime [9].

This paper is structured as follows. In Section II we briefly summarise the quasiprobability method. In Section III, we introduce our framework in two steps, working in the channel representation of all unitary gates U throughout, which are denoted as U ( · ) = U ( · ) U † . We first present the application of the quasiprobability method to target Z rotation channels over diagonal Clifford + T channels in Section III A using a linear combination of channels decomposition. We then generalise this to decompositions over diagonal Clifford + T 1 n channels in Section III B. Finally, in Section IV, we demonstrate the practical applicability of our framework for a second-order Trotter simulation of the Fermi-Hubbard model with comparison to gate synthesis.

## II. QUASIPROBABILITY METHOD

The motivation behind the quasiprobability method is that an ideal quantum operation can be decomposed into a basis set of noisy operations. Let U t ( ρ ) = U t ρU t † be the ideal target unitary channel of a quantum operation U t and let {U n i } be a set of channels corresponding to the noisy operations that can be performed on a given quantum hardware. The noise on these operations would typically be characterised using a tomography procedure [26, 47]. We can then write the following decomposition, hereafter referred to as the linear combinations of channels (LCC) decomposition

$$\mathcal { U } ^ { t } = \sum _ { i } x _ { i } \mathcal { U } _ { i } ^ { n }$$

where x i are real coefficients that can be positive or negative such that Eq. (1) is a quasiprobability representation.

It follows that the expectation value of an observable O for the target operation can be written in terms of the expectation value of the noisy operations as

$$T r [ O \mathcal { U } ^ { t } ( \rho ) ] & = T r [ O \sum _ { i } x _ { i } \mathcal { U } _ { i } ^ { n } ( \rho ) ] \\ & = \sum _ { i } x _ { i } T r [ O \mathcal { U } _ { i } ^ { n } ( \rho ) ] .$$

The expectation values Tr [ O U n i ( ρ ) ] associated with noisy channels U n i can be estimated using Monte Carlo sampling. Each noisy operation U n i , specified by index i , is applied with probability | x i | / ∑ i | x i | , and the resulting expectation value is multiplied by sign( x i ) ∑ i | x i | [26, 31]. From this, an estimate of the ideal expectation value can be calculated up to an accuracy ϵ and probability greater than 1 -δ , where

$$\delta = 2 \exp \left ( \frac { - N \epsilon ^ { 2 } } { 2 ( \sum _ { i } | x _ { i } | ) ^ { 2 } } \right ) \quad \ \ ( 3 )$$

and the number of samples N is determined by Hoeffding's inequality to be

$$N = \frac { 2 } { \epsilon ^ { 2 } } \left ( \sum _ { i } | x _ { i } | \right ) ^ { 2 } \ln \left ( \frac { 2 } { \bar { \delta } } \right ) .$$

Thus, the number of samples scale as O ( λ 2 /ϵ 2 ) up to logarithmic factors, with λ = ∑ i | x i | . The quantity λ 2 is referred to as the sampling overhead of using this method over finding the expectation value of the ideal target channel directly [26, 27].

## III. METHODOLOGY

## A. Linear Combination of Channels (LCC) Decomposition

We first demonstrate how the quasiprobability method can be used to decompose target Z -rotation channels. In the simplest case, we consider a diagonal Cliffords + T channel decomposition, forming an overcomplete basis set to ensure that we can optimise this decomposition with respect to the sampling overhead.

Consider the action of a small-angle Z -rotation channel R θ z ( ρ ) = R z ( θ ) ρ ( R z ( θ )) † acting on a state represented by density matrix ρ in Fig. 1, where R z ( θ ) = exp( -i ( θ/ 2) Z ) is a gate representing a rotation about the Z -axis with angle θ . In this geometric picture, we label eight channels corresponding to the action of a basis set of gates

$$G & = \{ T ^ { k } \colon 1 \leq k \leq 8 \} \\ & = \{ I , T , S , S T , Z , Z T , Z S , Z S T \} ,$$

FIG. 1. Action of T k rotation channels (where 1 ≤ k ≤ 8) on a density matrix ρ . The eight operations (in red) form the initial basis set G . The target rotation channel R θ z ( ρ ) is shown in blue.

<!-- image -->

which forms a cyclic group ( G, × ) generated by the T gate under multiplication. We represent these gates in their channel representation to form a set G such that

$$\mathcal { G } = \{ \mathcal { T } ^ { k } ( \rho ) = ( T ^ { k } ) \rho ( T ^ { k } ) ^ { \dagger } \colon 1 \leq k \leq 8 \} .$$

The LCC decomposition is given by

$$\mathcal { R } _ { z } ^ { \theta } ( \cdot ) = \sum _ { U \in G } x _ { U } U ( \cdot ) U ^ { \dagger } = \sum _ { U \in \mathcal { G } } x _ { U } \mathcal { U } ( \cdot ) ,$$

where R θ z ( · ) represents the single qubit Z -rotation channel for the R z ( θ ) gate. This is a quasiprobability decomposition such that the coefficients x U are real and satisfy ∑ U∈G x U = 1. The quantity λ is defined as the l 1 -norm of the coefficients in this decomposition, that is

$$\lambda = \| x \| _ { 1 } = \sum _ { U \in G } | x _ { U } | ,$$

such that λ 2 is the sampling overhead of each decomposition from Hoeffding's inequality [25, 27].

It can be noted that the decomposition in Eq. (7) is not unique over a chosen basis set and so it is important to minimise the sampling overhead over different solutions. We define the optimal decomposition for a given Z -rotation channel as the decomposition into elements of G with the minimum λ , which we denote as Λ G ( R θ z ). This can be written as

$$\intertext { t h } \Lambda _ { \mathcal { G } } ( \mathcal { R } _ { z } ^ { \theta } ( \cdot ) ) = \min \left \{ \lambda = \| x _ { U } \| _ { 1 } \left | \mathcal { R } _ { z } ^ { \theta } ( \cdot ) = \sum _ { U \in \mathcal { G } } x _ { U } \mathcal { U } ( \cdot ) \right \} . \\ \intertext { l e n s } \intertext { b y d o f i n i t i o n } \Lambda _ { \mathcal { G } } ( \mathcal { R } _ { z } ^ { \theta } ) > 1 \ w h o r o \ \Lambda _ { \mathcal { G } } ( \mathcal { R } ^ { \theta } ) = 1 \ i f \ \mathcal { R } _ { \mathcal { G } } ^ { \theta } \subset \mathcal { G }$$

By definition, Λ G ( R θ z ) ≥ 1 where Λ G ( R θ z ) = 1 if R θ z ∈ G for some group G representing the basis set of channels. The solution to Eq. (9) is equivalent to minimising the sampling overhead λ 2 over the basis set of channels, thus Λ G ( R θ z ( · )) finds the optimal decomposition of R θ z ( · ) for the chosen group G . This can be further expressed as a convex optimisation problem to solve a linear system given by

$$\Lambda _ { \mathcal { G } } ( \mathcal { R } _ { z } ^ { \theta } ( \cdot ) ) = \min \| x \| _ { 1 } \text { subject to } A x = b . \quad ( 1 0 ) \quad \begin{smallmatrix} \varphi & \\ & \\ \text {optimum} \end{smallmatrix}$$

Here, vector b represents m elements of the target channel R θ z expressed in a vectorised form, and A is an m × n matrix, with n columns for the basis set of channels in the decomposition and m rows of elements that specify each channel (see Eq. (A1) and Eq. (A2) as an example). The j th column of matrix A can be generated by determining the vectorised form of the j th channel U j ( · ) = U j ( · ) U † j for U j ∈ G and j ∈ { 1 , 2 , . . . , n } . Where possible, we also make a concerted effort to minimise the number of nonzero elements in x whilst keeping the optimal sampling overhead constant.

For the ideal basis set of channels G defined in Eq. (6), we use CVXPY [48, 49] to solve Eq. (10) and find that decompositions of the form

$$\mathcal { R } _ { z } ^ { \theta } ( \cdot ) = x _ { I } \mathcal { I } ( \cdot ) + x _ { T } \mathcal { T } ( \cdot ) + x _ { Z } \mathcal { Z } ( \cdot ) \quad ( 1 1 )$$

are optimal, with

$$\Lambda _ { \mathcal { G } } ( \mathcal { R } _ { z } ^ { \theta } ( \cdot ) ) = ( \sqrt { 2 } - 1 ) \sin { ( \theta ) } + \cos { ( \theta ) } \quad ( 1 2 ) \quad | \sqrt { 2 } |$$

for 0 ≤ θ ≤ π 4 . Additionally, considering subsets of G with only 2 elements, we find that a solution to the optimisation problem cannot be found, and therefore 3 contributions are required (see Section A).

As a classical baseline, we consider the subset of G that are Clifford operations, denoted as C . In that case, the optimal decomposition consists of {I , S , Z} channels and the corresponding l 1 -norm Λ C is

$$\Lambda _ { \mathcal { C } } ( \mathcal { R } _ { z } ^ { \theta } ( \cdot ) ) = \sin \left ( \theta \right ) + \cos \left ( \theta \right ) . \quad ( 1 3 ) \quad s i c a l { 1 } { 3 }$$

We compare this baseline to our quantum protocol by considering (Λ 2 G ) γ = Λ 2 C , which implicitly defines γ where

$$\gamma ( \theta ) = \frac { \ln ( \Lambda _ { C } ( \mathcal { R } _ { z } ^ { \theta } ) ) } { \ln ( \Lambda _ { \mathcal { G } } ( \mathcal { R } _ { z } ^ { \theta } ) ) } .$$

Consequently, we interpret γ as the polynomial degree of magic resource saving of the optimal decomposition over G compared to the optimal decomposition over C , for a specified target rotation channel. As θ → 0, γ approaches √ 2 + 1 ≈ 2 . 41 &gt; 2, indicating a slightly betterthan-quadratic advantage of decomposing a (very) smallangle rotation into a quasiprobability decomposition of {I , T , Z} channels instead of {I , S , Z} channels. From this, we can now proceed to generalise these findings to achieve a better advantage for small-angle rotations by our choice of G from the Clifford hierarchy.

## B. Climbing the Clifford Hierarchy

From Eq. (12) and Eq. (13), it can be seen that the optimal channel decompositions over our choice of G and C respectively are of the form {I , R ϕ z , Z} . Specifically, ϕ = π/ 2 for R ϕ z = S and ϕ = π/ 4 for R ϕ z = T with optimality valid within the range 0 ≤ θ ≤ ϕ . Therefore, for smaller target rotations, we can minimise Λ G ( R θ z ( · )) further by including R ϕ z channels with smaller ϕ in our choice of G .

First, we let i ∈ Z ≥ 0 and define n = 2 i -1 . We then choose G to be

$$\mathcal { G } = \{ \mathcal { T } ^ { \frac { k } { n } } ( \rho ) = ( T ^ { \frac { k } { n } } ) \rho ( T ^ { \frac { k } { n } } ) ^ { \dagger } \colon 1 \leq k \leq 8 n \} ,$$

where T 1 n is an n th -root T gate from the ( i +2)-th level of the Clifford hierarchy, and ϕ = π/ 4 n . Therefore, i = 0 represents the S gate, i = 1 represents the T gate, and so on. These T 1 n gates can be implemented by a generalised gate teleportation circuit as shown in Fig. 2.

FIG. 2. Generalised teleportation circuit to implement a n √ T gate using i distinct magic states, where n = 2 i -1 , and Clifford operations. Boxes and gates with a dashed line are classically controlled; they are only implemented if the measurement below obtains an outcome with eigenvalue -1.

<!-- image -->

We find that the LCC decomposition for Eq. (10) with G as Eq. (15) that minimises the sampling overhead is given by

$$\mathcal { R } _ { z } ^ { \theta } ( \cdot ) = x _ { I } \mathcal { I } ( \cdot ) + x _ { n } \mathcal { T } ^ { \frac { 1 } { n } } ( \cdot ) + x _ { Z } \mathcal { Z } ( \cdot ) , \quad ( 1 6 )$$

with corresponding Λ G ( R θ z ( · )) as

$$\Lambda _ { \mathcal { G } } ( \mathcal { R } _ { z } ^ { \theta } ( \cdot ) ) = \cos ( \theta ) + \frac { \sin ( \theta ) } { \sin ( \phi ) } \left ( 1 - \cos ( \phi ) \right ) . \quad ( 1 7 )$$

For small-angle rotations, Λ G ( R θ z ( · )) can be approximated to be

$$\Lambda _ { \mathcal { G } } ( \mathcal { R } _ { z } ^ { \theta } ( \cdot ) ) \approx 1 + \theta \left ( \frac { 1 - \cos ( \phi ) } { \sin ( \phi ) } \right ) ,$$

with a degree of resource saving compared to a Clifford decomposition of

$$\gamma = \frac { \sin ( \phi ) } { 1 - \cos ( \phi ) } = \cot \left ( \frac { \phi } { 2 } \right ) \quad \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \$$

in the limit of small θ (see Section B 1). Therefore in the {I , T 1 n , Z} decomposition, climbing the Clifford hierarchy in terms of T 1 n channels results in a larger degree of saving compared to the {I , S , Z} Clifford decomposition.

We now consider the case where the non-Clifford channels in our basis set are subject to noise, as originally motivated in the quasiprobability method. Non-Clifford operations (in our case T 1 n ) can be implemented via encoded gate teleportation circuits using noisy encoded magic states and error-corrected Clifford gates as shown in Fig. 2. The most relevant noise channel for these diagonal rotation gates in our basis set is the dephasing noise channel (see Section C), which is defined as

$$\varepsilon ( \cdot ) = ( 1 - p ) ( \cdot ) + p Z ( \cdot ) Z , \quad ( 2 0 ) \quad \text {wh}$$

where p quantifies the amount of dephasing noise. The action of the dephasing noise channel on a unitary channel in our basis set of unitary operations is given as

$$\mathcal { U } ^ { \text {depth} ( \cdot ) = \varepsilon ( \mathcal { U } ^ { \text {ideal} } ( \cdot ) ) = ( 1 - p ) \mathcal { U } ^ { \text {ideal} } ( \cdot ) + p \mathcal { Z } \circ \mathcal { U } ^ { \text {ideal} } ( \cdot ) . \quad \text {decom} \quad \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \$$

As the number of iterations of the teleportation circuit increases for the implementation of gates from higher levels of the Clifford hierarchy (Fig. 2), we find that the dephasing noise changes correspondingly. We assume that each non-stabiliser state | T 1 n ⟩ is prepared with uniform (independent of θ ) fidelity. However, in Section V, we discuss how θ -dependent fidelities could lead to further performance improvements.

If the dephasing noise for a T gate implementation (requiring a | T ⟩ magic state) is p , the effective dephasing noise for a T 1 n gate can be found by considering the errors on the non-stabiliser states that lead to an error on the T 1 n gate. For example, the probability of a Z error acting on a T 1 2 gate is given by the probability of an error occurring on either the | T ⟩ or | T 1 2 ⟩ state [50], that is

$$\stackrel { p _ { \text {eff} } = p \left ( 1 - \frac { p } { 2 } \right ) + \frac { p } { 2 } ( 1 - p ) = \frac { 3 } { 2 } p - p ^ { 2 } < \frac { 3 } { 2 } p , \quad ( 2 2 ) } { p _ { \text {eff} } = p \left ( 1 - \frac { p } { 2 } \right ) + \frac { p } { 2 } ( 1 - p ) = \frac { 3 } { 2 } p - p ^ { 2 } < \frac { 3 } { 2 } p , \quad ( 2 2 ) }$$

where we take into account that there is a 50% probability that a T gate correction needs to be applied (recall Fig. 2). Therefore, the effective dephasing noise on a T 1 n gate is bounded by p eff = ( 2 -n -1 ) p .

As a result of this, the l 1 -norm for the {I , ε ( T 1 n ) , Z} decomposition transforms from the ideal case in Eq. (17) to the following:

$$\Lambda _ { \mathcal { G } } ( \mathcal { R } _ { z } ^ { \theta } ( \cdot ) ) = & \left | \cos ^ { 2 } \left ( \frac { \theta } { 2 } \right ) - \left [ \cos ^ { 2 } \left ( \frac { \phi } { 2 } \right ) - p _ { \text {eff} } \cos ( \phi ) \right ] \frac { \sin ( \theta ) } { ( 1 - 2 p _ { \text {eff} } ) \sin ( \phi ) } \right | \\ & + \left | \frac { \sin ( \theta ) } { ( 1 - 2 p _ { \text {eff} } ) \sin ( \phi ) } \right | \\ & + \left | \sin ^ { 2 } \left ( \frac { \theta } { 2 } \right ) - \left [ \sin ^ { 2 } \left ( \frac { \phi } { 2 } \right ) + p _ { \text {eff} } \cos ( \phi ) \right ] \frac { \sin ( \theta ) } { ( 1 - 2 p _ { \text {eff} } ) \sin ( \phi ) } \right | .$$

In Fig. 3 we present Λ G ( R θ z ) as function of θ for {I , ε ( T 1 n ) , Z} decompositions with n ∈ { 0 . 5 , 1 , 2 , 4 , 8 } for p = 0 . 1% dephasing noise, where n = 0 . 5 corresponds to the S channel.

In particular, we are interested in the degree of magic resource saving γ to benchmark against the classical Clifford decomposition. As θ → 0, γ with respect to the {I , S , Z} Clifford decomposition is approximated by (see Section B 2)

$$\frac { 1 } { \gamma } \approx \frac { \csc ( \phi ) } { ( 1 - 2 p _ { \text {eff} } ) } - \cot ( \phi ) . \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \text {f o u } \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \text {f o u } \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t } \\ \end{array} } \quad \text { (24)} \quad \text { \begin{array} { c c } \text {e s t }$$

From Fig. 4, we find that for p = 0 . 1% and in the limit of small θ , we can achieve at least a ∼ 2 . 4 degree of saving in the simplest case of a {I , ε ( T ) , Z} decomposition, and greater than ∼ 11 . 4 degree of saving relative to the Clifford decomposition by replacing T with a T 1 8 channel.

We further note the dependence of Λ G ( R θ z ) on the dephasing noise p . For p = 0 . 1%, increasing n in our protocol results in a greater advantage up to n = 8, as shown in Fig. 4. However, for higher p , this is not always the case. In fact, for 1% dephasing noise, going beyond n = 2 presents no further improvement in resource saving as shown in Table I (see Section D for corresponding values of ln(Λ G ( R θ z ))). In other words, the {I , ε ( T 1 2 ) , Z} decomposition is optimal and provides a lower bound of ∼ 3 . 6 degree of saving for small θ . In general, the smallest value of n that provides the optimal saving can be found by maximising γ with respect to n (indicated in bold in Table I).

A further useful metric to consider is the expected number of magic states required per sample for an optimal decomposition of the form Eq. (16) which we derive from the proportion of | x n | relative to Λ G ( R θ z ), and the total number of magic states (per sample) required to implement a T 1 n gate using Fig. 2:

FIG. 3. Λ G ( R θ z ) as a function of target rotation angle θ for different optimal decompositions of the form {I , ε ( T 1 n ) , Z} including the optimal Clifford decomposition of {I , S , Z} . A dephasing error of 0 . 1% is assumed for non-Clifford state preparation.

<!-- image -->

FIG. 4. Degree of magic resource saving γ as a function of target rotation angle θ for different optimal decompositions of the form {I , ε ( T 1 n ) , Z} relative to the optimal Clifford decomposition of {I , S , Z} . A dephasing error of 0 . 1% is assumed for non-Clifford state preparation.

<!-- image -->

$$E = \left ( 2 - \frac { 1 } { n } \right ) \frac { \left | x _ { n } \right | } { \Lambda _ { \mathcal { G } } ( \mathcal { R } _ { z } ^ { \theta } ) } .$$

In this expression, x n is the coefficient of the T 1 n term in the LCC decomposition of the form {I , ε ( T 1 n ) , Z} , and Λ G is the l 1 -norm of the coefficients in this decomposition. As the target rotation angle θ decreases, | x n | also decreases, resulting in a smaller number of expected magic states. Thus, this method 'dilutes' magic resource in simulating smaller rotations from T 1 n channels of higher magic resource. This dilution phenomenon is evident in Fig. 5, which shows the expected number of magic states (per sample) decreasing with the rotation angle θ .

TABLE I. Degree of magic resource saving γ for a basis set of channels G with optimal channel decomposition {I , ε ( T 1 n ) , Z} relative to the {I , S , Z} channel combination for increasing n up to the sixth level of the Clifford hierarchy, with non-Clifford gates subject to dephasing noise with probability p .

|   n | ϕ    | R ϕ z      | γ (Small θ )           | γ (Small θ )   | γ (Small θ )   |
|-----|------|------------|------------------------|----------------|----------------|
|     |      |            | p = 0 . 01% p = 0 . 1% | p = 0 . 5%     | p = 1 . 0%     |
|   1 | π 4  | T √        | 2.41 2.40              | 2.33           | 2.26           |
|   2 | π 8  | T 5.01 √   | 4.84                   | 4.19           | 3.58           |
|   4 | π 16 | 4 T 9.97 √ | 8.58                   | 5.27           | 3.52           |
|   8 | π 32 | 8 T 18.88  | 11.43                  | 4.10           | 2.24           |

FIG. 5. Expected number of magic states E per sample as a function of target rotation angle θ for different optimal decompositions of the form {I , ε ( T 1 n ) , Z} relative to the optimal Clifford decomposition of {I , S , Z} . A dephasing error of 0 . 1% is assumed for non-Clifford state preparation.

<!-- image -->

We also present a comparison of our quantum protocol to the classical sum-over-Cliffords simulation method [34]. The total runtime of this method scales as O ( ξ/ϵ 4 ) where ξ is the stabilizer extent and ϵ is the precision of the simulation. Therefore, the sum-over-Cliffords method has a worse scaling w.r.t. the desired precision than MMD where the scaling is proportional to 1 /ϵ 2 as in Eq. (4). In the small θ limit, the stabilizer extent for a Z -rotation is given by

$$\xi ( R ( \theta ) ) = \exp ( \tan ( \pi / 8 ) \theta ) .$$

Therefore, we can define a resource saving degree γ SE such that (Λ 2 G ) γ SE = ξ analogously to Eq. (24). This results in

$$\gamma _ { \text {SE} } ( \theta ) = \frac { \ln ( \xi ( R ( \theta ) ) ) } { 2 \ln ( \Lambda _ { \mathcal { G } } ( \mathcal { R } _ { z } ^ { \theta } ) ) } .$$

We present this with the caveat that MMD has an additional advantage with respect to precision ϵ scaling, which is not captured by γ SE .

TABLE II. Degree of magic resource saving γ SE for a basis set of channels G with optimal channel decomposition {I , ε ( T 1 n ) , Z} relative to the stabiliser extent method for increasing n up to the sixth level of the Clifford hierarchy, with non-Clifford gates subject to dephasing noise with probability p .

|   n | ϕ    | R ϕ z   | γ SE (Small θ )        | γ SE (Small θ )   | γ SE (Small θ )   |
|-----|------|---------|------------------------|-------------------|-------------------|
|     |      |         | p = 0 . 01% p = 0 . 1% | p = 0 . 5%        | p = 1 . 0%        |
|   1 | π 4  | T √     | 0.50 0.50              | 0.48              | 0.47              |
|   2 | π 8  | T √     | 1.04 1.00              | 0.87              | 0.74              |
|   4 | π 16 | 4 T √   | 2.07 1.78              | 1.09              | 0.73              |
|   8 | π 32 | 8 T     | 3.91 2.37              | 0.85              | 0.46              |

As shown in Table II, the MMD method is able to achieve a better-than-quadratic advantage for p = 0 . 1% dephasing noise with respect to the stabilizer extent. Meanwhile for higher dephasing noise, our method provides comparable performance with a slight increase in magic resource for p = 1 . 0%.

## IV. FERMI-HUBBARD MODEL SIMULATION

The Fermi-Hubbard model describes the behaviour of interacting electrons in 2D materials. The Hubbard Hamiltonian is composed of hopping terms H h which represent the kinetic energy of electrons that can tunnel between neighbouring lattice sites, and interaction terms H i which represent the potential energy due to the onsite repulsion of electrons. For this analysis, we consider H i subject to a chemical potential shift as per Ref. [6]. The resulting Hamiltonian takes the form

̸

$$H & = H _ { h } + H _ { i } \\ & = \sum _ { \sigma \in \uparrow , \downarrow } \sum _ { i \neq j } R _ { i , j } a _ { i , \sigma } ^ { \dagger } a _ { j , \sigma } + \frac { u } { 4 } \sum _ { i } \hat { z } _ { i , \uparrow } \hat { z } _ { i , \downarrow } \\$$

where a, a † are the creation and annihilation operators respectively, u is the repulsive interaction strength between spin-up and spin-down electrons at each site, and ˆ z is related to the number operator ˆ n = a † a by ˆ z = (2ˆ n -✶ ). The hopping strength is defined as R i,j = τ if i, j are nearest-neighbour lattice sites, allowing electrons to tunnel between adjacent sites, and R i,j = 0 otherwise. We choose parameters that lie within the regime widely considered to be classically challenging for simulation [6, 42]. As such, we set u/τ = 8 and consider 2D square lattices of size L × L with L ∈ { 4 , 6 , 8 } . The total number of spin orbitals is given by N = 2 L 2 .

To estimate the resource requirements for simulating the Fermi-Hubbard model using MMD, we employ the Fermionic swap network Trotter step algorithm to implement a second-order Trotterisation of the system, follow- ing Ref. [51]. We determine the number of rotations and corresponding angle of rotations required for each secondorder Trotter step. Specifically, for r Trotter steps, N h = 8 Nr arbitrary rotations of angle θ h = τt/ 4 r are needed to simulate the hopping terms, while N i = Nr/ 2 arbitrary rotations of angle θ i = ut/ 4 r are required to simulate the interaction terms. This makes use of a slight improvement upon Ref. [51] due to the shifted form of the interaction Hamiltonian [6].

FIG. 6. Number of samples ( N sample ) required to perform MMD for the second-order Trotterised time evolution of the 2D Fermi-Hubbard model in the limit of large (10 6 ) Trotter steps.

<!-- image -->

From this, we calculate the number of magic states required per sample as

$$N _ { m } = N _ { h } E _ { h } + N _ { i } E _ { i } ,$$

where the number of magic states E h ( i ) (per sample) for each rotation is given by

$$E _ { h ( i ) } = \left ( 2 - \frac { 1 } { n } \right ) \frac { \left | x _ { n } \right | } { \Lambda _ { \mathcal { G } } ( \mathcal { R } _ { z } ^ { \theta _ { h ( i ) } } ) }$$

in analogy to Eq. (25).

The total number of samples ( N sample ) is calculated from Hoeffding's inequality to be

$$\mathbb { I } ) . \quad & \quad N _ { \text {sample} } = \frac { 2 \ln ( 2 / \delta ) } { \epsilon _ { \text {sample,EM} } ^ { 2 } } \left [ ( \Lambda _ { \mathcal { G } } ( \mathcal { R } _ { z } ^ { \theta _ { h } } ) ) ^ { 2 N _ { h } } ( \Lambda _ { \mathcal { G } } ( \mathcal { R } _ { z } ^ { \theta _ { i } } ) ) ^ { 2 N _ { i } } \right ] . \\ \text {We}$$

Here we take the probability of error mitigation failing, δ to be 0 . 01 and the error bound for failure mitigation ϵ sample , EM to be 0 . 02. The total number of magic states over all samples then becomes

$$N _ { t o t a l } = N _ { m } \times N _ { s a m p l e } .$$

Considering the exponential scaling of the sampling overhead, we first evaluate the total number of samples for which our framework is practically feasible as a function of the evolution time t . We assume a dephasing noise of p = 0 . 1% throughout the analysis in this section. In the limit of large Trotter steps for the MMD method, the number of samples for a lattice size of L = 6 scales with t as per Fig. 6.

FIG. 7. Number of magic states over all samples ( N total ) to perform MMD for the second-order Trotterised time evolution of the 2D Fermi-Hubbard model compared to gate synthesis. Results are shown for an L × L lattice with L ∈ { 4 , 6 , 8 } .

<!-- image -->

We see that a purely classical implementation of our MMD method (for which n = 0 . 5) requires 10 70 samples to simulate t = 0 . 35, whereas a quantum implementation of our method (so n ≥ 1) requires from 10 31 to 10 7 samples as n increases. We also overlay the upper-bounded runtime scaling of the stabilizer extent method with precision ϵ = 0 . 01 in Fig. 6.

We finally present a representative comparison of this framework with direct gate synthesis methods. Asymptotically optimal unitary synthesis is possible using the Ross-Selinger method [29] with improvements possible by employing random compiling as shown in Ref. [52]. Adding an ancillary qubit, mixed fallback techniques [53, 54] obtain the best T -count known to date:

$$T _ { \text {synth} } = 0 . 5 3 \log _ { 2 } \left ( \frac { \ N _ { R } } { \epsilon _ { \text {synth} } } \right ) + 4 . 8 6 , \quad ( 3 3 ) \quad \begin{smallmatrix} \text {include} & & \text {include} \\ & & \\ & & \text {angle} \\ & & \text {angle} \end{smallmatrix}$$

where N R = N h + N i is the total number of rotations.

To ensure a fair comparison, we allow an error budget of ϵ synth + ϵ trotter = 0 . 01, a favourable sampling error ϵ sample , RS = 0 . 01, and N sample is a constant. Here, ϵ trotter = W FS t 3 /s 2 is the Trotter error for the Fermionic swap network algorithm, taking W FS values from Ref. [51]. From this, we optimise the number of required Trotter steps s that minimise N R T synth for gate synthesis.

In Fig. 7, we see that the MMD method provides a significant reduction in the magic state count for very small t , for all cases of n . Smaller lattice sizes see up to a few orders of magnitude saving and could provide an advantage for longer t compared to direct gate synthesis. To achieve the same advantage as the lattice size and evolution time increases, MMD requires gates from higher levels (larger n ) of the Clifford hierarchy as shown. In particular, for L = 4 , 6 and 8, MMD presents at least an order of magnitude resource saving for time evolution up to 0.8, 0.35 and 0.2 respectively.

## V. DISCUSSION AND CONCLUSIONS

In this paper, we have presented our mitigated magic dilution framework for implementing small-angle singlequbit Z -rotations, making use of error mitigation to provide an advantage in terms of the sampling overhead when benchmarked against a classical approach.

We have further identified a use-case of mitigated magic dilution for simulating time evolution of the FermiHubbard Hamiltonian using Trotterisation. Through this, we have demonstrated a resource benefit of implementing mitigated magic dilution over conventional direct synthesis when taking into account the number of magic states and sampling overhead. Thus, our framework is suitable for early fault-tolerant quantum computers. Broadly speaking, our approach is more advantageous for algorithms containing a large number of very small angle rotations, such as Trotterised simulations. Our work hints towards a wide variety of directions for future work when larger angle rotations are encountered, including hybrid approaches with MMD used for small angles and synthesis used for larger angles, and hybrid approaches where the gate set G used in MMD includes partially synthesised rotations.

A key assumption we have made in our MMD method is that all magic states are prepared with the same fidelity. Consequently, we observed optimal performance at some finite level of the Clifford hierarchy, fixed by the fidelity. However, recent literature indicates that this can be improved such that magic states of smaller rotationsand therefore gates higher in the Clifford hierarchy-can be prepared with a lower logical error rate [8, 55]. This is particularly relevant for this work as it suggests that the optimal performance will be at even higher Clifford hierarchy levels, leading to higher degrees of magic resource saving and hence speedup. Recent methods including magic state cultivation [56] to construct high fidelity | T ⟩ magic states also complement the methods we present in this paper, however further research is needed to determine the feasibility and effectiveness of applying similar techniques to other magic states such as | T 1 2 ⟩ for higher levels of the Clifford hierarchy.

It would be interesting to further analyse the resource requirements when compiling down to lattice surgery operations for particular algorithms. Since our scheme uses repeated teleportation circuits (recall Fig. 2), these can be realised with logical ZZ measurements without using Hadamard gates or patch rotations. In contrast, when using the gate synthesis approach, we require either Hadamard gates that take a long time to execute [57, 58], or a fast data block structure that comes with an additional qubit overhead compared to compact layouts [46].

The Trotterised time evolution studied in this paper lends itself well into statistical phase estimation for future work. Furthermore, we have studied the effect of single-qubit dephasing noise channels, however for specific quantum hardware, it may be worthwhile to explore other noise models. Finally, further advancements in better logical magic states as discussed earlier will improve the advantages presented in this paper.

We have compared our approach against two families of near-Clifford simulators. Clearly, there are a range of other simulators to consider, including tensor network simulators that are suited to shallow local circuits on 2D arrays of qubits [59]. However, our techniques are directly applicable to simulating systems with long-range interactions or in higher-dimensional geometries, and in such settings tensor-network methods perform poorly. Conversely, we envisage further improvements to mitigated magic dilution by extending to a dyadic decomposition approach similar to that used in some classical simulators [32].

## ACKNOWLEDGMENTS

This work was supported by the Engineering and Physical Sciences Research Council [grant numbers EP/S021582/1, EP/Y004140/1, EP/Y004310/1]. We thank Nick Blunt and Alex Gramolin for comments on the manuscript.

## Appendix A: Minimum Requirement of Three Channels

In the general case, A and b in Eq. (10) can be written in matrix form as

$$A = \begin{bmatrix} \cos ^ { 2 } ( \frac { \phi _ { 1 } } { 2 } ) & \cos ^ { 2 } ( \frac { \phi _ { 2 } } { 2 } ) & \cos ^ { 2 } ( \frac { \phi _ { 3 } } { 2 } ) & \cdots \\ \cos ( \frac { \phi _ { 1 } } { 2 } ) \sin ( \frac { \phi _ { 1 } } { 2 } ) & \cos ( \frac { \phi _ { 2 } } { 2 } ) \sin ( \frac { \phi _ { 2 } } { 2 } ) & \cos ( \frac { \phi _ { 3 } } { 2 } ) \sin ( \frac { \phi _ { 3 } } { 2 } ) & \cdots \\ \sin ^ { 2 } ( \frac { \phi _ { 1 } } { 2 } ) & \sin ^ { 2 } ( \frac { \phi _ { 2 } } { 2 } ) & \sin ^ { 2 } ( \frac { \phi _ { 3 } } { 2 } ) & \cdots \end{bmatrix} ,$$

$$b = \begin{bmatrix} \cos ^ { 2 } ( \frac { \theta } { 2 } ) \\ \cos ( \frac { \theta } { 2 } ) \sin ( \frac { \theta } { 2 } ) \\ \sin ^ { 2 } ( \frac { \theta } { 2 } ) . \end{bmatrix} .$$

Specifically for the two channel case, we have

$$\begin{bmatrix} \cos ^ { 2 } ( \frac { \phi _ { 1 } } { 2 } ) & \cos ^ { 2 } ( \frac { \phi _ { 2 } } { 2 } ) \\ \cos ( \frac { \phi _ { 1 } } { 2 } ) \sin ( \frac { \phi _ { 1 } } { 2 } ) & \cos ( \frac { \phi _ { 2 } } { 2 } ) \sin ( \frac { \phi _ { 2 } } { 2 } ) \\ \sin ^ { 2 } ( \frac { \phi _ { 1 } } { 2 } ) & \sin ^ { 2 } ( \frac { \phi _ { 2 } } { 2 } ) \end{bmatrix} \begin{bmatrix} x _ { 1 } \\ x _ { 2 } \end{bmatrix} = \begin{bmatrix} \cos ^ { 2 } ( \frac { \theta } { 2 } ) \\ \cos ( \frac { \theta } { 2 } ) \sin ( \frac { \theta } { 2 } ) \end{bmatrix}$$

from which we write three simultaneous equations:

$$x _ { 1 } \cos ^ { 2 } \left ( \frac { \phi _ { 1 } } { 2 } \right ) + x _ { 2 } \cos ^ { 2 } \left ( \frac { \phi _ { 2 } } { 2 } \right ) = \cos ^ { 2 } \left ( \frac { \theta } { 2 } \right ) ,$$

$$x _ { 1 } \cos \left ( \frac { \phi _ { 1 } } { 2 } \right ) \sin \left ( \frac { \phi _ { 1 } } { 2 } \right ) + x _ { 2 } \cos \left ( \frac { \phi _ { 2 } } { 2 } \right ) \sin \left ( \frac { \phi _ { 2 } } { 2 } \right ) = \cos \left ( \frac { \theta } { 2 } \right ) \sin \left ( \frac { \theta } { 2 } \right ) ,$$

$$x _ { 1 } \sin ^ { 2 } \left ( \frac { \phi _ { 1 } } { 2 } \right ) + x _ { 2 } \sin ^ { 2 } \left ( \frac { \phi _ { 2 } } { 2 } \right ) = \sin ^ { 2 } \left ( \frac { \theta } { 2 } \right ) .$$

Upon solving Eq. (A4a) and Eq. (A4c), we obtain

$$x _ { 1 } + x _ { 2 } = 1 ,$$

and which arises due to the unitarity of the channels. From this, we can find two solutions for x 1 by substituting this into Eq. (A4a) and Eq. (A4b) respectively, resulting in

$$x _ { 1 } = & \frac { \cos ( ( \theta + \phi _ { 1 } ) / 2 ) \sin ( ( \theta + \phi _ { 2 } ) / 2 ) } { \cos ( ( \phi _ { 1 } + \phi _ { 2 } ) / 2 ) \sin ( ( \phi _ { 1 } + \phi _ { 2 } ) / 2 ) } \\ = & \frac { \sin ( ( \theta + \phi _ { 1 } ) / 2 ) \sin ( ( \theta + \phi _ { 2 } ) / 2 ) } { \sin ( ( \phi _ { 1 } + \phi _ { 2 } ) / 2 ) \sin ( ( \phi _ { 1 } + \phi _ { 2 } ) / 2 ) } .$$

Therefore all three equations in this overdetermined system are only satisfied when

$$\phi _ { 1 } = \theta + 2 k \pi \Rightarrow x _ { 1 } = 1 , x _ { 2 } = 0$$

$$\phi _ { 2 } = \theta + 2 k \pi \Rightarrow x _ { 1 } = 0 , x _ { 2 } = 1 ,$$

where k ∈ Z , i.e., the trivial case of only a single channel in the decomposition. So, for multiple channels in the decomposition, at least three channels are required.

## Appendix B: LCC Decomposition for {I , T 1 n , Z} Channels

In the main text, we showed that the optimal decompositions found using convex optimisation were of the form {I , T 1 n , Z} for both ideal and noisy T 1 n channels. In the following sections, we derive the l 1 -norm and γ corresponding to these optimal decompositions.

## 1. Ideal Case

A T 1 n channel can be written as a Z -rotation channel with rotation angle ϕ ,

$$\mathcal { R } _ { z } ^ { \phi } ( \rho ) & = e ^ { - i \frac { \phi } { 2 } Z } \rho e ^ { i \frac { \phi } { 2 } Z } \\ & = \cos ^ { 2 } \left ( \frac { \phi } { 2 } \right ) \rho + \sin ^ { 2 } \left ( \frac { \phi } { 2 } \right ) Z \rho Z + i \cos \left ( \frac { \phi } { 2 } \right ) \sin \left ( \frac { \phi } { 2 } \right ) [ \rho Z - Z \rho ] ,$$

where ϕ = π 4 n . Recall that n = 2 i -1 where i ∈ Z ≥ 0 such that i = 0 is the S channel, i = 1 is the T channel, etc. For an LCC decomposition in terms of {I , R ϕ z , Z} channels, we obtain

$$\mathcal { R } _ { z } ^ { \theta } ( \rho ) & = x _ { 0 } \mathcal { I } ( \rho ) + x _ { 1 } \mathcal { R } _ { z } ^ { \phi } ( \rho ) + x _ { 2 } \mathcal { Z } ( \rho ) \\ & = x _ { 0 } \rho + x _ { 1 } \left ( \cos ^ { 2 } \left ( \frac { \phi } { 2 } \right ) \rho + i \cos \left ( \frac { \phi } { 2 } \right ) \sin \left ( \frac { \phi } { 2 } \right ) \left [ \rho Z - Z \rho \right ] + \sin ^ { 2 } \left ( \frac { \phi } { 2 } \right ) Z \rho Z \right ) + x _ { 2 } Z \rho Z \\ & = \left ( x _ { 0 } + \cos ^ { 2 } \left ( \frac { \phi } { 2 } \right ) x _ { 1 } \right ) \rho + i \cos \left ( \frac { \phi } { 2 } \right ) \sin \left ( \frac { \phi } { 2 } \right ) x _ { 1 } [ \rho Z - Z \rho ] + \left ( \sin ^ { 2 } \left ( \frac { \phi } { 2 } \right ) x _ { 1 } + x _ { 2 } \right ) Z \rho Z \\ & = \cos ^ { 2 } \left ( \frac { \theta } { 2 } \right ) \rho + i \cos \left ( \frac { \theta } { 2 } \right ) \sin \left ( \frac { \theta } { 2 } \right ) [ \rho Z - Z \rho ] + \sin ^ { 2 } \left ( \frac { \theta } { 2 } \right ) Z \rho Z . \\ \intertext { The o f f i c t i o n s r . g e n b o d e r m a n d y s l o w t h e s u m p l u t a n e c o u s i n c t i o n s }$$

The coefficients x i can be determined by solving three simultaneous equations:

$$x _ { 0 } + \cos ^ { 2 } \left ( \frac { \phi } { 2 } \right ) x _ { 1 } = \cos ^ { 2 } \left ( \frac { \theta } { 2 } \right ) ,$$

$$\cos \left ( \frac { \phi } { 2 } \right ) \sin \left ( \frac { \phi } { 2 } \right ) x _ { 1 } = \cos \left ( \frac { \theta } { 2 } \right ) \sin \left ( \frac { \theta } { 2 } \right ) ,$$

$$\sin ^ { 2 } \left ( \frac { \phi } { 2 } \right ) x _ { 1 } + x _ { 2 } = \sin ^ { 2 } \left ( \frac { \theta } { 2 } \right ) ,$$

or with solutions given by

$$x _ { 0 } = \cos ^ { 2 } \left ( \frac { \theta } { 2 } \right ) - \left ( \frac { \sin ( \theta ) } { \sin ( \phi ) } \right ) \cos ^ { 2 } \left ( \frac { \phi } { 2 } \right ) ,$$

$$x _ { 1 } = \frac { \sin ( \theta ) } { \sin ( \phi ) } ,$$

$$x _ { 2 } = \sin ^ { 2 } \left ( \frac { \theta } { 2 } \right ) - \left ( \frac { \sin ( \theta ) } { \sin ( \phi ) } \right ) \sin ^ { 2 } \left ( \frac { \phi } { 2 } \right ) .$$

The l 1 -norm of this decomposition for target rotation angles 0 ≤ θ ≤ ϕ is

$$The \eta _ { 1 } \text {norm of this decomposition for target rotation angles } 0 \leq \theta \leq \Phi \, I s \\ \Lambda _ { \mathcal { G } } ( \mathcal { R } _ { z } ^ { \theta } ) = | x _ { 0 } | + | x _ { 1 } | + | x _ { 2 } | \\ = \left | \cos ^ { 2 } \left ( \frac { \theta } { 2 } \right ) - \left ( \frac { \sin ( \theta ) } { \sin ( \phi ) } \right ) \cos ^ { 2 } \left ( \frac { \phi } { 2 } \right ) \right | + \left | \frac { \sin ( \theta ) } { \sin ( \phi ) } \right | + \left | \sin ^ { 2 } \left ( \frac { \theta } { 2 } \right ) - \left ( \frac { \sin ( \theta ) } { \sin ( \phi ) } \right ) \sin ^ { 2 } \left ( \frac { \phi } { 2 } \right ) \right | \\ = \cos ^ { 2 } \left ( \frac { \theta } { 2 } \right ) - \left ( \frac { \sin ( \theta ) } { \sin ( \phi ) } \right ) \cos ^ { 2 } \left ( \frac { \phi } { 2 } \right ) + \frac { \sin ( \theta ) } { \sin ( \phi ) } - \sin ^ { 2 } \left ( \frac { \theta } { 2 } \right ) + \left ( \frac { \sin ( \theta ) } { \sin ( \phi ) } \right ) \sin ^ { 2 } \left ( \frac { \phi } { 2 } \right ) \\ = \cos ( \theta ) + \frac { \sin ( \theta ) } { \sin ( \phi ) } \left ( 1 - \cos ( \phi ) \right ) . \\$$

noting that x 2 ≤ 0 while x 0 , x 1 ≥ 0 for this range of θ .

For small rotation angles θ , we approximate

$$\Lambda _ { \theta } ( \mathcal { R } _ { z } ^ { \theta } ) & = \cos ( \theta ) + \sin ( \theta ) \left ( \frac { 1 - \cos ( \phi ) } { \sin ( \phi ) } \right ) \\ & \approx 1 - \frac { \theta ^ { 2 } } { 2 } + \theta \left ( \frac { 1 - \cos ( \phi ) } { \sin ( \phi ) } \right ) \\ & \approx 1 + \theta \left ( \frac { 1 - \cos ( \phi ) } { \sin ( \phi ) } \right ) .$$

Thus γ in Eq. (14) is obtained as follows

$$d \text { as follows} \\ \gamma ( \theta ) = \frac { \ln ( \Lambda c ( \mathcal { R } _ { z } ^ { \theta } ) ) } { \ln ( \Lambda g ( \mathcal { R } _ { z } ^ { \theta } ) ) } \\ = \frac { \ln \left ( 1 + \theta \right ) } { \ln \left ( 1 + \theta \left ( \frac { 1 - \cos ( \phi ) } { \sin ( \phi ) } \right ) \right ) } \\ \approx \frac { \theta } { \left ( \frac { 1 - \cos ( \phi ) } { \sin ( \phi ) } \right ) \theta } \\ = \frac { \sin ( \phi ) } { 1 - \cos ( \phi ) } = \cot \left ( \frac { \phi } { 2 } \right ) .$$

## 2. Dephased T 1 n Case

We consider a dephasing noise channel as given by Eq. (21). In the main text, we define an effective dephasing noise p eff , which we use in the following derivation.

The dephasing noise channel can applied to R ϕ z as follows:

$$\varepsilon ( \mathcal { R } _ { z } ^ { \phi } ( \rho ) ) = & ( 1 - p _ { \text {eff} } ) ( \mathcal { R } _ { z } ^ { \phi } ( \rho ) ) + p _ { \text {eff} } Z ( \mathcal { R } _ { z } ^ { \phi } ( \rho ) ) Z \\ = & \left [ \cos ^ { 2 } \left ( \frac { \phi } { 2 } \right ) - p _ { \text {eff} } \cos ( \phi ) \right ] \rho + ( 1 - 2 p _ { \text {eff} } ) \left [ i \cos \left ( \frac { \phi } { 2 } \right ) \sin \left ( \frac { \phi } { 2 } \right ) \right ] [ \rho Z - Z \rho ] \\ & + \left [ \sin ^ { 2 } \left ( \frac { \phi } { 2 } \right ) + p _ { \text {eff} } \cos ( \phi ) \right ] Z \rho Z .$$

The LCC decomposition of the R θ z ( ρ ) channel in terms of {I , ε ( R ϕ z ) , Z} is given by

$$The LCC decomposition of the \mathcal { R } _ { z } ^ { \rho } ( \rho ) \text { channel in terms of } \{ I , \varepsilon ( \mathcal { R } _ { z } ^ { \phi } ) , Z \} \text { is given by} \\ \mathcal { R } _ { z } ^ { \rho } ( \rho ) & + x _ { 0 } \mathcal { I } ( \rho ) + x _ { 1 } \varepsilon ( \mathcal { R } _ { z } ^ { \phi } ( \rho ) ) + x _ { 2 } Z ( \rho ) \\ & = x _ { 0 } \rho + x _ { 1 } \left [ \left [ \cos ^ { 2 } \left ( \frac { \phi } { 2 } \right ) - p _ { e f f } \cos ( \phi ) \right ] \rho + ( 1 - 2 p _ { e f f } ) \left [ i \cos \left ( \frac { \phi } { 2 } \right ) \sin \left ( \frac { \phi } { 2 } \right ) \right ] [ \rho Z - Z \rho ] \\ & + \left [ \sin ^ { 2 } \left ( \frac { \phi } { 2 } \right ) + p _ { e f f } \cos ( \phi ) \right ] Z \rho Z \right ] + x _ { 2 } Z \rho Z \\ & = \left ( x _ { 0 } + \left [ \cos ^ { 2 } \left ( \frac { \phi } { 2 } \right ) - p _ { e f f } \cos ( \phi ) \right ] x _ { 1 } \right ) \rho + i ( 1 - 2 p _ { e f f } ) \cos \left ( \frac { \phi } { 2 } \right ) \sin \left ( \frac { \phi } { 2 } \right ) x _ { 1 } [ \rho Z - Z \rho ] \\ & + \left ( \left [ \sin ^ { 2 } \left ( \frac { \phi } { 2 } \right ) + p _ { e f f } \cos ( \phi ) \right ] x _ { 1 } + x _ { 2 } \right ) Z \rho Z \\ & = \cos ^ { 2 } \left ( \frac { \theta } { 2 } \right ) \rho + i \cos \left ( \frac { \theta } { 2 } \right ) \sin \left ( \frac { \theta } { 2 } \right ) [ \rho Z - Z \rho ] + \sin ^ { 2 } \left ( \frac { \theta } { 2 } \right ) Z \rho Z \\ \intertext { The coefficients } \text { the coefficients } x _ { 1 } \text { can be determined by solving three simultaneous equations} .$$

The coefficients x i can be determined by solving three simultaneous equations:

$$x _ { 0 } + \left [ \cos ^ { 2 } \left ( \frac { \phi } { 2 } \right ) - p _ { \text {eff} } \cos \left ( \phi \right ) \right ] x _ { 1 } = \cos ^ { 2 } \left ( \frac { \theta } { 2 } \right ) ,$$

$$( 1 - 2 p _ { e f f } ) \cos \left ( \frac { \phi } { 2 } \right ) \sin \left ( \frac { \phi } { 2 } \right ) x _ { 1 } = \cos \left ( \frac { \theta } { 2 } \right ) \sin \left ( \frac { \theta } { 2 } \right ) ,$$

$$\left [ \sin ^ { 2 } \left ( \frac { \phi } { 2 } \right ) + p _ { e f f } \cos \left ( \phi \right ) \right ] x _ { 1 } + x _ { 2 } = \sin ^ { 2 } \left ( \frac { \theta } { 2 } \right ) .$$

$$x _ { 0 } = \cos ^ { 2 } \left ( \frac { \theta } { 2 } \right ) - \left [ \cos ^ { 2 } \left ( \frac { \phi } { 2 } \right ) - p _ { e f f } \cos ( \phi ) \right ] \frac { \sin ( \theta ) } { ( 1 - 2 p _ { e f f } ) \sin ( \phi ) }$$

$$x _ { 1 } = \frac { \sin ( \theta ) } { ( 1 - 2 p _ { \text {eff} } ) \sin ( \phi ) } & & ( B 1 0 b )$$

$$x _ { 2 } = \sin ^ { 2 } \left ( \frac { \theta } { 2 } \right ) - \left [ \sin ^ { 2 } \left ( \frac { \phi } { 2 } \right ) + p _ { e f f } \cos \left ( \phi \right ) \right ] \frac { \sin ( \theta ) } { ( 1 - 2 p _ { e f f } ) \sin ( \phi ) } .$$

The l 1 -norm of this decomposition is

$$The l _ { 1 } n o r m o f i s \, \text { decomposition is} \\ & \Lambda g ( \mathcal { R } _ { 2 } ^ { \theta } ) = | x _ { 0 } | + | x _ { 1 } | + | x _ { 2 } | \\ & = \left | \cos ^ { 2 } \left ( \frac { \theta } { 2 } \right ) - \left [ \cos ^ { 2 } \left ( \frac { \phi } { 2 } \right ) - p _ { e f f } \cos \left ( \phi \right ) \right ] \frac { \sin ( \theta ) } { ( 1 - 2 p e f t ) \sin ( \phi ) } \right | + \left | \frac { \sin ( \theta ) } { ( 1 - 2 p e f t ) \sin ( \phi ) } \right | \\ & + \left | \sin ^ { 2 } \left ( \frac { \theta } { 2 } \right ) - \left [ \sin ^ { 2 } \left ( \frac { \phi } { 2 } \right ) + p _ { e f f } \cos \left ( \phi \right ) \right ] \frac { \sin ( \theta ) } { ( 1 - 2 p e f t ) \sin ( \phi ) } \right | \\ & = \cos ^ { 2 } \left ( \frac { \theta } { 2 } \right ) - \left [ \cos ^ { 2 } \left ( \frac { \phi } { 2 } \right ) - p _ { e f f } \cos \left ( \phi \right ) \right ] \frac { \sin ( \theta ) } { ( 1 - 2 p e f t ) \sin ( \phi ) } + \frac { \sin ( \theta ) } { ( 1 - 2 p e f t ) \sin ( \phi ) } \left ( B 1 \right ) \\ & - \sin ^ { 2 } \left ( \frac { \theta } { 2 } \right ) + \left [ \sin ^ { 2 } \left ( \frac { \phi } { 2 } \right ) + p _ { e f f } \cos \left ( \phi \right ) \right ] \frac { \sin ( \theta ) } { ( 1 - 2 p e f t ) \sin ( \phi ) } \\ & = \cos \left ( \theta \right ) - \frac { \sin ( \theta ) } { ( 1 - 2 p e f t ) \sin ( \phi ) } \left ( ( 1 - 2 p e f t ) \cos \left ( \phi \right ) - 1 \right ) \\ & = \cos \left ( \theta \right ) + \sin ( \theta ) \left ( \frac { 1 } { ( 1 - 2 p e f t ) } \csc \left ( \phi \right ) - \cot \left ( \phi \right ) \right ) .$$

with solutions given by for target rotation angles 0 ≤ θ ≪ ϕ . For small θ , we can approximate

$$\Lambda _ { \mathcal { G } } ( \mathcal { R } _ { z } ^ { \theta } ) & = \cos ( \theta ) + \sin ( \theta ) \left ( \frac { 1 } { ( 1 - 2 p _ { e f f } ) } \csc ( \phi ) - \cot ( \phi ) \right ) \\ & \approx 1 - \frac { \theta ^ { 2 } } { 2 } + \theta \left ( \frac { 1 } { ( 1 - 2 p _ { e f f } ) } \csc ( \phi ) - \cot ( \phi ) \right ) \\ & \approx 1 + \theta \left ( \frac { 1 } { ( 1 - 2 p _ { e f f } ) } \csc ( \phi ) - \cot ( \phi ) \right ) .$$

$$\gamma ( \theta ) & = \frac { \ln ( \Lambda _ { c } ( \mathcal { R } _ { z } ^ { \theta } ) ) } { \ln ( \Lambda _ { g } ( \mathcal { R } _ { z } ^ { \theta } ) ) } \\ & = \frac { \ln \left ( 1 + \theta \left ( \frac { 1 } { ( 1 - 2 p _ { e f t } ) } \csc \left ( \phi \right ) - \cot \left ( \phi \right ) \right ) \right ) } { \theta } \\ & \approx \frac { \theta } { \theta \left ( \frac { 1 } { ( 1 - 2 p _ { e f t } ) } \csc \left ( \phi \right ) - \cot \left ( \phi \right ) \right ) } \\ & = \frac { 1 } { \frac { \csc \left ( \phi \right ) } { ( 1 - 2 p _ { e f t } ) } - \cot \left ( \phi \right ) } .$$

## Appendix C: Noise in Generalised Gate Teleportation Circuit

We can show that the generalised gate teleportation circuit in Fig. 2 results in a rotation that differs from the target rotation θ by either dephasing noise, or coherent errors. We note that coherent errors can be handled through calibration, and accurate calibration is an underlying assumption required for the estimation of the level of dephasing noise present.

We proceed by considering a single step of generalised teleportation with noisy states as shown in Fig. 8.

FIG. 8. A single step of generalised teleportation when the magic state used is an arbitrary mixed state σ n . The outcome of the measurement is denoted m such that the correction is applied if m = 1 (eigenvalue is -1).

<!-- image -->

The state σ n will have an eigenvalue decomposition

$$\sigma _ { n } = | \phi _ { 0 } \rangle \langle \phi _ { 0 } | + | \phi _ { 1 } \rangle \langle \phi _ { 1 } |$$

where | ϕ j ⟩ are not individually normalised, but ⟨ ϕ 0 | ϕ 0 ⟩ + ⟨ ϕ 1 | ϕ 1 ⟩ = 1. It is a common assumption to take | ϕ 0 ⟩ = √ 1 -p | n √ T † ⟩ and | ϕ 1 ⟩ as its orthogonal partner. However, the purpose of this appendix is to allow for a fully general σ n .

After measurement outcome m , ρ gets mapped to

$$\mathcal { E } _ { m } ( \rho ) = \kappa _ { 0 , m } \rho \kappa _ { 0 , m } ^ { \dagger } + \kappa _ { 1 , m } \rho \kappa _ { 1 , m } ^ { \dagger } ,$$

where κ j,m is the Kraus operator corresponding to teleportation using a pure state | ϕ j ⟩ after measurement outcome

Therefore, γ becomes m . Denoting | ϕ j ⟩ = A j | 0 ⟩ + B j | 1 ⟩ , calculating the action of the teleportation circuit one finds

$$\kappa _ { 0 , 0 } = A _ { 0 } | 0 \rangle \langle 0 | + B _ { 0 } | 1 \rangle \langle 1 | = \left ( \frac { A _ { 0 } + B _ { 0 } } { 2 } \right ) I + \left ( \frac { A _ { 0 } - B _ { 0 } } { 2 } \right ) Z ,$$

$$\kappa _ { 0 , 1 } = A _ { 0 } | 1 \rangle \langle 1 | + B _ { 0 } | 0 \rangle \langle 0 | = \left ( \frac { A _ { 0 } + B _ { 0 } } { 2 } \right ) I + \left ( \frac { - A _ { 0 } + B _ { 0 } } { 2 } \right ) Z ,$$

$$\kappa _ { 1 , 0 } = A _ { 1 } | 0 \rangle \langle 0 | + B _ { 1 } | 1 \rangle \langle 1 | = \left ( \frac { A _ { 1 } + B _ { 1 } } { 2 } \right ) I + \left ( \frac { A _ { 1 } - B _ { 1 } } { 2 } \right ) Z ,$$

$$\kappa _ { 1 , 1 } = A _ { 1 } | 1 \rangle \langle 1 | + B _ { 1 } | 0 \rangle \langle 0 | = \left ( \frac { A _ { 1 } + B _ { 1 } } { 2 } \right ) I + \left ( \frac { - A _ { 1 } + B _ { 1 } } { 2 } \right ) Z$$

and so every relevant Kraus operator is diagonal in the Z -basis. Therefore, expanding out the channel we find that

$$\mathcal { E } _ { m } ( \rho ) = E _ { 0 , 0 } ^ { m } \rho + E _ { 0 , 1 } ^ { m } \rho Z + E _ { 1 , 0 } ^ { m } Z \rho + E _ { 1 , 1 } ^ { m } Z \rho Z .$$

where E m k,ℓ are numbers depending on A 0 , A 1 , B 0 , A 1 that in turn depend on σ n .

We are not quite done because in the case where m = 1, we need to apply a correction (i.e. using a magic state from one level lower in the Clifford hierarchy σ n/ 2 ). Nonetheless, this correction process will also perform diagonal Kraus operators, and since the group of diagonal operators is closed in multiplication, we conclude that generalised teleportation with result in some channel E that is a sum of diagonal Kraus operators. Expanding these out in the Pauli basis, we will again have an expression of the form

$$\mathcal { E } ( \rho ) = E _ { 0 , 0 } \rho + E _ { 0 , 1 } \rho Z + E _ { 1 , 0 } Z \rho + E _ { 1 , 1 } Z \rho Z ,$$

where E i,j depend on the density matrices of all magic states { σ n , σ n/ 2 , σ n/ 4 , . . . , σ 1 } in the generalised teleportation circuit. This means a large number of parameters are involved, but fortunately we can proceed with our proof using only the form of Eq. (C5) and the following observation: once all corrections are completed (we mix over all measurement outcomes) the full channel E must be CPTP. Note that, in contrast, each component E m will be completely positive (CP) but not necessarily trace preserving (TP). Therefore, under the Choi-Jamioglyph[suppress] lkowski isomorphism, the Choi state for this channel must be a physical density matrix (Hermitian, positive semi-definite and trace normalized to unity). Furthermore, due to the form of Eq. (C5), the Choi state has the form

$$\Phi _ { \varepsilon } = ( \mathcal { E } \otimes \mathcal { I } ) ( | \Phi \rangle \langle \Phi | ) = \left ( \begin{array} { c c c } a _ { 0 , 0 } & 0 & 0 & a _ { 0 , 1 } \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ a _ { 1 , 0 } & 0 & 0 & a _ { 1 , 1 } \end{array} \right ) .$$

where for instance a 1 , 1 = ( E 0 , 0 -E 0 , 1 -E 1 , 0 + E 1 , 1 ) / 2. In particular, the Choi state has at most 2 non-zero eigenvalues, and by the CPTP property we can denote these as p and 1 -p (with 1 ≤ p ≤ 0), so they can be interpreted as probabilities. Therefore,

$$\Phi _ { \mathcal { E } } = p | K _ { 0 } \rangle \langle K _ { 0 } | + ( 1 - p ) | K _ { 1 } \rangle \langle K _ { 1 } |$$

where | K j ⟩ are a pair of orthogonal pure states supported on the non-trivial 2 × 2 submatrix of Eq. (C6). We may now reverse the Choi-Jamioglyph[suppress] lkowski isomorphism, so that

$$\mathcal { E } ( \rho ) = p K _ { 0 } \rho K _ { 0 } ^ { \dagger } + ( 1 - p ) K _ { 1 } \rho K _ { 1 } ^ { \dagger }$$

where K j is the single Kraus operator isomorphic to the state | K j ⟩⟨ K j | . Since the state representation is restricted to a specific submatrix, we can conclude that K j are unitary operators diagonal in the Z basis and we are free to choose the global phase. Therefore, there exists angles φ j such that K j = R z ( φ j ). Finally, since | K j ⟩ are orthogonal to each other, we can conclude that Tr[ K † 1 K 0 ] = 0. This orthogonality entails that φ 1 is such that K 1 = K 0 Z upto a global phase. This brings us to the final form

$$\mathcal { E } ( \rho ) = p \mathcal { R } _ { z } ^ { \varphi _ { 0 } } ( \rho ) + ( 1 - p ) Z \mathcal { R } _ { z } ^ { \varphi _ { 0 } } ( \rho ) Z$$

which has the claimed form of dephasing noise and potentially a coherent error which deviates from the ideal angle ϕ by a phase of δ = φ 0 -ϕ .

We have assumed throughout that physical noise is well characterized. The impact of changes in the magic states σ n affects the form of the resulting channel E . If there is a undesired coherent error, we can adjust the angle of the prepared magic state σ n to eliminate this, thereby leaving only dephasing error as assumed throughout the main text.

## Appendix D: Supplementary Data

TABLE III. ln(Λ G ( R θ z )) as a function of target rotation angle θ for different optimal decompositions of the form {I , ε ( T 1 n ) , Z} including the optimal Clifford decomposition of {I , S , Z} . The values presented here correspond to the relative values used to calculate γ in Table I.

|   n | ϕ    | R ϕ z   | ln(Λ G ( R θ z )) (Small θ )   | ln(Λ G ( R θ z )) (Small θ )   | ln(Λ G ( R θ z )) (Small θ )   |
|-----|------|---------|--------------------------------|--------------------------------|--------------------------------|
|     |      |         | p = 0 . 01%                    | p = 0 . 5%                     | p = 1 . 0%                     |
|   0 | π 2  | S       | 1.00E-07                       | 1.00E-07                       | 1.00E-07                       |
|   1 | π 4  | T √     | 4.14E-08                       | 4.28E-08                       | 4.43E-08                       |
|   2 | π 8  | T √     | 2.00E-08                       | 2.39E-08                       | 2.40E-08                       |
|   4 | π 16 | 4 T √   | 1.00E-08                       | 1.90E-08                       | 2.84E-08                       |
|   8 | π 32 | 8 T     | 5.30E-09                       | 2.44E-08                       | 4.47E-09                       |

- [1] Google Quantum AI and Collaborators, Quantum error correction below the surface code threshold, Nature 10.1038/s41586-024-08449-y (2024).
- [2] D. Bluvstein et al. , Logical quantum processor based on reconfigurable atom arrays, Nature 626 , 58 (2024).
- [3] P. S. Rodriguez et al. , Experimental Demonstration of Logical Magic State Distillation (2024), arXiv:2412.15165 [quant-ph].
- [4] [B. W. Reichardt et al. , Demonstration of quantum computation and error correction with a tesseract code (2024), arXiv:2409.04628 [quant-ph].](https://doi.org/10.48550/arXiv.2409.04628)
- [5] E. Campbell, A series of fast-paced advances in quantum error correction, Nature Reviews Physics 6 , 160 (2024).
- [6] E. T. Campbell, Early fault-tolerant simulations of the Hubbard model, Quantum Sci. Technol. 7 , 015007 (2022), arXiv:2012.09238 [quant-ph].
- [7] A. Katabarwa et al. , Early Fault-Tolerant Quantum Computing, PRX Quantum 5 , 020101 (2024).
- [8] R. Toshio, Y. Akahoshi, J. Fujisaki, H. Oshima, S. Sato, and K. Fujii, Practical quantum advantage on partially fault-tolerant quantum computer (2024), arXiv:2408.14848 [quant-ph].
- [9] J. Preskill, Beyond nisq: The megaquop machine, ACM Transactions on Quantum Computing 10.1145/3723153 (2025).
- [10] D. Gottesman, The Heisenberg Representation of Quantum Computers (1998), arXiv:quant-ph/9807006.
- [11] S. Bravyi and A. Kitaev, Universal quantum computation with ideal Clifford gates and noisy ancillas, Phys. Rev. A 71 , 022316 (2005).
- [12] D. Litinski, Magic State Distillation: Not as Costly as You Think, Quantum 3 , 205 (2019).
- [13] C. Gidney and A. G. Fowler, Efficient magic state factories with a catalyzed | CCZ ⟩ to 2 | T ⟩ transformation, Quantum 3 , 135 (2019).
- [14] A. Wills, M.-H. Hsieh, and H. Yamasaki, Constant-Overhead Magic State Distillation (2024), arXiv:2408.07764 [quant-ph].
- [15] J. O'Gorman and E. T. Campbell, Quantum computation with realistic magic-state factories, Phys. Rev. A 95 , 032338 (2017).
- [16] J. Lee, D. W. Berry, C. Gidney, W. J. Huggins, J. R. McClean, N. Wiebe, and R. Babbush, Even more efficient quantum computations of chemistry through tensor hypercontraction, PRX Quantum 2 , 030305 (2021).
- [17] [C. Gidney, How to factor 2048 bit rsa integers with less than a million noisy qubits (2025), arXiv:2505.15917 [quant-ph].](https://arxiv.org/abs/2505.15917)
- [18] T. N. Georges, M. Bothe, C. S¨ underhauf, B. K. Berntson, R. Izs´ ak, and A. V. Ivanov, Quantum simulations of chemistry in first quantization with any basis set, npj Quantum Information 11 , 55 (2025).
- [19] A. Peruzzo et al. , A variational eigenvalue solver on a photonic quantum processor, Nat Commun 5 , 4213 (2014).
- [20] R. D. Somma, Quantum eigenvalue estimation via time series analysis, New J. Phys. 21 , 123025 (2019).
- [21] L. Lin and Y. Tong, Heisenberg-Limited Ground-State Energy Estimation for Early Fault-Tolerant Quantum Computers, PRX Quantum 3 , 010318 (2022).
- [22] K. Wan, M. Berta, and E. T. Campbell, Randomized Quantum Algorithm for Statistical Phase Estimation, Phys. Rev. Lett. 129 , 030503 (2022).
- [23] N. S. Blunt et al. , Statistical phase estimation and error mitigation on a superconducting quantum processor, PRX Quantum 4 , 040341 (2023).
- [24] J. G¨ unther, F. Witteveen, A. Schmidhuber, M. Miller, M. Christandl, and A. Harrow, Phase estimation with partially randomized time evolution, arXiv preprint arXiv:2503.05647 (2025).
- [25] K. Temme, S. Bravyi, and J. M. Gambetta, Error Mitigation for Short-Depth Quantum Circuits, Phys. Rev. Lett. 119 , 180509 (2017).
- [26] Z. Cai et al. , Quantum Error Mitigation, Rev. Mod. Phys. 95 , 045005 (2023).
- [27] C. Piveteau et al. , Error Mitigation for Universal Gates on Encoded Qubits, Phys. Rev. Lett. 127 , 200505 (2021).
- [28] Y. Suzuki et al. , Quantum Error Mitigation as a Universal Error Reduction Technique: Applications from the NISQ to the Fault-Tolerant Quantum Computing Eras, PRX Quantum 3 , 010345 (2022).
- [29] N. J. Ross and P. Selinger, Optimal ancilla-free

Clifford+T approximation of z-rotations (2016), arXiv:1403.2975.

- [30] V. Veitch et al. , The resource theory of stabilizer quantum computation, New J. Phys. 16 , 013009 (2014).
- [31] M. Howard and E. Campbell, Application of a Resource Theory for Magic States to Fault-Tolerant Quantum Computing, Phys. Rev. Lett. 118 , 090501 (2017).
- [32] J. R. Seddon et al. , Quantifying Quantum Speedups: Improved Classical Simulation From Tighter Magic Monotones, PRX Quantum 2 , 010345 (2021).
- [33] J. R. Seddon and E. T. Campbell, Quantifying magic for multi-qubit operations, Proc. R. Soc. A. 475 , 20190251 (2019).
- [34] S. Bravyi et al. , Simulation of quantum circuits by lowrank stabilizer decompositions, Quantum 3 , 181 (2019).
- [35] B. Koczor, J. J. L. Morton, and S. C. Benjamin, Probabilistic Interpolation of Quantum Rotation Angles, Phys. Rev. Lett. 132 , 130602 (2024).
- [36] H. Pashayan, J. J. Wallman, and S. D. Bartlett, Estimating Outcome Probabilities of Quantum Circuits Using Quasiprobabilities, Physical Review Letters 115 , 070501 (2015).
- [37] D. Gottesman and I. L. Chuang, Demonstrating the viability of universal quantum computation using teleportation and single-qubit operations, Nature 402 , 390 (1999).
- [38] E. T. Campbell and J. O'Gorman, An efficient magic state approach to small angle rotations, Quantum Sci. Technol. 1 , 015007 (2016), arXiv:1603.04230 [quant-ph].
- [39] Y. Li, A magic state's fidelity can be superior to the operations that created it, New J. Phys. 17 , 023037 (2015).
- [40] J. Hubbard and B. H. Flowers, Electron correlations in narrow energy bands, Proceedings of the Royal Society of London. Series A. Mathematical and Physical Sciences 276 , 238 (1963).
- [41] The Hubbard model at half a century, Nature Phys 9 , 523 (2013).
- [42] C. Cade et al. , Strategies for solving the Fermi-Hubbard model on near-term quantum computers, Phys. Rev. B 102 , 235122 (2020).
- [43] E. Dagotto, Correlated electrons in high-temperature superconductors, Rev. Mod. Phys. 66 , 763 (1994).
- [44] M. Imada, A. Fujimori, and Y. Tokura, Metal-insulator transitions, Rev. Mod. Phys. 70 , 1039 (1998).
- [45] R. Babbush, J. R. McClean, M. Newman, C. Gidney, S. Boixo, and H. Neven, Focus beyond quadratic

speedups for error-corrected quantum advantage, PRX Quantum 2 , 010103 (2021).

- [46] D. Litinski, A Game of Surface Codes: Large-Scale Quantum Computing with Lattice Surgery, Quantum 3 , 128 (2019), arXiv:1808.02892 [cond-mat, physics:quant-ph].
- [47] S. Endo, S. C. Benjamin, and Y. Li, Practical Quantum Error Mitigation for Near-Future Applications, Phys. Rev. X 8 , 031027 (2018).
- [48] S. Diamond and S. Boyd, CVXPY: A Python-embedded modeling language for convex optimization, Journal of Machine Learning Research 17 , 1 (2016).
- [49] A. Agrawal, R. Verschueren, S. Diamond, and S. Boyd, A rewriting system for convex optimization problems, Journal of Control and Decision 5 , 42 (2018).
- [50] Note that if Z errors occur on both the | T ⟩ and | T 1 2 ⟩ states, then the overall effect on the T 1 2 gate is Z 2 = I , meaning this case is equivalent to no error occurring.
- [51] I. D. Kivlichan et al. , Improved Fault-Tolerant Quantum Simulation of Condensed-Phase Correlated Electrons via Trotterization, Quantum 4 , 296 (2020), arXiv:1902.10673 [quant-ph].
- [52] E. Campbell, Shorter gate sequences for quantum computing by mixing unitaries, Phys. Rev. A 95 , 042306 (2017).
- [53] V. Kliuchnikov, K. Lauter, R. Minko, A. Paetznick, and C. Petit, Shorter quantum circuits via single-qubit gate approximation, Quantum 7 , 1208 (2023).
- [54] N. Yoshioka, S. Akibue, H. Morisaki, H. Morisaki, K. Tsubouchi, and Y. Suzuki, Error crafting in mixed quantum gate synthesis, npj Quantum Information 11 , 95 (2025).
- [55] H. Choi et al. , Fault Tolerant Non-Clifford State Preparation for Arbitrary Rotations (2023), arXiv:2303.17380 [quant-ph].
- [56] C. Gidney, N. Shutty, and C. Jones, Magic state cultivation: Growing T states as cheap as CNOT gates (2024), arXiv:2409.17595 [quant-ph].
- [57] D. Horsman, A. G. Fowler, S. Devitt, and R. V. Meter, Surface code quantum computing by lattice surgery, New Journal of Physics 14 , 123011 (2012).
- [58] G. P. Geh´ er et al. , Error-corrected Hadamard gate simulated at the circuit level, Quantum 8 , 1394 (2024).
- [59] S. Boixo, S. V. Isakov, V. N. Smelyanskiy, R. Babbush, N. Ding, Z. Jiang, M. J. Bremner, J. M. Martinis, and H. Neven, Characterizing quantum supremacy in nearterm devices, Nature Physics 14 , 595 (2018).