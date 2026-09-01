# Flying Hand: End-Effector-Centric Framework for Versatile Aerial Manipulation Teleoperation and Policy Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (16 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p130.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p130.pdf. Reading tracker status/evidence was not changed.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: NEXT
- Tags: Robotics, aerial manipulation, whole-body control, teleoperation, Imitation Learning, assembly
- Official paper: https://www.roboticsproceedings.org/rss21/p130.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p130.pdf
- Code/Project: https://lecar-lab.github.io/flying_hand/
- Paper type: system
- Source audit: full-text PDF body checked on 2026-09-02 (16 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 However, most previous works have been tailored to specific tasks, developing unique platforms and algorithms accordingly, lacking the ability to handle different types of tasks, In real-world scenarios, manipulation tasks can be ...를 문제로 두고, Our framework consists of a fully-actuated hexarotor with a 4:DoF robotic arm, an end-effector-centrie whole-body: model predictive controller, and a high-level po is end-effector controller enables efficient and ‘operation for versatil ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Aerial manipulation has recently attracted inereasing interest from both industry and academia.
- **p. 1 / Abstract - extractive body cue:** Previous approaches have demonstrated success in various specific tasks.
- **p. 1 / Abstract - extractive body cue:** However, their hardware design and control frameworks are often tightly coupled with task specifications, limiting the detelopment of cros-las and crompatform algorithms, Ingpred by the ...
- **p. 1 / Abstract - extractive body cue:** Our framework consists of a fully-actuated hexarotor with a 4:DoF robotic arm, an end-effector-centrie whole-body: model predictive controller, and a high-level po is end-effector controller ...
- **p. 1 / Abstract - extractive body cue:** Real-world experiments show that the proposed framework significantly improves end-effector tracking accuracy and can handle multiple aerial teleoperation and tion learning tasks, including writing, peg-inchanging ...
- **p. 1 / 1. Iyrropuction - extractive body cue:** However, most previous works have been tailored to specific tasks, developing unique platforms and algorithms accordingly, lacking the ability to handle different types of tasks, ...
- **p. 3 / C. Teleportation and Imitation Learning - extractive body cue:** However, there is no precedent to incorporate such IL-based policy into aerial manipulation fields due to the lack of a mature demonstration collection system, such ...

## Core Idea

- **p. 1 / Abstract - extractive body cue:** Our framework consists of a fully-actuated hexarotor with a 4:DoF robotic arm, an end-effector-centrie whole-body: model predictive controller, and a high-level po is end-effector controller ...
- **p. 7 / VII. EE-CENTRIC TELEOPERATION AND POLICY - extractive body cue:** [As we mentioned, our framework enables the decoupling between the high-level policy and low-level controller, with the ee-centric interface serving asthe sole connection between them.
- **p. 2 / B. Mobile Manipulation Framework and EE-Centric Interface - extractive body cue:** [25] proposed a framework that consists of a robust humanoid whole-body controller with a high-level policy, either an autonomous agent like GPT-40 or an imitation ...
- **p. 7 / VII. EE-CENTRIC TELEOPERATION AND POLICY - extractive body cue:** In this section, we introduce two aerial manipulation systems we ‘developed based on this framework: the ee-centrc aerial tele- ‘operation system and the imitaton-Iearning-based autonomous ...
- **p. 2 / 1. Iyrropuction - extractive body cue:** By effectively decoupling high-level policies from low-level control, it enables the development ‘of embodiment-agnostic policies 47}, {10}.
- **p. 7 / B. EE-Centrie Policy Learning - extractive body cue:** The transformerbased decoder generates action sequences from the latent variable (only during training and set to be the mean of the prior during testing), current ...
- **p. 10 / B. Implementation Details - extractive body cue:** ‘To show the advantage of leaming from an ee-centric demonstration compared to a joint space demonstration, we use the same demonstration trajectory but change the ...
- **p. 7 / B. EE-Centrie Policy Learning - extractive body cue:** ACT utilizes a Conditional Variational Autoencoder (CVAE) where the encoder compresses action sequences and Joint observations into a latent style variable.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | After that, we train a joint space ACT policy with the same training setting as the ee-centric ACT policy, except that the end-effector pose in the observation and action space is replaced ... | proprioception, reference pose/motion, visual or language command | p. 10 (B. Implementation Details), p. 4 (C. Teleportation and Imitation Learning) |
| State/latent | After, train, joint, space, ACT, policy, same, training, setting, ee-centric, except, end-effector | whole-body pose, balance/contact state와 skill/mode | p. 10 (B. Implementation Details), p. 4 (C. Teleportation and Imitation Learning), p. 2 (B. Mobile Manipulation Framework and EE-Centric Interface) |
| Output/action | At the most highlevel, the ee-centric policy module gets current observations and generates the target end-effector states online without the need to consider the specific platform jointly. | joint/whole-body action, motion target 또는 task trajectory | p. 4 (C. Teleportation and Imitation Learning), p. 2 (B. Mobile Manipulation Framework and EE-Centric Interface), p. 7 (B. EE-Centrie Policy Learning) |
| Objective/outcome | ‘The MPC formulation minimizes a cost function over a finite time horizon H while subject to system dynamics and constraints: | tracking, balance, skill/task success와 recovery | p. 6 (A. End-Effector-Centric Model Predictive Controller), p. 6 (A. End-Effector-Centric Model Predictive Controller), p. 8 (B. Implementation Details) |

## Main Claims and Actual Contribution

- **p. 1 / Abstract - extractive body cue:** Our framework consists of a fully-actuated hexarotor with a 4:DoF robotic arm, an end-effector-centrie whole-body: model predictive controller, and a high-level po is end-effector controller ...
- **p. 7 / VII. EE-CENTRIC TELEOPERATION AND POLICY - extractive body cue:** [As we mentioned, our framework enables the decoupling between the high-level policy and low-level controller, with the ee-centric interface serving asthe sole connection between them.
- **p. 2 / B. Mobile Manipulation Framework and EE-Centric Interface - extractive body cue:** [25] proposed a framework that consists of a robust humanoid whole-body controller with a high-level policy, either an autonomous agent like GPT-40 or an imitation ...
- **p. 7 / VII. EE-CENTRIC TELEOPERATION AND POLICY - extractive body cue:** In this section, we introduce two aerial manipulation systems we ‘developed based on this framework: the ee-centrc aerial tele- ‘operation system and the imitaton-Iearning-based autonomous ...
- **p. 2 / 1. Iyrropuction - extractive body cue:** By effectively decoupling high-level policies from low-level control, it enables the development ‘of embodiment-agnostic policies 47}, {10}.
- **p. 9 / B. Implementation Details - extractive body cue:** improvements can be achieved through more accurate system modeling and higher-precision hardware to enhance tracking accuracy.
- **p. 10 / B. Implementation Details - extractive body cue:** + Multi-Skill Composition: In the open and retrieve task, our ee-centric policy achieves 2 higher success rate than the joint space policy, which demonstrates its ...
- **p. 10 / B. Implementation Details - extractive body cue:** + Geometric Precision Advantage: Our ee-centric policy achieves 2.5% higher success rate in geometrically sensitive peg in hole task, directly benefiting from task-space supervision that ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 9 (B. Implementation Details), p. 10 (B. Implementation Details) |
| Embodiment/environment | Some work also showed amazing results, achieving high-speed grasping, or grasping moving objects [50], but sacrificed payload capacity or precision due to specialized hardware designs. | hardware/simulator version and reset protocol | p. 2 (4) Rich real-world experiments demonstrated the versatility), p. 2 (4) Rich real-world experiments demonstrated the versatility) |
| Dataset/benchmark | 2) Real-world Experiments: We adopt the aerial peg-inhole task to demonstrate our capability to derive an autonomous policy from human demonstrations for aerial manipulation in the real world. ‘The task configurations are ... | role, split, size and leakage | p. 2 (4) Rich real-world experiments demonstrated the versatility), p. 2 (4) Rich real-world experiments demonstrated the versatility), p. 10 (B. Implementation Details), p. 10 (B. Implementation Details) |
| Metric | + Geometric Precision Advantage: Our ee-centric policy achieves 2.5% higher success rate in geometrically sensitive peg in hole task, directly benefiting from task-space supervision that eliminates the accumulated end-effector error fro ... | definition, denominator, direction and uncertainty | p. 10 (B. Implementation Details), p. 11 (B. Implementation Details), p. 10 (B. Implementation Details) |
| Baseline/ablation | 4, compared with our method (blue), the baseline wo. | fair input/data/compute/action matching | p. 8 (B. Implementation Details), p. 7 (A. Experimental Setup), p. 7 (A. Experimental Setup) |

## Explicit Limitations and Failure Boundary

- **p. 11 / IX. LIMITATIONS - extractive body cue:** Although we have demonstrated the proposed framework through various real-world experiments, there are still several limitations due to time constraints and methodological limitations.
- **p. 11 / IX. LIMITATIONS - extractive body cue:** Incorporating onboard perception to detect obstacles and generate safety constraints in real-time will be our next step, as various studies have demonstrated the feasibility of ...
- **p. 8 / B. Implementation Details - extractive body cue:** MPC (orange) suffers from significant motion lag, as DFFC fails to account for trajectory feedforward.
- **p. 7 / A. Experimental Setup - extractive body cue:** LI: This baseline excludes the L1 adaptive component, leaving disturbances from UAV and manipulator interactions and modeling uncertainties uncompensated during control execution.
- **p. 8 / B. Implementation Details - extractive body cue:** 8 shows disturbances along the base x (red), = (blue) and Open (green), respectively. ‘The disturbances and model uncertainties primarily arise from arm motions, inaccurate ...
- **p. 9 / B. Implementation Details - extractive body cue:** 7 reveals that tracking error increases at lower altitudes (around Im), likely due to unmodeled ground and wall effect disturbances.
- **p. 10 / B. Implementation Details - extractive body cue:** Disturbance zeae and LI disturbance

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 However, most previous works have been tailored to specific tasks, developing unique platforms and algorithms accordingly, lacking the ability to handle different types of tasks, In real-world scenarios, manipulation tasks can be ...를 문제로 두고, Our framework consists of a fully-actuated hexarotor with a 4:DoF robotic arm, an end-effector-centrie whole-body: model predictive controller, and a high-level po is end-effector controller enables efficient and ‘operation for versatil ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Iyrropuction), p. 3 (C. Teleportation and Imitation Learning), p. 2 (1. Iyrropuction), p. 3 (C. Teleportation and Imitation Learning), p. 2 (1. Iyrropuction), p. 7 (B. EE-Centrie Policy Learning) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
