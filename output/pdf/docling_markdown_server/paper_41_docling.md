## Machine learning for predicting control landscape maps of quantum molecular dynamics: Laser-induced three-dimensional alignment of asymmetric top molecules

```
Tomotaro Namba 1)  and Yukiyoshi Ohtsuki* Department of Chemistry, Graduate School of Science, Tohoku University 6-3 Aramaki Aza-Aoba, Aoba-ku, Sendai 980-8578, Japan 1) present address Nuclear Science and Engineering Center, Japan Atomic Energy Agency 2-4 Shirakata, Tokai-mura, Naka-gun, Ibaraki 319-1195, Japan * Corresponding author: yukiyoshi.ohtsuki.d2@tohoku.ac.jp Tel/fax: +81-22-795-7725
```

(August 30, 2024)

## Abstract

Machine learning for predicting control landscape maps of full quantum molecular dynamics is examined  through  a  case  study  of  the  laser-induced  three-dimensional  (3D)  alignment  of asymmetric top molecules, an essential technique for observing and/or manipulating molecular dynamics in a molecule-fixed frame.    We consider the 'prolate-type' asymmetric top molecules with  the  asymmetry  parameters 1 0    and  the 2 C v symmetry  in  the  low-temperature limiting case, which are aligned by using mutually orthogonal linearly polarized double laser pulses.    The  landscape  map  for  each  molecule  consists  of  6000  pixels,  each  pixel  of  which represents the maximum degree of alignment achieved by each set of control parameters.    After examining ways to deal with the markedly different molecular parameters in a unified manner for suitably training a convolutional neural network (CNN) model, we train the CNN model by using 55 training sample molecules to predict the control landscape maps of 35 test sample molecules with reasonably high accuracy.    As the predicted landscape maps provide a big picture of the alignment  control,  we  show,  for  example,  that  the  double  pulse  control  scheme  is  especially effective for a molecule having a polarizability component that is much larger in value than the other two components.

## I. INTRODUCTION

Our  capability  to  simulate  full  quantum  molecular  dynamics  is  severely  limited  by quantum correlations due to the many-body interactions even when the initial states are localized because the quantum entanglements spread over the entire systems with time.    Machine learning (ML) approaches have attracted immense attention as a means to overcome these difficulties [13].    It  would be convenient to classify the ML approaches into three categories.    In the first category, ML approaches are applied to determine molecular properties such as potential energy surfaces and forces while avoiding computationally expensive electronic structure calculations [4-6] typically used  in  model-based  simulations. In the second  category, variational representations of quantum states such as neural-network quantum states are proposed on the basis  of  the  ansatz  that  tractable  subspaces  of  total  Hilbert  spaces  may  represent  many-body wavefunctions [7-10].    Some studies [10] consider the time-dependent expectation values of the set of observables instead of the wavefunctions because they can be straightforwardly connected to the experimental measurements.    ML approaches in the second category are used to predict the excitation energy transfer , e.g., in the Fenna-Matthews-Olson (FMO) complex [11-15], the optimal control design [16,17], the landscapes of the cost functions [18] and so on.

There is third category of ML approaches that provide computationally effective tools for  quantum molecular  dynamics simulation.    In this category, we simulate the dynamics by exactly  solving  the  Schrödinger  equation  at  the  expense  of  high  computational  costs.    Vast computer  resources,  albeit  not  practically  feasible,  are  required  to  simulate  the  dynamics  of various molecules in a unified manner, e.g., to find the mechanisms and/or the rules of thumb for valid control across the molecules.    The purpose of the present study is to consider one example through a case study of laser-induced three-dimensional (3D) molecular alignment [19-22].    To be  specific,  we  examine  ML  approaches  for  predicting  control  landscape  maps  of  the  3D

alignment control, i.e., the full quantum molecular dynamics.    Alignment control is essential to realize further control of molecular dynamics and/or measurements in the molecule-fixed frame.

To achieve molecular alignment in the field-free condition, we  often utilize polarizability interactions induced by mildly intense non-resonant laser pulses, taking advantage of  the  controlled  intense electric fields  of the laser pulses [23].    Because it is obvious that a higher degree of 3D alignment is better for applications, several control schemes for effective 3D alignment of asymmetric molecules have been proposed [24-34].    One control scheme proposes the  use  of  a  train  of  elliptically  polarized  laser  pulses  with  optimized  ellipticities,  which  are suitably adjusted to the polarizability components of the target molecules [24,25].    In another control scheme, a pair of mutually orthogonal linearly polarized laser pulses is adopted, in which the first pulse 1D aligns the most polarized molecular axis along the polarization vector and the second orthogonal pulse interacts with the other molecular axes at the timing when the torque exerted  on  the  first  molecular  axis  is  minimized  [26,27].    In  our  previous  study  [33],  we considered  the  laser-induced  3D  alignment  of  SO2,  a  typical  molecule  in  proof-of-principle experiments and theoretical studies, and derived the mutually orthogonal pulse train as the optimal solution by using the optimal control theory.    We also showed that the optimal pulse train can be approximated  by  the  mutually  orthogonal  double  pulses  while  reasonably  maintaining  the effectiveness of the 3D alignment control.    All of the above-mentioned studies focused on their own 'specific' molecules, intending to clarify some general features of the alignment control through specific examples.    It would be, thus, natural to consider the 3D alignment control of a certain class of asymmetric top molecules in a unified manner by resolving computational-cost issues with, e.g., convolutional neural network (CNN) models.

In  the  present study,  assuming alignment control with a pair of mutually orthogonal linearly polarized laser pulses, we apply the control scheme to 'prolate-type' asymmetric top molecules with 2 C v symmetry with the aim of examining how much we could increase their degrees  of  3D  alignment  in  the  control  scheme,  clarifying  the  molecule-dependent  control mechanisms,  and  so  on.    For  these  purposes,  we  focus  on  control  landscape  maps  [35-37] defined  by  the  maximum  degrees  of  3D  alignment  as  a  function  of  control  parameters  [37]. Assuming induced-dipole interactions, we specify the asymmetric top molecules by using sets of three rotational constants and polarizability tensors, the values of which are widely distributed over  2-3  orders  of  magnitude  depending  on  the  molecule.    In  addition,  the  asymmetric  top molecules are not uniformly distributed in the 'molecular space' in which the CNN model is trained.    Therefore,  the  training  efficiency  is  severely  reduced  and  CNN model  performance deteriorates.    Our purpose is to examine how to overcome these difficulties by actively utilizing dimensionless molecular and control parameters and by introducing 'artificial' molecules.    We show that the present CNN model predicts the control landscape maps with reasonable accuracy, whereby the general features of the alignment control can be semi-quantitatively examined.

This manuscript is organized as follows.    In Sec. II, we briefly summarize a numerical method to solve the laser-induced rotational dynamics and define the control landscape maps in a general way.    After introducing a class of asymmetric top molecules considered in the present study, we explain how to prepare samples suitable for CNN model training.    In Sec. III, we show and discuss the results, and in Sec. IV, we summarize the present study.

## II. Theory

## A. Time evolution of rotational wave packets and control landscape maps

We consider asymmetric top molecules interacting with pairs of mutually orthogonal linearly polarized non-resonant laser pulses, the polarization vectors of which are assumed to be parallel to the space-fixed X - and Y -axes.    We introduce the unit vectors X e , Y e , and Z e ( a e , b e ,  and c e ) of the space-fixed XYZ -axes (the molecule-fixed principal axes of inertia).    The time evolution of the rotational dynamics is described by the wave packet ( ) t  that obeys the Schrödinger equation

$$i \hbar { \frac { \partial } { \partial t } } | \psi ( t ) \rangle = H ( t ) | \psi ( t ) \rangle = [ H _ { 0 } + V ( t ) ] | \psi ( t ) \rangle \, ,$$

with  the  initial  condition 0 0 ( ) t   . In  Eq.  (1), 0 H and ( ) V t are  the  field-free Hamiltonian and the laser-molecule interaction, respectively.    If we introduce the dimensionless angular momentum operator J ,  which is the angular momentum operator divided by  ,  the field-free Hamiltonian [38] is expressed as

$$H _ { 0 } = h ( A J _ { a } ^ { 2 } + B J _ { b } ^ { 2 } + C J _ { c } ^ { 2 } ) \, ,$$

where  the  components  of  the  dimensionless  angular  momentum  operator  are  defined  by a a J   e J , etc.    In Eq. (2), the rotational constants are defined by 4 aa A I    , 4 bb B I    , and 4 cc C I    ( A B C   )  with aa I being the a component of the principal moment of inertia, etc.

As we assume mildly intense non-resonant laser pulses, we consider the lowest-order induced-dipole interaction and take the cycle average over the optical frequency.    We then have the interaction

$$V ( t ) = - \frac { 1 } { 4 } \alpha _ { X X } [ \mathcal { E } _ { X } ( t - t _ { X } ^ { 0 } ) ] ^ { 2 } - \frac { 1 } { 4 } \alpha _ { Y Y } [ \mathcal { E } _ { Y } ( t - t _ { Y } ^ { 0 } ) ] ^ { 2 } \, ,$$

where XX  ( YY  ) is the space-fixed XX ( YY ) component of the polarizability tensor.    In Eq. (3), 0 ( ) X X t t   and 0 ( ) Y Y t t   are the envelope functions of the laser pulses linearly polarized along  the  space-fixed X -axis  and Y -axis,  respectively.    Here,  we  assume  the  temporal  peak positions 0 X t and 0 Y t ,  which  define  the time  delay 0 0 ( 0) Y X t t     .    According  to  the temporal widths of the laser pulses and the grid size associated with  , which will be explained in  Sec.  IIC,  we  can  safely  ignore  the  temporal  overlap  between 0 ( ) X X t t   and 0 ( ) Y Y t t   when 0   .    In the case of 0   , we assume the fixed value of 2  for the phase difference in the optical frequency between the X and Y polarized laser pulses as we are not interested in the control  with  elliptically  polarized  laser  pulses  in  the  present  study. Because  of  this,  the interaction potential is always given by Eq. (3) independent of the value of 0   .    The total pulse fluence F is given by

$$F = & \frac { 1 } { 2 } \varepsilon _ { 0 } c \int _ { - \infty } ^ { \infty } d t \left \{ \left [ \mathcal { E } _ { X } ( t ) \right ] ^ { 2 } + \left [ \mathcal { E } _ { Y } ( t ) \right ] ^ { 2 } \right \} \equiv F _ { X } + F _ { Y } \equiv r F + ( 1 - r ) F \ ,$$

where 0  and c are the dielectric constant in vacuum and the speed of light, respectively.    We introduce the ratio r that determines how to divide the total pulse fluence F into the fluence of the X -polarized laser pulse X F and that of the Y -polarized laser pulse Y F .    We focus on 0 0 Y X t t    and r as  the  control  parameters,  assuming  that  the  temporal  widths  of  the  laser pulses are fixed.

It is necessary to deal with various asymmetric top molecules, the rotational constants of which are distributed in the range of 2 to 3 orders of magnitude in value.    In order to treat them in a unified manner, we measure the energy in units of the rotational constant hA .    The Schrödinger equation is expressed in the dimensionless form as

$$i \frac { \partial } { \partial t } | \psi ( t ) \rangle = [ J _ { a } ^ { 2 } + \tilde { B } J _ { b } ^ { 2 } + \tilde { C } J _ { c } ^ { 2 } + \tilde { V } ( t ) ] | \psi ( t ) \rangle \, ,$$

where B B A   , C C A   ( 0 1 C B      ), and ( ) ( ) V t V t hA   .    Although we use the same notation ' t ' as that in Eq. (1), we introduce the dimensionless time t in Eq. (5), which is defined by multiplying the original time by  2 A  .    Under given sets of laser pulses 0 ( ) X X t t   and 0 ( ) Y Y t t   , we numerically integrate Eq. (5) during the period 0 f [ , ] t t , where f t specifies the final time.    We expand the rotational wave packet ( ) t  in terms of the eigenfunctions of a symmetric top  { } JKM , which satisfy the eigenvalue equations 2 ( 1) JKM J J JKM   J , c J JKM K JKM  ( , 1, , K J J J      )  with c c J   e J ,  and Z J JKM M JKM  ( , 1, , M J J J      )  with Z Z J   e J . The  details  of  the  numerical  integration  are summarized in Appendix A.    For simplicity, we ignore the nuclear spin statistics.

Next, we define the degrees of 3D alignment as a function of the control parameters, i.e., the time delay 0 0 Y X t t    [Eq. (3)] and the ratio r [Eq. (4)].    To be specific, we calculate the expectation values of all possible combinations, i.e., a total of six combinations of the direction cosines, which are defined by

$$\varphi _ { a b c } ( \tau , r ; t ) = & \frac { 1 } { 3 } \langle \psi ( t ) | [ ( e _ { a } \cdot e _ { X } ) ^ { 2 } + ( e _ { b } \cdot e _ { Y } ) ^ { 2 } + ( e _ { c } \cdot e _ { Z } ) ^ { 2 } ] | \psi ( t ) \rangle , \\ & \cdots \\ \varphi _ { c b } ( \tau , r ; t ) = & \frac { 1 } { 3 } \langle \psi ( t ) | [ ( e _ { c } \cdot e _ { X } ) ^ { 2 } + ( e _ { b } \cdot e _ { Y } ) ^ { 2 } + ( e _ { a } \cdot e _ { Z } ) ^ { 2 } ] | \psi ( t ) \rangle ,$$

after the temporal peak of the second pulse.    During 0 f [ , ] Y t t t  , we search the maximum value for a given set of control parameters  and r , which is denoted by ( , ) r  .    The contour map of ( , ) r  as a function of  and r defines the control landscape map in the present study. If the landscape map is composed of, for example, 6000 ( , ) r  values, we have to solve Eqs. (5) and (6) 6000 times for each molecule.    The landscape map contains abundant information on the  3D  alignment  control,  but  its  construction  requires  a  high  computational  cost.    This  has motivated us to adopt the ML approaches to reduce the computational cost.

## B. Asymmetric top molecules considered in the present study

Because of the issue of the high computational cost mentioned above, we focus on some specific classes of asymmetric top molecules to reduce the number of training samples.    We introduce the first criterion associated with the asymmetry parameter (2 ) ( ) (2 1 ) (1 ) B A C A C B C C             , which takes a value between 1  for a prolate top ( B C  ) and 1  for an oblate top ( A B  ) [38].    We consider the prolate-type asymmetric top molecules with 1 0    .    The second criterion is about the principal axes.    The principal axes  of  inertia  characterize  the  free  rotational  dynamics,  whereas  those  of  polarizability characterize the 'torques' received from the laser pulses.    Without significant loss of generality, we consider the molecules with 2 C v symmetry so that the two principal-axis systems become the same.    Because of the 2 C v symmetry, the polarizability interaction in Eq. (3) is reduced to

$$V ( t ) = - \frac { 1 } { 4 } \left [ \Delta \alpha _ { a c } ( e _ { a } \cdot e _ { X } ) ^ { 2 } + \Delta \alpha _ { b c } ( e _ { b } \cdot e _ { X } ) ^ { 2 } \right ] \left ( \mathcal { E } _ { X } ^ { 0 } \right ) ^ { 2 } \varphi _ { X } ( t - t _ { X } ^ { 0 } ) \\ - \frac { 1 } { 4 } \left [ \Delta \alpha _ { a c } ( e _ { a } \cdot e _ { Y } ) ^ { 2 } + \Delta \alpha _ { b c } ( e _ { b } \cdot e _ { Y } ) ^ { 2 } \right ] ( \mathcal { E } _ { Y } ^ { 0 } ) ^ { 2 } \varphi _ { Y } ( t - t _ { Y } ^ { 0 } ) ,$$

where ac aa cc













and bc bb cc













.  In Eq. (7), the squares of the laser pulses are

assumed to be expressed as 0 2 0 2 0 [ ( )] ( ) ( ) X X X X X t t t t       and 0 2 0 2 0 [ ( )] ( ) ( ) Y Y Y Y Y t t t t       for convenience, where the normalized non-negative functions 0 ( ) X X t t   and 0 ( ) Y Y t t   representing  the  intensity  envelope  functions  with  the  temporal peak positions 0 X t and 0 Y t , respectively, are assumed to be given functions of time.    From Eq. (7), the values of 0 2 ( ) X  and 0 2 ( ) Y  are specified by the total pulse fluence F and the ratio r [see Eq. (4)].    Because of the first criterion 1 0    , most of the molecules are characterized by 1 0      if  we  introduce  the  asymmetry  parameter  associated  with  the  polarizability defined  by (2 ) ( ) bb aa cc aa cc            .    We thus  remove  'exceptional  molecules', the   values of which are not within the range of 1 0      .    This 'weak' restriction is referred to as the third criterion.

We restrict ourselves to the electrically neutral molecules in the electronic ground states with spin singlet states and take the asymmetric top molecules that satisfy the above-mentioned three criteria from the NIST database [39] except for SO2.    By using the coordinates provided by the NIST database as the initial molecular structures, we re-optimize the structures by RHF/6311G (d, p) with the Gaussian 16 program package and obtain the rotational constants.    We then have 65 molecules remaining because we remove molecules that lose the 2 C v symmetry after our optimization calculations.    We calculate the polarizabilities by adopting CCSD/cc-pVDZ. For SO2, the parameters are taken from Refs. [40] and [41].

The  rotational  dynamics  considered  here  is  expressed  in  terms  of B  , C  , ac  , bc  , and F together with the control parameters  and r .    To decrease the  number of parameters, we empirically determine the value of F that leads to the best degree of alignment for each molecule.    To this end, we first choose six molecules (Table I) on the basis of the values of  the  asymmetry  parameter  ranging  from 1    to 0   at  approximately  every  0.2, regardless  of  the  value  of   .    For  each  molecule,  we  calculate ( , ) r   by  systematically changing the total pulse fluence, the time delay  , and the ratio r to find the best value of F . We plot the numerically found six best values of F as a function of B  , C  ,  , ac bc     , bc  ,   , etc., and find the following 'empirical' relation

$$F \left [ J / c m ^ { 2 } \right ] = \frac { 1 2 . 3 } { \Delta \alpha _ { b c } \left [ a . u . \right ] } \, ,$$

where F and bc  are measured in units of 2 J cm and a.u., respectively.    When deriving Eq. (8) in Fig. 1, we use the Levenberg-Marquardt algorithm in the nonlinear least squares curvefitting method.    In our trial, we cannot find any clear relationship between F and the other parameters.    Because the data corresponding to the six molecules in Fig. 1 do not appear around ~ 3 a.u. bc  and ~ 20 a.u. bc  , we employ two more molecules with (g) 3.04 a.u. bc   and (h) 20.8 a.u.  in Table I.    We again perform a numerical search for the best values of F through a trial-and-error approach.    We see that the two extra results added in Fig.1 [(g) and (h)] almost lie on the fitting curve [Fig. (8)].    For reference, we recalculate the fitting curve by using the eight molecules [(a)-(h)] and the above-mentioned least squares curve-fitting.    The

Table I.    List of asymmetric top molecules in Fig. 1 [(a)-(f)] used to empirically determine the fluence [Eq. (8)], which is suitably adjusted to achieve the highest degrees of alignment (see text). For each molecule, the value of the asymmetry parameter κ , that of κα , and that of the degree of alignment  (DOA)  are  also  shown.    Two  extra  molecules  with  (g) 3.04 a.u. bc   and  (h) 20.8 a.u. bc   are used to illustrate the validity of Eq. (8) (see text).

| molecule                |     κ |   κ α |   DOA |
|-------------------------|-------|-------|-------|
| (a) C 7 H 12 1)         | -0.06 | -0.24 |  0.64 |
| (b) SF 4                | -0.48 | -0.10 |  0.67 |
| (c) CF 2 Cl 2           | -0.59 | -0.31 |  0.68 |
| (d) (CH 3 ) 2 CCCH 2    | -0.64 | -0.76 |  0.73 |
| (e) CH 3 CHCHCH 3       | -0.84 | -0.22 |  0.68 |
| (f) SO 2                | -0.94 | -0.67 |  0.77 |
| (g) CH 3 (CH 2 ) 5 CH 3 | -0.99 | -0.77 |  0.80 |
| (h) CH 2 CHOCHCH 2      | -0.99 | -0.26 |  0.68 |

1) Bicyclo[2.2.1]heptane recalculated fitting curve is the same as that in Eq. (8) up to two significant digits in the numerator on the right-hand side of Eq. (8).    Because of this, we will use Eq. (8) in the following.    By substituting Eq. (8) into Eq. (7), we have the dimensionless interaction expressed as

Figure 1 Red curve shows the empirically determined fluence [Eq. (8)] as a function of bc  , which is derived from the Levenberg-Marquardt algorithm with the molecules (a)-(f) in Table I.    Fluence associated with extra molecules (g) and (h) in Table I are well fitted by Eq. (8) (see text).

<!-- image -->

$$\tilde { V } ( t ) = & - \frac { \eta _ { 0 } } { 4 } r \left [ \left ( \frac { \Delta \alpha _ { a c } } { \Delta \alpha _ { b c } } \right ) ( e _ { a } \cdot e _ { X } ) ^ { 2 } + ( e _ { b } \cdot e _ { X } ) ^ { 2 } \right ] \varphi _ { X } ( t - t _ { X } ^ { 0 } ) \\ & - \frac { \eta _ { 0 } } { 4 } ( 1 - r ) \left [ \left ( \frac { \Delta \alpha _ { a c } } { \Delta \alpha _ { b c } } \right ) ( e _ { a } \cdot e _ { Y } ) ^ { 2 } + ( e _ { b } \cdot e _ { Y } ) ^ { 2 } \right ] \varphi _ { Y } ( t - t _ { Y } ^ { 0 } ) ,$$

with the constant 0 0 24.6 ( ) hA c    .

## C. Preparing training samples

From Eqs. (5) and (9), we see that the laser-induced rotational dynamics is described by the  three  molecular  parameters B  , C  ,  and ac bc     ,  that  define  the  coordinate  system referred to as a molecular space.    Each molecule is uniquely specified by a point in the molecular space, as shown in Fig. 2(a).    From the 65 molecules in the molecular space in Fig. 2(a), we first choose 30 training sample molecules by using the Kennard-Stone algorithm [42].    Figure 2(b) shows the projected components on the BC  -plane, which are distributed within a small region defined  by  the  three  lines.    Two  lines  originate  from  the  first  criterion,  i.e.,  the  asymmetry parameter 1 0    so  that C B    and 2 1 C B     .    The  third  line  originates  from  the inequality ( 1) C B B      ,  which  is  derived  under  the  condition cc aa bb I I I   .    Within  the specified  region  on  the BC  -plane,  the  distribution  of  the  points  (projected  components)  is reasonably uniform.

Figure 2(a)

Molecular parameters for the 90 asymmetric top molecules are specified in the present molecular space,  the  three  axes  of  which  represent B  , C  ,  and ac bc     .    Among the 55  training sample molecules, 30 (black solid squares) are from the NIST dataset and 25 (red solid stars) are artificial molecules (see text).    The blue solid circles correspond to the 35 test sample molecules. The three test sample molecules indicated by arrows with chemical formulas are discussed in Fig. 3.

Figure 2(b)

<!-- image -->

The molecules in Fig. 2(a) are projected onto the BC  plane.    Black solid squares and blue solid circles correspond to the 30 training and 35 test samples, respectively.    The artificial molecules are not shown here.    The three purple straight lines that define the projection area are explained in the text.    The blue straight line ( , ) L L B C    is the least squares straight line derived from the 65 points.

<!-- image -->

## Figure 2(c)

The  molecules  in  Fig.  2(a)  are  projected  onto  the  plane  defined  by  the  two  straight  lines, ( , ) L L B C    [see  Fig.  2(b)]  and  the ac bc     axis. Red  solid  stars  correspond  to  the projected  25  artificial  molecules.    Black  solid  squares,  which  correspond  to  the  black  solid squares in Fig. 2(a), are the 30 training sample molecules.    The test sample molecules are shown by the 3 blue open circles and the 32 blue solid circles, the former of which specify the molecules used to evaluate the generic error (see text).

On  the  other  hand,  the  points  projected  onto  the  other  two  planes  defined  by  the ac bc     axis exhibit a non-uniform distribution (not shown).    We see from Fig. 2(a) that the 30 training samples are localized in specific regions in the molecular space, making it difficult to train the CNN model.    To facilitate the CNN model training, we take advantage of the fact that the rotational dynamics is specified by a small number of molecular parameters B  , C  , and ac bc     .    Because of this, we can introduce 'artificial' molecules to realize a reasonably uniform distribution of the training samples in the molecular space so that the test samples, i.e., the other molecules not included in the training set, are reasonably interpolated.    We adopt the following procedure.    First, we introduce a rectangle with ( , ) L L B C    being one of the sides on the BC  -plane.    It is the least squares straight line derived by using the 65 molecules [Fig. 2(b)].    To  effectively  introduce  the  artificial  molecules,  the  other  side  of the  rectangle  is  set parallel to the ac bc     axis scaled by B C    because more (less) molecules are originally distributed when the value of B C    is small (large) in Fig. 2(a).    We then divide the rectangle into  7 7  small  rectangles  to  introduce  64  lattice  points  into  the  molecular  space.    We intuitively extract the 25 lattice points that correspond to the artificial molecules, which are added to the training sample molecules, as shown in Fig. 2(c).    The 55 training samples are composed of the originally chosen 30 molecules and the 25 artificial molecules, which are shown by the black solid squares and the red solid stars, respectively, in Fig. 2(a).

<!-- image -->

We already introduced the dimensionless time [Eq. (5)] to treat various molecules in a unified  manner.    Even  so,  the  values  of  the  dimensionless  rotational  constants B  and C  , which characterize a 'slow' rotational motion, are still distributed over an approximately singledigit  range  in  Fig.  2.    This  feature  introduces  markedly  different  temporal  behavior  into  the rotational dynamics depending on the molecule, leading to difficulty in control landscape map prediction by the CNN model.    To solve this problem, we measure the dimensionless time in units of rot ( ) T B C     , which will be referred to as the rotational period for convenience.    As will be discussed in Sec. III, rot T measures the slow dynamics in a unified way probably because of rot (2 ) (2 ) B T C       .    By using rot T ,  the  normalized  intensity  envelope  functions  are defined by

$$\varphi _ { X } ( t - t _ { X } ^ { 0 } ) = & \frac { 1 } { \sqrt { 2 \pi } \sigma } \exp \left [ - \frac { ( t - t _ { X } ^ { 0 } ) ^ { 2 } } { \sigma ^ { 2 } } \right ] \text { and } \varphi _ { Y } ( t - t _ { Y } ^ { 0 } ) = & \frac { 1 } { \sqrt { 2 \pi } \sigma } \exp \left [ - \frac { ( t - t _ { Y } ^ { 0 } ) ^ { 2 } } { \sigma ^ { 2 } } \right ] ,$$

where the FWHM ( 2 ln 2  ) and 0 X t are set to rot 0.003 T and rot 0.1 T , respectively.

The control parameters are uniformly discretized such that the time delay ( 1) i i      ( 1, 2, ,120 i   )  with rot 0.01 T   ( rot 0.003 T  )  and  the  fluence  ratio ( 1) j r j r   

( 1, 2, , 50 j   ) with 0.01 r   so that the control landscape map of each molecule consists of 6000 pixels.    We emphasize again that each pixel in the single landscape map represents the maximum degree of alignment ( , ) i j r  under the given set of control parameters i  and j r . We search the maximum degree of alignment ( , ) i j r  by assuming 0 0 t  and 0 f rot 1.2 Y t t T   .    We thus have to numerically solve Eqs. (5) and (6) 6000 times even to prepare a  single  control  landscape  map,  i.e.,  a  single  training  sample. To  circumvent  this  high computational cost, we utilize the CNN model as explained below.    For each landscape map of the training sample molecule, we randomly choose 600 sets of control parameters and calculate 600 { ( , ) i j r   }, which are regarded as the training samples to train the CNN model to generate a total of 6000 values.    We adopt and train the CNN model for each training sample molecule within the Keras framework [43].    According to Ref. [37], each set of control parameters i  and j r is represented by the sparse  120 50  matrix, that is, one of the matrix elements that correspond  to  the  specified  time  delay i  ( 1, 2, ,120 i   ),  and  the  fluence  ratio j r ( 1, 2, , 50 j   ) is set to 1, while all the other elements are set to 0.    This input matrix and its label ( , ) i j r   consist of one of the training samples for the CNN model.    The input matrix is sent  to  the  two  convolutional  layers  composed  of  four  5 5  filters  and  sixteen  5 5  filters, respectively; to the single fully connected layer with the 64 units; and finally to the output layer with a single unit.    The output layer provides the predicted value (pred) ( , ) i j r   .    We use the ReLU activation function for all layers except the output layer in which the sigmoid function is used.    We finish training the CNN model when the value of MSE associated with the 600 sets of { ( , ) i j r   and (pred) ( , ) i j r   }  is  smaller  than 6 10  .    We repeat  the  procedure  for  all  the training sample molecules to prepare the training set.    In Appendix B, the two typical examples of the scattered plots associated with the training samples are provided to illustrate the validity of the above-mentioned procedure.

## D. Training CNN model

We  develop  the  CNN  model  to  predict  the  landscape  maps  of  the  35  test  sample molecules, which are not included in the training set (Sec. IIC).    The input matrix that represents the control parameters is sent to the two convolutional layers, both of which are composed of four 5 5  filters, and then to the two fully connected NN layers with 300 and 50 units.    On the other hand, the inputs associated with the molecular parameters B  , C  , and max ( ) ( ) ac bc ac bc         with max ( ) 11.7 ac bc      are  sent  to  the  other  two  fully connected  NN  layers  with  50  and  1000  units. Here, max ( ) ac bc     is  introduced  to normalize the value of ac bc     .    The outputs of the 1000 units are simply added to those of the 50 units associated with the control parameters to form the layer with 1050 units, which are sequentially sent to the fully connected layers with 100, 50, and 11 units, and finally to the output layer.    We always use the ReLU activation function for all layers except the output layer.    The output layer with the sigmoid activation function provides the predicted value (pred) ( , ) i j r   for the input molecule under the specified control parameters i  and j r .    The CNN model is trained to minimize the mean squared error (MSE) defined by

$$\Delta = & \frac { 1 } { N } \sum _ { n = 1 } ^ { N } \ \frac { 1 } { 1 2 0 \times 5 0 } \sum _ { i = 1 } ^ { 1 2 0 } \sum _ { j = 1 } ^ { 5 0 } \ \left | \Phi _ { n } ^ { ( \text {pred} ) } ( \tau _ { i } , r _ { j } ) - \Phi _ { n } ( \tau _ { i } , r _ { j } ) \right | ^ { 2 } ,$$

where the subscript ' n ' in (pred) n  and n  is introduced to distinguish the 55 N  training sample molecules.    We estimate the generic error by using the 31st, 32nd, and 33rd test sample molecules chosen by the Kennard-Stone algorithm in the molecular space.    We use the same expression as that in Eq. (11) for the three molecules to evaluate the generic error.    To avoid overlearning,  we  regard  the  generic  error  of 4 4.8 10   as  the  converged  value.    When  the convergence is achieved, the MSE in Eq. (11) has a value of 4 2.5 10    .

## III. Results and discussion

We apply the trained CNN model to predict the control landscape maps of the 35 test sample molecules that are not involved in the training set.    The control landscape map of each molecule  shows  the  maximum  degrees  of  alignment (pred) ( , ) i j r   as  a  function  of  the discretized i  and j r .    In each control landscape map, the 'maximum' value is referred to as the optimal value because it is the optimal degree of 3D alignment corresponding to the optimal control solution within the present double pulse control.    Here, the predicted optimal value and the numerically obtained (true) optimal value are denoted by (pred) opt  and (true) opt  , respectively, which also specify their optimal time delays and optimal ratios.

It is apparent that one of the direct applications of the landscape maps is to predict the optimal value (pred) opt  for each molecule.    In Fig. 3, we show the optimal values associated with the 35 test sample molecules in descending order.    We also show the numerically obtained (true) optimal values using the purple solid triangles, which are obtained as follows.    In each predicted landscape map composed of 6000 pixels, we focus on the top 5%, i.e., the 300 pixels according to their degrees of alignment, and sort them in descending order in value.    We first select the pixel with the largest value and regard it as one of the candidates for the true optimal value.    Next, we select the pixel with the second largest value.    This pixel is selected as a candidate if it is at least 5 Chebyshev distance (chessboard distance) apart from the previously selected (first) pixel. If not, we simply ignore the second pixel.    By repeating the procedure 300 times, we prepare a set  of  candidate  pixels  associated  with  the  true  optimal  value.    For  each  candidate  pixel,  we define the  5 5  pixel region, the center of which is the candidate pixel.    Then, we numerically calculate the degrees of alignment for all the pixel regions to find the 'maximum' value, which is regarded as the true optimal value for each molecule.    In Fig. 3, we see a good agreement between the predicted (pred) opt  and the true (true) opt  optimal values especially when the optimal values are larger than ca. 0.65.    For values smaller than ca. 0.65, the CNN model still reasonably predicts the optimal values although some of the predicted optimal values are slightly different from  those  obtained  numerically.    The  difficulty  in  predicting  the  optimal  values  of  some molecules can be partly attributed to their near-edge positions in the molecular space [Fig. 2(a)].

Figure 3

For the 35 test sample molecules listed in Appendix C (Table II), the blue solid circles show the predicted optimal values { (pred) opt  } in descending order.    The purple solid triangles show the numerically obtained (true) optimal values { (true) opt  } (see text).

<!-- image -->

We see from Fig. 3 that the 35 optimal values are widely distributed from ca. 0.55 to ca. 0.8 even though we have restricted ourselves to the prolate-type 2 C v asymmetric top molecules. We expect that the differences in the optimal values can be interpreted in terms of the asymmetry parameter  and ac bc     that characterize the free rotational motion and the laser-induced interaction,  respectively.    In  Fig.  4,  we  plot (pred) opt  of  the  87  molecules  including  the  25 artificial molecules as a function of  and ac bc     .    Note that we solely use the predicted optimal values (pred) opt  and ignore the three molecules numbered 30, 31, and 32 in Fig. 3 and Table II (Appendix C) because of the large deviations in predicted value ( 0.05  ).    Roughly speaking, we see a curved distribution from top to bottom in Fig. 4.    To examine the distribution pattern in detail, we apply the hierarchical clustering approach to classify the 87 optimal values into the three clusters.    First, we normalize the predicted landscape map of each molecule with respect to its optimal value and regard the 6000 points in each normalized landscape map as the 6000-dimensional vectors.    By using the 6000-dimensional vectors associated with the control landscape  maps,  we  calculate  the  Euclidean  distances  between  them.    On  the  basis  of  the Euclidean distances, we apply the agglomerative approach [44] together with Ward's method [45], a hierarchical clustering approach, to classify the landscape maps into the three clusters named Clusters 1, 2, and 3.    In Fig. 4, the optimal values belonging to Clusters 1, 2, and 3 are specified by red, blue, and black solid colors, respectively.      The molecules in Cluster 1 have large optimal values  and  are  characterized  by  large  values  of | | 0.65   and 5 ac bc      . The molecules in Cluster 3 do not have large optimal values and are characterized by the small values of 4.5 ac bc      ,  while  being  widely  distributed  along  the  axis.    The  molecules  in Cluster 2 have small values of  3 4.5 ac bc       and large values of  | | 0.85   , indicating that these molecules possess characteristics intermediate of those of Clusters 1 and 3.

Figure 4

Predicted optimal degrees of alignment (pred) opt  with respect  to the asymmetry parameter  and ac bc     .    Red, blue, and black solid circles (stars) correspond to the 62 molecules (25 artificial molecules) classified into Clusters 1, 2, and 3, respectively (see text).

Finally,  we  consider  the  control  mechanisms  in  each  cluster  through  the  typical examples of the control landscape maps.    Figures 5(a) and (b) show that the typical landscape maps belonging to Cluster 1, which are characterized by the two sharp peaks around rot ~ 0.4 T  and rot ~1.0 T  with  the  small  values  of r .    Here,  the  small  values  of r mean  that  the fluence of the first X -polarized pulse is (much) weaker than that of the second Y -polarized pulse. The 3D alignment control mechanisms for Cluster-1 molecules can be understood according to Refs. [26] and [27].    Because the value of ac  is considerably larger than that of bc  in Cluster-1 molecules, the first pulse with weak pulse fluence selectively and highly aligns the molecular a -axis  along  the X -axis  (1D  alignment).    Then,  the  second  strong  pulse  polarized along the Y -axis kicks the molecule at the timings when the a -axis maximally 1D aligns along the X -axis to minimize the torque exerted on the a -axis.

<!-- image -->

Figure 5

<!-- image -->

Typical  examples  of  control  landscape  maps  of  the  asymmetric  top  molecules  classified  into Cluster 1 [(a) and (b)], Cluster 2 [(c) and (d)], and Cluster 3 [(e) and (f)] are shown.    We use molecule-dependent color scales to clearly show the distribution patterns. (a) CH2BH ( 0.98    , 11.2 ac bc      ),  (b)  SO 2 ( 0.94  , 5.70   ),  (c)  CH 2Cl2  ( 0.98  , 3.50   ),  (d)  SeO 2 ( 0.83  , 4.23 ), (e) C4H2O3 ( 0.73  ,  2.40 ), and (f) BeCO3 ( 0.37  , 4.61).    Molecules (a), (c), and (e) belong to the test set, and molecules (b), (d), and (f) belong to the training set.    We use moleculedependent color scales to clearly show the distribution patterns.

Examples of the control landscape maps belonging to Cluster 2 are shown in Figs. 5(c) and (d), which are characterized by the single narrow peaks around rot ~1.0 T  along the τ -axis while the peaks are widely distributed along the r -axis.    We can understand the features of the Cluster-2  molecules  in  terms  of  the  large  values  of | | 0.85   ,  meaning  that  the  Cluster-2 molecules are similar in shape to the prolate symmetric top molecules ( 1    ).    The rotational wave packets of the Cluster-2 molecules show almost regular and clear revivals after the first pulse,  which  determines  the  best  timing of the second  pulse rot ~1.0 T .    The small values of 3 4.5 ac bc       , on the other hand, reduce the degrees of 1D alignment of the a -axis along the X -axis by the first pulse.    Because of this, the a -axis is slightly affected by the torque exerted by the second pulse, resulting in a slight decrease in the degree of 3D alignment relative to that of the Cluster-1 molecules.

Regarding the Cluster-3 molecules, the small values of ac bc     make it difficult to selectively 1D align the most polarizable molecular a -axes along the X -axis, leading not only to a further reduction of the degree of 3D alignment but also to a variety of structures of the landscape maps depending on their molecular parameters, as shown in Figs. 5(e) and (f).    For Cluster-3 molecules, we may need to shape the laser pulses beyond the double pulse excitation schemes considered here in order to achieve higher degrees of 3D alignment.

## Summary

We have demonstrated the effectiveness of the CNN-based approach for predicting the control landscape maps of the full quantum molecular dynamics through a case study of the laserinduced 3D alignment of asymmetric top molecules with the double pulse control scheme.    The control landscape map of each molecule is defined by the maximum 3D degree of alignment ( , ) i j r   as a function of the discretized i  ( 1, 2, , 120 i   ) and j r ( 1, 2, , 50 j   ) with

 and r being the time delay and the fluence ratio, respectively.    We have restricted ourselves to the prolate-type asymmetric top molecules with the 2 C v symmetry to prepare the training samples at a reasonable computational cost.    We have assumed the low-temperature limiting case as the most remarkable quantum behavior of the rotational wave packets is expected.    By using the empirically derived fluence formula [Eq. (8)], the molecules are shown to be specified in the molecular space defined by the three axes, i.e., the two dimensionless rotational constants B  and C  ,  and  the  ratio  of  the  polarizabilities ac bc     . To  realize  the  uniform distribution  of  the  training  sample  molecules  in  the  molecular space,  we  have introduced  the artificial molecules by taking advantage of the fact that the rotational dynamics is specified by the rotational constants and the polarizability components.    This is practically important because the CNN model is known to be especially good at data interpolation.

The  present  CNN  model  is  trained  by  55  landscape  maps  of  the  training  sample molecules including the 25 artificial molecules.    The trained CNN models have successfully predicted the control landscape maps of the test sample molecules with reasonably high accuracy as illustrated by the screening for the optimal degrees of 3D alignment.    As the optimal values are  widely  distributed  from  ca.  0.55  to  ca.  0.8  (Fig.  3),  we  have  applied  the  agglomerative approach to classify all the landscape maps, i.e., all the molecules, into the three groups.    The control  landscape  maps  belonging  to  each  cluster  have  common  structural  characteristics, reflecting the effectiveness of the 3D alignment control.    The double pulse control is especially effective for  the  molecules  that  have a large value of ac bc     ,  which  would  be  in  good agreement with the control mechanism proposed in Refs. [26] and [27].

The successfully predicted control landscape maps in the present case study strongly suggest  the  usefulness  of  applying  the  ML  approaches  to  the  laser  control  of  full  quantum molecular  dynamics.    When  considering  the  quantum  control  of  molecular  dynamics,  it  is natural to investigate the optimal methods, e.g., based on optimal control theory.    As the optimal control  approaches actively cooperate with the complicated quantum interferences among the molecular wave functions, the control mechanisms are often too complicated to be understood by our chemical physics-based intuitions and/or considerations.    In this regard, quantum optimal control approaches in combination with ML-based interpretations such as control landscape maps would  be  useful  not  only  for  quantum  molecular  dynamics  but  also  for  other  quantum technologies.

## Acknowledgements

YO acknowledges support in the form of a Grant-in-Aid for Scientific Research (C) (23K04659) and partial support from the Joint Usage/Research Program on Zero-Emission Energy Research, Institute of Advanced Energy, Kyoto University (ZE2024B-17).    This work was also supported by JST SPRING, Grant Number JPMJSP2114.    Computations were performed in the Research Center for Computational Science, Okazaki, Japan (Project: 22-IMS-C987).

## APPENDIX A: Time evolution of rotational wave packets

We briefly summarize the numerical method to solve the dimensionless Schrödinger equation in Eq. (5).    We expand the rotational wave packet in terms of the eigenfunctions of the symmetric top { JKM } so that we have

$$\left | \psi ( t ) \right \rangle = \sum _ { J = 0 } ^ { J _ { \max } } \sum _ { K , M = - J } ^ { J } \, C _ { K M } ^ { J } \left ( t \right ) | J K M \rangle \ .$$

Here,  the  eigenfunction JKM is  also  expressed  as  the  complex  conjugate  of  the  Wigner rotational matrix [38]

$$\langle \hat { R } | J K M \rangle = \sqrt { \frac { 2 J + 1 } { 8 \pi ^ { 2 } } } D _ { M K } ^ { J ^ { * } } ( \hat { R } ) \, ,$$

where the set of Euler angles is denoted as ˆ R .    If we substitute Eq. (A1) into Eq. (5), we have the equations of motion for { ( ) J C KM t },

$$i \dot { C } _ { K M } ^ { J } ( t ) = \sum _ { J ^ { \prime } M ^ { \prime } K ^ { \prime } } \, \left \langle J K M | [ \tilde { H } _ { 0 } + \tilde { V } ( t ) ] | J ^ { \prime } K ^ { \prime } M ^ { \prime } \rangle C _ { K ^ { \prime } M ^ { \prime } } ^ { J ^ { \prime } } ( t ) ,$$

which is expressed in terms of the matrix elements of the dimensionless field-free Hamiltonian 0 H  and the dimensionless interaction potential ( ) V t  [Eq. (9)].    We rewrite 0 H  as

$$\tilde { H } _ { 0 } = J _ { a } ^ { 2 } + \tilde { B } _ { b } ^ { 2 } + \tilde { C } _ { c } ^ { 2 } = \left ( \frac { 1 + \tilde { B } } { 2 } \right ) J ^ { 2 } + \left ( \tilde { C } - \frac { 1 + \tilde { B } } { 2 } \right ) J _ { c } ^ { 2 } + \left ( \frac { 1 - \tilde { B } } { 4 } \right ) \left ( J _ { + } ^ { 2 } + J _ { - } ^ { 2 } \right ) .$$

Here, the operators a b J J iJ    have the following non-zero matrix elements [38]

$$\left \langle J K \mp 2 M \left | J ^ { 2 } _ { \pm } \right | J K M \right \rangle = \sqrt { J ( J + 1 ) - K ( K \mp 1 ) } \sqrt { J ( J + 1 ) - ( K \mp 1 ) ( K \mp 2 ) } \ .$$

We  also  need  to  calculate  the  matrix  elements  associated  with  the  squares  of  the direction cosines such as 2 ( ) a X  e e , 2 ( ) a Y  e e ,  , and 2 ( ) c Z  e e , which are involved in ( ) V t 

and in the operators associated with the degrees of alignment in Eq. (6).    With the aid of the Clebsch-Gordan series [38], we have

$$( e _ { a } \cdot e _ { X } ) ^ { 2 } \\ = & \frac { 1 } { 1 2 } \left [ 4 D _ { 0 0 } ^ { 0 } + 2 D _ { 0 0 } ^ { 2 } - \sqrt { 6 } \left ( D _ { 2 0 } ^ { 2 } + D _ { - 2 0 } ^ { 2 } + D _ { 0 2 } ^ { 2 } + D _ { - 0 2 } ^ { 2 } \right ) + 3 \left ( D _ { 2 2 } ^ { 2 } + D _ { - 2 2 } ^ { 2 } + D _ { - 2 - 2 } ^ { 2 } + D _ { - 2 - 2 } ^ { 2 } \right ) \right ] ^ { ( A 6 ) }$$

 , and

$$( e _ { c } \cdot e _ { Z } ) ^ { 2 } = & \frac { 1 } { 3 } \left ( D _ { 0 0 } ^ { 0 } + 2 D _ { 0 0 } ^ { 2 } \right ) ,$$

where we omit ˆ R in  { ˆ ( ) J D MK R } for simplicity.    All the matrix elements are reduced to the integrals over the triple products of the Wigner rotation matrices [38], which are expressed in terms of the Clebsch-Gordan coefficients.    We substitute the matrix elements into the equations of  motion  for  { ( ) J C KM t }  and  numerically  integrate  Eq.  (A3)  by  the  5th-order  Runge-Kutta method.

## APPENDIX B: Preparing control landscape maps of training sample molecules

The control landscape map of each molecule is composed of 6000 pixels that represent { ( , ) i j r   : 1, 2, , 120 i   and 1, 2, , 50 j   }.    For  each  training  sample  molecule,  as explained in Sec. IIC, we numerically calculate the randomly chosen 600 { ( , ) i j r   } and use them to predict the values of the 6000 pixels.    We evaluate the validity of this procedure by considering the randomly chosen two training sample molecules, CH2CS (Fig. 6) and CH3CSCH3

Figure 6 Landscape map and scattered plot associated with the training sample molecule CH2CS.    (a) Initially chosen (numerically calculated) 600{ ( , ) i j r   }, (b) the predicted landscape map (see text), and (c) the scatter plot of all the 6000 { ( , ) i j r   }.

<!-- image -->

Figure 7 Landscape map and scattered plot associated with the training sample molecule CH3CSCH3.    (a) Initially chosen (numerically calculated) 600{ ( , ) i j r   }, (b) the predicted landscape map (see text), and (c) the scatter plot of all the 6000 { ( , ) i j r   }.

<!-- image -->

(Fig. 7).    From the initially prepared (numerically calculated) 600 { ( , ) i j r   } in Figs. 6(a) and 7(a), the CNN model constructs the control landscape maps in Figs. 6(b) and 7(b) with reasonably high probability.    This is confirmed by the scatter plots in Figs. 6(c) and 7(c), both of which are composed of the 6000 values of { ( , ) i j r   }.

## APPENDIX C: List of test sample molecules in Fig. 3

Table II provides the test sample molecules, the optimal degrees of 3D alignment of which are shown in Fig. 3.    For convenience, we number the test sample molecules in descending order of the value of (pred) opt  such that (pred) , opt n  ( 1, 2, , 35 n   ).

Table II.    List of 35 test sample molecules in Fig. 3, numbered in descending order of the value of (pred) opt  .    The dimensionless rotational constants B  and C  ,  , / ac bc     , and cluster classification numbers (#cluster), which are examined in Fig. 4, are also listed.

|   no. | molecule            |   B  |   C  |       |   / ac bc     |   #cluster |
|-------|---------------------|-------|-------|--------|-------------------|------------|
|     1 | CH 3 (CH 2 ) 7 CH 3 | 0.037 | 0.036 | -0.999 |              10.0 |          1 |
|     2 | CH 2 CS             | 0.020 | 0.019 | -0.999 |              10.7 |          1 |
|     3 | BrOBr               | 0.035 | 0.034 | -0.998 |              7.27 |          1 |
|     4 | ONONO               | 0.051 | 0.049 | -0.995 |              7.84 |          1 |
|     5 | C 3 H 7 OC 3 H 7    | 0.058 | 0.056 | -0.997 |              10.6 |          1 |
|     6 | CH 2 BH             | 0.096 | 0.088 | -0.982 |              11.2 |          1 |
|     7 | S 3                 | 0.125 | 0.111 | -0.969 |              7.02 |          1 |
|     8 | CH 3 (CH 2 ) 3 CH 3 | 0.112 | 0.107 | -0.987 |              6.85 |          1 |
|     9 | H 2 CS              | 0.060 | 0.057 | -0.993 |              5.69 |          1 |
|    10 | Cl 2 O              | 0.080 | 0.074 | -0.987 |              5.30 |          1 |
|    11 | B 2 H 4             | 0.129 | 0.125 | -0.989 |              6.33 |          1 |
|    12 | CH 2 ClCH 2 CH 2 Cl | 0.055 | 0.053 | -0.996 |              4.11 |          2 |
|    13 | C 2 H 5 SC 2 H 5    | 0.117 | 0.109 | -0.982 |              4.06 |          2 |
|    14 | CH 2 Cl 2           | 0.101 | 0.093 | -0.983 |              3.50 |          2 |
|    15 | HS(CH 2 ) 3 SH      | 0.062 | 0.060 | -0.994 |              3.15 |          2 |
|    16 | BHCl 2              | 0.067 | 0.063 | -0.991 |              2.99 |          3 |
|    17 | CF 2 Cl 2           | 0.626 | 0.530 | -0.595 |              2.88 |          3 |
|    18 | C 6 H 12 1)         | 0.276 | 0.252 | -0.936 |              4.11 |          2 |
|    19 | NCCH 2 CN           | 0.140 | 0.125 | -0.965 |              2.97 |          3 |
|    20 | SeF 4               | 0.638 | 0.518 | -0.503 |              2.23 |          3 |
|    21 | CHOOCHO             | 0.053 | 0.050 | -0.994 |              2.74 |          3 |
|    22 | N 2 H 2             | 0.134 | 0.118 | -0.964 |              2.13 |          3 |
|    23 | SiCl 2 (CH 3 ) 2    | 0.714 | 0.631 | -0.547 |              2.09 |          3 |

|   24 | SiH 2 Cl 2      |   0.180 |   0.157 |   -0.944 |   2.60 |   3 |
|------|-----------------|---------|---------|----------|--------|-----|
|   25 | COBr 2          |   0.187 |   0.158 |   -0.930 |   2.26 |   3 |
|   26 | SCl 2           |   0.202 |   0.168 |   -0.918 |   2.37 |   3 |
|   27 | C 8 H 6 2)      |   0.211 |   0.174 |   -0.911 |   2.38 |   3 |
|   28 | C 4 H 2 O 3     |   0.366 |   0.268 |   -0.732 |   2.41 |   3 |
|   29 | CH 3 NNCH 3     |   0.402 |   0.305 |   -0.721 |   4.22 |   3 |
|   30 | CH 3 CHCHCH 3   |   0.307 |   0.246 |   -0.840 |   2.57 |   3 |
|   31 | CH 3 CCl 2 CH 3 |   0.669 |   0.587 |   -0.603 |   2.22 |   3 |
|   32 | CBr 2 Cl 2      |   0.673 |   0.587 |   -0.585 |   2.24 |   3 |
|   33 | BrF 3           |   0.375 |   0.273 |   -0.719 |   2.62 |   3 |
|   34 | C 2 H 4 CO 3    |   0.476 |   0.334 |   -0.572 |   3.58 |   3 |
|   35 | Li 2 CO 3       |   0.617 |   0.381 |   -0.239 |   2.64 |   3 |

- 1) cis-1,3-dimethylcyclobutane
- 2) 5-(2-Cyclopropen-1-ylidene)-1,3-cyclopentadiene

## References

- [1]  M.  Rupp,  O. A.  von  Lilienfeld,  and  K.  Burke,  J.  Chem.  Phys.  148,  241401  (2018),  and references therein.
- [2] G. Carleo, I. Cirac, K. Cranmer, L. Daudet, M. Schuld, N. Tishby, L. Vogt-Marant, and L. Zdeborová, Rev. Mod. Phys. 91, 045002 (2019).
- [3] M. Ceriotti, C. Clementi, and O. A. von Lilienfeld, J. Chem. Phys. 154, 160401 (2021), and references therein.
- [4] B. Huang, G. F. von Rudorff, and O. A. von Lilienfeld, Science 381, 170 (2023).
- [5] P. O. Dral and M. Barbatti, Nat. Rev. Chem. 5, 388 (2021).
- [6] J. Westermayr and P. Marquetand, Chem. Rev. 121, 9873 (2021).
- [7] G. Carleo and M. Troyer, Science 355, 602 (2017).

- [8] L. E. H. Rodrígues, A. Ullah, K. J. R. Espinosa, P. O. Dral, and A. A. Kananenka, Mach. Learn.: Sci. Technol. 3, 045016 (2022).
- [9] D. R. Vivas, J. Madroñero, V. Bucheli, L. O. Gonzá, and J. H. Reina, arXiv:2204.12966 (2022).
- [10] N. Mohseni, T. Fösel, L. Guo, C. Navarrete-Benlloch, and F. Marquardt, arXiv:2105.00352 (2022).
- [11] F. Háse, C. Kreisbeck, and A. Aspuru-Guzik, Chem. Sci. 8, 8419 (2017).
- [12] L. E. H. Rodríguez and A. A. Kananenka, J. Phys. Chem. Lett. 12, 2476 (2021).
- [13] K. Lin, J. Peng, F. L. Gu, and Z. Lan, J. Phys. Chem. Lett. 12, 10225 (2021).
- [14] A. Ullah and P. O. Dral, Nat. Commun. 13, 1930 (2022).
- [15] A. Jaouadi, E. Mangaud, and M. Desouter-Lecomte, Phys. Rev. A 109, 013104 (2024).
- [16] Z. An, H.-J. Song, Q.-K. He, and D. L. Zhou, Phys. Rev. A 103, 012404 (2021).
- [17] M.-Y. Mao, Z. Cheng, L. Li, N. Wu, and W.-L. You, Phys. Rev. A 109, 042428 (2024).
- [18] M. Dalgaard, F. Motzoi, and J. Sherson, Phys. Rev. A 105, 012402 (2022).
- [19] D. Herschbach, Eur. Phys. J. D 38 , 3 (2006).
- [20] T. Seideman and E. Hamilton, Adv. At. Mol., Opt. Phys . 52 , 289 (2006).
- [21] Y. Ohtsuki, M. Yoshida, and Y. Arakawa, Progress in Ultrafast Intense Laser Science XIV , edited by K. Yamanouchi et al. (Springer Nature Switzerland, 2018), Chap. 4.
- [22] C. Koch, M. Lemeshko, and D. Sugny, Rev. Mod. Phys . 91 , 035005 (2019).
- [23] B. Friedrich and D. Herschbach, Phys. Rev. Lett . 74 , 4623 (1995).
- [24] A. Rouzée, S. Guérin, O. Faucher, and B. Lavorel, Phys. Rev. A 77 , 043412 (2008).
- [25] S. Pabst and R. Santra, Phys. Rev. A 81 , 065401 (2010).
- [26] J. G. Underwood, B. J. Sussman, and A. Stolow, Phys. Rev. Lett . 94 , 143002 (2005).
- [27] K. F. Lee, D. M. Villeneuve, P. B. Corkum, A. Stolow, and J. G. Underwood, Phys. Rev. Lett . 97 , 173001 (2006).

- [28] S. S. Viftrup, V. Kumarappan, S. Trippel, H. Stapelfeldt, E. Hamilton, and T. Seideman, Phys. Rev. Lett . 99 , 143602 (2007).
- [29] L. Holmegaard, J. H. Nielsen, I. Nevo, H. Stapelfeldt, F. Filsinger, J. Küpper, and G. Meijer, Phys. Rev. Lett. 102, 023001 (2009).
- [30] S. S. Viftrup, V . Kumarappan, L. Holmegaard, C. Z. Bisgaard, H. Stapelfeldt, M.

Artamonov, E. Hamilton, and T. Seideman, Phys. Rev. A 79 , 023404 (2009).

- [31] X. Ren, V. Makhija, and V. Kumarappan, Phys. Rev. Lett. 112, 173603 (2014).
- [32] D. Takei, J. H. Mun, S. Minemoto, and H. Sakai, Phys. Rev. A 94 , 013401 (2016).
- [33] M. Yoshida, N. Takemoto, and Y. Ohtsuki, Phys. Rev. A 98 , 053434 (2018).
- [34] H. Zhao, Y. Xiong, and M. Centurion, Phys. Rev. A 109, 053107 (2024).
- [35] H. A. Rabitz, M. Hsieh, and C. Rosenthal, Science 303, 1998 (2004).
- [36] C. Brif, R. Chakrabarti, and H. Rabitz, New J. Phys. 12, 075008 (2010).
- [37] T. Namba, M. Yoshida, and Y. Ohtsuki, J. Chem. Phys. 153, 024120 (2020).
- [38] R. N. Zare, ' Angular Momentum ' (Wiley, New York, 1988).
- [39]  NIST  Computational  Chemistry  Comparison  and  Benchmark  Database  NIST  Standard Reference Database Number 101. https://cccbdb.nist.gov/pglistx.asp.
- [40] G. Herzberg (ed ） Electronic Spectra of Polyatomic Molecules. Van Nostrand Reinhold: New York (1966).
- [41] D. Xenides and G. Maroulis, Chem. Phys. Lett. 319, 618 (2000).
- [42] R. W. Kennard and L. A. Stone, Technometrics 11, 137 (1969).
- [43] F. Chollet et al. Keras. 2015. https://keras.io.
- [44] A. Fernández ad S. Gómez, arXiv:1906.09222
- [45] J. H. Ward, Jr., J. Am. Stat. Assoc. 58, 236 (1963).