# Insights — Constrained Policy Optimization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v70/achiam17a.html; PDF retrieval source: https://arxiv.org/pdf/1705.10528. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / 1. Introduction - extractive body cue:** In this work, we propose the first such algorithm, allowing applications to constrained deep RL.
- **p. 5 / 5.3. Trust Region Optimization for Constrained MDPs - extractive body cue:** Then, because the theoretically guaranteed update will take toosmall steps in practice, we propose CPO as a practical approximation based on trust region methods.
- **p. 5 / 5.3. Trust Region Optimization for Constrained MDPs - extractive body cue:** Inspired by trust region methods, we propose CPO, which uses a trust region instead of penalties on policy divergence to enable larger step sizes: πk+1 ...
- **p. 1 / 1. Introduction - extractive body cue:** Driving our approach is a new theoretical result that bounds the difference between the rewards or costs of two different policies.
- **p. 2 / 1. Introduction - extractive body cue:** In our experiments, we show that CPO can train neural network policies with thousands of parameters on highdimensional simulated robot locomotion tasks to maximize rewards ...
- **p. 6 / 6.1. Approximately Solving the CPO Update - extractive body cue:** Constrained Policy Optimization Algorithm 1 Constrained Policy Optimization Input: Initial policy π0 ∈Πθ tolerance α for k = 0, 1, 2, ... do Sample a ...
- **p. 4 / 5.2. Trust Region Methods - extractive body cue:** Trust region algorithms for reinforcement learning (Schulman et al., 2015; 2016) have policy updates of the form πk+1 = arg max π∈Πθ E s∼dπk a∼π ...
- **Contribution anchor:** p. 1 (1. Introduction), p. 5 (5.3. Trust Region Optimization for Constrained MDPs), p. 5 (5.3. Trust Region Optimization for Constrained MDPs), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 6 (6.1. Approximately Solving the CPO Update)

### Strongest assumption and failure boundary

- **p. 1 / 1. Introduction - extractive body cue:** Although optimal policies for finite CMDPs with known models can be obtained by linear programming, methods for high-dimensional control are lacking.
- **p. 1 / 1. Introduction - extractive body cue:** Currently, policy search algorithms enjoy state-of-theart performance on high-dimensional control tasks (Mnih et al., 2016; Duan et al., 2016).
- **p. 6 / 6.2. Feasibility - extractive body cue:** Sometimes (11) will still be feasible and CPO can automatically recover from its bad step, but for the infeasible case, a recovery method is necessary.
- **p. 6 / 6.3. Tightening Constraints via Cost Shaping - extractive body cue:** We choose ∆to be the probability of entering an unsafe state within a fixed time horizon, according to a learned model that is updated at ...
- **Boundary to test:** Sometimes (11) will still be feasible and CPO can automatically recover from its bad step, but for the infeasible case, a recovery method is necessary.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In this work, we propose the first such algorithm, allowing applications to constrained deep RL. | p. 1 (1. Introduction), p. 5 (5.3. Trust Region Optimization for Constrained MDPs) |
| Reported outcome | We find that CPO generally outperforms PDO on enforcing constraints, without compromising performance with respect to return. | p. 8 (8.1. Evaluating CPO and Comparison Analysis), p. 8 (8.1. Evaluating CPO and Comparison Analysis) |
| Failure/limitation | Sometimes (11) will still be feasible and CPO can automatically recover from its bad step, but for the infeasible case, a recovery method is necessary. | p. 6 (6.2. Feasibility), p. 6 (6.3. Tightening Constraints via Cost Shaping) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** Recently, deep reinforcement learning has enabled neural network policies to achieve state-of-the-art performance on many high-dimensional control tasks, including Atari games (using pixels as inputs) (Mnih et al., 2015; 2016), ... (p. 1, 1. Introduction).
- **Paper-specific mechanism:** In this work, we propose the first such algorithm, allowing applications to constrained deep RL. (p. 1, 1. Introduction).
- **Evidence boundary:** the reported outcome is In our experiments, we aim to answer the following: • Does CPO succeed at enforcing behavioral constraints when training neural network policies with thousands of parameters? • How does CPO ... (p. 6, 8. Experiments); the relevant task/metric cue is We find that CPO generally outperforms PDO on enforcing constraints, without compromising performance with respect to return. (p. 8, 8.1. Evaluating CPO and Comparison Analysis). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** Additionally, PDO is sensitive to the initialization of the dual variable. (p. 7, 8.1. Evaluating CPO and Comparison Analysis).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `RL, IL, offline learning, and robot data`; tags: `Robotics, safe reinforcement learning, constraints, policy optimization`.
- **Reading predecessor in the generated track queue:** Hindsight Experience Replay (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Conservative Q-Learning for Offline Reinforcement Learning (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Sometimes (11) will still be feasible and CPO can automatically recover from its bad step, but for the infeasible case, a recovery method is necessary.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Recently, deep reinforcement learning has enabled neural network policies to achieve state-of-the-art performance on many high-dimensional control tasks, including Atari games (using pixels as inputs) (Mnih et al., 2015; 2016), ... (p. 1, 1. Introduction); preserve the objective/update rule: When the objective is estimated by linearizing around πk as J(πk) + gT (θ -θk), g is the policy gradient, and the standard policy gradient update is obtained by choosing ... (p. 3, 5. Constrained Policy Optimization).
2. Use the paper-reported task/data/environment cue: We consider two tasks, and train multiple different agents (robots) for each task: • Circle: The agent is rewarded for running in a wide circle, but is constrained to stay ... (p. 6, 8. Experiments).
3. Compare against the reported or matched baseline: We find that CPO generally outperforms PDO on enforcing constraints, without compromising performance with respect to return. (p. 8, 8.1. Evaluating CPO and Comparison Analysis).
4. Report the body metric with its denominator and aggregation: We find that CPO generally outperforms PDO on enforcing constraints, without compromising performance with respect to return. (p. 8, 8.1. Evaluating CPO and Comparison Analysis).
5. Re-run the reported ablation or stress/failure condition: However, CPO is nearly constraint-satisfying even without cost shaping. (p. 8, 8.2. Ablation on Cost Shaping); if none is reported, design one around: Additionally, PDO is sensitive to the initialization of the dual variable. (p. 7, 8.1. Evaluating CPO and Comparison Analysis).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (1. Introduction), p. 1 (1. Introduction), match the reported outcome at p. 6 (8. Experiments), p. 7 (8. Experiments), p. 8 (8.1. Evaluating CPO and Comparison Analysis), and measure the boundary at p. 7 (8.1. Evaluating CPO and Comparison Analysis), p. 7 (8.1. Evaluating CPO and Comparison Analysis).

## Falsifiable research question

Under the paper's stated interface (Recently, deep reinforcement learning has enabled neural network policies to achieve state-of-the-art performance on many high-dimensional control tasks, including Atari games (using ...), does the paper-specific mechanism (In this work, we propose the first such algorithm, allowing applications to constrained deep RL.) retain the reported evaluation outcome (We find that CPO generally outperforms PDO on enforcing constraints, without compromising performance with respect to return.) when tested against the paper's strongest explicit boundary (Additionally, PDO is sensitive to the initialization of the dual variable.)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (We find that CPO generally outperforms PDO on enforcing constraints, without compromising performance with respect to return.) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** In this work, we propose the first such algorithm, allowing applications to constrained deep RL. (p. 1, 1. Introduction).
- **Paper-supported outcome:** In our experiments, we aim to answer the following: • Does CPO succeed at enforcing behavioral constraints when training neural network policies with thousands of parameters? • How does CPO ... (p. 6, 8. Experiments).
- **Strongest explicit boundary:** Additionally, PDO is sensitive to the initialization of the dual variable. (p. 7, 8.1. Evaluating CPO and Comparison Analysis).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
