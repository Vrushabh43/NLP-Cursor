## Dependable Classical-Quantum Computer Systems Engineering

Edoardo Giusto ∗ , Santiago Nu˜ nez-Corrales † , Phuong Cao † ,

Alessandro Cilardo ∗ , Ravishankar K. Iyer ‡ , Weiwen Jiang ∥ , Paolo Rech § , Flavio Vella § ,

Bartolomeo Montrucchio ¶ , Samudra Dasgupta ∗∗ , and Travis S. Humble ∗∗

∗ University of Naples Federico II, Italy - egiusto@ieee.org

† National Center for Supercomputing Applications, Urbana, IL, US

‡ University of Illinois Urbana-Champaign, US

§ University of Trento, Italy

¶ Politecnico di Torino, Italy

∥ George Mason University, VA, US

∗∗ Oak Ridge National Laboratory, TN, US

Abstract -Quantum Computing (QC) offers the potential to enhance traditional High-Performance Computing (HPC) workloads by leveraging the unique properties of quantum computers, leading to the emergence of a new paradigm: HPC-QC. While this integration presents new opportunities, it also brings novel challenges, particularly in ensuring the dependability of such hybrid systems. This paper aims to identify integration challenges, anticipate failures, and foster a diverse co-design for HPC-QC systems by bringing together QC, cloud computing, HPC, and network security. The focus of this emerging inter-disciplinary effort is to develop engineering principles that ensure the dependability of hybrid systems, aiming for a more prescriptive co-design cycle. Our framework will help to prevent design pitfalls and accelerate the maturation of the QC technology ecosystem. Key aspects include building resilient HPC-QC systems, analyzing the applicability of conventional techniques to the quantum domain, and exploring the complexity of scaling in such hybrid systems. This underscores the need for performance-reliability metrics specific to this new computational paradigm.

Index Terms -Hybrid Classical-Quantum systems, HPC, quantum computing, dependability, reliability, resiliency, security, reproducibility

## I. INTRODUCTION

Exploiting the expected potential benefits Quantum Computing (QC) across scientific and engineering applications [1] will require integrating QCs into standard HPC infrastructures, already the backbone of scientific computing. This scenario ushers in a new computational paradigm: HPC-QC [2]. Such paradigm entails the efficient and dependable incorporation of QPUs into standard HPC workflows [3]-[5]. Scaling up emerging Noisy Intermediate-Scale Quantum (NISQ) devices and integrating them with HPC infrastructures pose significant engineering challenges. Such classical-quantum integration has triggered exploration of multiple hardware [2] and software [3] pathways starting from a model of Quantum Processing Units (QPUs) as remotely accessible hardware accelerators, akin to Graphics processing Units (GPUs), to much tighter, direct coupling within HPC systems. Recent advances highlight the integration of QPUs as HPC accelerators [6],

Fig. 1: The Venn diagram highlights the intersection of reproducibility, resiliency and security in creating dependable computing systems.

<!-- image -->

[7], the conceptualization of HPC-QPU enablers [3], and the development of quantum kernels for scientific applications [4].

In this paper, we highlight the need for dependable HPC-QC systems engineering by describing how aspects of dependability usually found in HPC infrastructure will apply to quantum platforms as their integration to classical resources deepens. We do so by identifying how reproducibility , resiliency , and security &amp; privacy (Fig. 1) fit the new HPC-QC paradigm. These three pillars make up the definition of dependability of a system. The complexity derived from the intersection across pillars is non-trivial in emerging HPC-QC environments, and calls for an all-encompassing solution from a high-level view of computing architecture (Figure 2).

Resiliency concerns both hardware and software at a very low abstraction level, concerning the compilation, verification, and execution of code on heterogeneous systems. A layer above we find reproducibility, managing the execution of a scientific calculation workflow in such a way that the produced output is consistent and repeatable between different executions and systems. Security eventually encompasses the whole spectrum of the system components, ensuring that the aforementioned workflow is not hampered by an external agent and that the processed data are untampered with and kept private.

Fig. 2: Dependability pillars in HPC-QC high-level architecture

<!-- image -->

The rest of the paper is organized in the following way: Sections II, III and IV address each of the pillars of dependability, while Section V brings them all together, laying out in the quest of dependable HPC-QC scale-up. Eventually, Section VI wraps up the discussion.

## II. REPRODUCIBILITY

Reproducibility is foundational to science and the ability to communicating and transferring knowledge reliably. In the presence of noise, quantum computers may become unreliable, in a formal sense, as their behaviors are no longer strictly predictable. Statistical notions of operations and their outcomes become necessary for describing such noisy quantum computers. Moreover, results from quantum programs executed on noisy devices raise concerns for how to statistically quantify reproducibility in the presence of noise and errors [8]-[11].

## A. Accuracy vs. stability

The accuracy of a QC system represents the agreement between the observed and expected results of the QC program. For conventional analysis, binary outcomes from measuring the quantum register after execution of a quantum program (currently expressed as a quantum circuit) constitute the objects of interest. Histograms drawn from these outcomes characterize the stability of the computation, which varies due to noise sources unpredictably due to non-stationary stochastic processes and their statistical observables [12]. Whereas accuracy is a measure of the error in the calculation itself, stability quantifies the fluctuations in such observations with respect to time. Large and unpredictable fluctuations in these are a fundamental concern for the reproducibility of results.

These uncertainties arise since practical efforts to build quantum computers introduce unexpected sources of noise through various types of imperfections [13], [14]. In consequence, imperfections cause quantum devices to depart from idealized computing behavior. Example noise sources include spontaneous decay of qubits, leakage from the computational subspace, undesired external coupling due to spurious charge and magnetic fields, as well as inter-qubit cross-talk from capacitive coupling. Similarly, noise in the control system arises from imperfections in the fundamental gate operations, e.g., in superconducting qubits, distortion and drift in microwave pulses often lead to errors. Externally, a multitude of mechanisms are put in place to isolate the quantum device and stave off decoherence as it interacts its environment (e.g., ultra-low temperatures, ultra-low vacuum). Thus anticipating how HPC environments will impinge on QC device operation becomes inescapable.

Remark 1: The non-stationary noise in contemporary quantum devices presents a challenge for computational reproducibility that impacts the verification and validation of quantum computing demonstrations and hinders the production of trustworthy results.

## B. Measuring quantum reproducibility

To measure reproducibility in quantum computing systems, we extend the analysis of stability to discrete distributions with binary outcomes { f b } from quantum stochastic processes. To achieve this, we choose the Hellinger distance among various statistical distance measures as it extends to both discrete and continuous distributions, thus satisfying the requirements of a distance metric for comparison. For distributions f ( b ) and g ( b ) , the Hellinger distance H ( f, g ) ∈ [0 , 1] [15] is defined as

$$H ( f , g ) = \sqrt { 1 - B ( f , q ) }$$

with Bhattacharyya coefficient

$$B ( f , g ) = \sum _ { b } \sqrt { f ( b ) g ( b ) }$$

Outcomes are δ -reproducible with tolerance ϵ when

$$\Pr ( H ( f , g ) \leq \epsilon ) \geq 1 - \delta$$

For quantum programs, f and g are computed for a given quantum circuit using multiple shots. As an example, the minimum sample size L min required for reproducibility for the Bernstein-Vazirani algorithm can be shown to be a nonlinear function of the confidence level 1 -δ and the accuracy threshold ϵ :

$$L _ { \min } = z _ { \delta } ^ { 2 } \frac { p _ { r } ^ { - 2 } - 1 } { p _ { r } ^ { - 2 } ( 1 - \epsilon ) ^ { 2 } - 1 }$$

where z represents the standard normal variable (with mean 0 and variance 1), z δ denotes the particular point where Pr ( z ≥ z δ ) = 1 -δ , and p r signifies the probability of successfully identifying the secret string r using the Bernstein-Vazirani algorithm in the presence of noise. A pressing concern is what values of the tolerances, ϵ and δ , are sufficient for real-world applications of dependable QC.

## III. RESILIENCY

Resiliency characterizes the ability of a system to maintain a desired state given a range of perturbations, making it trusted and effective to accomplish its functionality, and capable of providing detection and graceful degradation of function and performance [16]. In computer systems, hardware and software components are expected to undertake this responsibility. At the software level, executable code must fulfill its purpose. To do so, compilation of a quantum workload from circuits to pulses must be verified to acquire trustworthiness of compiled output. At the hardware level, faults arising in one or multiple physical units of the system should ideally not disrupt the execution flow or alter the reproducibility of results; more realistically, quantum program execution should be accompanied by information about the impact of faults. We briefly review here compilation/transpilation and verification of quantum circuits, as well as faults in classical and quantum systems, and discuss both classical and quantum techniques to counteract such faults, analyzing whether it is possible to apply classical dependability techniques to the quantum domain.

## A. Compilation and verification

Compiling (or transpiling) quantum circuits involves program transformations that match program constructs to quantum hardware capabilities and constraints. Constraints include native gate sets, qubit connectivity, coherence time, and qubit fidelity among others. This process seeks to optimize circuit performance while mitigating the effects of hardware limitations [17], [18]. In tandem, quantum circuit verification is critical to ensure correctness and reliability. All this entails addressing both classical and quantum aspects derived from the probabilistic nature of quantum computation and noisy hardware. Existing methods include both simulation in classical computers and formal techniques which rigorously prove the correctness of the circuit [19].

Compilation and verification of quantum programs must then be put in the context of hybrid HPC-QC environments. This brings a plethora of new concerns such as workload balancing optimization for specific and heterogeneous architectures (CPU+GPU+TPU+QPU), enabling parallel execution on such heterogeneous architectures, performance tuning, profiling and program optimization. Formal verification must then be overlaid across this complexity to guarantee that requirements are fulfilled, across the entire composite system.

Remark 2: Compilation processes must be adapted to heterogeneous HPC-QC architectures. Quantum program execution must be verified across the entire stack, from high-level specifications to sequences of pulses.

Fig. 3: Classical techniques available at each level of a system.

<!-- image -->

Fig. 4: Resiliency measures in relation to the fault cycle of a classical system.

<!-- image -->

## B. Fault management

Classical-quantum programs may fail to run for reasons well beyond compilation and verification errors. More generally, system or application failure can be caused by faults/errors at different levels of the system hierarchy (e.g., hardware, operating system, communication layer, middleware, or application). Their cascading effects thus call for a system perspective: we need to anticipate and engineer mechanisms that produce resilient computing systems as a result. Figure 3 poses relevant questions across the system hierarchy prior to building a resilient computing system [20].

As with reproducibility, we need metrics to quantify the resiliency of an HPC-QC system. We draw from prior research [20] and suggest four metrics for the purpose at hand. These metrics are quantified through mean time to failure (MTTF) or mean time to error (MTTE), mean time between failures (MTBF), mean time to catastrophic failure (MTTCF), fault latency, error latency, and repair time. These metrics determine the extent of a fault cycle (Figure 4).

- Reliability: continuity of service delivery in the presence of hazards.
- Maintainability: the probability that the system will be repaired within a time less than t .
- Availability: service delivery for the alternation of the delivery and interruptions.
- Safety: time to catastrophic failure and unsafe system states.

In classical computing systems, particle impacts constitute a major source of faults. These are a naturally occurring byproduct of cosmic ray decay which corrupts stored values and the executed operations in both classical and quantum devices. In a classical CMOS transistor, ionizing particles generate electron-hole pairs, releasing and depositing charge. A sufficiently large deposited charge forces a transistor state to flip with three possible consequences. There may not be an effect on program output if the fault is masked, or the corrupted data is not used. In another case, known as silent data corruption (SDC), the program yields incorrect results yet continues to run. Finally, a bit flip may trigger a detected unrecoverable error (DUE) in which the program crashes or the device is forced to reboot.

In QC devices, the impact of particles alters the state of qubit(s) by forcing them into decoherence. As an example, a fault mechanism in superconducting devices involves the generation of electron-hole pairs in the silicon substrate of the quantum chip, which in turn break Cooper pairs in the Josephson junction forming quasiparticles, that rapidly give rise to long-lasting phonons responsible for spreading the energy across the lattice of the quantum computer's substrate and interconnections [21], [22]. While in a classical transistor the state is temporary reversed only if the deposited charge by the particle is higher than a threshold, in a qubit, even a single Cooper pair break is sufficient to disturb the quantum equilibrium, thus modifying the logic status.

Field experiments performed by Google AI on a 25 qubits array showed radiation-induced faults every tens of seconds [23]. The reported error rate is several orders of magnitude higher than the one of modern CMOS technology. As a reference, the whole Titan supercomputer (composed of 14,000 nodes) has an error rate in the order of one error every few hours [24]. Finally, a Quantum Vulnerability Factor has been recently proposed to quantify such effects at different levels of abstraction in the execution of quantum circuits [25], [26]. At the physical level, hardware improvements are continuously proposed to mitigate internal and external noise factors [27], [28].

Remark 3: Faults add randomness on top of intrinsic noise, changing the output probability distribution of the computation. Failures are likely to have larger impact on qubits than on classical CMOS transistors, and disrupt qubit behavior for a longer time.

HPC systems have led to the development of widespread techniques to handle faults (Fig. 3). Checkpointing involves periodically saving the state of a running computation to restart from in case of failure. While inapplicable to quantum states due to the exponential growth in information and inability to reconstruct arbitrary states, one can envision classical-like portions of quantum circuits where this may be possible. More generally, classical parts of quantum algorithms such as the variational quantum eigensolver (VQE) may be well suited for checkpointing.

Replication instead consists of running the same on multiple processing units simultaneously. In QC, this is the main method used to estimate the resulting state vector's probabilities statistically. Finally, job resubmission entails re-executing failed jobs, potentially on different resources, to improve the chances of successful completion. This can be done in QC if an error detection technique is implemented to identify sporadic external errors such as those induced by radiation, but not for errors due to inherent decoherence.

In the same direction, quantum error suppression (QES), quantum error mitigation (QEM) and quantum error correction (QEC) have drawn substantial interest. QES integrates resiliency directly into the hardware design, for instance by optimizing pulse engineering to minimize errors during gate operations [29]. QEM addresses errors after their occurrence by statistically correcting noise effects on the final output [30]. QEC employs redundancy across multiple physical qubits to detect and correct errors. This is not without challenges due to resource overhead and complex operations [31], as well as the presence of correlated faults [27].

Remark 4: The Threshold and No-cloning Theorems place fundamental limitations on our ability to apply classical techniques to quantum computing systems. Classicalquantum systems will force the community to re-think resiliency across the stack.

## IV. SECURITY &amp; PRIVACY

The complex interfaces between traditional HPC, QC, and emerging applications introduce hosts of new security issues:

- Challenge 1 : The security of classical systems is threatened Quantum-driven adversaries , for example, traditional cryptography based on large integer factorization such as RSA can be broken by QC running Shor's algorithm.
- Challenge 2 : The security of Quantum systems themselves , for example, the confidentiality of information, the integrity of data, and the availability of Quantum Cloud services to the end user.
- Challenge 3 : The privacy of user data and regulations when using HPC-QC to process sensitive research and health data such as Controlled Unclassified Information (CUI) and Health Insurance Portability and Accountability Act (HIPAA) data.

We further lay out research directions for each of the challenging threat models in this hybrid domain as follows.

A. Quantum-driven adversaries against Quantum and Classical systems

With more powerful computation capabilities, attackers will leverage practical QPUs to upend traditional security assumptions, expected to break classical encryption in the next few decades. In this context, the problem of adopting latticebased cryptography is critically important. Moreover, as GPUs become more powerful, we observe artificial intelligencedriven malware that automatically learns when and how to launch stealth data-stealing campaigns to minimize their footprints [32].

Remark 5: Modern quantum-driven attacks will leverage the power of QPUs to

- 1) mask the presence of attacks as natural faults
- 2) adapt attack traces to minimize their footprint, and
- 3) learn when, how, and where to launch attacks in a QC stack to maximize damage.

## B. Attacks at the surface of HPC-QC integration

New attack surfaces will emerge as physicists and computer scientists join forces to integrate HPC and QC, as both sides will make different assumptions on HPC-QC interfaces. On the classical side, access control mechanisms such as federated authentication, key management, and computer network measurements must be adapted to the hybrid workload and data being transferred through the HPC-QC interface to gain visibility on adversaries. As Quantum Key Distribution (QKD) systems and control mechanisms mature, the classical systems become the weakest link in HPC-QC integration and need careful security engineering and monitoring across the stack. One of the possible approaches to security and performance issues in this context would be the development of a Quantum Internet able to interconnect the quantum part of HPC-QC systems.

- Remark 6: Preemptive attack detection [33] at the surface of HPC-QC is critical to ensure secure integration, which requires
- 1) inventing a new instrument that monitors quantum network data
- 2) distributing security monitoring instruments across networks for early detection of attacks
- 3) defining checkpointing and remedy mechanisms to respond to attacks.

## C. Privacy concerns in integrated HPC-QC platforms

Privacy-Perserving QC is critical as QC services, presumed to be untrusted, will be adopted in domains where data privacy and intellectual property are an inherent requirement, such as drug discovery, financial optimization, and machine learning for health applications.

- 1) Pure cryptography-based privacy-preserving approach: Confidential QC approaches adopt classical cryptographic schemes for privacy-preserving computing, i.e. Fully Homomorphic Encryption (FHE) and Multi-Party Computation (MPC). In particular, Blind Quantum Computing (BQC) [34] partially delegates quantum computation to a remote server without disclosing the computation itself. More recent proposals for BQC relaxed this requirement [35], but still need an assumption of multiple non-colluding servers, which may

not be realistic in practice. Quantum Homomorphic Encryption (QHE) [36], on the other hand, enables the quantum computer to work on encrypted quantum data and produce an encrypted outcome, without accessing data, similar to its classical counterpart, but it remains impractical as it involves exponential computational overheads. As an interesting development, there are some attempts to come up with special-purpose cryptographic schemes for privacy-preserving computing, i.e. schemes which can only be applied for specific types of computation. For example, the authors of [37] propose a privacy-preserving scheme specific to Quantum Approximate Optimization Algorithm, which achieves realistic performance and proves to be feasible on current and near-term quantum computers.

- 2) A Trusted Quantum Computing Base (TQCB) for privacy-preserving: Classical Trusted Execution Environments (TEEs) rely on hardware that isolates computation within a chip, offering security. Quantum computers, with their distributed data and components, pose challenges to redefining Trusted Computing Base [38] as researchers are exploring ways to establish natively quantum TEEs for protecting sensitive data.
2. Remark 7: Standardizing data privacy and security specifications using mathematical formalisms, and more importantly making specifications executable , is critically needed to enable:
- 1) secure-by-construction data access and sharing protocols,
- 2) formal verification of the entire quantum computing stacks and synthesizing corresponding correct implementations, and
- 3) testbed for evaluating different attack scenarios such as data leaks or compromising root of trust.

We expect to engage with NIST to formally define the above standard needs.

## V. DISCUSSION

To become a dependable technology capable of delivering actual value to users with scientific applications in need of performance, quantum hardware platforms will need to adapt to the pressures and environments HPC systems already operate. The question of how to successfully perform this HPC-QC integration is far from answered since differences between classical and quantum technologies, and the state of maturity across both fields introduce additional confounding factors.

Our work -as well as cited works from otherssuggests that a new area of research is needed at the intersection between classical HPC and quantum computing. The title of this article, Dependable Classical-Quantum Computing Systems Engineering , deliberately qualifies the nature of the endeavor as one drawing heavily from scientific principles to articulate usable systems, not to advance the science of devices per se . Experimental quantum testbeds dedicated to research have been instrumental in advancing the state of the art in

## Roadmap: Dependable Classical-Quantum Computing

<!-- image -->

System Complexity

Fig. 5: Roadmap for Dependable HPC-QC.

quantum hardware; our views suggest we need actual HPCQC testbeds dedicated to a holistic and rigorous interrogation of dependability.

The three pillars of dependability are deeply intertwined into HPC-QC systems: the more application and research users depend on these, the more sophisticated the ability of the system to satisfy essential guarantees must be. Starting from the high-level definition of a scientific workload, application users are concerned with the solution to their problem -i.e. computing as a service-, with little to no practical interest in the lower levels of the stack that satisfy their needs. However, application users do concern themselves with performance, reproducibility, resiliency, and security in their scientific work. Building dependable classical-quantum hardware and software components multiplies the complexity of standard dependability concerns across HPC.

At a technical level, the ability to make progress across multiple directions requires transparent access to software and hardware systems. HPC systems are currently mostly structured around open-source stacks where the code is fully inspectable, and the hardware can be easily interrogated at every meaningful level. A similar ecosystem of tools and software for classical-quantum computing has yet to consolidate. We do observe an increasing number of standard packages used in quantum hardware research and practice; ensuring these remain accessible and more are produced constitutes a substantial objective toward dependable HPC-QC. In particular, reference implementations that are open, transparent, and accessible become highly desirable.

We believe it is necessary to fully engage the HPC, networking, and QC communities, with three main goals. The first goal is to delimit specific problem areas where we only have intuitions of how to address them so far: the collection of remarks derived here points to joint, interdisciplinary work to address multiple sources of uncertainty. The second goal is to identify milestones in the development of dependable HPC-QC systems that synergistically benefit from ongoing work by members of the QC community. These milestones must be connected to progress in quantum hardware testbeds and accelerate hardware-software co-design of full systems. A successful selection of milestones will be characterized by a healthy balance between new avenues of exploration and effective ways to discard unproductive research directions. Third and last, we seek to foster a larger conversation resulting in a roadmap akin to that in Figure 5 capable of fully realizing a long-term, sustainable HPC-QC integration program.

## VI. CONCLUSION

This article shows that, despite experience gathered across several decades of HPC practice, the introduction of QC brings new and interesting challenges. Ensuring the dependability of hybrid systems is paramount in order to leverage such computational power for scientific computing applications. This paper describes the three pillars of dependability - reproducibility, resiliency, and security &amp; privacy - in the context of HPC-QC integration. Reproducibility is impacted by quantum noise, while classical approaches in the resiliency domain may have fundamental shortcomings if applied to the quantum realm. Security threats are amplified due to the intricate integration of such heterogeneous components. Overcoming the dependability challenges is crucial for enabling reliable, high-performance scientific applications leveraging quantum resources. This is a call to arms to experts across HPC, QC, and cybersecurity communities to come together to address these issues. We argue that developing a combined co-design approach, supported by open testbeds, can pave the way towards dependable, robust HPC-QC platforms that can deliver on the revolutionary promise of this emerging paradigm.

## REFERENCES

- [1] Yuri Alexeev, Maximilian Amsler, Paul Baity, Marco Antonio Barroca, Sanzio Bassini, Torey Battelle, Daan Camps, David Casanova, Frederic T Chong, Charles Chung, et al. Quantum-centric supercomputing for materials science: A perspective on challenges and future directions. arXiv preprint arXiv:2312.09733 , 2023.
- [2] Keith A Britt and Travis S Humble. High-performance computing with quantum processing units. ACM Journal on Emerging Technologies in Computing Systems (JETC) , 13(3):1-13, 2017.
- [3] Nishant Saurabh, Shantenu Jha, and Andre Luckow. A conceptual architecture for a quantum-hpc middleware. In 2023 IEEE International Conference on Quantum Software (QSW) , pages 116-127. IEEE, 2023.
- [4] AY Matsuura and Timothy G Mattson. Introducing the quantum research kernels: Lessons from classical parallel computing. arXiv preprint arXiv:2211.00844 , 2022.
- [5] Wei Tang and Margaret Martonosi. Distributed quantum computing via integrating quantum and classical computing. Computer , 57(4):131-136, 2024.
- [6] Alexander J McCaskey, Eugene F Dumitrescu, Dmitry Liakh, Mengsu Chen, Wu-chun Feng, and Travis S Humble. A language and hardware independent approach to quantum-classical computing. SoftwareX , 7:245-254, 2018.
- [7] Alexander J McCaskey, Dmitry I Lyakh, Eugene F Dumitrescu, Sarah S Powers, and Travis S Humble. Xacc: a system-level software infrastructure for heterogeneous quantum-classical computing. Quantum Science and Technology , 5(2):024002, 2020.
- [8] Samudra Dasgupta and Travis S Humble. Characterizing the reproducibility of noisy quantum circuits. Entropy , 24(2):244, 2022.
- [9] Samudra Dasgupta and Travis S Humble. Assessing the stability of noisy quantum computation. In Quantum Communications and Quantum Imaging XX , volume 12238, pages 44-49. SPIE, 2022.
- [10] Zhirui Hu, Robert Wolle, Mingzhen Tian, Qiang Guan, Travis Humble, and Weiwen Jiang. Toward consistent high-fidelity quantum learning on unstable devices via efficient in-situ calibration. In 2023 IEEE International Conference on Quantum Computing and Engineering (QCE) , volume 1, pages 848-858. IEEE, 2023.
- [11] Priyabrata Senapati, Zhepeng Wang, Weiwen Jiang, Travis S Humble, Bo Fang, Shuai Xu, and Qiang Guan. Towards redefining the reproducibility in quantum computing: A data analysis approach on nisq devices. In 2023 IEEE International Conference on Quantum Computing and Engineering (QCE) , volume 1, pages 468-474. IEEE, 2023.
- [12] Samudra Dasgupta and Travis S Humble. Reliability of noisy quantum computing devices. arXiv preprint arXiv:2307.06833 , 2023.
- [13] Yvonne Y Gao, M Adriaan Rol, Steven Touzard, and Chen Wang. Practical guide for building superconducting quantum devices. PRX Quantum , 2(4):040202, 2021.
- [14] Karen Wintersperger, Florian Dommert, Thomas Ehmer, Andrey Hoursanov, Johannes Klepsch, Wolfgang Mauerer, Georg Reuber, Thomas Strohm, Ming Yin, and Sebastian Luber. Neutral atom quantum computing hardware: performance and end-user perspective. EPJ Quantum Technology , 10(1):32, 2023.
- [15] Bruce G Lindsay. Efficiency versus robustness: the case for minimum hellinger distance and related methods. The annals of statistics , 22(2):1081-1114, 1994.
- [16] Simon R Goerger, Azad M Madni, and Owen J Eslinger. Engineered resilient systems: A dod perspective. Procedia Computer Science , 28:865-872, 2014.
- [17] Colin Campbell, Frederic T Chong, Denny Dahl, Paige Frederick, Palash Goiporia, Pranav Gokhale, Benjamin Hall, Salahedeen Issa, Eric Jones, Stephanie Lee, et al. Superstaq: Deep optimization of quantum programs. In 2023 IEEE International Conference on Quantum Computing and Engineering (QCE) , volume 1, pages 1020-1032. IEEE, 2023.
- [18] Kaitlin N Smith and Mitchell A Thornton. A quantum computational compiler and design tool for technology-specific targets. In Proceedings of the 46th International Symposium on Computer Architecture , pages 579-588, 2019.
- [19] Robert Wille and Lukas Burgholzer. Verification of quantum circuits. Handbook of Computer Architecture , pages 1-28, 2022.
- [20] Ravishankar K. Iyer Zbigniew T. Kalbarczyk, Nithin M. Nakka. Dependable Computing: Design and Assessment , chapter 1. ISBN: 978-1-118-70944-3, John Wiley &amp; Sons, 2024.
- [21] Antti P. Veps¨ al¨ ainen, Amir H. Karamlou, John L. Orrell, Akshunna S. Dogra, Ben Loer, Francisca Vasconcelos, David K. Kim, Alexander J. Melville, Bethany M. Niedzielski, Jonilyn L. Yoder, Simon Gustavsson, Joseph A. Formaggio, Brent A. VanDevender, and William D. Oliver. Impact of ionizing radiation on superconducting qubit coherence. Nature , 584(7822):551-556, 2020.
- [22] C. D. Wilen, S. Abdullah, N. A. Kurinsky, C. Stanford, L. Cardani, G. D'Imperio, C. Tomei, L. Faoro, L. B. Ioffe, C. H. Liu, A. Opremcak, B. G. Christensen, J. L. DuBois, and R. McDermott. Correlated charge noise and relaxation errors in superconducting qubits. Nature , 594(7863):369-373, 2021.
- [23] Matt McEwen, Lara Faoro, Kunal Arya, Andrew Dunsworth, Trent Huang, Seon Kim, Brian Burkett, Austin Fowler, Frank Arute, Joseph C Bardin, et al. Resolving catastrophic error bursts from cosmic raysrin large arrays of superconducting qubits. Nature Physics , 18(1):107-111, 2022.
- [24] D. Tiwari, S. Gupta, J. Rogers, D. Maxwell, P. Rech, S. Vazhkudai, D. Oliveira, D. Londo, N. DeBardeleben, P. Navaux, L. Carro, and A. Bland. Understanding GPU errors on large-scale HPC systems and the implications for system design and operation. In 2015 IEEE 21st International Symposium on High Performance Computer Architecture (HPCA) , pages 331-342, 2015.
- [25] Daniel Oliveira, Edoardo Giusto, Betis Baheri, Qiang Guan, Bartolomeo Montrucchio, and Paolo Rech. A systematic methodology to compute the quantum vulnerability factors for quantum circuits. IEEE Transactions on Dependable and Secure Computing , pages 1-15, 2023.
- [26] Daniel Oliveira, Edoardo Giusto, Emanuele Dri, Nadir Casciola, Betis Baheri, Qiang Guan, Bartolomeo Montrucchio, and Paolo Rech. Qufi: a quantum fault injector to measure the reliability of qubits and quantum circuits. In 2022 52nd Annual IEEE/IFIP International Conference on Dependable Systems and Networks (DSN) , pages 137-149. IEEE, 2022.
- [27] John M Martinis. Saving superconducting quantum processors from decay and correlated errors generated by gamma and cosmic rays. npj Quantum Information , 7(1):90, 2021.
- [28] Matt McEwen, Kevin C Miao, Juan Atalaya, Alex Bilmes, Alex Crook, Jenna Bovaird, John Mark Kreikebaum, Nicholas Zobrist, Evan Jeffrey, Bicheng Ying, et al. Resisting high-energy impact events through gap engineering in superconducting qubit arrays. arXiv preprint arXiv:2402.15644 , 2024.
- [29] Pranav S Mundada, Aaron Barbosa, Smarak Maity, Yulun Wang, Thomas Merkh, TM Stace, Felicity Nielson, Andre RR Carvalho, Michael Hush, Michael J Biercuk, et al. Experimental benchmarking of an automated deterministic error-suppression workflow for quantum algorithms. Physical Review Applied , 20(2):024034, 2023.
- [30] Zhenyu Cai, Ryan Babbush, Simon C Benjamin, Suguru Endo, William J Huggins, Ying Li, Jarrod R McClean, and Thomas E O'Brien. Quantum error mitigation. Reviews of Modern Physics , 95(4):045005, 2023.
- [31] Joschka Roffe. Quantum error correction: an introductory guide. Contemporary Physics , 60(3):226-245, 2019.
- [32] Keywhan Chung, Phuong Cao, Zbigniew T. Kalbarczyk, and Ravishankar K. Iyer. stealthml: Data-driven malware for stealthy data exfiltration. In 2023 IEEE International Conference on Cyber Security and Resilience (CSR) , pages 16-21, 2023.
- [33] Phuong Cao, Eric Badger, Zbigniew Kalbarczyk, Ravishankar Iyer, and Adam Slagell. Preemptive intrusion detection: Theoretical framework and real-world measurements. In Proceedings of the 2015 Symposium and Bootcamp on the Science of Security , pages 1-12, 2015.
- [34] Joseph F. Fitzsimons. Private quantum computation: an introduction to blind quantum computing and related protocols. npj Quantum Information , 3(1):23, Jun 2017.
- [35] He-Liang Huang, Qi Zhao, Xiongfeng Ma, Chang Liu, Zu-En Su, XiLin Wang, Li Li, Nai-Le Liu, Barry C. Sanders, Chao-Yang Lu, and Jian-Wei Pan. Experimental blind quantum computing for a classical client. Phys. Rev. Lett. , 119:050503, Aug 2017.
- [36] Yingkai Ouyang, Si-Hui Tan, and Joseph Fitzsimons. Quantum homomorphic encryption from quantum codes. Physical Review A , 2015.
- [37] Ramin Ayanzadeh, Ahmad Mousavi, Narges Alavisamani, and Moinuddin Qureshi. Enigma: Privacy-preserving execution of qaoa on untrusted quantum computers, 2023.
- [38] T. Trochatos, C. Xu, S. Deshpande, Y. Lu, Y. Ding, and J. Szefer. A quantum computer trusted execution environment. IEEE Computer Architecture Letters , 22(02):177-180, jul 2023.