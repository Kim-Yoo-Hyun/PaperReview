# Evaluation - Constrained Policy Optimization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v70/achiam17a.html; PDF retrieval source: https://arxiv.org/pdf/1705.10528. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (8.1. Evaluating CPO and Comparison Analysis), p. 8 (8.1. Evaluating CPO and Comparison Analysis), p. 7 (8.1. Evaluating CPO and Comparison Analysis), p. 7 (8. Experiments)): We find that CPO generally outperforms PDO on enforcing constraints, without compromising performance with respect to return.

## Evaluation Body Digest

- **p. 6 / 8. Experiments - extractive body cue:** We consider two tasks, and train multiple different agents (robots) for each task: • Circle: The agent is rewarded for running in a wide circle, ...
- **p. 7 / 8.1. Evaluating CPO and Comparison Analysis - extractive body cue:** To benchmark the environments, we also include TRPO (trust region policy optimization) (Schulman et al., 2015), a stateof-the-art unconstrained reinforcement learning algorithm.
- **p. 7 / 8. Experiments - extractive body cue:** We experiment with three different agents: a point-mass (S ⊆R9, A ⊆R2), a quadruped robot (called an ‘ant') (S ⊆R32, A ⊆R8), and a simple ...
- **p. 8 / 8.1. Evaluating CPO and Comparison Analysis - extractive body cue:** In the Point environments, we experiment with ν0 = 1000 and show that although this does assure constraint satisfaction, it also can substantially harm performance ...
- **p. 8 / 8.1. Evaluating CPO and Comparison Analysis - extractive body cue:** Using cost shaping (CS) in the constraint while optimizing generally improves the agent's adherence to the true constraint on C-return. environment and makes sense when ...
- **p. 5 / 6.1. Approximately Solving the CPO Update - extractive body cue:** However, for small step sizes δ, the objective and cost constraints are well-approximated by linearizing around πk, and the KLdivergence constraint is well-approximated by second ...
- **p. 5 / 6.1. Approximately Solving the CPO Update - extractive body cue:** Denoting the gradient of the objective as g, the gradient of constraint i as bi, the Hessian of the KL-divergence as H, and defining ci ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 1. Average performance for CPO, PDO, and TRPO over several seeds (5 in the Point environments, 10 in all others); the x-axis is training ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** uncertain robot state와 safe/unsafe operating region.
- **Input boundary:** observation, uncertainty/risk estimate와 task command.
- **Output/decision under evaluation:** shielded, recovery 또는 safe action.
- **Primary target:** task return과 violation/failure probability.
- **Detected evaluation headings:** 6. Practical Implementation (p. 5); 8. Experiments (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 8.1. Evaluating CPO and Comparison Analysis | EMPIRICAL / SOURCE-REPORTED EVALUATION | We find that CPO generally outperforms PDO on enforcing constraints, without compromising performance with respect to return. | p. 8 (8.1. Evaluating CPO and Comparison Analysis) |
| 8.1. Evaluating CPO and Comparison Analysis | EMPIRICAL / SOURCE-REPORTED EVALUATION | Using cost shaping (CS) in the constraint while optimizing generally improves the agent's adherence to the true constraint on C-return. environment and makes sense ... | p. 8 (8.1. Evaluating CPO and Comparison Analysis) |
| 8.1. Evaluating CPO and Comparison Analysis | EMPIRICAL / SOURCE-REPORTED EVALUATION | We find that CPO is successful at approximately enforcing constraints in all environments. | p. 7 (8.1. Evaluating CPO and Comparison Analysis) |
| 8. Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Average performance for CPO, PDO, and TRPO over several seeds (5 in the Point environments, 10 in all others); the x-axis is training iteration. | p. 7 (8. Experiments) |

## Dataset / Benchmark Role

- **p. 6 / 8. Experiments - extractive body cue:** We consider two tasks, and train multiple different agents (robots) for each task: • Circle: The agent is rewarded for running in a wide circle, ...
- **p. 7 / 8.1. Evaluating CPO and Comparison Analysis - extractive body cue:** To benchmark the environments, we also include TRPO (trust region policy optimization) (Schulman et al., 2015), a stateof-the-art unconstrained reinforcement learning algorithm.
- **p. 7 / 8. Experiments - extractive body cue:** We experiment with three different agents: a point-mass (S ⊆R9, A ⊆R2), a quadruped robot (called an ‘ant') (S ⊆R32, A ⊆R8), and a simple ...
- **p. 8 / 8.1. Evaluating CPO and Comparison Analysis - extractive body cue:** In the Point environments, we experiment with ν0 = 1000 and show that although this does assure constraint satisfaction, it also can substantially harm performance ...
- **p. 8 / 8.1. Evaluating CPO and Comparison Analysis - extractive body cue:** Using cost shaping (CS) in the constraint while optimizing generally improves the agent's adherence to the true constraint on C-return. environment and makes sense when ...
- **p. 5 / 6.1. Approximately Solving the CPO Update - extractive body cue:** However, for small step sizes δ, the objective and cost constraints are well-approximated by linearizing around πk, and the KLdivergence constraint is well-approximated by second ...
- **p. 5 / 6.1. Approximately Solving the CPO Update - extractive body cue:** Denoting the gradient of the objective as g, the gradient of constraint i as bi, the Hessian of the KL-divergence as H, and defining ci ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 7 / Figure/Table caption - extractive body cue:** Figure 1. Average performance for CPO, PDO, and TRPO over several seeds (5 in the Point environments, 10 in all others); the x-axis is training ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 2. The Humanoid-Circle and Point-Gather environments. In Humanoid-Circle, the safe area is between the blue panels. son to be fair, we give PDO every ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 3. Using cost shaping (CS) in the constraint while optimiz- ing generally improves the agent's adherence to the true constraint on C-return. environment and ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4. Comparison between CPO and FPO (fixed penalty opti- mization) for various values of fixed penalty.
- **p. 17 / Figure/Table caption - extractive body cue:** Figure 5. In the Circle task, reward is maximized by moving along the green circle. The agent is not allowed to enter the blue regions, ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We consider two tasks, and train multiple different agents (robots) for each task: • Circle: The agent is rewarded for running in a wide ... | embodiment, simulator version and control stack | p. 6 (8. Experiments), p. 7 (8.1. Evaluating CPO and Comparison Analysis) |
| Task/environment | To benchmark the environments, we also include TRPO (trust region policy optimization) (Schulman et al., 2015), a stateof-the-art unconstrained reinforcement learning algorithm. | reset, timeout, object/scene variation | p. 7 (8.1. Evaluating CPO and Comparison Analysis), p. 7 (8. Experiments) |
| Observation/sensor | observation, uncertainty/risk estimate와 task command | calibration, preprocessing, privileged input | p. 6 (6.1. Approximately Solving the CPO Update), p. 1 (1. Introduction) |
| Output/decision | shielded, recovery 또는 safe action | action frame, controller and termination | p. 4 (5.2. Trust Region Methods), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 1. Average performance for CPO, PDO, and TRPO over several seeds (5 in the Point environments, 10 in all others); the x-axis is ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| We consider two tasks, and train multiple different agents (robots) for each task: • Circle: The agent is rewarded for running in a wide ... | definition/direction/unit from same section | p. 6 (8. Experiments) |
| The reward and constraint cost functions are described in supplementary material (Section 10.3.1). | definition/direction/unit from same section | p. 7 (8. Experiments) |
| The cost shaping does help, almost completely accounting for CPO's inherent approximation errors. | definition/direction/unit from same section | p. 8 (8.2. Ablation on Cost Shaping) |
| In contrast, CPO automatically picks penalty coefficients to attain the desired trade-off between reward and constraint cost. | definition/direction/unit from same section | p. 8 (8.3. Constraint vs. Fixed Penalty) |
| Due to approximation errors, CPO may take a bad step and produce an infeasible iterate πk. | definition/direction/unit from same section | p. 6 (6.2. Feasibility) |
| To address the issue of approximation and sampling errors that arise in practice, as well as the potential violations described by Proposition 2, we ... | definition/direction/unit from same section | p. 5 (6. Practical Implementation) |
| Figure 5. In the Circle task, reward is maximized by moving along the green circle. The agent is not allowed to enter the blue ... | definition/direction/unit from same section | p. 17 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We find that CPO generally outperforms PDO on enforcing constraints, without compromising performance with respect to return. | comparison identity and matched condition | p. 8 (8.1. Evaluating CPO and Comparison Analysis) |
| In our experiments, we aim to answer the following: • Does CPO succeed at enforcing behavioral constraints when training neural network policies with thousands ... | comparison identity and matched condition | p. 6 (8. Experiments) |
| For our comparison, we implement PDO with (16) as the update rule for the dual variables, using a constant learning rate α; details are ... | comparison identity and matched condition | p. 7 (8.1. Evaluating CPO and Comparison Analysis) |
| Our metric for comparison is the C-return, the ‘true' constraint. | comparison identity and matched condition | p. 8 (8.2. Ablation on Cost Shaping) |
| This is a convex program in m+1 variables; when the number of constraints is small by comparison to the dimension of θ, this is ... | comparison identity and matched condition | p. 5 (6.1. Approximately Solving the CPO Update) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| However, CPO is nearly constraint-satisfying even without cost shaping. | component/input/data sensitivity | p. 8 (8.2. Ablation on Cost Shaping) |
| In Figure 3, we compare performance of CPO with and without cost shaping in the constraint. | component/input/data sensitivity | p. 8 (8.2. Ablation on Cost Shaping) |
| For the special case where there is only one constraint, we give an analytical solution in the supplementary material (Theorem 2) which removes the ... | component/input/data sensitivity | p. 5 (6.1. Approximately Solving the CPO Update) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this work, we propose the first such algorithm, allowing applications to constrained deep RL. | We find that CPO generally outperforms PDO on enforcing constraints, without compromising performance with respect to return. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (8.1. Evaluating CPO and Comparison Analysis), p. 8 (8.1. Evaluating CPO and Comparison Analysis), p. 7 (8.1. Evaluating CPO and Comparison Analysis), p. 7 (8. Experiments) |
| Primary metric/result | Using cost shaping (CS) in the constraint while optimizing generally improves the agent's adherence to the true constraint on C-return. environment and makes sense ... | numeric claim only at cited anchor | p. 8 (8.1. Evaluating CPO and Comparison Analysis) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Sometimes (11) will still be feasible and CPO can automatically recover from its bad step, but for the infeasible case, a recovery method is ... | p. 6 (6.2. Feasibility) |
| body limitation/failure cue | We choose ∆to be the probability of entering an unsafe state within a fixed time horizon, according to a learned model that is updated ... | p. 6 (6.3. Tightening Constraints via Cost Shaping) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For our comparison, we implement PDO with (16) as the update rule for the dual variables, using a constant learning rate α; details are ... | p. 7 (8.1. Evaluating CPO and Comparison Analysis) |
| In this section, we show how to implement an approximation to the update (10) that can be efficiently computed, even when optimizing policies with ... | p. 5 (6. Practical Implementation) |
| We give the pseudocode for our algorithm (for the single-constraint case) as Algorithm 1. | p. 6 (6.2. Feasibility) |
| Like (Schulman et al., 2015), we approximately compute them using the conjugate gradient method. | p. 6 (6.1. Approximately Solving the CPO Update) |
| Average performance for CPO, PDO, and TRPO over several seeds (5 in the Point environments, 10 in all others); the x-axis is training iteration. | p. 7 (8. Experiments) |
| Furthermore, we argue that this is not adequate in general: after the dual variable decreases, the agent could learn a new behavior that increases ... | p. 8 (8.1. Evaluating CPO and Comparison Analysis) |
| When using sampling to compute policy updates, as is typically done in high-dimensional control (Duan et al., 2016), this requires off-policy evaluation, which is ... | p. 3 (5. Constrained Policy Optimization) |
| Our theoretical analysis shows that for our choices of surrogates, we can bound our update's worstcase performance and worst-case constraint violation with values that ... | p. 3 (5. Constrained Policy Optimization) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 6.2. Feasibility - extractive body cue:** Sometimes (11) will still be feasible and CPO can automatically recover from its bad step, but for the infeasible case, a recovery method is necessary.
- **p. 6 / 6.3. Tightening Constraints via Cost Shaping - extractive body cue:** We choose ∆to be the probability of entering an unsafe state within a fixed time horizon, according to a learned model that is updated at ...

- **Evidence anchors reviewed:** datasets p. 6 (8. Experiments), p. 7 (8.1. Evaluating CPO and Comparison Analysis), p. 7 (8. Experiments), p. 8 (8.1. Evaluating CPO and Comparison Analysis), p. 8 (8.1. Evaluating CPO and Comparison Analysis), p. 5 (6.1. Approximately Solving the CPO Update), metrics p. 7 (Figure/Table caption), p. 6 (8. Experiments), p. 7 (8. Experiments), p. 8 (8.2. Ablation on Cost Shaping), p. 8 (8.3. Constraint vs. Fixed Penalty), p. 6 (6.2. Feasibility), baselines p. 8 (8.1. Evaluating CPO and Comparison Analysis), p. 6 (8. Experiments), p. 7 (8.1. Evaluating CPO and Comparison Analysis), p. 8 (8.2. Ablation on Cost Shaping), p. 5 (6.1. Approximately Solving the CPO Update), results p. 8 (8.1. Evaluating CPO and Comparison Analysis), p. 8 (8.1. Evaluating CPO and Comparison Analysis), p. 7 (8.1. Evaluating CPO and Comparison Analysis), p. 7 (8. Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** In our experiments, we aim to answer the following: • Does CPO succeed at enforcing behavioral constraints when training neural network policies with thousands of parameters? • How does CPO ... (p. 6, 8. Experiments).
- **Metric evidence:** We find that CPO generally outperforms PDO on enforcing constraints, without compromising performance with respect to return. (p. 8, 8.1. Evaluating CPO and Comparison Analysis).
- **Baseline/ablation evidence:** We find that CPO generally outperforms PDO on enforcing constraints, without compromising performance with respect to return. (p. 8, 8.1. Evaluating CPO and Comparison Analysis).
- **Failure/negative evidence:** Additionally, PDO is sensitive to the initialization of the dual variable. (p. 7, 8.1. Evaluating CPO and Comparison Analysis).
