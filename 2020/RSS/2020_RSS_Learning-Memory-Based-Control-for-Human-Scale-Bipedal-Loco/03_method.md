# Method - Learning Memory-Based Control for Human-Scale Bipedal Locomotion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss16/p031.html; PDF retrieval source: https://www.roboticsproceedings.org/rss16/p031.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD)): Optimize surrogate L wrt θ, using ˆs, ˆa, ˆA if KL(πθ(ˆs, ˆa), πθold(ˆs, ˆa)) > klthresh then break end if end for end for end for During training, we used ...

## Method Body Digest

- **p. 4 / III. METHOD - extractive body cue:** Optimize surrogate L wrt θ, using ˆs, ˆa, ˆA if KL(πθ(ˆs, ˆa), πθold(ˆs, ˆa)) > klthresh then break end if end for end for end ...
- 목표 전진 속도, 보행 위상의 사인·코사인, 추정한 몸체 방향·관절 위치·속도를 입력받아 모터 위치 목표를 낸다. [PDF 3쪽](https://www.roboticsproceedings.org/rss16/p031.pdf#page=3)
- **p. 4 / III. METHOD - extractive body cue:** Recurrent Proximal Policy Optimization We trained all policies with PPO, a model-free reinforcement learning algorithm.
- **p. 3 / III. METHOD - extractive body cue:** Reward Design Our learning process makes use of a reference trajectory produced by an expert walking controller to help the policy learn in the initial ...
- **p. 3 / III. METHOD - extractive body cue:** All policies were trained to maximize the following reward function: R =0.20 · exp(-qerr) +0.20 · exp(-˙xerr) +0.05 · exp(-xerr) +0.20 · exp(-˙yerr) +0.30 · ...
- **p. 3 / III. METHOD - extractive body cue:** It is important to note that while the reward function is partially based on a reference motion, very similarly to Xie et al.
- **p. 4 / III. METHOD - extractive body cue:** However, correctly calculating the gradient of an RNN requires the use of the backpropagation through time (BPTT) algorithm, which necessitates special measures when sampling from ...
- **p. 4 / III. METHOD - extractive body cue:** The recurrent critic was also an LSTM network with two layers of 128 units each, with a single output representing the value function.

## Design Rationale

- 목표 전진 속도, 보행 위상의 사인·코사인, 추정한 몸체 방향·관절 위치·속도를 입력받아 모터 위치 목표를 낸다. [PDF 3쪽](https://www.roboticsproceedings.org/rss16/p031.pdf#page=3)
- **p. 2 / I. INTRODUCTION - extractive body cue:** One of the main contributions of our work is to demonstrate that this approach is highly effective for training RNN controllers for the Cassie biped.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We show that by randomizing a small number of dynamics parameters over reasonable ranges, the RNNs can be consistently trained in simulation and successfully transferred ...

## Source Evidence Cues

- **p. 4 / III. METHOD - extractive body cue:** Optimize surrogate L wrt θ, using ˆs, ˆa, ˆA if KL(πθ(ˆs, ˆa), πθold(ˆs, ˆa)) > klthresh then break end if end for end for end ...
- 목표 전진 속도, 보행 위상의 사인·코사인, 추정한 몸체 방향·관절 위치·속도를 입력받아 모터 위치 목표를 낸다. [PDF 3쪽](https://www.roboticsproceedings.org/rss16/p031.pdf#page=3)
- **p. 4 / III. METHOD - extractive body cue:** Recurrent Proximal Policy Optimization We trained all policies with PPO, a model-free reinforcement learning algorithm.
- **p. 3 / III. METHOD - extractive body cue:** Reward Design Our learning process makes use of a reference trajectory produced by an expert walking controller to help the policy learn in the initial ...
- **Detected method headings:** III. METHOD (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| 입력 구성 | 명령과 로봇 상태를 결합한다 | 목표 전진 속도, 보행 위상의 사인·코사인, 추정한 몸체 방향·관절 위치·속도 | 49차원 입력 벡터 구성 | 정책 입력 | 본문 III-A | [PDF 3쪽](https://www.roboticsproceedings.org/rss16/p031.pdf#page=3) |
| 관절 위치 정책 | 30 ms마다 목표를 갱신한다 | 정책 입력 및 이전 순환 상태 | LSTM 갱신 | 중립 자세에 더할 모터 위치 목표 | 그림 2 | [PDF 3쪽](https://www.roboticsproceedings.org/rss16/p031.pdf#page=3) |
| 관절 PD 제어 | 모터 위치를 추종한다 | 중립 자세를 더한 위치 목표와 센서 신호 | 2 kHz PD 제어 | 모터 토크 | 그림 2 | [PDF 3쪽](https://www.roboticsproceedings.org/rss16/p031.pdf#page=3) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / III. METHOD - extractive body cue:** All policies were trained to maximize the following reward function: R =0.20 · exp(-qerr) +0.20 · exp(-˙xerr) +0.05 · exp(-xerr) +0.20 · exp(-˙yerr) +0.30 · ...
- **p. 3 / III. METHOD - extractive body cue:** It is important to note that while the reward function is partially based on a reference motion, very similarly to Xie et al.
- **p. 4 / III. METHOD - extractive body cue:** However, correctly calculating the gradient of an RNN requires the use of the backpropagation through time (BPTT) algorithm, which necessitates special measures when sampling from ...
- **p. 4 / III. METHOD - extractive body cue:** The recurrent critic was also an LSTM network with two layers of 128 units each, with a single output representing the value function.
- 정책은 속도 지령·주기 신호·추정한 로봇 상태에서 관절 위치 목표를 낸다. 학습 보상에는 전진 속도·자세·관절의 참조 궤적 추종 오차가 들어간다. [PDF 3쪽](https://www.roboticsproceedings.org/rss16/p031.pdf#page=3)
- **Equation/algorithm anchors:** p. 4 (III. METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | 목표 전진 속도, 보행 위상의 사인·코사인, 추정한 몸체 방향·관절 위치·속도 | 49차원 네트워크 입력 | [PDF 3쪽](https://www.roboticsproceedings.org/rss16/p031.pdf#page=3) |
| State/latent | LSTM의 순환 상태 | 기억 없는 정책과 비교 | [PDF 4쪽](https://www.roboticsproceedings.org/rss16/p031.pdf#page=4) |
| Action/output | 중립 자세에 더할 모터 위치 목표 | PD 제어기로 전달 | [PDF 3쪽](https://www.roboticsproceedings.org/rss16/p031.pdf#page=3) |
| Objective/constraint | policies, trained, maximize, following, reward, function, qerr, xerr, yerr, orienterr | return, tracking or stability objective | equation anchor required |

## Observation–State–Action Interface

- 목표 전진 속도, 보행 위상의 사인·코사인, 추정한 몸체 방향·관절 위치·속도를 입력받아 모터 위치 목표를 낸다. [PDF 3쪽](https://www.roboticsproceedings.org/rss16/p031.pdf#page=3)
- **p. 2 / II. BACKGROUND - extractive body cue:** The policy is often a stochastic policy, in which case it is a function π(a/s) which takes in a state s and outputs the parameters ...
- **p. 3 / III. METHOD - extractive body cue:** The outputs of the policy are simply raw motor PD targets, much like Xie et al.
- **p. 4 / III. METHOD - extractive body cue:** Network Architecture All policies had an input dimension of length 49, and an output dimension of size 10.
- **p. 4 / III. METHOD - extractive body cue:** No information about the dynamics disturbances was provided to either the policy or the critic in the input space.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Recent work in transferring these trained controllers from simulation onto real robots has also enjoyed encouraging results [1, 2, 3, 4, 5, 6], but many ...
- **p. 2 / II. BACKGROUND - extractive body cue:** The reward r = R(s, a) is a scalar signal that expresses how good a particular state-action pair is.
- 정책 입력은 목표 전진 속도, 보행 위상의 사인·코사인, 추정한 몸체 방향·관절 위치·속도다. 순환 정책은 모터 위치 목표를 내고 PD 제어기가 토크를 계산한다. [PDF 3쪽](https://www.roboticsproceedings.org/rss16/p031.pdf#page=3)
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | 보행 참조의 주기 위상을 입력으로 제공 | 정책을 실행할 때마다 위상 카운터를 갱신 | [PDF 3쪽](https://www.roboticsproceedings.org/rss16/p031.pdf#page=3) |
| Rate / latency | 정책 30 ms 주기, 관절 PD 2 kHz | 그림 2와 III-A에서 명시 | 추론 지연 시간은 별도 지표 |
| Memory | LSTM의 순환 상태 | 기억 없는 정책과 같은 과제에서 비교 | [PDF 4쪽](https://www.roboticsproceedings.org/rss16/p031.pdf#page=4) |
| Compute | 정책과 관절 PD 제어의 주기를 비교 | 그림 2에 보고한 각 갱신 주기 | [PDF 3쪽](https://www.roboticsproceedings.org/rss16/p031.pdf#page=3) |

## Training vs Inference

- **p. 4 / III. METHOD - extractive body cue:** Optimize surrogate L wrt θ, using ˆs, ˆa, ˆA if KL(πθ(ˆs, ˆa), πθold(ˆs, ˆa)) > klthresh then break end if end for end for end ...
- **p. 4 / III. METHOD - extractive body cue:** Recurrent Proximal Policy Optimization We trained all policies with PPO, a model-free reinforcement learning algorithm.
- **p. 3 / III. METHOD - extractive body cue:** Reward Design Our learning process makes use of a reference trajectory produced by an expert walking controller to help the policy learn in the initial ...
- **p. 5 / IV. RESULTS - extractive body cue:** When training the feedforward policies, we used a batch size of 1024 timesteps.
- **p. 3 / III. METHOD - extractive body cue:** Though we believe that the recurrent policies do not have any theoretical reason for needing a clock input, we were not able to train any ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Optimize, surrogate, klthresh, then, break, During, training, fixed, action, standard, deviation, value, State, Space, policy, input, consists, fvel, desired, forward.
- **Relevant PDF headings:** III. METHOD (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| 순환 기억 | 무작위화 없이 훈련했을 때 LSTM의 시뮬레이션 보상 이득은 실물 보행에서 재현되지 않았다. | [PDF 5쪽](https://www.roboticsproceedings.org/rss16/p031.pdf#page=5) |
| 학습 조건 | LSTM과 피드포워드 정책을 각각 동역학 무작위화가 있는 조건과 없는 조건에서 비교했다. | [PDF 4쪽](https://www.roboticsproceedings.org/rss16/p031.pdf#page=4) |
| 실물 전이 | 무작위화한 동역학에서 학습한 LSTM이 실제 Cassie에서 가장 잘 수행한 조건을 제시한다. | [PDF 5쪽](https://www.roboticsproceedings.org/rss16/p031.pdf#page=5) · [PDF 6쪽](https://www.roboticsproceedings.org/rss16/p031.pdf#page=6) |

## Failure and Ablation Link

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We use recurrent neural networks and dynamics randomization to greatly improve the sim-to-real transfer rate and demonstrate learned, memory-based control on the bipedal ...
- **p. 4 / IV. RESULTS - extractive body cue:** Simulation We trained ten LSTM networks and ten FF networks with dynamics randomization, and ten LSTM networks and ten FF networks without dynamics randomization, each ...
- **p. 5 / IV. RESULTS - extractive body cue:** 5: Reward curve of LSTM and FF networks during training without dynamics randomization.
- **p. 5 / IV. RESULTS - extractive body cue:** As can be seen in Figure 5, when trained without dynamics randomization, LSTM networks attain a significantly higher reward than feedforward networks, with surprisingly little ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We use recurrent neural networks and dynamics randomization to greatly improve the sim-to-real transfer rate and demonstrate learned, memory-based control on the bipedal ...
- **p. 6 / V. CONCLUSION - extractive body cue:** The policies were learned and tested first in simulation, then transferred to the robot, demonstrating the robustness and promise of this approach.
- **p. 5 / IV. RESULTS - extractive body cue:** We conducted a robustness test in simulation across ten chosen sets of dynamics, taken from the range in Table I.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD), objective p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD), temporal p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD), p. 1 (Abstract), p. 1 (I. INTRODUCTION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
