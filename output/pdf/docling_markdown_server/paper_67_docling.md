## The multimode conditional quantum Entropy Power Inequality and the squashed entanglement of the multimode extreme bosonic Gaussian channels

Alessandro Falco and Giacomo De Palma

Abstract -We prove the multimode conditional quantum Entropy Power Inequality for bosonic quantum systems. This inequality determines the minimum conditional von Neumann entropy of the output of the most general linear mixing of bosonic quantum modes among all the input states of the modes with given conditional entropies. Bosonic quantum systems constitute the mathematical model for the electromagnetic radiation in the quantum regime, which provides the most promising platform for quantum communication and quantum key distribution. We apply our multimode conditional quantum Entropy Power Inequality to determine new lower bounds to the squashed entanglement of a large family of bosonic Gaussian states. The squashed entanglement is one of the main entanglement measures in quantum communication theory, providing the best known upper bound to the distillable key. Exploiting this result, we determine a new lower bound to the squashed entanglement of the multimode bosonic Gaussian channels that are extreme, i.e. , that cannot be decomposed as a non-trivial convex combination of quantum channels. The squashed entanglement of a quantum channel provides an upper bound to its secret-key capacity, i.e. , the capacity to generate a secret key shared between the sender and the receiver. Lower bounds to the squashed entanglement are notoriously hard to prove. Our results contribute to break this barrier and will stimulate further research in the field of quantum communication with bosonic quantum systems.

Index Terms -Bosonic Gaussian channels, continuous variables, Entropy Power Inequality, squashed entanglement.

## I. INTRODUCTION

T HE Shannon differential entropy of a random variable X with values in R n and probability density p ( x ) d n x is [1]

$$S ( X ) \coloneqq - \int _ { \mathbb { R } ^ { n } } \ln ( p ( x ) ) \, d p ( x ) \, , & & ( 1 ) \\ \intertext { s t a n t i f o w s } \intertext { c o n t i f o w s } \intertext { a n d p o w s } & = \intertext { s t h e r } \intertext { o n t i f o w s } & = \intertext { s t h e r } \intertext { o n t i f o w s }$$

and quantifies the noise or the information contained in X . The classical Entropy Power Inequality (EPI) [2]-[4] determines the minimum Shannon differential entropy of the sum of two independent random variables X 1 and X 2 with values in R n and given Shannon differential entropies:

$$\exp \left ( \frac { 2 \, S ( X _ { 1 } + X _ { 2 } ) } { n } \right ) \geq \exp \left ( \frac { 2 \, S ( X _ { 1 } ) } { n } \right ) + \exp \left ( \frac { 2 \, S ( X _ { 2 } ) } { n } \right ) , \quad \text {quantum} \\ \quad \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \$$

Alessandro Falco was with the Scuola Normale Superiore, 56127 Pisa, Italy. He is now with the Institute for Quantum Inspired and Quantum Optimization, Technische Universität Hamburg, Germany and also with the Quantum Research Centre, Technology Innovation Institute, Abu Dhabi, United Arab Emirates (e-mail: alessandro.falco@sns.it).

Giacomo De Palma is with the Department of Mathematics, University of Bologna, Bologna, Italy (e-mail: giacomo.depalma@unibo.it).

This paper was presented in part at Quantum Information Processing (QIP) 2024 and Beyond IID in Information Theory 12 (2024).

and is a fundamental element of classical information theory [1]. For any random variable X with values in R n and any invertible M ∈ R n × n we have

$$S ( M X ) = S ( X ) + \frac { 1 } { 2 } \ln ( \det ( M ) ) \, . \quad \quad ( 3 ) \\$$

Let X 1 , . . . , X K be independent random variables taking values in R n , and let M 1 , . . . ,M K ∈ R n × n . Let us consider the linear combination

$$Y \coloneqq \sum _ { k = 1 } ^ { K } M _ { k } \, X _ { k } \, .$$

The property (3) implies the following multimode generalization of the EPI (2):

$$\begin{array} { c c } \text {n} & \exp \left ( \frac { 2 \, S ( Y ) } { n } \right ) \geq \sum _ { k = 1 } ^ { K } | \det ( M _ { k } ) | ^ { \frac { 2 } { n } } \exp \left ( \frac { 2 \, S ( X _ { k } ) } { n } \right ) . \quad ( 5 ) \\ \text {r} & L \text {et. now } Z \text { be an arbitrary random variable and let} \end{array}$$

Let now Z be an arbitrary random variable, and let X 1 , . . . , X K be random variables conditionally independent given Z and with values in R n . The entropy of the random variable X conditioned on the random variable Z is the expectation value with respect to Z of the entropy of X given the value of Z :

$$S ( X | Z ) = \int \, S ( X | Z = z ) \, d p ( z ) \, . \\ , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, , \, ,$$

Jensen's inequality implies the following conditional version of the EPI (5):

$$x \text { is } & \quad \exp \left ( \frac { 2 \, S ( Y | Z ) } { n } \right ) \geq \sum _ { k = 1 } ^ { K } | \det ( M _ { k } ) | ^ { \frac { 2 } { n } } \exp \left ( \frac { 2 \, S ( X _ { k } | Z ) } { n } \right ) . \ \ ( 7 ) \\ \text { } & \quad \text {The first result of this paper is to prove a quantum general} .$$

The first result of this paper is to prove a quantum generalization of the EPI (7). The quantum counterpart of probability measures are quantum states, which are positive-semidefinite linear operators with unit trace acting on the Hilbert space of a quantum system. The counterpart of the probability measures on R n with even n are the states of a bosonic quantum system with m = n / 2 modes, and the counterpart of the coordinates of R n are self-adjoint linear operators called quadratures. Bosonic quantum systems [5]-[9], model electromagnetic waves in the quantum regime. Electromagnetic waves traveling through optical fibers or free space provide the most promising platform for quantum communication and quantum key distribution [10]. Bosonic quantum systems then play a key role in quantum communication and quantum cryptography and provide the model to determine the maximum communication and key distribution rates achievable in principle by quantum communication devices. The quantum counterpart of the linear combination (4) is a symplectic unitary operation, which implements a symplectic linear redefinition of the quadratures. Symplectic unitary operations are the fundamental elements of quantum optics and model the attenuation and the amplification of electromagnetic signals. The quantum counterpart of the Shannon differential entropy is the von Neumann entropy of a quantum state [5], [11]

$$S ( \hat { \rho } ) & \colon = - \text {tr} \left [ \hat { \rho } \ln ( \hat { \rho } ) \right ] . & & ( 8 ) \quad _ { A \text { and } } \\$$

Let A 1 , . . . , A K be m -mode bosonic quantum systems such that each A k has quadratures ˆ R ( k ) 1 , . . . , ˆ R ( k ) 2 m . Let M 1 , . . . , M K ∈ R 2 m × 2 m such that the rectangular matrix ( M 1 . . .M K ) constitutes the first 2 m rows of the symplectic matrix S ∈ Sp ( 2 Km, R ) . Let ˆ U be the unitary operator that implements S , i.e. , such that

$$\hat { U } ^ { \dagger } \, \hat { R } _ { i } ^ { ( 1 ) } \, \hat { U } = \sum _ { k = 1 } ^ { K } \sum _ { j = 1 } ^ { 2 m } ( M _ { k } ) _ { i j } \, \hat { R } _ { j } ^ { ( k ) } \, , \quad i = 1 , \dots , \, 2 \, m \, . \quad ( 9 ) \quad \text {One of} \quad \begin{matrix} 0 & 0 \\ 0 & 0 \end{matrix} \\ \quad \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \$$

Let M be an arbitrary quantum system. Let us consider a joint quantum input state ˆ ρ A 1 ...A K M such that A 1 . . . A K are conditionally independent given M , i.e. , such that

$$S ( A _ { 1 } \dots A _ { K } | M ) = \sum _ { k = 1 } ^ { K } S ( A _ { k } | M ) \, , \quad ( 1 0 ) \quad \begin{array} { c c } \text {know} & \text { } \\ \text { } & \text { } \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \text { } & \text { } \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \text { } & \text { } \\ \text { } & \text { } \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \text { } & \text { } \\ \text { } & \text { } \\ \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \text { } & \text { } \\ \text { } & \text { } \\ \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \text { } & \text { } \\ \text { } & \text { } \\ \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \text { } & \text { } \\ \text { } & \text { } \\ \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \text { } & \text { } \\ \text { } & \text { } \\ \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \text { } & \text { } \\ \text { } & \text { } \\ \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \text { } & \text { } \\ \text { } & \text { } \\ \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \text { } & \text { } \\ \text { } & \text { } \\ \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \text { } & \text { } \\ \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \text { } & \text { } \\ \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \text { } & \text { } \\ \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \end{array} \quad \begin{array} { c c } \text { } & \text { } \\ \text { } & \text { } \\ \end{array} \$$

where

$$S ( X | M ) \coloneqq S ( X M ) - S ( M ) & & ( 1 1 ) & \quad \text {are } \, \mathbf n \\ \ddots & \quad \, \mathbf n \\ \mathbf r \colon & \quad \, \mathbf n \\$$

is the conditional quantum entropy, and let us define the output state

ˆ ρ BM = Tr A 2 ...A K [( ˆ U ⊗ ˆ ✶ M ) ˆ ρ A 1 ...A K M ( ˆ U † ⊗ ˆ ✶ M )] , (12) where we denote with B the bosonic quantum system A 1 after the application of ˆ U . The multimode conditional quantum EPI determines a lower bound to the conditional quantum entropy of the output among all the input states as above with given conditional quantum entropies:

$$& \exp \left ( \frac { S ( B | M ) } { m } \right ) \geq \sum _ { k = 1 } ^ { K } | \det ( M _ { k } ) | ^ { \frac { 1 } { m } } \exp \left ( \frac { S ( A _ { k } | M ) } { m } \right ) . \quad ( 1 3 ) \\ & \text {The quantum FPI has been first proved in the unconditionally   where   }$$

The quantum EPI has been first proved in the unconditional case ( i.e. , when M is not present) when ˆ U implements the 50 ∶ 50 beamsplitter [12], [13] and has later been extended to any beamsplitter and amplifier [14] and to the most general symplectic unitary transformation [15], [16]. The conditional generalization of the quantum EPI for the beamsplitter and the amplifier has been conjectured in [17] and proved in [18], [19]. The conditional generalization of the EPI for arbitrary symplectic unitary transformations was still an open conjecture, which is settled by this paper. While in the classical setting the multimode conditional EPI (7) is an easy consequence of the EPI (2), in the quantum setting the generalization is highly nontrivial and requires to rebuild the proof from scratch.

We apply the multimode conditional quantum EPI to determine lower bounds to the squashed entanglement of any bipartite bosonic Gaussian state whose covariance matrix has half of the symplectic eigenvalues equal to 1 / 2 . Furthermore, we apply the above bounds to determine lower bounds to the squashed entanglement of any multimode extreme bosonic Gaussian channel, i.e. , any multimode bosonic Gaussian channel that cannot be expressed as a nontrivial convex combination of quantum channels.

The squashed entanglement of a bipartite quantum state ˆ ρ AB is the infimum over all its possible extensions ˆ ρ ABR of half of the quantum mutual information between the quantum systems A and B conditioned on the quantum system R [20]-[28]:

$$\begin{array} { c c c } { { \text {systems} } } & { { E _ { s q } ( \hat { \rho } _ { A B } ) = \frac { 1 } { 2 } \inf _ { \hat { \rho } _ { A B R } } \left \{ I ( A \colon B | R ) _ { \hat { \rho } _ { A B R } } \colon \text {tr} _ { R } \hat { \rho } _ { A B R } = \hat { \rho } _ { A B } \right \} , } } \\ { { \text {matrix} } } & { { \quad } } \\ { { \text {matrix} } } & { { \quad } } \end{array}$$

where the conditional quantum mutual information is defined as [11]

$$I ( A \colon B | R ) = S ( A | R ) + S ( B | R ) - S ( A B | R ) \, . \\ \\ O _ { 0 } = S ( A ) \cdot \dot { S } ( A ) + S ( B ) | 0 |$$

One of the main properties of squashed entanglement is its additivity for tensor products of states [26, Proposition 4]. The squashed entanglement is one of the two main entanglement measures in quantum communication theory: together with the relative entropy of entanglement [29], [30], it provides the best known upper bound to the length of a shared secret key that can be generated by two parties holding many copies of the quantum state [26], [31]-[33]. Moreover, it has applications in recoverability theory [34], [35] and multiparty information theory [36]-[38]. Lower bounds to the squashed entanglement are notoriously difficult to prove, since the optimization in (14) over all the possible extensions of the quantum state is almost never analytically treatable. The multimode conditional quantum EPI allows us to overcome the difficulty.

Any entanglement measure for quantum states can be extended to quantum channels defining it as the maximum entanglement achievable between sender and receiver. The relative entropy of entanglement of several quantum channels has been determined in [39]. The squashed entanglement of a quantum channel Φ [40] is the maximum squashed entanglement achievable between sender and receiver:

$$E _ { s q } ( \Phi ) = \sup _ { \hat { \rho } _ { A B } } E _ { s q } \left ( ( 1 _ { A } \otimes \Phi ) ( \hat { \rho } _ { A B } ) \right ) , \quad ( 1 6 ) \\ \text {here the sender generates the bipartite quantum state } \hat { \rho } _ { A B } , \\ \text {eps the quantum system } A \text { and sends the quantum system}$$

where the sender generates the bipartite quantum state ˆ ρ AB , keeps the quantum system A and sends the quantum system B to the receiver through Φ . Similarly to what happens for the states, the squashed entanglement is additive for the tensor product of channels [40, Corollary 8]. In the same way as the squashed entanglement of a quantum state is an upper bound to the distillable key of the state, the squashed entanglement of a quantum channel is an upper bound to the capacity of the channel to generate a secret key shared between sender and receiver [40], [41]. The results of this paper significantly extends the results of Ref. [42], where the squashed entanglement of the noiseless bosonic Gaussian attenuator and amplifier have been determined.

The paper is structured as follows. In Section II we present bosonic quantum systems. In Section III we prove the multimode conditional quantum Entropy Power Inequality. In Section IV we apply such inequality to determine new lower bounds to the squashed entanglement of a large family of bosonic Gaussian states. In Section V, we provide a theoretical method for finding lower and upper bounds to the multimode extreme bosonic Gaussian channels, i.e. , the bosonic Gaussian channels that cannot be decomposed as non-trivial convex combinations of quantum channels. In Section VI we show a numerical example for the calculation of upper and lower bounds to the squashed entanglement of a given extremal bosonic Gaussian channel. We discuss our results in Section VII. Appendix A contains some results used in the main text, while Appendix B contains the proofs of the auxiliary lemmas. Lastly, in Appendix C, we report some numerical simulations of the squashed entanglement bounds of a given multimode extreme bosonic Gaussian channel.

## II. BOSONIC QUANTUM SYSTEMS

In this section we briefly present bosonic quantum systems. For more details, the reader can refer to the books [43], [44] and [5, Chapter 12]. A one-mode bosonic quantum system is the mathematical model for a harmonic oscillator or for one mode of the electromagnetic radiation. An n -mode bosonic quantum system is the union of n one-mode bosonic quantum systems, and its Hilbert space is the n -th tensor power of the Hilbert space of a one-mode bosonic quantum system. The Hilbert space of a n -mode bosonic quantum system is the irreducible representation of the canonical commutation relations

$$[ \hat { Q } _ { j } , \hat { Q } _ { k } ] & = [ \hat { P } _ { j } , \hat { P } _ { k } ] = 0 \, , \quad [ \hat { Q } _ { j } , \hat { P } _ { k } ] = i \delta _ { j k } \hat { \mathbb { I } } \, , \quad ( 1 7 ) \quad \text {and} \\ \text {for } j , k \, = \, 1 , \dots , n , \text { where } \hat { Q } _ { j } \text { and } \hat { P } _ { j } \text { are the quadrature } \\ o p e r a t i o n s , \text { which for the harmonic oscillator represent the }$$

for j, k = 1 , . . . , n , where ˆ Q j and ˆ P j are the quadrature operators , which for the harmonic oscillator represent the position and momentum operators. Defining the vector

$$\hat { R } & = \left ( \hat { Q } _ { 1 } , \hat { P } _ { 1 } , \dots , \hat { Q } _ { n } , \hat { P } _ { n } \right ) , & & \text { of a } \hat { R } \\ \hat { \hat { R } } & = \hat { \hat { Q } } _ { 1 } , \hat { \hat { P } } _ { 1 } , \dots , \hat { Q } _ { n } , \hat { P } _ { n } \right ) , & & \text { of a } \hat { \hat { R } } \\$$

where ˆ R 2 k -1 = ˆ Q k , ˆ R 2 k = ˆ P k , for k = 1 , . . . , n , Equation (17) becomes

$$[ \hat { R } _ { i } , \hat { R } _ { j } ] & = i \Delta _ { i j } \hat { \mathbb { I } } \, , \\ , 2 n , \, \text {where } \Delta _ { i j } \, \text { are the entries of the matrix} \\ & \quad n \, \left ( \, 0 \, , \, 1 \right )$$

for i, j = 1 , . . . , 2 n , where ∆ ij are the entries of the matrix

$$\Delta = \bigoplus _ { k = 1 } ^ { n } \begin{pmatrix} 0 & 1 \\ - 1 & 0 \end{pmatrix} , \quad \text {the} \ \sigma ( 0 ) \quad \text {the} \ \sigma ( 2 ) \\ \intertext { a n s . s y m p l e c t i c f o r m . $ M o r $ g e r a l l y . a s y m _ { 2 } . } \sigma ( \hat { \rho } ) = \sigma ( \hat { \rho } )$$

which is known as symplectic form . More generally, a symplectic form is any antisymmetric and invertible matrix ∆ ′ . In fact, there always exists a matrix M such that M ∆ ′ M T = ∆ , the canonical form. The Hamiltonian that counts the number of excitations or photons is

where

$$\hat { H } = \sum _ { i = 1 } ^ { n } \hat { a } _ { i } ^ { \dagger } \hat { a } _ { i } = \sum _ { k = 1 } ^ { 2 n } \left ( \hat { R } _ { k } \right ) ^ { 2 } - \frac { n } { 2 } \hat { \mathbb { I } } \, , \quad \ \ ( 2 1 ) \quad \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \$$

$$\hat { a } _ { i } = \frac { \hat { Q } _ { i } + i \hat { P } _ { i } } { \sqrt { 2 } } \quad ( 2 2 ) \quad R e m$$

is the ladder operator. The vector annihilated by ˆ a is the vacuum and is denoted by ∣ 0 ⟩ .

Definition II.1 (displacement operator) . Given a vector r ∈ R 2 n , the displacement operator of parameter r is defined as

$$\hat { D } _ { \mathbf r } = \exp ( i \mathbf r ^ { T } \Delta ^ { - 1 } \hat { R } ) \, . \\$$

Observation II.2 (unitarity of ˆ D r ) . Since r T ∆ -1 ˆ R is a selfadjoint operator, ˆ D r is unitary and in particular it holds

$$\hat { D } _ { r } ^ { \dagger } = \hat { D } _ { r } ^ { - 1 } = \hat { D } _ { - r } \, . \\$$

The name 'displacement operator' is due to the following

Proposition II.3. In Heisenberg's representation it holds

ˆ D † r ˆ R ˆ D r = ˆ R + r ˆ ✶ . (25) For regularity reasons, in this paper we will consider only quantum states with finite average energy. We stress that such restriction is not relevant from an experimental perspective, since any quantum state that can be realized in an actual experiment must have finite average energy. Formally, we have the following definition:

Definition II.4. (finite average energy) Let ˆ ρ be a state of an n -mode bosonic quantum system with quadratures ˆ R 1 , . . . , ˆ R 2 n , and let

$$\hat { \rho } = \sum _ { k = 0 } ^ { + \infty } p _ { k } | \psi _ { k } \rangle \langle \psi _ { k } | \\ \text {composition of } \hat { \rho } \ \hat { \rho } _ { k } \text { with } \text {aggregation } \{ n \colon \hat { n } \subset \mathbb { N } \}$$

be an eigendecomposition of ˆ ρ with eigenvalues { p k ∶ k ∈ N } and eigenvectors {∣ ψ k ⟩ ∶ k ∈ N } . We say that ˆ ρ has finite average energy if each ∣ ψ k ⟩ belongs to the domain of each ˆ R i and

$$\sum _ { k = 0 } ^ { + \infty } p _ { k } \| \hat { R } _ { i } | \psi _ { k } \rangle \| ^ { 2 } & < + \infty \, , \quad \forall \, i = 1 , \dots , 2 n \, . \\ \intertext { l e c h a n t u m } \, T h e q u u n t y c o u n t e r p a r t s \, o f t h e f i n t a n d s e r d \, m o m p e s$$

The quantum counterparts of the first and second moments of a random variable with values in R n are defined as follows:

Definition II.5. (first moments) Given a quantum state ˆ ρ with finite average energy, the vector of the fi rst moments ¯ r ( ˆ ρ ) is defined as the expectation value of the quadratures ˆ R ,

$$\bar { r } ( \hat { \rho } ) = & \text {tr} [ \hat { \rho } \hat { R } ] \, . \\$$

Definition II.6. (second moments) Given a quantum state ˆ ρ , the covariance matrix σ ( ˆ ρ ) is defined as

$$a \, \text {sym} - \ \sigma ( \hat { \rho } ) _ { i j } = \frac { 1 } { 2 } \, \text {tr} \left [ \left ( \hat { R } _ { i } - \bar { r } _ { i } \right ) \hat { \rho } \left ( \hat { R } _ { j } - \bar { r } _ { j } \right ) + \left ( \hat { R } _ { j } - \bar { r } _ { j } \right ) \hat { \rho } \left ( \hat { R } _ { i } - \bar { r } _ { i } \right ) \right ] \, , \\ \text {x} \, \Delta ^ { \prime } \, \text {In} \quad \\ \text {T} \, \hat { \tau } \, \text { } \, \Delta _ { i } = \bar { \epsilon } \, \hat { \tau } \, \right )$$

where ¯ r = ¯ r ( ˆ ρ ) .

The eigenvalues of the matrix ∆ -1 σ are pure imaginary and pairwise opposite.

Definition II.7 (symplectic eigenvalues) . The symplectic eigenvalues of a real positive matrix σ are the absolute values of the eigenvalues of ∆ -1 σ .

Remark II.8 . The average number of photons of a quantum state ˆ ρ is related to its covariance matrix σ by

$$N = \frac { 1 } { 2 } \, t r \left ( \sigma - \frac { I } { 2 } \right ) \, .$$

## A. Symplectic group

Given a symplectic matrix S , i.e. , a matrix that satisfies

$$S \, \Delta \, S ^ { T } = \Delta \, , \\$$

ˆ U S is a unitary operator on the Hilbert space that applies the matrix S on the quadratures.

Proposition II.9 ( ˆ U S operator) . Given a symplectic matrix S ∈ Sp ( 2 n, R ) , there exists a unitary operator ˆ U S acting on the Hilbert space of an n -mode bosonic quantum system such that

$$\hat { U } _ { S } ^ { \dagger } \hat { R } \hat { U } _ { S } = S \hat { R } \, . \\$$

$$P r o o f . \, S e e \, [ 4 4 ] .$$

a) Properties of ¯ r and σ .: Equations (25) and (32) imply the following properties for the first and second moments ¯ r and σ . The displacement operators and the symplectic unitaries transform the first moments vector as

$$\bar { r } ( \hat { D } _ { r } \, \hat { \rho } \, \hat { D } _ { r } ^ { \dagger } ) & = \bar { r } ( \hat { \rho } ) + r \, , \quad \bar { r } ( \hat { U } _ { S } \, \hat { \rho } \, \hat { U } _ { S } ^ { \dagger } ) = S \bar { r } ( \hat { \rho } ) \, , \quad ( 3 3 ) \\ \text {bulk for the observation} \, & \quad \text {that} \, \max \,$$

while for the covariance matrix it holds

$$\sigma ( \hat { D } _ { r } \, \hat { \rho } \, \hat { D } _ { r } ^ { \dagger } ) & = \sigma ( \hat { \rho } ) \, , \quad \sigma ( \hat { U } _ { S } \, \hat { \rho } \hat { U } _ { S } ^ { \dagger } ) = S \, \sigma ( \hat { \rho } ) \, S ^ { T } , \quad ( 3 4 ) \quad \text {attnuat} \\ \text {where } r \in \mathbb { R } ^ { 2 n } \text { and } S \in S p ( 2 n , \mathbb { R } ) . & & \text {through} \\ & \text {through}$$

## B. Bosonic Gaussian states

The quantum analogue of real Gaussian probability distributions are the bosonic Gaussian states.

Definition II.10 (Gaussian states) . Bosonic Gaussian states are density operators proportional to the exponential of a quadratic Hamiltonian in the quadratures together with the projectors on its ground states. In formulae, Gaussian states can be written as

$$\hat { \rho } _ { \beta } \times & \exp \left ( - \frac { \beta } { 2 } ( \hat { R } - \bar { r } _ { 0 } ) ^ { T } h ( \hat { R } - \bar { r } _ { 0 } ) \right ) , & & \text {of the} \, \text {the} \, \text {by} \, \text {the} \, \text {probability} \, \hat { R } - \bar { r } _ { 0 } \right ) , \\ \hat { \rho } _ { 0 } = & \lim _ { \beta \to + \infty } \hat { \rho } _ { \beta } \, , & & \text {Prop} \, \sigma \\ \text {here } h \text { is a positive-definite real symmetric matrix} , & & \text {boson} \, , & & \text {2n} \, ,$$

where h is a positive-definite real symmetric matrix.

Definition II.11 (thermal states) . A thermal Gaussian state is a bosonic Gaussian state, as in Equation (35), with ¯ r 0 = 0 and h ∝ I .

Proposition II.12 (characterisation of Gaussian states) . Bosonic Gaussian states are uniquely determined by their first and second moments. In other words, given a first moment r ′ and a covariance matrix σ ′ , there exists a unique bosonic Gaussian state ˆ ρ such that ¯ r ( ˆ ρ ) = r ′ and σ ( ˆ ρ ) = σ ′ .

$$P r o o f . \, S e e \, [ 4 4 ] .$$

Proposition II.13. The von Neumann entropy of an n -mode bosonic Gaussian state is

$$S = \sum _ { k = 1 } ^ { n } g \left ( \nu _ { k } - \frac { 1 } { 2 } \right ) , & & \text {as} \ a \\ \nu _ { k } \ a r e \ t h e \ s y m p l e c t i c \ e i g e n a l u e s \ o f \ i t s \ c o v a r i - & &$$

where ν 1 , . . . , ν n are the symplectic eigenvalues of its covariance matrix and the function g is defined as

$$g ( x ) \coloneqq ( x + 1 ) \ln ( x + 1 ) - x \ln ( x ) \, .$$

$$P r o f \, \text { See [44, Equation (3.92)]} .$$

One-mode thermal Gaussian states can be written as

$$\hat { \omega } ( N ) & = \frac { 1 } { N + 1 } \left ( \frac { N } { N + 1 } \right ) ^ { \hat { a } ^ { \dagger } \hat { a } } , \\ \geq 0 \text { is the average number of photons} .$$

$$\ t r [ \hat { \omega } ( N ) \, \hat { a } ^ { \dagger } \hat { a } ] & = N \, . \\$$

where N ≥ 0 is the average number of photons:

The covariance matrix of these states is given by

$$\sigma ( \hat { \omega } ( N ) ) = \left ( N + \frac { 1 } { 2 } \right ) I _ { 2 } \, .$$

We notice that ˆ ω ( 0 ) = ∣ 0 ⟩ ⟨ 0 ∣ is the vacuum state. The von Neumann entropy of ˆ ω ( N ) is

$$\bar { r } \text { and } \quad S ( \hat { \omega } ( N ) ) = ( N + 1 ) \ln ( N + 1 ) - N \ln ( N ) = \colon g ( N ) \, .$$

## C. Bosonic Gaussian channels

Bosonic Gaussian channels are those quantum channels that map Gaussian states into Gaussian states. They play a key role in quantum communication since they model the attenuation and the noise that affect light pulses travelling through optical fibres and electromagnetic signals travelling through free space. The most important families of bosonic Gaussian channels are the beam splitter, the squeezing and the bosonic Gaussian attenuators and amplifiers. The first two are the quantum analogue of classical linear mixing of random variables and are the main transformations of quantum optics. In the physical representation, a bosonic Gaussian channel can be seen as an ancillary system, the environment, that is in a Gaussian initial state and interacts with the state of the system of interest via a quadratic Hamiltonian coupling. Such a transformation preserves the Gaussian character of the state of the system of interest. The bosonic Gaussian channels are briefly and exhaustively characterised as follows.

Proposition II.14 (bosonic Gaussian channels) . An n -mode bosonic Gaussian channels is completely characterized by two 2 n × 2 n real matrices K and α satisfying

$$\alpha \geq \pm \frac { i } { 2 } \left ( \Delta - K \, \Delta \, K ^ { T } \right ) . \\$$

Such channel acts on the moments of an n -mode input Gaussian state with vector of first moments ¯ r and covariance matrix σ as follows:

$$\bar { r } & \longmapsto K \bar { r } \, , \\ \sigma & \longmapsto K \, \sigma \, K ^ { T } + \alpha \, . \\ 4 . \, \text {Section} \, 5 . 3 \, \text {L} \, \Big | \, \Omega \, \prod \Omega$$

$$\prod \left [ \begin{array} { c c } P r o o f . \, S e e \, [ 4 4 , \, S e c t i o n \, 5 . 3 ] . \end{array} \right ] .$$

In what follows, we will refer to a bosonic Gaussian channel characterised by the matrices K and α , as in Proposition II.14, as a ( K,α ) Gaussian channel . The space of quantum channels with fixed input and output systems is convex. A prominent role is played by the following class of quantum channels.

Definition II.15 (extreme quantum channels) . A quantum channel is said to be extreme if it cannot be decomposed as a non-trivial convex combination of quantum channels [45].

The following Proposition II.16 provides an easy characterization of the extreme bosonic Gaussian channels.

Proposition II.16 (extreme bosonic Gaussian channels) . A bosonic Gaussian channel characterized by the matrices ( K,α ) , as in Proposition II.14, is extreme iff α is a minimal solution of inequality (42) .

Proof. See [45, Corollary 1] and [5, Equation (12.138)].

Remark II.17 . In other words, a ( K,α ) Gaussian channel is extreme if there is no ( K,α ′ ) Gaussian channel such that α ′ ≤ α and α ′ ≠ α . That is, if the only α ′ ∈ R 2 n × 2 n such that α ≥ α ′ ≥ ± i 2 ( ∆ -K ∆ K T ) is α ′ = α .

1) Beam-splitter and squeezing.: Let us now briefly introduce two relevant examples of extreme bosonic Gaussian channels [44]. Given the one-mode bosonic quantum systems A,B , and C,D , the beam splitter with transmissivity coefficient 0 ≤ η ≤ 1 is the mixing unitary operator ˆ U η ∶H A ⊗H B →H C ⊗H D acting on the quadratures, as in Equation (32), through the symplectic matrix

$$S _ { \eta } = \left ( \begin{matrix} \sqrt { \eta } \, I _ { 2 } & \sqrt { 1 - \eta } \, I _ { 2 } \\ - \sqrt { 1 - \eta } \, I _ { 2 } & \sqrt { \eta } \, I _ { 2 } \end{matrix} \right ) . \quad \ \ ( 4 4 ) \quad \ \ T o g e { I _ { 2 } } = 0 .$$

$$\text {returns through the symmetric matrix} & \quad \text {where} \quad \text {where} \quad \text {is the} \quad \text {n} _ { k = 1 } ^ { n } \\ S _ { \kappa } & = \begin{pmatrix} \sqrt { \kappa } \, I _ { 2 } & \sqrt { \kappa - 1 } \, Z _ { 2 } \\ \sqrt { \kappa - 1 } \, Z _ { 2 } & \sqrt { \kappa } \, I _ { 2 } \end{pmatrix} , \quad \text { (45)} \\ I _ { 2 } \text { is the } 2 \times 2 \text { identity matrix and } Z _ { 2 } \text { is the } \sigma _ { z } \text { Pauli} \quad \text {dition} \\$$

Similarly, the squeezing unitary operator ˆ U κ ∶ H A ⊗ H B → H C ⊗ H D with squeezing parameter κ &gt; 1 acts on the quadratures through the symplectic matrix

where I 2 is the 2 × 2 identity matrix and Z 2 is the σ z Pauli matrix.

## III. THE MULTIMODE ENTROPY POWER INEQUALITY

Entropic inequalities are the main tool to prove upper bounds to quantum communication rates [5], [11] and to prove the security of quantum key distribution protocols [46]. In these scenarios, a prominent role is played by entropic inequalities in the presence of quantum memory, where the entropies are conditioned on the knowledge of an external observer holding a memory quantum system.

## A. The problem

The aim of this section is to provide a proof of a new entropic inequality, the multimode conditional quantum Entropy Power Inequality for bosonic quantum systems (Theorem III.18). Let us first define the action of a quantum channel on input systems.

Definition III.1 (linear mixing of quantum modes) . Let B = ( B 1 ⋯ B K ) ∈ R 2 n × 2 Kn be a real matrix of rank 2 n formed by K blocks B i ∈ R 2 n × 2 n , satisfying the condition

Let S B ∈ Sp ( 2 Kn, R ) such that its first 2 n rows are given by B . The quantum analogue of the linear transformation (4) is given by

$$\sum _ { i = 1 } ^ { K } B _ { i } \, \Delta \, B _ { i } ^ { T } = \Delta \, . \quad \\ K n _ { \, , \, \mathbb { R } } \right ) \, \text {such that its first 2n \, rows are given by}$$

$$\hat { \rho } _ { Y } = \Phi _ { X } ^ { B } ( \hat { \rho } _ { X } ) \coloneqq \text {tr} _ { Z } \left [ \hat { U } _ { S _ { B } } \, \hat { \rho } _ { X } \, \hat { U } _ { S _ { B } } ^ { \dagger } \right ] , \quad ( 4 7 ) \ \text {entropy}$$

where ˆ U S B ∶ H X → H Y ⊗ H Z (see Proposition II.9) is an isometry between the input Hilbert space H X and the tensor product of the output Hilbert space H Y with an ancillary Hilbert space H Z , satisfying

with ˆ R X i and ˆ R Y respectively the quadratures of the systems X i and Y .

$$\hat { U } _ { S _ { B } } ^ { \dagger } \hat { R } ^ { Y } \hat { U } _ { S _ { B } } = B \hat { R } ^ { X } = \sum _ { i = 1 } ^ { K } B _ { i } \hat { R } ^ { X _ { i } } , \\ \hat { R } ^ { X _ { i } } \, \text {and} \, \hat { R } ^ { Y } \, \text {respectively} \, the \, \text {quadratures of the systems}$$

Remark III.2 . Condition (46) is necessary to preserve the canonical commutation relations and ensures the existence of S B . The isometry ˆ U S B does not necessarily conserve energy, i.e. , it can contain active elements, so that even if the input ˆ ρ X is the vacuum state on all its K modes, the output ˆ ρ Y can be a thermal state with a non-zero temperature.

Example III.3 (beam-splitter and quantum amplifier) . For K = 2 , the beam splitter with attenuation parameter 0 ≤ η ≤ 1 is easily recovered by defining

To get the quantum amplifier of parameter κ ≥ 1 , one must instead take

$$\text { } B _ { 1 } = \sqrt { \eta } \, I _ { 2 n } \, , \quad B _ { 2 } = \sqrt { 1 - \eta } \, I _ { 2 n } \, . \\ \intertext { s t a t h s c r . } \text { } \det \text { } the \text { quantum applier of parameter } \kappa > 1 \text { } \text { } \text { one must }$$

$$B _ { 1 } = \sqrt { \kappa } \, I _ { 2 n } \, , \quad B _ { 2 } = \sqrt { \kappa - 1 } \, Z _ { 2 n } \, , \\ \text {here} \, Z _ { 0 } \text { is the } n \text {-mode} \text { time} \text { reversal} \text { matrix} \text { } Z _ { 0 } \text { } \div \Xi$$

We are going to study the output system given by K conditionally independent input systems which interact through the linear mixing process given by Φ B in presence of a memory quantum system. Let { X i } i = 1 ,...,K be the n -mode input bosonic quantum systems, and let Y be the n -mode output bosonic quantum system. Let us consider a joint quantum input state ˆ ρ XM , where X = X 1 ⋯ X K is the overall input system, such that { X i } i = 1 ,...,K are conditionally independent given the memory system M , i.e. ,

where Z 2 n is the n -mode time reversal matrix Z 2 n ∶= ⊕ n k = 1 diag ( 1 , -1 ) .

$$S ( X _ { 1 } \dots X _ { K } | M ) & = \sum _ { i = 1 } ^ { K } S ( X _ { i } | M ) \, . \\ \hat { \otimes } _ { \gamma \nu } \, \underline { \epsilon } = ( \Phi _ { \nu } ^ { B } \otimes \mathbb { I } _ { \gamma \nu } ) ( \hat { \rho } _ { \gamma \nu \tau } ) \, \text {be the output state of the}$$

$$\int _ { B } \exp \left ( \frac { S ( Y | M ) _ { \hat { \rho } _ { Y } M } } { n } \right ) \geq \sum _ { i = 1 } ^ { K } b _ { i } \exp \left ( \frac { S ( X _ { i } | M ) _ { \hat { \rho } _ { X _ { i } M } } } { n } \right ) , \quad ( 5 2 ) \\ \intertext { b e r $ w h e r $ b _ { i } are constants dependent on B , }$$

Let ˆ ρ Y M = ( Φ B X ⊗ ✶ M )( ˆ ρ XM ) be the output state of the linear mixing process. The multimode conditional quantum Entropy Power Inequality determines the minimum conditional quantum entropy S ( Y ∣ M ) of the output state among all the input quantum states ˆ ρ XM as above and with given conditional quantum entropies { S ( X i ∣ M )} i = 1 ,...,K :

where b i are constants dependent on B .

a) Outline of the proof.: The proof proceeds as follows. We evolve the input system with the heat semigroup time evolution (Definition III.4). Employing the quantum de Brujin identity (Proposition III.15) and a new conditional quantum Stam inequality (Section III-D), we prove that such evolution degrades the Entropy Power Inequality. We conclude by proving that the inequality holds in the limit of infinite time via asymptotic estimates of the time scaling of the conditional entropies.

## B. Preliminary results

In this section we prove some important intermediate results that will play a key role in the proof of the multimode conditional quantum Entropy Power Inequality (MCQEPI).

Definition III.4 (heat semigroup) . The heat-semigroup time evolution is generated by the convex combination of displacement operators according to a centred Gaussian distribution with covariance matrix α . For any quantum state ˆ ρ

$$\mathcal { N } ( \alpha ) ( \hat { \rho } ) & \coloneqq \int _ { \mathbb { R } ^ { 2 n } } \hat { D } ( x ) \, \hat { \rho } \, \hat { D } ( x ) ^ { \dagger } \frac { e ^ { - \frac { 1 } { 2 } x ^ { T } \alpha ^ { - 1 } x } } { \sqrt { ( 2 \pi ) ^ { n } \det ( \alpha ) } } \, d x \, . \quad ( 5 3 ) \quad \text {as} \, \ m a t h s c r { D } ( x ) \\ \intertext { The following lemma states how the heat semigroup e v o - } \quad \text {positive}$$

The following lemma states how the heat semigroup evolution of the subsystems X i is related to the heat semigroup evolution of the overall system X .

Lemma III.5. Let X = X 1 ⋯ X K be a multipartite bosonic quantum system, where each X i is a n -mode bosonic quantum system and α = ⊕ K i = 1 α i , α i ∈ R 2 n × 2 n &gt; 0 ∀ i , a block diagonal matrix, then it holds

$$\mathcal { N } _ { X } ( \alpha ) = \bigotimes _ { i = 1 } ^ { K } \mathcal { N } _ { X _ { i } } ( \alpha _ { i } ) \, . \\$$

$$& D _ { X } ( z ) = \otimes _ { i = 1 } ^ { i } D _ { X _ { i } } ( z _ { i } ) \, \text { holds. From the definition of the heat} \quad \text {mation} . \\ & \text {semigroup, } \forall \ \hat { \rho } _ { X } \text { it holds:} \\ & \mathcal { N } _ { X } ( \alpha ) \hat { \rho } _ { X } = \mathbb { E } _ { Z } [ \hat { D } _ { X } ( \mathbb { Z } ) \hat { \rho } _ { X } \hat { D } _ { X } ^ { \dagger } ( \mathbb { Z } ) ] \\ & = \int _ { \mathbb { R } ^ { 2 K n } } \hat { D } _ { X } ( z ) \, \hat { \rho } _ { X } \, \hat { D } _ { X } ^ { \dagger } ( z ) \, e ^ { - \frac { 1 } { 2 } z ^ { T } \alpha ^ { - 1 } z } \frac { d z } { \sqrt { ( 2 \pi ) ^ { 2 K n } \det ( \alpha ) } } \\ & = \int _ { \mathbb { R } ^ { 2 K n } } \hat { D } _ { X } ( z ) \, \hat { \rho } _ { X } \, \hat { D } _ { X } ^ { \dagger } ( z ) \, e ^ { - \frac { 1 } { 2 } \sum _ { i = 1 } ^ { K } z _ { i } ^ { T } \alpha _ { i } ^ { - 1 } z _ { i } } \prod _ { i = 1 } ^ { K } \frac { d z _ { i } } { \sqrt { ( 2 \pi ) ^ { 2 n } \det ( \alpha _ { i } ) } } \\ & = \prod _ { i = 1 } ^ { K } \int _ { \mathbb { R } ^ { 2 n } } \hat { D } _ { X _ { i } } ( z _ { i } ) \, \hat { \rho } _ { X _ { i } } \, \hat { D } _ { X _ { i } } ^ { \dagger } ( z _ { i } ) \, e ^ { - \frac { 1 } { 2 } z _ { i } ^ { T } \alpha _ { i } ^ { - 1 } z _ { i } } \frac { d z _ { i } } { \sqrt { ( 2 \pi ) ^ { 2 n } \det ( \alpha _ { i } ) } } \quad \text {classical} \\ & = \bigotimes _ { i = 1 } ^ { K } \mathcal { N } _ { X _ { i } } ( \alpha _ { i } ) \hat { \rho } _ { X _ { i } } , \\ & \quad \text {where } \mathbb { Z } \text { is a classical Gaussian random variable with zero condition} \\ & \text {mean and covariance matrix} \alpha$$

Proof. Let z = ( z 1 ⋯ z K ) T , z i ∈ R 2 n ∀ i . It is easy to notice that det ( α ) = ∏ K i = 1 det ( α i ) and α -1 = ⊕ K i = 1 α -1 i . Furthermore, from the definition of displacement operator, ˆ D X ( z ) = ⊗ K i = 1 ˆ D X i ( z i ) holds. From the definition of the heat semigroup, ∀ ˆ ρ X it holds:

where Z is a classical Gaussian random variable with zero mean and covariance matrix α .

For the map defined in Equation (53) the following composition rules apply.

Lemma III.6. Let B be as in Definition III.1, for each α,β ∈ R 2 n × 2 n &gt; 0 , it holds

$$\mathcal { N } _ { X } ( \alpha ) \circ \mathcal { N } _ { X } ( \beta ) = \mathcal { N } _ { X } ( \alpha + \beta ) \, . \\ \intertext { S o _ { X } [ 4 7 } \, S o t i o n \, 2 1 } \prod \Psi = \prod \Psi$$

Proof. See [47, Section 3].

The following two lemmas describe how the transformation Φ B (Definition III.1) behaves under the heat semigroup evolution and displacements.

Lemma III.7 (compatibility with the heat semigroup) . Let B be as in Definition III.1, for each α,β ∈ R 2 n × 2 n ≥ 0 , it holds

$$\Phi _ { B } \circ \mathcal { N } _ { X } ( \alpha ) = \mathcal { N } _ { Y } ( B \, \alpha \, B ^ { T } ) \circ \Phi _ { B } \, .$$

$$P r o o f . \ S e e \ [ 4 7 , L e m m a \ 1 ] .$$

Lemma III.8 (compatibility with displacements) . For any α ∈ R 2 n × 2 n ≥ 0 and any x ∈ R 2 n ,

where ˆ D x acts on system X while ˆ D B x acts on system Y .

$$\Phi _ { B } ( \hat { D } _ { x } \cdot \hat { D } _ { x } ^ { \dagger } ) & = \hat { D } _ { B x } \, \Phi _ { B } ( \cdot ) \, \hat { D } _ { B x } ^ { \dagger } , \\ \hat { D } _ { B } & = \left ( \hat { D } _ { x } - \hat { V } _ { x } \right ) = \hat { D } _ { B x } \, \Phi _ { B } ( \cdot ) \, \hat { D } _ { B x } ^ { \dagger } , \\ \hat { D } _ { B } & = \left ( \hat { D } _ { x } - \hat { V } _ { x } \right ) = \hat { V } _ { x } \, \hat { D } _ { B }$$

$$^ { \Pi } \ P r o o f . \ S e e \ [ 4 7 , L e m m a \ 1 ] .$$

A fundamental result for the proof of the MCQEPI is the asymptotic scaling of the conditional entropy with respect to the time evolution induced by the heat semigroup with a positive definite matrix.

Proposition III.9 (asymptotic scaling of the entropy) . Let X be a n -mode bosonic quantum system, then, for any quantum state ˆ ρ XM of XM , such that S ( M ) is finite and ˆ ρ X has finite energy, and any α ∈ R 2 n × 2 n &gt; 0 , for t →+∞

$$\ a g o n a l \quad S ( X | M ) ( \mathcal { N } _ { X } ( t \alpha ) ( \hat { \rho } _ { X M } ) ) & = \frac { 1 } { 2 } \ln ( \det ( e t \alpha ) ) + \mathcal { O } \left ( \frac { 1 } { t } \right ) . \ ( 5 9 ) \\$$

Proof. See [47, Proposition 10].

## C. Quantum integral de Bruijn identity

Let us start by defining the integral version of the conditional quantum Fisher information.

Definition III.10 (integral conditional quantum Fisher information) . Let A be a n -mode bosonic quantum system, M a generic quantum system and ˆ ρ AM a quantum state of AM . For any α ∈ R 2 n × 2 n ≥ 0 , we define the quantum integral Fisher information of A conditioned on M as

$$\Delta _ { A | M } ( \hat { \rho } _ { A M } ) ( \alpha ) & \coloneqq I ( A \colon \mathbb { X } | M ) _ { \hat { \sigma } _ { A M X } } \geq 0 \, , \\ \Delta _ { A | U } ( \hat { \rho } _ { A U } ) ( 0 ) & \coloneqq 0 \, .$$

$$\Delta _ { A | M } ( \hat { \rho } _ { A M } ) ( 0 ) & \coloneqq 0 \, , \\ \intertext { b h w r a } \mathbb { W } \, i s \, e s \, \underset { \ } a l l \, C o v i s g r a n \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ } w i d e r s \, \underset { \ }$$

where X is a classical Gaussian random variable with zero mean and covariance matrix α and ˆ σ AM X is the joint quantumclassical state of AM X such that for any x ∈ R 2 n

$$\hat { \sigma } _ { A M | \mathbb { X } = \mathbb { X } } & = \hat { D } _ { A } ( \mathbb { X } ) \hat { \rho } _ { A M } \hat { D } _ { A } ( \mathbb { X } ) ^ { \dagger } \, . \\ \intertext { t h e f l o w i n g i n t u l l d e r $ \rho _ { A } \colon \rho _ { A M } \colon \hat { D } _ { A } ( \mathbb { X } ) ^ { \dagger } \, . }$$

The following integral de Bruijn identity proves that the integral Fisher information is equal to the increase in the conditional entropy induced by the heat semigroup.

Proposition III.11 (integral de Bruijn identity) . For any quantum state ˆ ρ XM of XM such that S ( M ) is finite and ˆ ρ X has finite energy any α ∈ R n × n ≥ 0 , it holds

$$h ( \alpha , \beta \in \Delta _ { X | M } ( \hat { \rho } _ { X M } ) ( \alpha ) = S ( X | M ) _ { ( \mathcal { N } _ { X } ( \alpha ) \otimes 1 _ { M } ) ( \hat { \rho } _ { X M } ) ^ { - } } S ( X | M ) _ { \hat { \rho } _ { X M } ^ { _ { M } } } . \\ ( 5 6 ) \quad P r o o f . \quad [ 4 7 , \, \text {Proposition } 2 ] .$$

We can now give the definition of the conditional quantum Fisher information.

Definition III.12 (conditional quantum Fisher information) . Let ˆ ρ XM a quantum state of XM , such that S ( M ) is finite and ˆ ρ X has finite energy. For any α ∈ R n × n ≥ 0 , the conditional quantum Fisher information of ˆ ρ XM is defined as

$$J _ { X | M } ( \hat { \rho } _ { X M } ) ( \alpha ) \coloneqq \lim _ { t \to 0 } \frac { \Delta _ { X | M } ( \hat { \rho } _ { X M } ( t \alpha ) ) } { t } \, .$$

Remark III.13 . From [47, Proposition 5], the limit in Equation (63) always exists, finite or infinite.

Lemma III.14 (linearity of the conditional quantum Fisher information) . For any quantum state ˆ ρ XM of XM , such that S ( M ) is finite and ˆ ρ X has finite energy, any α ∈ R n × n ≥ 0 and any t ≥ 0 , it holds

$$J _ { X | M } ( \hat { \rho } _ { X M } ) ( t \alpha ) & = t \, J _ { X | M } ( \hat { \rho } _ { X M } ) ( \alpha ) \, . \\ \\ \intertext { f . } \intertext { c . } [ 4 7 . 1 ] \intertext { s . } \intertext { e . }$$

$$P r o o f . \ [ 4 7 , \text { Lemma } 2 ] .$$

The following de Bruijn identity relates the conditional quantum Fisher information to the time derivative of the conditional entropy with respect to the heat semigroup time evolution [47].

Proposition III.15 (de Bruijn identity) . Let X be a n -mode bosonic quantum system and ˆ ρ XM a quantum state of XM , such that S ( M ) is finite and ˆ ρ X has finite energy. For each α ∈ R 2 n × 2 n ≥ 0 and t ∈ R , let us define ˆ ρ XM ( t ) ∶= (N X ( t α ) ⊗ ✶ M ) ˆ ρ XM . The following relation holds d d t S ( X ∣ M ) ˆ ρ XM ( t ) = J X ∣ M ( ˆ ρ XM ( t ))( α ) , (65)

where J X ∣ M ( ˆ ρ XM ( t ))( α ) is defined in Definition III.12.

$$P r o o f \, \text { See [4 7, Proposition 7]} .$$

## D. Conditional quantum Stam Inequality

The following new integral Stam inequality proves that the conditional quantum Fisher information is decreasing with respect to the application of the quantum channel Φ B (Definition III.1).

Theorem III.16 (conditional quantum Stam inequality) . Let X 1 , . . . , X K and Y be n -mode bosonic quantum systems, let X = X 1 ⋯ X K , let M a quantum system and Φ B ∶ X → Y the transformation defined in Definition III.1. Let ˆ ρ XM be a state of XM such that ˆ ρ X has finite average energy and S ( ˆ ρ M ) &lt; +∞ , and let us suppose that the systems { X i } i = 1 ,...,K are conditionally independent given M , i.e. , such that

$$S ( X _ { 1 } \dots X _ { K } | M ) & = \sum _ { k = 1 } ^ { K } S ( X _ { k } | M ) \, . & \quad ( 6 6 ) \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \$$

Then, for any set λ = { λ 1 , . . . , λ K } such that λ k = 0 if det ( B k ) = 0 and 0 ≤ λ i ≤ 1 with ∑ K i = 1 λ i = 1 , the conditional quantum linear Stam inequality holds:

$$J _ { Y | M } ( \hat { \rho } _ { Y M } ) \Big ( I _ { 2 n } ) & \leq \sum _ { i = 1 } ^ { K } J _ { X _ { i } | M } \Big ( \hat { \rho } _ { X _ { i } M } ) \Big ( \lambda _ { i } ^ { 2 } B _ { i } ^ { - 1 } B _ { i } ^ { - T } \Big ) , \quad \text {in} \ \, \text {Equ.} \\ \intertext { w h e r a } \ w h e r a \Big ( 6 ) & \quad \text {by } \exp ( 6 ) , \quad \text {in} \ \, \text {tr}$$

where

ˆ ρ Y M ∶= ( Φ B X ⊗ ✶ M ) ˆ ρ XM . (68) Proof. We will prove the following inequality for the integral conditional quantum Fisher information:

$$\Delta _ { Y | M } ( \hat { \rho } _ { Y M } ) ( t \, I _ { 2 n } ) \leq \sum _ { i = 1 } ^ { K } \Delta _ { X _ { i } | M } ( \hat { \rho } _ { X _ { i } M } ) \left ( t \, \lambda _ { i } ^ { 2 } B _ { i } ^ { - 1 } B _ { i } ^ { - T } \right ) . \\$$

The linear conditional quantum Stam inequality (67) follows taking the derivative of (69) in t = 0 . For any t ≥ 0

$$\Delta _ { Y | M } ( \hat { \rho } _ { Y M } ) ( t \, I _ { 2 n } ) = I ( Y \colon \mathbb { Z } | M ) _ { \sigma _ { Y M Z } } \, , \\ \\ \intertext { t h e r w } \Delta _ { Y | M } ( \hat { \rho } _ { Y M } ) ( t \, I _ { 2 n } ) = I ( Y \colon \mathbb { Z } | M ) _ { \sigma _ { Y M Z } } \, , \\$$

where Z is a Gaussian random variable with zero mean and covariance matrix t I 2 n and ˆ σ Y M Z is the joint quantumclassical state of Y M Z such that for any z ∈ R 2 n

$$\hat { \sigma } _ { Y M | \mathbb { Z } = \mathbb { Z } } = \hat { D } _ { Y } ( \mathbb { Z } ) \hat { \rho } _ { Y M } \hat { D } _ { Y } ^ { \dagger } ( \mathbb { Z } ) \, . \\$$

We define the joint quantum-classical state ˆ σ XM Z of XM Z such that for any z ∈ R 2 n

Applying Lemma III.8, with x = ( λ 1 B -1 1 z ⋯ λ K B -1 K z ) T , B = ( B 1 ⋯ B K ) and exploiting ∑ K i = 1 λ i = 1 , we then have that for any t ≥ 0

$$\begin{array} { r l } { \text {of the} } & { \hat { \sigma } _ { X M | \mathbb { Z } = z } } \\ { p } & { \quad = \hat { D } _ { X _ { 1 } ( \lambda _ { 1 } B _ { 1 } ^ { - 1 } z ) \cdots \hat { D } _ { X _ { K } ( \lambda _ { K } B _ { K } ^ { - 1 } z ) \hat { \rho } _ { X M } \hat { D } _ { X _ { 1 } } ^ { \dagger } ( \lambda _ { 1 } B _ { 1 } ^ { - 1 } z ) \cdots ( 7 2 ) } \\ & { \quad \cdots \hat { D } _ { X _ { K } } ^ { \dagger } ( \lambda _ { K } B _ { K } ^ { - 1 } z ) \, . } \\ { \text {mode} } & { \quad \cdots \text { } \Delta ( \lambda _ { K } B _ { K } ^ { - 1 } z ) \, . } \\ { F } & { X M , \quad \text {Applying Univariate II} \, 8 \text { with } x = ( \lambda _ { 1 } B _ { 1 } ^ { - 1 } \tau _ { x } \cdots ( \lambda _ { 2 } B _ { 2 } ^ { - 1 } \tau _ { z } ) \cdots ( \lambda _ { 3 } B _ { 3 } ^ { - 1 } \tau _ { z } ) ^ { T } } \end{array}$$

ˆ σ Y M Z ( t I 2 n ) = ( Φ B X ⊗ ✶ M Z ) ˆ σ XM Z ( t I 2 n ) . (73) By hypothesis, from Equation (66) and Lemma B.18, we have that, for every disjoint sets of initial systems X A = { X i 1 , . . . , X i k } and X B = { X j 1 , . . . , X j m } , it holds

$$\Box & & I ( X _ { A } \colon X _ { B } | M \mathbb { Z } ) _ { \hat { \sigma } _ { X M } \mathbb { Z } } = \int _ { \mathbb { R } ^ { 2 n } } I ( X _ { A } \colon X _ { B } | M ) _ { \hat { \sigma } _ { X M } | \mathbb { Z } = \mathbb { Z } } \, d p _ { Z } ( z ) \\ \intertext { t h a t h e } & = \int _ { \mathbb { R } ^ { 2 n } } I ( X _ { A } \colon X _ { B } | M ) _ { \hat { \rho } _ { X M } \, d p _ { Z } ( z ) } \\ & = 0 \, .$$

In the second equality we have exploited the fact that ˆ σ XM ∣ Z = z is a quantum state of the form ˆ U ˆ ρ XM ˆ U † , with ˆ U a unitary operator factorised on the two systems, i.e. , ˆ U = ˆ U X ⊗ ˆ U M , and thus, since the conditional mutual information can be written in terms of von Neumann entropies and the entropy is invariant under the tensor product of local unitary transformations, it holds I ( X A ∶ X B ∣ M ) ˆ σ XM ∣ Z = z = I ( X A ∶ X B ∣ M ) ˆ U ˆ ρ XM ˆ U † = I ( X A ∶ X B ∣ M ) ˆ ρ XM . From the data-processing inequality for quantum mutual information (Proposition B.19) and from Equation (74), we then have

$$I ( Y \colon \mathbb { Z } | M ) _ { \hat { \sigma } _ { Y M Z } } & \leq I ( X \colon \mathbb { Z } | M ) _ { \hat { \sigma } _ { X M Z } } \\ & \leq \sum _ { i = 1 } ^ { K } I ( X _ { i } \colon \mathbb { Z } | M ) _ { \hat { \sigma } _ { X _ { i } M Z } } \, , \\ \intertext { w h e u s e d i n e q u l i t iles ( 2 6 8 ) a n d ( 2 6 1 ) . The last inequality }$$

where we used inequalities (268) and (261). The last inequality in Equation (75) is a consequence of the definition of the conditional mutual information. Let us prove it by induction. By expressing the conditional quantum mutual information in terms of the von Neumann entropies of the individual subsystems, it is easy to verify that for K = 2 the following equality is satisfied:

$$I ( X _ { 1 } X _ { 2 } \mathbb { Z } | M ) _ { \hat { \sigma } _ { X M Z } } \\ = I ( X _ { 1 } \mathbb { Z } | M ) _ { \hat { \sigma } _ { X M Z } } + I ( X _ { 2 } \mathbb { Z } | M ) _ { \hat { \sigma } _ { X M Z } } + \\ + I ( X _ { 1 } \colon X _ { 2 } | M \mathbb { Z } ) _ { \hat { \sigma } _ { X M Z } } - I ( X _ { 1 } \colon X _ { 2 } | M ) _ { \hat { \sigma } _ { X M Z } } \\ \leq I ( X _ { 1 } \colon \mathbb { Z } | M ) _ { \hat { \sigma } _ { X M Z } } + I ( X _ { 2 } \colon \mathbb { Z } | M ) _ { \hat { \sigma } _ { X M Z } } \, ,$$

where we used Equation (74) with X A = X 1 and X B = X 2 . Let us now assume that this equation is valid for K -1 systems, which we denote altogether by J = X 1 ⋯ X K -1 , i.e. , that we have

$$I ( X _ { 1 } \cdots X _ { K - 1 } \colon \mathbb { Z } | M ) _ { \hat { \sigma } _ { X M Z } } & \leq \sum _ { i = 1 } ^ { K - 1 } I ( X _ { i } \colon \mathbb { Z } | M ) _ { \hat { \sigma } _ { X M Z } } \cdot ( 7 7 ) \quad g i v e n \ M \\ \text {We now verify that this relation is also valid for } K \text { systems}$$

We now verify that this relation is also valid for K systems, which we denote altogether by X = X 1 ⋯ X K = J X K . From Equations (76) and (77) we have that

$$E q u a t i m s \left ( / 6 \right ) & \text { and } ( / 7 ) \text { we have that } & & \text {Then, } & \text { } & \text {Then, } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { } & \text { }$$

Being true for K = 2 , we conclude that inequality (78) is true for every K ≥ 2 . First of all, let us note that, from inequality (72), it holds

$$( \iota ) , \, & \text {in} \, \hat { D } _ { X _ { i } } ( \lambda _ { i } B _ { i } ^ { - 1 } z ) \hat { \rho } _ { X _ { i } M } \hat { D } _ { X _ { i } } ^ { \dagger } ( \lambda _ { i } B _ { i } ^ { - 1 } z ) \, \text {d} p _ { \alpha } ( z ) \\ \hat { \sigma } _ { X _ { i } M } = & \int \hat { D } _ { X _ { i } } ( \lambda _ { i } B _ { i } ^ { - 1 } \mathbb { Z } ) \, \hat { \rho } _ { X _ { i } M } \, \hat { D } _ { X } ^ { \dagger } ( \lambda _ { i } B _ { i } ^ { - 1 } \mathbb { Z } ) \right ] \\ & = \mathbb { E } _ { \mathbb { Z } } [ \hat { D } _ { X } ( \lambda _ { i } B _ { i } ^ { - 1 } \mathbb { Z } ) \, \hat { \rho } _ { X _ { i } M } \, \hat { D } _ { X } ^ { \dagger } ( \lambda _ { i } B _ { i } ^ { - 1 } \mathbb { Z } ) ] \\ & = \mathbb { E } _ { Y } [ \hat { D } _ { X } ( \Psi ) \, \hat { \rho } _ { X _ { i } M } \, \hat { D } _ { X } ^ { \dagger } ( \Psi ) ] & & \text {where} \ \ A \text { here } \ A \\ & = ( \mathcal { N } _ { X _ { i } } ( t \, \lambda _ { i } ^ { 2 } B _ { i } ^ { - 1 } B _ { i } ^ { - T } ) \otimes \mathbb { I } _ { M } ) \, \hat { \rho } _ { X _ { i } M } \, , & & \text {the block} \\ \text {where we defined the Gaussian random variable } Y = \lambda _ { i } B _ { i } ^ { - 1 } \mathbb { Z } , & & \text {inequalities} \\$$

✶ where we defined the Gaussian random variable Y = λ i B -1 i Z , which has zero mean and covariance matrix λ 2 i B -1 i B -T i . Proceeding in the proof we get

$$I ( X _ { i } \colon \mathbb { Z } | M ) \hat { \sigma } _ { X _ { i } M \mathbb { Z } } & = S ( X _ { i } | M ) \hat { \sigma } _ { X _ { i } M } - S ( X _ { i } | M ) \hat { \rho } _ { X _ { i } M } \\ & = S ( X _ { i } | M ) ( \mathcal { N } _ { X _ { i } } ( t \lambda _ { i } ^ { 2 } B _ { i } ^ { - 1 } B _ { i } ^ { - T } ) \otimes 1 _ { M } ) \hat { \rho } _ { X _ { i } M } + \\ & - S ( X _ { i } | M ) \hat { \rho } _ { X _ { i } M } \\ & = \Delta _ { X _ { i } | M } ( \hat { \rho } _ { X _ { i } M } ) \left ( t \lambda _ { i } ^ { 2 } B _ { i } ^ { - 1 } B _ { i } ^ { - T } \right ) . \quad \text {we will} \\ & \quad ( 8 0 ) \quad \text {product} \\ \intertext { f o r $ \sigma $ $ ( 7 0 ) $ , $ d o w $ $ ( 8 0 ) $ , $ t o t h e r $ $ with $ i n e a u l i t y $ ( 7 5 ) $ $ $ such as } \intertext { f o r $ \sigma $ $ $ ( 7 0 ) $ , $ d o w $ $ $ ( 8 0 ) $ $ , $ t o t h e r $ $ $ with $ i n e a u l i t y $ ( 7 5 ) $ $ $ }$$

From Equations (70) and (80) together with inequality (75), Equation (69) is easily obtained and from this we finally obtain Equation (67).

Example III.17. For K = 2 we have, in the case of the beam splitter with parameter 0 ≤ η ≤ 1 , the matrices

$$B _ { 1 } = \sqrt { \eta } \, I _ { 2 n } \quad \text {and} \quad B _ { 2 } = \sqrt { 1 - \eta } \, I _ { 2 n } \, , \quad \text { (81) } \quad \text {where} \quad \text {where} \\ \text {in the one} \sigma \sigma \text { of } \text {causing with } \text {normator } \sigma > 1 \text {, the } \text {normics } \text { } \text {evolut}$$

or, in the case of squeezing with parameter κ &gt; 1 , the matrices

$$B _ { 1 } = \sqrt { \kappa } \, I _ { 2 n } \quad \text {and} \quad B _ { 2 } = \sqrt { \kappa - 1 } \, Z _ { 2 n } \, , \\ \intertext { o r o . \ Z \quad h o s \, b o n \, \text {defined in Exercism } \, I I _ { 2 } \, \text {, with those } \, \Omega }$$

where Z 2 n has been defined in Example III.3. With these matrices, from Equation (67), we obtain the result found in [18, Equation (66)].

## E. Proof of the multimode conditional quantum Entropy Power Inequality

Theorem III.18 (multimode conditional quantum Entropy Power Inequality) . Let X 1 , . . . , X K and Y be n -mode bosonic quantum systems, let X be the multipartite system X =

X 1 ⋯ X K , let M be a quantum system and let Φ B ∶ X → Y be the linear mixing defined in Definition III.1. Let ˆ ρ XM be a quantum state on XM such that ˆ ρ X has finite average energy (as per Definition II.4) and S ( ˆ ρ M ) &lt; +∞ , and let us suppose that the systems X 1 . . . X K are conditionally independent given M , i.e. , such that

$$S ( X _ { 1 } \dots X _ { K } | M ) _ { \hat { \rho } _ { X M } } = \sum _ { k = 1 } ^ { K } S ( X _ { k } | M ) _ { \hat { \rho } _ { X M } } \, . \\$$

Then, defining b i ∶= ∣ det B i ∣ 1 n , the multimode conditional quantum Entropy Power Inequality holds:

$$\begin{bmatrix} \text {Multimode conditional quantum Entropy Power} \\ \text {Inequality} \end{bmatrix} & \\ & \exp \left ( \frac { S ( Y | M ) _ { \hat { \rho } _ { Y M } } } { n } \right ) \geq \sum _ { i = 1 } ^ { K } b _ { i } \exp \left ( \frac { S ( X _ { i } | M ) _ { \hat { \rho } _ { X _ { i } M } } } { n } \right ) , \\$$

Proof. Let us first recall Definition III.1 for the matrix B :

$$B & = \left ( B _ { 1 } \quad \cdots \quad B _ { K } \right ) \in \mathbb { R } ^ { 2 n \times 2 K n } \, , \\ \\ \bar { B } & = 2 n \nu _ { 2 n } \, .$$

where ˆ ρ Y M = ( Φ B ⊗ ✶ M ) ˆ ρ XM .

where B i ∈ R 2 n × 2 n . As a first step, we observe that if all the blocks B i of the matrix B are non-invertible, then the inequality (84) we wish to prove is trivial. We therefore assume in the following that there exists at least one invertible block. Let's define

$$\Lambda _ { i } \coloneqq \lambda _ { i } I _ { 2 n } \, , \quad \Lambda \coloneqq \bigoplus _ { i = 1 } ^ { K } \Lambda _ { i } \, , \quad \tilde { B } \coloneqq \bigoplus _ { i = 1 } ^ { K } B _ { i } \, , \\$$

where 0 ≤ λ i ≤ 1 , such that ∑ K i = 1 λ i = 1 and λ k = 0 if B k is non-invertible. In the following, with a little abuse of notation, we will define as 0 all those quantities that are given by the product of a certain λ k = 0 and a quantity that is not defined, such as B -1 k for a certain non-invertible B k , i.e. , λ k B -1 k ∶= 0 . We define, for each t ≥ 0 , the time evolution:

ˆ ρ XM ( t ) ∶= ( K ⊗ i = 1 N X i ( t λ i B -1 i B -T i ) ⊗ ✶ M ) ˆ ρ XM , (87a) ˆ ρ Y M ( t ) ∶= ( Φ B ⊗ ✶ M ) ˆ ρ XM ( t ) , (87b) where X = X 1 ⋯ X K , 0 ≤ λ i ≤ 1 and ∑ K i = 1 λ i = 1 . The time evolution of the subsystems is then given by:

ˆ ρ X i M ( t ) = (N X i ( t λ i B -1 i B -T i ) ⊗ ✶ M ) ˆ ρ X i M . (88) From Equation (87a) and Lemma III.5, it holds

ˆ ρ XM ( t ) = (N X ( t ˜ B -1 Λ ˜ B -T ) ⊗ ✶ M ) ˆ ρ XM . (89) While from Equation (87b) and Lemma III.1, it holds

$$\begin{array} { r l } & { P o w e r } & { \hat { \rho } _ { Y M } ( t ) = \left ( \Phi _ { B } \otimes \mathbb { I } _ { M } \right ) \left ( \mathcal { N } _ { X } ( t \tilde { B } ^ { - 1 } \Lambda \tilde { B } ^ { - T } ) \otimes \mathbb { I } _ { M } \right ) \hat { \rho } _ { X M } } \\ & { \intertext { t h o r p y } & { = \left ( \mathcal { N } _ { Y } \left ( t \tilde { B } \tilde { ^ { - 1 } } \Lambda \tilde { B } ^ { - T } B ^ { T } \right ) \otimes \mathbb { I } _ { M } \right ) \hat { \rho } _ { Y M } } \\ & { X \ = \ } & { = \left ( \mathcal { N } _ { Y } ( t \, I _ { 2 n } ) \otimes \mathbb { I } _ { M } \right ) \hat { \rho } _ { Y M } \, , } \end{array}$$

where we have exploited the fact that ∑ K i = 1 λ i = 1 . We define the function

$$\phi ( t ) \coloneqq S ( Y | M ) _ { \hat { \rho } _ { Y M } ( t ) } - \sum _ { i = 1 } ^ { K } \lambda _ { i } S ( X _ { i } | M ) _ { \hat { \rho } _ { X _ { i } M } ( t ) } \, . \quad ( 9 1 ) \ \ C D \text { char} \\ \intertext { f o r } \exp \left ( D \cos i t \Omega _ { i } \Omega _ { i } \Omega _ { i } + \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i } \Omega _ { i$$

From Proposition III.15 and Lemma III.14, the following applies

$$\phi ^ { \prime } ( t ) & = J _ { Y | M } \left ( \hat { \rho } _ { Y M } ( t ) \right ) ( I _ { 2 n } ) + \\ & - \sum _ { i = 1 } ^ { K } J _ { X _ { i } | M } \left ( \hat { \rho } _ { X _ { i } M } ( t ) \right ) ( \lambda _ { i } ^ { 2 } B _ { i } ^ { - 1 } B _ { i } ^ { - T } ) \quad ( 9 2 ) \quad \mathcal { H } _ { A } \otimes \mathcal { H } _ { A } \\ & \leq 0 , \quad \text {with an} \quad \text {in Prop} \\ \text {where the inequality was obtained from Theorem III.16, with} & \quad \text {of $n$ of $n$ or $n$}$$

where the inequality was obtained from Theorem III.16, with α i = B -1 i Λ i B -T i (whence α = ˜ B -1 Λ ˜ B -T and BαB T = I 2 n ). Inequality (92), together with the asymptotic scaling of the conditional entropy stated in Proposition III.9, implies that

$$\text {conditional entropy stated in Proposition III.9, implies that} \\ \phi ( 0 ) \geq \lim _ { t \to + \infty } \phi ( t ) & & \text {The sym} _ { \hat { U } _ { S } \text { can } T } \\ = \lim _ { t \to + \infty } \left ( S ( Y | M ) _ { \hat { p } _ { Y M } ( t ) } - \sum _ { i = 1 } ^ { K } \lambda _ { i } S ( X _ { i } | M ) _ { \hat { p } _ { X i } ( t ) } \right ) & \\ = \frac { 1 } { 2 } \ln \left ( \det ( e t 1 _ { 2 n } ) \right ) - \sum _ { i = 1 } ^ { K } \frac { 1 } { 2 } \lambda _ { i } \ln \left ( \det ( e t \lambda _ { i } B _ { i } ^ { - 1 } B _ { i } ^ { T } ) \right ) & \text {rows and} \\ = n \left ( \sum _ { i = 1 } ^ { K } \lambda _ { i } \ln \frac { b _ { i } } { \lambda _ { i } } \right ) , & \text {block in} \\ & \quad A \text { while} \\ \text {where } h _ { i } \colon = \left | \det B _ { i } \right | ^ { \frac { 1 } { n } } \text {From inequality} \left ( 93 \right ) \text { immediately} \ \text {Remark}$$

where b i ∶= ∣ det B i ∣ 1 n . From inequality (93) immediately follows the multimode linear conditional quantum Entropy Power Inequality :

$$\frac { S ( Y | M ) _ { \hat { \rho } _ { Y } M } } { n } & \geq \sum _ { i = 1 } ^ { K } \lambda _ { i } \frac { S ( X _ { i } | M ) _ { \hat { \rho } _ { X _ { i } M } } } { n } + \sum _ { i = 1 } ^ { K } \lambda _ { i } \ln \left ( \frac { b _ { i } } { \lambda _ { i } } \right ) . \quad ( 9 4 ) \quad \text {entangle} \\$$

Maximising the RHS of Equation (94) with respect to { λ i ∶ i = 1 , . . . , K } (see Appendix A-D), i.e. , choosing

$$\lambda _ { j } = \frac { b _ { j } \exp \left ( \frac { S ( X _ { j } | M ) _ { \beta _ { X _ { j } M } } } { n } \right ) } { \sum _ { i = 1 } ^ { K } b _ { i } \exp \left ( \frac { S ( X _ { i } | M ) _ { \beta _ { X _ { i } M } } } { n } \right ) } .$$

for all j , we obtain precisely the MCQEPI in Equation (84).

Observation III.19. In the special case of K = 2 and S the symplectic matrices associated with the attenuator and the amplifier (see Example III.17) we find the inequality proved in [18, Theorem 6].

## IV. THE SQUASHED ENTANGLEMENT OF BOSONIC GAUSSIAN STATES

This section is devoted to determine upper and lower bounds to the squashed entanglement of the bosonic Gaussian states whose covariance matrix has half of the symplectic eigenvalues equal to 1 / 2 .

A. The problem

Let C and D be two n -mode bosonic quantum systems. Let us define the family F of bosonic Gaussian states of the system CD characterised by a covariance matrix with at least half of the symplectic eigenvalues equal to 1 / 2 . From Williamson's theorem (Theorem B.2) and properties (33) and (34), every state ˆ ρ CD ∈ F can be written in the following form:

where A and B are suitable n -mode subsystems of X , ˆ U S ∶ H A ⊗H B →H C ⊗H D is the unitary transformation associated with an appropriate symplectic matrix S ∈ Sp ( 4 n, R ) , defined in Proposition II.9, and ˆ ω A ( N ) is defined as the tensor product of n one-mode thermal states with average number of photons N = ( N 1 , . . . , N n ) :

$$\hat { \rho } _ { C D } ^ { S , N } = \hat { D } _ { r } \hat { U } _ { S } \left ( \hat { \omega } _ { A } ( N ) \otimes | 0 \rangle _ { B } \langle 0 | \right ) \hat { U } _ { S } ^ { \dagger } \hat { D } _ { r } ^ { \dagger } , \\ \\$$

$$\hat { \omega } _ { A } ( N ) & \colon = \hat { \omega } _ { A _ { 1 } } ( N _ { 1 } ) \otimes \cdots \otimes \hat { \omega } _ { A _ { n } } ( N _ { n } ) \, . \\ \\ \intertext { a n d } \omega _ { A } ( N ) & \colon = \hat { \omega } _ { A _ { 1 } } ( N _ { 1 } ) \otimes \cdots \otimes \hat { \omega } _ { A _ { n } } ( N _ { n } ) \, . \\$$

The symplectic matrix S defining the isometric transformation ˆ U S can be seen as a real 4 n × 4 n block matrix

$$S = \begin{pmatrix} B _ { 1 } ^ { C } & B _ { 2 } ^ { C } \\ B _ { 1 } ^ { D } & B _ { 2 } ^ { D } \end{pmatrix} ,$$

where the blocks are 2 n × 2 n real-valued matrices. The first 2 n rows and 2 n columns of matrix S act on system A while the last 2 n rows and 2 n columns act on system B . The upper left block implements therefore the transformation on the system A while the lower right block implements the transformation on system B .

Remark IV.1 . Since the translation operators act independently on each subsystem and the squashed entanglement is invariant under local unitary transformations (Proposition B.27), then, in what follows, the translation operators ˆ D r in Equation (96) will be neglected in the calculation of the squashed entanglement.

Example IV.2 (squeezing) . If S is the squeezing symplectic matrix, then B C = ( B C 1 B C 2 ) and B D = ( B D 1 B D 2 ) (see Example III.3) are given by

$$\text {Example in} . 5 \text { and } \text {given by} \\ B _ { 1 } ^ { C } = B _ { 2 } ^ { D } = \text {diag} ( \sqrt { \kappa _ { 1 } } \, I _ { 2 } , \cdots , \sqrt { \kappa _ { n } } \, I _ { 2 } ) \, , \\ B _ { 1 } ^ { D } = B _ { 2 } ^ { C } = \text {diag} ( \sqrt { \kappa _ { 1 } - 1 } \, Z _ { 2 } , \cdots , \sqrt { \kappa _ { n } - 1 } \, Z _ { 2 } ) \, , \\ \text {where} \, \kappa _ { i } > 1 \ \forall i \text { and } I _ { 2 } = \text {diag} ( 1 , 1 ) , \, Z _ { 2 } = \text {diag} ( 1 , - 1 ) , \, The$$

where κ i &gt; 1 ∀ i and I 2 = diag ( 1 , 1 ) , Z 2 = diag ( 1 , -1 ) . The output states are given by

$$\hat { \rho } _ { C } ^ { S , N } & = \Phi _ { B ^ { C } } \left ( \hat { \omega } _ { A } ( N ) \otimes | 0 \rangle _ { B } \langle 0 | \right ) , & ( 1 0 0 a ) \\ \hat { \rho } _ { A } ^ { S , N } & = \Phi _ { B ^ { \prime } } \left ( \hat { \omega } _ { A } ( N ) \otimes | 0 \rangle _ { A } \langle 0 | \right )$$

$$\hat { \rho } _ { D } ^ { S , N } = \Phi _ { B ^ { D } } \left ( \hat { \omega } _ { A } ( N ) \otimes | 0 \rangle _ { B } \langle 0 | \right ) . \quad ( 1 0 0 b ) \\ \intertext { a n t h e w s } \left ( 1 - \Phi _ { B } \left ( \hat { \omega } _ { A } ( N ) \otimes | 0 \rangle _ { B } \langle 0 | \right ) \right ) . \quad ( 1 0 0 b ) \\$$

Given the above definitions, the following theorem holds.

Theorem IV.3. For any S ∈ Sp ( 4 n, R ) as in Equation (98) and any N = ( N 1 , . . . , N n ) ∈ R n + , the squashed entanglement of the bosonic Gaussian state ˆ ρ S, N CD defined in Equation (96) satisfies

$$\begin{bmatrix} & & \text {Lower bound} \\ & & \\ & & \frac { n } { 2 } \ln \left ( 2 \, b _ { 1 } ^ { C } b _ { 1 } ^ { D } + b _ { 1 } ^ { D } b _ { 2 } ^ { C } + b _ { 1 } ^ { C } b _ { 2 } ^ { D } \right ) \leq E _ { s q } ( \hat { \rho } _ { C D } ^ { S , N } ) , & & ( 1 0 1 ) \end{bmatrix}$$

where b Y i ∶= ∣ det B Y i ∣ 1 / n for i = 1 , 2 and Y = C,D , and

$$w h e r e \, b _ { i } ^ { Y } \colon & \models | \det B _ { i } ^ { Y } | ^ { 1 / n } \text { for } i = 1 , 2 \text { and } Y = C , D , \text { and } \quad \stackrel { \text {margin} } { \gamma } _ { R } \circled { O } \\ & \quad \text {Upper bound} \\ & \quad \\ & \quad E _ { S } ( \hat { \rho } _ { C D } ^ { S , N } ) \\ & \quad \leq \frac { 1 } { 4 } \ln \left [ \det ( B _ { 1 2 N } ^ { C } ) \det \left ( C _ { N } - B _ { N } B _ { 1 } ^ { C T } ( B _ { 1 2 N } ^ { C } ) ^ { - 1 } B _ { 1 } ^ { C } B _ { N } \right ) \right ] \\ & \quad + \frac { 1 } { 4 } \ln \left [ \det \left ( B _ { 1 2 N } ^ { D } \right ) \det \left ( C _ { N } - B _ { N } B _ { 1 } ^ { D T } ( B _ { 1 2 N } ^ { D } ) ^ { - 1 } B _ { 1 } ^ { D } B _ { N } \right ) \right ] \\ & \quad + 2 n - \sum _ { i = 1 } ^ { n } g ( N _ { i } / 2 ) \, , \\ & \quad \text {where} \\ & \quad \text {where}$$

where

$$\ W h { C } ^ { Y } & = \bigoplus _ { i = 1 } ^ { n } \left ( N _ { i } + \frac { 1 } { 2 } \right ) B _ { 1 } ^ { Y } B _ { 1 } ^ { Y } + \frac { 1 } { 2 } B _ { 2 } ^ { Y } B _ { 2 } ^ { Y } T \, , \quad \text {Inequal} \\ Z _ { 2 n } & \coloneqq \bigoplus _ { i = 1 } ^ { n } \left ( \begin{smallmatrix} 1 & 0 \\ 0 & - 1 \end{smallmatrix} \right ) , \\ \text {for } Y & = C , D \text { and the } q \text { function as in } E \text { equation } ( 3 7 ) \text { and } \quad \text {and} \quad \text {and} \quad \text {and} \quad \text {and} \quad \text {and} \quad \text {and}$$

for Y = C,D and the g function as in Equation (37) and

$$B _ { N } \coloneqq \bigoplus _ { i = 1 } ^ { n } \sqrt { N _ { i } ( N _ { i } + 1 ) / 2 } \, Z _ { 2 } \, , \quad C _ { N } \coloneqq \bigoplus _ { i = 1 } ^ { n } \left ( \frac { N _ { i } } { 2 } + \frac { 1 } { 2 } \right ) I _ { 2 } \, . \quad \exp \left ( \frac { S } { 1 0 4 } \right )$$

Observation IV.4. The symplectic matrix S which brings into normal form the covariance matrix of the state (96) is not unique. However, if exactly half of the symplectic eigenvalues of this state are equal to 1 / 2 , thanks to Lemma B.11, the only freedom on the choice of this matrix is to multiply the diagonal blocks by orthogonal symplectic matrices. Since such matrices have unit determinant, they do not change the determinants of the blocks of the symplectic matrix and thus the lower bound of Theorem IV.3.

## B. Preliminary results

In this section we show some important preliminary results for the squashed entanglement.

Proposition IV.5 (convexity) . The squashed entanglement is a convex function of the state. In particular, given a finite alphabet X , an ensemble of quantum states { ˆ ρ x AB } x ∈ X and a probability distribution p ( x ) ∶ X →[ 0 , 1 ] , it holds

$$E _ { s q } \left ( \sum _ { x \in X } p ( x ) \, \hat { \rho } _ { A B } ^ { x } \right ) & \leq \sum _ { x \in X } p ( x ) \, E _ { s q } ( \hat { \rho } _ { A B } ^ { x } ) \, . \quad \ \ ( 1 0 5 ) \quad ^ { \text {Hence,} } _ { ( 1 1 2 ) \text { } g } \\ \\ \intertext { B } E _ { s q } \left ( \sum _ { x \in X } p ( x ) \, \hat { \rho } _ { A B } ^ { x } \right ) & \leq \sum _ { x \in X } p ( x ) \, E _ { s q } ( \hat { \rho } _ { A B } ^ { x } ) \, . \quad \ \ ( 1 0 5 ) \quad ^ { \text {Hence,} } _ { ( 1 1 2 ) \text { } g } \\$$

Proof. See [26, Proposition 3].

The following lemma provides a useful application of the multimode conditional quantum Entropy Power Inequality to a broad class of bosonic Gaussian states. This result will play a key role for the proof of Theorem IV.3.

Lemma IV.6 (application of the MCQEPI) . Let A be an n -mode bosonic quantum system, and let R be a generic quantum system. Let ˆ γ AR be a joint quantum state of AR such that its marginal ˆ γ A on A has finite average energy and its marginal ˆ γ R on R has finite entropy. Let

$$\hat { \rho } _ { C D R } & = \hat { U } _ { S } \left ( \hat { \rho } _ { A B R } \right ) \hat { U } _ { S } ^ { \dagger } \\ & = \hat { U } _ { S } \left ( \hat { \gamma } _ { A R } \otimes | 0 \rangle _ { B } \langle 0 | \right ) \hat { U } _ { S } ^ { \dagger } \, , \\ | 0 \rangle _ { S } & = | 0 \rangle ^ { \otimes n } \, \text { is } \ t h e \ v a c { u u } { m } \ t h e \sigma \text { of system } B \ g r a d \hat { U } _ { S }$$

where ∣ 0 ⟩ B = ∣ 0 ⟩ ⊗ n B is the vacuum state of system B and ˆ U S is the 2 n -mode isometric operator acting on AB defined in Proposition II.9. Then,

$$S ( C | R ) _ { \hat { \rho } _ { C D R } } \geq n \ln \left ( b _ { 1 } ^ { C } \exp \left ( \frac { S ( A | R ) _ { \hat { \gamma } _ { A R } } } { n } \right ) + b _ { 2 } ^ { C } \right ) , \ ( 1 0 7 \, a )$$

$$S ( D | R ) _ { \hat { \rho } C D R } \geq n \ln \left ( b _ { 1 } ^ { D } \exp \left ( \frac { S ( A | R ) _ { \hat { \gamma } _ { A R } } } { n } \right ) + b _ { 2 } ^ { D } \right ) , \ ( 1 0 7 b )$$

where the constants are defined as in Section IV-A.

Proof. The multimode conditional quantum Entropy Power Inequality, proven in Theorem III.18, states that

$$\exp \left ( \frac { S ( Y | R ) _ { \hat { \rho } _ { Y } R } } { n } \right ) & \geq \sum _ { i = 1 } ^ { K } b _ { i } ^ { Y } \exp \left ( \frac { S ( X _ { i } | R ) _ { \hat { \rho } _ { X _ { i } } R } } { n } \right ) , \quad ( 1 0 8 ) \\ \text {where in this case} \ K = 2 \ Y = C \text { or } Y = D \ X _ { 1 } = A \ X _ { 2 } = B$$

where, in this case, K = 2 , Y = C or Y = D , X 1 = A , X 2 = B and b Y i = ∣ det B Y i ∣ 1 / n . With these parameters, it holds:

$$I _ { 2 } \cdot \exp \left ( \frac { S ( C | R ) _ { \hat { \rho } _ { C R } } } { n } \right ) \geq b _ { 1 } ^ { C } \exp \left ( \frac { S ( A | R ) _ { \hat { \rho } _ { A R } } } { n } \right ) + b _ { 2 } ^ { C } \exp \left ( \frac { S ( B | R ) _ { \hat { \rho } _ { B R } } } { n } \right ) , \\ \text {gs into} \quad \exp \left ( \frac { S ( D | R ) _ { \hat { \rho } _ { D R } } } { n } \right ) \geq b _ { 1 } ^ { D } \exp \left ( \frac { S ( A | R ) _ { \hat { \rho } _ { A R } } } { n } \right ) + b _ { 2 } ^ { D } \exp \left ( \frac { S ( B | R ) _ { \hat { \rho } _ { B R } } } { n } \right ) . \\ \text {values} \quad \text {one only}$$

Let's now observe that

$$S ( B | R ) _ { \hat { \rho } _ { B R } } = S ( B | R ) _ { \hat { \gamma } _ { R } \otimes | 0 \rangle _ { B } ( 0 | } = 0 \, . \\ \\ \intertext { s c . } \rho _ { B } ( 1 ) \dot { \rho } _ { B } = S ( B | R ) _ { \hat { \gamma } _ { R } \otimes | 0 \rangle _ { B } ( 0 | } = 0 \, . \\$$

In fact, taking advantage of the property S ( AB ) ˆ ρ A ⊗ ˆ ρ B = S ( A ) ˆ ρ A + S ( B ) ˆ ρ B and the fact that the entropy of a pure state is zero, in our case S ( B ) ∶= S ( B ) ∣ 0 ⟩ B ⟨ 0 ∣ = 0 , we obtain:

$$S ( B | R ) & \coloneqq S ( B R ) - S ( R ) \\ & = S ( B ) + S ( R ) - S ( R ) = S ( B ) = 0 \, . \\ \intertext { t s } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text$$

Equation (109) is therefore rewritten as

$$\text {ent} \text { is } \quad & \exp \left ( \frac { S ( C | R ) _ { \hat { \rho } _ { C R } } } { n } \right ) \geq b _ { 1 } ^ { C } \exp \left ( \frac { S ( A | R ) _ { \hat { \rho } _ { A R } } } { n } \right ) + b _ { 2 } ^ { C } \, , \ \ ( 1 1 2 a ) \\ \text {and} \quad & \exp \left ( \frac { S ( D | R ) _ { \hat { \rho } _ { D R } } } { n } \right ) \geq b _ { 1 } ^ { D } \exp \left ( \frac { S ( A | R ) _ { \hat { \rho } _ { A R } } } { n } \right ) + b _ { 2 } ^ { D } \, . \ \ ( 1 1 2 b ) \\ & \text {Hono-tuning} \, \text {the} \, \log \text {ithm} \, \text {of} \, \text {the} \, L \text { HS and RHS of} \, \text {Equations}$$

Hence, taking the logarithm of the LHS and RHS of Equations (112) gives precisely the thesis, Equation (107).

In the next lemma we state a result that will be useful for the proof of the lower bound of Theorem IV.3.

Lemma IV.7. Let ˆ ρ CD be a quantum state of the form ˆ ρ CD = ˆ U ( ˆ σ A ⊗∣ ψ ⟩ B ⟨ ψ ∣) ˆ U † where ˆ U is an isometric operator acting on system AB , then the extensions of this state will be all and only those of the form

$$\hat { \tau } _ { C D R } = \hat { U } \left ( \hat { \sigma } _ { A R } \otimes | \psi \rangle _ { B } \langle \psi | \right ) \hat { U } ^ { \dagger } \, , \\ \hat { \hat { \tau } } _ { C D R } = \hat { U } \left ( \hat { \sigma } _ { A R } \otimes | \psi \rangle _ { B } \langle \psi | \right ) \hat { U } ^ { \dagger } \, ,$$

where ˆ σ AR is an extension of ˆ σ A .

Proof. Let us prove the two implications.

- 1) The fact that ˆ τ CDR in Equation (113) is an extension of ˆ ρ CD is obvious, indeed:

$$\rho _ { C D } \text { is 0bvisius,  indeed: } & \\ & \text {tr} _ { R } [ \hat { \tau } _ { C D R } ] = \text {tr} _ { R } [ \hat { U } ( \hat { \sigma } _ { A R } \otimes | \psi \rangle _ { B } \langle \psi | ) \hat { U } ^ { \dagger } ] \\ & = \hat { U } \left ( \text {tr} _ { R } [ \hat { \sigma } _ { A R } ] \otimes | \psi \rangle _ { B } \langle \psi | \right ) \hat { U } ^ { \dagger } \\ & = \hat { U } \left ( \hat { \sigma } _ { A } \otimes | \psi \rangle _ { B } \langle \psi | \right ) \hat { U } ^ { \dagger } \\ & = \hat { \rho } _ { C D } \, . \\ \intertext { 2 ) The fact that all extensions of } \hat { \rho } _ { C D } \text { are of the form } ( 1 1 3 ) \quad \text {from } v$$

- 2) The fact that all extensions of ˆ ρ CD are of the form (113) is less obvious. Let ˆ τ CDR be a generic extension of ˆ ρ CD , then ˆ U † ˆ τ CDR ˆ U is an extension of ˆ σ A ⊗∣ ψ ⟩ B ⟨ ψ ∣ , indeed

$$\ t r _ { R } [ \hat { U } ^ { \dagger } \hat { \tau } _ { C D R } \hat { U } ] = \hat { \sigma } _ { A } \otimes | \psi \rangle _ { B } \langle \psi | \, . \quad ( 1 1 5 ) \quad \text {whenever} \\ \hat { \psi } ^ { * } \hat { \tau } _ { A } \hat { \psi } = \hat { \psi } _ { A } \, . \quad ( 1 1 5 ) \quad \text {holds}$$

Then, ˆ U † ˆ τ CDR ˆ U has the form

$$\hat { U } ^ { \dagger } \hat { \tau } _ { C D R } \hat { U } = \hat { \sigma } _ { A R } \otimes | \psi \rangle _ { B } \langle \psi | \, , \quad ( 1 1 6 ) \\$$

for some quantum state ˆ σ AR , extension of ˆ σ A . From this follows Equation (113).

We can now prove Theorem IV.3.

## C. Lower bound

Applying Lemma IV.6, is now possible to provide a lower bound to the squashed entanglement of the state defined in Equation (96). In the following we will distinguish the input systems A and B from the output systems C and D of the operator ˆ U S . According to Lemma IV.7, the extensions of the state ˆ ρ S, N CD are all and only those of the form

$$\hat { \rho } _ { C D R } = \hat { U } _ { S } ( \hat { \omega } _ { A R } \otimes | 0 \rangle _ { B } \langle 0 | ) \hat { U } _ { S } ^ { \dagger } \, , \quad t r _ { R } [ \hat { \omega } _ { A R } ] = \hat { \omega } _ { A } ( N ) \, . \\$$

The conditional mutual information of this state is therefore written as:

$$I ( C \colon D | R ) _ { \hat { \rho } _ { C D R } } \coloneqq & S ( C | R ) _ { \hat { \rho } _ { C D R } } + S ( D | R ) _ { \hat { \rho } _ { C D R } } - S ( C D | R ) _ { \hat { \rho } _ { C D R } } \\ = & S ( C | R ) _ { \hat { \rho } _ { C D R } } + S ( D | R ) _ { \hat { \rho } _ { C D R } } - S ( A | R ) _ { \hat { \omega } _ { A R } } \, , \\ & ( 1 1 8 ) \quad D . \ U p p$$

where we used the unitary invariance of the entropy, the additivity with respect to the tensor product between states and the fact that the entropy of a pure state is zero:

$$and the fact that the entropy of a pure state is zero: & \quad \text {an } n \text {-} m \\ S ( C D | R ) _ { \hat { \rho } C D R } \colon & = S ( C D R ) _ { \hat { \rho } C D R } - S ( R ) _ { \hat { \rho } C D R } & \quad \text {bosonic} \\ & = S ( C D R ) _ { \hat { U } S } ( \hat { \omega } _ { A R } | 0 ) _ { B } ( 0 ) | \hat { U } _ { S } ^ { \dagger } - S ( R ) _ { \text {tr} C D [ \hat { \rho } C D R ] } & \quad \text {product} \\ & = S ( A B R ) _ { \hat { \omega } _ { A R } } | 0 ) _ { B } ( 0 | - S ( R ) _ { \text {tr} A B } [ \hat { \omega } _ { A } | 0 ) _ { B } | 0 ] \\ & = S ( A R ) _ { \hat { \omega } _ { A R } } - S ( R ) _ { \hat { \omega } _ { R } } & \quad \text {paramet} \\ & \colon = S ( A | R ) _ { \hat { \omega } _ { A R } } \, . & & \text {form } ( 1 1 9 ) \quad \text {and} \\ & \quad \text {for the sake of simplicity, } \, \text {let } \, \text {us. now. define} \, x \, \colon = \\$$

For the sake of simplicity, let us now define x ∶= S ( A ∣ R ) ˆ ω AR / n . From Lemma IV.6, we have

$$I ( C \colon D | R ) _ { \hat { \rho } C D R } & & \text {is the $b$} \\ & \geq n \ln ( b _ { 1 } ^ { C } e ^ { x } + b _ { 2 } ^ { C } ) + n \ln ( b _ { 1 } ^ { D } e ^ { x } + b _ { 2 } ^ { D } ) - n \ln ( e ^ { x } ) & & \text {half of the} \\ & = n \ln ( b _ { 1 } ^ { C } b _ { 1 } ^ { D } e ^ { x } + b _ { 2 } ^ { C } b _ { 2 } ^ { D } e ^ { - x } + ( b _ { 2 } ^ { C } b _ { 1 } ^ { D } + b _ { 1 } ^ { C } b _ { 2 } ^ { D } ) ) . & & \text {defined}$$

Exploiting Lemma B.1, i.e. , b C 1 b D 1 = b C 2 b D 2 , inequality (120) reads as

$$I ( C \colon D | R ) _ { \hat { \rho } _ { C D R } } & \geq n \ln \left ( b _ { 1 } ^ { C } b _ { 1 } ^ { D } ( e ^ { x } + e ^ { - x } ) + \left ( b _ { 2 } ^ { C } b _ { 1 } ^ { D } + b _ { 1 } ^ { C } b _ { 2 } ^ { D } \right ) \right ) \\ & = n \ln \left ( 2 b _ { 1 } ^ { C } b _ { 1 } ^ { D } \cosh ( x ) + \left ( b _ { 2 } ^ { C } b _ { 1 } ^ { D } + b _ { 1 } ^ { C } b _ { 2 } ^ { D } \right ) \right ) \\ & \geq n \ln \left ( 2 b _ { 1 } ^ { C } b _ { 1 } ^ { D } + b _ { 2 } ^ { C } b _ { 1 } ^ { D } + b _ { 1 } ^ { C } b _ { 2 } ^ { D } \right ) , \\$$

from which the lower bound of Equation (101) is obtained.

Remark IV.8 . The lower bound (101) can be saturated only when the last inequality in Equation (121) is saturated, i.e. , when cosh ( x ) = 1 and thus when the following condition holds:

$$S ( A | R ) _ { \hat { \omega } _ { A R } } = 0 \, .$$

This remark tells us that if under certain conditions (e.g. for the number of photons N of the thermal state ˆ ω A ( N ) going to infinity) the gap between the lower bound and the upper bound we are going to study closes, then the extension ˆ ω AR of the state ˆ ω A ( N ) will necessarily have to satisfy the condition in Equation (122).

Example IV.9 (squeezing transformation) . If we consider the specific case in which the unitary operator ˆ U S is associated with a one-mode squeezing transformation with parameter κ , it holds

$$\text {the} \quad B _ { 1 } ^ { C } = B _ { 2 } ^ { D } = \sqrt { \kappa } \, I _ { 2 } \, , \quad B _ { 1 } ^ { D } = B _ { 2 } ^ { C } = \sqrt { \kappa - 1 } \, Z _ { 2 } \, .$$

Equation (101), with n = 1 , thus implies that

$$E _ { \text {sq} } ( \hat { \rho } _ { C D } ^ { S , N } ) \geq \ln ( 2 k - 1 ) \, ,$$

which is exactly the result proven in [42, Theorem 1].

## D. Upper bound

To prove the upper bound in Equation (102) we consider a collection of extensions of the state ˆ ρ S, N CD . First of all, given an n -mode bosonic quantum system, we define the noisless bosonic Gaussian attenuator on such a system as the tensor product of n one-mode noisless bosonic Gaussian attenuators with attenuation parameters η i on each individual mode, i.e. , E η ∶= E η 1 ⊗ ⋯ ⊗ E η n . Specifically, let us consider the n -parameter family of extensions { ˆ ρ CDR ( η )} η ∈[ 0 , 1 ] n of the form (117) where R is a n -mode bosonic quantum system and

$$\hat { \omega } _ { A R } ( \eta ) = ( \mathbb { I } _ { A } \otimes \mathcal { E } _ { \eta } ) ( | \phi _ { N } \rangle _ { A R } \langle \phi _ { N } | ) \quad ( 1 2 5 ) \\ \intertext { i n e b o s i c G a u s i g a n s i t a n t e u a t i o n a p e l y i n g t h e n o i s e l e s } \text {cubic Gaussian state obtained applying the noiseless } \text {cubic Gaussian } \attenuator \text { with attenuation parameter } n \text { to }$$

is the bosonic Gaussian state obtained applying the noiseless bosonic Gaussian attenuator with attenuation parameter η to half of the 2 n -mode squeezed vacuum state ∣ ϕ N ⟩ AR with average number of photons per mode N i . The state ∣ ϕ N ⟩ AR ⟨ ϕ N ∣ is defined as the tensor product of n two-mode squeezed vacuum states. We leave η as a free parameter over which we will optimize in the end. The covariance matrix of ˆ ω AR ( η ) is 1

$$\sigma ( \hat { \omega } _ { A R } ( \eta ) ) = \bigoplus _ { i = 1 } ^ { n } \left ( \int _ { \sqrt { \eta _ { i } N _ { i } ( N _ { i } + 1 ) } } ^ { N _ { i } + \frac { 1 } { 2 } } I _ { 2 } \right ) & \quad \sqrt { \eta _ { i } N _ { i } ( N _ { i } + 1 ) } \, Z _ { 2 } \right ) \\ \text {where for convenience we rearranged the modes as } A _ { 1 } R _ { 1 }$$

where for convenience we rearranged the modes as A 1 R 1 ⋯ A n R n , with A i and R i are one-mode bosonic quantum systems and I 2 = diag ( 1 , 1 ) and Z 2 = diag ( 1 , -1 ) .

Lemma IV.10. The symplectic eigenvalues of σ ( ˆ ω AR ( η )) defined in Equation (126) are

$$\nu _ { 2 k - 1 } ( \hat { \omega } _ { A R } ( \eta ) ) = ( 1 - \eta _ { k } ) N _ { k } + \frac { 1 } { 2 } \, , \quad \nu _ { 2 k } ( \hat { \omega } _ { A R } ( \eta ) ) = \frac { 1 } { 2 } \, , \\ \sigma ( \hat { \rho } _ { C } ) = \sigma ( \hat { \rho } _ { C } )$$

for k = 1 , . . . , n .

Proof. In the case n = 1 , covariance matrix (126) is of the form

$$\sigma ( \hat { \omega } _ { A R } ( \eta ) ) = & \left ( \sqrt { N + \frac { 1 } { 2 } } \right ) I _ { 2 } \quad \sqrt { \eta N ( N + 1 ) } \, Z _ { 2 } \right ) , \quad \sigma ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ { A } ( \hat { \rho } _ { D } ( \hat { \rho } _ {$$

Its symplectic eigenvalues are

$$\nu _ { + } ( \hat { \omega } _ { A R } ( \eta ) ) = ( 1 - \eta ) N + \frac { 1 } { 2 } \, , \quad \nu _ { - } ( \hat { \omega } _ { A R } ( \eta ) ) = \frac { 1 } { 2 } \, . \, \ ( 1 2 9 )$$

For the quantum state ˆ ω AR ( η ) = ⊗ n i = 1 ˆ ω A i R i ( η i ) , the covariance matrix is

$$\sigma ( \hat { \omega } _ { A R } ( \eta ) ) = \bigoplus _ { i = 1 } ^ { n } \left ( \begin{array} { c c } \left ( N _ { i } + \frac { 1 } { 2 } \right ) I _ { 2 } & \sqrt { \eta _ { i } N _ { i } ( N _ { i } + 1 ) } \, \sigma _ { z } \\ \sqrt { \eta _ { i } N _ { i } ( N _ { i } + 1 ) } \, \sigma _ { z } & \left ( \eta _ { i } N _ { i } + \frac { 1 } { 2 } \right ) I _ { 2 } \end{array} \right ) \cdot \quad \text {We   c } \, \sigma _ { z } \\ \text {The matrices (130)} \, \text {and} \, \Delta \, \text {are block diagonal, then so will be} \, \text {state with}$$

The matrices (130) and ∆ are block diagonal, then so will be the matrix ∆ σ ( ˆ ω AR ( η )) . Since the eigenvalues of a diagonal block matrix are the eigenvalues of the individual blocks, it is clear that the symplectic eigenvalues of matrix (130) are

$$\nu _ { 2 k - 1 } ( \hat { \omega } _ { A R } ( \eta ) ) & = ( 1 - \eta _ { k } ) N _ { k } + \frac { 1 } { 2 } \, , \quad \nu _ { 2 k } ( \hat { \omega } _ { A R } ( \eta ) ) = \frac { 1 } { 2 } \, , \\ \text {with } k = 1 , \dots , n . & \quad \Box \quad \text {where } \nu _ { 2 k } ( \hat { \omega } ) = \sum _ { \substack { ( 1 3 1 ) \\ 0 \\ \quad } } S _ { G }$$

=

From Proposition II.13 and Lemma IV.10 it holds

$$From \text {Proposition II.13 and Lemma IV.10 it holds} & \quad w i t h c o v i n d s \\ S ( C D R ) \hat { \rho } _ { C D R } ( \eta ) & = S ( A R ) _ { \hat { \omega } A R } ( \eta ) \\ & = \sum _ { k = 1 } ^ { n } \left [ g ( \nu _ { 2 k - 1 } ( \hat { \omega } _ { A _ { k } R _ { k } } ( \eta _ { k } ) ) - \frac { 1 } { 2 } ) + \\ & + g \left ( \nu _ { 2 k } ( \hat { \omega } _ { A _ { k } R _ { k } } ( \eta _ { k } ) ) - \frac { 1 } { 2 } \right ) \quad \text {From} \\ & = \sum _ { k = 1 } ^ { n } g ( ( 1 - \eta _ { k } ) N _ { k } ) \, . \\ & \quad \text {For the calculation of this covariance matrix, please refer to Appendix}$$

1 For the calculation of this covariance matrix, please refer to Appendix A-A.

As far as entropy S ( R ) is concerned, we must consider the blocks associated with the systems R 1 , . . . , R n of the matrix in Equation (126):

$$S ( R ) _ { \hat { \rho } _ { C D R } ( \eta ) } & = S ( R ) _ { \hat { \omega } _ { A R } ( \eta ) } \\ & = \sum _ { k = 1 } ^ { n } g \left ( \nu _ { k } ( \hat { \omega } _ { R _ { k } } ( \eta _ { k } ) ) - \frac { 1 } { 2 } \right ) \\ & = \sum _ { k = 1 } ^ { n } g ( \eta _ { k } N _ { k } ) . \\ \text {Let } \hat { \rho } _ { C R } ( \eta ) \text { and } \hat { \rho } _ { D R } ( \eta ) \text { be the marginals of } \hat { \rho } _ { C D R } ( \eta ) \text { on }$$

Let ˆ ρ CR ( η ) and ˆ ρ DR ( η ) be the marginals of ˆ ρ CDR ( η ) on systems CR and DR , respectively. They are bosonic Gaussian states with covariance matrices (see Appendix A-B)

$$\frac { \frac { 1 } { 2 } } { 1 2 7 ) } , \quad \sigma ( \hat { \rho } _ { C R } ( \eta ) ) = \begin{pmatrix} A _ { N } \, B _ { 1 } ^ { C } \, B _ { 1 } ^ { C T } + \frac { 1 } { 2 } \, B _ { 2 } ^ { C } \, B _ { 2 } ^ { C T } & B _ { 1 } ^ { C } \, B _ { N } \\ B _ { N } \, B _ { 1 } ^ { C T } & C _ { N } \end{pmatrix} ,$$

(134a)

$$\sigma ( \hat { \rho } _ { D R } ( \eta ) ) = \begin{pmatrix} A _ { N } \, B _ { 1 } ^ { D } \, B _ { 1 } ^ { D } ^ { T } + \frac { 1 } { 2 } \, B _ { 2 } ^ { D } \, B _ { 2 } ^ { D } \, ^ { T } & B _ { 1 } ^ { D } \, B _ { N } \\ B _ { N } \, B _ { 1 } ^ { D ^ { T } } & C _ { N } \end{pmatrix} ,$$

where we have defined the following quantities

$$\text {have defined the following quantities} \\ A _ { N } \coloneqq \bigoplus _ { i = 1 } ^ { n } \left ( N _ { i } + \frac { 1 } { 2 } \right ) I _ { 2 } \, , \\ B _ { N } \coloneqq \bigoplus _ { i = 1 } ^ { n } \sqrt { \eta _ { i } \, N _ { i } ( N _ { i } + 1 ) } \, Z _ { 2 } \, , \quad ( 1 3 5 ) \\ C _ { N } \coloneqq \bigoplus _ { i = 1 } ^ { n } \left ( \eta _ { i } \, N _ { i } + \frac { 1 } { 2 } \right ) I _ { 2 } \, . \\ \text {now  derive the upper bound of the  squared}$$

We can now derive the upper bound of the squashed entanglement for the state ˆ ρ S, N CD . To do so we exploit the fact that the von Neumann entropy S Q ( γ ) of a bosonic Gaussian state with covariance matrix γ satisfies the inequality given by the following

Lemma IV.11. For any γ ∈ R 2 n × 2 n &gt; 0 with ν min ( γ ) ≥ 1 / 2 it holds

$$\int _ { 1 } ^ { 1 } \int _ { \Box } S _ { G } ( \gamma ) - \frac { n } { 4 \nu _ { \min } ( \gamma ) ^ { 2 } } \ln \left ( \frac { e } { 2 } \right ) \leq S _ { Q } ( \gamma ) \leq S _ { G } ( \gamma ) \, , \quad ( 1 3 6 ) \\ \Box \quad w h o r a \, y _ { \quad } ( \gamma ) \, \colon \, i s \, t h o \, \min i m u m \, \sum \min i o t i o \, \arg n y l o f \, \alpha \, , \quad ( 1 3 6 )$$

where ν min ( γ ) is the minimum symplectic eigenvalue of γ and S G ( γ ) is the Shannon entropy of a Gaussian random variable with covariance matrix γ ,

$$S _ { G } ( \gamma ) = \frac { 1 } { 2 } \ln ( \det ( e \gamma ) ) \, .$$

Proof.

$$o f . \, S e e \, [ 4 7 , L e m m a \, 9 ] .$$

From Equations (137) and (136), it is therefore true that

$$S ( C R ) _ { \hat { \rho } _ { C D R } } ( \eta ) & \leq S _ { G } ( \sigma ( \hat { \rho } _ { C R } ( \eta ) ) ) \\ & = \frac { 1 } { 2 } \ln \left ( \det \left ( e \sigma ( \hat { \rho } _ { C R } ( \eta ) ) \right ) \right ) \\ & = 2 n + \frac { 1 } { 2 } \ln \left ( \det \left ( \sigma ( \hat { \rho } _ { C R } ( \eta ) ) \right ) \right ) ,$$

where n is the number of modes of the individual subsystems. Using the formula for the determinant of a block matrix 2 , Equation (138) becomes

$$S ( C R ) _ { \hat { \rho } _ { C } D R } ( \eta ) \\ \leq 2 n + \frac { 1 } { 2 } \ln \left [ \det ( B _ { 1 2 N } ^ { C } ) \det \left ( C _ { N } - B _ { N } B _ { 1 } ^ { C } ( B _ { 1 2 N } ^ { C } ) ^ { - 1 } B _ { 1 } ^ { C } B _ { N } \right ) \right ] , \\ + \\$$

where, for typographical reasons, we have defined the matrix

$$B _ { 1 2 N } ^ { Y } = A _ { N } \, B _ { 1 } ^ { Y } \, B _ { 1 } ^ { Y ^ { T } } + \frac { 1 } { 2 } \, B _ { 2 } ^ { Y } \, B _ { 2 } ^ { Y ^ { T } } \, , \quad ( 1 4 0 )$$

where Y = C,D . Similarly (with the replacement of blocks B C 1 → B D 1 and B C 2 → B D 2 ) it holds

$$S ( D R ) _ { \hat { \rho } _ { C } D R } ( \eta ) \\ \leq 2 n + \frac { 1 } { 2 } \ln \left [ \det ( B _ { 1 2 N } ^ { D } ) \det \left ( C _ { N } - B _ { N } B _ { 1 } ^ { D } \left ( B _ { 1 2 N } ^ { D } \right ) ^ { - 1 } B _ { 1 } ^ { D } B _ { N } \right ) \right ] . \quad \text {In the} \quad \text {quasihe} \\ \quad \text {Gaussian}$$

Therefore, for any 0 ≤ η i ≤ 1 it holds

$$\text {There, for any } 0 \leq \eta _ { i } \leq 1 \text { it holds} \\ \text { } E _ { \text {sq} } ( \hat { \rho } _ { C D } ^ { S , N } ) & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & &$$

Now, from an explicit form of the individual blocks of the symplectic matrix, we could optimise the expression above to obtain the value of η that minimises this upper bound. However, we know from Equation (121) that the lower bound can be saturated only when S ( A ∣ R ) ˆ ω AR = 0 , which, with the notation of Equation (125) and from Equations (132) and (133) can happen for example for 3 η i = 1 / 2 ∀ i . Indeed

$$S ( A | R ) _ { \hat { \omega } _ { A R } ( \eta ) } & \coloneqq S ( A R ) _ { \hat { \omega } _ { A R } ( \eta ) } - S ( R ) _ { \hat { \omega } _ { A R } ( \eta ) } & \text {such that} \\ & = \sum _ { i = 1 } ^ { n } g ( ( 1 - \eta _ { i } ) N _ { i } ) - \sum _ { i = 1 } ^ { n } g ( \eta _ { i } N _ { i } ) \quad ( 1 4 3 ) \\ & = 0 \, , & \Sigma ^ { \prime } & =$$

2 If A is invertible, it holds

$$\det \begin{pmatrix} A & B \\ C & D \end{pmatrix} = \det ( A ) \det \left ( D - C A ^ { - 1 } B \right ) .$$

3 Actually this condition can also be fulfilled for E = 0 , but we are mostly interested in the case E &gt; 0 .

which is fulfilled for η i = 1 / 2 ∀ i . We can give an expression for the upper bound by setting η i = 1 / 2 ∀ i :

$$\text {matrix} ^ { 2 } , \quad \text {for the upper bound by setting } \eta _ { i } = 1 / 2 \ \forall i \colon \\ E _ { \text {sq} } ( \hat { \rho } _ { C D } ^ { S , N } ) \\ \leq \frac { 1 } { 4 } \ln \left [ \det ( B _ { 1 2 N } ^ { C } ) \det ( C _ { N } - B _ { N } B _ { 1 } ^ { C } ( B _ { 1 2 N } ^ { C } ) ^ { - 1 } B _ { 1 } ^ { C } B _ { N } ) \right ] \\ ( 1 3 ) \quad + \frac { 1 } { 4 } \ln \left [ \det ( B _ { 1 2 N } ^ { P } ) \det ( C _ { N } - B _ { N } B _ { 1 } ^ { T } \left ( B _ { 1 2 N } ^ { P } \right ) ^ { - 1 } B _ { 1 } ^ { P } B _ { N } ) \right ] \\ \quad + 2 n - \sum _ { i = 1 } ^ { n } g ( N _ { i } / 2 ) \, , \\ ( 1 4 ) \\ \text {is which is the thesis, Equation } ( 1 2 ) .$$

which is the thesis, Equation (102).

## V. THE SQUASHED ENTANGLEMENT OF MULTIMODE EXTREME BOSONIC GAUSSIAN CHANNELS

In this section we determine the lower bound to the squashed entanglement of all the multimode extreme bosonic Gaussian channels , i.e. , the bosonic Gaussian channels that cannot be decomposed as a non-trivial convex combination of quantum channels. The proof will be based on the results obtained in Section IV.

Every bosonic Gaussian channel N can be written in the physical representation as

$$\mathcal { N } ( \hat { \rho } _ { S } ) = \text {tr} _ { E } \left [ \hat { U } _ { S E } \left ( \hat { \rho } _ { S } \otimes \hat { \phi } _ { E } \right ) \hat { U } _ { S E } ^ { \dagger } \right ] ,$$

where ˆ ϕ E is a Gaussian environment state with which the system interacts via the unitary transformation ˆ U SE associated to a symplectic matrix as in Proposition II.9.

## A. Preliminary results

This section is devoted to some preliminary results that are needed to prove the lower bound to the squashed entanglement of the multimode extreme bosonic Gaussian channels.

Lemma V.1. Let A and A ′ be m -mode bosonic quantum systems and let

$$\Sigma = \left ( \begin{array} { c c } \sigma _ { A A } & \sigma _ { A A ^ { \prime } } \\ \sigma _ { A ^ { \prime } A } & \sigma _ { A ^ { \prime } A ^ { \prime } } \end{array} \right ) \geq \pm \frac { i } { 2 } \left ( \begin{array} { c c } \Delta & 0 \\ 0 & \Delta \end{array} \right )$$

be the covariance matrix of a pure bosonic Gaussian state such that the matrices σ A ′ A ′ ± i 2 ∆ are both invertible. Let K, α ∈ R 2 n × 2 n . Then, α ≥ ± i 2 ( ∆ -K ∆ K T ) iff

$$\Sigma ^ { \prime } = \left ( \begin{array} { c c c } K \, \sigma _ { A A } \, K ^ { T } + \alpha & K \, \sigma _ { A A ^ { \prime } } \\ \sigma _ { A ^ { \prime } A } \, K ^ { T } & \sigma _ { A ^ { \prime } A ^ { \prime } } \end{array} \right ) \geq \pm \frac { i } { 2 } \left ( \begin{array} { c c c } \Delta & 0 \\ 0 & \Delta \end{array} \right ) .$$

Proof. Let us show the two implications separately. a) ' /Leftrightline⇒ ': Inequality (147) is equivalent to the following

$$\begin{pmatrix} K \sigma _ { A A } K ^ { T } + \alpha \mp \frac { i } { 2 } \Delta & K \sigma _ { A A ^ { \prime } } \\ \sigma _ { A ^ { \prime } A } K ^ { T } & \sigma _ { A ^ { \prime } A ^ { \prime } } \mp \frac { i } { 2 } \Delta \end{pmatrix} \geq 0 \, .$$

By hypothesis, conditions (146) and α ≥ ± i 2 ( ∆ -K ∆ K T ) imply that

$$\text {implly that} & & \text {compomon} & & \text {component} \\ & \begin{pmatrix} K \sigma _ { A A } \, K ^ { T } + \alpha \mp \frac { i } { 2 } \Delta & K \sigma _ { A A ^ { \prime } } \\ \sigma _ { A ^ { \prime } A } \, K ^ { T } & \sigma _ { A ^ { \prime } A ^ { \prime } } \mp \frac { i } { 2 } \Delta \end{pmatrix} & & \text {dimensions} & & \text {dimension} \\ & \geq & \begin{pmatrix} K \left ( \sigma _ { A A } \mp \frac { i } { 2 } \Delta \right ) K ^ { T } & K \sigma _ { A A ^ { \prime } } \\ \sigma _ { A ^ { \prime } A } \, K ^ { T } & \sigma _ { A ^ { \prime } A ^ { \prime } } \mp \frac { i } { 2 } \Delta \end{pmatrix} & & \text {at least} & & \text {the only} \\ & = & \begin{pmatrix} K & 0 \\ 0 & I \end{pmatrix} & \begin{pmatrix} \sigma _ { A A } \mp \frac { i } { 2 } \Delta & \sigma _ { A A ^ { \prime } } \\ \sigma _ { A ^ { \prime } A } & \sigma _ { A ^ { \prime } A ^ { \prime } } \mp \frac { i } { 2 } \Delta \end{pmatrix} & & \text {left} & & \text {where} \ v v \\ & \geq 0 & & & \text {then} & & \text {still post} \\ & b ) & \ll = & \colon \text {Given condition} & ( 1 7 ) \text { and being } \sigma _ { A ^ { \prime } A ^ { \prime } } \pm \frac { i } { 2 } \Delta & & \text {Lemmas} \end{pmatrix}$$

b) ' ⇐/Leftrightline ': Given condition (147) and being σ A ′ A ′ ± i 2 ∆ invertible by hypothesis, Lemma B.8 ensures that

$$K \sigma _ { A A } K ^ { T } + \alpha \mp \frac { i } { 2 } \Delta - K \sigma _ { A A ^ { \prime } } \left ( \sigma _ { A ^ { \prime } A ^ { \prime } } \mp \frac { i } { 2 } \Delta \right ) ^ { - 1 } \sigma _ { A ^ { \prime } A ^ { \prime } } K ^ { T } & \geq 0 \, . \\ P r o f \, K$$

Being, by hypothesis, Σ the covariance matrix of a pure bosonic Gaussian state, Lemma B.5 and Lemma B.7 imply rank ( Σ ± i 2 ∆ ) = 2 n . By hypothesis σ A ′ A ′ ± i 2 ∆ is invertible, so rank ( σ A ′ A ′ ± i 2 ∆ ) = 2 n = rank ( Σ ± i 2 ∆ ) . Since rank ( Σ ± i 2 ∆ ) = rank ( σ A ′ A ′ ± i 2 ∆ ) , Proposition B.9 implies that

$$\sigma _ { A A } \mp \frac { i } { 2 } \Delta = \sigma _ { A A ^ { \prime } } \left ( \sigma _ { A A } \mp \frac { i } { 2 } \Delta \right ) ^ { - 1 } \sigma _ { A ^ { \prime } A } \, . \quad \text { (151) } \quad \text {which} \\ \sigma _ { A } \dot { \sigma } = \sigma _ { A } \dot { \sigma } \, . \quad \text {extrem}$$

Substituting Equation (151) into Equation (150), it holds

$$\alpha \geq \pm \frac { i } { 2 } \left ( \Delta - K \Delta K ^ { T } \right ) . \quad \quad ( 1 5 2 ) \quad \text {ing p} \quad \quad \text {the r}$$

Lemma V.2. Let Σ ′ ∈ R 4 n × 4 n satisfy

$$\Sigma ^ { \prime } \geq \pm \frac { i } { 2 } \left ( \begin{array} { c c } \Delta & 0 \\ 0 & \Delta \end{array} \right ) . \quad \quad ( 1 5 3 ) \stackrel { m o d e } { h a s }$$

Let us assume that the only δ ∈ R 2 n × 2 n such that δ ≥ 0 and

$$\Sigma ^ { \prime } - \left ( \begin{array} { c c } \delta & 0 \\ 0 & 0 \end{array} \right ) \geq \pm \frac { i } { 2 } \left ( \begin{array} { c c } \Delta & 0 \\ 0 & \Delta \end{array} \right ) \quad \quad ( 1 5 4 )$$

is δ = 0 . Then, Σ ′ has at least n symplectic eigenvalues equal to 1 / 2 .

Since C is isomorphic to R 2 , we can identify the vector space C 2 n given by the span of the first 2 n vectors of the canonical basis of C 4 n with W = R 4 n . That is, we can identify C 2 n with the set of ordered pairs ( v , w ) , where v , w ∈ R 2 n are the real and the imaginary part, respectively, of the complex vector. By this analogy, the space given by the intersection of the support of Σ ′ + i 2 ∆ and the span of the first 2 n vectors of the canonical basis of C 4 n will be V = R 2 n + 2 . We therefore

Proof. Let us assume that Σ ′ has at least n + 1 symplectic eigenvalues strictly larger than 1 / 2 . Therefore, Lemma B.6 and Lemma B.7 ensure that Σ ′ + i 2 ∆ has rank at least 2 n + n + 1 = 3 n + 1 . Then, the intersection between the support of Σ ′ + i 2 ∆ and the span of the first 2 n vectors of the canonical basis of C 4 n has dimension at least 3 n + 1 + 2 n -4 n = n + 1 . The statement follows if we prove that such an intersection contains at least one unit real vector v ∈ R 4 n by choosing δ = ε vv T with ε strictly smaller than the smallest eigenvector of the matrix Σ ′ + i 2 ∆ .

want to show that V ⊂ W contains a vector with only real components, that is, a vector of the form ( r , 0 ) . This must be necessarily true because the orthogonal space of a subspace of dimension 2 n + 2 has dimension 2 n -2 and if in R 2 n we impose the orthogonality condition to 2 n -2 vectors the solutions have at least dimension 2 .

The proof is concluded by the general property which states that subtracting from a positive semidefinite matrix ε vv T , where v is a unit vector in the matrix support, and ε is smaller than the smallest eigenvector of the matrix, then the matrix is still positive semidefinite.

Lemma V.3. With the same notation of Lemma V.1, let the ( K,α ) Gaussian channel be extreme. Then, Σ ′ has at least n symplectic eigenvalues equal to 1 / 2 .

Proof. Let δ ∈ R 2 n × 2 n , δ ≥ 0 and let us assume that

$$\Sigma ^ { \prime } - \left ( \begin{array} { c c } \delta & 0 \\ 0 & 0 \end{array} \right ) \geq \pm \frac { i } { 2 } \left ( \begin{array} { c c } \Delta & 0 \\ 0 & \Delta \end{array} \right ) \cdot \quad ( 1 5 5 )$$

Lemma V.1 (with α → α -δ ) implies that

$$\alpha \geq \alpha - \delta \geq \pm \frac { i } { 2 } ( \Delta - K \, \Delta \, K ^ { T } ) \, , \\$$

which means δ = 0 , being the ( K,α ) Gaussian channel extreme. The claim follows from Lemma V.2.

Thanks to these observations, we can now state the following proposition, which will play an important role throughout the rest of the work.

Proposition V.4. Let ˆ ρ be a 2 n -mode pure bosonic Gaussian state and Φ an extreme bosonic quantum channel acting on n modes, then the covariance matrix of the state ( ✶ ⊗ Φ )( ˆ ρ ) has at least half of its symplectic eigenvalues equal to 1 / 2 .

Proof. This is a direct consequence of Lemmas V.1, V.2 and V.3.

## B. Extremality condition

In this subsection we provide an algorithm to check that a given quantum channel fulfils the condition of being extreme.

## Algorithm 1 Test for the extremality condition

Input: Two matrices K,α ∈ R 2 n × 2 n describing a bosonic Gaussian channel.

Output: True if the channel is extreme, False otherwise. Procedure:

1. Output True if the following equality is satisfied, False otherwise:

$$- \left ( \alpha \left ( \Delta - K \, \Delta \, K ^ { T } \right ) ^ { - 1 } \right ) ^ { 2 } = \frac { I } { 4 } \, .$$

Proposition V.5. Algorithm 1 provides a method for verifying that a bosonic Gaussian channel is extreme.

Proof. As stated in Proposition II.16, a bosonic Gaussian channel defined by the matrices ( K,α ) is extreme if and only if it does not exist a matrix γ ≠ α such that α ≥ γ ≥ ± i 2 ( ∆ -K ∆ K T ) ∶= ± i 2 ∆ ′ . To verify that a ( K,α ) Gaussian channel is extreme we have to check that α is minimal among all matrices satisfying α ≥ ± i 2 ∆ ′ . The condition α ≥ ± i 2 ∆ ′ tells us that α is a covariance matrix with respect to the symplectic form ∆ ′ . A covariance matrix of a quantum state is minimal if and only if its symplectic eigenvalues are all equal to 1 / 2 . Recalling Definition II.7, we are therefore interested in the moduli of the eigenvalues of α ∆ ′-1 . Requiring α to be minimal is then equivalent to require that it has all symplectic eigenvalues equal to 1 / 2 , or alternatively that the matrix α ∆ ′-1 has all eigenvalues equal to ± i / 2 , since these are pure imaginary and pairwise opposite, α being a real matrix. This is then equivalent to requiring that the eigenvalues of -(-α ∆ ′-1 ) 2 are all equal to -(± i / 2 ) 2 = 1 / 4 . Being a matrix proportional to the identity, i.e. , with all eigenvalues identical, equal in all bases, this implies that for α to be minimal -(-α ∆ ′-1 ) 2 must equal to I / 4 .

## C. Upper bound

In this section we provide an algorithm to compute an upper bound to the squashed entanglement of any multimode (not necessarily extreme) bosonic Gaussian channel. The squashed entanglement of a quantum channel N A → B can also be written in the alternative form [40, Lemma 4]:

$$E _ { s q } ( \mathcal { N } ) = \sup _ { \hat { \rho } _ { A } } \frac { 1 } { 2 } \inf _ { S _ { E ^ { \prime } \to E ^ { \prime \prime } } } \left ( S ( B | E ^ { \prime \prime } ) _ { \hat { \psi } } + S ( B | F ^ { \prime } ) _ { \hat { \psi } } \right ) , \quad ( 1 5 7 ) \quad \gamma _ { A } \oplus \sigma _ { 1 } \\ \longrightarrow ( I _ { \ }$$

where ˆ ψ = ˆ ψ BE ′′ F ′ is the quantum state given by

$$\hat { \psi } _ { B E ^ { \prime \prime } F ^ { \prime } } = & \, \mathcal { U } _ { E ^ { \prime } F \to E ^ { \prime \prime } F ^ { \prime } } ^ { \mathcal { S } } \mathcal { U } _ { A E \to B E ^ { \prime } } ^ { \mathcal { N } } \left ( \hat { \rho } _ { A } \otimes | 0 \rangle _ { E } \langle 0 | \otimes | 0 \rangle _ { F } \langle 0 | \right ) , \quad \text {where} \\ \\ & \, \quad \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \$$

where U S E ′ F → E ′′ F ′ and U N AE → BE ′ are the unitary quantum channels associated to the unitary dilations of the squashing channel S E ′ → E ′′ and the considered channel N A → B respectively.

Theorem V.6. The squashed entanglement of a bosonic Gaussian channel N satisfies

$$U p p e r \, b o u n d$$

$$E _ { s q } ( \mathcal { N } ) \leq \lim _ { t \to + \infty } \frac { 1 } { 2 } \left ( S ( B | E ^ { \prime \prime } ) _ { \hat { \psi } ( t ) } + S ( B | F ^ { \prime } ) _ { \hat { \psi } ( t ) } \right ) , \\$$

where ˆ ψ ( t ) is the quantum state given by

$$\hat { \psi } _ { B E ^ { \prime \prime } F ^ { \prime } } ( t ) & \coloneqq \mathcal { U } _ { E ^ { \prime } F \rightarrow E ^ { \prime \prime } F ^ { \prime } } ^ { \mathcal { L } } \mathcal { U } _ { A E \rightarrow B E ^ { \prime } } ^ { \mathcal { N } } \left ( \hat { \rho } _ { A } \otimes | 0 \rangle _ { E } \langle 0 | \otimes | 0 \rangle _ { F } \langle 0 | \right ) . \\ \\ & \quad + \mathcal { C }$$

U L E ′ F → E ′′ F ′ is a unitary quantum channels associated to the unitary dilation of a multimode extreme Gaussian attenuator L ∶ E ′ → E ′′ with transmissivity 1 / 2 on all modes and the environment state a generic pure Gaussian state. U N AE → BE ′ is a unitary quantum channels associated to the unitary dilation of the channel N ∶ A → B . ˆ ρ A ( t ) is a bosonic Gaussian state with covariance matrix t γ A , where γ A is an arbitrary positive-definite fixed matrix.

Proof. Our proof is divided into two parts. In the first part we show that

$$\begin{array} { c c } \text {long} & E _ { s q } ( \mathcal { N } ) \leq \sup _ { \gamma _ { A } } \frac { 1 } { 2 } \left ( S ( B | E ^ { \prime \prime } ) _ { \hat { \psi } ( t ) } + S ( B | F ^ { \prime } ) _ { \hat { \psi } ( t ) } \right ) , \\ \text {the} & \end{array} \quad ( 1 6 1 )$$

where ˆ ψ ( t ) is defined in Equation (160). In the second part, we show that the sup in Equation (161) can be restricted to matrices proportional to a given matrix and that Equation (161) is equivalent to Equation (159).

It is convenient to use the equivalent definition (157) of the squashed entanglement of a quantum channel. In what follows, we will consider the channel in Stinespring representation and use the notation of Equation (145). It is not an easy task to optimize over the squashing channel S . Instead, we consider a specific squashing channel: a multimode extreme Gaussian attenuator S = L with transmissivity 1 / 2 on all modes and the environment state a generic pure bosonic Gaussian state. Since the overall channel from A to BE ′′ is Gaussian and the overall channel from A to BF ′ is also Gaussian, it follows from Proposition B.24 that the maximization in Equation (157) can be restricted to the set of Gaussian states. The covariance matrix of the initial state in the system AEF is given by γ A ⊕ σ E ⊕ σ F , where σ E is the covariance matrix of the state of the environment when we consider the physical representation of the channel N as in Equation (145). The beamsplitting operation and the symplectic operation act on the covariance matrices as

$$\gamma _ { A } \oplus \sigma _ { E } \oplus \sigma _ { F } \\ \longrightarrow ( I _ { 2 n } \oplus S _ { 1 / 2 } ) ( S \oplus I _ { 2 n } ) ( \gamma _ { A } \oplus \sigma _ { E } \oplus \sigma _ { F } ) ( S \oplus I _ { 2 n } ) ^ { T } ( I _ { 2 n } \oplus S _ { 1 / 2 } ) ^ { T } , \\$$

where

$$\text {antun} \quad S _ { 1 / 2 } = \frac { 1 } { \sqrt { 2 } } \begin{pmatrix} I _ { 2 n } & I _ { 2 n } \\ - I _ { 2 n } & I _ { 2 n } \end{pmatrix} \quad \text {and} \quad S = \begin{pmatrix} B _ { 1 } ^ { C } & B _ { 2 } ^ { C } \\ B _ { 1 } ^ { D } & B _ { 2 } ^ { D } \end{pmatrix} . \ \ ( 1 6 3 )$$

We obtain

$$\vec { E } _ { s q } ( \mathcal { N } ) & \leq \sup _ { \hat { \rho } _ { A } } \frac { 1 } { 2 } \left ( S ( B | E ^ { \prime \prime } ) _ { \hat { \psi } ( t ) } + S ( B | F ^ { \prime } ) _ { \hat { \psi } ( t ) } \right ) \\ & = \sup _ { \gamma _ { A } } \frac { 1 } { 2 } \left ( S ( B | E ^ { \prime \prime } ) _ { \hat { \psi } ( t ) } + S ( B | F ^ { \prime } ) _ { \hat { \psi } ( t ) } \right ) , \\$$

where we have replaced the sup on Gaussian states with the sup on covariance matrices, the expression in brackets being dependent only on the latter, according to Proposition II.13, and where ˆ ψ ( t ) is the quantum state given by Equation (160). With the same notation as in Lemma B.22, given a Gaussian state ˆ ρ γ A with covariance matrix γ and a bosonic Gaussian channel Φ ∶ A → BE ′′ F ′ , we define the function

$$\bar { S } ( \gamma ) \coloneqq S ( B | E ^ { \prime \prime } ) _ { \Phi ( \hat { \rho } _ { A } ^ { \gamma } ) } + S ( B | F ^ { \prime } ) _ { \Phi ( \hat { \rho } _ { A } ^ { \gamma } ) } \, . \\ \intertext { B C i n g e s w i n g e s i n t i o n w i s e r $ d \rho ( \hat { \rho } _ { A } ^ { \gamma } ) $ }$$

Given a generic positive definite matrix α and a parameter t 4 , let us now prove that sup over all possible covariance matrices of the function ¯ S defined in Equation (165) is equivalent to evaluating that function in the matrix t α and then taking the limit for t going to infinity. First of all, the sup of ¯ S over all possible covariance matrices is surely greater than or equal to the limit for t going to infinity of ¯ S ( t α ) , since the latter case is limited to a particular class of covariance matrices: sup γ A ¯ S ( γ A ) ≥ lim t →+∞ ¯ S ( t α ) . On the other hand, since the quantity in Equation (165) is increasing in the covariance matrix of the input state ˆ ρ A of the channel, from Lemma B.22, if we consider any covariance matrix γ A , for t sufficiently large, t α will be greater than or equal to the matrix γ A , we therefore have sup γ A ¯ S ( γ A ) ≤ lim t →+∞ ¯ S ( t α ) . These two inequalities imply that

4 Every positive definite matrix multiplied by a sufficiently large constant t is a covariance matrix, i.e. , has all symplectic eigenvalues greater than or equal to 1 / 2 (the latter being linear in t ).

$$\sup _ { \gamma _ { A } } \bar { S } ( \gamma _ { A } ) = \lim _ { t \to + \infty } \bar { S } ( t \alpha ) \, . \quad \quad ( 1 6 6 ) \quad b o s o n$$

Remark V.7 . The particular choice we have made for the squashing channel is due to the fact that this choice is known to be optimal for the one-mode extreme bosonic Gaussian attenuator and amplifier.

Remark V.8 . This result greatly simplifies the calculation of the upper bound of the squashed entanglement of a quantum channel. We have in fact reduced the sup over an infinite number of parameters to a limit in a single variable, thus avoiding multiple variable optimisations through, for example, gradient descent.

From Theorem V.6, it is easy to see that the following algorithm provides a method for calculating an upper bound of the form (159) to the squashed entanglement of a generic multimode bosonic Gaussian channel.

$$\text {Algorithm 2 Upper bound to } E _ { s q } ( \mathcal { N } ) \\ \text {t: Two matrices} \ K _ { \ } \alpha \in \mathbb { R } ^ { 2 n \times 2 n } \ \text {describing a host}$$

Output: A constant C UB such that E sq (N) ≤ C UB . Procedure:

Input: Two matrices K,α ∈ R 2 n × 2 n describing a bosonic Gaussian channel N .

Calculate numerically the limit C UB = lim t →+∞ C UB ( t ) , where the quantity C UB ( t ) is computed as follows.

1. From matrices K,α , derive an environment-state covariance matrix σ E ∈ R 2 n × 2 n &gt; 0 and a coupling symplectic matrix S ∈ Sp ( 4 n, R ) describing the bosonic Gaussian channel in Stinespring representation as in [44, Section 5.3].

2. Evaluate the matrix σ BE ′′ F ′ ( t ) :

$$( I _ { 2 n } \oplus S _ { 1 / 2 } ) ( S \oplus I _ { 2 n } ) ( t \, I _ { 2 n } \oplus \sigma _ { E } \oplus \sigma _ { F } ) ( S \oplus I _ { 2 n } ) ^ { T } ( I _ { 2 n } \oplus S _ { 1 / 2 } ) ^ { T } , \quad \\ \intertext { ( I _ { 2 n } \oplus S _ { 1 / 2 } ) ( S \oplus I _ { 2 n } ) ( t \, I _ { 2 n } \oplus \sigma _ { E } \oplus \sigma _ { F } ) ( S \oplus I _ { 2 n } ) ^ { T } ( I _ { 2 n } \oplus S _ { 1 / 2 } ) ^ { T } , \quad \\ \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ( 1 6 7 ) } \intertext { ($$

where S 1 / 2 is defined in Equation (163) and σ F the environment-state covariance matrix of a multimode bosonic Gaussian channel.

3. Calculate the symplectic eigenvalues { ν j σ ( t )} j of the matrices: σ E ′′ ( t ) , σ F ′ ( t ) , σ BE ′′ ( t ) , σ BF ′ ( t ) ;

4. Compute the quantity:

$$\# \colon C o n p d a c { \text { the quantity} } . & & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \quad & \text {state has} \$$

## D. Lower bound

In this section, we provide an algorithm for calculating a lower bound to the squashed entanglement of any multimode extreme bosonic Gaussian channel. The proof of this algorithm is based on Theorem IV.3 and on the definition (157) of the squashed entanglement of a quantum channel. Regarding this last definition, the results for attenuator and amplifier [42] lead us to formulate the following

Conjecture V.9. For any bosonic Gaussian channel N , the optimal squashing channel in Equation (158) is always a bosonic Gaussian channel.

$$\text {Algorithm 3 Lower bound to } E _ { s q } ( \mathcal { N } ) \\ \text {at} \colon T w o \text { matrices } K _ { \ } \alpha \in \mathbb { R } ^ { 2 n \times 2 n } \text { describing an ext}$$

Input: Two matrices K,α ∈ R 2 n × 2 n describing an extreme bosonic Gaussian channel N , an average number of photons N .

Output: A constant C LB such that C LB ≤ E sq (N) . Procedure:

Calculate numerically the limit C LB = lim N →+∞ C LB ( N ) , where the quantity C LB ( N ) is computed as follows.

1. Build the matrix:

$$\begin{array} { c c } \text {tuple,} & \sigma _ { C D } ( N ) = ( I _ { 2 n } \oplus K ) \, \sigma _ { A B } ( N ) \, ( I _ { 2 n } \oplus K ) ^ { T } + ( 0 _ { 2 n } \oplus \alpha ) \, , \\ & \text {wiring} & \sigma _ { C D } ( N ) = ( I _ { 2 n } \oplus K ) \, \sigma _ { A B } ( N ) \, ( I _ { 2 n } \oplus K ) ^ { T } + ( 1 6 9 ) \end{array}$$

where σ AB ( N ) ∈ R 4 n × 4 n &gt; 0 is the covariance matrix of the tensor product of n two-mode squeezed vacuum states with average number of photons per mode N .

2. Find a symplectic matrix (which exists according to Williamson's theorem, Theorem B.2) S ∈ Sp ( 4 n, R ) such that the matrix

$$S \sigma _ { C D } ( N ) \, S ^ { T }$$

is diagonal.

3. With the same notation of Equation (98), compute the quantity:

$$C _ { L B } ( N ) = \frac { n } { 2 } \ln \left ( 2 \, b _ { 1 } ^ { C } b _ { 1 } ^ { D } + b _ { 1 } ^ { D } b _ { 2 } ^ { C } + b _ { 1 } ^ { C } b _ { 2 } ^ { D } \right ) .$$

Theorem V.10. Every constant C LB ( N ) computed by the Algorithm 3 is a lower bound to the squashed entanglement of a generic multimode extreme bosonic Gaussian channel.

Proof. Any choice of the input state will provide a lower bound to the squashed entanglement of the quantum channel. We choose as input state the tensor product ∣ ϕ N ⟩ AR ⟨ ϕ N ∣ of n two-mode squeezed vacuum states with average number of photons per mode N . From Proposition V.4, when an extreme bosonic Gaussian channel acts on half of a pure Gaussian state the covariance matrix of the resulting output state has at least half of its symplectic eigenvalues equal to 1 / 2 . This insight enables us to represent the output state in the form given by Equation (96). In particular, the proof of Williamson's theorem (Theorem B.2) states that a symplectic matrix that diagonalises the covariance matrix σ CD is given by S = Mσ -1 / 2 CD , where M is a non-singular matrix that brings the antisymmetric real matrix ∆ ′ = σ -1 / 2 CD ∆ σ -1 / 2 CD into canonical form, as discussed in Lemma B.14. Subsequently, having the explicit form for the matrix S , thanks to Theorem IV.3, we can determine a lower bound to the squashed entanglement of the output state ( ✶ A ⊗N B )(∣ ϕ N ⟩ AR ⟨ ϕ N ∣) , using the expression in Equation (101). Finally, sending the average number of photons per mode N of the tensor product of n twomode squeezed vacuum states to infinity, makes the constant C LB = lim N →+∞ C LB ( N ) still a lower bound to the squashed entanglement of the channel. This last step is justified by the fact that in the one-mode case this limit provides the optimal lower bound to the squashed entanglement for the extreme Gaussian attenuator and amplifier.

In the case of the one-mode extreme Gaussian attenuator and amplifier, the lower bound to the squashed entanglement obtained with the above method is sharp and coincides with the actual value of the squashed entanglement [42]. In the next section we will explicitly show a numerical example of the calculation of this quantity.

## E. Some relevant examples

In this subsection, we show how our results (Algorithm 2 and Algorithm 3) for the lower and upper bound of the squashed entanglement for multimode extreme bosonic Gaussian channels are perfectly compatible with known results for some very important examples of one-mode extreme bosonic Gaussian channels, i.e. , the one-mode noiseless bosonic Gaussian attenuator and the one-mode noiseless bosonic Gaussian amplifier [42].

1) One-mode noiseless bosonic Gaussian attenuator:

a) Lower bound.: Let us begin by computing the lower bound of a one-mode pure-loss bosonic Gaussian attenuator. To do this we apply step by step Algorithm 3 with n = 1 .

- 1) With the same notation as in Algorithm 3 and thanks to Equations (199), (44) and (283) we have:

$$E q u t i o n s \left ( 1 9 9 \right ) , \left ( 4 4 \right ) \text { and } \left ( 2 8 3 \right ) \text { we have:} \\ \sigma _ { A B } ( N ) = \begin{pmatrix} \left ( \left ( N + \frac { 1 } { 2 } \right ) I _ { 2 } & \sqrt { N ( N + 1 ) } \, Z _ { 2 } \\ \sqrt { N ( N + 1 ) } \, Z _ { 2 } & \left ( ^ { N + \frac { 1 } { 2 } } \right ) I _ { 2 } \end{pmatrix} , \\ K = \sqrt { \eta } \, I _ { 2 } \quad \text {and} \quad \alpha = \frac { 1 - \eta } { 2 } \, I _ { 2 } \, .$$

From Equation (169) therefore follows

$$\sigma _ { C D } ( N ) = \begin{pmatrix} \left ( N + \frac { 1 } { 2 } \right ) I _ { 2 } & \sqrt { \eta N ( N + 1 ) } \, Z _ { 2 } \\ \sqrt { \eta N ( N + 1 ) } \, Z _ { 2 } & \left ( \eta N + \frac { 1 } { 2 } \right ) I _ { 2 } \end{pmatrix} . \\ \intertext { 2 } \intertext { 3 } I \text { is easy to verify that a symmetric matrix that diago-}$$

- 2) It is easy to verify that a symplectic matrix that diagonalises σ CD ( N ) is given by

$$\text {sises } \sigma _ { C D } ( N ) \text { is given by} \\ S _ { \kappa ^ { \prime } } = \left ( \sqrt { \kappa ^ { \prime } } \, I _ { 2 } \quad \sqrt { \kappa ^ { \prime } - 1 } \, Z _ { 2 } \right ) , \\ \kappa ^ { \prime } = \frac { N + 1 } { ( 1 - \eta ) N + 1 } \, . \\ \intertext { m e q uation } \text {m} \, E q uation \, ( 1 7 3 ) , \, i t \, i s \, e a s y \, t o \, s e e \, t h a t \, the \, q u n t i ties$$

- 3) From Equation (173), it is easy to see that the quantities defined in Theorem IV.3 are b C 1 = b D 2 = k ′ and b D 1 = b C 2 = k ′ -1 , from which it follows that Equation (170) takes the form

$$C _ { L B } ( N ) = \ln ( 2 \kappa ^ { \prime } - 1 ) \\ \stackrel { N \to + \infty } { \longrightarrow } \ln \left ( \frac { 1 - \eta } { 1 + \eta } \right ) . \\$$

b) Upper bound: Although the upper bound for this channel has already been proved in [40], [48], [49], we compare this result with our new algorithm Algorithm 2 for calculating the upper bound.

- 1) Thanks to Equations (163) and (44) and fixing the state of the system F to be the vacuum state, it holds

$$S _ { 1 / 2 } & = \frac { 1 } { \sqrt { 2 } } \begin{pmatrix} I _ { 2 } & I _ { 2 } \\ - I _ { 2 } & I _ { 2 } \end{pmatrix} , \\ S _ { \eta } & = \begin{pmatrix} \sqrt { \eta } \, I _ { 2 } & \sqrt { 1 - \eta } \, I _ { 2 } \\ - \sqrt { 1 - \eta } \, I _ { 2 } & \sqrt { \eta } \, I _ { 2 } \end{pmatrix} , \\ \sigma _ { E } & = \sigma _ { F } = \frac { 1 } { 2 } \, I _ { 2 } \, , \\ \intertext { k s . t . } \text {Equals } ( 1 6 7 ) , \, \sigma _ { B F } \prime \prime \prime ( t ) \text { then turns to be }$$

- 2) Thanks to Equation (167), σ BE ′′ F ′ ( t ) then turns to be

$$\sigma _ { B E ^ { \prime } F ^ { \prime } } ( t ) = \begin{pmatrix} \left ( \frac { \eta ( t - \frac { 1 } { 2 } ) + \frac { 1 } { 2 } \right ) I _ { 2 } & \frac { 1 } { 2 \sqrt { 2 } } \sqrt { \eta } ( 1 - 2 t ) \, I _ { 2 } & \frac { 1 } { 2 \sqrt { 2 } } \sqrt { \eta } ( 2 t - 1 ) \, I _ { 2 } \\ \frac { 1 } { 2 \sqrt { 2 } } \sqrt { \eta } ( 1 - 2 t ) \, I _ { 2 } & \frac { 1 } { 4 } \left ( \eta + 2 \bar { \eta } t + 1 \right ) \, I _ { 2 } & \frac { 1 } { 4 } \bar { \eta } \left ( 1 - 2 t \right ) \, I _ { 2 } \\ \frac { 1 } { 2 \sqrt { 2 } } \sqrt { \eta } ( 1 - 2 t ) \, I _ { 2 } & \frac { 1 } { 4 } \bar { \eta } \left ( 1 - 2 t \right ) \, I _ { 2 } & \frac { 1 } { 4 } \left ( \eta + 2 \bar { \eta } t + 1 \right ) \, I _ { 2 } \end{pmatrix} .$$

- 3) We must now compute the symplectic eigenvalues of the matrices σ BE ′′ , σ BF ′ , σ E ′ and σ F ′ , which are respectively

$$\nu _ { \sigma _ { B E ^ { \prime \prime } } } = \nu _ { \sigma _ { B F ^ { \prime } } } = \left \{ \frac { 1 } { 2 } , \frac { 1 } { 4 } \left ( 1 - \eta + 2 t ( 1 + \eta ) \right ) \right \} , \\ \nu _ { \sigma _ { E ^ { \prime \prime } } } = \nu _ { \sigma _ { F ^ { \prime } } } = \frac { 1 } { 4 } \left ( 1 + 2 t ( 1 - \eta ) + \eta \right ) . \quad \text {Let us}$$

- 4) The upper bound in Equation (168) then becomes

$$C _ { U B } ( t ) & = \left [ g ( 0 ) + g \left ( \frac { 1 } { 4 } \left ( 1 - \eta + 2 t ( 1 + \eta ) \right ) \right ) + \\ & - g \left ( \frac { 1 } { 4 } \left ( 1 + 2 t ( 1 - \eta ) + \eta \right ) \right ) \right ] \\ & \stackrel { t \to + \infty } { \longrightarrow } \ln \left ( \frac { 1 + \eta } { 1 - \eta } \right ) . \\ \text {Let us observe that the values for the lower and upper bound}$$

Let us observe that the values for the lower and upper bound computed via Algorithm 3 and Algorithm 2 coincide, thus providing the exact value for the squashed entanglement of a one-mode noisless bosonic Gaussian attenuator, a result already proved in [42].

2) One-mode noisless bosonic Gaussian amplifier: In this example, we are going to compute the squashed entanglement of a one-mode noisless bosonic Gaussian amplifier and verify that the results provided by Algorithm 2 and Algorithm 3 are compatible with the results shown in [42].

a) Lower bound: Let us begin compute the lower bound of a one-mode noisless bosonic Gaussian amplifier. Let us apply step by step Algorithm 3 with n = 1 .

- 1) With the same notation as in Algorithm 3 and thanks to Equations (199), (45) and (283) we have:

$$E q u a t i o n s \left ( 1 9 9 \right ) , \, ( 4 5 ) \text { and } ( 2 8 3 ) \text { we have:} & & \text {calcular} \\ \sigma _ { A B } ( N ) = \begin{pmatrix} \left ( \left ( N + \frac { 1 } { 2 } \right ) I _ { 2 } & \sqrt { N ( N + 1 ) } \, Z _ { 2 } \\ \sqrt { N ( N + 1 ) } \, Z _ { 2 } & \left ( ^ { N + \frac { 1 } { 2 } } \right ) I _ { 2 } \end{pmatrix} , \\ K = \sqrt { \kappa } \, I _ { 2 } & \text { and } & \alpha = \frac { \kappa - 1 } { 2 } \, I _ { 2 } \, . \\ \text {From Equation } ( 1 6 9 ) \text { it holds}$$

From Equation (169) it holds

$$From Equation ( 1 6 9 ) \, i t h o l d s \\ \sigma _ { C D } ( N ) = \left ( \begin{array} { c c } \left ( N + \frac { 1 } { 2 } \right ) I _ { 2 } & \sqrt { \eta \, N ( N + 1 ) } \, Z _ { 2 } \\ \sqrt { \eta \, N ( N + 1 ) } \, Z _ { 2 } & \left ( \eta \, N + \frac { 1 } { 2 } \right ) I _ { 2 } \end{array} \right ) . \\ \intertext { 2 } I \, i s \, e a l y \, t o \, \text {verify that a symmetric matrix that diago-}$$

- 2) It is easy to verify that a symplectic matrix that diagonalises σ CD ( N ) is given by

$$\text {ises } \sigma _ { C D } ( N ) \text { is given by} \\ S _ { \kappa ^ { \prime } } = \left ( \sqrt { \kappa ^ { \prime } } \, I _ { 2 } \quad \sqrt { \kappa ^ { \prime } - 1 } \, Z _ { 2 } \right ) , \\ \kappa ^ { \prime } = \frac { \kappa ( N + 1 ) } { ( \kappa - 1 ) N + 1 } \, . \\$$

$$\sigma _ { B E } { " F } ^ { ( t ) } = \left ( \begin{array} { c c c } \frac { 1 } { 2 } ( 2 \kappa t + \bar { \kappa } ) \, I _ { 2 } & \frac { 1 } { 2 \sqrt { 2 } } \sqrt { \kappa } ( 2 t + 1 ) \, Z _ { 2 } & - \frac { 1 } { 2 \sqrt { 2 } } \sqrt { \kappa } ( 2 t + 1 ) \, Z _ { 2 } \\ \frac { 1 } { 2 } \sqrt { \kappa } ( 2 t + 1 ) \, Z _ { 2 } & \frac { 1 } { 4 } ( 2 \bar { \kappa } t + \kappa + 1 ) \, I _ { 2 } & - \frac { 1 } { 4 } \bar { \kappa } ( 2 t + 1 ) \, I _ { 2 } \\ - \frac { 1 } { 2 \sqrt { 2 } } \sqrt { \kappa } ( 2 t + 1 ) \, Z _ { 2 } & - \frac { 1 } { 4 } \bar { \kappa } ( 2 t + 1 ) \, I _ { 2 } & \frac { 1 } { 4 } ( 2 \bar { \kappa } t + \kappa + 1 ) \, I _ { 2 } \end{array} \right ) .$$

- 3) At this point, the algorithm Algorithm 2 requires computing the symplectic eigenvalues of the matrices, σ BE ′′ , σ BF ′ , σ E ′′ and σ F ′ , which are respectively:

$$\nu _ { \sigma _ { B E } } & = \nu _ { \sigma _ { B F } } = \left \{ \frac { 1 } { 2 } , \frac { 1 } { 4 } ( \kappa - 1 + 2 t ( 1 + \kappa ) ) \right \} , & \text {value for} \\ \nu _ { \sigma _ { E } } & = \nu _ { \sigma _ { F } } = \frac { 1 } { 4 } \left ( 1 + 2 t ( \kappa - 1 ) + \kappa \right ) . & \text {In the}$$

- 4) The upper bound in Equation (168) then becomes

$$C _ { U B } ( t ) = & \left [ g ( 0 ) + g \left ( \frac { 1 } { 4 } ( \kappa - 1 + 2 t ( 1 + \kappa ) ) \right ) + \left [ \begin{array} { c c } \text {of a } m \\ \text {loss of } \\ \text {number} \\ - g \left ( \frac { 1 } { 4 } ( 1 + 2 t ( \kappa - 1 ) + \kappa ) \right ) \right ] \\ \stackrel { t \rightarrow + \infty } { \longrightarrow } \ln \left ( \frac { 1 + \kappa } { \kappa - 1 } \right ) .$$

Also in the example of a one-mode noisless bosonic Gaussian amplifier, the calculation of the lower bound via Algorithm 3 coincides with the calculation of the upper bound found using Algorithm 2. We have therefore determined the exact value for the squashed entanglement of a one-mode noisless bosonic Gaussian amplifier, a result already proved in [42].

## VI. NUMERICAL SIMULATIONS

In this section we present some numerical results regarding the lower and upper bounds to the squashed entanglement of a multimode extreme bosonic Gaussian channel. Without loss of generality, for this numerical simulation we set the number of modes of each system equal to 2 . We will consider a Gaussian attenuator with different attenuation parameters on each mode, and the state of the environment E interacting with the state of the input system A is assumed to be a twomode squeezed vacuum state. This particular choice of the

- 3) From Equation (173), it is easy to see that the quantities defined in Theorem IV.3 are b C 1 = b D 2 = κ ′ and b D 1 = b C 2 = κ ′ -1 , from which it follows that Equation (170) takes the form

$$C _ { L B } ( N ) = \ln ( 2 \kappa ^ { \prime } - 1 ) \\ \stackrel { N \rightarrow + \infty } { \longrightarrow } \ln \left ( \frac { \kappa + 1 } { \kappa - 1 } \right ) . \\$$

b) Upper bound.: As mentioned for the one-mode noisless bosonic Gaussian attenuator, also the upper bound for this channel has already been proved in [40], [48], [49]. We compare this result with our new algorithm Algorithm 2 for calculating the upper bound.

- 1) Thanks to Equations (163) and (44) and fixing the state of the system F to be the vacuum state, we have:

$$S _ { 1 / 2 } & = \frac { 1 } { \sqrt { 2 } } \begin{pmatrix} I _ { 2 } & I _ { 2 } \\ - I _ { 2 } & I _ { 2 } \end{pmatrix} , \\ S _ { \kappa } & = \begin{pmatrix} \sqrt { \kappa } \, I _ { 2 } & \sqrt { \kappa - 1 } \, Z _ { 2 } \\ \sqrt { 1 - \kappa } \, Z _ { 2 } & \sqrt { \kappa } \, I _ { 2 } \end{pmatrix} , \\ \sigma _ { E } & = \sigma _ { F } = \frac { 1 } { 2 } \, I _ { 2 } \, , \\ \intertext { k s . t . } \intertext { o f u a t i o n } \, ( 1 6 7 ) \, \sigma _ { P } \rho _ { E } \rho _ { V } ( t ) \, \text { then } \, \text { turns to be }$$

- 2) Thanks to Equation (167), σ BE ′′ F ′ ( t ) then turns to be

channel is clearly inspired by reality, however the strategy we are going to follow is completely generic and can be applied to any extreme bosonic Gaussian channel on an arbitrary number of modes. In formulae, the channel we are going to consider is defined as

$$\mathcal { N } _ { A \to B } ^ { ( \eta _ { 1 } , \eta _ { 2 } , \kappa ) } ( \hat { \rho } _ { A } ) = t r _ { E } \left [ \hat { U } _ { A E } ^ { ( \eta _ { 1 } , \eta _ { 2 } ) } \left ( \hat { \rho } _ { A } \otimes \hat { \phi } _ { E } ^ { \kappa } \right ) \hat { U } _ { A E } ^ { ( \eta _ { 1 } , \eta _ { 2 } ) } \right ] , \, ( 1 8 7 )$$

where ˆ U ( η 1 ,η 2 ) AE is the unitary operator implementing the symplectic matrix

$$S _ { A E } ^ { ( \eta _ { 1 } , \eta _ { 2 } ) } = \begin{matrix} A _ { 1 } & A _ { 2 } & E _ { 1 } & E _ { 2 } \\ B _ { 1 } & \sqrt { \eta _ { 1 } } I _ { 2 } & 0 & \sqrt { \bar { \eta } _ { 1 } } I _ { 2 } & 0 \\ 0 & \sqrt { \eta _ { 2 } } I _ { 2 } & 0 & \sqrt { \bar { \eta } _ { 2 } } I _ { 2 } \\ E _ { 1 } & - \sqrt { \bar { \eta } _ { 1 } } I _ { 2 } & 0 & \sqrt { \eta _ { 1 } } I _ { 2 } & 0 \\ 0 & - \sqrt { \bar { \eta } _ { 1 } } I _ { 2 } & 0 & \sqrt { \eta _ { 1 } } I _ { 2 } & \text {value of } \pi \\ \end{matrix} \quad \text {attnuation} \\ \text {where } \bar { \eta } _ { i } = 1 - \eta _ { i } , i = 1 , 2 , \text { whereas the state of the envi-} \ \text {Remark}$$

where ¯ η i = 1 -η i , i = 1 , 2 , whereas the state of the environment ˆ ϕ κ E = ∣ ϕ κ ⟩ E ⟨ ϕ κ ∣ = ˆ U κ E ∣ 00 ⟩ E ⟨ 00 ∣ ˆ U κ E † is the twomode squeezed vacuum state with squeezing parameter κ &gt; 0 . Systems A , B and E are two-mode bosonic quantum systems respectively made up by the one-mode bosonic quantum systems A 1 , A 2 , B 1 , B 2 and E 1 , E 2 .

First of all, we observe that, as proved in Section C-A, the bosonic Gaussian channel we are considering is indeed extreme. Regarding the explicit lower and upper bounds calculation, instead, please refer to Section C-B and Section C-C. Here we present some plots showing the behaviour of the lower and upper bounds of the squashed entanglement of the channel taken into account by varying certain parameters of interest.

Figure 1. Lower bound (blue line) and upper bound (orange line) to the squashed entanglement of the channel N ( η 1 ,η 2 ,κ ) A → B as a function of the squeezing parameter κ of the environment state, fixed η 1 = 0 . 5 and η 2 = 0 . 25 . The upper bound has been obtained by considering as a squashing channel a bosonic Gaussian attenuator with transmissivity 1 / 2 and the environment state a two-mode squeezed vacuum state and optimising on this squeezing parameter for each value of κ .

<!-- image -->

Figure 2. Lower bound (blue line) and upper bound (orange line) of the squashed entanglement of the channel N ( η 1 ,η 2 ,κ ) A → B as a function of the attenuation parameter η 2 , fixed η 1 = 0 . 5 and κ = 4 . 0 . The upper bound has been obtained by considering as a squashing channel a bosonic Gaussian attenuator with transmissivity 1 / 2 and the environment state a two-mode squeezed vacuum state and optimising on this squeezing parameter for each value of η 2 .

<!-- image -->

Remark VI.1 . We observe that, in the graph in Figure 1, for κ = 0 we get back to the case discussed in [42, Theorem 2] and thus exactly determine the squashed entanglement of this channel, E sq (N ( η 1 ,η 2 , 0 ) A → B ) = ln ( 1 + η 1 1 -η 1 ) + ln ( 1 + η 2 1 -η 2 ) , where we used the additivity of the squashed entanglement with respect to the tensor product of quantum channels [40, Corollary 8].

Remark VI.2 . Knowing that applying a quantum channel to a state can only decrease the squashed entanglement of the state, i.e. ,

$$E _ { s q } ( \Phi ( \hat { \rho } ) ) & \leq E _ { s q } ( \hat { \rho } ) \, , \\ \\ \\ 1 _ { \Phi } + 1 _ { \Phi } & = 1 _ { \Phi }$$

it is easy to show that the squashed entanglement of a composition of quantum channels is smaller or equal to the squashed entanglement of the individual channels, i.e. ,

$$E _ { s q } ( \Phi _ { 2 } \circ \Phi _ { 1 } ) & \leq E _ { s q } ( \Phi _ { 1 } ) , E _ { s q } ( \Phi _ { 2 } ) \, . \\ \\ \\ E _ { s q } ( \Phi _ { 2 } \circ \Phi _ { 1 } ) & \leq E _ { s q } ( \Phi _ { 1 } ) , E _ { s q } ( \Phi _ { 2 } ) \, .$$

The proof is straightforward. For the channel Φ 2 it holds:

$$E _ { s q } ( \Phi _ { 2 } \circ \Phi _ { 1 } ) & = \sup _ { \hat { \rho } _ { A B } } E _ { s q } ( ( \mathbb { 1 } \otimes \Phi _ { 2 } \circ \Phi _ { 1 } ) ( \hat { \rho } _ { A B } ) ) \\ & \leq \sup _ { \hat { \tau } _ { A B } } E _ { s q } ( ( \mathbb { 1 } \otimes \Phi _ { 2 } ) ( \hat { \tau } _ { A B } ) ) \\ & \coloneqq E _ { s q } ( \Phi _ { 2 } ) \, , \\ \intertext { w h e u s e d t h e f a c t h a t o t i m i sation for the compositions }$$

where we used the fact that optimisation for the compositions of the channels Φ 1 and Φ 2 is suboptimal compared to optimisation for the channel Φ 2 alone. For the channel Φ 1 it holds:

$$E _ { s q } ( \Phi _ { 2 } \circ \Phi _ { 1 } ) & = \sup _ { \hat { \rho } _ { A B } } E _ { s q } ( ( \mathbb { 1 } \otimes \Phi _ { 2 } \circ \Phi _ { 1 } ) ( \hat { \rho } _ { A B } ) ) \\ & \leq \sup _ { \hat { \rho } _ { A B } } E _ { s q } ( ( \mathbb { 1 } \otimes \Phi _ { 1 } ) ( \hat { \rho } _ { A B } ) ) \\ & \div E _ { s q } ( \Phi _ { 1 } ) \, , \\ \intertext { t o r } \text { where } \text { we used } \text { Equation } ( 1 8 9 ) \text { applied to the channel } \Phi _ { 2 } .$$

where we used Equation (189) applied to the channel Φ 2 . It is therefore easy now to understand why the bounds in Figure 2 decrease as η 2 decreases. Indeed, from the wellknown composition rule for bosonic Gaussian attenuators ( E η 2 ○ E η 1 = E η 2 η 1 ), decreasing η 2 is equivalent to applying a further attenuator to the system A 2 and thus the squashed entanglement is expected to decrease.

Remark VI.3 . An important observation on the graph in Figure 2 is that for η 1 = η 2 the lower bound coincides with the upper bound and thus we we are able to exactly determine the squashed entanglement of the channel N ( η 1 ,η 2 ,κ ) A → B taken into consideration. This follows from the fact that the squashed entanglement is additive for the tensor product of channels and if η 1 = η 2 the channel we are considering is the two-mode extension of the extreme bosonic Gaussian attenuator studied in [42, Theorem 2]. This result follows from the observation that applying a symplectic trasformation to one input of a beam splitter with attenuation parameters η i = η ∀ i is equivalent to applying that symplectic to the output and its inverse to the other input, as proven in Lemma B.26. With the same notation of Lemma B.26, if the symplectic transformation we are going to consider is the squeezing operation, then the channel whose squashed entanglement we are going to calculate is given by

$$\Phi _ { \eta } ^ { \hat { U } _ { \kappa } \left | 0 \right \rangle \left \langle 0 \right | \hat { U } _ { \kappa } ^ { \dagger } } ( \cdot ) = \hat { U } _ { \kappa } \, \Phi _ { \eta } ^ { \left | 0 \right \rangle \left \langle 0 \right | } ( \hat { U } _ { \kappa } ^ { \dagger } \cdot \hat { U } _ { \kappa } ) \, \hat { U } _ { \kappa } ^ { \dagger } , \quad ( 1 9 3 ) \quad ^ { 1 / 2 , \ a n d } \\ \intertext { \ } \ w h o r b e \left | 0 \right \rangle \cdot \left | 0 0 \right \rangle \, \text {This, among, that, among, the, a } \ w h o r e \colon \quad \text {vacuum} \quad .$$

where ∣ 0 ⟩ ∶= ∣ 00 ⟩ . This means that applying the squeezing to one input of the beam splitter is equivalent to applying it to the output of the channel and applying its inverse to the other input. Now, being the squashed entanglement an entanglement measure [26], and thus invariant under local unitaries [50], [51], it holds

$$[ 1 ] , & \, \imath \, \text {mod} \, S \\ E _ { \text {sq} } ( ( \hat { \imath } \otimes \hat { U } _ { \kappa } ) [ \mathbb { I } \otimes \Phi _ { \eta } ^ { | 0 | \times 0 | } ( \hat { U } _ { \kappa } ^ { \dagger } \cdot \hat { U } _ { \kappa } ) ] ( \hat { \mathbb { I } } \otimes \hat { U } _ { \kappa } ^ { \dagger } ) ) \\ & = E _ { \text {sq} } ( ( \mathbb { I } \otimes \Phi _ { \eta } ^ { | 0 \times 0 | } ) ( \hat { U } _ { \kappa } ^ { \dagger } \cdot \hat { U } _ { \kappa } ) ) \, . \\$$

Finally, the optimisation on the input states of the channel implies that

$$\text {graph in} \quad E _ { s q } ( \Phi _ { \eta } ^ { | 0 \times 0 | } ( \hat { U } _ { \kappa } ^ { \dagger } \cdot \hat { U } _ { \kappa } ) ) & = \sup _ { \hat { \rho } _ { A B } } E _ { s q } ( ( 1 \otimes \Phi _ { \eta } ^ { | 0 \times 0 | } ) ( \hat { U } _ { \kappa } ^ { \dagger } \hat { \rho } _ { A B } \hat { U } _ { \kappa } ) ) \\ & = \sup _ { \hat { \rho } _ { A B } } E _ { s q } ( ( 1 \otimes \Phi _ { \eta } ^ { | 0 \times 0 | } ) ( \hat { \rho } _ { A B } ) ) \\ & \quad = E _ { s q } ( \Phi _ { \eta } ^ { | 0 \times 0 | } ) \, . \\ \intertext { t h e r } \text {one into} & \quad \hat { \rho } _ { A B } \\ & = E _ { s q } ( \Phi _ { \eta } ^ { | 0 \times 0 | } ) \, . \\ \intertext { b o t h e r } \text {mode} & \quad - \text {e} _ { \kappa } . \\$$

We have thus shown that the case η 1 = η 2 is equivalent to the trivial two-mode extension of the squashed entanglement calculation for a one-mode extreme Gaussian attenuator, as discussed in [42, Theorem 2].

Remark VI.4 . Another observation that can be made is the following. If the channel N ( η 1 ,η 2 ,κ ) A → B defined in Equation (187) is characterised by having η 1 = η 2 then the optimal squashing channel for the squashed entanglement calculation, according to the definition (157), is a two-mode Gaussian attenuator, with the two attenuation parameters both equal to 1 / 2 , and with the environment state a two-mode squeezed vacuum state with squeezing parameter κ , the same squeezing parameter that appears in N ( η 1 ,η 2 ,κ ) A → B . Let N κ η be a two-mode Gaussian attenuator with both attenuation parameters equal to η and environment state a two-mode squeezed vacuum state with squeezing parameter κ . Let U κ X (⋅) ∶= ( ˆ U κ ) X ⋅ ( ˆ U † κ ) X be the squeezing unitary channel on system X with attenuation parameter κ defined in Section II-C. Given a quantum state ˆ ρ BE ′′ F ′ of the system BE ′′ F ′ , let's define the function ¯ S ( ˆ ρ BE ′′ F ′ ) ∶= S ( B ∣ E ′′ ) ˆ ρ BE ′′ F ′ + S ( B ∣ F ′ ) ˆ ρ BE ′′ F ′ . It holds

$$E _ { \text {sq} } ( \mathcal { N } ) & = \sup _ { \hat { \rho } _ { A } } \frac { 1 } { 2 } \inf _ { S ^ { \prime } _ { E ^ { \prime } - E ^ { \prime \prime } } } \left ( \bar { S } ( U _ { E ^ { \prime } F \to E ^ { \prime \prime } F } ^ { S } U _ { A E ^ { \prime } - B E ^ { \prime } } ^ { \mathcal { N } ^ { \prime } _ { \eta } } \left ( \hat { \rho } _ { A } \otimes | 0 \rangle _ { E } ( | 0 \rangle _ { F } \langle 0 | ) \right ) \right ) \\ & = \sup _ { \hat { \rho } _ { A } } \frac { 1 } { 2 } \inf _ { S ^ { \prime } _ { E ^ { \prime } - E ^ { \prime \prime } } } \left ( \bar { S } ( U _ { E ^ { \prime } F \to E ^ { \prime \prime } F } ^ { S } U _ { B E ^ { \prime } } ^ { \mathcal { N } ^ { \prime } _ { \eta } } U _ { A E ^ { \prime } - B E ^ { \prime } } ^ { \mathcal { N } ^ { \prime } _ { A } } \left ( \hat { \rho } _ { A } \otimes | 0 \rangle _ { E } ( | 0 \rangle _ { F } ( | 0 \rangle _ { F } ( | 0 | ) ) \right ) \right ) \\ & = \sup _ { \hat { \rho } _ { A } } \frac { 1 } { 2 } \inf _ { S ^ { \prime } _ { E ^ { \prime } - E ^ { \prime \prime } } } \left ( \bar { S } ( U _ { E ^ { \prime } F \to E ^ { \prime \prime } F } ^ { S } U _ { B E ^ { \prime } } ^ { \mathcal { N } ^ { \prime } _ { \eta } } U _ { A E ^ { \prime } - B E ^ { \prime } } ^ { \mathcal { N } ^ { \prime } _ { A } } \left ( \hat { \rho } _ { A } \otimes | 0 \rangle _ { E } ( | 0 \rangle _ { F } ( | 0 \rangle _ { F } ( | 0 | ) ) \right ) \right ) \\ & = \sup _ { \hat { \rho } _ { A } } \frac { 1 } { 2 } \inf _ { S ^ { \prime } _ { E ^ { \prime } - E ^ { \prime \prime } } } \left ( \bar { S } ( U _ { E ^ { \prime } F \to E ^ { \prime \prime } F } ^ { S } U _ { E ^ { \prime } F \to E ^ { \prime } } ^ { \mathcal { N } ^ { \prime } _ { \eta } } U _ { A E ^ { \prime } - B E ^ { \prime } } ^ { \mathcal { N } ^ { \prime } _ { A } } \left ( \hat { \rho } _ { A } \otimes | 0 \rangle _ { E } ( | 0 \rangle _ { F } ( | 0 \rangle _ { F } ( | 0 | ) ) \right ) \right ) .$$

In the second equality we used the fact that applying a symplectic unitary (in our case the squeezing operator) to the two outputs of a beam splitter and its inverse to the two inputs leaves the overall transformation unchanged (Lemma B.26). In the third equality, we simply incorporated the squeezing unitary channel U κ † A when we optimise over all possible input states ˆ ρ A . Finally, in the fourth equality we used the fact that U κ BE ′ is factorised on the systems on which it acts, i.e. , U κ BE ′ = U κ B ⊗U κ E ′ , and that ¯ S is invariant under local unitaries. Now, for the additivity of squashed entanglement under the tensor product of channels and from Ref.s [40], [42], we know that the optimal squashing channel S is such that it holds U S E ′ F → E ′′ F ′ U κ E ′ = U N 0 1 / 2 E ′ F → E ′′ F ′ . Whence, in our case, the unitary extension of the squashing channel satisfies

$$\text {to the} \quad \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \$$

Since U κ † E ′′ F ′ = U κ E ′′ † ⊗U κ F ′ † , and ¯ S being invariant under local unitaries, it is sufficient that U S E ′ F → E ′′ F ′ = U N κ 1 / 2 E ′ F → E ′′ F ′ . Thus, apart from local unitaries, the optimal squashing channel is N κ 1 / 2 , from which the thesis follows.

## VII. CONCLUSIONS

We have proved the multimode conditional quantum Entropy Power Inequality for bosonic quantum systems (Theorem III.18), which determines the minimum von Neumann conditional entropy of the output of any linear mixing of bosonic modes among all the input states with given conditional entropies. Moreover, we have determined new lower bounds to the squashed entanglement of a large family of bosonic Gaussian states (Theorem IV.3), and we have applied such bounds to determine new lower bounds to the squashed entanglement of all the multimode extreme bosonic Gaussian channels (Section V), i.e. , the bosonic Gaussian channels that cannot be decomposed as a convex combination of quantum channels. Our lower bound is known to be optimal in the case of the extreme bosonic Gaussian attenuator and amplifier [42].

It is well known that proving the lower bounds to the squashed entanglement of a quantum state or a quantum channel is a challenging task since the optimizations in Equations (14) and (16) over all the possible extensions of the quantum state are almost never analytically treatable. We overcome this problem by employing the new multimode conditional quantum Entropy Power Inequality (84), which holds for any conditioning quantum system. We significantly extended the results of Ref. [42], where the squashed entanglement of the noiseless bosonic Gaussian attenuator and amplifier have been determined. In particular, we extend the set of states for which it is possible to provide a lower bound to the squashed entanglement to all those quantum states whose covariance matrix has at least half of the symplectic eigenvalues equal to 1 / 2 and we provide the first method for calculating a non-trivial lower bound to the squashed entanglement of any multimode extreme bosonic Gaussian channel.

Our results can have applications in quantum key distribution, establishing the first upper bounds to the distillable key of such a large family of bosonic Gaussian states and to the secret-key capacity and the two-way quantum capacity that is achievable over any multimode extreme bosonic Gaussian channel. Furthermore, having a proven lower bound for the squashed entanglement of a quantum channel helps in establishing an optimal upper bound. In fact, if during the optimisation process for the upper bound the lower bound is reached then the squashed entanglement is exactly determined. The upper bounds on the squashed entanglement of quantum channels establish corresponding upper bounds on both the secret-key capacity and the two-way quantum capacity. Conversely, the lower bounds on the squashed entanglement imply that the squashed entanglement cannot yield tighter upper bounds on the aforementioned capacities than those provided by the lower bounds.

## APPENDIX A MATHEMATICAL NOTES

This section is dedicated to showing and deriving some results used in the main text.

Lemma A.1 (covariance matrix of a product state) . The covariance matrix of a product state can be written in terms of the covariance matrices of the states of the individual subsystems as

$$\sigma ( \hat { \rho } _ { 1 } \otimes \hat { \rho } _ { 2 } ) = \sigma ( \hat { \rho } _ { 1 } ) \oplus \sigma ( \hat { \rho } _ { 2 } ) \, .$$

Lemma A.2 (covariance matrix of a two-mode squeezed vacuum state) . The covariance matrix of a two-mode squeezed vacuum state ∣ ϕ N ⟩ ⟨ ϕ N ∣ as a function of the average number of photons N per single mode is given by

$$\begin{array} { r l } & { \text {applied} } & { o f photons \ N \ p e r \ s i n g l e \ m o d e \ i s \ g i v e n \ b y } \\ & { \text {quasched} } & \\ & { \text {Gaussian} } & \\ & { \sigma ( | \phi _ { N } \rangle \phi _ { N } | ) = \left ( \begin{array} { c c } \left ( N + \frac { 1 } { 2 } \right ) I _ { 2 } & \sqrt { N ( N + 1 ) } \, Z _ { 2 } \\ \sqrt { N ( N + 1 ) } \, Z _ { 2 } & \left ( N + \frac { 1 } { 2 } \right ) I _ { 2 } \end{array} \right ) , \ ( 1 9 9 ) } \\ & { \text {quantum} } & \\ & { \text {the case} } & { w h e r e \ I _ { 2 } = d i a g ( 1 , 1 ) \ a n d \ Z _ { 2 } = d i a g ( 1 , - 1 ) \, . } \\ & { \text {fier} \ [ 4 2 ] . } & { P r o f . \ \text {Since } N \, \text { is the average number of photons per single} } \end{array}$$

Proof. Since N is the average number of photons per single mode, the two-mode squeezed vacuum state ∣ ϕ N ⟩ ⟨ ϕ N ∣ has average number of photons 2 N . Therefore, recalling Equation (30), it holds

$$2 N & = \frac { 1 } { 2 } \ t r \left [ \sigma \left ( | \phi _ { N } \rangle \langle \phi _ { N } | \right ) - \frac { I _ { 4 } } { 2 } \right ] , \\$$

where I 4 = diag ( 1 , 1 ) ⊕ 2 . Whence, from [44, Equation (5.21)], it holds

$$\cosh ( 2 r ) & = 2 N + 1 \, . & ( 2 0 1 ) \\ \intertext { n g h i s e x i p e r s i o n } \intertext { w i t h i s e x i p e r s i o n }$$

By substituting this expression into [44, Equation (5.21)] Equation (199) is obtained.

Lemma A.3 (covariance matrix of a 2 n -mode squeezed vacuum state) . The covariance matrix of a 2 n -mode squeezed vacuum state as a function of the average number of photons N i per single mode is given by

$$\text {at} \ a \quad N _ { i } \ p e r \, \text {single mode is given by} \\ \text {of any} & & \sigma ( | \phi _ { N } \rangle _ { A R } \langle \phi _ { N } | ) = \begin{pmatrix} \oplus _ { i = 1 } ^ { n } \left ( N _ { i } + \frac { 1 } { 2 } \right ) I _ { 2 } & \oplus _ { i = 1 } ^ { n } \sqrt { N _ { i } ( N _ { i } + 1 ) } Z _ { 2 } \\ \oplus _ { i = 1 } ^ { n } \sqrt { N _ { i } ( N _ { i } + 1 ) } Z _ { 2 } & \oplus _ { i = 1 } ^ { n } \left ( N _ { i } + \frac { 1 } { 2 } \right ) I _ { 2 } \\ \end{pmatrix} , \\ \text {distrib} & & \text {stillable} \\ \text {stillable} & & ( 2 0 2 )$$

where A and R are n -mode bosonic quantum systems.

Proof. Let us think of systems A and R as the union of n one-mode quantum systems { A i } i = 1 ,...,n and { R j } j = 1 ,...,n . The 2 n -mode squeezed vacuum state is defined as the tensor product of n two-mode squeezed vacuum state, as follows

$$| \phi _ { N } \rangle _ { A R } \langle \phi _ { N } | = \bigotimes _ { i = 1 } ^ { n } | \phi _ { N _ { i } } \rangle _ { A _ { i } R _ { i } } \langle \phi _ { N _ { i } } | \ , \\ \text {covariance matrix}$$

with covariance matrix

$$\text {quantum} \quad \text {with covariance matrix} \\ \text {both the} \\ \text {city. Con-} \quad \sigma ( | \phi _ { N } \rangle _ { A R } \langle \phi _ { N } | ) = \bigoplus _ { i = 1 } ^ { n } \left ( \begin{matrix} \left ( N _ { i } + \frac { 1 } { 2 } \right ) I _ { 2 } & \sqrt { N _ { i } ( N _ { i } + 1 ) } \, Z _ { 2 } \\ \sqrt { N _ { i } ( N _ { i } + 1 ) } \, Z _ { 2 } & \left ( N _ { i } + \frac { 1 } { 2 } \right ) I _ { 2 } \end{matrix} \right ) . \\ \text {upper} \\ \text {provided} \quad \text {Matrix (204) is a block diagonal matrix which is related to}$$

Matrix (204) is a block diagonal matrix which is related to systems, in order, A 1 , R 1 , . . . , A n , R n . Since we are interested in the ordering AR = A 1 ⋯ A n R 1 ⋯ R n , we can rearrange the rows and columns of matrix (204) to obtain Equation (202).

## A. Covariance matrix of the output of a Gaussian attenuator

Let us consider the quantum state

$$\text {Let} \ \text {is consider the quantum state} \\ \text {a.t.} \ \ \hat { \omega } _ { A R } ( \eta ) \\ \text {a.t.terms} \\ = ( \mathbb { 1 } _ { A } \otimes \mathcal { E } _ { \eta } ) ( | \phi _ { N } \rangle _ { A R } \langle \phi _ { N } | ) \\ = \text {tr} _ { B } \left [ ( 1 _ { A } \otimes \hat { U } _ { R B } ^ { \eta } ) \left ( | \phi _ { N } \rangle _ { A R } \langle \phi _ { N } | \otimes | 0 \rangle _ { B } \langle 0 | \right ) \left ( \mathbb { 1 } _ { A } \otimes \hat { U } _ { R B } ^ { \eta \dagger } \right ) \right ] . \\$$

The covariance matrix σ ( ˆ ω AR ( η )) is derived by only taking the rows and columns relative to the systems A and R of the following covariance matrix:

$$& \quad \sigma ( \hat { \omega } _ { A R B } ( \eta ) ) \\ & \quad = \sigma \left ( ( \hat { \mathbf l } _ { A } \otimes \hat { U } _ { R B } ^ { \eta } ) \left ( | \phi _ { N } \rangle _ { A R } \langle \phi _ { N } | \otimes | 0 \rangle _ { B } \langle 0 | \right ) \left ( \hat { \mathbf l } _ { A } \otimes \hat { U } _ { R B } ^ { \eta } \right ) \right ) \\ & \quad = \left ( I _ { 2 n } \oplus S _ { \eta } \right ) \left ( \sigma ( | \phi _ { N } \rangle _ { A R } \langle \phi _ { N } | ) \oplus \sigma ( | 0 \rangle _ { B } \langle 0 | ) \right ) \left ( I _ { 2 n } \oplus S _ { \eta } \right ) ^ { T } . \\ & \quad \text {and recalc} \quad \\ & \quad \text {if we now only fit this approximation in terms of matrices of matrices, and for} \quad \text {ated with}$$

If we now explicit this expression in terms of matrices, and, for convenience, we reorder the systems as A 1 R 1 B 1 ⋯ A n R n B n we have

$$I _ { 2 n } \oplus S _ { \eta } & = \bigoplus _ { i = 1 } ^ { n } \begin{pmatrix} I _ { 2 } & 0 & 0 \\ 0 & \sqrt { \eta _ { i } } \, I _ { 2 } & \sqrt { 1 - \eta _ { i } } \, I _ { 2 } \\ 0 & - \sqrt { 1 - \eta _ { i } } \, I _ { 2 } & \sqrt { \eta _ { i } } \, I _ { 2 } \end{pmatrix} , \\ \intertext { a n d }$$

and

$$\sigma ( | \phi _ { N } \rangle _ { A R } \langle \phi _ { N } | ) & \oplus \sigma ( | 0 \rangle _ { B } \langle 0 | ) \\ & = \bigoplus _ { i = 1 } ^ { n } \left ( \sqrt { N _ { i } ( N _ { i } + 1 ) } \, I _ { 2 } \quad \sqrt { N _ { i } ( N _ { i } + 1 ) } \, Z _ { 2 } \quad 0 \\ \text {whence} & \quad 0 \quad 0 \quad \frac { I _ { 2 } } { 2 } \right ) .$$

whence

$$\text {whence} & & C . \ C o v a c { C } \\ & & \quad \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \$$

from which, considering only the rows and columns relative to the systems A and R , matrix σ ( ˆ ω AR ( η )) in Equation (126) is obtained.

## B. Covariance matrix of the output of a generic symplectic transformation

In this section, we derive Equations (134a) and (134b). The covariance matrices of the marginal states ˆ ρ CR ( η ) and ˆ ρ DR ( η ) are derived from σ ( ˆ ρ CDR ( η )) . This covariance matrix is given by

$$\sigma ( \hat { \rho } _ { C R D } ( \eta ) ) & & \sigma ( \hat { \rho } _ { C D } ^ { S } ) & & \sigma ( \hat { \gamma } _ { C D } ^ { S } ) & = \sigma \left ( ( \hat { U } _ { A B } ^ { S } \otimes \hat { I } _ { R } ) \left ( \hat { \omega } _ { A R } ( \eta ) \otimes | 0 \rangle _ { B } \langle 0 | \right ) \left ( \hat { U } _ { A B } ^ { S \dagger } \otimes \hat { I } _ { R } \right ) \right ) & = \sigma \left ( \left ( ( \hat { U } _ { A B } ^ { S } ) ^ { T } \right ) ^ { T } , & & = \sigma \left ( \left ( ( \hat { I } _ { A B } ^ { S } \otimes I _ { R } ) ^ { T } \right ) ^ { T } , & & = \left ( I _ { A } ^ { S } \right ) ^ { T }$$

where ˆ U S AB is an isometric transformation acting on the quadratures via a symplectic matrix of the form (98). Now, defining the variables

$$A _ { N } & \coloneqq \bigoplus _ { i = 1 } ^ { n } \left ( N _ { i } + \frac { 1 } { 2 } \right ) I _ { 2 } \, , \\ B _ { N } & \coloneqq \bigoplus _ { i = 1 } ^ { n } \sqrt { \eta _ { i } \, N _ { i } ( N _ { i } + 1 ) } \, Z _ { 2 } \, , \\ C _ { N } & \coloneqq \bigoplus _ { i = 1 } ^ { n } \left ( \eta _ { i } \, N _ { i } + \frac { 1 } { 2 } \right ) I _ { 2 } \, , \\ \text {calling that the rows and columns are in order, associ-}$$

and recalling that the rows and columns are, in order, associated with the systems A , R and B , the matrix form of Equation (210) is

$$& _ { n } R _ { n } B _ { n } \quad ( 2 1 0 ) \text { is } \\ & \quad \sigma ( \hat { \rho } _ { C R D } ( \eta ) ) \\ & \quad = \begin{pmatrix} B _ { 1 } ^ { C } & 0 & B _ { 2 } ^ { C } \\ 0 & I _ { 2 n } & 0 \\ B _ { 1 } ^ { D } & 0 & B _ { 2 } ^ { D } \end{pmatrix} \begin{pmatrix} A _ { N } & B _ { N } & 0 \\ B _ { 1 } & 0 & B _ { 1 } ^ { D } \\ 0 & I _ { 2 n } & 0 \\ B _ { 2 } ^ { C } T & 0 & B _ { 2 } ^ { D } T \end{pmatrix} \\ & = \begin{pmatrix} A _ { N } B _ { 1 } ^ { C } B _ { 1 } ^ { T } + \frac { 1 } { 2 } B _ { 2 } ^ { C } B _ { 2 } ^ { T } & B _ { 1 } ^ { C } B _ { N } & A _ { N } B _ { 1 } ^ { C } B _ { 1 } ^ { D } + \frac { 1 } { 2 } B _ { 2 } ^ { C } B _ { 2 } ^ { D } \\ B _ { 1 } B _ { 1 } ^ { C } & C & B _ { N } B _ { 1 } ^ { D } \end{pmatrix} . \\ & = \begin{pmatrix} A _ { N } B _ { 1 } ^ { D } B _ { 1 } ^ { C } + \frac { 1 } { 2 } B _ { 2 } ^ { D } B _ { 2 } ^ { C } & B _ { 1 } ^ { D } B _ { N } & A _ { N } B _ { 1 } ^ { D } B _ { 1 } ^ { D } + \frac { 1 } { 2 } B _ { 2 } ^ { D } B _ { 2 } ^ { D } \end{pmatrix} . \\ & = \begin{pmatrix} 2 1 2 \\ 2 1 2 \end{pmatrix} \\$$

## C. Covariance matrix of the output of a two-mode Gaussian attenuator

In this section, we calculate the covariance matrix σ CD of Section C-B. Given 3 two-mode squeezed vacuum states ϕ N 1 A 1 B 1 , ϕ N 2 A 2 B 2 , ϕ N 3 E with average number of photons N 1 , N 2 and N 3 respectively, let us calculate the covariance matrix of the state

$$\text {relative} \quad & \text {the state} \\ \text {on } ( 1 2 6 ) \quad & \hat { \gamma } _ { C D } ^ { S } \\ & = ( \mathbb { 1 } _ { A } \otimes \mathcal { N } _ { B } ) \left ( \hat { \phi } ^ { N _ { 1 } } \otimes \hat { \phi } ^ { N _ { 2 } } \right ) _ { A B } \\ & = \text {tr} _ { E } \left [ \left ( \hat { \mathbb { 1 } } _ { A } \otimes \hat { U } _ { B E } ^ { S } \right ) \left ( \hat { \phi } ^ { N _ { 1 } } \otimes \hat { \phi } ^ { N _ { 2 } } \right ) _ { A B } \otimes \hat { \phi } _ { E } ^ { N _ { 3 } } \right ) \left ( \hat { \mathbb { 1 } } _ { A } \otimes \hat { U } _ { B E } ^ { S } \right ) \right ] , \\ & ( 1 3 4 b ) . \\ \eta ( \text { and } \quad & \text {where} \ \hat { U } _ { B E } ^ { S } \text { is an isometric transformation } \text { acting on the
}$$

$$& \quad \text {the covariance matrix } \sigma ( \hat { \gamma } _ { C D E } ^ { S } ) . \\ & \quad \sigma ( \hat { \gamma } _ { C D E } ^ { S } ) \\ & \quad = \sigma \left ( \left ( \hat { \mathbb { I } } _ { A } \otimes \hat { U } _ { B E } ^ { S } \right ) \left ( \left ( \hat { \phi } ^ { N _ { 1 } } \otimes \hat { \phi } ^ { N _ { 2 } } \right ) _ { A B } \otimes \hat { \phi } _ { E } ^ { N _ { 3 } } \right ) \left ( \hat { \mathbb { I } } _ { A } \otimes \hat { U } _ { B E } ^ { S } \right ) \right ) \\ & \quad = \left ( I _ { A } \oplus S _ { B E } \right ) \left ( \sigma ( \left ( \hat { \phi } ^ { N _ { 1 } } \otimes \hat { \phi } ^ { N _ { 2 } } \right ) _ { A B } ) \oplus \sigma ( \hat { \phi } _ { E } ^ { N _ { 3 } } ) \right ) \left ( I _ { A } \oplus S _ { B E } \right ) ^ { T } . \\ & \quad . \text { Now,} \\ & \quad \text {In a more explicit form, it holds}$$

where ˆ U S BE is an isometric transformation acting on the quadratures of the systems B and E via a 8 × 8 symplectic matrix which can be seen in the form (98). Let us calculate the covariance matrix σ ( ˆ γ S CDE ) :

In a more explicit form, it holds

$$\begin{array} { c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c$$

where σ E is defined in Equation (295). Let us now consider the special case in which the symplectic matrix is given by Equation (287). In this case, the following relations apply:

$$I \left ( 2 6 / 7 \right ) & \colon \text {in this case, the following relations apply.} \\ B _ { 1 } ^ { C } & = B _ { 2 } ^ { D } = \bigoplus _ { i = 1 } ^ { 2 } \sqrt { \eta _ { i } } \, I _ { 2 } \, , \\ B _ { 2 } ^ { C } & = - B _ { 1 } ^ { D } = \bigoplus _ { i = 1 } ^ { 2 } \sqrt { 1 - \eta _ { i } } \, I _ { 2 } \, . \\$$

By replacing these matrix blocks in Equation (215) and considering only the first eight rows and columns, those related to the spaces C and D , the explicit form for the matrix σ ( ˆ γ S CD ) is obtained:

$$i = 1 & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & &$$

## D. Maximisation of the multimode linear conditional quantum EPI

The aim of this section is to maximise the RHS of Equation (94) with respect to λ i , i = 1 , . . . , K and subject to the constraint ∑ K i = 1 λ i = 1 . It is natural to treat this problem using the method of Lagrange multipliers. In particular, let us the objective and constraint function as

$$f ( \lambda ) = & \sum _ { i = 1 } ^ { K } \lambda _ { i } \frac { x _ { i } } { n } + \sum _ { i = 1 } ^ { K } \lambda _ { i } \ln \left ( \frac { b _ { i } } { \lambda _ { i } } \right ) , \\ g ( \lambda ) = & \sum _ { i = 1 } ^ { K } \lambda _ { i } - 1 \, , \\ x _ { i } \coloneqq & S ( X _ { i } | M ) \hat { \varrho } _ { X _ { i } M } \text { and } \lambda = ( \lambda _ { 1 } \dots \lambda _ { K } ) . \text { We can now } \quad \text {thery}$$

where x i ∶= S ( X i ∣ M ) ˆ ρ Xi M and λ = ( λ 1 . . . λ K ) . We can now build the Lagrangian function

$$\Lambda ( \lambda , \delta ) = f ( \lambda ) + \delta g ( \lambda ) & & ( 2 1 9 ) & \text {where} \\$$

and impose the system

$$\text {and impose the system} \\ \left \{ \frac { \partial } { \partial \lambda _ { i } } \Lambda ( \lambda , \delta ) = 0 \quad & \implies \begin{cases} \lambda _ { j } = \frac { b _ { j } \exp \left ( \frac { x _ { j } } { n } \right ) } { e ^ { 1 - \delta } } & ( 2 2 0 ) \\ \frac { K } { \partial \delta } \Lambda ( \lambda , \delta ) = 0 & \text {exponent} \end{cases} \quad \text {Explicit} \\ \text {where it is implicitly understood that the first equation in the} \\ & \quad \text {is implicitly understood that the first equation in the} \\$$

$$\lambda _ { j } = \frac { b _ { j } \exp \left ( \frac { x _ { j } } { n } \right ) } { \sum _ { i } ^ { K } b _ { i } \exp \left ( \frac { x _ { i } } { n } \right ) } \, , \quad ( 2 2 1 ) \\ \text {tally} \, \text {Equation (95)} \, , \, \text {Moreover, since } \, f \text { is a concave}$$

where it is implicitly understood that the first equation in the system (220) is valid ∀ i . By substituting the first K equations of the system (220) into the last equation, we obtain that e 1 -δ = ∑ K i b i exp ( x i n ) and thus, ∀ j , it holds

which is exactly Equation (95). Moreover, since f is a concave function in λ with a unique stationary point, that point is necessarily the global maximum.

## APPENDIX B

## AUXILIARY LEMMAS

In this appendix, we provide the statements and the proofs of some lemmas and results used in the main text.

A. Some linear algebra lemmas

Lemma B.1. Given a symplectic matrix S ∈ Sp ( 2 n, R ) that we can write in a block form as

$$S = \begin{pmatrix} A & B \\ C & D \end{pmatrix} , \quad ( 2 2 2 )$$

then the following relationship for the blocks applies

$$a \, c & = b \, d \, , \\ \\ \intertext { a c = b \, d \, , } \intertext { a \, c = b \, d \, , }$$

where a = ∣ det A ∣ , b = ∣ det B ∣ , c = ∣ det C ∣ and d = ∣ det D ∣ .

Proof. By definition of symplectic matrix, the following relation holds

$$S \, \Delta \, S ^ { T } = \Delta \, ,$$

where

$$S & = \begin{pmatrix} A & B \\ C & D \end{pmatrix} , \\ \Delta & = \begin{pmatrix} \Delta _ { 2 n } & 0 \\ 0 & \Delta _ { 2 n } \end{pmatrix} , \quad \Delta _ { 2 n } = \bigoplus _ { i = 1 } ^ { n } \begin{pmatrix} 0 & 1 \\ - 1 & 0 \end{pmatrix} . \\ \text {Explicitly,} \, \text {Equation (224) can be written as}$$

Explicitly, Equation (224) can be written as

$$\begin{array} { r l } & { n \text { in the } } & { \begin{pmatrix} A \Delta _ { 2 n } A ^ { T } + B \Delta _ { 2 n } B ^ { T } & A \Delta _ { 2 n } C ^ { T } + B \Delta _ { 2 n } D ^ { T } \\ C \Delta _ { 2 n } A ^ { T } + D \Delta _ { 2 n } B ^ { T } & C \Delta _ { 2 n } C ^ { T } + D \Delta _ { 2 n } D ^ { T } \end{pmatrix} = \begin{pmatrix} \Delta _ { 2 n } & 0 \\ 0 & \Delta _ { 2 n } \end{pmatrix} . } \\ & { t \, e ^ { 1 - \delta } = } & { \quad } \\ & { \quad } & { \quad } \, \text {in the quotient } \, \log \, t \, \text { the } \, b \, \log 1 \, \text { in the } \, \log \, t \, \text { right } \, \arg \, n \, \text { this } } \end{array}$$

In particular, looking at the block in the top right corner, this implies that

$$A \, \Delta _ { 2 n } \, C ^ { T } = - B \, \Delta _ { 2 n } \, D ^ { T } \, , \\$$

from which, it holds

$$\det ( A ) \det ( C ) & = - \det ( B ) \det ( D ) \, , & ( 2 2 8 ) \\$$

from which Equation (223) directly follows.

Theorem B.2 (Williamson) . Given h ∈ R 2 n × 2 n &gt; 0 symmetric, there exists a symplectic matrix S such that

$$S h S ^ { T } = \bigoplus _ { k = 1 } ^ { n } \nu _ { k } I _ { 2 } = \colon D \, , \quad ( 2 2 9 )$$

where D is a diagonal matrix with pairwise equal eigenvalues. The { ν k } k = 1 ,...,n are the symplectic eigenvalues of the matrix h .

$$P r o o f . \, S e e \, [ 4 4 ] .$$

Lemma B.3. Let A and B be two 2 n × 2 n real positive definite matrices such that A &gt; B . Suppose that A and B have symplectic eigenvalues d 1 ( A ) ≤ ⋯ ≤ d n ( A ) , d 1 ( B ) ≤ ⋯≤ d n ( B ) . Then for all i = 1 , . . . , n ,

$$d _ { i } ( A ) \geq d _ { i } ( B ) \, . & & ( 2 3 0 ) & \stackrel { \rho \text {Pos} } { \ f u l f i } \\ d _ { i } ( A ) \geq d _ { i } ( B ) \, . & & ( 2 3 0 ) & \stackrel { \ f u l f i } { \ f u l f i } \\ d _ { i } ( B ) \geq d _ { i } ( A ) \, . & & ( 2 3 0 ) & \stackrel { \ f u l f i } { \ f u l f i } \\$$

This means that the ordered symplectic eigenvalues of matrix A are one-to-one greater than the ordered symplectic eigenvalues of matrix B .

Proof. This is a direct consequence of [52, Corollary 2]. In particular, if A &gt; B then A = B + δ , where δ is a positive definite real matrix. Fixing k = 1 , Corollary 2 of [52] states that for every 1 ≤ i j ≤ n , with 1 ≤ j ≤ n , it holds

$$d _ { i _ { j } } ( A ) = d _ { i _ { j } } ( B + \delta ) \geq d _ { i _ { j } } ( B ) + d _ { j } ( \delta ) \geq d _ { i _ { j } } ( B ) \, . \quad ( 2 3 1 ) \quad A \, \text { comp} \\ \Gamma _ { \ } e x { v e r } \colon ( 2 2 1 ) \, \dot { i } _ { \ } e x { v e r } \, \Gamma _ { \ } e x { v e r } \, \Gamma _ { \ } e x { v e r } \, 1 \quad \text {the the these}$$

From Equation (231) it therefore follows that for every 1 ≤ j ≤ n it holds d i ( A ) ≥ d i ( B ) , whence the thesis.

Lemma B.3 thus states that given two matrices A and B such that A &gt; B the ordered symplectic eigenvalues of matrix A are one-to-one greater than the ordered symplectic eigenvalues of matrix B .

Proposition B.4. Let U be a 2 n × 2 n positive definite real matrix, V a 2 n × 2 n constant symmetric real matrix, t a real variable and g ( x ) ∶= ( x + 1 ) ln ( x + 1 ) -x ln ( x ) . Let W = t U + V and let { ν i W } i = 1 ,...,n and { ν i U } i = 1 ,...,n be the ordered symplectic eigenvalues of W and U respectively. In the limit of t going to infinity for every i = 1 , . . . , n holds g ( ν i W -1 2 ) ∼ g ( t ν i U -1 2 ) , i.e. ,

$$\lim _ { t \to \infty } \frac { g ( \nu _ { W } ^ { i } - \frac { 1 } { 2 } ) } { g ( \nu _ { t U } ^ { i } - \frac { 1 } { 2 } ) } = 1 . \quad ( 2 3 2 ) \quad \text {of the} \, \exp ( 2 3 2 ) \\ \text {exists a constant } r > 0 \, \text {such that } - r I < V < r I U \quad \text {unc}$$

Proof. There exists a constant r &gt; 0 such that -r U ≤ V ≤ r U , and a possible choice is r = ∥ U -1 / 2 V U -1 / 2 ∥ ∞ , where ∥⋅∥ ∞ denotes the infinity norm 5 . This means that ( t -r ) U ≤ t U + V ≤ ( t + r ) U . It also holds that the symplectic eigenvalues respect the inequalities between matrices, i.e. , that the ordered symplectic eigenvalues of t U + V lie between the ordered symplectic eigenvalues of ( t -r ) U and ( t + r ) U (see Lemma B.3). This means that for every i = 1 , . . . , n it holds:

$$\nu _ { ( t - r ) \, U } ^ { i } \leq \nu _ { W } ^ { i } \leq \nu _ { ( t + r ) \, U } ^ { i } \cdot \quad ( 2 3 3 ) \quad \text {we know} \\ \text {we know} \quad ( 2 3 3 ) \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \Delta = 0 \, \$$

Moreover, since the function g is monotonically increasing in its argument, i.e. , for every x, y such that x &gt; y &gt; 0 g ( x ) &gt; g ( y ) holds, for every i = 1 , . . . , n it holds:

$$g \left ( \nu _ { ( t - r ) \, U } ^ { i } - \frac { 1 } { 2 } \right ) \leq g \left ( \nu _ { W } ^ { i } - \frac { 1 } { 2 } \right ) \leq g \left ( \nu _ { ( t + r ) \, U } ^ { i } - \frac { 1 } { 2 } \right ) . \quad ( 2 3 4 ) \quad \text {Thus thus} \\$$

5 Multiplying the inequalities -r U ≤ V ≤ r U by U -1 / 2 will result in -r I ≤ U -1 / 2 V U -1 / 2 ≤ r I which basically means that ∥ U -1 / 2 V U -1 / 2 ∥ ∞ ≤ r , so r exists if U is invertible.

Simple calculations show that, for t ≫ 1 , the following applies

and

$$\begin{array} { c c } \overset { v e } { B } & g \left ( \nu _ { ( t \pm r ) U } ^ { i } - \frac { 1 } { 2 } \right ) = \ln \left ( t \, \nu _ { U } ^ { i } \right ) + 1 \pm \frac { r } { t } + \mathcal { O } \left ( t ^ { - 2 } \right ) , \\ \leq & \end{array} \quad ( 2 3 6 )$$

where we used the fact that, for every real constant c and every positive definite matrix A , every symplectic eigenvalue of A fulfils the condition ν cA = c ν A . From Equations (234) and (236) it follows that

$$\begin{array} { r l } { c e i g e n { - } } & { \ln ( t \nu _ { U } ^ { i } ) + 1 - \frac { r } { t } + \mathcal { O } ( t ^ { - 2 } ) \leq g \left ( \nu _ { W } ^ { i } - \frac { 1 } { 2 } \right ) \leq \ln ( t \nu _ { U } ^ { i } ) + 1 + \frac { r } { t } + \mathcal { O } ( t ^ { - 2 } ) \, . } \\ { r y \, 2 ] . \, I n } & { \ln ( t \nu _ { U } - i g \cdot t ) + 1 - \frac { r } { t } + \mathcal { O } ( t ^ { - 2 } ) \, . } \end{array}$$

In the limit of t tending to infinity, it holds

$$\text {rates} \quad g \left ( \nu _ { W } ^ { i } - \frac { 1 } { 2 } \right ) \sim \ln \left ( t \nu _ { U } ^ { i } \right ) + 1 \, , \quad \text {for} \quad t \to \infty \, .$$

A comparison of Equation (238) with Equation (235) yields the thesis, i.e. ,

$$\Box \quad g \left ( \nu _ { W } ^ { i } - \frac { 1 } { 2 } \right ) \sim g \left ( \nu _ { t U } ^ { i } - \frac { 1 } { 2 } \right ) , \quad \text {for} \quad t \to \infty \, .$$

Lemma B.5. The symplectic eigenvalues of the covariance matrix of any pure bosonic Gaussian state are all equal to 1 / 2 .

Proof. It is well known that any pure bosonic Gaussian state can be written in the form ˆ ω = ˆ D r ˆ U S ∣ 0 ⟩ ⟨ 0 ∣ ˆ U † S ˆ D † r , for appropriate symplectic unitaries ˆ U S and translation operators ˆ D r . Since the covariance matrix of a quantum state is invariant under translation operators, and since the symplectic eigenvalues are invariant under symplectic transformations, every pure bosonic Gaussian state has the same symplectic eigenvalues of the vacuum state, i.e. , all equal to 1 / 2 . See also [44].

Lemma B.6. A positive-definite real matrix σ satisfies the uncertainty principle σ ≥ ± i 2 ∆ if and only if all its symplectic eigenvalues ν k are greater than or equal to 1 / 2 .

$$\sum _ { e s } \ P r o o f . \ S e e \ [ 4 4 , \, \text {Section 3.4} ] .$$

Lemma B.7. Let's consider a matrix σ ∈ R 2 n × 2 n &gt; 0 satisfying σ ≥ ± i 2 ∆ and with symplectic eigenvalues { ν k } k = 1 ,...,n . The rank of σ ± i 2 ∆ is equal to n plus the number of ν k &gt; 1 / 2 .

Proof. Since rank is an invariant under matrix equivalence, we have that rank ( σ ± i 2 ∆ ) = rank ( SσS T ± i 2 ∆ ) , where S is the symplectic matrix provided by Williamson's theorem that brings the matrix σ into its normal form. Being SσS T ± i 2 ∆ a Hermitian matrix, and therefore a diagonalizable matrix, its rank is equal to the number of its non-zero eigenvalues. Thus the rank of the matrix σ ± i 2 ∆ is equal to the non-zero eigenvalues of the matrix

$$\bigoplus _ { k = 1 } ^ { n } \begin{pmatrix} \nu _ { k } & \pm i / 2 \\ \mp i / 2 & \nu _ { k } \end{pmatrix} ,$$

$$g \left ( \nu _ { t U } ^ { i } - \frac { 1 } { 2 } \right ) = \ln \left ( t \nu _ { U } ^ { i } \right ) + 1 + \mathcal { O } \left ( \frac { 1 } { t ^ { 2 } } \right ) \quad ( 2 3 5 )$$

which are { ν k ± 1 2 } k = 1 ,...,n . Lemma B.5 ensures that ν k ≥ 1 / 2 ∀ k , then it holds

$$r a n k ( \sigma \pm \frac { i } { 2 } \Delta ) & = r a n k ( S \sigma S ^ { T } \pm \frac { i } { 2 } \Delta ) \\ & = \# \{ \nu _ { k } \colon \nu _ { k } + \frac { 1 } { 2 } \neq 0 \} _ { k } + \# \{ \nu _ { k } \colon \nu _ { k } - \frac { 1 } { 2 } \neq 0 \} _ { k } \\ & = n + \# \{ \nu _ { k } \colon \nu _ { k } > \frac { 1 } { 2 } \} _ { k } ,$$

with k = 1 , . . . , n

$$- =$$

Lemma B.8. For any symmetric matrix M of the form

$$M = \begin{pmatrix} A & B \\ B ^ { T } & C \end{pmatrix} \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \qu$$

if C is invertible then the following property hold: M &gt; 0 iff C &gt; 0 and A -BC -1 B T &gt; 0 .

$$P r o o f \ S e e \, [ 5 3 , \, \text {Proposition } 2 . 1 ] .$$

Lemma B.9 (Guttman rank additivity formula) . Let

$$M = \left ( \begin{array} { c c } A & B \\ C & D \end{array} \right ) \quad ( 2 4 3 ) \quad \text {The} \quad \begin{array} { c c } \text {eigen} & \\ \text {The} & \text {d} \end{array} \quad \text {the}$$

be a square matrix such that D is invertible and rank M = rank D . Then,

$$A = B \, D ^ { - 1 } \, C \, . \\$$

Proof. See [54].

Lemma B.10 (canonical decomposition) . Given an antisymmetric matrix ∆ ′ ∈ R 2 n × 2 n , there exists an orthogonal matrix O ′ ∈ R ( 2 n ) and a set of values d k ∈ R such that

$$O ^ { \prime } \Delta ^ { \prime } O ^ { \prime T } = \bigoplus _ { k = 1 } ^ { n } d _ { k } ^ { - 1 } \Delta _ { 2 } \, , \quad w i t h \quad \Delta _ { 2 } = \begin{pmatrix} 0 & 1 \\ - 1 & 0 \end{pmatrix} \, . \quad ( 2 4 5 ) \quad \begin{array} { c c c } \ r e a l { \ m a t h s c r { m a t h s c r { O } } } \\ u _ { 1 } + i v \\ s p o n d i n \end{array} .$$

Proof.

$$o f . \ S e e \ [ 4 4 , \, \text {Section 3.2.3} ] .$$

Lemma B.11. The symplectic matrix S of Theorem B.2 is unique up to left multiplication by a block diagonal orthogonal symplectic matrix where each block acts on an eigenspace of the matrix D , i.e. , S → OS with O = ⊕ k ≤ n j = 1 O j .

Proof. Let h ∈ R 2 n × 2 n &gt; 0 and let S and S ′ be two symplectic matrices such that D = S hS T = S ′ hS ′ T , where the matrix D is defined as D ∶= diag ( ν 1 I 2 , . . . , ν n I 2 ) . It is easy to verify that

$$D = X \, D \, X ^ { T } , & & ( 2 4 6 ) \\$$

where we defined the symplectic matrix X ∶= S ′ S -1 . Since D is invertible, the equation above is equivalent to

$$\left ( D ^ { - 1 / 2 } \ X \ D ^ { 1 / 2 } \right ) \left ( D ^ { - 1 / 2 } \ X \ D ^ { 1 / 2 } \right ) ^ { T } = I _ { 2 n } \, , \quad ( 2 4 7 ) \ \ \ _ { t h e n } ^ { B . 1 2 \ a n } \\$$

O ∶= D -1 / 2 XD 1 / 2 is thus an orthogonal matrix and X can be written as

$$X = D ^ { 1 / 2 } \, O \, D ^ { - 1 / 2 } \, . & & ( 2 4 8 ) & \, \Pr o { 0 } { 2 } \\ & & & & \, \Pr { R e m }$$

Substituting this expression into the condition for X to be symplectic, i.e. , X ∆ X T = ∆ , we have

$$D ^ { - 1 / 2 } \, \Delta \, D ^ { - 1 / 2 } = O \, D ^ { - 1 / 2 } \, \Delta \, D ^ { - 1 / 2 } \, O ^ { T } \, , \quad ( 2 4 9 ) \ \begin{pmatrix} 1 & 1 & 1 \\ 1 & - 1 & 1 \end{pmatrix}$$

from which it holds

$$from \text { which it holds} \\ D ^ { - 1 / 2 } \, \Delta \, D ^ { - 1 / 2 } = \bigoplus _ { j = 1 } ^ { n } \frac { 1 } { \nu _ { j } } \Delta _ { 2 } \\ = \left ( \bigoplus _ { i = 1 } ^ { n } u \right ) \left ( \bigoplus _ { i = 1 } ^ { n } - d \right ) \left ( \bigoplus _ { i = 1 } ^ { n } u \right ) ^ { \dagger } \\ = \colon U \, \tilde { D } \, U ^ { \dagger } , \\ \text { where we used that being $\Delta_{2}:= \left( \begin{array} { c c } 0 & 1 \\ - \infty & 0 \end{array} \right)$ an antisymmetric}$$

where we used that being ∆ 2 ∶= ( 0 1 -1 0 ) an antisymmetric matrix, and therefore normal, by the spectral theorem is diagonalisable by a unitary matrix u and, defined U ∶= (⊕ n i = 1 u ) and ˜ D ∶= (⊕ n i = 1 1 ν j d ) 6 , Equation (249) then becomes

$$\text {if} \quad D ^ { - 1 / 2 } \, \Delta \, D ^ { - 1 / 2 } = U \, \tilde { D } \, U ^ { \dagger } = ( O U ) \, \tilde { D } \, ( O U ) ^ { \dagger } \, . \\ \text {This, using all the $u$-th $u$-vector} \, .$$

This equation tells us that we have two spectral decompositions of matrix D -1 / 2 ∆ D -1 / 2 . The eigenvectors associated with distinct eigenvalues are orthogonal to each other and two orthogonal sets of eigenvectors associated with the same eigenvalue are mapped into each other via a unitary matrix. Then there exists a block diagonal matrix V = ⊕ k ≤ n j = 1 V j , where the blocks V j are unitary matrices of the same size as the blocks of ˜ D proportional to the identity, such that OU = V U . This implies that V = O and thus, from Equation (248),

$$X = O = \oplus _ { j = 1 } ^ { k \leq n } V _ { j } \, ,$$

implying

$$S ^ { \prime } = O \, S \, . \\$$

Lemma B.12. Given a 2 n × 2 n anti-symmetric non-singular real matrix B and let ± b 1 i, . . . , ± b n i be its eigenvalues and u 1 + i v 1 , . . . , u n + i v n the n orthogonal eigenvectors corresponding to the eigenvalues b 1 i, . . . , b n i . Then the orthogonal matrix

$$O = \left ( \ \frac { u _ { 1 } } { \| u _ { 1 } \| } \, \left | \ \frac { v _ { 1 } } { \| v _ { 1 } \| } \, \right | \, \cdots \, \right | \ \frac { u _ { n } } { \| u _ { n } \| } \, \left | \ \frac { v _ { n } } { \| v _ { n } \| } \, \right ) \\ f \quad i s \, s u c h \ t h a t \quad$$

$$O ^ { T } \, B \, O = \bigoplus _ { j = 1 } ^ { n } \begin{pmatrix} 0 & b _ { j } \\ - b _ { j } & 0 \end{pmatrix} . \quad \quad ( 2 5 5 ) \\ [ 5 5 ] [ 5 7 ]$$

is such that

Proof. See [55]-[57].

Remark B.13 . It is easy to see that for each non-singular matrix A with det A = b -1 it is true that

Lemma B.14. Let the matrices B , O and A i be as in Lemma B.12 and Remark B.13, defining A = ⊕ n i = 1 A i and M = OA , then

$$A ^ { T } \begin{pmatrix} 0 & b \\ - b & 0 \end{pmatrix} A = \begin{pmatrix} 0 & 1 \\ - 1 & 0 \end{pmatrix} . \\ \intertext { B 1 4 } \intertext { L e t h e m a t r i c e B R A n d A \colon b e a s i n L e m m a }$$

$$M ^ { T } \, B \, M & = \bigoplus _ { j = 1 } ^ { n } \binom { 0 } { - 1 } \, . \\ \intertext { i s i a d e c t a n d s e c h a r r e c c e }$$

Proof. This is a direct consequence of Lemma B.12 and Remark B.13.

$$X & \text { to be } & ^ { 6 } \text {Explicitly: } d = \frac { i } { 2 } \, Z _ { 2 } \text { and } u = S ^ { \dagger } H , \text { where } S = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix} \text { and } H = \\ & ( 2 4 9 ) & \begin{pmatrix} 1 & 1 \\ 1 & - 1 \end{pmatrix} .$$

## B. Entropic functionals in quantum communication

In this subsection we show some fundamental entropic inequalities. In the following, for the sake of simplicity, the Von Neumann entropy of a state ˆ ρ A will be denoted as S ( A ) ∶= S ( ˆ ρ A ) . By analogy with the classical case, we state the following definitions [58].

Definition B.15 (quantum conditional entropy) . The quantum conditional entropy is defined as:

$$S ( A | B ) = S ( A B ) - S ( B ) \, .$$

Definition B.16 (quantum mutual information) . The quantum mutual information is defined as:

$$I ( A \colon B ) = S ( A ) + S ( B ) - S ( A B ) \, , \\$$

which is a non-negative quantity.

Exploiting the strong subadditivity for the Von Neumann entropy, it is possible to prove the following proposition [59, Chapter 4].

## Proposition B.17. The following relationships hold.

- i. Conditioning always decreases entropy,

$$S ( A | B C ) \leq S ( A | C ) , S ( A | B ) \, .$$

- ii. Discarding systems always decreases the quantum mutual information,

$$I ( A \colon B C ) \geq I ( A \colon B ) \, . & & ( 2 6 1 ) \\ & & U \\$$

The independence condition (51) for K quantum systems is fully equivalent to the condition (10). This can be formally expressed by the following

Lemma B.18. Let us consider K quantum systems { X i } i = 1 ,...,K , a quantum system M and the set of indices K = { 1 , . . . , K } . Then

$$S ( A _ { 1 } \dots A _ { K } | M ) & = \sum _ { k = 1 } ^ { K } S ( A _ { k } | M ) & \text {extension} & \quad ( 2 6 ) \\ \Longleftrightarrow I ( X _ { A } \colon X _ { B } | M ) & = 0 \ \forall \mathcal { A } , \mathcal { B } \subseteq \mathcal { K } \ s . t . \ \mathcal { A } \cap \mathcal { B } = \emptyset \, ,$$

$$\Longleftrightarrow I ( X _ { \mathcal { A } } \colon X _ { \mathcal { B } } | M ) = 0 \ \forall \mathcal { A } , \mathcal { B } \subseteq \mathcal { K } \ s . t . \ \mathcal { A } \cap \mathcal { B } = \varnothing \, , \\ \\ \\$$

where, given a subset of indices D = { j 1 , . . . , j r } ⊂ K , X D is defined as X D ∶= X j 1 . . . X j r .

Proof. Let us prove the two implications separately. First of all, let's notice that

$$S ( A _ { 1 } \dots A _ { K } | M ) & = \sum _ { k = 1 } ^ { K } S ( A _ { k } | M ) & & \text {written} \\ & \iff S ( X _ { \mathcal { C } } | M ) = \sum _ { k = 1 } ^ { | \mathcal { C } | } S ( X _ { l _ { k } } | M ) \ \forall \mathcal { C } \subset \mathcal { K } \, . & & \text {since } m \ \text {where} \\ \intertext { The implication } & \longleftarrow S ( X _ { \mathcal { C } } | M ) = \sum _ { k = 1 } ^ { K } S ( X _ { l _ { k } } | M ) \ \forall \mathcal { C } \subset \mathcal { K } \, . & & \text {since } m \ \text {proof.} \\ \intertext { The implication } & \longleftarrow \, \text {"" is obvious by considering } \mathcal { C } = \mathcal { K } . \, \text {The} \quad a \, \text {linear}$$

The implication ' ⇐/Leftrightline ' is obvious by considering C = K . The implication ' /Leftrightline⇒ ' is a consequence of the following.

$$\sum _ { k \in \mathcal { C } } S ( A _ { k } | M ) + \sum _ { k \in \mathcal { K } \subset \mathcal { C } } S ( A _ { k } | M ) & = S ( A _ { 1 } \dots A _ { K } | M ) & \text { \quad and } & \text { \quad are   unique} \\ & \leq S ( X _ { C } | M ) + S ( X _ { \mathcal { C } } | M ) \, , \quad ( \text {Propis} )$$

whence

$$0 & \leq \left ( \sum _ { k \in \mathcal { C } } S ( A _ { k } | M ) - S ( X _ { \mathcal { C } } | M ) \right ) + \\ & + \left ( \sum _ { k \in \mathcal { K } \subset \mathcal { C } } S ( A _ { k } | M ) - S ( X _ { \mathcal { K } \subset } | M ) \right ) \leq 0 \, , \\ \intertext { f o r w h i c h e t s e d o n e q u a t i o n i n ( 2 6 3 ) . }$$

from which the second equation in (263).

$$\text {from which the second equation in (263).} \\ a ) \stackrel { ( a ) } { \sim } \colon = \colon \text {Let's consider two disjoint subsets } \mathcal { A } = \\ \{ i _ { 1 } , \dots , i _ { m } \} , \mathcal { B } = \{ j _ { 1 } , \dots , j _ { r } \} \text { of the set of indexes } K , \text { then} \\ I ( X _ { A } \colon X _ { B } | M ) \\ = S ( X _ { \mathcal { A } } | M ) + S ( X _ { B } | M ) - S ( X _ { \mathcal { A } } X _ { B } | M ) \\ = \sum _ { q = 1 } ^ { m } S ( X _ { i _ { q } } | M ) + \sum _ { s = 1 } ^ { r } S ( X _ { j _ { s } } | M ) + \\ - \left ( \sum _ { q = 1 } ^ { m } S ( X _ { i _ { q } } | M ) + \sum _ { s = 1 } ^ { r } S ( X _ { j _ { s } } | M ) \right ) \\ = 0 . \\ b ) \stackrel { ( r ) } { \longleftarrow } \colon = \colon \text {Given } \mathcal { C } = \{ j _ { 1 } , \dots , j _ { r } \} \subset \mathcal { K } , \text { let's define } \mathcal { A } = \\ \{ j _ { 1 } , \dots , j _ { r - 1 } \} \text { and } \mathcal { B } = \{ j _ { r } \} . \text {Then}$$

b) ' ⇐/Leftrightline ': Given C = { j 1 , . . . , j r } ⊂ K , let's define A= { j 1 , . . . , j r -1 } and B = { j r } . Then

$$S ( X _ { \mathcal { A } } \colon X _ { j _ { r } } | M ) & = S ( X _ { \mathcal { A } } | M ) + S ( X _ { j _ { r } } | M ) - I ( X _ { \mathcal { A } } \colon X _ { j _ { r } } | M ) \\ & = S ( X _ { \mathcal { A } } | M ) + S ( X _ { j _ { r } } | M ) \, .$$

By applying this decomposition recursively, we obtain exactly what we want to prove.

Under the action of quantum channels, the following proposition holds true [59, Chapter 4].

Proposition B.19 (data-processing inequality) . Given the quantum channel Φ A ⊗ ✶ B ∶ AB → A ′ B , the following inequality holds

<!-- formula-not-decoded -->

Remark B.20 . In this case it is sufficient that ˆ ρ AB is an extension of ˆ ρ A .

This therefore says that the quantum mutual information between two systems A and B decreases under the action of a quantum channel Φ on one of the two systems.

Lemma B.21. Given two bosonic Gaussian states ˆ ρ γ and ˆ ρ β , with the same first moments and covariance matrices γ and β respectively, with γ ≥ β , it follows that the state ˆ ρ γ can be written as

<!-- formula-not-decoded -->

where X is a centered Gaussian random variable with covariance matrix equal to γ -β .

Proof. Knowing that ˆ ρ β is a bosonic Gaussian state and that a linear combination of Gaussian states is still a Gaussian state, we can conclude that the RHS of Equation (269) is still a Gaussian state. Moreover, knowing that Gaussian states are uniquely determined by their first and second moments (Proposition II.12), in order to verify equality (269) it is sufficient to verify that the states at the LHS and RHS have the same first moments and covariance matrices. Assuming r ( ˆ ρ γ ) = r ( ˆ ρ β ) = ¯ r , for the first moments we have:

<!-- formula-not-decoded -->

where we used the linearity of the trace, the property described in Section II-A and the normalisation and symmetry of the Gaussian integral. Equation (270) therefore tells us that the states at the RHS and LHS of Equation (269) have the same first moments. Exploiting the same properties, for the second moments we have

<!-- formula-not-decoded -->

where we used that the fact that the covariance matrix of the random variable X , with zero mean, is written as γ ij -β ij = E [ x i x j ] = ∫ R n x i x j d µ X ( x ) . Finally then, the state covariance matrix of the state to the RHS of Equation (269) is

<!-- formula-not-decoded -->

Equation (272) thus proves that the states at the RHS and LHS of Equation (269) also have the same second moments.

Lemma B.22. Given a bosonic Gaussian channel Φ ∶ A → BCD , defined by the matrices ( K,α ) , the quantity ¯ S ( γ ) ∶= S ( B ∣ C ) Φ ( ˆ ρ γ A ) + S ( B ∣ D ) Φ ( ˆ ρ γ A ) is increasing in the covariance matrix γ of the Gaussian state ˆ ρ γ A .

Proof. From Lemma III.8, Lemma B.21, the linearity of quantum channels and exploiting the concavity and invariance under local unitaries of the conditional entropy, it holds

$$\begin{array} { r l } & { \text {ing} \quad \text {under local unitaries of the conditional entropy, it holds} } \\ & { \quad \bar { S } \left ( \Phi ( \hat { \rho } _ { A } ^ { \gamma } ) \right ) = \bar { S } \left ( \Phi \left ( \int _ { \mathbb { R } ^ { n } } \hat { D } _ { x } \, \hat { \rho } _ { A } ^ { \beta } \, \hat { D } _ { x } ^ { \dagger } \, d \mu _ { X } ( x ) \right ) \right ) } \\ & { ) } & { = \bar { S } \left ( \int _ { \mathbb { R } ^ { n } } \Phi \left ( \hat { D } _ { x } \, \hat { \rho } _ { A } ^ { \beta } \, \hat { D } _ { x } ^ { \dagger } \right ) d \mu _ { X } ( x ) \right ) } \\ & { \geq \int _ { \mathbb { R } ^ { n } } \bar { S } \left ( \Phi \left ( \hat { D } _ { x } \, \hat { \rho } _ { A } ^ { \beta } \, \hat { D } _ { x } ^ { \dagger } \right ) \right ) d \mu _ { X } ( x ) } \\ & { = \int _ { \mathbb { R } ^ { n } } \bar { S } \left ( \hat { D } _ { K x } \, \Phi \left ( \hat { \rho } _ { A } ^ { \beta } \right ) \hat { D } _ { K x } ^ { \dagger } \right ) d \mu _ { X } ( x ) } \\ & { = \int _ { \mathbb { R } ^ { n } } \bar { S } \left ( \Phi ( \hat { \rho } _ { A } ^ { \beta } ) \right ) d \mu _ { X } ( x ) } \\ & { = \bar { S } \left ( \Phi ( \hat { \rho } _ { A } ^ { \beta } ) \right ) , } \\ & { \text {the} } & { = \bar { S } \left ( \hat { \rho } _ { A } ^ { \beta } \right ) , } \\ & { \text {same} \quad \text {where} \ \hat { \rho } _ { A } ^ { \beta } \text { and } X \text { are defined as in Lemma B.21.} } & { \Box } \\ & { \end{array}$$

where ˆ ρ β A and X are defined as in Lemma B.21.

Lemma B.23. Given a Gaussian state ˆ ρ γ ABC of the tripartite bosonic quantum system ABC with covariance matrix γ , the function

$$\bar { S } ( \gamma ) \coloneqq S ( A | B ) _ { \hat { \rho } _ { A B C } ^ { \gamma } } + S ( A | C ) _ { \hat { \rho } _ { A B C } ^ { \gamma } } \quad ( 2 7 4 ) \\ \vdots \quad \vdots \quad \vdots \quad \vdots \quad \vdots \quad \vdots \quad \vdots \quad \vdots \quad \vdots$$

is increasing in the covariance matrix, i.e. , γ ≥ β implies ¯ S ( γ ) ≥ ¯ S ( β ) .

Proof. This is a direct consequence of Proposition B.22, assuming the bosonic Gaussian channel Φ ∶ ABC → ABC being the identity.

Proposition B.24. Let A , B and C be three bosonic quantum systems and let Φ ∶ A → BC be a bosonic Gaussian channel. Let ˆ ρ A be a state of A with finite average energy, and let ˆ ω A be the Gaussian state with the same first and second moments as ˆ ρ A . Let ˆ ω BC ∶= Φ A → BC ( ˆ ω A ) and ˆ ρ BC ∶= Φ A → BC ( ˆ ρ A ) . Then,

$$S ( B | C ) _ { \hat { \omega } _ { B C } } \geq S ( B | C ) _ { \hat { \rho } _ { B C } } \, . \\ \\$$

Proof. We first verify that for each density operator ˆ ρ A with finite average energy and first and second moments equal to those of a Gaussian state ˆ ω A it holds

$$S ( B | C ) _ { \hat { \omega } _ { B C } } - S ( B | C ) _ { \hat { \rho } _ { B C } } = S ( \hat { \rho } _ { B C } \| \hat { \omega } _ { B C } ) - S ( \hat { \rho } _ { C } \| \hat { \omega } _ { C } ) \, . \\ \\ = \bar { S } ( 2 6 )$$

From the definitions of these quantities, it is easy to verify that this equality (276) is verified if and only if

tr [( ˆ ρ BC -ˆ ω BC )(-ln ˆ ω BC -ˆ ✶ B ⊗ ln ˆ ω C )] = 0 . (277) This condition, being ˆ ρ BC -ˆ ω BC = Φ ( ˆ ρ A -ˆ ω A ) , can be rewritten as

tr [( ˆ ρ A -ˆ ω A ) Φ † A → BC (-ln ˆ ω BC -ˆ ✶ B ⊗ ln ˆ ω C )] = 0 . (278) This means that the initial states ˆ ρ A and ˆ ω A must have the same energy with respect to the Hamiltonian Φ † A → BC (-ln ˆ ω BC -ˆ ✶ B ⊗ ln ˆ ω C ) . Since this Hamiltonian is a quadratic polynomial in the quadratures and since ˆ ρ A and ˆ ω A have the same first and second moments then the equation above is verified. To conclude then

$$S ( B | C ) _ { \hat { \omega } } - S ( B | C ) _ { \hat { \rho } } = S ( \hat { \rho } _ { B C } \| \hat { \omega } _ { B C } ) - S ( \hat { \rho } _ { C } \| \hat { \omega } _ { C } ) \geq 0 \, , \\$$

where we have exploited the monotonicity of the relative entropy. Hence the thesis follows.

Proposition B.25. Given the covariance matrix σ E ∈ R 2 n × 2 n &gt; 0 of the environment state and the symplectic matrix S SE ∶= ( S SS S SE S ES S EE ) ∈ Sp ( 4 n, R ) of the coupling describing a bosonic Gaussian channel, the matrices describing the channel are given by K = S SS and α = S SE σ E S T SE .

Proof. Knowing that the symplectic matrix describing the unitary ˆ U SE and acting on the system SE is given by

$$S _ { S E } \coloneqq \begin{pmatrix} S _ { S S } & S _ { S E } \\ S _ { E S } & S _ { E E } \end{pmatrix} , \quad ( 2 8 0 ) \quad \text {In} \quad \substack { 2 0 8 0 \\ 2 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 $$

and that the covariance matrix of the initial joint state is given by σ SE = σ S ⊕ σ E , where σ E is the covariance matrix of the environment state, the symplectic transformation acts on the overall state covariance matrix as

$$S \sigma _ { S E } S _ { S E } ^ { T } & = \begin{pmatrix} S _ { S S } & S _ { S E } \\ S _ { E S } & S _ { E E } \end{pmatrix} \begin{pmatrix} \sigma _ { S } & 0 \\ 0 & \sigma _ { E } \end{pmatrix} \begin{pmatrix} S _ { S S } ^ { T } & S _ { E S } ^ { T } \\ S _ { S E } ^ { T } & S _ { E E } ^ { T } \end{pmatrix} \\ & = \begin{pmatrix} S _ { S S } \sigma _ { S } S _ { S S } ^ { T } + S _ { S E } \sigma _ { S } S _ { S E } ^ { T } & * \\ * & * \end{pmatrix} . \quad \text {and} \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { }$$

From the equation above, we therefore have that the channel acts on the matrix σ S as

$$\sigma _ { S } & \longrightarrow K \, \sigma _ { S } \, K ^ { T } + \alpha \\ & = S _ { S S } \, \sigma _ { S } \, S _ { S S } ^ { T } + S _ { S E } \, \sigma _ { E } \, S _ { S E } ^ { T } \, , \\ \text {which we derive that} & \quad \text {the} \quad \text {the} \, \sigma _ { S }$$

from which we derive that

$$K \coloneqq S _ { S S } \, , \quad \alpha \coloneqq S _ { S E } \, \sigma _ { E } \, S _ { S E } ^ { T } \, . \\$$

Proposition B.26. Let us consider a beam splitter that uniformly combines the modes of the input states, i.e. , the attenuation parameter is equal to η for all modes. Then, applying a symplectic to one input of that beam splitter is equivalent to applying that symplectic to the output and its inverse to the other input. Let Φ ˆ ϕ E η ( ˆ ρ A ) be the channel described by a beam splitter with a uniform attenuation parameter η that makes the state of the system ˆ ρ A interact with the environment state ˆ ϕ E , then it holds

$$\Phi _ { \eta } ^ { \hat { \phi } _ { E } } ( \hat { U } _ { S } \, \hat { \rho } _ { A } \, \hat { U } _ { S } ^ { \dagger } ) & = \hat { U } _ { S } \, \Phi _ { \eta } ^ { \hat { U } _ { S } ^ { \dagger } \, \hat { \phi } _ { E } \, \hat { U } _ { S } } ( \hat { \rho } _ { A } ) \, \hat { U } _ { S } ^ { \dagger } . \\ \\ \Phi _ { \eta } ^ { \hat { \phi } _ { E } } ( \hat { U } _ { S } \, \hat { \rho } _ { A } \, \hat { U } _ { S } ^ { \dagger } ) & = \hat { U } _ { S } \, \Phi _ { \eta } ^ { \hat { U } _ { S } ^ { \dagger } \, \hat { \phi } _ { E } \, \hat { U } _ { S } } ( \hat { \rho } _ { A } ) \, \hat { U } _ { S } ^ { \dagger } . \\$$

Proof. The proof is straightforward and proceeds as follows.

$$P r o f . \text { The proof is straightforward and proceeds as follows. } & \quad \text {Finally,} \\ \Phi _ { \eta } ^ { \hat { \phi } _ { E } } ( \hat { U } _ { S } \hat { \rho } _ { A } \hat { U } _ { S } ^ { \dagger } ) & & - \left ( - \alpha \left ( \hat { \rho } \left ( \hat { U } _ { S } \left ( \hat { U } _ { A } \hat { U } _ { S } ^ { \dagger } \right ) \\ = \text {tr} _ { E } \left [ \hat { U } _ { \eta } \left ( \hat { U } _ { S } \hat { \rho } _ { A } \hat { U } _ { S } ^ { \dagger } \otimes \hat { \phi } _ { E } \right ) \hat { U } _ { \eta } ^ { \dagger } \right ] & & B . \ L o w a l \\ & = \text {tr} _ { E } \left [ \hat { U } _ { \eta } \left ( \hat { U } _ { S } \otimes \hat { U } _ { S } \right ) \left ( \hat { \rho } _ { A } \otimes \hat { U } _ { S } ^ { \dagger } \hat { \phi } _ { E } \hat { U } _ { S } \right ) \left ( \hat { U } _ { S } \otimes \hat { U } _ { S } \right ) ^ { \dagger } \hat { U } _ { \eta } ^ { \dagger } \right ] & & \text {to comp} \\ & = \text {tr} _ { E } \left [ \left ( \hat { U } _ { S } \otimes \hat { U } _ { S } \right ) \hat { U } _ { \eta } \left ( \hat { \rho } _ { A } \otimes \hat { U } _ { S } ^ { \dagger } \hat { \phi } _ { E } \hat { U } _ { S } \right ) \hat { U } _ { \eta } ^ { \dagger } \left ( \hat { U } _ { S } \otimes \hat { U } _ { S } \right ) ^ { \dagger } \right ] & & \text {sian char} \\ & = \hat { U } _ { S } \text {tr} _ { E } [ \hat { U } _ { \eta } \left ( \hat { \rho } _ { A } \otimes \hat { U } _ { S } ^ { \dagger } \hat { \phi } _ { E } \hat { U } _ { S } \right ) \hat { U } _ { \eta } ^ { \dagger } ] & & \sup o v { \text { } & & \text {sup over} \\ & = \hat { U } _ { S } \Phi _ { \eta } ^ { \hat { U } _ { S } ^ { \dagger } \hat { \phi } _ { E } \hat { U } _ { S } } ( \hat { \rho } _ { A } ) \hat { U } _ { S } ^ { \dagger } . & & \text {channel} \\ & = \hat { U } _ { S } \Phi _ { \eta } ^ { \hat { U } _ { S } ^ { \dagger } \hat { \phi } _ { E } \hat { U } _ { S } } ( \hat { \rho } _ { A } ) \hat { U } _ { S } ^ { \dagger } . & & \text {a simple} \\ & \quad \Box \quad \text {the input}$$

Proposition B.27. The squashed entanglement is invariant under local unitary transformations, i.e. ,

$$g _ { \ } a & & E _ { s q } ( \hat { \rho } _ { A B } ) = E _ { s q } \left ( \left ( \hat { U } _ { A } \otimes \hat { U } _ { B } \right ) \hat { \rho } _ { A B } \left ( \hat { U } _ { A } \otimes \hat { U } _ { B } \right ) ^ { \dagger } \right ) . \quad ( 2 8 6 ) \\ \ n n e l & & E _ { s q } = - \, \overline { E } _ { s q } \left ( \left ( \hat { U } _ { A } \otimes \hat { U } _ { B } \right ) \hat { \rho } _ { A B } \left ( \hat { U } _ { A } \otimes \hat { U } _ { B } \right ) ^ { \dagger } \right ) .$$

Proof. This is true since squashed entanglement is a entanglement measure, see [50].

## APPENDIX C NUMERICAL SIMULATIONS

In this section, the analytical results of Section VI are discussed.

## A. Extremality condition

In this subsection we verify that the channel defined in Equation (187) fulfils the condition of being extreme, following the algorithm proposed in Section V-B. First, we derive the matrices K and α that describe the channel we wish to treat. The symplectic matrix describing the unitary ˆ U ( η 1 ,η 2 ) SE and acting on the system SE is given by

$$\text { and } \text {acting on the system } S E \text { is given by} \\ \text {channel} \quad & \quad S _ { S E } ^ { ( \eta _ { 1 } , \eta _ { 2 } ) } \equiv \left ( \begin{array} { c c c c } \sqrt { \eta _ { 1 } } \, I _ { 2 } & 0 & \sqrt { 1 - \eta _ { 1 } } \, I _ { 2 } & 0 \\ 0 & \sqrt { \eta _ { 2 } } \, I _ { 2 } & 0 & \sqrt { 1 - \eta _ { 2 } } \, I _ { 2 } \\ - \sqrt { 1 - \eta _ { 1 } } \, I _ { 2 } & 0 & \sqrt { \eta _ { 1 } } \, I _ { 2 } & 0 \\ 0 & - \sqrt { 1 - \eta _ { 2 } } \, I _ { 2 } & 0 & \sqrt { \eta _ { 2 } } \, I _ { 2 } \end{array} \right ) , \\ \text {while the covariance matrix } \sigma _ { F } \text { of the environment state is}$$

while the covariance matrix σ E of the environment state is the covariance matrix of the two-mode squeezed vacuum state ˆ ϕ κ E ,

$$\sigma _ { E } = \begin{pmatrix} \left ( \kappa - \frac { 1 } { 2 } \right ) I _ { 2 } & \sqrt { \kappa ( \kappa - 1 ) } \, Z _ { 2 } \\ \sqrt { \kappa ( \kappa - 1 ) } \, Z _ { 2 } & \left ( \kappa - \frac { 1 } { 2 } \right ) I _ { 2 } \end{pmatrix} . \quad ( 2 8 8 ) \\ \intertext { o r m a l o r i h t h \, 1 \, a b o v e , \, w e t h e r e f o r e \, have t h e t h e \, c h i n n e }$$

From Algorithm 1 above, we therefore have that the channel is described by the matrices

$$K = \left ( \begin{matrix} \sqrt { \eta _ { 1 } } \, I _ { 2 } & 0 \\ 0 & \sqrt { \eta _ { 2 } } \, I _ { 2 } \end{matrix} \right )$$

and

$$\begin{array} { r l } & { a n d } \\ { t a t e \hat { \phi } _ { E } , } & { \alpha = \left ( \begin{matrix} \left ( \kappa - \frac { 1 } { 2 } \right ) ( 1 - \eta _ { 1 } ) \, I _ { 2 } & \sqrt { \kappa ( \kappa - 1 ) ( 1 - \eta _ { 1 } ) ( 1 - \eta _ { 2 } ) } \, Z _ { 2 } \\ \sqrt { \kappa ( \kappa - 1 ) ( 1 - \eta _ { 1 } ) ( 1 - \eta _ { 2 } ) } \, Z _ { 2 } & \left ( \kappa - \frac { 1 } { 2 } \right ) ( 1 - \eta _ { 2 } ) \, I _ { 2 } \\ \end{matrix} \right ) . } \\ & { ( 2 8 4 ) } \\ & { \quad \text {Finally, } \quad i t \quad i s \quad e a s y \quad t o \quad \text {verify } \quad i n \quad o r \quad c a s e \quad t h a t } \end{array}$$

Finally, it is easy to verify in our case that -(-α ( ∆ -K ∆ K T ) -1 ) 2 is equal to I 4 / 4 .

## B. Lower bound

In this section we apply the algorithm of Section V-D to compute the lower bound of the extreme bosonic Gaussian channel N ( η 1 ,η 2 ) S → S we are considering. Knowing that the squashed entanglement of the channel is defined by taking the sup over all possible input states on a bipartite system of the squashed entanglement of the state obtained by applying the channel to the reduced state on one of the two initial systems, a simple way to find a lower bound to this quantity is to fix the input state. Let us then take as the input state the tensor product of 2 two-mode squeezed vacuum states ˆ ϕ N 1 A 1 B 1 ⊗ ˆ ϕ N 2 A 2 B 2

on the bipartite system AB , with average number of photons N 1 and N 2 respectively. Let us then apply the considered channel N ( η 1 ,η 2 ) B → D on the system B and compute the squashed entanglement of the resulting state. Knowing that the lower bound of the squashed entanglement of a state (in our case the channel's output state) is a function of the blocks of the symplectic matrix that diagonalises the covariance matrix of the considered state, we must find the symplectic matrix that diagonalises the covariance matrix of the channel's output state, which is given by

$$& ( \mathbb { 1 } _ { A } \otimes \mathcal { N } _ { B } ) \left ( \hat { \phi } _ { A _ { 1 } B _ { 1 } } ^ { N _ { 1 } } \otimes \hat { \phi } _ { A _ { 2 } B _ { 2 } } ^ { N _ { 2 } } \right ) & \text { of the } \text { the } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { }$$

First, we compute the covariance matrix σ CD of the output state ( ✶ A ⊗N B )( ˆ ϕ N 1 ⊗ ˆ ϕ N 2 ) AB of the channel. In particular, the symplectic matrix associated with the unitary transformation ˆ ✶ A ⊗ ˆ U ( η 1 ,η 2 ) BE is given by

$$S _ { A B E } ^ { \eta } = \begin{pmatrix} I _ { 4 } & 0 \\ 0 & S _ { \eta } \end{pmatrix} , \quad \quad ( 2 9 2 ) \quad \text {and}$$

where S η ∶= S ( η 1 ,η 2 ) BE is defined in Equation (287) and the covariance matrix of the overall input state ( ˆ ϕ N 1 ⊗ ˆ ϕ N 2 ) AB ⊗ ˆ ϕ N 3 E is given by

$$\sigma _ { A B E } = \sigma _ { A B } \oplus \sigma _ { E } \, ,$$

where

$$\text {where} & & \quad \ \ 0 & \sqrt { N _ { 1 } ( N _ { 1 } + 1 ) } Z _ { 2 } & \ 0 \\ \sigma _ { A B } & \frac { 0 } { \sqrt { N _ { 1 } ( N _ { 1 } + 1 ) } Z _ { 2 } } & \ 0 & \left ( N _ { 2 } + \frac { 1 } { 2 } \right ) I _ { 2 } & \ 0 & \sqrt { N _ { 2 } ( N _ { 2 } + 1 ) } Z _ { 2 } \\ & \quad 0 & \sqrt { N _ { 2 } ( N _ { 2 } + 1 ) } Z _ { 2 } & 0 & \left ( N _ { 1 } + \frac { 1 } { 2 } \right ) I _ { 2 } & \ 0 \\ & \quad 0 & \sqrt { N _ { 2 } ( N _ { 2 } + 1 ) } Z _ { 2 } & 0 & \left ( N _ { 2 } + \frac { 1 } { 2 } \right ) I _ { 2 } \\ & \quad \ \ 2 & \sqrt { N _ { 2 } ( N _ { 2 } + 1 ) } Z _ { 2 } & 0 & \left ( N _ { 2 } + \frac { 1 } { 2 } \right ) I _ { 2 } \\ & \quad \ \ 2 & S _ { \eta } = & \\$$

and

The matrix σ CD is then derived by considering the appropriate submatrix of the covariance matrix of the overall channel's output state

$$& \text {and} \\ & \sigma _ { E } = \begin{pmatrix} \left ( N _ { 3 } + \frac { 1 } { 2 } \right ) I _ { 2 } & \sqrt { N _ { 3 } ( N _ { 3 } + 1 ) } \, Z _ { 2 } \\ \sqrt { N _ { 3 } ( N _ { 3 } + 1 ) } \, Z _ { 2 } & \left ( N _ { 3 } + \frac { 1 } { 2 } \right ) I _ { 2 } \end{pmatrix} . \quad ( 2 9 5 ) \\ & \text {The matrix } \sigma _ { E } \text { is then derived by considering the appropriate}$$

$$\sigma _ { C D E } = S _ { A B E } \, \sigma _ { A B E } \, S _ { A B E } \, . \\ \intertext { i n v e r } i _ { C D E } = S _ { A B E } \, \sigma _ { A B E } \, S _ { A B E } \, . \\$$

The matrix σ CD is derived in Appendix A-C and its explicit form can be found in Equation (217). Now, from Algorithm 3 we derive the lower bound by applying Equation (170) to the symplectic matrix which diagonalises σ CD .

## C. Upper bound

The channel we are going to consider is the one in Equation (187). As it is not an easy task to optimise over all possible squashing channels, let us consider a specific family of squashing channels: a two-mode extreme bosonic Gaussian attenuator with transmissivities ( τ 1 , τ 2 ) = ( 1 / 2 , 1 / 2 ) and the environment state a two-mode squeezed vacuum state, with average number of photons per single mode N s . For what is stated in Proposition B.24, the optimal state ˆ ρ A in Equation (157) is a Gaussian state. Moreover, fixed the squashing channel, Lemma B.23 implies that the quantity S ( B ∣ E ′′ ) ˆ ψ + S ( B ∣ F ′ ) ˆ ψ in Equation (157) is an increasing function in the covariance matrix. This means that the supremum on the states can be taken by considering any sequence of states with covariance matrix whose eigenvalues go to infinite. For convenience we therefore choose a sequence of thermal states with covariance matrix

$$\sigma _ { A } = \begin{pmatrix} ( t + \frac { 1 } { 2 } ) \, I _ { 2 } & 0 \\ 0 & ( t + \frac { 1 } { 2 } ) \, I _ { 2 } \end{pmatrix} .$$

Since, in the physical representation of the channel, the state of the environment we are going to consider is a two-mode squeezed vacuum state, with average number of photons per single mode N 3 , and since the environment on which the squashing channel acts is the two-mode squeezed vacuum state, the covariance matrix of the initial state in the system AEF is given by σ A ⊕ σ E ⊕ σ F , where

$$\sigma _ { E } = \begin{pmatrix} \left ( N _ { 3 } + \frac { 1 } { 2 } \right ) I _ { 2 } & \sqrt { N _ { 3 } ( N _ { 3 } + 1 ) } \, Z _ { 2 } \\ \sqrt { N _ { 3 } ( N _ { 3 } + 1 ) } \, Z _ { 2 } & \left ( N _ { 3 } + \frac { 1 } { 2 } \right ) I _ { 2 } \end{pmatrix} \quad ( 2 9 8 ) \\ \text {and}$$

and

The covariance matrix of the state ˆ ψ BE ′′ F ′ is therefore given by

$$& \quad \text {and} \\ & \quad \ \sigma _ { F } = \begin{pmatrix} \left ( N _ { s } + \frac { 1 } { 2 } \right ) I _ { 2 } & \sqrt { N _ { s } ( N _ { s } + 1 ) } \, Z _ { 2 } \\ \sqrt { N _ { s } ( N _ { s } + 1 ) } \, Z _ { 2 } & \left ( N _ { s } + \frac { 1 } { 2 } \right ) I _ { 2 } \end{pmatrix} . \quad \ \ ( 2 9 9 ) \\ & \quad \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \$$

$$\sigma _ { B E ^ { \prime \prime } F ^ { \prime } } = S _ { \tau } \, S _ { \eta } \left ( \sigma _ { A } \oplus \sigma _ { E } \oplus \sigma _ { F } \right ) S _ { \eta } ^ { T } \, S _ { \tau } ^ { T } \, , \\$$

where S τ ∶= S ( τ 1 ,τ 2 ) E ′ F → E ′′ F ′ and S η ∶= S ( η 1 ,η 2 ) AE → BE ′ are defined as

$$\overline { Z } _ { 2 } \right ) & \quad \text {where } S _ { \tau } \coloneqq S _ { E ^ { \prime } F \rightarrow E ^ { \prime \prime } F ^ { \prime } } ^ { ( \tau _ { 1 } , \tau _ { 2 } ) } \text { and } S _ { \eta } \coloneqq S _ { A E \rightarrow B E ^ { \prime } } ^ { ( \eta _ { 1 } , \eta _ { 2 } ) } \text { are defined as } \\ \overline { Z } _ { 2 } \right ) & \quad S _ { \eta } \equiv \left ( \begin{matrix} \sqrt { \eta _ { 1 } } \, I _ { 2 } & 0 & \sqrt { 1 - \eta _ { 1 } } \, I _ { 2 } & 0 & 0 & 0 \\ 0 & \sqrt { \eta _ { 2 } } \, I _ { 2 } & 0 & \sqrt { 1 - \eta _ { 2 } } \, I _ { 2 } & 0 & 0 \\ 0 & - \sqrt { 1 - \eta _ { 1 } } \, I _ { 2 } & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & I _ { 2 } & 0 \\ 0 & 0 & 0 & 0 & 0 & I _ { 2 } \\ ( 3 0 1 ) \end{matrix} \right ) \\ \text { and } & \quad \text { and }$$

and

$$\begin{array} { r l } { o r p r i a t e } & { i n d } \\ { \text {channel's} } & { \quad } \\ { S _ { \tau } = \left ( \begin{matrix} I _ { 2 } & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & I _ { 2 } & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & \sqrt { \tau _ { 1 } } I _ { 2 } & 0 & \sqrt { 1 - \tau _ { 1 } } I _ { 2 } & 0 \\ 0 & 0 & 0 & \sqrt { \tau _ { 1 } } I _ { 2 } & 0 & \sqrt { 1 - \tau _ { 1 } } I _ { 2 } \\ 0 & 0 & - \sqrt { 1 - \tau _ { 1 } } I _ { 2 } & 0 & \sqrt { \tau _ { 1 } } I _ { 2 } & 0 \\ 0 & 0 & 0 & - \sqrt { 1 - \tau _ { 1 } } I _ { 2 } & 0 & \sqrt { \tau _ { 1 } } I _ { 2 } \\ ( 3 0 2 ) } \\ { \text {from the covariance matrix } \sigma _ { B E ^ { \prime \prime } F ^ { \prime } } \text { in Equation (300)} , \, the } \end{array} \right ) . } \end{array}$$

From the covariance matrix σ BE ′′ F ′ in Equation (300), the covariance matrices of the marginal states on the systems E ′′ , F ′ , BE ′′ and BF ′ can be obtained. Simple calculations show that these covariance matrices are linear in the parameter t , i.e. , they can be written as t U + V , where U and V are two constant symmetric matrices dependent on the other parameters involved. It is also possible to show that U is a strictly positive matrix. In what follows we will be interested in the symplectic eigenvalues of those matrices, i.e. , matrices of the form t U + V where U is strictly positive and V symmetric. For the computation of the upper bound we are interested in functions of the type g ( ν i t U + V -1 2 ) (see Algorithm 2), in the limit of t going to infinity. For this purpose, the Proposition B.4 assures us that, in this limit, we can restrict ourselves to considering only the part of t U + V proportional to t , and thus the following matrices:

$$\sigma _ { E ^ { \prime \prime } } = \begin{pmatrix} t \tau _ { 1 } \bar { \eta } _ { 1 } I _ { 2 } & 0 \\ 0 & t \tau _ { 2 } \bar { \eta } _ { 2 } I _ { 2 } \end{pmatrix} , \quad \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \$$

$$\sigma _ { F ^ { \prime } } = \begin{pmatrix} t \bar { \tau } _ { 1 } \bar { \eta } _ { 1 } I _ { 2 } & 0 \\ 0 & t \bar { \tau } _ { 2 } \bar { \eta } _ { 2 } I _ { 2 } \end{pmatrix} , \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \qu$$

$$\sigma _ { B F ^ { \prime } } \equiv \begin{pmatrix} \ t \eta _ { 1 } I _ { 2 } & 0 & \ t \sqrt { \eta _ { 1 } \bar { \tau } _ { 1 } \bar { \eta } _ { 1 } } I _ { 2 } & 0 \\ 0 & \ t \eta _ { 2 } I _ { 2 } & 0 & \ t \sqrt { \eta _ { 2 } \bar { \tau } _ { 2 } \bar { \eta } _ { 2 } } I _ { 2 } \\ \ t \sqrt { \eta _ { 1 } \bar { \tau } _ { 1 } \bar { \eta } _ { 1 } } I _ { 2 } & 0 & \bar { \ t } \bar { \tau } _ { 1 } \bar { \eta } _ { 1 } I _ { 2 } & 0 \\ 0 & \ t \sqrt { \eta _ { 2 } \bar { \tau } _ { 2 } \bar { \eta } _ { 2 } } I _ { 2 } & 0 & \ t \bar { \tau } _ { 2 } \bar { \eta } _ { 2 } I _ { 2 } \\ 0 & \ t \sqrt { \eta _ { 2 } \bar { \tau } _ { 2 } \bar { \eta } _ { 2 } } I _ { 2 } & 0 & \bar { \ t } \bar { \tau } _ { 2 } \bar { \eta } _ { 2 } I _ { 2 } \\ 3 0 3 d ) & [ 5 ] & A . S . \\ & & & \text {Intr}$$

$$\sigma _ { F ^ { \prime \prime } } = \left ( \begin{array} { c c c } 0 & t \bar { \tau } _ { 2 } \bar { \eta } _ { 2 } I _ { 2 } \\ 0 & t \bar { \tau } _ { 2 } \bar { \eta } _ { 2 } I _ { 2 } \end{array} \right ) , \quad \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \$$

where, for typographical reasons, we have defined ¯ η = 1 -η and ¯ τ = 1 -τ . The symplectic eigenvalues of these covariance matrices are ν σ E ′′ = { t τ 1 ¯ η 1 , t τ 2 ¯ η 2 } , ν σ F ′ = { t ¯ τ 1 ¯ η 1 , t ¯ τ 2 ¯ η 2 } , ν σ BE ′′ = { 0 , 0 , t ( τ 1 + ¯ τ 1 η 1 ) , t ( τ 2 + ¯ τ 2 η 2 )} and ν σ BF ′ = { 0 , 0 , t ( ¯ τ 1 + τ 1 η 1 ) , t ( ¯ τ 2 + τ 2 η 2 )} . From the formula (36) for the entropy of a bosonic Gaussian state, in the limit of infinite average number of photons t , it holds

$$S ( B | E ^ { \prime \prime } ) + S ( B | F ^ { \prime } ) & = \sum _ { i = 1 } ^ { 2 } \left [ g ( t \left ( \tau _ { i } + \bar { \tau } _ { i } \, \eta _ { i } \right ) ) - g ( t \tau _ { i } \, \bar { \eta } _ { i } ) + \\ & + g ( t \left ( \bar { \tau } _ { i } + \tau _ { i } \, \eta _ { i } \right ) ) - g ( t \bar { \tau } _ { i } \, \bar { \eta } _ { i } ) \right ] . \\$$

Having chosen τ 1 = τ 2 = 1 / 2 , an upper bound to the squashed entanglement of the channel N , in the limit t → ∞ , is therefore

$$\text {where} \\ E _ { s q } ( \mathcal { N } ) & \leq \lim _ { t \to + \infty } \sum _ { i = 1 } ^ { 2 } \left [ g ( t \, \frac { 1 + \eta _ { i } } { 2 } ) - g ( t \, \frac { 1 - \eta _ { i } } { 2 } ) \right ] \\ & = \sum _ { i = 1 } ^ { 2 } \ln \left ( \frac { 1 + \eta _ { i } } { 1 - \eta _ { i } } \right ) . \\ R e m a r k \, C . 1 . \, \text { We note that in the limit we have considered, } i . e . , \quad \left [ 1 \right ] \, \ G i a l a r { ( 3 0 5 ) } _ { i } & = 0 .$$

Remark C.1 . We note that in the limit we have considered, i.e. , in which the states on which the quantum channel acts are a family of thermal states with the number of photons going to infinity, we have obtained a straightforward multi-mode extension of the result for the one mode pure-loss bosonic channel [40, Appendix A].

## ACKNOWLEDGEMENTS

GDP has been supported by the HPC Italian National Centre for HPC, Big Data and Quantum Computing - Proposal code CN00000013 -CUP J33C22001170001 and by the Italian Extended Partnership PE01 - FAIR Future Artificial Intelligence Research -Proposal code PE00000013 - CUP J33C22002830006 under the MUR National Recovery and Resilience Plan funded by the European Union - NextGenerationEU. Funded by the European Union - NextGenerationEU under the National Recovery and Resilience Plan (PNRR)

-Mission 4 Education and research - Component 2 From research to business - Investment 1.1 Notice Prin 2022 - DD N. 104 del 2/2/2022, from title 'understanding the LEarning process of QUantum Neural networks (LeQun)', proposal code 2022WHZ5XH - CUP J53D23003890006. GDP is a member of the 'Gruppo Nazionale per la Fisica Matematica (GNFM)' of the 'Istituto Nazionale di Alta Matematica 'Francesco Severi' (INdAM)'.

## REFERENCES

- [1] T.M. Cover and J.A. Thomas. Elements of Information Theory . A Wiley-Interscience publication. Wiley, 2006.
- [2] A. Dembo, T.M. Cover, and J.A. Thomas. Information theoretic inequalities. IEEE Transactions on Information Theory , 37(6):15011518, 1991.
- [3] A.J. Stam. Some inequalities satisfied by the quantities of information of Fisher and Shannon. Information and Control , 2(2):101-112, 1959.
- [4] C. E. Shannon. A mathematical theory of communication. The Bell System Technical Journal , 27(3):379-423, 1948.
- [5] A.S. Holevo. Quantum Systems, Channels, Information: A Mathematical Introduction . Texts and monographs in theoretical physics. De Gruyter, 2019.
- [6] A. S. Holevo. Gaussian optimizers and the additivity problem in quantum information theory. Russian Mathematical Surveys , 70(2):331, apr 2015.
- [7] Krzysztof Ptaszy´ nski and Massimiliano Esposito. Quantum and classical contributions to entropy production in fermionic and bosonic gaussian systems. PRX Quantum , 4(2):020353, 2023.
- [8] Junseo Lee and Kabgyun Jeong. Quantum rényi entropy functionals for bosonic gaussian systems. Physics Letters A , 490:129183, 2023.
- [9] Ludovico Lami, Sumeet Khatri, Gerardo Adesso, and Mark M. Wilde. Extendibility of bosonic gaussian states. Physical Review Letters , 123(5):050501, 2019.
- [10] Christian Weedbrook, Stefano Pirandola, Raúl García-Patrón, Nicolas J. Cerf, Timothy C. Ralph, Jeffrey H. Shapiro, and Seth Lloyd. Gaussian quantum information. Rev. Mod. Phys. , 84:621-669, May 2012.
- [11] M.M. Wilde. Quantum Information Theory . Cambridge University Press, 2017.
- [12] Robert König and Graeme Smith. The Entropy Power Inequality for Quantum Systems. IEEE Transactions on Information Theory , 60(3):1536-1548, 2014.
- [13] Robert König and Graeme Smith. Corrections to 'The Entropy Power Inequality for Quantum Systems' [mar 14 1536-1548]. IEEE Transactions on Information Theory , 62(7):4358-4359, 2016.
- [14] Giacomo De Palma, Andrea Mari, and Vittorio Giovannetti. A generalization of the entropy power inequality to bosonic quantum systems. Nature Photonics , 8(12):958-964, 2014.
- [15] G. De Palma, A. Mari, S. Lloyd, and V. Giovannetti. Multimode quantum entropy power inequality. Phys. Rev. A , 91:032320, Mar 2015.
- [16] Giacomo De Palma. Gaussian optimizers and other topics in quantum information. arXiv:1710.09395 , 2017.
- [17] Robert König. The conditional entropy power inequality for Gaussian quantum states. Journal of Mathematical Physics , 56(2), 02 2015. 022201.
- [18] Giacomo De Palma and Dario Trevisan. The conditional entropy power inequality for bosonic quantum systems. Communications in Mathematical Physics , 360:639-662, 2018.
- [19] Giacomo De Palma and Stefan Huber. The conditional entropy power inequality for quantum additive noise channels. Journal of Mathematical Physics , 59(12), 12 2018. 122201.
- [20] Robert R. Tucci. Quantum Entanglement and Conditional Information Transmission. arXiv:quant-ph/9909041 , 1999.
- [21] Robert R. Tucci. Separability of Density Matrices and Conditional Information Transmission. arXiv:quant-ph/0005119 , 2000.
- [22] Robert R. Tucci. Entanglement of Formation and Conditional Information Transmission. arXiv:quant-ph/0010041 , 2000.
- [23] Robert R. Tucci. Relaxation Method For Calculating Quantum Entanglement. arXiv:quant-ph/0101123 , 2001.
- [24] Robert R. Tucci. Entanglement of Bell Mixtures of Two Qubits. arXiv:quant-ph/0103040 , 2001.
- [25] Robert R. Tucci. Entanglement of Distillation and Conditional Mutual Information. arXiv:quant-ph/0202144 , 2002.

- [26] Matthias Christandl and Andreas Winter. 'squashed entanglement': An additive entanglement measure. Journal of Mathematical Physics , 45(3):829-840, 02 2004.
- [27] Fernando GSL Brandao, Matthias Christandl, and Jon Yard. Faithful squashed entanglement. Communications in Mathematical Physics , 306:805-830, 2011.
- [28] Kaushik P Seshadreesan, Mario Berta, and Mark M Wilde. Rényi squashed entanglement, discord, and relative entropy differences. Journal of Physics A: Mathematical and Theoretical , 48(39):395303, sep 2015.
- [29] K. Audenaert, J. Eisert, E. Jané, M. B. Plenio, S. Virmani, and B. De Moor. Asymptotic Relative Entropy of Entanglement. Phys. Rev. Lett. , 87:217902, Nov 2001.
- [30] V. Vedral. The role of relative entropy in quantum information theory. Rev. Mod. Phys. , 74:197-234, Mar 2002.
- [31] Matthias Christandl, Artur Ekert, Michał Horodecki, Paweł Horodecki, Jonathan Oppenheim, and Renato Renner. Unifying classical and quantum key distillation. In Theory of Cryptography: 4th Theory of Cryptography Conference, TCC 2007, Amsterdam, The Netherlands, February 21-24, 2007. Proceedings 4 , pages 456-478. Springer, 2007.
- [32] Ke Li and Andreas Winter. Relative entropy and squashed entanglement. Communications in Mathematical Physics , 326:63-80, 2014.
- [33] Mark M Wilde. Squashed entanglement and approximate private states. Quantum Information Processing , 15(11):4563-4580, 2016.
- [34] Kaushik P. Seshadreesan and Mark M. Wilde. Fidelity of recovery, squashed entanglement, and measurement recoverability. Phys. Rev. A , 92:042321, Oct 2015.
- [35] Ke Li and Andreas Winter. Squashed entanglement, k-extendibility, quantum markov chains, and recovery maps. Foundations of Physics , 48(8):910-924, 2018.
- [36] Gerardo Adesso, Marie Ericsson, and Fabrizio Illuminati. Coexistence of unlimited bipartite and genuine multipartite entanglement: Promiscuous quantum correlations arising from discrete to continuous-variable systems. Phys. Rev. A , 76:022315, Aug 2007.
- [37] David Avis, Patrick Hayden, and Ivan Savov. Distributed compression and multiparty squashed entanglement. Journal of Physics A: Mathematical and Theoretical , 41(11):115301, mar 2008.
- [38] Dong Yang, Karol Horodecki, Michal Horodecki, Pawel Horodecki, Jonathan Oppenheim, and Wei Song. Squashed Entanglement for Multipartite States and Entanglement Measures Based on the Mixed Convex Roof. IEEE Transactions on Information Theory , 55(7):33753387, 2009.
- [39] Stefano Pirandola, Riccardo Laurenza, Carlo Ottaviani, and Leonardo Banchi. Fundamental limits of repeaterless quantum communications. Nature communications , 8(1):15043, 2017.
- [40] Masahiro Takeoka, Saikat Guha, and Mark M. Wilde. The Squashed Entanglement of a Quantum Channel. IEEE Transactions on Information Theory , 60(8):4987-4998, 2014.
- [41] Mario Berta and Mark M Wilde. Amortization does not enhance the max-Rains information of a quantum channel. New Journal of Physics , 20(5):053044, may 2018.
- [42] Giacomo De Palma. The squashed entanglement of the noiseless quantum Gaussian attenuator and amplifier. Journal of Mathematical Physics , 60(11), 11 2019. 112201.
- [43] Alessandro Ferraro, Stefano Olivares, and Matteo GA Paris. Gaussian states in continuous variable quantum information. arXiv preprint quantph/0503237 , 2005.
- [44] A. Serafini. Quantum Continuous Variables: A Primer of Theoretical Methods . CRC Press, 2017.
- [45] Alexander Semenovich Holevo. Extreme bosonic linear channels. Theoretical and Mathematical Physics , 174:288-297, 2013.
- [46] Patrick J Coles, Mario Berta, Marco Tomamichel, and Stephanie Wehner. Entropic uncertainty relations and their applications. Reviews of Modern Physics , 89(1):015002, 2017.
- [47] Giacomo De Palma and Dario Trevisan. The generalized strong subadditivity of the von neumann entropy for bosonic quantum gaussian systems. arXiv preprint arXiv:2105.05627 , 2021.
- [48] Giacomo De Palma. The entropy power inequality with quantum conditioning. Journal of Physics A: Mathematical and Theoretical , 52(8):08LT03, 2019.
- [49] Masahiro Takeoka, Saikat Guha, and Mark M Wilde. Fundamental rateloss tradeoff for optical quantum key distribution. Nature communications , 5(1):5235, 2014.
- [50] Vlatko Vedral, Martin B Plenio, Michael A Rippin, and Peter L Knight. Quantifying entanglement. Physical Review Letters , 78(12):2275, 1997.
- [51] Martin B Plenio and Shashank Virmani. An introduction to entanglement measures. arXiv preprint quant-ph/0504163 , 2005.
- [52] Tanvi Jain. Sums and products of symplectic eigenvalues. Linear Algebra and its Applications , 631:67-82, 2021.
- [53] Jean Gallier. The schur complement and symmetric positive semidefinite (and definite) matrices, August 2019. Version dated 24 August 2019.
- [54] F. Zhang. Matrix Theory: Basic Results and Techniques . Universitext. Springer New York, 2011.
- [55] Bruno Zumino. Normal forms of complex matrices. Journal of Mathematical Physics , 3(5):1055-1057, 1962.
- [56] HG Becker. On the transformation of a complex skew-symmetric matrix into a real normal form and its application to a direct proof of the blochmessiah theorem. Lettere al Nuovo Cimento (1971-1985) , 8:185-188, 1973.
- [57] W.H. Greub. Linear Algebra . Graduate Texts in Mathematics. Springer New York, 2012.
- [58] M.A. Nielsen and I.L. Chuang. Quantum Computation and Quantum Information . Cambridge Series on Information and the Natural Sciences. Cambridge University Press, 2000.
- [59] Sumeet Khatri and Mark M Wilde. Principles of quantum communication theory: A modern approach. arXiv preprint arXiv:2011.04672 , 2020.

Alessandro Falco was born in Cuneo, Italy, in 1998. He received the B.S. and M.S. degrees in physics from the University of Pisa in 2020 and 2022, respectively, and the Diploma di Licenza degree in physics from Scuola Normale Superiore in 2023. From 2022, he holds an associate researcher position with the Technology Innovation Institute, Abu Dhabi.

Giacomo De Palma was born in Lanciano, Italy, in 1990. He received the B.S. and M.S. degrees in physics from the University of Pisa in 2011 and 2013, respectively, and the Diploma di Licenza and Ph.D. degrees in physics from Scuola Normale Superiore in 2014 and 2016, respectively. From 2016 to 2018, he held a post-doctoral research position with the University of Copenhagen. From 2018 to 2019, he was a Marie-Sklodowska Curie Fellow with the University of Copenhagen. From March 2019 to March 2021, he was a Post-Doctoral Associate with MIT. From March 2021 to December 2021, he was a Tenure-Track Assistant Professor in mathematical physics with Scuola Normale Superiore. In December 2021, he became Associate Professor in mathematical physics with the University of Bologna, where since October 2024 he is Full Professor. He is the author of 52 scientific articles. His research interests include all aspects of quantum information and computation. He is a member of the International Association of Mathematical Physics (IAMP), of the Italian Mathematical Union (UMI) and of the Istituto Nazionale di Alta Matematica 'Francesco Severi' (INdAM). He was a recipient of the Best Italian Researcher in Denmark (BIRD) Award in 2018.