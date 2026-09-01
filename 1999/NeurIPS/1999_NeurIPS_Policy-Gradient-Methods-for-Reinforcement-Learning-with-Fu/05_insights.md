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

- **Closed-loop position:** `state 또는 observation, action, reward와 transition history → policy/value state와 action-selection variable → action policy와 induced trajectory`.
- 이 논문의 재사용 가능한 지점은 For example, the policy might be represented by a neural network whose input is a representation of the state, whose output is action selection probabilities, and whose weights are the policy parameters.를 The dominant approach for the last decade has been the value-function approach, in which all function approximation effort goes into estimating a value function, with the action-selection policy represented implicitly as the ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 policy/value state와 action-selection variable가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Similarly, Gordon's (1995) fitted value iteration is also convergent and value-based, but does not find a locally optimal policy.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Konda and Tsitsiklis (in prep.) independently developed a very simialr result to ours.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `CORE` in `RL, IL, offline learning, and robot data`; tags: `Robotics, Reinforcement Learning, Policy Gradient, actor-critic`.
- **Reading predecessor in the generated track queue:** Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** PILCO: A Model-Based and Data-Efficient Approach to Policy Search (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Similarly, Gordon's (1995) fitted value iteration is also convergent and value-based, but does not find a locally optimal policy.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: The environment's dynamics are characterized by state transition probabilities, P:SI = Pr { St+ 1 = Sf I St = s, at = a}, and expected rewards 'R~ = E {rt+l 1st ....
3. Compare against the body-reported baseline or a matched simpler baseline: The issues here are entirely analogous to those in the use of reinforcement baselines in earlier work (e.g., Williams, 1992; Dayan, 1991; Sutton, 1984)..
4. Report the body metric and its denominator/aggregation: However, VAPS methods do not climb the gradient of performance (expected long-term reward), but of a measure combining performance and valuefunction accuracy..
5. Re-run the body-reported ablation/failure condition: In any event, the key aspect of both expressions for the gradient is that their are no terms of the form adiJII): the effect of policy changes on the distribution of states ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 2 (Abstract), p. 1 (Abstract), p. 1 (Abstract); the primary result is directionally consistent at p. 2 (Abstract), p. 4 (Abstract), p. 2 (Abstract); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Konda, Tsitsiklis, prep mechanism이 The issues here are entirely analogous to those in the use of reinforcement baselines in earlier ... 대비 However, VAPS methods do not climb the gradient of performance (expected long-term reward), but of a measure combining ...을 개선하고, Similarly, Gordon's (1995) fitted value iteration is also convergent and value-based, but does not find a ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
