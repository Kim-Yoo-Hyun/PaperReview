# Evaluation - Manual2Skill: Learning to Read Manuals and Acquire Robotic Skills for Furniture Assembly Using Vision-Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (26 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p150.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p150.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (C. Overall Performance Evaluation), p. 8 (C. Overall Performance Evaluation), p. 16 (B. Pose Estimation Implementation), p. 15 (B. Pose Estimation Implementation), p. 8 (C. Overall Performance Evaluation), p. 9 (C. Overall Performance Evaluation)): We present the results in Table IV, showing that our method outperforms the baseline and achieves a high success rate in real-world assembly tasks.

## Evaluation Body Digest

- **p. 9 / C. Overall Performance Evaluation - extractive body cue:** Failures occur when the RRTConnect algorithm cannot find a feasible trajectory when the planned path results in collisions with the robotic arm or surrounding objects ...
- **p. 8 / C. Overall Performance Evaluation - extractive body cue:** Note that, in this experiment, wwe focus on object-centric motion planning and omit robotic ‘execution in our framework
- **p. 8 / C. Overall Performance Evaluation - extractive body cue:** We source all test furniture models from the IKEA-Manuals dataset [49] Given these manuals along with 3D parts, we generate the preassembly scene images as ...
- **p. 9 / C. Overall Performance Evaluation - extractive body cue:** We present the results in Table IV, showing that our method outperforms the baseline and achieves a high success rate in real-world assembly tasks.
- **p. 17 / B. Pose Estimation Implementation - extractive body cue:** 1) Pose Estimation in the Real World: We utilize FoundationPose [52] to evaluate the 6D pose and point cloud of components in the real-world scene.
- **p. 17 / B. Pose Estimation Implementation - extractive body cue:** During each step of the assembly proces the mesh-along with the RGB and depth images and an object mask-is input into the FoundationPose model, which ...
- **p. 15 / B. Pose Estimation Implementation - extractive body cue:** In contrast, our pose estimation dataset includes per-step data (i.e., subassemblies).
- **p. 15 / B. Pose Estimation Implementation - extractive body cue:** As shown in Table VII, adding per-step data improves assembly prediction accuracy, demonstrating that per-step inference enhances robot assembly performance.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** experiments (p. 2); C. Overall Performance Evaluation (p. 8); A. Per-step Assembly Pose Estimation Dataset (p. 14); B. Pose Estimation Implementation (p. 14).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| C. Overall Performance Evaluation | EMPIRICAL / REAL-ROBOT OR HARDWARE | We present the results in Table IV, showing that our method outperforms the baseline and achieves a high success rate in real-world assembly tasks. | p. 9 (C. Overall Performance Evaluation) |
| C. Overall Performance Evaluation | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our framework achieves a success rate of $8%, demonstrating the effectiveness of our proposed framework. | p. 8 (C. Overall Performance Evaluation) |
| B. Pose Estimation Implementation | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Table X (Ours (w/o Segmentation)), this method significantly impair VLM performance in generating assembly graphs, leading to more than double accuracy ... | p. 16 (B. Pose Estimation Implementation) |
| B. Pose Estimation Implementation | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Table VII, adding per-step data improves assembly prediction accuracy, demonstrating that per-step inference enhances robot assembly performance. | p. 15 (B. Pose Estimation Implementation) |
| C. Overall Performance Evaluation | EMPIRICAL / REAL-ROBOT OR HARDWARE | ‘TABLE III: Success Rate on 4 Furniture Categories(*) | p. 8 (C. Overall Performance Evaluation) |

## Dataset / Benchmark Role

- **p. 9 / C. Overall Performance Evaluation - extractive body cue:** Failures occur when the RRTConnect algorithm cannot find a feasible trajectory when the planned path results in collisions with the robotic arm or surrounding objects ...
- **p. 8 / C. Overall Performance Evaluation - extractive body cue:** Note that, in this experiment, wwe focus on object-centric motion planning and omit robotic ‘execution in our framework
- **p. 8 / C. Overall Performance Evaluation - extractive body cue:** We source all test furniture models from the IKEA-Manuals dataset [49] Given these manuals along with 3D parts, we generate the preassembly scene images as ...
- **p. 9 / C. Overall Performance Evaluation - extractive body cue:** We present the results in Table IV, showing that our method outperforms the baseline and achieves a high success rate in real-world assembly tasks.
- **p. 17 / B. Pose Estimation Implementation - extractive body cue:** 1) Pose Estimation in the Real World: We utilize FoundationPose [52] to evaluate the 6D pose and point cloud of components in the real-world scene.
- **p. 17 / B. Pose Estimation Implementation - extractive body cue:** During each step of the assembly proces the mesh-along with the RGB and depth images and an object mask-is input into the FoundationPose model, which ...
- **p. 15 / B. Pose Estimation Implementation - extractive body cue:** In contrast, our pose estimation dataset includes per-step data (i.e., subassemblies).
- **p. 15 / B. Pose Estimation Implementation - extractive body cue:** As shown in Table VII, adding per-step data improves assembly prediction accuracy, demonstrating that per-step inference enhances robot assembly performance.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Overview of Manual2Skill Framework. We propose Manual2 ‘enabling robots to understand and execute complex manipulation tasks in mi the input of our pipeline: ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: Framework Overview. (1) GP'T-40 [1] is queried with manual pages to generate a sequential assembly plan, represented as a hierarchical assembly graph. (2) ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3: Qualitative results. Our method significantly outper- forms the baselines. SingleStep fails on moderately complex furniture, while GeoCluster generates physically impossible subassemblies (highlighted in ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4: Pre-Assembly Scene Variations. (Left) original pre- assembly scene. (Middle) parts randomly shuffled along the ground plane. (Right) parts randomly rotated in-place.
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 5: Qualitative results on three furniture categories. We "observe better pose predictions than baselines
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 6: Qualitative Evaluation on real IKEA furniture items. This figure illustrates the assembly process of various IKEA furniture items, including FLISAT, VARIERA, SUNDVIK, and ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 7: Real-World Setup. We use two UFactory xArm6 for assembly and a RealSense D435 camera for pose estimation,
- **p. 14 / Figure/Table caption - extractive body cue:** Fig. 9: Manual images of our proposed dataset. ‘There are variations in furniture shapes, subassemblies, and camera views.

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Failures occur when the RRTConnect algorithm cannot find a feasible trajectory when the planned path results in collisions with the robotic arm or surrounding ... | embodiment, simulator version and control stack | p. 9 (C. Overall Performance Evaluation), p. 8 (C. Overall Performance Evaluation) |
| Task/environment | Note that, in this experiment, wwe focus on object-centric motion planning and omit robotic ‘execution in our framework | reset, timeout, object/scene variation | p. 8 (C. Overall Performance Evaluation), p. 8 (C. Overall Performance Evaluation) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 4 (2. Per-step Assembly Pose Estimation), p. 17 (B. Pose Estimation Implementation) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 2 (B. VLM Guided Robot Learning), p. 3 (A. VLM Guided Hierarchical Assembly Graph Generation) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| As shown in Table X (Ours (w/o Segmentation)), this method significantly impair VLM performance in generating assembly graphs, leading to more than double accuracy ... | definition/direction/unit from same section | p. 16 (B. Pose Estimation Implementation) |
| ‘TABLE III: Success Rate on 4 Furniture Categories(*) | definition/direction/unit from same section | p. 8 (C. Overall Performance Evaluation) |
| Our framework achieves a success rate of $8%, demonstrating the effectiveness of our proposed framework. | definition/direction/unit from same section | p. 8 (C. Overall Performance Evaluation) |
| We present the results in Table IV, showing that our method outperforms the baseline and achieves a high success rate in real-world assembly tasks. | definition/direction/unit from same section | p. 9 (C. Overall Performance Evaluation) |
| The performance score shown is calculated by taking the maximum of Precision, Recall, and FI Score, Mask Seg is an additional method we evaluated, ... | definition/direction/unit from same section | p. 16 (B. Pose Estimation Implementation) |
| Besides using the Success Rate metric defined in Section V-A for evaluating VLM assembly graph generation, we also provide additional analysis using evaluation metrics ... | definition/direction/unit from same section | p. 15 (B. Pose Estimation Implementation) |
| squared error (MSE) loss to measire the distance between the round truth translation ¢ andthe predicted translation f: | definition/direction/unit from same section | p. 14 (B. Pose Estimation Implementation) |
| These findings underscore the practicality and effectiveness of our approach for real-world implementation. ‘The primary | definition/direction/unit from same section | p. 9 (C. Overall Performance Evaluation) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We present the results in Table IV, showing that our method outperforms the baseline and achieves a high success rate in real-world assembly tasks. | comparison identity and matched condition | p. 9 (C. Overall Performance Evaluation) |
| Beyond this, our GPT-4o-based method outperforms both baselines across. all categories in Table VII, which highlights the effectiveness of VLMSs in interpreting manuals and ... | comparison identity and matched condition | p. 16 (B. Pose Estimation Implementation) |
| As the first to propose a comprehensive pipeline for furniture assembly, there is no direct baseline for comparison, So we design a baseline method ... | comparison identity and matched condition | p. 8 (C. Overall Performance Evaluation) |
| (Our system successfully assembles 29 out of 50 furniture pieces, whereas the baseline method assembles only 15. | comparison identity and matched condition | p. 8 (C. Overall Performance Evaluation) |
| Method FLISAT VARIERA SUNDVIK_ KNAGGLIG Oracle Foxe ms 80 wo 900 Mean-Max Pool 525617 400 700 Ours 0 800 680. | comparison identity and matched condition | p. 9 (C. Overall Performance Evaluation) |
| Although Mask Seg slightly outperforms the original version without mask segmentations, we chose the latter for all reported tables. | comparison identity and matched condition | p. 16 (B. Pose Estimation Implementation) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To evaluate the effectiveness of each component in our pipeline, we conduct an ablation study on the chair category. | component/input/data sensitivity | p. 15 (B. Pose Estimation Implementation) |
| 1) Excluding Manual Pages Entirely: To explore whether «4 modified framework could perform the task without manual images by relying on the VLM's existing ... | component/input/data sensitivity | p. 16 (B. Pose Estimation Implementation) |
| 10: Qualitative Results of Ablations. | component/input/data sensitivity | p. 15 (B. Pose Estimation Implementation) |
| E, Assembly Graph Generation Ablation Studies | component/input/data sensitivity | p. 16 (B. Pose Estimation Implementation) |
| Therefore, we report Stage If results as an intermediate measure of how effectively our approach aligns manual images with real components. | component/input/data sensitivity | p. 19 (B. Pose Estimation Implementation) |
| 3) We place a part that is not near any other components, causing it to suspend in midair after each assembly step. | component/input/data sensitivity | p. 8 (C. Overall Performance Evaluation) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper, we present Manual2Skill, a novel framework that enables robots to perform complex assembly tasks guided by highleyel manual instructions. | We present the results in Table IV, showing that our method outperforms the baseline and achieves a high success rate in real-world assembly tasks. | PDF body cue; verify exact table/figure and matched conditions | p. 9 (C. Overall Performance Evaluation), p. 8 (C. Overall Performance Evaluation), p. 16 (B. Pose Estimation Implementation), p. 15 (B. Pose Estimation Implementation), p. 8 (C. Overall Performance Evaluation), p. 9 (C. Overall Performance Evaluation) |
| Primary metric/result | Our framework achieves a success rate of $8%, demonstrating the effectiveness of our proposed framework. | numeric claim only at cited anchor | p. 8 (C. Overall Performance Evaluation) |

- Numeric sentences retained from the body:
- **p. 9 / C. Overall Performance Evaluation - extractive body cue:** We perform each task over 10 trials with varying initial 3D part poses.
- **p. 15 / B. Pose Estimation Implementation - extractive body cue:** Each experiment runs for 800 epochs (approximately 46 hours).
- **p. 17 / B. Pose Estimation Implementation - extractive body cue:** Se Siogksep 1s) Nse 0 700 oo Goocinee 1038021408 2176 1449 699 Sm 417 0 wer 0 08 Our tak Seg) 100 107500 7281 S605 ...
- **p. 18 / B. Pose Estimation Implementation - extractive body cue:** Step 2: Parts Involved: 4, Subassembly from Step 1 Step 3: Parts Involved: 0, Subassembly from Step 2
- **p. 18 / B. Pose Estimation Implementation - extractive body cue:** Step 4: Parts Involved: 5, 6, Subassembly from Step 3 Step 5: Parts Involved: 1, 2, Subassembly from Step 4 Step 6: Parts Involved: 3, ...
- **p. 18 / B. Pose Estimation Implementation - extractive body cue:** Step 1 Step 2: Step 3: Step 4 Step 5: Step 6: Parts Involved

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Failures occur when the RRTConnect algorithm cannot find a feasible trajectory when the planned path results in collisions with the robotic arm or surrounding ... | p. 9 (C. Overall Performance Evaluation) |
| body limitation/failure cue | failure mode arises from planning limitations, particularly in handling complex obstacles. | p. 9 (C. Overall Performance Evaluation) |
| body limitation/failure cue | The most common failure occurs when the VLM fails to generate a fully accurate assembly graph, leading to misalignment between the point cloud and ... | p. 8 (C. Overall Performance Evaluation) |
| body limitation/failure cue | We adopt the assembly success rate as the evaluation metric and define the following situations as a failure: 1) A partis placed at a ... | p. 8 (C. Overall Performance Evaluation) |
| body limitation/failure cue | Manually inspecting each assembly plan reveals common failure modes: the VLM frequently misidentifies parts (e.g. labeling a bench seat as a "tabletop"), generates physically ... | p. 16 (B. Pose Estimation Implementation) |
| body limitation/failure cue | We analyze the faire cases in assembly graph generation mek os The most ffequent failure modes inchude: (1) The VLM a ae] | p. 17 (B. Pose Estimation Implementation) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| 3) Hyperparameters in Training of Pose Estimation: We train our pose estimation model on a single NVIDIA A100 40GB GPU with a batch size ... | p. 15 (B. Pose Estimation Implementation) |
| where 1V is the total number of tials, S; is the number of steps completed in trial j, and Sigai denotes the total number ... | p. 9 (C. Overall Performance Evaluation) |
| Afterward, we use a cosine annealing schedule to decay the learning rate. | p. 15 (B. Pose Estimation Implementation) |
| For detailed implementation of our real-world experiments, please check Appendix G. | p. 8 (C. Overall Performance Evaluation) |
| We perform each task over 10 trials with varying initial 3D part poses. | p. 9 (C. Overall Performance Evaluation) |
| For all pairs (j1, 2) within the same group, we compute the Chamfer distance between the transformed point clouds P;, and P,,, encouraging the ... | p. 14 (B. Pose Estimation Implementation) |
| For each group of equivalent components, we apply the predicted transformation to the point cloud of each component and then compute the Chamfer distance ... | p. 14 (B. Pose Estimation Implementation) |
| The issues of hallucinations in part identification and logical inconsistencies in assembly steps highlight the limitations of relying solely on the VLM's learned priors, ... | p. 16 (B. Pose Estimation Implementation) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / C. Overall Performance Evaluation - extractive body cue:** Failures occur when the RRTConnect algorithm cannot find a feasible trajectory when the planned path results in collisions with the robotic arm or surrounding objects ...
- **p. 9 / C. Overall Performance Evaluation - extractive body cue:** failure mode arises from planning limitations, particularly in handling complex obstacles.
- **p. 8 / C. Overall Performance Evaluation - extractive body cue:** The most common failure occurs when the VLM fails to generate a fully accurate assembly graph, leading to misalignment between the point cloud and the ...
- **p. 8 / C. Overall Performance Evaluation - extractive body cue:** We adopt the assembly success rate as the evaluation metric and define the following situations as a failure: 1) A partis placed at a pose ...
- **p. 16 / B. Pose Estimation Implementation - extractive body cue:** Manually inspecting each assembly plan reveals common failure modes: the VLM frequently misidentifies parts (e.g. labeling a bench seat as a "tabletop"), generates physically plausible ...
- **p. 17 / B. Pose Estimation Implementation - extractive body cue:** We analyze the faire cases in assembly graph generation mek os The most ffequent failure modes inchude: (1) The VLM a ae]

- **PDF anchors reviewed:** datasets p. 9 (C. Overall Performance Evaluation), p. 8 (C. Overall Performance Evaluation), p. 8 (C. Overall Performance Evaluation), p. 9 (C. Overall Performance Evaluation), p. 17 (B. Pose Estimation Implementation), p. 17 (B. Pose Estimation Implementation), metrics p. 16 (B. Pose Estimation Implementation), p. 8 (C. Overall Performance Evaluation), p. 8 (C. Overall Performance Evaluation), p. 9 (C. Overall Performance Evaluation), p. 16 (B. Pose Estimation Implementation), p. 15 (B. Pose Estimation Implementation), baselines p. 9 (C. Overall Performance Evaluation), p. 16 (B. Pose Estimation Implementation), p. 8 (C. Overall Performance Evaluation), p. 8 (C. Overall Performance Evaluation), p. 9 (C. Overall Performance Evaluation), p. 16 (B. Pose Estimation Implementation), results p. 9 (C. Overall Performance Evaluation), p. 8 (C. Overall Performance Evaluation), p. 16 (B. Pose Estimation Implementation), p. 15 (B. Pose Estimation Implementation), p. 8 (C. Overall Performance Evaluation), p. 9 (C. Overall Performance Evaluation).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
