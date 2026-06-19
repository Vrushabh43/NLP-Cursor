## Independent Chiral Control in Theory-Space Models: A Rank-Preserving Framework and Its Application to Neutrino Mass Generation

Aadarsh Singh ∗

Centre for High Energy Physics, Indian Institute of Science, C V Raman Avenue, Bangalore 560 012, India

(Dated: June 17, 2026)

We develop a general framework of rank-preserving, element-wise matrix transformations for engineering fermion mass hierarchies in theory-space constructions. We prove that preservation of massless modes requires the transformation function to be separable, g f ( i, j ) = g ( L ) f ( i ) g ( R ) f ( j ), which in turn enables independent control of left- and right-chiral zero-mode profiles directly at the level of the theory-space mass matrix. This formalism unifies and extends the clockwork mechanism, permits controlled deformation of Kaluza-Klein spectra, and enhances hierarchy generation in GIMlike fine-cancellation scenarios. As a concrete application, we show that in theory-space models for neutrino masses, suitable transformations allow sub-eV light neutrinos to arise from TeV-scale new physics with only O (40) additional fermionic sites, while remaining consistent with charged-lepton flavor-violation bounds. In contrast, the corresponding untransformed models asymptote at the MeV scale and cannot access the phenomenologically required regime without extreme field multiplicities or hierarchical parameters.

## I. INTRODUCTION

The origin of hierarchical scales in nature, from the electroweak scale to the sub-eV masses of neutrinos, remains a central and unresolved puzzle in particle physics. A particularly powerful class of Beyond the Standard Model (BSM) theories addresses this by geometrizing the hierarchy. In these 'theory-space' models-including clockwork constructions and dimensional deconstruction-small effective couplings arise not from parameters inserted by hand, but dynamically from the localization of zero modes (massless fermionic states) across the sites of a discretized extra dimension [1-6]. The spatial profile of the zero mode directly determines the resulting hierarchical suppression. In addition to geometric setups, localization may also arise from randomness in the underlying parameters, leading to Andersonlike hierarchies [7-9].

Despite their success, standard theory-space constructions often possess a rigid structure. In many commonly studied models with nearest-neighbor interactions and simple boundary conditions, the leftand right-chiral zero-mode profiles are shaped by the same underlying Hamiltonian [2, 10-15]. As a result, the two chiralities are typically correlated, and reshaping them independently within a symmetric theory space Hamiltonian requires additional structure in conventional constructions. Independent chiral localization is a well-established feature of extra-dimensional models, here we emphasize that a similar independence can also be realized directly at the level of the theory space mass matrix through separable transformations. Moreover, in frameworks where light masses arise from fine-cancellation (GIM-like cancellation) between quasi-degenerate heavy states rather than from zero-mode localization, the accessible mass scales are often restricted by the asymptotic behaviour of the spectrum. These limitations motivate the search for a systematic method to reshape zero-mode profiles and modify spectral features while rigorously preserving the number of massless modes.

[∗ aadarshsingh@iisc.ac.in](mailto:aadarshsingh@iisc.ac.in)

In this work we propose a general framework that achieves such control through a class of index-dependent, element-wise transformations of the form

$$b _ { i j } = \frac { a _ { i j } } { g _ { f } ( i , j ) } \, .$$

These transformations may be viewed as a generalized Hadamard (Schur) scaling of the matrix entries [16], with broad relevance in areas such as network theory, image processing, and machine learning [17-19]. Our central result establishes a necessary and sufficient condition for these transformations to preserve the rank and nullity of the matrix, and hence the number of zero modes. We show that massless states are preserved if and only if the transformation function is separable,

$$g _ { f } ( i , j ) = g _ { f } ^ { ( L ) } ( i ) \, g _ { f } ^ { ( R ) } ( j ) \, .$$

The separability condition plays a crucial role: the factors g ( L ) f ( i ) and g ( R ) f ( j ) act independently on rows and columns, allowing controlled re-sculpting of the left- and right-chiral zero-mode profiles while keeping the zeromode count fixed.

This capability has significant consequences for theoryspace model building. Specific choices of g ( L ) f and g ( R ) f reproduce familiar constructions such as exponential clockwork localization, warped-extra-dimensional-like profiles, or staggered patterns, while more general choices enable smooth interpolation between them. Crucially, the independent row/column action allows the chiral profiles of a Dirac fermion to be modified separately-a feature that is difficult to realize in conventional models where the zero-mode structure is tightly constrained by the underlying Hamiltonian. In addition, these transformations offer a systematic means of modulating the massive spectrum, including the controlled introduction of near-degeneracies relevant for fine-cancellation mechanisms.

We illustrate the utility of this framework through several applications. First, we show that the standard clockwork mechanism emerges as a special case of an appropriate separable transformation. Second, we demonstrate that independent chiral zero-mode localization can be engineered even in symmetric theory-space Hamiltonians. Third, we analyze how Kaluza-Klein mass towers in deconstructed extra dimensions respond to such transformations, showing how the massive spectrum can be reshaped without altering the number of zero modes. Finally, we apply the framework to neutrino mass generation, where the transformations expand the phenomenologically viable parameter space and allow sub-eV masses to be obtained from TeV-scale physics within moderate lattice sizes, consistent with charged-lepton-flavorviolation constraints. It is important to emphasize the scope and intent of the present framework. The goal is not to engineer an arbitrary fermion mass matrix with prescribed eigenvalues and mixing matrices, which can always be achieved abstractly at the level of matrix parametrization by writing M = U † DV . Rather, we focus on identifying a restricted class of element-wise transformations that are compatible with theory-space constructions, preserve rank and nullity, and admit a clear physical interpretation in terms of site-local couplings. Within this constrained setting, the framework provides a systematic means of reshaping localization profiles and mass spectra while maintaining the underlying theoryspace structure.

We emphasise that the framework is UV agnostic by construction; it characterizes the structural class of rankpreserving element-wise deformations available within theory space models, while the specific UV origin of any particular transformation is determined by the model under consideration. In concrete realizations such transformations can arise from physical parameters, for example, in deconstructed models, the mass matrix entries are set by site-dependent vacuum expectation values of scalar link fields, and different choices of these profiles lead to corresponding rescalings of matrix elements. Similarly, in extra-dimensional constructions, fermion masses arise from overlap integrals of left and right chiral wavefunctions, where the profiles of the two chiralities enter independently.

The remainder of this paper is organized as follows. Section II develops the theoretical framework for rankpreserving transformations, including proof sketches and physical interpretation, with complete mathematical details provided in the Appendix A. Section III presents applications to theory-space models: generalized clockwork constructions, independent chiral zero-mode engineering, controlled deformation of Kaluza-Klein spectra, and a worked example in neutrino mass generation. Section IV summarizes our results and discusses potential extensions.

## II. RANK-PRESERVING SEPARABLE TRANSFORMATIONS OF MASS MATRICES

Theory-space constructions encode fermion masses in matrix structures whose null spaces correspond to massless modes in the four-dimensional effective theory. The localization profiles of these zero modes determine the resulting hierarchies in couplings and masses. In this section we introduce a class of index-dependent, elementwise transformations that preserve the number of zero modes while reshaping their profiles. This capability is the key to engineering controlled chiral structures in BSM model building.

## A. Definition of the Transformation

Consider a fermion mass matrix A of dimension m × n arising from a theory-space construction. We define an index-dependent element-wise transformation producing a new matrix B with entries

$$b _ { i j } = \frac { a _ { i j } } { g _ { f } ( i , j ) } \, ,$$

where g f ( i, j ) is a nonvanishing function acting on the row and column indices. The label f ∈ F parameterizes a family of such transformations, with g f : N × N → F taking values in a field such as R or C .

This operation may be viewed as a generalized Hadamard (Schur) scaling of the matrix entries [16]. However, unlike a uniform rescaling, it can in general alter the rank of A . Since massless fermions correspond to zero modes of the mass matrix, our interest lies in identifying the conditions under which the rank and nullity are preserved.

## B. Rank and Nullity Preservation: The Separability Condition

The central structural property that governs rank preservation is the separability of the transformation function. We state the main result here and provide the detailed proof in Appendix A.

Main Result (Separability Condition). The transformation b ij = a ij /g f ( i, j ) preserves the rank and nullity of A if and only if g f ( i, j ) is separable,

$$g _ { f } ( i , j ) = g _ { f } ^ { ( L ) } ( i ) \, g _ { f } ^ { ( R ) } ( j ) \, .$$

To understand the origin of this condition, consider a row v i 0 of A that is linearly dependent on the remaining rows,

̸

$$v _ { i _ { 0 } } = \sum _ { j \neq i _ { 0 } } \alpha _ { j } v _ { j } \, .$$

Examining the k th component before and after the transformation leads to the requirement

$$\frac { g _ { f } ( j , k ) } { g _ { f } ( i _ { 0 } , k ) } = G _ { f } ( j ) \, ,$$

where G f ( j ) is independent of the column index k . This condition is equivalent to the functional separability of g f [20]. If not separable, the transformation generally modifies the number of linear dependencies among rows or columns, altering the rank. Conversely, separability ensures a one-to-one correspondence between null vectors of A and B , guaranteeing identical rank and nullity. A complete derivation is provided in Appendix A.

## C. Transformation of Zero-Mode Profiles

We now determine how the zero modes themselves transform under a separable scaling. This result is crucial for understanding how localization profiles can be engineered without affecting the existence of massless fermions.

Zero-Mode Transformation. Let { v 1 , . . . , v n } be a basis for the null space of A . Under a separable transformation g f ( i, j ) = g ( L ) f ( i ) g ( R ) f ( j ) , the corresponding null space of B is spanned by vectors v ′ i whose components are

$$( v ^ { \prime i } ) _ { j } = ( v ^ { i } ) _ { j } \, g _ { f } ^ { ( R ) } ( j ) \, .$$

This follows from substituting a lj = b lj g ( L ) f ( l ) g ( R ) f ( j ) into the condition Av i = 0, yielding

$$\sum _ { j } b _ { l j } \left ( v _ { j } ^ { i } g _ { f } ^ { ( R ) } ( j ) \right ) = 0 \, , \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \$$

which shows that v ′ i j = v i j g ( R ) f ( j ) spans the null space of B . The column-dependent factor g ( R ) f ( j ) therefore directly modifies the spatial profile of the right-chiral zero mode, while the row-dependent factor g ( L ) f ( i ) analogously controls the left-chiral profile (as relevant for Dirac fermions). This independent row/column action enables controlled reshaping of the two chiral sectors while preserving the zero-mode count.

Eigenvalue Preservation. For completeness, we note that if A is diagonalizable with eigenvalues { µ i } , then B shares the same eigenvalues provided the separable function satisfies

$$g _ { f } ^ { ( L ) } ( k ) \, g _ { f } ^ { ( R ) } ( k ) = 1 \quad \forall \, k .$$

This additional constraint ensures that diagonal entries transform trivially. The proof is given in Appendix A.2.2. Although eigenvalue preservation is not required for our later applications, we include it as it clarifies the broader mathematical structure of the transformation.

Having established the rank-preserving nature of separable transformations and their action on zero-mode profiles, we now turn to explicit applications within the context of theory-space models.

## III. APPLICATIONS TO THEORY SPACE MODELS

In this section we illustrate how rank-preserving separable transformations may be used as a practical tool for engineering fermion mass structures in theory-space models. Since the transformations preserve the number of zero modes while reshaping their localization profiles, they enable controlled manipulation of both the chiral structure and the massive spectrum. We present several representative applications. Section III A shows that the standard clockwork construction arises as a special case of an appropriate separable function, while more general choices lead to qualitatively different localization patterns. Section III B demonstrates how the independent row/column action of the transformation allows one to separate the left- and right-chiral zero-mode profiles. In Section III C we examine the impact on Kaluza-Klein spectra in dimensional deconstruction. Finally, in Section III D we apply the framework to neutrino mass generation as a concrete phenomenological example.

## A. Generalizing the Clockwork Mechanism

The clockwork mechanism provides a particularly elegant realization of large hierarchies from O (1) parameters by generating exponentially suppressed effective couplings through zero-mode localization in a discretized extra dimension or theory space [1, 3]. In its standard form, a nearest-neighbor structure produces a single massless mode whose wavefunction is exponentially localized toward one end of the 'gear chain,' thereby inducing hierarchical interactions with fields located on specific sites [21]. This structure is usually introduced at the level of the Lagrangian via site-dependent couplings or background parameters.

Our framework reproduces the clockwork construction as a special case of a rank-preserving separable transformation and simultaneously provides a method for exploring a broader space of localization profiles. To illustrate this, consider the generalized clockwork Hamiltonian with site-dependent masses m i and nearest-neighbor couplings q i [22],

$$\mathcal { H } _ { i , j } ^ { c w } = m _ { i } \, \delta _ { i , j } + m _ { i } q _ { i } \, \delta _ { i + 1 , j } .$$

This follows from the Lagrangian

$$\text { our } \quad \mathcal { L } _ { \text {NP} } = \mathcal { L } _ { \text {kin} } - \sum _ { i = 1 } ^ { n } m _ { i } \overline { L _ { i } } R _ { i } - \sum _ { i = 1 } ^ { n } m _ { i } q _ { i } \, \overline { L _ { i } } R _ { i + 1 } + h . c . \, \left ( 1 1 \right )$$

To isolate the role of the separable transformation, we first consider the uniform reference case with m i = m and q i = 1. The corresponding Dirac mass matrix in the basis { L i , R j } is

$$M _ { C W } = m \begin{pmatrix} 1 & 1 & 0 & \cdots & 0 \\ 0 & 1 & 1 & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 1 & 1 \end{pmatrix} _ { n \times ( n + 1 ) } .$$

This starting point is useful because its zero mode is delocalized. Its components satisfy ( ξ 0 ) j ∝ ( -1) j -1 , so the magnitude of the wavefunction is uniform across the chain, and no hierarchy is generated in this basis.

We now apply the separable transformation

$$b _ { i j } = \frac { a _ { i j } } { g _ { q } ( i , j ) } , \quad g _ { q } ( i , j ) = q ^ { i - j } . \quad ( 1 3 )$$

This function can be written as g q ( i, j ) = g ( L ) q ( i ) g ( R ) q ( j ) with g ( L ) q ( i ) = q i and g ( R ) q ( j ) = q -j . By Corollary A.2.1, the transformed zero-mode components are obtained by multiplying the original components by g ( R ) q ( j ), giving

$$\xi _ { 0 } ^ { \prime } \, \infty \, \{ ( - q ) ^ { - 1 } , \, ( - q ) ^ { - 2 } , \dots , \, ( - q ) ^ { - ( n + 1 ) } \} , \quad \text {corre}$$

up to an overall normalization. This is the standard exponentially localized clockwork profile.

The transformed Hamiltonian is

$$\mathcal { H } _ { i , j } ^ { c w ^ { \prime } } = \frac { \mathcal { H } _ { i , j } ^ { c w } } { q ^ { i - j } } = \mathcal { H } _ { i , j } ^ { c w } \, q ^ { j - i } . \quad \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \$$

For the nonzero entries of Eq. (12), this gives diagonal entries proportional to m and nearest-neighbour entries proportional to mq . Thus, the separable transformation generates the canonical clockwork coupling pattern starting from the delocalized q i = 1 reference matrix. Thus, the q i = 1 matrix provides a delocalized reference configuration, and the separable transformation maps it to the usual clockwork form with localized zero mode.

The framework also highlights that exponential localization is not unique. Any separable transformation g q ( i, j ) = g ( L ) q ( i ) g ( R ) q ( j ) preserves the zero-mode structure while modifying its profile. As an illustrative example, consider

$$\bar { g } _ { q } ( i , j ) = q ^ { ( - 1 ) ^ { j } \, j } , & & \quad ( 1 6 ) & & \stackrel { \text {sam} } { \ n i }$$

which depends only on the column index and therefore automatically satisfies the rank-preserving criterion. The corresponding zero-mode profile becomes

$$( \xi _ { 0 } ^ { \prime \prime } ) _ { k } = ( - 1 ) ^ { k } \, q ^ { n + 1 - ( - 1 ) ^ { k } } , \quad k = 1 , \dots , n + 1 . \ ( 1 7 )$$

This produces a 'staggered' localization pattern with alternating signs and site-dependent exponential behaviour. Both the standard and staggered profiles exhibit strong localization, as is evident directly from the transformed zero-mode expressions, although the functional forms governing the localization differ qualitatively. This demonstrates that rank-preserving separable transformations provide a systematic method for generating qualitatively new localization patterns while retaining the massless sector.

The method generalizes straightforwardly to non-local or random clockwork constructions [8, 9, 23, 24], where such transformations can either induce localization or enhance it. More broadly, separable transformations furnish a unified perspective on a wide class of theory-space models, connecting disparate constructions through a single mathematical framework and making explicit the structural conditions underlying the emergence of hierarchies.

## B. Independent Control of Chiral Zero-Modes

A characteristic feature of many theory-space constructions with symmetric Hamiltonians is that the leftand right-chiral zero-mode profiles are tightly correlated. For a Dirac mass matrix M D , the right-chiral zero modes correspond to the null space of M D , while the left-chiral zero modes are determined by the null space of M † D . In such setups these two profiles coincide up to complex conjugation, leaving little freedom to engineer chiral asymmetries directly at the level of the theory-space mass matrix. We note that independent chiral localization is a standard feature of extra-dimensional constructions-arising, for example, from orbifold boundary conditions, bulk mass terms, or split-fermion arrangements as mentioned in introduction. The purpose of this section is to show that a similar independence of the two chiral profiles can also be achieved within the theoryspace framework through separable transformations.

The separable transformations introduced in Sec. II provide a systematic method to overcome this limitation. As shown in Corollary A.2.1, a transformation of the form g f ( i, j ) = g ( L ) f ( i ) g ( R ) f ( j ) rescales the right-chiral zero modes by the column function g ( R ) f ( j ), while the leftchiral zero modes-being null vectors of M † D -are instead rescaled by the row function g ( L ) f ( i ). Thus, the two chiralities respond to different functional components of the same transformation. Provided g ( L ) f and g ( R ) f are nonvanishing, they may be chosen independently, enabling controlled and finite reshaping of both chiral sectors while preserving the number of zero modes.

To illustrate this capability, consider the symmetric tridiagonal Hamiltonian [25]

$$\mathcal { H } _ { i , j } = m \left ( \delta _ { i , j } + \delta _ { i + 1 , j } + \delta _ { i - 1 , j } \right ) .$$

For lattice sizes satisfying n ≡ 2 (mod 3), this matrix contains a single zero mode whose components follow the repeating pattern

$$\xi _ { 0 } ^ { k } = \begin{cases} - 1 , & k \bmod 3 = 1 , \\ & 1 , & k \bmod 3 = 2 , \\ & 0 , & k \bmod 3 = 0 . \end{cases}$$

Since the Hamiltonian is symmetric, the left- and rightchiral zero modes share the same delocalized structure, ξ ⃗ 0 ,L = ξ ⃗ 0 ,R ∝ { ξ 1 0 , . . . , ξ n 0 } . This represents a typical situation in which symmetric theory-space models offer no freedom to reshape the two chiral sectors independently.

We now apply the separable transformation

$$g _ { a } ( i , j ) = \sin ( 2 a \, i ) \, a ^ { ( - 1 ) ^ { j } j } , \quad \ \ ( 1 9 ) \quad \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \$$

yielding the transformed Hamiltonian

$$\mathcal { H } _ { i , j } ^ { \prime } = \mathcal { H } _ { i , j } \, \sin ( 2 a \, i ) \, a ^ { ( - 1 ) ^ { j } j } . \quad \quad ( 2 0 ) \quad \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \$$

The row factor sin(2 ai ) modifies the left-chiral zeromode profile, while the column factor a ( -1) j j independently modifies the right-chiral profile. The two chiralities now exhibit entirely distinct localization patterns: The right-chiral mode acquires a staggered, exponentially varying profile set by the column-dependent transformation, while the left-chiral mode exhibits an oscillatory behaviour governed by the row-dependent sinusoidal factor.

The explicit form of the transformed right-chiral zero mode follows directly from Corollary A.2.1,

$$\xi _ { 0 , R } ^ { \prime k } = \xi _ { 0 } ^ { k } \, a ^ { ( - 1 ) ^ { k } k } , & & ( 2 1 ) ^ { \ m a t h s c r { G } }$$

while the left-chiral zero mode is given, up to normalization, by

$$\xi _ { 0 , L } ^ { \prime k } = \xi _ { 0 } ^ { k } \, \sin ( 2 a \, k ) .$$

These expressions illustrate the general principle: separable transformations act independently on rows and columns, and therefore allow the two chiral sectors to be engineered separately. The particular functions chosen above are for demonstration purposes only; any nonvanishing choice of g ( L ) f ( i ) and g ( R ) f ( j ) produces a new pair of left- and right-chiral profiles while preserving the existence of the massless mode.

For completeness, explicit closed-form expressions for the transformed zero-mode components for different lattice sizes (including the cases n = 2 + 6( h -1) and n = 2 + 3(2 h -1)) are provided in Appendix A 4. These formulas illustrate how the general scaling rule of Corollary A.2.1 manifests in specific realizations, and highlight the variety of chiral structures that can be engineered within this framework without altering the number of zero modes.

Although constructed as a simple example, this mechanism has broad applicability. In flavor model building, composite Higgs frameworks, and seesaw-type scenarios [4, 26-28], it is often advantageous to localize different chiralities in different regions of theory space. Separable transformations provide a systematic and modelindependent method to achieve such structures starting from otherwise rigid Hamiltonians, thereby significantly expanding the space of realizable chiral configurations in theory-space models.

## C. Engineering the Kaluza-Klein Mass Spectrum

Beyond controlling zero modes, separable transformations provide a handle on the entire tower of massive Kaluza-Klein (KK) states. Although the transformation preserves the number of massless modes, it generically reshapes the spectrum of massive states. Even in cases where the eigenvalues of the mass matrix are held fixed by the condition of Corollary A.2.2, the physical KK masses-corresponding to singular values-can change. This distinction enables controlled deformation of the massive spectrum without altering the zero-mode content.

To set the stage, recall the correspondence between a five-dimensional fermion theory and its deconstructed four-dimensional counterpart. A 5D fermion with Lagrangian [29]

$$\mathcal { L } _ { 5 } ( x ^ { \mu } , x ^ { 5 } ) = \bar { \Psi } ( i \gamma ^ { \mu } D _ { \mu } - \gamma ^ { 5 } D _ { 5 } ) \Psi - \frac { 1 } { 4 } \text {Tr} ( F _ { M N } F ^ { M N } ) , \\ \intertext { z e r o } \mathcal { L } _ { 5 } ( x ^ { \mu } , x ^ { 5 } ) = \bar { \Psi } ( i \gamma ^ { \mu } D _ { \mu } - \gamma ^ { 5 } D _ { 5 } ) \Psi - \frac { 1 } { 4 } \text {Tr} ( F _ { M N } F ^ { M N } ) ,$$

compactified on an interval, yields a KK tower with masses m k ∝ k determined by boundary conditions. Deconstruction replaces the 5D continuum with a lattice of N gauge groups and fermions Ψ k at sites with link fields connecting nearest neighbors [30-32]. The linkfield vacuum expectation values generate a Dirac-type mass matrix whose spectrum reproduces the KK tower in the largeN limit. For uniform couplings of strength M f , one obtains the well-known spectrum [33]

$$\sum _ { \tan ^ { - } } \quad m _ { k } = 2 M _ { f } \sin \left ( \frac { k \pi } { 2 N } \right ) , \quad k = 1 , 2 , \dots , N - 1 , \quad ( 2 4 )$$

which reduces to an approximately linear spectrum for k ≪ N ,

$$\stackrel { l a t \sim } { \text {and} } \quad m _ { k } \approx M _ { f } \, \frac { k \pi } { N } , \quad \Delta m _ { k } \equiv m _ { k + 1 } - m _ { k } \approx M _ { f } \, \frac { \pi } { N } .$$

Separable transformations modify this spectrum by effectively rescaling the link-field VEVs and site-dependent masses. While a closed-form solution for a fully arbitrary transformation is generally unavailable, useful intuition can be gained from specific cases that are analytically tractable [5]. Consider a transformation that uniformly rescales the diagonal and off-diagonal elements,

$$g _ { f } ( i , i ) = g _ { f } , \quad g _ { f } ( i + 1 , i ) = \tilde { g } _ { f } ,$$

leading to the transformed mass matrix

$$M ^ { \prime } = M _ { f } \left ( \begin{array} { c c c c c c c c } g _ { f } & 0 & 0 & \cdots & 0 \\ - \tilde { g } _ { f } & g _ { f } & 0 & \cdots & 0 \\ 0 & - \tilde { g } _ { f } & g _ { f } & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & \cdots & g _ { f } \\ 0 & 0 & 0 & \cdots & - \tilde { g } _ { f } \end{array} \right ) .$$

This form may be interpreted as a separable transformation g f ( i, j ) = (˜ g f /g f ) i -j combined with an overall premultiplication by g f . Although the eigenvalues are preserved when the condition of Corollary A.2.2 holds, the physical KK masses are set by the singular values of M ′ . Computing the mass-squared matrix,

$$M ^ { \prime } \colon & \text {Computing the mass-squared matrix} , & \text {decons} & & \text {decons} , \\ & \quad \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \$$

one finds the exact eigenvalues

$$m _ { k } ^ { \prime 2 } = M _ { f } ^ { 2 } \left ( g _ { f } ^ { 2 } + g _ { f } ^ { \prime 2 } - 2 g _ { f } \tilde { g } _ { f } \cos \frac { k \pi } { N + 1 } \right ) , \quad k = 1 , \dots , N \text {.} \ \text {construct} \\ S o u n s l e f o t u m e s \ f o w h e l l \ \text {in the low} \ k \ \text {lange} \ N \ \text {liit} \quad \ \ \ \text {ertheless} ,$$

Several features follow. In the lowk , largeN limit,

$$m _ { k } ^ { \prime } \approx M _ { f } | g _ { f } - \tilde { g } _ { f } | + M _ { f } \frac { g _ { f } \tilde { g } _ { f } } { | g _ { f } - \tilde { g } _ { f } | } \frac { k ^ { 2 } \pi ^ { 2 } } { 2 N ^ { 2 } } , \quad ( 3 0 ) \quad \text {sees} \quad \\$$

$$\Delta m _ { k } ^ { \prime } \approx M _ { f } \frac { g _ { f } \tilde { g } _ { f } } { | g _ { f } - \tilde { g } _ { f } | } \frac { ( 2 k + 1 ) \pi ^ { 2 } } { 2 N ^ { 2 } } . \quad \ \ ( 3 1 ) \quad \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \$$

Thus, the transformation introduces:

- a uniform offset M f | g f -˜ g f | to all KK masses, and
- a nonuniform deformation of the level spacings, making low-lying states relatively denser.

Figure 1 illustrates a more general example obtained from the transformation g f ( i, j ) = ( -1) i -j sin(2fi). Unlike uniform rescaling, the row dependence introduces site-specific modulations that propagate through the KK spectrum. The resulting masses cluster into regions of near-degeneracy, a feature frequently exploited in fine-cancellation mechanisms for neutrino physics and other phenomenological applications [23]. We emphasise that while zero-mode localization depends exclusively on g ( R ) f ( j ) (right-chiral modes) or g ( L ) f ( i ) (left-chiral modes), the massive sector is sensitive to the combined structure of the full transformation function.

## D. Application to Neutrino Mass Generation via Fine Cancellation

We now apply the transformation framework to neutrino mass generation in theory-space models. In con- trast to clockwork constructions, which generate hierarchies via zero-mode localization, nearest-neighbor deconstruction models with aliphatic structure typically possess no zero mode in the Dirac mass matrix. Nevertheless, such models can yield small neutrino masses through a fine-cancellation mechanism [23], where neardegenerate heavy states interfere destructively in the seesaw-like sum that determines the effective light mass. We show that separable transformations can enhance this cancellation by increasing the level of near-degeneracy in the heavy spectrum, thereby enabling lighter neutrino masses with a smaller number of sites.

FIG. 1. Modification of the Kaluza-Klein spectrum in a deconstructed setup. The orange curve corresponds to the original spectrum of Eq. (24), while the green curve shows the spectrum obtained from the transformed mass matrix M ′ with g f ( i, j ) = ( -1) i -j sin(2fi) (with N = 50 and f = 1). The transformation induces regions of controlled near-degeneracy while preserving the number of zero modes.

<!-- image -->

The Lagrangian for the nearest-neighbor theory-space model with n sites is [25]

$$\mathcal { L } _ { T S } = \mathcal { L } _ { k i n } - \sum _ { i , j = 1 } ^ { n } \bar { L } _ { i } \mathcal { H } _ { i j } R _ { j } ,$$

where H ij is the symmetric tridiagonal matrix introduced in Eq. (18). To couple the Standard Model neutrinos to the heavy fermions, we introduce boundary interactions,

$$\mathcal { L } _ { i n t } = \frac { y _ { 1 } v } { \sqrt { 2 } } \, \bar { \nu } _ { L } R _ { n } + \frac { y _ { 2 } v } { \sqrt { 2 } } \, \bar { \nu } _ { R } L _ { 1 } + h . c . ,$$

where v ≃ 246 GeV and ⟨ H ⟩ = v/ √ 2. Integrating out the heavy states at the tree level gives the light-neutrino mass

$$m _ { \nu } = \frac { y _ { 1 } y _ { 2 } v ^ { 2 } } { 2 } \sum _ { i = 1 } ^ { n } \frac { ( u _ { L } ) _ { 1 } ^ { i } ( u _ { R } ) _ { n } ^ { i } } { m _ { i } } \, .$$

where m i are the heavy singular values, and ( u L/R ) i denote the projections of the boundary fields onto the i th mass eigenstate. When the heavy spectrum becomes nearly degenerate, the sum contains significant cancellations due to alternating phases and orthogonality, yielding a naturally suppressed effective mass even when all underlying parameters are O (1). The achievable suppression is governed by the degree of near-degeneracy in the KK-like spectrum.

For the untransformed tridiagonal Hamiltonian, increasing degeneracy requires a large number of sites. As shown in [23], masses at the MeV scale can be obtained from TeV-scale parameters with N ∼ O (10 3 ), but further suppression becomes increasingly less efficient.

A separable transformation can modify this behaviour. As a concrete example, we consider the separable transformation

$$g _ { f } ( i , j ) = \sin ( 2 f ) \, ^ { i - j } ,$$

̸

which can be written in the separable form g f ( i, j ) = g ( L ) f ( i ) g ( R ) f ( j ) with g ( L ) f ( i ) = sin(2 f ) i and g ( R ) f ( j ) = sin(2 f ) -j (for sin(2 f ) = 0). This yields the transformed Hamiltonian

$$\mathcal { H } _ { i j } ^ { \prime } = \sin ( 2 f ) ^ { i - j } \, \mathcal { H } _ { i j } .$$

̸

By construction, the transformation preserves the rank and nullity structure of the mass matrix, while inducing a nontrivial modulation of the heavy spectrum. For definiteness, we fix f = 1 . 3 in the numerical examples shown below; this choice is representative, and qualitatively similar behaviour is obtained for generic values of f satisfying | sin(2 f ) | = 0 , 1. This modulation alters level spacings and can significantly strengthen neardegeneracy across portions of the spectrum.

Figure 2 compares the scales reached in the untransformed and transformed cases as a function of the number of sites N . The untransformed model reproduces earlier results: MeV-scale masses can be reached with N ∼ 10 3 for TeV new physics, but additional suppression becomes progressively inefficient. In contrast, the transformed Hamiltonian achieves comparable suppression for N ∼ 13, and continues to produce substantially smaller effective masses as N increases. For N ≈ 3040, the cancellation yields values near 0 . 1 eV, consistent with the observed neutrino mass scale. The oscillatory pattern in Fig. 2 results from the periodic structure of the sine function.

a. Sensitivity to perturbations. A common concern in mechanisms that generate light masses through cancellations among heavy modes is the sensitivity of the result to perturbations of the underlying mass matrix. Since exact degeneracies would typically require symmetry protection, it is important to verify that the enhanced cancellation enabled by the transformed Hamiltonian does not hinge on finely tuned matrix entries.

To assess this, we perturb the transformed Hamiltonian according to

$$\mathcal { H } ^ { \prime } \to \mathcal { H } ^ { \prime } + \delta \mathcal { H } , \quad ( \delta \mathcal { H } ) _ { i j } = \epsilon _ { i j } \, \mathcal { H } ^ { \prime } _ { i j } , \quad ( 3 7 ) \quad \text {ber of}$$

where the ϵ ij are independent random variables uniformly sampled in the range [ -δ, δ ], with δ parametrizing the magnitude of the perturbation. This corresponds to independent multiplicative perturbations of each nonzero matrix element, without enforcing any structural correlations beyond those already present in H ′ . For each value of δ , the effective neutrino mass m ν is computed via exact numerical diagonalization of the perturbed matrix, and the resulting distribution is characterized by its median and inter-quantile range over many realizations.

FIG. 2. Achievable light-neutrino mass scale as a function of the number of theory-space sites N . Orange points correspond to the untransformed Hamiltonian H ij , which reaches MeV-scale suppression only for N ∼ 10 3 and exhibits diminishing improvement at larger N . Green points show the transformed Hamiltonian H ′ ij = sin(2 f ) i -j H ij with f = 1 . 3. In the transformed model, the phenomenologically relevant subeV regime is reached for N ∼ 30-40.

<!-- image -->

We find that, under percent-level perturbations of the transformed mass matrix, the resulting light-neutrino mass can exhibit O (1) fractional variations in regions where the cancellation is exceptionally strong and the median approaches zero. This behaviour is expected for a mechanism based on near-degeneracy and destructive interference among heavy states. Crucially, however, across the entire ensemble the generated masses remain concentrated in the same parametric regime: for N ∼ 30-40, the distribution consistently lies in the phenomenologically relevant sub-eV range, up to O (1) factors.

This demonstrates that the transformation robustly accesses the hierarchical regime without requiring delicate tuning of individual matrix elements. While the precise numerical value of m ν is sensitive to the strength of the cancellation, the order-of-magnitude suppression relative to the TeV-scale input is stable under moderate perturbations. The hierarchy therefore reflects a collective spectral property of the transformed theory-space construction rather than an artifact of finely adjusted couplings.

These results demonstrate that separable transformations provide a controlled method for adjusting the level spacing of the heavy spectrum without altering the number of zero modes. In phenomenological applications such as neutrino mass generation, where cancellations among heavy states play a central role, this added freedom enlarges the accessible parameter space and allows realistic neutrino masses to be obtained with moderate lattice sizes and without introducing extremely small input parameters.

## E. Phenomenological Constraints

The boundary interactions in Eq. (33) that generate a light neutrino mass also induce mixings between the Standard Model leptons and the heavy theory-space states. These mixings lead to several phenomenological signatures. Direct production of heavy neutral leptons at hadron colliders or future lepton colliders can manifest as missing energy or displaced vertices, depending on the mass spectrum and decay widths [34-36]. In addition, mixing with the heavy states modifies electroweak precision observables through loop corrections to the oblique parameters [37]. Although the fine-cancellation mechanism does not intrinsically require the new states to lie at the TeV scale, taking them significantly below this scale with O (1) couplings is strongly constrained by existing collider data. We therefore consider masses in the multiTeV range as a representative and conservative regime.

A more stringent probe arises from charged-lepton flavor violation (CLFV), especially the decay µ → eγ , which provides one of the strongest constraints on neutrino mixing with heavy fermionic states [38]. In the presence of heavy neutral leptons, the charged current becomes

$$\mathcal { L } _ { C C } = g W _ { \mu } ^ { - } J _ { W } ^ { \mu + } + h . c . , \quad \ \ ( 3 8 ) \quad \ \ \max _ { \real \ s h a r { } }$$

with

$$J _ { W } ^ { \mu + } = \sum _ { \alpha = e , \mu , \tau } \sum _ { j = 1 } ^ { n + 1 } \frac { ( U _ { L \alpha } ) ^ { j } } { \sqrt { 2 } } \, \bar { e } _ { \alpha } \gamma ^ { \mu } P _ { L } \nu _ { j , \alpha } , \quad ( 3 9 ) \quad \text {tion} \\ \quad \stackrel { ( 3 9 ) } { \alpha } \sum _ { \alpha = e , \mu , \tau } \sum _ { j = 1 } ^ { n + 1 } \frac { ( U _ { L \alpha } ) ^ { j } } { \sqrt { 2 } } \, \bar { e } _ { \alpha } \gamma ^ { \mu } P _ { L } \nu _ { j , \alpha } , \quad ( 3 9 ) \\$$

where ( U Lα ) j denotes the mixing of the SM flavor α with the j th mass eigenstate. These mixings enter the oneloop amplitude for µ → eγ , yielding [39, 40]

$$B R ( \mu \rightarrow e \gamma ) & = \frac { 3 \alpha } { 8 \pi } \left | \mathcal { A } \right | ^ { 2 } , & & ( 4 0 ) & & \text {severa} \\ \mathcal { A } = & \sum _ { \alpha = 1 } ^ { 3 } \sum _ { j = 1 } ^ { N + 1 } V _ { \mu \alpha } V _ { e \alpha } ^ { * } | ( U _ { L \alpha } ) ^ { j } | ^ { 2 } \, F \left ( \frac { m _ { j , \alpha } ^ { 2 } } { m _ { W } ^ { 2 } } \right ) , & & \text {propr} \\ & , & & \text {choice} \\ & , & & \text {pattern} \\ & , & & \text {of the theorem}$$

where V αβ is the PMNS matrix and

$$F ( x ) & = \frac { 1 } { 6 ( 1 - x ) ^ { 4 } } \left [ 1 0 - 4 3 x + 7 8 x ^ { 2 } - 4 9 x ^ { 3 } + 4 x ^ { 4 } + 1 8 x ^ { 3 } \ln x \right ] . \quad \text {tion} . \\ & = \frac { ( 4 ) } { 6 ( 1 - x ) ^ { 4 } } \left [ 1 0 - 4 3 x + 7 8 x ^ { 2 } - 4 9 x ^ { 3 } + 4 x ^ { 4 } + 1 8 x ^ { 3 } \ln x \right ] . \\$$

The MEG bound BR( µ → eγ ) &lt; 4 . 2 × 10 -13 [41] implies that, for O (1) Yukawa couplings, the heavy neutrino masses must typically satisfy m j ≳ O (10) TeV [22]. Within our framework, achieving m j ≳ 10 TeV is compatible with the parameter choices used in Sec. III D. For N ∼ 30-40 sites, the transformed Hamiltonian can simultaneously satisfy:

- heavy neutrino masses in the multi-TeV regime (consistent with CLFV bounds),
- light neutrino masses of order 0 . 1 eV (consistent with oscillation data),
- and O (1) values for the boundary Yukawa couplings.

This illustrates that the transformation enlarges the region of viable parameter space compared with untransformed constructions, which typically require either substantially larger N or a hierarchy between diagonal and off-diagonal mass terms.

Future experiments will continue to probe this parameter space. Heavy fermions in the multi-TeV range remain within the prospective reach of next-generation facilities such as the FCC and other proposed multi-TeV colliders [37, 42, 43]. Upcoming upgrades to CLFV searches, such as MEG II, aim to improve sensitivity to BR( µ → eγ ) down to ∼ 10 -14 [44, 45], which will place even tighter constraints on scenarios with sizable mixing between light and heavy neutrino states.

## IV. CONCLUSION

In this work, we have presented a general framework for constructing fermion mass hierarchies in theory-space models through index-dependent, element-wise transformations that preserve the number of zero modes while reshaping their localization profiles. The central theoretical result identifies a necessary and sufficient condition for rank and nullity preservation: the transformation function must be separable, g f ( i, j ) = g ( L ) f ( i ) g ( R ) f ( j ). This separability enables controlled and independent manipulation of the left- and right-chiral zero-mode wavefunctions, a feature that is not straightforward to realize in conventional constructions where both chiralities are governed by the same mass matrix structure.

We demonstrated the utility of this framework through several representative applications. First, the standard clockwork mechanism follows as a special case of an appropriate separable transformation, and more general choices of g f naturally generate alternative localization patterns. Second, we showed that independent control of the two chiral sectors can be achieved starting from a symmetric Hamiltonian, illustrating how nontrivial chiral structures can emerge from a simple initial configuration. Third, we analyzed the impact of such transformations on the massive Kaluza-Klein spectrum in deconstructed setups, showing how level spacings can be systematically reshaped and regions of near-degeneracy introduced. Finally, we applied the framework to neutrino mass generation via fine-cancellation, finding that suitable transformations can enhance spectral compression and enable light-neutrino masses consistent with oscillation data using moderate lattice sizes and O (1) couplings. The resulting scenarios can satisfy current charged-lepton flavor-violation limits while remaining testable at future high-intensity and high-energy experiments.

These results establish separable rank-preserving transformations as a versatile tool for model building in theory space. Several natural extensions merit further investigation. The framework is not intended as a method for arbitrary mass-matrix construction, but as a controlled tool for exploring physically motivated deformations within theory-space models.

On the phenomenological side, constructing threegeneration flavor models within this framework and exploring predictive texture structures would be of particular interest. The present framework does not by itself predict flavor mixing angles, since such predictions require an explicit multi-generation construction and specified boundary couplings. Nevertheless, separable transformations act on a Dirac mass matrix as

$$M \rightarrow D _ { L } ^ { - 1 } M D _ { R } ^ { - 1 } , & & \quad f o r \\ & & \quad \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \$$

where D L and D R are diagonal but generally non-unitary matrices. Such transformations can modify the singularvector structure of MM † , and therefore can affect the unitary matrices that enter the physical mixing matrix in a three-generation realization. A systematic study of flavor mixing within this framework is, therefore a natural direction for future work. A related three-generation realization of hierarchy and flavor structure was studied in Ref. [26]. On the theoretical side, a systematic classification of separable transformations and a clearer connection to continuum descriptions-such as metric engineering in warped or modulated extra-dimensional geometries-may reveal additional mechanisms for hierarchy generation. Taken together, the framework developed here provides a flexible and mathematically well-defined approach for addressing long-standing questions related to mass hierarchies, flavor structure, and naturalness in physics beyond the Standard Model.

## ACKNOWLEDGMENTS

A.S. acknowledges financial support from the Council of Scientific and Industrial Research (CSIR), Government of India, under Senior Research Fellowship No. 09/0079(15487)/2022-EMR-I. The author also gratefully acknowledges the use of open-source scientific software, including Python and associated libraries, for numerical analysis. Large Language Models (LLMs) were used solely for language polishing; all scientific content and conclusions are the author's own. All code used in this work is publicly available at: /github GitHub Profile.

## Appendix A: Mathematical Framework: Complete Proofs

This appendix provides formal proofs of the results stated in Sec. II. Although our primary applications lie in fermion mass generation within theory-space models, the underlying structure of rank-preserving element-wise transformations is more general and may prove useful in areas such as network theory, quantum walks, and condensed-matter eigenvalue problems. We therefore present the results in a theorem-proof format and adopt standard matrix-analysis notation.

## 1. Definitions and Notation

Definition A.1 (Index-dependent element-wise transformation) . Let A = [ a ij ] be an N × M matrix over a field F . An index-dependent element-wise transformation of A is a matrix B = [ b ij ] defined by

$$b _ { i j } = h _ { f } ( a _ { i j } , i , j ) ,$$

for some function h f : F × N × N → F . In this work we consider the special case

$$b _ { i j } = \frac { a _ { i j } } { g _ { f } ( i , j ) } , & & ( A 2 )$$

with g f ( i, j ) = 0 for all i, j .

̸

Notation. For a parameter f ∈ F , we denote by g f : N × N → F a family of index-dependent functions, where g f ( i, j ) acts multiplicatively on entry a ij of A . The subscript f indicates that the function may vary across a family of transformations. The more general map h f ( a ij , i, j ) is used only for completeness; all results here concern the separable case b ij = a ij /g f ( i, j ).

## 2. Theorems and Proofs

̸

Theorem A.1. Let A be an N × M matrix and let B be defined by b ij = a ij /g f ( i, j ) , with g f ( i, j ) = 0 . Then A and B have the same rank (and hence the same nullity) if g f satisfies either of the following equivalent conditions for some fixed reference indices ( k 0 , l 0 ) :

$$\underset { O V - } { \text {un} } \quad \frac { g _ { f } ( i , j ) } { g _ { f } ( k _ { 0 } , j ) } = G _ { f } ( i ) \quad o r \quad \frac { g _ { f } ( i , j ) } { g _ { f } ( i , l _ { 0 } ) } = \tilde { G } _ { f } ( j ) , \ \ ( A 3 )$$

where G f depends only on the row index and ˜ G f depends only on the column index.

Proof. Since the transformation does not change the matrix dimensions, any trivial nullity that arises when N &lt; M is automatically preserved. We therefore focus on additional linear dependencies among the rows.

Assume that the i 0 -th row of A is linearly dependent,

̸

$$v _ { i _ { 0 } } = \sum _ { j \neq i _ { 0 } } \alpha _ { j } \, v _ { j } ,$$

where v i denotes the i -th row of A . Let v ′ i denote the corresponding rows of B . Taking the k -th entry of Eq. (A4), we have

̸

$$v _ { i _ { 0 } , k } = \sum _ { j \neq i _ { 0 } } \alpha _ { j } \, v _ { j , k } .$$

Using v ′ i,k = v i,k /g f ( i, k ), this becomes

̸

$$v _ { i _ { 0 } , k } ^ { \prime } = \frac { 1 } { g _ { f } ( i _ { 0 } , k ) } \sum _ { j \neq i _ { 0 } } \alpha _ { j } \, v _ { j , k } ^ { \prime } \, g _ { f } ( j , k ) . \quad ( A 6 )$$

If the function g f satisfies

$$\frac { g _ { f } ( j , k ) } { g _ { f } ( i _ { 0 } , k ) } = G _ { f } ( j ) ,$$

with G f ( j ) depending only on the row index, then the expression above becomes

̸

$$v _ { i _ { 0 } , k } ^ { \prime } = \sum _ { j \neq i _ { 0 } } \alpha _ { j } G _ { f } ( j ) \, v _ { j , k } ^ { \prime } ,$$

̸

with coefficients α ′ j = α j G f ( j ) independent of k . Thus v ′ i 0 = ∑ j = i 0 α ′ j v ′ j , so the same row of B is linearly dependent.

The converse follows by the same argument applied to B . Hence A and B contain the same number of linearly dependent rows. Row-column rank equality [46] then implies they also have the same number of linearly dependent columns, so their nullities agree. Finally, the rank-nullity theorem gives

$$\ r a n k ( A ) = r a n k ( B ) .$$

Theorem A.2. A function g f ( x, y ) satisfies the conditions of Theorem A.1 if and only if it is separable.

Proof. Theorem 6 of Ref. [20] states that g f is separable if and only if

$$g _ { f } ( i , j ) \, g _ { f } ( x , y ) = g _ { f } ( x , j ) \, g _ { f } ( i , y ) .$$

Rearranging yields

$$\frac { g _ { f } ( x , y ) } { g _ { f } ( i , y ) } = \frac { g _ { f } ( x , j ) } { g _ { f } ( i , j ) } \quad \text {or} \quad \frac { g _ { f } ( x , y ) } { g _ { f } ( x , j ) } = \frac { g _ { f } ( i , y ) } { g _ { f } ( i , j ) } , \quad \\ \intertext { w h i o n t e s } \intertext { s u r } \intertext { p r o f } \intertext { f o r } \intertext { g r o f } \intertext { s u r } \intertext { P r o f o f } \intertext { P r o f o f } \intertext { s u r } \intertext { A 9 } \intertext { r e a d s } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext { P r o f } \intertext { s u r } \intertext {$$

which matches exactly the structural condition appearing in Theorem A.1. Choosing i and j as reference indices identifies the corresponding row-only and column-only functions G f and ˜ G f , completing the proof.

## 3. Corollaries

Corollary A.2.1. Let A be an N × M matrix with null-space basis { v 1 , . . . , v r } . If B is obtained from A via a separable transformation b ij = a ij /g f ( i, j ) with g f ( i, j ) = g ( L ) f ( i ) g ( R ) f ( j ) , then a corresponding basis for the null space of B is given by

$$( v ^ { \prime i } ) _ { j } = ( v ^ { i } ) _ { j } \, g _ { f } ^ { ( R ) } ( j ) . \quad ( A 1 0 )$$

Proof. Let v i be a null vector of A , so that

$$\sum _ { j = 1 } ^ { M } a _ { l , j } v _ { j } ^ { i } = 0 , \quad \forall l = 1 , \dots , N . \quad ( A 1 1 )$$

Using a l,j = b l,j g ( L ) f ( l ) g ( R ) f ( j ), we obtain

$$\sum _ { j = 1 } ^ { M } b _ { l , j } \, g _ { f } ^ { ( L ) } ( l ) \, g _ { f } ^ { ( R ) } ( j ) v _ { j } ^ { i } = 0 . \quad ( A 1 2 )$$

̸

Since g ( L ) f ( l ) = 0, it may be divided out:

$$\sum _ { j = 1 } ^ { M } b _ { l , j } \, g _ { f } ^ { ( R ) } ( j ) v _ { j } ^ { i } = 0 . \quad ( A 1 3 )$$

Define v ′ i j = v i j g ( R ) f ( j ). Then the above condition becomes

$$\sum _ { j = 1 } ^ { M } b _ { l , j } \, v _ { j } ^ { \prime i } = 0 ,$$

so v ′ i is a null vector of B . Since the transformation multiplies each component of each basis vector by a nonvanishing factor, the dimension of the null space is unchanged and { v ′ i } is a basis.

Corollary A.2.2. Let A be an N × N diagonalizable matrix with eigenvalues { µ i } and corresponding eigenvectors { v i } . Under the transformation b ij = a ij /g f ( i, j ) with g f ( i, j ) = g ( L ) f ( i ) g ( R ) f ( j ) , the transformed matrix B has the same eigenvalues as A and eigenvectors

$$( v ^ { \prime i } ) _ { j } = ( v ^ { i } ) _ { j } \, g _ { f } ^ { ( R ) } ( j ) , \quad ( A 1 5 )$$

if and only if

$$g _ { f } ^ { ( L ) } ( k ) g _ { f } ^ { ( R ) } ( k ) = 1 \quad \forall \, k = 1 , \dots , N . \quad ( A 1 6 )$$

Proof. Let v i satisfy Av i = µ i v i . Componentwise this reads

$$\sum _ { j = 1 } ^ { N } a _ { l , j } v _ { j } ^ { i } = \mu _ { i } v _ { l } ^ { i } .$$

Substituting a l,j = b l,j g ( L ) f ( l ) g ( R ) f ( j ) gives

$$\sum _ { j = 1 } ^ { N } b _ { l , j } g _ { f } ^ { ( L ) } ( l ) g _ { f } ^ { ( R ) } ( j ) \, v _ { j } ^ { i } - \mu _ { i } v _ { l } ^ { i } = 0 .$$

Separate the j = l term:

̸

$$\i i \text { for } \sum _ { j \neq l } b _ { l , j } g _ { f } ^ { ( L ) } ( l ) g _ { f } ^ { ( R ) } ( j ) v _ { j } ^ { i } + ( b _ { l , l } g _ { f } ^ { ( L ) } ( l ) g _ { f } ^ { ( R ) } ( l ) - \mu _ { i } ) \, v _ { l } ^ { i } = 0 . \\ ( A 1 0 )$$

If g ( L ) f ( l ) g ( R ) f ( l ) = 1 for all l , this becomes

̸

$$\sum _ { j \neq l } b _ { l , j } g _ { f } ^ { ( L ) } ( l ) g _ { f } ^ { ( R ) } ( j ) v _ { j } ^ { i } + ( b _ { l , l } - \mu _ { i } ) v _ { l } ^ { i } = 0 . \quad ( A 2 0 )$$

Multiplying by g ( R ) f ( l ) and defining v ′ i j = v i j g ( R ) f ( j ) yields

$$\sum _ { j = 1 } ^ { N } ( b _ { l , j } - \mu _ { i } \delta _ { l } ^ { j } ) v _ { j } ^ { \prime i } = 0 , \quad ( A 2 1 )$$

which is the eigenvalue equation for B with eigenvalue µ i .

For the converse, assume A and B share all eigenvalues and v ′ i j = v i j g ( R ) f ( j ) are eigenvectors of B . Tracing the steps above backward forces the diagonal condition g ( L ) f ( k ) g ( R ) f ( k ) = 1 for each k .

Corollary A.2.3. If A is diagonalizable and the separability condition of Corollary A.2.2 is satisfied, then the transformed matrix B is similar to A .

Proof. Two diagonalizable matrices are similar if and only if they share the same set of eigenvalues [47]. Corollary A.2.2 ensures that A and B are both diagonalizable and have identical eigenvalues. Hence there exists an invertible matrix P such that B = P -1 AP .

## 4. Explicit Examples of Chiral Zero-Mode Transformations

This subsection collects explicit closed-form expressions for the chiral zero-mode components appearing in Sec. III B. These formulas illustrate how the general transformation rule of Corollary A.2.1,

$$v _ { j } ^ { \prime i } = v _ { j } ^ { i } \, g _ { f } ^ { ( R ) } ( j ) ,$$

manifests in concrete theory-space Hamiltonians whose untransformed zero-mode structure exhibits a periodic pattern.

## Untransformed Zero Mode

For the symmetric tridiagonal Hamiltonian

$$\mathcal { H } _ { i , j } = m ( \delta _ { i , j } + \delta _ { i + 1 , j } + \delta _ { i - 1 , j } ) , \quad ( A 2 2 ) \quad \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \$$

and lattice sizes satisfying n ≡ 2 (mod 3), the mass matrix possesses a single zero mode with components

$$\xi _ { 0 } ^ { k } = \begin{cases} - 1 , & k \bmod 3 = 1 , \\ 1 , & k \bmod 3 = 2 , \quad k = 1 , \dots , n . \\ 0 , & k \bmod 3 = 0 , \end{cases}$$

This mod-3 structure arises from the linear dependence condition among rows.

## Right-Chiral Zero Mode Under the Transformation

Consider the separable transformation

$$g _ { a } ( i , j ) = \sin ( 2 a \, i ) \, a ^ { ( - 1 ) ^ { j } j } ,$$

used in Sec. III B. The right-chiral zero mode is rescaled by the column function g ( R ) a ( j ) = a ( -1) j j , yielding

$$\xi _ { 0 , R } ^ { \prime } k = \xi _ { 0 } ^ { k } a ^ { ( - 1 ) ^ { k } k } .$$

For clarity, the explicit forms for the two periodic cases of n that appear in Sec. III B are quoted below.

$$a . \ C a s e \ 1 \colon n = 2 + 6 ( h - 1 ) , \, h \in \mathbb { N } .$$

$$\begin{array} { r l } & { \text {enval} ^ { - } } \\ & { \text {tracing} } \\ & { \text {dition} } & { \xi _ { 0 , R } ^ { k } = \left \{ \begin{array} { l l } { - \, a ^ { n - ( - 1 ) ^ { n - k } _ { \cdot } } , } & { k \bmod 3 = 2 , } \\ { a ^ { n - ( - 1 ) ^ { n - k } _ { \cdot } } , } & { k \bmod 3 = 1 , } & { k = 1 , \dots , n . } \\ { 0 , } & { k \bmod 3 = 0 , } \end{array} } \end{array}$$

$$e \quad b . \ \ C a s e \ 2 \colon n = 2 + 3 ( 2 h - 1 ) , \, h \in \mathbb { N } .$$

$$\text {if and} \quad \xi _ { 0 , R } ^ { k } = \begin{cases} - \ a ^ { - [ n - ( - 1 ) ^ { n - k } k ] } , & k \bmod 3 = 2 , \\ \ a ^ { - [ n - ( - 1 ) ^ { n - k } k ] } , & k \bmod 3 = 1 , \quad k = 1 , \dots , n . \\ 0 , & k \bmod 3 = 0 , \end{cases}$$

These patterns differ by the effective phase assignment ( -1) n -k and the exponent sign, but both follow directly from the multiplicative scaling rule applied to the mod-3 untransformed zero mode.

## Left-Chiral Zero Mode Under the Transformation

Since left-chiral zero modes correspond to the null space of H † and thus pick up the row function g ( L ) a ( i ) = sin(2 ai ), we obtain

$$\xi _ { 0 , L } ^ { \prime } \, ^ { k } = \xi _ { 0 } ^ { k } \, \sin ( 2 a \, k ) .$$

Explicitly, for n = 2 + 3 h with h ∈ N ,

$$\text {adic} \\ \xi _ { 0 , L } = \begin{cases} - \frac { \sin ( 2 n a ) } { \sin ( 2 k a ) } , & k \bmod 3 = 2 , \\ \frac { \sin ( 2 n a ) } { \sin ( 2 k a ) } , & k \bmod 3 = 1 , \\ 0 , & k \bmod 3 = 0 , \end{cases} k = 1 , \dots , n .$$

As in the right-chiral case, the structure reflects the mod-3 periodicity of the untransformed zero mode and the multiplicative row-dependent scaling from the transformation.

These examples illustrate concretely how separable transformations reshape chiral zero-mode profiles while preserving the existence of the massless state, in agreement with Corollary A.2.1. They also show how analytically tractable patterns emerge when the underlying Hamiltonian exhibits lattice periodicities, providing explicit benchmarks for the general principles discussed in the main text.

- [1] G. F. Giudice and M. McCullough, A clockwork theory, Journal of High Energy Physics 2017 , 1 (2017).
- [2] N. Arkani-Hamed, A. G. Cohen, and H. Georgi, Electroweak symmetry breaking from dimensional deconstruction, Physics Letters B 513 , 232 (2001).
- [3] D. E. Kaplan and R. Rattazzi, Large field excursions and approximate discrete symmetries from a clockwork axion, Physical Review D 93 , 085007 (2016).
- [4] G. Cacciapaglia, H. Cai, A. Deandrea, T. Flacke, S. J. Lee, and A. Parolini, Composite scalars at the lhc: the higgs, the sextet and the octet, Journal of High Energy Physics 2015 , 1 (2015).
- [5] N. Kan, K. Shiraishi, and M. Takeuchi, Light fermion masses in partially deconstructed models, The European Physical Journal C 84 , 1041 (2024).
- [6] D. Choudhury and S. Maharana, A closed clockwork theory: Z 2 parity and more, Journal of High Energy Physics 2022 , 1 (2022).
- [7] N. Craig and D. Sutherland, Exponential hierarchies from anderson localization in theory space, Physical Review Letters 120 , 221802 (2018).
- [8] F. A. de Souza and G. von Gersdorff, A random clockwork of flavor, Journal of High Energy Physics 2020 , 1 (2020).
- [9] K. M. Patel, Hierarchies from deterministic non-locality in theory space anderson localisation, Journal of High Energy Physics 2025 , 1 (2025).
- [10] Y. Grossman and M. Neubert, Neutrino masses and mixings in non-factorizable geometry, Physics Letters B 474 , 361 (1999).
- [11] R. Contino, T. Kramer, M. Son, and R. Sundrum, Warped/composite phenomenology simplified, Journal of High Energy Physics 2007 , 074 (2007).
- [12] C. Csaki, C. Grojean, L. Pilo, and J. Terning, Fermions on an interval: Quark and lepton masses without a higgs, Physical Review Letters 92 , 101802 (2004).
- [13] S. J. Huber and Q. Shafi, Fermion masses, mixings and proton decay in a randall-sundrum model, Physics Letters B 498 , 256 (2001).
- [14] T. Gherghetta and A. Pomarol, Bulk fields and supersymmetry in a slice of ads, Nuclear Physics B 586 , 141 (2000).
- [15] R. S. Chivukula, E. H. Simmons, H.-J. He, M. Kurachi, and M. Tanabashi, Ideal fermion delocalization in five dimensional gauge theories, Physical Review D-Particles, Fields, Gravitation, and Cosmology 72 , 095013 (2005).
- [16] R. A. Horn and C. R. Johnson, The hadamard product, in Topics in Matrix Analysis (Cambridge University Press, 1991) p. 298-381.
- [17] R. C. Gonzalez, Digital image processing (Pearson education india, 2009).
- [18] I. Goodfellow, Y. Bengio, and A. Courville, Deep learning (MIT press, 2016).
- [19] H. Neudecker, S. Liu, and W. Polasek, The hadamard product and some of its applications in statistics, Statistics: A Journal of Theoretical and Applied Statistics 26 , 365 (1995).
- [20] C. Viazminsky, Necessary and sufficient conditions for a function to be separable, Applied mathematics and computation 204 , 658 (2008).
- [21] R. Alonso, A. Carmona, B. M. Dillon, J. F. Kamenik,

J. M. Camalich, and J. Zupan, A clockwork solution to the flavor puzzle, Journal of High Energy Physics 2018 , 1 (2018).

- [22] A. Ibarra, A. Kushwaha, and S. K. Vempati, Clockwork for neutrino masses and lepton flavor violation, Physics Letters B 780 , 86 (2018).
- [23] [A. Singh, Revisiting neutrino masses in clockwork models (2024), arXiv:2407.13733 [hep-ph].](https://arxiv.org/abs/2407.13733)
- [24] I. Ben-Dayan, Generalized clockwork theory, Physical Review D 99 , 096006 (2019).
- [25] A. Tropper and J. J. Fan, Randomness-assisted exponential hierarchies, Physical Review D 103 , 015001 (2021).
- [26] A. Ibarra, A. Singh, and S. K. Vempati, Flavour from fractal mass chains, arXiv preprint arXiv:2509.04811 (2025).
- [27] S. Covone, J. Davighi, G. Isidori, and M. Pesut, Flavour deconstructing the composite higgs, Journal of High Energy Physics 2025 , 1 (2025).
- [28] D. Bunk, J. Hubisz, J. Shao, and P. Tanedo, A top seesaw on a 5d playground, arXiv preprint arXiv:1111.3951 (2011).
- [29] C. T. Hill and A. K. Leibovich, Deconstructing 5d qed, Physical Review D 66 , 016006 (2002).
- [30] N. Arkani-Hamed, A. G. Cohen, and H. Georgi, (de) constructing dimensions, Physical Review Letters 86 , 4757 (2001).
- [31] C. T. Hill, S. Pokorski, and J. Wang, Gauge invariant effective lagrangian for kaluza-klein modes, Physical Review D 64 , 105005 (2001).
- [32] C. Csaki, J. Erlich, V. V. Khoze, E. Poppitz, Y. Shadmi, and Y. Shirman, Exact results in 5d from instantons and deconstruction, Physical Review D 65 , 085033 (2002).
- [33] T. H¨ allgren, T. Ohlsson, and G. Seidl, Neutrino oscillations in deconstructed dimensions, Journal of High Energy Physics 2005 , 049 (2005).
- [34] A. Abada, P. Escribano, X. Marcano, and G. Piazza, Collider searches for heavy neutral leptons: beyond simplified scenarios, The European Physical Journal C 82 , 1030 (2022).
- [35] T. H. Kwok, L. Li, T. Liu, and A. Rock, Searching for heavy neutral leptons at a future muon collider, Physical Review D 110 , 075009 (2024).
- [36] X. Marcano, Heavy neutral leptons and displaced vertices at lhc, arXiv preprint arXiv:1808.04705 (2018).
- [37] A. M. Abdullahi, P. B. Alz´ as, B. Batell, J. Beacham, A. Boyarsky, S. Carbajal, A. Chatterjee, J. I. CrespoAnad´ on, F. F. Deppisch, A. De Roeck, et al. , The present and future status of heavy neutral leptons, Journal of Physics G: Nuclear and Particle Physics 50 , 020501 (2023).
- [38] S. Hong, G. Kurup, and M. Perelstein, Clockwork neutrinos, Journal of High Energy Physics 2019 , 1 (2019).
- [39] T. P. Cheng and L.-F. Li, µ → eγ in theories with dirac and majorana neutrino-mass terms, Phys. Rev. Lett. 45 , 1908 (1980).
- [40] E. Ma and A. Pramudita, Exact formula for ( µ → e γ )-type processes in the standard model, Physical Review D 24 , 1410 (1981).
- [41] A. Baldini, Y. Bao, E. Baracchini, C. Bemporad, F. Berg, M. Biasotti, G. Boca, M. Cascella, P. Cattaneo, G. Cavoto, et al. , Search for the lepton flavour violat-

ing decay µ + → e+ γ with the full dataset of the meg experiment: Meg collaboration, The European Physical Journal C 76 , 434 (2016).

- [42] A. Boyarsky, O. Mikulenko, M. Ovchynnikov, and L. Shchutska, Exploring the potential of fcc-hh to search for particles from b mesons, Journal of High Energy Physics 2023 , 1 (2023).
- [43] M. Benedikt, A. Blondel, P. Janot, M. Mangano, and F. Zimmermann, Future circular colliders succeeding the lhc, Nature Physics 16 , 402 (2020).
- [44] A. M. Baldini et al. (MEG II), The Search for µ + → e+ γ with 10-14 Sensitivity: The Upgrade of the MEG Ex-

periment, Symmetry 13 , 1591 (2021), arXiv:2107.10767 [hep-ex].

- [45] K. Afanaciev, A. Baldini, S. Ban, H. Benmansour, G. Boca, P. Cattaneo, G. Cavoto, F. Cei, M. Chiappini, A. Corvaglia, et al. , New limit on the \ mu+¿ e+ \ gamma decay with the meg ii experiment, arXiv preprint arXiv:2504.15711 (2025).
- [46] A. Steward, Row rank= column rank, International Journal of Mathematical Education in Science and Technology 12 , 709 (1981).
- [47] [D. Zwick, Lecture 34, https://www.math.utah.edu/ ~ zwick/Classes/Fall2012\_2270/Lectures/Lecture34\_ with\_Examples.pdf (2012), accessed on Nov 06, 2023.](https://www.math.utah.edu/~zwick/Classes/Fall2012_2270/Lectures/Lecture34_with_Examples.pdf)