# Evaluation - GaussianVLM: Scene-Centric 3D Vision-Language Models Using Language-Aligned Gaussian Splats for Embodied Reasoning and Beyond

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html; PDF retrieval source: https://arxiv.org/pdf/2507.00886. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 10 (Figure/Table caption)): On the scene-centric SQA3D benchmark, GaussianVLM achieves an exact match accuracy of 49.4%, surpassing LEO's 47.0% by 2.4 percentage points.

## Evaluation Body Digest

- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Scene-Centric Tasks, in contrast, require holistic reasoning about the environment, its layout, and the agent's situated context-without reducing the scene to individual object tokens.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** We align the visual and language modalities using the ReferIt3D dataset [1] providing detailed object captions.
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** Dataset We evaluate our model under the LL3DA, a SOTA 3D VLM, training protocol [9].
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** We also evaluate on embodied reasoning (SQA3D [30]), a popular 3D VLM benchmark [23], [56], where we follow the LEO [23] training protocol.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Embodied Dialogue Embodied Planning Scene Captioning Sim
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** ROUGE captures structural similarity and emphasizes recall without over-rewarding redundant context.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Consequently, BLEU and CIDEr can assign misleadingly high scores to captions that correctly describe the scene context but identify the wrong object.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** On the scene-centric SQA3D benchmark, GaussianVLM achieves an exact match accuracy of 49.4%, surpassing LEO's 47.0% by 2.4 percentage points.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** IV. EXPERIMENTS (p. 4).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| IV. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | On the scene-centric SQA3D benchmark, GaussianVLM achieves an exact match accuracy of 49.4%, surpassing LEO's 47.0% by 2.4 percentage points. | p. 5 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Results and Analysis The evaluation results, shown in Tab. | p. 5 (IV. EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 3: Qualitative results on scene-centric tasks. | p. 10 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Scene-Centric Tasks, in contrast, require holistic reasoning about the environment, its layout, and the agent's situated context-without reducing the scene to individual object tokens.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** We align the visual and language modalities using the ReferIt3D dataset [1] providing detailed object captions.
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** Dataset We evaluate our model under the LL3DA, a SOTA 3D VLM, training protocol [9].
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** We also evaluate on embodied reasoning (SQA3D [30]), a popular 3D VLM benchmark [23], [56], where we follow the LEO [23] training protocol.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Embodied Dialogue Embodied Planning Scene Captioning Sim

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: The proposed GaussianVLM performs comprehensive scene understanding in natural language for 3D scenes represented as Gaussian Splats. It adopts a fully scene-centric approach, ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: The GaussianVLM architecture processes a user task prompt (query and optional location) and a 3D scene (Gaussian Splat representation). A 3D vision module ...
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 3: Qualitative results on scene-centric tasks.
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 4: Qualitative results on object-centric tasks. Task
- **p. 13 / Figure/Table caption - extractive body cue:** Fig. 5: Distribution of the questions on object counts, answered correctly by GaussianVLM. The distribution is according to object class labels. Overall, 254 questions answered ...
- **p. 13 / Figure/Table caption - extractive body cue:** Fig. 6: Distribution of the questions on object counts, answered correctly by LL3DA. The distribution is according to object class labels. Overall, 44 questions answered ...
- **p. 14 / Figure/Table caption - extractive body cue:** Fig. 7: Distribution of object count questions (correcly answered by GaussianVLM, vs all questions) according to object class labels.
- **p. 15 / Figure/Table caption - extractive body cue:** Fig. 8: Distribution of object count questions (correcly answered by LL3DA, vs all questions) according to object class labels.

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Scene-Centric Tasks, in contrast, require holistic reasoning about the environment, its layout, and the agent's situated context-without reducing the scene to individual object tokens. | embodiment, simulator version and control stack | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Task/environment | We align the visual and language modalities using the ReferIt3D dataset [1] providing detailed object captions. | reset, timeout, object/scene variation | p. 5 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (III. METHOD), p. 3 (III. METHOD) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (III. METHOD), p. 4 (III. METHOD) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| ROUGE captures structural similarity and emphasizes recall without over-rewarding redundant context. | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| Consequently, BLEU and CIDEr can assign misleadingly high scores to captions that correctly describe the scene context but identify the wrong object. | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Implementation Details Following prior work, we represent each 3D scene using 40k randomly sampled Gaussians from the GaussianWorld [27] Gaussian splats scene. | comparison identity and matched condition | p. 5 (IV. EXPERIMENTS) |
| Dataset We evaluate our model under the LL3DA, a SOTA 3D VLM, training protocol [9]. | comparison identity and matched condition | p. 4 (IV. EXPERIMENTS) |
| ROUGE captures structural similarity and emphasizes recall without over-rewarding redundant context. | comparison identity and matched condition | p. 5 (IV. EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| ROUGE captures structural similarity and emphasizes recall without over-rewarding redundant context. | component/input/data sensitivity | p. 5 (IV. EXPERIMENTS) |
| To encourage linguistic diversity, we use GPT-4o to generate 40 paraphrased variants per prompt with varied syntax and vocabulary. | component/input/data sensitivity | p. 5 (IV. EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Overall, this work makes the following contributions: • We introduce a fully scene-centric 3D VLM that achieves SOTA results, without requiring any dependencies on ... | On the scene-centric SQA3D benchmark, GaussianVLM achieves an exact match accuracy of 49.4%, surpassing LEO's 47.0% by 2.4 percentage points. | PDF body cue; verify exact table/figure and matched conditions | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 10 (Figure/Table caption) |
| Primary metric/result | Results and Analysis The evaluation results, shown in Tab. | numeric claim only at cited anchor | p. 5 (IV. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Our training procedure adheres to the standard protocols: 5 epochs of alignment followed by 10 epochs of instruction tuning for LEO, and 32 epochs for ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Training completes in under one day on 8 A100-80 GPUs.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Additionally, we pre-train our task-guided sparsifier on the object captioning task for 5 epochs We employ the AdamW optimizer with a weight decay of 0.1 ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Evaluation is performed every 8 epochs for LL3DA and every epoch for LEO.
- **p. 4 / III. METHOD - extractive body cue:** The dual sparsifier comprises: 1) a location-guided pathway that selects language features from Gaussians within a ROI around the task location, producing ROI tokens; and ...
- **p. 4 / III. METHOD - extractive body cue:** To mitigate the computational overhead of cross-attention on a large number of tokens, we first apply a simple uniform downsampling strategy to reduce the representation ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | By directly embedding language features into the spatial structure of 3D scenes, GaussianVLM, overcomes the inherent limitations of object detector dependencies, enabling a more ... | p. 7 (V. CONCLUSION) |
| body limitation/failure cue | These tasks fall into two broad categories: object-centric and scene-centric, reflecting differing demands on spatial grounding and semantic abstraction. | p. 5 (IV. EXPERIMENTS) |
| body limitation/failure cue | SentenceBERT directly evaluates semantic similarity in embedding space for robustness to paraphrasing. | p. 5 (IV. EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Additionally, we pre-train our task-guided sparsifier on the object captioning task for 5 epochs We employ the AdamW optimizer with a weight decay of ... | p. 5 (IV. EXPERIMENTS) |
| Evaluation is performed every 8 epochs for LL3DA and every epoch for LEO. | p. 5 (IV. EXPERIMENTS) |
| The location is encoded through learnable Fourier embeddings (Eq. | p. 3 (III. METHOD) |
| Following established practices [9], [54], [19], [10], sampling 40k Gaussians yields a corresponding 40k output tokens, originating from different SceneSplat decoder layers (specifically, 589, ... | p. 3 (III. METHOD) |
| The decoder's hidden states also inform the task-guided sparsifier. | p. 4 (III. METHOD) |
| Corresponding to each SceneSplat decoder block is a cross-attention sparsifier block. | p. 4 (III. METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / V. CONCLUSION - extractive body cue:** By directly embedding language features into the spatial structure of 3D scenes, GaussianVLM, overcomes the inherent limitations of object detector dependencies, enabling a more natural ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** These tasks fall into two broad categories: object-centric and scene-centric, reflecting differing demands on spatial grounding and semantic abstraction.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** SentenceBERT directly evaluates semantic similarity in embedding space for robustness to paraphrasing.

- **Evidence anchors reviewed:** datasets p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), metrics p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), baselines p. 5 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), results p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 10 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
