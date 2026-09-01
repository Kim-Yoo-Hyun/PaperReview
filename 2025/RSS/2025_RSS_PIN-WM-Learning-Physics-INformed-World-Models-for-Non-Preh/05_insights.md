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
- **p. 1 / Front matter - extractive body cue:** *Shenzhen University "Equal contributions
- **p. 3 / B. World Models for Policy Learning - extractive body cue:** In contrast, PIN-WM enables end-to-end identification of 3D rigid-body dynamics from visual observations using few-shot, task-agnostic interaction data, which facilitates the training of vision-based manipulation ...
- **p. 5 / B. Physics-INformed World Model - extractive body cue:** We formulate this system identification process as a velocity-based Linear Complementarity Problem (LCP) [16, 68] which solves the equations of motion under global constraints, Here, ...
- **p. 3 / B. World Models for Policy Learning - extractive body cue:** DINOWM [84] leverages spatial patch features pre-trained with DINOv2 to learn a world model and achieve task-agnostic behavior planning by treating goal features as prediction ...
- **Contribution anchor:** p. 2 (2 Wuhan Universi), p. 2 (2 Wuhan Universi), p. 3 (C. Domain Randomization), p. 1 (Front matter), p. 3 (B. World Models for Policy Learning), p. 5 (B. Physics-INformed World Model)

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

- **Closed-loop position:** `observation, uncertainty/risk estimate와 task command → safe set, recovery state 또는 constraint margin → shielded, recovery 또는 safe action`.
- 이 논문의 재사용 가능한 지점은 Adopting differentiable physics simulation, PIN-WM can be learned with few-shot and task-agnostic physical interaction trajectories. ‘observational loss induced ‘aussian Splatting without needing state estimation.를 The transformed observations = {Z(,e¢°)} 4 are then obtained in simulation with Equation 5, where x - G(X+++-1) At+s-1, 8) is the updated state when applying action ¢«-1- The physics parameter 8 ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 safe set, recovery state 또는 constraint margin가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Since neither of the two methods learns rendering parameters and their trained policies cannot work without aligned visual input, we add our rendering function Z to enhance these two methods.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: We introduce PIN-WM, a Physies-INformed World Mode! that allows end-to-end identification of a 3D rigid body ‘dynamical system from visual observations.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `World models, safety, uncertainty, and recovery`; tags: `Robotics, world model, physics-informed learning, non-prehensile manipulation`.
- **Reading predecessor in the generated track queue:** Mastering Diverse Domains through World Models (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Since neither of the two methods learns rendering parameters and their trained policies cannot work without aligned visual input, we add our rendering function Z to enhance these two methods.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Experiment setup: n simulation, we collect a single task-agnostc trajectory thatthe target object is pushed forward along a straight line by the robot end-effector for a predefined distance in the target domain..
3. Compare against the body-reported baseline or a matched simpler baseline: Note that all physics-based methods being compared are trained with the same task-agnostic trajectories as PIN-WM, for fair comparison..
4. Report the body metric and its denominator/aggregation: All RL-based policies are trained using PPO [66], with the same model architecture, reward function, hyperparameters, and stopping criterion based on the success rate..
5. Re-run the body-reported ablation/failure condition: All policies are trained until no significant success rate performance can be gained and are then deployed directly to the target domain for evaluation, We also conduct an ablation study of our ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (B. Physics-INformed World Model), p. 3 (B. World Models for Policy Learning), p. 5 (B. Physics-INformed World Model); the primary result is directionally consistent at p. 7 (A. Evaluations in Simulation), p. 8 (A. Evaluations in Simulation), p. 8 (A. Evaluations in Simulation); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 introduce, PIN-WM, Physies-INformed mechanism이 Note that all physics-based methods being compared are trained with the same task-agnostic trajectories as PIN-WM, ... 대비 All RL-based policies are trained using PPO [66], with the same model architecture, reward function, hyperparameters, and stopping ...을 개선하고, Since neither of the two methods learns rendering parameters and their trained policies cannot work without ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
