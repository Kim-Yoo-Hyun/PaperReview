# Evaluation - Learning Robust Rewards with Adversarial Inverse Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1710.11248; PDF retrieval source: https://arxiv.org/pdf/1710.11248. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (7 EXPERIMENTS), p. 7 (Figure/Table caption), p. 6 (7 EXPERIMENTS), p. 8 (7 EXPERIMENTS), p. 7 (7 EXPERIMENTS), p. 8 (7 EXPERIMENTS)): We also show that in the transfer learning setup, under a new transition matrix T ′, the optimal policy under the state-only reward achieves optimal performance (it is identical to ...

## Evaluation Body Digest

- **p. 6 / 7 EXPERIMENTS - extractive body cue:** (2016a), which we refer to as GAN-GCL, on standard benchmark tasks that do not evaluate transfer.
- **p. 8 / 7 EXPERIMENTS - extractive body cue:** Point Mass-Maze Ant-Disabled GAN-GCL No -40.2 -44.8 GAN-GCL Yes -41.8 -43.4 AIRL (ours) No -31.2 -41.4 AIRL (ours) Yes -8.82 130.3 GAIL, policy transfer N/A ...
- **p. 6 / 7 EXPERIMENTS - extractive body cue:** In this way, we simulate a scenario where we wish to use RL to solve a task but wish to refrain from manual reward engineering ...
- **p. 7 / 7 EXPERIMENTS - extractive body cue:** In each task, a reward is learned via IRL on the training environment, and the reward is used to reoptimize a new policy on a ...
- **p. 7 / 7 EXPERIMENTS - extractive body cue:** GAN-GCL can presumably learn disentangled rewards, but we find that the trajectorycentric formulation does not perform well even in learning rewards in the original task, ...
- **p. 8 / 7 EXPERIMENTS - extractive body cue:** Numerical results are presented in Table 2.These experiments do not test transfer, and in a sense can be regarded as "testing on the training set," ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1: Results on transfer learning tasks. Mean scores (higher is better) are reported over 5 runs. We also include results for TRPO optimizing the ...
- **p. 6 / 7 EXPERIMENTS - extractive body cue:** 7.1 RECOVERING TRUE REWARDS IN TABULAR MDPS We first consider MaxEnt IRL in a toy task with randomly generated MDPs.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** demonstration으로 정의된 robot task distribution.
- **Input boundary:** observation history와 expert trajectory/action.
- **Output/decision under evaluation:** predicted action 또는 action chunk.
- **Primary target:** imitation error, task success, robustness와 compounding error.
- **Detected evaluation headings:** 7 EXPERIMENTS (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 7 EXPERIMENTS | EMPIRICAL / SIMULATION | We also show that in the transfer learning setup, under a new transition matrix T ′, the optimal policy under the state-only reward achieves ... | p. 6 (7 EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Fig. 4. In our second task, we modify the agent itself. We train a quadrupedal "ant" agent to run forwards, and at test time ... | p. 7 (Figure/Table caption) |
| 7 EXPERIMENTS | EMPIRICAL / SIMULATION | We find that AIRL performs on par with GAIL in a traditional imitation learning setup while vastly outperforming it in transfer learning setups, and ... | p. 6 (7 EXPERIMENTS) |
| 7 EXPERIMENTS | EMPIRICAL / SIMULATION | We also include results for TRPO optimizing the ground truth reward, and the performance of a policy learned via GAIL on the training environment. | p. 8 (7 EXPERIMENTS) |
| 7 EXPERIMENTS | EMPIRICAL / SIMULATION | Numerical results for these environment transfer experiments are given in Table 1. | p. 7 (7 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 6 / 7 EXPERIMENTS - extractive body cue:** (2016a), which we refer to as GAN-GCL, on standard benchmark tasks that do not evaluate transfer.
- **p. 8 / 7 EXPERIMENTS - extractive body cue:** Point Mass-Maze Ant-Disabled GAN-GCL No -40.2 -44.8 GAN-GCL Yes -41.8 -43.4 AIRL (ours) No -31.2 -41.4 AIRL (ours) Yes -8.82 130.3 GAIL, policy transfer N/A ...
- **p. 6 / 7 EXPERIMENTS - extractive body cue:** In this way, we simulate a scenario where we wish to use RL to solve a task but wish to refrain from manual reward engineering ...
- **p. 7 / 7 EXPERIMENTS - extractive body cue:** In each task, a reward is learned via IRL on the training environment, and the reward is used to reoptimize a new policy on a ...
- **p. 7 / 7 EXPERIMENTS - extractive body cue:** GAN-GCL can presumably learn disentangled rewards, but we find that the trajectorycentric formulation does not perform well even in learning rewards in the original task, ...
- **p. 8 / 7 EXPERIMENTS - extractive body cue:** Numerical results are presented in Table 2.These experiments do not test transfer, and in a sense can be regarded as "testing on the training set," ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 7 / Figure/Table caption - extractive body cue:** Figure 1: Ground truth (a) and learned rewards (b, c) on the random MDP task. Dark blue corresponds to a reward of 1, and white ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 2: Learning curve for the transfer learning experiment on tabular MDPs. Value iteration steps are plot- ted on the x-axis, against returns for the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 4. In our second task, we modify the agent itself. We train a quadrupedal "ant" agent to run forwards, and at test time we ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 3: Illustration of the shifting maze task, where the agent (blue) must reach the goal (green). During training the agent must go around the ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: Reward learned on the point mass shifting maze task. The goal is located at the green star and the agent starts at the ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Top row: An ant running forwards (right in the picture) in the training environment. Bottom row: Behavior acquired by optimizing a state-only reward ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1: Results on transfer learning tasks. Mean scores (higher is better) are reported over 5 runs. We also include results for TRPO optimizing the ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 2: Results on imitation learning benchmark tasks. Mean scores (higher is better) are reported across 5 runs. Pendulum Ant Swimmer Half-Cheetah GAN-GCL -261.5

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | (2016a), which we refer to as GAN-GCL, on standard benchmark tasks that do not evaluate transfer. | embodiment, simulator version and control stack | p. 6 (7 EXPERIMENTS), p. 8 (7 EXPERIMENTS) |
| Task/environment | Point Mass-Maze Ant-Disabled GAN-GCL No -40.2 -44.8 GAN-GCL Yes -41.8 -43.4 AIRL (ours) No -31.2 -41.4 AIRL (ours) Yes -8.82 130.3 GAIL, policy transfer ... | reset, timeout, object/scene variation | p. 8 (7 EXPERIMENTS), p. 6 (7 EXPERIMENTS) |
| Observation/sensor | observation history와 expert trajectory/action | calibration, preprocessing, privileged input | p. 3 (3 BACKGROUND), p. 3 (3 BACKGROUND) |
| Output/decision | predicted action 또는 action chunk | action frame, controller and termination | p. 5 (3 BACKGROUND), p. 4 (3 BACKGROUND) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 1: Results on transfer learning tasks. Mean scores (higher is better) are reported over 5 runs. We also include results for TRPO optimizing ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| 7.1 RECOVERING TRUE REWARDS IN TABULAR MDPS We first consider MaxEnt IRL in a toy task with randomly generated MDPs. | definition/direction/unit from same section | p. 6 (7 EXPERIMENTS) |
| We also show that in the transfer learning setup, under a new transition matrix T ′, the optimal policy under the state-only reward achieves ... | definition/direction/unit from same section | p. 6 (7 EXPERIMENTS) |
| We have demonstrated that AIRL can learn disentangled rewards that can accommodate significant domain shift even in high-dimensional environments where it is difficult to ... | definition/direction/unit from same section | p. 7 (7 EXPERIMENTS) |
| Dark blue corresponds to a reward of 1, and white corresponds to 0. | definition/direction/unit from same section | p. 7 (7 EXPERIMENTS) |
| Note that there is little reward shaping, which enables the reward to transfer well. | definition/direction/unit from same section | p. 8 (7 EXPERIMENTS) |
| Table 2: Results on imitation learning benchmark tasks. Mean scores (higher is better) are reported across 5 runs. Pendulum Ant Swimmer Half-Cheetah GAN-GCL -261.5 | definition/direction/unit from same section | p. 9 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We find that AIRL performs on par with GAIL in a traditional imitation learning setup while vastly outperforming it in transfer learning setups, and ... | comparison identity and matched condition | p. 6 (7 EXPERIMENTS) |
| We also include results for directly transferring the policy learned with GAIL, and an oracle result that involves optimizing the ground truth reward function ... | comparison identity and matched condition | p. 7 (7 EXPERIMENTS) |
| Numerical results are presented in Table 2.These experiments do not test transfer, and in a sense can be regarded as "testing on the training ... | comparison identity and matched condition | p. 8 (7 EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| no ablation sentence selected | not reported; proposed stress test only | verify ablation section |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper, we propose adversarial inverse reinforcement learning (AIRL), an inverse reinforcement learning algorithm based on adversarial learning. | We also show that in the transfer learning setup, under a new transition matrix T ′, the optimal policy under the state-only reward achieves ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (7 EXPERIMENTS), p. 7 (Figure/Table caption), p. 6 (7 EXPERIMENTS), p. 8 (7 EXPERIMENTS), p. 7 (7 EXPERIMENTS), p. 8 (7 EXPERIMENTS) |
| Primary metric/result | Fig. 4. In our second task, we modify the agent itself. We train a quadrupedal "ant" agent to run forwards, and at test time ... | numeric claim only at cited anchor | p. 7 (Figure/Table caption) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | 6 LEARNING DISENTANGLED REWARDS WITH AIRL In the method presented in Section 4, we cannot learn a state-only reward function, rθ(s), meaning that we ... | p. 5 (3 BACKGROUND) |
| body limitation/failure cue | At test time, the agent cannot simply mimic the actions learned during training, and instead must successfully infer that the goal in the maze ... | p. 7 (7 EXPERIMENTS) |
| body limitation/failure cue | However, we leave this direction to future work. | p. 4 (3 BACKGROUND) |
| body limitation/failure cue | (2016a) does not implement or evaluate GAN-GCL and, to our knowledge, we present the first empirical evaluation of this algorithm. | p. 6 (7 EXPERIMENTS) |
| body limitation/failure cue | We subtract a constant offset from all reward functions so that they share the same mean for visualization - this does not influence the ... | p. 6 (7 EXPERIMENTS) |
| body limitation/failure cue | GAIL learns successfully in the training domain, but does not acquire a representation that is suitable for transfer to test domains. | p. 7 (7 EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Value iteration steps are plotted on the x-axis, against returns for the policy on the y-axis. | p. 7 (7 EXPERIMENTS) |
| We train a quadrupedal "ant" agent to run forwards, and at test time we disable and shrink two of the front legs of the ... | p. 7 (7 EXPERIMENTS) |
| They operate in a trajectory-centric formulation, where the discriminator takes on a particular form (fθ(τ) is a learned function; π(τ) is precomputed and its ... | p. 3 (3 BACKGROUND) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / 3 BACKGROUND - extractive body cue:** 6 LEARNING DISENTANGLED REWARDS WITH AIRL In the method presented in Section 4, we cannot learn a state-only reward function, rθ(s), meaning that we cannot ...
- **p. 7 / 7 EXPERIMENTS - extractive body cue:** At test time, the agent cannot simply mimic the actions learned during training, and instead must successfully infer that the goal in the maze is ...
- **p. 4 / 3 BACKGROUND - extractive body cue:** However, we leave this direction to future work.
- **p. 6 / 7 EXPERIMENTS - extractive body cue:** (2016a) does not implement or evaluate GAN-GCL and, to our knowledge, we present the first empirical evaluation of this algorithm.
- **p. 6 / 7 EXPERIMENTS - extractive body cue:** We subtract a constant offset from all reward functions so that they share the same mean for visualization - this does not influence the optimal ...
- **p. 7 / 7 EXPERIMENTS - extractive body cue:** GAIL learns successfully in the training domain, but does not acquire a representation that is suitable for transfer to test domains.

- **Evidence anchors reviewed:** datasets p. 6 (7 EXPERIMENTS), p. 8 (7 EXPERIMENTS), p. 6 (7 EXPERIMENTS), p. 7 (7 EXPERIMENTS), p. 7 (7 EXPERIMENTS), p. 8 (7 EXPERIMENTS), metrics p. 8 (Figure/Table caption), p. 6 (7 EXPERIMENTS), p. 6 (7 EXPERIMENTS), p. 7 (7 EXPERIMENTS), p. 7 (7 EXPERIMENTS), p. 8 (7 EXPERIMENTS), baselines p. 6 (7 EXPERIMENTS), p. 7 (7 EXPERIMENTS), p. 8 (7 EXPERIMENTS), results p. 6 (7 EXPERIMENTS), p. 7 (Figure/Table caption), p. 6 (7 EXPERIMENTS), p. 8 (7 EXPERIMENTS), p. 7 (7 EXPERIMENTS), p. 8 (7 EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
