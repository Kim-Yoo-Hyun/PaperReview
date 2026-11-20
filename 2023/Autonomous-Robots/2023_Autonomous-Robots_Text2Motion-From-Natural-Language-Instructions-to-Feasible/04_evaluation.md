# Evaluation - Text2Motion: From Natural Language Instructions to Feasible Plans

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (30 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2303.12153; PDF retrieval source: https://arxiv.org/pdf/2303.12153. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 11 (6.2 Search-based reasoning is), p. 11 (6.2 Search-based reasoning is), p. 10 (6.1 Feasibility planning is required), p. 12 (6.4 Plan termination is made), p. 12 (6.4 Plan termination is made), p. 10 (6.1 Feasibility planning is required)): In the first two tasks (LH, Figure 5), we find that shooting achieves slightly higher success rates than greedy-search, while both methods achieve 100% success rates in the third task ...

## Evaluation Body Digest

- **p. 9 / 5.4 Task suite - extractive body cue:** For example, Task 1 in Figure 4 requires the robot to pick and place three objects for a total of six skills.
- **p. 9 / 5.4 Task suite - extractive body cue:** However, the scene description obtained through predicate classifiers Lχ (described in Section 4.1) and the instruction i do not indicate whether it is necessary to ...
- **p. 8 / 5.1 Baselines - extractive body cue:** Execution terminates when the score of the stop "skill" is larger than the other skills. innermono-gs: We implement the Object + Scene variant of Inner ...
- **p. 8 / 5 Experiments - extractive body cue:** We conduct experiments to test four hypotheses: H1 Geometric feasibility planning is a necessary ingredient when using LLMs and robot skills to solve manipulation tasks ...
- **p. 11 / 6.2 Search-based reasoning is - extractive body cue:** For example, Task 1 (Figure 4) asks the robot to put three boxes onto the rack; shooting allows the robot to test multiple different skill ...
- **p. 10 / 5.5 Evaluation and metrics - extractive body cue:** Success rates are averaged over ten random seeds per task, where each seed corresponds to a different geometric instantiation of the task (Section 5.4).
- **p. 10 / 5.5 Evaluation and metrics - extractive body cue:** We do not perform task-level replanning, which would involve querying the LLM at timestep t + 1 for a new sequence of skills ψt+1:H. saycan-gs ...
- **p. 11 / 6.1 Feasibility planning is required - extractive body cue:** Bottom: For the non-PAP tasks, shooting outperforms greedy-search.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** graph, configuration space 또는 task-and-motion planning domain.
- **Input boundary:** start/goal, map, dynamics와 successor/operator description.
- **Output/decision under evaluation:** feasible action sequence 또는 minimum-cost plan.
- **Primary target:** path cost, goal reachability, feasibility와 computation.
- **Detected evaluation headings:** 5 Experiments (p. 8); 5.5 Evaluation and metrics (p. 9); 6 Results (p. 10).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 6.2 Search-based reasoning is | EMPIRICAL / SOURCE-REPORTED EVALUATION | In the first two tasks (LH, Figure 5), we find that shooting achieves slightly higher success rates than greedy-search, while both methods achieve 100% ... | p. 11 (6.2 Search-based reasoning is) |
| 6.2 Search-based reasoning is | EMPIRICAL / SOURCE-REPORTED EVALUATION | In terms of success, greedysearch solves 40%-60% of the PAP tasks, while shooting achieves a 10% success rate on Task 4 (LG + PAP) ... | p. 11 (6.2 Search-based reasoning is) |
| 6.1 Feasibility planning is required | EMPIRICAL / SOURCE-REPORTED EVALUATION | This divergence arises because it is possible to make progress on tasks without resolving geometric dependencies in the earlier timesteps; however, failure to account ... | p. 10 (6.1 Feasibility planning is required) |
| 6.4 Plan termination is made | EMPIRICAL / SOURCE-REPORTED EVALUATION | We find that terminating planning when LLM-predicted goals are satisfied results in a 10% boost in success rate over stop scoring. at every timestep. | p. 12 (6.4 Plan termination is made) |
| 6.4 Plan termination is made | EMPIRICAL / SOURCE-REPORTED EVALUATION | The results in Figure 7 suggest that, for the tasks we consider, our proposed goal prediction method leads to 10% higher success rates than ... | p. 12 (6.4 Plan termination is made) |

## Dataset / Benchmark Role

- **p. 9 / 5.4 Task suite - extractive body cue:** For example, Task 1 in Figure 4 requires the robot to pick and place three objects for a total of six skills.
- **p. 9 / 5.4 Task suite - extractive body cue:** However, the scene description obtained through predicate classifiers Lχ (described in Section 4.1) and the instruction i do not indicate whether it is necessary to ...
- **p. 8 / 5.1 Baselines - extractive body cue:** Execution terminates when the score of the stop "skill" is larger than the other skills. innermono-gs: We implement the Object + Scene variant of Inner ...
- **p. 8 / 5 Experiments - extractive body cue:** We conduct experiments to test four hypotheses: H1 Geometric feasibility planning is a necessary ingredient when using LLMs and robot skills to solve manipulation tasks ...
- **p. 11 / 6.2 Search-based reasoning is - extractive body cue:** For example, Task 1 (Figure 4) asks the robot to put three boxes onto the rack; shooting allows the robot to test multiple different skill ...
- **p. 10 / 5.5 Evaluation and metrics - extractive body cue:** Success rates are averaged over ten random seeds per task, where each seed corresponds to a different geometric instantiation of the task (Section 5.4).
- **p. 10 / 5.5 Evaluation and metrics - extractive body cue:** We do not perform task-level replanning, which would involve querying the LLM at timestep t + 1 for a new sequence of skills ψt+1:H. saycan-gs ...
- **p. 11 / 6.1 Feasibility planning is required - extractive body cue:** Bottom: For the non-PAP tasks, shooting outperforms greedy-search.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. Second, they do not explicitly predict a multi-step plan, which prevents verification of desired properties or outcomes prior to execu- tion. Examples of ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For example, Task 1 in Figure 4 requires the robot to pick and place three objects for a total of six skills. | embodiment, simulator version and control stack | p. 9 (5.4 Task suite), p. 9 (5.4 Task suite) |
| Task/environment | However, the scene description obtained through predicate classifiers Lχ (described in Section 4.1) and the instruction i do not indicate whether it is necessary ... | reset, timeout, object/scene variation | p. 9 (5.4 Task suite), p. 8 (5.1 Baselines) |
| Observation/sensor | start/goal, map, dynamics와 successor/operator description | calibration, preprocessing, privileged input | p. 5 (4.1 Goal prediction), p. 3 (3.1 LLM and skill library) |
| Output/decision | feasible action sequence 또는 minimum-cost plan | action frame, controller and termination | p. 5 (4.1 Goal prediction), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Reported metrics: We report success rates and subgoal completion rates for all methods. | definition/direction/unit from same section | p. 10 (5.5 Evaluation and metrics) |
| Bottom: Methods without geometric feasibility planning tend to have high sub-goal completion rates but very low success rates. | definition/direction/unit from same section | p. 10 (6.1 Feasibility planning is required) |
| In the first two tasks (LH, Figure 5), we find that shooting achieves slightly higher success rates than greedy-search, while both methods achieve 100% ... | definition/direction/unit from same section | p. 11 (6.2 Search-based reasoning is) |
| In terms of success, greedysearch solves 40%-60% of the PAP tasks, while shooting achieves a 10% success rate on Task 4 (LG + PAP) ... | definition/direction/unit from same section | p. 11 (6.2 Search-based reasoning is) |
| We find that terminating planning when LLM-predicted goals are satisfied results in a 10% boost in success rate over stop scoring. at every timestep. | definition/direction/unit from same section | p. 12 (6.4 Plan termination is made) |
| The results in Figure 7 suggest that, for the tasks we consider, our proposed goal prediction method leads to 10% higher success rates than ... | definition/direction/unit from same section | p. 12 (6.4 Plan termination is made) |
| For consistency, we use the same skill library Lψ, with independently trained policies π and Q-functions Qπ, the OOD rejection strategy (Section 4.5) and, ... | definition/direction/unit from same section | p. 8 (5.1 Baselines) |
| We acquire innermono-gs by equipping [4] with generator-scorer for cost efficiency. | definition/direction/unit from same section | p. 8 (5.1 Baselines) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Top: Our method (Text2Motion) significantly outperforms all baselines on tasks involving partial affordance perception (Task 4, 5, 6). | comparison identity and matched condition | p. 10 (6.1 Feasibility planning is required) |
| For tasks without partial affordance perception, the methods that use geometric feasibility planning (Text2Motion, shooting, greedy-search) convincingly outperform the methods (saycan-gs and innermono-gs) that ... | comparison identity and matched condition | p. 10 (6.1 Feasibility planning is required) |
| H2 greedy-search is better equipped to solve tasks with partial affordance perception (as defined in Section 5.4) compared to shooting. | comparison identity and matched condition | p. 8 (5 Experiments) |
| The following subsections describe the baseline methods we compare against, details on LLMs and prompts, the tasks over which planners are evaluated, and performance ... | comparison identity and matched condition | p. 8 (5 Experiments) |
| Bottom: For the non-PAP tasks, shooting outperforms greedy-search. | comparison identity and matched condition | p. 11 (6.1 Feasibility planning is required) |
| The results in Figure 7 suggest that, for the tasks we consider, our proposed goal prediction method leads to 10% higher success rates than ... | comparison identity and matched condition | p. 12 (6.4 Plan termination is made) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We use two pretrained language models, both of which were accessed through the OpenAI API: i) text-davinci-003, a variant of the InstructGPT [61] language ... | component/input/data sensitivity | p. 8 (5.2 Large language model) |
| Execution terminates when the score of the stop "skill" is larger than the other skills. innermono-gs: We implement the Object + Scene variant of ... | component/input/data sensitivity | p. 8 (5.1 Baselines) |
| We do not perform task-level replanning, which would involve querying the LLM at timestep t + 1 for a new sequence of skills ψt+1:H. ... | component/input/data sensitivity | p. 10 (5.5 Evaluation and metrics) |
| Bottom: Methods without geometric feasibility planning tend to have high sub-goal completion rates but very low success rates. | component/input/data sensitivity | p. 10 (6.1 Feasibility planning is required) |
| In this plot, we analyse the various types of failure modes that occur with Text2Motion, shooting and greedy-search when evaluated on tasks with partial ... | component/input/data sensitivity | p. 11 (6.1 Feasibility planning is required) |
| Plan Length 5.0 7.0 7.0 Table 1 Ablation on hybrid planning method. | component/input/data sensitivity | p. 12 (6.2 Search-based reasoning is) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We propose Text2Motion, a language-based planning framework that interfaces an LLM with a library of learned skills and a geometric feasibility planner [8] to ... | In the first two tasks (LH, Figure 5), we find that shooting achieves slightly higher success rates than greedy-search, while both methods achieve 100% ... | PDF body cue; verify exact table/figure and matched conditions | p. 11 (6.2 Search-based reasoning is), p. 11 (6.2 Search-based reasoning is), p. 10 (6.1 Feasibility planning is required), p. 12 (6.4 Plan termination is made), p. 12 (6.4 Plan termination is made), p. 10 (6.1 Feasibility planning is required) |
| Primary metric/result | In terms of success, greedysearch solves 40%-60% of the PAP tasks, while shooting achieves a 10% success rate on Task 4 (LG + PAP) ... | numeric claim only at cited anchor | p. 11 (6.2 Search-based reasoning is) |

- Numeric sentences retained from the body:
- **p. 12 / 6.2 Search-based reasoning is - extractive body cue:** Hybrid planning breakdown Task 4 Task 5 Task 6 % shooting only 14% 0% 0% % greedy-search only 0% 0% 0% % Combination 86% 100% ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Text2Motion relies on greedy-search as a fallback if shooting fails, and thus can also contend with PAP tasks. | p. 11 (6.1 Feasibility planning is required) |
| body limitation/failure cue | Two failure cases are tracked: i) planning failure: the method does not produce a sequence of skills ψ1:H whose optimized parameters a∗ 1:H (Eq. | p. 9 (5.5 Evaluation and metrics) |
| body limitation/failure cue | 4) results in a state that satisfies F G sat within a maximum plan length of dmax; ii) execution failure: the execution of a ... | p. 9 (5.5 Evaluation and metrics) |
| body limitation/failure cue | This is expected because shooting does not exhibit planning failures on these tasks (Figure 6) and Text2Motion starts by invoking shooting, which results in ... | p. 11 (6.2 Search-based reasoning is) |
| body limitation/failure cue | While we mitigate such failures by combining greedy-search and shooting in the hybrid Text2Motion algorithm, leveraging calibration techniques to increase the reliability LLM likelihoods ... | p. 12 (7 Limitations and Future Work) |
| body limitation/failure cue | To further delineate the performance of Text2Motion from shooting and greedy-search, we also report the percentages of planning and execution failures. | p. 10 (5.5 Evaluation and metrics) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Subgoal completion rates are computed over all plans by measuring the number of steps an oracle planner would take to reach the ground-truth goal ... | p. 10 (5.5 Evaluation and metrics) |
| For all other queries, we use code-davinci-002 as it was found to be reliable. | p. 8 (5.2 Large language model) |
| We use two pretrained language models, both of which were accessed through the OpenAI API: i) text-davinci-003, a variant of the InstructGPT [61] language ... | p. 8 (5.2 Large language model) |
| To compute the skill usefulness (Eq. | p. 9 (5.3 Prompt engineering) |
| Hence, we evaluate them in a closed-loop manner for a maximum of dmax steps. | p. 10 (5.5 Evaluation and metrics) |
| We run 120 experiments (two variations, six tasks, and ten seeds each) in total on the TableEnv Manipulation task suite. | p. 12 (6.4 Plan termination is made) |
| K do 7: s(j) 2:H+1, a(j) 1:H ←STAP(s1, ψ(j) 1:H, Lψ) 8: if F G sat(s(j) t ) == 1 for t ≤H + ... | p. 5 (4.2 Shooting-based planning) |
| 11 by the Q-value evaluated at predicted future state st with optimized parameter a∗ t , both of which are computed by the geometric ... | p. 6 (4.3 Search-based planning) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 11 / 6.1 Feasibility planning is required - extractive body cue:** Text2Motion relies on greedy-search as a fallback if shooting fails, and thus can also contend with PAP tasks.
- **p. 9 / 5.5 Evaluation and metrics - extractive body cue:** Two failure cases are tracked: i) planning failure: the method does not produce a sequence of skills ψ1:H whose optimized parameters a∗ 1:H (Eq.
- **p. 9 / 5.5 Evaluation and metrics - extractive body cue:** 4) results in a state that satisfies F G sat within a maximum plan length of dmax; ii) execution failure: the execution of a plan ...
- **p. 11 / 6.2 Search-based reasoning is - extractive body cue:** This is expected because shooting does not exhibit planning failures on these tasks (Figure 6) and Text2Motion starts by invoking shooting, which results in their ...
- **p. 12 / 7 Limitations and Future Work - extractive body cue:** While we mitigate such failures by combining greedy-search and shooting in the hybrid Text2Motion algorithm, leveraging calibration techniques to increase the reliability LLM likelihoods [64, ...
- **p. 10 / 5.5 Evaluation and metrics - extractive body cue:** To further delineate the performance of Text2Motion from shooting and greedy-search, we also report the percentages of planning and execution failures.

- **Evidence anchors reviewed:** datasets p. 9 (5.4 Task suite), p. 9 (5.4 Task suite), p. 8 (5.1 Baselines), p. 8 (5 Experiments), p. 11 (6.2 Search-based reasoning is), p. 10 (5.5 Evaluation and metrics), metrics p. 10 (5.5 Evaluation and metrics), p. 10 (6.1 Feasibility planning is required), p. 11 (6.2 Search-based reasoning is), p. 11 (6.2 Search-based reasoning is), p. 12 (6.4 Plan termination is made), p. 12 (6.4 Plan termination is made), baselines p. 10 (6.1 Feasibility planning is required), p. 10 (6.1 Feasibility planning is required), p. 8 (5 Experiments), p. 8 (5 Experiments), p. 11 (6.1 Feasibility planning is required), p. 12 (6.4 Plan termination is made), results p. 11 (6.2 Search-based reasoning is), p. 11 (6.2 Search-based reasoning is), p. 10 (6.1 Feasibility planning is required), p. 12 (6.4 Plan termination is made), p. 12 (6.4 Plan termination is made), p. 10 (6.1 Feasibility planning is required).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
