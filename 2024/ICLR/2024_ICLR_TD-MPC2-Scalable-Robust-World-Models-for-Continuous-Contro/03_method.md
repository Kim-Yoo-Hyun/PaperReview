# Method - TD-MPC2: Scalable, Robust World Models for Continuous Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (31 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2310.16828; PDF retrieval source: https://arxiv.org/pdf/2310.16828. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (2 BACKGROUND), p. 1 (ABSTRACT), p. 5 (2 BACKGROUND), p. 2 (1 INTRODUCTION), p. 4 (2 BACKGROUND), p. 3 (2 BACKGROUND)): The TD-MPC2 architecture is shown in Figure 3 and consists of five components: Encoder z = h(s, e) ▷Maps observations to their latent representations Latent dynamics z′ = d(z, a, ...

## Method Body Digest

- **p. 3 / §3.1 - extractive body cue:** The TD-MPC2 architecture is shown in Figure 3 and consists of five components: Encoder z = h(s, e) ▷Maps observations to their latent representations Latent ...
- **p. 1 / ABSTRACT - extractive body cue:** TD-MPC is a model-based reinforcement learning (RL) algorithm that performs local trajectory optimization in the latent space of a learned implicit (decoderfree) world model.
- **p. 5 / §3.3 - extractive body cue:** To do so, we zero-pad all model inputs and outputs to their largest respective dimensions, and mask out invalid action dimensions in predictions made by ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our algorithm, which builds upon TD-MPC (Hansen et al., 2022), performs local trajectory optimization in the latent space of a learned implicit (decoder-free) world model.
- **p. 4 / 2 BACKGROUND - extractive body cue:** Specifically, our approach leverages the MPC framework for local trajectory optimization using Model Predictive Path Integral (MPPI) (Williams et al., 2015) as a derivative-free optimizer ...
- **p. 3 / §3.1 그림 3 - extractive body cue:** The model then recurrently predicts actions ˆa, rewards ˆr, and terminal values ˆq, without decoding future observations.
- **p. 2 / 2 BACKGROUND - extractive body cue:** Reinforcement Learning (RL) aims to learn a policy from interaction with an environment, formulated as a Markov Decision Process (MDP) (Bellman, 1957).
- 인코더와 잠재 동역학, 보상·가치 예측기를 리플레이 전이로 함께 학습한다. [§3.1 식 3 · PDF 4쪽](https://arxiv.org/pdf/2310.16828v2#page=4)

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this work, we present TDMPC2: a significant step towards achieving this goal.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our algorithmic contributions, which have been key to achieving this milestone, are two-fold: (1) improved algorithmic robustness by revisiting core design choices, and (2) careful ...
- **p. 1 / ABSTRACT - extractive body cue:** In this work, we present TD-MPC2: a series of improvements upon the TD-MPC algorithm.

## Source Evidence Cues

- **p. 3 / §3.1 - extractive body cue:** The TD-MPC2 architecture is shown in Figure 3 and consists of five components: Encoder z = h(s, e) ▷Maps observations to their latent representations Latent ...
- **p. 1 / ABSTRACT - extractive body cue:** TD-MPC is a model-based reinforcement learning (RL) algorithm that performs local trajectory optimization in the latent space of a learned implicit (decoderfree) world model.
- **p. 5 / §3.3 - extractive body cue:** To do so, we zero-pad all model inputs and outputs to their largest respective dimensions, and mask out invalid action dimensions in predictions made by ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our algorithm, which builds upon TD-MPC (Hansen et al., 2022), performs local trajectory optimization in the latent space of a learned implicit (decoder-free) world model.
- **p. 4 / 2 BACKGROUND - extractive body cue:** Specifically, our approach leverages the MPC framework for local trajectory optimization using Model Predictive Path Integral (MPPI) (Williams et al., 2015) as a derivative-free optimizer ...
- **p. 3 / §3.1 그림 3 - extractive body cue:** The model then recurrently predicts actions ˆa, rewards ˆr, and terminal values ˆq, without decoding future observations.
- **p. 2 / 2 BACKGROUND - extractive body cue:** Reinforcement Learning (RL) aims to learn a policy from interaction with an environment, formulated as a Markov Decision Process (MDP) (Bellman, 1957).
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| 잠재 상태 전개 | 후보 행동의 결과를 예측 | 관측·작업 임베딩·행동 | 현재 관측을 인코딩하고 잠재 동역학을 반복 적용 | 예측 잠재 상태 | $z=h(s,e)$, $z^\prime=d(z,a,e)$ | [§3.1 그림 3·식 2 · PDF 3쪽](https://arxiv.org/pdf/2310.16828v2#page=3) |
| 수익 추정 | 행동열의 가치 계산 | 잠재 상태와 후보 행동열 | 유한 구간의 예측 보상에 종단 가치를 결합 | 행동열별 기대 수익 | 식 6의 목적함수 | [§3.2 식 6 · PDF 4쪽](https://arxiv.org/pdf/2310.16828v2#page=4) |
| 행동 선택·재계획 | 현재 스텝의 행동 결정 | 행동열별 수익과 샘플링 분포 | 수익에 따라 분포를 갱신하고 첫 행동만 실행 | 연속 행동과 다음 계획의 초기값 | 이전 계획을 한 칸 이동 | [§3.2 식 6의 실행 절차 · PDF 5쪽](https://arxiv.org/pdf/2310.16828v2#page=5) |

- 정책 사전분포는 계획할 행동열 일부를 제안한다. [§3.2 식 6의 실행 절차 · PDF 5쪽](https://arxiv.org/pdf/2310.16828v2#page=5)

## Objective / Update Rule

- 리플레이에서 뽑은 연속 전이에 대해 인코더 $h$, 잠재 동역학 $d$, 보상 $R$, 종단 가치 $Q$를 함께 학습한다. 시점별 손실은 $\lambda^t\!\left(\lVert z'_t-\operatorname{sg}(h(s'_t))\rVert_2^2+\operatorname{CE}(\hat r_t,r_t)+\operatorname{CE}(\hat q_t,q_t)\right)$이며 $t=0,\ldots,H$에 대해 합산해 기댓값을 최소화한다. $\operatorname{sg}$는 목표 임베딩에서 기울기 전파를 멈춘다. [§3.1 식 3 · PDF 4쪽](https://arxiv.org/pdf/2310.16828v2#page=4)
- **p. 3 / 2 BACKGROUND - extractive body cue:** Model Predictive Control (MPC) is a general framework for model-based control that optimizes action sequences at:t+H of finite length such that return is maximized (or ...
- **p. 5 / §3.2 - extractive body cue:** Notably, Equation 6 estimates the full RL objective introduced in Section 2 by bootstrapping with the learned terminal value function beyond horizon H.
- **p. 3 / §3.1 - extractive body cue:** The TD-MPC2 architecture is shown in Figure 3 and consists of five components: Encoder z = h(s, e) ▷Maps observations to their latent representations Latent ...
- **p. 4 / §3.1 - extractive body cue:** As the magnitude of rewards may differ drastically between tasks, TD-MPC2 formulates reward and value prediction as a discrete regression (multiclass classification) problem in a ...
- **p. 5 / §3.2 - extractive body cue:** Equation 6 is solved by iteratively sampling action sequences from N(µ, σ2), evaluating their expected return, and updating µ, σ based on a weighted average.
- **학습과 제어.** 식 3으로 세계 모델을, 식 4로 정책 사전분포를 학습한다. 식 6은 그 모델로 제어 시점의 기대 수익을 최적화한다. [§3.1 식 3 · PDF 4쪽](https://arxiv.org/pdf/2310.16828v2#page=4) · [§3.1 식 4 · PDF 4쪽](https://arxiv.org/pdf/2310.16828v2#page=4) · [§3.2 식 6의 실행 절차 · PDF 5쪽](https://arxiv.org/pdf/2310.16828v2#page=5)
- **식 위치.** 구성 요소는 식 2, 세계 모델 학습은 식 3, 정책 학습은 식 4, 행동열 계획은 식 6에 정의된다. [§3.1 그림 3·식 2 · PDF 3쪽](https://arxiv.org/pdf/2310.16828v2#page=3) · [§3.1 식 3 · PDF 4쪽](https://arxiv.org/pdf/2310.16828v2#page=4) · [§3.2 식 6의 실행 절차 · PDF 5쪽](https://arxiv.org/pdf/2310.16828v2#page=5)
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | $s,e$ | 관측과 작업 임베딩 | [§3.1 그림 3·식 2 · PDF 3쪽](https://arxiv.org/pdf/2310.16828v2#page=3) |
| State/latent | $z=h(s,e)$ | 후보 행동열을 평가할 잠재 상태 | [§3.1 그림 3·식 2 · PDF 3쪽](https://arxiv.org/pdf/2310.16828v2#page=3) |
| Action/output | $a_t$ | 매 결정 시점에 계획에서 샘플링한 첫 행동 | [§3.2 식 6의 실행 절차 · PDF 5쪽](https://arxiv.org/pdf/2310.16828v2#page=5) |
| Objective/constraint | 잠재 예측·보상·가치 손실 | 세계 모델 학습 | [§3.1 식 3 · PDF 4쪽](https://arxiv.org/pdf/2310.16828v2#page=4) |

## Observation–State–Action Interface

- **p. 3 / §3.1 - extractive body cue:** The TD-MPC2 architecture is shown in Figure 3 and consists of five components: Encoder z = h(s, e) ▷Maps observations to their latent representations Latent ...
- **p. 5 / §3.3 - extractive body cue:** To do so, we zero-pad all model inputs and outputs to their largest respective dimensions, and mask out invalid action dimensions in predictions made by ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Tasks include high-dimensional state and action spaces (up to A ∈R39), image observations, sparse rewards, multi-object manipulation, physiologically accurate musculoskeletal motor control, complex locomotion (e.g.
- **p. 2 / 2 BACKGROUND - extractive body cue:** Reinforcement Learning (RL) aims to learn a policy from interaction with an environment, formulated as a Markov Decision Process (MDP) (Bellman, 1957).
- **p. 3 / §3.1 그림 3 - extractive body cue:** The model then recurrently predicts actions ˆa, rewards ˆr, and terminal values ˆq, without decoding future observations.
- **p. 5 / §3.3 - extractive body cue:** (ii) how to accommodate multiple observation and action spaces without specific domain knowledge?
- **p. 1 / 1 INTRODUCTION - extractive body cue:** While researchers have recently extended this paradigm to robotics (Reed et al., 2022; Brohan et al., 2023), a generalist embodied agent that learns to perform ...
- **관측에서 행동까지.** 모델은 관측을 잠재 상태로 바꾸고, 행동열의 수익을 추정한다. 계획기는 분포를 갱신해 첫 행동을 선택한다. [§3.1 그림 3·식 2 · PDF 3쪽](https://arxiv.org/pdf/2310.16828v2#page=3) · [§3.2 식 6의 실행 절차 · PDF 5쪽](https://arxiv.org/pdf/2310.16828v2#page=5)
- 실시간 적용 시에는 과제별 계획 지연과 제어 주기를 측정할 수 있다.

## Temporal and Runtime Contract

| Contract | 원문의 설정 | 근거 | 재현 시 구분할 조건 |
|---|---|---|---|
| Horizon | 학습은 리플레이 구간 $0{:}H$의 손실에 $\lambda^t$를 곱한다. | 계획은 유한 길이 행동열의 보상과 종단 가치를 평가한다. [§3.1 식 3 · PDF 4쪽](https://arxiv.org/pdf/2310.16828v2#page=4) · [§3.2 식 6의 실행 절차 · PDF 5쪽](https://arxiv.org/pdf/2310.16828v2#page=5) | 학습 구간과 실행하는 첫 행동을 구분 |
| Rate / latency | 환경 스텝마다 첫 행동을 실행한 뒤 재계획한다. | 반복 샘플링으로 분포 갱신. [§3.2 식 6의 실행 절차 · PDF 5쪽](https://arxiv.org/pdf/2310.16828v2#page=5) | 실제 제어 주기의 단위와 측정 환경 |
| Memory | 직전 계획을 한 스텝 이동해 다음 계획의 초기 분포로 사용한다. | [§3.2 식 6의 실행 절차 · PDF 5쪽](https://arxiv.org/pdf/2310.16828v2#page=5) | 에피소드 경계에서의 초기화 |
| Compute | 각 결정에서 여러 행동열을 반복 샘플링하고 잠재 공간에서 평가한다. | [§3.2 식 6의 실행 절차 · PDF 5쪽](https://arxiv.org/pdf/2310.16828v2#page=5) | 추론 지연과 학습 비용 |

## Training vs Inference

- **p. 5 / §3.3 - extractive body cue:** To do so, we zero-pad all model inputs and outputs to their largest respective dimensions, and mask out invalid action dimensions in predictions made by ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** TD-MPC2, architecture, Figure, consists, five, components, Encoder, Maps, observations, latent, representations, dynamics, Models, forward, Reward, Predicts, transition, Terminal, value, discounted.
- **원문 절.** §3.1은 잠재 모델 학습, §3.2는 계획, §3.3은 다중 과제 임베딩과 행동 마스킹을 다룬다. [§3.1 식 3 · PDF 4쪽](https://arxiv.org/pdf/2310.16828v2#page=4) · [§3.2 식 6의 실행 절차 · PDF 5쪽](https://arxiv.org/pdf/2310.16828v2#page=5)
- 식 3의 잠재 상태 예측 목표에는 기울기 전파를 멈추는 연산이 들어간다. [§3.1 식 3 · PDF 4쪽](https://arxiv.org/pdf/2310.16828v2#page=4)

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| 연속 제어 | 네 도메인에서 환경 스텝에 따른 수익 또는 성공률을 비교한다. | [그림 4·§4 · PDF 5쪽](https://arxiv.org/pdf/2310.16828v2#page=5) |
| 다관절 보행·물체 조작 | 보행 수익과 조작 성공률의 과제별 곡선을 비교한다. | [§4.1 그림 5·6 · PDF 6쪽](https://arxiv.org/pdf/2310.16828v2#page=6) |
| 다중 과제 모델 크기 | 모델 크기에 따른 정규화 점수와 학습 비용을 비교한다. | [§4.1 그림 7·표 1 · PDF 7쪽](https://arxiv.org/pdf/2310.16828v2#page=7) |

## Failure and Ablation Link

- **p. 8 / 4.1 RESULTS - extractive body cue:** Our ablations highlight the relative importance of each design choice; red is the default formulation of TD-MPC2.
- **p. 8 / 4.1 RESULTS - extractive body cue:** Our main ablations, shown in Figure 9, are conducted on three of the most difficult online RL tasks, as well as largescale multitask training (80 ...
- **p. 9 / 4.1 RESULTS - extractive body cue:** TD-MPC2 performs comparably to the two best baselines, DrQ-v2 and DreamerV3, without any changes to hyperparameters.
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3. The TD-MPC2 architecture. Observations s are encoded into their (normalized) latent representation z. The model then recurrently predicts actions ˆa, rewards ˆr, and ...
- **p. 19 / Figure/Table caption - extractive body cue:** Table 5. MyoSuite. We consider a total of 10 continuous control tasks from the MyoSuite domain. The MyoSuite benchmark is designed for high-dimensional physiologically accurate ...
- **p. 25 / Figure/Table caption - extractive body cue:** Figure 18. Normalized task embeddings. Normalized score of 19M parameter multitask (80 tasks) TD-MPC2 agents, with and without normalized task embeddings e as described in ...
- **p. 25 / Figure/Table caption - extractive body cue:** Figure 19. T-SNE of task embeddings with and without normalization. T-SNE (van der Maaten & Hinton, 2008) visualizations of task embeddings learned by TD-MPC2 agent ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (2 BACKGROUND), p. 1 (ABSTRACT), p. 5 (2 BACKGROUND), p. 2 (1 INTRODUCTION), p. 4 (2 BACKGROUND), p. 3 (2 BACKGROUND), objective p. 4 (2 BACKGROUND), p. 3 (2 BACKGROUND), p. 5 (2 BACKGROUND), p. 3 (2 BACKGROUND), p. 4 (2 BACKGROUND), p. 5 (2 BACKGROUND), temporal p. 4 (2 BACKGROUND), p. 6 (4 EXPERIMENTS), p. 7 (4.1 RESULTS), p. 8 (4.1 RESULTS), p. 3 (2 BACKGROUND), p. 6 (4 EXPERIMENTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- 추론 시간을 재현할 때 모델 전개·반복 샘플링·환경 스텝에 걸리는 시간을 구분하는가?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (31 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** The TD-MPC2 architecture is shown in Figure 3 and consists of five components: Encoder z = h(s, e) ▷Maps observations to their latent representations Latent dynamics z′ = d(z, a, ... (p. 3, 2 BACKGROUND).
- **세계 모델 갱신.** $\lambda^t$로 가중한 잠재 상태 예측·보상·가치 손실을 합산하며, 잠재 예측의 목표에는 기울기가 흐르지 않는다. [§3.1 식 3 · PDF 4쪽](https://arxiv.org/pdf/2310.16828v2#page=4)
- **Temporal/runtime evidence:** Episode return as a function of environment steps in Humanoid (A ∈R21) and Dog (A ∈R38) locomotion tasks from DMControl. (p. 6, 4 EXPERIMENTS).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
