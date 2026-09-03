# Insights — Policy Gradient Methods for Reinforcement Learning with Function Approximation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.neurips.cc/paper/1999/hash/464d828b85b0bed98e80ade0a5c43b0f-Abstract.html; PDF retrieval source: https://proceedings.neurips.cc/paper/1999/hash/464d828b85b0bed98e80ade0a5c43b0f-Abstract.html. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / Abstract - extractive body cue:** Konda and Tsitsiklis (in prep.) independently developed a very simialr result to ours.
- **p. 2 / Abstract - extractive body cue:** For example, the policy might be represented by a neural network whose input is a representation of the state, whose output is action selection probabilities, ...
- **p. 1 / Abstract - extractive body cue:** First, it is oriented toward finding deterministic policies, whereas the optimal policy is often stochastic, selecting different actions with specific probabilities (e.g., see Singh, Jaakkola, ...
- **p. 1 / Abstract - extractive body cue:** The dominant approach for the last decade has been the value-function approach, in which all function approximation effort goes into estimating a value function, with ...
- **p. 2 / Abstract - extractive body cue:** Our result also suggests a way of proving the convergence of a wide variety of algorithms based on "actor-critic" or policy-iteration architectures (e.g., Barto, Sutton, ...
- **p. 3 / Abstract - extractive body cue:** This leads to Williams's episodic REINFORCE algorithm, t::..Ot oc a1r~~,at2 Rt (1 ) (the ~a 7r St,at 7r\St,Ut) corrects for the oversampling of actions preferred ...
- **p. 3 / Abstract - extractive body cue:** In the average reward formulation, the value of a state-action pair given a policy is defined as 00 Q1r(s,a) = LE {rt - p(1I") I ...
- **Contribution anchor:** p. 2 (Abstract), p. 2 (Abstract), p. 1 (Abstract), p. 1 (Abstract), p. 2 (Abstract), p. 3 (Abstract)

### Strongest assumption and failure boundary

- **p. 1 / Abstract - extractive body cue:** The value-function approach has worked well in many applications, but has several limitations.
- **p. 1 / Abstract - extractive body cue:** Function approximation is essential to reinforcement learning, but the standard approach of approximating a value function and determining a policy from it has so far ...
- **p. 2 / Abstract - extractive body cue:** Our result strengthens theirs and generalizes it to arbitrary differentiable function approximators.
- **p. 2 / Abstract - extractive body cue:** Similarly, Gordon's (1995) fitted value iteration is also convergent and value-based, but does not find a locally optimal policy.
- **p. 2 / Abstract - extractive body cue:** As a result, VAPS does not converge to a locally optimal policy, except in the case that no weight is put upon value-function accuracy, in ...
- **p. 3 / Abstract - extractive body cue:** In any event, the key aspect of both expressions for the gradient is that their are no terms of the form adiJII): the effect of ...
- **p. 5 / Abstract - extractive body cue:** (This follows immediately because l:a 87r~~a) = 0, Vs E S.) The choice of v does not affect any of our theorems, but can substantially ...
- **Boundary to test:** Similarly, Gordon's (1995) fitted value iteration is also convergent and value-based, but does not find a locally optimal policy.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Konda and Tsitsiklis (in prep.) independently developed a very simialr result to ours. | p. 2 (Abstract), p. 2 (Abstract) |
| Reported outcome | If the above can be achieved, then 0 can usually be assured to converge to a locally optimal policy in the performance measure p. | p. 2 (Abstract), p. 4 (Abstract) |
| Failure/limitation | Similarly, Gordon's (1995) fitted value iteration is also convergent and value-based, but does not find a locally optimal policy. | p. 2 (Abstract), p. 2 (Abstract) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** For example, the policy might be represented by a neural network whose input is a representation of the state, whose output is action selection probabilities, and whose weights are the ... (p. 2, Abstract).
- **Paper-specific mechanism:** Williams's REINFORCE method and actor-critic methods are examples of this approach. (p. 1, Abstract).
- **Evidence boundary:** the reported outcome is However, VAPS methods do not climb the gradient of performance (expected long-term reward), but of a measure combining performance and valuefunction accuracy. (p. 2, Abstract); the relevant task/metric cue is However, VAPS methods do not climb the gradient of performance (expected long-term reward), but of a measure combining performance and valuefunction accuracy. (p. 2, Abstract). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** The value-function approach has worked well in many applications, but has several limitations. (p. 1, Abstract).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `CORE` in `RL, IL, offline learning, and robot data`; tags: `Robotics, Reinforcement Learning, Policy Gradient, actor-critic`.
- **Reading predecessor in the generated track queue:** Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** PILCO: A Model-Based and Data-Efficient Approach to Policy Search (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Similarly, Gordon's (1995) fitted value iteration is also convergent and value-based, but does not find a locally optimal policy.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: For example, the policy might be represented by a neural network whose input is a representation of the state, whose output is action selection probabilities, and whose weights are the ... (p. 2, Abstract); preserve the objective/update rule: In this paper we explore an alternative approach in which the policy is explicitly represented by its own function approximator, independent of the value function, and is updated according to ... (p. 1, Abstract).
2. Use the paper-reported task/data/environment cue: The environment's dynamics are characterized by state transition probabilities, P:SI = Pr { St+ 1 = Sf I St = s, at = a}, and expected rewards 'R~ = E ... (p. 2, Abstract).
3. Compare against the reported or matched baseline: Williams's (1988, 1992) REINFORCE algorithm also finds an unbiased estimate of the gradient, but without the assistance of a learned value function. (p. 2, Abstract).
4. Report the body metric with its denominator and aggregation: However, VAPS methods do not climb the gradient of performance (expected long-term reward), but of a measure combining performance and valuefunction accuracy. (p. 2, Abstract).
5. Re-run the reported ablation or stress/failure condition: Williams's (1988, 1992) REINFORCE algorithm also finds an unbiased estimate of the gradient, but without the assistance of a learned value function. (p. 2, Abstract); if none is reported, design one around: The value-function approach has worked well in many applications, but has several limitations. (p. 1, Abstract).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (Abstract), p. 1 (Abstract), match the reported outcome at p. 2 (Abstract), p. 3 (Abstract), p. 3 (Abstract), and measure the boundary at p. 1 (Abstract), p. 1 (Abstract).

## Falsifiable research question

Under the paper's stated interface (For example, the policy might be represented by a neural network whose input is a representation of the state, whose output is ...), does the paper-specific mechanism (Williams's REINFORCE method and actor-critic methods are examples of this approach.) retain the reported evaluation outcome (However, VAPS methods do not climb the gradient of performance (expected long-term reward), but of a measure combining ...) when tested against the paper's strongest explicit boundary (The value-function approach has worked well in many applications, but has several limitations.)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (However, VAPS methods do not climb the gradient of performance (expected long-term reward), but of a measure combining ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (7 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Williams's REINFORCE method and actor-critic methods are examples of this approach. (p. 1, Abstract).
- **Paper-supported outcome:** However, VAPS methods do not climb the gradient of performance (expected long-term reward), but of a measure combining performance and valuefunction accuracy. (p. 2, Abstract).
- **Strongest explicit boundary:** The value-function approach has worked well in many applications, but has several limitations. (p. 1, Abstract).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
