# Evaluation - Maximum a Posteriori Policy Optimisation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=S1ANxQW0b; PDF retrieval source: https://openreview.net/forum?id=S1ANxQW0b. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 18 (Figure/Table caption)): This difference is so extreme that in several instances the PPO baseline converges an order of magnitude slower than the off-policy algorithms and we thus indicate the asymptotic performance of ...

## Evaluation Body Digest

- **p. 7 / 5 EXPERIMENTS - extractive body cue:** For example, the classical cart-pole and acrobot dynamical systems, 2D and Humanoid walking as well as simple low-dimensional planar reaching and manipulation tasks.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** The reward in the Acrobot task is the distance of the robots end-effector to an upright position of the underactuated system.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** Published as a conference paper at ICLR 2018 5.1.1 DETAILED ANALYSIS ON WALKER-2D, ACROBOT, HOPPER We start by looking at the results for the classical ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** The single learner vanilla DDPG implementation learns the lower dimensional environments quickly but suffers in terms of learning speed in environments with sparse rewards (finger, ...
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** Top: Acrobot, Ball-in-cup, Cart-pole, Cheetah, Finger, Fish, Hopper.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** Overall, MPO is able to solve all environments using surprisingly moderate amounts of data.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** All tasks have rewards that are scaled to be between 0 and 1000.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** 0.0 0.2 0.4 0.6 0.8 1.0 1.2 1.4 training_steps 1e7 0 200 400 600 800 1000 mean_return task_name=run, domain_name=humanoid agent=DDPG agent=EPG + retrace + entropy ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** robot/environment의 sequential decision process.
- **Input boundary:** state 또는 observation, action, reward와 transition history.
- **Output/decision under evaluation:** action policy와 induced trajectory.
- **Primary target:** expected return, task success, stability와 sample efficiency.
- **Detected evaluation headings:** 5 EXPERIMENTS (p. 7); C EXPERIMENT DETAILS (p. 18).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | This difference is so extreme that in several instances the PPO baseline converges an order of magnitude slower than the off-policy algorithms and we ... | p. 9 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | For the Humanoid running domain we can observe a similar trend to the experiments from the previous section: MPO quickly finds a stable running ... | p. 9 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Furthermore, we can observe that changing from the non-parametric variational distribution to a parametric distribution3 (which, as described above, can be related to PPO) ... | p. 8 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | While we include plots depicting the performance of our algorithm on all tasks below; comparing it against the state-of-the-art algorithms in terms of data-efficiency. | p. 7 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | We plot the median performance over 10 experiments with different random seeds. | p. 8 (5 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 7 / 5 EXPERIMENTS - extractive body cue:** For example, the classical cart-pole and acrobot dynamical systems, 2D and Humanoid walking as well as simple low-dimensional planar reaching and manipulation tasks.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** The reward in the Acrobot task is the distance of the robots end-effector to an upright position of the underactuated system.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** Published as a conference paper at ICLR 2018 5.1.1 DETAILED ANALYSIS ON WALKER-2D, ACROBOT, HOPPER We start by looking at the results for the classical ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** The single learner vanilla DDPG implementation learns the lower dimensional environments quickly but suffers in terms of learning speed in environments with sparse rewards (finger, ...
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** Top: Acrobot, Ball-in-cup, Cart-pole, Cheetah, Finger, Fish, Hopper.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** Overall, MPO is able to solve all environments using surprisingly moderate amounts of data.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 7 / Figure/Table caption - extractive body cue:** Figure 1: Control Suite domains used for benchmarking. Top: Acrobot, Ball-in-cup, Cart-pole, Cheetah, Finger, Fish, Hopper. Bottom: Humanoid, Manipulator, Pendulum, Point-mass, Reacher, Swimmers (6 and ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 2: Ablation study of the MPO algorithm and comparison to common baselines from the liter- ature on three domains from the control suite. We ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 3: MPO on high-dimensional control problems (Parkour Walker2D and Humanoid walking from control suite). 0.0 0.2 0.4 0.6 0.8 1.0
- **p. 11 / Figure/Table caption - extractive body cue:** Figure 4: Complete comparison of results for the control suite. We plot the median performance over 10 random seeds together with 5 and 95 % ...
- **p. 18 / Figure/Table caption - extractive body cue:** Table 1: Results on a subset of the ALE environments in comparison to baselines taken from (Belle- mare et al., 2017) Game/Agent Human DQN Prior. ...
- **p. 18 / Figure/Table caption - extractive body cue:** Table 2: Parameters for non-parametric variational distribution Hyperparameters for MPO with parametric variational distribution were as follows, 18
- **p. 19 / Figure/Table caption - extractive body cue:** Table 3: Parameters for parametric variational distribution D DERIVATION OF UPDATE RULES FOR A GAUSSIAN POLICY For continuous control we assume that the policy is ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For example, the classical cart-pole and acrobot dynamical systems, 2D and Humanoid walking as well as simple low-dimensional planar reaching and manipulation tasks. | embodiment, simulator version and control stack | p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |
| Task/environment | The reward in the Acrobot task is the distance of the robots end-effector to an upright position of the underactuated system. | reset, timeout, object/scene variation | p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |
| Observation/sensor | state 또는 observation, action, reward와 transition history | calibration, preprocessing, privileged input | p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT) |
| Output/decision | action policy와 induced trajectory | action frame, controller and termination | p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The reward in the Acrobot task is the distance of the robots end-effector to an upright position of the underactuated system. | definition/direction/unit from same section | p. 8 (5 EXPERIMENTS) |
| All tasks have rewards that are scaled to be between 0 and 1000. | definition/direction/unit from same section | p. 8 (5 EXPERIMENTS) |
| The single learner vanilla DDPG implementation learns the lower dimensional environments quickly but suffers in terms of learning speed in environments with sparse rewards ... | definition/direction/unit from same section | p. 9 (5 EXPERIMENTS) |
| 0.0 0.2 0.4 0.6 0.8 1.0 1.2 1.4 training_steps 1e7 0 200 400 600 800 1000 mean_return task_name=run, domain_name=humanoid agent=DDPG agent=EPG + retrace + ... | definition/direction/unit from same section | p. 9 (5 EXPERIMENTS) |
| In both cases we use a Gaussian distribution for the policy whose mean and covariance are parameterized by a neural network (see appendix for ... | definition/direction/unit from same section | p. 7 (5 EXPERIMENTS) |
| While we include plots depicting the performance of our algorithm on all tasks below; comparing it against the state-of-the-art algorithms in terms of data-efficiency. | definition/direction/unit from same section | p. 7 (5 EXPERIMENTS) |
| Figure 4: Complete comparison of results for the control suite. We plot the median performance over 10 random seeds together with 5 and 95 ... | definition/direction/unit from same section | p. 11 (Figure/Table caption) |
| Table 3: Parameters for parametric variational distribution D DERIVATION OF UPDATE RULES FOR A GAUSSIAN POLICY For continuous control we assume that the policy ... | definition/direction/unit from same section | p. 19 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 2: Ablation study of the MPO algorithm and comparison to common baselines from the liter- ature on three domains from the control suite. ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| We note that in order to ensure a fair comparison all algorithms ran with exactly the same network configuration, used a single learner (no ... | comparison identity and matched condition | p. 8 (5 EXPERIMENTS) |
| This difference is so extreme that in several instances the PPO baseline converges an order of magnitude slower than the off-policy algorithms and we ... | comparison identity and matched condition | p. 9 (5 EXPERIMENTS) |
| While we include plots depicting the performance of our algorithm on all tasks below; comparing it against the state-of-the-art algorithms in terms of data-efficiency. | comparison identity and matched condition | p. 7 (5 EXPERIMENTS) |
| From the plot a few trends are readily apparent: i) We can clearly observe the advantage in terms of data-efficiency that methods relying on ... | comparison identity and matched condition | p. 9 (5 EXPERIMENTS) |
| Table 1: Results on a subset of the ALE environments in comparison to baselines taken from (Belle- mare et al., 2017) Game/Agent Human DQN ... | comparison identity and matched condition | p. 18 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Finally using only a single sample to estimate the integral (and hence the likelihood ratio gradient) results in an actor-critic variant with Retrace that ... | component/input/data sensitivity | p. 8 (5 EXPERIMENTS) |
| To make computation time bearable in these more complicated domains we utilize a parallel variant of our algorithm: in this implementation K learners are ... | component/input/data sensitivity | p. 9 (5 EXPERIMENTS) |
| This difference is so extreme that in several instances the PPO baseline converges an order of magnitude slower than the off-policy algorithms and we ... | component/input/data sensitivity | p. 9 (5 EXPERIMENTS) |
| Figure 2: Ablation study of the MPO algorithm and comparison to common baselines from the liter- ature on three domains from the control suite. ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper we propose a novel off-policy algorithm that benefits from the best properties of both classes. | This difference is so extreme that in several instances the PPO baseline converges an order of magnitude slower than the off-policy algorithms and we ... | PDF body cue; verify exact table/figure and matched conditions | p. 9 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 18 (Figure/Table caption) |
| Primary metric/result | For the Humanoid running domain we can observe a similar trend to the experiments from the previous section: MPO quickly finds a stable running ... | numeric claim only at cited anchor | p. 9 (5 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** The suite of continuous control tasks that we are evaluating against contains 18 tasks, comprising a wide range of domains including well known tasks from ...
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** Published as a conference paper at ICLR 2018 5.1.1 DETAILED ANALYSIS ON WALKER-2D, ACROBOT, HOPPER We start by looking at the results for the classical ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** On average less than 1000 trajectories (or 106 samples) are needed to reach the best performance.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** In addition to the walker experiment we have also evaluated MPO on the Parkour domain using a humanoid body (with 22 degrees of freedom) which ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | 0.0 0.2 0.4 0.6 0.8 1.0 1.2 1.4 training_steps 1e7 0 200 400 600 800 1000 mean_return task_name=run, domain_name=humanoid agent=DDPG agent=EPG + retrace + ... | p. 9 (5 EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| 0.0 0.2 0.4 0.6 0.8 1.0 1.2 1.4 training_steps 1e7 0 200 400 600 800 1000 mean_return task_name=run, domain_name=humanoid agent=DDPG agent=EPG + retrace + ... | p. 9 (5 EXPERIMENTS) |
| We plot the median performance over 10 experiments with different random seeds. | p. 8 (5 EXPERIMENTS) |
| The hyperparameters for MPO were kept fixed for all experiments in the paper (see the appendix for hyperparameter settings). | p. 8 (5 EXPERIMENTS) |
| We refer to the appendix for a complete description of the hyperparameters. | p. 9 (5 EXPERIMENTS) |
| It exhibits the scalability, robustness and hyperparameter insensitivity of on-policy algorithms, while offering the data-efficiency of off-policy, value-based methods. | p. 1 (1 INTRODUCTION) |
| In particular, for continuous control, our method outperforms existing methods with respect to sample efficiency, premature convergence and robustness to hyperparameter settings. | p. 1 (ABSTRACT) |
| All experiments used the same optimisation hyperparameters 1. | p. 2 (1 INTRODUCTION) |
| By using this estimation objective we have more control over the policy change in both E and M steps, yielding robust learning. | p. 2 (1 INTRODUCTION) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 5 EXPERIMENTS - extractive body cue:** 0.0 0.2 0.4 0.6 0.8 1.0 1.2 1.4 training_steps 1e7 0 200 400 600 800 1000 mean_return task_name=run, domain_name=humanoid agent=DDPG agent=EPG + retrace + entropy ...

- **PDF anchors reviewed:** datasets p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), metrics p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), baselines p. 8 (Figure/Table caption), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 18 (Figure/Table caption), results p. 9 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 18 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
