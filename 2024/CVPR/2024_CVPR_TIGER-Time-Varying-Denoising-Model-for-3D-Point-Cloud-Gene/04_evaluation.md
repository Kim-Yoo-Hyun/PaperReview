# Evaluation - TIGER: Time-Varying Denoising Model for 3D Point Cloud Generation with Diffusion Process

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Ren_TIGER_Time-Varying_Denoising_Model_for_3D_Point_Cloud_Generation_with_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Ren_TIGER_Time-Varying_Denoising_Model_for_3D_Point_Cloud_Generation_with_CVPR_2024_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.3. Ablation and Analysis), p. 6 (4.2. Comparison with SoTA methods), p. 6 (4.2. Comparison with SoTA methods), p. 7 (4.3. Ablation and Analysis), p. 3 (Figure/Table caption)): Furthermore, our proposed position encoding methods, PSPE and BλPE, significantly improve performance compared to no position encoding or learnable position encoding.

## Evaluation Body Digest

- **p. 6 / 4.2. Comparison with SoTA methods - extractive PDF cue:** It is noteworthy that in order to compare with LION, which uses a different dataset splitting strategy (sampling from the first 10, 000 points instead ...
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** For each shape, we sample 2, 048 points and normalize them globally across the entire dataset.
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** This metric has been shown to effectively measure both the quality and diversity of generated point clouds and a score closer to 50% indicates superior ...
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** Following the baselines PVD [55] and LION [53], we use 1-NN (1-nearest neighbor) accuracy [32] as our evaluation metric.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Ablation of different architecture designs. W1 and W2 are the weights for the ConvNet branch and Transformer branch. [Key: Best, Second Best] 1-NN ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 5. The overview of the position-aware self-attention. We compute position relationship map H by previous position embed- ding to reweigh the QKT matrix. where ...
- **p. 7 / 4.3. Ablation and Analysis - extractive PDF cue:** Transformer backbones, position encoding, and selfattention strategies.
- **p. 8 / 4.3. Ablation and Analysis - extractive PDF cue:** To further demonstrate the generalizability of our model, we train a universal TIGER model on all 55 categories of ShapeNetv2 [6].

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** high-dimensional data 또는 robot action-trajectory distribution.
- **Input boundary:** conditioning observation와 noisy/intermediate sample.
- **Output/decision under evaluation:** generated sample, action chunk 또는 trajectory.
- **Primary target:** distribution fit, multimodality, sample quality와 latency.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.1. Experimental Setup (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.3. Ablation and Analysis | SYSTEM / EVALUATION SCOPE UNRESOLVED | Furthermore, our proposed position encoding methods, PSPE and BλPE, significantly improve performance compared to no position encoding or learnable position encoding. | p. 7 (4.3. Ablation and Analysis) |
| 4.2. Comparison with SoTA methods | SYSTEM / EVALUATION SCOPE UNRESOLVED | 1, we outperform LION in four out of six metrics. | p. 6 (4.2. Comparison with SoTA methods) |
| 4.2. Comparison with SoTA methods | SYSTEM / EVALUATION SCOPE UNRESOLVED | Compared to other methods, our performance is significantly better. | p. 6 (4.2. Comparison with SoTA methods) |
| 4.3. Ablation and Analysis | SYSTEM / EVALUATION SCOPE UNRESOLVED | Further, channel-wise time masking improves performance slightly more than scale value setting due to its greater expressivity. | p. 7 (4.3. Ablation and Analysis) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 2. Illustration of our time-varying two-stream architecture (TIGER). The network's input is a noisy point cloud Xt at timestep t, and the goal ... | p. 3 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 4.2. Comparison with SoTA methods - extractive PDF cue:** It is noteworthy that in order to compare with LION, which uses a different dataset splitting strategy (sampling from the first 10, 000 points instead ...
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** For each shape, we sample 2, 048 points and normalize them globally across the entire dataset.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. An illustration of different roles played by convolution and attention operations in the denoising model. Convolution is good for learning local relationships, and ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Illustration of our time-varying two-stream architecture (TIGER). The network's input is a noisy point cloud Xt at timestep t, and the goal is ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. The overview of our encoder. It extracts features in voxel space and downsamples the point cloud by applying trilinear interpolation of voxel with ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 4. Illustration of two examples of the position embedding from PSPE and BλPE respectively. Both methods show distin- guished representation for each position. Following ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 5. The overview of the position-aware self-attention. We compute position relationship map H by previous position embed- ding to reweigh the QKT matrix. where ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 6. The overview of our decoder. By querying the latent volume ˆXF with previous coordinates information Xt, we can upsample the latent point cloud ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Quantitative comparison with baselines using 1-NN. Both CD and EMD are considered, where CD is multiplied by 103 and EMD is multiplied by ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 7. Our generation results (right) compared to baseline models (left). TIGER generates high-quality and diverse 3D point clouds. where WD×3 is the projection matrix ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | It is noteworthy that in order to compare with LION, which uses a different dataset splitting strategy (sampling from the first 10, 000 points ... | embodiment, simulator version and control stack | p. 6 (4.2. Comparison with SoTA methods), p. 6 (4.1. Experimental Setup) |
| Task/environment | For each shape, we sample 2, 048 points and normalize them globally across the entire dataset. | reset, timeout, object/scene variation | p. 6 (4.1. Experimental Setup) |
| Observation/sensor | conditioning observation와 noisy/intermediate sample | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 4 (3.2. Noisy Point Cloud Encoder) |
| Output/decision | generated sample, action chunk 또는 trajectory | action frame, controller and termination | p. 1 (1. Introduction), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| This metric has been shown to effectively measure both the quality and diversity of generated point clouds and a score closer to 50% indicates ... | definition/direction/unit from same section | p. 6 (4.1. Experimental Setup) |
| Following the baselines PVD [55] and LION [53], we use 1-NN (1-nearest neighbor) accuracy [32] as our evaluation metric. | definition/direction/unit from same section | p. 6 (4.1. Experimental Setup) |
| Table 3. Ablation of different architecture designs. W1 and W2 are the weights for the ConvNet branch and Transformer branch. [Key: Best, Second Best] ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 5. The overview of the position-aware self-attention. We compute position relationship map H by previous position embed- ding to reweigh the QKT matrix. ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Transformer backbones, position encoding, and selfattention strategies. | definition/direction/unit from same section | p. 7 (4.3. Ablation and Analysis) |
| To further demonstrate the generalizability of our model, we train a universal TIGER model on all 55 categories of ShapeNetv2 [6]. | definition/direction/unit from same section | p. 8 (4.3. Ablation and Analysis) |
| High quality and diverse 3D point clouds generated from our TIGER model trained on 55 ShapeNetv2 categories. long-range relationships in the data. | definition/direction/unit from same section | p. 8 (4.3. Ablation and Analysis) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 7. Our generation results (right) compared to baseline models (left). TIGER generates high-quality and diverse 3D point clouds. where WD×3 is the projection ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| 1, we outperform LION in four out of six metrics. | comparison identity and matched condition | p. 6 (4.2. Comparison with SoTA methods) |
| Figure 8. Visualization of attention maps in 3D point clouds. Col- umn (c) is the result of column (b) multiplied by position relation- ship ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| 4, our latent point cloud Transformer outperforms both PCT and Point Transformer under various settings. | comparison identity and matched condition | p. 7 (4.3. Ablation and Analysis) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Ablation of Transformer backbones, position encoding, and self-attention strategies. | component/input/data sensitivity | p. 7 (4.3. Ablation and Analysis) |
| In this ablation, we also compare the performance of our time masking with scalar value setting and channel-wise value setting. | component/input/data sensitivity | p. 7 (4.3. Ablation and Analysis) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our main contributions include: • We propose a novel two-stream denoising model, which uses timestep to optimally reweigh the global feature from Transformer and ... | Furthermore, our proposed position encoding methods, PSPE and BλPE, significantly improve performance compared to no position encoding or learnable position encoding. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.3. Ablation and Analysis), p. 6 (4.2. Comparison with SoTA methods), p. 6 (4.2. Comparison with SoTA methods), p. 7 (4.3. Ablation and Analysis), p. 3 (Figure/Table caption) |
| Primary metric/result | 1, we outperform LION in four out of six metrics. | numeric claim only at cited anchor | p. 6 (4.2. Comparison with SoTA methods) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** For each shape, we sample 2, 048 points and normalize them globally across the entire dataset.
- **p. 6 / 4.2. Comparison with SoTA methods - extractive PDF cue:** It is noteworthy that in order to compare with LION, which uses a different dataset splitting strategy (sampling from the first 10, 000 points instead ...
- **p. 3 / 3.2. Noisy Point Cloud Encoder - extractive PDF cue:** To effectively represent the N ×3 points, we adopt the voxelization encoding scheme of PVCNN [30].
- **p. 4 / 3.2. Noisy Point Cloud Encoder - extractive PDF cue:** Specifically, Vu,v,w = PN n=1 I(xn ∈N(u, δ), yn ∈N(v, δ), zn ∈N(w, δ)) ∗fn, (4) where N(z, δ) = {x/x ∈[z -δ, z + ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Although we generate high-quality and natural samples, we cannot control the category of the generated shape. | p. 8 (5. Conclusions) |
| body limitation/failure cue | But future works can increase the backbone efficiency by proposing time-varying properties with only one network. | p. 8 (5. Conclusions) |
| body limitation/failure cue | Figure 2. Illustration of our time-varying two-stream architecture (TIGER). The network's input is a noisy point cloud Xt at timestep t, and the goal ... | p. 3 (Figure/Table caption) |
| body limitation/failure cue | Figure 7. Our generation results (right) compared to baseline models (left). TIGER generates high-quality and diverse 3D point clouds. where WD×3 is the projection ... | p. 6 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Training Time (GPU hours) Inference Time (s) PVD [55] 142 8.46 LION [53] 550 27.12 Tiger 164 9.73 Table 2. | p. 7 (Method) |
| 2, our model trains much faster than LION, with only a quarter of its training time and a third of its inference time. | p. 7 (Method) |
| Then, we dive into the details of our time-varying two-stream architecture, including the encoder part, latent point Transformer, time mask generator, and decoder part. | p. 3 (3. Method) |
| The overview of our encoder is illustrated in Fig. | p. 4 (3.2. Noisy Point Cloud Encoder) |
| It is worth noting we preserve the coordinates of Xt and Xs t to do upsampling with the decoder and provide position embedding for ... | p. 4 (3.2. Noisy Point Cloud Encoder) |
| (16) Then we encode a timestep t to a sinusoidal position embedding [18, 48] to temb ∈Rc. | p. 5 (3.4. Time Mask Generator) |
| We compute position relationship map H by previous position embedding to reweigh the QKT matrix. where pos is a polynomial expression of λ. | p. 5 (3.3. Latent Point Cloud Transformer) |
| The overview of our decoder is shown in Fig. | p. 6 (Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusions - extractive PDF cue:** Although we generate high-quality and natural samples, we cannot control the category of the generated shape.
- **p. 8 / 5. Conclusions - extractive PDF cue:** But future works can increase the backbone efficiency by proposing time-varying properties with only one network.
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Illustration of our time-varying two-stream architecture (TIGER). The network's input is a noisy point cloud Xt at timestep t, and the goal is ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 7. Our generation results (right) compared to baseline models (left). TIGER generates high-quality and diverse 3D point clouds. where WD×3 is the projection matrix ...

- **PDF anchors reviewed:** datasets p. 6 (4.2. Comparison with SoTA methods), p. 6 (4.1. Experimental Setup), metrics p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 7 (Figure/Table caption), p. 5 (Figure/Table caption), p. 7 (4.3. Ablation and Analysis), p. 8 (4.3. Ablation and Analysis), baselines p. 6 (Figure/Table caption), p. 6 (4.2. Comparison with SoTA methods), p. 7 (Figure/Table caption), p. 7 (4.3. Ablation and Analysis), results p. 7 (4.3. Ablation and Analysis), p. 6 (4.2. Comparison with SoTA methods), p. 6 (4.2. Comparison with SoTA methods), p. 7 (4.3. Ablation and Analysis), p. 3 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
