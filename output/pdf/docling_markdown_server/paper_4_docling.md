## Thermalization propagation front and robustness against avalanches in localized systems

Annarita Scocco , 1 Gianluca Passarelli , 2 Mario Collura , 3, 4 Procolo Lucignano , 2 and Angelo Russomanno 2

1 Scuola Superiore Meridionale, Largo San Marcellino 10, I-80138 Napoli, Italy

2 Dipartimento di Fisica 'E. Pancini', Universit` a di Napoli Federico II,

Complesso di Monte S. Angelo, via Cinthia, I-80126 Napoli, Italy

3 SISSA, Via Bonomea 265, I-34136 Trieste, Italy

4 INFN, Sezione di Trieste, Via Valerio 2, 34127 Trieste, Italy

We investigate the robustness of the many-body localized (MBL) phase to the quantum-avalanche instability by studying the dynamics of a localized spin chain coupled to a T = ∞ thermal bath through its leftmost site. By analyzing local magnetizations we estimate the size of the thermalized sector of the chain and find that it increases logarithmically slowly in time. This logarithmically slow propagation of the thermalization front allows us to lower bound the slowest thermalization time, and find a broad parameter range where it scales fast enough with the system size that MBL is robust against thermalization induced by avalanches. The further finding that the imbalance - a global quantity measuring localization - thermalizes over an exponential time scale both in disorder strength and system size is in agreement with these results.

## I. INTRODUCTION

Thermalization in quantum systems occurs in a way remarkably different than in classical systems, by a mechanism called eigenstate thermalization hypothesis (ETH) [1-3]. In a thermalizing quantum system eigenstates are locally equivalent to thermal density matrices, and this gives rise to long-time thermalization of local observables [4-6]. Generic isolated quantum systems are expected to thermalize and obey ETH [7]. It is therefore of particular interest to find systems that avoid thermalization: In this case, quantum information encoded in the initial state can persist for long times, with relevance for technological applications, as quantum memories [8].

In an ergodic system, thermalization occurs because its various parts can exchange particles and energy, so a possible way for a system to avoid thermalization is to exhibit insulating behavior, an example of which is given by Anderson localization [9], occurring in noninteracting disordered systems. In the presence of small enough interactions, the system is still space localized and non thermalizing, a phenomenon called many-body localization (MBL) [10]. Following the works [11, 12], this topic has been tremendously explored over the past few years, from a theoretical [13-15], experimental [1621], and numerical [22-33] point of view, particularly focusing on one-dimensional systems. MBL systems display many interesting features such as the emergence of a complete set of quasi-localized integrals of motion [34-36], area law entanglement in all many-body eigenstates [25, 37, 38], logarithmic growth of entanglement entropy with time [23, 37, 39, 40]. This last slowentanglement-growth property is especially relevant, due the role played by entanglement in giving rise to ETH of local observables [41]. The properties of MBL systems have been extensively described in different reviews [4244].

However, the stability of this regime has been put into question in the thermodynamic limit, as it was pointed out that under certain circumstances many-body localized systems may be unstable towards rare regions of small disorder by a mechanism dubbed 'quantum avalanches' [45]. This phenomenon has been considered in one- or higher-dimensional systems, both theoretically [46-49] and experimentally [50, 51], studying the spectral properties or the dynamics of a MBL system in contact with an ergodic inclusion [52-54]. In some important cases the effect of the ergodic inclusion was studied using a Lindbladian acting on an end of the system [5557], as we better clarify below. [58]

The search for evidence of the avalanche mechanism in standard MBL models is still very active. One possible approach is through many-body resonances, which allow globally different spin configurations to interact [57, 59, 60]. They are negligible in the MBL phase but there is a crossover regime where they become more and more relevant with increasing system size. This leads eventually to avalanches [57], that spread just thanks to the coupling between rare near-resonant eigenstates [61]. Avalanches are also related to interaction-driven instabilities seen in the behavior of correlation lengths [62]. From the experimental point of view, in Ref. [50], avalanche spread is monitored by measuring the site-resolved entropy over time.

The studies mentioned above argue in favor of the robustness of MBL to avalanches, although robustness occurs above a disorder-strength threshold larger than the one corresponding to the finite-size crossover to MBL. There are also critical voices to the existence of MBL in the thermodynamic limit. They report a crossover point to MBL that linearly increases with the system size. In [63, 64] this result is obtained by numerically analyzing the ratio of the Thouless time and the Heisenberg time obtained from the spectral form factor, and in [65] by numerically studying the behavior of the fidelity susceptibility. These are all numerical finite-size results, so the question is still debated, and far from being settled, because finite-size numerical results cannot be univocally extrapolated to the thermodynamic limit [44].

Our contribution comes into this debate by looking from a different perspective at the idea that an ergodic inclusion, which occurs almost certainly in sufficiently large systems, can thermalize the entire chain if the thermalization time of any subchain is short enough [57]. This time can be numerically estimated by coupling a subchain to a thermal bath by one of its ends, simulating the already thermalized part of the chain. If the slowest thermalization time, corresponding to the time it takes for the farthest spin to thermalize, scales slowly enough with the size of the subchain, then the avalanche propagates and the system thermalizes [55, 57].

In this work, we suggest a different way to estimate this thermalization time, based on the logarithmically slow propagation of the heat. We couple an MBL system to a T = ∞ thermal bath by one of its extremities and study how the slowest thermalization time scales with the system size, to understand if MBL is robust to avalanches. We use the single-site Lindbladian bath considered in [66], applying it to the leftmost site, as in [5557] This choice of bath can be numerically studied with an approach of Hamiltonian dynamics with noise [66-68], allows scaling to large system sizes in the case of Anderson localized system, and can provide a lower bound to the slowest thermalization time. Furthermore, it allows scaling to large system sizes in the case of Anderson localized systems.

Weestimate the slowest thermalization time by looking at the propagation of the thermalization front through the chain, an approach that, to the best of our knowledge, has not yet been used in this context. Heat propagates through the system, from the bath at the leftmost site, and at any time there is a subchain on the left side that has already thermalized [see the cartoon in Fig. 1]. We estimate the length of this thermalized subchain by defining a thermalization length scale based on the behavior of the local magnetizations. We find that both in Anderson and MBL localized systems this length scale increases logarithmically in time - in agreement with the general analytical predictions of logarithmic light cones in MBL systems of [69, 70], the analytical prediction of their robustness under local perturbations of [71], and the logarithmic increase of a length scale related to the twotime density-density correlators in the Anderson case [66] undergoing single-site noise.

We use the logarithmic growth of the thermalization length scale to estimate the time in which the thermalization front reaches the other end of the chain. We find that this time scale exponentially increases with the system size, and there is a regime of parameters where this exponential increase is fast enough that localization is robust against thermalization induced by avalanches. We find that the slope of the logarithmic increase of the thermalization length scale is the same both with a particle-number-conserving or a particle-number nonconserving coupling to the bath, consistently with the logarithmic light cone being independent of this conservation [71]. We remark also that the results we find for the Anderson-localized model provide information relevant also for MBL, as the coupling to the bath makes the system interacting [52]. We also study the slowest thermalization time by looking at the thermalization behavior of the imbalance and obtain results in agreement.

FIG. 1. Graphical visualization of the model: a 1D chain of interacting 1/2 spins with a fixed disorder profile, starting from the N´ eel state, and with open boundary conditions. Different copies of the system mean different subsequent times, as indicated by the time arrow on the right. The leftmost spin is coupled to a T = ∞ thermal bath (a noisy time-dependent kick) and a thermalization front (shaded area) propagates logarithmically slowly.

<!-- image -->

The paper is organized as follows. In Sec. II we define our model, and in Sec. III we discuss the numerical methods we use in the case of many-body localization. In Sec. IV A we numerically show that the imbalance thermalization time is exponential both in the system size and in the disorder strength, and this allows us to show that there is a critical strength beyond which MBL is robust against the avalanche instability. In Sec. IVB we define a thermalization length scale using the local magnetizations and show that it logarithmically increases with time. This implies that the thermalization time of the imbalance exponentially increases with system size. In Sec. V we draw our conclusions and sketch perspectives of future work. In the Appendixes we discuss some important aspects that would have broken the main discussion. In particular, in Appendix A we review how the Hamiltonian quantum-trajectory approach works, in Appendix B we discuss how the Gaussian nature of the state in the case of the Anderson model simplifies the numerical analysis, in Appendix C we take a particle-number nonconserving bath and find that the logarithmic propagation occurs with the same slope, and in Appendix D we review the derivation of the threshold above which the scaling of the slowest thermalization time is slow enough to guarantee robustness against avalanches.

## II. MODEL

We consider the 1D spin-1/2 XXZ Heisenberg model in a random magnetic field

$$\hat { H } _ { 0 } = \sum _ { j = 1 } ^ { L } h _ { j } \hat { S } _ { j } ^ { z } + J \sum _ { j = 1 } ^ { L - 1 } ( \hat { S } _ { j } ^ { x } \hat { S } _ { j + 1 } ^ { x } + \hat { S } _ { j } ^ { y } \hat { S } _ { j + 1 } ^ { y } + \Delta \hat { S } _ { j } ^ { z } \hat { S } _ { j + 1 } ^ { z } ) , \quad \text {discrete} \quad \text {if} \quad \text {it, so} \\ = \sum _ { j = 1 } ^ { ( 1 ) } h _ { j } \hat { S } _ { j } + J \sum _ { j = 1 } ^ { ( 1 ) } \hat { S } _ { j + 1 } ^ { x } \hat { S } _ { j + 1 } ^ { x } + \hat { S } _ { j } ^ { y } \hat { S } _ { j + 1 } ^ { y } + \Delta \hat { S } _ { j } ^ { z } \hat { S } _ { j + 1 } ^ { z } ) , \quad \text {if} \quad \text {the} \quad \text {if} \quad \text {the} \quad \text {if} \quad \text {the} \quad \text {if} \quad \text {the} \quad \text {if} \quad \text {the} \quad \text {if} \quad \text {the} \quad \text {if} \quad \text {the} \quad \text {if} \quad \text {the} \quad \text {if} \quad \text {the} \quad \text {if} \quad \text {the} \quad \text {if} \quad \text {the} \quad \text {if} \quad \text {the} \quad \text {if} \quad \text {the} \quad \text {if} \quad \text {the} \quad \text {if} \quad \text {if} \quad \text {the} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text {if} \quad \text$$

where L is the system size, ˆ S α j ≡ ˆ σ α j / 2 are the on-site magnetizations ( α ∈ { x, y, z } ) and J = 1 sets the energy scale. The on-site magnetic fields h j are chosen randomly and uniformly in the interval [ -W,W ], and the system conserves the total magnetization S z tot = ∑ L j =1 ˆ S z j in the z direction. We consider open boundary conditions.

This model has been widely studied as a paradigmatic model displaying MBL behavior [23, 28, 63, 72-76]. It exhibits at finite sizes a crossover [57] from the ergodic to the localized regime, and it is believed to capture the essential properties of the MBL systems. At ∆ = 1 various estimates of this crossover point W c have been made, some of them including W c ≈ 3 . 5 [24], W c ≈ 3 . 7 [28], W c ≈ 5 [77], W c ≈ 5 . 4 [78], nevertheless it is impossible to univocally extrapolate finite-size results to the thermodynamic limit, and so the question is far from being settled [22, 44, 63-65, 79]. Furthermore, the Jordan-Wigner transformation [80] allows to map this model to a system of interacting spinless fermions with tunneling matrix element J and nearest-neighbor interaction strength ∆ (see Appendix B for details), connecting the model and the experiments on quasirandom optical lattices [16].

We couple one end of this system to a thermal bath that induces T = ∞ thermalization. This evolution is described by the Lindbladian

$$\dot { \hat { \rho } } ( t ) = - i [ \hat { H } _ { 0 } , \hat { \rho } ( t ) ] - \gamma ^ { 2 } [ \hat { S } _ { 1 } ^ { z } , [ \hat { S } _ { 1 } ^ { z } , \hat { \rho } ( t ) ] ] \, , \quad ( 2 )$$

where γ 2 is the coupling to the bath. This noise conserves the value of S z tot , corresponding to the particle number in the fermionic representation. (We relax this particlenumber-conserving property in Appendix C, finding essentially no difference for the slope of the logarithmic propagation discussed in Sec. IV B.) Restricting to any S z tot subspace, one can see that the identity is the only steady state of this Lindblad dynamics, implying the T = ∞ thermalization inside that subspace.

In order to study this Lindbladian, we use a quantum trajectory approach. More specifically we rely on the so-called unitary unraveling [66, 68] where the dynamics of Eq. (2) is described by an average over many realizations of unitary Schr¨ odinger evolutions with a noisy Hamiltonian. So one should evolve with the stochastic Hamiltonian

$$\hat { H } _ { \gamma } ( t ) = \hat { H } _ { 0 } + \gamma \xi ( t ) \hat { S } _ { 1 } ^ { z } \, , \quad \text { (3) } \quad \text {ind}$$

where ˆ H 0 is defined in Eq. (1) and ξ ( t ) is an uncorrelated Gaussian noise, for which ⟨ ξ ( t ) ⟩ = 0, ⟨ ξ ( t ) ξ ( t ′ ) ⟩ = δ ( t -t ′ )

and all the cumulants are vanishing. Angular brakets denote the average over noise realizations. This Hamiltonian for the Anderson ∆ = 0 case has already been considered in [66], where the entanglement entropy and the two-time density-density correlations are considered. In order to numerically implement this evolution, we must discretize it over time intervals τ ≪ 1 /J and Trotterize it, so that the n -th evolution step is given by the action of the operator

$$\hat { U } _ { n } = e ^ { - i \eta _ { n } \gamma \hat { S } _ { 1 } ^ { z } } e ^ { - i \tau \hat { H } _ { 0 } } \, ,$$

where η n are Gaussian random variables defined as η n = ∫ nτ ( n -1) τ ξ ( t ) dt , so that ⟨ η n ⟩ = 0 and ⟨ η n η n ′ ⟩ = τδ n,n ′ . In the following we fix τ = 0 . 05, as we have verified that a shorter τ does not affect the result. Averaging over random realizations, in the limit τ → 0 one recovers the Lindblad equation, Eq. (2), as we show in Appendix A. In the Anderson-model case ∆ = 0 the dynamics along each trajectory is given by Gaussian states, allowing thereby to numerically address large system sizes , as we discuss in detail in Appendix B.

## III. METHODS

For the dynamics, it is customary to evolve the system starting from the high energy, out-of-equilibrium, unentangled, antiferromagnetic N´ eel state | ψ ⟩ = |↑↓ . . . ↑↓⟩ , which has total magnetization S z tot = 0 and gives rise to a dynamics restricted to the corresponding S z tot subspace whose dimension is N = ( L L/ 2 ) . In order to detect the effect of the noise on the system, we compare two different evolutions, one with the Hamiltonian Eq. (1), without noise ( γ = 0)

$$| \psi _ { 0 } ( t ) \rangle = e ^ { - i \hat { H } _ { 0 } t } \left | \uparrow \downarrow \uparrow \downarrow \dots \rangle \ ,$$

and one with the fully noisy Hamiltonian ˆ H γ [Eq. (3)], fixing the same disorder realization

$$| \psi _ { \gamma } ( t ) \rangle = \prod _ { n = 1 } ^ { [ t / \tau ] } \hat { U } _ { n } \left | \uparrow \downarrow \uparrow \downarrow \dots \right \rangle \, ,$$

ending both evolutions at some final time t f . The state | ψ 0 ( t ) ⟩ is unaffected by noise and will be considered as a reference. We average each of the quantities over N r different disorder/noise realizations. When γ = 0 in each realization we take a different random choice of the onsite fields h j , for j ∈ { 1 , . . . , L } in Eq. (1). When γ = 1 we take in each realization a different choice of the h j and also a different choice of the random sequence η n , with n ∈ { 1 , . . . , [ t f /τ ] } providing the noise in Eq. (4). We indicate the average over the N r disorder/noise realizations with an overline ( . . . ). We evaluate the errorbar on this average as the root mean square deviation divided by √ N r , performing error propagation where appropriate.

In the case of the Anderson model we take N r = 1200 while in the case of MBL, in which the simulation times are longer, the number of realizations will be going from N r = 500 for the smallest system L = 8, to N r = 100 for the biggest one L = 16. When we compare γ = 1 and γ = 0 we average over the same set of disorder realization. To simulate the time evolution we use exact diagonalization and Krylov subspace projection methods [81]. Exact diagonalization is much more efficient in the case of the Anderson model (∆ = 0) thanks to the mapping of each trajectory to a free fermion model (see Appendix B). In the following text, whenever we consider an interacting case, we fix ∆ = 1, and when we consider coupling to the thermal bath we take γ = 1.

## IV. IMBALANCE AND LOCAL MAGNETIZATIONS

## A. Imbalance behavior and robustness against avalanche instability

The imbalance I between the even and odd sites in the spin representation is defined as

$$\mathcal { I } ( t ) = \frac { 1 } { L } \sum _ { j = 1 } ^ { L } ( - 1 ) ^ { j } \langle \psi ( t ) | \hat { S } _ { j } ^ { z } | \psi ( t ) \rangle . \quad ( 7 ) \quad \text {that}$$

It is a global feature of the system which can be computed from local quantities, and can be experimentally measured [16, 82]. The normalization ensures I ( t = 0) = 1. The long-time stationary value of the imbalance effectively serves as an order parameter of the MBL phase, which is why it has been widely used in the literature [72, 77, 83]. For small W , in the ergodic regime, a power-law decay I ( t ) ∝ t -β has been observed. For larger W , in the finite-size localized regime, one numerically sees convergence to a non-vanishing value at long times, although the problem is particularly challenging [72].

̸

The goal of our analysis is to understand how the imbalance with the noise I γ =1 ( t ) differs from the noiseless case, I γ =0 ( t ), varying the size of the system L and the strength of the disorder W . We show some examples of I γ ( t ) versus t in Fig. 2, for L = 16 and two different values of W [ W = 2 in panel (a) and W = 8 in panel (b)]. We see that when the coupling to the bath γ = 0, I γ ( t ) deviates from I 0 ( t ), starting at a time t ∼ 1, and eventually decaying to zero.

In order to perform a size scaling we define a relative imbalance I r as

$$\mathcal { I } _ { r } ( t ) = \frac { \bar { I } _ { 0 } ( t ) - \bar { I } _ { \gamma } ( t ) } { \bar { I } _ { 0 } ( t ) } \, . \quad \quad ( 8 ) \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \$$

This quantity increases from the initial value I r ( t = 0) = 0 [due to I 0 ( t = 0) = I γ ( t = 0)] to the asymptotic value I r ( t → ∞ ) = 1 [due to I γ ( t → ∞ ) = 0], as we show in Fig. 2. We can study the time scale over which this happens and we do that computing the minimum time ˜ t it takes for the relative imbalance I r to grow above a fixed threshold, within the statistical error. Given the computational limitations, we fixed the common threshold to be r th = 0 . 17. [84]

FIG. 2. Interacting case. Time evolution of the imbalance in the noiseless case I 0 , in the noisy case I 1 and relative difference I r for L = 16, for W = 2 in panel (a) and W = 8 in panel (b), and N r = 100.

<!-- image -->

We show results in Fig. 3. From one side we see that ˜ t displays a behavior consistent with an exponential increase with the disorder strength W , as the fits in Fig. 3(a) show. This is in agreement with the exponential dependence of the thermalization time on the disorder strength, seen when one end of an MBL chain is time-periodically coupled to an ergodic one [54]. From the other side, we find that ˜ t also exponentially increases with the size L of the system, as we show in Fig. 3(b).

So we conclude that, at least for the parameters considered in Fig. 3, there is some α &gt; 0 such that the thermalization time of the imbalance has the behavior

$$\tilde { t } \sim \exp ( \alpha L W ) \, .$$

We use the argument of Ref. [57], according to which MBL is robust if the slowest thermalization time t s grows faster than 4 L (see Appendix D for more details). Imposing t ∗ &gt; 4 L and considering that ˜ t is a lower bound to the slowest thermalization time t s - as by definition t s &gt; ˜ t - we find that there is a minimum value of disorder

$$\widetilde { W } = \frac { 2 \ln 2 } { \alpha }$$

such that for W &gt; ˜ W MBL is robust against avalanche instability. We underline that MBL could still be robust even for W &lt; ˜ W , because t s might still grow faster than 4 L . If the scaling behavior observed in Fig. 3 holds over a sufficiently wide range of parameters, there exists a disorder strength beyond which MBL remains robust.

To estimate the coefficient α in Eq. (9), we plot ln ˜ t as a function of the product LW , displaying all the points of Fig. 3 on one single curve shown in Fig. 4, and apply a linear fit such that ln( ˜ t ) = αLW + β . From the fit we obtain α = 0 . 036 ± 0 . 001; Substituting this result in Eq. (10) we find a threshold value ˜ W ≃ 38 . 5. This is larger than the estimate obtained below with the heat propagation (see Sec. IV B), but it is not a problem. Indeed, ˜ t is only a lower bound to the slowest thermalization time. We know for sure that for W &gt; ˜ W the slowest thermalization time scales slowly enough that MBL is robust to avalanches; Below this threshold it could be robust or not. Nevertheless this analysis provides the important information that for W &gt; ˜ W MBL is a robust phase.

FIG. 3. Interacting case. (Panel a) ˜ t versus W for different values of L . (Panel b) ˜ t as a function of L for different values of W . The error bars are the maximum error, N r goes from 500 for L = 8 to 100 for L = 16.

<!-- image -->

FIG. 4. ln( ˜ t ) as a function of the product LW , and the linear fit providing the slope α .

<!-- image -->

To gain a deeper understanding of the imbalance behavior, we focus now on the properties of the local magnetizations.

## B. Thermalization front and local magnetizations

## 1. Logarithmic propagation of the thermalization front

Let us consider the local magnetizations ( S z j ) γ ( t ) = ⟨ ψ t | ˆ S z j | ψ t ⟩ for the evolution with a given γ . To see how thermalization propagates through the chain, let us set

$$\delta S _ { j } ( t ) = \left | \overline { ( S _ { j } ^ { z } ) } _ { \gamma = 0 } ( t ) - \overline { ( S _ { j } ^ { z } ) } _ { \gamma = 1 } ( t ) \right | \, , \quad ( 1 1 )$$

and define a thermalization length scale as

$$h ( t ) = \frac { \sum _ { j = 1 } ^ { L } ( j - 1 ) \delta S _ { j } ( t ) } { \sum _ { j = 1 } ^ { L } \delta S _ { j } ( t ) } \, ,$$

and study its behavior as a function of time. We plot h ( t ) versus t for the Anderson-model case in Fig. 5(a) and in the interacting case in Fig. 5(b). In the Anderson-model case, whatever the disorder strength W , we see that h ( t ) logarithmically increases with time for t large enough, as h ( t ) ∼ A ln( t ). In the interacting case we see the same logarithmic increase for disorder strengths W &gt; 2. We have checked that the result is converged in system size and does not depend on L for the time interval we have numerically access to. For W = 2 we see a faster growth and a saturation due to finite-size effects.) We obtain the slope A with a linear fit of h ( t ) versus ln t , applying the fit for times such that the linear regime in ln t has already set in. We plot the 1 /A resulting from this fit as a function of W in the insets of Fig. 5. In the Andersonmodel case we see that 1 /A irregularly increases with W , while in the interacting case the increase is more regular, slightly faster than linear.

## 2. Relation with the behavior of the imbalance

So we have found that the thermalization front propagates logarithmically. This gives rise to some interesting predictions on the behavior of I r ( t ). Because at time t only a fraction f ( t ) ∼ A ln( t ) /L of the chain has thermalized, we can predict a behavior

$$\mathcal { I } _ { r } ( t ) \sim A \ln ( t ) / L \, .$$

We have obtained this estimate as follows. Due to extensivity, let us write the long-time value of the noiseless imbalance I 0 ( t ) = qL for some q ∈ (0 , 1) and t ≫ 1 /J . If only a fraction of f ( t ) sites has thermalized, we can roughly approximate I γ ( t ) ∼ Lq [1 -f ( t )], and so we apply Eq. (8) and get Eq. (13), valid for t ≫ 1 /J .

We have numerically checked that this prediction is obeyed for large L in the Anderson case as we show in Fig. 6(a), and for smaller system sizes in the interacting case as we show in Fig. 6(b). In both panels we fix W and plot L I r ( t ) versus t for different values of L , with a logarithmic scale on the horizontal axis. We see that the rescaled curves tend to a limit curve, meaning that the scaling with 1 /L holds for large system sizes. Furthermore, the limit curve increases linearly with time in logarithmic scale, consistently with Eq. (13). This finding implies an exponential scaling with the system size of the thermalization time of the imbalance, as the one shown in Fig. 3(b).

FIG. 5. (Main panels) h ( t ) versus t in the Anderson (∆ = 0) case in panel (a) and interacting case (∆ = 1) in panel (b). Notice the logarithmic scale on the horizontal axis. (Insets) 1 /A versus W , where A is the slope obtained linearly fitting h ( t ) versus ln t , applying the fit for times large enough that the linear in ln t regime has already set in. The blue lines in the main panel (b) mark the linear fits, and in the inset in panel (b) there is the reference value 1 /A = 4ln2, as defined in Eq. (19). Numerical parameters in (a): L = 100 , N r = 1200. Numerical parameters in (b): L = 16, N r = 100.

<!-- image -->

As we can see in the inset of Fig. 5(b), the behavior of 1 /A is consistent with a linear increase in W , so we can write 1 /A ∼ βW for some β &gt; 0. Substituting 1 /A = βW in Eq. (13) and imposing I r ( ˜ t ) = r th (= 0 . 17) we get

$$\stackrel { \stackrel { \stackrel { \dots } { t } } { t } \sim \exp \left ( r _ { t h } \beta L W \right ) } { \sim } ,$$

consistent with Eq. (9).

FIG. 6. L I r ( t ) versus t for and W = 8 in the Anderson (∆ = 0) case in panel (a) and in the interacting case in panel (b). Notice the logarithmic scale on the horizontal axis.

<!-- image -->

## 3. Slowest thermalization time and robustness to avalanches

Let us see what the results above imply for robustness of localization against avalanches. In Sec. IV we have derived the threshold value in Eq. (10), which implies the robustness of MBL for W large enough. Let us now assume to average over infinite disorder/randomness realization and observe that Eq. (11) implies

$$\delta S _ { j } ( \infty ) = \lim _ { t \to \infty } \delta S _ { j } ( t ) = \lim _ { t \to \infty } \left | \overline { ( S _ { j } ^ { z } ) } _ { \gamma = 0 } ( t ) \right | \, ,$$

because lim t →∞ ( S z j ) γ =1 ( t ) = 0 ∀ j = 1 , . . . , L due to thermalization. In periodic boundary conditions (PBC), due to the symmetries of the problem averaged over disorder, both ∣ ∣ ∣ ( S z j ) γ =0 ( t ) ∣ ∣ ∣ and δS j ( ∞ ) are independent of j , (let us write δS j ( ∞ ) ≡ δS ), so that

$$= 0 ) \quad \lim _ { \substack { t \to \infty \\ t t t i n g } } h ( t ) = \frac { \delta S \sum _ { j = 1 } ^ { L } ( j - 1 ) } { \delta S \sum _ { j = 1 } ^ { L } 1 } = \frac { L - 1 } { 2 } \quad \text {for PBC. } ( 1 6 ) \\$$

The open boundary conditions affect the behavior of the ∣ ∣ ∣ ( S z j ) γ =0 ( t ) ∣ ∣ ∣ , and then of the δS j ( ∞ ), for a finite length l b near the boundaries. This length l b is finite and does not scale with L because we assume the system with γ = 0 to be localized (Anderson or MBL). So we can write in our case

$$\lim _ { t \to \infty } h ( t ) = \frac { L - 1 } { 2 } + \mathcal { O } ( l _ { b } ) \quad \text {for $\O B C$.} \quad ( 1 7 )$$

We can say that all local magnetizations have thermalized, at time t ∗ , when h ( t ∗ ) = lim t →∞ h ( t ). Using that for t ≫ 1 /J the length scale h ( t ) ∼ A ln( t ), we get with some simple algebra the thermalization time t ∗ as

$$t ^ { * } \sim \exp \left ( \frac { L } { 2 A } \right ) \, ,$$

with some multiplicative constants in front that are irrelevant for the scaling with L . In order to have robustness against avalanches, we must have a scaling faster than 4 L . We meet this condition if exp ( 1 2 A ) &gt; 4 or

$$\frac { 1 } { A } > 2 \ln 4 \, . & & ( 1 9 ) & & \stackrel { \text {ar} } { h } \\$$

In the inset of Fig. 5(a), we observe that the Anderson model consistently satisfies this requirement within the parameter range we investigate. The Anderson model is inherently integrable and unable to generate ergodic inclusions. However, if an ergodic inclusion is introduced into the model, it remains resistant to thermalization induced by avalanches within this parameter range.

In contrast, the MBL model satisfies Eq. (19) provided that W exceeds a threshold value W ∗ ≳ 7, as shown in the inset of Fig. 5(b). For W &gt; W ∗ , MBL remains robust. For W &lt; W ∗ , we cannot make definitive claims about stability because t ∗ in Eq. (18) only offers a lower bound on the slowest thermalization time t s .

## V. CONCLUSION AND PERSPECTIVES

In conclusion we have studied a many-body or Anderson localized model coupled to a T = ∞ thermal bath by one end. The coupling is described by a Lindbladian, and to numerically study it we have used a quantumtrajectory approach. More specifically, we have used a unitary unraveling such that the dynamics is an average over many realizations of a unitary Schr¨ odinger evolution with noise. In the case of Anderson localization this approach allows to reach quite large system sizes, due to the Gaussian form of the state along each quantum trajectory.

We have first numerically studied the dynamics of the imbalance, a global quantity widely used to assess the presence of localization. We have defined its thermalization time as the time beyond which the normalized difference of the imbalance with and without thermal bath goes beyond a given threshold, and we see that in the MBL case this thermalization time exponentially increases with the strength of the disorder and the size of the system. We have shown that this result implies that the MBL is robust against the avalanche instability when the disorder strength goes beyond a given threshold.

We have then focused on the heat propagation through the system considering how a thermalization front propagated. We have estimated the extension of the already thermalized part of the chain, defining a thermalization length scale using the onsite magnetizations, and found that it logarithmically increases with time, in agreement with the existing analytical estimates [71]. This is true both for the Anderson and the MBL case and we could use it to lower bound the slowest thermalization time with a quantity exponentially scaling with the system size. We have found that in the strong-disorder regime this scaling is fast enough that the system is robust to avalanches.

As a perspective for future work, we can focus our attention on the density-density correlator [85], a quantity whose logarithmically slow propagation properties are known in the noisy Anderson case [66, 67], and see how this behavior is changed in the MBL case. Second, we can perform a similar analysis on the OTOC (that for MBL systems has been considered in [86]) to see how the thermalization front affects the scrambling properties of the system. Finally, we can study more deeply the relation between the strength of localization of the integrals of motion, the logarithmic thermalization front, the scaling of the slowest thermalization time, and the robustness of MBL to avalanches, also in MBL models with long-range interactions [87-89], where the behavior of the thermalization length scale has not yet been explored, to the best of our knowledge.

## ACKNOWLEDGMENTS

We acknowledge useful discussions with D. Singh Bhakuni and useful comments on the manuscript by D. Huse, N. Laflorencie, D. Luitz and D. Toniolo. M. C., G.P., P. L. and A. R. acknowledge financial support from PNRR MUR Project PE0000023- NQSTI and computational resources from MUR, PON 'Ricerca e Innovazione 2014-2020', under Grant No. PIR01 00011 - (I.Bi.S.Co.). G.P. acknowledges computational resources from the CINECA award under the ISCRA initiative. This work was furthermore supported by the European Union's Horizon 2020 research and innovation programme under Grant Agreement No 101017733, by the MUR project CN 00000013-ICSC (P. L.), and by the QuantERA II Programme STAQS project that has received funding from the European Union's Horizon 2020 research and innovation program.

## Appendix A: Derivation of the Lindblad equation form the quantum-trajectory scheme

Let us start with the Schr¨ odinger equation with the Hamiltonian Eq. (3)

$$i \frac { d } { d t } \left | \psi ( t ) \right \rangle = \left [ \hat { H } _ { 0 } + \gamma \xi ( t ) \hat { S } _ { 1 } ^ { z } \right ] \left | \psi ( t ) \right \rangle \, . \quad ( A 1 )$$

We can write it as

$$\begin{array} { r l } & { \text {top} ^ { - } } & { | \psi ( t + \Delta t ) \rangle \left \langle \psi ( t + \Delta t ) | = | \psi ( t ) \rangle \left \langle \psi ( t ) | } \\ & { i d y } & { - i \Delta t [ \hat { H } _ { 0 } , | \psi ( t ) \rangle \left \langle \psi ( t ) | ] - i \Delta W _ { t } \gamma [ \hat { S } _ { 1 } ^ { z } , | \psi ( t ) \rangle \left \langle \psi ( t ) | ] \, , } \\ & { \text {und} } \end{array}$$

where ⟨ ∆ W t ⟩ = ∆ t and ⟨ ∆ W t ∆ W t ′ ⟩ = δ t, t ′ ∆ t are Gaussian uncorrelated variables. Let us also write

$$\begin{array} { r l } { u } & { | \psi ( t ) \rangle \langle \psi ( t ) | = | \psi ( t - \Delta t ) \rangle \langle \psi ( t - \Delta t ) | } \\ { v } & { \quad - i \Delta t [ \hat { H } _ { 0 } , | \psi ( t - \Delta t ) \rangle \langle \psi ( t - \Delta t ) | ] \quad ( A 3 ) } \\ { e } & { - i \Delta W _ { t } \gamma [ \hat { \sigma } _ { 1 } ^ { z } , | \psi ( t - \Delta t ) \rangle \langle \psi ( t - \Delta t ) | ] \, , } \end{array}$$

and substitute it in the last term of Eq. (A2). We get many terms. Averaging over randomness and defining ˆ ρ t = 〈 ϱ ( t ) 〉 with ϱ ( t ) ≡ | ψ ( t ) ⟩ ⟨ ψ ( t ) | , we get

$$\hat { \rho } _ { t + \Delta t } & = \hat { \rho } _ { t } - i \Delta t [ \hat { H } _ { 0 } , \hat { \rho } _ { t } ] & & \text {spin, } & & \text {spin, } \\ & - ( \overline { \Delta W _ { t } \Delta W _ { t } } ) \gamma ^ { 2 } [ \hat { S } _ { 1 } ^ { z } , [ \hat { S } _ { 1 } ^ { z } , \hat { \rho } _ { t - \Delta t } ] ] + o ( \Delta t ) \cdot \left ( A 4 \right ) & & \text {not ch} \\$$

Using ⟨ ∆ W t ∆ W t ⟩ = ∆ t and going in the limit ∆ t → 0 we get

$$\frac { d } { d t } \hat { \rho } _ { t } = - i [ \hat { H } _ { 0 } , \hat { \rho } _ { t } ] - \gamma ^ { 2 } [ \hat { S } _ { 1 } ^ { z } , [ \hat { S } _ { 1 } ^ { z } , \hat { \rho } _ { t } ] ] \, . \quad ( A 5 )$$

## Appendix B: Case of the Anderson model

Applying the Jordan-Wigner transformation, the model in Eq. (1) becomes the spinless-fermion model

$$\hat { H } _ { 0 } = \sum _ { j = 1 } ^ { L } h _ { j } \hat { n } _ { j } + J \sum _ { j = 1 } ^ { L - 1 } \left [ \frac { 1 } { 2 } ( \hat { c } _ { j } ^ { \dagger } \hat { c } _ { j + 1 } + H . c . ) + \Delta \hat { n } _ { j } \hat { n } _ { j + 1 } \right ] \\ \\ \hat { H } _ { 0 } = \sum _ { j = 1 } ^ { L } h _ { j } \hat { n } _ { j } + J \sum _ { j = 1 } ^ { L - 1 } \left [ \frac { 1 } { 2 } ( \hat { c } _ { j } ^ { \dagger } \hat { c } _ { j + 1 } + H . c . ) + \Delta \hat { n } _ { j } \hat { n } _ { j + 1 } \right ] \\ \\ \hat { H } _ { 0 } = \hat { \left ( } t \right ) _ { 0 } \hat { H } _ { 0 } = \hat { \cdot } \cdot \hat { H } _ { 0 } \cdot \hat { H } _ { 0 } \\$$

where ˆ c ( † ) j are anticommuting fermionic operators acting on the j -th site. The number of fermions N ≡ ∑ L j =1 ˆ n j is conserved. In the Anderson-model case we have ∆ = 0 and we get a quadratic fermionic Hamiltonian, so that the time evolved state | ψ ( t ) ⟩ along each trajectory can be cast in the form of a generic Gaussian state (Slater determinant). The full information of such state is contained in a L × N matrix W ( t ), defined by

$$| \psi ( t ) \rangle = \prod _ { k = 1 } ^ { N } \left [ \sum _ { j = 1 } ^ { L } \left [ W ( t ) \right ] _ { j , k } \hat { c } _ { j } ^ { \dagger } \right ] | \Omega \rangle \ , \quad ( B 2 )$$

where | Ω ⟩ is the vacuum of the fermionic operators ˆ c j . Because the number of fermions is conserved and we initialize with the N´ eel state we have N = L/ 2. At initial time, the matrix L × N matrix defining the N´ eel state is given by [ W (0)] k,l = ∑ L/ 2 j =1 δ 2 j,l δ j,k . The discrete evolution step (see Eq. (4))

$$| \psi ( t + \tau ) \rangle = e ^ { - i \eta _ { n } \gamma \hat { S } _ { 1 } ^ { z } } e ^ { - i \tau \hat { H } _ { 0 } } \left | \psi ( t ) \right \rangle$$

is simply translated in the dynamics of the matrix W ( t ) as

$$W ( t + \tau ) = K _ { n } e ^ { - i \tau Q } W ( t ) \, ,$$

where the noisy step is implemented through the L × L diagonal matrix K n with matrix element [ K n ] i,j = δ i,j + δ 1 ,i δ 1 ,j ( e -iη n γ -1), while the L × L matrix Q implementing the action of the Anderson Hamiltonian has matrix elements [ Q ] i,j = δ i,j h j + J 2 ( δ i,j +1 + δ i,j -1 ). Thanks to the validity of Wick's theorem, one can use the matrix W ( t ) to obtain the expectation of any observable, and even the entanglement entropy, as clarified in [68]. In this way one can numerically reach quite large system sizes, up to L ∼ O (10 2 ).

## Appendix C: Particle-number non-conserving case

The coupling to the bath of Eq. (2) conserves the total spin, which is the particle number in the fermionic representation of Eq. (B1). Breaking this conservation does not change very much, due to the propagation of heat being constrained by a logarithmic light cone [71]. In order to check this, let us focus on the Anderson model (∆ = 0), and apply to it a different particle-number nonconserving boundary noise

$$\hat { H } _ { \gamma } ( t ) & = \hat { H } _ { 0 } + \gamma \xi _ { 1 } ( t ) \hat { S } _ { 1 } ^ { z } + \gamma _ { 1 } \xi _ { 2 } ( t ) \left ( \hat { S } _ { 1 } ^ { + } \hat { S } _ { 2 } ^ { + } + \hat { S } _ { 1 } ^ { - } \hat { S } _ { 2 } ^ { - } \right ) \, , \\ \\ \intertext { A 5 ) } \hat { H } _ { \gamma } ( t ) & = \hat { H } _ { 0 } + \gamma \xi _ { 1 } ( t ) \hat { S } _ { 1 } ^ { z } + \gamma _ { 1 } \xi _ { 2 } ( t ) \left ( \hat { S } _ { 1 } ^ { + } \hat { S } _ { 2 } ^ { + } + \hat { S } _ { 1 } ^ { - } \hat { S } _ { 2 } ^ { - } \right ) \, , \\$$

where ξ 1 ( t ) and ξ 2 ( t ) are uncorrelated Gaussian random processes ⟨ ξ j ( t ) ξ l ( t ′ ) ⟩ = δ j l δ ( t -t ′ ). Averaging over the noise, one gets the Lindblad equation

$$\begin{array} { r l } & { \det } & { \dot { \hat { \rho } } ( t ) = - i [ \hat { H } _ { 0 } , \hat { \rho } ( t ) ] - \gamma ^ { 2 } [ \hat { S } _ { 1 } ^ { z } , [ \hat { S } _ { 1 } ^ { z } , \hat { \rho } ( t ) ] ] } \\ & { i _ { j + 1 } \right ] & { - \gamma _ { 1 } ^ { 2 } \left [ \left ( \hat { S } _ { 1 } ^ { + } \hat { S } _ { 2 } ^ { + } + \hat { S } _ { 1 } ^ { - } \hat { S } _ { 2 } ^ { - } \right ) , \left [ \left ( \hat { S } _ { 1 } ^ { + } \hat { S } _ { 2 } ^ { + } + \hat { S } _ { 1 } ^ { - } \hat { S } _ { 2 } ^ { - } \right ) , \hat { \rho } ( t ) \right ] \right ] , } \\ & { ( C 2 ) } \end{array}$$

The dynamics in Eq. (C1) can be numerically studied by applying the Jordan-Wigner transformation and using the Bogoliubov-de Gennes formalism [90]. If we discretize the time with a step τ , Trotterize, and apply the Jordan-Wigner transformation we get the discrete timestep evolution operator

$$\hat { U } _ { n } = e ^ { - i \gamma \eta _ { n } ^ { ( 1 ) } \hat { n } _ { 1 } ^ { z } } e ^ { - i \gamma _ { 1 } \eta _ { n } ^ { ( 2 ) } \left ( \hat { c } _ { 1 } ^ { \dagger } \hat { c } _ { 1 } ^ { \dagger } \hat { c } _ { 2 } \right ) } e ^ { - i \tau \hat { H } _ { 0 } } \, , \quad ( C 3 )$$

with

$$\hat { H } _ { 0 } = \sum _ { j = 1 } ^ { L } h _ { j } \hat { n } _ { j } + \frac { J } { 2 } \sum _ { j = 1 } ^ { L - 1 } ( \hat { c } _ { j } ^ { \dagger } \hat { c } _ { j + 1 } + H . c . ) \, , \quad ( C 4 )$$

and η (1) n , η (2) n are uncorrelated zero-mean Gaussian random variables such that ⟨ η ( j ) n η ( k ) n ′ ⟩ = δ j k δ nn ′ τ . Using the Bogoliubov formalism we introduce the fermionic operators ˆ γ α ( t ) = ∑ L j =1 ( U ∗ j α ( t )ˆ c j + V ∗ j α ( t )ˆ c † j ) such that ˆ γ α ( t ) | ψ ( t ) ⟩ = 0, and the coefficients U j α ( t ), V j α ( t ) form a 2 L × L matrix that obeys the relation

$$a \ 2 L \times L \, \text { matrix that obeys the relation} \\ 3 ) \quad & \left ( \begin{array} { c } U ( t + \tau ) \\ V ( t + \tau ) \end{array} \right ) = \exp \left [ - i \gamma \eta _ { n } ^ { ( 1 ) } \left ( \begin{array} { c c } A & 0 \\ 0 & - A \end{array} \right ) \right ] \\ & \exp \left [ - i \gamma _ { 1 } \eta _ { n } ^ { ( 2 ) } \left ( \begin{array} { c c } 0 & B \\ - B & 0 \end{array} \right ) \right ] \\ & \exp \left [ - i \tau \left ( \begin{array} { c c } Q & 0 \\ 0 & - Q \end{array} \right ) \right ] \left ( \begin{array} { c } U ( t ) \\ V ( t ) \end{array} \right ) \, , \\ + \quad & \text {where the } L \times L \, \text { matrices } A , B , B \text { and } Q \text { have matrix}$$

where the L × L matrices A , B , and Q have matrix elements

$$[ A ] _ { j l } & = \delta _ { j 1 } \delta _ { l 1 } \\ [ B ] _ { j l } & = \delta _ { j 1 } \delta _ { l 2 } \\ [ Q ] _ { j l } & = h _ { j } \delta _ { j l } + \frac { J } { 2 } ( \delta _ { j \, l + 1 } + \delta _ { j \, l - 1 } ) \, . \quad ( C 6 )$$

FIG. 7. (Panels a, b) Examples of comparison of h ( t ) versus t with the particle-number conserving ( γ 1 = 0) and nonconserving ( γ 1 = 1) noises for different values of W in the Anderson-model case (∆ = 0). Other numerical parameters: γ = 1 , L = 10 , N r = 1200. (Panel c, d) Examples of comparison of h ( t ) versus t with the particle-number conserving noise Eq. (4) and nonconserving noise Eq. (C9) for different values of W and ∆ = 1. Other numerical parameters: γ = 1 , L = 8 , N r = 576.

<!-- image -->

The on-site magnetizations at time t are given by

$$\langle \hat { S } _ { j } ^ { z } \rangle _ { t } = \sum _ { \alpha } | V _ { j \alpha } ( t ) | ^ { 2 } - 1 / 2 \, . \quad ( C 7 ) \quad \stackrel { i z e } { \underset { s i z e } { \text {size} } }$$

We compare for some values of W the evolution of h ( t ) under particle-number conserving noise ( γ 1 = 0) and the one under particle-number nonconserving noise ( γ 1 = 1). Putting the logarithmic scale on the horizontal axis, we see that in each cases the two curves tend to straight lines with the same slope [see Fig. 7(a,b)]. Therefore, the value of the slope A (needed for estimating t ∗ ) is the same with and without particle-number conservation. The physical reason is that the propagation is bounded by the same logarithmic light cone with and without particle conservation [71].

We can do a similar analysis for the interacting case with ∆ = 1. In this case we apply the following particlenumber nonconserving boundary noise

$$\hat { H } _ { \gamma } ( t ) = \hat { H } _ { 0 } + \gamma \xi _ { z } ( t ) \hat { S } _ { 1 } ^ { z } + \gamma \xi _ { x } ( t ) \hat { S } _ { 1 } ^ { x } \, . \quad ( C 8 ) \quad \text {ics} \, ( 2 )$$

So we must compare the dynamics induced by the oper- ator Eq. (4) with the one induced by

FIG. 8. Scheme of an MBL chain for the analysis of robustness of MBL to avalanches. The red region is the ergodic inclusion, the yellow region the thermalized part of the chain, the blue region the part of the chain not yet thermalized. We focus on a subset of the latter (dark blue) that is in contact with the thermalized region and is made by two sectors, each of length ∆ r .

<!-- image -->

$$\hat { U } _ { n } ^ { \prime } = e ^ { - i \eta _ { n } ^ { x } \gamma \hat { S } _ { 1 } ^ { x } } e ^ { - i \eta _ { n } ^ { z } \gamma \hat { S } _ { 1 } ^ { z } } e ^ { - i \tau \hat { H } _ { 0 } } \, ,$$

where η z n and η x n are Gaussian zero-average random variables such that ⟨ η α n η β m ⟩ = τδ αβ δ mn . We show some examples of comparison of h ( t ) obtained with the two types of noise, for corresponding parameters of ˆ H 0 , in Fig. 7(c,d). We see that after a transient the two types of noise provide the same curve.

## Appendix D: Scaling of the slowest thermalization time and robustness of localization against avalanches

In this section we explain why, in order for localization to be robust against avalanches, the slowest thermalization time should scale faster than 4 L when one end of the system is coupled to a thermal bath. The thing has already been clearly explained in [55, 57], and we add this section just for completeness. Let us consider Fig. 8 depicting an MBL chain. We have an ergodic inclusion of size r 0 (red region), and a part that has already thermalize (yellow region) made by two sectors, with the same size r (we assume the avalanches to act symmetrically). The rest of the system is already localized (blue region) and we want to see if thermalization can further propagate there by avalanches. With this aim, we focus on a part of the localized region in contact with the ergodic region, made by two sectors of length ∆ r (dark blue region). We ask ourselves if this region thermalizes due to the contact with the yellow region, that's to say if the avalanche propagates. This can happen if each sector in the dark-blue region (let's say the right one they are equal) thermalizes fast enough. So the slowest thermalization time t s of each dark-blue sector must be much shorter than the inverse gap 1 /δ of the region obtained joining the red, the yellow and the dark blue regions. The point is that thermalization in each darkblue sector must be faster than the time needed to the part of the chain involved in the thermalizing dynamics (red+yellow+dark-blue) to express finite-size revivals and other quantum dynamical effects connected with the discreteness of the spectrum that hinder thermalization.

On general grounds [55, 57] (and we numerically verify it also in our work) one has t s ∼ κ ∆ r for some κ &gt; 0. Being this a spin 1/2 system one has δ = 2 -( r 0 +2 r +2∆ r ) . Imposing t s ≪ 1 /δ , and asking that this condition should be verified also in the limit of ∆ r ≫ r , one finds

$$\kappa < 4 .$$

By contrast, if κ &gt; 4 MBL is robust to avalanches. So it is very important to know κ . In order to find it, we

- [1] J. M. Deutsch, Quantum statistical mechanics in a closed system, Phys. Rev. A 43 , 2046 (1991).
- [2] M. Srednicki, Chaos and quantum thermalization, Phys. Rev. E 50 , 888 (1994).
- [3] T. c. v. Prosen, Ergodic properties of a generic nonintegrable quantum many-body system in the thermodynamic limit, Phys. Rev. E 60 , 3949 (1999).
- [4] A. Polkovnikov, K. Sengupta, A. Silva, and M. Vengalattore, Colloquium: Nonequilibrium dynamics of closed interacting quantum systems, Rev. Mod. Phys. 83 , 863 (2011).
- [5] A. P. Luca D'Alessio, Yariv Kafri and M. Rigol, From quantum chaos and eigenstate thermalization to statistical mechanics and thermodynamics, Advances in Physics 65 , 239 (2016).
- [6] M. Rigol, V. Dunjko, and M. Olshanii, Thermalization and its mechanism for generic isolated quantum systems, Nature 452 , 854 (2008).
- [7] P. Reimann, Typical fast thermalization processes in closed many-body systems, Nature Communications 7 , 10.1038/ncomms10821 (2016).
- [8] M. Serbyn, M. Knap, S. Gopalakrishnan, Z. Papi´ c, N. Y. Yao, C. R. Laumann, D. A. Abanin, M. D. Lukin, and E. A. Demler, Interferometric probes of many-body localization, Phys. Rev. Lett. 113 , 147204 (2014).
- [9] P. W. Anderson, Absence of diffusion in certain random lattices, Phys. Rev. 109 , 1492 (1958).
- [10] L. Fleishman and P. W. Anderson, Interactions and the anderson transition, Phys. Rev. B 21 , 2366 (1980).
- [11] D. Basko, I. Aleiner, and B. Altshuler, Metal-insulator transition in a weakly interacting many-electron system with localized single-particle states, Annals of Physics 321 , 1126 (2006).
- [12] I. V. Gornyi, A. D. Mirlin, and D. G. Polyakov, Interacting electrons in disordered wires: Anderson localization and lowt transport, Phys. Rev. Lett. 95 , 206603 (2005).
- [13] R. Vosk and E. Altman, Many-body localization in one dimension as a dynamical renormalization group fixed point, Phys. Rev. Lett. 110 , 067204 (2013).
- [14] R. Vosk, D. A. Huse, and E. Altman, Theory of the manybody localization transition in one-dimensional systems, Phys. Rev. X 5 , 031032 (2015).
- [15] J. Z. Imbrie, On many-body localization for quantum spin chains, Journal of Statistical Physics 163 , 998 (2016).
- [16] M. Schreiber, S. S. Hodgman, P. Bordia, H. P. L¨ uschen, M. H. Fischer, R. Vosk, E. Altman, U. Schneider, and I. Bloch, Observation of many-body localization of interacting fermions in a quasirandom optical lattice, Science

have done as biologists do when move a portion of neural tissue from in vivo to in vitro [55, 57]: We have cut away the right blue region from the system in Fig. 8, we have connected its left site to a thermal bath simulating the yellow thermalized region in Fig. 8, and we have studied the scaling of the slowest thermalization time with ∆ r . We have renamed ∆ r as L for merely aesthetic reasons.

[349 , 842 (2015).](https://doi.org/10.1126/science.aaa7432)

- [17] J. yoon Choi, S. Hild, J. Zeiher, P. Schauß, A. RubioAbadal, T. Yefsah, V. Khemani, D. A. Huse, I. Bloch, and C. Gross, Exploring the many-body localization transition in two dimensions, Science 352 , 1547 (2016), https://www.science.org/doi/pdf/10.1126/science.aaf8834.
- [18] J. Smith, A. Lee, P. Richerme, B. Neyenhuis, P. W. Hess, P. Hauke, M. Heyl, D. A. Huse, and C. Monroe, Many-body localization in a quantum simulator with programmable random disorder, Nature Physics 12 , 907 (2016).
- [19] P. Bordia, H. L¨ uschen, U. Schneider, M. Knap, and I. Bloch, Periodically driving a many-body localized quantum system, Nature Physics 13 , 460 (2017).
- [20] A. Lukin, M. Rispoli, R. Schittko, M. E. Tai, A. M. Kaufman, S. Choi, V. Khemani, J. L´ eonard, and M. Greiner, Probing entanglement in a many-body-localized system, Science 364 , 256 (2019).
- [21] A. Rubio-Abadal, J.-y. Choi, J. Zeiher, S. Hollerith, J. Rui, I. Bloch, and C. Gross, Many-body delocalization in the presence of a quantum bath, Phys. Rev. X 9 , 041014 (2019).
- [22] V. Oganesyan and D. A. Huse, Localization of interacting fermions at high temperature, Phys. Rev. B 75 , 155111 (2007).
- [23] M. ˇ Znidariˇ c, T. c. v. Prosen, and P. Prelovˇ sek, Manybody localization in the heisenberg xxz magnet in a random field, Phys. Rev. B 77 , 064426 (2008).
- [24] A. Pal and D. A. Huse, Many-body localization phase transition, Phys. Rev. B 82 , 174411 (2010).
- [25] B. Bauer and C. Nayak, Area laws in a many-body localized state and its implications for topological order, Journal of Statistical Mechanics: Theory and Experiment 2013 , P09005 (2013).
- [26] A. D. Luca and A. Scardicchio, Ergodicity breaking in a model showing many-body localization, Europhysics Letters 101 , 37003 (2013).
- [27] J. A. Kj¨ all, J. H. Bardarson, and F. Pollmann, Manybody localization in a disordered quantum ising chain, Phys. Rev. Lett. 113 , 107204 (2014).
- [28] D. J. Luitz, N. Laflorencie, and F. Alet, Many-body localization edge in the random-field heisenberg chain, Phys. Rev. B 91 , 081103 (2015).
- [29] C. Artiaco, F. Balducci, M. Heyl, A. Russomanno, and A. Scardicchio, Spatiotemporal heterogeneity of entanglement in many-body localized systems, Phys. Rev. B 105 , 184202 (2022).
- [30] C. Artiaco, C. Fleckenstein, D. Aceituno Ch´ avez, T. K. Kvorning, and J. H. Bardarson, Efficient large-scale

many-body quantum dynamics via local-information time evolution, PRX Quantum 5 , 020352 (2024).

- [31] Y. Bar Lev, G. Cohen, and D. R. Reichman, Absence of diffusion in an interacting system of spinless fermions on a one-dimensional disordered lattice, Phys. Rev. Lett. 114 , 100601 (2015).
- [32] F. Iemini, A. Russomanno, D. Rossini, A. Scardicchio, and R. Fazio, Signatures of many-body localization in the dynamics of two-site entanglement, Phys. Rev. B 94 , 214206 (2016).
- [33] E. V. Doggen, I. V. Gornyi, A. D. Mirlin, and D. G. Polyakov, Many-body localization in large systems: Matrix-product-state approach, Annals of Physics 435 , 168437 (2021), special Issue on Localisation 2020.
- [34] M. Serbyn, Z. Papi´ c, and D. A. Abanin, Local conservation laws and the structure of the many-body localized states, Phys. Rev. Lett. 111 , 127201 (2013).
- [35] D. A. Huse, R. Nandkishore, and V. Oganesyan, Phenomenology of fully many-body-localized systems, Phys. Rev. B 90 , 174202 (2014).
- [36] J. Z. Imbrie, V. Ros, and A. Scardicchio, Local integrals of motion in many-body localized systems, Annalen der Physik 529 , 1600278 (2017).
- [37] G. D. Chiara, S. Montangero, P. Calabrese, and R. Fazio, Entanglement entropy dynamics of heisenberg chains, Journal of Statistical Mechanics: Theory and Experiment 2006 , P03001 (2006).
- [38] J. Eisert, M. Cramer, and M. B. Plenio, Colloquium: Area laws for the entanglement entropy, Rev. Mod. Phys. 82 , 277 (2010).
- [39] J. H. Bardarson, F. Pollmann, and J. E. Moore, Unbounded growth of entanglement in models of many-body localization, Phys. Rev. Lett. 109 , 017202 (2012).
- [40] M. Serbyn, Z. Papi´ c, and D. A. Abanin, Universal slow growth of entanglement in interacting strongly disordered systems, Phys. Rev. Lett. 110 , 260601 (2013).
- [41] D. Roy, R. Singh, and R. Moessner, Probing many-body localization by spin noise spectroscopy, Physical Review B 92 , 10.1103/physrevb.92.180205 (2015).
- [42] F. Alet and N. Laflorencie, Many-body localization: An introduction and selected topics, Comptes Rendus Physique 19 , 498 (2018).
- [43] D. A. Abanin, E. Altman, I. Bloch, and M. Serbyn, Colloquium: Many-body localization, thermalization, and entanglement, Rev. Mod. Phys. 91 , 021001 (2019).
- [44] P. Sierant, M. Lewenstein, A. Scardicchio, L. Vidmar, and J. Zakrzewski, Many-Body Localization in the Age of Classical Computing, arXiv e-prints 10.48550/arXiv.2403.07111 (2024).
- [45] W. De Roeck and F. m. c. Huveneers, Stability and instability towards delocalization in many-body localization systems, Phys. Rev. B 95 , 155129 (2017).
- [46] S. Gopalakrishnan and D. A. Huse, Instability of manybody localized systems as a phase transition in a nonstandard thermodynamic limit, Phys. Rev. B 99 , 134305 (2019).
- [47] K. Agarwal, E. Altman, E. Demler, S. Gopalakrishnan, D. A. Huse, and M. Knap, Rare-region effects and dynamics near the many-body localization transition, Annalen der Physik 529 , 1600326 (2017).
- [48] I.-D. Potirniche, S. Banerjee, and E. Altman, Exploration of the stability of many-body localization in d &gt; 1, Phys. Rev. B 99 , 205149 (2019).
- [49] T. Szoglyph[suppress] ldra, P. Sierant, M. Lewenstein, and J. Zakrzewski, Catching thermal avalanches in the disordered xxz model, Phys. Rev. B 109 , 134202 (2024).
- [50] J. L´ eonard, S. Kim, M. Rispoli, A. Lukin, R. Schittko, J. Kwan, E. Demler, D. Sels, and M. Greiner, Probing the onset of quantum avalanches in a many-body localized system, Nature Physics 19 , 481 (2023).
- [51] H. P. L¨ uschen, P. Bordia, S. S. Hodgman, M. Schreiber, S. Sarkar, A. J. Daley, M. H. Fischer, E. Altman, I. Bloch, and U. Schneider, Signatures of many-body localization in a controlled open quantum system, Phys. Rev. X 7 , 011034 (2017).
- [52] D. J. Luitz, F. m. c. Huveneers, and W. De Roeck, How a small quantum bath can thermalize long localized chains, Phys. Rev. Lett. 119 , 150602 (2017).
- [53] L. Colmenarez, D. J. Luitz, and W. De Roeck, Ergodic inclusions in many-body localized systems, Phys. Rev. B 109 , L081117 (2024).
- [54] J. C. Peacock and D. Sels, Many-body delocalization from embedded thermal inclusion, Phys. Rev. B 108 , L020201 (2023).
- [55] D. Sels, Bath-induced delocalization in interacting disordered spin chains, Phys. Rev. B 106 , L020202 (2022).
- [56] Y.-T. Tu, D. Vu, and S. Das Sarma, Avalanche stability transition in interacting quasiperiodic systems, Phys. Rev. B 107 , 014203 (2023).
- [57] A. Morningstar, L. Colmenarez, V. Khemani, D. J. Luitz, and D. A. Huse, Avalanches and many-body resonances in many-body localized systems, Phys. Rev. B 105 , 174205 (2022).
- [58] Unrelated with the problem of the thermal inclusion, many works have studied the effect on MBL if a bath connected to the whole system [91-94].
- [59] S. Gopalakrishnan, M. M¨ uller, V. Khemani, M. Knap, E. Demler, and D. A. Huse, Low-frequency conductivity in many-body localized systems, Phys. Rev. B 92 , 104202 (2015).
- [60] P. J. D. Crowley and A. Chandran, A constructive theory of the numerically accessible many-body localized to thermal crossover, SciPost Phys. 12 , 201 (2022).
- [61] H. Ha, A. Morningstar, and D. A. Huse, Many-body resonances in the avalanche instability of many-body localization, Phys. Rev. Lett. 130 , 250405 (2023).
- [62] J. 'Colbois, F. Alet, and N. Laflorencie, InteractionDriven Instabilities in the Random-Field XXZ Chain, arXiv e-prints (2024), arXiv:2403.09608 [cond-mat.disnn].
- [63] J. ˇ Suntajs, J. Bonˇ ca, T. c. v. Prosen, and L. Vidmar, Quantum chaos challenges many-body localization, Phys. Rev. E 102 , 062144 (2020).
- [64] J. ˇ Suntajs, J. Bonˇ ca, T. c. v. Prosen, and L. Vidmar, Ergodicity breaking transition in finite disordered spin chains, Phys. Rev. B 102 , 064207 (2020).
- [65] D. Sels and A. Polkovnikov, Dynamical obstruction to localization in a disordered spin chain, Phys. Rev. E 104 , 054105 (2021).
- [66] T. L. M. Lezama and Y. B. Lev, Logarithmic, noiseinduced dynamics in the Anderson insulator, SciPost Phys. 12 , 174 (2022).
- [67] D. S. Bhakuni, T. L. M. Lezama, and Y. B. Lev, Noiseinduced transport in the Aubry-Andr´ e-Harper model, SciPost Phys. Core 7 , 023 (2024).
- [68] X. Cao, A. Tilloy, and A. De Luca, Entanglement in a fermion chain under continuous monitoring, SciPost

[Phys. 7 , 24 (2019).](https://doi.org/10.21468/SciPostPhys.7.2.024)

- [69] [I. H. Kim, A. Chandran, and D. A. Abanin, Local integrals of motion and the logarithmic lightcone in manybody localized systems (2014), arXiv:1412.3073 [condmat.dis-nn].](https://arxiv.org/abs/1412.3073)
- [70] [A. Elgart and A. Klein, Slow propagation of information on the random xxz quantum spin chain (2024), arXiv:2311.14188 [math-ph].](https://arxiv.org/abs/2311.14188)
- [71] D. Toniolo and S. Bose, Stability of slow Hamiltonian dynamics from Lieb-Robinson bounds, arXiv e-prints https://doi.org/10.48550/arXiv.2405.05958 (2024).
- [72] P. Sierant and J. Zakrzewski, Challenges to observation of many-body localization, Phys. Rev. B 105 , 224203 (2022).
- [73] L. Colmenarez, P. A. McClarty, M. Haque, and D. J. Luitz, Statistics of correlation functions in the random Heisenberg chain, SciPost Phys. 7 , 064 (2019).
- [74] P. Sierant and J. Zakrzewski, Level statistics across the many-body localization transition, Phys. Rev. B 99 , 104205 (2019).
- [75] T. Chanda, P. Sierant, and J. Zakrzewski, Time dynamics with matrix product states: Many-body localization transition of large systems revisited, Phys. Rev. B 101 , 035148 (2020).
- [76] M. Serbyn, A. A. Michailidis, D. A. Abanin, and Z. Papi´ c, Power-law entanglement spectrum in many-body localized phases, Phys. Rev. Lett. 117 , 160601 (2016).
- [77] E. V. H. Doggen, F. Schindler, K. S. Tikhonov, A. D. Mirlin, T. Neupert, D. G. Polyakov, and I. V. Gornyi, Many-body localization and delocalization in large quantum chains, Phys. Rev. B 98 , 174202 (2018).
- [78] P. Sierant, M. Lewenstein, and J. Zakrzewski, Polynomially filtered exact diagonalization approach to manybody localization, Phys. Rev. Lett. 125 , 156601 (2020).
- [79] D. Abanin, J. Bardarson, G. De Tomasi, S. Gopalakrishnan, V. Khemani, S. Parameswaran, F. Pollmann, A. Potter, M. Serbyn, and R. Vasseur, Distinguishing localization from chaos: Challenges in finite-size systems, Annals of Physics 427 , 168415 (2021).
- [80] E. Lieb, T. Schultz, and D. Mattis, Two soluble models of an antiferromagnetic chain, Annals of Physics 16 , 407 (1961).
- [81] R. Sidje, Expokit: A software package for computing matrix exponentials, ACM Trans. Math. Softw. 24 , 130 (1998).
- [82] P. Bordia, H. P. L¨ uschen, S. S. Hodgman, M. Schreiber, I. Bloch, and U. Schneider, Coupling identical onedimensional many-body localized systems, Phys. Rev. Lett. 116 , 140401 (2016).
- [83] D. J. Luitz, N. Laflorencie, and F. Alet, Extended slow dynamical regime close to the many-body localization transition, Phys. Rev. B 93 , 060201 (2016).
- [84] For the smaller values of L , where relaxation times are shorter, we can use larger threshold, and get clearer exponential increases with W than the ones shown in Fig. 3(a).
- [85] Y. Bar Lev, G. Cohen, and D. R. Reichman, Absence of diffusion in an interacting system of spinless fermions on a one-dimensional disordered lattice, Phys. Rev. Lett. 114 , 100601 (2015).
- [86] K. Slagle, Z. Bi, Y.-Z. You, and C. Xu, Out-of-timeorder correlation in marginal many-body localized systems, Phys. Rev. B 95 , 165136 (2017).
- [87] D. B. Gutman, I. V. Protopopov, A. L. Burin, I. V. Gornyi, R. A. Santos, and A. D. Mirlin, Energy transport in the anderson insulator, Phys. Rev. B 93 , 245427 (2016).
- [88] N. Y. Yao, C. R. Laumann, S. Gopalakrishnan, M. Knap, M. M¨ uller, E. A. Demler, and M. D. Lukin, Many-body localization in dipolar systems, Phys. Rev. Lett. 113 , 243002 (2014).
- [89] D. Vu, K. Huang, X. Li, and S. Das Sarma, Fermionic many-body localization for random and quasiperiodic systems in the presence of short- and long-range interactions, Phys. Rev. Lett. 128 , 146601 (2022).
- [90] G. B. Mbeng, A. Russomanno, and G. E. Santoro, The quantum Ising chain for beginners, SciPost Phys. Lect. Notes , 82 (2024).
- [91] M. H. Fischer, M. Maksymenko, and E. Altman, Dynamics of a many-body-localized system coupled to a bath, Phys. Rev. Lett. 116 , 160401 (2016).
- [92] E. Levi, M. Heyl, I. Lesanovsky, and J. P. Garrahan, Robustness of many-body localization in the presence of dissipation, Phys. Rev. Lett. 116 , 237203 (2016).
- [93] B. Everest, I. Lesanovsky, J. P. Garrahan, and E. Levi, Role of interactions in a dissipative many-body localized system, Phys. Rev. B 95 , 024310 (2017).
- [94] M. V. Medvedyeva, T. c. v. Prosen, and M. ˇ Znidariˇ c, Influence of dephasing on many-body localization, Phys. Rev. B 93 , 094205 (2016).