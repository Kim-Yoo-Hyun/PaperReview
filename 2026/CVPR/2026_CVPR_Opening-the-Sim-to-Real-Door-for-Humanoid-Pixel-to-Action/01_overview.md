# Opening the Sim-to-Real Door for Humanoid Pixel-to-Action Policy Transfer

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Xue_Opening_the_Sim-to-Real_Door_for_Humanoid_Pixel-to-Action_Policy_Transfer_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Xue_Opening_the_Sim-to-Real_Door_for_Humanoid_Pixel-to-Action_Policy_Transfer_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: Robotics, humanoid, pixel-to-action, visual sim-to-real, articulated object manipulation
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Xue_Opening_the_Sim-to-Real_Door_for_Humanoid_Pixel-to-Action_Policy_Transfer_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Xue_Opening_the_Sim-to-Real_Door_for_Humanoid_Pixel-to-Action_Policy_Transfer_CVPR_2026_paper.pdf
- Code/Project: https://openaccess.thecvf.com/content/CVPR2026/html/Xue_Opening_the_Sim-to-Real_Door_for_Humanoid_Pixel-to-Action_Policy_Transfer_CVPR_2026_paper.html
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 These requirements remain unmet in prior work; and (ii) the visual sim-to-real gap spans a vast space of appearance and physics variation, requiring broad, heterogeneous data rather than a few curated scenes.를 문제로 두고, To summarize, the main contributions of our work are: • We present the first end-to-end humanoid sim-to-real policy capable of diverse articulated loco-manipulation from pure RGB perception. • We introduce a teacher-student-bootstrap ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Recent progress in GPU-accelerated, photorealistic simulation has opened a scalable data-generation path for robot learning, where massive physics and visual randomization allow policies to generalize ...
- **p. 1 / Abstract - extractive body cue:** Building on these advances, we develop a teacher-student-bootstrap learning framework for visionbased humanoid loco-manipulation, using articulatedobject interaction as a representative high-difficulty benchmark.
- **p. 1 / Abstract - extractive body cue:** Our approach introduces a staged-reset exploration strategy that stabilizes long-horizon privileged-policy training, and a GRPO-based fine-tuning procedure designed to mitigate partial observability and improve closed-loop ...
- **p. 1 / Abstract - extractive body cue:** Trained entirely on synthetic simulation data, the resulting policy achieves robust zero-shot performance across diverse articulated objects-including multiple door types-and outperforms human teleoperators by up ...
- **p. 1 / 1. Introduction - extractive body cue:** The reality of robotics is that humanoid kung fu and backflips are solved before they can open doors using only RGB vision.
- **p. 2 / 1. Introduction - extractive body cue:** These requirements remain unmet in prior work; and (ii) the visual sim-to-real gap spans a vast space of appearance and physics variation, requiring broad, heterogeneous ...
- **p. 4 / 2.2. Multi-Stage Whole-Body Loco-Manipulation - extractive body cue:** These challenges have not been foreseen in the prior success of RL whole-body control literature.

## Core Idea

- **p. 3 / 1. Introduction - extractive body cue:** To summarize, the main contributions of our work are: • We present the first end-to-end humanoid sim-to-real policy capable of diverse articulated loco-manipulation from pure ...
- **p. 3 / 1. Introduction - extractive body cue:** To address the first challenge, we introduce a novel, scalable teacher-student-bootstrap learning pipeline.
- **p. 4 / 2.2. Multi-Stage Whole-Body Loco-Manipulation - extractive body cue:** Here, we present the design of a robust teacher training pipeline for whole-body loco-manipulation tasks.
- **p. 4 / 2.2. Multi-Stage Whole-Body Loco-Manipulation - extractive body cue:** To address this, we introduce a staged reset law α = (α1, . . . , αK), K X y=1 αy = 1, (1) which ...
- **p. 5 / 2.4. Massive-Scale Simulation Randomization - extractive body cue:** Compared with prior work such as InfinigenSim [21], our IsaacLab-native implementation significantly improves physical realism and enables contact simulation that is both accurate and efficient ...
- **p. 3 / 1. Introduction - extractive body cue:** To improve training efficiency, we introduce an exploration scheme that resets environments from late-stage snapshots, leveraging the recoverability of the simulator.
- **p. 6 / 2.4. Massive-Scale Simulation Randomization - extractive body cue:** To balance rendering quality and performance while training an RL policy in parallel, we use the RTX Real-Time renderer in performance mode, with post-processing effects ...
- **p. 5 / 2.3. RL Finetuning for Partial Observability - extractive body cue:** It is worth mentioning that during fine-tuning, we use mainly a binary task success signal, plus simple shaping reward terms such as joint velocity, joint ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | While the student policy has access to non-privileged proprioception information, such as joint angles q, joint velocities ˙q, and root angular velocities ˙ω ∈R3, its perception of the task relies mostly on ... | proprioception, reference pose/motion, visual or language command | p. 4 (2.1. Visual RL and Teacher-Student Distillation), p. 3 (2.1. Visual RL and Teacher-Student Distillation) |
| State/latent | While, student, policy, access, non-privileged, proprioception, information, joint, angles, velocities, root, angular | whole-body pose, balance/contact state와 skill/mode | p. 4 (2.1. Visual RL and Teacher-Student Distillation), p. 3 (2.1. Visual RL and Teacher-Student Distillation), p. 3 (2.1. Visual RL and Teacher-Student Distillation) |
| Output/action | In humanoid wholebody control literature, the policy is responsible for outputting target joint positions, which, in the case of a Unitree G1 robot, includes 29 body joints and 14 hand joints, resulting ... | joint/whole-body action, motion target 또는 task trajectory | p. 3 (2.1. Visual RL and Teacher-Student Distillation), p. 3 (2.1. Visual RL and Teacher-Student Distillation), p. 1 (Body text (section not recovered)) |
| Objective/outcome | We train the teacher policy using standard proximal policy optimization (PPO) [35], with the exact reward shaping recipe available in Appendix ??. | tracking, balance, skill/task success와 recovery | p. 4 (2.1. Visual RL and Teacher-Student Distillation), p. 4 (2.2. Multi-Stage Whole-Body Loco-Manipulation), p. 5 (2.3. RL Finetuning for Partial Observability) |

## Main Claims and Actual Contribution

- **p. 3 / 1. Introduction - extractive body cue:** To summarize, the main contributions of our work are: • We present the first end-to-end humanoid sim-to-real policy capable of diverse articulated loco-manipulation from pure ...
- **p. 3 / 1. Introduction - extractive body cue:** To address the first challenge, we introduce a novel, scalable teacher-student-bootstrap learning pipeline.
- **p. 4 / 2.2. Multi-Stage Whole-Body Loco-Manipulation - extractive body cue:** Here, we present the design of a robust teacher training pipeline for whole-body loco-manipulation tasks.
- **p. 4 / 2.2. Multi-Stage Whole-Body Loco-Manipulation - extractive body cue:** To address this, we introduce a staged reset law α = (α1, . . . , αK), K X y=1 αy = 1, (1) which ...
- **p. 5 / 2.4. Massive-Scale Simulation Randomization - extractive body cue:** Compared with prior work such as InfinigenSim [21], our IsaacLab-native implementation significantly improves physical realism and enables contact simulation that is both accurate and efficient ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 7. Training progress of student policy bootstrapping with improvements in task success rate. The dashed lines are teacher policy success rates. cies can consistently ...
- **p. 7 / 3.2. Effect of Photorealistic Visual Randomization - extractive body cue:** This setting achieves a commendable success rate of 65.8-70%.
- **p. 6 / 3.1. Surpassing Human-Teleop Baseline - extractive body cue:** We hypothesize that the current whole-body teleoperation technology, due to its unintuitive nature, create a gap in both efficiency and success rate compared to direct ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 7 (3.2. Effect of Photorealistic Visual Randomization) |
| Embodiment/environment | Real-world visuals are unseen during training. | hardware/simulator version and reset protocol | p. 6 (3.1. Surpassing Human-Teleop Baseline), p. 6 (3. Experiment) |
| Dataset/benchmark | Qualitatively, teleoperators often fail to gauge the spring-loaded force of the door handle and the door hinge, or whether the robot is leaning with the appropriate amount to maintain smooth and consistent ... | role, split, size and leakage | p. 6 (3.1. Surpassing Human-Teleop Baseline), p. 6 (3. Experiment), p. 7 (3.1. Surpassing Human-Teleop Baseline), p. 7 (3.4. Effect of Staged Reset Exploration) |
| Metric | Success rate and completion time are evaluated at when the robot traverses through the door and reaches a point 1 m beyond the door frame on the opposite side. | definition, denominator, direction and uncertainty | p. 6 (3.1. Surpassing Human-Teleop Baseline), p. 6 (3.1. Surpassing Human-Teleop Baseline), p. 7 (3.3. Performance Boost in GRPO Fine-Tuning) |
| Baseline/ablation | In this section, we will establish real-world comparison with human baselines. | fair input/data/compute/action matching | p. 6 (3. Experiment), p. 6 (3.1. Surpassing Human-Teleop Baseline), p. 7 (3.1. Surpassing Human-Teleop Baseline) |

## Explicit Limitations and Failure Boundary

- **p. 8 / Figure/Table caption - extractive body cue:** Figure 8. Teacher training progress with different reset buffer sizes of 0, 10 and 100. reset buffer, as the policy finds it difficult to enter ...
- **p. 7 / 3.4. Effect of Staged Reset Exploration - extractive body cue:** The exploration fails when not using the 6648
- **p. 8 / 5. Conclusion - extractive body cue:** Trained entirely in photorealistic simulation, the resulting policy achieves robust zero-shot performance on articulated-object interaction tasks, including diverse door configurations, and exceeds human teleoperation baselines ...
- **p. 7 / 3.1. Surpassing Human-Teleop Baseline - extractive body cue:** Qualitatively, teleoperators often fail to gauge the spring-loaded force of the door handle and the door hinge, or whether the robot is leaning with the ...

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 These requirements remain unmet in prior work; and (ii) the visual sim-to-real gap spans a vast space of appearance and physics variation, requiring broad, heterogeneous data rather than a few curated scenes.를 문제로 두고, To summarize, the main contributions of our work are: • We present the first end-to-end humanoid sim-to-real policy capable of diverse articulated loco-manipulation from pure RGB perception. • We introduce a teacher-student-bootstrap ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 4 (2.2. Multi-Stage Whole-Body Loco-Manipulation), p. 2 (1. Introduction), p. 3 (1. Introduction), p. 3 (1. Introduction), p. 3 (1. Introduction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
