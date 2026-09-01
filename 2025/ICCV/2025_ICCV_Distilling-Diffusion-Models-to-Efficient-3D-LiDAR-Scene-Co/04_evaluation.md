# Evaluation - Distilling Diffusion Models to Efficient 3D LiDAR Scene Completion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_Distilling_Diffusion_Models_to_Efficient_3D_LiDAR_Scene_Completion_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_Distilling_Diffusion_Models_to_Efficient_3D_LiDAR_Scene_Completion_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (5.2. Ablation study), p. 7 (5.1. Scene completion), p. 6 (5.1. Scene completion), p. 6 (5.1. Scene completion), p. 2 (Figure/Table caption), p. 8 (5.3. Qualitative analysis)): However, after considering the structural loss, the performance of ScoreLiDAR improves significantly, which achieves better performance on all metrics.

## Evaluation Body Digest

- **p. 6 / 5. Experiment - extractive PDF cue:** Ablation study of different sampling steps on the SemanticKITTI dataset. completion tasks (Sec.
- **p. 7 / 5.2. Ablation study - extractive PDF cue:** The results show that the variant without structural loss exhibits lower performance in scene completion on both datasets.
- **p. 8 / 5.3. Qualitative analysis - extractive PDF cue:** 5, on both datasets, the difference of point distance matrix between the completed scene of LiDiff [23] and the ground truth is the largest, followed ...
- **p. 6 / 5.1. Scene completion - extractive PDF cue:** We validate ScoreLiDAR on SemanticKITTI [1] and KITTI-360 [16] datasets.
- **p. 7 / 5.3. Qualitative analysis - extractive PDF cue:** 4 shows the completed scenes by our proposed ScoreLiDAR and LiDiff [23] on KITTI-360.
- **p. 8 / 5.3. Qualitative analysis - extractive PDF cue:** The bar chart shows the distribution of distances between corresponding points in the completed and ground truth scenes.
- **p. 7 / 5.2. Ablation study - extractive PDF cue:** We compared the scene completion performances of the proposed ScoreLiDAR with a variant that does not incorporate structural loss.
- **p. 7 / 5.3. Qualitative analysis - extractive PDF cue:** To further demonstrate the effectiveness of ScoreLiDAR and the structural loss, we calculate the distance between the points in the completed scene and their corresponding ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5. Experiment (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5.2. Ablation study | SYSTEM / EVALUATION SCOPE UNRESOLVED | However, after considering the structural loss, the performance of ScoreLiDAR improves significantly, which achieves better performance on all metrics. | p. 7 (5.2. Ablation study) |
| 5.1. Scene completion | SYSTEM / EVALUATION SCOPE UNRESOLVED | ScoreLiDAR achieves better completion than LiDiff [24] with fewer sampling steps. a fivefold speedup with 12% improvement in CD and 2% in JSD compared ... | p. 7 (5.1. Scene completion) |
| 5.1. Scene completion | SYSTEM / EVALUATION SCOPE UNRESOLVED | The performance of ScoreLiDAR outperforms the teacher model LiDiff [23]. | p. 6 (5.1. Scene completion) |
| 5.1. Scene completion | SYSTEM / EVALUATION SCOPE UNRESOLVED | ScoreLiDAR also achieves optimal performance in most cases and boasts 5012 | p. 6 (5.1. Scene completion) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 2. A visualization of LiDAR scene completion perfor- mances with different models on SemanticKITTI [1] dataset. Gen- erally, our proposed ScoreLiDAR achieves better ... | p. 2 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 5. Experiment - extractive PDF cue:** Ablation study of different sampling steps on the SemanticKITTI dataset. completion tasks (Sec.
- **p. 7 / 5.2. Ablation study - extractive PDF cue:** The results show that the variant without structural loss exhibits lower performance in scene completion on both datasets.
- **p. 8 / 5.3. Qualitative analysis - extractive PDF cue:** 5, on both datasets, the difference of point distance matrix between the completed scene of LiDiff [23] and the ground truth is the largest, followed ...
- **p. 6 / 5.1. Scene completion - extractive PDF cue:** We validate ScoreLiDAR on SemanticKITTI [1] and KITTI-360 [16] datasets.
- **p. 7 / 5.3. Qualitative analysis - extractive PDF cue:** 4 shows the completed scenes by our proposed ScoreLiDAR and LiDiff [23] on KITTI-360.
- **p. 8 / 5.3. Qualitative analysis - extractive PDF cue:** The bar chart shows the distribution of distances between corresponding points in the completed and ground truth scenes.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. A demonstration of the LiDAR scene completion examples. Given a sparse LiDAR scan in (a), the model aims to recover the ground-truth dense ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2. A visualization of LiDAR scene completion perfor- mances with different models on SemanticKITTI [1] dataset. Gen- erally, our proposed ScoreLiDAR achieves better scene ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. The overall structure of ScoreLiDAR. (1) The student model generates the completed scene based on the sparse scan. (2) The sparse scan and ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. The completion performance on the SemanticKITTI dataset. Colors denote the 1st , 2nd , and 3rd best-performing model. The sampling time is estimated ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. The completion performance on the KITTI-360 dataset. The meaning of notations is the same as those in Tab. 1.
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 3. Ablation study of the structural loss.
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 4. Ablation study of different sampling steps on the Se- manticKITTI dataset. completion tasks (Sec. 5.1). Secondly, we present the re- sults of ablation ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4. Qualitative results on KITTI-360. ScoreLiDAR achieves better completion than LiDiff [24] with fewer sampling steps. a fivefold speedup with 12% improvement in CD ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Ablation study of different sampling steps on the SemanticKITTI dataset. completion tasks (Sec. | embodiment, simulator version and control stack | p. 6 (5. Experiment), p. 7 (5.2. Ablation study) |
| Task/environment | The results show that the variant without structural loss exhibits lower performance in scene completion on both datasets. | reset, timeout, object/scene variation | p. 7 (5.2. Ablation study), p. 8 (5.3. Qualitative analysis) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (3.1. Brief introduction of diffusion models), p. 3 (3.2. 3D LiDAR scene completion diffusion models) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (3.2. 3D LiDAR scene completion diffusion models), p. 5 (4.2. Structural loss) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We compared the scene completion performances of the proposed ScoreLiDAR with a variant that does not incorporate structural loss. | definition/direction/unit from same section | p. 7 (5.2. Ablation study) |
| To further demonstrate the effectiveness of ScoreLiDAR and the structural loss, we calculate the distance between the points in the completed scene and their ... | definition/direction/unit from same section | p. 7 (5.3. Qualitative analysis) |
| Figure 2. A visualization of LiDAR scene completion perfor- mances with different models on SemanticKITTI [1] dataset. Gen- erally, our proposed ScoreLiDAR achieves better ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Secondly, we present the results of ablation studies showing the effectiveness of the structural loss and the performances of ScoreLiDAR given different sampling steps ... | definition/direction/unit from same section | p. 6 (5. Experiment) |
| 5, on both datasets, the difference of point distance matrix between the completed scene of LiDiff [23] and the ground truth is the largest, ... | definition/direction/unit from same section | p. 8 (5.3. Qualitative analysis) |
| Figure 5. The qualitative analysis of structural loss. The bar chart shows the distribution of distances between corresponding points in the completed and ground ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Figure 1. A demonstration of the LiDAR scene completion examples. Given a sparse LiDAR scan in (a), the model aims to recover the ground-truth ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| The performance of ScoreLiDAR outperforms the teacher model LiDiff [23]. | definition/direction/unit from same section | p. 6 (5.1. Scene completion) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Compared to the SOTA method LiDiff [23] with refinement, which takes 30.55 seconds to complete a scene, ScoreLiDAR completes a scene in just 5.47 ... | comparison identity and matched condition | p. 6 (5.1. Scene completion) |
| In addition, we compared the ablation results about the terms of structural loss, different keypoint selection methods, varying numbers of keypoints, and different values ... | comparison identity and matched condition | p. 7 (5.2. Ablation study) |
| The performance of ScoreLiDAR outperforms the teacher model LiDiff [23]. | comparison identity and matched condition | p. 6 (5.1. Scene completion) |
| ScoreLiDAR achieves completion results with higher quality and greater fidelity in less time compared to LiDiff. | comparison identity and matched condition | p. 7 (5.3. Qualitative analysis) |
| Figure 1. A demonstration of the LiDAR scene completion examples. Given a sparse LiDAR scan in (a), the model aims to recover the ground-truth ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| 5, on both datasets, the difference of point distance matrix between the completed scene of LiDiff [23] and the ground truth is the largest, ... | comparison identity and matched condition | p. 8 (5.3. Qualitative analysis) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| The results show that the variant without structural loss exhibits lower performance in scene completion on both datasets. | component/input/data sensitivity | p. 7 (5.2. Ablation study) |
| 5, on both datasets, the difference of point distance matrix between the completed scene of LiDiff [23] and the ground truth is the largest, ... | component/input/data sensitivity | p. 8 (5.3. Qualitative analysis) |
| Secondly, we present the results of ablation studies showing the effectiveness of the structural loss and the performances of ScoreLiDAR given different sampling steps ... | component/input/data sensitivity | p. 6 (5. Experiment) |
| In this part, we conduct the ablation study to verify the effectiveness of the structural loss in the training of the proposed ScoreLiDAR. | component/input/data sensitivity | p. 7 (5.2. Ablation study) |
| Ablation study of different sampling steps on the SemanticKITTI dataset. completion tasks (Sec. | component/input/data sensitivity | p. 6 (5. Experiment) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this work, we propose ScoreLiDAR, a novel distillation method tailored for 3D LiDAR scene completion diffusion models, which enables efficient and high-quality scene ... | However, after considering the structural loss, the performance of ScoreLiDAR improves significantly, which achieves better performance on all metrics. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (5.2. Ablation study), p. 7 (5.1. Scene completion), p. 6 (5.1. Scene completion), p. 6 (5.1. Scene completion), p. 2 (Figure/Table caption), p. 8 (5.3. Qualitative analysis) |
| Primary metric/result | ScoreLiDAR achieves better completion than LiDiff [24] with fewer sampling steps. a fivefold speedup with 12% improvement in CD and 2% in JSD compared ... | numeric claim only at cited anchor | p. 7 (5.1. Scene completion) |

- Numeric sentences retained from the body:
- **p. 6 / 5. Experiment - extractive PDF cue:** We first evaluate the performance of ScoreLiDAR in scene Model CD ↓ JSD ↓ EMD ↓ Time (s) ↓ LiDiff (50 steps) [23] 0.434 0.444 ...
- **p. 7 / 5.1. Scene completion - extractive PDF cue:** Input Sparse Scan Ground Truth LiDiff(50 steps refined) ScoreLiDAR (8 steps refined) (a) (b) (c) (d) Figure 4.
- **p. 7 / 5.3. Qualitative analysis - extractive PDF cue:** In contrast, the scene completed by ScoreLiDAR with only 8 steps in Fig.
- **p. 4 / 3.2. 3D LiDAR scene completion diffusion models - extractive PDF cue:** Auxiliary diffusion model Teacher diffusion model !" ℒ#$ = #" $%, &, ' -#! $%, &, ' & & ℒ'( = # -#! $%, &, ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Thus, further exploration is required to find a more effective method to improve the training process of ScoreLiDAR and avoid the limitations of the ... | p. 8 (6. Conclusion) |
| body limitation/failure cue | We compared the scene completion performances of the proposed ScoreLiDAR with a variant that does not incorporate structural loss. | p. 7 (5.2. Ablation study) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Ablation study of different sampling steps on the SemanticKITTI dataset. completion tasks (Sec. | p. 6 (5. Experiment) |
| Secondly, we present the results of ablation studies showing the effectiveness of the structural loss and the performances of ScoreLiDAR given different sampling steps ... | p. 6 (5. Experiment) |
| In contrast, the scene completed by ScoreLiDAR with only 8 steps in Fig. | p. 7 (5.3. Qualitative analysis) |
| Input Sparse Scan Ground Truth LiDiff(50 steps refined) ScoreLiDAR (8 steps refined) (a) (b) (c) (d) Figure 4. | p. 7 (5.1. Scene completion) |
| During the training, the diffusion model tries to predict the added noise at different timesteps t. | p. 3 (3.1. Brief introduction of diffusion models) |
| In this process, the number of required inference steps varies depending on different sampling methods. | p. 3 (3.1. Brief introduction of diffusion models) |
| Our goal is to distill a pre-trained 3D LiDAR scene completion diffusion model into a student model with significantly fewer sampling steps, enabling efficient ... | p. 4 (4. Method) |
| Therefore, we select n key points to compute the distance matrix with n ≪M. | p. 5 (4.2. Structural loss) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 6. Conclusion - extractive PDF cue:** Thus, further exploration is required to find a more effective method to improve the training process of ScoreLiDAR and avoid the limitations of the teacher ...
- **p. 7 / 5.2. Ablation study - extractive PDF cue:** We compared the scene completion performances of the proposed ScoreLiDAR with a variant that does not incorporate structural loss.

- **PDF anchors reviewed:** datasets p. 6 (5. Experiment), p. 7 (5.2. Ablation study), p. 8 (5.3. Qualitative analysis), p. 6 (5.1. Scene completion), p. 7 (5.3. Qualitative analysis), p. 8 (5.3. Qualitative analysis), metrics p. 7 (5.2. Ablation study), p. 7 (5.3. Qualitative analysis), p. 2 (Figure/Table caption), p. 6 (5. Experiment), p. 8 (5.3. Qualitative analysis), p. 8 (Figure/Table caption), baselines p. 6 (5.1. Scene completion), p. 7 (5.2. Ablation study), p. 6 (5.1. Scene completion), p. 7 (5.3. Qualitative analysis), p. 1 (Figure/Table caption), p. 8 (5.3. Qualitative analysis), results p. 7 (5.2. Ablation study), p. 7 (5.1. Scene completion), p. 6 (5.1. Scene completion), p. 6 (5.1. Scene completion), p. 2 (Figure/Table caption), p. 8 (5.3. Qualitative analysis).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
