# Demonstrating OK-Robot: What Really Matters in Integrating Open-Knowledge Models for Robotics

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (27 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss20/p091.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss20/p091.pdf. Reading tracker status/evidence was not changed.

- Year/Venue: 2024 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: NEXT
- Tags: Robotics, mobile manipulation, open-vocabulary perception, home robotics
- Official paper: https://www.roboticsproceedings.org/rss20/p091.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss20/p091.pdf
- Code/Project: https://ok-robot.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (27 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 mobile_manipulation 문제를 이해하기 위해 읽는다. 본문은 We also find that using heuristics to counteract the robot's physical limitations can lead to a better success rate in the real world (see Section II-D.) • Several challenges still remain: While, ...를 문제로 두고, We present OK-Robot, an Open Knowledge Robot that integrates state-of-the-art VLMs with powerful robotics primitives for navigation and grasping to enable pick-and-drop.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 2 / Abstract - extractive body cue:** Remarkable progress has been made in recent years in the fields of vision, language, and robotics.
- **p. 2 / Abstract - extractive body cue:** We now have vision models capable of recognizing objects based on language queries, navigation systems that can effectively control mobile systems, and grasping models that ...
- **p. 2 / Abstract - extractive body cue:** Despite these advancements, general-purpose applications of robotics still lag behind, even though they rely on these fundamental capabilities of recognition, navigation, and grasping.
- **p. 2 / Abstract - extractive body cue:** In this paper, we adopt a systems-first approach to develop a new Open Knowledge-based robotics framework called OK-Robot.
- **p. 2 / Abstract - extractive body cue:** By combining Vision-Language Models (VLMs) for object detection, navigation primitives for movement, and grasping primitives for object manipulation, OK-Robot offers a integrated solution for pick-and-drop ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We also find that using heuristics to counteract the robot's physical limitations can lead to a better success rate in the real world (see Section ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** To highlight the difficulty of this problem, the recent NeurIPS 2023 challenge for open-vocabulary mobile manipulation (OVMM) [22] registered a success rate of 33% for ...

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** We present OK-Robot, an Open Knowledge Robot that integrates state-of-the-art VLMs with powerful robotics primitives for navigation and grasping to enable pick-and-drop.
- **p. 3 / II. TECHNICAL COMPONENTS AND METHOD - extractive body cue:** The system we introduce is a combination of three primary subsystems combined on a Hello Robot: Stretch.
- **p. 3 / II. TECHNICAL COMPONENTS AND METHOD - extractive body cue:** This manual scan simply consists of taking a video of the home using the Record3D app on the iPhone, which results in a sequence of ...
- **p. 4 / II. TECHNICAL COMPONENTS AND METHOD - extractive body cue:** If -→p is the grasp point and -→a is the approach vector given by the grasping model, our robot gripper follows the following trajectory: ⟨-→p ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Hence, making progress on this problem requires a careful and nuanced framework that both integrates * Denotes equal contribution and † denotes equal advising.
- **p. 3 / II. TECHNICAL COMPONENTS AND METHOD - extractive body cue:** Open-home, open-vocabulary object navigation The first component of our method is an open-home, openvocabulary object navigation model that we use to map a home and ...
- **p. 3 / II. TECHNICAL COMPONENTS AND METHOD - extractive body cue:** Navigating to objects in the real world: Once our navigation model gives us a 3D location coordinate in the real world, we use that as ...
- **p. 4 / II. TECHNICAL COMPONENTS AND METHOD - extractive body cue:** We use the VoxelMap [25] for localizing objects with natural language queries, and use an A* algorithm similar to USANet [26] for path planning.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Overall, through our experiments, we make the following observations: • Pre-trained VLMs are highly effective for openvocabulary navigation: Current open-vocabulary visionlanguage models such as CLIP [9] or OWL-ViT [8] offer strong perf ... | egocentric RGB-D, language/task goal, base-arm proprioception | p. 2 (I. INTRODUCTION), p. 5 (II. TECHNICAL COMPONENTS AND METHOD) |
| State/latent | Overall, through, experiments, make, following, observations, Pre-trained, VLMs, highly, effective, openvocabulary, navigation | map/object/contact state와 base-arm coordination decision | p. 2 (I. INTRODUCTION), p. 5 (II. TECHNICAL COMPONENTS AND METHOD), p. 3 (II. TECHNICAL COMPONENTS AND METHOD) |
| Output/action | Since we do not implement error detection or correction, our state machine model is a simple linear chain of steps leading from navigating to object, to grasping, to navigating to goal, and ... | base motion plus arm/gripper action | p. 5 (II. TECHNICAL COMPONENTS AND METHOD), p. 3 (II. TECHNICAL COMPONENTS AND METHOD), p. 3 (II. TECHNICAL COMPONENTS AND METHOD) |
| Objective/outcome | Then, we find the voxel where the dot product between the encoded embedding and the voxel's associated embedding is maximized. | long-horizon task success, reachability, collision과 recovery | p. 3 (II. TECHNICAL COMPONENTS AND METHOD), p. 3 (II. TECHNICAL COMPONENTS AND METHOD), p. 4 (II. TECHNICAL COMPONENTS AND METHOD) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** We present OK-Robot, an Open Knowledge Robot that integrates state-of-the-art VLMs with powerful robotics primitives for navigation and grasping to enable pick-and-drop.
- **p. 3 / II. TECHNICAL COMPONENTS AND METHOD - extractive body cue:** The system we introduce is a combination of three primary subsystems combined on a Hello Robot: Stretch.
- **p. 3 / II. TECHNICAL COMPONENTS AND METHOD - extractive body cue:** This manual scan simply consists of taking a video of the home using the Record3D app on the iPhone, which results in a sequence of ...
- **p. 4 / II. TECHNICAL COMPONENTS AND METHOD - extractive body cue:** If -→p is the grasp point and -→a is the approach vector given by the grasping model, our robot gripper follows the following trajectory: ⟨-→p ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Hence, making progress on this problem requires a careful and nuanced framework that both integrates * Denotes equal contribution and † denotes equal advising.
- **p. 6 / III. EXPERIMENTS - extractive body cue:** Results of home experiments Over the 10 home environment, OK-Robot achieved a 58.5% success rates in completing full pick-and-drops.
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: OK-Robot is an Open Knowledge robotic system, which integrates a variety of learned models trained on publicly available data, to pick and drop ...
- **p. 7 / III. EXPERIMENTS - extractive body cue:** Similarly, as we clean up clutters from the environment, we find that the manipulation accuracy also improves and the error rates decrease from 25% to ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (III. EXPERIMENTS), p. 1 (Figure/Table caption) |
| Embodiment/environment | The three leading causes of failures are failing to retrieve the right object to navigate to from the semantic memory (9.3%), getting a difficult pose from the manipulation module (8.0%), and robot ... | hardware/simulator version and reset protocol | p. 7 (III. EXPERIMENTS), p. 8 (III. EXPERIMENTS) |
| Dataset/benchmark | The robot hardware or the RealSense camera can occasionally get miscalibrated over time, especially during continuous home operations. | role, split, size and leakage | p. 7 (III. EXPERIMENTS), p. 8 (III. EXPERIMENTS), p. 8 (III. EXPERIMENTS), p. 6 (III. EXPERIMENTS) |
| Metric | Similarly, as we clean up clutters from the environment, we find that the manipulation accuracy also improves and the error rates decrease from 25% to 16% and finally 13%. | definition, denominator, direction and uncertainty | p. 7 (III. EXPERIMENTS), p. 7 (III. EXPERIMENTS), p. 6 (III. EXPERIMENTS) |
| Baseline/ablation | Fig. 5: Ablation experiment using different semantic memory and grasping modules, with the bars showing average performance and the error bars showing standard deviation over the environments. vocabulary navigation and grasping modules. ... | fair input/data/compute/action matching | p. 7 (Figure/Table caption), p. 6 (III. EXPERIMENTS), p. 7 (III. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 7 / III. EXPERIMENTS - extractive body cue:** Grasping module limitations: One failure mode of our manipulation module comes from executing grasps from a pre-trained manipulation model's output based on a single RGB-D ...
- **p. 8 / III. EXPERIMENTS - extractive body cue:** Robot hardware limitations: While our robot of choice, a Hello Robot: Stretch, is able to pick-and-drop a variety of objects, certain hardware limitations also dictate ...
- **p. 6 / III. EXPERIMENTS - extractive body cue:** 4) What are the failure modes of such a system and its individual components in real home environments?
- **p. 6 / III. EXPERIMENTS - extractive body cue:** As a result, each success and failure of the robot tells us something interesting about applying open-knowledge models in robotics, which we analyze over the ...
- **p. 7 / III. EXPERIMENTS - extractive body cue:** However, at a closer look, we notice a long tail of failure causes presented in Figure 4.
- **p. 8 / IV. RELATED WORKS - extractive body cue:** 8: Samples of failures of our manipulation module.
- **p. 16 / Figure/Table caption - extractive body cue:** Fig. 10: Sample objects on our home experiments, sampled from each home environment, which OK-Robot failed to pick up successfully.

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 mobile_manipulation 문제를 이해하기 위해 읽는다. 본문은 We also find that using heuristics to counteract the robot's physical limitations can lead to a better success rate in the real world (see Section II-D.) • Several challenges still remain: While, ...를 문제로 두고, We present OK-Robot, an Open Knowledge Robot that integrates state-of-the-art VLMs with powerful robotics primitives for navigation and grasping to enable pick-and-drop.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (II. TECHNICAL COMPONENTS AND METHOD), p. 3 (II. TECHNICAL COMPONENTS AND METHOD), p. 4 (II. TECHNICAL COMPONENTS AND METHOD), p. 4 (II. TECHNICAL COMPONENTS AND METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
