# Evaluation - IGGT: Instance-Grounded Geometry Transformer for Semantic 3D Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=swiL18PmUV; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/248038. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 20 (A.8 CLASS-AGNOSTIC SEGMENTATION EXPERIMENTS), p. 9 (8.83 AP while avoiding its expensive mesh gen), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS)): Our method significantly outperforms graph-based grouping approaches such as VGGT+Graph Cut across all metrics, achieving an 8.83 improvement in AP.

## Evaluation Body Digest

- **p. 9 / 8.83 AP while avoiding its expensive mesh gen - extractive body cue:** We evaluate our model on various OOD scenarios: outdoor scenes (ETH3D (Schops et al., 2017)), autonomous driving scenes (Waymo Open Dataset (Sun et al., 2020)), ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** From each dataset, we randomly select 10 scenes and sample 8-10 images per scene, with the selection strategy designed to maximize spatial coverage of the ...
- **p. 17 / A.6 ADDITION INFORMATION OF OUR INSSCENE-15K DATASET - extractive body cue:** While web-captured datasets such as RE10K (Zhou et al., 2018) offer a large number of scenes (i.e., high diversity), they lack depth and 3D-consistent instance ...
- **p. 17 / A.6 ADDITION INFORMATION OF OUR INSSCENE-15K DATASET - extractive body cue:** As for our InsScene-15K dataset, we build upon our own annotation pipeline to re-annotate ScanNet++ and RE10K with instance masks, ensuring that our dataset provides ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** To comprehensively evaluate the tracking quality of our proposed method and competing approaches, particularly under large viewpoint changes with multiple objects, we manually annotate a ...
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** We compare our method with other Image-to-3D feedforward method (Fan et al., 2024), per-scene optimized methods (Zhou et al., 2024; Kobayashi et al., 2022), and ...
- **p. 9 / 8.83 AP while avoiding its expensive mesh gen - extractive body cue:** 10 show that our method can reconstruct scenes and produce 3D-consistent instance clustering on these unseen domains, demonstrating strong generalization ability.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Following recent 3D instance segmentation works (Yin et al., 2024; Yang et al., 2024; Huang et al., 2024c), we provide a class-agnostic instance segmentation evaluation ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 EXPERIMENTS (p. 7); A.6 ADDITION INFORMATION OF OUR INSSCENE-15K DATASET (p. 17); A.8 CLASS-AGNOSTIC SEGMENTATION EXPERIMENTS (p. 20); A.12 OUT-OF-DISTRIBUTION (OOD) RESULTS (p. 24).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| A.8 CLASS-AGNOSTIC SEGMENTATION EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our method significantly outperforms graph-based grouping approaches such as VGGT+Graph Cut across all metrics, achieving an 8.83 improvement in AP. | p. 20 (A.8 CLASS-AGNOSTIC SEGMENTATION EXPERIMENTS) |
| 8.83 AP while avoiding its expensive mesh gen | EMPIRICAL / SOURCE-REPORTED EVALUATION | This further demonstrates the flexibility of our method in using different VLMs to achieve improved text query performance. | p. 9 (8.83 AP while avoiding its expensive mesh gen) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | By leveraging implicit 3D reasoning, our approach successfully distinguishes object identities to achieve nearly 100% TSR accuracy. | p. 7 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | (a) For MultiView Instance Matching evaluation, we evaluate tracking performance using Temporal mIoU (TmIoU) and Temporal Success Rate (T-SR). | p. 7 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | This performance improvement is further demonstrated in 3D segmentation (see Tab. | p. 8 (4 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 9 / 8.83 AP while avoiding its expensive mesh gen - extractive body cue:** We evaluate our model on various OOD scenarios: outdoor scenes (ETH3D (Schops et al., 2017)), autonomous driving scenes (Waymo Open Dataset (Sun et al., 2020)), ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** From each dataset, we randomly select 10 scenes and sample 8-10 images per scene, with the selection strategy designed to maximize spatial coverage of the ...
- **p. 17 / A.6 ADDITION INFORMATION OF OUR INSSCENE-15K DATASET - extractive body cue:** While web-captured datasets such as RE10K (Zhou et al., 2018) offer a large number of scenes (i.e., high diversity), they lack depth and 3D-consistent instance ...
- **p. 17 / A.6 ADDITION INFORMATION OF OUR INSSCENE-15K DATASET - extractive body cue:** As for our InsScene-15K dataset, we build upon our own annotation pipeline to re-annotate ScanNet++ and RE10K with instance masks, ensuring that our dataset provides ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** To comprehensively evaluate the tracking quality of our proposed method and competing approaches, particularly under large viewpoint changes with multiple objects, we manually annotate a ...
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** We compare our method with other Image-to-3D feedforward method (Fan et al., 2024), per-scene optimized methods (Zhou et al., 2024; Kobayashi et al., 2022), and ...
- **p. 9 / 8.83 AP while avoiding its expensive mesh gen - extractive body cue:** 10 show that our method can reconstruct scenes and produce 3D-consistent instance clustering on these unseen domains, demonstrating strong generalization ability.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Following recent 3D instance segmentation works (Yin et al., 2024; Yang et al., 2024; Huang et al., 2024c), we provide a class-agnostic instance segmentation evaluation ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: IGGT: building upon our curated large-scale dataset InsScene-15K, we propose a novel end-to-end framework that enables geometric reconstruction and contextual understanding in a ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Data Curation Pipeline. Our data is collected from various sources and then annotated by a novel data engine driven by SAM2 (Ravi et ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3: Visualization of mask annotations from three different sources. For the RGBD-scan scene, we additionally compare the vanilla ground-truth masks from ScanNet++ (Yeshwanth et ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4: Overview of IGGT. Given input images, our method encodes them into a series of Unified Token Representations, which are then processed by the ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1: Quantitative Results on ScanNet (Dai et al., 2017). Here we showcase the capability overview and report the performance of multi-view instance matching (MV ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2: Quantitative Results on ScanNet++ (Yeshwanth et al., 2023). Here we report the multi- view instance matching quality, reconstruction accuracy, and 2D / 3D ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: Qualitative results on multi-view instance matching. We present two example scenes from ScanNet (Dai et al., 2017) and ScanNet++ (Yeshwanth et al., 2023), ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 6: We visualize our 3D-consistent PCA results with corresponding clustered masks derived from instance-grounded features. Similar colors in PCA indicate higher feature similarity between ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We evaluate our model on various OOD scenarios: outdoor scenes (ETH3D (Schops et al., 2017)), autonomous driving scenes (Waymo Open Dataset (Sun et al., ... | embodiment, simulator version and control stack | p. 9 (8.83 AP while avoiding its expensive mesh gen), p. 7 (4 EXPERIMENTS) |
| Task/environment | From each dataset, we randomly select 10 scenes and sample 8-10 images per scene, with the selection strategy designed to maximize spatial coverage of ... | reset, timeout, object/scene variation | p. 7 (4 EXPERIMENTS), p. 17 (A.6 ADDITION INFORMATION OF OUR INSSCENE-15K DATASET) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 5 (3 METHODOLOGY), p. 2 (1 INTRODUCTION) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (3 METHODOLOGY), p. 4 (3 METHODOLOGY) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| (a) For MultiView Instance Matching evaluation, we evaluate tracking performance using Temporal mIoU (TmIoU) and Temporal Success Rate (T-SR). | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |
| We report the average precision scores at IoU thresholds of 0.25 (AP25) and 0.50 (AP50), as well as averaged over IoU thresholds from 0.50 ... | definition/direction/unit from same section | p. 20 (A.8 CLASS-AGNOSTIC SEGMENTATION EXPERIMENTS) |
| This performance improvement is attributed to our method's superior multi-view consistency, which helps correct object recognition errors caused by incomplete views, as illustrated in ... | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| Figure 19: Visualization on clustered masks with different granularities. A.11 ADDITIONAL VISUALIZATION ON 3D VQA As shown in Fig. 20, we showcase two tasks, ... | definition/direction/unit from same section | p. 23 (Figure/Table caption) |
| By leveraging implicit 3D reasoning, our approach successfully distinguishes object identities to achieve nearly 100% TSR accuracy. | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |
| On the other hand, we also evaluate the accuracy of depth estimation on multi-view inputs. | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| In contrast, feed-forward methods such as LSM (Multi-View) achieve faster processing but suffer from limited reconstruction accuracy and are unable to support tasks like ... | definition/direction/unit from same section | p. 9 (8.83 AP while avoiding its expensive mesh gen) |
| As shown in the table, LSeg and OpenSeg, with better global context representation, achieve higher accuracy on background classes (e.g., cabinet), while CLIP, with ... | definition/direction/unit from same section | p. 9 (8.83 AP while avoiding its expensive mesh gen) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 9: Visualization of the Class-Agnostic 3D Mask Segmentation Results. Applications of QA Scene Grounding. We present the QA application results in Fig. 11 ... | comparison identity and matched condition | p. 9 (Figure/Table caption) |
| In contrast, baseline methods fail at this crucial task, yielding a T-mIoU below 30%, whereas our approach surpasses 60%. | comparison identity and matched condition | p. 7 (4 EXPERIMENTS) |
| For baseline methods, we modify SAM2 (Ravi et al., 2024) to support dense segmentation and tracking under multi-view inputs, denoted as SAM2*. | comparison identity and matched condition | p. 7 (4 EXPERIMENTS) |
| 2), where our method outperforms previous approaches by 4.31% and 4.97% in terms of 3D mIoU. | comparison identity and matched condition | p. 8 (4 EXPERIMENTS) |
| The results show that our method is on par with VGGT on ScanNet, and outperforms VGGT on ScanNet++ by 0.14 in Abs. | comparison identity and matched condition | p. 8 (4 EXPERIMENTS) |
| Compared with NeRF/3D-GS or other per-scene optimization methods, our approach substantially reduces reconstruction time. | comparison identity and matched condition | p. 9 (8.83 AP while avoiding its expensive mesh gen) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 19: Visualization on clustered masks with different granularities. A.11 ADDITIONAL VISUALIZATION ON 3D VQA As shown in Fig. 20, we showcase two tasks, ... | component/input/data sensitivity | p. 23 (Figure/Table caption) |
| We also conduct ablations on integrating different VLMs into our method (e.g., LSeg (Li et al., 2022), CLIP (Radford et al., 2021), OpenSeg (Ghiasi ... | component/input/data sensitivity | p. 9 (8.83 AP while avoiding its expensive mesh gen) |
| Without the cross-modal fusion model, the instance head struggles to capture high-resolution geometric information, leading to more difficult convergence, as reflected in the sharpness ... | component/input/data sensitivity | p. 9 (8.83 AP while avoiding its expensive mesh gen) |
| Images "Ottolegnghi" LSM Ours w/ LSeg Ours w/ CLIP "Cabinet" Ours w/OpenSeg "DALL-E" Figure 12: Visualization of our method using different VLMs. w/ Multi-Modal ... | component/input/data sensitivity | p. 10 (8.83 AP while avoiding its expensive mesh gen) |
| Table 6: Comparison of Different Datasets. Here, we evaluate these datasets along five dimen- sions: RGB images, camera poses, depth, instance masks, and diversity. ... | component/input/data sensitivity | p. 19 (Figure/Table caption) |
| Table 7: Ablation study with different values of λ of contrastive supervision. Metrics λ 0.1 0.5 1 2 10 | component/input/data sensitivity | p. 20 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| 3.1 OVERVIEW Our method consists of two main phases. | Our method significantly outperforms graph-based grouping approaches such as VGGT+Graph Cut across all metrics, achieving an 8.83 improvement in AP. | PDF body cue; verify exact table/figure and matched conditions | p. 20 (A.8 CLASS-AGNOSTIC SEGMENTATION EXPERIMENTS), p. 9 (8.83 AP while avoiding its expensive mesh gen), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Primary metric/result | This further demonstrates the flexibility of our method in using different VLMs to achieve improved text query performance. | numeric claim only at cited anchor | p. 9 (8.83 AP while avoiding its expensive mesh gen) |

- Numeric sentences retained from the body:
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** From each dataset, we randomly select 10 scenes and sample 8-10 images per scene, with the selection strategy designed to maximize spatial coverage of the ...
- **p. 9 / 8.83 AP while avoiding its expensive mesh gen - extractive body cue:** Time Final Time NeRF-DFF 50.33s 3min - - 3.84min Feature-3DGS 50.33s 47min - - 47.84min LSM (Multi-Views) - - 15.98s 13.72s 29.70s VGGT+Graph Cut - ...
- **p. 17 / A.6 ADDITION INFORMATION OF OUR INSSCENE-15K DATASET - extractive body cue:** 17) and contain only around 1,000 scenes.
- **p. 17 / A.6 ADDITION INFORMATION OF OUR INSSCENE-15K DATASET - extractive body cue:** As for our InsScene-15K dataset, we build upon our own annotation pipeline to re-annotate ScanNet++ and RE10K with instance masks, ensuring that our dataset provides ...
- **p. 5 / 3 METHODOLOGY - extractive body cue:** (3) After that, we concatenate all refined instance features { ˆF ins i,(l)} and map them through a conventional 3 × 3 convolutional layer to ...
- **p. 5 / 3 METHODOLOGY - extractive body cue:** We enforce 3D consistency on the instance features Oins ∈RN×8×H×W by applying a multi-view contrastive loss Lmvc, which is designed to pull features from the ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | As a result, the accuracy of object boundaries in the clustered masks cannot yet rival that of state-of-the-art segmentation models (e.g., SAM2 (Ravi et ... | p. 24 (A.13 LIMITATION) |
| body limitation/failure cue | Figure 16: We visualize the RGB and semantic 3D points of the ground truth, IGGT(Ours), LSM(Multi-Views), and Feature-3DGS. supervision fails to provide sufficiently discriminative ... | p. 19 (Figure/Table caption) |
| body limitation/failure cue | Future work may integrate stronger DETR-based (Cheng et al., 2022) instance heads and larger annotated datasets to improve segmentation accuracy. | p. 24 (A.13 LIMITATION) |
| body limitation/failure cue | In contrast, baseline methods fail at this crucial task, yielding a T-mIoU below 30%, whereas our approach surpasses 60%. | p. 7 (4 EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The learning rate is set to 1 × 10-6 for the large unified Transformer backbone and 1 × 10-5 for both the geometry and ... | p. 17 (A.4 TRAINING DETAILS) |
| eration, reducing runtime by about 8 minutes. | p. 8 (8.83 AP while avoiding its expensive mesh gen) |
| Here, we use 10 images from a single scene to evaluate the detailed runtime, as reported in Tab. | p. 9 (8.83 AP while avoiding its expensive mesh gen) |
| For VGGT + Graph Cut, we first use VGGT to reconstruct the entire scene as a point cloud from the input images, then compute ... | p. 20 (A.8 CLASS-AGNOSTIC SEGMENTATION EXPERIMENTS) |
| Moreover, our method even approaches the performance of the per-scene optimization method VGGT+SAI3D, while achieving nearly a 5× reduction in runtime (2.5 min v.s. | p. 21 (A.8 CLASS-AGNOSTIC SEGMENTATION EXPERIMENTS) |
| Meanwhile, since this graph cut algorithm requires a mesh as input, a substantial amount of time is spent on mesh generation, whereas our approach ... | p. 21 (A.8 CLASS-AGNOSTIC SEGMENTATION EXPERIMENTS) |
| We employ two downstream branches-Geometry Head and Instance Head-to decode the unified tokens Ti} into geometric and instance features, respectively. | p. 4 (3 METHODOLOGY) |
| We follow VGGT to construct a 1B parameter large unified Transformer, designed to encode the multi-view images {Ii}N i=1 into a set of powerful ... | p. 4 (3 METHODOLOGY) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 24 / A.13 LIMITATION - extractive body cue:** As a result, the accuracy of object boundaries in the clustered masks cannot yet rival that of state-of-the-art segmentation models (e.g., SAM2 (Ravi et al., ...
- **p. 19 / Figure/Table caption - extractive body cue:** Figure 16: We visualize the RGB and semantic 3D points of the ground truth, IGGT(Ours), LSM(Multi-Views), and Feature-3DGS. supervision fails to provide sufficiently discriminative instance ...
- **p. 24 / A.13 LIMITATION - extractive body cue:** Future work may integrate stronger DETR-based (Cheng et al., 2022) instance heads and larger annotated datasets to improve segmentation accuracy.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** In contrast, baseline methods fail at this crucial task, yielding a T-mIoU below 30%, whereas our approach surpasses 60%.

- **Evidence anchors reviewed:** datasets p. 9 (8.83 AP while avoiding its expensive mesh gen), p. 7 (4 EXPERIMENTS), p. 17 (A.6 ADDITION INFORMATION OF OUR INSSCENE-15K DATASET), p. 17 (A.6 ADDITION INFORMATION OF OUR INSSCENE-15K DATASET), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), metrics p. 7 (4 EXPERIMENTS), p. 20 (A.8 CLASS-AGNOSTIC SEGMENTATION EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 23 (Figure/Table caption), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), baselines p. 9 (Figure/Table caption), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (8.83 AP while avoiding its expensive mesh gen), results p. 20 (A.8 CLASS-AGNOSTIC SEGMENTATION EXPERIMENTS), p. 9 (8.83 AP while avoiding its expensive mesh gen), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
