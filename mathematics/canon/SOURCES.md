# Sources

This file indexes the main sources used for the mathematics research packet.

## State-Space, Control, Stability

1. MIT OpenCourseWare, `6.241J Dynamic Systems and Control`
   Link: https://ocw.mit.edu/courses/6-241j-dynamic-systems-and-control-spring-2011/pages/lecture-notes/
   Why it matters:
   - solid official material for state-space models, observability, stability, and control optimization.

2. MIT OpenCourseWare, `2.160 Identification, Estimation, and Learning`
   Link: https://ocw.mit.edu/courses/2-160-identification-estimation-and-learning-spring-2006/resources/lecture_10/
   Why it matters:
   - useful for state-space modeling and estimation framing.

3. R. E. Kalman, `A New Approach to Linear Filtering and Prediction Problems` (1960)
   DOI: https://doi.org/10.1115/1.3662552
   Supporting citation page: https://www.bibsonomy.org/bibtex/46000cea585242435901ab4a9f5738b5
   Why it matters:
   - foundational estimator math for hidden-state systems.

## Optimization

4. Stephen Boyd and Lieven Vandenberghe, `Convex Optimization`
   Link: https://web.stanford.edu/~boyd/cvxbook/
   Why it matters:
   - principal reference for constrained optimization, quadratic forms, duality, and reliable numerical problem setup.

## Information Theory

5. Claude Shannon, `A Mathematical Theory of Communication` (1948)
   Publication record: https://www.mpi.nl/publications/item2383162/mathematical-theory-communication
   Historical document page: https://www.computerhistory.org/chess/doc-431614f68e1be/
   Why it matters:
   - entropy, information, uncertainty, and surprise are necessary for a serious agent control layer.

## Graph Theory And Network Science

6. Albert-László Barabási, `Network Science`
   Link: https://networksciencebook.com/translations/en/partials/home.html
   Why it matters:
   - gives usable math for graph structure, centrality, diffusion, and network-level dynamics.

## Sequential Decision And Reinforcement Learning

7. Richard Bellman, `Dynamic Programming`
   Open historical article related to the framework:
   https://pmc.ncbi.nlm.nih.gov/articles/PMC528622/
   Why it matters:
   - dynamic programming is the core mathematical lens for multistage optimal control and planning.

8. Richard S. Sutton and Andrew G. Barto, `Reinforcement Learning: An Introduction`, 2nd ed.
   MIT Press: https://mitpress.mit.edu/9780262039246/reinforcement-learning
   Why it matters:
   - formalizes sequential decision making through MDPs, value functions, and policy improvement.

## Notes On Source Quality

Selection criteria used here:
- prefer official course pages, official publisher pages, or original publication records,
- prefer foundational works over derivative summaries,
- use modern textbooks only where they are canonical and directly relevant.

Current gaps:
- a dedicated primary-source packet for Lyapunov stability,
- a stronger primary-source packet for spectral graph theory,
- a dedicated source set for partially observed control beyond classic Kalman filtering.

Those can be added next in a second research pass.

## Second-Pass Sources Added

9. MIT OpenCourseWare, `6.243J Dynamics of Nonlinear Systems`
   Lyapunov-related lecture notes:
   https://ocw.mit.edu/courses/6-243j-dynamics-of-nonlinear-systems-fall-2003/resources/lec6_6243_2003/
   https://ocw.mit.edu/courses/6-243j-dynamics-of-nonlinear-systems-fall-2003/resources/lec11_6243_2003/
   Why it matters:
   - gives formal Lyapunov and nonlinear stability grounding from an official source.

10. MIT OpenCourseWare, `6.245 Multivariable Control Systems`
    Course lecture notes:
    https://ocw.mit.edu/courses/6-245-multivariable-control-systems-spring-2004/pages/lecture-notes/
    Standard LTI optimization setup:
    https://ocw.mit.edu/courses/6-245-multivariable-control-systems-spring-2004/resources/lec1_6245_2004/
    H-infinity algorithms:
    https://ocw.mit.edu/courses/6-245-multivariable-control-systems-spring-2004/resources/lec7_6245_2004/
    Uncertain systems:
    https://ocw.mit.edu/courses/6-245-multivariable-control-systems-spring-2004/resources/lec13_6245_2004/
    Why it matters:
    - directly relevant for robust top-level control, performance outputs, and disturbance rejection.

11. Yale, Daniel Spielman, `Spectral Graph Theory`
    Course hub:
    https://www.cs.yale.edu/homes/spielman/eigs/
    Newer course schedule:
    https://cs.yale.edu/homes/spielman/462/462schedule.html
    Why it matters:
    - gives an authoritative graph-Laplacian and eigenvalue foundation for the cognitive web.

12. Brown CS, Anthony Cassandra / Leslie Kaelbling / Michael Littman
    Acting optimally in partially observable stochastic domains:
    https://cs.brown.edu/research/pubs/techreports/reports/CS-94-20.html
    Optimal policies for POMDPs:
    https://cs.brown.edu/research/pubs/techreports/reports/CS-94-14.html
    Why it matters:
    - strong primary material for belief-state planning and partial observability.

13. Carnegie Mellon, POMDP lecture notes
    Reid Simmons:
    https://www.cs.cmu.edu/~reids/planning/handouts/POMDP.pdf
    Geoffrey Gordon:
    https://www.cs.cmu.edu/~ggordon/780-fall07/lectures/POMDP_lecture.pdf
    Why it matters:
    - useful official academic notes for how POMDP planning is actually taught and approximated.

## Third-Pass Sources Added

14. MIT OpenCourseWare, reachability and observability
    https://ocw.mit.edu/courses/6-241j-dynamic-systems-and-control-spring-2011/resources/mit6_241js11_lec20/
    https://ocw.mit.edu/courses/6-011-signals-systems-and-inference-spring-2018/resources/mit6_011s18lec7/
    Why it matters:
    - direct official notes for observability structure and minimal realizations.

15. MIT Underactuated Robotics, LQR and Lyapunov
    LQR:
    https://underactuated.mit.edu/lqr.html
    Lyapunov:
    https://underactuated.mit.edu/lyapunov.html
    Why it matters:
    - practical, mathematically explicit notes connecting Riccati equations, stabilization, and Lyapunov analysis.

16. Stanford EE392m / EE364b, MPC
    EE392m lecture notes cover:
    https://web.stanford.edu/class/archive/ee/ee392m/ee392m.1034/Cover.pdf
    MPC lecture:
    https://web.stanford.edu/class/archive/ee/ee392m/ee392m.1056/Lecture14_MPC.pdf
    Boyd MPC slides:
    https://web.stanford.edu/class/ee364b/lectures/mpc_slides.pdf
    Receding horizon control paper page:
    https://web.stanford.edu/~boyd/papers/code_gen_rhc.html
    Why it matters:
    - gives the constrained optimization and receding-horizon framing needed for bounded agent control.

17. Change-point detection / CUSUM
    Original CUSUM paper record:
    https://doi.org/10.1093/biomet/41.1-2.100
    Modern open article:
    https://pmc.ncbi.nlm.nih.gov/articles/PMC12002415/
    Why it matters:
    - provides a mathematically clean basis for persistent-regime detection rather than brittle thresholding.

## Relativity, Information, And The AI Analogue

18. Albert Einstein, `Does the Inertia of a Body Depend Upon its Energy-Content?`
    English translation:
    https://www.fourmilab.ch/etexts/einstein/E_mc2/www/
    Why it matters:
    - primary historical source for the rest-energy result that later became known as `E = mc²`.

19. MIT OpenCourseWare, `8.033 Introduction to Relativity and Spacetime Physics`
    Full lecture notes:
    https://ocw.mit.edu/courses/8-033-introduction-to-relativity-and-spacetime-physics-fall-2024/mit8_033_f24_lec_full.pdf
    Why it matters:
    - useful official source for the full energy-momentum invariant, which is the deeper structure behind `E = mc²`.

20. Rolf Landauer, `Irreversibility and Heat Generation in the Computing Process`
    DOI:
    https://doi.org/10.1147/rd.53.0183
    Why it matters:
    - connects information transformation to physical cost and provides the cleanest bridge between computation and energetic accounting.

21. Karl Friston, `The free-energy principle: a unified brain theory?`
    Nature Reviews Neuroscience:
    https://www.nature.com/articles/nrn2787
    Open-access overview:
    https://discovery.ucl.ac.uk/id/eprint/10175520/
    Why it matters:
    - useful for treating adaptive intelligence through a single uncertainty-and-regulation budget, which helps frame the AI-side analogue.
