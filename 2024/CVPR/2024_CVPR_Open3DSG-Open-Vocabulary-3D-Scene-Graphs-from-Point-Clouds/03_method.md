# Method - Open3DSG: Open-Vocabulary 3D Scene Graphs from Point Clouds with Queryable Objects and Open-Set Relationships

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Koch_Open3DSG_Open-Vocabulary_3D_Scene_Graphs_from_Point_Clouds_with_Queryable_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Koch_Open3DSG_Open-Vocabulary_3D_Scene_Graphs_from_Point_Clouds_with_Queryable_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (3. Method), p. 3 (3. Method)): We first construct an initial graph representation (Sec.

## Method Body Digest

- **p. 3 / 3. Method - extractive body cue:** We first construct an initial graph representation (Sec.
- **p. 3 / 3. Method - extractive body cue:** These features are then aligned to the ones extracted via the 3D GNN (Sec.
- **p. 3 / 3. Method - extractive body cue:** 3.1), and in parallel, we extract vision-language features from aligned 2D images (Sec.
- **p. 3 / 3. Method - extractive body cue:** The overall goal of our approach is to distill the knowledge of 2D vision-language models into a 3D graph neural network (GNN) to predict open-vocabulary ...
- **p. 1 / 1. Introduction - extractive body cue:** Given their complexity and high-level abstraction, 3D How are TV and Wall related?
- **p. 1 / 1. Introduction - extractive body cue:** The state-of-the-art (SOTA) methods for 3D scene graph prediction are limited to a fixed set of object and relationship labels provided by small-scale datasets.
- **p. 2 / 1. Introduction - extractive body cue:** Thus effectively proposing the first open-vocabulary scene graph prediction approach from 3D point cloud data. • Our proposed approach shows promising results on the closed-set ...
- **p. 2 / 1. Introduction - extractive body cue:** We highlight the following three contributions: • We are the first to present a method to create an interactive graph representation of a scene from ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** We highlight the following three contributions: • We are the first to present a method to create an interactive graph representation of a scene from ...
- **p. 1 / 1. Introduction - extractive body cue:** We present Open3DSG the first approach for learning to predict open-vocabulary 3D scene graphs from 3D point clouds.
- **p. 1 / 1. Introduction - extractive body cue:** The advantage of our method is that it can be queried and prompted for any instance in the scene, such as the TV and Wall, ...

## Source Evidence Cues

- **p. 3 / 3. Method - extractive body cue:** We first construct an initial graph representation (Sec.
- **p. 3 / 3. Method - extractive body cue:** These features are then aligned to the ones extracted via the 3D GNN (Sec.
- **Detected method headings:** 3. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | We first construct an initial graph representation (Sec. | p. 3 (3. Method), p. 3 (3. Method) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | These features are then aligned to the ones extracted via the 3D GNN (Sec. | p. 3 (3. Method) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | We first construct an initial graph representation (Sec. | p. 3 (3. Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- objective/update cue 없음 - inspect equations and algorithm boxes
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | parallel, extract, vision-language, features, aligned, images, Sec, overall, goal, distill, knowledge, models, graph, neural | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | parallel, extract, vision-language, features, aligned, images, Sec, overall, goal, distill | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | highlight, following, three, contributions, first, present, create, interactive, graph, representation | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | not recovered | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3. Method - extractive body cue:** 3.1), and in parallel, we extract vision-language features from aligned 2D images (Sec.
- **p. 3 / 3. Method - extractive body cue:** The overall goal of our approach is to distill the knowledge of 2D vision-language models into a 3D graph neural network (GNN) to predict open-vocabulary ...
- **p. 1 / 1. Introduction - extractive body cue:** Given their complexity and high-level abstraction, 3D How are TV and Wall related?
- **p. 1 / 1. Introduction - extractive body cue:** The state-of-the-art (SOTA) methods for 3D scene graph prediction are limited to a fixed set of object and relationship labels provided by small-scale datasets.
- **p. 2 / 1. Introduction - extractive body cue:** Thus effectively proposing the first open-vocabulary scene graph prediction approach from 3D point cloud data. • Our proposed approach shows promising results on the closed-set ...
- **p. 2 / 1. Introduction - extractive body cue:** We highlight the following three contributions: • We are the first to present a method to create an interactive graph representation of a scene from ...
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | At inference time, we perform a two-step prediction for objects and relationships. | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | The first step for aligning our 3D GNN with the 2D vision-language models is to extract 2D fea14185 | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 3. Method - extractive body cue:** At inference time, we perform a two-step prediction for objects and relationships.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** first, construct, initial, graph, representation, Sec, features, then, aligned, ones, extracted, GNN, parallel, extract, vision-language, images, overall, goal, distill, knowledge.
- **Relevant PDF headings:** 3. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | However, since 3DSSG is the only dataset to provide ground truth scene graph labels, we evaluate our distilled model quantitatively on it. | p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup) |
| Global / local decision | We outperform all our supervised baselines on object, predicate and relationship prediction. | p. 7 (4.2. Closed-set 3D scene graph prediction), p. 6 (4.1. Experimental Setup) |
| Motion execution / recovery | We also evaluate the performance of NegCLIP [52] which is supposed to have improved compositional understanding. | p. 6 (4.1. Experimental Setup), p. 7 (4.2. Closed-set 3D scene graph prediction) |

## Failure and Ablation Link

- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Ablation study. 3D scene graph prediction with different input modalities, object VLM, privileged ground-truth information and supervised fine-tuning. potential and advantages of open-vocabulary ...
- **p. 8 / 4.3. Ablation studies - extractive body cue:** Therefore, given the comparably small vocabulary of predicates, we choose to fine-tune our model on 27 fixed predicate classes with only a few labels per ...
- **p. 8 / 4.5. Limitations - extractive body cue:** While closed-vocabulary evaluations are valuable, they cannot highlight the huge potential of open-vocabulary methods such as ours.
- **p. 8 / 5. Conclusion - extractive body cue:** In future work, we see potential in improving relationship prediction even further to achieve even better and more reliable openvocabulary 3D scene graph predictions that ...
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** However, since we predict relationships in a generative manner, we cannot provide fixed queries for our relationship prediction.
- **p. 7 / 4.2. Closed-set 3D scene graph prediction - extractive body cue:** We demonstrate that a naive CLIP-based approach is ill-suited for relationship prediction, but also a two-step approach similar to our method by combining OpenSeg [11] ...
- **p. 7 / 4.2. Closed-set 3D scene graph prediction - extractive body cue:** This demonstrates the core advantage of our zero-shot open-vocabulary approach that it performs robustly on a wide variety of objects and predicates.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (3. Method), p. 3 (3. Method), objective 본문 anchor 없음, temporal p. 3 (3. Method), p. 3 (3.2. 2D feature extraction), p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 7 (4.2. Closed-set 3D scene graph prediction), p. 7 (4.2. Closed-set 3D scene graph prediction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
