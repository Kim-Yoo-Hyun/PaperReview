# Evaluation - ZeroKey: Point-Level Reasoning and Zero-Shot 3D Keypoint Detection from Large Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Gong_ZeroKey_Point-Level_Reasoning_and_Zero-Shot_3D_Keypoint_Detection_from_Large_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Gong_ZeroKey_Point-Level_Reasoning_and_Zero-Shot_3D_Keypoint_Detection_from_Large_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (Figure/Table caption), p. 7 (6.3. Quantitative and Qualitative Analysis), p. 1 (Figure/Table caption), p. 7 (6.3. Quantitative and Qualitative Analysis), p. 6 (Figure/Table caption), p. 3 (Figure/Table caption)): Figure 7. Comparison of the performance across different config- urations: (blue) our original method; (red) results with a Global Text prompt; (orange, purple, brown) results using different ren- dering; (green) ...

## Evaluation Body Digest

- **p. 6 / 6.1. Setup and Dataset - extractive body cue:** We evaluate our method using the KeypointNet dataset.
- **p. 6 / 6.1. Setup and Dataset - extractive body cue:** We also stick to the same three classes of the dataset for evaluation: airplane, chair, and table.
- **p. 7 / 6.3. Quantitative and Qualitative Analysis - extractive body cue:** Furthermore, our method achieves IoU levels comparable to those of reference-based Few-Shot and fully supervised methods tailored for this dataset, such as B2-3D [49].
- **p. 8 / 6.3. Quantitative and Qualitative Analysis - extractive body cue:** These findings show the need for an MLLM backbone trained with point-level tasks for precise keypoint detection, underscore the potential of point-level reasoning as a ...
- **p. 6 / 6.1. Setup and Dataset - extractive body cue:** [55], which computes the Intersection over Union (IoU) between predicted keypoints and ground-truth keypoints from the KeypointNet dataset, using varying distance thresholds.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5. We show through a quantitative study that "salient" points are retrieved with higher accuracy than "non-salient" ones, regardless of the distance threshold used. ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Comparison of IoU between the predicted and ground-truth keypoints from KeypointNet using different methods across various geodesic distance thresholds. The bold text indicates ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Zero-shot 3D Keypoint Detection. Without any ground truth labels or supervised training, our method leverages the point-level reasoning embedded within MLLMs to extract ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 6. Experiments (p. 6); 6.1. Setup and Dataset (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 7. Comparison of the performance across different config- urations: (blue) our original method; (red) results with a Global Text prompt; (orange, purple, brown) ... | p. 8 (Figure/Table caption) |
| 6.3. Quantitative and Qualitative Analysis | SYSTEM / EVALUATION SCOPE UNRESOLVED | Our KeypointNet evaluation shows (see Table.1) that our Zero-Shot method significantly outperforms MLLM-based baselines (PaliGemma 2[45], GPT-4o, CLIP-DINOiser [50]) across all distance thresholds. | p. 7 (6.3. Quantitative and Qualitative Analysis) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 1. Zero-shot 3D Keypoint Detection. Without any ground truth labels or supervised training, our method leverages the point-level reasoning embedded within MLLMs to ... | p. 1 (Figure/Table caption) |
| 6.3. Quantitative and Qualitative Analysis | SYSTEM / EVALUATION SCOPE UNRESOLVED | Furthermore, our method achieves IoU levels comparable to those of reference-based Few-Shot and fully supervised methods tailored for this dataset, such as B2-3D [49]. | p. 7 (6.3. Quantitative and Qualitative Analysis) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 5. We show through a quantitative study that "salient" points are retrieved with higher accuracy than "non-salient" ones, regardless of the distance threshold ... | p. 6 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 6.1. Setup and Dataset - extractive body cue:** We evaluate our method using the KeypointNet dataset.
- **p. 6 / 6.1. Setup and Dataset - extractive body cue:** We also stick to the same three classes of the dataset for evaluation: airplane, chair, and table.
- **p. 7 / 6.3. Quantitative and Qualitative Analysis - extractive body cue:** Furthermore, our method achieves IoU levels comparable to those of reference-based Few-Shot and fully supervised methods tailored for this dataset, such as B2-3D [49].
- **p. 8 / 6.3. Quantitative and Qualitative Analysis - extractive body cue:** These findings show the need for an MLLM backbone trained with point-level tasks for precise keypoint detection, underscore the potential of point-level reasoning as a ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Zero-shot 3D Keypoint Detection. Without any ground truth labels or supervised training, our method leverages the point-level reasoning embedded within MLLMs to extract ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. ZeroKey Pipeline. Our proposed ZeroKey employs MLLM Molmo for zero-shot keypoint detection on 3D objects by 1) rendering multiple views for a given ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. The number of rendered views versus the detected key- points after aggregation. This figure shows how varying the num- ber of rendered views ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4. We ask Molmo to describe the green point, and using this as a prompt ZeroKey predicts the blue point. We show that salient ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5. We show through a quantitative study that "salient" points are retrieved with higher accuracy than "non-salient" ones, regardless of the distance threshold used. ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Comparison of IoU between the predicted and ground-truth keypoints from KeypointNet using different methods across various geodesic distance thresholds. The bold text indicates ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6. We compare against baselines CLIP-DINOiser and Red- Circle. While both baselines identify some prominent regions, they fall in accurately localizing keypoints according to ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 7. Comparison of the performance across different config- urations: (blue) our original method; (red) results with a Global Text prompt; (orange, purple, brown) results ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We evaluate our method using the KeypointNet dataset. | embodiment, simulator version and control stack | p. 6 (6.1. Setup and Dataset), p. 6 (6.1. Setup and Dataset) |
| Task/environment | We also stick to the same three classes of the dataset for evaluation: airplane, chair, and table. | reset, timeout, object/scene variation | p. 6 (6.1. Setup and Dataset), p. 7 (6.3. Quantitative and Qualitative Analysis) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 7 (Method), p. 4 (4.2. Prompting Molmo to Detect 2D Keypoints) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (4.2. Prompting Molmo to Detect 2D Keypoints), p. 7 (Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| [55], which computes the Intersection over Union (IoU) between predicted keypoints and ground-truth keypoints from the KeypointNet dataset, using varying distance thresholds. | definition/direction/unit from same section | p. 6 (6.1. Setup and Dataset) |
| Figure 5. We show through a quantitative study that "salient" points are retrieved with higher accuracy than "non-salient" ones, regardless of the distance threshold ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Table 1. Comparison of IoU between the predicted and ground-truth keypoints from KeypointNet using different methods across various geodesic distance thresholds. The bold text ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Furthermore, our method achieves IoU levels comparable to those of reference-based Few-Shot and fully supervised methods tailored for this dataset, such as B2-3D [49]. | definition/direction/unit from same section | p. 7 (6.3. Quantitative and Qualitative Analysis) |
| These findings show the need for an MLLM backbone trained with point-level tasks for precise keypoint detection, underscore the potential of point-level reasoning as ... | definition/direction/unit from same section | p. 8 (6.3. Quantitative and Qualitative Analysis) |
| Figure 1. Zero-shot 3D Keypoint Detection. Without any ground truth labels or supervised training, our method leverages the point-level reasoning embedded within MLLMs to ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 2. ZeroKey Pipeline. Our proposed ZeroKey employs MLLM Molmo for zero-shot keypoint detection on 3D objects by 1) rendering multiple views for a ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| While both baselines identify some prominent regions, they fall in accurately localizing keypoints according to the text prompt. | definition/direction/unit from same section | p. 8 (6.3. Quantitative and Qualitative Analysis) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 1. Zero-shot 3D Keypoint Detection. Without any ground truth labels or supervised training, our method leverages the point-level reasoning embedded within MLLMs to ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| Our KeypointNet evaluation shows (see Table.1) that our Zero-Shot method significantly outperforms MLLM-based baselines (PaliGemma 2[45], GPT-4o, CLIP-DINOiser [50]) across all distance thresholds. | comparison identity and matched condition | p. 7 (6.3. Quantitative and Qualitative Analysis) |
| Side-by-side comparisons between ground truth keypoints and our Zero-Shot predictions, a figure of GPT-4o fails to precisely locate the keypoint, and a comparison of ... | comparison identity and matched condition | p. 7 (6.3. Quantitative and Qualitative Analysis) |
| We compare against baselines CLIP-DINOiser and RedCircle. | comparison identity and matched condition | p. 8 (6.3. Quantitative and Qualitative Analysis) |
| While both baselines identify some prominent regions, they fall in accurately localizing keypoints according to the text prompt. | comparison identity and matched condition | p. 8 (6.3. Quantitative and Qualitative Analysis) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| This provides strong evidence for our claim that the pixel-level annotations used to train MLLMs can be leveraged to both extract and name salient ... | component/input/data sensitivity | p. 7 (6.3. Quantitative and Qualitative Analysis) |
| Figure 1. Zero-shot 3D Keypoint Detection. Without any ground truth labels or supervised training, our method leverages the point-level reasoning embedded within MLLMs to ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |
| Figure 7. Comparison of the performance across different config- urations: (blue) our original method; (red) results with a Global Text prompt; (orange, purple, brown) ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Inspired by these recent developments, we propose investigating MLLMs endowed with point-level reasoning in the context of 3D shape understanding and specifically for zero-shot ... | Figure 7. Comparison of the performance across different config- urations: (blue) our original method; (red) results with a Global Text prompt; (orange, purple, brown) ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (Figure/Table caption), p. 7 (6.3. Quantitative and Qualitative Analysis), p. 1 (Figure/Table caption), p. 7 (6.3. Quantitative and Qualitative Analysis), p. 6 (Figure/Table caption), p. 3 (Figure/Table caption) |
| Primary metric/result | Our KeypointNet evaluation shows (see Table.1) that our Zero-Shot method significantly outperforms MLLM-based baselines (PaliGemma 2[45], GPT-4o, CLIP-DINOiser [50]) across all distance thresholds. | numeric claim only at cited anchor | p. 7 (6.3. Quantitative and Qualitative Analysis) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 6. We compare against baselines CLIP-DINOiser and Red- Circle. While both baselines identify some prominent regions, they fall in accurately localizing keypoints according ... | p. 8 (Figure/Table caption) |
| body limitation/failure cue | Side-by-side comparisons between ground truth keypoints and our Zero-Shot predictions, a figure of GPT-4o fails to precisely locate the keypoint, and a comparison of ... | p. 7 (6.3. Quantitative and Qualitative Analysis) |
| body limitation/failure cue | Our evaluations demonstrate the efficacy of our approach and suggest that point-level reasoning is an effective way to endow MLLMs with a robust understanding ... | p. 8 (7. Conclusion and Future Work) |
| body limitation/failure cue | Figure 1. Zero-shot 3D Keypoint Detection. Without any ground truth labels or supervised training, our method leverages the point-level reasoning embedded within MLLMs to ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | Our KeypointNet evaluation shows (see Table.1) that our Zero-Shot method significantly outperforms MLLM-based baselines (PaliGemma 2[45], GPT-4o, CLIP-DINOiser [50]) across all distance thresholds. | p. 7 (6.3. Quantitative and Qualitative Analysis) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| [55], which computes the Intersection over Union (IoU) between predicted keypoints and ground-truth keypoints from the KeypointNet dataset, using varying distance thresholds. | p. 6 (6.1. Setup and Dataset) |
| The σ is set to h 3 in our implementation. | p. 5 (4.3. Zero-Shot 3D Keypoint Detection) |
| A straightforward method is to compute the weighted mean of the points ˆPi = PM j=1 Wi,jPi,j PM j=1 Wij . | p. 5 (4.3. Zero-Shot 3D Keypoint Detection) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6. We compare against baselines CLIP-DINOiser and Red- Circle. While both baselines identify some prominent regions, they fall in accurately localizing keypoints according to ...
- **p. 7 / 6.3. Quantitative and Qualitative Analysis - extractive body cue:** Side-by-side comparisons between ground truth keypoints and our Zero-Shot predictions, a figure of GPT-4o fails to precisely locate the keypoint, and a comparison of our ...
- **p. 8 / 7. Conclusion and Future Work - extractive body cue:** Our evaluations demonstrate the efficacy of our approach and suggest that point-level reasoning is an effective way to endow MLLMs with a robust understanding of ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Zero-shot 3D Keypoint Detection. Without any ground truth labels or supervised training, our method leverages the point-level reasoning embedded within MLLMs to extract ...
- **p. 7 / 6.3. Quantitative and Qualitative Analysis - extractive body cue:** Our KeypointNet evaluation shows (see Table.1) that our Zero-Shot method significantly outperforms MLLM-based baselines (PaliGemma 2[45], GPT-4o, CLIP-DINOiser [50]) across all distance thresholds.

- **Evidence anchors reviewed:** datasets p. 6 (6.1. Setup and Dataset), p. 6 (6.1. Setup and Dataset), p. 7 (6.3. Quantitative and Qualitative Analysis), p. 8 (6.3. Quantitative and Qualitative Analysis), metrics p. 6 (6.1. Setup and Dataset), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 7 (6.3. Quantitative and Qualitative Analysis), p. 8 (6.3. Quantitative and Qualitative Analysis), p. 1 (Figure/Table caption), baselines p. 1 (Figure/Table caption), p. 7 (6.3. Quantitative and Qualitative Analysis), p. 7 (6.3. Quantitative and Qualitative Analysis), p. 8 (6.3. Quantitative and Qualitative Analysis), p. 8 (6.3. Quantitative and Qualitative Analysis), results p. 8 (Figure/Table caption), p. 7 (6.3. Quantitative and Qualitative Analysis), p. 1 (Figure/Table caption), p. 7 (6.3. Quantitative and Qualitative Analysis), p. 6 (Figure/Table caption), p. 3 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
