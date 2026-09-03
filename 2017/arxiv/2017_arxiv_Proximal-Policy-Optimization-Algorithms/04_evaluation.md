# Evaluation - Proximal Policy Optimization Algorithms

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1707.06347; PDF retrieval source: https://arxiv.org/pdf/1707.06347. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (6 Experiments), p. 6 (6 Experiments), p. 6 (6 Experiments), p. 7 (6 Experiments), p. 8 (6 Experiments), p. 8 (6 Experiments)): We see that PPO outperforms the previous methods on almost all the continuous control environments.

## Evaluation Body Digest

- **p. 6 / 6 Experiments - extractive body cue:** Namely, we used 7 simulated robotics tasks2 implemented in OpenAI Gym [Bro+16], which use the MuJoCo [TET12] physics engine.
- **p. 7 / 6 Experiments - extractive body cue:** The three tasks we test on are (1) RoboschoolHumanoid: forward locomotion only, (2) RoboschoolHumanoidFlagrun: position of target is randomly varied every 200 timesteps or whenever ...
- **p. 8 / 6 Experiments - extractive body cue:** 6.4 Comparison to Other Algorithms on the Atari Domain We also ran PPO on the Arcade Learning Environment [Bel+15] benchmark and compared against well-tuned implementations ...
- **p. 6 / 6 Experiments - extractive body cue:** 0.69 Table 1: Results from continuous control benchmark.
- **p. 7 / 6 Experiments - extractive body cue:** [Hee+17] used the adaptive KL variant of PPO (Section 4) to learn locomotion policies for 3D robots.
- **p. 8 / 6 Experiments - extractive body cue:** In the first six frames, the robot runs towards a target.
- **p. 5 / 6 Experiments - extractive body cue:** Here, we compare the surrogate objective LCLIP to several natural variations and ablated versions.
- **p. 5 / 6 Experiments - extractive body cue:** 6.1 Comparison of Surrogate Objectives First, we compare several different surrogate objectives under different hyperparameters.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** robot/environment의 sequential decision process.
- **Input boundary:** state 또는 observation, action, reward와 transition history.
- **Output/decision under evaluation:** action policy와 induced trajectory.
- **Primary target:** expected return, task success, stability와 sample efficiency.
- **Detected evaluation headings:** 6 Experiments (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 6 Experiments | EMPIRICAL / SIMULATION | We see that PPO outperforms the previous methods on almost all the continuous control environments. | p. 7 (6 Experiments) |
| 6 Experiments | EMPIRICAL / SIMULATION | 0.69 Table 1: Results from continuous control benchmark. | p. 6 (6 Experiments) |
| 6 Experiments | EMPIRICAL / SIMULATION | Note that we also tried clipping in log space, but found the performance to be no better. | p. 6 (6 Experiments) |
| 6 Experiments | EMPIRICAL / SIMULATION | A2C stands for advantage actor critic, and is a synchronous version of A3C, which we found to have the same or better performance than ... | p. 7 (6 Experiments) |
| 6 Experiments | EMPIRICAL / SIMULATION | A table of results and learning curves for all 49 games is provided in Appendix B. | p. 8 (6 Experiments) |

## Dataset / Benchmark Role

- **p. 6 / 6 Experiments - extractive body cue:** Namely, we used 7 simulated robotics tasks2 implemented in OpenAI Gym [Bro+16], which use the MuJoCo [TET12] physics engine.
- **p. 7 / 6 Experiments - extractive body cue:** The three tasks we test on are (1) RoboschoolHumanoid: forward locomotion only, (2) RoboschoolHumanoidFlagrun: position of target is randomly varied every 200 timesteps or whenever ...
- **p. 8 / 6 Experiments - extractive body cue:** 6.4 Comparison to Other Algorithms on the Atari Domain We also ran PPO on the Arcade Learning Environment [Bel+15] benchmark and compared against well-tuned implementations ...
- **p. 6 / 6 Experiments - extractive body cue:** 0.69 Table 1: Results from continuous control benchmark.
- **p. 7 / 6 Experiments - extractive body cue:** [Hee+17] used the adaptive KL variant of PPO (Section 4) to learn locomotion policies for 3D robots.
- **p. 8 / 6 Experiments - extractive body cue:** In the first six frames, the robot runs towards a target.
- **p. 5 / 6 Experiments - extractive body cue:** Here, we compare the surrogate objective LCLIP to several natural variations and ablated versions.
- **p. 5 / 6 Experiments - extractive body cue:** 6.1 Comparison of Surrogate Objectives First, we compare several different surrogate objectives under different hyperparameters.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive body cue:** Figure 1: Plots showing one term (i.e., a single timestep) of the surrogate function LCLIP as a function of the probability ratio r, for positive ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Surrogate objectives, as we interpolate between the initial policy parameter θold, and the updated policy parameter, which we compute after one iteration of ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 3. To represent the policy, we used a fully-connected MLP with two hidden layers of 64 units, and tanh nonlinearities, outputting the mean of ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1: Results from continuous control benchmark. Average normalized scores (over 21 runs of the algorithm, on 7 environments) for each algorithm / hyperparameter setting ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3: Comparison of several algorithms on several MuJoCo environments, training for one million timesteps. 6.3 Showcase in the Continuous Domain: Humanoid Running and Steering ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Learning curves from PPO on 3D humanoid control tasks, using Roboschool. 7
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Still frames of the policy learned from RoboschoolHumanoidFlagrun. In the first six frames, the robot runs towards a target. Then the position is ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: Number of games "won" by each algorithm, where the scoring metric is averaged across three trials. 7

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Namely, we used 7 simulated robotics tasks2 implemented in OpenAI Gym [Bro+16], which use the MuJoCo [TET12] physics engine. | embodiment, simulator version and control stack | p. 6 (6 Experiments), p. 7 (6 Experiments) |
| Task/environment | The three tasks we test on are (1) RoboschoolHumanoid: forward locomotion only, (2) RoboschoolHumanoidFlagrun: position of target is randomly varied every 200 timesteps or ... | reset, timeout, object/scene variation | p. 7 (6 Experiments), p. 8 (6 Experiments) |
| Observation/sensor | state 또는 observation, action, reward와 transition history | calibration, preprocessing, privileged input | p. 1 (Abstract), p. 2 (1 Introduction) |
| Output/decision | action policy와 induced trajectory | action frame, controller and termination | p. 1 (1 Introduction), p. 3 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 3. To represent the policy, we used a fully-connected MLP with two hidden layers of 64 units, and tanh nonlinearities, outputting the mean ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| We consider the following two scoring metrics: (1) average reward per episode over entire training period (which favors fast learning), and (2) average reward ... | definition/direction/unit from same section | p. 8 (6 Experiments) |
| Average normalized scores (over 21 runs of the algorithm, on 7 environments) for each algorithm / hyperparameter setting . β was initialized at 1. | definition/direction/unit from same section | p. 6 (6 Experiments) |
| A2C ACER PPO Tie (1) avg. episode reward over all of training 1 18 30 0 (2) avg. episode reward over last 100 episodes ... | definition/direction/unit from same section | p. 8 (6 Experiments) |
| Table 6: Mean final scores (last 100 episodes) of PPO and A2C on Atari games after 40M game frames (10M timesteps). 12 | definition/direction/unit from same section | p. 12 (Figure/Table caption) |
| A2C stands for advantage actor critic, and is a synchronous version of A3C, which we found to have the same or better performance than ... | definition/direction/unit from same section | p. 7 (6 Experiments) |
| 6.3 Showcase in the Continuous Domain: Humanoid Running and Steering To showcase the performance of PPO on high-dimensional continuous control problems, we train on ... | definition/direction/unit from same section | p. 7 (6 Experiments) |
| Table 5: PPO hyperparameters used in Atari experiments. α is linearly annealed from 1 to 0 over the course of learning. B Performance on ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 6.4 Comparison to Other Algorithms on the Atari Domain We also ran PPO on the Arcade Learning Environment [Bel+15] benchmark and compared against well-tuned ... | comparison identity and matched condition | p. 8 (6 Experiments) |
| We compared against tuned implementations of the following algorithms: trust region policy optimization [Sch+15b], cross-entropy method (CEM) [SL06], vanilla policy gradient with adaptive stepsize3, ... | comparison identity and matched condition | p. 6 (6 Experiments) |
| We see that PPO outperforms the previous methods on almost all the continuous control environments. | comparison identity and matched condition | p. 7 (6 Experiments) |
| 6.1 Comparison of Surrogate Objectives First, we compare several different surrogate objectives under different hyperparameters. | comparison identity and matched condition | p. 5 (6 Experiments) |
| 6.2 Comparison to Other Algorithms in the Continuous Domain Next, we compare PPO (with the "clipped" surrogate objective from Section 3) to several other ... | comparison identity and matched condition | p. 6 (6 Experiments) |
| 0 1000000 500 0 500 1000 1500 2000 HalfCheetah-v1 0 1000000 0 500 1000 1500 2000 2500 Hopper-v1 0 1000000 0 2000 4000 6000 ... | comparison identity and matched condition | p. 7 (6 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Because we are searching over hyperparameters for each algorithm variant, we chose a computationally cheap benchmark to test the algorithms on. | component/input/data sensitivity | p. 6 (6 Experiments) |
| Note that the score is negative for the setting without clipping or penalties, because for one environment (half cheetah) it leads to a very ... | component/input/data sensitivity | p. 6 (6 Experiments) |
| [Hee+17] used the adaptive KL variant of PPO (Section 4) to learn locomotion policies for 3D robots. | component/input/data sensitivity | p. 7 (6 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Whereas standard policy gradient methods perform one gradient update per data sample, we propose a novel objective function that enables multiple epochs of minibatch ... | We see that PPO outperforms the previous methods on almost all the continuous control environments. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (6 Experiments), p. 6 (6 Experiments), p. 6 (6 Experiments), p. 7 (6 Experiments), p. 8 (6 Experiments), p. 8 (6 Experiments) |
| Primary metric/result | 0.69 Table 1: Results from continuous control benchmark. | numeric claim only at cited anchor | p. 6 (6 Experiments) |

- Numeric sentences retained from the body:
- **p. 6 / 6 Experiments - extractive body cue:** We scored each run of the algorithm by computing the average total reward of the last 100 episodes.
- **p. 8 / 6 Experiments - extractive body cue:** We consider the following two scoring metrics: (1) average reward per episode over entire training period (which favors fast learning), and (2) average reward per ...
- **p. 8 / 6 Experiments - extractive body cue:** A2C ACER PPO Tie (1) avg. episode reward over all of training 1 18 30 0 (2) avg. episode reward over last 100 episodes 1 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| no explicit failure cue selected | unreported; domain stress test remains open | verify Discussion/Conclusion |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Algorithm 1 PPO, Actor-Critic Style for iteration=1, 2, . . . do for actor=1, 2, . . . , N do Run policy πθold ... | p. 5 (1 1 + ϵ) |
| Each algorithm was run on all 7 environments, with 3 random seeds on each. | p. 6 (6 Experiments) |
| We compared against tuned implementations of the following algorithms: trust region policy optimization [Sch+15b], cross-entropy method (CEM) [SL06], vanilla policy gradient with adaptive stepsize3, ... | p. 6 (6 Experiments) |
| In the simplest instantiation of this algorithm, we perform the following steps in each policy update: • Using several epochs of minibatch SGD, optimize ... | p. 4 (1 1 + ϵ) |
| However, there is room for improvement in developing a method that is scalable (to large models and parallel implementations), data efficient, and robust (i.e., ... | p. 1 (1 Introduction) |
| 6.1 Comparison of Surrogate Objectives First, we compare several different surrogate objectives under different hyperparameters. | p. 5 (6 Experiments) |
| Hyperparameters are provided in Table 4. | p. 7 (6 Experiments) |
| For PPO, we used the hyperparameters from the previous section, with ϵ = 0.2. | p. 7 (6 Experiments) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- explicit limitation/failure sentence not stated or recoverable in the selected PDF body

- **Evidence anchors reviewed:** datasets p. 6 (6 Experiments), p. 7 (6 Experiments), p. 8 (6 Experiments), p. 6 (6 Experiments), p. 7 (6 Experiments), p. 8 (6 Experiments), metrics p. 6 (Figure/Table caption), p. 8 (6 Experiments), p. 6 (6 Experiments), p. 8 (6 Experiments), p. 12 (Figure/Table caption), p. 7 (6 Experiments), baselines p. 8 (6 Experiments), p. 6 (6 Experiments), p. 7 (6 Experiments), p. 5 (6 Experiments), p. 6 (6 Experiments), p. 7 (6 Experiments), results p. 7 (6 Experiments), p. 6 (6 Experiments), p. 6 (6 Experiments), p. 7 (6 Experiments), p. 8 (6 Experiments), p. 8 (6 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Table 1: Results from continuous control benchmark. Average normalized scores (over 21 runs of the algorithm, on 7 environments) for each algorithm / hyperparameter setting . β was initialized at ... (p. 6, Figure/Table caption).
- **Metric evidence:** We consider the following two scoring metrics: (1) average reward per episode over entire training period (which favors fast learning), and (2) average reward per episode over last 100 episodes ... (p. 8, 6 Experiments).
- **Baseline/ablation evidence:** 6.4 Comparison to Other Algorithms on the Atari Domain We also ran PPO on the Arcade Learning Environment [Bel+15] benchmark and compared against well-tuned implementations of A2C [Mni+16] and ACER ... (p. 8, 6 Experiments).
- **Failure/negative evidence:** Q-learning (with function approximation) fails on many simple problems1 and is poorly understood, vanilla policy gradient methods have poor data effiency and robustness; and trust region policy optimization (TRPO) is ... (p. 1, 1 Introduction).
