# Evaluation - S2GS: Streaming Semantic Gaussian Splatting for Online Scene Understanding and Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=CbWCaD8tRC; PDF retrieval source: https://openreview.net/pdf/fec4864d5571755c82ad1d076f9a8e3e4ca69cf8.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.2. Results), p. 8 (4.3. Ablation Studies), p. 8 (4.3. Ablation Studies), p. 6 (4.2. Results), p. 5 (4.1. Experimental Setup), p. 7 (4.2. Results)): Nevertheless, as the number of input views increases (8/14/32), S2GS consistently improves and achieves strong performance in both reconstruction quality and temporal semantic/instance consistency, highlighting its effectiveness in prac ...

## Evaluation Body Digest

- **p. 6 / 4.1. Experimental Setup - extractive body cue:** Comparison with feed-forward methods on the ScanNet (Dai et al., 2017) dataset under short-sequence inputs. "•", "†", and "⋆" denote reconstruction-only, understanding-only, and joint reconstruction-and-understanding ...
- **p. 7 / 4.2. Results - extractive body cue:** Qualitative results on ScanNet dataset.
- **p. 7 / 4.2. Results - extractive body cue:** Zero-shot cross-dataset comparison under 32-view input.
- **p. 8 / 4.2. Results - extractive body cue:** Nevertheless, under the same training configuration, S2GS achieves better reconstruction and semantic performance on both datasets, demonstrating stronger cross-dataset generalization and robustness.
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** Detailed sequence construction, the IoU definition, and training settings are provided in the appendix.
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** S2GS: Streaming Semantic Gaussian Splatting for Online Scene Understanding and Reconstruction Table 2.
- **p. 6 / 82.49 Method - extractive body cue:** For 3D scene understanding, we report per-frame semantic segmentation accuracy with mIoU, and cross-frame instance consistency using T-mIoU and T-SR.
- **p. 8 / 4.3. Ablation Studies - extractive body cue:** As shown in Table 7, geometry-semantic decoupling leads to a clear improvement in per-frame semantic accuracy and yields even larger gains in temporal instance consistency ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Experimental Setup (p. 5); 4.2. Results (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Nevertheless, as the number of input views increases (8/14/32), S2GS consistently improves and achieves strong performance in both reconstruction quality and temporal semantic/instance consistency, ... | p. 6 (4.2. Results) |
| 4.3. Ablation Studies | EMPIRICAL / SOURCE-REPORTED EVALUATION | The results demonstrate that the distillation loss significantly improves reconstruction quality. | p. 8 (4.3. Ablation Studies) |
| 4.3. Ablation Studies | EMPIRICAL / SOURCE-REPORTED EVALUATION | As shown in Table 7, geometry-semantic decoupling leads to a clear improvement in per-frame semantic accuracy and yields even larger gains in temporal instance ... | p. 8 (4.3. Ablation Studies) |
| 4.2. Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | As shown in Table 2, under the extremely sparse 2-view setting, S2GS does not achieve the best PSNR/SSIM. | p. 6 (4.2. Results) |
| 4.1. Experimental Setup | EMPIRICAL / SOURCE-REPORTED EVALUATION | In addition, we report results for reconstruction-only Gaussian splatting baselines, including pixelSplat (Charatan et al., 2024), MVSplat (Chen et al., 2024), and NoPoSplat (Ye ... | p. 5 (4.1. Experimental Setup) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Experimental Setup - extractive body cue:** Comparison with feed-forward methods on the ScanNet (Dai et al., 2017) dataset under short-sequence inputs. "•", "†", and "⋆" denote reconstruction-only, understanding-only, and joint reconstruction-and-understanding ...
- **p. 7 / 4.2. Results - extractive body cue:** Qualitative results on ScanNet dataset.
- **p. 7 / 4.2. Results - extractive body cue:** Zero-shot cross-dataset comparison under 32-view input.
- **p. 8 / 4.2. Results - extractive body cue:** Nevertheless, under the same training configuration, S2GS achieves better reconstruction and semantic performance on both datasets, demonstrating stronger cross-dataset generalization and robustness.
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** Detailed sequence construction, the IoU definition, and training settings are provided in the appendix.
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** S2GS: Streaming Semantic Gaussian Splatting for Online Scene Understanding and Reconstruction Table 2.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Comparison of current-frame inference time and GPU memory usage between S2GS (Ours) and the recent advanced joint reconstruction and understanding method, SIU3R(Xu et ...
- **p. 3 / Figure/Table caption - extractive body cue:** Table 1. Comparison of S2GS with prior paradigms for 3D re- construction and scene understanding. SC: strictly causal; RF: reprocessing-free; IS: instance-level semantics; SS: streaming ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Overview of S2GS. S2GS processes an uncalibrated and unposed RGB image stream in a strictly causal manner. A causal Transformer encoder, guided by ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Comparison with feed-forward methods on the ScanNet (Dai et al., 2017) dataset under short-sequence inputs. "•", "†", and "⋆" denote reconstruction-only, understanding-only, and ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 3. Comparison under Long-sequence input views. Views
- **p. 6 / Figure/Table caption - extractive body cue:** Table 4. Current-frame inference time and PGM under online streaming input. Views SIU3R Ours Time(s) ↓PGM(GB) ↓Time(s) ↓PGM(GB) ↓ 16 0.26
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3. Qualitative results on ScanNet dataset. GT Ours SIU3R 64-views input. GT Ours 256-views input.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Late-stage novel view synthesis results under longer input streams.

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Comparison with feed-forward methods on the ScanNet (Dai et al., 2017) dataset under short-sequence inputs. "•", "†", and "⋆" denote reconstruction-only, understanding-only, and joint ... | embodiment, simulator version and control stack | p. 6 (4.1. Experimental Setup), p. 7 (4.2. Results) |
| Task/environment | Qualitative results on ScanNet dataset. | reset, timeout, object/scene variation | p. 7 (4.2. Results), p. 7 (4.2. Results) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 1 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 5 (3.4. Language-driven Open-vocabulary Segmentation), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Detailed sequence construction, the IoU definition, and training settings are provided in the appendix. | definition/direction/unit from same section | p. 5 (4.1. Experimental Setup) |
| For 3D scene understanding, we report per-frame semantic segmentation accuracy with mIoU, and cross-frame instance consistency using T-mIoU and T-SR. | definition/direction/unit from same section | p. 6 (82.49 Method) |
| As shown in Table 7, geometry-semantic decoupling leads to a clear improvement in per-frame semantic accuracy and yields even larger gains in temporal instance ... | definition/direction/unit from same section | p. 8 (4.3. Ablation Studies) |
| The results demonstrate that the distillation loss significantly improves reconstruction quality. | definition/direction/unit from same section | p. 8 (4.3. Ablation Studies) |
| The main difference lies in our longsequence sampling strategy. | definition/direction/unit from same section | p. 5 (4.1. Experimental Setup) |
| Nevertheless, as the number of input views increases (8/14/32), S2GS consistently improves and achieves strong performance in both reconstruction quality and temporal semantic/instance consistency, ... | definition/direction/unit from same section | p. 6 (4.2. Results) |
| Figure 2. Overview of S2GS. S2GS processes an uncalibrated and unposed RGB image stream in a strictly causal manner. A causal Transformer encoder, guided ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We also include widely used 2D semantic segmentation baselines, LSeg (Li et al., 2022) and Mask2Former (Cheng et al., 2022). | comparison identity and matched condition | p. 5 (4.1. Experimental Setup) |
| In addition, we report results for reconstruction-only Gaussian splatting baselines, including pixelSplat (Charatan et al., 2024), MVSplat (Chen et al., 2024), and NoPoSplat (Ye ... | comparison identity and matched condition | p. 5 (4.1. Experimental Setup) |
| We evaluate S2GS on ScanNet and compare it with offline feed-forward baselines. | comparison identity and matched condition | p. 6 (4.2. Results) |
| This is expected, since offline baselines can exploit non-causal cross-view aggregation over the full input set to better resolve view ambiguity and occlusions when ... | comparison identity and matched condition | p. 6 (4.2. Results) |
| Method mIoU↑ T-mIoU↑ T-SR↑ w/o CL 47.13 28.64 50.13 w CL 48.95 30.01 62.39 outperforming SIU3R and LSeg. | comparison identity and matched condition | p. 8 (4.2. Results) |
| We observe that both S2GS and the baseline SIU3R (Xu et al., 2025) exhibit non-trivial zero-shot generalization capability. | comparison identity and matched condition | p. 8 (4.2. Results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Ablation study on the effectiveness of query-level semantic-embedding contrastive learning. | component/input/data sensitivity | p. 8 (4.2. Results) |
| Ablation study on the effectiveness of distilling the base model for the geometric backbone. | component/input/data sensitivity | p. 8 (4.2. Results) |
| In contrast, S2GS is designed for streaming inputs and incrementally aggregates multi-view evidence as views arrive, without relying on global alignment. | component/input/data sensitivity | p. 6 (4.2. Results) |
| Figure 2. Overview of S2GS. S2GS processes an uncalibrated and unposed RGB image stream in a strictly causal manner. A causal Transformer encoder, guided ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We propose S2GS, a strictly causal and reprocessing-free framework for online joint 3D reconstruction and scene understanding, which incrementally maintains scene geometry, appearance, and ... | Nevertheless, as the number of input views increases (8/14/32), S2GS consistently improves and achieves strong performance in both reconstruction quality and temporal semantic/instance consistency, ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.2. Results), p. 8 (4.3. Ablation Studies), p. 8 (4.3. Ablation Studies), p. 6 (4.2. Results), p. 5 (4.1. Experimental Setup), p. 7 (4.2. Results) |
| Primary metric/result | The results demonstrate that the distillation loss significantly improves reconstruction quality. | numeric claim only at cited anchor | p. 8 (4.3. Ablation Studies) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | As shown in Table 2, under the extremely sparse 2-view setting, S2GS does not achieve the best PSNR/SSIM. | p. 6 (4.2. Results) |
| body limitation/failure cue | This is expected, since offline baselines can exploit non-causal cross-view aggregation over the full input set to better resolve view ambiguity and occlusions when ... | p. 6 (4.2. Results) |
| body limitation/failure cue | Nevertheless, under the same training configuration, S2GS achieves better reconstruction and semantic performance on both datasets, demonstrating stronger cross-dataset generalization and robustness. | p. 8 (4.2. Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Current-frame inference time and PGM under online streaming input. | p. 6 (4.2. Results) |
| benchmarks and long-horizon online settings, S2GS achieves performance on par with or better than strong offline baselines, while significantly outperforming offline global paradigms in ... | p. 2 (4. Across multiple joint reconstruction-and-understanding) |
| Our method maintains low per-frame runtime with only mild growth as the stream length increases, while SIU3R (Xu et al., 2025) exhibits rapidly growing ... | p. 7 (4.2. Results) |
| Method ScanNet++ Replica PSNR↑ mIoU↑ PSNR↑ mIoU↑ SIU3R 12.85 33.51 13.14 21.42 S2GS 15.33 41.67 15.66 37.47 and updating the persistent state) and peak ... | p. 7 (4.2. Results) |
| At test time, given a text description r, we obtain a normalized text embedding er using the SigLIP2 (Tschannen et al., 2025) text encoder ... | p. 5 (3.4. Language-driven Open-vocabulary Segmentation) |
| Following prior designs (Wang et al., 2025a; Lan et al., 2025), each frame is encoded into visual tokens (Oquab et al., 2023) and processed ... | p. 3 (3.2. Causal Transformer for 3D Gaussian Regression) |
| S2GS operates under a strictly causal setting: at time t, the model processes only the current frame It together with persistent states accumulated from ... | p. 3 (3.1. Overview and Online Setting) |
| Each incoming frame It is encoded by a frozen 2D vision foundation model (Tschannen et al., 2025) to extract robust semantic features. | p. 4 (3.3. Online Instance Tracking and Semantic) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 4.2. Results - extractive body cue:** As shown in Table 2, under the extremely sparse 2-view setting, S2GS does not achieve the best PSNR/SSIM.
- **p. 6 / 4.2. Results - extractive body cue:** This is expected, since offline baselines can exploit non-causal cross-view aggregation over the full input set to better resolve view ambiguity and occlusions when observations ...
- **p. 8 / 4.2. Results - extractive body cue:** Nevertheless, under the same training configuration, S2GS achieves better reconstruction and semantic performance on both datasets, demonstrating stronger cross-dataset generalization and robustness.

- **Evidence anchors reviewed:** datasets p. 6 (4.1. Experimental Setup), p. 7 (4.2. Results), p. 7 (4.2. Results), p. 8 (4.2. Results), p. 5 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), metrics p. 5 (4.1. Experimental Setup), p. 6 (82.49 Method), p. 8 (4.3. Ablation Studies), p. 8 (4.3. Ablation Studies), p. 5 (4.1. Experimental Setup), p. 6 (4.2. Results), baselines p. 5 (4.1. Experimental Setup), p. 5 (4.1. Experimental Setup), p. 6 (4.2. Results), p. 6 (4.2. Results), p. 8 (4.2. Results), p. 8 (4.2. Results), results p. 6 (4.2. Results), p. 8 (4.3. Ablation Studies), p. 8 (4.3. Ablation Studies), p. 6 (4.2. Results), p. 5 (4.1. Experimental Setup), p. 7 (4.2. Results).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
