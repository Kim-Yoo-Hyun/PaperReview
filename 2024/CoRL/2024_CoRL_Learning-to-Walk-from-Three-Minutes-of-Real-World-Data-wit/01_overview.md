# Learning to Walk from Three Minutes of Real-World Data with Semi-structured Dynamics Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v270/levy25a.html.
> PDF retrieval source: https://arxiv.org/pdf/2410.09163. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CoRL
- Authors: Jacob Levy, Tyler Westenbroek, David Fridovich-Keil
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: Robotics, locomotion, model-based reinforcement learning, real-world learning
- Official paper: https://proceedings.mlr.press/v270/levy25a.html
- Full-text retrieval: https://arxiv.org/pdf/2410.09163
- Code/Project: https://sites.google.com/utexas.edu/ssrl
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0)

> DOC-QA2 targeted source review: 2026-10-23; PDF pp. 14. 손상 구간·직접 연결된 표 분류만 원문 이미지와 대조했다. 전체 주장 정독·실험 검증·reading status 승격을 뜻하지 않는다. [URL·PDF hash·수정 기록](../../../work/sources/pdf_note_review_followup_2026-10-23.json).

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
| Objective/outcome | Table 3은 step reward의 weighted sum을 정의한다. Forward velocity vₓ 가중치 0.42, yaw-rate exp(−ω_z²/0.2) 0.11, roll/pitch exp(−φ²/0.25) 각각 0.05이며 자세·속도·가속도·energy·torque 제한 항을 함께 사용한다. | 학습 reward 구성; 독립적인 terrain generalization 결과가 아님 | PDF p. 14 Appendix A.2 Table 3 |

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
- **PDF p. 14, Appendix A.2 Eq. (7) (DOC-QA2 원문 대조):** Termination flag dₜ=1은 base roll 절댓값 또는 pitch 절댓값이 π/4를 넘는 경우이며, 그 외에는 0이다. 낙상 이후 reward 누적을 중단하는 규칙이다.
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 8: Our approach is robust to errors in a priori knowledge of the robot's inertial properties. B.4 Modeling Uncertainty Here, we examine the benefit ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2: The SSRL framework. A deterministic policy is used to collect data from the real world while a stochastic policy is utilized in conjunction ...
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 7: Prediction error for 20-step synthetic rollouts using our semi-structured dynamics models and the black-box models where the best results from the 1- or ...
- **p. 17 / Figure/Table caption - extractive body cue:** Figure 9: Training performance when removing the noise estimators and removing both the noise estimators and ensemble. B.5 Additional Simulated Terrain Experiments To further demonstrate ...

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 locomotion 문제를 이해하기 위해 읽는다. 본문은 However, in practice, the black-box neural network models favored in the ∗These ...
