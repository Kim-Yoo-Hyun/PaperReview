# Learning Agile and Dynamic Motor Skills for Legged Robots

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1901.08652.
> PDF retrieval source: https://arxiv.org/pdf/1901.08652. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2019 / Science Robotics
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: Robotics, legged locomotion, Reinforcement Learning, sim-to-real
- Official paper: https://arxiv.org/abs/1901.08652
- Full-text retrieval: https://arxiv.org/pdf/1901.08652
- Code/Project: https://leggedrobotics.github.io/rl-blindloco/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 locomotion 문제를 이해하기 위해 읽는다. 본문은 The nominal posture cannot be adjusted to this level in the approach of Bellicoso et al. since this would drastically increase the rate of failure (falling).를 문제로 두고, Furthermore, the system still consists of two independent modules that do not adapt to each other's performance characteristics.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Body text (section not recovered) - extractive body cue:** Dynamic and agile maneuvers of animals cannot be imitated by existing methods that are crafted by humans.
- **p. 1 / Body text (section not recovered) - extractive body cue:** A compelling alternative is reinforcement learning, which requires minimal craftsmanship and promotes the natural evolution of a control policy.
- **p. 1 / Body text (section not recovered) - extractive body cue:** However, so far, reinforcement learning research for legged robots is mainly limited to simulation, and only few and comparably simple examples have been deployed on ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** The primary reason is that training with real robots, particularly with dynamically balancing systems, is complicated and expensive.
- **p. 1 / Body text (section not recovered) - extractive body cue:** In the present work, we report a new method for training a neural network policy in simulation and transferring it to a state-of-the-art legged system, ...
- **p. 4 / Body text (section not recovered) - extractive body cue:** The nominal posture cannot be adjusted to this level in the approach of Bellicoso et al. since this would drastically increase the rate of failure ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** However, systems of this type cannot be scaled down (usually > 40 kg) and generate smoke and noise, limiting them to outdoor environments.

## Core Idea

- **p. 2 / Body text (section not recovered) - extractive body cue:** Furthermore, the system still consists of two independent modules that do not adapt to each other's performance characteristics.
- **p. 4 / Body text (section not recovered) - extractive body cue:** A command consists of three components: forward velocity, lateral velocity, and yaw rate.
- **p. 4 / Body text (section not recovered) - extractive body cue:** Next, we compare our method to ablated alternatives: training with an ideal actuator model and training with an analytical actuator model.
- **p. 1 / Body text (section not recovered) - extractive body cue:** Their freedom to choose contact points with the environment enables them to overcome obstacles comparable to their leg length.
- **p. 3 / Body text (section not recovered) - extractive body cue:** First, the controller enables the ANYmal robot to follow base velocity commands more accurately and energy-efficiently than the best previously existing controller running on the ...
- **p. 3 / Body text (section not recovered) - extractive body cue:** We use the hybrid simulator for training controllers via reinforcement learning (Fig.
- **p. 1 / Body text (section not recovered) - extractive body cue:** In the present work, we report a new method for training a neural network policy in simulation and transferring it to a state-of-the-art legged system, ...
- **p. 2 / Body text (section not recovered) - extractive body cue:** In general, trajectory optimization for a complex rigid-body model with many unspecified contact points is beyond the capabilities of current optimization techniques.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The controller is represented by a multi-layer perceptron that takes as input the history of the robot's states and produces as output the joint position target. | proprioception, terrain/perception observation과 velocity command | p. 3 (Body text (section not recovered)), p. 8 (Body text (section not recovered)) |
| State/latent | controller, represented, multi-layer, perceptron, takes, input, history, robot, states, produces, output, joint | body/contact state, foothold 또는 behavior mode | p. 3 (Body text (section not recovered)), p. 8 (Body text (section not recovered)), p. 7 (Body text (section not recovered)) |
| Output/action | The policy network maps the current observation and the joint state history to the joint position targets. | joint target, torque, footstep 또는 locomotion action | p. 8 (Body text (section not recovered)), p. 7 (Body text (section not recovered)), p. 8 (Body text (section not recovered)) |
| Objective/outcome | The idea of RL is to collect data by trial and error and automatically tune the controller to optimize the given cost (or reward) function representing the task. | velocity/progress, stability, energy와 terrain generalization | p. 2 (Body text (section not recovered)), p. 6 (Body text (section not recovered)), p. 7 (Body text (section not recovered)) |

## Main Claims and Actual Contribution

- **p. 2 / Body text (section not recovered) - extractive body cue:** Furthermore, the system still consists of two independent modules that do not adapt to each other's performance characteristics.
- **p. 4 / Body text (section not recovered) - extractive body cue:** A command consists of three components: forward velocity, lateral velocity, and yaw rate.
- **p. 4 / Body text (section not recovered) - extractive body cue:** Next, we compare our method to ablated alternatives: training with an ideal actuator model and training with an analytical actuator model.
- **p. 1 / Body text (section not recovered) - extractive body cue:** Their freedom to choose contact points with the environment enables them to overcome obstacles comparable to their leg length.
- **p. 3 / Body text (section not recovered) - extractive body cue:** First, the controller enables the ANYmal robot to follow base velocity commands more accurately and energy-efficiently than the best previously existing controller running on the ...
- **p. 6 / Body text (section not recovered) - extractive body cue:** We then further improved the success rate to 100 % by relaxing the joint velocity constraints.
- **p. 9 / Body text (section not recovered) - extractive body cue:** [57] found that such a controller can outperform a torque controller in both training speed and final control performance.
- **p. 9 / Body text (section not recovered) - extractive body cue:** A learning session terminates if the average performance of the policy does not improve by more than a task-specific threshold within 300 TRPO iterations.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (Body text (section not recovered)), p. 9 (Body text (section not recovered)) |
| Embodiment/environment | Many hardware changes were introduced as well: different robot configurations, which roughly contribute 2.0 kg to the total weight, and a new drive which has a spring three times stiffer than the ... | hardware/simulator version and reset protocol | p. 7 (Body text (section not recovered)), p. 6 (Body text (section not recovered)) |
| Dataset/benchmark | DISCUSSION The learning-based control approach presented in this paper achieved a new level of locomotion skill based purely on training in simulation and without tedious tuning on the physical robot. | role, split, size and leakage | p. 7 (Body text (section not recovered)), p. 6 (Body text (section not recovered)), p. 6 (Body text (section not recovered)), p. 8 (Body text (section not recovered)) |
| Metric | We then further improved the success rate to 100 % by relaxing the joint velocity constraints. | definition, denominator, direction and uncertainty | p. 6 (Body text (section not recovered)), p. 5 (Figure/Table caption), p. 10 (Body text (section not recovered)) |
| Baseline/ablation | It outperformed the previous speed record by 25 % and learned to consistently restore the robot to an operational configuration by dynamically rolling over its body. | fair input/data/compute/action matching | p. 6 (Body text (section not recovered)), p. 9 (Body text (section not recovered)), p. 5 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 9 / Body text (section not recovered) - extractive body cue:** However, since this height estimator cannot be used when the robot is not on its feet, we removed the height observation when training for recovery ...
- **p. 11 / Body text (section not recovered) - extractive body cue:** For training recovery from a fall, the collision bodies of the ANYmal model are randomized in size and position.
- **p. 10 / Body text (section not recovered) - extractive body cue:** However, as in many other RL literature, our control policy is state-indexed and does not suffer from the limitations of common PD controllers.
- **p. 6 / Body text (section not recovered) - extractive body cue:** Fast and flexible recovery after a fall, as seen in animals, requires dynamic motion with multiple unspecified contact points.
- **p. 7 / Body text (section not recovered) - extractive body cue:** Developing the recovery policy took about a week largely due to the fact that some safety concerns (i.e., high impacts, fast swing legs, collisions with ...
- **p. 11 / Body text (section not recovered) - extractive body cue:** For training for recovery from a fall, TRPO took 79 days of simulated time, which corresponds to eleven hours of computation in real time.
- **p. 6 / Body text (section not recovered) - extractive body cue:** The collision model for our quadruped is highly complicated: it consists of 41 collision bodies, such as boxes, cylinders, and spheres (Fig.

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 locomotion 문제를 이해하기 위해 읽는다. 본문은 The nominal posture cannot be adjusted to this level in the approach of Bellicoso et al. since this would drastically increase the rate of failure (falling).를 문제로 두고, Furthermore, the system still consists of two independent modules that do not adapt to each other's performance characteristics.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 4 (Body text (section not recovered)), p. 1 (Body text (section not recovered)), p. 2 (Body text (section not recovered)), p. 1 (Body text (section not recovered)), p. 2 (Body text (section not recovered)), p. 3 (Body text (section not recovered)) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
