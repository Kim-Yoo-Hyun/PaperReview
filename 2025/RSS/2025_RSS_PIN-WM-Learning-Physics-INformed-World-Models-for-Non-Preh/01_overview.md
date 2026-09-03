# PIN-WM: Learning Physics-INformed World Models for Non-Prehensile Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p153.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p153.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: Robotics, world model, physics-informed learning, non-prehensile manipulation
- Official paper: https://www.roboticsproceedings.org/rss21/p153.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p153.pdf
- Code/Project: https://www.roboticsproceedings.org/rss21/p153.html
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (14 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 However, significant challenges arise from the difficulty of fully dictating. the motion and pose of the object being pushed.를 문제로 두고, We introduce PIN-WM, a Physies-INformed World Mode! that allows end-to-end identification of a 3D rigid body ‘dynamical system from visual observations.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** While non-prehensile manipulation (e.g, controlled. pushing/poking) constitutes a foundational robotic skil, its learning remains challenging due to the high sensitivity to comple physical interactions involving ...
- **p. 1 / Abstract - extractive body cue:** To achieve robust policy learning and generalization, we opt to learn a world model of the 3D rigid body dynamics involved in nonprehensile manipulations and ...
- **p. 1 / Abstract - extractive body cue:** Adopting differentiable physics simulation, PIN-WM can be learned with few-shot and task-agnostic physical interaction trajectories. ‘observational loss induced ‘aussian Splatting without needing state estimation.
- **p. 1 / Abstract - extractive body cue:** To bridge Sim2Real gaps, we turn the learned PIN-WM into a group of Digital Cousins via perturb physics and rendering parameters to generate diverse and ...
- **p. 1 / Abstract - extractive body cue:** learning robust non-prehensile manipulation skills with Sim2Real transfer, surpassing the Real2Sim2Real state-of-the-arts.
- **p. 1 / 1. Iyrropuction - extractive body cue:** However, significant challenges arise from the difficulty of fully dictating. the motion and pose of the object being pushed.
- **p. 2 / A. Non-Prehensile Manipulation - extractive body cue:** However, the large gap between simulation and reality poses significant cha lenges for transferring these policies to the real world [12, 45], Building an interactive ...

## Core Idea

- **p. 2 / 2 Wuhan Universi - extractive body cue:** We introduce PIN-WM, a Physies-INformed World Mode! that allows end-to-end identification of a 3D rigid body ‘dynamical system from visual observations.
- **p. 2 / 2 Wuhan Universi - extractive body cue:** + We conduct real robot implementation to demonstrate that our approach enables learning control policies with minimal task-agnostic interaction data and attains high performance Real2Sim2Real ...
- **p. 3 / C. Domain Randomization - extractive body cue:** We provide an overview of our framework in Figure 2
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** *Shenzhen University ".
- **p. 3 / B. World Models for Policy Learning - extractive body cue:** In contrast, PIN-WM enables end-to-end identification of 3D rigid-body dynamics from visual observations using few-shot, task-agnostic interaction data, which facilitates the training of vision-based manipulation ...
- **p. 5 / B. Physics-INformed World Model - extractive body cue:** We formulate this system identification process as a velocity-based Linear Complementarity Problem (LCP) [16, 68] which solves the equations of motion under global constraints, Here, ...
- **p. 3 / B. World Models for Policy Learning - extractive body cue:** DINOWM [84] leverages spatial patch features pre-trained with DINOv2 to learn a world model and achieve task-agnostic behavior planning by treating goal features as prediction ...
- **p. 5 / B. Physics-INformed World Model - extractive body cue:** The transformed observations = {Z(,e¢°)} 4 are then obtained in simulation with Equation 5, where x - G(X+++-1) At+s-1, 8) is the updated state when ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Adopting differentiable physics simulation, PIN-WM can be learned with few-shot and task-agnostic physical interaction trajectories. ‘observational loss induced ‘aussian Splatting without needing state estimation. | observation, uncertainty/risk estimate와 task command | p. 1 (Abstract), p. 5 (B. Physics-INformed World Model) |
| State/latent | Adopting, differentiable, physics, simulation, PIN-WM, learned, few-shot, task-agnostic, physical, interaction, trajectories, observational | safe set, recovery state 또는 constraint margin | p. 1 (Abstract), p. 5 (B. Physics-INformed World Model), p. 14 (A. Implementation Details for Baselines) |
| Output/action | The transformed observations = {Z(,e¢°)} 4 are then obtained in simulation with Equation 5, where x - G(X+++-1) At+s-1, 8) is the updated state when applying action ¢«-1- The physics parameter 8 ... | shielded, recovery 또는 safe action | p. 5 (B. Physics-INformed World Model), p. 14 (A. Implementation Details for Baselines), p. 1 (Abstract) |
| Objective/outcome | The transformed observations = {Z(,e¢°)} 4 are then obtained in simulation with Equation 5, where x - G(X+++-1) At+s-1, 8) is the updated state when applying action ¢«-1- The physics parameter 8 ... | task return과 violation/failure probability | p. 5 (B. Physics-INformed World Model), p. 5 (B. Physics-INformed World Model), p. 6 (B. Physics-INformed World Model) |

## Main Claims and Actual Contribution

- **p. 2 / 2 Wuhan Universi - extractive body cue:** We introduce PIN-WM, a Physies-INformed World Mode! that allows end-to-end identification of a 3D rigid body ‘dynamical system from visual observations.
- **p. 2 / 2 Wuhan Universi - extractive body cue:** + We conduct real robot implementation to demonstrate that our approach enables learning control policies with minimal task-agnostic interaction data and attains high performance Real2Sim2Real ...
- **p. 3 / C. Domain Randomization - extractive body cue:** We provide an overview of our framework in Figure 2
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** *Shenzhen University ".
- **p. 3 / B. World Models for Policy Learning - extractive body cue:** In contrast, PIN-WM enables end-to-end identification of 3D rigid-body dynamics from visual observations using few-shot, task-agnostic interaction data, which facilitates the training of vision-based manipulation ...
- **p. 7 / A. Evaluations in Simulation - extractive body cue:** All policies are trained until no significant success rate performance can be gained and are then deployed directly to the target domain for evaluation, We ...
- **p. 8 / A. Evaluations in Simulation - extractive body cue:** Without PADC, our method still outperforms others, although with a performance decrease.
- **p. 8 / A. Evaluations in Simulation - extractive body cue:** Our method achieves the best performance for both non-prehensile manipulation tasks, thanks to the accurate system identification of PIN-WM and the meaningful digital cousins of ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (A. Evaluations in Simulation), p. 8 (A. Evaluations in Simulation) |
| Embodiment/environment | Experiment setup: n simulation, we collect a single task-agnostc trajectory thatthe target object is pushed forward along a straight line by the robot end-effector for a predefined distance in the target domain. | hardware/simulator version and reset protocol | p. 7 (A. Evaluations in Simulation), p. 8 (B. Evaluations in Real-World) |
| Dataset/benchmark | ‘We evaluate our method on rigid body motion control. ‘The robot's objective is to perform a sequence of non-prehensile actions to move an object into a target pose. | role, split, size and leakage | p. 7 (A. Evaluations in Simulation), p. 8 (B. Evaluations in Real-World), p. 6 (IV. RESULTS AND EVALUATIONS), p. 6 (IV. RESULTS AND EVALUATIONS) |
| Metric | All RL-based policies are trained using PPO [66], with the same model architecture, reward function, hyperparameters, and stopping criterion based on the success rate. | definition, denominator, direction and uncertainty | p. 14 (A. Implementation Details for Baselines), p. 7 (A. Evaluations in Simulation), p. 7 (A. Evaluations in Simulation) |
| Baseline/ablation | Note that all physics-based methods being compared are trained with the same task-agnostic trajectories as PIN-WM, for fair comparison. | fair input/data/compute/action matching | p. 7 (A. Evaluations in Simulation), p. 8 (A. Evaluations in Simulation), p. 6 (IV. RESULTS AND EVALUATIONS) |

## Explicit Limitations and Failure Boundary

- **p. 7 / A. Evaluations in Simulation - extractive body cue:** Since neither of the two methods learns rendering parameters and their trained policies cannot work without aligned visual input, we add our rendering function Z ...
- **p. 8 / A. Evaluations in Simulation - extractive body cue:** The purely data-driven world model Dreamer V2 [27], albeit having access to more task-agnostic data, fails to accurately approximate the dynamics of the target domain, ...
- **p. 14 / Figure/Table caption - extractive body cue:** Fig. 10: Push cube object on a slippery plane.
- **p. 8 / A. Evaluations in Simulation - extractive body cue:** We can observe that Dreamer V2 quickly converges on the training dataset, but it does not generalize well on the test dataset.
- **p. 7 / A. Evaluations in Simulation - extractive body cue:** ‘¢ Methods that rely purely on data. representative is the well-known Dreamer V2 [27], which is a latent-space dynamies model from data for handling high-dimensional ...

## Why Read It

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 However, significant challenges arise from the difficulty of fully dictating. the motion and pose of the object being pushed.를 문제로 두고, We introduce PIN-WM, a Physies-INformed World Mode! that allows end-to-end identification of a 3D rigid body ‘dynamical system from visual observations.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Iyrropuction), p. 2 (A. Non-Prehensile Manipulation), p. 1 (1. Iyrropuction), p. 2 (2 Wuhan Universi), p. 3 (B. World Models for Policy Learning), p. 5 (B. Physics-INformed World Model) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (14 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, significant challenges arise from the difficulty of fully dictating. the motion and pose of the object being pushed. (p. 1, 1. Iyrropuction).
- **Actual contribution:** + We conduct real robot implementation to demonstrate that our approach enables learning control policies with minimal task-agnostic interaction data and attains high performance Real2Sim2Real without real-world fine-tuning. (p. 2, 2 Wuhan Universi).
- **Evaluation boundary:** All policies are trained until no significant success rate performance can be gained and are then deployed directly to the target domain for evaluation, We also conduct an ablation study ... (p. 7, A. Evaluations in Simulation).
- **Explicit failure boundary:** Moreover, the policies trained with physics-based alternatives exhibit unsatisfactory performance in the target domain, ‘One reason is that their world models failed to effectively ‘capture the target-domain dynamics. (p. 8, A. Evaluations in Simulation).
