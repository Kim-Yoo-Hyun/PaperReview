# Policy Gradient Methods for Reinforcement Learning with Function Approximation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.neurips.cc/paper/1999/hash/464d828b85b0bed98e80ade0a5c43b0f-Abstract.html.
> PDF retrieval source: https://proceedings.neurips.cc/paper/1999/hash/464d828b85b0bed98e80ade0a5c43b0f-Abstract.html. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 1999 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: CORE
- Tags: Robotics, Reinforcement Learning, Policy Gradient, actor-critic
- Official paper: https://proceedings.neurips.cc/paper/1999/hash/464d828b85b0bed98e80ade0a5c43b0f-Abstract.html
- Full-text retrieval: https://proceedings.neurips.cc/paper/1999/hash/464d828b85b0bed98e80ade0a5c43b0f-Abstract.html
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 rl 문제를 이해하기 위해 읽는다. 본문은 The value-function approach has worked well in many applications, but has several limitations.를 문제로 두고, Konda and Tsitsiklis (in prep.) independently developed a very simialr result to ours.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Function approximation is essential to reinforcement learning, but the standard approach of approximating a value function and determining a policy from it has so far ...
- **p. 1 / Abstract - extractive body cue:** In this paper we explore an alternative approach in which the policy is explicitly represented by its own function approximator, independent of the value function, ...
- **p. 1 / Abstract - extractive body cue:** Williams's REINFORCE method and actor-critic methods are examples of this approach.
- **p. 1 / Abstract - extractive body cue:** Our main new result is to show that the gradient can be written in a form suitable for estimation from experience aided by an approximate ...
- **p. 1 / Abstract - extractive body cue:** Using this result, we prove for the first time that a version of policy iteration with arbitrary differentiable function approximation is convergent to a locally ...
- **p. 1 / Abstract - extractive body cue:** The value-function approach has worked well in many applications, but has several limitations.
- **p. 2 / Abstract - extractive body cue:** Our result strengthens theirs and generalizes it to arbitrary differentiable function approximators.

## Core Idea

- **p. 2 / Abstract - extractive body cue:** Konda and Tsitsiklis (in prep.) independently developed a very simialr result to ours.
- **p. 2 / Abstract - extractive body cue:** For example, the policy might be represented by a neural network whose input is a representation of the state, whose output is action selection probabilities, ...
- **p. 1 / Abstract - extractive body cue:** First, it is oriented toward finding deterministic policies, whereas the optimal policy is often stochastic, selecting different actions with specific probabilities (e.g., see Singh, Jaakkola, ...
- **p. 1 / Abstract - extractive body cue:** The dominant approach for the last decade has been the value-function approach, in which all function approximation effort goes into estimating a value function, with ...
- **p. 2 / Abstract - extractive body cue:** Our result also suggests a way of proving the convergence of a wide variety of algorithms based on "actor-critic" or policy-iteration architectures (e.g., Barto, Sutton, ...
- **p. 3 / Abstract - extractive body cue:** This leads to Williams's episodic REINFORCE algorithm, t::..Ot oc a1r~~,at2 Rt (1 ) (the ~a 7r St,at 7r\St,Ut) corrects for the oversampling of actions preferred ...
- **p. 3 / Abstract - extractive body cue:** In the average reward formulation, the value of a state-action pair given a policy is defined as 00 Q1r(s,a) = LE {rt - p(1I") I ...
- **p. 4 / Abstract - extractive body cue:** If fw satisfies (3) and is compatible with the policy parameterization in the sense thatl 8fw(s, a) 81r(s, a) 1 = 8w 80 1r(s, a) ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | For example, the policy might be represented by a neural network whose input is a representation of the state, whose output is action selection probabilities, and whose weights are the policy parameters. | state 또는 observation, action, reward와 transition history | p. 2 (Abstract), p. 1 (Abstract) |
| State/latent | example, policy, might, represented, neural, network, whose, input, representation, state, output, action | policy/value state와 action-selection variable | p. 2 (Abstract), p. 1 (Abstract), p. 3 (Abstract) |
| Output/action | The dominant approach for the last decade has been the value-function approach, in which all function approximation effort goes into estimating a value function, with the action-selection policy represented implicitly as the ... | action policy와 induced trajectory | p. 1 (Abstract), p. 3 (Abstract), p. 1 (Abstract) |
| Objective/outcome | In this paper we explore an alternative approach in which the policy is explicitly represented by its own function approximator, independent of the value function, and is updated according to the gradient ... | expected return, task success, stability와 sample efficiency | p. 1 (Abstract), p. 3 (Abstract), p. 2 (Abstract) |

## Main Claims and Actual Contribution

- **p. 2 / Abstract - extractive body cue:** Konda and Tsitsiklis (in prep.) independently developed a very simialr result to ours.
- **p. 2 / Abstract - extractive body cue:** If the above can be achieved, then 0 can usually be assured to converge to a locally optimal policy in the performance measure p.
- **p. 4 / Abstract - extractive body cue:** For example, Jaakkola, Singh, and Jordan (1995) proved that for the special case of function approximation arising in a tabular POMDP one could assure positive ...
- **p. 2 / Abstract - extractive body cue:** However, VAPS methods do not climb the gradient of performance (expected long-term reward), but of a measure combining performance and valuefunction accuracy.
- **p. 3 / Abstract - extractive body cue:** We extend their results to the start-state formulation and provide simpler and more direct proofs.
- **p. 3 / Abstract - extractive body cue:** Our first result concerns the gradient of the performance metric with respect to the policy parameter: Theorem 1 (Policy Gradient).
- **p. 5 / Abstract - extractive body cue:** Our results establish that that approximation process can proceed without affecting the expected evolution of fw and 1r.
- **p. 5 / Abstract - extractive body cue:** Our results can be viewed as a justification for the special status of advantages as the target for value function approximation in RL.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

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

RL, IL, offline learning, and robot data의 rl 문제를 이해하기 위해 읽는다. 본문은 The value-function approach has worked well in many applications, but has several limitations.를 문제로 두고, Konda and Tsitsiklis (in prep.) independently developed a very simialr result to ours.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (Abstract), p. 1 (Abstract), p. 2 (Abstract), p. 2 (Abstract), p. 1 (Abstract), p. 1 (Abstract) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (7 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** The value-function approach has worked well in many applications, but has several limitations. (p. 1, Abstract).
- **Actual contribution:** Williams's REINFORCE method and actor-critic methods are examples of this approach. (p. 1, Abstract).
- **Evaluation boundary:** However, VAPS methods do not climb the gradient of performance (expected long-term reward), but of a measure combining performance and valuefunction accuracy. (p. 2, Abstract).
- **Explicit failure boundary:** The value-function approach has worked well in many applications, but has several limitations. (p. 1, Abstract).
