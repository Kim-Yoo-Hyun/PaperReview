# Evaluation - MT-Opt: Continuous Multi-Task Robotic Reinforcement Learning at Scale

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2104.08212; PDF retrieval source: https://arxiv.org/abs/2104.08212. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (VII. EXPERIMENTS), p. 7 (VII. EXPERIMENTS), p. 8 (VII. EXPERIMENTS), p. 8 (VII. EXPERIMENTS), p. 6 (VII. EXPERIMENTS), p. 6 (VII. EXPERIMENTS)): Looking at the average performance across all task, we observe that MT-Opt significantly outperforms the baselines, in some cases with ≈3× average improvement.

## Evaluation Body Digest

- **p. 6 / VII. EXPERIMENTS - extractive body cue:** The goal of our real-world experiments is to answer the following questions: (1) How does MT-Opt perform, quantitatively and qualitatively, on a large set of ...
- **p. 6 / VII. EXPERIMENTS - extractive body cue:** Experimental Setup MT-Opt provides a general robotic skill learning framework that we use to learn multiple tasks, including semantic picking (i.e., picking an object from ...
- **p. 7 / VII. EXPERIMENTS - extractive body cue:** The two policies are trained from the same offline dataset. lift-bottle, which have more data, especially on-policy data, have higher success rates than underrepresented tasks, ...
- **p. 7 / VII. EXPERIMENTS - extractive body cue:** We use the same fIskill task impersonation strategy, and the exact same offline dataset (i.e. both policies use the data from the extra 10 narrower ...
- **p. 8 / VII. EXPERIMENTS - extractive body cue:** 5) consists of 5400 episodes collected for that task (i.e.
- **p. 8 / VII. EXPERIMENTS - extractive body cue:** The single-task policy learned from the 16600 episodes yields performance of 3%.
- **p. 7 / VII. EXPERIMENTS - extractive body cue:** 7 shows the success rates of MT-Opt on the 12 evaluation tasks.
- **p. 17 / Figure/Table caption - extractive body cue:** Fig. 17: Effective success rate for each task in our offline dataset. This plot represents the distribution of successes within the entirety of our offline ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** multi-robot demonstration/dataset ecosystem.
- **Input boundary:** multi-view observation, language/task label과 action trajectory.
- **Output/decision under evaluation:** dataset sample 또는 learned policy action.
- **Primary target:** coverage, cross-embodiment transfer, data efficiency와 task success.
- **Detected evaluation headings:** VII. EXPERIMENTS (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| VII. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Looking at the average performance across all task, we observe that MT-Opt significantly outperforms the baselines, in some cases with ≈3× average improvement. | p. 7 (VII. EXPERIMENTS) |
| VII. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | The 12-task policy outperforms the 2task policy even on the two tasks that the 2-task policy is trained on, suggesting that training multiple tasks ... | p. 7 (VII. EXPERIMENTS) |
| VII. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | MT-Opt, which uses impersonated successes and failures, achieves 39% success for the same task, a ≈10× improvement. | p. 8 (VII. EXPERIMENTS) |
| VII. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Data Re-Balancing Strategy Function uniform sampling task re-balanced sampling fIorig 0.10 / 0.32 / 0.94 / 0.18 0.16 / 0.55 / 0.85 / 0.42 ... | p. 8 (VII. EXPERIMENTS) |
| VII. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | (3) Does data sharing improve performance of the system? | p. 6 (VII. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 6 / VII. EXPERIMENTS - extractive body cue:** The goal of our real-world experiments is to answer the following questions: (1) How does MT-Opt perform, quantitatively and qualitatively, on a large set of ...
- **p. 6 / VII. EXPERIMENTS - extractive body cue:** Experimental Setup MT-Opt provides a general robotic skill learning framework that we use to learn multiple tasks, including semantic picking (i.e., picking an object from ...
- **p. 7 / VII. EXPERIMENTS - extractive body cue:** The two policies are trained from the same offline dataset. lift-bottle, which have more data, especially on-policy data, have higher success rates than underrepresented tasks, ...
- **p. 7 / VII. EXPERIMENTS - extractive body cue:** We use the same fIskill task impersonation strategy, and the exact same offline dataset (i.e. both policies use the data from the extra 10 narrower ...
- **p. 8 / VII. EXPERIMENTS - extractive body cue:** 5) consists of 5400 episodes collected for that task (i.e.
- **p. 8 / VII. EXPERIMENTS - extractive body cue:** The single-task policy learned from the 16600 episodes yields performance of 3%.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: A) Multi-task data collection. B) Training objects. C) Sample of tasks that the system is trained on. D) Sample of behaviorally and visually ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: MT-Opt overview. A) The user defines a success detector for tasks through examples of desired outcomes, and relabeling outcomes of prior episodes. B) ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: Path of episodes through task impersonation, where episodes are routed to train relevant tasks, and data re- balancing where the ratio of success ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: Video frames for the place-anywhere task. Success and failure videos are iteratively captured in pairs to mitigate correlations with spurious workspace features such ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 5: Offline dataset properties. We use our data collection strategy to simultaneously collect data for multiple tasks, where we use easier and more general ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 6: Top: 12 tasks trained for ablations, giving rise to Object Acquisition and Object Manipulation skills. Bottom: examples of additional tasks that a skilled ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 7: Quantitative evaluation of MT-Opt across 12 tasks. QT- Opt trains each task individually using only data collected for that task. QT-Opt Multi-Task trains ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 8: Top row: Example of pick-carrot. The robot repositions the carrot out of the corner to pick it. Bottom row: cover- object. The deformable ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The goal of our real-world experiments is to answer the following questions: (1) How does MT-Opt perform, quantitatively and qualitatively, on a large set ... | embodiment, simulator version and control stack | p. 6 (VII. EXPERIMENTS), p. 6 (VII. EXPERIMENTS) |
| Task/environment | Experimental Setup MT-Opt provides a general robotic skill learning framework that we use to learn multiple tasks, including semantic picking (i.e., picking an object ... | reset, timeout, object/scene variation | p. 6 (VII. EXPERIMENTS), p. 7 (VII. EXPERIMENTS) |
| Observation/sensor | multi-view observation, language/task label과 action trajectory | calibration, preprocessing, privileged input | p. 3 (III. SYSTEM OVERVIEW), p. 3 (III. SYSTEM OVERVIEW) |
| Output/decision | dataset sample 또는 learned policy action | action frame, controller and termination | p. 5 (V. REWARDS VIA MULTI-TASK SUCCESS DETECTORS), p. 4 (III. SYSTEM OVERVIEW) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 7 shows the success rates of MT-Opt on the 12 evaluation tasks. | definition/direction/unit from same section | p. 7 (VII. EXPERIMENTS) |
| The two policies are trained from the same offline dataset. lift-bottle, which have more data, especially on-policy data, have higher success rates than underrepresented ... | definition/direction/unit from same section | p. 7 (VII. EXPERIMENTS) |
| Fig. 17: Effective success rate for each task in our offline dataset. This plot represents the distribution of successes within the entirety of our ... | definition/direction/unit from same section | p. 17 (Figure/Table caption) |
| Fig. 5: Offline dataset properties. We use our data collection strategy to simultaneously collect data for multiple tasks, where we use easier and more ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Fig. 10: Comparison of single-headed and multi-headed neural networks approximating the Q-function. In both cased task ID was fed as the input to the ... | definition/direction/unit from same section | p. 13 (Figure/Table caption) |
| Fig. 11: System overview: Task episodes from disk are continuously loaded by LogReplay job into task replay buffers. LogReplay process assigns binary reward signal ... | definition/direction/unit from same section | p. 14 (Figure/Table caption) |
| The deformable cloth is laid over the object. demonstrates the value of both successful and unsuccessful data collected by other tasks for learning new ... | definition/direction/unit from same section | p. 8 (VII. EXPERIMENTS) |
| Without any additional data-sharing and re-balancing, this data imbalance causes the baseline strategy fIorig to attain good performance for the easier, overrepresented tasks, but ... | definition/direction/unit from same section | p. 8 (VII. EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Looking at the average performance across all task, we observe that MT-Opt significantly outperforms the baselines, in some cases with ≈3× average improvement. | comparison identity and matched condition | p. 7 (VII. EXPERIMENTS) |
| Tasks such as lift-carrot and Parameter Sharing Ablation (Success Rate) Model: 2-Task Model 12-Task Model lift-any 0.82 0.89 place-any 0.63 0.85 TABLE I: The ... | comparison identity and matched condition | p. 7 (VII. EXPERIMENTS) |
| Without any additional data-sharing and re-balancing, this data imbalance causes the baseline strategy fIorig to attain good performance for the easier, overrepresented tasks, but ... | comparison identity and matched condition | p. 8 (VII. EXPERIMENTS) |
| MT-Opt (ours) provides a significant improvement over the baselines, especially for the harder tasks with less data. | comparison identity and matched condition | p. 8 (VII. EXPERIMENTS) |
| Fig. 1: A) Multi-task data collection. B) Training objects. C) Sample of tasks that the system is trained on. D) Sample of behaviorally and ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| Fig. 6: Top: 12 tasks trained for ablations, giving rise to Object Acquisition and Object Manipulation skills. Bottom: examples of additional tasks that a ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Tasks such as lift-carrot and Parameter Sharing Ablation (Success Rate) Model: 2-Task Model 12-Task Model lift-any 0.82 0.89 place-any 0.63 0.85 TABLE I: The ... | component/input/data sensitivity | p. 7 (VII. EXPERIMENTS) |
| Fig. 12: Practical effect of task impersonation for successful outcomes. Dark blue indicates data specifically collected for a task; light blue indicates episodes impersonated ... | component/input/data sensitivity | p. 14 (Figure/Table caption) |
| We use the same fIskill task impersonation strategy, and the exact same offline dataset (i.e. both policies use the data from the extra 10 ... | component/input/data sensitivity | p. 7 (VII. EXPERIMENTS) |
| Data Strategies Ablation (min, mean, max, mean of low data tasks) Imperson. | component/input/data sensitivity | p. 8 (VII. EXPERIMENTS) |
| Data-Sharing Multi-Task also trains a single network for all tasks and shares the data across all tasks without further re-balancing. | component/input/data sensitivity | p. 8 (VII. EXPERIMENTS) |
| Fig. 6: Top: 12 tasks trained for ablations, giving rise to Object Acquisition and Object Manipulation skills. Bottom: examples of additional tasks that a ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We further make the following contributions: • We address the challenge of providing rewards by creating a scalable and intuitive success-classifier-based approach that allows ... | Looking at the average performance across all task, we observe that MT-Opt significantly outperforms the baselines, in some cases with ≈3× average improvement. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (VII. EXPERIMENTS), p. 7 (VII. EXPERIMENTS), p. 8 (VII. EXPERIMENTS), p. 8 (VII. EXPERIMENTS), p. 6 (VII. EXPERIMENTS), p. 6 (VII. EXPERIMENTS) |
| Primary metric/result | The 12-task policy outperforms the 2task policy even on the two tasks that the 2-task policy is trained on, suggesting that training multiple tasks ... | numeric claim only at cited anchor | p. 7 (VII. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 6 / VII. EXPERIMENTS - extractive body cue:** In the following experiments, we use a set of 12 tasks for quantitative evaluation of our algorithm.
- **p. 6 / VII. EXPERIMENTS - extractive body cue:** These 12 tasks include a set of plastic food objects and divided plate fixtures and they can be split into ‘object acquisition' and ‘object manipulation' ...
- **p. 6 / VII. EXPERIMENTS - extractive body cue:** The resulting policy is deployed on 7 robots attempting each task 100 times for evaluation.
- **p. 7 / VII. EXPERIMENTS - extractive body cue:** The 12-task policy outperforms the 2task policy even on the two tasks that the 2-task policy is trained on, suggesting that training multiple tasks not ...
- **p. 8 / VII. EXPERIMENTS - extractive body cue:** Data Re-Balancing Strategy Function uniform sampling task re-balanced sampling fIorig 0.10 / 0.32 / 0.94 / 0.18 0.16 / 0.55 / 0.85 / 0.42 fIall ...
- **p. 8 / VII. EXPERIMENTS - extractive body cue:** The effect is especially pronounced for the underrepresented tasks. across all the evaluation tasks, with improvements of up to 10x for some tasks.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | These include the exact same set of successful lift-sausage episodes as MT-Opt, but does not include the failures from other tasks. | p. 8 (VII. EXPERIMENTS) |
| body limitation/failure cue | Fig. 4: Video frames for the place-anywhere task. Success and failure videos are iteratively captured in pairs to mitigate correlations with spurious workspace features ... | p. 5 (Figure/Table caption) |
| body limitation/failure cue | Fig. 3: Path of episodes through task impersonation, where episodes are routed to train relevant tasks, and data re- balancing where the ratio of ... | p. 5 (Figure/Table caption) |
| body limitation/failure cue | MT-Opt, which uses impersonated successes and failures, achieves 39% success for the same task, a ≈10× improvement. | p. 8 (VII. EXPERIMENTS) |
| body limitation/failure cue | Fig. 11: System overview: Task episodes from disk are continuously loaded by LogReplay job into task replay buffers. LogReplay process assigns binary reward signal ... | p. 14 (Figure/Table caption) |
| body limitation/failure cue | Fig. 14: Counts of labelled SD training data by task and outcome. This data was generated either from human video demonstration, or by labelling ... | p. 16 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Note, that we are not able run this baseline for the placing tasks, since they require a separate task to lift the object, which ... | p. 7 (VII. EXPERIMENTS) |
| In addition to fIskill task impersonation, we re-balance each training batch between the tasks as well as within each task to keep the relative ... | p. 7 (VII. EXPERIMENTS) |
| While existing methods are effective and able to generalize, they require considerable on-robot training time, as well as extensive engineering effort for setting up ... | p. 1 (I. INTRODUCTION) |
| For example, the QT-Opt [36] system can learn vision-based robotic grasping, but it requires over 500, 000 trials collected across multiple robots. | p. 1 (I. INTRODUCTION) |
| Similarly to [36], we use the cross-entropy method (CEM) to perform the stochastic optimization to compute the target value function. | p. 4 (III. SYSTEM OVERVIEW) |
| where QT (s, a, s′) = r(s, a) + γV (s′) is a target Q-value and D is a divergence metric, such as cross-entropy, ... | p. 4 (III. SYSTEM OVERVIEW) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / VII. EXPERIMENTS - extractive body cue:** These include the exact same set of successful lift-sausage episodes as MT-Opt, but does not include the failures from other tasks.
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: Video frames for the place-anywhere task. Success and failure videos are iteratively captured in pairs to mitigate correlations with spurious workspace features such ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: Path of episodes through task impersonation, where episodes are routed to train relevant tasks, and data re- balancing where the ratio of success ...
- **p. 8 / VII. EXPERIMENTS - extractive body cue:** MT-Opt, which uses impersonated successes and failures, achieves 39% success for the same task, a ≈10× improvement.
- **p. 14 / Figure/Table caption - extractive body cue:** Fig. 11: System overview: Task episodes from disk are continuously loaded by LogReplay job into task replay buffers. LogReplay process assigns binary reward signal to ...
- **p. 16 / Figure/Table caption - extractive body cue:** Fig. 14: Counts of labelled SD training data by task and outcome. This data was generated either from human video demonstration, or by labelling terminal ...

- **Evidence anchors reviewed:** datasets p. 6 (VII. EXPERIMENTS), p. 6 (VII. EXPERIMENTS), p. 7 (VII. EXPERIMENTS), p. 7 (VII. EXPERIMENTS), p. 8 (VII. EXPERIMENTS), p. 8 (VII. EXPERIMENTS), metrics p. 7 (VII. EXPERIMENTS), p. 7 (VII. EXPERIMENTS), p. 17 (Figure/Table caption), p. 5 (Figure/Table caption), p. 13 (Figure/Table caption), p. 14 (Figure/Table caption), baselines p. 7 (VII. EXPERIMENTS), p. 7 (VII. EXPERIMENTS), p. 8 (VII. EXPERIMENTS), p. 8 (VII. EXPERIMENTS), p. 1 (Figure/Table caption), p. 6 (Figure/Table caption), results p. 7 (VII. EXPERIMENTS), p. 7 (VII. EXPERIMENTS), p. 8 (VII. EXPERIMENTS), p. 8 (VII. EXPERIMENTS), p. 6 (VII. EXPERIMENTS), p. 6 (VII. EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Looking at the average performance across all task, we observe that MT-Opt significantly outperforms the baselines, in some cases with ≈3× average improvement. (p. 7, VII. EXPERIMENTS).
- **Metric evidence:** (3) Does data sharing improve performance of the system? (p. 6, VII. EXPERIMENTS).
- **Baseline/ablation evidence:** Looking at the average performance across all task, we observe that MT-Opt significantly outperforms the baselines, in some cases with ≈3× average improvement. (p. 7, VII. EXPERIMENTS).
- **Failure/negative evidence:** These include the exact same set of successful lift-sausage episodes as MT-Opt, but does not include the failures from other tasks. (p. 8, VII. EXPERIMENTS).
