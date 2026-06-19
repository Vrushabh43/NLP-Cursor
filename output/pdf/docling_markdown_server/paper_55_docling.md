## Quantum EigenGame for excited state calculation

David Quiroga ∗ , Jason Han, Anastasios Kyrillidis Computer Science, Rice University and Ken Kennedy Institute daq3@rice.edu, jh146@rice.edu, anastasios@rice.edu

Computing the excited states of a given Hamiltonian is computationally hard for large systems, but methods that do so using quantum computers scale tractably. This problem is equivalent to the PCA problem where we are interested in decomposing a matrix into a collection of principal components. Classically, PCA is a wellstudied problem setting, for which both centralized and distributed approaches have been developed. On the distributed side, one recent approach is that of EigenGame, a game-theoretic approach to finding eigenvectors where each eigenvector reaches a Nash equilibrium either sequentially or in parallel. With this work, we extend the EigenGame algorithm for both a 0 th -order approach and for quantum computers, and harness the framework that quantum computing provides in computing excited states. Results show that using the Quantum EigenGame allows us to converge to excited states of a given Hamiltonian without the need of a deflation step. We also develop theory on error accumulation for finite-differences and parameterized approaches.

## 1. Introduction

Quantum computing offers an alternative approach to solving complex computational tasks, potentially reducing the time and space complexity compared to classical methods. Quantum algorithms -like Quantum Phase Estimation [1], the Deutsch-Jozsa algorithm [2], and Grover's algorithm [3]- demonstrate superior performance in ideal, noiseless conditions. However, in the Noisy Intermediate-Scale Quantum (NISQ) era [4], noise remains a significant challenge, influencing the stability and reliability of quantum computations [5-8].

Performing optimization tasks under noisy settings is a common scenario in the algorithmic literature. In optimization and machine learning, errors that propagate throughout iterations critically influence performance metrics and outcomes [9-12]. Understanding and mitigating error propagation is crucial for enhancing the practical utility of algorithms in real-world applications.

Particularly relevant to the present work, consider the case of derivative-free optimization (DFO) [13-18]: DFO is employed effectively in scenarios where traditional gradient-based methods falter [16]. However, the efficiency of DFO methods often lags, particularly for high-dimensional problems, due to their reliance on sampling routines that may require many function evaluations to approximate gradients [15]. Further, DFO may struggle with precision near minima [17]. Overall, DFO demands more resources, posing a significant limitation in large-scale scenarios.

This paper's focus: VQE. Within this interplay between algorithms and error in calculations, we focus on a specific type of variational quantum algorithm [19], the Variational Quantum Eigensolver (VQE) [20]. VQE is the quantum analog of PCA that approximates the minimum/maximum eigenvalue/eigenvector pair of a given matrix (Hamiltonian), and can provide exponential time and space reduction over classical methods [21]. This problem is crucial for tasks like finding the ground state energies of molecules, which is pivotal in fields ranging from quantum chemistry to materials science [21-23]. Yet, VQE constitutes a framework with multiple moving parts: classical optimization procedures, quantum ansatzes, quantum observables, and hyperparameter tuning, all requiring careful setup before being applied to specific domains.

∗ Corresponding author

While VQE is meant for calculating the ground state energy of a Hamiltonian, it is also of interest to higher energy states, also known as 'excited states' [24-26]. Computing excited states provides insight into the properties of quantum systems. In quantum chemistry, determining excited states helps to understand chemical reaction mechanisms, including the absorption spectra and photochemistry of molecules [27]. In materials science, excited states can reveal information about electronic properties such as conductivity and magnetism, which are vital to designing new materials with targeted functionalities [28]. Calculating these excited states, as opposed to only finding the ground state, provides broader information on molecules of interest, and poses a greater technical challenge due to the requirement of maintaining orthogonality among calculated states.

Motivation and our contributions. This work builds upon a classical collaborative computation model, the EigenGame, presented in [29], to compute excited states in a noisy quantum environment. Unlike existing approaches that rely on deflation to calculate successive states [30-35], our method allows such a computation via a regularized objective inspired by game-theoretic ideas. Our primary contributions are:

- Theoretical Component : We provide a theory that validates the convergence properties of our algorithm. By formalizing the interaction between error calculations -due to noisy gradients and DFO routines- and convergence rates, we establish a theory for VQE targeting excited states.
- Algorithmic Framework : We propose a VQE meta-algorithm that changes the computational dynamics to find excited states. Using a modified quantum objective, our approach avoids deflation steps, diverging from traditional deflation-based computation models.
- Empirical Validation : The current implementation shows that our approach leads to favorable performance compared to baseline algorithms in terms of either convergence rate or accuracy.

## 2. Background

Notation. Matrices are denoted by uppercase letters, such as A ∈ C p × p , while lowercase letters, like b ∈ C p , represent vectors. Scalars are distinguished based on the context. The Euclidean ℓ 2 -norm is symbolized by ∥ · ∥ 2 . The qubit is the basic unit, analogous to the bit in classical computing. A qubit's state is expressed using the Dirac (bra-ket) notation; a single qubit state | ψ ⟩ ∈ C 2 is a linear combination of the basis states | 0 ⟩ = [1 0] ⊤ and | 1 ⟩ = [0 1] ⊤ in C 2 . For example, | ψ ⟩ = α | 0 ⟩ + β | 1 ⟩ where α, β ∈ C are complex amplitudes. These amplitudes encode the probabilities that the qubit's state collapses to | 0 ⟩ or | 1 ⟩ , satisfying the normalization condition | α | 2 + | β | 2 = 1 .

The notation |·⟩ represents a column vector (referred to as a ket ), and ⟨·| denotes its conjugate transpose ( bra ). This is a convenient notation that allows an inner product to be expressed by ⟨ x | y ⟩ and an outer product to be represented by | x ⟩⟨ y | , with ⟨ x | x ⟩ = 1 and ⟨ x | y ⟩ = 0 , for x ⊥ y . A separable q -qubit state, residing in a q -qubit Hilbert space, is the Kronecker product of q individual qubit states, represented as H = ⊗ q i =1 C 2 ∼ = C 2 q . It is expected to equate 2 q = p . Quantum states are manipulated by quantum gates, which are unitary matrices acting on state vectors. A single-qubit gate U ∈ C 2 × 2 , for example, transforms a state | ψ ⟩ into U | ψ ⟩ , adjusting the state's probability amplitudes according to the operation defined by U . An ideal quantum gate U is defined as a unitary matrix, where U † U = UU † = I allows rotation effects on | ψ ⟩ to preserve the normalization condition of the amplitude.

Principal component analysis and VQE. PCA has been studied as a way of finding the representative components from matrix data [36, 37]. This unsupervised learning problem effectively looks for the top (or bottom) principal component of a data matrix calculated via:

$$\max _ { v \in \mathbb { R } \colon \| v \| _ { 2 } = 1 } v ^ { \top } M v , \\$$

where M = 1 n X ⊤ X ∈ R p × p is often the covariance matrix of a dataset X ∈ R n × p with usually centered, normalized rows. For our discussion, assume that M is a real symmetric matrix with eigenvalues and eigenvectors { λ ⋆ i , v ⋆ i } p i =1 , satisfying λ ⋆ 1 ≥ λ ⋆ 2 ≥ · · · ≥ λ ⋆ p ≥ 0 . Then, v ⋆ 1 corresponds to the vector that maximizes (1) with objective value v ⋆ ⊤ 1 Mv ⋆ 1 = λ ⋆ 1 , and v ⋆ p is the vector that minimizes (1) with objective value v ⋆ ⊤ p Mv ⋆ p = λ ⋆ p .

Aninteresting aspect of PCA is the connection of (1) with the quadratic form maximization formulations found in the descriptions of quantum problems. In particular, in VQE and given a Hamiltonian M ∈ C p × p , the ground state energy, E min ∈ R , is always upper-bounded by the expectation of M with respect to a trial wavefunction. That is, E min ≤ ⟨ ψ | M | ψ ⟩ for any ψ ∈ C p . Similarly, the maximum energy, E max ∈ R , is always lower bounded as in E max ≥ ⟨ ψ | M | ψ ⟩ for any ψ ∈ C p .

What is different in VQE is the way we evolve the putative solution: Given an initial point | ψ 0 ⟩ , we start exploring from that point through the dynamics of the variational form | ψ ( θ ) ⟩ = ∏ ℓ -1 i =0 U i ( θ i ) | ψ 0 ⟩ , where U i ( θ i ) is a user-defined/designed unitary matrix. In more detail, an ansatz is prepared through a set of parameters θ ∈ R m to calculate the eigenvector/ eigenstate corresponding to the largest or least eigenvalue of M via:

$$\max _ { \theta \in \mathbb { R } ^ { m } } \, \langle \psi ( \theta ) | M | \psi ( \theta ) \rangle \, \ s . t . \ | \psi ( \theta ) \rangle = \prod _ { i = 0 } ^ { \ell - 1 } U _ { i } ( \theta _ { i } ) | \psi _ { 0 } \rangle .$$

Here, the dimension p = 2 q acts on q qubits; | ψ ( θ ) ⟩ ∈ C p is a quantum state, parameterized by m variables θ ∈ R m ; U i ( θ i ) ∈ C p × p represents a layer of an ansatz, repeated × ℓ times. See Figure 1 for a depiction. Using the bra-ket notation above, the analogs of i ) v ↔| ψ ( θ ) ⟩ , ii ) x ⊤ y ↔ ⟨ x | y ⟩ , and iii ) ∥ v ∥ 2 = 1 ↔ ∥| ψ ( θ ) ⟩∥ 2 = 1 , are determined between PCA and VQE. The key differences are the fact that PCA operates directly on v with no restrictions other than forcing v to be normalized, while, in VQE, we are looking for a parameterized vector | ψ ( θ ) ⟩ through a specific evolution from an initial state as in | ψ ( θ ) ⟩ = ∏ ℓ -1 i =0 U i ( θ i ) | ψ 0 ⟩ . Details of the ingredients of (2) are in the text below.

Figure 1: Circuit schematic for VQE where | ψ ( θ ) ⟩ is prepared as | ψ ( θ ) ⟩ = U ( θ ) | ψ 0 ⟩ when | ψ 0 ⟩ = | + ⟩ . The initial layer of Hadamard gates may be excluded to have | ψ 0 ⟩ = | 0 ⟩ . The circuit is then measured over an observable M to retrieve ⟨ ψ ( θ ) | M | ψ ( θ ) ⟩ .

<!-- image -->

We note that solving the maximization or minimization problem in (1) or (2) is an equivalent problem, since e.g., min ⟨ ψ ( θ ) | M | ψ ( θ ) ⟩ = max -⟨ ψ ( θ ) | M | ψ ( θ ) ⟩ by applying a sign operator. For the rest of the text, we will focus on the maximization case.

## Algorithm 1 Ideal VQE with Deflation

Input : M ∈ C p × p , VQE routine for ground state calculation, # of excited states k , and iters t .

$$\overline { \Psi } = \emptyset _ { \substack { M _ { 1 } \leftarrow M \\ \text {for } j = 1 \colon k \text { do } \\ | \psi _ { j } ( \theta ) \rangle \leftarrow V Q E \left ( M _ { j } , t \right ) \text { in } ( 7 ) \\ \lambda _ { j } \leftarrow \langle \psi _ { j } ( \theta ) | M _ { j } | \psi _ { j } ( \theta ) \rangle \\ M _ { j + 1 } \leftarrow M _ { j } - \lambda _ { j } | \psi _ { j } ( \theta ) \rangle \langle \psi _ { j } ( \theta ) | \\ \Psi \leftarrow \Psi \cup \{ | \psi _ { j } ( \theta ) \rangle \} \\ \end{end for } } }$$

```
|
```

end for Return Set Ψ of estimated eigenstates.

second component (second excited state) | ψ ⋆ 2 ⟩ , and so on.

Beyond 'top' eigenstates. Multicomponent PCA looks for K principal components, which means finding the K most excited states in a VQE setting. For M ∈ C p × p with sorted true principal components | ψ ⋆ 1 ⟩ , | ψ ⋆ 2 ⟩ , . . . , | ψ ⋆ p ⟩ , we are interested in finding vectors | ψ 1 ⟩ , . . . , | ψ k ⟩ , where k ≤ p , such that the difference between the corresponding true eigenvector | ψ ⋆ i ⟩ and | ψ i ⟩ , for all i ∈ [ k ] , is bounded as in ∥| ψ i ⟩ - | ψ ⋆ i ⟩∥ 2 ≤ ε, for some desired bound ε . One way to handle such a case is through deflation [37]: once the largest component | ψ ⋆ 1 ⟩ is approximated, M is further processed to 'live' on the subspace orthogonal to the subspace spanned by this component. The process then continues by again applying single-component VQE on the deflated M , which leads to an approximation of the

Howcould quantum deflation look in math? At the ( j +1) -th iteration of deflation, we estimate the leading eigenvector of:

$$\max _ { \theta \in \mathbb { R } ^ { m } } \ \langle \psi ( \theta ) | M _ { j + 1 } | \psi ( \theta ) \rangle \ \ s . t . \ \ | \psi ( \theta ) \rangle = \prod _ { i = 0 } ^ { \ell - 1 } U _ { i } ( \theta _ { i } ) | \psi _ { 0 } \rangle ,$$

where M j +1 is the deflated Hamiltonian, based on M j +1 = M j -λ j | ψ j ⟩⟨ ψ j | , where M j is the deflated Hamiltonian in the previous iteration, with M 1 := M and | ψ j ⟩ is the approximate estimate in (7) based on M j with corresponding energy λ j := ⟨ ψ j | M j | ψ j ⟩ . A generic procedure for solving the multicomponent VQE with deflation is detailed in Algorithm 1.

In practice though, successively reconstructing a deflated Hamiltonian represents a computational burden as it would require the construction of the deflated Hamiltonian-that entails a sum of Pauli operators for measuring it. Existing literature relies on implicit deflation algorithms, where one still uses the VQE framework but changes the objective to favor orthogonal solutions by adding a penalty term for vectors that are not orthogonal to the current vector. Such an example is the case of the Variational Quantum Deflation (VQD) algorithm [30]; we describe and compare with VQD in the experimental section.

In this work, we are exploring a novel penalty term in the objective, inspired by a game-theoretic formulation.

## 3. An EigenGame for VQE

What is EigenGame? Arecent study for calculating PCA in a distributed fashion led to the creation of EigenGame [29]. EigenGame is an algorithm posed as a competitive game, where 'players' are assigned to estimate eigenvectors, distinct from other eigenvectors of M . The way the algorithm operates leads to the Nash equilibrium of an eigenvalue game and does so by a sequential or a parallel version of EigenGame, namely EigenGame and EigenGameR [29], respectively.

Let v i ∈ R p denote an approximation of the i -th principal component of M . EigenGame defines an alternative utility objective to be maximized by the i -th 'player' in this game, defined as follows:

$$\max _ { v _ { i } \colon \| v _ { i } \| _ { 2 } = 1 } \left \{ f ( v _ { i } \, | \, v _ { j < i } ) \colon = v _ { i } ^ { \top } M v _ { i } - \sum _ { j < i } \frac { ( v _ { i } ^ { \top } \, M v _ { j } ) ^ { 2 } } { v _ { j } ^ { \prime } \, M v _ { j } } \right \} .$$

## Algorithm 2 EigenGame for the i -th player

Input : M ∈ R p × p , initial vectors v i, init , learned parents v j&lt;i , step size α , and # of iters t i . v i, 1 ← v i, init for t = 1 : t i do ∇ v i f ( v i,t | v j&lt;i ) = 2 M ( v i,t -∑ j&lt;i v ⊤ i,t Mv j v ⊤ j Mv j v j ) ˜ v i,t +1 ← v i,t + α ∇ v i f ( v i,t | v j&lt;i ) v i,t +1 ← ˜ v i,t +1 ∥ ˜ v i,t +1 ∥ 2 end for Return v i,t i

seeks to maximize its utility in terms of variance captured, considering the presence and position of other vectors. The gradient of the utility function, assuming access to a first-order oracle , can be calculated as ∇ v i f ( v i | v j&lt;i ) = 2 M ( v i -∑ j&lt;i v ⊤ i Mv j v ⊤ j Mv j v j ) . We describe EigenGame in Algorithm 2.

The term in blue maximizes the variance of the projected data along the vector being optimized. This is analogous to the traditional goal of PCA in (1). The term in red penalizes the alignment of the vector with any other vectors that have already been optimized. This term ensures implicit orthogonality among the vectors, mimicking the orthogonality constraint in PCA. The intuition behind this redefined objective function is to transform the PCA problem from a passive eigenvalue decomposition into an active, competitive process: each 'player'

Preparing the quantum EigenGame. Our interest steers towards obtaining a utility gradient that uses quantum oracle calls to calculate eigenvalue/eigenvector pairs. We first convert the classical EigenGame objective formulation into a parameterized one, using quantum computing formulations. Denoting the r -th player's parameters as θ ( r ) ∈ R m , its corresponding objective becomes:

$$\max _ { \theta ^ { ( r ) } \in \mathbb { R } ^ { m } } \left \{ \langle \psi ( \theta ^ { ( r ) } ) | M | \psi ( \theta ^ { ( r ) } ) \rangle - \sum _ { j < r } \frac { \langle \psi ( \theta ^ { ( r ) } ) | M | \psi ( \theta ^ { ( j ) } ) \rangle ^ { 2 } } { \langle \psi ( \theta ^ { G } ) | M | \psi ( \theta ^ { ( j ) } ) \rangle } \right \} \ s . t . \ | \psi ( \theta ^ { ( r ) } ) \rangle = \prod _ { i = 0 } ^ { \ell - 1 } U _ { i } ( \theta _ { i } ^ { ( r ) } ) | \psi _ { 0 } \rangle .$$

What differentiates (5) from the classical VQE formulation in (2) is the inclusion of the regularization term in red. That is, (5) defines different objectives per 'player'. Note that the term in blue is the measurement of the observable Hamiltonian M for the r -th player and is identical to that of the VQE objective in (2).

Focusing on the red part in (5), to incorporate information from the previous eigenvalue/eigenvector pairs, we compute the term ⟨ ψ ( θ ( r ) ) | M | ψ ( θ ( j ) ) ⟩ 2 using a procedure that calculates inner products on quantum states. We do so through an approach similar to the Hadamard Test [38, 39], where we first create an equal superposition of | ψ ( θ ( j ) ) ⟩ and | ψ ( θ ( r ) ) ⟩ with one additional ancilla qubit, followed by an H gate on said ancilla to yield Re ( ⟨ ψ ( θ ( r ) ) | M | ψ ( θ ( j ) ) ⟩ ) via Hamiltonian expectation with M = R ( ω ) † ZR ( ω ) . By adding an S gate, we can compute Im ( ⟨ ψ ( θ ( r ) ) | M | ψ ( θ ( j ) ) ⟩ ) . Here,

Figure 2: To compute terms of the form ⟨ ψ ( θ ( r ) ) | M | ψ ( θ ( j ) ) ⟩ , we utilize interference between | ψ ( θ ( r ) ) ⟩ and | ψ ( θ ( j ) ) ⟩ .

$$H & = \frac { 1 } { \sqrt { 2 } } \left [ \begin{matrix} 1 & 1 \\ 1 & - 1 \end{matrix} \right ] \text { and } S = \left [ \begin{matrix} 1 & 0 \\ 0 & i \end{matrix} \right ] \text { are single-qubit unit-}$$

tary gates, Z = [ 1 0 0 -1 ] is the computational basis Hamiltonian, and R ( ω ) is an arbitrary rotation gate. The ancilla qubit is an auxiliary qubit useful for intermediate computations. For an ancilla qubit with state | a ⟩ , the state of an n-qubit system that contains an ancilla can be defined as | Ψ ⟩ = ∑ 2 n -1 i =0 α i | i ⟩ ⊗ | a ⟩ . This implementation shown in Figure 2 computes ⟨ ψ ( θ ( r ) ) | M | ψ ( θ ( j ) ) ⟩ with only one additional qubit and two quantum oracle calls, providing an effective solution. See Appendix B for a detailed discussion and a derivation for our implementation. From here, we will also refer to quantum EigenGame as QuantumGame.

## Algorithm 3 QuantumGame of r -th player

Input : matrix M ∈ C p × p , initial values θ ( r ) init ∈ R m , T S η &gt; 0

```
# of iters/ , # of shots , step size . θ ( r ) 1 , : := θ ( r ) init . for t = 1 : T do Prepare state | ψ ( θ ( r ) t, : ) ⟩ = ∏ ℓ -1 i =0 U i ( θ ( r ) t,i ) | + ⟩ . Use | ψ ( θ ( r ) t, : ) ⟩ to approximate the gradient of objective in (5) w.r.t. θ ( r ) ; denote as ˜ ∇ ( r ) t, : ∈ R m . Update θ ( r ) t +1 , : = θ ( r ) t, : + η ˜ ∇ ( r ) t, : . end for Return | ψ ( θ ( r ) ) ⟩ := | ψ ( θ ( r ) T +1 , : ) ⟩ .
```

classical side (for the case of maximization) with step size η θ

Based on the above, Algorithm 3 provides our algorithm for the r -th player. Note the abuse of notation where θ ( r ) t,i indicates the variational parameters of the r -th player, associated with the i -th layer of the VQE that is ⊂ θ ( r ) t, : at the t -th iteration. Then, given the Hamiltonian M , and an initialization θ ( r ) init ∈ R m for the variational parameters, Algorithm 3 repeats over T iterations the steps of: i ) preparing the quantum state | ψ ( θ ( r ) t, : ) ⟩ = ∏ ℓ -1 i =0 U i ( θ ( r ) t,i ) | + ⟩ ; ii ) calculating gradient approximation of the objective in (5) w.r.t. θ ( r ) t, : , and iii ) performing gradient ascent on the to update ( r ) .

At the end of the execution, the eigenvalue ⟨ ψ ( θ ( r ) ) | M | ψ ( θ ( r ) ) ⟩ is broadcast to all 'children' agents r ′ &gt; r , alongside with the corresponding eigenvector | ψ ( θ ( r ) ) ⟩ to form (5) for the next 'player'. This process has a distributed flavor where each eigenvalue/eigenvector pair a parent agent calculates is broadcast to all its children agents, creating a directed graph acyclic hierarchy; see also Figure 3.

Challenges for the quantum EigenGame. Quantum computers typically interact with 0 th -order oracles, meaning they can only access function values without gradient information. This limitation impacts the efficiency and precision of algorithms, like EigenGame, which rely on gradients [29].

Any oracle call on a quantum computer is inherently noisy. The noise arises from multiple sources, including the underlying Hamiltonian, the calibration of quantum gates, cross-talk, the accuracy of the measurement mechanisms, and stochastic errors associated with measurements [4-6].

2 Note that the term ⟨ ψ ( θ ( j ) ) | M | ψ ( θ ( j ) ) ⟩ in the denominator of the red term is a classical observable operation, given the prepared state | ψ ( θ ( j ) ) ⟩ .

<!-- image -->

Finally, to our knowledge, the convergence analysis of the EigenGame under the effect of errors is not well understood. Traditional convergence proofs assume ideal conditions with precise computations, which do not hold in practical quantum scenarios. Recent advances in quantum algorithm analysis provide a foundation, but specific adaptations for the EigenGame are necessary [19].

Regarding gradient approximation, recent works leverage parameter-shift rules [38, 40-43] to obtain exact gradients using the same number of oracle evaluations as finite differences, given prior knowledge on the eigenvalues of the applied ansatz. In particular, for a single-qubit unitary with two distinct eigenvalues ± λ , the exact derivative is: ∂f ( θ ) ∂ m = λ [ f ( θ + π 4 λ ˆ e m ) -f ( θ -π 4 λ ˆ e m )] [38].

Classical 0 th -order EigenGame. To better understand the nature of having 0 th -order oracles in QuantumGame, we analyze the classical Eigengame with that same constraint. In principle, the 0 th -order version of EigenGame should not require gradient information, relying instead on function evaluations to guide the search for optimal solutions. These techniques, such as forward finite differences [44] and simultaneous perturbation stochastic approximation (SPSA) [45], provide approximate gradient information through multiple function evaluations [18].

For simplicity, we will focus on the forward finite differences technique. Based on the objective in (4), we study the case when an error σ ∈ R appears in each partial derivative. The error σ can be purely stochastic or predefined, and the treatment we give to it will differ based

Figure 3: QuantumGame with three players.

<!-- image -->

on its nature. Then, the 0 th -order utility partial derivative with respect to the m -th component of v i ∈ R p can be approximated as:

$$\frac { \partial f ( v _ { i } \, | \, v _ { j < i } ) } { \partial v _ { i , m } } \approx \frac { f ( v _ { i , 1 } , \dots , v _ { i , m } + \sigma , \dots , v _ { i , p } \, | \, v _ { j < i } ) ) - f ( v _ { i } \, | \, v _ { j < i } ) ) } { \sigma }$$

The above lead to the following observation, that will be helpful in the theory we will present:

Observation 1 We perform forward finite differences in order to obtain an analytical expression for a σ -approximate partial derivative of the m -th component of v i , which yields (see Appendix A):

$$\tilde { \nabla } _ { v _ { i } } f ( v _ { i } \, | \, v _ { j < i } ) = 2 M \left ( v _ { i } - \sum _ { j < i } \frac { v _ { i } ^ { \top } \, M v _ { j } } { v _ { j } ^ { \, M } v _ { j } } v _ { j } \right ) + \sigma \left ( d i a g ( M ) - \sum _ { j < i } \frac { ( M v _ { j } ) ^ { \circ 2 } } { v _ { j } ^ { \, M } v _ { j } } \right ) .$$

## Algorithm 4 0 th -order EigenGame for i -th player

Input : M ∈ R p × p , initial vectors v i, init , learned approximate parents v j&lt;i , perturbation σ ∈ R and step size α , # of iters. t i

$$\begin{array} { r l } & { \quad a p r o x i m a t e p a n t s v _ { j < i } , \, p e r t u r b a t i o n \sigma \in \mathbb { R } } \\ & { \quad a n d s e p s i z a , \# o f i t i s . \, t _ { i } } \\ & { \quad v _ { i , 1 } \leftarrow v _ { i , i n i t } } \\ & { \quad f o r t = 1 \colon t _ { i } \, d o } \\ & { \quad u t i l l i t y \colon = 2 M ( v _ { i , t } - \sum _ { j < i } \frac { v _ { i , t } ^ { \top } M v _ { j } } { v _ { j } M v _ { j } } v _ { i } ) } \\ & { \quad e r r o \colon = \sigma ( d i a g ( M ) - \sum _ { j < i } \frac { ( M v _ { j } ) ^ { 2 } } { v _ { j } ^ { \prime } M v _ { j } } ) } \\ & { \quad \widetilde { \nabla } _ { v _ { i } } f ( v _ { i , t } | v _ { j < i } ) = u t i l l i t y \ + \ e r r o } \\ & { \quad \widetilde { v } _ { i , t + 1 } \leftarrow v _ { i , t } + \alpha \widetilde { \nabla } _ { v _ { i } } f ( v _ { i , t } | v _ { j < i } ) } \\ & { \quad v _ { i , t + 1 } \leftarrow \frac { \widetilde { v } _ { i , t + 1 } } { | \widetilde { v } _ { i , t + 1 } | | 2 } } \\ & { \quad \text {end for} } \\ & { \quad \text {Return } v _ { i , t _ { i } } } \\ & { \quad \text {Eigene Game for all players} . \ \ \text {Consider the Algorithm } } \end{array}$$

Observe a linear dependence on σ on the second term, while the first term is identical to the analytical utility gradient. Based on (6), Algorithm 4 describes the 0 th -order EigenGame procedure including both the analytical and the error terms of the finite differences approximated utility gradient.

Theoretical guarantees. We provide convergence proofs for the 0 th -order EigenGame and for the parameterized EigenGame in Appendices C and E, respectively, and error accumulation theory for both in Appendix G. We first summarize the global convergence rate for both algorithms in the following.

Theorem 1 (Convergence of 0 th -order EigenGame for all players). Consider the Algorithm 4 with input matrix M ∈ R p × p and learned

'parent' eigenvectors v j&lt;i ∈ R p that are accurate enough, i.e., that | ϕ j&lt;i | ≤ c i g i ( i -1)Λ 11 ≤ √ 1 2 with 0 ≤ c i ≤ 1 16 . Let the initialization vector v i, init be within perturbation π 4 from v ⋆ i , i.e., ∠ ( v i, init , v ⋆ i ) ≤ π 4 , for all i . Consider perturbation σ ∈ R for the finite difference approximation, and step size α for the gradient ascent. Then, Algorithm 4 returns an approximate eigenvector v i with angular error less than ϕ tol &gt; 0 in

$$T = \left \lceil \mathcal { O } \left ( \sum _ { i = 1 } ^ { k } \frac { L _ { i } ( 0 ) } { L _ { i } ( \sigma ) } \left [ \frac { ( k - 1 ) ! } { \phi _ { i n } } \prod _ { j = 1 } ^ { k } \left ( \frac { 1 6 \Lambda _ { 1 1 } } { g _ { j } } \right ) \right ] ^ { 2 } \right ) \right \rceil \quad i t e r a t i o n s ,$$

where L i ( σ ) is the Lipschitz continuity assumption of the 0 th -order EigenGame based on a finite difference step size σ as in ∥ ˜ ∇ v i f ( v i | v j&lt;i ) ∥ 2 ≤ L i ( σ ) , Λ is the diagonal eigenvalue matrix of M containing eigenvalues Λ 11 &gt; Λ 22 &gt; . . . &gt; Λ kk with Λ 11 being the top eigenvalue, and g i = Λ ii -Λ i +1 ,i +1 is the eigengap between the two consecutive eigenvalues of players i and i +1 . The proof of this theorem is developed in Appendix D.

Theorem 2 (Convergence of QuantumGame for all players). Under sufficient decrease assumptions, Algorithm 3 achieves convergence to within ϕ tol angular error of the topk principal components independent of initialization. Let | ϕ j&lt;i | ≤ c i g i ( i -1)Λ 11 ≤ √ 1 2 with 0 ≤ c i ≤ 1 16 . Let each v ( ˆ θ i ) = U ( ˆ θ i ) | s ⟩ , with a sufficiently expressive ansatz U ( ˆ θ i ) [46, 47] and an initial state | s ⟩ such that ∠ ( v ( ˆ θ i ) , v ⋆ i ) ≤ π 4 . Algorithm 3 returns the eigenvectors with angular error less than ϕ tol in

$$T = \left \lceil \mathcal { O } \left ( \sum _ { i = 1 } ^ { k } \frac { L _ { \theta _ { i } } } { \sqrt { \ell _ { q } } } \left [ \frac { ( k - 1 ) ! } { \phi _ { t o l } } \prod _ { j = 1 } ^ { k } \left ( \frac { 1 6 \Lambda _ { 1 1 } } { g _ { j } } \right ) \right ] ^ { 2 } \right ) \right \rceil \quad t e r a t i o n s ,$$

where L θ i is the Lipschitz continuity constant of QuantumGame, ℓ is the number of layers of the ansatz and q is the number of qubits. The proof is shown in Appendix F.

We are also interested in establishing the error accumulation rate in both algorithms, given inaccurate parents. To do so, we bound the gradient difference between exact and inexact parent eigenvectors. Our error accumulation theorem is stated as follows.

Theorem 3 ( 0 th -order and parameterized error accumulation). Assume the angular error ϕ j ≤ ϵ between the true eigenvector v j , j &lt; i of a parent and its estimate ˆ v j to satisfy ϵ ≪ 1 . The Euclidean error of the parent is O ( ϵ ) and the Euclidean error of the child's 0 th -order gradient is O ( ϵ ) . Similarly, the Euclidean error of the child's parameterized gradient is O ( ϵ √ ℓq ) , with ℓ being the number of layers and q the number of qubits of the parameter space. An illustration for the 0 th -order case is shown in Figure 4, and proofs are given in Appendix G.

Figure 4: Error accumulation of a child eigenvector ˆ v i from its parent eigenvector ˆ v j , given ϕ j ≤ ϵ ≪ 1 .

<!-- image -->

Proof Sketch of Theorems 1 and 2. The 0 th -order theory begins by specifying the assumptions of utility lower bound (Assumption 1) and sufficient decrease (Assumption 2) necessary to identify the finite sample convergence rate of the i -th player of Algorithm 4. Theorem 5 specifies the generic Riemannian descent convergence rate under both assumptions, which we use for Riemannian ascent instead. The theory follows by defining the conditions under which the assumptions are satisfied, and used in Theorem 5.

Lemmas 9 and 10 provide a Lipschitz continuity coefficient L i ( σ ) that admits a finite-differences approximation error σ for the i -th player, where L i (0) becomes the Lipschitz coefficient of the exact EigenGame gradient. Corollary 11 approximately bounds the utility using L i ( σ ) , approximately satisfying Assumption 1. Lemma 12 then incorporates Corollary 11 to approximately bound the difference in the utility of consecutive steps, approximately satisfying Assumption 2. We then input these values into Theorem 5, and thus determine the number of iterations required for the 0 th -order EigenGame to converge in Lemma 15.

We employ a similar strategy for the parameterized scenario that we implement on quantum devices: we aim to satisfy Assumptions 1 and 2, and find the convergence rate for each player. To that effect, we assume the use of a highly expressive ansatz that can reach the exact eigenvalue of interest, and include information on the number of parameters of the ansatz in our analysis.

Lemmas 17 and 18 determine a Lipschitz continuity constant L ˆ ϕ i for the i -th player, introducing the number of layers ℓ and the number of qubits q from the ansatz. Corollary 19 states that the utility of the parameterized EigenGame is bounded by the same L i constant of the original EigenGame, satisying Assumption 1. We use a first-order Taylor expansion of the utility to approximately satisfy Assumption 2 in Lemma 20. The identified values that satisfy Assumption 1 and approximately satisfy Assumption 2 are used to provide the number of iterations necessary to reach finite sample convergence for QuantumGame in Lemma 22.

## 4. Experiments and discussion

We are interested in understanding how well our versions of EigenGame perform compared to the state of the art. With the application being the retrieval of energy levels for specific molecules, our experiments focus on characterizing the energy levels of the H 2 molecule, as well as understanding the impact of noise on QuantumGame compared to the Variational Quantum Deflation (VQD) algorithm.

Experimental setup. We use Pennylane's RandomLayers ansatz [48] with a number of layers ℓ proportional to the problem size of q qubits, following ansatz design suggestions from [49] where a direct relation between the degree of entanglement and the number of layers of an ansatz is made in the low-qubit regime, showingalinear scaling for layers that we adopt here. We study a 2 -qubit version of the H 2 molecule by applying a ParityMapper to the second quantization Hamiltonian of H 2 . We select a low number of 3 parameters per layer with 3 layers, sufficient to obtain the correct eigenvalues in a noiseless scenario.

Baselines. Wecompareresults against the Variational Quantum Deflation (VQD) algorithm [30], which aims to optimize:

Figure 5: Excited state energy levels of the two-qubit H 2 molecule mapping calculated with noiseless QuantumGame (blue line), noisy QuantumGame (orange line), noiseless VQD (green line) and noisy VQD (purple line) over accumulative iterations. The noisy setting only uses statistical shot noise with 10k shots. The exact energy level (dashed line) is extracted using Numpy. The inset plot shows the total number of iterations for noiseless VQD and noisy VQD with values of β ∈ [0 . 1 , 0 . 5 , 1 , 2 , 3 , 4 , 5] .

<!-- image -->

$$[ \sec ^ { 0 } ( r ) \min _ { \theta ^ { ( r ) } \in \mathbb { R } ^ { n } } \langle \psi ( \theta ^ { ( r ) } ) | M | \psi ( \theta ^ { ( r ) } ) \rangle + \sum _ { j < r } \beta | \langle \psi ( \theta ^ { ( r ) } ) | \psi ( \theta ^ { ( j ) } ) \rangle | ^ { 2 } \ \ s . t . \ \ | \psi ( \theta ^ { ( r ) } ) \rangle = \prod _ { i = 0 } ^ { \ell - 1 } U _ { i } ( \theta _ { i } ^ { ( r ) } ) | \psi _ { 0 } \rangle , \ \ ( 7 )$$

a similar approach to our algorithm but instead including a regularization parameter β which requires adequate tuning to reach comparable accuracy, adding a small overhead. We avoid this overhead by using an energy-aware adaptive regularization term, scaled with previously calculated eigenvalues. We test VQD over β ∈ [0 . 1 , 0 . 5 , 1 , 2 , 3 , 4 , 5] and set it to 0 . 1 in the main plot of Figure 5, with the least total number of iterations among the options tested. The total number of iterations for all β values are shown in the inset plot of Figure 5. Our settings for QuantumGame and VQD experiments are comprised of exact statevector simulation and shot-based simulation, where results are estimated based on averaging values over 10 k shots or samples affected by statistical shot noise through the expression ⟨ M ⟩ est ≈ ⟨ M ⟩ ± √ Var ( M ) N , where N is the number of shots, ⟨ M ⟩ est is the estimate of the expectation value of M and Var ( M ) = ⟨ M 2 ⟩ - ⟨ M ⟩ 2 is its variance [48].

Results. Figure 5 illustrates the convergence of the QuantumGame and VQD to the energy levels of the H 2 molecule when no noise effects are present and when under the effect of statistical shot noise -our noisy scenario- for 10 k shots. We use the Gradient Descent optimizer with η = 1 / 2 L , L = ∥ M ∥ , and a tolerance ∥∇ ˆ θ i f ( v ( ˆ θ i ) , v ( ˆ θ j&lt;i )) ∥ 2 ≤ 10 -2 . A similar convergence rate can be observed for the eigenvalue estimates of VQD when noise is present against their noiseless counterparts for β ≤ 1 , with shot noise being a larger source of errors among all values of β tested. This could be caused by our choices of the Gradient Descent optimizer, step size η , or the number of shots. For any of the scenarios, either more parameters or more shots may aid in obtaining higher accuracy. QuantumGamethusshowsmoreaccurateresultsthanthebaseline without hyperparameter tuning.

Figure 6: Total number of iterations required for eigenvalue calculation to within a tolerance of ρ i ≤ 10 -3 , i &lt; k using the exact and the 0 th -order EigenGame over k = { 2 i | i ∈ [3 , 10] } nondegenerate eigenvalues sampled from a powerlaw distribution over 5 runs. The blue and red line correspond to the exact EigenGame and the 0 th -order EigenGame, respectively.

<!-- image -->

vertible matrix P as a random orthonormal matrix through a QR decomposition where Q = P , P † = P -1 , P ∈ C n × n . Figure 6 describes our results and shows a similar scaling trend on both algorithms when using the Gradient Descent optimizer with η = 1 / 2 L , L = ∥ M ∥ .

## 5. Conclusions

We propose a variational algorithm for the problem of finding the top k eigenvalues of a Hamiltonian based on EigenGame [50]. We also propose a 0 th -order EigenGame using forward finite differences based on a 0 th -order oracle restriction motivated by the oracle class available to quantum computers. We perform a conventional classical convergence analysis for the 0 th -order EigenGame and state a global convergence rate, along with an error accumulation rate that accounts for imprecise parents. A similar analysis is performed for QuantumGame, where we include the number of layers and qubits of an ansatz.

We conduct an ablation study on the 0 th -order EigenGame by comparing the number of steps required to accurately estimate the top k eigenvalues of a Hamiltonian M against the exact EigenGame for small, medium and large dimensionality. We observe a similar scaling trend, implying that despite numerical errors being introduced, correct eigenvalues can still be found. We compared our QuantumGameformulation against the VQD algorithm and found an advantage of our formulation over VQD in experimental convergence rate and accuracy.

Ablation studies. We also inspect the behavior of our 0 th -order EigenGame compared to the exact EigenGame to validate the accuracy and convergence rate of the algorithms. These experiments are performed in a classical noiseless setting, as mapping exact statevectors v i onto a quantum computer is impractical given the exponential resources required. We first prepare the M Hamiltonian matrix from which we calculate the 8 leading eigenvalue/eigenvector pairs. Our focus is on finding the number of iterations required to reach ∥∇ v i f ( v i | v j&lt;i ) ∥ 2 ≤ 10 -3 on all i &lt; k eigenvalues, for k = { 2 i | i ∈ [3 , 10] } . In order to have adequate control over the optimization process and to ensure results that don't end up as corner cases, we construct M using a set of eigenvalues sampled from a power-law distribution in the range (0 , 1) and employing a similarity transformation through M = P -1 DP with D = λI a diagonal matrix with eigenvalues on the diagonal, and λ being a set of non-negative and non-degenerate eigenvalues. Given no prior knowledge on the eigenvectors to calculate, we generate a random in- Future work. A parallel implementation of QuantumGame where eigenvalues are calculated on different quantum devices simultaneously. It is our aim to remove any unnecessary assumptions in the analysis of our algorithms to strengthen our theory.

## Acknowledgements

This research was funded in part by: The Robert A. Welch Foundation (grant No. C-2118 A.K.); Rice University (Faculty Initiative award); NSF FET:Small (award no. 1907936); NSF CMMI (award no. 2037545); NSF CAREER (award no. 2145629); a Rice InterDisciplinary Excellence Award (IDEA); an Amazon Research Award; a Microsoft Research Award. AK would also like to thank the Ken Kennedy Institute for its support through the Research Cluster 'QuanTAS'. The content is solely the responsibility of the authors and does not necessarily represent the official views of the Funders. We thank professors Cesar Uribe and Tirthak Patel for insightful discussions on the project.

## References

- [1] A. Yu Kitaev. Quantum measurements and the abelian stabilizer problem. URL http:// arxiv.org/abs/quant-ph/9511026 .
- [2] David Deutsch and Richard Jozsa. Rapid solution of problems by quantum computation. Proceedings of the Royal Society of London. Series A: Mathematical and Physical Sciences , 439(1907): 553-558, 1992. doi: 10.1098/rspa.1992.0167. URL https://royalsocietypublishing.org/ doi/abs/10.1098/rspa.1992.0167 .
- [3] Lov K. Grover. A fast quantum mechanical algorithm for database search. In Proceedings of the Twenty-Eighth Annual ACM Symposium on Theory of Computing , STOC '96, page 212-219, New York, NY, USA, 1996. Association for Computing Machinery. ISBN 0897917855. doi: 10.1145/237814.237866. URL https://doi.org/10.1145/237814.237866 .
- [4] John Preskill. Quantum computing in the NISQ era and beyond. 2:79. ISSN 2521-327X. doi: 10.22331/q-2018-08-06-79. URL http://arxiv.org/abs/1801.00862 .
- [5] Guanru Feng, Joel J. Wallman, Brandon Buonacorsi, Franklin H. Cho, Daniel Park, Tao Xin, Dawei Lu, Jonathan Baugh, and Raymond Laflamme. Estimating the coherence of noise in quantum control of a solid-state qubit. 117(26):260501. ISSN 0031-9007, 1079-7114. doi: 10. 1103/PhysRevLett.117.260501. URL http://arxiv.org/abs/1603.03761 .
- [6] Michael A. Nielsen and Isaac L. Chuang. Quantum Computation and Quantum Information: 10th Anniversary Edition . Cambridge University Press, 2010.
- [7] Joel Wallman, Chris Granade, Robin Harper, and Steven T Flammia. Estimating the coherence of noise. New Journal of Physics , 17(11):113020, November 2015. ISSN 1367-2630. doi: 10.1088/ 1367-2630/17/11/113020. URL http://dx.doi.org/10.1088/1367-2630/17/11/113020 .
- [8] Prakash Murali, David C. Mckay, Margaret Martonosi, and Ali Javadi-Abhari. Software mitigation of crosstalk on noisy intermediate-scale quantum computers. In Proceedings of the Twenty-Fifth International Conference on Architectural Support for Programming Languages and Operating Systems , ASPLOS '20, page 1001-1016, New York, NY, USA, 2020. Association for Computing Machinery. ISBN 9781450371025. doi: 10.1145/3373376.3378477. URL https: //doi.org/10.1145/3373376.3378477 .
- [9] LéonBottou, Frank E Curtis, and Jorge Nocedal. Optimization methods for large-scale machine learning. SIAM review , 60(2):223-311, 2018.
- [10] Suvrit Sra, Sebastian Nowozin, and Stephen J Wright. Optimization for machine learning . Mit Press, 2012.
- [11] Nicholas J Higham. Accuracy and stability of numerical algorithms . SIAM, 2002.

- [12] Moritz Hardt and Eric Price. The noisy power method: A meta algorithm with applications. Advances in neural information processing systems , 27, 2014.
- [13] Andrew R Conn, Katya Scheinberg, and Luis N Vicente. Introduction to derivative-free optimization. MPS-SIAM Series on Optimization , 8, 2009.
- [14] Luis Miguel Rios and Nikolaos V Sahinidis. Derivative-free optimization: a review of algorithms and comparison of software implementations. Journal of Global Optimization , 56(3): 1247-1293, 2013.
- [15] Jeffrey Larson, Matt Menickelly, and Stefan M Wild. Derivative-free optimization methods. Acta Numerica , 28:287-404, 2019.
- [16] Tamara G Kolda, Robert Michael Lewis, and Virginia Torczon. Optimization by direct search: New perspectives on some classical and modern methods. SIAM review , 45(3):385-482, 2003.
- [17] Michael JD Powell et al. The BOBYQA algorithm for bound constrained optimization without derivatives. Cambridge NA Report NA2009/06, University of Cambridge, Cambridge , 26:26-46, 2009.
- [18] Albert S. Berahas, Liyuan Cao, Krzysztof Choromanski, and Katya Scheinberg. A theoretical and empirical comparison of gradient approximations in derivative-free optimization. URL http://arxiv.org/abs/1905.01332 .
- [19] M. Cerezo, Andrew Arrasmith, Ryan Babbush, Simon C. Benjamin, Suguru Endo, Keisuke Fujii, Jarrod R. McClean, Kosuke Mitarai, Xiao Yuan, Lukasz Cincio, and Patrick J. Coles. Variational quantum algorithms. 3(9):625-644. ISSN 2522-5820. doi: 10.1038/s42254-021-00348-9. URL http://arxiv.org/abs/2012.09265 .
- [20] Alberto Peruzzo, Jarrod McClean, Peter Shadbolt, Man-Hong Yung, Xiao-Qi Zhou, Peter J. Love, Alán Aspuru-Guzik, and Jeremy L. O'Brien. A variational eigenvalue solver on a quantum processor. 5(1):4213. ISSN 2041-1723. doi: 10.1038/ncomms5213. URL http: //arxiv.org/abs/1304.3061 .
- [21] Jules Tilly, Hongxiang Chen, Shuxiang Cao, Dario Picozzi, Kanav Setia, Ying Li, Edward Grant, Leonard Wossnig, Ivan Rungger, George H. Booth, and Jonathan Tennyson. The variational quantum eigensolver: A review of methods and best practices. Physics Reports , 986:1-128, November 2022. ISSN 0370-1573. doi: 10.1016/j.physrep.2022.08.003. URL http://dx.doi. org/10.1016/j.physrep.2022.08.003 .
- [22] Abhinav Kandala, Antonio Mezzacapo, Kristan Temme, Maika Takita, Markus Brink, Jerry M. Chow, and Jay M. Gambetta. Hardware-efficient variational quantum eigensolver for small molecules and quantum magnets. Nature , 549(7671):242-246, September 2017. ISSN 14764687. doi: 10.1038/nature23879. URL http://dx.doi.org/10.1038/nature23879 .
- [23] Jarrod R McClean, Jonathan Romero, Ryan Babbush, and Alán Aspuru-Guzik. The theory of variational hybrid quantum-classical algorithms. New Journal of Physics , 18(2):023023, February 2016. ISSN 1367-2630. doi: 10.1088/1367-2630/18/2/023023. URL http://dx.doi.org/ 10.1088/1367-2630/18/2/023023 .
- [24] P. J. J. O'Malley, R. Babbush, I. D. Kivlichan, J. Romero, J. R. McClean, R. Barends, J. Kelly, P. Roushan, A. Tranter, N. Ding, B. Campbell, Y. Chen, Z. Chen, B. Chiaro, A. Dunsworth, A. G. Fowler, E. Jeffrey, E. Lucero, A. Megrant, J. Y. Mutus, M. Neeley, C. Neill, C. Quintana, D. Sank, A. Vainsencher, J. Wenner, T. C. White, P. V. Coveney, P. J. Love, H. Neven, A. AspuruGuzik, and J. M. Martinis. Scalable quantum simulation of molecular energies. Phys. Rev. X , 6:031007, Jul 2016. doi: 10.1103/PhysRevX.6.031007. URL https://link.aps.org/doi/10. 1103/PhysRevX.6.031007 .

- [25] Oscar Higgott, Daochen Wang, and Stephen Brierley. Variational quantum computation of excited states. 3:156. ISSN 2521-327X. doi: 10.22331/q-2019-07-01-156. URL http://arxiv. org/abs/1805.08138 .
- [26] Cheng-Lin Hong, Luis Colmenarez, Lexin Ding, Carlos L. Benavides-Riveros, and Christian Schilling. Quantum parallelized variational quantum eigensolvers for excited states, 2023.
- [27] Sam McArdle, Suguru Endo, Alán Aspuru-Guzik, Simon C Benjamin, and Xiao Yuan. Quantum computational chemistry. Reviews of Modern Physics , 92(1):015003, 2020.
- [28] Yudong Cao, Jonathan Romero, Jonathan P Olson, Matthias Degroote, Peter D Johnson, Mária Kieferová, Ian D Kivlichan, Tim Menke, Borja Peropadre, Nicolas PD Sawaya, et al. Quantum chemistry in the age of quantum computing. Chemical reviews , 119(19):10856-10915, 2019.
- [29] Ian Gemp, Brian McWilliams, Claire Vernade, and Thore Graepel. EigenGame: PCA as a Nash equilibrium. In International Conference on Learning Representations , 2021.
- [30] Oscar Higgott, Daochen Wang, and Stephen Brierley. Variational quantum computation of excited states. Quantum , 3:156, 2019.
- [31] Yohei Ibe, Yuya O Nakagawa, Nathan Earnest, Takahiro Yamamoto, Kosuke Mitarai, Qi Gao, and Takao Kobayashi. Calculating transition amplitudes by variational quantum deflation. Physical Review Research , 4(1):013173, 2022.
- [32] Jingwei Wen, Dingshun Lv, Man-Hong Yung, and Gui-Lu Long. Variational quantum packaged deflation for arbitrary excited states. Quantum Engineering , 3(4):e80, 2021.
- [33] David Schaich and Christopher Culver. Exploring lattice supersymmetry with variational quantum deflation. arXiv preprint arXiv:2410.11514 , 2024.
- [34] Soichi Shirai, Takahiro Horiba, and Hirotoshi Hirai. Calculation of core-excited and coreionized states using variational quantum deflation method and applications to photocatalyst modeling. Acs Omega , 7(12):10840-10853, 2022.
- [35] Zohim Chandani, Kazuki Ikeda, Zhong-Bo Kang, Dmitri E Kharzeev, Alexander McCaskey, Andrea Palermo, CR Ramakrishnan, Pooja Rao, Ranjani G Sundaram, and Kwangmin Yu. Efficient charge-preserving excited state preparation with variational quantum algorithms. arXiv preprint arXiv:2410.14357 , 2024.
- [36] Karl Pearson. Liii. on lines and planes of closest fit to systems of points in space. The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science , 2(11):559-572, 1901. doi: 10.1080/14786440109462720. URL https://doi.org/10.1080/14786440109462720 .
- [37] H. Hotelling. Analysis of a complex of statistical variables into principal components. Journal of Educational Psychology , 24(6):417-441, September 1933. ISSN 1939-2176, 0022-0663. doi: 10.1037/h0071325. URL https://doi.apa.org/doi/10.1037/h0071325 .
- [38] Maria Schuld, Ville Bergholm, Christian Gogolin, Josh Izaac, and Nathan Killoran. Evaluating analytic gradients on quantum hardware. Phys. Rev. A , 99:032331, Mar 2019. doi: 10.1103/ PhysRevA.99.032331. URL https://link.aps.org/doi/10.1103/PhysRevA.99.032331 .
- [39] Carlos Bravo-Prieto, Ryan LaRose, M. Cerezo, Yigit Subasi, Lukasz Cincio, and Patrick J. Coles. Variational quantum linear solver. Quantum , 7:1188, November 2023. ISSN 2521-327X. doi: 10.22331/q-2023-11-22-1188. URL http://dx.doi.org/10.22331/q-2023-11-22-1188 .
- [40] K. Mitarai, M. Negoro, M. Kitagawa, and K. Fujii. Quantum circuit learning. Physical Review A , 98(3), September 2018. ISSN 2469-9934. doi: 10.1103/physreva.98.032309. URL http: //dx.doi.org/10.1103/PhysRevA.98.032309 .

- [41] David Wierichs, Josh Izaac, Cody Wang, and Cedric Yen-Yu Lin. General parameter-shift rules for quantum gradients. Quantum , 6:677, March 2022. ISSN 2521-327X. doi: 10.22331/ q-2022-03-30-677. URL http://dx.doi.org/10.22331/q-2022-03-30-677 .
- [42] Artur F. Izmaylov, Robert A. Lang, and Tzu-Ching Yen. Analytic gradients in variational quantum algorithms: Algebraic extensions of the parameter-shift rule to general unitary transformations. Physical Review A , 104(6), December 2021. ISSN 2469-9934. doi: 10.1103/physreva. 104.062443. URL http://dx.doi.org/10.1103/PhysRevA.104.062443 .
- [43] Ioannis Kolotouros, Ioannis Petrongonas, Miloš Prokop, and Petros Wallden. Adiabatic quantum computing with parameterized quantum circuits, 2023.
- [44] Brook Taylor. Methodus Incrementorum Directa et Inversa . Gulielmus Innys, London, 1715.
- [45] J.C. Spall. Multivariate stochastic approximation using a simultaneous perturbation gradient approximation. IEEE Transactions on Automatic Control , 37(3):332-341, 1992. doi: 10.1109/9. 119632.
- [46] Sukin Sim, Peter D. Johnson, and Alán Aspuru-Guzik. Expressibility and entangling capability of parameterized quantum circuits for hybrid quantum-classical algorithms. Advanced QuantumTechnologies , 2(12), October 2019. ISSN 2511-9044. doi: 10.1002/qute.201900070. URL http://dx.doi.org/10.1002/qute.201900070 .
- [47] Zoë Holmes, Kunal Sharma, M. Cerezo, and Patrick J. Coles. Connecting ansatz expressibility to gradient magnitudes and barren plateaus. PRX Quantum , 3(1), January 2022. ISSN 26913399. doi: 10.1103/prxquantum.3.010313. URL http://dx.doi.org/10.1103/PRXQuantum. 3.010313 .
- [48] Ville Bergholm, Josh Izaac, Maria Schuld, Christian Gogolin, Shahnawaz Ahmed, Vishnu Ajith, M. Sohaib Alam, Guillermo Alonso-Linaje, B. AkashNarayanan, Ali Asadi, Juan Miguel Arrazola, Utkarsh Azad, Sam Banning, Carsten Blank, Thomas R Bromley, Benjamin A. Cordier, Jack Ceroni, Alain Delgado, Olivia Di Matteo, Amintor Dusko, Tanya Garg, Diego Guala, Anthony Hayes, Ryan Hill, Aroosa Ijaz, Theodor Isacsson, David Ittah, Soran Jahangiri, Prateek Jain, Edward Jiang, Ankit Khandelwal, Korbinian Kottmann, Robert A. Lang, Christina Lee, Thomas Loke, Angus Lowe, Keri McKiernan, Johannes Jakob Meyer, J. A. MontañezBarrera, Romain Moyard, Zeyue Niu, Lee James O'Riordan, Steven Oud, Ashish Panigrahi, Chae-Yeun Park, Daniel Polatajko, Nicolás Quesada, Chase Roberts, Nahum Sá, Isidor Schoch, Borun Shi, Shuli Shu, Sukin Sim, Arshpreet Singh, Ingrid Strandberg, Jay Soni, Antal Száva, Slimane Thabet, Rodrigo A. Vargas-Hernández, Trevor Vincent, Nicola Vitucci, Maurice Weber, David Wierichs, Roeland Wiersema, Moritz Willmann, Vincent Wong, Shaoming Zhang, and Nathan Killoran. Pennylane: Automatic differentiation of hybrid quantum-classical computations, 2022. URL https://arxiv.org/abs/1811.04968 .
- [49] Carlos Bravo-Prieto, Josep Lumbreras-Zarapico, Luca Tagliacozzo, and José I. Latorre. Scaling of variational quantum circuit depth for condensed matter systems. Quantum , 4:272, May 2020. ISSN 2521-327X. doi: 10.22331/q-2020-05-28-272. URL http://dx.doi.org/10.22331/ q-2020-05-28-272 .
- [50] Ian Gemp, Brian McWilliams, Claire Vernade, and Thore Graepel. Eigengame: Pca as a nash equilibrium, 2021.
- [51] Adriano Barenco, Andre' Berthiaume, David Deutsch, Artur Ekert, Richard Jozsa, and Chiara Macchiavello. Stabilisation of quantum computations by symmetrisation, 1996.
- [52] Harry Buhrman, Richard Cleve, John Watrous, and Ronald de Wolf. Quantum fingerprinting. Physical Review Letters , 87(16), September 2001. ISSN 1079-7114. doi: 10.1103/physrevlett.87. 167902. URL http://dx.doi.org/10.1103/PhysRevLett.87.167902 .

- [53] Nicolas Boumal, P.-A. Absil, and Coralia Cartis. Global rates of convergence for nonconvex optimization on manifolds. 39(1):1-33. ISSN 0272-4979, 1464-3642. doi: 10.1093/imanum/ drx080. URL http://arxiv.org/abs/1605.08101 .

## A. Calculating the expression of the finite differences EigenGame gradient

To map the finite differences formulation on the EigenGame objective, we delve into the specifics of the utility function, by unrolling the matrix/vector inner products entrywise:

̸

̸

̸

̸

$$the utility function, by unrolling the matrix/vector inner products entrywise: \\ f ( v _ { i } \, | \, v _ { j < i } ) = v _ { i } ^ { T } M v _ { i } - \sum _ { j < i } \frac { ( v _ { i } ^ { T } M v _ { j } ) ^ { 2 } } { v _ { j } ^ { T } M v _ { j } } \\ = \sum _ { k } \sum _ { i } v _ { i , k } v _ { i , k } M _ { 1 , k } - \sum _ { j < i } \frac { ( \sum _ { l } \sum _ { k } v _ { j , l } v _ { i , k } M _ { k , l } ) ^ { 2 } } { \sum _ { l } \sum _ { k } v _ { j , l } v _ { j , k } M _ { l , k } } \\ = v _ { i , m } \cdot \left ( \sum _ { k \neq m } v _ { i , k } M _ { m , k } \right ) + \left ( \sum _ { k \neq m } v _ { i , k } M _ { k , m } \right ) \cdot v _ { i , m } + v _ { i , m } ^ { 2 } M _ { m , m } + \sum _ { l \neq m } \sum _ { k \neq m } v _ { i , l } v _ { i , k } M _ { l , k } \\ - \sum _ { j < i } \frac { \left ( v _ { i , m } \cdot ( \sum _ { l } M _ { m , l } v _ { j , l } ) + \sum _ { l } \sum _ { k \neq m } v _ { j , l } v _ { i , k } M _ { k , l } \right ) ^ { 2 } } { v _ { j } ^ { T } M v _ { j } } \\ \text {where blue terms correspond to the components from the core objective term } v _ { i } ^ { T } M v _ { i } , \text { while red}$$

̸

where blue terms correspond to the components from the core objective term v ⊤ i Mv i , while red terms correspond to the regularized term of the EigenGame formulation, ∑ j&lt;i ( v ⊤ i Mv j ) 2 v ⊤ j Mv j . Adding the error term σ to the m -entry of v i , we obtain:

̸

̸

$$t h e r \, \text {term} \, \sigma \, \circ t h e r \, \text {or} \, v _ { i } , \, \text {we obtain} \colon \\ f ( v _ { i , 1 } , \dots , v _ { i , m } + \sigma , \dots , v _ { i , p } \, | \, v _ { j < i } ) = ( v _ { i , m } + \sigma ) \cdot \left ( \sum _ { k \neq m } v _ { i , k } M _ { m , k } \right ) + \left ( \sum _ { k \neq m } v _ { i , k } M _ { k , m } \right ) \\ \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \$$

̸

Next, we perform forward finite differences in order to obtain an expression for an σ -approximate partial derivative of the m -th component of v i :

̸

̸

$$& \text {partial derivative of the } m { \text {th component of } v _ { i } } \\ & \quad \frac { f ( v _ { i , 1 } , \dots , v _ { i , m } + \sigma , \dots , v _ { i , p } | \ v _ { j < i } ) - f ( v _ { i } | \ v _ { j < i } ) } { \sigma } \\ & \quad = \frac { \sigma } { \sigma } \left ( \sum _ { k \neq m } v _ { i , k } M _ { m , k } + \sum _ { k \neq m } v _ { i , k } M _ { k , m } + ( 2 v _ { i , m } + \sigma ) M _ { m , m } \\ & \quad - \sum _ { j < i } \frac { ( 2 v _ { i , m } + \sigma ) ( \sum _ { l } M _ { m , l } v _ { j , l } ) ^ { 2 } } { v _ { j } ^ { \prime } M v _ { j } } - \sum _ { j < i } \frac { 2 ( \sum _ { l } M _ { m , l } v _ { j , l } ) ( \sum _ { l } \sum _ { k \neq m } v _ { j , l } v _ { i , k } M _ { k , l } ) } { v _ { j } ^ { \prime } M v _ { j } } \right ) \\ & \quad = 2 M _ { m , \cdot } v _ { i } + \sigma M _ { m , m } - \sum _ { j < i } \left ( \frac { 2 M _ { m , \cdot } v _ { j } ( v _ { i } ^ { \top } M v _ { j } ) + \sigma ( M _ { m , \cdot } v _ { j } ) ( M _ { m , \cdot } v _ { j } ) } { v _ { j } ^ { \prime } M v _ { j } } \right ) \\ & \quad = 2 M _ { m , \cdot } \left ( v _ { i } - \sum _ { j < i } \frac { v _ { j } ^ { \top } M v _ { j } } { v _ { j } ^ { \prime } M v _ { j } } v _ { j } \right ) + \sigma \left ( M _ { m , m } - \sum _ { j < i } \frac { ( M _ { m , \cdot } v _ { j } ) ^ { 2 } } { v _ { j } ^ { \prime } M v _ { j } } \right ) \\ \intertext { a n t i l y } \text {finally, the previous expression, in a vectorized gradient form, is equivalent to: }$$

̸

Finally, the previous expression, in a vectorized gradient form, is equivalent to:

$$\widetilde { \nabla } _ { v _ { i } } f ( v _ { i } \, | \, v _ { j < i } ) = 2 M \left ( v _ { i } - \sum _ { j < i } \frac { v _ { i } ^ { \top } \, M v _ { i } } { v _ { j } ^ { \, M } v _ { j } } v _ { j } \right ) + \sigma \left ( \text {diag} ( M ) - \sum _ { j < i } \frac { ( M v _ { j } ) ^ { \circ 2 } } { v _ { j } ^ { \, M } v _ { j } } \right ) .$$

̸

̸

## B. Swap test and Hadamard test derivations

The SwapTest [51, 52] calculates the inner product between two quantum states. It requires 2 q +1 qubits for its operation, including q qubits for representing each of both quantum states, and 1 ancilla qubit that will store the inner product. In particular, for two states | ϕ 1 ⟩ , | ϕ 2 ⟩ ∈ C p , the SwapTest circuit outputs a probability value:

$$P ( | 0 \dots \rangle ) = \frac { 1 } { 2 } - \frac { 1 } { 2 } | \langle \phi _ { 1 } | \phi _ { 2 } \rangle | ^ { 2 } \in [ 1 / 2 , 1 ] ,$$

that represents the probability of the first qubit in a quantum state being in the | 0 ⟩ state. E.g., when | ϕ 1 ⟩ , | ϕ 2 ⟩ are coaligned, then |⟨ ϕ 1 | ϕ 2 ⟩| = 1 , and thus P ( | 0 . . . ⟩ ) = 1 , while when | ϕ 1 ⟩ , | ϕ 2 ⟩ are orthogonal, then |⟨ ϕ 1 | ϕ 2 ⟩| = 0 and thus P ( | 0 . . . ⟩ ) = 1 2 (i.e., observing 0 is equivalent to a toss of a perfect coin). This allows one to, for example, estimate the squared inner product between the two states, |⟨ ϕ 1 | ϕ 2 ⟩| 2 , to ε additive error by taking the average over O ( 1 ε 2 ) runs of the SwapTest .

Figure 7 shows our implementation of the procedure, where we prepare:

$$| \phi _ { 1 } \rangle = | \psi ( \theta ^ { ( i ) } ) \rangle , \ | \phi _ { 2 } \rangle = M | \psi ( \theta ^ { ( j ) } ) \rangle ,$$

for each index in the sum of eq. 5, obtaining:

$$| \langle \psi ( \theta ^ { ( i ) } ) | M | \psi ( \theta ^ { ( j ) } ) \rangle | ^ { 2 } = 1 - 2 P ( | 0 \dots \rangle ) . \quad ( 1 0 ) ^ { | \psi ( 0 ) | ^ { 2 } }$$

In order to correctly implement the SwapTest, the matrix M must satisfy one of the following requirements:

- M is a unitary matrix.
- M can be decomposed into a linear combination of unitary matrices { U i } as M = ∑ i a i U i such that each evaluation ⟨ ˆ v i ( θ i ) | U i | ˆ v j ( θ i ) ⟩ 2 ≥ 0 .
- M can be decomposed into a linear combination of Pauli operators { P i } as M = ∑ i a i P i such that each evaluation ⟨ ˆ v i ( θ i ) | P i | ˆ v j ( θ i ) ⟩ 2 ≥ 0 .

Figure 7: Circuit schematic for SwapTest. Here, M is the problem Hamiltonian, and H is the Hadamard gate.

<!-- image -->

These limitations are due to the SwapTest being only able to calculate the overlap of quantum states when M is a quantum gate applied to one of the two states. If M is already a unitary matrix, only one evaluation is necessary. On the other hand, if M is not a unitary matrix, it should be decomposed into a linear combination of unitary matrices such as Pauli operators. After a successful decomposition of M as M = ∑ i a i U i , the following quantities may be calculated:

$$| \langle \psi ( \theta _ { i } ) | U _ { i } | \psi ( \theta _ { j } ) \rangle | = \sqrt { 1 - 2 P _ { i } ( | 0 \dots \rangle ) } .$$

which can be combined and contrasted with the expected calculation via

$$| \langle \psi ( \theta _ { i } ) | M | \psi ( \theta _ { j } ) \rangle | & = \left | \sum _ { i } a _ { i } \langle \psi ( \theta _ { i } ) | U _ { i } | \psi ( \theta _ { j } ) \rangle \right | \\ & \geq \sum _ { i } a _ { i } | \langle \psi ( \theta _ { i } ) | U _ { i } | \psi ( \theta _ { j } ) \rangle | .$$

In order to reach an equivalence, either M = U 0 or:

$$\langle \psi ( \theta _ { i } ) | U _ { i } | \psi ( \theta _ { j } ) \rangle \geq 0 , a _ { i } > 0$$

must be satisfied.

In order to overcome the limitation of (13), we propose a novel circuit for computing this value, illustrated in Figure 2. We will describe how this implementation computes ⟨ ψ ( θ ( r ) ) | M | ψ ( θ ( j ) ) ⟩ via the following Lemma:

Lemma 4 The circuit depicted in Figure 2 is able to compute the value ⟨ ψ ( θ ( r ) ) | M | ψ ( θ ( j ) ) ⟩ using q + 1 qubits and two expectations of M .

Proof. Without loss of generality, assume we are computing Re ( ⟨ ψ ( θ ( r ) ) | M | ψ ( θ ( j ) ) ⟩ ) (as computing Im ( ⟨ ψ ( θ ( r ) ) | M | ψ ( θ ( j ) ) ⟩ ) is an analogous operation). We will show that we can compute Re ( ⟨ ψ ( θ ( r ) ) | M | ψ ( θ ( j ) ) ⟩ ) with q +1 qubits and one expectation of M .

Let | ψ ( θ ( j ) ) ⟩ = U ( θ ( j ) ) | 0 ⟩ and | ψ ( θ ( r ) ) ⟩ = U ( θ ( r ) ) | 0 ⟩ , after preparing the superposition in Figure 2, if we let Ψ represent the state of our quantum system, then Ψ can be written as:

$$\Psi = \frac { 1 } { \sqrt { 2 } } ( | \psi ( \theta ^ { ( j ) } ) | 0 \rangle + | \psi ( \theta ^ { ( r ) } ) \rangle | 1 \rangle )$$

We then apply the phase gate S to Ψ depending on whether we want to measure the imaginary component of ⟨ ψ ( θ ( r ) ) | ˆ H | ψ ( θ ( j ) ) ⟩ . We will proceed our analysis without applying the S gate to compute Re ( ⟨ ψ ( θ ( r ) ) | ˆ H | ψ ( θ ( j ) ) ⟩ ) , although the analysis will proceed symmetrically if the S gate is applied to compute Im ( ⟨ ψ ( θ ( r ) ) | ˆ H | ψ ( θ ( j ) ) ⟩ ) .

We then apply the H gate again to our quantum system, putting it in the state:

$$\Psi = \frac { 1 } { 2 } ( | \psi ( \theta ^ { ( j ) } ) | 0 \rangle + | \psi ( \theta ^ { ( j ) } ) | 1 \rangle + | \psi ( \theta ^ { ( r ) } ) | 0 \rangle - | \psi ( \theta ^ { ( r ) } ) | 1 \rangle )$$

We then compute the expectation value of our Hamiltonian, measuring the effects of our ancilla:

$$\text {we then compute the expectation value of our random constant, measureing the effects of our anchra.} \\ \langle \Psi | \hat { H } \otimes Z | \Psi \rangle = \frac { 1 } { 4 } ( \langle | \langle \psi ( \theta ^ { ( j ) } ) | + \langle 1 | \langle \psi ( \theta ^ { ( j ) } ) | + \langle 0 | \langle \psi ( \theta ^ { ( r ) } ) | - \langle 1 | \langle \psi ( \theta ^ { ( r ) } ) | \hat { H } \otimes Z | ( \psi ( \theta ^ { ( j ) } ) | 0 ) \, \left ( 1 6 \right ) } \\ + | \psi ( \theta ^ { ( j ) } ) | 1 + | \psi ( \theta ^ { ( r ) } ) | 0 - | \psi ( \theta ^ { ( r ) } ) | 1 ) \\ = \frac { 1 } { 4 } ( \langle \psi ( \theta ^ { ( j ) } ) | \hat { H } | \psi ( \theta ^ { ( j ) } ) \rangle + \langle \psi ( \theta ^ { ( r ) } ) | \hat { H } | \psi ( \theta ^ { ( j ) } ) \rangle - \langle \psi ( \theta ^ { ( j ) } ) | \hat { H } | \psi ( \theta ^ { ( j ) } ) \rangle \\ + \langle \psi ( \theta ^ { ( r ) } ) | \hat { H } | \psi ( \theta ^ { ( j ) } ) \rangle + \langle \psi ( \theta ^ { ( j ) } ) | \hat { H } | \psi ( \theta ^ { ( r ) } ) \rangle + \langle \psi ( \theta ^ { ( r ) } ) | \hat { H } | \psi ( \theta ^ { ( r ) } ) \rangle \\ + \langle \psi ( \theta ^ { ( j ) } ) | \hat { H } | \psi ( \theta ^ { ( r ) } ) \rangle - \langle \psi ( \theta ^ { ( r ) } ) | \hat { H } | \psi ( \theta ^ { ( r ) } ) \rangle \\ = \frac { 1 } { 4 } ( 2 \langle \psi ( \theta ^ { ( r ) } ) | \hat { H } | \psi ( \theta ^ { ( j ) } ) + 2 \langle \psi ( \theta ^ { ( j ) } ) | \hat { H } | \psi ( \theta ^ { ( r ) } ) \rangle \\ = \frac { 1 } { 4 } ( 4 R e ( \langle \psi ( \theta ^ { ( r ) } ) | \hat { H } | \psi ( \theta ^ { ( j ) } ) \rangle ) \\ = R e ( \langle \psi ( \theta ^ { ( r ) } ) | \hat { H } | \psi ( \theta ^ { ( j ) } ) \rangle ) \\ \intertext { as desired. }$$

as desired.

## C. Classical finite differences convergence analysis

Following recent theory on nonconvex optimization on manifolds [53], we can restate two main assumptions regarding the convergence of the generic Riemann descent algorithm:

Assumption 1 (Assumption O.2 in [29]) (Lower bound). There exists f ⋆ &gt; -∞ such that f ( x ) ≥ f ⋆ , ∀ x ∈ M .

Assumption 2 (Assumption O.3 in [29]) (Sufficient decrease). There exist scalars ξ , ξ ′ &gt; 0 such that, ∀ k ≥ 0 ,

$$f ( x _ { k } ) - f ( x _ { k + 1 } ) \geq \min \{ \xi \cdot \| \nabla ^ { R } f ( x _ { k } ) \| _ { 2 } , \, \xi ^ { \prime } \} \cdot \| \nabla ^ { R } f ( x _ { k } ) \| _ { 2 } .$$

We make another assumption based on a design decision made in [29], where the authors claim omitting the projection step mimics modulating the learning rate, improving stability:

$$\text {Assumption} \, 3 \, \left ( P r o j e c t i o n \right ) . \text { For all } k \geq 0 , \forall x \in \mathcal { M } = \mathbb { R } ^ { n } , \\ \nabla ^ { R } f ( x _ { k } ) \colon = \nabla f ( x _ { k } ) .$$

Based on Assumption 3, the sufficient decrease of Assumption 2 may be reformulated as:

$$f ( x _ { k } ) - f ( x _ { k + 1 } ) \geq \min \{ \xi \cdot \| \nabla f ( x _ { k } ) \| _ { 2 } , \, \xi ^ { \prime } \} \cdot \| \nabla f ( x _ { k } ) \| _ { 2 } .$$

For our derivative-free approach, we will define the gradient of function f as ∇ f ( x ) := ∇ x f ( x ) + ∇ σ f ( x ) , an additively separable gradient that decomposes into a term that corresponds to the analytical gradient ∇ x f ( x ) , and a term that corresponds to the error ∇ σ f ( x ) . In order to find the number of iterations required to reach convergence, we will consider the case where the algorithm converges with a finite differences gradient estimation (i.e. when the gradient is error-prone, represented by ∇ f ( x ) ), and use Theorem 3 of [53] which we state in Theorem 5 of this paper.

Theorem 5 (Thm 3 in [53]) Under Assumption 1 and Assumption 2, the generic Riemannian descent algorithm returns an error-prone x ∈ M satisfying f ( x ) ≤ f ( x 0 ) and ∥∇ f ( x ) ∥ 2 ≤ δ in

$$\left \lceil \frac { f ( x _ { 0 } ) - f ^ { * } } { \xi } \cdot \frac { 1 } { \delta ^ { 2 } } \right \rceil$$

iterations, provided ϵ ≤ ξ ′ ξ . If ρ &gt; ξ ′ ξ , at most ⌈ f ( x 0 ) -f ⋆ ξ · 1 δ ⌉ iterations are required.

Proof. If Algorithm 2 executes K -1 iterations without terminating, then ∥∇ f ( x k ) ∥ 2 &gt; δ for all k ∈ 0 , . . . , K -1 . Using Assumption 1 and Assumption 2 in a classic telescoping summation argument gives:

$$f ( x _ { 0 } ) - f ^ { * } & \geq f ( x _ { 0 } ) - f ( x _ { K } ) = \sum _ { k = 0 } ^ { K - 1 } f ( x _ { k } ) - f ( x _ { k + 1 } ) \\ & \stackrel { A ^ { 2 } } { \geq } \sum _ { k = 0 } ^ { K - 1 } \min \{ \xi \cdot \| \nabla f ( x _ { k } ) \| _ { 2 } , \, \xi ^ { \prime } \} \cdot \| \nabla f ( x _ { k } ) \| _ { 2 } \\ & \| \nabla f ( x _ { k } ) \| _ { 2 } \delta \sum _ { k = 0 } ^ { K - 1 } \min \{ \xi \cdot \delta , \, \xi ^ { \prime } \} \cdot \delta \\ & = K \min \{ \xi \cdot \delta , \xi ^ { \prime } \} \cdot \delta . \\ \intertext { y c o n t r a d i c t i o n , w h e n f ( x _ { 0 } ) - f ^ { * } \, \leq \, K \min \{ \xi \cdot \delta , \xi ^ { \prime } \} \cdot \delta , t h e a l g o r i m h w i l h a v e t r a m i n e d i n t i o n }$$

By contradiction, when f ( x 0 ) -f ⋆ ≤ K min { ξ · δ, ξ ′ } · δ , the algorithm will have terminated if K ≥ f ( x 0 ) -f ∗ min { ξδ,ξ ′ } δ .

The proofs for this section aim towards finding the conditions that satisfy Assumptions 1 and 2, and determine a convergence rate for an i -th agent using Theorem 5, which we finally state in Theorem 1. We resume by stating the convergence proofs of [29] that can be directly applied to our problem. Theorem L.1 proves that the PCA solution is the Unique strict-Nash Equilibrium as is stated in the following.

Theorem 6 (PCA Solution is the Unique strict-Nash Equilibrium). Assume that the top-k eigenvalues of X ⊤ X are positive and distinct. Then the top-k eigenvectors form the unique strict-Nash equilibrium of the proposed game in Equation (4) .

The theory from Section N of [29] can be directly applied to our problem, as the results presented there mainly depend on the utility function and are algorithm-independent. The main result from the mentioned section is contained in Theorem N.2, where a bound on the angular deviation of any maximizer of a child's utility given any deviation direction for the child or its parents is derived. Here we restate the theorem.

$$\text {Theorem} \, 7 \, \text { Assume it is given that } | \phi _ { j } | \leq \frac { c _ { i } g _ { i } } { ( i - 1 ) \Lambda _ { 1 1 } } \leq \sqrt { \frac { 1 } { 2 } } \, \text {for all } j < i \, \text {with } 0 \leq c _ { i } \leq \frac { 1 } { 1 6 } \, \text {.} \\ | \phi _ { i } ^ { * } | = | \arg \max \{ u _ { i } ( \hat { v } _ { i } ( \phi _ { i } , \Delta _ { i } ) , \hat { v } _ { j < i } ) \} | \leq 8 c _ { i } .$$

We can summarize the redefinition of u i (ˆ v i , v j&lt;i ) included in Section N of [29], which the authors use to determine initialization conditions for ϕ i . Lemma N.1 defines ˆ v i = cos( ϕ i ) v i +sin( ϕ i )∆ i in order to restate the utility function using

$$u _ { i } ( \hat { v } _ { i } , v _ { j < i } ) = u _ { i } ( v _ { i } , v _ { j < i } ) - \sin ^ { 2 } ( \phi _ { i } ) \left ( \Lambda _ { i i } - \sum _ { l > i } z _ { l } \Lambda _ { l l } u \right ) .$$

Lemma N.3 further redefines u i (ˆ v i , v j&lt;i ) as

$$u _ { i } ( \hat { v } _ { i } , v _ { j < i } ) = A ( \phi _ { j } , \Delta _ { j } , \Delta _ { i } ) \sin ^ { 2 } ( \phi _ { i } ) - B ( \phi _ { j } , \Delta _ { j } , \Delta _ { i } ) \frac { \sin ( 2 \phi _ { i } ) } { 2 } + C ( \phi _ { j } , \Delta _ { j } , \Delta _ { i } ) , \quad ( 3 0 )$$

and Lemma N.4 simplifies the previous expression into

$$u _ { i } ( \hat { v } _ { i } , v _ { j < i } ) = \frac { 1 } { 2 } \left [ \sqrt { A ^ { 2 } + B ^ { 2 } } \cos ( 2 \phi _ { i } + \gamma ) + A + 2 C \right ] ,$$

where ϕ = tan -1 ( B A ) .

LemmaO.7 also remains unchanged, and specifies an upper bound to the ratio of generalized inner products in Lemma 8 below. By using Lemma O.7 we may also state the Lipschitz bound of the gradient estimate similarly to Lemma O.8 in Lemma 9 below.

Lemma 8 Let | ϕ j | ≤ ϵ &lt; 1 for all j &lt; i . Then, the ratio of generalized inner products is bounded as:

<!-- formula-not-decoded -->

Lemma 9 (Lipschitz Bound). Let | ϕ j | ≤ ϵ &lt; 1 for all j &lt; i . Then, the norm of the approximate ambient gradient of u i is bounded as:

<!-- formula-not-decoded -->

Proof. Starting with the gradient (eq. 6), we find:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Weuse this previous result to provide a Lipschitz bound where the error is upper bounded, and we reach an expression dependent on the current agent i .

Lemma 10 (Lipschitz Bound with Accurate Parents) . Assume | ϕ j | ≤ ϵ ≤ c i g i ( i -1)Λ 11 ≤ √ 1 2 for all j &lt; i with 0 ≤ c i ≤ 1 16 . Then the norm of the ambient gradient of u i is bounded as:

∥ ˜ ∇ ˆ v i u i (ˆ v i , ˆ v j&lt;i ) ∥ 2 ≤ 4 (Λ 11 i +(1 + κ i -1 ) cg i ) + σ ( ∥ diag( M ) ∥ 2 +2( i -1)Λ 11 κ i -1 ) def = L i ( σ ) (36) where L i = 4[Λ 11 i +(1 + κ i -1 ) cg i ] when σ = 0 .

Proof. Starting with Lemma 9, we find:

<!-- formula-not-decoded -->

Corollary 11 (Bound on Utility) . Assume | ϕ j | ≤ c i g i ( i -1)Λ 11 ≤ √ 1 2 for all j &lt; i with 0 ≤ c i ≤ 1 16 . Then, the norm of the absolute value of the utility is bounded as follows:

$$| u _ { i } ( \hat { v } _ { i } , \hat { v } _ { j < i } ) | = | \hat { v } _ { i } ^ { \top } \nabla _ { \hat { v } _ { i } } | \leq \| \hat { v } _ { i } \| _ { 2 } \cdot \| \nabla _ { \hat { v } _ { i } } \| _ { 2 } = \| \nabla _ { \hat { v } _ { i } } \| _ { 2 } \approx \| \tilde { \nabla } _ { \hat { v } _ { i } } \| _ { 2 } \leq L _ { i } ( \sigma ) ,$$

thereby approximately satisfying Assumption 1.

Lemma 12 Assume | ϕ j | ≤ c i g i ( i -1)Λ 11 ≤ √ 1 2 for all j &lt; i with 0 ≤ c i ≤ 1 16 . Then Assumption 2 is approximately satisfied with ξ = ξ ′ = 8 5 L i ( σ ) . The proof is developed in Lemma O.10 of [29].

We now shift our focus towards defining an accuracy for | ϕ i | . Lemma 13 defines a somewhat general target accuracy which acts as a criteria for reasonable approximate optimization. Lemma 14 provides upper bounds for the difference between one agent's estimated value for θ and its optimal value for an inaccurate gradient calculation that includes finite differences. These directly correspond to O.11 and O.12 of [29], respectively. The proof continues with Lemma 15 where a number of iterations is given for convergence of an agent's cost function, and ends on Theorem 1 with the finite sample convergence rate for all agents.

Lemma 13 (Approximate Optimization is Reasonable Given Accurate Parents) . Assume | ϕ j | ≤ c i g i ( i -1)Λ 11 ≤ √ 1 2 for all j &lt; i with 0 ≤ c i ≤ 1 16 . i.e., the parents have been learned accurately. Then for any approximate local maximizer ( ¯ ϕ i , ¯ ∆ i ) of u i (ˆ v i ( ϕ i , ∆ i ) , ˆ v j&lt;i ) , if the angular deviation | ¯ ϕ i -ϕ ∗ i | ≤ ¯ e where θ ∗ i forms the global max:

$$| \bar { \phi } _ { i } | \leq \bar { e } + 8 c _ { i }$$

where ¯ ϕ i denotes the angular distance of the approximate local maximizer to the true eigenvector v i .

Lemma 14 Assume ˆ v i is within π 4 of its maximizer, i.e., | ϕ i -ϕ ∗ i | ≤ π 4 . Also, assume that | ϕ j&lt;i | ≤ c i g i ( i -1)Λ 11 ≤ √ 1 2 with 0 ≤ c i ≤ 1 16 . Then the norm of the Riemannian gradient of u i upper bounds this angular deviation:

$$| \phi _ { i } - \phi _ { i } ^ { * } | \leq \frac { \pi } { g _ { i } } \| \nabla _ { \hat { v } _ { i } } ^ { R } u _ { i } ( \hat { v } _ { i } , \hat { v } _ { j < i } ) \| _ { 2 }$$

We now use ∇ f ( x ) = ∇ f ( x ) x + ∇ f ( x ) σ to state the following lemma.

Lemma 15 Assume ˆ v i is initialized within π 4 of its maximizer and its parents are accurate enough, i.e., that | ϕ j&lt;i | ≤ c i g i ( i -1)Λ 11 ≤ √ 1 2 with 0 ≤ c i ≤ 1 16 . Let δ i = ρ i -∥ ˜ ∇ ˆ v i f (ˆ v i | ˆ v j&lt;i ) σ ∥ 2 be the maximum tolerated error desired for ˆ v i . Then finite-differences Riemannian gradient ascent returns:

$$| \phi _ { i } | \leq \frac { \pi } { g _ { i } } \delta _ { i } + 8 c _ { i } ,$$

after at most ⌈ 5 L i (0) 4 L i ( σ ) · 1 δ 2 i ⌉ iterations.

Proof. The assumptions of Theorem 5 are approximately met by Corollary 11 and Lemma 12 with ξ = ξ ′ = 8 5 using Riemannian gradient ascent. Theorem 5 thus ensures that Riemannian gradient ascent returns unit vector ˆ v i satisfying u (ˆ v i ) ≥ u (ˆ v 0 i ) and ∥∇ R ∥ 2 ≤ δ i in at most:

$$\left \lceil \frac { u ( \hat { v } _ { i } ^ { * } ) - u ( \hat { v } _ { i } ^ { 0 } ) } { \frac { 8 } { 5 } L _ { i } ( \sigma ) } \cdot \frac { 1 } { \delta _ { i } ^ { 2 } } \right \rceil$$

iterations (where ˆ v i is initialized to ˆ v 0 i ). Also, for any ˆ v i , u i (ˆ v ∗ i ) -u i (ˆ v i ) ≤ 2 L i ( σ ) where L i ( σ ) bounds the absolute value of the utility u i (see Corollary 11) and ˆ v ∗ i = arg max u i (ˆ v i ) . Combining this with Lemma 14 gives:

$$| \phi _ { i } - \phi _ { i } ^ { * } | \leq \frac { \pi } { g _ { i } } \delta _ { i }$$

after at most ⌈ 5 L i (0) 4 L i ( σ ) · 1 δ 2 i ⌉ iterations. We then use Lemma 13 to yield | ϕ i | ≤ π g i δ i + 8 c i in the said amount of iterations.

## D. Proof of the main 0 th -order convergence theorem

We state our finite sample convergence theorem on the 0 th -order EigenGame for all players.

(Convergence of 0 th -order EigenGame for all players). Consider the Algorithm 4 with input matrix M ∈ R p × p and learned 'parent' eigenvectors v j&lt;i ∈ R p that are accurate enough, i.e., that | ϕ j&lt;i | ≤ c i g i ( i -1)Λ 11 ≤ √ 1 2 with 0 ≤ c i ≤ 1 16 . Let the initialization vector v i, init be within perturbation π 4 from v ⋆ i , i.e., ∠ ( v i, init , v ⋆ i ) ≤ π 4 , for all i . Consider perturbation σ ∈ R for the finite difference approximation, and step size α for the gradient ascent. Then, Algorithm 4 returns an approximate eigenvector v i with angular error less than ϕ tol &gt; 0 in:

$$T = \left \lceil \mathcal { O } \left ( \sum _ { i = 1 } ^ { k } \frac { L _ { i } ( 0 ) } { L _ { i } ( \sigma ) } \left [ \frac { ( k - 1 ) ! } { \phi _ { i n } } \prod _ { j = 1 } ^ { k } \left ( \frac { 1 6 \Lambda _ { 1 1 } } { g _ { j } } \right ) \right ] ^ { 2 } \right ) \right \rceil \quad i t e r a t i o n s ,$$

where L i ( σ ) is the Lipschitz continuity assumption of the 0 th -order EigenGame based on a finite difference step size σ as in ∥ ˜ ∇ v i f ( v i | v j&lt;i ) ∥ 2 ≤ L i ( σ ) , Λ is the diagonal eigenvalue matrix of M containing eigenvalues Λ 11 &gt; Λ 22 &gt; . . . &gt; Λ kk with Λ 11 being the top eigenvalue, and g i = Λ ii -Λ i +1 ,i +1 is the eigengap between the two consecutive eigenvalues of players i and i +1 .

Proof. Let | ϕ j&lt;i | ≤ c i g i ( i -1)Λ 11 ≤ √ 1 2 with c k ≤ 1 16 for all j &lt; k and let the initialization vector v i, init be within perturbation π 4 from v ⋆ i , i.e., ∠ ( v i, init , v ⋆ i ) ≤ π 4 . Lemma 13 defines a bound for the angular error in ˆ v k obtained from Riemmanian gradient descent as:

$$| \bar { \phi } _ { i } | \leq \bar { e } + 8 c _ { i }$$

where ¯ e quantifies the convergence error and 8 c i the error propagated by the parents. Let half the error of | θ k | come from imperfect parents ˆ v j&lt;k and half come from the convergence error of the k -th agent. Also, let each parent be learned accurately enough, and the error from learning ˆ v i -1 be less than the threshold of any of its succesors. Per [29], the error from ˆ v i -1 's parents can be bounded as

$$c _ { i - 1 } \leq \frac { c _ { i } g _ { i } } { 1 6 ( i - 1 ) \Lambda _ { 1 1 } } ,$$

which recursively leads to a bound on c i through:

$$c _ { i } \leq \frac { ( i - 1 ) ! \prod _ { j = i + 1 } ^ { k } g _ { j } } { ( 1 6 \Lambda _ { 1 1 } ) ^ { k - i } ( k - 1 ) ! } c _ { k } ,$$

which would satisfy the requirement for accurate parents in ˆ v i 's error bound. We may then bound the convergence error of the i -th agent as:

$$\rho \leq \left [ \frac { g _ { i } g _ { i + 1 } } { 2 \pi i \Lambda _ { 1 1 } } \right ] c _ { i + 1 } ,$$

$$t _ { i } = \left \lceil \frac { 5 L _ { i } ( 0 ) } { L _ { i } ( \sigma ) } \left ( \frac { \pi i \Lambda _ { 1 1 } } { g _ { i } g _ { i + 1 } } \right ) ^ { 2 } \frac { 1 } { c _ { i + 1 } ^ { 2 } } \right \rceil$$

iterations through Lemma 15. We can then input eq. 46 to obtain

with at most

$$t _ { i } & = \left \lceil \frac { 5 L _ { i } ( 0 ) } { L _ { i } ( \sigma ) } \left ( \frac { \pi i \Lambda _ { 1 1 } } { g _ { i } g _ { i + 1 } } \right ) ^ { 2 } \frac { ( 1 6 \Lambda _ { 1 1 } ) ^ { 2 ( k - i - 1 ) } ( ( k - 1 ) ! ) ^ { 2 } } { ( i ! ) ^ { 2 } \prod _ { j = i + 2 } ^ { k } g _ { j } ^ { 2 } } \frac { 1 } { c _ { k } ^ { 2 } } \right \rceil \\ & = \left \lceil \frac { 5 \pi ^ { 2 } L _ { i } ( 0 ) } { L _ { i } ( \sigma ) } \frac { 1 6 ^ { 2 ( k - i ) } \Lambda _ { 1 1 } ^ { ( k - i ) } ( ( k - 1 ) ! ) ^ { 2 } } { ( \prod _ { j = i } ^ { k } g _ { j } ^ { 2 } ) ( ( i - 1 ) ! ) ^ { 2 } } - \frac { 1 } { ( 1 6 c _ { k } ) ^ { 2 } } \right \rceil \\ & \leq \left | \frac { 5 \pi ^ { 2 } L _ { i } ( 0 ) } { L _ { i } ( \sigma ) } \left [ \frac { ( 1 6 \Lambda _ { 1 1 } ) ^ { k - 1 } ( k - 1 ) ! } { \prod _ { j = 1 } ^ { k } g _ { j } } \frac { 1 } { 1 6 c _ { k } } \right ] , \quad \Lambda _ { 1 1 } \geq g _ { i } \quad \forall i \\ & = \left \lceil O \left ( \frac { L _ { i } ( 0 ) } { L _ { i } ( \sigma ) } \left [ \frac { ( 1 6 \Lambda _ { 1 1 } ) ^ { k - 1 } ( k - 1 ) ! } { \prod _ { j = 1 } ^ { k } g _ { j } } \frac { 1 } { 1 6 c _ { k } } \right ] \right ) \right \rceil \\ \intertext { a n g a t e i . $ $ $ $ } \text {any agent } i . $ $ $ $ } \text {the total number of iterations to learn } \hat { v } _ { j < k } \text { is thus }$$

for any agent i . The total number of iterations to learn ˆ v j&lt;k is thus

$$T _ { k } = \left \lceil \mathcal { O } \left ( \sum _ { i = 1 } ^ { k } \frac { L _ { i } ( 0 ) } { L _ { i } ( \sigma ) } \left [ \frac { ( 1 6 \Lambda _ { 1 1 } ) ^ { k - 1 } ( k - 1 ) ! } { \prod _ { j = 1 } ^ { k } g _ { j } } \frac { 1 } { 1 6 c _ { k } } \right ] ^ { 2 } \right ) \right \rceil .$$

## E. Parameterized convergence analysis

The generic Riemannian descent convergence analysis of [29] is analyzed in the context of a parameterized EigenGame in this section, given that x = v ( θ ) = | ψ ( θ ) ⟩ with x ∈ M = R n , and θ ∈ M = R ℓ × q over ℓ layers and q qubits representing the parameters of an ansatz U ( θ ) that prepares a state via v ( θ ) = U ( θ ) | s ⟩ . We choose to use v ( θ ) instead of | ψ ( θ ) ⟩ for the proofs to facilitate analysis. Particularly, Assumptions 1 and 2 remain unchanged for θ .

The θ parameters do not require any explicit projection for | ψ ( θ ) ⟩ to lie within the unit sphere S n -1 , and the design decision for Assumption 3 becomes a strict statement. Hence, we restate Assumption 3 in the following.

$$\text {Lemma 16 (Non-projection). For all $k \geq 0,\forall \theta \in \mathcal { M } = \mathbb { R } ^ { \ell \times q } ,} \\ \nabla ^ { R } f ( \theta _ { k } ) = \nabla f ( \theta _ { k } ) .$$

The proofs for the parameterized EigenGame stems from the generic Riemannian descent convergence of Theorem 5, with a similar approach as in the 0 th -order case, with a rate of convergence for a particular agent i in Lemma 22, and a finite sample convergence rate for all agents in Theorem 2. The remainder of the proofs from Appendix C remain unchanged except for those we restate in the rest of this section.

Lemma 17 (Parameterized Lipschitz Bound) . Let | ϕ j | ≤ ϵ &lt; 1 for all j &lt; i . Assume J ˆ θ ikl = ∂v ( ˆ θ i ) ∂ ˆ θ ikl = U ′ ( ˆ θ i ) | s ⟩ ∈ C n where ∥ ∥ ∥ J ˆ θ ikl ∥ ∥ ∥ = 1 . Then the norm of the ambient gradient of u i is bounded as:

$$\| \nabla _ { \hat { \theta } _ { i } } u _ { i } ( v ( \hat { \theta } _ { i } ) , v ( \hat { \theta } _ { j < i } ) ) \| \leq 2 \sqrt { \ell } q \Lambda _ { 1 1 } \left ( 1 + ( i - 1 ) \frac { 1 + ( 1 + \kappa _ { i - 1 } ) \epsilon } { \sqrt { 1 - \epsilon ^ { 2 } } } \right ) .$$

Proof. Westart by defining the gradient of the utility with respect to ˆ θ i and relating it to the gradient with respect to v ( ˆ θ i ) as follows:

$$\nabla _ { \hat { \theta } _ { i } } u _ { i } ( v ( \hat { \theta } _ { i } ) , v ( \hat { \theta } _ { j < i } ) ) = \frac { d u _ { i } } { d v } \frac { d v } { d \hat { \theta } _ { i } } = J _ { \hat { \theta } _ { i } } \nabla _ { v ( \hat { \theta } _ { i } ) } u _ { i } ( v ( \hat { \theta } _ { i } ) , v ( \hat { \theta } _ { j < i } ) ) ,$$

where

$$J _ { \hat { \theta } _ { i } } = \underbrace { \left [ - \, \frac { \partial v ( \hat { \theta } _ { i } ) } { \partial \hat { \theta } _ { i k l } } \, - \right ] } _ { \ell \times q } .$$

We proceed by including the number of layers ℓ and qubits q in the new upper bound:

$$We proceed by including the number of layers \ell \, and \, q \, \text {bits} \, q \text { in the new upper bound:} \\ \| \nabla _ { \hat { \theta } _ { i } } u _ { i } ( v ( \hat { \theta } _ { i } ) , v ( \hat { \theta } _ { j < i } ) ) \| _ { 2 } & = \left \| J _ { \hat { \theta } _ { i } } \nabla _ { v ( \hat { \theta } _ { i } ) } u _ { i } ( v ( \hat { \theta } _ { i } ) , v ( \hat { \theta } _ { j < i } ) ) \right \| _ { 2 } \\ & \leq 2 \left \| J _ { \hat { \theta } _ { i } } \right \| _ { 2 } \cdot \left \| M \left ( v ( \hat { \theta } _ { i } ) - \sum _ { j < i } \frac { v ( \hat { \theta } _ { i } ) ^ { \dagger } M v ( \hat { \theta } _ { j } ) } { v ( \hat { \theta } _ { j } ) ^ { \dagger } M v ( \hat { \theta } _ { j } ) } v ( \hat { \theta } _ { j } ) \right ) \right \| _ { 2 } \\ & \stackrel { L ^ { 9 } } { \leq } 2 \left \| J _ { \hat { \theta } _ { i } } \right \| _ { 2 } \cdot \Lambda _ { 1 1 } \left ( 1 + ( i - 1 ) \frac { 1 + ( 1 + \kappa _ { i - 1 } ) \epsilon } { \sqrt { 1 - \epsilon ^ { 2 } } } \right ) \\ & = 2 \sqrt { \ell } q \Lambda _ { 1 1 } \left ( 1 + ( i - 1 ) \frac { 1 + ( 1 + \kappa _ { i - 1 } ) \epsilon } { \sqrt { 1 - \epsilon ^ { 2 } } } \right ) . \\ \intertext { W e p o w u p e r $ o u n d $ t h e r $ o r $ a n d $ i n p s h i z t $ } \text {We now upper bound the error and define a } I \, \text {inspectivity} \, \text {containing $bound$ for agent } i \\$$

We now upper bound the error and define a Lipschitz continuity bound for agent i .

Lemma 18 (Parameterized Lipschitz Bound with Accurate Parents) . Assume | ϕ j | ≤ ϵ ≤ c i g i ( i -1)Λ 11 ≤ √ 1 2 for all j &lt; i with 0 ≤ c i ≤ 1 16 , and J ˆ θ ikl = ∂v ( ˆ θ i ) ∂ ˆ θ ikl = U ′ ( ˆ θ i ) | s ⟩ ∈ C n where ∥ ∥ ∥ J ˆ θ ikl ∥ ∥ ∥ = 1 . Then the norm of the ambient gradient of u i is bounded as:

$$\| \nabla _ { \hat { \theta } _ { i } } u _ { i } ( v ( \hat { \theta } _ { i } ) , v ( \hat { \theta } _ { j < i } ) ) \| _ { 2 } \leq 4 \sqrt { \ell } q \left [ \Lambda _ { 1 1 } i + ( 1 + \kappa _ { i - 1 } ) c g _ { i } \right ] = \sqrt { \ell } q L _ { i } \stackrel { d e f } { = } L _ { \theta _ { i } } .$$

Proof. Starting with Lemma 17 and using the derivation for the first term of Lemma 10 we find:

$$\| \nabla _ { \hat { \sigma } _ { i } } u _ { i } ( v ( \hat { \sigma } _ { i } ) , v ( \hat { \sigma } _ { j < i } ) ) \| _ { 2 } & \leq 2 \sqrt { \ell } q \Lambda _ { 1 1 } \left ( 1 + ( i - 1 ) \frac { 1 + ( 1 + \kappa _ { i - 1 } ) \epsilon } { \sqrt { 1 - \epsilon ^ { 2 } } } \right ) \\ & \leq 4 \sqrt { \ell } q \left ( \Lambda _ { 1 1 } i + ( 1 + \kappa _ { i - 1 } ) c g _ { i } \right ) \\ & \stackrel { C 1 1 } { = } \sqrt { \ell } q L _ { i } .$$

We redefine the notation of Corollary 11 by accounting for the ansatz parameters ˆ θ .

Corollary 19 (Parameterized Bound on Utility) . Assume | ϕ j | ≤ c i g i ( i -1)Λ 11 ≤ √ 1 2 for all j &lt; i with 0 ≤ c i ≤ 1 16 . Then the norm of the absolute value of the utility is bounded as follows:

$$| u _ { i } ( v ( \hat { \theta } _ { i } ) , v ( \hat { \theta } _ { j < i } ) ) | = | v ( \hat { \theta } _ { i } ) ^ { \dagger } \nabla _ { v ( \hat { \theta } _ { i } ) } | \leq \| v ( \hat { \theta } _ { i } ) \| _ { 2 } \cdot \| \nabla _ { v ( \hat { \theta } _ { i } ) } \| _ { 2 } = \| \nabla _ { v ( \hat { \theta } _ { i } ) } \| _ { 2 } \leq D _ { i } ,$$

Lemma 20 Assume | ϕ j | ≤ c i g i ( i -1)Λ 11 ≤ √ 1 2 for all j &lt; i with 0 ≤ c i ≤ 1 16 . Then Assumption 2 is approximately satisfied with ξ = ξ ′ = 1 2 L θ i .

Proof. Let ω = α ∇ ˆ θ i u i ( ˆ θ i ) , α &gt; 0 . Using the first-order Taylor approximation of u i ( ˆ θ i + ω ) :

$$u _ { i } ( \hat { \theta } _ { i } + \omega ) & \approx u _ { i } ( \hat { \theta } _ { i } ) + \nabla _ { \hat { \theta } _ { i } } u _ { i } ( \hat { \theta } _ { i } ) ^ { \dagger } \omega \\ & = u _ { i } ( \hat { \theta } _ { i } ) + \alpha \nabla _ { \hat { \theta } _ { i } } u _ { i } ( \hat { \theta } _ { i } ) ^ { \dagger } \nabla _ { \hat { \theta } _ { i } } u _ { i } ( \hat { \theta } _ { i } ) \\ & = u _ { i } ( \hat { \theta } _ { i } ) + \alpha \| \nabla _ { \hat { \theta } _ { i } } u _ { i } ( \hat { \theta } _ { i } ) \| ^ { 2 } .$$

We may now lower bound the utility difference as follows. Let α = 1 2 L θ i , then:

$$u _ { i } ( \hat { \theta } _ { i } + \omega ) - u _ { i } ( \hat { \theta } _ { i } ) & \approx u _ { i } ( \hat { \theta } _ { i } ) + \alpha \| \nabla _ { \theta _ { i } } u _ { i } ( \hat { \theta } _ { i } ) \| ^ { 2 } - u _ { i } ( \hat { \theta } _ { i } ) \\ & = \alpha \| \nabla _ { \hat { \theta } _ { i } } u _ { i } ( \hat { \theta } _ { i } ) \| ^ { 2 } \\ & \geq \min ( \alpha , \alpha \| \nabla _ { \hat { \theta } _ { i } } u _ { i } ( \hat { \theta } _ { i } ) \| ) \| \nabla _ { \theta _ { i } } u _ { i } ( \hat { \theta } _ { i } ) \| \\ & = \min ( \xi , \xi ^ { \prime } \| \nabla _ { \hat { \theta } _ { i } } u _ { i } ( \hat { \theta } _ { i } ) \| ) \| \nabla _ { \hat { \theta } _ { i } } u _ { i } ( \hat { \theta } _ { i } ) \|$$

with ξ = ξ ′ = α = 1 2 L θ i .

Lemma 21 Assume | ˆ v ( θ i ) ⟩ is within π 4 of its maximizer, i.e., | ϕ i -ϕ ∗ i | ≤ π 4 . Also, assume that | ϕ j&lt;i | ≤ c i g i ( i -1)Λ 11 ≤ √ 1 2 with 0 ≤ c i ≤ 1 16 . Then the norm of the Riemannian gradient of u i upper bounds this angular deviation:

$$| \phi _ { i } - \phi _ { i } ^ { * } | \leq \frac { \pi } { g _ { i } } \| \nabla _ { \hat { \theta } _ { i } } u _ { i } ( | v ( \hat { \theta } _ { i } ) \rangle , | v ( \hat { \theta } _ { j < i } ) \rangle ) \|$$

Lemma 22 Assume | v ( ˆ θ i ) ⟩ is initialized within π 4 of its maximizer and its parents are accurate enough, i.e., that | ϕ j&lt;i | ≤ c i g i ( i -1)Λ 11 ≤ √ 1 2 with 0 ≤ c i ≤ 1 16 . Let ρ i be the maximum tolerated error desired for ˆ θ i . Then Riemannian gradient ascent returns:

after at most

iterations.

Proof. We input the results of Corollary 19 and Lemma 20 into Lemma 5, thus satisfying Assumptions 1 and 2, respectively, to provide an upper bound on the number of iterations required for Riemannian gradient ascent to reach convergence in the following. Given ξ = ξ ′ = α = 1 2 L θ i from Lemma20, we reach a set of parameters ϕ that satisfy u ( v ( ˆ θ i )) ≥ u ( v ( ˆ θ 0 i )) and ∥∇ ˆ θ i ∥ ≤ ρ i in at most:

$$\left \lceil \frac { u ( v ( \hat { \theta } _ { i } ^ { * } ) ) - u ( v ( \hat { \theta } _ { i } ^ { 0 } ) ) } { 1 / 2 L _ { \theta _ { i } } } \cdot \frac { 1 } { \rho _ { i } ^ { 2 } } \right \rceil$$

iterations. We may now use Corollary 19 to specify u ( v ( ˆ θ ∗ i )) -u ( v ( ˆ θ 0 i )) ≤ 2 L i = 2 L θ i / √ ℓq where:

in at most:

iterations.

$$| \phi _ { i } - \phi _ { i } ^ { * } | & \leq \frac { \pi } { g _ { i } } \rho _ { i }$$

$$\left \lceil \frac { 4 L _ { \theta _ { i } } } { \sqrt { \ell q } } \cdot \frac { 1 } { \rho _ { i } ^ { 2 } } \right \rceil$$

## F. Proof of the main parameterized convergence theorem

(Convergence of QuantumGame for all players). Algorithm 3 achieves finite sample convergence to within ϕ tol angular error of the topk principal components independent of initialization. Let | ϕ j&lt;i | ≤ c i g i ( i -1)Λ 11 ≤ √ 1 2 with 0 ≤ c i ≤ 1 16 . Let each v ( ˆ θ i ) = U ( ˆ θ i ) | s ⟩ , with a sufficiently expressive ansatz U ( ˆ θ i ) [46, 47] and an initial state | s ⟩ such that ∠ ( v ( ˆ θ i ) , v ⋆ i ) ≤ π 4 . Algorithm 3 returns the eigenvectors with angular error less than ϕ tol in:

$$T = \left \lceil \mathcal { O } \left ( \sum _ { i = 1 } ^ { k } \frac { L _ { \theta _ { i } } } { \sqrt { \ell q } } \left [ \frac { ( k - 1 ) ! } { \phi _ { t o l } } \prod _ { j = 1 } ^ { k } \left ( \frac { 1 6 \Lambda _ { u 1 } } { g _ { j } } \right ) \right ] ^ { 2 } \right ) \right \rceil \quad t i r a t i o n s ,$$

$$| \phi _ { i } | \leq \frac { \pi } { g _ { i } } \rho _ { i } + 8 c _ { i }$$

$$\left \lceil \frac { 4 L _ { \theta _ { i } } } { \sqrt { \ell q } } \cdot \frac { 1 } { \rho _ { i } ^ { 2 } } \right \rceil$$

where L θ i is the Lipschitz continuity constant of QuantumGame, ℓ is the number of layers of the ansatz and q is the number of qubits.

Proof. Let | ϕ j&lt;i | ≤ c i g i ( i -1)Λ 11 ≤ √ 1 2 with c k ≤ 1 16 for all j &lt; k and let the initialization vector v i, init be within perturbation π 4 from v ⋆ i , i.e., ∠ ( v i, init , v ⋆ i ) ≤ π 4 . Using the same convergence error bound for the i -th agent:

$$\rho \leq \left [ \frac { g _ { i } g _ { i + 1 } } { 2 \pi i \Lambda _ { 1 1 } } \right ] c _ { i + 1 }$$

from Theorem 1, convergence is reached in at most:

$$t _ { i } = \left \lceil \frac { 4 L _ { \theta _ { i } } } { \sqrt { \ell \bar { q } } } \left ( \frac { \pi i \Lambda _ { 1 1 } } { g _ { i } g _ { i + 1 } } \right ) ^ { 2 } \frac { 1 } { c _ { i + 1 } ^ { 2 } } \right \rceil$$

iterations using Lemma 22. The total numer of iterations required to reach finite sample convergence for all players with eigenvectors v ( ˆ θ ) j&lt;k is then:

$$T _ { k } = \left \lceil \mathcal { O } \left ( \sum _ { i = 1 } ^ { k } \frac { L _ { \theta _ { i } } } { \sqrt { \ell q } } \left [ \frac { ( 1 6 \Lambda _ { 1 1 } ) ^ { k - 1 } ( k - 1 ) ! } { \prod _ { j = 1 } ^ { k } g _ { j } } \frac { 1 } { 1 6 c _ { k } } \right ] ^ { 2 } \right ) \right \rceil .$$

## G. Error accumulation

Theorem 23 Assume the angular error ϕ j ≤ ϵ between the true eigenvector of a parent v j and its estimate ˆ v j to satisfy ϵ ≪ 1 such that the length of the cord that connects both vectors is l = | ˆ v j -v j | = 2 sin ( ϵ 2 ) for the Euclidean error of the parent to be O ( ϵ ) . The Euclidean error of the child's 0 th -order gradient is O ( ϵ ) and is expressed as:

$$\| b \| & = \| \nabla _ { \hat { v } _ { j } } ^ { R } u ( \hat { v } _ { j } | \hat { v } _ { j } < i ) - \nabla _ { \hat { v } _ { j } } ^ { R } u ( \hat { v } _ { j } | v _ { j } < i ) \| \\ & \leq 2 \, \| M \| \sum _ { j < i } ( \| v _ { j } w _ { j } ^ { \top } \| + \| w _ { j } v _ { j } ^ { \top } \| + \| w _ { j } w _ { j } ^ { \top } \| ) \, \frac { \Lambda _ { u } } { \Lambda _ { j } } + \sigma \sum _ { j < i } ( 2 \, \| M v _ { j } \| \, \| M w _ { j } \| + \| M w _ { j } \| ^ { 2 } ) \, \frac { 1 } { \Lambda _ { j j } } \, .$$

Proof. Let b be the difference between the Riemannian gradient with approximate parents and that with exact parents. We can specify ˆ v j = v j + w j where w j is the vector that represents the misspecification error of ˆ v j , and proceed by bounding b in the following:

$$b = \nabla _ { \hat { v } _ { i } } ^ { R } u ( \hat { v } _ { i } | \hat { v } _ { j < i } ) - \nabla _ { \hat { v } _ { i } } ^ { R } u ( \hat { v } _ { i } | v _ { j < i } )$$

$$= ( I - \hat { v } _ { i } \hat { v } _ { i } ^ { \top } ) \left [ 2 M \left ( \hat { v } _ { i } - \sum _ { j < i } \frac { \hat { v } _ { i } ^ { \top } M \hat { v } _ { i } } { \hat { v } _ { j } ^ { \bot } M \hat { v } _ { j } } \hat { v } _ { j } \right ) + \sigma \left ( \text {diag} ( M ) - \sum _ { j < i } \frac { ( M \hat { v } _ { j } ) ^ { \circ 2 } } { \hat { v } _ { j } ^ { \bot } M \hat { v } _ { j } } \right )$$

$$- \, 2 M \left ( \hat { v } _ { i } - \sum _ { j < i } \frac { \hat { v } _ { i } ^ { \top } M v _ { j } } { v _ { j } ^ { \top } M v _ { j } } v _ { j } \right ) + \sigma \left ( \text {diag} ( M ) - \sum _ { j < i } \frac { ( M v _ { j } ) ^ { \circ 2 } } { v _ { j } ^ { \top } M v _ { j } } \right ) \right ]$$

$$= \left ( I - \hat { v } _ { i } \hat { v } _ { i } ^ { \top } \right ) \left [ 2 M \left ( \sum _ { j < i } \frac { \hat { v } _ { j } ^ { \top } M v _ { j } } { v _ { j } ^ { \frac { \tau } { M } } v _ { j } } v _ { j } - \sum _ { j < i } \frac { \hat { v } _ { j } ^ { \top } M \hat { v } _ { j } } { \hat { v } _ { j } ^ { \frac { \tau } { M } } \hat { v } _ { j } } \hat { v } _ { j } \right ) + \sigma \left ( \sum _ { j < i } \frac { ( M v _ { j } ) ^ { \circ 2 } } { v _ { j } ^ { \top } M v _ { j } } - \sum _ { j < i } \frac { ( M \hat { v } _ { j } ) ^ { \circ 2 } } { \hat { v } _ { j } ^ { \ast } M \hat { v } _ { j } } \right ) \right ] ,$$

$$( 7 2 ) \\ ( 7 3 ) \\ ( 7 4 ) \\ ( 7 5 )$$

where the norm of the difference is

$$where the n o r of the d i f f e n c e i s \\ \| b \| & = \left \| ( I - \hat { v } _ { i } \hat { v } _ { i } ^ { T } ) \left ( 2 M \left ( \sum _ { j < i } \frac { \hat { v } _ { j } ^ { T } M _ { v _ { j } } } { M _ { v _ { j } } } \hat { v } _ { j } - \sum _ { j < i } \frac { \hat { v } _ { i } ^ { T } M _ { i _ { j } } } { M _ { i _ { j } } } \hat { v } _ { i _ { j } } \right ) \right ) + \sigma \left ( \sum _ { j < i } \frac { ( M _ { v _ { j } } ) ^ { 2 } } { M _ { v _ { j } } } - \sum _ { j < i } \frac { ( M _ { i _ { j } } ) ^ { 2 } } { M _ { i _ { j } } } \right ) \right ) \right \| _ { 2 } \\ & \leq \| ( I - \hat { v } _ { i } \hat { v } _ { i } ^ { T } ) \| _ { 2 } \cdot \left \| 2 M \left ( \sum _ { j < i } \frac { \hat { v } _ { i } ^ { T } M _ { v _ { j } } } { M _ { v _ { j } } } \hat { v } _ { j } - \sum _ { j < i } \frac { \hat { v } _ { i } ^ { T } M _ { i _ { j } } } { M _ { i _ { j } } } \hat { v } _ { i _ { j } } \right ) + \sigma \left ( \sum _ { j < i } \frac { ( M _ { v _ { j } } ) ^ { 2 } } { M _ { v _ { j } } } - \sum _ { j < i } \frac { ( M _ { i _ { j } } ) ^ { 2 } } { M _ { i _ { j } } } \right ) \right \| _ { 2 } \\ & \leq \left \| 2 M \left ( \sum _ { j < i } \frac { \hat { v } _ { i } ^ { T } M _ { v _ { j } } } { M _ { v _ { j } } } \hat { v } _ { j } - \sum _ { j < i } \frac { \hat { v } _ { i } ^ { T } M _ { i _ { j } } } { M _ { i _ { j } } } \hat { v } _ { i _ { j } } \right ) + \sigma \left ( \sum _ { j < i } \frac { ( M _ { v _ { j } } ) ^ { 2 } } { M _ { v _ { j } } } - \sum _ { j < i } \frac { ( M _ { i _ { j } } ) ^ { 2 } } { M _ { i _ { j } } } \right ) \right \| _ { 2 } \\ & = \left \| 2 M \left ( \sum _ { j < i } \frac { \hat { v } _ { i } ^ { T } M _ { v _ { j } } } { M _ { i _ { j } } } \hat { v } _ { j } - \sum _ { j < i } \frac { \hat { v } _ { i } ^ { T } M _ { i _ { j } } } { M _ { i _ { j } } } \hat { v } _ { i _ { j } } \right ) + \sigma \left ( \sum _ { j < i } \frac { ( M _ { v _ { j } } ) ^ { 2 } } { M _ { i _ { j } } } - \sum _ { j < i } \frac { ( M _ { i _ { j } } ) ^ { 2 } } { M _ { i _ { j } } } \right ) \right \| _ { 2 } \\ & \quad \left \| \left ( - \sum _ { i } \bar { T } _ { i _ { j } } - \sum _ { j < i } \bar { T } _ { i _ { j } } \right ) \right ) \left ( - \sum _ { i } \bar { v } _ { i _ { j } } \right ) + \sigma \left ( - \sum _ { i } \bar { v } _ { i _ { j } } \right ) - \sum _ { j < i } \frac { ( M _ { i _ { j } } ) ^ { 2 } } { M _ { i _ { j } } } \right ) \right \| _ { 2 } \\$$

$$& \leq \left \| 2 M \left ( \sum _ { j < i } \frac { \hat { v } _ { i j } ^ { \intercal } M v _ { i } } { \Lambda _ { j j } } v _ { j } - \sum _ { j < i } \frac { \hat { v } _ { i } ^ { \intercal } M \hat { v } _ { i } } { \Lambda _ { j j } } \hat { v } _ { j } \right ) + \sigma \left ( \sum _ { j < i } \frac { ( M v _ { j } ) ^ { \sigma ^ { 2 } } } { \Lambda _ { j j } } - \sum _ { j < i } \frac { ( M \hat { v } _ { j } ) ^ { \sigma ^ { 2 } } } { \Lambda _ { j j } } \right ) \right \| \\ & \quad \stackrel { \dots } { \leq } \left \| 2 M \left ( \sum _ { j < i } \frac { \hat { v } _ { i j } ^ { \intercal } M v _ { i } } { \Lambda _ { j j } } v _ { j } - \sum _ { j < i } \frac { \hat { v } _ { i } ^ { \intercal } M \hat { v } _ { i } } { \Lambda _ { j j } } \hat { v } _ { j } \right ) + \sigma \left ( \sum _ { j < i } \frac { ( M v _ { j } ) ^ { \sigma ^ { 2 } } } { \Lambda _ { j j } } - \sum _ { j < i } \frac { ( M \hat { v } _ { j } ) ^ { \sigma ^ { 2 } } } { \Lambda _ { j j } } \right ) \right \|$$

$$& \leq 2 \left \| M \right \| \sum _ { j < i } \left \| \frac { \tt t ^ { \Psi } _ { i } M v _ { j } } { \Lambda _ { j j } } v _ { j } - \frac { \tt t ^ { \Psi } _ { i } M v _ { j } } { \Lambda _ { j j } } \hat { v } _ { j } \right \| + \sigma \sum _ { j < i } \left \| \frac { ( M v _ { j } ) ^ { \circ 2 } } { \Lambda _ { j j } } - \frac { ( M v _ { j } ) ^ { \circ 2 } } { \Lambda _ { j j } } \right \| _ { 2 } \\$$

$$= 2 \| M \| _ { 2 } \cdot \sum _ { j < i } \left | \left | \frac { ( v _ { j } v _ { j } ^ { \top } - \bar { v } _ { j } v _ { j } ^ { \top } ) M \bar { v } _ { i } } { \Lambda _ { j j } } \right | _ { 2 } + \sigma \cdot \sum _ { j < i } \left | \frac { ( M v _ { j } ) ^ { 2 } - ( M \bar { v } _ { i } ) ^ { 2 } } { \Lambda _ { j j } } \right | _ { 2 }$$

$$& \leq 2 \| M \| _ { 2 } \cdot \sum _ { j < i } \| v _ { j } v _ { j } ^ { \top } - \hat { v } _ { j } \hat { v } _ { j } ^ { \top } \| _ { 2 } \cdot \frac { \| M \hat { v } _ { i } \| _ { 2 } } { | \Lambda _ { j j } | } + \sigma \cdot \sum _ { j < i } \left \| \frac { ( M v _ { j } ) ^ { \sigma _ { 2 } } - ( M \hat { v } _ { i j } ) ^ { \sigma _ { 2 } } } { \Lambda _ { j j } } \right \| _ { 2 }$$

$$& \leq 2 \| M \| _ { 2 } \cdot \sum _ { j < i } \| v _ { j } v _ { j } ^ { \top } - \hat { v } _ { j } \hat { v } _ { j } ^ { \top } \| _ { 2 } \cdot \frac { \Lambda _ { 1 1 } } { \Lambda _ { j j } } + \sigma \cdot \sum _ { j < i } \left \| \frac { ( M v _ { j } ) ^ { \circ 2 } - ( M \hat { v } _ { j } ) ^ { \circ 2 } } { \Lambda _ { j j } } \right \| _ { 2 }$$

$$& = 2 \left \| M \right \| _ { 2 } \cdot \sum _ { j < i } \left \| v _ { j } v _ { j } ^ { \top } - ( v _ { j } + w _ { j } ) ( v _ { j } + w _ { j } ) ^ { \top } \right \| _ { 2 } \cdot \frac { \Lambda _ { 1 1 } } { \Lambda _ { j j } } + \sigma \sum _ { j < i } \left \| \frac { ( M _ { v _ { j } } ) ^ { \circ 2 } - ( M ( v _ { j } + w _ { j } ) ) ^ { \circ 2 } } { \Lambda _ { j j } } \right \|$$

$$= 2 \| M \| _ { 2 } \cdot \sum _ { j < i } \left \| - ( v _ { j } w _ { j } ^ { \top } + w _ { j } v _ { j } ^ { \top } + w _ { j } w _ { j } ^ { \top } ) \right \| _ { 2 } \cdot \frac { \Lambda _ { 1 j } } { \Lambda _ { j j } } + \sigma \cdot \sum _ { j < i } \left \| \frac { - ( 2 ( M _ { v _ { j } } ) \circ ( M _ { w _ { j } } ) + ( M _ { w _ { j } } ) ^ { \circ 2 } ) } { \Lambda _ { j j } } \right \| _ { 2 } \\$$

$$& \leq 2 \| M \| _ { 2 } \cdot \sum _ { j < i } ( \| v _ { j } w _ { j } ^ { \top } \| _ { 2 } + \| w _ { j } v _ { j } ^ { \top } \| _ { 2 } + \| w _ { j } w _ { j } ^ { \top } \| _ { 2 } ) \cdot \frac { \Lambda _ { 1 i } } { \Lambda _ { j j } } + \sigma \cdot \sum _ { j < i } ( 2 \| M v _ { j } \| _ { 2 } \cdot \| M w _ { j } \| _ { 2 } + \| M w _ { j } \| _ { 2 } ^ { 2 } ) \frac { 1 } { \Lambda _ { j j } } .$$

Theorem 24 Assume the angular error ϕ j ≤ ϵ between the true eigenvector of a parent v j and its estimate ˆ v j to satisfy ϵ ≪ 1 such that the length of the cord that connects both vectors is l = | ˆ v j -v j | = 2 sin ( ϵ 2 ) for the Euclidean error of the parent to be O ( ϵ ) . The Euclidean error of the child's parameterized gradient is O ( ϵ √ ℓq ) , with ℓ being the number of layers and q the number of qubits for the parameter space, and is expressed as:

$$\| b \| _ { 2 } & = \| \nabla _ { \hat { \theta } _ { i } } ^ { R } u ( v ( \hat { \theta } _ { j } ) | v ( \hat { \theta } _ { j < i } ) ) - \nabla _ { \hat { \theta } _ { i } } ^ { R } u ( v ( \hat { \theta } _ { i } ) | v ( \theta _ { j < i } ) ) \| _ { 2 } \\ & \leq 2 \sqrt { \ell } q \cdot \| M \| _ { 2 } \cdot \sum _ { j < i } \left ( \| v ( \theta _ { j } ) w _ { j } ^ { \top } \| _ { 2 } + \| w _ { j } v ( \theta _ { j } ) ^ { \top } \| _ { 2 } + \| w _ { j } w _ { j } ^ { \top } \| _ { 2 } \right ) \cdot \frac { \Lambda _ { 1 1 } } { \Lambda _ { j j } } .$$

Proof. Let b be the difference between the Riemannian gradient with approximate parents and that with exact parents. We can specify v ( ˆ θ j ) = v ( θ j ) + w j where w j is the vector that represents the mis-specification error of v ( ˆ θ j ) , and proceed by bounding b in the following:

$$b = \nabla ^ { R } _ { \hat { \theta } _ { i } } u ( v ( \hat { \theta } _ { i } ) | v ( \hat { \theta } _ { j < i } ) ) - \nabla ^ { R } _ { \hat { \theta } _ { i } } u ( v ( \hat { \theta } _ { i } ) | v ( \hat { \theta } _ { j < i } ) )$$

$$& = ( I - v ( \hat { \theta } _ { i } ) v ( \hat { \theta } _ { i } ) ^ { \top } ) \left [ \nabla _ { \hat { \theta } _ { i } } u ( \hat { \theta } _ { i } ) | v ( \hat { \theta } _ { j < i } ) ) - \nabla _ { \hat { \theta } _ { i } } u ( v ( \hat { \theta } _ { i } ) | v ( \hat { \theta } _ { j < i } ) ) \right ]$$

$$& = ( I - v ( \hat { \theta } _ { i } ) v ( \hat { \theta } _ { i } ^ { \top } ) J _ { v } ( \hat { \theta } _ { i } ) \left [ \nabla _ { \hat { \theta } _ { i } } u ( v ( \hat { \theta } _ { i } ) | v ( \hat { \theta } _ { j < i } ) ) - \nabla _ { \hat { \theta } _ { i } } u ( v ( \hat { \theta } _ { i } ) | v ( \hat { \theta } _ { j < i } ) ) \right ]$$

$$= ( I - v ( \hat { \theta } _ { i } ) v ( \hat { \theta } _ { i } ) ^ { \top } ) J _ { v ( \hat { \theta } _ { i } ) } \left [ 2 M \left ( v ( \hat { \theta } _ { i } ) - \sum _ { j < i } \frac { v ( \hat { \theta } _ { i } ) ^ { \top } M v ( \hat { \theta } _ { j } ) } { v ( \hat { \theta } _ { j } ) ^ { \top } M v ( \hat { \theta } _ { j } ) } v ( \hat { \theta } _ { j } ) \right ) - 2 M \left ( v ( \hat { \theta } _ { i } ) - \sum _ { j < i } \frac { v ( \hat { \theta } _ { i } ) ^ { \top } M v ( \hat { \theta } _ { j } ) } { v ( \hat { \theta } _ { j } ) ^ { \top } M v ( \hat { \theta } _ { j } ) } v ( \hat { \theta } _ { j } ) \right ) \right ] \\ = ( I - v ( \hat { \theta } _ { i } ) v ( \hat { \theta } _ { i } ) ^ { \top } ) J _ { v ( \hat { \theta } _ { i } ) } \left [ 2 M \left ( v ( \hat { \theta } _ { i } ) - \sum _ { j < i } \frac { v ( \hat { \theta } _ { i } ) ^ { \top } M v ( \hat { \theta } _ { j } ) } { v ( \hat { \theta } _ { j } ) ^ { \top } M v ( \hat { \theta } _ { j } ) } v ( \hat { \theta } _ { j } ) \right ) - 2 M \left ( v ( \hat { \theta } _ { i } ) - \sum _ { j < i } \frac { v ( \hat { \theta } _ { i } ) ^ { \top } M v ( \hat { \theta } _ { j } ) } { v ( \hat { \theta } _ { j } ) ^ { \top } M v ( \hat { \theta } _ { j } ) } v ( \hat { \theta } _ { j } ) \right ) \right ] \\$$

$$= \left ( I - v ( \hat { \theta } _ { i } ) v ( \hat { \theta } _ { i } ) ^ { \top } \right ) J _ { v } ( \hat { \theta } _ { i } ) \left [ 2 M \left ( \sum _ { j < i } \frac { v ( \hat { \theta } _ { j } ) ^ { \top } M v ( \theta _ { j } ) } { v ( \theta _ { j } ) ^ { \top } M v ( \theta _ { j } ) } v ( \theta _ { j } ) - \sum _ { j < i } \frac { v ( \hat { \theta } _ { j } ) ^ { \top } M v ( \hat { \theta } _ { j } ) } { v ( \hat { \theta } _ { j } ) ^ { \top } M v ( \hat { \theta } _ { j } ) } v ( \hat { \theta } _ { j } ) \right ) \right ] ,$$

where the norm of the difference is

$$\| b \| = \left ( \left ( I - v ( \hat { \theta } _ { i } ) v ( \hat { \theta } _ { i } ) ^ { \top } \right ) J _ { v } ( \hat { \theta } _ { i } ) \left [ 2 M \left ( \sum _ { j < i } \frac { v ( \hat { \theta } _ { i } ) ^ { \top } M v ( \theta _ { j } ) } { v ( \theta _ { j } ) ^ { \top } M v ( \theta _ { j } ) } v ( \theta _ { j } ) - \sum _ { j < i } \frac { v ( \hat { \theta } _ { i } ) ^ { \top } M v ( \hat { \theta } _ { j } ) } { v ( \hat { \theta } _ { j } ) ^ { \top } M v ( \hat { \theta } _ { j } ) } v ( \hat { \theta } _ { j } ) \right ) \right ] \right ] _ { i } \quad ( 9 4 )$$

$$& \quad \left \| \begin{array} { c } \\ \\ \end{array} \right \| ( I - v ( \hat { \theta } _ { i } ) v ( \hat { \theta } _ { i } ) ^ { \top } ) \right \| \left \| J _ { v } ( \hat { \theta } _ { i } ) \right \| \left \| 2 M \left ( \sum _ { j < i } \frac { v ( \hat { \theta } _ { i } ) ^ { \top } M v ( \theta _ { j } ) } { v ( \theta _ { j } ) ^ { \top } M v ( \theta _ { j } ) } v ( \theta _ { j } ) - \sum _ { j < i } \frac { v ( \hat { \theta } _ { i } ) ^ { \top } M v ( \hat { \theta } _ { j } ) } { v ( \hat { \theta } _ { j } ) ^ { \top } M v ( \hat { \theta } _ { j } ) } v ( \hat { \theta } _ { j } ) \right ) \right \| \, \left ( 9 5 \right ) \\ & \quad \right \| \begin{array} { c } \\ \end{array} \right \| ,$$

$$& \leq \left \| J _ { v } ( \hat { \theta } _ { i } ) \right \| _ { 2 M } \left ( \sum _ { j < i } \frac { v ( \hat { \theta } _ { i } ) ^ { \top } M v ( \theta _ { j } ) } { v ( \theta _ { j } ) ^ { \top } M v ( \theta _ { j } ) } v ( \theta _ { j } ) - \sum _ { j < i } \frac { v ( \hat { \theta } _ { i } ) ^ { \top } M v ( \hat { \theta } _ { j } ) } { v ( \theta _ { j } ) ^ { \top } M v ( \theta _ { j } ) } v ( \hat { \theta } _ { j } ) \right ) \right \| \\$$

$$= \left \| J _ { v } ( \hat { \theta } _ { i } ) \right \| _ { \substack { 2 M \left ( \sum _ { j < i } \frac { v ( \hat { \theta } _ { i } ) ^ { \top } M v ( \theta _ { j } ) } { \Lambda _ { j j } } v ( \theta _ { j } ) - \sum _ { j < i } \frac { v ( \hat { \theta } _ { i } ) ^ { \top } M v ( \hat { \theta } _ { j } ) } { v ( \hat { \theta } _ { j } ) ^ { \top } M v ( \hat { \theta } _ { j } ) } v ( \hat { \theta } _ { j } ) \right ) \right \| _ { \substack { 2 M v ( \theta _ { j } ) ^ { 2 } \\ 2 M v ( \theta _ { j } ) ^ { 2 } } }$$

$$& \leq \left \| J _ { v } ( \hat { \theta } _ { i } ) \right \| _ { \left \| 2 M \left ( \sum _ { j < i } \frac { v ( \hat { \theta } _ { i } ) ^ { \top } M v ( \theta _ { j } ) } { \Lambda _ { j j } } v ( \theta _ { j } ) - \sum _ { j < i } \frac { v ( \hat { \theta } _ { i } ) ^ { \top } M v ( \hat { \theta } _ { j } ) } { \Lambda _ { j j } } v ( \hat { \theta } _ { j } ) \right ) \right \| \\$$

$$& \leq 2 \left \| M \right \| \overset { ^ { \prime } } { J } _ { v } ( \hat { \theta } _ { j } ) \left \| \sum _ { j < i } \left \| \frac { v ( \hat { \theta } _ { i } ) ^ { \top } M v ( \theta _ { j } ) } { \Lambda _ { j j } } v ( \theta _ { j } ) - \frac { v ( \hat { \theta } _ { i } ) ^ { \top } M v ( \hat { \theta } _ { j } ) } { \Lambda _ { j j } } v ( \hat { \theta } _ { j } ) \right \|$$

$$= 2 \left \| M \right \| \left \| J _ { v } ( \hat { \theta } _ { j } ) \right \| \sum _ { j < i } \left \| \frac { ( v ( \theta _ { j } ) v ( \theta _ { j } ) ^ { \top } - v ( \hat { \theta } _ { j } ) v ( \hat { \theta } _ { j } ) ^ { \top } ) M v ( \hat { \theta } _ { i } ) } { \Lambda _ { j } } \right \|$$

$$& \leq 2 \, \| M \| \left \| J _ { v } ( \hat { \theta } _ { j } ) \right \| \sum _ { j < i } \left \| v ( \theta _ { j } ) v ( \theta _ { j } ) ^ { \top } - v ( \hat { \theta } _ { j } ) v ( \hat { \theta } _ { j } ) ^ { \top } \right \| \frac { \| M v ( \hat { \theta } _ { i } ) \| } { \Lambda _ { j j } } \|$$

$$& \leq 2 \, \| M \| \left \| J _ { v } ( \hat { \theta } _ { j } ) \right \| \sum _ { j < i } \left \| v ( \theta _ { j } ) v ( \theta _ { j } ) ^ { \top } - v ( \hat { \theta } _ { j } ) v ( \hat { \theta } _ { j } ) ^ { \top } \right \| \frac { \Lambda _ { 1 1 } } { \Lambda _ { j j } }$$

$$= 2 \left \| M \right \| \left [ J _ { v } ( \hat { \theta } _ { j } ) \right ] \sum _ { j < i } \left \| v ( \theta _ { j } ) v ( \theta _ { j } ) ^ { \top } - ( v ( \theta _ { j } ) + w _ { j } ) ( v ( \theta _ { j } ) + w _ { j } ) ^ { \top } \right \| \frac { \Lambda _ { 1 1 } } { \Lambda _ { j j } }$$

$$= 2 \left \| M \right \| \left [ J _ { v } ( \hat { \theta } _ { j } ) \right ] \sum _ { j < i } \left \| - ( v ( \theta _ { j } ) w _ { j } ^ { \top } + w _ { j } v ( \theta _ { j } ) ^ { \top } + w _ { j } w _ { j } ^ { \top } ) \right \| \frac { \Lambda _ { 1 1 } } { \Lambda _ { j j } }$$

$$& \leq 2 \left \| M \right \| \left [ J _ { v } ( \hat { \theta } _ { j } ) \right ] \sum _ { j < i } ( \| v ( \theta _ { j } ) w _ { j } ^ { \top } \| + \| w _ { j } v ( \theta _ { j } ) ^ { \top } \| + \| w _ { j } w _ { j } ^ { \top } \| ) \frac { \Lambda _ { 1 1 } } { \Lambda _ { j j } } \\$$

$$= 2 \sqrt { \ell q } \| M \| \sum _ { j < i } ( \| v ( \theta _ { j } ) w _ { j } ^ { \top } \| + \| w _ { j } v ( \theta _ { j } ) ^ { \top } \| + \| w _ { j } w _ { j } ^ { \top } \| ) \frac { \Lambda _ { 1 1 } } { \Lambda _ { j j } } .$$