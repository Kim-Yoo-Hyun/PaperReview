# Evaluation - SIU3R: Simultaneous Scene Understanding and 3D Reconstruction Beyond Feature Alignment

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=GtImvTta8x; PDF retrieval source: https://arxiv.org/pdf/2507.02705. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (4 Experiments), p. 9 (4 Experiments), p. 8 (Figure/Table caption), p. 8 (4 Experiments), p. 7 (4 Experiments), p. 5 (Figure/Table caption)): We can see that this module can significantly w/ R→U w/o R→U RGB w/ R→U w/o R→U RGB ✓ ☓ ✓ ☓ Figure 6: Ablation on Multi-View Mask Aggregation (R→U). ...

## Evaluation Body Digest

- **p. 15 / A.1 Data Preprocessing - extractive body cue:** We adopt the official training and validation dataset splitting of ScanNet, and then resize and crop original images to centered images at 256 × 256 ...
- **p. 7 / 4 Experiments - extractive body cue:** We utilize ScanNet[17] for training and validation, the largest public dataset that concurrently provides multi-view images with dense semantic/instance segmentation labels and text-referred segmentation labels[56].
- **p. 8 / 4 Experiments - extractive body cue:** We also conduct experiments to validate the generalizability of our method to more input views, unseen data domains and real-world scenarios.
- **p. 7 / 4 Experiments - extractive body cue:** All baseline methods are evaluated on ScanNet dataset under the same protocols as ours for fair comparison.
- **p. 9 / 4 Experiments - extractive body cue:** Please refer to our appendices for more results (3D instance and panoptic segmentation, extension to versatile 3D editing, comparisons with more 3D-based baselines, real-world scenarios, ...
- **p. 8 / 4 Experiments - extractive body cue:** For scene understanding, existing methods like LSeg and Mask2Former are limited to 2D-only understanding of input context views and specific segmentation tasks.
- **p. 9 / 4 Experiments - extractive body cue:** With this module that employs mask guidance for geometry refinement, we can obtain much better 3D geometries ("depth estimation") and higher visual quality ("novel view ...
- **p. 15 / A.1 Data Preprocessing - extractive body cue:** During training, we constrain the IoU to [0.3, 0.8] to randomly select our training samples from scenes.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiments (p. 7); A Additional Implementation Details (p. 15); A.3 Implementation Details about Versatile 3D Editing (p. 16).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | We can see that this module can significantly w/ R→U w/o R→U RGB w/ R→U w/o R→U RGB ✓ ☓ ✓ ☓ Figure 6: ... | p. 9 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | As demonstrated in Fig.5 (b), thanks to our simultaneous task modeling and Multi-View Mask Aggregation mechanism, our method can effectively leverage geometric clues to ... | p. 9 (4 Experiments) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 5: Qualitative Results. that can achieve 3D-aware understanding is LSM. However, its understanding capability is restricted by its source 2D model (LSeg) due ... | p. 8 (Figure/Table caption) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | RGB GTs Ours LSM LSeg Texts (b) Semantic Segmentation (best viewed in enlarged resolution) (c) Text-Referred Segmentation (best viewed in enlarged resolution) Inputs GTs ... | p. 8 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | For 3D reconstruction, we evaluate the performance from two aspects: depth estimation and novel view synthesis, using depth accuracy metrics (i.e., AbsRel and RMSE) ... | p. 7 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 15 / A.1 Data Preprocessing - extractive body cue:** We adopt the official training and validation dataset splitting of ScanNet, and then resize and crop original images to centered images at 256 × 256 ...
- **p. 7 / 4 Experiments - extractive body cue:** We utilize ScanNet[17] for training and validation, the largest public dataset that concurrently provides multi-view images with dense semantic/instance segmentation labels and text-referred segmentation labels[56].
- **p. 8 / 4 Experiments - extractive body cue:** We also conduct experiments to validate the generalizability of our method to more input views, unseen data domains and real-world scenarios.
- **p. 7 / 4 Experiments - extractive body cue:** All baseline methods are evaluated on ScanNet dataset under the same protocols as ours for fair comparison.
- **p. 9 / 4 Experiments - extractive body cue:** Please refer to our appendices for more results (3D instance and panoptic segmentation, extension to versatile 3D editing, comparisons with more 3D-based baselines, real-world scenarios, ...
- **p. 8 / 4 Experiments - extractive body cue:** For scene understanding, existing methods like LSeg and Mask2Former are limited to 2D-only understanding of input context views and specific segmentation tasks.
- **p. 9 / 4 Experiments - extractive body cue:** With this module that employs mask guidance for geometry refinement, we can obtain much better 3D geometries ("depth estimation") and higher visual quality ("novel view ...
- **p. 15 / A.1 Data Preprocessing - extractive body cue:** During training, we constrain the IoU to [0.3, 0.8] to randomly select our training samples from scenes.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Simultaneous Scene Understanding and 3D Reconstruction (SIU3R). (a) 2D-to-3D Feature alignment paradigm of previous methods. (b) Alignment-free paradigm of our SIU3R method. (c) ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Pipeline. Our method consists of Image and Text Encoders for extracting multi-view and text features, Gaussian Decoder for decoding pixel-aligned 3D Gaussians, Unified ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Unified Query Decoder. In (a), we employ multi-view semantic-focused features fU, unified queries Q, and L1 stacked cross-/self-attention layer blocks to decode cross-view ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4: Mutual Benefit Mechanism. In (a), our Multi-View Mask Aggregation module utilizes reconstructed 3D Gaussians as geometry clues to improve cross-view mask consistency in ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Quantitative comparisons. "†", "‡" and "⋆" denote reconstruction-only, understanding-only, and simultaneous scene understanding and 3D reconstruction methods, respectively. "-" indicates that the corresponding ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Qualitative Results. that can achieve 3D-aware understanding is LSM. However, its understanding capability is restricted by its source 2D model (LSeg) due to ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 2: Comparisons between design choices of Multi-View Aggregation. 3D Reconstruction Context Views(2D-Only) Novel View (3D-aware) Memory PSNR↑SSIM↑LPIPS↓mIoUs↑mAP↑ PQ↑ mIoUt↑mIoUs↑mAP↑
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 6: Ablation on Multi-View Mask Aggregation (R→U). improve our performance in both 2D-only and 3D-aware scene understanding, without sacrificing 3D reconstruction accuracy due to ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We adopt the official training and validation dataset splitting of ScanNet, and then resize and crop original images to centered images at 256 × ... | embodiment, simulator version and control stack | p. 15 (A.1 Data Preprocessing), p. 7 (4 Experiments) |
| Task/environment | We utilize ScanNet[17] for training and validation, the largest public dataset that concurrently provides multi-view images with dense semantic/instance segmentation labels and text-referred segmentation ... | reset, timeout, object/scene variation | p. 7 (4 Experiments), p. 8 (4 Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 6 (3 Methodology), p. 3 (3 Methodology) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (3 Methodology), p. 6 (3 Methodology) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For 3D reconstruction, we evaluate the performance from two aspects: depth estimation and novel view synthesis, using depth accuracy metrics (i.e., AbsRel and RMSE) ... | definition/direction/unit from same section | p. 7 (4 Experiments) |
| We can see that this module can significantly w/ R→U w/o R→U RGB w/ R→U w/o R→U RGB ✓ ☓ ✓ ☓ Figure 6: ... | definition/direction/unit from same section | p. 9 (4 Experiments) |
| For 3D reconstruction, unlike MVSplat and PixelSplat that require camera poses as input, or LSM that relies on ground-truth depth supervision, our framework eliminates ... | definition/direction/unit from same section | p. 8 (4 Experiments) |
| The overlap is determined by a pair-wise Intersection over Union (IoU) metric as shown in Fig.I. | definition/direction/unit from same section | p. 15 (A.1 Data Preprocessing) |
| During training, we constrain the IoU to [0.3, 0.8] to randomly select our training samples from scenes. | definition/direction/unit from same section | p. 15 (A.1 Data Preprocessing) |
| For understanding-only method (i.e., Mask2Former), we only use its mask losses for supervision. | definition/direction/unit from same section | p. 7 (4 Experiments) |
| The qualitative results also demonstrate the superiority of our method. | definition/direction/unit from same section | p. 9 (4 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Therefore, we evaluate our method against three types of baseline methods, all of which are state-of-the-arts on their respective tasks: 1) Sparse-view 3D reconstruction: ... | comparison identity and matched condition | p. 7 (4 Experiments) |
| As shown in Table 1, our approach outperforms all baselines across all tasks by a clear margin. | comparison identity and matched condition | p. 8 (4 Experiments) |
| All baseline methods are evaluated on ScanNet dataset under the same protocols as ours for fair comparison. | comparison identity and matched condition | p. 7 (4 Experiments) |
| Please refer to our appendices for more results (3D instance and panoptic segmentation, extension to versatile 3D editing, comparisons with more 3D-based baselines, real-world ... | comparison identity and matched condition | p. 9 (4 Experiments) |
| As demonstrated in Fig.5 (b), thanks to our simultaneous task modeling and Multi-View Mask Aggregation mechanism, our method can effectively leverage geometric clues to ... | comparison identity and matched condition | p. 9 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 6: Ablation on Multi-View Mask Aggregation (R→U). improve our performance in both 2D-only and 3D-aware scene understanding, without sacrificing 3D reconstruction accuracy due ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |
| Specifically, without reconstructed 3D structures, 2D-based methods can only perform segmentation on the input context views. | component/input/data sensitivity | p. 7 (4 Experiments) |
| However, as shown in Table 2, such early aggregation leads to poor performance without re-training our model. | component/input/data sensitivity | p. 9 (4 Experiments) |
| Remove Gaussians for a specified instance (ID = ins_id): G′ = G \ {gij v /M v,ij ins = ins_id} 3. | component/input/data sensitivity | p. 17 (A.3 Implementation Details about Versatile 3D Editing) |
| The modified Gaussians G′ are rendered into original context views to obtain images I′, with an off-the-shelf diffusion-based inpainting model [60] applied to fill ... | component/input/data sensitivity | p. 17 (A.3 Implementation Details about Versatile 3D Editing) |
| As shown in Fig.1 of main manuscript, our simultaneous modeling of scene understanding and 3D reconstruction enables diverse 3D scene manipulations through unified pixel-aligned ... | component/input/data sensitivity | p. 16 (A.3 Implementation Details about Versatile 3D Editing) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our method consists of Image and Text Encoders for extracting multi-view and text features, Gaussian Decoder for decoding pixel-aligned 3D Gaussians, Unified Query Decoder ... | We can see that this module can significantly w/ R→U w/o R→U RGB w/ R→U w/o R→U RGB ✓ ☓ ✓ ☓ Figure 6: ... | PDF body cue; verify exact table/figure and matched conditions | p. 9 (4 Experiments), p. 9 (4 Experiments), p. 8 (Figure/Table caption), p. 8 (4 Experiments), p. 7 (4 Experiments), p. 5 (Figure/Table caption) |
| Primary metric/result | As demonstrated in Fig.5 (b), thanks to our simultaneous task modeling and Multi-View Mask Aggregation mechanism, our method can effectively leverage geometric clues to ... | numeric claim only at cited anchor | p. 9 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 7 / 4 Experiments - extractive body cue:** We conduct training on 8 NVIDIA GeForce RTX 4090 GPUs, with our model trained for 100 epochs using a per-GPU batch size of 3 (total ...
- **p. 4 / 3 Methodology - extractive body cue:** Our method consists of Image and Text Encoders for extracting multi-view and text features, Gaussian Decoder for decoding pixel-aligned 3D Gaussians, Unified Query Decoder for ...
- **p. 4 / 3 Methodology - extractive body cue:** The network establishes two key outputs: 1) pixel-aligned multi-view 3D Gaussians G = {gij v }V,H,W v,i,j=1 for 3D reconstruction, where g = {µ, α, ...
- **p. 4 / 3 Methodology - extractive body cue:** This cross-/self-attention block is stacked L1 times to progressively consolidate semantic information across views, ultimately decoding them into multi-view mask logits M = {mij n,v}Nq,V,H,W ...
- **p. 6 / 3 Methodology - extractive body cue:** Thus, to make 3D Gaussians within the same mask to be more clustered, we propose Mask-Guided Geometry Refinement module, which utilizes masks as guidance to ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| no explicit failure cue selected | unreported; domain stress test remains open | verify Discussion/Conclusion |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We conduct training on 8 NVIDIA GeForce RTX 4090 GPUs, with our model trained for 100 epochs using a per-GPU batch size of 3 ... | p. 7 (4 Experiments) |
| AdamW optimizer[57] is employed with an initial learning rate of 1e-4 followed by cosine decay scheduling. | p. 7 (4 Experiments) |
| Here we take instance removal as an example to derive the implementation of such 3D editing: 1. | p. 16 (A.3 Implementation Details about Versatile 3D Editing) |
| Gaussian Decoder Unified Query Decoder (Sec. | p. 4 (3 Methodology) |
| We design our Image Encoder following [52]'s architecture as a Vision Transformer (ViT) enhanced with an adapter module. | p. 4 (3 Methodology) |
| In (a), we employ multi-view semantic-focused features fU, unified queries Q, and L1 stacked cross-/self-attention layer blocks to decode cross-view instance and semantic masks. | p. 5 (3 Methodology) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- explicit limitation/failure sentence not recovered

- **Evidence anchors reviewed:** datasets p. 15 (A.1 Data Preprocessing), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments), p. 8 (4 Experiments), metrics p. 7 (4 Experiments), p. 9 (4 Experiments), p. 8 (4 Experiments), p. 15 (A.1 Data Preprocessing), p. 15 (A.1 Data Preprocessing), p. 7 (4 Experiments), baselines p. 7 (4 Experiments), p. 8 (4 Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), results p. 9 (4 Experiments), p. 9 (4 Experiments), p. 8 (Figure/Table caption), p. 8 (4 Experiments), p. 7 (4 Experiments), p. 5 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
