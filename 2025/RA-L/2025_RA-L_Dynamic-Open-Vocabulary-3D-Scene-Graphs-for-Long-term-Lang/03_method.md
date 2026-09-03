# Method - Dynamic Open-Vocabulary 3D Scene Graphs for Long-term Language-Guided Mobile Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2410.11989; PDF retrieval source: https://arxiv.org/pdf/2410.11989. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (III. METHOD), p. 4 (III. METHOD), p. 5 (III. METHOD), p. 5 (III. METHOD), p. 3 (III. METHOD), p. 3 (III. METHOD)): We propose an efficient method that leverages new RGB-D observations to update the volumetric representation accordingly.

## Method Body Digest

- **p. 4 / III. METHOD - extractive body cue:** We propose an efficient method that leverages new RGB-D observations to update the volumetric representation accordingly.
- **p. 4 / III. METHOD - extractive body cue:** Then, we apply an advanced Open-Vocal segmentation model to segment regions in the RGB images, extract semantic feature vectors for each region, and project them ...
- **p. 5 / III. METHOD - extractive body cue:** 2) Mobile control: Once the target location is determined, we use the A* [34] algorithm to generate a collision-free navigation path from the start point ...
- **p. 5 / III. METHOD - extractive body cue:** Each subtask output by GPT consists of an "action_name" and multiple "object_name", which are directly extracted from the description and maintain the same level of ...
- **p. 3 / III. METHOD - extractive body cue:** Open-vocabulary 3D Object Mapping With the RGB-D sequences and camera poses, we proceed to construct an object-centric 3D representation from RGB-D observations It = {I1, ...
- **p. 3 / III. METHOD - extractive body cue:** We then extract the visual features of each object using two mask-based images with CLIP, and fuse them using a weighted sum method, as described ...
- **p. 6 / III. METHOD - extractive body cue:** 1) Pick up: To focus the AnyGrasp model on the target object, we first preprocess the point cloud by cropping it to a region around ...
- **p. 3 / III. METHOD - extractive body cue:** 1) Open-vocabuary 2D Segmentation: To maximize object recognition in the scene, we first apply the image tagging model Recognize-Anything [6] to each frame It, generating ...

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** Our contributions are as follows: • We propose a novel robotic framework that integrates dynamic open-vocabulary 3D scene graphs with languageguided task planning, enabling accurate ...
- **p. 4 / III. METHOD - extractive body cue:** We propose an efficient method that leverages new RGB-D observations to update the volumetric representation accordingly.
- **p. 2 / III. METHOD - extractive body cue:** DovSG enables mobile robots to perform long-term tasks in indoor environments by constructing dynamic 3D scene graphs and using large language models for task planning.

## Source Evidence Cues

- **p. 4 / III. METHOD - extractive body cue:** We propose an efficient method that leverages new RGB-D observations to update the volumetric representation accordingly.
- **p. 4 / III. METHOD - extractive body cue:** Then, we apply an advanced Open-Vocal segmentation model to segment regions in the RGB images, extract semantic feature vectors for each region, and project them ...
- **p. 5 / III. METHOD - extractive body cue:** 2) Mobile control: Once the target location is determined, we use the A* [34] algorithm to generate a collision-free navigation path from the start point ...
- **p. 5 / III. METHOD - extractive body cue:** Each subtask output by GPT consists of an "action_name" and multiple "object_name", which are directly extracted from the description and maintain the same level of ...
- **p. 3 / III. METHOD - extractive body cue:** Open-vocabulary 3D Object Mapping With the RGB-D sequences and camera poses, we proceed to construct an object-centric 3D representation from RGB-D observations It = {I1, ...
- **p. 3 / III. METHOD - extractive body cue:** We then extract the visual features of each object using two mask-based images with CLIP, and fuse them using a weighted sum method, as described ...
- **p. 6 / III. METHOD - extractive body cue:** 1) Pick up: To focus the AnyGrasp model on the target object, we first preprocess the point cloud by cropping it to a region around ...
- **Detected method headings:** III. METHOD (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Scene / interaction state | base·arm·object 관계를 표현한다 | egocentric RGB-D, language goal, proprioception | map, object, reachability, contact 또는 affordance state를 구성 | base-arm interaction state | We propose an efficient method that leverages new RGB-D observations to update the volumetric representation accordingly. | p. 4 (III. METHOD), p. 4 (III. METHOD) |
| Base-arm task decision | 접근·도킹·grasp·manipulation sequence를 결정한다 | interaction state와 task instruction | keypoint, option, trajectory, grasp 또는 joint planning을 수행 | base path plus arm/gripper plan | Then, we apply an advanced Open-Vocal segmentation model to segment regions in the RGB images, extract semantic feature vectors for each region, ... | p. 4 (III. METHOD), p. 5 (III. METHOD) |
| Execution / correction | 부분 실행 후 observation으로 계획을 수정한다 | current pose, visual/force feedback | tracking, regrasp, docking correction, recovery 또는 replan을 수행 | next mobile-manipulation action | 2) Mobile control: Once the target location is determined, we use the A* [34] algorithm to generate a collision-free navigation path from ... | p. 5 (III. METHOD), p. 5 (III. METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / III. METHOD - extractive body cue:** 1) Open-vocabuary 2D Segmentation: To maximize object recognition in the scene, we first apply the image tagging model Recognize-Anything [6] to each frame It, generating ...
- **p. 4 / III. METHOD - extractive body cue:** This refinement step minimizes both geometric and photometric discrepancies between the new observations and the existing map, yielding a precise transformation T icp k that ...
- **p. 6 / III. METHOD - extractive body cue:** After generating candidate grasps, we apply cost-based filtering to select the best option.
- **p. 6 / III. METHOD - extractive body cue:** Furthermore, we filtered the grasps based on translational and rotational costs, with the red grasps indicating the highest confidence.
- **p. 2 / III. METHOD - extractive body cue:** From these, a 3D scene graph is generated, capturing object relationships and continuously updated when the environment changes.
- **p. 4 / III. METHOD - extractive body cue:** The refined poses Ipose k are then updated using the transformation Ipose k ←T icpIpose k .
- **Formal bridge:** base-arm-object state and language/task goal -> base plus arm/gripper action -> long-horizon task utility under reachability/contact constraints -> task completion and recovery.
- **Equation/algorithm anchors:** p. 2 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD), p. 5 (III. METHOD), p. 5 (III. METHOD), p. 6 (III. METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | YAN, DYNAMIC, OPEN-VOCABULARY, SCENE, GRAPHS, LONG-TERM, LANGUAGE-GUIDED, MOBILE, MANIPULATION, color, information, process, observation, follows | egocentric RGB-D, language/task goal, base-arm proprioception | body cue; exact tensor/frame verify |
| State/latent | YAN, DYNAMIC, OPEN-VOCABULARY, SCENE, GRAPHS, LONG-TERM, LANGUAGE-GUIDED, MOBILE, MANIPULATION, color | map/object/contact state와 base-arm coordination decision | body cue; notation verify |
| Action/output | contributions, follows, novel, robotic, framework, integrates, dynamic, open-vocabulary, scene, graphs | base motion plus arm/gripper action | body cue; unit/decoder verify |
| Objective/constraint | Open-vocabuary, Segmentation, maximize, object, recognition, scene, first, apply, image, tagging | long-horizon task utility under reachability/contact constraints | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / III. METHOD - extractive body cue:** YAN et al.: DYNAMIC OPEN-VOCABULARY 3D SCENE GRAPHS FOR LONG-TERM LANGUAGE-GUIDED MOBILE MANIPULATION 5 and color information, we process each new observation Ik as follows: ...
- **p. 4 / III. METHOD - extractive body cue:** After the robot collects new RGB-D observations Ik for k ∈{t + 1, ..., t + n}, where each observation Ik = ⟨Irgb k , ...
- **p. 5 / III. METHOD - extractive body cue:** (12) 3) Update low-level memory: After the above step, the local scene in the historical low-level memory will be updated to the latest state based ...
- **p. 3 / III. METHOD - extractive body cue:** Open-vocabulary 3D Object Mapping With the RGB-D sequences and camera poses, we proceed to construct an object-centric 3D representation from RGB-D observations It = {I1, ...
- **p. 4 / III. METHOD - extractive body cue:** FEBRUARY, 2025 3D objects 3D Scene Graphs Color Mapping Based on CLIP Similarity Query: tangerine transform pose Pre-Frame detected object features and point clouds New ...
- **p. 6 / III. METHOD - extractive body cue:** In the first row, we cropped the point cloud input into anyGrasp within a certain range around the target object, allowing anyGrasp to focus more ...
- **p. 6 / III. METHOD - extractive body cue:** This heuristic strategy is only activated when AnyGrasp can't provide a suitable grasp, ensuring optimal interaction with the object's geometry 2) Place: We first obtain ...
- **Normalized interface:** observation=egocentric RGB-D, language/task goal, base-arm proprioception; state=map/object/contact state와 base-arm coordination decision; output/action=base motion plus arm/gripper action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | paper-specific horizon; exact value was not selected from the PDF body. | 2) Remove obsolete indices: This step is to identify and remove obsolete voxels from the memory map. | episode/sequence/action-chunk boundary |
| Rate / latency | paper-specific inference/control rate; exact value was not selected from the PDF body. | This refinement step minimizes both geometric and photometric discrepancies between the new observations and the existing map, yielding a precise transformation T ... | Hz/fps, inference time and control rate |
| Memory | paper-specific history/state memory; exact value was not selected from the PDF body. | 2) Remove obsolete indices: This step is to identify and remove obsolete voxels from the memory map. | window and reset |
| Compute | representation, optimization/inference steps와 hardware가 latency를 결정한다; exact profile was not selected from the PDF body. | Overall, for each method, each level of modification was tested through 20 long-term tasks per room across 4 rooms, resulting in a ... | hardware, batch and throughput |

## Training vs Inference

- training/inference separation PDF body cue not selected; no claim inferred

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** efficient, leverages, RGB-D, observations, update, volumetric, representation, accordingly, Then, apply, advanced, Open-Vocal, segmentation, model, segment, regions, RGB, images, extract, semantic.
- **Relevant PDF headings:** III. METHOD (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Scene / interaction state | 2) Environment and Task Setups: To verify our method's ability to enable robots to perform long-term tasks in dynamic environments, we designed ... | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Base-arm task decision | In contrast, DovSG, supported by precise relocalization, can accurately identify the voxel index where changes have occurred in the scene, significantly outperforming ... | p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |
| Execution / correction | This makes it highly likely for the robot to navigate near the target, resulting in a significantly higher success rate compared to ... | p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 6 / IV. EXPERIMENTS - extractive body cue:** (2) How effectively does this facilitate the completion of consecutive tasks without manual resets?
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** In the "Positional Shift" scenario, the residual effect of CLIP features can occasionally mislead the robot into navigating toward the object's historical location, ultimately causing ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** This detailed evaluation provides a comprehensive analysis of the effectiveness of our method across different components of task execution.
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4. Two proposed grasp strategies in DovSG. In the first row, we cropped the point cloud input into anyGrasp within a certain range around ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. Overview of Our DovSG System. DovSG is a mobile robotic system designed to perform long-term tasks in real-world environments. It can detect changes ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1. To address the challenge of scene perception, our per- ception module integrates advanced tools such as Recognize- Anything [6], Grounding DINO [7], Segment ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** In the "Positional Shift" scenario, the residual effect of CLIP features can occasionally mislead the robot into navigating toward the object's historical location, ultimately causing ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (III. METHOD), p. 4 (III. METHOD), p. 5 (III. METHOD), p. 5 (III. METHOD), p. 3 (III. METHOD), p. 3 (III. METHOD), objective p. 3 (III. METHOD), p. 4 (III. METHOD), p. 6 (III. METHOD), p. 6 (III. METHOD), p. 2 (III. METHOD), p. 4 (III. METHOD), temporal p. 4 (III. METHOD), p. 4 (III. METHOD), p. 5 (III. METHOD), p. 2 (I. INTRODUCTION), p. 2 (II. RELATED WORKS), p. 3 (III. METHOD).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Open-vocabulary 3D Object Mapping With the RGB-D sequences and camera poses, we proceed to construct an object-centric 3D representation from RGB-D observations It = {I1, I2, . . . , ... (p. 3, III. METHOD).
- **Objective/update evidence:** From these, a 3D scene graph is generated, capturing object relationships and continuously updated when the environment changes. (p. 2, III. METHOD).
- **Temporal/runtime evidence:** 2) Remove obsolete indices: This step is to identify and remove obsolete voxels from the memory map. (p. 4, III. METHOD).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
