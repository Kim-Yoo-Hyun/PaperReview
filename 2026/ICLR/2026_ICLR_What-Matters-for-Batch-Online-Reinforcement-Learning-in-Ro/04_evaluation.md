# Evaluation - What Matters for Batch Online Reinforcement Learning in Robotics?

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://iclr.cc/virtual/2026/poster/10006859; PDF retrieval source: https://arxiv.org/pdf/2505.08078. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (3 Preliminaries), p. 5 (3 Preliminaries), p. 6 (3 Preliminaries), p. 7 (3 Preliminaries)): Figure 3: Normalized returns of different algorithm classes over multiple iterations of improvement. Value-based RL significantly outperforms IL and filtered-IL. Runs are 3 seeds, 100 evaluations. Based on our results, ...

## Evaluation Body Digest

- **p. 5 / 3 Preliminaries - extractive body cue:** Based on our results, in Section 5 we present a recipe for batch online RL, and demonstrate the practicality of the recipe on a challenging ...
- **p. 8 / 3 Preliminaries - extractive body cue:** To validate the practicality of our proposed recipe, we conduct an experiment with running batch online RL on a challenging real-world vision-based robotic manipulation task.
- **p. 7 / 3 Preliminaries - extractive body cue:** Though they are a less expressive class of policies, Gaussian policy are still worth examining because they are fast for inference, which is especially desirable ...
- **p. 7 / 3 Preliminaries - extractive body cue:** Interestingly, we find that although explicit policy extraction achieves a stronger initial performance in nearly every benchmark task, implicit policy extraction performs significantly better after ...
- **p. 8 / 3 Preliminaries - extractive body cue:** The task involves controlling a 7-DoF Franka Research 3 robot to precisely grasp a roll of tape and hang it onto a hook.
- **p. 9 / 6 Discussion - extractive body cue:** First, we focus on robotic tasks with a continuous action space for the study.
- **p. 6 / 3 Preliminaries - extractive body cue:** This approach has the advantage of explicitly learning on signals from the Q-function, while still making the policy stay close to the behavior dataset.
- **p. 9 / 6 Discussion - extractive body cue:** We believe solving these questions will result in significantly better and more capable self-improving robotic models.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** multi-robot demonstration/dataset ecosystem.
- **Input boundary:** multi-view observation, language/task label과 action trajectory.
- **Output/decision under evaluation:** dataset sample 또는 learned policy action.
- **Primary target:** coverage, cross-embodiment transfer, data efficiency와 task success.
- **Detected evaluation headings:** A Additional Experiments (p. 13); B Experiment Hyperparameters (p. 14).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 3: Normalized returns of different algorithm classes over multiple iterations of improvement. Value-based RL significantly outperforms IL and filtered-IL. Runs are 3 seeds, ... | p. 5 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 7: Normalized returns of value-based RL with diffusion versus Gaussian policy before and after improvement. To address confounding of policy extraction methods, we ... | p. 7 (Figure/Table caption) |
| 3 Preliminaries | EMPIRICAL / REAL-ROBOT OR HARDWARE | However, it does not improve data scaling because the correlated noise has the effect of increasing the distribution the policy learns, but this increase ... | p. 8 (3 Preliminaries) |
| 3 Preliminaries | EMPIRICAL / REAL-ROBOT OR HARDWARE | We observe that value-based RL methods tend to significantly outperform IL-based methods. | p. 5 (3 Preliminaries) |
| 3 Preliminaries | EMPIRICAL / REAL-ROBOT OR HARDWARE | In all but one task, value-based RL performs significantly better as the amount data increases, suggesting stronger ability to leverage large batches of data ... | p. 6 (3 Preliminaries) |

## Dataset / Benchmark Role

- **p. 5 / 3 Preliminaries - extractive body cue:** Based on our results, in Section 5 we present a recipe for batch online RL, and demonstrate the practicality of the recipe on a challenging ...
- **p. 8 / 3 Preliminaries - extractive body cue:** To validate the practicality of our proposed recipe, we conduct an experiment with running batch online RL on a challenging real-world vision-based robotic manipulation task.
- **p. 7 / 3 Preliminaries - extractive body cue:** Though they are a less expressive class of policies, Gaussian policy are still worth examining because they are fast for inference, which is especially desirable ...
- **p. 7 / 3 Preliminaries - extractive body cue:** Interestingly, we find that although explicit policy extraction achieves a stronger initial performance in nearly every benchmark task, implicit policy extraction performs significantly better after ...
- **p. 8 / 3 Preliminaries - extractive body cue:** The task involves controlling a 7-DoF Franka Research 3 robot to precisely grasp a roll of tape and hang it onto a hook.
- **p. 9 / 6 Discussion - extractive body cue:** First, we focus on robotic tasks with a continuous action space for the study.
- **p. 6 / 3 Preliminaries - extractive body cue:** This approach has the advantage of explicitly learning on signals from the Q-function, while still making the policy stay close to the behavior dataset.
- **p. 9 / 6 Discussion - extractive body cue:** We believe solving these questions will result in significantly better and more capable self-improving robotic models.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive body cue:** Figure 1: Overview. We consider the batch online RL problem setting, in which a policy is trained on an initial dataset, used to collect batches ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2: Simulation environments. Robomimic tasks: Lift, Can, Square; MimicGen tasks: Threading, Stack; Adroit tasks: Pen.
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Normalized returns of different algorithm classes over multiple iterations of improvement. Value-based RL significantly outperforms IL and filtered-IL. Runs are 3 seeds, 100 ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4: Heatmap of the state visitations of successful trajectories after batch online RL for value-based RL and filtered-IL on Lift and Square. A 3D ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 6: Normalized returns of explicit versus implicit policy extraction. Pre refers to the initial base policy π0 trained on D0 and Post refers to ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5: Normalized re- turns of different algorithm classes at various data scales averaged across all tasks. Value-based RL scales better with larger batches of ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 7: Normalized returns of value-based RL with diffusion versus Gaussian policy before and after improvement. To address confounding of policy extraction methods, we show ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 1. In our experiments, we instantiate the recipe with a diffusion-based policy network trained with IL, a Q-function trained via the IQL objective, and ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Based on our results, in Section 5 we present a recipe for batch online RL, and demonstrate the practicality of the recipe on a ... | embodiment, simulator version and control stack | p. 5 (3 Preliminaries), p. 8 (3 Preliminaries) |
| Task/environment | To validate the practicality of our proposed recipe, we conduct an experiment with running batch online RL on a challenging real-world vision-based robotic manipulation ... | reset, timeout, object/scene variation | p. 8 (3 Preliminaries), p. 7 (3 Preliminaries) |
| Observation/sensor | multi-view observation, language/task label과 action trajectory | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 6 (3 Preliminaries) |
| Output/decision | dataset sample 또는 learned policy action | action frame, controller and termination | p. 8 (3 Preliminaries), p. 3 (3 Preliminaries) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| However, directly adding noise may not be applicable in some deployment settings, though we find empirically that adding a small amount of noise only ... | definition/direction/unit from same section | p. 9 (6 Discussion) |
| Figure 14: Scenes showing sample initial and success state and the initial state distribution of the real-world Tape task. Success Detection. The Tape task ... | definition/direction/unit from same section | p. 15 (Figure/Table caption) |
| Figure 3: Normalized returns of different algorithm classes over multiple iterations of improvement. Value-based RL significantly outperforms IL and filtered-IL. Runs are 3 seeds, ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| We separate policy extraction into two distinct categories, explicit policy extraction and implicit policy extraction, to analyze the effect of extraction method on performance. | definition/direction/unit from same section | p. 6 (3 Preliminaries) |
| On top of that, offline RL methods such as ReBRAC [27] based on Gaussian policies have shown performance on par to diffusion based methods, ... | definition/direction/unit from same section | p. 7 (3 Preliminaries) |
| Figure 7: Normalized returns of value-based RL with diffusion versus Gaussian policy before and after improvement. To address confounding of policy extraction methods, we ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 12: Normalized returns of value-based RL for Robomimic Square and MimicGen Stack. Value-based RL with more rollouts per iteration. We also report runs ... | definition/direction/unit from same section | p. 13 (Figure/Table caption) |
| Figure 1: Overview. We consider the batch online RL problem setting, in which a policy is trained on an initial dataset, used to collect ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 11: Normalized returns of value-based RL compared with IL, filtered-IL, and temporally- correlated noise at different data scales, shown for each task. From ... | comparison identity and matched condition | p. 13 (Figure/Table caption) |
| We observe that value-based RL methods tend to significantly outperform IL-based methods. | comparison identity and matched condition | p. 5 (3 Preliminaries) |
| Filtered-IL, while exhibiting an initial improvement, often converges quickly to suboptimal performance compared to value-based RL. | comparison identity and matched condition | p. 5 (3 Preliminaries) |
| Implicit policy extraction significantly outperforms explicit policy extraction in batch online RL. | comparison identity and matched condition | p. 6 (3 Preliminaries) |
| Given the advantages of value-based RL compared to IL and filtered-IL methods in the batch online RL setting from Section 4.1, the second axis ... | comparison identity and matched condition | p. 6 (3 Preliminaries) |
| We find that across all tasks and environments, the former significantly outperforms the latter. | comparison identity and matched condition | p. 7 (3 Preliminaries) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We separate policy extraction into two distinct categories, explicit policy extraction and implicit policy extraction, to analyze the effect of extraction method on performance. | component/input/data sensitivity | p. 6 (3 Preliminaries) |
| However, it does not improve data scaling because the correlated noise has the effect of increasing the distribution the policy learns, but this increase ... | component/input/data sensitivity | p. 8 (3 Preliminaries) |
| Figure 8: Normalized re- turns of value-based RL with and without temporally corre- lated noise at different data scales, averaged over all tasks. Improving ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Batch online RL provides a paradigm for just that-enabling policies to leverage their own rollouts for self-improvement without the complications of online RL. | component/input/data sensitivity | p. 9 (6 Discussion) |
| For researchers, we bring to attention open questions for future work to optimize each component of the recipe further. | component/input/data sensitivity | p. 9 (6 Discussion) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| On top of the recipe, we propose a simple practical addition to induce even more diversity and achieve better sample efficiency: applying a small ... | Figure 3: Normalized returns of different algorithm classes over multiple iterations of improvement. Value-based RL significantly outperforms IL and filtered-IL. Runs are 3 seeds, ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (3 Preliminaries), p. 5 (3 Preliminaries), p. 6 (3 Preliminaries), p. 7 (3 Preliminaries) |
| Primary metric/result | Figure 7: Normalized returns of value-based RL with diffusion versus Gaussian policy before and after improvement. To address confounding of policy extraction methods, we ... | numeric claim only at cited anchor | p. 7 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 6 / 3 Preliminaries - extractive body cue:** Returns are averaged over 3 seeds and 100 evaluation trials at each iteration. more diverse trajectories after batch online RL.
- **p. 6 / 3 Preliminaries - extractive body cue:** For each environment, we set M to a small, medium, and large value: 50, 100, and 200 trajectories for Robomimic and Mimicgen, and 100, 200, ...
- **p. 8 / 3 Preliminaries - extractive body cue:** The task involves controlling a 7-DoF Franka Research 3 robot to precisely grasp a roll of tape and hang it onto a hook.
- **p. 8 / 3 Preliminaries - extractive body cue:** We collect 5 initial demonstrations in D0 and run N = 3 iterations of batch online RL, each with M = 30 rollouts.
- **p. 8 / 3 Preliminaries - extractive body cue:** We compare our recipe with filtered-IL and a steering baseline adapted from [11], where we train the Q-function on M = 90 rollouts (as well ...
- **p. 4 / 3 Preliminaries - extractive body cue:** We run N=10 to 20 iterations of batch online RL with M=200 rollouts per iteration.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Our work presents a general recipe on batch online RL, though it does have a number of limitations. | p. 9 (6 Discussion) |
| body limitation/failure cue | 7 Limitations In this work, we empirically analyze the key axes that affect performance in batch online RL, demonstrating that the general recipe of ... | p. 9 (6 Discussion) |
| body limitation/failure cue | Vanilla IL performs the worst on all tasks, which is perhaps not surprising as vanilla IL will fit the failure trajectories of the autonomous ... | p. 5 (3 Preliminaries) |
| body limitation/failure cue | Intuitively, this makes sense because value-based RL methods can use the Q-function to determine which states and actions are desirable even in failure trajectories, ... | p. 6 (3 Preliminaries) |
| body limitation/failure cue | One takeaway from this section is that for batch online RL, we cannot get away with just doing IL or filtered-IL as many prior ... | p. 6 (3 Preliminaries) |
| body limitation/failure cue | The policy extracted from explicit policy extraction cannot adjust to this shift as well as implicit policy extraction, resulting in subpar performance. | p. 7 (3 Preliminaries) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Returns are averaged over 3 seeds and 100 evaluation trials at each iteration. more diverse trajectories after batch online RL. | p. 6 (3 Preliminaries) |
| Robotics, in contrast to domains such as computer vision and natural language processing, possesses considerably less data as robotics data do not naturally exist ... | p. 1 (1 Introduction) |
| We run N=10 to 20 iterations of batch online RL with M=200 rollouts per iteration. | p. 4 (3 Preliminaries) |
| Intuitively, τ is a hyperparameter that controls how much the value function approaches the maximum of the Q-function, with greater τ making the value ... | p. 4 (3 Preliminaries) |
| To control for the advantages of the implicit policy extraction method in batch online RL that we observed in Section 4.2, we additionally run ... | p. 7 (3 Preliminaries) |
| We will open source the code for the final recipe. | p. 9 (6 Discussion) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 6 Discussion - extractive body cue:** Our work presents a general recipe on batch online RL, though it does have a number of limitations.
- **p. 9 / 6 Discussion - extractive body cue:** 7 Limitations In this work, we empirically analyze the key axes that affect performance in batch online RL, demonstrating that the general recipe of value-based ...
- **p. 5 / 3 Preliminaries - extractive body cue:** Vanilla IL performs the worst on all tasks, which is perhaps not surprising as vanilla IL will fit the failure trajectories of the autonomous rollouts.
- **p. 6 / 3 Preliminaries - extractive body cue:** Intuitively, this makes sense because value-based RL methods can use the Q-function to determine which states and actions are desirable even in failure trajectories, thus ...
- **p. 6 / 3 Preliminaries - extractive body cue:** One takeaway from this section is that for batch online RL, we cannot get away with just doing IL or filtered-IL as many prior works ...
- **p. 7 / 3 Preliminaries - extractive body cue:** The policy extracted from explicit policy extraction cannot adjust to this shift as well as implicit policy extraction, resulting in subpar performance.

- **Evidence anchors reviewed:** datasets p. 5 (3 Preliminaries), p. 8 (3 Preliminaries), p. 7 (3 Preliminaries), p. 7 (3 Preliminaries), p. 8 (3 Preliminaries), p. 9 (6 Discussion), metrics p. 9 (6 Discussion), p. 15 (Figure/Table caption), p. 5 (Figure/Table caption), p. 6 (3 Preliminaries), p. 7 (3 Preliminaries), p. 7 (Figure/Table caption), baselines p. 13 (Figure/Table caption), p. 5 (3 Preliminaries), p. 5 (3 Preliminaries), p. 6 (3 Preliminaries), p. 6 (3 Preliminaries), p. 7 (3 Preliminaries), results p. 5 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (3 Preliminaries), p. 5 (3 Preliminaries), p. 6 (3 Preliminaries), p. 7 (3 Preliminaries).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
