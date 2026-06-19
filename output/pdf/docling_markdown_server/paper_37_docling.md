## WHAT IS A GAUSSIAN CHANNEL, AND WHEN IS IT PHYSICALLY IMPLEMENTABLE USING A MULTIPORT INTERFEROMETER?

REPANA DEVENDRA, TIJU CHERIAN JOHN, AND K. SUMESH

Abstract. Quantum Gaussian channels are fundamental models for communication and information processing in continuous-variable quantum systems. This work addresses both foundational aspects and physical implementation pathways for these channels. Firstly, we provide a rigorous, unified framework by formally proving the equivalence of three principal definitions of quantum Gaussian channels prevalent in the literature, consolidating theoretical understanding. Secondly, we investigate the physical realization of these channels using multiport interferometers, a key platform in quantum optics. We focus on the standard parameterization involving matrices X and Y , governed by the condition Y -i ( J -X T JX ) ≥ 0 with J = [ 0 I -I 0 ] . The central research contribution is a precise characterization of the specific pairs ( X,Y ) that correspond to Gaussian channels physically implementable via linear optical multiport interferometers. This characterization bridges the abstract mathematical description with concrete physical architectures. Along the way, we also resolve some questions posed by Parthasarathy [Indian J. Pure Appl. Math. 46, 419-439 (2015)].

Keywords: quantum information, quantum Gaussian channels, multi-port interferometer, linear optical devices, Gaussian states

2020 Mathematics Subject Classification: 81P47, 81V73, 81V80, 46L07

## Contents

| 1.                                                        | Introduction                                              |   2 |
|-----------------------------------------------------------|-----------------------------------------------------------|-----|
| 2.                                                        | Preliminaries                                             |   2 |
| 2.1.                                                      | Symplectic and Orthosymplectic Matrices                   |   4 |
| 2.2.                                                      | Weyl Representation and Bogoliubov Transformations        |   4 |
| 2.3.                                                      | Gaussian States                                           |   5 |
| 3.                                                        | Gaussian Channels                                         |   6 |
| 4.                                                        | Characterization of Linear Optical Channels               |  13 |
| 5.                                                        | Conclusion                                                |  14 |
| Acknowledgment                                            | Acknowledgment                                            |  15 |
| Appendix A. Supplementary Analysis of Existing Literature | Appendix A. Supplementary Analysis of Existing Literature |  15 |
| References                                                | References                                                |  18 |

Department of Mathematics, Indian Institute of Technology Bombay, Mumbai, Maharashtra, 400076, India

Department of Electrical and Computer Engineering, The University of Arizona, Tucson, AZ, 85719, USA

Department of Mathematics, Indian Institute of Technology Madras, Chennai, Tamil Nadu, 600036, India E-mail addresses : r.deva1992@gmail.com, tijucherian@fulbrightmail.org, sumeshkpl@gmail.com . Date : June 10, 2025.

## 1. Introduction

Quantum channels are fundamental for classical and quantum communication systems, describing the dynamics of quantum states in various physical processes, including noise, decoherence, and information transfer [Wat18, Wil13, NC10]. Among quantum channels, Gaussian channels are particularly important in the study of continuous-variable quantum systems. This article focuses on this particular class of quantum channels. They play a fundamental role in areas such as open quantum systems, classical-quantum communication systems like optical fibers, general quantum communication, quantum error correction, and quantum computation, making their theoretical and practical understanding crucial [Ser17, SW17, WPGP + 12, Guh08, HW01]. The mathematical characterization of Gaussian channels is a rich and well-studied area, with multiple definitions appearing in the literature. These definitions include descriptions based on the action on transformation of Gaussian states (or equivalently, mean and covariance matrices), Weyl unitary operators, and Gaussian unitary dilation [Hol19, Ser17, EW07, HW01, Fan76]. Although it is implicitly understood that these definitions are all equivalent, it has not been formally proved in the literature as a unified theorem. This gap in formalization not only leaves the equivalence as an unstated assumption, but also poses challenges for researchers seeking a mathematically rigorous foundation for their work.

Beyond their theoretical significance, Gaussian channels are crucial for the experimental realization of quantum technologies. A key practical question is their implementability using optical devices such as multiport interferometers, which perform linear transformations of optical modes through passive components such as beam splitters and phase shifters [RZBB94]. Although multiport interferometers are widely used in quantum optics, a detailed mathematical framework to determine the conditions under which they can implement a given Gaussian channel remains absent from the literature. This article aims to address these issues with a mathematically oriented treatment that unifies existing knowledge and extends it to new domains.

The article is organized as follows: In Section 2, we introduce the basic objects of the theory. In Section 3 we establish the equivalence of various definitions of the Gaussian channel through rigorous mathematical arguments. The main technical result that aids our proof is Proposition 3.2 which is inspired from [Ser17, page 99]. Section 4 presents the characterization of the physical implementability of Gaussian channels using multiport interferometers. We investigate the parameterization of Gaussian channels using two matrices X and Y satisfying the condition Y -i ( J -X T JX ) ≥ 0 , where J = [ 0 I -I 0 ] , focusing on the conditions under which they can be physically implemented using multiport interferometers. Along the way, we also answer affirmatively some questions asked by Parthasarathy in [Par15].

## 2. Preliminaries

For any Hilbert space H , whether it is finite-dimensional or infinite-dimensional, and regardless of whether it is defined over the field of real or complex numbers, we denote the space of all bounded linear operators on H as B ( H ) . The adjoint of a real linear operator A defined in a real Hilbert space is denoted by A T and that of a complex linear operator A defined in a complex Hilbert space is denoted by A † . In the space of all bounded self-adjoint operators ( A = A † ), as well as in the space of real symmetric ( A = A T ) or complex Hermitian matrices, we define a partial order, denoted by A ≤ B . This ordering is defined by the condition that 〈 z | ( B -A ) | z 〉 ≥ 0 for all vectors z ∈ H . If 0 ≤ B , then we say that B is a positive operator (or matrix , depending on the context). We say that A is a strictly positive operator (or matrix ) if it is positive and invertible. The symbol ≥ is used with obvious meanings arising from the discussion above.

The space of all trace-class operators on H is denoted by T ( H ) . By a state in H we mean a positive trace-class operator ρ ∈ T ( H ) satisfying tr( ρ ) = 1 . If H and K are Hilbert spaces and ρ is a state on H ⊗ K , then tr 2 ( ρ ) ∈ T ( H ) denote the partial trace of ρ over the second factor K . For d 1 , d 2 ∈ N , we define M d 1 × d 2 ( C ) and M d 1 × d 2 ( R ) to be the space of all d 1 × d 2 complex matrices and real matrices, respectively. In particular, M d ( C ) = M d × d ( C ) and M d ( R ) = M d × d ( R ) .

Any vector z ∈ C d (or R d ) is represented as a column vector z = [ z 1 , z 2 , . . . , z d ] T in the standard orthonormal basis of C d (or R d ). The round bracket ( z 1 , z 2 , . . . , z d ) is often used to refer to the column vector z . For a vector z = ( z 1 , z 2 , . . . , z d ) ∈ C d we define ¯ z := (¯ z 1 , ¯ z 2 , . . . , ¯ z d ) , where ¯ z j denotes the complex conjugate of z j ∈ C . Given z = ( z 1 , z 2 , . . . , z d ) and w = ( w 1 , w 2 , . . . , w d ) in C d we define

$$z ^ { T } w \coloneqq \sum _ { j = 1 } ^ { d } z _ { j } w _ { j } ; \quad \langle z | w \rangle \coloneqq \bar { z } ^ { T } w = \sum _ { j = 1 } ^ { d } \bar { z } _ { j } w _ { j } ; \quad \| z \| \colon = \langle z | z \rangle ^ { 1 / 2 } .$$

We consider C d as a 2 d -dimensional real Hilbert space with Re 〈·|·〉 as the inner product, and as a symplectic space with its standard symplectic form -i Im 〈·|·〉 . A set { z 1 , · · · , z k , w 1 , · · · , w k } ⊆ C d , 1 ≤ k ≤ d is said to be a symplectic set if

$$\text {Im} \left \langle z _ { i } | z _ { j } \right \rangle = 0 = \text {Im} \left \langle w _ { i } | w _ { j } \right \rangle \quad \text {and} \quad \text {Im} \left \langle z _ { i } | w _ { j } \right \rangle = \delta _ { i j } , \quad \forall \, 1 \leq i , j \leq k .$$

If k = d , then a symplectic set will form a basis for the real vector space C d , and in such a case, we call it a symplectic basis . It is well known that any symplectic set can be extended to a symplectic basis [Gos06, Theorem 1.15].

We identify C d with R 2 d as real Hilbert spaces in two different ways. With these identifications, we also discuss the symplectic bases in R 2 d . In the first case, we identify C d = R d + i R d with R 2 d = R d ⊕ R d via the identification z = x + i y ↦→ ( x , y ) . Under this identification,

we realize an element A + iB of M d ( C ) = M d ( R ) + iM d ( R ) as the element [ A -B B A ] of M 2 d ( R ) = M 2 ( M d ( R )) . In particular, -iI d ∈ M d ( C ) corresponds to the block matrix

$$J _ { 2 d } \colon = \begin{bmatrix} 0 & I _ { d } \\ - I _ { d } & 0 \end{bmatrix} \in M _ { 2 d } ( \mathbb { R } ) ,$$

where I d is the identity matrix of size d × d . Note that J 2 d is invertible with the inverse J -1 2 d = J T 2 d = -J 2 d . In the second case, we write d = d 1 + d 2 , and write C d = C d 1 ⊕ C d 2 = R 2 d 1 ⊕ R 2 d 2 via the identification

$$( x _ { 1 } + i y _ { 1 } ) \oplus ( x _ { 2 } + i y _ { 2 } ) & \mapsto ( x _ { 1 } , y _ { 1 } , x _ { 2 } , y _ { 2 } ) , \quad \forall \, x _ { j } , y _ { j } \in \mathbb { R } ^ { d _ { j } } , j = 1 , 2 .$$

Under this identification, given A i,j , B i,j ∈ M d i × d j ( R ) we identify

$$M _ { d } ( \mathbb { C } ) \ni \begin{bmatrix} A _ { 1 1 } + i B _ { 1 1 } & A _ { 1 2 } + i B _ { 1 2 } \\ A _ { 2 1 } + i B _ { 2 1 } & A _ { 2 2 } + i B _ { 2 2 } \end{bmatrix} & \mapsto \begin{bmatrix} A _ { 1 1 } & - B _ { 1 1 } & A _ { 1 2 } & - B _ { 1 2 } \\ B _ { 1 1 } & A _ { 1 1 } & B _ { 1 2 } & A _ { 1 2 } \\ A _ { 2 1 } & - B _ { 2 1 } & A _ { 2 2 } & - B _ { 2 2 } \\ B _ { 2 1 } & A _ { 2 1 } & B _ { 2 2 } & A _ { 2 2 } \end{bmatrix} \in M _ { 2 d } ( \mathbb { R } ) .$$

In particular, -iI d ∈ M d ( C ) corresponds to the block matrix J 2 d 1 ⊕ J 2 d 2 . Note that, under both identifications, the adjoint of a complex matrix corresponds to the transpose of its identification.

- 2.1. Symplectic and Orthosymplectic Matrices. By a symplectic transformation of C d we mean a real linear operator L on C d that preserves the standard symplectic form, i.e.,

$$I m \left \langle L u | L v \right \rangle = I m \left \langle u | v \right \rangle \quad \forall \, u , v \in \mathbb { C } ^ { d } .$$

Now, fix an identification of C d with R 2 d , as described in the previous section. This identification allows us to represent the real linear transformation L as a 2 d × 2 d real matrix (again denoted as L ). Consider a specific J ∈ { J 2 d , J 2 d 1 ⊕ J 2 d 2 } , where d = d 1 + d 2 . It is important to note that z T J z ′ = Im 〈 z | z ′ 〉 for all z , z ′ ∈ C d = R 2 d . Therefore, the equation (1) is equivalent to stating that L T JL = J . The elements of the set

$$S p ( 2 d , J ) \colon = \{ L \in M _ { 2 d } ( \mathbb { R } ) \colon L ^ { T } J L = J \}$$

are called J -symplectic matrices. A J -symplectic matrix that is also orthogonal is called a J -orthosymplectic matrix. The set Sp (2 d, J ) forms a group under multiplication, called J -symplectic group . Clearly, J ∈ Sp (2 d, J ) . Every J -symplectic matrix L has determinant 1 , and its inverse is given by L -1 = J T L T J . Note also that L ∈ Sp (2 d, J ) implies L T ∈ Sp (2 d, J ) . A J 2 d -symplectic matrix and a J 2 d -orthosymplectic matrix are simply called a symplectic matrix and an orthosymplectic matrix, respectively. Note that if L = [ u 1 u 2 · · · u 2 d ] ∈ M 2 d ( R ) and J = [ J ik ] ∈ M 2 d ( R ) , then

$$L \in S p ( 2 d , J ) \Longleftrightarrow \mathbf u _ { i } ^ { T } J \mathbf u _ { k } = J _ { i k } , \quad \forall \, 1 \leq i , k \leq 2 d .$$

Consequently, a matrix L = [ u 1 , · · · , u d , v 1 , · · · , v d ] ∈ M 2 d ( R ) is a symplectic if and only if its columns form a symplectic basis.

## 2.2. Weyl Representation and Bogoliubov Transformations. The symmetric Fock space over C d is defined by

$$\Gamma ( \mathbb { C } ^ { d } ) \colon = \bigoplus _ { k = 0 } ^ { \infty } ( \mathbb { C } ^ { d } ) ^ { \mathbb { S } ^ { k } } ,$$

where ( C d ) s ⃝ k is the k -times symmetric tensor product of C d (see [Par92, Chapter 2] for details). For v ∈ C d , the exponential vector | e ( v ) 〉 is defined as

$$| e ( v ) \rangle \colon = \bigoplus _ { k = 0 } ^ { \infty } \frac { v ^ { \otimes ^ { k } } } { \sqrt { k ! } } ,$$

where v ⊗ 0 := 1 ∈ C . The span of exponential vectors forms a dense subset of Γ( C d ) . For u ∈ C d , the Weyl unitary operator , W ( u ) is the unique unitary operator on Γ( C d ) satisfying

$$W ( u ) \, | e ( v ) \rangle = \exp \left \{ - \frac { 1 } { 2 } \| u \| ^ { 2 } - \langle u | v \rangle \right \} | e ( u + v ) \rangle \, , \quad \forall \, v \in \mathbb { C } ^ { d } .$$

The adjoint of W ( u ) is given by W ( u ) † = W ( -u ) . The Weyl unitary operators satisfy the Weyl form of the the canonical commutation relations :

$$W ( u ) W ( v ) & = \exp \{ - i \, I m \, \langle u | v \rangle \} W ( u + v ) , \quad \forall \, u , v \in \mathbb { C } ^ { d } ; \\ W ( u ) W ( v ) & = \exp \{ - 2 i \, I m \, \langle u | v \rangle \} W ( v ) W ( u ) , \quad \forall \, u , v \in \mathbb { C } ^ { d } .$$

$$-$$

The map u ↦→ W ( u ) , u ∈ C d is called the Weyl representation of the additive group C d . Now write d = d 1 + d 2 , where d 1 , d 2 ∈ N . Then C d = C d 1 ⊕ C d 2 , and the map given by | e ( v 1 ⊕ v 2 ) 〉 ↦→ | e ( v 1 ) 〉 ⊗ | e ( v 2 ) 〉 , for all v 1 ∈ C d 1 , v 2 ∈ C d 2 extends to a Hilbert space isomorphism between Γ( C d ) and Γ( C d 1 ) ⊗ Γ( C d 2 ) . Under this isomorphism, we identify these two Fock spaces and write Γ( C d ) = Γ( C d 1 ) ⊗ Γ( C d 2 ) and we have W ( u 1 ⊕ u 2 ) = W ( u 1 ) ⊗ W ( u 2 ) , for all u 1 ∈ C d 1 , u 2 ∈ C d 2 called the factorizability of the Weyl representation. Finally, the map u ↦→ W ( u ) , u ∈ C d is a strongly continuous, projective, factorizable and irreducible unitary representation of the additive abelian group C d .

Another important class of unitary operators we need in this article consists of the so called Bogoliubov transformations on Γ( C d ) . Given a symplectic transformation L on C d , there exists a unique unitary Γ( L ) on Γ( C d ) , called the Bogoliubov unitary at L , satisfying Γ( L ) W ( u )Γ( L ) † = W ( L u ) , and 〈 e (0) | Γ( L ) | e (0) 〉 &gt; 0 . In this case, we have Γ( L ) † = Γ( L -1 ) . We refer the reader to [Par92, Chapter 2] and [JP21, Section IV] for more details on the topics mentioned in this sub section.

2.3. Gaussian States. In this section, we define Gaussian states and describe their properties which we need in a basis independent way. This will help us provide rigorous proofs later.

Definition 2.1. Let ρ be a state on Γ( C d ) . Then the map ̂ ρ : C d → C defined by

(3)

is called the quantum characteristic function of ρ . If there exist a vector m ∈ C d and a real linear operator S on C d such that

$$\widehat { \rho } ( z ) = \exp \left \{ - i \, R e \, \langle m | z \rangle - \frac { 1 } { 2 } \, R e \, \langle z | S | z \rangle \right \} , \quad \forall \, z \in \mathbb { C } ^ { d } ,$$

then ρ is called a d -mode quantum Gaussian state or simply a Gaussian state . In this case, the pair ( m , S ) is unique; the vector m is called the mean vector and S is called the covariance operator of the Gaussian state ρ ; and we write ρ = ρ ( m ,S ) .

Let ρ be a Gaussian state with mean vector m and covariance operator S . If V denotes an identification of C d with R 2 d as described in Section 2, then the quantum characteristic function of ρ can be considered as the map ̂ ρ : R 2 d → C given by

$$\widehat { \rho } ( V z ) = \exp \left \{ - i ( V m ) ^ { T } ( V z ) - \frac { 1 } { 2 } ( V z ) ^ { T } ( V S V ^ { T } ) ( V z ) \right \} , \quad \forall \, z \in \mathbb { C } ^ { d } ,$$

where V SV T ∈ M 2 d ( R ) . When the identification is clear from the context, we abuse the notation and write m ∈ R 2 d and S ∈ M 2 d ( R ) . Furthermore, an arbitrary matrix S ∈ M 2 d ( R ) is the covariance matrix of a Gaussian state if and only if it belongs to the set

$$\mathcal { C M } ( d ) \colon = \{ A \in M _ { 2 d } ( \mathbb { R } ) \, \colon A + i J \geq 0 \} ,$$

where J is taken as J 2 d or J 2 d 1 ⊕ J 2 d 2 according to the identification we have chosen. For more details on quantum Gaussian states, we refer to [Par10], and for the basis-independent description of Gaussian states, see [Joh18]. The following proposition is a consequence of the definitions.

Proposition 2.2. Let ρ = ρ ( m ,S ) be a Gaussian state on Γ( C d ) . If u ∈ C d and L is a symplectic transformation of C d , then

$$W ( \mathbf u ) \Gamma ( L ) \rho _ { ( \mathbf m , S ) } \Gamma ( L ) ^ { \dagger } W ( \mathbf u ) ^ { \dagger } = \rho _ { ( ( L ^ { - 1 } ) ^ { T } \mathbf m - i 2 \mathbf u , ( L ^ { - 1 } ) ^ { T } S L ^ { - 1 } ) } .$$

In particular, if L is a unitary operator then

$$W ( \mathbf u ) \Gamma ( L ) \rho _ { ( \mathbf m , S ) } \Gamma ( L ) ^ { \dagger } W ( \mathbf u ) ^ { \dagger } = \rho _ { ( L \mathbf m - i 2 \mathbf u , L S L ^ { T } ) } .$$

Remark 2.3. Let ρ = ρ ( m ,S ) be a Gaussian state on Γ( C d ) . If u ∈ R 2 d and L ∈ Sp (2 d, J ) , then

$$W ( \mathbf u ) \Gamma ( L ) \rho _ { ( m , S ) } \Gamma ( L ) ^ { \dagger } W ( \mathbf u ) ^ { \dagger } = \rho _ { ( ( L ^ { - 1 } ) ^ { T } m + 2 J \mathbf u , ( L ^ { - 1 } ) ^ { T } S L ^ { - 1 } ) } .$$

In particular, if L is a J -orthosymplectic matrix then

$$W ( u ) \Gamma ( L ) \rho _ { ( \mathfrak { m } , S ) } \Gamma ( L ) ^ { \dagger } W ( u ) ^ { \dagger } = \rho _ { ( L \mathfrak { m } + 2 J u , L S L ^ { T } ) } .$$

Definition 2.4. A unitary operator U on Γ( C d ) is called a Gaussian unitary operator (or Gaussian symmetry ) if UρU † is a Gaussian state for every Gaussian state ρ on Γ( C d ) .

Proposition 2.5 ([Par13, Joh18]) . Let U be a unitary operator on Γ( C d ) . Then U is a Gaussian unitary operator if and only if U = λW ( u )Γ( L ) for some λ ∈ C with | λ | = 1 , u ∈ C d and some symplectic transformation L on C d .

## 3. Gaussian Channels

This section discusses quantum channels defined on Fock spaces. Mathematically, quantum channels are represented by trace-preserving completely positive maps (in the Schrödinger picture), or equivalently, unital completely positive maps (in the Heisenberg picture). To ensure clarity, we will provide a brief overview of each term used in this context.

A linear map Φ : B (Γ( C d )) → B (Γ( C d )) is said to be completely positive (CP) if the positivity condition ∑ n j,k =1 B ∗ j Φ( A ∗ j A k ) B k ≥ 0 is satisfied for any finite subsets { A j } n j =1 , { B j } n j =1 ⊆ B (Γ( C d )) and n ∈ N . We refer to [Sti55, Pau02] for more details on CP maps and its properties. Given any bounded (with respect to the trace-norm) linear map Ψ : T (Γ( C d )) → T (Γ( C d )) there exists a unique bounded (with respect to the operator-norm) linear map Ψ ∗ : B (Γ( C d )) → B (Γ( C d )) , called the dual of Ψ , such that tr(Ψ( ϱ ) A ) = tr( ϱ Ψ ∗ ( A )) for all ϱ ∈ T (Γ( C d )) and A ∈ B (Γ( C d )) . The map Ψ ∗ is necessarily a normal map, i.e., continuous with respect to the σ -weak (or weak ∗ ) topology on B (Γ( C d )) . The map Ψ is said to be completely positive if Ψ ∗ is a completely positive map. Furthermore, Ψ is trace-preserving (i.e., tr(Ψ( ϱ )) = tr( ϱ ) for all ϱ ∈ T (Γ( C d )) ) if and only if Ψ ∗ is unital (i.e., Ψ ∗ ( I ) = I , where I is the identity map of Γ( C d ) ). A trace-preserving completely positive map Ψ : T (Γ( C d )) → T (Γ( C d )) is called a quantum channel on Γ( C d ) . According to the Stinespring representation theorem [Sti55, Att13], if Ψ is a quantum channel on Γ( C d ) , then there exists a separable Hilbert space K , a unitary operator U on C d ⊗K , and a state ρ K on K such that the channel acts on an operator ϱ ∈ T (Γ( C d )) as follows:

$$\Psi ( \varrho ) = t r _ { 2 } ( U ( \varrho \otimes \rho _ { K } ) U ^ { \dagger } ) .$$

In this section, we aim to characterize all quantum channels that map Gaussian states to Gaussian states.

$$\text {Proposition} \, 3 . 1 . \, \text { Let } d = d _ { 1 } + d _ { 2 } , \, \mathbf u = \mathbf u _ { 1 } \oplus \mathbf u _ { 2 } \in \mathbb { R } ^ { 2 d _ { 1 } } \oplus \mathbb { R } ^ { 2 d _ { 2 } } \text { and } L \in S p ( 2 d , J ) \text { with } L ^ { - 1 } = \\ \begin{bmatrix} L _ { 1 1 } & L _ { 1 2 } \\ L _ { 2 1 } & L _ { 2 2 } \end{bmatrix} , L _ { J j } \in M _ { 2 d _ { j } } ( \mathbb { R } ) , \, j = 1 , 2 . \, \text { Then the map } \Psi \colon \mathcal { I } ( \mathbb { C } ^ { d _ { 1 } } ) \to \mathcal { I } ( \mathbb { C } ^ { d _ { 1 } } ) \text { defined by } \end{bmatrix}$$

$$\Psi ( \varrho ) \coloneqq & \text {tr} _ { 2 } \left ( W ( \mathbf u ) \Gamma ( L ) ( \varrho \otimes \rho _ { ( 0 , I _ { d _ { 2 } } ) } ) ( W ( \mathbf u ) \Gamma ( L ) ) ^ { \dagger } \right ) , \quad \forall \, \varrho \in \mathcal { T } ( \Gamma _ { s } ( \mathbb { C } ^ { d _ { 1 } } ) ) ,$$

$$1 = \\ ( 6 )$$

is a quantum channel that maps Gaussian states to Gaussian states. Indeed,

$$\Psi ( \rho _ { ( m , S ) } ) = \rho _ { ( L _ { 1 1 } ^ { T } \mathfrak { m } + 2 J _ { 2 d _ { 1 } } \mathfrak { u } _ { 1 } , L _ { 1 1 } ^ { T } S L _ { 1 1 } + L _ { 2 1 } ^ { T } L _ { 2 1 } ) } ,$$

for every Gaussian states ρ ( m ,S ) on Γ( C d 1 ) .

Proof. Since U := W ( u )Γ( L ) is a unitary, by Stinespring representation theorem, we know that Ψ is a quantum channel. Further, given any Gaussian state ρ ( m ,S ) the quantum characteristic function of Ψ( ρ m ,S ) at any v ∈ R 2 d 1 is given by

$$\text {that $\varphi$ is a quantum channel. For whether, given any Gaussian state $\varphi(m,s)$, the quantum charac-
teristic function of $\varphi(m,s)$ at any v \in \mathbb { R } ^ { 2 d _ { 1 } } is given by & \\ \widehat { \Psi ( \rho ( m , s ) ( v ) = \text {tr} \left ( \text {wr} ( u ) \Gamma ( L ) ( \rho ( m , s ) \otimes \rho ( 0 , I _ { 2 } ) ) ( W ( u ) \Gamma ( L ) ) ^ { \dagger } \right ) W ( v ) ) \\ = & \text {tr} \left ( \left ( \rho ( m , S ) \otimes \rho ( 0 , I _ { 2 } ) \right ) \Gamma ( L ) ^ { \dagger } W ( - u ) W ( v \oplus 0 ) W ( u ) \Gamma ( L ) \right ) \\ = & \text {tr} \left ( \left ( \rho ( m , S ) \otimes \rho ( 0 , I _ { 2 } ) \right ) \Gamma ( L ^ { - 1 } ) W ( v \oplus 0 ) \Gamma ( L ^ { - 1 } ) ^ { \dagger } \right ) \exp \{ 2 i \Im \left ( u _ { 1 } | v \right ) \} \\ = & \text {tr} \left ( \left ( \rho ( m , S ) \otimes \rho ( 0 , I _ { 2 } ) \right ) W ( L ^ { - 1 } ( v \oplus 0 ) ) \right ) \exp \{ 2 i u _ { 1 } ^ { T } J _ { 2 d _ { 1 } } v \} \\ = & \text {tr} \left ( \left ( \rho ( m , S ) \otimes \rho ( 0 , I _ { 2 } ) \right ) W ( L _ { 1 1 } v \oplus L _ { 2 1 } v ) \right ) \exp \{ 2 i u _ { 1 } ^ { T } J _ { 2 d _ { 1 } } v \} \\ = & \text {tr} \left ( \rho ( m , S ) W ( L _ { 1 1 } v ) \right ) \text {tr} \left ( \rho ( 0 , I _ { 2 } ) W ( L _ { 2 1 } v ) \right ) \exp \{ 2 i u _ { 1 } ^ { T } J _ { 2 d _ { 1 } } v \} \\ = & \exp \left \{ - i \left ( L _ { 1 1 } ^ { T } m + 2 J _ { 2 d _ { 1 } } u \right ) ^ { T } v - \frac { 1 } { 2 } v ^ { T } \left ( L _ { 1 1 } ^ { T } S L _ { 1 1 } + L _ { 2 1 } L _ { 2 1 } \right ) v \right \} . \\ \text {Since } v \in \mathbb { R } ^ { 2 d _ { 1 } } \text { is arbitrary} \text { we conclude that } \Psi ( \rho ( m , S ) ) \text { is a Gaussian state with mean } L _ { 1 1 } ^ { T } m + \\ \text {2} \cdot \text {u, and covariant} \text { L} \text {S} _ { L } \text { + } L ^ { T } L _ { 1 } L _ { 2 } \\ = & \prod _ { 1 } \prod _ { 2 } \prod _ { n = 1 } ^ { 2 } \prod _ { k = 1 } ^ { 2 } \prod _ { l = 1 } ^ { 2 } L _ { 1 } L _ { 2 }$$

Since v ∈ R 2 d 1 is arbitrary we conclude that Ψ( ρ ( m ,S ) ) is a Gaussian state with mean L T 11 m + 2 J 2 d 1 u 1 and covariance L T 11 SL 11 + L T 21 L 21 . □

To achieve our main goal, we will first establish some technical results.

Lemma 3.1. Let λ j ∈ [ -1 , 1] for 1 ≤ j ≤ d . Then there exists Q ∈ M 2 d × 4 d ( R ) such that QQ T = I 2 d and

$$Q ( \bigoplus _ { j = 1 } ^ { 2 d } \left [ \begin{smallmatrix} 0 & 1 \\ - 1 & 0 \end{smallmatrix} \right ] ) Q ^ { T } = \bigoplus _ { j = 1 } ^ { d } \left [ \begin{smallmatrix} 0 & \lambda _ { j } \\ - \lambda _ { j } & 0 \end{smallmatrix} \right ] .$$

$$Q ( \theta ) \colon = \begin{bmatrix} \cos \theta & 0 & - \sin \theta & 0 \\ & & & \\ 0 & \cos \theta & 0 & \sin \theta \end{bmatrix} .$$

Then, we have Q ( θ ) Q ( θ ) T = I 2 , and

$$Q ( \theta ) \left ( \bigoplus _ { j = 1 } ^ { 2 } \left [ \begin{matrix} 0 & 1 \\ - 1 & 0 \end{matrix} \right ] \right ) Q ( \theta ) ^ { T } = \begin{bmatrix} 0 & \cos 2 \theta \\ - \cos 2 \theta & 0 \end{bmatrix} .$$

Now, for each 1 ≤ j ≤ d , choose and fix θ j ∈ R be such that cos 2 θ j = λ j . Then Q := ⊕ d j =1 Q ( θ j ) gives the required matrix. □

Corollary 3.1. Let A ∈ M d ( R ) be a positive contraction. Then there exists a matrix Q ∈

$$M _ { 2 d \times 4 d } ( \mathbb { R } ) \text { such that } Q Q ^ { T } = I _ { 2 d } \text { and } Q J _ { 4 d } Q ^ { T } = \begin{bmatrix} 0 & A \\ - A & 0 \end{bmatrix} .$$

Proof. For any θ ∈ R , let Proof. By the spectral theorem we know that A = UDU T for some D ∈ M 2 d ( R ) diagonal and U ∈ M 2 d ( R ) orthogonal. Then

$$\begin{bmatrix} 0 & A \\ - A & 0 \end{bmatrix} = \begin{bmatrix} 0 & U D U ^ { T } \\ - U D U ^ { T } & 0 \end{bmatrix} = \begin{bmatrix} U & 0 \\ 0 & U \end{bmatrix} \begin{bmatrix} 0 & D \\ - D & 0 \end{bmatrix} \begin{bmatrix} U & 0 \\ 0 & U \end{bmatrix} ^ { T } .$$

So it is enough to prove the result for A diagonal, say A = Diag( λ 1 , λ 2 , · · · , λ d ) with λ j ∈ [0 , 1] . Now, by the above Lemma, there exists a matrix Q ∈ M 2 d × 4 d ( R ) such that QQ T = I 2 d and

$$Q ( \bigoplus _ { j = 1 } ^ { 2 d } \left [ \begin{smallmatrix} 0 & 1 \\ - 1 & 0 \end{smallmatrix} \right ] ) Q ^ { T } = \bigoplus _ { j = 1 } ^ { d } \left [ \begin{smallmatrix} 0 & \lambda _ { j } \\ - \lambda _ { j } & 0 \end{smallmatrix} \right ] .$$

By taking conjugations with suitable permutation matrices, we obtain a matrix, again denoted

[ ]

$$\text {by } Q \in M _ { 2 d \times 4 d } ( \mathbb { R } ) \text { such that } Q Q ^ { T } = I _ { 2 d } \text { and } Q J _ { 4 d } Q ^ { T } = \begin{bmatrix} 0 & A \\ - A & 0 \end{bmatrix} .$$

Proposition 3.2. Let X,Y ∈ M 2 d ( R ) . Then the following are equivalent:

$$\text {Proposition} \, 3 . 2 \, \text { Let } X , Y \in M _ { 2 d } ( \mathbb { R } ) . \text { Then the following are equivalent:} \\ ( i ) \text { There exists a } ( J _ { 2 d } \oplus J _ { 2 d ^ { \prime } } ) \text {-symplectic matrix } L & = \begin{bmatrix} X & L _ { 1 2 } \\ L _ { 2 1 } & L _ { 2 1 } \end{bmatrix} \in M _ { 2 ( d + d ^ { \prime } ) } ( \mathbb { R } ) \text { with} \\ L _ { 2 1 } ^ { T } L _ { 2 1 } & = Y , \text { where } L _ { 1 2 } ^ { T } , L _ { 2 1 } \in M _ { 2 d ^ { \prime } \times 2 d } ( \mathbb { R } ) , L _ { 2 2 } \in M _ { 2 d ^ { \prime } } ( \mathbb { R } ) \text { for some } d ^ { \prime } \geq 1 ; \\ ( i i ) \text { } Y + i ( J _ { 2 d } - X ^ { T } J _ { 2 d } X ) \geq 0 ; \\ ( i i i ) \text { } Y - i ( J _ { 2 d } - X ^ { T } J _ { 2 d } X ) \geq 0 . \\ ( i n e a c h o f the a b o w e s t a m p e r i t y ) \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text$$

(In each of the above statements, the matrix Y is necessarily positive.)

Proof. ( i ) ⇒ ( ii ) Suppose there exist L T , L 21 ∈ M 2 d ′ × 2 d ( R ) , L 22 ∈ M 2 d ′ ( R ) such that L T L 21

Y and the matrix L = X L 12 L 21 L 22 ∈ M 2( d + d ′ ) ( R ) is ( J 2 d ⊕ J 2 d ′ )

12 21 = [ ] -symplectic. Then

$$\begin{bmatrix} X & L _ { 1 2 } \\ L _ { 2 1 } & L _ { 2 2 } \end{bmatrix} ^ { T } \begin{bmatrix} J _ { 2 d } & 0 \\ 0 & J _ { 2 d ^ { \prime } } \end{bmatrix} \begin{bmatrix} X & L _ { 1 2 } \\ L _ { 2 1 } & L _ { 2 2 } \end{bmatrix} = \begin{bmatrix} J _ { 2 d } & 0 \\ 0 & J _ { 2 d ^ { \prime } } \end{bmatrix} .$$

By comparing the (1 , 1) -entry of both sides, we obtain the relation

$$L _ { 2 1 } ^ { T } J _ { 2 d ^ { \prime } } L _ { 2 1 } = J _ { 2 d } - X ^ { T } J _ { 2 d } X .$$

Since I 2 d ′ + iJ 2 d ′ ≥ 0 , using the above identity, we get

$$0 \leq L _ { 2 1 } ^ { T } ( I _ { 2 d ^ { \prime } } + i J _ { 2 d ^ { \prime } } ) L _ { 2 1 } = L _ { 2 1 } ^ { T } L _ { 2 1 } + i ( J _ { 2 d } - X ^ { T } J _ { 2 d } X ) = Y + i ( J _ { 2 d } - X ^ { T } J _ { 2 d } X ) .$$

( ii ) ⇒ ( i ) Assume that Y + i ( J 2 d -X T J 2 d X ) ≥ 0 . Then for any z ∈ R 2 d we have

$$0 \leq \langle z | ( Y + i ( J - X ^ { T } J X ) | z \rangle = \langle z | Y | z \rangle + i \, \langle z | ( J - X ^ { T } J X ) | z \rangle \, .$$

This implies that 〈 z | ( J -X T JX ) | z 〉 = 0 and 〈 z | Y | z 〉 ≥ 0 for all z ∈ R 2 d . Therefore Y ≥ 0 . Now we will construct L ∈ M 6 d ( R ) , i.e., d ′ = 2 d . To do so, we proceed by splitting the remainder of the proof into two steps:

Step 1: To show that there exists L 21 ∈ M 4 d × 2 d ( R ) such that L T 21 J 4 d L 21 = J 2 d -X T J 2 d X and L T 21 L 21 = Y . We do this in two cases:

Case 1: Assume that Y is invertible. Then the operator Y -1 2 ( J 2 d -X T J 2 d X ) Y -1 2 is skewsymmetric, and hence by [HJ12, Corollary 2.5.11], there exists a positive diagonal matrix D ∈ M d ( R ) and an orthogonal matrix R ∈ M 2 d ( R ) such that

$$R ^ { T } Y ^ { - \frac { 1 } { 2 } } \left ( J _ { 2 d } - X ^ { T } J _ { 2 d } X \right ) Y ^ { - \frac { 1 } { 2 } } R = \begin{bmatrix} 0 & D \\ - D & 0 \end{bmatrix} .$$

Observe that Y + i ( J 2 d -X T J 2 d X ) ≥ 0 implies that I + iR T Y -1 2 ( J 2 d -X T J 2 d X ) Y -1 2 R ≥ 0 , which further implies I + i [ 0 D -D 0 ] ≥ 0 . Hence D is a positive contraction. Therefore, by

Corollary 3.1, there exists Q ∈ M 2 d × 4 d ( R ) such that QQ T = I 2 d and QJ 4 d Q T = [ 0 D -D 0 ] . Let

L 21 := Q T R T Y 1 2 . Then L T 21 L 21 = Y and

$$L _ { 2 1 } ^ { T } J _ { 4 d } L _ { 2 1 } & = Y ^ { \frac { 1 } { 2 } } R \begin{bmatrix} 0 & D \\ - D & 0 \end{bmatrix} R ^ { T } Y ^ { \frac { 1 } { 2 } } \\ & = Y ^ { \frac { 1 } { 2 } } R R ^ { T } Y ^ { - \frac { 1 } { 2 } } ( J _ { 2 d } - X ^ { T } J _ { 2 d } X ) Y ^ { - \frac { 1 } { 2 } } R R ^ { T } Y ^ { \frac { 1 } { 2 } } \\ & = J _ { 2 d } - X ^ { T } J _ { 2 d } X .$$

Case 2: Suppose Y is not invertible. Note that Y n := Y + 1 n I is positive, invertible and satisfies Y n + i ( J 2 d -X T J 2 d X ) ≥ 0 for all n ≥ 1 . Therefore, by Case 1, there exist orthogonal matrices R n ∈ M 2 d ( R ) and Q n ∈ M 4 d × 2 d ( R ) such that Q n Q T n = I 2 d and L 21 ,n := Q T n R T n Y 1 2 n satisfies

$$( L _ { 2 1 , n } ) ^ { T } L _ { 2 1 , n } = Y _ { n } \quad \text {and} \quad L _ { 2 1 , n } ^ { T } J _ { 4 d } L _ { 2 1 , n } = J _ { 2 d } - X ^ { T } J _ { 2 d } X , \quad \forall \, n \geq 1 .$$

Since both the sets { Q ∈ M 4 d × 2 d ( R ) : QQ T = I } and { R ∈ M 2 d ( R ) : R is orthogonal } are compact, we get a subsequence { Q n k } ⊆ { Q n } and { R n k } ⊆ { R n } such that Q n k converges to Q and R n k converges to R . Note that QQ T = I 2 d and R is orthogonal. Further, L 21 ,n k converges to L 21 := Q T R T Y 1 2 . From the construction L T 21 L 21 = Y and L T 21 J 4 d L 21 = J 2 d -X T J 2 d X .

Step 2: To construct the required matrix L . For all 1 ≤ i ≤ d , let ξ i := ( e i , 0) and η i = (0 , e i ) ∈ R 2 d , where 0 ∈ R d and { e i } d i =1 ⊆ R d is the standard orthonormal basis. In R 2 d ⊕ R 4 d , consider the sets

$$E _ { 1 } = \{ u _ { i } \colon = X \xi _ { i } \oplus L _ { 2 1 } \xi _ { i } \} _ { i = 1 } ^ { d } \ \text { and } \quad E _ { 2 } = \{ v _ { i } \colon = X \eta _ { i } \oplus L _ { 2 1 } \eta _ { i } \} _ { i = 1 } ^ { d } .$$

Note that

$$\begin{bmatrix} X \\ L _ { 2 1 } \end{bmatrix} = \left [ u _ { 1 } \ \ u _ { 2 } \ \cdots \ \ u _ { d } \ \ v _ { 1 } \ \ v _ { 2 } \ \cdots \ \ v _ { d } \right ] .$$

Further, for all 1 ≤ i, k ≤ d we have

$$u _ { i } ^ { T } ( J _ { 2 d } \oplus J _ { 4 d } ) u _ { k } & = ( X \xi _ { i } \oplus L _ { 2 1 } \xi _ { i } ) ^ { T } ( J _ { 2 d } \oplus J _ { 4 d } ) ( X \xi _ { k } \oplus L _ { 2 1 } \xi _ { k } ) \\ & = \xi _ { i } ^ { T } ( X ^ { T } J _ { 2 d } X + L _ { 2 1 } ^ { T } J _ { 4 d } L _ { 2 1 } ) \xi _ { k } \\ & = \xi _ { i } ^ { T } J _ { 2 d } \xi _ { k } \\ & = 0 .$$

Similarly, for all 1 ≤ i, k ≤ d , we see that

$$v _ { i } ^ { T } ( J _ { 2 d } \oplus J _ { 4 d } ) v _ { k } = \eta _ { i } ^ { T } J _ { 2 d } \eta _ { k } = 0 \quad \text {and} \quad \mathbf u _ { i } ^ { T } ( J _ { 2 d } \oplus J _ { 4 d } ) v _ { k } = \xi _ { i } ^ { T } J _ { 2 d } \eta _ { k } = \delta _ { i , k } .$$

Observe that J 2 d ⊕ J 4 d = P T J 6 d P , where P ∈ M 6 d ( R ) is the permutation matrix given by

$$P = \begin{bmatrix} I _ { d } & 0 & 0 & 0 \\ 0 & 0 & I _ { d } & 0 \\ 0 & I _ { 2 d } & 0 & 0 \\ 0 & 0 & 0 & I _ { 2 d } \end{bmatrix} .$$

Then, for all 1 ≤ i, k ≤ d we have

$$( P u _ { i } ) ^ { T } J _ { 6 d } ( P u _ { k } ) & = u _ { i } ^ { T } ( J _ { 2 d } \oplus J _ { 4 d } ) u _ { k } = 0 \\ ( P v _ { i } ) ^ { T } J _ { 6 d } ( P v _ { k } ) & = v _ { i } ^ { T } ( J _ { 2 d } \oplus J _ { 4 d } ) v _ { k } = 0 \\ ( P u _ { i } ) ^ { T } J _ { 6 d } ( P v _ { k } ) & = u _ { i } ^ { T } ( J _ { 2 d } \oplus J _ { 4 d } ) v _ { k } = \delta _ { i k } .$$

Hence, by [Gos06, Theorem 1.15] and (2), there exist vectors { u ′ j } 3 d j = d +1 , { v ′ j } 3 d j = d +1 ⊆ R 6 d such that

$$M \coloneqq \left [ P u _ { 1 } \ \cdots \ P u _ { d } \ u _ { d + 1 } ^ { \prime } \ \cdots \ u _ { 3 d } ^ { \prime } \ P v _ { 1 } \ \cdots \ P v _ { d } \ v _ { d + 1 } ^ { \prime } \ \cdots \ v _ { 3 d } ^ { \prime } \right ] \in M _ { 6 d } ( \mathbb { R } )$$

is a symplectic matrix. Consequently, L := P T MP is a ( J 2 d ⊕ J 4 d ) -symplectic matrix. But

$$i s a \, & \, \text {synthetic matrix} . \, \text {Confusedly, } L \equiv P ^ { \dagger } F \, i s a \, i ( J _ { 2 d } \oplus J _ { 4 d } ) \text {synthetic matrix} . \, \text {But} \\ & \, P ^ { T } M P = \left [ u _ { 1 } \, \cdots \, u _ { d } \, P ^ { T } u _ { d + 1 } ^ { \prime } \, \cdots \, P ^ { T } u _ { 3 d } ^ { \prime } \, v _ { 1 } \, \cdots \, v _ { d } \, P ^ { T } v _ { d + 1 } ^ { \prime } \, \cdots \, P ^ { T } v _ { 3 d } ^ { \prime } \right ] P \\ & \, = \left [ u _ { 1 } \, \cdots \, u _ { d } \, \ v _ { 1 } \, \cdots \, \ v _ { d } \, \ast \, \ast \, \cdots \, \right ] \\ & \, = \left [ \begin{array} { c } X & \ast \\ L _ { 2 1 } & \ast \end{array} \right ] , \\ \text {where} \, & \, \ast ^ { \prime } \, \text {denotes unspecified block matrices} \,$$

where ' ∗ ' denotes unspecified block matrices.

- ( ii ) ⇐⇒ ( iii ) Assume that Z := Y + i ( J 2 d -X T J 2 d X ) ≥ 0 . Then we have that Y ≥ 0 as noticed above. Since J T = -J , the transpose matrix Z T = Y -i ( J 2 d -X T J 2 d X ) ≥ 0 . Conversely, the reverse direction follows in a similar manner. This completes the proof. □

Now we are ready to prove our main theorem.

Theorem 3.1. Let Ψ : T (Γ( C d )) → T (Γ( C d )) be a quantum channel. Then the following are equivalent:

- (i) The channel Ψ maps Gaussian states to Gaussian states;
- (ii) There exist X,Y ∈ M 2 d ( R ) and w ∈ R 2 d such that for every Gaussian state ρ ( m ,S ) , the transformed state Ψ( ρ ( m ,S ) ) is also a Gaussian state with mean X T m + w and covariance X T SX + Y , i.e.,

$$\Psi ( \rho _ { ( m , S ) } ) = \rho _ { ( X ^ { T } m + w , X ^ { T } S X + Y ) } ;$$

- (iii) There exist X,Y ∈ M 2 d ( R ) and w ∈ R 2 d such that the dual map Ψ ∗ : B (Γ( C d )) → B (Γ( C d )) satisfies

$$\Psi ^ { * } ( W ( z ) ) = \exp \left \{ - i w ^ { T } z - \frac { 1 } { 2 } z ^ { T } Y z \right \} W ( X z ) , \ \forall \, z \in \mathbb { R } ^ { 2 d } ;$$

- (iv) There exists a Gaussian unitary operator U on Γ( C d + d ′ ) = Γ( C d ) ⊗ Γ( C d ′ ) , for some d ′ ≥ 1 , such that

$$\Psi ( \varrho ) = \text {tr} _ { 2 } \left ( U ( \varrho \otimes \rho _ { ( 0 , I _ { 2 d ^ { \prime } } ) } ) U ^ { \dagger } \right ) , \quad \forall \, \varrho \in \mathcal { T } ( \Gamma ( \mathbb { C } ^ { d } ) ) ;$$

- (v) The channel id T (Γ( C k )) ⊗ Ψ maps Gaussian states on Γ( C k ⊕ C d ) to Gaussian states for all k ∈ N ∪ { 0 } . (Here Γ( C 0 ) := C .)

In such a case, in both (ii) and (iii), the matrix Y + i ( J 2 d -X T J 2 d X ) ≥ 0 and hence Y ≥ 0 .

Proof. ( i ) = ⇒ ( ii ) Note that a Gaussian state is completely characterized by its mean and covariance matrix. Hence, by assumption, there exist functions α 1 : R 2 d × CM ( d ) → R 2 d and α 2 : R 2 d × CM ( d ) → CM ( d ) such that for every Gaussian state ρ ( m ,S ) , the transformed state Ψ( ρ ( m ,S ) ) is also a Gaussian state with mean α 1 ( m , S ) and covariance α 2 ( m , S ) . The rest of the proof follows from Theorem A.1.

( ii ) = ⇒ ( iv ) Assume that the channel Ψ satisfies (8). Then, by Proposition A.3 in the Appendix, we have Y + i ( J 2 d -X T J 2 d X ) ≥ 0 . Hence, by Proposition (3.2), we get L = [ X L 12 L 21 L 22 ] ∈ Sp (6 d, J 2 d ⊕ J 4 d ) such that L T 21 L 21 = Y . Then U := W ( 1 2 J T 2 d w ⊕ 0)Γ( L -1 ) ∈ Γ( C 3 d ) is a Gaussian unitary, where 0 ∈ R 4 d . Define Ψ ′ : T (Γ( C d )) → T (Γ( C d )) by

$$\Psi ^ { \prime } ( \varrho ) \coloneqq \text {tr} _ { 2 } \left ( U ( \varrho \otimes \rho _ { ( 0 , I _ { 4 d } ) } U ^ { \dagger } ) , \quad \forall \, \varrho \in \mathcal { T } ( \Gamma ( \mathbb { C } ^ { d } ) ) .$$

Then Ψ ′ is a quantum channel. It can be easily verified that

$$t r \left ( \Psi ^ { \prime } ( \rho _ { ( m , S ) } ) W ( z ) \right ) = t r \left ( \Psi ( \rho _ { ( m , S ) } ) W ( z ) \right )$$

for all Gaussian states ρ and z ∈ R 2 d . Hence, we conclude that Ψ ′ = Ψ

( iv ) = ⇒ ( v ) . By the assumption, there exists a Gaussian unitary operator U on Γ( C d + d ) = Γ( C d ) ⊗ Γ( C d ′ ) , for some d ′ ≥ 1 , such that

( m ,S ) . ′

$$\Psi ( \varrho ) = \text {tr} _ { 2 } \left ( U ( \varrho \otimes \rho _ { ( 0 , I _ { 2 d ^ { \prime } } ) } ) U ^ { \dagger } \right ) , \quad \forall \, \varrho \in \mathcal { T } ( \Gamma ( \mathbb { C } ^ { d } ) ) ;$$

Fix k ≥ 1 . We show that there exists Gaussian unitary ˜ U on Γ( C k + d + d ′ ) = Γ( C k + d ) ⊗ Γ( C d ′ ) such that

$$( i d _ { \mathcal { T } ( \Gamma ( \mathbf C ^ { k } ) ) } \otimes \Psi ) ( \widetilde { \rho } ) = t r _ { 2 } \left ( \widetilde { U } ( \widetilde { \rho } \otimes \rho _ { ( 0 , I _ { 2 d ^ { \prime } } ) } ) \widetilde { U } ^ { \dagger } \right ) , \quad \forall \, \widetilde { \rho } \in \mathcal { T } ( \mathbb { C } ^ { k + d } ) ,$$

where tr 2 is the partial trace over the second factor Γ( C d ′ ) . Then, from Proposition 3.1, we conclude that id T (Γ( C k )) ⊗ Ψ maps Gaussian states to Gaussian states. To this end we consider the Gaussian unitary ˜ U := I Γ( C k ) ⊗ U defined on Γ( C k ) ⊗ Γ( C d + d ′ ) = Γ( C k + d + d ′ ) . Then for any T 1 ∈ T (Γ( C k )) and T 2 ∈ T (Γ( C d )) ,

$$tr _ { 2 } \left ( \tilde { U } ( T _ { 1 } \otimes T _ { 2 } \otimes \rho _ { ( 0 , I _ { 2 ^ { d } } ) } ) \tilde { U } ^ { \dagger } \right ) & = \text {tr} _ { 2 } \left ( ( I _ { \Gamma ( \ast ) } \otimes U ) ( T _ { 1 } \otimes T _ { 2 } \otimes \rho _ { ( 0 , I _ { 2 ^ { d } } ) } ) ( I _ { \Gamma ( \mathbb { C } ^ { \ast } ) } \otimes U ) ^ { \dagger } \right ) \\ & = \text {tr} _ { 2 } \left ( T _ { 1 } \otimes U ( T _ { 2 } \otimes \rho _ { ( 0 , I _ { 2 ^ { d } } ) } ) U ^ { \dagger } \right ) \\ & = T _ { 1 } \otimes \text {tr} _ { 2 } \left ( U ( T _ { 2 } \otimes \rho _ { ( 0 , I _ { 2 ^ { d } } ) } ) U ^ { \dagger } \right ) \\ & = ( i d _ { \mathcal { X } } ( \Gamma ( \mathbb { C } ^ { k } ) \otimes \Psi ) ( T _ { 1 } \otimes T _ { 2 } ) .$$

Since the set { T 1 ⊗ T 2 : T 1 ∈ T (Γ( C k )) , T 1 ∈ T (Γ( C d )) } is total, we conclude that

$$( i d _ { \mathcal { T } ( \Gamma ( \mathbb { C } ^ { k } ) ) } \otimes \Psi ) ( \widetilde { \rho } ) = t r _ { 2 } \left ( \widetilde { U } ( \widetilde { \rho } \otimes \rho _ { ( 0 , I _ { 2 d ^ { \prime } } ) } ) \widetilde { U } ^ { \dagger } \right ) , \quad \forall \, \widetilde { \rho } \in \mathcal { T } ( \Gamma ( \mathbb { C } ^ { k + d } ) ) .$$

- ( v ) ⇒ ( i ) . Follows from the case k = 0 .
- ( ii ) ⇐⇒ ( iii ) Assume that there exist X,Y ∈ M 2 d ( R ) such that Ψ satisfies (8). Then, for any

z ∈ R 2 d and Gaussian states ρ ( m ,S ) consider

$$z \in \mathbb { R } ^ { 2 d } \, \text { and Gaussian states } \rho ( m , s ) \, \text { consider} \\ \text {tr} \left ( \rho ( m , s ) \Psi ^ { * } ( W ( z ) ) \right ) & = \text {tr} \left ( \Psi ( \rho ( m , s ) ) W ( z ) \right ) \\ & = \Psi ( \rho ( m , s ) ) ( z ) \\ & = \exp \left \{ - i \left ( X ^ { T } m + w \right ) ^ { T } z - \frac { 1 } { 2 } z ^ { T } ( X ^ { T } S X + Y ) z \right \} \\ & = \exp \left \{ - i w ^ { T } z - \frac { 1 } { 2 } z ^ { T } Y z \right \} \exp \left \{ - i m ^ { T } X z - \frac { 1 } { 2 } z ^ { T } X ^ { T } S X z \right \} \\ & = \exp \left \{ - i w ^ { T } z - \frac { 1 } { 2 } z ^ { T } Y z \right \} \text {tr} \left ( \rho ( m , s ) W ( X z ) \right ) . \\ \text {Since the span of Gaussian states is dense in } \mathcal { I } ( \mathbb { C } ^ { d } ) \, \text { by } [ F V 7 5 , Theorem II.4 ] , \, ( \text {cf. } [ F V 7 6 ] ) ,$$

Since the span of Gaussian states is dense in T (Γ( C d )) by [FV75, Theorem II.4], (cf. [FV76]), we get

$$\ t r \left ( \varrho \Psi ^ { * } ( W ( z ) ) \right ) = \exp \left \{ - i w ^ { T } z - \frac { 1 } { 2 } z ^ { T } Y z \right \} \text {tr} \left ( \varrho W ( X z ) \right ) , \quad \forall \, \varrho \in \mathcal { T } ( \mathbb { C } ^ { d } ) .$$

Hence

$$\Psi ^ { * } ( W ( z ) ) = \exp \left \{ - i w ^ { T } z - \frac { 1 } { 2 } z ^ { T } Y z \right \} W ( X z ) , \quad \forall \, z \in \mathbb { R } ^ { 2 d } .$$

Conversely, if Ψ ∗ satisfies (9), then for all Gaussian states ρ ( m ,S ) and z ∈ R 2 d we have

$$t r ( \Psi ( \rho _ { ( m , S ) } ) W ( z ) ) & = t r ( \rho _ { ( m , S ) } \Psi ^ { * } ( W ( z ) ) ) \\ & = \exp \{ - i ( X ^ { T } m + w ) ^ { T } z - \frac { 1 } { 2 } z ^ { T } ( X ^ { T } S X + Y ) z \} \\ & = t r ( \rho _ { ( X ^ { T } + m , X ^ { T } S X + Y ) } W ( z ) ) ,$$

so that Ψ satisfies (8).This completes the proof.

□

A quantum channel Ψ : T (Γ( C d )) → T (Γ( C d )) that satisfies any of the equivalence conditions in the above theorem is called a ( d -mode) quantum Gaussian channel . Quantum channels Ψ of the form (10) or equivalently (6) are commonly referred to as Gaussian channels among physicists. Additionally, quantum channels that satisfy the condition ( iii ) of the above theorem are also referred to as Gaussian channels in the literature.

Remark 3.3. Let Ψ : T (Γ( C d )) → T (Γ( C d )) be a quantum channel that satisfies any of the statements (ii)-(iii) of the above theorem. Then the above proof indicates that we can choose the Gaussian unitary operator in (iv) to be defined on Γ( C 3 d ) = Γ( C d ) ⊗ Γ( C 2 d ) . However, we have not discussed the minimality of d ′ , i.e., the minimal number of environment modes required for the dilation, in Theorem 3.1 (iv). Although a complete characterization of the minimal number of environment modes required for a dilation is not available in the literature, an upper bound for d ′ is given in [CEGH08, Theorem 2] as

$$d ^ { \prime } = \text {rank} [ Y ] - \text {rank} [ Y - \Sigma Y ^ { \ominus } \Sigma ^ { T } ] ,$$

where Y ⊖ is the Moore-Penrose inverse of Y , Σ = J 2 d -X T J 2 d X and X,Y are as in (8).

Remark 3.4. We give a proof of ( iv ) ⇒ ( ii ) here because it shows how to get the channel parameters X and Y from the Stinespring representation of a Gaussian channel. Suppose Ψ is a quantum Gaussian channel given by (10). Then, by Proposition 2.5, there exist λ ∈ C with | λ | = 1 , u = u 1 ⊕ u 2 ∈ R 2 d ⊕ R 2 d ′ and L ∈ Sp (2( d + d ′ ) , J 2 d ⊕ J 2 d ′ ) such that U = λW ( u )Γ( L ) .

Without loss of generality, assume that λ = 1 . Write L -1 = [ L 11 L 12 L 21 L 22 ] with L 11 ∈ M 2 d ( R ) and L 22 ∈ M 2 d ′ ( R ) . Then, by Proposition 3.1, we have

$$\Psi ( \rho _ { ( m , S ) } ) = \rho _ { ( X ^ { T } m + w , X ^ { T } S X + Y ) } ,$$

is a Gaussian state for any Gaussian state ρ ( m ,S ) , where w = 2 J 2 d u 1 , X = L 11 and Y = L T 21 L 21 .

## Corollary 3.5. Let X,Y ∈ M 2 d ( R ) . Then the following are equivalent:

- (i) There exists a quantum Gaussian channel Ψ : T (Γ( C d )) → T (Γ( C d )) that transforms a Gaussian state ρ ( m ,S ) to a Gaussian state with covariance X T SX + Y ;

$$( i i ) \ Y + i ( J _ { 2 d } - X ^ { T } J _ { 2 d } X ) \geq 0 .$$

Proof. This follows directly from Theorem 3.1 and the proof of the implication (ii) = ⇒ (iv). □

## 4. Characterization of Linear Optical Channels

A general d -mode linear optical channel , also known as a d -mode universal multiport interferometer , is mathematically described as a Gaussian channel Ψ : Γ( C d ) → Γ( C d ) of the form

$$\Psi ( \varrho ) = t r _ { 2 } \left ( \Gamma ( L ) \left ( \varrho \otimes \rho _ { ( 0 , I _ { d ^ { \prime } } ) } \right ) \Gamma ( L ) ^ { \dagger } \right ) , \quad \forall \, \varrho \in \mathcal { T } ( \Gamma ( \mathbb { C } ^ { d } ) ) ,$$

where L ∈ M 2( d + d ′ ) ( R ) is an orthosymplectic matrix and d ′ ≥ 1 . Here d ′ is called the number of environment modes . It is known that any such channel can be physically implemented using d ( d -1) / 2 Mach-Zehnder interferometers, that is, an optical device composed of only two 50 : 50 beam splitters and two phase shifters [RZBB94, CHM + 16]. As discussed in the previous section, such a Gaussian channel is completely described by two matrices X and Y . Since linear optical channels are special cases of Gaussian channels, it is important to understand when a Gaussian channel, represented by the matrices X and Y , can be physically implemented using a multiport interferometer. We answer this question in the present section. The mathematical result at the heart of this physical problem is an orthosymplectic version of Proposition 3.2, which we will prove next. First, we recall a simple linear algebraic fact.

[

A

-

B

B

A

]

Lemma 4.1.

A matrix

L

∈

M

2

d

(

R

)

is an orthosymplectic matrix if and only if

for some A,B ∈ M d ( R ) with A T A + B T B = I and A T B is symmetric.

Lemma 4.2. Let X,Y ∈ M d ( R ) with ‖ X ‖ ≤ 1 and Y ≥ 0 . Then the following are equivalent:

- (i) There exists an orthosymplectic matrix L = [ X B -B X ] ∈ M 2 d ( R ) with B T B = Y ; √
- (ii) X T X + Y = I and X T Q Y is symmetric for some orthogonal matrix Q ∈ M d ( R ) .

$$P r o o f \, \left ( i \right ) \Rightarrow \left ( i i \right ) \text { Assume that there exists an orthosymplectic matrix } L = \begin{bmatrix} X & B \\ - B & X \end{bmatrix} \in M _ { 2 d } ( \mathbb { R } )$$

) with B T B = Y . Then, by the above lemma, X T X + Y = I and X T B is symmetric. But, by polar decomposition, B = Q √ B T B = Q √ Y for some orthogonal matrix Q ∈ M d ( R ) . ( ii ) = ⇒ ( i ) Clearly, L = [ X Q √ Y -Q √ Y X ] ∈ M 2 d ( R ) is an orthosymplectic matrix with the required properties. □

Theorem 4.1. Let Ψ : Γ( C d ) → Γ( C d ) be a quantum Gaussian channel. Then the following are equivalent:

L

=

- (1) The channel Ψ can be implemented using a multiport interferometer with d number of environment modes;
- (2) There exist matrices X,Y ∈ M 2 d ( R ) such that X T X + Y = I , X T Q √ Y is symmetric for some orthogonal matrix Q ∈ M 2 d ( R ) and

$$\Psi ( \rho _ { ( m , S ) } ) = \rho _ { ( X ^ { T } \mathbf m , X ^ { T } S X + Y ) }$$

for all Gaussian states ρ ( m ,S ) .

Proof. ( i ) ⇒ ( ii ) Assume that Ψ can be implemented by using a multiport interferometer with d number of environment modes, i.e., there exists an orthosymplectic matrix L ∈ M 2( d + d ) ( R ) such that Ψ is given by (12). Since L -1 ∈ M 4 d ( R ) is orthosympletic, by Lemma 4.1, we have

$$\text { such that } & \mathfrak { s y n g l e b y } ( 1 2 ) . \text { Since } L \in \text {M4a} ( \mathbb { Y } ) \text { is of symmetric} , \text { by} \text { lemma} 4 . 1 , \text { we have} \\ & L ^ { - 1 } = \begin{bmatrix} X & B \\ - B & X \end{bmatrix} \text { for some } X , B \in M _ { 2 d } ( \mathbb { R } ) \text { satisfying } X ^ { T } X + B ^ { T } B = I \text { and } X ^ { T } B \text { is symmetric} . \\ & \text { letting } Y \coloneqq B ^ { T } B , \text { by} \text { lemma} 4 . 2 \text { we have } X ^ { T } Q \sqrt { Y } \text { is symmetric for some orthogonal matrix}$$

Letting Y := B T B , by Lemma 4.2, we have X T Q Y is symmetric for some orthogonal matrix Q ∈ M 2 d ( R ) . Furthermore, by Proposition 3.1, it follows that Ψ satisfies (13).

(

ii

X

⇒

X

+

(

i

Y

Conversely, assume that there exists an orthogonal matrix

=

I

and

X

Q

Y

is symmetric and

Ψ

satisfies (13). Then,

L

∈

M

[

:=

-

2

d

(

X

Q

R

√

M 4 d ( R ) is an orthosymplectic matrix. By Proposition 3.1, the map Ψ ′ defined by

$$\Psi ^ { \prime } ( \varrho ) \coloneqq & \text {tr} _ { 2 } ( \Gamma ( L ) ( \varrho \otimes \rho _ { ( 0 , I _ { d } ) } ) \Gamma ( L ) ^ { \dagger } ) \quad \forall \, \varrho \in \mathcal { T } ( \Gamma ( \mathbb { C } ^ { d } ) )$$

defines a quantum Gaussian channel such that

$$\Psi ^ { \prime } ( \rho _ { ( m , S ) } ) = \rho _ { ( X ^ { T } m , X ^ { T } S X + Y ) }$$

for all Gaussian states ρ ( m ,S ) . Since Gaussian states are total we conclude that Ψ = Ψ ′ . □

## 5. Conclusion

This article provides a mathematically rigorous treatment of the equivalence of various definitions of Gaussian channels. Our analysis helps us to derive necessary and sufficient conditions for the physical implementation of certain Gaussain channels using linear optical devices. Furthermore, it also answers the questions asked by Parthasarathy 1 [Par15, page 438]: Consider the following convex sets:

$$\mathcal { F } _ { d } ( X ) & = \left \{ Y \colon Y \geq 0 , X ^ { T } S X + Y \in \mathcal { C M } ( d ) \ \forall \ S \in \mathcal { C M } ( d ) \right \} , \\ \mathcal { F } _ { d } ^ { 0 } ( X ) & = \left \{ Y \colon Y + i \left ( J _ { 2 d } - X ^ { T } J _ { 2 d } X \right ) \geq 0 \right \} ,$$

where X ∈ M 2 d ( R ) . Note that elements of CM ( d ) and F 0 d ( X ) are necessarily positive. The following questions were asked by Parthasarathy:

- (1) What are the necessary and sufficient conditions for the existence of a "symplectic dilation" L = [ X L 12 ] such that L T 21 L 21 ∈ F 0 d ( X ) ?

$$\boxed { L _ { 2 1 } \ L _ { 2 2 } \}$$

- (2) Is it true that for every Y ∈ F d ( X ) there exists a quantum channel that maps a Gaussian state ρ ( m ,S ) to a Gaussian state with covariance matrix X T SX + Y ?
- (3) Are there any Gaussian channels not belonging to the semigroup generated by all reversible, Bosonic, symplectic and quasifree Gaussian channels? (See [Par15] for details.)

1 Note that Parthasarathy uses L 2 ( R n ) while we use Γ( C n ) . The theory of Bosonic systems which we consider in this article remains same on both these space via the isomorphism explained in Section II item 4 of [JP21]

Y

T

√

-

1

)

T

)

Q

)

such that

Q

√

Y

]

X

∈

Proposition 3.2 affirmatively answers the question (i). We will now show that the answer to question (ii) is not true in general. Note that, by Corollary 3.5, there exists a Gaussian channel that transforms a Gaussian state ρ ( m ,S ) to a Gaussian state with covariance X T SX + Y if and only if Y ∈ F 0 d ( X ) . The following example, inspired by one provided by Poletti through private communication in a different context, provides a pair ( X,Y ) such that Y ∈ F d ( X ) but Y / ∈ F 0 d ( X ) .

$$& \text {Example } 5 . 1 . \text { Take } X = \begin{bmatrix} 0 & I _ { d } \\ I _ { d } & 0 \end{bmatrix} , Y = \begin{bmatrix} I _ { d } & 0 \\ 0 & I _ { d } \end{bmatrix} . \text { Then } Y \in \mathcal { C M } ( d ) , \, i . e . , \, Y + i J _ { 2 d } \geq 0 . \text { If } \\ & S \in \mathcal { C M } ( d ) \text { then } S \geq 0 \text { and } \text {hence}$$

$$X ^ { T } S X + Y + i J _ { 2 d } \geq 0 ,$$

i.e., X T SX + Y ∈ CM ( d ) implying that Y ∈ F d ( X ) . On the other hand, Y / ∈ F 0 d ( X ) because

$$Y + i \left ( J _ { 2 d } - X ^ { T } J _ { 2 d } X \right ) & = \begin{bmatrix} I _ { d } & 0 \\ 0 & I _ { d } \end{bmatrix} + i \left ( \left [ \begin{matrix} 0 & I _ { d } \\ - I _ { d } & 0 \end{matrix} \right ] - \begin{bmatrix} 0 & I _ { d } \\ I _ { d } & 0 \end{bmatrix} \left [ \begin{matrix} 0 & I _ { d } \\ - I _ { d } & 0 \end{matrix} \right ] \left [ I _ { d } & I _ { d } \\ I _ { d } & 0 \end{bmatrix} \right ) \\ & = \begin{bmatrix} I _ { d } & 2 i I _ { d } \\ - 2 i I _ { d } & I _ { d } \end{bmatrix} \not \cong 0 .$$

Now, coming to question (iii), the answer is no , because from Theorem 3.1 (iv), and using the definitions of Parthasarathy we see that every Gaussian channel is a symplectic Gaussian channel composed with a displacement, which is a reversible channel , and hence it is in the semigroup generated by all reversible, Bosonic, symplectic and quasifree Gaussian channels.

## Acknowledgment

RD is supported by the Postdoctoral Fellowship of Indian Institute of Technology Bombay. TCJ expresses gratitude to Saikat Guha for his guidance in learning quantum optics and to the Indian Institute of Technology, Madras, for facilitating his visit to conduct this research. SK acknowledges partial support from the IoE Project of MHRD (India) under reference number SB22231267MAETWO008573, and is also partially funded by the NBHM grant (No. 02011/10/2023 NBHM (R.P) R&amp;D II/4225) for this research.

## Appendix A. Supplementary Analysis of Existing Literature

A trace-norm continuous linear map Ψ : T (Γ( C d )) → T (Γ( C d )) is said to be positive , if Ψ ∗ is positive. Let Ψ : T (Γ( C d )) → T (Γ( C d )) be a positive trace preserving map. In [Pol22a], Poletti called such a map to be a Gaussian map if there exist continuous maps α 1 : R 2 d × CM ( d ) → R 2 d and α 2 : R 2 d × CM ( d ) → CM ( d ) such that for every Gaussian state ρ ( m ,S ) on Γ( C d ) , the transformed state Ψ( ρ ( m ,S ) ) is also a Gaussian state with mean α 1 ( m , S ) and covariance α 2 ( m , S ) , that is,

$$\Psi ( \rho _ { ( m , S ) } ) = \rho _ { ( \alpha _ { 1 } ( m , S ) , \alpha _ { 2 } ( m , S ) ) } , \quad \forall \, ( m , S ) \in \mathbb { R } ^ { 2 d } \times \mathcal { C M } ( d ) .$$

Furthermore, Poletti proved [Pol22a, Theorem 4.1] that if Ψ is a Gaussian map, then there exist w ∈ R 2 d and X,Y ∈ M 2 d ( R ) such that

$$\alpha _ { 1 } ( m , S ) = X ^ { T } \mathbf m + \mathbf w , \ \alpha _ { 2 } ( m , S ) = X ^ { T } S X + Y , \ \text { and } \ Y + i ( J _ { 2 d } - X ^ { T } J _ { 2 d } X ) \geq 0 .$$

(We have seen that the last condition implies Y ≥ 0 ). However, in Proposition A.2 below, we show that any functions α j 's satisfying (14) are necessarily continuous, making the explicit continuity assumption superfluous. Furthermore, in Proposition A.3 below, we observe that if there exist X,Y satisfying the inequality Y + i ( J 2 d -X T J 2 d X ) ≥ 0 , then Ψ must be a quantum channel. In contrast, Poletti assumed that Ψ is only a positive map. In fact, as demonstrated in Example A.1, the transpose map on T (Γ( C d )) provides a counterexample: it is a positive map that sends Gaussian states to Gaussian states via continuous maps α j satisfying (14), yet it is not a quantum channel. This is because its dual, the transpose map on B (Γ( C d )) , is not completely positive (cf. [DPMGH15]). So we refine Poletti's theorem [Pol22a, Theorem 4.1] as follows, using essentially the same proof:

Theorem A.1. [Pol22a] Let Ψ : T (Γ( C d )) → T (Γ( C d )) be a quantum channel. Let α 1 : R 2 d × CM ( d ) → R 2 d and α 2 : R 2 d × CM ( d ) → CM ( d ) be two functions such that (14) holds. Then there exist w ∈ R 2 d and X,Y ∈ M 2 d ( R ) such that

$$\alpha _ { 1 } ( \mathbf m , S ) = X ^ { T } \mathbf m + \mathbf w \ \text { and } \ \alpha _ { 2 } ( \mathbf m , S ) = X ^ { T } S X + Y .$$

Furthermore, Y + i ( J 2 d -X T J 2 d X ) ≥ 0 .

In the following, we address certain gaps in the original formulation of Poletti's result. First, we recall the following well-known result called Wigner isomorphism. For a mathematically oriented exposition of Wigner isomorphism one may refer to [JP21, Theorem III.5].

Theorem A.2 ( Wigner isomorphism ) . Let L 2 ( C d ) denote the Hilbert space of square integrable functions on C d with respect to the 2 d -dimensional Lebesgue measure on C d . Define F d : T (Γ( C d )) → L 2 ( C d ) , to be the map satisfying

$$\mathbb { F } _ { d } ( \rho ) ( z ) = \pi ^ { - d / 2 } \widehat { \rho } ( z ) , \quad \forall \, z \in \mathbb { C } ^ { d } , \ \rho \in \mathcal { T } ( \Gamma ( \mathbb { C } ^ { d } ) ) .$$

Then F d extends uniquely to a Hilbert space isomorphism, again denoted by F d , from T 2 (Γ( H ) ) onto L 2 ( C d ) , where T 2 (Γ( H ) denotes the Hilbert space of Hilbert-Schmidt operators on Γ( H ) .

Proposition A.1. Let ρ, ρ n be states on Γ( C d ) . Then ρ n → ρ in trace norm if and only if tr( ρ n W ( z )) → tr( ρW ( z )) for all z ∈ C d .

Proof. Assume that tr( ρ n W ( z )) → tr( ρW ( z )) for all z ∈ C d . To show that ρ n → ρ in trace-norm. By [Ara81, Theorem in Appendix], it is enough to prove that ρ n → ρ in weak operator topology. For any z , w ∈ C d , by Theorem A.2, we have

$$y \, z , w \in \mathbb { C } ^ { 4 } , \, by \, I \text { theorem} \, A . 2 , \, we \, have \, \\ & ( e ( w ) | \rho | e ( z ) ) = \text {tr} \, | e ( z ) \rangle \langle e ( w ) | \rho \\ & = \text {tr} \left ( | e ( w ) \rangle \langle e ( z ) | ^ { \dagger } \, \rho \right ) \\ & = \int \, \overline { \mathbb { F } _ { d } ( | e ( w ) \rangle \langle e ( z ) | ) ( u ) } \mathbb { F } _ { d } ( \rho ) d u \\ & = \int \, \overline { \mathbb { F } _ { d } ( | e ( w ) \rangle \langle e ( z ) | ) ( u ) } \pi ^ { - d / 2 } \widehat { \rho } ( u ) d u \\ & = \int \, \overline { \mathbb { F } _ { d } ( | e ( w ) \rangle \langle e ( z ) | ) ( u ) } \pi ^ { - d / 2 } \left ( \lim _ { k \to \infty } \widehat { \rho } _ { k } ( u ) \right ) d u .$$

Now we will use the dominated convergence theorem to interchange the limit and the integration above. To this end, note that for every z , w ,

$$\pi ^ { - d / 2 } \mathbb { F } _ { d } ( | e ( w ) \rangle \langle e ( z ) | ) ( u ) & = \text {tr} \, | e ( w ) \rangle \langle e ( z ) | \, W ( u ) \\ & = \langle e ( z ) | W ( u ) | e ( w ) \rangle \\ & = e ^ { - \frac { 1 } { 2 } | u | ^ { 2 } - \langle u | w \rangle } \, \langle e ( z ) | e ( u + w ) \rangle \\ & = e ^ { \bar { u } } e ^ { - \frac { 1 } { 2 } | z | ^ { 2 } + \bar { v } z - \bar { z } u } .$$

Thus, the function u ↦→ F d ( | e ( w ) 〉 〈 e ( z ) | )( u ) is integrable. By the dominated convergence theorem, we have

$$\int _ { \mathbb { C } ^ { d } } \overline { \mathbb { F } _ { d } ( | e ( w ) \rangle \langle e ( z ) | ) ( u ) \pi ^ { - d / 2 } \left ( \lim _ { k \to \infty } \widehat { \rho } _ { k } ( u ) \right ) \, d u & = \lim _ { k \to \infty } \int \overline { \mathbb { F } _ { n } ( | e ( w ) \rangle \langle e ( z ) | ) ( u ) \pi ^ { - d / 2 } \widehat { \rho } _ { k } ( u ) \mathrm d u \\ & = \lim _ { k \to \infty } \langle e ( w ) | \rho _ { k } | e ( z ) \rangle \, .$$

Finally, combining (16) and the above we have proved that

$$\langle e ( w ) | \rho | e ( z ) \rangle = \lim _ { k \to \infty } \, \langle e ( w ) | \rho _ { k } | e ( z ) \rangle \, , \ \forall z , w \in \mathbb { C } ^ { d } .$$

Now, the totality of exponential vectors shows that ρ k → ρ in the weak operator topology. □

Proposition A.2. Let Ψ : T (Γ( C d )) → T (Γ( C d )) be a positive map and let α 1 : R 2 d × CM ( d ) → R 2 d and α 2 : R 2 d × CM ( d ) → CM ( d ) be such that for every Gaussian state ρ ( m ,S ) , the transformed state Ψ( ρ ( m ,S ) ) is also a Gaussian state with mean α 1 ( m , S ) and covariance α 2 ( m , S ) . Then the maps α 1 , α 2 are continuous.

Proof. Let ( m n , S n ) , ( m , S ) ∈ R 2 d × CM ( d ) be such that ( m n , S n ) → ( m , S ) . Define the Gaussian states ρ := ρ ( m , S ) and ρ n := ρ ( m n , S n ) for all n ≥ 1 on Γ( C d ) . Then, for all z ∈ C d ,

$$\rho ( \text {in} , 3 ) & \text { and } \rho _ { n } \cdot - \rho ( \text {in} _ { n } , 3 _ { n } ) \text { for all } n \geq 1 \text { on } 1 \subset ( \mathbb { C } \ \real ) . \\ & \lim _ { n } \widehat { \rho } _ { n } ( z ) = \lim _ { n } \exp \{ - i \text { Re} \{ \langle m _ { n } | z \rangle \} - \frac { 1 } { 2 } \text { Re} \{ \langle z | S _ { n } | z \rangle \} \} \\ & = \exp \{ - i \text { Re} \{ \langle m | z \rangle \} - \frac { 1 } { 2 } \text { Re} \{ \langle z | S | z \rangle \} \} \\ & = \widehat { \rho } ( z ) . \\$$

Then, by Proposition A.1, we obtain ρ n → ρ in the trace norm. As Ψ is continuous, we get Ψ( ρ n ) → Ψ( ρ ) in trace norm. Let σ := Ψ( ρ ) and σ n := Ψ( ρ n ) for all n ≥ 1 . Note that σ is a Gaussian state with mean α 1 ( m , S ) and covariance α 2 ( m , S ) , and similarly σ n is also a Gaussian state with mean α 1 ( m n , S n ) and covariance α 2 ( m n , S n ) for all n ≥ 1 . Again, by Proposition A.1, for all z ∈ C d we have ̂ σ n ( z ) → ̂ σ ( z ) , i.e.,

$$& \lim _ { n } \exp \{ - i \, R e \{ \langle \alpha _ { 1 } ( m _ { n } , S _ { n } ) | z \rangle \} - \frac { 1 } { 2 } \, R e \{ \, \langle z | \alpha _ { 2 } ( m _ { n } , S _ { n } ) | z \rangle \} \} \\ & \quad = \exp \{ - i \, R e \{ \langle \alpha _ { 1 } ( m , S ) | z \rangle \} - \frac { 1 } { 2 } \, R e \{ \, \langle z | \alpha _ { 2 } ( m , S ) | z \rangle \} \} .$$

Fix z ∈ C d . Then by applying Logarithm to both sides, and then comparing the real and imaginary part, we get

$$& \lim _ { n } R e \{ \langle \alpha _ { 1 } ( m _ { n } , S _ { n } ) | z \rangle \} = R e \{ \langle \alpha _ { 1 } ( m , S ) | z \rangle \} \quad \text {and} \\ & \lim _ { n } R e \{ \langle z | \alpha _ { 2 } ( m _ { n } , S _ { n } ) | z \rangle \} = R e \{ \langle z | \alpha _ { 2 } ( m , S ) | z \rangle \} .$$

Since z ∈ C d is arbitrary, we conclude that α 1 ( m n , S n ) → α 1 ( m , S ) and α 2 ( m n , S n ) → α 2 ( m , S ) . This completes the proof. □

Proposition A.3. Let Ψ : T (Γ( C d )) → T (Γ( C d )) be a positive trace-preserving map such that

$$\Psi ( \rho _ { ( m , S ) } ) = \rho _ { ( X ^ { T } \mathbf m + \mathbf w , X ^ { T } S X + Y ) } , \quad \forall \, \rho _ { ( \mathbf m , S ) }$$

and for some X,Y ∈ M 2 d ( R ) and w ∈ R 2 d . Then Ψ is a quantum channel if and only if Y + i ( J 2 d -X T J 2 d X ) ≥ 0 .

For a proof of the above proposition, the reader is referred to [Par22, Section 3].

Example A.1. Let B be the Fock number basis (also known as particle basis see [JP21, Section II] cf. [Par92, Proposition 19.3]) for the space Γ( C d ) . Let Ψ : T (Γ( C d )) → T (Γ( C d )) be the transpose map with respect to the basis B , i.e., Ψ( ρ ) := ρ T , which is defined so that the matrix representation of ρ T in the basis B is the transpose of the matrix representation of ρ in the basis B . By [JP21, Proposition V .5 and Theorem V.7], a state ρ on Γ( C d ) is Gaussian if and only if there exists a triple ( α , A, Λ) consisting of a scalar α ∈ C , and matrices A, Λ ∈ M d ( C ) satisfying A = A T and Λ ≥ 0 , such that

$$G _ { \rho } ( u , v ) \coloneqq \langle e ( \bar { u } ) | \rho | e ( v ) \rangle = c \exp \left \{ u ^ { T } \alpha + \bar { \alpha } ^ { T } v + u ^ { T } A u + u ^ { T } \Lambda v + v ^ { T } \bar { A } v \right \} ,$$

for all u , v ∈ C d , where c = 〈 e (0) | ρ | e (0) 〉 . Note that 〈 e (¯ u ) | ρ T | e ( v ) 〉 = 〈 e (¯ v ) | ρ | e ( u ) 〉 . So

$$G _ { \rho ^ { T } } ( u , v ) & = \langle e ( \bar { v } ) | \rho | e ( u ) \rangle = c \exp \left \{ v ^ { T } \alpha + \bar { \alpha } ^ { T } u + v ^ { T } A v + v ^ { T } \Lambda u + u ^ { T } \bar { A } u \right \} \\ & = c \exp \left \{ u ^ { T } \bar { \alpha } + \alpha ^ { T } v + u ^ { T } \bar { A } u + u ^ { T } \Lambda ^ { T } v + v ^ { T } A v \right \} ,$$

$$=$$

which preserves the structure of the right side of (18) with the new triple ( ¯ α , ¯ A, Λ T ) . Hence, the transpose map Ψ sends Gaussian states to Gaussian states. Note now that the dual map Ψ ∗ is the transpose map of B (Γ( C d )) with respect to the same basis B . It is well-known that the transpose map is a positive but not CP map. By Proposition A.2, we see that the transpose map satisfies the hypothesis of [Pol22a, Theorem 4.1] and [Pol22b, Theorem 2] but transpose map is not CP and hence not a quantum channel.

## References

- [Ara81] Jonathan Arazy. More on convergence in unitary matrix spaces. Proc. Am. Math. Soc. , 83(1):44, September 1981.
- [Att13] Stéphane Attal. Quantu channels. Lecture notes , 2013.
- [CEGH08] F Caruso, J Eisert, V Giovannetti, and A S Holevo. Multi-mode bosonic Gaussian channels. New J. Phys. , 10(8):083030, August 2008.
- [CHM + 16] William R Clements, Peter C Humphreys, Benjamin J Metcalf, W Steven Kolthammer, and Ian A Walsmley. Optimal design for universal multiport interferometers. Optica , 3(12):1460, December 2016.
- [DPMGH15] Giacomo De Palma, Andrea Mari, Vittorio Giovannetti, and Alexander S Holevo. Normal form decomposition for Gaussian-to-Gaussian superoperators. J. Math. Phys. , 56(5):052202, May 2015.
- [EW07] J Eisert and M M Wolf. Gaussian Quantum Channels. In Quantum Information with Continuous Variables of Atoms and Light , pages 23-42. Published by Imperial College Press and distributed by World Scientific Publishing Co., February 2007.
- [Fan76] MFannes. Quasi-free states and automorphisms of the CCR-algebra. Commun. Math. Phys. , 51(1):55-66, February 1976.
- [FV75] M Fannes and A Verbeure. Gauge transformations and normal states of the CCR. J. Math. Phys. , 16(10):2086-2088, October 1975.
- [FV76] M Fannes and A Verbeure. Erratum: Gauge transformations and normal states of the CCR. J. Math. Phys. , 17(2):284-284, February 1976.
- [Gos06] Maurice A Gosson. Symplectic Geometry and Quantum Mechanics . Advances in Partial Differential Equations. Birkhauser Verlag AG, Basel, Switzerland, 2006 edition, December 2006.

- [Guh08] Saikat Guha. Multiple-User Quantum Information Theory for Optical Communication Channels . Ph.d. thesis, Massachusetts Institute of Technology Cambridge, May 2008.
- [HJ12] Roger A Horn and Charles R Johnson. Matrix Analysis . Cambridge University Press, 2 edition, 2012.
- [Hol19] Alexander S Holevo. Quantum Systems, Channels, Information A Mathematical Introduction . Texts and Monographs in Theoretical Physics. De Gruyter, 2019.
- [HW01] A S Holevo and R F Werner. Evaluating capacities of bosonic Gaussian channels. Phys. Rev. A , 63(3):032312, February 2001.
- [Joh18] Tiju Cherian John. Infinite mode quantum gaussian states . Ph.d. thesis, Indian Statistical InstituteKolkata, 2018.
- [JP21] Tiju Cherian John and K. R. Parthasarathy. A common parametrization for finite mode Gaussian states, their symmetries, and associated contractions with some applications. Journal of Mathematical Physics , 62(2):022102, 02 2021.
- [NC10] Michael A. Nielsen and Isaac L. Chuang. Quantum Computation and Quantum Information: 10th Anniversary Edition . Cambridge University Press, 2010.
- [Par92] K. R. Parthasarathy. An introduction to quantum stochastic calculus . Modern Birkhäuser Classics. Birkhäuser/Springer Basel AG, Basel, 1992. [2012 reprint of the 1992 original] [MR1164866].
- [Par10] K R Parthasarathy. What is a Gaussian state? Commun. Stoch. Anal. , 4(2):143-160, 2010.
- [Par13] K. R. Parthasarathy. The symmetry group of gaussian states in L 2 ( R n ) , 2013.
- [Par15] K. R. Parthasarathy. Symplectic dilations, Gaussian states and Gaussian channels. Indian J. Pure Appl. Math. , 46(4):419-439, 2015.
- [Par22] K. R. Parthasarathy. Twisted convolution quantum information channels, one-parameter semigroups and their generators. Infinite Dimensional Analysis, Quantum Probability and Related Topics , 25(04), December 2022.
- [Pau02] Vern Paulsen. Completely bounded maps and operator algebras , volume 78 of Cambridge Studies in Advanced Mathematics . Cambridge University Press, Cambridge, 2002.
- [Pol22a] Damiano Poletti. Characterization of gaussian quantum markov semigroups. Infinite Dimensional Analysis, Quantum Probability and Related Topics , 25(03):2250014, 2022.
- [Pol22b] Damiano Poletti. Characterization of Gaussian Quantum Markov Semigroups. In Infinite Dimensional Analysis, Quantum Probability and Applications , pages 197-211. Springer International Publishing, 2022.
- [RZBB94] M Reck, A Zeilinger, H J Bernstein, and P Bertani. Experimental realization of any discrete unitary operator. Phys. Rev. Lett. , 73(1):58-61, July 1994.
- [Ser17] Alessio Serafini. Quantum Continuous Variables: A Primer of Theoretical Methods . Apple Academic Press, Oakville, MO, June 2017.
- [Sti55] W. Forrest Stinespring. Positive functions on C ∗ -algebras. Proc. Amer. Math. Soc. , 6:211-216, 1955.
- [SW17] Krishna Kumar Sabapathy and Andreas Winter. Non-Gaussian operations on bosonic modes of light: Photon-added Gaussian channels. Phys. Rev. A , 95(6):062309, June 2017.
- [Wat18] John Watrous. The Theory of Quantum Information . Cambridge University Press, 2018.
- [Wil13] Mark M. Wilde. Quantum Information Theory . Cambridge University Press, 2013.
- [WPGP + 12] Christian Weedbrook, Stefano Pirandola, Raúl García-Patrón, Nicolas J Cerf, Timothy C Ralph, Jeffrey H Shapiro, and Seth Lloyd. Gaussian quantum information. Rev. Mod. Phys. , 84(2):621-669, May 2012.