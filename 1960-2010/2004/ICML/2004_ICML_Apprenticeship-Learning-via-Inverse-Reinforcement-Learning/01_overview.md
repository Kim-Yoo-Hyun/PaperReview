# Apprenticeship Learning via Inverse Reinforcement Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://api.crossref.org/works/10.1145/1015330.1015430.
> PDF retrieval source: https://ai.stanford.edu/~ang/papers/icml04-apprentice.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2004 / ICML
- Authors: Pieter Abbeel, Andrew Y. Ng
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: Robotics, Imitation Learning, inverse reinforcement learning, apprenticeship learning
- Official paper: https://api.crossref.org/works/10.1145/1015330.1015430
- Full-text retrieval: https://ai.stanford.edu/~ang/papers/icml04-apprentice.pdf
- Code/Project: https://ai.stanford.edu/~pabbeel/irl/
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

Abbeel과 Ng는 전문가의 보상이 알려진 특징들의 선형 결합이라고 가정하고, 시연만으로 전문가에 가까운 성과를 내는 정책을 찾는다. [PDF 1쪽](https://ai.stanford.edu/~ang/papers/icml04-apprentice.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We consider learning in a Markov decision process where we are not explicitly given a reward function, but where instead we can observe an expert ...
- **p. 1 / Abstract - extractive body cue:** This setting is useful in applications (such as the task of driving) where it may be difficult to write down an explicit reward function specifying ...
- **p. 1 / Abstract - extractive body cue:** We think of the expert as trying to maximize a reward function that is expressible as a linear combination of known features, and give an ...
- **p. 1 / Abstract - extractive body cue:** Our algorithm is based on using "inverse reinforcement learning" to try to recover the unknown reward function.
- **p. 1 / Abstract - extractive body cue:** We show that our algorithm terminates in a small number of iterations, and that even though we may never recover the expert's reward function, the ...
- **p. 1 / 1. Introduction - extractive body cue:** From conversations with engineers in industry and our own experience in applying reinforcement learning algorithms to several robots, we believe that, for many problems, the ...
- **p. 1 / 1. Introduction - extractive body cue:** However, we believe that even the reward function is frequently difficult to specify manually.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we assume that the expert is trying (without necessarily succeeding) to optimize an unknown reward function that can be expressed as a ...
- **p. 3 / 3. Algorithm - extractive body cue:** (The SVM problem is a quadratic programming problem (QP), so we can also use any generic QP solver.) In Figure 1 we show an example ...
- **p. 3 / 3. Algorithm - extractive body cue:** (Whether the algorithm terminates is discussed in Section 4.) Then directly from Eq.
- **p. 4 / 3.1. A simpler algorithm - extractive body cue:** Briefly, the projection method replaces step 2 of the algorithm with the following: - Set ¯µ(i-1) = ¯µ(i-2)+ (µ(i-1)-¯µ(i-2))T (µE-¯µ(i-2)) (µ(i-1)-¯µ(i-2))T (µ(i-1)-¯µ(i-2))(µ(i-1)-¯µ(i-2)) (This computes the ...
- **p. 4 / 3. Algorithm - extractive body cue:** The performance guarantees of our algorithm only depend on (approximately) matching the feature expectations, not on recovering the true underlying reward function.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | A policy π is a mapping from states to probability distributions over actions. | observation history와 expert trajectory/action | p. 2 (2. Preliminaries), p. 2 (2. Preliminaries) |
| State/latent | policy, mapping, states, probability, distributions, over, actions, value, Es0, Here, expectation, taken | behavior policy와 temporal action context | p. 2 (2. Preliminaries), p. 2 (2. Preliminaries), p. 1 (1. Introduction) |
| Output/action | The value of a policy π is Es0∼D[V π(s0)] = E[P∞ t=0 γtR(st)/π] (1) = E[P∞ t=0 γtw · φ(st)/π] (2) = w · E[P∞ t=0 γtφ(st)/π] (3) Here, the expectation is ... | predicted action 또는 action chunk | p. 2 (2. Preliminaries), p. 1 (1. Introduction), p. 1 (1. Introduction) |
| Objective/outcome | Three iterations for max-margin algorithm. the reward function being optimized by the expert. | imitation error, task success, robustness와 compounding error | p. 3 (3. Algorithm), p. 3 (3. Algorithm), p. 4 (3. Algorithm) |

## Main Claims and Actual Contribution

- 할인된 특징 기대값을 전문가의 값에 가깝게 만들면 허용한 보상 함수들에 대해 성과 차이를 제한할 수 있음을 보인다. [PDF 2쪽](https://ai.stanford.edu/~ang/papers/icml04-apprentice.pdf#page=2) · [PDF 3쪽](https://ai.stanford.edu/~ang/papers/icml04-apprentice.pdf#page=3)
- 정책을 반복해 추가하는 투영 방법을 제시하고 모의 운전에서 서로 다른 전문가의 선호를 모방한다. [PDF 4쪽](https://ai.stanford.edu/~ang/papers/icml04-apprentice.pdf#page=4) · [PDF 6쪽](https://ai.stanford.edu/~ang/papers/icml04-apprentice.pdf#page=6)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 6 (5.1. Gridworld), p. 4 (4. Theoretical results) |
| Embodiment/environment | The simulation runs at 10Hz, and in the experiments that follow, the expert's features were estimated from a single trajectory of 1200 samples (corresponding to 2 minutes of driving time). | hardware/simulator version and reset protocol | p. 6 (5.2. Car driving simulation), p. 6 (5.2. Car driving simulation) |
| Dataset/benchmark | In particular, we do not rely on the expert's demonstrations to learn the state transition probabilities. | role, split, size and leakage | p. 6 (5.2. Car driving simulation), p. 6 (5.2. Car driving simulation), p. 5 (5.1. Gridworld), p. 5 (5.1. Gridworld) |
| Metric | In the case where the true reward function R∗does not lie exactly in the span of the basis functions φ, the algorithm still enjoys a graceful degradation of performance. | definition, denominator, direction and uncertainty | p. 4 (4. Theoretical results), p. 5 (4. Theoretical results), p. 5 (5.1. Gridworld) |
| Baseline/ablation | Screenshot of driving simulator. learning a compact representation of the reward function, our algorithm significantly outperforms the other methods. | fair input/data/compute/action matching | p. 6 (5.1. Gridworld), p. 5 (5.1. Gridworld) |

## Explicit Limitations and Failure Boundary

- **p. 5 / 5.1. Gridworld - extractive body cue:** The agent has four actions to try to move in each of the four compass directions, but with 30% chance an action fails and results ...
- **p. 6 / 5.2. Car driving simulation - extractive body cue:** Nice: The highest priority is to avoid collisions than the "mimic the expert" algorithm initially.
- **p. 6 / 5.2. Car driving simulation - extractive body cue:** Since no "true" reward was ever specified or used in the experiments, we cannot report on the results of the algorithm according to R∗.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Feature expectations of teacher ˆµE and of selected/learned policy µ(˜π) (as estimated by Monte Carlo). and weights w corresponding to the reward function ...
- **p. 4 / 4. Theoretical results - extractive body cue:** In the case where the true reward function R∗does not lie exactly in the span of the basis functions φ, the algorithm still enjoys a ...
- **p. 4 / 4. Theoretical results - extractive body cue:** If the algorithm sometimes does not terminate, or if it sometimes takes a very (perhaps exponentially) large number of iterations to terminate, then it would ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (2. Preliminaries), p. 3 (3. Algorithm)이다.
