## Markovian to non-Markovian phase transition in the operator dynamics of a mobile impurity

Dominic Gribben 1 , Jamir Marino 1 , Shane P. Kelly 1,2*

- 1 Institute for Physics, Johannes Gutenberg University of Mainz, D-55099 Mainz, Germany
- 2 Mani L. Bhaumik Institute for Theoretical Physics, Department of Physics and Astronomy, University of California at Los Angeles, Los Angeles, CA 90095 * skelly@physics.ucla.edu

July 1, 2024

## Abstract

We study a random unitary circuit model of an impurity moving through a chaotic medium. The exchange of information between the medium and impurity is controlled by varying the velocity of the impurity, v d , relative to the speed of information propagation within the medium, v B . Above supersonic velocities, v d &gt; v B , information cannot flow back to the impurity after it has moved into the medium, and the resulting dynamics are Markovian. Below supersonic velocities, v d &lt; v B , the dynamics of the impurity and medium are non-Markovian, and information is able to flow back onto the impurity. We show the two regimes are separated by a continuous phase transition with exponents directly related to the diffusive spreading of operators in the medium. This is demonstrated by monitoring an out-of-time-order correlator (OTOC) in a scenario where the impurity is substituted at an intermediate time. During the Markovian phase, information from the medium cannot transfer onto the replaced impurity, manifesting in no significant operator development. Conversely, in the non-Markovian phase, we observe that operators acquire support on the newly introduced impurity. We also characterize the dynamics using the coherent information and provide two decoders which can efficiently probe the transition between Markovian and non-Markovian information flow. Our work demonstrates that Markovian and non-Markovian dynamics can be separated by a phase transition, and we propose an efficient protocol for observing this transition.

## Contents

|   1 | Introduction                             |   2 |
|-----|------------------------------------------|-----|
|   2 | Model                                    |   4 |
|     | 2.1 One-dimensional medium               |   5 |
|     | 2.1.1 Motivation and expectations        |   6 |
| 2.2 | Two-dimensional medium                   |   7 |
|     | 2.2.1 Motivation and expectations        |   7 |
|   3 | Capturing operator dynamics and backflow |   7 |
|     | 3.1 Operator backflow                    |   8 |

| 4          | Operator dynamics                                 | Operator dynamics                                 |   9 |
|------------|---------------------------------------------------|---------------------------------------------------|-----|
|            | 4.1                                               | One-dimensional medium                            |   9 |
|            | 4.2                                               | Two-dimensional medium                            |  11 |
| 5          | Information transition                            | Information transition                            |  13 |
|            | 5.1                                               | Echo protocol                                     |  13 |
|            |                                                   | 5.1.1 Echo decoder                                |  14 |
|            | 5.2                                               | Teleportation protocol                            |  15 |
|            |                                                   | 5.2.1 Teleportation decoder                       |  16 |
| 6          | Operator Markovianty                              | Operator Markovianty                              |  17 |
| 7          | Conclusion                                        | Conclusion                                        |  18 |
| A          | Alternate 1D circuit                              | Alternate 1D circuit                              |  19 |
| B          | Derivation of Eq. (11)                            | Derivation of Eq. (11)                            |  22 |
| C          | Details of HP fidelity and derivation of Eq. (15) | Details of HP fidelity and derivation of Eq. (15) |  23 |
| References | References                                        | References                                        |  24 |

## 1 Introduction

The scrambling of quantum information is a concept crucial to a number of fields [1-9]. Its study helps quantify the complexity of quantum processes and can be related to the local recoverability of information [1,10]. Quantum experiments carried out in reality are inextricable from their environments which often hinder information tasks when quantum information in the system is irretrievably lost to the environment [11-22]. However, there is always a finite probability that this information can flow back into the system and for certain physical processes this backflow is crucial. For example, in closed system thermalization the bulk of the system acts as an environment to, and becomes entangled with, local subsystems [23-25]. Furthermore, this information back flow, or non-Markovanity, may be a useful resource for quantum information processing [26,27].

Recently, phase transitions in information dynamics have been demonstrated in a variety of settings ranging from PT-symmetric non-Hermitian systems [28-34] to systems monitored by projective measurements [35-44], to more general open systems involving qubits arranged in a variety of space-time geometries [14, 21, 32, 45-61]. It is therefore natural to wonder if open system dynamics undergo a phase transition in information flow as they are tuned between Markovian and non-Markovian limits. In this light, the authors of Refs. [62, 63] investigated non-Markovian effects of monitored systems with a non-Markovian environment but did not find a transition in non-Markovanity. In another context, Refs. [64,65] found the non-Markovianity of an impurity is sensitive to a topological phase transition occurring within the environment. However, it is not clear if the two phases are distinguished by Markovian and non-Markovian dynamics. Furthermore, the environment in both systems are non-scrambling and Gaussian which is not characteristic of generic quantum systems.

Thus, in this work, we investigate the possibility of a phase transition in non-Markovianity of an impurity coupled to a quantum chaotic environment. We present a model in which the system can be taken between regions of zero and non-zero information backflow by only varying the form of the coupling between the system and environment. Distinct from previous results [62,64,65], we find that these regions are separated by a continuous phase transition, and identify a critical point characterized by scale-free temporal correlations.

Figure 1: Cartoon of the model we consider: an impurity (blue circle) moving through a medium. The circles within the medium correspond to the unitary brickwork which drives the evolution of the medium. Initially, the medium contains no information about the impurity (clear circles). Then at a random time, the impurity interacts with the medium and leaks information into it at that particular point in spacetime. The information is rapidly scrambled away from this point (green circles) at a characteristic velocity. In this work, we investigate the behaviour for subsonic (left) and supersonic (right) impurity velocities.

<!-- image -->

The model we consider describes an impurity moving through a chaotic medium. The capacity at which information can leave the impurity and re-enter at a later time can be tuned by varying the velocity of the impurity relative to the information scrambling velocity within the medium. We simulate the chaotic dynamics of the model using random unitary circuits and capture the flow of information by computing the out-of-time-order correlator (OTOC) [66-68]. The strength of the OTOC on the impurity at late times results from a combination of information retained by the impurity over time and information backflow from the medium. To isolate the contribution from backflow we enact a protocol in which the impurity is removed at an intermediate time and replaced with a fresh impurity. Any non-trivial operator support on the fresh impurity must be a result of feedback from the medium. Beginning with a single qubit impurity moving through a 1D medium, we find that on varying the velocity of the impurity a phase transition occurs between zero and non-zero backflow. Using a mapping between operator growth and a random walk [67,68], we show that the criticality is a result of the diffusive growth of the operator within the medium.

The effect of varying the velocity of a local object, e.g. an impurity or local quench, within a medium relative to the speed of light within that medium has been studied previously in contexts such as Hawking radiation within many-body systems [69]. More generally the effect of this moving perturbation on the underlying state of the medium has been studied in a variety of approaches [70-74]. In contrast to these studies we instead focus on the dynamics of the information localized on the impurity and how this is affected by its velocity.

We then extend our model to that describing a 1D impurity moving through a 2D medium to study the effect of the backflow transition on scrambling within the impurity. In particular we focus on how the presence of backflow affects a distinct phase transition known to occur in the Markovian limit of this extended model [14]. This transition is between phases of persistent and vanishing scrambling within the impurity and we shall refer to it here as the scrambling transition . We find that the scrambling transition is only possible when there is no operator backflow.

As in the scrambling transition, the backflow phase transition can also be observed in a particular channel capacity. The relevant channel in this case captures the information about the initial state contained within the medium and discarded impurity at late times. We show that a party with access to only these degrees of freedom can recover the initial impurity state with perfect fidelity when the channel capacity is maximal. This is achieved via a protocol where a fresh impurity is coupled to the medium and the dynamics are reversed. Additionally, we show that the backflow transition can be observed in a complementary channel. This channel characterizes the ability to decode information on the initial impurity state given access to its final state along with the initial states of the medium and the fresh impurity inserted in the reset step. The decoder for the complementary channel is reminiscent of that proposed in [10], for the Hayden-Preskill protocol. We associate these two quantum channels with distinct decoding protocols and in each case derive relations between the decoder fidelity and the channel capacity. In one case the decoder fidelity is optimal in the limit of zero backflow whereas for the other decoding it is enhanced in the opposite limit where non-Markovianity is maximal.

Weconclude with a discussion of the distinction between the operator non-Markovianity introduced in this paper and non-Markovianity observed in time ordered correlations [75]. We highlight how operator non-Markovianity is only captured by protocols involving an echo such as the OTOC and decoder fidelities discussed in this paper. In contrast, the notions of Markovianity as discussed in Ref. [75], do not capture an echo and do not naturally capture the phase transition here. To connect the two we discuss a situation in which the observer has access to the initial environment but loses access at later times.

The paper is organized as follows. In Section 2 we introduce the model and give the details of the circuit implementation for both the 1D and 2D cases. We continue, in Section 3, to detail how we capture the operator dynamics and in particular the protocol we implement to capture operator backflow. First, we consider a single qubit impurity coupled to a 1D medium, and discuss the OTOC dynamics of this model in Section 4.1. Here we compute the degree of information backflow as a function of velocity and determine finite-time scaling exponents. In Section 4.2 we take a 1D impurity moving through a 2D medium and investigate the impact of the backflow transition on scrambling within the impurity. We then, in Section 5, investigate how the backflow transition is manifest in a pair of complementary channel capacities. We detail decoding protocols whose fidelity is directly related to these channel capacities and can be used to observe the transition in small, near term quantum computers. We conclude our discussion, in Section 6, where we emphasize what defines operator non-Markovianity before we finally, in Section 7, summarize our results and discuss potential future directions.

## 2 Model

Below we construct a random circuit model aimed at capturing the information dynamics of an impurity moving through a chaotic medium. To do so, we will consider the full unitary evolution of the total system of impurity and medium. By partitioning a closed system into subsystems labelled system and environment, we are then able to apply open systems concepts such as Markovianity. In this paper we always consider Markovianity of the impurity as a system with the medium as its environment. The main result is that the change from non-Markovian to Markovian operator dynamics on the impurity corresponds to a continuous phase transition.

Figure 2: Circuit diagram of the model implementation. Here the medium qubits are all initialized in an infinite temperature state, ρ ∞ , and the impurity is initially in state ρ I (0). In this realization the impurity initially drifts two sites away from its origin and then interacts with the medium, after a further drift of one site it once again swaps qubits with the medium. The green gates indicate the lightcone associated with the information transferred into the medium by the first swap. The second swap is still within this scrambling lightcone and thus could lead to backflow of information from medium to impurity.

<!-- image -->

## 2.1 One-dimensional medium

Our first model is of a single impurity qubit moving over a 1D chain of qubits describing the medium. The chaotic evolution of the medium is captured by a random circuit and the impurity-medium interaction consists of swap gates applied at a fixed rate, p . We choose to use this form of interaction as it is analogous to the absorption/emission of quanta from/into the medium. However, we expect the results of this paper to hold for any interaction that results in operators being spread from impurity to medium and vice versa 1 . The circuit implementation of this evolution is depicted in Figure 2. The medium is initialized in an infinite temperature state and evolves under a brickwork of random unitaries drawn from the Clifford group. The Clifford group is a unitary 3-design: it exactly reproduces the first, second and third order moments of the Haar distribution [76]. Below, we consider the dynamics of OTOCs, which are second order functions of the brickwork unitaries, and hence are equivalent to those that would be generated by Haar random circuits.

1 We have confirmed this prediction numerically for an interaction consisting of random unitaries drawn from the Clifford group.

Figure 3: Illustration of the model implementation for a 1D impurity moving through a 2D medium. The left diagram shows the circuit which evolves the impurity through time with swaps occurring between each site and its independent strip of the medium. The right-hand cartoon shows how the impurity moves through the medium. Each green strip of the medium evolves independently via the circuit displayed in Figure 2.

<!-- image -->

Between every two layers of unitaries, the impurity qubit is swapped with the medium qubit at position x ∈ Z with probability p . Initially, the impurity is at position x = 0, and after each interaction step it shifts from x to x + d where the drift, d ∈ Z , is drawn, independently at each step, from the following binomial distribution:

$$p ( d ) = \begin{pmatrix} d _ { \max } \\ d \end{pmatrix} p _ { D } ^ { d } ( 1 - p _ { D } ) ^ { d _ { \max } - d } . \quad ( 1 )$$

Such a process implements a biased random walk with drift velocity v d = p D d max /τ = p D d max where τ is the time between shifts. For the results presented in this article, we work in units of τ ≡ 1 and fix d max = 20 2 .

## 2.1.1 Motivation and expectations

This model could describe, for instance, a mobile impurity immersed in a Bose gas, or equivalently a static impurity in a flowing gas [77-81]. In such a system, the general expectation is that information transferred from impurity to medium is rapidly scrambled away from the location of the interaction in a characteristic lightcone [67, 68]. This lightcone captures the velocity at which information is scrambled through the medium.

By tuning the impurity velocity relative to the speed of information scrambling within the medium, one may expect the information dynamics to undergo a transition. When the impurity moves slower than the information scrambling in the medium there is potential for information to flow back into the impurity and hence the reduced dynamics of the impurity can be non-Markovian. On the other hand, if the velocity is increased such that the trajectory falls outside the light cone, information backflow becomes impossible and the medium acts as a Markovian environment for the impurity. This limit, where the probability of feedback is zero, corresponds to v d &gt; c where c is the maximum velocity of information in the medium; in our case two layers of unitaries are applied per time step such that c = 2. In this limit the medium is effectively reset with respect to the dynamics of the impurity and there is no possibility of feedback. The general model and these two cases are depicted in Figure 1. In the Appendix A, we consider an alternate circuit where the scrambling within the medium only occurs up to the position of the impurity.

2 We have confirmed that the main results of these paper do not qualitatively change if a deterministic shift is used instead.

## 2.2 Two-dimensional medium

Motivated by Ref. [14] we also consider a chain of N impurity qubits moving through a 2D lattice of N × M qubits. The 2D medium evolves as N decoupled chains of M qubits evolving under the brickwork circuit in Figure 2. The N media are treated as independent but evolve under equivalent parameters i.e. p and v d are global properties. Although treating the environments as independent is artificial it presents a simple limit in which we can explore the effect of backflow on the scrambling within the impurity. The 1D impurity chain takes steps through this medium in the x -direction with the step length being drawn from the distribution in Eq. (1). We allow for interactions to occur between the individual impurity sites via a random unitary brickwork equivalent to that occurring in the medium. Between applying each layer of unitaries to the impurity chain, each qubit of the chain is swapped independently into the medium with probability p . The 2D model is depicted in Figure 3; another perspective is gained by considering Figure 2 as a cross-section.

## 2.2.1 Motivation and expectations

For the 2D model we must account for the scrambling in the medium, the scrambling on the impurity, and the interaction between them. When taking the limit of Markovian impurity dynamics, v d &gt; c , the scrambling dynamics of the medium can be ignored and the circuit is equivalent to the one studied in Ref. [14]. There, the medium was a stationary reservoir of infinite temperature qubits. Similarly, in the limit v d &gt; c the 1D impurity is deterministically beyond the scrambling lightcone and only interacts with infinite temperature qubits unaffected by past medium-impurity interactions. In this Markovian limit, the swaps occurring between the impurity and the medium suppress scrambling within the 1D impurity. In Ref. [14], it was shown that this suppression can result in a phase transition at a critical swap rate, p c , above which scrambling in the impurity quickly vanishes corresponding the a complete loss of information into the environment. This scrambling transition was identified to be part of the directed percolation universality class [14].

Outside of the Markovian limit, v d &lt; c , information backflow is possible, and we investigate its effect on the scrambling transition identified in the Markovian limit. A simple expectation is that information backflow into the impurity increases information scrambling in the impurity and increases the critical swap rate.

## 3 Capturing operator dynamics and backflow

In this section we start with the 1D problem. We initialize an operator localized on the impurity, after some time on the order of p -1 it is swapped into to the medium and then scrambled. To capture how the operator is scrambled within the medium we compute the out-of-time-order correlator (OTOC) defined by

$$C ^ { ( M ) } ( x , t ) = \frac { 1 } { 4 } t r \left \{ \rho _ { 0 } ^ { I M } [ X ^ { ( I ) } ( t ) , Y _ { x } ^ { ( M ) \dagger } [ X ^ { ( I ) } ( t ) , Y _ { x } ^ { ( M ) } ] \right \} , \quad ( 2 )$$

where X ( I ) is the Pauli-X operator acting on the impurity and X ( I ) ( t ) = U † t X ( I ) U t is this operator evolved to time t in the Heisenberg picture. Y ( M ) x is the Pauli-Y operator acting on the medium qubit at site x . OTOCs quantify where in Hilbert space a time-evolved operator has support. In addition to the operator weight in the medium, we capture the operator weight remaining on the impurity with the OTOC given by

Figure 4: Schematic of the protocol used to measure the operator backflow quantified by B = 1 4 tr { ρ IM 0 [ ˜ X ( I ) ( t ) , Y ( I ) ] † [ ˜ X ( I ) ( t ) , Y ( I ) ] } . The total space is partitioned into the impurity, I , the medium, M , and the fresh impurity swapped in at the reset step, R . Highlighted in green and blue are the potential channels for information about X ( I ) to be carried, non-trivial operator weight on the impurity is detected by computing the overlap with Y ( I ) . It is only possible for non-trivial weight to be carried to the fresh impurity via M and channel highlighted in blue, with the perspective of the impurity as system and medium as environment this corresponds to a non-Markovian information flow. The unitaries, U 1 and U 2 , are given by the circuit in Figure 2.

<!-- image -->

$$C ^ { ( I ) } ( t ) = \frac { 1 } { 4 } t r \left \{ \rho _ { 0 } ^ { I M } [ X ^ { ( I ) } ( t ) , Y ^ { ( I ) } ] ^ { \dagger } [ X ^ { ( I ) } ( t ) , Y ^ { ( I ) } ] \right \} , \quad ( 3 )$$

where Y ( I ) is the Pauli-Y operator acting on the impurity. The choice of Pauli operators in the above expressions is arbitrary in our case; on averaging over Clifford circuit realizations, any two distinct non-identity Pauli operators for the initial and time-evolved operators would yield identical results.

If C ( I ) ( t ) vanishes at some time t then the entire information content of the initial operator has flowed into the environment. In the case of Markovian environments this information is irretrievable unless one can access the environment. However, for a generic environment, information can flow back into the system at later times leading to nonMarkovian revivals of the OTOC on the system. But this non-Markovianity is distinct from that typically considered in the field of open quantum systems which concerns the evolution and/or correlations of a state rather than an operator [75, 82]. We will now outline a protocol in which we can measure the degree of this backflow.

## 3.1 Operator backflow

We capture operator backflow with a protocol analogous to the causal break of the process tensor formalism [75,83-88]. At the break the system is effectively reset such that across this break information can only be communicated via the environment; any dependence of the system's evolution post-break on its evolution pre-break is an indication of nonMarkovianity. Our protocol in this spirit is depicted in Figure 4. First, the model is evolved for a time t 1 , then the impurity is reset by swapping the qubit with one in an infinite temperature state. This fresh impurity is then evolved for a further time t 2 to give a total evolution time of T ≡ t 1 + t 2 . After these steps we again track the operator weight on the impurity via an OTOC given by

$$B ( v _ { d } , T ) = \frac { 1 } { 4 } \text {tr} \left \{ \rho _ { 0 } ^ { I M } [ \tilde { X } ^ { ( I ) } ( T ) , Y ^ { ( I ) } ] [ \tilde { X } ^ { ( I ) } ( T ) , Y ^ { ( I ) } ] \right \} ,$$

whose definition is equivalent to that of C ( I ) ( T ), but with the operators evolved under the backflow protocol, i.e. ˜ X ( I ) ( T ) = U † 2 U † 1 X ( I ) U 1 U 2 . We enforce that t 1 , t 2 ≫ p -1 such that the impurity and medium have significant time to interact before the reset step and subsequent OTOC readout.

In the case of random unitary evolution the environment strongly scrambles any information that flows into it and the system evolution is Markovian as characterized by a process tensor which factorizes between timesteps. However, it has recently been shown that although the state evolution may be Markovian or near-Markovian, the OTOC can still display non-Markovian correlations [89]. These correlations arise due to the Heisenberg evolution of the operator; in our model this causes the support of the operator to first spread onto the medium and then, after the reset step, onto the fresh impurity. This is highlighted in Figure 2 where we illustrate how information of the initial state can flow through the various channels of the process. The only way for this information to flow onto the final impurity is via the channel represented by the blue line. This corresponds to backflow of information from the medium via U 2 , this information having flowed into the medium via U 1 . We expect U 1 to transfer information from the impurity to the medium regardless of the impurity's velocity, but U 2 can only implement the reverse if the impurity remains causally connected to the initial transfer, i.e. if it travels at sub-luminal velocities. Although we treat the full system unitarily, by considering the impurity sector as the system and the medium as the environment, we can consistently refer to the Markovianity of the reduced operator dynamics on the impurity.

## 4 Operator dynamics

In this section, we present the OTOC dynamics for both the 1D and 2D models introduced in Section 2. First, we investigate the dynamics of the backflow protocol for the 1D system and perform finite-time scaling on the late-time dynamics. For the 2D system, we consider the steady state of the OTOC without applying the reset step and investigate the effect of operator backflow on the scrambling of operators within the 1D impurity.

## 4.1 One-dimensional medium

We shall focus exclusively on B ( v d , T ), the disorder-averaged weight of the OTOC on the impurity at time T during the reset protocol depicted in Figure 4. In Figure 5 we plot B ( v d , T ) at a late time as a function of the drift velocity v d . A transition occurs between at a critical velocity of v ∗ ≈ 1 . 2. To understand the significance of this value we must recall that the information dynamics within the medium is stochastic. So, while the rate at which the lightcone broadens is bounded from above by c , we can also associate a butterfly velocity, v B , with the typical expansion rate. The average increase in the number of sites on which an operator has support after a time t is then given by 2 v B t [68]. In our case we have v B = 1 . 2, precisely the velocity at which we observe the transition.

In Figure 6 we show that the disorder-averaged backflow satisfies a finite-time scaling of the following form: √

$$\overline { B ( v _ { d } , T ) } = f ( ( v _ { d } - v ^ { * } ) \sqrt { T } ) ,$$

where f is a universal scaling function. The origin of this exponent can be understood by analyzing the operator dynamics within the medium. Given that t 2 is much larger than the inverse swap rate 1 /p , we expect that, at t 2 , the impurity has equilibrated with the local medium and will follow the dynamics of the nearest medium qubit. We are therefore interested in the weight of the OTOC in the medium at the position of the impurity; after disorder averaging that position is x I = v d t .

Figure 5: Backflow order parameter on variation of impurity drift velocity. Here we set t 1 = 100, t 2 = 1000 and p = 0 . 1. This is the result of an average over 10 4 disorder realizations.

<!-- image -->

To determine the OTOC at this position, we use the approach detailed in Ref. [68]. There, the average OTOC is considered by choosing the unitary bricks from the Clifford group and using the fact that the Clifford group is a 3-design [76]. This ensures the average over the Clifford group is the same as the average over the Haar group for the OTOC. Clifford circuits map Pauli strings to Pauli strings, and since we consider an initial Pauli X operator, this operator remains a Pauli string for all time. From the definition of the OTOC we have B ( v d , t ) = 1 if the operator X ( I ) ( t ) has character of X or Z on the impurity and otherwise equals zero. On disorder averaging if the operator has non-trivial (i.e. non-identity) support on a particular site then it has equal probability of having X , Y or Z character. Therefore we have that B ( v d , t ) = 2 3 n I ( v d , t ), where n I ( v d , t ) is a density that is equal to one if X ( I ) ( t ) has non-trivial support on the impurity, and zero otherwise. We can equivalently express the disorder-averaged OTOC within the medium at position x as B ( M ) ( x, t ) = 2 3 n M ( x, t ), where B ( M ) is the OTOC within the medium during the backflow protocol. The late-time dynamics of n M ( x, t ) is characterized by regions of zero and non-zero density separated by diffusively propagating boundaries. The dynamics of these boundaries can be well captured by a hydrodynamic description where the probability distribution of the boundary position evolves according to a Fokker-Planck equation [68]. The OTOC weight at the position of the impurity is given by

$$P ( v _ { d } , t ) = \overline { n _ { M } ( \overline { x _ { I } } , t ) } = \frac { 1 } { 2 } \left [ 1 - \text {erf} \left ( \frac { v \sqrt { t } } { 2 \sqrt { D } } \right ) \right ] ,$$

where v = v d -v B is the difference between the impurity velocity, v d and operator butterfly velocity v B , and D is a constant. This satisfies the diffusion-like scaling relation:

$$P ( v , t ) = F ( v \sqrt { t } ) .$$

The backflow transition satisfies precisely the same scaling relation as that followed by the OTOC weight within the medium at the position of the impurity. This occurs because at late times the impurity matches the free dynamics of the OTOC within the medium without affecting it, the diffusive nature of this dynamics gives us the numerically observed scaling relations shown in Fig. 6. Moreover, the dynamics described by Eq. (6) are scalefree when v = 0. Away from this point the dynamics instead follow an error function which at long times corresponds to exponential relaxation on a timescale given by v 2 4 D .

Figure 6: Left: Expanded view of the backflow phase transition near the critical point. Right: Data collapse under a finite-time rescaling. Here we set t 1 = 100 and p = 0 . 1. This is the result of an average over 10 4 disorder realizations.

<!-- image -->

## 4.2 Two-dimensional medium

For the 2D problem the quantity of interest is the density of the OTOC over the entire impurity. We first extend the definition of the OTOC in Eq. 3 to have spatial dependence:

$$C ^ { ( I ) } ( y , t ) = \frac { 1 } { 4 } \text {tr} \left \{ \rho _ { 0 } ^ { I M } [ X _ { 0 } ^ { ( I ) } ( t ) , Y _ { y } ^ { ( I ) } ] [ X _ { 0 } ^ { ( I ) } ( t ) , Y _ { y } ^ { ( I ) } ] \right \} ,$$

where y has been introduced to index the position on the impurity. From this we can analogously define the, now site-dependent, density: C ( I ) ( y, t ) = 2 3 n I ( y, t ). The sitedependence of the operator weight on the impurity is irrelevant to the question of backflow we study here. Instead, we consider the total operator weight

$$\overline { N _ { I } ( t ) } = \frac { 1 } { N } \sum _ { y } \overline { n _ { I } ( y , t ) } ,$$

where N is the number of qubits within the impurity. This is the order parameter observing the phase transition in scrambling in the Markovian limit of this model [14]. The transition is characterized by the steady-state value of N I ; below the critical swap rate p c , N I is finite and the system is in the scrambling phase, while above the crticial swap rate N I vanishes and the system is in the 'absorbing phase'. This was shown to belong to the directed percolation universality class, where bond formation is promoted by the unitary gates and suppressed by the swap operations [14]. In the language of directed percolation, operator backflow can be associated with the formation of long-range temporal bonds in the temporal direction. We now consider the effect of these long-range temporal bonds on the percolation within the impurity.

Figure 7 shows the phase diagram we observe on varying the p as we take v d across the backflow transition. There are four relevant regimes: subsonic velocities v d &lt; v ∗ , supersonic yet subluminal velocities v ∗ &lt; v d ≤ c , superluminal velocities v d &gt; c , and a critical velocity v d = v ∗ . In the subsonic regime, v d &lt; v ∗ , the operator flow is in non-Markovian phase of the 1D model. Here, operators flow back into the system and operator support on the impurity is always maintained; this region is purely scrambling. Conversely, in the superluminal regime, v d &gt; c , the impurity is beyond the deterministic lightcone of the medium and backflow is impossible. However, within this regime there is a region where results differ from the expected Markovian limit. This discrepancy can be attributed to the use of a stochastic drift velocity in our model. This introduces fluctuations, causing the impurity to occasionally traverse within the lightcone, thus deviating from the anticipated Markovian behavior. Despite this deviation, our model faithfully reproduces the Markovian outcomes as v d is increased, exhibiting two distinct phases: a percolating phase where the steady state value of N I ( t ) is greater than zero and an absorbing phase where it vanishes. These phases survive even when v ∗ &lt; v d &lt; c , but the critical swap rate, p c , is shifted. The long-range bonds formed in this region are suppressed exponentially in time and their only affect is to renormalize the probability of the short-range bond formation. This renormalization diverges as we approach the critical velocity, v d = v ∗ , and the probability of long-range bond formation becomes constant. This occurs because, at this velocity, the impurity is perfectly following the centre of the diffuse lightcone boundary within the medium such that from its reference frame the local operator weight is constant in time. Unless the long-range bonds are broken at a comparable, unphysical, rate then the impurity will always percolate.

Figure 7: Phase diagram for the two-dimensional model as a function of swap rate, p , and impurity drift velocity, v d . The absorbing phase corresponds to a steady state with N I = 0, while the percolating phase corresponds to N I &gt; 0 in the steady state. The vertical line in the plot indicates the position of the critical velocity, v ∗ , of the backflow transition in the one-dimensional model. The horizontal line indicates the critical swap rate, p c , of the scrambling phase transition in the Markovian model as reported in Ref. [14].

<!-- image -->

## 5 Information transition

We have shown that an impurity moving in a 1D medium can exhibit a phase transition in operator Markovianity by studying the OTOC dynamics of the system with the impurity reset operation shown in Fig. 4. Operator dynamics has been linked to the spread of information [1, 14], and we will now explore how the phase transition in operator nonMarkovianity manifests in the dynamics of quantum information. Specifically we study the coherent information transmitted through two complementary channels. These channels are those highlighted in the right-hand panel of Figure 8 as Yellow → Blue for the echo protocol and Yellow → Green for the Teleportation protocol. The results in this section were numerically simulated using the QuantumClifford.jl software package [90].

## 5.1 Echo protocol

In the thought experiment, Alice prepares the impurity qubit, I , in a particular state, ρ I , and then allows it to move through the chaotic medium, M , evolving under the circuit described in Section 2. At an intermediate time she discards her qubit and replaces it with a maximally mixed qubit, R . At the end of the experiment, a second party, Bob, obtains access to both the discarded qubit, D , and the medium M . For clarity, we emphasise that Bob cannot access the impurity and has no knowledge of the input states.

We now show that the transition in operator backflow can also be observed in the information Bob has about the state, ρ I , that Alice prepared in the impurity qubit at the beginning of the experiment. We quantify this information using the coherent information [91]. The coherent information is most easily calculated by introducing an ancilla qubit, A , that is maximally entangled with the initial state of Alice's qubit (the impurity). Conceptually, this ancilla acts a memory of the initial state of the impurity, and allows us to track how much of that information remains on the impurity as it interacts with the medium. Note that this protocol is complementary to the one in which Alice prepares a specific state ρ I on the impurity. The coherent information accessible by Bob is then given [91] as

$$I ( A \rightarrow B o b ) = S ( \rho _ { B o b } ) - S ( \rho _ { B o b \cup A } ) ,$$

where S ( ρ C ) = -Tr[ ρ C log 2 ρ C ] is the von-Neumann entanglement entropy of the reduced density matrix of subspace C . The subspace labelled 'Bob' contains the qubits that Bob can access, namely the qubit discarded by Alice and the final state of the medium: Bob ≡ D ∪ M . For a circuit which allows Bob to recover Alice's state ρ I perfectly, his qubits will end up maximally entangled with the ancilla A such that I ( A → Bob) = 1. While if Bob ends up with no information about Alice's state, his qubits and the ancilla will decouple, and I ( A → Bob) ≤ 0.

During the first stage of the protocol, the initial state is entirely encoded in the impurity and the medium subspaces. Immediately after this impurity is discarded, prior to the occurrence of any swaps, this is still true and Bob has perfect access to Alice's initial qubit such that I ( A → Bob) = 1. As long as this remains true, Bob will always have complete information on the initial state. This is certainly true if the dynamics are Markovian. Here there is no operator back flow, the information remains in the medium and again Bob has perfect access to the information in Alice's initial qubit. Once the operator dynamics become non-Markovian, however, some information flows back into Alice's impurity and Bob loses the ability to decode the initial state of Alice's qubits. This is shown in the left-hand panel of Figure 8 where we plot I ( A → Bob) as a function of v d . There we see a transition occurring at the same critical velocity as the backflow transition observed by the OTOC. We again find the diffusive scaling exponents as shown in Figure 9, with the relevant scaling quantity being 1 -I ( A → Bob). This quantity is zero only in the region of zero backflow and increases as the velocity is decreased into the phase of non-zero backflow i.e. it acts as a witness of operator non-Markovianity.

Figure 8: Left: Manifestation of backflow phase transition in coherent information. Here we set t 1 = 100, t 2 = 1000 and p = 0 . 1. This is the result of an average over 400 disorder realizations. Right: Diagram of the general protocol, the colors highlight the qubits accessible by the parties in both the echo and teleportation protocols. In the Markovian phase, there is no backflow and information of the initial state is only accessible via M and D so we expect Bob's decoder fidelity to be maximal. Conversely, Charlie's decoder is dependent on information flowing back onto the fresh impurity, R , and therefore we expect his decoder fidelity to be maximal in the non-Markovian phase.

<!-- image -->

## 5.1.1 Echo decoder

The information accessible to Bob is maximal in the Markovian limit as all of the information about the Alice's qubit has flowed to Bob. We will now describe a decoder which yields a perfect fidelity in this limit and can be used to observe the transition. The decoder is depicted in Figure 10 as the green unitary operations. The construction is similar to the decoder in Ref. [14]; here Bob inserts a new impurity qubit, I ′ , prepared in an infinite temperature state and carries out the time-reversal of the evolution up to that point. The additional reset step in reverse consists of tracing out the impurity and replacing it with Alice's discarded impurity, D . The fidelity of this decoder is then given by the probability of a Bell pair forming between the final state of D and A . Perfect fidelity is achieved when Tr R [ U 2 ρ R ], and by extension Tr I [ U † 2 ρ I ], is unitary, which implies no information is transferred from M to R . When this occurs, such as in the Markovian limit, U † 1 is trivially able to cancel the effect of U 1 and the initial state is recovered.

There is a connection between the coherent information and the decoder fidelity for a given circuit realization given by

$$I ( A \rightarrow B o b ) = 1 + \log _ { 2 } \mathcal { F } ,$$

we derive this in Appendix B. In the supersonic phase the coherent information approaches unity and the decoder achieves perfect fidelity, while in the subsonic phase some information of the initial state flows back onto R such that the decoder can no longer perfectly recover the initial state. We will now outline how a different protocol witnesses the same transition.

Figure 9: Left: Information phase transition around critical point. Right: Data collapse under a finite-time rescaling. Here we set t 1 = 100 and p = 0 . 1. This is the result of an average over 400 disorder realizations.

<!-- image -->

## 5.2 Teleportation protocol

Here we make use of a fundamental property of bipartite entropies to derive a distinct protocol which exhibits an equivalent transition in coherent information but for a channel complementary to the previous protocol. In this new protocol Alice carries out an equivalent role i.e. she prepares the impurity qubit, I , in a specific state, allows it to interact with the medium, M , and then replaces it with a new qubit, R , in an infinite temperature state. Throughout this the total evolution is unitary, as such any information which Bob cannot access from the discarded qubit, D , or the final state of M must be accessible elsewhere in the system. With this in mind we now introduce a third party, Charlie, who is also attempting to deduce information about the initial state of the impurity. Charlie has qubits that are maximally entangled with the initial states of M and R , A M and A R respectively, as well as having access to the final state of R . These new ancilla, A M and A R , play a similar role to A in that they perfectly remember the initial state of the medium and the new qubit. Charlie having access to these implies he can make use of this information to help decode Alice's information. However, unlike Bob, Charlie has no knowledge of the discarded qubit, D , or the final state of M . The degrees of freedom Charlie can access are complementary to those accessible by Bob. This allows us to greatly simplify the calculation of the coherent information available to Charlie.

For pure states, like the one describing the quantum correlations between Alice, Charlie and Bob, all bipartite entanglement entropies satisfy

$$S ( \rho _ { B } ) = S ( \rho _ { B ^ { \perp } } )$$

where B ⊥ is the complement to the subspace B . Take a generic tripartite space consisting of X ∪ Y ∪ Z and consider the coherent informations I ( X → Y ) and I ( X → Z ). Making use of Eq. (12) allows us to relate these in the following way:

$$I ( X \to Y ) & = S ( \rho _ { Y } ) - S ( \rho _ { X U Y } ) \\ & = S ( \rho _ { Y ^ { \perp } } ) - S ( \rho _ { ( X U Y ) ^ { \perp } } ) \\ & = S ( \rho _ { X \cup Z } ) - S ( \rho _ { Z } ) \\ & = - I ( X \to Z ) .$$

Figure 10: Diagram of the decoding protocol. When Alice reliquishes control of the impurity Bob performs a reversal of the dynamics up to that point except he only has access to the medium, M , and the impurity discarded by Alice in the refresh step, D .

<!-- image -->

Applying this relation to the relevant channels of Bob and Charlie then yields

$$I ( A \rightarrow \text {Charlie} ) = - I ( A \rightarrow \text {Bob} ) .$$

This equivalence implies that I ( A → Charlie) must also witness the backflow transition when v d is varied. In contrast to Bob, Charlie has no information about Alice's qubits in the Markovian regime (when Bob can decode perfectly). While, in the regime of operator Non-Markovianity, Charlie has partial information about Alice's qubits.

## 5.2.1 Teleportation decoder

As before, we can construct a decoding protocol that reconstructs this partial information as shown in Figure 11. In that figure, the decoder is shown in green, and we show the diagram for the corresponding fidelity, ˜ F , in Appendix C. There is a clear similarity with the Hayden-Preskill protocol decoder proposed by Yoshida and Kitaev [10]; in both cases a Bell measurement is performed to facilitate the teleportation of Alice's information to Charlie's qubits. The teleportation that Charlie hopes to achieve in this case is indicated by the blue arrow in Figure 11. The success of the teleportation improves when the bell measurement probability is lower (see Appendix C). Given that R and A R are initially in a Bell state, the decoder has the worst fidelity when Tr M [ U 2 ρ M ( t 1 )] is unitary, i.e. U 2 and U ∗ 2 do nothing to disentangle R and A R .

As in the previous protocol, we can relate Charlie's decoder fidelity, ˜ F to the coherent information (details in Appendix C):

$$I ( A \rightarrow \text {Charlie} ) = 1 + \log _ { 2 } \tilde { \mathcal { F } } .$$

The logarithm of the fidelity, therefore also observes the backflow transition. Note, that while Bob's decoder works perfectly in the Markovian phase, Charlie's decoder only partially succeeds in the non-Markovian phase. This is the main difference with the HaydenPreskill protocol, and highlights the fact that the scrambling of operators back on to the impurity is not maximal, as is assumed for the black hole in the Hayden-Preskill protocol.

Figure 11: Diagrams depicting the complementary decoding protocol performed by Charlie given he only has access to the final state of the impurity along with the initial states of the medium and the impurity inserted at the reset state. The blue arrow indicates the goal of the protocol: to teleport information from the initial state of Alice's qubits to Charlie's ancillas.

<!-- image -->

The phase transition in the OTOC dynamics explored in Section 4.1 is related to a revival in operator support on the impurity due to non-Markovian feedback from the medium. However, the non-Markovian effects only arise because of the echo step carried out in the OTOC calculation. This new protocol we have identified undergoes a phase transition in non-Markovianity more aligned with its traditional definition: in terms of the backflow of information from environment to system. While the decoding is facilitated by Charlie initially having access to the medium, this access is lost during the dynamics and the enhancement of the decoder fidelity is driven by feedback of information onto the impurity.

## 6 Operator Markovianty

In this paper we found a model which shows a phase transition in the operator dynamics of an impurity moving through a medium. At slow velocities, the operator dynamics were non-Markovian, while at high velocities the operators dynamics were Markovian. Above, we introduced several protocols that observe the transition, and in this section, we compare non-Markovianity in the operator dynamics to non-Markovianity in time ordered correlations. We capture non-Markovianity in the operator dynamics explicitly with the backflow OTOC introduced in Eq. (4) and Figure 4. The back flow OTOC determines the weight of an operator, initially localized on the impurity, at a late time T on the impurity, given that the impurity was replaced at an earlier time t 1 . The replacement removes all operator support from the impurity such that any subsequent operator support there can only be due to operator support in the environment, which itself must have flowed from the initial impurity, spreading back into the fresh impurity.

While this back flow OTOC detects non-Markovianity in the dynamics of the operator, it does not detect the existence of non-Markovianity in time-ordered correlations. NonMarkovianity in time-ordered correlations can instead be characterized by the operational framework introduced in Ref [75]. Considering non-Markovianity of the impurity in that framework, we must assume that the medium is operationally in accessible. This implies that an echo of the environment cannot be performed and the backflow OTOC cannot be captured by that framework. This also allows for the possibility that the time-ordered correlations do not show non-Markovianity, but the backflow OTOC does. This is likely the case for the dynamics discussed here when the environment is initialized in a maximally mixed state. Even though operators flow back onto the system, they also have large support in the medium, and thus imply large correlations between the system and the environment. Since the chaotic dynamics of the medium spread these correlations nonlocally, they will be inaccessible to the local probes provided by the multi-time correlations of the impurity.

Nonetheless, there is still a notion in which the information dynamics is non-Markovian. This is demonstrated by the two channel capacities and decoders discussed above. For the echo decoder, introduced in Section 5.1, the information accessible to Bob is used to decode Alice's qubit. In the Markovian phase, Bob obtains all information about Alice's qubit and can perfectly decode. In contrast, when operators spread back on to the impurity after t 1 , some of the information is lost to him and he loses some ability to decode. Note that while some information about Alice's qubits has left the medium (Bob's qubits), it has not completely transferred into the impurity. Instead, that information has spread into the correlations between Bob's qubits and the fresh impurity. In both phases, the late-time impurity can not recover Alice's qubit, while only in the Markovian phase, when Bob doesn't lose information due to operator backflow onto the impurity, can Bob decode.

A different reasoning applies to the teleportation decoder discussed in Section 5.2. In contrast to the echo decoder, Charlie requires access to the initial state of the medium, but not the final state. If we consider the medium to be inaccessible at all times such a protocol falls outside the operational notion of non-Markovianity as discussed in Ref [75]. However, if we consider an experiment to have initial access, but to lose that access after the first step of dynamics we match the two pictures. In this case, the fidelity of the teleportation decoder has the form of a multi-time correlation. In the Markovian phase, Charlie cannot decode, and the fidelity vanishes, while in the non-Markovian phase, the teleportation protocol partially succeeds and the fidelity becomes positive.

## 7 Conclusion

Within the framework of random unitary circuits we have studied an impurity moving through a chaotic medium and the flow of information between them as characterized by an OTOC. Information deposited into the medium is rapidly scrambled away from the deposition site at the speed of sound v B . We show that the supersonic ( v &gt; v B ) and subsonic ( v &lt; v B ) impurity velocities correspond to regimes of zero and non-zero operator backflow respectively. This was determined by defining a protocol in which the impurity qubit was swapped with a fresh one uncorrelated with the environment and computing the OTOC on this new qubit. The scaling exponents associated with this transition was shown to be related to the diffusive evolution of the OTOC in the medium.

We considered the implications of the backflow transition on the scrambling transition previously observed in a 1D impurity interacting with a Markovian environment [14]. As expected from that work, this transition is only possible at supersonic velocities where the backflow occurs with a rate which decays exponentially with a characteristic timescale. When this is no longer the case, i.e. when the probability of backflow remains constant or decays algebraically with a small exponent as in Appendix A, there can be no absorbing phase. However, in the case of power-law decay, there is a potential for the transition to survive, provided the power is sufficiently large [92].

We went on to show how the operator non-Markovanity transition is also manifest in a quantum channel capacity, namely that between the initial impurity state and the final state of the environment plus the qubit discarded in the backflow protocol. We associated with this channel a decoder whose fidelity was closely related to the channel capacity and became ideal in the Markovian limit. By considering the complement to this quantum channel we then derived an alternative protocol which resembles the proposed in [10] for the Hayden-Preskill protocol. In this case the performance of the decoder was tied to the degree of backflow from the environment becoming optimal in the non-Markovian limit.

We have presented a relatively simple model that undergoes a phase transition in information backflow. Similar to the scrambling transition [14] and the measurement induced phase transition (MIPT) [35,36,93,94], the transition occurs in the dynamics of information. Unlike the MIPT, but similar to the scrambling transition, there is no exponential time complexity barrier in observing the backflow transition. Similar to the scrambling transition, the dynamics of information in the backflow transition can be observed using one of the two simple decoder shown above. The main gain in comparison to the scrambling transition (which requires storing L 2 qubits of the medium) is that the backflow transition occurs in 1D medium, and only requires storing L qubits during the time evolution and decoding. This difference may be of importance when simulating the transitions on near term quantum computers.

Beyond realizing this transition on modern near-term devices other promising directions would be to extend this to a more realistic open quantum model such as a spin-boson type model [95,96] or a Kondo model [97]. Already we can draw some conclusions when considering a mobile impurity coupled non-chaotic environments such as these. A typical example is a mobile atom coupled to electromagnetic radiation. In this case, the impurity is not only Markovian if it moves outside the light cone, but can also be if it moves inside the light cone. This is because operators dynamics are ballistic in a wave medium [98], and operators only have significant support close to the light cone. This is in contrast to a generic chaotic medium, where operators have non-negligible support through out the light cone. In studying open quantum systems closer to reality, recent techniques developed to treat non-Markovian dynamics will be of great assistance [99-103].

## Acknowledgements

The authors gratefully acknowledge the computing time granted on the supercomputer MOGON 2 at Johannes Gutenberg-University Mainz (hpc.uni-mainz.de).

Funding information This work has been funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) - TRR 288 - 422213477 (project B09), TRR 306 QuCoLiMa ('Quantum Cooperativity of Light and Matter'), Project-ID 429529648 (project D04) and in part by the QuantERA II Programme that has received funding from the European Union's Horizon 2020 research and innovation programme under Grant Agreement No 101017733 ('QuSiED') and by the DFG (project number 499037529), and by the Dynamics and Topology Centre funded by the State of Rhineland Palatinate.

## A Alternate 1D circuit

Here we show that the backflow transition, with modified exponents, also occurs when the 1D model of the main text is slightly modified. We now allow for scrambling to only occur up to the position of the impurity as depicted in Figure 12. In this case the backflow order parameter on variation of v d is shown in Figure 13. The change to the circuit modifies the spread of the operator within the environment and in particular the weight of the OTOC

Figure 12: Cartoon of the modified boundary conidition where scrambling in the environment, as indicated by the green region, can only occur up to the position of the impurity, the dashed line.

<!-- image -->

Figure 13: Backflow order parameter for the alternate circuit on variation of impurity drift velocity. Here we set t 1 = 100, t 2 = 1000 and p = 0 . 1. This is the result of an average over 10 4 disorder realizations.

<!-- image -->

at the impurity position which is instead given by

$$P _ { 1 } ( v _ { d } , t ) = \frac { \exp \left ( \frac { - v ^ { 2 } t } { 4 D } \right ) } { \sqrt { \pi D t } \left [ 1 + \text {erf} \left ( \frac { v \sqrt { t } } { 2 \sqrt { D } } \right ) \right ] } .$$

This in turn satisfies a distinct scaling relation:

$$P _ { 1 } ( v , t ) = \sqrt { t } F _ { 1 } ( v \sqrt { t } ) ,$$

and we see this manifest as well in the scaling of the backflow order parameter in Figure 14

Figure 14: Left: Expanded view of the backflow phase transition for the alternate circuit near the critical point. Right: Data collapse under a finite-time rescaling. Here we set t 1 = 100 and p = 0 . 1. This is the result of an average over 10 4 disorder realizations.

<!-- image -->

Figure 15: Left: The fidelity of Bob's decoding protocol for a given unitary circuit, U , and initial states: ρ M , ρ R and ρ I ′ . Right: The purity of the reduced density matrix ρ A ∪ Bob . If ρ M , ρ I ′ and ρ R are all infinite temperature states then these two diagrams are equivalent down to a numerical factor.

<!-- image -->

## B Derivation of Eq. (11)

The fidelity of the decoder for Bob's protocol is related to the purity of the reduced density matrix ρ A ∪ Bob prior to decoding via

$$\mathcal { F } = d _ { M } ^ { - 1 } \text {Tr} ( \rho _ { A \cup B o b } ^ { 2 } ) ,$$

where d M is the Hilbert space dimension of the medium; we show this diagrammatically in Figure 15. By manipulating the fidelity diagram the decoder becomes a replica in the purity diagram. These two diagrams correspond when ρ M , ρ I ′ and ρ R are infinite temperature states. Infinite temperature states in the fidelity are related to trace operations in the purity (and vice versa ) via

$$\rho _ { B } ^ { \infty } \leftrightarrow d _ { B } ^ { - 1 } \text {Tr} _ { B } [ \cdot ] ,$$

where d B is the Hilbert space dimension of B . These dimensional factors mostly cancel in our case except for d M .

Now, the entanglement spectrum for Clifford circuits is flat[]; this results in an equivalence between Renyi entropies, S n ( ρ C ), defined by

$$S _ { n } ( \rho _ { C } ) = \frac { 1 } { n - 1 } \log _ { 2 } \text {Tr} [ \rho _ { C } ^ { n } ] .$$

This combined with the relation S ( ρ C ) = lim n → 1 S n ( ρ C ) allows us to make the following substitutions:

$$I ( A \rightarrow B o b ) & = S _ { 2 } ( \rho _ { B o b } ) - S _ { 2 } ( \rho _ { A \cup B o b } ) \\ & = - \log _ { 2 } T r [ \rho _ { B o b } ^ { 2 } ] + \log _ { 2 } T r [ \rho _ { A \cup B o b } ^ { 2 } ] \\ & = 1 + \log _ { 2 } \mathcal { F } ,$$

where to arrive at the last line we used S 2 ( ρ Bob ) = -log 2 ( d M d I ) = 1 -log 2 ( d M ).

Figure 16: The fidelity of the second Hayden-Preskill-like protocol of the main text. The numerator trivially contracts to yield a constant factor and the nontrivial dependence on the unitary appears in the probability of measuring a bell pair, P EPR

<!-- image -->

.

## C Details of HP fidelity and derivation of Eq. (15)

The fidelity for Charlie's decoding protocol is shown diagrammatically in Figure 16 where the only non-trivial factor is given by the probability of measuring a Bell pair, P EPR . By comparing the diagram for P EPR and that for the original decoder's fidelity, F in Figure 15, it is apparent that

$$P _ { E P R } \equiv \mathcal { F } .$$

The numerator in ˜ F trivally contracts to yield a factor of d -2 I where d I is the Hilbert space dimension of the impurity. Altogether we have the following relation between the two fidelities:

$$\mathcal { F } = \frac { 1 } { \tilde { \mathcal { F } } d _ { I } ^ { 2 } } .$$

Substituting this into Eq. (11) and making use of Eq. (14) (along with d I = 2) then yields Eq. (15).

## References

- [1] P. Hayden and J. Preskill, Black holes as mirrors: Quantum information in random subsystems , J. High Energy Phys. 2007 (09), 120 (2007), doi:10.1088/11266708/2007/09/120.
- [2] Y. Sekino and L. Susskind, Fast scramblers , J. High Energy Phys. 2008 (10), 065 (2008), doi:10.1088/1126-6708/2008/10/065.
- [3] J. Maldacena, S. H. Shenker and D. Stanford, A bound on chaos , J. High Energy Phys. 2016 (8), 106 (2016), doi:10.1007/JHEP08(2016)106.
- [4] B. Swingle, Unscrambling the physics of out-of-time-order correlators , Nat. Phys. 14 (10), 988 (2018), doi:10.1038/s41567-018-0295-5.
- [5] D. Ben-Zion and J. McGreevy, Strange metal from local quantum chaos , Phys. Rev. B 97 (15), 155117 (2018), doi:10.1103/PhysRevB.97.155117.
- [6] M. Blake, R. A. Davison and S. Sachdev, Thermal diffusivity and chaos in metals without quasiparticles , Phys. Rev. D 96 (10), 106008 (2017), doi:10.1103/PhysRevD.96.106008.
- [7] N. Dowling and K. Modi, An operational metric for quantum chaos and the corresponding spatiotemporal entanglement structure , doi:10.48550/arXiv.2210.14926 (2023).
- [8] L. Piroli, C. S¨ underhauf and X.-L. Qi, A random unitary circuit model for black hole evaporation , J. High Energy Phys. 2020 (4), 63 (2020), doi:10.1007/JHEP04(2020)063.
- [9] D. N. Page, Average entropy of a subsystem , Phys. Rev. Lett. 71 (9), 1291 (1993), doi:10.1103/PhysRevLett.71.1291.
- [10] B. Yoshida and A. Kitaev, Efficient decoding for the Hayden-Preskill protocol , doi:10.48550/arXiv.1710.03363 (2017).
- [11] Y.-L. Zhang, Y. Huang and X. Chen, Information scrambling in chaotic systems with dissipation , Phys. Rev. B 99 (1), 014303 (2019), doi:10.1103/PhysRevB.99.014303.
- [12] P. Zanardi and N. Anand, Information scrambling and chaos in open quantum systems , Phys. Rev. A 103 (6), 062214 (2021), doi:10.1103/PhysRevA.103.062214.
- [13] B. Yoshida and N. Y. Yao, Disentangling scrambling and decoherence via quantum teleportation , Phys. Rev. X 9 (1), 011006 (2019), doi:10.1103/PhysRevX.9.011006.
- [14] Z. Weinstein, S. P. Kelly, J. Marino and E. Altman, Scrambling transition in a radiative random unitary circuit , Phys. Rev. Lett. 131 (22), 220404 (2023), doi:10.1103/PhysRevLett.131.220404.
- [15] T. Schuster and N. Y. Yao, Operator growth in open quantum systems , doi:10.48550/arXiv.2208.12272 (2022).
- [16] M. Knap, Entanglement production and information scrambling in a noisy spin system , Phys. Rev. B 98 (18), 184416 (2018), doi:10.1103/PhysRevB.98.184416.

- [17] F. D. Dom´ ınguez and G. A. ´ Alvarez, Dynamics of quantum information scrambling under decoherence effects measured via active spins clusters , Phys. Rev. A 104 (6), 062406 (2021), doi:10.1103/PhysRevA.104.062406.
- [18] F. D. Dom´ ınguez, M. C. Rodr´ ıguez, R. Kaiser, D. Suter and G. A. ´ Alvarez, Decoherence scaling transition in the dynamics of quantum information scrambling , Phys. Rev. A 104 (1), 012402 (2021), doi:10.1103/PhysRevA.104.012402.
- [19] F. Andreadakis, N. Anand and P. Zanardi, Scrambling of algebras in open quantum systems , Phys. Rev. A 107 (4), 042217 (2023), doi:10.1103/PhysRevA.107.042217.
- [20] A. Bhattacharya, P. Nandy, P. P. Nath and H. Sahu, Operator growth and Krylov construction in dissipative open quantum systems , J. High Energy Phys. 2022 (12), 81 (2022), doi:10.1007/JHEP12(2022)081.
- [21] B. Bhattacharjee, X. Cao, P. Nandy and T. Pathak, Operator growth in open quantum systems: Lessons from the dissipative SYK , J. High Energy Phys. 2023 (3), 54 (2023), doi:10.1007/JHEP03(2023)054.
- [22] A. Bhattacharya, P. Nandy, P. P. Nath and H. Sahu, On Krylov complexity in open systems: an approach via bi-Lanczos algorithm , J. High Energy Phys. 2023 (12) (2023), doi:10.1007/jhep12(2023)066.
- [23] S. Popescu, A. J. Short and A. Winter, The foundations of statistical mechanics from entanglement: Individual states vs. averages , Nat. Phys. 2 (11), 754 (2006), doi:10.1038/nphys444.
- [24] J. M. Deutsch, Quantum statistical mechanics in a closed system , Phys. Rev. A 43 (4), 2046 (1991), doi:10.1103/PhysRevA.43.2046.
- [25] M. Srednicki, Chaos and quantum thermalization , Phys. Rev. E 50 (2), 888 (1994), doi:10.1103/PhysRevE.50.888.
- [26] G. D. Berk, S. Milz, F. A. Pollock and K. Modi, Extracting quantum dynamical resources: Consumption of non-Markovianity for noise reduction , npj Quantum Inf. 9 , 1 (2021).
- [27] B. Bylicka, D. Chru´ sci´ nski and S. Maniscalco, Non-Markovianity and reservoir memory of quantum channels: A quantum information theory perspective , Sci. Rep. 4 (2014).
- [28] K. Kawabata, Y. Ashida and M. Ueda, Information retrieval and criticality in parity-time-symmetric systems , Phys. Rev. Lett. 119 , 190401 (2017), doi:10.1103/PhysRevLett.119.190401.
- [29] L. Xiao, K. Wang, X. Zhan, Z. Bian, K. Kawabata, M. Ueda, W. Yi and P. Xue, Observation of critical phenomena in parity-time-symmetric quantum dynamics , Phys. Rev. Lett. 123 , 230401 (2019), doi:10.1103/PhysRevLett.123.230401.
- [30] M. Huang, R.-K. Lee, L. Zhang, S.-M. Fei and J. Wu, Simulating broken PT -symmetric Hamiltonian systems by weak measurement , Phys. Rev. Lett. 123 , 080404 (2019), doi:10.1103/PhysRevLett.123.080404.
- [31] L. Ding, K. Shi, Y. Wang, Q. Zhang, C. Zhu, L. Zhang, J. Yi, S. Zhang, X. Zhang and W. Zhang, Information retrieval and eigenstate coalescence in a non-Hermitian quantum system with antiPT symmetry , Phys. Rev. A 105 , L010204 (2022), doi:10.1103/PhysRevA.105.L010204.

- [32] A. M. Garc´ ıa-Garc´ ıa, Y. Jia, D. Rosa and J. J. M. Verbaarschot, Dominance of replica off-diagonal configurations and phase transitions in a PT symmetric Sachdev-Ye-Kitaev model , Phys. Rev. Lett. 128 , 081601 (2022), doi:10.1103/PhysRevLett.128.081601.
- [33] Y.-L. Fang, J.-L. Zhao, Y. Zhang, D. Chen, Q. Wu, Y.-H. Zhou, C. Yang and F. Nori, Experimental demonstration of coherence flow in PT - and antiPT -symmetric systems , Commun. Phys. 4 , 1 (2021), doi:10.1038/s42005-021-00728-8.
- [34] W.-L. Zhao, R.-R. Wang, H. Ke and J. Liu, Scaling laws of the out-of-time-order correlators at the transition to the spontaneous PT -symmetry breaking in a floquet system , Phys. Rev. A 107 , 062201 (2023), doi:10.1103/PhysRevA.107.062201.
- [35] B. Skinner, J. Ruhman and A. Nahum, Measurement-induced phase transitions in the dynamics of entanglement , Phys. Rev. X 9 (3), 031009 (2019), doi:10.1103/PhysRevX.9.031009.
- [36] Y. Li, X. Chen and M. P. A. Fisher, Measurement-driven entanglement transition in hybrid quantum circuits , Phys. Rev. B 100 (13), 134306 (2019), doi:10.1103/PhysRevB.100.134306.
- [37] A. Chan, R. M. Nandkishore, M. Pretko and G. Smith, Unitary-projective entanglement dynamics , Phys. Rev. B 99 , 224307 (2019), doi:10.1103/PhysRevB.99.224307.
- [38] M. J. Gullans and D. A. Huse, Dynamical purification phase transition induced by quantum measurements , Phys. Rev. X 10 , 041020 (2020), doi:10.1103/PhysRevX.10.041020.
- [39] R. Fan, S. Vijay, A. Vishwanath and Y.-Z. You, Self-organized error correction in random unitary circuits with measurement , Phys. Rev. B 103 , 174309 (2021), doi:10.1103/PhysRevB.103.174309.
- [40] S. Choi, Y. Bao, X.-L. Qi and E. Altman, Quantum error correction in scrambling dynamics and measurement-induced phase transition , Phys. Rev. Lett. 125 , 030505 (2020), doi:10.1103/PhysRevLett.125.030505.
- [41] M. J. Gullans and D. A. Huse, Scalable probes of measurement-induced criticality , Phys. Rev. Lett. 125 , 070606 (2020), doi:10.1103/PhysRevLett.125.070606.
- [42] Y. Li and M. P. A. Fisher, Statistical mechanics of quantum error correcting codes , Phys. Rev. B 103 , 104306 (2021), doi:10.1103/PhysRevB.103.104306.
- [43] C. Noel, P. Niroula, D. Zhu, A. Risinger, L. Egan, D. Biswas, M. Cetina, A. V. Gorshkov, M. J. Gullans, D. A. Huse and C. Monroe, Observation of measurementinduced quantum phases in a trapped-ion quantum computer , Nat. Phys. 18 (7), 760 (2022), doi:10.1038/s41567-022-01619-7.
- [44] J. C. Hoke, M. Ippoliti, E. Rosenberg, D. Abanin, R. Acharya, T. I. Andersen, M. Ansmann, F. Arute, K. Arya, A. Asfaw, J. Atalaya, J. C. Bardin et al. , Measurement-induced entanglement and teleportation on a noisy quantum processor , Nature 622 (7983), 481-486 (2023), doi:10.1038/s41586-023-06505-7.
- [45] Y. Bao, M. Block and E. Altman, Finite-time teleportation phase transition in random quantum circuits , Phys. Rev. Lett. 132 , 030401 (2024), doi:10.1103/PhysRevLett.132.030401.

- [46] M. Ippoliti and V. Khemani, Postselection-free entanglement dynamics via spacetime duality , Phys. Rev. Lett. 126 (6), 060501 (2021), doi:10.1103/PhysRevLett.126.060501.
- [47] T.-C. Lu and T. Grover, Spacetime duality between localization transitions and measurement-induced transitions , PRX Quantum 2 , 040319 (2021), doi:10.1103/PRXQuantum.2.040319.
- [48] B. Fert´ e and X. Cao, A solvable model of quantum Darwinism-encoding transitions , doi:10.48550/arXiv.2305.03694 (2023).
- [49] X. Turkeshi, R. Fazio and M. Dalmonte, Measurement-induced criticality in (2 + 1) -dimensional hybrid quantum circuits , Phys. Rev. B 102 , 014315 (2020), doi:10.1103/PhysRevB.102.014315.
- [50] O. Lunt, M. Szyniszewski and A. Pal, Measurement-induced criticality and entanglement clusters: A study of one-dimensional and two-dimensional Clifford circuits , Phys. Rev. B 104 , 155111 (2021), doi:10.1103/PhysRevB.104.155111.
- [51] P. Sierant, M. Schir` o, M. Lewenstein and X. Turkeshi, Measurement-induced phase transitions in ( d + 1) -dimensional stabilizer circuits , Phys. Rev. B 106 , 214316 (2022), doi:10.1103/PhysRevB.106.214316.
- [52] S.-K. Jian, C. Liu, X. Chen, B. Swingle and P. Zhang, Measurement-induced phase transition in the monitored Sachdev-Ye-Kitaev model , Phys. Rev. Lett. 127 , 140601 (2021), doi:10.1103/PhysRevLett.127.140601.
- [53] B. Bhattacharjee, P. Nandy and T. Pathak, Operator dynamics in Lindbladian SYK: A Krylov complexity perspective , J. High Energy Phys. 2024 , 1 (2023), doi:10.1007/JHEP01(2024)094.
- [54] A. Milekhin and F. K. Popov, Measurement-induced phase transition in teleportation and wormholes , doi:10.48550/arXiv.2210.03083 (2023).
- [55] O. Lunt and A. Pal, Measurement-induced entanglement transitions in many-body localized systems , Phys. Rev. Res. 2 (4), 043072 (2020), doi:10.1103/PhysRevResearch.2.043072.
- [56] K. Yamamoto and R. Hamazaki, Localization properties in disordered quantum many-body dynamics under continuous measurement , Phys. Rev. B 107 , L220201 (2023), doi:10.1103/PhysRevB.107.L220201.
- [57] H. Wang, C. Liu, P. Zhang and A. M. Garc´ ıa-Garc´ ıa, Entanglement transition and replica wormhole in the dissipative Sachdev-Ye-Kitaev model , doi:10.48550/arXiv.2306.12571 (2023).
- [58] R. Vasseur, A. C. Potter, Y.-Z. You and A. W. W. Ludwig, Entanglement transitions from holographic random tensor networks , Phys. Rev. B 100 (13) (2019), doi:10.1103/PhysRevB.100.134203.
- [59] Z.-C. Yang, Y. Li, M. P. A. Fisher and X. Chen, Entanglement phase transitions in random stabilizer tensor networks , Phys. Rev. B 105 , 104306 (2022), doi:10.1103/PhysRevB.105.104306.
- [60] S. P. Kelly and J. Marino, Information exchange symmetry breaking in quantumenhanced experiments , doi:10.48550/arXiv.2310.03061 (2023).

- [61] I. Lovas, U. Agrawal and S. Vijay, Quantum coding transitions in the presence of boundary dissipation , doi:10.48550/arxiv.2304.02664 (2023).
- [62] M. Tsitsishvili, D. Poletti, M. Dalmonte and G. Chiriac` o, Measurement induced transitions in non-Markovian free fermion ladders , doi:10.48550/arXiv.2307.06624 (2023).
- [63] G. Chiriac` o, M. Tsitsishvili, D. Poletti, R. Fazio and M. Dalmonte, Diagrammatic method for many-body non-Markovian dynamics: Memory effects and entanglement transitions , Phys. Rev. B 108 , 075151 (2023), doi:10.1103/PhysRevB.108.075151.
- [64] G. L. Giorgi, S. Longhi, A. Cabot and R. Zambrini, Quantum probing topological phase transitions by non-Markovianity , Ann. Phys. (Berl.) 531 (12), 1900307 (2019), doi:10.1002/andp.201900307.
- [65] M. Saha, B. K. Agarwalla and B. P. Venkatesh, Readout of quasiperiodic systems using qubits , Phys. Rev. A 103 (2), 023330 (2021), doi:10.1103/PhysRevA.103.023330.
- [66] M. P. A. Fisher, V. Khemani, A. Nahum and S. Vijay, Random quantum circuits , Annu. Rev. Condens. Matter Phys. 14 (1), 335 (2023), doi:10.1146/annurevconmatphys-031720-030658.
- [67] A. Nahum, S. Vijay and J. Haah, Operator spreading in random unitary circuits , Phys. Rev. X 8 (2), 021014 (2018), doi:10.1103/PhysRevX.8.021014.
- [68] C. von Keyserlingk, T. Rakovszky, F. Pollmann and S. Sondhi, Operator hydrodynamics, OTOCs, and entanglement growth in systems without conservation laws , Phys. Rev. X 8 (2), 021013 (2018), doi:10.1103/PhysRevX.8.021013.
- [69] D. Maertens, N. Bultinck and K. Van Acoleyen, Hawking radiation on the lattice from Floquet and local Hamiltonian quench dynamics , Phys. Rev. B 109 (1), 014309 (2024), doi:10.1103/PhysRevB.109.014309.
- [70] A. De Luca and A. Bastianello, Entanglement front generated by an impurity traveling in an isolated many-body quantum system , Phys. Rev. B 101 (8), 085139 (2020), doi:10.1103/PhysRevB.101.085139.
- [71] P. Mitra, M. Ippoliti, R. N. Bhatt, S. L. Sondhi and K. Agarwal, Cooling arbitrary near-critical systems using hyperbolic quenches , Phys. Rev. B 99 (10), 104308 (2019), doi:10.1103/PhysRevB.99.104308.
- [72] A. Bastianello and A. De Luca, Nonequilibrium steady state generated by a moving defect: the supersonic threshold , Phys. Rev. Lett. 120 (6), 060602 (2018), doi:10.1103/PhysRevLett.120.060602.
- [73] A. Bastianello and A. De Luca, Superluminal moving defects in the Ising spin chain , Phys. Rev. B 98 (6), 064304 (2018), doi:10.1103/PhysRevB.98.064304.
- [74] K. Agarwal, R. N. Bhatt and S. Sondhi, Fast preparation of critical ground states using superluminal fronts , Phys. Rev. Lett. 120 (21), 210604 (2018), doi:10.1103/PhysRevLett.120.210604.
- [75] F. A. Pollock, C. Rodr´ ıguez-Rosario, T. Frauenheim, M. Paternostro and K. Modi, Operational Markov condition for quantum processes , Phys. Rev. Lett. 120 (4), 040405 (2018), doi:10.1103/PhysRevLett.120.040405, 1801.09811 .

- [76] Z. Webb, The Clifford group forms a unitary 3-design , Quantum Inf. Comput. 16 (15-16), 1379-1400 (2016), doi:10.26421/QIC16.15-16-8.
- [77] Y. E. Shchadilova, R. Schmidt, F. Grusdt and E. Demler, Quantum dynamics of ultracold Bose polarons , Phys. Rev. Lett. 117 (11), 113002 (2016), doi:10.1103/PhysRevLett.117.113002.
- [78] K. Seetharam, Y. Shchadilova, F. Grusdt, M. B. Zvonarev and E. Demler, Dynamical quantum Cherenkov transition of fast impurities in quantum liquids , Phys. Rev. Lett. 127 (18), 185302 (2021), doi:10.1103/PhysRevLett.127.185302.
- [79] K. Seetharam, Y. Shchadilova, F. Grusdt, M. Zvonarev and E. Demler, Quantum Cherenkov transition of finite momentum Bose polarons , doi:10.48550/arXiv.2109.12260 (2021).
- [80] M. Will, J. Marino, H. Ott and M. Fleischhauer, Controlling superfluid flows using dissipative impurities , SciPost Phys. 14 (4), 064 (2023), doi:10.21468/SciPostPhys.14.4.064.
- [81] J. Marino, G. Menezes and I. Carusotto, Zero-point excitation of a circularly moving detector in an atomic condensate and phonon laser dynamical instabilities , Phys. Rev. Res. 2 (4), 042009 (2020), doi:10.1103/PhysRevResearch.2.042009.
- [82] H.-P. Breuer, E.-M. Laine, J. Piilo and B. Vacchini, Colloquium: Non-Markovian dynamics in open quantum systems , Rev. Mod. Phys. 88 (2), 021002 (2016), doi:10.1103/RevModPhys.88.021002.
- [83] P. Taranto, S. Milz, F. A. Pollock and K. Modi, Structure of quantum stochastic processes with finite Markov order , Phys. Rev. A 99 , 042108 (2019), doi:10.1103/PhysRevA.99.042108.
- [84] G. A. L. White, K. Modi and C. D. Hill, Filtering crosstalk from bath nonMarkovianity via spacetime classical shadows , Phys. Rev. Lett. 130 , 160401 (2023), doi:10.1103/PhysRevLett.130.160401.
- [85] S. Milz and K. Modi, Quantum stochastic processes and quantum non-Markovian phenomena , PRX Quantum 2 , 030201 (2021), doi:10.1103/PRXQuantum.2.030201.
- [86] P. Taranto, F. A. Pollock and K. Modi, Non-Markovian memory strength bounds quantum process recoverability , npj Quantum Inf. 7 (1), 149 (2021), doi:10.1038/s41534-021-00481-4.
- [87] U. Shrikant and P. Mandayam, Quantum non-Markovianity: Overview and recent developments , Front. Quantum Sci. Technol. 2 , 1134583 (2023), doi:10.3389/frqst.2023.1134583.
- [88] F. Sakuldee, S. Milz, F. A. Pollock and K. Modi, Non-Markovian quantum control as coherent stochastic trajectories , J. Phys. A 51 (41), 414014 (2018), doi:10.1088/17518121/aabb1e.
- [89] M. Zonnios, J. Levinsen, M. M. Parish, F. A. Pollock and K. Modi, Signatures of quantum chaos in an out-of-time-order tensor , Phys. Rev. Lett. 128 (15), 150601 (2022), doi:10.1103/PhysRevLett.128.150601, 2105.08282 .
- [90] QuantumSavory/QuantumClifford.jl , Quantum Savory, https://github.com/ QuantumSavory/QuantumClifford.jl .

- [91] S. Lloyd, Capacity of the noisy quantum channel , Phys. Rev. A 55 (3), 1613 (1997), doi:10.1103/PhysRevA.55.1613.
- [92] A. Jimenez-Dalmaroni, Directed percolation with incubation times , Phys. Rev. E 74 (1), 011123 (2006), doi:10.1103/PhysRevE.74.011123, cond-mat/0603151 .
- [93] C.-M. Jian, Y.-Z. You, R. Vasseur and A. W. W. Ludwig, Measurement-induced criticality in random quantum circuits , Phys. Rev. B 101 (10), 104302 (2020), doi:10.1103/PhysRevB.101.104302.
- [94] Y. Bao, S. Choi and E. Altman, Theory of the phase transition in random unitary circuits with measurements , Phys. Rev. B 101 (10), 104301 (2020), doi:10.1103/PhysRevB.101.104301.
- [95] H.-P. Breuer and F. Petruccione, The Theory of Open Quantum Systems , Oxford University Press, ISBN 978-0-19-852063-4 (2002).
- [96] A. O. Caldeira and A. J. Leggett, Quantum tunnelling in a dissipative system , Ann. Phys. (N. Y.) 149 (2), 374 (1983), doi:10.1016/0003-4916(83)90202-6.
- [97] A. C. Hewson, The Kondo Problem to Heavy Fermions , Cambridge Studies in Magnetism. Cambridge University Press, Cambridge, ISBN 978-0-521-59947-4, doi:10.1017/CBO9780511470752 (1993).
- [98] C.-J. Lin and O. I. Motrunich, Out-of-time-ordered correlators in a quantum Ising chain , Phys. Rev. B 97 , 144304 (2018), doi:10.1103/PhysRevB.97.144304.
- [99] G. E. Fux, D. Kilda, B. W. Lovett and J. Keeling, Tensor network simulation of chains of non-Markovian open quantum systems , Phys. Rev. Res. 5 , 033078 (2023), doi:10.1103/PhysRevResearch.5.033078.
- [100] D. Gribben, A. Strathearn, G. E. Fux, P. Kirton and B. W. Lovett, Using the environment to understand non-Markovian open quantum systems , Quantum 6 , 847 (2022), doi:10.22331/q-2022-10-25-847.
- [101] A. Lerose, M. Sonner and D. A. Abanin, Overcoming the entanglement barrier in quantum many-body dynamics via space-time duality , Phys. Rev. B 107 , L060305 (2023), doi:10.1103/PhysRevB.107.L060305.
- [102] J. Thoenniss, A. Lerose and D. A. Abanin, Nonequilibrium quantum impurity problems via matrix-product states in the temporal domain , Phys. Rev. B 107 , 195101 (2023), doi:10.1103/PhysRevB.107.195101.
- [103] M. R. Jørgensen and F. A. Pollock, Exploiting the causal tensor network structure of quantum processes to efficiently simulate non-Markovian path integrals , Phys. Rev. Lett. 123 , 240602 (2019), doi:10.1103/PhysRevLett.123.240602.