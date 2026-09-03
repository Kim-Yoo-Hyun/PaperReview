# Evaluation - VideoRFSplat: Direct Scene-Level Text-to-3D Gaussian Splatting Generation with Flexible Pose and Multi-View Joint Modeling

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Go_VideoRFSplat_Direct_Scene-Level_Text-to-3D_Gaussian_Splatting_Generation_with_Flexible_Pose_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Go_VideoRFSplat_Direct_Scene-Level_Text-to-3D_Gaussian_Splatting_Generation_with_Flexible_Pose_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 8 (Figure/Table caption), p. 5 (5. Experimental Results), p. 1 (Figure/Table caption), p. 6 (5.1. Experimental Setups)): Table 2. Quantitative results on MVImgNet [84] and DL3DV [41] validation sets. VideoRFSplat achieves the higher performance across all metrics without SDS++ refinement. sess image quality and CLIP score for ...

## Evaluation Body Digest

- **p. 6 / 5.1. Experimental Setups - extractive body cue:** Following previous works [20, 35], we evaluate our model on the MVImgNet and DL3DV validation datasets, as well as the T3Bench benchmark [23].
- **p. 6 / 5.1. Experimental Setups - extractive body cue:** We utilize four real-world datasets for training: RealEstate10K [93], MVImgNet [84], DL3DV10K [41], and ACID [43].
- **p. 8 / Figure/Table caption - extractive body cue:** Table 5. VideoRFSplat outperforms other methods in FID-8K (43.07), translation error (0.063), rotation error (0.4223), and CLIPScore (31.1). These results confirm that VideoRFSplat generates images ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Quantitative results on MVImgNet [84] and DL3DV [41] validation sets. VideoRFSplat achieves the higher performance across all metrics without SDS++ refinement. sess image ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Ablation study on asynchronous sampling. We also report CLIP scores on multi-view images to assess text alignment of not lifted images to 3DGS. ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 5. Results on camera conditioned generation. VideoRFS- plat can perform camera-conditioned generation. models under identical conditions for 60K iterations with Mochi [69] and then ...
- **p. 5 / 5. Experimental Results - extractive body cue:** Here, we demonstrate the effectiveness of VideoRFSplat for text-to-3DGS generation.
- **p. 6 / 5.1. Experimental Setups - extractive body cue:** Despite not using SDS++ [35], VideoRFSplat generates detailed, visually consistent scenes, producing appropriate scene-specific camera poses.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** high-dimensional data 또는 robot action-trajectory distribution.
- **Input boundary:** conditioning observation와 noisy/intermediate sample.
- **Output/decision under evaluation:** generated sample, action chunk 또는 trajectory.
- **Primary target:** distribution fit, multimodality, sample quality와 latency.
- **Detected evaluation headings:** 5. Experimental Results (p. 5); 5.1. Experimental Setups (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 2. Quantitative results on MVImgNet [84] and DL3DV [41] validation sets. VideoRFSplat achieves the higher performance across all metrics without SDS++ refinement. sess ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 5. VideoRFSplat outperforms other methods in FID-8K (43.07), translation error (0.063), rotation error (0.4223), and CLIPScore (31.1). These results confirm that VideoRFSplat generates ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 5. Results on camera conditioned generation. VideoRFS- plat can perform camera-conditioned generation. models under identical conditions for 60K iterations with Mochi [69] and ... | p. 8 (Figure/Table caption) |
| 5. Experimental Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our primary result is that VideoRFSplat, without SDS optimization, outperforms previous direct text-to-3DGS methods that employ SDS optimization. | p. 5 (5. Experimental Results) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 1. Generated 3D Gaussian Splattings and rendered views from diverse texts by VideoRFSplat. VideoRFSplat directly generates realistic 3D scenes from text without SDS ... | p. 1 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 5.1. Experimental Setups - extractive body cue:** Following previous works [20, 35], we evaluate our model on the MVImgNet and DL3DV validation datasets, as well as the T3Bench benchmark [23].
- **p. 6 / 5.1. Experimental Setups - extractive body cue:** We utilize four real-world datasets for training: RealEstate10K [93], MVImgNet [84], DL3DV10K [41], and ACID [43].

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Generated 3D Gaussian Splattings and rendered views from diverse texts by VideoRFSplat. VideoRFSplat directly generates realistic 3D scenes from text without SDS [35, ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. VideoRFSplat Overview. (a) VideoRFSplat consists of a dual-stream pose-video model and a Gaussian Splat decoder. To minimize pose-image interference, the pose model is ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Failure analysis of synchronized sampling and the effectiveness of asynchronous sampling. (Left) Early in sampling (t > 0.85), synchronous sampling induces excessive oscillations ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. Asynchrnous schedule (δ = 0.2). During sampling, we denoise the pose modality faster than im- ages, as it is robust to fast denoising. ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5. Qualitative comparison of text-to-3DGS generation on DL3DV [41] and MVImgNet [84] validation sets as well as T3Bench [23]. Rendered scenes: First two rows ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Quantitative results on T3Bench [23]. VideoRFSplat outperforms all baselines without SDS++ refinement.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Quantitative results on MVImgNet [84] and DL3DV [41] validation sets. VideoRFSplat achieves the higher performance across all metrics without SDS++ refinement. sess image ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Ablation study on asynchronous sampling. We also report CLIP scores on multi-view images to assess text alignment of not lifted images to 3DGS. ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Following previous works [20, 35], we evaluate our model on the MVImgNet and DL3DV validation datasets, as well as the T3Bench benchmark [23]. | embodiment, simulator version and control stack | p. 6 (5.1. Experimental Setups), p. 6 (5.1. Experimental Setups) |
| Task/environment | We utilize four real-world datasets for training: RealEstate10K [93], MVImgNet [84], DL3DV10K [41], and ACID [43]. | reset, timeout, object/scene variation | p. 6 (5.1. Experimental Setups) |
| Observation/sensor | conditioning observation와 noisy/intermediate sample | calibration, preprocessing, privileged input | p. 8 (Method), p. 2 (1. Introduction) |
| Output/decision | generated sample, action chunk 또는 trajectory | action frame, controller and termination | p. 8 (Method), p. 4 (4.1. Dual-Stream Pose-Video Joint Model) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 5. VideoRFSplat outperforms other methods in FID-8K (43.07), translation error (0.063), rotation error (0.4223), and CLIPScore (31.1). These results confirm that VideoRFSplat generates ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Table 2. Quantitative results on MVImgNet [84] and DL3DV [41] validation sets. VideoRFSplat achieves the higher performance across all metrics without SDS++ refinement. sess ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Table 3. Ablation study on asynchronous sampling. We also report CLIP scores on multi-view images to assess text alignment of not lifted images to ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Table 5. Results on camera conditioned generation. VideoRFS- plat can perform camera-conditioned generation. models under identical conditions for 60K iterations with Mochi [69] and ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Here, we demonstrate the effectiveness of VideoRFSplat for text-to-3DGS generation. | definition/direction/unit from same section | p. 5 (5. Experimental Results) |
| Despite not using SDS++ [35], VideoRFSplat generates detailed, visually consistent scenes, producing appropriate scene-specific camera poses. | definition/direction/unit from same section | p. 6 (5.1. Experimental Setups) |
| Since these datasets lack paired textual descriptions, we generate textual annotations using InternVL-2.5-26B [12], producing multiple captions per sequence. | definition/direction/unit from same section | p. 6 (5.1. Experimental Setups) |
| Figure 1. Generated 3D Gaussian Splattings and rendered views from diverse texts by VideoRFSplat. VideoRFSplat directly generates realistic 3D scenes from text without SDS ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 1. Quantitative results on T3Bench [23]. VideoRFSplat outperforms all baselines without SDS++ refinement. | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Our primary result is that VideoRFSplat, without SDS optimization, outperforms previous direct text-to-3DGS methods that employ SDS optimization. | comparison identity and matched condition | p. 5 (5. Experimental Results) |
| Figure 1. Generated 3D Gaussian Splattings and rendered views from diverse texts by VideoRFSplat. VideoRFSplat directly generates realistic 3D scenes from text without SDS ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| Additionally, for evaluations on T3Bench [23], we include previously reported baseline results [20, 35]. | comparison identity and matched condition | p. 6 (5.1. Experimental Setups) |
| Table 5. VideoRFSplat outperforms other methods in FID-8K (43.07), translation error (0.063), rotation error (0.4223), and CLIPScore (31.1). These results confirm that VideoRFSplat generates ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Table 5. Results on camera conditioned generation. VideoRFS- plat can perform camera-conditioned generation. models under identical conditions for 60K iterations with Mochi [69] and ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| As both methods use SDS++ [35] as a refinement step, we compare two variants for each method: with and without SDS++. | component/input/data sensitivity | p. 6 (5.1. Experimental Setups) |
| Our primary result is that VideoRFSplat, without SDS optimization, outperforms previous direct text-to-3DGS methods that employ SDS optimization. | component/input/data sensitivity | p. 5 (5. Experimental Results) |
| Figure 1. Generated 3D Gaussian Splattings and rendered views from diverse texts by VideoRFSplat. VideoRFSplat directly generates realistic 3D scenes from text without SDS ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |
| Table 1. Quantitative results on T3Bench [23]. VideoRFSplat outperforms all baselines without SDS++ refinement. | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Table 3. Ablation study on asynchronous sampling. We also report CLIP scores on multi-view images to assess text alignment of not lifted images to ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Furthermore, we propose an asynchronous adaptation of Classifier-Free Guidance (CFG) that enables the clearer pose to better guide multi-view image generation. | Table 2. Quantitative results on MVImgNet [84] and DL3DV [41] validation sets. VideoRFSplat achieves the higher performance across all metrics without SDS++ refinement. sess ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 8 (Figure/Table caption), p. 5 (5. Experimental Results), p. 1 (Figure/Table caption), p. 6 (5.1. Experimental Setups) |
| Primary metric/result | Table 5. VideoRFSplat outperforms other methods in FID-8K (43.07), translation error (0.063), rotation error (0.4223), and CLIPScore (31.1). These results confirm that VideoRFSplat generates ... | numeric claim only at cited anchor | p. 8 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 6 / 5.1. Experimental Setups - extractive body cue:** We resize all frames to 320×512 during training, setting K = 8, as in SplatFlow [20] and Director3D [35].
- **p. 7 / Method - extractive body cue:** 4) 35.3 5.64 33.3 32.8 δ = 0.1, w/o modified CFG 34.0 4.43 33.8 33.2 δ = 0.2, w/o modified CFG 34.1 4.39 34.0 33.2 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 3. Failure analysis of synchronized sampling and the effectiveness of asynchronous sampling. (Left) Early in sampling (t > 0.85), synchronous sampling induces excessive ... | p. 5 (Figure/Table caption) |
| body limitation/failure cue | Figure 7. Architecture Comparison. For each example, Left: chan- nel concat architecture (SplatFlow). Right: our architecture. framed key objects. We hypothesize that uncertainty in ... | p. 8 (Figure/Table caption) |
| body limitation/failure cue | Figure 4. Asynchrnous schedule (δ = 0.2). During sampling, we denoise the pose modality faster than im- ages, as it is robust to fast ... | p. 5 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Light blue computer mouse with green light . | p. 6 (5.1. Experimental Setups) |
| This loss enables vector field prediction even with different timesteps for pose and image modalities. | p. 5 (4.1. Dual-Stream Pose-Video Joint Model) |
| In implementation, both modalities start from Gaussian noise, with the pose's sampling timestep adjusted as tR = max(tI -δ, 0) as shown in Fig. | p. 5 (4.1. Dual-Stream Pose-Video Joint Model) |
| Moreover, asynchronous sampling remains robustly effective even with 200 sampling steps. | p. 7 (Method) |
| In addition to metrics for T3Bench, we compute CLIP scores on generated multi-view images to assess text alignment for unlifted images to 3DGS. | p. 7 (Method) |
| Our proposed training scheme, which divides timesteps, demonstrates slightly better results. | p. 8 (Method) |
| This suggests that our approach of dividing timesteps during training is not detrimental and achieves comparable or marginally improved performance. | p. 8 (Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Failure analysis of synchronized sampling and the effectiveness of asynchronous sampling. (Left) Early in sampling (t > 0.85), synchronous sampling induces excessive oscillations ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 7. Architecture Comparison. For each example, Left: chan- nel concat architecture (SplatFlow). Right: our architecture. framed key objects. We hypothesize that uncertainty in early ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. Asynchrnous schedule (δ = 0.2). During sampling, we denoise the pose modality faster than im- ages, as it is robust to fast denoising. ...

- **Evidence anchors reviewed:** datasets p. 6 (5.1. Experimental Setups), p. 6 (5.1. Experimental Setups), metrics p. 8 (Figure/Table caption), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 5 (5. Experimental Results), p. 6 (5.1. Experimental Setups), baselines p. 7 (Figure/Table caption), p. 5 (5. Experimental Results), p. 1 (Figure/Table caption), p. 6 (5.1. Experimental Setups), p. 8 (Figure/Table caption), p. 8 (Figure/Table caption), results p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 8 (Figure/Table caption), p. 5 (5. Experimental Results), p. 1 (Figure/Table caption), p. 6 (5.1. Experimental Setups).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
