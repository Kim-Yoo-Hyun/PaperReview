# Insights — Learning to Predict by the Methods of Temporal Differences

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (36 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1007/BF00115009; PDF retrieval source: https://doi.org/10.1007/BF00115009. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** S(!TTON In this article, we introduce and provide tilt first formal results in the theory of temporal-difference {TD) methods, a class of incremental learning procedures ...
- **p. 11 / 3.2 A random-walk example - extractive body cue:** In this paper, we propose that the only required characteristic is that the system predicted be a dynamical one, that it have a state which ...
- **p. 2 / 1. Introduction - extractive body cue:** This simplification allows us to evaluate them in isolation and has enabled us to obtain formal results.
- **p. 8 / 3. Examples of faster learning with TD methods - extractive body cue:** In this section, we develop two illustrative examples: a game-playing example to help develop intuitions, and a random-walk example as a simple demonstration with experimental ...
- **p. 9 / 3.1 A game-playing example - extractive body cue:** What evaluation should the novel position receive as a result of this experience?
- **p. 10 / 3.1 A game-playing example - extractive body cue:** If either edge state, A or G, is entered, then the walk terminates. loss.
- **p. 11 / 3.2 A random-walk example - extractive body cue:** For each nonterminal state i, there was a corresponding observation vector xi; if the walk was in state i at time t then xt = ...
- **Contribution anchor:** p. 2 (1. Introduction), p. 11 (3.2 A random-walk example), p. 2 (1. Introduction), p. 8 (3. Examples of faster learning with TD methods), p. 9 (3.1 A game-playing example), p. 10 (3.1 A game-playing example)

### Strongest assumption and failure boundary

- **p. 1 / 1. Introduction - extractive body cue:** Most pattern recognition problems, for examt)le, can be treated as prediction problems in which the classifier nmst predict the correct classifications.
- **p. 1 / 1. Introduction - extractive body cue:** Learning-to-predict problems also arise in heuristic search, e.g., in learning an evahmtion function that predicts tile utility of searching particular parts of tile search space, ...
- **p. 2 / 1. Introduction - extractive body cue:** S(!TTON In this article, we introduce and provide tilt first formal results in the theory of temporal-difference {TD) methods, a class of incremental learning procedures ...
- **p. 32 / 7. Conclusion - extractive body cue:** In speech recognition, for example, current learning methods cannot be applied until the correct classification of the word is known.
- **p. 25 / 5.1 Predicting cumulative outcomes - extractive body cue:** In a poh,-balancing problem one may want to predict time until a failure in balancing, and in a packet-switched telecomnnmications network one may want to ...
- **p. 19 / 4.1 Convergence of linear TD(0) - extractive body cue:** We cannot apply this lemma directly to D(I - Q) because it is not symmetric.
- **p. 22 / 4.2 Optimality and learning rate - extractive body cue:** SUTTON and biased coins, and thus cannot be uniquely determined.
- **Boundary to test:** In speech recognition, for example, current learning methods cannot be applied until the correct classification of the word is known.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | S(!TTON In this article, we introduce and provide tilt first formal results in the theory of temporal-difference {TD) methods, a class of incremental learning procedures specialized for prediction problems. | p. 2 (1. Introduction), p. 11 (3.2 A random-walk example) |
| Reported outcome | Averaging over training sets, we found that performance improved rapidly as A was reduced below 1 (the supervised-learning method) and was best at ,~ = 0 (the extreme TD method), as shown ... | p. 13 (3.2 A random-walk example), p. 29 (6.1 Samuel's checker-playing program) |
| Failure/limitation | In speech recognition, for example, current learning methods cannot be applied until the correct classification of the word is known. | p. 32 (7. Conclusion), p. 25 (5.1 Predicting cumulative outcomes) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `state 또는 observation, action, reward와 transition history → policy/value state와 action-selection variable → action policy와 induced trajectory`.
- 이 논문의 재사용 가능한 지점은 For each nonterminal state i, there was a corresponding observation vector xi; if the walk was in state i at time t then xt = xi.를 Thus, if the state the walk was in at time t has its 1 at the i th component of its observation vector, then the prediction Pt = 'wTxt was simply the ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 policy/value state와 action-selection variable가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 In speech recognition, for example, current learning methods cannot be applied until the correct classification of the word is known.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: S(!TTON In this article, we introduce and provide tilt first formal results in the theory of temporal-difference {TD) methods, a class of incremental learning procedures specialized for prediction problems.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `CORE` in `RL, IL, offline learning, and robot data`; tags: `Robotics, Reinforcement Learning, temporal difference, Value Learning`.
- **Reading predecessor in the generated track queue:** start of this track queue (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Q-Learning (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** In speech recognition, for example, current learning methods cannot be applied until the correct classification of the word is known.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: This measure was averaged over 100 training sets to produce the data shown..
3. Compare against the body-reported baseline or a matched simpler baseline: This procedure may require as much as O(n a) computation per time step as compared to O(n) for the supervised-learning and TD methods..
4. Report the body metric and its denominator/aggregation: The )~ = t data points represent performances of the Widrow-Hoff supervised-learning procedure. a measure of the performance of a learning procedure on a training set, we used the root mean squared ....
5. Re-run the body-reported ablation/failure condition: In this way the effect of the 1 could be propagated back to the beginning of the sequence with only a single presentation..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 10 (3.1 A game-playing example), p. 11 (3.2 A random-walk example), p. 11 (3.2 A random-walk example); the primary result is directionally consistent at p. 13 (3.2 A random-walk example), p. 29 (6.1 Samuel's checker-playing program), p. 30 (6.3 Holland's bucket brigade); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 TTON, article, introduce mechanism이 This procedure may require as much as O(n a) computation per time step as compared to ... 대비 The )~ = t data points represent performances of the Widrow-Hoff supervised-learning procedure. a measure of the performance ...을 개선하고, In speech recognition, for example, current learning methods cannot be applied until the correct classification of ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
