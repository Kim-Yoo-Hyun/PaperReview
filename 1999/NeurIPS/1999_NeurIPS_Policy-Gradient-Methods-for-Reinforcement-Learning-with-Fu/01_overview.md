# Policy Gradient Methods for Reinforcement Learning with Function Approximation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> 2026-11-19 표본 감사에서 요약과 관련 본문 표현을 원문에 대조해 교정했다. [원문](https://proceedings.neurips.cc/paper/1999/hash/464d828b85b0bed98e80ade0a5c43b0f-Abstract.html)
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.neurips.cc/paper/1999/hash/464d828b85b0bed98e80ade0a5c43b0f-Abstract.html.
> PDF retrieval source: https://proceedings.neurips.cc/paper/1999/hash/464d828b85b0bed98e80ade0a5c43b0f-Abstract.html. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 1999 / NeurIPS
- Authors: Richard S. Sutton, David McAllester, Satinder Singh, Yishay Mansour
- Primary track: RL, IL, offline learning, and robot data
- Tier: CORE
- Tags: Robotics, Reinforcement Learning, Policy Gradient, actor-critic
- Official paper: https://proceedings.neurips.cc/paper/1999/hash/464d828b85b0bed98e80ade0a5c43b0f-Abstract.html
- Full-text retrieval: https://proceedings.neurips.cc/paper/1999/hash/464d828b85b0bed98e80ade0a5c43b0f-Abstract.html
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Sutton 등은 정책 경사를 행동가치로 표현하고, 그 자리에 함수 근사기를 사용해도 같은 경사를 얻는 조건을 증명했다. [원문](https://proceedings.neurips.cc/paper/1999/hash/464d828b85b0bed98e80ade0a5c43b0f-Abstract.html)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Function approximation is essential to reinforcement learning, but the standard approach of approximating a value function and determining a policy from it has so far ...
- **p. 1 / Abstract - extractive body cue:** In this paper we explore an alternative approach in which the policy is explicitly represented by its own function approximator, independent of the value function, ...
- **p. 1 / Abstract - extractive body cue:** Williams's REINFORCE method and actor-critic methods are examples of this approach.
- **p. 1 / Abstract - extractive body cue:** Our main new result is to show that the gradient can be written in a form suitable for estimation from experience aided by an approximate ...
- **p. 1 / Abstract - extractive body cue:** Using this result, we prove for the first time that a version of policy iteration with arbitrary differentiable function approximation is convergent to a locally ...
- **p. 1 / Abstract - extractive body cue:** The value-function approach has worked well in many applications, but has several limitations.
- **p. 2 / Abstract - extractive body cue:** Our result strengthens theirs and generalizes it to arbitrary differentiable function approximators.

## Core Idea

Sutton 등은 정책 성능의 경사를 정책의 미분과 행동가치의 기댓값으로 표현하는 정책 경사 정리를 제시한다. 정책과 호환되는 특징을 쓰고 논문의 적합 조건을 만족하는 가치 근사기는 경사 계산에서 실제 행동가치를 대체할 수 있다. [원문](https://proceedings.neurips.cc/paper/1999/hash/464d828b85b0bed98e80ade0a5c43b0f-Abstract.html)

## Observation, State, and Output Interface

상태에서 확률적 정책이 행동을 샘플링한다. 정리는 그 정책의 행동가치와 정책 미분을 기대 성능의 파라미터 경사에 연결한다. [원문](https://proceedings.neurips.cc/paper/1999/hash/464d828b85b0bed98e80ade0a5c43b0f-Abstract.html)

## Main Claims and Actual Contribution

평균 보상 및 할인 보상 설정에서 정책 경사를 표현하는 정리와 호환 함수 근사의 충분조건을 제시했다. 이론의 적용에는 논문이 명시한 특징과 근사기 적합 조건이 필요하다. [원문](https://proceedings.neurips.cc/paper/1999/hash/464d828b85b0bed98e80ade0a5c43b0f-Abstract.html)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 2 (Abstract), p. 4 (Abstract) |
| Embodiment/environment | The environment's dynamics are characterized by state transition probabilities, P:SI = Pr { St+ 1 = Sf I St = s, at = a}, and expected rewards 'R~ = E {rt+l 1st ... | hardware/simulator version and reset protocol | p. 2 (Abstract), p. 3 (Abstract) |
| Dataset/benchmark | We will give our results only once, but they will apply to this formulation as well under the definitions p(1I") = E{t. "(t-lrt I 80 ,1I"} and Q1r(s,a) = E{t. "(k-lrt+k 1St ... | role, split, size and leakage | p. 2 (Abstract), p. 3 (Abstract), p. 3 (Abstract) |
| Metric | However, VAPS methods do not climb the gradient of performance (expected long-term reward), but of a measure combining performance and valuefunction accuracy. | definition, denominator, direction and uncertainty | p. 2 (Abstract), p. 2 (Abstract), p. 3 (Abstract) |
| Baseline/ablation | The issues here are entirely analogous to those in the use of reinforcement baselines in earlier work (e.g., Williams, 1992; Dayan, 1991; Sutton, 1984). | fair input/data/compute/action matching | p. 5 (Abstract), p. 2 (Abstract), p. 5 (Abstract) |

## Explicit Limitations and Failure Boundary

- **p. 2 / Abstract - extractive body cue:** Similarly, Gordon's (1995) fitted value iteration is also convergent and value-based, but does not find a locally optimal policy.
- **p. 2 / Abstract - extractive body cue:** As a result, VAPS does not converge to a locally optimal policy, except in the case that no weight is put upon value-function accuracy, in ...
- **p. 3 / Abstract - extractive body cue:** In any event, the key aspect of both expressions for the gradient is that their are no terms of the form adiJII): the effect of ...
- **p. 5 / Abstract - extractive body cue:** (This follows immediately because l:a 87r~~a) = 0, Vs E S.) The choice of v does not affect any of our theorems, but can substantially ...

## Why Read It

actor–critic 방법에서 critic 근사 오차가 actor의 갱신에 미치는 영향을 해석하는 이론적 기준이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (7 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** The value-function approach has worked well in many applications, but has several limitations. (p. 1, Abstract).
- **Actual contribution:** Sutton 등은 정책 성능의 경사를 정책의 미분과 행동가치의 기댓값으로 표현하는 정책 경사 정리를 제시한다. 정책과 호환되는 특징을 쓰고 논문의 적합 조건을 만족하는 가치 근사기는 경사 계산에서 실제 행동가치를 대체할 수 있다. [원문](https://proceedings.neurips.cc/paper/1999/hash/464d828b85b0bed98e80ade0a5c43b0f-Abstract.html)
- **Evaluation boundary:** However, VAPS methods do not climb the gradient of performance (expected long-term reward), but of a measure combining performance and valuefunction accuracy. (p. 2, Abstract).
- **Explicit failure boundary:** The value-function approach has worked well in many applications, but has several limitations. (p. 1, Abstract).
