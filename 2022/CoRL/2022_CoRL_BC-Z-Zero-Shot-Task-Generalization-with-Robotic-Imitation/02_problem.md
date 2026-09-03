# Problem - BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2202.02005; PDF retrieval source: https://arxiv.org/pdf/2202.02005. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction)): However, zero-shot generalization to new tasks remains a challenge, particularly when considering vision-based manipulation tasks that cover a breadth of skills (e.g., wiping, pushing, pick-and-place) with diverse objects.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** In this paper, we study the problem of enabling a vision-based robotic manipulation system to generalize to novel tasks, a long-standing challenge in robot learning.
- **p. 1 / Abstract - extractive body cue:** We approach the challenge from an imitation learning perspective, aiming to study how scaling and broadening the data collected can facilitate such generalization.
- **p. 1 / Abstract - extractive body cue:** To that end, we develop an interactive and flexible imitation learning system that can learn from both demonstrations and interventions and can be conditioned on ...
- **p. 1 / Abstract - extractive body cue:** When scaling data collection on a real robot to more than 100 distinct tasks, we find that this system can perform 24 unseen manipulation tasks ...
- **p. 1 / Abstract - extractive body cue:** Keywords: Zero-Shot Imitation Learning, Multi-Task Imitation, Deep Learning
- **p. 1 / 1 Introduction - extractive body cue:** However, zero-shot generalization to new tasks remains a challenge, particularly when considering vision-based manipulation tasks that cover a breadth of skills (e.g., wiping, pushing, pick-and-place) ...
- **p. 1 / 1 Introduction - extractive body cue:** Achieving such generalization depends on solving challenges relating to scaling up data collection and learning algorithms for diverse data.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, zero-shot generalization to new tasks remains a challenge, particularly when considering vision-based manipulation tasks that cover a breadth of skills (e.g., ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | Second, our system flexibly conditions the policy on different forms of task specification, including a language instruction or a video of a ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | Second, system, flexibly, conditions, policy, different, forms, task, specification, including | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | Another, limitation, lower, performance, video-conditioned, policy, encourages, future | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: Second, system, flexibly, conditions, policy, different, forms, task, specification, including | p. 1 (1 Introduction), p. 2 (1 Introduction), p. 8 (7 Discussion) |
| Decision / output variable | action, pose, option or chunk a; body terms: main, contribution, empirical, study, large-scale, interactive, imitation, learning | p. 2 (1 Introduction), p. 8 (7 Discussion), p. 2 (1 Introduction) |
| Objective / loss / cost | policy/action modeling objective; cue terms: not stated or recoverable in the selected PDF body | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | 본문 anchor 없음 |
| Success / guarantee | instruction-conditioned task success | p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 14 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive body cue:** Achieving such generalization depends on solving challenges relating to scaling up data collection and learning algorithms for diverse data.
- **p. 2 / 1 Introduction - extractive body cue:** Our main contribution is an empirical study of a large-scale interactive imitation learning system that solves a breadth of tasks, including zero-shot and few-shot generalization ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1 Introduction), p. 8 (7 Discussion), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (Abstract)): Our main contribution is an empirical study of a large-scale interactive imitation learning system that solves a breadth of tasks, including zero-shot and few-shot generalization to tasks not seen during ...

- **p. 8 / 7 Discussion - extractive body cue:** We presented a multi-task imitation learning system that combines flexible task embeddings with large-scale training on a 100-task demonstration dataset, enabling it to generalize to ...
- **p. 2 / 1 Introduction - extractive body cue:** We show this system produces a policy that is capable of generalizing zero-shot to new unseen tasks.
- **p. 1 / 1 Introduction - extractive body cue:** We develop an interactive imitation learning system with two key properties that enable high-quality data collection and generalization to entirely new tasks.
- **p. 1 / Abstract - extractive body cue:** In this paper, we study the problem of enabling a vision-based robotic manipulation system to generalize to novel tasks, a long-standing challenge in robot learning.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 20 | Figure 13: An example of adapting a sim image (left) to look real (right) using RetinaGAN [51]. environment ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Our system does have a number of limitations. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | A direction to address this limitation is to relabel the dataset with a variety of human-provided annotations [24], ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 13 | Table 5: Teleoperation buttons and controls. Control Function Right Controller (Arm) A Start recording, or mark demo as ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 1 (1 Introduction), p. 2 (1 Introduction), p. 8 (7 Discussion), p. 1 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), interface p. 1 (1 Introduction), p. 2 (1 Introduction), p. 8 (7 Discussion), p. 1 (1 Introduction), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (23 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** However, zero-shot generalization to new tasks remains a challenge, particularly when considering vision-based manipulation tasks that cover a breadth of skills (e.g., wiping, pushing, pick-and-place) with diverse objects. (p. 1, 1 Introduction).
- **Formulation-changing contribution:** We develop an interactive imitation learning system with two key properties that enable high-quality data collection and generalization to entirely new tasks. (p. 1, 1 Introduction).
- **Assumption/failure evidence:** Further, any collision of the robot base and arm (not including the gripper) with the environment counted as the task failure by the operator. (p. 20, C Featurization Details).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
