## 3D N = 1 supergravity from Virasoro TQFT: Gravitational partition function and Out-of-time-order correlator

## Arpan Bhattacharyya, a Saptaswa Ghosh, a Poulami Nandi, b Sounak Pal a

a Indian Institute of Technology, Gandhinagar, Gujarat-382055, India

b David Rittenhouse Laboratory, University of Pennsylvania, 209 South 33rd Street, Philadelphia, PA 19104, USA

```
E-mail: abhattacharyya@iitgn.ac.in , saptaswaghosh@iitgn.ac.in , pnandi@sas.upenn.edu , palsounak@iitgn.ac.in
```

Abstract: In this paper, we compute the partition functions of N = 1 SUGRA for different boundary topologies, i.e. punctured sphere and torus, using super-Virasoro TQFT. We use fusion and modular kernels of the super-Liouville theory to compute the necklace-channel conformal block and showcase formalism by proving that the inner product holds for superconformal blocks, defined as states in the Hilbert space. Finally, we compute the out-of-time-order correlator for the torus topology with superconformal primary insertions as matter using the tools of super-Virasoro TQFT and investigate its early-time behaviour.

## Contents

| 1   | Introduction                                                                              |   1 |
|-----|-------------------------------------------------------------------------------------------|-----|
| 2   | Geometric quantization and inner product of super conformal blocks                        |   5 |
| 3   | Supergravity partition function from VTQFT                                                |  11 |
| 4   | Four-point Conformal blocks on T 2                                                        |  19 |
| 5   | A brief tour to OTOC                                                                      |  22 |
|     | 5.1 OTOC in plane for super-Liouville CFT                                                 |  26 |
|     | 5.2 OTOC on even torus                                                                    |  27 |
| 6   | Conclusion and Outlook                                                                    |  31 |
| A   | Sketching the derivation of the necklace channel conformal block                          |  33 |
| B   | Definition of different functions                                                         |  39 |
| C   | Torus two-point function (Liouville CFT) with general left and right moving temper- ature |  40 |
| D   | Different transformations                                                                 |  43 |
| E   | Computation of semiclassical Liouville torus partition function                           |  44 |

## 1 Introduction

Quantum gravity has been a topic of interest for many years. However, the construction of tractable problems in quantum gravity is non-trivially challenging, with much development occurring in the lower dimensional cases [ 1-3 ] . Also, several insights came from the AdS / CFT correspondence [ 4, 5 ] . In the last few years, many studies on computing the partition function for two-dimensional gravity and its deformation have been made [ 3, 6-12 ] . However, the portrait of a richer three-dimensional gravity is still not very clear. In three spacetime dimensions, pure Einstein gravity is non-dynamical, implying the non-existence of gravitational waves. This simplifies the gravity theory dramatically and provides a hint that gravity theory in three dimensions can be formulated in terms of topological quantum field theory (TQFT) [ 13, 14 ] , where the edge modes are in the form of the graviton excitations in the asymptotic boundaries. However, full quantum treatment of three-dimensional gravity did not achieve much progress, unlike twodimensional Jackiw-Titelboim gravity [ 3 ] . Though the ensemble average description works well in the case of JT gravity , in the case of 3d gravity there are strong constraints of locality in terms of operator product expansion and modular transformations. The solution to the crossing equations in the holographic regime is rarely available to us. There have been multiple efforts of quantizing three-dimensional gravity [ 15-18 ] emerging since the late 2000s based on AdS / CFT conjecture [ 4 ] . Despite significant progress, the status of dual boundary CFT is not yet fully settled. Taking intuition from two-dimensional gravity [ 3 ] , it is expected that the boundary CFT is not just a family of 2D CFTs admitting a large-c limit but an ensemble of chaotic large-c CFTs. In spite of partial progress on this line [ 19-27 ] , there is no known unitary large-c chaotic CFT with a sparse light spectrum and Virasoro symmetry. Recently, the problem has been nicely tackled in [ 28, 29 ] showing the relation of AdS 3 quantum gravity with topological field theory, which relies on the bulk description of the problem, unlike the other conventional approaches. This opens up a new pathway to computing observables directly from the bulk description. These issues are further addressed in [ 30-32 ] 1 .

In this paper, we aim to address the quantization of N = 1 supergravity [ 34 ] via geometric quantization using super-Virasoro TQFT. The TQFT description for pure AdS 3 gravity has been studied for decades, starting from the matching at the classical level between PSL ( 2, Ρ ) × PSL ( 2, Ρ ) Chern-Simons theory Einstein's gravity in AdS 3 . However, the direct quantization PSL ( 2, Ρ ) × PSL ( 2, Ρ ) Chern-Simmons theory is not the same as quantizing pure AdS 3 gravity. The fundamental principles in gravity need the metric to be non-degenerate, while the CS theory does not have such a requirement. The gravitational phase decomposes to two copies of Teichmuller space on a spatial slice (say Σ ). Teichmuller space describes the shape of the initial value surface and becomes the universal covering of the moduli space of Riemann surfaces. For a Riemann surface Σ g , n of genus g and n punctures, the Teichmuller space T g , n can also be understood as the space of all metrics on Σ g , n modulo small diffeomorphisms and Weyl rescalings [ 35 ] ,

$$\mathcal { T } _ { g , n } = \frac { \text {Metrics on } \Sigma _ { g , n } } { \text {Diff} _ { 0 } ( \Sigma _ { g , n } ) \times \text {Weyl} ( \Sigma _ { g , n } ) } .$$

The important fact here is that the Teichmuller space can be quantized on its own, and therefore, it is possible to assign a Hilbert space H Σ having a definition of well-defined inner-product. Quantum Teichmuller theory has been an intriguing topic connecting various branches of mathematics and physics [ 13, 14, 28, 36 ] . There are many generalizations possible for the Teichmuller TQFT, especially considering moduli spaces of super Riemann surfaces. Though the super Teichmuller space plays a fundamental role in superstring perturbation theory, geometric quantization is a relatively new direction. The main goal of the paper is to generalize the technologies of geometric quantization [ 35 ] for the supersymmetric case. Sometimes it is also referred to as superTeichmuller spin TQFT [ 37, 38 ] in literature. In this paper, we compute the partition functions of different 3-manifolds. Here, the algorithm is based on surgery techniques [ 39 ] of super-Riemann surfaces [ 40 ] . It turns out that the super-Teichmuller TQFT is connected to the three-dimensional Chern-Simmons theory with complexifications of OSp ( 1 | 2 ) and SO ( 3 ) gauge groups.

1 In [ 33 ] , a simplical 3D gravity model using BCFT data has been constructed.

In the process of geometric quantization, we identified the states in the bulk Hilbert space with superconformal blocks. Conformal blocks [ 41 ] are known to be the solution of the Casimir equation for the corresponding conformal group. For N = 1 super-Liouville theory, we systematically establish the inner product of conformal blocks following [ 35 ] . The inner product turns out to produce a Dirac delta function with the difference of two different Wilson line momenta. The N = 1 super-Liouville theory has contributions from fermions leading to the choice of different spin structures in the super-Riemann surface. Depending on the different boundary conditions of the super-torus geometry, we aim to perform different modular sums, which are given in terms of the famous Eisenstein series representation. Apart from this, the spin structures using Kasteleyn orientations are known for N = 1 [ 38 ] . The isometry group OSp(1|2) acts on the upper half-plane Η 1 | 1 by general Möbius transformations of the form,

$$x \rightarrow x ^ { \prime } = \frac { a x + b + \rho \theta } { c x + d + \delta \theta } , \quad \theta \rightarrow \theta ^ { \prime } = \frac { \alpha x + \beta + g \theta } { c x + d + \delta \theta } . \\$$

We can define two types of conformal invariants, even Z and odd ζ under the general Möbius transformation. The former is the superconformal generalization of the normal cross ratio in the super upper half-plane for points Pj =( x j | θ j ) , j = 1, · · · 4:

$$Z \coloneqq \frac { X _ { 1 4 } X _ { 2 3 } } { X _ { 1 2 } X _ { 3 4 } } ,$$

where X i j : = x i -x j -θ i θ j . The other odd invariant cross ratio ζ for the collection of three points Pj =( x j | θ j ) , j = 1, · · · 3:

$$\zeta \coloneqq \pm \frac { x _ { 2 3 } \theta _ { 1 } + x _ { 3 1 } \theta _ { 2 } + x _ { 1 2 } \theta _ { 3 } - \frac { 1 } { 2 } \theta _ { 1 } \theta _ { 2 } \theta _ { 3 } } { ( X _ { 1 2 } X _ { 2 3 } X _ { 3 1 } ) ^ { 1 / 2 } } ,$$

where, x i j : = x i -x j .

The field of quantum chaos [ 42, 43 ] , developed in the early seventies, addresses the quantum manifestation of classically chaotic systems. There are many studies aiming to probe the quantum chaotic nature of quantum many-body systems [ 44-60 ] 2 . The study of quantum chaos in quantum gravity and holography has seen a renewed interest in recent years [ 52, 53, 61-72 ] 3 . The gap between the two apparently distinct fields has been bridged in [ 63, 75 ] , focusing on the 2D quantum gravity. Over the years, several diagnostics have been developed to probe quantum chaos [ 76, 77 ] . In particular, to probe the early-time (quantum) chaos, one computes the out-oftime-order correlator (OTOC) [ 63, 64, 78-82 ] 4 . One of the primary focuses of our study in this paper, is the OTOC of the form,

$$\langle \mathcal { O } _ { A } \mathcal { O } _ { B } \mathcal { O } _ { A } \mathcal { O } _ { B } \rangle _ { \beta }$$

2 This list is by no means exhaustive. Interested readers are referred to references and citations of these papers.

3 Again this list is by no means exhaustive. Interested readers are referred to this review [ 73 ] and the thesis [ 74 ] for more references.

4 Interested readers are referred to [ 83, 84 ] for more references.

on a torus. Here β is the inverse temperature. O A and O B are approximately local insertions smeared over the thermal circle. The behaviour of such functions should be contrasted with the behaviour of correlation functions of the following type,

$$\langle \mathcal { O } _ { A } ( t ) \mathcal { O } _ { A } ( t ) \mathcal { O } _ { B } \mathcal { O } _ { B } \rangle _ { \beta } , \quad \langle \mathcal { O } _ { A } \mathcal { O } _ { B } ( t ) \mathcal { O } _ { B } ( t ) \mathcal { O } _ { A } \rangle _ { \beta }$$

which tends to a O ( 1 ) value 〈 O A O A 〉 β 〈 O B O B 〉 β as t increases. All of the above four-point configurations can be obtained from the Euclidean four-point function. The difference in behaviour arises due to analytic continuation and multivaluedness of a function. OTOCs have been well studied in the literature, particularly for 2D CFTs [ 63, 85-89 ] . One can extract the quantum Lyapunov exponent from the early-time exponential decay of the OTOC and for certain holographic theories (at finite temperature), it satisfies the Maldacena-Shenker-Stanford (MSS) bound [ 64 ] . Also, by investigating the early-time exponential delay of OTOC, one can extract the information about scrambling time [ 47 ] . It is worth noting that black holes are fast scramblers, i.e scrambling time scales logarithmically in the number of degrees of freedom of the system, t Sc ∼ log N [ 90 ] . Motivated by these, in this paper, to probe the chaotic nature of the bulk gravitational theory, we compute the leading contribution to the OTOC from the superconformal matter insertions on the super-torus using the formalism of the Virasoro-TQFT . We will restrict ourselves to the largec regime in N = 1 superconformal field theory to connect with the gravitational case.

Our paper is organized as follows. In Sec. (2), we start by reviewing N = 1 super-Liouville theory, and subsequently, we describe the ingredients for computing the partition function for wormholes with different number of boundaries and topologies using super-Teichmuller TQFT. Furthermore, we discuss the process of geometric quantization for super-Liouville theory and the inner product of superconformal blocks. In Sec. (3), we calculated the (super-) VTQFT partition and the gravitational partition function by taking some specific examples of topologies. Then, in Sec. (4), we put the calculation of 4-point superconformal blocks on the torus, which is required to compute the OTOC. Finally, in Sec. (5), to probe the regime of chaos, we calculate the out-of-time-order correlation functions with super-Liouville matter insertions. To get an analytic handle on it, we calculate it using some specific but relevant limits. We use braiding and modular transformations to compute the OTOC in both channels, i.e. the necklace and the OPE channel. In Sec. (6), we conclude by summarising the main findings and giving some future outlooks. Last but not least, we have added a few appendices to give the details of some of the computations.

## Some Definition:

- Modular parameter τ is related to q as q = e 2 π i τ .
- Θ ( τ ) are Jacobi theta functions .
- χ NS are super-virasoro characters .
- ξ ( z , θ ) are super-elliptic functions .
- s T ≡ super-Teichmuller .
- ( a ) m denotes the Pochhammer symbols, ( a ) m = : Γ ( a + m ) Γ ( a ) .

## 2 Geometric quantization and inner product of super conformal blocks

In this section, we will discuss how to compute the gravitational partition function using the super-Teichmuller spin TQFT, the boundary theory being the N = 1 super-Liouville theory. The gravitational partition function is found from the character of the Osp ( 1 | 2 ) algebra. The gravitational partition function can also be given by the square of the super-Liouville partition function as shown in [ 35 ] . We claim that the inner product of the super-Liouvile zero-point conformal block on the torus is,

$$\boxed { \langle \mathcal { F } _ { ( 1 , 0 ) } ^ { s ( 0 ) } ( \vec { P } _ { 1 } ) | \mathcal { F } _ { ( 1 , 0 ) } ^ { s ( 0 ) } ( \vec { P } _ { 2 } ) \rangle = \int _ { \mathcal { T } } d ( s W P ) \, \det ( \hat { \mathcal { P } } _ { 1 } ^ { \dagger } \hat { \mathcal { P } } _ { 1 } ) ^ { 1 / 2 } \, Z _ { \text {timelike SL} } \, \mathcal { F } _ { ( 1 , 0 ) } ^ { s ( 0 ) } ( \overline { \vec { P } _ { 2 } } \, \overline { \mathcal { F } _ { ( 1 , 0 ) } ^ { s ( 0 ) } ( \vec { P } _ { 1 } ) \, \infty } \, \delta ( \vec { P } _ { 1 } - \vec { P } _ { 2 } ) . } \\$$

where, F s ( n ) ( g , n ) ( ⃗ P ) is the n -point super-conformal block for Riemann surface with g -genus and n -puncture, P denotes the Liouville momenta , sWP is called the super-Weil-Peterson volume and sdet is the super-determinant. In this section, we wish to prove our claim. However, before we get into the details of our proof, let us take a detour to briefly review the necessary concepts utilised in this section.

## A brief review of super-Liouville Theory

Let us review the basics of the N = 1 super-Liouville theory. The theory is defined via following Lagrangian density [ 91 ] ,

$$\mathcal { L } = \frac { 1 } { 2 } g _ { a b } \partial _ { a } \varphi \partial _ { b } \varphi + \frac { 1 } { 2 \pi } ( \psi \bar { \partial } \psi + \bar { \psi } \partial \bar { \psi } ) + 2 i \mu b ^ { 2 } \bar { \psi } \psi e ^ { b \varphi } + 2 \pi \mu ^ { 2 } b ^ { 2 } e ^ { 2 b \varphi } + \frac { 1 } { 2 \pi } Q R \phi \, .$$

The energy-momentum tensor and the supercurrent is given by,

$$T & = - \frac { 1 } { 2 } ( \partial \varphi \partial \varphi - Q \partial ^ { 2 } \varphi + \psi \partial \psi ) , \\ G & = i ( \psi \partial \varphi - Q \partial \psi ) \, .$$

The superconformal algebra is given by,

$$[ L _ { m } , L _ { n } ] & = ( m - n ) L _ { m + n } + \frac { c _ { S L } } { 1 2 } m ( m ^ { 2 } - 1 ) \delta _ { m + n } , \\ [ L _ { m } , G _ { k } ] & = \frac { m - 2 k } { 2 } G _ { m + k } , \\ \{ G _ { k } , G _ { l } \} & = 2 L _ { l + k } + \frac { c } { 3 } ( k ^ { 2 } - \frac { 1 } { 4 } ) \delta _ { k + l } .$$

Here the central charge is given by c SL = 3 2 + 3 Q 2 where Q = b + 1 b . k , l takes integer values for the Ramond algebra, and half-integer ones for Neveu-Schwarz (NS) algebra. Q is known as the total background charge .

For the super Liouville theory, one-point function of the vertex operator, Va = e a Φ SL with Φ SL = ϕ + θψ -¯ θ ¯ ψ , on a torus is given by [ 92 ] ,

$$\langle V _ { a } \rangle _ { \tau } = \int _ { \gamma } \frac { d P } { 4 \pi } C _ { a , Q / 2 + i P } ^ { ( L ) Q / 2 + i P } ( q \bar { q } ) ^ { - 1 / 2 4 + P ^ { 2 } } \times | F _ { L } ( \Delta _ { a } ^ { L } , \Delta _ { Q / 2 + i P } ^ { L } , q ) | ^ { 2 }$$

where the structure constant is given by,

$$C _ { a , Q / 2 + i P } ^ { ( L ) Q / 2 + i P } = ( \pi \mu \gamma ( b ^ { 2 } ) b ^ { 2 - 2 b ^ { 2 } } ) ^ { - a / b } \frac { \Upsilon _ { N S } ( b ) \Upsilon _ { N S } ( 2 a ) \Upsilon _ { N S } ( 2 i P ) \Upsilon _ { N S } ( - 2 i P ) } { \Upsilon _ { N S } ^ { 2 } ( a ) \Upsilon _ { N S } ( a + 2 i P ) \Upsilon _ { N S } ( a - 2 i P ) }$$

and F L is the conformal block. The Υ ( x ) functions are defined as,

$$\Upsilon _ { b } ( x ) & = \frac { 1 } { \Gamma _ { b } ( x ) \Gamma _ { b } ( Q - x ) } , \quad S _ { b } ( x ) = \frac { \Gamma _ { b } ( x ) } { \Gamma _ { b } ( Q - x ) } \, , \\ \Gamma _ { N S } ( x ) & = \Gamma _ { b } ( x / 2 ) \, \Gamma _ { b } ( \frac { x + Q } { 2 } ) , \quad \Gamma _ { R } ( x ) = \Gamma _ { b } ( \frac { x + b } { 2 } ) \Gamma _ { b } ( \frac { x + b ^ { - 1 } } { 2 } ) \, , \\ \Upsilon _ { N S } ( x ) & = \Upsilon _ { b } ( x / 2 ) \, \Upsilon _ { b } ( \frac { x + Q } { 2 } ) \, , \quad \Upsilon _ { R } ( x ) = \Upsilon _ { b } ( \frac { x + b } { 2 } ) \Upsilon _ { b } ( \frac { x + b ^ { - 1 } } { 2 } ) \, .$$

Using the following definition of the superfields [ 91 ] ,

$$V _ { a } \equiv \Phi _ { a } = \phi _ { a } ( z , \bar { z } ) + \theta \Lambda _ { a } ( z , \bar { z } ) - \bar { \theta } \bar { \Lambda } _ { a } ( z , \bar { z } ) \sim e ^ { a \Phi _ { S L } } \, ,$$

$$\phi _ { a } \sim e ^ { a \varphi } , & & \Lambda _ { a } \sim a e ^ { a \varphi } \psi .$$

and Φ SL = ϕ + θψ -¯ θ ¯ ψ . Now we can write the two-point and three-point functions in the following way,

$$\langle \Phi _ { 1 } ( Z _ { 1 } , \bar { Z } _ { 1 } ) \Phi _ { 2 } ( Z _ { 2 } , \bar { Z } _ { 2 } ) \rangle = \frac { c _ { 1 2 } } { Z _ { 1 2 } ^ { 2 \Delta } \bar { Z } _ { 1 2 } ^ { 2 \bar { \Delta } } } , \quad \Delta = \Delta _ { 1 } = \Delta _ { 2 } , \ \bar { \Delta } = \bar { \Delta } _ { 1 } = \bar { \Delta } _ { 2 } \, .$$

Here c 12 is a constant, and

$$\langle \Phi ( z _ { 3 } , \theta _ { 3 } ; \bar { z } _ { 3 } , \bar { \theta } _ { 3 } ) \Phi ( z _ { 2 } , \theta _ { 2 } ; \bar { z } _ { 2 } , \bar { \theta } _ { 2 } ) \Phi ( z _ { 1 } , \theta _ { 1 } ; \bar { z } _ { 1 } , \bar { \theta } _ { 1 } ) \rangle = Z _ { 3 2 } ^ { \beta _ { 1 } } Z _ { 3 1 } ^ { \beta _ { 2 } } Z _ { 2 1 } ^ { \beta _ { 3 } } \\ \langle \Phi ( \infty , 0 ; \infty , 0 ) \Phi ( 1 , \Theta ; 1 , \bar { \Theta } ) \Phi ( 0 , 0 ; 0 , 0 ) \rangle$$

where,

$$\beta _ { i } = \Delta _ { i } - \Delta _ { j } - \Delta _ { k } , \, Z _ { 1 2 } = z _ { 1 } - z _ { 2 } - \theta _ { 1 } \theta _ { 2 } , \, \Theta = \frac { 1 } { \sqrt { z _ { 1 2 } z _ { 1 3 } z _ { 2 3 } } } \left ( \theta _ { 1 } z _ { 2 3 } + \theta _ { 2 } z _ { 3 1 } + \theta _ { 3 } z _ { 1 2 } - \frac { 1 } { 2 } \theta _ { 1 } \theta _ { 2 } \theta _ { 3 } \right ) .$$

We used conformal invariance to write the three-point function (2.10).

where

## Geometric quantization in Liouville theory

Before proceeding to prove (2.1), we briefly review the geometric quantization technique in the context of the Liouville theory. To carry out the path integral over metric, we parametrize the space of metrics by g = exp ( δ v ) e 2 σ ˆ g . Here ˆ g is transversal to the orbits of Weyl ( M ) and Diff 0 ( M ) . The joint action of the reparametrizations and Weyl transformations is given by [ 93 ] ,

$$\delta g _ { m n } = ( 2 \delta \sigma + \nabla ^ { p } \delta v _ { p } ) g _ { m n } + ( \mathcal { P } _ { 1 } \delta v ) _ { m n } .$$

If the diffeomorphisms are generated by a vector field v , then

$$( \mathcal { P } _ { 1 } v ) _ { m n } = \nabla _ { m } v _ { n } + \nabla _ { n } v _ { m } - ( \nabla _ { c } v ^ { c } ) g _ { m n } \, .$$

P 1 generates symmetric and traceless variations. Deformations δ g ⊥ that are elements of Ker P † 1 (satisfying P † 1 δ g ⊥ = 0) are orthogonal to those generated by conformal transformations and Diffeomorphism.

$$\langle \delta g ^ { \perp } , \mathcal { P } _ { 1 } \vec { v } \rangle = \langle \mathcal { P } _ { 1 } ^ { \dagger } \delta g ^ { \perp } , \mathcal { P } _ { 1 } \vec { v } \rangle = 0 \, .$$

Therefore, only those that are not achieved by diffeomorphism and Weyl transformation are inside the (Range P 1 ) ⊥ . So any deformation can be decomposed into the following,

$$\left \{ \delta g _ { m n } \right \} = \left \{ \delta \sigma g _ { m n } \right \} \bigoplus \text {Range } \mathcal { P } _ { 1 } \bigoplus \text {Ker} \mathcal { P } _ { 1 } ^ { \dagger } ,$$

where the action of P † 1 on the symmetric tensors are given by,

$$( \mathcal { P } _ { 1 } ^ { \dagger } \delta g ) _ { m } = - 2 \nabla ^ { n } \delta g _ { m n } ,$$

and we have the following identification

$$( \text {Range } \mathcal { P } _ { 1 } ) ^ { \perp } = \text {Kernel} \mathcal { P } _ { 1 } ^ { \dagger } \, .$$

To determine the number of zero modes of the operators, one needs to resort to an index theorem, which gives the difference between the number of zero modes of the operator and its adjoint, expressing it in terms of a topological invariant. The index theorem reduces to the RiemannRoch theorem [ 94 ] , which says;

$$\dim ( \text {Ker} \mathcal { P } ) - \dim ( \text {Ker} \mathcal { P } ^ { \dagger } ) = 3 \chi ( M ) .$$

In the absence of the anomalies, the path integrals should reduce over the space of inequivalent metrics under the Weyl and diffeomorphism symmetries [ 93 ] . Now, we proceed to write the path integral measure using the formulas for the bosonic string theory,

$$& \left ( \frac { \det \mathcal { ^ { T } } _ { 1 } \mathcal { P } _ { 1 } } { \det ( \phi _ { j } | \phi _ { k } ) } \right ) ^ { 1 / 2 } = \left ( \frac { \det \mathcal { ^ { T } } _ { 1 } \hat { \mathcal { P } } _ { 1 } } { \det ( \langle \phi _ { j } | \hat { \phi } _ { k } \rangle ) } \right ) ^ { 1 / 2 } e ^ { - 2 6 S _ { L } ( \sigma ) } , \\ & \left ( \frac { 8 \pi ^ { 2 } \det ^ { \prime } \Delta _ { g } } { d ^ { 2 } \xi \sqrt { g } } \right ) ^ { 1 / 2 } = \left ( \frac { 8 \pi ^ { 2 } \det ^ { \prime } \Delta _ { g } } { d ^ { 2 } \xi \sqrt { \hat { g } } } \right ) ^ { 1 / 2 } e ^ { - S _ { l } ( \sigma ) } .$$

Now to compute the measure due to the change of variable from g → { σ , v , ˆ g } , we need to compute the Jacobian in the following way,

$$D g _ { m n } = V o l _ { g } ( g \delta \sigma , P _ { 1 } \delta v , f _ { j } ) \, D \sigma \, D v \, d m _ { j } \, .$$

In equation (2.19) we have used the fact,

$$\delta g ( m ) = \sum _ { j = 1 } ^ { 3 h - 3 } \delta m _ { j } \hat { f } _ { j } \, .$$

Here, the coordinates along ˆ S are δσ ˆ g , ˆ P 1 δ v and f j . Using the orthogonality, the volume can be decomposed as [ 93 ] ,

$$D g _ { m n } = V o l _ { g } ( g \delta \sigma ) V o l _ { g } ( \mathcal { P } _ { 1 } \delta v ) V o l _ { g } ( f _ { j } \perp \text {Proj.} \ K e r \mathcal { P } _ { 1 } ^ { \dagger } ) D \sigma D v d m _ { j }$$

where one can define, Vol g ( P 1 δ v ) : =( det ( P † 1 P 1 )) 1 / 2 and Vol g ( f j ⊥ Proj.Ker P † 1 ) : = det 〈 f j | φ k 〉 g ( det 〈 φ j | φ k 〉 ) 1 / 2 g . Using ultralocality, the first term can be ignored. Again,

$$\langle f _ { j } | \phi _ { k } \rangle _ { g } = \langle \hat { f } _ { j } | \phi _ { k } \rangle _ { g } = \langle \mu _ { j } | \phi _ { k } \rangle _ { g } ,$$

where, µ z j ¯ z = ˆ g z ¯ z ˆ f jz ¯ z are the Beltrami differentials [ 95 ] corresponding to the moduli deformations along the slice ˆ S . Now we proceed to write the inner product of the states in the Teichmuller space using the vierbein formalism ds 2 = e + N e -. The zweibein ( e + , e -) are respresented as

$$e ^ { + } = e ^ { \xi ( z , \bar { z } ) } | d z + \mu ( z , \bar { z } ) d \bar { z } | \ , \ \ e ^ { - } = \overline { e ^ { + } } \, .$$

Now, following [ 96 ] , we achieve the following definition of the inner product,

$$\mathcal { J } _ { ( \mathcal { F } _ { 1 , 0 } ^ { s ( 0 ) } ) } ^ { ( \mathcal { F } _ { 1 } ) } | \mathcal { F } _ { ( 0 ) } ^ { s ( 0 ) } ( \vec { P } _ { 2 } ) & = \int _ { T } d ( W P ) \, \mathcal { D } \sigma \, \mathcal { D } v ( \det ( \hat { \mathcal { P } } _ { 1 } ^ { \dagger } \hat { \mathcal { P } } _ { 1 } ) ) ^ { 1 / 2 } e ^ { ( c _ { m } - 2 6 ) S _ { l } ( \sigma ) } \overline { \mathcal { F } _ { ( 1 , 0 ) } ^ { s ( 0 ) } ( \vec { P } _ { 1 } ) } \mathcal { F } _ { ( 1 , 0 ) } ^ { s ( 0 ) } , \\ & = \int _ { T } d ( W P ) Z _ { T , L } \det ( \hat { \mathcal { P } } _ { 1 } ^ { \dagger } \hat { \mathcal { P } } _ { 1 } ) ^ { 1 / 2 } \overline { \mathcal { F } _ { ( 1 , 0 ) } ^ { s ( 0 ) } ( \vec { P } _ { 1 } ) } \mathcal { F } _ { ( 1 , 0 ) } ^ { s ( 0 ) } .$$

In the first line, we have used d ( WP ) = Q 6 h -6 j = 1 dmj det 〈 f j | φ k 〉 g ( det 〈 φ j | φ k 〉 ) 1 / 2 g .

Now we are ready to proceed to compute the inner product of the (super-)conformal blocks in the subsequent section.

## Towards the inner product of super-Liouville torus conformal blocks

With the necessary machinery at hand, we now proceed to prove our claim (2.1). Though this seems a straightforward generalization of the Liouville inner product, a few subtleties are involved here, at N = 1 super-Liouville theory. In this case, we need to consider the super-Teichmuller space, which has two types of spin structures, even and odd, according to the triangulations of the super-Riemann surface(SRS). Also, the generalization of the ghosts in the Liouville theory are Super-ghosts 5 (b,c, β , γ ). The super weil-Peterson volumes are given by [ 93 ] ,

$$d ( s W P ) = \frac { \text {det} \langle \mu _ { j } | \hat { \Phi } _ { k } \rangle } { \text {det} \langle \hat { \Phi } _ { j } | \hat { \Phi } _ { k } \rangle } \prod _ { J } d m _ { J } \, .$$

The odd(C) and even ( B ) superfields, where C = c + θγ , B = β + θ b satisfy , 6

$$\int D ( B ^ { \prime } \overline { B ^ { \prime } } C \overline { C ^ { \prime } } ) e ^ { - I _ { s g h ( C , B ^ { \prime } ) } } = ( \text {det} ( P _ { 1 } ^ { \dagger } P _ { 1 } ) ) ^ { 1 / 2 } .$$

Hence the, inner product in the super-Teichmuller can be written as 7 ,

$$\langle \mathcal { F } _ { ( 1 , 0 ) } ^ { s ( 0 ) } ( \vec { P } _ { 1 } ) | \mathcal { F } _ { ( 1 , 0 ) } ^ { s ( 0 ) } ( \vec { P } _ { 2 } ) \rangle = \int _ { \mathcal { T } } d ( s W P ) \, \text {det} ( \hat { \mathcal { P } } _ { 1 } ^ { \dagger } ) ^ { 1 / 2 } Z _ { \text {timelike SL} } \mathcal { F } _ { ( 1 , 0 ) } ^ { s ( 0 ) } ( \vec { P } _ { 2 } ) \overline { \mathcal { F } _ { ( 1 , 0 ) } ^ { s ( 0 ) } ( \vec { P } _ { 1 } ) } , \quad ( 2 . 2 6 )$$

which proves the claim that we have done in (2.1).

Now, let us calculate the inner product explicitly to show the orthogonality of the superconformal blocks on the super-torus. To proceed further and compute the action on the torus we define the super-coordinates Z =( z , θ ) along with the super-derivatives as,

$$D _ { \alpha } = \partial _ { \theta } + \theta \partial z , & & D _ { \bar { \alpha } } = \partial _ { \bar { \theta } } - \bar { \theta } \partial \bar { z } .$$

Before going to the details of the inner product, the first task is to compute the torus partition function in super-Liouville theory. We consider the super-Liouville action with an even spin structure. In principle, the partition function can be computed perturbatively in the cosmological constant µ . But we know that the VTQFT formalism works for Liouville theories with central charge c L ≥ 1 [ 28, 29 ] . For simplicity, in our case, we take the large charge limit (and we do not expand in µ ), i.e. c SL →∞ (semiclassical limit) and correspondingly, the semiclassical partition function reduces to ( free bosonic ) ⊗ ( free fermionic ) partition function along with some prefactor depending on the cosmological constant µ . It can be shown that in this limit, µ acts as an regulator for the zero mode integral. An explicit derivation of the claim for the Liouville theory is given in Appendix (E). The same extends to super-Liouville straightforwardly.

5 One also uses the convention of ρ , σ ghosts. The ρ ghost cancels the contribution of two pair of twisted fermions in N = 4 supersymmetric theory and σ cancels the contribution of pair of bosonic oscillator [ 27 ] .

6 Note that, The ghost superfields can have different definitions in different gauges (Wess-Zumino supergauge).

7 The super-Virasoro character function is given by [ 97 ] ,

$$\chi _ { H . C } ( q ) = \prod _ { n = 0 } ^ { \infty } \frac { 1 + q ^ { n + 1 / 2 } } { 1 - q ^ { n + 1 } } \, .$$

For type-A contraction of the superalgebra, the character is trivial and χ F ( q ) = 1.

In the large charge limit the action reduces to [ 91 ] ,

$$S _ { s l } & = \int _ { s T } d ^ { 2 } z d ^ { 2 } \theta D _ { \alpha } S _ { 1 } D _ { \bar { \alpha } } \Phi _ { S L } \\ & = \int _ { s T } d ^ { 2 } z d ^ { 2 } \theta \left ( \bar { \psi } \psi + \bar { \theta } \psi \bar { \partial } \varphi - \bar { \theta } \theta \psi \bar { \partial } \psi - \theta \bar { \psi } \partial \varphi - \theta \bar { \theta } \partial \varphi \bar { \partial } \varphi + \theta \bar { \theta } \psi \partial \bar { \psi } \right ) , \\ & = \int _ { T } d ^ { 2 } z \left ( \partial \varphi \bar { \partial } \varphi + \psi \bar { \partial } \psi + \bar { \psi } \partial \bar { \psi } \right ) .$$

Now d 2 θ = d ¯ θ d θ ; The super-Liouville partition function on super-Torus is given by,

$$Now & \text { } \sigma \text { } \sigma \text { } \sigma \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } Z _ { \text {sl} _ { \text {even} } } = \int [ \mathcal { D } \varphi \mathcal { D } \psi \bar { \mathcal { D } } \bar { \psi } ] e ^ { - S _ { \bar { \ell } } } \, , \\ & = Z _ { \text {Bosonic} } \text { } \times Z _ { \text {Fermionic} } \, , \\ & = \det ( \nabla ^ { 2 } ) ^ { - 1 / 2 } \times P f ( \partial ) P f ( \bar { \partial } ) \, , \\ & = \frac { 1 } { \sqrt { \tau } _ { 2 } | \eta ( \tau ) | ^ { 2 } } \left ( \left | \frac { \Theta _ { 3 } ( z = 0 | \tau ) } { \eta ( \tau ) } \right | + \left | \frac { \Theta _ { 4 } ( z = 0 | \tau ) } { \eta ( \tau ) } \right | + \left | \frac { \Theta _ { 2 } ( z = 0 | \tau ) } { \eta ( \tau ) } \right | \right ) . \\ \text {The } Z _ { \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text$$

The Z sl even turns out to be modular invariant as it is a product of the free bosonic and fermionic modular invariant partition functions on the torus. The Pffafian ( P f ( A )) is defined as,

$$P f ( A ) = \sqrt { \det A } .$$

Therefore the inner product defined in (2.26) becomes,

$$\langle \mathcal { F } _ { ( 1 , 0 ) } ^ { s ( 0 ) } ( \vec { P } _ { 1 } ) | \mathcal { F } _ { ( 1 , 0 ) } ^ { s ( 0 ) } ( \vec { P } _ { 2 } ) \rangle = \int _ { \mathcal { T } } d ( s W P ) \, \ s d e t _ { ( 1 , n = 0 ) } ( \hat { \mathcal { P } } _ { 1 } ^ { \dagger } \hat { \mathcal { P } } _ { 1 } ) ^ { 1 / 2 } \, Z _ { \text {timelike} \, s l } \, \mathcal { F } _ { ( 1 , 0 ) } ^ { s ( 0 ) } ( \overline { \hat { P } } _ { ( 1 , 0 ) } \overline { \mathcal { F } } _ { ( 1 , 0 ) } ^ { s ( 0 ) } ( \vec { P } _ { 1 } ) } \quad ( 2 . 3 1 )$$

where, d ( sWP ) = d 4 τ Y , Y = Im ( z ) + θ ¯ θ 2 and sdet ( 1, n = 0 ) ( ˆ P † 1 ˆ P 1 ) 1 / 2 = | η ( τ ) | 6 Θ 2 [ a , b ]( 0, τ ) [ 98 ] 8 .

For the odd-spin structure, it turns out to be more subtle. In this case the odd modular parameter also contributes to the fermionic partition function as shown in (3.31). The superconformal blocks on the torus are just zero-point super-Virasoro characters. For simplicity, we will discuss the evenspin sector. As the super-Virasoro conformal block on torus are super-Virasoro characters [ 91 ] , these are given by,

$$\mathcal { F } _ { 1 , 0 } ^ { s ( 0 ) } = \chi _ { \text {even} } = \sqrt { \frac { \Theta [ a , b ] ( 0 , \tau ) } { \eta ( \tau ) } } \frac { q ^ { p ^ { 2 } } } { \eta ( \tau ) } \, .$$

Before going further, let us take a moment to remind the reader of the definition of the Theta and Dedekind's eta functions. Few modular properties of theta functions are given in Appendix (B) of

8 Wecan think that we are working with "Non-critical strings". Then, we can identify Z Τ 2 super-ghost = sdet ( 1, n = 0 ) ( ˆ P † 1 ˆ P 1 ) 1 / 2 expressions of which follows from [ 93 ] .

Table 1 : Table of a few super-characters corresponding to different boundary conditions in the Neveu-Schwarz and Ramond sectors. The "PP"(Periodic-Periodic) structure is called the 'odd', and the other three types are called 'even' spin structures.

| AA   | Tr NS q L 0 - c / 24           | r Θ 3 ( τ ) η ( τ )   |
|------|--------------------------------|-----------------------|
| AP   | Tr NS ( - 1 ) F q L 0 - c / 24 | r Θ 4 ( τ ) η ( τ )   |
| PA   | Tr R q L 0 - c / 24            | r Θ 2 ( τ ) η ( τ )   |
| PP   | Tr R ( - 1 ) F q L 0 - c / 24  | r Θ 1 ( τ ) η ( τ )   |

[ 99 ] .

$$\Theta _ { 2 } ( \tau ) & = 2 q ^ { 1 / 8 } \prod _ { n = 1 } ^ { \infty } ( 1 - q ^ { n } ) ( 1 + q ^ { n } ) ^ { 2 } , \\ \Theta _ { 3 } ( \tau ) & = \prod _ { n = 1 } ^ { \infty } ( 1 - q ^ { n } ) ( 1 + q ^ { n - 1 / 2 } ) ^ { 2 } , \\ \Theta _ { 4 } ( \tau ) & = \prod _ { n = 1 } ^ { \infty } ( 1 - q ^ { n } ) ( 1 - q ^ { n - 1 / 2 } ) ^ { 2 } . \\ \intertext { o n s h a v e s p l i m e s t r o m a t i o n p e r t i o n }$$

Above theta functions have simple transformation properties under the action of the modular group. The Dedekind's eta ( η ) function is defined to be [ 100 ] 9 ,

$$\eta ( \tau ) = q ^ { 1 / 2 4 } \prod _ { n = 1 } ^ { \infty } \left ( 1 - q ^ { n } \right ) .$$

After computing the intgeral in (2.31), we get the inner product to be proportional to the delta function. For P 1 , P 2 ≥ 0, the inner-product of conformal blocks turns out to be,

$$\langle \mathcal { F } _ { ( 1 , 0 ) } ^ { s ( 0 ) } ( \vec { P } _ { 1 } ) | \mathcal { F } _ { ( 1 , 0 ) } ^ { s ( 0 ) } ( \vec { P } _ { 2 } ) \rangle \in \mathcal { N } \, \delta ( \vec { P } _ { 1 } - \vec { P } _ { 2 } )$$

where, N is the divergent constant.

## 3 Supergravity partition function from VTQFT

We begin this section by interpreting the connection between partition function of the superLiouville theory and that of the supergravity, thereby extending the proposal of [ 28 ] , i.e equating

9 A few known Θ [ a , b ]( z , τ ) is defined as follows.

$$\Theta [ a , b ] ( z , \tau ) = \sum _ { n } e ^ { i \pi [ ( n + a ) ^ { 2 } \tau + 2 ( n + a ) ( z + b ) ] } \\$$

along with some additional definitions

$$\Theta _ { 1 } = \Theta [ 1 / 2 , 1 / 2 ] , \ \Theta _ { 2 } = \Theta [ 1 / 2 , 0 ] , \ \Theta _ { 3 } = \Theta [ 0 , 0 ] , \ \Theta _ { 4 } = \Theta [ 0 , 1 / 2 ] .$$

· NS , NS , R sector are the even torus boundary conditions and e R is the odd torus boundary condition.

the gravity partition function on a manifold with a fixed topology to the Virasoro TQFT partition function, to the case of N = 1 super-Liouville theory with super-Teichmuller geometric quantization. We propose that,

$$Z _ { s u g r a } ( M ) = \frac { 1 } { | \Map ( M , \partial M ) | } \sum _ { \gamma \in \Map ( \partial M ) } | Z _ { s u p e r V i r } ( M ^ { \gamma } ) | ^ { 2 }$$

which can also be expressed alternatively as 10 ,

$$Z _ { s u g r a } ( M ) = \frac { 1 } { | \Map { _ { 0 } ( M , \partial M ) } | } \sum _ { \gamma \in \frac { \Map { _ { 0 } ( M , \partial M ) } } { \Map { _ { 0 } ( M , \partial M ) } } } | Z _ { \text {superVir} } ( M ^ { \gamma } ) | ^ { 2 } .$$

The LHS of (3.1) can be thought as sum over different topologies. The simplest one is the Σ g , n × Ι . We take the the subclass, Σ { 0,1 } , n × Ι . Also in (3.1), the Map ( M , ∂ M ) and Map ( ∂ M ) are the bulk and boundary mapping class group respectively [ 28 ] . The large diffeomorphisms in a gravity theory are not gauge transformations from the TQFT side. Hence we coset the set of all diffeomorphisms by small diffeomorphisms denoted by Diff 0 ( M , ∂ M ) [ 101 ] . These are described by the mapping class groups

$$\text {Map} ( M , \partial M ) \equiv \frac { \text {Diff} ( M , \partial M ) } { \text {Diff} _ { 0 } ( M , \partial M ) } , \quad \text {Map} ( \partial M ) \equiv \frac { \text {Diff} ( \partial M ) } { \text {Diff} _ { 0 } ( \partial M ) } .$$

The mapping class group prevents the theory of quantum gravity from following basic axioms in QFT, e.g. factorization in amplitudes. Also, the part of the bulk mapping class group that acts trivially on the boundary is given by,

$$\text {Map} _ { 0 } ( M , \partial M ) = \frac { \text {Map} ( M , \partial M ) } { \text {Ker} ( \text {Map} ( M , \partial M ) \to \text {Map} ( \partial M ) ) } .$$

## For two boundary wormholes with genus zero

We begin to test our claim (3.1) with a warm-up exercise considering the case of two boundary wormholes before moving on to the more complicated examples. We calculate the partition function of the simplest topology i.e a wormhole ( g = 0) with two boundary three-punctured sphere ( n = 3 ) . Assuming the spheres are at the boundary and Wilson lines are non-spinning, we get from the inner product of conformal blocks, Hence,

<!-- image -->

Figure 1 : Figure depicting the four three punctured sphere wormholes in super-Liouville theory with non-spinning Liouvile momenta. The figure on the right side shows the Heegard splitting.

<!-- image -->

$$Z _ { s u g r a } = | Z _ { s u p e r v i r } | ^ { 2 } = \frac { 1 } { | C _ { N S } ( i \hat { P } _ { i } , i \hat { P } _ { j } , i \hat { P } _ { k } ) | ^ { 2 } } \, .$$

As argued in [ 28 ] , for the general case (i.e for arbitrary g and n ) we define,

$$\langle \mathcal { F } _ { g , n } ^ { s \, \mathcal { C } } ( \vec { P } _ { 1 } ) | \mathcal { F } _ { g , n } ^ { s \, \mathcal { C } } ( \vec { P } _ { 2 } ) \rangle = \frac { \delta ^ { 3 g - 3 + n } ( \vec { P } _ { 1 } - \vec { P } _ { 2 } ) } { \rho _ { g , n } ^ { s \, \mathcal { C } } ( \vec { P } _ { 1 } ) } \, .$$

Here, the channel C is specified by cutting the Riemann surface into 2 g -2 + n pairs of pants sewn together along 3 g -3 + n specific internal cuffs. In particular extending [ 28 ] for supersymmetric case we have,

$$\rho _ { g , n } ^ { s \, \mathcal { C } } ( \vec { P } ) = \prod _ { \text {cuffs a} } \Omega _ { 0 \, s } ( P _ { a } ) \prod _ { \text {pairs of pants} } C _ { N S } ( P _ { i } , P _ { j } , P _ { k } ) ,$$

where Ω 0 s ( α a ) 11 is defined to be,

$$\Omega _ { 0 \, s } ( \alpha _ { a } ) = \frac { W _ { N S } ( \alpha _ { a } ) } { W _ { N S } ( Q - \alpha _ { a } ) } ,$$

where WNS has been defined in Appendix (B).

11 α a = Q / 2 + i P a .

## Four boundary genus zero wormhole

For a four-boundary wormhole, to find the gravitational partition function after Heegard splitting into the basis of compression bodies ( M 1and M 2 in Fig. (1)), we need to use the super-Virasoro fusion kernel to convert the s channel block to t channel block. We use the three-point superblock for the three punctured spheres, which is similar to the DOZZ structure constant in Liouville theory apart from a little modification [ 102 ] . The four-boundary super-Virasoro sphere wormhole partition function can be written as,

<!-- image -->

In evaluating the above, we used the Ponsot-Teschner fusion kernel [ 103 ] , which expands t -channel block { t } in terms of the complete basis of s -channel block { s } . The SLFT fusion kernel is given in Appendix (C). The main advantage of using such a formula is even without knowing the { s } or { t } channel conformal blocks, we can use the closed form of the fusion kernel to obtain the OPE density, which is one of the important ingredients to calculate / check quantities, e.g. partition function, ETH [ 104-106 ] .

## Gravity partition function of a torus

Usually, the partition function for torus is written in the following way as the sum of the vacuum characters [ 107 ] .

$$z _ { \text {Torus} } \left ( \begin{pmatrix} \text {Torus} \\ \text {T} \end{pmatrix} \right ) = \chi _ { 0 } ( q ) , \text { with } \chi _ { 0 } ( q ) = ( 1 - q ) \frac { q ^ { - \frac { c - 1 } { 2 4 } } } { \eta ( q ) } .$$

Hence the gravity partition function of the torus is given by,

$$Z _ { \text {gravity} } ^ { \text {torus} } = \sum _ { \gamma \in P S L ( 2 , \mathbb { Z } ) } | \chi _ { 0 } ( \gamma \cdot \tau ) | ^ { 2 }$$

The sum is given by a divergent Poincare series and can be written as,

$$Z _ { \text {gravity} } ^ { \text {torus} } ( \tau ) = \frac { 1 } { \sqrt { \text {Im} ( \tau ) } | \eta ( \tau ) | ^ { 2 } } \sum _ { c , d } \left ( \sqrt { \text {Im} ( \tau ) } \, | \bar { q } q | ^ { - c + 1 / 2 4 } | 1 - q | ^ { 2 } \right ) \Big | _ { \gamma } \, .$$

Now, this Poincare series can be written as the special case of Eisenstein series,

$$E ( \tau ; n , m ) = \sum _ { c , d } \left ( \sqrt { I m ( \tau ) } \, q ^ { - n } \bar { q } ^ { - m } \right ) \Big | _ { \gamma } ,$$

with n -m becoming 0 or ± 1. Using the modular weight of modular forms properly the final result in terms of the Eisenstein Series can be written as 12 ,

$$Z _ { \text {gravity} } ^ { \text {torus} } ( \tau ) = \frac { 1 } { \sqrt { I m ^ { 2 } \tau } | \eta ( \tau ) | ^ { 2 } } \left ( E ( 2 k - 1 / 1 2 , 0 ) + E ( 2 k + 2 - 1 / 1 2 , 0 ) - E ( 2 k + 1 - 1 / 1 2 , 1 ) - E ( 2 k + 1 - 1 / 1 2 , - 1 ) \right ) .$$

Now the non-degenerate and the degenerate primary characters transforms under modular Stransformation as [ 107 ] 13 ,

$$\chi _ { P } \left ( - \, \frac { 1 } { \tau } \right ) = \int _ { 0 } ^ { \infty } d P ^ { \prime } S _ { P } ^ { p ^ { \prime } } \chi _ { p ^ { \prime } } , \ \chi _ { m , n } \left ( - \, \frac { 1 } { \tau } \right ) = \int _ { 0 } ^ { \infty } d p ^ { \prime } S _ { m , n } ^ { p ^ { \prime } } \chi _ { P ^ { \prime } } .$$

with S P ′ m , n = 2 π 2sinh ( π mP ′ b -1 ) sinh ( π nP ′ b ) and S P ′ P = π 2cos ( π PP ′ ) . Now the cardy density of states for Liouville CFT has the asymptotic form given by,

$$\rho ( P , \bar { P } ) = \mathbb { S } _ { P _ { 1 } } [ 1 ] \mathbb { S } _ { \bar { P } _ { 1 } } [ 1 ] + \sum _ { i } \mathbb { S } _ { P P _ { i } } [ 1 ] \mathbb { S } _ { \bar { P } \bar { P } _ { i } } [ 1 ] ,$$

where Σ P 1 [ 1 ] is the modular S-matrix. Asymptotic spectrum of the CFT is quite generally given by 14 ,

$$\rho _ { 0 } ( P ) = \mathbb { S } _ { P 1 } [ 1 ] = 4 \sqrt { 2 } \sinh ( 2 \pi b P ) \sinh ( 2 \pi b ^ { - 1 } P ) .$$

Considering analytic continuation of the Liouville OPE for α/ ∈ [ 0, Q ] , we can obtain the following representation of fusion,

$$\mathcal { V } _ { \alpha _ { A } } \times \mathcal { V } _ { \alpha _ { B } } \colon = \sum _ { \substack { \alpha _ { n } , m < Q / 2 \\ n , m \in \mathbb { Z } _ { \geq 0 } } } \mathcal { V } _ { \alpha _ { n , m } } + \int _ { Q / 2 + 0 } ^ { Q / 2 + i \infty } d \alpha \mathcal { V } _ { \alpha } ,$$

where V α is a primary with associated conformal dimension ∆ = α ( Q -α ) . In calculating OTOC we consider α &gt; Q / 2, so we only have the contribution from the integral.

12 One can find the regularized sum for these divergent series in [ 15, 108 ] .

14 with ρ ( P ) ∼ ρ 0 ( P ) ρ 0 ( ¯ P ) as P , ¯ P →∞ .

13 The vacuum character is the degenerate primary χ vac = χ 1,1 .

## SUGRA partition function of a even torus

By continuing the same argument, the super Virasoro partition function takes the form (2.35),

$$Z _ { \text {superVir} } ^ { \text {torus} } = \chi _ { \text {even} } ( \tau ) = \sqrt { \frac { \Theta _ { i } ( 0 , \tau ) } { \eta ( \tau ) } } \frac { q ^ { p ^ { 2 } } } { \eta ( \tau ) } , \, \forall i = 2 , 3 , 4 ,$$

Correspondingly, the supergravity partition function is given by,

$$Z _ { s u g r a } ^ { \text {torus} } = \sum _ { \gamma } | \chi _ { \text {even} } ( \gamma \cdot \tau ) | ^ { 2 } .$$

Having all these ingredients in hand, we proceed to calculate the partition function for different subdominant topologies.

## Calculation of partition function Torus Wormhole:

After calculating the partition function of multiboundary sphere wormholes, we now proceed to calculate the partition function of the two boundary wormholes on the super-torus. The computation of the partition function is similar to the Liouville case, and the modular sum is the same as the usual (non-supersymmetric) Liouville theory. The main reason behind this is that for the even spin structure, superspace generalisation of the torus does not contain the Im ( τ ) factor or any other extra modular parameter to change the modular sum. The modular sum changes substantially when we consider the odd-spin structure on the super-torus.

Even spin structure: The two boundary torus wormhole partition function is given by,

$$Z _ { \text {super-Liouville} } ^ { \text {torus} } = \frac { 1 } { \sqrt { - i ( \tau - \bar { \tau } ) } | \eta ( \tau ) | ^ { 2 } } \times \left ( \left | \frac { \Theta _ { 3 } ( z = 0 | \tau ) } { \eta ( \tau ) } \right | + \left | \frac { \Theta _ { 4 } ( z = 0 | \tau ) } { \eta ( \tau ) } \right | + \left | \frac { \Theta _ { 2 } ( z = 0 | \tau ) } { \eta ( \tau ) } \right | \right ) .$$

̸

The Θ functions appearing in (3.22) are chosen according to the boundary conditions mentioned in Table (1). Now replacing τ → τ 1 and -¯ τ → γ · τ 2 , where the usual modular transformation γ · τ = a τ + b c τ + d , with ad -bc = 0, the gravity partition function is written as,

$$Z _ { s u g r a } ( T ^ { 2 } \times [ 0 , 1 ] ) = \left ( \bigcup _ { \Sigma _ { 8 } , \cdot } \Im ( \bigcup _ { \tau _ { 1 } } \Im ( \bigcup _ { \tau _ { 2 } } \Im ( \tau _ { 1 } ) Z _ { \text {superVir} } ^ { \text {torus-wormhole} } ( \tau _ { 1 } ) Z _ { \text {superVir} } ^ { \text {torus-wormhole} } ( \tau _ { 2 } ) \sum _ { \gamma } \frac { \sqrt { \text {Im} ( \tau _ { 1 } ) \text {Im} ( \gamma \cdot \tau _ { 2 } ) } } { | \tau _ { 1 } + \gamma \cdot \tau _ { 2 } | } \, .$$

However, it should be noted that there exists an issue with the calculated partition function in N = 1 super-Liouville theory with the modular sum, which is similar to [ 35 ] . For the gravitino field, there is at least one cycle around which the gravitino changes sign due to the boundary condition and in such cases, there are no zero modes.

At this point, we note that while computing the inner product between different conformal blocks of the same spin structure but with different boundary conditions in different cycles of the torus, one should, in principle, introduce the element of spin mapping class group ( U ( γ ) ) sandwiched between the states of the Hilbert space i.e the superconformal blocks, schematically, 〈 F ( ⃗ P 1 ) | U ( γ )) | F ( ⃗ P 2 ) 〉 . While the odd spin structure cannot be obtained from an even one by applying a S (modular S transform) or T (T-transform) move, the inner product is ambiguous between even and odd spin structures as one can not construct the mapping torus because of the absence of suitable spin mapping class group action, U ( γ ) , between them. 15 Hence, at this point, it is quite unclear to us how to define the super-Virasoro partition function for this. We leave this for detailed future investigation. Now, the action of the spin mapping class group changes the boundary condition (within an even / odd spin structure) from one to the other depending on the action of the S or T moves, as shown in [ 38 ] . Hence the 'mapping torus' has a fundamental group,

$$\pi _ { 1 } ( M ) = \pi _ { 1 } ( \Sigma ) \rtimes _ { \phi _ { * } } \mathbb { Z } ,$$

where φ ∗ : π 1 ( Σ ) → π 1 ( Σ ) is the induced map from φ ∈ Aut ( Σ ) . Here M is the 3-manifold with spin-2 manifolds ( Σ ) on the boundary. Now to compute the gravity partition function one should in principle sum over the spin mapping class group. In general the representation of the spin mapping class group ( U ( γ ) ) will not be proportional to identity e.g. for the case of two boundary torus ( Τ 2 ) with the even spin structure at the two boundary but with different boundary conditions. But in this paper, we have chosen the same spin structure on Σ with the same boundary condition; hence for our case, U ( γ ) is always identity. We leave a more general study of the partition function of two boundary torus with the same (even) spin structure but different boundary conditions for the future.

Odd torus-Wormhole partition function: For the odd spin structure, we identify the points,

$$( z , \theta ) \sim ( z + 1 , \theta ) ; & & ( z , \theta ) \sim ( z + \tau + \theta \delta , \theta + \delta ) \, .$$

Clearly, due to this, a function (for odd spin structure) ξ ( z , θ ) satisfies

$$\xi ( z , \theta ) & = \xi ( z + \tau + \theta \delta , \theta + \delta ) \, , \\ \xi ( z , \theta ) & = \xi ( z + 1 , \theta ) \, .$$

Physically, the odd( δ ) and the even ( τ ) are the modular periods of ( θ , z ) correspond to zero modes for gravitino and the graviton (these constant modes cannot be gauged). These type of functions in (3.26) are also known as 'Superelliptic' functions. To obtain the partition function 16 ,

15 Mapping torus is obtained for a Σ × S 1 topology as,

$$M . T ( \Sigma \times S ^ { 1 } ) = ( \Sigma \times S ^ { 1 } ) _ { [ \phi ] } \colon = ( \Sigma \times [ 0 , 1 ] ) / \sim ,$$

where the equivalence class ∼ is given by, ( x , 0 ) ∼ ( φ ( x ) , 1 ) for x ∈ Σ and φ ∈ Aut ( Σ ) .

16 Generally the partition function for the odd sector is 0, if one does not consider the coupling of ψ and ¯ ψ .

we have the following action as [ 109 ] ,

$$A ^ { \prime } = \frac { g } { 2 \pi } \int _ { \tau } d ^ { 2 } \omega \left [ \partial _ { \omega } \varphi _ { 1 } \partial _ { \bar { \omega } } \varphi _ { 1 } + \bar { \psi } _ { 1 } \partial _ { \bar { \omega } } \bar { \psi } _ { 1 } - \psi _ { 1 } \partial _ { \bar { \omega } } \psi _ { 1 } + \frac { \delta \bar { \delta } } { 2 \tau _ { I } ^ { 2 } } \bar { \psi } _ { 1 } \psi _ { 1 } - F _ { 1 } ^ { 2 } - \frac { i \delta } { \tau _ { I } } \psi _ { 1 } \partial _ { \omega } \varphi _ { 1 } - \frac { i \bar { \delta } } { \tau _ { I } } \bar { \psi } _ { 1 } \partial _ { \bar { \omega } } \varphi _ { 1 } \\ + g \frac { \delta \bar { \delta } } { 4 \pi \tau _ { I } } \bar { \psi } _ { 0 } \psi _ { 0 } - \frac { g \tau _ { I } F _ { 0 } ^ { 2 } } { 2 \pi } \right ] .$$

Here the new coordinates W =( ω , ˆ θ ) is related with Z =( z , θ ) in the following way,

$$z = \omega + \hat { \theta } \delta \frac { \omega _ { I } } { \tau _ { I } } , \ \theta = \hat { \theta } + \delta \frac { \omega _ { I } } { \tau _ { I } } \, .$$

ω I and τ I denotes the imaginary part of ω , τ . The action (3.27) comes from the expansion of

$$A ^ { \prime } = \frac { g } { 2 \pi } \int _ { s \mathcal { T } } d ^ { 4 } z D _ { \theta } J D _ { \bar { \theta } } J$$

with

$$J ( W , \bar { W } ) = \phi ( \omega , \bar { \omega } ) + \hat { \theta } \psi ( \omega , \bar { \omega } ) - \bar { \hat { \theta } } \bar { \psi } ( \omega , \bar { \omega } ) + \bar { \hat { \theta } } \hat { \theta } F ( \omega , \bar { \omega } ) \, .$$

The auxiliary field F can be removed by using the equation of motion. The total partition function is given by [ 109 ] ,

$$Z _ { s _ { o d d } } = \int \mathcal { D } \varphi _ { 1 } e ^ { - A _ { \varphi _ { 1 } } } \, \int \mathcal { D } S _ { 0 } \, \mathcal { D } [ \psi _ { 1 } , \bar { \psi } _ { 1 } ] e ^ { - A _ { r } } = Z _ { 0 } \cdot Z _ { 1 } ,$$

$$Z _ { 0 } = \left ( \frac { g } { 2 \tau _ { I } } \right ) ^ { 1 / 2 } \frac { 1 } { | \eta ( \tau ) | ^ { 2 } } \ , \quad Z _ { 1 } = \frac { \bar { \delta } \delta } { \tau _ { I } } | \eta ( \tau ) | ^ { 2 } ,$$

where, D S 0 = CdF 0 d ψ 0 d ¯ ψ 0 and Ar = A ′ -A Φ 1 . Z 0 comes from the contribution of zero modes of action, and Z 1 comes from the path integral over Φ 1 . In odd super-torus, the modular transformation works as,

$$\tau ^ { \prime } = \frac { a \tau + b } { c \tau + d } , \quad \delta ^ { \prime } = \frac { \delta } { ( c \tau + d ) ^ { 3 / 2 } } ,$$

where τ , δ belongs to the super-torus and a b c d ∈ SL ( 2, Ζ ) . The modular sum (which gives the gravitational partition function) vanishes as the partition function is trivially zero (as the odd R-R sector super-Virasoro character trivially vanishes for decoupled ψ and ¯ ψ ), though we have a non vanishing super-Liouville partition function Zsl odd given by the product of Z 0 and Z 1 in (3.32) due

where, to the coupling of ψ and ¯ ψ via odd modular parameter in zero modes. Hence in the odd sector the supergravity partition function becomes ,

$$Z _ { s u g r a } ^ { o d d } ( T ^ { 2 } \times [ 0 , 1 ] ) = \sum _ { \gamma ^ { \prime } \in \frac { \delta } { ( c + d ) ^ { 3 / 2 } } } \left | Z _ { \text {superVir} } ^ { o d d } ( \gamma \cdot \tau , \gamma ^ { \prime } \cdot \delta ) \right | ^ { 2 } .$$

We will leave performing the modular sum and its extensions for future work. For this case, the boundary conditions are periodic in both cycles of the torus. Hence the gravitino field does not change its sign, and therefore, there are zero modes appearing in theory. Due to this, the laplacian operator does not yield an inverse. This is one of the important subtleties involved in the "PP" boundary condition. So, we perform the calculation where the fermionic mode is at least antiperiodic in one of the cycles of the torus (i.e. for an even spin structure), leaving the complete analysis for the odd spin case for future studies.

In this section we focused on the computation of partition function. Now, a natural question arises: What are the gravitational descriptions of higher point functions? The answer to this question is a bit tricky. The direct answer is that, although there is a general holographic correspondence between 3D gravity and 2D CFT working for ensemble averages of large charge CFTs, they reproduce the gravitational counterparts in very few cases. For the Gaussian ensemble, it reproduces the gravitational result upto two boundary wormholes [ 31 ] . However, for wormholes with more than two boundaries, non-gaussianities [ 110 ] are important, and Gaussian contractions lead to wrong results. Partial progress has been made by considering non-gaussian contractions to reproduce the gravitational counterparts in [ 31 ] . In VTQFT formalism, one can define states in super-Virasoro CFT as four punctured torus surfaces, and one can calculate the gravitational counterpart by squaring and performing the modular sum. Generally, the one-punctured torus wormholes correspond to carving out a solid tori from the interior and glueing along the inner torus boundary. These types of wormholes are called Maldacena-Maoz wormholes [ 111 ] . Furthermore, one can think of the higher point functions as conical defects propagating in the bulk of such a wormhole.

In our paper, we focus on calculating the fount-point OTOC on torus (leading geometry), taking resort of (super-) VTQFT braiding transformations . One can calculate the contribution to the OTOC in the bulk silde coming from the torus-wormhole, by taking the inner-product of four-point conformal blocks on torus. In the next section we present the details of the computation of OTOC.

## 4 Four-point Conformal blocks on T 2

In this section, we proceed to evaluate the torus ( T 2 ) four-point block in the large-charge ( c →∞ ) regime. One way to evaluate this is to use the monodromy method for super-torus using superWard identities. However, we use the procedure mentioned in [ 112 ] to calculate the large charge conformal blocks using the recursive approach. The calculated conformal blocks are Necklace channel conformal blocks. We showcase the formalism to calculate the OPE channel blocks from the necklace channel blocks using some basic fusion and modular transformations. To begin with, we first review what is the torus one-point function in this approach in Liouville CFT .

## NS Vertex operators

Super-descendants Φ∆ , ¯ ∆ ( ξ , ¯ ξ | Z , ¯ Z ) of the super-primary field Φ∆ , ¯ ∆ ( Z , ¯ Z ) = Φ∆ , ¯ ∆ ( ν , ¯ ν | Z , ¯ Z ) are given by the following relation,

$$\Phi _ { \Delta , \bar { \Delta } } ( L _ { - m } \xi , \bar { \xi } | Z , \bar { Z } ) & = \oint \frac { d W } { 2 \pi i } ( W - Z ) ^ { 1 - m } T ( W ) \Phi _ { \Delta , \bar { \Delta } } ( \xi , \bar { \xi } | Z , \bar { Z } ) \quad m \in \mathbb { N } , \\ \Phi _ { \Delta , \bar { \Delta } - k } ( G _ { - k } \bar { \xi } , \bar { \xi } | Z , \bar { Z } ) & = \oint \frac { d W } { 2 \pi i } ( W - Z ) ^ { 1 / 2 - k } T ( W ) \Phi _ { \Delta , \bar { \Delta } } ( \xi , \bar { \xi } | Z , \bar { Z } ) \quad k \in N - 1 / 2 .$$

Few conformal ward identities can be found in [ 113, 114 ] .

## Liouville Torus one-point function:

The torus one-point function φλ , ¯ λ with the modular parameter τ can be casted as [ 113 ] ,

$$\langle \phi _ { \lambda , \bar { \lambda } } \rangle = ( q \bar { q } ) ^ { - c / 2 } \sum _ { \Delta , \bar { \Delta } } \sum _ { f , \bar { f } \in \frac { 1 } { 2 } \cup \{ 0 \} } q ^ { \Delta + f } \bar { q } ^ { \bar { \Delta } + \bar { f } } \sum _ { \bar { f } = | M | + | K | = | N | + | L | } [ B _ { \Delta } ^ { f } ] ^ { M K , N L } [ B _ { \bar { \Delta } } ^ { \bar { f } } ] ^ { \bar { M } , \bar { N } , \bar { L } } \\ \times \langle \langle \Delta | _ { M K } \otimes ( \bar { \Delta } | _ { \bar { M } \bar { K } } | \phi _ { \lambda , \bar { \lambda } } ( 1 , 1 ) | \Delta ) _ { N L } \otimes | \bar { \Delta } \rangle _ { \bar { N } L } \rangle \\$$

where q = exp ( 2 π i τ ) and the sum runs over the whole supermodule of the Neveu-schwarz(NS) sector. The matrices [ B f ∆ ] MK , NL , [ B f ¯ ∆ ] ¯ M ¯ K , ¯ N ¯ L are the inverse of the Gram matrices, and they are given by,

$$[ B _ { \Delta } ^ { f } ] _ { M K , N L } = \langle \langle \Delta | _ { M K } \Big | | \Delta \rangle _ { N L } \rangle , \quad [ B _ { \bar { \Delta } } ^ { \bar { f } } ] _ { \bar { M } \bar { K } , \bar { N } \bar { L } } = \langle \langle \bar { \Delta } | _ { \bar { M } \bar { K } } \Big | | \bar { \Delta } \rangle _ { \bar { N } \bar { L } } \rangle$$

calculated in the standard NS sector. Apart from this, we have,

$$| \Delta \rangle _ { M K } = L _ { - M } G _ { - K } | \Delta \rangle = L _ { - m _ { j } } \cdots L _ { - m _ { 1 } } G _ { - k _ { i } } \cdots G _ { - k _ { 1 } } | \Delta \rangle$$

where k i &gt; · · · &gt; k 1 and k s ∈ Ν -1 / 2 alongwith mj ≥··· ≥ m 1 , mr ∈ Ν . For K , L and ¯ K , ¯ L having the same parity one has,

$$\langle \langle \Delta | _ { M K } \bigotimes \langle \bar { \Delta } | _ { \bar { M } \bar { K } } \Big | \phi _ { \lambda , \bar { \lambda } } ( 1 , 1 ) | \Delta \rangle _ { N L } \bigotimes | \bar { \Delta } \rangle _ { \bar { N } \bar { L } } \rangle = \rho _ { N N } ( \Delta _ { M K } , \Delta _ { \lambda } , \Delta _ { N L } ) \rho _ { N N } ( \bar { \Delta } _ { \bar { M } \bar { K } } , \bar { \Delta } _ { \bar { \lambda } } , \bar { \Delta } _ { \bar { N } \bar { L } } ) C _ { \Delta , \bar { \Delta } } ^ { \lambda , \bar { \lambda } } ,$$

where the quantity C λ , ¯ λ ∆ , ¯ ∆ is the primary three-point structure constants. The quantity ρ can be computed by taking the product of fusion polynomials. 17

17 Fusion polynomials are written as

$$P ^ { r s } \begin{bmatrix} \Delta _ { 2 } \\ \Delta _ { 1 } \end{bmatrix} = \mathcal { X } _ { e } ^ { r s } ( \lambda _ { 1 } + \lambda _ { 2 } ) \mathcal { X } _ { e } ^ { r s } ( \lambda _ { 1 } - \lambda _ { 2 } ) \, ,$$

In the next subsection, we move on to the computation of the torus four-point conformal block, which is relevant for computing the OTOC [ 63, 85 ] .

## Super-Liouville four-point function on torus:

Now, we proceed to compute the torus four-point block in s -channel. The t -channel block can be computed by using the fusion kernel method or by taking the OPE directly in the different channels. Then, we will show how to achieve the global blocks in the c →∞ limit. Recalling that 〈 ˜ ∆ m | φ k ( z k ) | ˜ ∆ l 〉 = C ˜ ∆ m ∆ k ˜ ∆ l z ˜ ∆ m -∆ k -˜ ∆ l k are the structure constants, we write the four point function for super-Liouville theory as,

$$& \langle \Phi _ { 1 } ( Z _ { 1 } , \bar { Z } _ { 1 } ) \Phi _ { 2 } ( Z _ { 2 } , \bar { Z } _ { 2 } ) \Phi _ { 3 } ( Z _ { 3 } , \bar { Z } _ { 3 } ) \Phi _ { 4 } ( Z _ { 4 } , \bar { Z } _ { 4 } ) \rangle _ { \tau } \\ & = \sum _ { \tilde { \Delta } _ { 1 } , \tilde { \Delta } _ { 2 } , \tilde { \Delta } _ { 4 } , \tilde { \Delta } _ { 5 } , \tilde { \Delta } _ { 6 } } C _ { \tilde { \Delta } _ { 1 } \tilde { \Delta } _ { 2 } \tilde { \Delta } _ { 4 } \tilde { \Delta } _ { 2 } \tilde { \Delta } _ { 3 } \tilde { \Delta } _ { 3 } \tilde { \Delta } _ { 4 } \tilde { \Delta } _ { 4 } \tilde { \Delta } _ { 4 } \tilde { \Delta } _ { 1 } } \rangle _ { \tau } \\ & \times Z _ { 1 } ^ { \tilde { \Delta } _ { 1 } \tilde { \Delta } _ { 1 } - \tilde { \Delta } _ { 2 } \tilde { Z } _ { 2 } ^ { 2 } - \tilde { \Delta } _ { 2 } - \tilde { \Delta } _ { 3 } \tilde { Z } _ { 3 } ^ { 3 } - \tilde { \Delta } _ { 3 } \tilde { Z } _ { 4 } ^ { 4 } \tilde { Z } _ { 4 } ^ { 4 } - \tilde { \Delta } _ { 1 } \tilde { C } _ { c } } [ \mathcal { F } _ { c } ^ { \{ \delta } \Delta _ { 1 , 2 , 3 , 4 } \hat { \Delta } _ { 1 , 2 , 3 , 4 } ^ { 2 , 3 , 4 } ] \times ( \text {anti-homorphism} ) \\$$

where the necklace-channel conformal block is denoted by F { s } and the expression is given by,

$$\text {where the neclack-channel conformal block is denoted by } \mathcal { F } ^ { ( s ) } & = \int _ { \mathcal { C } } ^ { 2 } \sum _ { \substack { m , r , m = 0 \\ & \quad \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \$$

We will be mainly focusing on the calculation of the Out-of-time-order (OTO) four-point function, which has a form of 〈 O A O B O A O B 〉 . We will set the conformal dimensions of the two primaries (super-Virasoro) inserted on the time circle in the torus to be equal while calculating the timeordered (TO) super-Liouville four-point function. We can write the conformal block structure in the TO four-point function on the torus as, (defining x = z 2 / z 1 )

$$\mathcal { F } _ { \langle \Phi _ { 1 } ( z _ { 1 } , \bar { z } _ { 1 } ) \Phi _ { 1 } ( z _ { 2 } , \bar { z } _ { 2 } ) \Phi _ { 3 } ( z _ { 3 } , \bar { z } _ { 3 } ) \Phi _ { 3 } ( z _ { 4 } , \bar { z } _ { 4 } ) \rangle _ { \tau } } = \mathcal { A } _ { c } ^ { \Delta _ { 1 , 2 , 2 } \tilde { \Delta } _ { 1 , 2 , 3 , 4 } } ( z _ { 1 , 2 , 3 , 4 } ) + q ^ { 1 / 2 } \mathcal { B } _ { c } ^ { \Delta _ { 1 , 2 , 3 , 4 } \tilde { \Delta } _ { 1 , 2 , 3 , 4 } } ( z _ { 1 , 2 , 3 , 4 } ) + \mathcal { O } ( q ) + \cdots .$$

Here A c and B c are given in (A.2) and (A.3) respectively. In the next section, we use the fourpoint function given in (4.4) to compute the OTOC using suitable transformation and analyze its early-time behaviour.

with

$$\mathcal { X } _ { e } ^ { r s } ( \lambda ) = \prod _ { p = 1 - r } ^ { r - 1 } \prod _ { q = 1 - s } ^ { s - 1 } ( \frac { \lambda - p b - q b ^ { - 1 } } { 2 \sqrt { 2 } } )$$

and the products run over p 1 -r 2 k , q 1 -s 2 l , k l ∈ 2 Ν S { 0 } .

$$\mathcal { X } _ { e } ^ { r s } ( \lambda ) = \prod _ { p = 1 - r q = 1 - s } \prod _ { ( \frac { \lambda - p b - q b ^ { - 1 } } { 2 \sqrt { 2 } } ) } ( \frac { \lambda - p b - q b ^ { - 1 } } { 2 \sqrt { 2 } } ) \\ \intertext { o n v e r p = 1 - r + 2 k , \quad } q = 1 - s + 2 l , \quad k + l \in 2 N \bigcup \{ 0 \} .$$

## 5 A brief tour to OTOC

The out-of-time-order correlator (OTOC) is a probe for early-time chaos. The OTOC is defined as the inner product between two states A ( t ) B | 0 〉 β and BA ( t ) | 0 〉 β where the operators A and B are separated in space by x and in Lorentzian time by t at the inverse temperature β . The definition of the normalised OTOC is given by ,

$$\mathcal { C } _ { \beta } ( x , t ) \colon = \frac { \langle B ^ { \dagger } A ^ { \dagger } ( t ) B A ( t ) \rangle _ { \beta } } { \sqrt { \langle B ^ { \dagger } A ^ { \dagger } ( t ) B ( t ) A \rangle _ { \beta } \langle A ^ { \dagger } ( t ) B ^ { \dagger } B A ( t ) \rangle _ { \beta } } } \, .$$

To compute the OTOC, we do the analytic continuation of the following TO correlator, 〈 B † ( z 1 , ¯ z 1 ) B ( z 2 , ¯ z 2 ) A † ( z 3 , ¯ z 3 ) A ( z 4 , ¯ z 4 ) 〉 β , so that the operator ordering becomes 〈 B † A † ( t ) BA ( t ) 〉 β .

This can be obtained by the following choice of coordinates on the thermal cylinder as [ 63 ] ,

$$z _ { 1 } & = e ^ { \frac { 2 \pi } { \beta } ( t + i \epsilon _ { 1 } ) } , & \bar { z } _ { 1 } & = e ^ { - \frac { 2 \pi } { \beta } ( t + i \epsilon _ { 1 } ) } , \\ z _ { 2 } & = e ^ { \frac { 2 \pi } { \beta } ( t + i \epsilon _ { 2 } ) } , & \bar { z } _ { 2 } & = e ^ { - \frac { 2 \pi } { \beta } ( t + i \epsilon _ { 1 } ) } , \\ z _ { 3 } & = e ^ { \frac { 2 \pi } { \beta } ( x + i \epsilon _ { 3 } ) } , & \bar { z } _ { 3 } & = e ^ { + \frac { 2 \pi } { \beta } ( x - i \epsilon _ { 3 } ) } , \\ z _ { 4 } & = e ^ { \frac { 2 \pi } { \beta } ( x + i \epsilon _ { 4 } ) } , & \bar { z } _ { 4 } & = e ^ { \frac { 2 \pi } { \beta } ( x - i \epsilon _ { 4 } ) }$$

where we analytically continued the correlator to the real-time considering ε 1 &lt;ε 3 &lt;ε 2 &lt;ε 4 .

At late times, the OTOC is exponentially damped for truly chaotic systems, and it may decay polynomically for non-chaotic models. The time evolution of the cross-ratio z is given by ( 1 -z ) → ( 1 -z ) e -2 π i , which means, in turn, that the late time behaviour of the OTOC is given by the corresponding Regge limit of the correlator.

In this case, the cross-ratio on the complex plane is given by,

$$z \approx e ^ { \frac { - 2 \pi } { \beta } ( x - t ) } \epsilon _ { 1 2 } ^ { * } \epsilon _ { 3 4 } \, , & & \bar { z } \approx - e ^ { \frac { - 2 \pi } { \beta } ( x + t ) } \epsilon _ { 1 2 } ^ { * } \epsilon _ { 3 4 } \, ,$$

where we use the abbreviation,

$$\epsilon _ { i j } = i \left ( e ^ { \frac { 2 \pi } { \beta } i \epsilon _ { i } } - e ^ { \frac { 2 \pi } { \beta } i \epsilon _ { j } } \right ) .$$

Now, one needs to pick the monodromy around the branch cut in z ∼ [ 1, ∞ ) .

Furthermore, we will use the following limits of fusion kernel to find the OTOC for our case.

$$\mathbb { F } _ { P _ { 3 } , P _ { t } } \left [ \begin{matrix} P _ { 3 } & P _ { 2 } \\ 1 & P _ { 1 } \end{matrix} \right ] & = \delta ( P _ { 1 } - P _ { t } ) \ , \\ \mathbb { F } _ { 1 , P _ { t } } \left [ \begin{matrix} P _ { 3 } & P _ { 2 } \\ P _ { 3 } & P _ { 2 } \end{matrix} \right ] & = C _ { N S } ( P _ { 2 } , P _ { 3 } , P _ { t } ) \, \frac { W _ { N S } ( \alpha _ { t } ) } { W _ { N S } ( Q - \alpha _ { t } ) } \ , \\ \mathbb { S } _ { 1 , P } [ 1 ] & = W _ { N S } ( \alpha ) W _ { N S } ( Q - \alpha ) \ .$$

In case of finding the OTOC on the torus one needs to remember that there are two cycles in this specific topology. One is called the spatial circle, and the other one is called the time circle. We are interested in finding this probe of chaos (OTOC) for super-Liouville matter insertions. For calculating the Out-of-time-order correlator in this case, we need to perform an R-transformation on the time-ordered four-point function. Pictorially this can be described as [ 82 ] 18 ,

$$\begin{array} { r l } { - } & { O _ { B } } & { = \int d \alpha _ { s } \mathbb { R } _ { \alpha _ { s } \alpha _ { \iota } } ^ { ( s ) \gamma , \epsilon } \begin{bmatrix} \alpha _ { B } & \alpha _ { A } \\ \alpha _ { \psi } & \alpha _ { \psi ^ { \prime } } \end{bmatrix} \frac { \psi ^ { \prime } } { \psi _ { s } } - O _ { A } } \\ { - } & { O _ { A } } & { = O _ { B } } \end{array}$$

In the above equation, Ρ matrix is related to the fusion matrix in the following fashion for Virasoro respresentation as 19 [ 113 ] ,

$$\mathbb { R } _ { \alpha _ { s } \alpha _ { t } } \begin{bmatrix} \alpha _ { 3 } & \alpha _ { 2 } \\ \alpha _ { 4 } & \alpha _ { 1 } \end{bmatrix} = e ^ { 2 \pi i ( \Delta _ { 2 } + \Delta _ { 4 } - \Delta _ { s } - \Delta _ { t } ) } \mathbb { F } _ { \alpha _ { s } \alpha _ { t } } \begin{bmatrix} \alpha _ { 3 } & \alpha _ { 2 } \\ \alpha _ { 4 } & \alpha _ { 1 } \end{bmatrix} .$$

The Φ -matrix can be written in terms of quantum 6j symbols via,

$$\mathbb { F } _ { \alpha _ { s } \alpha _ { t } } \begin{bmatrix} \alpha _ { 3 } & \alpha _ { 2 } \\ \alpha _ { 4 } & \alpha _ { 1 } \end{bmatrix} = | S _ { b } ( 2 \alpha _ { t } ) S _ { b } ( 2 \alpha _ { s } ) | \sqrt { \frac { C ( \alpha _ { 4 } , \alpha _ { t } , \alpha _ { 1 } ) C ( \bar { \alpha } _ { t } , \alpha _ { 3 } , \alpha _ { 2 } ) } { C ( \alpha _ { 3 } , \alpha _ { 4 } , \alpha _ { s } ) C ( \bar { \alpha } _ { s } , \alpha _ { 2 } , \alpha _ { 1 } ) } } \begin{cases} \alpha _ { 1 } & \alpha _ { 2 } & \alpha _ { s } \\ \alpha _ { 3 } & \alpha _ { 4 } & \alpha _ { t } \end{cases} \right \} _ { b }$$

where S b denotes the double sine function , α j = Q 2 + i bk j |{z} P j and C ( α 1 , α 2 , α s ) are the usual DOZZ

coefficients in the Liouville theory. The 6j symbols can be found in [ 115 ] . The generalization to the super-Liouville case is quite straightforward.

The necklace channel braiding ( Ρ ) matrix is given by,

$$\mathbb { R } _ { \alpha , \alpha _ { t } } ^ { \gamma , \epsilon } \begin{bmatrix} \alpha _ { 3 } & \alpha _ { 2 } \\ \alpha _ { 4 } & \alpha _ { 1 } \end{bmatrix} = e ^ { \pi i \epsilon ( \Delta _ { 4 } + \Delta _ { 1 } - \Delta _ { s } - \Delta _ { 1 } ) } \mathbb { R } _ { \alpha , \alpha _ { t } } ^ { \gamma } \begin{bmatrix} \alpha _ { 3 } & \alpha _ { 2 } \\ \alpha _ { 4 } & \alpha _ { 1 } \end{bmatrix} \quad \gamma = ( e , o ) \quad \epsilon = \text {sign} ( \text {Arg} z _ { 3 } - \text {Arg} z _ { 2 } )$$

where,

$$\mathbb { R } _ { \alpha _ { s } a _ { t } } ^ { \gamma } \begin{bmatrix} \alpha _ { 3 } & \alpha _ { 2 } \\ \alpha _ { 4 } & \alpha _ { 1 } \end{bmatrix} = M _ { \alpha _ { s } , \alpha _ { t } } ^ { \gamma } \begin{bmatrix} \alpha _ { 3 } & \alpha _ { 2 } \\ \alpha _ { 4 } & \alpha _ { 1 } \end{bmatrix} \frac { \Gamma _ { N S } ( 2 \alpha _ { s } ) \Gamma _ { N S } ( 2 Q - 2 \alpha _ { s } ) } { 4 \Gamma _ { N S } ( Q - 2 \alpha _ { t } ) \Gamma _ { N S } ( 2 \alpha _ { t } - Q ) } \int _ { - i \infty } ^ { i \infty } \frac { d \tau } { i } J _ { \alpha , \alpha _ { t } } ^ { \gamma }$$

18 Comment : We should remember that if we set ∆ ψ = 0, we are no longer allowing four-point insertion. In this case, the four-point block will be reduced to a three-point necklace channel block. This is one of the main differences with the OPE channel block.

19 Few basic moves are described pictorially in Appendix (D).

with,

$$M _ { \alpha , \alpha _ { t } } ^ { e } \begin{bmatrix} \alpha _ { 3 } \ \alpha _ { 2 } \\ \alpha _ { 4 } \ \alpha _ { 1 } \end{bmatrix} = & \frac { 4 | \sigma | _ { \Gamma _ { t } ( \alpha _ { t } + \alpha _ { 4 } - \alpha _ { 2 } ) _ { \Gamma _ { t } ( \bar { \alpha } _ { t } + \alpha _ { 4 } - \alpha _ { 2 } ) _ { \Gamma _ { t } ( \bar { \alpha } _ { t } + \bar { \alpha } _ { 4 } - \alpha _ { 2 } ) } ) } { 4 | \eta | _ { \Gamma _ { s } ( \alpha _ { 4 } + \alpha _ { 3 } - \alpha _ { 3 } ) _ { \Gamma _ { \eta } ( \bar { \alpha } _ { s } + \alpha _ { 4 } - \alpha _ { 3 } ) _ { \Gamma _ { \eta } ( \alpha _ { s } + \bar { \alpha } _ { 4 } - \alpha _ { 3 } ) _ { \Gamma _ { \eta } ( \bar { \alpha } _ { s } + \bar { \alpha } _ { 4 } - \alpha _ { 3 } ) } } } \\ & \times \frac { \Gamma _ { \sigma } ( \alpha _ { t } + \alpha _ { 1 } - \alpha _ { 3 } ) _ { \Gamma _ { \sigma } ( \bar { \alpha } _ { t } + \alpha _ { 1 } - \alpha _ { 3 } ) _ { \Gamma _ { \sigma } ( \alpha _ { t } + \bar { \alpha } _ { 1 } - \alpha _ { 3 } ) _ { \Gamma _ { \sigma } ( \bar { \alpha } _ { t } + \bar { \alpha } _ { 1 } - \alpha _ { 3 } ) } } { \Gamma _ { \eta } ( \alpha _ { s } + \alpha _ { 1 } - \alpha _ { 2 } ) _ { \Gamma _ { \eta } ( \bar { \alpha } _ { s } + \alpha _ { 1 } - \alpha _ { 2 } ) _ { \Gamma _ { \eta } ( \alpha _ { s } + \bar { \alpha } _ { 1 } - \alpha _ { 2 } ) _ { \Gamma _ { \eta } ( \bar { \alpha } _ { s } + \bar { \alpha } _ { 1 } - \alpha _ { 2 } ) } } } \\ \end{bmatrix}$$

and for the even structure, the J( τ ) matrix is given by [ 116 ] ,

$$J ^ { e } ( \tau ) = \left ( \begin{array} { c c c } \left [ \begin{matrix} N & N & N & N \\ N & N & N & N \\ N & N & N & N \\ \end{matrix} \right ] + \left [ \begin{matrix} R & R & R & R \\ R & R & R & R \\ i & \frac { 1 } { i } & \left [ \begin{matrix} N & N & N & N \\ R & R & N & N \\ N & N & R & N \\ \end{matrix} \right ] + i \left [ \begin{matrix} R & R & R & R \\ N & N & R & N \\ N & N & R & R \\ \end{matrix} \right ] \right ) \\ J ^ { e } ( \tau ) = \left ( \begin{array} { c c c } \left [ \begin{matrix} N & N & N & N \\ \frac { 1 } { i } & \left [ \begin{matrix} N & N & N & N \\ N & N & R & R \\ \end{matrix} \right ] + i \left [ \begin{matrix} R & R & R & R \\ R & R & N & N \\ N & N & R & R \\ \end{matrix} \right ] - \left [ \begin{matrix} N & N & N & N \\ R & R & R & R \\ N & N & N & N \\ \end{matrix} \right ] - \left [ \begin{matrix} R & R & R & R \\ N & N & R & N \\ N & N & R & R \\ \end{matrix} \right ] \right )$$

where we use the abbreviations,

$$\begin{bmatrix} N & N & N & N \\ N & N & N & N \end{bmatrix} = \frac { S _ { N S } ( \bar { \alpha } _ { 4 } - \alpha _ { 3 } + \alpha _ { 2 } + \tau ) S _ { N S } ( \alpha _ { 1 } + \tau ) S _ { N S } ( \alpha _ { 4 } - \alpha _ { 3 } + \alpha _ { 2 } + \tau ) S _ { N S } ( \bar { \alpha } _ { 1 } + \tau ) } { S _ { N S } ( \bar { \alpha } _ { 3 } + \bar { \alpha } _ { t } + \tau ) S _ { N S } ( \bar { \alpha } _ { 3 } + \alpha _ { t } + \tau ) S _ { N S } ( \alpha _ { s } + \alpha _ { 2 } + \tau ) S _ { N S } ( \bar { \alpha } _ { s } + \alpha _ { 2 } + \tau ) } \quad ( 5 . 1 1 )$$

similarly,

$$\begin{bmatrix} N & R & N & R \\ N & N & N & N \end{bmatrix} = \frac { S _ { N S } ( \bar { \alpha } _ { 4 } - \alpha _ { 3 } + \alpha _ { 2 } + \tau ) S _ { R } ( \alpha _ { 1 } + \tau ) S _ { N S } ( \alpha _ { 4 } - \alpha _ { 3 } + \alpha _ { 2 } + \tau ) S _ { R } ( \bar { \alpha } _ { 1 } + \tau ) } { S _ { N S } ( \bar { \alpha } _ { 3 } + \bar { \alpha } _ { t } + \tau ) S _ { N S } ( \bar { \alpha } _ { 3 } + \alpha _ { t } + \tau ) S _ { N S } ( \alpha _ { s } + \alpha _ { 2 } + \tau ) S _ { N S } ( \bar { \alpha } _ { s } + \alpha _ { 2 } + \tau ) } .$$

Here, ¯ α i = Q -α i . Again ,

$$\lim _ { \alpha _ { 1 } \to 0 } \mathbb { R } _ { \alpha _ { s } \alpha _ { t } } ^ { e } \left [ \alpha _ { 3 } ^ { \ } \alpha _ { 2 } \right ] _ { \lambda } ^ { e } = \delta ( \alpha _ { s } - \alpha _ { 2 } ) \delta _ { \lambda } ^ { e } \delta ( P _ { t } - P _ { 3 } ) \, .$$

Before computing the exact form of the integral, we wish to extract the asymptotic behaviour of the 4-point necklace channel conformal block and see how it depends on the cross-ratio and the conformal dimension ∆ s , which can easily be done using the shadow formalism [ 117-119 ] .

## Torus blocks: Shadow formalism

To calculate the OTOC in super-Liouville field theory on the torus one should compute the asymptotic behaviour of the necklace channel conformal block precisely [ 120 ] . This computation will mainly help to fix the nature of OTOC with time. We show that as there is a connection between comb channel conformal blocks and necklace channel conformal blocks, we can extract the n -point necklace channel conformal block from the n + 2-point comb channel conformal block [ 120 ] .

$$\mathcal { F } _ { N } ^ { ( n ) } ( q , z | \Delta , \tilde { \Delta } , \Delta _ { \alpha } ) = \sum _ { m = 0 } ^ { \infty } \frac { q ^ { m + \Delta _ { a } } A _ { m } ^ { ( n + 2 ) } ( z | \Delta , \tilde { \Delta } , \Delta _ { \alpha } ) } { m ! ( 2 \Delta _ { \alpha } ) _ { m } } ,$$

where,

$$A _ { m } ^ { ( n + 2 ) } ( z | \Delta , \tilde { \Delta } , \Delta _ { \alpha } ) = \lim _ { \substack { z _ { 0 } \to 0 \\ z _ { n + 1 } \to 0 } } \partial _ { 0 } ^ { m } \partial _ { n + 1 } ^ { m } \left ( z _ { 0 } ^ { - 2 \Delta _ { \alpha } } \mathcal { G } _ { n + 2 } ( 1 / z _ { 0 } , z , z _ { n + 1 } | \Delta , \tilde { \Delta } , \Delta _ { \alpha } ) \right ) .$$

In (5.14), G n + 2 denotes the n + 2-point comb channel conformal block. We denote the external dimensions as ( ∆ , ∆ 1 · · · ∆ n ) and the internal dimensions as ( ˜ ∆ 0 , ˜ ∆ 1 · · · ˜ ∆ n -2 ) . In general, the computation of 6-point comb channel blocks yields the following compact form,

$$\mathcal { G } _ { \bar { \Delta } _ { 1 } , \bar { \Delta } _ { 2 } , \bar { \Delta } _ { 3 } } ^ { \Delta _ { 1 } , \cdots , \Delta _ { 6 } } ( z _ { 0 } , z _ { n + 1 } ) = \mathcal { L } ^ { ( \Delta _ { 1 } , \cdots , \Delta _ { 4 } ) } ( z _ { 0 } , \cdots , z _ { 4 } ) \, \chi _ { 0 } ^ { \bar { \Delta } _ { 1 } } \chi _ { 1 } ^ { \bar { \Delta } _ { 2 } } \mathbf F _ { K } \left [ \, - \mathcal { S } _ { 1 } \, \quad \tilde { \Delta } _ { 0 } + \tilde { \Delta } _ { 1 } - \Delta _ { 2 } \, \quad \tilde { \Delta } _ { 1 } + \tilde { \Delta } _ { 2 } - \Delta _ { 3 } \, \ - \mathcal { S } _ { 2 } \, \right ] ( \chi _ { 0 } , \chi _ { 1 } , \chi _ { 2 } )$$

where the leg-factor can be casted in a compact form as,

$$\mathcal { L } ^ { ( \Delta _ { 1 } , \cdots \Delta _ { 4 } ) } ( z _ { 0 } , \cdots , z _ { 4 } ) = \left ( \frac { z _ { 1 2 } z _ { 3 4 } } { z _ { 0 1 } z _ { 0 2 } z _ { 4 5 } z _ { 3 5 } } \right ) ^ { \Delta _ { a } } \prod _ { i = 0 } ^ { 3 } ( \frac { z _ { i , i + 2 } } { z _ { i , i + 1 } z _ { i + 1 , i + 2 } } ) ^ { \Delta _ { i + 1 } }$$

and the comb function is given by,

$$F _ { K } \begin{bmatrix} a _ { 1 } , \, b _ { 1 } , \cdots b _ { k - 1 } , \, a _ { 2 } \end{bmatrix} ( x _ { 1 } , \cdots x _ { k } ) = \sum _ { n _ { 1 } , \cdots , n _ { k } = 0 } ^ { \infty } \frac { ( a _ { 1 } ) _ { n _ { 1 } } ( b _ { 1 } ) _ { n _ { 1 } + n _ { 2 } } ( b _ { 2 } ) _ { n _ { 2 } + n _ { 3 } } \cdots ( b _ { k - 1 } ) _ { n _ { k - 1 } + n _ { k } } ( a _ { 2 } ) _ { n _ { k } } } { ( c _ { 1 } ) _ { n _ { 1 } } \cdots ( c _ { k } ) _ { n _ { k } } } \frac { x _ { 1 } ^ { n _ { 1 } } } { n _ { 1 } ! } \cdots \frac { x _ { k } ^ { n _ { k } } } { n _ { k } ! } .$$

In (5.15), we define the cross-ratios as,

$$\chi _ { 0 } = \frac { z _ { 0 1 } z _ { 2 3 } } { z _ { 0 2 } z _ { 1 3 } } ; \quad \chi _ { 1 } = \frac { z _ { 1 2 } z _ { 3 4 } } { z _ { 1 3 } z _ { 2 4 } } ; \quad \chi _ { 2 } = \frac { z _ { 2 3 } z _ { 4 5 } } { z _ { 2 4 } z _ { 3 5 } }$$

and we also have used the short notation of ∆ i j = ∆ i -∆ j . FK denotes the comb function. Its properties and few identitites are defined in [ 120 ] . In (5.15) we define,

$$\mathcal { S } _ { 1 } = \Delta _ { 1 } - \Delta _ { \alpha } - \tilde { \Delta } _ { 0 } , & & \mathcal { S } _ { 2 } = \Delta _ { 4 } - \Delta _ { \alpha } - \tilde { \Delta } _ { 2 } \, .$$

Nowthe quantity A ( 6 ) m ( z | ∆ , ˜ ∆ , ∆ α ) which is related to the 4-point necklace channel block becomes,

$$A _ { m } ^ { ( 6 ) } ( z | \Delta , \tilde { \Delta } , \Delta _ { \alpha } ) & = \lim _ { z _ { 0 } \to 0 } ( \Delta _ { 1 } - \Delta _ { \alpha } - n _ { 1 } ) _ { m } ( 1 - z _ { 0 } ) ^ { - \Delta _ { \alpha } + \Delta _ { 1 } - m n _ { 1 } } ( - \Delta _ { 4 } - \Delta _ { \alpha } + n _ { 3 } ) _ { m } ( \chi _ { 1 } - z _ { 5 } ) ^ { - \Delta _ { \alpha } } \Delta _ { 4 } - m + n _ { 3 } \, \times \, \Xi ( \rho ) \, , \\ & = ( \Delta _ { 1 } - \Delta _ { \alpha } - n _ { 1 } ) _ { m } ( - \Delta _ { 4 } - \Delta _ { \alpha } + n _ { 3 } ) _ { m } ( \chi _ { 1 } ) ^ { - \Delta _ { \alpha } - \Delta _ { 4 } + m + n _ { 3 } } \, \Xi ( \rho ) \, . \\$$

Here, ρ denotes the other insertion points except z 0 and z 5 . Ξ ( ρ ) refers to the part of the correlation function independent of the cross-ratio. We need mainly the dependence on the cross ratio in leading behaviour to find the out-of-time-order correlator. We will use this in Sec. (5.2).

## 5.1 OTOC in plane for super-Liouville CFT

In superplane the super-Liouville four point function can be written as [ 121-124 ] ,

$$\langle \Phi _ { 1 } \Phi _ { 2 } \Phi _ { 3 } \Phi _ { 4 } \rangle \colon = Y ( a + b _ { 1 } W _ { 2 3 4 } + b _ { 4 } W _ { 1 2 3 } + c V ) ,$$

where

$$Y = \prod _ { i < j } ( z _ { i j } ) ^ { \Delta / 3 - \Delta _ { i } - \Delta _ { j } } , \quad W _ { i j k } \colon = \frac { \theta _ { i } z _ { j k } - \theta _ { j } z _ { i k } + \theta _ { k } z _ { i j } + \theta _ { i } \theta _ { j } \theta _ { k } } { \sqrt { z _ { i j } z _ { i k } z _ { j k } } } ,$$

$$V \colon = \frac { \theta _ { 1 } \theta _ { 2 } z _ { 3 4 } } { z _ { 1 3 } z _ { 2 4 } } + \frac { \theta _ { 3 } \theta _ { 4 } z _ { 1 2 } } { z _ { 1 3 } z _ { 2 4 } } + \frac { \theta _ { 1 } \theta _ { 4 } z _ { 2 3 } } { z _ { 1 3 } z _ { 2 4 } } + \frac { \theta _ { 2 } \theta _ { 3 } z _ { 1 4 } } { z _ { 1 3 } z _ { 2 4 } } - \frac { \theta _ { 1 } \theta _ { 3 } } { z _ { 1 3 } } - \frac { \theta _ { 2 } \theta _ { 4 } } { z _ { 2 4 } } + 3 \frac { \theta _ { 1 } \theta _ { 2 } \theta _ { 3 } \theta _ { 4 } } { z _ { 1 3 } z _ { 2 4 } } , \quad \Delta = \sum _ { i } \Delta _ { i } ,$$

and a , b 1 , b 4 and c are functions of cross ratio. The leading behaviour of the 4-point comb channel conformal block (each of a , b 1 , b 4 , c ) has the following form for our case as [ 125 ] ,

$$\mathcal { V } _ { c } ^ { \Delta _ { 1 , 2 , 3 , 4 } , \tilde { \Delta } _ { 1 , 2 , 3 , 4 } } \sim \chi _ { 1 } ^ { \alpha _ { s } ( Q - \alpha _ { s } ) } .$$

Now, to compute the OTOC we need to compute the following integral as given in (5.6) 20 ,

$$\text {OTOC} = \mathcal { F } _ { r } \int _ { Q / 2 } ^ { Q / 2 + i \infty } d \alpha , s ^ { \pi i \epsilon ( \tilde { \Delta } _ { 2 } + \tilde { \Delta } _ { 4 } - \Delta _ { s } \cdot \Delta _ { t } ) } \frac { W _ { N S } ( Q ) W _ { N S } ( \alpha _ { s } ) } { \pi W _ { N S } ( Q - \alpha _ { A } ) W _ { N S } ( Q - \alpha _ { B } ) } \\ \times C _ { N S } ( \alpha _ { s } , \alpha _ { A } , \alpha _ { B } ) \mathcal { V } _ { c } ^ { \Delta _ { 1 , 2 , 3 , 4 } , \tilde { \Delta } _ { 1 , 2 , 3 , 4 } } M _ { \alpha , \alpha , \alpha , \Delta _ { B } } ^ { p } \right ] ,$$

$$& = \underbrace { \lim _ { P _ { s } \to 0 } \partial _ { P _ { s } } ^ { 2 } \left [ \Psi ( \alpha _ { A _ { B } } , \alpha _ { B } , Q , P _ { s } ) \bar { \Psi } ( \bar { \alpha } _ { A } , \bar { \alpha } _ { B } , Q , \bar { P } _ { s } ) M ^ { P } _ { \alpha _ { A } , \alpha _ { s } } [ \alpha _ { A } , \alpha _ { B } ] \right ] \mathcal { F } _ { r } \int _ { 0 } ^ { \infty } d P _ { s } P _ { s } ^ { 2 } \chi _ { 1 } ^ { 2 p _ { s } ^ { 2 } } , \\ & = \tilde { \Theta } ( \alpha _ { A } , \alpha _ { B } , Q ) \frac { \chi _ { 1 } ^ { Q ^ { 2 } / 4 } } { ( - \log ( \chi _ { 1 } ) ) ^ { 3 / 2 } } \mathcal { F } _ { r } \sim \chi _ { 1 } ^ { Q ^ { 2 } / 4 } \left ( - \log ( \chi _ { 1 } ) \right ) ^ { - 3 / 2 } \mathcal { F } _ { r } , \quad \alpha _ { A } , \alpha _ { B } > \frac { Q } { 4 } \, .$$

$$( 5 . 2 5 )$$

Where Μ p α t , α s α A , α B is the monodromy matrix which is defined to be,

$$\mathcal { F } _ { B B } ^ { A A } ( h _ { p } | \chi _ { 1 } ) \xrightarrow { ( 1 - \chi _ { 1 } ) \to ( 1 - \chi _ { 1 } ) e ^ { 2 \pi i } } \int _ { \mathbb { S } ^ { \prime } } d \alpha \, \mathbb { M } _ { \alpha _ { t } , \alpha _ { s } } ^ { p } \left [ \alpha _ { A } , \alpha _ { B } \right ] \mathcal { F } _ { B B } ^ { A A } ( h _ { \alpha } | \chi _ { 1 } )$$

20 The fermionic contribution to the leading order dependence on cross-ratio is the same like the bosonic case.

In (5.26) the contour Σ ′ runs from Q / 2 → Q / 2 + i ∞ and in fact it can be expressed in terms of fusion matrix as [ 85 ] ,

$$\mathbb { M } _ { \alpha _ { p } , \alpha } ^ { p } \begin{bmatrix} \alpha _ { A } & \alpha _ { A } \\ \alpha _ { B } & \alpha _ { B } \end{bmatrix} = \int _ { \mathbb { S } ^ { \prime } } d \beta e ^ { - 2 \pi i ( h _ { \beta } - h _ { A } - h _ { B } ) } F _ { \alpha _ { p } , \beta } \begin{bmatrix} \alpha _ { A } & \alpha _ { B } \\ \alpha _ { A } & \alpha _ { B } \end{bmatrix} F _ { \beta , \alpha } \begin{bmatrix} \alpha _ { A } & \alpha _ { A } \\ \alpha _ { B } & \alpha _ { B } \end{bmatrix} .$$

In (5.25) the function Ψ ( α A , α B , Q , Ps ) is defined in (A.29) of Appendix (A). This behaviour of OTOC in the super-Liouville theory is exactly similar to the behaviour of OTOC obtained in [ 85 ] for the case of Liouville theory . To compute the integral, we used the saddle-point approach , and we have taken CNS approximated for two light conformal dimensions and one heavy conformal dimension. In deriving its the asymptotic form, we used the expression of Γ b ( x ) defined in Appendix (B). F r is independent of α s and it comes from the other remaining part of the conformal block.

## 5.2 OTOC on even torus

The two-point bosonic and fermionic super-Virasoro blocks in torus at leading order in q is given by 21 ,

$$\mathcal { B } _ { B } ^ { ( 1 ) } = \frac { \left [ ( \Delta _ { s } + \tilde { \Delta } _ { 2 } - \Delta _ { 2 } ) ( \tilde { \Delta } _ { 4 } + \Delta _ { s } - \Delta _ { 3 } ) \right ] } { 2 \Delta _ { s } } \chi _ { 1 } + \mathcal { O } ( q ) \, , \\ \mathcal { B } _ { F } ^ { ( 1 ) } = \left [ \frac { ( - \tilde { \Delta } _ { 2 } - \Delta _ { s } - \Delta _ { 2 } + 1 / 2 ) ( - \Delta _ { s } - \tilde { \Delta } _ { 4 } - \Delta _ { 3 } + 1 / 2 ) } { 2 \Delta _ { s } } \right ] \chi _ { 1 } + \mathcal { O } ( q ) \, .$$

In the following part, we focus on the "classical" torus conformal block , which is given by,

$$\mathcal { V } _ { c } ^ { \Delta _ { 1 , 2 , 3 , 4 } , \tilde { \Delta } _ { 1 , 2 , 3 , 4 } } ( q , z _ { 1 , 2 , 3 , 4 } ) = \exp ( \frac { c } { 6 } f ^ { \epsilon _ { 1 , 2 , 3 , 4 } , \tilde { \epsilon } _ { 1 , 2 , 3 , 4 } } ) \ \text { as } \ c \to \infty \ ,$$

where the function f is the classical conformal block and 22 ,

$$\epsilon _ { i } = \frac { \Delta _ { i } } { k } , \quad \tilde { \epsilon } _ { i } = \frac { \tilde { \Delta } _ { i } } { k } , \quad \text {where} \quad k = \frac { c } { 6 } .$$

Now, using (A.1) the s -channel block function is given by,

$$f ^ { \epsilon _ { 1 , 2 , 3 , 4 } , \tilde { \epsilon } _ { 1 , 2 , 3 , 4 } } = ( \tilde { \epsilon } _ { 1 } - 1 / 4 ) \log ( q ) + \sum _ { n = 0 } ^ { \infty } q ^ { n } f _ { n , B / F } ^ { ( 1 ) } ( \epsilon , \tilde { \epsilon } | x , y ) ,$$

where the first few expansion coefficients are,

$$f _ { B 0 } ^ { ( 1 ) } & = \frac { 1 } { 2 \tilde { \varepsilon } _ { 3 } } [ \frac { ( \tilde { \varepsilon } _ { 1 } + \tilde { \varepsilon } _ { 2 } - \epsilon _ { 1 } ) ( \tilde { \varepsilon } _ { 2 } + \tilde { \varepsilon } _ { 3 } - \epsilon _ { 2 } ) } { 2 \tilde { \varepsilon } _ { 2 } } \chi _ { 1 } \frac { ( \tilde { \varepsilon } _ { 3 } + \tilde { \varepsilon } _ { 4 } - \epsilon _ { 3 } ) ( \tilde { \varepsilon } _ { 4 } + \tilde { \varepsilon } _ { 1 } - \epsilon _ { 4 } ) } { 2 \tilde { \varepsilon } _ { 4 } } ] , \\ f _ { F 0 } ^ { ( 1 ) } & = \frac { 1 } { 2 \tilde { \varepsilon } _ { 3 } } [ \frac { ( - \tilde { \varepsilon } _ { 1 } - \tilde { \varepsilon } _ { 2 } - \epsilon _ { 1 } + 1 / 2 ) ( - \tilde { \varepsilon } _ { 2 } - \tilde { \varepsilon } _ { 3 } - \epsilon _ { 2 } + 1 / 2 ) } { 2 \tilde { \varepsilon } _ { 2 } } \chi _ { 1 } \frac { ( - \tilde { \varepsilon } _ { 3 } - \tilde { \varepsilon } _ { 4 } + 1 / 2 ) ( - \tilde { \varepsilon } _ { 4 } - \tilde { \varepsilon } _ { 1 } - \epsilon _ { 4 } + 1 / 2 ) } { 2 \tilde { \varepsilon } _ { 4 } } ] \\ \frac { 1 } { 2 }$$

21 only ∆ s dependent part is written here.

22 Heavy operators scales as ∆ H ∼ c ε and light operators scales as ∆ L ∼ ε . ε denotes the classical dimension.

Figure 2 : Figure depicting the transformation needed to get the OTO OPE block from the Necklace channel out of time order conformal block by modularΣ transformation and the fusionΦ transformation.

<!-- image -->

with 23 , χ 1 : = z 12 z 34 z 13 z 24 . Also, B / F denotes the bosonic or fermionic counterpart.

The out-of-time-order OPE channel conformal block can be obtained from the necklace channel conformal block by composition of three fusion( Φ ) and one Σ -move [ 31 ] .

$$\mathcal { F } _ { O P E } = \int \frac { d \tilde { a } _ { 2 } } { 2 } \frac { d \tilde { a } _ { 3 } } { 2 } \frac { d \tilde { a } _ { 4 } } { 2 } \frac { d \tilde { a } _ { 1 } } { 2 } \frac { d \tilde { a } _ { 1 } } { 2 } \mathbb { F } _ { \alpha _ { 2 } ^ { \prime } \tilde { a } _ { 2 } ^ { 2 } } \left [ \alpha _ { A } ^ { \ \tilde { a } _ { 3 } } \right ] \mathbb { F } _ { \alpha _ { 3 } ^ { \prime } } \left [ \alpha _ { \tilde { a } _ { 1 } } ^ { \ \tilde { a } _ { 2 } } \right ] \mathbb { F } _ { \alpha _ { 1 } ^ { \prime } } \mathbb { F } _ { \tilde { a } _ { 1 } } ^ { \alpha _ { B } ^ { \prime } } \left [ \begin{matrix} \alpha _ { A } & \tilde { a } _ { 2 } \\ \tilde { a } _ { 1 } & \tilde { a } _ { 2 } \end{matrix} \right ] \mathbb { S } _ { \alpha _ { 1 } ^ { \prime } } \left [ \alpha _ { 1 } ^ { \prime } \right ] \mathcal { F } _ { N } ^ { O T O } \, .$$

Now in the limit, α ′ 3 = α ′ 2 = α B and α A = ε → 0 we get,

$$\mathbb { F } _ { \alpha _ { 3 } ^ { \prime } \tilde { \alpha } _ { 3 } } \begin{bmatrix} \epsilon & \tilde { \alpha } _ { 4 } \\ \tilde { \alpha } _ { 2 } ^ { \prime } & \tilde { \alpha } _ { 1 } \end{bmatrix} & = \delta ( \tilde { \alpha } _ { 3 } - \alpha _ { 2 } ^ { \prime } ) + \mathcal { O } ( \epsilon ) , \\ \mathbb { F } _ { \alpha _ { 2 } ^ { \prime } \tilde { \alpha } _ { 2 } } \begin{bmatrix} \alpha _ { B } & \tilde { \alpha } _ { 3 } \\ \epsilon & \tilde { \alpha } _ { 1 } \end{bmatrix} & = \delta ( \tilde { \alpha } _ { 2 } - \alpha _ { B } ) + \mathcal { O } ( \epsilon ) .$$

The transformations are schematically sketched in Fig. (2). Now considering α ′ 4 , α ′ 1 → 0, the integral simplifies to,

$$\mathcal { F } _ { O P E } & = \int \frac { d \tilde { a } _ { 2 } } { 2 } \frac { d \tilde { a } _ { 3 } } { 2 } \frac { d \tilde { a } _ { 4 } } { 2 } \frac { d \tilde { a } _ { 1 } } { 2 } \delta ( \tilde { a } _ { 3 } - \alpha _ { 2 } ^ { \prime } ) \delta ( \tilde { a } _ { 2 } - \alpha _ { 1 } ) C _ { N S } ( \tilde { a } _ { 4 } , \tilde { a } _ { 1 } , \alpha _ { B } ) \frac { W _ { N S } ( Q ) W _ { N S } ( \tilde { a } _ { 4 } ) } { \pi W _ { N S } ( Q - \tilde { a } _ { 1 } ) W _ { N S } ( Q - \alpha _ { B } ) } \\ & = \int \frac { d \tilde { a } _ { 4 } } { 2 } \frac { d \tilde { a } _ { 1 } } { 2 } C _ { N S } ( \tilde { a } _ { 4 } , \tilde { a } _ { 1 } , \alpha _ { B } ) \frac { W _ { N S } ( Q ) W _ { N S } ( \tilde { a } _ { 4 } ) } { \pi W _ { N S } ( Q - \tilde { a } _ { 1 } ) W _ { N S } ( Q - \alpha _ { B } ) } \mathbb { S } _ { 0 \tilde { a } _ { 1 } } [ 0 ] \times \mathcal { F } _ { N } ^ { O T O } | _ { \tilde { a } _ { 3 } = \alpha _ { 2 } ^ { \prime } , \tilde { a } _ { 2 } = \alpha _ { B } } + ( \cdots ) \\$$

where in (5.34) we define ,

$$W _ { N S } ( \alpha ) = \frac { 2 ( \pi \mu \gamma ( \frac { b Q } { 2 } ) ) ^ { - \frac { Q - 2 \alpha } { 2 b } } \pi ( \alpha - Q / 2 ) } { \Gamma ( 1 + b ( \alpha - Q / 2 ) ) \Gamma ( 1 + \frac { 1 } { b } ( \alpha - Q / 2 ) ) }$$

23 This definition of χ 1 is valid for torus one-point superblocks.

where γ ( x ) = Γ ( x ) Γ ( 1 -x ) , and the structure constant is given by,

$$C _ { N S } ( \alpha _ { 1 } , \alpha _ { 2 } , \alpha _ { 3 } ) = \lambda ^ { ( Q - \sum _ { i = 1 } ^ { 3 } \alpha _ { i } ) / b }$$

$$x \xrightarrow { \Upsilon ^ { \prime } _ { N S } ( 0 ) \Upsilon _ { N S } ( 2 \alpha _ { 1 } ) \Upsilon _ { N S } ( 2 \alpha _ { 2 } ) \Upsilon _ { N S } ( 2 \alpha _ { 3 } ) } \times \frac { \Upsilon ^ { \prime } _ { N S } ( 0 ) \Upsilon _ { N S } ( 2 \alpha _ { 1 } ) \Upsilon _ { N S } ( 2 \alpha _ { 2 } ) \Upsilon _ { N S } ( 2 \alpha _ { 3 } ) } { \Upsilon _ { N S } ( \alpha _ { 1 } + \alpha _ { 2 } + \alpha _ { 3 } - Q ) \Upsilon _ { N S } ( \alpha _ { 1 } + \alpha _ { 2 } - \alpha _ { 3 } ) \Upsilon _ { N S } ( - \alpha _ { 1 } + \alpha _ { 2 } + \alpha _ { 3 } ) \Upsilon _ { N S } ( - \alpha _ { 3 } + \alpha _ { 1 } - \alpha _ { 2 } ) }$$

with λ = πµγ ( bQ / 2 ) b 1 -b 2 . F OTO N is the out-of-time-order conformal block. Also we need the following modularΣ transformation matrix elements,

$$\mathbb { S } _ { 0 , \alpha _ { 1 } } [ 0 ] = \sin ( \pi b ^ { - 1 } ( \alpha _ { 1 } - Q / 2 ) ) \sin ( \pi b ( \alpha _ { 1 } - Q / 2 ) ) \, ,$$

$$\mathbb { S } _ { 0 , \alpha _ { 3 } } [ 0 ] = \sin ( \pi b ^ { - 1 } ( \alpha _ { 3 } - Q / 2 ) ) \sin ( \pi b ( \alpha _ { 3 } - Q / 2 ) ) \, .$$

## Behaviour of OTOC with time:

Finally we have all the ingredients to analyze the behvaiour of OTOC as a function time. To do that, we mainly focus on the bosonic part ( φ a ) of the super-Virasoro primary operators as defined in (2.8), leaving the more general study involving a fermionic part as defined in (2.7) for future. The bare n -point necklace channel torus block for this scalar primary is given by [ 126 ] , 24

$$\mathcal { V } _ { \Delta } ^ { h } ( \rho ) = \prod _ { i = 1 } ^ { n } \rho _ { i } ^ { \tilde { \Delta } _ { i } } \ F _ { K } \begin{bmatrix} \tilde { \Delta } _ { 1 } + \tilde { \Delta } _ { 2 } - \Delta _ { 1 } & \tilde { \Delta } _ { 2 } + \tilde { \Delta } _ { 3 } - \Delta _ { 2 } & \cdots & \tilde { \Delta } _ { n } + \tilde { \Delta } _ { 1 } - \Delta _ { n } \\ 2 \tilde { \Delta } _ { 1 } , 2 \tilde { \Delta } _ { 2 } , 2 \tilde { \Delta } _ { 3 } , \cdots , 2 \Delta _ { n } & \end{bmatrix} ( \rho _ { 1 } , \rho _ { 2 } , \cdots , \rho _ { n } )$$

where the cross-ratios on the torus are defined as,

$$\rho _ { 1 } & = \frac { q z _ { 1 2 } z _ { n - 1 , n } } { ( z _ { n - 1 } - q z _ { 1 } ) ( z _ { n } - q z _ { 2 } ) } = - q \chi _ { 1 } , & \rho _ { 2 } & = \frac { z _ { 2 3 } ( z _ { n } - q z _ { 1 } ) } { z _ { 1 3 } ( z _ { n } - q z _ { 2 } ) } = 1 - \chi _ { 1 } \, , \\ \rho _ { n } & = \frac { z _ { 2 3 } ( z _ { n } - q z _ { 1 } ) } { z _ { 1 3 } ( z _ { n } - q z _ { 2 } ) } = \chi _ { 1 } , & \rho _ { i } & = \frac { z _ { i - 2 , i - 1 } z _ { i , i + 1 } } { z _ { i - 2 , i } z _ { i - 1 , i + 1 } } = \chi _ { 1 } - 1 \, , & \text {for } 3 \leq i \leq n - 1 \, . \\$$

The above cross-ratios are obtained for the configuration z 1 = 0, z 2 = χ 1 , z 3 = 1, z 4 = ∞ . The monodromy ( Μ 1 ) around χ 1 = 1 is given by 25 ,

$$M _ { \lceil \nabla \rceil } ^ { \lceil \nabla \rceil } = & \lim _ { \epsilon \to 0 } \pi ( - \hat { 1 } _ { \ast } \hat { \gamma } _ { \ast } ^ { \Delta _ { 1 } } ( - q _ { \chi _ { 1 } } ) ^ { \hat { \bar { 1 } } } \csc ( \pi ( - \hat { \bar { } { 1 } } _ { - } - \hat { \bar { } { 3 } } _ { + } + \Delta _ { 1 } + \Delta _ { 2 } ) ) \Gamma ( 2 \hat { \bar { } { 2 } } _ { 1 } ) \, \ s f _ { 1 } ( - \Delta _ { 2 } + \hat { \bar { } { 1 } } _ { + } + \Delta _ { 4 } , - \Delta _ { 1 } + \hat { \bar { } { 3 } } _ { + } + \Delta _ { 4 } ; 2 \hat { \bar { } { 4 } } _ { 4 } ; - 1 ) \\ & \left ( \frac { 1 } { \Gamma ( \Delta _ { 1 } - \hat { \bar { } { 1 } } _ { + } + \Delta _ { 2 } ) \Gamma ( \Delta _ { 2 } + \hat { \bar { } { 2 } } _ { - } - \hat { \bar { } { 3 } } _ { \Delta _ { 1 } } ) \Gamma ( - \Delta _ { 1 } - \Delta _ { 2 } + \hat { \bar { } { 1 } } _ { + } + \Delta _ { 3 } + 1 ) } { e ^ { - \frac { i \pi } { 2 } ( \bar { \Delta } _ { 1 } - \bar { \Delta } _ { 3 } + \Delta _ { 1 } ) + 2 ( \pi ) } - \bar { \Delta } _ { 1 } - \bar { \Delta } _ { 3 } + \Delta _ { 1 } + \Delta _ { 2 } - \bar { \Delta } _ { 1 } - \bar { \Delta } _ { 3 } + \Delta _ { 2 } } ) \right ) .$$

$$\Gamma ^ { 1 } & = \left ( \frac { 1 } { \Gamma ( \Delta _ { 1 } - \tilde { \Delta } _ { 1 } + \tilde { \Delta } _ { 2 } ) \Gamma ( \Delta _ { 2 } + \tilde { \Delta } _ { 2 } - \tilde { \Delta } _ { 3 } ) \Gamma ( - \Delta _ { 1 } - \Delta _ { 2 } + \tilde { \Delta } _ { 1 } + \tilde { \Delta } _ { 3 } + 1 ) } { \Gamma ( \Delta _ { 1 } - \tilde { \Delta } _ { 1 } + \tilde { \Delta } _ { 2 } ) \Gamma ( \Delta _ { 1 } + \Delta _ { 2 } - \tilde { \Delta } _ { 1 } - \tilde { \Delta } _ { 3 } + \Delta _ { 1 } + \Delta _ { 2 } \epsilon - \tilde { \Delta } _ { 1 } - \tilde { \Delta } _ { 3 } + \Delta _ { 1 } + \Delta _ { 2 } } \right ) . \\$$

24 ˜ ∆ i and ∆ i are intermediate and external conformal dimensions respectively.

25 For our case the 2 F 1 has branch cut in z ∈ [ 1, ∞ ) .

In Fig. (3), we have shown the plot of super-Liouville OTOC for real and imaginary parts. The leading behaviour with respect to time can be easily extracted by substituting 26 [ 77 ] ,

$$\tau = i \frac { K _ { 1 } ( 1 - \chi _ { 1 } ) } { K _ { 1 } ( \chi _ { 1 } ) } , \quad \chi _ { 1 } = \left ( \frac { \Theta _ { 2 } ( e ^ { i \pi \tau } ) } { \Theta _ { 3 } ( e ^ { i \pi \tau } ) } \right ) ^ { 4 } . \\$$

in (5.25). K 1 ( z ) are elliptic integral of the first kind. The monodromy around χ 1 = 1 is mapped to torus modular parameter via ,

$$\tau \rightarrow \frac { \tau } { 1 + 2 \tau } , \quad \bar { \tau } \rightarrow \bar { \tau } . \\$$

The behaviour of the holomorphic part of OTOC in time is given by 27 ,

$$\text {Inc.} \, \text {Variance of the} \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi \, \Pi$$

Figure 3 : Figure depicting the plot of non-normalized Out-of-time-order correlator for the case of super-Liouville OTOC. The blue curve depicts the real part of OTOC, and the red curve denotes the imaginary part of the OTOC. Brown curve denotes absolute value of the OTOC. The real part of the OTOC saturates at zero value at late time. Similarly the imaginary part saturates after decaying at the specific same value.

<!-- image -->

It's evident from (non-normalized) (5.44) that the early-time behaviour of the OTOC does not show a simple exponential decay, i.e. it is (the real part of it) not simply of the form α -β e λ L t Fig. (3) shows the plot of the real, imaginary and absolute value of the non-normalized OTOC. This is quite distinct from what is known for the Schwarzian theory dual to JT gravity [ 53 ] . Further studies are required, including subleading corrections from the geometry, to understand its implication for quantum chaos better.

26 Here χ 1 means cross ratio in the super-plane.

27 We used the conformal transformation to obtain the OTOC as a function of time from the cross-ratio space χ 1 .

## 6 Conclusion and Outlook

Mainly motivated by the aspects of Topological QFT and Gravity, in this paper, we discuss how to compute the partition function of N = 1 super-Liouville theory using super-Virasoro TQFT. Due to different spin structures related to the super-torus, the bosonic or fermionic fields may or may not have zero modes. Correspondingly, the path integral and the modular sum changes. Apart from calculating partition functions for different topologies with sphere and torus boundaries, we also compute the OTOC on the torus, including the fermionic contribution to probe the early-time chaotic regime. As a probe matter, we include super-Liouville primaries in the boundary of the torus. Below, we summarize the main findings of the paper,

- First, we show that the claim of [ 35 ] , that the gravitational partition function is equal to the sum of the modulus square of the Virasoro partition function from the Teichmuller × Teichmuller correspondence also holds for the N = 1 super-Liouville theory. We claimed and showed that the inner product of the superconformal blocks with two different Liouville momenta satisfies delta function type normalization. The bulk mapping class group (MCG) becomes a subset of the boundary mapping class group for Riemann surfaces with boundaries. Due to this, we needed to perform an extra modular sum to compute the gravitational partition function. The modular sum depends on the spin structure corresponding to the different boundary conditions.
- Second, we compute the partition function of supergravity by using the super-Virasoro TQFT . Apart from the spherical boundary, we also consider torus wormholes. Different spin structures lead to different partition functions. Odd spin structures change the boundary condition so that the zero modes contribute, and we also had to sum over odd modular parameter transformations.
- Eventually, we calculate the OTOC on the super-torus with super-Liouville matter insertions. For this purpose, we first compute the necklace channel out-of-time-order conformal block in the large charge ( c → ∞ ) limit. In this semiclassical limit, one can see that the conformal blocks are exponentiated. One should be able to verify this using the monodromy method. However, in the torus, it is a bit tedious to calculate the exponential function using superconformal ward identities on the super-torus. Hence, we use braiding transformation to compute the out-of-time order necklace channel conformal block from the time-ordered one. Then, we find the OPE channel conformal block using fusion and modular transformations on the torus. As the leading order behaviour of the super-torus four-point conformal blocks in χ 1 → 0 limit is uniform i.e χ ∆ s 1 for all the piece of super-blocks, we consider only that for the computation of the saddle point integral for super-torus OTOC [ 125 ] . We leave the more general analysis for future studies.
- The result of the off-shell torus wormhole partition function in VTQFT differs from the result obtained in [ 127 ] and the difference lies in the fact of bulk mapping class group. When we take two trumpets (with one asymptotic T 2 boundary and one geodesic T 2 boundary) and

try to glue them along some bulk torus slice, one needs to perform a non-trivial gauging of the bulk mapping class group (corresponding to the twist angle upto 2 π ). This makes the inner product different from what achieved in VTQFT and make the inner product nonorthogonal. One can verify this by calculating the 〈 ρρ 〉 correlator (using ensemble averaging) and find the Vandermonde determinant to compute the overlap between the states of different Liouville momenta as shown in [ 32 ] . In virasoro or super-Virasoro TQFT the problem is universal because of the orthogonality between Liouville momenta states. The torus wormhole itself is a off-shell geometry. Now other off-shell geometries ( Σ g , n × S 1 ) can be calculated also in N = 1 supergravity using super-Virasoro TQFT or Index theorems following [ 101 ] and detailed investigation of that is indeed important which we leave for future investigations.

- It is worth interesting to investigate the nature of OTOC after including higher genus Riemann surfaces in the boundary. Though the corrections are expected to be subleading, one should still compute it explicitly, to figure out any notable changes in the nature of the OTOC.

Now, we end by discussing some possible future directions. One can, in principle, generalize this study for N = 2 super-Liouville theory and test whether the normalization (2.1) of the conformal block holds. However, one has to first study the fusion and modular transformation matrices for N = 2 as they are not well know. Furthermore, one should also consider non-gaussian contractions for multi-boundary OPE statistics as well as test the Eigenstate-Thermalization Hypothesis (ETH). Another immediate calculation is to calculate the Handlebody partition function for the super-Liouville case generalizing [ 35 ] . Currently, there has been a resurgence of studying field theories on null manifolds with Carrollian symmetry [ 128, 129 ] and its supersymmetric extensions [ 130 ] . It will be interesting to generalize the computations presented in Sec. (4) and Sec. (5) for BMS3 super-torus generalizing [ 131 ] .

## Acknowledgement

AB thanks the speakers and participants of the workshop 'Quantum Information in QFT and AdS / CFT-III" organized at IIT Hyderabad between 16-18th September, 2022 and funded by SERB through a Seminar Symposia (SSY) grant (SSY / 2022 / 000446), 'Quantum Information Theory in Quantum Field Theory and Cosmology" held in 4-9th June, 2023 hosted by Banff International Research Centre at Canada AB would also like to thank the Department of Physics of BITS Pilani, Goa Campus, for hospitality during the course of this work. S.G (PMRF ID: 1702711) and S.P (PMRF ID: 1703278) are supported by the Prime Minister's Research Fellowship of the Government of India. S.G would like to thank Prof. Jan Plefka at Humboldt University, Prof. Niels Emil BjerrumBohr at Niels Bohr Institute and Prof. Rafael Porto at DESY for their kind hospitality during the course of the work. PN is supported by a Fulbright-Nehru Postdoctoral Research Fellowship. She would like to thank Vijay Balasubramanian and the hospitality of the University of Pennsylvania during the course of this work. AB is supported by the Core Research Grant (CRG / 2023 / 001120)

and Mathematical Research Impact Centric Support Grant (MTR / 2021 / 000490) by the Department of Science and Technology Science and Engineering Research Board (India), India AB also acknowledges the associateship program of the Indian Academy of Science, Bengaluru.

## A Sketching the derivation of the necklace channel conformal block

$$\mathcal { F } ^ { \{ s \} } = \mathcal { A } _ { c } ^ { \Delta _ { 1 , 2 , 3 , 4 } , \tilde { \Delta } _ { 1 , 2 , 3 , 4 } } ( z _ { 1 , 2 , 3 , 4 } ) + q ^ { 1 / 2 } \mathcal { B } _ { c } ^ { \Delta _ { 1 , 2 , 3 , 4 } , \tilde { \Delta } _ { 1 , 2 , 3 , 4 } } ( z _ { 1 , 2 , 3 , 4 } ) + \mathcal { O } ( q ) ,$$

The coefficients can be defined as ,

$$\text {The coefficients can be defined as ,} \\ \mathcal { A } _ { c } = \sum _ { m , r , g = 0 | S | + | \Psi | + | T | + | P | = m } \frac { \langle \tilde { \Delta } _ { 1 } | \Phi _ { 1 } ( Z _ { 1 } ) | S J , \tilde { \Delta } _ { 2 } \rangle } { \langle \tilde { \Delta } _ { 1 } | \Phi _ { 1 } ( Z _ { 1 } ) | \tilde { \Delta } _ { 2 } \rangle } [ B _ { \Delta } ^ { 2 } ] ^ { S J , T P } \frac { \langle \tilde { \Delta } _ { 2 } , T P | \Phi _ { 2 } ( Z _ { 2 } ) | O Y , \tilde { \Delta } _ { 3 } \rangle } { \langle \tilde { \Delta } _ { 2 } | \Phi _ { 2 } ( Z _ { 2 } ) | \tilde { \Delta } _ { 3 } \rangle } \\ \times [ B _ { \Delta } ^ { 3 } ] ^ { O Y , U ( \frac { \tilde { \Delta } _ { 3 } , U V | \Phi _ { 3 } ( Z _ { 3 } ) | E W , \tilde { \Delta } _ { 4 } ) } { \langle \tilde { \Delta } _ { 3 } | \Phi _ { 3 } ( Z _ { 3 } ) | \tilde { \Delta } _ { 4 } \rangle } [ B _ { \Delta } ^ { 4 } ] ^ { E W , C X } \frac { ( \tilde { \Delta } _ { 4 } , C X | \Phi _ { 4 } ( Z _ { 4 } ) | \tilde { \Delta } _ { 1 } ) } { ( \tilde { \Delta } _ { 4 } | \Phi _ { 4 } ( Z _ { 4 } ) | \tilde { \Delta } _ { 1 } ) } \\ \intertext { and similarly the other coefficient can be determined as , }$$

and similarly the other coefficient can be determined as ,

$$\mathcal { B } _ { c } & = \sum _ { m , r , g = 0 } ^ { \infty } \sum _ { | S | + J | = | T | + | P | = m } \frac { \langle \tilde { \Delta } _ { 1 } | G _ { 1 } \Phi _ { 1 } ( Z _ { 1 } ) | S J , \tilde { \Delta } _ { 2 } \rangle } { \langle \tilde { \Delta } _ { 1 } | \Phi _ { 1 } ( Z _ { 1 } ) | \tilde { \Delta } _ { 2 } \rangle } [ B _ { \Delta } ^ { 2 } ] ^ { S J , T P } \frac { \langle \tilde { \Delta } _ { 2 } , T P | \Phi _ { 2 } ( Z _ { 2 } ) | O Y , \tilde { \Delta } _ { 3 } \rangle } { \langle \tilde { \Delta } _ { 1 } | \Phi _ { 2 } ( Z _ { 2 } ) | \tilde { \Delta } _ { 3 } \rangle } \\ & \quad \times [ B _ { \Delta } ^ { 3 } ] ^ { O Y , U V } \frac { ( \tilde { \Delta } _ { 3 } , U V | \Phi _ { 3 } ( Z _ { 3 } ) | E W , \tilde { \Delta } _ { 4 } ) } { \langle \tilde { \Delta } _ { 3 } | \Phi _ { 3 } ( Z _ { 3 } ) | \tilde { \Delta } _ { 4 } \rangle } \left [ B _ { \Delta } ^ { 4 } \right ] ^ { E W , C X } \frac { ( \tilde { \Delta } _ { 4 } , C X | \Phi _ { 4 } ( Z _ { 4 } ) G _ { - 1 } | \tilde { \Delta } _ { 1 } ) } { ( \tilde { \Delta } _ { 4 } | \Phi _ { 4 } ( Z _ { 4 } ) | \tilde { \Delta } _ { 1 } ) } . \\ \text {Using (A.20) one achieves,}$$

Using (A.20) one achieves,

$$\text {Using (A.20) on architecture,} \\ \frac { ( \tilde { \Delta } _ { 2 } , T P | \Phi ( z , \theta ) | O Y , \tilde { \Delta } _ { 3 } ) } { ( \tilde { \Delta } _ { 2 } | \Phi ( z , \theta ) | \tilde { \Delta } _ { 3 } ) } & \sim \frac { ( \tilde { \Delta } _ { 2 } | G _ { 1 } \Phi ( z , \theta ) G _ { - 1 } | \tilde { \Delta } _ { 3 } ) } { C _ { \Phi _ { 1 } \Phi _ { 2 } \Phi _ { 3 } } } = & \frac { ( \tilde { \Delta } _ { 3 } + \tilde { \Delta } _ { 2 } - \Delta ) \, C _ { \phi \phi \phi } \tilde { \Delta } ^ { \tilde { \Delta } _ { 2 } - \Delta } \tilde { \phi } \tilde { \phi } } { C _ { \Phi _ { 1 } \Phi _ { 2 } \Phi _ { 3 } } } + \\ & \frac { ( - \tilde { \Delta } _ { 2 } - \tilde { \Delta } _ { 3 } - \Delta + 1 / 2 ) \, C _ { \phi _ { 1 } \phi _ { 2 } \Phi _ { 3 } } } { C _ { \Phi _ { 1 } \Phi _ { 2 } \Phi _ { 3 } } } . \\$$

## · Non-vanishing structure constants:

$$C _ { \Phi _ { 1 } \Phi _ { 2 } \Phi _ { 3 } } = \left ( \pi \mu \gamma \left ( \frac { Q b } { 2 } \right ) b ^ { 1 - b ^ { 2 } } \right ) ^ { \frac { Q - a } { b } } \frac { \Upsilon _ { N S } ^ { \prime } ( 0 ) \Upsilon _ { N S } ( 2 a _ { 1 } ) \Upsilon _ { N S } ( 2 a _ { 2 } ) \Upsilon _ { N S } ( 2 a _ { 3 } ) } { \Upsilon _ { N S } ( a - Q ) \Upsilon _ { N S } ( a _ { 1 + 2 - 3 } ) \Upsilon _ { N S } ( a _ { 3 + 2 - 1 } ) \Upsilon _ { N S } ( a _ { 3 + 1 - 2 } ) } \, , \quad ( A . 5 )$$

$$\tilde { C } _ { \phi _ { 1 } \phi _ { 2 } \phi _ { 3 } } = & \left ( \pi \mu _ { \gamma } \left ( \frac { Q b } { 2 } \right ) b ^ { 1 - b ^ { 2 } } \right ) ^ { \frac { Q - a } { b } } \frac { 2 i \Upsilon _ { N S } ^ { \prime } ( 0 ) \Upsilon _ { N S } ( 2 a _ { 1 } ) \Upsilon _ { N S } ( 2 a _ { 2 } ) \Upsilon _ { N S } ( 2 a _ { 3 } ) } { \Upsilon _ { R } ( a - Q ) \Upsilon _ { R } ( a _ { 1 + 2 - 3 } ) \Upsilon _ { R } ( a _ { 3 + 2 - 1 } ) \Upsilon _ { R } ( a _ { 3 + 1 - 2 } ) } \quad ( A . 6 ) \\$$

where Υ NS and Υ R are defined in (2.6). Now we also have,

$$C _ { \Phi _ { 1 } \psi _ { 2 } \Phi _ { 3 } } = x _ { 3 1 } \tilde { C } _ { \Phi _ { 1 } \Phi _ { 2 } \Phi _ { 3 } } & & C _ { \Phi _ { 1 } \psi _ { 2 } \psi _ { 3 } } = - \frac { \Delta _ { 2 } + \Delta _ { 3 } - \Delta _ { 1 } } { x _ { 2 3 } } C _ { \Phi _ { 1 } \Phi _ { 2 } \Phi _ { 3 } } \, .$$

## NS algebra and Superfields

The mode expansion of the superfield of conformal dimension ∆ is given by,

$$\Phi _ { \Delta } ( Z ) = \sum _ { m \in \mathbb { N } _ { 0 } } z ^ { - m - \Delta } \Phi _ { m } + \sum _ { 2 m \in \mathbb { N } _ { 0 } } z ^ { - m - 1 / 2 - \Delta } \theta \, \Phi _ { m }$$

where Ν 0 denotes non-negative integers and Z denotes the super-coordinate Z ≡ Z ( z , θ ) .The OPE of G(z) with the superfield Φ is given by 28 ,

$$G ( z ) \Phi _ { N S } ( 0 , 0 ) = \sum _ { k \in \mathbb { Z } + 1 / 2 } z ^ { k - 3 / 2 } G _ { - k } \Phi _ { N S } ( 0 , 0 ) \, .$$

Again the OPE with Virasoro generators L n is defined as,

$$T ( z ) \Phi _ { N S } = \sum _ { k \in \mathbb { Z } } z ^ { n - 2 } L _ { - n } \Phi _ { N S } ( 0 , 0 ) \, .$$

The generator algebra takes the following form,

$$[ L _ { m } , L _ { n } ] & = ( m - n ) L _ { m + n } + \frac { c } { 1 2 } m ( m ^ { 2 } - 1 ) \delta _ { m + n , 0 } , \\ & [ L _ { m } , G _ { k } ] = \frac { m - 2 k } { 2 } G _ { m + k } , \\ & \{ G _ { k } , G _ { l } \} = 2 L _ { k + l } + \frac { c } { 3 } ( k ^ { 2 } - \frac { 1 } { 4 } ) \delta _ { k + l , 0 } .$$

The superfields satisfy the algebra,

$$[ L _ { n } , \Phi _ { \Delta , \hat { z } } ( z , \theta , \bar { z } , \bar { \theta } ) ] & = z ^ { n } [ z \partial _ { z } + ( n + 1 ) ( \Delta + \frac { 1 } { 2 } \theta \partial _ { \theta } ) ] \Phi _ { \Delta , \bar { \phi } } \, , \\ [ \bar { L } _ { n } , \Phi _ { \Delta , \bar { z } } ( z , \theta , \bar { \theta } ) ] & = \bar { z } ^ { n } [ \bar { z } \partial _ { z } + ( n + 1 ) ( \bar { \Delta } + \frac { 1 } { 2 } \bar { \theta } \partial _ { \theta } ) ] \Phi _ { \Delta , \bar { \phi } } \, , \\ [ G _ { k } , \Phi _ { \Delta , \bar { \Delta } } ( z , \theta , \bar { \theta } ) ] & = z ^ { k - 1 / 2 } [ z \partial _ { \theta } - \theta z \partial _ { z } - \theta ( 2 k + 1 ) \Delta ] \Phi _ { \Delta , \bar { \phi } } \, , \\ [ \bar { G } _ { k } , \Phi _ { \Delta , \bar { \Delta } } ( z , \theta , \bar { \theta } ) ] & = \bar { z } ^ { k - 1 / 2 } [ \bar { z } \partial _ { \bar { \theta } } - \bar { \theta } z \bar { \theta } z - \bar { \theta } ( 2 k + 1 ) \bar { \Delta } ] \Phi _ { \Delta , \bar { \phi } } \, .$$

The three-point function of the super-primary fields is given by

$$\langle \Phi ( z _ { 3 } , \theta _ { 3 } ; \bar { z } _ { 3 } , \bar { \theta } _ { 3 } ) \Phi ( z _ { 2 } , \theta _ { 2 } ; \bar { z } _ { 2 } , \bar { \theta } _ { 2 } ) \Phi ( z _ { 1 } , \theta _ { 1 } ; \bar { z } _ { 1 } , \bar { \theta } _ { 1 } ) \rangle = \\ Z _ { 3 2 } ^ { \beta _ { 1 } } Z _ { 3 1 } ^ { \beta _ { 2 } } Z _ { 2 1 } ^ { \beta _ { 3 } } \langle \Phi ( \infty , 0 ; \infty , 0 ) \Phi ( 1 , \Theta ; 1 , \bar { \Theta } ) \Phi ( 0 , 0 ; 0 , 0 ) \rangle$$

where β i = ∆ i -∆ j -∆ k , Z 12 = z 1 -z 2 -θ 1 θ 2 , along with

$$\Theta = \frac { 1 } { \sqrt { z _ { 1 2 } z _ { 1 3 } z _ { 2 3 } } } \left ( \theta _ { 1 } z _ { 2 3 } + \theta _ { 2 } z _ { 3 1 } + \theta _ { 3 } z _ { 1 2 } - \frac { 1 } { 2 } \theta _ { 1 } \theta _ { 2 } \theta _ { 3 } \right ) .$$

28 In the upcoming calculation, the ' SL ' subscript in labelling the super-primary is implicit.

We need to compute the following quantity 29 ,

$$\langle \tilde { \Delta } _ { 2 } | G _ { \frac { 1 } { 2 } } \Phi ( z ) G _ { - \frac { 1 } { 2 } } | \tilde { \Delta } _ { 3 } \rangle \equiv \langle \tilde { \Delta } _ { 2 } | G _ { \frac { 1 } { 2 } } ( \phi ( z ) + \theta \psi ( z ) ) G _ { - \frac { 1 } { 2 } } | \tilde { \Delta } _ { 3 } \rangle \, .$$

To do this, we need to have the mode expansion of the scalar and the fermionic field as mentioned in (A.8). We have,

$$\psi _ { \Delta + 1 / 2 } ( z ) = \sum _ { m \in \mathbb { Z } + 1 / 2 } z ^ { - m - 1 / 2 - \Delta } \, \psi _ { m } \, .$$

The mode coefficient can be extracted using the Cauchy residue theorem and is given by,

$$\psi _ { m } = \oint _ { 0 } \frac { d z } { 2 \pi i } \, z ^ { m + \Delta - 1 / 2 } \, \psi _ { \Delta + 1 / 2 } ( z ) .$$

Now, in (A.12), let's first concentrate on the Fermionic part and do the algebra,

$$\langle \tilde { \Delta } _ { 2 } | G _ { \frac { 1 } { 2 } } \psi ( z ) G _ { - \frac { 1 } { 2 } } | \tilde { \Delta } _ { 3 } \rangle = \sum _ { m \in \mathbb { Z } + 1 / 2 } z ^ { - m - 1 / 2 - \Delta } \langle \tilde { \Delta } _ { 2 } | G _ { \frac { 1 } { 2 } } \psi _ { m } G _ { - \frac { 1 } { 2 } } | \tilde { \Delta } _ { 3 } \rangle \, .$$

Our goal is to express the correlation function in terms of the three-point function 〈 ˜ ∆ 2 | ψ ( z ) | ˜ ∆ 3 〉 . To do this, one has to know the following algebra { Gr , ψ m } and [ Gr , φ m ] .

$$\| \ a d _ { m } \| _ { 0 } & \ h a s \, ( z _ { 0 } \, \ m a t h s c r { D } _ { z } \, ( z _ { r } , \phi _ { m } ) \, \ a d \, [ z _ { r } , \phi _ { m } ] . \\ & \{ G _ { r } , \psi _ { m } \} = \oint _ { 0 } \frac { d z } { 2 \pi i } \, z ^ { m + \Delta - 1 / 2 } \{ G _ { r } , \psi _ { \Delta + q / 2 } ( z ) \} \, , \\ & = \oint _ { 0 } \frac { d z } { 2 \pi i } \, z ^ { m + \Delta + r - 1 } ( z \partial _ { z } + ( 2 r + 1 ) \Delta ) \phi _ { \Delta } ( z ) \, , \\ & = \oint _ { 0 } \frac { d z } { 2 \pi i } z ^ { m + r + \Delta - 1 } [ - ( m + r + \Delta ) + ( 2 r + 1 ) \Delta ] \phi _ { \Delta } ( z ) \, , \\ & = [ - ( m + r + \Delta ) + ( 2 r + 1 ) \Delta ] \phi _ { m + r } \, .$$

Similarly, we can have the algebra for the second one,

$$[ G _ { r } , \phi _ { m } ] & = \oint _ { 0 } \frac { d z } { 2 \pi i } z ^ { m + \Delta - 1 } [ G _ { r } , \phi _ { \Delta } ( z ) ] , \\ & = \oint _ { 0 } \frac { d z } { 2 \pi i } z ^ { m + r + \Delta - 1 / 2 } \psi ( z ) = \psi _ { m + r } .$$

29 We have taken the definition of the superfield a bit different from (2.8).

Now, (A.14) can be evaluated as follows,

$$Now , ( A . 1 4 ) \, \text { can be evaluated as follows,} \\ \langle \tilde { \Delta } _ { 2 } | G _ { \frac { 1 } { 2 } } \psi ( z ) G _ { - \frac { 1 } { 2 } } | \tilde { \Delta } _ { 3 } \rangle & = \sum _ { m \in \mathbb { Z } + 1 / 2 } z ^ { - m - 1 / 2 - \Delta } \langle \tilde { \Delta } _ { 3 } | G _ { \frac { 1 } { 2 } } \psi _ { - m } G _ { - \frac { 1 } { 2 } } \rangle ^ { * } , \\ & = \sum _ { m \in \mathbb { Z } + 1 / 2 } z ^ { - m - 1 / 2 - \Delta } \langle \tilde { \Delta } _ { 3 } | \{ G _ { \frac { 1 } { 2 } } , \psi _ { - m } \} - \psi _ { - m } G _ { - \frac { 1 } { 2 } } \rangle ^ { * } , \\ & = \sum _ { m \in \mathbb { Z } + 1 / 2 } z ^ { - m - 1 / 2 - \Delta } \langle \tilde { \Delta } _ { 3 } | ( m - 1 / 2 + \Delta ) \phi _ { - m + 1 / 2 } G _ { - \frac { 1 } { 2 } } - \psi _ { - m } G _ { - \frac { 1 } { 2 } } | \tilde { \Delta } _ { 2 } \rangle ^ { * } , \\ & = \sum _ { m \in \mathbb { Z } + 1 / 2 } z ^ { - m - 1 / 2 - \Delta } ( m - 1 / 2 + \Delta ) \langle \tilde { \Delta } _ { 3 } | \phi _ { - m + 1 / 2 } G _ { - \frac { 1 } { 2 } } | \tilde { \Delta } _ { 2 } \rangle ^ { * } \\ & \quad - \sum _ { m \in \mathbb { Z } + 1 / 2 } z ^ { m - 1 / 2 + \Delta } \langle \tilde { \Delta } _ { 3 } | \psi _ { - m } 2 L _ { 0 } | \tilde { \Delta } _ { 2 } \rangle ^ { * } , \\ & = ( - \tilde { \Delta } _ { 2 } - \tilde { \Delta } _ { 3 } - \Delta + 1 / 2 ) ( \tilde { \Delta } _ { 2 } | \psi _ { \Delta + 1 / 2 } ( z ) | \tilde { \Delta } _ { 3 } ) \, . \\ \\ \intertext { I n a s i m i a l f s h i a n o w c a n p u t e c h o w l i n g c o rrelator } \langle \tilde { \Delta } _ { 2 } \, G _ { - } ( \tilde { \Delta } _ { 2 } - \tilde { \Delta } _ { 3 } - \Delta ) \tilde { \Delta } _ { 2 } | \tilde { \Delta } _ { 2 } \, G _ { - } \, + \, C _ { 2 } \, | \tilde { \Delta } _ { 2 } \rangle ^ { * }$$

In a similar fashion one can compute the following correlator,

$$\text {In a similar fashion one can compute the following correlator,} \\ \langle \tilde { \Delta } _ { 2 } | G _ { \frac { 1 } { 2 } } \phi ( z ) G _ { - \frac { 1 } { 2 } } | \tilde { \Delta } _ { 3 } \rangle & = \sum _ { m \in \mathbb { Z } } z ^ { - m - \Delta } \langle \tilde { \Delta } _ { 3 } | G _ { \frac { 1 } { 2 } } \phi _ { - m - \frac { 1 } { 2 } } | \tilde { \Delta } _ { 2 } \rangle ^ { * } , \\ & = \sum _ { m \in \mathbb { Z } } z ^ { - m - \Delta } \langle \tilde { \Delta } _ { 3 } | \psi _ { - m + 1 / 2 } G _ { - \frac { 1 } { 2 } } | \tilde { \Delta } _ { 2 } \rangle ^ { * } - 2 \sum _ { m \in \mathbb { Z } } z ^ { - m - \Delta } \langle \tilde { \Delta } _ { 3 } | \phi _ { - m } | \tilde { \Delta } _ { 2 } \rangle ^ { * } , \\ & = ( \tilde { \Delta } _ { 3 } + \tilde { \Delta } _ { 2 } - \Delta ) \langle \tilde { \Delta } _ { 2 } | \phi _ { \Delta } ( z ) | \tilde { \Delta } _ { 3 } \rangle \, . \\ \intertext { T h e r f o r e - the correlator involving the superfield }$$

Therefore the correlator involving the superfield Φ is given by,

$$\langle \tilde { \Delta } _ { 2 } | G _ { \frac { 1 } { 2 } } \Phi ( z , \theta ) G _ { - \frac { 1 } { 2 } } | \tilde { \Delta } _ { 3 } \rangle = ( \tilde { \Delta } _ { 3 } + \tilde { \Delta } _ { 2 } - \Delta ) \, z ^ { \tilde { \Delta } _ { 2 } - \Delta - } \tilde { \Delta } _ { 3 } + ( - \tilde { \Delta } _ { 2 } - \tilde { \Delta } _ { 3 } - \Delta + 1 / 2 ) \, C _ { \phi \psi } \, \theta \, z ^ { \tilde { \Delta } _ { 2 } - \Delta - 1 / 2 - \tilde { \Delta } _ { 3 } }$$

where the structure constants take the following non-vanishing contributions,

$$C _ { \Phi \phi \Phi } = C _ { \phi \phi \phi } - \tilde { \theta } _ { 2 } \tilde { \theta } _ { 3 } C _ { \psi \phi \psi } , \, C _ { \Phi \psi \Phi } = \tilde { \theta } _ { 2 } C _ { \psi \psi \phi } - \tilde { \theta } _ { 3 } C _ { \phi \psi \psi } \, .$$

In the last line, we used the relation,

$$\sum _ { m } ( \tilde { \Delta } _ { 2 } - \tilde { \Delta } _ { 3 } ) \langle \tilde { \Delta } _ { 2 } | \psi _ { m } | \tilde { \Delta } _ { 3 } \rangle z ^ { - m - \Delta - 1 / 2 } = - \sum _ { m } \langle \tilde { \Delta } _ { 2 } | m \psi _ { m } | \tilde { \Delta } _ { 3 } \rangle z ^ { - m - 1 / 2 - \Delta }$$

and

$$\sum _ { m } ( \tilde { \Delta } _ { 2 } - \tilde { \Delta } _ { 3 } ) \langle \tilde { \Delta } _ { 2 } | \phi _ { m } | \tilde { \Delta } _ { 3 } \rangle z ^ { - m - \Delta } = - \sum _ { m } \langle \tilde { \Delta } _ { 2 } | m \phi _ { m } | \tilde { \Delta } _ { 3 } \rangle z ^ { - m - \Delta } \, .$$

In a similar way, we also have,

$$\left ( \tilde { \Delta } _ { 2 } | G _ { \frac { 1 } { 2 } } \Phi ( z ) | \tilde { \Delta } _ { 3 } \right ) & = \sqrt { z } C _ { \phi \psi } + \theta ( \tilde { \Delta } _ { 2 } - \tilde { \Delta } _ { 3 } + \Delta ) C _ { \phi \phi } \, , \\ \left ( \tilde { \Delta } _ { 2 } | \Phi ( z ) G _ { - \frac { 1 } { 2 } } | \tilde { \Delta } _ { 3 } \right ) & = - C _ { \Phi \psi \Phi } + \theta z ^ { - 1 } ( \tilde { \Delta } _ { 2 } - \tilde { \Delta } _ { 3 } + \Delta ) C _ { \Phi \phi \Phi } \, . \\$$

Wedecompose the super-primary field into the Liouville primary field and the fermionic field. The non-vanishing matrix elements are given by (A.19) and (A.24). In principle one should compute the matrix elements to all orders in q .

## Asymptotic formulas

- We define the Upsilon function as,

$$\Upsilon _ { b } ( x ) = \frac { 1 } { \Gamma _ { b } ( x ) \Gamma _ { b } ( Q - x ) } \, .$$

This function is an entire function of x with zeroes located at x = -mb -nb -1 and x = Q + mb + nb -1 and it has the following integral representation,

$$\log \Upsilon _ { b } ( x ) \coloneqq \int _ { 0 } ^ { \infty } \frac { d t } { t } \left [ ( Q / 2 - x ) ^ { 2 } e ^ { - t } - \frac { \sinh ^ { 2 } ( ( Q / 2 - x ) t / 2 ) } { \sinh ( b t / 2 ) \sinh ( t / 2 b ) } \right ] \quad \text {for } 0 < R e ( x ) < Q . \quad ( A . 2 6 )$$

The asymptotics of the Upsilon function for large x in the upper half plane is given by [ 132 ] ,

$$\log \Upsilon _ { b } ( x ) \sim & x ^ { 2 } \log ( x ) - \left ( 3 / 2 + \frac { i \pi } { 2 } \right ) x ^ { 2 } - Q x \log x + ( 1 + \frac { i \pi } { 2 } ) Q x + ( \frac { Q ^ { 2 } + 1 } { 6 } ) \log x - \\ & - \frac { i \pi } { 1 2 } ( Q ^ { 2 } + 1 ) - 2 \log \Gamma _ { 0 } ( b ) + \mathcal { O } ( x ^ { - 1 } ) \, .$$

In (A.27) the function Γ 0 ( b ) independent of x is given by,

$$\log \Gamma _ { 0 } ( b ) = - \int _ { 0 } ^ { \infty } \frac { d t } { t } \left ( \frac { e ^ { - Q t / 2 } } { ( 1 - e ^ { - b t } ) ( 1 - e ^ { - t / b } ) } - \frac { 1 } { t ^ { 2 } } - \frac { Q ^ { 2 } - 2 } { 2 4 } e ^ { - t } \right ) .$$

- ·The quantity Ψ is defined below comes from the asymptotic expansions of CNS .

$$\Psi ( \alpha _ { A } , \alpha _ { B } , Q , P ) \equiv \frac { \Psi _ { 1 } } { \Psi _ { 2 } }$$

where,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## B Definition of different functions

In this appendix, we will review some special functions that we heavily used in the main text.

## · Barnes double gamma function

For Re(x) &gt; 0 the function Γ b ( x ) is given by the integral representation,

<!-- formula-not-decoded -->

Γ b ( x ) is a special case of Barnes double gamma Γ ν 1 ν 2 ( x ) with ν 1 = ν -1 2 = b , being an analytic continuation of the function,

<!-- formula-not-decoded -->

to s = 0, showing a self duality property,

$$\Gamma _ { b } ( x ) = \Gamma _ { b ^ { - 1 } } ( x ) .$$

$$\Gamma _ { b } ( x + b ) = \frac { \sqrt { 2 \pi } b ^ { b x - 1 / 2 } \Gamma _ { b } ( x ) } { \Gamma ( b x ) } \, ,$$

$$S _ { N S } ( x ) = S _ { b } ( \frac { x } { 2 } ) S _ { b } ( \frac { Q + x } { 2 } ) \, .$$

$$S _ { N S } ( x ) S _ { N S } ( Q - x ) = S _ { R } ( x ) S _ { R } ( Q - x ) = 1 \, .$$

## · Location of the Zeroes and poles:

$$S _ { N S } ( x ) & = 0 \iff x = Q + m b + n b ^ { - 1 } , \ m , n \in \mathbb { Z } _ { \geq 0 } , \ \ m + n \in 2 \mathbb { Z } \\ S _ { R } ( x ) & = 0 \iff x = Q + m b + n b ^ { - 1 } , \ \ m , n \in \mathbb { Z } _ { \geq 0 } , \ \ m + n \in 2 \mathbb { Z } + 1 \\ S _ { N S } ^ { - 1 } ( x ) & = 0 \iff x = - m b - n b ^ { - 1 } , \ \ m , n \in \mathbb { Z } _ { \geq 0 } , \ \ m + n \in 2 \mathbb { Z } \\ S _ { R } ^ { - 1 } ( x ) & = 0 \iff x = - m b - n b ^ { - 1 } , \ \ m , n \in \mathbb { Z } _ { \geq 0 } , \ \ m + n \in 2 \mathbb { Z } + 1 \\$$

- Basic Residue:
- Few important functions:

Γ b ( x ) satisfies also,

## · Reflection Properties:

$$\lim _ { x \to 0 } x \, S _ { N S } ( x ) = \frac { 1 } { \pi } \, .$$

$$\frac { \Gamma _ { N S } ( 2 \alpha ) } { \Gamma _ { N S } ( 2 \alpha - Q ) } = W _ { N S } ( \alpha ) \lambda ^ { \frac { Q - 2 \alpha } { 2 b } } \, .$$

Where,

## · Upsilon functions :

where,

$$W _ { N S } ( \alpha ) = \frac { 2 ( \pi \mu \gamma ( \frac { b Q } { 2 } ) ) ^ { - \frac { Q - 2 \alpha } { 2 b } } \pi ( \alpha - Q / 2 ) } { \Gamma ( 1 + b ( \alpha - Q / 2 ) ) \Gamma ( 1 + \frac { 1 } { b } ( \alpha - Q / 2 ) ) }$$

- Γ NS ( x ) has a pole at 0, the behaviour near the pole is given by

$$\Gamma _ { N S } ( x ) \xrightarrow { x \to 0 } \frac { \Gamma _ { N S } ( Q ) } { \pi x } , \quad \Upsilon _ { N S } ^ { \prime } ( 0 ) = \frac { \pi } { \Gamma _ { N S } ^ { 2 } ( Q ) } .$$

$$\frac { \Upsilon _ { N S } ( 2 x ) } { \Upsilon _ { N S } ( 2 x - Q ) } = \mathcal { G } _ { N S } ( x ) \lambda ^ { - \frac { Q - 2 x } { b } } ,$$

$$\mathcal { G } _ { N S } ( x ) = \frac { W _ { N S } ( Q - x ) } { W _ { N S } ( x ) } .$$

## C Torus two-point function (Liouville CFT) with general left and right moving temperature

We first calculate the torus two-point function in 2d CFT where we have some intermediate left and right moving temperature β L and β R , respectively. We insert the two operators O 1 and O 2 in the Euclidean time circle . To distinguish them from the insertion in the spatial circle, we use a tilde symbol. Now we use the modular crossing kernels and Virasoro fusion kernel to calculate the torus two-point function in the following fashion Fig. (4), considering α = Q 2 + i P (where P is the Liouville Momenta),

$$\mathcal { F } _ { h h ^ { \prime } } ^ { \tilde { N } } & = \widehat { \mathcal { F } _ { P ^ { \prime } P } } ^ { O P E } , \\ & = \int \frac { d P _ { 2 } } { 2 } \frac { d P _ { 1 } } { 2 } \mathbb { S } _ { P ^ { \prime } P _ { 2 } } [ P ] \mathbb { F } _ { P , P _ { 1 } } \left [ \tilde { P } \ P _ { 2 } \right ] \mathcal { F } _ { P _ { 1 } , P _ { 2 } } ^ { N } .$$

Now we know that the fusion kernel can be written in the following integral form [ 133 ] ,

$$\mathbb { F } _ { P ^ { \prime \prime } , P } \begin{bmatrix} P ^ { * } & \tilde { P } \\ P ^ { * } & \tilde { P } \end{bmatrix} = P ( \alpha _ { i } ; \alpha ^ { \prime \prime } , \alpha ) P ( \alpha _ { i } ; Q - \alpha ^ { \prime \prime } , Q - \alpha ) \int _ { \mathcal { C } ^ { \prime } } \frac { d s } { i } \prod _ { k = 1 } ^ { 4 } \frac { \mathcal { S } _ { b } ( s + U _ { k } ) } { \mathcal { S } _ { b } ( s + V _ { k } ) }$$

where,

$$P ( \alpha _ { i } ; \alpha ^ { \prime \prime } , \alpha ) = \frac { \Gamma _ { b } ^ { 2 } ( \alpha ^ { \prime \prime } + \alpha ^ { * } - \tilde { \alpha } ) \Gamma ( \alpha ^ { \prime \prime } + Q - \tilde { \alpha } - \alpha ^ { * } ) \Gamma ( \alpha ^ { \prime \prime } - Q + \tilde { \alpha } + \alpha ^ { * } ) \Gamma _ { b } ( 2 \alpha ) } { \Gamma _ { b } ^ { 2 } ( \alpha ) \Gamma ( \alpha + Q - 2 \tilde { \alpha } ) \Gamma ( \alpha - Q + 2 \alpha ^ { * } ) \Gamma _ { b } ( 2 \alpha - Q ) } \quad ( C . 3 )$$

along with,

$$\mathcal { S } _ { b } ( x ) \colon = \frac { \Gamma _ { b } ( x ) } { \Gamma _ { b } ( Q - x ) } .$$

Figure 4 : In the first step we transform from the ˜ N channel to the OPE channel. Then we use the modular crossing transformation. At last, we use the Virasoro fusion kernel to write the OPE channel in terms of the Necklace channel.

<!-- image -->

We also define Uk and Vk as follows,

$$U _ { 1 } & = i ( P _ { 1 } - P _ { 4 } ) = 0 \, , & V _ { 1 } & = Q / 2 + i ( - P ^ { \prime \prime } + P ^ { * } - \tilde { P } ) \, , \\ U _ { 2 } & = - i ( P _ { 1 } + P _ { 4 } ) = - 2 i \tilde { P } \, , & V _ { 2 } & = Q / 2 + i ( P ^ { \prime \prime } + P ^ { * } - \tilde { P } ) \, , \\ U _ { 3 } & = i ( P _ { 2 } + P _ { 3 } ) = 2 i P ^ { * } \, , & V _ { 3 } & = Q / 2 + i P \, , \\ U _ { 4 } & = i ( P _ { 2 } - P _ { 3 } ) = 0 \, , & V _ { 4 } & = Q / 2 - i P \, .$$

Various limits of the fusion kernel with heavy operator insertions are discussed in [ 134 ] .

Now we will proceed to show the formalism to compute the Virasoro torus two-point function. If we insert the operator in the dual Necklace channel (Euclidean time circle), this can be written as, Considering the probe operators O 1 = O 2 = ˜ O to be heavy, we can write (C.6) as,

<!-- image -->

$$= \sum _ { p , q } | C _ { \tilde { \mathcal { O } } _ { p } \mathcal { O } _ { q } } | ^ { 2 } | \mathcal { F } _ { 1 2 } ^ { g = 1 } ( h _ { p } , h _ { q } ; \tau , \nu ) | ^ { 2 } \, .$$

Now the average over the product of two torus two-point function is given by [ 135 ] :

$$& \overline { \langle \mathcal { O } _ { 1 } ( \nu , \bar { \nu } ) \mathcal { O } _ { 2 } ( 0 ) \rangle _ { T ^ { 2 } ( \tau , \bar { \tau } ) } \langle \mathcal { O } _ { 1 } ( \nu ^ { \prime } , \bar { \nu } ^ { \prime } ) \mathcal { O } _ { 2 } ( 0 ) \rangle _ { T ^ { 2 } ( \tau ^ { \prime } , \bar { \tau } ^ { \prime } ) } \, , \\ & = \sum _ { p , q , g , h } \overline { | C _ { \mathcal { O } _ { 1 } \mathcal { O } _ { q } \mathcal { O } _ { n } \mathcal { O } _ { g } \mathcal { O } _ { h } } | ^ { 2 } } \mathcal { F } _ { \mathcal { I } _ { 1 2 } ^ { \bar { N } , g = 1 } ( h _ { p } , h _ { q } ; \tau , \nu ) } | ^ { 2 } \mathcal { F } _ { \mathcal { I } _ { 1 2 } ^ { \bar { N } , g = 1 } ( h _ { g } , h _ { h } ; \tau , \nu ) } | ^ { 2 } , \\ & = 2 \left | \int d h _ { p } d h _ { q } \rho _ { 0 } ( h _ { p } ) \rho _ { 0 } ( h _ { q } ) C _ { \bar { 0 } ( \bar { h } , h _ { p } , h _ { q } ) } C _ { \bar { h } , \bar { h } _ { p } , \bar { h } _ { q } } ) | \mathcal { F } _ { \bar { 1 } 2 } ^ { \bar { N } , g = 1 } ( h _ { p } , h _ { q } ; \tau , \nu ) | ^ { 2 } \right | ^ { 2 }$$

where

and

$$C _ { 0 } ( P _ { 1 } , P _ { 2 } , P _ { 3 } ) = \frac { \Gamma _ { b } ( 2 Q ) \Gamma _ { b } ( \frac { Q } { 2 } \pm i P _ { 1 } \pm i P _ { 2 } \pm i P _ { 3 } ) } { \sqrt { 2 } \Gamma _ { b } ( Q ) ^ { 3 } \prod _ { k = 1 } ^ { 3 } \Gamma _ { b } ( Q \pm 2 i P _ { k } ) } .$$

In (C.7) the 'bar' denotes the averaging over the dimensions of the heavy operators while the other conformal dimensions are held fixed. The Liouville structure constants show a universal behavior in this limit [ 132 ] .

$$\mathcal { F } _ { 1 2 } ^ { \tilde { N } , g = 1 } ( h , h ^ { \prime } ; \tau , \nu ) = \int \frac { d P _ { 2 } } { 2 } \frac { d P _ { 1 } } { 2 } \mathbb { S } _ { P ^ { \prime } P _ { 2 } } [ P ] \mathbb { F } _ { P , P _ { 1 } } \begin{bmatrix} \tilde { P } & P _ { 2 } \\ \tilde { P } & P _ { 2 } \end{bmatrix} \mathcal { F } _ { P _ { 1 } , P _ { 2 } } ^ { N } .$$

## Fusion matrix in super Liouville field theory

We describe the fusion matrix in SLFT in this appendix . Generally, the fusion matrices take the following form { i , j } = 1, 2 which correspond to parity of even and odd respectively ,

$$& \text {following form} \, \{ i , j \} = 1 , 2 \text { which correspond to parity of even and odd respectively} \, , \\ & \mathbb { F } _ { \alpha , a _ { t } } \left [ \begin{matrix} \alpha _ { 3 } & \alpha _ { 2 } \\ \alpha _ { 4 } & \alpha _ { 1 } \end{matrix} \right ] = \frac { \Gamma _ { ( 2 Q - \alpha _ { t } - \alpha _ { 2 } - \alpha _ { 3 } ) } \Gamma _ { ( i } Q - \alpha _ { t } + \alpha _ { 3 } - \alpha _ { 2 } ) \Gamma _ { ( i } ( Q + \alpha _ { t } - \alpha _ { 2 } - \alpha _ { 3 } ) \Gamma _ { ( i } ( \alpha _ { 3 } + \alpha _ { t } - \alpha _ { 2 } ) } \right ) } { \Gamma _ { ( 2 Q - \alpha _ { 1 } - \alpha _ { s } ) } \Gamma _ { ( j } ( Q - \alpha _ { s } - \alpha _ { 2 } + \alpha _ { 1 } ) \Gamma _ { ( j } ( Q - \alpha _ { 1 } - \alpha _ { 2 } + \alpha _ { s } ) \Gamma _ { ( j } ( \alpha _ { s } + \alpha _ { 1 } - \alpha _ { 2 } ) } } \right ) \\ & \times \frac { \Gamma _ { ( i } ( Q - \alpha _ { t } - \alpha _ { 1 } + \alpha _ { 4 } ) \Gamma _ { ( i } ( \alpha _ { 1 } + \alpha _ { 4 } - \alpha _ { t } ) \Gamma _ { ( i } ( \alpha _ { t } + \alpha _ { 4 } - \alpha _ { 1 } ) \Gamma _ { ( i } ( \alpha _ { t } + \alpha _ { 1 } + \alpha _ { 4 } - Q ) } } { \Gamma _ { ( j } ( Q - \alpha _ { s } - \alpha _ { 3 } + \alpha _ { 4 } ) \Gamma _ { ( j } ( \alpha _ { 3 } + \alpha _ { 4 } - \alpha _ { s } ) \Gamma _ { ( j } ( \alpha _ { s } + \alpha _ { 4 } - Q ) } } \\ & \times \frac { \Gamma _ { \text {NS} } ( 2 Q - 2 \alpha _ { s } ) \Gamma _ { \text {NS} } ( 2 \alpha _ { s } ) } { \Gamma _ { \text {NS} } ( Q - 2 \alpha _ { t } ) \Gamma _ { \text {NS} } ( 2 \alpha _ { t } - Q ) } \frac { 1 } { i } \int _ { - i \infty } ^ { i \infty } d \tau J _ { \alpha , \alpha _ { t } } \left [ \begin{matrix} \alpha _ { 3 } & \alpha _ { 2 } \\ \alpha _ { 4 } & \alpha _ { 1 } \end{matrix} \right ] _ { j } , \\ & \text {We will consider } i = j = 1 , \text { for the fusion matrix in NS sector. we have,}$$

We will consider i = j = 1, for the fusion matrix in NS sector. we have,

$$\text {we consider } & t = J = 1 , \text { for the reduction in } N \text { section. } \text { we have,} \\ J _ { \alpha , \alpha _ { t } } \left [ \begin{array} { c } \alpha _ { 3 } \, \alpha _ { 2 } \\ \alpha _ { 4 } \, \alpha _ { 1 } \end{array} \right ] = \frac { S _ { N s } ( Q + \tau - \alpha _ { 1 } ) S _ { N s } ( \tau + \alpha _ { 4 } + \alpha _ { 2 } - \alpha _ { 3 } ) S _ { N s } ( \tau + \alpha _ { 1 } ) S _ { N s } ( \tau + \alpha _ { 4 } + \alpha _ { 2 } + \alpha _ { 3 } - Q ) } { S _ { N s } ( Q + \tau + \alpha _ { 4 } - \alpha _ { 3 } ) S _ { N s } ( \tau + \alpha _ { 4 } + \alpha _ { 1 } ) S _ { N s } ( Q + \tau + \alpha _ { 2 } - \alpha _ { 3 } ) S _ { N s } ( \tau + \alpha _ { 2 } + \alpha _ { 3 } ) } \\ & + \frac { S _ { R } ( Q + \tau - \alpha _ { 1 } ) S _ { R } ( \tau + \alpha _ { 4 } + \alpha _ { 2 } - \alpha _ { 3 } ) S _ { R } ( \tau + \alpha _ { 1 } ) S _ { R } ( \tau + \alpha _ { 4 } + \alpha _ { 2 } + \alpha _ { 3 } - Q ) } { S _ { R } ( Q + \tau + \alpha _ { 4 } - \alpha _ { 1 } ) S _ { R } ( \tau + \alpha _ { 4 } + \alpha _ { 3 } ) S _ { R } ( Q + \tau + \alpha _ { 2 } - \alpha _ { 3 } ) S _ { R } ( \tau + \alpha _ { 2 } + \alpha _ { 3 } ) } \, , \\ & \quad \text {where } S _ { R } ( \tau - \alpha _ { 1 } ) S _ { R } ( \tau ) \, .$$

where SNS , R are defined by,

$$S _ { N S } ( x ) = \frac { \Gamma _ { N S } ( x ) } { \Gamma _ { N S } ( Q - x ) } , \quad S _ { R } ( x ) = \frac { \Gamma _ { R } ( x ) } { \Gamma _ { R } ( Q - x ) } \quad \text {with} \quad \Gamma _ { R } ( x ) = \Gamma _ { b } ( \frac { x + b } { 2 } ) \Gamma _ { b } ( \frac { x + b ^ { - 1 } } { 2 } ) \\$$

Alternatively, it can be shown that for α s = 0, the fusion matrix takes the following form [ 136 ] ,

$$F _ { 0 , \alpha _ { t } } \left [ \begin{array} { c c } \alpha _ { 3 } & \alpha _ { 1 } \\ \alpha _ { 3 } & \alpha _ { 1 } \end{array} \right ] _ { 1 } = C _ { N S } ( \alpha _ { t } , \alpha _ { 1 } , \alpha _ { 3 } ) \frac { W _ { N S } ( Q ) W _ { N S } ( \alpha _ { t } ) } { \pi W _ { N S } ( Q - \alpha _ { 1 } ) W _ { N S } ( Q - \alpha _ { 3 } ) } \, .$$

One can also verify that,

$$W _ { N S } ( x ) W _ { N S } ( Q - x ) = - 4 \sin \pi b ( x - Q / 2 ) \sin \pi \frac { 1 } { b } ( x - Q / 2 ) \, .$$

## D Different transformations

We have the following basic moves [ 28 ] :

- Braiding:

<!-- image -->

## · Fusion:

<!-- image -->

## · Modular S-transformation:

<!-- image -->

$$\mathbb { B } _ { 1 2 } ^ { 3 } = \pm e ^ { \pi i ( \Delta _ { 3 } - \Delta _ { 1 } - \Delta _ { 2 } ) } \, .$$

## E Computation of semiclassical Liouville torus partition function

In this section we will compute the semiclassical Liouville partition function at large central charge and will show how the the cosmological constant can be treated as an integral regulator while integrating over zero mode. We start with the Liouville theory on torus,

$$S = \int _ { \mathcal { T } } d ^ { 2 } z \sqrt { g } \left ( \frac { 1 } { 4 \pi } g ^ { a b } \partial _ { a } \phi \partial _ { b } \phi + \frac { 1 } { 4 \pi } Q R \phi + \mu e ^ { 2 b \phi } \right ) .$$

where, Q = b + 1 / b and central charge is, c = 1 + 6 Q 2 . Now the torus metric is conformally flat (even any metric in 2D is conformally flat) and can be written as,

$$d s ^ { 2 } = e ^ { 2 \varphi ( z , \bar { z } ) } | d z | ^ { 2 } , \det ( g ) = e ^ { 4 \varphi }$$

Therefore, the Ricci scalar can be written as,

$$R = - 2 e ^ { - 2 \varphi ( z , \bar { z } ) } \hat { g } ^ { a b } \, \nabla _ { a } \nabla _ { b } \varphi .$$

Note that, for our case the transformed metric is flat so ˆ g ab = δ ab . Hence it follows that the second term in the action can be written as,

$$Q R \phi \rightarrow - 2 Q e ^ { - 2 \varphi ( z , \bar { z } ) } \delta ^ { a b } \phi \, \partial _ { a } \partial _ { b } \varphi .$$

Β is easy to determine, Therefore the Liouville action takes the form,

$$S & = \int d ^ { 2 } z \, e ^ { 2 \varphi ( z , \vec { z } ) } \left ( \frac { 1 } { 4 \pi } e ^ { - 2 \varphi } \delta ^ { a b } \hat { \partial } _ { a } \phi \, \hat { \partial } _ { b } \phi - \frac { 2 Q } { 4 \pi } e ^ { - 2 \varphi } \delta ^ { a b } \, \phi \, \hat { \partial } _ { b } \hat { \partial } _ { a } \varphi + \mu e ^ { 2 b \phi } \right ) , \\ & \to \int d ^ { 2 } z \, \left ( \frac { 1 } { 4 \pi } \delta ^ { a b } \hat { \partial } _ { a } \phi \, \hat { \partial } _ { b } \phi + \frac { 2 Q } { 4 \pi } \, \hat { \partial } _ { b } \varphi \, \hat { \partial } _ { a } \varphi + \mu e ^ { 2 b \phi + 2 \varphi } \right ) .$$

Now, the classical limit corresponds to b → 0. In this limit, one can identify the field ϕ = b φ [ 137 ] . The e.o.m for the Liouville field is,

$$\frac { 1 + 2 b Q } { 4 \pi } \Delta \phi = 4 b \mu e ^ { 4 b \phi } , \, ( \text {Note that in classical limit } \phi \text { scales as } \varphi / b ) .$$

In the classical limit, the Liouville field satisfies the zero mode condition (for torus) [ 138 ] :

$$\Delta \phi = 0 \, \Longrightarrow \, \tau _ { 2 } \partial _ { \bar { z } } \partial _ { z } = 0$$

which admits only constant solutions (say φ 0 ) i.e. Ker( ∆ ) = constant (independent of z , ¯ z ) on torus. Now we compute the semiclassical partition function by considering only the contribution from the classical saddle to the Liouville interaction. Decomposing the Liouville field as φ = φ 0 + δφ ,

$$Z & = \int d \phi _ { 0 } \, e ^ { - \mu e ^ { 4 b \phi _ { 0 } } \int d ^ { 2 } z } \int \mathcal { D } \delta \phi \, e ^ { - \int d ^ { 2 } z \left ( \frac { 1 + 2 b \Omega } { 4 \pi } \, \delta ^ { a b } \partial _ { a } \delta \phi \, \partial _ { b } \delta \phi \right ) + \cdots } , \\ & \to - \frac { \log ( \mu ) } { 4 b \int d ^ { 2 } z } \, Z _ { b o s o n } ( \tau ) \, .$$

In the absence of µ , the zero mode integral ( R d φ 0 ) gives a divergent result. However, as shown in (E.8), in the presence of µ the integral gives a convergent result, and that is how µ acts as an integral regulator. All in all, ignoring the overall constants we will get,

$$Z _ { L } \sim Z _ { b o s o n } ( \tau ) \, .$$

Extrapolating the same argument, the super-Liouville partition function at large central charge takes the form:

$$Z _ { S L } \sim Z _ { b o s o n } \times Z _ { f e r m i o n } .$$

## References

- [ 1 ] R. Jackiw, Lower Dimensional Gravity , Nucl. Phys. B 252 (1985) 343-356.
- [ 2 ] C. Teitelboim, Gravitation and Hamiltonian Structure in Two Space-Time Dimensions , Phys. Lett. B 126 (1983) 41-45.
- [ 3 ] P . Saad, S. H. Shenker and D. Stanford, JT gravity as a matrix integral , 1903.11115 .

- [ 4 ] J. M. Maldacena, The Large N limit of superconformal field theories and supergravity , Adv. Theor. Math. Phys. 2 (1998) 231-252 [ hep-th/9711200 ] .
- [ 5 ] E. Witten, Anti-de Sitter space and holography , Adv. Theor. Math. Phys. 2 (1998) 253-291 [ hep-th/9802150 ] .
- [ 6 ] G. J. Turiaci and E. Witten, N = 2 JT supergravity and matrix models , JHEP 12 (2023) 003 [ 2305.19438 ] .
- [ 7 ] L. V . Iliesiu, On 2D gauge theories in Jackiw-Teitelboim gravity , 1909.05253 .
- [ 8 ] L. V . Iliesiu and G. J. Turiaci, The statistical mechanics of near-extremal black holes , JHEP 05 (2021) 145 [ 2003.02860 ] .
- [ 9 ] L. V . Iliesiu, J. Kruthoff, G. J. Turiaci and H. Verlinde, JT gravity at finite cutoff , SciPost Phys. 9 (2020) 023 [ 2004.07242 ] .
- [ 10 ] S. Collier, L. Eberhardt, B. Muehlmann and V . A. Rodriguez, The Virasoro minimal string , SciPost Phys. 16 (2024), no. 2, 057 [ 2309.10846 ] .
- [ 11 ] S. Ebert, H.-Y. Sun and Z. Sun, TT-deformed free energy of the Airy model , JHEP 08 (2022) 026 [ 2202.03454 ] .
- [ 12 ] A. Bhattacharyya, S. Ghosh and S. Pal, Aspects of T ¯ T + J ¯ T deformed 2D topological gravity : from partition function to late-time SFF , 2309.16658 .
- [ 13 ] M. Atiyah, Topological quantum field theories , Inst. Hautes Etudes Sci. Publ. Math. 68 (1989) 175-186.
- [ 14 ] V . Mikhaylov, Teichmüller TQFT vs. Chern-Simons theory , JHEP 04 (2018) 085 [ 1710.04354 ] .
- [ 15 ] A. Maloney and E. Witten, Quantum Gravity Partition Functions in Three Dimensions , JHEP 02 (2010) 029 [ 0712.0155 ] .
- [ 16 ] X. Yin, Partition Functions of Three-Dimensional Pure Gravity , Commun. Num. Theor. Phys. 2 (2008) 285-324 [ 0710.2129 ] .
- [ 17 ] E. Witten, Three-Dimensional Gravity Revisited , 0706.3359 .
- [ 18 ] J. Manschot, AdS(3) Partition Functions Reconstructed , JHEP 10 (2007) 103 [ 0707.1159 ] .
- [ 19 ] A. Maloney and E. Witten, Averaging over Narain moduli space , JHEP 10 (2020) 187 [ 2006.04855 ] .
- [ 20 ] S. Collier and A. Maloney, Wormholes and spectral statistics in the Narain ensemble , JHEP 03 (2022) 004 [ 2106.12760 ] .
- [ 21 ] N. Afkhami-Jeddi, H. Cohn, T. Hartman and A. Tajdini, Free partition functions and an averaged holographic duality , JHEP 01 (2021) 130 [ 2006.04839 ] .
- [ 22 ] N. Benjamin, C. A. Keller, H. Ooguri and I. G. Zadeh, Narain to Narnia , Commun. Math. Phys. 390 (2022), no. 1, 425-470 [ 2103.15826 ] .
- [ 23 ] J. Chandra, S. Collier, T . Hartman and A. Maloney, Semiclassical 3D gravity as an average of large-c CFTs , JHEP 12 (2022) 069 [ 2203.06511 ] .
- [ 24 ] A. Belin and J. de Boer, Random statistics of OPE coefficients and Euclidean wormholes , Class. Quant. Grav. 38 (2021), no. 16, 164001 [ 2006.05499 ] .

- [ 25 ] T. G. Mertens, J. Simón and G. Wong, A proposal for 3d quantum gravity and its bulk factorization , JHEP 06 (2023) 134 [ 2210.14196 ] .
- [ 26 ] L. Eberhardt, M. R. Gaberdiel and R. Gopakumar, Deriving the AdS 3 / CFT 2 correspondence , JHEP 02 (2020) 136 [ 1911.00378 ] .
- [ 27 ] L. Eberhardt, M. R. Gaberdiel and R. Gopakumar, The Worldsheet Dual of the Symmetric Product CFT , JHEP 04 (2019) 103 [ 1812.01007 ] .
- [ 28 ] S. Collier, L. Eberhardt and M. Zhang, Solving 3d gravity with Virasoro TQFT , SciPost Phys. 15 (2023), no. 4, 151 [ 2304.13650 ] .
- [ 29 ] S. Collier, L. Eberhardt and M. Zhang, 3d gravity from Virasoro TQFT: Holography, wormholes and knots , 2401.13900 .
- [ 30 ] A. Dymarsky and A. Shapere, Bulk derivation of TQFT gravity , 2405.20366 .
- [ 31 ] J. de Boer, D. Liska and B. Post, Multiboundary wormholes and OPE statistics , 2405.13111 .
- [ 32 ] D. L. Jafferis, L. Rozenberg and G. Wong, 3d Gravity as a random ensemble , 2407.02649 .
- [ 33 ] L. Chen, L.-Y. Hung, Y. Jiang and B.-X. Lao, Quantum 2D Liouville Path-Integral Is a Sum over Geometries in AdS 3 Einstein Gravity , 2403.03179 .
- [ 34 ] R. Ducrocq, M. Rausch De Traubenberg and M. Valenzuela, A pedagogical discussion of N = 1 four-dimensional supergravity in superspace , Mod. Phys. Lett. A 36 (2021), no. 16, 2130015 [ 2104.06671 ] .
- [ 35 ] L. Eberhardt, Notes on crossing transformations of Virasoro conformal blocks , 2309.11540 .
- [ 36 ] J. Ellegaard Andersen and R. Kashaev, A TQFT from Quantum Teichmüller Theory , Commun. Math. Phys. 330 (2014) 887-934 [ 1109.6295 ] .
- [ 37 ] N. Aghaei, M. Pawelkiewicz and J. Teschner, Quantisation of super Teichmüller theory , Commun. Math. Phys. 353 (2017), no. 2, 597-631 [ 1512.02617 ] .
- [ 38 ] N. Aghaei, M. K. Pawelkiewicz and M. Yamazaki, Towards Super Teichmüller Spin TQFT , Adv. Theor. Math. Phys. 26 (2022), no. 2, 245-294 [ 2008.09829 ] .
- [ 39 ] A. Sen and B. Zwiebach, String Field Theory: A Review , 2405.19421 .
- [ 40 ] E. Witten, Notes On Super Riemann Surfaces And Their Moduli , Pure Appl. Math. Quart. 15 (2019), no. 1, 57-211 [ 1209.2459 ] .
- [ 41 ] F . A. Dolan and H. Osborn, Conformal four point functions and the operator product expansion , Nucl. Phys. B 599 (2001) 459-496 [ hep-th/0011040 ] .
- [ 42 ] A. I. Larkin and Y. N. Ovchinnikov, Quasiclassical Method in the Theory of Superconductivity , Journal of Experimental and Theoretical Physics (1969).
- [ 43 ] F . Haake, Quantum Signatures of Chaos . Springer Series in Synergetics. Springer, Berlin, 2010.
- [ 44 ] O. Bohigas, M. J. Giannoni and C. Schmit, Characterization of chaotic quantum spectra and universality of level fluctuation laws , Phys. Rev. Lett. 52 (1984) 1-4.
- [ 45 ] M. V . Berry, The Bakerian Lecture, 1987: Quantum Chaology , Proceedings of the Royal Society of London Series A 413 (Sept., 1987) 183-198.

- [ 46 ] L. D'Alessio, Y. Kafri, A. Polkovnikov and M. Rigol, From quantum chaos and eigenstate thermalization to statistical mechanics and thermodynamics , Adv. Phys. 65 (2016), no. 3, 239-362 [ 1509.06411 ] .
- [ 47 ] P . Hosur, X.-L. Qi, D. A. Roberts and B. Yoshida, Chaos in quantum channels , JHEP 02 (2016) 004 [ 1511.04021 ] .
- [ 48 ] A. Nahum, S. Vijay and J. Haah, Operator Spreading in Random Unitary Circuits , Phys. Rev. X 8 (2018), no. 2, 021014 [ 1705.08975 ] .
- [ 49 ] C. von Keyserlingk, T . Rakovszky, F . Pollmann and S. Sondhi, Operator hydrodynamics, OTOCs, and entanglement growth in systems without conservation laws , Phys. Rev. X 8 (2018), no. 2, 021013 [ 1705.08910 ] .
- [ 50 ] I. L. Aleiner, L. Faoro and L. B. Ioffe, Microscopic model of quantum butterfly effect: out-of-time-order correlators and traveling combustion waves , Annals Phys. 375 (2016) 378-406 [ 1609.01251 ] .
- [ 51 ] M. Gärttner, J. G. Bohnet, A. Safavi-Naini, M. L. Wall, J. J. Bollinger and A. M. Rey, Measuring out-of-time-order correlations and multiple quantum spectra in a trapped ion quantum magnet , Nature Phys. 13 (2017) 781 [ 1608.08938 ] .
- [ 52 ] A. Kitaev, A simple model of quantum holography. https: // online.kitp.ucsb.edu / online / entangled15 / kitaev2 / .
- [ 53 ] J. Maldacena and D. Stanford, Remarks on the Sachdev-Ye-Kitaev model , Phys. Rev. D 94 (2016), no. 10, 106002 [ 1604.07818 ] .
- [ 54 ] J. Cotler, N. Hunter-Jones, J. Liu and B. Yoshida, Chaos, Complexity, and Random Matrices , JHEP 11 (2017) 048 [ 1706.05400 ] .
- [ 55 ] D. Chowdhury and B. Swingle, Onset of many-body chaos in the O ( N ) model , Phys. Rev. D 96 (2017), no. 6, 065005 [ 1703.02545 ] .
- [ 56 ] V . Khemani, D. A. Huse and A. Nahum, Velocity-dependent Lyapunov exponents in many-body quantum, semiclassical, and classical chaos , Phys. Rev. B 98 (2018), no. 14, 144304 [ 1803.05902 ] .
- [ 57 ] A. Seshadri, V . Madhok and A. Lakshminarayan, Tripartite mutual information, entanglement, and scrambling in permutation symmetric systems with an application to quantum chaos , Phys. Rev. E 98 (2018), no. 5, 052205 [ 1806.00113 ] .
- [ 58 ] K. Hashimoto, K. Murata and R. Yoshii, Out-of-time-order correlators in quantum mechanics , JHEP 10 (2017) 138 [ 1703.09435 ] .
- [ 59 ] T. Ali, A. Bhattacharyya, S. S. Haque, E. H. Kim, N. Moynihan and J. Murugan, Chaos and Complexity in Quantum Mechanics , Phys. Rev. D 101 (2020), no. 2, 026021 [ 1905.13534 ] .
- [ 60 ] A. Bhattacharyya, W . Chemissany, S. S. Haque, J. Murugan and B. Yan, The Multi-faceted Inverted Harmonic Oscillator: Chaos and Complexity , SciPost Phys. Core 4 (2021) 002 [ 2007.01232 ] .
- [ 61 ] S. Sachdev and J. Ye, Gapless spin-fluid ground state in a random quantum Heisenberg magnet. , Physical review letters 70 21 (1992) 3339-3342.
- [ 62 ] P . Di Francesco, P . H. Ginsparg and J. Zinn-Justin, 2-D Gravity and random matrices , Phys. Rept. 254 (1995) 1-133 [ hep-th/9306153 ] .

- [ 63 ] D. A. Roberts and D. Stanford, Two-dimensional conformal field theory and the butterfly effect , Phys. Rev. Lett. 115 (2015), no. 13, 131603 [ 1412.5123 ] .
- [ 64 ] J. Maldacena, S. H. Shenker and D. Stanford, A bound on chaos , JHEP 08 (2016) 106 [ 1503.01409 ] .
- [ 65 ] A. Kitaev and S. J. Suh, The soft mode in the Sachdev-Ye-Kitaev model and its gravity dual , JHEP 05 (2018) 183 [ 1711.08467 ] .
- [ 66 ] A. M. García-García and J. J. M. Verbaarschot, Spectral and thermodynamic properties of the Sachdev-Ye-Kitaev model , Phys. Rev. D 94 (2016), no. 12, 126010 [ 1610.03816 ] .
- [ 67 ] K. Papadodimas and S. Raju, Local Operators in the Eternal Black Hole , Phys. Rev. Lett. 115 (2015), no. 21, 211601 [ 1502.06692 ] .
- [ 68 ] G. Sárosi, AdS 2 holography and the SYK model , PoS Modave2017 (2018) 001 [ 1711.08482 ] .
- [ 69 ] J. S. Cotler, G. Gur-Ari, M. Hanada, J. Polchinski, P . Saad, S. H. Shenker, D. Stanford, A. Streicher and M. Tezuka, Black Holes and Random Matrices , JHEP 05 (2017) 118 [ 1611.04650 ] , [ Erratum: JHEP 09, 002 (2018) ] .
- [ 70 ] V . Balasubramanian, B. Craps, B. Czech and G. Sárosi, Echoes of chaos from string theory black holes , JHEP 03 (2017) 154 [ 1612.04334 ] .
- [ 71 ] C. Krishnan, S. Sanyal and P . N. Bala Subramanian, Quantum Chaos and Holographic Tensor Models , JHEP 03 (2017) 056 [ 1612.06330 ] .
- [ 72 ] E. Dyer and G. Gur-Ari, 2D CFT Partition Functions at Late Times , JHEP 08 (2017) 075 [ 1611.04592 ] .
- [ 73 ] V . Jahnke, Recent developments in the holographic description of quantum chaos , Adv. High Energy Phys. 2019 (2019) 9632708 [ 1811.06949 ] .
- [ 74 ] N. R. Hunter-Jones, Chaos and Randomness in Strongly-Interacting Quantum Systems. , Dissertation (Ph.D.), California Institute of Technology. 52 (2018) 1-4.
- [ 75 ] A. Altland, B. Post, J. Sonner, J. van der Heijden and E. P . Verlinde, Quantum chaos in 2D gravity , SciPost Phys. 15 (2023), no. 2, 064 [ 2204.07583 ] .
- [ 76 ] A. Bhattacharyya, W . Chemissany, S. Shajidul Haque and B. Yan, Towards the web of quantum chaos diagnostics , Eur. Phys. J. C 82 (2022), no. 1, 87 [ 1909.01894 ] .
- [ 77 ] J. Kudler-Flam, L. Nie and S. Ryu, Conformal field theory and the web of quantum chaos diagnostics , JHEP 01 (2020) 175 [ 1910.14575 ] .
- [ 78 ] T. Zhou and B. Swingle, Operator growth from global out-of-time-order correlators , Nature Commun. 14 (2023), no. 1, 3411 [ 2112.01562 ] .
- [ 79 ] B. Swingle, Unscrambling the physics of out-of-time-order correlators , Nature Phys. 14 (2018), no. 10, 988-990.
- [ 80 ] S. H. Shenker and D. Stanford, Black holes and the butterfly effect , JHEP 03 (2014) 067 [ 1306.0622 ] .
- [ 81 ] D. Stanford, Many-body chaos at weak coupling , JHEP 10 (2016) 009 [ 1512.07687 ] .
- [ 82 ] T. G. Mertens and G. J. Turiaci, Solvable models of quantum black holes: a review on Jackiw-Teitelboim gravity , Living Rev. Rel. 26 (2023), no. 1, 4 [ 2210.10846 ] .

- [ 83 ] S. Xu and B. Swingle, Scrambling Dynamics and Out-of-Time-Ordered Correlators in Quantum Many-Body Systems , PRX Quantum 5 (2024), no. 1, 010201 [ 2202.07060 ] .
- [ 84 ] I. García-Mata, R. A. Jalabert and D. A. Wisniacki, Out-of-time-order correlators and quantum chaos , Scholarpedia 18 (2023) 55237 [ 2209.07965 ] .
- [ 85 ] Y. Kusuki and M. Miyaji, Entanglement Entropy, OTOC and Bootstrap in 2D CFTs from Regge and Light Cone Limits of Multi-point Conformal Block , JHEP 08 (2019) 063 [ 1905.02191 ] .
- [ 86 ] P . Caputa, Y. Kusuki, T . Takayanagi and K. Watanabe, Out-of-Time-Ordered Correlators in ( T 2 ) n / Ζ n , Phys. Rev. D 96 (2017), no. 4, 046020 [ 1703.09939 ] .
- [ 87 ] P . Caputa, T. Numasawa and A. Veliz-Osorio, Out-of-time-ordered correlators and purity in rational conformal field theories , PTEP 2016 (2016), no. 11, 113B06 [ 1602.06542 ] .
- [ 88 ] B. Craps, S. Khetrapal and C. Rabideau, Chaos in CFT dual to rotating BTZ , JHEP 11 (2021) 105 [ 2107.13874 ] .
- [ 89 ] S. Das, B. Ezhuthachan, A. Kundu, S. Porey, B. Roy and K. Sengupta, Out-of-Time-Order correlators in driven conformal field theories , JHEP 08 (2022) 221 [ 2202.12815 ] .
- [ 90 ] Y. Sekino and L. Susskind, Fast Scramblers , JHEP 10 (2008) 065 [ 0808.2096 ] .
- [ 91 ] R. H. Poghossian, Structure constants in the N = 1 superLiouville field theory , Nucl. Phys. B 496 (1997) 451-464 [ hep-th/9607120 ] .
- [ 92 ] A. Artemev and V . Belavin, Torus one-point correlation numbers in minimal Liouville gravity , JHEP 02 (2023) 116 [ 2210.14568 ] .
- [ 93 ] E. D'Hoker and D. H. Phong, The Geometry of String Perturbation Theory , Rev. Mod. Phys. 60 (1988) 917.
- [ 94 ] A. Borel and J.-P . Serre, Le théorème de Riemann-Roch , Bulletin de la Société Mathématique de France 86 (1958) 97-136.
- [ 95 ] L. Baulieu and M. P . Bellon, Beltrami Parametrization and String Theory , Phys. Lett. B 196 (1987) 142-150.
- [ 96 ] H. Verlinde, Conformal field theory, two-dimensional quantum gravity and quantization of Teichmüller space , Nuclear Physics B 337 (1990), no. 3, 652-680.
- [ 97 ] K. Alkalaev and V . Belavin, Large-c superconformal torus blocks , JHEP 08 (2018) 042 [ 1805.12585 ] .
- [ 98 ] C. Grosche, Selberg Supertrace Formula for Superriemann Surfaces, Analytic Properties of Selberg Superzeta Functions and Multiloop Contributions for the Fermionic String , Commun. Math. Phys. 133 (1990) 433-486.
- [ 99 ] A. Dei, B. Knighton, K. Naderi and S. Sethi, Tensionless AdS 3 / CFT 2 and Single Trace T T , 2408.00823 .
- [ 100 ] P . H. Ginsparg, APPLIED CONFORMAL FIELD THEORY , in Les Houches Summer School in Theoretical Physics: Fields, Strings, Critical Phenomena . 9, 1988. hep-th/9108028 .
- [ 101 ] L. Eberhardt, Off-shell Partition Functions in 3d Gravity , Commun. Math. Phys. 405 (2024), no. 3, 76 [ 2204.09789 ] .

- [ 102 ] S. He, Conformal bootstrap to Rényi entropy in 2D Liouville and super-Liouville CFTs , Phys. Rev. D 99 (2019), no. 2, 026005 [ 1711.00624 ] .
- [ 103 ] B. Ponsot and J. Teschner, Liouville bootstrap via harmonic analysis on a noncompact quantum group , hep-th/9911110 .
- [ 104 ] M. Srednicki, Thermal fluctuations in quantized chaotic systems , J. Phys. A 29 (1996) L75-L79 [ chao-dyn/9511001 ] .
- [ 105 ] J. M. Deutsch, Quantum statistical mechanics in a closed system , Phys. Rev. A 43 (Feb, 1991) 2046-2049.
- [ 106 ] M. Rigol, V . Dunjko and M. Olshanii, Thermalization and its mechanism for generic isolated quantum systems , Nature 452 (2007) 854-858.
- [ 107 ] N. Benjamin, H. Ooguri, S.-H. Shao and Y. Wang, Light-cone modular bootstrap and pure gravity , Phys. Rev. D 100 (2019), no. 6, 066029 [ 1906.04184 ] .
- [ 108 ] P . Fleig, H. P . A. Gustafsson, A. Kleinschmidt and D. Persson, Eisenstein series and automorphic representations: With Applications in String Theory , vol. 176. Cambridge University Press, 6, 2018.
- [ 109 ] Y.-S. Myung, CORRELATION FUNCTION FOR N = 1 SUPERCONFORMAL MODELS ON SUPERTORUS , Phys. Rev. D 40 (1989) 1980.
- [ 110 ] A. Belin, J. de Boer, D. L. Jafferis, P . Nayak and J. Sonner, Approximate CFTs and Random Tensor Models , 2308.03829 .
- [ 111 ] J. M. Maldacena and L. Maoz, Wormholes in AdS , JHEP 02 (2004) 053 [ hep-th/0401024 ] .
- [ 112 ] K. B. Alkalaev and V . A. Belavin, Holographic duals of large-c torus conformal blocks , JHEP 10 (2017) 140 [ 1707.09311 ] .
- [ 113 ] P . Suchanek, Elliptic recursion for 4-point superconformal blocks and bootstrap in N = 1 SLFT , JHEP 02 (2011) 090 [ 1012.2974 ] .
- [ 114 ] L. Hadasz, Z. Jaskolski and P . Suchanek, Recursion representation of the Neveu-Schwarz superconformal block , JHEP 03 (2007) 032 [ hep-th/0611266 ] .
- [ 115 ] A. Blommaert, T. G. Mertens and H. Verschelde, The Schwarzian Theory - A Wilson Line Perspective , JHEP 12 (2018) 022 [ 1806.07765 ] .
- [ 116 ] D. Chorazkiewicz and L. Hadasz, Braiding and fusion properties of the Neveu-Schwarz super-conformal blocks , JHEP 01 (2009) 007 [ 0811.1226 ] .
- [ 117 ] S. Ferrara, A. F . Grillo, G. Parisi and R. Gatto, Covariant expansion of the conformal four-point function , Nucl. Phys. B 49 (1972) 77-98 [ Erratum: Nucl.Phys.B 53, 643-643 (1973) ] .
- [ 118 ] L. Iliesiu, F . Kos, D. Poland, S. S. Pufu, D. Simmons-Duffin and R. Yacoby, Bootstrapping 3D Fermions , JHEP 03 (2016) 120 [ 1508.00012 ] .
- [ 119 ] K. Alkalaev and S. Mandrygin, Torus shadow formalism and exact global conformal blocks , JHEP 11 (2023) 157 [ 2307.12061 ] .
- [ 120 ] V . Rosenhaus, Multipoint Conformal Blocks in the Comb Channel , JHEP 02 (2019) 142 [ 1810.03244 ] .
- [ 121 ] V . A. Belavin, On the N = 1 super Liouville four-point functions , Nucl. Phys. B 798 (2008) 423-442 [ 0705.1983 ] .

- [ 122 ] B. Eden, P . S. Howe, C. Schubert, E. Sokatchev and P . C. West, Four point functions in N = 4 supersymmetric Yang-Mills theory at two loops , Nucl. Phys. B 557 (1999) 355-379 [ hep-th/9811172 ] .
- [ 123 ] B. U. Eden, P . S. Howe, A. Pickering, E. Sokatchev and P . C. West, Four point functions in N = 2 superconformal field theories , Nucl. Phys. B 581 (2000) 523-558 [ hep-th/0001138 ] .
- [ 124 ] M. Khorrami, A. Aghamohammadi and A. M. Ghezelbash, Logarithmic N = 1 superconformal field theories , Phys. Lett. B 439 (1998) 283-288 [ hep-th/9803071 ] .
- [ 125 ] V . Belavin, J. Ramos Cabezas and B. Runov, Shadow formalism for supersymmetric conformal blocks , 2408.07684 .
- [ 126 ] M. Gerbershagen, Monodromy methods for torus conformal blocks and entanglement entropy at large central charge , JHEP 08 (2021) 143 [ 2101.11642 ] .
- [ 127 ] J. Cotler and K. Jensen, AdS 3 gravity and random CFT , JHEP 04 (2021) 033 [ 2006.08648 ] .
- [ 128 ] A. Bagchi, A. Mehra and P . Nandi, Field Theories with Conformal Carrollian Symmetry , JHEP 05 (2019) 108 [ 1901.10147 ] .
- [ 129 ] A. Bagchi, R. Basu, A. Mehra and P . Nandi, Field Theories on Null Manifolds , JHEP 02 (2020) 141 [ 1912.09388 ] .
- [ 130 ] A. Bagchi, D. Grumiller and P . Nandi, Carrollian superconformal theories and super BMS , JHEP 05 (2022) 044 [ 2202.01172 ] .
- [ 131 ] A. Bagchi, P . Nandi, A. Saha and Zodinmawia, BMS Modular Diaries: Torus one-point function , JHEP 11 (2020) 065 [ 2007.11713 ] .
- [ 132 ] S. Collier, Y . Gobeil, H. Maxfield and E. Perlmutter, Quantum Regge Trajectories and the Virasoro Analytic Bootstrap , JHEP 05 (2019) 212 [ 1811.05710 ] .
- [ 133 ] A. Ghosh, H. Maxfield and G. J. Turiaci, A universal Schwarzian sector in two-dimensional conformal field theories , JHEP 05 (2020) 104 [ 1912.07654 ] .
- [ 134 ] S. Collier, A. Maloney, H. Maxfield and I. Tsiares, Universal dynamics of heavy operators in CFT 2 , JHEP 07 (2020) 074 [ 1912.00222 ] .
- [ 135 ] C. Yan, More on torus wormholes in 3d gravity , JHEP 11 (2023) 039 [ 2305.10494 ] .
- [ 136 ] H. Poghosyan and G. Sarkissian, Comments on fusion matrix in N = 1 super Liouville field theory , Nucl. Phys. B 909 (2016) 458-479 [ 1602.07476 ] .
- [ 137 ] A. B. Zamolodchikov and A. B. Zamolodchikov, Liouville field theory on a pseudosphere , hep-th/0101152 .
- [ 138 ] Y. Nakayama, Liouville field theory: A Decade after the revolution , Int. J. Mod. Phys. A 19 (2004) 2771-2930 [ hep-th/0402009 ] .