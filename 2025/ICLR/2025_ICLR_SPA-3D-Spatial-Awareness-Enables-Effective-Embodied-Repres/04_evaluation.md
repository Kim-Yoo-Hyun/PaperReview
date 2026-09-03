# Evaluation - SPA: 3D Spatial-Awareness Enables Effective Embodied Representation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (31 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=6TLdqAZgzn; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/114708. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 6 (Figure/Table caption), p. 2 (Figure/Table caption), p. 7 (Figure/Table caption), p. 10 (Figure/Table caption)): Tab. 3. For detailed results on each task and each random seed, please refer to Appendix D. We also have visualized the performance radar chart and the per-task rank distributions ...

## Evaluation Body Digest

- **p. 23 / C.2 PRE-TRAINING DETAILS - extractive body cue:** (14) F REAL-WORLD EXPERIMENT DETAILS Our real-world hardware setup is based on the open-source Low-Cost-Robot project (Koch, 2024).
- **p. 23 / C.2 PRE-TRAINING DETAILS - extractive body cue:** The experiment is conducted on GraspNet-1Billion (Fang et al., 2020), a large-scale real-world object grasping benchmark.
- **p. 21 / C.1 DATASET DETAILS - extractive body cue:** Each epoch includes 5 times the dataset size.
- **p. 21 / C.1 DATASET DETAILS - extractive body cue:** The datasets used for SPA include ScanNet, ScanNet++, Hypersim, ADT, S3DIS, and Droid.
- **p. 22 / C.2 PRE-TRAINING DETAILS - extractive body cue:** (2024) for camera pose estimation using the NAVI dataset (Jampani et al., 2023).
- **p. 24 / C.2 PRE-TRAINING DETAILS - extractive body cue:** The models are evaluated on two subsets of the VC-1 benchmark.
- **p. 24 / C.2 PRE-TRAINING DETAILS - extractive body cue:** It was trained on the ScanNet dataset without semantic supervision, ensuring a fair comparison with the result in the last line of Tab.
- **p. 22 / C.1 DATASET DETAILS - extractive body cue:** Frames with very small valid depth areas or scene boxes are filtered out.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** B EVALUATION SETUPS (p. 17); B.1 SINGLE-TASK BENCHMARKS (p. 17); B.2 LANGUAGE-CONDITIONED MULTI-TASK BENCHMARKS (p. 18); C MORE IMPLEMENTATION DETAILS (p. 21); C.1 DATASET DETAILS (p. 21).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Tab. 3. For detailed results on each task and each random seed, please refer to Appendix D. We also have visualized the performance radar ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 4: Correlation between mean success rate and camera pose regression error. 5.2 ADDITIONAL COMPARISONS (Q1) We primarily compare with SOTA methods using the ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 1: Influence of different datasets. We present the performance results on the VC-1 benchmark. Mean S.R. refers to the mean success rate across ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 1: Performance comparison across representations. Above: (a) Mean rank and (b) mean success rate on benchmarks. Lines represent the performance of SPA, best, ... | p. 2 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 3: Comparison of different representation learning methods. ‘OOM' indicates an out- of-memory error during evaluation. The best and second-best results are bolded and ... | p. 7 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 23 / C.2 PRE-TRAINING DETAILS - extractive body cue:** (14) F REAL-WORLD EXPERIMENT DETAILS Our real-world hardware setup is based on the open-source Low-Cost-Robot project (Koch, 2024).
- **p. 23 / C.2 PRE-TRAINING DETAILS - extractive body cue:** The experiment is conducted on GraspNet-1Billion (Fang et al., 2020), a large-scale real-world object grasping benchmark.
- **p. 21 / C.1 DATASET DETAILS - extractive body cue:** Each epoch includes 5 times the dataset size.
- **p. 21 / C.1 DATASET DETAILS - extractive body cue:** The datasets used for SPA include ScanNet, ScanNet++, Hypersim, ADT, S3DIS, and Droid.
- **p. 22 / C.2 PRE-TRAINING DETAILS - extractive body cue:** (2024) for camera pose estimation using the NAVI dataset (Jampani et al., 2023).
- **p. 24 / C.2 PRE-TRAINING DETAILS - extractive body cue:** The models are evaluated on two subsets of the VC-1 benchmark.
- **p. 24 / C.2 PRE-TRAINING DETAILS - extractive body cue:** It was trained on the ScanNet dataset without semantic supervision, ensuring a fair comparison with the result in the last line of Tab.
- **p. 22 / C.1 DATASET DETAILS - extractive body cue:** Frames with very small valid depth areas or scene boxes are filtered out.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Performance comparison across representations. Above: (a) Mean rank and (b) mean success rate on benchmarks. Lines represent the performance of SPA, best, and ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Pipeline Overview. Given multi-view images, we randomly mask patches and input the remaining into a Vision Transformer. The upsampled latent features generate multi-view ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Overview of our large-scale embodied evaluation. We conduct the largest-scale evaluation of embodied representation learning to date. Our study encompasses 268 tasks across ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1: Influence of different datasets. We present the performance results on the VC-1 benchmark. Mean S.R. refers to the mean success rate across all ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Summary of different representation learning methods. ‘#Param.' is the total parameters of the encoder, while ‘#Frames' indicates the total number of image frames ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3: Comparison of different representation learning methods. ‘OOM' indicates an out- of-memory error during evaluation. The best and second-best results are bolded and underlined ...
- **p. 7 / Figure/Table caption - extractive body cue:** Tab. 3. For detailed results on each task and each random seed, please refer to Appendix D. We also have visualized the performance radar chart ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4: Additional comparisons of ViT-base models. S.R. denotes ‘Success Rate'. Methods DINOV2-B (Oquab et al., 2023) MAE-B (He et al., 2022)

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | (14) F REAL-WORLD EXPERIMENT DETAILS Our real-world hardware setup is based on the open-source Low-Cost-Robot project (Koch, 2024). | embodiment, simulator version and control stack | p. 23 (C.2 PRE-TRAINING DETAILS), p. 23 (C.2 PRE-TRAINING DETAILS) |
| Task/environment | The experiment is conducted on GraspNet-1Billion (Fang et al., 2020), a large-scale real-world object grasping benchmark. | reset, timeout, object/scene variation | p. 23 (C.2 PRE-TRAINING DETAILS), p. 21 (C.1 DATASET DETAILS) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 3 (2 METHODOLOGY), p. 3 (2 METHODOLOGY) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 1 (1 INTRODUCTION), p. 23 (C.2 PRE-TRAINING DETAILS) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Meta-World RL Task Method (ViT-B) Success Rate Episode Reward button-press-topdown-v2 CLIP 0.93 653.97 DINOv2 1.00 746.04 MAE 0.46 517.54 MoCoV3 0.99 749.93 SPA (Ours) ... | definition/direction/unit from same section | p. 24 (C.2 PRE-TRAINING DETAILS) |
| Table 3: Comparison of different representation learning methods. ‘OOM' indicates an out- of-memory error during evaluation. The best and second-best results are bolded and ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 4: Correlation between mean success rate and camera pose regression error. 5.2 ADDITIONAL COMPARISONS (Q1) We primarily compare with SOTA methods using the ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| We report the evaluation success rate and episode reward below in Tab. | definition/direction/unit from same section | p. 23 (C.2 PRE-TRAINING DETAILS) |
| Tab. 3. For detailed results on each task and each random seed, please refer to Appendix D. We also have visualized the performance radar ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 1: Performance comparison across representations. Above: (a) Mean rank and (b) mean success rate on benchmarks. Lines represent the performance of SPA, best, ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Table 1: Influence of different datasets. We present the performance results on the VC-1 benchmark. Mean S.R. refers to the mean success rate across ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Table 4: Additional comparisons of ViT-base models. S.R. denotes ‘Success Rate'. Methods DINOV2-B (Oquab et al., 2023) MAE-B (He et al., 2022) | definition/direction/unit from same section | p. 8 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 4: Correlation between mean success rate and camera pose regression error. 5.2 ADDITIONAL COMPARISONS (Q1) We primarily compare with SOTA methods using the ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Figure 3: Overview of our large-scale embodied evaluation. We conduct the largest-scale evaluation of embodied representation learning to date. Our study encompasses 268 tasks ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |
| Nevertheless, overall, our 3D spatial-aware representation outperforms other representation learning methods. | comparison identity and matched condition | p. 23 (C.2 PRE-TRAINING DETAILS) |
| (2023) to use DrQ-v2 (Yarats et al., 2021), a state-of-the-art off-policy actor-critic approach for continuous vision-based control. | comparison identity and matched condition | p. 23 (C.2 PRE-TRAINING DETAILS) |
| We refer to this baseline as MV-MAE. | comparison identity and matched condition | p. 24 (C.2 PRE-TRAINING DETAILS) |
| It was trained on the ScanNet dataset without semantic supervision, ensuring a fair comparison with the result in the last line of Tab. | comparison identity and matched condition | p. 24 (C.2 PRE-TRAINING DETAILS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 6: Additional ablations on VC-1. Methods SPA-B SPA-MAE RADIO E-RADIO VC-1 AD | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Figure 4: Correlation between mean success rate and camera pose regression error. 5.2 ADDITIONAL COMPARISONS (Q1) We primarily compare with SOTA methods using the ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| This initialization does not affect the validity of our conclusions, as demonstrated by the ablation study of SPA-MAE in Sec. | component/input/data sensitivity | p. 22 (C.2 PRE-TRAINING DETAILS) |
| It was trained on the ScanNet dataset without semantic supervision, ensuring a fair comparison with the result in the last line of Tab. | component/input/data sensitivity | p. 24 (C.2 PRE-TRAINING DETAILS) |
| Table 11: Additional Ablation Study on Neural Rendering. The models are evaluated on two subsets of the VC-1 benchmark. The model architectures are both ... | component/input/data sensitivity | p. 24 (Figure/Table caption) |
| Table 7: Mask ratio and loss components. C., D., S. denote color, depth, and semantic. Mask Ratio Loss VC-1 Benchmark Mean S.R. | component/input/data sensitivity | p. 9 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contribution can be summarized as follows. • We propose a significant spatial hypothesis: 3D spatial awareness is crucial for embodied representation learning. | Tab. 3. For detailed results on each task and each random seed, please refer to Appendix D. We also have visualized the performance radar ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 6 (Figure/Table caption), p. 2 (Figure/Table caption), p. 7 (Figure/Table caption), p. 10 (Figure/Table caption) |
| Primary metric/result | Figure 4: Correlation between mean success rate and camera pose regression error. 5.2 ADDITIONAL COMPARISONS (Q1) We primarily compare with SOTA methods using the ... | numeric claim only at cited anchor | p. 8 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 21 / C.1 DATASET DETAILS - extractive body cue:** For each scene, a random starting frame is selected, followed by the sampling of 1 to 8 frames at random, with an interval of 8 ...
- **p. 21 / C.1 DATASET DETAILS - extractive body cue:** For each scene, a random starting frame is selected, followed by the sampling of 1 to 8 frames at random, with an interval of 5 ...
- **p. 22 / C.1 DATASET DETAILS - extractive body cue:** For each scene, a random starting frame is selected, followed by the sampling of 1 to 8 frames at random, with an interval of 5 ...
- **p. 22 / C.2 PRE-TRAINING DETAILS - extractive body cue:** The model is trained for 2000 epochs on 80 NVIDIA A100-80G GPUs, using a gradient clipping threshold of 1.0.
- **p. 22 / C.2 PRE-TRAINING DETAILS - extractive body cue:** The model is trained for 100 epochs with a base learning rate of 1 × 10-3 and a starting percentage of 0.1.
- **p. 23 / C.2 PRE-TRAINING DETAILS - extractive body cue:** For each task, we collect 50 demonstrations, and during evaluation, we conduct 25 rollouts, each with randomized object locations and orientations.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Since Droid does not provide depth data, we utilize Croco-Stereo Weinzaepfel et al. | p. 22 (C.1 DATASET DETAILS) |
| body limitation/failure cue | This initialization does not affect the validity of our conclusions, as demonstrated by the ablation study of SPA-MAE in Sec. | p. 22 (C.2 PRE-TRAINING DETAILS) |
| body limitation/failure cue | Simple multiview attention-based interaction, as used in MV-MAE, does not perform as effectively in learning 3D spatial awareness. | p. 24 (C.2 PRE-TRAINING DETAILS) |
| body limitation/failure cue | Tab. 3. For detailed results on each task and each random seed, please refer to Appendix D. We also have visualized the performance radar ... | p. 7 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Each GPU processes a batch size of 2, with 8 gradient accumulation steps, resulting in a total effective batch size of 2 × 80 ... | p. 22 (C.2 PRE-TRAINING DETAILS) |
| The base learning rate is set to 5 × 10-6, and the actual learning rate is scaled by a factor of 8 times the ... | p. 22 (C.2 PRE-TRAINING DETAILS) |
| We run three seeds for each experiment. | p. 23 (C.2 PRE-TRAINING DETAILS) |
| We train for a total of 1.1M frames and all other hyperparameters including random seeds are kept as default and same. | p. 23 (C.2 PRE-TRAINING DETAILS) |
| In this study, we maintained all settings identical-data loading, training techniques, hyperparameters, and the encoder-while replacing the volume neural rendering decoder with a multiview ... | p. 24 (C.2 PRE-TRAINING DETAILS) |
| This alternative decoder receives masked patches filled with mask tokens corresponding to multiview images. | p. 24 (C.2 PRE-TRAINING DETAILS) |
| Following MAE, we apply random masking to input images to enhance robustness, but without a ViT decoder and MAE's pixel reconstruction objective. | p. 3 (2 METHODOLOGY) |
| (2) Unlike prior work (Huang et al., 2023; Zhu et al., 2023b; Yang et al., 2024a), which employs an MLP to compute the attributes ... | p. 3 (2 METHODOLOGY) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 22 / C.1 DATASET DETAILS - extractive body cue:** Since Droid does not provide depth data, we utilize Croco-Stereo Weinzaepfel et al.
- **p. 22 / C.2 PRE-TRAINING DETAILS - extractive body cue:** This initialization does not affect the validity of our conclusions, as demonstrated by the ablation study of SPA-MAE in Sec.
- **p. 24 / C.2 PRE-TRAINING DETAILS - extractive body cue:** Simple multiview attention-based interaction, as used in MV-MAE, does not perform as effectively in learning 3D spatial awareness.
- **p. 7 / Figure/Table caption - extractive body cue:** Tab. 3. For detailed results on each task and each random seed, please refer to Appendix D. We also have visualized the performance radar chart ...

- **Evidence anchors reviewed:** datasets p. 23 (C.2 PRE-TRAINING DETAILS), p. 23 (C.2 PRE-TRAINING DETAILS), p. 21 (C.1 DATASET DETAILS), p. 21 (C.1 DATASET DETAILS), p. 22 (C.2 PRE-TRAINING DETAILS), p. 24 (C.2 PRE-TRAINING DETAILS), metrics p. 24 (C.2 PRE-TRAINING DETAILS), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 23 (C.2 PRE-TRAINING DETAILS), p. 7 (Figure/Table caption), p. 2 (Figure/Table caption), baselines p. 8 (Figure/Table caption), p. 5 (Figure/Table caption), p. 23 (C.2 PRE-TRAINING DETAILS), p. 23 (C.2 PRE-TRAINING DETAILS), p. 24 (C.2 PRE-TRAINING DETAILS), p. 24 (C.2 PRE-TRAINING DETAILS), results p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 6 (Figure/Table caption), p. 2 (Figure/Table caption), p. 7 (Figure/Table caption), p. 10 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
