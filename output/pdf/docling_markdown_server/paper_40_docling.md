## BI-based Reasoning about Quantum Programs with Heap Manipulations

BONAN SU, Department of Computer Science and Technology, Tsinghua University, China

LI ZHOU, Key Laboratory of System Software (Chinese Academy of Sciences) and State Key Laboratory of Computer Science, Institute of Software, Chinese Academy of Sciences, China

YUAN FENG, Department of Computer Science and Technology, Tsinghua University, China

MINGSHENG YING, Centre for Quantum Software and Information, University of Technology Sydney, Australia

Weprovide well-founded semantics for a quantum programming language Qwhile-hp with heap manipulations, where allocation statements follow a dirty pattern, meaning that newly allocated qubits can nondeterministically assume arbitrary initial states. To thoroughly characterize heap manipulations in the quantum setting, we develop a quantum BI-style logic that includes interpretations for separating implication ( - ∗ ) and separating conjunction ( ∗ ). We then adopt this quantum BI-style logic as an assertion language to reason about heap-manipulated quantum programs and present a quantum separation logic which is sound and relatively complete. Finally, we apply our framework to verify the correctness of various practical quantum programs and to prove the correct usage of dirty ancilla qubits.

Additional Key Words and Phrases: Bunched Implication, Quantum Programs, Heap Manipulation, Separation Logic, Dirty Qubits

## 1 Introduction

Quantum programming languages, essential for large-scale deployment of quantum computing, have seen rapid development and widespread attention. Notable examples include IBM's Qiskit [49], Google's Cirq [14], Microsoft's Q# [58], Silq [5], Qunity [62], etc. Nevertheless, current quantum hardware is significantly perturbed by noise, which imposes limitations on the number and depth of quantum gates, as well as the number of logical qubits. These constraints are likely to persist in the near future, presenting challenges for achieving large-scale practical quantum supremacy. Therefore, it is crucial to introduce new features at the programming language design level to conserve and optimize the use of these scarce quantum resources.

In classical programming languages, memory management is a crucial mechanism for optimizing both spatial and temporal utilization. It is abstracted in the language as dynamic allocation and deallocation, allowing programmers to have finer control over memory resources. Similarly, most quantum programming languages support the dynamic allocation and deallocation of qubits. However, the unique properties of quantum states, such as superposition and entanglement, necessitate extra caution when managing dynamic memory. For instance, Silq [5] incorporates the first automatic support of uncomputation, ensuring that temporarily allocated clean qubits (initialized to the ground state) remain unentangled with the primary system after computation. This feature prevents unexpected errors that arise from the casual release of entangled auxiliary qubits.

Dirty qubit [27] is another important technique for reducing the costs of quantum circuits. Unlike clean qubits, allocated dirty qubits might be in arbitrary initial states instead of ground states, conserving the additional initialization. Dirty qubits are further required to be restored to the original state after computation. In terms of efficiency, although dirty qubits do not reduce the circuit size as effectively as clean ones, they grant great flexibility in qubit scheduling as illustrated in Section 2 and achieve a better balance between the circuit size and the number of auxiliary qubits within limited quantum resources. Moreover, in scenarios involving concurrent execution, dirty qubits can be borrowed and transferred between processes, as shown in Fig. 3.

Authors' Contact Information: Bonan Su, Department of Computer Science and Technology, Tsinghua University, Beijing, China, sbn24@mails.tsinghua.edu.cn; Li Zhou, , Key Laboratory of System Software (Chinese Academy of Sciences) and State Key Laboratory of Computer Science, Institute of Software, Chinese Academy of Sciences, Beijing, China, zhouli@ios.ac.cn; Yuan Feng, Department of Computer Science and Technology, Tsinghua University, Beijing, China, yuan\_feng@tsinghua.edu.cn; Mingsheng Ying, , Centre for Quantum Software and Information, University of Technology Sydney, Ultimo, Australia, Mingsheng.Ying@uts.edu.au.

Despite the support for the correct use of clean ancillary qubits in some languages such as Silq, programmers are still responsible for more general heap manipulations , including the runtime allocation and deallocation of qubits, especially dirty qubits, as seen in Q# [58]. Furthermore, dirty qubits inherently suffer from unique quantum-mechanical phenomena such as the no-cloning theorem and entanglement. These challenges make writing correct quantum programs with heap manipulations particularly difficult.

Concretely speaking, quantum states can exist in superpositions of multiple states, and distinct qubits can be entangled with each other. This contrasts sharply with classical memory cells, which have well-defined, independent states. Managing qubits in superposition and entangled states requires careful consideration of how an operation affects the state of qubits outside the domain of the operation. Additionally, dynamic management of quantum memory inevitably necessitates the process of addressing during the execution of quantum programs, which can cause memory faults even for experienced programmers.

Therefore, an effective formal method is needed to verify the correctness of quantum programs with heap manipulations. Meanwhile, separation logic [28, 52] has emerged as one of the most successful methods for reasoning about heap-manipulated programs. This naturally leads to the central question addressed in this paper:

Is there a feasible approach to interpret separation logic in the quantum setting, enabling the development of an effective proof system for reasoning about quantum programs involving heap manipulations, including the correct use of dirty qubits?

Technical Challenges. The primary technical challenges in obtaining a satisfactory answer through quantum separation logic fall into three main aspects:

- (1) Programming Language and Semantics . The dynamic allocation of dirty qubits requires the operational semantics to capture nondeterminism in both the addressing and initial states of newly allocated qubits. These qubits can be in arbitrary initial states and may even be entangled with the primary system or with the memory owned by other processes.
- (2) BI-style Assertion Logic . The quantum interpretation of Bunched Implication (BI) [45] which underpins separation logic, needs to address several critical issues: (i) Classical interpretation of logical connectives is inadequate for reasoning about quantum properties, partly because the superposition of quantum states makes disjunction ( ∨ ) unsuitable for backwards reasoning about quantum measurements; (ii) The separating conjunction ( ∗ ) and separating implication ( - ∗ ) need appropriate interpretations to describe the allocation and deallocation of qubits, enabling local reasoning and supporting backwards reasoning about heap manipulations.
- (3) Program Logic . A proof system needs to be established that is capable of describing and reasoning about the correct usage of dirty qubits and the manipulation of quantum heaps. However, domain-dependent semantics also raises completeness issues when reasoning about properties related to parts of an entangled system.

Contributions of the paper : We give an affirmative answer to the above question and technical challenges through a key design decision, i.e., the projection-based and domain-dependent semantics tailored for quantum-adapted BI logic [45]. We then leverage this framework to reason about quantum programs involving heap manipulations. Specifically, our contributions include:

- AQuantum BI-style Logic. Weextend Birkhoff-von Neumann quantum logic [6] with BI logical connectives ( ∗ ) and (- ∗) , where semantics for assertion formulas are domain-dependent and associated with projection operators. The separating conjunction ( ∗ ) is interpreted with a so-called separation-in-domain scheme: intuitively, a state 𝜌 with domain 𝑑 satisfies 𝜑 1 ∗ 𝜑 2 if there exists a partition 𝑑 1 and 𝑑 2 of 𝑑 such that the marginal 1 of 𝜌 on 𝑑 𝑖 satisfies 𝜑 𝑖 for 𝑖 = 1 , 2. This approach combines local semantics of formula clauses on separated domains to characterize entangled quantum heaps. It is important to note that satisfaction of a separable assertion 𝜌 ⊨ 𝜓 ∗ 𝜑 does not imply that the quantum heap can be separated into two isolated systems 2 . Despite this departure from classical BI logic, we establish a sound Hilbert-style proof system for our quantum BI-style logic, ensuring that inference rules for ( ∗ ) and ( - ∗ ) align with those proposed in classical BI logic.
- A Quantum Separation Logic. We adopt our BI-style logic as an assertion language to reason about quantum programs implemented in Qwhile-hp , a quantum programming language supporting heap manipulations. We formalize operational semantics and quantum heaps such that program statements including nondeterministic allocation of dirty qubits are executed within the scope of accessible resources. This contextual approach ensures that the runtime environment of Qwhile-hp does not need to encompass all qubits throughout execution. Furthermore, we present a sound and relatively complete proof system for our quantum separation logic. This system incorporates a frame rule for local reasoning and small axioms 3 tailored to reason about individual program statements. With the help of the separating implication ( - ∗ ), we then integrate backward inference rules for each program statement into the proof system.

As an application, we provide a formal definition for the correct usage of dirty qubits within a realistic model, which faithfully simulates executions of quantum programs in real world scenarios. To showcase the effectiveness of our quantum separation logic, we apply it to validate the correct usage of dirty qubits in various contexts. These include fundamental quantum circuits like an in-place addition circuit [27], multi-controlled X gates, a repeat-until-success circuit [47], and the quantum recursive Fourier sampling algorithm [41].

Related Works . Several attempts have been made to adapt separation logic to quantum programs. Zhou et al. [71] reinterpreted BI logic in the quantum setting to enable local reasoning about quantum programs. They instantiated the separating operator in BI frame as the tensor product 𝜌 1 ⊗ 𝜌 2 . However, the primary purpose of [71] is to perform local and modular reasoning, not to reason about heap manipulations. Le et al. [34] proposed a quantum separation logic where the separable conjunction is interpreted as the tensor factorization of pure states; that is, | 𝑢 ⟩ | = 𝜙 1 ∗ 𝜙 2 if | 𝑢 ⟩ = | 𝑢 1 ⟩ ⊗ | 𝑢 2 ⟩ such that | 𝑢 1 ⟩ | = 𝜙 1 and | 𝑢 2 ⟩ | = 𝜙 2 . They integrated classical variables and heap manipulations into their framework, but assumed that newly allocated qubits are set to the ground state. Both of these studies aimed at practical applications, emphasizing local reasoning, without providing a well-founded semantics for the separating implication ( - ∗ ) or ensuring the completeness of their proof systems.

In addition, other works explored the utility of quantum separation logic. Li et al. [38] presented a framework that translated quantum programs with classical pointers into a classical Hoare/separation logic framework implemented in the Dafny program verifier, strictly adhering to the interpretation of logical connectives from classical separation logic. Hietala et al. [24] developed Fig. 2. Costs associated with various implementations of addition | 𝑎 ⟩ ↦→ | 𝑎 + 𝑐 ⟩ of a value 𝑎 by a classical constant 𝑐 . (cf. Table 1 in [27])

1 The marginal of quantum states is mathematically characterized by partial density operator. Here, we say 'intuitively' because in the rigorous definition of ∗ , an existential quantification (of quantum states) over different partitions is used.

2 We say a quantum heap 𝜌 can be separated into two isolated systems if 𝜌 = 𝜌 1 ⊗ 𝜌 2 as discussed in [34, 71]

3 Small axioms are inference rules which only pertain to locally modified heaps [44]

<!-- image -->

Fig. 1. Circuit computing the last bit of 𝑟 = 𝑎 + ( 011 ) 2 .

|          | Draper [19]   | Cuccaro et al. [16]   | Takahashi et al. [59]   | Häner et al. [27]   |
|----------|---------------|-----------------------|-------------------------|---------------------|
| Size     | Θ ( 𝑛 2 )     | Θ ( 𝑛 )               | Θ ( 𝑛 )                 | Θ ( 𝑛 log 𝑛 )       |
| Depth    | Θ ( 𝑛 )       | Θ ( 𝑛 )               | Θ ( 𝑛 )                 | Θ ( 𝑛 )             |
| Ancillas | 0             | 𝑛 + 1(clean)          | 𝑛 (clean)               | 1(dirty)            |

Q ★ , an implementation of quantum separation logic [34] in the general purpose functional programming language F ★ . Singhal et al. [57] proposed an ideal computational model and a specification language, advocating for a comprehensive study of memory models before developing programming languages and verifiers, in accordance with the motivations underlying this paper.

## 2 A Motivating Example for Dirty Qubits

Before delving into formal definitions and technical details regarding the use of dirty qubits, let us first examine a simple example from [27] to understand the primitive motivations and capabilities of dirty qubits. The circuit in Fig. 1 presents an in-place addition circuit with only Pauli X, controlledNOT and Toffoli gates. A simple calculation shows that for arbitrary 𝑎 ∈ { 0 , 1 } 3 and 𝑔 ∈ { 0 , 1 } 2 , the circuit transforms | 𝑎 0 , 𝑔 0 , 𝑎 1 , 𝑔 1 , 𝑎 2 ⟩ to | 𝑎 0 , 𝑔 0 , 𝑎 1 , 𝑔 1 , 𝑎 2 + 𝑎 1 + 𝑎 0 + 𝑎 0 𝑎 1 ⟩ where the addition and multiplication are modulo 2 and 𝑟 2 ≜ 𝑎 2 + 𝑎 1 + 𝑎 0 + 𝑎 0 𝑎 1 is the last bit of 𝑟 = 𝑎 + ( 011 ) 2 . Thus, this circuit functions as a constant adder with ancilla qubits | 𝑔 0 , 𝑔 1 ⟩ in arbitrary initial states, which are referred to as dirty ancilla qubits .

It has become a consensus that ancilla qubits are helpful in reducing the size and depth of quantum circuits. Fig. 2 compares the costs of various implementations of the addition circuits. We observe that the depth and size (number of gates) of quantum circuits with ancilla qubits are smaller than those without ancillas, and circuits with initially clean ancilla qubits in ground states outperform those with dirty ancilla qubits.

However, since dirty qubits have no constraints on their initial states, they offer great potential in quantum programs by providing considerable flexibility in scheduling qubits. For example, consider a situation where two processes (with possible communication) are assigned to the same quantum computer and all available qubits have been allocated to them. What if Process 2 wants another qubit to optimize its local computation? If Process 2 requires the qubit to be in a clean state, then it has to wait until Process 1 finishes and releases some qubits. Otherwise, if Process 2 requires only a dirty one, then the scheduler could lock Process 1 and allow Process 2 to borrow a dirty qubit from it. After Process 2 finishes its computation involving the dirty qubit and restores it to its original state, Process 1 will resume its work. This process is illustrated in Fig. 3, where we no longer 'allocate' another qubit to Process 2; instead, we borrow a dirty qubit from Process 1. The ability to borrow dirty qubits from any idle part of a computation enhances our utilization of quantum resources and the efficiency of quantum programs.

Fig. 3. Borrowing a dirty qubit from another process

<!-- image -->

Despite the flexibility and efficiency improvements that dirty qubits offer to quantum resource scheduling, they also introduce challenges even for experts in designing quantum programs. A significant issue is that they impose stricter requirements on the uncomputation of dirty qubits compared to the clean ones. In addition to restoring dirty qubits to their original states, computations must ensure not to 'disrupt' the entanglement of dirty qubits.

Example 2.1. Consider the operation of applying a CNOT gate to qubits 𝑞, 𝑞 ′ where 𝑞 is the control qubit. If 𝑞 is a clean qubit initialized to | 0 ⟩ , such an operation does nothing, and 𝑞 remains unchanged. However, when 𝑞 is dirty, the CNOT gate can introduce additional entanglement. For example, 𝑞, 𝑞 ′ in the state |+ , 0 ⟩ will be transformed to 1 √ 2 (| 00 ⟩ + | 11 ⟩) , which is highly undesirable when dirty qubits are used.

The paper is organized as follows. We first introduce the concept of quantum heaps and discuss formal descriptions of dirty-qubit allocation in Section 3. Then, in Sections 4 and 6, we develop a BI-style assertion language and quantum separation logic to characterize the behaviors of heapmanipulated quantum programs. In Section 7, we construct a realistic model from scratch to depict practical scenarios and define the correct usage of dirty qubits. Finally, we illustrate how to prove the correct usage of dirty qubits using our program logic.

## 3 Quantum Heaps and Manipulations of Quantum Memory

This section aims to provide an intuitive illustration of quantum heaps and their manipulations. As an analogy to classical heap memory, quantum heaps serve as a program state recording state values of qubits in memory and can be expanded (allocation of qubits) or restricted (disposal of qubits) during runtime.

In contrast with quantum programming languages without memory management where the runtime context is fixed and includes all available qubits throughout executions, quantum heaps in this paper provide a local view of the runtime context in that they only have access to allocated qubits and retain no knowledge of others. Therefore, the domain of quantum heaps, which denotes the set of allocated qubits, plays a significant role in the manipulation of quantum heaps.

Recall that in the classical setting, a heap memory is often abstracted as a fi nite partial mapping :

$$& \text {Heap} \triangle q \bigcup _ { A \subseteq _ { f i n } \text {Addresses} } ( A \to \text {Values} ) \quad \text {in RelyongsTo} \left [ 5 \right ] \\ & o r \text { Heap} \triangle q \loc \to _ { f i n } \text {Val} \times \text {Val} \quad \quad \text {in Ishtiaq and O'Hearn} \left [ 28 \right ]$$

where Addresses and Loc represent the set of addresses/locations of memory cells, while Values and Val are for the content values. This abstraction contains two primary pieces of information: (1) A heap records the correspondence between addresses and values ; (2) A heap is a local resource that encompasses only a finite part of the entire memory space which is usually considered an infinitely long array. Following the same spirit, we give the definition of a quantum heap as a mixed quantum state (density operator) with a finite domain .

In quantum computation and quantum information, a pure state of an 𝑛 -qubit system is represented with a normalized column vector in 2 𝑛 -dimensional Hilbert space H , which is denoted by Dirac notation ket | 𝜓 ⟩ ∈ H such that ⟨ 𝜓 | 𝜓 ⟩ ≜ ⟨ 𝜓 | · | 𝜓 ⟩ = 1. Dirac notation bra ⟨ 𝜓 | ≜ | 𝜓 ⟩ † is a row vector where 𝐴 † stands for the conjugate transpose of matrix/vector 𝐴 . | 0 ⟩ ≜ 1 0 , | 1 ⟩ ≜ 0 1 , |+⟩ ≜ 1 √ 2 (| 0 ⟩ + | 1 ⟩) and |-⟩ ≜ 1 √ 2 (| 0 ⟩ - | 1 ⟩) are four commonly seen pure states of one qubit, where | 0 ⟩ is often referred to the ground state. Due to the probabilistic nature of quantum measurement and the indistinguishability between ensembles, a probabilistic distribution over pure states, called a mixed quantum state, is represented by a density operator . For example, suppose that the system is in state | 0 ⟩ or | 1 ⟩ with probability 1 2 respectively. Then the mixed state of it can be represented with the density operator 1 2 | 0 ⟩⟨ 0 | + 1 2 | 1 ⟩⟨ 1 | = 1 2 1 0 0 1 = 𝐼 2 where 𝐼 is the identity matrix.

Definition 3.1 (Quantum Heap). Let qName ≜ { 𝑞, 𝑞 0 , 𝑞 1 , ... } be a countably infinite set of qubit names, and let qDangle ≜ {⊔ 1 , ⊔ 2 , ⊔ 3 , ... } be the set of dangling names. Then a quantum heap is a density operator over a finite domain ⊆ qDomain ≜ qName ∪ qDangle :

$$\rho \in Q H e a p \triangle q \bigcup _ { d \subset f i n \ q \text {Domain} } \mathcal { D } ( \mathcal { H } _ { d } )$$

where H 𝑑 ≜ ¸ 𝑞 ∈ 𝑑 H 𝑞 is a 2 | 𝑑 | -dimensional Hilbert space ( H 𝑞 is the state space for qubit 𝑞 ) and D(H) is the set of density operators on H . We use 𝑑𝑜𝑚 𝜌 to denote the domain of 𝜌 , i.e. 𝜌 ∈ D(H 𝑑𝑜𝑚𝜌 ) .

Example 3.1 (Quantum Heap with Dangling Qubit). We use 𝜌 = | 0101 ⟩ 𝑞 1 , ⊔ 1 ,𝑞 3 ,𝑞 4 ⟨ 0101 | to represent a quantum heap with 𝑑𝑜𝑚 𝜌 = { 𝑞 1 , ⊔ 1 , 𝑞 3 , 𝑞 4 } that lies in a pure state | 0101 ⟩ . Roughly speaking, such a quantum heap can be viewed as a combination of stack and heap:

| Name   | ( 𝑠𝑡𝑎𝑐𝑘 )   | Logical Addresses   | ( ℎ𝑒𝑎𝑝 )   | Value                |
|--------|-------------|---------------------|------------|----------------------|
| 𝑞 1    | -→          | 1st qubit           | -→         | &#124; 0 ⟩⟨ 0 &#124; |
|        |             | 2nd qubit           | -→         | &#124; 1 ⟩⟨ 1 &#124; |
| 𝑞 3    | -→          | 3rd qubit           | -→         | &#124; 0 ⟩⟨ 0 &#124; |
| 𝑞 4    | -→          | 4th qubit           | -→         | &#124; 1 ⟩⟨ 1 &#124; |

where the second qubit is a dangling qubit that originates from a duplicated allocation. For example, qalloc ( 𝑞 ) ; qalloc ( 𝑞 ) will produce a dangling qubit where qalloc ( 𝑞 ) is a statement similar to 𝑞 : = malloc ( 𝑠𝑖𝑧𝑒 ) in classical programming languages like C/C++.

There are three primary manipulations of heap memory in classical setting: mutation , expansion and restriction . In the following, we will discuss how each of them works for quantum heaps.

## 3.1 Mutations of Quantum Heaps

In classical programs, the mutation statement [ 𝑎 ] : = 𝑣 consists of two parameters: the address 𝑎 and a new value 𝑣 . The execution of [ 𝑎 ] : = 𝑣 depends on the evaluation of 𝑎 and will cause an error if 𝑎 is outside the heap domain. Similarly, the mutation of quantum heaps is represented with the statement E[ 𝑞 ] consisting of two parts: the quantum operation E and the target qubits 𝑞 ⊆ 𝑓 𝑖𝑛 qName .

A quantum operation is often referred to a complete positive and trace non-increasing superoprator E : D(H) → D(H) between partial density operators. According to Kraus theorem, quantum operator E has the general form E( 𝐴 ) = ˝ 𝑘 𝐸 𝑘 𝐴𝐸 † 𝑘 such that ˝ 𝑘 𝐸 † 𝑘 𝐸 𝑘 ⊑ 𝐼 where ⊑ stands for the

Löwner order; that is, 𝐴 ⊑ 𝐵 △ ⇐⇒ 𝐵 -𝐴𝑖𝑠 𝑝𝑜𝑠𝑖𝑡𝑖𝑣𝑒 . We use Kronecker product to combine quantum operations E 1 ⊗ E 2 or matrices 𝐴 ⊗ 𝐵 to a larger domain. In addition to typical quantum operations such as unitary transformation ( E( 𝐴 ) = 𝑈𝐴𝑈 † where 𝑈𝑈 † = 𝑈 † 𝑈 = 𝐼 ) and initialization ( E( 𝐴 ) = ˝ 𝑛 | 0 ⟩⟨ 𝑛 | 𝐴 | 𝑛 ⟩⟨ 0 | ) introduced in Example 3.2, 3.3, quantum measurement with a specific result can also be viewed as a quantum operation. In this paper, we focus exclusively on projective quantum measurement, characterized by a set of projective operators 𝑀 𝑃 = { 𝑃 1 , 𝑃 2 , ..., 𝑃 𝑛 } such that ˝ 𝑖 𝑃 𝑖 = 𝐼 . A projective operator (or projection operator ) 𝑃 ∈ P(H) on the Hilbert space H has the general form 𝑃 = ˝ 𝜆 | 𝜆 ⟩⟨ 𝜆 | and corresponds to a closed subspace 𝐸 ( 𝑃 ) ≜ span {| 𝜆 ⟩} spanned by eigenvectors of 𝑃 . With an abuse of notation, we no longer distinguish an operator 𝑃 and its corresponding subspace 𝐸 ( 𝑃 ) . When measuring 𝜌 ∈ D(H) with 𝑀 𝑃 , we get the measurement result 𝑖 and the state of the system collapses into 𝑃 𝑖 𝜌𝑃 𝑖 𝑡𝑟 ( 𝑃 𝑖 𝜌 ) with probability 𝑡𝑟 ( 𝑃 𝑖 𝜌 ) , according to the measurement hypothesis in quantum mechanics. Ignoring the coefficient, E( 𝜌 ) = 𝑃𝜌𝑃 is also referred to as a projective operation. For example, if we measure |+⟩⟨+| with 𝑀 𝑃 = { 𝑃 0 = | 0 ⟩⟨ 0 | , 𝑃 1 = | 1 ⟩⟨ 1 |} , then with probability 1 2 we get the measurement result 0 and the state of the system collapse into | 0 ⟩⟨ 0 | .

For mutations of quantum heaps, execution of E[ 𝑞 ] applies the quantum operation E to 𝑞 , formally:

$$\rho \xrightarrow { \mathcal { E } [ \bar { q } ] } ( I _ { d o m \, \rho \, \bar { q } } \otimes \mathcal { E } _ { \bar { q } } ) ( \rho ) \ \text { provided } \ \bar { q } \subseteq d o m \, \rho$$

where I stands for identity quantum operation, indicating that E[ 𝑞 ] does nothing to qubits other than 𝑞 . The mutation will also fail and raise an error if 𝑞 \ 𝑑𝑜𝑚 𝜌 ≠ ∅ ; i.e. some target qubits are outside the heap domain.

Example 3.2 (Unitary Transformation). Continuing from Example 3.1, consider a unitary quantum operation E( 𝐴 ) ≜ 𝑋 · 𝐴 · 𝑋 † where 𝑋 is Pauli-X matrix and target qubits 𝑞 ≜ { 𝑞 3 } , then

$$| 0 1 0 1 \rangle _ { q _ { 1 } , \cup _ { 1 } , q _ { 3 } , q _ { 4 } } \langle 0 1 0 1 | \stackrel { \mathcal { E } [ q _ { 3 } ] } { \longrightarrow } ( I _ { q _ { 1 } , \cup _ { 1 } , q _ { 4 } } \otimes X _ { q _ { 3 } } ) | 0 1 0 1 \rangle \langle 0 1 0 1 | ( I _ { q _ { 1 } , \cup _ { 1 } , q _ { 4 } } \otimes X _ { q _ { 3 } } ) ^ { \dagger } = | 0 1 1 1 \rangle _ { q _ { 1 } , \cup _ { 1 } , q _ { 3 } , q _ { 4 } } \langle 0 1 1 1 |$$

Example 3.3 (Initialization). Given a quantum heap 𝜌 = 1 2 | 0 ⟩ 𝑞 ⟨ 0 | + 1 2 | 1 ⟩ 𝑞 ⟨ 1 | , the initialization E( 𝐴 ) ≜ ˝ 𝑖 ∈{ 0 , 1 } | 0 ⟩⟨ 𝑖 | 𝐴 | 𝑖 ⟩⟨ 0 | on qubit 𝑞 has the effect:

$$\frac { 1 } { 2 } | 0 \rangle _ { q } \langle 0 | + \frac { 1 } { 2 } | 1 \rangle _ { q } \langle 1 | \xrightarrow { \mathcal { E } [ q ] } | 0 \rangle _ { q } \langle 0 |$$

## 3.2 Expansions and Restrictions of Quantum Heaps

As introduced at the beginning of this section, quantum heaps allow the runtime allocation and disposal of qubits, achieved through the expansion and restriction of quantum heaps.

Nondeterminism in allocation of dirty qubits. Two nondeterministic choices are made during the allocation of qubits: (1) Address assigned to the newly allocated qubit; (2) Initial state of the newly allocated qubit. For (1), we assume a verified mechanism that manages a one-to-one correspondence between logical addresses (1st qubit, 2nd qubit, . . . as shown in Example 3.1) and physical addresses . Thus, allocating a new qubit can always be regarded as appending it to the tail of the density operator. For (2), we define small-step operational semantics in a nondeterministic manner to formally describe the process of allocating dirty qubits.

Let us first consider the disposal of qubits, where we define the restriction of a quantum heap using the partial trace 𝑡𝑟 𝑞 ( 𝜌 ) ≜ ˝ 𝑖 ∈{ 0 , 1 } ( 𝐼 ⊗ ⟨ 𝑖 | 𝑞 ) 𝜌 ( 𝐼 ⊗ | 𝑖 ⟩ 𝑞 ) , a common method in quantum information to describe the restricted view on the state of a subsystem:

$$\rho \xrightarrow { \ q f r e ( q ) } \rho | _ { d o m \, \rho \, \rangle q } \stackrel { \mathfrak { s } } { = } t r _ { q } ( \rho ) \ \text { provided } \ q \in d o m \, \rho$$

where 𝜌 | 𝐴 ≜ 𝑡𝑟 𝑑𝑜𝑚𝜌 \ 𝐴 ( 𝜌 ) is the restriction of 𝜌 to domain 𝐴 , and 𝜌 is an expansion of 𝜌 | 𝐴 .

For allocation, unlike previous work [34, 63], which requires newly allocated qubits to be set to the ground state deterministically, we allow the allocation of dirty qubits. The only constraint we impose on allocation is: the new heap after tracing out the allocated qubits coincides with the old one :

$$\rho \xrightarrow { \ q a l l o c ( q ) } \rho ^ { \prime } \quad \text {provided} \quad \rho ^ { \prime } \in \mathcal { D } ( \mathcal { H } _ { d o m \, \rho [ q \Rightarrow ] } \otimes \mathcal { H } _ { q } ) \ \text {and} \ \rho ^ { \prime } | _ { d o m \, \rho [ q \Rightarrow ] } = \rho [ q \Rightarrow \sqcup ]$$

where 𝑑𝑜𝑚 𝜌 [ 𝑞 ⇒⊔] denotes the domain substituting 𝑞 in 𝑑𝑜𝑚 𝜌 by a dangling name ⊔ ∉ 𝑑𝑜𝑚 𝜌 , and 𝜌 [ 𝑞 ⇒⊔] denotes the density operator renaming 𝑞 to 𝑞 ′ in subscripts of 𝜌 . Such a renaming process ensures that qubit allocation will never fail, and if the qubit 𝑞 has already been allocated, attempting to allocate it again will result in a dangling qubit.

Note that a similar mechanism has already been provided by Q# through the borrow statement [8]. Obviously, we can also implement the allocation of a clean qubit 𝑞 in [34, 55] by applying the initialization operation E[ 𝜌 ] ≜ ˝ 𝑖 = 0 , 1 | 0 ⟩⟨ 𝑖 | 𝜌 | 𝑖 ⟩⟨ 0 | after qalloc ( 𝑞 ) :

$$\rho \xrightarrow { \ q a l l o c ( q ) } \rho ^ { \prime } \xrightarrow { \mathcal { E } [ q ] } \rho [ q \Rightarrow \sqcup ] \otimes | 0 \rangle _ { q } \langle 0 |$$

Example 3.4 (Duplicated Allocation and Dangling Qubit). Let quantum heap 𝜌 ≜ | 0 ⟩ 𝑞 ⟨ 0 | , then a possible execution of repeatedly allocating qubit 𝑞 is

$$| 0 \rangle _ { q } \langle 0 | \xrightarrow { \ q a l l o c ( q ) } | 0 \rangle _ { \sqcup } \langle 0 | \otimes | 1 \rangle _ { q } \langle 1 | \xrightarrow { \ q a l l o c ( q ) } | 0 \rangle _ { \sqcup } \langle 0 | \otimes | 1 \rangle _ { \sqcup _ { 1 } } \langle 1 | \otimes | + \rangle _ { q } \langle + |$$

where the 1st and 2nd qubits are no longer accessible and become dangling qubits.

Example 3.5 (Diversity in Allocation of Dirty Qubits). Let 𝜌 ≜ 1 2 (| 0 ⟩ 𝑞 ⟨ 0 | + | 1 ⟩ 𝑞 ⟨ 1 |) . The following heaps are all possible outputs after allocating a dirty qubit 𝑞 ′ :

$$\begin{array} { r l } { J } & { 0 } & { 1 } \\ { ( 1 ) } & { \rho ^ { \prime } } & { \triangle q \frac { 1 } { 2 } ( | 0 \rangle _ { q } \langle 0 | + | 1 \rangle _ { q } \langle 1 | ) \otimes | 0 \rangle _ { q ^ { \prime } } \langle 0 | } \\ { ( 2 ) } & { \rho ^ { \prime } } & { \triangle q \frac { 1 } { 2 } ( | 0 0 \rangle + | 1 1 \rangle ) _ { q , q ^ { \prime } } ( \langle 0 0 | + \langle 1 1 | ) } \\ { ( 0 ) } & { \theta } & { 1 } \end{array}$$

$$( 3 ) \ \rho ^ { \prime } \stackrel { \underline { \frac { 1 } { 1 } } } { = } \frac { \frac { 1 } { 2 } ( | 0 \rangle _ { q } \langle 0 | + | 1 \rangle _ { q } \langle 1 | ) \otimes \frac { 1 } { 2 } ( | 0 \rangle _ { q ^ { \prime } } \langle 0 | + | 1 \rangle _ { q ^ { \prime } } \langle 1 | ) } { 2 }$$

Here, (1) aligns with previous works where the allocation is performed to append 𝑞 ′ in the ground state. We further allow (2), where the new qubit 𝑞 ′ is entangled with 𝑞 , and (3), where 𝑞 ′ is separable from 𝑞 but in a mixed state. Interestingly, 𝑞 ′ in (3) can actually be entangled with a third qubit not described in the current quantum heap.

Wehave already seen that the expansion for quantum heaps differs significantly from the classical case due to the existence of entanglement . A particularly counterintuitive phenomenon is that operations applied to newly allocated qubits may also affect previously allocated qubits if they are entangled. This poses serious challenges for reasoning about heap manipulations in quantum programs.

## 4 A BI-style assertion language

To reason about the correctness of quantum programs with heap manipulations and the correct usage of dirty qubits, we need an assertion language to formally characterize quantum heaps.

BI (Bunched Implication) logic [28, 45] is widely adopted as an effective logic system to describe the nature of classical heaps. In this section, we will reformulate BI logic in a quantum setting to develop well-founded semantics and a sound proof system both of which capture the essential properties of quantum heaps. In addition, our proof system aligns well with classical BI logic, making it easy to reuse and extend existing tools for classical BI logic.

Fig. 4 compares the assertion formulas of classical BI logic and the quantum BI-style logic that we propose. The core of classical BI logic is two new connectives: separating conjunction ( ∗ ) which characterizes local properties of classical heaps via spatial separation, and separating implication ( - ∗ ) which is critical to backward reasoning. We introduce these two logical connectives to Birkhoff-von Neumann logic to obtain the same expressiveness for quantum heaps.

## 4.1 Why Birkhoff-von Neumann Quantum Logic and Projection-based Semantics?

Birkhoff and von Neumann [6] proposed a logic system containing logical connectives in classical fashion to characterize quantum events with fixed Hilbert space H , where semantics of atomic propositions and assertion formulas is associated with projection operators:

Fig. 4. Comparison between classical BI logic and quantum BI-style logic

<!-- image -->

$$[ P \in \text {Atomic} \stackrel { \triangle } { = } \mathcal { P } ( \mathcal { H } ) ] & \triangle P \quad [ \neg \psi ] \triangle \left [ [ \psi ] ^ { \perp } \quad [ \psi \wedge \varphi ] \triangle \left [ [ \psi ] \cap [ \varphi ] \quad [ \psi \vee \varphi ] \triangle \left ( [ \psi ] \cup [ \varphi ] \right ) \\ \\ \intertext { [P \in \text {Atomic} } \intertext { [P \in \text {Atomic} } \intertext { [P \in \mathcal { H } \circ \mathcal { I } ] \cup \mathcal { I } \circ \mathcal { H } \circ \mathcal { I } | \psi \rangle \triangle \left ( 0 \text { denotes the automorphism} \triangle \intertext { [P \in \text {Atomic} } \intertext { [P \in \mathcal { H } \circ \mathcal { I } ] \cup \mathcal { I } \circ \mathcal { H } \circ \mathcal { I } | \psi \rangle \triangle \left ( 0 \text { denotes the automorphism} \triangle \intertext { [P \in \text {Atomic} } \intertext { [P \in \mathcal { H } \circ \mathcal { I } ] \cup \mathcal { I } \circ \mathcal { H } \circ \mathcal { I } | \psi \rangle \triangle \left ( 0 \text { denotes the automorphism} \triangle \intertext { [P \in \text {Atomic} } \intertext { [P \in \mathcal { H } \circ \mathcal { I } ] \cup \mathcal { I } \circ \mathcal { H } \circ \mathcal { I } | \psi \rangle \triangle \left ( 0 \text { denotes the automorphism} \triangle \intertext { [P \in \text {Atomic} } \intertext { [P \in \mathcal { H } \circ \mathcal { I } ] \cup \mathcal { I } \circ \mathcal { H } \circ \mathcal { I } | \psi \rangle \triangle \left ( 0 \text { denotes the automorphism} \triangle \intertext { [P \in \text {Atomic} } \intertext { [P \in \mathcal { H } \circ \mathcal { I } ] \cup \mathcal { I } \circ \mathcal { H } \circ \mathcal { I } | \psi \rangle \triangle \left ( 0 \text { denotes the automorphism} \triangle \intertext { [P \in \text {Atomic} } \intertext { [P \in \mathcal { H } \circ \mathcal { I } ] \cup \mathcal { I } \circ \mathcal { H } \circ \mathcal { I } | \psi \rangle \triangle \left ( 0 \text { denotes the automorphism} \triangle \intertext { [P \in \text {Atomic} } \intertext { [P \in \mathcal { H } \circ \mathcal { I } ] \cup \mathcal { I } \circ \mathcal { H } \circ \mathcal { I } | \psi \rangle \triangle \left ( 0 \text { denotes the automorphism} \triangle \intertext { [P \in \text {Atomic} } \intertext { [P \in \mathcal { H } \circ \mathcal { I } ] \cup \mathcal { I } \circ \mathcal { H } \circ \mathcal { I } | \psi \rangle \triangle \left ( 0 \text { denotes the automorphism} \triangle \intertext { [P \in \text {Atomic} } \intertext { [P \in \mathcal { H } \circ \mathcal { I } ] \cup \mathcal { I } \circ \mathcal { H } \circ \mathcal { I } | \psi \rangle \triangle \left ( 0 \text { denotes the automorphism} \triangle \intertext { [P \in \text {Atomic} } \intertext { [P \in \mathcal { H } \circ \mathcal { I } ] \cup \mathcal { I } \circ \mathcal { H } \circ \mathcal { I } | \psi \rangle \triangle \left ( 0 \text { denotes the automorphism} \triangle \intertext { [P \in \text {Atomic} } \intertext { [P \in \mathcal { H } \circ \mathcal { I } ] \cup \mathcal { I } \circ \mathcal { H } \circ \mathcal { I } | \psi \rangle \triangle \left ( 0 \text { denotes the automorphism} \triangle \intertext { [P \in \text {Atomic} } \intertext { [P \in \mathcal { H } \circ \mathcal { I } ] \cup \mathcal { I } \circ \mathcal { H } \circ \mathcal { I } | \psi \rangle \triangle \left ( 0 \text { denotes the automorphism} \triangle \intertext { [P \in \text {Atomic} } \intertext { [P \in \mathcal { H } \circ \mathcal { I } ] \cup \mathcal { I } \circ \mathcal { H } \circ \mathcal { I } | \psi \rangle \triangle \left ( 0 \text { denotes the automorphism} \triangle \intertext { [P \in \text {Atomic} } \intertext { [P \in \mathcal { H } \circ \mathcal { I } ] \cup \mathcal { I } \circ \mathcal { H } \circ \mathcal { I } | \psi \rangle \triangle \left ( 0 \text { denotes the automorphism} \triangle \intertext { [P \in \text {Atomic} } \intertext { [P \in \mathcal { H } \circ \mathcal { I } ] \cup \mathcal { I } \circ \mathcal { H } \circ \mathcal { I } | \psi \rangle \triangle \left ( 0 \text { denotes the automorphism} \triangle \intertext { [P \in \text {Atomic} } \intertext { [P \in \mathcal { H } \circ \mathcal { I } ] \cup \mathcal { I } \circ \mathcal { H } \circ \mathcal { I } | \psi \rangle \triangle \left ( 0 \text { denotes the automorphism} \triangle \intertext { [P \in \text {Atomic} } \intertext { [P \in \mathcal { H } \circ \mathcal { I } ] \cup \mathcal { I } \circ \mathcal { H } \circ \mathcal { I } | \psi \rangle \triangle \left ( 0 \text { denotes the automorphism} \triangle \intertext { [P \in \text {Atomic} } \intertext { [P \in \mathcal { H } \circ \mathcal { I } ] \cup \mathcal { I } \circ \mathcal { H } \circ \mathcal { I } | \psi \rangle \triangle \left ( 0 \text { denotes the automorphism} \triangle \intertext { [P \in \text {Atomic} } \intertext { [P \in \mathcal { H } \circ \mathcal { I } ] \cup \mathcal { I } \circ \mathcal { H } \circ \mathcal { I } | \psi \rangle \triangle \left ( 0 \text { denotes the automorphism} \triangle \intertext { [P \in \text {Atomic} } \intertext { [P \in \mathcal { H } \circ \mathcal { I } ] \cup \mathcal { I } \circ \mathcal { H } \circ \mathcal { I } | \psi \rangle \triangle \left ( 0 \text { denotes the automorphism} \triangle \intertext { [P \in \text {Atomic} } \intertext { [P \in \mathcal { H } \circ \mathcal { I } ] \cup \mathcal { I } \circ \mathcal { H } \circ \mathcal { I } | \psi \rangle \triangle \left ( 0 \text { denotes the automorphism} \triangle \intertext { [P \in \text {Atomic} } \intertext { [P \in \mathcal { H } \circ \mathcal { I } ] \cup \mathcal { I } \circ \mathcal { H } \circ \mathcal { I } | \psi \rangle \triangle \left ( 0 \$$

where 𝑃 ⊥ ≜ {| 𝜓 ⟩ ∈ H : 𝑃 | 𝜓 ⟩ = 0 } denotes the orthogonal complement subspace of 𝑃 , 𝑃 ∩ 𝑄 denotes the intersection space of 𝑃, 𝑄 and 𝑠𝑝𝑎𝑛 ( 𝑃 ∪ 𝑄 ) stands for the linearly spanned union space 𝑃 ∪ 𝑄 . Birkhoff-von Neumann logic has already been adopted in [61, 67, 72] as an assertion language to reason about quantum programs with a fixed runtime context. In this paper, we follow the same spirit and extend it by assigning projection-based but domain-dependent semantics to logical connectives, including BI connectives, to describe runtime-variable quantum heaps. We will briefly justify the use of projection-based semantics and outline its advantages, then introduce in detail about domain-dependent and projection-based semantics for quantum BI-style logic in next section.

Several quantum assertion languages have been explored in the literature. One of them takes observables as assertions [17, 66] and interprets logical connectives in effect algebra [21, 29, 32]. However, there is a lack of algebraic structure that is universally adaptive for structural reasoning. For instance, the semantics of disjunction " 𝐴 ∨ 𝐵 " for observables 𝐴, 𝐵 is problematic and only well-defined for observables with additional requirements.

Another approach interprets logical connectives in a classical way [34, 71]. Here, 𝜌 ⊨ 𝜓 ∨ 𝜑 is defined as 𝜌 ⊨ 𝜓 or 𝜌 ⊨ 𝜑 , rather than considering the spanned space ⌈ 𝜌 ⌉ ⊆ 𝑠𝑝𝑎𝑛 ( J 𝜓 K ∪ J 𝜑 K ) where ⌈ 𝜌 ⌉ ≜ ( 𝜌 ⊥ ) ⊥ = space spanned by eigenvectors of 𝜌 is the support space of 𝜌 . However, this classical approach faces technical challenges when reasoning about probabilistic branches. To address these issues, an additional requirement known as closed under mixtures 4 has been introduced for valid assertions. For example, consider the quantum program 'measure the qubit, then flip it if the measurement result is 1' defined formally as 𝑆 ≜ if 𝑀 𝑝 [ 𝑞 ] then 𝑋 [ 𝑞 ] else skip . An easy observation is that, regardless of the initial state, this operation changes the qubit's state to | 0 ⟩⟨ 0 | . This transformation is captured by the Hoare-style specification 𝐼 𝑞 𝑆 | 0 ⟩ 𝑞 ⟨ 0 | . However, with commonly used inference rules for if-branches, we can only derive | 0 ⟩ 𝑞 ⟨ 0 | ∨ | 1 ⟩ 𝑞 ⟨ 1 | 𝑆 | 0 ⟩ 𝑞 ⟨ 0 | , which is notably incomplete.

## 4.2 Domain-dependent and Projection-based Semantics

As discussed in Section 3, quantum heaps can be dynamically expanded or restricted during runtime. This variability necessitates the development of domain-dependent semantics for each assertion. Specifically, for each assertion formula 𝜓 generated by the grammar defined in Fig. 4b where 𝑞 ⊆ 𝑓 𝑖𝑛 qName , its semantics is a function such that given a domain 𝑑 ⊆ 𝑓 𝑖𝑛 qDomain , J 𝜓 K ( 𝑑 ) ∈ P(H 𝑑 ) is a projection operator on H 𝑑 ; that is, 𝜓 : ˛ 𝑑 ⊆ 𝑓 𝑖𝑛 qDomain P(H 𝑑 ) is of dependent function type.

J K The intuition behind domain-dependent semantics stems from the dynamic expansions and restrictions of quantum heaps, which necessitates different interpretations of assertion formula

4 cf. Definition 4.6 in [2] and Definition 4.2 in [71]

Fig. 5. Comparison of classical and quantum heaps

<!-- image -->

$$\longrightarrow \\ [ \mathbb { T } ] \left ( d \right ) \triangle q _ { d } \left [ \mathbb { I } \right ] \left ( d \right ) \triangle q _ { d } \left [ \bar { q } \mapsto P \right ] \left ( d \right ) \triangle q _ { 0 } ^ { \int P _ { d } \ \ d = \bar { q } } \left [ \mathbb { T } ^ { * } \right ] \left ( d \right ) = \left \{ 1 _ { d } \ \ d = 0 \\ 0 _ { d } \ \ o . w . \quad \left [ \mathbb { T } ^ { * } \right ] \left ( d \right ) = \left \{ 0 _ { d } \ \ o . w . \quad \\ [ \psi _ { 1 } \ \uparrow \psi _ { 2 } ] \left ( d \right ) \triangle q _ { \left [ \psi _ { 1 } \right ] } \left ( d \right ) \triangle q _ { \left [ \psi _ { 2 } \right ] } \left ( d \right ) \left [ \psi _ { 1 } \lor \psi _ { 2 } \right ] \left ( d \right ) \triangle q \left ( \left [ \psi _ { 1 } \right ] \left ( d \right ) \right ) ^ { \perp } \\ [ \psi _ { 1 } \ \sim \psi _ { 2 } ] \left ( d \right ) \triangle q _ { \left [ \psi _ { 1 } \right ] } \left ( d \right ) \triangle q \left [ \psi _ { 2 } \right ] \left ( d \right ) = \left ( \left [ \psi _ { 1 } \right ] \left ( d \right ) \right ) ^ { \perp } \vee \left ( \left [ \psi _ { 1 } \right ] \left ( d \right ) \triangle q _ { \left [ \psi _ { 2 } \right ] } \left ( d \right ) \\ [ \psi _ { 1 } \ * \psi _ { 2 } ] \left ( d \right ) \triangle q _ { \left [ \psi _ { 1 } \right ] } \left ( d ^ { \prime } \right ) \otimes \left [ \psi _ { 2 } \right ] \left ( d \right ) ^ { \perp } \triangle q _ { \left [ \psi _ { 1 } \right ] } \left ( d ^ { \prime } \right ) \left ( \left [ \psi _ { 2 } \right ] \left ( d ^ { \prime } \right ) d \right ) \\ \intertext { [ \psi _ { 1 } \ * \psi _ { 2 } ] \left ( d \right ) \triangle q _ { \left [ \psi _ { 1 } \right ] } \left ( d ^ { \prime } \right ) \otimes \left [ \psi _ { 2 } \right ] \left ( d \right ) ^ { \perp } \triangle q _ { \left [ \psi _ { 1 } \right ] } \left ( d ^ { \prime } \right ) \left ( \left [ \psi _ { 2 } \right ] \left ( d ^ { \prime } \right ) d \right ) } \\ \intertext { \quad \intertext { [ \psi _ { 1 } \ * \psi _ { 2 } ] \left ( d \right ) \triangle q _ { \left [ \psi _ { 1 } \right ] } \left ( d ^ { \prime } \right ) \otimes \left [ \psi _ { 2 } \right ] \left ( d \right ) ^ { \perp } \triangle q _ { \left [ \psi _ { 1 } \right ] } \left ( d ^ { \prime } \right ) \left ( \left [ \psi _ { 2 } \right ] \left ( d ^ { \prime } \right ) d \right ) } \\ \intertext { [ \psi _ { 1 } \ * \psi _ { 2 } ] \left ( d \right ) \triangle q _ { \left [ \psi _ { 1 } \right ] } \left ( d ^ { \prime } \right ) \otimes \left [ \psi _ { 2 } \right ] \left ( d ^ { \prime } \right ) \triangle q _ { \left [ \psi _ { 1 } \right ] } \left ( d ^ { \prime } \right ) \left ( \left [ \psi _ { 2 } \right ] \left ( d ^ { \prime } \right ) d \right ) } \\ \intertext { \quad \intertext { [ \psi _ { 1 } \ * \psi _ { 2 } ] \left ( d \right ) \triangle q _ { \left [ \psi _ { 1 } \right ] } \left ( d ^ { \prime } \right ) \otimes \left ( \left [ \psi _ { 2 } \right ] \left ( d ^ { \prime } \right ) d \right ) } \\ \intertext { [ \psi _ { 1 } \ * \psi _ { 2 } ] \left ( d \right ) \triangle q _ { \left [ \psi _ { 1 } \right ] } \left ( d ^ { \prime } \right ) \otimes \left ( \left [ \psi _ { 2 } \right ] \left ( d ^ { \prime } \right ) d \right ) } \\ \intertext { [ \psi _ { 1 } \ * \psi _ { 2 } ] \left ( d \right ) \triangle q _ { \left [ \psi _ { 1 } \right ] } \left ( d ^ { \prime } \right ) \otimes \left ( \left [ \psi _ { 2 } \right ] \left ( d ^ { \prime } \right ) d \right ) } \\ \intertext { [ \psi _ { 1 } \ * \psi _ { 2 } ] \left ( d \right ) \triangle q _ { \left [ \psi _ { 1 } \right ] } \left ( d ^ { \prime } \right ) \otimes \left ( \left [ \psi _ { 2 } \right ] \left ( d ^ { \prime } \right ) d \right ) } \\ \intertext { [ \psi _ { 1 } \ * \psi _ { 2 } ] \left ( d \right ) \triangle q _ { \left [ \psi _ { 1 } \right ] } \left ( d ^ { \prime } \right ) \otimes \left ( \left [ \psi _ { 2 } \right ] \left ( d ^ { \prime } \right ) d \right ) } \\ \intertext { [ \psi _ { 1 } \ * \psi _ { 2 } ] \left ( d \right ) \triangle q _ { \left [ \psi _ { 1 } \right ] } \left ( d ^ { \prime } \right ) \otimes \left ( \left [ \psi _ { 2 } \right ] \left ( d ^ { \prime } \right ) d \right ) } \\ \intertext { [ \psi _ { 1 } \ * \psi _ { 2 } ] \left ( d \right ) \triangle q _ { \left [ \psi _ { 1 } \right ] } \left ( d ^ { \prime } \right ) \otimes \left ( \left [ \psi _ { 2 } \right ] \left ( d ^ { \prime } \right ) d \right ) } \\ \intertext { [ \psi _ { 1 } \ * \psi _ { 2 } ] \left ( d \right ) \triangle q _ { \left [ \psi _ { 1 } \right ] } \left ( d ^ { \prime } \right ) \otimes \left ( \left [ \psi _ { 2 } \right ] \left ( d ^ { \prime } \right ) d \right ) } \\ \intertext { [ \psi _ { 1 } \ * \psi _ { 2 } ] \left ( d \right ) \triangle q _ { \left [ \psi _ { 1 } \right ] } \left ( d ^ { \prime } \right ) \otimes \left ( \left [ \psi _ { 2 } \right ] \left ( d ^ { \prime } \right ) d \right ) } \\ \intertext { [ \psi _ { 1 } \ * \psi _ { 2 } ] \left ( d \right ) \triangle q _ { \left [ \$$

Fig. 6. Semantics of assertion formulas in quantum BI-style logic

across different domains. In other words, J 𝜓 K ( 𝑑 ) denotes the semantics of assertion 𝜓 within a specific domain 𝑑 , where resources such as qubits are constrained.

The most tricky challenge to construct BI-style assertion language for quantum heaps is that unlike classical heaps, not all quantum heaps can be separated into two isolated systems due to entanglement. Consequently, we can hardly interpret separating conjunction in a classical way (shown in Fig. 5a), because it fails to characterize entangled resources, as demonstrated by existing work [34, 71].

As a solution, we choose to interpret the separating conjunction ( ∗ ) in our assertion language with a so-called separation in domain scheme as shown in Fig. 5b. To put it short and simple, Fig. 5a demonstrates the slogan for semantics of separating conjunction ( ∗ ) in the classical setting: ' separable resources, separable assertion ', while for quantum heaps, Fig. 5b suggests that ' separable assertions are combined to describe entangled resources '. This idea is formalized by the domaindependent semantics of assertions defined in Fig. 6, where tensor implication ( -⊗ ) serves as an adjoint connective of tensor product ( ⊗ ) with respect to projection operators:

Lemma 4.1 (Tensor Implication). Let 𝑃 and 𝑄 be two projections with 𝑑𝑜𝑚𝑃 ⊆ 𝑑𝑜𝑚𝑄 . Define

$$P \neg \otimes Q \stackrel { \circ } { = } \max \{ R \in \mathcal { P } ( \mathcal { H } _ { d o m \, Q \, \rangle \, d o m \, P } ) \, \colon P \otimes R \subseteq Q \} .$$

Then 𝑃 -⊗ 𝑄 = 𝐼 if 𝑃 = 0 and 𝐸 𝑡𝑟 𝑑𝑜𝑚𝑃 𝑃 dim 𝑃 · 𝑄 otherwise, where dim 𝑃 is the dimension of 𝑃 . Furthermore, for all 𝑅 , 𝑃 ⊗ 𝑅 ⊆ 𝑄 iff 𝑅 ⊆ 𝑃 -⊗ 𝑄 , which justifies the duality between ⊗ and -⊗ .

The satisfaction relation ⊨ ⊆ QHeap × Assr (where Assr stands for the set of all assertion formulas) is naturally defined as following, which suggests that the support space of the quantum heap 𝜌 is contained in assertion 𝜓 (whose semantics is associated with a projection operator):

$$\rho \models \psi \iff \lceil \rho \rceil \subseteq [ \psi ] \left ( d o m \, \rho \right ) \\ \text {ations on intuitions behind the semantics}$$

We will give detailed explanations on intuitions behind the semantics of each formula.

Atomic predicates ( ⊤ , ⊥ , ⊤ ∗ , 𝑞 ↦→ 𝑃 ). It's obvious that ⊤ and ⊥ are tautology ( true ) and contradiction ( false ) respectively, which means ∀ 𝜌 ∈ QHeap . 𝜌 ⊨ ⊤ and 𝜌 ⊭ ⊥ since 𝐼 stands for the entire space while 0 is the null space. Atomic predicate 𝑞 ↦→ 𝑃 serves an analogy to ' 𝑥 ↦→ 𝑣 ' in [52] or ' 𝐸 ↦→ 𝐸 1 , 𝐸 2 ' in [28] which describes a heap with an exact domain 𝑞 :

$$\rho \models \bar { q } \mapsto P \iff d o m \, \rho = \bar { q } \text { and } \lceil \rho \rceil \subseteq P$$

For ⊤ ∗ , it asserts that the quantum heap is empty i.e. 𝜌 ⊨ ⊤ ∗ ⇐⇒ 𝑑𝑜𝑚 𝜌 = ∅ , and later we will show that it functions as the unit element with respect to separating conjunction ( ∗ ).

Logical connectives ( ∨ , ∧ , ¬ , ⇝ ). The first three logical connectives are inherited pointwisely from Birkhoff-von Neumann logic, and 𝑃 ⇝ 𝑄 ≜ 𝑃 ⊥ ∨ ( 𝑃 ∧ 𝑄 ) is often referred to as Sasaki hook [42, 54], all of which guarantee that fix a domain 𝑑 ⊆ 𝑓 𝑖𝑛 qDomain , 𝜓 ( 𝑑 ) is a projective operator.

J K Sasaki hook is widely regarded as a weak analogy to implication in orthologic as it satisfies 𝑃 ⊆ 𝑄 ⇐⇒ 𝑃 ⇝ 𝑄 = 𝐼 and a weak version of import-export condition:

$$P \subseteq Q \hookrightarrow R \Rightarrow P \wedge Q \subseteq R \quad P \wedge Q \subseteq R \text { and } P , Q \text { are compatible } \Rightarrow P \subseteq Q \hookrightarrow R$$

where 𝑃 and 𝑄 are compatible requires 𝑃 = ( 𝑃 ∧ 𝑄 ) ∨ ( 𝑃 ∧ 𝑄 ⊥ ) . Although the Sasaki hook violates some positive laws e.g. 𝑃 ⇝ ( 𝑄 ⇝ 𝑃 ) ≠ 𝐼 , it still has great potential to reason about the weakest liberal conditions of probabilistic branches in quantum programs [20].

Separating conjunction ( ∗ ). In classical BI logic, separating conjunction is designed to describe heap resources from a local and restricted view. Concretely speaking, ℎ ⊨ 𝜓 ∗ ... 5 suggests that 𝜓 is interpreted within a restriction of ℎ , and full information about ℎ is not necessary to check validity of 𝜓 . This idea has been carried forward in our assertion language as well, but instead of separating quantum heaps, we choose to restrict the domain and combine local interpretations of assertions to describe entangled quantum heaps, as shown in Fig. 5b.

Mathematically, J 𝜓 1 ∗ 𝜓 2 K ( 𝑑 ) ≜ 𝑑 ′ ⊆ 𝑑 J 𝜓 1 K ( 𝑑 ′ ) ⊗ J 𝜓 2 K ( 𝑑 \ 𝑑 ′ ) suggests that the domain 𝑑 is split into two disjoint parts: 𝑑 ′ and 𝑑 \ 𝑑 ′ , and we interpret assertions 𝜓 1 , 𝜓 2 on 𝑑 ′ , 𝑑 \ 𝑑 ′ separately. Then we combine them with tensor product to form a projection operator on the entire domain 𝑑 . Since for classical heaps we only require the existence of sub-heaps ℎ 1 , ℎ 2 , thus similarly we use disjunction ( ∨ ) to join cases of different 𝑑 ′ and 𝑑 \ 𝑑 ′ .

Example 4.1. Consider an assertion 𝜓 ≜ 𝑞 1 ↦→ 𝐼 ∗ 𝑞 2 ↦→ 𝐼 , then given a quantum heap 𝜌 = 1 2 (| 00 ⟩ + | 11 ⟩) 𝑞 1 ,𝑞 2 (⟨ 00 | + ⟨ 11 |) , we could check that 𝜌 ⊨ 𝜓 because 𝑑𝑜𝑚 𝜌 = { 𝑞 1 , 𝑞 2 } and:

$$[ \psi ] \{ q _ { 1 } , q _ { 2 } \} & = [ q _ { 1 } \mapsto I ] \emptyset \otimes [ q _ { 2 } \mapsto I ] \{ q _ { 1 } , q _ { 2 } \} \vee [ \mathbb { q } _ { 1 } \mapsto I ] \{ q _ { 1 } \} \otimes [ \mathbb { q } _ { 2 } \mapsto I ] \{ q _ { 2 } \} \vee \\ & \quad [ q _ { 1 } \mapsto I ] \{ q _ { 2 } \} \otimes [ \mathbb { q } _ { 2 } \mapsto I ] \{ q _ { 1 } \} \vee [ \mathbb { q } _ { 1 } \mapsto I ] \{ q _ { 1 } , q _ { 2 } \} \otimes [ \mathbb { q } _ { 2 } \mapsto I ] \emptyset \\ & = 0 _ { q _ { 1 } , q _ { 2 } } \vee I _ { q _ { 1 } , q _ { 2 } } \vee 0 _ { q _ { 1 } , q _ { 2 } } \vee 0 _ { q _ { 1 } , q _ { 2 } } = I _ { q _ { 1 } , q _ { 2 } }$$

and ⌈ 𝜌 ⌉ = { 1 √ 2 (| 00 ⟩ + | 11 ⟩) 𝑞 1 ,𝑞 2 } ⊆ 𝐼 𝑞 1 ,𝑞 2 . This example illustrates that an entangled state could also satisfy a separable assertion.

Example 4.2. Similar to notations in [28, 52], we denote 𝑞 ↩ → 𝑃 ≜ 𝑞 ↦→ 𝑃 ∗ ⊤ which indicates that the quantum heap contains at least 𝑞 rather than exactly 𝑞 . It could be verified that:

$$| 0 1 \rangle _ { q _ { 1 } , q _ { 2 } } \langle 0 1 | \, \vDash \, q _ { 1 } \hookrightarrow | 0 \rangle \langle 0 | \quad b u t \quad | 0 1 \rangle _ { q _ { 1 } , q _ { 2 } } \langle 0 1 | \, \vDash \, q _ { 1 } \mapsto | 0 \rangle \langle 0 |$$

5 In classical separation logic, ℎ ⊨ 𝜓 ∗ 𝜑 △ ⇐⇒ ∃ disjoint ℎ 1 , ℎ 2 𝑠.𝑡 . ℎ is the combination of ℎ 1 and ℎ 2 . ℎ 1 ⊨ 𝜓 and ℎ 2 ⊨ 𝜑

Moreover, the projection-based and separation-in-domain semantics ensures validity of local reasoning, essence of which could be formally described as:

$$\forall \mathcal { E } , P , Q . \exists P ^ { \prime } . \lceil \rho \rceil \subseteq P \otimes Q \implies \left \lceil ( \mathcal { E } _ { d o m P } \otimes I _ { d o m Q } ) ( \rho ) \rceil \subseteq P ^ { \prime } \otimes Q$$

The implication above suggests that the domain of quantum operation E (i.e. 𝑑𝑜𝑚𝑃 ) is sufficient to ensure that E will not affect other disjoint parts of assertion (i.e. projection 𝑄 stays unchanged) no matter whether 𝜌 is entangled or not. As we will see in Section 6, this forms the cornerstone of the validity of the frame rule [44] in our program logic.

Separating implication ( - ∗ ). There are two primary intuitions about separating implication which is also referred to as the magic wand in certain context: (i). 𝜓 1 - ∗ 𝜓 2 is the weakest assertion 𝜑 satisfying 𝜓 1 ∗ 𝜑 ⊨ 𝜓 2 where the double turnstile stands for the entailment relation between assertions introduced immediately after. (ii). 𝜌 ⊨ 𝜓 1 - ∗ 𝜓 2 suggests that, for any expansion 𝜌 ′ (not necessarily in the form of 𝜌 ⊗ 𝜎 ) of 𝜌 , if the expanded part satisfies 𝜓 1 , then the whole heap 𝜌 ′ will satisfy 𝜓 2 .

Our semantics perfectly fits both of these two intuitions. For (i), 𝑃 -⊗ 𝑄 is the largest subspace 𝑅 such that 𝑃 ⊗ 𝑅 ⊆ 𝑄 and we could prove that 𝜓 ∗ 𝜑 ⊨ 𝜙 ⇐⇒ 𝜓 ⊨ 𝜑 - ∗ 𝜙 in the next section. For (ii), the semantics J 𝜓 1 - ∗ 𝜓 2 K ( 𝑑 ) ≜ 𝑑 ′ ⊆ 𝑓 𝑖𝑛 qDomain ,𝑑 ′ ∩ 𝑑 = ∅ J 𝜓 1 K ( 𝑑 ′ ) -⊗ J 𝜓 2 K ( 𝑑 ′ ∪ 𝑑 ) mean that: If for an arbitrarily disjoint domain 𝑑 ′ (which could be understood as the expanded part), 𝜌 satisfies 𝜓 2 in 𝑑 ′ ∪ 𝑑 'excluding' 𝜓 1 on 𝑑 ′ , then any expansion of 𝜌 to domain 𝑑 ′ ∪ 𝑑 will satisfy 𝜓 2 if the expanded part satisfies 𝜓 1 . This 'exclusion' is carried out with ( -⊗ ), which serves as an adjoint connective of the tensor product ( ⊗ ) with respect to projection operators. The combination of ( ∧ ) and ( -⊗ ) in the semantics of separating implication can also be viewed as corresponding to the combination of ( ∨ ) and ( ⊗ ) in the semantics of separating conjunction ( ∗ ).

$$\text {Combination of } & ( v ) \text { and } ( \S ) \text { in the semantics of separating conjunction} ( \S ) . \\ & \exp A 3 . \text { Consider} \psi \triangle q _ { 1 } \mapsto | 0 \rangle \langle 0 | + q _ { 1 } , q _ { 2 } \mapsto | 0 \rangle \langle 0 | , \text { then} \\ & [ \psi ] \{ q _ { 2 } \} = \bigwedge _ { q _ { 2 } \notin \mathcal { S } } \exp A \left [ q _ { 1 } \mapsto | 0 \rangle \langle 0 | \right ] ( d ) \to [ q _ { 1 } , q _ { 2 } \mapsto | 0 \rangle \langle 0 | ] \left ( d \cup \{ q _ { 2 } \} \right ) \\ & = ( | 0 \rangle _ { q _ { 1 } } \langle 0 | - \otimes | 0 | _ { q _ { 1 } , q _ { 2 } } ( | 0 | ) \wedge ( \bigwedge _ { d \neq \{ q _ { 1 } \} } 0 _ { d } - \otimes \dots ) \\ & = | 1 \rangle _ { q _ { 2 } } ( | 1 | ) \\ & \text {which suggests that for the quantum heap } 0 \text {, if } q _ { 1 } \mapsto q _ { 1 } \mapsto | 1 \rangle \langle 1 | \text {, then} \text { loosely speaking} \text { after}$$

which suggests that, for the quantum heap 𝜌 , if 𝜌 ⊨ 𝑞 2 ↦→ | 1 ⟩⟨ 1 | , then, loosely speaking, after appending another heap satisfying 𝑞 1 ↦→ | 0 ⟩⟨ 0 | the whole heap will satisfy 𝑞 1 , 𝑞 2 ↦→ | 01 ⟩⟨ 01 | . This exactly reflects our intuitive understanding of separating implication.

Example 4.4. Consider 𝜓 ≜ 𝑞 ↦→ 𝐼 - ∗ 𝑞 ↩ → 𝐼 . By careful computation, we notice that for arbitrary domain 𝑑 , J 𝜓 K ( 𝑑 ) = 𝐼 𝑑 , which means 𝜓 is equivalent to ⊤ . Intuitively, 𝑞 ↦→ 𝐼 - ∗ 𝑞 ↩ → 𝐼 requires that if another heap with domain { 𝑞 } is appended, then the whole heap will contain at least 𝑞 . This is obviously a tautology.

## 4.3 Entailment Relation and Proof System

After introducing the entailment relation and inference rules for our BI-style assertion language, we believe that the readers will get a deeper understanding of the semantics defined in last section.

Definition 4.1 (Entailment Relation). We say ' 𝜓 entails 𝜑 ', denoted 𝜓 ⊨ 𝜑 , if and only if

$$\psi \vdash \varphi \iff \forall d \subseteq _ { f i n } q \Box \text {main.} \ [ \psi ] \ ( d ) \subseteq [ \varphi ] \ ( d ) \\ \intertext { g l e m m a j u i s f i t i s the definition of the entailment relation between }$$

The following lemma justifies the definition of the entailment relation between assertions.

Lemma 4.2. For any assertions 𝜓 and 𝜑 ,

$$\psi \, \Leftrightarrow \, \varphi \, \Longleftrightarrow \, \forall \rho \in Q \text {Heap} . \, \rho \, \Leftrightarrow \, \psi \, \Longrightarrow \, \rho \, \Leftrightarrow \, \varphi$$

Fig. 7. Hilbert-style proof system for quantum BI logic, where 𝑖 = 1 or 2 for Rules 5 and 8. 𝜓 and 𝜑 are compatible if for each domain 𝑑 ⊆ 𝑓 𝑖𝑛 qDomain , projection operators J 𝜓 K ( 𝑑 ) and J 𝜑 K ( 𝑑 ) are compatible.

| 0 .   | ¬¬ 𝜓 ⊢ 𝜓                  | 1 .   | 𝜓 ⊢ 𝜓                       | 2 .   | 𝜓 ⊢ ⊤                                  |
|-------|---------------------------|-------|-----------------------------|-------|----------------------------------------|
| 3 .   | ⊥ ⊢ 𝜓                     | 4 .   | 𝜂 ⊢ 𝜓 𝜂 ⊢ 𝜑 𝜂 ⊢ 𝜓 ∧ 𝜑       | 5 .   | 𝜂 ⊢ 𝜓 1 ∧ 𝜓 2 𝜂 ⊢ 𝜓 𝑖                  |
| 6 .   | 𝜑 ⊢ 𝜓 𝜂 ∧ 𝜑 ⊢ 𝜓           | 7 .   | 𝜂 ⊢ 𝜓 𝜑 ⊢ 𝜓 𝜂 ∨ 𝜑 ⊢ 𝜓       | 8 .   | 𝜂 ⊢ 𝜓 𝑖 𝜂 ⊢ 𝜓 1 ∨ 𝜓 2                  |
| 9 .   | 𝜉 ⊢ 𝜑 𝜂 ⊢ 𝜓 𝜉 ∗ 𝜂 ⊢ 𝜑 ∗ 𝜓 | 10 .  | 𝜂 ⊢ 𝜑 ⇝ 𝜓 𝜂 ⊢ 𝜑 𝜂 ⊢ 𝜓       | 11 .  | 𝜑 ⊢ 𝜓 𝜑 and 𝜂 are compatible 𝜂 ⊢ 𝜑 ⇝ 𝜓 |
| 12 .  | 𝜂 ∗ 𝜑 ⊢ 𝜓 𝜂 ⊢ 𝜑 - ∗ 𝜓     | 13 .  | 𝜉 ⊢ 𝜑 - ∗ 𝜓 𝜂 ⊢ 𝜑 𝜉 ∗ 𝜂 ⊢ 𝜓 | 14 .  | ( 𝜑 ∗ 𝜓 ) ∗ 𝜉 ⊢ 𝜑 ∗ ( 𝜓 ∗ 𝜉 )          |
| 15 .  | 𝜓 ∗ 𝜑 ⊢ 𝜑 ∗ 𝜓             | 16 .  | 𝜓 ∗⊤ ∗ ⊢ 𝜓                  | 17 .  | 𝜓 ⊢ 𝜓 ∗⊤ ∗                             |

Example 4.5. It holds that 𝑞 ↦→ 𝐼 ⊨ 𝑞 ↦→ 𝐼 ∨ 𝑞 ′ ↦→ | 0 ⟩⟨ 0 | , although the right-hand side formula involves two qubits 𝑞, 𝑞 ′ , while the left-hand side formula involves only one qubit 𝑞 . This example illustrates another reason for domain-dependent semantics: it enables us to reason about the entailment between assertions with different qubits involved.

Furthermore, we develop a Hilbert-style proof system for quantum BI-style logic similar to one in classical BI logic where the turnstile ⊢ ⊆ Assr × Assr is used to represent the derivation, that is, 𝜓 ⊢ 𝜑 is interpreted as from 𝜓 , we can derive 𝜑 .

The proof system for quantum BI-style logic is shown in Fig. 7. Compared with the inference rules presented in [18, 28], the only compromise for our BI-style logic is rule 11 due to the limitation of Sasaki hook as introduced above. Inference rules concerned with separating conjunction ( ∗ ) and separating implication ( - ∗ ) all work well for quantum BI-style logic.

Proposition 4.1 (Soundness of Proof System for Quantum BI-style Logic). The proof system defined in Fig. 7 is sound, i.e. if 𝜓 ⊢ 𝜑 , then 𝜓 ⊨ 𝜑 .

Example 4.6. We show 𝑞 ↦→ 𝐼 ⊢ 𝑞 ↩ → 𝐼 , which indicates that a quantum heap containing exactly one qubit 𝑞 is an instance of heaps that contain at least 𝑞 . Using Rules 1 and 2, we derive 𝑞 ↦→ 𝐼 ⊢ 𝑞 ↦→ 𝐼 and ⊤ ∗ ⊢ ⊤ , respectively. Then

$$q \mapsto I * \top ^ { * } \mapsto I * \top$$

from Rule 9, and 𝑞 ↦→ 𝐼 ⊢ 𝑞 ↦→ 𝐼 ∗ ⊤ ∗ from Rule 17. Thus, the conclusion follows.

In addition to the inference rules in Fig. 7, we provide several additional inference rules for quantum atomic predicates.

Proposition 4.2 (Additional Atomic Inference Rules). The following useful inference rules for atomic predicates are sound:

$$\frac { \bar { q } \cap \bar { q } ^ { \prime } \dot { = } \emptyset } { \bar { q } \mapsto P \ast \bar { q } ^ { \prime } \mapsto Q + \bar { q } , \bar { q } ^ { \prime } \mapsto P \otimes Q } \quad \frac { P \subseteq Q } { \bar { q } \mapsto P + \bar { q } \mapsto Q } \quad \frac { \mapsto \{ \wedge , \vee \} } { \bar { q } \mapsto P \rtimes \bar { q } \mapsto Q + \bar { q } \mapsto P \rtimes Q } \\ \frac { \overline { \bar { q } \mapsto P \wedge \bar { q } \hookrightarrow Q + \bar { q } \mapsto P \wedge Q } } { \bar { q } \mapsto P \wedge \bar { q } \hookrightarrow Q + \bar { q } \mapsto P \wedge Q } \quad \frac { \overline { \bar { q } \mapsto P \vee \bar { q } \hookrightarrow Q + \bar { q } \hookrightarrow P \vee Q } } { \bar { q } \mapsto P \vee \bar { q } \hookrightarrow Q + \bar { q } \hookrightarrow P \vee Q } \quad \frac { \overline { \bar { q } \mapsto P \rtimes \bar { q } \mapsto Q } } { \bar { q } \mapsto P \rtimes \bar { q } \mapsto Q + \bar { q } \hookrightarrow P \rtimes Q }$$

Example 4.7. We show 𝑞 ↦→ 𝐼 ⊢ 𝑞 ↩ → 𝑃 ⇝ 𝑞 ↦→ 𝑃 for arbitrary 𝑃 . It is simple to check that 𝑞 ↩ → 𝑃 and 𝑞 ↦→ 𝐼 are compatible and we know that 𝑞 ↦→ 𝐼 ∧ 𝑞 ↩ → 𝑃 ⊢ 𝑞 ↦→ 𝑃 . The conclusion then follows from Rule 11.

## 5 A Quantum Programming Language with Heap Manipulations

In this section, we introduce Qwhile-hp , a quantum programming language with heap manipulations. It extends the Qwhile language proposed in [66, 68] by incorporating the general allocation and disposal of dirty qubits discussed in Section 3.1.

The statements of Qwhile-hp are generated according to the following grammar:

```
Statement 𝑆 :: = skip | qalloc ( 𝑞 ) | qfree ( 𝑞 ) | [ 𝑞 ] : = | 0 ⟩ | 𝑈 [ 𝑞 ] | 𝑆 1 ; 𝑆 2 | if □ 𝑚 · 𝑀 𝑃 [ 𝑞 ] → 𝑆 𝑚 fi | while 𝑀 𝑃 [ 𝑞 ] do 𝑆 end
```

where 𝑞 is an ordered distinct list of quantum address, and 𝑈 denotes a 2 | 𝑞 | -dimensional unitary gate. 𝑀 𝑃 = { 𝑃 𝑚 } in the if-statement is a projective measurement satisfying ˝ 𝑚 𝑃 𝑚 = 𝐼 , and 𝑀 𝑃 in the while-loop stands for a 0/1 measurement. The semantics of quantum if-branching can be straightforwardly interpreted: if the measurement result is 𝑚 , then the branch 𝑆 𝑚 will be executed. For quantum while-loops, the loop body 𝑆 is executed repeatedly until the measurement result becomes 0. Unless otherwise specified, we use if 𝑀 𝑃 [ 𝑞 ] then 𝑆 1 else 𝑆 0 to denote a binary if-branching.

From the perspective of programming language, we only take the allocation of dirty qubits into account because clean ones can be produced and analyzed with an initialization statement. But in practical implementations such as Q# [58], the compiler needs to distinguish between allocating a dirty qubit and allocating a clean qubit. Each time a dirty qubit is allocated, the operating system will execute an automated verifier (which could be developed with the criteria discussed in Section 7) to decide whether the dirty qubit is used correctly. If so, the OS is reassured to borrow a qubit from other parts of computation, while if not, the OS has to assign another qubit that may not be in the ground state, but whose ownership is necessarily unoccupied.

A program configuration in Qwhile-hp is defined as a pair ( 𝑆, 𝜌 ) ⊆ ( Statement ∪{↓})× QHeap that functions as a global description of both the current quantum heap 𝜌 and the remaining program 𝑆 to be executed. The symbol ↓ indicates successful termination. The small-step operational semantics of Qwhile-hp is defined as a transition ( 𝑆, 𝜌 ) → ( 𝑆 ′ , 𝜌 ′ ) between program configurations, representing a step of execution. The relation → is determined by the rules defined in Fig. 8 that formalize the manipulations of the quantum heaps detailed in Section 3.

Since the allocation of dirty qubits is inherently nondeterministic and quantum measurement typically involves a probabilistic nature, our language must accommodate both nondeterministic and probabilistic choices. However, our use of an assertion language with projection-based semantics implies that we do not consider probabilistic properties; instead, we distinguish only between 'possible' and 'impossible' outcomes.

Statements like [ 𝑞 ] : = | 0 ⟩ , 𝑈 [ 𝑞 ] , and 𝑀 𝑃 [ 𝑞 ] are typical quantum operations that can get stuck (meaning that no rules can progress further) if 𝑞 is out of heap memory. Similarly, attempting to reclaim qubits that are not within the heap domain will also result in getting stuck during execution. For notations, we use

$$[ S ] \, \rho \, \triangle q \, \{ \rho ^ { \prime } \in Q H e a p \, \colon ( S , \rho ) \to ^ { * } ( \downarrow , \rho ^ { \prime } ) \}$$

J K to denote the set of successfully terminating program states, where → ∗ ≜ -∞ 𝑛 = 0 → 𝑛 indicates the reflexive and transitive closure of the binary relation → .

Example 5.1 (Unrealistic Execution). Consider such a program:

```
𝑆 ≜ ( if 𝑀 𝑃 [ 𝑞 1 ] then skip else skip ) ; qfree ( 𝑞 2 ) ; qalloc ( 𝑞 2 )
```

$$B l \text {based Reasoning about Quantum Programs with Heap Manipulations} \\ \text {Skip} & \quad \text {INIT} & \quad \bar { q } \subseteq d o m \rho \\ \underbar { ( \langle q \rangle = | 0 \rangle , \rho ) } & \to \left ( \downarrow , \sum _ { i = 0 } ^ { 2 ^ { 1 / 1 } } | 0 \rangle _ { \overline { q } } \langle i | \rho _ { i } \rangle _ { \overline { q } } \langle 0 | \right ) & \quad \text {UNTRARY} & \quad \bar { q } \subseteq d o m \rho \\ \text {QALLOC} & \quad \text {Q-Loop} & \quad \bar { q } \sqcup _ { i } | \rho _ { i } | _ { \overline { q } } \langle 0 | \\ \underbar { \underline { \ell } \in Q \arg 1 e } & \text {dom } \rho & \quad \bar { p } \in \mathcal { D } ( \mathcal { H } _ { \dom n } \rho _ { \overline { q } } \sqcup ) & \quad \bar { q } \sqcup _ { | \dom n | = \sqcup } | q | _ { \overline { q } } + \bar { q } | _ { \overline { q } } \\ \text {QFree} & \quad \text {Sequence} & \quad \text {SEQUENCE} & \quad \text {SEQUENCE} \\ \underbar { \frac { q \in \text {dom } \rho } { ( q \free ( q ) , \rho ) } } & \quad \frac { ( S _ { 1 } , \rho ) \to ( S _ { 1 } ^ { \prime } , \rho ^ { \prime } ) } { ( S _ { 1 } ; S _ { 2 } , \rho ) \to ( S _ { 1 } ^ { \prime } ; S _ { 2 } , \rho ^ { \prime } ) } & \quad \frac { ( S _ { 1 } , \rho ) \to ( \downarrow , \rho ^ { \prime } ) } { ( S _ { 1 } ; S _ { 2 } , \rho ) \to ( S _ { 2 } , \rho ^ { \prime } ) } \\ \text {If} & \quad \bar { q } \subseteq \text {dom } \rho & \quad P _ { m } \in M _ { P } & \quad \text {tr} ( P _ { m } \rho ) \neq 0 & \quad \bar { q } \subseteq \text {dom } \rho & \quad P _ { 0 } \in M _ { P } & \quad \text {tr} ( P _ { 0 } \rho ) \neq 0 \\ \text {if} & \in \text {M} _ { P } | \bar { q } | \to S _ { m } \, \bar { \eta } , \rho ) & \quad \text {m} _ { \overline { \ } t r ( P _ { m } \rho ) } & \quad ( \text {while } M _ { P } | \bar { q } | \, \text {do } S \text { end, } \rho ) \to \left ( \downarrow , \frac { P _ { 0 } P _ { 0 } } { \ t r ( P _ { 0 } \rho ) } \right ) & \quad \text {while } \underline { \text {loop} } & \quad \bar { q } \subseteq \text {dom } \rho & \quad P _ { 1 } \in M _ { P } & \quad \text {tr} ( P _ { 1 } \rho ) \neq 0 \\ & \quad - \text {while } M _ { P } | \bar { q } | \, \text {do } S \text { end, } \rho ) \to \left ( S ; \text {while } M _ { P } | \bar { q } | \, \text {do } S \text { end, } \frac { P _ { 1 } P _ { 1 } } { \ t r ( P _ { 1 } \rho ) } \right ) & \quad \text {fig. 8.  Operational semantics of Q while-hp}$$

Fig. 8. Operational semantics of Qwhile-hp

where 𝑀 𝑃 = { 𝑃 0 = | 0 ⟩⟨ 0 | , 𝑃 1 = | 1 ⟩⟨ 1 |} is a projective measurement. Then it can be verified that the entangled state 𝜌 ≜ 1 2 (| 00 ⟩ + | 11 ⟩) 𝑞 1 ,𝑞 2 (⟨ 00 | + ⟨ 11 |) could remain unchanged after execution of program 𝑆 , that is, 𝜌 ∈ J 𝑆 K ( 𝜌 ) . Such a computation is valid within our semantics but unrealistic in that 𝑞 2 should not be entangled with 𝑞 1 after reallocation. Tracing out qubits after measurement will wipe out any clues that the measurement might destroy the entanglement in specific states

As Example 5.1 shows, some executions that would never happen in real world are also valid with respect to rules in Fig. 8, which indicates that the operational semantics for nondeterministic allocation is somehow too general. Nevertheless, with projection-based semantics for our BI-style assertion logic as introduced in Section 4, it can be proved that for arbitrary assertion 𝜓 ,

$$\forall \rho ^ { \prime } \in [ \mathfrak { q } l o c ( q ) ] \, ( \rho ) . \rho ^ { \prime } \in \psi \iff \forall \rho ^ { \prime } \in [ \mathfrak { q } l o c ( q ) ] _ { r e a l } \, ( \rho ) . \rho ^ { \prime } \equiv \psi \iff \rho [ q \Rightarrow \sqcup ] _ { 2 } ^ { 1 } I _ { q } \equiv \psi \\$$

where J qalloc ( 𝑞 ) K 𝑟𝑒𝑎𝑙 ( 𝜌 ) denotes the set of realistic output states after allocating 𝑞 and 𝜌 [ 𝑞 ⇒ ⊔]⊗ 1 2 𝐼 𝑞 is always a realistic output state, which imply that 𝜌 [ 𝑞 ⇒⊔]⊗ 1 2 𝐼 𝑞 ∈ J qalloc ( 𝑞 ) K 𝑟𝑒𝑎𝑙 ( 𝜌 ) ⊆ J qalloc ( 𝑞 ) K ( 𝜌 ) . The equivalence suggests that although the operational semantics for nondeterministic allocation is overly general in some sense, it exactly determines the realistic set with respect to properties characterized by assertion language.

Moreover, we say that a program 𝑆 is stable in domain 𝑑 if, for any 𝜌 ∈ QHeap such that 𝑑𝑜𝑚 𝜌 = 𝑑 , the execution of 𝑆 on 𝜌 does not get stuck. In other words, the stability of program 𝑆 ensures that the input domain is sufficient to guarantee that all executions of program 𝑆 will proceed without getting stuck. We consider this property a natural requirement for ensuring robustness of quantum programs against noisy inputs, particularly when analyzing the correct usage of dirty qubits in subsequent sections.

Example5.2 (Stability of /q.sc\_u.scantum programs). The program 𝑆 ≜ if 𝑀 𝑃 [ 𝑞 ] then 𝐻 ( 𝑞 ) else 𝐻 ( 𝑞 ′ ) is not stable in the domain { 𝑞 } as it gets stuck in the input | 0 ⟩ 𝑞 ⟨ 0 | , which means that if the input state is perturbed by noise and becomes a superposition containing | 0 ⟩ , then it probably gets stuck.

## Skip { 𝜓 } skip { 𝜓 } Qalloc ⊤ ∗ qalloc ( 𝑞 ) { 𝑞 ↦→ 𝐼 } Qfree { 𝑞 ↦→ 𝐼 } qfree ( 𝑞 ) ⊤ ∗ Init { 𝑞 ↦→ 𝐼 } [ 𝑞 ] : = | 0 ⟩ { 𝑞 ↦→| 0 ⟩⟨ 0 |} Unitary 𝑞 ⊆ 𝑞 ′ ⊆ 𝑓 𝑖𝑛 qName 𝑃 ∈ P(H 𝑞 ′ ) 𝑞 ′ ↦→ 𝑃 𝑈 [ 𝑞 ] n 𝑞 ′ ↦→ 𝑈𝑃𝑈 † o Se/q.sc\_u.scence { 𝜓 } 𝑆 1 { 𝜑 } { 𝜑 } 𝑆 2 { 𝜙 } { 𝜓 } 𝑆 1 ; 𝑆 2 { 𝜙 } Conse/q.sc\_u.scence 𝜓 ⊨ 𝜓 ′ 𝜓 ′ 𝑆 𝜑 ′ 𝜑 ′ ⊨ 𝜑 { 𝜓 } 𝑆 { 𝜑 } If 𝑀 𝑃 = { 𝑃 𝑚 } ∀ 𝑚. { 𝜓 𝑚 } 𝑆 𝑚 { 𝜓 } n ( 𝑞 ↩ → 𝐼 ) ∧ 𝑚 ( 𝑞 ↩ → 𝑃 𝑚 ) ⇝ 𝜓 𝑚 o if □ 𝑚 · 𝑀 𝑃 [ 𝑞 ] → 𝑆 𝑚 fi { 𝜓 } While 𝑀 𝑃 = { 𝑃 0 , 𝑃 1 } { 𝜑 } 𝑆 {( 𝑞 ↩ → 𝐼 ) ∧ (( 𝑞 ↩ → 𝑃 0 ) ⇝ 𝜓 ) ∧ (( 𝑞 ↩ → 𝑃 1 ) ⇝ 𝜑 )} {( 𝑞 ↩ → 𝐼 ) ∧ (( 𝑞 ↩ → 𝑃 0 ) ⇝ 𝜓 ) ∧ (( 𝑞 ↩ → 𝑃 1 ) ⇝ 𝜑 )} while 𝑀 𝑃 [ 𝑞 ] do 𝑆 end { 𝜓 } 𝑆𝑡𝑟𝑢𝑐𝑡𝑢𝑟𝑎𝑙 𝑅𝑢𝑙𝑒𝑠 Conjunction { 𝜓 1 } 𝑆 { 𝜑 1 } { 𝜓 2 } 𝑆 { 𝜑 2 } { 𝜓 1 ∧ 𝜓 2 } 𝑆 { 𝜑 1 ∧ 𝜑 2 } Disjunction { 𝜓 1 } 𝑆 { 𝜑 1 } { 𝜓 2 } 𝑆 { 𝜑 2 } { 𝜓 1 ∨ 𝜓 2 } 𝑆 { 𝜑 1 ∨ 𝜑 2 } Frame { 𝜓 } 𝑆 { 𝜑 } 𝑞𝑏𝑖𝑡 ( 𝜙 ) ∩ 𝑎𝑙𝑙𝑜𝑐 ( 𝑆 ) = ∅ { 𝜓 ∗ 𝜙 } 𝑆 { 𝜑 ∗ 𝜙 }

Fig. 9. Proof System for Quantum Separation Logic

## 6 A Quantum Separation Logic

In this section, we utilize the quantum BI-style logic introduced in Section 4 as an assertion language to reason about quantum programs with heap manipulations defined in Section 5. This approach can be seen as a quantum adaptation of the separation logic [28, 52]. The central task is to develop a sound and relatively complete proof system for Hoare-style correctness triple , formally defined as:

$$\vDash & \quad \forall \rho \in Q \text {Heap} . \rho \models \psi \implies S , \rho \text { is safe} ^ { 6 } , a n d \forall \rho ^ { \prime } \in [ S ] \left ( \rho \right ) . \rho ^ { \prime } \cong \varphi \\ \intertext { t h e x t i n i l l } \left \langle \psi \right \rangle S \left \{ \varphi \right \} \Longleftrightarrow \forall \rho \in Q \text {Heap} . \rho \models \psi \implies S , \rho \text { is safe} ^ { 6 } , a n d \forall \rho ^ { \prime } \in [ S ] \left ( \rho \right ) . \rho ^ { \prime } \cong \varphi \\ \intertext { t h e x t i n i l l } \left \langle \rho \right \rangle S \left \{ \psi \right \} \Longleftarrow \varphi \right \} \Longleftarrow \varphi$$

Intuitively, the validity of such a correctness triple implies that for any quantum heap satisfying the precondition, executing program 𝑆 on it ensures the absence of getting stuck, while producing quantum heaps that satisfy the postcondition.

## 6.1 Proof System for Quantum Separation Logic

Fig. 9 presents our core proof system for reasoning about the correctness specification, where the inference rules follow a small axiom scheme. We will show in detail that the proof system is sound, relatively complete, and consistent with our intuitive understanding.

Qalloc, Qfree. These two inference rules precisely embody our intuition regarding the allocation and disposal of qubits. In our BI-style logic, 𝑞 ↦→ 𝐼 is analogous to 𝑥 ↦→ -in classical BI logic, indicating that 𝑞 is allocated without assuming its state, since 𝐼 stands for the entire space. Qalloc states that starting from an empty heap satisfying ⊤ ∗ , after allocating 𝑞 , the heap will contain exactly 𝑞 with an arbitrary initial state. In contrast, the precondition of the rule Qfree implies that from a quantum heap containing exactly 𝑞 , regardless of the state of 𝑞 , the heap will be empty after freeing 𝑞 .

6 The jargon term safe comes from [28] which means execution of 𝑆 on 𝜌 will not get stuck

, Vol. 1, No. 1, Article . Publication date: September 2024.

Init, Unitary. As introduced in Section 3, the most significant difference between classical mutation and quantum mutation is that quantum mutation follows a 'transformation' pattern, necessitating the recording of the old value 𝑃 of target qubits 𝑞 . Rules Init and Unitary embody our understanding of quantum heap mutations, where quantum operations directly affect the target qubits. However, a tricky completeness issue in the quantum setting involves reasoning about entangled states. To address this, we adjust the Unitary rule to handle larger heaps containing at least 𝑞 , rather than exactly 𝑞 . This modification is unnecessary for initialization statements, as the state remains unentangled after initialization.

Se/q.sc\_u.scence. The Se/q.sc\_u.scence rule is straightforward; it allows the sequential composition of correctness triples to reason about programs structured in a sequential manner.

If, While. These two rules reveal a novel application of the Sasaki hook in reasoning about the precondition of quantum if-branching. The assertion ' 𝑞 ↩ → 𝐼 ' in the precondition ensures that the measurement on 𝑞 will not get stuck, while 𝑚 ( 𝑞 ↩ → 𝑃 𝑚 ⇝ 𝜓 𝑚 ) indicates that if the measurement outcome is 𝑚 , then the post-measurement quantum heap will satisfy 𝜓 𝑚 . For those who are familiar with Hoare logic, the inference rule for the if statement can also be presented in another form:

$$\frac { \forall m . \{ \psi _ { m } \} \, S \, \{ \psi \} } { \left \{ \bigvee _ { m } ( \bar { q } \hookrightarrow P _ { m } ) \wedge \psi _ { m } \right \} \text { if } \Box m \cdot M _ { P } [ \bar { q } ] \rightarrow S _ { m } \text { if } \{ \psi \} } I _ { F }$$

Such an inference rule appears to be more tidy and concise as the precondition inherently implies 𝑞 ↩ → 𝐼 . However, it is discouraged in practice because the ( ∨ )-introduction rule (i.e., rule 8 in Fig. 7) is very weak in quantum logic. We can prove 𝜓 ⊨ 𝑚 ( 𝑞 ↩ → 𝑃 𝑚 ) ∧ 𝜓 𝑚 with the inference rules in Fig. 7 only if 𝜓 ⊨ ( 𝑞 ↩ → 𝑃 𝑚 ) ∧ 𝜓 𝑚 for some 𝑚 , which means that only one branch of the if statement can potentially be executed. Such a scenario is reasonable in classical programming languages, where guard conditions are mutually exclusive. However, in quantum programming, multiple branches of the if statements are chosen nondeterministically. Therefore, the precondition needs to maintain a more easily deducible form, and the Sasaki hook is a well-studied connective with many algebraic properties that aid in reasoning about related formulas.

In While, 𝜑 is commonly known as the loop invariant , ensuring that any quantum heap satisfying 𝜑 continues to satisfy 𝜑 after executing 𝑆 , if the measurement result is 1. When the measurement result is 0, the loop terminates and 𝜓 must hold. A concrete example illustrating reasoning about a program with a while loop will be demonstrated in Section 8.2.

Conjunction, Disjunction. The structural rule for conjunction works exactly as it does in classical program logic, since in quantum BI-style logic, conjunction is interpreted in the same way as in classical logic: 𝜌 ⊨ 𝜓 1 ∧ 𝜓 2 ⇐⇒ 𝜌 ⊨ 𝜓 1 and 𝜌 ⊨ 𝜓 2 . Therefore, 𝑤𝑙𝑝.𝑆. ( 𝜓 1 ∧ 𝜓 2 ) = 𝑤𝑙𝑝.𝑆.𝜓 1 ∧ 𝑤𝑙𝑝.𝑆.𝜓 2 7 . However, it does not hold for disjunction since, in our BI-style quantum logic, disjunction is interpreted as a spanned subspace. This implies that 𝑤𝑙𝑝.𝑆. ( 𝜓 1 ∨ 𝜓 2 ) can be strictly weaker than 𝑤𝑙𝑝.𝑆.𝜓 1 ∨ 𝑤𝑙𝑝.𝑆.𝜓 2 , as the following example shows.

Example 6.1. The following correctness specifications can be verified:

$$\{ \perp \} \, [ q ] \colon = | 0 \rangle \, \{ q \mapsto | + \rangle \langle + | \} \quad \{ \perp \} \, [ q ] \colon = | 0 \rangle \, \{ q \mapsto | - \rangle \langle - | \} ,$$

as the output state can never be |+⟩⟨+| or |-⟩⟨-| after initialization. However, their combination {⊥} [ 𝑞 ] : = | 0 ⟩ { 𝑞 ↦→|+⟩⟨+| ∨ 𝑞 ↦→|-⟩⟨-|} using the Disjunction rule is far from satisfactory because the postcondition simplifies to 𝑞 ↦→ 𝐼 , which allows for deriving a much weaker precondition 𝑞 ↦→ 𝐼 than ⊥ .

7 𝑤𝑙𝑝.𝑆.𝜓 is a conventional notation to denote the weakest liberal precondition for program 𝑆 and postcondition 𝜓

Frame. Note that in the premise of Rule Frame, 𝑞𝑏𝑖𝑡 ( 𝜙 ) denotes the set of qubit names appearing in assertion 𝜙 , while 𝑎𝑙𝑙𝑜𝑐 ( 𝑆 ) denotes the set of qubit names allocated in program 𝑆 . In classical programming languages, there are three typical assignments that involve pointers: (1) allocation: 𝑥 : = 𝑛𝑒𝑤 ( 𝑣 ) , (2) simple assignment: 𝑥 : = 𝑣 , and (3) addressing assignment: [ 𝑥 ] : = 𝑣 . Both (1) and (2) modify the value of the variable 𝑥 , while (3) modifies the value at the address 𝑥 . In classical separation logic, the premise for the Frame rule requires 𝐹𝑉 ( 𝜙 ) ∩ 𝑚𝑜𝑑 ( 𝑆 ) = ∅ [28, 52], where the set 𝑚𝑜𝑑 ( 𝑆 ) accounts for variables modified in statements (1) or (2) in the program 𝑆 , and the modification in statement (3) is inherently described by spatial separation. In Qwhile-hp , only assignments (1) and (3) can be executed, and we do not allow statements like 𝑞 : = 𝑞 ′ . Consequently, 𝑎𝑙𝑙𝑜𝑐 ( 𝑆 ) = 𝑚𝑜𝑑 ( 𝑆 ) in our setting.

The Frame rule is often considered the core of local reasoning, as it reveals the essence of separating conjunction and why such a logical connective is needed. Unlike structural rules for conjunction and disjunction, the premise in Frame concerns only one clause of ( ∗ ). This suggests that, for an arbitrary quantum heap 𝜌 , if its restriction satisfies 𝜓 , then this restriction contains all the information needed to execute 𝑆 . As a result, the execution of 𝑆 on 𝜌 can be completely described by the execution on the restriction. This idea of local reasoning will greatly simplify our proof and we will illustrate it with the following concrete example.

Example 6.2. To derive { 𝑞 1 ↦→| 0 ⟩⟨ 0 | ∗ 𝑞 2 ↦→| 0 ⟩⟨ 0 |} 𝐻 ( 𝑞 1 ) { 𝑞 1 ↦→|+⟩⟨+| ∗ 𝑞 2 ↦→| 0 ⟩⟨ 0 |} , we can temporarily neglect 𝑞 2 in the postcondition and get { 𝑞 1 ↦→| 0 ⟩⟨ 0 |} 𝐻 ( 𝑞 1 ) { 𝑞 1 ↦→|+⟩⟨+|} . The result is then obtained using Rule Frame by simply 'pasting' 𝑞 2 ↦→| 0 ⟩⟨ 0 | without any additional burden.

Theorem 6.1 (Soundness and Relative Completeness). The proof system defined in Fig. 9 is sound and relatively complete; that is, if all valid entailments 𝜓 ⊨ 𝜑 are derivable, then ⊨ { 𝜓 } 𝑆 { 𝜑 } if and only if { 𝜓 } 𝑆 { 𝜑 } is derivable from the proof system in Fig. 9.

## 6.2 Backward Inference Rules Expressed by Separating Implication

In this section, we present inference rules in a backward scheme, which simplifies proofs in practical usage by placing no restrictions on the structure of postconditions. However, similar to classical logic, universal quantifier ( ∀ ) and renaming 𝜓 [ 𝑞 ⇒ 𝑞 ′ ] are necessary to describe preconditions involving nondeterministic allocation. Specifically, we extend our assertion language to include formulas of the form ∀ 𝑞 ′ .𝜓 [ 𝑞 ⇒ 𝑞 ′ ] , where 𝜓 is generated by the grammar in Fig. 4b. The formal semantics is defined as

$$\mathbb { [ } \forall q ^ { \prime } . \psi [ q \Rightarrow q ^ { \prime } ] ] \left ( d \right ) \triangle \bigcap _ { q ^ { \prime } \in \L q \Name } \mathbb { [ } \psi [ q \Rightarrow q ^ { \prime } ] ] \left ( d \right ) \\ \\ \mathbb { [ } 1 _ { q } - 1 _ { q } \cdot \dot { q } ^ { \prime } \cdot 1 _ { q } \cdot \dot { q } \cdot 1 _ { q } - 1 _ { q } \cdot \dot { q } \cdot \dot { q } ^ { \prime } \cdot \dot { q } + 1 _ { q } \cdot \dot { q } ^ { \prime } \cdot \dot { q } \cdot 1 _ { q } \cdot \dot { q }$$

where 𝜓 [ 𝑞 ⇒ 𝑞 ′ ] denotes the assertion obtained by substituting 𝑞 in 𝜓 with 𝑞 ′ . The universal quantifier encompasses infinitely many qubit names and allows us to reason about assertions in a classical manner by considering all possible renamings. Therefore, while the new construct enhances our proof capabilities, we consider it an extension rather than part of our core assertion language, emphasizing its role in facilitating rigorous proofs involving quantum heap manipulations.

Example 6.3. Let 𝜓 ≜ 𝑞 ↦→ 𝐼 - ∗ 𝑞 ↦→ 𝐼 . Then

$$\mathbb { I } ^ { \forall q ^ { \prime } , \psi [ q \Rightarrow q ^ { \prime } ] ] \left ( d \right ) = \bigcap _ { q ^ { \prime } \in \mathbf q ^ { \Name } } \left [ \mathbb { q } ^ { \prime } \mapsto I \ast q ^ { \prime } \mapsto I \right ] \left ( d \right ) = \left [ \mathbb { T } ^ { \ast } \right ] \left ( d \right ) . \\$$

Furthermore, inference rules can be introduced for reasoning about formulas featuring a universal quantifier:

Init { 𝑞 ↦→ 𝐼 ∗ ( 𝑞 ↦→| 0 ⟩⟨ 0 | - ∗ 𝜓 )} [ 𝑞 ] : = | 0 ⟩ { 𝜓 } Unitary 𝑞 ⊆ 𝑞 ′ ⊆ 𝑓 𝑖𝑛 qName 𝑃 ∈ P(H 𝑞 ′ ) n 𝑞 ′ ↦→ 𝑃 ∗ ( 𝑞 ′ ↦→ 𝑈𝑃𝑈 † - ∗ 𝜓 ) o 𝑈 [ 𝑞 ] { 𝜓 } Qalloc 𝜑 ≜ 𝑞 ↦→ 𝐼 - ∗ 𝜓 ∀ 𝑞 ′ .𝜑 [ 𝑞 ⇒ 𝑞 ′ ] qalloc ( 𝑞 ) { 𝜓 } Qfree { 𝑞 ↦→ 𝐼 ∗ 𝜓 } qfree ( 𝑞 ) { 𝜓 }

Fig. 10. Backward inference rules for program statements

Lemma 6.1. The following three inference rules are sound:

$$\frac { q _ { 1 } \in \mathbf q ^ { \dagger } _ { 1 } } { \forall q ^ { \prime } . \psi [ q \Rightarrow q ^ { \prime } ] \vdash \psi [ q \Rightarrow q _ { 1 } ] } \quad \frac { \psi \cong \varphi } { \forall q ^ { \prime } . \psi [ q \Rightarrow q ^ { \prime } ] \vdash \forall q ^ { \prime } . \varphi [ q \Rightarrow q ^ { \prime } ] } \quad \frac { q \notin q b i t ( \psi ) } { \psi \vdash \forall q ^ { \prime } . \psi [ q \Rightarrow q ^ { \prime } ] }$$

where 𝑞𝑏𝑖𝑡 ( 𝜓 ) denotes the set of qubit names in 𝜓 .

Now we are ready to present the proof system in a backward fashion, as outlined in Fig. 10. We will briefly illustrate the intuitive ideas that underlie them.

Theorem 6.2 (Soundness of Extended Proof System). The proof system defined in Fig. 9 remains sound when supplemented with the additional backward inference rules in Fig. 10.

Init, Unitary. Both Init and Unitary are formulated as updates that can be expressed with ( ∗ ) and ( - ∗ ), aligning with the classical separation logic (cf. Section 5 in [28]).

Qalloc, Qfree. To reason about allocation, the precondition needs to enumerate qubit names to account for all possible nondeterministic choices, similar to classical separation logic [28].

Example 6.4. Let 𝜓 ≜ 𝑞, 𝑞 1 ↩ → 𝐼 . Using the rules in Lemma 6.1, we derive

$$q _ { 1 } \hookrightarrow I \ \Rightarrow \ \forall q ^ { \prime } . ( q _ { 1 } \hookrightarrow I ) [ q \Rightarrow q ^ { \prime } ] \ \not \ = \ \forall q ^ { \prime } . ( q \mapsto I \ast q , q _ { 1 } \hookrightarrow I ) [ q \Rightarrow q ^ { \prime } ] .$$

Thus, we conclude ⊨ { 𝑞 1 ↩ → 𝐼 } qalloc ( 𝑞 ) { 𝑞, 𝑞 1 ↩ → 𝐼 } with the Consequence rule.

Rule Qfree embodies our understanding of the separating conjunction: if a quantum heap can be described by the separable assertion 𝑞 ↦→ 𝐼 ∗ 𝜓 , then after reclaiming 𝑞 , the remaining part will satisfy 𝜓 . Furthermore, it can be shown that both the rules Qfree and Qalloc yield the weakest liberal precondition for qfree ( 𝑞 ) and qalloc ( 𝑞 ) , respectively.

## 7 Correct Usage of Dirty Qubits

In this section, we construct a realistic model from scratch to demonstrate scenarios that involve the allocation, use, and reclaiming of dirty qubits. Then we formally define the correct usage of dirty qubits within this model and apply our quantum separation logic to prove the correct usage of dirty qubits in quantum programs implemented in Qwhile-hp .

The semantics of Qwhile-hp is defined from a local view of the quantum system, which means that we only have access to the qubits that have been allocated, without knowing those outside the current domain. In contrast, our realistic model is constructed from a global view, which faithfully simulates real-world situations. To track domains and operations during execution, we introduce the concept of an execution path 𝜋 as:

$$\pi \colon d \stackrel { \pi _ { 1 } } { \longrightarrow } d _ { 1 } \stackrel { \pi _ { 2 } } { \longrightarrow } d _ { 2 } \stackrel { \pi _ { 3 } } { \longrightarrow } \dots \stackrel { \pi _ { n } } { \longrightarrow } d _ { n }$$

where each 𝑑 𝑖 ⊆ 𝑓 𝑖𝑛 qDomain is the domain of a quantum heap and 𝜋 𝑖 is the operation applied at the 𝑖 -th step. Such a path is sufficient to track a possible execution of the program 𝑆 until normal termination, as getting stuck is only caused by the lack of target qubits in the domain.

Fig. 11. Encoding execution path to quantum operation. If 𝑑 𝑖 ⊊ 𝑑 𝑖 + 1 , then E 𝜋 𝑖 ≜ E 𝐷𝜋 \ 𝑑 𝑖 ⊗ I 𝑑 𝑖 for arbitrary quantum operation E . If 𝑑 𝑖 ⊋ 𝑑 𝑖 + 1 , then E 𝜋 𝑖 ≜ E 𝐷𝜋 \ 𝑑 𝑖 + 1 ⊗ I 𝑑 𝑖 + 1 for arbitrary quantum operation E . If 𝑑 𝑖 = 𝑑 𝑖 + 1 , then E 𝜋 𝑖 ≜ E 𝑞 ⊗ I 𝐷𝜋 \ 𝑞 for specific E to denote a basic quantum operation.

<!-- image -->

Example 7.1 (Execution path). Consider 𝑆 ≜ if 𝑀 𝑃 [ 𝑞 ] then qfree ( 𝑞 ′ ) else qalloc ( 𝑞 ′ ) . A possible execution path starting from the domain { 𝑞, 𝑞 ′ } is 𝜋 : { 𝑞, 𝑞 ′ } 𝑃 1 ,𝑞 - - - →{ 𝑞, 𝑞 ′ } qfree ( 𝑞 ′ ) - - - - - - - → { 𝑞 } . It records that from a quantum heap containing qubits 𝑞 and 𝑞 ′ , we first measure qubit 𝑞 and get the result 1 , then qubit 𝑞 ′ is freed.

As an execution path determines the probabilistic decisions made during execution, given a quantum heap 𝜌 such that 𝑑𝑜𝑚 𝜌 = 𝑑 , we can instantiate the execution path 𝜋 on 𝜌 . Since the measurement results depend on the state of the quantum heap, we accept instantiations of the execution path with a zero matrix, as the following example illustrates.

Example 7.2. Continuing from Example 7.1, given a quantum heap 𝜌 ≜ |+ , 0 ⟩ 𝑞,𝑞 ′ ⟨+ , 0 | we can instantiate 𝜋 as 𝜋 ( 𝜌 ) : |+ , 0 ⟩ 𝑞,𝑞 ′ ⟨+ , 0 | 𝑃 1 ,𝑞 - - - → 1 2 | 1 , 0 ⟩ 𝑞,𝑞 ′ ⟨ 1 , 0 | qfree ( 𝑞 ′ ) - - - - - - -→ 1 2 | 1 ⟩ 𝑞 ⟨ 1 | where we keep the coefficient 1 2 to ensure that E( 𝜌 ) ≜ | 0 ⟩ 𝑞 ⟨ 0 | 𝜌 | 0 ⟩ 𝑞 ⟨ 0 | is a valid quantum operation. However, if 𝜌 ≜ | 0 , 0 ⟩ 𝑞,𝑞 ′ ⟨ 0 , 0 | , then the instantiation is 𝜋 ( 𝜌 ) : | 0 , 0 ⟩ 𝑞,𝑞 ′ ⟨ 0 , 0 | 𝑃 1 ,𝑞 - - - → 0 𝑞,𝑞 ′ qfree ( 𝑞 ′ ) - - - - - - -→ 0 𝑞 which suggests that starting from | 0 , 0 ⟩ 𝑞,𝑞 ′ ⟨ 0 , 0 | , the path 𝜋 is executed with probability 0 .

From these two examples, we observe that ensuring correct domains is sufficient to guarantee that execution will not get stuck because stuck is only triggered by the lack of target qubits in domains. In contrast, the state value only affects the branching, which is taken into account by allowing branches with probability 0.

Next, we encode the execution path 𝜋 into a global quantum operation E 𝜋 : D(H 𝐷𝜋 ) → D(H 𝐷𝜋 ) that simulates the execution of 𝜋 in the real world, where 𝐷𝜋 ≜ -𝑖 𝑑 𝑖 represents the union of all domains encountered along 𝜋 . As is depicted in Fig. 11, we encode each step of execution into a quantum operation E 𝜋 𝑖 , and compose them to produce the encoding of 𝜋 .

- If 𝑑 𝑖 ⊊ 𝑑 𝑖 + 1 , then the 𝑖 -th step is to allocate a qubit. The execution of the 𝑖 -th step is encoded as E 𝜋 𝑖 ≜ E 𝐷𝜋 \ 𝑑 𝑖 ⊗I 𝑑 𝑖 by choosing an arbitrary E to indicate that we have no knowledge of what had happened to qubits out of domain, and those allocated qubits remain unchanged. Similarly, if 𝑑 𝑖 ⊋ 𝑑 𝑖 + 1 , then the 𝑖 -th step is to reclaim a qubit and we encode it as E 𝜋 𝑖 ≜ E 𝐷𝜋 \ 𝑑 𝑖 + 1 ⊗ I 𝑑 𝑖 + 1 .
- If 𝑑 𝑖 = 𝑑 𝑖 + 1 , then the 𝑖 -th step is to perform a basic quantum operation E[ 𝑞 ] as discussed in Section 3 which is encoded as E 𝜋 𝑖 ≜ E 𝑞 ⊗ I 𝐷𝜋 \ 𝑞 .

To encompass all possible quantum operations when 𝑑 𝑖 ≠ 𝑑 𝑖 + 1 , the execution path 𝜋 is encoded into a set of quantum operations E 𝜋 ≜ {E 𝜋 𝑛 ◦ . . . ◦ E 𝜋 1 } as demonstrated in the following example.

Example 7.3. Continuing from Example 7.1, we encode 𝜋 as

$$\mathcal { E } \pi = \underbrace { \{ ( \mathcal { E } _ { q ^ { \prime } } \otimes \mathcal { I } _ { q } ) } _ { \mathfrak { q f r e e } ( q ^ { \prime } ) } \circ \underbrace { ( P _ { 1 , q } \otimes \mathcal { I } _ { q ^ { \prime } } ) } _ { M _ { P } [ q ] } \colon \mathcal { E } _ { q ^ { \prime } } \text { is a quantum operation} \} } _ { \mathfrak { q f r e e } ( q ^ { \prime } ) }$$

with 𝐷𝜋 = { 𝑞, 𝑞 ′ } . Here, E 𝜋 exactly characterizes all possible scenarios in the real-world execution of the program along 𝜋 .

Now we are ready to give the formal definition of correct usage of dirty qubits within the realistic model above.

Definition 7.1 (Correct Usage of Dirty Qubit). Given a program 𝑆 , we say that it correctly uses the dirty qubit 𝑞 if for all execution paths 𝜋 starting from a stable domain of 𝑆 , we have either 𝑞 ∉ 𝐷𝜋 or ∀E ∈ E 𝜋. E = E ′ 𝐷𝜋 \{ 𝑞 } ⊗ I 𝑞 for some quantum operation E ′ .

Definition 7.1 comprehensively captures our intuitive understanding of the correct usage of dirty qubits and serves as a formal description of restoring dirty qubits to their original state . In simple terms, a dirty qubit 𝑞 is correctly used and restored to its original state if for those stable execution paths (as introduced in Section 5), the quantum operation E ∈ E 𝜋 that simulates execution in the realistic model is equivalent to keeping qubit 𝑞 untouched, i.e. E = E ′ ⊗ I 𝑞 .

Example 7.4. Continuing from Example 7.1, we can verify that program 𝑆 is not using dirty qubit 𝑞 ′ or 𝑞 correctly, as execution of 𝑆 might change their state.

Additionally, we aim to establish a formal approach for verifying the correct usage of dirty qubits. Fortunately, our program logic proves to be powerful enough to encompass the fundamental aspects of correct dirty qubit usage, as indicated by the following theorem.

Theorem 7.1 (Main Theorem for Correct Usage of Dirty Qubits). Suppose 𝑆 does not contain the allocation or disposal of qubit 𝑞 , and

$$\forall \psi . \, \equiv \{ \psi \} \, S \, \{ \top \} \, \Longrightarrow \{ \psi \wedge q , q ^ { \prime } \hookrightarrow | \Phi \rangle \langle \Phi | \} \, S \, \{ q , q ^ { \prime } \hookrightarrow | \Phi \rangle \langle \Phi | \}$$

where | Φ ⟩ ≜ 1 √ 2 (| 00 ⟩ + | 11 ⟩) is the maximally entangled state, and 𝑞 ′ is an arbitrary qubit not appearing in 𝑆 or 𝜓 . Then 𝑆 correctly uses the dirty qubit 𝑞 .

Theorem 7.1 suggests that to verify the correct usage of a dirty qubit, it suffices to prove a correctness specification involving an auxiliary qubit, without the need to enumerate all possible executions in realistic scenarios. In the context of quantum circuits (i.e. quantum programs composed solely of basic quantum operations), the main theorem can be further simplified to the following form.

Corollary 7.1 (Correct usage of dirty /q.sc\_u.scbits in /q.sc\_u.scantum circuits). Suppose quantum program 𝑆 does not contain statement of allocation or deallocation, then it correctly uses dirty qubit 𝑞 if 8 :

$$\vDash \left \{ \overline { q } \mapsto I * q , q ^ { \prime } \hookrightarrow | \Phi \rangle \langle \Phi | \right \} S \left \{ q , q ^ { \prime } \hookrightarrow | \Phi \rangle \langle \Phi | \right \}$$

where 𝑞 ≜ 𝑞𝑏𝑖𝑡 ( 𝑆 )\{ 𝑞 } and 𝑞 ′ ∉ 𝑞𝑏𝑖𝑡 ( 𝑆 ) . Here, 𝑞𝑏𝑖𝑡 ( 𝑆 ) denotes the set of qubits in the circuit 𝑆 .

## 8 Case Studies

In this section, we apply our framework to verify the correctness of four practical quantum programs and demonstrate the correct usage of dirty qubits in the first two examples.

8 The condition is strengthened to be necessary and sufficient when 𝑆 contains only initialization, unitary transformation and measurement ( if □ 𝑚 · 𝑀 𝑃 [ 𝑞 ] → skip end ), because all qubits in 𝑞𝑏𝑖𝑡 ( 𝑆 ) are necessary for execution of program 𝑆 .

<!-- image -->

## 8.1 Programs with Dirty Ancilla Qubits: In-place Addition Circuit and MCX Gate

The first example is the one introduced in Section 2, where the circuit shown in Fig. 1 functions as an in-place constant adder computing the last bit of 𝑟 = 𝑎 + ( 011 ) 2 . The quantum circuit can be implemented in Qwhile-hp as follows:

$$\begin{array} { c c c } S & \triangle q \ a l l o c ( g _ { 0 } ; q a l l o c ( g _ { 1 } ; C N O T [ g _ { 1 } , a _ { 2 } ] ; C N O T [ a _ { 1 } , g _ { 1 } ] ; X [ a _ { 1 } ] ; T o f f o l i [ g _ { 0 } , a _ { 1 } , g _ { 1 } ] ; \\ & C N O T [ a _ { 0 } , g _ { 0 } ] ; T o f f o l i [ g _ { 0 } , a _ { 1 } , g _ { 1 } ] ; C N O T [ g _ { 1 } , a _ { 2 } ] ; T o f f o l i [ g _ { 0 } , a _ { 1 } , g _ { 1 } ] ; & ( 1 ) \\ & C N O T [ a _ { 0 } , g _ { 0 } ] ; T o f f o l i [ g _ { 0 } , a _ { 1 } , g _ { 1 } ] ; X [ a _ { 1 } ] ; C N O T [ a _ { 1 } , g _ { 1 } ] ; q f r e e ( g _ { 0 } ) ; q f r e e ( g _ { 1 } ) & \end{array}$$

The correctness specification for 𝑆 is formulated as follows:

$$\forall \bar { C } \in \{ 0 , 1 \} ^ { 3 } \colon \, \Leftrightarrow \left \{ \bar { a } \mapsto | \bar { C } \rangle \langle \bar { C } | \} \, S \left \{ \bar { a } \mapsto | f ( \bar { C } ) \rangle \langle f ( \bar { C } ) | \right \}$$

where 𝑓 ( 𝐶 0 , 𝐶 1 , 𝐶 2 ) = 𝐶 0 , 𝐶 1 , 𝐶 2 + 𝐶 1 + 𝐶 0 + 𝐶 0 𝐶 1 and ¯ 𝑎 = 𝑎 0 , 𝑎 1 , 𝑎 2 . This specification can be derived using the proof system in Fig. 9. Furthermore, the body of 𝑆 , which is the subprogram of 𝑆 without the qalloc and qfree statements (highlighted in red in Eq. (1)) at the beginning and the end, correctly uses dirty qubits 𝑔 0 and 𝑔 1 . This is established by Corollary 7.1 and the following valid triples where 𝑔 ′ 0 , 𝑔 ′ 1 ∉ ¯ 𝑎 ∪ { 𝑔 0 , 𝑔 1 } :

$$\ni \left \{ \bar { a } \mapsto I * g _ { 0 } , g _ { 0 } ^ { \prime } \mapsto | \Phi \rangle \langle \Phi | * g _ { 1 } , g _ { 1 } ^ { \prime } \mapsto | \Phi \rangle \langle \Phi | \right \} S . b o d y \left \{ g _ { 0 } , g _ { 0 } ^ { \prime } \mapsto | \Phi \rangle \langle \Phi | * g _ { 1 } , g _ { 1 } ^ { \prime } \mapsto | \Phi \rangle \langle \Phi | * \top \right \}$$

Therefore, we can confidently borrow dirty qubits 𝑔 0 and 𝑔 1 from any other part of computation when they are allocated at the beginning of 𝑆 . Their original states will be restored before they are freed at the end of 𝑆 .

Next, we verify an implementation of the Multiple-Controlled X (MCX) Gate with dirty ancilla qubits. Fig. 12 demonstrates the circuit that implements a 3-controlled X gate using 4 Toffoli gates and 1 dirty qubit. The correctness specification is represented by the triple:

$$\forall \bar { C } \in \{ 0 , 1 \} ^ { 3 } , T \in \{ 0 , 1 \} . \ \{ \bar { c } , t \mapsto | \bar { C } , T \rangle \} \ S \ \{ \bar { c } , t \mapsto | \bar { C } , T + C _ { 0 } C _ { 1 } C _ { 2 } \rangle \}$$

where ¯ 𝑐, 𝑡 ↦→ | ¯ 𝐶,𝑇 ⟩ is shorthand for ¯ 𝑐, 𝑡 ↦→ | ¯ 𝐶,𝑇 ⟩⟨ ¯ 𝐶,𝑇 | , and the program 𝑆 is shown in Fig. 13. Again, we can verify that the body of 𝑆 uses the dirty ancilla qubit 𝑎 correctly, using Corollary 7.1 and the validity of

$$\{ \bar { c } , t \mapsto I * a , a ^ { \prime } \mapsto | \Phi \rangle \langle \Phi | \} \ S . b o d y \ \{ a , a ^ { \prime } \hookrightarrow | \Phi \rangle \langle \Phi | \} \text { for } a ^ { \prime } \notin \{ c _ { 0 } , c _ { 1 } , c _ { 2 } , t , a \} .$$

<!-- image -->

## 8.2 Program with While Loop: Repeat-Until-Success Circuit

It is well known in quantum computing that any unitary gate can be approximated to arbitrary precision by composing basic gates such as single-qubit gates and the controlled NOT gate [43]. Furthermore, Jones [30], Paetznick and Svore [47] have demonstrated that this decomposition can be implemented non-deterministically, potentially reducing the number of required quantum operations.

Fig. 14 (cf. Figure 1(b) in [47]) shows the repeat-until-success circuit that probabilistically implements a unitary gate 𝑉 3 ≜ 𝐼 + 2 𝑖𝑍 √ 5 on | 𝜓 ⟩ using three ancilla qubits. Each measurement in the circuit is performed in the Pauli 𝑋 basis; that is, 𝑀 𝑃 = { 𝑃 0 ≜ |+⟩⟨+| , 𝑃 1 ≜ |-⟩⟨-|} . The controlled𝑍 gate, enclosed by dashed lines, is classically controlled by the measurement on 𝑞 3 ; specifically, it is only executed when the measurement yields 1. To implement 𝑉 3 , we simply need to repeat the execution of the circuit until the measurement results of the top two ancilla qubits are 0. The probability of this happening in each execution is 5 / 8. If other measurement results are obtained, the state of the target qubit 𝑞 remains unchanged. This repeat-until-success approach significantly reduces the expected number of basic quantum gates compared to a deterministic decomposition circuit for 𝑉 3 .

Fig. 15 illustrates the implementation of this circuit in our Qwhile-hp language, along with an inline correctness specification, where 𝑀 𝑃, 1 = { 𝑃 0 ≜ | + +⟩⟨+ + | , 𝑃 1 ≜ 𝐼 - | + +⟩⟨+ + |} and 𝑀 𝑃, 2 = { 𝑃 ′ 0 ≜ |+⟩⟨+| , 𝑃 ′ 1 ≜ |-⟩⟨-|} . Note that we dynamically allocate and free 𝑞 3 in each loop iteration, allowing other programs running in parallel to access 𝑞 3 between iterations, thereby saving quantum resources. However, 𝑞 1 and 𝑞 2 cannot be allocated and freed in the same manner due to their involvement in the loop's termination condition.

The correctness specification for the program, denoted 𝑆 , is represented by the triple { 𝑞 ↦→| 𝜆 ⟩} 𝑆 { 𝑞 ↦→ 𝑉 3 | 𝜆 ⟩} where, for brevity, we use 𝑞 ↦→ | 𝜆 ⟩ to denote 𝑞 ↦→ | 𝜆 ⟩⟨ 𝜆 | . The loop invariant in this case is 𝜑 ≜ 𝑞 1 , 𝑞 2 , 𝑞 ↦→ 𝐼 ⊗ | 𝜆 ⟩⟨ 𝜆 | , as shown at the beginning of the loop body.

## 8.3 Program with Recursion: Quantum Recursive Fourier Sampling

In this subsection, we will slightly extend our programming language to support recursion by incorporating classical variables evaluated at meta-level to control the depth of recursion. This extension will allow for the implementation of more practical and complex programs without overhualing the core theoretical foundations.

```
Module 𝑄𝑅𝐹𝑆 ( 𝑘 ) { qalloc ( 𝑞 𝑘 ) ; [ 𝑞 𝑘 ] : = | 0 ⟩ ; 𝑋 [ 𝑞 𝑘 ] ; 𝐻 [ 𝑞 𝑘 ] ; if 𝑘 = 𝑙 then 𝐴 [ ¯ 𝑥 0 , . . . , ¯ 𝑥 𝑙 -1 , 𝑞 𝑘 ] else { qalloc ( ¯ 𝑥 𝑘 ) ; [ ¯ 𝑥 𝑘 ] : = | 0 ⟩ ; 𝐻 ⊗ 𝑛 [ ¯ 𝑥 𝑘 ] ; 𝑄𝑅𝐹𝑆 ( 𝑘 + 1 ) ; 𝐻 ⊗ 𝑛 [ ¯ 𝑥 𝑘 ] ; 𝐺 [ ¯ 𝑥 𝑘 , 𝑞 𝑘 ] ; 𝐻 ⊗ 𝑛 [ ¯ 𝑥 𝑘 ] ; 𝑄𝑅𝐹𝑆 ( 𝑘 + 1 ) ; qfree ( ¯ 𝑥 𝑘 ) } qfree ( 𝑞 𝑘 ) ; } Fig. 16. Quantum recursive Fourier sampling { 𝜓 ( 𝑙, 𝑏 ) } = n ¯ 𝑥 0 , . . . , ¯ 𝑥 𝑙 -1 ↦→ ˝ 2 𝑙𝑛 -1 𝑖 = 0 (-1 ) 𝑏𝑖 | 𝑖 ⟩ o 𝑄𝑅𝐹𝑆 ( 𝑙 ) = qalloc ( 𝑞 𝑙 ) ; [ 𝑞 𝑙 ] : = | 0 ⟩ ; 𝑋 [ 𝑞 𝑙 ] ; 𝐻 [ 𝑞 𝑙 ] ; 𝐴 [ ¯ 𝑥 0 , . . . , ¯ 𝑥 𝑙 -1 , 𝑞 𝑙 ] ; qfree ( 𝑞 𝑙 ) { 𝜑 ( 𝑙, 𝑏 ) } = n ¯ 𝑥 0 , . . . , ¯ 𝑥 𝑙 -1 ↦→ ˝ 2 𝑙𝑛 -1 𝑖 = 0 (-1 ) 𝑔 ( 𝑠 𝑖 ) (-1 ) 𝑏𝑖 | 𝑖 ⟩ o { 𝜓 ( 𝑘,𝑏 ) } = n ¯ 𝑥 0 , . . . , ¯ 𝑥 𝑘 -1 ↦→ ˝ 2 𝑘𝑛 -1 𝑖 = 0 (-1 ) 𝑏𝑖 | 𝑖 ⟩ o 𝑄𝑅𝐹𝑆 ( 𝑘 ) = qalloc ( 𝑞 𝑘 ) ; [ 𝑞 𝑘 ] : = | 0 ⟩ ; 𝑋 [ 𝑞 𝑘 ] ; 𝐻 [ 𝑞 𝑘 ] ; qalloc ( ¯ 𝑥 𝑘 ) ; [ ¯ 𝑥 𝑘 ] : = | 0 ⟩ ; 𝐻 ⊗ 𝑛 [ ¯ 𝑥 𝑘 ] ; { 𝜓 ( 𝑘 + 1 , 𝑏 ′ ) ∗ 𝑞 𝑘 ↦→ |-⟩} 𝑄𝑅𝐹𝑆 ( 𝑘 + 1 ) ; { 𝜑 ( 𝑘 + 1 , 𝑏 ′ ) ∗ 𝑞 𝑘 ↦→ |-⟩} 𝐻 ⊗ 𝑛 [ ¯ 𝑥 𝑘 ] ; 𝐺 [ ¯ 𝑥 𝑘 , 𝑞 𝑘 ] ; 𝐻 ⊗ 𝑛 [ ¯ 𝑥 𝑘 ] ; { 𝜓 ( 𝑘 + 1 , 𝑐 ) ∗ 𝑞 𝑘 ↦→ |-⟩} 𝑄𝑅𝐹𝑆 ( 𝑘 + 1 ) ; { 𝜑 ( 𝑘 + 1 , 𝑐 ) ∗ 𝑞 𝑘 ↦→ |-⟩} = ⇒ { 𝜑 ( 𝑘,𝑏 ) ∗ ¯ 𝑥 𝑘 ↦→ 𝐼 ∗ 𝑞 𝑘 ↦→ |-⟩} qfree ( ¯ 𝑥 𝑘 ) ; qfree ( 𝑞 𝑘 ) { 𝜑 ( 𝑘,𝑏 ) } = n ¯ 𝑥 0 , . . . , ¯ 𝑥 𝑙 -1 ↦→ ˝ 2 𝑘𝑛 -1 𝑖 = 0 (-1 ) 𝑔 ( 𝑠 𝑖 ) (-1 ) 𝑏𝑖 | 𝑖 ⟩ o where 𝑏 ′ 𝑖 ≜ 𝑏 fi rst 𝑘𝑛 bits of 𝑖 , and 𝑐 𝑥,𝑦 ≜ 𝑠 𝑥 · 𝑦 ⊕ 𝑏 𝑥 ⊕ 𝑔 ( 𝑠 𝑥 ) for 𝑥 ∈ { 0 , 1 } 𝑘𝑛 , 𝑦 ∈ { 0 , 1 } 𝑛 . Fig. 17. Inline correctness specifications
```

Recursive Fourier sampling (RFS) [41] is a widely discussed topic in complexity theory. It serves as a natural example for a modular recursive quantum program. Consider a complete 2 𝑛 -ary tree with 𝑙 -layers, meaning that each node (except the leaves) has 2 𝑛 children labeled with a string in { 0 , 1 } 𝑛 . Without loss of generality, a 𝑘 -layer node in the tree can be represented by an 𝑛 · 𝑘 binary string ( 𝑥 1 , 𝑥 2 , . . . , 𝑥 𝑘 ) , which records the path from the root to the node. Now assume that for each node, there is a secret string 𝑠 ( 𝑥 1 ,...,𝑥 𝑘 ) ∈ { 0 , 1 } 𝑛 for 𝑘 = 1 , . . . , 𝑙 , and 𝑠 ∅ for the root. We cannot access the secret strings directly, but there is an efficiently computable function 𝑔 : { 0 , 1 } 𝑛 →{ 0 , 1 } such that for any node ( 𝑥 1 , . . . , 𝑥 𝑘 ) in the tree, 𝑔 ( 𝑠 𝑥 1 ,...,𝑥 𝑘 ) = 𝑠 𝑥 1 ,...,𝑥 𝑘 -1 · 𝑥 𝑘 , where the inner product is taken modulo 2, and 𝑠 𝑥 1 ,...,𝑥 𝑘 = 1 = 𝑠 ∅ if 𝑘 = 1. Now, given an oracle 𝐴 : { 0 , 1 } 𝑛 · 𝑙 →{ 0 , 1 } computing within the leaves:

$$A ( x _ { 1 } , \dots , x _ { l } ) = g ( s _ { x _ { 1 } , \dots , x _ { l } } ) ,$$

we need to compute 𝑔 ( 𝑠 ∅ ) ∈ { 0 , 1 } .

The recursive nature of the RFS problem is evident: each subtree rooted at any node shares the same properties as the entire tree. Hence, each subtree defines an RFS problem that can be recursively solved, with the trivial case being the subtree rooted in a leaf where the oracle directly provides the solution. Let the quantum unitary oracle associated with the RFS problem be given as:

$$G | s \rangle | y \rangle = | s \rangle | y \oplus g ( s ) \rangle \quad A | x _ { 1 } , x _ { 2 } , \dots , x _ { l } \rangle | y \rangle = | x _ { 1 } , \dots , x _ { l } \rangle | y \oplus g ( s _ { x _ { 1 } , \dots , x _ { l } } ) \rangle$$

We can implement the recursive quantum Fourier sampling algorithm as shown in Fig. 16, where 𝑘 is a classical variable recording the depth of recursion, and ¯ 𝑥 𝑘 = 𝑥 ( 1 ) 𝑘 , 𝑥 ( 2 ) 𝑘 , . . . , 𝑥 ( 𝑛 ) 𝑘 . We use qalloc ( ¯ 𝑥 𝑘 ) as the shorthand for qalloc 𝑥 ( 1 ) 𝑘 ; . . . ; qalloc 𝑥 ( 𝑛 ) 𝑘 . When executing statements containing the classical variable 𝑘 , we assume that 𝑘 is evaluated at the meta level and treated as a constant number in Qwhile-hp . Because 𝑘 only increases monotonically with depth of recursion, the correctness specification of such a program segment can be verified by induction. Formally, we need to prove:

- (1) ∀ 𝑏 ∈ { 0 , 1 } 𝑙 · 𝑛 . ⊨ { 𝜓 ( 𝑙, 𝑏 )} 𝑄𝑅𝐹𝑆 ( 𝑙 ) { 𝜑 ( 𝑙, 𝑏 )} ;
- (2) taking ∀ 𝑏 ∈ { 0 , 1 } ( 𝑘 + 1 ) 𝑛 . ⊨ { 𝜓 ( 𝑘 + 1 , 𝑏 )} 𝑄𝑅𝐹𝑆 ( 𝑘 + 1 ) { 𝜑 ( 𝑘 + 1 , 𝑏 )} as a hypothesis, prove that ∀ 𝑏 ∈ { 0 , 1 } 𝑘 · 𝑛 . ⊨ { 𝜓 ( 𝑘,𝑏 )} 𝑄𝑅𝐹𝑆 ( 𝑘 ) { 𝜑 ( 𝑘, 𝑏 )} .

Here 𝜓 ( 𝑘,𝑏 ) ≜ ¯ 𝑥 0 , . . . , ¯ 𝑥 𝑘 -1 ↦→ ˝ 2 𝑘𝑛 -1 𝑖 = 0 (-1 ) 𝑏 𝑖 | 𝑖 ⟩ , 𝜑 ( 𝑘, 𝑏 ) ≜ ¯ 𝑥 0 , . . . , ¯ 𝑥 𝑘 -1 ↦→ ˝ 2 𝑘𝑛 -1 𝑖 = 0 (-1 ) 𝑔 ( 𝑠 𝑖 ) (-1 ) 𝑏 𝑖 | 𝑖 ⟩ , and we write 𝑞 ↦→| 𝜆 ⟩ instead of 𝑞 ↦→| 𝜆 ⟩⟨ 𝜆 | to simplify the notation. The inductive proof process described above can be effectively accomplished within our logic framework. Fig. 17 shows the locally decorated correctness specifications for 𝑄𝑅𝐹𝑆 ( 𝑙 ) and 𝑄𝑅𝐹𝑆 ( 𝑘 ) , respectively.

## 9 Related Works

BI-based reasoning about quantum programs with heap manipulations is an interdisciplinary topic. This section explores relevant works in varying detail based on their relevance to our research.

Separation Logic . Ishtiaq and O'Hearn [28] and Reynolds [52] pioneered the use of BI logic as an assertion language for reasoning about heap resources. We extend their concepts of local reasoning and logical formulas to quantum programs in the current paper. Various extensions of separation logic have been explored across different resource models, including permissions [7], concurrency [9], time and auxiliary state [56], and protocols [33]. Practical applications range from automatic verification tools to interactive verification methodologies have been reviewed in [44].

Bunched Implication Logic . O'Hearn and Pym [45] introduced bunched logic as a substructural logic suitable for describing resource composition. BI logic has found applications in various contexts such as type theory [46, 53], game theory [40], and quantum computation [71]. It has also been extended to characterize probabilistic [3] and relational properties [64] of programs with heap manipulations.

Quantum Logic . Two main approaches based on different interpretation of quantum assertions have emerged. The first approach, proposed by Birkhoff and von Neumann [6], associates quantum events with projective operators which form an orthomodular lattice. This approach has been further developed using categorical and algebraic methods [1, 48, 65], and reformulated as orthologic whose proof theory and algorithms have been well-studied [22, 23, 51]. The second approach associates quantum events with physical observables [66], which generalize projective operators to describe probabilistic properties and retain algebraic structure known as effect algebra [21, 29, 32].

Formal Verification of Quantum Programs . As reviewed in [12], software engineering methods have been adapted for quantum computing, including model checking [69], testing and debugging [26, 37], abstract interpretation [70], ZX calculus for quantum circuit [15, 31] and various automatic/interactive verifiers [4, 11, 35, 38]. Predicate transformers for quantum computation were introduced by D'hondt and Panangaden [17]. Based on it, Ying [66] established quantum Hoare logic. Since then, quantum Hoare logic have been refined and adapted for various practical utilities [36], including incorporation of projection-based assertions [60, 61, 72].

Dirty Qubits . Häner et al. [27] highlighted the potential of dirty qubits in reducing the size of quantum circuits and conserving resources. Subsequent studies have explored their applications in various applications such as factoring [27], unitary synthesis [39], and error correction [10]. In the realm of programming language, ReQwire [50] noted that uncomputing dirty ancilla qubits requires substantial additional machinery but offers significant gains in expressiveness. Moreover, languages like Q# [58] already facilitate the borrowing of dirty qubits.

## 10 Conclusions and Future Works

The contributions of this paper are three-fold. Firstly, we propose a quantum programming language with heap manipulations. This language supports a nondeterministic and dirty pattern for qubit allocation, where newly allocated qubits are not assumed to be in the ground state. A formal semantics of the language is defined. Secondly, building upon Birkhoff-von Neumann quantum logic, we introduce a quantum-adapted BI-style logic tailored for specifying and reasoning about quantum heaps. Finally, we develop a quantum separation logic that utilizes our BI-style logic as an assertion language for the verification of quantum programs that manipulate heap resources. In this logic, the separation conjunction is interpreted using a separation-in-domain scheme to handle entangled resources effectively.

For future work, we plan to integrate classical variables and modular programming into our framework. This enhancement will significantly broaden its capabilities and applicability.

## References

- [1] Samson Abramsky and Bob Coecke. 2009. Categorical quantum mechanics. Handbook of quantum logic and quantum structures 2 (2009), 261-325.
- [2] Manuel Barbosa, Gilles Barthe, Xiong Fan, Benjamin Grégoire, Shih-Han Hung, Jonathan Katz, Pierre-Yves Strub, Xiaodi Wu, and Li Zhou. 2021. EasyPQC: Verifying Post-Quantum Cryptography. In Proceedings of the 2021 ACM SIGSAC Conference on Computer and Communications Security (Virtual Event, Republic of Korea) (CCS '21) . Association for Computing Machinery, New York, NY, USA, 2564-2586. https://doi.org/10.1145/3460120.3484567
- [3] Kevin Batz, Benjamin Lucien Kaminski, Joost-Pieter Katoen, Christoph Matheja, and Thomas Noll. 2019. Quantitative separation logic: a logic for reasoning about probabilistic pointer programs. Proc. ACM Program. Lang. 3, POPL, Article 34 (jan 2019), 29 pages. https://doi.org/10.1145/3290347
- [4] Fabian Bauer-Marquart, Stefan Leue, and Christian Schilling. 2023. symQV: Automated Symbolic Verification of Quantum Programs. In Formal Methods: 25th International Symposium, FM 2023, Lübeck, Germany, March 6-10, 2023, Proceedings (Lübeck, Germany). Springer-Verlag, Berlin, Heidelberg, 181-198. https://doi.org/10.1007/978-3-03127481-7\_12
- [5] Benjamin Bichsel, Maximilian Baader, Timon Gehr, and Martin Vechev. 2020. Silq: a high-level quantum language with safe uncomputation and intuitive semantics. In Proceedings of the 41st ACM SIGPLAN Conference on Programming Language Design and Implementation (London, UK) (PLDI 2020) . Association for Computing Machinery, New York, NY, USA, 286-300. https://doi.org/10.1145/3385412.3386007
- [6] Garrett Birkhoff and John von Neumann. 1936. The Logic of Quantum Mechanics. Annals of Mathematics 37, 4 (1936), 823-843. http://www.jstor.org/stable/1968621
- [7] Richard Bornat, Cristiano Calcagno, Peter O'Hearn, and Matthew Parkinson. 2005. Permission accounting in separation logic. SIGPLAN Not. 40, 1 (jan 2005), 259-270. https://doi.org/10.1145/1047659.1040327
- [8] Bradben and geduardo. 2024. Quantum Memory Management in Q#. https://learn.microsoft.com/en-us/azure/quantum/ user-guide/language/statements/quantummemorymanagement.
- [9] Stephen Brookes and Peter W. O'Hearn. 2016. Concurrent separation logic. ACM SIGLOG News 3, 3 (aug 2016), 47-65. https://doi.org/10.1145/2984450.2984457
- [10] Daniel Bultrini, Samson Wang, Piotr Czarnik, Max Hunter Gordon, Marco Cerezo, Patrick J Coles, and Lukasz Cincio. 2023. The battle of clean and dirty qubits in the era of partial error correction. Quantum 7 (2023), 1060. https://doi.org/10.22331/q-2023-07-13-1060
- [11] Christophe Chareton, Sébastien Bardin, François Bobot, Valentin Perrelle, and Benoît Valiron. 2021. An Automated Deductive Verification Framework for Circuit-building Quantum Programs. In Programming Languages and Systems , Nobuko Yoshida (Ed.). Springer International Publishing, Cham, 148-177. https://doi.org/10.1007/978-3-030-72019-3\_6
- [12] Christophe Chareton, Sébastien Bardin, Dong Ho Lee, Benoît Valiron, Renaud Vilmart, and Zhaowei Xu. 2023. Formal Methods for Quantum Algorithms. In Handbook of Formal Analysis and Verification in Cryptography . CRC Press, 319-422. https://cea.hal.science/cea-04479879
- [13] Maria Luisa Dalla Chiara and Roberto Giuntini. 2002. Quantum logics. Handbook of philosophical logic (2002), 129-228.
- [14] [Cirq Developers. 2023. Cirq . https://doi.org/10.5281/zenodo.8161252](https://doi.org/10.5281/zenodo.8161252)
- [15] Bob Coecke and Ross Duncan. 2008. Interacting Quantum Observables. In Automata, Languages and Programming , Luca Aceto, Ivan Damgård, Leslie Ann Goldberg, Magnús M. Halldórsson, Anna Ingólfsdóttir, and Igor Walukiewicz (Eds.). Springer Berlin Heidelberg, Berlin, Heidelberg, 298-310.
- [16] Steven A. Cuccaro, Thomas G. Draper, Samuel A. Kutin, and David Petrie Moulton. 2004. A new quantum ripple-carry addition circuit. arXiv:quant-ph/0410184 [quant-ph] https://arxiv.org/abs/quant-ph/0410184
- [17] Ellie D'hondt and Prakash Panangaden. 2006. Quantum weakest preconditions. Mathematical Structures in Computer Science 16, 3 (2006), 429-451.
- [18] Simon Robert Docherty. 2019. Bunched logics: a uniform approach . Ph. D. Dissertation. UCL (University College London). https://discovery.ucl.ac.uk/id/eprint/10073115
- [19] Thomas G. Draper. 2000. Addition on a Quantum Computer. arXiv:quant-ph/0008033 [quant-ph] https://arxiv.org/ abs/quant-ph/0008033
- [20] Yuan Feng, Li Zhou, and Yingte Xu. 2023. Refinement calculus of quantum programs with projective assertions. arXiv preprint arXiv:2311.14215 (2023).
- [21] David J Foulis and Mary K Bennett. 1994. Effect algebras and unsharp quantum logics. Foundations of physics 24, 10 (1994), 1331-1352. https://doi.org/10.1007/BF02283036
- [22] R. I. Goldblatt. 1974. Semantic Analysis of Orthologic. Journal of Philosophical Logic 3, 1/2 (1974), 19-35. http: //www.jstor.org/stable/30226082
- [23] Simon Guilloud and Viktor Kunčak. 2024. Orthologic with Axioms. Proc. ACM Program. Lang. 8, POPL, Article 39 (jan 2024), 29 pages. https://doi.org/10.1145/3632881

- [24] Kesha Hietala, Sarah Marshall, Robert Rand, and Nikhil Swamy. 2022. Q*: Implementing Quantum Separation Logic in F*. Programming Languages for Quantum Computing (PLanQC) 2022 Poster Abstract (2022).
- [25] Charles Antony Richard Hoare. 1969. An axiomatic basis for computer programming. Commun. ACM 12, 10 (1969), 576-580.
- [26] Yipeng Huang and Margaret Martonosi. 2019. Statistical assertions for validating patterns and finding bugs in quantum programs. In Proceedings of the 46th International Symposium on Computer Architecture (Phoenix, Arizona) (ISCA '19) . Association for Computing Machinery, New York, NY, USA, 541-553. https://doi.org/10.1145/3307650.3322213
- [27] Thomas Häner, Martin Roetteler, and Krysta M. Svore. 2017. Factoring using 2n+2 qubits with Toffoli based modular multiplication. arXiv:1611.07995 [quant-ph] https://arxiv.org/abs/1611.07995
- [28] Samin S. Ishtiaq and Peter W. O'Hearn. 2001. BI as an assertion language for mutable data structures. SIGPLAN Not. 36, 3 (jan 2001), 14-26. https://doi.org/10.1145/373243.375719
- [29] Bart Jacobs. 2015. New directions in categorical logic, for classical, probabilistic and quantum logic. Logical Methods in Computer Science 11 (2015).
- [30] Nathan Cody Jones. 2013. Logic synthesis for fault-tolerant quantum computers . Ph. D. Dissertation. Stanford University.
- [31] Aleks Kissinger and John van de Wetering. 2019. PyZX: Large Scale Automated Diagrammatic Reasoning. In Proceedings 16th International Conference on Quantum Physics and Logic, QPL 2019, Chapman University, Orange, CA, USA, June 10-14, 2019 (EPTCS, Vol. 318) , Bob Coecke and Matthew Leifer (Eds.). 229-241. https://doi.org/10.4204/EPTCS.318.14
- [32] Karl Kraus, Arno Böhm, John D Dollard, and WH Wootters. 1983. States, Effects, and Operations Fundamental Notions of Quantum Theory: Lectures in Mathematical Physics at the University of Texas at Austin . Springer. https: //doi.org/10.1007/3-540-12732-1
- [33] Robbert Krebbers, Ralf Jung, Aleš Bizjak, Jacques-Henri Jourdan, Derek Dreyer, and Lars Birkedal. 2017. The Essence of Higher-Order Concurrent Separation Logic. In Programming Languages and Systems: 26th European Symposium on Programming, ESOP 2017, Held as Part of the European Joint Conferences on Theory and Practice of Software, ETAPS 2017, Uppsala, Sweden, April 22-29, 2017, Proceedings (Uppsala, Sweden). Springer-Verlag, Berlin, Heidelberg, 696-723. https://doi.org/10.1007/978-3-662-54434-1\_26
- [34] Xuan-Bach Le, Shang-Wei Lin, Jun Sun, and David Sanan. 2022. A Quantum interpretation of separating conjunction for local reasoning of Quantum programs based on separation logic. Proc. ACM Program. Lang. 6, POPL, Article 36 (jan 2022), 27 pages. https://doi.org/10.1145/3498697
- [35] Adrian Lehmann, Ben Caldwell, Bhakti Shah, and Robert Rand. 2023. VyZX: Formal Verification of a Graphical Quantum Language. arXiv:2311.11571 [cs.PL] https://arxiv.org/abs/2311.11571
- [36] Marco Lewis, Sadegh Soudjani, and Paolo Zuliani. 2023. Formal Verification of Quantum Programs: Theory, Tools, and Challenges. 5, 1, Article 1 (dec 2023), 35 pages. https://doi.org/10.1145/3624483
- [37] Gushu Li, Li Zhou, Nengkun Yu, Yufei Ding, Mingsheng Ying, and Yuan Xie. 2020. Projection-based runtime assertions for testing and debugging Quantum programs. Proc. ACM Program. Lang. 4, OOPSLA, Article 150 (nov 2020), 29 pages. https://doi.org/10.1145/3428218
- [38] Liyi Li, Mingwei Zhu, Rance Cleaveland, Alexander Nicolellis, Yi Lee, Le Chang, and Xiaodi Wu. 2024. Qafny: A Quantum-Program Verifier. arXiv:2211.06411 [quant-ph] https://arxiv.org/abs/2211.06411
- [39] Guang Hao Low, Vadym Kliuchnikov, and Luke Schaeffer. 2024. Trading T gates for dirty qubits in state preparation and unitary synthesis. Quantum 8 (June 2024), 1375. https://doi.org/10.22331/q-2024-06-17-1375
- [40] Guy McCusker and David Pym. 2007. A Games Model of Bunched Implications. In Computer Science Logic , Jacques Duparc and Thomas A. Henzinger (Eds.). Springer Berlin Heidelberg, Berlin, Heidelberg, 573-588.
- [41] Matthew McKague. 2011. Interactive proofs with efficient quantum prover for recursive Fourier sampling. arXiv:1012.5699 [quant-ph] https://arxiv.org/abs/1012.5699
- [42] P. Mittelstaedt. 2014. On the Interpretation of the Lattice of Subspaces of the Hilbert Space as a Propositional Calculus. Zeitschrift Naturforschung Teil A 27 (06 2014), 1358. https://doi.org/10.1515/zna-1972-8-935
- [43] Michael A. Nielsen and Isaac L. Chuang. 2010. Quantum Computation and Quantum Information: 10th Anniversary Edition . Cambridge University Press.
- [44] Peter O'Hearn. 2019. Separation logic. Commun. ACM 62, 2 (jan 2019), 86-95. https://doi.org/10.1145/3211968
- [45] Peter W. O'Hearn and David J. Pym. 1999. The Logic of Bunched Implications. The Bulletin of Symbolic Logic 5, 2 (1999), 215-244. http://www.jstor.org/stable/421090
- [46] PETER O'HEARN. 2003. On bunched typing. Journal of Functional Programming 13, 4 (2003), 747-796. https: //doi.org/10.1017/S0956796802004495
- [47] Adam Paetznick and Krysta M. Svore. 2014. Repeat-until-success: non-deterministic decomposition of single-qubit unitaries. Quantum Info. Comput. 14, 15-16 (nov 2014), 1277-1301.
- [48] V. Pratt. 1992. Linear Logic For Generalized Quantum Mechanics. In Workshop on Physics and Computation . 166-180. https://doi.org/10.1109/PHYCMP.1992.615518

- [49] Qiskit contributors. 2023. Qiskit: An Open-source Framework for Quantum Computing. https://doi.org/10.5281/ zenodo.2573505
- [50] Robert Rand, Jennifer Paykin, Dong-Ho Lee, and Steve Zdancewic. 2019. ReQWIRE: Reasoning about Reversible Quantum Circuits. Electronic Proceedings in Theoretical Computer Science 287 (Jan. 2019), 299-312. https://doi.org/10. 4204/eptcs.287.17
- [51] J. P. Rawling and S. A. Selesnick. 2000. Orthologic and quantum logic: models and computational elements. J. ACM 47, 4 (jul 2000), 721-751. https://doi.org/10.1145/347476.347481
- [52] John C. Reynolds. 2002. Separation Logic: A Logic for Shared Mutable Data Structures. In Proceedings of the 17th Annual IEEE Symposium on Logic in Computer Science (LICS '02) . IEEE Computer Society, USA, 55-74.
- [53] Mitchell Riley. 2022. A Bunched Homotopy Type Theory for Synthetic Stable Homotopy Theory . Ph. D. Dissertation. Wesleyan University.
- [54] Usa Sasaki. 1954. Orthocomplemented Lattices Satisfying the Exchange Axiom. Journal of Science of the Hiroshima University, Series A (Mathematics, Physics, Chemistry) 17, 3 (1954), 293 - 302. https://doi.org/10.32917/hmj/1557281141
- [55] PETER SELINGER. 2004. Towards a quantum programming language. Mathematical Structures in Computer Science 14, 4 (2004), 527-586. https://doi.org/10.1017/S0960129504004256
- [56] Ilya Sergey, Aleksandar Nanevski, and Anindya Banerjee. 2015. Mechanized verification of fine-grained concurrent programs. SIGPLAN Not. 50, 6 (jun 2015), 77-87. https://doi.org/10.1145/2813885.2737964
- [57] Kartik Singhal, ROBERT Rand, and MATTHEW Amy. 2022. Beyond separation: Toward a specification language for modular reasoning about quantum programs. Programming Languages for Quantum Computing (PLanQC) 2022 Poster Abstract (2022).
- [58] Krysta Svore, Alan Geller, Matthias Troyer, John Azariah, Christopher Granade, Bettina Heim, Vadym Kliuchnikov, Mariia Mykhailova, Andres Paz, and Martin Roetteler. 2018. Q#: Enabling Scalable Quantum Computing and Development with a High-level DSL. In Proceedings of the Real World Domain Specific Languages Workshop 2018 (Vienna, Austria) (RWDSL2018) . Association for Computing Machinery, New York, NY, USA, Article 7, 10 pages. https://doi.org/10.1145/3183895.3183901
- [59] Yasuhiro Takahashi, Seiichiro Tani, and Noboru Kunihiro. 2010. Quantum addition circuits and unbounded fan-out. Quantum Info. Comput. 10, 9 (sep 2010), 872-890.
- [60] Dominique Unruh. 2019. Quantum relational Hoare logic. Proc. ACM Program. Lang. 3, POPL, Article 33 (jan 2019), 31 pages. https://doi.org/10.1145/3290346
- [61] Dominique Unruh. 2021. Quantum Hoare logic with ghost variables. In Proceedings of the 34th Annual ACM/IEEE Symposium on Logic in Computer Science (Vancouver, Canada) (LICS '19) . IEEE Press, Article 47, 13 pages.
- [62] Finn Voichick, Liyi Li, Robert Rand, and Michael Hicks. 2023. Qunity: A Unified Language for Quantum and Classical Computing. Proc. ACM Program. Lang. 7, POPL, Article 32 (jan 2023), 31 pages. https://doi.org/10.1145/3571225
- [63] Zhaowei Xu, Mingsheng Ying, and Benoît Valiron. 2021. Reasoning about Recursive Quantum Programs. arXiv:2107.11679 [cs.LO] https://arxiv.org/abs/2107.11679
- [64] Hongseok Yang. 2007. Relational separation logic. Theoretical Computer Science 375 (05 2007), 308-334. https: //doi.org/10.1016/j.tcs.2006.12.036
- [65] David N. Yetter. 1990. Quantales and (Noncommutative) Linear Logic. The Journal of Symbolic Logic 55, 1 (1990), 41-64. http://www.jstor.org/stable/2274953
- [66] Mingsheng Ying. 2012. Floyd-hoare logic for quantum programs. ACM Trans. Program. Lang. Syst. 33, 6, Article 19 (jan 2012), 49 pages. https://doi.org/10.1145/2049706.2049708
- [67] Mingsheng Ying. 2022. Birkhoff-von Neumann Quantum Logic as an Assertion Language for Quantum Programs. arXiv:2205.01959 [cs.LO] https://arxiv.org/abs/2205.01959
- [68] Mingsheng Ying. 2024. Foundations of Quantum Programming (2nd Edotion) . Morgan Kaufmann.
- [69] Mingsheng Ying and Yuan Feng. 2021. Model Checking Quantum Systems: Principles and Algorithms . Cambridge University Press, v-viii.
- [70] Nengkun Yu and Jens Palsberg. 2021. Quantum abstract interpretation. In Proceedings of the 42nd ACM SIGPLAN International Conference on Programming Language Design and Implementation (Virtual, Canada) (PLDI 2021) . Association for Computing Machinery, New York, NY, USA, 542-558. https://doi.org/10.1145/3453483.3454061
- [71] Li Zhou, Gilles Barthe, Justin Hsu, Mingsheng Ying, and Nengkun Yu. 2021. A quantum interpretation of bunched logic &amp; quantum separation logic. In Proceedings of the 36th Annual ACM/IEEE Symposium on Logic in Computer Science (Rome, Italy) (LICS '21) . Association for Computing Machinery, New York, NY, USA, Article 75, 14 pages. https://doi.org/10.1109/LICS52264.2021.9470673
- [72] Li Zhou, Nengkun Yu, and Mingsheng Ying. 2019. An applied quantum Hoare logic. In Proceedings of the 40th ACM SIGPLAN Conference on Programming Language Design and Implementation (Phoenix, AZ, USA) (PLDI 2019) . Association for Computing Machinery, New York, NY, USA, 1149-1162. https://doi.org/10.1145/3314221.3314584

## A Preliminaries

We briefly review some necessary background knowledge of quantum computation/information and BI/separation logic mentioned in main text. In Section A.1, we present notations universally used in quantum computation, and then introduce operators between quantum states in Section A.2. In Section A.3 we discuss three primitive but important quantum operations and introduce quantum logic and the Sasaki hook in Section A.4. Finally, we recall the basic ideas of BI logic and separation logic in Section A.5.

## A.1 Dirac Notations for Quantum States

For Dirac notations, we use ket to denote a vector, e.g. | 𝜓 ⟩ = 𝑎 𝑏 where 𝑎, 𝑏 ∈ C , and bra to denote

its conjugate transpose ⟨ 𝜓 | = 𝑎 ∗ 𝑏 ∗ where 𝑎 ∗ stands for the conjugate of complex number 𝑎 . For matrices, 𝐴 † denotes the conjugate transpose of 𝐴 . Different from the fact that value of one classical bit is either 0 or 1, the state of a qubit is represented with a normalized vector | 𝜓 ⟩ in 2-dimensional Hilbert space H , i.e. ⟨ 𝜓 | · | 𝜓 ⟩ = 1 where we usually ignore the symbol for matrix multiplication and simply write ⟨ 𝜓 | 𝜑 ⟩ to denote the inner product of | 𝜑 ⟩ and | 𝜓 ⟩ . | 0 ⟩ ≜ 1 0 and | 1 ⟩ ≜ 0 1 are

two typical valid states that forms a basis for the 2-dimensional Hilbert space which means that the state of one qubit has the general form | 𝜓 ⟩ = 𝛼 | 0 ⟩ + 𝛽 | 1 ⟩ such that | 𝑎 | 2 + | 𝑏 | 2 = 1, and | 0 ⟩ is often referred as ground state . Particularly, |+⟩ ≜ 1 √ 2 (| 0 ⟩ + | 1 ⟩) and |-⟩ ≜ 1 √ 2 (| 0 ⟩ - | 1 ⟩) denote two uniform superposition states.

To represent state of multi-qubits system, we use Kronecker product (a specialization of tensor product ) of vectors to combine states of each qubit. Formally speaking, suppose {| 𝑒 1 ⟩ , ..., | 𝑒 𝑛 ⟩} forms an orthonormal basis for Hilbert space H 1 and {| 𝑒 ′ 1 ⟩ , ..., | 𝑒 ′ 𝑚 ⟩} forms an orthonormal basis for H 2 , then H 1 ⊗ H 2 is the space spanned by basis {| 𝑒 𝑖 ⟩ ⊗ | 𝑒 𝑗 ⟩ ′ : 𝑖 = 1 , ..., 𝑛 ; 𝑗 = 1 , ..., 𝑚 } whose dimension is dim (H 1 ⊗ H 2 ) = dim H 1 · dim H 2 .

For example, consider two qubits whose states are | 0 ⟩ and |+⟩ respectively, then the state of this two-qubits system is computed to be | 0 ⟩ ⊗ |+⟩ = 1 √ 2 ( 1 , 1 , 0 , 0 ) † . However, not all state vectors of multi-qubits system can be factorized into a tensor product of individual qubit states due to quantum mechanics hypothesis on entanglement . Strictly speaking, the state of 𝑛 -qubits system is represented with a vector in the tensor product of 𝑛 instances of 2-dimensional Hilbert space.

For example, Bell state | Φ ⟩ ≜ 1 √ 2 (| 0 ⟩ ⊗ | 0 ⟩ + | 1 ⟩ ⊗ | 1 ⟩) is a typical two-qubits state that can not be factorized into | 𝜓 1 ⟩ ⊗ | 𝜓 2 ⟩ , which phenomena is also referred as the entanglement between systems. For short of notation, we may write | 𝜓,𝜑 ⟩ instead of | 𝜓 ⟩ ⊗ | 𝜑 ⟩ .

## A.2 Operators and Löwner Order

Given a finite-dimensional Hilbert space, we use L(H) to denote the set of linear operators (represented with matrices) on H e.g. 0 and I are two typical examples of linear operators, where the former one is zero-matrix and the latter one is identity matrix. The Löwner order between linear operators are defined as ' 𝐴 ⊑ 𝐵 △ ⇐⇒ 𝐵 -𝐴 is a positive operator', which is a partial order on L(H) . In this paper, we mainly care about two particular class of linear operators: density operators and projective operators .

Vector-representation of quantum states introduced in last section is often referred as pure states . Because of the probabilistic hypothesis on quantum measurement introduced in next section, a general description of quantum states is an ensemble of orthogonal pure states e.g. { 1 2 | 0 ⟩ , 1 2 | 1 ⟩} suggests that the state is | 0 ⟩ with probability 1 2 , and | 1 ⟩ with probability 1 2 , which is also referred as a mixed state. It's obvious that a pure state | 𝜓 ⟩ is an instance of mixed state { 1 | 𝜓 ⟩} in that the pure state indicates that the state is | 𝜓 ⟩ with probability 1.

Due to the indistinguishability between ensembles (e.g. { 1 2 | 0 ⟩ , 1 2 | 1 ⟩} and { 1 2 |-⟩ , 1 2 |+⟩} will have exactly the same behavior in arbitrary quantum operations), we encode ensembles into density operators 𝜌 ≜ ˝ 𝜆 𝑝 𝜆 | 𝜆 ⟩⟨ 𝜆 | ∈ D(H) such that 𝑝 𝜆 are real numbers and ˝ 𝜆 𝑝 𝜆 = 1, which suggests that with probability 𝑝 𝜆 the state of system is | 𝜆 ⟩ . For example, both { 1 2 | 0 ⟩ , 1 2 | 1 ⟩} and { 1 2 |-⟩ , 1 2 |+⟩} will be encoded as density operator 1 2 | 0 ⟩⟨ 0 | + 1 2 | 1 ⟩⟨ 1 | = 1 2 |+⟩⟨+| + 1 2 |-⟩⟨-| = 1 2 𝐼 . Given a density operator 𝜌 ∈ D(H 1 ⊗ H 2 ) , we use partial trace to denote the state of a subsystem of 𝜌 , i.e. 𝑡𝑟 H 2 ( 𝜌 ) ≜ ˝ 𝑒 ( 𝐼 H 1 ⊗ ⟨ 𝑒 |H 2 ) · 𝜌 · ( 𝐼 H 1 ⊗ | 𝑒 ⟩H 2 ) ∈ D(H 1 ) denotes the state of subsystem restricting 𝜌 to H 1 , where {| 𝑒 ⟩} is an othonormal basis for H 2 .

Another class of operators worth mentioning is projective operators 𝑃 = ˝ 𝜆 ∈ Λ | 𝜆 ⟩⟨ 𝜆 | ∈ P(H) and in finite-dimensional Hilbert space, each projective operator one-to-one corresponds to a linear closed subspace denoted with 𝐸 ( 𝑃 ) ≜ {| 𝜓 ⟩ ∈ H : 𝑃 | 𝜓 ⟩ = | 𝜓 ⟩} = 𝑠𝑝𝑎𝑛 {| 𝜆 ⟩ : 𝜆 ∈ Λ } And the Löwner order between projective operators simplifies into set inclusions, i.e. 𝑃 ⊑ 𝑄 ⇐⇒ 𝐸 ( 𝑃 ) ⊆ 𝐸 ( 𝑄 ) . With slight abuse of notations we may not distinguish 𝑃 and 𝐸 ( 𝑃 ) . We could notice that a projective operator inherently represents a set of states, loosely speaking, it could naturally serve as a semantic for quantum predicates i.e. | 𝜓 ⟩ satisfies 𝑃 ⇐⇒ | 𝜓 ⟩ ∈ 𝑃 .

## A.3 Basic Quantum Operations

In last section, we have introduced some basic knowledge about operators on Hilbert space. Given a linear operator (which is represented as a matrix) 𝐴 , we could consider it as a transformation between quantum states | 𝜓 ⟩ 𝐴 - → 𝐴 | 𝜓 ⟩ , if 𝐴 | 𝜓 ⟩ is still a valid quantum state which means ⟨ 𝜓 | 𝐴 † 𝐴 | 𝜓 ⟩ = 1. We say an operator 𝑈 is unitary if and only if 𝑈 † 𝑈 = 𝑈𝑈 † = 𝐼 , in other words 𝑈 preserves inner product. And transformation | 𝜓 ⟩ 𝑈 - → 𝑈 | 𝜓 ⟩ is also referred as unitary transformation. Here are some typical examples of unitary operators:

$$X \triangle q \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \quad & Z \triangle q \begin{pmatrix} 1 & 0 \\ 0 & - 1 \end{pmatrix} \quad & H \triangle q \frac { 1 } { \sqrt { 2 } } \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix} \quad & C N O T \triangle q \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}$$

«

‹

As we have mentioned that density operators are used to encode the general mixed states, the quantum operations we mainly focus on is superoperators between operators E : D(H) → D(H) . According to hypothesis in quantum mechanics, a quantum operation could always be represented as a completely positive and trace non-increasing superoperator E , which has the general form E( 𝐴 ) = ˝ 𝑘 𝐸 𝑘 𝐴𝐸 † 𝑘 such that ˝ 𝑘 𝐸 † 𝑘 𝐸 𝑘 ⊑ 𝐼 according to Kraus theorem. In this paper, we concern three quantum operations: initialization , unitary transformation and projective measurement .

+ Initialization . E 𝑖𝑛𝑖𝑡 ( 𝐴 ) ≜ ˝ 𝑛 -1 𝑖 = 0 | 0 ⟩⟨ 𝑖 | 𝐴 | 𝑖 ⟩⟨ 0 | where 𝑛 is the dimension of Hilbert space. Such a quantum operation is trace-preserving and set the state of quantum system to | 0 ⟩ forcefully. For example, consider state 𝜌 = 1 2 | 0 ⟩⟨ 0 | + 1 2 | 1 ⟩⟨ 1 | , then E 𝑖𝑛𝑖𝑡 ( 𝜌 ) = | 0 ⟩⟨ 0 | .
+ Unitary transformation . E 𝑢 ( 𝐴 ) ≜ 𝑈𝐴𝑈 † is just performing unitary transformation 𝐴 . For example, consider 𝑈 = 𝐶𝑁𝑂𝑇 and 𝜌 = 1 3 | + 0 ⟩⟨+ 0 | + 2 3 | 11 ⟩⟨ 11 | , then E 𝑢 ( 𝜌 ) = 1 3 | Φ ⟩⟨ Φ | + 2 3 | 10 ⟩⟨ 10 | . + Measurement . In this paper we only concern projective measurement, where the quantum measurement is represented with a set of projective operators 𝑀 𝑃 = { 𝑃 𝑖 : 𝑖 ∈ 𝐼 } such that ˝ 𝑖 𝑃 𝑖 = 𝐼 . When measuring 𝜌 with 𝑀 𝑃 , with probability 𝑝 𝑖 ≜ 𝑡𝑟 ( 𝑃 𝑖 𝜌 ) we would get 𝑖 (a classical number) as the result of measurement and the state collapse into 𝜌 𝑖 ≜ 𝑃 𝑖 𝜌𝑃 𝑖 𝑡𝑟 ( 𝑃 𝑖 𝜌 ) . For example, if we measure 𝜌 = |+⟩⟨+| with computational basis 𝑀 𝑃 = { 𝑃 0 = | 0 ⟩⟨ 0 | , 𝑃 1 = | 1 ⟩⟨ 1 |} , then we would randomly get result 𝑖 with post-measurement state | 𝑖 ⟩⟨ 𝑖 | with probability 1 2 for 𝑖 ∈ { 0 , 1 } respectively.

## A.4 Birkhoff-von Neumann Quantum Logic and Sasaki Hook

Birkhoff and von Neumann [1936] proposed that projections on a Hilbert space can be viewed as propositions about physical observables, where atomic propositions and logical connectives are interpreted as projections and operations between projections respectively. Formally, for a finite dimensional Hilbert space H , logical formulas are generated by following grammar:

$$\psi \colon = P \in A \text {atomic} \cong \mathcal { P } ( \mathcal { H } ) \, | \, \psi _ { 1 } \vee \psi _ { 2 } \, | \, \psi _ { 1 } \wedge \psi _ { 2 } \, | \, \neg \psi$$

And the semantics of each formula is interpreted as a projective operator on H :

$$[ P \in \text {Atomic} ] & \triangle q \quad [ [ \psi _ { 1 } \vee \psi _ { 2 } ] \triangle q \, \sup a n ( [ \psi _ { 1 } ] \cup [ \psi _ { 2 } ] ) \quad [ \psi _ { 1 } \wedge \psi _ { 2 } ] \triangle q \, [ \psi _ { 1 } ] \cap [ \psi _ { 2 } ] \quad [ \neg \psi ] \triangle q \, [ \psi ] ^ { \perp } \\ \text {where } P \cap Q \, \text {does the intersection of subspaces } P \text { and } Q \, \text { and } P ^ { \perp } \triangle q \, \{ | \psi \rangle \in \mathcal { H } \colon P \, | \psi \rangle \, = \, | \psi \rangle \} \text { is}$$

where 𝑃 ∩ 𝑄 denotes the intersection of subspaces 𝑃 and 𝑄 and 𝑃 ⊥ ≜ {| 𝜓 ⟩ ∈ H : 𝑃 | 𝜓 ⟩ = | 𝜓 ⟩} is the orthogonal complement space of 𝑃 , 𝑠𝑝𝑎𝑛 ( 𝑃 ∪ 𝑄 ) is the spanned space of union of 𝑃, 𝑄 . All of 𝑃 ∩ 𝑄, 𝑃 ⊥ and 𝑠𝑝𝑎𝑛 ( 𝑃 ∪ 𝑄 ) are linear closed spaces that correspond to projective operators, and forms a orthomodular lattices on P(H) .

For projective operators 𝑃, 𝑄 , there are five polynomial binary operators ( → ) satisfying that 𝑃 ⊆ 𝑄 if and only if 𝑃 → 𝑄 = 𝐼 . But Chiara and Giuntini [2002] stated that none of them satisfies import-export condition i.e. 𝑃 → 𝑄 ⊆ 𝑅 ⇐⇒ 𝑃 ⊆ 𝑄 → 𝑅 , and only the Sasaki hook [Mittelstaedt 2014; Sasaki 1954] defined as 𝑃 ⇝ 𝑄 ≜ 𝑃 ⊥ ∨ ( 𝑃 ∧ 𝑄 ) satisfies weak import-export condition:

$$P \subseteq Q \hookrightarrow R \Rightarrow P \wedge Q \subseteq R \quad P \wedge Q \subseteq R \text { and } P , Q \text { are compatible } \Rightarrow P \subseteq Q \hookrightarrow R$$

where 𝑃 and 𝑄 are compatible requires 𝑃 = ( 𝑃 ∧ 𝑄 ) ∨ ( 𝑃 ∧ 𝑄 ⊥ ) . Although Sasaki hook violates some important positive laws e.g. 𝑃 ⇝ ( 𝑄 ⇝ 𝑃 ) ≠ 𝐼 , it still has great potential to reason about weakest liberal conditions of if-branches in quantum programs[Feng et al. 2023] and we view it as a quantum analogy of implication ( → ) in classical logic.

## A.5 Bunched Implication Logic and Separation Logic

Bunched Implication (BI) logic is a variety of of substructural logic proposed by O'Hearn and Pym [1999], in which separating conjunction ( ∗ ) and separating implication ( - ∗ ) are two substructural logical connectives describing resource composition. And separation logic [Ishtiaq and O'Hearn 2001; Reynolds 2002] is an extension of Hoare logic [Hoare 1969] that adopts BI logic as an assertion language to describe and prove correctness of programs with heap manipulations.

Concretely, in memory model the satisfaction ℎ ⊨ 𝜓 ∗ 𝜑 between a heap ℎ and assertion 𝜓 ∗ 𝜑 with separating conjunction indicates that the heap memory can be separated into two disjoint sub-heaps ℎ 1 , ℎ 2 such that ℎ 1 ⊨ 𝜓 and ℎ 2 ⊨ 𝜑 respectively. In other words, heap memory is treated as a composition of separated resources. And separating implication ( - ∗ ) is the adjoint connective of ( ∗ ): ℎ ⊨ 𝜓 - ∗ 𝜑 suggests that for any heap ℎ ′ such that ℎ ′ is disjoint with ℎ and ℎ ′ ⊨ 𝜓 , the composition of ℎ, ℎ ′ will satisfy 𝜑 .

This way of treating heap memory as a resource and describe them with separating assertions plays a significant role in program logic reasoning about heap manipulations. On one hand, separating conjunction and implication exactly characterize allocation and disposal of memory space in execution of programs, on the other hand, separating heap memory guarantees that any operation applied to one part of memory will not affect the other part, which is regarded as the core of local reasoning and separation logic.

## B Deferred Proofs

## B.1 Proof for Lemma 4.1

It suffices to show that for projection operators 𝑃, 𝑄, 𝑅 , 𝑃 ⊗ 𝑄 ⊆ 𝑅 if and only if 𝑄 ⊆ 𝑃 -⊗ 𝑅 .

Proof.

- ( ⇒ ) If 𝑃 ⊗ 𝑄 ⊆ 𝑅 , then for arbitrary | 𝜓 ⟩ ∈ 𝑃 and | 𝜑 ⟩ ∈ 𝑄 , it holds that ⟨ 𝜓,𝜑 | 𝑅 | 𝜓,𝜑 ⟩ = 1. By definition of 𝑃 -⊗ 𝑅 , we know that

$$P \rightarrow \mathbf O \, R = \left \{ | \phi \rangle \colon \sum _ { \lambda } \langle \lambda , \phi | \, Q \, | \lambda , \phi \rangle = \dim P \right \} \text { where } P = \sum _ { \lambda } | \lambda \rangle \langle \lambda |$$

We could prove that | 𝜑 ⟩ ∈ 𝑃 -⊗ 𝑅 because for all | 𝜆 ⟩ ∈ 𝑃 , ⟨ 𝜆, 𝜑 | 𝑄 | 𝜆, 𝜑 ⟩ = 1, thus ˝ 𝜆 ⟨ 𝜆, 𝜑 | 𝑄 | 𝜆, 𝜑 ⟩ = 1 · dim 𝑃 = dim 𝑃 .

- ( ⇐ ) Similar to ( ⇒ ), if ˝ 𝜆 ⟨ 𝜆, 𝜙 | 𝑄 | 𝜆, 𝜙 ⟩ = dim 𝑃 where 𝑃 = ˝ 𝜆 | 𝜆 ⟩⟨ 𝜆 | , then for arbitrary | 𝜆 ⟩ ∈ 𝑃 it holds that ⟨ 𝜆, 𝜙 | 𝑄 | 𝜆, 𝜙 ⟩ = 1, which means | 𝜓 ⟩⟨ 𝜓 | ⊗ 𝑃 ⊆ 𝑅 . Therefore 𝑄 ⊗ 𝑃 ⊆ 𝑅 .

□

## B.2 Proof for Lemma 4.2

Proof.

- (⇒) Sppose 𝜓 ⊨ 𝜑 , then it's trivial to check that

$$\rho \mapsto \psi \implies \lceil \rho \rceil \subseteq [ \psi ] \left ( d o m \rho \right ) \subseteq [ \varphi ] \left ( d o m \rho \right ) \implies \rho \mapsto \varphi \\ \text {pose} \, \forall o \, \rho \mapsto \psi \implies o \mapsto \varphi \text { then for arbitrary domain } d \subset _ { \varphi } \ a \text {Domain} \text { we could}$$

- (⇐) Suppose ∀ 𝜌. 𝜌 ⊨ 𝜓 = ⇒ 𝜌 ⊨ 𝜑 , then for arbitray domain 𝑑 ⊆ 𝑓 𝑖𝑛 qDomain , we could construct valid quantum heap 𝜌 ≜ 1 dim J 𝜓 K ( 𝑑 ) J 𝜓 K ( 𝑑 ) ⊨ 𝜓 , then:

$$\rho \models \psi \implies \rho \models \varphi \implies \left [ \psi \right ] ( d ) \subseteq \left [ \varphi \right ] ( d ) \\ \text {cunclude that} \, \psi \not \in \varphi$$

thus we could conclude that 𝜓 ⊨ 𝜑 .

## B.3 Proof for Proposition 4.1

Before proving Proposition 4.1, we wil firstly introduce two useful lemmas.

Lemma B.1. For two projection operators 𝑃, 𝑄 ∈ P(H) , if 𝑃 and 𝑄 are compatible, then 𝑃 ⊆ 𝑄 ⇝ 𝑃 .

Proof. Since 𝑃 and 𝑄 are compatible, then

$$\wedge Q ^ { \perp } ) \subseteq ( P \wedge Q ) \vee Q ^ { \perp } = Q ^ { \perp } = Q$$

$$P = ( P \wedge Q ) \vee ( P \wedge Q ^ { \perp } ) \subseteq ( P \wedge Q ) \vee Q ^ { \perp } = Q \hookrightarrow P \\$$

Lemma B.2. For two projective operators 𝑃, 𝑄 ∈ P(H) , if 𝑃 and 𝑄 are compatible and 𝑃 ∧ 𝑄 ⊆ 𝑅 , then 𝑃 ⊆ 𝑄 ⇝ 𝑅 .

Proof. By Lemma B.1, we know that 𝑃 ⊆ 𝑄 ⇝ 𝑃 . Then it suffices to show that 𝑄 ⇝ 𝑃 ⊆ 𝑄 ⇝ 𝑅 . Since 𝑃 ∧ 𝑄 ⊆ 𝑅 , thus 𝑃 ∧ 𝑄 ⊆ 𝑅 ∧ 𝑄 , then it holds that

$$Q \sim P = Q ^ { \perp } \vee ( Q \wedge P ) \subseteq Q ^ { \perp } \vee ( Q \wedge R ) = Q \sim R$$

therefore we could conclude that 𝑃 ⊆ 𝑄 ⇝ 𝑃 ⊆ 𝑄 ⇝ 𝑅 .

We are now ready to prove Proposition 4.1.

Proof. We prove with induction hypothesis that the premise of each rule is valid.

□

□

- ▷ Rule 0. For arbitrary 𝑑 ⊆ 𝑓 𝑖𝑛 qDomain , it holds that

$$[ \neg \neg \psi ] \, d = ( [ \neg \psi ] \, d ) ^ { \perp } = ( ( [ \psi ] \, d ) ^ { \perp } ) ^ { \perp } = [ \psi ] \, d$$

therefore ¬¬ 𝜓 ⊨ 𝜓 .

- ▷ Rule 1. Trivial.
- ▷ Rule 2. For arbitrary 𝑑 ⊆ 𝑓 𝑖𝑛 qDomain , it holds that

$$[ \psi ] \, d \subset I _ { d } = [ \top ] \, d$$

therefore 𝜓 ⊨ ⊤ .

- ▷ Rule 3. For arbitrary 𝑑 ⊆ 𝑓 𝑖𝑛 qDomain , it holds that

$$[ \perp ] \, d = 0 _ { d } \subseteq [ \psi ] \, d$$

therefore ⊥ ⊨ 𝜓 .

- ▷ Rule 4. For arbitrary 𝑑 ⊆ 𝑓 𝑖𝑛 qDomain , if J 𝜂 K 𝑑 ⊆ J 𝜓 K 𝑑 and J 𝜂 K 𝑑 ⊆ J 𝜑 K 𝑑 , then

$$[ \eta ] \, d \subseteq [ \psi ] \, d \cap [ \varphi ] \, d = [ \psi \wedge \varphi ] \, d$$

therefore 𝜂 ⊨ 𝜓 ∧ 𝜑 .

- ▷ Rule 5. For arbitrary 𝑑 ⊆ 𝑓 𝑖𝑛 qDomain , if J 𝜂 K 𝑑 ⊆ J 𝜓 1 ∧ 𝜓 2 K 𝑑 = J 𝜓 1 K 𝑑 ∩ J 𝜓 2 K 𝑑 , then

$$[ \eta ] \, d \subseteq [ \psi _ { i } ] \, d \ \text { for } i = 1 , 2$$

therefore 𝜂 ⊨ 𝜓 𝑖 .

- ▷ Rule 6. For arbitrary 𝑑 ⊆ 𝑓 𝑖𝑛 qDomain , if J 𝜑 K 𝑑 ⊆ J 𝜓 K 𝑑 , then

$$[ \eta \wedge \varphi ] \, d \subseteq [ \varphi ] \, d \subseteq [ \psi ] \, d$$

therefore 𝜂 ∧ 𝜑 ⊨ 𝜓 .

- ▷ Rule 7. For arbitrary 𝑑 ⊆ 𝑓 𝑖𝑛 qDomain , if J 𝜂 K 𝑑 ⊆ J 𝜓 K 𝑑 and J 𝜑 K 𝑑 ⊆ J 𝜓 K 𝑑 , then since J 𝜓 K 𝑑 is a linear closed subspace, it holds that

$$\mathbb { [ } \eta \vee \varphi ] { d } = s p a n \left ( \mathbb { [ } \eta ] { d \cup \left [ \varphi \right ] } { d } \right ) \subseteq \left [ \psi \right ] d \\$$

therefore 𝜂 ∨ 𝜑 ⊨ 𝜓 .

- ▷ Rule 8. For arbitrary 𝑑 ⊆ 𝑓 𝑖𝑛 qDomain , if J 𝜂 K 𝑑 ⊆ J 𝜓 𝑖 K 𝑑 , then

$$[ \eta ] \, d \subseteq [ \psi _ { i } ] \, d \subseteq s p a n \left ( [ \psi _ { 1 } ] \, d \cup [ \psi _ { 2 } ] \, d \right ) = [ \psi _ { 1 } \vee \psi _ { 2 } ] \, d \\$$

therefore 𝜂 ⊨ 𝜓 1 ∨ 𝜓 2 .

- ▷ Rule 9. If ∀ 𝑑 ⊆ 𝑓 𝑖𝑛 qDomain . J 𝜉 K 𝑑 ⊆ J 𝜑 K 𝑑 and J 𝜂 K 𝑑 ⊆ J 𝜓 K 𝑑 , then for arbitrary 𝑑 it holds that

$$[ \xi * \eta ] \, d = \Big / _ { d ^ { \prime } \subseteq d } \left [ \xi \right ] d ^ { \prime } \otimes [ \eta ] \left ( d \rangle d ^ { \prime } \right ) \subseteq \Big / _ { d ^ { \prime } \subseteq d } \left [ \varphi \right ] d ^ { \prime } \otimes [ \psi ] \left ( d \rangle d ^ { \prime } \right ) = [ \varphi * \psi ] \, d \\ = \Big / _ { d ^ { \prime } \subseteq d } \left [ \xi \right ] d = \Big / _ { d ^ { \prime } \subseteq d } \left [ \xi \right ] d ^ { \prime } \otimes [ \eta ] \left ( d \rangle d ^ { \prime } \right ) \subseteq \Big / _ { d ^ { \prime } \subseteq d } \left [ \varphi * \eta \right ] d$$

- ▷ Rule 10. For arbitrary 𝑑 ⊆ 𝑓 𝑖𝑛 qDomain , if J 𝜂 K 𝑑 ⊆ J 𝜑 ⇝ 𝜓 K 𝑑 and J 𝜂 K 𝑑 ⊆ 𝜑 , then it holds that J 𝜂 K 𝑑 ⊆ J 𝜑 ⇝ 𝜓 K 𝑑 ∩ J 𝜑 K 𝑑 = J 𝜑 K ⊥ ∨ ( J 𝜑 K 𝑑 ∧ J 𝜓 K 𝑑 ) ∩ J 𝜑 K 𝑑 = J 𝜑 K 𝑑 ∧ J 𝜓 K 𝑑 ⊆ J 𝜓 K 𝑑

therefore 𝜂 ⊨ 𝜓 .

- ▷ Rule 11. For arbitrary 𝑑 ⊆ 𝑓 𝑖𝑛 qDomain , if J 𝜂 K 𝑑 ∧ J 𝜑 K 𝑑 ⊆ J 𝜓 K 𝑑 and J 𝜑 K 𝑑 and J 𝜂 K 𝑑 are compatible, with lemma B.2 we could conclude that

$$\left [ \eta \right ] d \subseteq \left [ \varphi \right ] d ^ { \perp } \vee \left ( \left [ \varphi \right ] d \wedge \left [ \psi \right ] d \right ) = \left [ \varphi \sim \psi \right ] d \\$$

therefore 𝜂 ⊨ 𝜑 ⇝ 𝜓 .

- ▷ Rule 12. Suppose 𝜂 ∗ 𝜑 ⊨ 𝜓 , then for arbitrary disjoint 𝑑 1 , 𝑑 2 it holds that

$$\left [ \eta \right ] d _ { 1 } \otimes \left [ \varphi \right ] d _ { 2 } \subseteq \left [ \psi \right ] ( d _ { 1 } \cup d _ { 2 } ) \\ \text {point} \, d ^ { \prime } \, d _ { \ } b y \, I \, o m m o _ { 4 \, 1 }$$

Thus for arbitrary disjoint 𝑑 ′ , 𝑑 , by Lemma 4.1,

$$\left [ \eta \right ] d \subseteq \left [ \varphi \right ] d ^ { \prime } - \otimes \left [ \psi \right ] ( d ^ { \prime } \cup d ) \\ \\$$

Therefore J 𝜂 K 𝑑 ⊆ 𝑑 ′ ⊆ 𝑓 𝑖𝑛 qDomain ,𝑑 ′ ∩ 𝑑 = ∅ J 𝜑 K 𝑑 ′ -⊗ J 𝜓 K ( 𝑑 ′ ∪ 𝑑 ) = J 𝜑 - ∗ 𝜓 K 𝑑 , which means 𝜂 ⊨ 𝜑 - ∗ 𝜓 .

- ▷ Rule 13. Suppose 𝜉 ⊨ 𝜑 - ∗ 𝜓 and 𝜂 ⊨ 𝜑 , then for arbitrary disjoint 𝑑 ′ , 𝑑 , it holds that:

$$[ \xi ] \, d \subseteq [ \varphi ] \, d ^ { \prime } \, - \otimes \, [ \psi ] \, ( d ^ { \prime } \cup d ) \quad [ \eta ] \, d \subseteq [ \varphi ] \, d \\ \intertext { o f o r b i t r o r y $ d i o i n t $ d $ d $ b y $ l o m m o $ 4 $ 1 $ i t h o l d s $ t h o t $ f o r }$$

therefore for arbitrary disjoint 𝑑 1 , 𝑑 2 , by Lemma 4.1 it holds that for

$$& \left [ \xi \right ] d _ { 1 } \otimes \left [ \eta \right ] d _ { 2 } \subseteq \left [ \varphi \right ] d _ { 2 } \otimes \left ( \left [ \varphi \right ] d _ { 2 } - \otimes \left [ \psi \right ] \left ( d _ { 1 } \cup d _ { 2 } \right ) \right ) \subseteq \left [ \psi \right ] \left ( d _ { 1 } \cup d _ { 2 } \right ) \\ \intertext { t h u s f o r b i t r o r y d }$$

Thus for arbitrary 𝑑 ,

$$[ \xi * \eta ] \, d = \bigvee _ { d ^ { \prime } \subset d } [ \mathbb { Z } ] \, d ^ { \prime } \otimes [ \eta ] \, ( d \rangle d ^ { \prime } ) \subseteq [ \psi ] \, ( d ^ { \prime } \cup d \rangle d ^ { \prime } ) = [ \psi ] \, d$$

which means 𝜉 ∗ 𝜂 ⊨ 𝜓 .

- ▷ Rule 14. It's trivial that for disjoint 𝑑 1 , 𝑑 2 , 𝑑 3

$$\bigvee _ { d _ { 3 } } \left ( \bigvee _ { d _ { 1 } , d _ { 2 } } ( [ \mathbb { Q } ] ) d _ { 1 } \otimes [ \psi ] \, d _ { 2 } \right ) \otimes [ \xi ] \, d _ { 3 } = \bigvee _ { d _ { 1 } , d _ { 2 } , d _ { 3 } } [ \mathbb { Q } ] \, d _ { 1 } \otimes [ \psi ] \, d _ { 2 } \otimes [ \xi ] \, d _ { 3 } = \bigvee _ { d _ { 1 } } [ \mathbb { Q } ] \, d _ { 1 } \otimes ( \bigvee _ { d _ { 2 } , d _ { 3 } } [ \psi ] \, d _ { 2 } \otimes [ \xi ] \, d _ { 3 } )$$

therefore ( 𝜑 ∗ 𝜓 ) ∗ 𝜉 𝑑 = 𝜑 ∗ ( 𝜓 ∗ 𝜉 ) 𝑑 , which means ( 𝜑 ∗ 𝜓 ) ∗ 𝜉 ⊨ 𝜑 ∗ ( 𝜓 ∗ 𝜉 ) .

- J K J K ▷ Rule 15. Trivially obtained from commutative law of tensor product.
- ▷ Rule 16. 17. For arbitrary 𝑑 ⊆ 𝑓 𝑖𝑛 qDomain ,

$$\left [ \psi * \top ^ { * } \right ] d & = \left [ \psi \right ] d \otimes \left [ \top ^ { * } \right ] \emptyset = \left [ \psi \right ] d \\ \psi \text { and } \psi \mapsto \psi * \top ^ { * }$$

therefore 𝜓 ∗ ⊤ ∗ ⊨ 𝜓 and 𝜓 ⊨ 𝜓 ∗ ⊤ ∗ .

## B.4 Proof for Proposition 4.2

Proof.

- ▷ For arbitrary 𝑑 ⊆ 𝑓 𝑖𝑛 qDomain , it holds that:

$$\left [ \bar { q } \mapsto P * \bar { q } ^ { \prime } \mapsto Q \right ] d = \left [ \bar { q } , \bar { q } ^ { \prime } \mapsto P \otimes Q \right ] d = \begin{cases} P _ { \bar { q } } \otimes Q _ { \bar { q } ^ { \prime } } & d = \bar { q } \cup \bar { q } ^ { \prime } \\ 0 _ { d } & \text {otherwise} \end{cases}$$

- ▷ For arbitrary 𝑑 ⊆ 𝑓 𝑖𝑛 qDomain , it holds that:

$$[ \bar { q } \mapsto P ] \, d = \begin{cases} P _ { d } & d = \bar { q } \\ 0 _ { d } & \text {otherwise} \end{cases} \subseteq \begin{cases} Q _ { d } & d = \bar { q } \\ 0 _ { d } & \text {otherwise} \end{cases} = [ \bar { q } \mapsto Q ] \, d$$

▷

Trivially obtained because semantics for

∧

,

- ▷ For arbitrary 𝑑 ⊆ 𝑓 𝑖𝑛 qDomain , it holds that:

$$\mathbb { [ } \bar { q } \mapsto P \wedge \bar { q } \hookrightarrow Q ] \, d = \begin{cases} P _ { d } \wedge Q _ { d } & d = \bar { q } \\ 0 _ { d } & \text {otherwise} \end{cases} = \mathbb { [ } \bar { q } \mapsto P \wedge Q ] \, d$$

∨

are pointwisely defined, and

0

⊲⊳

0

=

0

.

□

▷ For arbitrary 𝑑 ⊆ 𝑓 𝑖𝑛 qDomain , it holds that:

$$\mathbb { [ } \bar { q } \mapsto P \vee \bar { q } \hookrightarrow Q \mathbb { ] } \, d = \begin{cases} P _ { d } \vee Q _ { d } & d = \bar { q } \\ I _ { d } & \text {otherwise} \end{cases} = \mathbb { [ } \bar { q } \hookrightarrow P \vee Q \mathbb { ] } \, d$$

- ▷ Trivially obtained because semantics for ∧ , ∨ are pointwisely defined, and 𝐼 ⊲⊳ 𝐼 = 𝐼 .

## B.5 Proof for Theorem 6.1

Before stepping into the proof for soundness and relative completeness of proof system, we would firstly formalize our intuition about finite properties of assertion semantics which is generated by grammar defined in Figure 4b.

## B.5.1 Finite Properties of Assertion Semantics.

Lemma B.3 (Trivial Renaming). Given an assertion 𝜓 generated by grammar defined in Figure 4b. For arbitrary 𝑞, 𝑞 ′ ∈ qDomain \ 𝑞𝑏𝑖𝑡 ( 𝜓 ) and domain 𝑑 ⊆ 𝑓 𝑖𝑛 qDomain such that 𝑞, 𝑞 ′ ∉ 𝑑 , then

$$\left [ \psi \right ] ( d \cup \{ q \} ) = \left [ \psi \right ] ( d \cup \{ q ^ { \prime } \} ) [ q ^ { \prime } \Rightarrow q ]$$

Proof. Trivial.

□

Lemma B.3 suggests that name of qubits out of 𝑞𝑏𝑖𝑡 ( 𝜓 ) plays a trivial role in semantics of 𝜓 , and we could rename it to any other 𝑞 ′ ∉ 𝑞𝑏𝑖𝑡 ( 𝜓 ) . For example, consider 𝜓 ≜ 𝑞 ↩ → 𝐼 , then we know that

$$\left [ \psi \right ] \left \{ q , q _ { 1 } \right \} = I _ { q , q _ { 1 } } = \left [ \psi \right ] \left \{ q , q _ { 2 } \right \} \left [ q _ { 2 } \Rightarrow q _ { 1 } \right ] = \left [ \psi \right ] \left \{ q , q _ { 3 } \right \} \left [ q _ { 3 } \Rightarrow q _ { 1 } \right ] = \dots \\ \\ \left ( \psi \right ) = \left ( \psi , q _ { 1 } \right ) = \left ( \psi , q _ { 1 } \right ) = \left [ \psi , q _ { 2 } \right ] \left [ q _ { 2 } \Rightarrow q _ { 1 } \right ] = \dots \\$$

From now on, we no longer care about the name of 𝑞 ∉ 𝑞𝑏𝑖𝑡 ( 𝜓 ) , instead we care about the number of them. Without loss of generality, for 𝑑 ⊆ 𝑞𝑏𝑖𝑡 ( 𝜓 ) we use 𝑑 ∪ 𝑛 to denote the union of 𝑑 and arbitrary 𝑛 qubits out of 𝑞𝑏𝑖𝑡 ( 𝜓 ) . For example, 𝑑 ∪ 1 could be 𝑑 ∪ { 𝑞 } for arbitrary 𝑞 ∉ 𝑞𝑏𝑖𝑡 ( 𝜓 ) , and we know that all 𝑑 ∪ { 𝑞 } have same behavior by Lemma B.3.

Lemma B.4 (Assertion is Meaningful in Finite Domain). Consider an arbitrary assertion 𝜓 and domain 𝑑 ⊆ 𝑞𝑏𝑖𝑡 ( 𝜓 ) . There exists a threshold 𝑁 ( 𝜓 ) such that:

$$\forall n \geq N ( \psi ) . \, \left [ \psi \right ] ( d \cup n ) = \left [ \psi \right ] ( d \cup N ( \psi ) ) \otimes I _ { n - N ( \psi ) } \\ \\ 1 \, \cdot \, 1 \, \cdot \, 1 \, + \, \dots \, + \, 1 \, \cdot \, 1 \, + \, \dots \, + \, 1 \, + \, \dots \, + \, 1 \, + \, \dots \, + \, 1 \, + \, \dots \, + \, 1$$

Proof. We prove by induction on the structure of 𝜓 . Notice that 𝑁 ( 𝜓 ) given in the following proof is not optimal, but a only a valid one. There may be smaller 𝑁 ( 𝜓 ) if we know more about structure of 𝜓 .

- ▷ When 𝜓 = 𝑞 ↦→ 𝑃 , 𝑁 ( 𝜓 ) = 1.
- ▷ When 𝜓 = ¬ 𝜓 1 , 𝑁 ( 𝜓 ) = 𝑁 ( 𝜓 1 ) .

$$\triangleright \text {When } \psi = \psi _ { 1 } \wedge \psi _ { 2 } , N ( \psi ) = \max ( N ( \psi _ { 1 } ) , N ( \psi _ { 2 } ) ) .$$

▷ When 𝜓 = 𝜓 1 ∨ 𝜓 2 , 𝑁 = 𝑚𝑎𝑥 ( 𝑁 ( 𝜓 1 ) , 𝑁 ( 𝜓 2 )) .

$$\triangleright \text {When } \psi = \psi _ { 1 } * \psi _ { 2 } , N ( \psi ) = N ( \psi _ { 1 } ) + N ( \psi _ { 2 } ) . \text { We know that}$$

$$\left [ \psi _ { 1 } * \psi _ { 2 } \right ] ( d \cup n ) & = \bigvee _ { d _ { 1 } \cup d _ { 2 } = d } ^ { d _ { 1 } \cap d _ { 2 } = \emptyset } \bigvee _ { n _ { 1 } + n _ { 2 } = n } \left [ \psi _ { 1 } \right ] ( d _ { 1 } \cup n _ { 1 } ) \otimes \left [ \psi _ { 2 } \right ] ( d _ { 2 } \cup n _ { 2 } ) \\$$

Because 𝑛 1 + 𝑛 2 ≥ 𝑁 ( 𝜓 1 ) + 𝑁 ( 𝜓 2 ) , we know that

- If 𝑛 1 &lt; 𝑁 ( 𝜓 1 ) , then 𝑛 -𝑛 2 &lt; 𝑁 ( 𝜓 1 ∗ 𝜓 2 ) -𝑁 ( 𝜓 2 ) , thus 𝑛 2 -𝑁 ( 𝜓 2 ) &gt; 𝑛 -𝑁 ( 𝜓 1 ∗ 𝜓 2 ) .
- If 𝑛 2 &lt; 𝑁 ( 𝜓 2 ) , then 𝑛 1 -𝑁 ( 𝜓 1 ) &gt; 𝑛 -𝑁 ( 𝜓 1 ∗ 𝜓 2 ) .
- If 𝑛 1 ≥ 𝑁 ( 𝜓 1 ) and 𝑛 2 ≥ 𝑁 ( 𝜓 2 ) , then ( 𝑛 1 -𝑁 ( 𝜓 1 )) + ( 𝑛 2 -𝑁 ( 𝜓 2 )) = 𝑛 -𝑁 ( 𝜓 1 ∗ 𝜓 2 ) .

□

## Therefore

where

$$n _ { 1 } ^ { \prime } = \begin{cases} n _ { 1 } & n _ { 1 } < N ( \psi _ { 1 } ) \\ n _ { 1 } - ( n - N ( \psi _ { 1 } * \psi _ { 2 } ) ) & n _ { 2 } < N ( \psi _ { 2 } ) \\ N ( \psi _ { 1 } ) & \text {otherwise} \end{cases} \quad n _ { 2 } ^ { \prime } = \begin{cases} n _ { 2 } & n _ { 2 } < N ( \psi _ { 2 } ) \\ n _ { 2 } - ( n - N ( \psi _ { 1 } * \psi _ { 2 } ) ) & n _ { 1 } < N ( \psi _ { 1 } ) \\ N ( \psi _ { 2 } ) & \text {otherwise} \end{cases}$$

 Thus we conclude that

$$\left [ \psi _ { 1 } \right ] \left ( d _ { 1 } \cup n _ { 1 } \right ) \otimes \left [ \psi _ { 2 } \right ] \left ( d _ { 2 } \cup n _ { 2 } \right ) = I _ { n - N ( \psi _ { 1 } * \psi _ { 2 } ) } \otimes \left [ \psi _ { 1 } \right ] \left ( d _ { 1 } \cup n _ { 1 } ^ { \prime } \right ) \otimes \left [ \psi _ { 2 } \right ] \left ( d _ { 2 } \cup n _ { 2 } ^ { \prime } \right ) \\ \text {where}$$



$$\text {In} \, \substack { \text {I} _ { 1 } \ast \psi _ { 2 } \right ] ( d \cup n ) & = I _ { n - N ( \psi _ { 1 } \ast \psi _ { 2 } ) } \otimes \bigvee _ { d _ { 1 } \cup d _ { 2 } = d } ^ { d _ { 1 } \cap d _ { 2 } = 0 } \Big / _ { n _ { 1 } ^ { + } + n _ { 2 } ^ { \prime } = N ( \psi _ { 1 } \ast \psi _ { 2 } ) } \left [ \psi _ { 1 } \right ] ( d _ { 1 } \cup n _ { 1 } ^ { \prime } ) \otimes \left [ \psi _ { 2 } \right ] ( d _ { 2 } \cup n _ { 2 } ^ { \prime } ) \\ & = I _ { n - N ( \psi _ { 1 } \ast \psi _ { 2 } ) } \otimes \left [ \psi _ { 1 } \ast \psi _ { 2 } \right ] ( d \cup N ( \psi _ { 1 } \ast \psi _ { 2 } ) ) \\ \triangleright \text {When} \, \psi & = \psi _ { 1 } \ast \psi _ { 2 } , N ( \psi ) = N ( \psi _ { 2 } ) . \text { We know that}$$

▷ When 𝜓 = 𝜓 1 - ∗ 𝜓 2 , 𝑁 ( 𝜓 ) = 𝑁 ( 𝜓 2 ) . We know that

$$\mathbb { P } \left ( \psi _ { 1 } = \psi _ { 1 } \right ) & = \gamma _ { 1 } ^ { 1 } * \gamma _ { 2 } , \mathbb { N } ( \psi _ { 2 } ) = \mathbb { N } ( \gamma _ { 2 } ) ; \intertext { [ [ \psi _ { 1 } + \psi _ { 2 } ] ] } [ [ \psi _ { 1 } = \psi _ { 2 } ] ] & \left ( d \cup n \right ) = \bigwedge _ { d ^ { \prime } \leq q b i t ( \psi _ { 1 } \neq \psi _ { 2 } ) , d \cap 0 = \bigwedge _ { n ^ { \prime } } [ \psi _ { 1 } ] } \left ( d ^ { \prime } \cup n ^ { \prime } \right ) - \otimes \left [ [ \psi _ { 2 } ] \right ] \left ( d ^ { \prime } \cup d \cup n + n ^ { \prime } \right ) \\ & = I _ { n - N ( \psi _ { 2 } ) } \otimes \bigwedge _ { d ^ { \prime } \leq q b i t ( \psi _ { 1 } \neq \psi _ { 2 } ) , d \cap 0 = 0 } \bigwedge _ { n ^ { \prime } } [ \psi _ { 1 } ] \left ( d ^ { \prime } \cup n ^ { \prime } \right ) - \otimes \left [ [ \psi _ { 2 } ] \right ] \left ( d ^ { \prime } \cup d \cup N ( \psi _ { 2 } ) + n ^ { \prime } \right ) \\ & = I _ { n - N ( \psi _ { 1 } - \psi _ { 2 } ) } \otimes \left [ [ \psi _ { 1 } - \psi _ { 2 } ] \right ] \left ( d \cup N ( \psi _ { 1 } \neq \psi _ { 2 } ) \right ) \\ & \quad \Box$$

□

LemmaB.5 (Finite Judgement of Entailment). For assertions 𝜓,𝜑 generated by grammar defined in Figure 4b, there exists a finite domain 𝐷 ⊆ 𝑓 𝑖𝑛 qDomain such that

$$\psi \models \varphi \iff \forall d \subseteq D . \, \mathbb { [ } \psi ] \left ( d \right ) \subseteq \mathbb { [ } \varphi \right ] \left ( d \right ) \\$$

Proof. Let 𝐷 = 𝑞𝑏𝑖𝑡 ( 𝜓 ) ∪ 𝑞𝑏𝑖𝑡 ( 𝜑 ) + 𝑚𝑎𝑥 ( 𝑁 ( 𝜓 ) , 𝑁 ( 𝜑 )) , by Lemma B.4 we know that for arbitray domain 𝑑 ′ , either 𝑑 ′ ⊆ 𝐷 or

$$\left [ \psi \right ] ( d ) = \left [ \psi \right ] ( d \cap D ) \otimes I _ { d \vee D } \quad \left [ \varphi \right ] ( d ) = \left [ \varphi \right ] ( d \cap D ) \otimes I _ { d \vee D } \\ \subset \, c \colon \ q \text {Domain } \, \mathbb { I } / \mathbb { I } \, ( d ) \subset \mathbb { I } \varphi \, \mathbb { I } \, ( d ) \text { is full determined by those } d \subset D$$

Thus ∀ 𝑑 ⊆ 𝑓 𝑖𝑛 qDomain . J 𝜓 K ( 𝑑 ) ⊆ J 𝜑 K ( 𝑑 ) is fully determinined by those 𝑑 ⊆ 𝐷 . □

Both Lemma B.4 and Lemma B.5 reflect our intuition that it's meaningless to consider infinite number of qubits when interpreting a finite assertion 𝜓 or reasoning about entailment relation.

## B.5.2 Soundness of Proof System in Figure 9.

Now we are ready to prove the soundness of proof system defined in Figure 9.

▷ Rule Skip. Trivial.

▷ Rule Qalloc. We know that

$$\rho \ni \top ^ { * } \implies \rho = 1 _ { 0 } \, \Longrightarrow \, [ q a l l o c ( q ) ] \left ( \rho \right ) = \mathcal { D } ( \mathcal { H } _ { q } ) \, \Longrightarrow \, \forall \rho ^ { \prime } \in \left [ q a l l o c ( q ) \right ] ( \rho ) . \rho ^ { \prime } \cong q \mapsto I$$

- ▷ Rule Qfree. We know that

$$& 1 _ { 0 } \longrightarrow \mathbb { I } ^ { q a l 1 0 } ( q ) \mathbb { I } ( \rho ) = \mathcal { D } ( \mathcal { I } _ { q } ) \longrightarrow \nabla \rho \in \mathbb { I } ^ { q a l 1 0 } \mathcal { C } ( q ) \mathbb { I } ( \rho ) . \rho \models \mathbb { F } \\ & \quad \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \$$

$$& \rho \mapsto q \mapsto I \implies t r _ { q } ( \rho ) = 1 _ { 0 } \implies \left [ \mathfrak { q } f r e ( q ) \right ] ( \rho ) = \{ 1 _ { 0 } \} \implies \forall \rho ^ { \prime } \in \left [ \mathfrak { q } f r e ( q ) \right ] ( \rho ) . \rho ^ { \prime } \mapsto \top ^ { * } \\ & \quad \mapsto \text {Rule InUT. We know that}$$

▷ Rule Init. We know that

$$\forall \rho \in \mathcal { D } ( \mathcal { H } _ { \overline { q } } ) . \, \sum \nolimits _ { i = 0 } ^ { 2 ^ { | \overline { q } | } - 1 } | 0 \rangle \langle i | \rho | i \rangle \langle 0 | = | 0 \rangle \langle 0 |$$

thus 𝜌 ⊨ 𝑞 ↦→ 𝐼 = ⇒ J [ 𝑞 ] : = | 0 ⟩ K ( 𝜌 ) ⊨ 𝑞 ↦→ | 0 ⟩⟨ 0 | where J [ 𝑞 ] : = | 0 ⟩ K ( 𝜌 ) contains only one element | 0 ⟩⟨ 0 | .

▷ Rule Unitary. We know that for all 𝑞 ⊆ 𝑞 ′ ,

$$\rho \mapsto \overline { q } ^ { \prime } \mapsto P \implies \rho \in \mathcal { D } ( \mathcal { H } _ { \overline { q } ^ { \prime } } ) \wedge \lceil \rho \rceil \subseteq P \implies U _ { \overline { q } } \rho U _ { \overline { q } } ^ { \dagger } \in \mathcal { D } ( \mathcal { H } _ { \overline { q } } ) \wedge \left [ U _ { \overline { q } } U _ { \overline { q } } ^ { \dagger } \right ] \subseteq U _ { \overline { q } } P U _ { \overline { q } } ^ { \dagger }$$

which means J 𝑈 [ 𝑞 ] K ( 𝜌 ) ⊨ 𝑞 ′ ↦→ 𝑈𝑃𝑈 † where J 𝑈 [ 𝑞 ] K 𝜌 contains only one element. ▷ Rule Se/q.sc\_u.scence. By operational semantics of sequential composition, we know that:

$$\left [ S _ { 1 } ; S _ { 2 } \right ] \rho = \bigcup _ { \rho ^ { \prime } \in \left [ S _ { 1 } \right ] \rho } \left [ S _ { 2 } \right ] \rho ^ { \prime } \\ \ t h o t \circledast \psi \, = \, \psi \, \ t h o \, v \, t h o \, v \, d i t y \, o f \, p r o m i s o \, w$$

Then for arbitrary 𝜌 such that 𝜌 ⊨ 𝜓 , by the validity of premise we know that ∀ 𝜌 ′ ∈ J 𝑆 1 K 𝜌. 𝜌 ′ ⊨ 𝜑 and execution of 𝑆 1 on 𝜌 will not get stuck. Then 𝜌 ′ ⊨ 𝜑 implies that execution of 𝑆 2 on 𝜌 ′ will not get stuck and ∀ 𝜌 ′′ ∈ J 𝑆 2 K 𝜌 ′ . 𝜌 ′′ ⊨ 𝜙 . Thus we could conclude that execution of 𝑆 1 ; 𝑆 2 on 𝜌 ▷ Rule Conse/q.sc\_u.scence. By Lemma 4.2 We know that

$$\rho \mapsto \psi \implies \rho \mapsto \psi ^ { \prime } \implies \text { execution of S on } \rho \text { will not get stuck, and } \forall \rho ^ { \prime } \in [ S ] \rho . \rho ^ { \prime } \mapsto \varphi ^ { \prime } \\ \text {Thus we could conclude that } \forall \rho ^ { \prime } \in \mathbb { S } | \Omega \ \rho ^ { \prime } \ \varpi \ \rho ^ { \prime } \in \mathbb { W }$$

Thus we could conclude that ∀ 𝜌 ′ ∈ J 𝑆 K 𝜌. 𝜌 ′ ⊨ 𝜑 . ▷ Rule If . For arbitrary 𝜌 ⊨ ( 𝑞 ↩ → 𝐼 ) ∧ 𝑚 ( 𝑞 ↩ → 𝑃 𝑚 ) ⇝ 𝜓 𝑚 , we know that 𝜌 ⊨ 𝑞 ↩ → 𝐼 and 𝑑𝑜𝑚 𝜌 ⊇ 𝑞 , thus the measurement will not get stuck. Besides, ∀ 𝑚. 𝜌 ⊨ ( 𝑞 ↩ → 𝑃 𝑚 ) ⇝ 𝜓 𝑚 suggests that

$$\lceil \rho \rceil \subseteq ( P _ { m } \otimes I _ { d o m \sqrt { \bar { q } } } ) ^ { \perp } \vee ( ( P _ { m } \otimes I _ { d o m \sqrt { \bar { q } } } ) \wedge [ \psi _ { m } ] ( d o m \, \rho ) ) \\ \text {measurement, if the result of measurement is } m , \text { then} \colon$$

J then after measurement, if the result of measurement is 𝑚 , then:

$$\int ( P _ { m } \otimes I _ { \bar { q } } ) \rho ( P _ { m } \otimes I _ { \bar { q } } ) ^ { \dagger } \Big ] \subseteq ( P _ { m } \otimes I _ { d o m \ \bar { q } } ) \wedge [ \psi _ { m } ] \, d o m \, \rho \subseteq [ \psi _ { m } ] \, d o m \, \rho \\ \text {us we know that the quantum heap } \varrho \text { after measuring with result } m \text { would satisfy } \psi _ { m } \text { .} \text { Then}$$

Thus we know that the quantum heap 𝜌 𝑚 after measuring with result 𝑚 would satisfy 𝜓 𝑚 . Then by the validity of premise, we know that the execution of 𝑆 𝑚 on 𝜌 𝑚 will not get stuck and the output states will all satisfy 𝜑 .

▷ Rule While. Similar to if statement, after 𝑛 rounds of execution of loop body, the quantum heap always satisfies that: (i). measurement on it will not get stuck. (ii). if the result of measurement is 0, then the quantum heap after measurement will satisfy 𝜓 . (iii). if the result of measurement is 1, then the quantum heap after measurement will satisfy 𝜑 . And since the guard condition to exit loop is the measurement results in 0, therefore after the execution of while loop the output quantum heap will satisfy 𝜓 .

▷ Rule Conjunction. Suppose ⊨ { 𝜓 1 } 𝑆 { 𝜑 1 } and ⊨ { 𝜓 2 } 𝑆 { 𝜑 2 } , then for arbitrary 𝜌 ⊨ 𝜓 1 ∧ 𝜓 2 , it holds that 𝜌 ⊨ 𝜓 1 and 𝜌 ⊨ 𝜓 2 , thus by any of the two premises we know that 𝑆 will not get stuck, and by both of them:

$$\forall \rho ^ { \prime } \in [ S ] \, \rho . \, \rho ^ { \prime } \equiv \varphi _ { 1 } \, \text {and} \, \rho ^ { \prime } \, \mathfrak { H } \, \in \varphi _ { 2 }$$

Therefore we conclude that ∀ 𝜌 ′ ∈ 𝑆 . 𝜌 ′ ⊨ 𝜑 1 ∧ 𝜑 2 .

▷ Rule Disjunction. We prove by induction on the structure of 𝑆 .

- 𝑆 = skip , abort , trivial.
- 𝑆 = qalloc ( 𝑞 ) , suppose ⊨ { 𝜓 𝑖 } qalloc ( 𝑞 ) { 𝜑 𝑖 } , we know that:

$$\left [ \varphi _ { i } \right ] ( d o m \, \rho [ q \Rightarrow \sqcup ] \cup \{ q \} ) \supset & \cong \left [ \psi _ { i } \right ] ( d o m \, \rho ) [ q \Rightarrow \sqcup ] \otimes I _ { q } \\ \text {use if not then we could choose } \rho ^ { \prime } = \rho [ q \to | \sqcup | ] \otimes \frac { 1 } { I } \in \mathbb { I } _ { \ } [ \real a ] \log ( q ) \right ] ( \rho ) \, \exists$$

because if not, then we could choose 𝜌 ′ = 𝜌 [ 𝑞 ⇒⊔] ⊗ 1 2 𝐼 ∈ J qalloc ( 𝑞 ) K ( 𝜌 ) , and 𝜌 ′ ⊨ 𝜑 𝑖 . Therefore it holds that:

$$& \left [ \varphi _ { 1 } \vee \varphi _ { 2 } \right ] ( d o m \, \rho [ q \Rightarrow \sqcup ] \cup \{ q \} ) \supseteq \left [ \psi _ { 1 } \vee \psi _ { 2 } \right ] ( d o m \, \rho ) [ q \Rightarrow \sqcup ] \otimes I _ { q } \\ \text {For arbitrary } & \circled { \theta } / \psi _ { 1 } \vee \psi _ { 2 } \text {, its expansion will satisfy } \varpi \, \otimes \varpi _ { 1 }$$

For for arbitrary 𝜌 ⊨ 𝜓 1 ∨ 𝜓 2 , its expansion will satisfy 𝜑 1 ∨ 𝜑 2 .

- 𝑆 = qfree ( 𝑞 ) , suppose premises are valid, then 𝜌 ⊨ 𝜓 1 ∨ 𝜓 2 indicates that at least one of J 𝜓 1 K 𝑑𝑜𝑚 𝜌 and J 𝜓 2 K 𝑑𝑜𝑚 𝜌 is not 0 , or in other words, is satisfiable. Then by hypothesis triple, we know that 𝑞 ∈ 𝑑𝑜𝑚 𝜌 because otherwise J 𝜓 1 K 𝑑𝑜𝑚 𝜌 and J 𝜓 2 K 𝑑𝑜𝑚 𝜌 should be both unsatisfiable. Therefore qfree ( 𝑞 ) will not get stuck.

Due to the linearity of partial trace, we know that

$$\left \lceil t r _ { q } \left ( \left [ \psi _ { 1 } \right ] d o m \, \rho \, \vee \, \left [ \psi _ { 2 } \right ] d o m \, \rho \right ) \right \rceil = \left \lceil t r _ { q } \left ( \left [ \psi _ { 1 } \right ] d o m \, \rho \right ) \right \rceil \vee \left \lceil t r _ { q } \left ( \left [ \psi _ { 2 } \right ] d o m \, \rho \right ) \right \rceil$$

J K J K

And by premises we know that

$$\left \lceil t r _ { q } \left ( \left [ \psi _ { i } \right ] \right ] d o m \, \rho \right ) \right \rceil \subseteq \left [ \varphi _ { i } \right ] \left ( d o m \, \rho \langle \{ q \} \right ) \\ \text {we will not hold. Therefore we could conclude that} \, f$$

$$\ f r e e ( q ) & | ] \, \rho , \\ & [ \rho ^ { \prime } ] = \left [ t r _ { q } ( \rho ) \right ] \\ & \subseteq \left [ t r _ { q } \left ( [ \psi _ { 1 } ] \right ) d o m \, \rho \vee [ \psi _ { 2 } ] \right ] d o m \, \rho ) | ] \\ & = \left [ t r _ { q } \left ( [ \psi _ { 1 } ] \right ) d o m \, \rho \right ) | \vee \left [ t r _ { q } \left ( [ \psi _ { 2 } ] \right ) d o m \, \rho \right ) | \\ & \subseteq [ \varphi _ { 1 } \vee \varphi _ { 2 } ] \left ( d o m \, \rho \langle q \rangle \right ) \\ s \, \rho ^ { \prime } & \, \mapsto \varphi _ { 1 } \vee \varphi _ { 2 } .$$

otherwise the triple will not hold. Therefore we could conclude that for arbitrary 𝜌 ⊨ 𝜓 1 ∨ 𝜓 2 and 𝜌 ′ ∈ J qfree ( 𝑞 ) K 𝜌 ,

which means 𝜌 ′ ⊨ 𝜑 1 ∨ 𝜑 2 .

- For the rest part, we only need to prove that for three basic quantum operations:

$$\mathcal { E } _ { i n i t } ( \rho ) = \sum _ { i = 0 } ^ { 2 ^ { | J | } - 1 } | 0 \rangle _ { \bar { q } } \langle i | \rho | i \rangle _ { \bar { q } } \langle 0 | & & \mathcal { E } _ { u } ( \rho ) = U _ { \bar { q } } \rho U _ { \bar { q } } ^ { \dagger } & & \mathcal { E } _ { m } ( \rho ) = P _ { m } \rho P _ { m } ^ { \dagger }$$

satisfy Disjunction rule, noticing that l 𝑃 𝑚 𝜌𝑃 † 𝑚 𝑡𝑟 ( 𝑃 𝑚 𝜌𝑃 † 𝑚 ) m = l 𝑃 𝑚 𝜌𝑃 † 𝑚 m if 𝑡𝑟 ( 𝑃 𝑚 𝜌𝑃 † 𝑚 ) ≠ 0. Then proofs for both if and while statements, and sequential composition of statements could be directly obtained by induction hypothesis. Besides, for ⌈ 𝜌 ⌉ ⊆ 𝑃 ∨ 𝑄 , then all possible measurement results of 𝜌 are included in the measurement results of 𝑃 and 𝑄 , which means branches of 𝜌 will also be executed for at least one of 𝑃 or 𝑄 .

For arbitrary quantum operator E( 𝐴 ) = ˝ 𝑚 𝑃 𝑚 𝐴𝑃 † 𝑚 , since it's a composition of matrix multiplication and addition, its linear property guarantees that

$$\lceil \mathcal { E } ( P \vee Q ) \rceil = \lceil \mathcal { E } ( P ) \rceil \vee \lceil \mathcal { E } ( Q ) \rceil$$

for projective operators 𝑃 and 𝑄 . And by premises we know that

$$\lceil \mathcal { E } ( [ [ \psi _ { i } ] ] \, d o m \, \rho ) \rceil \subseteq [ [ \varphi _ { i } ] ] \, d o m \, \rho \\ \text {will not hold} \, \text { therefore we conclude the}$$

otherwise the triple will not hold. Therefore we conclude that for arbitrary 𝜌 such that ⌈ 𝜌 ⌉ ⊆ J 𝜓 1 K 𝑑𝑜𝑚 𝜌 ∨ 𝜓 2 𝑑𝑜𝑚 𝜌 ,

Thus we finish the proof by E( 𝜌 ) ⊨ 𝜑 1 ∨ 𝜑 2 .

$$\text {dom } \rho \vee [ \psi _ { 2 } ] \, d o m \, \rho , \\ [ \mathcal { E } ( \rho ) ] & \subseteq [ \mathcal { E } \left ( [ \psi _ { 1 } ] \right ) d o m \, \rho \vee [ \psi _ { 2 } ] \right ] d o m \, \rho ) ] \\ & = [ \mathcal { E } ( [ \psi _ { 1 } ] \right ) d o m \, \rho ) ] \vee [ \mathcal { E } ( [ \psi _ { 2 } ] \right ) d o m \, \rho ) ] \\ & \subseteq [ \varphi _ { 1 } ] \, d o m \, \rho \vee [ \varphi _ { 2 } ] \, d o m \, \rho \\ & = [ \varphi _ { 1 } \vee \varphi _ { 2 } ] \, d o m \, \rho \\ \intertext { i s h i t h e p o f b y } \text { } & \mathcal { E } ( \rho ) \, \vDash \varphi _ { 1 } \vee \varphi _ { 2 } .$$

▷ Rule Frame. We prove by induction on the structure of 𝑆 .

- 𝑆 = skip , abort trivial.
- 𝑆 = qalloc ( 𝑞 ) . It suffices to fix disjoint domains 𝑑 1 , 𝑑 2 such that 𝑑 1 ∪ 𝑑 2 = 𝑑𝑜𝑚 𝜌 , and prove that exists disjoint domains 𝑑 ′ 1 , 𝑑 ′ 2 such that 𝑑 ′ 1 ∪ 𝑑 ′ 2 = 𝑑𝑜𝑚 𝜌 [ 𝑞 ⇒⊔] ∪ { 𝑞 } and

$$\lceil \rho \rceil \subseteq [ \psi ] { d _ { 1 } \otimes [ \phi ] } \, d _ { 2 } \, \Longrightarrow \, \lceil \rho [ q \Rightarrow \sqcup ] \otimes I _ { q } \rceil \subseteq [ \varphi ] { d _ { 1 } ^ { \prime } \otimes [ \phi ] } \, d _ { 2 } ^ { \prime } \\ \text {The disjunction of different $d_{i}$, $d_{j}$ is naturally larger than the properties of any}$$

The disjunction of different 𝑑 1 , 𝑑 2 is naturally guaranteed by linear properties of expansions of quantum heaps.

If 𝑞 ∉ 𝑑 1 ∪ 𝑑 2 , then by premise we know that J 𝜑 K ( 𝑑 1 ∪ { 𝑞 }) ⊇ J 𝜓 K 𝑑 1 ⊗ 𝐼 𝑞 , thus

$$\lceil \rho \rceil \subseteq [ \psi ] { d _ { 1 } \otimes [ \phi ] } \, d _ { 2 } \, \Longrightarrow \, \lceil \rho \otimes I _ { q } \rceil \subseteq [ \psi ] { d _ { 1 } \otimes I _ { q } \otimes [ \phi ] } \, d _ { 2 } \, \Longrightarrow \, \lceil \rho \otimes I _ { q } \rceil \subseteq [ \varphi ] { ( d _ { 1 } \cup \{ q \} ) \otimes [ \phi ] } \, d _ { 2 }$$

If 𝑞 ∈ 𝑑 1 , then we know that 𝜌 | 𝑑 1 ⊨ 𝜓 , and by premise we know that expansion of 𝜌 | 𝑑 1 [ 𝑞 ⇒ ⊔] ⊗ 𝐼 𝑞 ⊨ 𝜑 , thus

$$\lceil \rho \rceil \subseteq [ \psi ] { d _ { 1 } } \otimes [ \phi ] { d _ { 2 } } \ & \Longrightarrow \ \lceil \rho | _ { d _ { 1 } } \rceil \subseteq [ \psi ] { d _ { 1 } } \land \lceil \rho | _ { d _ { 2 } } \right \} \subseteq [ \phi ] { d _ { 2 } } \\ & \Longrightarrow \ \lceil \rho | _ { d _ { 1 } } [ q \Rightarrow \sqcup ] \otimes I _ { q } \right \} \subseteq [ \varphi ] { ( d _ { 1 } [ q \Rightarrow \sqcup ] \cup \{ q \} ) } \land \lceil \rho | _ { d _ { 2 } } \right \} \subseteq [ \phi ] { d _ { 2 } } \\ & \Longrightarrow \ \lceil \rho [ q \Rightarrow \sqcup ] \otimes I _ { q } \right \} \subseteq [ \psi ] { ( d _ { 1 } [ q \Rightarrow \sqcup ] \cup \{ q \} ) } \otimes [ \phi ] { d _ { 2 } } \\ \intertext { I f q \in d _ { 2 } , \, since q \notin q b i t ( \phi ) , \, thus by trivial renaming Lemma B . 3 we know that }$$

If 𝑞 ∈ 𝑑 2 , since 𝑞 ∉ 𝑞𝑏𝑖𝑡 ( 𝜙 ) , thus by trivial renaming Lemma B.3 we know that

$$\lceil \rho \rceil & \subseteq [ \psi ] \, d _ { 1 } \otimes [ \phi ] \, d _ { 2 } \, \Longrightarrow \, \lceil \rho [ q \Rightarrow \sqcup ] \rceil \subseteq [ \psi ] \, d _ { 1 } \otimes [ \phi ] \, ( d _ { 2 } [ q \Rightarrow \sqcup ] ) \\ & \quad \Longrightarrow \, [ \rho [ q \Rightarrow \sqcup ] \otimes I _ { q } ] \subseteq [ \varphi ] \, ( d _ { 1 } \cup \{ q \} ) \otimes [ \phi ] \, ( d _ { 2 } [ q \Rightarrow \sqcup ] ) \\ \intertext { t h e r f o r e w c o l d u c h o l p e r t h a r e l w a s e x i s d _ { \prime } \, d ^ { \prime } \, d ^ { \prime } \, s u c h t o r \, [ o [ q \Rightarrow | ] \otimes I _ { L } ] \subset }$$

- J K J K · For quantum operation E[ 𝑞 ] , similar to the last case, because of the validity of premise we know that J 𝜓 K 𝑑 1 ≠ 0 = ⇒ 𝑞 ⊆ 𝑑 1 and

therefore

Because the linear property of E( 𝐴 ) = ˝ 𝑚 𝑃 𝑚 𝜌𝑃 † 𝑚 , we know that

Therefore we could conclude that there always exists 𝑑 ′ 1 , 𝑑 ′ 2 such that 𝜌 [ 𝑞 ⇒⊔] ⊗ 𝐼 𝑞 ⊆ 𝜑 𝑑 ′ 1 ⊗ 𝜙 𝑑 ′ 2 .

$$\left \lceil \mathcal { E } _ { \overline { q } } ( [ \psi ] \, d _ { 1 } ) \right \rceil \otimes \left [ [ \phi ] \, d _ { 2 } \subseteq [ \varphi ] \, d _ { 1 } \otimes [ \phi ] \, d _ { 2 }$$

$$\lceil \rho \rceil \subseteq [ \psi ] \, d _ { 1 } \otimes [ \phi ] \, d _ { 2 } \ & \Longrightarrow \ [ \mathcal { E } _ { \overline { q } } ( \rho ) \Big ] \subseteq [ \mathcal { E } _ { \overline { q } } ( [ \psi ] \, d _ { 1 } ) ] \otimes [ \phi ] \, d _ { 2 } \\ & \Longrightarrow \ [ \mathcal { E } _ { \overline { q } } ( \rho ) \Big ] \subseteq [ \varphi ] \, d _ { 1 } \otimes [ \phi ] \, d _ { 2 } \\ \intertext { c a u s e \, the \, l e a r \, p e r y \, o f \, \mathcal { E } ( A ) = \, \Sigma \, \ P \, \rho D ^ { \dagger } _ { q } \, \ w e \, k n o w \, t h a t }$$

$$\lceil \rho \rceil \subseteq \bigvee _ { d _ { 1 } , d _ { 2 } } [ \psi ] \, d _ { 1 } \otimes [ \phi ] \, d _ { 2 } \implies \left \lceil \mathcal { E } _ { \overline { q } } ( \rho ^ { \prime } ) \right \rceil \subseteq \bigvee _ { d _ { 1 } , d _ { 2 } } [ \varphi ] \, d _ { 1 } \otimes [ \phi ] \, d _ { 2 }$$

which implies exactly that the triple holds { 𝜓 ∗ 𝜙 } E[ 𝑞 ] { 𝜑 ∗ 𝜙 } .

## B.5.3 Relative Completeness of Proof System in Figure 9.

For relative completeness of proof system, we would discuss allocation separately and introduce weakest liberal precondition for other program statements.

▷ For qfree ( 𝑞 ) , we prove that 𝑤𝑙𝑝. qfree ( 𝑞 ) .𝜓 = 𝑞 ↦→ 𝐼 ∗ 𝜓 . Firstly, let us prove the validity of { 𝑞 ↦→ 𝐼 ∗ 𝜓 } qfree ( 𝑞 ) { 𝜓 } . By sound rules Frame and Qfree, we know that

$$\vDash \{ q \mapsto I * \psi \} \, q f r e e ( q ) \, \{ \top ^ { * } * \psi \}$$

and ⊤ ∗ ∗ 𝜓 ⊨ 𝜓 , by Conse/q.sc\_u.scence rule we conclude that ⊨ { 𝑞 ↦→ 𝐼 ∗ 𝜓 } qfree ( 𝑞 ) { 𝜓 } .

Then it suffices to prove ⊨ { 𝜑 } qfree ( 𝑞 ) { 𝜓 } = ⇒ 𝜑 ⊨ 𝑞 ↦→ 𝐼 ∗ 𝜓 . We only need to consider the case when 𝑞 ∈ 𝑑 , because by validity of ⊨ { 𝜑 } qfree ( 𝑞 ) { 𝜓 } , J 𝜑 K 𝑑 = 0 𝑑 otherwise. For arbitrary 𝑞 ∈ 𝑑 ⊆ 𝑓 𝑖𝑛 qDomain , we need to prove

$$[ \varphi ] \, d \subseteq [ q \mapsto I * \psi ] \, d = [ \psi ] \, ( d \langle \{ q \} ) \otimes I _ { q } \\ \intertext { m a t o t o } \intertext { a n t o t o } \intertext { d \in } \intertext { s u p l i n } \intertext { c h o w } \intertext { s u p l i n } \intertext { d \in } \intertext { s u p l i n } \intertext { d \neq n o n \, f o r \, w i l l i t y \, o f \, t h o p \, t r i n }$$

We construct quantum state 𝜌 ≜ 1 dim J 𝜑 K 𝑑 J 𝜑 K 𝑑 , then from validity of the triple we know that

$$\ t r _ { q } ( \rho ) \models \psi \, \Longrightarrow \, \ t r _ { q } ( [ \varphi ] \, d ) \subseteq [ \psi ] \, ( d \langle \{ q \} ) \\ \subset \mathbb { I } _ { \psi } ( \mathbb { I } ) \left ( d \rangle \{ q \} \right ) \otimes I$$

J K J K ▷ For [ 𝑞 ] : = | 0 ⟩ , we prove that 𝑤𝑙𝑝. [ 𝑞 ] : = | 0 ⟩ .𝜓 = 𝑞 ↦→ 𝐼 ∗ ( 𝑞 ↦→ | 0 ⟩⟨ 0 | - ∗ 𝜓 ) . Firstly the validity of { 𝑞 ↦→ 𝐼 ∗ ( 𝑞 ↦→| 0 ⟩⟨ 0 | - ∗ 𝜓 )} [ 𝑞 ] : = | 0 ⟩ { 𝜓 } is easy to check. By sound rules Frame and Init, we know that

which implies 𝜑 𝑑 ⊆ 𝜓 ( 𝑑 \{ 𝑞 }) ⊗ 𝐼 𝑞 .

$$\vDash \left ( \bar { q } \mapsto I * ( \bar { q } \mapsto | 0 \rangle \langle 0 | + \psi ) \ \left [ \bar { q } \right ] \colon = | 0 \rangle \ \left \{ \bar { q } \mapsto | 0 \rangle \langle 0 | * ( \bar { q } \mapsto | 0 \rangle \langle 0 | + \psi ) \right \}$$

By sound rule 13 in Figure 7 we know that 𝑞 ↦→ | 0 ⟩⟨ 0 | ∗ ( 𝑞 ↦→ | 0 ⟩⟨ 0 | - ∗ 𝜓 ) ⊨ 𝜓 , thus with Conse/q.sc\_u.scence rule we could conclude that { 𝑞 ↦→ 𝐼 ∗ ( 𝑞 ↦→| 0 ⟩⟨ 0 | - ∗ 𝜓 )} [ 𝑞 ] : = | 0 ⟩ { 𝜓 } .

Then it suffices to show that ⊨ { 𝜑 } [ 𝑞 ] : = | 0 ⟩ { 𝜓 } implies 𝜑 ⊨ 𝑞 ↦→ 𝐼 ∗ ( 𝑞 ↦→| 0 ⟩⟨ 0 | - ∗ 𝜓 ) , which is equivalent to 𝑞 ↦→| 0 ⟩⟨ 0 | ∗ ( 𝑞 ↦→ 𝐼 - ∗ 𝜑 ) ⊨ 𝜓 .

For arbitrary 𝑞 ⊆ 𝑑 ⊆ 𝑓 𝑖𝑛 qDomain , notice that:

$$\left [ ( \varphi \ast \bar { q } \mapsto I ) \ast \bar { q } \mapsto | 0 \rangle \langle 0 | \right ] d = | 0 \rangle \langle 0 | _ { \bar { q } } \otimes E \left ( \frac { 1 } { 2 ^ { | \bar { q } | } } t r _ { \bar { q } } ( [ \varphi ] \, d ) \right )$$

and we construct 𝜌 ≜ 1 dim J 𝜑 K 𝑑 J 𝜑 K 𝑑 , since 𝜌 ⊨ 𝜑 , thus

$$| 0 \rangle \langle 0 | _ { \bar { q } } \otimes t r _ { \bar { q } } ( [ \varphi ] \, d ) \in [ [ \bar { q } ] \, \colon = | 0 \rangle ] \, \rho \, \Longrightarrow \, | 0 \rangle \langle 0 | _ { \bar { q } } \otimes t r _ { \bar { q } } ( [ \varphi ] \, d ) \, \mapsto \, \psi \\$$

therefore

$$\mathbb { [ } ( \varphi * \bar { q } \mapsto I ) * \bar { q } \mapsto | 0 \rangle \langle 0 | ] \, d = | 0 \rangle \langle 0 | _ { \bar { q } } \otimes E \left ( \frac { 1 } { 2 | \bar { q } | } t r _ { \bar { q } } ( [ \varphi ] \, d ) \right ) \subseteq | 0 \rangle \langle 0 | _ { \bar { q } } \otimes \left \{ t r _ { \bar { q } } ( [ \varphi ] \, d ) \right \} \subseteq [ \psi ] \, d$$

from which we conclude that ( 𝜑 - ∗ 𝑞 ↦→ 𝐼 ) ∗ 𝑞 ↦→| 0 ⟩⟨ 0 | ⊨ 𝜓 . ▷ For 𝑈 [ 𝑞 ] , we prove that 𝑤𝑙𝑝.𝑈 [ 𝑞 ] .𝜓 = 𝑞 ⊆ 𝑞 ′ ⊆ 𝑞𝑏𝑖𝑡 ( 𝜓 )+ 𝑁 ( 𝜓 )+ 1 𝑞 ′ ↦→ 𝑃 𝑞 ′ ∗ ( 𝑞 ′ ↦→ 𝑈𝑃 𝑞 ′ 𝑈 † - ∗ 𝜓 ) , where 𝑃 𝑞 ′ = 𝑈 † 𝜓 ( 𝑞 ′ ) 𝑈 .

J K To prove validity of ⊨ { 𝑤𝑙𝑝.𝑈 [ 𝑞 ] .𝜓 } 𝑈 [ 𝑞 ] { 𝜓 } , it suffices to show that

$$\Rightarrow \{ \overline { q } ^ { \prime } \mapsto P * ( \overline { q } ^ { \prime } \mapsto U P U ^ { \dagger } * \psi ) \} \, U [ \overline { q } ] \ \{ \psi \}$$

is valid for arbitrary 𝑞 ′ ⊇ 𝑞 and 𝑃 ∈ P(H 𝑞 ′ ) , then with sound rule Disjunction, we could join them together to get ⊨ { 𝑤𝑙𝑝.𝑈 [ 𝑞 ] .𝜓 } 𝑈 [ 𝑞 ] { 𝜓 } .

With rule Unitary and Frame, we know that

$$\asymp \{ \overline { q } ^ { \prime } \mapsto P * ( \overline { q } ^ { \prime } \mapsto U P U ^ { \dagger } * \psi ) \} \, U [ \overline { q } ] \ \{ \overline { q } ^ { \prime } \mapsto U P U ^ { \dagger } * ( \overline { q } ^ { \prime } \mapsto U P U ^ { \dagger } * \psi ) \}$$

Similar to the last case, we know that

$$\bar { q } ^ { \prime } \mapsto U P U ^ { \dagger } * ( \bar { q } ^ { \prime } \mapsto U P U ^ { \dagger } * \psi ) \ltimes \psi$$

Therefore with rule Conse/q.sc\_u.scence, we conclude that ⊨ 𝑞 ↦→ 𝑃 ∗ ( 𝑞 ↦→ 𝑈𝑃𝑈 † - ∗ 𝜓 ) 𝑈 [ 𝑞 ] { 𝜓 } .

Next, assuming ⊨ { 𝜑 } 𝑈 [ 𝑞 ] { 𝜓 }

′ ′ , from the validity of correctness triple, we know that:

$$\text {For $d \supseteq \bar{q}$, \quad } & [ \varphi ] \, d \subseteq U ^ { \dagger } \cdot [ \psi ] \, d \cdot U \\ \text {Otherwise} & \quad [ \varphi ] \, d = 0 \\ \text {that for $d \supseteq \bar{q} \ \mathbb{I} [ \varphi ] \, d \subset \, U ^ { \dagger } \cdot \mathbb{I} [ \psi ] \, d \colon U \subset \mathbb{I} [ w l n \, U } \\$$

Thus it suffices to show that for 𝑑 ⊇ 𝑞, J 𝜑 K 𝑑 ⊆ 𝑈 † · J 𝜓 K 𝑑 · 𝑈 ⊆ J 𝑤𝑙𝑝.𝑈 [ 𝑞 ] .𝜓 K 𝑑 . By Lemma B.5, we don't need to enumerate all possible 𝑑 , and it suffcies to enumerate 𝑑 ⊆ 𝑚𝑎𝑥 ( 𝑤𝑙𝑝.𝑈 [ 𝑞 ] .𝜓,𝜓 ) = 𝑞𝑏𝑖𝑡 ( 𝜓 ) ∪ 𝑁 ( 𝜓 ) + 1. Thus for arbitrary 𝑑 ⊆ 𝑚𝑎𝑥 ( 𝑤𝑙𝑝.𝑈 [ 𝑞 ] .𝜓,𝜓 ) = 𝑞𝑏𝑖𝑡 ( 𝜓 ) ∪ 𝑁 ( 𝜓 ) + 1,

$$U ^ { \dagger } \cdot [ \psi ] \left ( d \right ) \cdot U & = \left [ d \mapsto U ^ { \dagger } \cdot [ \psi ] \right ] d \cdot U * \left ( d \mapsto \left [ \psi \right ] d \ast \psi \right ) \right ] d \\ & \subseteq \left [ \left \langle \sqrt { q } ^ { \prime } \mapsto U ^ { \dagger } \cdot \left [ \psi \right ] d \cdot U * \left ( \overline { q } ^ { \prime } \mapsto \left [ \psi \right ] d \ast \psi \right ) \right ] d \\ & = \left [ \left \langle w l p . U [ \overline { q } ] . \psi \right ] d \\ S _ { 1 } ; S _ { 2 } , \, i t s i r v i a l t h w l p . S _ { 1 } ; S _ { 2 } . \psi & = w l p . S _ { 1 } . ( w l p . S _ { 2 } . \psi ) .$$

▷ For 𝑆 1 ; 𝑆 2 , it is trivial that 𝑤𝑙𝑝.𝑆 1 ; 𝑆 2 .𝜓 = 𝑤𝑙𝑝.𝑆 1 . ( 𝑤𝑙𝑝.𝑆 2 .𝜓 ) .

▷ For if statements, we prove that 𝑤𝑙𝑝. ( if □ 𝑚 · 𝑀 𝑃 [ 𝑞 ] → 𝑆 𝑚 fi ) .𝜓 = 𝑞 ↩ → 𝐼 ∧ 𝑚 ( 𝑞 ↩ → 𝑃 𝑚 ) ⇝ 𝑤𝑙𝑝.𝑆 𝑚 .𝜓 .

It suffices to show that for any 𝜌 such that 𝑑𝑜𝑚 𝜌 ⊇ 𝑞 ,

$$\lceil P _ { m } \rho P _ { m } \rceil \subseteq [ \lceil w l { p . S } _ { m } . \psi \rceil ] \, d o m \, \rho \iff [ \lceil \rho \rceil \subseteq [ ( \bar { q } \hookrightarrow P _ { m } ) \sim \omega \, w l { p . S } _ { m } . \psi ] \, d o m \, \rho$$

according to Schrödinger-Heisenberg duality, we know that:

$$\lceil P _ { m } \rho P _ { m } \rceil \subseteq [ \lceil w l { p . S } _ { m } . \psi \rceil ] \, d o m \, \rho \iff \lceil \rho \rceil \subseteq ( P _ { m } \cdot [ \lceil w l { p . S } _ { m } . \psi ] \, d o m \, \rho ^ { \perp } \cdot P _ { m } ) ^ { \perp } \\ \text {Thus it suffices to show that} \colon$$

Thus it suffices to show that:

$$( P Q ^ { \perp } P ) ^ { \perp } = P \sim Q$$

where 𝑃 = 𝑃 𝑚 , 𝑄 = J 𝑤𝑙𝑝.𝑆 𝑚 .𝜓 K 𝑑𝑜𝑚 𝜌 . This can be obtained from the fact that for any normalized state | 𝜂 ⟩ = | 𝜂 1 ⟩ + | 𝜂 2 ⟩ where | 𝜂 1 ⟩ ∈ 𝑃 ⊥ and | 𝜂 2 ⟩ ∈ 𝑃 ,

$$\| \text {where } | \eta _ { 1 } \rangle \in P ^ { \ } a n d \, | \eta _ { 2 } \rangle \in P , \\ | \eta \rangle \in ( P Q ^ { \perp } P ) ^ { \perp } & \iff \langle \eta | \, P Q ^ { \perp } P \, | \eta \rangle = 0 \\ & \iff \langle \eta _ { 2 } | \, Q ^ { \perp } \, | \eta _ { 2 } \rangle = 0 \\ & \iff | \eta _ { 2 } \rangle \in Q \\ & \iff | \eta \rangle \in P ^ { \perp } \vee ( P \wedge Q )$$

▷ For while statement, similar to if statement we could get that 𝑤𝑙𝑝. while 𝑀 𝑃 [ 𝑞 ] do 𝑆 end .𝜓 = 𝑛 ≥ 0 𝜑 𝑛 , where

because

$$\ n { \geq \varphi _ { n } } , \text { where } & & \quad \left ( \bar { q } \hookrightarrow I \right ) & & n = 0 \\ \varphi _ { n } \triangle q & \begin{cases} ( \bar { q } \hookrightarrow I ) & ( \bar { q } \hookrightarrow P _ { 1 } \sim \ w l p . S . \varphi _ { n - 1 } ) \wedge ( \bar { q } \hookrightarrow P _ { 0 } \sim \psi ) & n > 0 \\ ( \bar { q } \hookrightarrow I ) \wedge ( \bar { q } \hookrightarrow P _ { 1 } \sim \ w l p . S . \varphi _ { n - 1 } ) & \wedge ( \bar { q } \hookrightarrow P _ { 0 } \sim \psi ) & n > 0 \end{cases} \\ \intertext { c a u s e } & \left [ \text {while } M _ { P } [ \bar { q } ] \right ] \text { do } S \text { end} \right ] \rho = \bigcup _ { n \geq 0 } \left [ \text {while} ^ { ( n ) } \right ] \\$$

where

$$\ w h i l e ^ { ( 0 ) } \stackrel { \triangle } { = } \text {abort} \ \ w h i l e ^ { ( n ) } \stackrel { \triangle } { = } \text {if } M _ { P } [ \overline { q } ] \text { then } \ w h i l e ^ { ( n - 1 ) } \text { else skip}$$

By the weakest liberal precondition for if statement and induction we know that 𝑤𝑙𝑝.𝑤ℎ𝑖𝑙𝑒 ( 𝑛 ) .𝜓 = ( 𝑞 ↩ → 𝐼 ) ∧ ( 𝑞 ↩ → 𝑃 1 ⇝ 𝑤𝑙𝑝.𝑆.𝜑 𝑛 -1 ) ∧ ( 𝑞 ↩ → 𝑃 0 ⇝ 𝜓 ) , therefore we conclude that

$$\ w l p . ( \text {while } M _ { P } [ \bar { q } ] \, \text { do } S \, \text { end} ) . \psi = \bigwedge _ { n \geq 0 } \ w l p . w h i l e ^ { ( n ) } . \psi = \bigwedge _ { n \geq 0 } \varphi _ { n }$$

▷ For qalloc ( 𝑞 ) . We firstly prove that, if ⊨ { 𝜑 } qalloc ( 𝑞 ) { 𝜙 } , then there exists an assertion formula 𝜓 such that 𝑞 ∉ 𝑞𝑏𝑖𝑡 ( 𝜓 ) and

$$\Rightarrow \{ \varphi \} \ q a l l o c ( q ) \ \{ \phi \} \iff \Rightarrow \{ \varphi \} \ q a l l o c ( q ) \ \{ q \mapsto I * \psi \}$$

By validity of triple ⊨ { 𝜑 } qalloc ( 𝑞 ) { 𝜙 } , we know that

$$\forall d \subseteq _ { f i n } \mathbf q \text {Domain} \ s . t . \ q \notin d . \ \mathbb { [ } \phi ] ( d \cup \{ q \} ) = I _ { q } \otimes P _ { d } \text { for some } P _ { d } \\ \text {v} \text {I} e m m a \ B \ 5 i t \text { can be observed that there exists an assertion } \iota \text { such that } a \notin \mathcal { A } \text {hit} ( \iota )$$

And by Lemma B.5, it can be observed that there exists an assertion 𝜓 such that 𝑞 ∉ 𝑞𝑏𝑖𝑡 ( 𝜓 ) and

$$\forall q \notin d . \ \left [ \phi \right ] ( d \cup \{ q \} ) = \left [ q \mapsto I * \psi \right ] ( d \cup \{ q \} ) = I _ { q } \otimes \left [ \psi \right ] d \\ \text {is meaningful in finite domains} \ ( A c t u a l l y \ t h e s t r o n g e s t p o s t c o n d i t i o n \ o f ( \varpi _ { i } \ s u )$$

because 𝜙 is meaningful in finite domains. ( Actually, the strongest postcondition of 𝜑 is substituting each occurence of 𝑞 in 𝜑 with ¬⊤ ∗ which suggests non-empty. For example, if 𝜑 = 𝑞, 𝑞 1 ↦→ 𝑃 then 𝜓 = 𝑞 1 ↦→ 𝑡𝑟 𝑞 ( 𝑃 ) ∗ ¬⊤ ∗ ∗ 𝑞 ↦→ 𝐼 ) Then it suffices to show that 𝑤𝑙𝑝. qalloc ( 𝑞 ) . ( 𝑞 ↦→ 𝐼 ∗ 𝜓 ) = 𝜓 , because assuming so, it holds that 𝑤𝑙𝑝. qalloc ( 𝑞 ) .𝜙 = 𝜓 .

$$\begin{array} { r l } { \mathbb { m } { 0 } } & { 1 \stackrel { I } { \sim } ( 1 ) ^ { 2 } } \\ & { \mapsto \{ \varphi \} \, S \{ \phi \} \, \Longleftrightarrow \, \mathbb { m } { \leftarrow } \{ \varphi \} \ q a l l o c ( q ) \ \{ q \mapsto I * \psi \} } \\ & { \Longleftrightarrow \, \varphi \, \mathbb { m } { l } p . q a l l o c ( q ) . ( q \mapsto I * \psi ) } \\ & { \Longleftrightarrow \, \varphi \, \mathbb { m } { l } \psi } \end{array}$$

In next proof for Proposition 6.2, we would prove that

$$[ w l p . q a l l o c ( q ) . ( q \mapsto I * \psi ) ] \, d = \bigwedge _ { q ^ { \prime } } \left [ q ^ { \prime } \mapsto I * ( q ^ { \prime } \mapsto I * \psi ) \right ] d = \left [ \psi \right ] d$$

, Vol. 1, No. 1, Article . Publication date: September 2024.

## B.6 Proof for Theorem 6.2

For Theorem 6.2, we would prove that ∀ 𝑞 ′ . ( 𝑞 ↦→ 𝐼 - ∗ 𝜓 ) [ 𝑞 ⇒ 𝑞 ′ ] serves as the weakest liberal precondition for allocation statements, and other backwards inference rules have been proved in last section.

Soundness . Let us firstly prove that ⊨ {∀ 𝑞 ′ . ( 𝑞 ↦→ 𝐼 - ∗ 𝜓 ) [ 𝑞 ⇒ 𝑞 ′ ]} qalloc ( 𝑞 ) { 𝜓 } . The process of allocation consists of three steps: (i) expand a qubit 𝑞 ′ ∉ 𝑑𝑜𝑚 𝜌 . (ii) rename 𝑞 ⇒⊔ . (iii) rename 𝑞 ′ ⇒ 𝑞 . Thus for arbitrary 𝜌 ⊨ ∀ 𝑞 ′ .𝑞 ′ ↦→ 𝐼 - ∗ 𝜓 [ 𝑞 ⇒ 𝑞 ′ ] , after first step it holds that

$$\rho ^ { \prime } \vDash \psi [ q \Rightarrow q ^ { \prime } ] \text { provided } \rho ^ { \prime } | _ { d o m \, \rho } = \rho \text { and } q ^ { \prime } \notin d o m \, \rho$$

Because ⌈ 𝜌 ⌉ ⊆ 𝐼 𝑞 ′ -⊗ J 𝜓 [ 𝑞 ⇒ 𝑞 ′ ] K ( 𝑑𝑜𝑚 𝜌 ∪{ 𝑞 ′ }) implies 𝜌 ⊗ 𝐼 𝑞 ′ ⊆ J 𝜓 [ 𝑞 ⇒ 𝑞 ′ ] K ( 𝑑𝑜𝑚 𝜌 ∪{ 𝑞 ′ }) . Next, since ⊔ ∉ 𝑞𝑏𝑖𝑡 ( 𝜓 ) , it holds that

$$\rho ^ { \prime } \, \Leftrightarrow \psi [ q \Rightarrow q ^ { \prime } ] \, \Longrightarrow \, \rho ^ { \prime } \, \Leftrightarrow \psi [ q \Rightarrow q ^ { \prime } , \sqcup \Leftrightarrow q ] \, \Longrightarrow \, \rho ^ { \prime } [ q \Rightarrow \sqcup , q ^ { \prime } \Rightarrow q ] \, \Leftrightarrow \psi$$

which suggests that after allocation, the output state will satisfy 𝜓 .

Completeness . Next, supposing ⊨ { 𝜑 } qalloc ( 𝑞 ) { 𝜓 } , we prove that 𝜑 ⊨ ∀ 𝑞 ′ .𝑞 ′ ↦→ 𝐼 - ∗ 𝜓 [ 𝑞 ⇒ 𝑞 ′ ] . It suffices to show that 𝜑 𝑑 ⊆ 𝑞 ′ ↦→ 𝐼 - ∗ 𝜓 [ 𝑞 ⇒ 𝑞 ′ ] 𝑑 for arbitrary 𝑑 ⊆ 𝑓 𝑖𝑛 qDomain and 𝑞 ′ .

J K If 𝑞 ′ ∉ 𝑑 , then we construct a quantum heap 𝜌 ≜ 1 dim J 𝜑 K 𝑑 J 𝜑 K 𝑑 , after allocation it should satisfy 𝜓 , which suggests that ( 𝜑 ∗ 𝑞 ′ ↦→ 𝐼 ) [ 𝑞 ⇒ ⊔ , 𝑞 ′ ⇒ 𝑞 ] ⊨ 𝜓 , thus we could conclude that 𝜑 ⊨ 𝑞 ′ ↦→ 𝐼 - ∗ 𝜓 [ 𝑞 ⇒ 𝑞 ′ ] .

J K J K If 𝑞 ′ ∈ 𝑑 , then 𝑞 ′ ↦→ 𝐼 - ∗ 𝜓 [ 𝑞 ⇒ 𝑞 ′ ] 𝑑 = 𝐼 𝑑 and 𝑙ℎ𝑠 ⊆ 𝑟ℎ𝑠 is trivial.

RemarkB.1. Wewouldprove ∀ 𝑞 ′ .𝑞 ′ ↦→ 𝐼 - ∗ ( 𝑞 ′ ↦→ 𝐼 ∗ 𝜓 ) ≡ 𝜓 , which suggests that 𝑤𝑙𝑝. qalloc ( 𝑞 ) .𝑞 ↦→ 𝐼 ∗ 𝜓 = 𝜓 in the ending of last section. For arbitrary domain 𝑑 ⊆ 𝑓 𝑖𝑛 qDomain , if 𝑞 ′ ∈ 𝑑 then J 𝑞 ′ ↦→ 𝐼 - ∗ ( 𝑞 ′ ↦→ 𝐼 ∗ 𝜓 ) K 𝑑 = 𝐼 𝑑 . Thus it suffices to consider those 𝑞 ′ ∉ 𝑑 , where

therefore we conclude that ∀ 𝑞 ′ .𝑞 ′ ↦→ 𝐼 - ∗ ( 𝑞 ′ ↦→ 𝐼 ∗ 𝜓 ) ≡ 𝜓 .

$$\mathbb { I } [ q ^ { \prime } \mapsto I \ast ( q ^ { \prime } \mapsto I \ast \psi ) ] \, d = I _ { q ^ { \prime } } - \otimes \left ( I _ { q ^ { \prime } } \otimes \left [ \psi \right ] \right ) d ) = \left [ \psi \right ] d \\ \intertext { v e c n c l u d e t h a t \forall a ^ { \prime } \, q ^ { \prime } \mapsto I \ast ( q ^ { \prime } \mapsto I \ast \psi ) }$$

## B.7 Proof for Lemma 6.1

Soundness of the first inference rule is obvious:

$$\left [ \forall q ^ { \prime } . \psi [ q \Rightarrow q ^ { \prime } ] \right ] d = \bigcap _ { q ^ { \prime } \in \mathbf q \Name } \left [ \psi [ q \Rightarrow q ^ { \prime } ] \right ] d \subseteq \left [ \psi [ q \Rightarrow q _ { 1 } ] \right ] \text { for some } q _ { 1 } \in \mathbf q \Name$$

For the second inference rule, it's trivial that

$$[ \psi ] \, d \subseteq [ \varphi ] \, d \, \Longrightarrow \, \bigcap _ { q ^ { \prime } \in \mathbf q ^ { \prime } \in \mathbf q } [ \psi [ q \Rightarrow q ^ { \prime } ] ] \, d \subseteq \bigcap _ { q ^ { \prime } \in \mathbf q ^ { \prime } } [ \varphi [ q \Rightarrow q ^ { \prime } ] ]$$

For the third inference rule, when 𝑞 ∉ 𝑞𝑏𝑖𝑡 ( 𝜓 ) , then

$$\mathbb { [ } \forall q ^ { \prime } . \psi [ q \Rightarrow q ^ { \prime } ] ] \, \mathbb { ] } = \bigcap _ { q ^ { \prime } \in \mathbf q \, \mathbf X } \left [ \psi \right ] \, d = \left [ \psi \right ] \, d$$

## B.8 Proof for Theorem 7.1

The premise of Theorem 7.1 is equivalent to program 𝑆 does not contain allocation/free of qubit 𝑞 and the following triple is valid

$$\vDash \{ w l p . S . \top \wedge q , q ^ { \prime } \hookrightarrow | \Phi \rangle \langle \Phi | \} \, S \, \{ q , q ^ { \prime } \hookrightarrow | \Phi \rangle \langle \Phi | \}$$

For a stable domain 𝑑 , it can be easily verified that J 𝑤𝑙𝑝.𝑆. ⊤ K 𝑑 = 𝐼 𝑑 . The above triple suggests that, for execution path 𝜋 and encoded quantum operation E ∈ E 𝜋 , it holds that

$$\forall \rho \in \mathcal { D } ( \mathcal { H } _ { D \pi \langle q \rangle } ) . ( \mathcal { E } \otimes I _ { q ^ { \prime } } ) ( \rho \otimes | \Phi \rangle _ { q , q ^ { \prime } } \langle \Phi | ) = \rho ^ { \prime } \otimes | \Phi \rangle _ { q , q ^ { \prime } } \langle \Phi | \text { for some } \rho ^ { \prime }$$

Because 𝑞 ′ is not appearing in 𝑆 and 𝜌 ⊗ | Φ ⟩ 𝑞,𝑞 ′ ⟨ Φ | ⊨ 𝑤𝑙𝑝.𝑆. ⊤ ∧ 𝑞, 𝑞 ′ ↩ → | Φ ⟩⟨ Φ | . Thus the proof simplifies to: for a domain 𝑑 , 𝑞, 𝑞 ′ ∉ 𝑑 and quantum operation E on 𝑑 ∪ { 𝑞 } , if:

$$\forall \rho \in \mathcal { D } ( \mathcal { H } _ { d } ) . \, ( \mathcal { E } _ { d , q } \otimes I _ { q ^ { \prime } } ) ( \rho _ { d } \otimes | \Phi \rangle _ { q , q ^ { \prime } } \langle \Phi | ) = \rho _ { d } ^ { \prime } \otimes | \Phi \rangle _ { q , q ^ { \prime } } \langle \Phi | \text { for some } \rho ^ { \prime }$$

then exists E ′ on 𝑑 such that E = E ′ ⊗ I 𝑞 .

Supposing the Kraus representation of E is E( 𝐴 ) = ˝ 𝑘 𝐸 𝑘 𝐴𝐸 † 𝑘 , then:

$$\left \lceil ( \mathcal { E } _ { d , q } \otimes I _ { q } ^ { \prime } ) ( \rho ) \right \rceil \subseteq I _ { d } \otimes | \Phi _ { q , q ^ { \prime } } \langle \Phi | \, \Longrightarrow \, \forall | i \rangle \in \mathcal { H } _ { d } , k . \, \frac { 1 } { \sqrt { 2 } } \sum _ { j = 0 , 1 } ( E _ { k } \otimes I _ { q ^ { \prime } } ) | i \rangle _ { d } | j \rangle _ { q } | j \rangle _ { q ^ { \prime } } \in I _ { d } \otimes | \Phi \rangle _ { q , q ^ { \prime } } \langle \Phi |$$

Therefore for each 𝑖, 𝑘 , there exists a vector | 𝛽 ( 𝑘, 𝑖 )⟩ (not normalized) such that

$$\frac { 1 } { \sqrt { 2 } } \sum _ { j = 0 , 1 } ( E _ { k } \otimes I _ { q ^ { \prime } } ) | i \rangle _ { d } | j \rangle _ { q ^ { \prime } } | j \rangle _ { q ^ { \prime } } = | \beta ( k , i ) _ { d } \rangle \otimes | \Phi \rangle _ { q , q ^ { \prime } }$$

We multiply 𝐼 𝑑,𝑞 ⊗ ⟨ 𝑗 | 𝑞 ′ on both sides, for 𝑗 = 0 , 1,

$$E _ { k } | i \rangle _ { d } | j \rangle _ { q } = | \beta ( k , i ) \rangle _ { d } | j \rangle _ { q } \text { for each } k , i , j$$

therefore

$$E _ { k } = \sum _ { i , j } ( | \beta ( k , i ) \rangle _ { d } \otimes | j \rangle _ { q } ) ( \langle \beta ( k , i ) | _ { d } \otimes \langle j | _ { q } ) = \sum _ { i } | \beta ( k , i ) \rangle _ { d } \langle i | \otimes I _ { q }$$

where both {| 𝑖 ⟩} , {| 𝑗 ⟩} forms an orthonormal basis of H 𝑑 , H 𝑞 respectively. Thus we could conclude that E = E ′ ⊗ I 𝑞 for some E ′ .

## C Supplement Proof Details for Case Studies

In this section, we present proof details in the verification of cases in Section 8.

## C.1 Programs with Dirty Ancilla Qubits: In-place Addition Circuit and MCX Gate

Firstly we prove the correctness specification of in-place addition circuit step by step and compose them with rule Se/q.sc\_u.scence.

- Step 1, to prove ⊨ ¯ 𝑎 ↦→| ¯ 𝐶 ⟩ qalloc ( 𝑔 0 ) ¯ 𝑎 ↦→| ¯ 𝐶 ⟩ ∗ 𝑔 0 ↦→ 𝐼 . By rule Qalloc and Frame, it can be derived that

$$\Rightarrow \left \{ \bar { a } \mapsto | \bar { C } \rangle * \top ^ { * } \right \} \ q a l l o c ( g _ { 0 } ) \left \{ \bar { a } \mapsto | \bar { C } \rangle * g _ { 0 } \mapsto I \right \}$$

And with sound rule 17 in Figure 7, we know that ¯ 𝑎 ↦→| ¯ 𝐶 ⟩ ⊨ ¯ 𝑎 ↦→| ¯ 𝐶 ⟩ ∗ ⊤ ∗ , with rule Conse/q.sc\_u.scence:

$$\frac { \bar { a } \mapsto | \bar { C } \rangle \in \bar { a } \mapsto | \bar { C } \rangle * \top ^ { * } \quad \left \{ \bar { a } \mapsto | \bar { C } \rangle * \top ^ { * } \right \} \text {call} ( g _ { 0 } ) \ \left \{ \bar { a } \mapsto | \bar { C } \rangle * g _ { 0 } \mapsto I \right \} \\ \quad \left \{ \bar { a } \mapsto | \bar { C } \rangle \right \} \text {allloc} ( g _ { 0 } ) \ \left \{ \bar { a } \mapsto | \bar { C } \rangle * g _ { 0 } \mapsto I \right \}$$

- Step 2, similar to step 1, we can prove that

$$\Rightarrow \left \{ \bar { a } \mapsto | \bar { C } \rangle * g _ { 0 } \mapsto I \right \} \ q a l l o c ( g _ { 1 } ) \left \{ \bar { a } \mapsto | \bar { C } \rangle * g _ { 0 } \mapsto I * g _ { 1 } \mapsto I \right \}$$

By rules in Proposition 4.2, we know that

$$\bar { a } \mapsto | \bar { C } \rangle * g _ { 0 } \mapsto I * g _ { 1 } \mapsto I \vDash \bar { a } , g _ { 0 } , g _ { 1 } \mapsto \sum _ { i , j = 0 , 1 } | \bar { C } \rangle \langle \bar { C } | \otimes | i , j \rangle \langle i , j |$$

Thus after allocation statements, we conclude that

$$\ni \{ \bar { a } \mapsto | \bar { C } \rangle \langle \bar { C } | \} \ q a l l o c ( g _ { 0 } ) ; q a l l o c ( g _ { 1 } ) \left \{ \bar { a } , g _ { 0 } , g _ { 1 } \mapsto \sum _ { i , j = 0 , 1 } | \bar { C } \rangle \langle \bar { C } | \otimes | i , j \rangle \langle i , j | \right \}$$

- Step 3, with rule Unitary, we can prove for the body of program 𝑆 :

```
¯ 𝑎, 𝑔 0 , 𝑔 1 ↦→ ˝ 𝑖,𝑗 = 0 , 1 | ¯ 𝐶 ⟩⟨ ¯ 𝐶 | ⊗ | 𝑖, 𝑗 ⟩⟨ 𝑖, 𝑗 | 𝐶𝑁𝑂𝑇 [ 𝑔 1 , 𝑎 2 ] ; ¯ 𝑎, 𝑔 0 , 𝑔 1 ↦→ ˝ 𝑖,𝑗 = 0 , 1 | 𝐶 0 , 𝐶 1 , 𝐶 2 + 𝑗 ⟩⟨ 𝐶 0 , 𝐶 1 , 𝐶 2 + 𝑗 | ⊗ | 𝑖, 𝑗 ⟩⟨ 𝑖, 𝑗 | 𝐶𝑁𝑂𝑇 [ 𝑎 1 , 𝑔 1 ] ; ¯ 𝑎, 𝑔 0 , 𝑔 1 ↦→ ˝ 𝑖,𝑗 = 0 , 1 | 𝐶 0 , 𝐶 1 , 𝐶 2 + 𝑗 ⟩⟨ 𝐶 0 , 𝐶 1 , 𝐶 2 + 𝑗 | ⊗ | 𝑖, 𝑗 + 𝐶 1 ⟩⟨ 𝑖, 𝑗 + 𝐶 1 | 𝑋 [ 𝑎 1 ] ; ¯ 𝑎, 𝑔 0 , 𝑔 1 ↦→ ˝ 𝑖,𝑗 = 0 , 1 | 𝐶 0 , 𝐶 1 + 1 , 𝐶 2 + 𝑗 ⟩⟨ 𝐶 0 , 𝐶 1 + 1 , 𝐶 2 + 𝑗 | ⊗ | 𝑖, 𝑗 + 𝐶 1 ⟩⟨ 𝑖, 𝑗 + 𝐶 1 | 𝑇𝑜𝑓 𝑓 𝑜𝑙𝑖 [ 𝑔 0 , 𝑎 1 , 𝑔 1 ] ; ¯ 𝑎, 𝑔 0 , 𝑔 1 ↦→ ˝ 𝑖,𝑗 = 0 , 1 | 𝐶 0 , 𝐶 1 + 1 , 𝐶 2 + 𝑗 ⟩⟨ 𝐶 0 , 𝐶 1 + 1 , 𝐶 2 + 𝑗 | ⊗ | 𝑖, 𝑗 + 𝐶 1 + 𝑖 ( 𝐶 1 + 1 )⟩⟨ 𝑖, 𝑗 + 𝐶 1 + 𝑖 ( 𝐶 1 + 1 )| 𝐶𝑁𝑂𝑇 [ 𝑎 0 , 𝑔 0 ] ; ¯ 𝑎, 𝑔 0 , 𝑔 1 ↦→ ˝ 𝑖,𝑗 = 0 , 1 | 𝐶 0 , 𝐶 1 + 1 , 𝐶 2 + 𝑗 ⟩⟨ 𝐶 0 , 𝐶 1 + 1 , 𝐶 2 + 𝑗 | ⊗ | 𝑖 + 𝐶 0 , 𝑗 + 𝐶 1 + 𝑖 ( 𝐶 1 + 1 )⟩⟨ 𝑖 + 𝐶 0 , 𝑗 + 𝐶 1 + 𝑖 ( 𝐶 1 + 𝑇𝑜𝑓 𝑓 𝑜𝑙𝑖 [ 𝑔 0 , 𝑎 1 , 𝑔 1 ] ; ¯ 𝑎, 𝑔 0 , 𝑔 1 ↦→ ˝ 𝑖,𝑗 = 0 , 1 | 𝐶 0 , 𝐶 1 + 1 , 𝐶 2 + 𝑗 ⟩⟨ 𝐶 0 , 𝐶 1 + 1 , 𝐶 2 + 𝑗 | ⊗ | 𝑖 + 𝐶 0 , 𝑗 + 𝐶 0 + 𝐶 1 + 𝐶 0 𝐶 1 ⟩⟨ 𝑖 + 𝐶 0 , 𝑗 + 𝐶 0 + 𝐶 1 + 𝐶 𝐶𝑁𝑂𝑇 [ 𝑔 1 , 𝑎 2 ] ; ¯ 𝑎, 𝑔 0 , 𝑔 1 ↦→ ˝ 𝑖,𝑗 = 0 , 1 | 𝐶 0 , 𝐶 1 + 1 , 𝐶 2 + 𝐶 0 + 𝐶 1 + 𝐶 0 𝐶 1 ⟩⟨ 𝐶 0 , 𝐶 1 + 1 , 𝐶 2 + 𝐶 0 + 𝐶 1 + 𝐶 0 𝐶 1 | ⊗ | 𝑖 + 𝐶 0 , 𝑗 + 𝐶 0 + 𝐶 1 + 𝐶 𝑇𝑜𝑓 𝑓 𝑜𝑙𝑖 [ 𝑔 0 , 𝑎 1 , 𝑔 1 ] ; ¯ 𝑎, 𝑔 0 , 𝑔 1 ↦→ ˝ 𝑖,𝑗 = 0 , 1 | 𝐶 0 , 𝐶 1 + 1 , 𝐶 2 + 𝐶 0 + 𝐶 1 + 𝐶 0 𝐶 1 ⟩⟨ 𝐶 0 , 𝐶 1 + 1 , 𝐶 2 + 𝐶 0 + 𝐶 1 + 𝐶 0 𝐶 1 | ⊗ | 𝑖 + 𝐶 0 , 𝑗 + 𝐶 1 + 𝑖 ( 𝐶 1 + 𝐶𝑁𝑂𝑇 [ 𝑎 0 , 𝑔 0 ] ; ¯ 𝑎, 𝑔 0 , 𝑔 1 ↦→ ˝ 𝑖,𝑗 = 0 , 1 | 𝐶 0 , 𝐶 1 + 1 , 𝐶 2 + 𝐶 0 + 𝐶 1 + 𝐶 0 𝐶 1 ⟩⟨ 𝐶 0 , 𝐶 1 + 1 , 𝐶 2 + 𝐶 0 + 𝐶 1 + 𝐶 0 𝐶 1 | ⊗ | 𝑖, 𝑗 + 𝐶 1 + 𝑖 ( 𝐶 1 + 1 )⟩⟨ 𝑇𝑜𝑓 𝑓 𝑜𝑙𝑖 [ 𝑔 0 , 𝑎 1 , 𝑔 1 ] ; ¯ 𝑎, 𝑔 0 , 𝑔 1 ↦→ ˝ 𝑖,𝑗 = 0 , 1 | 𝐶 0 , 𝐶 1 + 1 , 𝐶 2 + 𝐶 0 + 𝐶 1 + 𝐶 0 𝐶 1 ⟩⟨ 𝐶 0 , 𝐶 1 + 1 , 𝐶 2 + 𝐶 0 + 𝐶 1 + 𝐶 0 𝐶 1 | ⊗ | 𝑖, 𝑗 + 𝐶 1 ⟩⟨ 𝑖, 𝑗 + 𝐶 1 | 𝑋 [ 𝑎 1 ] ; ¯ 𝑎, 𝑔 0 , 𝑔 1 ↦→ ˝ 𝑖,𝑗 = 0 , 1 | 𝐶 0 , 𝐶 1 , 𝐶 2 + 𝐶 0 + 𝐶 1 + 𝐶 0 𝐶 1 ⟩⟨ 𝐶 0 , 𝐶 1 , 𝐶 2 + 𝐶 0 + 𝐶 1 + 𝐶 0 𝐶 1 | ⊗ | 𝑖, 𝑗 + 𝐶 1 ⟩⟨ 𝑖, 𝑗 + 𝐶 1 | 𝐶𝑁𝑂𝑇 [ 𝑎 1 , 𝑔 1 ] ; ¯ 𝑎, 𝑔 0 , 𝑔 1 ↦→ ˝ 𝑖,𝑗 = 0 , 1 | 𝐶 0 , 𝐶 1 + 1 , 𝐶 2 + 𝐶 0 + 𝐶 1 + 𝐶 0 𝐶 1 ⟩⟨ 𝐶 0 , 𝐶 1 + 1 , 𝐶 2 + 𝐶 0 + 𝐶 1 + 𝐶 0 𝐶 1 | ⊗ | 𝑖, 𝑗 ⟩⟨ 𝑖, 𝑗 | = ⇒ ¯ 𝑎 ↦→| 𝑓 ( ¯ 𝐶 )⟩⟨ 𝑓 ( ¯ 𝐶 )| ∗ 𝑔 0 ↦→ 𝐼 ∗ 𝑔 1 ↦→ 𝐼
```

- Step 4, With backwards inference rules in Theorem 6.2, we conclude that

```
⊨ ¯ 𝑎 ↦→| 𝑓 ( ¯ 𝐶 )⟩⟨ 𝑓 ( ¯ 𝐶 )| ∗ 𝑔 0 ↦→ 𝐼 ∗ 𝑔 1 ↦→ 𝐼 qfree ( 𝑔 0 ) ; qfree ( 𝑔 1 ) ¯ 𝑎 ↦→| 𝑓 ( ¯ 𝐶 )⟩⟨ 𝑓 ( ¯ 𝐶 )|
```

where 𝑓 ( ¯ 𝐶 ) = 𝐶 0 , 𝐶 1 , 𝐶 2 + 𝐶 0 + 𝐶 1 + 𝐶 0 𝐶 1 .

- Step 5, with rule Se/q.sc\_u.scence, we conclude that

$$\neq \left \{ \bar { a } \mapsto | \bar { C } \rangle \langle \bar { C } | \right \} S \left \{ \bar { a } \mapsto | f ( \bar { C } ) \rangle \langle f ( \bar { C } ) | \right \}$$

Next, we prove the correct usage of dirty qubit 𝑔 0 in 𝑆.𝑏𝑜𝑑𝑦 , by Theorem 7.1 we know that it suffices to prove the validty of triple:

$$\Rightarrow \left \{ \bar { a } , g _ { 1 } \mapsto I * g _ { 0 } , g _ { 0 } ^ { \prime } \mapsto | \Phi \rangle \langle \Phi | \right \} S . b o d y \left \{ \top * g _ { 0 } , g _ { 0 } ^ { \prime } \mapsto | \Phi \rangle \langle \Phi | \right \}$$

With rule Unitary,

```
¯ 𝑎, 𝑔 1 ↦→ 𝐼 ∗ 𝑔 0 , 𝑔 ′ 0 ↦→| Φ ⟩⟨ Φ | = ⇒ ¯ 𝑎, 𝑔 1 , 𝑔 0 , 𝑔 ′ 0 ↦→ ˝ 𝑖,𝑗 | 𝑖 0 , 𝑖 1 , 𝑖 2 , 𝑖 3 , 𝑗, 𝑗 ⟩⟨ 𝑖 0 , 𝑖 1 , 𝑖 2 , 𝑖 3 , 𝑗, 𝑗 | 𝐶𝑁𝑂𝑇 [ 𝑔 1 , 𝑎 2 ] ; ¯ 𝑎, 𝑔 1 , 𝑔 0 , 𝑔 ′ 0 ↦→ ˝ 𝑖,𝑗 | 𝑖 0 , 𝑖 1 , 𝑖 2 + 𝑖 3 , 𝑖 3 , 𝑗, 𝑗 ⟩⟨ 𝑖 0 , 𝑖 1 , 𝑖 2 + 𝑖 3 , 𝑖 3 , 𝑗, 𝑗 | 𝐶𝑁𝑂𝑇 [ 𝑎 1 , 𝑔 1 ] ; ¯ 𝑎, 𝑔 1 , 𝑔 0 , 𝑔 ′ 0 ↦→ ˝ 𝑖,𝑗 | 𝑖 0 , 𝑖 1 , 𝑖 2 + 𝑖 3 , 𝑖 3 + 𝑖 1 , 𝑗, 𝑗 ⟩⟨ 𝑖 0 , 𝑖 1 , 𝑖 2 + 𝑖 3 , 𝑖 3 + 𝑖 1 , 𝑗, 𝑗 | 𝑋 [ 𝑎 1 ] ; ¯ 𝑎, 𝑔 1 , 𝑔 0 , 𝑔 ′ 0 ↦→ ˝ 𝑖,𝑗 | 𝑖 0 , 𝑖 1 + 1 , 𝑖 2 + 𝑖 3 , 𝑖 3 + 𝑖 1 , 𝑗, 𝑗 ⟩⟨ 𝑖 0 , 𝑖 1 + 1 , 𝑖 2 + 𝑖 3 , 𝑖 3 + 𝑖 1 , 𝑗, 𝑗 | 𝑇𝑜𝑓 𝑓 𝑜𝑙𝑖 [ 𝑔 0 , 𝑎 1 , 𝑔 1 ] ; ¯ 𝑎, 𝑔 1 , 𝑔 0 , 𝑔 ′ 0 ↦→ ˝ 𝑖,𝑗 | 𝑖 0 , 𝑖 1 + 1 , 𝑖 2 + 𝑖 3 , 𝑖 3 + 𝑖 1 + 𝑗𝑖 1 + 𝑗, 𝑗, 𝑗 ⟩⟨ 𝑖 0 , 𝑖 1 + 1 , 𝑖 2 + 𝑖 3 , 𝑖 3 + 𝑖 1 + 𝑗𝑖 1 + 𝑗, 𝑗, 𝑗 | 𝐶𝑁𝑂𝑇 [ 𝑎 0 , 𝑔 0 ] ; ¯ 𝑎, 𝑔 1 , 𝑔 0 , 𝑔 ′ 0 ↦→ ˝ 𝑖,𝑗 | 𝑖 0 , 𝑖 1 + 1 , 𝑖 2 + 𝑖 3 , 𝑖 3 + 𝑖 1 + 𝑗𝑖 1 + 𝑗, 𝑗 + 𝑖 0 , 𝑗 ⟩⟨ 𝑖 0 , 𝑖 1 + 1 , 𝑖 2 + 𝑖 3 , 𝑖 3 + 𝑖 1 + 𝑗𝑖 1 + 𝑗, 𝑗 + 𝑖 0 , 𝑗 | 𝑇𝑜𝑓 𝑓 𝑜𝑙𝑖 [ 𝑔 0 , 𝑎 1 , 𝑔 1 ] ; ¯ 𝑎, 𝑔 1 , 𝑔 0 , 𝑔 ′ 0 ↦→ ˝ 𝑖,𝑗 | 𝑖 0 , 𝑖 1 + 1 , 𝑖 2 + 𝑖 3 , 𝑗 + 𝑖 0 𝑖 1 + 𝑖 0 + 𝑖 3 + 𝑖 1 , 𝑗 + 𝑖 0 , 𝑗 ⟩⟨ 𝑖 0 , 𝑖 1 + 1 , 𝑖 2 + 𝑖 3 , 𝑗 + 𝑖 0 𝑖 1 + 𝑖 0 + 𝑖 3 + 𝑖 1 , 𝑗 + 𝑖 0 , 𝐶𝑁𝑂𝑇 [ 𝑔 1 , 𝑎 2 ] ; ¯ 𝑎, 𝑔 1 , 𝑔 0 , 𝑔 ′ 0 ↦→ ˝ 𝑖,𝑗 | 𝑖 0 , 𝑖 1 + 1 , 𝑗 + 𝑖 0 𝑖 1 + 𝑖 0 + 𝑖 2 + 𝑖 1 , 𝑗 + 𝑖 0 𝑖 1 + 𝑖 0 + 𝑖 3 + 𝑖 1 , 𝑗 + 𝑖 0 , 𝑗 ⟩⟨ 𝑖 0 , 𝑖 1 + 1 , 𝑗 + 𝑖 0 𝑖 1 + 𝑖 0 + 𝑖 2 + 𝑖 1 , 𝑇𝑜𝑓 𝑓 𝑜𝑙𝑖 [ 𝑔 0 , 𝑎 1 , 𝑔 1 ] ; ¯ 𝑎, 𝑔 1 , 𝑔 0 , 𝑔 ′ 0 ↦→ ˝ 𝑖,𝑗 | 𝑖 0 , 𝑖 1 + 1 , 𝑗 + 𝑖 0 𝑖 1 + 𝑖 0 + 𝑖 2 + 𝑖 1 , 𝑖 1 𝑗 + 𝑖 3 + 𝑖 1 , 𝑗 + 𝑖 0 , 𝑗 ⟩⟨ 𝑖 0 , 𝑖 1 + 1 , 𝑗 + 𝑖 0 𝑖 1 + 𝑖 0 + 𝑖 2 + 𝑖 1 , 𝑖 1 𝑗 + 𝑖 3 𝐶𝑁𝑂𝑇 [ 𝑎 0 , 𝑔 0 ] ; ¯ 𝑎, 𝑔 1 , 𝑔 0 , 𝑔 ′ 0 ↦→ ˝ 𝑖,𝑗 | 𝑖 0 , 𝑖 1 + 1 , 𝑗 + 𝑖 0 𝑖 1 + 𝑖 0 + 𝑖 2 + 𝑖 1 , 𝑖 1 𝑗 + 𝑖 3 + 𝑖 1 , 𝑗, 𝑗 ⟩⟨ 𝑖 0 , 𝑖 1 + 1 , 𝑗 + 𝑖 0 𝑖 1 + 𝑖 0 + 𝑖 2 + 𝑖 1 , 𝑖 1 𝑗 + 𝑖 3 + 𝑖 1 , 𝑇𝑜𝑓 𝑓 𝑜𝑙𝑖 [ 𝑔 0 , 𝑎 1 , 𝑔 1 ] ; ¯ 𝑎, 𝑔 1 , 𝑔 0 , 𝑔 ′ 0 ↦→ ˝ 𝑖,𝑗 | 𝑖 0 , 𝑖 1 + 1 , 𝑗 + 𝑖 0 𝑖 1 + 𝑖 0 + 𝑖 2 + 𝑖 1 , 𝑖 3 + 𝑖 1 , 𝑗, 𝑗 ⟩⟨ 𝑖 0 , 𝑖 1 + 1 , 𝑗 + 𝑖 0 𝑖 1 + 𝑖 0 + 𝑖 2 + 𝑖 1 , 𝑖 3 + 𝑖 1 , 𝑗, 𝑗 | 𝑋 [ 𝑎 1 ] ; ¯ 𝑎, 𝑔 1 , 𝑔 0 , 𝑔 ′ 0 ↦→ ˝ 𝑖,𝑗 | 𝑖 0 , 𝑖 1 , 𝑗 + 𝑖 0 𝑖 1 + 𝑖 0 + 𝑖 2 + 𝑖 1 , 𝑖 3 + 𝑖 1 , 𝑗, 𝑗 ⟩⟨ 𝑖 0 , 𝑖 1 , 𝑗 + 𝑖 0 𝑖 1 + 𝑖 0 + 𝑖 2 + 𝑖 1 , 𝑖 3 + 𝑖 1 , 𝑗, 𝑗 | 𝐶𝑁𝑂𝑇 [ 𝑎 1 , 𝑔 1 ] ; ¯ 𝑎, 𝑔 1 , 𝑔 0 , 𝑔 ′ 0 ↦→ ˝ 𝑖,𝑗 | 𝑖 0 , 𝑖 1 , 𝑗 + 𝑖 0 𝑖 1 + 𝑖 0 + 𝑖 2 + 𝑖 1 , 𝑖 3 , 𝑗, 𝑗 ⟩⟨ 𝑖 0 , 𝑖 1 , 𝑗 + 𝑖 0 𝑖 1 + 𝑖 0 + 𝑖 2 + 𝑖 1 , 𝑖 3 , 𝑗, 𝑗 | = ⇒ ⊤∗ 𝑔 0 , 𝑔 ′ 0 ↩ →| Φ ⟩⟨ Φ |
```

As a matter of fact, we could notice that if the circuit is composed with only X, CNOT and Toffoli gates, it suffices to verify the circuit with input in computational basis. And verification for MCX gate is carried out in the same way.

## C.2 Program with While Loop: Repeat-Until-Success Circuit

Before entering loop

## . Similar to the last case, we can prove that

```
{ 𝑞 ↦→| 𝜆 ⟩} qalloc ( 𝑞 1 ) ; { 𝑞 ↦→| 𝜆 ⟩ ∗ 𝑞 1 ↦→ 𝐼 } qalloc ( 𝑞 2 ) ; { 𝑞 ↦→| 𝜆 ⟩ ∗ 𝑞 1 ↦→ 𝐼 ∗ 𝑞 2 ↦→ 𝐼 } = ⇒ { 𝑞 ↦→| 𝜆 ⟩ ∗ 𝑞 1 , 𝑞 2 ↦→ 𝐼 }
```

Then with rule Init,Unitary and Frame, we continue the proof

$$\begin{array} { r l } & { \cdots } \\ & { \Longrightarrow \ \{ q \mapsto | \lambda \rangle * q _ { 1 } , q _ { 2 } \mapsto I \} } \\ & { [ q _ { 1 } , q _ { 2 } ] \colon = | 0 \rangle ; } \\ & { \Longrightarrow \ \{ q \mapsto | \lambda \rangle * q _ { 1 } , q _ { 2 } \mapsto | 0 0 \rangle \} } \\ & { X [ q _ { 1 } ] ; H [ q _ { 1 } ] ; } \\ & { \Longrightarrow \ \{ q \mapsto | \lambda \rangle * q _ { 1 } , q _ { 2 } \mapsto | 0 - \rangle \} } \end{array}$$

Next, we need to prove that

$$q \mapsto | \lambda \rangle * q _ { 1 } , q _ { 2 } \mapsto | 0 - \rangle \equiv ( q _ { 1 } , q _ { 2 } \hookrightarrow I ) \wedge ( q _ { 1 } , q _ { 2 } \hookrightarrow P _ { 1 } \mapsto \varphi ) \wedge ( q _ { 1 } , q _ { 2 } \hookrightarrow P _ { 0 } \mapsto \psi )$$

Each conjunction clause is proven separately. With sound rules in Figure 7 it can be derived that

$$\frac { q \mapsto | \lambda \rangle \vDash \top \quad q _ { 1 } , q _ { 2 } \mapsto | 0 - \rangle \vDash q _ { 1 } , q _ { 2 } \mapsto I } { q \mapsto | \lambda \rangle * q _ { 1 } , q _ { 2 } \mapsto | 0 - \rangle \vDash \top * q _ { 1 } , q _ { 2 } \mapsto I ) }$$

Next, because | 0 -⟩⟨ 0 - | ⊆ 𝑃 1 , therefore

$$( q \mapsto | \lambda \rangle * q _ { 1 } , q _ { 2 } \mapsto | 0 - \rangle ) \wedge ( q _ { 1 } , q _ { 2 } \hookrightarrow P _ { 1 } ) \equiv q \mapsto | \lambda \rangle * q _ { 1 } , q _ { 2 } \mapsto | 0 - \rangle \not \equiv q _ { 1 } , q _ { 2 } , q \mapsto I \otimes | \lambda \rangle \langle \lambda | = \varphi$$

So with introduction rule for Sasaki hook, we conclude that

$$q \mapsto | \lambda \rangle * q _ { 1 } , q _ { 2 } \mapsto | 0 - \rangle \cong ( q _ { 1 } , q _ { 2 } \hookrightarrow P _ { 1 } ) \hookrightarrow \varphi$$

Similarly, since | 0 -⟩⟨ 0 - | ∧ 𝑃 0 = 0 , thus

$$( q \mapsto | \lambda \rangle * q _ { 1 } , q _ { 2 } \mapsto | 0 - \rangle ) \wedge ( q _ { 1 } , q _ { 2 } \hookrightarrow P _ { 0 } ) \equiv \perp \vDash$$

$$q \mapsto | \lambda \rangle * q _ { 1 } , q _ { 2 } \mapsto | 0 - \rangle \cong ( q _ { 1 } , q _ { 2 } \hookrightarrow P _ { 0 } ) \hookrightarrow \psi$$

Loop body . With rule While, we prove for the loop body

```
{ 𝑞 1 , 𝑞 2 , 𝑞 ↦→ 𝐼 ⊗ | 𝜆 ⟩⟨ 𝜆 |} qalloc ( 𝑞 3 ) ; { 𝑞 1 , 𝑞 2 , 𝑞 ↦→ 𝐼 ⊗ | 𝜆 ⟩⟨ 𝜆 | ∗ 𝑞 3 ↦→ 𝐼 } = ⇒ { 𝑞 1 , 𝑞 2 , 𝑞 3 ↦→ 𝐼 ∗ 𝑞 ↦→| 𝜆 ⟩} [ 𝑞 1 , 𝑞 2 , 𝑞 3 ] : = | 0 ⟩ ; = ⇒ { 𝑞 1 , 𝑞 2 , 𝑞 3 ↦→| 0 ⟩ ∗ 𝑞 ↦→| 𝜆 ⟩} 𝐻 [ 𝑞 1 ]; 𝐻 [ 𝑞 2 ]; 𝑇𝑜𝑓 𝑓 𝑜𝑙𝑖 [ 𝑞 1 , 𝑞 2 , 𝑞 3 ]; 𝑞 1 , 𝑞 2 , 𝑞 3 ↦→ 1 2 (| 00 ⟩ + | 01 ⟩ + | 10 ⟩)| 0 ⟩ + | 11 ⟩| 1 ⟩ ∗ 𝑞 ↦→| 𝜆 ⟩ = ⇒ 𝑞 1 , 𝑞 2 , 𝑞 3 , 𝑞 ↦→ 1 2 (| 00 ⟩ + | 01 ⟩ + | 10 ⟩)| 0 ⟩| 𝜆 ⟩ + | 11 ⟩| 1 ⟩| 𝜆 ⟩ 𝐶𝑁𝑂𝑇 [ 𝑞 3 , 𝑞 ] ; 𝑆 [ 𝑞 ] ; 𝐶𝑁𝑂𝑇 [ 𝑞 3 , 𝑞 ] ; 𝑍 [ 𝑞 ] ; 𝑞 1 , 𝑞 2 , 𝑞 3 , 𝑞 ↦→ 1 2 (| 00 ⟩ + | 01 ⟩ + | 10 ⟩)| 0 ⟩( 𝑍𝑆 | 𝜆 ⟩) + | 11 ⟩| 1 ⟩( 𝑍𝑋𝑆𝑋 | 𝜆 ⟩) = ⇒ { 𝑞 3 , 𝑞 1 , 𝑞 2 , 𝑞 ↦→ 1 2 √ 2 |+⟩[(| 00 ⟩ + | 01 ⟩ + | 10 ⟩)( 𝑍𝑆 | 𝜆 ⟩) + | 11 ⟩( 𝑍𝑋𝑆𝑋 | 𝜆 ⟩)] + 1 2 √ 2 |-⟩[(| 00 ⟩ + | 01 ⟩ + | 10 ⟩)( 𝑍𝑆 | 𝜆 ⟩) - | 11 ⟩( 𝑍𝑋𝑆𝑋 | 𝜆 ⟩)]}
```

Next, because 𝑞 ↦→| 𝑣 ⟩ + | 𝑤 ⟩ = ⇒ 𝑞 ↦→| 𝑣 ⟩⟨ 𝑣 | + | 𝑤 ⟩⟨ 𝑤 | = ⇒ 𝑞 ↦→| 𝑣 ⟩ ∨ 𝑞 ↦→| 𝑤 ⟩ , thus

$$& \{ q _ { 3 } , q _ { 1 } , q _ { 2 } , q \mapsto \frac { 1 } { 2 } \frac { 1 } { | } + | \langle [ ( 0 0 ) + | 0 1 \rangle + | 1 0 \rangle ) ( Z S | \lambda ) \rangle + | 1 1 \rangle ( Z X S | \lambda ) \rangle ] \\ & + \frac { + \frac { 1 } { 2 } | - | \langle [ 0 0 ] + | 0 1 \rangle + | 1 0 \rangle ( Z S | \lambda ) \rangle - | 1 1 \rangle ( Z X S | \lambda ) \rangle ] \implies \\ & \{ q _ { 3 } , q _ { 1 } , q _ { 2 } , q \mapsto \frac { 1 } { 2 } | + \rangle ( | 0 0 \rangle + | 0 1 \rangle + | 1 0 \rangle ) ( Z S | \lambda ) + | 1 1 \rangle ( Z X S | \lambda ) \rangle ] v \\ & q _ { 3 } , q _ { 1 } , q _ { 2 } , q \mapsto \frac { 1 } { 2 } | - \rangle [ ( | 0 0 \rangle + | 0 1 \rangle + | 1 0 \rangle ) ( Z S | \lambda ) - | 1 1 \rangle ( Z X S | \lambda ) \rangle ]$$

So we conclude that

$$Bl-based Reasoning about Quantum Programs with Heap Manipulations & \\
After the measurement, we need to prove that & & \\ & \quad \text {if } M [ q s ] \text { then} \\ & \quad \text {CZ} [ q _ { 2 } ] _ { 2 } \\ & \quad \text {else} & \quad \text {skip} \\ & \quad \{ q _ { 3 } \mapsto 1 * q _ { 2 } , q \mapsto \frac { [ ( 0 0 ) + | 0 1 ) + | 0 1 ) ( Z S | \lambda ) } { | 1 | ( Z X S | \lambda ) | ] \} \\ \text {With rule Ir and Unrary, it suffices to show that} & \\ & \quad \text {(q$_{3 } \leftrightarrow 1)^{\lambda}} & & \\ & \quad ( q _ { 3 } \leftrightarrow | + \rangle \mapsto q _ { 1 } \mapsto 1 * q _ { 2 } , q _ { 2 } \mapsto \frac { [ ( 0 0 ) + | 0 1 ) + | 0 1 ) ( Z S | \lambda ) + | 1 | ( Z X S | \lambda ) | } { | 2 | ( 0 0 ) + | 0 1 | + | 0 1 ) ( Z S | \lambda ) - | 1 | ( Z X S | \lambda ) | } ) \\ & \quad ( q _ { 3 } \leftrightarrow | - \rangle \mapsto q _ { 1 } \mapsto 1 * q _ { 1 } , q _ { 2 } \mapsto \frac { [ ( 0 0 ) + | 0 1 ) + | 0 1 ) ( Z S | \lambda ) - | 1 | ( Z X S | \lambda ) | } { | 2 | ( 0 0 ) + | 0 1 | + | 0 1 ) ( Z S | \lambda ) + | 1 | ( Z X S | \lambda ) | } ) \\ \text {where Post denotes the postcondition in Equation 2. And it can be easily check that} & \\ & \quad \text {Post } \wedge ( q _ { 3 } \leftrightarrow | + \rangle \mapsto q _ { 1 } , q _ { 2 } , q _ { 2 } \mapsto \frac { | 2 | + | ( | 0 0 | + | 0 1 ) + | 0 1 ) ( Z S | \lambda ) + | 1 | ( Z X S | \lambda ) | } { | 2 | ( 0 0 ) + | 0 1 | + | 0 1 ) ( Z S | \lambda ) + | 1 | ( Z X S | \lambda ) | } ) \\ & \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \qu$$

$$q _ { 1 } , q _ { 2 } , q & \mapsto | \mu \rangle \in q _ { 1 } , q _ { 2 } , q _ { 3 } \mapsto | + \rangle \langle + + | \otimes V _ { 3 } | \rangle \langle \lambda | V _ { 3 } ^ { \dagger } \vee q _ { 1 } , q _ { 2 } , q _ { 3 } \mapsto ( I - | + \rangle \langle + + | ) \otimes | \lambda \rangle \langle \lambda | \\ & \mapsto ( q _ { 1 } , q _ { 2 } \hookrightarrow I ) \wedge ( q _ { 1 } , q _ { 2 } \hookrightarrow P _ { 0 } \mapsto \psi ) \wedge ( q _ { 1 } , q _ { 2 } \hookrightarrow P _ { 1 } \mapsto \varphi ) .$$

Thus when exiting while-loop, we conclude that

$$\{ \dots \} \dots \text {end } \left \{ q _ { 1 } , q _ { 2 } , q \mapsto I \otimes V _ { 3 } | \lambda \rangle \langle \lambda | V _ { 3 } ^ { \dagger } \right \}$$

After while-loop . After freeing 𝑞 1 , 𝑞 2 , we could prove that

<!-- formula-not-decoded -->

And we conclude the correctness specification for the whole program

<!-- formula-not-decoded -->

## C.3 Program with Recursion: Quantum Recursive Fourier Sampling

For 𝑄𝑅𝐹𝑆 ( 𝑙 ) . We could prove that

<!-- formula-not-decoded -->

For QRFS(k). We could prove that

<!-- formula-not-decoded -->

For each 𝑖 ∈ { 0 . 1 } ( 𝑘 + 1 ) 𝑛 , we divided it into two parts: the first 𝑘𝑛 bits and last 𝑛 bits, which is denoted as 𝑖 = 𝑥,𝑦 . We know that

<!-- formula-not-decoded -->

## Therefore

```
n ¯ 𝑥 0 , . . . , ¯ 𝑥 𝑘 ↦→ ˝ 2 ( 𝑘 + 1 ) 𝑛 -1 𝑖 = 0 (-1 ) 𝑔 ( 𝑠 𝑖 ) (-1 ) 𝑏 ′ 𝑖 | 𝑖 ⟩ ∗ 𝑞 𝑘 ↦→|-⟩ o = ⇒ n ¯ 𝑥 0 , . . . , ¯ 𝑥 𝑘 ↦→ ˝ 2 𝑘𝑛 -1 𝑥 = 0 (-1 ) 𝑏 𝑥 ˝ 2 𝑛 -1 𝑦 = 0 (-1 ) 𝑠 𝑥 · 𝑦 | 𝑥,𝑦 ⟩ ∗ 𝑞 𝑘 ↦→|-⟩ o 𝐻 ⊗ 𝑛 [ ¯ 𝑥 𝑘 ] ; n ¯ 𝑥 0 , . . . , ¯ 𝑥 𝑘 , 𝑞 𝑘 ↦→ ˝ 2 𝑘𝑛 -1 𝑥 = 0 (-1 ) 𝑏 𝑥 | 𝑥, 𝑠 𝑥 ⟩|-⟩ o 𝐺 [ ¯ 𝑥 𝑘 , 𝑞 𝑘 ] ; n ¯ 𝑥 0 , . . . , ¯ 𝑥 𝑘 , 𝑞 𝑘 ↦→ ˝ 2 𝑘𝑛 -1 𝑥 = 0 (-1 ) 𝑔 ( 𝑠 𝑥 ) (-1 ) 𝑏 𝑥 | 𝑥, 𝑠 𝑥 ⟩|-⟩ o = ⇒ n ¯ 𝑥 0 , . . . , ¯ 𝑥 𝑘 ↦→ ˝ 2 𝑘𝑛 -1 𝑥 = 0 (-1 ) 𝑔 ( 𝑠 𝑥 ) (-1 ) 𝑏 𝑥 | 𝑥, 𝑠 𝑥 ⟩ ∗ 𝑞 𝑘 ↦→|-⟩ o 𝐻 ⊗ 𝑛 [ ¯ 𝑥 𝑘 ] ; n ¯ 𝑥 0 , . . . , ¯ 𝑥 𝑘 ↦→ ˝ 2 𝑘𝑛 -1 𝑥 = 0 ˝ 2 𝑛 -1 𝑦 = 0 (-1 ) 𝑐 𝑥,𝑦 | 𝑥,𝑦 ⟩ ∗ 𝑞 𝑘 ↦→|-⟩ o where for 𝑥,𝑦 ∈ { 0 , 1 } ( 𝑘 + 1 ) 𝑛 , 𝑐 𝑥,𝑦 = 𝑠 𝑥 · 𝑦 ⊕ 𝑏 𝑥 ⊕ 𝑔 ( 𝑠 𝑥 ) . Then by induction hypothesis, n ¯ 𝑥 0 , . . . , ¯ 𝑥 𝑘 ↦→ ˝ 2 𝑘𝑛 -1 𝑥 = 0 ˝ 2 𝑛 -1 𝑦 = 0 (-1 ) 𝑐 𝑥,𝑦 | 𝑥,𝑦 ⟩ ∗ 𝑞 𝑘 ↦→|-⟩ o 𝑄𝑅𝐹𝑆 ( 𝑘 + 1 ) ; n ¯ 𝑥 0 , . . . , ¯ 𝑥 𝑘 ↦→ ˝ 2 𝑘𝑛 -1 𝑥 = 0 ˝ 2 𝑛 -1 𝑦 = 0 (-1 ) 𝑔 ( 𝑠 𝑥,𝑦 ) (-1 ) 𝑐 𝑥,𝑦 | 𝑥,𝑦 ⟩ ∗ 𝑞 𝑘 ↦→|-⟩ o By careful computation. it can be checked that 𝑔 ( 𝑠 𝑥,𝑦 ) ⊕ 𝑐 𝑥,𝑦 = 𝑠 𝑥 · 𝑦 ⊕ 𝑠 𝑥 · 𝑦 ⊕ 𝑏 𝑥 ⊕ 𝑔 ( 𝑠 𝑥 ) = 𝑏 𝑥 ⊕ 𝑔 ( 𝑠 𝑥 ) Therefore n ¯ 𝑥 0 , . . . , ¯ 𝑥 𝑘 ↦→ ˝ 2 𝑘𝑛 -1 𝑥 = 0 ˝ 2 𝑛 -1 𝑦 = 0 (-1 ) 𝑔 ( 𝑠 𝑥,𝑦 ) (-1 ) 𝑐 𝑥,𝑦 | 𝑥,𝑦 ⟩ ∗ 𝑞 𝑘 ↦→|-⟩ o = ⇒ n ¯ 𝑥 0 , . . . , ¯ 𝑥 𝑘 -1 ↦→ ˝ 2 𝑘𝑛 -1 𝑥 = 0 (-1 ) 𝑔 ( 𝑠 𝑥 ) (-1 ) 𝑏 𝑥 | 𝑥 ⟩ ∗ ¯ 𝑥 𝑘 ↦→ ˝ 2 𝑛 -1 𝑦 = 0 | 𝑦 ⟩ ∗ 𝑞 𝑘 ↦→|-⟩ o = ⇒ n ¯ 𝑥 0 , . . . , ¯ 𝑥 𝑘 -1 ↦→ ˝ 2 𝑘𝑛 -1 𝑥 = 0 (-1 ) 𝑔 ( 𝑠 𝑥 ) (-1 ) 𝑏 𝑥 | 𝑥 ⟩ ∗ ¯ 𝑥 𝑘 ↦→ 𝐼 ∗ 𝑞 𝑘 ↦→ 𝐼 o qfree ( ¯ 𝑥 𝑘 ) ; qfree ( 𝑞 𝑘 ) n ¯ 𝑥 0 , . . . , ¯ 𝑥 𝑘 -1 ↦→ ˝ 2 𝑘𝑛 -1 𝑥 = 0 (-1 ) 𝑔 ( 𝑠 𝑥 ) (-1 ) 𝑏 𝑥 | 𝑥 ⟩ o
```

which finishes the proof.