# Learning Memory-Based Control for Human-Scale Bipedal Locomotion

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss16/p031.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss16/p031.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2020 / RSS
- Authors: Jonah Siekmann, Srikar Valluri, Jeremy Dao, Francis Bermillo, Helei Duan, Alan Fern, Jonathan Hurst
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: Robotics, bipedal locomotion, recurrent policy, sim-to-real, Reinforcement Learning
- Official paper: https://www.roboticsproceedings.org/rss16/p031.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss16/p031.pdf
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

Cassie 보행 실험은 순환 정책의 시뮬레이션 성능 이득이 실물로 전이되는 데 동역학 무작위화가 어떤 역할을 하는지 조사한다. [PDF 1쪽](https://www.roboticsproceedings.org/rss16/p031.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Controlling a non-statically stable biped is a difficult problem largely due to the complex hybrid dynamics involved.
- **p. 1 / Abstract - extractive body cue:** Recent work has demonstrated the effectiveness of reinforcement learning (RL) for simulation-based training of neural network controllers that successfully transfer to real bipeds.
- **p. 1 / Abstract - extractive body cue:** The existing work, however, has primarily used simple memoryless network architectures, even though more sophisticated architectures, such as those including memory, often yield superior performance ...
- **p. 1 / Abstract - extractive body cue:** In this work, we consider recurrent neural networks (RNNs) for sim-to-real biped locomotion, allowing for policies that learn to use internal memory to model important ...
- **p. 1 / Abstract - extractive body cue:** We show that while RNNs are able to significantly outperform memoryless policies in simulation, they do not exhibit superior behavior on the real biped due ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** RNNs trained without dynamics randomization are unable to consistently transfer to hardware (failures darkened and overlaid with X), while the same RNNs, when trained with ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** A common way to help address this sim-to-real challenge is the use of dynamics randomization during simulation-based training.

## Core Idea

- 목표 전진 속도, 보행 위상의 사인·코사인, 추정한 몸체 방향·관절 위치·속도를 입력받아 모터 위치 목표를 낸다. [PDF 3쪽](https://www.roboticsproceedings.org/rss16/p031.pdf#page=3)
- **p. 2 / I. INTRODUCTION - extractive body cue:** One of the main contributions of our work is to demonstrate that this approach is highly effective for training RNN controllers for the Cassie biped.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We show that by randomizing a small number of dynamics parameters over reasonable ranges, the RNNs can be consistently trained in simulation and successfully transferred ...
- **p. 4 / III. METHOD - extractive body cue:** Optimize surrogate L wrt θ, using ˆs, ˆa, ˆA if KL(πθ(ˆs, ˆa), πθold(ˆs, ˆa)) > klthresh then break end if end for end for end ...
- **p. 4 / III. METHOD - extractive body cue:** Recurrent Proximal Policy Optimization We trained all policies with PPO, a model-free reinforcement learning algorithm.
- **p. 3 / III. METHOD - extractive body cue:** Reward Design Our learning process makes use of a reference trajectory produced by an expert walking controller to help the policy learn in the initial ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 목표 전진 속도, 보행 위상의 사인·코사인, 추정한 몸체 방향·관절 위치·속도 | 49차원 정책 입력 | [PDF 3쪽](https://www.roboticsproceedings.org/rss16/p031.pdf#page=3) |
| State/latent | LSTM의 순환 상태 | 기억 없는 정책과 비교 | [PDF 4쪽](https://www.roboticsproceedings.org/rss16/p031.pdf#page=4) |
| Output/action | 중립 자세에 더할 모터 위치 목표 | 약 33 Hz 정책과 2 kHz 관절 PD 제어 | [PDF 3쪽](https://www.roboticsproceedings.org/rss16/p031.pdf#page=3) |
| Objective/outcome | All policies were trained to maximize the following reward function: R =0.20 · exp(-qerr) +0.20 · exp(-˙xerr) +0.05 · exp(-xerr) +0.20 · exp(-˙yerr) +0.30 · exp(-orienterr) +0.05 · exp(-springerr) (1) qerr, ˙xerr, ... | velocity/progress, stability, energy와 terrain generalization | p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD) |

## Main Claims and Actual Contribution

- 전진 속도 명령·주기 신호·추정 로봇 상태를 받아 관절 위치 목표를 출력하는 순환 정책과 기억 없는 정책을 비교한다. [PDF 3쪽](https://www.roboticsproceedings.org/rss16/p031.pdf#page=3) · [PDF 4쪽](https://www.roboticsproceedings.org/rss16/p031.pdf#page=4)
- 숨은 상태가 동역학 정보를 담는지 분석하고 실물에서 학습 중 무작위화 여부에 따른 보행 차이를 측정한다. [PDF 5쪽](https://www.roboticsproceedings.org/rss16/p031.pdf#page=5) · [PDF 6쪽](https://www.roboticsproceedings.org/rss16/p031.pdf#page=6)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 5 (IV. RESULTS), p. 5 (IV. RESULTS) |
| Embodiment/environment | The LSTM achieves a much higher reward with remarkably little variance, but both networks perform roughly the same on hardware. | hardware/simulator version and reset protocol | p. 5 (IV. RESULTS), p. 5 (IV. RESULTS) |
| Dataset/benchmark | Simulation We trained ten LSTM networks and ten FF networks with dynamics randomization, and ten LSTM networks and ten FF networks without dynamics randomization, each with separate random seeds. | role, split, size and leakage | p. 5 (IV. RESULTS), p. 5 (IV. RESULTS), p. 4 (IV. RESULTS) |
| Metric | Feedforward networks obtain a notably lower reward, with high variance. | definition, denominator, direction and uncertainty | p. 5 (IV. RESULTS), p. 5 (IV. RESULTS), p. 4 (IV. RESULTS) |
| Baseline/ablation | Simulation We trained ten LSTM networks and ten FF networks with dynamics randomization, and ten LSTM networks and ten FF networks without dynamics randomization, each with separate random seeds. | fair input/data/compute/action matching | p. 4 (IV. RESULTS), p. 5 (IV. RESULTS), p. 5 (IV. RESULTS) |

## Explicit Limitations and Failure Boundary

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We use recurrent neural networks and dynamics randomization to greatly improve the sim-to-real transfer rate and demonstrate learned, memory-based control on the bipedal ...
- **p. 6 / V. CONCLUSION - extractive body cue:** The policies were learned and tested first in simulation, then transferred to the robot, demonstrating the robustness and promise of this approach.
- **p. 5 / IV. RESULTS - extractive body cue:** We conducted a robustness test in simulation across ten chosen sets of dynamics, taken from the range in Table I.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 4 (III. METHOD), p. 3 (III. METHOD)이다.
