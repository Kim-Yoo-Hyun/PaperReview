# Evaluation - 3D-LLM: Injecting the 3D World into Large Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2307.12981; PDF retrieval source: https://arxiv.org/pdf/2307.12981. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (5 Experiments), p. 14 (Figure/Table caption), p. 7 (5 Experiments), p. 8 (5 Experiments), p. 16 (Figure/Table caption), p. 7 (5 Experiments)): Our model outperforms all baseline models for most of the evaluation metrics. they have much lower performances compared to 3D-LLMs, probably because features of multi-view images are disorganized, thus losing ...

## Evaluation Body Digest

- **p. 7 / 5 Experiments - extractive PDF cue:** Specifically, our 3D-language data generation pipeline generates the held-in datasets of multiple tasks. we split the datasets into train/val/test sets (8:1:1).
- **p. 7 / 5 Experiments - extractive PDF cue:** We utilize training sets of held-in datasets for pre-training foundation 3D-LLMs, and their validation and test sets can be applied for held-in evaluation.
- **p. 8 / 5 Experiments - extractive PDF cue:** 5.2 More Extensive Evaluation Held-In Evaluation We carry out experiments on held-in datasets of three tasks: 3D captioning, 3D-assited dialog and task decomposition.
- **p. 8 / 5 Experiments - extractive PDF cue:** BLEU-1 BLEU-4 METEOR ROUHE-L CIDER EM SingleImage+MCAN 16.5 0.0 8.4 21.5 38.6 15.8 VoteNet+MCAN* 29.5 6.0 12.0 30.9 58.2 19.7 ScanRefer+MCAN* 27.9 7.5 11.9 30.7 ...
- **p. 9 / 5 Experiments - extractive PDF cue:** Describe the scene Black and white table with stairs in it.
- **p. 9 / 5 Experiments - extractive PDF cue:** Describe the scene A 3D model of a small, old, and ruined castle with a doorway and stairs Can you help me find my shoes?
- **p. 7 / 5 Experiments - extractive PDF cue:** We report BLEU, ROUGE-L, METEOR, CIDEr for robust answer matching.
- **p. 7 / 5 Experiments - extractive PDF cue:** The models are trained with the standard language modeling loss to output responses.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5 Experiments (p. 7); B Experiments (p. 13); B.1 Implementation Details (p. 13); B.2 Held-Out Evaluation (p. 14); B.3 Held-In Evaluation (p. 16).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our model outperforms all baseline models for most of the evaluation metrics. they have much lower performances compared to 3D-LLMs, probably because features of ... | p. 8 (5 Experiments) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 4: Experimental results on 3DMV-VQA dataset. * denotes using explicit object representations and neuro-symbolic reasoning. Result Analysis Table 4 shows the performances on ... | p. 14 (Figure/Table caption) |
| 5 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | For example, for BLEU-1, our model outperforms the state-of-the-art ScanQA model by ∼9% for validation set and ∼7% for test set. | p. 7 (5 Experiments) |
| 5 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | From the table, we could see that 3D-LLMs could generate high-quality responses, outperforming both 2D VLMs and language-only LLMs. | p. 8 (5 Experiments) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 8: Visualization of an object navigation episode. B.3 Held-In Evaluation B.3.1 3D Dense Captioning In Table 6, we show the results of 3D ... | p. 16 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 7 / 5 Experiments - extractive PDF cue:** Specifically, our 3D-language data generation pipeline generates the held-in datasets of multiple tasks. we split the datasets into train/val/test sets (8:1:1).
- **p. 7 / 5 Experiments - extractive PDF cue:** We utilize training sets of held-in datasets for pre-training foundation 3D-LLMs, and their validation and test sets can be applied for held-in evaluation.
- **p. 8 / 5 Experiments - extractive PDF cue:** 5.2 More Extensive Evaluation Held-In Evaluation We carry out experiments on held-in datasets of three tasks: 3D captioning, 3D-assited dialog and task decomposition.
- **p. 8 / 5 Experiments - extractive PDF cue:** BLEU-1 BLEU-4 METEOR ROUHE-L CIDER EM SingleImage+MCAN 16.5 0.0 8.4 21.5 38.6 15.8 VoteNet+MCAN* 29.5 6.0 12.0 30.9 58.2 19.7 ScanRefer+MCAN* 27.9 7.5 11.9 30.7 ...
- **p. 9 / 5 Experiments - extractive PDF cue:** Describe the scene Black and white table with stairs in it.
- **p. 9 / 5 Experiments - extractive PDF cue:** Describe the scene A 3D model of a small, old, and ruined castle with a doorway and stairs Can you help me find my shoes?

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: Examples from our generated 3D-language data, which covers multiple 3D-related tasks. relationships, affordances, physics and interaction so on. Therefore, such LLMs pale in ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: 3D-language data generation pipelines. obstacles like how to handle the problem of data sparsity, how to align the 3D world with 2D images, ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3: Overview of our 3D-LLM framework. The first two columns show our 3D feature extractor. We first render a few multi-view images from the ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. We observe a significant increase in the evaluation metrics. For example, for BLEU-1, our model outperforms the state-of-the-art ScanQA model by ∼9% for ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 1: Experimental results on ScanQA validation set. * Means the models use explicit object representations. B-1, B-2, B-3, B-4 denote BLEU-1, BLEU-2, BLEU-3, BLEU-4 ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2: Experimental results on ScanQA test set. * Means the models use explicit object representations. Our model outperforms all baseline models for most of ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3: Experimental Results on Held-In Datasets. 3D-LLMs outperform 2D VLMs. 8
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 4: Qualitative examples of 3D-LLM's prediction. Qualitative Examples In Figure 4, we show qualitative examples of 3D-LLM's predictions. We can see that our 3D-LLM ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Specifically, our 3D-language data generation pipeline generates the held-in datasets of multiple tasks. we split the datasets into train/val/test sets (8:1:1). | embodiment, simulator version and control stack | p. 7 (5 Experiments), p. 7 (5 Experiments) |
| Task/environment | We utilize training sets of held-in datasets for pre-training foundation 3D-LLMs, and their validation and test sets can be applied for held-in evaluation. | reset, timeout, object/scene variation | p. 7 (5 Experiments), p. 8 (5 Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (5. Facing the mirror and dress), p. 6 (5. Facing the mirror and dress) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 6 (5. Facing the mirror and dress), p. 2 (5. Facing the mirror and dress) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We report BLEU, ROUGE-L, METEOR, CIDEr for robust answer matching. | definition/direction/unit from same section | p. 7 (5 Experiments) |
| The models are trained with the standard language modeling loss to output responses. | definition/direction/unit from same section | p. 7 (5 Experiments) |
| We report the held-in evaluation performances in Table 3. | definition/direction/unit from same section | p. 8 (5 Experiments) |
| B-1, B-2, B-3, B-4 denote BLEU-1, BLEU-2, BLEU-3, BLEU-4 respectively. | definition/direction/unit from same section | p. 8 (5 Experiments) |
| Additionally, we apply a linear warmup of the learning rate during the initial 1K steps, increasing from 10-8 to 10-5, followed by a cosine ... | definition/direction/unit from same section | p. 13 (B.1 Implementation Details) |
| The learning rate is increased linearly from 0 to 10-4 up over the first 5000 steps then held constant for the duration of training. | definition/direction/unit from same section | p. 14 (B.1 Implementation Details) |
| Figure 1: Examples from our generated 3D-language data, which covers multiple 3D-related tasks. relationships, affordances, physics and interaction so on. Therefore, such LLMs pale ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Figure 2: 3D-language data generation pipelines. obstacles like how to handle the problem of data sparsity, how to align the 3D world with 2D ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 2. We observe a significant increase in the evaluation metrics. For example, for BLEU-1, our model outperforms the state-of-the-art ScanQA model by ∼9% ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Our model outperforms all baseline models for most of the evaluation metrics. they have much lower performances compared to 3D-LLMs, probably because features of ... | comparison identity and matched condition | p. 8 (5 Experiments) |
| Table 4: Experimental results on 3DMV-VQA dataset. * denotes using explicit object representations and neuro-symbolic reasoning. Result Analysis Table 4 shows the performances on ... | comparison identity and matched condition | p. 14 (Figure/Table caption) |
| Table 1: Experimental results on ScanQA validation set. * Means the models use explicit object representations. B-1, B-2, B-3, B-4 denote BLEU-1, BLEU-2, BLEU-3, ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Figure 8: Visualization of an object navigation episode. B.3 Held-In Evaluation B.3.1 3D Dense Captioning In Table 6, we show the results of 3D ... | comparison identity and matched condition | p. 16 (Figure/Table caption) |
| In addition to these baselines, we also design several LLMbased baselines. | comparison identity and matched condition | p. 7 (5 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| This shows that our model could perform visual reasoning about objects and their relationships even without explicit object representations. | component/input/data sensitivity | p. 7 (5 Experiments) |
| Furthermore, 3D-based baselines use object detectors like VoteNet to segment the objects, and then send per-object features into their models, while our inputs are ... | component/input/data sensitivity | p. 7 (5 Experiments) |
| We add one language-only baseline: FlanT5, which examines LLMs' ability to complete these tasks without any visual input. | component/input/data sensitivity | p. 8 (5 Experiments) |
| Using Pretrained BLIP-2 as backbones, we train 3D-LLMs for 100K steps, and validate every 1K step. | component/input/data sensitivity | p. 13 (B.1 Implementation Details) |
| 3D-LLMs based on pretrained flamingo are trained using the AdamW optimizer with global norm clipping of 1, no weight decay for the perceiver resampler ... | component/input/data sensitivity | p. 13 (B.1 Implementation Details) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To sum up, our paper has the following contributions: • We introduce a new family of 3D-based Large Language models (3D-LLMs) that can take ... | Our model outperforms all baseline models for most of the evaluation metrics. they have much lower performances compared to 3D-LLMs, probably because features of ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (5 Experiments), p. 14 (Figure/Table caption), p. 7 (5 Experiments), p. 8 (5 Experiments), p. 16 (Figure/Table caption), p. 7 (5 Experiments) |
| Primary metric/result | Table 4: Experimental results on 3DMV-VQA dataset. * denotes using explicit object representations and neuro-symbolic reasoning. Result Analysis Table 4 shows the performances on ... | numeric claim only at cited anchor | p. 14 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 14 / B.1 Implementation Details - extractive PDF cue:** The learning rate is increased linearly from 0 to 10-4 up over the first 5000 steps then held constant for the duration of training.
- **p. 5 / 5. Facing the mirror and dress - extractive PDF cue:** HM3DSem [47] further adds semantic annotations and bounding boxes for more than 200 scenes of HM3D.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | A limitation is that the 3D feature extractor relies on 2D multi-view images, and thus all 3D scenes need to be rendered so that ... | p. 9 (6 Conclusion) |
| body limitation/failure cue | We report BLEU, ROUGE-L, METEOR, CIDEr for robust answer matching. | p. 7 (5 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Additionally, we apply a linear warmup of the learning rate during the initial 1K steps, increasing from 10-8 to 10-5, followed by a cosine ... | p. 13 (B.1 Implementation Details) |
| The learning rate is increased linearly from 0 to 10-4 up over the first 5000 steps then held constant for the duration of training. | p. 14 (B.1 Implementation Details) |
| The batch size is 16 for each node. | p. 13 (B.1 Implementation Details) |
| For Flamingo, we initialize the model from the Flamingo9B checkpoint released in OpenFlamingo repository [2]. | p. 7 (5 Experiments) |
| LLaVA is a visual instruction tuning that connects a vision encoder and LLM for general-purpose visual and language understanding. | p. 7 (5 Experiments) |
| However, this paradigm consumes tremendous data, time, and GPU resources. | p. 3 (5. Facing the mirror and dress) |
| Specifically, we append 3D position embeddings to the extracted 3D features to better encode spatial information. | p. 3 (5. Facing the mirror and dress) |
| Furthermore, for 3D scenes, there are no available pretrained encoders like those for 2D images (e.g., CLIP ViT encoders). | p. 5 (5. Facing the mirror and dress) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 6 Conclusion - extractive PDF cue:** A limitation is that the 3D feature extractor relies on 2D multi-view images, and thus all 3D scenes need to be rendered so that they ...
- **p. 7 / 5 Experiments - extractive PDF cue:** We report BLEU, ROUGE-L, METEOR, CIDEr for robust answer matching.

- **PDF anchors reviewed:** datasets p. 7 (5 Experiments), p. 7 (5 Experiments), p. 8 (5 Experiments), p. 8 (5 Experiments), p. 9 (5 Experiments), p. 9 (5 Experiments), metrics p. 7 (5 Experiments), p. 7 (5 Experiments), p. 8 (5 Experiments), p. 8 (5 Experiments), p. 13 (B.1 Implementation Details), p. 14 (B.1 Implementation Details), baselines p. 7 (Figure/Table caption), p. 8 (5 Experiments), p. 14 (Figure/Table caption), p. 8 (Figure/Table caption), p. 16 (Figure/Table caption), p. 7 (5 Experiments), results p. 8 (5 Experiments), p. 14 (Figure/Table caption), p. 7 (5 Experiments), p. 8 (5 Experiments), p. 16 (Figure/Table caption), p. 7 (5 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
