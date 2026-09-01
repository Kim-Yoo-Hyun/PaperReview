# Evaluation - MM-Spatial: Exploring 3D Spatial Understanding in Multimodal LLMs

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Daxberger_MM-Spatial_Exploring_3D_Spatial_Understanding_in_Multimodal_LLMs_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Daxberger_MM-Spatial_Exploring_3D_Spatial_Understanding_in_Multimodal_LLMs_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (Figure/Table caption), p. 5 (5.2. Overview of Benchmark Category Results), p. 7 (5.4. CV-Bench Results), p. 2 (3. We run extensive experiments illustrating the benefits), p. 5 (5.1. Model Variants), p. 7 (5.4. CV-Bench Results)): Table 3. CA-VQA Results. MM-Spatial-3B significantly outperforms (much larger) top open-source and commercial models across all tasks, demonstrating its strong spatial understanding ability. Model performance is further improved by inco ...

## Evaluation Body Digest

- **p. 2 / Dataset - extractive PDF cue:** CA-VQA is the first dataset that is based on high-quality 3D ground truth, includes depth maps (both from sensors and monocular) and multi-view images, covers ...
- **p. 2 / Dataset - extractive PDF cue:** We apply this pipeline to CA-1M [61] to generate Cubify Anything VQA (CAVQA), a new spatial understanding dataset for MLLM fine-tuning, covering diverse indoor scenes.
- **p. 7 / 5.5. SpatialRGPT-Bench Results - extractive PDF cue:** To enable a fair comparison of model capabilities, we thus align with the benchmark by generating CA-VQAω, a variant of CA-VQA adopting their AABB-based definitions, ...
- **p. 5 / 5.1. Model Variants - extractive PDF cue:** Benchmark Category Results MM-Spatial is a generalist MLLM that improves strongly on the Spatial category while rivaling the MM1.5 baseline across the other task categories. ...
- **p. 7 / 5.4. CV-Bench Results - extractive PDF cue:** Notably, MM-Spatial (Blind eval) 13 achieves the best accuracy among all models on the 2D Object Count task, revealing a substantial bias in this benchmark.
- **p. 5 / 5.1. Model Variants - extractive PDF cue:** Model Benchmark Category Averages Spatial General Knowl.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 5. Metric Depth Estimation Results. We evaluate the metric depth estimates of our CoT model produced as part of its responses on the CA-VQA ...
- **p. 5 / 5.1. Model Variants - extractive PDF cue:** Accuracy improves further when leveraging ground-truth depth via tool-use (1c), although our CoT model's (1b) predictions are very close to that, for both the intermediate ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** Dataset (p. 2); 2. We release a new spatial understanding benchmark de (p. 2); 3. We run extensive experiments illustrating the benefits (p. 2); 5. Experiments (p. 4); 5.2. Overview of Benchmark Category Results (p. 5); 5.3. Results on our CA-VQA Benchmark (p. 5); 5.4. CV-Bench Results (p. 7); 5.5. SpatialRGPT-Bench Results (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 3. CA-VQA Results. MM-Spatial-3B significantly outperforms (much larger) top open-source and commercial models across all tasks, demonstrating its strong spatial understanding ability. Model ... | p. 6 (Figure/Table caption) |
| 5.2. Overview of Benchmark Category Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | MM-Spatial significantly improves on the Spatial category while maintaining performance competitive with MM1.5 across the other categories, suggesting that spatial reasoning can be improved ... | p. 5 (5.2. Overview of Benchmark Category Results) |
| 5.4. CV-Bench Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | 4 demonstrate that MMSpatial-3B 10 significantly outperforms the much larger SOTA Cambrian-1-34B 8 , highlighting the effectiveness of SFT on similar data. | p. 7 (5.4. CV-Bench Results) |
| 3. We run extensive experiments illustrating the benefits | EMPIRICAL / SOURCE-REPORTED EVALUATION | We show that 1) we can train MM-Spatial, a generalist MLLM achieving SOTA on spatial understanding benchmarks (CV-Bench, SpatialRGPT-Bench, CA-VQA), while retaining performance on ... | p. 2 (3. We run extensive experiments illustrating the benefits) |
| 5.1. Model Variants | EMPIRICAL / SOURCE-REPORTED EVALUATION | Benchmark Category Results MM-Spatial is a generalist MLLM that improves strongly on the Spatial category while rivaling the MM1.5 baseline across the other task ... | p. 5 (5.1. Model Variants) |

## Dataset / Benchmark Role

- **p. 2 / Dataset - extractive PDF cue:** CA-VQA is the first dataset that is based on high-quality 3D ground truth, includes depth maps (both from sensors and monocular) and multi-view images, covers ...
- **p. 2 / Dataset - extractive PDF cue:** We apply this pipeline to CA-1M [61] to generate Cubify Anything VQA (CAVQA), a new spatial understanding dataset for MLLM fine-tuning, covering diverse indoor scenes.
- **p. 7 / 5.5. SpatialRGPT-Bench Results - extractive PDF cue:** To enable a fair comparison of model capabilities, we thus align with the benchmark by generating CA-VQAω, a variant of CA-VQA adopting their AABB-based definitions, ...
- **p. 5 / 5.1. Model Variants - extractive PDF cue:** Benchmark Category Results MM-Spatial is a generalist MLLM that improves strongly on the Spatial category while rivaling the MM1.5 baseline across the other task categories. ...
- **p. 7 / 5.4. CV-Bench Results - extractive PDF cue:** Notably, MM-Spatial (Blind eval) 13 achieves the best accuracy among all models on the 2D Object Count task, revealing a substantial bias in this benchmark.
- **p. 5 / 5.1. Model Variants - extractive PDF cue:** Model Benchmark Category Averages Spatial General Knowl.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. (Left) We generate the Cubify Anything VQA (CA-VQA) dataset and benchmark, covering various 1) input signals: single image, metric depth (sensor-based and estimated), ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Table 1. 3D Spatial Dataset Overview. Comparison of object-centric 3D spatial MLLM datasets to CA-VQA (in gray: non-public ones). CA-VQA is the first dataset that ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. CA-VQA Data Example. Example of a single sample from our dataset. Each reference frame has between 0-4 multi-view support frames. All frames (reference ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. Example of leveraging depth maps via tool-use. The model predicts the objects' 2D bounding boxes and function calls, receives the tool outputs (which ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4. Qualitative Example. We show the predictions of various models on a challenging example from our CA-VQA benchmark. Strong commercial (2a&b) and research models ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Table 2. Benchmark Category Results MM-Spatial is a gener- alist MLLM that improves strongly on the Spatial category while rivaling the MM1.5 baseline across the ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 3. CA-VQA Results. MM-Spatial-3B significantly outperforms (much larger) top open-source and commercial models across all tasks, demonstrating its strong spatial understanding ability. Model performance ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 4. CV-Bench Results. MM-Spatial-3B substantially outperforms the (much larger) SOTA models, with CoT and depth input further improving performance. It almost fully solves the ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | CA-VQA is the first dataset that is based on high-quality 3D ground truth, includes depth maps (both from sensors and monocular) and multi-view images, ... | embodiment, simulator version and control stack | p. 2 (Dataset), p. 2 (Dataset) |
| Task/environment | We apply this pipeline to CA-1M [61] to generate Cubify Anything VQA (CAVQA), a new spatial understanding dataset for MLLM fine-tuning, covering diverse indoor ... | reset, timeout, object/scene variation | p. 2 (Dataset), p. 7 (5.5. SpatialRGPT-Bench Results) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 8 (Model), p. 1 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (4.1. Model Architecture), p. 4 (4.1. Model Architecture) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 5. Metric Depth Estimation Results. We evaluate the metric depth estimates of our CoT model produced as part of its responses on the ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Accuracy improves further when leveraging ground-truth depth via tool-use (1c), although our CoT model's (1b) predictions are very close to that, for both the ... | definition/direction/unit from same section | p. 5 (5.1. Model Variants) |
| MM-Spatial achieves almost perfect accuracy on the indoor splits of the 3D tasks, and also demonstrates strong out-of-domain generalization to the outdoor splits. | definition/direction/unit from same section | p. 7 (5.4. CV-Bench Results) |
| Compared to existing benchmarks, ours 1) includes diverse tasks (incl. relative and metric distance / size estimation and 3D grounding), 2) provides rich input ... | definition/direction/unit from same section | p. 2 (2. We release a new spatial understanding benchmark de) |
| We show that 1) we can train MM-Spatial, a generalist MLLM achieving SOTA on spatial understanding benchmarks (CV-Bench, SpatialRGPT-Bench, CA-VQA), while retaining performance on ... | definition/direction/unit from same section | p. 2 (3. We run extensive experiments illustrating the benefits) |
| MM-Spatial significantly improves on the Spatial category while maintaining performance competitive with MM1.5 across the other categories, suggesting that spatial reasoning can be improved ... | definition/direction/unit from same section | p. 5 (5.2. Overview of Benchmark Category Results) |
| Table 3. CA-VQA Results. MM-Spatial-3B significantly outperforms (much larger) top open-source and commercial models across all tasks, demonstrating its strong spatial understanding ability. Model ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Figure 1. (Left) We generate the Cubify Anything VQA (CA-VQA) dataset and benchmark, covering various 1) input signals: single image, metric depth (sensor-based and ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| In contrast, on our CA-VQA benchmark, using vision input outperforms the blind baseline on Counting by →13 points. | comparison identity and matched condition | p. 7 (5.4. CV-Bench Results) |
| Table 3. CA-VQA Results. MM-Spatial-3B significantly outperforms (much larger) top open-source and commercial models across all tasks, demonstrating its strong spatial understanding ability. Model ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| We now present an in-depth analysis of the Spatial results, comparing MM-Spatial with SOTA baselines. | comparison identity and matched condition | p. 5 (5.2. Overview of Benchmark Category Results) |
| MM-Spatial-3B 8 substantially outperforms various (much larger) top opensource and commercial models 1 - 6 , incl. the SOTA GPT-4o model 3 , demonstrating ... | comparison identity and matched condition | p. 5 (5.3. Results on our CA-VQA Benchmark) |
| 4 demonstrate that MMSpatial-3B 10 significantly outperforms the much larger SOTA Cambrian-1-34B 8 , highlighting the effectiveness of SFT on similar data. | comparison identity and matched condition | p. 7 (5.4. CV-Bench Results) |
| Compared to existing benchmarks, ours 1) includes diverse tasks (incl. relative and metric distance / size estimation and 3D grounding), 2) provides rich input ... | comparison identity and matched condition | p. 2 (2. We release a new spatial understanding benchmark de) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Trained on single-view RGB inputs, without depth information. | component/input/data sensitivity | p. 4 (5.1. Model Variants) |
| We explore the following model variants in our study, leveraging the various input signals provided within CA-VQA: • MM-Spatial. | component/input/data sensitivity | p. 4 (5.1. Model Variants) |
| We assess the model variants outlined in Sec. | component/input/data sensitivity | p. 5 (5.3. Results on our CA-VQA Benchmark) |
| 4.2 by default; some ablations use Specialist Models trained only on CA-VQA. | component/input/data sensitivity | p. 5 (5.2. Overview of Benchmark Category Results) |
| To enable a fair comparison of model capabilities, we thus align with the benchmark by generating CA-VQAω, a variant of CA-VQA adopting their AABB-based ... | component/input/data sensitivity | p. 7 (5.5. SpatialRGPT-Bench Results) |
| We apply this pipeline to CA-1M [61] to generate Cubify Anything VQA (CAVQA), a new spatial understanding dataset for MLLM fine-tuning, covering diverse indoor ... | component/input/data sensitivity | p. 2 (Dataset) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To address these †Equal contribution. | Table 3. CA-VQA Results. MM-Spatial-3B significantly outperforms (much larger) top open-source and commercial models across all tasks, demonstrating its strong spatial understanding ability. Model ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (Figure/Table caption), p. 5 (5.2. Overview of Benchmark Category Results), p. 7 (5.4. CV-Bench Results), p. 2 (3. We run extensive experiments illustrating the benefits), p. 5 (5.1. Model Variants), p. 7 (5.4. CV-Bench Results) |
| Primary metric/result | MM-Spatial significantly improves on the Spatial category while maintaining performance competitive with MM1.5 across the other categories, suggesting that spatial reasoning can be improved ... | numeric claim only at cited anchor | p. 5 (5.2. Overview of Benchmark Category Results) |

- Numeric sentences retained from the body:
- **p. 7 / 5.4. CV-Bench Results - extractive PDF cue:** In contrast, on our CA-VQA benchmark, using vision input outperforms the blind baseline on Counting by →13 points.
- **p. 6 / Model - extractive PDF cue:** While the performance on Counting and Multi-choice is still acceptable - likely due to inherent remaining biases such as the naturally skewed distribution of object ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | CA-VQA is the first dataset that is based on high-quality 3D ground truth, includes depth maps (both from sensors and monocular) and multi-view images, ... | p. 2 (Dataset) |
| body limitation/failure cue | In future work, we aim to extend our scope to outdoor scenes to complement our high-quality indoor dataset. | p. 8 (6. Conclusion) |
| body limitation/failure cue | MM-Spatial-3B 8 substantially outperforms various (much larger) top opensource and commercial models 1 - 6 , incl. the SOTA GPT-4o model 3 , demonstrating ... | p. 5 (5.3. Results on our CA-VQA Benchmark) |
| body limitation/failure cue | Table 6. SpatialRGPT-Bench Results. MM-Spatial-3B achieves SOTA with both image-only input and tool-use monocular depth, out- performing SpatialRGPT-VILA-1.5-8B (which fully encodes depth). Training on ... | p. 8 (Figure/Table caption) |
| body limitation/failure cue | Strong commercial (2a&b) and research models (2c&d) fail. | p. 5 (5.1. Model Variants) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We use the same training hyperparameters as MM1.5 [128], with unfrozen image encoder and LLM. | p. 4 (4.2. Data and Training) |
| For the 3) supervised fine-tuning (SFT) stage, we start from the MM1.5 single-image SFT mixture, which includes datasets across multiple categories: General VQA, Knowledge ... | p. 4 (4.2. Data and Training) |
| Trained on singleview RGB inputs plus fully encoded depth maps, as described in Sec. | p. 5 (5.1. Model Variants) |
| 2D object grounding and depth prediction) and/or leveraging more test-time compute benefits model accuracy. • Depth (GT): Tool-use vs. | p. 6 (Model) |
| We report the ω1 (accuracy at 25% relative error) and AbsRel (absolute relative error) metrics [57] commonly used in the depth estimation literature [12], ... | p. 7 (Model) |
| MM-Spatial-3B achieves SOTA with both image-only input and tool-use monocular depth, outperforming SpatialRGPT-VILA-1.5-8B (which fully encodes depth). | p. 8 (Model) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 2 / Dataset - extractive PDF cue:** CA-VQA is the first dataset that is based on high-quality 3D ground truth, includes depth maps (both from sensors and monocular) and multi-view images, covers ...
- **p. 8 / 6. Conclusion - extractive PDF cue:** In future work, we aim to extend our scope to outdoor scenes to complement our high-quality indoor dataset.
- **p. 5 / 5.3. Results on our CA-VQA Benchmark - extractive PDF cue:** MM-Spatial-3B 8 substantially outperforms various (much larger) top opensource and commercial models 1 - 6 , incl. the SOTA GPT-4o model 3 , demonstrating 1) ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 6. SpatialRGPT-Bench Results. MM-Spatial-3B achieves SOTA with both image-only input and tool-use monocular depth, out- performing SpatialRGPT-VILA-1.5-8B (which fully encodes depth). Training on a ...
- **p. 5 / 5.1. Model Variants - extractive PDF cue:** Strong commercial (2a&b) and research models (2c&d) fail.

- **PDF anchors reviewed:** datasets p. 2 (Dataset), p. 2 (Dataset), p. 7 (5.5. SpatialRGPT-Bench Results), p. 5 (5.1. Model Variants), p. 7 (5.4. CV-Bench Results), p. 5 (5.1. Model Variants), metrics p. 7 (Figure/Table caption), p. 5 (5.1. Model Variants), p. 7 (5.4. CV-Bench Results), p. 2 (2. We release a new spatial understanding benchmark de), p. 2 (3. We run extensive experiments illustrating the benefits), p. 5 (5.2. Overview of Benchmark Category Results), baselines p. 7 (5.4. CV-Bench Results), p. 6 (Figure/Table caption), p. 5 (5.2. Overview of Benchmark Category Results), p. 5 (5.3. Results on our CA-VQA Benchmark), p. 7 (5.4. CV-Bench Results), p. 2 (2. We release a new spatial understanding benchmark de), results p. 6 (Figure/Table caption), p. 5 (5.2. Overview of Benchmark Category Results), p. 7 (5.4. CV-Bench Results), p. 2 (3. We run extensive experiments illustrating the benefits), p. 5 (5.1. Model Variants), p. 7 (5.4. CV-Bench Results).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
