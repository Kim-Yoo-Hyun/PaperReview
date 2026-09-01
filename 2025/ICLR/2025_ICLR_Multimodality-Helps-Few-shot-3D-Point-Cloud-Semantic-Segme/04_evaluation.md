# Evaluation - Multimodality Helps Few-shot 3D Point Cloud Semantic Segmentation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=jXvwJ51vcK; PDF retrieval source: https://openreview.net/pdf/8fd72e10cf4596642e77049c226ea9fd50cd5c23.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (Figure/Table caption), p. 8 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 2 (Figure/Table caption)): Figure 4: Qualitative comparison of predictions from each head and our final prediction using TACC (Default) in the 1-way 1-shot setting on the S3DIS dataset. The target classes in the ...

## Evaluation Body Digest

- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** (2021), we divide the large-scale scenes into 1m × 1m blocks.
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** ScanNet provides 2D RGB images of 3D scenes while S3DIS lacks.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** Similarly, it achieves +4.53% and +8.58% improvements on the S3DIS dataset in the 1/2-way settings, respectively.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** Overall, our model secures average mIoU improvements of +3.97% and +9.25% across the 1/2-way settings on both datasets.
- **p. 10 / 4 EXPERIMENTS - extractive PDF cue:** By default, We use 4 MSF blocks for the ScanNet dataset.
- **p. 18 / B ADDITIONAL IMPLEMENTATION DETAILS - extractive PDF cue:** (2024), input features from both datasets include XYZ coordinates and RGB colors.
- **p. 18 / B ADDITIONAL IMPLEMENTATION DETAILS - extractive PDF cue:** This allows us to directly employ pretrained weights from 2D-3D datasets for starting meta-learning on 3D-only datasets.
- **p. 17 / B ADDITIONAL IMPLEMENTATION DETAILS - extractive PDF cue:** Simultaneously training both heads might complicate and destabilize the optimization process due to significant heterogeneity across different modalities (Morency & Baltrušaitis, 2017; Lu et al., ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 EXPERIMENTS (p. 8); A ADDITIONAL EXPERIMENTS (p. 16); B ADDITIONAL IMPLEMENTATION DETAILS (p. 17).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SIMULATION | Figure 4: Qualitative comparison of predictions from each head and our final prediction using TACC (Default) in the 1-way 1-shot setting on the S3DIS ... | p. 9 (Figure/Table caption) |
| 4 EXPERIMENTS | EMPIRICAL / SIMULATION | Despite leveraging the 2D-aligned backbone weights, COSeg† does not significantly improve over COSeg, highlighting the critical role of well-designed fusion modules in achieving significant ... | p. 8 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SIMULATION | 3d shows that adding the image modality improves the 3D-only baseline, and further incorporating the textual modality leads to better results. | p. 10 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SIMULATION | Moreover, combining both MCF and MSF together further improves performance, confirming that their fusion strategies are both essential and complementary for enhancing few-shot learning. | p. 10 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SIMULATION | Overall, our model secures average mIoU improvements of +3.97% and +9.25% across the 1/2-way settings on both datasets. | p. 9 (4 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** (2021), we divide the large-scale scenes into 1m × 1m blocks.
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** ScanNet provides 2D RGB images of 3D scenes while S3DIS lacks.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** Similarly, it achieves +4.53% and +8.58% improvements on the S3DIS dataset in the 1/2-way settings, respectively.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** Overall, our model secures average mIoU improvements of +3.97% and +9.25% across the 1/2-way settings on both datasets.
- **p. 10 / 4 EXPERIMENTS - extractive PDF cue:** By default, We use 4 MSF blocks for the ScanNet dataset.
- **p. 18 / B ADDITIONAL IMPLEMENTATION DETAILS - extractive PDF cue:** (2024), input features from both datasets include XYZ coordinates and RGB colors.
- **p. 18 / B ADDITIONAL IMPLEMENTATION DETAILS - extractive PDF cue:** This allows us to directly employ pretrained weights from 2D-3D datasets for starting meta-learning on 3D-only datasets.
- **p. 17 / B ADDITIONAL IMPLEMENTATION DETAILS - extractive PDF cue:** Simultaneously training both heads might complicate and destabilize the optimization process due to significant heterogeneity across different modalities (Morency & Baltrušaitis, 2017; Lu et al., ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: Comparison between traditional unimodal FS-PCS and our proposed multimodal FS-PCS. Previous FS-PCS methods only make use of point clouds as unimodal input. In ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Overall architecture of the proposed MM-FSS. Given support and query point clouds, we first generate intermodal features Fi s/q from the IF head ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 1: Quantitative comparison with previous methods in mIoU (%) on the S3DIS dataset. There are four few-shot settings: 1/2-way 1/5-shot. S0/S1 refers to using ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2: Quantitative comparison with previous methods in mIoU (%) on the ScanNet dataset. where 1{x} is the indicator function that equals one if x ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 3: Ablation study. (a) Effect of fusion modules. (b) Effect of interactions between two feature heads. (c) Impact of the number of MSF layers. ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 3: Qualitative comparison between COSeg and our proposed MM-FSS in the 1-way 1-shot setting on the S3DIS dataset. The target classes in the first ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 4: Qualitative comparison of predictions from each head and our final prediction using TACC (Default) in the 1-way 1-shot setting on the S3DIS dataset. ...
- **p. 16 / Figure/Table caption - extractive PDF cue:** Table 4: Quantitative comparison with previous methods in terms of mIoU (%) on the ScanNet dataset. The last two rows represent the FS-PCS performance of ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | (2021), we divide the large-scale scenes into 1m × 1m blocks. | embodiment, simulator version and control stack | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Task/environment | ScanNet provides 2D RGB images of 3D scenes while S3DIS lacks. | reset, timeout, object/scene variation | p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 5 (3 METHODOLOGY), p. 1 (1 INTRODUCTION) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| This performance gap underscores our model's superior ability to utilize multimodal knowledge for FS-PCS and the importance of considering commonly-ignored multimodal information to enhance ... | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| The results demonstrate that increasing the number of MSF blocks enhances few-shot performance. | definition/direction/unit from same section | p. 10 (4 EXPERIMENTS) |
| Moreover, combining both MCF and MSF together further improves performance, confirming that their fusion strategies are both essential and complementary for enhancing few-shot learning. | definition/direction/unit from same section | p. 10 (4 EXPERIMENTS) |
| The learning rate is reduced to 0.0001 during the meta-learning phase. | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| For optimization, we use the AdamW optimizer, setting a weight decay of 0.01 and a learning rate of 0.006 during pretraining. | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| (d) Performance gains from each modality. | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| Hence, we adopt a two-step training strategy to mitigate potential performance issues. | definition/direction/unit from same section | p. 17 (B ADDITIONAL IMPLEMENTATION DETAILS) |
| Figure 2: Overall architecture of the proposed MM-FSS. Given support and query point clouds, we first generate intermodal features Fi s/q from the IF ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| In contrast, MM-FSS consistently outperforms the former state-of-the-art across all settings, demonstrating superior cross-modal knowledge integration to enhance novel class segmentation. | comparison identity and matched condition | p. 9 (4 EXPERIMENTS) |
| 4.2 COMPARISON WITH STATE-OF-THE-ART METHODS We compare MM-FSS with previous models on the S3DIS (Armeni et al., 2016) and ScanNet (Dai et al., 2017) ... | comparison identity and matched condition | p. 8 (4 EXPERIMENTS) |
| 3g presents a comparison of the FLOPs and parameter count between our model and the previous state-of-the-art method, COSeg (An et al., 2024). | comparison identity and matched condition | p. 10 (4 EXPERIMENTS) |
| Fixed coefficients (1:1 and 1:0.5) are unable to dynamically adjust calibration and only slightly improve over the baseline (0:1). | comparison identity and matched condition | p. 10 (4 EXPERIMENTS) |
| Figure 6: Visual comparison between COSeg (An et al., 2024) and our proposed MM-FSS on the S3DIS dataset. Each row represents one 1-way 1-shot ... | comparison identity and matched condition | p. 20 (Figure/Table caption) |
| Figure 1: Comparison between traditional unimodal FS-PCS and our proposed multimodal FS-PCS. Previous FS-PCS methods only make use of point clouds as unimodal input. ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 3: Ablation study. (a) Effect of fusion modules. (b) Effect of interactions between two feature heads. (c) Impact of the number of MSF ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |
| The two datasets allow us to demonstrate our model's effectiveness in exploiting multimodal data and its capability to excel in FS-PCS even without 2D ... | component/input/data sensitivity | p. 8 (4 EXPERIMENTS) |
| Figure 5: Visualization on the effects of weight Wq between textual and visual modalities in Eq. (7). The last column displays the heatmap of ... | component/input/data sensitivity | p. 16 (Figure/Table caption) |
| We also evaluate a variant of the previously leading method COSeg (An et al., 2024), denoted as COSeg†, retrained using the same 2D-aligned pretrained ... | component/input/data sensitivity | p. 8 (4 EXPERIMENTS) |
| 44.73 50.07 (b) K 1-shot 5-shot 3 43.33 45.97 4 42.83 48.04 5 44.69 48.36 (c) 3D Image Text 1-shot 5-shot ✓ 40.69 45.51 ... | component/input/data sensitivity | p. 9 (4 EXPERIMENTS) |
| Published as a conference paper at ICLR 2025 4.3 ABLATION STUDY In this section, unless stated otherwise, we report the mIoU results for both ... | component/input/data sensitivity | p. 10 (4 EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Under this cost-free multimodal FS-PCS setup, we introduce a novel model, MultiModal Few-Shot SegNet (MM-FSS), to effectively address FS-PCS by harnessing complementary information from ... | Figure 4: Qualitative comparison of predictions from each head and our final prediction using TACC (Default) in the 1-way 1-shot setting on the S3DIS ... | PDF body cue; verify exact table/figure and matched conditions | p. 9 (Figure/Table caption), p. 8 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 2 (Figure/Table caption) |
| Primary metric/result | Despite leveraging the 2D-aligned backbone weights, COSeg† does not significantly improve over COSeg, highlighting the critical role of well-designed fusion modules in achieving significant ... | numeric claim only at cited anchor | p. 8 (4 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** (2024), voxelizing raw input points within each block using a 0.02m grid size and uniformly sampling to maintain a maximum of 20,480 points per block.
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** The initial pretraining phase spans 100 epochs, while the subsequent meta-learning phase includes 40,000 episodes, following An et al.
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** (2024), the evaluation sets consist of 1,000 episodes per class in the 1-way setting and 100 episodes per class combination in the 2-way setting.
- **p. 18 / B ADDITIONAL IMPLEMENTATION DETAILS - extractive PDF cue:** Training and inference are conducted on four RTX 3090 GPUs.
- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** Each episode corresponds to an N-way K-shot segmentation task, containing a support set S =  {Xn,k s , Yn,k s }K k=1 N n=1 ...
- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** The goal of FS-PCS is to segment the query samples {Xn q}N n=1 into N target classes and ‘background' by leveraging the knowledge of the ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Using only Gq (1:0) yields the lowest performance due to the IF head's limitations in utilizing support samples for learning novel classes. | p. 10 (4 EXPERIMENTS) |
| body limitation/failure cue | Despite leveraging the 2D-aligned backbone weights, COSeg† does not significantly improve over COSeg, highlighting the critical role of well-designed fusion modules in achieving significant ... | p. 8 (4 EXPERIMENTS) |
| body limitation/failure cue | In the first step, we concentrate on training the IF head to learn robust 3D features aligned with 2D modality, providing a solid foundation ... | p. 17 (B ADDITIONAL IMPLEMENTATION DETAILS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The learning rate is reduced to 0.0001 during the meta-learning phase. | p. 8 (4 EXPERIMENTS) |
| For optimization, we use the AdamW optimizer, setting a weight decay of 0.01 and a learning rate of 0.006 during pretraining. | p. 8 (4 EXPERIMENTS) |
| The 2D features F2D ∈RH×W ×Dt aligned with text modality can be extracted using the pretrained image encoder in LSeg (Li et al., 2022) ... | p. 17 (B ADDITIONAL IMPLEMENTATION DETAILS) |
| We compute embeddings for the ‘background' and target classes using the LSeg (Li et al., 2022) text encoder, denoted as T = {t0, · ... | p. 5 (3 METHODOLOGY) |
| Beyond mining visual connections, we use the LSeg text encoder (Li et al., 2022) to generate text embeddings for class names. | p. 5 (3 METHODOLOGY) |
| Therefore, we first compute the similarity between the query intermodal features and text embeddings to generate semantic guidance Gq ∈RNQ×NC 6 | p. 6 (3 METHODOLOGY) |
| Using the support intermodal features Fi s and the text embeddings T, we compute Gs, which is then used to generate predicted labels Ps. | p. 7 (3 METHODOLOGY) |
| Note that it computes the relative importance between visual and textual modalities for all pairs of points and classes, improving the effective integration of ... | p. 7 (3 METHODOLOGY) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / 4 EXPERIMENTS - extractive PDF cue:** Using only Gq (1:0) yields the lowest performance due to the IF head's limitations in utilizing support samples for learning novel classes.
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** Despite leveraging the 2D-aligned backbone weights, COSeg† does not significantly improve over COSeg, highlighting the critical role of well-designed fusion modules in achieving significant advancements.
- **p. 17 / B ADDITIONAL IMPLEMENTATION DETAILS - extractive PDF cue:** In the first step, we concentrate on training the IF head to learn robust 3D features aligned with 2D modality, providing a solid foundation for ...

- **PDF anchors reviewed:** datasets p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 18 (B ADDITIONAL IMPLEMENTATION DETAILS), metrics p. 9 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), baselines p. 9 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 20 (Figure/Table caption), p. 2 (Figure/Table caption), results p. 9 (Figure/Table caption), p. 8 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 2 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
