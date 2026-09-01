# Evaluation - SAM 2: Segment Anything in Images and Videos

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (42 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2408.00714; PDF retrieval source: https://arxiv.org/pdf/2408.00714. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 31 (dataset), p. 32 (dataset), p. 32 (dataset)): We report the performance of prior works as evaluated by the LVOSv2 authors.

## Evaluation Body Digest

- **p. 30 / dataset - extractive PDF cue:** Sparse Validation videos on egocentric cameras 1185 1185 327,080 9,035 VIPSeg (Miao et al., 2022) VIPSeg Panoptic Large scale and real world scenarios for video ...
- **p. 32 / dataset - extractive PDF cue:** The video benchmark suite included domains such as driving data, microscopy, egocentric video, robotic surgery.
- **p. 30 / dataset - extractive PDF cue:** Sparse All 12 12 4,012 412 LVOSv2 (Hong et al., 2024) LVOSv2 Long videos Long-term video object segmentation benchmark, on average 1.14 minutes Dense Validation ...
- **p. 33 / dataset - extractive PDF cue:** The dataset was designed for the PVS task.
- **p. 31 / dataset - extractive PDF cue:** LVOS val Method J &F J F DEVA (Cheng et al., 2023b) 55.9 51.1 60.7 DDMemory (Hong et al., 2023) 60.7 55.0 66.3 Cutie-base (Cheng ...
- **p. 31 / dataset - extractive PDF cue:** LVOSv2 val Method J &F Js Fs Ju Fu STCN (Cheng et al., 2021a) 60.6 57.2 64.0 57.5 63.8 RDE (Li et al., 2022a) 62.2 ...
- **p. 32 / dataset - extractive PDF cue:** SAM 2 was evaluated on the same suite of image benchmarks as Kirillov et al.
- **p. 33 / 3. Who funded the creation of the dataset? - extractive PDF cue:** The dataset was funded by Meta FAIR.

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 논문이 정의한 robot/embodied environment.
- **Input boundary:** 논문이 명시한 observation과 task input.
- **Output/decision under evaluation:** paper-specific output/action.
- **Primary target:** primary task objective와 closed-loop behavior.
- **Detected evaluation headings:** dataset (p. 30); 3. Who funded the creation of the dataset? (p. 33).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| dataset | SYSTEM / EVALUATION SCOPE UNRESOLVED | We report the performance of prior works as evaluated by the LVOSv2 authors. | p. 31 (dataset) |
| dataset | SYSTEM / EVALUATION SCOPE UNRESOLVED | Risks and harms In Section E.1.1 of the main text we analyze SAM 2 performance on people across demographic groups. | p. 32 (dataset) |
| dataset | SYSTEM / EVALUATION SCOPE UNRESOLVED | G: We use G for evaluation on YTVOS 2019 for the semi-supervised VOS task. mIoU: We evaluate performance using mIoU for the promptable image ... | p. 32 (dataset) |

## Dataset / Benchmark Role

- **p. 30 / dataset - extractive PDF cue:** Sparse Validation videos on egocentric cameras 1185 1185 327,080 9,035 VIPSeg (Miao et al., 2022) VIPSeg Panoptic Large scale and real world scenarios for video ...
- **p. 32 / dataset - extractive PDF cue:** The video benchmark suite included domains such as driving data, microscopy, egocentric video, robotic surgery.
- **p. 30 / dataset - extractive PDF cue:** Sparse All 12 12 4,012 412 LVOSv2 (Hong et al., 2024) LVOSv2 Long videos Long-term video object segmentation benchmark, on average 1.14 minutes Dense Validation ...
- **p. 33 / dataset - extractive PDF cue:** The dataset was designed for the PVS task.
- **p. 31 / dataset - extractive PDF cue:** LVOS val Method J &F J F DEVA (Cheng et al., 2023b) 55.9 51.1 60.7 DDMemory (Hong et al., 2023) 60.7 55.0 66.3 Cutie-base (Cheng ...
- **p. 31 / dataset - extractive PDF cue:** LVOSv2 val Method J &F Js Fs Ju Fu STCN (Cheng et al., 2021a) 60.6 57.2 64.0 57.5 63.8 RDE (Li et al., 2022a) 62.2 ...
- **p. 32 / dataset - extractive PDF cue:** SAM 2 was evaluated on the same suite of image benchmarks as Kirillov et al.
- **p. 33 / 3. Who funded the creation of the dataset? - extractive PDF cue:** The dataset was funded by Meta FAIR.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- figure/table caption cue 없음

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Sparse Validation videos on egocentric cameras 1185 1185 327,080 9,035 VIPSeg (Miao et al., 2022) VIPSeg Panoptic Large scale and real world scenarios for ... | embodiment, simulator version and control stack | p. 30 (dataset), p. 32 (dataset) |
| Task/environment | The video benchmark suite included domains such as driving data, microscopy, egocentric video, robotic surgery. | reset, timeout, object/scene variation | p. 32 (dataset), p. 30 (dataset) |
| Observation/sensor | 논문이 명시한 observation과 task input | calibration, preprocessing, privileged input | p. 1 (1 Introduction), p. 1 (1 Introduction) |
| Output/decision | paper-specific output/action | action frame, controller and termination | p. 27 (Method), p. 27 (Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Sparse Validation 921 921 736,030 4,426 HT1080WT cells embedded in 3D collagen type I matrices (Gómez-de Mariscal et al., 2021) HT1080WT Microscopy; cells Timelapse ... | definition/direction/unit from same section | p. 30 (dataset) |
| We report the performance of prior works as evaluated by the LVOSv2 authors. | definition/direction/unit from same section | p. 31 (dataset) |
| Risks and harms In Section E.1.1 of the main text we analyze SAM 2 performance on people across demographic groups. | definition/direction/unit from same section | p. 32 (dataset) |
| G: We use G for evaluation on YTVOS 2019 for the semi-supervised VOS task. mIoU: We evaluate performance using mIoU for the promptable image ... | definition/direction/unit from same section | p. 32 (dataset) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We report the performance of prior works as evaluated by the LVOSv2 authors. | comparison identity and matched condition | p. 31 (dataset) |
| We evaluated prior works on SA-V using their open-sourced code and checkpoints. | comparison identity and matched condition | p. 31 (dataset) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| no ablation sentence selected | not reported; proposed stress test only | verify ablation section |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We introduce the Segment Anything Model 2 (SAM 2), a unified model for video and image segmentation (we consider an image as a single-frame ... | We report the performance of prior works as evaluated by the LVOSv2 authors. | PDF body cue; verify exact table/figure and matched conditions | p. 31 (dataset), p. 32 (dataset), p. 32 (dataset) |
| Primary metric/result | Risks and harms In Section E.1.1 of the main text we analyze SAM 2 performance on people across demographic groups. | numeric claim only at cited anchor | p. 32 (dataset) |

- Numeric sentences retained from the body:
- **p. 32 / dataset - extractive PDF cue:** Cost and impact of compute The released SAM 2 was trained on 256 A100 GPUs for 108 hours.
- **p. 27 / Method - extractive PDF cue:** SAM 2 (Hiera-B+) trained only on SA-1B outperforms SAM (ViT-H) on 1-click accuracy, and both SAM (ViT-H) and HQ-SAM (ViT-H) on 5-click accuracy while being ...
- **p. 27 / Method - extractive PDF cue:** SAM 2 (Hiera-L) further improves the 1-click accuracy by 1 point on average, but trading off speed.
- **p. 27 / Method - extractive PDF cue:** Despite being slower than Hiera-B+, it is still 3.4x faster than SAM (ViT-H) and 1.5x faster than SAM (ViT-B).

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We leveraged our online model in the loop setup to enable this, requesting annotators to use SAM 2 interactively to identify failure modes and ... | p. 21 (C Limitations) |
| body limitation/failure cue | If the ground-truth does not contain a mask for a frame, we do not supervise any of the mask outputs (but always supervise the ... | p. 18 (C Limitations) |
| body limitation/failure cue | The model may fail to segment objects across shot changes and can lose track of or confuse objects in crowded scenes, after long occlusions ... | p. 16 (C Limitations) |
| body limitation/failure cue | Our memory encoder does not use an additional image encoder and instead reuses the image embeddings produced by the Hiera encoder, which are fused ... | p. 17 (C Limitations) |
| body limitation/failure cue | 3We note that this estimation does not account for the model's tracking FPS. | p. 23 (C Limitations) |
| body limitation/failure cue | If a dataset does not follow the standard VOS format, we preprocess it into a format similar to MOSE (Ding et al., 2023). | p. 24 (C Limitations) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We evaluated prior works on SA-V using their open-sourced code and checkpoints. | p. 31 (dataset) |
| The last two rows in Table 15 illustrate the benefits of training with our mix of image and video data, which boosts the average ... | p. 27 (Method) |
| We include results from SAM 2 trained only on SA-1B, SA-V and Internal data, for different encoder sizes. | p. 28 (Method) |
| 15, where the per-dataset delta in 1-click mIoU relative to SAM is color-coded to indicate the data type (image or video). | p. 28 (Method) |
| Cost and impact of compute The released SAM 2 was trained on 256 A100 GPUs for 108 hours. | p. 32 (dataset) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 21 / C Limitations - extractive PDF cue:** We leveraged our online model in the loop setup to enable this, requesting annotators to use SAM 2 interactively to identify failure modes and then ...
- **p. 18 / C Limitations - extractive PDF cue:** If the ground-truth does not contain a mask for a frame, we do not supervise any of the mask outputs (but always supervise the occlusion ...
- **p. 16 / C Limitations - extractive PDF cue:** The model may fail to segment objects across shot changes and can lose track of or confuse objects in crowded scenes, after long occlusions or ...
- **p. 17 / C Limitations - extractive PDF cue:** Our memory encoder does not use an additional image encoder and instead reuses the image embeddings produced by the Hiera encoder, which are fused with ...
- **p. 23 / C Limitations - extractive PDF cue:** 3We note that this estimation does not account for the model's tracking FPS.
- **p. 24 / C Limitations - extractive PDF cue:** If a dataset does not follow the standard VOS format, we preprocess it into a format similar to MOSE (Ding et al., 2023).

- **PDF anchors reviewed:** datasets p. 30 (dataset), p. 32 (dataset), p. 30 (dataset), p. 33 (dataset), p. 31 (dataset), p. 31 (dataset), metrics p. 30 (dataset), p. 31 (dataset), p. 32 (dataset), p. 32 (dataset), baselines p. 31 (dataset), p. 31 (dataset), results p. 31 (dataset), p. 32 (dataset), p. 32 (dataset).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
