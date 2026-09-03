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

- **Paper-specific interface:** Trust Region Policy Optimization This problem imposes a constraint that the KL divergence is bounded at every point in the state space. (p. 4, 2 Preliminaries).
- **Paper-specific mechanism:** In our experiments, we show that the same TRPO methods can learn complex policies for swimming, hopping, and walking, as well as playing Atari games directly from raw images. (p. 1, 1 Introduction).
- **Evidence boundary:** the reported outcome is Table 1. Performance comparison for vision-based RL algorithms on the Atari domain. Our algorithms (bottom rows) were run once on each task, with the same architecture and parameters. Performance varies ... (p. 8, Figure/Table caption); the relevant task/metric cue is Table 1. Performance comparison for vision-based RL algorithms on the Atari domain. Our algorithms (bottom rows) were run once on each task, with the same architecture and parameters. Performance varies ... (p. 8, Figure/Table caption). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** Our analysis also provides a perspective that unifies policy gradient and policy iteration methods, and shows them to be special limiting cases of an algorithm that optimizes a certain objective ... (p. 8, 9 Discussion).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `CORE` in `RL, IL, offline learning, and robot data`; tags: `Robotics, Reinforcement Learning, policy optimization, on-policy RL`.
- **Reading predecessor in the generated track queue:** Generative Adversarial Imitation Learning (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Proximal Policy Optimization Algorithms (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** The analytic estimator integrates over the action at each state sn, and does not depend on the action an that was sampled.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Trust Region Policy Optimization This problem imposes a constraint that the KL divergence is bounded at every point in the state space. (p. 4, 2 Preliminaries); preserve the objective/update rule: The natural policy gradient (Kakade, 2002) can be obtained as a special case of the update in Equation (12) by using a linear approximation to L and a quadratic approximation ... (p. 6, 3. Approximately solve this constrained optimization).
2. Use the paper-reported task/data/environment cue: 2D robot models used for locomotion experiments. (p. 6, 1. What are the performance characteristics of the single).
3. Compare against the reported or matched baseline: This self-normalized estimator removes the need to use a baseline for the Q-values (note that the gradient is unchanged by adding a constant to the Q-values). (p. 5, 2 Preliminaries).
4. Report the body metric with its denominator and aggregation: Table 1. Performance comparison for vision-based RL algorithms on the Atari domain. Our algorithms (bottom rows) were run once on each task, with the same architecture and parameters. Performance varies ... (p. 8, Figure/Table caption).
5. Re-run the reported ablation or stress/failure condition: This self-normalized estimator removes the need to use a baseline for the Q-values (note that the gradient is unchanged by adding a constant to the Q-values). (p. 5, 2 Preliminaries); if none is reported, design one around: Our analysis also provides a perspective that unifies policy gradient and policy iteration methods, and shows them to be special limiting cases of an algorithm that optimizes a certain objective ... (p. 8, 9 Discussion).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (1 Introduction), p. 1 (Abstract), match the reported outcome at p. 8 (Figure/Table caption), p. 7 (3. Can TRPO be used to solve challenging large-scale), p. 6 (3. Approximately solve this constrained optimization), and measure the boundary at p. 8 (9 Discussion), p. 2 (2 Preliminaries).

## Falsifiable research question

Under the paper's stated interface (Trust Region Policy Optimization This problem imposes a constraint that the KL divergence is bounded at every point in the state space.), does the paper-specific mechanism (In our experiments, we show that the same TRPO methods can learn complex policies for swimming, hopping, and walking, as well as ...) retain the reported evaluation outcome (Table 1. Performance comparison for vision-based RL algorithms on the Atari domain. Our algorithms (bottom rows) were run ...) when tested against the paper's strongest explicit boundary (Our analysis also provides a perspective that unifies policy gradient and policy iteration methods, and shows them to ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Table 1. Performance comparison for vision-based RL algorithms on the Atari domain. Our algorithms (bottom rows) were run ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (16 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** In our experiments, we show that the same TRPO methods can learn complex policies for swimming, hopping, and walking, as well as playing Atari games directly from raw images. (p. 1, 1 Introduction).
- **Paper-supported outcome:** Table 1. Performance comparison for vision-based RL algorithms on the Atari domain. Our algorithms (bottom rows) were run once on each task, with the same architecture and parameters. Performance varies ... (p. 8, Figure/Table caption).
- **Strongest explicit boundary:** Our analysis also provides a perspective that unifies policy gradient and policy iteration methods, and shows them to be special limiting cases of an algorithm that optimizes a certain objective ... (p. 8, 9 Discussion).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
