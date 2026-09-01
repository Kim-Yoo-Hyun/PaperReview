# Evaluation - Vision-and-Language Navigation: Interpreting Visually-Grounded Navigation Instructions in Real Environments

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1711.07280; PDF retrieval source: https://arxiv.org/pdf/1711.07280. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (6. Results), p. 8 (6. Results), p. 7 (6. Results), p. 8 (6. Results), p. 5 (4.4. Evaluation Protocol), p. 6 (4.4. Evaluation Protocol)): As illustrated in Table 1, our exploitative RANDOM agent achieves an average success rate of 13.2% on the test set (which appears to be slightly more challenging than the validation ...

## Evaluation Body Digest

- **p. 3 / 3.1. Matterport3D Dataset - extractive PDF cue:** These datasets typically offer only one or two paths through a scene, making them inadequate for simulating robot motion.
- **p. 3 / 3.1. Matterport3D Dataset - extractive PDF cue:** Many of the scenes in the dataset can be viewed in the Matterport 3D spaces gallery2.
- **p. 6 / 4.4. Evaluation Protocol - extractive PDF cue:** We reserve an additional 11 scenes and 2,349 instructions for validating in unseen environments (val unseen).
- **p. 6 / 4.4. Evaluation Protocol - extractive PDF cue:** The remaining 61 scenes are pooled together, with instructions split 14,025 train / 1,020 val seen.
- **p. 5 / 4.3. R2R Dataset Analysis - extractive PDF cue:** This likely reflects differences in people's mental models of the way a ‘smart robot' works [43], making the handling of these differences an important aspect ...
- **p. 5 / 4.3. R2R Dataset Analysis - extractive PDF cue:** Although we use the R2R dataset in conjunction with the Matterport3D Simulator, we see no technical reason why this dataset couldn't also be used with ...
- **p. 7 / 6. Results - extractive PDF cue:** In comparison, AMT workers achieve 86.4% success on the test set, illustrating the high quality of the dataset instructions.
- **p. 8 / 6. Results - extractive PDF cue:** The techniques and practices used to optimize performance on existing vision and language datasets are unlikely to be sufficient for models that are expected to ...

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** 3.1. Matterport3D Dataset (p. 3); 4.3. R2R Dataset Analysis (p. 5); 4.4. Evaluation Protocol (p. 5); 6. Results (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 6. Results | BENCHMARK / DATASET | As illustrated in Table 1, our exploitative RANDOM agent achieves an average success rate of 13.2% on the test set (which appears to be ... | p. 7 (6. Results) |
| 6. Results | BENCHMARK / DATASET | Both methods improve significantly over the RANDOM baseline, as illustrated in Figure 8. | p. 8 (6. Results) |
| 6. Results | BENCHMARK / DATASET | In comparison, AMT workers achieve 86.4% success on the test set, illustrating the high quality of the dataset instructions. | p. 7 (6. Results) |
| 6. Results | BENCHMARK / DATASET | Even using strong regularization (dropout and weight decay), performance in unseen environments plateaus quickly, but further training continues to improve performance in the training ... | p. 8 (6. Results) |
| 4.4. Evaluation Protocol | BENCHMARK / DATASET | One of the strengths of the R2R task is that, in contrast to many other vision and language tasks such as image captioning and ... | p. 5 (4.4. Evaluation Protocol) |

## Dataset / Benchmark Role

- **p. 3 / 3.1. Matterport3D Dataset - extractive PDF cue:** These datasets typically offer only one or two paths through a scene, making them inadequate for simulating robot motion.
- **p. 3 / 3.1. Matterport3D Dataset - extractive PDF cue:** Many of the scenes in the dataset can be viewed in the Matterport 3D spaces gallery2.
- **p. 6 / 4.4. Evaluation Protocol - extractive PDF cue:** We reserve an additional 11 scenes and 2,349 instructions for validating in unseen environments (val unseen).
- **p. 6 / 4.4. Evaluation Protocol - extractive PDF cue:** The remaining 61 scenes are pooled together, with instructions split 14,025 train / 1,020 val seen.
- **p. 5 / 4.3. R2R Dataset Analysis - extractive PDF cue:** This likely reflects differences in people's mental models of the way a ‘smart robot' works [43], making the handling of these differences an important aspect ...
- **p. 5 / 4.3. R2R Dataset Analysis - extractive PDF cue:** Although we use the R2R dataset in conjunction with the Matterport3D Simulator, we see no technical reason why this dataset couldn't also be used with ...
- **p. 7 / 6. Results - extractive PDF cue:** In comparison, AMT workers achieve 86.4% success on the test set, illustrating the high quality of the dataset instructions.
- **p. 8 / 6. Results - extractive PDF cue:** The techniques and practices used to optimize performance on existing vision and language datasets are unlikely to be sufficient for models that are expected to ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Room-to-Room (R2R) navigation task. We focus on executing natural language navigation instructions in previously unseen real-world buildings. The agent's camera can be rotated ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2. Differences between Vision-and-Language Navigation (VLN) and Visual Question Answering (VQA). Both tasks can be formu- lated as visually grounded sequence-to-sequence transcoding problems. However, ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. Example navigation graph for a partial floor of one building-scale scene in the Matterport3D Simulator. Navigable paths between panoramic viewpoints are illustrated in ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4. Randomly selected examples of navigation instructions (three per trajectory) shown with the view from the starting pose. tion at leading to a new ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 5. Distribution of instruction length and navigation trajec- tory length in the R2R dataset. end, we provide workers with an interactive 3D WebGL en- ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 6. Although we use the R2R dataset in conjunction with the Matterport3D Simulator, we see no technical rea- son why this dataset couldn't also ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 6. Distribution of navigation instructions based on their first four words. Instructions are read from the center outwards. Arc lengths are proportional to the ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1. Average R2R navigation results using evaluation metrics defined in Section 4.4. Our seq-2-seq model trained with student- forcing achieves promising results in previously ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | These datasets typically offer only one or two paths through a scene, making them inadequate for simulating robot motion. | embodiment, simulator version and control stack | p. 3 (3.1. Matterport3D Dataset), p. 3 (3.1. Matterport3D Dataset) |
| Task/environment | Many of the scenes in the dataset can be viewed in the Matterport 3D spaces gallery2. | reset, timeout, object/scene variation | p. 3 (3.1. Matterport3D Dataset), p. 6 (4.4. Evaluation Protocol) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 6 (5.1. Sequence-to-Sequence Model), p. 2 (1. Introduction) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 6 (5.1. Sequence-to-Sequence Model), p. 7 (5.2. Training) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Validation loss, navigation error and success rate during training. | definition/direction/unit from same section | p. 8 (6. Results) |
| As illustrated in Table 1, our exploitative RANDOM agent achieves an average success rate of 13.2% on the test set (which appears to be ... | definition/direction/unit from same section | p. 7 (6. Results) |
| Using the student-forcing approach we establish the first test set leaderboard result achieving a 20.4% success rate. | definition/direction/unit from same section | p. 8 (6. Results) |
| We define navigation error as the shortest path distance in the navigation graph G between the agent's final position vT | definition/direction/unit from same section | p. 5 (4.4. Evaluation Protocol) |
| We consider an episode to be a success if the navigation error is less than 3m. | definition/direction/unit from same section | p. 6 (4.4. Evaluation Protocol) |
| This threshold allows for a margin of error of approximately one viewpoint, yet it is comfortably below the minimum starting error of 5m. | definition/direction/unit from same section | p. 6 (4.4. Evaluation Protocol) |
| One of the strengths of the R2R task is that, in contrast to many other vision and language tasks such as image captioning and ... | definition/direction/unit from same section | p. 5 (4.4. Evaluation Protocol) |
| In comparison, AMT workers achieve 86.4% success on the test set, illustrating the high quality of the dataset instructions. | definition/direction/unit from same section | p. 7 (6. Results) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| To disentangle the problem of recognizing the goal location, we also report success for each agent under an oracle stopping rule, i.e. if the ... | comparison identity and matched condition | p. 6 (4.4. Evaluation Protocol) |
| Both methods improve significantly over the RANDOM baseline, as illustrated in Figure 8. | comparison identity and matched condition | p. 8 (6. Results) |
| In comparison, AMT workers achieve 86.4% success on the test set, illustrating the high quality of the dataset instructions. | comparison identity and matched condition | p. 7 (6. Results) |
| Figure 3. Example navigation graph for a partial floor of one building-scale scene in the Matterport3D Simulator. Navigable paths between panoramic viewpoints are illustrated ... | comparison identity and matched condition | p. 4 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 3. Example navigation graph for a partial floor of one building-scale scene in the Matterport3D Simulator. Navigable paths between panoramic viewpoints are illustrated ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To enable the reproducible evaluation of VLN methods, we present the Matterport3D Simulator. | As illustrated in Table 1, our exploitative RANDOM agent achieves an average success rate of 13.2% on the test set (which appears to be ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (6. Results), p. 8 (6. Results), p. 7 (6. Results), p. 8 (6. Results), p. 5 (4.4. Evaluation Protocol), p. 6 (4.4. Evaluation Protocol) |
| Primary metric/result | Both methods improve significantly over the RANDOM baseline, as illustrated in Figure 8. | numeric claim only at cited anchor | p. 8 (6. Results) |

- Numeric sentences retained from the body:
- **p. 6 / 4.4. Evaluation Protocol - extractive PDF cue:** The test set consists of 18 scenes, and 4,173 instructions.
- **p. 6 / 4.4. Evaluation Protocol - extractive PDF cue:** We reserve an additional 11 scenes and 2,349 instructions for validating in unseen environments (val unseen).
- **p. 6 / 4.4. Evaluation Protocol - extractive PDF cue:** The remaining 61 scenes are pooled together, with instructions split 14,025 train / 1,020 val seen.
- **p. 6 / 5.1. Sequence-to-Sequence Model - extractive PDF cue:** The left, right, up and down actions are defined to move the camera by 30 degrees.
- **p. 7 / 5.2. Training - extractive PDF cue:** We set the simulator image resolution to 640 × 480 with a vertical field of view of 60 degrees.
- **p. 7 / 5.2. Training - extractive PDF cue:** As we have discretized the agent's heading and elevation changes in 30 degree increments, for fast training we extract and pre-cache all CNN feature vectors.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Nevertheless, people are not infallible when it comes to navigation. | p. 7 (6. Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We train in PyTorch using the Adam optimizer [28] with weight decay and a batch size of 100. | p. 7 (5.2. Training) |
| Implementation Details We perform only minimal text pre-processing, converting all sentences to lower case, tokenizing on white space, and filtering words that do not ... | p. 7 (5.2. Training) |
| The encoder computes a representation of ¯x. | p. 6 (5.1. Sequence-to-Sequence Model) |
| These buildings contain enormous visual diversity, posing real challenges to computer vision. | p. 3 (3.1. Matterport3D Dataset) |
| The decoder LSTM operates as h ′ t = LSTMdec (qt, h ′ t-1). | p. 6 (5.1. Sequence-to-Sequence Model) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 6. Results - extractive PDF cue:** Nevertheless, people are not infallible when it comes to navigation.

- **PDF anchors reviewed:** datasets p. 3 (3.1. Matterport3D Dataset), p. 3 (3.1. Matterport3D Dataset), p. 6 (4.4. Evaluation Protocol), p. 6 (4.4. Evaluation Protocol), p. 5 (4.3. R2R Dataset Analysis), p. 5 (4.3. R2R Dataset Analysis), metrics p. 8 (6. Results), p. 7 (6. Results), p. 8 (6. Results), p. 5 (4.4. Evaluation Protocol), p. 6 (4.4. Evaluation Protocol), p. 6 (4.4. Evaluation Protocol), baselines p. 6 (4.4. Evaluation Protocol), p. 8 (6. Results), p. 7 (6. Results), p. 4 (Figure/Table caption), results p. 7 (6. Results), p. 8 (6. Results), p. 7 (6. Results), p. 8 (6. Results), p. 5 (4.4. Evaluation Protocol), p. 6 (4.4. Evaluation Protocol).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
