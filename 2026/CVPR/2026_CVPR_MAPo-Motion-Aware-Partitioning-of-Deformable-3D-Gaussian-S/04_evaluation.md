# Evaluation - MAPo: Motion-Aware Partitioning of Deformable 3D Gaussian Splatting for High-Fidelity Dynamic Scene Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Jiao_MAPo_Motion-Aware_Partitioning_of_Deformable_3D_Gaussian_Splatting_for_High-Fidelity_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Jiao_MAPo_Motion-Aware_Partitioning_of_Deformable_3D_Gaussian_Splatting_for_High-Fidelity_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 1 (Figure/Table caption), p. 7 (5.3.1. Quantitative Comparisons), p. 8 (Figure/Table caption), p. 6 (5.1. Dataset and Metrics), p. 2 (Figure/Table caption), p. 4 (Figure/Table caption)): Figure 1. Overview. (a-b) Deformation-based methods often blur details in regions with complex or rapid motion. (c) Our MAPo significantly improves rendering quality in these areas. (d) Ground Truth.

## Evaluation Body Digest

- **p. 6 / 5.1. Dataset and Metrics - extractive PDF cue:** We evaluate our method on two real-world dynamic scene datasets: N3DV [15] and Meet Room [14].
- **p. 6 / 5.1. Dataset and Metrics - extractive PDF cue:** Quantitative comparison on the N3DV dataset.
- **p. 7 / 5.3.1. Quantitative Comparisons - extractive PDF cue:** 2, our method consistently achieves SOTA rendering quality across both datasets while avoiding prohibitive computational overhead, thus offering a compelling balance between high fidelity and ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. An overview of MAPo. (a) 3DGs' deformation process. (b) Compute the dynamic score of 3DGs from history positions during training. (c) High-dynamic 3DGs ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 7. Observation of static partition on Salmon. D3DGS model, which serves as our Baseline, and a naive temporal slicing approach of E-D3DGS (Baseline (seg)) ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4. Effectiveness of temporal partitioning strategy and consistency loss on a toy example. (a) A 3D curve \protect \mathbf {p}(t ) simulates a dynamic ...
- **p. 7 / 5.3.2. Qualitative Comparisons - extractive PDF cue:** For example, in cases with fast-moving hands or detailed facial expressions, baseline methods exhibit severe motion blur and loss of detail.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 9. Ablation study on the Lcross. We visualize how Lcross improves temporal consistency and rendering quality across a par- tition boundary (frames 74-75). The ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5. Experiment (p. 6); 5.1. Dataset and Metrics (p. 6); 5.2. Implementation Details (p. 6); 3. We provide complete implementation details in the ap (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 1. Overview. (a-b) Deformation-based methods often blur details in regions with complex or rapid motion. (c) Our MAPo significantly improves rendering quality in ... | p. 1 (Figure/Table caption) |
| 5.3.1. Quantitative Comparisons | EMPIRICAL / REAL-ROBOT OR HARDWARE | 2, our method consistently achieves SOTA rendering quality across both datasets while avoiding prohibitive computational overhead, thus offering a compelling balance between high fidelity ... | p. 7 (5.3.1. Quantitative Comparisons) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 9. Ablation study on the Lcross. We visualize how Lcross improves temporal consistency and rendering quality across a par- tition boundary (frames 74-75). ... | p. 8 (Figure/Table caption) |
| 5.1. Dataset and Metrics | EMPIRICAL / REAL-ROBOT OR HARDWARE | 2 only reported results on the flame salmon frag1 and was trained on 8 GPUs. | p. 6 (5.1. Dataset and Metrics) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 2. Rendering results of a single unified model. (a) shows the temporally averaged representation, which is visualized by di- rectly rendering the canonical ... | p. 2 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 5.1. Dataset and Metrics - extractive PDF cue:** We evaluate our method on two real-world dynamic scene datasets: N3DV [15] and Meet Room [14].
- **p. 6 / 5.1. Dataset and Metrics - extractive PDF cue:** Quantitative comparison on the N3DV dataset.
- **p. 7 / 5.3.1. Quantitative Comparisons - extractive PDF cue:** 2, our method consistently achieves SOTA rendering quality across both datasets while avoiding prohibitive computational overhead, thus offering a compelling balance between high fidelity and ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Overview. (a-b) Deformation-based methods often blur details in regions with complex or rapid motion. (c) Our MAPo significantly improves rendering quality in these ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2. Rendering results of a single unified model. (a) shows the temporally averaged representation, which is visualized by di- rectly rendering the canonical 3DGs. ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. An overview of MAPo. (a) 3DGs' deformation process. (b) Compute the dynamic score of 3DGs from history positions during training. (c) High-dynamic 3DGs ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4. Effectiveness of temporal partitioning strategy and consistency loss on a toy example. (a) A 3D curve \protect \mathbf {p}(t ) simulates a dynamic ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 5. Qualitative comparisons against existing SOTA methods on the MeetRoom and N3DV dataset. of the current view V , which is captured at timestamp ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Quantitative comparison on the N3DV dataset. 1 flame salmon was trained on only frag1. 2 only reported results on the flame salmon frag1 ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Quantitative comparison on the Meet Room dataset. Storage, training time, and FPS are calculated on discussion.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Progressive component ablation on Meet Room. Stor- age, training time, and FPS are calculated on discussion. Configuration PSNR↑ SSIM↑ LPIPS↓ Storage↓ Time↓

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We evaluate our method on two real-world dynamic scene datasets: N3DV [15] and Meet Room [14]. | embodiment, simulator version and control stack | p. 6 (5.1. Dataset and Metrics), p. 6 (5.1. Dataset and Metrics) |
| Task/environment | Quantitative comparison on the N3DV dataset. | reset, timeout, object/scene variation | p. 6 (5.1. Dataset and Metrics), p. 7 (5.3.1. Quantitative Comparisons) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 5 (4.1.1. Dynamic Score Calculation), p. 5 (4.2. Cross-Frame Consistency Loss) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (1. Introduction), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 3. An overview of MAPo. (a) 3DGs' deformation process. (b) Compute the dynamic score of 3DGs from history positions during training. (c) High-dynamic ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Figure 7. Observation of static partition on Salmon. D3DGS model, which serves as our Baseline, and a naive temporal slicing approach of E-D3DGS (Baseline ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 4. Effectiveness of temporal partitioning strategy and consistency loss on a toy example. (a) A 3D curve \protect \mathbf {p}(t ) simulates a ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| For example, in cases with fast-moving hands or detailed facial expressions, baseline methods exhibit severe motion blur and loss of detail. | definition/direction/unit from same section | p. 7 (5.3.2. Qualitative Comparisons) |
| Figure 9. Ablation study on the Lcross. We visualize how Lcross improves temporal consistency and rendering quality across a par- tition boundary (frames 74-75). ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| In addition to these SOTA baselines, we additionally introduce a simple segmentation baseline, E-D3DGS (seg), for comparison to highlight the advantages of our approach. | comparison identity and matched condition | p. 7 (5.3.1. Quantitative Comparisons) |
| The comparison highlights that baseline methods often produce degraded results in areas with complex or rapid motion. | comparison identity and matched condition | p. 7 (5.3.2. Qualitative Comparisons) |
| Quantitative comparison on the N3DV dataset. | comparison identity and matched condition | p. 6 (5.1. Dataset and Metrics) |
| Figure 5. Qualitative comparisons against existing SOTA methods on the MeetRoom and N3DV dataset. of the current view V , which is captured at ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Table 4. Ablation study on the partition level parameter. All experiments are conducted on the flame salmon frag3. | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Figure 9. Ablation study on the Lcross. We visualize how Lcross improves temporal consistency and rendering quality across a par- tition boundary (frames 74-75). ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Progressive component ablation on Meet Room. | component/input/data sensitivity | p. 7 (5.4. Ablation Study and Analysis) |
| To evaluate our method, we present a progressive ablation study in Tab. | component/input/data sensitivity | p. 7 (5.4. Ablation Study and Analysis) |
| Table 4. Ablation study on the partition level parameter. All experiments are conducted on the flame salmon frag3. | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Figure 9. Ablation study on the Lcross. We visualize how Lcross improves temporal consistency and rendering quality across a par- tition boundary (frames 74-75). ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our key contributions are summarized as follows: • We propose MAPo, a novel framework for high-fidelity dynamic scene reconstruction based on a dynamic scorebased ... | Figure 1. Overview. (a-b) Deformation-based methods often blur details in regions with complex or rapid motion. (c) Our MAPo significantly improves rendering quality in ... | PDF body cue; verify exact table/figure and matched conditions | p. 1 (Figure/Table caption), p. 7 (5.3.1. Quantitative Comparisons), p. 8 (Figure/Table caption), p. 6 (5.1. Dataset and Metrics), p. 2 (Figure/Table caption), p. 4 (Figure/Table caption) |
| Primary metric/result | 2, our method consistently achieves SOTA rendering quality across both datasets while avoiding prohibitive computational overhead, thus offering a compelling balance between high fidelity ... | numeric claim only at cited anchor | p. 7 (5.3.1. Quantitative Comparisons) |

- Numeric sentences retained from the body:
- **p. 6 / 5.1. Dataset and Metrics - extractive PDF cue:** N3DV includes videos at 30 FPS captured by 20 cameras.
- **p. 6 / 5.1. Dataset and Metrics - extractive PDF cue:** Following previous works, we downsample its images to 1352×1014 and segment the longer flame salmon sequence into four 10s clips.
- **p. 6 / 5.1. Dataset and Metrics - extractive PDF cue:** 2 only reported results on the flame salmon frag1 and was trained on 8 GPUs.
- **p. 6 / 5.1. Dataset and Metrics - extractive PDF cue:** Method PSNR↑ SSIM↑ LPIPS↓ Storage↓ Training Time↓ FPS↑ DyNeRF1,2 29.58 - 0.083 56MB 1344 hours 0.01 NeRFPlayer1,3 30.69 0.932 0.111 1654MB 5 hours 36 mins ...
- **p. 6 / 4.2. Cross-Frame Consistency Loss - extractive PDF cue:** We apply Lcross only for training views whose frame indices are within 5 frames of any partition boundary.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The comparison highlights that baseline methods often produce degraded results in areas with complex or rapid motion. | p. 7 (5.3.2. Qualitative Comparisons) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Our implementation builds upon the E-D3DGS codebase. | p. 6 (5.2. Implementation Details) |
| Storage, training time, and FPS are measured on flame salmon frag1. | p. 6 (5.1. Dataset and Metrics) |
| Storage, training time, and FPS are calculated on discussion. | p. 7 (5.2. Implementation Details) |
| Method PSNR↑ SSIM↑ LPIPS↓ Storage↓ Training Time↓ FPS↑ D3DGS 25.81 0.890 0.233 | p. 7 (5.2. Implementation Details) |
| Here, m is a hyperparameter controlling the number of recorded positions per 3DG. | p. 4 (4.1.1. Dynamic Score Calculation) |
| For the i-th 3DG, its maximum displacement ri and position variance vi are computed as: r _i = \ big l \/ \ max ... | p. 4 (4.1.1. Dynamic Score Calculation) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 5.3.2. Qualitative Comparisons - extractive PDF cue:** The comparison highlights that baseline methods often produce degraded results in areas with complex or rapid motion.

- **PDF anchors reviewed:** datasets p. 6 (5.1. Dataset and Metrics), p. 6 (5.1. Dataset and Metrics), p. 7 (5.3.1. Quantitative Comparisons), metrics p. 4 (Figure/Table caption), p. 7 (Figure/Table caption), p. 5 (Figure/Table caption), p. 7 (5.3.2. Qualitative Comparisons), p. 8 (Figure/Table caption), baselines p. 7 (5.3.1. Quantitative Comparisons), p. 7 (5.3.2. Qualitative Comparisons), p. 6 (5.1. Dataset and Metrics), p. 6 (Figure/Table caption), p. 8 (Figure/Table caption), p. 8 (Figure/Table caption), results p. 1 (Figure/Table caption), p. 7 (5.3.1. Quantitative Comparisons), p. 8 (Figure/Table caption), p. 6 (5.1. Dataset and Metrics), p. 2 (Figure/Table caption), p. 4 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
