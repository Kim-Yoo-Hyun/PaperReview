# Problem - Opening the Sim-to-Real Door for Humanoid Pixel-to-Action Policy Transfer

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Xue_Opening_the_Sim-to-Real_Door_for_Humanoid_Pixel-to-Action_Policy_Transfer_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Xue_Opening_the_Sim-to-Real_Door_for_Humanoid_Pixel-to-Action_Policy_Transfer_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 4 (2.2. Multi-Stage Whole-Body Loco-Manipulation), p. 2 (1. Introduction), p. 3 (1. Introduction), p. 3 (1. Introduction)): These requirements remain unmet in prior work; and (ii) the visual sim-to-real gap spans a vast space of appearance and physics variation, requiring broad, heterogeneous data rather than a few ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Recent progress in GPU-accelerated, photorealistic simulation has opened a scalable data-generation path for robot learning, where massive physics and visual randomization allow policies to generalize ...
- **p. 1 / Abstract - extractive body cue:** Building on these advances, we develop a teacher-student-bootstrap learning framework for visionbased humanoid loco-manipulation, using articulatedobject interaction as a representative high-difficulty benchmark.
- **p. 1 / Abstract - extractive body cue:** Our approach introduces a staged-reset exploration strategy that stabilizes long-horizon privileged-policy training, and a GRPO-based fine-tuning procedure designed to mitigate partial observability and improve closed-loop ...
- **p. 1 / Abstract - extractive body cue:** Trained entirely on synthetic simulation data, the resulting policy achieves robust zero-shot performance across diverse articulated objects-including multiple door types-and outperforms human teleoperators by up ...
- **p. 1 / 1. Introduction - extractive body cue:** The reality of robotics is that humanoid kung fu and backflips are solved before they can open doors using only RGB vision.
- **p. 2 / 1. Introduction - extractive body cue:** These requirements remain unmet in prior work; and (ii) the visual sim-to-real gap spans a vast space of appearance and physics variation, requiring broad, heterogeneous ...
- **p. 4 / 2.2. Multi-Stage Whole-Body Loco-Manipulation - extractive body cue:** These challenges have not been foreseen in the prior success of RL whole-body control literature.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | These requirements remain unmet in prior work; and (ii) the visual sim-to-real gap spans a vast space of appearance and physics variation, ... | high-DoF humanoid whole-body dynamics와 contacts | body wording is the source claim |
| Observation / input | While the student policy has access to non-privileged proprioception information, such as joint angles q, joint velocities ˙q, and root angular velocities ... | proprioception, reference pose/motion, visual or language command | exact sensor/frame/preprocessing from PDF body |
| State / latent | While, student, policy, access, non-privileged, proprioception, information, joint, angles, velocities | whole-body pose, balance/contact state와 skill/mode | notation and tensor shape require body check |
| Output / action | Consider, partially, observable, Markov, decision, process, POMDP, where | joint/whole-body action, motion target 또는 task trajectory | exact unit/frame/decoder require body check |
| Target outcome | motion/task success and recovery | tracking, balance, skill/task success와 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | whole-body pose/contact/reference state; body terms: While, student, policy, access, non-privileged, proprioception, information, joint, angles, velocities | p. 4 (2.1. Visual RL and Teacher-Student Distillation), p. 3 (2.1. Visual RL and Teacher-Student Distillation), p. 3 (2.1. Visual RL and Teacher-Student Distillation) |
| Decision / output variable | joint/whole-body action; body terms: summarize, main, contributions, present, first, end-to-end, humanoid, sim-to-real | p. 3 (1. Introduction), p. 3 (1. Introduction), p. 4 (2.2. Multi-Stage Whole-Body Loco-Manipulation) |
| Objective / loss / cost | tracking/balance/task objective; cue terms: train, teacher, policy, standard, proximal, optimization, PPO, exact | p. 4 (2.2. Multi-Stage Whole-Body Loco-Manipulation), p. 4 (2.3. RL Finetuning for Partial Observability), p. 5 (2.3. RL Finetuning for Partial Observability) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (1. Introduction), p. 3 (1. Introduction), p. 5 (2.3. RL Finetuning for Partial Observability) |
| Success / guarantee | motion/task success and recovery | p. 6 (3.1. Surpassing Human-Teleop Baseline), p. 6 (3.1. Surpassing Human-Teleop Baseline), p. 7 (3.3. Performance Boost in GRPO Fine-Tuning) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 4 / 2.2. Multi-Stage Whole-Body Loco-Manipulation - extractive body cue:** These challenges have not been foreseen in the prior success of RL whole-body control literature.
- **p. 2 / 1. Introduction - extractive body cue:** DARPA-Robotics-Challenge-era systems [29] depended heavily on scripting and operator intervention, while more recent teleoperation-centered pipelines [22] remain brittle.
- **p. 3 / 1. Introduction - extractive body cue:** To address the first challenge, we introduce a novel, scalable teacher-student-bootstrap learning pipeline.
- **p. 3 / 1. Introduction - extractive body cue:** To tackle the second challenge, we build a large-scale domain randomization pipeline in IsaacLab [28] that spans both physics and appearance variation at scale.

## What the Paper Changes

PDF body contribution framing (p. 3 (1. Introduction), p. 3 (1. Introduction), p. 4 (2.2. Multi-Stage Whole-Body Loco-Manipulation), p. 4 (2.2. Multi-Stage Whole-Body Loco-Manipulation), p. 5 (2.4. Massive-Scale Simulation Randomization)): To summarize, the main contributions of our work are: • We present the first end-to-end humanoid sim-to-real policy capable of diverse articulated loco-manipulation from pure RGB perception. • We introduce ...

- **p. 3 / 1. Introduction - extractive body cue:** To address the first challenge, we introduce a novel, scalable teacher-student-bootstrap learning pipeline.
- **p. 4 / 2.2. Multi-Stage Whole-Body Loco-Manipulation - extractive body cue:** Here, we present the design of a robust teacher training pipeline for whole-body loco-manipulation tasks.
- **p. 4 / 2.2. Multi-Stage Whole-Body Loco-Manipulation - extractive body cue:** To address this, we introduce a staged reset law α = (α1, . . . , αK), K X y=1 αy = 1, (1) which ...
- **p. 5 / 2.4. Massive-Scale Simulation Randomization - extractive body cue:** Compared with prior work such as InfinigenSim [21], our IsaacLab-native implementation significantly improves physical realism and enables contact simulation that is both accurate and efficient ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Figure 8. Teacher training progress with different reset buffer sizes of 0, 10 and 100. reset buffer, as ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | The exploration fails when not using the 6648 | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Trained entirely in photorealistic simulation, the resulting policy achieves robust zero-shot performance on articulated-object interaction tasks, including diverse ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Qualitatively, teleoperators often fail to gauge the spring-loaded force of the door handle and the door hinge, or ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

humanoid writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (2.1. Visual RL and Teacher-Student Distillation), p. 3 (2.1. Visual RL and Teacher-Student Distillation), p. 3 (2.1. Visual RL and Teacher-Student Distillation), p. 1 (Body text (section not recovered)). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 4 (2.2. Multi-Stage Whole-Body Loco-Manipulation), p. 2 (1. Introduction), p. 3 (1. Introduction), p. 3 (1. Introduction), interface p. 4 (2.1. Visual RL and Teacher-Student Distillation), p. 3 (2.1. Visual RL and Teacher-Student Distillation), p. 3 (2.1. Visual RL and Teacher-Student Distillation), p. 1 (Body text (section not recovered)), objective p. 4 (2.2. Multi-Stage Whole-Body Loco-Manipulation), p. 4 (2.3. RL Finetuning for Partial Observability), p. 5 (2.3. RL Finetuning for Partial Observability).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
