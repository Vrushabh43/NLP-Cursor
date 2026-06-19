## Utilizing classical programming principles in the Intel Quantum SDK: implementation of quantum lattice Boltzmann method

Quanscient Oy, Finland and University of Jyväskylä, Finland

Quanscient Oy, Finland and Faculty of Technical Sciences, University of Novi Sad, Serbia Quanscient Oy, Finland

Quanscient Oy, Finland

Technische Hochschule Deggendorf, Germany

Technische Hochschule Deggendorf, Germany

TEJAS SHINDE, LJUBOMIR BUDINSKI, OSSI NIEMIMÄKI, VALTTERI LAHTINEN, HELENA LIEBELT, RUI LI,

We explore the use of classical programming techniques in implementing the quantum lattice Boltzmann method in the Intel Quantum SDK - a software tool for quantum circuit creation and execution on Intel quantum hardware. As hardware access is limited, we use the state vector simulator provided by the SDK. The novelty of this work lies in leveraging classical techniques for the implementation of quantum algorithms. We emphasize the refinement of algorithm implementation and devise strategies to enhance quantum circuits for better control over problem variables. To this end, we adopt classical principles such as modularization, which allows for systematic and controlled execution of complex algorithms. Furthermore, we discuss how the same implementation could be expanded from state vector simulations to execution on quantum hardware with minor adjustments in these configurations.

CCS Concepts: · Software and its engineering → Software creation and management ; · Applied computing → Physical sciences and engineering .

Additional Key Words and Phrases: quantum computing, quantum algorithm, Intel Quantum SDK

## ACMReference Format:

Tejas Shinde, Ljubomir Budinski, Ossi Niemimäki, Valtteri Lahtinen, Helena Liebelt, and Rui Li. 2024. Utilizing classical programming principles in the Intel Quantum SDK: implementation of quantum lattice Boltzmann method. In . ACM, New York, NY, USA, 17 pages. https://doi.org/10.1145/nnnnnnn.nnnnnnn

## 1 INTRODUCTION

In the field of engineering, industrial and scientific simulations place substantial demands on computational resources. Advances in computing hardware, such as high-performance computing clusters and GPUs, are catering to increasing computational demands, but the ability to shrink transistors is hitting physical limits, threatening the well-known Moore's law [Waldrop 2016]. Quantum computing has received substantial attention over the past few years as a means for pushing the envelope. New algorithms have been developed, showing algorithmic efficiency over classical computing. For example, there is a potential quantum speed-up in applications such as linear algebra [Lloyd et al. 2020; Qian et al. 2019; Ambainis 2010], quantum chemistry [Cao et al. 2019], optimization [Kerenidis and Prakash 2020; Farhi et al. 2014] and machine learning [Garg and Ramakrishnan 2020; Sharma 2020].

Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than ACM must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org.

© 2024 Association for Computing Machinery.

Manuscript submitted to ACM

With the development of algorithms, there is a need for refined methods and techniques for smooth and robust implementation. Implementing the quantum circuits in a reusable and scalable manner, and integrating them into possible applications poses a new challenge. At its core, this challenge arises from the intricate nature of quantum algorithms, which usually rely on complex sequences of quantum gates acting on qubits. Achieving reusability is challenging due to the constraints and the specificity of each application. Scalability is vital for building larger optimized quantum algorithms and ensuring efficient utilization of the resources as systems grow in size.

Themaincontribution of this work is the use of classical programming principles in implementing quantum algorithms in the Intel Quantum SDK [Khalate et al. 2022]. The Intel Quantum SDK is a C ++ based quantum programming framework tailored for hybrid quantum-classical programming. For this work, we have chosen the quantum lattice Boltzmann method (QLBM) as an example for the implementation. The QLBM is a promising quantum algorithm for computational fluid dynamics simulations. It provides a quantum-native way to solve transport phenomena, with recent advancements showing its potential for quantum efficiency [Budinski 2021, 2022; Budinski et al. 2023]. In this paper, we focus on the QLBM algorithm for the advection-diffusion equation as presented in [Budinski 2021]. Additionally, we provide a brief explanation on expanding the implementation to 2D advection-diffusion [Budinski 2021, Section 3.2] and Navier-Stokes equations using the stream function-vorticity formulation [Budinski 2022]. However, we do not aim to expand or improve the QLBM algorithm itself in this work, but rely solely on the already-existing knowledge.

Through this example, we explore the programming design principles in the context of quantum algorithms. We focus on the modular approach in forming generic building blocks for the complex algorithm, such that can be easily scaled and reused in different configurations. We also outline possibilities for hybrid design, for which the Intel Quantum SDK is particularly suitable.

This paper is structured as follows. Section 2 provides a concise overview of the Intel Quantum SDK. In Section 3 we briefly recap the lattice Boltzmann method and discuss the quantum circuit implementation in general. In Section 4, we begin with an analysis of how classical techniques are employed for the implementation of quantum algorithms in the Intel Quantum SDK. The section concludes with an exploration of expanding the implementation to address 2D advection-diffusion and Navier-Stokes equations, accompanied by numerical validation using a simple example.

## 2 INTEL QUANTUM SDK

The Intel Quantum SDK is an LLVM 1 based environment that allows the writing of hybrid quantum-classical algorithms on computational systems, targeting variational quantum algorithms in particular [Khalate et al. 2022]. The SDK follows a similar approach as a classical hardware accelerator environment, which allows one to write instructions targeted for specialized hardware such as GPU and FPGA in order to increase efficiency. The SDK aims to make it efficient to run hybrid quantum-classical parts of computational problems, where the quantum hardware acts as an accelerator. The Intel Quantum SDK enables quantum kernels for quantum instructions targeted for the quantum hardware, and classical methods for the classical instructions targeted towards the CPU within the same algorithm. Separating the instructions benefits the use of hybrid quantum and classical computing.

The SDK provides a C ++ based programming interface based on the circuit model for quantum computation. The SDK is developed with the Intel quantum hardware in mind, but these devices are not yet available to general public. Instead, the SDK provides a full-state simulator class with API calls to set up a CPU-based simulator and provides access the quantum state during the simulation. It allows users to simulate and test their program in an ideal case without access to actual quantum hardware. The quantum state is accessed through methods that return the conditional probabilities of the qubits and complex amplitudes of the state space. Fig. 1 gives an overview of the Intel quantum computing stack.

1 A collection of compiler and toolchain technologies.

Fig. 1. Overview of Intel Quantum SDK as described in [Khalate et al. 2022].

<!-- image -->

The version 1.0 of the Intel Quantum SDK added a Python interface to the existing framework. This helps convert OpenQASM2 [Cross et al. 2017] circuit instructions to Intel Quantum SDK compatible C ++ source code. The Python interface also allows to compile and run the quantum circuits directly. We make use of this in the implementation to add circuit functionalities that would have been otherwise difficult to realize through the C ++ interface at the time of writing.

## 3 QUANTUM LATTICE BOLTZMANN METHOD

The lattice Boltzmann method (LBM) is a computational fluid dynamics technique for simulating complex fluid flows. Traditional methods in computational fluid dynamics, such as finite difference, finite volume, and finite element methods, rely on solving the Navier-Stokes equations to model fluid flow. These techniques involve complex discretization schemes and extensive computational resources, often leading to challenges in handling complex boundary conditions and multiphase flows. In contrast, the LBM offers a more intuitive and flexible approach by simulating fluid dynamics through the evolution of particle distribution functions on a lattice grid - see for example [A.A.Mohamad 2019] for a comparison of the LBM with the traditional finite difference method in different scenarios.

In particular, we are interested in the LBM as a promising method for solving fluid dynamics problems with quantum computers, and use the simple advection-diffusion model [Budinski 2021] as an example of a hybrid computation scheme. For more recent advancements on quantum implementations see for example [Schalkers and Möller 2024a] and [Schalkers and Möller 2024b].

The LBM operates on a lattice grid where each node represents a fluid particle distribution function. Through a series of collision and propagation steps, these functions evolve over time to simulate fluid behavior.

The LBM follows a mesoscopic approach and bridges the gap between molecular dynamics and macroscopic fluid dynamics, offering insights into various flow phenomena at different scales. [Krueger et al. 2016]

A D1Q2 lattice arrangement is shown in Fig. 2, where DnQm stands for 𝑛 dimensions and 𝑚 velocity vectors.

Fig. 2. 1D lattice arrangement

<!-- image -->

The D1Q2 arrangement consists of two velocity vectors 𝑒 1 = 1 , 𝑒 2 = -1 for the distributions 𝑓 1 and 𝑓 2 , respectively. At an instance in time, two particles exist at a site, moving right and left in the streaming process. The weighting factors for the D1Q2 are 1 / 2 for both distributions 𝑓 𝑖 .

As a simple example, we study the QLBM solution to the advection-diffusion equation. The quantum algorithm for the D1Q2 QLBM can be divided into four major steps: encoding, collision, propagation, and the calculation of macroscopic variables. Each of these is illustrated in the circuit implementation in Fig. 3. The steps proceed as follows:

- (1) Encoding: In the encoding step we set up two quantum registers 𝑞 and 𝑎 . To encode the vector into quantum states and do the computation we require the quantum working register 𝑞 . The working register encodes the vector with concentration 𝐶 ( 𝑥, 𝑡 ) having qubits equal to log 2 ( 2 𝑀 ) , where 𝑀 is the lattice size. The ancilla register 𝑎 consists of only one qubit and is used in the controlled operation in the collision step, as shown in Fig. 3. To achieve the initial state, external state preparation is used, for example the state preparation procedure proposed by Shende et al. [Shende et al. 2006]
- (2) Collision: The collision step is a point-wise multiplication between the vector 𝐶 and the block diagonal matrix according to

$$f _ { i } ^ { e q } ( \vec { x } , t ) = \omega _ { i } C ( x , t ) \left ( 1 + \frac { e _ { i } \cdot \vec { u } } { c _ { s } ^ { 2 } } \right ) , & & ( 1 )$$

excluding the depended variable vector 𝐶 ( 𝑥, 𝑡 ) . Since the block diagonal matrix is non-unitary, linear combination of unitaries approach is used, providing two unitary diagonal operators 𝐴 1 and 𝐴 2 . The quantum circuit for the collision part is given in Fig. 3 in between the states | 𝜓 0 ⟩ and | 𝜓 1 ⟩ . The decomposition of the 𝐴 1 and 𝐴 2 gates in the circuit Fig. 3 is given in Fig. 4 involving a phase gate and an 𝑋 gate.

- (3) Propagation: In the propagation step we use the quantum walk [Childs 2009; Low and Chuang 2019] procedure for the streaming of the distributions. In this step the distribution function 𝑓 1 moves to the right with speed 𝑒 1 = 1 and the distribution function 𝑓 2 moves to the left with speed 𝑒 2 = -1. This is achieved by the operators illustrated in the Fig. 3, 𝑅 and 𝐿 for right shift and left shift respectively.
- (4) Macroscopic variables: The last step involves the calculation of the macroscopic variables, density or velocity, this is possible through the point-wise addition of the two quantum states. As the equation [Budinski 2021, Eq. 11] indicates that both of the distribution functions are located in the subsystem controlled by the ancilla qubit | 0 ⟩ 𝑎 , for the point-wise addition at first a swap gate is added between the last qubit 𝑞 𝑛 of the working register 𝑞 and the ancilla qubit 𝑎 . This operation switches the states of the working register controlled by the | 0 ⟩ 𝑎 and | 1 ⟩ 𝑎 in the ancilla register, resulting in the positioning of the sub-state of the second distribution function, controlled by | 0 ⟩ 𝑎 , to the state controlled by | 1 ⟩ 𝑎 . The implementation of this is simple as given in the Fig. 3, just the swap and a Hadamard gate on the ancilla at the end.

The LBM is a time-marching algorithm, and the above outline covers only one time step. It is not detailed in [Budinski 2021] how to connect time steps purely inside a quantum circuit, and we will not attempt to present such a solution here. We use the re-encoding of the initial state at each time step as an example of a hybrid design and study the implementation from this particular angle. Note that following this approach likely destroys the possible speed-up advantages of the quantum algorithm. However, it provides an interesting point of study from the program design perspective, which can be useful even after the time-stepping problem for the QLBM has been resolved. Recent attempts towards efficient time-step concatenation can be found, for example, in [Schalkers and Möller 2024a].

Fig. 3. Quantum circuit to solve the 1D advection-diffusion equation with the lattice Boltzmann method.

<!-- image -->

Fig. 4. Quantum circuit to implement the 𝐴 1 ,𝜆 1 operator.

<!-- image -->

The gate complexity of the QLBM depends on the resolution of the computational domain, as detailed in [Budinski 2021, Section 3.3]. It is highlighted that the encoding step is the most resource-intensive, requiring a significant number of state preparation steps and 𝐶𝑋 gates, which depends on the problem to be solved - in the most general case, this cost is exponential. In the collision step, the complexity is not directly affected by the resolution of the computational domain: increasing the number of qubits to achieve a higher resolution does not change the size of the ancillary register, and the number of multi-qubit gate operations required in the 𝑞 register is constant. The propagation step is influenced by the resolution of the computational domain, and the depth of this subroutine increases logarithmically. The complexity of the propagation step can be optimized for example by using the parallel state shift method [Budinski et al. 2023]. The overall complexity of the algorithm, excluding the encoding step, is determined to be 𝑂 ( log 2 ( 𝛼𝐷 ) , where 𝛼 represents the number of velocity vectors and 𝐷 depends on the domain resolution ( 𝐷 = 2 𝑀 for 𝐷 1 𝑄 2).

## 4 QUANTUM ALGORITHM IMPLEMENTATION IN INTEL QUANTUM SDK

In the form presented above, the quantum lattice Boltzmann algorithm is a hybrid method, although not a variational one. This hybrid property makes it, nevertheless, an interesting example for implementation on platforms that support hybrid classical and quantum computing, such as the Intel Quantum SDK.

In this section, we detail such an implementation and explore the use of modularization with the aim of creating easily reusable and scalable quantum circuits.

## 4.1 Implementation

Due to the complex nature of the quantum lattice Boltzmann algorithm, it becomes essential to employ specific quantum software engineering techniques for the implementation. A general idea is proposed in [Khan et al. 2022, Section 3] about the iterative development cycle and infrastructure for quantum program development: to construct adaptable quantum circuits optimised for execution. In this section, we focus on cycle 2, especially the implementation, the quantum algorithm design cycle, where we adhere to an iterative process for creating and testing various configurations. A modular design methodology is followed for the implementation in the Intel Quantum SDK, similar to one described in [Zhao 2021].

The quantum circuit for the algorithm is provided in Fig. 3. Fig. 6 illustrates how the hybrid time-stepping is performed in the algorithm. The time-step process explained here is specifically for the purpose of implementing the algorithm in the Intel Quantum SDK, and we have chosen it as an example of the hybrid approach in the algorithm design. To implement the time-stepping, the algorithm is divided into three modules, following the modular design methodology [Zhao 2021, Section 5.4], as described below.

- (1) Pre-processing: preparing the initial encoding circuit.
- (2) Solver: solving the four steps discussed in Section 3 in the Intel Quantum SDK.
- (3) Post-processing: extracting the state vector from the Intel Quantum SDK and post-processing the data.

4.1.1 The top-down approach. In this study, we employ the top-down approach to software engineering, adhering to the Single Responsibility Principle. This methodology begins with a high-level design of the overall system, ensuring that each module has a single responsibility. The system is progressively decomposed into smaller, more detailed components, with each module focusing on a specific task. This decomposition promotes modularization, facilitating easier maintenance and scalability.

The Intel Quantum SDK provides a set of quantum logic gates that can be used to create quantum circuits, with each circuit forming a quantum kernel. The goal is to use these quantum kernels and create mutable quantum circuits (adaptable to different configurations) for the different steps involved in the QLBM solver. The hardware accelerator design helps us in the modularization of the quantum circuit in Fig. 3 and to write a quantum kernel for each module, which we will call subcircuits . The different subcircuits are according to the steps involved such as the encoding, collision, propagation and the calculation of macroscopic variables.

The subcircuits might include gates controlled by multiple qubits. All but one of the quantum logic gates available in the Intel Quantum SDK are one- and two-qubit gates, the exception being the three-qubit Toffoli gate. For the implementation of multi-qubit controlled gates, the decomposition method described in the book [Nielsen and Chuang 2010, Section 4.3] is utilized. We call such decomposed gates custom gates . With the help of the basic logic gates and the custom gates, we have the basic building blocks for the subcircuits, minimising the size of the modules.

The flowchart in Figure 5 outlines the structure of a quantum algorithm, divided into three main stages: Pre-processing, Solver, and Post-processing. In the pre-processing stage, input data is processed and encoded. The solver stage includes custom gates and subcircuits, with subcircuits further broken down into collision, propagation, and macroscopic variable calculation. The post-processing stage involves saving results and preparing the state for the next step. Each level of the flowchart provides a clear hierarchical view, from high-level algorithm structure down to specific computational tasks.

The quantum algorithm can be modularized according to the flowchart, allowing for clear separation of tasks and easier management. This ensures each stage is independently developed and tested, facilitating parallel development.

Fig. 5. Illustration of progressive decomposition of the quantum algorithm into smaller implementable modules - specifically for QLBM decomposing into modules such as Custom gates and Subcircuits shown.

<!-- image -->

The hierarchical structure promotes scalability and adaptability, making it suitable for various quantum algorithms by customizing each module to fit specific requirements.

4.1.2 Pre-processing. The quantum lattice Boltzmann method requires that initial values for the advection-diffusion problem be provided in the form of an amplitude vector. These initial values can be arbitrary and may vary according to the specific problem. The Intel Quantum SDK does not include a built-in amplitude encoding algorithm, and this makes it necessary to either to build one with the SDK or use some external amplitude encoding routine. There are several state preparation algorithms documented in the literature, such as the ones referenced in [Shende et al. 2006], [Zhang et al. 2022], and [Zylberman and Debbasch 2023]. To study the hybrid time-stepping implementation on the full-state simulator, we use the Qiskit [Qiskit contributors 2023] state preparation class as an external routine, which is built upon the reverse iterative procedure proposed by [Shende et al. 2006, Section 4].

We implement this step using the Python interface which allows the conversion from OpenQASM to C ++ source code compatible with the Intel Quantum SDK. The flowchart in Fig. 6 illustrates the steps involved in encoding the initial state. Note that any other amplitude encoding routine could just as well be used in the place of the Qiskit algorithm; we have simply chosen it out of convenience.

4.1.3 Solver. This module gathers together the implementation of four algorithmic steps: encoding, collision, propagation, and the calculation of macroscopic variables. Section 4.1.2 outlined the implementation of the encoding step. We then have three steps to implement inside the SDK, and we divide each step into subcircuits with different quantum kernels, allowing for flexibility with the circuit parameters. Additionally, multi-qubit custom gates are generated for these subcircuits. The generation of these subcircuits culminates in the main function which calls all the defined subcircuits, as outlined in Algorithm 2. The subcircuits are formed using the custom gates and the definition of custom gates is given below.

Fig. 6. Overview on the hybrid time-stepping.

<!-- image -->

Initialize backend. In the main function, the initial step involves setting up a backend to act as our quantum hardware. The Intel Quantum SDK provides a full-state simulator, which serves as our window to testing the algorithm in ideal setting.

Once we have access to actual quantum hardware, we can set up and prepare the backend to work with that specific type of quantum hardware. This is really the only significant change we will need to make. The core structure,

## Algorithm 1 Encoding

Require:

initial state = [] , num-qubits, lattice-size

Ensure:

Qasm file with Quantum Circuit

- 1: normalize initial state
- 2: initialize quantum Circuit (qc)
- 3: (qc) use qiskit initialize function with specified num-qubits and initial state
- 4: resulting qc passed to Qiskit transpile
- 5: transpiled circuit converted and saved as OpenQASM file

## Algorithm 2 Solver: Main function

Require:

subcircuits

Ensure:

probabilities

- 1: initialize the backend
- 2: quantum kernel encoding
- 3: quantum kernel collision
- 4: quantum kernel propagation
- 5: quantum kernel macros
- 6: get probabilities and amplitude and save the data

Fig. 7. Decomposition of two-qubit controlled phase gate : CCPHASE

<!-- image -->

algorithms, and methods we are using and discussing can be consistently reused regardless of the backend. Essentially, adjusting to real quantum hardware mainly involves configuring the backend while keeping everything else intact.

Custom gates. The Intel Quantum SDK provides a set of basic logic gates, with the help of these logic gates the different multi-qubit gates can be derived. We use these custom gates as buildings block for the subcircuits.

In the quantum circuit given in Fig. 3, for the collision subcircuit there are two-qubit phase and two-qubit 𝑋 gates. The two-qubit 𝑋 gate or Toffoli is one of the logic gates in the set of given basic logic gates. The two-qubit controlled phase gate can be derived by using one- and two-qubit gates from the gate set. The decompositions illustrated for a two-qubit phase gate in Fig. 7 and for a five-qubit controlled 𝑋 gate in Fig. 8 are based on the general multi-qubit controlled gate decomposition explained in [Nielsen and Chuang 2010, Section 4.3]. The pseudo-code for the two-qubit-controlled phase gate decomposition is given in Algorithm 3. With this formulation we have created a basic building block custom gate named CCPHASE .

Similarly, for the multi-qubit gates, there is the additional requirement of ancilla qubits as shown in the five-qubit example in Fig. 8. The number of ancilla qubits required is one less than the number of control qubits. The pseudo-code for this particular five-qubit decomposition is given in Algorithm 4.

Subcircuits. In the Section 4.1.3 we explained the basic building blocks needed for constructing the subcircuits. This section elucidates the formation of different subcircuits mentioned in Section 3 using custom gates and the basic gates

⊲ Calling the subcircuits

## Algorithm 3 Custom gate: CCPHASE - two-qubit controlled phase gate

Require:

const int (control qubit1,control qubit2, target qubit, phase angle)

Ensure:

basic gate

- 1: function (/q.sc\_u.scantum kernel) CCPHASE(control 1, control 2, target qubit, angle)

- 2: CPhase(qubit control 2, target, angle / 2);

- 3: CX(qubit control 1, qubit control 2);

- 4: CPhase(qubit control 2, target, - angle / 2);

- 5: CX(qubit control 1, qubit control 2);

- 6: CPhase(qubit control 1, target, angle / 2);

- 7: end function

## Algorithm 4 Custom gate: five-qubit controlled 𝑋 gate

Require: const int (control 1 - 5, target, phase angle)

Ensure:

basic gate

- 1: function (/q.sc\_u.scantum kernel) MCX5(control 1 - 5, target qubit, ancilla 1 - 4) ⊲ 5 qubit controlled X gate
- 2: Toffoli(control 1, control 2, ancilla 1)
- 3: Toffoli(control 3, ancilla 1, ancilla 2)
- 4: Toffoli(control 4, ancilla 2, ancilla 3)
- 5: Toffoli(control 5, ancilla 3, ancilla 4)
- 6: CX(ancilla 4, target)
- 7: Toffoli(control 5, ancilla 3, ancilla 4)
- 8: Toffoli(control 4, ancilla 2, ancilla 3)
- 9: Toffoli(control 3, ancilla 1, ancilla 2)
- 10: Toffoli(control 1, control 2, ancilla 1)

## 11: end function

Fig. 8. Decomposition of five-qubit controlled 𝑋 gate (MCX5) using ancilla qubits

<!-- image -->

provided by the SDK. The process of constructing the subcircuits is identical to that of custom gates, the only difference being that the subcircuits are one level higher and make use of the custom gates. It is important to note that the qubit parameters for the gates must be unambiguous, allowing the compiler to differentiate between quantum and classical instructions. Currently, this is a disadvantage when creating generalized quantum custom gates, as it requires precise qubit specification during the design.

## Algorithm 5 Subcircuit: Collision

Require:

```
const int (control qubit1,control qubit2, target qubit, phase angles 1-2) Ensure: collision subcircuit 1: function (/q.sc_u.scantum kernel) collision(control 1, control 2, target qubit, angles 1-2) 2: H(qubit control 1) 3: X(qubit control 1) 4: X(qubit control 2) ⊲ Changing the control value of qubit from 1 to 0 using X gate 5: 6: CCPHASE(control 1, control 2, target qubit, angle 1) 7: Toffoli(control 1, control 2, target qubit) 8: CCPHASE(control 1, control 2, target qubit, angle 1) 9: Toffoli(control 1, control 2, target qubit) 10: 11: X(qubit control 1) 12: 13: CCPHASE(control 1, control 2, target qubit, angle 2) 14: Toffoli(control 1, control 2, target qubit) 15: CCPHASE(control 1, control 2, target qubit, angle 2) 16: Toffoli(control 1, control 2, target qubit) 17: 18: X(qubit control 1) 19: X(qubit control 2) 20: 21: CCPHASE(control 1, control 2, target qubit, -angle 1) 22: Toffoli(control 1, control 2, target qubit) 23: CCPHASE(control 1, control 2, target qubit, -angle 1) 24: Toffoli(control 1, control 2, target qubit) 25: 26: X(qubit control 1) 27: 28: CCPHASE(control 1, control 2, target qubit, -angle 2) 29: Toffoli(control 1, control 2, target qubit) 30: CCPHASE(control 1, control 2, target qubit, -angle 2) 31: Toffoli(control 1, control 2, target qubit) 32: 33: H(qubit control 1) 34: end function
```

The collision subcircuit requires the two-qubit controlled phase gate and a Toffoli with Hadamard gates on either side. The CCPHASE custom gate is used to implement this subcircuit. The subcircuit also contains some controls with a value of zero instead of one. To convert the control value from one to zero, the 𝑋 gate is applied before and after the gate on the control qubit. The subcircuit is outlined in pseudo-code in Algorithm 5.

For the propagation subcircuit, further division into two modules (subcircuits) is possible based on the streaming direction, left and right. As an example we explain the construction of the right shift operator, shown in the case of five working qubits in Fig. 9. This right shift subcircuit consists of three, four, and five qubit-controlled 𝑋 gates. The Intel Quantum SDK enables us to create different custom gates for distinct numbers of control qubits in the general case. Here, various custom gates with MCX5, MCX4, and MCX3 are constructed following the steps provided in Section. 4.1.3. These custom gate quantum kernels are invoked in the subcircuit of the right shift operator. The pseudocode in Algorithm 6 demonstrates this particular implementation.

## Algorithm 6 Subcircuit: five-qubit right shift

Require:

const int (control qubits, target qubits)

Ensure:

right shift subcircuit

- 1: function (/q.sc\_u.scantum kernel) right\_shift(control qubits, target qubits)

- 2: X(qubit control)

- 3: MCX5(control qubits, target)

- 4: MCX4(control qubits, target)

- 5: MCX3(control qubits, target)

- 6: CX(control, target)

- 7: CX(control, target)

- 8: Toffoli(control qubits, target)

- 9: X(qubit control)

- 10: end function

Fig. 9. The right shift operator for a circuit of five working qubits. The last qubit controls on the direction of the shift

<!-- image -->

Constructing the subcircuit and custom gates help us divide the complex algorithm in smaller modules. It helps in writing generalized and expandable programs on a higher level, giving an optimized way for writing quantum circuits. Coupling these subcircuits together as illustrated in Algorithm 2, we complete the whole algorithm for the QLBM example.

4.1.4 Post-processing. Post-processing module consist of extracting the required probabilities from the full-state simulator and deriving the macroscopic concentration values. The process to derive the concentration from the probabilities is given in [Budinski 2021, Section 3.1], in particular the renormalization of the state amplitudes. These values are then fed back to the algorithm as the initial state for the next time step, until the desired time evolution is completed.

## 4.2 Expanding to 2D advection-diffusion and Navier-Stokes equations

The implementation of the 1D quantum algorithm involves formulating custom gates that can be generalized, resulting in a set of generic multi-qubit gates. This approach allows for the reuse of these custom gates in other algorithms, and new custom gates can similarly be formulated to suit other quantum circuits. In this spirit, we briefly outline an expansion to the 2D advection-diffusion [Budinski 2021] and Navier-Stokes [Budinski 2022] algorithms. These algorithms share several similarities with the 1D advection-diffusion, which simplifies their construction.

For the 2D advection-diffusion, which follows a D2Q5 lattice arrangement, the difference is mainly in the collision subcircuit with five multi-qubit controlled operators, one for each velocity. The process of creating these operators is similar to 1D: formulate custom gates (to be specific, a three-qubit controlled phase gate) and utilize them to derive the subcircuit for the 2D collision. Similarly for the propagation step, the circuit is divided into four smaller modules according to the directions of the necessary four shifts. Combining them together similarly to the 1D case forms the propagation subcircuit. Many custom gates from the 1D implementation can be reused but some new gates are also needed.

The implementation of the Navier-Stokes QLBM algorithm involves solving two lattice Boltzmann equations simultaneously as explained in [Budinski 2022]. The collision subcircuit is completely different from the one used in 2D advection-diffusion equation, while the propagation step is carried out twice respectively for the two governing equations. The primary challenge lies in the collision subcircuit, which requires classical calculation of the diagonal elements of the non-unitary matrix and further encoding the matrix using the linear combination of operators approach. The efficient hybrid quantum-classical design is particularly valuable here. The remaining parts of the algorithm can be implemented using the modular approach (custom gates and subcircuits) in the vein of the previous discussion.

## 4.3 Numerical validation of the circuits

In this section we implemented the quantum algorithm for 1D advection-diffusion in the Intel Quantum SDK while demonstrating the use of classical programming principles in quantum programming. Further, for a simple numerical validation of the soundness of the implementation as a physics model, we compare the results after each step with the known analytical solution and the classical lattice Boltzmann method.

The example problem considered is a transport in a channel having a fluid concentration 𝐶 ( 𝑥, 𝑡 ) . A Gauss-like distribution sets the initial concentration 𝐶 ( 𝑥, 0 ) for the problem. The setup is the following:

- (1) A periodic boundary condition.
- (2) Number of lattice sites is a power of 2, the size is chosen so that the distributions do not overlap. We use a minimum of 2 4 = 16 lattice sites.
- (3) For the illustration here, the number of lattice sites is 32 and the initial concentration is given as 𝐶 ( 5 , 0 ) = 𝐶 ( 7 , 0 ) = 0 . 5 and 𝐶 ( 6 , 0 ) = 1 . 0.

In Fig. 10 we visualize the concentrations extracted after time steps 2 and 40. The initial concentration is a triangleshape with maximum concentration at a lattice site 𝑥 = 6 (denoted with a red cross), gradually decreasing towards the edge of the domain. The results show some difference with the analytical solution in the first few time steps. This is not produced by the quantum algorithm itself but is a characteristic of the Boltzmann discretization and the low resolution of the computational grid. To some extent the accuracy of the model could be increased with a finer grid providing a higher resolution and, hence, requiring a greater number of qubits for the circuit implementation. We compared these results with the classical lattice Boltzmann method and they agree within a numerical tolerance of 10 -12 which is ignorable, which confirms that the discrepancies are due to the inherent limitations of the discretization and grid resolution.

Fig. 10. Comparison between the analytical (denoted by a dotted red line with cross mark), QLBM (denoted by a blue line) and the classical lattice Boltzmann method (denoted by green triangle) results for time steps 2 and 40 . The standalone red cross at the top denotes the concentration 𝐶 ( 6 , 0 ) = 1 . 0 as the initial condition.

<!-- image -->

## 5 DISCUSSION: USING CLASSICAL TECHNIQUES ON QUANTUM SDKS

The Intel Quantum SDK differs from other quantum software development kits like Qiskit[Qiskit contributors 2023], PennyLane [Bergholm et al. 2022], and the Munich Quantum Toolkit (MQT) [Quetschlich et al. 2023] in several key aspects, including its target hardware, programming approach, and integration with classical computing resources. In essence, the Intel Quantum SDK is distinct in its integration with the Intel classical computing resources and its focus on high-performance and hybrid quantum-classical computing, leveraging C++ for development. In contrast, Qiskit, PennyLane, and MQT are more flexible in terms of hardware support and focus on accessibility and integration with programming languages like Python, each with its own specialized use cases and target communities. The classical programming principles outlined can be applied to these quantum SDKs with some adjustments to fit the specific features and capabilities. Here is a brief overview of the aforementioned SDKs from this perspective:

- (1) Modularization: All Qiskit, Pennylane and Munich Quantum Toolkit support modular programming, allowing developers to create reusable components. This principle can be applied by structuring quantum programs into functions or classes that can be easily reused and maintained.
- (2) Hybrid design: These SDKs also support hybrid quantum-classical computing, enabling the integration of quantum algorithms with classical pre- and post-processing. Developers can design algorithms that leverage the strengths of both quantum and classical computing.
- (3) Custom gates: While the specific method of creating custom gates may vary between SDKs, the concept remains the same. Developers can define new gates as combinations of existing gates to simplify complex circuit designs.
- (4) Iterative development: The iterative approach to developing and refining quantum algorithms is universally applicable. Developers can iteratively test and optimize their quantum circuits in any SDK to achieve the desired outcomes.

Overall, the principles of classical programming provide a solid foundation for developing quantum algorithms in any quantum SDK, promoting code reusability, maintainability, and efficiency. The key is to adapt these principles to the unique features and constraints of the chosen SDK. In this work, the Intel Quantum SDK has been utilized due to its emphasis on adapting such features to the C++ programming language, particularly crafted to support quantum operations to bridge the gap between traditional programming and the unique requirements of quantum computing [Wu et al. 2023]. In our experience, this integration of classical programming paradigms with quantum functionalities creates a user-friendly and efficient hybrid quantum-classical programming experience, making it accessible to a broad range of users. However, as mentioned above, similar efforts are commonplace in the quantum computing community, and we do not aim to (nor can we) place these efforts in any particular order of preference based on this work.

## 6 SUMMARY

In this paper, we recreated the quantum algorithm for solving the advection-diffusion equation using the lattice Boltzmann method while explaining the principles used to generalize and expand the quantum circuits with the Intel Quantum SDK. It was shown how classical programming techniques, such as iterative development cycles and modular design methods, can be leveraged in quantum programming. The top-down modular design approach helps break down complex quantum algorithms into subcircuits, while the creation of custom gates aids in implementing multi-qubit controlled gates. The creation of generalized circuits in terms of number of qubits and the problem variables benefits from this approach. In particular, these techniques enable one to maintain and reuse quantum kernels in the Intel Quantum SDK. This is an example of how the utilization of classical software development methodologies helps to achieve robust and beneficial quantum software code.

## ACKNOWLEDGMENT

We would especially like to thank and appreciate the entire Intel family for their key support. Among these are Prof. Dr. Anne Matsuura and Dr. Kevin Rasch who were consistently guiding and encouraging us throughout the process. Lastly, T.S. would like to appreciate all his colleagues and teachers for their academic and moral support throughout the journey. This research was partially supported by the Business Finland project 9820/31/2022 QuantumNative Multiphysics.

## REFERENCES

M. Mitchell Waldrop. Feb. 2016. 'The chips are down for Moore's law.' Nature , 530, 7589, (Feb. 2016), 144-147. doi: 10.1038/530144a.

- Seth Lloyd, Giacomo De Palma, Can Gokler, Bobak Kiani, Zi-Wen Liu, Milad Marvian, Felix Tennie, and Tim Palmer. 2020. Quantum algorithm for nonlinear differential equations . (2020). arXiv: 2011.06571 [quant-ph] .
- Peng Qian, Wei-Cong Huang, and Gui-Lu Long. 2019. A quantum algorithm for solving systems of nonlinear algebraic equations . (2019). arXiv: 1903.05608 [quant-ph] .
- Andris Ambainis. 2010. Variable time amplitude amplification and a faster quantum algorithm for solving systems of linear equations . (2010). arXiv: 1010.4458 [quant-ph] .
- Yudong Cao et al.. Aug. 2019. 'Quantum Chemistry in the Age of Quantum Computing.' Chemical Reviews , 119, 19, (Aug. 2019), 10856-10915. doi: 10.1021/acs.chemrev.8b00803.
- Iordanis Kerenidis and Anupam Prakash. Feb. 2020. 'Quantum gradient descent for linear systems and least squares.' Physical Review A , 101, 2, (Feb. 2020), 022316. doi: 10.1103/physreva.101.022316.

Edward Farhi, Jeffrey Goldstone, and Sam Gutmann. 2014. A Quantum Approximate Optimization Algorithm . (2014). arXiv: 1411.4028 [quant-ph] .

- Siddhant Garg and Goutham Ramakrishnan. 2020. Advances in Quantum Deep Learning: An Overview . (2020). arXiv: 2005.04316 [quant-ph] .
- Siddharth Sharma. 2020. QEML (Quantum Enhanced Machine Learning): Using Quantum Computing to Enhance ML Classifiers and Feature Spaces . (2020). arXiv: 2002.10453 [quant-ph] .
- Pradnya Khalate, Xin-Chuan Wu, Shavindra Premaratne, Justin Hogaboam, Adam Holmes, Albert Schmitz, Gian Giacomo Guerreschi, Xiang Zou, and A. Y. Matsuura. 2022. An LLVM-based C++ Compiler Toolchain for Variational Hybrid Quantum-Classical Algorithms and Quantum Accelerators . (2022). arXiv: 2202.11142 [quant-ph] .
- Ljubomir Budinski. Feb. 2021. 'Quantum algorithm for the advection-diffusion equation simulated with the lattice Boltzmann method.' Quantum Information Processing , 20, 2, (Feb. 2021), 57. doi: 10.1007/s11128-021-02996-3.
- Ljubomir Budinski. Aug. 2022. 'Quantum algorithm for the Navier-Stokes equations by using the streamfunction-vorticity formulation and the lattice Boltzmann method.' International Journal of Quantum Information , 20, 02, (Aug. 2022), 2150039. doi: 10.1142/s0219749921500398.

ACM Transactions on Quantum Computing, 15.00 Tejas Shinde, Ljubomir Budinski, Ossi Niemimäki, Valtteri Lahtinen, Helena Liebelt, and Rui Li

Ljubomir Budinski, Ossi Niemimäki, Roberto Zamora-Zamora, and Valtteri Lahtinen. Sept. 2023. 'Efficient parallelization of quantum basis state shift.' Quantum Science and Technology , 8, 4, (Sept. 2023), 045031. doi: 10.1088/2058-9565/acfab7.

Andrew W. Cross, Lev S. Bishop, John A. Smolin, and Jay M. Gambetta. 2017. Open Quantum Assembly Language . (2017). arXiv: 1707.03429 [quant-ph] . A.A.Mohamad. 2019. Lattice Boltzmann Method - Fundamentals and Engineering Applications with Computer codes . Springer-Verlag London Ltd. isbn: 978-1-4471-7422-6.

Merel A. Schalkers and Matthias Möller. 2024a. 'Efficient and fail-safe quantum algorithm for the transport equation.' Journal of Computational Physics , 502, 112816. doi: https://doi.org/10.1016/j.jcp.2024.112816.

Merel A. Schalkers and Matthias Möller. Apr. 2024b. 'Momentum exchange method for quantum Boltzmann methods,' (Apr. 2024). arXiv: 2404.17618 [quant-ph] .

Timm Krueger, Halim Kusumaatmaja, Alexandr Kuzmin, Orest Shardt, Goncalo Silva, and Erlend Magnus Viggen. 2016. The Lattice Boltzmann Method: Principles and Practice . Graduate Texts in Physics. Springer, Cham, Switzerland. isbn: 978-3-319-44647-9.

V.V. Shende, S.S. Bullock, and I.L. Markov. June 2006. 'Synthesis of quantum-logic circuits.' IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems , 25, 6, (June 2006), 1000-1010. doi: 10.1109/tcad.2005.855930.

Andrew M. Childs. 2009. 'Universal Computation by Quantum Walk.' Phys. Rev. Lett. , 102, 180501, 18. doi: 10.1103/PhysRevLett.102.180501.

Guang Hao Low and Isaac L. Chuang. July 2019. 'Hamiltonian Simulation by Qubitization.' Quantum , 3, (July 2019), 163. doi: 10.22331/q-2019-07-12-163. Arif Ali Khan, Mahdi Fahmideh, Aakash Ahmad, Muhammad Waseem, Mahmood Niazi, Valtteri Lahtinen, and Tommi Mikkonen. 2022. 'Embracing

Iterations in Quantum Software: A Vision.' In: Proceedings of the 1st International Workshop on Quantum Programming for Software Engineering (QP4SE 2022). Association for Computing Machinery, Singapore, Singapore, 11-14. isbn: 9781450394581. doi: 10.1145/3549036.3562057.

Jianjun Zhao. 2021. Quantum Software Engineering: Landscapes and Horizons . (2021). arXiv: 2007.07047 [cs.SE] .

Michael A. Nielsen and Isaac L. Chuang. 2010. Quantum Computation and Quantum Infomation . Cambridge University Press, Cambridge. isbn: 978-1-10700217-3.

Xiao-Ming Zhang, Tongyang Li, and Xiao Yuan. Nov. 2022. 'Quantum State Preparation with Optimal Circuit Depth: Implementations and Applications.' Physical Review Letters , 129, 23, (Nov. 2022), 230504. doi: 10.1103/physrevlett.129.230504.

Julien Zylberman and Fabrice Debbasch. 2023. Efficient Quantum State Preparation with Walsh Series . (2023). arXiv: 2307.08384 [quant-ph] .

Qiskit contributors. 2023. Qiskit: An Open-source Framework for Quantum Computing . (2023). doi: 10.5281/zenodo.2573505.

Ville Bergholm et al.. 2022. PennyLane: Automatic differentiation of hybrid quantum-classical computations . (2022). arXiv: 1811.04968 [quant-ph] . Nils Quetschlich, Lukas Burgholzer, and Robert Wille. 2023. 'MQT Bench: Benchmarking Software and Design Automation Tools for Quantum Computing.' Quantum . MQT Bench is available at https://www.cda.cit.tum.de/mqtbench/.

Xin-Chuan Wu, Shavindra Premaratne, and Kevin Rasch. 2023. 'Invited Paper: Introduction to Hybrid Quantum-Classical Programming Using C++ Quantum Extension.' In: 2023 IEEE/ACM International Conference on Computer Aided Design (ICCAD) , 1-6. doi: 10.1109/ICCAD57390.2023.10323946.

## APPENDIX

## A LINEAR COMBINATION OF UNITARY MATRIX APPROACH

The linear combination of unitaries (LCU) approach is a technique used in quantum computing to efficiently simulate quantum circuits and algorithms. This approach involves representing a quantum operation as a linear combination of elementary unitary operations. Unitary operations are fundamental to quantum mechanics and represent reversible transformations on quantum states.

Mathematically, this can be expressed as follows:

Suppose we have a quantum operation 𝑈 that we want to represent as a linear combination of unitaries 𝑈 1 , 𝑈 2 , . . . , 𝑈 𝑛 . Then, we can write:

$$U = \sum _ { i = 1 } ^ { n } c _ { i } U _ { i } \\$$

where 𝑐 𝑖 are complex coefficients representing the proportions of each unitary operation 𝑈 𝑖 in the combination. Here is a more detailed breakdown:

- 𝑈 : The target quantum operation we want to represent.
- 𝑈 1 , 𝑈 2 , . . . , 𝑈 𝑛 : Elementary unitary operations or a set of predefined unitaries.

- 𝑐 1 , 𝑐 2 , . . . , 𝑐 𝑛 : Complex coefficients determining the contribution of each unitary operation in the linear combination.

In practice, determining the coefficients 𝑐 𝑖 can involve various techniques such as optimization algorithms, theoretical analysis, or experimental measurements.

LCU is particularly useful in quantum computing for efficiently simulating quantum circuits and algorithms, as it allows for the decomposition of complex quantum operations into simpler unitary operations, making simulations more tractable and scalable.

Let's consider the example of a single-qubit quantum operation, the Hadamard gate ( 𝐻 gate). The Hadamard gate is a fundamental gate in quantum computing that creates superposition. It can be represented by the following matrix:

$$H = \frac { 1 } { \sqrt { 2 } } \begin{bmatrix} 1 & 1 \\ 1 & - 1 \end{bmatrix}$$

Now, let's decompose the Hadamard gate into a linear combination of elementary unitary operations. We can represent the Hadamard gate as a linear combination of the Pauli matrices, which are elementary unitary operations. The Pauli matrices are denoted as:

$$\sigma _ { x } & = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} \\ \sigma _ { y } & = \begin{bmatrix} 0 & - i \\ i & 0 \end{bmatrix} \\ \sigma _ { z } & = \begin{bmatrix} 1 & 0 \\ 0 & - 1 \end{bmatrix} \\ \intertext { a l i n e r c o m b i n a t } \ s a l i n e r c o m b i n a t$$

Now, we can express the Hadamard gate ( 𝐻 ) as a linear combination of the Pauli matrices:

$$H = \frac { 1 } { \sqrt { 2 } } \sigma _ { x } + \frac { 1 } { \sqrt { 2 } } \sigma _ { z }$$

This representation shows that the Hadamard gate can be decomposed into a linear combination of the Pauli matrices 𝜎 𝑥 and 𝜎 𝑧 .