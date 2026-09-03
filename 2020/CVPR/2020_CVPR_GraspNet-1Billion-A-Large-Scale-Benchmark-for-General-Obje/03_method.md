# Method - GraspNet-1Billion: A Large-Scale Benchmark for General Object Grasping

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1912.13470; PDF retrieval source: https://arxiv.org/pdf/1912.13470. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 3 (3.2. Data Collection), p. 4 (2 Cams), p. 2 (1. Introduction), p. 2 (3. GraspNet Dataset)): Firstly, the grasp pose has different representations including rectangle [23] and 6D pose [24] representation and are evaluated with different metrics [11, 10, 24] correspondingly.

## Method Body Digest

- **p. 1 / 1. Introduction - extractive body cue:** Firstly, the grasp pose has different representations including rectangle [23] and 6D pose [24] representation and are evaluated with different metrics [11, 10, 24] correspondingly.
- **p. 1 / 1. Introduction - extractive body cue:** Thanks to our automatic annotation process, we built the first large-scale in-the-wild grasp pose dataset that can serve as a base for training and evaluating ...
- **p. 3 / 3.2. Data Collection - extractive body cue:** The robot arm then moves along a fixed trajectory that covers 256 distinct viewpoints on a quarter sphere.
- **p. 4 / 2 Cams - extractive body cue:** The force-closure metric [20, 24] has been proved effective in grasp evaluation: given a grasp pose, the associated object and a friction coefficient µ, force-closure ...
- **p. 2 / 1. Introduction - extractive body cue:** For all 88 objects in our dataset, we provide accurate 3D mesh models.
- **p. 2 / 3. GraspNet Dataset - extractive body cue:** We next describe the main features of our dataset and how we build it.
- **p. 3 / 3.3. Data Annotation - extractive body cue:** To achieve that, high quality mesh models are downsampled such that the sampled points (called grasp points) are uniformly distributed in voxel space.
- **p. 1 / 1. Introduction - extractive body cue:** The difference in evaluation metrics makes it difficult to compare these methods directly in an unified manner, while evaluating with real robots would dramatically increase ...

## Design Rationale

- **p. 1 / 1. Introduction - extractive body cue:** Our methodology for building the dataset.
- **p. 1 / 1. Introduction - extractive body cue:** Specifically, inspired by previous literature [24], we propose a two-step pipeline to generate tremendous grasp poses for a scene.
- **p. 2 / 3.1. Overview - extractive body cue:** To overcome these issues, we propose a large-scale dataset in clustered scenario with dense and rich annotations for grasp pose prediction named GraspNet.

## Source Evidence Cues

- **p. 1 / 1. Introduction - extractive body cue:** Firstly, the grasp pose has different representations including rectangle [23] and 6D pose [24] representation and are evaluated with different metrics [11, 10, 24] correspondingly.
- **p. 1 / 1. Introduction - extractive body cue:** Thanks to our automatic annotation process, we built the first large-scale in-the-wild grasp pose dataset that can serve as a base for training and evaluating ...
- **p. 3 / 3.2. Data Collection - extractive body cue:** The robot arm then moves along a fixed trajectory that covers 256 distinct viewpoints on a quarter sphere.
- **p. 4 / 2 Cams - extractive body cue:** The force-closure metric [20, 24] has been proved effective in grasp evaluation: given a grasp pose, the associated object and a friction coefficient µ, force-closure ...
- **p. 2 / 1. Introduction - extractive body cue:** For all 88 objects in our dataset, we provide accurate 3D mesh models.
- **p. 2 / 3. GraspNet Dataset - extractive body cue:** We next describe the main features of our dataset and how we build it.
- **p. 3 / 3.3. Data Annotation - extractive body cue:** To achieve that, high quality mesh models are downsampled such that the sampled points (called grasp points) are uniformly distributed in voxel space.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | Firstly, the grasp pose has different representations including rectangle [23] and 6D pose [24] representation and are evaluated with different metrics [11, ... | p. 1 (1. Introduction), p. 1 (1. Introduction) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | Thanks to our automatic annotation process, we built the first large-scale in-the-wild grasp pose dataset that can serve as a base for ... | p. 1 (1. Introduction), p. 3 (3.2. Data Collection) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | The robot arm then moves along a fixed trajectory that covers 256 distinct viewpoints on a quarter sphere. | p. 3 (3.2. Data Collection), p. 4 (2 Cams) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / 1. Introduction - extractive body cue:** The difference in evaluation metrics makes it difficult to compare these methods directly in an unified manner, while evaluating with real robots would dramatically increase ...
- **p. 1 / 1. Introduction - extractive body cue:** We circumvent this issue by exploring a new direction, that is, collecting data from the real world and annotating them by analytic computation in simulation, ...
- **p. 4 / 2 Cams - extractive body cue:** The grasp with lower friction coefficient µ has more probability of success.
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | grasping, detect, grasp, pose, given, visual, inputs, image, point, cloud, drawn, many, attentions, computer | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | grasping, detect, grasp, pose, given, visual, inputs, image, point, cloud | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | methodology, building, dataset, Specifically, inspired, previous, literature, two-step, pipeline, generate | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | difference, evaluation, metrics, makes, difficult, compare, methods, directly, unified, manner | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1. Introduction - extractive body cue:** The key of grasping is to detect the grasp pose given visual inputs (image or point cloud) and has drawn many attentions in computer vision ...
- **p. 4 / 2 Cams - extractive body cue:** The force-closure metric [20, 24] has been proved effective in grasp evaluation: given a grasp pose, the associated object and a friction coefficient µ, force-closure ...
- **p. 3 / 3.2. Data Collection - extractive body cue:** View 1 View 2 Kinect4A RealSense 6D-Pose 6DoF Grasp Poses Rectangle-based Grasp Poses Instance Masks Unified Evaluation System Object Models …… Rich Data Dense Annotations ...
- **p. 2 / 3.1. Overview - extractive body cue:** For each image, we densely annotate 6-DoF grasp poses by analytic computation of force closure [20].
- **p. 2 / 3.1. Overview - extractive body cue:** Each frame is also associated with a camera pose, thus multi-view point cloud can be easily fused.
- **p. 1 / Abstract - extractive body cue:** Our dataset contains 87,040 RGBD image with over 370 million grasp poses.
- **p. 3 / 3.2. Data Collection - extractive body cue:** A synchronized image pair from both RGB-D cameras as well as their camera poses will be saved.
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | In this work, we adopt an online evaluation algorithm to evaluate the grasp accuracy. | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | Summary of real world success rate of grasping given different grasp score. grasp poses to the camera frame using objects' 6D poses, ... | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | not stated or recoverable in the selected PDF body | hardware, batch and throughput |

## Training vs Inference

- **p. 1 / 1. Introduction - extractive body cue:** Thanks to our automatic annotation process, we built the first large-scale in-the-wild grasp pose dataset that can serve as a base for training and evaluating ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Firstly, grasp, pose, different, representations, including, rectangle, representation, evaluated, metrics, correspondingly, Thanks, automatic, annotation, process, built, first, large-scale, in-the-wild, dataset.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | Dataset Split For our 170 scenes, we use 100 for training and 70 for testing. | p. 4 (3.4. Evaluation), p. 4 (3.4. Evaluation) |
| Baseline harness | Fig 2 illustrates the key components of our dataset. | p. 2 (3.1. Overview), p. 3 (Figure/Table caption) |
| Metric / failure reporting | Summary of real world success rate of grasping given different grasp score. grasp poses to the camera frame using objects' 6D poses, ... | p. 5 (4.1. Ground-Truth Evaluation), p. 4 (3.4. Evaluation) |

## Failure and Ablation Link

- **p. 2 / 3.1. Overview - extractive body cue:** Fig 2 illustrates the key components of our dataset.
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. The key components of our dataset. RGB-D images are taken using both RealSense camera and Kinect camera from different views. The 6D pose ...
- **p. 5 / 3.5. Discussion - extractive body cue:** The previous method that pre-computed ground truth for evaluating grasping, no matter collected by human annotation [11] or simulation [7], cannot cover all feasible solution.
- **p. 5 / 3.5. Discussion - extractive body cue:** Such evaluation method does not assume the representation of the grasp pose, thus is general in practice.
- **p. 3 / 3.3. Data Annotation - extractive body cue:** Collision detection is also conducted to avoid the collision between grasps and background or other object. where Pj i is the 6D pose of object ...
- **p. 3 / 3.3. Data Annotation - extractive body cue:** The 6D poses will then be propagated to the remaining frames by: Pj i = cam-1 i cam0Pj 0, (1) Gripper Depth Sampling Grasp View ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Our methodology for building the dataset. We collect data with real-world sensors and annotate grasp poses for every single object by analytic computation. ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 1 (1. Introduction), p. 1 (1. Introduction), p. 3 (3.2. Data Collection), p. 4 (2 Cams), p. 2 (1. Introduction), p. 2 (3. GraspNet Dataset), objective p. 1 (1. Introduction), p. 1 (1. Introduction), p. 4 (2 Cams), temporal p. 4 (3.4. Evaluation), p. 5 (4.1. Ground-Truth Evaluation), p. 1 (1. Introduction), p. 2 (3.1. Overview), p. 2 (1. Introduction), p. 3 (3.3. Data Annotation).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (7 pages; PyMuPDF text; extraction quality: high; title-token overlap: 0.75). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** The key of grasping is to detect the grasp pose given visual inputs (image or point cloud) and has drawn many attentions in computer vision community [8, 21]. (p. 1, 1. Introduction).
- **Objective/update evidence:** The difference in evaluation metrics makes it difficult to compare these methods directly in an unified manner, while evaluating with real robots would dramatically increase the evaluation cost. (p. 1, 1. Introduction).
- **Temporal/runtime evidence:** Summary of real world success rate of grasping given different grasp score. grasp poses to the camera frame using objects' 6D poses, we paste ArUco code on the objects and ... (p. 5, 4.1. Ground-Truth Evaluation).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
