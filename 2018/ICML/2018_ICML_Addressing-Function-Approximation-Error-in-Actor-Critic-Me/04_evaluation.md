# Evaluation - Addressing Function Approximation Error in Actor-Critic Methods

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1802.09477; PDF retrieval source: https://arxiv.org/pdf/1802.09477. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (6.2. Ablation Studies), p. 8 (6.1. Evaluation), p. 6 (6. Experiments), p. 7 (6.1. Evaluation), p. 7 (6.1. Evaluation)): Method HCheetah Hopper Walker2d Ant TD3 9532.99 3304.75 4565.24 4185.06 DDPG 3162.50 1731.94 1520.90 816.35 AHE 8401.02 1061.77 2362.13 564.07 AHE + DP 7588.64 1465.11 2459.53 896.13 AHE + TPS ...

## Evaluation Body Digest

- **p. 8 / 6.1. Evaluation - extractive body cue:** Addressing Function Approximation Error in Actor-Critic Methods average reward over 10 episodes with no exploration noise.
- **p. 7 / 6.1. Evaluation - extractive body cue:** (2016) with no modifications to the environment or reward.
- **p. 7 / 6. Experiments - extractive body cue:** Learning curves for the OpenAI gym continuous control tasks.
- **p. 8 / 6.2. Ablation Studies - extractive body cue:** Maximum value for each task is bolded.
- **p. 6 / 6. Experiments - extractive body cue:** We present the Twin Delayed Deep Deterministic policy gradient algorithm (TD3), which builds on the Deep Deterministic Policy Gradient algorithm (DDPG) (Lillicrap et al., 2015) ...
- **p. 7 / 6. Experiments - extractive body cue:** Addressing Function Approximation Error in Actor-Critic Methods 0.0 0.2 0.4 0.6 0.8 1.0 Time steps (1e6) 0 2000 4000 6000 8000 10000 Average Return TD3 ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Average estimated value of a randomly selected state on Hopper-v1 without target networks, (τ = 1), and with slow- updating target networks, (τ ...
- **p. 8 / 6.1. Evaluation - extractive body cue:** TD3 matches or outperforms all other algorithms in both final performance and learning speed across all tasks.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** robot/environment의 sequential decision process.
- **Input boundary:** state 또는 observation, action, reward와 transition history.
- **Output/decision under evaluation:** action policy와 induced trajectory.
- **Primary target:** expected return, task success, stability와 sample efficiency.
- **Detected evaluation headings:** 6. Experiments (p. 6); 6.1. Evaluation (p. 7); C. Convergence results for single-step on-policy (p. 10).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 6.2. Ablation Studies | EMPIRICAL / SOURCE-REPORTED EVALUATION | Method HCheetah Hopper Walker2d Ant TD3 9532.99 3304.75 4565.24 4185.06 DDPG 3162.50 1731.94 1520.90 816.35 AHE 8401.02 1061.77 2362.13 564.07 AHE + DP 7588.64 ... | p. 8 (6.2. Ablation Studies) |
| 6.1. Evaluation | EMPIRICAL / SOURCE-REPORTED EVALUATION | TD3 matches or outperforms all other algorithms in both final performance and learning speed across all tasks. | p. 8 (6.1. Evaluation) |
| 6. Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | We present the Twin Delayed Deep Deterministic policy gradient algorithm (TD3), which builds on the Deep Deterministic Policy Gradient algorithm (DDPG) (Lillicrap et al., ... | p. 6 (6. Experiments) |
| 6.1. Evaluation | EMPIRICAL / SOURCE-REPORTED EVALUATION | To evaluate our algorithm, we measure its performance on the suite of MuJoCo continuous control tasks (Todorov et al., 2012), interfaced through OpenAI Gym ... | p. 7 (6.1. Evaluation) |
| 6.1. Evaluation | EMPIRICAL / SOURCE-REPORTED EVALUATION | Unlike the original implementation of DDPG, we used uncorrelated noise for exploration as we found noise drawn from the Ornstein-Uhlenbeck (Uhlenbeck & Ornstein, 1930) ... | p. 7 (6.1. Evaluation) |

## Dataset / Benchmark Role

- **p. 8 / 6.1. Evaluation - extractive body cue:** Addressing Function Approximation Error in Actor-Critic Methods average reward over 10 episodes with no exploration noise.
- **p. 7 / 6.1. Evaluation - extractive body cue:** (2016) with no modifications to the environment or reward.
- **p. 7 / 6. Experiments - extractive body cue:** Learning curves for the OpenAI gym continuous control tasks.
- **p. 8 / 6.2. Ablation Studies - extractive body cue:** Maximum value for each task is bolded.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive body cue:** Figure 1. Measuring overestimation bias in the value estimates of DDPG and our proposed method, Clipped Double Q-learning (CDQ), on MuJoCo environments over 1 million ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Measuring overestimation bias in the value estimates of actor critic variants of Double DQN (DDQN-AC) and Double Q- learning (DQ-AC) on MuJoCo environments ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Average estimated value of a randomly selected state on Hopper-v1 without target networks, (τ = 1), and with slow- updating target networks, (τ ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4. Example MuJoCo environments (a) HalfCheetah-v1, (b) Hopper-v1, (c) Walker2d-v1, (d) Ant-v1.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. Learning curves for the OpenAI gym continuous control tasks. The shaded region represents half a standard deviation of the average evaluation over 10 ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Max Average Return over 10 trials of 1 million time steps. Maximum value for each task is bolded. ± corresponds to a single ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5. TD3 matches or outperforms all other algorithms in both final performance and learning speed across all tasks.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2. Average return over the last 10 evaluations over 10 trials of 1 million time steps, comparing ablation over delayed policy updates (DP), target ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Addressing Function Approximation Error in Actor-Critic Methods average reward over 10 episodes with no exploration noise. | embodiment, simulator version and control stack | p. 8 (6.1. Evaluation), p. 7 (6.1. Evaluation) |
| Task/environment | (2016) with no modifications to the environment or reward. | reset, timeout, object/scene variation | p. 7 (6.1. Evaluation), p. 7 (6. Experiments) |
| Observation/sensor | state 또는 observation, action, reward와 transition history | calibration, preprocessing, privileged input | p. 2 (3. Background), p. 6 (5.3. Target Policy Smoothing Regularization) |
| Output/decision | action policy와 induced trajectory | action frame, controller and termination | p. 6 (5.3. Target Policy Smoothing Regularization), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Addressing Function Approximation Error in Actor-Critic Methods average reward over 10 episodes with no exploration noise. | definition/direction/unit from same section | p. 8 (6.1. Evaluation) |
| We present the Twin Delayed Deep Deterministic policy gradient algorithm (TD3), which builds on the Deep Deterministic Policy Gradient algorithm (DDPG) (Lillicrap et al., ... | definition/direction/unit from same section | p. 6 (6. Experiments) |
| Addressing Function Approximation Error in Actor-Critic Methods 0.0 0.2 0.4 0.6 0.8 1.0 Time steps (1e6) 0 2000 4000 6000 8000 10000 Average Return ... | definition/direction/unit from same section | p. 7 (6. Experiments) |
| (2016) with no modifications to the environment or reward. | definition/direction/unit from same section | p. 7 (6.1. Evaluation) |
| Figure 3. Average estimated value of a randomly selected state on Hopper-v1 without target networks, (τ = 1), and with slow- updating target networks, ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| TD3 matches or outperforms all other algorithms in both final performance and learning speed across all tasks. | definition/direction/unit from same section | p. 8 (6.1. Evaluation) |
| Figure 2. Measuring overestimation bias in the value estimates of actor critic variants of Double DQN (DDQN-AC) and Double Q- learning (DQ-AC) on MuJoCo ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Table 3. A complete comparison of hyper-parameter choices between our DDPG and the OpenAI baselines implementation (Dhariwal et al., 2017). Hyper-parameter Ours DDPG Critic ... | definition/direction/unit from same section | p. 13 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| A full comparison between our re-tuned version and the baselines DDPG is provided in the supplementary material. | comparison identity and matched condition | p. 8 (6.1. Evaluation) |
| The full algorithm outperforms every other combination in most tasks. | comparison identity and matched condition | p. 8 (6.2. Ablation Studies) |
| Table 3. A complete comparison of hyper-parameter choices between our DDPG and the OpenAI baselines implementation (Dhariwal et al., 2017). Hyper-parameter Ours DDPG Critic ... | comparison identity and matched condition | p. 13 (Figure/Table caption) |
| To allow for reproducible comparison, we use the original set of tasks from Brockman et al. | comparison identity and matched condition | p. 7 (6.1. Evaluation) |
| While a larger d would result in a larger benefit with respect to accumulating errors, for fair comparison, the critics are only trained once ... | comparison identity and matched condition | p. 7 (6.1. Evaluation) |
| Figure 3. Average estimated value of a randomly selected state on Hopper-v1 without target networks, (τ = 1), and with slow- updating target networks, ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We additionally compare the effectiveness of the actor-critic variants of Double Q-learning (Van Hasselt, 2010) and Double DQN (Van Hasselt et al., 2016), denoted ... | component/input/data sensitivity | p. 8 (6.2. Ablation Studies) |
| We perform ablation studies to understand the contribution of each individual component: Clipped Double Q-learning (Section 4.2), delayed policy updates (Section 5.2) and target ... | component/input/data sensitivity | p. 8 (6.2. Ablation Studies) |
| To remove the dependency on the initial parameters of the policy we use a purely exploratory policy for the first 10000 time steps of ... | component/input/data sensitivity | p. 7 (6.1. Evaluation) |
| Figure 2. Measuring overestimation bias in the value estimates of actor critic variants of Double DQN (DDQN-AC) and Double Q- learning (DQ-AC) on MuJoCo ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |
| Figure 3. Average estimated value of a randomly selected state on Hopper-v1 without target networks, (τ = 1), and with slow- updating target networks, ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |
| Figure 8. Comparison of TD3 and the Double Q-learning (DQ-AC) and Double DQN (DDQN-AC) actor-critic variants, which also leverage delayed policy updates and target ... | component/input/data sensitivity | p. 15 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Finally, we introduce a novel regularization strategy, where a SARSA-style update bootstraps similar action estimates to further reduce variance. | Method HCheetah Hopper Walker2d Ant TD3 9532.99 3304.75 4565.24 4185.06 DDPG 3162.50 1731.94 1520.90 816.35 AHE 8401.02 1061.77 2362.13 564.07 AHE + DP 7588.64 ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (6.2. Ablation Studies), p. 8 (6.1. Evaluation), p. 6 (6. Experiments), p. 7 (6.1. Evaluation), p. 7 (6.1. Evaluation) |
| Primary metric/result | TD3 matches or outperforms all other algorithms in both final performance and learning speed across all tasks. | numeric claim only at cited anchor | p. 8 (6.1. Evaluation) |

- Numeric sentences retained from the body:
- **p. 7 / 6. Experiments - extractive body cue:** The shaded region represents half a standard deviation of the average evaluation over 10 trials.
- **p. 7 / 6. Experiments - extractive body cue:** Max Average Return over 10 trials of 1 million time steps.
- **p. 7 / 6. Experiments - extractive body cue:** Environment TD3 DDPG Our DDPG PPO TRPO ACKTR SAC HalfCheetah 9636.95 ± 859.065 3305.60 8577.29 1795.43 -15.57 1450.46 2347.19 Hopper 3564.07 ± 114.74 2020.46 1860.02 ...
- **p. 8 / 6.1. Evaluation - extractive body cue:** Addressing Function Approximation Error in Actor-Critic Methods average reward over 10 episodes with no exploration noise.
- **p. 8 / 6.2. Ablation Studies - extractive body cue:** Average return over the last 10 evaluations over 10 trials of 1 million time steps, comparing ablation over delayed policy updates (DP), target policy smoothing ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Due to the connection between noise and overestimation, we examine the accumulation of errors from temporal difference learning. | p. 8 (7. Conclusion) |
| body limitation/failure cue | Afterwards, we use an off-policy exploration strategy, adding Gaussian noise N(0, 0.1) to each action. | p. 7 (6.1. Evaluation) |
| body limitation/failure cue | Unlike the original implementation of DDPG, we used uncorrelated noise for exploration as we found noise drawn from the Ornstein-Uhlenbeck (Uhlenbeck & Ornstein, 1930) ... | p. 7 (6.1. Evaluation) |
| body limitation/failure cue | Addressing Function Approximation Error in Actor-Critic Methods average reward over 10 episodes with no exploration noise. | p. 8 (6.1. Evaluation) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Max Average Return over 10 trials of 1 million time steps. | p. 7 (6. Experiments) |
| Each task is run for 1 million time steps with evaluations every 5000 time steps, where each evaluation reports the | p. 7 (6.1. Evaluation) |
| Although the actor is trained for only half the number of iterations, the inclusion of delayed policy update generally improves performance, while reducing training ... | p. 8 (6.2. Ablation Studies) |
| Our results are reported over 10 random seeds of the Gym simulator and the network initialization. | p. 8 (6.1. Evaluation) |
| As deep function approximators require multiple gradient updates to converge, target networks provide a stable objective in the learning 0.0 0.2 0.4 0.6 0.8 ... | p. 5 (5.2. Target Networks and Delayed Policy Updates) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 7. Conclusion - extractive body cue:** Due to the connection between noise and overestimation, we examine the accumulation of errors from temporal difference learning.
- **p. 7 / 6.1. Evaluation - extractive body cue:** Afterwards, we use an off-policy exploration strategy, adding Gaussian noise N(0, 0.1) to each action.
- **p. 7 / 6.1. Evaluation - extractive body cue:** Unlike the original implementation of DDPG, we used uncorrelated noise for exploration as we found noise drawn from the Ornstein-Uhlenbeck (Uhlenbeck & Ornstein, 1930) process ...
- **p. 8 / 6.1. Evaluation - extractive body cue:** Addressing Function Approximation Error in Actor-Critic Methods average reward over 10 episodes with no exploration noise.

- **Evidence anchors reviewed:** datasets p. 8 (6.1. Evaluation), p. 7 (6.1. Evaluation), p. 7 (6. Experiments), p. 8 (6.2. Ablation Studies), metrics p. 8 (6.1. Evaluation), p. 6 (6. Experiments), p. 7 (6. Experiments), p. 7 (6.1. Evaluation), p. 5 (Figure/Table caption), p. 8 (6.1. Evaluation), baselines p. 8 (6.1. Evaluation), p. 8 (6.2. Ablation Studies), p. 13 (Figure/Table caption), p. 7 (6.1. Evaluation), p. 7 (6.1. Evaluation), p. 5 (Figure/Table caption), results p. 8 (6.2. Ablation Studies), p. 8 (6.1. Evaluation), p. 6 (6. Experiments), p. 7 (6.1. Evaluation), p. 7 (6.1. Evaluation).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** While a larger d would result in a larger benefit with respect to accumulating errors, for fair comparison, the critics are only trained once per time step, and training the ... (p. 7, 6.1. Evaluation).
- **Metric evidence:** We present the Twin Delayed Deep Deterministic policy gradient algorithm (TD3), which builds on the Deep Deterministic Policy Gradient algorithm (DDPG) (Lillicrap et al., 2015) by applying the modifications described ... (p. 6, 6. Experiments).
- **Baseline/ablation evidence:** A full comparison between our re-tuned version and the baselines DDPG is provided in the supplementary material. (p. 8, 6.1. Evaluation).
- **Failure/negative evidence:** For transitions where the episode terminates by reaching some failure state, and not due to the episode running until the max horizon, the value of Q(s, ·) is set to ... (p. 14, 4. Q values are stored in a lookup table).
