# Evaluation - GRIN: Zero-Shot Metric Depth with Pixel-Level Diffusion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/; PDF retrieval source: https://openreview.net/attachment?id=VSG65wVNuL&name=pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (5.3. Zero-Shot Metric Depth Estimation), p. 7 (5.4. Zero-Shot Relative Depth Estimation), p. 8 (5.5. Fine-Tuning Experiments), p. 8 (5.5. Fine-Tuning Experiments), p. 6 (5.1. Training Datasets), p. 6 (5.1. Training Datasets)): We believe GRIN could be modified to operate in a similar setting, which would potentially further improve performance, however this is left for future work.

## Evaluation Body Digest

- **p. 5 / 5.1. Training Datasets - extractive body cue:** We trained GRIN using a diverse combination of indoor and outdoor datasets from both real-world and syn
- **p. 6 / 5.1. Training Datasets - extractive body cue:** N/A indicate methods that cannot be evaluated zero-shot in a particular benchmark, because the benchmark dataset is used during training. thetic sources.
- **p. 6 / 5.2. Implementation Details - extractive body cue:** The remaining 80k steps used all training datasets, shuffled to ensure a similar ratio of indoor and outdoor samples per batch, as well as real-world ...
- **p. 7 / 5.3. Zero-Shot Metric Depth Estimation - extractive body cue:** We argue that our approach of directly ingesting sparse data is more scalable, since it enables supervised pre-training on much more diverse real-world datasets without ...
- **p. 8 / 5.4. Zero-Shot Relative Depth Estimation - extractive body cue:** All methods were fine-tuned on the training splits of the validation datasets.
- **p. 7 / 5.3. Zero-Shot Metric Depth Estimation - extractive body cue:** N/A indicates methods trained on the target dataset.
- **p. 8 / 5.6. Ablation Study - extractive body cue:** Similarly, in (B) we show that removing global conditioning also significantly degrades performance, due to the lack of scene-level context for consistent local predictions.
- **p. 7 / 5.3. Zero-Shot Metric Depth Estimation - extractive body cue:** We believe GRIN could be modified to operate in a similar setting, which would potentially further improve performance, however this is left for future work.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** high-dimensional data 또는 robot action-trajectory distribution.
- **Input boundary:** conditioning observation와 noisy/intermediate sample.
- **Output/decision under evaluation:** generated sample, action chunk 또는 trajectory.
- **Primary target:** distribution fit, multimodality, sample quality와 latency.
- **Detected evaluation headings:** 5. Experiments (p. 5); 5.1. Training Datasets (p. 5); 5.2. Implementation Details (p. 6); 5.5. Fine-Tuning Experiments (p. 8).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5.3. Zero-Shot Metric Depth Estimation | EMPIRICAL / REAL-ROBOT OR HARDWARE | We believe GRIN could be modified to operate in a similar setting, which would potentially further improve performance, however this is left for future ... | p. 7 (5.3. Zero-Shot Metric Depth Estimation) |
| 5.4. Zero-Shot Relative Depth Estimation | EMPIRICAL / REAL-ROBOT OR HARDWARE | Results of this experiment are shown in Table 2, indicating that GRIN also outperforms the current state-of-the-art in relative depth estimation across multiple datasets, ... | p. 7 (5.4. Zero-Shot Relative Depth Estimation) |
| 5.5. Fine-Tuning Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Results are shown in Table 3, indicating that GRIN also outperforms other metric depth estimation methods that use in-domain training data. | p. 8 (5.5. Fine-Tuning Experiments) |
| 5.5. Fine-Tuning Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Although our main focus is on zero-shot depth estimation, here we explore how GRIN can also be fine-tuned indomain to further improve performance in ... | p. 8 (5.5. Fine-Tuning Experiments) |
| 5.1. Training Datasets | EMPIRICAL / REAL-ROBOT OR HARDWARE | Zero-shot metric monocular depth estimation results on various indoor and outdoor datasets. | p. 6 (5.1. Training Datasets) |

## Dataset / Benchmark Role

- **p. 5 / 5.1. Training Datasets - extractive body cue:** We trained GRIN using a diverse combination of indoor and outdoor datasets from both real-world and syn
- **p. 6 / 5.1. Training Datasets - extractive body cue:** N/A indicate methods that cannot be evaluated zero-shot in a particular benchmark, because the benchmark dataset is used during training. thetic sources.
- **p. 6 / 5.2. Implementation Details - extractive body cue:** The remaining 80k steps used all training datasets, shuffled to ensure a similar ratio of indoor and outdoor samples per batch, as well as real-world ...
- **p. 7 / 5.3. Zero-Shot Metric Depth Estimation - extractive body cue:** We argue that our approach of directly ingesting sparse data is more scalable, since it enables supervised pre-training on much more diverse real-world datasets without ...
- **p. 8 / 5.4. Zero-Shot Relative Depth Estimation - extractive body cue:** All methods were fine-tuned on the training splits of the validation datasets.
- **p. 7 / 5.3. Zero-Shot Metric Depth Estimation - extractive body cue:** N/A indicates methods trained on the target dataset.
- **p. 8 / 5.6. Ablation Study - extractive body cue:** Similarly, in (B) we show that removing global conditioning also significantly degrades performance, due to the lack of scene-level context for consistent local predictions.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. GRIN sets a new state of the art in zero-shot metric monocular depth estimation, via efficient pixel-level diffusion and the proper handling of ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Recurrent Interface Networks (RIN) architecture. (a) Latent tokens Zin read from input tokens Xin, are processed via a series of self-attention layers, and ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Diagram of GRIN for monocular depth estimation. An input image I with intrinsics K is used to condition the diffusion process both locally, ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Zero-shot metric monocular depth estimation results on various indoor and outdoor datasets. Numbers in italics indicate results obtained by evaluating specific methods on ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Qualitative zero-shot metric depth estimation results using GRIN on various indoor and outdoor datasets. The same model was used in all evaluations. For ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Zero-shot relative monocular depth estimation results (AbsRel). All methods use test-time scale alignment, and do not require intrinsics as input. N/A indicates methods ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5. Uncertainty estimation analysis using multiple GRIN samples. In (a), Depth and uncertainty maps are calculated taking the median and standard deviation of s ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. In-domain metric monocular depth estimation results. All methods were fine-tuned on the training splits of the validation datasets. GRIN FT NI indicates our ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We trained GRIN using a diverse combination of indoor and outdoor datasets from both real-world and syn | embodiment, simulator version and control stack | p. 5 (5.1. Training Datasets), p. 6 (5.1. Training Datasets) |
| Task/environment | N/A indicate methods that cannot be evaluated zero-shot in a particular benchmark, because the benchmark dataset is used during training. thetic sources. | reset, timeout, object/scene variation | p. 6 (5.1. Training Datasets), p. 6 (5.2. Implementation Details) |
| Observation/sensor | conditioning observation와 noisy/intermediate sample | calibration, preprocessing, privileged input | p. 3 (3. Diffusion Preliminaries), p. 2 (1. Introduction) |
| Output/decision | generated sample, action chunk 또는 trajectory | action frame, controller and termination | p. 3 (3. Diffusion Preliminaries), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We believe GRIN could be modified to operate in a similar setting, which would potentially further improve performance, however this is left for future ... | definition/direction/unit from same section | p. 7 (5.3. Zero-Shot Metric Depth Estimation) |
| (a) Qualitative examples of uncertainty maps, given by the standard deviation from multiple samples. | definition/direction/unit from same section | p. 8 (5.4. Zero-Shot Relative Depth Estimation) |
| In (a), Depth and uncertainty maps are calculated taking the median and standard deviation of s = 10 samples. | definition/direction/unit from same section | p. 8 (5.4. Zero-Shot Relative Depth Estimation) |
| The second stage used this same training strategy for an additional 80k steps, with | definition/direction/unit from same section | p. 6 (5.2. Implementation Details) |
| In total, training takes roughly 5 days with distributed data parallel (DDP) across 32 A100 GPUs, with mixed precision format. | definition/direction/unit from same section | p. 7 (5.2. Implementation Details) |
| Figure 2. Recurrent Interface Networks (RIN) architecture. (a) Latent tokens Zin read from input tokens Xin, are processed via a series of self-attention layers, ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Figure 3. Diagram of GRIN for monocular depth estimation. An input image I with intrinsics K is used to condition the diffusion process both ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Figure 6. Zero-shot GRIN qualitative results, including input image (top), predicted depth map (middle), and uncertainty map (bottom). | definition/direction/unit from same section | p. 10 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Results of this experiment are shown in Table 2, indicating that GRIN also outperforms the current state-of-the-art in relative depth estimation across multiple datasets, ... | comparison identity and matched condition | p. 7 (5.4. Zero-Shot Relative Depth Estimation) |
| UniDepth [49] was re-evaluated in most benchmarks because it does not report standard metrics in them (for a fair comparison, we used the UniDepth-C ... | comparison identity and matched condition | p. 6 (5.1. Training Datasets) |
| Interestingly, we also outperform ZeroDepth [27], that uses a similar approach to bridge the geometric domain gap. | comparison identity and matched condition | p. 7 (5.3. Zero-Shot Metric Depth Estimation) |
| Results are shown in Table 3, indicating that GRIN also outperforms other metric depth estimation methods that use in-domain training data. | comparison identity and matched condition | p. 8 (5.5. Fine-Tuning Experiments) |
| GRIN FT NI indicates our model (Table 1) fine-tuned without intrinsics. | comparison identity and matched condition | p. 8 (5.4. Zero-Shot Relative Depth Estimation) |
| Figure 1. GRIN sets a new state of the art in zero-shot metric monocular depth estimation, via efficient pixel-level diffusion and the proper handling ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| GRIN FT NI indicates our model (Table 1) fine-tuned without intrinsics. | component/input/data sensitivity | p. 8 (5.4. Zero-Shot Relative Depth Estimation) |
| We argue that our approach of directly ingesting sparse data is more scalable, since it enables supervised pre-training on much more diverse real-world datasets ... | component/input/data sensitivity | p. 7 (5.3. Zero-Shot Metric Depth Estimation) |
| Ablation study of different design choices. ent depth parameterizations, namely linear and natural logarithm, each emphasizing different ranges. | component/input/data sensitivity | p. 8 (5.6. Ablation Study) |
| Thus, we replace them with default pinhole values: fx = cx = W/2 and fy = cy = H/2, and reutilize our pre-trained metric ... | component/input/data sensitivity | p. 7 (5.4. Zero-Shot Relative Depth Estimation) |
| Figure 8. Degradation in depth estimation performance when removing global conditioning vectors during inference. The percentage value indicates how many global conditioning vectors are ... | component/input/data sensitivity | p. 12 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our contributions are as follows: • We introduce GRIN, a novel diffusion-based monocular depth estimation framework designed to (i) ingest sparse training ... | We believe GRIN could be modified to operate in a similar setting, which would potentially further improve performance, however this is left for future ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (5.3. Zero-Shot Metric Depth Estimation), p. 7 (5.4. Zero-Shot Relative Depth Estimation), p. 8 (5.5. Fine-Tuning Experiments), p. 8 (5.5. Fine-Tuning Experiments), p. 6 (5.1. Training Datasets), p. 6 (5.1. Training Datasets) |
| Primary metric/result | Results of this experiment are shown in Table 2, indicating that GRIN also outperforms the current state-of-the-art in relative depth estimation across multiple datasets, ... | numeric claim only at cited anchor | p. 7 (5.4. Zero-Shot Relative Depth Estimation) |

- Numeric sentences retained from the body:
- **p. 6 / 5.2. Implementation Details - extractive body cue:** During training, input images (and intrinsics) are first resized to fit within a 640×512 resolution, and then randomly resized between [0.5, 1.5] of this resolution, ...
- **p. 6 / 5.2. Implementation Details - extractive body cue:** If the result is larger than 640×512 it is randomly cropped, otherwise it is padded, so it can be collated as part of a batch.
- **p. 8 / 5.4. Zero-Shot Relative Depth Estimation - extractive body cue:** In (a), Depth and uncertainty maps are calculated taking the median and standard deviation of s = 10 samples.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Interestingly, these uncertainty maps also accurately detect failure cases of our model, such as the mirror on the bottom of the second column, due ... | p. 9 (6. Conclusion) |
| body limitation/failure cue | Table 1. Zero-shot metric monocular depth estimation results on various indoor and outdoor datasets. Numbers in italics indicate results obtained by evaluating specific methods ... | p. 6 (Figure/Table caption) |
| body limitation/failure cue | We then provide additional architecture details in Section C, and in Section D we discuss potential limitations of our architecture. | p. 9 (6. Conclusion) |
| body limitation/failure cue | Figure 2. Recurrent Interface Networks (RIN) architecture. (a) Latent tokens Zin read from input tokens Xin, are processed via a series of self-attention layers, ... | p. 3 (Figure/Table caption) |
| body limitation/failure cue | We believe GRIN could be modified to operate in a similar setting, which would potentially further improve performance, however this is left for future ... | p. 7 (5.3. Zero-Shot Metric Depth Estimation) |
| body limitation/failure cue | In this setting, camera intrinsics are not required, since the model does not need to reason over physical 3D properties of the environment, focusing ... | p. 7 (5.4. Zero-Shot Relative Depth Estimation) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We used the LION optimizer [7], with batch size b = 1024, weight decay of wd = 10-2 (applied only to layer weights), β1 ... | p. 6 (5.2. Implementation Details) |
| For a fair comparison, we used the standard evaluation protocol for each of these benchmarks, and when necessary re-evaluated models under the same conditions ... | p. 7 (5.3. Zero-Shot Metric Depth Estimation) |
| At training time we discard pixels with missing depth information (i.e., djk = 0), resulting in a ˆV loc matrix with varying length N. | p. 5 (4.4. Training Procedure) |
| The second stage used this same training strategy for an additional 80k steps, with | p. 6 (5.2. Implementation Details) |
| Inference for a 640 × 384 image can be done in 0.8 seconds on a single similar GPU (faster than Marigold). | p. 7 (5.2. Implementation Details) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 6. Conclusion - extractive body cue:** Interestingly, these uncertainty maps also accurately detect failure cases of our model, such as the mirror on the bottom of the second column, due to ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Zero-shot metric monocular depth estimation results on various indoor and outdoor datasets. Numbers in italics indicate results obtained by evaluating specific methods on ...
- **p. 9 / 6. Conclusion - extractive body cue:** We then provide additional architecture details in Section C, and in Section D we discuss potential limitations of our architecture.
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Recurrent Interface Networks (RIN) architecture. (a) Latent tokens Zin read from input tokens Xin, are processed via a series of self-attention layers, and ...
- **p. 7 / 5.3. Zero-Shot Metric Depth Estimation - extractive body cue:** We believe GRIN could be modified to operate in a similar setting, which would potentially further improve performance, however this is left for future work.
- **p. 7 / 5.4. Zero-Shot Relative Depth Estimation - extractive body cue:** In this setting, camera intrinsics are not required, since the model does not need to reason over physical 3D properties of the environment, focusing instead ...

- **Evidence anchors reviewed:** datasets p. 5 (5.1. Training Datasets), p. 6 (5.1. Training Datasets), p. 6 (5.2. Implementation Details), p. 7 (5.3. Zero-Shot Metric Depth Estimation), p. 8 (5.4. Zero-Shot Relative Depth Estimation), p. 7 (5.3. Zero-Shot Metric Depth Estimation), metrics p. 7 (5.3. Zero-Shot Metric Depth Estimation), p. 8 (5.4. Zero-Shot Relative Depth Estimation), p. 8 (5.4. Zero-Shot Relative Depth Estimation), p. 6 (5.2. Implementation Details), p. 7 (5.2. Implementation Details), p. 3 (Figure/Table caption), baselines p. 7 (5.4. Zero-Shot Relative Depth Estimation), p. 6 (5.1. Training Datasets), p. 7 (5.3. Zero-Shot Metric Depth Estimation), p. 8 (5.5. Fine-Tuning Experiments), p. 8 (5.4. Zero-Shot Relative Depth Estimation), p. 1 (Figure/Table caption), results p. 7 (5.3. Zero-Shot Metric Depth Estimation), p. 7 (5.4. Zero-Shot Relative Depth Estimation), p. 8 (5.5. Fine-Tuning Experiments), p. 8 (5.5. Fine-Tuning Experiments), p. 6 (5.1. Training Datasets), p. 6 (5.1. Training Datasets).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
