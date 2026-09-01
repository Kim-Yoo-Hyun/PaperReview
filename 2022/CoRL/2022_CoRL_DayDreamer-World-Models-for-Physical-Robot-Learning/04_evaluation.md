# Evaluation - DayDreamer: World Models for Physical Robot Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v205/wu23c.html; PDF retrieval source: https://arxiv.org/pdf/2206.14176. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (3 Experiments), p. 7 (3 Experiments), p. 5 (3 Experiments), p. 6 (3 Experiments), p. 6 (3 Experiments), p. 4 (3 Experiments)): We find that DrQv2, a model-free algorithm specifically designed to continuous control from pixels, achieves similar performance.

## Evaluation Body Digest

- **p. 6 / 3 Experiments - extractive body cue:** 3.2 UR5 Multi-Object Visual Pick and Place Common in warehouse and logistics environments, pick and place tasks require a robot manipulator to transport items from ...
- **p. 7 / 3 Experiments - extractive body cue:** As the goal is fixed, after 100 environment steps, we end the episode and randomize the robot's position through a sequence of high power random ...
- **p. 7 / 3 Experiments - extractive body cue:** While soft objects would be challenging to model accurately in a simulator, Dreamer avoids this issue by directly learning on the real robot without a ...
- **p. 4 / 3 Experiments - extractive body cue:** The experiments are representative of common robotic tasks, such as locomotion, manipulation, and navigation.
- **p. 4 / 3 Experiments - extractive body cue:** We evaluate Dreamer on 4 robots, each with a different task, and compare its performance to appropriate algorithmic and human baselines.
- **p. 5 / 3 Experiments - extractive body cue:** In contrast, we train in the end-toend reinforcement learning setting directly on the robot, without simulators or resets.
- **p. 5 / 3 Experiments - extractive body cue:** This high-dimensional continuous control task requires training a quadruped robot to roll over from its back, stand up, and walk forward at a fixed target ...
- **p. 6 / 3 Experiments - extractive body cue:** Over time, grasping becomes precise and the robot learns to push objects out of corners.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** uncertain robot state와 safe/unsafe operating region.
- **Input boundary:** observation, uncertainty/risk estimate와 task command.
- **Output/decision under evaluation:** shielded, recovery 또는 safe action.
- **Primary target:** task return과 violation/failure probability.
- **Detected evaluation headings:** 3 Experiments (p. 4).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 3 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | We find that DrQv2, a model-free algorithm specifically designed to continuous control from pixels, achieves similar performance. | p. 7 (3 Experiments) |
| 3 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Dreamer learns a policy that enables the XArm to achieve an average pick rate of 3.1 objects per minute in 10 hours of time, ... | p. 7 (3 Experiments) |
| 3 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | We choose Rainbow (Hessel et al., 2018) as a powerful representative of this category, an algorithm that combines many improvements of DQN. | p. 5 (3 Experiments) |
| 3 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | The robot initially struggles to learn as the reward signal is very sparse, but begins to gradually improve after 2 hours of training. | p. 6 (3 Experiments) |
| 3 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Successfully grasping one of the 3 objects, detected by partial gripper closure, results in a +1 reward, releasing the object in the same bin ... | p. 6 (3 Experiments) |

## Dataset / Benchmark Role

- **p. 6 / 3 Experiments - extractive body cue:** 3.2 UR5 Multi-Object Visual Pick and Place Common in warehouse and logistics environments, pick and place tasks require a robot manipulator to transport items from ...
- **p. 7 / 3 Experiments - extractive body cue:** As the goal is fixed, after 100 environment steps, we end the episode and randomize the robot's position through a sequence of high power random ...
- **p. 7 / 3 Experiments - extractive body cue:** While soft objects would be challenging to model accurately in a simulator, Dreamer avoids this issue by directly learning on the real robot without a ...
- **p. 4 / 3 Experiments - extractive body cue:** The experiments are representative of common robotic tasks, such as locomotion, manipulation, and navigation.
- **p. 4 / 3 Experiments - extractive body cue:** We evaluate Dreamer on 4 robots, each with a different task, and compare its performance to appropriate algorithmic and human baselines.
- **p. 5 / 3 Experiments - extractive body cue:** In contrast, we train in the end-toend reinforcement learning setting directly on the robot, without simulators or resets.
- **p. 5 / 3 Experiments - extractive body cue:** This high-dimensional continuous control task requires training a quadruped robot to roll over from its back, stand up, and walk forward at a fixed target ...
- **p. 6 / 3 Experiments - extractive body cue:** Over time, grasping becomes precise and the robot learns to push objects out of corners.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: To study the applicability of Dreamer for sample-efficient robot learning, we apply the algorithm to learn robot locomotion, manipulation, and navigation tasks from ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2: Dreamer follows a simple pipeline for online learning on robot hardware without simulators. The cur- rent learned policy collects experience on the robot. ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3: Neural Network Training We leverage the Dreamer algorithm (Hafner et al., 2019; 2020) for fast robot learning in real world. Dreamer consists of ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4: A1 Quadruped Walking Starting from lying on its back with the feet in the air, Dreamer learns to roll over, stand up, and ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 8: Within 10 minutes of perturb- ing the learned walking behavior, the robot adapts to withstanding pushes or quickly rolling over and back on ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5: UR5 Multi Object Visual Pick and Place This task requires learning to locate three ball objects from third-person camera images, grasp them, and ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 6: XArm Visual Pick and Place The XArm is an affordable robot arm that operates slower than the UR5. To demonstrate successful learning on ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 7: Sphero Navigation This task requires the Sphero Ollie robot to navigate to a fixed goal location through continuous actions given a top-down RGB ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 3.2 UR5 Multi-Object Visual Pick and Place Common in warehouse and logistics environments, pick and place tasks require a robot manipulator to transport items ... | embodiment, simulator version and control stack | p. 6 (3 Experiments), p. 7 (3 Experiments) |
| Task/environment | As the goal is fixed, after 100 environment steps, we end the episode and randomize the robot's position through a sequence of high power ... | reset, timeout, object/scene variation | p. 7 (3 Experiments), p. 7 (3 Experiments) |
| Observation/sensor | observation, uncertainty/risk estimate와 task command | calibration, preprocessing, privileged input | p. 3 (2 Approach), p. 3 (1 Introduction) |
| Output/decision | shielded, recovery 또는 safe action | action frame, controller and termination | p. 4 (2 Approach), p. 4 (2 Approach) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Dreamer overcomes the challenges of visual localization and sparse rewards on this task, learning a successful strategy within a few hours of autonomous operation. | definition/direction/unit from same section | p. 6 (3 Experiments) |
| Successfully grasping one of the 3 objects, detected by partial gripper closure, results in a +1 reward, releasing the object in the same bin ... | definition/direction/unit from same section | p. 6 (3 Experiments) |
| The robot is provided with a dense reward equal to the negative L2 distance. | definition/direction/unit from same section | p. 7 (3 Experiments) |
| While Rainbow converges to the local optimum of grasping and ungrasping the object in the same bin, Dreamer learns a successful pick and place ... | definition/direction/unit from same section | p. 7 (3 Experiments) |
| Figure 1: To study the applicability of Dreamer for sample-efficient robot learning, we apply the algorithm to learn robot locomotion, manipulation, and navigation tasks ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| 0 20 40 60 Minutes 5 7 9 11 Avg Reward A1 Quadruped Walking Dreamer SAC Figure 4: A1 Quadruped Walking Starting from lying ... | definition/direction/unit from same section | p. 5 (3 Experiments) |
| The graph shows a single training run with the shaded area indicating one standard deviation within each time bin. | definition/direction/unit from same section | p. 5 (3 Experiments) |
| We evaluate Dreamer on 4 robots, each with a different task, and compare its performance to appropriate algorithmic and human baselines. | definition/direction/unit from same section | p. 4 (3 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| The state-of-the-art baseline in this category is DrQv2 (Yarats et al., 2021), which uses image augmentation to increase sample-efficiency. | comparison identity and matched condition | p. 5 (3 Experiments) |
| Figure 1: To study the applicability of Dreamer for sample-efficient robot learning, we apply the algorithm to learn robot locomotion, manipulation, and navigation tasks ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| We evaluate Dreamer on 4 robots, each with a different task, and compare its performance to appropriate algorithmic and human baselines. | comparison identity and matched condition | p. 4 (3 Experiments) |
| Baselines We compare to a strong learning algorithm for each of our experimental setups. | comparison identity and matched condition | p. 5 (3 Experiments) |
| Specifically, we aim to answer the following research questions: • Does Dreamer enable robot learning directly in the real world, without simulators? • Does ... | comparison identity and matched condition | p. 4 (3 Experiments) |
| In comparison, SAC quickly learns to roll off its back but fails to stand up or walk given the small data budget. | comparison identity and matched condition | p. 6 (3 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Specifically, we aim to answer the following research questions: • Does Dreamer enable robot learning directly in the real world, without simulators? • Does ... | component/input/data sensitivity | p. 4 (3 Experiments) |
| In contrast, we train in the end-toend reinforcement learning setting directly on the robot, without simulators or resets. | component/input/data sensitivity | p. 5 (3 Experiments) |
| Due to space constraints, we manually intervene when the robot has reached the end of the available training area, without modifying the joint configuration ... | component/input/data sensitivity | p. 5 (3 Experiments) |
| While soft objects would be challenging to model accurately in a simulator, Dreamer avoids this issue by directly learning on the real robot without ... | component/input/data sensitivity | p. 7 (3 Experiments) |
| Figure 3: Neural Network Training We leverage the Dreamer algorithm (Hafner et al., 2019; 2020) for fast robot learning in real world. Dreamer consists ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |
| Figure 1: To study the applicability of Dreamer for sample-efficient robot learning, we apply the algorithm to learn robot locomotion, manipulation, and navigation tasks ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Dreamer consists of two neural network components. | We find that DrQv2, a model-free algorithm specifically designed to continuous control from pixels, achieves similar performance. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (3 Experiments), p. 7 (3 Experiments), p. 5 (3 Experiments), p. 6 (3 Experiments), p. 6 (3 Experiments), p. 4 (3 Experiments) |
| Primary metric/result | Dreamer learns a policy that enables the XArm to achieve an average pick rate of 3.1 objects per minute in 10 hours of time, ... | numeric claim only at cited anchor | p. 7 (3 Experiments) |

- Numeric sentences retained from the body:
- **p. 4 / 3 Experiments - extractive body cue:** We evaluate Dreamer on 4 robots, each with a different task, and compare its performance to appropriate algorithmic and human baselines.
- **p. 5 / 3 Experiments - extractive body cue:** 0 20 40 60 Minutes 5 7 9 11 Avg Reward A1 Quadruped Walking Dreamer SAC Figure 4: A1 Quadruped Walking Starting from lying on ...
- **p. 5 / 3 Experiments - extractive body cue:** After 1 hour of training, we start pushing the robot and find that it adapts its behavior within 10 minutes to withstand light pushes and ...
- **p. 5 / 3 Experiments - extractive body cue:** The motors are controlled at 20 Hz via continuous actions that represent motor angles that are realized by a PD controller on the hardware.
- **p. 6 / 3 Experiments - extractive body cue:** 0 2 4 6 8 Hours 0 1 2 3 4 Objects / Minute Human UR5 Visual Pick Place Dreamer Rainbow PPO Figure 5: UR5 ...
- **p. 6 / 3 Experiments - extractive body cue:** About 1 hour into training, the robot learns a pronking gait to walk forward at the desired velocity.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Limitations While Dreamer shows promising results, learning on hardware over many hours creates wear on robots that may require human intervention or repair. | p. 8 (5 Discussion) |
| body limitation/failure cue | In comparison, SAC quickly learns to roll off its back but fails to stand up or walk given the small data budget. | p. 6 (3 Experiments) |
| body limitation/failure cue | Prior work in quadruped locomotion requires either extensive training in simulation under domain randomization, using recovery controllers to avoid unsafe states, or defining the ... | p. 5 (3 Experiments) |
| body limitation/failure cue | The filled circles indicate times where the robot fell on its back, requiring the learning of a robust strategy for getting back up. | p. 5 (3 Experiments) |
| body limitation/failure cue | We hypothesize that Rainbow DQN and PPO fail because they require larger amounts of experience, which is not feasible for us to collect in ... | p. 6 (3 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| 0 20 40 60 Minutes 5 7 9 11 Avg Reward A1 Quadruped Walking Dreamer SAC Figure 4: A1 Quadruped Walking Starting from lying ... | p. 5 (3 Experiments) |
| This enables massively parallel behavior learning with typical batch sizes of 16K on a single GPU, similar to specialized modern simulators (Makoviychuk et al., ... | p. 4 (2 Approach) |
| The graph shows a single training run with the shaded area indicating one standard deviation within each time bin. | p. 5 (3 Experiments) |
| An upright reward is computed from the base frame up vector ˆzT , terms for matching the standing pose are computed from the joint ... | p. 6 (3 Experiments) |
| As shown in Figure 7, Dreamer achieves an average distance to the goal of 0.15, measured in units of the area size and averaged ... | p. 7 (3 Experiments) |
| As the goal is fixed, after 100 environment steps, we end the episode and randomize the robot's position through a sequence of high power ... | p. 7 (3 Experiments) |
| In our implementation, a learner thread continuously trains the world model and actor critic behavior, while an actor thread in parallel computes actions for ... | p. 3 (2 Approach) |
| This reduces accumulating errors and enables massively parallel training with a large batch size. | p. 3 (2 Approach) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5 Discussion - extractive body cue:** Limitations While Dreamer shows promising results, learning on hardware over many hours creates wear on robots that may require human intervention or repair.
- **p. 6 / 3 Experiments - extractive body cue:** In comparison, SAC quickly learns to roll off its back but fails to stand up or walk given the small data budget.
- **p. 5 / 3 Experiments - extractive body cue:** Prior work in quadruped locomotion requires either extensive training in simulation under domain randomization, using recovery controllers to avoid unsafe states, or defining the action ...
- **p. 5 / 3 Experiments - extractive body cue:** The filled circles indicate times where the robot fell on its back, requiring the learning of a robust strategy for getting back up.
- **p. 6 / 3 Experiments - extractive body cue:** We hypothesize that Rainbow DQN and PPO fail because they require larger amounts of experience, which is not feasible for us to collect in the ...

- **PDF anchors reviewed:** datasets p. 6 (3 Experiments), p. 7 (3 Experiments), p. 7 (3 Experiments), p. 4 (3 Experiments), p. 4 (3 Experiments), p. 5 (3 Experiments), metrics p. 6 (3 Experiments), p. 6 (3 Experiments), p. 7 (3 Experiments), p. 7 (3 Experiments), p. 1 (Figure/Table caption), p. 5 (3 Experiments), baselines p. 5 (3 Experiments), p. 1 (Figure/Table caption), p. 4 (3 Experiments), p. 5 (3 Experiments), p. 4 (3 Experiments), p. 6 (3 Experiments), results p. 7 (3 Experiments), p. 7 (3 Experiments), p. 5 (3 Experiments), p. 6 (3 Experiments), p. 6 (3 Experiments), p. 4 (3 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
