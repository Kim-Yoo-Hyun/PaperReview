# Evaluation - Spatial Understanding from Videos: Structured Prompts Meet Simulation Data

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=SBYCu5uJJf; PDF retrieval source: https://arxiv.org/pdf/2506.03642. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (5 Experiments), p. 7 (5 Experiments), p. 8 (5 Experiments), p. 9 (Figure/Table caption), p. 9 (5 Experiments), p. 6 (5 Experiments)): Results show that this strategy achieves improved performance, surpassing the original Qwen2.5-VL-7B baseline, suggesting that spatial fine-tuning can be harmonized with broader capabilities through data balancing.

## Evaluation Body Digest

- **p. 9 / 5 Experiments - extractive body cue:** Importantly, both datasets and the VSI-Bench benchmark originate from the same source (i.e., ScanNet [31]), resulting in minimal data discrepancy.
- **p. 8 / 5 Experiments - extractive body cue:** These results validate the robustness of our approach and confirm its applicability across diverse spatial tasks and datasets.
- **p. 8 / 5 Experiments - extractive body cue:** To investigate whether enhancing visualspatial capabilities via fine-tuning adversely impacts a model's general performance, we conducted evaluations on MVBench [52] and Video-MME [53], two broad ...
- **p. 9 / 5 Experiments - extractive body cue:** As shown in Table 3, fine-tuning on either of these datasets results in lower performance compared to ScanForgeQA, and even reduces accuracy on tasks involving ...
- **p. 6 / 5 Experiments - extractive body cue:** The experimental settings (including benchmarks, baselines, etc.) and more experimental results can be found in the Appendix A and B.
- **p. 7 / 5 Experiments - extractive body cue:** Consequently, we adopted the textual description format in subsequent experiments as the default scene representation.
- **p. 7 / 5 Experiments - extractive body cue:** Method Room Size Avg Qwen2.5-VL-7B 38.9 37.2 +SQA3D 38.8 38.9 +ScanQA 38.5 39.1 +ScanForgeQA 44.9 43.3 Qwen2.5-VL-72B 49.8 39.2 +CoT-Question 50.6 41.3 +CoT-Scene 52.1 42.7 ...
- **p. 7 / 5 Experiments - extractive body cue:** Method OpenEQA ScanQA SQA3D Acc/Score BLEU-1 EM-1 Qwen2.5-VL-7B 50.1/3.1 32.5 17.2 +SpatialMind 53.7/3.2 33.1 19.8 +ScanForgeQA 56.2/3.3 34.8 23.3 +Both 58.6/3.5 37.9 24.5 Qwen2.5-VL-72B 53.8/3.2 ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5 Experiments (p. 6); 5 Experiments (p. 16); A.1 Benchmarks (p. 16); B More Experimental Results (p. 16); A Experimental Settings (p. 17); A.1 Benchmarks (p. 17); B More Experimental Results (p. 19).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Results show that this strategy achieves improved performance, surpassing the original Qwen2.5-VL-7B baseline, suggesting that spatial fine-tuning can be harmonized with broader capabilities through ... | p. 8 (5 Experiments) |
| 5 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Across all models, a consistent trend emerges: the +Des variant outperforms others, followed by +Grid, while +Map yields the least improvement. | p. 7 (5 Experiments) |
| 5 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | The results, reported in the "+Both" row of Table 1, show consistent performance improvements across all evaluated models. | p. 8 (5 Experiments) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 6: Two examples from VSI-Bench comparing predictions from Qwen2.5-VL-7B and Ours. On prompting strategy. To isolate the contributions of each component in the ... | p. 9 (Figure/Table caption) |
| 5 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our method consistently outperforms the baseline across all settings, with performance further improving as the number of frames and resolution increase. | p. 9 (5 Experiments) |

## Dataset / Benchmark Role

- **p. 9 / 5 Experiments - extractive body cue:** Importantly, both datasets and the VSI-Bench benchmark originate from the same source (i.e., ScanNet [31]), resulting in minimal data discrepancy.
- **p. 8 / 5 Experiments - extractive body cue:** These results validate the robustness of our approach and confirm its applicability across diverse spatial tasks and datasets.
- **p. 8 / 5 Experiments - extractive body cue:** To investigate whether enhancing visualspatial capabilities via fine-tuning adversely impacts a model's general performance, we conducted evaluations on MVBench [52] and Video-MME [53], two broad ...
- **p. 9 / 5 Experiments - extractive body cue:** As shown in Table 3, fine-tuning on either of these datasets results in lower performance compared to ScanForgeQA, and even reduces accuracy on tasks involving ...
- **p. 6 / 5 Experiments - extractive body cue:** The experimental settings (including benchmarks, baselines, etc.) and more experimental results can be found in the Appendix A and B.
- **p. 7 / 5 Experiments - extractive body cue:** Consequently, we adopted the textual description format in subsequent experiments as the default scene representation.
- **p. 7 / 5 Experiments - extractive body cue:** Method Room Size Avg Qwen2.5-VL-7B 38.9 37.2 +SQA3D 38.8 38.9 +ScanQA 38.5 39.1 +ScanForgeQA 44.9 43.3 Qwen2.5-VL-72B 49.8 39.2 +CoT-Question 50.6 41.3 +CoT-Scene 52.1 42.7 ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive body cue:** Figure 1: Illustration of our SpatailMind prompting strategy. for real-world deployment. In this context, we further investigate whether purely vision-based inputs can provide a more ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2: The pipeline of ScanForgeQA data construction. Separation. We modify existing scene datasets to leverage available resources effectively. Specifi- cally, we utilize the 3D-FRONT ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: Effects of different scene expression. Spatial Reasoning. This category targets inter- object spatial relationships, requiring models to infer positional and geometric properties such ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Performance comparison on VSI-Bench. † indicates results on VSI-Bench (tiny) set.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Performance comparison on the EM-EQA subset of OpenEQA and the validation set of ScanQA and SQA3D.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3: Effects of different fine- tuning data and prompting strategy.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: Performance of Qwen2.5-VL-7B on MVBench and Video-MME. 8 16 24 32 Frame 128
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Ablation study of Qwen2.5-VL-7B under varying numbers of frames and resolution. across a range of VLMs, varying in architectures, parameter size, and openness ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Importantly, both datasets and the VSI-Bench benchmark originate from the same source (i.e., ScanNet [31]), resulting in minimal data discrepancy. | embodiment, simulator version and control stack | p. 9 (5 Experiments), p. 8 (5 Experiments) |
| Task/environment | These results validate the robustness of our approach and confirm its applicability across diverse spatial tasks and datasets. | reset, timeout, object/scene variation | p. 8 (5 Experiments), p. 8 (5 Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 1 (Abstract), p. 1 (1 Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (1 Introduction), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Method OpenEQA ScanQA SQA3D Acc/Score BLEU-1 EM-1 Qwen2.5-VL-7B 50.1/3.1 32.5 17.2 +SpatialMind 53.7/3.2 33.1 19.8 +ScanForgeQA 56.2/3.3 34.8 23.3 +Both 58.6/3.5 37.9 24.5 Qwen2.5-VL-72B ... | definition/direction/unit from same section | p. 7 (5 Experiments) |
| Our enhanced variant, benefiting from both structured prompting and spatially grounded fine-tuning, demonstrates notable improvements in accuracy and reasoning robustness. | definition/direction/unit from same section | p. 9 (5 Experiments) |
| Base +ScanForgeQA +5% +10% 69.0 69.5 70.0 70.5 71.0 71.5 72.0 72.5 Accuracy (%) MVBench Video-MME(w sub) Figure 4: Performance of Qwen2.5-VL-7B on MVBench ... | definition/direction/unit from same section | p. 8 (5 Experiments) |
| As shown in Table 3, fine-tuning on either of these datasets results in lower performance compared to ScanForgeQA, and even reduces accuracy on tasks ... | definition/direction/unit from same section | p. 9 (5 Experiments) |
| This contrast underscores the potential of VLMs to complement human perception in spatial tasks. | definition/direction/unit from same section | p. 8 (5 Experiments) |
| Figure 7: A complete example illustrating the visual prompting process with intermediate outputs. such as "What is between the sofa and the table?" or ... | definition/direction/unit from same section | p. 19 (Figure/Table caption) |
| Figure 8: Distribution of room types in the ScanForgeQA dataset. are consistent with those reported in our main analysis, further reinforcing the effectiveness and ... | definition/direction/unit from same section | p. 20 (Figure/Table caption) |
| How do SpatialMind and ScanForgeQA impact VLM performance? | definition/direction/unit from same section | p. 7 (5 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our method consistently outperforms the baseline across all settings, with performance further improving as the number of frames and resolution increase. | comparison identity and matched condition | p. 9 (5 Experiments) |
| The experimental settings (including benchmarks, baselines, etc.) and more experimental results can be found in the Appendix A and B. | comparison identity and matched condition | p. 6 (5 Experiments) |
| Across all models, a consistent trend emerges: the +Des variant outperforms others, followed by +Grid, while +Map yields the least improvement. | comparison identity and matched condition | p. 7 (5 Experiments) |
| For instance, Qwen2.5-VL-7B gains 6.1% from fine-tuning, compared to only 2.0% from prompting. | comparison identity and matched condition | p. 8 (5 Experiments) |
| Results show that this strategy achieves improved performance, surpassing the original Qwen2.5-VL-7B baseline, suggesting that spatial fine-tuning can be harmonized with broader capabilities through ... | comparison identity and matched condition | p. 8 (5 Experiments) |
| 5.3 Qualitative Analysis In Figure 6, we presented two illustrative examples from VSI-Bench, comparing predictions from the baseline Qwen2.5-VL-7B and our enhanced variant (+Both). | comparison identity and matched condition | p. 9 (5 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 6: Two examples from VSI-Bench comparing predictions from Qwen2.5-VL-7B and Ours. On prompting strategy. To isolate the contributions of each component in the ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |
| Figure 5: Ablation study of Qwen2.5-VL-7B under varying numbers of frames and resolution. across a range of VLMs, varying in architectures, parameter size, and ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| 5.2 Ablation Study In this section, we explored the impact of various design choices, including prompting strategies, fine-tuning datasets, frame sampling strategies, and input ... | component/input/data sensitivity | p. 8 (5 Experiments) |
| Our enhanced variant, benefiting from both structured prompting and spatially grounded fine-tuning, demonstrates notable improvements in accuracy and reasoning robustness. | component/input/data sensitivity | p. 9 (5 Experiments) |
| Across all models, a consistent trend emerges: the +Des variant outperforms others, followed by +Grid, while +Map yields the least improvement. | component/input/data sensitivity | p. 7 (5 Experiments) |
| Figure 1: Illustration of our SpatailMind prompting strategy. for real-world deployment. In this context, we further investigate whether purely vision-based inputs can provide a ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions are summarized as follows: • We introduce SpatialMind, a spatial prompting strategy that decomposes spatial reasoning into structured steps, enabling pre-trained VLMs ... | Results show that this strategy achieves improved performance, surpassing the original Qwen2.5-VL-7B baseline, suggesting that spatial fine-tuning can be harmonized with broader capabilities through ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (5 Experiments), p. 7 (5 Experiments), p. 8 (5 Experiments), p. 9 (Figure/Table caption), p. 9 (5 Experiments), p. 6 (5 Experiments) |
| Primary metric/result | Across all models, a consistent trend emerges: the +Des variant outperforms others, followed by +Grid, while +Map yields the least improvement. | numeric claim only at cited anchor | p. 7 (5 Experiments) |

- Numeric sentences retained from the body:
- **p. 8 / 5 Experiments - extractive body cue:** 8 16 24 32 Frame 128 256 384 512 Resolution 4 5 6 7 Gain (+Both - Base) 4.5 5.0 5.5 6.0 6.5 Figure 5: ...
- **p. 5 / A B - extractive body cue:** We define a circular trajectory centered in the room at a height of approximately 1.5 meters, corresponding to typical adult eye level.
- **p. 5 / A B - extractive body cue:** An image is captured every 5 degrees of rotation, resulting in 72 frames per orbit scan.
- **p. 5 / A B - extractive body cue:** For each path, the camera first performs a 360-degree rotation at the starting point, capturing an image every 12 degrees (30 images total).
- **p. 5 / A B - extractive body cue:** It then traverses the path toward the destination, during which 12 frames are uniformly sampled.
- **p. 6 / A B - extractive body cue:** In total, 72 frames are recorded per path.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In Case (a), Qwen2.5-VL-7B fails to produce the correct directional prediction, likely due to its limited capacity for 3D spatial reasoning. | p. 9 (5 Experiments) |
| body limitation/failure cue | Case (b) involves a simpler spatial reasoning task, however, Qwen2.5-VL-7B still fails, potentially due to insufficient object localization. | p. 9 (5 Experiments) |
| body limitation/failure cue | These results validate the robustness of our approach and confirm its applicability across diverse spatial tasks and datasets. | p. 8 (5 Experiments) |
| body limitation/failure cue | Figure 8: Distribution of room types in the ScanForgeQA dataset. are consistent with those reported in our main analysis, further reinforcing the effectiveness and ... | p. 20 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Notably, the scene description contributes more significantly to model performance than the reasoning steps, suggesting its central role in facilitating spatial understanding. | p. 9 (5 Experiments) |
| To address this, point clouds have become a mainstream representation for 3D scene understanding due to their ability to encode rich geometric information [16, ... | p. 1 (1 Introduction) |
| This framework combines SpatialMind, a structured prompting strategy that decomposes complex scenes and questions into interpretable reasoning steps, with ScanForgeQA, a scalable question-answering dataset ... | p. 1 (Abstract) |
| Our contributions are summarized as follows: • We introduce SpatialMind, a spatial prompting strategy that decomposes spatial reasoning into structured steps, enabling pre-trained VLMs ... | p. 2 (1 Introduction) |
| We randomly select two objects as the navigation start and end points and compute the shortest path between them on the mesh. | p. 5 (A B) |
| Additional implementation details are provided in the Appendix C. | p. 6 (A B) |
| For distancerelated questions, we compute Euclidean distances between object centroids in the global 3D coordinate space. | p. 6 (A B) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 5 Experiments - extractive body cue:** In Case (a), Qwen2.5-VL-7B fails to produce the correct directional prediction, likely due to its limited capacity for 3D spatial reasoning.
- **p. 9 / 5 Experiments - extractive body cue:** Case (b) involves a simpler spatial reasoning task, however, Qwen2.5-VL-7B still fails, potentially due to insufficient object localization.
- **p. 8 / 5 Experiments - extractive body cue:** These results validate the robustness of our approach and confirm its applicability across diverse spatial tasks and datasets.
- **p. 20 / Figure/Table caption - extractive body cue:** Figure 8: Distribution of room types in the ScanForgeQA dataset. are consistent with those reported in our main analysis, further reinforcing the effectiveness and generalizability ...

- **Evidence anchors reviewed:** datasets p. 9 (5 Experiments), p. 8 (5 Experiments), p. 8 (5 Experiments), p. 9 (5 Experiments), p. 6 (5 Experiments), p. 7 (5 Experiments), metrics p. 7 (5 Experiments), p. 9 (5 Experiments), p. 8 (5 Experiments), p. 9 (5 Experiments), p. 8 (5 Experiments), p. 19 (Figure/Table caption), baselines p. 9 (5 Experiments), p. 6 (5 Experiments), p. 7 (5 Experiments), p. 8 (5 Experiments), p. 8 (5 Experiments), p. 9 (5 Experiments), results p. 8 (5 Experiments), p. 7 (5 Experiments), p. 8 (5 Experiments), p. 9 (Figure/Table caption), p. 9 (5 Experiments), p. 6 (5 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
