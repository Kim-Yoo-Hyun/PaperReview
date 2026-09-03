# Learning to Walk from Three Minutes of Real-World Data with Semi-structured Dynamics Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=evCXwlCMIi.
> PDF retrieval source: https://arxiv.org/pdf/2410.09163. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: Robotics, locomotion, model-based reinforcement learning, real-world learning
- Official paper: https://openreview.net/forum?id=evCXwlCMIi
- Full-text retrieval: https://arxiv.org/pdf/2410.09163
- Code/Project: https://sites.google.com/utexas.edu/ssrl
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 locomotion 문제를 이해하기 위해 읽는다. 본문은 However, in practice, the black-box neural network models favored in the ∗These ...

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Traditionally, model-based reinforcement learning (MBRL) methods exploit neural networks as flexible function approximators to represent a priori unknown environment dynamics.
- **p. 1 / Abstract - extractive body cue:** However, training data are typically scarce in practice, and these black-box models often fail to generalize.
- **p. 1 / Abstract - extractive body cue:** Modeling architectures that leverage known physics can substantially reduce the complexity of system-identification, but break down in the face of complex phenomena such as contact.
- **p. 1 / Abstract - extractive body cue:** We introduce a novel framework for learning semi-structured dynamics models for contact-rich systems which seamlessly integrates structured first principles modeling techniques with black-box auto-regressive models.
- **p. 1 / Abstract - extractive body cue:** Specifically, we develop an ensemble of probabilistic models to estimate external forces, conditioned on historical observations and actions, and integrate these predictions using known Lagrangian ...
- **p. 1 / 1 Introduction - extractive body cue:** However, in practice, the black-box neural network models favored in the ∗These ...
- **p. 6 / 1 Introduction - extractive body cue:** Predictions from semi-structured dynamics models demonstrate greater accuracy and improved generalization beyond training data compared to black-box models.

## Core Idea

- **p. 6 / 1 Introduction - extractive body cue:** This, when combined with the accuracy of our predictions over long-horizons (Section 4.2) provides insight into why our approach enables such effective policy optimization [38].
- **p. 3 / 1 Introduction - extractive body cue:** The space of observations Ωconsists of the states that can be measured, and the observation distribution O(·/st, at, et) provides (noisy) estimates of the states ...
- **p. 4 / 1 Introduction - extractive body cue:** 3 Semi-structured Reinforcement Learning A high-level overview of our method is presented in Fig.
- **p. 5 / 1 Introduction - extractive body cue:** 3.4 Policy Optimization Finally, we introduce the Semi-Structured Reinforcement Learning (SSRL) in Algorithm 2.
- **p. 7 / 1 Introduction - extractive body cue:** Right-Prediction error for 20-step synthetic rollouts in an unseen environment showcases our method's superior ability to generalize.
- **p. 14 / A.3 Control Architecture - extractive body cue:** The desired joint angles are sent to the joint level PD controllers, where the desired torque outputs are: τt = Kp(qdes -qj) -Kp ˙qj, (11) ...
- **p. 14 / A.3 Control Architecture - extractive body cue:** Referring to the action space definition Table 2, the policy takes in the current observation and a history of observations and outputs offsets to foot ...
- **p. 13 / A.1 Observation and Action Spaces - extractive body cue:** The observation space Ω⊂R36 consists of the elements in Table 1.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Algorithm 1 Auto-Regressive State Predictions 1: Inputs hallucination buffer Dmodel, models {ˆpi ψi}, policy πθ, start state s0, start history h0 2: for t = 0 . . . k -1 do ... | proprioception, terrain/perception observation과 velocity command | p. 5 (1 Introduction), p. 14 (A.3 Control Architecture) |
| State/latent | Algorithm, Auto-Regressive, State, Predictions, Inputs, hallucination, buffer, Dmodel, models, policy, start, history | body/contact state, foothold 또는 behavior mode | p. 5 (1 Introduction), p. 14 (A.3 Control Architecture), p. 3 (1 Introduction) |
| Output/action | Referring to the action space definition Table 2, the policy takes in the current observation and a history of observations and outputs offsets to foot positions and a nominal height for the ... | joint target, torque, footstep 또는 locomotion action | p. 14 (A.3 Control Architecture), p. 3 (1 Introduction), p. 4 (1 Introduction) |
| Objective/outcome | Reward Term Expression Weight Maximize forward velocity vx t+1 0.42 Limit base yaw rate exp  -(ωz t+1)2/0.2  0.11 Limit base roll exp  -(φx t+1)2/0.25  0.05 Limit base pitch ... | velocity/progress, stability, energy와 terrain generalization | p. 14 (A.2 Reward Function and Termination Condition), p. 13 (A.2 Reward Function and Termination Condition), p. 13 (A Implementation Details) |

## Main Claims and Actual Contribution

- **p. 6 / 1 Introduction - extractive body cue:** This, when combined with the accuracy of our predictions over long-horizons (Section 4.2) provides insight into why our approach enables such effective policy optimization [38].
- **p. 3 / 1 Introduction - extractive body cue:** The space of observations Ωconsists of the states that can be measured, and the observation distribution O(·/st, at, et) provides (noisy) estimates of the states ...
- **p. 4 / 1 Introduction - extractive body cue:** 3 Semi-structured Reinforcement Learning A high-level overview of our method is presented in Fig.
- **p. 5 / 1 Introduction - extractive body cue:** 3.4 Policy Optimization Finally, we introduce the Semi-Structured Reinforcement Learning (SSRL) in Algorithm 2.
- **p. 7 / 1 Introduction - extractive body cue:** Right-Prediction error for 20-step synthetic rollouts in an unseen environment showcases our method's superior ability to generalize.
- **p. 18 / Figure/Table caption - extractive body cue:** Figure 12: Simulated benchmark results. Better performance is achieved when using our semi- structured dynamics models and a multi-step loss. Plots show the mean and ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2: The SSRL framework. A deterministic policy is used to collect data from the real world while a stochastic policy is utilized in conjunction ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Real-world results. Left-SSRL efficiently performs policy optimization, even when data is scarce. Center-With our approach, the quadruped steadily learns to walk faster. Right-Predicted ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 18 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Embodiment/environment | not recovered | hardware/simulator version and reset protocol | 본문 anchor 없음 |
| Dataset/benchmark | not recovered | role, split, size and leakage | 본문 anchor 없음 |
| Metric | Figure 7: Prediction error for 20-step synthetic rollouts using our semi-structured dynamics models and the black-box models where the best results from the 1- or 4- step losses are presented. Pre- diction ... | definition, denominator, direction and uncertainty | p. 16 (Figure/Table caption), p. 18 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Baseline/ablation | Figure 5: Left-SSRL achieves better policy performance compared to a baseline using black-box models. Right-Prediction error for 20-step synthetic rollouts in an unseen environment showcases our method's supe- rior ability to generalize ... | fair input/data/compute/action matching | p. 7 (Figure/Table caption), p. 2 (Figure/Table caption), p. 7 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5 Related Work - extractive body cue:** However there are several key limitations.
- **p. 8 / 5 Related Work - extractive body cue:** 6 Limitations This paper presents a novel framework for model-based reinforcement learning, which leverages physics-informed, semi-structured dynamics models to enable highly sample-efficient policy learning in ...
- **p. 14 / A.2 Reward Function and Termination Condition - extractive body cue:** The termination flag dt stops the accumulation of reward after the quadruped falls and is defined by: dt = 1 if /φx t / > ...
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 8: Our approach is robust to errors in a priori knowledge of the robot's inertial properties. B.4 Modeling Uncertainty Here, we examine the benefit ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2: The SSRL framework. A deterministic policy is used to collect data from the real world while a stochastic policy is utilized in conjunction ...
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 7: Prediction error for 20-step synthetic rollouts using our semi-structured dynamics models and the black-box models where the best results from the 1- or ...
- **p. 17 / Figure/Table caption - extractive body cue:** Figure 9: Training performance when removing the noise estimators and removing both the noise estimators and ensemble. B.5 Additional Simulated Terrain Experiments To further demonstrate ...

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 locomotion 문제를 이해하기 위해 읽는다. 본문은 However, in practice, the black-box neural network models favored in the ∗These ...
