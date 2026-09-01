# Evaluation - GenSplat: Bridging the Generalization Gap in 3DGS Language Comprehension

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Liu_GenSplat_Bridging_the_Generalization_Gap_in_3DGS_Language_Comprehension_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_GenSplat_Bridging_the_Generalization_Gap_in_3DGS_Language_Comprehension_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.3. Comparison with State-of-the-Art Models), p. 7 (4.3. Comparison with State-of-the-Art Models), p. 2 (Figure/Table caption), p. 6 (4.3. Comparison with State-of-the-Art Models), p. 6 (4.2. Evaluation Datasets and Metrics), p. 8 (4.4. Ablation Study)): Our GenSplat achieves consistently better results over the expert model SplatTalk [61] (e.g., a +26.8% CIDEr (C) improvement on ScanQA [2]), as well as the 3D MLLM-based 3D-LLaVA [14], on ...

## Evaluation Body Digest

- **p. 6 / 4.2. Evaluation Datasets and Metrics - extractive PDF cue:** Comparison of 3D referring segmentation on five scenes (selected by ReferSplat [22]) from the ScanRefer [5] dataset.
- **p. 7 / 4.4. Ablation Study - extractive PDF cue:** We draw five key conclusions from Table 4: ①Progressive pretraining is foundational: as demonstrated in (I), (II) and (III), hierarchical concept learning from semantic- to ...
- **p. 6 / 4.3. Comparison with State-of-the-Art Models - extractive PDF cue:** We report comparison results on the ScanRefer [5] (featuring single referred object) and Multi3DRefer [76] (featuring varying numbers of referred objects) datasets, as shown in ...
- **p. 7 / 4.3. Comparison with State-of-the-Art Models - extractive PDF cue:** We further compare our method against Grounded-SAM and per-scene optimization-based methods on five scenes selected by ReferSplat [22] from ScanRefer.
- **p. 8 / 4.4. Ablation Study - extractive PDF cue:** Qualitative visualization on the ScanRefer [5] and SQA3D [50] datasets.
- **p. 8 / 4.4. Ablation Study - extractive PDF cue:** We showcase referring segmentation results on both scenes (a) and (b), and additionally present a question answering example on scene (b). ⑤Geometry-aware fusion facilitates synergistic ...
- **p. 6 / 4.2. Evaluation Datasets and Metrics - extractive PDF cue:** For the question answering task, we follow [18, 26] to evaluate the generated responses on ScanQA [2] using CIDEr (C), BLEU-4 (B-4), METEOR (M), and ...
- **p. 6 / 4.1. Implementation Details - extractive PDF cue:** We use AdamW optimizer with a learning rate initialized as 2 × 10-4 and updated using the cosine annealing schedule.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.1. Implementation Details (p. 6); 4.2. Evaluation Datasets and Metrics (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.3. Comparison with State-of-the-Art Models | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our GenSplat achieves consistently better results over the expert model SplatTalk [61] (e.g., a +26.8% CIDEr (C) improvement on ScanQA [2]), as well as ... | p. 7 (4.3. Comparison with State-of-the-Art Models) |
| 4.3. Comparison with State-of-the-Art Models | EMPIRICAL / SOURCE-REPORTED EVALUATION | Results in Table 2 show that our GenSplat method significantly outperforms other methods without requiring per-scene optimization, showcasing its robust generalization capabilities. | p. 7 (4.3. Comparison with State-of-the-Art Models) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 1. We propose GenSplat, the first approach to achieve generalizable language-guided understanding in 3DGS. By hierarchically grounding multi-level linguistic concepts in 3D Gaussian ... | p. 2 (Figure/Table caption) |
| 4.3. Comparison with State-of-the-Art Models | EMPIRICAL / SOURCE-REPORTED EVALUATION | We report comparison results on the ScanRefer [5] (featuring single referred object) and Multi3DRefer [76] (featuring varying numbers of referred objects) datasets, as shown ... | p. 6 (4.3. Comparison with State-of-the-Art Models) |
| 4.2. Evaluation Datasets and Metrics | EMPIRICAL / SOURCE-REPORTED EVALUATION | For the question answering task, we follow [18, 26] to evaluate the generated responses on ScanQA [2] using CIDEr (C), BLEU-4 (B-4), METEOR (M), ... | p. 6 (4.2. Evaluation Datasets and Metrics) |

## Dataset / Benchmark Role

- **p. 6 / 4.2. Evaluation Datasets and Metrics - extractive PDF cue:** Comparison of 3D referring segmentation on five scenes (selected by ReferSplat [22]) from the ScanRefer [5] dataset.
- **p. 7 / 4.4. Ablation Study - extractive PDF cue:** We draw five key conclusions from Table 4: ①Progressive pretraining is foundational: as demonstrated in (I), (II) and (III), hierarchical concept learning from semantic- to ...
- **p. 6 / 4.3. Comparison with State-of-the-Art Models - extractive PDF cue:** We report comparison results on the ScanRefer [5] (featuring single referred object) and Multi3DRefer [76] (featuring varying numbers of referred objects) datasets, as shown in ...
- **p. 7 / 4.3. Comparison with State-of-the-Art Models - extractive PDF cue:** We further compare our method against Grounded-SAM and per-scene optimization-based methods on five scenes selected by ReferSplat [22] from ScanRefer.
- **p. 8 / 4.4. Ablation Study - extractive PDF cue:** Qualitative visualization on the ScanRefer [5] and SQA3D [50] datasets.
- **p. 8 / 4.4. Ablation Study - extractive PDF cue:** We showcase referring segmentation results on both scenes (a) and (b), and additionally present a question answering example on scene (b). ⑤Geometry-aware fusion facilitates synergistic ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1. We propose GenSplat, the first approach to achieve generalizable language-guided understanding in 3DGS. By hierarchically grounding multi-level linguistic concepts in 3D Gaussian representations, ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. Overview of the GenSplat framework. Given a set of multi-view RGB images {Ii}N i=1 and a text query Q (e.g., for Referring Segmentation ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3. We propose Geometry-Aware Frame Selector (GAFS) to identify the most informative views for MLLM reasoning. GAFS bridges the critical gap between MLLM's native ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Comparison of 3D referring segmentation on ScanRe- fer [5] and Multi3DRefer [76] validation sets. "2D MLLMs" denote methods that apply a 2D MLLM ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. Comparison of 3D referring segmentation on five scenes (selected by ReferSplat [22]) from the ScanRefer [5] dataset. Best results are bolded. Methods Grounded-SAM ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Comparison of 3D question answering on ScanQA [2] and SQA3D [50]. Best results are bolded. Methods Modality ScanQA (val) SQA3D (test) C↑ B-4↑
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 4. Key ablation studies on different design components. Methods ScanRefer Multi3DRefer ScanQA SQA3D mIoU↑ mIoU↑ C↑
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4. Qualitative visualization on the ScanRefer [5] and SQA3D [50] datasets. We showcase referring segmentation results on both scenes (a) and (b), and additionally ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Comparison of 3D referring segmentation on five scenes (selected by ReferSplat [22]) from the ScanRefer [5] dataset. | embodiment, simulator version and control stack | p. 6 (4.2. Evaluation Datasets and Metrics), p. 7 (4.4. Ablation Study) |
| Task/environment | We draw five key conclusions from Table 4: ①Progressive pretraining is foundational: as demonstrated in (I), (II) and (III), hierarchical concept learning from semantic- ... | reset, timeout, object/scene variation | p. 7 (4.4. Ablation Study), p. 6 (4.3. Comparison with State-of-the-Art Models) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 5 (3.1. Progressive Language Grounding Curriculum), p. 4 (3.1. Progressive Language Grounding Curriculum) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (3.1. Progressive Language Grounding Curriculum), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For the question answering task, we follow [18, 26] to evaluate the generated responses on ScanQA [2] using CIDEr (C), BLEU-4 (B-4), METEOR (M), ... | definition/direction/unit from same section | p. 6 (4.2. Evaluation Datasets and Metrics) |
| We use AdamW optimizer with a learning rate initialized as 2 × 10-4 and updated using the cosine annealing schedule. | definition/direction/unit from same section | p. 6 (4.1. Implementation Details) |
| These results demonstrate the effectiveness of GenSplat in both scene-level and object-level geometric-language reasonings. | definition/direction/unit from same section | p. 7 (4.3. Comparison with State-of-the-Art Models) |
| For 3D question answering, instance query features are passed to the captioning head [57] to generate the textual prediction. | definition/direction/unit from same section | p. 7 (4.4. Ablation Study) |
| Figure 1. We propose GenSplat, the first approach to achieve generalizable language-guided understanding in 3DGS. By hierarchically grounding multi-level linguistic concepts in 3D Gaussian ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| The (I) Baseline model contains the randomly-initialized Gaussian Encoder and Instance Decoder (i.e., without the MLLM-guided reasoning and Referring Decoder). | comparison identity and matched condition | p. 7 (4.4. Ablation Study) |
| Results in Table 2 show that our GenSplat method significantly outperforms other methods without requiring per-scene optimization, showcasing its robust generalization capabilities. | comparison identity and matched condition | p. 7 (4.3. Comparison with State-of-the-Art Models) |
| We showcase referring segmentation results on both scenes (a) and (b), and additionally present a question answering example on scene (b). ⑤Geometry-aware fusion facilitates ... | comparison identity and matched condition | p. 8 (4.4. Ablation Study) |
| Comparison of 3D referring segmentation on five scenes (selected by ReferSplat [22]) from the ScanRefer [5] dataset. | comparison identity and matched condition | p. 6 (4.2. Evaluation Datasets and Metrics) |
| We report comparison results on the ScanRefer [5] (featuring single referred object) and Multi3DRefer [76] (featuring varying numbers of referred objects) datasets, as shown ... | comparison identity and matched condition | p. 6 (4.3. Comparison with State-of-the-Art Models) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We now report ablation results to validate the effectiveness of each proposed component based on the 3D referring segmentation and 3D question answering tasks. | component/input/data sensitivity | p. 7 (4.4. Ablation Study) |
| Key ablation studies on different design components. | component/input/data sensitivity | p. 7 (4.4. Ablation Study) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our key contributions are: • We introduce GenSplat, the first generalizable 3DGS framework that enables open-vocabulary language understanding and spatial reasoning, through ... | Our GenSplat achieves consistently better results over the expert model SplatTalk [61] (e.g., a +26.8% CIDEr (C) improvement on ScanQA [2]), as well as ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.3. Comparison with State-of-the-Art Models), p. 7 (4.3. Comparison with State-of-the-Art Models), p. 2 (Figure/Table caption), p. 6 (4.3. Comparison with State-of-the-Art Models), p. 6 (4.2. Evaluation Datasets and Metrics), p. 8 (4.4. Ablation Study) |
| Primary metric/result | Results in Table 2 show that our GenSplat method significantly outperforms other methods without requiring per-scene optimization, showcasing its robust generalization capabilities. | numeric claim only at cited anchor | p. 7 (4.3. Comparison with State-of-the-Art Models) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Implementation Details - extractive PDF cue:** Gaussian Encoder is first trained on ScanNet train set [12] for 100 epochs and then trained with the Instance Decoder on ScanNet200 [59] for 512 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | An example failure case of our method. | p. 8 (5. Conclusion) |
| body limitation/failure cue | Extensive experiments across diverse tasks, such as 3D referring segmentation, visual question answering, and open-vocabulary understanding, have demonstrated its robust generalization and reasoning abilities. | p. 8 (5. Conclusion) |
| body limitation/failure cue | Since SQA3D [50] does not provide frame-level annotations, we apply GPT-5 [52] for annotation. | p. 6 (4.1. Implementation Details) |
| body limitation/failure cue | Note that our method does not require test-time per-scene optimization beyond 3DGS reconstruction. | p. 6 (4.1. Implementation Details) |
| body limitation/failure cue | In contrast, 2D-based methods such as Grounded-SAM and per-scene optimization approaches fail under these challenging scenarios. | p. 7 (4.3. Comparison with State-of-the-Art Models) |
| body limitation/failure cue | Results in Table 2 show that our GenSplat method significantly outperforms other methods without requiring per-scene optimization, showcasing its robust generalization capabilities. | p. 7 (4.3. Comparison with State-of-the-Art Models) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| In both stages, we use the AdamW optimizer with a learning rate of 1 × 10-4 (weight decay of 0.01) and a batch size ... | p. 6 (4.1. Implementation Details) |
| The GAFS is trained with a learning rate of 5 × 10-4 and a batch size of 2 per GPU, where each iteration samples ... | p. 6 (4.1. Implementation Details) |
| We assign a text encoder [15] to extract text embeddings, which Table 4. | p. 7 (4.4. Ablation Study) |
| The (I) Baseline model contains the randomly-initialized Gaussian Encoder and Instance Decoder (i.e., without the MLLM-guided reasoning and Referring Decoder). | p. 7 (4.4. Ablation Study) |
| During inference time, GAFS ranks candidate views by their predicted scores. | p. 5 (3.2. MLLM-guided Reasoning Model) |
| Specifically, we adopt a standard SparseConvUNet [11] as our Gaussian Encoder (denoted 5223 | p. 3 (3.1. Progressive Language Grounding Curriculum) |
| 2, GenSplat consists of three main components: the Gaussian Encoder, the Instance Decoder, and the MLLMguided Referring Decoder. | p. 3 (3. The GenSplat Method) |
| Within this Transformer-based decoder, the queries Oq interact with the keys and values from the pooled semantic features ˆL through cross-attention. | p. 4 (3.1. Progressive Language Grounding Curriculum) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusion - extractive PDF cue:** An example failure case of our method.
- **p. 8 / 5. Conclusion - extractive PDF cue:** Extensive experiments across diverse tasks, such as 3D referring segmentation, visual question answering, and open-vocabulary understanding, have demonstrated its robust generalization and reasoning abilities.
- **p. 6 / 4.1. Implementation Details - extractive PDF cue:** Since SQA3D [50] does not provide frame-level annotations, we apply GPT-5 [52] for annotation.
- **p. 6 / 4.1. Implementation Details - extractive PDF cue:** Note that our method does not require test-time per-scene optimization beyond 3DGS reconstruction.
- **p. 7 / 4.3. Comparison with State-of-the-Art Models - extractive PDF cue:** In contrast, 2D-based methods such as Grounded-SAM and per-scene optimization approaches fail under these challenging scenarios.
- **p. 7 / 4.3. Comparison with State-of-the-Art Models - extractive PDF cue:** Results in Table 2 show that our GenSplat method significantly outperforms other methods without requiring per-scene optimization, showcasing its robust generalization capabilities.

- **PDF anchors reviewed:** datasets p. 6 (4.2. Evaluation Datasets and Metrics), p. 7 (4.4. Ablation Study), p. 6 (4.3. Comparison with State-of-the-Art Models), p. 7 (4.3. Comparison with State-of-the-Art Models), p. 8 (4.4. Ablation Study), p. 8 (4.4. Ablation Study), metrics p. 6 (4.2. Evaluation Datasets and Metrics), p. 6 (4.1. Implementation Details), p. 7 (4.3. Comparison with State-of-the-Art Models), p. 7 (4.4. Ablation Study), p. 2 (Figure/Table caption), baselines p. 7 (4.4. Ablation Study), p. 7 (4.3. Comparison with State-of-the-Art Models), p. 8 (4.4. Ablation Study), p. 6 (4.2. Evaluation Datasets and Metrics), p. 6 (4.3. Comparison with State-of-the-Art Models), results p. 7 (4.3. Comparison with State-of-the-Art Models), p. 7 (4.3. Comparison with State-of-the-Art Models), p. 2 (Figure/Table caption), p. 6 (4.3. Comparison with State-of-the-Art Models), p. 6 (4.2. Evaluation Datasets and Metrics), p. 8 (4.4. Ablation Study).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
