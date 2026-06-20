## Disorder-Induced Strongly Correlated Photons in Waveguide QED

Guoqing Tian, 1 Li-Li Zheng, 2, ∗ Zhi-Ming Zhan, 2 Franco Nori, 3, 4 and Xin-You L¨ u 1, †

1 School of Physics and Institute for Quantum Science and Engineering, Huazhong University of Science and Technology,

and Wuhan institute of quantum technology, Wuhan, 430074, P. R. China

2 School of Artificial Intelligence, Jianghan University, Wuhan 430074, China

3 Quantum Computing Center, RIKEN, Wakoshi, Saitama 351-0198, Japan

Department of Physics, The University of Michigan, Ann Arbor, Michigan 48109-1040, USA (Dated: October 14, 2025)

4

Strongly correlated photons play a crucial role in modern quantum technologies. Here, we investigate the probability of generating strongly correlated photons in a chain of N qubits coupled to a one-dimensional (1D) waveguide. We found that disorder in the transition frequencies can induce photon antibunching, and especially nearly perfect photon blockade events in the transmission and reflection outputs. As a comparison, in ordered chains, strongly correlated photons cannot be generated in the transmission output, and only weakly antibunched photons are found in the reflection output. The occurrence of nearly perfect photon blockade events stems from the disorder-induced near completely destructive interference of photon scattering paths. Our work highlights the impact of disorder on photon correlation generation and suggests that disorder can enhance the potential for achieving strongly correlated photon.

Strongly correlated photons are of importance in a wide range of quantum optical applications, including quantum communication[1-3], quantum computation [46], and the study of fundamental quantum mechanics [7, 8]. Various methods have been developed to produce such strongly correlated photons in the fields of cavity QED[9-12] and waveguide QED[13-15]. In particular, the 1D waveguide QED platform offers a highly controlled environment for interacting photons with quantum emitters, providing an excellent means to realize strongly correlated photons [16-20]. By leveraging the properties of waveguide structures and the coupling with quantum emitters, the scattered light can exhibit either temporal photon attraction (bunching) or repulsion (antibunching), owing to the interference effects and the intrinsic nonlinearity of quantum emitters, making the waveguide QED platform stand out as a powerful tool for generating and manipulating strongly correlated photons for quantum technologies [21-28].

In practical experimental settings, disorder arising from fabrication limitations is inherently unavoidable. Research on the impact of disorder in quantum systems is an active area of study, e.g., [29-31]. Over the past few decades, the effects of disorder have also been extensively studied in the fields of cavity and waveguide QED [32-41]. These works demonstrated that disorder has significant impact on localization-delocalization and the quantum dynamics of the atomic excitations. However, the correlation of scattered photons in the presence of disorder remains relatively unexplored. Crucially, given that the correlation of scattered photons significantly depends on the nonlinearity, namely the level structure of the quantum emitters, this raises an intriguing question: Can the system produce strongly correlated photons, if the disorder in the level structure of quantum emitters is taken into account?

In this work, we address this question and give a positive answer by quantitatively studying the possibility of strong correlation events of scattered photons in a chain of N qubits coupled to a 1D waveguide. The strong correlation events studied in our work are photon antibunching (PA), perfect photon blockade (PPB) and nearly perfect photon blockade (NPPB) events, which have been extensively investigated across various physical systems [42-50]. For a resonant, weak classical input light, the transmission output does not generate antibunched photons when N = 1, while the reflection output always exhibits PPB due to the Pauli blockade. For N = 2, neither the transmission nor the reflection output produces antibunched photons. The presence of disorder does not change the possibility of these strong correlation events [see Fig. S2(b)].

When the chain contains multiple ( N &gt; 2) qubits, antibunched photons do not occur in the transmission output and only weakly antibunched photons occur in the reflection output. Notably, introducing disorder makes these strong correlation events possible. Especially, we show that the probability of NPPB events remains finite, in stark contrast to ordered chains where NPPB events are absent. The occurrence of NPPB events stems from the destructive interference of the photons scattering path induced by the disorder. Furthermore, the probability of these strongly correlated photon events can be effectively increased by appropriately adjusting the system parameters. Specifically, increasing the chain size can enhance the probability of both PA and NPPB events in the transmission output, and the probability of NPPB events in the reflection output increases with disorder.

Model .-Let us consider a right propagating coherent pulse with frequency ω 0 (zero bandwidth) and strength

FIG. 1. (a) Schematics of a chain of qubits coupled to a 1D waveguide. The qubits have different transition frequencies denoted by ω k = ω 0 + ∆ k . The decay rate of each qubit is γ , and the qubits are uniformly-spaced with distance d . For a weak classical input light with frequency ω 0 , both the reflection and the transmission outputs can generate strongly correlated photons. (b) PA, PPB, and NPPB events for the reflection and transmission outputs. Here PPB (NPPB) corresponds to N ≤ 2 ( N &gt; 2). The corresponding event is possible (denoted by ' ✓ ') or impossible (' ✗ '). Blue (red) color denotes the events for systems without (with) disorder.

<!-- image -->

α as input light interacting with an chain of N qubits with inhomogeneous transition frequency ω m = ω 0 + ∆ m [see Fig. S2(a)]. The detunings of the qubits follow a normal distribution, i.e., p (∆ 1 , ∆ 2 , · · · , ∆ N ) = ∏ N m =1 p (∆ m ), with p (∆ m ) = exp ( -∆ 2 m / 2 W 2 ) / √ 2 πW 2 . We assume that the qubits only weakly deviate from the resonant frequency ω 0 , with the condition ω 0 /W ≫ N , such that the time evolution of the qubits can be described by the master equation ˙ ρ = -i [( H eff + H d ) ρ -ρ ( H † eff + H d )] + ∑ mn 2( γ T Θ( m -n ) + γ R Θ( n -m ) + γ nw δ m,n ) cos( | m -n | φ ) σ m ρσ † n [51, 52]. Here H d = ∑ m √ γ T α ( e imφ σ † m + h.c. ), γ T ( γ R ) is the individual decay rate of each qubit to transmission (reflection) waveguide mode and γ nw is the loss to non-waveguide (nw) modes, φ = ω 0 d/c , with d being the distance between adjacent qubits; Θ( x ) denotes the Heaviside function. The non-Hermitian effective Hamiltonian is (in the rotated frame with respect to H 0 = ∑ m ω 0 σ † m σ m ),

$$H _ { e f f } = & \sum _ { m = 1 } ^ { N } \left ( \Delta _ { m } - \frac { i ( \gamma _ { n w } + \gamma _ { T } + \gamma _ { R } ) } { 2 } \right ) \sigma _ { m } ^ { \dagger } \sigma _ { m } \\ & - i \sum _ { m > n } \left ( \gamma _ { T } e ^ { i | m - n | \varphi } \sigma _ { m } ^ { \dagger } \sigma _ { n } + \gamma _ { R } e ^ { i | m - n | \varphi } \sigma _ { n } ^ { \dagger } \sigma _ { m } \right ) . & \text {ward} \\ & \text {we consider } \gamma _ { n w } = 0 \text { and } \gamma _ { R } = \gamma _ { T } = \gamma / 2 \text { in main text, } \text { single}$$

We consider γ nw = 0 and γ R = γ T = γ/ 2 in main text, discussing the impact of losses to non-waveguide modes and the chirality in the Supplemental Materials [51]. We also discuss the effect of finite bandwidth of the input state. We show that the obtained results for a finitebandwidth input show good agreements with those for zero-bandwidth input, provided that the bandwidth is an order of magnitude below the individual decay rate of qubit [51]. This validates the zero-bandwidth approximation considered in our work; and the requirement of such narrow bandwidth can be experimentally implemented in the state-of-the-art waveguide platforms [18, 53, 54]. Hereafter, we choose γ as the energy scale and set γ = 1 in our numerical calculations. We only consider 0 ≤ φ ≤ π/ 2, due to the symmetry of this system.

The correlation of the emitted field is characterized by the zero-time second-order photon correlation function g µ = ⟨ a † 2 µ, out ( t ) a 2 µ, out ( t ) ⟩ / ⟨ a † µ, out ( t ) a µ, out ( t ) ⟩ 2 , where a µ, out ( t ), with µ = T (R) denotes the annihilation operator of the transmission (reflection) mode in the time domain. Utilizing the input-output formalism [55], the formal expressions of the correlations g µ in the weakdrive limit, α ≪ 1, can be calculated as [51]

$$\ g _ { T } = \frac { | 1 - 2 i \langle \phi _ { + } ^ { 1 } | \psi ^ { 1 } \rangle - \langle \phi _ { + } ^ { 2 } | \psi ^ { 2 } \rangle | ^ { 2 } } { | 1 - i \langle \phi _ { + } ^ { 1 } | \psi ^ { 1 } \rangle | ^ { 4 } } , \quad g _ { R } = \frac { | \langle \phi _ { - } ^ { 2 } | \psi ^ { 2 } \rangle | ^ { 2 } } { | \langle \phi _ { - } ^ { 1 } | \psi ^ { 1 } \rangle | ^ { 4 } } . \quad ( 2 )$$

Here | ϕ 1 ± ⟩ = √ 1 / 2 ∑ m exp( ± imφ ) σ † m | G ⟩ and | ϕ 2 ± ⟩ = ∑ m&gt;n exp( ± i ( m + n ) φ ) σ † m σ † n | G ⟩ , with | G ⟩ being the fully-inverted ground state of qubits; | ψ 1 ⟩ = -( H (1) eff ) -1 H + | G ⟩ and | ψ 2 ⟩ = -( H (2) eff ) -1 H + | ψ 1 ⟩ are respectively the singleand two-excitation component of the truncated steady-state solution for the qubit ensemble, with H + = √ γ/ 2 ∑ m e imφ σ † m . H (1) eff and H (2) eff are the singleand two-excitation sectors of Eq. (S1). In the presence of disorder, the probability density functions of g µ encode the full information of the photon correlations. The definition of the probability density function is given by P ( s ) = ∫ ∞ -∞ · · · ∫ ∞ -∞ δ ( g µ -s ) p (∆ 1 , · · · , ∆ N )d∆ 1 · · · d∆ N . The value of P ( s ) ranges from 0 to infinity, and is proportional to the probability of having a correlation function with value s . Especially, P ( ϵ ) with ϵ → 0 ( ϵ = 0) is proportional to the probability of a NPPB (PPB) event. We also define P ( s &lt; 1) := ∫ 1 0 P ( s )d s , which corresponds to the probability of the field being antibunched.

Photon correlations without system disorder .-Photon correlations in the qubit chains, including the Markov property [24, 56-60] and chirality [61] have been extensively studied. For the transmission output, when the qubits are strongly coupled ( γ nw = 0) to the waveguide in a non-chiral configuration ( γ R = γ T ), a straightforward result is that g T is always divergent regardless of the chain size N and distance d . The strong photon bunching occurs because resonant qubits block the propagation of single photons from the input [62, 63], hence the output field contains only multiphoton components. While when the qubits are weakly coupled ( γ nw ≫ γ R + γ T ) to the waveguide in a perfectly chiral configuration ( γ R = 0), the photon statistics of the transmitted light evolving from Poissonian to antibunching and even bunching as the number of qubits increases [51], which is consistent with the results reported in [25]. For the reflection output, g R = 0 when a single qubit is coupled to the waveguide. This PPB occurs because a single qubit cannot be excited by two photons simultaneously [15]. When two qubits are coupled to the waveguide, the output light maintains coherent, i.e., g R = 1. When the chain contains N &gt; 2 qubits, it is practically impossible to derive a closed-form expression for the correlation function. The numerical result for g R as a function of N and φ is given in Fig. S4 of the Supplemental Materials [51]. The result shows that, for N &gt; 2, the reflected photons exhibit weak bunching for φ within the range 0 to 0 . 25 π and weak antibunching for φ within the range 0 . 3 π to 0 . 5 π .

FIG. 2. Correlation statistics of the transmission output. Probability of PA versus φ and W in (a), and versus N and W in (b). Inset in (a) displays the zoom-in of (a). N = 10 in (a). In (b), φ = 0 . 0125 π , corresponding to the position where P ( s &lt; 1) in (a) reach its maximum value. In all plots, the results are obtained from Monte Carlo integration. The numerical details are discussed in the Supplemental Materials [51].

<!-- image -->

̸

Transmission photon correlations with system disorder .-In the presence of disorder, the inhomogeneity in transition frequencies significantly modulates photon correlations in the transmission output. For a chain with a few qubits, we can derive an explicit expression of g T . For example, for a single-qubit system the correlation function is given by g T = (1+4∆ 2 1 ) 2 / (16∆ 4 1 ). In contrast to the divergent correlation obtained in a clean chain, g T remains finite provided that the qubit is off-resonant with the input (i.e., ∆ 1 = 0). However, one can readily show that g T &gt; 1, which indicates that the transmission light is consistently bunched, thereby ruling out the possibility of PA and PPB. In other words, for system with N = 1 it follows that P ( s &lt; 1) = P (0) = 0. For an array with N = 2, the correlation function is given by

$$g _ { T } = \frac { q ( ( \Delta _ { 1 } + \Delta _ { 2 } ) ^ { 2 } ( f _ { - } - \cos \varphi ) + p ) } { ( 6 4 \Delta _ { 1 } ^ { 4 } \Delta _ { 2 } ^ { 4 } ( 1 + ( \Delta _ { 1 } + \Delta _ { 2 } ) ^ { 2 } ) ) } , \quad ( 3 ) \quad \begin{matrix} \text {order} \\ \text {gle p} \end{matrix}$$

where q = 8∆ 2 1 ∆ 2 2 + f + -cos 2 φ and p = 8∆ 2 1 ∆ 2 2 (1 + (∆ 1 + ∆ 2 ) 2 ) + 4∆ 1 ∆ 2 (∆ 1 + ∆ 2 ) sin 2 φ , with f ± = 1 + 2∆ 2 1 +2∆ 2 2 ± 4∆ 1 ∆ 2 cos(2 φ ) -2(∆ 1 +∆ 2 ) sin(2 φ ). The correlation function has a minimum value min { g T } = 1. Hence, the same conclusion applies to the two-qubit system, i.e., P ( s &lt; 1) = 0 and P (0) = 0.

FIG. 3. Correlation statistics of the transmission output. (a,b) Probability density functions. The chosen parameters are { N = 3 , φ = 0 . 04 π, W = 0 . 14 } in (a) and { N = 3 , φ = 0 , W = 1 } in (b). Inset of (a) shows the solutions { ∆ 1 , ∆ 2 , ∆ 3 } that satisfy g T = 10 -10 . The solutions are constrained to | ∆ j | ≤ 1. Inset of (b) shows g min T , corresponding to the minimum value of g T , for φ = 0 (blue line) and for φ = 0 . 04 π (orange line) with respect to chain size, dashed line is the numerical fit N -2 . (c,d) P (10 -3 ) versus φ and W in (c), and versus N and W in (d). N = 10 in (c). In (d), φ = 0 . 006 π , corresponding to the position where P (10 -3 ) in (c) reach its maximum value.

<!-- image -->

When the chain contains more than two qubits, an explicit expression of the correlation function becomes too complex to work out P ( s &lt; 1) analytically [51]. In Figs. S3(a,b), we present the numerical results of P ( s &lt; 1) under various phases, chain sizes, and disorder strengths. In contrast to the few-qubit array, these results show that antibunched photons can occur in the transmission output. Notably, in the intermediate-disorder regime ( W ∼ O (1)), P ( s &lt; 1) attains its maximum value when the array is highly dense ( φ ≪ 1) and the chain size is appropriately taken. Such requirement from deeply subwavelength qubit array can be relaxed by the periodicity φ → φ + 2 π of the system [51]. Moreover, the deeply subwavelength qubit distance is experimentally feasible in the state-of-the-art superconducting platforms [20], so that the condition φ ≪ 1 can also be experimentally implemented. For a sparse array, P ( s &lt; 1) rapidly decreases with either an increase or a decrease in the disorder strength. In the weak-disorder limit W ≪ 1, a single photon has a low probability of propagating through the chain, resulting in a low probability of PA. In the strong-disorder limit W ≫ 1, the long-range interaction mediated by photons is largely quenched; consequently, the probability of PA decreases as disorder becomes too strong [51].

FIG. 4. Correlation statistics of the transmission output. (a) The maximum values of P ( s &lt; 1) and P (10 -3 ) versus N . Green circles (purple squares) display the maximum values of P ( s &lt; 1) ( P (10 -3 )) versus N . Green and purple solid lines are the numerical fits of 1 -0 . 97 N -1 / 40 and 0 . 04 N 1 / 2 , respectively. (b) and (c) display W and φ , respectively, where P ( s &lt; 1) and P (10 -3 ) reach their maximum values. Black arrows point in the direction of increasing N . Inset of (c) displays the zoom-in of (c).

<!-- image -->

Regarding the possibility of NPPB events, we first present the probability density function for a system with N = 3 and φ/π = 0 . 04 in Fig. S4(a). Our results indicate that P ( s ) saturates to a constant value for s ≪ 1, implying that P ( s → 0) = 0. This behavior of P ( s ) is attributed to the existence of specific detuning values { ∆ 1 , ∆ 2 , ∆ 3 } that satisfy the NPPB condition g T = ε [see the inset of Fig. S4(a)], where ε can be arbitrarily close to 0 [51]. According to scattering theory [27], these NPPB events stem from the nearly completely destructive interference of single-photon scattering paths with probability amplitude ⟨ ϕ 1 + | ψ 1 ⟩ , the two-photon scattering paths with probability amplitude ⟨ ϕ 2 + | ψ 2 ⟩ , and the free propagation paths with probability amplitude 1. These scattering paths are further determined by the transition paths that are governed by the non-Hermitian effective Hamiltonian Eq. (S1). A detailed discussion of these destructive effects is provided in [51]. Considering such asymptotic behavior of P ( s ), hereafter, we adopt P (10 -3 ) as the representative value of the probability density function for an NPPB event. In Figs. S4(c,d), we present P (10 -3 ) for different system parameters. Our results show that NPPB events can occur, provided that φ = 0. In the Dicke-limit φ = 0, however, we find P (10 -3 ) = 0 for relatively small chain sizes [see Fig. S4(b)]. In this case, P (10 -3 ) vanishes because, unlike the systems with φ = 0 where g T can be arbitrarily close to 0, the correlation function for φ = 0 can only attain a minimal value that scales as N -2 with the chain size [see the inset of Fig. S4(b)]. This indicates that P ( ϵ ) = 0 for ϵ ≲ N -2 .

̸

Our results shown in Figs. S3-S4 demonstrate that

̸

̸

FIG. 5. Correlation statistics of the reflection output. P ( s &lt; 1) versus φ and W in (a), and versus N and W in (b). The white solid curve in (a) denotes the regime where P ( s &lt; 1) = 1 / 2. N = 10 in (a). φ = 0 . 4 π ( φ = 0 . 1 π ) in the top (bottom) of (b). (c) ˜ P ( s &lt; 1) for different chain sizes and phases, with ˜ P ( s &lt; 1) = P ( s &lt; 1) -2 / 3. W = 100 in (c). (d) P (10 -µ ) versus disorder strength. Solid lines in different colors correspond to different values of µ , with µ = -3 , -5 , -7. Dashed lines are the numerical slopes. In (d), we only consider the contributions from non-interacting transition paths, whose validation is discussed in [51]. Results are obtained from 10 10 disorder realizations.

<!-- image -->

both P ( s &lt; 1) and P (10 -3 ) can attain their optimal (maximum) values when system parameters are suitably tuned. We subsequently investigate how these optimal values depend on the system parameters. As shown in Fig. S5(a), the maximum values of P ( s &lt; 1) and P (10 -3 ) exhibit power-law scaling with the number N of qubits according to (1 -0 . 97 N -1 / 40 ) and 0 . 04 N 1 / 2 , respectively. In addition to power-law scaling, the dependence of these optimal values on W and φ exhibits both similar and distinctive features. Specifically, as the number of qubits increases, the optimal values of P ( s &lt; 1) and P (10 -3 ) are reached at lower values of φ ; however, achieving the maximum P ( s &lt; 1) requires a stronger disorder strength, whereas the maximum P (10 -3 ) is obtained when the disorder strength is around 0.15 [see Figs. S5(b,c)].

Reflection photon correlations with system disorder .-One can expect that correlations in the reflection output exhibit behaviors distinct from those obtained in the transmission output, since reflected photons necessarily interact with the qubits, whereas transmitted photons can pass through the waveguide without interaction. In the presence of disorder, it is evident that g R = 0 for N = 1, implying that only PPB events occur. For a twoqubit chain, the correlation function is given by g R = | ( -i + i exp(2 iφ )+2∆ 1 +2∆ 2 )(exp(2 iφ )+(2∆ 1 -i )(2∆ 2 -i )) / ((∆ 1 +∆ 2 -i )(2∆ 2 -i +exp(2 iφ )(2∆ 1 + i )) 2 ) | 2 . Based on this explicit expression, in the Supplemental Materi- als [51], we show analytically and numerically that

$$\mathbb { P } ( s < 1 ) \geq \frac { 2 } { 3 } , \quad P ( 0 ) = 0 . \quad \ \ \ ( 4 ) \quad \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \$$

This result reveals two features: (i) Introducing disorder enables PA events, with a probability exceeding 1 / 2, indicating that the output light is more likely to be antibunched; (ii) Despite the possibility of PA, the two-qubit system rules out the possibility of PPB, due to the absence of destructive interference of two-photon scattering paths. In fact, only strong PA can occur, provided that one qubit is far off-resonant while the other remains nearly resonant. In this case, the two-photon scattering probability amplitude ⟨ ϕ 2 -| ψ 2 ⟩ is near zero, due to a large detuning, | ∆ 1 + ∆ 2 | ≫ 1, between the two-excitation state of the qubits and the two-photon state of the input; meanwhile, the single-photon scattering probability amplitude ⟨ ϕ 1 -| ψ 1 ⟩ is near unity, since the nearly resonant qubit blocks the transmission of single photons from the input. However, the PPB events can never occur, since ⟨ ϕ 2 -| ψ 2 ⟩ can never be exactly zero, due to the finite detuning of the far off-resonant qubit.

For a chain with N &gt; 2, the behavior of P ( s &lt; 1) is distinct from those obtained in chains with fewer qubits. In Figs. S6(a,b), we present the results of P ( s &lt; 1) for different system parameters. Our results reveal that, for W ≪ 1, the system exhibits a high (low) probability of PA when 0 . 3 π &lt; φ &lt; 0 . 5 π (0 &lt; φ &lt; 0 . 25 π ). As disorder strength increases, the probability of PA decreases (increases) when 0 . 3 π &lt; φ &lt; 0 . 5 π (0 &lt; φ &lt; 0 . 25 π ). In the strong-disorder regime, P ( s &lt; 1), especially for large chain sizes, saturates at a value close to 2 / 3 [see Fig. S6(c)]. This value corresponds to the probability of PA for the two-qubit system with φ = 0[51]. Regarding the probability of NPPB, its value increases and follows a power-law scaling with disorder strength when W ≫ 1 [see Fig. S6(d)]. This is in contrast to the results of the transmission output, where P (10 -3 ) rapidly decreases when disorder becomes too strong. We show in the Supplemental Materials that [51], the enhancement of the probability of NPPB events in the reflection output stems from the fact that NPPB events involve solely the nearly completely destructive interference of two-photon non-interacting scattering paths.

Conclusion .-In summary, we have investigated the possibility of generating repulsively correlated photons in a chain of qubits coupled to a 1D waveguide. We found that, in the presence of disorder, it is possible to produce antibunched and nearly perfect blockaded photons, provided that the system parameters N , φ , and W are suitably chosen. Furthermore, we demonstrate that the interplay among these parameters can significantly modulate the probability of strongly correlated photon events. Notably, our results reveal that the probabilities of PA and NPPB increase with the number of qubits according to a power-law scaling, while the proba- bility of NPPB exhibits a power-law scaling with disorder strength. Our findings not only reveal the critical role of disorder in enabling strong photon correlations but also pave the way for disorder-engineered strongly correlated photons and potential single-photon sources.

Acknowledgement .-We sincerely thank Prof. Francesco Ciccarello for his valuable suggestions and insightful comments, which have greatly improved this work. We also thank Zhi-Guang Lu for his valuable suggestions. X.-Y. L. is supported by the National Science Fund for Distinguished Young Scholars of China (Grant No. 12425502), the Innovation Program for Quantum Science and Technology (Grant No. 2024ZD0301000), the National Key Research and Development Program of China (Grant No. 2021YFA1400700), and the Fundamental Research Funds for the Central Universities (Grant No. 2024BRA001). F.N. is supported in part by: the Japan Science and Technology Agency (JST) [via the CREST Quantum Frontiers program Grant No. JPMJCR24I2, the Quantum Leap Flagship Program (Q-LEAP), and the Moonshot R&amp;D Grant Number JPMJMS2061], and the Office of Naval Research (ONR) Global (via Grant No. N62909-23-1-2074).

Data availability .-The data that support the findings of this Letter are not publicly available. The data are available from the authors upon reasonable request.

- [∗ zhenglili@jhun.edu.cn](mailto:zhenglili@jhun.edu.cn)
- †
- [xinyoulu@hust.edu.cn](mailto:xinyoulu@hust.edu.cn)
- [1] H. J. Kimble, 'The quantum internet,' Nature 453 , 1023 (2008).
- [2] X. Lu, Q. Li, D. A. Westly, G. Moille, A. Singh, V. Anant, and K. Srinivasan, 'Chip-integrated visible-telecom entangled photon pair source for quantum communication,' Nature physics 15 , 373 (2019).
- [3] L. Zhou, Z. R. Gong, Y.-x. Liu, C. P. Sun, and F. Nori, 'Controllable Scattering of a Single Photon inside a OneDimensional Resonator Waveguide,' Phys. Rev. Lett. 101 , 100501 (2008).
- [4] E. Knill, R. Laflamme, and G. J. Milburn, 'A scheme for efficient quantum computation with linear optics,' Nature 409 , 46 (2001).
- [5] J. L. O'Brien, 'Optical Quantum Computing,' Science 318 , 1567 (2007).
- [6] P. Kok, W. J. Munro, K. Nemoto, T. C. Ralph, J. P. Dowling, and G. J. Milburn, 'Linear optical quantum computing with photonic qubits,' Reviews of Modern Physics 79 , 135 (2007).
- [7] I. Carusotto and C. Ciuti, 'Quantum fluids of light,' Reviews of Modern Physics 85 , 299 (2013).
- [8] D. Roy, C. M. Wilson, and O. Firstenberg, 'Colloquium: Strongly interacting photons in one-dimensional continuum,' Reviews of Modern Physics 89 , 021001 (2017).
- [9] K. M. Birnbaum, A. Boca, R. Miller, A. D. Boozer, T. E. Northup, and H. J. Kimble, 'Photon blockade in an optical cavity with one trapped atom,' Nature 436 , 87 (2005).

- [10] H. Walther, B. T. Varcoe, B.-G. Englert, and T. Becker, 'Cavity quantum electrodynamics,' Reports on Progress in Physics 69 , 1325 (2006).
- [11] N. Lambert, Y.-N. Chen, and F. Nori, 'Unified singlephoton and single-electron counting statistics: From cavity QED to electron transport,' Phys. Rev. A 82 , 063840 (2010).
- [12] A. Reiserer and G. Rempe, 'Cavity-based quantum networks with single atoms and optical photons,' Reviews of Modern Physics 87 , 1379 (2015).
- [13] D. Chang, J. Douglas, A. Gonz´ alez-Tudela, C.-L. Hung, and H. J. Kimble, ' Colloquium : Quantum matter built from nanoscopic lattices of atoms and photons,' Reviews of Modern Physics 90 , 031002 (2018).
- [14] M. Reitz, C. Sommer, and C. Genes, 'Cooperative Quantum Phenomena in Light-Matter Platforms,' PRX Quantum 3 , 010201 (2022).
- [15] A. S. Sheremet, M. I. Petrov, I. V. Iorsh, A. V. Poshakinskiy, and A. N. Poddubny, 'Waveguide quantum electrodynamics: Collective radiance and photon-photon correlations,' Reviews of Modern Physics 95 , 015002 (2023).
- [16] E. Vetsch, D. Reitz, G. Sagu´ e, R. Schmidt, S. T. Dawkins, and A. Rauschenbeutel, 'Optical Interface Created by Laser-Cooled Atoms Trapped in the Evanescent Field Surrounding an Optical Nanofiber,' Phys. Rev. Lett. 104 , 203603 (2010).
- [17] M. A. Versteegh, M. E. Reimer, K. D. J¨ ons, D. Dalacu, P. J. Poole, A. Gulinatti, A. Giudice, and V. Zwiller, 'Observation of strongly entangled photon pairs from a nanowire quantum dot,' Nature communications 5 , 5298 (2014).
- [18] S. Faez, P. T¨ urschmann, H. R. Haakh, S. G¨ otzinger, and V. Sandoghdar, 'Coherent Interaction of Light and Single Molecules in a Dielectric Nanoguide,' Phys. Rev. Lett. 113 , 213601 (2014).
- [19] A. Sipahigil, R. E. Evans, D. D. Sukachev, M. J. Burek, J. Borregaard, M. K. Bhaskar, C. T. Nguyen, J. L. Pacheco, H. A. Atikian, C. Meuwly, et al. , 'An integrated diamond nanophotonics platform for quantumoptical networks,' Science 354 , 847 (2016).
- [20] J. D. Brehm, A. N. Poddubny, A. Stehli, T. Wolz, H. Rotzinger, and A. V. Ustinov, 'Waveguide bandgap engineering with an array of superconducting qubits,' npj Quantum Materials 6 , 10 (2021).
- [21] L. Zhou, H. Dong, Y.-x. Liu, C. P. Sun, and F. Nori, 'Quantum supercavity with atomic mirrors,' Phys. Rev. A 78 , 063827 (2008).
- [22] J. R. Johansson, G. Johansson, C. M. Wilson, and F. Nori, 'Dynamical Casimir Effect in a Superconducting Coplanar Waveguide,' Phys. Rev. Lett. 103 , 147003 (2009).
- [23] J.-Q. Liao, Z. R. Gong, L. Zhou, Y.-x. Liu, C. P. Sun, and F. Nori, 'Controlling the transport of single photons by tuning the frequency of either one or two cavities in an array of coupled cavities,' Phys. Rev. A 81 , 042304 (2010).
- [24] T. Shi, D. E. Chang, and J. I. Cirac, 'Multiphotonscattering theory and generalized master equations,' Phys. Rev. A 92 , 053834 (2015).
- [25] A. S. Prasad, J. Hinney, S. Mahmoodian, K. Hammerer, S. Rind, P. Schneeweiss, A. S. Sørensen, J. Volz, and A. Rauschenbeutel, 'Correlating photons using the collective nonlinear response of atoms weakly coupled to an optical mode,' Nature Photonics 14 , 719 (2020).
- [26] H. Le Jeannic, A. Tiranov, J. Carolan, T. Ramos, Y. Wang, M. H. Appel, S. Scholz, A. D. Wieck, A. Ludwig, N. Rotenberg, et al. , 'Dynamical photon-photon interaction mediated by a quantum emitter,' Nature Physics 18 , 1191 (2022).
- [27] Z.-G. Lu, C. Shang, Y. Wu, and X.-Y. L¨ u, 'Analytical approach to higher-order correlation functions in U(1) symmetric systems,' Phys. Rev. A 108 , 053703 (2023).
- [28] M. Teˇ cer, M. Di Liberto, P. Silvi, S. Montangero, F. Romanato, and G. Calaj´ o, 'Strongly Interacting Photons in 2D Waveguide QED,' Phys. Rev. Lett. 132 , 163602 (2024).
- [29] E. Abrahams, P. W. Anderson, D. C. Licciardello, and T. V. Ramakrishnan, 'Scaling Theory of Localization: Absence of Quantum Diffusion in Two Dimensions,' Physical Review Letters 42 , 673 (1979).
- [30] F. Evers and A. D. Mirlin, 'Anderson transitions,' Reviews of Modern Physics 80 , 1355 (2008).
- [31] D. A. Abanin, E. Altman, I. Bloch, and M. Serbyn, ' Colloquium : Many-body localization, thermalization, and entanglement,' Reviews of Modern Physics 91 , 021001 (2019).
- [32] E. Akkermans, A. Gero, and R. Kaiser, 'Photon Localization and Dicke Superradiance in Atomic Gases,' Physical Review Letters 101 , 103602 (2008).
- [33] H. H. Jen, 'Disorder-assisted excitation localization in chirally coupled quantum emitters,' Physical Review A 102 , 043525 (2020).
- [34] N. Fayard, L. Henriet, A. Asenjo-Garcia, and D. E. Chang, 'Many-body localization in waveguide quantum electrodynamics,' Physical Review Research 3 , 033233 (2021).
- [35] C. Sommer, M. Reitz, F. Mineo, and C. Genes, 'Molecular polaritonics in dense mesoscopic disordered ensembles,' Physical Review Research 3 , 033141 (2021).
- [36] G. Fedorovich, D. Kornovan, A. Poddubny, and M. Petrov, 'Chirality-driven delocalization in disordered waveguide-coupled quantum arrays,' Physical Review A 106 , 043723 (2022).
- [37] N. Sauerwein, F. Orsi, P. Uhrich, S. Bandyopadhyay, F. Mattiotti, T. Cantat-Moltrecht, G. Pupillo, P. Hauke, and J.-P. Brantut, 'Engineering random spin models with atoms in a high-finesse cavity,' Nature Physics 19 , 1128 (2023).
- [38] V. Viggiano, R. Bachelard, F. D. Cunden, P. Facchi, R. Kaiser, S. Pascazio, and F. V. Pepe, 'Cooperative photon emission rates in random atomic clouds,' Physical Review A 108 , 063701 (2023).
- [39] M. Lei, R. Fukumori, J. Rochman, B. Zhu, M. Endres, J. Choi, and A. Faraon, 'Many-body cavity quantum electrodynamics with driven inhomogeneous emitters,' Nature 617 , 271 (2023).
- [40] F. Mattiotti, J. Dubail, D. Hagenm¨ uller, J. Schachenmayer, J.-P. Brantut, and G. Pupillo, 'Multifractality in the interacting disordered Tavis-Cummings model,' Physical Review B 109 , 064202 (2024).
- [41] N. O. Gjonbalaj, S. Ostermann, and S. F. Yelin, 'Modifying cooperative decay via disorder in atom arrays,' Physical Review A 109 , 013720 (2024).
- [42] A. Faraon, I. Fushman, D. Englund, N. Stoltz, P. Petroff, and J. Vuˇ ckovi´ c, 'Coherent generation of non-classical light on a chip via photon-induced tunnelling and blockade,' Nature Physics 4 , 859 (2008).
- [43] T. C. H. Liew and V. Savona, 'Single Photons from Cou-

pled Quantum Modes,' Phys. Rev. Lett. 104 , 183601 (2010).

- [44] C. Lang, D. Bozyigit, C. Eichler, L. Steffen, J. M. Fink, A. A. Abdumalikov, M. Baur, S. Filipp, M. P. da Silva, A. Blais, and A. Wallraff, 'Observation of Resonant Photon Blockade at Microwave Frequencies Using Correlation Function Measurements,' Phys. Rev. Lett. 106 , 243601 (2011).
- [45] J.-Q. Liao and F. Nori, 'Photon blockade in quadratically coupled optomechanical systems,' Phys. Rev. A 88 , 023853 (2013).
- [46] A. Miranowicz, J. c. v. Bajer, M. Paprzycka, Y.-x. Liu, A. M. Zagoskin, and F. Nori, 'State-dependent photon blockade via quantum-reservoir engineering,' Phys. Rev. A 90 , 033831 (2014).
- [47] H. Flayac and V. Savona, 'Unconventional photon blockade,' Phys. Rev. A 96 , 053810 (2017).
- [48] R. Huang, A. Miranowicz, J.-Q. Liao, F. Nori, and H. Jing, 'Nonreciprocal Photon Blockade,' Phys. Rev. Lett. 121 , 153601 (2018).
- [49] R. Huang, S ¸ K. ¨ ozdemir, J.-Q. Liao, F. Minganti, L.M. Kuang, F. Nori, and H. Jing, 'Exceptional Photon Blockade: Engineering Photon Blockade with Chiral Exceptional Points,' Laser &amp; Photonics Reviews 16 , 2100430 (2022).
- [50] Z.-G. Lu, Y. Wu, and X.-Y. L¨ u, 'Chiral Interaction Induced Near-Perfect Photon Blockade,' Phys. Rev. Lett. 134 , 013602 (2025).
- [51] See supplemental Material at URL, for the derivation of the second-order correlation function, the detailed calculation of the probabilibity density function, which includes Refs.[64,65].
- [52] D. A. Lidar, 'Lecture notes on the theory of open quantum systems,' arXiv preprint arXiv:1902.00967 (2019).
- [53] B. Kuyken, T. Ideguchi, S. Holzner, M. Yan, T. W. H¨ ansch, J. Van Campenhout, P. Verheyen, S. Coen, F. Leo, R. Baets, et al. , 'An octave-spanning midinfrared frequency comb generated in a silicon nanophotonic wire waveguide,' Nature communications 6 , 6310 (2015).
- [54] Z. Bao, Y. Li, Z. Wang, J. Wang, J. Yang, H. Xiong, Y. Song, Y. Wu, H. Zhang, and L. Duan, 'A cryogenic on-chip microwave pulse generator for large-scale superconducting quantum computing,' Nature Commu-

[nications 15 , 5958 (2024).](https://www.nature.com/articles/s41467-024-50333-w)

- [55] T. Caneva, M. T. Manzoni, T. Shi, J. S. Douglas, J. I. Cirac, and D. E. Chang, 'Quantum dynamics of propagating photons with strong interactions: a generalized input-output formalism,' New Journal of Physics 17 , 113001 (2015).
- [56] H. Zheng and H. U. Baranger, 'Persistent Quantum Beats and Long-Distance Entanglement from WaveguideMediated Interactions,' Phys. Rev. Lett. 110 , 113601 (2013).
- [57] Y.-L. L. Fang, H. Zheng, and H. U. Baranger, 'One-dimensional waveguide coupled to multiple qubits: photon-photon correlations,' EPJ Quantum Technology 1 , 1 (2014).
- [58] Y.-L. L. Fang and H. U. Baranger, 'Waveguide QED: Power spectra and correlations of two photons scattered off multiple distant qubits and a mirror,' Phys. Rev. A 91 , 053845 (2015).
- [59] Y.-L. L. Fang, F. Ciccarello, and H. U. Baranger, 'NonMarkovian dynamics of a qubit due to single-photon scattering in a waveguide,' New Journal of Physics 20 , 043035 (2018).
- [60] P. R. Berman, 'Theory of two atoms in a chiral waveguide,' Phys. Rev. A 101 , 013830 (2020).
- [61] S. Mahmoodian, M. ˇ Cepulkovskis, S. Das, P. Lodahl, K. Hammerer, and A. S. Sørensen, 'Strongly Correlated Photon Transport in Waveguide Quantum Electrodynamics with Weakly Coupled Emitters,' Phys. Rev. Lett. 121 , 143601 (2018).
- [62] D. E. Chang, L. Jiang, A. Gorshkov, and H. J. Kimble, 'Cavity QED with atomic mirrors,' New Journal of Physics 14 , 063003 (2012).
- [63] L. Leonforte, A. Carollo, and F. Ciccarello, 'Vacancylike Dressed States in Topological Waveguide QED,' Phys. Rev. Lett. 126 , 063601 (2021).
- [64] A. Asenjo-Garcia, M. Moreno-Cardoner, A. Albrecht, H. J. Kimble, and D. E. Chang, 'Exponential Improvement in Photon Storage Fidelities Using Subradiance and 'Selective Radiance' in Atomic Arrays,' Physical Review X 7 , 031024 (2017).
- [65] Y. Wang, W. Verstraelen, B. Zhang, T. C. H. Liew, and Y. D. Chong, 'Giant Enhancement of Unconventional Photon Blockade in a Dimer Chain,' Phys. Rev. Lett. 127 , 240402 (2021).

## Supplemental Material for

## 'Disorder-Induced Strongly Correlated Photons in Waveguide QED'

This supplemental materials contain eight parts: I. A detailed derivation of the second-order equal-time correlation function; II. Analytical calculations of the probability of photon antibunching (PA) and perfect photon blockade (PPB) for few-qubit systems; III. The physical mechanism of nearly perfect photon blockade (NPPB); IV. Correlation functions in weak- and strong-disorder limit; V. Effects of losses on non-waveguide modes; VI. Effects of chirality in coupling to waveguide modes; VII. Effects of finite bandwidth of input state; VIII. The details of numerical method used in this work.

## CONTENTS

| I.                                                                              |   Derivation of second-order correlation function 2 |
|---------------------------------------------------------------------------------|-----------------------------------------------------|
| II. Analytical Calculations of P ( s < 1) and P (0) for few-qubit systems.      |                                                   4 |
| A. Transmission                                                                 |                                                   5 |
| B. Reflection                                                                   |                                                   5 |
| III. Physical mechanism of NPPB                                                 |                                                   7 |
| IV. Correlation function in the weak- and strong-disorder limits                |                                                  10 |
| A. Weak-disorder limit ( W ≪ 1)                                                 |                                                  10 |
| B. Strong-disorder limit ( W ≫ 1)                                               |                                                  10 |
| V. Effects of losses on non-waveguide modes                                     |                                                  13 |
| A. Transmission output                                                          |                                                  13 |
| B. Reflection                                                                   |                                                  14 |
| VI. Effects of chirality in coupling to waveguide modes                         |                                                  14 |
| VII. Effects of finite bandwidth of input state                                 |                                                  15 |
| VIII. Numerical calculations of P ( s < 1) and P ( s ≪ 1) for many-qubit system |                                                  18 |
| A. Calculation about P ( s < 1)                                                 |                                                  18 |
| B. Calculation about P ( s ≪ 1)                                                 |                                                  19 |
| References                                                                      |                                                  19 |

## I. DERIVATION OF SECOND-ORDER CORRELATION FUNCTION

In this section, we present the Gorini-Kossakowski-Sudarshan-Lindblad master equation for our setup and, by incorporating the input-output formalism, derive the formal expressions for the correlation functions in the transmission and reflection outputs. To this end, we consider a one-dimensional array of N qubits coupled to a single optical waveguide bath. Under the rotating-wave approximation, the time evolution of the system is governed by the Hamiltonian

$$H = \sum _ { m = 1 } ^ { N } \omega _ { m } \sigma _ { m } ^ { \dagger } \sigma _ { m } + \sum _ { \mu = R , T } \int _ { - \infty } ^ { \infty } d \omega \, \omega a _ { \mu } ^ { \dagger } ( \omega ) a _ { \mu } ( \omega ) + \sum _ { m , \mu } \int _ { - \infty } ^ { \infty } d \omega \, \left ( \kappa _ { m , \mu } ( \omega ) a _ { \mu } ^ { \dagger } ( \omega ) \sigma _ { m } + h . c . \right ) .$$

Here, ω m = ω 0 +∆ m denotes the transition frequency of the m th qubit, and σ m = | g m ⟩⟨ e m | is its corresponding lowering operator. The operator a µ ( ω ) is the boson annihilation operator for a bath mode with frequency ω , where the subscript µ = T (transmission) or R (reflection) distinguishes the mode. We assume weak inhomogeneity, namely, | ∆ m |≪ ω 0 . In this regime, the coupling strengths satisfy κ m, T / R ( ω ) = g m,, T / R exp(( -/ +) iωx m /c ) ≈ g T / R exp(( -/ +) iωx m /c ), so that the interaction strength for each qubit is approximately homogeneous, i.e., | κ m, T / R ( ω ) | ≈ g T / R . The qubits are assumed to be equally spaced with separation d , so that x m = md . For simplicity, we set v g = 1.

We first derive the master equation describing the time evolution of the system, which further supports the calculation of the field correlation function. The derivations mainly follow those in [1, 2, 64]. Following standard derivations, the Heisenberg equation for the field operator are obtained as

$$\dot { a } _ { T } ( \omega , t ) = - i \omega a _ { T } ( \omega , t ) - i g _ { T } e ^ { - i \omega x _ { m } } \sigma _ { m } ( t ) , \quad \dot { a } _ { R } ( \omega , t ) = - i \omega a _ { R } ( \omega , t ) - i g _ { R } e ^ { i \omega x _ { m } } \sigma _ { m } ( t ) ,$$

which can be formally integrated as

$$a _ { T } ( \omega , t ) & = e ^ { - i \omega ( t - t _ { 0 } ) } a _ { T } ( \omega , t _ { 0 } ) - i g _ { T } \sum _ { m } \int _ { t _ { 0 } } ^ { t } e ^ { - i \omega ( t - \tau ) - i \omega x _ { m } } \sigma _ { m } ( \tau ) \, d \tau \, , \ a _ { R } ( \omega , t ) = - i g _ { R } \sum _ { m } \int _ { t _ { 0 } } ^ { t } e ^ { - i \omega ( t - \tau ) + i \omega x _ { m } } \sigma _ { m } ( \tau ) \, d \tau \, , \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & & \\ & & \\ & & \\ & & & \\ & & & & \\ & & & & \\ & & & & & \\ & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & &$$

where we have assumed that photons are injected from the left side of the waveguide, such that a R ( ω, t 0 ) = 0. Consequently, the Heisenberg equations for the atomic operator are given by

$$\dot { \sigma } _ { m } ( t ) = - i \omega _ { m } \sigma _ { m } ( t ) - i \sigma _ { m } ^ { z } ( \int \nolimits _ { - \infty } ^ { \infty } g _ { T } a _ { T } ( \omega , t ) e ^ { i \omega x _ { m } } \, d \omega + \int \nolimits _ { - \infty } ^ { \infty } g _ { R } a _ { R } ( \omega , t ) e ^ { - i \omega x _ { m } } \, d \omega ) .$$

Substituting the solutions of the field operators into the equations for the atomic operator, we have

$$\text {Substituting the solutions of the field operators into the equations for the atomic operator, we have} \\ & \dot { \sigma } _ { m } ( t ) = - i \omega \sigma _ { m } ( t ) - i \sigma _ { m } ^ { z } ( t ) \left ( g _ { T } \int _ { - \infty } ^ { \infty } e ^ { - i \omega ( t - t _ { 0 } ) + i \omega x _ { m } } a _ { T } ( \omega , t _ { 0 } ) \, d \omega \\ & - i g _ { T } ^ { 2 } 2 \pi \sum _ { n } \Theta ( x _ { m } - x _ { n } ) \sigma _ { n } ( t - | x _ { m } - x _ { n } | ) - i g _ { R } ^ { 2 } 2 \pi \sum _ { n } \Theta ( x _ { n } - x _ { m } ) \sigma _ { n } ( t - | x _ { m } - x _ { n } | ) \right ) \\ & \approx - i \omega \sigma _ { m } ( t ) - i \sigma _ { m } ^ { z } ( t ) \left ( g _ { T } \int _ { - \infty } ^ { \infty } e ^ { - i \omega ( t - t _ { 0 } ) + i \omega x _ { m } } a _ { T } ( \omega , t _ { 0 } ) \, d \omega \\ & - i g _ { T } ^ { 2 } 2 \pi \sum _ { n } \Theta ( x _ { m } - x _ { n } ) \sigma _ { n } ( t ) e ^ { i \omega _ { 0 } | x _ { m } - x _ { n } | } - i g _ { R } ^ { 2 } 2 \pi \sum _ { n } \Theta ( x _ { n } - x _ { m } ) e ^ { i \omega _ { 0 } | x _ { m } - x _ { n } | } \sigma _ { n } ( t ) \right ) . \\ \intertext { In the last line, we have used the Markovian approximation }$$

In the last line, we have used the Markovian approximation

$$\sigma _ { n } ( t - | x _ { m } - x _ { n } | / c ) \approx \sigma _ { n } ( t ) e ^ { i \omega _ { n } | x _ { m } - x _ { n } | / c } = \sigma _ { n } ( t ) e ^ { i \omega _ { 0 } ( 1 + \Delta _ { n } / \omega _ { 0 } ) | m - n | d / c } ,$$

and, for our purposes, we neglect the dependence of ∆ n in the phase factor, i.e.,

$$\sigma _ { n } ( t ) e ^ { i \omega _ { n } | x _ { m } - x _ { n } | / c } \approx \sigma _ { n } ( t ) e ^ { i \omega _ { 0 } | m - n | d / c } .$$

This approximation is valid when the condition | ∆ n | /ω 0 ≪ N -1 holds. Equivalently, this condition is satisfied if C W ≪ ω 0 /N , where C ∼ O (1) is a dimensionless constant. Specifically, for a detuning ∆ n drawn from a normal distribution with standard deviation W , the inequality | ∆ n | ≤ C W is met with probability erf( C / √ 2). For instance, taking C = 2 yields erf( C / √ 2) ≈ 0 . 95, implying that the condition | ∆ n | ≤ C W is satisfies with near-unit probability. Thus, the approximation | ∆ n | /ω 0 ≪ N -1 holds with probability near unit (0.95), provided that C W ≪ ω 0 /N is met. Integrating the bath degrees of freedom, we have

$$\dot { \sigma } _ { m } ( t ) & = - i \omega _ { m } \sigma _ { m } ( t ) - i \sqrt { \gamma } \Gamma _ { m } ^ { z } ( t ) f ( t - t _ { 0 } , x _ { m } ) \\ & - \gamma _ { T } \sigma _ { m } ^ { z } ( t ) \sum _ { n } \sigma _ { n } ( t ) \Theta ( x _ { m } - x _ { n } ) e ^ { i \omega _ { 0 } | x _ { m } - x _ { n } | } - \gamma _ { R } \sigma _ { m } ^ { z } ( t ) \sum _ { n } \sigma _ { n } ( t ) \Theta ( x _ { n } - x _ { m } ) e ^ { i \omega _ { 0 } | x _ { m } - x _ { n } | } ,$$

where γ T / R = 2 π g 2 T / R and f ( τ, z ) is defined by

$$f ( \tau , z ) = \frac { 1 } { \sqrt { 2 \pi } } \int _ { - \infty } ^ { \infty } e ^ { - i \omega ( \tau - z ) } \, \text {Tr} \left [ \rho _ { E } ( t _ { 0 } ) a _ { T } ( \omega , t _ { 0 } ) \right ] \mathrm d \omega \, .$$

Eq. (I) coincides with the equation of motion governed by the master equation

$$\dot { \rho } = - i ( ( H _ { \text {eff} } + H _ { d } ) \rho - \rho ( H _ { \text {eff} } ^ { \dagger } + H _ { d } ) ) + \sum _ { m n } 2 ( \gamma _ { \text {T} } \Theta ( m - n ) \cos ( | m - n | \varphi ) + \gamma _ { R } \Theta ( n - m ) \cos ( | m - n | \varphi ) ) \sigma _ { m } \rho \sigma _ { n } ^ { \dagger } , \, ( S 8 )$$

with

$$H _ { e f f } = \sum _ { m = 1 } ^ { N } \left ( \Delta _ { m } - \frac { i ( \gamma _ { n w } + \gamma _ { T } + \gamma _ { R } ) } { 2 } \right ) \sigma _ { m } ^ { \dagger } \sigma _ { m } - i \sum _ { m > n } ^ { N } \left ( \gamma _ { T } e ^ { i | m - n | \varphi } \sigma _ { m } ^ { \dagger } \sigma _ { n } + \gamma _ { R } e ^ { i | m - n | \varphi } \sigma _ { n } ^ { \dagger } \sigma _ { m } \right ) ,$$

and

where φ = ω 0 d/v g .

The zero-time second-order photon correlations of the emitted field are defined as

$$g _ { \mu } = \frac { \langle a _ { \mu , o u t } ^ { \dagger } ( t ) a _ { \mu , o u t } ^ { \dagger } ( t ) a _ { \mu , o u t } ( t ) a _ { \mu , o u t } ( t ) \rangle } { \langle a _ { \mu , o u t } ^ { \dagger } ( t ) a _ { \mu , o u t } ( t ) \rangle ^ { 2 } } ,$$

where ⟨·⟩ denotes the expectation value over the emitted field. The input-output relations are given by

$$a _ { T , o u t } ( t ) = a _ { T , i n } ( t ) - i \sqrt { \gamma _ { T } } \sum _ { m } e ^ { - i m \varphi } \sigma _ { m } ( t ) , \quad a _ { R , o u t } ( t ) = - i \sqrt { \gamma _ { R } } \sum _ { m } e ^ { i m \varphi } \sigma _ { m } ( t ) ,$$

with

$$a _ { T , i n } ( t ) = \frac { 1 } { \sqrt { 2 \pi } } \int _ { - \infty } ^ { \infty } e ^ { - i \omega ( t - t _ { 0 } ) } a _ { T } ( \omega , t _ { 0 } ) \, d \omega \, .$$

Let us now consider a right-propagating coherent pulse as an input (drive), given by ρ E ( t 0 ) ∝ exp( αa † T ( ω in ) -αa T ( ω in )) | 0 ⟩ , where the input pulse is assumed to be resonant with the transition frequency for the ordered system, i.e., ω in = ω 0 . In the long-time limit, the properties of the emitted field are fully determined by the steady state ρ ss of the qubits (in the rotating frame with respect to H 0 = ω 0 ∑ m σ † σ m ). By substituting the input-output relations into the definition of g µ , one obtains

$$g _ { \mu } = \frac { \text {Tr} ( \rho _ { s s } C _ { \mu } ^ { \dagger } C _ { \mu } ^ { \dagger } C _ { \mu } C _ { \mu } ) } { \text {Tr} \left ( \rho _ { s s } C _ { \mu } ^ { \dagger } C _ { \mu } \right ) ^ { 2 } } ,$$

where C R = -i √ γ R ∑ m e iφm σ m and C T = α -i √ γ T ∑ m e -iφm σ m , ρ ss denotes the steady state corresponding to the master equation Eq. (S8) with f ( t -t 0 , x m ) = αe -iω 0 ( t -t 0 ) e imφ . In the weak-input limit ( α ≪ 1), one can solve for ρ ss by neglecting quantum jumps, which yields the expansion ρ ss ≈ | G ⟩ + α | ψ 1 ⟩ + α 2 | ψ 2 ⟩ + O ( α 3 ) [4]. Here, | G ⟩ = ⊗ N m =1 | g m ⟩ , | ψ 1 ⟩ = -( H (1) eff ) -1 H + | G ⟩ and | ψ 2 ⟩ = -( H (2) eff ) -1 H + | ψ 1 ⟩ are the single- and two-excitation

$$H _ { d } = \sum _ { m } \sqrt { \gamma _ { T } } ( f ( t - t _ { 0 } , m d ) \sigma _ { m } ^ { \dagger } + h . c . ) ,$$

FIG. S1. (a) Probability of PA versus φ and W , where φ ranges from 0 . 001 π to 0 . 05 π . (b) Probability of PA versus φ and W , where φ ranges from 2 . 001 π to 2 . 05 π

<!-- image -->

.

components of the truncated steady-state, respectively, with H + = √ γ T ∑ m e imφ σ † m . The operators H (1) eff and H (2) eff denote the single- and two-excitation subspace of the effective Hamiltonian H eff , respectively. After some calculations, one obtains for the transmitted field

$$g _ { T } = \frac { | 1 - 2 i \langle G | \tilde { C } _ { T } | \psi ^ { 1 } \rangle - \langle G | \tilde { C } _ { T } \tilde { C } _ { T } | \psi ^ { 2 } \rangle | ^ { 2 } } { | 1 - i \langle G | \tilde { C } _ { T } | \psi ^ { 1 } \rangle | ^ { 4 } } + \mathcal { O } ( | \alpha | ^ { 2 } ) ,$$

$$g _ { R } = \frac { \langle \psi ^ { 2 } | ( \tilde { C } _ { R } ^ { \dagger } ) ^ { 2 } ( \tilde { C } _ { R } ) ^ { 2 } | \psi ^ { 2 } \rangle } { \langle \psi ^ { 1 } | \tilde { C } _ { R } ^ { \dagger } \tilde { C } _ { R } | \psi ^ { 1 } \rangle ^ { 2 } } + \mathcal { O } ( | \alpha | ^ { 2 } ) ,$$

where ˜ C T = √ γ T ∑ m e -iφm σ m and ˜ C R = √ γ R ∑ m e iφm σ m . These expressions can be further simplified as

$$g _ { T } = \frac { | 1 - 2 i \langle \phi _ { + } ^ { 1 } | \psi ^ { 1 } \rangle - \langle \phi _ { + } ^ { 2 } | \psi ^ { 2 } \rangle | ^ { 2 } } { | 1 - i \langle \phi _ { + } ^ { 1 } | \psi ^ { 1 } \rangle | ^ { 4 } } ,$$

$$g _ { R } = \frac { | \langle \phi _ { - } ^ { 2 } | \psi ^ { 2 } \rangle | ^ { 2 } } { | \langle \phi _ { - } ^ { 1 } | \psi ^ { 1 } \rangle | ^ { 4 } } ,$$

where | ϕ 1 ± ⟩ = √ γ T ∑ m exp( ± imφ ) σ † m | G ⟩ and | ϕ 2 ± ⟩ = 2 γ T ∑ m&gt;n exp( ± i ( m + n ) φ ) σ † m σ † n | G ⟩ . When the coupling strengths to left- and right-going modes are homogeneous, i.e., γ T = γ R = γ/ 2, these equations, Eqs. (S17,S18), recover Eq. (2) of the main text.

We also emphasize the periodic nature of all the above derivations, including the master equation and the inputoutput relations, in the phase φ . Consequently, photon correlation should also be periodic in φ , with a period of 2 π . Likewise, all the statistic quantities studied in the main text, such as the probability of PA and the probability density function, are also periodic in φ with period of 2 π . For example, the probability of PA in the transmission for N = 10 (the inset of Fig. 2(a) in the main text) with φ/π ∈ (0 . 001 , 0 . 05), and that with φ/π ∈ (2 . 001 , 2 . 05), are shown in Fig. S1. The results show good agreements with each other.

## II. ANALYTICAL CALCULATIONS OF P ( s &lt; 1) AND P (0) FOR FEW-QUBIT SYSTEMS.

̸

In this section, we present detailed calculations for the probabilities of PA and PPB for few-qubit systems, which further substantiate the results reported in the main text. The calculations for the transmission output and for the reflection output with φ = 0 are carried out analytically, whereas those for the reflection output with φ = 0 are performed numerically.

and for the reflected field

and For s ≥ 1, the PDF is given by

## A. Transmission

We first consider the single-qubit case. In this system, all two-photon scattering processes vanish, meaning that any terms involving | ψ 2 ⟩ (or ⟨ ψ 2 | ) drop out. Since H (1) eff is a 1 × 1 matrix in this case, the evaluation of | ψ 1 ⟩ is straightforward. After some algebraic manipulations, the second-order correlation function is given by

$$g _ { T } = \frac { ( 1 + 4 \Delta _ { 1 } ^ { 2 } ) ^ { 2 } } { 1 6 \Delta _ { 1 } ^ { 2 } } .$$

Moreover, an analytical expression for the probability density function (PDF) corresponding to Eq. (S19) can be obtained. Specifically, the PDF is calculated as

$$P ( s ) = \frac { 1 } { \sqrt { 2 \pi } W } \int _ { - \infty } ^ { \infty } \delta \left ( \frac { ( 1 + 4 \Delta _ { 1 } ^ { 2 } ) ^ { 2 } } { 1 6 \Delta _ { 1 } ^ { 4 } } - s \right ) e ^ { - \Delta _ { 1 } ^ { 2 } / 2 W ^ { 2 } } \, d \Delta _ { 1 } .$$

Here, the Dirac delta function is handled using the standard identity δ ( f ( x )) = ∑ j δ ( x -x j ) / | f ′ ( x j ) | . After some calculations, one finds that P ( s ) = 0 for s &lt; 1. Thus, we have

$$\mathbb { P } ( s < 1 ) = P ( 0 ) = 0 .$$

$$P ( s ) = \frac { 1 } { 4 \sqrt { 2 \pi } W } \frac { 1 } { ( \sqrt { s } - 1 ) ^ { 3 / 2 } \sqrt { s } } e ^ { 1 / ( 1 - 1 \sqrt { s } ) 8 W ^ { 2 } } .$$

The asymptotic behaviors for P ( s &gt; 1) are

$$P ( s \to 1 ^ { + } ) \sim \frac { 1 } { 4 \pi W } ( s - 1 ) ^ { - 3 / 2 } e ^ { - 1 / ( 4 W ^ { 2 } ( s - 1 ) ) } , \quad P ( s \to + \infty ) \sim \frac { 1 } { 4 \sqrt { 2 } \pi W } s ^ { - 5 / 4 } .$$

Furthermore, the mode of the PDF, corresponding to the most probable value of the correlation function, is located at

$$s _ { \max } = \frac { 1 + 5 6 W ^ { 2 } + 4 6 W ^ { 4 } + \sqrt { W ^ { 8 } ( 1 + 2 8 W ^ { 2 } ) ^ { 2 } ( 1 + 5 6 W ^ { 2 } + 4 6 W ^ { 4 } ) } } { 8 0 0 W ^ { 4 } } , \\$$

This result shows that the mode scales as s max ∼ W -4 for W → 0 + and s max ∼ 1 for W → + ∞ . In other words, when W ≪ 1 the most probable output is strongly bunched, while for W ≫ 1 it is nearly coherent.

For a two-qubit system, although the analytical expression become more involved, the calculation remains tractable. In this case, the correlation function is given by

$$g _ { T } = \frac { ( 8 \Delta _ { 1 } ^ { 2 } \Delta _ { 2 } ^ { 2 } + f _ { + } - \cos ( 2 \varphi ) ) ( 8 \Delta _ { 1 } ^ { 2 } \Delta _ { 2 } ^ { 2 } ( 1 + ( \Delta _ { 1 } + \Delta _ { 2 } ) ^ { 2 } ) + ( \Delta _ { 1 } + \Delta _ { 2 } ) ^ { 2 } ( f _ { - } - \cos ( \varphi ) ) + 4 \Delta _ { 1 } \Delta _ { 2 } ( \Delta _ { 1 } + \Delta _ { 2 } ) \sin ( 2 \varphi ) ) } { 6 4 \Delta _ { 1 } ^ { 4 } \Delta _ { 2 } ^ { 4 } ( 1 + ( \Delta _ { 1 } + \Delta _ { 2 } ) ^ { 2 } ) } ,$$

with f ± = 1 + 2∆ 2 1 +2∆ 2 2 ± 4∆ 1 ∆ 2 cos(2 φ ) -2(∆ 1 +∆ 2 ) sin(2 φ ). It is practically infeasible to derive a closed-form expression for the corresponding PDF in this case. Nonetheless, since the correlation function g T ≥ 1, we have P ( s &lt; 1) = 0 and P (0) = 0.

## B. Reflection

For the single-qubit system, the absence of two-photon scattering processes implies that ⟨ ϕ 2 -| ψ 2 ⟩ = 0, so that g R = 0. For the two-qubit system, we first consider the case φ = 0. In this situation, the correlation function reduces to

$$g _ { R } = \frac { ( \Delta _ { 1 } + \Delta _ { 2 } ) ^ { 2 } + 4 \Delta _ { 1 } ^ { 2 } \Delta _ { 2 } ^ { 2 } } { ( \Delta _ { 1 } + \Delta _ { 2 } ) ^ { 2 } + ( \Delta _ { 1 } + \Delta _ { 2 } ) ^ { 4 } } .$$

The probability of PA is then calculated from

$$\mathbb { P } ( s < 1 ) = \int _ { 0 } ^ { 1 } P ( s ) d s = \frac { 1 } { 2 \pi W ^ { 2 } } \int _ { - \infty } ^ { \infty } \mathrm d \Delta _ { 1 } \int _ { - \infty } ^ { \infty } \mathrm d \Delta _ { 2 } \ \exp \left ( - \frac { \Delta _ { 1 } ^ { 2 } + \Delta _ { 2 } ^ { 2 } } { 2 W ^ { 2 } } \right ) \Theta ( g _ { R } - 1 ) ,$$

where Θ( x ) denotes the Heaviside step function. Changing the variables as 2Ω = ∆ 1 +∆ 2 and 2Λ = ∆ 1 -∆ 2 , one obtains g R = (Ω 2 +(Ω 2 -Λ 2 ) 2 ) / (Ω 2 +4Ω 4 ). PA occurs when

$$| \Omega | > \frac { 1 } { \sqrt { 3 } } | \Lambda | .$$

It follows that the probability of PA is given by

$$\mathbb { P } ( s < 1 ) = \frac { 1 } { \pi W ^ { 2 } } \iint _ { | \Omega | > \frac { | \Lambda | } { \sqrt { 3 } } } \, d \Omega d \Lambda \, \exp \left ( - \frac { \Omega ^ { 2 } + \Lambda ^ { 2 } } { W ^ { 2 } } \right ) = \frac { 2 } { 3 } ,$$

which recovers the equality stated in Eq.(4) of the main text. To demonstrate the result P (0) = 0 presented in the main text, we now analyze the asymptotic behavior of P ( s ) for s ≪ 1. Starting from

$$P ( s ) = \frac { 4 } { \pi W ^ { 2 } } \int _ { 0 } ^ { \infty } d \Omega \int _ { 0 } ^ { \infty } d \Lambda \, \exp \left ( - \frac { \Omega ^ { 2 } + \Lambda ^ { 2 } } { W ^ { 2 } } \right ) \delta \left ( \frac { \Omega ^ { 2 } + ( \Omega ^ { 2 } - \Lambda ^ { 2 } ) ^ { 2 } } { \Omega ^ { 2 } + 4 \Omega ^ { 4 } } - s \right ) .$$

a change of variables Ω 2 → Ω and Λ 2 → Λ yields

$$P ( s ) = \frac { 1 } { \pi W ^ { 2 } } \int _ { 0 } ^ { \infty } d \Omega \int _ { 0 } ^ { \infty } d \Lambda \, \frac { 1 } { \sqrt { \Omega \Lambda } } \exp \left ( - \frac { \Omega + \Lambda } { W ^ { 2 } } \right ) \delta \left ( \frac { \Omega + ( \Omega - \Lambda ) ^ { 2 } } { \Omega + 4 \Omega ^ { 2 } } - s \right ) .$$

Carrying out the integral over Λ leads to

$$P ( s ) = \frac { 1 } { \pi W ^ { 2 } } \int _ { ( 1 - s ) / 4 s } ^ { \infty } d \Omega \, \exp ( - \Omega / W ^ { 2 } ) \, \frac { ( 1 + 4 \Omega ) } { \sqrt { 4 s \Omega + s - 1 } } \left [ \frac { \exp \left ( \frac { - \Omega _ { + } } { W ^ { 2 } } \right ) } { \sqrt { \Omega _ { + } } } + \frac { \exp \left ( \frac { - \Omega _ { - } } { W ^ { 2 } } \right ) } { \sqrt { \Omega _ { - } } } \right ] ,$$

where Ω ± = Ω ± √ Ω(4 s Ω+ s -1). In the limit s ≪ 1, the lower limit of the Ω integral can be approximated as (1 -s ) / 4 s ≈ 1 / 4 s . In this regime, one can approximate Ω ± ≈ Ω and √ 4 s Ω+ s -1 ≈ √ 4 s Ω -1. With these approximations, the expression simplifies to

$$P ( s ) \approx \frac { 2 } { \pi W ^ { 2 } \sqrt { s } } \int _ { 1 / 4 s } ^ { \infty } \text {d} \Omega \ e ^ { - 2 \Omega / W ^ { 2 } } \frac { 1 } { \sqrt { 4 s \Omega - 1 } } .$$

This asymptotic form reveals that strong photon antibunching ( g R ≪ 1) is associated with large detuning, as dictated by the lower integration bound Ω = ∆ 1 +∆ 2 &gt; 1 / 4 s ∼ s -1 . Performing the integral over Ω yields

$$P ( s \ll 1 ) \sim \frac { 1 } { \sqrt { 2 \pi } W } s ^ { - 1 } \exp \left ( - \frac { 1 } { 2 W ^ { 2 } s } \right ) .$$

From this expression it is evident that as s → 0, P ( s ) → 0; hence, P (0) = 0, in agreement with the result stated in the main text. Finally, we compare this analytical approximation to numerical integration of the starting expression (Eq. (S30)) [see Figs. S2(a-c)].

̸

For the system with φ = 0, the correlation function is given by

$$g _ { R } = \left | \frac { ( - i + i e ^ { 2 i \varphi } + 2 \Delta _ { 1 } + 2 \Delta _ { 2 } ) ( e ^ { 2 i \varphi } + ( 2 \Delta _ { 1 } - i ) ( 2 \Delta _ { 2 } - i ) ) } { ( \Delta _ { 1 } + \Delta _ { 2 } - i ) ( 2 \Delta _ { 2 } - i + e ^ { 2 i \varphi } ( 2 \Delta _ { 1 } + i ) ) ^ { 2 } } \right | ^ { 2 } .$$

In this case, the analytical forms for both P ( s &lt; 1) and P (0) are practically infeasible to obtain. Fig. S2(g) displays the numerical results for P ( s &lt; 1), which now depend on both the phase and the disorder strength. Notably, the numerical data imply that P ( s &lt; 1) is bounded from below by 2 / 3, the value obtained in the Dicke limit for a twoqubit system. As the disorder strength increases, P ( s &lt; 1) attains a maximum at φ ∼ 0 . 25 π , and then saturates to the lower bound of 2 / 3 when φ ∼ 0 or 0 . 5 π .

FIG. S2. (a-c) The asymptotic behaviors of P ( s ). The chosen disorder strengths are W = 0 . 1 (a), W = 1 (b), and W = 10 (c). In all plots, red dots are obtained from the numerical integration of Eq. (S30), and black lines represent the analytical solutions from Eq. (S34). (d-f) The asymptotic behaviors of P ( s ). The chosen disorder strengths are W = 0 . 1 (d), W = 1 (e), and W = 10 (f). The different symbols correspond to systems with different values of φ . In all plots, the symbols are obtained from the numerical integration with the correlation expression replaced by Eq. (S35), and black lines represent the analytical solutions from Eq. (S34). (g) ˜ P ( s &lt; 1) = P ( s &lt; 1) -2 / 3 versus phase and disorder strength. The result is obtained from numerical integration of Eq. (S27), while the expression of correlation is replaced by Eq. (S35)

<!-- image -->

.

TABLE S1. Partial solutions { ∆ 1 , ∆ 2 , ∆ 3 } of equation g T = s 0 with s 0 = 10 -8 , 10 -10 , 10 -12 . Here φ = 0 . 04 π , which is the same with the parameters in Fig. 1(c) of main text.

| g T     | ∆ 1                 | ∆ 2                   | ∆ 3                 |
|---------|---------------------|-----------------------|---------------------|
| 10 - 8  | 0 . 149124450372206 | - 0 . 053903424589490 | 0 . 144085703957167 |
| 10 - 10 | 0 . 148134188883455 | - 0 . 055253952848190 | 0 . 144762975264912 |
| 10 - 12 | 0 . 149005562567387 | - 0 . 054129160721382 | 0 . 144182673551411 |

̸

Regarding P (0), Figs. S2(d-f) illustrate the asymptotic behavior of P ( s ) for s ≪ 1. It is evident that P ( s ≪ 1) displays essentially the same asymptotic form as in the case of φ = 0. This similarity arises because strong PA is primarily associated with samples { ∆ 1 , ∆ 2 } in which one detuning | ∆ i | ≪ 1 (i.e., nearly resonant), while the other | ∆ j = i | ≫ 1 (i.e., far off-resonant). Physically, this scenario corresponds to one qubit interacting strongly with the input while the other is nearly transparent to it, effectively reducing the system to a single-photon absorber/emitter. However, since the detunings are sampled from a Gaussian distribution, the probability of obtaining | ∆ j = i | ≫ 1 decreases exponentially with | ∆ j = i | , which ultimately leads to an exponential decay of P ( s ) as s → 0. Consequently, P (0) = 0 is recovered in this regime.

̸

̸

These findings demonstrate that, even when φ = 0, the essential asymptotic behavior of the correlation function remains consistent with the φ = 0 case, while the overall probability P ( s &lt; 1) exhibits a nontrivial dependence on both the phase and the disorder strength.

## III. PHYSICAL MECHANISM OF NPPB

Although the solutions presented in the main text correspond to g T = 10 -10 , one can also obtain solutions for g T = ϵ , where ϵ can be made arbitrarily close to 0 as computational precision increases. To achieve an NPPB event, i.e., g T / R = ϵ → 0, the detunings of the qubits must be very finely tuned (see Table. S1 for an example). This requirement for fine-tuning of parameters for an NPPB event suggests that the underlying physical mechanism is the destructive interference of quantum paths [5, 6].

̸

FIG. S3. (a-b) Schematics of single-photon scattering path involves (a) non-interacting path (b) interacting path for an array with N = 3.

<!-- image -->

FIG. S4. (a-c) Top: PDFs; Bottom: Solutions of g T = 10 -10 for the transmission output. The chosen parameters are φ = 0 . 01 π and W = 0 . 15; the chain sizes are indicated above the plots. (d-f) Top: PDFs; Bottom: Solutions of g R = 10 -10 for the reflection output. The chosen system parameters are φ = 0 . 5 π and W = 1; the chain sizes are indicated above the plots. In the top of (a-f), the results are obtained from 10 9 disorder realizations. (g-h) PDFs for the transmission (g) and reflection (h) outputs under different numbers of disorder realizations. The chosen parameters are N = 3, φ = 0 . 01 π , W = 0 . 15 in (g) and N = 3, φ = 0 . 5 π , W = 1 in (h).

<!-- image -->

To manifest the interference effect, note that the photon correlations depend solely on the single- and two-photon scattering processes. Consequently, the overall quantum path comprises three contributions: (i) a single-photon scattering path with probability amplitude ⟨ ϕ 1 ± | ψ 1 ⟩ ; (ii) a two-photon scattering path with probability amplitude ⟨ ϕ 2 ± | ψ 2 ⟩ ; (iii) a free propagation path with probability amplitude 1. From Eqs. (S17-S18), NPPB in the transmission output involves nearly completely destructive interference among the single-photon scattering path, the two-photon scattering path, and the free propagation path, whereas NPPB in the reflection output involves nearly completely destructive interference solely of the two-photon scattering path. Furthermore, the single- and two-photon scattering paths are determined by transition paths, which are governed by the non-Hermitian effective Hamiltonian H eff . These transition paths dictate how the qubits are excited by the input and how the emitted photons interfere with each other.

More specifically, in the single-photon scattering path the fully inverted chain of qubits is first excited by the input to the state, | G ⟩ + αH + | G ⟩ . Then, the single-excitation component, αH + | G ⟩ ∝ ∑ m exp( imφ ) σ † m | G ⟩ , transitions to the steady state through an infinite number of transition paths. To see this, we can rewrite

$$| \psi ^ { 1 } \rangle = - ( H _ { e f f } ^ { ( 1 ) } ) ^ { - 1 } H _ { + } | G \rangle = \lim _ { z \to 0 } \frac { 1 } { z - H _ { e f f } ^ { ( 1 ) } } H _ { + } | G \rangle = \lim _ { z \to 0 } ( G _ { \mathcal { X } } ^ { ( 1 ) } ( z ) + G _ { c } ^ { ( 1 ) } ( z ) ) H _ { + } | G \rangle ,$$

with

$$G _ { \mathcal { I } } ^ { ( 1 ) } ( z ) = \frac { 1 } { z - H _ { 0 } ^ { ( 1 ) } } , \quad G _ { \mathcal { C } } ^ { ( 1 ) } ( z ) = \sum _ { j = 1 } ^ { \infty } G _ { \mathcal { C } , j } ^ { ( 1 ) } ( z ) , \quad G _ { \mathcal { C } , j } ^ { ( 1 ) } ( z ) = \left ( G _ { \mathcal { I } } ^ { ( 1 ) } ( z ) T ^ { ( 1 ) } \right ) ^ { j } G _ { \mathcal { I } } ^ { ( 1 ) } ( z ) .$$

̸

Here H 0 = ∑ m (∆ m -iγ/ 2) σ † m σ m and T = -iγ ∑ m = n exp( iφ | m -n | ) σ † m σ n / 2 represent the free and interaction terms of the non-Hermitian Hamiltonian, respectively; the superscript (1) denotes the single-excitation sector. Now, assuming that the single-excitation component of the steady state can be written as | ψ 1 ⟩ = ∑ m ψ m σ † m | G ⟩ , the unnormalized probability amplitude is given by ψ m = ψ I m + ψ C m , with

$$\psi _ { m } ^ { \mathcal { I } } = \lim _ { z \to 0 } \langle G | \sigma _ { m } G _ { I } ^ { ( 1 ) } ( z ) H _ { + } | G \rangle = - \sqrt { \frac { \gamma } { 2 } } \frac { e ^ { i m \varphi } } { \Delta _ { m } - i \gamma / 2 } , \quad \psi _ { m } ^ { c } = - \sqrt { \frac { \gamma } { 2 } } \lim _ { z \to 0 } \sum _ { n = 1 } ^ { N } e ^ { i n \varphi } \langle G | \sigma _ { m } G _ { c , j } ^ { ( 1 ) } ( z ) \sigma _ { n } ^ { \dagger } | G \rangle . \quad ( S 3 8 )$$

The first term, ψ I m , represents the steady-state probability amplitude of qubits individually interacting with the waveguide, while the second term, ψ C m , represents the probability amplitude for qubits collectively interacting with the waveguide. This collective term involves transitions between different qubits mediated by the long-range interaction of photons. Such transitions can be viewed as an emission-reabsorption process, whereby photons emitted by one qubit are reabsorbed by another. Specifically, for the n -th qubit initially excited by the input, the excitation transfers to the m -th qubit through an infinite sequence of transitions, with the unnormalized probability amplitudes for the j -th path given by e inφ √ γ/ 2 ⟨ G | σ m G (1) C ,j ( z ) σ † n | G ⟩ .

After excitation, each excited qubit in the state ψ m σ † m | G ⟩ can emit a single photon into the waveguide with an (unnormalized) probability amplitude ψ m . The propagation of this emitted photon acquires a phase factor exp( ± imφ ), where the minus (plus) sign corresponds to the transmission (reflection) output. Consequently, the final probability amplitude for the single-photon path is given by

$$\langle \sup _ { \pm } ^ { 1 } | \psi ^ { 1 } \rangle = P _ { T / R } ^ { \mathcal { I } } + P _ { T / R } ^ { \mathcal { C } } ,$$

with

$$P _ { T / R } ^ { \tau } = - \frac { \gamma } { 2 } \sum _ { m = 1 } ^ { N } \frac { \exp [ ( 0 / 2 ) i m \varphi ] } { \Delta _ { m } - i \gamma / 2 } , \quad P _ { T / R } ^ { c } = \sqrt { \frac { \gamma } { 2 } } \lim _ { z \to 0 } \sum _ { m = 1 } ^ { N } \sum _ { j = 1 } ^ { \infty } \exp [ ( - / + ) i m \varphi ] ( G | \sigma _ { m } G _ { \mathcal { C } , j } ^ { ( 1 ) } ( z ) H _ { + } | G ) . \quad ( S 4 0 )$$

The first term, P I T / R , involves only a sum over the qubit index. It represents the superposition of N paths in which the m -th path corresponds to a photon emitted from the m -th qubit propagating along the waveguide without being reabsorbed by other qubits; we refer to this term as the probability amplitude of the 'non-interacting transition path'. Consequently, the second term, P C T / R , represents the probability amplitude for the case in which the emitted photon can be reabsorbed by other qubits, and we refer to it as 'interacting transition path'. Thus, the final probability amplitude for the single-photon scattering path, ⟨ ϕ 1 ± | ψ 1 ⟩ , is the combination of the non-interacting path and interacting paths. In Fig. S3, we present the single-photon scattering processes for an array with N = 3 as an example.

As for the two-photon scattering path, the conclusion is similar. In addition to the single-photon events, the twophoton scattering path, ⟨ ϕ 2 ± | ψ 2 ⟩ , further involves the two-excitation steady state of the qubit ensemble. After similar derivations, the probability amplitude for the two-photon scattering path can be expressed as

$$\langle \sup _ { \pm } ^ { 2 } | \psi ^ { 2 } \rangle = P _ { T / R } ^ { \mathcal { I X } } + P _ { T / R } ^ { \mathcal { I C } } + P _ { T / R } ^ { \mathcal { C I } } + P _ { T / R } ^ { \mathcal { C } } ,$$

$$\text {with} & & \int _ { P _ { T } ^ { I I } / R } = \frac { \gamma ^ { 2 } } { 2 } \sum _ { m > n } \frac { \exp [ ( 0 / 2 ) i ( m + n ) \varphi ] } { ( \Delta _ { m } - i \gamma / 2 ) ( \Delta _ { n } - i \gamma / 2 ) } \\ & P _ { T / R } ^ { I C } = \gamma \lim _ { z \to 0 } \sum _ { m > n } \sum _ { j = 1 } ^ { \infty } \exp [ ( - \, + \, ) i ( m + n ) \varphi ] ( G | \sigma _ { m } \sigma _ { n } G _ { I } ^ { ( 2 ) } ( z ) H _ { + } G _ { C , j } ^ { ( 1 ) } ( z ) H _ { + } | G \rangle \\ & P _ { T / R } ^ { C T } = \gamma \lim _ { z \to 0 } \sum _ { m > n } \sum _ { j = 1 } ^ { \infty } \exp [ ( - \, + \, ) i ( m + n ) \varphi ] ( G | \sigma _ { m } \sigma _ { n } G _ { C , j } ^ { ( 2 ) } ( z ) H _ { + } G _ { T } ^ { ( 1 ) } ( z ) H _ { + } | G \rangle \\ & P _ { T / R } ^ { C C } = \gamma \lim _ { z \to 0 } \sum _ { m > n } \sum _ { j = 1 , k = 1 } ^ { \infty } \exp [ ( - \, + \, ) i ( m + n ) \varphi ] ( G | \sigma _ { m } \sigma _ { n } G _ { C , j } ^ { ( 2 ) } ( z ) H _ { + } G _ { C , k } ^ { ( 1 ) } ( z ) H _ { + } | G \rangle$$

with Similarly, the first term P II T / R denotes the probability amplitude of the non-interacting path, while the remaining terms correspond to the probability amplitudes of the interacting path. As a consequence, NPPB in the transmission output involves nearly completely destructive interference among the single-photon scattering path with a probability amplitude ⟨ ϕ 1 + | ψ 1 ⟩ , the two-photon scattering path with a probability amplitude ⟨ ϕ 2 + | ψ 2 ⟩ , and the free propagation path with a probability amplitude 1; whereas NPPB in the reflection output involves nearly completely destructive interference solely of the two-photon scattering path with a probability amplitude ⟨ ϕ 2 -| ψ 2 ⟩ .

In addition to the physical mechanism of NPPB, the mathematical structure of solutions satisfying g T / R = 0 is somewhat subtle. For an array of N qubits, the solutions for g T / R = 0 form a ( N -2)-dimensional submanifold. This is because, these solutions are essentially constrained by two conditions

$$g _ { T / R } = 0 , \quad \nabla g _ { T / R } = 0 .$$

̸

The second condition arises from the fact that the correlation function is analytical and attains its minimum value at 0; hence, its gradient must vanish at 0. Consequently, solutions of g T / R = ϵ with ϵ = 0 form a ( N -1)-dimensional submanifold, since only the condition g T / R = ϵ is imposed. However, as the value of ϵ decreases toward 0, one can expect that this ( N -1)-dimensional submanifold nearly collapses into a ( N -2)-dimensional submanifold, corresponding to the solutions of g T / R = 0. As a result, solutions of g T = 10 -10 for an array with N = 3 form near a curve embedded in the 3D parameters space, as shown in the main text. In Fig. S4, we present solutions of the correlation functions for chains with N ≥ 3. The solutions are obtained as follows: (i) For N = 3, we first use a nonlinear programming solver to find the maximum value of ∑ m ∆ 2 m , the set { ∆ 1 , min , ∆ 2 , min , ∆ 3 , min } , under the constraint g T / R = 10 -10 . That is,

$$g _ { T / R } | _ { \Delta _ { 1 } = \Delta _ { 1 , \min } , \Delta _ { 2 } = \Delta _ { 2 , \min } , \Delta _ { 3 } = \Delta _ { 3 , \min } } = 1 0 ^ { - 1 0 } , \quad \sum _ { m } \Delta _ { m } ^ { 2 } | _ { \Delta _ { 1 } = \Delta _ { 1 , \min } , \Delta _ { 2 } = \Delta _ { 2 , \min } , \Delta _ { 3 } = \Delta _ { 3 , \min } } = \min \left \{ \sum _ { m } \Delta _ { m } ^ { 2 } \right \} . \quad ( S 4 4 )$$

Based on this solution, we then apply the Gauss-Newton algorithm to automatically find solutions to the equation g T / R = 10 -10 until a maximum number of solutions, K sols , is reached. Here, we set K sols = 10 5 . (ii) For N &gt; 3, we similarly find the minimum of ∑ m ∆ 2 m under the constraints g T / R = 10 -10 ; while in the Gauss-Newton algorithm, we fix the first ( N -3) detunings and solve the equation g T / R = 10 -10 for the last three detunings. Due to the existence of NPPB, the PDF tends to be constant at s ≪ 1, with fluctuations near that constant, as shown in Figs. S4(a-f). These fluctuations arise from the standard deviation inherent in the numerical method used to estimate the PDF, and they can be effectively suppressed by increasing the number of disorder realizations [see Figs. S4(g-h)]. Details regarding the numerical method are discussed in the last section.

## IV. CORRELATION FUNCTION IN THE WEAK- AND STRONG-DISORDER LIMITS

## A. Weak-disorder limit ( W ≪ 1 )

In the weak-disorder limit, one can expect that the photon correlations do not deviate significantly from their clean counterparts. This means that for the reflection output, the correlation functions are expected to be distributed around the value of g R for W = 0 [see Fig. S5(a)]; while for the transmission output, the correlation functions are expected to be distributed around g T ∼ + ∞ . To confirm this statement, we present the PDFs in Figs. S5(b-i). For the reflection output [see Figs. S5(f-i)], the shapes of P ( s ) become increasingly sharper around { 1 , 0 . 444 , 1 , 1 } , as disorder strength decreases. The peaks of the PDFs correspond to the values of the correlation function in the clean limit ( W = 0). For the transmission output, as the disorder strength decreases, when φ = 0 . 5 π the region where P ( s ) = 0 shifts further towards infinity; and when φ = 0, the value of P ( s ) decreases for smaller s while it increases for larger s [see Figs. S5(b-e)]. Both of these results indicate that g T in the weak-disorder limit is distributed around infinity.

## B. Strong-disorder limit ( W ≫ 1 )

In the strong-disorder limit, one can expect that the photon-mediated interaction between qubits is significantly quenched [see Fig. S6(a)]. This indicates that the probability amplitudes of interacting paths are extremely suppressed, so that one can consider only the probability amplitudes of non-interacting paths. In this situation, the correlation

̸

FIG. S5. (a) Correlation functions for the reflection output in the absence of disorder. (b-e) PDFs for the reflection output versus disorder strength. Parameters are indicated above the plots. (f-i) PDFs for the reflection output versus disorder strength. Parameters are the same as (b-e). In all plots, the results are obtained from 10 7 disorder realizations.

<!-- image -->

functions can be solved exactly, as derived in the previous section. After some calculations, the truncated steady states are given by

$$| \tilde { \psi } ^ { 1 } \rangle = - \frac { \gamma } { 2 } \sum _ { m = 1 } ^ { N } \frac { \exp ( i m \varphi ) } { \Delta _ { m } - i \gamma / 2 } \sigma _ { m } ^ { \dagger } | G \rangle , \quad | \tilde { \psi } ^ { 2 } \rangle = | \tilde { \psi } ^ { 1 } \rangle = \frac { \gamma ^ { 2 } } { 2 } \sum _ { m > n } \frac { \exp ( i ( m + n ) \varphi ) } { ( \Delta _ { m } - i \gamma / 2 ) ( \Delta _ { n } - i \gamma / 2 ) } \sigma _ { m } ^ { \dagger } \sigma _ { n } ^ { \dagger } | G \rangle . \quad ( S 4 5 )$$

Thus,

and

$$g _ { T } = \frac { | 1 - 2 i P _ { T } ^ { \mathcal { I } } - P _ { T } ^ { \mathcal { I } \mathcal { I } } | ^ { 2 } } { | 1 - i P _ { T } ^ { \mathcal { I } } | ^ { 4 } } = \frac { | 1 + i \sum _ { m } ( \Delta _ { m } - i / 2 ) ^ { - 1 } - \sum _ { m > n } ( \Delta _ { m } - i / 2 ) ^ { - 1 } ( \Delta _ { n } - i / 2 ) ^ { - 1 / 2 } | ^ { 2 } } { | 1 + i \sum _ { m } ( \Delta _ { m } - i / 2 ) ^ { - 1 / 2 } | ^ { 4 } } \quad ( S 4 6 )$$

$$g _ { R } = \frac { | P _ { R } ^ { \mathcal { X } T } | ^ { 2 } } { | P _ { R } ^ { \mathcal { X } T } | ^ { 4 } } = \frac { | 2 \sum _ { m > n } \frac { e ^ { 2 i ( m + n ) \varphi } } { ( \Delta _ { m } - i / 2 ) ( \Delta _ { n } - i / 2 ) } | ^ { 2 } } { | \sum _ { m } \frac { e ^ { 2 i m \varphi } } { \Delta _ { m } - i / 2 } | ^ { 4 } } .$$

̸

From Eq.(S46), the correlation function in the transmission output is independent of the distance between qubits, i.e., independent of φ . In addition, solutions of g T = 0 exist when φ = 0, provided that N ≥ 3. For instance, one can easily verify that g T = 0 if ∆ i = 1 / 2 and ∆ j = -1 / 2 for i = j . However, these results do not contradict those obtained from Eq. (S15), where the correlation functions are distance-dependent and have no solutions satisfying g T = 0 when φ = 0. This discrepancy arises because Eqs. (S46,S47) are valid only in the sense of disorder averaging.

To examine the validity of Eqs. (S46,S47), we numerically calculate the normalized fidelity

$$F _ { 1 } = \frac { | \langle \tilde { \psi } ^ { 1 } | \psi ^ { 1 } \rangle | } { \sqrt { | \langle \tilde { \psi } ^ { 1 } | \tilde { \psi } ^ { 1 } \rangle | | \langle \psi ^ { 1 } | \psi ^ { 1 } \rangle | } } , \quad F _ { 2 } = \frac { | \langle \tilde { \psi } ^ { 2 } | \psi ^ { 2 } \rangle | } { \sqrt { | \langle \tilde { \psi } ^ { 2 } | \tilde { \psi } ^ { 2 } \rangle | | \langle \psi ^ { 2 } | \psi ^ { 2 } \rangle | } } .$$

Since photon correlations are fully encoded in the truncated steady states, the closer the normalized fidelity is to unity, the closer the values of the two types of correlation functions (obtained from Eqs. (S15,S16) and Eqs. (S46,S47)) will be. We also investigate the Hellinger distance between the PDFs P ( s ) obtained from Eqs. (S15-S16) and the PDFs ˜ P ( s ) obtained from Eqs. (S46,S47). The Hellinger distance between two probability density functions, q ( x ) and p ( x ), is defined as

$$H ( q ( x ) , p ( x ) ) = \frac { 1 } { 2 } \int \left ( \sqrt { p ( x ) } - \sqrt { q ( x ) } \right ) ^ { 2 } d x .$$

The Hellinger distance measures the similarity between p ( x ) and q ( x ); its values range from 0 to 1, with values closer to 0 indicating that the two distributions are more similar. From Figs. S6(b-e), one can see that (i) the fidelity is

<!-- image -->

̸

FIG. S6. (a) Schematics of the systems in the weak- and intermediate-disorder regimes (left panel); and in the strong-disorder regime (right panel). Here T mn = -i exp( i | m -n | φ ) σ † m σ n / 2 with m = n . (b,c) Fidelity between the truncated steady state { | ψ 1 ⟩ , | ψ 2 ⟩ } obtained from the non-Hermitian Hamiltonian with long-range interactions and the truncated steady state { | ˜ ψ 1 ⟩ , | ˜ ψ 2 ⟩ } obtained from Eq. (S45). (d,e) Hellinger distance between the PDFs obtained from Eqs. (S15-S16) and those obtained from Eqs. (S46,S47). Here we plot ˜ H( P, ˜ P ) = 1 -˜ H( P, ˜ P ). N = 10 in plots (b-e). The results are obtained from 10 4 disorder realizations. (f,g) Probability of PA and P (10 -3 ) for the transmission output versus disorder strength for different system sizes. The dashed lines indicate slopes of W -3 . These results are obtained from Eq. (S46) using 10 10 disorder realizations. (h,i) Probability of PA and P (10 -3 ) for the reflection output versus disorder strength for different system sizes and phases. These results are obtained from Eq. (S47) using 10 10 disorder realizations. Different colored lines correspond to different chain sizes (the same as those in (f,g)). In the top panel of (i), the parameters are the same as in (h) (labeled within the plot), and in the bottom panel of (i), we plot P ( s &lt; 1) -2 / 3 for N = 10.

close to 1 for both the single- and two-excitation steady states as the disorder strength increases, and (ii) the value of H( P ( s ) , ˜ P ( s )) approaches 0 both for both the transmission and reflection outputs as the disorder strength increases. This implies that Eqs. (S46,S47) are indeed good approximations in the strong-disorder limit. Note that, although we only calculated the case of N = 10 here, similar results can be obtained for other chain sizes.

In Figs. S6(f-i), we present P (10 -3 ) and P ( s &lt; 1) versus different disorder strengths. For the transmission output, our results indicate that both P (10 -3 ) and P ( s &lt; 1) decrease as the disorder strength increases. This decrease follows a scaling of the form W -3 , regardless of the chain size. For the reflection output, the probability of NPPB increases with increasing disorder strength, while the probability of PA saturates to a constant in the limit W ≫ 1. This constant is close to 2 / 3, i.e., the value of P ( s &lt; 1) for a system with N = 2 and φ = 0. This result is also consistent with Fig. 4(c) of the main text, where P ( s &lt; 1) is calculated based on Eq. (S18).

FIG. S7. Correlation statistics of the transmission output. (a) Probability of PA versus γ nw and W . Here N = 1. (b) PDFs for different γ nw , with the values of γ nw being indicated besides each curve. The chosen parameters are { N = 3 , φ = 0 . 04 π, W = 0 . 14 } (top) and { N = 3 , φ = 0 , W = 1 } (bottom), which are the same as Figs. 2(a,b) of the main text. These results are obtained from 10 10 disorder realizations.

<!-- image -->

## V. EFFECTS OF LOSSES ON NON-WAVEGUIDE MODES

In this section, we consider losses to modes external to the waveguide. With such losses, the non-Hermitian Hamiltonian becomes

$$H _ { e f f } = \sum _ { m , n = 1 } ^ { N } \left ( \Delta _ { m } \delta _ { m , n } - \frac { i \gamma _ { n w } } { 2 } \delta _ { m , n } - \frac { i \gamma } { 2 } e ^ { i | m - n | \varphi } \right ) \sigma _ { m } ^ { \dagger } \sigma _ { n } ,$$

where γ nw denotes the decay rate to non-waveguide modes. Again, we set γ = 1 in the remainder of this section and use the symbol β to represent the coupling efficiency. The definition of β is β = γ/ ( γ + γ nw ) = (1 + γ nw ) -1 . In the main text, we set γ nw = 0, corresponding to a unit value of the coupling efficiency.

## A. Transmission output

We first consider the single-qubit system, for which P ( s &lt; 1) and P (0) can be analytically calculated. In this case, the correlation function is given by

$$g _ { T } = \frac { ( 4 \Delta _ { 1 } ^ { 2 } + ( \gamma _ { n w } - 1 ) ^ { 2 } ) ( 4 \Delta _ { 1 } ^ { 2 } + ( \gamma _ { n w } + 1 ) ^ { 2 } ) } { ( 4 \Delta _ { 1 } ^ { 2 } + \gamma _ { n w } ^ { 2 } ) ^ { 2 } } .$$

Before proceeding to disordered systems, let us first focus on clean systems. For a resonant qubit, i.e., ∆ 1 = 0, the correlation function is g T = ( γ 2 nw -1) 2 /γ 4 nw , which satisfies g T &lt; 1 for γ nw &gt; 1 / √ 2 ( β ≲ 0 . 58) and g T = 0 for γ nw = 1 ( β = 1 / 2). Unlike lossless system, here the transmission output can produce either antibunched or perfectly blockaded photons by appropriately adjusting the coupling efficiency.

Considering the effects of disorder, the probability of PA is calculated as

$$\text {Considering the effects of disorder, the probability of PA is calculated as} \\ \mathbb { P } ( s < 1 ) & = \frac { 1 } { \sqrt { 2 \pi W } } \int _ { - \infty } ^ { \infty } e ^ { - \Delta _ { 1 } ^ { 2 } / 2 w ^ { 2 } } \, \text {E} \left ( \frac { ( 4 \Delta _ { 1 } ^ { 2 } + ( \gamma _ { n w } - 1 ) ^ { 2 } ) ( 4 \Delta _ { 1 } ^ { 2 } + ( \gamma _ { n w } + 1 ) ^ { 2 } ) } { ( 4 \Delta _ { 1 } ^ { 2 } + \gamma _ { n w } ^ { 2 } ) ^ { 2 } } - 1 \right ) \, d \Delta _ { 1 } \\ & = \frac { 1 } { \sqrt { 2 \pi W } } \int _ { 0 } ^ { \frac { 1 } { 4 } - \frac { 1 } { 4 } - \Delta _ { 1 } / 2 w ^ { 2 } } { \sqrt { \Delta _ { 1 } } } \, \text {E} \left ( \gamma _ { n w } - \frac { 1 } { \sqrt { 2 } } \right ) \, d \Delta _ { 1 } \\ & = \text {erf} \left ( \frac { \sqrt { 2 \pi } w ^ { 2 } / 4 - 1 / 8 } { \sqrt { 2 W } } \right ) \text {e} \left ( \gamma _ { n w } - \frac { 1 } { \sqrt { 2 } } \right ) ,$$

where erf( x ) is the error function. This result shows that when a single qubit is strongly coupled to the waveguide, PA in the transmission output is impossible. By reducing the coupling efficiency until reaching a critical value β cri = 1 / (1 + 1 / √ 2) ≈ 0 . 58, PA events can be observed. For β &lt; β cri , the probability of PA increases as the coupling efficiency decreases, as shown in Fig. S7(a).

As for P (0), we first calculate the PDF. After performing the integral (similar to Eq. (S20)), the PDF for s &lt; 1 is given by

$$P ( s ) & = - \frac { 1 } { \sqrt { 2 \pi } W } \frac { ( - 1 + \sqrt { s + 4 ( 1 - s ) ^ { 2 } } \gamma ^ { 3 } ) ^ { 2 } } { \sqrt { - 1 + ( s - 1 ) ^ { 2 } \gamma ^ { 2 } _ { n w } + \sqrt { s + 4 ( 1 - s ) ^ { 2 } } \gamma ^ { 2 } _ { n w } ) ^ { 2 } } ( s - 1 ) ^ { 2 } ( 4 ( s - 1 ) ^ { 2 } \gamma ^ { 2 } _ { n w } - s + \sqrt { s + 4 ( 1 - s ) ^ { 2 } \gamma ^ { 2 } _ { n w } } ) ( 1 - s ) ^ { 3 / 2 } \\ & \exp \left ( \frac { - 1 + ( s - 1 ) ^ { 2 } \gamma ^ { n w } + \sqrt { s + 4 ( 1 - s ) ^ { 2 } } \gamma ^ { n w } } { ( 8 s - 8 ) W ^ { 2 } } \right ) \\ & \text {where } \gamma _ { n w } > 1 / \sqrt { 2 } \text { and } 1 + \gamma _ { n w } ^ { - 4 } - 2 \gamma ^ { - 2 } < s < 1 . \text { From this result, } P ( 0 ) = 0 \text { for } \beta \neq 1 / 2 \left ( \gamma _ { n w } \neq 1 / 2 \right ) \text { only when the }$$

where γ nw &gt; 1 / 2 and 1 + γ -4 nw -2 γ -2 nw &lt; s &lt; 1. From this result, P (0) = 0 for β = 1 / 2 ( γ nw = 1 / 2); only when the coupling efficiency is exactly 1 / 2, P ( s ) diverges as P ( s ) ∼ ( W √ s ) -1 , whereby PPB events become possible.

̸

̸

̸

In Figs. S8(a,b), we present the numerical results for the probability of PA for N = 5 and N = 10. These results show that the probability of PA can be efficiently enhanced by decreasing the coupling efficiency (by increasing γ nw ). In particular, the probability of PA can reach unit provided that the chain is highly dense, i.e., φ ≪ 1. We then calculate the PDFs for the system with N = 3 [see Fig. S7](b). When φ = 0, the results show that as the coupling efficiency decreases, the PDFs still exhibit a constant behavior at s ≪ 1 as long as β ≳ 0 . 45; this behavior disappears for β ≲ 0 . 45. For β ≳ 0 . 45, the value of P ( s ) at s ≪ 1 can even be larger than that for lossless systems ( γ nw = 0). This is observed, for instance, when γ nw = 1 . 2 ( β ≊ 0 . 45). Therefore, we still use P (10 -3 ) as a measure for the probability of NPPB and present the results for different system parameters in Figs. S8(c,d). The results show that the probability of NPPB attains a larger value when the coupling efficiency is not too high ( β ≲ 0 . 5). Moreover, when φ = 0, the generation of strongly antibunched photon is impossible [see Fig. S7], similar to the system with β = 1.

## B. Reflection

In Figs. S9(a,b), we present the results of the probability of PA for N = 5 and N = 10. As the coupling efficiency decreases, a high probability of PA can only be achieved when the chain is highly dense, which is similar to the transmission output. Besides, it maintains a finite value even for strong disorder strength. This is because the effects of losses will be suppressed by strong disorder. We also investigate the behavior of P ( s 0 ) at s 0 ≪ 1 when W ≫ 1. In this limit, the correlation function is given by

$$g _ { R } = \frac { | P _ { R } ^ { \mathcal { I } } | ^ { 2 } } { | P _ { R } ^ { \mathcal { I } } | ^ { 4 } } = \frac { | 2 \sum _ { m > n } \frac { e ^ { 2 i ( m + n ) \rho } } { ( \Delta _ { m } - i / 2 - i \gamma _ { n w } / 2 ) ( \Delta _ { n - i } - i / 2 - i \gamma _ { n w } / 2 ) } | ^ { 2 } } { | \sum _ { m } \frac { e ^ { 2 i m \varphi } } { \Delta _ { m } - i / 2 - i \gamma _ { n w } / 2 } | ^ { 4 } } .$$

The numerical results in Figs. S9(c,d) show clearly that the probability of NPPB increases with increasing disorder strength, which is similar to systems where β = 1.

## VI. EFFECTS OF CHIRALITY IN COUPLING TO WAVEGUIDE MODES

̸

In this section, we consider chirality in coupling to waveguide modes, i.e., γ T = γ R . We define the chirality as α = γ R /γ T , and we set γ T = 1 as the energy unit. Figures S10(a1) show the photon correaltions for transmission output, for system with chain size N = 10. The chirality together with the losses on non-waveguide modes significantly affect photon correlations. For transmission output, when qubits weakly coupled to waveguide ( β ≪ 1), photons maintain the coherence for all values of chirality; while when qubits strongly coupled to waveguide ( β ≈ 1), photons exhibit strong bunching for α ≳ 0 . 5, and antibunched even strongly antibunched photon emerge by further increasing chirality (decreasing α ). When the qubits are weakly coupled to the waveguide in a perfectly chiral fashion, the transmitted photon exhibit Poisson statistics for small system size, N = 10. As the chain size increases, the output becomes antibunched and approaches near-perfect antibunching at the optimal chain size N ≈ 183; beyond this optimal chain size the output light becomes bunched as N increases further [see Fig. S10(a2)]. Note that these behaviors are quantitatively consistent with Fig. 3a in [10].

FIG. S8. Correlation statistics of the transmission output. (a,b) Probability of PA versus φ and W for different N and γ nw . (c,d) P (10 -3 ) versus φ and W for different N and γ nw . These results for P ( s &lt; 1) ( P (10 -3 )) are obtained from 5 4 (5 × 10 6 ) disorder realizations.

<!-- image -->

In the presence of disorder, Figs. S10(b1-c2) show P ( s &lt; 1) and P (10 -3 ) for the case of complete transimissionchirality ( α = 0). On the one hand, the probability of photon antibunching approach unit when qubits weakly coupled to waveguide, and rapidly decrease with increasing coupling strength. On the other hand, the probability of strong photon antibunching exhibits non-negligible value only for 0 . 1 ≲ β ≲ 0 . 4. Notably, for the chain size investigated here N = 10 , 20, these behaviors of P ( s &lt; 1) and P (10 -3 ) do not change significantly with changing N . Considering that when N ∼ 10 2 , the qubit number significantly affects the correlations even without the presence of disorder, we expect that P ( s &lt; 1) and P (10 -3 ) may show quite distinctive behaviors with further increasing N , in comparison with the results provided here.

## VII. EFFECTS OF FINITE BANDWIDTH OF INPUT STATE

In this section, we consider the effects of finite bandwidth of the input state, which should be compared with the single-mode (zero bandwidth) coherent input state considered in the main text. We assume that the input state has the form

$$\rho _ { E } ( t _ { 0 } ) \, \in \exp \left ( \bar { n } \int _ { - \infty } ^ { \infty } \alpha ( \omega ) a _ { T } ( \omega ) - \alpha ( \omega ) a _ { T } ^ { \dagger } ( \omega ) \, d \omega \right ) .$$

FIG. S9. Correlation statistics of the reflection output. (a,b) Probability of versus φ and W for different N and γ nw . (c,d) Solid lines denote P (10 µ ) versus φ and W for different N and γ nw , with the values of µ = -3 , -7. Dashed lines represent the numerical fits of ∼ W . These results for P ( s &lt; 1) ( P ( s 0 )) are obtained from 5 4 (5 × 10 10 ) disorder realizations.

<!-- image -->

Here, α ( ω ) controls the profile of the input state and is required to be normalized, i.e., ∫ ( α ( ω )) 2 d ω = 1, such that ¯ n 2 = ∫ ∞ -∞ Tr [ ρ E a † T ( ω ) a T ( ω ) ] d ω represents the total number of photons in the input state, and we still consider the weak-input limit ¯ n 2 ≪ 1. To be able to compare with the case of zero bandwidth, we require α ( ω ) to exhibit two following generic features: (i) α ( ω ) approaches its maximum at ω 0 and rapidly decreases to zero for ω away from ω 0 ; (ii) a characteristic bandwidth denoted by σ ω is able to characterize the width of α ( ω ), such that σ ω → 0 ( σ ω →∞ ) corresponds to a ideal zero-bandwidth input ( δ -pulse input in the time domain). Hereafter, we consider α ( ω ) to be Lorentz profile, i.e., (we assume γ = 1)

$$\alpha ( \omega ) = \frac { 1 } { \mathcal { N } } \frac { \sigma _ { \omega } } { ( \omega - \omega _ { 0 } ) ^ { 2 } + \sigma _ { \omega } ^ { 2 } } ,$$

where N = ( π/ 2 σ ω ) 1 / 2 denotes the normalization factor. The total number of photons in the time domain is given by

$$\bar { n } ^ { 2 } ( t ) = \int \text {Tr} \{ a _ { T } ^ { \dagger } ( \omega , t ) a _ { T } ( \omega , t ) \rho _ { E } ( t _ { 0 } ) \} \, d \omega = \frac { 1 } { \sqrt { 2 \pi } } \int \text {Tr} \left \{ e ^ { - i \omega ( t - t _ { 0 } ) } a _ { T } ^ { \dagger } ( \omega ) a _ { T } ( \omega ) \rho _ { E } ( t _ { 0 } ) \right \} d \omega = \bar { n } ^ { 2 } \frac { e ^ { - \sigma _ { \omega } | t _ { 0 } | } ( 1 + \sigma _ { \omega } | t - t _ { 0 } | ) } { \sqrt { 2 \pi } } .$$

This expression demonstrates that the input is also a wave package in the time domain, where ¯ n 2 ( t ) approaches its maximum at t = t 0 and rapidly decreases for t away from t 0 .

FIG. S10. (a1) Photon correlations in the transmission output versus chirality and coupling strength for N = 10 and φ = 0. (a2) Photon correlations in the transmission output versus chain size. Here the chosen parameters are α = 0 and β = 0 . 0083. (b1,c1) Probability of photon antibunching in the transmission output versus disorder and coupling strength. N = 10 in (b1) and N = 20 in (c1). (b2,c2) P (10 -3 ) in the transmission output versus disorder and coupling strength. N = 10 in (b2) and N = 20 in (c2). α = 0 in (b1-c2). Results are obtained from 10 5 disorder realizations.

<!-- image -->

In this case, the master equation is still given by Eq. (S8), with

$$f ( t - t _ { 0 } , m d ) = \bar { n } \sqrt { \sigma _ { \omega } } e ^ { - \sigma _ { \omega } | t - t _ { 0 } - m d / v _ { g } | } e ^ { - i \omega _ { 0 } ( t - t _ { 0 } - m d / v _ { g } ) } \approx \bar { n } \sqrt { \sigma _ { \omega } } e ^ { - \sigma _ { \omega } | t - t _ { 0 } | } e ^ { - i \omega _ { 0 } ( t - t _ { 0 } ) } ,$$

where we assume that photons are injected far from the atomic ensemble, such that t 0 + md/v g ≈ t 0 . Consequently, the correlation function can be obtained as

$$g _ { \mu } ( \tau , \tau ) = \frac { \text {Tr} \left [ \rho ( \tau ) a _ { \mu , o u t } ^ { \dagger } ( \tau ) a _ { \mu , o u t } ^ { \dagger } ( \tau ) a _ { \mu , o u t } ( \tau ) a _ { \mu , o u t } ( \tau ) \right ] } { \text {Tr} \left [ \rho ( \tau ) a _ { \mu , o u t } ^ { \dagger } ( \tau ) a _ { \mu , o u t } ( \tau ) \right ] ^ { 2 } } ,$$

where ρ ( τ ) denotes the density matrix of atomic ensemble governed by the master equation. The input-output relations read as

$$a _ { T , o u t } ( \tau ) = a _ { T , i n } ( \tau ) - i \sqrt { \frac { \gamma } { 2 } } \sum _ { m } e ^ { - i m d } \sigma _ { m } ( \tau ) , \quad a _ { R , o u t } ( \tau ) = - i \sqrt { \frac { \gamma } { 2 } } \sum _ { m } e ^ { i m d } \sigma _ { m } ( \tau ) ,$$

with

$$a _ { T , i n } ( \tau ) = \frac { 1 } { \sqrt { 2 \pi } } \int \text {Tr} \left [ \rho _ { E } ( t _ { 0 } ) e ^ { - i \omega ( \tau - t _ { 0 } ) } a _ { T } ( \omega , t _ { 0 } ) \right ] d \omega = \bar { n } \sqrt { \sigma _ { \omega } } e ^ { - \sigma _ { \omega } | \tau - t _ { 0 } | } e ^ { - i \omega _ { 0 } ( \tau - t _ { 0 } ) } .$$

Before proceeding to present the results for the correlation functions, we stress that, in addition to the bandwidth σ ω , the evolution time τ will also significantly affect the photon correlation. For a ideal zero-bandwidth input, the correlation functions g µ are time-independent for t ≫ 1, and thus their values can be obtained from the steady state of the atomic ensemble. This actually arises from the fact that the drive strength ∝ | f ( t -t 0 , md ) | remains a constant in the time domain. However, for a finite-bandwidth input, the drive strength is now time-dependent, therefore, one should expect that g µ ( τ, τ ) is also dependent on the evolution time τ .

FIG. S11. (a) Photon correlation in the transmission versus bandwidth and evolution time for system with N = 1 and ∆ 1 = 0. (b) Probability of photon antibunching in the reflection output versus band width for system with N = 2 and φ = 0. Results are obtained from 10000 disorder realizations. (c) Probability density function in the reflection output for different values of band width for system with N = 3 and φ = 0 . 5 π . Results are obtained from 10 5 disorder realizations. τ = t 0 in (b) and (c). ¯ n = 0 . 1 in (a-c).

<!-- image -->

̸

In Fig. S11(a), we present the photon correlation in the transmission output for N = 1 with ∆ 1 = 0. For a ideal zero-bandwidth input, g T = ∞ . Our result reveals that g T ( τ, τ ) generally recovers its zero-bandwidth counterpart when σ ω ≪ 1. This is because, when the bandwidth is much smaller than the individual decay rate γ , the input can be approximately considered as a zero-bandwidth coherent state, resulting in g T ( τ, τ ) ≫ 1. Increasing σ ω , g T ( τ, τ ) becomes sensitive to the evolution time τ : its value still approximately recovers the zero-bandwidth counterpart for τ ∼ t 0 ; while for | τ -t 0 | ≫ 1, g T ( τ, τ ) significantly deviates from infinity, which can even approaches near zero. In Figs. S11(b,c), we present the probability of PA for system with N = 2 and φ = 0, and the probability density functions for system with N = 3 and φ = 0 . 5 π in the reflection output. The obtained results show good agreement with their zero-bandwidth counterpart as long as σ ω /γ ≲ 0 . 1, i.e., P ( s &lt; 1) = 2 / 3 and P ( s ≪ 1) = 0.

In summary, when one considers the effect of finite band width of input state, the obtained results show good agreement with their zero-bandwidth counterpart, as long as the bandwidth σ ω is much smaller than the individual decay rate γ , and the detection time τ is appropriately chosen. In typical waveguide QED platforms, γ ∼ MHz, therefore, the required band width should be σ ω ≲ KHz, which can be achieved in the state-of-art waveguide platforms [7-9].

## VIII. NUMERICAL CALCULATIONS OF P ( s &lt; 1) AND P ( s ≪ 1) FOR MANY-QUBIT SYSTEM

## A. Calculation about P ( s &lt; 1)

The definition of P ( s &lt; 1) is

$$\mathbb { P } ( s < 1 ) = \int _ { 0 } ^ { 1 } P ( s ) d s = \int _ { - \infty } ^ { \infty } \cdots \int _ { - \infty } ^ { \infty } \Theta ( g _ { \mu } - 1 ) p ( \Delta _ { 1 } , \Delta _ { 2 } , \cdots , \Delta _ { N } ) d \Delta _ { 1 } \cdots d \Delta _ { N } .$$

According to the Monte Carlo method, this integral can be approximately evaluated by

$$\mathbb { P } ( s < 1 ) = E [ \Theta ( g _ { \mu } - 1 ) ] \approx \frac { 1 } { K } \sum _ { j = 1 } ^ { K } \Theta ( g _ { \mu } | _ { \tilde { \Delta } _ { j } } - 1 ) ,$$

where ⃗ ∆ j = { ∆ 1 ,j , · · · , ∆ N,j } denotes the j -th sample drawn from the i.i.d Gaussian distribution. The sample size K should be large enough to reduce the variance of the estimation in Eq. (S63), which is given by V [Θ( g µ -1)] ∼ K -1 . In Fig. S12(a), we present E [Θ( g µ -1)] for the reflection output versus the sample size K , with N = 2 and φ = 0. The mean and standard deviation are obtained from 10 2 estimations of Eq. (S63). As shown, K ∼ 10 4 is sufficient to reduce V [Θ( g µ -1)], so that the mean value deviate only slightly from the exact value of 2 / 3, even for a single estimation. Therefore, in the main text, we set K = 50000 and perform a single estimation for all plots concerning P ( s &lt; 1).

FIG. S12. (a) Probability of PA for the reflection output from the Monte Carlo integration. The result is obtained from 10 2 estimations. Red dots and the shaded area denote the mean value and the standard deviation of the estimations, respectively. Here the chosen parameter are N = 2 and φ = 0, so that the solid line represents the exact value of P ( s &lt; 1), which is equal to 2 / 3. (b-c) PDFs for the transmission (b) and reflection (c) outputs from the Monte Carlo integration. The result is obtained from 10 2 estimations. Red dots and the shaded area denote the mean value and the standard deviation from Eq. (S64), respectively. The number of disorder realizations is K = 50000. The solid blue lines represent the results from K = 10 11 disorder realizations. Here the chosen parameters are N = 3, φ = 0 . 04 π , and W = 0 . 15 in (b); N = 3, φ = 0 . 5 π , W = 1 in (c).

<!-- image -->

## B. Calculation about P ( s ≪ 1)

Similarly, P ( s ) can be approximately estimated by the Monte Carlo method according to

$$P ( s ) = E [ \delta ( g _ { \mu } - s ) ] \approx \frac { 1 } { K } \sum _ { j = 1 } ^ { K } \lim _ { \varepsilon \to 0 } \tilde { \delta } _ { \varepsilon } \left ( g _ { \mu } | _ { \tilde { \Delta } _ { j } } - s \right ) ,$$

where ˜ δ ε ( x ) represents a function that weakly converges to the Dirac-delta function in the limit ε → 0. Compare to the estimation in Eq. (S63), the estimation of P ( s ), especially at s ≪ 1, requires a larger number of disorder realizations to achieve an acceptable error. This is because the number of events s -ϵ &lt; g µ &lt; s + ϵ with ϵ ≪ s decreases with decreasing s . To see this, note that the probability of the event s 0 -ϵ &lt; g µ &lt; s 0 + ϵ , with ϵ ≪ s 0 , is given by

$$\mathbb { P } ( s _ { 0 } - \epsilon < s < s _ { 0 } + \epsilon ) = \int _ { s _ { 0 } - \epsilon } ^ { s _ { 0 } + \epsilon } P ( s ) \, d s \sim P ( s _ { 0 } ) \epsilon .$$

Since we have shown that P ( s 0 ) ∼ constant for s 0 ≪ 1, this probability decreases as s 0 decreases, due to the condition ϵ ≪ s 0 . In fact, the constant form of P ( s ) implies that this probability scales as s ; i.e., P ( s 0 -ϵ &lt; s &lt; s 0 + ϵ ) ∼ s if we let ϵ = ηs 0 with η ≪ 1. The decrease of P ( s 0 -ϵ &lt; s &lt; s 0 + ϵ ) ∼ s means that the number of events with s -ϵ &lt; g µ &lt; s + ϵ also decreases as s decreases. As a result, many estimations from Eq. (S64) for s ≪ 1 will yield zero if K is not sufficiently large, because the value of ˜ δ ϵ ( x ) is proportional to the number of such events. Meanwhile, the computational cost increases rapidly with K , especially for large chain size. To balance the accuracy of the Monte Carlo integration results with the computational cost, an appropriate value of K must be chosen.

In Figs. S12(b,c), we compare the PDFs obtained from K = 50000 with those obtained from K = 10 11 . For K = 50000, we perform 10 2 estimations so that the total sample size is 5 6 . For K = 10 11 , the variation in the estimation is negligible, and it can be regarded as the exact PDF. Compared to the estimation of Eq. (S63), the variation increases as s decreases s and becomes non-negligible for s ≪ 1. However, despite the increased variation, the mean values from 10 2 are very close to the exact value. Therefore, unless otherwise noted, we set K = 50000 and perform 10 2 estimations using Eq. (S64) to obtain all plots related to P (10 -3 ) in the main text.

- [∗ zhenglili@jhun.edu.cn](mailto:zhenglili@jhun.edu.cn)
- [† xinyoulu@hust.edu.cn](mailto:xinyoulu@hust.edu.cn)

[1] T. Caneva, M. T. Manzoni, T. Shi, J. S. Douglas, J. I. Cirac, and D. E. Chang, 'Quantum dynamics of propagating photons with strong interactions: a generalized input-output formalism,' New Journal of Physics 17 , 113001 (2015).

- [2] A. S. Sheremet, M. I. Petrov, I. V. Iorsh, A. V. Poshakinskiy, and A. N. Poddubny, 'Waveguide quantum electrodynamics: Collective radiance and photon-photon correlations,' Reviews of Modern Physics 95 , 015002 (2023).
- [3] A. Asenjo-Garcia, M. Moreno-Cardoner, A. Albrecht, H. J. Kimble, and D. E. Chang, 'Exponential Improvement in Photon Storage Fidelities Using Subradiance and 'Selective Radiance' in Atomic Arrays,' Physical Review X 7 , 031024 (2017).
- [4] Y. Wang, W. Verstraelen, B. Zhang, T. C. H. Liew, and Y. D. Chong, 'Giant Enhancement of Unconventional Photon Blockade in a Dimer Chain,' Phys. Rev. Lett. 127 , 240402 (2021).
- [5] T. C. H. Liew and V. Savona, 'Single Photons from Coupled Quantum Modes,' Phys. Rev. Lett. 104 , 183601 (2010).
- [6] H. Flayac and V. Savona, 'Unconventional photon blockade,' Phys. Rev. A 96 , 053810 (2017).
- [7] S. Faez, P. T¨ urschmann, H. R. Haakh, S. G¨ otzinger, and V. Sandoghdar, 'Coherent interaction of light and single molecules in a dielectric nanoguide,' Physical review letters 113 , 213601 (2014).
- [8] B. Kuyken, T. Ideguchi, S. Holzner, M. Yan, T. W. H¨ ansch, J. Van Campenhout, P. Verheyen, S. Coen, F. Leo, R. Baets, et al. , 'An octave-spanning mid-infrared frequency comb generated in a silicon nanophotonic wire waveguide,' Nature communications 6 , 6310 (2015).
- [9] Z. Bao, Y. Li, Z. Wang, J. Wang, J. Yang, H. Xiong, Y. Song, Y. Wu, H. Zhang, and L. Duan, 'A cryogenic on-chip microwave pulse generator for large-scale superconducting quantum computing,' Nature Communications 15 , 5958 (2024).
- [10] A. S. Prasad, J. Hinney, S. Mahmoodian, K. Hammerer, S. Rind, P. Schneeweiss, A. S. Sørensen, J. Volz, and A. Rauschenbeutel, 'Correlating photons using the collective nonlinear response of atoms weakly coupled to an optical mode,' Nature Photonics 14 , 719 (2020).