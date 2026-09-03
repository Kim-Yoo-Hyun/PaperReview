# Bridging the Sim-to-Real Gap for Athletic Loco-Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p125.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p125.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: Robotics, quadruped locomotion, loco-manipulation, sim-to-real
- Official paper: https://www.roboticsproceedings.org/rss21/p125.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p125.pdf
- Code/Project: https://www.roboticsproceedings.org/rss21/p125.html
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 locomotion 문제를 이해하기 위해 읽는다. 본문은 However, training solely with task rewards introduces two major challenges: these rewards are prone (o exploitation (reward hacking), and the exploration process can lack sufficient direction.를 문제로 두고, Rather than enforcing strict adherence to a reference trajectory, we propose treating it as a hint to guide exploration, In our approach, « WBC is frst pre-trained on random base velocities and ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Body text (section not recovered) - extractive body cue.
- **p. 1 / Body text (section not recovered) - extractive body cue:** Bridging the Sim-to-Real Gap for Athletic Loco-Manipulation
- **p. 1 / Body text (section not recovered) - extractive body cue:** Improbable Al Lab.
- **p. 1 / Body text (section not recovered) - extractive body cue:** Achieving athletic loco-manipulation on robots requires moving beyond traditional tracking rewards-which simply guide the robot along a reference trajectory-to task rewards that drive truly dynamic, ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** Commands such as "throw the ball as far as you can" or "lift the weight as quickly as possible" compel the robot to exhibit the ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** However, training solely with task rewards introduces two major challenges: these rewards are prone (o exploitation (reward hacking), and the exploration process can lack sufficient ...
- **p. 1 / 1. Iyrropucrion - extractive body cue:** However, these task rewards pose two major challenges: (i) they are prone 10 reward hacking, where the policy exploits imperfections in the simulation, and (i) ...

## Core Idea

- **p. 2 / 1. Iyrropucrion - extractive body cue:** Rather than enforcing strict adherence to a reference trajectory, we propose treating it as a hint to guide exploration, In our approach, « WBC is ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** First, we introduce the Un= supervised Actuator Net (UAN), which leverages real-world data {o bridge the sim-to-real gap for complex actuation mechanisms without requiring access ...
- **p. 2 / A. Unsupervised Actuator Net - extractive body cue:** Alternatively, we propose a method for matching the transition dynamics of the actuator such that
- **p. 3 / A. Unsupervised Actuator Net - extractive body cue:** Each training episode consists of a 20s rollout executing the torque sequence from the hardware data from 3, t0 8744.20 Through taining on rollouts, the ...
- **p. 3 / B. Whole-body Controller Pre-training - extractive body cue:** 2) Observation Space: ‘The policy's observation space consists of proprioceptive readings from the robot's onboard sen= sors including the gravity vector projected in the robot's ...
- **p. 5 / A. Comparing System Identification Approaches - extractive body cue:** We first evaluate the modeling accuracy of these approaches by reporting the mean-square joint position error on both the training data and on an unseen ...
- **p. 3 / B. Whole-body Controller Pre-training - extractive body cue:** 1) Policy Architecture: "The WBC is a control policy, a, = ro(Or-yc4)e Where the action at time f, ay, is a vector of position targets ...
- **p. 5 / A. Comparing System Identification Approaches - extractive body cue:** We compare several methods for modeling the actuator dynamics of the Unitree Z1 Pro arm in Isaac Sim.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 2) Observation Space: ‘The policy's observation space consists of proprioceptive readings from the robot's onboard sen= sors including the gravity vector projected in the robot's body frame g, a base velocity command ... | proprioception, terrain/perception observation과 velocity command | p. 3 (B. Whole-body Controller Pre-training), p. 3 (B. Whole-body Controller Pre-training) |
| State/latent | Observation, Space, policy, consists, proprioceptive, readings, robot, onboard, sors, including, gravity, vector | body/contact state, foothold 또는 behavior mode | p. 3 (B. Whole-body Controller Pre-training), p. 3 (B. Whole-body Controller Pre-training), p. 2 (1. Iyrropucrion) |
| Output/action | 1) Policy Architecture: "The WBC is a control policy, a, = ro(Or-yc4)e Where the action at time f, ay, is a vector of position targets for each ofthe robots joints and oy ... | joint target, torque, footstep 또는 locomotion action | p. 3 (B. Whole-body Controller Pre-training), p. 2 (1. Iyrropucrion), p. 4 (B. Whole-body Controller Pre-training) |
| Objective/outcome | The EE tracking term rewards ‘minimizing the distance between four key points, where one key point is positioned at the frame's origin, and the others are positioned along each axis of the ... | velocity/progress, stability, energy와 terrain generalization | p. 4 (B. Whole-body Controller Pre-training), p. 4 (B. Whole-body Controller Pre-training), p. 5 (A. Comparing System Identification Approaches) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Iyrropucrion - extractive body cue:** Rather than enforcing strict adherence to a reference trajectory, we propose treating it as a hint to guide exploration, In our approach, « WBC is ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** First, we introduce the Un= supervised Actuator Net (UAN), which leverages real-world data {o bridge the sim-to-real gap for complex actuation mechanisms without requiring access ...
- **p. 2 / A. Unsupervised Actuator Net - extractive body cue:** Alternatively, we propose a method for matching the transition dynamics of the actuator such that
- **p. 3 / A. Unsupervised Actuator Net - extractive body cue:** Each training episode consists of a 20s rollout executing the torque sequence from the hardware data from 3, t0 8744.20 Through taining on rollouts, the ...
- **p. 3 / B. Whole-body Controller Pre-training - extractive body cue:** 2) Observation Space: ‘The policy's observation space consists of proprioceptive readings from the robot's onboard sen= sors including the gravity vector projected in the robot's ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: UAN improves simulator accuracy and real throwing performance. UAN (Ours) achieves lower sim-to-real difference in throw distance as compared to standard baselines, resulting ...
- **p. 5 / A. Comparing System Identification Approaches - extractive body cue:** We first evaluate the modeling accuracy of these approaches by reporting the mean-square joint position error on both the training data and on an unseen ...
- **p. 6 / B. Finetuning Foundational WBC - extractive body cue:** We found that No-Pre-Training achieved similar throwing performance to No-E2E, despite hitting a larger peak power ouput

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 5 (Figure/Table caption), p. 5 (A. Comparing System Identification Approaches) |
| Embodiment/environment | On hardware, the ball was thrown approximately 20m, with the real robot throwing slightly further than in simulation - possibly due to inaccuracies in the ball-bucket contact modeling. | hardware/simulator version and reset protocol | p. 6 (B. Finetuning Foundational WBC), p. 3 (A. Unsupervised Actuator Net) |
| Dataset/benchmark | 2) Data collection: We collect data on real hardware to construct a dataset of transitions {(s1.74,S+.1),}\g fom each actuator. | role, split, size and leakage | p. 6 (B. Finetuning Foundational WBC), p. 3 (A. Unsupervised Actuator Net), p. 3 (A. Unsupervised Actuator Net), p. 4 (B. Whole-body Controller Pre-training) |
| Metric | We first evaluate the modeling accuracy of these approaches by reporting the mean-square joint position error on both the training data and on an unseen test trajectory (see Figure 6) ur results ... | definition, denominator, direction and uncertainty | p. 5 (A. Comparing System Identification Approaches), p. 5 (Figure/Table caption), p. 4 (B. Whole-body Controller Pre-training) |
| Baseline/ablation | Fig. 4: UAN improves simulator accuracy and real throwing performance. UAN (Ours) achieves lower sim-to-real difference in throw distance as compared to standard baselines, resulting in a better real throw distance. For ... | fair input/data/compute/action matching | p. 5 (Figure/Table caption), p. 5 (A. Comparing System Identification Approaches), p. 6 (A. Comparing System Identification Approaches) |

## Explicit Limitations and Failure Boundary

- **p. 5 / A. Arm Modifications - extractive body cue:** During development, the Unitree ZI Pro arm experienced structural failures at inks 2 and 4, with minor deformations at Tink 5.
- **p. 6 / A. Comparing System Identification Approaches - extractive body cue:** Meanwhile, the Default, DR, and ROA policies produced unstable behaviors-the Default policy, for instance, strayed excessively and failed to throw the bull at all.
- **p. 7 / A. Whole-Body Control - extractive body cue:** ‘To avoid the reliance on high-quality pre-training, another possibility is to discard the explicit notion of reference trajectories altogether and directly train end-to-end policies for ...
- **p. 5 / C. Task-Specific Finetuning - extractive body cue:** For this comparison, wwe train and test policies with a fixed-base arm, to avoid the risk of the legged base falling during performance-critical ablations,
- **p. 7 / B. Finetuning Foundational WBC - extractive body cue:** Since the robot's arm is much weaker than the legs, the policy learns to pitch its base backwards to swing the weight upwards into the ...
- **p. 6 / A. Comparing System Identification Approaches - extractive body cue:** As shown by Figure 6, UAN can even accurately capture the arm's response to Gaussian noise control input, which is commonly used for exploration in ...
- **p. 3 / B. Whole-body Controller Pre-training - extractive body cue:** The value function approximator network has the same architecture but does not share weights with the policy.

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 locomotion 문제를 이해하기 위해 읽는다. 본문은 However, training solely with task rewards introduces two major challenges: these rewards are prone (o exploitation (reward hacking), and the exploration process can lack sufficient direction.를 문제로 두고, Rather than enforcing strict adherence to a reference trajectory, we propose treating it as a hint to guide exploration, In our approach, « WBC is frst pre-trained on random base velocities and ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (Body text (section not recovered)), p. 1 (1. Iyrropucrion), p. 2 (1. Iyrropucrion), p. 2 (1. Iyrropucrion), p. 3 (A. Unsupervised Actuator Net), p. 3 (B. Whole-body Controller Pre-training) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
