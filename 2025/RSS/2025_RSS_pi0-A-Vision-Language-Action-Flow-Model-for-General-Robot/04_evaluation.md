# Evaluation - π0: A Vision-Language-Action Flow Model for General Robot Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> 2026-11-19 표본 감사에서 요약과 관련 본문 표현을 원문에 대조해 교정했다. [원문](https://arxiv.org/html/2410.24164)
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p010.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p010.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

사전학습한 기본 정책을 직접 실행한 조건과 특정 과제에 미세조정한 조건을 구별한다. 세탁물 접기는 여러 단계가 필요한 조작 실험의 한 예다. [원문](https://arxiv.org/html/2410.24164)

## Evaluation Body Digest

- **p. 7 / VI. EXPERIMENTAL EVALUATION - source paraphrase:** We study this question by directly evaluating π₀, with comparisons to other robot foundation models.
- **p. 7 / VI. EXPERIMENTAL EVALUATION - extractive body cue:** These tasks take between 5 and 20 minutes to complete.
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 9: Language evaluation. We compare "flat" versions of our policies, -flat, which receive only the overall task command (e.g, "bag the groceries") with ...
- **p. 7 / VI. EXPERIMENTAL EVALUATION - extractive body cue:** How well does xo follow language commands? ‘These experiments compare xo to xo-Small, a smaller version of our ‘model without VLM initialization, to evaluate its ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Our generalist robot policy uses a pre-trained vision-language model (VLM) backbone, as well as a diverse cross- ‘embodiment dataset with a variety of ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: Overview of our dataset: The pre-training mixture consists of a subset of OXE [10] and the 7 dataset. We use a subset of ...
- **p. 8 / Figure/Table caption - source paraphrase:** Fig. 7: Out-of-box evaluation results: We evaluate π₀ trained for the full 700k steps, a version trained for 160k steps that ‘matches the number of ...
- **p. 11 / C. Learning new dexterous tasks - extractive body cue:** DISCUSSION, LIMITATIONS, AND FUTURE WORK

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** VI. EXPERIMENTAL EVALUATION (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 9: Language evaluation. We compare "flat" versions of our policies, -flat, which receive only the overall task command (e.g, "bag the groceries") ... | p. 9 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 7: Out-of-box evaluation results: We evaluate π₀ trained for the full 700k steps, a version trained for 160k steps that ‘matches the number ... | p. 8 (Figure/Table caption) |
| VI. EXPERIMENTAL EVALUATION | EMPIRICAL / SOURCE-REPORTED EVALUATION | How well does xo follow language commands? ‘These experiments compare xo to xo-Small, a smaller version of our ‘model without VLM initialization, to evaluate ... | p. 7 (VI. EXPERIMENTAL EVALUATION) |

## Dataset / Benchmark Role

- **p. 7 / VI. EXPERIMENTAL EVALUATION - source paraphrase:** We study this question by directly evaluating π₀, with comparisons to other robot foundation models.
- **p. 7 / VI. EXPERIMENTAL EVALUATION - extractive body cue:** These tasks take between 5 and 20 minutes to complete.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Our generalist robot policy uses a pre-trained vision-language model (VLM) backbone, as well as a diverse cross- ‘embodiment dataset with a variety of ...
- **p. 2 / Figure/Table caption - source paraphrase:** Fig. 2: π₀ controls a mobile manipulator to fold laundry. Our model is pre-trained on diverse data from 7 distinet robot configurations and 68 tasks, ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Overview of our framework. We start with pre-training mixture, which consists of both our own dexterous ‘manipulation datasets and open-source data, We use ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: Overview of our dataset: The pre-training mixture consists of a subset of OXE [10] and the 7 dataset. We use a subset of ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: The robots used in our experiments. These include single and dual-arm manipulators with 6-DoF and 7-DoF arms, as well as holonomic and nonholonomic ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: Out-of-box evaluation tasks: To evaluate our base ‘model, we run it after pre-training on five tasks: shirt folding, bussing easy, bussing hard, grocery ...
- **p. 8 / Figure/Table caption - source paraphrase:** Fig. 7: Out-of-box evaluation results: We evaluate π₀ trained for the full 700k steps, a version trained for 160k steps that ‘matches the number of ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 8: The tasks in our language evaluation, We evaluate our model on 3 different language-conditioned tasks, each of Which requires following a sequence of ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We study this question by directly evaluating π₀, with comparisons to other robot foundation models. | embodiment, simulator version and control stack | p. 7 (VI. EXPERIMENTAL EVALUATION), p. 7 (VI. EXPERIMENTAL EVALUATION) |
| Task/environment | These tasks take between 5 and 20 minutes to complete. | reset, timeout, object/scene variation | p. 7 (VI. EXPERIMENTAL EVALUATION) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 5 (IV. THE x MODEL), p. 4 (IV. THE x MODEL) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 3 (1. INTRODUCTION), p. 2 (1. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Fig. 9: Language evaluation. We compare "flat" versions of our policies, -flat, which receive only the overall task command (e.g, "bag the groceries") ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| How well does xo follow language commands? ‘These experiments compare xo to xo-Small, a smaller version of our ‘model without VLM initialization, to evaluate ... | definition/direction/unit from same section | p. 7 (VI. EXPERIMENTAL EVALUATION) |
| Fig. 1: Our generalist robot policy uses a pre-trained vision-language model (VLM) backbone, as well as a diverse cross- ‘embodiment dataset with a variety ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Fig. 4: Overview of our dataset: The pre-training mixture consists of a subset of OXE [10] and the 7 dataset. We use a subset ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Fig. 7: Out-of-box evaluation results: We evaluate π₀ trained for the full 700k steps, a version trained for 160k steps that ‘matches the number ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| We study this question by directly evaluating π₀, with comparisons to other robot foundation models. | comparison identity and matched condition | p. 7 (VI. EXPERIMENTAL EVALUATION) |
| How well does xo follow language commands? ‘These experiments compare xo to xo-Small, a smaller version of our ‘model without VLM initialization, to evaluate ... | comparison identity and matched condition | p. 7 (VI. EXPERIMENTAL EVALUATION) |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| How well does xo follow language commands? ‘These experiments compare xo to xo-Small, a smaller version of our ‘model without VLM initialization, to evaluate ... | component/input/data sensitivity | p. 7 (VI. EXPERIMENTAL EVALUATION) |
| Fig. 9: Language evaluation. We compare "flat" versions of our policies, -flat, which receive only the overall task command (e.g, "bag the groceries") ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |
| In our final set of experiments, we fine-tune 9 to a set of particularly ‘complex tasks, including folding laundry and bussing a table. | component/input/data sensitivity | p. 7 (VI. EXPERIMENTAL EVALUATION) |
| Fig. 10: Fine-tuning evaluation tasks: We fine-tune our model to a variety of downstream tasks that are distinct from, the tasks seen in pre-training. ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |
| Fig. 1: Our generalist robot policy uses a pre-trained vision-language model (VLM) backbone, as well as a diverse cross- ‘embodiment dataset with a variety ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |
| Fig. 2: π₀ controls a mobile manipulator to fold laundry. Our model is pre-trained on diverse data from 7 distinet robot configurations and 68 ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| π₀ combines a pretrained VLM with a flow-matching action expert and is evaluated on multistage tasks including laundry folding. | Fig. 9: Language evaluation. We compare "flat" versions of our policies, -flat, which receive only the overall task command (e.g, "bag the groceries") ... | PDF body cue; verify exact table/figure and matched conditions | p. 9 (Figure/Table caption), p. 8 (Figure/Table caption), p. 7 (VI. EXPERIMENTAL EVALUATION) |
| Primary metric/result | Fig. 7: Out-of-box evaluation results: We evaluate π₀ trained for the full 700k steps, a version trained for 160k steps that ‘matches the number ... | numeric claim only at cited anchor | p. 8 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 6 / A. Prectraining and post-training - extractive body cue:** y2 [52], and DROID [23]. ‘The robots and tasks in these datasets typically have one or two cameras and use lowfrequency control, between 2 and ...
- **p. 6 / A. Prectraining and post-training - extractive body cue:** This data has 68 tasks, where each task is composed of ‘complex behaviors - e.g., the "bussing" task involves putting a wide range of different ...
- **p. 6 / A. Prectraining and post-training - extractive body cue:** Different tasks require very different datasets, with the simplest of the tasks necessitating only 5 hours and the most complex tasks using 100 or more ...
- **p. 7 / A. Evaluating the base model - extractive body cue:** The evaluation metric uses normalized score averaged over 10 episodes per task and method, where an episode receives « score of 1.0 for full success, ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | DISCUSSION, LIMITATIONS, AND FUTURE WORK | p. 11 (C. Learning new dexterous tasks) |
| body limitation/failure cue | This presents challenges due to the egg shape, slipperiness, and the need for careful placement. | p. 10 (C. Learning new dexterous tasks) |

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The left figure illustrates their relative sizes as measured by the number of steps. | p. 5 (A. Prectraining and post-training) |
| Since each training example corresponds to a timestep - i.e. a tuple (0, A), - we will quantify data in terms of timesteps in ... | p. 5 (A. Prectraining and post-training) |
| To earn dexterous and more complex tasks, we also use 903M timesteps of data from our own datasets, where 106M steps are from single-arm ... | p. 6 (A. Prectraining and post-training) |
| 6: Out-of-box evaluation tasks: To evaluate our base ‘model, we run it after pre-training on five tasks: shirt folding, bussing easy, bussing hard, grocery ... | p. 7 (VI. EXPERIMENTAL EVALUATION) |
| We therefore also compare to a "compute parity" version of our model, which is tained for only 160k steps (as opposed to 700K steps ... | p. 7 (A. Evaluating the base model) |
| Following the standard late fusion VLM recipe [3, 11, 30], image encoders embed the robot's image observations into the same embedding space as language ... | p. 4 (IV. THE x MODEL) |
| 7: Out-of-box evaluation results: We evaluate π₀ trained for the full 700k steps, a version trained for 160k steps that ‘matches the number of ... | p. 8 (A. Evaluating the base model) |

## Limitations and Verification Questions

- **p. 11 / C. Learning new dexterous tasks - extractive body cue:** DISCUSSION, LIMITATIONS, AND FUTURE WORK
- **p. 10 / C. Learning new dexterous tasks - extractive body cue:** This presents challenges due to the egg shape, slipperiness, and the need for careful placement.

- **Evidence anchors reviewed:** datasets p. 7 (VI. EXPERIMENTAL EVALUATION), p. 7 (VI. EXPERIMENTAL EVALUATION), metrics p. 9 (Figure/Table caption), p. 7 (VI. EXPERIMENTAL EVALUATION), p. 1 (Figure/Table caption), p. 5 (Figure/Table caption), baselines p. 8 (Figure/Table caption), p. 7 (VI. EXPERIMENTAL EVALUATION), p. 7 (VI. EXPERIMENTAL EVALUATION), results p. 9 (Figure/Table caption), p. 8 (Figure/Table caption), p. 7 (VI. EXPERIMENTAL EVALUATION).

[공통 검토 기준](../../../research/READING_STATUS.md#note-checks)

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Fig. 7: Out-of-box evaluation results: We evaluate π₀ trained for the full 700k steps, a version trained for 160k steps that ‘matches the number of updates for baseline models, x-small, ... (p. 8, Figure/Table caption).
- **Metric evidence:** How well does xo follow language commands? ‘These experiments compare xo to xo-Small, a smaller version of our ‘model without VLM initialization, to evaluate its performance ‘on following language commands. (p. 7, VI. EXPERIMENTAL EVALUATION).
- **Baseline/ablation evidence:** We study this question by directly evaluating π₀, with comparisons to other robot foundation models. (p. 7, VI. EXPERIMENTAL EVALUATION).
- **Failure/negative evidence:** OpenVLA struggles on these tasks because its autoregressive diseretization architecture does not support action chunks. (p. 7, A. Evaluating the base model).
