# Insights — Trust Region Policy Optimization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v37/schulman15.html; PDF retrieval source: https://arxiv.org/pdf/1502.05477. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 2 Preliminaries - extractive body cue:** Instead, we introduce the following local approximation to η: Lπ(˜π) = η(π) + X s ρπ(s) X a ˜π(a/s)Aπ(s, a).
- **p. 3 / 2 Preliminaries - extractive body cue:** Trust region policy optimization, which we propose in the following section, is an approximation to Algorithm 1, which uses a constraint on the KL divergence ...
- **p. 5 / 2 Preliminaries - extractive body cue:** 6 Practical Algorithm Here we present two practical policy optimization algorithm based on the ideas above, which use either the single path or vine sampling ...
- **p. 1 / 1 Introduction - extractive body cue:** In our experiments, we show that the same TRPO methods can learn complex policies for swimming, hopping, and walking, as well as playing Atari games ...
- **p. 4 / 2 Preliminaries - extractive body cue:** Using q to denote the sampling distribution, the contribution of a single sn to the loss function is X a πθ(a/sn)Aθold(sn, a) = Ea∼q πθ(a/sn) ...
- **p. 5 / 3. Approximately solve this constrained optimization - extractive body cue:** We use the conjugate gradient algorithm followed by a line search, which is altogether only slightly more expensive than computing the gradient itself.
- **p. 5 / 3. Approximately solve this constrained optimization - extractive body cue:** Empirically, it is hard to robustly choose the penalty coefficient, so we use a hard constraint instead of a penalty, with parameter δ (the bound ...
- **Contribution anchor:** p. 2 (2 Preliminaries), p. 3 (2 Preliminaries), p. 5 (2 Preliminaries), p. 1 (1 Introduction), p. 4 (2 Preliminaries), p. 5 (3. Approximately solve this constrained optimization)

### Strongest assumption and failure boundary

- **p. 1 / 1 Introduction - extractive body cue:** Tetris is a classic benchmark problem for approximate dynamic programming (ADP) methods, stochastic optimization methods are difficult to beat on this task (Gabillon et al., ...
- **p. 1 / 1 Introduction - extractive body cue:** Most algorithms for policy optimization can be classified into three broad categories: (1) policy iteration methods, which alternate between estimating the value function under the ...
- **p. 2 / 2 Preliminaries - extractive body cue:** The complex dependency of ρ˜π(s) on ˜π makes Equation (2) difficult to optimize directly.
- **p. 2 / 2 Preliminaries - extractive body cue:** To define the conservative policy iteration update, let πold denote the current policy, and let π′ = arg maxπ′ Lπold(π′).
- **p. 3 / 2 Preliminaries - extractive body cue:** Since mixture policies are rarely used in practice, this result is crucial for extending the improvement guarantee to practical problems.
- **p. 5 / 3. Approximately solve this constrained optimization - extractive body cue:** The analytic estimator integrates over the action at each state sn, and does not depend on the action an that was sampled.
- **p. 6 / 3. Approximately solve this constrained optimization - extractive body cue:** Unlike REPS, our approach does not require a costly nonlinear optimization in the inner loop.
- **Boundary to test:** The analytic estimator integrates over the action at each state sn, and does not depend on the action an that was sampled.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Instead, we introduce the following local approximation to η: Lπ(˜π) = η(π) + X s ρπ(s) X a ˜π(a/s)Aπ(s, a). | p. 2 (2 Preliminaries), p. 3 (2 Preliminaries) |
| Reported outcome | Though this difference might seem subtle, our experiments demonstrate that it significantly improves the algorithm's performance on larger problems. | p. 6 (3. Approximately solve this constrained optimization), p. 5 (3. Approximately solve this constrained optimization) |
| Failure/limitation | The analytic estimator integrates over the action at each state sn, and does not depend on the action an that was sampled. | p. 5 (3. Approximately solve this constrained optimization), p. 6 (3. Approximately solve this constrained optimization) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `state 또는 observation, action, reward와 transition history → policy/value state와 action-selection variable → action policy와 induced trajectory`.
- 이 논문의 재사용 가능한 지점은 This implies the classic result that the update performed by exact policy iteration, which uses the deterministic policy ˜π(s) = arg maxa Aπ(s, a), improves the policy if there is at least ...를 Here, we generate a set of trajectories via simulation of the policy and incorporate all state-action pairs (sn, an) into the objective.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 policy/value state와 action-selection variable가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 The analytic estimator integrates over the action at each state sn, and does not depend on the action an that was sampled.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Instead, we introduce the following local approximation to η: Lπ(˜π) = η(π) + X s ρπ(s) X a ˜π(a/s)Aπ(s, a).
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `CORE` in `RL, IL, offline learning, and robot data`; tags: `Robotics, Reinforcement Learning, policy optimization, on-policy RL`.
- **Reading predecessor in the generated track queue:** Generative Adversarial Imitation Learning (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Proximal Policy Optimization Algorithms (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** The analytic estimator integrates over the action at each state sn, and does not depend on the action an that was sampled.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: 8.1 Simulated Robotic Locomotion We conducted the robotic locomotion experiments using the MuJoCo simulator (Todorov et al., 2012)..
3. Compare against the body-reported baseline or a matched simpler baseline: This self-normalized estimator removes the need to use a baseline for the Q-values (note that the gradient is unchanged by adding a constant to the Q-values)..
4. Report the body metric and its denominator/aggregation: Table 1. Performance comparison for vision-based RL algorithms on the Atari domain. Our algorithms (bottom rows) were run once on each task, with the same architecture and parameters. Performance varies substantially from ....
5. Re-run the body-reported ablation/failure condition: This self-normalized estimator removes the need to use a baseline for the Q-values (note that the gradient is unchanged by adding a constant to the Q-values)..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (3. Approximately solve this constrained optimization), p. 5 (3. Approximately solve this constrained optimization), p. 6 (3. Approximately solve this constrained optimization); the primary result is directionally consistent at p. 6 (3. Approximately solve this constrained optimization), p. 5 (3. Approximately solve this constrained optimization), p. 5 (3. Approximately solve this constrained optimization); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Instead, introduce, following mechanism이 This self-normalized estimator removes the need to use a baseline for the Q-values (note that the ... 대비 Table 1. Performance comparison for vision-based RL algorithms on the Atari domain. Our algorithms (bottom rows) were run ...을 개선하고, The analytic estimator integrates over the action at each state sn, and does not depend on ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
