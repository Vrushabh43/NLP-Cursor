## Intermodulation spectroscopy and the nonlinear response of two-level systems in superconducting coplanar waveguide resonators

Janka Bizn´ arov´ a, 1, ∗ J. C. Rivera Hern´ andez, 2 Daniel Forchheimer, 3

1 2 1, 4, †

Jonas Bylander, David B. Haviland, and Gustav Andersson

Chalmers University of Technology, Microtechnology and Nanoscience, SE-41296, Gothenburg, Sweden

Department of Applied Physics, KTH Royal Institute of Technology, SE-106 91 Stockholm, Sweden

Intermodulation Products AB, Segersta, Sweden

2 3

4 Pritzker School of Molecular Engineering, University of Chicago, IL 60637 Chicago, USA

(Dated: February 19, 2024)

Two-level system (TLS) loss is typically limiting the coherence of superconducting quantum circuits. The loss induced by TLS defects is nonlinear, resulting in quality factors with a strong dependence on the circulating microwave power. We observe frequency mixing due to this nonlinearity by applying a two-tone drive to a coplanar waveguide resonator and measuring the intermodulation products using a multifrequency lock-in technique. This intermodulation spectroscopy method provides an efficient approach to characterizing TLS loss in superconducting circuits. Using harmonic balance reconstruction, we recover the nonlinear parameters of the device-TLS interaction, which are in good agreement with the standard tunnelling model for TLSs.

## I. INTRODUCTION

Superconducting quantum computing is facing a challenge in the relatively short coherent lifetimes of state-ofthe-art qubits, currently in the sub-millisecond range [15]. A significant source of decoherence for these qubits is dielectric loss caused by parasitic two-level system (TLS) defects [6-8], whose microscopic origin is a topic of ongoing active research [9-11]. These TLSs can couple to qubits, providing a source of energy loss and parameter fluctuations, and therefore decoherence. In this article we introduce a method for the measurement and analysis of the inherent nonlinearity of these TLSs in superconducting resonators.

Superconducting resonators are essential components of quantum processors and a good testbed for characterizing dielectric loss. In circuit quantum electrodynamics resonators are treated as linear elements, typically modelled as lumped-element LC oscillators. The resonator's coupling to TLS defects gives rise to a characteristic dependence of the internal quality factor Q i on circulating power, with a drop in Q i at low powers where the TLS bath is not driven to saturation [12, 13]. This powerdependent response makes resonators ideal for probing TLSs in a qubit's environment.

In this work we explore how the power-dependent behaviour of Q i translates to a low-power nonlinear response of the resonator. We measure this nonlinearity in a high-quality-factor coplanar waveguide (CPW) resonator, showing that it gives rise to frequency mixing, or intermodulation - a characteristic feature of nonlinear response which has been observed for TLS-induced [14] and other nonlinearities in superconducting circuits [15-17]. Intermodulation results in response at integer combina- tions of the applied drive frequencies, f IMP = ∑ i k i f i , where f i are drive frequencies and k i integers. The amplitude and phase of these intermodulation products (IMPs) can be measured with large signal-to-noise ratios (SNR) using lock-in techniques. Modelling the system as a driven harmonic oscillator with nonlinear damping due to parasitic TLSs, we reconstruct the nonlinear response of the device as a function of drive amplitude and frequency using harmonic balance analysis.

[∗ jankab@chalmers.se](mailto:jankab@chalmers.se)

[† gandersson@uchicago.edu](mailto:gandersson@uchicago.edu)

## II. EXPERIMENTAL METHODS

We perform all measurements on a superconducting aluminium λ/ 4 coplanar waveguide resonator with a resonance frequency of 4 . 11 GHz, capacitively coupled to a transmission line in a notch configuration. The device has no engineered nonlinear elements. All microwave measurements presented here were carried out inside a dilution refrigerator at ∼ 10 mK using the set-up outlined in Appendix B.

For the initial characterization of the resonator, we measure the S 21 scattering parameter in transmission using a vector network analyzer and extract the relevant parameters such as Q i and the resonance frequency f r using the circle-fitting method [18], as detailed in Appendix D. We characterize Q i for excitation powers ranging from the single photon level, relevant for quantum computing applications, up to 10 8 photons where we observe other, non-TLS related loss and nonlinear mechanisms.

The average number of photons ⟨ n ⟩ circulating in the resonator is estimated using the relation

$$\langle n \rangle = \frac { Z _ { 0 } } { Z _ { r } } \frac { Q _ { l } ^ { 2 } } { | Q _ { c } | } \frac { 2 P _ { i n } } { \hbar { ( } 2 \pi f _ { r } ) ^ { 2 } } ,$$

where Z 0 and Z r are the characteristic impedances of the transmission line and the resonator, respectively. The

1

FIG. 1. Intermodulation measurements at drive powers corresponding to ⟨ n ⟩ = 10 3 when on resonance. a) A schematic of the tones generated at the output of the measurement instrumentation (MI) and the output of the device-under-test (DUT). b) IMPs measured when two drive tones are applied at resonance. The abscissa shows the detection comb frequencies f relative to the centre of the detection comb f c = ( f 1 + f 2 ) / 2. IMPs are detected at frequencies fulfilling the f IMP = k 1 f 1 + k 2 f 2 condition, which falls on every other tone in this detection comb. c) IMP power spectroscopy performed by sweeping the frequency comb depicted in a) across a frequency spectrum centered around the resonance frequency f r . d) Vertical line-cuts of the IMP spectroscopy data shown in c): the device resonance demonstrates as a dip in the transmission of drive tone f 1 , the third IMP f 3 presents as a peak at 2 f 2 -f 1 , and the background noise is shown at a frequency f BG that does not correspond to any IMP. The phase response is shown in Appendix C.

<!-- image -->

power at the device input P in is calculated by subtracting the input line attenuation from the measurement instrument output power. The input line attenuation was obtained via an ac-Stark shift measurement of a qubit device [19] in a separate experiment.

To probe nonlinearities in the device through intermodulation distortion we use a multi-frequency lock-in amplifier platform [20], where we output two drive tones separated by ∆ = 100 Hz, see Fig. 1a). We choose this drive spacing to be significantly smaller than the powerdependent linewidth of the resonator (8-11 kHz). This choice guarantees that both the drives and the lowestorder IMPs remain well within the resonance linewidth.

We measure the response of the device to these two drive tones using a detection frequency comb demodulating the IQ quadratures at frequencies spaced by ∆ / 2. Consequently, intermodulation produces a signal at every other frequency in this comb, and the remaining detection frequencies sample the noise background. The generation of drive tones and digitization of the response is performed in the second Nyquist zone, without the use of analog mixers for frequency conversion. Odd-order IMPs, i.e. when | k 1 | + | k 2 | is an odd number, appear as a comb of frequencies when f c coincides with the resonance frequency f r , as shown in Fig. 1 b). Even-order IMPs fall far outside of the resonance linewidth.

We perform intermodulation spectroscopy, stepping the detection frequency comb with the two drives in the centre across a frequency range. This frequency range is centred around f r , with a span well outside the res- onance linewidth. As shown in Fig. 1 c), we detect no IMPs when the centre of the comb is off-resonant. As the two drives approach f r , we measure a clear signal at the IMP frequencies, peaking at f c = f r . The decay of the measured IMPs outside of resonance shows that the IMPs are generated in the device and are not artifacts of nonlinearities present elsewhere in the measurement system. Thus, we can use this intermodulation spectroscopy method to characterize nonlinearities native to our CPW resonator.

## III. RESULTS

The standard resonator characterization shows the expected trend where Q i is suppressed at low ⟨ n ⟩ due to interaction with parasitic TLSs. This observation fits the so-called standard tunnelling model [21]

$$\frac { 1 } { Q _ { i } } = F \delta _ { T L S } ^ { 0 } \frac { \tanh \left ( h f _ { r } / 2 k _ { B } T \right ) } { \left ( 1 + \langle n \rangle / n _ { c } \right ) ^ { \beta } } + \delta _ { 0 } , \quad \left ( 2 \right )$$

where Fδ 0 TLS describes the power-dependent loss due to parasitic TLSs, with F quantifying the TLS filling factor, and δ 0 TLS is the dielectric loss tangent, dependent on the density of the TLSs. The parameter n c is the critical photon number for the saturation of the TLS bath, and the power-independent term δ 0 quantifies the other, nonTLS-related sources of loss, such as radiation or resistive losses due to quasiparticles. T , h , and k B denote temper- ature, the Planck constant, and the Boltzmann constant, respectively.

FIG. 2. a) Internal quality factor Q i as a function of applied power ⟨ n ⟩ , fitted to equation 2. b) The power of the four strongest IMPs, as well as the background noise at non-IMP frequencies, plotted as a function of applied drive power, for the case when the drive tones are applied at resonance. In the entirety of the measured power span, the signal corresponding to the two strongest IMPs measured is well above the noise floor. At drive powers exceeding ∼ 5 × 10 5 photons, the dominant nonlinearity is due to kinetic inductance, and the strength of the IMPs increases rapidly. The slope of the power dependence of the data plotted on a logarithmic scale is fitted for ⟨ n ⟩ in the range of 200-2 × 10 5 photons.

<!-- image -->

In the standard tunnelling model, the parameter β = 0 . 5 characterizes the change of Q i with photon number. This value often fits data poorly, especially for high-quality resonators, which show a weaker powerdependence [22-24]. We treat β as a fitting parameter, finding a best-fit value β = 0 . 3 (see Fig. 2a). These deviations in β have been attributed to the spectral instability of the device-TLS system, and the interactions between different TLSs themselves, not just interactions between a TLS and the quantum circuit [25-27].

Having performed standard resonator characterization measurements, we proceed to intermodulation spectroscopy as a function of applied drive power. Figure 2b) shows a clear signal at IMP frequencies across the entire measured power range, with a power-dependent amplitude of the measured IMPs. We identify three separate regions with different power-dependent characteristics, consistent with the observations from Fig. 2a).

The drive powers used in this measurement exceed the critical photon number n c . In the low-power regime where ⟨ n ⟩ &lt; 200, TLSs dominate the total loss of the resonator, and the dependence of the IMPs on power is strong with a variable slope. In the intermediate drive power regime where ⟨ n ⟩ ≫ n c , the four strongest IMPs show a power-law behaviour, scaling with drive power as ⟨ n ⟩ k . The fit parameters k are laid out in Table I, alongside the parameters predicted by the model in section IV. We note that due to the saturation of the TLS bath, the IMPs increase more slowly than the drive amplitude (i.e. k &lt; 1). The opposite is typically the case for intermodulation distortion in electronic devices [28]. At drive powers exceeding ∼ 5 × 10 5 photons, the non- linearity increases sharply, which relates to the onset of kinetic inductance effects at high input power [29, 30].

These trends are consistent with the Q i vs. ⟨ n ⟩ curve shown in Fig. 2a). Here, TLSs contribute significantly to the loss at low excitation numbers and become saturated with stronger probes. At high power, current-induced pair breaking changes the kinetic inductance and the frequency of the resonator shifts, as shown in Fig. 9.

The coupling between quantum circuits and TLSs tends to fluctuate on slow time scales [27, 31]. We study this effect on the measured IMPs in Fig. 3, where we repeat the same IMP spectroscopy measurement at a fixed drive power level of ∼ 10 3 photons for 25 hours. Each of the individual measurements is averaged for ∼ 5 min. We do observe seemingly random fluctuations of the measured IMPs over time in this measurement, correlated between the different orders of IMPs. The fluctuations do not extend to the measured amplitudes of the drive tones, which are stable in comparison, nor to the measured background noise. From this we conclude that the fluctuations are native to the nonlinearity in the device, and do not originate in the measurement setup from sources such as drifts in room-temperature electronics.

We also conclude that the fluctuations shown in Fig. 2 are likely not a function of applied power. Rather, the intermodulation spectrum is unstable, revealing a change of coupling between the TLS and the device over time, a typical feature of TLS interaction [32].

FIG. 3. IMPs measured repeatedly for 25h, in 5-minute intervals, at a constant drive power level of ∼ 10 3 photons.

<!-- image -->

TABLE I. Power dependence of the measured IMPs in Fig. 2d), and of the modeled IMPs in Fig. 4, fitted to ⟨ n ⟩ k · 10 l .

|   IMP order | Experimental fit   |   Model fit k |
|-------------|--------------------|---------------|
|           3 | 0.41 ± 0.05        |          0.42 |
|           5 | 0.38 ± 0.04        |          0.43 |
|           7 | 0.42 ± 0.04        |          0.44 |
|           9 | 0.48 ± 0.05        |          0.45 |

## IV. NONLINEAR PARAMETER RECONSTRUCTION

In this section, we detail the modelling and reconstruction of the nonlinear loss due to parasitic TLSs. Our reconstruction algorithm is based on fitting the linear and nonlinear oscillator parameters to a single intermodulation spectrum by harmonic balance [33, 34].

We model our resonator as a driven harmonic oscillator with non-linear damping caused by parasitic TLSs. The Heisenberg-Langevin equation of motion describing the dynamics of the resonator in the rotating-wave approximation is then

$$\dot { \hat { a } } = - i \omega _ { 0 } \hat { a } - \frac { \kappa _ { 0 } + \kappa _ { e x t } } { 2 } \hat { a } - \frac { \kappa _ { T L S } ( | a | ) } { 2 } \hat { a } - \sqrt { \kappa _ { e x t } } a _ { i n } , \ ( 3 )$$

where ˆ a and a in are the time-dependent intra-cavity modes and the input drives respectively, ω 0 the resonant frequency, κ 0 the internal linear loss rate, κ ext the external coupling to the transmission line, and κ TLS ( | a | ) the power-dependent loss due to parasitic TLSs. We consider a power-dependent damping of the standard form of Eq. (2), giving

$$\kappa _ { T L S } ( | a | ) a = \frac { \kappa _ { T L S } } { \left [ 1 + ( | a | / a _ { c } ) ^ { 2 } \right ] ^ { \beta } } , \quad ( 4 ) \quad \text {matt} \quad \begin{matrix} 4 \\ 2 \end{matrix}$$

where κ TLS = f r Fδ 0 TLS represents the TLS loss rate, and a 2 c = n c the critical photon number.

We drive the system with two tones, separated by ∆, such that the IMPs created are within the resonator's linewidth, where the sensitivity is enhanced. When the drive frequencies are periodic in some measurement time T = 2 π/ ∆, and the nonlinearities and drives are sufficiently weak, the system's response is a discrete spectrum at frequencies that correspond to integer multiples of ∆.

We first solve the forward problem by numerically integrating Eq. (3) using scipy.integrate.ode from the SciPy library [35] to obtain the time-dependent intra-cavity field. The output field is then obtained using the inputoutput relation ˆ a out = √ κ ext ˆ a + a in . Fig. 4) shows the four strongest IMPs as a function of drive power simulated with experimentally relevant parameters. For strong drives ⟨ n ⟩ ≫ 1, the IMP power shows a powerlaw scaling proportional to ⟨ n ⟩ k , with parameters k laid out in Table I. This behaviour matches the experimental results shown in Fig. 2 b). We also simulate a sweep of the drive tone frequency across the resonance and analyze the power dependence of the IMPs as a function of β (see Appendix E for details).

To reconstruct the nonlinear parameters of the system, we expand the TLS damping in Eq. 4 in a power series, transforming the equation of motion to

$$\dot { \hat { a } } = - i \omega _ { 0 } \hat { a } - \sum _ { n = 1 } ^ { N } c _ { n } | a | ^ { n - 1 } \hat { a } - \sqrt { \kappa _ { e x t } } a _ { i n } ,$$

which is linear in the coefficients c n . The coefficients are independent of the proposed model, allowing the application of the reconstruction algorithm to various types of nonlinearities [17, 36], including unknown ones.

In the experiment we measure only a limited number of frequencies with good SNR, corresponding to the two drive tones and 14 IMPs. These frequencies, denoted as ω k with Fourier component ˆ A k , represent a partial spectral response of the system. Specifically, ˆ A k corresponds to the intracavity field amplitude at the frequency ω k .

By Fourier transforming and rewriting Eq. (5) in matrix form, we arrive at an expression linear in the coefficients c n [17]

$$\sum _ { l } H _ { k l } p _ { l } = - A _ { i n , k } ,$$

where the k th row of the matrix H kl is given by

$$\text {constant} \quad H _ { k } = \left ( i \omega _ { k } \hat { A } _ { k } \ i \hat { A } _ { k } \ \hat { A } _ { k } \ \mathcal { F } \left \{ | a | ^ { 2 } \hat { a } \right \} _ { k } \ \cdots \ \mathcal { F } \left \{ | a | ^ { N - 1 } \hat { a } \right \} _ { k } \right ) ,$$

and p l are the components of a vector containing the unknown parameters

$$\sqrt { \kappa _ { e x t } } \, p ^ { T } = \left ( 1 \ \omega _ { 0 } \ c _ { 1 } \ \cdots \ c _ { N } \right ) .$$

We solve Eq. (6) by numerical pseudo-inverse of the matrix H to find the best-fit vector p , which includes the polynomial coefficients c n . To extract the TLS damping parameters κ TLS , a c and β from the polynomial expansion coefficients and to compare our harmonic balance results with the circle fit analysis, we perform a least-squares fitting. For this fit, we set κ 0 = 0 . 86 kHz, based on the value extracted from a fit of the parameters extracted from the standard circle fit to Eq. 2 in the high-power regime. Our reconstruction is based on measurements of a single intermodulation spectrum and encounters limitations in simultaneously capturing both a c and β . We therefore fix β = 0 . 3 motivated by the slope of the 3rd-order IMP strength in the TLS saturation regime (see Appendix E).

FIG. 4. Simulation of the power of the generated IMPs as a function of applied drive power. The parameters of the fit shown with dashed lines are shown in Table I.

<!-- image -->

TABLE II. Reconstructed resonator parameters via fitting the standard tunnelling model Eq. (2) and the intermodulation spectral method with harmonic balance.

| Parameters    |   Standard model |   Harmonic balance |
|---------------|------------------|--------------------|
| f 0 [GHz]     |             4.11 |               4.11 |
| κ ext [kHz]   |             6.77 |               6.62 |
| κ TLS [kHz] √ |             3.95 |               5.22 |
| a c [ n ]     |            1.414 |              1.641 |

The resulting parameters, listed in Table II, show good agreement with the standard fit values. Without fixing the parameter β , our reconstruction method still yields the important TLS loss parameter κ TLS in good agreement with the standard method. Differences may be due to variable conditions across cooling cycles as the standard resonance sweeps and IMP data were obtained in separate cooldowns [37].

## V. DISCUSSION AND CONCLUSION

We demonstrate the inherent nonlinear nature of parasitic TLSs in superconducting circuits by observing frequency mixing products in a CPW resonator when driven near-resonantly by two slightly detuned drive tones. We characterize the intermodulation products of this frequency mixing as a function of drive detuning with re- spect to the resonance frequency, as well as the applied drive power. Drawing a comparison to the standard tunnelling model for TLSs, we observe an analogous power dependence of the IMPs on applied drive power, as we expect from the conventional analysis of the Q i suppression at decreasing drive powers as an effect of a saturable bath of TLSs.

Repeated measurements of the IMPs generated in the device when driven by the same conditions over 25 h show correlated jumps in the IMP amplitudes. This approach provides an efficient method of studying the timescales of TLS-device interaction with a high SNR.

Using harmonic balance analysis and assuming a model for a driven harmonic oscillator with nonlinear damping, we reconstruct the nonlinear parameters of this deviceTLS interaction, in good agreement with the parameters extracted from the experimental data using the conventional tunnelling TLS model. Our reconstruction method is promising for characterizing TLSs in superconducting devices, as it eliminates the need for a comprehensive frequency and power sweep, enabling analysis through a single intermodulation spectrum.

## ACKNOWLEDGMENTS

This work was funded by the Knut and Alice Wallenberg (KAW) Foundation through the Wallenberg Center for Quantum Technology (WACQT). The device fabrication was performed at Myfab Chalmers. D. B. H. and D. F. are part owners of the company Intermodulation Products AB, which produces the digital microwave platform used in this experiment.

## Appendix A: Sample fabrication

The device was fabricated on a 280 µ m thick, high resistivity ( ρ ≥ 10 kΩ cm), intrinsic silicon substrate. Prior to thin film deposition, the substrate was submerged in 2% HF for 60 s to remove the native surface oxide, then rinsed in deionized water and loaded immediately into a heated load-lock of a sputter deposition tool, where the substrate was heated to 80 ° C during pump-down. After transfer into the deposition chamber, the substrate was heated to 300 ◦ C for 10 minutes and left to cool down for 16 hours, after which the chamber pressure was 2 . 2 × 10 -8 mbar. A 150 nm thick layer of Al was deposited by sputtering at 0 . 9 nms -1 , and the film was oxidized in situ by static oxidation at 10 mbar.

The device was patterned by direct-write optical lithography on a PMMA A2 + S1805 resist stack. The optically sensitive S1805 was developed in a TMAHbased developer. After development, the exposed PMMA protecting the underlying Al from TMAH was ashed in oxygen plasma, and the pattern was transferred into Al by wet etch in an H 3 PO 4 :HNO 3 :CH 2 O 2 solution at room temperature.

FIG. 5. Cryogenic measurement setup.

<!-- image -->

The remaining resist was then dissolved in an NMPbased resist remover, acetone, and isopropanol. The wafer was coated with a fresh layer of protective photoresist (S1805), diced, and stripped again in the aforementioned solvents. The cleaning was finished with an ozone-cleaning step.

## Appendix B: Measurement setup

The chip is placed in a light-tight copper sample box, where the transmission line is wire-bonded to input and output SMA connectors, and the ground plane of the CPW is wire-bonded to the copper box along the chip periphery.

The sample box is then mounted onto a copper tail attached to the mixing chamber stage of a dilution refrigerator. The copper tail is enclosed in an additional copper can coated with a layer of Stycast mixed with SiC on the inside, which is in turn enclosed in a Cryoperm magnetic shield. This is in addition to the shields attached to every temperature stage as marked in Fig. 5.

On the input signal line, the incoming signal is attenuated at each stage with individual attenuators amounting to a total of 55 dB attenuation. The input line attenuated by an additional 11 dB, as determined from an ac-Stark shift measurement of a qubit.

Microwave switches are present below the mixing chamber stage on both the input and output lines. On the output line, above the 10 mK stage, the signal is passed through a chain of microwave isolators and filters to suppress reflected signals, as well as thermal noise coming from the higher temperature stages and the amplifiers. The weak signal is amplified at the 4 K stage by a low-noise HEMT cryogenic amplifier. At room temperature, the signal is further amplified by two gain block amplifiers connected in series.

For intermodulation product measurements, the cryogenic microwave measurement setup was connected to a multi-frequency lock-in amplifier [20]. We use a separate signal output for each drive tone, passing through a 34.3 GHz bandpass filter before being combined in a power splitter and routed through the cryogenic measurement setup.

For the quality factor characterization of the device, the microwave setup was connected to a vector network analyzer, with a 30 dB attenuator added to the output of the analyzer at low power measurements.

## Appendix C: Additional data

To investigate the origins of the non-linearity we observe through intermodulation, we repeat the intermodulation measurement; only this time, we place the frequency comb far outside the resonance, detuned by 700 kHz. Here the resonator does not interact with the drive signals, and instead, we measure the transmission of our microwave measurement set-up and the transmission line of the device itself. We do not observe any intermodulation here, ruling out the measurement set-up as the origin of this nonlinearity.

We show the phase response of the resonator and the three strongest IMPs in Fig. 7. The phase response at the drive tone wraps by less than π across resonance, which is an expected response for an asymmetric, overcoupled resonator in a notch configuration [38]. The phase response of the IMPs wraps by 2 π .

## Appendix D: Resonator characterization

The initial characterization of the resonator is performed using a vector network analyzer, where the complex S 21 transmission scattering parameter is measured in a spectroscopy. The S 21 data is analyzed using the resonance circle fitting method with diameter correc- tion [18]:

FIG. 6. Intermodulation measurement performed around a frequency 700 kHz away from resonance. We observe no intermodulation products as a result of the two drive tones, showing that the non-linearities we observe are native to the device and not an artifact of our measurement set-up.

<!-- image -->

FIG. 7. The phase response of the resonator at the drive frequency and the three strongest IMPs, as a function of drive frequency. The drives are at resonance when the detection comb frequency f c coincides with the resonance frequency f r .

<!-- image -->

$$S _ { 2 1 } ( f ) = a e ^ { i \alpha } e ^ { - 2 \pi f \tau } \left [ 1 - \frac { ( Q _ { l } / | Q _ { c } | ) e ^ { i \phi } } { 1 + 2 i Q _ { l } ( f / f _ { r } - 1 ) } \right ] \quad ( D 1 ) \quad \text {in the} \quad \text {plane}$$

where f r is the resonance frequency, f the probe frequency, ϕ the impedance mismatch, Q c the coupling quality factor and Q l the loaded quality factor, from which Q i can be extracted with Q -1 l = Q -1 i + Re { Q -1 c } . The remaining parameters, additional amplitude a , phase shift α , and electronic delay τ , account for environmental imperfections. For an example of the accuracy of this fit at the single photon level, see Fig. 8.

The circle fitting method is at its most reliable when the resonator is near-critically coupled to the transmission line, i.e. Q i ≈ | Q c | . With a | Q c | of 6 × 10 5 and a Q i in the range of 1-5 × 10 6 depending on their applied drive power, our device is close to this condition, as seen in the symmetry of the resonance circle on the complex plane plotted in Fig. 8 b).

FIG. 8. The resonance circle fit method at the single photon level. a) shows the fit of the absolute value of the transmission scattering parameter S 21 as a function of frequency, with a dip in transmission at resonance. b) shows the resonance circle on the complex plane.

<!-- image -->

FIG. 9. The resonator's frequency extracted from a circle fit of the complex S 21 data, as a function of average photon number ⟨ n ⟩

<!-- image -->

## Appendix E: Additional modeling

We simulate a sweep of the drive frequencies across the resonance shown in Fig. 10. The drive strength presents a dip on resonance, while the IMP strength increases, qualitatively matching the experimental results in Fig. 1. We also simulate the power dependence of the third-order IMP for various β values, as illustrated in Fig. 11. Notably, with increasing β we observe a reduction in the slope of the third-order IMP above n c . The connection between the slope above n c and the parameter β is seen in the inset of Fig. 11. As β increases, we observe a no- ticeable decrease in the slope, becoming 0 at β = 0 . 5. This behaviour indicates that the observed power dependence above n c is not a feature of the standard tunnelling model with β = 0 . 5. The value of β = 0 . 3 found in Fig. 2 is also in agreement with this simulation.

FIG. 10. Intermodulation simulation results. a) A schematic of the input tones and the output of the device-under-test (DUT). b) Simulated IMPs when two drive tones are applied inside the resonance linewidth. The abscissa shows the detection comb frequencies f relative to the centre of the detection comb f c = ( f 1 + f 2 ) / 2. IMPs appear at frequencies fulfilling the f IMP = k 1 f 1 + k 2 f 2 condition, which falls on every other tone in this detection comb. c) Simulated IMP spectroscopy performed by sweeping the frequency comb depicted in a) across a frequency spectrum centred around the resonance frequency f r . d) Vertical line cuts of the simulated IMP spectroscopy data shown in c). The device resonance shows a dip in the transmission of drive tone f 1 , and the third IMP f 3 presents a peak at 2 f 2 -f 1 .

<!-- image -->

FIG. 11. Simulation of the power of the 3rd order IMP as a function of the input drive power normalized by photon number at different β values. The inset shows the value of the slope of the TLS saturation regime k as a function of β .

<!-- image -->

- [1] Morten Kjaergaard, Mollie E. Schwartz, Jochen Braum¨ uller, Philip Krantz, Joel I.-J. Wang, Simon Gustavsson, and William D. Oliver, 'Superconducting Qubits: Current State of Play,' Annu. Rev. Condens.

[Matter Phys. 11 , 369-395 (2020).](http://dx.doi.org/10.1146/annurev-conmatphys-031119-050605)

- [2] Alexander P. M. Place, Lila V. H. Rodgers, Pranav Mundada, Basil M. Smitham, Mattias Fitzpatrick, Zhaoqi Leng, Anjali Premkumar, Jacob Bryon, An-

drei Vrajitoarea, Sara Sussman, Guangming Cheng, Trisha Madhavan, Harshvardhan K. Babla, Xuan Hoang Le, Youqi Gang, Berthold J¨ ack, Andr´ as Gyenis, Nan Yao, Robert J. Cava, Nathalie P. de Leon, and Andrew A. Houck, 'New material platform for superconducting transmon qubits with coherence times exceeding 0.3 milliseconds,' Nat. Commun. 12 , 1-6 (2021).

- [3] Peter A. Spring, Shuxiang Cao, Takahiro Tsunoda, Giulio Campanaro, Simone Fasciati, James Wills, Mustafa Bakr, Vivek Chidambaram, Boris Shteynas, Lewis Carpenter, Paul Gow, James Gates, Brian Vlastakis, and Peter J. Leek, 'High coherence and low cross-talk in a tileable 3D integrated superconducting circuit architecture,' Sci. Adv. 8 (2022), 10.1126/sciadv.abl6698.
- [4] Chenlu Wang, Xuegang Li, Huikai Xu, Zhiyuan Li, Junhua Wang, Zhen Yang, Zhenyu Mi, Xuehui Liang, Tang Su, Chuhong Yang, Guangyue Wang, Wenyan Wang, Yongchao Li, Mo Chen, Chengyao Li, Kehuan Linghu, Jiaxiu Han, Yingshan Zhang, Yulong Feng, Yu Song, Teng Ma, Jingning Zhang, Ruixia Wang, Peng Zhao, Weiyang Liu, Guangming Xue, Yirong Jin, and Haifeng Yu, 'Towards practical quantum computers: transmon qubit with a lifetime approaching 0.5 milliseconds,' npj Quantum Inf. 8 , 1-6 (2022).
- [5] A. Somoroff, Q. Ficheux, R. A. Mencia, H. Xiong, R. Kuzmin, and V. E. Manucharyan, 'Millisecond Coherence in a Superconducting Qubit,' Phys. Rev. Lett. 130 , 267001 (2023).
- [6] D. P. Pappas, M. R. Vissers, D. S. Wisbey, J. S. Kline, and J. Gao, 'Two level system loss in superconducting microwave resonators,' IEEE T. Appl. Supercond. 21 , 871-874 (2011).
- [7] J¨ urgen Lisenfeld, Grigorij J. Grabovskij, Clemens M¨ uller, Jared H. Cole, Georg Weiss, and Alexey V. Ustinov, 'Observation of directly interacting coherent two-level systems in an amorphous material,' Nat. Commun. 6 , 6182 (2015).
- [8] Clemens M¨ uller, Jared H. Cole, and J¨ urgen Lisenfeld, 'Towards understanding two-level-systems in amorphous solids: insights from quantum circuits,' Rep. Prog. Phys. 82 , 124501 (2019).
- [9] M. Molina-Ruiz, Y. J. Rosen, H. C. Jacks, M. R. Abernathy, T. H. Metcalf, X. Liu, J. L. DuBois, and F. Hellman, 'Origin of mechanical and dielectric losses from two-level systems in amorphous silicon,' Phys. Rev. Mater. 5 , 035601 (2021).
- [10] Sun Un, Sebastian de Graaf, Patrice Bertet, Sergey Kubatkin, and Andrey Danilov, 'On the nature of decoherence in quantum circuits: Revealing the structural motif of the surface radicals in α -Al2O3,' Sci. Adv. 8 , eabm6169 (2022).
- [11] Martin Spiecker, Patrick Paluch, Nicolas Gosling, Niv Drucker, Shlomi Matityahu, Daria Gusenkova, Simon G¨ unzler, Dennis Rieger, Ivan Takmakov, Francesco Valenti, Patrick Winkel, Richard Gebauer, Oliver Sander, Gianluigi Catelani, Alexander Shnirman, Alexey V. Ustinov, Wolfgang Wernsdorfer, Yonatan Cohen, and Ioan M. Pop, 'Two-level system hyperpolarization using a quantum Szilard engine,' Nat. Phys. , 1-6 (2023).
- [12] Jeremy M. Sage, Vladimir Bolkhovsky, William D. Oliver, Benjamin Turek, and Paul B. Welander, 'Study of loss in superconducting coplanar waveguide res-

[onators,' J. Appl. Phys. 109 , 063915 (2011).](http://dx.doi.org/10.1063/1.3552890)

- [13] A. Megrant, C. Neill, R. Barends, B. Chiaro, Yu Chen, L. Feigl, J. Kelly, Erik Lucero, Matteo Mariantoni, P. J. J. O'Malley, D. Sank, A. Vainsencher, J. Wenner, T. C. White, Y. Yin, J. Zhao, C. J. Palmstrøm, John M. Martinis, and A. N. Cleland, 'Planar superconducting resonators with internal quality factors above one million,' Appl. Phys. Lett. 100 (2012), 10.1063/1.3693409.
- [14] Ryan Kaufman, Theodore White, Mark I. Dykman, Andrea Iorio, George Stirling, Sabrina Hong, Alex Opremcak, Andreas Bengtsson, Lara Faoro, Joseph C. Bardin, Tim Burger, Robert Gasca, and Ofer Naaman, 'Josephson parametric amplifier with Chebyshev gain profile and high saturation,' arXiv (2023), 10.48550/arXiv.2305.17816, 2305.17816.
- [15] R. P. Erickson, M. R. Vissers, M. Sandberg, S. R. Jefferts, and D. P. Pappas, 'Frequency Comb Generation in Superconducting Resonators,' Phys. Rev. Lett. 113 , 187002 (2014).
- [16] A. Yu. Dmitriev, R. Shaikhaidarov, T. H¨ onigl-Decrinis, S. E. de Graaf, V. N. Antonov, and O. V. Astafiev, 'Probing photon statistics of coherent states by continuous wave mixing on a two-level system,' Phys. Rev. A 100 , 013808 (2019).
- [17] T. Weißl, S. W. Jolin, R. Borgani, D. Forchheimer, and D. B. Haviland, 'A general characterization method for nonlinearities in superconducting circuits,' New J. Phys. 21 , 053018 (2019).
- [18] S. Probst, F. B. Song, P. A. Bushev, A. V. Ustinov, and M. Weides, 'Efficient and robust analysis of complex scattering data under noise in microwave resonators,' Rev. Sci. Instrum. 86 , 024706 (2015).
- [19] A. Bruno, G. de Lange, S. Asaad, K. L. van der Enden, N. K. Langford, and L. DiCarlo, 'Reducing intrinsic loss in superconducting resonators by surface treatment and deep etching of silicon substrates,' Appl. Phys. Lett. 106 , 182601 (2015).
- [20] Mats O. Thol´ en, Riccardo Borgani, Giuseppe Ruggero Di Carlo, Andreas Bengtsson, Christian Kriˇ zan, Marina Kudra, Giovanna Tancredi, Jonas Bylander, Per Delsing, Simone Gasparinetti, and David B. Haviland, 'Measurement and control of a superconducting quantum processor with a fully integrated radio-frequency system on a chip,' Rev. Sci. Instrum. 93 (2022), 10.1063/5.0101398.
- [21] J Burnett, L Faoro, and T Lindstr¨ om, 'Analysis of high quality superconducting resonators: consequences for tls properties in amorphous oxides,' Supercond. Sci. Tech. 29 , 044008 (2016).
- [22] J. Burnett, J. Sagar, O. W. Kennedy, P. A. Warburton, and J. C. Fenton, 'Low-Loss Superconducting Nanowire Circuits Using a Neon Focused Ion Beam,' Phys. Rev. Appl. 8 , 014039 (2017).
- [23] David Niepce, Jonathan Burnett, and Jonas Bylander, 'High Kinetic Inductance NbN Nanowire Superinductors,' Phys. Rev. Appl. 11 , 044014 (2019).
- [24] M. Kudra, J. Bizn´ arov´ a, A. Fadavi Roudsari, J. J. Burnett, D. Niepce, S. Gasparinetti, B. Wickman, and P. Delsing, 'High quality three-dimensional aluminum microwave cavities,' Appl. Phys. Lett. 117 , 070601 (2020).
- [25] J. Burnett, L. Faoro, I. Wisby, V. L. Gurtovoi, A. V. Chernykh, G. M. Mikhailov, V. A. Tulin, R. Shaikhaidarov, V. Antonov, P. J. Meeson, A. Ya. Tzalenchuk, and T. Lindstr¨ om, 'Evidence for interacting

two-level systems from the 1/f noise of a superconducting resonator,' Nat. Commun. 5 , 4119 (2014).

- [26] Lara Faoro and Lev B. Ioffe, 'Interacting tunneling model for two-level systems in amorphous materials and its predictions for their dephasing and noise in superconducting microresonators,' Phys. Rev. B 91 , 014201 (2015).
- [27] Clemens Mueller, Juergen Lisenfeld, Alexander Shnirman, and Stefano Poletto, 'Interacting two-level defects as sources of fluctuating high-frequency noise in superconducting circuits,' Physical Review B 92 (2015), 10.1103/PhysRevB.92.035442.
- [28] Hank Zumbahlen and the engineering staff Of Analog Devices, Linear Circuit Design Handbook (Newnes, 2008).
- [29] D. C. Mattis and J. Bardeen, 'Theory of the Anomalous Skin Effect in Normal and Superconducting Metals,' Phys. Rev. 111 , 412-417 (1958).
- [30] Jonas Zmuidzinas, 'Superconducting Microresonators: Physics and Applications,' Annu. Rev. Condens. Matter Phys. 3 , 169-214 (2012).
- [31] Jonathan J. Burnett, Andreas Bengtsson, Marco Scigliuzzo, David Niepce, Marina Kudra, Per Delsing, and Jonas Bylander, 'Decoherence benchmarking of superconducting qubits,' npj Quantum Inf. 5 , 1-8 (2019).
- [32] David Niepce, Jonathan J. Burnett, Marina Kudra, Jared H. Cole, and Jonas Bylander, 'Stability of superconducting resonators: Motional narrowing and the role of Landau-Zener driving of two-level defects,' Sci. Adv. 7 , eabh0462 (2021).
- [33] [Kimihiko Yasuda, Shozo Kawamura, and Koutaro Watanabe, 'Identification of Nonlinear Multi-Degree-ofFreedom Systems : Presentation of an Identification](http://dx.doi.org/10.1299/JSMEC1988.31.8)

[Technique,' (1988).](http://dx.doi.org/10.1299/JSMEC1988.31.8)

- [34] Carsten Hutter, Daniel Platz, E. A. Thol´ en, T. H. Hansson, and D. B. Haviland, 'Reconstructing Nonlinearities with Intermodulation Spectroscopy,' Phys. Rev. Lett. 104 , 050801 (2010).
- [35] Pauli Virtanen, Ralf Gommers, Travis E. Oliphant, Matt Haberland, Tyler Reddy, David Cournapeau, Evgeni Burovski, Pearu Peterson, Warren Weckesser, Jonathan Bright, St´ efan J. van der Walt, Matthew Brett, Joshua Wilson, K. Jarrod Millman, Nikolay Mayorov, Andrew R. J. Nelson, Eric Jones, Robert Kern, Eric Larson, C J Carey, ˙ Ilhan Polat, Yu Feng, Eric W. Moore, Jake VanderPlas, Denis Laxalde, Josef Perktold, Robert Cimrman, Ian Henriksen, E. A. Quintero, Charles R. Harris, Anne M. Archibald, Antˆ onio H. Ribeiro, Fabian Pedregosa, Paul van Mulbregt, and SciPy 1.0 Contributors, 'SciPy 1.0: Fundamental Algorithms for Scientific Computing in Python,' Nature Methods 17 , 261-272 (2020).
- [36] Daniel Forchheimer, Daniel Platz, Erik A. Thol´ en, and David B. Haviland, 'Model-based extraction of material properties in multifrequency atomic force microscopy,' Phys. Rev. B 85 , 195449 (2012).
- [37] Corey Rae H. McRae, Gregory M. Stiehl, Haozhi Wang, Sheng-Xiang Lin, Shane A. Caldwell, David P. Pappas, Josh Mutus, and Joshua Combes, 'Reproducible coherence characterization of superconducting quantum devices,' Appl. Phys. Lett. 119 (2021), 10.1063/5.0060370.
- [38] M. Simoen, Parametric interactions with signals and the vacuum , Ph.D. thesis, Chalmers University of Technology (2015).