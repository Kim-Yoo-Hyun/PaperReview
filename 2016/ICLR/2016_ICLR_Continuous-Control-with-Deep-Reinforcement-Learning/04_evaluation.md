# Evaluation - Continuous Control with Deep Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1509.02971; PDF retrieval source: https://arxiv.org/pdf/1509.02971. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 5 (4 RESULTS), p. 5 (4 RESULTS), p. 6 (4 RESULTS), p. 6 (4 RESULTS)): Table 1: Performance after training across all environments for at most 2.5 million steps. We report both the average and best observed (across 5 runs). All scores, except Torcs, are ...

## Evaluation Body Digest

- **p. 6 / 4 RESULTS - extractive body cue:** We examined DDPG's estimates empirically by comparing the values estimated by Q after training with the true returns seen on test episodes.
- **p. 5 / 4 RESULTS - extractive body cue:** In all tasks, we ran experiments using both a low-dimensional state description (such as joint angles and positions) and high-dimensional renderings of the environment.
- **p. 6 / 4 RESULTS - extractive body cue:** In order from the left: the cartpole swing-up task, a reaching task, a gasp and move task, a puck-hitting task, a monoped balancing task, two ...
- **p. 4 / 4 RESULTS - extractive body cue:** This included classic reinforcement learning environments such as cartpole, as well as difficult, 4
- **p. 4 / 4 RESULTS - extractive body cue:** We constructed simulated physical environments of varying levels of difficulty to test our algorithm.
- **p. 5 / 4 RESULTS - extractive body cue:** These environments were simulated using MuJoCo (Todorov et al., 2012).
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Performance after training across all environments for at most 2.5 million steps. We report both the average and best observed (across 5 runs). ...
- **p. 6 / 4 RESULTS - extractive body cue:** Cart Pendulum Swing-up Cartpole Swing-up Fixed Reacher Blockworld Gripper Puck Shooting Monoped Balancing Moving Gripper Cheetah Million Steps 0 1 1 0 1 1 0 ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** robot/environment의 sequential decision process.
- **Input boundary:** state 또는 observation, action, reward와 transition history.
- **Output/decision under evaluation:** action policy와 induced trajectory.
- **Primary target:** expected return, task success, stability와 sample efficiency.
- **Detected evaluation headings:** 4 RESULTS (p. 4).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SIMULATION | Table 1: Performance after training across all environments for at most 2.5 million steps. We report both the average and best observed (across 5 ... | p. 7 (Figure/Table caption) |
| 4 RESULTS | EMPIRICAL / SIMULATION | We normalized the scores using two baselines. | p. 5 (4 RESULTS) |
| 4 RESULTS | EMPIRICAL / SIMULATION | We also report results with components of our algorithm (i.e. the target network or batch normalization) removed. | p. 5 (4 RESULTS) |
| 4 RESULTS | EMPIRICAL / SIMULATION | We normalize scores so that the naive policy has a mean score of 0 and iLQG has a mean score of 1. | p. 6 (4 RESULTS) |
| 4 RESULTS | EMPIRICAL / SIMULATION | Cart Pendulum Swing-up Cartpole Swing-up Fixed Reacher Blockworld Gripper Puck Shooting Monoped Balancing Moving Gripper Cheetah Million Steps 0 1 1 0 1 1 ... | p. 6 (4 RESULTS) |

## Dataset / Benchmark Role

- **p. 6 / 4 RESULTS - extractive body cue:** We examined DDPG's estimates empirically by comparing the values estimated by Q after training with the true returns seen on test episodes.
- **p. 5 / 4 RESULTS - extractive body cue:** In all tasks, we ran experiments using both a low-dimensional state description (such as joint angles and positions) and high-dimensional renderings of the environment.
- **p. 6 / 4 RESULTS - extractive body cue:** In order from the left: the cartpole swing-up task, a reaching task, a gasp and move task, a puck-hitting task, a monoped balancing task, two ...
- **p. 4 / 4 RESULTS - extractive body cue:** This included classic reinforcement learning environments such as cartpole, as well as difficult, 4
- **p. 4 / 4 RESULTS - extractive body cue:** We constructed simulated physical environments of varying levels of difficulty to test our algorithm.
- **p. 5 / 4 RESULTS - extractive body cue:** These environments were simulated using MuJoCo (Todorov et al., 2012).

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 6 / Figure/Table caption - extractive body cue:** Figure 1: Example screenshots of a sample of environments we attempt to solve with DDPG. In order from the left: the cartpole swing-up task, a ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 2: Performance curves for a selection of domains using variants of DPG: original DPG algorithm (minibatch NFQCA) with batch normalization (light grey), with target ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3: Density plot showing estimated Q values versus observed returns sampled from test episodes on 5 replicas. In simple domains such as pendulum and ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Performance after training across all environments for at most 2.5 million steps. We report both the average and best observed (across 5 runs). ...
- **p. 12 / Figure/Table caption - extractive body cue:** Table 2: Dimensionality of the MuJoCo tasks: the dimensionality of the underlying physics model dim(s), number of action dimensions dim(a) and observation dimensions dim(o). task ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We examined DDPG's estimates empirically by comparing the values estimated by Q after training with the true returns seen on test episodes. | embodiment, simulator version and control stack | p. 6 (4 RESULTS), p. 5 (4 RESULTS) |
| Task/environment | In all tasks, we ran experiments using both a low-dimensional state description (such as joint angles and positions) and high-dimensional renderings of the environment. | reset, timeout, object/scene variation | p. 5 (4 RESULTS), p. 6 (4 RESULTS) |
| Observation/sensor | state 또는 observation, action, reward와 transition history | calibration, preprocessing, privileged input | p. 2 (1 INTRODUCTION), p. 2 (2 BACKGROUND) |
| Output/decision | action policy와 induced trajectory | action frame, controller and termination | p. 3 (2 BACKGROUND), p. 4 (2 BACKGROUND) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 1: Performance after training across all environments for at most 2.5 million steps. We report both the average and best observed (across 5 ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Cart Pendulum Swing-up Cartpole Swing-up Fixed Reacher Blockworld Gripper Puck Shooting Monoped Balancing Moving Gripper Cheetah Million Steps 0 1 1 0 1 1 ... | definition/direction/unit from same section | p. 6 (4 RESULTS) |
| We normalized the scores using two baselines. | definition/direction/unit from same section | p. 5 (4 RESULTS) |
| We normalize scores so that the naive policy has a mean score of 0 and iLQG has a mean score of 1. | definition/direction/unit from same section | p. 6 (4 RESULTS) |
| The first baseline is the mean return from a naive policy which samples actions from a uniform distribution over the valid action space. | definition/direction/unit from same section | p. 5 (4 RESULTS) |
| Figure 3: Density plot showing estimated Q values versus observed returns sampled from test episodes on 5 replicas. In simple domains such as pendulum ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We normalized the scores using two baselines. | comparison identity and matched condition | p. 5 (4 RESULTS) |
| The second baseline is iLQG (Todorov & Li, 2005), a planning based solver with full access to the 5 | comparison identity and matched condition | p. 5 (4 RESULTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We also report results with components of our algorithm (i.e. the target network or batch normalization) removed. | component/input/data sensitivity | p. 5 (4 RESULTS) |
| We evaluated the policy periodically during training by testing it without exploration noise. | component/input/data sensitivity | p. 5 (4 RESULTS) |
| Figure 2: Performance curves for a selection of domains using variants of DPG: original DPG algorithm (minibatch NFQCA) with batch normalization (light grey), with ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this work we present a model-free, off-policy actor-critic algorithm using deep function approximators that can learn policies in high-dimensional, continuous action spaces. | Table 1: Performance after training across all environments for at most 2.5 million steps. We report both the average and best observed (across 5 ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 5 (4 RESULTS), p. 5 (4 RESULTS), p. 6 (4 RESULTS), p. 6 (4 RESULTS) |
| Primary metric/result | We normalized the scores using two baselines. | numeric claim only at cited anchor | p. 5 (4 RESULTS) |

- Numeric sentences retained from the body:
- **p. 1 / 1 INTRODUCTION - extractive body cue:** For example, a 7 degree of freedom system (as in the human arm) with the coarsest discretization ai ∈{-k, 0, k} for each joint leads ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Table 2: Dimensionality of the MuJoCo tasks: the dimensionality of the underlying physics model dim(s), number of action dimensions dim(a) and observation dimensions dim(o). ... | p. 12 (Figure/Table caption) |
| body limitation/failure cue | The work combines insights from recent advances in deep learning and reinforcement learning, resulting in an algorithm that robustly solves challenging problems across a ... | p. 8 (6 CONCLUSION) |
| body limitation/failure cue | We evaluated the policy periodically during training by testing it without exploration noise. | p. 5 (4 RESULTS) |
| body limitation/failure cue | We used an identical network architecture and learning algorithm hyper-parameters to the physics tasks but altered the noise process for exploration because of the ... | p. 6 (4 RESULTS) |
| body limitation/failure cue | On both low-dimensional and from pixels, some replicas were able to learn reasonable policies that are able to complete a circuit around the track ... | p. 6 (4 RESULTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We consider a standard reinforcement learning setup consisting of an agent interacting with an environment E in discrete timesteps. | p. 2 (2 BACKGROUND) |
| In many cases, we are also able to learn good policies directly from pixels, again keeping hyperparameters and network structure constant 1. | p. 2 (1 INTRODUCTION) |
| We employ these in the context of DDPG and explain their implementation in the next section. | p. 3 (2 BACKGROUND) |
| 2In practice, as in commonly done in policy gradient implementations, we ignored the discount in the statevisitation distribution ρβ. | p. 3 (2 BACKGROUND) |
| Additionally, to make efficient use of hardware optimizations, it is essential to learn in minibatches, rather than online. | p. 4 (2 BACKGROUND) |
| See supplementary information for details of our network structure and hyperparameters. | p. 5 (4 RESULTS) |
| For each timestep of the agent, we step the simulation 3 timesteps, repeating the agent's action and rendering each time. | p. 5 (4 RESULTS) |
| Cart Pendulum Swing-up Cartpole Swing-up Fixed Reacher Blockworld Gripper Puck Shooting Monoped Balancing Moving Gripper Cheetah Million Steps 0 1 1 0 1 1 ... | p. 6 (4 RESULTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 12 / Figure/Table caption - extractive body cue:** Table 2: Dimensionality of the MuJoCo tasks: the dimensionality of the underlying physics model dim(s), number of action dimensions dim(a) and observation dimensions dim(o). task ...
- **p. 8 / 6 CONCLUSION - extractive body cue:** The work combines insights from recent advances in deep learning and reinforcement learning, resulting in an algorithm that robustly solves challenging problems across a variety ...
- **p. 5 / 4 RESULTS - extractive body cue:** We evaluated the policy periodically during training by testing it without exploration noise.
- **p. 6 / 4 RESULTS - extractive body cue:** We used an identical network architecture and learning algorithm hyper-parameters to the physics tasks but altered the noise process for exploration because of the very ...
- **p. 6 / 4 RESULTS - extractive body cue:** On both low-dimensional and from pixels, some replicas were able to learn reasonable policies that are able to complete a circuit around the track though ...

- **PDF anchors reviewed:** datasets p. 6 (4 RESULTS), p. 5 (4 RESULTS), p. 6 (4 RESULTS), p. 4 (4 RESULTS), p. 4 (4 RESULTS), p. 5 (4 RESULTS), metrics p. 7 (Figure/Table caption), p. 6 (4 RESULTS), p. 5 (4 RESULTS), p. 6 (4 RESULTS), p. 5 (4 RESULTS), p. 7 (Figure/Table caption), baselines p. 5 (4 RESULTS), p. 5 (4 RESULTS), results p. 7 (Figure/Table caption), p. 5 (4 RESULTS), p. 5 (4 RESULTS), p. 6 (4 RESULTS), p. 6 (4 RESULTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
