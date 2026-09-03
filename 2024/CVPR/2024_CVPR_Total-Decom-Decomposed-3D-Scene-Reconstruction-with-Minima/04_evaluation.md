# Evaluation - Total-Decom: Decomposed 3D Scene Reconstruction with Minimal Interaction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Lyu_Total-Decom_Decomposed_3D_Scene_Reconstruction_with_Minimal_Interaction_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Lyu_Total-Decom_Decomposed_3D_Scene_Reconstruction_with_Minimal_Interaction_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (7.2. Results), p. 7 (7.1. Experiment Setup), p. 8 (7.2. Results), p. 3 (Figure/Table caption)): Our reconstructed results also outperform ObjSDF++ qualitatively.

## Evaluation Body Digest

- **p. 7 / 7.1. Experiment Setup - extractive body cue:** To further demonstrate the robustness of our method, we also use the ScanNet [6] as the real-world dataset which provides 1513 scenes.
- **p. 7 / 7.2. Results - extractive body cue:** Scene reconstruction and object decomposition on the Replica dataset.
- **p. 8 / 7.2. Results - extractive body cue:** Visualized assessments on different datasets.
- **p. 8 / 7.2. Results - extractive body cue:** ObjSDF++ ObjSDF++ Ours Ours Room_0 Room_0 Office_4 Background Foreground Decomposed Objects Replica Office_4 Background Decomposed Results Scene_0050 Scene_0000 Apartment ScanNet NICE-SLAM Billiard room Self-captured scene ...
- **p. 7 / 7.1. Experiment Setup - extractive body cue:** The reconstruction results are mainly evaluated by Chamfer-L1 and F-Score.
- **p. 7 / 7.2. Results - extractive body cue:** To evaluate the decomposed reconstruction accuracy of Total-Decom, we conduct experiments on the Replica dataset as it provides ground-truth objects' meshes for evaluation.
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 5. In the following, we first elaborate on our recon- struction network and rendering formula, and then detail our core design for achieving background ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Indoor scenes consist of complex compositions of objects and backgrounds. Our proposed method, Total-Decom, (a) performs 3D reconstruction from posed multiview images, (b) ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 7. Experiments (p. 7); 7.1. Experiment Setup (p. 7); 7.2. Results (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 7.2. Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our reconstructed results also outperform ObjSDF++ qualitatively. | p. 7 (7.2. Results) |
| 7.1. Experiment Setup | EMPIRICAL / REAL-ROBOT OR HARDWARE | The reconstruction results are mainly evaluated by Chamfer-L1 and F-Score. | p. 7 (7.1. Experiment Setup) |
| 7.2. Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | We present the reconstruction results for the background, foreground and decomposed objects on Replica [31], ScanNet [6], NICE-SLAM [44] and our self-captured billiard room. | p. 8 (7.2. Results) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 3. Comparison on different decomposition methods with SAM feature. SAM + region growing represents object extraction with our method. SAM + similarity indicates ... | p. 3 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 7 / 7.1. Experiment Setup - extractive body cue:** To further demonstrate the robustness of our method, we also use the ScanNet [6] as the real-world dataset which provides 1513 scenes.
- **p. 7 / 7.2. Results - extractive body cue:** Scene reconstruction and object decomposition on the Replica dataset.
- **p. 8 / 7.2. Results - extractive body cue:** Visualized assessments on different datasets.
- **p. 8 / 7.2. Results - extractive body cue:** ObjSDF++ ObjSDF++ Ours Ours Room_0 Room_0 Office_4 Background Foreground Decomposed Objects Replica Office_4 Background Decomposed Results Scene_0050 Scene_0000 Apartment ScanNet NICE-SLAM Billiard room Self-captured scene ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Indoor scenes consist of complex compositions of objects and backgrounds. Our proposed method, Total-Decom, (a) performs 3D reconstruction from posed multiview images, (b) ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Visualization for distilled generalized features. ever, these methods rely heavily on accurate multi-view consistent ground-truth instance-level labels and cannot ef- fectively preserve all ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3. Comparison on different decomposition methods with SAM feature. SAM + region growing represents object extraction with our method. SAM + similarity indicates object ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 4. Consequently, we propose a novel approach that leverages SAM features and a mesh-based region-growing method to decompose a 3D scene with minimal human ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 4. Visualization of the SAM feature for the same object in different views with t-SNE [33]. All the features are in the same feature ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 5. In the following, we first elaborate on our recon- struction network and rendering formula, and then detail our core design for achieving background ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 5. Overview of Total-Decom. (1) Foreground and background decomposed neural reconstruction. We have four networks in this stage to predict the geometry, appearance, semantic, ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 6. The effect of different constraint on Replica room 1. where ˆpf, ˆpw represent the probabilities of the pixel being floor and wall derived ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | To further demonstrate the robustness of our method, we also use the ScanNet [6] as the real-world dataset which provides 1513 scenes. | embodiment, simulator version and control stack | p. 7 (7.1. Experiment Setup), p. 7 (7.2. Results) |
| Task/environment | Scene reconstruction and object decomposition on the Replica dataset. | reset, timeout, object/scene variation | p. 7 (7.2. Results), p. 8 (7.2. Results) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 1 (Abstract), p. 2 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (1. Introduction), p. 4 (5. Neural Implicit Feature Distillation and Sur) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The reconstruction results are mainly evaluated by Chamfer-L1 and F-Score. | definition/direction/unit from same section | p. 7 (7.1. Experiment Setup) |
| To evaluate the decomposed reconstruction accuracy of Total-Decom, we conduct experiments on the Replica dataset as it provides ground-truth objects' meshes for evaluation. | definition/direction/unit from same section | p. 7 (7.2. Results) |
| Fig. 5. In the following, we first elaborate on our recon- struction network and rendering formula, and then detail our core design for achieving ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Figure 1. Indoor scenes consist of complex compositions of objects and backgrounds. Our proposed method, Total-Decom, (a) performs 3D reconstruction from posed multiview images, ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 3. Comparison on different decomposition methods with SAM feature. SAM + region growing represents object extraction with our method. SAM + similarity indicates ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Figure 2. Visualization for distilled generalized features. ever, these methods rely heavily on accurate multi-view consistent ground-truth instance-level labels and cannot ef- fectively preserve ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Figure 5. Overview of Total-Decom. (1) Foreground and background decomposed neural reconstruction. We have four networks in this stage to predict the geometry, appearance, ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We mainly compared our approach with the ObjSDF++, the state-of-the-art method that decomposes the scene structure with pseudo geometry priors as far as we ... | comparison identity and matched condition | p. 7 (7.2. Results) |
| The compared methods are mainly divided into two categories. | comparison identity and matched condition | p. 7 (7.1. Experiment Setup) |
| Figure 3. Comparison on different decomposition methods with SAM feature. SAM + region growing represents object extraction with our method. SAM + similarity indicates ... | comparison identity and matched condition | p. 3 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 6. The effect of different constraint on Replica room 1. where ˆpf, ˆpw represent the probabilities of the pixel being floor and wall ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In sum, our main contributions are as follows: • We introduce a novel pipeline that seamlessly integrates the segment anything model with hybrid implicit-explicit ... | Our reconstructed results also outperform ObjSDF++ qualitatively. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (7.2. Results), p. 7 (7.1. Experiment Setup), p. 8 (7.2. Results), p. 3 (Figure/Table caption) |
| Primary metric/result | The reconstruction results are mainly evaluated by Chamfer-L1 and F-Score. | numeric claim only at cited anchor | p. 7 (7.1. Experiment Setup) |

- Numeric sentences retained from the body:
- **p. 7 / 7.1. Experiment Setup - extractive body cue:** Our method is implemented using Pytorch and uses the Adam optimizer with a learning rate of 5e -4 for the tiny MLP part ( 2 ...
- **p. 7 / 7.1. Experiment Setup - extractive body cue:** To further demonstrate the robustness of our method, we also use the ScanNet [6] as the real-world dataset which provides 1513 scenes.
- **p. 7 / 7.2. Results - extractive body cue:** Scene Reconstruction Decomposed Reconstruction Method Chamfer-L1 ↓ F-score ↑ Chamfer-L1 ↓ F-score ↑ ObjSDF++ 3.58 85.69 3.84 ± 0.02 79.49 ± 0.08 Ours 3.53 85.82 ...
- **p. 7 / 7.2. Results - extractive body cue:** Because the number of decomposed objects from ObjSDF++ is limited (around 25 objects per scene), we only evaluate the foreground objects that ObjSDF++ can extract ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 3. Comparison on different decomposition methods with SAM feature. SAM + region growing represents object extraction with our method. SAM + similarity indicates ... | p. 3 (Figure/Table caption) |
| body limitation/failure cue | Figure 2. Visualization for distilled generalized features. ever, these methods rely heavily on accurate multi-view consistent ground-truth instance-level labels and cannot ef- fectively preserve ... | p. 3 (Figure/Table caption) |
| body limitation/failure cue | Since this type of method does not introduce geometric constraints, we mainly compare the way of decomposition. | p. 7 (7.1. Experiment Setup) |
| body limitation/failure cue | To further demonstrate the robustness of our method, we also use the ScanNet [6] as the real-world dataset which provides 1513 scenes. | p. 7 (7.1. Experiment Setup) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Our method is implemented using Pytorch and uses the Adam optimizer with a learning rate of 5e -4 for the tiny MLP part ( ... | p. 7 (7.1. Experiment Setup) |
| Scene reconstruction from multi-view images is a fundamental problem in computer vision and graphics. | p. 1 (Abstract) |
| Recently, neural implicit surface reconstruction methods such as VolSDF [39] and NeuS [35] have been proposed to address this problem and have achieved highThis ... | p. 1 (1. Introduction) |
| This process leverages distilled feature similarities of vertices and 3D mesh geometry topology for accurate object decomposition, further ensuring precision by confining the growing ... | p. 2 (1. Introduction) |
| Then, in order to identify and separate the desired object for surface decomposition, we utilize the SAM decoder and the rendered SAM feature, converting ... | p. 2 (1. Introduction) |
| T r i and αi represent the transmittance and alpha value (a.k.a opacity) of the sample point, and their values can be computed by ... | p. 4 (5. Neural Implicit Feature Distillation and Sur) |
| Then, given rendered images and features from the mesh surface, our method employs the SAM decoder to convert image clicks into dense object masks ... | p. 4 (4. Overview) |
| Passing the feature image and user-selected prompt into the SAM decoder allows us to obtain the 2D mask of the regions of interest. | p. 5 (5. Neural Implicit Feature Distillation and Sur) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3. Comparison on different decomposition methods with SAM feature. SAM + region growing represents object extraction with our method. SAM + similarity indicates object ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Visualization for distilled generalized features. ever, these methods rely heavily on accurate multi-view consistent ground-truth instance-level labels and cannot ef- fectively preserve all ...
- **p. 7 / 7.1. Experiment Setup - extractive body cue:** Since this type of method does not introduce geometric constraints, we mainly compare the way of decomposition.
- **p. 7 / 7.1. Experiment Setup - extractive body cue:** To further demonstrate the robustness of our method, we also use the ScanNet [6] as the real-world dataset which provides 1513 scenes.

- **Evidence anchors reviewed:** datasets p. 7 (7.1. Experiment Setup), p. 7 (7.2. Results), p. 8 (7.2. Results), p. 8 (7.2. Results), metrics p. 7 (7.1. Experiment Setup), p. 7 (7.2. Results), p. 4 (Figure/Table caption), p. 1 (Figure/Table caption), p. 3 (Figure/Table caption), p. 3 (Figure/Table caption), baselines p. 7 (7.2. Results), p. 7 (7.1. Experiment Setup), p. 3 (Figure/Table caption), results p. 7 (7.2. Results), p. 7 (7.1. Experiment Setup), p. 8 (7.2. Results), p. 3 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
