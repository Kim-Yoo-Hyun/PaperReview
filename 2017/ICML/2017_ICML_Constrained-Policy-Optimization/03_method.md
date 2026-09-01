# Method - Constrained Policy Optimization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v70/achiam17a.html; PDF retrieval source: https://arxiv.org/pdf/1705.10528. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 6 (6.1. Approximately Solving the CPO Update), p. 4 (5.2. Trust Region Methods), p. 3 (5. Constrained Policy Optimization), p. 5 (5.3. Trust Region Optimization for Constrained MDPs), p. 4 (5.2. Trust Region Methods), p. 5 (5.3. Trust Region Optimization for Constrained MDPs)): Constrained Policy Optimization Algorithm 1 Constrained Policy Optimization Input: Initial policy π0 ∈Πθ tolerance α for k = 0, 1, 2, ... do Sample a set of trajectories D = ...

## Method Body Digest

- **p. 6 / 6.1. Approximately Solving the CPO Update - extractive body cue:** Constrained Policy Optimization Algorithm 1 Constrained Policy Optimization Input: Initial policy π0 ∈Πθ tolerance α for k = 0, 1, 2, ... do Sample a ...
- **p. 4 / 5.2. Trust Region Methods - extractive body cue:** Trust region algorithms for reinforcement learning (Schulman et al., 2015; 2016) have policy updates of the form πk+1 = arg max π∈Πθ E s∼dπk a∼π ...
- **p. 3 / 5. Constrained Policy Optimization - extractive body cue:** Policy search algorithms approach this problem by searching for the optimal policy within a set Πθ ⊆Π of parametrized policies with parameters θ (for example, ...
- **p. 5 / 5.3. Trust Region Optimization for Constrained MDPs - extractive body cue:** First, we describe a policy search update for CMDPs that alleviates the issue of off-policy evaluation, and comes with guarantees of monotonic performance improvement and ...
- **p. 4 / 5.2. Trust Region Methods - extractive body cue:** Despite the approximation, trust region steps usually give monotonic improvements (Schulman et al., 2015; Duan et al., 2016) and have shown state-of-the-art performance in the ...
- **p. 5 / 5.3. Trust Region Optimization for Constrained MDPs - extractive body cue:** Inspired by trust region methods, we propose CPO, which uses a trust region instead of penalties on policy divergence to enable larger step sizes: πk+1 ...
- **p. 3 / 5. Constrained Policy Optimization - extractive body cue:** We conclude by motivating, presenting, and proving gurantees on our algorithm, Constrained Policy Optimization (CPO), a trust region method for CMDPs.
- **p. 5 / 6.1. Approximately Solving the CPO Update - extractive body cue:** However, for small step sizes δ, the objective and cost constraints are well-approximated by linearizing around πk, and the KLdivergence constraint is well-approximated by second ...

## Design Rationale

- **p. 1 / 1. Introduction - extractive body cue:** In this work, we propose the first such algorithm, allowing applications to constrained deep RL.
- **p. 5 / 5.3. Trust Region Optimization for Constrained MDPs - extractive body cue:** Then, because the theoretically guaranteed update will take toosmall steps in practice, we propose CPO as a practical approximation based on trust region methods.
- **p. 5 / 5.3. Trust Region Optimization for Constrained MDPs - extractive body cue:** Inspired by trust region methods, we propose CPO, which uses a trust region instead of penalties on policy divergence to enable larger step sizes: πk+1 ...

## Source Evidence Cues

- **p. 6 / 6.1. Approximately Solving the CPO Update - extractive body cue:** Constrained Policy Optimization Algorithm 1 Constrained Policy Optimization Input: Initial policy π0 ∈Πθ tolerance α for k = 0, 1, 2, ... do Sample a ...
- **p. 4 / 5.2. Trust Region Methods - extractive body cue:** Trust region algorithms for reinforcement learning (Schulman et al., 2015; 2016) have policy updates of the form πk+1 = arg max π∈Πθ E s∼dπk a∼π ...
- **p. 3 / 5. Constrained Policy Optimization - extractive body cue:** Policy search algorithms approach this problem by searching for the optimal policy within a set Πθ ⊆Π of parametrized policies with parameters θ (for example, ...
- **p. 5 / 5.3. Trust Region Optimization for Constrained MDPs - extractive body cue:** First, we describe a policy search update for CMDPs that alleviates the issue of off-policy evaluation, and comes with guarantees of monotonic performance improvement and ...
- **p. 4 / 5.2. Trust Region Methods - extractive body cue:** Despite the approximation, trust region steps usually give monotonic improvements (Schulman et al., 2015; Duan et al., 2016) and have shown state-of-the-art performance in the ...
- **p. 5 / 5.3. Trust Region Optimization for Constrained MDPs - extractive body cue:** Inspired by trust region methods, we propose CPO, which uses a trust region instead of penalties on policy divergence to enable larger step sizes: πk+1 ...
- **p. 3 / 5. Constrained Policy Optimization - extractive body cue:** We conclude by motivating, presenting, and proving gurantees on our algorithm, Constrained Policy Optimization (CPO), a trust region method for CMDPs.
- **Detected method headings:** 5. Constrained Policy Optimization (p. 3); 5.1. Policy Performance Bounds (p. 3); 5.2. Trust Region Methods (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Risk / failure representation | unsafe state와 uncertainty를 계산한다 | observation, nominal command, history | barrier, risk model, failure classifier, uncertainty 또는 safe set을 추정 | risk/margin/failure state | Constrained Policy Optimization Algorithm 1 Constrained Policy Optimization Input: Initial policy π0 ∈Πθ tolerance α for k = 0, 1, 2, ... ... | p. 6 (6.1. Approximately Solving the CPO Update), p. 4 (5.2. Trust Region Methods) |
| Filtering / recovery | nominal command를 안전 command로 바꾼다 | nominal action과 safety constraint | QP shield, backup policy, correction, stop 또는 recovery plan을 선택 | safe/recovery action | Trust region algorithms for reinforcement learning (Schulman et al., 2015; 2016) have policy updates of the form πk+1 = arg max π∈Πθ ... | p. 4 (5.2. Trust Region Methods), p. 3 (5. Constrained Policy Optimization) |
| Monitoring / re-entry | 실행 결과를 다시 risk decision에 반영한다 | executed action과 next observation | threshold, update, replan, abort 또는 return-to-task를 수행 | continue/correct/abort state | Policy search algorithms approach this problem by searching for the optimal policy within a set Πθ ⊆Π of parametrized policies with parameters ... | p. 3 (5. Constrained Policy Optimization), p. 5 (5.3. Trust Region Optimization for Constrained MDPs) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 6.1. Approximately Solving the CPO Update - extractive body cue:** However, for small step sizes δ, the objective and cost constraints are well-approximated by linearizing around πk, and the KLdivergence constraint is well-approximated by second ...
- **p. 5 / 6.1. Approximately Solving the CPO Update - extractive body cue:** Denoting the gradient of the objective as g, the gradient of constraint i as bi, the Hessian of the KL-divergence as H, and defining ci ...
- **p. 3 / 5. Constrained Policy Optimization - extractive body cue:** When the objective is estimated by linearizing around πk as J(πk) + gT (θ -θk), g is the policy gradient, and the standard policy gradient ...
- **p. 3 / 5. Constrained Policy Optimization - extractive body cue:** The surrogates we choose are easy to estimate from samples collected on πk, and are good local approximations for the objective and constraints.
- **p. 6 / 6.3. Tightening Constraints via Cost Shaping - extractive body cue:** In our experiments, where we have only one constraint, we partition states into safe states and unsafe states, and the agent suffers a safety cost ...
- **p. 6 / 6.3. Tightening Constraints via Cost Shaping - extractive body cue:** Because of the various approximations between (3) and our practical algorithm, it is important to build a factor of safety into the algorithm to minimize ...
- **Formal bridge:** state/history and risk h(s) -> filtered/recovery action u_safe -> task utility subject to safety constraint -> low violation/failure probability with useful intervention.
- **Equation/algorithm anchors:** p. 5 (6.1. Approximately Solving the CPO Update), p. 5 (6.1. Approximately Solving the CPO Update), p. 3 (5. Constrained Policy Optimization), p. 3 (5. Constrained Policy Optimization), p. 6 (6.2. Feasibility), p. 6 (6.1. Approximately Solving the CPO Update).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Constrained, Policy, Optimization, Algorithm, Input, Initial, tolerance, Sample, trajectories, Form, estimates, approximate, CPO, feasible | observation, uncertainty/risk estimate와 task command | body cue; exact tensor/frame verify |
| State/latent | Constrained, Policy, Optimization, Algorithm, Input, Initial, tolerance, Sample, trajectories, Form | safe set, recovery state 또는 constraint margin | body cue; notation verify |
| Action/output | first, algorithm, allowing, applications, constrained, deep, Then, because, theoretically, guaranteed | shielded, recovery 또는 safe action | body cue; unit/decoder verify |
| Objective/constraint | However, small, step, sizes, objective, cost, constraints, well-approximated, linearizing, around | task utility subject to safety constraint | equation anchor required |

## Observation–State–Action Interface

- **p. 6 / 6.1. Approximately Solving the CPO Update - extractive body cue:** Constrained Policy Optimization Algorithm 1 Constrained Policy Optimization Input: Initial policy π0 ∈Πθ tolerance α for k = 0, 1, 2, ... do Sample a ...
- **p. 1 / 1. Introduction - extractive body cue:** Recently, deep reinforcement learning has enabled neural network policies to achieve state-of-the-art performance on many high-dimensional control tasks, including Atari games (using pixels as inputs) ...
- **p. 4 / 5.2. Trust Region Methods - extractive body cue:** Despite the approximation, trust region steps usually give monotonic improvements (Schulman et al., 2015; Duan et al., 2016) and have shown state-of-the-art performance in the ...
- **p. 1 / 1. Introduction - extractive body cue:** Currently, policy search algorithms enjoy state-of-theart performance on high-dimensional control tasks (Mnih et al., 2016; Duan et al., 2016).
- **p. 5 / 5.3. Trust Region Optimization for Constrained MDPs - extractive body cue:** First, we describe a policy search update for CMDPs that alleviates the issue of off-policy evaluation, and comes with guarantees of monotonic performance improvement and ...
- **p. 5 / 5.3. Trust Region Optimization for Constrained MDPs - extractive body cue:** (Observe that the constraint here is on an upper bound for JCi(π) by (6).) The off-policy evaluation issue is alleviated, because both the objective and ...
- **p. 4 / 5.2. Trust Region Methods - extractive body cue:** Trust region algorithms for reinforcement learning (Schulman et al., 2015; 2016) have policy updates of the form πk+1 = arg max π∈Πθ E s∼dπk a∼π ...
- **Normalized interface:** observation=observation, uncertainty/risk estimate와 task command; state=safe set, recovery state 또는 constraint margin; output/action=shielded, recovery 또는 safe action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | 현재 command의 one-step safety 또는 recovery trajectory horizon; exact lookahead 확인 필요. | Trust region algorithms for reinforcement learning (Schulman et al., 2015; 2016) have policy updates of the form πk+1 = arg max π∈Πθ ... | episode/sequence/action-chunk boundary |
| Rate / latency | nominal policy와 safety monitor/filter의 runtime rate를 별도로 기록한다. | Despite the approximation, trust region steps usually give monotonic improvements (Schulman et al., 2015; Duan et al., 2016) and have shown state-of-the-art ... | Hz/fps, inference time and control rate |
| Memory | risk score, recent trajectory/history와 recovery state. | not recovered | window and reset |
| Compute | risk inference, barrier/QP solve 또는 backup policy selection이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 6.1. Approximately Solving the CPO Update - extractive body cue:** Constrained Policy Optimization Algorithm 1 Constrained Policy Optimization Input: Initial policy π0 ∈Πθ tolerance α for k = 0, 1, 2, ... do Sample a ...
- **p. 5 / 5.3. Trust Region Optimization for Constrained MDPs - extractive body cue:** First, we describe a policy search update for CMDPs that alleviates the issue of off-policy evaluation, and comes with guarantees of monotonic performance improvement and ...
- **p. 3 / 5. Constrained Policy Optimization - extractive body cue:** We conclude by motivating, presenting, and proving gurantees on our algorithm, Constrained Policy Optimization (CPO), a trust region method for CMDPs.
- **p. 6 / 6.2. Feasibility - extractive body cue:** We give the pseudocode for our algorithm (for the single-constraint case) as Algorithm 1.
- **p. 7 / 8. Experiments - extractive body cue:** Average performance for CPO, PDO, and TRPO over several seeds (5 in the Point environments, 10 in all others); the x-axis is training iteration.
- **p. 8 / 8.1. Evaluating CPO and Comparison Analysis - extractive body cue:** Furthermore, we argue that this is not adequate in general: after the dual variable decreases, the agent could learn a new behavior that increases the ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Constrained, Policy, Optimization, Algorithm, Input, Initial, tolerance, Sample, trajectories, Form, estimates, approximate, CPO, feasible, then, Solve, dual, problem, Compute, proposal.
- **Relevant PDF headings:** 5. Constrained Policy Optimization (p. 3); 5.1. Policy Performance Bounds (p. 3); 5.2. Trust Region Methods (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Risk / failure representation | We consider two tasks, and train multiple different agents (robots) for each task: • Circle: The agent is rewarded for running in ... | p. 6 (8. Experiments), p. 7 (8.1. Evaluating CPO and Comparison Analysis) |
| Filtering / recovery | We find that CPO generally outperforms PDO on enforcing constraints, without compromising performance with respect to return. | p. 8 (8.1. Evaluating CPO and Comparison Analysis), p. 6 (8. Experiments) |
| Monitoring / re-entry | We find that CPO generally outperforms PDO on enforcing constraints, without compromising performance with respect to return. | p. 8 (8.1. Evaluating CPO and Comparison Analysis), p. 8 (8.1. Evaluating CPO and Comparison Analysis) |

## Failure and Ablation Link

- **p. 8 / 8.2. Ablation on Cost Shaping - extractive body cue:** However, CPO is nearly constraint-satisfying even without cost shaping.
- **p. 8 / 8.2. Ablation on Cost Shaping - extractive body cue:** In Figure 3, we compare performance of CPO with and without cost shaping in the constraint.
- **p. 5 / 6.1. Approximately Solving the CPO Update - extractive body cue:** For the special case where there is only one constraint, we give an analytical solution in the supplementary material (Theorem 2) which removes the need ...
- **p. 6 / 6.2. Feasibility - extractive body cue:** Sometimes (11) will still be feasible and CPO can automatically recover from its bad step, but for the infeasible case, a recovery method is necessary.
- **p. 6 / 6.3. Tightening Constraints via Cost Shaping - extractive body cue:** We choose ∆to be the probability of entering an unsafe state within a fixed time horizon, according to a learned model that is updated at ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 6 (6.1. Approximately Solving the CPO Update), p. 4 (5.2. Trust Region Methods), p. 3 (5. Constrained Policy Optimization), p. 5 (5.3. Trust Region Optimization for Constrained MDPs), p. 4 (5.2. Trust Region Methods), p. 5 (5.3. Trust Region Optimization for Constrained MDPs), objective p. 5 (6.1. Approximately Solving the CPO Update), p. 5 (6.1. Approximately Solving the CPO Update), p. 3 (5. Constrained Policy Optimization), p. 3 (5. Constrained Policy Optimization), p. 6 (6.3. Tightening Constraints via Cost Shaping), p. 6 (6.3. Tightening Constraints via Cost Shaping), temporal p. 4 (5.2. Trust Region Methods), p. 4 (5.2. Trust Region Methods), p. 5 (6.1. Approximately Solving the CPO Update), p. 6 (6.2. Feasibility), p. 6 (6.2. Feasibility), p. 7 (8.1. Evaluating CPO and Comparison Analysis).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
