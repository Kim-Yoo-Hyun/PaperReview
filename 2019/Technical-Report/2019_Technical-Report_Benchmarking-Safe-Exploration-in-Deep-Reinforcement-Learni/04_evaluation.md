# Evaluation - Benchmarking Safe Exploration in Deep Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openai.com/index/benchmarking-safe-exploration-in-deep-reinforcement-learning/; PDF retrieval source: https://cdn.openai.com/safexp-short.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 21 (5.3 Results), p. 14 (5 Experiments), p. 10 (Figure/Table caption), p. 14 (5 Experiments), p. 15 (5 Experiments), p. 15 (5 Experiments)): By success, we mean attaining improvements simultaneously along both the episodic return axis and the constraint regret axis, while still producing a constraint-satisfying policy at the conclusion of training.

## Evaluation Body Digest

- **p. 15 / 5 Experiments - extractive PDF cue:** SG6 has at least one environment for each task, robot, and level.
- **p. 21 / 5.3 Results - extractive PDF cue:** Problem 1 can be investigated with unmodified Safety Gym benchmark environments, using the Level 1 and 2 versions of each task as (First Environment, Second ...
- **p. 15 / 5 Experiments - extractive PDF cue:** SGCar: All six Car robot environments with constraints in Safety Gym.
- **p. 16 / 5 Experiments - extractive PDF cue:** Experiments for Point and Car robots used batch sizes of 30, 000 environment interaction steps, and experiments for Doggo used 60, 000.
- **p. 16 / 5.3 Results - extractive PDF cue:** [2017]. • Lagrangian methods are able to find constraint-satisfying policies that attain nontrivial returns in several of the Point environments, demonstrating that when controlling for ...
- **p. 18 / 5.3 Results - extractive PDF cue:** CPO PPO PPO-Lagrangian TRPO TRPO-Lagrangian PointGoal1 0 5 10 15 20 25 AverageEpRet 20 40 60 80 AverageEpCost 0.02 0.04 0.06 0.08 CostRate PointGoal2 5 ...
- **p. 19 / 5.3 Results - extractive PDF cue:** CPO PPO PPO-Lagrangian TRPO TRPO-Lagrangian CarGoal1 0 10 20 30 AverageEpRet 20 40 60 80 AverageEpCost 0.00 0.02 0.04 0.06 0.08 CostRate CarGoal2 0 5 ...
- **p. 20 / 5.3 Results - extractive PDF cue:** CPO PPO PPO-Lagrangian TRPO TRPO-Lagrangian DoggoGoal1 0 10 20 30 40 50 AverageEpRet 0 20 40 60 80 100 120 AverageEpCost 0.02 0.04 0.06 0.08 ...

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** 5 Experiments (p. 14); 5.3 Results (p. 16).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5.3 Results | BENCHMARK / DATASET | By success, we mean attaining improvements simultaneously along both the episodic return axis and the constraint regret axis, while still producing a constraint-satisfying policy ... | p. 21 (5.3 Results) |
| 5 Experiments | BENCHMARK / DATASET | However, we highlight a few common rules that guide our discussion: • All agents that fail to satisfy constraints are strictly worse than all ... | p. 14 (5 Experiments) |
| Figure/Table caption | BENCHMARK / DATASET | Figure 3: Constraint elements used in our environments. currently-highlighted button, which is the goal button. After the agent presses the correct button, the environment ... | p. 10 (Figure/Table caption) |
| 5 Experiments | BENCHMARK / DATASET | Metrics: To characterize the task and safety performance of an agent and its training run, we measure the following throughout training: • The average ... | p. 14 (5 Experiments) |
| 5 Experiments | BENCHMARK / DATASET | We report average normalized scores for various sets of environments: SG1: The set of all nine level 1 Safety Gym environments. | p. 15 (5 Experiments) |

## Dataset / Benchmark Role

- **p. 15 / 5 Experiments - extractive PDF cue:** SG6 has at least one environment for each task, robot, and level.
- **p. 21 / 5.3 Results - extractive PDF cue:** Problem 1 can be investigated with unmodified Safety Gym benchmark environments, using the Level 1 and 2 versions of each task as (First Environment, Second ...
- **p. 15 / 5 Experiments - extractive PDF cue:** SGCar: All six Car robot environments with constraints in Safety Gym.
- **p. 16 / 5 Experiments - extractive PDF cue:** Experiments for Point and Car robots used batch sizes of 30, 000 environment interaction steps, and experiments for Doggo used 60, 000.
- **p. 16 / 5.3 Results - extractive PDF cue:** [2017]. • Lagrangian methods are able to find constraint-satisfying policies that attain nontrivial returns in several of the Point environments, demonstrating that when controlling for ...
- **p. 18 / 5.3 Results - extractive PDF cue:** CPO PPO PPO-Lagrangian TRPO TRPO-Lagrangian PointGoal1 0 5 10 15 20 25 AverageEpRet 20 40 60 80 AverageEpCost 0.02 0.04 0.06 0.08 CostRate PointGoal2 5 ...
- **p. 19 / 5.3 Results - extractive PDF cue:** CPO PPO PPO-Lagrangian TRPO TRPO-Lagrangian CarGoal1 0 10 20 30 AverageEpRet 20 40 60 80 AverageEpCost 0.00 0.02 0.04 0.06 0.08 CostRate CarGoal2 0 5 ...
- **p. 20 / 5.3 Results - extractive PDF cue:** CPO PPO PPO-Lagrangian TRPO TRPO-Lagrangian DoggoGoal1 0 10 20 30 40 50 AverageEpRet 0 20 40 60 80 100 120 AverageEpCost 0.02 0.04 0.06 0.08 ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 1: Pre-made robots in Safety Gym. These robots are used in our benchmark environments. (a) Position (b) Button (c) Push
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 2: Tasks for our environments. From left to right: Goal, Button, Push. In "Goal," the objective is to move the robot inside the green ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Figure 3: Constraint elements used in our environments. currently-highlighted button, which is the goal button. After the agent presses the correct button, the environment will ...
- **p. 11 / Figure/Table caption - extractive PDF cue:** Figure 4: Visualizations of pseudo-lidar observation spaces. On the left, we see a lidar halo repre- senting the goal pseudo-lidar for this agent. On the ...
- **p. 12 / Figure/Table caption - extractive PDF cue:** Figure 5: Images of benchmark environments. Top row: Goal environments. Middle row: Button environments. Bottom row: Push environments. In each subfigure, the left column shows ...
- **p. 12 / Figure/Table caption - extractive PDF cue:** Figure 6: Diversity of generated layouts for the Safexp-PointPush2-v0 env. 4.2 Safety Gym Benchmark Suite Safety Gym ships with a suite of pre-configured benchmark environments, ...
- **p. 16 / Figure/Table caption - extractive PDF cue:** Table 1: Normalized metrics from the conclusion of training averaged over the SG18 slate of environments and three random seeds per environment. • Constrained Policy ...
- **p. 17 / Figure/Table caption - extractive PDF cue:** Table 2: Normalized metrics from the conclusion of training averaged over various slates of environ- ments and three random seeds per environment. 17

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | SG6 has at least one environment for each task, robot, and level. | embodiment, simulator version and control stack | p. 15 (5 Experiments), p. 21 (5.3 Results) |
| Task/environment | Problem 1 can be investigated with unmodified Safety Gym benchmark environments, using the Level 1 and 2 versions of each task as (First Environment, ... | reset, timeout, object/scene variation | p. 21 (5.3 Results), p. 15 (5 Experiments) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 1 (Abstract) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 2 (1 Introduction), p. 3 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We compare normalized scores like we would compare individual training runs: the average constraint violation should be zero (or within noise of zero), and ... | definition/direction/unit from same section | p. 15 (5 Experiments) |
| Unconstrained RL algorithms are able to score high returns by taking unsafe actions, as measured by the cost function. | definition/direction/unit from same section | p. 16 (5.3 Results) |
| Constrained RL algorithms attain lower levels of return, and correspondingly maintain desired levels of costs. • The design decision to make Level 2 Safety ... | definition/direction/unit from same section | p. 16 (5.3 Results) |
| We report average normalized scores for various sets of environments: SG1: The set of all nine level 1 Safety Gym environments. | definition/direction/unit from same section | p. 15 (5 Experiments) |
| Metrics: To characterize the task and safety performance of an agent and its training run, we measure the following throughout training: • The average ... | definition/direction/unit from same section | p. 14 (5 Experiments) |
| However, we highlight a few common rules that guide our discussion: • All agents that fail to satisfy constraints are strictly worse than all ... | definition/direction/unit from same section | p. 14 (5 Experiments) |
| By success, we mean attaining improvements simultaneously along both the episodic return axis and the constraint regret axis, while still producing a constraint-satisfying policy ... | definition/direction/unit from same section | p. 21 (5.3 Results) |
| Figure 3: Constraint elements used in our environments. currently-highlighted button, which is the goal button. After the agent presses the correct button, the environment ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Advancing SOTA on Safety Gym: Our baseline results for constrained RL indicate a need for stronger and/or better-tuned algorithms to succeed on Safety Gym ... | comparison identity and matched condition | p. 21 (5.3 Results) |
| In this section, we describe our experiments to baseline existing unconstrained and constrained RL algorithms on Safety Gym environments. | comparison identity and matched condition | p. 14 (5 Experiments) |
| And finally, we evaluated baseline unconstrained and constrained RL algorithms on Safety Gym environments to partially clarify the current state of the art in ... | comparison identity and matched condition | p. 21 (5.3 Results) |
| Comparing Training Runs: There are several ways to rank agents and training runs based on these measurements, and different comparison rules will be appropriate ... | comparison identity and matched condition | p. 14 (5 Experiments) |
| The normalized values allow easy comparison to a reference point (in this case, unconstrained PPO). | comparison identity and matched condition | p. 16 (5.3 Results) |
| These learning curves depict the metrics Jr(θ), Jc(θ), and ρc(θ) without normalization, and show the absolute performance of each algorithm. | comparison identity and matched condition | p. 16 (5.3 Results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| These learning curves depict the metrics Jr(θ), Jc(θ), and ρc(θ) without normalization, and show the absolute performance of each algorithm. | component/input/data sensitivity | p. 16 (5.3 Results) |
| [2017]. • Lagrangian methods are able to find constraint-satisfying policies that attain nontrivial returns in several of the Point environments, demonstrating that when controlling ... | component/input/data sensitivity | p. 16 (5.3 Results) |
| We note that standard model-free RL approaches without replay buffers are fundamentally limited in their ability to minimize constraint regret: they must continually experience ... | component/input/data sensitivity | p. 21 (5.3 Results) |
| Figure 3: Constraint elements used in our environments. currently-highlighted button, which is the goal button. After the agent presses the correct button, the environment ... | component/input/data sensitivity | p. 10 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To address the gap, we present Safety Gym: a set of tools for accelerating safe exploration research. | By success, we mean attaining improvements simultaneously along both the episodic return axis and the constraint regret axis, while still producing a constraint-satisfying policy ... | PDF body cue; verify exact table/figure and matched conditions | p. 21 (5.3 Results), p. 14 (5 Experiments), p. 10 (Figure/Table caption), p. 14 (5 Experiments), p. 15 (5 Experiments), p. 15 (5 Experiments) |
| Primary metric/result | However, we highlight a few common rules that guide our discussion: • All agents that fail to satisfy constraints are strictly worse than all ... | numeric claim only at cited anchor | p. 14 (5 Experiments) |

- Numeric sentences retained from the body:
- **p. 16 / 5 Experiments - extractive PDF cue:** Point and Car agents were trained for 107 steps, and Doggo agents were trained for 108 steps.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | [2017], we omit the learned failure predictor they used for cost shaping. | p. 16 (5 Experiments) |
| body limitation/failure cue | There are a number of avenues we consider promising for future work. | p. 21 (5.3 Results) |
| body limitation/failure cue | Figure 6: Diversity of generated layouts for the Safexp-PointPush2-v0 env. 4.2 Safety Gym Benchmark Suite Safety Gym ships with a suite of pre-configured benchmark ... | p. 12 (Figure/Table caption) |
| body limitation/failure cue | First and foremost, it corresponds directly to safety outcomes: a lower cost rate means that fewer unsafe things happened. | p. 14 (5 Experiments) |
| body limitation/failure cue | E τ∼πθ XT t=0 ct  ≤d, where ct is the aggregate indicator cost function for the environment (ct = 1 for an unsafe ... | p. 14 (5 Experiments) |
| body limitation/failure cue | 3Characteristic return and cumulative cost were obtained by averaging over the last five epochs of training to reduce noise. | p. 15 (5 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We assign each environment E a set of characteristic metrics, JE r , JE c , ρE c (all strictly positive), and compute normalized ... | p. 15 (5 Experiments) |
| Experiments for Point and Car robots used batch sizes of 30, 000 environment interaction steps, and experiments for Doggo used 60, 000. | p. 16 (5 Experiments) |
| Because training on the full slate SG18 with multiple seeds per environment is computationally taxing, we recommend SG6 as a basic slate for constrained ... | p. 15 (5 Experiments) |
| All experiments were run with three random seeds. | p. 16 (5 Experiments) |
| We believe that ρc is a suitable measure of safety regret for a training run. | p. 14 (5 Experiments) |
| The quantity we aim to constrain. • The average cost over the entirety of training, ρc (the sum of all costs divided by total ... | p. 14 (5 Experiments) |
| Dashed red lines indicate the target value for a constraint-satisfying policy (AverageEpCost curves) or approximately constraint-satisfying training run (CostRate curves). | p. 18 (5.3 Results) |
| 6 Conclusions In this work, we took three main steps towards progress on the safe exploration problem. | p. 21 (5.3 Results) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 16 / 5 Experiments - extractive PDF cue:** [2017], we omit the learned failure predictor they used for cost shaping.
- **p. 21 / 5.3 Results - extractive PDF cue:** There are a number of avenues we consider promising for future work.
- **p. 12 / Figure/Table caption - extractive PDF cue:** Figure 6: Diversity of generated layouts for the Safexp-PointPush2-v0 env. 4.2 Safety Gym Benchmark Suite Safety Gym ships with a suite of pre-configured benchmark environments, ...
- **p. 14 / 5 Experiments - extractive PDF cue:** First and foremost, it corresponds directly to safety outcomes: a lower cost rate means that fewer unsafe things happened.
- **p. 14 / 5 Experiments - extractive PDF cue:** E τ∼πθ XT t=0 ct  ≤d, where ct is the aggregate indicator cost function for the environment (ct = 1 for an unsafe interaction, ...
- **p. 15 / 5 Experiments - extractive PDF cue:** 3Characteristic return and cumulative cost were obtained by averaging over the last five epochs of training to reduce noise.

- **PDF anchors reviewed:** datasets p. 15 (5 Experiments), p. 21 (5.3 Results), p. 15 (5 Experiments), p. 16 (5 Experiments), p. 16 (5.3 Results), p. 18 (5.3 Results), metrics p. 15 (5 Experiments), p. 16 (5.3 Results), p. 16 (5.3 Results), p. 15 (5 Experiments), p. 14 (5 Experiments), p. 14 (5 Experiments), baselines p. 21 (5.3 Results), p. 14 (5 Experiments), p. 21 (5.3 Results), p. 14 (5 Experiments), p. 16 (5.3 Results), p. 16 (5.3 Results), results p. 21 (5.3 Results), p. 14 (5 Experiments), p. 10 (Figure/Table caption), p. 14 (5 Experiments), p. 15 (5 Experiments), p. 15 (5 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
