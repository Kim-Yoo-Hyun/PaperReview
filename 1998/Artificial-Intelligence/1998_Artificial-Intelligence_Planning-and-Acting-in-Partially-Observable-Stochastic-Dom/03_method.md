# Method - Planning and Acting in Partially Observable Stochastic Domains

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (45 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.sciencedirect.com/science/article/pii/S000437029800023X; PDF retrieval source: https://www.cassandra.org/arc/papers/aij98.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 23 (4.5. Alternative Approaches), p. 19 (44 The Witness Algorithm), p. 7 (2.9 Computing an Optimal Policy), p. 23 (4.5. Alternative Approaches), p. 18 (44 The Witness Algorithm), p. 18 (44 The Witness Algorithm)): The resulting algorithm might be called the two-pass algorithm [9], and, its form is much like the witness algorithm because it first constructs each separate Q-function, then combines the Q-functions ...

## Method Body Digest

- **p. 23 / 4.5. Alternative Approaches - extractive body cue:** The resulting algorithm might be called the two-pass algorithm [9], and, its form is much like the witness algorithm because it first constructs each separate ...
- **p. 19 / 44 The Witness Algorithm - extractive body cue:** This is because maximizing over actions and then policy trees is the same as maximizing over the pooled sets of policy trees.
- **p. 7 / 2.9 Computing an Optimal Policy - extractive body cue:** Tt makes use of an aundliary function, Q/(s), which is the tstep value of starting in state s, taking action a, then continuing with the ...
- **p. 23 / 4.5. Alternative Approaches - extractive body cue:** Although the algorithm is sophisticated and, in principle, avoids exhaustively enumerating the set of possibly useful policy trees at each iteration, it appears to run ...
- **p. 18 / 44 The Witness Algorithm - extractive body cue:** Tn what sense is the witness algorithm superior to previous algorithms for solving Pompps, then?
- **p. 18 / 44 The Witness Algorithm - extractive body cue:** The witness algorithm is a method for computing Q? in time polynomial in /S], [AJ [2/, [V.-1[, and /Q] (specifically, run time is polynomial in ...
- **p. 7 / 2.9 Computing an Optimal Policy - extractive body cue:** If /Vi(s)-Vi-a(s)/ < € for all s, then the value of the greedy policy with respect to V; does not differ from V* by more ...
- **p. 19 / 44 The Witness Algorithm - extractive body cue:** From the definition of the state estimator SE and the t-step value function

## Design Rationale

- **p. 3 / 1 Introduction - extractive body cue:** This paper is intended to make two contributions.
- **p. 3 / 1 Introduction - extractive body cue:** The second is to describe a novel algorithmic approach for solving POMDPs exactly.
- **p. 19 / 44 The Witness Algorithm - extractive body cue:** The code in Table 2 outlines our approach to solving PompPs.

## Source Evidence Cues

- **p. 23 / 4.5. Alternative Approaches - extractive body cue:** The resulting algorithm might be called the two-pass algorithm [9], and, its form is much like the witness algorithm because it first constructs each separate ...
- **p. 19 / 44 The Witness Algorithm - extractive body cue:** This is because maximizing over actions and then policy trees is the same as maximizing over the pooled sets of policy trees.
- **p. 7 / 2.9 Computing an Optimal Policy - extractive body cue:** Tt makes use of an aundliary function, Q/(s), which is the tstep value of starting in state s, taking action a, then continuing with the ...
- **p. 23 / 4.5. Alternative Approaches - extractive body cue:** Although the algorithm is sophisticated and, in principle, avoids exhaustively enumerating the set of possibly useful policy trees at each iteration, it appears to run ...
- **p. 18 / 44 The Witness Algorithm - extractive body cue:** Tn what sense is the witness algorithm superior to previous algorithms for solving Pompps, then?
- **p. 18 / 44 The Witness Algorithm - extractive body cue:** The witness algorithm is a method for computing Q? in time polynomial in /S], [AJ [2/, [V.-1[, and /Q] (specifically, run time is polynomial in ...
- **p. 7 / 2.9 Computing an Optimal Policy - extractive body cue:** If /Vi(s)-Vi-a(s)/ < € for all s, then the value of the greedy policy with respect to V; does not differ from V* by more ...
- **Detected method headings:** 2.9 Computing an Optimal Policy (p. 7); 3.4 Finding an Optimal Policy (p. 11); 4.1 Policy Trees (p. 12); 44 The Witness Algorithm (p. 18); 4.5. Alternative Approaches (p. 23); 6.3 Transition Model (p. 33); 6.4 Observation Model (p. 34)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Problem / state representation | decision state와 feasible set을 만든다 | state, map, goal, constraints | source-specific graph, symbolic state, belief 또는 configuration representation을 구성 | search/optimization state | The resulting algorithm might be called the two-pass algorithm [9], and, its form is much like the witness algorithm because it first ... | p. 23 (4.5. Alternative Approaches), p. 19 (44 The Witness Algorithm) |
| Search / trajectory decision | goal을 향한 candidate를 생성·개선한다 | state와 cost/heuristic | search, sampling, dynamic programming 또는 trajectory optimization을 적용 | plan, path, option 또는 trajectory | This is because maximizing over actions and then policy trees is the same as maximizing over the pooled sets of policy trees. | p. 19 (44 The Witness Algorithm), p. 7 (2.9 Computing an Optimal Policy) |
| Execution interface | 계획을 실행 가능한 command로 변환한다 | plan과 current feedback | collision/contact/dynamics check, smoothing, replanning 또는 controller handoff를 수행 | waypoint, option, action 또는 reference | Tt makes use of an aundliary function, Q/(s), which is the tstep value of starting in state s, taking action a, then ... | p. 7 (2.9 Computing an Optimal Policy), p. 23 (4.5. Alternative Approaches) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 19 / 44 The Witness Algorithm - extractive body cue:** This is because maximizing over actions and then policy trees is the same as maximizing over the pooled sets of policy trees.
- **p. 19 / 44 The Witness Algorithm - extractive body cue:** From the definition of the state estimator SE and the t-step value function
- **p. 12 / 3.4 Finding an Optimal Policy - extractive body cue:** and © p(b,a) is the reward function on belief states, constructed from the original reward function on world states:
- **p. 12 / 3.4 Finding an Optimal Policy - extractive body cue:** The reward function may seem strange; the agent appears to be rewarded for merely believing that it is in good states.
- **p. 23 / 4.5. Alternative Approaches - extractive body cue:** For each one, it creates a set of constraints that form the border of the true region, then searches those borders to determine whether another ...
- **p. 24 / 4.5. Alternative Approaches - extractive body cue:** White and Scherer [65] propose an alternative approach in which the reward function is changed so that all of the algorithms discussed in this chapter ...
- **Formal bridge:** s/q -> a/ξ ∈ feasible decisions -> path/task cost or expected utility -> success/reachability and constraint satisfaction.
- **Equation/algorithm anchors:** p. 23 (4.5. Alternative Approaches), p. 19 (44 The Witness Algorithm).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | component, labeled, state, estimator, responsible, updating, belief, last, action, current, observation, previous, policy, before | start/goal, map, dynamics와 successor/operator description | body cue; exact tensor/frame verify |
| State/latent | component, labeled, state, estimator, responsible, updating, belief, last, action, current | path, trajectory, symbolic state 또는 task-motion decision | body cue; notation verify |
| Action/output | intended, make, contributions, second, describe, novel, algorithmic, solving, POMDPs, exactly | feasible action sequence 또는 minimum-cost plan | body cue; unit/decoder verify |
| Objective/constraint | because, maximizing, over, actions, then, policy, trees, same, pooled, sets | path/task cost or expected utility | equation anchor required |

## Observation–State–Action Interface

- **p. 9 / 3.2 Problem Structure - extractive body cue:** The component labeled SE is the state estimator: it is responsible for updating the belief state based on the last action, the current observation, and ...
- **p. 3 / 1 Introduction - extractive body cue:** As shown in Figure 1, the agent takes as input the state of the world and generates as output actions, which themselves affect the state ...
- **p. 10 / 3.2 Problem Structure - extractive body cue:** These distributions encode the agent's subjective probability about the state of the world and provide a basis for acting under uncertainty, Further more, they comprise ...
- **p. 25 / 5.1 The Tiger Problem - extractive body cue:** No matter what state the world is in, the LEFT and RIGHT actions result in either observation with probability 0.5.
- **p. 25 / 5.1 The Tiger Problem - extractive body cue:** The LEFT and RIGHT actions cause a transition to world state sy with probability .5 and to state s, with probability .5 (essentially resetting the ...
- **p. 11 / 3.4 Finding an Optimal Policy - extractive body cue:** The policy component of a POMDP agent must map the current belief state into action.
- **p. 5 / 2.2 Acting Optimally - extractive body cue:** The policy 7 is to be used to choose the action on the to-last step as a function of the current state, s,.
- **Normalized interface:** observation=start/goal, map, dynamics와 successor/operator description; state=path, trajectory, symbolic state 또는 task-motion decision; output/action=feasible action sequence 또는 minimum-cost plan.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | start/goal 또는 task sequence까지의 long-horizon plan; exact horizon은 paper-specific. | As the horizon ¢ increases, the rewards received for the final few steps have decreasing influence on the situation-action mappings for earlier ... | episode/sequence/action-chunk boundary |
| Rate / latency | query/event-driven planning 뒤 controller가 partial plan을 실행; numeric rate 확인 필요. | A stationary policy, 7: S + A, isa situation-action mapping that specifies, for each state, an action to be taken. ‘The choice ... | Hz/fps, inference time and control rate |
| Memory | graph/tree/roadmap/plan and current state; history size는 method-specific. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | collision checking, search branching 또는 optimization iterations가 latency를 결정한다. | Vi(b), we can express (Q(b) (recall that this is the value of taking action a in belief state b and continuing optimally ... | hardware, batch and throughput |

## Training vs Inference

- training/inference separation PDF body cue not selected; no claim inferred

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** resulting, algorithm, might, called, two-pass, form, much, like, witness, because, first, constructs, separate, Q-function, then, combines, Q-functions, together, create, optimal.
- **Relevant PDF headings:** 2.9 Computing an Optimal Policy (p. 7); 3.4 Finding an Optimal Policy (p. 11); 4.1 Policy Trees (p. 12); 44 The Witness Algorithm (p. 18); 4.5. Alternative Approaches (p. 23); 6.3 Transition Model (p. 33); 6.4 Observation Model (p. 34).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Problem / state representation | A plan graph is essentially a finite-state controller, It uses the minimal possible amount of memory to act optimally in a partially ... | p. 30 (5.4 Plan Graphs), p. 15 (1) I step to go) |
| Search / trajectory decision | As a result, compared to exhaustive caumeration, very few nonuseful policy trees are considered and the algorithm runs extremely quickly. | p. 24 (4.5. Alternative Approaches), p. 30 (5.4 Plan Graphs) |
| Execution interface | ‘To improve the complexity of the valueiteration algorithm, we must avoid generating V;*; instead, we would like to generate the elements of ... | p. 18 (44 The Witness Algorithm), p. 20 (441 Witness inner loop) |

## Failure and Ablation Link

- **p. 38 / A. Appendix - extractive body cue:** Note that we are defining two trees to be equal if they have the same value function; this makes it unnecessary to deal with the ...
- **p. 16 / 1) I step to go - extractive body cue:** The optimal action for cach belief state in this region is a(p), the action in the root node of policy tree p; furthermore, the entire ...
- **p. 17 / 42 Value Functions as Sets of Vectors - extractive body cue:** The simplest pruning strategy, proposed by Sondik [58,42], is to test R(a, Y) for every a in V and remove those a that are nowhere ...
- **p. 22 / 444 A single step of value iteration - extractive body cue:** If no witness points are discovered, then that policy tree is removed from the agenda, When the agenda is empty, the algorithm terminates.
- **p. 22 / 444 A single step of value iteration - extractive body cue:** Each of these linear programs either removes a policy tree from the agenda (this happens at most 1+ ([Vi-1/ - 1)/®[]Q¢] times) or a witness ...
- **p. 29 / 5.4 Plan Graphs - extractive body cue:** This is because the behavior of ‘these algorithms on this problem appears to be extremely sensitive to the numerical precision used in comparisons-the better the ...
- **p. 29 / 5.4 Plan Graphs - extractive body cue:** One drawback of the POMDP approach is that the agent must maintain a belief state and use it to select an optimal action on every ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 23 (4.5. Alternative Approaches), p. 19 (44 The Witness Algorithm), p. 7 (2.9 Computing an Optimal Policy), p. 23 (4.5. Alternative Approaches), p. 18 (44 The Witness Algorithm), p. 18 (44 The Witness Algorithm), objective p. 19 (44 The Witness Algorithm), p. 19 (44 The Witness Algorithm), p. 12 (3.4 Finding an Optimal Policy), p. 12 (3.4 Finding an Optimal Policy), p. 23 (4.5. Alternative Approaches), p. 24 (4.5. Alternative Approaches), temporal p. 28 (5.3 Infinite-Horizon Policies), p. 5 (2.2 Acting Optimally), p. 25 (5.2. Finite-Horizon Policies), p. 26 (5.2. Finite-Horizon Policies), p. 28 (5.3 Infinite-Horizon Policies), p. 4 (2.2 Acting Optimally).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (45 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Tt makes use of an aundliary function, Q/(s), which is the tstep value of starting in state s, taking action a, then continuing with the optimal (t-1)= step norstationary policy. (p. 7, 2.9 Computing an Optimal Policy).
- **Objective/update evidence:** Tn what sense is the witness algorithm superior to previous algorithms for solving Pompps, then? (p. 18, 44 The Witness Algorithm).
- **Temporal/runtime evidence:** One such framework is finito-horizon optimality, (p. 4, 2.2 Acting Optimally).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
