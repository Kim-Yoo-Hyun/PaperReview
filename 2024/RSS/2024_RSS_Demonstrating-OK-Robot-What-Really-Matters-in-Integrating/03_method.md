# Method - Demonstrating OK-Robot: What Really Matters in Integrating Open-Knowledge Models for Robotics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p091.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p091.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (II. TECHNICAL COMPONENTS AND METHOD), p. 3 (II. TECHNICAL COMPONENTS AND METHOD), p. 4 (II. TECHNICAL COMPONENTS AND METHOD), p. 4 (II. TECHNICAL COMPONENTS AND METHOD), p. 5 (II. TECHNICAL COMPONENTS AND METHOD), p. 5 (II. TECHNICAL COMPONENTS AND METHOD)): Open-home, open-vocabulary object navigation The first component of our method is an open-home, openvocabulary object navigation model that we use to map a home and subsequently navigate to any object ...

## Method Body Digest

- **p. 3 / II. TECHNICAL COMPONENTS AND METHOD - extractive body cue:** Open-home, open-vocabulary object navigation The first component of our method is an open-home, openvocabulary object navigation model that we use to map a home and ...
- **p. 3 / II. TECHNICAL COMPONENTS AND METHOD - extractive body cue:** Navigating to objects in the real world: Once our navigation model gives us a 3D location coordinate in the real world, we use that as ...
- **p. 4 / II. TECHNICAL COMPONENTS AND METHOD - extractive body cue:** We use the VoxelMap [25] for localizing objects with natural language queries, and use an A* algorithm similar to USANet [26] for path planning.
- **p. 4 / II. TECHNICAL COMPONENTS AND METHOD - extractive body cue:** Grasp perception: Once the robot reaches the object location using the navigation method outlined in Section II-A, we use a pre-trained grasping model, AnyGrasp [19], ...
- **p. 5 / II. TECHNICAL COMPONENTS AND METHOD - extractive body cue:** Since we do not implement error detection or correction, our state machine model is a simple linear chain of steps leading from navigating to object, ...
- **p. 5 / II. TECHNICAL COMPONENTS AND METHOD - extractive body cue:** We query our navigation module to filter out all the navigation failures; i.e. objects that our semantic memory module could not locate properly.
- **p. 3 / II. TECHNICAL COMPONENTS AND METHOD - extractive body cue:** Then, we find the voxel where the dot product between the encoded embedding and the voxel's associated embedding is maximized.
- **p. 3 / II. TECHNICAL COMPONENTS AND METHOD - extractive body cue:** The ideal navigation point -→x ∗is the point in space that minimizes s(-→x ), and the ideal direction is given by the vector from -→ ...

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** We present OK-Robot, an Open Knowledge Robot that integrates state-of-the-art VLMs with powerful robotics primitives for navigation and grasping to enable pick-and-drop.
- **p. 3 / II. TECHNICAL COMPONENTS AND METHOD - extractive body cue:** The system we introduce is a combination of three primary subsystems combined on a Hello Robot: Stretch.
- **p. 3 / II. TECHNICAL COMPONENTS AND METHOD - extractive body cue:** This manual scan simply consists of taking a video of the home using the Record3D app on the iPhone, which results in a sequence of ...

## Source Evidence Cues

- **p. 3 / II. TECHNICAL COMPONENTS AND METHOD - extractive body cue:** Open-home, open-vocabulary object navigation The first component of our method is an open-home, openvocabulary object navigation model that we use to map a home and ...
- **p. 3 / II. TECHNICAL COMPONENTS AND METHOD - extractive body cue:** Navigating to objects in the real world: Once our navigation model gives us a 3D location coordinate in the real world, we use that as ...
- **p. 4 / II. TECHNICAL COMPONENTS AND METHOD - extractive body cue:** We use the VoxelMap [25] for localizing objects with natural language queries, and use an A* algorithm similar to USANet [26] for path planning.
- **p. 4 / II. TECHNICAL COMPONENTS AND METHOD - extractive body cue:** Grasp perception: Once the robot reaches the object location using the navigation method outlined in Section II-A, we use a pre-trained grasping model, AnyGrasp [19], ...
- **p. 5 / II. TECHNICAL COMPONENTS AND METHOD - extractive body cue:** Since we do not implement error detection or correction, our state machine model is a simple linear chain of steps leading from navigating to object, ...
- **p. 5 / II. TECHNICAL COMPONENTS AND METHOD - extractive body cue:** We query our navigation module to filter out all the navigation failures; i.e. objects that our semantic memory module could not locate properly.
- **Detected method headings:** II. TECHNICAL COMPONENTS AND METHOD (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Scene / interaction state | base·arm·object 관계를 표현한다 | egocentric RGB-D, language goal, proprioception | map, object, reachability, contact 또는 affordance state를 구성 | base-arm interaction state | Open-home, open-vocabulary object navigation The first component of our method is an open-home, openvocabulary object navigation model that we use to map ... | p. 3 (II. TECHNICAL COMPONENTS AND METHOD), p. 3 (II. TECHNICAL COMPONENTS AND METHOD) |
| Base-arm task decision | 접근·도킹·grasp·manipulation sequence를 결정한다 | interaction state와 task instruction | keypoint, option, trajectory, grasp 또는 joint planning을 수행 | base path plus arm/gripper plan | Navigating to objects in the real world: Once our navigation model gives us a 3D location coordinate in the real world, we ... | p. 3 (II. TECHNICAL COMPONENTS AND METHOD), p. 4 (II. TECHNICAL COMPONENTS AND METHOD) |
| Execution / correction | 부분 실행 후 observation으로 계획을 수정한다 | current pose, visual/force feedback | tracking, regrasp, docking correction, recovery 또는 replan을 수행 | next mobile-manipulation action | We use the VoxelMap [25] for localizing objects with natural language queries, and use an A* algorithm similar to USANet [26] for ... | p. 4 (II. TECHNICAL COMPONENTS AND METHOD), p. 4 (II. TECHNICAL COMPONENTS AND METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / II. TECHNICAL COMPONENTS AND METHOD - extractive body cue:** Then, we find the voxel where the dot product between the encoded embedding and the voxel's associated embedding is maximized.
- **p. 3 / II. TECHNICAL COMPONENTS AND METHOD - extractive body cue:** The ideal navigation point -→x ∗is the point in space that minimizes s(-→x ), and the ideal direction is given by the vector from -→ ...
- **p. 4 / II. TECHNICAL COMPONENTS AND METHOD - extractive body cue:** During A* search, we use the s3 as a heuristic function on the node costs to navigate further away from any obstacles, which makes our ...
- **p. 4 / II. TECHNICAL COMPONENTS AND METHOD - extractive body cue:** If -→p is the grasp point and -→a is the approach vector given by the grasping model, our robot gripper follows the following trajectory: ⟨-→p ...
- **Formal bridge:** base-arm-object state and language/task goal -> base plus arm/gripper action -> long-horizon task utility under reachability/contact constraints -> task completion and recovery.
- **Equation/algorithm anchors:** p. 3 (II. TECHNICAL COMPONENTS AND METHOD), p. 3 (II. TECHNICAL COMPONENTS AND METHOD), p. 5 (II. TECHNICAL COMPONENTS AND METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Overall, through, experiments, make, following, observations, Pre-trained, VLMs, highly, effective, openvocabulary, navigation, Current, open-vocabulary | egocentric RGB-D, language/task goal, base-arm proprioception | body cue; exact tensor/frame verify |
| State/latent | Overall, through, experiments, make, following, observations, Pre-trained, VLMs, highly, effective | map/object/contact state와 base-arm coordination decision | body cue; notation verify |
| Action/output | present, OK-Robot, Open, Knowledge, Robot, integrates, state-of-the-art, VLMs, powerful, robotics | base motion plus arm/gripper action | body cue; unit/decoder verify |
| Objective/constraint | Then, find, voxel, where, product, between, encoded, embedding, associated, maximized | long-horizon task utility under reachability/contact constraints | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / I. INTRODUCTION - extractive body cue:** Overall, through our experiments, we make the following observations: • Pre-trained VLMs are highly effective for openvocabulary navigation: Current open-vocabulary visionlanguage models such as CLIP ...
- **p. 5 / II. TECHNICAL COMPONENTS AND METHOD - extractive body cue:** Since we do not implement error detection or correction, our state machine model is a simple linear chain of steps leading from navigating to object, ...
- **p. 3 / II. TECHNICAL COMPONENTS AND METHOD - extractive body cue:** Once collected, the RGB-D images, along with the camera pose and positions, are exported to our library for map-building.
- **p. 3 / II. TECHNICAL COMPONENTS AND METHOD - extractive body cue:** VoxelMap is built by back-projecting the object masks in real-world coordinates using the depth image and the pose collected by the camera.
- **p. 4 / II. TECHNICAL COMPONENTS AND METHOD - extractive body cue:** To navigate to this target point safely from any other point in space, we follow a similar approach to [26, 32] by building an obstacle ...
- **p. 5 / II. TECHNICAL COMPONENTS AND METHOD - extractive body cue:** First, we segment the point cloud P captured by the robot's head camera using LangSam [24] similar to Section II-B using the drop language query.
- **p. 4 / II. TECHNICAL COMPONENTS AND METHOD - extractive body cue:** We backproject and convert the depth image to a pointcloud and pass this information to the grasp generation model.
- **Normalized interface:** observation=egocentric RGB-D, language/task goal, base-arm proprioception; state=map/object/contact state와 base-arm coordination decision; output/action=base motion plus arm/gripper action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | paper-specific horizon; exact value was not selected from the PDF body. | We apply the detector on every frame, and extract each of the object bounding box, CLIPembedding, detector confidence, and pass these information ... | episode/sequence/action-chunk boundary |
| Rate / latency | paper-specific inference/control rate; exact value was not selected from the PDF body. | This VoxelMap builds the base of our object memory module. | Hz/fps, inference time and control rate |
| Memory | paper-specific history/state memory; exact value was not selected from the PDF body. | We apply the detector on every frame, and extract each of the object bounding box, CLIPembedding, detector confidence, and pass these information ... | window and reset |
| Compute | representation, optimization/inference steps와 hardware가 latency를 결정한다; exact profile was not selected from the PDF body. | not stated or recoverable in the selected PDF body | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / II. TECHNICAL COMPONENTS AND METHOD - extractive body cue:** Grasp perception: Once the robot reaches the object location using the navigation method outlined in Section II-A, we use a pre-trained grasping model, AnyGrasp [19], ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Open-home, open-vocabulary, object, navigation, first, component, openvocabulary, model, home, subsequently, navigate, interest, designated, natural, language, query, Navigating, objects, real, world.
- **Relevant PDF headings:** II. TECHNICAL COMPONENTS AND METHOD (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Scene / interaction state | The three leading causes of failures are failing to retrieve the right object to navigate to from the semantic memory (9.3%), getting ... | p. 7 (III. EXPERIMENTS), p. 8 (III. EXPERIMENTS) |
| Base-arm task decision | Fig. 5: Ablation experiment using different semantic memory and grasping modules, with the bars showing average performance and the error bars showing ... | p. 7 (Figure/Table caption), p. 6 (III. EXPERIMENTS) |
| Execution / correction | Results of home experiments Over the 10 home environment, OK-Robot achieved a 58.5% success rates in completing full pick-and-drops. | p. 6 (III. EXPERIMENTS), p. 1 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 6 / III. EXPERIMENTS - extractive body cue:** Ablations over system components Apart from the navigation and manipulation strategies used in OK-Robot, we also evaluated a number of alternative open
- **p. 7 / III. EXPERIMENTS - extractive body cue:** As we can see from this breakdown, as we clean up the environment and remove the ambiguous objects, the navigation accuracy goes up, and the ...
- **p. 7 / III. EXPERIMENTS - extractive body cue:** 5: Ablation experiment using different semantic memory and grasping modules, with the bars showing average performance and the error bars showing standard deviation over the ...
- **p. 6 / III. EXPERIMENTS - extractive body cue:** 4) What are the failure modes of such a system and its individual components in real home environments?
- **p. 8 / III. EXPERIMENTS - extractive body cue:** Since the memory module depends on pretrained large vision language model, its performance shows susceptibility to particular "incantations" similar to current LLMs.
- **p. 7 / III. EXPERIMENTS - extractive body cue:** Grasping module limitations: One failure mode of our manipulation module comes from executing grasps from a pre-trained manipulation model's output based on a single RGB-D ...
- **p. 8 / III. EXPERIMENTS - extractive body cue:** Robot hardware limitations: While our robot of choice, a Hello Robot: Stretch, is able to pick-and-drop a variety of objects, certain hardware limitations also dictate ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (II. TECHNICAL COMPONENTS AND METHOD), p. 3 (II. TECHNICAL COMPONENTS AND METHOD), p. 4 (II. TECHNICAL COMPONENTS AND METHOD), p. 4 (II. TECHNICAL COMPONENTS AND METHOD), p. 5 (II. TECHNICAL COMPONENTS AND METHOD), p. 5 (II. TECHNICAL COMPONENTS AND METHOD), objective p. 3 (II. TECHNICAL COMPONENTS AND METHOD), p. 3 (II. TECHNICAL COMPONENTS AND METHOD), p. 4 (II. TECHNICAL COMPONENTS AND METHOD), p. 4 (II. TECHNICAL COMPONENTS AND METHOD), temporal p. 3 (II. TECHNICAL COMPONENTS AND METHOD), p. 3 (II. TECHNICAL COMPONENTS AND METHOD), p. 4 (II. TECHNICAL COMPONENTS AND METHOD), p. 4 (II. TECHNICAL COMPONENTS AND METHOD), p. 5 (II. TECHNICAL COMPONENTS AND METHOD), p. 5 (II. TECHNICAL COMPONENTS AND METHOD).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (27 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Then, we find the voxel where the dot product between the encoded embedding and the voxel's associated embedding is maximized. (p. 3, II. TECHNICAL COMPONENTS AND METHOD).
- **Objective/update evidence:** Thus, our navigation method has to balance the following objectives: 1) The robot needs to be close enough to the object to manipulate it, 2) The robot needs some space ... (p. 3, II. TECHNICAL COMPONENTS AND METHOD).
- **Temporal/runtime evidence:** We apply the detector on every frame, and extract each of the object bounding box, CLIPembedding, detector confidence, and pass these information onto the object memory module. (p. 3, II. TECHNICAL COMPONENTS AND METHOD).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
