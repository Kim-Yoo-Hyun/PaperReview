# Learning Robust Perceptive Locomotion for Quadrupedal Robots in the Wild

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2201.08117.
> PDF retrieval source: https://arxiv.org/pdf/2201.08117. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2022 / Science Robotics
- Authors: Takahiro Miki, Joonho Lee, Jemin Hwangbo, Lorenz Wellhausen, Vladlen Koltun, Marco Hutter
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: Robotics, quadruped locomotion, perception, rough terrain
- Official paper: https://arxiv.org/abs/2201.08117
- Full-text retrieval: https://arxiv.org/pdf/2201.08117
- Code/Project: https://leggedrobotics.github.io/rl-perceptiveloco/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

이 연구는 지형 관측의 신뢰도가 달라질 때 자기수용감각과 외부 지각을 적응적으로 결합해 사족 로봇의 보행을 제어한다. [PDF 1쪽](https://arxiv.org/pdf/2201.08117v1#page=1)

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

- 순환 인코더의 내부 지형 추정을 학습하고 주의 기제로 외부 관측이 행동에 미치는 영향을 조절한다. [PDF 9쪽](https://arxiv.org/pdf/2201.08117v1#page=9) · [PDF 10쪽](https://arxiv.org/pdf/2201.08117v1#page=10)
- 산악 경로 주행과 지형 지도가 잘못되는 조건의 실험으로 시각 정보와 접촉 피드백의 역할을 평가한다. [PDF 4쪽](https://arxiv.org/pdf/2201.08117v1#page=4) · [PDF 6쪽](https://arxiv.org/pdf/2201.08117v1#page=6)

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

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. INTRODUCTION), p. 3 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 8 (4. MATERIALS AND METHODS)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (22 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Endowing legged robots with this ability is a grand challenge in robotics. (p. 1, 1. INTRODUCTION).
- **Actual contribution:** Here we present a terrain-aware locomotion controller for quadrupedal robots that overcomes limitations of previous approaches and enables robust traversal of harsh natural terrain at unprecedented speeds (Movie 1). (p. 3, 1. INTRODUCTION).
- **Evaluation boundary:** First, we compared the success rate of overcoming fixed-height steps as shown in Figure 4A. (p. 5, 2. RESULTS).
- **Explicit failure boundary:** Large noise magnitude for each scan point to simulate complete lack of terrain information due to occlusion or mapping failure. (p. 12, 2. Perturbing the height values).
