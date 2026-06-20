## Article

## Aperturbative approach to the solution of the Thirring quantum cellular automaton

<!-- image -->

<!-- image -->

Citation: Bisio, A.; Perinotti, P.; Pizzamiglio, A.; Rota, S. A perturbative approach to the solution of the Thirring quantum cellular automaton. Preprints 2024 , 1 , 0. https://doi.org/

<!-- image -->

Copyright: © 2024 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ 4.0/).

<!-- image -->

Alessandro Bisio 1 , Paolo Perinotti 2 , Andrea Pizzamiglio 3 and Saverio Rota

4

- 1 Dipartimento di Fisica, Università di Pavia and INFN sezione di Pavia; alessandro.bisio@unipv.it
- 2 Dipartimento di Fisica, Università di Pavia and INFN sezione di Pavia; paolo.perinotti@unipv.it
- 3 Dipartimento di Fisica, Università di Pavia and INFN sezione di Pavia; andrea.pizzamiglio01@universitadipavia.it
- 4 Dipartimento di Fisica, Università di Pavia; saverio.rota01@universitadipavia.it

Abstract: The Thirring Quantum Cellular Automaton (QCA) describes the discrete time dynamics of local fermionic modes that evolve according to one step of the Dirac cellular automaton followed by the most general on-site number-preserving interaction, and serves as the QCA counterpart of the Thirring model in quantum field theory. In this work, we develop perturbative techniques for the QCA path-sum approach, expanding both the number of interaction vertices and the mass parameter of the Thirring QCA. By classifying paths within the regimes of very light and very heavy particles, we computed the transition matrices in the two- and three-particle sectors to the first few orders. Our investigation into the properties of the Thirring QCA, addressing the combinatorial complexity of the problem, yielded some useful results applicable to the many-particle sector of any on-site number-preserving interactions in one spatial dimension.

Keywords: Quantum cellular automata; perturbative approach; approximation thechniques

## 1. Introduction

Understanding the dynamics of interacting many-body quantum systems remains one of the paramount unsolved challenges in physics. The intricate behaviours and interdependencies within these systems render both analytical descriptions and numerical simulations exceedingly arduous. Nonetheless, the past decades of research have heralded an uplifting new horizon. The confluence of cutting-edge quantum technologies and the maturation of quantum information theory offers a wealth of promising investigative tools, both practical and theoretical. The rapidly increasing precision in control over quantum apparatus suggests that we will soon be able to test both novel and long-standing hypotheses, ranging from simulations in particle physics and condensed matter to exploring the very foundations of contemporary physics.

Specifically, in addressing the inefficiency of classical computers in simulating quantum systems, Quantum Cellular Automata (QCAs) delineate practical quantum algorithms for simulating the dynamics of an interacting quantum many-body system [1-5]. Quantum cellular automata are homogeneous networks of local quantum systems that abide by a translationally invariant discrete-time evolution, each interacting with a finite number of neighbours. The most interesting QCAs for quantum simulations are those that can be implemented as Finite-Depth Quantum Circuits (FDQC). Furthermore, QCAs offer an inherent architecture for the implementation of quantum simulation hardware and for distributed quantum computation [4,6], and they are universal for quantum computation as they were proved equivalent both to the quantum Turing machine and the circuit paradigm of quantum computation [6].

In recent years, QCAs, and Quantum Walks (QWs)-which can be regarded as the one-particle sector, or first quantisation counterpart of QCAs-have been investigated as instruments for simulating relativistic quantum fields and as discrete methods for studying the foundations of Quantum Field Theory (QFT) [7-13]. There are many advantages of such an approach to the foundations. From an information theoretical standpoint, quantum systems might be conceived as elementary information carriers, rather than elementary constituents of matter, circumventing the molasses of interpretational issues of quantum mechanics. With this premises, relationships between elementary quantum systems can be thought of as logical connections within an algorithm, as opposed to the usual space-time relations. Along this line, embracing the principle initially proposed by Feynman [1] and later refined by Deutsch [2], that every experiment involving a finite space-time region should be perfectly simulated by a finite quantum algorithm, we can devise physical laws as algorithms that govern the update of memory registers constituting a physical system. Within this scope, the QCA framework naturally emerges by imposing-once reframed in this context-the characteristic properties of physical laws onto such algorithms, as locality and homogeneity [14].

This approach to fundamental physics has relevant practical advantages. Over the last decades, several quantum simulation schemes have been devised [15], yet these are predominantly Hamiltonian-based. They rely on a discrete-space continuous-time version of the QFT. Analog quantum systems mimicking the Hamiltonian are sought, or alternatively, staggered trotterisation (Suzuki-Trotter decomposition) is performed to obtain unitary transformations that may be implemented as a quantum circuit on a digital quantum computer. Trotterised gates are close to the identity though and contrast with QCAs gates, which conversely, not being subject to trotterisation conditions, can be highly non-trivial, converging faster to physical dynamics [16-18] under suitable conditions. Furthermore, the possibility of framing algorithms not originating from conventional QFTs suggests a broader spectrum of possibilities for simulating them via quantum computers beyond lattice QFT.

In the second place, given that the traditional action-based approach is only surreptitiously continuous, namely up to renormalisation [19], a crucial procedure for both its mathematical amenability and physical significance, it is conceptually clearer to start from new premises, based on a natively discrete theory. Indeed, QCAs exhibit manifest unitarity and possess a local formulation.

Gauge invariance can be handled as outlined in [20-22]. Moreover, an ab initio quantum description, namely not obtained by carrying out a quantization procedure on a classical theory, sidesteps the ambiguities that arise when striving to develop a quantum theory based on a classical action, and due to the emergent nature of the geometry of space-time, it represents an enticing arena for approaching a quantum theory of gravity [23-26].

There are of course also drawbacks in facing a new formulation of QFT. In the first place, being intrinsically discrete, this kind of models were for a long time dismissed as incompatible with the relativistic framework that is the crucial feature of quantum fields [27]. However, in recent years their compatibility with Lorentz-covariance has been explicitly demonstrated in compliance with different prescriptions [24,28,29], e.g. by identifying a change of inertial frame with a symmetry of the dynamics. The bounded speed of light in circuit-based quantum simulation is naturally enforced by the wiring between local quantum gates.

Secondarily, despite QCAs have achieved promising success in recovering free quantum field theories from principles of information processing [10], to date, a thorough study of interaction processes within the QCA framework is lacking, representing a largely unexplored avenue. Like in QFT, this point is the source of main troubles, and the newborn theory of QCAs cannot yet count on the wealth of techniques and approaches of the standard formulation. This requires an extensive review of theoretical tools with the aim of either adapting them to the discrete framework or to replace them by new, more suitable techniques.

In the present study, we tackle the issue by endeavouring to expand a specific instance of the QCA approach that has proved successful in solving the non-interacting dynamics: the path sum [30]. As a case study, we consider the (1+1)-dimensional Thirring Quantum Cellular Automaton. The interaction described by the Thirring QCA is the most general one, being both number-preserving-meaning the number of particles remains constant before and after the interaction-and on-site, requiring particles to occupy the same lattice site simultaneously to interact. Moreover, our choice is driven by three primary reasons. In the first place, the interaction-free model has been exactly treated via a path-sum approach [30], providing a solid starting toolbox, and the interacting one has been analytically solved in the two-particle sector [31], allowing us to validate the results and check the accuracy of approximations. Secondarily, in the (1+1)-dimensional case, we can easily visualise the discrete evolution of the automaton on a two-dimensional space-time lattice. The evolution of a particle with specified initial and final conditions can be effectively represented by a collection of interfering paths connecting these points. Within the path-sum paradigm, transition amplitudes are then obtained by summing over such paths. Finally, the Thirring model in QFT belongs to the restricted category of integrable models. Though it is not completely obvious that the Thirring QCA obtains the Thirring model in some limit, this allows us to borrow techniques from established results, and to have a source for future validation and developments.

Despite the simplicity of local rules governing QCAs, the emerging behaviour exhibits increasing complexity as the evolution progresses. While this is one of the general reasons why QCAs represent a valuable tool in studying complex systems, it is also the reason why their actual classification proves to be remarkably challenging [32-35]. Within the path sum approach, and given the on-site nature of Thirring interaction, the origin of the complexity here is embodied in a comprehensive classification of all possible paths based on the number of intersections that yield an interaction. Such classification requires to take into account a both the Pauli exclusion principle and the fact that the free dynamics of the QCAunivocally determines the internal state of the systems at every lattice site.

At the outset, one is led to follow a perturbative approach in the number of interactions, where fixed the number of time steps, the initial and final conditions, and we expanded transition amplitudes in a sum of terms, each corresponding to a fixed the number of interactions. Unfortunately, the algorithm that identifies all paths with a given number of interactions (i.e. crossings) is computationally expensive. Consequently, we focused on a different perturbative approach, consisting in a power expansion in the mass parameter of the automaton. The regularity of the paths within the extremal regimes of ultra-light and ultra-heavy fermions, allowed for their full enumeration. We then computed the transition matrices in these regimes up to third order and up to the three particles sector.

The paper is structured as follows. Section 2 gives an outline of the one-dimensional Dirac QCA [36]. We then provide an overview of the path sum approach to its solution [30]. In section 3 a synopsis of the Thirring QCA [31] is presented. Section 4 shows an overarching characterization of the particle paths, grounded in the general features of Thirring QCA. Sections 5 and 6 cover the path sum approach in the two-particle sector, with a perturbative technique in the number of interactions and in the particle mass respectively. Finally, in section 7 we discuss the multi-particle sector and in particular the three-particle case.

## 2. One-dimensional Dirac QCA

## 2.1. Derivation

The following discussion may appear as a mere exercise, yet it unveils the potential to reformulate the description of a relativistic quantum theory without initially resorting to the conventional categories of physics, such as spacetime or differential equations thereof. This proves that is feasible to develop an emergent physical semantics on top of the concept of information and its processing, without introducing theoretical physical concepts ab initio. The operational physical notions will be connected to the mathematical symbols through comparison with observations, in a similar way as thermodynamic quantities are derived in statistical mechanics.

Indeed, the Dirac equation can be derived solely from fundamental principles of information processing, without appealing a priori to a spacetime background or special relativity. It has been shown that the Dirac equation in any spatial dimension can be recovered from the large-scale dynamics of a QCA of fermionic systems satisfying linearity, unitarity, locality, homogeneity, and discrete isotropy. Here we briefly sketch the construction (see [14] for a full derivation). The systems are local fermionic modes labelled by the elements g of a countable index set G . Their operator algebra is generated by evaluations ψ ( g ) = ( ψ 1 ( g ) , . . . , ψ s ( g )) of an s -dimensional complex vector field ψ over G , obeying the canonical anti-commutation relations

$$& \{ \psi _ { a } ( f ) , \psi _ { b } ( g ) \} = \left \{ \psi _ { a } ^ { \dagger } ( f ) , \psi _ { b } ^ { \dagger } ( g ) \right \} = 0 , \\ & \left \{ \psi _ { a } ^ { \dagger } ( f ) , \psi _ { b } ( g ) \right \} = \delta _ { f g } \delta _ { a b } \quad \forall f , g \in G , \, a , b , \in \{ 1 , 2 , \dots , s \} .$$

By linearity, we mean the interaction among systems is described by linear transition functions Agf , allowing us to write the evolution of system ψ ( g ) as

$$\psi ( g , t + 1 ) = \alpha [ \psi ( g , t ) ] = \sum _ { f \in S _ { g } } A _ { g f } \, \psi ( f , t ) \, ,$$

̸

with Sg ⊂ G the set of systems interacting with ψ ( g ) . Locality is phrased by imposing Sg being finite for every g . Such a locality condition introduces a notion of causal cone in the emergent spacetime lattice. The homogeneity requirement amounts to ask that the cardinality of Sg , as well as the set of functions { Agf } f ∈ Sg , are independent of g ; whence we can identify Sg = S and the functions Agf = Ah for some h ∈ S . Moreover, we impose Agf = 0 if and only if Afg = 0. We are thus assuming that the QCA evolution does not discriminate systems. It follows that the structure of the connections between systems can be regarded as the application of generators (and their inverses) h ∈ S of a discrete group-that we identify with G -which allows one to move from an element g ∈ G to another element f = hg ∈ G . We can then define a spatial lattice as one possible Cayley graph of this group [37]. The graph describes the interacting set of systems, by taking them as the nodes of the graph, with the links corresponding to their interactions. The isotropy condition stipulates that no preferential direction exists on the lattice. Mathematically, this necessitates the presence of a permutation group acting on S which can be faithfully represented on the internal degrees of freedom. To confine our analysis to the dynamics on an emergent flat Minkowski spacetime, we assume the group G to be virtually abelian, meaning G contains an abelian subgroup of finite index. These are the groups whose Cayley graph can be quasi-isometrically embedded in Euclidean space [38]. Finally, the unitarity assumption-namely reversibility of the algorithm-requires the local rule of a QCAto be a unitary representation US of ∑ h ∈ S Ah . The quantum walk W associated with the QCA α , acting on the Hilbert space C s ⊗ l 2 ( G ) , is obtained by considering the evolution of single-particle states

$$\varphi _ { a } ( g ) = \psi _ { a } ^ { \dagger } ( g ) | \Omega \rangle ,$$

where | Ω ⟩ denotes the vacuum state vector. The quantum walk is given by

$$\varphi ( g , t + 1 ) = W \varphi ( g , t + 1 ) = \sum _ { f \in S _ { g } } A _ { g f } ^ { * } \varphi ( f , t )$$

and thus it contains all the information that is needed in order to reconstruct α [14].

All the QCAs with s = 2, G = Z and S = { 1 } of fermionic systems-whose internal degrees of freedom will be denoted as R , L -whose dynamics is linear in the field and fulfils

̸

the conditions above, are unitarily equivalent to the following QW on H = C 2 ⊗ l 2 ( Z ) , which is called the Dirac QCA (or Quantum Walk) in one dimension:

$$W = \begin{pmatrix} n S _ { R } & i m I \\ i m I & n S _ { L } \end{pmatrix} , \quad n , m \in \mathbb { R } ^ { + } , \, n ^ { 2 } + m ^ { 2 } = 1 , \\ \Psi ( t + 1 ) = W \Psi ( t ) , \quad \Psi ( t ) = ( \dots , \psi ( x - 1 , t ) , \psi ( x , t ) , \psi ( x + 1 , t ) , \dots ) ^ { T } , \quad ( 2 ) \\ \psi ( x , t ) = \begin{pmatrix} \psi _ { R } ( x , t ) \\ \psi _ { L } ( x , t ) \end{pmatrix} ,$$

where I , SR = ∑ x ∈ Z | x + 1 ⟩ ⟨ x | and SL = S † R are the identity, the right shift and the left shift operators on l 2 ( Z ) , respectively. The field component at time t + 1 and at site x depends only on the field components at sites x ± 1 at time t (first-neighboring scheme). Moreover, since W commutes with translations along the lattice, the automaton can be diagonalized in the wave-vector space. In wave-vector representation the Dirac QCA becomes

$$W = \int _ { B } d k \, \widetilde { W } ( k ) \otimes | k \rangle \langle k | \, , \quad \widetilde { W } ( k ) = \left ( \begin{matrix} n e ^ { - i k } & i m \\ i m & n e ^ { i k } \end{matrix} \right ) ,$$

with | k ⟩ ⟨ k | defined on L 2 ( B ) , where B : = [ -π , π ] denotes the Brillouin zone. Upon identifying the parameter m with the mass and k with the momentum of a particle, in the low-mass and low-momentum regime, it can be shown that the evolution described by the automaton cannot be discerned from the one prescribed by the Dirac equation of quantum field theory [36]. Hence the name Dirac QCA.

## 2.2. Path-sum solution

The Dirac automaton in space representation can be conveniently expressed as [30]

$$W = W _ { R } \otimes S _ { R } + W _ { L } \otimes S _ { L } + W _ { F } \otimes I ,$$

along with the following binary encoding

where

$$W _ { R } \coloneqq n W _ { 0 0 } \ , \quad W _ { L } \coloneqq n W _ { 1 1 } \ , \quad W _ { F } \coloneqq i m ( W _ { 0 1 } + W _ { 1 0 } ) \, , \\ \\ W _ { 0 0 } = \left ( \begin{smallmatrix} 1 & 0 \\ 0 & 0 \end{smallmatrix} \right ) , \quad W _ { 1 1 } = \left ( \begin{smallmatrix} 0 & 0 \\ 0 & 1 \end{smallmatrix} \right ) , \\ W _ { 0 1 } = \left ( \begin{smallmatrix} 0 & 1 \\ 0 & 0 \end{smallmatrix} \right ) , \quad W _ { 1 0 } = \left ( \begin{smallmatrix} 0 & 0 \\ 1 & 0 \end{smallmatrix} \right ) . \\$$

One can check that these binary matrices form a closed algebra under multiplication and satisfy a simple composition rule

$$W _ { a b } W _ { c d } = \frac { 1 + ( - 1 ) ^ { b \oplus c } } { 2 } W _ { a d } = \delta _ { b c } W _ { a d } \, ,$$

where a ⊕ b : = ( a + b ) mod2 . Each dynamical step of the automaton consists of a shift Sh acting on coordinates space according to the action of the corresponding transition matrix Wh on the internal degrees of freedom, with h ∈ { R , L , F } and SF ≡ I . Aright shift ( R ) increases the site coordinate of right modes ψ R by one, a left shift ( L ) decreases the site coordinate of left modes ψ L by the same amount, and a free shift ( F ) leaves the site coordinate unchanged upon flipping right to left mode and vice-versa. In the one-particle sector, the QCA describes a Quantum Walk. The evolution of the field over T steps is given by W T and can be thought of as a path connecting sites on the space-time lattice Z × N . We can then associate the generic path connecting x to y in T discrete time steps with a string s = s 1 s 2 . . . sT ∈ { R , L , F } T of transitions, which gives the overall transition matrix W ( s )

$$\mathcal { W } ( s ) \colon = W _ { s _ { T } } W _ { s _ { T - 1 } } \cdots W _ { s _ { 1 } } \, .$$

The path sum approach consists of expressing the state of the system at a given time as the outcome of all the possible evolutions allowed by the dynamics, each identifying a path on the space-time lattice. In this scenario, this translates into expressing the state ψ ( x , t ) as the result of the action of W ( s ) on the generic initial state ψ ( y , 0 ) , summed over all possible paths s and all points y in the past causal cone of site ( x , t ) :

$$\psi ( x , t ) = \sum _ { y } \sum _ { s } \mathcal { W } ( s ) \, \psi ( y , 0 ) \, .$$

Upon denoting with s f the generic path containing f occurrences of the F -transition, eq. (6) becomes

$$\psi ( x , t ) = \sum _ { y } \sum _ { f = 0 } ^ { t - | x - y | } \sum _ { s ^ { f } } \mathcal { W } \left ( s ^ { f } \right ) \psi ( y , 0 )$$

In a path s f , the F transitions identify f + 1 slots

$$\tau _ { 1 } F \tau _ { 2 } F \cdots F \tau _ { f + 1 }$$

where τ i denotes a (possibly empty) string of R or L . The composition rule in eq. (5) forbids the string s codifying a generic path from containing substrings of the form

$$s _ { i } s _ { i - 1 } & = R L & s _ { i } s _ { i - 1 } & = L R \\ s _ { i } s _ { i - 1 } s _ { i - 2 } & = R F R & s _ { i } s _ { i - 1 } s _ { i - 2 } & = L F L$$

as they give null transition amplitude. It follows that each sub-string τ i only consists of equal letters, namely either τ i = RR · · · R or τ i = LL · · · L . Moreover, two consecutive strings τ i and τ i + 1 must contain different transitions. Therefore, all substrings τ 2 i occupying the even slots must be of one kind, and all substrings τ 2 i + 1 occupying the odd ones must be of the other kind. Exploiting the algebra (5) and relying on combinatorial arguments, we can ultimately express the state of the field at ( x , t ) as:

$$\psi ( x , t ) = \sum _ { y } \sum _ { a , b \in \{ 0 , 1 \} } \sum _ { f = 0 } ^ { t - | x - y | } \left [ \alpha ( f ) \, c _ { a b } ( f ) \, W _ { a b } \right ] \psi ( y , 0 ) \, ,$$

where the factor α ( f ) is given by

where

$$\alpha ( f ) \colon = ( i m ) ^ { f } \, n ^ { t - f }$$

with f the number of F -type transitions within the path connecting the field at ( y , 0 ) to the field at ( x , t ) . The coefficients c ab ( f ) account for the number of strings s f corresponding to paths giving Wab as the total transition matrix and can be computed by the following product of binomial coefficients

$$c _ { a b } ( f ) = \begin{pmatrix} \mu _ { + } - \nu \\ f _ { \frac { - 1 } { 2 } } - \nu \end{pmatrix} \begin{pmatrix} \mu _ { - } + \nu \\ f _ { \frac { - 1 } { 2 } } + \nu \end{pmatrix} ,$$

$$\nu = \frac { a b - \bar { a } \bar { b } } { 2 } \quad \mu _ { \pm } = \frac { t \pm ( x - y ) - 1 } { 2 } \, ,$$

and satisfy caa ( 2 k + 1 ) = ca ¯ a ( 2 k ) = 0, with ¯ a = a ⊕ 1. The analytical solution of the Dirac walk (8) can also be expressed in terms of Jacobi polynomials P ( α , β ) k by explicitly computing the sum over f (see [30]).

## 3. Thirring QCA

To accomplish interacting quantum walkers, namely true QCAs, we must involve unitary transformations that are non-linear in the degrees of freedom [22]. Non-linearity naturally stems from the discreteness of the evolution. While a continuous framework might inherently imply a continuous evolution of the Hilbert space basis representing a local system, discrete steps in QCA framework lack an inherent method to compare the local basis at subsequent times. Consequently, we allow a free misalignment, introducing a local unitary evolution at each timestep - alongside the linear one - that is non-linear in the fermionic modes, while preserving topological symmetries.

Weintroduce the most general on-site number-preserving interaction in the one-dimensional Dirac QCA, particularly focusing on the two-particle sector. This type of interaction characterises a few notable integrable quantum systems [39-42] such as Hubbard's [43] and Thirring's [44] models. Hence, the present model is denoted as Thirring Quantum Cellular Automaton [31]. When discussing non-interacting particles, the one-particle sector completely specifies the dynamics. Indeed, the evolution of N free Dirac fermions is described by the operator WN : = W ⊗ N acting on the Hilbert space H ⊗ N , obtained by the tensorisation of the single-particle evolution (2). The Thirring QCA is defined as the most general on-site coupling J ( χ ) of one-dimensional many Dirac fermions, that preserves the number of particles. It is demonstrated [45] that such interaction takes the form

$$J ( \chi ) \coloneqq e ^ { i \chi n _ { R } ( x ) n _ { L } ( x ) }$$

where na ( x ) = ψ † a ( x ) ψ a ( x ) is the number operator at site x with internal state a ∈ { R , L } , and χ ∈ [ -π , π ] is the automaton coupling constant. The single-step evolution consisting of both the free evolution and the on-site interaction for N particles, from now on referred as Thirring QCA , is therefore defined by

$$U _ { N } \coloneqq W _ { N } \, J ( \chi ) \, .$$

Given that this QCA shares the same interaction term as the Hubbard and Thirring models, which are known to be integrable, it is natural to question its own integrability. All known quantum integrable systems are solved via the Bethe ansatz . This method consists of solving the two-particle dynamics, formulating an ansatz for the solution of the N-particle case based on the two-particle solution, and verifying that the ansatz provides all the solutions. However, in the case of the Thirring QCA, the discrete nature of time evolution introduces nontrivial differences in the dynamics and results in a distinct phenomenology. Thus, the conventional N -particle ansatz cannot be straightforwardly applied to the Thirring QCA, leaving the question of its integrability unsolved.

We briefly recall here the solution in the two-particle sector (see Ref.[31]). In the two-particle case, N = 2, it is convenient to work in the centre-of-mass basis | a 1 , a 2 ⟩| y ⟩| w ⟩ ∈ H ⊗ 2 , where ai ∈ { R , L } , while y = x 1 -x 2 and w = x 1 + x 2 denote the relative position and the centre-of-mass coordinates of the particles, respectively. The interaction operator can thus be represented as

$$J ( \chi ) = e ^ { i \chi \delta _ { y , 0 } ( 1 - \delta _ { a _ { 1 } , a _ { 2 } } ) } \, .$$

Defining k , p ∈ B as the (half) relative momentum and the (half) total momentum of the particles respectively, the free QCA in the momentum representation is written as

$$W _ { 2 } = \int _ { B \times B } d k \, d p \, \widetilde { W } _ { 2 } ( k , p ) \otimes | k \rangle \langle k | \otimes | p \rangle \langle p | \, , \\ \widetilde { W } _ { 2 } ( k , p ) \colon = \widetilde { W } ( p + k ) \otimes \widetilde { W } ( p - k ) \, ,$$

with ˜ W as in (3). Since the interacting dynamics described by U 2 commutes with the translations in the center-of-mass coordinate w , it is convenient to write the automaton in the hybrid basis | a 1 , a 2 ⟩| y ⟩| p ⟩

$$U _ { 2 } & = \int _ { B } d p \, U _ { 2 } ( \chi , p ) \otimes | p \rangle ( \mu , \ U _ { 2 } ( \chi , p ) \coloneqq W _ { 2 } ^ { h } ( p ) J ^ { h } ( \chi ) \\ W _ { 2 } ^ { h } ( p ) & \coloneqq m n \left ( \frac { \frac { n } { m } e ^ { - i 2 p } } { i e ^ { - i p T _ { Y } } } \, \ i e ^ { - i p T _ { Y } } \, \quad e ^ { - i p T _ { Y } } \, \frac { - \frac { m } { n } } { i ^ { 2 } p ^ { 2 } } + \dots + \dots \right ) \\ & \quad \left ( i e ^ { - i p T _ { Y } } \right ) \quad \frac { n } { m } \, \frac { 1 } { n } \, \frac { m } { 2 } T _ { Y } ^ { 2 } \quad \frac { - m } { n } \, \frac { 1 } { n } \, i ^ { 2 } p ^ { 2 } T _ { Y } ^ { 2 } \right ) \quad J ^ { h } ( \chi ) \coloneqq \begin{pmatrix} 0 & e ^ { i \chi _ { \delta , 0 } I } & 0 & 0 \\ 0 & 0 & e ^ { i \chi _ { \delta , 0 } I } & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix} \\ & \quad - \frac { m } { n } \, \frac { i e ^ { i p T _ { Y } } } { i ^ { 2 } p ^ { 2 } } \, \frac { i e ^ { i p T _ { Y } } } { i ^ { 2 } p } \, \frac { 1 } { n } e ^ { i 2 p } \, \right )$$

where the superscript h stands for "hybrid", and Ty , T † y are the right and left shift in the relative coordinate y . Solving the two-particle dynamics amounts to the diagonalisation of the infinite-dimensional operator U 2 ( χ , p ) . Although, generally, it is not possible to obtain the analytical solution for an infinite-dimensional eigenvalue problem, the authors of [31] show that the eigenvalue problem

$$U _ { 2 } ( \chi , p ) | \psi \rangle = e ^ { i \omega } | \psi \rangle$$

can be suitably reduced to a finite set of algebraic equations that admit an analytical solution. This is done by considering the linear difference equation

$$U _ { 2 } ( \chi , p ) & f _ { p , \omega , \chi } = e ^ { i \omega } f _ { p , \omega , \chi } \\ & f _ { p , \omega , \chi } \ \colon \ \mathbb { Z } \to \mathbb { C } ^ { 4 } \ \ , \ \ \omega \in \mathbb { C }$$

for any possible value of χ and p . Since, in the new coordinates, the interacting term acts only at the origin, for y &gt; 0 such an equation results in a linear recurrence relation with constant coefficients, which are then determined by requiring the solutions to be antisymmetric eigenvectors (or generalised eigenvectors) of U 2 ( χ , p ) intended as an operator on the Hilbert space C 4 ⊗ l 2 ( Z ) . The solutions thus obtained present some rather peculiar features, most notably:

- there are bound states for every value of the total momentum, which also exist in the free case;
- there are four classes of scattering solutions, as opposed to the two obtained with the usual quantum field theory approach;
- the Thirring QCA in the continuum limit does not straightforwardly yield the Thirring model.

## 4. Preliminary results

In this section, we present the mathematical tools useful for analyzing and classifying particle paths in the interacting scenario. All detailed proofs can be found in Appendix A. The central result shown here is the fact that, given the initial conditions of the field, the free dynamics of the automaton univocally determines its state at each site of the space-time lattice. Combined with Pauli's exclusion principles, this establishes necessary boundary conditions for particles to interact at any space-time point. It is convenient to denote by bit 0 the right mode of the field and by bit 1 the left mode. The evolution of one particle can thus be described both with a string of transitions, made up of R , L , F , or with a binary string associated with the state of the particle at each time step. The main advantage of employing binary strings lies in their lack of constraints regarding the arrangement of their elements. Unlike translations, where substrings LR and RL are prohibited by the algebra of transition matrices, any sequence of 0s and 1s constitutes a valid path. We begin by defining a mapping between binary strings of internal degrees of freedom and the corresponding strings of translations on the lattice, which serves to elucidate the argument (see Fig.1).

Definition 1. Let M be a map associating a pair of bits, encoding the state of the particle for two subsequent evolution steps, with the corresponding translation on the lattice

$$\mathcal { M } \ \colon \ \{ 0 , 1 \} ^ { 2 } & \to \{ R , L , F \} \\ b _ { 1 } b _ { 2 } & \mapsto \mathcal { M } _ { b _ { 1 } b _ { 2 } }$$

according to the following rules:

$$\mathcal { M } _ { 0 0 } = R \ \ ; \ \ \mathcal { M } _ { 1 1 } = L \ \ ; \ \ \mathcal { M } _ { 0 1 } = \mathcal { M } _ { 1 0 } = F \, .$$

A correspondence between the binary string of subsequent internal degrees of freedom b = b 0 · · · bT and the string of translations s = s 1 · · · sT can be established:

$$\overline { \mathcal { M } } \ \colon \ \{ 0 , 1 \} ^ { T + 1 } & \to \{ R , L , F \} ^ { T } \\ b & \mapsto \overline { \mathcal { M } } ( b ) = s$$

$$s _ { k } = \mathcal { M } _ { b _ { k - 1 } b _ { k } } \quad 1 \leq k \leq T \, .$$

Figure 1. On the left, the correspondence between different ways of representing the evolution of the particle at each step of the automaton is given. On the right, an example of the three representations for a generic walk is shown. The strings, whether representing lattice transitions or internal degrees of freedom, are ordered with time progressing from left to right, while on the lattice, time flows from bottom to top.

<!-- image -->

We introduce a function that takes a single-step transition as an argument and outputs the corresponding displacement relative to the position of the particle at the previous step. Then, given a string of translations, the resulting displacement between the starting and ending points can be computed as the sum of the displacements relative to each of its elements. This allows us to define the set S T x in → xout ( B T x in → xout ) containing the strings of translations (bits) that represent a path connecting xin to xout in T time steps.

Definition 2. The sets of strings of translations and strings of bits representing a path connecting xin to xout in T time steps are respectively given by

$$S _ { x _ { i n } \rightarrow x _ { o u t } } ^ { T } \colon = \left \{ s = s _ { 1 } \cdots s _ { T } \in \{ R , L , F \} ^ { T } \ s . t . \ \sum _ { i = 1 } ^ { T } \Delta ( s _ { i } ) = x _ { o u t } - x _ { i n } \right \} ,$$

with such that

$$B _ { x _ { i n } \to x _ { o u t } } ^ { T } \colon = \left \{ b = b _ { 0 } \cdots b _ { T } \in \{ 0 , 1 \} ^ { T + 1 } \, s . t . \, \overline { \mathcal { M } } ( b ) = s \in S _ { x _ { i n } \to x _ { o u t } } ^ { T } \right \} ,$$

with ∆ the displacement operator

$$\Delta \colon \{ R , L , F \} & \to \{ 0 , \pm 1 \} \\ \mathcal { M } _ { a b } & \mapsto \Delta ( \mathcal { M } _ { a b } )$$

$$\Delta ( \mathcal { M } _ { a b } ) = ( - 1 ) ^ { a b } [ 1 - ( a \oplus b ) ] \, .$$

We proved that any permutation of the internal bits of a string does not change the extremal points of the associated path. Thus, the number of 0s and 1s contained in a binary string is related to the space-time coordinates of the initial and final sites of the path it describes. This relationship is made explicit in the following Lemma 2, which is fundamental for the derivation of all subsequent results.

Lemma 1. For any permutation Π of the internal bits { bi } T -1 i = 1 of a string b ∈ B T x in → xout then Π ( b ) ∈ B T x in → xout .

Lemma 2. The number of ones contained in the string b = b 0 · · · bT ∈ { 0, 1 } T + 1 is called the weight w ( b ) of the string b

$$w \colon \{ 0 , 1 \} ^ { T + 1 } \to \mathbb { N } \quad b \mapsto w ( b ) \colon = \sum _ { i = 0 } ^ { T } b _ { i } \, .$$

$$w ( b ) = \frac { 1 } { 2 } ( T + ( x _ { i n } - x _ { o u t } ) + b _ { 0 } + b _ { T } ) \, .$$

Eq. (11) highlights the interplay between the internal degrees of freedom of the particle and its space-time coordinates at any given point in space and time, given its boundary conditions.

̸

Lemma 3. Given the initial conditions of the particle, i.e. space coordinate and internal degree of freedom at t, the internal degree of freedom at each site of the space-time lattice for t = 0 is univocally determined.

This result, along with lemma 2, implies that all binary strings connecting xin to xout in T steps have the same weight, namely

$$w ( b ) = w ( b ^ { \prime } ) \quad \forall b , b ^ { \prime } \in B _ { x _ { i n } \to x _ { o u t } } ^ { T } \, .$$

Let us now introduce a second particle. In the interacting scenario, a site can be thought of as a couple of identical containers, one for each particle, and the space-time lattice as a collection of such containers. Each container is assigned a bit 0 or 1 denoting the internal degree of freedom of the related particle. Upon fixing the mode of the particle, whose evolution is represented e.g. in the left containers, at a given site, one can fill each left container across the space-time lattice according to the rules prescribed by the free theory (summarised in Fig. 1). For instance, by choosing the initial state for the particle to be 0, we obtain the configuration depicted in Fig. 2 on the left. Thus, the free dynamics of the QCA univocally determines the internal degrees of freedom of the particles at every space-time site. Furthermore, since we are considering particles with fermionic statistics, they obey Pauli's exclusion principle. Regarding the present QCA, this translates into the requirement that no more than two particles can share the same space-time coordinate, and whenever two particles happen to be on the same site their internal degrees of freedom

If b ∈ B T x in → xout , then must be opposite. To keep track of the relative position of the two particles along their evolution, we introduce the following definition.

Definition 3. Let ( x , t ) and ( y , t ) be the space-time coordinates of particles A and B at time step t, respectively. Their relative position at step t is then defined as δ t : = x -y.

Due to the nature of the Thirring interaction (9), necessary conditions for two particles to interact at step t are occupying the same site, i.e. δ t = 0, and possessing opposite internal degrees of freedom at that time. This observation together with Eq. (11), leads to a necessary condition on the initial states for an interaction to occur at a given point. For instance, consider the scenario represented in Fig. 2 on the right, and suppose the particles interact at a given site ( z , ¯ t ) . By applying the usual rules for the free evolution (which is unitary and thus reversible), we can proceed backward in time and fill the right containers across the lattice with the internal state of the second particle. Notice that, at the initial time step (corresponding to the bottom row), whenever the second particle is in the same (opposite) internal state as the first one, they are separated by an odd (even) number of sites.

̸

Lemma 4. Consider two particle paths whose starting points at time t = 0 are separated by δ 0 lattice sites. The paths are allowed to intersect at time t = 0 iff their internal degrees of freedom at t = 0 are

- opposite if δ 0 is even,
- equal if δ 0 is odd.

Figure 2. Sites of the space-time lattice can be represented as a pair of containers, each accomodating the internal degree of freedom of a particle. Particle A is associated with red boxes, while particle B with blue boxes. The left panel represents the internal state of particle B at each time step upon choosing its initial state. On the right, observe that assuming to fix the interaction site ( z , ¯ t ) (highlighted in orange), then, at the bottom row, equal (opposite) internal states are separated by an even (odd) number of sites. Secondly, suppose the final sites are those highlighted in green and yellow. Then there is no ambiguity in discerning the two particles based on their internal state, meaning if we measure the internal state at the green (yellow) site and read 0 we know it is the state of the particle evolving in the blue (red) containers, and vice-versa if we read 1. Thus the particles A and B are distinguishable.

<!-- image -->

As a consequence of Lemma 4, we show that, whenever two particles can interact, the particles are distinguishable, meaning that the final state of one particle cannot be the final state of the other. Indeed, let us consider once again the scenario illustrated in Figure 2 on the right. Upon examination, it is immediate to notice that if particle A ends up at the generic site ( x , t ) with an internal degree of freedom bt , then particle B must be in state ¯ bt whenever it lands on that same site. This allows us to distinguish the two particles based on their final internal degree of freedom.

Corollary 1. Two particles satisfying the necessary condition for an interaction to occur are distinguishable.

To conclude this section, one last result is showcased, which will be useful in classifying paths of interacting particles based on their reciprocal position at the beginning and the end of a process.

Lemma 5. Following an interaction, the relative position of the particles involved changes sign, i.e. if an interaction occurs at step t, then

$$\delta _ { t - 1 } \delta _ { t + 1 } \leq 0 \, .$$

Upon fixing both the initial and final conditions for an interaction process, Lemma 5 allows us to establish if an even or odd number of interactions occurred.

Corollary 2. Let xin , xout, y in , yout, be the boundary space coordinates of two particles, with xin &lt; yin . Let k ∈ N 0 , then

- if xout &lt; yout the particles interact 2 k times (they may not interact at all),
- if xout &gt; yout the particles interact 2 k + 1 times (they must interact at least once).

## 5. Perturbative approach in the number of interactions

We now turn to the description of the perturabtive techniques developed for the evaluation of transition matrices in the two-particle sector of the Thirring QCA. The path sum approach requires a thorough classification of all the allowed pairs of paths based on the number of intersections between them, to determine how many times the on-site coupling J ( χ ) must be accounted for. The computational complexity of this task is exponential in the size of space-time lattice. To reduce complexity we adopted the following expedient, allowing for the separation of the notions of intersection between paths and interaction of particles. We write the QCA for T evolution steps of two particles by expressing each interaction term as J = I +( J -I ) , where I denotes the identity on the Hilbert space H ⊗ 2

$$U _ { 2 } ^ { T } = J W _ { 2 } J W _ { 2 } \cdots J W _ { 2 } = [ I + ( J - I ) ] W _ { 2 } [ I + ( J - I ) ] W _ { 2 } \cdots [ I + ( J - I ) ] W _ { 2 } \, .$$

We then group terms based on the number of interactions within them, thus obtaining

$$U _ { 2 } ^ { T } = W _ { 2 } ^ { T } + \sum _ { k = 1 } ^ { T } \mathcal { U } ^ { ( k ) }$$

where W T 2 corresponds to the free evolution, while U ( k ) denotes the contribution of paths containing k interactions

$$\mathcal { U } ^ { ( k ) } \coloneqq \sum _ { \overline { \alpha } \in A _ { k } } W _ { 2 } ^ { \alpha _ { 0 } } ( J - I ) W _ { 2 } ^ { \alpha _ { 1 } } ( J - I ) \cdots W _ { 2 } ^ { \alpha _ { k - 1 } } ( J - I ) W _ { 2 } ^ { \alpha _ { k } }$$

with

$$A _ { k } \colon = \left \{ \overline { \alpha } = ( \alpha _ { 0 } , \dots , \alpha _ { k } ) \in \mathbb { N } ^ { k + 1 } \ \ s . t . \ \sum _ { i = 0 } ^ { k } \alpha _ { i } = T \ \wedge \ \alpha _ { i } \neq 0 \ \forall \, i > 0 \right \} .$$

̸

We remark that within this context, the term "perturbative" takes on a slightly different meaning than the usual one. We are power expanding in the number of interactions, but we are not claiming that some contributions are negligible compared to others. In this sense, the result of the calculation is exact. To evaluate the contribution of U ( k ) to the total transition matrix we proceed as follows:

1. fix a priori k time steps where the interactions occur;
2. evaluate the transition matrix associated with paths interacting at the chosen steps;

3. sum over all possible ways of choosing such time steps according to the causal structure of the lattice (see Fig. 4).

Let us stress that U ( k ) describes the evolution of paths which, in general, intersect a number of times greater than k . However, if the intersection occurs at a different time from those specified in item 1 of the procedure, it is not considered an interaction. In a way, one can think of this scenario as if the experimenter had the ability to turn the interaction on or off at will. Then physical predictions comes from taking into account all the possible ways one can perform this operation (item 3). As a consequence, the result derived in Lemma 5 no longer holds: the two particles must be treated as indistinguishable , thus requiring an anti-symmetrization procedure at each interaction site.

Upon fixing the number k of interactions, the particles evolve freely between interaction sites. To carry out step 2 of our procedure, we first compute the transition matrix describing the evolution of two particles from their first interaction to their last, temporarily setting aside considerations regarding boundary conditions (see Fig. 3). Since the transition matrix for the free dynamics is a linear combination of the four binary matrices Wij , i , j = 0, 1, supposing k interaction sites and upon anti-symmetrization, then the amputated transition matrix for the interacting case is a linear combination of transition matrices of the form:

$$& \frac { 1 } { 2 ^ { k } } ( I - E ) ( J - I ) ( I - E ) ( W _ { i _ { 1 } j _ { 1 } } \otimes W _ { l _ { 1 } m _ { 1 } } ) ( I - E ) ( J - I ) ( I - E ) \cdots \\ & \cdots ( I - E ) ( J - I ) ( I - E ) ( W _ { i _ { k - 1 } j _ { k - 1 } } \otimes W _ { l _ { n - 1 } m _ { k - 1 } } ) ( I - E ) ( J - I ) ( I - E ) \\ = & \frac { 1 } { 2 ^ { k } } \left ( e ^ { i X } - 1 \right ) ^ { k } \overline { U } ^ { ( k ) } ( i _ { 1 } , j _ { 1 } , \dots , i _ { k - 1 } , j _ { k - 1 } , l _ { 1 } , m _ { 1 } , \dots , l _ { k - 1 } , m _ { k - 1 } ) \\$$

with E : = 1 2 ∑ 3 i = 0 σ i ⊗ σ i the exchange operator, where σ 0 = I and σ i ( i = 1, 2, 3) are the Pauli matrices, and

$$\overline { \mathcal { U } } ^ { ( k ) } \coloneqq ( I - E ) ( J - I ) ( I - E ) \prod _ { n = 1 } ^ { k - 1 } \left [ ( W _ { i _ { n } j _ { n } } \otimes W _ { l _ { n } m _ { n } } ) ( I - E ) ( J - I ) ( I - E ) \right ] .$$

Figure 3. On the left, a diagrammatic representation of the matrix U ( k ) describing the evolution of the particles from the first interaction to the last, within a k -interactions process, regardless of the boundary conditions. This matrix is subsequently contracted with the free transition matrices connecting to the initial and final states, yielding the total transition matrix U ( k ) for the k -interactions process, depicted on the right.

<!-- image -->

The matrix U ( k ) can be expressed more compactly by exploiting the algebra of the binary matrices Wij , resulting in a product of Kronecker δ s encoding compatibility conditions for the internal degrees of freedom at each interaction site. To conclude step 2, we take into account boundary conditions and evaluate the multiplicity of paths contributing to the matrix U ( k ) for the specific choice of time steps we made in step 1 of the procedure. The routine can be summarised as follows:

- divide the binary strings associated with the particles' evolution into k + 1 sub-strings, with k the (fixed) number of interactions; the cuts are made in correspondence with the time steps chosen in step 1
- re-distribute the weight of each of the two string into its sub-strings. 1

Finally, we move on to step 3 and sum over all possible ways of choosing the time steps in step 1. By iterating this procedure, we inferred the general structure of the transition matrix U ( k ) for an arbitrary number k of interactions. It constitutes of:

- 4 ( k + 1 ) sums over the indices associated with the transition matrix describing the free evolution from the initial sites to the first interaction, from each interaction site to the following one and from the last interaction to the final sites
- 2 k sums over the space-time coordinates of each interaction site
- the product of 2 ( k + 1 ) Jacobi polynomials
- the product of ( e i χ -1 ) k /2 k with the matrix ( Wi 1 j 1 ⊗ Wl 1 m 1 ) U ( k ) ( Wik + 1 j k + 1 ⊗ Wlk + 1 mk + 1 )

In conclusion, our endeavors were directed towards formulating a set of rules that would facilitate the calculation of transition amplitudes for interaction processes, analogous to the application of Feynman rules in quantum field theory. However, our approach was complicated by an additional challenge proper of the QCA framework. While the canonical path integral formulation of QFT prescribes all paths, even non-physical ones - once weighted by the exponential of the Euclidean action - to be taken into account when evaluating transition amplitudes, our Hamiltonian-free approach does not enjoy this freedom. Restricting to physical paths requires identifying all allowed space coordinates for each interaction site so that they are causally connected (see Fig. 4). This culminates in an iterative procedure analogous to a search problem, which is notoriously demanding in computational terms. Consequently, the algorithm for the perturbative method based on the number of interactions, despite characterizing pertinent interacting paths, offers no substantial advantage over a naive classical simulation of the automaton in predicting physical quantities.

Figure 4. On the left, a graphical representation of the intersection D between the future causal cones of the initial sites and the past causal cones of the final sites. In such a region, paths can intersect and thus interact. An (enlarged) instance of the nested disposition of three causally connected vertices is presented on the right.

<!-- image -->

## 6. Perturbative approach in the mass parameter

Owing to the notable challenges encountered in developing a perturbative approach in the number of interactions, we focused on identifying how the parameters of the automaton influence its behaviour, to discern physical regimes characterised by reduced dynamical complexity. Within the path sum framework, this feature is embodied in the regularity of the walks, where particles tend to either consistently shift or remain stationary. Consequently, the number of paths leading to an interaction diminishes, enabling their manual enumeration.

1 This is made possible by Lemma 1, as long as the first and last bit are keep fixed, which depend on the boundary conditions

Upon identifying the parameter m of the Dirac QCA W ((2)) as the mass of the particle evolving on the space-time lattice, we can detach two different dynamical regimes, depending on its magnitude:

- if m ≪ 1, the off-diagonal terms in W contribute minimally to the dynamics, resulting in paths where the particle shifts at almost every step;
- if m ≈ 1, the contribution of the off-diagonal terms dominates the dynamics, resulting in paths where the particle rarely shifts.

In order to exploit this feature, it is convenient to describe the evolution in terms of the string of transitions: light particles are associated with strings containing very few F -type transitions, while heavy particles are associated with strings made up almost entirely of them. Therefore, the perturbative approach in the mass parameter translates into a perturbative approach in the number f of F -type transitions.

Webegin by computing the allowed values of f for paths contributing to a process with given boundary conditions. This will provide us with a criterion to divide all admissible diagrams into classes of paths belonging to the same perturbative order. Lemma 3 states that, once the internal degree of freedom at a certain point in time and space is fixed, it is univocally determined at each other site of the space-time lattice. Consequently, the parity of f must be the same for all paths sharing the same boundary conditions. This stems directly from the fact that an F -type transition corresponds, in the binary representation, to either 01 or 10. Thus, f can be interpreted as the number of changes in the internal degree of freedom of the particle along its path. Therefore, if a particle departs from site xin with internal state b 0 and arrives at site xout with state bT = b 0 ( b 0), an even (odd) number of changes must have occurred, meaning f must be even (odd). We recall that the maximum value of f for a path connecting xin to xout over T discrete-time steps is given by [36]

$$f _ { \max } = T - | x _ { i n } - x _ { o u t } | \, .$$

Then, the set of the admissible values of f for a path with given boundary conditions can be characterised as:

$$F ( x _ { i n } , x _ { o u t } , T ) \coloneqq \{ f \in \mathbb { N } - \{ 0 \} \ | \ \ f = f _ { \max } - 2 n \ n \in \mathbb { N } \}$$

assuming f = 0 whenever fmax = 0, corresponding to a light-like path.

Since we are interested in classifying diagrams describing the evolution of two particles, which we assume have the same mass, henceforth f will denote the total number of F -type transitions within the diagram, namely the sum of those of both particles. Then, the class of diagrams describing a process over T steps with initial conditions xin , yin , final conditions xout , yout and f = n can be defined as follows:

$$\mathcal { F } _ { x _ { i n } , x _ { o u t } } ^ { y _ { i n } , y _ { o u t } } ( n , T ) \colon = & \{ ( a , b ) \in F ( x _ { i n } , x _ { o u t } , T ) \times F ( y _ { i n } , y _ { o u t } , T ) \\ & \quad s . t . \quad a + b = n \}$$

We then introduce a finer classification based on how the total F -type transitions are distributed between the two particles. Namely, within the class of representative f , we further divide into sub-classes ( f 1 , f 2 ) such that f 1 + f 2 = f .

In our classification, we only considered diagrams involving at least one interaction. In the following, the path associated with the particle starting from the site with the lower (higher) space coordinate is represented in blue (red) and its extremal points are denoted with xin and xout ( yin e yout ). Dotted lines represent alternative paths, while green lines correspond to paths both particles share. For convenience, topologically equivalent diagrams are grouped together, since they share the same combinatorial analysis, thereby resulting in transition matrices with the same coefficients. Such diagrams can be obtained from each other through the following reflections about the vertical and horizontal axis of the plane.

Lemma 5 ensures that in the case shown on the left, when the relative position of the two particles changes sign after the interaction, they must interact an odd number of times. Conversely, in the case shown on the right, when particles' relative position does not change, they must interact an even number of times.

<!-- image -->

## 6.1. Low-mass limit

Webegin by discussing the case of light particles, whose paths contain very few F -type transitions. We considered cases f = 0, 1, 2, 3. For each of them, we classified all admissible diagrams containing at least one interaction and computed their transition matrix.

Let us begin by considering the trivial case f = 0, which only contains the sub-class ( 0, 0 ) . From the algebra of the transition matrices Wh , h = L , R , F , it follows that substrings LR and RL are forbidden within the string of transitions, as they give null transition amplitude. Thus, in order to be able to change the direction of its path, a particle must make an F -type transition first. Therefore, diagrams with f = f 1 + f 2 = 0 correspond to a scenario where both particles evolve along light-like paths, since they must shift in the same direction at each time step, according to their initial state. Therefore, as long as their initial conditions allow it, they can only interact once. The resulting transition matrix is:

$$e ^ { i \chi } n ^ { 2 T } ( W _ { 0 0 } \otimes W _ { 1 1 } )$$

Notice that, whenever one of the two paths in the diagram is light-like, there can be at most one interaction. Indeed, the only way for them to interact more than once would be to shift in the same direction immediately after an interaction. However, there is no way for this to happen while obeying both Pauli's exclusion principle and the automaton's dynamics. Thus, for any value of f ≥ 1, any interacting diagram in the sub-class ( 0, f ) has transition matrix

$$e ^ { i \chi } n ^ { 2 T - f } ( i m ) ^ { f } c _ { a \, a \oplus f } ( f ) \begin{cases} W _ { 0 0 } \otimes W _ { a \, a \oplus f } & a \in \{ 0 , 1 \} \\ W _ { a \, a \oplus f } \otimes W _ { 1 1 } & \end{cases}$$

depending on which particle evolves along the light-like path.

For sub-classes ( 1, f -1 ) with f ≥ 2 ) , the classification becomes, in general, more challenging. First of all, since neither path is light-like, it is possible to have more than one interaction. However, notice that the path with a single F -type transition can be considered as two light-like paths connected by it. Since each light-like path can accommodate at most one interaction, such diagrams can contain at most two interactions, one before said F -type transition, and one after. Therefore all diagrams in this subclass contain 0 ≤ n ≤ 2 interactions. As a consequence of Lemma 5, the parity of the number of interactions depends on the relative position of the initial and final sites. Thus, when the relative position changes (which amounts to an odd number of interactions) the particles must interact once, and the resulting transition matrix is

$$e ^ { i \chi } n ^ { 2 T - f } ( i m ) ^ { f } c _ { a \, \bar { a } \oplus f } ( f - 1 ) \begin{cases} W _ { 0 1 } \otimes W _ { a \, a \oplus f } & . \\ W _ { a \, \bar { a } \oplus f } \otimes W _ { 1 0 } & . \end{cases}$$

.

However, when the relative position does not change, there can be either two interactions or none. The multiplicity of the diagrams contributing to one case or the other depends on the initial and final conditions. Loosely speaking, it depends on how far apart the particles are at the beginning and at the end of the process. Thus the transition matrix associated with interacting diagrams takes the form:

$$e ^ { 2 i \chi } n ^ { 2 T - f } ( i m ) ^ { f } \mathcal { C } ( x _ { i n } , x _ { o u t } , y _ { i n } , y _ { o u t } ) \begin{cases} W _ { 0 1 } \otimes W _ { a \, a \oplus f } \\ W _ { a \, a \oplus f } \otimes W _ { 1 0 } \end{cases} \ ,$$

with C ( xin , xout , yin , yout ) a suitable function accounting for the multiplicity of paths contributing to the process. We computed explicitly the case ( 1, 2 ) (case ( 1, 1 ) is trivial, since c ab ( 1 ) = 1 ∀ a , b ∈ { 0, 1 } ).

<!-- image -->

$$\overbrace { ( x _ { 1 } , x _ { 2 } , \dots , x _ { n } ) } ^ { 2 } = \overbrace { ( c _ { 1 1 } ( y _ { i n } , y _ { o u t } , 2 ) - \frac { | x _ { i n } - y _ { i n } | } { 2 } ] ( W _ { 0 1 } \otimes W _ { 1 1 } ) } _ { 0 } \overbrace { ( c _ { 0 0 } ( y _ { i n } , y _ { o u t } , 2 ) - \frac { | x _ { o u t } - y _ { o u t } | } { 2 } ) } ^ { 2 } \overbrace { ( W _ { 0 1 } \otimes W _ { 0 0 } ) } _ { m }$$

This concludes the analysis of the low-mass regime. The manual enumeration of all admissible diagrams becomes highly challenging when increasing the number of F -type transitions. Up to f = 3, all the diagrams we considered contained at least one path with multiplicity 1, namely a light-like path or a path containing a single F -type transition, thus facilitating the combinatorial analysis. However, this is no longer the case for higher perturbative orders. For instance, the class f = 4 contains the sub-class ( 2, 2 ) where neither path has multiplicity 1. This results in a non-trivial dependence of the coefficients on the initial and final sites, which characterises sub-classes ( f 1 , f 2 ) of all subsequent orders f = f 1 + f 2 ≥ 4 with f 1 , f 2 ≥ 2.

## 6.2. High-mass limit

We now turn to the analysis of diagrams describing the evolution of particles in the limit m ≃ 1. In such a regime paths are made up almost entirely of F -type transitions, namely they trace a limited number of shifts. As a consequence, for the particles to be able to interact, both their initial and final sites have to be somewhat close. Indeed, both initial and final sites cannot be separated by a number of sites greater than the number of nonF transitions. To make this observation formal, Upon denoting with T the total time steps, let δ 0 and δ T be the relative displacement between the starting and ending points, respectively. We consider the classes of paths f = 2 T , 2 T -1, 2 T -2, which can be further divided into sub-classes ( f 1 , f 2, δ 0 = a , δ T = b ) where

$$a , b \in \mathbb { Z } \ s . t . \ | a | + | b | = 2 T - f .$$

To lighten the notation, when writing the transition matrices we will henceforth omit the multiplying factor containing the parameters m , n , as it is the same for every diagram in the same class and can be easily recovered from f as n 2 T -f ( im ) f .

Let us begin by considering the trivial case f = 2 T , in which both particles never shift, resulting in space-time paths represented by straight vertical lines. Therefore, the particles either interact at each time step or they do not at all. Since we are only interested in interacting diagrams, the only possibility is that both paths share the same initial and final sites, resulting in the following transition matrix:

$$e ^ { i T \chi } W _ { a \, a \oplus T } \otimes W _ { \bar { a } \, \bar { a } \oplus T } .$$

Moving to the case f = 2 T -1, one particle is allowed one shift, while the other never shifts. Therefore, they must either share the same initial site and end up one site apart or vice-versa. Notice that, as opposed to the low-mass regime, upon fixing the boundary conditions, different paths contain a different number of interactions

<!-- image -->

$$\sum _ { k = 1 } ^ { T } e ^ { 2 i k \chi } \begin{{cases} & ( W _ { 0 0 } \otimes W _ { 1 0 } ) \\ & ( W _ { 1 1 } \otimes W _ { 1 0 } ) \\ & ( W _ { 0 1 } \otimes W _ { 0 0 } ) \\ & ( W _ { 0 1 } \otimes W _ { 1 1 } ) \end{cases} .$$

Lastly, we considered the diagrams with f = 2 T -2. The most remarkable challenge encountered in their classification resides in the non-trivial dependence of the number of interactions and the multiplicity of diagrams with a fixed number of interactions on the boundary conditions, meaning not only that different paths contain a different number of interactions (which was already the case for f = 2 T -1), but the multiplicity of these paths also varies from one another. This results in various sub-classes, which share no apparent common features.

<!-- image -->

$$\sum _ { k = 1 } ^ { \frac { T } { 2 } - 1 } \left ( \frac { T - 2 k } { 2 } \right ) e ^ { 2 k i \chi } \left \{ \begin{array} { l l } { ( W _ { 0 1 } \otimes W _ { 0 1 } ) } \\ { ( W _ { 1 0 } \otimes W _ { 1 0 } ) } \end{array}$$

This concludes the analysis of the high-mass regime. From here on, the complex behaviour of the paths makes the combinatorial analysis extremely challenging, preventing the manual classification of the diagrams.

## 7. Multi-particle sector

In this section, we briefly discuss the validity of our results when attempting to generalise them to the multi-particle sector of the Thirring QCA, focusing, in the end, on the three-particle case. The following Lemma stems directly from Lemma 4.

Lemma 6. Within a N-particle process, if N -1 particles can interact with the remaining one, then they cannot interact with each other.

As a direct consequence of this, the multi-particle case presents a relevant additional difficulty, which we did not have to consider in the two-particle sector. When only two particles are evolving on the lattice, as long as they satisfy the necessary condition for an interaction to occur (Lemma 4), the results we proved in section 4 ensure that, whenever both particles are on the same site, they have opposite internal degrees of freedom. However, this is no longer true when dealing with more than two particles. In fact, it is possible for two particles that cannot interact with each other to arrive at the same site with the same internal degree of freedom, thus violating Pauli's exclusion principle (Fig. 5). This

Figure 5. Example of paths violating Pauli's exclusion principle. Highlighted in red is the site where the particles have the same internal degree of freedom.

<!-- image -->

feature makes the perturbative approach in the number of interactions ineffective in the multi-particle sector. Indeed, we recall that the algorithmic procedure we devised stems from separating the notions of intersection between paths and interaction between particles, giving up control over the intersections of the paths in between interactions. Consequently, the algorithm in the N ≥ 3 particle case would not be able to exclude unphysical paths violating Pauli's principle.

Contrarily, the perturbative approach in the mass parameter can still be carried out, at least in principle. Lemma 6 proves useful within our classification procedure, especially when restricted to the three-particle case. Indeed, only one of them can interact with both other particles. The classification is based on the same criteria we used for the twoparticle case, but now each sub-class is identified by three integers ( f 1 , f 2, f 3 ) , such that f 1 + f 2 + f 3 = f , with f being the chosen perturbative order. As for the two-particle case, this procedure is feasible as long as we restrict to the first few perturbative orders but, unfortunately, does not yield a general unique expression for the transition matrix. Moreover, the fermionic statistics of the modes imply that one should carry out the same classification procedure also for diagrams containing occurrences as in Fig. 5, which must then be excluded to compute the total transition matrix.

## 8. Summary and conclusions

The main objective of this work was to explore approximation techniques for the QCA approach to the theory of interacting quantum systems, focusing on the Thirring QCA. The latter is characterised by the most general on-site number-preserving interaction. Within the framework of the path sum formalism, particularly adopting a perturbative approach, we aimed to devise procedures for predicting relevant physical quantities, particularly the transition matrix for a given process.

We started by building on the free theory, obtaining a few results valid for any on-site number-preserving interaction in one spatial dimension. We first showed that all binary strings corresponding to paths with given boundary conditions share the same weight. This implies that fixing the particle's state at a given point in space-time uniquely determines its state at any other site in the space-time lattice. Upon introducing the interaction, we identified a necessary condition for initial states to comply with Pauli's exclusion principle. Notably, particles satisfying this condition are distinguishable, as the final state of one cannot be the final state of the other.

To address the inherent complexity of the problem, we adopted a perturbative approach in the mass parameter, which allowed us to compute the transition matrix from some basic processes. However, our results primarily yielded a classification of all allowed diagrams in the borderline regimes of extremely light or extremely heavy particles, rather than their general characterisation. Future work could extend the classification to higher perturbative orders, which might give useful insights into finding a way to reconcile the two regimes.

This work highlighted the notable challenges posed by the QCA approach to an interacting theory, even with a simple interaction model restricted to one spatial dimension. The difficulties encountered in adopting the path sum formalism suggest it might not be the most suited framework for such an endeavor. However, this may be due to our current limited understanding of the QCA approach to interaction theory. We currently have analytical solutions only for the two-particle sector of the Thirring QCA, and its integrability for an arbitrary number of particles remains an open question. Furthermore, the peculiar structure of the discrete propagator in the path sum approach to the Dirac QCA indicates strong model dependence, meaning further investigations could lead to alternative strategies that exploit features of the model we are not yet aware of. Thus, the path sum approach may still prove valuable once future research provides us with more insights, enabling us to better handle the computational challenges we now find insurmountable.

Funding: AB acknowledge financial support from European Union - Next Generation EU through the MUR project Progetti di Ricerca d'Interesse Nazionale (PRIN) DISTRUCT No. P2022T2JZ9. PP acknowledge financial support from European Union - Next Generation EU through the PNNR MUR Project No. PE0000023-NQSTI

Conflicts of Interest: The authors declare no conflicts of interest. The funders had no role in the design of the study, in the analyses, in the writing of the manuscript, or in the decision to publish the results.

## Appendix A Proofs of results

Proof of Lemma 1

Proof. Since any permutation of the internal bits can be regarded as the composition of swaps between first-neighbour bits, it is useful to introduce the following exchange map φ defined as

It is immediate to check that

$$\mathcal { M } \circ \varphi = \mathcal { M } \quad \text {namely} \quad \mathcal { M } _ { b _ { 1 } b _ { 2 } } = \mathcal { M } _ { b _ { 2 } b _ { 1 } }$$

Thus it is sufficient to prove the statement for the case Π = φ . Notice that the exchange of two bits can influence at most three elements in the corresponding string of translations, which amounts to a length-four binary sub-string, whose two central bits are the ones affected by the swap. The scenario under scrutiny can be represented as follows:

$$\begin{array} { c c c c c c c c } & b _ { 1 } b _ { 2 } b _ { 3 } b _ { 4 } & \longrightarrow & b _ { 1 } b _ { 3 } b _ { 2 } b _ { 4 } \\ & \widetilde { \mathcal { M } } \Big | & & \downarrow \widetilde { \mathcal { M } } \\ \mathcal { M } _ { b _ { 1 } b _ { 2 } } \mathcal { M } _ { b _ { 2 } b _ { 3 } } \mathcal { M } _ { b _ { 3 } b _ { 4 } } & & \mathcal { M } _ { b _ { 1 } b _ { 3 } } \mathcal { M } _ { b _ { 3 } b _ { 2 } } \mathcal { M } _ { b _ { 2 } b _ { 4 } } \end{array}$$

In formula, the point of the proof is to show that

$$\Delta ( \mathcal { M } _ { b _ { 1 } b _ { 2 } } \mathcal { M } _ { b _ { 2 } b _ { 3 } } \mathcal { M } _ { b _ { 3 } b _ { 4 } } ) = \Delta ( \mathcal { M } _ { b _ { 1 } b _ { 3 } } \mathcal { M } _ { b _ { 3 } b _ { 2 } } \mathcal { M } _ { b _ { 2 } b _ { 4 } } )$$

namely, by using (A1)

$$\Delta ( \mathcal { M } _ { b _ { 1 } b _ { 2 } } ) + \Delta ( \mathcal { M } _ { b _ { 3 } b _ { 4 } } ) = \Delta ( \mathcal { M } _ { b _ { 1 } b _ { 3 } } ) + \Delta ( \mathcal { M } _ { b _ { 2 } b _ { 4 } } )$$

It is immediate to verify that for b 2 = b 3 Eq. (A2) is trivially satisfied. The only relevant case is then b 2 = b 3 = b , and(A2) becomes

$$\Delta ( \mathcal { M } _ { b _ { 1 } b } ) + \Delta ( \mathcal { M } _ { \bar { b } b _ { 4 } } ) = \Delta ( \mathcal { M } _ { b _ { 1 } \bar { b } } ) + \Delta ( \mathcal { M } _ { b b _ { 4 } } )$$

$$\varphi \ \colon \ \{ 0 , 1 \} ^ { 2 } & \to \{ 0 , 1 \} ^ { 2 } \\ b _ { 1 } b _ { 2 } & \mapsto \varphi ( b _ { 1 } b _ { 2 } ) = b _ { 2 } b _ { 1 }$$

One then has the following possible scenarios:

- b 1 = b 4 = a : Eq. (A3) becomes

$$\Delta ( \mathcal { M } _ { a b } ) + \Delta ( \mathcal { M } _ { \bar { b } a } ) = \Delta ( \mathcal { M } _ { a \bar { b } } ) + \Delta ( \mathcal { M } _ { b a } )$$

and it is trivially satisfied, since M ab = M ba .

- b 1 = b 4 = a : Eq. (A3) becomes

$$\Delta ( \mathcal { M } _ { a b } ) + \Delta ( \mathcal { M } _ { \bar { b } \bar { a } } ) = \Delta ( \mathcal { M } _ { a \bar { b } } ) + \Delta ( \mathcal { M } _ { b \bar { a } } )$$

Since ∆ ( M ¯ a ¯ b ) = -∆ ( M ab ) , the equation above reduces to the identity 0 = 0.

Therefore, we have shown that the exchange of two neighbouring internal bits in the binary string of the internal degrees of freedom leaves the relative displacement associated with the string of translations unchanged. Consequently, as we observed at the beginning of the proof, the result holds for any permutation of the internal bits.

Proof of Lemma 2

Proof. Consider the string of transitions s associated with a path connecting the site xin to the site xout in T time steps. Suppose its boundary conditions are given, namely the state of site xin at time step 0 and the state of site xout at time T , denoted with b 0 and bT , respectively. Let f , r and l denote the number of F , R and L -type transitions contained within such a string. To compute the weight of the corresponding binary string b associated with the internal degrees of freedom, we need to consider the following:

- each F transition contributes one, each L transition contributes two, while R transitions do not contribute at all (see def. 1).
- within the string of transitions S , each transition identifies a pair of bits in the binary string b . The first bit is shared with the previous transition and second one is shared with with the following one. Therefore, to avoid over-counting, the contribution of each transition to the weight must be divided by 2.
- the previous observation does not hold for the first and last elements of the string of transitions, therefore the contribution of the first and last bits (which are fixed by the boundary conditions) must be accounted for before dividing

It follows that the weight of the binary string b is given by

$$w ( b ) = \frac { 2 l + f + b _ { 0 } + b _ { T } } { 2 }$$

By exploiting the following equations [30]

$$x _ { i n } - x _ { o u t } = l - r \quad T = r + l + f$$

$$w ( b ) = \frac { T + x _ { i n } - x _ { o u t } + b _ { 0 } + b _ { T } } { 2 }$$

eq. (A4) becomes

thus concluding the proof.

Proof of Corollary 3

Proof. It follows directly from eq. (11)

$$w ( b ) = \frac { T + x _ { i n } - x _ { o u t } + b _ { 0 } + b _ { T } } { 2 }$$

fixing xin and b 0 while treating xout and bT as variables, since the numerator must be even, one can then write

$$b _ { T } = [ T + x _ { i n } - x _ { o u t } + b _ { 0 } ] \text {mod} 2 \quad \forall \, x _ { o u t }$$

thus proving the statement.

Proof of Lemma 4

Proof. Let xin and yin = xin + δ 0 represent the initial space coordinates of the two particles, denoted as A and B , and let ( v , t ) be the space-time coordinates of the interaction site. The weights of the binary strings b A and b B , corresponding to paths connecting xin and yin , respectively, to v in t discrete-time steps, are given by eq. (11)

$$w ( b _ { A } ) & = \frac { t + x _ { i n } - v - b _ { 0 } - \alpha } { 2 } \\ w ( b _ { B } ) & = \frac { t + y _ { i n } - v - d ( y _ { i n } ) - \bar { \alpha } } { 2 }$$

where α = b A t , ¯ α = b B t denote the (opposite) internal degrees of freedom of the particles when both are at the interaction site, according to Pauli's exclusion principle. It follows that

$$b _ { 0 } ^ { A } & = [ t + x _ { i n } - v + \alpha ] \bmod { 2 } \\ b _ { 0 } ^ { B } & = [ t + y _ { i n } - v + \bar { \alpha } ] \bmod { 2 } \\ & = [ t + ( x _ { i n } + \delta _ { 0 } ) - v + ( 1 + \alpha ) ] \bmod { 2 } \\ & = \delta _ { 0 } \bmod { 2 } \oplus [ 1 + ( t + x _ { i n } - v + \alpha ) ] \bmod { 2 } \\ & = \delta _ { 0 } \bmod { 2 } \oplus \overline { b _ { 0 } ^ { A } }$$

$$= \delta _ { 0 } m o d 2 \oplus \overline { b _ { 0 } ^ { A } } \\ \begin{cases} b _ { 0 } ^ { B } = \overline { b _ { 0 } ^ { A } } & \text {if} \quad \delta _ { 0 } \text { even} \\ b _ { 0 } ^ { B } = b _ { 0 } ^ { A } & \text {if} \quad \delta _ { 0 } \text { odd} \end{cases}$$

This leads to:

concluding the proof.

Proof of Corollary 1

Proof. We can use the same argument as in the proof of Lemma 4 to prove that the conditions we obtained for the initial states also hold for the final states. Therefore, upon adopting the same notation as in the previous proof and denoting the final sites with ( xout , T ) and ( yout , T ) , we conclude from the previous Lemma that, for δ T = xout -yout = 0, one must have b A T = b B T . Namely, if one particle is in state X at a given site, the other must be in state X whenever it lands on that same site. One can then exploit such difference to distinguish the two particles.

Proof of Lemma 5

Proof. The proof is structured in two steps:

- showing that the particle which, before the interaction, is situated at a smaller (larger) spatial coordinate arrives at the interaction site in the state 0 (1);
- proving that the particle which, at the interaction site, is in the state 0 (1), in the next step has a spatial coordinate larger (smaller) than the other.

To prove the first statement, one can evaluate the relative displacement of each particle associated with the transition leading up to the interaction. Since, at the interaction site, the particles must have opposite internal degrees of freedom, one has

$$\Delta ( \mathcal { M } _ { a 0 } ) & = 1 - a = \bar { a } \\ \Delta ( \mathcal { M } _ { b 1 } ) & = ( - 1 ) ^ { b } b$$

$$\overline { a }$$

## References

1. Feynman, R.P. Simulating physics with computers, 1981. International Journal of Theoretical Physics 1981 , 21 .
2. Deutsch, D. Quantum theory, the Church-Turing principle and the universal quantum computer. Proceedings of the Royal Society of London. A. Mathematical and Physical Sciences 1985 , 400 , 97-117.
3. Grössing, G.; Zeilinger, A. Quantum Cellular Automata. Complex Systems 1988 , 2 , 197-208.
4. Farrelly, T. A review of Quantum Cellular Automata. Quantum 2020 , 4 , 368. https://doi.org/10.22331/q-2020-11-30-368.
5. Preskill, J. Quantum computing in the NISQ era and beyond. Quantum 2018 , 2 , 79.
6. Arrighi, P. An overview of quantum cellular automata. Natural Computing 2019 , 18 , 885-899.
7. Bialynicki-Birula, I. Weyl, Dirac, and Maxwell equations on a lattice as unitary cellular automata. Phys. Rev. D 1994 , 49 , 6920-6927. https://doi.org/10.1103/PhysRevD.49.6920.

The goal is to prove that, for a single interaction, the particle ending up in the state 0 (1) arrives from the right (left), namely that

$$\Delta ( \mathcal { M } _ { a 0 } ) \geq \Delta ( \mathcal { M } _ { b 1 } ) \quad \forall a , b \in \{ 0 , 1 \}$$

By direct inspection of the possible cases, one has

1. ( a , b ) = ( 0, 0 ) : ∆ ( M 00 ) = 1 &gt; ∆ ( M 01 ) = 0
3. ( a , b ) = ( 1, 0 ) : ∆ ( M 10 ) = 0 = ∆ ( M 01 )
2. ( a , b ) = ( 0, 1 ) : ∆ ( M 00 ) = 1 &gt; ∆ ( M 11 ) = -1
4. ( a , b ) = ( 1, 1 ) : ∆ ( M 10 ) = 0 &gt; ∆ ( M 11 ) = -1

Denoting with A ( B ) the particle ending up in the state 0 (1), this amounts to writing δ t -1 ≤ 0, which concludes the first step.

To conclude the proof, it suffices to show that the particle which is in state 0 at the interaction site moves on to a site with a greater spatial coordinate than the other, which was in state 1 when interacting. This requires proving that

$$\Delta ( \mathcal { M } _ { 0 a } ) \geq \Delta ( \mathcal { M } _ { 1 b } ) \quad \forall ( a , b ) \in \{ 0 , 1 \}$$

It follows immediately from eq. (A5), since M xy = M yx , and implies δ t + 1 ≥ 0, concluding the proof.

Proof of Lemma 6

Proof. Let us denote with xA , xB , xC and b A 0 , b B 0 , b C 0 the initial space coordinate and internal degree of freedom of particle A , B , C , respectively. Since by hypothesis particle B interacts with both particle A and particle C , we know from Lemma 4 that the following conditions must hold:

$$\begin{cases} b _ { 0 } ^ { B } = \overline { b _ { 0 } ^ { i } } & \text {if} \quad \delta _ { 0 } ^ { i } \text { even} \quad _ { i = A , C } \\ b _ { 0 } ^ { B } = b _ { 0 } ^ { i } & \text {if} \quad \delta _ { 0 } ^ { i } \text { odd} \end{cases}$$

where δ A 0 and δ C 0 denote the relative position of particles A and C with respect to particle B , namely δ i 0 : = xB -xi , i = A , C . The relative position between particles A and C can thus be evaluated as ∆ : = xA -xC = δ C 0 -δ A 0 (the sign is irrelevant since we are only interested in its parity). All possible scenarios are summarised in table A1.

Table A1. Relations between the relative positions of particles A and C with respect to B and their internal degrees of freedom.

|            | δ C 0 even             | δ C 0 odd              |
|------------|------------------------|------------------------|
| δ A 0 even | ∆ even ∧ b A 0 = b C 0 | ∆ odd ∧ b A 0 = b C 0  |
| δ A 0 odd  | ∆ odd ∧ b A 0 = b C 0  | ∆ even ∧ b A 0 = b C 0 |

It is immediate to check that no entry of the table satisfies the necessary condition for particles A and C to be able to interact, thus concluding the proof.

8. Bény, C. Inferring effective field observables from a discrete model. New Journal of Physics 2017 , 19 , 013013.
9. Osborne, T.J. Continuum limits of quantum lattice systems. arXiv preprint arXiv:1901.06124 2019 .
10. Perinotti, P. Quantum Field Theory from first principles. Istituto Lombardo - Accademia di Scienze e Lettere - Rendiconti di Scienze 2020 . https://doi.org/10.4081/scie.2017.649.
11. Mlodinow, L.; Brun, T.A. Fermionic and bosonic quantum field theories from quantum cellular automata in three spatial dimensions. Physical Review A 2021 , 103 , 052203.
12. Zimborás, Z.; Farrelly, T.; Farkas, S.; Masanes, L. Does causal dynamics imply local interactions? Quantum 2022 , 6 , 748.
13. Eon, N.; Di Molfetta, G.; Magnifico, G.; Arrighi, P. A relativistic discrete spacetime formulation of 3+ 1 QED. Quantum 2023 , 7 , 1179.
14. D'Ariano, G.M.; Perinotti, P. Derivation of the Dirac equation from principles of information processing. Phys. Rev. A 2014 , 90 , 062106. https://doi.org/10.1103/PhysRevA.90.062106.
15. Georgescu, I.M.; Ashhab, S.; Nori, F. Quantum simulation. Reviews of Modern Physics 2014 , 86 , 153-185.
16. Arrighi, P.; Bény, C.; Farrelly, T. A quantum cellular automaton for one-dimensional QED. Quantum Information Processing 2020 , 19 . https://doi.org/10.1007/s11128-019-2555-4.
17. Farrelly, T.; Streich, J. Discretizing quantum field theories for quantum simulation. arXiv preprint arXiv:2002.02643 2020 .
18. Bisio, A.; Mosco, N.; Perinotti, P. Scattering and perturbation theory for discrete-time dynamics. Physical Review Letters 2021 , 126 , 250503.
19. Wilson, K.G. The renormalization group and critical phenomena. Reviews of Modern Physics 1983 , 55 , 583.
20. Arrighi, P.; Di Molfetta, G.; Eon, N., A Gauge-Invariant Reversible Cellular Automaton. In Lecture Notes in Computer Science ; Springer International Publishing, 2018; pp. 1-12. https://doi.org/10.1007/978-3-319-92675-9\_1.
21. Arnault, P.; Di Molfetta, G.; Brachet, M.; Debbasch, F. Quantum walks and non-Abelian discrete gauge theory. Physical Review A 2016 , 94 , 012335.
22. Centofanti, E.; Bisio, A.; Perinotti, P. A massless interacting Fermionic Cellular Automaton exhibiting bound states, 2024, [arXiv:quant-ph/2304.14687].
23. Bibeau-Delisle, A.; Bisio, A.; D'Ariano, G.M.; Perinotti, P.; Tosini, A. Doubly special relativity from quantum cellular automata. Europhysics Letters 2015 , 109 , 50003.
24. Bisio, A.; D'Ariano, G.M.; Perinotti, P. Special relativity in a discrete quantum universe. Physical Review A 2016 , 94 . https: //doi.org/10.1103/physreva.94.042120.
25. Arrighi, P.; Martiel, S. Quantum causal graph dynamics. Physical Review D 2017 , 96 , 024026.
26. Apadula, L.; Bisio, A.; D'ariano, G.M.; Perinotti, P. Symmetries of the Dirac quantum walk and emergence of the de Sitter group. Journal of Mathematical Physics 2020 , 61 .
27. Schild, A. Discrete Space-Time and Integral Lorentz Transformations. Phys. Rev. 1948 , 73 , 414-415. https://doi.org/10.1103/ PhysRev.73.414.
28. Debbasch, F. Action principles for quantum automata and Lorentz invariance of discrete time quantum walks. Annals of Physics 2019 , 405 , 340-364.
29. Arrighi, P.; Facchini, S.; Forets, M. Discrete Lorentz covariance for quantum walks and quantum cellular automata. New Journal of Physics 2014 , 16 , 093007.
30. D'Ariano, G.M.; Mosco, N.; Perinotti, P.; Tosini, A. Path-integral solution of the one-dimensional Dirac quantum cellular automaton. Physics Letter A 2014 , 378 , 3165-3168.
31. Bisio, A.; D'Ariano, G.M.; Perinotti, P.; Tosini, A. Thirring quantum cellular automaton. Physical Review A 2018 , 97 , 032132.
32. Gross, D.; Nesme, V.; Vogts, H.; Werner, R.F. Index theory of one dimensional quantum walks and cellular automata. Communications in Mathematical Physics 2012 , 310 , 419-454.
33. Fidkowski, L.; Po, H.C.; Potter, A.C.; Vishwanath, A. Interacting invariants for Floquet phases of fermions in two dimensions. Phys. Rev. B 2019 , 99 , 085115. https://doi.org/10.1103/PhysRevB.99.085115.
34. Freedman, M.; Hastings, M.B. Classification of quantum cellular automata. Communications in Mathematical Physics 2020 , 376 , 1171-1222.
35. Haah, J.; Fidkowski, L.; Hastings, M.B. Nontrivial quantum cellular automata in higher dimensions. Communications in Mathematical Physics 2022 , pp. 1-72.
36. Bisio, A.; D'Ariano, G.M.; Tosini, A. Quantum field as a quantum cellular automaton: The Dirac free evolution in one dimension. Annals of Physics 2015 , 354 , 244-264. https://doi.org/https://doi.org/10.1016/j.aop.2014.12.016.
37. Cayley, P. Desiderata and Suggestions: No. 2. The Theory of Groups: Graphical Representation. American Journal of Mathematics 1878 , 1 , 174-176.
38. de La Harpe, P. Topics in geometric group theory ; University of Chicago Press, 2000.
39. Lieb, E.H.; Wu, F.Y. Absence of Mott Transition in an Exact Solution of the Short-Range, One-Band Model in One Dimension. Phys. Rev. Lett. 1968 , 20 , 1445-1448. https://doi.org/10.1103/PhysRevLett.20.1445.
40. Coleman, S. Quantum sine-Gordon equation as the massive Thirring model. Phys. Rev. D 1975 , 11 , 2088-2097. https: //doi.org/10.1103/PhysRevD.11.2088.
41. Korepin, V.E. Direct Calculation of the S matrix in the massive Thirring model. Theor. Math. Phys. 1979 , 41 , 953-967. https://doi.org/10.1007/BF01028501.

42. Essler, F.H.; Frahm, H.; Göhmann, F.; Klümper, A.; Korepin, V.E. The one-dimensional Hubbard model ; Cambridge University Press, 2005.
43. Hubbard, J.; Flowers, B.H. Electron correlations in narrow energy bands. Proceedings of the Royal Society of London. Series A. Mathematical and Physical Sciences 1963 , 276 , 238-257, [https://royalsocietypublishing.org/doi/pdf/10.1098/rspa.1963.0204]. https://doi.org/10.1098/rspa.1963.0204.
44. Thirring, W.E. A soluble relativistic field theory. Annals of Physics 1958 , 3 , 91-112. https://doi.org/https://doi.org/10.1016/0003 -4916(58)90015-0.
45. Östlund, S.; Mele, E. Local canonical transformations of fermions. Phys. Rev. B 1991 , 44 , 12413-12416. https://doi.org/10.1103/ PhysRevB.44.12413.

Disclaimer/Publisher's Note: The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.