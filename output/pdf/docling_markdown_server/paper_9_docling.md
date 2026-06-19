## Rydberg-atom manipulation through strong interaction with free electrons

Adamantios P. Synanidis, 1 P. A. D. Gonçalves, 1 and F. Javier García de Abajo 1,2, ∗

1 ICFO-Institut de Ciencies Fotoniques, The Barcelona Institute of Science and Technology, 08860 Castelldefels (Barcelona), Spain

2 ICREA-Institució Catalana de Recerca i Estudis Avançats, Passeig Lluís Companys 23, 08010 Barcelona, Spain (Dated: September 30, 2024)

Optically trapped Rydberg atoms are a suitable platform to explore quantum many-body physics mediated by long-range atom-atom interactions that can be engineered through externally applied light fields. However, this approach is limited to dipole-allowed transitions and a spatial resolution of the order of the optical wavelength. Here, we theoretically investigate the interaction between free electrons and individual Rydberg atoms as an approach to induce nondipolar transitions with subnanometer spatial precision and a substantial degree of control over the final atomic states. We observe unity-order excitation probabilities produced by a single electron for suitably chosen combinations of electron energies and electron-beam distance to the atom. We further discuss electron-atom entanglement in combination with lateral shaping of the electron followed by postselection. Our results support free electrons as powerful tools to manipulate Rydberg atoms in previously inaccessible ways.

## I. INTRODUCTION

Rydberg atoms have an electron in an orbital with a high principal quantum number [1] and display unique properties that find application in quantum computing [2-5] and quantum simulation of many-body systems [6-12]. In particular, highly excited Rydberg atoms possess long lifetimes ( ≲ 1 ms) and large dipole moments, rendering them highly sensitive to external fields and enabling long-range atom-atom interactions [13-15]. Because of the latter, the excitation of an atom to a Rydberg state inhibits the subsequent excitation of nearby atoms [16-18], thus enabling the implementation of quantum gates and entanglement [19, 20], while also producing a strong nonlinear optical response at the few- and single-photon level [21-23].

The formation and study of quantum gases of ultracold Rydberg atoms trapped in optical lattices [6, 24] are currently relying on optical techniques, which are employed to coherently control atom-atom interactions [7, 25] as well as to image [26-28] and read out the system [2, 28]. However, far-field excitation and probing restrict the control schemes to dipole transitions with a spatial resolution limited by optical diffraction.

Electron beams (e-beams) offer an appealing alternative for targeting and manipulating atomic and molecular transitions [29-32], where the evanescent electromagnetic field associated with free electrons mediates the interaction [33]. This field is highly inhomogeneous near the e-beam and contains multipolar components capable of inducing nondipolar transitions inaccessible to far-field light. In addition, e-beams can be focused down to subnanometer lateral widths [33, 34], thus providing an enhanced spatial resolution to address individual atoms. In the context of quantum gases, broad e-beams have been used as probes to image atoms in optical lattices [35-37], while quasi-free Rydberg electrons have been demonstrated to couple to Bose-Einstein condensates [38]. The use of e-beams to control and study Rydberg atoms could further benefit from recent advances in modulating the free-electron wave function through the interaction with free-space [39, 40] and scattered [41-49] optical fields or via electrostatic electron phase shaping [50, 51].

[∗ E-mail: javier.garciadeabajo@nanophotonics.es](mailto:javier.garciadeabajo@nanophotonics.es)

Here, we introduce a new approach for manipulating Rydberg atoms using free electrons (Fig. 1a). By characterizing the e-beam-Rydberg-atom interaction theoretically, we reveal a wealth of nondipolar transitions reaching the strong-coupling regime (i.e., near-unity transition probabilities). We demonstrate that the final state of the Rydberg atom consists of energy and angular-momentum superpositions that are strongly dependent on the e-beam energy and impact parameter (distance to the atom), thus enabling the coherent control of individual atoms. Through interaction with a periodic train of free electrons, precise transition frequencies are selected, corresponding to the delay between consecutive electrons. A wide range of final atomic states, including entanglement among two or more Rydberg atoms, is reached by using laterally shaped electron waves followed by electron postselection. Our results highlight appealing capabilities of e-beams for manipulating quantum systems based on Rydberg atoms in unprecedented ways using currently available state-of-the-art techniques.

## II. RESULTS

## A. Theoretical framework

We describe the electron as a classical point particle following a straight-line trajectory with a constant velocity vector v (nonrecoil approximation [33]), as illustrated in Fig. 1a. This approach is justified under the assumption that the e-beam is focused laterally down to a small diameter (e.g., &lt; 1 nm in transmission electron miscroscopes) compared to the size of the Rydberg atom (e.g., ∼ 5 -500 nm for principal quantum numbers n = 5 -50). In addition, the excitation probability is known to be independent of the electron wave function along the e-beam direction [34], which justifies treating the electron as a classical point particle to make theory simple. The moving electron introduces an external electromagnetic field that acts on the Rydberg atom, and we study their quantummechanical interaction by adopting the minimal coupling prescription [52] and neglecting A 2 terms. Then, the Hamiltonian of the system reduces to ˆ H ( r , t ) = ˆ H 0 ( r ) + ˆ H 1 ( r , t ), where ˆ H 0 ( r ) = -( ℏ 2 / 2 m e ) ∇ 2 + V ( r ) describes the Rydberg electron in a Coulomb-like core potential V ( r ) while ˆ H 1 ( r , t ) = -(i e ℏ / 2 m e c ) ∇ · A ( r , t ) + A ( r , t ) · ∇ -e ϕ ( r , t ) accounts for the perturbation produced by the swift electron through the vector and scalar potentials A and ϕ . Writing the electron trajectory as r 0 ( t ) = R 0 + v t (with R 0 ⊥ v ) and its associated electric field as E ( r , t ) = -(1 / c ) ∂ t A ( r , t ) -∇ ϕ ( r , t ), we have the potentials [53]

FIG. 1. Interaction of Rydberg atoms with electron beams. (a) The interaction of a Rydberg atom with a free electron moving along a straight line and passing at a position R 0 from the nucleus (impact parameter) can drive transitions between initial and final states, | ni , l i , mi ⟩ and | nf , l f , mf ⟩ , respectively. (b) Transition dipole moment d = e ⟨ ni , 0 , 0 | r | nf , 1 , 1 ⟩ (in units of ea 0) associated with dipolar transitions in the Rydberg atom as a function of initial principal quantum number ni for different values of ∆ n = nf -ni (see color legend). The inset shows results for | ni , l i , 0 ⟩ → | ni + 1 , l i + 1 , 1 ⟩ transitions with a wide range of l i values. (c) Impact-parameter dependence of the probability of | 10 , 5 , 5 ⟩ → | 11 , 5 + ∆ l , 5 + ∆ m ⟩ transitions for different values of ∆ l and ∆ m as produced by interaction with a 10 eV electron. First-order matrix-element calculations (solid curves) are compared to the large-| R 0 | scaling ∝ K 2 | ∆ m | ( | ε f i | R 0 / v ) with ℏ ε f i = (1 / n 2 i -1 / n 2 f ) Ry (dashed curves). A vertical broken line indicates the atomic radius Rn = n 2 a 0 with n = 10 and a 0 the Bohr radius.

<!-- image -->

$$\phi ( { \mathbf r } , t ) = - \frac { e \gamma } { \sqrt { | R - R _ { 0 } | ^ { 2 } + \gamma ^ { 2 } ( { \mathbf r } \cdot \hat { v } - v t ) ^ { 2 } } } ,$$

and A ( r , t ) = ( v / c ) ϕ ( r , t ), where γ = (1 -v 2 / c 2 ) -1 / 2 is the Lorentz factor. In what follows, we consider low-energy electrons ( v ≪ c ), so we approximate γ ≈ 1 and neglect the effect of the vector potential.

In general, the wave functions of the Rydberg states can be calculated analogously to those of the hydrogen atom using the so-called quantum defect theory [54], where the differences between the Coulomb potential of the proton in hydrogen and the actual potential experienced by a Rydberg electron are conveniently encapsulated in a species-dependent model potential with empirical parameters [1, 54, 55]. For simplicity, in this work, we consider Rydberg states described by hydrogenic wave functions ψ i ( r ) and neglect fine and hyperfine structure effects [56], so they satisfy ˆ H 0 ( r ) ψ i ( r , t ) = ℏ ε i ψ i ( r , t ) with V ( r ) = -e 2 / r and eigenenergies ℏ ε i = ( -1 / n 2 i ) Ry expressed in terms of the Bohr radius a 0. Here, i ≡ ( ni , l i , mi ) encapsulates the principal, angular, and azimuthal quantum numbers. Hydrogenic states form a complete orthonormal basis set, and therefore, the time-dependent wave function can be expanded as ψ ( r , t ) = P i α i ( t ) ψ i ( r ) e -i ε i t , where the expansion coeffi- cients α i ( t ) satisfy the equation of motion

$$\dot { \alpha } _ { i } ( t ) = - \frac { \mathbf i } { \hbar { } } \sum _ { j \neq i } e ^ { i \varepsilon _ { i j } t } \, M _ { i j } ( t ) \, \alpha _ { j } ( t ) \quad \ \ ( 1 )$$

with energy differences ε i j = ε i -ε j and Mij ( t ) and transition matrix elements defined by Mij ( t ) = R d 3 r ψ ∗ i ( r ) ˆ H 1 ( r , t ) ψ j ( r ) (Fig. 1a). [See Appendix A for details on the solution of Eq. (1).] This formalism can be straightforwardly applied to Rydberg electron wave functions resulting from more complex phenomenological core potentials V ( r ) [1, 54, 57].

## B. Interaction of a free electron with a Rydberg atom

Before solving the full dynamics described by Eq. (1), it is instructive to examine the interaction within first-order perturbation theory, where the transition probability becomes

$$\begin{array} { r l } & { y \text { elect-} } \\ & { \text {effect} } & { P _ { i \to f } ^ { ( 1 ) } = \frac { 1 } { \hbar { ^ } { 2 } } \left | \int _ { - \infty } ^ { \infty } d t \, e ^ { i \varepsilon _ { f } t } M _ { f i } ( t ) \right | ^ { 2 } } \\ & { \text {can be} } & { \quad } \\ & { \text {ing the} } & { = \left ( \frac { 2 e ^ { 2 } } { \hbar { v } } \right ) ^ { 2 } \left | \int _ { - \infty } ^ { \infty } d ^ { 3 } r \, \psi _ { f } ^ { * } ( r ) \, \psi _ { i } ( r ) \, e ^ { i \varepsilon _ { f } r \cdot v / 2 } K _ { 0 } \left ( \frac { | \varepsilon _ { f i } | | R - R _ { 0 } | } { v } \right ) \right | ^ { 2 } . } \end{array}$$

The electric dipole moment of a highly excited Rydberg atom exhibits a ∝ n 2 scaling with the principal quantum number, reaching large values for n ≫ 1 (Fig. 1b). In the dipolar limit (i.e., for e-beams passing far away from the atom, so that the interaction is dominated by dipolar transitions), the probability reduces to [33, 34]

$$\begin{array} { r l } { s e d } & P _ { i \to f } ^ { ( 1 ) } = \left ( \frac { 2 e \varepsilon _ { f i } } { \hbar { v } ^ { 2 } } \right ) ^ { 2 } \left [ | d _ { f i , x } | ^ { 2 } K _ { 1 } ^ { 2 } \left ( \frac { | \varepsilon _ { f i } | b } { v } \right ) + | d _ { f i , z } | ^ { 2 } K _ { 0 } ^ { 2 } \left ( \frac { | \varepsilon _ { f i } | b } { v } \right ) \right ] , \ ( 2 ) } \end{array}$$

where dfi , x and dfi , z denote Cartesian components of the transition dipole moment d f i = -e R d 3 r ψ ∗ f ( r ) r ψ i ( r ), and we take the electron trajectory as r 0 ( t ) = b ˆ x + vt ˆ z . For small arguments of the modified Bessel functions Km (i.e., | ε f i | b / v ≪ 1), the electron primarily couples to the dfi , x component (perpendicular to the e-beam), and the associated transition probabilities asymptotically approach a constant value for large principal quantum numbers ni (see Supplementary Fig. A): even though dfi , x ∝ n 2 i , the orbital radius of the Rydberg electron also increases as ∝ n 2 i , and thus, in the dipolar regime ( b ≫ ⟨ r ⟩ ), the increase in dipole-moment strength is compensated by the increase in impact parameter b . Therefore, a strong electronRydberg-atom interaction requires e-beams penetrating the inner region of the Rydberg atom (i.e., overlapping with the wave functions of the Rydberg electron). Indeed, Fig. 1c shows that free electrons can not only induce several types of multipolar transitions but they can also strongly couple to Rydberg atoms with near-unity probability for suitable choices of the impact parameters within the orbital radius of the Rydberg electron.

## C. Strong electron-atom coupling

The conditions for which strong electron-atom coupling is produced can be hinted by examining Eq. (2): because the probability scales as 1 / v 2 at large impact parameters, lowering the energy of the e-beam naturally leads to stronger coupling. Moreover, the probability diverges as 1 / b 2 near b = 0, so we are led to explore regions close to the nucleus of the Rydberg atom to make the initial and final wave functions maximally overlap with the trajectory of the e-beam.

In Fig. 2, we illustrate some conditions for which strong coupling is attained. In particular, we study the interaction as a function of impact parameter b for e-beams moving either parallel (Fig. 2a-c) or perpendicular (Fig. 2d-f) to the quantization axis (here chosen to be z ). In Fig. 2a,d, we focus on transitions of the form | n , n -1 , n -1 ⟩ → | n + 1 , n , n ⟩ (i.e., involving circular states [58]) within first-order in the electronatom interaction, which reveals a dramatic dependence on the orientation of the e-beam. This dependence includes the presence of a maximum of the transition probability as a function of impact parameter for v parallel to the quantization axis, in contrast to a monotonic decrease with increasing b for the perpendicular orientation. The position of the noted maximum, which scales as b ∝ n 2 , corresponds to the largest overlap of the e-beam with the involved Rydberg orbitals. In addition, increasing the principal quantum number roughly enhances the calculated transition probability in the parallel configuration (but with a weaker increase for n ≳ 30). In contrast, a reduction in the coupling is observed for the perpendicular e-beam as n increases.

A more quantitative measure of strong coupling is provided by the probability of depleting the initial atomic state after the passage of the electron. The transition probability calculated to first-order in the interaction already shows pronounced maxima with values well above unity (Supplementary Fig. A), indicating that we are entering a nonpertubative regime. When calculated to all orders of interaction (Fig. 2b,e), we observe regions of nearly 100% depletion (see black dots in Fig. 2b,e). We note that these high values of the total transition probability indicate that the final state of the atom is orthogonal to the initial state. This observation is important for the entanglement applications discussed below.

The presence of strong initial-state depletion is accompanied by maxima of the transition probability to other states. In particular, for | 5 , 4 , 4 ⟩ → | 6 , 5 , 5 ⟩ transitions (Fig. 2c,f), we observe absolute maxima at b ∼ 1 -2 nm, reaching values of ≈ 16% and ≈ 19% (with ≈ 12 eV and ≈ 3 eV kinetic energy) for the parallel and perpendicular e-beam orientations, respectively. The impact parameter and energy position of the transition maxima depend on the final state, as shown in Supplementary Fig. A, where we examine other elastic and inelastic transitions of dipolar and quadrupolar nature.

## D. Multipolar transitions enabled by swift electrons

In contrast to the interaction with far-field light, which can only produce transitions subject to the dipolar selection rules, the electromagnetic field displayed by the moving electron contains highly nondipolar components that can induce transitions beyond those accessible with light. This effect is more dramatic when the free electron overlaps with the electronic orbitals. In addition, the electron can be regarded as a broadband source that can produce multiple transitions simultaneously, including an intrashell redistribution of the bound Rydberg electron.

Figure 3 showcases the multipolar character of the Rydberge-beam interaction by showing the distribution of final state probabilities produced by a 10 eV electron interacting with a Rydberg atom prepared in different ni = 8 states. We present results calculated to all orders of scattering for electrons traversing the atom (Fig. 3a,d), passing right at the Rydberg radius (Fig. 3b,e), or well outside the atom (Fig. 3c,f). For every panel in the figure, each pixel corresponds to the transition to a given final state | nf , l f , mf ⟩ when the atom is prepared in a state | 8 , l i , mi ⟩ , so we organize the horizontal (initial state) and vertical (final state) axes following a normal ordering using the l - and m -dependent combined index l 2 + l + m . For the neighboring energy transitions ni = 8 → nf = 9 and distances outside the electron cloud (Fig. 3f), the largest contribution comes from dipolar transitions, as we are within the range of validity of the dipolar limit. In contrast, for impact parameters at and below the Rydberg radius (Fig. 3d,e), nondipolar processes become important.

Interestingly, elastic transitions (i.e., with nf = ni ) are also prominent (see Fig. 3a-c). These transitions, which cannot be accessed using a single laser source, are analogous to hybridization due to the Stark effect in the presence of a dynamical electric field (i.e., the one provided by the moving electron). Although the electron energy is preserved, we note that the electron can impart a change in angular momentum to the atom, and therefore, momentum conservation is expected to produce electron deflection, which could be exploited to reveal the presence of these types of transitions.

Incidentally, the e-beam trajectory considered in Fig. 3 is parallel to the quantization axis, but symmetry could be exploited to suppress or enhance specific transitions depending on e-beam orientation.

FIG. 2. Strong-coupling regime. Transition probabilities calculated for the e-beam configurations depicted in the insets of panels (a) and (d): velocity and impact parameter v = v ˆ z and R 0 = b ˆ x in (a-c), and v = v ˆ x and R 0 = b ˆ z in (d-f). The quantization axis is z in all cases. (a,d) Impact-parameter dependence of the linear-order probability for transitions | n , n -1 , n -1 ⟩ → | n + 1 , n , n ⟩ [i.e., between circular states n ◦ and ( n + 1) ◦ ] produced by free electrons of energies of 10 eV (solid curves), 100 eV (dashed curves), and 1 keV (dotted curves). (b,c,e,f) Depletion probability of an initial state | 5 , 4 , 4 ⟩ (b,e) and probability of ending in a final state | 6 , 5 , 5 ⟩ (c,f) calculated to all orders of interaction as a function of impact parameter and electron kinetic energy. Black dots in (b,e) indicate local maxima of the depletion probability.

<!-- image -->

## E. Multiple electrons

The interaction with a single electron produces a wide distribution of final states. This effect becomes more dramatic as we approach strong-coupling conditions by reducing the free-electron energy, as illustrated in Fig. 4a, starting in the | 11 , 10 , 10 ⟩ state and reaching the strong coupling regime for energies lower than ∼ 10 eV, where the initial state is depleted in favor of an increase in the population of adjacent energy levels. Interestingly, oscillations in the initial state population are observed at lower energies. This effect is a signature of coherent quantum dynamics. This example illustrates that we lack selectivity over the final state energy when using a single free electron.

Given the long optical periods associated with transitions in Rydberg atoms, we argue that ultrashort electron pulses (e.g., sub-ps wave packets such as those available in ultrafast electron microscopy [42, 59]) have small durations compared with such periods and, therefore, act as point particles. By sending a periodic sequence of N electrons (e.g., values of N = 1 -4 have already been demonstrated in experiment [60]) separated by well-defined intervals of duration t e, the proba- bility of a weak atomic transition can be enhanced by a factor N 2 relative to that of a single electron under the condition that ε f i t e is a multiple of 2 π . This is the so-called superradiance effect [61-64], illustrated for Rydberg atoms in Figs. 4b and 4c for off- and on-resonance conditions. In analogy to optical excitation by successive laser pulses, the approach explored in Fig. 4c offers a way of synthesizing highly excited Rydberg atoms by employing relatively energetic electrons (far from the strong-coupling regime), whose arrival times are engineered to successively excite the system until the desired state is reached.

## F. Using free electrons to produce quantum entanglement

Considering the large size of Rydberg atoms (radius 5 . 3132 nm for principal quantum numbers 10-50) compared to the electron wavelength (1 . 2-0 . 039 nm at 1-10 3 eV), it is physically possible to laterally focus the e-beam to form spots of small width compared to the extension of the electronic orbitals under consideration. Through the use of e-beam biprisms [65, 66] or diffraction gratings [67, 68], the electron wave function can be made to consist of multiple paths, sepa- rated by lateral distances up to several microns. In particular, we consider a two-path e-beam arranged as depicted in Fig. 5 relative to the Rydberg atom. Each of the electron paths (associated with states | A ⟩ and | B ⟩ ) produces a different final state of the atom (left and right, | L ⟩ and | R ⟩ ), so the postinteraction state of the system is entangled: | A ′ ⟩ ⊗ | L ⟩ + | B ′ ⟩ ⊗ | R ⟩ (Fig. 5a), where the prime indicates the change produced in the electron along each path due to the interaction.

FIG. 3. Multipolar excitations. Excitation probability produced by a 10 eV electron ( v parallel to the quantization axis z ) and calculated to all orders of interaction for impact parameters b = R 8 / 2, R 8 , and 2 R 8 (left, middle, and right panels), where R 8 ≈ 3 . 4 nm is the Rydberg radius for a fixed initial principal quantum number ni = 8. Results are shown for final states with nf = 8 (a-c) and nf = 9 (d-f). In each panel, the horizontal axis runs over initial quantum numbers l i and mi , each requiring a separate simulation starting from a state | 8 , l i , mi ⟩ . The vertical axes run over final quantum numbers l f and mf . States are organized consecutively along the axes using the combined index l 2 + l + m . Vertical and horizontal gray lines are introduced to separate rectangular areas corresponding to fixed l i and l f values.

<!-- image -->

An interesting scenario is presented when which-way information is erased through electron postselection [69]. This can be realized by coupling each of the paths to a common single output channel. For example, if the two paths are produced by diffraction in a transmission grating, a second conjugated grating can be placed at a suitable position in which the two paths have diverged sufficiently to overlap with each other in space, such that they are both diffracted to a common Bragg beam [67, 68]. Obviously, electrons transmitted in that beam do not contain which-way information (because of the conjugation between angles of propagation of the two paths), and therefore, the detection of an electron within the angular range spanned by this beam should herald a final atomic state | L ⟩ + | R ⟩ (Fig. 5b).

Leveraging these tools of e-beam splitting, projection, and postselection, in combination with state-of-the-art atomic optical trapping, one can produce entanglement among two or more Rydberg atoms by making the electron paths interact with them. For the in-series interaction with two atoms depicted in Fig. 5c, the A path produces left states on both of the atoms, whereas the B path induces right states. Upon detection of a postselected electron in the which-way -eraser configuration discussed above, the atomic system is finally prepared in an entangled state | L 1 ⟩ ⊗ | L 2 ⟩ + | R 1 ⟩ ⊗ | R 2 ⟩ , where the subindices label the two atoms.

FIG. 4. Tayloring the final Rydberg atom state with a periodic train of electrons. (a) Probability of finding the Rydberg atom with a final quantum number nf for an initial state | 11 , 10 , 10 ⟩ after interaction with a free electron moving parallel to the quantization axis z at an impact parameter b ≈ 7 . 01 nm. The vertical axis runs over the incident electron energy. A broader range of nf 's is observed as the electron energy is reduced. (b,c) Temporal evolution of a Rydberg atom prepared in an initial state | 5 , 4 , 4 ⟩ during the interaction with an e-beam consisting of a large number N ≫ 1 of 100 eV electrons separated by a constant time difference (b) t e = 0 . 01 π/ε 65 and (c) t e = 2 π/ε 65 (i.e., off- and on-resonance with ni = 5 → nf = 6 transitions, respectively).

<!-- image -->

FIG. 5. Quantum entanglement with free electrons and Rydberg atoms. (a) An electron prepared in a two-path state ( | A ⟩ and | B ⟩ ) can interact with a Rydberg atom and create left and right final states ( | L ⟩ and | R ⟩ ). After the interaction, the electron-atom system is placed in an entangled state | A ′ ⟩ ⊗ | L ⟩ + | B ′ ⟩ ⊗ | R ⟩ , where the primes indicate that the electron is also modified due to the interaction in each path. (b) Upon postselection of the electron considered in (a), such that one collects the contribution transmitted from both paths to a single output channel, and which-way information is erased, the atom is left in a superposition state | L ⟩ + | R ⟩ . (c) After the passage of the two-path electron through two noninteracting atoms arranged in an in-series configuration, followed by electron postselection, the atomic system is left in an entangled state | L 1 ⟩ ⊗ | L 2 ⟩ + | R 1 ⟩ ⊗ | R 2 ⟩ , where the subindices refer to atoms 1 and 2. (d) For two atoms in the depicted in-parallel configuration, an atomic state | L 1 ⟩ ⊗ | I 2 ⟩ + | I 1 ⟩ ⊗ | L 2 ⟩ is obtained, where | I j ⟩ denotes the initial state of atom j .

<!-- image -->

Analogously, in an in-parallel atomic configuration (Fig. 5d) with paths A and B passing on the left of atoms 1 and 2, respectively, electron postselection leads to a final atomic state | L 1 ⟩ ⊗ | I 2 ⟩ + | I 1 ⟩ ⊗ | L 2 ⟩ , where | I j ⟩ denotes the initial state of atom j = 1 , 2. We recall that a single electron can deplete the initial state of the atom (see Fig. 2), and therefore, for a suitable combination of electron energy and impact parameter, we can have orthogonal states satisfying ⟨ I j | Lj ⟩ = 0.

## III. DISCUSSION

We have presented an unexplored approach for manipulating the states of Rydberg atoms through their interaction with e-beams. In particular, we have theoretically shown that low- energy free electrons are capable of producing unity-order changes in the state of a Rydberg electron, including a complete depletion of the initial atomic state after interaction with a single free electron, as well as a large contribution of optically forbidden nondipolar transitions on par with (or even exceeding) dipolar ones. Because the de Broglie wavelength of the free electron is small compared with the size of Rydberg orbitals for the kinetic energies under consideration, the ebeam can be regarded as a line-like dipolar excitation oriented along the electron velocity direction [33]. In practice, currently avaiplable electron optics methods enable the focusing of feweV electrons down to few-nm lateral sizes (e.g., in low-energy electron microscopes [70, 71]). In addition, for high principal quantum numbers, the optical periods associated with the generated atomic transitions are large (e.g., picoseconds for ni , nf &gt; 10) compared to the duration of the photoemitted elec- tron pulses available in ultrafast electron microscopes [42, 59], and thus, electrons prepared as short pulses can be regarded as classical point particles in their interaction with Rydberg atoms, amenable to synchronization with high temporal precision relative to the transition optical period. In our study, we consider the atom to be placed at a well-defined spatial position (e.g., trapped in an optical lattice).

These considerations foresay a high degree of selectivity over the resulting final atomic state by playing with the electron kinetic energy, the time of interaction, and the e-beam arrangement relative to the atom. For example, we have shown that trains of electrons can be used to maximize the transition probability for designated transition energies. In addition, the predicted strong electron-atom coupling can be controllable through the e-beam parameters.

As an appealing opportunity opened by the interaction between controlled e-beams and Rydberg atoms, we argue that quantum entanglement between the electron and the atom can be achieved by laterally splitting the electron wave function into different paths, following electron-wave manipulation methods developed in the context of electron holography [66]. Moreover, projection and postselection of the electron enable the generation of entangled atom pairs and, more generally, atomic ensembles. This approach to multiatom entanglement exceeds the capabilities of laser-based far-field optics and could potentially be employed to obtain complex on-demand fewbody states in a selection of a given number of Rydberg atoms.

In brief, free electrons constitute an appealing tool to manipulate Rydberg atoms with capabilities that exceed those of far-field optical methods, such as the induction of nondipolar transitions, the synthesis of complex final atomic states, the control of such states through the energy and spatial profile of the free electrons, and the generation of entanglement between the electron and the atom as well as among two or more atoms traversed by the electron.

## Appendix A

We solve Eq. (1) by direct time integration using the nonretarded ( c →∞ ) matrix elements

$$M _ { i j } ( t ) = e ^ { 2 } \int d ^ { 3 } r \, \frac { \psi _ { i } ^ { * } ( r ) \, \psi _ { j } ( r ) } { | r - r _ { 0 } ( t ) | } \quad ( S 1 )$$

associated with | nj , l j , mj ⟩ → | ni , l i , mi ⟩ transitions produced by an electron following a trajectory given by r = r 0 ( t ). These elements admit analytical expressions when using real-space hydrogenic wave functions

$$\psi _ { n , l , m } ( r ) & = \langle r | n , l , m \rangle \\ & = \sqrt { \left ( \frac { 2 } { n a _ { 0 } } \right ) ^ { 3 } \frac { ( n - l - 1 ) ! } { 2 n ( n + l ) ! } e ^ { - r / n a _ { 0 } } \left ( \frac { 2 r } { n a _ { 0 } } \right ) ^ { l } L _ { n - l - 1 } ^ { 2 l + 1 } \left ( \frac { 2 r } { n a _ { 0 } } \right ) Y _ { l , m } ( \Omega _ { \uparrow } ) , }$$

where L β α are generalized Laguerre polynomials and Yl , m are spherical harmonics satisfying the orthogonality relation R d 2 Ω Y ∗ lm ( Ω ) Yl ′ m ′ ( Ω ) = δ ll ′ δ mm ′ . More precisely, expanding the generalized Laguerre polynomials into powers of r , we can write ψ ∗ i ( r ) ψ j ( r ) = e -gr P k Akr k using a finite number of coefficients Ak indexed by integers k and defining g = (1 / ni + 1 / nj ) / a 0. Inserting this expression into Eq. (S1) together with the expansion 1 / | r -r 0 | = 4 π P ∞ l = 0 P l m = -l (2 l + 1) -1 r l &lt; / r l + 1 &gt; Ylm ( Ω r ) Y ∗ lm ( Ω r 0 ) for the Coulomb interaction, where r &gt; = max { r , r 0 } and r &lt; = min { r , r 0 } , we finally obtain

$$M _ { i j } ( t ) = 4 \pi e ^ { 2 } \sum _ { k l m } \frac { A _ { k } } { 2 l + 1 } \, B _ { l m , l _ { 1 } m _ { 1 } , l m } \, C _ { k l } ( g , r _ { 0 } ) \, Y _ { l m } ^ { * } ( \Omega _ { r _ { 0 } } ) , \\$$

where the angular integral Blm , l ′ m ′ , l ′′ m ′′ = R d 2 Ω Y ∗ lm ( Ω ) Yl ′ m ′ ( Ω ) Yl ′′ m ′′ ( Ω ) can be expressed in terms of Clebsch-Gordan coefficients [72], while the radial integral yiels

$$C _ { k , l } ( g , r _ { 0 } ) & = \int _ { 0 } ^ { \infty } d r e ^ { - g r } r ^ { k } \, \frac { r _ { < } ^ { l } } { r _ { > } ^ { l + 1 } } \\ & = \frac { 1 } { g ^ { k } } \left [ ( g r _ { 0 } ) ^ { - l - 1 } \, \gamma ( k + l + 1 , g r _ { 0 } ) + ( g r _ { 0 } ) ^ { l } \, \Gamma ( k - l , g r _ { 0 } ) \right ]$$

in terms of the incomplete and lower-incomplete gamma functions [73] Γ ( α, z ) and γ ( α, z ).

## REFERENCES

- [1] T. F. Gallagher, Rydberg Atoms , Cambridge Monographs on Atomic, Molecular and Chemical Physics (Cambridge University Press, Cambridge, 1994).
- [2] M. Saffman, T. G. Walker, and K. Mølmer, Rev. Mod. Phys. 82 , 2313 (2010).
- [3] T. M. Graham, M. Kwon, B. Grinkemeyer, Z. Marra, X. Jiang, M. T. Lichtman, Y. Sun, M. Ebert, and M. Saffman, Phys. Rev. Lett. 123 , 230501 (2019).
- [4] H. Levine, A. Keesling, G. Semeghini, A. Omran, T. T. Wang, S. Ebadi, H. Bernien, M. Greiner, V. Vuleti´ c, H. Pichler, and M. D. Lukin, Phys. Rev. Lett. 123 , 170503 (2019).
- [5] C. S. Adams, J. D. Pritchard, and J. P. Shaffer, J. Phys. B 53 , 012002 (2019).
- [6] A. Browaeys and T. Lahaye, Nat. Phys. 16 , 132 (2020).
- [7] H. Labuhn, D. Barredo, S. Ravets, S. De Léséleuc, T. Macrì, T. Lahaye, and A. Browaeys, Nature 534 , 667 (2016).
- [8] H. Bernien, S. Schwartz, A. Keesling, H. Levine, A. Omran, H. Pichler, S. Choi, A. S. Zibrov, M. Endres, M. Greiner, V. Vuleti´ c, and M. D. Lukin, Nature 551 , 579 (2017).
- [9] H. Weimer, M. Müller, I. Lesanovsky, P. Zoller, and H. P. Büchler, Nat. Phys. 6 , 382 (2010).
- [10] S. De Léséleuc, V. Lienhard, P. Scholl, D. Barredo, S. Weber, N. Lang, H. P. Büchler, T. Lahaye, and A. Browaeys, Science 365 , 775 (2019).
- [11] P. Scholl, M. Schuler, H. J. Williams, A. A. Eberharter, D. Barredo, K.-N. Schymik, V. Lienhard, L.-P. Henry, T. C. Lang, T. Lahaye, A. M. Läuchli, and A. Browaeys, Nature 595 , 233 (2021).
- [12] S. Ebadi, T. T. Wang, H. Levine, A. Keesling, G. Semeghini, A. Omran, D. Bluvstein, R. Samajdar, H. Pichler, W. W. Ho, S. Choi, S. Sachdev, M. Greiner, V. Vuleti´ c, and M. D. Lukin, Nature 595 , 227 (2021).
- [13] M. Saffman and T. G. Walker, Phys. Rev. A 72 , 022347 (2005).
- [14] I. I. Beterov, I. I. Ryabtsev, D. B. Tretyakov, and V. M. Entin, Phys. Rev. A 79 , 052504 (2009).

- [15] C. Hölzl, A. Götzelmann, E. Pultinevicius, M. Wirth, and F. Meinert, Phys. Rev. X 14 , 021024 (2024).
- [16] M. D. Lukin, M. Fleischhauer, R. Cote, L. M. Duan, D. Jaksch, J. I. Cirac, and P. Zoller, Phys. Rev. Lett. 87 , 037901 (2001).
- [17] E. Urban, T. A. Johnson, T. Henage, L. Isenhower, D. D. Yavuz, T. G. Walker, and M. Saffman, Nat. Phys. 5 , 110 (2009).
- [18] A. Gaëtan, Y. Miroshnychenko, T. Wilk, A. Chotia, M. Viteau, D. Comparat, P. Pillet, A. Browaeys, and P. Grangier, Nat. Phys. 5 , 115 (2009).
- [19] L. Isenhower, E. Urban, X. L. Zhang, A. T. Gill, T. Henage, T. A. Johnson, T. G. Walker, and M. Saffman, Phys. Rev. Lett. 104 , 010503 (2010).
- [20] T. Wilk, A. Gaëtan, C. Evellin, J. Wolters, Y. Miroshnychenko, P. Grangier, and A. Browaeys, Phys. Rev. Lett. 104 , 010502 (2010).
- [21] A. V. Gorshkov, J. Otterbach, M. Fleischhauer, T. Pohl, and M. D. Lukin, Phys. Rev. Lett. 107 , 133602 (2011).
- [22] T. Peyronel, O. Firstenberg, Q.-Y. Liang, S. Hofferberth, A. V. Gorshkov, T. Pohl, M. D. Lukin, and V. Vuletic, Nature 488 , 57 (2012).
- [23] O. Firstenberg, T. Peyronel, Q.-Y. Liang, A. V. Gorshkov, M. D. Lukin, and V. Vuleti´ c, Nature 502 , 71 (2013).
- [24] D. Barredo, S. de Léséleuc, V. Lienhard, T. Lahaye, and A. Browaeys, Science 354 , 1021 (2016).
- [25] P. Schauß, M. Cheneau, M. Endres, T. Fukuhara, S. Hild, A. Omran, T. Pohl, C. Gross, S. Kuhr, and I. Bloch, Nature 491 , 87 (2012).
- [26] W. S. Bakr, J. I. Gillen, A. Peng, S. Fölling, and M. Greiner, Nature 462 , 74 (2009).
- [27] J. F. Sherson, C. Weitenberg, M. Endres, M. Cheneau, I. Bloch, and S. Kuhr, Nature 467 , 68 (2010).

[28]

K. D. Nelson, X. Li, and D. S. Weiss, Nat. Phys.

[3](http://dx.doi.org/10.1038/nphys645)

[, 556 (2007).](http://dx.doi.org/10.1038/nphys645)

- [29] C. B. O. Mohr and F. H. Nicoll, Proc. R. Soc. London, Ser. A 144 , 596 (1934).
- [30] D. Rapp and P. Englander-Golden, J. Chem. Phys. 43 , 1464 (1965).
- [31] H. Tanaka, M. Hoshino, and M. J. Brunger, Eur. Phys. J. D 75 , 293 (2021).
- [32] F. J. García de Abajo, E. J. C. Dias, and V. Di Giulio, Phys. Rev. Lett. 129 , 093401 (2022).
- [33] [F. J. García de Abajo, Rev. Mod. Phys. 82 , 209 (2010).](http://dx.doi.org/10.1103/RevModPhys.82.209)
- [34] F. J. García de Abajo and V. Di Giulio, ACS Photonics 8 , 945 (2021).
- [35] T. Gericke, P. Würtz, D. Reitz, T. Langen, and H. Ott, Nat. Phys. 4 , 949 (2008).
- [36] T. L. P. Würtz, T. Gericke, A. Koglbauer, and H. Ott, Phys. Rev. Lett. 103 , 080404 (2009).
- [37] T. Manthey, T. M. Weber, T. Niederprüm, P. Langer, V. Guarrera, G. Barontini, and H. Ott, New J. Phys. 16 , 083034 (2014).
- [38] J. B. Balewski, A. T. Krupp, A. Gaj, D. Peter, H. P. Büchler, R. Löw, S. Hofferberth, and T. Pfau, Nature 502 , 664 (2013).
- [39] F. J. García de Abajo and A. Koneˇ cná, Phys. Rev. Lett. 126 , 123901 (2021).
- [40] M. C. C. Mihaila, P. Weber, M. Schneller, L. Grandits, S. Nimmrichter, and T. Juffmann, Phys. Rev. X 12 , 031043 (2022).
- [41] B. Barwick, D. J. Flannigan, and A. H. Zewail, Nature 462 , 902 (2009).
- [42] A. Feist, K. E. Echternkamp, J. Schauss, S. V. Yalunin, S. Schäfer, and C. Ropers, Nature 521 , 200 (2015).
- [43] K. E. Priebe, C. Rathje, S. V. Yalunin, T. Hohage, A. Feist, S. Schäfer, and C. Ropers, Nat. Photon. 11 , 793 (2017).
- [44] O. Reinhardt and I. Kaminer, ACS Photonics 7 , 2859 (2020).
- [45] S. V. Yalunin, A. Feist, and C. Ropers, Phys. Rev. Research 3 , L032036 (2021).
- [46] Q. Guo, R. Yu, C. Li, S. Yuan, B. Deng, F. J. García de Abajo, and F. Xia, Nat. Mater. 17 , 986 (2018).
- [47] A. Koneˇ cná and F. J. García de Abajo, Phys. Rev. Lett. 125 , 030801 (2020).
- [48] I. Madan, V. Leccese, A. Mazur, F. Barantani, T. LaGrange, A. Sapozhnik, P. M. Tengdin, S. Gargiulo, E. Rotunno, J.-C. Olaya, I. Kaminer, V. Grillo, F. J. García de Abajo, F. Carbone, and G. M. Vanacore, ACS Photonics 9 , 3215 (2022).
- [49] A. P. Synanidis, P. A. D. Gonçalves, C. Ropers, and F. J. García de Abajo, Sci. Adv. 10 , eadp4096 (2024).
- [50] J. Verbeeck, A. Béché, K. Müller-Caspary, G. Guzzinati, M. A. Luong, and M. D. Hertog, Ultramicroscopy 190 , 58 (2018).
- [51] C.-P. Yu, F. Vega Ibañez, A. Béché, and J. Verbeeck, SciPost Phys. 15 , 223 (2023).
- [52] J. J. Sakurai, Modern Quantum Mechanics (Addison-Wesley, Boston, 1994).
- [53] J. D. Jackson, Classical Electrodynamics (Wiley, New York, 1975).
- [54] [M. J. Seaton, Rep. Prog. Phys. 46 , 167 (1983).](http://dx.doi.org/10.1088/0034-4885/46/2/002)
- [55] M. Marinescu, H. R. Sadeghpour, and A. Dalgarno, Phys. Rev. A 49 , 982 (1994).
- [56] F. Laloë, B. Diu, and C. Cohen-Tannoudji, Quantum Mechanics, Volume 2 (Wiley, Paris, 2005).
- [57] N. Šibali´ c, J. Pritchard, C. Adams, and K. Weatherill, Comput. Phys. Commun. 220 , 319 (2017).
- [58] R. G. Hulet and D. Kleppner, Phys. Rev. Lett. 51 , 1430 (1983).
- [59] L. Piazza, T. T. A. Lummen, E. Quiñonez, Y. Murooka, B. Reed, B. Barwick, and F. Carbone, Nat. Commun. 6 , 6407 (2015).
- [60] R. Haindl, A. Feist, T. Domröse, M. Möller, J. H. Gaida, S. V. Yalunin, and C. Ropers, Nat. Phys. 19 , 1410 (2023).
- [61] J. Urata, M. Goldstein, M. F. Kimmitt, A. Naumov, C. Platt, and J. E. Walsh, Phys. Rev. Lett. 80 , 516 (1998).
- [62] A. Gover, R. Ianconescu, A. Friedman, C. Emma, N. Sudar, P. Musumeci, and C. Pellegrini, Rev. Mod. Phys. 91 , 035003 (2019).
- [63] [A. Gover and A. Yariv, Phys. Rev. Lett. 124 , 064801 (2020).](http://dx.doi.org/10.1103/PhysRevLett.124.064801)
- [64] V. Di Giulio, O. Kfir, C. Ropers, and F. J. García de Abajo, ACS Nano 15 , 7290 (2021).
- [65] G. Möllenstedt and H. Düker, Z. Phys. 145 , 377 (1956).
- [66] D. Shindo, T. Tanigaki, and H. S. Park, Adv. Mater. 29 , 1602216 (2017).
- [67] C. W. Johnson, A. E. Turner, and B. J. McMorran, Phys. Rev. Research 3 , 043009 (2021).
- [68] C. W. Johnson, A. E. Turner, F. J. García de Abajo, and B. J. McMorran, Phys. Rev. Lett. 128 , 147401 (2022).
- [69] [J.-W. Henke, H. Jeng, and C. Ropers, 'Quantum eraser experiments for the demonstration of entanglement between swift electrons and light,' (2024), arXiv:2404.11368.](http://dx.doi.org/10.48550/arXiv.2404.11368)
- [70] [E. Bauer, Rep. Prog. Phys. 57 , 895 (1994).](http://dx.doi.org/10.1088/0034-4885/57/9/002)
- [71] [M. Rocca, Surf. Sci. Rep. 22 , 1 (1995).](http://dx.doi.org/10.1016/0167-5729(95)00004-6)
- [72] A. Messiah, Quantum Mechanics (North-Holland, New York, 1966).
- [73] M. Abramowitz and I. A. Stegun, Handbook of Mathematical Functions (Dover, New York, 1972).

## ACKNOWLEDGEMENTS

We are indebted to Claus Ropers and Murat Sivis for motivating the present study and suggesting that the interaction between free electrons and Rydberg atoms can produce large excitation probabilities. We thank them and Valerio Di Giulio for helpful and enjoyable discussions. This work has been sup- ported in part by the European Research Council (Advanced Grants 789104-eNANO and 101055435-ULEEM), the European Commission (Horizon 2020 Grants No. 101017720 FETProactive EBEAM and No. 964591-SMART-electron), the Spanish MICINN (PID2020-112625GB-I00 and Severo Ochoa CEX2019-000910-S), the Catalan AGAUR (Grant No. 2024 FI-2 00052) and CERCA Programs, and Fundaciós Cellex and Mir-Puig.

## ADDITIONAL FIGURES

FIG. S1. Dependence of the dipolar transition probability on principal quantum numbers and the orientation of the transition dipole. We plot the first-order dipolar transition probability produced by a free electron moving with velocity v = 0 . 1 c (parallel to the quantization axis z ) and impact parameter b = n 2 i + n 2 f a 0 from an initial s state | ni , 0 , 0 ⟩ to final p states [(1 / √ 2) | ni + ∆ n , 1 , 1 ⟩ + | ni + ∆ n , 1 , -1 ⟩ (a, x -type transition) and | ni + ∆ n , 1 , 0 ⟩ (b, z -type transition)] for various values of ∆ n [see legend in (a)].

<!-- image -->

FIG. S2. Strong coupling regime and nondipolar transitions revealed within first-order perturbation theory. We plot the transition probabilities calculated within first-order perturbation theory for the e-beam configurations depicted in left insets: velocity and impact parameter v = v ˆ z and R 0 = b ˆ x in (a,b), and v = v ˆ x and R 0 = b ˆ z in (c,d). The quantization axis is z in all cases. Starting in an initial state | 10 , 9 , 9 ⟩ , the probability is represented as a function of the impact parameter b and the electron kinetic energy for dipolar transitions (a,b; final state | 11 , 10 , 10 ⟩ ) and nondipolar transitions (a,b; final state | 11 , 7 , 7 ⟩ ).

<!-- image -->

FIG. S3. Additional transition probabilities under the conditions of Fig. 2 in the main text. We plot probability maps for transitions from an initial state | 5 , 4 , 4 ⟩ to other final states calculated to all orders in the electron-atom interaction. We show results for (a,b,e,f) elastic transitions to final states | 5 , 3 , 3 ⟩ and | 5 , 2 , 2 ⟩ ; (c,g) inelastic transitions with no angular-momentum exchange (final state | 6 , 4 , 4 ⟩ ); and (d,h) inelastic transitions with angular momentum exchanges ( | 6 , 2 , 2 ⟩ )

<!-- image -->