# Evaluation - Geometry Forcing: Marrying Video Diffusion and 3D Representation for Consistent World Modeling

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=ULXYZCms41; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/247965. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 20 (C.4 METRICS), p. 19 (C.4 METRICS), p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS)): Experimental results demonstrate that our approach achieves improvements across multiple evaluation dimensions, including visual aesthetics, motion smoothness, and motion quality, as detailed in Table 11.

## Evaluation Body Digest

- **p. 6 / 5 EXPERIMENTS - extractive body cue:** In this section, we evaluate Geometry Forcing (GF) on camera-view-conditioned video generation on the RealEstate10K (Zhou et al., 2018) dataset and action-conditioned video generation on ...
- **p. 18 / C.1 DATASET - extractive body cue:** This game dataset includes action annotations, enabling evaluation of video generation in dynamic environments with camera motion.
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** 2 presents qualitative comparisons on the RealEstate10K dataset.
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** We conduct a comprehensive evaluation of GF on the RealEstate10K (Zhou et al., 2018) dataset, comparing against state-of-the-art baselines.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** To validate the effectiveness of geometric representation, we compare two target representations in GF: VGGT (Wang et al., 2025b), trained on 3D datasets with strong ...
- **p. 18 / C.1 DATASET - extractive body cue:** This dataset contains camera poses for 10 million video frames, suitable for evaluating 3D consistency and camera navigation in generated videos.
- **p. 24 / C.4 METRICS - extractive body cue:** In particular, GF better preserves object shapes and scene layouts that are visible in context, while generating reasonable scenes not seen in the context.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** Average scores on Camera Following, Object Consistency, and Scene Continuity.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** high-dimensional data 또는 robot action-trajectory distribution.
- **Input boundary:** conditioning observation와 noisy/intermediate sample.
- **Output/decision under evaluation:** generated sample, action chunk 또는 trajectory.
- **Primary target:** distribution fit, multimodality, sample quality와 latency.
- **Detected evaluation headings:** 5 EXPERIMENTS (p. 6); C.1 Dataset (p. 17); C IMPLEMENTATION DETAILS (p. 18); C.1 DATASET (p. 18).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| C.4 METRICS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Experimental results demonstrate that our approach achieves improvements across multiple evaluation dimensions, including visual aesthetics, motion smoothness, and motion quality, as detailed in Table ... | p. 20 (C.4 METRICS) |
| C.4 METRICS | EMPIRICAL / SOURCE-REPORTED EVALUATION | We conduct Geometry Forcing algorithm on Pi3 model and also achieves significant improvement on video generation as shown in Tab. | p. 19 (C.4 METRICS) |
| 5 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | 5, the model achieves a lower FVD score, indicating that GF can be seamlessly integrated into video diffusion models and yields measurable gains. | p. 7 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | FVD results of NFD before and after applying Geometry Forcing (GF) on 16-Frame generation show clear improvement. | p. 8 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | 3, the combination of Angular Alignment and Scale Alignment achieves the best performance, indicating the benefit of aligning both angular and scale-related information. | p. 8 (5 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 6 / 5 EXPERIMENTS - extractive body cue:** In this section, we evaluate Geometry Forcing (GF) on camera-view-conditioned video generation on the RealEstate10K (Zhou et al., 2018) dataset and action-conditioned video generation on ...
- **p. 18 / C.1 DATASET - extractive body cue:** This game dataset includes action annotations, enabling evaluation of video generation in dynamic environments with camera motion.
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** 2 presents qualitative comparisons on the RealEstate10K dataset.
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** We conduct a comprehensive evaluation of GF on the RealEstate10K (Zhou et al., 2018) dataset, comparing against state-of-the-art baselines.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** To validate the effectiveness of geometric representation, we compare two target representations in GF: VGGT (Wang et al., 2025b), trained on 3D datasets with strong ...
- **p. 18 / C.1 DATASET - extractive body cue:** This dataset contains camera poses for 10 million video frames, suitable for evaluating 3D consistency and camera navigation in generated videos.
- **p. 24 / C.4 METRICS - extractive body cue:** In particular, GF better preserves object shapes and scene layouts that are visible in context, while generating reasonable scenes not seen in the context.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** Average scores on Camera Following, Object Consistency, and Scene Continuity.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Geometry Forcing equips video diffusion models with 3D awareness. (a) We pro- pose Geometry Forcing (GF), a simple yet effective paradigm to internalize ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1: Quantitative comparison on the RealEstate10K dataset for both short-term (16-Frame) and long-term (256-Frame) video generation. Geometry Forcing substantially improves over the baseline. bold ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 2: Qualitative comparison of camera view-conditioned video generation under full- circle rotation. Videos are generated from a single frame, and per-frame camera poses simulate ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: Ablation study on target represen- tation. We compare the effect of aligning the diffusion model with different target representa- tions: DINOv2 (semantic), VGGT ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3: Ablation study on alignment loss. Angular and Scale Alignment losses are evalu- ated for long-term video generation, with MSE as a naive baseline ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4: Ablation study on explicit and im- plicit geometry information. We compare the explicit geometry condition with internal align- ment (ours).
- **p. 8 / Figure/Table caption - extractive body cue:** Table 5: Evaluation on action-conditioned video generation in Minecraft. FVD results of NFD before and after applying Geometry Forc- ing (GF) on 16-Frame generation show ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 3: Ablation study on alignment depth. We present FVD-256 and FVD-16 re- sults for different alignment layers of the dif- fusion model, which suggest ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | In this section, we evaluate Geometry Forcing (GF) on camera-view-conditioned video generation on the RealEstate10K (Zhou et al., 2018) dataset and action-conditioned video generation ... | embodiment, simulator version and control stack | p. 6 (5 EXPERIMENTS), p. 18 (C.1 DATASET) |
| Task/environment | This game dataset includes action annotations, enabling evaluation of video generation in dynamic environments with camera motion. | reset, timeout, object/scene variation | p. 18 (C.1 DATASET), p. 7 (5 EXPERIMENTS) |
| Observation/sensor | conditioning observation와 noisy/intermediate sample | calibration, preprocessing, privileged input | p. 2 (1 INTRODUCTION), p. 21 (C.4 METRICS) |
| Output/decision | generated sample, action chunk 또는 trajectory | action frame, controller and termination | p. 21 (C.4 METRICS), p. 4 (3 PRELIMINARIES) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 5, the model achieves a lower FVD score, indicating that GF can be seamlessly integrated into video diffusion models and yields measurable gains. | definition/direction/unit from same section | p. 7 (5 EXPERIMENTS) |
| Aligning at layer 3 yields the best FVD-256 score while preserving FVD-16 performance. | definition/direction/unit from same section | p. 9 (5 EXPERIMENTS) |
| To further evaluate geometric consistency, we introduce Reprojection Error (RPE) (Duan et al., 2025) and Revisit Error (RVE) (Xiao et al., 2025). | definition/direction/unit from same section | p. 6 (5 EXPERIMENTS) |
| Revisit Error (RVE) assesses long-range temporal consistency by examining discrepancies between initial and revisited frames under complete camera rotation. | definition/direction/unit from same section | p. 6 (5 EXPERIMENTS) |
| Although direct mean squared error (MSE) also supervises magnitudes, changes in the diffusion model's feature scale may cause collapse in the following layers. | definition/direction/unit from same section | p. 8 (5 EXPERIMENTS) |
| This figure shows the trend of FVD scores during long-term video generation. | definition/direction/unit from same section | p. 9 (5 EXPERIMENTS) |
| The reprojection error is then computed by measuring the average Euclidean distance between the projected and observed pixel locations of co-visible 3D points across ... | definition/direction/unit from same section | p. 18 (C.4 METRICS) |
| Reprojection error (RPE) is a widely used metric in visual SLAM to evaluate multi-view geometric consistency. | definition/direction/unit from same section | p. 18 (C.4 METRICS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 2: Qualitative comparison of camera view-conditioned video generation under full- circle rotation. Videos are generated from a single frame, and per-frame camera poses ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| We conduct a comprehensive evaluation of GF on the RealEstate10K (Zhou et al., 2018) dataset, comparing against state-of-the-art baselines. | comparison identity and matched condition | p. 7 (5 EXPERIMENTS) |
| Compared to the baseline, GF results in significantly lower FVD after 100 frames. | comparison identity and matched condition | p. 9 (5 EXPERIMENTS) |
| 6, GF consistently outperforms all baselines across the three aspects of 3D consistency, demonstrating its effectiveness in producing geometrically coherent videos. | comparison identity and matched condition | p. 9 (5 EXPERIMENTS) |
| Figure 1: Geometry Forcing equips video diffusion models with 3D awareness. (a) We pro- pose Geometry Forcing (GF), a simple yet effective paradigm to ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| Figure 7: Qualitative comparisons on camera-conditioned video generation. All the videos are generated given the first frame and per-frame camera pose. We comprehensively compare ... | comparison identity and matched condition | p. 23 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 2: Ablation study on target represen- tation. We compare the effect of aligning the diffusion model with different target representa- tions: DINOv2 (semantic), ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Figure 3: Ablation study on alignment depth. We present FVD-256 and FVD-16 re- sults for different alignment layers of the dif- fusion model, which ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |
| 5.3 ABLATION STUDIES We provide a series of ablation studies to validate the design of GF. | component/input/data sensitivity | p. 7 (5 EXPERIMENTS) |
| Target Representation FVD-256 Baseline 364 DINOv2 Only 297 VGGT Only 243 VGGT + DINOv2 237 Table 3: Ablation study on alignment loss. | component/input/data sensitivity | p. 8 (5 EXPERIMENTS) |
| To further assess the impact of the proposed scale alignment loss, we conduct qualitative comparisons between models trained with and without this component (Fig. | component/input/data sensitivity | p. 24 (C.4 METRICS) |
| D SUPPLEMENTARY EXPERIMENTS D.1 ABLATION ON TEACHER MODEL Geometry Forcing does not depend on a specific 3D foundation model but still requires the 3D ... | component/input/data sensitivity | p. 19 (C.4 METRICS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To align these two representations, our method introduces two complementary alignment objectives: Angular Alignment and Scale Alignment. | Experimental results demonstrate that our approach achieves improvements across multiple evaluation dimensions, including visual aesthetics, motion smoothness, and motion quality, as detailed in Table ... | PDF body cue; verify exact table/figure and matched conditions | p. 20 (C.4 METRICS), p. 19 (C.4 METRICS), p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |
| Primary metric/result | We conduct Geometry Forcing algorithm on Pi3 model and also achieves significant improvement on video generation as shown in Tab. | numeric claim only at cited anchor | p. 19 (C.4 METRICS) |

- Numeric sentences retained from the body:
- **p. 6 / 5 EXPERIMENTS - extractive body cue:** For camera view-conditioned video generation, we apply GF on Diffusion Forcing Transformer (Song et al., 2025), training on 16-frame 256×256 videos for 2,500 steps with ...
- **p. 6 / 5 EXPERIMENTS - extractive body cue:** For action-conditioned video generation, we apply GF to Next-Frame Diffusion (Cheng et al., 2025), training on 32-frame 384×224 videos for 2,000 steps with a learning ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** Compared to the baseline, GF results in significantly lower FVD after 100 frames.
- **p. 18 / C.1 DATASET - extractive body cue:** For computational efficiency, we apply bilinear interpolation to reduce the spatial dimensions from the original resolution to a manageable 512×512 size.
- **p. 18 / C.2 TRAINING - extractive body cue:** Training proceeds for 2 epochs using a learning rate of 8 × 10-6 and a global batch size of 40.
- **p. 18 / C.3 INFERENCE - extractive body cue:** We demonstrate results using a DDIM sampler with 50 steps, though the approach is compatible with any standard diffusion sampling algorithm.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The primary limitation of this work lies in its scale. | p. 10 (6 CONCLUSION) |
| body limitation/failure cue | E.4 FAILURE CASE ANALYSIS Although our method significantly improves visual quality and geometric consistency in video generation, they still struggle in certain complex scenarios. | p. 22 (C.4 METRICS) |
| body limitation/failure cue | Figure 6: Failure Case Analysis. The transparent, reflective glass table intermittently disappears and reappears across frames, indicating that the model still has difficulty handling ... | p. 23 (Figure/Table caption) |
| body limitation/failure cue | While angular alignment alone helps maintain basic geometric coherence, the lack of scale supervision often leads to inconsistent camera motion, manifesting as unstable perspective ... | p. 24 (C.4 METRICS) |
| body limitation/failure cue | To combine the autoregressive nature with diffusion models, Diffusion Forcing (Chen et al., 2024a) proposes training video diffusion models with independent noise levels for ... | p. 6 (236 Discussion) |
| body limitation/failure cue | Motivated by the observation that video diffusion models trained on raw pixel data often fail to capture meaningful 3D structure, our method introduces two ... | p. 10 (6 CONCLUSION) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For action-conditioned video generation, we apply GF to Next-Frame Diffusion (Cheng et al., 2025), training on 32-frame 384×224 videos for 2,000 steps with a ... | p. 6 (5 EXPERIMENTS) |
| Training proceeds for 2 epochs using a learning rate of 8 × 10-6 and a global batch size of 40. | p. 18 (C.2 TRAINING) |
| We optimize the DPT head for 2500 steps using a learning rate of 1×10-4 and a batch size of 4. | p. 19 (C.4 METRICS) |
| In this section, we present the detailed implementations of the Reprojection Error (RPE) and the Revisit Error (RVE). | p. 18 (C.4 METRICS) |
| For fine-tuning, our method requires only a few thousand steps and completes within hours, yielding substantial efficiency gains over full pre-training. | p. 20 (C.4 METRICS) |
| E DISCUSSION E.1 COMPUTATIONAL EFFICIENCY We perform detailed profiling of our method on an NVIDIA A800 GPU and report the execution time and floating-point ... | p. 20 (C.4 METRICS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / 6 CONCLUSION - extractive body cue:** The primary limitation of this work lies in its scale.
- **p. 22 / C.4 METRICS - extractive body cue:** E.4 FAILURE CASE ANALYSIS Although our method significantly improves visual quality and geometric consistency in video generation, they still struggle in certain complex scenarios.
- **p. 23 / Figure/Table caption - extractive body cue:** Figure 6: Failure Case Analysis. The transparent, reflective glass table intermittently disappears and reappears across frames, indicating that the model still has difficulty handling reflective ...
- **p. 24 / C.4 METRICS - extractive body cue:** While angular alignment alone helps maintain basic geometric coherence, the lack of scale supervision often leads to inconsistent camera motion, manifesting as unstable perspective changes ...
- **p. 6 / 236 Discussion - extractive body cue:** To combine the autoregressive nature with diffusion models, Diffusion Forcing (Chen et al., 2024a) proposes training video diffusion models with independent noise levels for each ...
- **p. 10 / 6 CONCLUSION - extractive body cue:** Motivated by the observation that video diffusion models trained on raw pixel data often fail to capture meaningful 3D structure, our method introduces two alignment ...

- **Evidence anchors reviewed:** datasets p. 6 (5 EXPERIMENTS), p. 18 (C.1 DATASET), p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 18 (C.1 DATASET), metrics p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), baselines p. 7 (Figure/Table caption), p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 1 (Figure/Table caption), p. 23 (Figure/Table caption), results p. 20 (C.4 METRICS), p. 19 (C.4 METRICS), p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
