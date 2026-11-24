# Problem - TD-MPC2: Scalable, Robust World Models for Continuous Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (31 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2310.16828; PDF retrieval source: https://arxiv.org/pdf/2310.16828. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 3 (2 BACKGROUND), p. 5 (2 BACKGROUND), p. 5 (2 BACKGROUND), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION)): However, accurately predicting raw future observations (e.g., images or proprioceptive features) over long time horizons is a difficult problem, and does not necessarily lead to effective control (Lambert et al., ...

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive body cue:** TD-MPC is a model-based reinforcement learning (RL) algorithm that performs local trajectory optimization in the latent space of a learned implicit (decoderfree) world model.
- **p. 1 / ABSTRACT - extractive body cue:** In this work, we present TD-MPC2: a series of improvements upon the TD-MPC algorithm.
- **p. 1 / ABSTRACT - extractive body cue:** We demonstrate that TD-MPC2 improves significantly over baselines across 104 online RL tasks spanning 4 diverse task domains, achieving consistently strong results with a single ...
- **p. 1 / ABSTRACT - extractive body cue:** We further show that agent capabilities increase with model and data size, and successfully train a single 317M parameter agent to perform 80 tasks across ...
- **p. 1 / ABSTRACT - extractive body cue:** We conclude with an account of lessons, opportunities, and risks associated with large TD-MPC2 agents.
- **p. 3 / 2 BACKGROUND - extractive body cue:** However, accurately predicting raw future observations (e.g., images or proprioceptive features) over long time horizons is a difficult problem, and does not necessarily lead to ...
- **p. 5 / 2 BACKGROUND - extractive body cue:** However, in the general case where domain knowledge cannot be assumed, we may instead choose to learn the task embeddings (and, implicitly, task relations) from ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | 관측 자체를 장기 예측하지 않고도 연속 행동열의 수익을 추정한다. | 제어에 필요한 결과를 예측하는 세계 모델 | [§3.1 그림 3·식 2 · PDF 3쪽](https://arxiv.org/pdf/2310.16828v2#page=3) |
| Observation / input | 상태 또는 영상 관측 $s$, 다중 과제의 작업 임베딩 $e$ | 인코더 입력 | [§3.1 그림 3·식 2 · PDF 3쪽](https://arxiv.org/pdf/2310.16828v2#page=3) |
| State / latent | 정규화한 잠재 상태 $z$ | 후보 행동으로 잠재 공간에서 전개 | [§3.1 그림 3·식 2 · PDF 3쪽](https://arxiv.org/pdf/2310.16828v2#page=3) |
| Output / action | 유한 길이 행동열에서 샘플링한 첫 연속 행동 | 현재 스텝에 적용 | [§3.2 식 6의 실행 절차 · PDF 5쪽](https://arxiv.org/pdf/2310.16828v2#page=5) |
| Target outcome | 환경과의 상호작용 횟수에 따른 과제 성능 | DMControl 수익과 타 도메인 성공률 | [그림 4·§4 · PDF 5쪽](https://arxiv.org/pdf/2310.16828v2#page=5) |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | $s$를 인코딩한 $z=h(s,e)$ | [§3.1 그림 3·식 2 · PDF 3쪽](https://arxiv.org/pdf/2310.16828v2#page=3) |
| Decision / output variable | 보상과 종단 가치로 평가한 후보 행동열의 첫 행동 | [§3.2 식 6의 실행 절차 · PDF 5쪽](https://arxiv.org/pdf/2310.16828v2#page=5) |
| Objective / loss / cost | 시간 가중 잠재 예측·보상·가치 손실로 세계 모델을 학습하고, 계획에서는 기대 수익을 최대화한다. | [§3.1 식 3 · PDF 4쪽](https://arxiv.org/pdf/2310.16828v2#page=4) · [§3.2 식 6의 실행 절차 · PDF 5쪽](https://arxiv.org/pdf/2310.16828v2#page=5) |
| Constraint / feasibility | 다중 과제에서는 유효한 행동 차원만 샘플링한다. | [§3.3 행동 마스킹 · PDF 5쪽](https://arxiv.org/pdf/2310.16828v2#page=5) |
| Success / guarantee | 과제별 수익 또는 성공률을 실험으로 비교한다. | [그림 4·§4 · PDF 5쪽](https://arxiv.org/pdf/2310.16828v2#page=5) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 5 / 2 BACKGROUND - extractive body cue:** However, in the general case where domain knowledge cannot be assumed, we may instead choose to learn the task embeddings (and, implicitly, task relations) from ...
- **p. 5 / 2 BACKGROUND - extractive body cue:** However, learning a large generalist TD-MPC2 agent that performs a variety of tasks across multiple task domains, embodiments, and action spaces poses several unique challenges: ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** We argue that current approaches to generalist embodied agents suffer from (a) the assumption of near-expert trajectories for behavior cloning which severely limits the amount ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** An algorithm that can consume large multitask datasets will invariably need to be robust to variation between different tasks (e.g., action space dimensionality, difficulty of ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 3 (2 BACKGROUND), p. 3 (2 BACKGROUND)): In this work, we present TDMPC2: a significant step towards achieving this goal.

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our algorithmic contributions, which have been key to achieving this milestone, are two-fold: (1) improved algorithmic robustness by revisiting core design choices, and (2) careful ...
- **p. 1 / ABSTRACT - extractive body cue:** In this work, we present TD-MPC2: a series of improvements upon the TD-MPC algorithm.
- **p. 3 / 2 BACKGROUND - extractive body cue:** We introduce the TD-MPC2 algorithm in the following, and provide a full list of algorithmic improvements in Appendix A.
- **p. 3 / 2 BACKGROUND - extractive body cue:** Specifically, we propose a series of improvements to the TD-MPC algorithm, which have been key to achieving strong algorithmic robustness (can use the same hyperparameters ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | While we are excited by the potential of generalist world models, several challenges remain: (i) misspecification of task ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 22 | Figure 13. Single-task Meta-World results. Success rate (%) as a function of environment steps. TD-MPC2 performance is comparable ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Notably, performance does not appear to have saturated for our largest models (317M parameters) on either dataset, and ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 2 | Figure 2. Tasks. TD-MPC2 performs 104 diverse tasks from (left to right) DMControl (Tassa et al., 2018), Meta-World ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

관측을 인코딩하고 잠재 동역학으로 후보 행동열을 평가한다. 선택한 첫 행동을 적용한 뒤 새로운 관측에서 다시 계획한다. [§3.1 그림 3·식 2 · PDF 3쪽](https://arxiv.org/pdf/2310.16828v2#page=3) · [§3.2 식 6의 실행 절차 · PDF 5쪽](https://arxiv.org/pdf/2310.16828v2#page=5)

## Verification Questions

- **Evidence anchors reviewed:** problem p. 3 (2 BACKGROUND), p. 5 (2 BACKGROUND), p. 5 (2 BACKGROUND), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), interface p. 3 (2 BACKGROUND), p. 5 (2 BACKGROUND), p. 2 (1 INTRODUCTION), p. 2 (2 BACKGROUND), objective p. 4 (2 BACKGROUND), p. 4 (2 BACKGROUND), p. 5 (2 BACKGROUND), p. 3 (2 BACKGROUND), p. 3 (2 BACKGROUND), p. 5 (2 BACKGROUND).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (31 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** However, accurately predicting raw future observations (e.g., images or proprioceptive features) over long time horizons is a difficult problem, and does not necessarily lead to effective control (Lambert et al., ... (p. 3, 2 BACKGROUND).
- **Formulation-changing contribution:** In this work, we present TDMPC2: a significant step towards achieving this goal. (p. 2, 1 INTRODUCTION).
- **Assumption/failure evidence:** While we are excited by the potential of generalist world models, several challenges remain: (i) misspecification of task rewards can lead to unintended outcomes (Clark & Amodei, 2016) that may ... (p. 9, 4.1 RESULTS).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
