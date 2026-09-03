# Problem - Demonstrating OK-Robot: What Really Matters in Integrating Open-Knowledge Models for Robotics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p091.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p091.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): We also find that using heuristics to counteract the robot's physical limitations can lead to a better success rate in the real world (see Section II-D.) • Several challenges still ...

## PDF Body Digest

- **p. 2 / Abstract - extractive body cue:** Remarkable progress has been made in recent years in the fields of vision, language, and robotics.
- **p. 2 / Abstract - extractive body cue:** We now have vision models capable of recognizing objects based on language queries, navigation systems that can effectively control mobile systems, and grasping models that ...
- **p. 2 / Abstract - extractive body cue:** Despite these advancements, general-purpose applications of robotics still lag behind, even though they rely on these fundamental capabilities of recognition, navigation, and grasping.
- **p. 2 / Abstract - extractive body cue:** In this paper, we adopt a systems-first approach to develop a new Open Knowledge-based robotics framework called OK-Robot.
- **p. 2 / Abstract - extractive body cue:** By combining Vision-Language Models (VLMs) for object detection, navigation primitives for movement, and grasping primitives for object manipulation, OK-Robot offers a integrated solution for pick-and-drop ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We also find that using heuristics to counteract the robot's physical limitations can lead to a better success rate in the real world (see Section ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** To highlight the difficulty of this problem, the recent NeurIPS 2023 challenge for open-vocabulary mobile manipulation (OVMM) [22] registered a success rate of 33% for ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | We also find that using heuristics to counteract the robot's physical limitations can lead to a better success rate in the real ... | mobile base와 one/two-arm manipulation environment | body wording is the source claim |
| Observation / input | Overall, through our experiments, we make the following observations: • Pre-trained VLMs are highly effective for openvocabulary navigation: Current open-vocabulary visionlanguage models ... | egocentric RGB-D, language/task goal, base-arm proprioception | exact sensor/frame/preprocessing from PDF body |
| State / latent | Overall, through, experiments, make, following, observations, Pre-trained, VLMs, highly, effective | map/object/contact state와 base-arm coordination decision | notation and tensor shape require body check |
| Output / action | Once, collected, RGB-D, images, along, camera, pose, positions | base motion plus arm/gripper action | exact unit/frame/decoder require body check |
| Target outcome | task completion and recovery | long-horizon task success, reachability, collision과 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | base-arm-object state and language/task goal; body terms: Overall, through, experiments, make, following, observations, Pre-trained, VLMs, highly, effective | p. 2 (I. INTRODUCTION), p. 5 (II. TECHNICAL COMPONENTS AND METHOD), p. 3 (II. TECHNICAL COMPONENTS AND METHOD) |
| Decision / output variable | base plus arm/gripper action; body terms: present, OK-Robot, Open, Knowledge, Robot, integrates, state-of-the-art, VLMs | p. 2 (I. INTRODUCTION), p. 3 (II. TECHNICAL COMPONENTS AND METHOD), p. 3 (II. TECHNICAL COMPONENTS AND METHOD) |
| Objective / loss / cost | long-horizon task utility under reachability/contact constraints; cue terms: Then, find, voxel, where, product, between, encoded, embedding | p. 3 (II. TECHNICAL COMPONENTS AND METHOD), p. 3 (II. TECHNICAL COMPONENTS AND METHOD), p. 5 (II. TECHNICAL COMPONENTS AND METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (II. TECHNICAL COMPONENTS AND METHOD), p. 4 (II. TECHNICAL COMPONENTS AND METHOD), p. 4 (II. TECHNICAL COMPONENTS AND METHOD) |
| Success / guarantee | task completion and recovery | p. 7 (III. EXPERIMENTS), p. 7 (III. EXPERIMENTS), p. 6 (III. EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / I. INTRODUCTION - extractive body cue:** To highlight the difficulty of this problem, the recent NeurIPS 2023 challenge for open-vocabulary mobile manipulation (OVMM) [22] registered a success rate of 33% for ...

## What the Paper Changes

PDF body contribution framing (p. 2 (I. INTRODUCTION), p. 3 (II. TECHNICAL COMPONENTS AND METHOD), p. 3 (II. TECHNICAL COMPONENTS AND METHOD), p. 4 (II. TECHNICAL COMPONENTS AND METHOD), p. 2 (I. INTRODUCTION)): We present OK-Robot, an Open Knowledge Robot that integrates state-of-the-art VLMs with powerful robotics primitives for navigation and grasping to enable pick-and-drop.

- **p. 3 / II. TECHNICAL COMPONENTS AND METHOD - extractive body cue:** The system we introduce is a combination of three primary subsystems combined on a Hello Robot: Stretch.
- **p. 3 / II. TECHNICAL COMPONENTS AND METHOD - extractive body cue:** This manual scan simply consists of taking a video of the home using the Record3D app on the iPhone, which results in a sequence of ...
- **p. 4 / II. TECHNICAL COMPONENTS AND METHOD - extractive body cue:** If -→p is the grasp point and -→a is the approach vector given by the grasping model, our robot gripper follows the following trajectory: ⟨-→p ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, this success rate is largely dependant on the "naturalness" of the environment, as we show that with improving the queries, decluttering the space, and ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | Grasping module limitations: One failure mode of our manipulation module comes from executing grasps from a pre-trained manipulation ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Robot hardware limitations: While our robot of choice, a Hello Robot: Stretch, is able to pick-and-drop a variety ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | 4) What are the failure modes of such a system and its individual components in real home environments? | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | As a result, each success and failure of the robot tells us something interesting about applying open-knowledge models ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

mobile_manipulation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (I. INTRODUCTION), p. 5 (II. TECHNICAL COMPONENTS AND METHOD), p. 3 (II. TECHNICAL COMPONENTS AND METHOD), p. 3 (II. TECHNICAL COMPONENTS AND METHOD). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 2 (I. INTRODUCTION), p. 5 (II. TECHNICAL COMPONENTS AND METHOD), p. 3 (II. TECHNICAL COMPONENTS AND METHOD), p. 3 (II. TECHNICAL COMPONENTS AND METHOD), objective p. 3 (II. TECHNICAL COMPONENTS AND METHOD), p. 3 (II. TECHNICAL COMPONENTS AND METHOD), p. 5 (II. TECHNICAL COMPONENTS AND METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (27 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** To highlight the difficulty of this problem, the recent NeurIPS 2023 challenge for open-vocabulary mobile manipulation (OVMM) [22] registered a success rate of 33% for the winning solution [23]. (p. 2, I. INTRODUCTION).
- **Formulation-changing contribution:** We present OK-Robot, an Open Knowledge Robot that integrates state-of-the-art VLMs with powerful robotics primitives for navigation and grasping to enable pick-and-drop. (p. 2, I. INTRODUCTION).
- **Assumption/failure evidence:** Grasping module limitations: One failure mode of our manipulation module comes from executing grasps from a pre-trained manipulation model's output based on a single RGB-D image. (p. 7, III. EXPERIMENTS).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
