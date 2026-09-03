# Evaluation - Bridging Perception and Action: Spatially-Grounded Mid-Level Representations for Robot Generalization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p155.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p155.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 1 (Figure/Table caption), p. 6 (Figure/Table caption), p. 8 (Figure/Table caption)): Fig. 1: Bimanual, dexterous manipulation requires task-specifie grounding, The left depicts various axes for spatial gr ‘qualitative categorizations of different mid-level representations. Different representations lead to different lev ...

## Evaluation Body Digest

- **p. 7 / C. Experiment Setup - extractive body cue:** For RT-H, ‘we relabel robot demonstrations with the language "move the arm leftright/up/down." For each environment in simulation and the real-world, we vary the object ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Bimanual, dexterous manipulation requires task-specifie grounding, The left depicts various axes for spatial gr ‘qualitative categorizations of different mid-level representations. Different representations lead ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: Self-Consistency. On the left image, the robot's achieved trajectory doesn't match it's mid-level representation, which leads to a lower weight. In the right, ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 8: Real-World Results. There are clear differences in the benefits that different representations provide for tasks in the real world.
- **p. 6 / 4) Which policy architecture offers the best tradeoff be - extractive body cue:** tween responsiveness to structured mid-level representations and robustness to noise or spurious inputs?
- **p. 9 / C. Different Architectures offer Different Tradeoffs berween - extractive body cue:** Meanwhile, Table I! records the sensitivity scores for each of our mid-level experts as well as the robustness index. ‘The robustness index is computed by ...
- **p. 9 / C. Different Architectures offer Different Tradeoffs berween - extractive body cue:** This suggests that the benefits of more targeted feature utilization outweigh the slight decrease in robustness.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** multi-robot demonstration/dataset ecosystem.
- **Input boundary:** multi-view observation, language/task label과 action trajectory.
- **Output/decision under evaluation:** dataset sample 또는 learned policy action.
- **Primary target:** coverage, cross-embodiment transfer, data efficiency와 task success.
- **Detected evaluation headings:** C. Experiment Setup (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 1: Bimanual, dexterous manipulation requires task-specifie grounding, The left depicts various axes for spatial gr ‘qualitative categorizations of different mid-level representations. Different representations ... | p. 1 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 5: Self-Consistency. On the left image, the robot's achieved trajectory doesn't match it's mid-level representation, which leads to a lower weight. In the ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 8: Real-World Results. There are clear differences in the benefits that different representations provide for tasks in the real world. | p. 8 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 7 / C. Experiment Setup - extractive body cue:** For RT-H, ‘we relabel robot demonstrations with the language "move the arm leftright/up/down." For each environment in simulation and the real-world, we vary the object ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Bimanual, dexterous manipulation requires task-specifie grounding, The left depicts various axes for spatial gr ‘qualitative categorizations of different mid-level representations. Different representations lead ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: Policy Architecture. Four images are passed into a transformer encoder. In addition, an image is fed into each individual mid-level ‘expert. The resulis ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: Self-Consistency. On the left image, the robot's achieved trajectory doesn't match it's mid-level representation, which leads to a lower weight. In the right, ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 8: Real-World Results. There are clear differences in the benefits that different representations provide for tasks in the real world.

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For RT-H, ‘we relabel robot demonstrations with the language "move the arm leftright/up/down." For each environment in simulation and the real-world, we vary the ... | embodiment, simulator version and control stack | p. 7 (C. Experiment Setup) |
| Task/environment | not stated or recoverable in the selected PDF body | reset, timeout, object/scene variation | 본문 anchor 없음 |
| Observation/sensor | multi-view observation, language/task label과 action trajectory | calibration, preprocessing, privileged input | p. 6 (B. Training), p. 4 (V. ARCHITECTURE) |
| Output/decision | dataset sample 또는 learned policy action | action frame, controller and termination | p. 3 (1. Ivrropuction), p. 4 (1. Ivrropuction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| no metric sentence selected | not reported; do not infer from keyword | verify Results/Evaluation |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| In addition, we provide two ablations based on prior ‘works investigating a single representation: a keypoints-based ablation based on MOKA (25] and a language ... | comparison identity and matched condition | p. 7 (C. Experiment Setup) |
| In the Keypoint ablation, we identify important points of interest in the image by querying a VLM. | comparison identity and matched condition | p. 7 (C. Experiment Setup) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| In the Keypoint ablation, we identify important points of interest in the image by querying a VLM. | component/input/data sensitivity | p. 7 (C. Experiment Setup) |
| In addition, we provide two ablations based on prior ‘works investigating a single representation: a keypoints-based ablation based on MOKA (25] and a language ... | component/input/data sensitivity | p. 7 (C. Experiment Setup) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We show that while different mid-level representations excel at different tasks, our method can leverage these task-specitfic benefits to achieve consistently higher performance on ... | Fig. 1: Bimanual, dexterous manipulation requires task-specifie grounding, The left depicts various axes for spatial gr ‘qualitative categorizations of different mid-level representations. Different representations ... | PDF body cue; verify exact table/figure and matched conditions | p. 1 (Figure/Table caption), p. 6 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Primary metric/result | Fig. 5: Self-Consistency. On the left image, the robot's achieved trajectory doesn't match it's mid-level representation, which leads to a lower weight. In the ... | numeric claim only at cited anchor | p. 6 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 6 / B. Training - extractive body cue:** 3 Sample a minibatch of B states/actions {(s,,0,)}2., from D
- **p. 9 / C. Different Architectures offer Different Tradeoffs berween - extractive body cue:** Interestingly, Weighted Mid-Level MoE has an average of 10% higher performance than Mid-Level MoE across the 4 tasks.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | tween responsiveness to structured mid-level representations and robustness to noise or spurious inputs? | p. 6 (4) Which policy architecture offers the best tradeoff be) |
| body limitation/failure cue | Meanwhile, Table I! records the sensitivity scores for each of our mid-level experts as well as the robustness index. ‘The robustness index is computed ... | p. 9 (C. Different Architectures offer Different Tradeoffs berween) |
| body limitation/failure cue | This suggests that the benefits of more targeted feature utilization outweigh the slight decrease in robustness. | p. 9 (C. Different Architectures offer Different Tradeoffs berween) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| During inference time, each of the expert models are executed asynchronously. | p. 5 (B. Training) |
| points, with one annotation every 10 timesteps. | p. 5 (B. Training) |
| 4 Compute mid-level outputs m, - fagen() for each sample | p. 6 (B. Training) |
| The exact ‘method to compute the weights can be viewed in Appendix ?? | p. 6 (B. Training) |
| At each state, we denoise the decoder predicts ¢ = 10 action chunks simultaneously with a transformer. | p. 4 (V. ARCHITECTURE) |
| Each image is fed through a separate ResNetSO encoder, before being processed with a transformer encoder to obtain image embeddings. | p. 4 (V. ARCHITECTURE) |
| Meanwhile, Table I! records the sensitivity scores for each of our mid-level experts as well as the robustness index. ‘The robustness index is computed ... | p. 9 (C. Different Architectures offer Different Tradeoffs berween) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 4) Which policy architecture offers the best tradeoff be - extractive body cue:** tween responsiveness to structured mid-level representations and robustness to noise or spurious inputs?
- **p. 9 / C. Different Architectures offer Different Tradeoffs berween - extractive body cue:** Meanwhile, Table I! records the sensitivity scores for each of our mid-level experts as well as the robustness index. ‘The robustness index is computed by ...
- **p. 9 / C. Different Architectures offer Different Tradeoffs berween - extractive body cue:** This suggests that the benefits of more targeted feature utilization outweigh the slight decrease in robustness.

- **Evidence anchors reviewed:** datasets p. 7 (C. Experiment Setup), metrics 본문 anchor 없음, baselines p. 7 (C. Experiment Setup), p. 7 (C. Experiment Setup), results p. 1 (Figure/Table caption), p. 6 (Figure/Table caption), p. 8 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** In addition, we provide two ablations based on prior ‘works investigating a single representation: a keypoints-based ablation based on MOKA (25] and a language baseline based on RE-H [2]. (p. 7, C. Experiment Setup).
- **Metric evidence:** Fig. 1: Bimanual, dexterous manipulation requires task-specifie grounding, The left depicts various axes for spatial gr ‘qualitative categorizations of different mid-level representations. Different representations lead to different lev ... (p. 1, Figure/Table caption).
- **Baseline/ablation evidence:** In addition, we provide two ablations based on prior ‘works investigating a single representation: a keypoints-based ablation based on MOKA (25] and a language baseline based on RE-H [2]. (p. 7, C. Experiment Setup).
- **Failure/negative evidence:** This sensitivity-robusness tradeoff' underscores the necessity of developing robot policies that balance adherence 10 mid-level representations with the ability to remain adaptable and resilient in the face of environmental variations. ... (p. 4, 1. Ivrropuction).
