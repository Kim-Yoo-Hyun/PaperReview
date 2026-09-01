# Learning Robust Perceptive Locomotion for Quadrupedal Robots in the Wild

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (22 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2201.08117.
> PDF retrieval source: https://arxiv.org/pdf/2201.08117. Reading tracker status/evidence was not changed.

- Year/Venue: 2022 / Science Robotics
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: CORE
- Tags: Robotics, quadruped locomotion, perception, rough terrain
- Official paper: https://arxiv.org/abs/2201.08117
- Full-text retrieval: https://arxiv.org/pdf/2201.08117
- Code/Project: https://leggedrobotics.github.io/rl-perceptiveloco/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (22 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 locomotion 문제를 이해하기 위해 읽는다. 본문은 Most existing methods that rely on onboard terrain perception are still vulnerable to these failures.를 문제로 두고, Our method consists of three stages, illustrated in Figure 6.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / 1. INTRODUCTION - extractive body cue:** Legged robots can carry out missions in challenging environments that are too far or too dangerous for humans, such as hazardous areas and the surfaces ...
- **p. 1 / 1. INTRODUCTION - extractive body cue:** Legs can walk over challenging terrain with steep slopes, steps, and gaps that may impede wheeled or tracked vehicles of similar size.
- **p. 1 / 1. INTRODUCTION - extractive body cue:** There has been notable progress in legged robotics [1-5] and several commercial platforms are being deployed in the real world [6-10].
- **p. 1 / 1. INTRODUCTION - extractive body cue:** However, until now, legged robots could not match the performance of animals in traversing challenging real-world terrain.
- **p. 1 / 1. INTRODUCTION - extractive body cue:** Many legged animals such as humans and dogs can briskly walk or run in such environments by foreseeing the upcoming terrain and planning their footsteps ...
- **p. 1 / 1. INTRODUCTION - extractive body cue:** Most existing methods that rely on onboard terrain perception are still vulnerable to these failures.
- **p. 3 / 1. INTRODUCTION - extractive body cue:** Handling exteroception failures has been a challenging problem in robotics.

## Core Idea

- **p. 8 / 4. MATERIALS AND METHODS - extractive body cue:** Our method consists of three stages, illustrated in Figure 6.
- **p. 3 / 1. INTRODUCTION - extractive body cue:** Here we present a terrain-aware locomotion controller for quadrupedal robots that overcomes limitations of previous approaches and enables robust traversal of harsh natural terrain at ...
- **p. 3 / 1. INTRODUCTION - extractive body cue:** The elevation map serves as an abstraction layer between sensors and the locomotion controller, making our method independent of depth sensor choices.
- **p. 8 / 4. MATERIALS AND METHODS - extractive body cue:** Overview We train a neural network policy in simulation and then perform zeroshot sim-to-real transfer.
- **p. 8 / 4. MATERIALS AND METHODS - extractive body cue:** First, a teacher policy is trained with RL to follow a random target velocity over randomly generated terrain with random disturbances.
- **p. 10 / 1. Teacher policy training - extractive body cue:** Height scan Proprioception Privileged info Teacher Policy Action joint difference phase difference

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The controller gets onboard sensor observations and a desired velocity command, and outputs each joint's target position as the action. | proprioception, terrain/perception observation과 velocity command | p. 3 (1. INTRODUCTION), p. 3 (1. INTRODUCTION) |
| State/latent | controller, gets, onboard, sensor, observations, desired, velocity, command, outputs, joint, target, position | body/contact state, foothold 또는 behavior mode | p. 3 (1. INTRODUCTION), p. 3 (1. INTRODUCTION), p. 10 (1. Teacher policy training) |
| Output/action | The student policy learns to predict the teacher's optimal action given only partial and noisy observations of the environment. | joint target, torque, footstep 또는 locomotion action | p. 3 (1. INTRODUCTION), p. 10 (1. Teacher policy training), p. 8 (4. MATERIALS AND METHODS) |
| Objective/outcome | velocity/progress, stability, energy와 terrain generalization | velocity/progress, stability, energy와 terrain generalization | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- **p. 8 / 4. MATERIALS AND METHODS - extractive body cue:** Our method consists of three stages, illustrated in Figure 6.
- **p. 3 / 1. INTRODUCTION - extractive body cue:** Here we present a terrain-aware locomotion controller for quadrupedal robots that overcomes limitations of previous approaches and enables robust traversal of harsh natural terrain at ...
- **p. 3 / 1. INTRODUCTION - extractive body cue:** The elevation map serves as an abstraction layer between sensors and the locomotion controller, making our method independent of depth sensor choices.
- **p. 5 / 2. RESULTS - extractive body cue:** First, we compared the success rate of overcoming fixed-height steps as shown in Figure 4A.
- **p. 5 / 2. RESULTS - extractive body cue:** The success rate of the proprioceptive baseline dropped at 20 cm step height when the front legs started frequently getting stuck at the step (Figure ...
- **p. 3 / 2. RESULTS - extractive body cue:** Because of the exteroceptive perception, the robot could anticipate the terrain and adapt its motion to achieve fast and smooth walking.
- **p. 8 / 2. RESULTS - extractive body cue:** The sensors perceived the foam block as solid and the robot consequently prepared to step on it but could not achieve a stable foothold due ...
- **p. 3 / 2. RESULTS - extractive body cue:** ANYmal successfully traversed challenging natural environments with steep inclination, slippery surfaces, grass, and snow (Figure 1 A-J).

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 5 (2. RESULTS), p. 5 (2. RESULTS) |
| Embodiment/environment | The robot perceives the environment in the form of height samples from an elevation map constructed from point cloud input, as seen in Figure 3A. | hardware/simulator version and reset protocol | p. 5 (2. RESULTS), p. 3 (2. RESULTS) |
| Dataset/benchmark | Because of the exteroceptive perception, the robot could anticipate the terrain and adapt its motion to achieve fast and smooth walking. | role, split, size and leakage | p. 5 (2. RESULTS), p. 3 (2. RESULTS), p. 3 (2. RESULTS), p. 5 (2. RESULTS) |
| Metric | First, we compared the success rate of overcoming fixed-height steps as shown in Figure 4A. | definition, denominator, direction and uncertainty | p. 5 (2. RESULTS), p. 5 (2. RESULTS), p. 8 (2. RESULTS) |
| Baseline/ablation | We compared our controller to a proprioceptive baseline [4] that does not use exteroception. | fair input/data/compute/action matching | p. 5 (2. RESULTS), p. 5 (2. RESULTS), p. 3 (2. RESULTS) |

## Explicit Limitations and Failure Boundary

- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 4. Internal belief state inspection during perceptive failure using a learned belief decoder. Red dots indicate height samples given as input to the policy. ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1. Robust locomotion in the wild. The presented locomotion controller was extensively tested in a variety of complex environments over multiple seasons. The controller ...
- **p. 13 / Figure/Table caption - extractive body cue:** Fig. 6. Details of robust terrain perception components. (A) During student training, random noise is added to the height samples. The noise is sampled from ...
- **p. 5 / 2. RESULTS - extractive body cue:** Until this height, the dominating failure reason was the robot evading the step sideways instead of falling.
- **p. 5 / 2. RESULTS - extractive body cue:** As shown in Figure 3 B-G, the estimated elevation map can unreliable due to sensing failures, limitations of the 2.5D height map representation, or viewpoint ...
- **p. 6 / 2. RESULTS - extractive body cue:** The controller is robust to many perception challenges commonly encountered in the field: missing map information due to sensing failure (B, C, G) and misleading ...
- **p. 8 / 3. DISCUSSION - extractive body cue:** Therefore, the policy assumes a continuous surface and, as a result, the robot might step off and fall.

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 locomotion 문제를 이해하기 위해 읽는다. 본문은 Most existing methods that rely on onboard terrain perception are still vulnerable to these failures.를 문제로 두고, Our method consists of three stages, illustrated in Figure 6.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. INTRODUCTION), p. 3 (1. INTRODUCTION), p. 3 (1. INTRODUCTION), p. 1 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 8 (4. MATERIALS AND METHODS) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
