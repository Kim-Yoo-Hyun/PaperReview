# Learning to Predict by the Methods of Temporal Differences

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (36 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://doi.org/10.1007/BF00115009.
> PDF retrieval source: https://doi.org/10.1007/BF00115009. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 1988 / Machine Learning
- Authors: Richard S. Sutton
- Primary track: RL, IL, offline learning, and robot data
- Tier: CORE
- Tags: Reinforcement Learning, temporal difference, Value Learning
- Official paper: https://doi.org/10.1007/BF00115009
- Full-text retrieval: https://doi.org/10.1007/BF00115009
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (36 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## 공개 자료

- **데이터** 원문에 훈련 시퀀스를 생성하는 절차가 있다. 원래의 난수 보행 표본 자체를 내려받을 수 있는 저자 자료와의 대응은 미확인이다. [검토 근거](https://link.springer.com/content/pdf/10.1007/BF00115009.pdf)

## Why This Paper Is Here

시간차 학습은 연속한 시점의 예측 사이의 차이를 이용해 미래 결과의 예측을 점진적으로 갱신한다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** This article introduces a class of incremental learning procedures specialized for prediction that is, for using past experience with an incompletely known system to predict ...
- **p. 1 / Abstract - extractive body cue:** Whereas conventional prediction-learning methods assign credit by means of the difference between predicted and actual outcomes, tile new methods assign credit by means of the ...
- **p. 1 / Abstract - extractive body cue:** Although such temporal-difference method~ have been used in Samuel's checker player, Holland's bucket brigade, and the author's Adaptive Heuristic Critic, they have remained poorly understood.
- **p. 1 / Abstract - extractive body cue:** Here we prove their convergence and optimality for special cases and relate them to supervised-learning methods.
- **p. 1 / Abstract - extractive body cue:** For most real-world prediction problems, telnporal-differenee methods require less memory and less peak computation than conventional methods and they produce more accurate predictions.
- **p. 1 / 1. Introduction - extractive body cue:** Most pattern recognition problems, for examt)le, can be treated as prediction problems in which the classifier nmst predict the correct classifications.
- **p. 1 / 1. Introduction - extractive body cue:** Learning-to-predict problems also arise in heuristic search, e.g., in learning an evahmtion function that predicts tile utility of searching particular parts of tile search space, ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** S(!TTON In this article, we introduce and provide tilt first formal results in the theory of temporal-difference {TD) methods, a class of incremental learning procedures ...
- **p. 11 / 3.2 A random-walk example - extractive body cue:** In this paper, we propose that the only required characteristic is that the system predicted be a dynamical one, that it have a state which ...
- **p. 2 / 1. Introduction - extractive body cue:** This simplification allows us to evaluate them in isolation and has enabled us to obtain formal results.
- **p. 8 / 3. Examples of faster learning with TD methods - extractive body cue:** In this section, we develop two illustrative examples: a game-playing example to help develop intuitions, and a random-walk example as a simple demonstration with experimental ...
- **p. 9 / 3.1 A game-playing example - extractive body cue:** What evaluation should the novel position receive as a result of this experience?
- **p. 10 / 3.1 A game-playing example - extractive body cue:** If either edge state, A or G, is entered, then the walk terminates. loss.
- **p. 11 / 3.2 A random-walk example - extractive body cue:** For each nonterminal state i, there was a corresponding observation vector xi; if the walk was in state i at time t then xt = ...
- **p. 11 / 3.2 A random-walk example - extractive body cue:** Thus, if the state the walk was in at time t has its 1 at the i th component of its observation vector, then the ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | For each nonterminal state i, there was a corresponding observation vector xi; if the walk was in state i at time t then xt = xi. | state 또는 observation, action, reward와 transition history | p. 11 (3.2 A random-walk example), p. 11 (3.2 A random-walk example) |
| State/latent | nonterminal, state, there, corresponding, observation, vector, walk, time, then, Thus, component, prediction | policy/value state와 action-selection variable | p. 11 (3.2 A random-walk example), p. 11 (3.2 A random-walk example), p. 3 (1. Introduction) |
| Output/action | Thus, if the state the walk was in at time t has its 1 at the i th component of its observation vector, then the prediction Pt = 'wTxt was simply the ... | action policy와 induced trajectory | p. 11 (3.2 A random-walk example), p. 3 (1. Introduction), p. 9 (3.1 A game-playing example) |
| Objective/outcome | The "bad" position is known from long experience to lead 90% of the time to a loss and only 10% of the time to a win. | expected return, task success, stability와 sample efficiency | p. 9 (3.1 A game-playing example), p. 9 (3.1 A game-playing example), p. 10 (3.1 A game-playing example) |

## Main Claims and Actual Contribution

- 최종 결과가 주어지기 전에 후속 예측을 이용해 이전 상태의 예측을 수정하는 학습 규칙을 제시한다.
- 일부 경우에 한해 수렴과 최적성을 분석하고 감독학습에 의한 예측과 비교한다.

[저자 원문](https://doi.org/10.1007/BF00115009)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 13 (3.2 A random-walk example), p. 29 (6.1 Samuel's checker-playing program) |
| Embodiment/environment | This measure was averaged over 100 training sets to produce the data shown. | hardware/simulator version and reset protocol | p. 12 (3.2 A random-walk example), p. 12 (3.2 A random-walk example) |
| Dataset/benchmark | The second experiment concerns the question of learning rate when the training set is presented just once rather than repeatedly until convergence. | role, split, size and leakage | p. 12 (3.2 A random-walk example), p. 12 (3.2 A random-walk example), p. 13 (3.2 A random-walk example), p. 13 (3.2 A random-walk example) |
| Metric | The )~ = t data points represent performances of the Widrow-Hoff supervised-learning procedure. a measure of the performance of a learning procedure on a training set, we used the root mean squared ... | definition, denominator, direction and uncertainty | p. 13 (3.2 A random-walk example), p. 28 (6.1 Samuel's checker-playing program), p. 12 (Figure/Table caption) |
| Baseline/ablation | This procedure may require as much as O(n a) computation per time step as compared to O(n) for the supervised-learning and TD methods. | fair input/data/compute/action matching | p. 22 (4.2 Optimality and learning rate), p. 24 (4.2 Optimality and learning rate), p. 15 (3.2 A random-walk example) |

## Explicit Limitations and Failure Boundary

- **p. 32 / 7. Conclusion - extractive body cue:** In speech recognition, for example, current learning methods cannot be applied until the correct classification of the word is known.
- **p. 25 / 5.1 Predicting cumulative outcomes - extractive body cue:** In a poh,-balancing problem one may want to predict time until a failure in balancing, and in a packet-switched telecomnnmications network one may want to ...
- **p. 19 / 4.1 Convergence of linear TD(0) - extractive body cue:** We cannot apply this lemma directly to D(I - Q) because it is not symmetric.
- **p. 22 / 4.2 Optimality and learning rate - extractive body cue:** SUTTON and biased coins, and thus cannot be uniquely determined.
- **p. 27 / 5.3 Prediction by a fixed interval - extractive body cue:** Although this problem involves a sequence of predictions, TD methods cannot be directly applied because each prediction is of a different event and thus there ...
- **p. 13 / 3.2 A random-walk example - extractive body cue:** The answer is that the Widrow-Hoff procedure only minimizes error on the training set; it does not necessarily minimize error for future experience.
- **p. 22 / 4.2 Optimality and learning rate - extractive body cue:** This does not change any of the conclusions of the analysis.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 10 (3.1 A game-playing example), p. 11 (3.2 A random-walk example)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (36 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Most pattern recognition problems, for examt)le, can be treated as prediction problems in which the classifier nmst predict the correct classifications. (p. 1, 1. Introduction).
- **Actual contribution:** S(!TTON In this article, we introduce and provide tilt first formal results in the theory of temporal-difference {TD) methods, a class of incremental learning procedures specialized for prediction problems. (p. 2, 1. Introduction).
- **Evaluation boundary:** Figure 1. ....... t~~0 ~@ A game-playing example showing the inefficiency of supervised-learning methods. Each circle represents a position or class of positions from a two- person board game. The ... (p. 9, Figure/Table caption).
- **Explicit failure boundary:** In a poh,-balancing problem one may want to predict time until a failure in balancing, and in a packet-switched telecomnnmications network one may want to pre(tict the total delay in ... (p. 25, 5.1 Predicting cumulative outcomes).
