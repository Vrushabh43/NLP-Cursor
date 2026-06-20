## Quantum States in Twisted Tubes with Linear Cross-Section Variation

Guo-Hua Liang 1 , ∗ Ai-Guo Mei 1 , Men-Yun Lai 2 , and Shu-Sheng Xu 1

School of Science, Nanjing University of Posts and Telecommunications, Nanjing 210023, China and

1 2 College of Physics and Communication Electronics,

Jiangxi Normal University, Nanchang 330022, China

We study the quantum dynamics of a particle confined in a twisted tube with a linearly varying cross section. By relating a general linear transformation matrix to the system's Hamiltonian, we use an extended thin-layer method to derive an effective Hamiltonian for tangential motion under mild and general linear transformations. Explicit forms are provided for three fundamental transformations: rotation, scaling, and shearing. Rotation introduces a gauge field coupled to angular momentum, while scaling and shearing produce geometric potentials that lift degeneracies in noncircular cross sections. In square cross sections, these transformations cause energy splittings among formerly degenerate states, whereas circular cross sections retain degeneracy. Through an example combining rotation and squeezing, we analyze state evolution and compute the quantum geometric tensor to quantify geometric response. Our results demonstrate how geometric transformations can tailor quantum states and suggest that circular waveguides are more robust against mode mixing.

## I. INTRODUCTION

Quantum particles and photons confined in nanoscale systems can exhibit behavior similar to that observed in the presence of strong background fields [1, 2]. This occurs because the characteristic length scales in such systems approach the particle's wavelength, making nanoscale confinement an excellent platform for exploring a wider range of fundamental phenomena. In recent decades, advances in nanostructure fabrication [3-7] have enabled laboratory studies of various nanoscale dynamics. For example, scaled vertical-nanowire heterojunction tunnelling transistors are realized based on extreme quantum confinement in GaSb/InAs system [8], a roomtemperature nonlinear Hall effect has been observed in polycrystalline bismuth thin films [9], and the energy landscape of Bloch points in ferromagnetic nanowires can be tailored by curvature [10].

Certain nanostructures, especially low-dimensional ones, exhibit significant curvature and torsion. The effects of these geometric quantities have been investigated theoretically in various 2D and 1D systems. Using the thin-layer approach, it has been found that in 2D systems, curvature induces a scalar quantum potential known as the geometric potential [11-15]. When the particle possesses internal degrees of freedom [16-21] or the system is subjected to external fields [22, 23], curvature can act as an effective electric or magnetic field. In addition to curvature effects, torsion in quasi-1D and higher-dimensional systems plays the role of an induced gauge field that couples to the topological charge in the degenerate state space [24-32]. This feature in closed 1D systems is related to the Berry phase [33] and gives rise to a geometrically induced Aharonov-Bohm effect [34].

Most of these theoretical work adopts the idealized assumption that particles are confined to smooth surface layers or curved tubes with constant thickness or radius. However, defects are inevitable during the synthesis of nanomembranes or nanowires. By extending the thinlayer approach, it has been found that a slightly inhomogeneous thickness in a curved layer can induce an effective potential in the tangential dynamics, proportional to the ground-state energy and the thickness morphology function [35]. This potential allows quantum states to be localized in specific regions of the curved surface through engineered thickness distributions [36]. Further study indicates that thickness fluctuations do not affect spin dynamics [37].

[∗ lianggh@njupt.edu.cn](mailto:lianggh@njupt.edu.cn)

In this work, we employ the extended thin-layer approach to investigate the quantum dynamics of a particle confined within a twisted tube with a cross section that varies linearly along its axis. Studying quantum dynamics in tubes with varying cross sections is more challenging than in surface layers with nonuniform thickness, as the changing constrained dimension introduces additional complexity. A linear transformation of the two-dimensional cross section can be decomposed into fundamental transformations, namely rotation, scaling, and shearing [38]. We formulate the effective quantum dynamics in tubes under general linear transformations and examine the effects of each type of fundamental transformation individually. Furthermore, we investigate the sensitivity of quantum states, particularly degenerate states, to changes in transformation parameters, as captured by the quantum geometric tensor [39-42]. The real part of this tensor defines a Riemannian metric on the parameter space, providing a measure of the distance between quantum states, while the imaginary part corresponds to the Berry curvature, which governs the geometric phase of the system.

This paper is structured as follows. Section II builds the relationship between a general linear transformation matrix to the system Hamiltonian. Section III applies the condition of slight transformation and presents the explicit form of the effective Hamiltonian for rotation, scaling, and shearing of the cross section, respectively. In Section IV, we discuss the energy splitting, states phase and quantum geometric tensor in an example where a twisted tube experiences rotation and squeezing simultaneously. Finally, our conclusion are written in Section V.

## II. HAMILTONIAN IN ADAPTED COORDINATES

We consider a quantum particle confined to a twisted tube with its axis forming a space curve C , as illustrated in Fig. 1. The cross section of the tube varies linearly along C . In Fig. 1, we demonstrate three fundamental linear transformations, namely rotation, scaling and shearing, which are applied to both circular and square cross sections. The q 1 -q 2 plane represents the normal plane of C , where q 1 and q 2 are coordinates along the normal vector n and the binormal vector b , respectively. The tangent vector t of C , together with n and b , forms the Frenet frame. In this frame, the neighborhood space around C can be parameterized as

$$R = r ( s ) + q _ { 1 } n ( s ) + q _ { 2 } b ( s ) , \quad ( 1 )$$

where r ( s ) is the position vector of C and s represents the arclength. The Frenet frame satisfies the Frenet-Serret equation

$$\left ( \begin{array} { c } \dot { t } \\ \dot { n } \\ \dot { b } \end{array} \right ) = \left ( \begin{array} { c c c } 0 & \kappa ( s ) & 0 \\ - \kappa ( s ) & 0 & \tau ( s ) \\ 0 & - \tau ( s ) & 0 \end{array} \right ) \left ( \begin{array} { c } t \\ n \\ b \end{array} \right ) \, , \quad ( 2 ) \quad \text {section} \quad \text {and} \, s \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {and} \, s \quad \text {and} \, t \quad \text {an$$

where the dot denotes the derivative with respect to s ; κ ( s ) and τ ( s ) are the curvature and torsion of the curve, respectively.

To accommodate the variation in the cross section of the tube, we introduce new coordinates ( q ′ 1 , q ′ 2 ) in the normal plane of C , which are related to the original coordinates ( q 1 , q 2 ) via a 2 × 2 linear transformation matrix T ( s ), namely

$$\left ( \begin{array} { c } q _ { 1 } \\ q _ { 2 } \end{array} \right ) = \mathbb { T } ( s ) \left ( \begin{array} { c } q _ { 1 } ^ { \prime } \\ q _ { 2 } ^ { \prime } \end{array} \right ) . \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \$$

Here, the components T ab ( s ), with a, b = 1 , 2, are continuous functions of s . The matrix can be expressed as T = ( ¯ t 1 , ¯ t 2 ) T = ( ˜ t 1 , ˜ t 2 ), where ¯ t a = ( T a 1 , T a 2 ), ˜ t a = ( T 1 a , T 2 a ) T , and the superscript T denotes the transpose.

In the new coordinate system, the space around C can be parameterized as

$$R = r ( s ) + ( \bar { t } _ { 1 } \cdot q _ { \perp } ^ { \prime } ) n ( s ) + ( \bar { t } _ { 2 } \cdot q _ { \perp } ^ { \prime } ) b ( s ) , \quad ( 4 ) \quad \exp ( 2 )$$

where q ′ ⊥ = ( q ′ 1 , q ′ 2 ) T . A straightforward calculation yields

$$\partial _ { q _ { 1 } } R = T _ { 1 1 } n + T _ { 2 1 } b ,$$

$$\partial _ { q _ { 2 } } R = T _ { 1 2 } n + T _ { 2 2 } b ,$$

FIG. 1. (a) Schematic of a twisted tube with a circular cross section undergoing linear transformations: rotation, scaling, and shearing. (b) Same as (a), but with a square cross section.

<!-- image -->

and

$$\partial _ { s } R = \gamma \alpha + \zeta n + \eta b ,$$

where ˆ d = ( ∂ s , τ ) T is a vector operator, γ = 1 -κ ( ¯ t 1 · q ′ ⊥ ), ζ = ( σ z ˆ d ) T T q ′ ⊥ , and η = ( σ x ˆ d ) T T q ′ ⊥ . Here, σ x and σ z denote the Pauli matrices.

In the curvilinear coordinates ( q 1 , q 2 , s ), the metric tensor can be obtained through G ij = ∂ i R · ∂ j R , where i, j = 1 , 2 , 3. The explicit form of the metric is given by the matrix

$$G _ { i j } & = \left ( \begin{array} { c c c } | \tilde { t } _ { 1 } | ^ { 2 } & \tilde { t } _ { 1 } \cdot \tilde { t } _ { 2 } & \xi \cdot \tilde { t } _ { 1 } \\ \tilde { t } _ { 1 } \cdot \tilde { t } _ { 2 } & | \tilde { t } _ { 2 } | ^ { 2 } & \tilde { \xi } \cdot \tilde { t } _ { 2 } \\ \xi \cdot \tilde { t } _ { 1 } & \xi \cdot \tilde { t } _ { 2 } & \gamma ^ { 2 } + \zeta ^ { 2 } + \eta ^ { 2 } \end{array} \right ) , \\$$

where ξ = ( ζ, η ) T . The determinant of the metric is then G = det( G ij ) = (1 -κ ¯ t 1 · q ′ ⊥ ) 2 | T | 2 .

For the inverse of the metric, the components can be expressed in compact form as follows

$$G ^ { s s } = \frac { 1 } { \gamma ^ { 2 } } ,$$

$$G ^ { s a } = G ^ { a s } = \frac { \epsilon ^ { a c } t _ { c } \cdot \bar { \xi } } { \gamma ^ { 2 } | \mathbb { T } | } ,$$

and

$$G ^ { a b } = \gamma ^ { 2 } G ^ { s a } G ^ { s b } + \frac { ( \epsilon ^ { a c } \tilde { t } _ { c } ) \cdot ( \epsilon ^ { b d } \tilde { t } _ { d } ) } { | \mathbb { T } | ^ { 2 } } , \quad ( 1 1 ) \quad \text {tive} \\ \intertext { G ^ { a b } = \gamma ^ { 2 } G ^ { s a } G ^ { s b } + \frac { ( \epsilon ^ { a c } \tilde { t } _ { c } ) \cdot ( \epsilon ^ { b d } \tilde { t } _ { d } ) } { | \mathbb { T } | ^ { 2 } } , \quad ( 1 1 ) \quad \text {tive} \\ \intertext { G ^ { a b } = \gamma ^ { 2 } G ^ { s a } G ^ { s b } + \frac { ( \epsilon ^ { a c } \tilde { t } _ { c } ) \cdot ( \epsilon ^ { b d } \tilde { t } _ { d } ) } { | \mathbb { T } | ^ { 2 } } , \quad ( 1 1 ) \quad \text {tive} \\ \intertext { G ^ { a b } = \gamma ^ { 2 } G ^ { s a } G ^ { s b } + \frac { ( \epsilon ^ { a c } \tilde { t } _ { c } ) \cdot ( \epsilon ^ { b d } \tilde { t } _ { d } ) } { | \mathbb { T } | ^ { 2 } } , \quad ( 1 1 ) \quad \text {tive} \\ \intertext { G ^ { a b } = \gamma ^ { 2 } G ^ { s a } G ^ { s b } + \frac { ( \epsilon ^ { a c } \tilde { t } _ { c } ) \cdot ( \epsilon ^ { b d } \tilde { t } _ { d } ) } { | \mathbb { T } | ^ { 2 } } , \quad ( 1 1 ) \quad \text {tive} \\ \intertext { G ^ { a b } = \gamma ^ { 2 } G ^ { s a } G ^ { s b } + \frac { ( \epsilon ^ { a c } \tilde { t } _ { c } ) \cdot ( \epsilon ^ { b d } \tilde { t } _ { d } ) } { | \mathbb { T } | ^ { 2 } } , \quad ( 1 1 ) \quad \text {tive} \\ \intertext { G ^ { a b } = \gamma ^ { 2 } G ^ { s a } G ^ { s b } + \frac { ( \epsilon ^ { a c } \tilde { t } _ { c } ) \cdot ( \epsilon ^ { b d } \tilde { t } _ { d } ) } { | \mathbb { T } | ^ { 2 } } , \quad ( 1 1 ) \quad \text {tive} \\ \intertext { G ^ { a b } = \gamma ^ { 2 } G ^ { s a } G ^ { s b } + \frac { ( \epsilon ^ { a c } \tilde { t } _ { c } ) \cdot ( \epsilon ^ { b d } \tilde { t } _ { d } ) } { | \mathbb { T } | ^ { 2 } } , \quad ( 1 1 ) \quad \text {tive} \\ \intertext { G ^ { a b } = \gamma ^ { 2 } G ^ { s a } G ^ { s b } + \frac { ( \epsilon ^ { a c } \tilde { t } _ { c } ) \cdot ( \epsilon ^ { b d } \tilde { t } _ { d } ) } { | \mathbb { T } | ^ { 2 } } , \quad ( 1 1 ) \quad \text {tive} \\ \intertext { G ^ { a b } = \gamma ^ { 2 } G ^ { s a } G ^ { s b } + \frac { ( \epsilon ^ { a c } \tilde { t } _ { c } ) \cdot ( \epsilon ^ { b d } \tilde { t } _ { d } ) } { | \mathbb { T } | ^ { 2 } } , \quad ( 1 1 ) \quad \text {tive} \\ \intertext { G ^ { a b } = \gamma ^ { 2 } G ^ { s a } G ^ { s b } + \frac { ( \epsilon ^ { a c } \tilde { t } _ { c } ) \cdot ( \epsilon ^ { b d } \tilde { t } _ { d } ) } { | \mathbb { T } | ^ { 2 } } , \quad ( 1 1 ) \quad \text {tive} \\ \intertext { G ^ { a b } = \gamma ^ { 2 } G ^ { s a } G ^ { s b } + \frac { ( \epsilon ^ { a c } \tilde { t } _ { c } ) \cdot ( \epsilon ^ { b d } \tilde { t } _ { d } ) } { | \mathbb { T } | ^ { 2 } } , \quad ( 1 1 ) \quad \text {tive} \\ \intertext { G ^ { a b } = \gamma ^ { 2 } G ^ { s a } G ^ { s b } + \frac { ( \epsilon ^ { a c } \tilde { t } _ { c } ) \cdot ( \epsilon ^ { b d } \tilde { t } _ { d } ) } { | \mathbb { T } | ^ { 2 } } , \quad ( 1 1 ) \quad \text {tive} \\ \intertext { G ^ { a b } = \gamma ^ { 2 } G ^ { s a } G ^ { s b } + \frac { ( \epsilon ^ { a c } \tilde { t } _ { c } ) \cdot ( \epsilon ^ { b d } \tilde { t } _ { d } ) } { | \mathbb { T } | ^ { 2 } } , \quad ( 1 1 ) \quad \text {tive} \\ \intertext { G ^ { a b } = \gamma ^ { 2 } G ^ { s a } G ^ { s b } + \frac { ( \epsilon ^ { a c } \tilde { t } _ { c } ) \cdot ( \epsilon ^ { b d } \tilde { t } _ { d } ) } { | \mathbb { T } | ^ { 2 } } , \quad ( 1 1 ) \quad \text {tive} \\ \intertext { G ^ { a b } = \gamma ^ { 2 } G ^ { s a } G ^ { s b } + \frac { ( \epsilon ^ { a c } \tilde { t } _ { c } ) \cdot ( \epsilon ^ { b d } \tilde { t } _ { d } ) } { | \mathbb { T } | ^ { 2 } } , \quad ( 1 1 ) \quad \text {tive} \\ \intertext { G ^ { a b } = \gamma ^ { 2 } G ^ { s a } G ^ { s b } + \frac { ( \epsilon ^ { a c } \tilde { t } _ { c } ) \cdot ( \epsilon ^ { b d } \tilde { t } _ { d } ) } { | \mathbb { T } | ^ { 2 } } , \quad ( 1 1 ) \quad \text {tive} \\ \intertext { G ^ { a b } = \gamma ^ { 2 } G ^ { s a } G ^ { s b } + \frac { ( \epsilon ^ { a c } \tilde { t } _ { c } ) \cdot ( \epsilon ^ { b d } \tilde { t } _ { d } ) } { | \mathbb { T } | ^ { 2 } } , \quad ( 1 1 ) \quad \text {tive} \\ \intertext { G ^ { a b } = \gamma ^ { 2 } G ^ { s a } G ^ { s b } + \frac { ( \epsilon ^ { a c } \tilde { t } _ { c } ) \cdot ( \epsilon ^ { b d } \tilde { t } _ { d } ) } { | \mathbb { T } | ^ { 2 } } , \quad ( $$

where ϵ ac denotes the Levi-Civita symbol and ¯ ξ = iσ y ξ .

Now let us discuss the influence of cross section shape variations on the effective dynamics. We assume that the particles are confined to a twisted tube by a confining potential V c , which has a deep minimum at q 1 = q 2 = 0. If the cross section remains constant along the axis (as indicated by the dashed outlines in Fig. 1), i.e., V c = V c ( q 1 , q 2 ), the bound energy levels in the transverse direction are maintained. This facilitates a separation of dynamics between the longitudinal and transverse directions. However, when the cross section varies along the axis, V c becomes s -dependent, which prevents such a separation. We expect that the coordinate transformation T , adapted to the cross section variation, will restore the s -independence of the confining potential, transforming V c ( q 1 , q 2 , s ) into V ′ c ( q ′ 1 , q ′ 2 ).

In the curvilinear coordinates ( q ′ 1 , q ′ 2 , s ), the Schr¨ odinger equation for a particle confined within the tube is given by

$$- \frac { \hslash ^ { 2 } } { 2 m } \nabla ^ { 2 } \Psi + V _ { c } ^ { \prime } ( q _ { 1 } ^ { \prime } , q _ { 2 } ^ { \prime } ) \Psi = E \Psi , \quad ( 1 2 ) \quad \begin{matrix} c o r n { r } \\ f o r n { n } \end{matrix}$$

where the Laplacian operator corresponding to the given metric takes the form

$$\text {where the Laplacian operator corresponding to the given} & \quad \lim i t { \quad } \text {metric takes the form} & a \ g e n \\ \nabla ^ { 2 } = & \frac { 1 } { \sqrt { G } } \partial _ { i } ( \sqrt { G } G ^ { i j } \partial _ { j } ) & \quad \text {separates} \\ = & \frac { 1 } { \sqrt { G } } \frac { ( \epsilon ^ { a } t _ { c } ) \cdot ( \epsilon ^ { a } t _ { d } ) } { | \mathbb { T } | ^ { 2 } } \partial _ { a } \sqrt { G } \partial _ { b } + \frac { 1 } { \sqrt { G } } \partial _ { s } ( G ^ { s s } \sqrt { G } \partial _ { s } ) & \quad \text {where} \\ & + \frac { 1 } { \sqrt { G } } \partial _ { a } ( \sqrt { G } G ^ { s s } \frac { \mathcal { A } ^ { a } \mathcal { A } ^ { b } } { | \mathbb { T } | ^ { 2 } } \partial _ { b } ) & \quad \text {have} \\ & + \frac { 1 } { \sqrt { G } } \partial _ { s } ( \sqrt { G } G ^ { s a } \partial _ { a } ) + \frac { 1 } { \sqrt { G } } \partial _ { a } ( \sqrt { G } G ^ { s a } \partial _ { s } ) , & \quad \text {timate} \\ & \quad ( 1 3 ) \\ \text {with the definition } \mathcal { A } ^ { a } = \epsilon ^ { a c } \tilde { t } _ { c } \cdot \bar { \xi } . & \quad \text {variatint} \\ & \quad \text {by introducing } a \ d e r i v i v e { \, } \text {operator } D _ { s } \ = \ \partial _ { s } +$$

By introducing a derivative operator D s = ∂ s + 1 2 {A a ,∂ a } | T | , where {· , ·} denotes the anticommutator, we can compactly rewrite the Laplacian as

with the definition A a = ϵ ac ˜ t c · ¯ ξ .

$$\nabla ^ { 2 } & = \frac { 1 } { \sqrt { G } } D _ { s } \sqrt { G } G ^ { s s } D _ { s } + \frac { 1 } { \sqrt { G } } \frac { \epsilon ^ { a c } \epsilon ^ { b d } \tilde { t } _ { c } \cdot \tilde { t } _ { d } } { | \mathbb { T } | ^ { 2 } } \partial _ { a } \sqrt { G } \partial _ { b } - V _ { T } \\ \text {where} & \quad .$$

where

$$V _ { T } = & \frac { 1 } { 2 \gamma | \mathbb { T } | ^ { 2 } } \mathcal { A } ^ { a } \partial _ { a } \left [ \frac { 1 } { \gamma } ( \partial _ { b } \mathcal { A } ^ { b } ) \right ] + \frac { 1 } { 4 \gamma ^ { 2 } | \mathbb { T } | ^ { 2 } } ( \partial _ { a } \mathcal { A } ^ { a } ) ( \partial _ { b } \mathcal { A } ^ { b } ) \\ & + \frac { 1 } { 2 \gamma | \mathbb { T } | ^ { 2 } } \partial _ { s } \left [ \frac { | \mathbb { T } | } { \gamma } \partial _ { a } \mathcal { A } ^ { a } \right ] . & & \text {Here,} \\ & \text {Here we establish the relationship between the cross-}$$

Here we establish the relationship between the crosssectional transformation matrix and the equation of motion. It should be noted that when the transformation matrix reduces to the identity matrix, A a simplifies to ϵ ac τq c , and the anticommutator in the covariant derivative reduces to -i ℏ τ ˆ L [32, 33], where the angular momentum operator ˆ L = i ℏ ( q 2 ∂ q 1 -q 1 ∂ q 2 ).

## III. THIN-LAYER PROCEDURE FOR SLIGHT TRANSFORMATIONS

To obtain the tangential dynamics under the confining potential, it is necessary to distinguish between different energy regimes. For this purpose, we introduce a dimensionless small parameter δ . In the energy regime under consideration, the wave function is localized near q 1 = q 2 = 0. We therefore rescale the transverse coordinates as q ′ ⊥ → √ δ q ′ ⊥ . To match the kinetic energy in the transverse direction, the confining potential should be rescaled as V ′ c → V ′ c /δ . Considering the metric in the adapted coordinates, the wave function satisfies the normalization condition ∫ | Ψ | 2 √ Gdsd q ′ ⊥ = 1. By introducing a new wave function ψ = G 1 / 4 Ψ, we obtain a one-dimensional probability density along the axial direction defined as P ( s ) = ∫ | ψ | 2 d q ′ ⊥ , which satisfies the normalization condition ∫ P ( s ) ds = 1. The Hamiltonian corresponding to the new wave function is then transformed as H → G 1 / 4 HG -1 / 4 .

Before performing the thin-layer procedure, we need to limit the amplitude of the linear transformation T since a generally linear transformation prevents the dynamics separation between longitudinal and transverse direction.

Here, we consider the slight variation condition of the cross section, which takes the form T = R θ [1 + δ W ], where R θ is a 2D rotation matrix and W is a general 2 × 2 linear transformation matrix. Mathematically, we have | T | = 1 + δ tr( R -1 θ W ) + O ( δ 3 / 2 ). Furthermore, the variation of the transformation along s should be sufficiently slow, i.e., ∂ s T ab ≪ 1 / ( δq ). With this form, we estimate that A a is of order δ 1 / 2 . Accordingly, the rescaled Hamiltonian can be expanded in power of δ as

$$G ^ { 1 / 4 } H G ^ { - 1 / 4 } = H _ { ( - 1 ) } + H _ { ( 0 ) } + O ( \delta ^ { 1 / 2 } ) , \quad ( 1 6 )$$

where

$$H _ { ( - 1 ) } = \frac { 1 } { \delta } \left [ - \frac { \hslash ^ { 2 } } { 2 m } \nabla _ { \perp } ^ { 2 } + V _ { c } ( q _ { 1 } ^ { \prime } , q _ { 2 } ^ { \prime } ) \right ] , \quad ( 1 7 )$$

with ∇ 2 ⊥ = ∂ 2 q ′ 1 + ∂ 2 q ′ 2 , and

$$H _ { ( 0 ) } = - \frac { \hbar { ^ } { 2 } } { 2 m } [ \frac { 1 } { \sqrt { G } } D _ { s } ( \sqrt { G } G ^ { s s } D _ { s } ) ] + V _ { T } + V _ { g } + V _ { H } . \\ \\ \\ \\ \\$$

Here, the well-known geometric potential V g = -ℏ 2 κ 2 8 m , and the term V H , which arises from the linear transformation W , has the form

$$V _ { H } = - \frac { \hbar { ^ } { 2 } } { 2 m } [ 2 W _ { 1 1 } \partial _ { 2 } ^ { 2 } + 2 W _ { 2 2 } \partial _ { 1 } ^ { 2 } - 2 ( W _ { 1 2 } + W _ { 2 1 } ) \partial _ { 2 } \partial _ { 1 } ] , \, ( 1 9 )$$

where W ab are the components of W .

The Hamiltonian H ( -1) describes a quantum particle confined in a 2D plane by the potential V c ( q ′ 1 , q ′ 2 ), which governs the eigenstates in the transverse direction. The Hamiltonian H (0) , on the other hand, primarily governs the tangential dynamics along the tube. The kinetic energy term V H originates from the transverse direction and is explicitly induced by the transformation matrix W . Since H ( -1) is of order 1 /δ , the energy levels corresponding to different transverse eigenstates exhibit negligible overlap along the longitudinal direction within the energy range of H (0) . This allows us to employ the ansatz ψ ( q ′ ⊥ , s ) = ∑ β χ β ( q ′ ⊥ ) φ β ( s ), where β is a degeneracy index and χ β satisfies the eigenvalue equation H ( -1) χ β = E ( -1) χ β . Note that H (0) is not yet the desired effective Hamiltonian, as the operator D s and the term V H still depend on transverse coordinates and derivatives.

By projecting onto the subspace spanned by the transverse states χ β , the effective tangential Hamiltonian is obtained as

$$H _ { \text {eff} } ^ { \beta ^ { \prime } \beta } = \int \chi _ { \beta ^ { \prime } } ^ { * } H _ { ( 0 ) } \chi _ { \beta } d q _ { \perp } ^ { \prime } .$$

In the following, we derive the explicit forms of this effective Hamiltonian for the cases in which the tube cross section undergoes rotation, scaling, and shear transformations, respectively.

## A. Rotation

For a pure rotational transformation, we have W = 0 and

$$\mathbb { T } = \mathbb { R } _ { \theta } = \left [ \begin{array} { c c } \cos \theta ( s ) & - \sin \theta ( s ) \\ \sin \theta ( s ) & \cos \theta ( s ) \end{array} \right ] .$$

In this case, we obtain

$$\bar { \xi } = \sqrt { \delta } ( \omega + \tau ) \left ( \begin{array} { c } q _ { 1 } ^ { \prime } \cos \theta - q _ { 2 } ^ { \prime } \sin \theta \\ q _ { 1 } ^ { \prime } \sin \theta + q _ { 2 } ^ { \prime } \cos \theta \end{array} \right ) , \quad ( 2 2 ) \quad \mathbb { R } _ { \theta } = 0$$

where ω = ∂ s θ . This leads to

$$\mathcal { A } ^ { 1 } = \sqrt { \delta } q _ { 2 } ^ { \prime } ( \omega + \tau )$$

and

$$\mathcal { A } ^ { 2 } = - \sqrt { \delta } q _ { 1 } ^ { \prime } ( \omega + \tau ) \quad \quad ( 2 4 ) \quad \begin{matrix} o n o r \\ a s \\ \delta f \end{matrix}$$

As a result, ∂ a A a = 0, which implies V T = 0. The Hamiltonian H 0 therefore reduces to

$$H _ { 0 } = - \frac { \hbar { ^ } { 2 } } { 2 m } D _ { s } ^ { 2 } + V _ { g } ,$$

where the covariant derivative is given by D s = ∂ s -i ( ω + τ ) ˆ L/ ℏ .

If the linear transformation is applied to a tube with a circular cross section, the transverse eigenstates can be expressed as χ n,l ∝ R n,l ( ρ ) e ilθ , where ρ = √ q ′ 2 1 + q ′ 2 2 , l = 0 , ± 1 , ± 2 , · · · is the angular quantum number, n = 1 , 2 , 3 , . . . denotes the radial quantum number, and R n,l ( ρ ) represents the radial wave function. Using Eq. (20), we obtain the effective Hamiltonian for a circular cross section under a rotational transformation,

$$H _ { \text {cir} } = - \frac { \hbar { ^ } { 2 } } { 2 m } [ \partial _ { s } - i ( \omega + \tau ) l ] ^ { 2 } + V _ { g } .$$

If the transformation is applied to a tube with a square cross section, the transverse eigenstates are given by | n 1 n 2 〉 = 2 d sin( n 1 πq 1 d -n 1 π 2 ) sin( n 2 πq 2 d -n 2 π 2 ), where d is the side length. Due to the square symmetry, the states | n 1 n 2 〉 and | n 2 n 1 〉 are degenerate. A suitable choice of basis states is | + 〉 n 1 n 2 = ( | n 1 n 2 〉 + i | n 2 n 1 〉 ) / √ 2 and |-〉 n 1 n 2 = ( | n 1 n 2 〉 -i | n 2 n 1 〉 ) / √ 2. The effective Hamiltonian in the subspace spanned by | + 〉 n 1 n 2 and |-〉 n 1 n 2 takes the form

$$H _ { s q u } = - \frac { \hslash ^ { 2 } } { 2 m } [ \partial _ { s } - i ( \omega + \tau ) \sigma _ { z } \langle L \rangle _ { n _ { 1 } n _ { 2 } } ] ^ { 2 } + V _ { g } , \quad ( 2 7 )$$

where 〈 L 〉 n 1 n 2 = 16 n 2 1 n 2 2 [ -1+( -1) n 1 + n 2 ] 2 ( n 2 1 -n 2 2 ) 3 π 2 . It can be observed that when n 1 + n 2 is even, the gauge term in the effective Hamiltonian vanishes. In contrast, when n 1 + n 2 is odd, the gauge term takes opposite signs for the two basis states.

Therefore, both the rotational transformation and the torsion of the tube itself induce an effective angular momentum that acts as a gauge potential, coupling to the angular momentum eigenvalue. Moreover, in both circular and square cross sections, the rotational transformation does not break the degeneracy of the transverse eigenstates.

## B. Scaling

For a scaling transformation, we have θ ( s ) = 0, so that R θ = I , where I is the 2 × 2 identity matrix, and W is given by

$$\mathbb { W } = \left [ \begin{array} { c c } f _ { 1 } ( s ) & 0 \\ 0 & f _ { 2 } ( s ) \end{array} \right ] .$$

If the scaling corresponds to a stretching transformation, one of the functions f 1 or f 2 is set to unity. In the case of a squeezing transformation, the condition (1 + δf 1 )(1 + δf 2 ) = 1 must be satisfied, implying f 1 = -f 2 .

In this case,

$$\bar { \xi } & = \sqrt { \delta } \left [ \begin{array} { c c } ( 1 + \delta \dot { f } _ { 1 } ) \tau q _ { 1 } ^ { \prime } + \delta \dot { f } _ { 2 } q _ { 2 } ^ { \prime } \\ - \delta \dot { f } _ { 1 } q _ { 1 } ^ { \prime } + ( 1 + \delta \dot { f } _ { 2 } ) \tau q _ { 2 } ^ { \prime } \end{array} \right ] . \\$$

Consequently, we obtain

$$\mathcal { A } ^ { 1 } = ( 1 + \delta f _ { 2 } ) \sqrt { \delta } [ - \delta \dot { f } _ { 1 } q _ { 1 } ^ { \prime } + ( 1 + \delta \dot { f } _ { 2 } ) \tau q _ { 2 } ^ { \prime } ] \quad ( 3 0 )$$

and

$$\mathcal { A } ^ { 2 } & = - ( 1 + \delta f _ { 1 } ) \sqrt { \delta } [ ( 1 + \delta \dot { f } _ { 1 } ) \tau q _ { 1 } ^ { \prime } + \delta \dot { f } _ { 2 } q _ { 2 } ^ { \prime } ] \\ \\$$

One can find that V T ∼ O ( δ ) and ∂ a A a ∼ O ( δ ). Therefore, to zeroth order in δ , the covariant derivative remains D s = ∂ s -iτ ˆ L/ ℏ . When evaluating V H , different cases must be treated separately.

When the tube has a circular cross section, the effective Hamiltonian in the subspace spanned by χ n,l and χ n, -l is given by

$$V _ { H } ^ { l l ^ { \prime } } = \delta ( f _ { 1 } + f _ { 2 } ) E _ { n , l } I , \quad ( 3 2 ) \int _ { \ e r a r { } } ^ { 3 2 }$$

where E n,l denotes the transverse eigenenergy of the degenerate states. The resulting effective Hamiltonian becomes

$$H _ { \text {cir} } = - \frac { \hbar { ^ } { 2 } } { 2 m } ( \partial _ { s } - i \tau l ) ^ { 2 } + V _ { g } + \delta ( f _ { 1 } + f _ { 2 } ) E _ { n , l } . \quad ( 3 3 )$$

For a tube with a square cross section, the correction term within the subspace spanned by | + 〉 n 1 n 2 and |-〉 n 1 n 2 takes the form

$$V _ { H ( \text {scaling} ) } ^ { n _ { 1 } n _ { 2 } } = & \delta ( f _ { 1 } + f _ { 2 } ) ( E _ { n _ { 1 } } + E _ { n _ { 2 } } ) \mathbf I \\ & + \delta ( f _ { 1 } - f _ { 2 } ) ( E _ { n _ { 2 } } - E _ { n _ { 1 } } ) \sigma _ { x } , \quad \text {and} \\$$

where E n a is the transverse eigenenergy along the q ′ a direction. The corresponding effective Hamiltonian is then

$$H _ { s q u } = - \frac { \hbar { ^ } { 2 } } { 2 m } ( \partial _ { s } - i \tau \sigma _ { z } \langle L \rangle _ { n _ { 1 } n _ { 2 } } ) ^ { 2 } + V _ { g } + V _ { H ( s c a l i n g ) } ^ { n _ { 1 } n _ { 2 } } \quad \text {Once} \quad \\$$

̸

It can be observed that for a tube with a circular cross section, slight scaling introduces an effective potential without lifting the degeneracy of the energy levels. In contrast, for a square cross section, the effective potential resulting from scaling contains non-zero off-diagonal elements in excited modes where n 1 = n 2 , leading to a splitting of the degenerate levels. Notably, under a squeezing transformation where f 1 = -f 2 , the correction V H vanishes in the circular case, while in the square case only the off-diagonal components remain. This suggests that waveguides with circular cross sections are less susceptible to deformation-induced mode mixing than those with square cross sections, thereby offering better preservation of wave modes.

## C. Shearing

For a shearing transformation parallel to the q 1 axis, we have θ ( s ) = 0 and

$$\mathbb { W } = \left ( \begin{array} { c c } 0 & f ( s ) \\ 0 & 0 \end{array} \right )$$

One finds that

$$\bar { \xi } = \sqrt { \delta } \left [ \begin{array} { c } \tau ( q _ { 1 } ^ { \prime } + \delta f q _ { 2 } ^ { \prime } ) \\ ( - \delta \dot { f } + \tau ) q _ { 2 } ^ { \prime } \end{array} \right ] .$$

Subsequently, we obtain

$$\mathcal { A } ^ { 1 } = \sqrt { \delta } [ \delta f \tau ( q _ { 1 } ^ { \prime } + \delta f q _ { 2 } ^ { \prime } ) + ( - \delta \dot { f } + \tau ) q _ { 2 } ^ { \prime } ] \quad ( 3 8 )$$

and

$$\mathcal { A } ^ { 2 } = - \tau \sqrt { \delta } ( q _ { 1 } ^ { \prime } + \delta f q _ { 2 } ^ { \prime } )$$

Similar to the scaling case, here ∂ a A a ∼ O ( δ ) and V T ∼ O ( δ ). The covariant derivative remains D s = ∂ s -iτ ˆ L/ ℏ , and and the resulting term V H is given by V H = ℏ 2 m f∂ 1 ∂ 2 .

Performing the integral within the subspace of degenerate states for the circular and square cross section cases yields V ll ′ H = 0 and

$$V _ { H ( \text {shear} ) } ^ { n _ { 1 } n _ { 2 } } = - \frac { 3 2 f } { \pi ^ { 2 } } \frac { n _ { 1 } ^ { 2 } n _ { 2 } ^ { 2 } ( E _ { n _ { 1 } } + E _ { n _ { 2 } } ) } { ( n _ { 1 } ^ { 2 } - n _ { 2 } ^ { 2 } ) ^ { 2 } ( n _ { 1 } ^ { 2 } + n _ { 2 } ^ { 2 } ) } \sigma _ { x } , \\$$

respectively. Thus, the effective Hamiltonians for the circular and square cross-sections in this case are respectively

$$H _ { c i r } = - \frac { \hslash ^ { 2 } } { 2 m } ( \partial _ { s } - i \tau l ) ^ { 2 } + V _ { g } ,$$

and

$$^ { \prime } _ { a } \, \text {di-} \quad H _ { s q u } = - \frac { \hbar { ^ } { 2 } } { 2 m } ( \partial _ { s } - i \tau \sigma _ { z } \langle L \rangle _ { n _ { 1 } n _ { 2 } } ) ^ { 2 } + V _ { g } + V _ { H ( \text {shear} ) } ^ { n _ { 1 } n _ { 2 } } .$$

Once again, the difference between the Hamiltonians for the circular and square tubes under shearing transformation demonstrates that circular waveguides are more effective in preserving propagation modes.

## IV. COMBINATION OF ROTATION AND SQUEEZING IN HELICAL TUBES: STATE PHASE AND QUANTUM GEOMETRIC TENSOR

In this section, we consider a concrete example in which a tube with a square cross section undergoes a linear transformation that combines rotation with squeezing. The transformation matrix is given by T = R θ [1 + δ W ], where

$$\mathbb { W } = \left [ \begin{smallmatrix} f ( s ) & 0 \\ 0 & - f ( s ) \end{smallmatrix} \right ] .$$

Then, in the subspace spanned by the basis states | + 〉 n 1 n 2 and |-〉 n 1 n 2 , the effective equation becomes

$$- \frac { \hbar { ^ } { 2 } } { 2 m } [ \partial _ { s } - i \alpha \sigma _ { z } ] ^ { 2 } \phi ( s ) + V _ { H ( s q u e z e ) } ^ { n 1 n 2 } \phi ( s ) = E \phi ( s ) , \ ( 4 4 )$$

where α = ( ω + τ ) 〈 L 〉 n 1 n 2 and the potential V n 1 n 2 H (squeeze) in this basis is

$$V _ { H ( \text {squeeze} ) } ^ { n 1 n 2 } = \left [ \begin{array} { c c } 0 & 2 f \Delta E \\ 2 f \Delta E & 0 \end{array} \right ] ,$$

wherein ∆ E = E n 2 -E n 1 .

Obtaining an exact analytical solution to this equation is challenging because the gauge potential is diagonal while the effective potential is off-diagonal. Here, we assume that E ≫ | 2 f ∆ E | , E ≫ | ℏ 2 α 2 / (2 m ) | , and that the functions τ ( s ), f ( s ) and ω ( s ) vary slowly. Under these conditions, we can apply the WKB approximation by treating the effective Hamiltonian in a classical form and neglecting the term ∂ s ( ω + τ ). This leads to two energy branches

$$\mathcal { E } _ { \pm } = \frac { p ^ { 2 } } { 2 m } + \frac { \hbar { ^ } { 2 } \alpha ^ { 2 } } { 2 m } \pm \sqrt { ( \frac { \hbar { \alpha } p } { m } ) ^ { 2 } + ( 2 f \Delta E ) ^ { 2 } } ,$$

where p denotes the classical momentum. Setting E = E ± , we solve for the momentum

$$p _ { \pm } & \approx \pm \hbar { \alpha } \pm \sqrt { 2 m ( E \mp 2 f \Delta E ) - \hbar { ^ } { 2 } \alpha ^ { 2 } } . \\ \intertext { I n d i v i n g t h i s e x p r e s i o n f o r t h e m o m e n t u m t h e c o u r }$$

In deriving this expression for the momentum, the coupling term between p + and p -has been neglected. Notably, motion in opposite directions corresponds to distinct energy levels. This indicates that geometric chirality formed by rotation and squeezing transformations induces a splitting of the energy levels, thereby lifting the degeneracy of previously degenerate states and coupling the direction of motion to specific energy levels. This phenomenon is reminiscent of spin-momentum locking in topological insulators.

For each energy branch, we assume a WKB solution of the form

$$\phi _ { \pm } = u _ { \pm } ( s ) \exp ( \frac { i } { \hbar } \int p _ { \pm } d s ) , \quad \quad \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \$$

where u ± ( s ) can be interpreted as slowly varying SO(2) spinors.

Substituting the WKB ansatz into Eq. (44) and retaining terms to zeroth order in ℏ , we obtain

$$u _ { + } = \frac { C _ { + } } { \sqrt { | p _ { + } - \hbar { \alpha } | } } \frac { 1 } { \sqrt { 2 \Lambda _ { + } ( \Lambda _ { + } - \frac { \hbar { \alpha } p _ { + } } { m } ) } } \left [ \begin{array} { c c } 2 f \Delta E \\ \Lambda _ { + } - \frac { \hbar { \alpha } p _ { + } } { m } \\ \end{array} \right ] , \quad \text {now } r e s v e c { \Lambda _ { + } } { \Lambda _ { - } }$$

and

$$u _ { - } = \frac { C _ { - } } { \sqrt { | p _ { - } + \hbar { \alpha } | } } \frac { 1 } { \sqrt { 2 \Lambda _ { - } ( \Lambda _ { - } + \frac { \hbar { \alpha } p _ { - } } { m } ) } } \left [ \begin{array} { c c } - \Lambda _ { - } - \frac { \hbar { \alpha } p _ { - } } { m } \\ 2 f \Delta E \\ \end{array} \right ] , \quad \text {with} \ \Omega \quad \text {while} \quad \\$$

where Λ ± = √ (2 f ∆ E ) 2 +( ℏ αp ± m ) 2 and C ± are normalization constants.

As we have assumed E ≫ ℏ 2 α 2 / (2 m ), which implies p ± ≫ ℏ α , the difference between | p + | and | p -| can be neglected. The primary distinction between φ + and φ -thus lies in their spinor components u ± . The evolution of u ± can be visualized through the phase and amplitude of ψ ± = u ± · [( | + 〉 n 1 n 2 , 0) T + (0 , |-〉 n 1 n 2 ) T ] within the cross section. We choose δ = 0 . 02, ω = τ = 0 . 02 /a 0 , where a 0 is the characteristic size of the cross section, and f = sin(2 πs/s 0 ), with s 0 denoting the total length of the tube. Within the degenerate subspace corresponding to n 1 = 1 and n 2 = 2, we plot the phase and amplitude evolution of ψ + in Fig. 2.

FIG. 2. Evolution of the state ψ + in the tube's cross section for n 1 = 1 and n 2 = 2. (a) Phase evolution. (b) Amplitude evolution.

<!-- image -->

At s = 0, where the potential vanishes, the phase profile of | + 〉 12 is trisected symmetrically (Fig. 2(a)), and the amplitude distribution exhibits square symmetry (Fig. 2(b)), reflecting the degeneracy of the energy levels. As the propagation distance s increases, the phase distribution gradually transitions from a trisected to a bisected pattern. Between s = s 0 / 16 and s = 7 s 0 / 16, the phase remains stable, and the amplitude distribution shifts from square to a bifurcated form. Approaching s = s 0 / 2, as the influence of the potential diminishes, the phase begins to revert to a trisected distribution, and the amplitude recovers its square symmetry. Beyond s = s 0 / 2, the phase exhibits a π jump, and the amplitude abruptly transitions again to a bifurcated state, though now rotated by π/ 2 compared to the configuration observed at s = s 0 / 4. From s = s 0 / 2 to s = s 0 , the phase and amplitude evolve in a manner similar to the first half of the propagation. A comparison between the expressions for u + and u -reveals that the phase associated with u -differs from that of u + by approximately π/ 2, while their evolutionary behaviors remain similar.

Treating f and ω as slowly varying parameters and considering the Hamiltonian as a two-level system, we can approximately derive the quantum geometric tensor Q µν in the parameter space ( ω, f ),

$$Q _ { \mu \nu } = g _ { \mu \nu } - \frac { i } { 2 } F _ { \mu \nu } ,$$

where the Riemannian metric is given by

$$\lim i t s _ { \substack { \min \text { the } \\ 0 2 / a _ { 0 } , \\ \text {section} , } } \ g _ { \mu \nu } = \frac { 1 } { \Lambda ^ { 2 } } \left [ \begin{array} { c c } B ^ { 2 } ( p ^ { 2 } \sin ^ { 2 } 2 \varphi + \hbar { ^ } { 2 } \dot { \varphi } ^ { 2 } \cos ^ { 2 } 2 \varphi ) & - \frac { B p \Delta E } { 2 } \sin 4 \varphi \\ - \frac { B p \Delta E } { 2 } \sin 4 \varphi & \Delta E ^ { 2 } \cos ^ { 2 } 2 \varphi \end{array} \right ] ,$$

and the Berry curvature is

$$F _ { \mu \nu } = \frac { 1 } { \Lambda ^ { 2 } } \left [ \begin{array} { c c c } 0 & - 2 \Delta E B \dot { h } \dot { \varphi } \cos ^ { 2 } 2 \varphi \\ 0 & 0 \\ \end{array} \right ] , \quad \text {distinct} \\ \intertext { f o r } \text {with } R = \frac { h } { } \left [ \begin{array} { c c c } 0 & - 2 \Delta E B \dot { h } \dot { \varphi } \cos ^ { 2 } 2 \varphi \\ 0 & 0 \\ \end{array} \right ] , \quad \text {t i n } \text {if } \frac { \Lambda r } { 2 } \left [ \begin{array} { c c c } 5 3 \\ 5 3 \\ \end{array} \right ] \quad \text {distinct}$$

with B = ℏ 2 m 〈 L 〉 n 1 n 2 . In this derivation, we have used the approximations | p + | ≈ | p -| = p and Λ + ≈ Λ -= Λ. We have also define cos ϕ = 2 f ∆ E √ 2Λ(Λ -ℏ αp m ) and sin ϕ =

$$\frac { \Lambda - \frac { h \alpha p } { m } } { \sqrt { 2 \Lambda ( \Lambda - \frac { h \alpha p } { m } ) } } . \\$$

It is noted that the metric g µν may exhibit singular behavior when ϕ approaches 0 or π/ 2, which occurs as the quantum state becomes degenerate. The presence of off-diagonal elements indicates a non-trivial coupling between the parameters ω and f . The existence of the Berry curvature implies that during an adiabatic cyclic evolution in parameter space, the system accumulates a geometric phase, whose value is related to the integral of the curvature over the enclosed area.

## V. CONCLUSION

In this work, we have systematically investigated the effective quantum dynamics of a particle confined in a twisted tube with a cross section subject to linear transformations along the axial direction. By extending the thin-layer procedure to adapted curvilinear coordinates, we derived a general effective Hamiltonian that incorporates both geometric effects and contributions induced by the slight transformations.

- [1] P. ˇ Svanˇ cara, P. Smaniotto, L. Solidoro, J. F. MacDonald, S. Patrick, R. Gregory, C. F. Barenghi, and S. Weinfurtner, Nature 628 , 66 (2024).
- [2] [R. Bekenstein, Nature Photon. 11 (2017).](https://doi.org/10.1038/s41566-017-0008-0)
- [3] A. G. Pogosov, A. A. Shevyrin, D. A. Pokhabov, E. Y. Zhdanov, and S. Kumar, Journal of Physics: Condensed Matter 34 , 263001 (2022).
- [4] G. Lilian, L. Laurent, L. Guillaume, W. Benoit, and A. Benjamin, Communications Chemistry 5 (2022).
- [5] P. Gentile, M. Cuoco, O. M. Volkov, Z.-J. Ying, I. J. Vera-Marun, D. Makarov, and C. Ortix, Nature Electronics 5 , 551 (2022).
- [6] V. Harish, M. M. Ansari, D. Tewari, M. Gaur, A. B. Yadav, M.-L. Garc´ ıa-Betancourt, F. M. Abdel-Haleem, M. Bechelany, and A. Barhoum, Nanomaterials 12 (2022).
- [7] L. Wu, Z. Hu, L. Liang, R. Hu, J. Wang, and L. Yu, Nature Communications 16 , 965 (2025).
- [8] Y. Shao, M. Pala, H. Tang, B. Wang, J. Li, D. Esseni, and J. A. del Alamo, Nature Electronics 8 , 157 (2025).
- [9] P. Makushko, S. Kovalev, Y. Zabila, I. Ilyakov, A. Ponomaryov, A. Arshad, G. L. Prajapati, T. V. De Oliveira, J.-C. Deinert, P. Chekhonin, et al. , Nature Electronics 7 ,

Our analysis demonstrates that three different linear transformations, namely rotation, scaling, and shearing, distinctly shape the effective quantum behavior. Rotation introduces a geometric gauge field coupled to angular momentum, while scaling and shearing produce additional potential terms. Notably, square cross sections exhibit transformation induced energy level splitting, in contrast to circular ones, which remain invariant under such mode-mixing effects. Through a concrete example involving simultaneous rotation and squeezing, we further demonstrated how geometric transformations can lead to chirality-dependent energy branches and nontrivial phase evolution in degenerate subspaces. The computed quantum geometric tensor offers deeper insight into the parameter sensitivity and Berry curvature effects in such constrained systems.

These findings not only advance our understanding of deformation induced quantum phenomena in lowdimensional and curved structures but also suggest practical strategies for designing nanoscale waveguides with tailored spectral and transport properties. The methodology and conclusions presented in this work are also applicable to other one-dimensional scalar wave systems, such as scalar optical waveguides and acoustic wave systems.

## ACKNOWLEDGMENTS

This work is supported in part by the National Natural Science Foundation of China (under Grants No. 12104239), the Natural Science Foundation of Jiangsu Province (under Grant No. BK20210581). M. Y. L is supported by the Jiangxi Provincial Natural Science Foundation with Grant No. 20224BAB211020.

[207 (2024).](https://doi.org/10.1038/s41928-024-01118-y)

- [10] S. Ruiz-G´ omez, C. Abert, P. Morales-Fern´ andez, C. Fern´ andez-Gonz´ alez, S. Koraltan, L. Danesi, D. Suess, M. Varela, G. S´ anchez-Santolino, N. Bagu´ es, et al. , Nature Communications 16 , 7422 (2025).
- [11] H. Jensen and H. Koppe, Ann. Phys. 63 , 586 (1971).
- [12] [R. C. T. da Costa, Phys. Rev. A 23 , 1982 (1981).](http://dx.doi.org/10.1103/PhysRevA.23.1982)
- [13] A. Szameit, F. Dreisow, M. Heinrich, R. Keil, S. Nolte, A. T¨ unnermann, and S. Longhi, Phys. Rev. Lett. 104 , 150403 (2010).
- [14] C. Ortix, S. Kiravittaya, O. G. Schmidt, and J. van den Brink, Phys. Rev. B 84 , 045438 (2011).
- [15] Y.-L. Wang, H. Jiang, and H.-S. Zong, Phys. Rev. A 96 , 022116 (2017).
- [16] M. Burgess and B. Jensen, Phys. Rev. A 48 , 1861 (1993).
- [17] F. Brandt and J. S´ anchez-Monroy, Phys. Lett. A 380 , 3036 (2016).
- [18] M. V. Entin and L. I. Magarill, Phys. Rev. B 64 , 085330 (2001).
- [19] J.-Y. Chang, J.-S. Wu, and C.-R. Chang, Phys. Rev. B 87 , 174413 (2013).
- [20] G.-H. Liang, Y.-L. Wang, M.-Y. Lai, H. Liu, H.-S. Zong, and S.-N. Zhu, Phys. Rev. A 98 , 062112 (2018).

- [21] [S. Batz and U. Peschel, Phys. Rev. A 78 , 043821 (2008).](http://dx.doi.org/10.1103/PhysRevA.78.043821)
- [22] G. Ferrari and G. Cuoghi, Phys. Rev. Lett. 100 , 230403 (2008).
- [23] Y.-L. Wang, L. Du, C.-T. Xu, X.-J. Liu, and H.-S. Zong, Phys. Rev. A 90 , 042117 (2014).
- [24] P. Ouyang, V. Mohta, and R. Jaffe, Ann. Phys. 275 , 297 (1999).
- [25] [C. Ortix, Phys. Rev. B 91 , 245412 (2015).](http://dx.doi.org/10.1103/PhysRevB.91.245412)
- [26] M.-Y. Lai, Y.-L. Wang, G.-H. Liang, F. Wang, and H.-S. Zong, Phys. Rev. A 97 , 033843 (2018).
- [27] M.-Y. Lai, Y.-L. Wang, G.-H. Liang, and H.-S. Zong, Phys. Rev. A 100 , 033825 (2019).
- [28] P. Maraner and C. Destri, Mod. Phys. Lett. A 08 , 861 (1993).
- [29] [P. Maraner, J. Phys. A: Math. Gen. 28 , 2939 (1995).](http://dx.doi.org/10.1088/0305-4470/28/10/021)
- [30] [P. Maraner, Ann. Phys. 246 , 325 (1996).](http://dx.doi.org/https://doi.org/10.1006/aphy.1996.0029)
- [31] K. Fujii, N. Ogawa, S. Uchiyama, and N. M. Chepilko, Int. J. Mod. Phys. A 12 , 5235 (1997).
- [32] P. Schuster and R. Jaffe, Ann. Phys. 307 , 132 (2003).
- [33] S. Takagi and T. Tanzawa, Progress of Theoretical Physics 87 , 561 (1992).
- [34] M. Parto, H. Lopez-Aviles, J. E. Antonio-Lopez, M. Khajavikhan, R. Amezcua-Correa, and D. N. Christodoulides, Science Advances 5 , eaau8135 (2019).
- [35] G.-H. Liang and M.-Y. Lai, Phys. Rev. A 107 , 022213 (2023).
- [36] G.-H. Liang, A.-G. Mei, S.-S. Xu, M.-Y. Lai, and H. Zhao, Annals of Physics 481 , 170144 (2025).
- [37] G.-H. Liang and P.-L. Yin, Chinese Physics B 33 , 020201 (2024).
- [38] G. Farin and D. Hansford, Practical linear algebra: a geometry toolbox (Chapman and Hall/CRC, 2021).
- [39] R. Cheng, arXiv preprint arXiv:1012.1337 (2010).
- [40] Y.-Q. Ma, S. Chen, H. Fan, and W.-M. Liu, Phys. Rev. B 81 , 245129 (2010).
- [41] A. Gianfrate, O. Bleu, L. Dominici, V. Ardizzone, M. De Giorgi, D. Ballarini, G. Lerario, K. West, L. Pfeiffer, D. Solnyshkov, et al. , Nature 578 , 381 (2020).
- [42] M. Kang, S. Kim, Y. Qian, P. M. Neves, L. Ye, J. Jung, D. Puntel, F. Mazzola, S. Fang, C. Jozwiak, et al. , Nature Physics 21 , 110 (2025).