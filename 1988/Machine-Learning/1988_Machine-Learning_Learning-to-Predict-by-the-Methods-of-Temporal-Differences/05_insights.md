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

- **Paper-specific interface:** Now suppose you play a game that reaches a novel position (one that you have never seen before), that then progresses to reach the bad state, and that finally ends ... (p. 9, 3.1 A game-playing example).
- **Paper-specific mechanism:** S(!TTON In this article, we introduce and provide tilt first formal results in the theory of temporal-difference {TD) methods, a class of incremental learning procedures specialized for prediction problems. (p. 2, 1. Introduction).
- **Evidence boundary:** the reported outcome is Figure 1. ....... t~~0 ~@ A game-playing example showing the inefficiency of supervised-learning methods. Each circle represents a position or class of positions from a two- person board game. The ... (p. 9, Figure/Table caption); the relevant task/metric cue is The )~ = t data points represent performances of the Widrow-Hoff supervised-learning procedure. a measure of the performance of a learning procedure on a training set, we used the root ... (p. 13, 3.2 A random-walk example). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** In a poh,-balancing problem one may want to predict time until a failure in balancing, and in a packet-switched telecomnnmications network one may want to pre(tict the total delay in ... (p. 25, 5.1 Predicting cumulative outcomes).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `CORE` in `RL, IL, offline learning, and robot data`; tags: `Robotics, Reinforcement Learning, temporal difference, Value Learning`.
- **Reading predecessor in the generated track queue:** start of this track queue (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Q-Learning (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** In speech recognition, for example, current learning methods cannot be applied until the correct classification of the word is known.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Now suppose you play a game that reaches a novel position (one that you have never seen before), that then progresses to reach the bad state, and that finally ends ... (p. 9, 3.1 A game-playing example); preserve the objective/update rule: The "bad" position is known from long experience to lead 90% of the time to a loss and only 10% of the time to a win. (p. 9, 3.1 A game-playing example).
2. Use the paper-reported task/data/environment cue: In principle, hmg chains of rule invocations can be learned in this way, with strength being passed back from rule to rule, thus tile name %ueket brigade." For a chain ... (p. 30, 6.3 Holland's bucket brigade).
3. Compare against the reported or matched baseline: This procedure may require as much as O(n a) computation per time step as compared to O(n) for the supervised-learning and TD methods. (p. 22, 4.2 Optimality and learning rate).
4. Report the body metric with its denominator and aggregation: The )~ = t data points represent performances of the Widrow-Hoff supervised-learning procedure. a measure of the performance of a learning procedure on a training set, we used the root ... (p. 13, 3.2 A random-walk example).
5. Re-run the reported ablation or stress/failure condition: In this way the effect of the 1 could be propagated back to the beginning of the sequence with only a single presentation. (p. 15, 3.2 A random-walk example); if none is reported, design one around: In a poh,-balancing problem one may want to predict time until a failure in balancing, and in a packet-switched telecomnnmications network one may want to pre(tict the total delay in ... (p. 25, 5.1 Predicting cumulative outcomes).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (1. Introduction), p. 8 (3. Examples of faster learning with TD methods), match the reported outcome at p. 9 (Figure/Table caption), p. 12 (3.2 A random-walk example), p. 14 (3.2 A random-walk example), and measure the boundary at p. 25 (5.1 Predicting cumulative outcomes), p. 1 (Abstract).

## Falsifiable research question

Under the paper's stated interface (Now suppose you play a game that reaches a novel position (one that you have never seen before), that then progresses to ...), does the paper-specific mechanism (S(!TTON In this article, we introduce and provide tilt first formal results in the theory of temporal-difference {TD) methods, a class of ...) retain the reported evaluation outcome (The )~ = t data points represent performances of the Widrow-Hoff supervised-learning procedure. a measure of the performance ...) when tested against the paper's strongest explicit boundary (In a poh,-balancing problem one may want to predict time until a failure in balancing, and in a ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (The )~ = t data points represent performances of the Widrow-Hoff supervised-learning procedure. a measure of the performance ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (36 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** S(!TTON In this article, we introduce and provide tilt first formal results in the theory of temporal-difference {TD) methods, a class of incremental learning procedures specialized for prediction problems. (p. 2, 1. Introduction).
- **Paper-supported outcome:** Figure 1. ....... t~~0 ~@ A game-playing example showing the inefficiency of supervised-learning methods. Each circle represents a position or class of positions from a two- person board game. The ... (p. 9, Figure/Table caption).
- **Strongest explicit boundary:** In a poh,-balancing problem one may want to predict time until a failure in balancing, and in a packet-switched telecomnnmications network one may want to pre(tict the total delay in ... (p. 25, 5.1 Predicting cumulative outcomes).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
