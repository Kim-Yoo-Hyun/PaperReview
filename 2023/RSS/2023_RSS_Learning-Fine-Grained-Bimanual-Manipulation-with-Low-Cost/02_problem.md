# Problem - Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2304.13705; PDF retrieval source: https://arxiv.org/pdf/2304.13705. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): However, low-cost hardware is inevitably less precise than high-end platforms, making the sensing and planning challenge more pronounced.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Fine manipulation tasks, such as threading cable ties or slotting a battery, are notoriously difficult for robots because they require precision, careful coordination of contact ...
- **p. 1 / Abstract - extractive body cue:** Performing these tasks typically requires high-end robots, accurate sensors, or careful calibration, which can be expensive and difficult to set up.
- **p. 1 / Abstract - extractive body cue:** Can learning enable low-cost and imprecise hardware to perform these fine manipulation tasks?
- **p. 1 / Abstract - extractive body cue:** We present a low-cost system that performs end-to-end imitation learning directly from real demonstrations, collected with a custom teleoperation interface.
- **p. 1 / Abstract - extractive body cue:** Imitation learning, however, presents its own challenges, particularly in highprecision domains: errors in the policy can compound over time, and human demonstrations can be non-stationary.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, low-cost hardware is inevitably less precise than high-end platforms, making the sensing and planning challenge more pronounced.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Millimeters of error would lead to task failure.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, low-cost hardware is inevitably less precise than high-end platforms, making the sensing and planning challenge more pronounced. | rigid/articulated object와 robot manipulator contact scene | body wording is the source claim |
| Observation / input | Thus with action chunking, the policy outputs a k × 14 tensor given the current observation. | RGB-D/point cloud, object state와 contact/task observation | exact sensor/frame/preprocessing from PDF body |
| State / latent | Thus, action, chunking, policy, outputs, tensor, given, current, observation, CVAE | object geometry, affordance, contact mode 또는 end-effector state | notation and tensor shape require body check |
| Output / action | system, therefore, train, end-to-end, policy, directly, maps, RGB | grasp, pose, force 또는 end-effector trajectory | exact unit/frame/decoder require body check |
| Target outcome | completion, contact success and robustness | task completion, contact success, pose/force error와 generalization | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | object geometry/contact state; body terms: Thus, action, chunking, policy, outputs, tensor, given, current, observation, CVAE | p. 5 (IV. ACTION CHUNKING WITH TRANSFORMERS), p. 5 (IV. ACTION CHUNKING WITH TRANSFORMERS), p. 1 (I. INTRODUCTION) |
| Decision / output variable | grasp/pose/force/trajectory; body terms: contribution, low-cost, system, learning, fine, manipulation, comprising, teleoperation | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Objective / loss / cost | task/contact/pose objective; cue terms: whole, model, trained, maximize, log-likelihood, demonstration, action, chunks | p. 5 (IV. ACTION CHUNKING WITH TRANSFORMERS), p. 4 (IV. ACTION CHUNKING WITH TRANSFORMERS), p. 5 (IV. ACTION CHUNKING WITH TRANSFORMERS), p. 6 (IV. ACTION CHUNKING WITH TRANSFORMERS) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (IV. ACTION CHUNKING WITH TRANSFORMERS), p. 5 (IV. ACTION CHUNKING WITH TRANSFORMERS), p. 6 (IV. ACTION CHUNKING WITH TRANSFORMERS) |
| Success / guarantee | completion, contact success and robustness | p. 8 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS), p. 9 (V. EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / I. INTRODUCTION - extractive body cue:** Training an end-to-end policy, however, presents its own challenges.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Millimeters of error would lead to task failure.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Tasks that require precision and visual feedback present a significant challenge for imitation learning, even with high-quality demonstrations.

## What the Paper Changes

PDF body contribution framing (p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 4 (IV. ACTION CHUNKING WITH TRANSFORMERS), p. 5 (IV. ACTION CHUNKING WITH TRANSFORMERS)): The key contribution of this paper is a low-cost system for learning fine manipulation, comprising a teleoperation system and a novel imitation learning algorithm.

- **p. 2 / I. INTRODUCTION - extractive body cue:** To further improve the smoothness of the policy, we propose temporal ensembling, which queries the policy more frequently and averages across the overlapping action chunks.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we seek to develop a low-cost system for fine manipulation that is, in contrast, accessible and reproducible.
- **p. 4 / IV. ACTION CHUNKING WITH TRANSFORMERS - extractive body cue:** We therefore develop a novel algorithm, Action Chunking with Transformers (ACT), to leverage the data collected by ALOHA.
- **p. 5 / IV. ACTION CHUNKING WITH TRANSFORMERS - extractive body cue:** Implementing ACT We implement the CVAE encoder and decoder with transformers, as transformers are designed for both synthesizing information across a sequence and generating new ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | Due to the small clearance between the cube and the left gripper (around 1cm), small errors could result ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | The failure modes we observe are 1) at stage 2, the right arm closes its gripper too early ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Because of the cup's small size, the grippers cannot grasp the body of the cup by just approaching ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | The left arm then lays the tape segment flat on the surface of the box while the right ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

manipulation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 5 (IV. ACTION CHUNKING WITH TRANSFORMERS), p. 5 (IV. ACTION CHUNKING WITH TRANSFORMERS), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 5 (IV. ACTION CHUNKING WITH TRANSFORMERS), p. 5 (IV. ACTION CHUNKING WITH TRANSFORMERS), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), objective p. 5 (IV. ACTION CHUNKING WITH TRANSFORMERS), p. 4 (IV. ACTION CHUNKING WITH TRANSFORMERS), p. 5 (IV. ACTION CHUNKING WITH TRANSFORMERS), p. 6 (IV. ACTION CHUNKING WITH TRANSFORMERS).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** However, low-cost hardware is inevitably less precise than high-end platforms, making the sensing and planning challenge more pronounced. (p. 1, I. INTRODUCTION).
- **Formulation-changing contribution:** The key contribution of this paper is a low-cost system for learning fine manipulation, comprising a teleoperation system and a novel imitation learning algorithm. (p. 2, I. INTRODUCTION).
- **Assumption/failure evidence:** Due to the small clearance between the cube and the left gripper (around 1cm), small errors could result in collisions and task failure. (p. 6, V. EXPERIMENTS).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
