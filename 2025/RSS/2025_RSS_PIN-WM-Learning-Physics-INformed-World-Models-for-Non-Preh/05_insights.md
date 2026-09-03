# Insights — PIN-WM: Learning Physics-INformed World Models for Non-Prehensile Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (14 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p153.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p153.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 2 Wuhan Universi - extractive body cue:** We introduce PIN-WM, a Physies-INformed World Mode! that allows end-to-end identification of a 3D rigid body ‘dynamical system from visual observations.
- **p. 2 / 2 Wuhan Universi - extractive body cue:** + We conduct real robot implementation to demonstrate that our approach enables learning control policies with minimal task-agnostic interaction data and attains high performance Real2Sim2Real ...
- **p. 3 / C. Domain Randomization - extractive body cue:** We provide an overview of our framework in Figure 2
- **p. 3 / B. World Models for Policy Learning - extractive body cue:** In contrast, PIN-WM enables end-to-end identification of 3D rigid-body dynamics from visual observations using few-shot, task-agnostic interaction data, which facilitates the training of vision-based manipulation ...
- **p. 5 / B. Physics-INformed World Model - extractive body cue:** We formulate this system identification process as a velocity-based Linear Complementarity Problem (LCP) [16, 68] which solves the equations of motion under global constraints, Here, ...
- **p. 3 / B. World Models for Policy Learning - extractive body cue:** DINOWM [84] leverages spatial patch features pre-trained with DINOv2 to learn a world model and achieve task-agnostic behavior planning by treating goal features as prediction ...
- **Contribution anchor:** p. 2 (2 Wuhan Universi), p. 2 (2 Wuhan Universi), p. 3 (C. Domain Randomization), p. 1 (body section boundary not confidently recovered), p. 3 (B. World Models for Policy Learning), p. 5 (B. Physics-INformed World Model)

### Strongest assumption and failure boundary

- **p. 1 / 1. Iyrropuction - extractive body cue:** However, significant challenges arise from the difficulty of fully dictating. the motion and pose of the object being pushed.
- **p. 2 / A. Non-Prehensile Manipulation - extractive body cue:** However, the large gap between simulation and reality poses significant cha lenges for transferring these policies to the real world [12, 45], Building an interactive ...
- **p. 1 / 1. Iyrropuction - extractive body cue:** The complex underlying dynamics, caused by factors such as friction, restitution, and inertia, make motion prediction difficult and complicate motion planning and control
- **p. 2 / 2 Wuhan Universi - extractive body cue:** To bridge the Sim2Real gap, we turn the identified digital twin into plenty of digital cousins [15] through physics-sware perturbations which perturb the physics and ...
- **p. 3 / B. World Models for Policy Learning - extractive body cue:** However, purely data-driven world models rely heavily on the quantity and quality of training data and struggle to generalize to outof-distribution (OOD) scenarios {79, 62].
- **p. 7 / A. Evaluations in Simulation - extractive body cue:** Since neither of the two methods learns rendering parameters and their trained policies cannot work without aligned visual input, we add our rendering function Z ...
- **p. 8 / A. Evaluations in Simulation - extractive body cue:** The purely data-driven world model Dreamer V2 [27], albeit having access to more task-agnostic data, fails to accurately approximate the dynamics of the target domain, ...
- **Boundary to test:** Since neither of the two methods learns rendering parameters and their trained policies cannot work without aligned visual input, we add our rendering function Z to enhance these two methods.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We introduce PIN-WM, a Physies-INformed World Mode! that allows end-to-end identification of a 3D rigid body ‘dynamical system from visual observations. | p. 2 (2 Wuhan Universi), p. 2 (2 Wuhan Universi) |
| Reported outcome | All policies are trained until no significant success rate performance can be gained and are then deployed directly to the target domain for evaluation, We also conduct an ablation study of our ... | p. 7 (A. Evaluations in Simulation), p. 8 (A. Evaluations in Simulation) |
| Failure/limitation | Since neither of the two methods learns rendering parameters and their trained policies cannot work without aligned visual input, we add our rendering function Z to enhance these two methods. | p. 7 (A. Evaluations in Simulation), p. 8 (A. Evaluations in Simulation) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** We formulate this system identification process as a velocity-based Linear Complementarity Problem (LCP) [16, 68] which solves the equations of motion under global constraints, Here, we use LCP to first ... (p. 5, B. Physics-INformed World Model).
- **Paper-specific mechanism:** + We conduct real robot implementation to demonstrate that our approach enables learning control policies with minimal task-agnostic interaction data and attains high performance Real2Sim2Real without real-world fine-tuning. (p. 2, 2 Wuhan Universi).
- **Evidence boundary:** the reported outcome is All policies are trained until no significant success rate performance can be gained and are then deployed directly to the target domain for evaluation, We also conduct an ablation study ... (p. 7, A. Evaluations in Simulation); the relevant task/metric cue is We evaluate the accuracy of a world model using ‘one-step error (44] which measures the distance between the final object states after applying one sampled action to the (p. 7, A. Evaluations in Simulation). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** Moreover, the policies trained with physics-based alternatives exhibit unsatisfactory performance in the target domain, ‘One reason is that their world models failed to effectively ‘capture the target-domain dynamics. (p. 8, A. Evaluations in Simulation).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `World models, safety, uncertainty, and recovery`; tags: `Robotics, world model, physics-informed learning, non-prehensile manipulation`.
- **Reading predecessor in the generated track queue:** Mastering Diverse Domains through World Models (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Since neither of the two methods learns rendering parameters and their trained policies cannot work without aligned visual input, we add our rendering function Z to enhance these two methods.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: We formulate this system identification process as a velocity-based Linear Complementarity Problem (LCP) [16, 68] which solves the equations of motion under global constraints, Here, we use LCP to first ... (p. 5, B. Physics-INformed World Model); preserve the objective/update rule: We formulate this system identification process as a velocity-based Linear Complementarity Problem (LCP) [16, 68] which solves the equations of motion under global constraints, Here, we use LCP to first ... (p. 5, B. Physics-INformed World Model).
2. Use the paper-reported task/data/environment cue: Experiment setup: n simulation, we collect a single task-agnostc trajectory thatthe target object is pushed forward along a straight line by the robot end-effector for a predefined distance in the ... (p. 7, A. Evaluations in Simulation).
3. Compare against the reported or matched baseline: Note that all physics-based methods being compared are trained with the same task-agnostic trajectories as PIN-WM, for fair comparison. (p. 7, A. Evaluations in Simulation).
4. Report the body metric with its denominator and aggregation: We evaluate the accuracy of a world model using ‘one-step error (44] which measures the distance between the final object states after applying one sampled action to the (p. 7, A. Evaluations in Simulation).
5. Re-run the reported ablation or stress/failure condition: All policies are trained until no significant success rate performance can be gained and are then deployed directly to the target domain for evaluation, We also conduct an ablation study ... (p. 7, A. Evaluations in Simulation); if none is reported, design one around: Moreover, the policies trained with physics-based alternatives exhibit unsatisfactory performance in the target domain, ‘One reason is that their world models failed to effectively ‘capture the target-domain dynamics. (p. 8, A. Evaluations in Simulation).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (2 Wuhan Universi), p. 1 (Abstract), match the reported outcome at p. 7 (A. Evaluations in Simulation), p. 8 (B. Evaluations in Real-World), p. 6 (IV. RESULTS AND EVALUATIONS), and measure the boundary at p. 8 (A. Evaluations in Simulation), p. 8 (A. Evaluations in Simulation).

## Falsifiable research question

Under the paper's stated interface (We formulate this system identification process as a velocity-based Linear Complementarity Problem (LCP) [16, 68] which solves the equations of motion under ...), does the paper-specific mechanism (+ We conduct real robot implementation to demonstrate that our approach enables learning control policies with minimal task-agnostic interaction data and attains ...) retain the reported evaluation outcome (We evaluate the accuracy of a world model using ‘one-step error (44] which measures the distance between the ...) when tested against the paper's strongest explicit boundary (Moreover, the policies trained with physics-based alternatives exhibit unsatisfactory performance in the target domain, ‘One reason is that ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (We evaluate the accuracy of a world model using ‘one-step error (44] which measures the distance between the ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (14 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** + We conduct real robot implementation to demonstrate that our approach enables learning control policies with minimal task-agnostic interaction data and attains high performance Real2Sim2Real without real-world fine-tuning. (p. 2, 2 Wuhan Universi).
- **Paper-supported outcome:** All policies are trained until no significant success rate performance can be gained and are then deployed directly to the target domain for evaluation, We also conduct an ablation study ... (p. 7, A. Evaluations in Simulation).
- **Strongest explicit boundary:** Moreover, the policies trained with physics-based alternatives exhibit unsatisfactory performance in the target domain, ‘One reason is that their world models failed to effectively ‘capture the target-domain dynamics. (p. 8, A. Evaluations in Simulation).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
