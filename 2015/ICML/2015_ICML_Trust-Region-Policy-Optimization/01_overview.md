# Trust Region Policy Optimization

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v37/schulman15.html.
> PDF retrieval source: https://arxiv.org/pdf/1502.05477. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2015 / ICML
- Authors: John Schulman, Sergey Levine, Philipp Moritz, Michael Jordan, Pieter Abbeel
- 저자 표기 근거 — PMLR 게재 PDF의 표제면에서 Philipp Moritz가 세 번째, Pieter Abbeel이 마지막이다. [표제면](https://arxiv.org/pdf/1502.05477#page=1)
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, Reinforcement Learning, policy optimization, on-policy RL
- Official paper: https://proceedings.mlr.press/v37/schulman15.html
- Full-text retrieval: https://arxiv.org/pdf/1502.05477
- Code/Project: https://github.com/joschu/modular_rl
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0)

> DOC-QA2 targeted source review: 2026-10-23; PDF pp. 4. 손상 구간·직접 연결된 표 분류만 원문 이미지와 대조했다. 전체 주장 정독·실험 검증·reading status 승격을 뜻하지 않는다. [URL·PDF hash·수정 기록](../../../work/sources/pdf_note_review_followup_2026-10-23.json).

## Why This Paper Is Here

TRPO는 정책을 한 번에 너무 크게 바꿔 성능이 무너지는 문제를 다루는 정책 최적화 방법이다. [PDF 1쪽](https://arxiv.org/pdf/1502.05477#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We describe an iterative procedure for optimizing policies, with guaranteed monotonic improvement.
- **p. 1 / Abstract - extractive body cue:** By making several approximations to the theoretically-justified procedure, we develop a practical algorithm, called Trust Region Policy Optimization (TRPO).
- **p. 1 / Abstract - extractive body cue:** This algorithm is similar to natural policy gradient methods and is effective for optimizing large nonlinear policies such as neural networks.
- **p. 1 / Abstract - extractive body cue:** Our experiments demonstrate its robust performance on a wide variety of tasks: learning simulated robotic swimming, hopping, and walking gaits; and playing Atari games using ...
- **p. 1 / Abstract - extractive body cue:** Despite its approximations that deviate from the theory, TRPO tends to give monotonic improvement, with little tuning of hyperparameters.
- **p. 1 / 1 Introduction - extractive body cue:** Tetris is a classic benchmark problem for approximate dynamic programming (ADP) methods, stochastic optimization methods are difficult to beat on this task (Gabillon et al., ...
- **p. 1 / 1 Introduction - extractive body cue:** Most algorithms for policy optimization can be classified into three broad categories: (1) policy iteration methods, which alternate between estimating the value function under the ...

## Core Idea

- **p. 2 / 2 Preliminaries - extractive body cue:** Instead, we introduce the following local approximation to η: Lπ(˜π) = η(π) + X s ρπ(s) X a ˜π(a/s)Aπ(s, a).
- **p. 3 / 2 Preliminaries - extractive body cue:** Trust region policy optimization, which we propose in the following section, is an approximation to Algorithm 1, which uses a constraint on the KL divergence ...
- **p. 5 / 2 Preliminaries - extractive body cue:** 6 Practical Algorithm Here we present two practical policy optimization algorithm based on the ideas above, which use either the single path or vine sampling ...
- **p. 1 / 1 Introduction - extractive body cue:** In our experiments, we show that the same TRPO methods can learn complex policies for swimming, hopping, and walking, as well as playing Atari games ...
- **PDF p. 4, §5 sampling / Eq. (14) (DOC-QA2 원문 대조):** 단일 state의 action expectation은 q에서 sampling한 π_θ(a given s)/q(a given s) importance weight로 추정한다. Q-value surrogate를 최대화하면서 old-to-new policy의 평균 KL divergence≤δ 조건을 둔다. Sampling distribution의 support 조건을 보존해야 한다.
- **p. 5 / 3. Approximately solve this constrained optimization - extractive body cue:** We use the conjugate gradient algorithm followed by a line search, which is altogether only slightly more expensive than computing the gradient itself.
- **p. 5 / 3. Approximately solve this constrained optimization - extractive body cue:** Empirically, it is hard to robustly choose the penalty coefficient, so we use a hard constraint instead of a penalty, with parameter δ (the bound ...
- **p. 6 / 3. Approximately solve this constrained optimization - extractive body cue:** Relative entropy policy search (REPS) (Peters et al., 2010) constrains the state-action marginals p(s, a), while TRPO constrains the conditionals p(a/s).

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | This implies the classic result that the update performed by exact policy iteration, which uses the deterministic policy ˜π(s) = arg maxa Aπ(s, a), improves the policy if there is at least ... | state 또는 observation, action, reward와 transition history | p. 2 (2 Preliminaries), p. 4 (2 Preliminaries) |
| State/latent | implies, classic, result, update, performed, exact, policy, iteration, uses, deterministic, maxa, improves | policy/value state와 action-selection variable | p. 2 (2 Preliminaries), p. 4 (2 Preliminaries), p. 5 (2 Preliminaries) |
| Output/action | Here, we generate a set of trajectories via simulation of the policy and incorporate all state-action pairs (sn, an) into the objective. | action policy와 induced trajectory | p. 4 (2 Preliminaries), p. 5 (2 Preliminaries), p. 6 (3. Approximately solve this constrained optimization) |
| Objective/outcome | The natural policy gradient (Kakade, 2002) can be obtained as a special case of the update in Equation (12) by using a linear approximation to L and a quadratic approximation to the ... | expected return, task success, stability와 sample efficiency | p. 6 (3. Approximately solve this constrained optimization), p. 6 (3. Approximately solve this constrained optimization), p. 5 (3. Approximately solve this constrained optimization) |

## Main Claims and Actual Contribution

- 정책 성능의 하한을 바탕으로 개선 조건을 유도하고 KL 발산으로 갱신 폭을 제한하는 계산 가능한 근사를 제시한다. [PDF 3쪽](https://arxiv.org/pdf/1502.05477#page=3) · [PDF 5쪽](https://arxiv.org/pdf/1502.05477#page=5)
- 이론적 단조 개선과 실제 근사 알고리즘을 구분하고, 시뮬레이션 연속 제어 및 Atari에서 후자의 학습 성능을 비교했다. [PDF 7쪽](https://arxiv.org/pdf/1502.05477#page=7) · [PDF 8쪽](https://arxiv.org/pdf/1502.05477#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 6 (3. Approximately solve this constrained optimization), p. 5 (3. Approximately solve this constrained optimization) |
| Embodiment/environment | 8.1 Simulated Robotic Locomotion We conducted the robotic locomotion experiments using the MuJoCo simulator (Todorov et al., 2012). | hardware/simulator version and reset protocol | p. 6 (3. Can TRPO be used to solve challenging large-scale), p. 6 (1. What are the performance characteristics of the single) |
| Dataset/benchmark | We ended the episodes when the hopper fell over, which was defined by thresholds on the torso height and angle. | role, split, size and leakage | p. 6 (3. Can TRPO be used to solve challenging large-scale), p. 6 (1. What are the performance characteristics of the single), p. 7 (3. Can TRPO be used to solve challenging large-scale), p. 5 (2 Preliminaries) |
| Metric | Table 1. Performance comparison for vision-based RL algorithms on the Atari domain. Our algorithms (bottom rows) were run once on each task, with the same architecture and parameters. Performance varies substantially from ... | definition, denominator, direction and uncertainty | p. 8 (Figure/Table caption), p. 5 (3. Approximately solve this constrained optimization), p. 5 (3. Approximately solve this constrained optimization) |
| Baseline/ablation | This self-normalized estimator removes the need to use a baseline for the Q-values (note that the gradient is unchanged by adding a constant to the Q-values). | fair input/data/compute/action matching | p. 5 (2 Preliminaries), p. 7 (3. Can TRPO be used to solve challenging large-scale), p. 7 (3. Can TRPO be used to solve challenging large-scale) |

## Explicit Limitations and Failure Boundary

- **p. 5 / 3. Approximately solve this constrained optimization - extractive body cue:** The analytic estimator integrates over the action at each state sn, and does not depend on the action an that was sampled.
- **p. 6 / 3. Approximately solve this constrained optimization - extractive body cue:** Unlike REPS, our approach does not require a costly nonlinear optimization in the inner loop.
- **p. 5 / 2 Preliminaries - extractive body cue:** We can greatly reduce the variance of the Q-value differences between rollouts by using the same random number sequence for the noise in each of ...
- **p. 7 / 3. Can TRPO be used to solve challenging large-scale - extractive body cue:** These results provide empirical evidence that constraining the KL divergence is a more robust way to choose step sizes and make fast, consistent progress, compared ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1 Introduction), p. 2 (2 Preliminaries), p. 3 (2 Preliminaries), p. 5 (3. Approximately solve this constrained optimization)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (16 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Tetris is a classic benchmark problem for approximate dynamic programming (ADP) methods, stochastic optimization methods are difficult to beat on this task (Gabillon et al., 2013). (p. 1, 1 Introduction).
- **Actual contribution:** In our experiments, we show that the same TRPO methods can learn complex policies for swimming, hopping, and walking, as well as playing Atari games directly from raw images. (p. 1, 1 Introduction).
- **Evaluation boundary:** Table 1. Performance comparison for vision-based RL algorithms on the Atari domain. Our algorithms (bottom rows) were run once on each task, with the same architecture and parameters. Performance varies ... (p. 8, Figure/Table caption).
- **Explicit failure boundary:** Our analysis also provides a perspective that unifies policy gradient and policy iteration methods, and shows them to be special limiting cases of an algorithm that optimizes a certain objective ... (p. 8, 9 Discussion).

## 배포 범위 대조

- 코드 — 제1저자가 배포한 모듈형 TRPO 구현. ICML 표의 실험 시점 버전은 미확인이다. [배포 파일](https://raw.githubusercontent.com/joschu/modular_rl/6970cde3da265cf2a98537250fea5e0c0d9a7639/modular_rl/trpo.py)
- 데이터 — 원문에 학습 또는 제어 실험의 관측·궤적이 있다. 해당 실험의 원시 자료 배포 범위는 미확인이다. [검토 근거](https://arxiv.org/pdf/1502.05477#page=6)
