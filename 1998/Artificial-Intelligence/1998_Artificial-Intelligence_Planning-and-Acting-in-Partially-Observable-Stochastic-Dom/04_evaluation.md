# Evaluation - Planning and Acting in Partially Observable Stochastic Domains

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (45 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.sciencedirect.com/science/article/pii/S000437029800023X; PDF retrieval source: https://www.cassandra.org/arc/papers/aij98.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 18 (44 The Witness Algorithm), p. 20 (441 Witness inner loop), p. 20 (442 Identifying a witness), p. 21 (44.3. Checking the witness condition), p. 21 (44.3. Checking the witness condition), p. 22 (44.3. Checking the witness condition)): ‘To improve the complexity of the valueiteration algorithm, we must avoid generating V;*; instead, we would like to generate the elements of V; direct] Ifwe could do this, we might ...

## Evaluation Body Digest

- **p. 30 / 5.4 Plan Graphs - extractive body cue:** A plan graph is essentially a finite-state controller, It uses the minimal possible amount of memory to act optimally in a partially observable environment.
- **p. 15 / 1) I step to go - extractive body cue:** i pproptiately and so tends to gain less long-term reward.
- **p. 15 / 1) I step to go - extractive body cue:** In low entropy belief states, which are near the corners of the simplex, the agent can take actions more likely to be appropriate for the ...
- **p. 24 / 5.1 The Tiger Problem - extractive body cue:** Behind one of the doors is a tiger and behind the other is a large reward.
- **p. 24 / 4.5. Alternative Approaches - extractive body cue:** White and Scherer [65] propose an alternative approach in which the reward function is changed so that all of the algorithms discussed in this chapter ...
- **p. 25 / 5.1 The Tiger Problem - extractive body cue:** The reward for opening the correct door is +10 and the penalty for choosing the door with the tiger behind it is -100.
- **p. 25 / 5.1 The Tiger Problem - extractive body cue:** Immediately after the agent opens a door and receives a reward or penalty, the problem resets, randomly relocating the tiger behind one of the two ...
- **p. 28 / 5.3 Infinite-Horizon Policies - extractive body cue:** When we include a discount factor to decrease the value of future rewards, the structure of the finite-horizon POMDP value function changes slightly.

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** graph, configuration space 또는 task-and-motion planning domain.
- **Input boundary:** start/goal, map, dynamics와 successor/operator description.
- **Output/decision under evaluation:** feasible action sequence 또는 minimum-cost plan.
- **Primary target:** path cost, goal reachability, feasibility와 computation.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 44 The Witness Algorithm | SYSTEM / EVALUATION SCOPE UNRESOLVED | ‘To improve the complexity of the valueiteration algorithm, we must avoid generating V;*; instead, we would like to generate the elements of V; direct] ... | p. 18 (44 The Witness Algorithm) |
| 441 Witness inner loop | SYSTEM / EVALUATION SCOPE UNRESOLVED | The tree p is built with subtrees 7» for each observation 0, We add the new policy tree to Uy to improve the approximation. | p. 20 (441 Witness inner loop) |
| 442 Identifying a witness | SYSTEM / EVALUATION SCOPE UNRESOLVED | That is, if there is a belief state, b, for which Prey is an improvement over all the policy trees we have found so ... | p. 20 (442 Identifying a witness) |
| 44.3. Checking the witness condition | SYSTEM / EVALUATION SCOPE UNRESOLVED | If the linear program finds that the biggest advantage is not positive, that is, that 5 <0, then Pyew is not an improvement over ... | p. 21 (44.3. Checking the witness condition) |
| 44.3. Checking the witness condition | SYSTEM / EVALUATION SCOPE UNRESOLVED | The linear program in Table 3 solves exactly this problem, The variable d is the minimum amount of improvement of Pew Over any policy ... | p. 21 (44.3. Checking the witness condition) |

## Dataset / Benchmark Role

- **p. 30 / 5.4 Plan Graphs - extractive body cue:** A plan graph is essentially a finite-state controller, It uses the minimal possible amount of memory to act optimally in a partially observable environment.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 15 / Figure/Table caption - extractive body cue:** Fig. 6. A value function in three dimensions is made up of the upper surface of a. set of planes.
- **p. 17 / Figure/Table caption - extractive body cue:** Fig. 8. Some policy trees may be totally dominated by others and can be ignored.
- **p. 26 / Figure/Table caption - extractive body cue:** Fig. 10. The optimal situation-action mapping for t = 1 for the tiger problem shows that each of the three actions is optimal for some ...
- **p. 27 / Figure/Table caption - extractive body cue:** Fig. 13. The optimal non-stationary policy for ¢=4 has a rich streture.
- **p. 29 / Figure/Table caption - extractive body cue:** Fig. 15. Edges can be rearrangpd to form a stationary policy.

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | A plan graph is essentially a finite-state controller, It uses the minimal possible amount of memory to act optimally in a partially observable environment. | embodiment, simulator version and control stack | p. 30 (5.4 Plan Graphs) |
| Task/environment | not stated or recoverable in the selected PDF body | reset, timeout, object/scene variation | 본문 anchor 없음 |
| Observation/sensor | start/goal, map, dynamics와 successor/operator description | calibration, preprocessing, privileged input | p. 9 (3.2 Problem Structure), p. 3 (1 Introduction) |
| Output/decision | feasible action sequence 또는 minimum-cost plan | action frame, controller and termination | p. 10 (3.2 Problem Structure), p. 25 (5.1 The Tiger Problem) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| i pproptiately and so tends to gain less long-term reward. | definition/direction/unit from same section | p. 15 (1) I step to go) |
| In low entropy belief states, which are near the corners of the simplex, the agent can take actions more likely to be appropriate for ... | definition/direction/unit from same section | p. 15 (1) I step to go) |
| Behind one of the doors is a tiger and behind the other is a large reward. | definition/direction/unit from same section | p. 24 (5.1 The Tiger Problem) |
| White and Scherer [65] propose an alternative approach in which the reward function is changed so that all of the algorithms discussed in this ... | definition/direction/unit from same section | p. 24 (4.5. Alternative Approaches) |
| The reward for opening the correct door is +10 and the penalty for choosing the door with the tiger behind it is -100. | definition/direction/unit from same section | p. 25 (5.1 The Tiger Problem) |
| Immediately after the agent opens a door and receives a reward or penalty, the problem resets, randomly relocating the tiger behind one of the ... | definition/direction/unit from same section | p. 25 (5.1 The Tiger Problem) |
| When we include a discount factor to decrease the value of future rewards, the structure of the finite-horizon POMDP value function changes slightly. | definition/direction/unit from same section | p. 28 (5.3 Infinite-Horizon Policies) |
| As the horizon ¢ increases, the rewards received for the final few steps have decreasing influence on the situation-action mappings for earlier time steps ... | definition/direction/unit from same section | p. 28 (5.3 Infinite-Horizon Policies) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| As a result, compared to exhaustive caumeration, very few nonuseful policy trees are considered and the algorithm runs extremely quickly. | comparison identity and matched condition | p. 24 (4.5. Alternative Approaches) |
| This structure counts the relative nnmber of times the tiger was heard on the left as compared to the right, | comparison identity and matched condition | p. 30 (5.4 Plan Graphs) |
| This is because the behavior of ‘these algorithms on this problem appears to be extremely sensitive to the numerical precision used in comparisons-the better ... | comparison identity and matched condition | p. 29 (5.4 Plan Graphs) |
| The optimal action for cach belief state in this region is a(p), the action in the root node of policy tree p; furthermore, the ... | comparison identity and matched condition | p. 16 (1) I step to go) |
| One drawback of the POMDP approach is that the agent must maintain a belief state and use it to select an optimal action on ... | comparison identity and matched condition | p. 29 (5.4 Plan Graphs) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Note that we are defining two trees to be equal if they have the same value function; this makes it unnecessary to deal with ... | component/input/data sensitivity | p. 38 (A. Appendix) |
| The optimal action for cach belief state in this region is a(p), the action in the root node of policy tree p; furthermore, the ... | component/input/data sensitivity | p. 16 (1) I step to go) |
| The simplest pruning strategy, proposed by Sondik [58,42], is to test R(a, Y) for every a in V and remove those a that are ... | component/input/data sensitivity | p. 17 (42 Value Functions as Sets of Vectors) |
| If no witness points are discovered, then that policy tree is removed from the agenda, When the agenda is empty, the algorithm terminates. | component/input/data sensitivity | p. 22 (444 A single step of value iteration) |
| Each of these linear programs either removes a policy tree from the agenda (this happens at most 1+ ([Vi-1/ - 1)/®[]Q¢] times) or a ... | component/input/data sensitivity | p. 22 (444 A single step of value iteration) |
| This is because the behavior of ‘these algorithms on this problem appears to be extremely sensitive to the numerical precision used in comparisons-the better ... | component/input/data sensitivity | p. 29 (5.4 Plan Graphs) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| This paper is intended to make two contributions. | ‘To improve the complexity of the valueiteration algorithm, we must avoid generating V;*; instead, we would like to generate the elements of V; direct] ... | PDF body cue; verify exact table/figure and matched conditions | p. 18 (44 The Witness Algorithm), p. 20 (441 Witness inner loop), p. 20 (442 Identifying a witness), p. 21 (44.3. Checking the witness condition), p. 21 (44.3. Checking the witness condition), p. 22 (44.3. Checking the witness condition) |
| Primary metric/result | The tree p is built with subtrees 7» for each observation 0, We add the new policy tree to Uy to improve the approximation. | numeric claim only at cited anchor | p. 20 (441 Witness inner loop) |

- Numeric sentences retained from the body:
- **p. 19 / 44 The Witness Algorithm - extractive body cue:** Vi(b), we can express (Q(b) (recall that this is the value of taking action a in belief state b and continuing optimally for t- 1 ...
- **p. 19 / 44 The Witness Algorithm - extractive body cue:** Vi(b), we can express (Q(b) (recall that this is the value of taking action a in belief state b and continuing optimally for t- 1 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In such belief states, the agent cannot select | p. 15 (1) I step to go) |
| body limitation/failure cue | Pruning requires one linear program for each element of the starting set of policy trees and does not add to the asymptotic complexity of ... | p. 18 (42 Value Functions as Sets of Vectors) |
| body limitation/failure cue | The LISTEN action does not change the state of the world. | p. 25 (5.1 The Tiger Problem) |
| body limitation/failure cue | If the agent starts from the uniform belief state, b= (0.5,0.5), listening once does not change the belief state enough to make the expected ... | p. 26 (5.2. Finite-Horizon Policies) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| When an agent has one step remaining, all it can do is take a single action, With two steps to go, it can take ... | p. 12 (4.1 Policy Trees) |
| The new problem, then, is how to compute a parsimonious representation of Vj from a parsimonious representation of Vii. | p. 17 (42 Value Functions as Sets of Vectors) |
| The value function for a POMDP can be computed using value iteration, with the same basic structure as for the discrete MDP case. | p. 17 (42 Value Functions as Sets of Vectors) |
| The value functions for the policy trees in Vj can be computed efficiently from those of the subtrees. | p. 18 (42 Value Functions as Sets of Vectors) |
| We can compute V; by taking the union of the Q2 sets for all actions and pruning as described in the previous section. | p. 18 (44 The Witness Algorithm) |
| The code in Table 2 outlines our approach to solving PompPs. | p. 19 (44 The Witness Algorithm) |
| Vi(b), we can express (Q(b) (recall that this is the value of taking action a in belief state b and continuing optimally for t- ... | p. 19 (44 The Witness Algorithm) |
| iteration we ask, Is there some belief state b for which the true value Q(B), computed by one-step lookahead using Vj-1, is different from ... | p. 20 (441 Witness inner loop) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 15 / 1) I step to go - extractive body cue:** In such belief states, the agent cannot select
- **p. 18 / 42 Value Functions as Sets of Vectors - extractive body cue:** Pruning requires one linear program for each element of the starting set of policy trees and does not add to the asymptotic complexity of the ...
- **p. 25 / 5.1 The Tiger Problem - extractive body cue:** The LISTEN action does not change the state of the world.
- **p. 26 / 5.2. Finite-Horizon Policies - extractive body cue:** If the agent starts from the uniform belief state, b= (0.5,0.5), listening once does not change the belief state enough to make the expected value ...

- **Evidence anchors reviewed:** datasets p. 30 (5.4 Plan Graphs), metrics p. 15 (1) I step to go), p. 15 (1) I step to go), p. 24 (5.1 The Tiger Problem), p. 24 (4.5. Alternative Approaches), p. 25 (5.1 The Tiger Problem), p. 25 (5.1 The Tiger Problem), baselines p. 24 (4.5. Alternative Approaches), p. 30 (5.4 Plan Graphs), p. 29 (5.4 Plan Graphs), p. 16 (1) I step to go), p. 29 (5.4 Plan Graphs), results p. 18 (44 The Witness Algorithm), p. 20 (441 Witness inner loop), p. 20 (442 Identifying a witness), p. 21 (44.3. Checking the witness condition), p. 21 (44.3. Checking the witness condition), p. 22 (44.3. Checking the witness condition).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (45 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** The linear program in Table 3 solves exactly this problem, The variable d is the minimum amount of improvement of Pew Over any policy tree in Uy at b. (p. 21, 44.3. Checking the witness condition).
- **Metric evidence:** i pproptiately and so tends to gain less long-term reward. (p. 15, 1) I step to go).
- **Baseline/ablation evidence:** This is because the behavior of ‘these algorithms on this problem appears to be extremely sensitive to the numerical precision used in comparisons-the better the precision, the longer the algorithms ... (p. 29, 5.4 Plan Graphs).
- **Failure/negative evidence:** as the agent does not observe the goal state, it will alwajrs have some non-zero belief that it is in any of the non-goal states, since the actions have non-zero ... (p. 11, 3.2 Problem Structure).
