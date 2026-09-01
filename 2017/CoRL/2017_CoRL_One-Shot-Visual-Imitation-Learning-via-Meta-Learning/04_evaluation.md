# Evaluation - One-Shot Visual Imitation Learning via Meta-Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1703.07326; PDF retrieval source: https://arxiv.org/pdf/1703.07326. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 14 (Figure/Table caption), p. 7 (5 Experiments), p. 7 (Figure/Table caption), p. 5 (Figure/Table caption), p. 8 (5 Experiments), p. 8 (5 Experiments)): Figure 2: Success rates of different architectures for particle reaching. The "Train" curves show the success rates when conditioned on demonstrations seen during training, and running the policy on initial ...

## Evaluation Body Digest

- **p. 6 / 5 Experiments - extractive PDF cue:** We conduct experiments with the block stacking tasks described in Section 3.2.2 These experiments are designed to answer the following questions: • How does training ...
- **p. 7 / 5 Experiments - extractive PDF cue:** We measure success rate per task by executing the greedy policy (taking the most confident action at every time step) in 100 different configurations, each ...
- **p. 7 / 5 Experiments - extractive PDF cue:** However, a full trajectory, one which contains information about intermediate stages of the task's solution, can make it easier to train the optimal policy, because ...
- **p. 8 / 5 Experiments - extractive PDF cue:** In practice, such noise can come from natural human-induced noise through tele-operation, or by artificially injecting additional noise before applying it on the physical robot.
- **p. 8 / 5 Experiments - extractive PDF cue:** We are also interested in enabling the policy to condition on multiple demonstrations, in case where one demonstration does not fully resolve ambiguity in the ...
- **p. 6 / 5 Experiments - extractive PDF cue:** But we did not find this necessary for the tasks we consider.
- **p. 7 / 5 Experiments - extractive PDF cue:** 2 4 5 6 7 8 Number of Stages 0% 20% 40% 60% 80% 100% Average Success Rate Policy Type Demo BC DAGGER Snapshot Final ...
- **p. 7 / 5 Experiments - extractive PDF cue:** We report the average success rate over all tasks within the same group.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** demonstration으로 정의된 robot task distribution.
- **Input boundary:** observation history와 expert trajectory/action.
- **Output/decision under evaluation:** predicted action 또는 action chunk.
- **Primary target:** imitation error, task success, robustness와 compounding error.
- **Detected evaluation headings:** 5 Experiments (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 2: Success rates of different architectures for particle reaching. The "Train" curves show the success rates when conditioned on demonstrations seen during training, ... | p. 14 (Figure/Table caption) |
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | 2 4 5 6 7 8 Number of Stages 0% 20% 40% 60% 80% 100% Average Success Rate Policy Type Demo BC DAGGER Snapshot ... | p. 7 (5 Experiments) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 3: Comparison of different conditioning strategies. The darkest bar shows the performance of the hard-coded policy, which unsurprisingly performs the best most of ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 2: Illustration of the network architecture. In our experiments, we use p = 0.95, which reduces the length of demonstrations by a factor ... | p. 5 (Figure/Table caption) |
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | As the difficulty (number of stages) increases, however, conditioning on the entire demonstration starts to outperform conditioning on the final state. | p. 8 (5 Experiments) |

## Dataset / Benchmark Role

- **p. 6 / 5 Experiments - extractive PDF cue:** We conduct experiments with the block stacking tasks described in Section 3.2.2 These experiments are designed to answer the following questions: • How does training ...
- **p. 7 / 5 Experiments - extractive PDF cue:** We measure success rate per task by executing the greedy policy (taking the most confident action at every time step) in 100 different configurations, each ...
- **p. 7 / 5 Experiments - extractive PDF cue:** However, a full trajectory, one which contains information about intermediate stages of the task's solution, can make it easier to train the optimal policy, because ...
- **p. 8 / 5 Experiments - extractive PDF cue:** In practice, such noise can come from natural human-induced noise through tele-operation, or by artificially injecting additional noise before applying it on the physical robot.
- **p. 8 / 5 Experiments - extractive PDF cue:** We are also interested in enabling the policy to condition on multiple demonstrations, in case where one demonstration does not fully resolve ambiguity in the ...
- **p. 6 / 5 Experiments - extractive PDF cue:** But we did not find this necessary for the tasks we consider.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: (a) Traditionally, policies are task-specific. For example, a policy might have been trained through an imitation learning algorithm to stack blocks into towers ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 2: Illustration of the network architecture. In our experiments, we use p = 0.95, which reduces the length of demonstrations by a factor of ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 3: Comparison of different conditioning strategies. The darkest bar shows the performance of the hard-coded policy, which unsurprisingly performs the best most of the ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4: Visualizing attentions performed by the policy during an entire execution. The task being performed is ab cde fg hij. Note that the policy ...
- **p. 13 / Figure/Table caption - extractive PDF cue:** Figure 1: The robot is a point mass controlled with 2-dimensional force. The family of tasks is to reach a target landmark. The identity of ...
- **p. 14 / Figure/Table caption - extractive PDF cue:** Figure 2: Success rates of different architectures for particle reaching. The "Train" curves show the success rates when conditioned on demonstrations seen during training, and ...
- **p. 14 / Figure/Table caption - extractive PDF cue:** Table 1: Success rates of particle reaching conditioned on seen demonstrations, and running on seen initial configurations. B Further Details on Block Stacking B.1 Full ...
- **p. 15 / Figure/Table caption - extractive PDF cue:** Figure 3: Learning curves for particle reaching tasks. Shown success rates are moving averages of past 10 epochs for smoother curves. Each policy is trained ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We conduct experiments with the block stacking tasks described in Section 3.2.2 These experiments are designed to answer the following questions: • How does ... | embodiment, simulator version and control stack | p. 6 (5 Experiments), p. 7 (5 Experiments) |
| Task/environment | We measure success rate per task by executing the greedy policy (taking the most confident action at every time step) in 100 different configurations, ... | reset, timeout, object/scene variation | p. 7 (5 Experiments), p. 7 (5 Experiments) |
| Observation/sensor | observation history와 expert trajectory/action | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 1 (Abstract) |
| Output/decision | predicted action 또는 action chunk | action frame, controller and termination | p. 2 (1 Introduction), p. 5 (B C) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 2 4 5 6 7 8 Number of Stages 0% 20% 40% 60% 80% 100% Average Success Rate Policy Type Demo BC DAGGER Snapshot ... | definition/direction/unit from same section | p. 7 (5 Experiments) |
| We report the average success rate over all tasks within the same group. | definition/direction/unit from same section | p. 7 (5 Experiments) |
| Figure 2: Success rates of different architectures for particle reaching. The "Train" curves show the success rates when conditioned on demonstrations seen during training, ... | definition/direction/unit from same section | p. 14 (Figure/Table caption) |
| Table 1: Success rates of particle reaching conditioned on seen demonstrations, and running on seen initial configurations. B Further Details on Block Stacking B.1 ... | definition/direction/unit from same section | p. 14 (Figure/Table caption) |
| Figure 3: Learning curves for particle reaching tasks. Shown success rates are moving averages of past 10 epochs for smoother curves. Each policy is ... | definition/direction/unit from same section | p. 15 (Figure/Table caption) |
| Table 4: Success rates of different architectures on test tasks of block stacking. #Stages | definition/direction/unit from same section | p. 21 (Figure/Table caption) |
| Table 5: Success rates of varying number of ensembles using the DAGGER policy conditioned on full trajectories, across both training and test tasks. 9 | definition/direction/unit from same section | p. 21 (Figure/Table caption) |
| Table 6: Success rates of a set of tasks that are equivalent up to permutations, using the DAGGER policy conditioned on full trajectories. #Stages ... | definition/direction/unit from same section | p. 22 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| This assumes that a segmentation of the demonstration into multiple stages is available at test time, which gives it an unfair advantage compared to ... | comparison identity and matched condition | p. 7 (5 Experiments) |
| As the difficulty (number of stages) increases, however, conditioning on the entire demonstration starts to outperform conditioning on the final state. | comparison identity and matched condition | p. 8 (5 Experiments) |
| More surprisingly, conditioning on the entire demonstration also seems to outperform conditioning on the snapshot, which we originally expected to perform the best. | comparison identity and matched condition | p. 8 (5 Experiments) |
| A comparison between the two conditioning strategies will tell us whether this hypothesis is valid. | comparison identity and matched condition | p. 7 (5 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| However, a full trajectory, one which contains information about intermediate stages of the task's solution, can make it easier to train the optimal policy, ... | component/input/data sensitivity | p. 7 (5 Experiments) |
| We plan to extend the framework to demonstrations in the form of image data, which will allow more end-to-end learning without requiring a separate ... | component/input/data sensitivity | p. 8 (5 Experiments) |
| Another interesting finding was that training with behavioral cloning has the same level of performance as training with DAGGER, which suggests that the entire ... | component/input/data sensitivity | p. 8 (5 Experiments) |
| 1In principle, one can replace this module with an RNN module. | component/input/data sensitivity | p. 6 (5 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper, we propose a meta-learning framework for achieving such capability, which we call one-shot imitation learning. | Figure 2: Success rates of different architectures for particle reaching. The "Train" curves show the success rates when conditioned on demonstrations seen during training, ... | PDF body cue; verify exact table/figure and matched conditions | p. 14 (Figure/Table caption), p. 7 (5 Experiments), p. 7 (Figure/Table caption), p. 5 (Figure/Table caption), p. 8 (5 Experiments), p. 8 (5 Experiments) |
| Primary metric/result | 2 4 5 6 7 8 Number of Stages 0% 20% 40% 60% 80% 100% Average Success Rate Policy Type Demo BC DAGGER Snapshot ... | numeric claim only at cited anchor | p. 7 (5 Experiments) |

- Numeric sentences retained from the body:
- **p. 7 / 5 Experiments - extractive PDF cue:** We collect 1000 trajectories per task for training, and maintain a separate set of trajectories and initial configurations to be used for evaluation.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 6: Breakdown of the success and failure scenarios. The area that each color occupies represent the ratio of the corresponding scenario. B.5 Learning ... | p. 19 (Figure/Table caption) |
| body limitation/failure cue | Table 8: Breakdown of success and failure scenarios for DAGGER policy. 10 | p. 22 (Figure/Table caption) |
| body limitation/failure cue | Table 6: Success rates of a set of tasks that are equivalent up to permutations, using the DAGGER policy conditioned on full trajectories. #Stages ... | p. 22 (Figure/Table caption) |
| body limitation/failure cue | In fact, even our scripted policy frequently fails on the hardest tasks. | p. 7 (5 Experiments) |
| body limitation/failure cue | We leave this possibility for future work. | p. 6 (B C) |
| body limitation/failure cue | It processes both the current state and the embedding produced by the demonstration network, and outputs a context embedding, whose dimension does not depend ... | p. 6 (B C) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The trajectories are collected using a hard-coded policy. | p. 7 (5 Experiments) |
| The darkest bar shows the performance of the hard-coded policy, which unsurprisingly performs the best most of the time. | p. 7 (5 Experiments) |
| (b) We can observe a sparse pattern of time steps that have high attention weights. | p. 8 (5 Experiments) |
| There are two kinds of attention we are mainly interested in, one where the policy attends to different time steps in the demonstration, and ... | p. 8 (5 Experiments) |
| At training time, our algorithm is presented with pairs of demonstrations for a subset of all tasks. | p. 1 (Abstract) |
| Given this list of embeddings, we use two separate linear layers to compute a query vector and a context embedding for each block: qi ... | p. 5 (B C) |
| During test time, we can sample multiple downsampled trajectories, use each of them to compute downstream results, and average these results to produce an ... | p. 5 (B C) |
| Attention over demonstration: The context network starts by computing a query vector as a function of the current state, which is then used to ... | p. 6 (B C) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 19 / Figure/Table caption - extractive PDF cue:** Figure 6: Breakdown of the success and failure scenarios. The area that each color occupies represent the ratio of the corresponding scenario. B.5 Learning Curves ...
- **p. 22 / Figure/Table caption - extractive PDF cue:** Table 8: Breakdown of success and failure scenarios for DAGGER policy. 10
- **p. 22 / Figure/Table caption - extractive PDF cue:** Table 6: Success rates of a set of tasks that are equivalent up to permutations, using the DAGGER policy conditioned on full trajectories. #Stages Success ...
- **p. 7 / 5 Experiments - extractive PDF cue:** In fact, even our scripted policy frequently fails on the hardest tasks.
- **p. 6 / B C - extractive PDF cue:** We leave this possibility for future work.
- **p. 6 / B C - extractive PDF cue:** It processes both the current state and the embedding produced by the demonstration network, and outputs a context embedding, whose dimension does not depend on ...

- **PDF anchors reviewed:** datasets p. 6 (5 Experiments), p. 7 (5 Experiments), p. 7 (5 Experiments), p. 8 (5 Experiments), p. 8 (5 Experiments), p. 6 (5 Experiments), metrics p. 7 (5 Experiments), p. 7 (5 Experiments), p. 14 (Figure/Table caption), p. 14 (Figure/Table caption), p. 15 (Figure/Table caption), p. 21 (Figure/Table caption), baselines p. 7 (5 Experiments), p. 8 (5 Experiments), p. 8 (5 Experiments), p. 7 (5 Experiments), results p. 14 (Figure/Table caption), p. 7 (5 Experiments), p. 7 (Figure/Table caption), p. 5 (Figure/Table caption), p. 8 (5 Experiments), p. 8 (5 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
