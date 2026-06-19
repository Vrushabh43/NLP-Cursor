## Taking the Road Less Traveled: Solving the One-Dimensional Quantum Oscillator using the Parabolic-Cylinder Equation

M´ at´ e Garai 1 , Douglas A. Barlow 1

1 Department of Physics, The University of the South, Sewanee, TN 37383

## Abstract

The single well 1D harmonic oscillator is one of the most fundamental and commonly solved problems in quantum mechanics. Traditionally, in most introductory quantum mechanics textbooks, it is solved using either a power series method, which ultimately leads to the Hermite polynomials, or by ladder operators methods. We show here that, by employing one straightforward variable transformation, this problem can be solved, and the resulting state functions can be given in terms of parabolic cylinder functions. Additionally, the same approach can be used to solve the Schr¨ odinger equation for the 1D harmonic oscillator in a uniform electric field. In this case, the process yields two possible solutions. One is the well-known result where the 1D oscillator eigenvalues are reduced by a frequency-dependent term, which can have any positive value. The other is where the field term is restricted to be an integer and the eigenvalues are in the same form as for the field-free case. Additionally, we show how the results can be used to create a harmonic approximation for the bound states of a Lennard-Jones potential.

Keywords: Harmonic Oscillator; Parabolic Cylinder function; Weber-Hermite polynomial; Hermite polynomial

## 1 Introduction

The single well 1D harmonic oscillator is one of the most fundamental and commonly solved problems in undergraduate quantum mechanics courses. Traditionally, in most introductory quantum mechanics textbooks, the governing differential equation is solved analytically using a power series method, which ultimately leads to the Hermite polynomials, or algebraically using ladder operators. In fact, one or both of these methods were the exclusive approach taken in the more than thirty texts we reviewed for this study where the solution for the 1D quantum oscillator was given and discussed [1-39]. However, we demonstrate here a less laborious route to the complete solution for this problem. By employing one straightforward variable transformation, the governing equation can be written in the form of a parabolic cylinder equation, and the resulting state functions are thus given in terms of the parabolic cylinder functions. In the list of texts mentioned above, only Merzbacher [22] utilized a parabolic cylinder equation solution for any oscillator problem, and this is the double harmonic oscillator, not the single well 1D oscillator that we consider here.

Additionally, a similar approach can be used to solve the Schr¨ odinger equation for the 1D harmonic oscillator in a uniform electric field. In this case, the resulting parabolic cylinder equation reveals the possibility of two solutions. One is the well-known result where the 1D oscillator eigenvalues are reduced by a frequency-dependent term that can have any positive value [17]. The other is where the field term is restricted to be an integer, and the eigenvalues are more like those for the field-free case.

In the next section, steps are given for arriving at the solution for the 1D harmonic oscillator in terms of parabolic cylinder functions. In the subsequent section, the case where the oscillator is within a uniform electric field is considered. Again, steps leading to the solution in terms of parabolic cylinder functions are given. Finally, we demonstrate how the results for the oscillator in a uniform electric field can be used to approximate the bound states of a Lennard-Jones potential.

## 2 Solutions to the Quantum Harmonic Oscillator

We consider the classical potential energy, V , for the one dimensional (1D) harmonic oscillator as, V = 1 2 µω 2 x 2 , where µ is reduced mass, k is the force constant and x is position. It is useful to write the force constant in terms of the oscillator's natural frequency ω as ω = √ k/µ . With this substitution, the full Hamiltonian is written as

$$\hat { H } = - \frac { \hbar { ^ } { 2 } } { 2 \mu } \frac { d ^ { 2 } } { d x ^ { 2 } } + \frac { 1 } { 2 } m \omega ^ { 2 } x ^ { 2 } \ .$$

Therefore, the time-independent Schr¨ odinger equation for the 1D harmonic oscillator is:

$$- \frac { \hbar { ^ } { 2 } } { 2 \mu } \frac { d ^ { 2 } } { d x ^ { 2 } } \psi + \frac { 1 } { 2 } \mu \omega ^ { 2 } x ^ { 2 } \psi = E \psi \ .$$

After a bit of manipulation this becomes

$$\frac { \hbar { } } { 2 \mu \omega } \frac { d ^ { 2 } } { d x ^ { 2 } } \psi + \left ( \frac { E } { \hbar { \omega } } - \frac { \mu \omega } { 2 \hbar { } } x ^ { 2 } \right ) \psi = 0 \ .$$

The parabolic cylinder differential equation is of the form [40]:

$$\frac { d ^ { 2 } y } { d z ^ { 2 } } + \left ( n + \frac { 1 } { 2 } - \frac { 1 } { 4 } z ^ { 2 } \right ) y = 0 \ ,$$

where n is an integer. Eq. (3) can be transformed into the form of Eq. (4) with the aid of the following substitution:

$$z = \sqrt { \frac { 2 \mu \omega } { \hbar } } x \, .$$

$$\frac { d ^ { 2 } \psi } { d x ^ { 2 } } = \frac { 2 \omega \mu } { \hbar } \frac { d ^ { 2 } \psi } { d z ^ { 2 } } \ .$$

Using Eqs (6) and (5) in Eq. (3) leads to

$$\frac { d ^ { 2 } \psi } { d z ^ { 2 } } + \left ( \frac { E } { \hbar { \omega } } - \frac { z ^ { 2 } } { 4 } \right ) \psi = 0 \ . \\$$

As we are expecting quantized energy levels we set E = E n and let

$$E _ { n } = \hbar { \omega } ( n + 1 / 2 ) \ .$$

With this substitution, Eq. (7) is in the form of the parabolic cylinder equation so that the state functions ψ n are given by the complete orthogonal set of solutions for Eq. (7), the parabolic cylinder functions , { D n ( z ) } for n = 0 , 1 , 2 , . . . . The state functions for the 1D oscillator are then:

$$\psi _ { n } = N _ { n } \, D _ { n } \left ( \sqrt { \frac { 2 \mu \omega } { \hbar } } x \right ) \, , \\$$

where N n is a normalization constant.

Not surprisingly, the functions, D n can be written in terms of the Hermite polynomials, H n as [40]

$$D _ { n } ( z ) = \frac { 1 } { ( \sqrt { 2 } ) ^ { n } } e ^ { - z ^ { 2 } / 4 } H _ { n } \left ( \frac { z } { \sqrt { 2 } } \right ) \ , \\ n o t r u o \, f o t \, h o r m i t o \, p o l u m i o l _ { \ } r o t r i t i o \, n \, t o \, n o p n o t i v o \, i n t o g r a s$$

which, due to the nature of the Hermite polynomials, restricts n to non-negative integers. Using the Rodrigues formula for the Hermite polynomials, [41], we can write an effective Rodrigues formula for the parabolic cylinder functions as

$$D _ { n } ( z ) = ( - 1 ) ^ { n } e ^ { - \frac { z ^ { 2 } } { 4 } } \frac { d ^ { n } } { d z ^ { n } } e ^ { - \frac { z ^ { 2 } } { 2 } } \ .$$

The first six parabolic cylinder functions are listed in Table 1. A few of these functions are plotted in Figure 1.

The normalization constant can now be found using the following identity from Reference [42]:

$$\int _ { - \infty } ^ { \infty } e ^ { - x ^ { 2 } } H _ { n } ^ { 2 } ( x ) d x = 2 ^ { n } n ! \sqrt { \pi } \ .$$

From Eq. (5) one finds that Using Eqs. (9) and (10) we can write that

| Table   | 1: The first six parabolic cylinder functions D n ( z   |
|---------|---------------------------------------------------------|
|         | n D n ( z )                                             |
|         | 0 e - z 2 / 4                                           |
|         | 1 e - z 2 / 4 z                                         |
|         | 2 - e - z 2 / 4 (1 - z 2 )                              |
|         | 3 e - z 2 / 4 z ( z 2 - 3)                              |
|         | 4 - e - z 2 / 4 (6 z 2 - 3 - z 4 )                      |
|         | 5 e - z 2 / 4 z (15 10 z 2 + z 4 )                      |

Figure 1: The first four parabolic cylinder functions.

<!-- image -->

$$\langle \Psi _ { n } | \Psi _ { n } \rangle = \frac { N _ { n } } { 2 ^ { n } } \int _ { - \infty } ^ { \infty } e ^ { - z ^ { 2 } / 2 } H _ { n } ^ { 2 } \left ( \frac { z } { \sqrt { 2 } } \right ) d z = 1 \ . \\$$

Letting z be given by Eq. (5) in Eq. (13), and using Eq. (12) to evaluate the integral, leads to

Therefore, the complete set of state functions for the quantum harmonic oscillator is expressed in terms of parabolic cylinder functions as:

$$N _ { n } = \frac { 1 } { \sqrt { n ! } } \left ( \frac { \mu \omega } { \hbar { \pi } } \right ) ^ { 1 / 4 } \, . \\ \text {set of state functions for the quantum harmonic oscillator is ex-}$$

$$\psi _ { n } ( x ) = \frac { 1 } { \sqrt { n ! } } \left ( \frac { \mu \omega } { \hbar { \pi } } \right ) ^ { 1 / 4 } D _ { n } \left ( \sqrt { \frac { 2 \mu \omega } { \hbar { } } } x \right ) \ . \\$$

Using these state functions, the well-known energy eigenvalues and position expectation value for this problem can be computed. That is,

$$\hat { H } | \Psi _ { n } \rangle = \hbar { \omega } ( n + 1 / 2 ) \Psi _ { n } \ ,$$

and

$$\langle \Psi _ { n } | x | \Psi _ { n } \rangle = 0 \ .$$

## 3 The Harmonic Oscillator in a Uniform Electric Field:

The method of solution using parabolic cylinder functions is also useful when the oscillator Hamiltonian involves an additional first-order term. The physical interpretation of this case might involve an oscillator placed in a uniform electric field of magnitude E . In this case, the Hamiltonian is of the form:

$$\hat { H } = - \frac { \hslash ^ { 2 } } { 2 \mu } \frac { d ^ { 2 } } { d x ^ { 2 } } + \left ( \frac { 1 } { 2 } \mu \omega ^ { 2 } x ^ { 2 } + q \mathcal { E } x \right ) \ . \\$$

The 1D time-independent Schr¨ odinger equation is then written as:

$$- \frac { \hslash ^ { 2 } } { 2 \mu } \frac { d ^ { 2 } \psi } { d x ^ { 2 } } + \left ( \frac { 1 } { 2 } \mu \omega ^ { 2 } x ^ { 2 } + q \mathcal { E } x - E \right ) \psi = 0 \ .$$

Using the substitution from Eq. (5), which we now label as u = √ (2 µω/ ¯ h ) x , in Eq. (19) yields

$$- \hbar { \omega } \frac { d ^ { 2 } \psi } { d u ^ { 2 } } + \left ( \frac { \hbar { \omega } } { 4 } u ^ { 2 } + q \mathcal { E } \sqrt { \frac { } { 2 \omega \mu } } u - E \right ) = 0 \, .$$

Dividing this by -¯ hω we arrive at the following:

$$& \frac { d ^ { 2 } \psi } { d u ^ { 2 } } + \left ( \frac { E } { \hbar { \omega } } - \frac { u ^ { 2 } } { 4 } - \frac { q \mathcal { E } } { \sqrt { 2 \mu \hbar { \omega } ^ { 3 } } } u \right ) = 0 \, . \\ \intertext { t o f i n e the f o l l i w n g c o n t a n t \colon }$$

It is useful now to define the following constant:

Using this in Eq. (21) gives

$$\gamma = \frac { q \mathcal { E } } { \sqrt { 2 \mu \hbar { \omega } ^ { 3 } } } \cdot$$

$$\frac { d ^ { 2 } \psi } { d u ^ { 2 } } + \left ( \frac { E } { \hbar { \omega } } - \frac { u ^ { 2 } } { 4 } - \gamma u \right ) = 0 \ . \\$$

Now, we apply the additional variable transformation, z = u + 2 γ , so that Eq. (23) is converted into the form of the parabolic cylinder differential equation

$$\frac { d ^ { 2 } \psi } { d z ^ { 2 } } + \left ( \frac { E } { \hbar { \omega } } - \frac { z ^ { 2 } } { 4 } + \gamma ^ { 2 } \right ) \psi = 0 \, . \\$$

We are presented with two choices on writing the solution for Eq. (24). First, consider the solution where

$$E _ { n } = \hbar { \omega } ( n + 1 / 2 - \gamma ^ { 2 } ) \ .$$

Here we see that the energy levels of the harmonic oscillator will be shifted by the amount γ 2 due to the influence of the electric field. This is, of course, the classic result that can also be obtained via perturbation methods [17]. The normalized state functions in the case, which we label as Ψ n,γ 2 , are

$$\Psi _ { n , \gamma ^ { 2 } } ( x ) = N _ { n } D _ { n } \left ( \sqrt { \frac { 2 \mu \omega } { \hbar } } x + 2 \gamma \right ) \, .$$

Following the steps in the previous section, one can confirm that the normalization constant in this case is again given by Eq. (14). One can show that eq. (26) does indeed give the eigenfunctions for the eigenvalues given by Eq. (25).

However, it is interesting to consider a second solution for this problem afforded by Eq. (24). Here, we let

$$E _ { m } = \hbar { \omega } ( m + 1 / 2 ) \ ,$$

where m is an integer. Inserting this into Eq. (24) gives

$$\frac { d ^ { 2 } \psi } { d z ^ { 2 } } + \left ( m + \frac { 1 } { 2 } - \frac { z ^ { 2 } } { 4 } + \gamma ^ { 2 } \right ) \psi = 0 \, . \\$$

So, it must be that m + γ 2 ≥ 0. We define the integer k where k = m + γ 2 and k = 1 , 2 , 3 , . . . and thus γ 2 = 1 , 2 , 3 , . . . and then m = -γ 2 , γ 2 -1 , γ 2 -2 . . . . With this substitution, Eq. (28) is in the form of Eq. (4) and thus has as solutions the following state functions, which we label as Ψ m + γ 2 ,

$$\Psi _ { m + \gamma ^ { 2 } } = N _ { n } D _ { m + \gamma ^ { 2 } } \left ( \sqrt { \frac { 2 \mu \omega } { \hbar } } x + 2 \gamma \right ) \, ,$$

where N n is again given by Eq. (14). Thus for any m in the range of -γ 2 to any greater integer, Eq. (29) gives the eigenfunctions for the eigenvalues of Eq. (27) when γ 2 is a positive integer. That is,

for any γ 2 = 1 , 2 , 3 , . . . . So, it can be seen that the choice for the energy given by Eq. (27) filters out the values for E n in in Eq. (25) for cases where γ 2 is a positive integer.

$$\hat { H } | \Psi _ { m + \gamma ^ { 2 } } \rangle = \hbar { \omega } ( m + 1 / 2 ) | \Psi _ { m + \gamma ^ { 2 } } \rangle \ , \\ S _ { 0 } \ \dot { \cdot } _ { m + \gamma } = 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 ,$$

## 4 Discussion and Application

The solution for the harmonic oscillator described in the previous section, where the eigenvalues are given by Eq. (27), gives nothing new as these solutions are a subset of those for the more general situation where γ can have any positive value. However, this solution does awaken us to the fact that this model can be used when the values of γ 2 are restricted to the positive integers.

It is important to note that the effect of the electric field on the oscillator is to introduce negative energies to the eigenvalue spectrum. With this in mind, we can use the solution for the case where γ 2 is a positive integer to create an oscillator model for some other type of bound state potential for which the Schr¨ odinger equation might be difficult to solve. As an example, we consider the classic Lennard-Jones (L-J) potential, U ( r ), which is often used to describe bonding between two noble element atoms separated by a distance r :

Figure 2: Curves for a L-J potential well and its harmonic oscillator approximation with some of the energy levels denoted. ϵ and σ are set to 1 and k = 70 in arbitrary units.

<!-- image -->

$$U ( r ) = 4 \epsilon \left [ ( \sigma / r ) ^ { 1 2 } - ( \sigma / r ) ^ { 6 } \right ] \, . \\ \text {One} \, L _ { - } J \text { parameters.} \, \text { We demonstrate here, how to use the results of the
approximatum to the bound states of this potential as a harmonic oscillator}$$

Here ϵ and σ are the L-J parameters. We demonstrate here, how to use the results of the previous section to approximate the bound states of this potential as a harmonic oscillator. This process is facilitated by the fact that γ 2 can be restricted to integer values. The curve for a L-J potential, and an approximating harmonic oscillator curve are depicted in Figure 2.

The well known energy minimum for the L-J potential is simply -ϵ . To relate this to the harmoinc oscillator in the electric field we find the minimum energy for the potential in the Hamiltonian of Eq. (18). One finds by differentiation, and setting the result to zero, that this occurs when x = -q E / ( µω 2 ). Inserting the value for x back into the oscillator potential yields the energy minimum E min :

$$E _ { \min } = - \frac { ( q \mathcal { E } ) ^ { 2 } } { \mu \omega ^ { 2 } } \ .$$

Setting this equal to ϵ and using Eq. (22) we find that

$$\hbar { \omega } = \frac { \epsilon } { \gamma ^ { 2 } } \, .$$

Now, let γ 2 be the total number of bound states and m = -γ 2 , -γ 2 +1 , -γ 2 +2 , · · · -1 so that the energy levels of our approximating oscillator become

$$E _ { m } = \frac { \epsilon } { \gamma ^ { 2 } } \left ( m + 1 / 2 \right ) \, .$$

The minimum of the L-J potential can be shown to occur at r = 2 1 / 6 σ , so that the state functions from the previous section can be applied here by the transformation of x = r -2 1 / 6 σ . This system would have the selection rules for the harmonic oscillator [43], with an energy difference between adjacent levels of ϵ/γ 2 so that one could examine experimental data for the vibrational spectrum of the known diatomic and, from this, establish an estimate for γ 2 .

## 5 Conclusion:

The one-dimensional quantum harmonic oscillator is written and solved in terms of parabolic cylinder function by employing a few simple substitutions. The solution provides a quicker, more direct method for solving the simple quantum harmonic oscillator and also for the harmonic oscillator within a uniform electric field. The energy eigenvalues, as well as the stationary states of both systems, can be evaluated with minimal computation.

These results alert one to the fact that the oscillator in a uniform electric field can be considered for the cases where the field shifts the energy spectrum by an integer. From this, we proposed and gave a simple example of how the known solution for the oscillator in the uniform field model can be used to approximate the bound states of an L-J potential. Though we described the method of approximating an L-J potential here, this method could be used for any one-dimensional potential where the equilibrium position and minimum energy are known.

## References

- [1] E. S. Abers, Quantum Mechanics , (Pearson Education Inc., Upper Saddle River, NJ, 2004).
- [2] G. Auletta, M. Fortunato and G. Parisi, Quantum Mechanics , (Cambridge University Press, Camgridge, UK, 2009).
- [3] Y. B. Band and Y. Avishai, Quantum Mechanics , (Academic Press, Amsterdam, Netherlands, 2013).
- [4] D. B. Beard and G. B. Beard, Quantum Mechanics with Applications , (Allyn and Bacon Inc., Boston, MA, 1970).
- [5] D. Bohm, Quantum Theory , (Dover Publications Inc., Mineola, NY, 1951).
- [6] R. Bl¨ umel, Foundations of Quantum Mechanics , (Jones and Bartlett Publishers, London, UK, 2010).
- [7] C. Cohen-Tannoudji, B. Diu. and F. Laloe, Quantum Mechanics Vol. 1 , (John Wiley and Sons, New York, NY, 1977).
- [8] P. A. M. Dirac, The Principles of Quantum Mechanics, 4 th edition , (Oxford University Press, London, UK, 1958).
- [9] R. Eisberg, R. Resnick, Quantum Physics of Atoms Molecules, Solids, Nuclei and Particles 2 nd edition , (John Wiley and Sons, New York, NY, 1985).
- [10] M. D. Fayer, Elements of Quntum Mechanics , (Oxford University Press, New York, NY, 2001).
- [11] P. Fong, Elementary Quantum Mechanics , (World Scientific, Singapore, 2005).
- [12] A. P. French and E. F. Taylor, An Introduction to Quantum Physics , (W. W. Norton and Co., New York, NY, 1978).
- [13] S. Gasiorowicz, Quantum Physics , (John Wiley and Sons, New York, NY, 1974).
- [14] D. J. Griffiths, Introduction to Quantum Mechanics, 2 nd edition , (Pearson Prentice Hall Inc., Upper Saddle River, NJ, 2005).
- [15] K. Gottfried and T. -M. Yan, Quantum Mechanics: Fundamentals, 2 nd edition , (Springer-Verlag, New York, NY, 2003).
- [16] W. V. Houston, Principles of Quantum Mechanics , (Dover Publications Inc., New York, NY, 1959).
- [17] C. S. Johnson and L. G. Pedersen, Problems and Solutions in Quantum Chemistry and Physics , (Addison-Wesley Publishing Co., Reading, MA, 1976).

- [18] K. Konishi and G. Paffuti, Quantum Mechanics, a New Introduction , (Oxford University Press, Oxford, UK, 2009).
- [19] D. F. Lawden, The Mathematical Principles of Quantum Mechanics , (Methuen &amp; Co. LTD, London, 1967).
- [20] R. L. Liboff, Introductory Quantum Mechanics , (Addison-Wesley Publishing Co., Reading, MA, 1992).
- [21] F. Mandel, Quantum Mechanics, 2 nd edition , (Academic Press Inc., London, 1957).
- [22] E. Merzbacher, Quantum Mechanics, 3 rd edition , (John Wiley and Sons, New York, NY, 1998).
- [23] M. A. Morrison, Understanding Quantum Physics , (Prentice-Hall, Inc., Englewood Cliffs, NJ, 1990).
- [24] M. A. Morrison, T. L. Estle and N. F. Lane, Quantum States of Atoms, Molecules, and Solids. , (Prentice-Hall, Inc., Englewood Cliffs, NJ, 1976).
- [25] D. Park, Introduction to the Quantum Theory , (McGraw-Hill Book co. Inc., New York, NY, 1964).
- [26] L. Pauling and E. B. Wilson, Introduction to Quantum Mechanics , (McGraw-Hill Book co. Inc., New York, NY, 1959).
- [27] P. J. E. Peebles, Quantum Mechanics , (Princeton University Press, Princeton, NJ, 1992).
- [28] A. C. Phillips, Introduction to Quantum Mechanics , (John Wiley and Sons, West Sussex, England, 2003).
- [29] J. L. Powell and B. Crasemann, Quantum Mechanics , (Addison-Wesley Publishing Co., Reading, MA, 1961).
- [30] A. I. M. Rae, Quantum Mechanics, 5 th edition , (Taylor &amp; Francis, New York, NY, 2008).
- [31] R. W. Robinett, Quantum Mechanics, 2 nd edition , (Oxford University Press, Oxford, UK, 2006).
- [32] V. Rojansky, Introductory Quantum Mechanics , (Prentice-Hall, Inc., Englewood Cliffs, NJ, 1959).
- [33] J. J. Sakurai, Modern Quantum Mechanics, revised edition , (Addison-Wesley Publishing Co., Reading, MA, 1994).
- [34] D. S. Saxon, Elementary Quantum Mechanics , (Holden-Day, San Francisco, CA, 1968).
- [35] R. Scherrer, Quantum Mechanics, an Accessible Introduction , (Pearson Education, San Francisco, CA, 2006).

- [36] R. Shankar, Principles of Quantum Mechanics , (Plenum Press, New York, NY, 1980).
- [37] H. L. Strauss, Quantum Mechanics an Introduction , (Prentice-Hall, Inc., Englewood Cliffs, NJ, 1968).
- [38] J. S. Townsend, A Modern Approach to Quantum Mechanics , (University Science Books, Sausalito, CA, 2000).
- [39] N. Zettili, Quantum Mechanics , (John Wiley and Sons, West Sussex, England, 2001).
- [40] H. Bateman, Higher Transcendental Functions, Vol. 2 , (McGraw-Hill Book co. Inc., New York, NY, 1953, p. 116).
- [41] W. W. Bell, Special Functions for Scientists and Engineers , (Dover Publications Inc., Mineola, NY, 1969, p. 158).
- [42] N. N. Lebedev, Special Functions &amp; Their Applications , (Dover Publications Inc., Mineola, NY, 1972, p. 66).
- [43] F. Pilar, Elementary Quantum Chemistry, 2 nd edition , (Dover Publications Inc., Mineola, NY, 1990, p. 88).