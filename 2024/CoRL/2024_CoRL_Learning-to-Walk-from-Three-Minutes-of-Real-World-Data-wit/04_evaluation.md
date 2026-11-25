# Evaluation - Learning to Walk from Three Minutes of Real-World Data with Semi-structured Dynamics Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v270/levy25a.html; PDF retrieval source: https://arxiv.org/pdf/2410.09163. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA2 targeted source review: 2026-10-23; PDF pp. 14. 손상 구간·직접 연결된 표 분류만 원문 이미지와 대조했다. 전체 주장 정독·실험 검증·reading status 승격을 뜻하지 않는다. [URL·PDF hash·수정 기록](../../../work/sources/pdf_note_review_followup_2026-10-23.json).

## Evaluation in One Sentence

3분은 Go1에서 수집한 실제 상호작용 데이터의 길이다. 각 지면에서 3분의 자료를 쓴 뒤 평균 전진 속도는 단단한 바닥 0.98 m/s, 메모리폼 0.53 m/s였다. [PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/levy25a/levy25a.pdf#page=6) · [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/levy25a/levy25a.pdf#page=7)

## Evaluation Body Digest

- **p. 16 / Figure/Table caption - extractive body cue:** Figure 7: Prediction error for 20-step synthetic rollouts using our semi-structured dynamics models and the black-box models where the best results from the 1- or ...
- **p. 18 / Figure/Table caption - extractive body cue:** Figure 12: Simulated benchmark results. Better performance is achieved when using our semi- structured dynamics models and a multi-step loss. Plots show the mean and ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: Left-SSRL achieves better policy performance compared to a baseline using black-box models. Right-Prediction error for 20-step synthetic rollouts in an unseen environment showcases ...
- **PDF p. 14, Appendix A.2 Table 3 (DOC-QA2 원문 대조):** Table 3은 step reward의 weighted sum을 정의한다. Forward velocity vₓ 가중치 0.42, yaw-rate exp(−ω_z²/0.2) 0.11, roll/pitch exp(−φ²/0.25) 각각 0.05이며 자세·속도·가속도·energy·torque 제한 항을 함께 사용한다.
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 6: Predicted external forces and actual external force estimates over one second of real-world data for the floating base and the joints of the ...
- **p. 13 / A.2 Reward Function and Termination Condition - extractive body cue:** The reward function is a weighted sum of the terms in Table 3.
- **p. 13 / A Implementation Details - extractive body cue:** In this appendix, we provide details of our implementation for the Unitree Go1 Quadruped, including the observation and action spaces, the reward function, the termination ...
- **p. 14 / A.2 Reward Function and Termination Condition - extractive body cue:** The reward at each time step is a weighted sum of these terms.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** legged robot, terrain과 contact dynamics.
- **Input boundary:** proprioception, terrain/perception observation과 velocity command.
- **Output/decision under evaluation:** joint target, torque, footstep 또는 locomotion action.
- **Primary target:** velocity/progress, stability, energy와 terrain generalization.
- **Detected evaluation headings:** A Implementation Details (p. 13); B Additional Experiments (p. 15); B.5 Additional Simulated Terrain Experiments (p. 17); C Simulated Benchmark Experiments (p. 18).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 12: Simulated benchmark results. Better performance is achieved when using our semi- structured dynamics models and a multi-step loss. Plots show the mean ... | p. 18 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 5: Left-SSRL achieves better policy performance compared to a baseline using black-box models. Right-Prediction error for 20-step synthetic rollouts in an unseen environment ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 2: The SSRL framework. A deterministic policy is used to collect data from the real world while a stochastic policy is utilized in ... | p. 2 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 4: Real-world results. Left-SSRL efficiently performs policy optimization, even when data is scarce. Center-With our approach, the quadruped steadily learns to walk faster. ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 7: Prediction error for 20-step synthetic rollouts using our semi-structured dynamics models and the black-box models where the best results from the 1- ... | p. 16 (Figure/Table caption) |

## Dataset / Benchmark Role

- dataset/benchmark/environment role cue 없음

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Unitree Go1 quadruped learning to walk from scratch using SSRL on hard ground (left) and memory foam (right). 1
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2: The SSRL framework. A deterministic policy is used to collect data from the real world while a stochastic policy is utilized in conjunction ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3: Control architecture. The policy takes in a history of observations and outputs parameters to a gait generator and offsets to the gait. The ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Real-world results. Left-SSRL efficiently performs policy optimization, even when data is scarce. Center-With our approach, the quadruped steadily learns to walk faster. Right-Predicted ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: Left-SSRL achieves better policy performance compared to a baseline using black-box models. Right-Prediction error for 20-step synthetic rollouts in an unseen environment showcases ...
- **p. 13 / Figure/Table caption - extractive body cue:** Table 1: Observation space. The action space A ⊂R9 outputs the change in nominal height for the gait generator and offsets to nominal foot positions ...
- **p. 13 / Figure/Table caption - extractive body cue:** Table 2: Action space. A.2 Reward Function and Termination Condition Reward Function. The reward function is a weighted sum of the terms in Table 3. ...
- **p. 14 / Figure/Table caption - extractive body cue:** Table 3: Reward function terms. The reward at each time step is a weighted sum of these terms. Termination Condition. The termination flag dt stops ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | not recovered | embodiment, simulator version and control stack | 본문 anchor 없음 |
| Task/environment | not recovered | reset, timeout, object/scene variation | 본문 anchor 없음 |
| Observation/sensor | proprioception, terrain/perception observation과 velocity command | calibration, preprocessing, privileged input | p. 5 (1 Introduction), p. 14 (A.3 Control Architecture) |
| Output/decision | joint target, torque, footstep 또는 locomotion action | action frame, controller and termination | p. 3 (1 Introduction), p. 4 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 7: Prediction error for 20-step synthetic rollouts using our semi-structured dynamics models and the black-box models where the best results from the 1- ... | definition/direction/unit from same section | p. 16 (Figure/Table caption) |
| Figure 12: Simulated benchmark results. Better performance is achieved when using our semi- structured dynamics models and a multi-step loss. Plots show the mean ... | definition/direction/unit from same section | p. 18 (Figure/Table caption) |
| Figure 5: Left-SSRL achieves better policy performance compared to a baseline using black-box models. Right-Prediction error for 20-step synthetic rollouts in an unseen environment ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Table 3은 step reward의 weighted sum을 정의한다. Forward velocity vₓ 가중치 0.42, yaw-rate exp(−ω_z²/0.2) 0.11, roll/pitch exp(−φ²/0.25) 각각 0.05이며 자세·속도·가속도·energy·torque 제한 항을 함께 사용한다. | Reward specification; reported evaluation metric과 구분 | PDF p. 14 Table 3 |
| Figure 6: Predicted external forces and actual external force estimates over one second of real-world data for the floating base and the joints of ... | definition/direction/unit from same section | p. 15 (Figure/Table caption) |
| The reward function is a weighted sum of the terms in Table 3. | definition/direction/unit from same section | p. 13 (A.2 Reward Function and Termination Condition) |
| In this appendix, we provide details of our implementation for the Unitree Go1 Quadruped, including the observation and action spaces, the reward function, the ... | definition/direction/unit from same section | p. 13 (A Implementation Details) |
| The reward at each time step is a weighted sum of these terms. | definition/direction/unit from same section | p. 14 (A.2 Reward Function and Termination Condition) |

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 5: Left-SSRL achieves better policy performance compared to a baseline using black-box models. Right-Prediction error for 20-step synthetic rollouts in an unseen environment ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Figure 2: The SSRL framework. A deterministic policy is used to collect data from the real world while a stochastic policy is utilized in ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |
| Figure 4: Real-world results. Left-SSRL efficiently performs policy optimization, even when data is scarce. Center-With our approach, the quadruped steadily learns to walk faster. ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Figure 10: Training performance of our method with varying simulated contact conditions. B.6 SAC Performance State-of-the-art real-world quadrupedal locomotion results where policies are trained ... | comparison identity and matched condition | p. 17 (Figure/Table caption) |
| Table 4: Hyperparameters for our approach and the baseline approach with black-box models. x → y over epochs a →b denotes a clipped linear ... | comparison identity and matched condition | p. 19 (Figure/Table caption) |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 9: Training performance when removing the noise estimators and removing both the noise estimators and ensemble. B.5 Additional Simulated Terrain Experiments To further ... | component/input/data sensitivity | p. 17 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| This, when combined with the accuracy of our predictions over long-horizons (Section 4.2) provides insight into why our approach enables such effective policy optimization ... | Figure 12: Simulated benchmark results. Better performance is achieved when using our semi- structured dynamics models and a multi-step loss. Plots show the mean ... | PDF body cue; verify exact table/figure and matched conditions | p. 18 (Figure/Table caption), p. 7 (Figure/Table caption), p. 2 (Figure/Table caption), p. 7 (Figure/Table caption), p. 16 (Figure/Table caption), p. 17 (Figure/Table caption) |
| Primary metric/result | Figure 5: Left-SSRL achieves better policy performance compared to a baseline using black-box models. Right-Prediction error for 20-step synthetic rollouts in an unseen environment ... | numeric claim only at cited anchor | p. 7 (Figure/Table caption) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | However there are several key limitations. | p. 8 (5 Related Work) |
| body limitation/failure cue | 6 Limitations This paper presents a novel framework for model-based reinforcement learning, which leverages physics-informed, semi-structured dynamics models to enable highly sample-efficient policy learning ... | p. 8 (5 Related Work) |
| Termination rule | Roll 또는 pitch 절댓값>π/4이면 dₜ=1, 그 외 0. 정의된 termination 조건이며 관측된 failure 빈도는 아니다. | PDF p. 14 Eq. (7) |
| body limitation/failure cue | Figure 8: Our approach is robust to errors in a priori knowledge of the robot's inertial properties. B.4 Modeling Uncertainty Here, we examine the ... | p. 16 (Figure/Table caption) |
| body limitation/failure cue | Figure 2: The SSRL framework. A deterministic policy is used to collect data from the real world while a stochastic policy is utilized in ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | Figure 7: Prediction error for 20-step synthetic rollouts using our semi-structured dynamics models and the black-box models where the best results from the 1- ... | p. 16 (Figure/Table caption) |

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| In this appendix, we provide details of our implementation for the Unitree Go1 Quadruped, including the observation and action spaces, the reward function, the ... | p. 13 (A Implementation Details) |
| For each foot, the desired foot positions (10) are computed and sent to an inverse kinematics solver to produce desired joint angles qdes ∈R12. | p. 14 (A.3 Control Architecture) |

## Limitations and Verification Questions

- **p. 8 / 5 Related Work - extractive body cue:** However there are several key limitations.
- **p. 8 / 5 Related Work - extractive body cue:** 6 Limitations This paper presents a novel framework for model-based reinforcement learning, which leverages physics-informed, semi-structured dynamics models to enable highly sample-efficient policy learning in ...
- **PDF p. 14, Appendix A.2 Eq. (7) (DOC-QA2 원문 대조):** Termination flag dₜ=1은 base roll 절댓값 또는 pitch 절댓값이 π/4를 넘는 경우이며, 그 외에는 0이다. 낙상 이후 reward 누적을 중단하는 규칙이다.
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 8: Our approach is robust to errors in a priori knowledge of the robot's inertial properties. B.4 Modeling Uncertainty Here, we examine the benefit ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2: The SSRL framework. A deterministic policy is used to collect data from the real world while a stochastic policy is utilized in conjunction ...
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 7: Prediction error for 20-step synthetic rollouts using our semi-structured dynamics models and the black-box models where the best results from the 1- or ...

- **Evidence anchors reviewed:** datasets 본문 anchor 없음, metrics p. 16 (Figure/Table caption), p. 18 (Figure/Table caption), p. 7 (Figure/Table caption), p. 14 (A.2 Reward Function and Termination Condition), p. 15 (Figure/Table caption), p. 13 (A.2 Reward Function and Termination Condition), baselines p. 7 (Figure/Table caption), p. 2 (Figure/Table caption), p. 7 (Figure/Table caption), p. 17 (Figure/Table caption), p. 19 (Figure/Table caption), results p. 18 (Figure/Table caption), p. 7 (Figure/Table caption), p. 2 (Figure/Table caption), p. 7 (Figure/Table caption), p. 16 (Figure/Table caption), p. 17 (Figure/Table caption).

[공통 검토 기준](../../../research/READING_STATUS.md#note-checks)
