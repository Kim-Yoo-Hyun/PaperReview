# Evaluation - Learning to Predict by the Methods of Temporal Differences

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (36 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1007/BF00115009; PDF retrieval source: https://doi.org/10.1007/BF00115009. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 13 (3.2 A random-walk example), p. 29 (6.1 Samuel's checker-playing program), p. 30 (6.3 Holland's bucket brigade), p. 14 (3.2 A random-walk example), p. 12 (3.2 A random-walk example), p. 12 (3.2 A random-walk example)): Averaging over training sets, we found that performance improved rapidly as A was reduced below 1 (the supervised-learning method) and was best at ,~ = 0 (the extreme TD method), ...

## Evaluation Body Digest

- **p. 12 / 3.2 A random-walk example - extractive body cue:** This measure was averaged over 100 training sets to produce the data shown.
- **p. 12 / 3.2 A random-walk example - extractive body cue:** Instead, the Aw's were accumulated over sequences and only used to update the weight vector after the complete presentation of a training set.
- **p. 13 / 3.2 A random-walk example - extractive body cue:** The second experiment concerns the question of learning rate when the training set is presented just once rather than repeatedly until convergence.
- **p. 13 / 3.2 A random-walk example - extractive body cue:** The answer is that the Widrow-Hoff procedure only minimizes error on the training set; it does not necessarily minimize error for future experience.
- **p. 14 / 3.2 A random-walk example - extractive body cue:** First, each training set was presented once to each procedure.
- **p. 14 / 3.2 A random-walk example - extractive body cue:** Second, weight updates were performed after each sequence, as in (1), rather than after each complete training set.
- **p. 21 / 4.2 Optimality and learning rate - extractive body cue:** What might one mean by the %est'" predictions given such a training set'?
- **p. 21 / 4.2 Optimality and learning rate - extractive body cue:** In the following, we first define what we mean by optimal predictions for finite training sets.

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** robot/environment의 sequential decision process.
- **Input boundary:** state 또는 observation, action, reward와 transition history.
- **Output/decision under evaluation:** action policy와 induced trajectory.
- **Primary target:** expected return, task success, stability와 sample efficiency.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 3.2 A random-walk example | SYSTEM / EVALUATION SCOPE UNRESOLVED | Averaging over training sets, we found that performance improved rapidly as A was reduced below 1 (the supervised-learning method) and was best at ,~ ... | p. 13 (3.2 A random-walk example) |
| 6.1 Samuel's checker-playing program | SYSTEM / EVALUATION SCOPE UNRESOLVED | Nevertheless, SamueFs learning procedure was overall very successful; it played an imt)ortant role in significantly improving the play of his checkerplaying program until it ... | p. 29 (6.1 Samuel's checker-playing program) |
| 6.3 Holland's bucket brigade | SYSTEM / EVALUATION SCOPE UNRESOLVED | In principle, hmg chains of rule invocations can be learned in this way, with strength being passed back from rule to rule, thus tile ... | p. 30 (6.3 Holland's bucket brigade) |
| 3.2 A random-walk example | SYSTEM / EVALUATION SCOPE UNRESOLVED | Not surprisingly, the value of a had a significant effect on performance, with best results obtained with intermediate values. | p. 14 (3.2 A random-walk example) |
| 3.2 A random-walk example | SYSTEM / EVALUATION SCOPE UNRESOLVED | The A = 1 data point is the performance level attained by the Widrow-Hoff procedure. | p. 12 (3.2 A random-walk example) |

## Dataset / Benchmark Role

- **p. 12 / 3.2 A random-walk example - extractive body cue:** This measure was averaged over 100 training sets to produce the data shown.
- **p. 12 / 3.2 A random-walk example - extractive body cue:** Instead, the Aw's were accumulated over sequences and only used to update the weight vector after the complete presentation of a training set.
- **p. 13 / 3.2 A random-walk example - extractive body cue:** The second experiment concerns the question of learning rate when the training set is presented just once rather than repeatedly until convergence.
- **p. 13 / 3.2 A random-walk example - extractive body cue:** The answer is that the Widrow-Hoff procedure only minimizes error on the training set; it does not necessarily minimize error for future experience.
- **p. 14 / 3.2 A random-walk example - extractive body cue:** First, each training set was presented once to each procedure.
- **p. 14 / 3.2 A random-walk example - extractive body cue:** Second, weight updates were performed after each sequence, as in (1), rather than after each complete training set.
- **p. 21 / 4.2 Optimality and learning rate - extractive body cue:** What might one mean by the %est'" predictions given such a training set'?
- **p. 21 / 4.2 Optimality and learning rate - extractive body cue:** In the following, we first define what we mean by optimal predictions for finite training sets.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 9 / Figure/Table caption - extractive body cue:** Figure 1. ....... t~~0 ~@ A game-playing example showing the inefficiency of supervised-learning methods. Each circle represents a position or class of positions from a ...
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 2. A generator of bounded random walks. This Markov process generated the data sequences in the example. All walks begin in state D. From ...
- **p. 12 / Figure/Table caption - extractive body cue:** Figure 3. ERROR USING BEST o~ .20 .18 .16 .14.
- **p. 13 / Figure/Table caption - extractive body cue:** Figure 4. Average error on random walk problem after experiencing 10 sequences. All data are from TD(~) with different values of a and A. The ...
- **p. 14 / Figure/Table caption - extractive body cue:** Figure 5. Average error at best ~ value on random-walk problem. Each data point represents the average over 100 training sets of the error in ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | This measure was averaged over 100 training sets to produce the data shown. | embodiment, simulator version and control stack | p. 12 (3.2 A random-walk example), p. 12 (3.2 A random-walk example) |
| Task/environment | Instead, the Aw's were accumulated over sequences and only used to update the weight vector after the complete presentation of a training set. | reset, timeout, object/scene variation | p. 12 (3.2 A random-walk example), p. 13 (3.2 A random-walk example) |
| Observation/sensor | state 또는 observation, action, reward와 transition history | calibration, preprocessing, privileged input | p. 11 (3.2 A random-walk example), p. 11 (3.2 A random-walk example) |
| Output/decision | action policy와 induced trajectory | action frame, controller and termination | p. 3 (1. Introduction), p. 9 (3.1 A game-playing example) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The )~ = t data points represent performances of the Widrow-Hoff supervised-learning procedure. a measure of the performance of a learning procedure on a ... | definition/direction/unit from same section | p. 13 (3.2 A random-walk example) |
| In Samuel's learning procedure, the difference between the evaluations of each pair of successive positions occurring in a game was used as an error; ... | definition/direction/unit from same section | p. 28 (6.1 Samuel's checker-playing program) |
| Figure 3. ERROR USING BEST o~ .20 .18 .16 .14. | definition/direction/unit from same section | p. 12 (Figure/Table caption) |
| SUTTON I I i I I I 0.0 0.2 0.4 0.6 0.8 1.0 A Average error on the random-walk problem under repeated presentations. | definition/direction/unit from same section | p. 12 (3.2 A random-walk example) |
| Average error on random walk problem after experiencing 10 sequences. | definition/direction/unit from same section | p. 13 (3.2 A random-walk example) |
| Average error at best ~ value on random-walk problem. | definition/direction/unit from same section | p. 14 (3.2 A random-walk example) |
| The a value was selected from those shown in Figure 4 to yield the lowest error for that ), value. procedural changes. | definition/direction/unit from same section | p. 14 (3.2 A random-walk example) |
| The WidrowHoff rule, on the other hand, converges to the estimates that minimize error on | definition/direction/unit from same section | p. 23 (4.2 Optimality and learning rate) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| This procedure may require as much as O(n a) computation per time step as compared to O(n) for the supervised-learning and TD methods. | comparison identity and matched condition | p. 22 (4.2 Optimality and learning rate) |
| What is still needed is a characterization of the learning rate of TD methods that can be compared with those already available for supervised-learning ... | comparison identity and matched condition | p. 24 (4.2 Optimality and learning rate) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| In this way the effect of the 1 could be propagated back to the beginning of the sequence with only a single presentation. | component/input/data sensitivity | p. 15 (3.2 A random-walk example) |
| For a multi-step prediction problem, f Each time step's weight increments are then determined using VwQ(w, st), relying on the fact that Ex{V,,,Q(w,x)} = ... | component/input/data sensitivity | p. 24 (4.3 Temporal-difference methods as gradient descent) |
| For example, a constant function could still have been attained by setting the modifiable terms so as to cancel the effect of tile non-modifiable ... | component/input/data sensitivity | p. 29 (6.1 Samuel's checker-playing program) |
| Fourth, so that there was no bias either toward right-side or left-side terminations, all components of the weight vector were initially set to 0.5. | component/input/data sensitivity | p. 14 (3.2 A random-walk example) |
| Let Q denote the matrix with entries [Q],j = pij for i,j E N, and let h denote the vector with components [h]i = ... | component/input/data sensitivity | p. 16 (4.1 Convergence of linear TD(0)) |
| Second, the procedure involves keeping statistics on each pair of states (e.g., the :Siy) rather than on each state or component of the observation ... | component/input/data sensitivity | p. 22 (4.2 Optimality and learning rate) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| S(!TTON In this article, we introduce and provide tilt first formal results in the theory of temporal-difference {TD) methods, a class of incremental learning ... | Averaging over training sets, we found that performance improved rapidly as A was reduced below 1 (the supervised-learning method) and was best at ,~ ... | PDF body cue; verify exact table/figure and matched conditions | p. 13 (3.2 A random-walk example), p. 29 (6.1 Samuel's checker-playing program), p. 30 (6.3 Holland's bucket brigade), p. 14 (3.2 A random-walk example), p. 12 (3.2 A random-walk example), p. 12 (3.2 A random-walk example) |
| Primary metric/result | Nevertheless, SamueFs learning procedure was overall very successful; it played an imt)ortant role in significantly improving the play of his checkerplaying program until it ... | numeric claim only at cited anchor | p. 29 (6.1 Samuel's checker-playing program) |

- Numeric sentences retained from the body:
- **p. 18 / 4.1 Convergence of linear TD(0) - extractive body cue:** Assuming for the inoment that limn-~o¢ (I - aXTXD(1 - Q))n = 0, then, by theorem A.
- **p. 18 / 4.1 Convergence of linear TD(0) - extractive body cue:** It thus remains to show that limn-~o~ (I-aXTXD(IQ))n = 0.
- **p. 22 / 4.2 Optimality and learning rate - extractive body cue:** Thus, lim,~_-~c¢ (~n = 0 and Theorem A.1 applies, assuring the existence of the limit and inverse in the above equation.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In speech recognition, for example, current learning methods cannot be applied until the correct classification of the word is known. | p. 32 (7. Conclusion) |
| body limitation/failure cue | In a poh,-balancing problem one may want to predict time until a failure in balancing, and in a packet-switched telecomnnmications network one may want ... | p. 25 (5.1 Predicting cumulative outcomes) |
| body limitation/failure cue | We cannot apply this lemma directly to D(I - Q) because it is not symmetric. | p. 19 (4.1 Convergence of linear TD(0)) |
| body limitation/failure cue | SUTTON and biased coins, and thus cannot be uniquely determined. | p. 22 (4.2 Optimality and learning rate) |
| body limitation/failure cue | Although this problem involves a sequence of predictions, TD methods cannot be directly applied because each prediction is of a different event and thus ... | p. 27 (5.3 Prediction by a fixed interval) |
| body limitation/failure cue | The answer is that the Widrow-Hoff procedure only minimizes error on the training set; it does not necessarily minimize error for future experience. | p. 13 (3.2 A random-walk example) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Although it is difficult to prove a theorem concerning learning rate, it is easy to perform the relevant computational experiment. | p. 13 (3.2 A random-walk example) |
| The second experiment concerns the question of learning rate when the training set is presented just once rather than repeatedly until convergence. | p. 13 (3.2 A random-walk example) |
| This result also helps explain TD methods' empirically faster learning rates. | p. 21 (4.2 Optimality and learning rate) |
| What is still needed is a characterization of the learning rate of TD methods that can be compared with those already available for supervised-learning ... | p. 24 (4.2 Optimality and learning rate) |
| A bounded random walk is a state sequence generated by taking random steps to the right or to the left until a boundary is ... | p. 11 (3.2 A random-walk example) |
| For all procedures, weight increments were computed according to TD(A), as given by (4). | p. 12 (3.2 A random-walk example) |
| The true probabilities of right-side termination the ideal predictions - for each of the nonterminal states can be computed as described in section 4.1. ... | p. 12 (3.2 A random-walk example) |
| The drawback to this technique is that it loses the implementation advantages of TD methods. | p. 15 (3.2 A random-walk example) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 32 / 7. Conclusion - extractive body cue:** In speech recognition, for example, current learning methods cannot be applied until the correct classification of the word is known.
- **p. 25 / 5.1 Predicting cumulative outcomes - extractive body cue:** In a poh,-balancing problem one may want to predict time until a failure in balancing, and in a packet-switched telecomnnmications network one may want to ...
- **p. 19 / 4.1 Convergence of linear TD(0) - extractive body cue:** We cannot apply this lemma directly to D(I - Q) because it is not symmetric.
- **p. 22 / 4.2 Optimality and learning rate - extractive body cue:** SUTTON and biased coins, and thus cannot be uniquely determined.
- **p. 27 / 5.3 Prediction by a fixed interval - extractive body cue:** Although this problem involves a sequence of predictions, TD methods cannot be directly applied because each prediction is of a different event and thus there ...
- **p. 13 / 3.2 A random-walk example - extractive body cue:** The answer is that the Widrow-Hoff procedure only minimizes error on the training set; it does not necessarily minimize error for future experience.

- **PDF anchors reviewed:** datasets p. 12 (3.2 A random-walk example), p. 12 (3.2 A random-walk example), p. 13 (3.2 A random-walk example), p. 13 (3.2 A random-walk example), p. 14 (3.2 A random-walk example), p. 14 (3.2 A random-walk example), metrics p. 13 (3.2 A random-walk example), p. 28 (6.1 Samuel's checker-playing program), p. 12 (Figure/Table caption), p. 12 (3.2 A random-walk example), p. 13 (3.2 A random-walk example), p. 14 (3.2 A random-walk example), baselines p. 22 (4.2 Optimality and learning rate), p. 24 (4.2 Optimality and learning rate), results p. 13 (3.2 A random-walk example), p. 29 (6.1 Samuel's checker-playing program), p. 30 (6.3 Holland's bucket brigade), p. 14 (3.2 A random-walk example), p. 12 (3.2 A random-walk example), p. 12 (3.2 A random-walk example).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
