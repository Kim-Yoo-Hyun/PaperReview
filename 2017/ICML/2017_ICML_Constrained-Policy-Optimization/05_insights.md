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

- **Closed-loop position:** `observation, uncertainty/risk estimate와 task command → safe set, recovery state 또는 constraint margin → shielded, recovery 또는 safe action`.
- 이 논문의 재사용 가능한 지점은 Constrained Policy Optimization Algorithm 1 Constrained Policy Optimization Input: Initial policy π0 ∈Πθ tolerance α for k = 0, 1, 2, ... do Sample a set of trajectories D = {τ} ∼πk ...를 Recently, deep reinforcement learning has enabled neural network policies to achieve state-of-the-art performance on many high-dimensional control tasks, including Atari games (using pixels as inputs) (Mnih et al., 2015; 2016), robot lo ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 safe set, recovery state 또는 constraint margin가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Sometimes (11) will still be feasible and CPO can automatically recover from its bad step, but for the infeasible case, a recovery method is necessary.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In this work, we propose the first such algorithm, allowing applications to constrained deep RL.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `RL, IL, offline learning, and robot data`; tags: `Robotics, safe reinforcement learning, constraints, policy optimization`.
- **Reading predecessor in the generated track queue:** Hindsight Experience Replay (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Conservative Q-Learning for Offline Reinforcement Learning (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Sometimes (11) will still be feasible and CPO can automatically recover from its bad step, but for the infeasible case, a recovery method is necessary.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We consider two tasks, and train multiple different agents (robots) for each task: • Circle: The agent is rewarded for running in a wide circle, but is constrained to stay within a ....
3. Compare against the body-reported baseline or a matched simpler baseline: We find that CPO generally outperforms PDO on enforcing constraints, without compromising performance with respect to return..
4. Report the body metric and its denominator/aggregation: Figure 1. Average performance for CPO, PDO, and TRPO over several seeds (5 in the Point environments, 10 in all others); the x-axis is training iteration. CPO drives the constraint function almost ....
5. Re-run the body-reported ablation/failure condition: However, CPO is nearly constraint-satisfying even without cost shaping..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 6 (6.1. Approximately Solving the CPO Update), p. 4 (5.2. Trust Region Methods), p. 3 (5. Constrained Policy Optimization); the primary result is directionally consistent at p. 8 (8.1. Evaluating CPO and Comparison Analysis), p. 8 (8.1. Evaluating CPO and Comparison Analysis), p. 7 (8.1. Evaluating CPO and Comparison Analysis); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 first, algorithm, allowing mechanism이 We find that CPO generally outperforms PDO on enforcing constraints, without compromising performance with respect to ... 대비 Figure 1. Average performance for CPO, PDO, and TRPO over several seeds (5 in the Point environments, 10 ...을 개선하고, Sometimes (11) will still be feasible and CPO can automatically recover from its bad step, but ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
