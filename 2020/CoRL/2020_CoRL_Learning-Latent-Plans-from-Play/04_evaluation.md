# Evaluation - Learning Latent Plans from Play

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v100/lynch20a.html; PDF retrieval source: https://arxiv.org/pdf/1903.01973. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 15 (Figure/Table caption), p. 16 (Figure/Table caption)): 3) Does decoupling latent plan inference and plan decoding into independent problems, as is done in Play-LMP, improve performance over goal-conditioned Behavioral Cloning (Play-GCBC), (which does no explicit latent plan ...

## Evaluation Body Digest

- **p. 7 / 4 Experiments - extractive body cue:** To compare our play-supervised models to a conventional scenario, we collect a training set of 100 expert demonstrations per task in the environment, and train ...
- **p. 7 / 4 Experiments - extractive body cue:** We define two sets of experiments over these datasets: pixel experiments, where we study the multitask visual manipulation problem, and state experiments, where we ignore ...
- **p. 8 / 4 Experiments - extractive body cue:** 4 we embed 512 randomly selected windows from the play dataset as well as all validation task demonstrations, using the Φ plan recognition model.
- **p. 17 / A.4.3 Coverage Analysis of Interaction Space - extractive body cue:** Our state models were trained on a smaller dataset, up to 180 minutes of play (see Fig 8). "Random": we collected a random exploration dataset ...
- **p. 8 / 4 Experiments - extractive body cue:** 8 that even when trained on only 30 minutes of play data, individual Play-LMP policies outperform 18 BC policies trained on 90 minutes of expert ...
- **p. 17 / A.4.3 Coverage Analysis of Interaction Space - extractive body cue:** Play data, Fig 2d: This is our largest 7h play dataset, used to train our pixel experiment models.
- **p. 16 / A.4.3 Coverage Analysis of Interaction Space - extractive body cue:** To compute regions of interaction space, we quantized the 11 dimensions of action space corresponding to object interactions: the 3 position and 3 euler angle ...
- **p. 7 / 4 Experiments - extractive body cue:** 0.00 0.05 0.10 0.15 0.20 0.25 0.30 0.35 0.40 Perturbation amount (meters) 0 20 40 60 80 100 18 tasks average accuracy % Play-LMP (ours) ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** demonstration으로 정의된 robot task distribution.
- **Input boundary:** observation history와 expert trajectory/action.
- **Output/decision under evaluation:** predicted action 또는 action chunk.
- **Primary target:** imitation error, task success, robustness와 compounding error.
- **Detected evaluation headings:** 4 Experiments (p. 7); A.3 Experimental Details (p. 13); A.4 Results Details (p. 15).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | 3) Does decoupling latent plan inference and plan decoding into independent problems, as is done in Play-LMP, improve performance over goal-conditioned Behavioral Cloning (Play-GCBC), ... | p. 7 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | 10 5 0 5 10 15 20 25 Improvement of Play-LMP over Play-GCBC (absolute accuracy % points) rotate left close sliding grasp upright sweep ... | p. 7 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Additionally, we find that the decoupling happening in Play-LMP compared to Play-GCBC is beneficial and yields systematic improvements in performance. | p. 8 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | A single task-agnostic PlayLMP policy, trained on unlabeled play data generalizes with 85.5% success to the 18 test-time tasks with no finetuning, outperforming a ... | p. 8 (4 Experiments) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 12: Success per task while perturbing starting position. See Fig. 6b for the success averaged over all tasks. Perturbations vary (shown along the ... | p. 15 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 7 / 4 Experiments - extractive body cue:** To compare our play-supervised models to a conventional scenario, we collect a training set of 100 expert demonstrations per task in the environment, and train ...
- **p. 7 / 4 Experiments - extractive body cue:** We define two sets of experiments over these datasets: pixel experiments, where we study the multitask visual manipulation problem, and state experiments, where we ignore ...
- **p. 8 / 4 Experiments - extractive body cue:** 4 we embed 512 randomly selected windows from the play dataset as well as all validation task demonstrations, using the Φ plan recognition model.
- **p. 17 / A.4.3 Coverage Analysis of Interaction Space - extractive body cue:** Our state models were trained on a smaller dataset, up to 180 minutes of play (see Fig 8). "Random": we collected a random exploration dataset ...
- **p. 8 / 4 Experiments - extractive body cue:** 8 that even when trained on only 30 minutes of play data, individual Play-LMP policies outperform 18 BC policies trained on 90 minutes of expert ...
- **p. 17 / A.4.3 Coverage Analysis of Interaction Space - extractive body cue:** Play data, Fig 2d: This is our largest 7h play dataset, used to train our pixel experiment models.
- **p. 16 / A.4.3 Coverage Analysis of Interaction Space - extractive body cue:** To compute regions of interaction space, we quantized the 11 dimensions of action space corresponding to object interactions: the 3 position and 3 euler angle ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Play-LMP: A single model that self-supervises control from play data, then generalizes to a wide variety of manipulation tasks. (a) Training: 1) sample ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: The continuum of skills and its coverage. We advocate for learning the full continuum of skills at once rather than discrete ones. (a) ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: The Playground environment. Details in A.3.1 button pushing sequences all other play sequences grasping sequences drawer
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 5: Example of a supervised demonstration sequence labeled and segmented for the "sliding" task. 3 Learning Task-Agnostic Control from Play Data First we give ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 6: Quantitative task success and robustness. (a) Play-LMP consistently outperforms the baselines, whether trained on groundtruth states or directly on pixels. Success is reported ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 7: Improvement per task of Play-LMP over Play-GCBC (left) and BC baselines (right), in absolute percentage points of accuracy (model trained on states). Task ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 8: 18-tasks average success for self-supervised models trained on various amounts of cheap play data (left) vs. expert-trained models trained on expensive task demonstrations ...
- **p. 13 / Figure/Table caption - extractive body cue:** Figure 9: Detailed architecture of Play-LMP. A.3 Experimental Details A.3.1 Playground Environment We created a simulated "playground environment" with enough diversity that it can be ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | To compare our play-supervised models to a conventional scenario, we collect a training set of 100 expert demonstrations per task in the environment, and ... | embodiment, simulator version and control stack | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Task/environment | We define two sets of experiments over these datasets: pixel experiments, where we study the multitask visual manipulation problem, and state experiments, where we ... | reset, timeout, object/scene variation | p. 7 (4 Experiments), p. 8 (4 Experiments) |
| Observation/sensor | observation history와 expert trajectory/action | calibration, preprocessing, privileged input | p. 12 (A.1 Theoretical Motivation), p. 2 (1 Introduction) |
| Output/decision | predicted action 또는 action chunk | action frame, controller and termination | p. 12 (A.2 Architecture Details), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 0.00 0.05 0.10 0.15 0.20 0.25 0.30 0.35 0.40 Perturbation amount (meters) 0 20 40 60 80 100 18 tasks average accuracy % Play-LMP ... | definition/direction/unit from same section | p. 7 (4 Experiments) |
| 0 15 30 60 180 Minutes of unlabeled play data 0 20 40 60 80 100 18 tasks average accuracy % Self-Supervision from cheap ... | definition/direction/unit from same section | p. 8 (4 Experiments) |
| 10 5 0 5 10 15 20 25 Improvement of Play-LMP over Play-GCBC (absolute accuracy % points) rotate left close sliding grasp upright sweep ... | definition/direction/unit from same section | p. 7 (4 Experiments) |
| Shaded regions indicate 95% confidence intervals over 20 rollouts. | definition/direction/unit from same section | p. 8 (4 Experiments) |
| Figure 12: Success per task while perturbing starting position. See Fig. 6b for the success averaged over all tasks. Perturbations vary (shown along the ... | definition/direction/unit from same section | p. 15 (Figure/Table caption) |
| Figure 13: Naturally emerging retrying behavior: example run of Play-LMP policy on "grasp upright" task (grasping an object in upright position). The agent fails ... | definition/direction/unit from same section | p. 16 (Figure/Table caption) |
| Figure 14: Naturally emerging retrying behavior: example run of Play-LMP policy on "close sliding" task (sliding door left to right). The policy is aiming ... | definition/direction/unit from same section | p. 16 (Figure/Table caption) |
| Plots were generated by iterating the respective datasets and keeping track of summed time (x-axis) and cardinality of the set of visited quantized interaction ... | definition/direction/unit from same section | p. 17 (A.4.3 Coverage Analysis of Interaction Space) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| (a) Play-LMP consistently outperforms the baselines, whether trained on groundtruth states or directly on pixels. | comparison identity and matched condition | p. 7 (4 Experiments) |
| We believe this comparison is fair for two reasons: 1) the baseline gets 3x more training data, 2) the baseline training data consists of ... | comparison identity and matched condition | p. 8 (4 Experiments) |
| We additionally train a single multi-task behavioral cloning baseline conditioned on state and task id, Multitask BC (Rahmatizadeh et al. | comparison identity and matched condition | p. 7 (4 Experiments) |
| 7 the absolute improvement per task in percentage points of Play-LMP over the baselines, with up to 50 points of improvement. | comparison identity and matched condition | p. 8 (4 Experiments) |
| The different collection methods plotted are: Expert demonstrations, Fig 2c and 2d: This corresponds exactly to the BC baselines 18-task expert demonstration training data ... | comparison identity and matched condition | p. 17 (A.4.3 Coverage Analysis of Interaction Space) |
| Figure 14: Naturally emerging retrying behavior: example run of Play-LMP policy on "close sliding" task (sliding door left to right). The policy is aiming ... | comparison identity and matched condition | p. 16 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| These data ablation numbers were obtained from models trained on ground truth state observations. | component/input/data sensitivity | p. 8 (4 Experiments) |
| Figure 14: Naturally emerging retrying behavior: example run of Play-LMP policy on "close sliding" task (sliding door left to right). The policy is aiming ... | component/input/data sensitivity | p. 16 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this work, we propose an alternative means of obtaining task-agnostic control-self-supervising on top of unlabeled teleoperated play data: continuous logs of low-level observations ... | 3) Does decoupling latent plan inference and plan decoding into independent problems, as is done in Play-LMP, improve performance over goal-conditioned Behavioral Cloning (Play-GCBC), ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 15 (Figure/Table caption), p. 16 (Figure/Table caption) |
| Primary metric/result | 10 5 0 5 10 15 20 25 Improvement of Play-LMP over Play-GCBC (absolute accuracy % points) rotate left close sliding grasp upright sweep ... | numeric claim only at cited anchor | p. 7 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 7 / 4 Experiments - extractive body cue:** This results in 1800 demonstrations total or ∼1.5 hours of expert data.
- **p. 7 / 4 Experiments - extractive body cue:** We collect play datasets (example in A.3.2) of various sizes as training data for Play-LMP and Play-GCBC, up to ∼7 hours total.
- **p. 7 / 4 Experiments - extractive body cue:** 0.00 0.05 0.10 0.15 0.20 0.25 0.30 0.35 0.40 Perturbation amount (meters) 0 20 40 60 80 100 18 tasks average accuracy % Play-LMP (ours) ...
- **p. 8 / 4 Experiments - extractive body cue:** 7 the absolute improvement per task in percentage points of Play-LMP over the baselines, with up to 50 points of improvement.
- **p. 8 / 4 Experiments - extractive body cue:** 0 15 30 60 180 Minutes of unlabeled play data 0 20 40 60 80 100 18 tasks average accuracy % Self-Supervision from cheap play ...
- **p. 8 / 4 Experiments - extractive body cue:** Shaded regions indicate 95% confidence intervals over 20 rollouts.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 13: Naturally emerging retrying behavior: example run of Play-LMP policy on "grasp upright" task (grasping an object in upright position). The agent fails ... | p. 16 (Figure/Table caption) |
| body limitation/failure cue | The question of out-of-distribution generalization-say, playing in the living room and generalizing to the kitchen-is left to future work. | p. 17 (A.5 Limitations) |
| body limitation/failure cue | Emergent Retrying: We find qualitative evidence that play-supervised models, unlike models trained solely on expert demonstrations, make multiple attempts to retry the task after ... | p. 8 (4 Experiments) |
| body limitation/failure cue | Future work includes exploring whether generalization is possible to novel objects or novel environments, as well as exploring the effects of imbalance in play ... | p. 8 (5 Conclusion) |
| body limitation/failure cue | We hope to explore this in future work. | p. 17 (A.5 Limitations) |
| body limitation/failure cue | Figure 14: Naturally emerging retrying behavior: example run of Play-LMP policy on "close sliding" task (sliding door left to right). The policy is aiming ... | p. 16 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Success is reported with confidence intervals over 3 seeded training runs for pixel experiments. | p. 7 (4 Experiments) |
| To compute regions of interaction space, we quantized the 11 dimensions of action space corresponding to object interactions: the 3 position and 3 euler ... | p. 16 (A.4.3 Coverage Analysis of Interaction Space) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 16 / Figure/Table caption - extractive body cue:** Figure 13: Naturally emerging retrying behavior: example run of Play-LMP policy on "grasp upright" task (grasping an object in upright position). The agent fails initially, ...
- **p. 17 / A.5 Limitations - extractive body cue:** The question of out-of-distribution generalization-say, playing in the living room and generalizing to the kitchen-is left to future work.
- **p. 8 / 4 Experiments - extractive body cue:** Emergent Retrying: We find qualitative evidence that play-supervised models, unlike models trained solely on expert demonstrations, make multiple attempts to retry the task after initial ...
- **p. 8 / 5 Conclusion - extractive body cue:** Future work includes exploring whether generalization is possible to novel objects or novel environments, as well as exploring the effects of imbalance in play data ...
- **p. 17 / A.5 Limitations - extractive body cue:** We hope to explore this in future work.
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 14: Naturally emerging retrying behavior: example run of Play-LMP policy on "close sliding" task (sliding door left to right). The policy is aiming the ...

- **Evidence anchors reviewed:** datasets p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 17 (A.4.3 Coverage Analysis of Interaction Space), p. 8 (4 Experiments), p. 17 (A.4.3 Coverage Analysis of Interaction Space), metrics p. 7 (4 Experiments), p. 8 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 15 (Figure/Table caption), p. 16 (Figure/Table caption), baselines p. 7 (4 Experiments), p. 8 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 17 (A.4.3 Coverage Analysis of Interaction Space), p. 16 (Figure/Table caption), results p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 15 (Figure/Table caption), p. 16 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** 10 5 0 5 10 15 20 25 Improvement of Play-LMP over Play-GCBC (absolute accuracy % points) rotate left close sliding grasp upright sweep right grasp flat pull out shelf ... (p. 7, 4 Experiments).
- **Metric evidence:** 0.00 0.05 0.10 0.15 0.20 0.25 0.30 0.35 0.40 Perturbation amount (meters) 0 20 40 60 80 100 18 tasks average accuracy % Play-LMP (ours) Play-GCBC (ours) BC (b) Robustness ... (p. 7, 4 Experiments).
- **Baseline/ablation evidence:** (a) Play-LMP consistently outperforms the baselines, whether trained on groundtruth states or directly on pixels. (p. 7, 4 Experiments).
- **Failure/negative evidence:** The question of out-of-distribution generalization-say, playing in the living room and generalizing to the kitchen-is left to future work. (p. 17, A.5 Limitations).
