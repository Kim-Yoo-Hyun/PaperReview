# Evaluation - Relay Policy Learning: Solving Long-Horizon Tasks via Imitation and Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v100/gupta20a.html; PDF retrieval source: https://arxiv.org/pdf/1910.11956. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 8 (3 Preliminaries), p. 7 (3 Preliminaries), p. 6 (3 Preliminaries), p. 4 (3 Preliminaries)): Table 1: Comparison of RIL to goal-conditioned behavior cloning with and without relabeling in terms success and step-completion rate averaged across 17 tasks. RIL outperforms the non-hierarchical methods 5.2 Relay ...

## Evaluation Body Digest

- **p. 6 / 3 Preliminaries - extractive body cue:** The environment consists of a 9 DoF positioncontrolled Franka robot interacting with a kitchen scene that includes an openable microwave, four turnable oven burners, an ...
- **p. 4 / 3 Preliminaries - extractive body cue:** [22]) D, corresponding to demonstrations of meaningful activities provided by the user, without any particular task in mind, e.g. opening cabinet doors, playing with different ...
- **p. 5 / 3 Preliminaries - extractive body cue:** We construct the low-level dataset by iterating through the pool of demonstrations and relabeling them using our relay data relabelling algorithm.
- **p. 5 / 3 Preliminaries - extractive body cue:** To learn the relay policy from these demonstrations, we construct a low-level dataset Dl, and a high-level dataset Dh from these demonstrations via "relay data ...
- **p. 6 / 3 Preliminaries - extractive body cue:** Since these are considered "optimal" for reaching goals along the trajectory, they can be added to the buffer of demonstrations Dl and Dh, thereby contributing ...
- **p. 4 / 3 Preliminaries - extractive body cue:** RIL assumes access to the pool of demonstrations consisting of N trajectories D = {τ i, τ j, τ k, ...}, where each trajectory consists ...
- **p. 7 / 3 Preliminaries - extractive body cue:** (a) (b) (c) (d) Figure 4: Examples of compound goals in the kitchen environment.
- **p. 7 / 3 Preliminaries - extractive body cue:** 5.1 Relay Imitation Learning from Unstructured Demonstrations We start by aiming to understand whether RIL improves imitation learning over standard methods.

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** demonstration으로 정의된 robot task distribution.
- **Input boundary:** observation history와 expert trajectory/action.
- **Output/decision under evaluation:** predicted action 또는 action chunk.
- **Primary target:** imitation error, task success, robustness와 compounding error.
- **Detected evaluation headings:** A Experimental Details (p. 11).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 1: Comparison of RIL to goal-conditioned behavior cloning with and without relabeling in terms success and step-completion rate averaged across 17 tasks. RIL ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 5: Comparison of the RPL algorithm with a number of baselines averaged over 17 compound goals and 2 (baseline methods) or 3 (our ... | p. 8 (Figure/Table caption) |
| 3 Preliminaries | SYSTEM / EVALUATION SCOPE UNRESOLVED | While the success rate drops slightly, this gives us a single multi-task policy that can achieve multiple temporally-extended goals (Fig 5). | p. 8 (3 Preliminaries) |
| 3 Preliminaries | SYSTEM / EVALUATION SCOPE UNRESOLVED | When we analyze the proportion of compound goals that are actually fully achieved (see Table 1, bottom row), RIL shows significant improvement over other ... | p. 7 (3 Preliminaries) |
| 3 Preliminaries | SYSTEM / EVALUATION SCOPE UNRESOLVED | 5 Experimental Results Our experiments aim to answer the following questions: (1) Does RIL improve imitation learning with unstructured and unlabelled demonstrations? | p. 6 (3 Preliminaries) |

## Dataset / Benchmark Role

- **p. 6 / 3 Preliminaries - extractive body cue:** The environment consists of a 9 DoF positioncontrolled Franka robot interacting with a kitchen scene that includes an openable microwave, four turnable oven burners, an ...
- **p. 4 / 3 Preliminaries - extractive body cue:** [22]) D, corresponding to demonstrations of meaningful activities provided by the user, without any particular task in mind, e.g. opening cabinet doors, playing with different ...
- **p. 5 / 3 Preliminaries - extractive body cue:** We construct the low-level dataset by iterating through the pool of demonstrations and relabeling them using our relay data relabelling algorithm.
- **p. 5 / 3 Preliminaries - extractive body cue:** To learn the relay policy from these demonstrations, we construct a low-level dataset Dl, and a high-level dataset Dh from these demonstrations via "relay data ...
- **p. 6 / 3 Preliminaries - extractive body cue:** Since these are considered "optimal" for reaching goals along the trajectory, they can be added to the buffer of demonstrations Dl and Dh, thereby contributing ...
- **p. 4 / 3 Preliminaries - extractive body cue:** RIL assumes access to the pool of demonstrations consisting of N trajectories D = {τ i, τ j, τ k, ...}, where each trajectory consists ...
- **p. 7 / 3 Preliminaries - extractive body cue:** (a) (b) (c) (d) Figure 4: Examples of compound goals in the kitchen environment.
- **p. 7 / 3 Preliminaries - extractive body cue:** 5.1 Relay Imitation Learning from Unstructured Demonstrations We start by aiming to understand whether RIL improves imitation learning over standard methods.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: RPL learns complex, long-horizon manipulation tasks Recent years have seen reinforcement learning (RL) suc- cessfully applied to a number of robotics tasks such ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Relay policy learning: the algorithm starts with relabelling unstructured demonstrations at both the high and the low level of the hierarchical policy and ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: Relay policy architecture: A high level goal setter πθ takes high level goal sh g and sets goals sl g for a lower ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Examples of compound goals in the kitchen environment. Each goal has different elements manipu- lated, requiring multiple stages to solve: (a) microwave, kettle, ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Comparison of RIL to goal-conditioned behavior cloning with and without relabeling in terms success and step-completion rate averaged across 17 tasks. RIL outperforms ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Comparison of the RPL algorithm with a number of baselines averaged over 17 compound goals and 2 (baseline methods) or 3 (our approach) ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6: Left: Role of low level window size in RPL. As the window size increases, imitation learning and fine-tuning become less effective. Right: Role ...
- **p. 12 / Figure/Table caption - extractive body cue:** Figure 7: Splits generated by the oracle segmentation scheme. Each color corresponds to a different split and different demonstrations as plotted as different rows along ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The environment consists of a 9 DoF positioncontrolled Franka robot interacting with a kitchen scene that includes an openable microwave, four turnable oven burners, ... | embodiment, simulator version and control stack | p. 6 (3 Preliminaries), p. 4 (3 Preliminaries) |
| Task/environment | [22]) D, corresponding to demonstrations of meaningful activities provided by the user, without any particular task in mind, e.g. opening cabinet doors, playing with ... | reset, timeout, object/scene variation | p. 4 (3 Preliminaries), p. 5 (3 Preliminaries) |
| Observation/sensor | observation history와 expert trajectory/action | calibration, preprocessing, privileged input | p. 4 (3 Preliminaries), p. 3 (3 Preliminaries) |
| Output/decision | predicted action 또는 action chunk | action frame, controller and termination | p. 5 (3 Preliminaries), p. 5 (3 Preliminaries) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Performing reinforcement fine-tuning individually on 17 different compound goals seen in the demonstrations, we observe a significant improvement in the average success rate and ... | definition/direction/unit from same section | p. 7 (3 Preliminaries) |
| RIL (ours) GCBC relabeling GCBC no relabeling Success Rate (%) 21.7 8.8 7.6 Average Step Completion (of 4) 2.4 ± 1.13 2.2 ± 0.95 ... | definition/direction/unit from same section | p. 7 (3 Preliminaries) |
| Figure 5: Comparison of the RPL algorithm with a number of baselines averaged over 17 compound goals and 2 (baseline methods) or 3 (our ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| While the success rate drops slightly, this gives us a single multi-task policy that can achieve multiple temporally-extended goals (Fig 5). | definition/direction/unit from same section | p. 8 (3 Preliminaries) |
| Evaluation and Comparisons Since each of our tasks consist of compound goals that involve manipulating four elements in the environment, we evaluate policies based ... | definition/direction/unit from same section | p. 6 (3 Preliminaries) |
| [22] for the hierarchical setting, resulting in improved handling of multi-task generalization and compounding error. | definition/direction/unit from same section | p. 4 (3 Preliminaries) |
| However, this policy is often unable to perform well across all temporally extended tasks, due to the well-known compounding errors stemming from imitation learning ... | definition/direction/unit from same section | p. 5 (3 Preliminaries) |
| For the high-level policy, given a high-level goal-reaching reward function rh(st, gt, sh g), we can optimize it by running a similar goal-conditioned policy ... | definition/direction/unit from same section | p. 5 (3 Preliminaries) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 5: Comparison of the RPL algorithm with a number of baselines averaged over 17 compound goals and 2 (baseline methods) or 3 (our ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| The RPL method also outperforms the pre-train-low-level baseline, which we hypothesize is because we are not able to search very effectively in the goal ... | comparison identity and matched condition | p. 8 (3 Preliminaries) |
| Table 1: Comparison of RIL to goal-conditioned behavior cloning with and without relabeling in terms success and step-completion rate averaged across 17 tasks. RIL ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| For comparisons with methods that learn from scratch we compare with (6) an on-policy variant of HIRO [15] trained from scratch with natural policy ... | comparison identity and matched condition | p. 7 (3 Preliminaries) |
| Figure 7: Splits generated by the oracle segmentation scheme. Each color corresponds to a different split and different demonstrations as plotted as different rows ... | comparison identity and matched condition | p. 12 (Figure/Table caption) |
| [22]) D, corresponding to demonstrations of meaningful activities provided by the user, without any particular task in mind, e.g. opening cabinet doors, playing with ... | comparison identity and matched condition | p. 4 (3 Preliminaries) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We experiment with three variants of the fine-tuning update in our experimental evaluation: IRIL-RPL (fine-tuning with Eqn 2, 3 and iterative relay data relabeling ... | component/input/data sensitivity | p. 6 (3 Preliminaries) |
| Each goal has different elements manipulated, requiring multiple stages to solve: (a) microwave, kettle, light, slider, (b) kettle, burner, slider, cabinet, (c) burner, top ... | component/input/data sensitivity | p. 7 (3 Preliminaries) |
| The RPL method also outperforms the pre-train-low-level baseline, which we hypothesize is because we are not able to search very effectively in the goal ... | component/input/data sensitivity | p. 8 (3 Preliminaries) |
| Performing reinforcement fine-tuning individually on 17 different compound goals seen in the demonstrations, we observe a significant improvement in the average success rate and ... | component/input/data sensitivity | p. 7 (3 Preliminaries) |
| Fine-tuning with all three variants of our method outperforms fine-tuning using flat policies. | component/input/data sensitivity | p. 8 (3 Preliminaries) |
| [22]) D, corresponding to demonstrations of meaningful activities provided by the user, without any particular task in mind, e.g. opening cabinet doors, playing with ... | component/input/data sensitivity | p. 4 (3 Preliminaries) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Lastly, and most importantly, since our method ensures that every low-level trajectory is goal-conditioned (allowing for a simple reward specification) and of the same, ... | Table 1: Comparison of RIL to goal-conditioned behavior cloning with and without relabeling in terms success and step-completion rate averaged across 17 tasks. RIL ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 8 (3 Preliminaries), p. 7 (3 Preliminaries), p. 6 (3 Preliminaries), p. 4 (3 Preliminaries) |
| Primary metric/result | Figure 5: Comparison of the RPL algorithm with a number of baselines averaged over 17 compound goals and 2 (baseline methods) or 3 (our ... | numeric claim only at cited anchor | p. 8 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 4 / 3 Preliminaries - extractive body cue:** 7: end while 8: Distill fine-tuned policies into a single multi-goal policy Algorithm 2 Relay data relabeling for RIL low level Require: Demonstrations D = ...
- **p. 7 / 3 Preliminaries - extractive body cue:** RIL (ours) GCBC relabeling GCBC no relabeling Success Rate (%) 21.7 8.8 7.6 Average Step Completion (of 4) 2.4 ± 1.13 2.2 ± 0.95 1.78 ...
- **p. 4 / 3 Preliminaries - extractive body cue:** 7: end while 8: Distill fine-tuned policies into a single multi-goal policy Algorithm 2 Relay data relabeling for RIL low level Require: Demonstrations D = ...
- **p. 7 / 3 Preliminaries - extractive body cue:** RIL (ours) GCBC relabeling GCBC no relabeling Success Rate (%) 21.7 8.8 7.6 Average Step Completion (of 4) 2.4 ± 1.13 2.2 ± 0.95 1.78 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 9: Visualization of successful learned behavior for moving kettle, turning top knob, sliding the slider and opening the hinge cabinet D.2 Failure Cases | p. 13 (Figure/Table caption) |
| body limitation/failure cue | While these trajectories did not necessarily reach the goals that were originally commanded, and therefore cannot be considered optimal for those goals, they do ... | p. 6 (3 Preliminaries) |
| body limitation/failure cue | Figure 10: Visualization of failing learned behavior for moving kettle, turning the bottom knob, moving the slider and turning on the oven light 13 | p. 13 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We simplify the long-horizon policy learning problem by using a novel data-relabeling algorithm for learning goal-conditioned hierarchical policies, where the low-level only acts for ... | p. 1 (Abstract) |
| For the subsequent H steps, the goal produced by πh θ is kept fixed, while πl θ generates an action at at every time ... | p. 4 (3 Preliminaries) |
| Env Env Env Env Env Env Env High level goal Figure 3: Relay policy architecture: A high level goal setter πθ takes high level ... | p. 4 (3 Preliminaries) |
| The key idea behind relay data relabeling is to consider all states that are actually reached along a demonstration trajectory within Wl time steps ... | p. 5 (3 Preliminaries) |
| We also label all states st+1, ...., st+Wh along a valid trajectory as potential high-level goals that are reached from state st by the ... | p. 5 (3 Preliminaries) |
| Evaluation and Comparisons Since each of our tasks consist of compound goals that involve manipulating four elements in the environment, we evaluate policies based ... | p. 6 (3 Preliminaries) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 13 / Figure/Table caption - extractive body cue:** Figure 9: Visualization of successful learned behavior for moving kettle, turning top knob, sliding the slider and opening the hinge cabinet D.2 Failure Cases
- **p. 6 / 3 Preliminaries - extractive body cue:** While these trajectories did not necessarily reach the goals that were originally commanded, and therefore cannot be considered optimal for those goals, they do end ...
- **p. 13 / Figure/Table caption - extractive body cue:** Figure 10: Visualization of failing learned behavior for moving kettle, turning the bottom knob, moving the slider and turning on the oven light 13

- **Evidence anchors reviewed:** datasets p. 6 (3 Preliminaries), p. 4 (3 Preliminaries), p. 5 (3 Preliminaries), p. 5 (3 Preliminaries), p. 6 (3 Preliminaries), p. 4 (3 Preliminaries), metrics p. 7 (3 Preliminaries), p. 7 (3 Preliminaries), p. 8 (Figure/Table caption), p. 8 (3 Preliminaries), p. 6 (3 Preliminaries), p. 4 (3 Preliminaries), baselines p. 8 (Figure/Table caption), p. 8 (3 Preliminaries), p. 7 (Figure/Table caption), p. 7 (3 Preliminaries), p. 12 (Figure/Table caption), p. 4 (3 Preliminaries), results p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 8 (3 Preliminaries), p. 7 (3 Preliminaries), p. 6 (3 Preliminaries), p. 4 (3 Preliminaries).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Figure 5: Comparison of the RPL algorithm with a number of baselines averaged over 17 compound goals and 2 (baseline methods) or 3 (our approach) random seeds. Fine-tuning with all ... (p. 8, Figure/Table caption).
- **Metric evidence:** Performing reinforcement fine-tuning individually on 17 different compound goals seen in the demonstrations, we observe a significant improvement in the average success rate and stepwise completion scores over all the ... (p. 7, 3 Preliminaries).
- **Baseline/ablation evidence:** Figure 5: Comparison of the RPL algorithm with a number of baselines averaged over 17 compound goals and 2 (baseline methods) or 3 (our approach) random seeds. Fine-tuning with all ... (p. 8, Figure/Table caption).
- **Failure/negative evidence:** While these trajectories did not necessarily reach the goals that were originally commanded, and therefore cannot be considered optimal for those goals, they do end up reaching the actual states ... (p. 6, 3 Preliminaries).
