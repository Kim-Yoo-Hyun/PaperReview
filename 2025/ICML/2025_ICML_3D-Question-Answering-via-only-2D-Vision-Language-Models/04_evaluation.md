# Evaluation - 3D Question Answering via only 2D Vision-Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=IkhJApkJQ3; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/168051. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (Figure/Table caption), p. 4 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 8 (Figure/Table caption), p. 9 (Figure/Table caption)): Figure 5: Our viewAnnotator module operates in two steps: Caption Generation and View Matching (illustrated by light green boxes indicating outputs at each step). In Step 1, LVLMs processes question-answer ...

## Evaluation Body Digest

- **p. 7 / 5. Experiments - extractive body cue:** ScanQA contains over 41K question-answer annotations across 800 indoor 3D scenes, which are divided into train, val, and test sets (with or without objects).
- **p. 7 / 5. Experiments - extractive body cue:** SQA contains over 33K questionanswer pairs derived from 650 indoor scenes.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Performance comparisons with the state-of-the-art methods on the test set of ScanQA (Azuma et al., 2022) and SQA (Ma et al., 2022). For ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 5: Our viewAnnotator module operates in two steps: Caption Generation and View Matching (illustrated by light green boxes indicating outputs at each step). In ...
- **p. 7 / 5. Experiments - extractive body cue:** Furthermore, since the answers in ScanQA are often free-form, we use standard text similarity metrics, including BLEU-1 (Papineni et al., 2002), ROUGE-L (Lin, 2004), and ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: An ablation study performed on ScanQA. We show the best EM@1 scores with the corresponding (optimal) k. selected views is shown in Figure ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 3: Computational performance comparison between image retrieval and cdViews for zero-shot 3D-QA. loss spatially close views, and thus miss critical information. cdViews's Efficiency. We ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 4: Performance comparison of view selection methods on the validation set of ScanQA (Azuma et al., 2022). It can be observed that: 1) performance ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5. Experiments (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 5: Our viewAnnotator module operates in two steps: Caption Generation and View Matching (illustrated by light green boxes indicating outputs at each step). ... | p. 5 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 4: Performance comparison of view selection methods on the validation set of ScanQA (Azuma et al., 2022). It can be observed that: 1) ... | p. 4 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 1: Performance comparisons with the state-of-the-art methods on the test set of ScanQA (Azuma et al., 2022) and SQA (Ma et al., 2022). ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 7: The results of EM@1 using two configurations: optimal k (blue) vs. fixed k=9 (green). X-axis is the thresh- old T of viewNMS. ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 2: An ablation study performed on ScanQA. We show the best EM@1 scores with the corresponding (optimal) k. selected views is shown in ... | p. 8 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 7 / 5. Experiments - extractive body cue:** ScanQA contains over 41K question-answer annotations across 800 indoor 3D scenes, which are divided into train, val, and test sets (with or without objects).
- **p. 7 / 5. Experiments - extractive body cue:** SQA contains over 33K questionanswer pairs derived from 650 indoor scenes.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Comparison of 3D Question Answering meth- ods. (a): a1 for 3D-based methods; a2 and a3 for hybrid (2D+3D) methods. All of these methods ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2: Comparison of view selection methods. (cdViews) and then use them to perform LVLMs-based 3D-QA in a zero-shot manner. cdViews is designed on two ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: The pipeline of zero-shot 3D-QA using three different view selection methods: uniform sampling (option ①), image retrieval (option ②), and our cdViews (option ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 4: Performance comparison of view selection methods on the validation set of ScanQA (Azuma et al., 2022). It can be observed that: 1) performance ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 5: Our viewAnnotator module operates in two steps: Caption Generation and View Matching (illustrated by light green boxes indicating outputs at each step). In ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Performance comparisons with the state-of-the-art methods on the test set of ScanQA (Azuma et al., 2022) and SQA (Ma et al., 2022). For ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6: Qualitative results for BridgeQA (Mo & Liu, 2024), LLAVA-OV + Fretrieval, and our final model LLAVA-OV + FcdViews. The marks , , and ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: An ablation study performed on ScanQA. We show the best EM@1 scores with the corresponding (optimal) k. selected views is shown in Figure ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | ScanQA contains over 41K question-answer annotations across 800 indoor 3D scenes, which are divided into train, val, and test sets (with or without objects). | embodiment, simulator version and control stack | p. 7 (5. Experiments), p. 7 (5. Experiments) |
| Task/environment | SQA contains over 33K questionanswer pairs derived from 650 indoor scenes. | reset, timeout, object/scene variation | p. 7 (5. Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 6 (3. Preliminaries), p. 3 (3. Preliminaries) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (1. Introduction), p. 4 (3. Preliminaries) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 1: Performance comparisons with the state-of-the-art methods on the test set of ScanQA (Azuma et al., 2022) and SQA (Ma et al., 2022). ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 5: Our viewAnnotator module operates in two steps: Caption Generation and View Matching (illustrated by light green boxes indicating outputs at each step). ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Furthermore, since the answers in ScanQA are often free-form, we use standard text similarity metrics, including BLEU-1 (Papineni et al., 2002), ROUGE-L (Lin, 2004), ... | definition/direction/unit from same section | p. 7 (5. Experiments) |
| Table 2: An ablation study performed on ScanQA. We show the best EM@1 scores with the corresponding (optimal) k. selected views is shown in ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Table 3: Computational performance comparison between image retrieval and cdViews for zero-shot 3D-QA. loss spatially close views, and thus miss critical information. cdViews's Efficiency. ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Figure 4: Performance comparison of view selection methods on the validation set of ScanQA (Azuma et al., 2022). It can be observed that: 1) ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Figure 3: The pipeline of zero-shot 3D-QA using three different view selection methods: uniform sampling (option ①), image retrieval (option ②), and our cdViews ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Figure 7: The results of EM@1 using two configurations: optimal k (blue) vs. fixed k=9 (green). X-axis is the thresh- old T of viewNMS. ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 5: Our viewAnnotator module operates in two steps: Caption Generation and View Matching (illustrated by light green boxes indicating outputs at each step). ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |
| Table 1: Performance comparisons with the state-of-the-art methods on the test set of ScanQA (Azuma et al., 2022) and SQA (Ma et al., 2022). ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| ScanQA contains over 41K question-answer annotations across 800 indoor 3D scenes, which are divided into train, val, and test sets (with or without objects). | comparison identity and matched condition | p. 7 (5. Experiments) |
| Table 2: An ablation study performed on ScanQA. We show the best EM@1 scores with the corresponding (optimal) k. selected views is shown in ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Figure 1: Comparison of 3D Question Answering meth- ods. (a): a1 for 3D-based methods; a2 and a3 for hybrid (2D+3D) methods. All of these ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| Figure 2: Comparison of view selection methods. (cdViews) and then use them to perform LVLMs-based 3D-QA in a zero-shot manner. cdViews is designed on ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| ScanQA contains over 41K question-answer annotations across 800 indoor 3D scenes, which are divided into train, val, and test sets (with or without objects). | component/input/data sensitivity | p. 7 (5. Experiments) |
| Table 1: Performance comparisons with the state-of-the-art methods on the test set of ScanQA (Azuma et al., 2022) and SQA (Ma et al., 2022). ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Table 2: An ablation study performed on ScanQA. We show the best EM@1 scores with the corresponding (optimal) k. selected views is shown in ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Figure 7: The results of EM@1 using two configurations: optimal k (blue) vs. fixed k=9 (green). X-axis is the thresh- old T of viewNMS. ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We propose cdViews, a novel approach to automatically selecting critical and diverse Views for 3D-QA. cdViews consists of two key components: viewSelector prioritizing critical ... | Figure 5: Our viewAnnotator module operates in two steps: Caption Generation and View Matching (illustrated by light green boxes indicating outputs at each step). ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (Figure/Table caption), p. 4 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 8 (Figure/Table caption), p. 9 (Figure/Table caption) |
| Primary metric/result | Figure 4: Performance comparison of view selection methods on the validation set of ScanQA (Azuma et al., 2022). It can be observed that: 1) ... | numeric claim only at cited anchor | p. 4 (Figure/Table caption) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The reason is that the uniform sampling method ignores the question and the image retrieval method often fails to capture critical views or introduces ... | p. 7 (5.1. Comparisons with the State-of-the-Arts) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Training of the viewSelector is conducted with a learning rate of 5 × 10-5 and a batch size of | p. 7 (5. Experiments) |
| 4.1. viewAnnotator The implementation of viewAnnotator has two steps: caption generation and view matching, as shown in Figure 5. | p. 5 (3. Preliminaries) |
| The code is available at https: //github.com/fereenwong/cdViews. | p. 1 (Abstract) |
| During our preliminary trials, we identified several challenges. | p. 2 (1. Introduction) |
| For implementation, we first select a limited number of 2D views, and then take them as the only visual input to LVLMs to answer ... | p. 2 (1. Introduction) |
| As for inference, our cdViews has two modules to run: the viewSelector identifies critical views, and the viewNMS enhances view diversity and minimizes redundancy. | p. 4 (3. Preliminaries) |
| The training of viewSelector contains two steps: data annotation and model training. | p. 5 (3. Preliminaries) |
| 4.2. viewSelector As shown in Figure 3, viewSelector is plugged between the visual encoder and LVLM to select "views" in the feature space. | p. 6 (3. Preliminaries) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 5.1. Comparisons with the State-of-the-Arts - extractive body cue:** The reason is that the uniform sampling method ignores the question and the image retrieval method often fails to capture critical views or introduces redundancy ...

- **Evidence anchors reviewed:** datasets p. 7 (5. Experiments), p. 7 (5. Experiments), metrics p. 7 (Figure/Table caption), p. 5 (Figure/Table caption), p. 7 (5. Experiments), p. 8 (Figure/Table caption), p. 9 (Figure/Table caption), p. 4 (Figure/Table caption), baselines p. 5 (Figure/Table caption), p. 7 (Figure/Table caption), p. 7 (5. Experiments), p. 8 (Figure/Table caption), p. 1 (Figure/Table caption), p. 2 (Figure/Table caption), results p. 5 (Figure/Table caption), p. 4 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 8 (Figure/Table caption), p. 9 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
