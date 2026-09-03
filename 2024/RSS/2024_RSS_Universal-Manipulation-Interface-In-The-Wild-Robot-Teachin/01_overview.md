# Universal Manipulation Interface: In-The-Wild Robot Teaching Without In-The-Wild Robots

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss20/p045.html.
> PDF retrieval source: https://arxiv.org/pdf/2402.10329. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, Imitation Learning, human video, cross-embodiment, action representation, bimanual
- Official paper: https://www.roboticsproceedings.org/rss20/p045.html
- Full-text retrieval: https://arxiv.org/pdf/2402.10329
- Code/Project: https://umi-gripper.github.io
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 il 문제를 이해하기 위해 읽는다. 본문은 As a result, despite achieving impressive visual diversity across hundreds of environments, the collected actions are constrained to simple grasping [41] or quasi-static pick-andplace [50, 36], lacking action diversity.를 문제로 두고, 2), we show that UMI is capable of achieving a wide range of manipulation tasks that involve dynamic, bimanual, precise and long-horizon actions by only changing the training data for each task ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We present Universal Manipulation Interface (UMI) - a data collection and policy learning framework that allows direct skill transfer from in-the-wild human demonstrations to deployable ...
- **p. 1 / Abstract - extractive body cue:** UMI employs hand-held grippers coupled with careful interface design to enable portable, lowcost, and information-rich data collection for challenging bimanual and dynamic manipulation demonstrations.
- **p. 1 / Abstract - extractive body cue:** To facilitate deployable policy learning, UMI incorporates a carefully designed policy interface with inference-time latency matching and a relative-trajectory action representation.
- **p. 1 / Abstract - extractive body cue:** The resulting learned policies are hardware-agnostic and deployable across multiple robot platforms.
- **p. 1 / Abstract - extractive body cue:** Equipped with these features, UMI framework unlocks new robot manipulation capabilities, allowing zeroshot generalizable dynamic, bimanual, precise, and long-horizon behaviors, by only changing the training ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** As a result, despite achieving impressive visual diversity across hundreds of environments, the collected actions are constrained to simple grasping [41] or quasi-static pick-andplace [50, ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Recently, using sensorized hand-held grippers as a data collection interface [41, 50, 36] has emerged as a promising middle-ground alternative - simultaneously minimizing the embodiment ...

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** 2), we show that UMI is capable of achieving a wide range of manipulation tasks that involve dynamic, bimanual, precise and long-horizon actions by only ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Furthermore, when trained with diverse human demonstrations, the final policy exhibits zero-shot generalization to novel environments and objects, achieving a remarkable 70% success rate in ...
- **p. 3 / III. METHOD - extractive body cue:** It is designed with the following goals in mind: • Portable.
- **p. 3 / III. METHOD - extractive body cue:** Universal Manipulation Interface (UMI) is hand-held data collection and policy learning framework that allows direct transfer from in-the-wild human demonstrations to deployable robot policies.
- **p. 3 / III. METHOD - extractive body cue:** The following sections describe how we enable the above goals through our hardware and policy interface design.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | When combined with the GoPro's built-in IMU sensor, we can enable robust tracking under fast motion. • Second, we explore the right policy interface (i.e., observation and action representations) that could make ... | observation history와 expert trajectory/action | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| State/latent | When, combined, GoPro, built-in, IMU, sensor, enable, robust, tracking, under, fast, motion | behavior policy와 temporal action context | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Output/action | Concretely, we employ inference-time latency matching to handle different sensor observation and execution latency, use relative trajectory as action representation to remove the need for precise global action, and finally, apply Diffus ... | predicted action 또는 action chunk | p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (III. METHOD) |
| Objective/outcome | imitation error, task success, robustness와 compounding error | imitation error, task success, robustness와 compounding error | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** 2), we show that UMI is capable of achieving a wide range of manipulation tasks that involve dynamic, bimanual, precise and long-horizon actions by only ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Furthermore, when trained with diverse human demonstrations, the final policy exhibits zero-shot generalization to novel environments and objects, achieving a remarkable 70% success rate in ...
- **p. 3 / III. METHOD - extractive body cue:** It is designed with the following goals in mind: • Portable.
- **p. 3 / III. METHOD - extractive body cue:** Universal Manipulation Interface (UMI) is hand-held data collection and policy learning framework that allows direct transfer from in-the-wild human demonstrations to deployable robot policies.
- **p. 7 / V. CAPABILITY EXPERIMENTS - extractive body cue:** This baseline only achieves 11/20 = 55% success rate.
- **p. 7 / V. CAPABILITY EXPERIMENTS - extractive body cue:** This experiment achieves 18/20 = 90% success rate, with the 2 failure cases being joint limit violations, which could have been avoided if we had ...
- **p. 8 / V. CAPABILITY EXPERIMENTS - extractive body cue:** The delta action baseline achieves 16/20 = 80% success rate.
- **p. 8 / V. CAPABILITY EXPERIMENTS - extractive body cue:** Our policy (with inference time latency matching) achieves 105/120 = 87.5% success rate, counted by the number of objects successfully tossed to their corresponding bin.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (V. CAPABILITY EXPERIMENTS), p. 7 (V. CAPABILITY EXPERIMENTS) |
| Embodiment/environment | To access capability and generalization, we evaluate UMI on 4 real-world robotic tasks across both narrow domain and in-the-wild environments, shown in Fig. | hardware/simulator version and reset protocol | p. 6 (IV. EVALUATIONS), p. 6 (V. CAPABILITY EXPERIMENTS) |
| Dataset/benchmark | This task is evaluated in both narrow-domain and unseen environments as well as two robot embodiments. | role, split, size and leakage | p. 6 (IV. EVALUATIONS), p. 6 (V. CAPABILITY EXPERIMENTS), p. 7 (V. CAPABILITY EXPERIMENTS), p. 8 (V. CAPABILITY EXPERIMENTS) |
| Metric | (c) Success rate over 20 evaluation episodes, best performance for each column are bolded. | definition, denominator, direction and uncertainty | p. 8 (V. CAPABILITY EXPERIMENTS), p. 11 (Figure/Table caption), p. 7 (V. CAPABILITY EXPERIMENTS) |
| Baseline/ablation | (b) Typical failure mode of the baseline/ablation policy. | fair input/data/compute/action matching | p. 8 (V. CAPABILITY EXPERIMENTS), p. 7 (V. CAPABILITY EXPERIMENTS), p. 7 (V. CAPABILITY EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 11 / VIII. LIMITATIONS AND FUTURE WORKS - extractive body cue:** While UMI demonstrates policy efficacy across a wide range of tasks and scenarios, a few limitations remain.
- **p. 7 / V. CAPABILITY EXPERIMENTS - extractive body cue:** Beyond the expected failure mode where the cup is outside of camera view, we found this baseline policy to perform surprisingly poor even if the ...
- **p. 7 / V. CAPABILITY EXPERIMENTS - extractive body cue:** This experiment achieves 18/20 = 90% success rate, with the 2 failure cases being joint limit violations, which could have been avoided if we had ...
- **p. 8 / V. CAPABILITY EXPERIMENTS - extractive body cue:** (b) Typical failure mode of the baseline/ablation policy.
- **p. 8 / V. CAPABILITY EXPERIMENTS - extractive body cue:** The red arrow indicates failure behavior, green arrow indicates desired behavior.
- **p. 9 / V. CAPABILITY EXPERIMENTS - extractive body cue:** The most salient failure case is when the two arms lift the bottom hem of the shirt, where the baseline policy often misses one of ...
- **p. 9 / V. CAPABILITY EXPERIMENTS - extractive body cue:** Cafe Table Water Fountain Success Rate CLIP ViT finetune with narrow-domain Data 0 / 10 0 / 10 0.0 In-the-wild Data Training Cup 16 / ...

## Why Read It

RL, IL, offline learning, and robot data의 il 문제를 이해하기 위해 읽는다. 본문은 As a result, despite achieving impressive visual diversity across hundreds of environments, the collected actions are constrained to simple grasping [41] or quasi-static pick-andplace [50, 36], lacking action diversity.를 문제로 두고, 2), we show that UMI is capable of achieving a wide range of manipulation tasks that involve dynamic, bimanual, precise and long-horizon actions by only changing the training data for each task ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHOD), p. 3 (III. METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** As a result, despite achieving impressive visual diversity across hundreds of environments, the collected actions are constrained to simple grasping [41] or quasi-static pick-andplace [50, 36], lacking action diversity. (p. 1, I. INTRODUCTION).
- **Actual contribution:** 2), we show that UMI is capable of achieving a wide range of manipulation tasks that involve dynamic, bimanual, precise and long-horizon actions by only changing the training data for ... (p. 2, I. INTRODUCTION).
- **Evaluation boundary:** Fig. 8: Narrow-domain Evaluation Results. (a) Initial states for all evaluation episodes overlayed together. For each task, all methods start with the same set of initial states, matched manually with ... (p. 8, Figure/Table caption).
- **Explicit failure boundary:** This experiment achieves 18/20 = 90% success rate, with the 2 failure cases being joint limit violations, which could have been avoided if we had mounted the FR2 robot at ... (p. 7, V. CAPABILITY EXPERIMENTS).
