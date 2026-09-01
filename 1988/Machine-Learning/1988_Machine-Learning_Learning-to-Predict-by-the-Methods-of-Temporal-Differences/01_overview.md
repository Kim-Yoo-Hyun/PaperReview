# Learning to Predict by the Methods of Temporal Differences

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (36 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://doi.org/10.1007/BF00115009.
> PDF retrieval source: https://doi.org/10.1007/BF00115009. Reading tracker status/evidence was not changed.

- Year/Venue: 1988 / Machine Learning
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: CORE
- Tags: Robotics, Reinforcement Learning, temporal difference, Value Learning
- Official paper: https://doi.org/10.1007/BF00115009
- Full-text retrieval: https://doi.org/10.1007/BF00115009
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-02 (36 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 rl 문제를 이해하기 위해 읽는다. 본문은 Most pattern recognition problems, for examt)le, can be treated as prediction problems in which the classifier nmst predict the correct classifications.를 문제로 두고, S(!TTON In this article, we introduce and provide tilt first formal results in the theory of temporal-difference {TD) methods, a class of incremental learning procedures specialized for prediction problems.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

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

- **p. 2 / 1. Introduction - extractive body cue:** S(!TTON In this article, we introduce and provide tilt first formal results in the theory of temporal-difference {TD) methods, a class of incremental learning procedures ...
- **p. 11 / 3.2 A random-walk example - extractive body cue:** In this paper, we propose that the only required characteristic is that the system predicted be a dynamical one, that it have a state which ...
- **p. 2 / 1. Introduction - extractive body cue:** This simplification allows us to evaluate them in isolation and has enabled us to obtain formal results.
- **p. 8 / 3. Examples of faster learning with TD methods - extractive body cue:** In this section, we develop two illustrative examples: a game-playing example to help develop intuitions, and a random-walk example as a simple demonstration with experimental ...
- **p. 9 / 3.1 A game-playing example - extractive body cue:** What evaluation should the novel position receive as a result of this experience?
- **p. 13 / 3.2 A random-walk example - extractive body cue:** Averaging over training sets, we found that performance improved rapidly as A was reduced below 1 (the supervised-learning method) and was best at ,~ = ...
- **p. 29 / 6.1 Samuel's checker-playing program - extractive body cue:** Nevertheless, SamueFs learning procedure was overall very successful; it played an imt)ortant role in significantly improving the play of his checkerplaying program until it rivaled ...
- **p. 30 / 6.3 Holland's bucket brigade - extractive body cue:** In principle, hmg chains of rule invocations can be learned in this way, with strength being passed back from rule to rule, thus tile name ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

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

RL, IL, offline learning, and robot data의 rl 문제를 이해하기 위해 읽는다. 본문은 Most pattern recognition problems, for examt)le, can be treated as prediction problems in which the classifier nmst predict the correct classifications.를 문제로 두고, S(!TTON In this article, we introduce and provide tilt first formal results in the theory of temporal-difference {TD) methods, a class of incremental learning procedures specialized for prediction problems.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 10 (3.1 A game-playing example), p. 11 (3.2 A random-walk example), p. 11 (3.2 A random-walk example) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
