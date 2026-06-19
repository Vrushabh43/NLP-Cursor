## Short Blocklength Error Correction Codes for Continuous-Variable Quantum Key Distribution

Kadir Gümü¸ s (1) , João dos Reis Frazão (1) , Boris Škori´ c (2) ,

Gabriele Liga (3) , Aaron Albores-Mejia (1) , Thomas Bradley (1) , and Chigo Okonkwo (1)

(1) High-Capacity Optical Transmission Laboratory, Electro-Optical Communications Group, Eindhoven University of Technology, The Netherlands, k.gumus@tue.nl

- (2) Dept. of Mathematics and Computer Science, Eindhoven University of Technology, The Netherlands
- (3) Information and Communication Theory Lab, Eindhoven University of Technology, The Netherlands

Abstract We introduce a two-step error correction scheme for reconciliation in continuous-variable quantum key distribution systems. Using this scheme, it is possible to use error correction codes with small blocklengths (1000 bits), increasing secret key rates at a distance of 140km by up to 7.3 times. ©2024 The Author(s)

## Introduction

Quantum key distribution (QKD) is a method for securely sharing keys between two parties, Alice and Bob, in the presence of an eavesdropper with access to a quantum computer [1] . Continuousvariable (CV) QKD is a variant of QKD allowing for sharing secret keys using conventional telecommunication equipment [2] . Compared to discretevariable QKD, two disadvantages that CV-QKD has are that the transmission distance is limited and that the implementation of the reconciliation is significantly more difficult [3] .

Reconciliation is part of the post-processing for a QKD system and is where the keys are generated in the case of CV-QKD. Works focusing on reconciliation [4]-[7] use long blocklengths ( 10 5 -10 6 bits), as it increases performance. These codes, however, are quite complex to implement on application-specific hardware. Additionally, for higher reconciliation efficiencies β ≥ 98% , the frame error rate (FER) approaches 1 very quickly, reducing key rates at longer distances.

A potential solution to these problems is using short blocklength error correction codes ( 10 3 -10 4 bits). These codes require fewer decoding iterations and take up fewer resources on hardware. In general, at high β , the FER is better than codes with long blocklengths. However, the error detection after decoding, which is often chosen to be a cyclic redundancy check (CRC) [4] , significantly affects β and makes short blocklength error correction codes infeasible.

This paper proposes a protocol for using short blocklength error correction codes for CV-QKD. We show that with this method, it is possible to perform reconciliation at high β ( ≥ 99% ) with reasonable FERs ( ≤ 87% ). Increases in secret key rates over a distance of 140km of up to 7.3 times are shown.

## Multi-dimensional Reconciliation

Multi-dimensional reconciliation is a commonly used reconciliation protocol for CV-QKD [8] . Our protocol, as shown in Fig. 1, is based on multidimensional reconciliation but includes a second decoding step. We first describe conventional multi-dimensional reconciliation.

At the start of reconciliation Alice has a string x of transmitted quadrature values, x = [ x 1 , x 2 , · · · , x N ] , where N is the blocklength of the code, and E [ x 2 i ] = 1 2 . Bob has a string of measured quadrature values y = [ y 1 , y 2 , · · · y N ] , which is a noisy version of x . The quantum channel over which Alice transmits the states is assumed to be an additive white Gaussian noise channel; therefore, y i = x i + z i . where z i ∼ N (0 , σ 2 z / 2) , where σ 2 z is the channel noise variance over both quadratures of the quantum state.

Using a random number generator, Bob generates a string of bits s = [ s 1 , s 2 , · · · , s k ] , where k = R · N with R being the rate of the code. Using an encoder, Bob calculates the codeword c belonging to s . The codeword is then converted to a sequence of BPSK symbols u through u i = ( -1) c i . Bob generates m ∈ R N using a mapping function m = M ( u , y ) and transmits m over the classical channel to Alice. Alice recovers m , and applies the inverse mapping function to obtain r = M -1 ( m , x ) , which is a noisy version of u .

Based on r , Alice calculates the log-likelihood ratios llr and uses them as input to her decoder. At the output of her decoder, she obtains a codeword estimate ˆ c . She then confirms whether ˆ c is a valid codeword. This confirmation step is codedependent, and in the case of LDPC codes, this would be equivalent to checking whether the syndrome is 0, i.e., ˆ cH T = 0 , where H is the parity check matrix of the code. If the codeword is not valid, a frame error has occurred, and the frame is discarded. Otherwise, ˆ c is a valid codeword, but this does not guarantee that ˆ c = c .

In conventional reconciliation, an error detection step takes place after error correction. The most common form of error detection is using a cyclic redundancy check (CRC) [4] . The last n crc bits of the estimated information bits ˆ s are transmitted by Alice over the classical channel to Bob. Bob compares these bits to the last n crc information bits s on his side. If the bits do not match, reconciliation fails, and the frame is discarded. If they are the same, Bob confirms this information with Alice and the information bits of the frame s and ˆ s are kept for privacy amplification. Importantly, the revealed bits are discarded when accepting the frame, as these are known to Eve. This has a slight effect on the reconciliation efficiency, as n crc information bits are discarded:

Fig. 1: An overview of short-blocklength reconciliation.

<!-- image -->

$$\beta = \frac { R \cdot N - n _ { c r c } } { N I _ { A B } } , \quad ( 1 ) \quad \begin{matrix} 0 \\ 0 \\ 1 \end{matrix}$$

where I AB is the mutual information between x and y .

The SKR for multi-dimensional reconciliation can then be given by:

$$S K R = ( 1 - F E R ) ( \beta I _ { A B } - \chi _ { B E } - \Delta _ { n } ) , \quad ( 2 ) \quad \text {not}$$

where χ BE is the Holevo information, and ∆ n is the finite-size penalty which is dependent on the privacy amplification blocklength N privacy [5] .

In Fig. 2 we show how n crc influences β depending on N for an R = 1 50 type-based protograph (TBP) LDPC code [9] . As N decreases, the effect on β crc increases. Even for n crc = 1 , a reduction in β of 5% occurs when N = 1000 . Hence, the use of small blocklength error correction codes becomes infeasible. Therefore, we have developed a reconciliation protocol where short blocklength error correction codes can be used, without applying a heavy penalty on β .

Fig. 2: The reduction in β vs. n crc for different error correction code blocklengths N .

<!-- image -->

## Short-Blocklength Reconciliation

Instead of a CRC, we use a second hard-decision high-rate error correction code, which effectively operates as an outer code, to remove any residual errors between ˆ s and s . Let the blocklength of the outer code be N out , which is a multiple of k . Wedo multi-dimensional reconciliation until A = N out /k frames have been accepted.

The number of reconciliation attempts K for this to happen is on average equal to E [ K ] = N out k · (1 -FER ) . These bits, w = [ s idx 1 , s idx 2 , · · · , s idx A ] , where idx denotes the indices of the accepted frames, are not a codeword of the outer code, hence the syndrome is not equal to 0 .

Alice sends idx over the classical channel to Bob. Bob computes the syndrome p of w and sends the syndrome under one-time pad encryption to Alice. Alice attempts to recreate w using the information bits of the accepted frames ˆ w = [ˆ s idx 1 , ˆ s idx 2 , · · · , ˆ s idx Nout /N ] . As there might be bit flips between w and ˆ w , Alice uses p and the decoder of the outer code to remove residual bit errors. Afterwards, Alice and Bob are left with ˆ w and w , which are the same with high probability, and they will use these bits for privacy amplification.

Having to one-time pad p requires some key material, which has to be deducted from the overall SKR. We can write this as a penalty R out on β :

$$\beta = \frac { R \cdot R _ { o u t } } { I _ { A B } } .$$

From our simulations, for all β and N , we observed that the bit error rate (BER) between w and ˆ w is relatively small (BER « 10 -4 ). Hence, the rate of the outer code R out can be very high, R out &gt; 0 . 999 , and the penalty to the reconciliation efficiency is negligible.

## Simulations

In Fig. 3, we show the FER against the reconciliation efficiency for codes with different blocklengths.

Fig. 3: β vs. FER for an R = 1 50 TBP-LDPC code for different blocklengths N . The right figure zooms in on the high FER regime. The threshold of the code was determined using density evolution.

<!-- image -->

For all blocklengths, we have generated an R = 1 50 TBP-LDPC code. For each point, we simulate until at least 100 frame errors have occurred. As N increases, the slope of the FER curve increases, indicating a better error correction performance. For N = 10 6 , the curve is steep and starts approaching the threshold of the code, while for smaller N , the FER stays high for β ≥ 90% . Note that focusing on the high FER regime, the FER of the short blocklength error correction codes is better when operating beyond the threshold of the code.

In Fig. 4 we show how this lower FER impacts the SKR over long distances for different N and β . For this CV-QKD system, we use the following parameters: quantum efficiency η = 0 . 6 , excess noise on Bob ξ Bob = 0 . 001 , electronic noise ν el = 0 . 01 , fibre attenuation α = 0 . 2 dB/km, and N privacy = 10 10 . The modulation variance V A is chosen such that at any distance d the mutual information I AB = R/β . For the outer code, we assume R out = 0 . 999 . We also show the DevetakWinter bound [10] , which is a lower bound on the maximum achievable SKR, and the Pirandola, Laurenza, Ottaviani and Banchi (PLOB) bound [11] , which is the upper bound on the SKR.

As β increases, the distance over which keys can be shared between Alice and Bob increases. The distance increase of β = 100% compared to β = 95% , which is a common value of β , is 37%, however, the key rates are lower because of the high FER. When N = 1000 , we observe an increase in SKR of 7.3 times compared to N = 10 6 at a distance of 140km. There is still a significant gap between the key rates reported here and the PLOB bound. A potential way to bridge the gap would be to use error correction codes with β &gt; 1 for the first decoding step of our short blocklength reconciliation protocol, however, the security proofs are not yet mature enough to accurately estimate the key rates.

## Conclusion

In this paper, we have proposed a reconciliation protocol for short blocklength error correction codes ( N = 10 3 ). We show that for long-distance (140km) transmission, using short blocklength error correction codes can increase SKRs by 7.3 times, while offering reduced decoding complexity. Future research will focus on designing good short blocklength error correction codes and security proofs for reconciliation with β &gt; 1 .

Fig. 4: SKR vs. d comparing an R = 1 50 TBP-LDPC code for N = 10 6 and N = 10 3 for different values of β . Also shown are the Devetak-Winter and PLOB bounds.

<!-- image -->

## Acknowledgements

This work was supported by the PhotonDelta GrowthFunds Programme on Photonics and by the Dutch Ministry of Economic Affairs (EZ), as part of the Quantum Delta NL KAT-2 programme on Quantum Communications. This work also acknowledges support of the European Union via the Marie Curie Doctoral Network QuNEST (Grant Agreement: 101120422) and the EIC Transition Grant project PAQAAL (under Grant Agreement 101213884)

## References

- [1] C. H. Bennett and G. Brassard, 'Quantum cryptography: Public key distribution and coin tossing', Theoretical Computer Science , vol. 560, pp. 7-11, 2014, ISSN: 03043975.
- [2] F. Grosshans and P. Grangier, 'Continuous variable quantum cryptography using coherent states', Phys. Rev. Lett. , vol. 88, p. 057 902, 5 2002.
- [3] S. Yang, Z. Yan, H. Yang, et al. , 'Information reconciliation of continuous-variables quantum key distribution: Principles, implementations and applications', EPJ Quantum Technology , vol. 10, no. 1, p. 40, 2023.
- [4] M. Milicevic, C. Feng, L. M. Zhang, and P . G. Gulak, 'Quasi-cyclic multi-edge LDPC codes for long-distance quantum cryptography', npj Quantum Information , vol. 4, no. 1, 2018.
- [5] K. Gümü¸ s, J. dos Reis Frazão, V. van Vliet, et al. , 'Rateadaptive reconciliation for experimental continuousvariable quantum key distribution with discrete modulation over a free-space optical link', Journal of Lightwave Technology , 2025.
- [6] E. E. Cil and L. Schmalen, 'Rate-adaptive protographbased raptor-like LDPC code for continuous-variable quantum key distribution', in Photonic Networks and Devices , Optica Publishing Group, 2024, JTu1A-51.
- [7] H. Mani, T. Gehring, P. Grabenweger, B. Ömer, C. Pacher, and U. L. Andersen, 'Multiedge-type low-density parity-check codes for continuous-variable quantum key distribution', Physical Review A , vol. 103, no. 6, p. 062 419, 2021.
- [8] A. Leverrier, R. Allé aume, J. Boutros, G. Zémor, and P . Grangier, 'Multidimensional reconciliation for a continuous-variable quantum key distribution', Physical Review A , vol. 77, no. 4, 2008.
- [9] K. Gümü¸ s and L. Schmalen, 'Low rate protograph-based LDPC codes for continuous variable quantum key distribution', Proc. ISWCS 2021 , 2021.
- [10] I. Devetak and A. Winter, 'Distillation of secret key and entanglement from quantum states', Proceedings of the Royal Society A: Mathematical, Physical and engineering sciences , vol. 461, no. 2053, pp. 207-235, 2005.
- [11] S. Pirandola, R. Laurenza, C. Ottaviani, and L. Banchi, 'Fundamental limits of repeaterless quantum communications', Nature communications , vol. 8, no. 1, p. 15 043, 2017.