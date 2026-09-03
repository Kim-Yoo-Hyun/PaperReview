# Problem - Constrained Policy Optimization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v70/achiam17a.html; PDF retrieval source: https://arxiv.org/pdf/1705.10528. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction)): Although optimal policies for finite CMDPs with known models can be obtained by linear programming, methods for high-dimensional control are lacking.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** For many applications of reinforcement learning it can be more convenient to specify both a reward function and constraints, rather than trying to design behavior ...
- **p. 1 / Abstract - extractive body cue:** For example, systems that physically interact with or around humans should satisfy safety constraints.
- **p. 1 / Abstract - extractive body cue:** Recent advances in policy search algorithms (Mnih et al., 2016; Schulman et al., 2015; Lillicrap et al., 2016; Levine et al., 2016) have enabled new ...
- **p. 1 / Abstract - extractive body cue:** We propose Constrained Policy Optimization (CPO), the first general-purpose policy search algorithm for constrained reinforcement learning with guarantees for near-constraint satisfaction at each iteration.
- **p. 1 / Abstract - extractive body cue:** Our method allows us to train neural network policies for high-dimensional control while making guarantees about policy behavior all throughout training.
- **p. 1 / 1. Introduction - extractive body cue:** Although optimal policies for finite CMDPs with known models can be obtained by linear programming, methods for high-dimensional control are lacking.
- **p. 1 / 1. Introduction - extractive body cue:** Currently, policy search algorithms enjoy state-of-theart performance on high-dimensional control tasks (Mnih et al., 2016; Duan et al., 2016).

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Although optimal policies for finite CMDPs with known models can be obtained by linear programming, methods for high-dimensional control are lacking. | uncertain robot state와 safe/unsafe operating region | body wording is the source claim |
| Observation / input | Constrained Policy Optimization Algorithm 1 Constrained Policy Optimization Input: Initial policy π0 ∈Πθ tolerance α for k = 0, 1, 2, ... ... | observation, uncertainty/risk estimate와 task command | exact sensor/frame/preprocessing from PDF body |
| State / latent | Constrained, Policy, Optimization, Algorithm, Input, Initial, tolerance, Sample, trajectories, Form | safe set, recovery state 또는 constraint margin | notation and tensor shape require body check |
| Output / action | Despite, approximation, trust, region, steps, usually, give, monotonic | shielded, recovery 또는 safe action | exact unit/frame/decoder require body check |
| Target outcome | low violation/failure probability with useful intervention | task return과 violation/failure probability | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | state/history and risk h(s); body terms: Constrained, Policy, Optimization, Algorithm, Input, Initial, tolerance, Sample, trajectories, Form | p. 6 (6.1. Approximately Solving the CPO Update), p. 1 (1. Introduction), p. 4 (5.2. Trust Region Methods) |
| Decision / output variable | filtered/recovery action u_safe; body terms: first, algorithm, allowing, applications, constrained, deep, Then, because | p. 1 (1. Introduction), p. 5 (5.3. Trust Region Optimization for Constrained MDPs), p. 5 (5.3. Trust Region Optimization for Constrained MDPs) |
| Objective / loss / cost | task utility subject to safety constraint; cue terms: However, small, step, sizes, objective, cost, constraints, well-approximated | p. 5 (6.1. Approximately Solving the CPO Update), p. 5 (6.1. Approximately Solving the CPO Update), p. 3 (5. Constrained Policy Optimization), p. 3 (5. Constrained Policy Optimization), p. 6 (6.2. Feasibility), p. 6 (6.1. Approximately Solving the CPO Update) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (5. Constrained Policy Optimization), p. 6 (6.3. Tightening Constraints via Cost Shaping), p. 6 (6.3. Tightening Constraints via Cost Shaping) |
| Success / guarantee | low violation/failure probability with useful intervention | p. 7 (Figure/Table caption), p. 6 (8. Experiments), p. 7 (8. Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** Currently, policy search algorithms enjoy state-of-theart performance on high-dimensional control tasks (Mnih et al., 2016; Duan et al., 2016).

## What the Paper Changes

PDF body contribution framing (p. 1 (1. Introduction), p. 5 (5.3. Trust Region Optimization for Constrained MDPs), p. 5 (5.3. Trust Region Optimization for Constrained MDPs), p. 1 (1. Introduction), p. 2 (1. Introduction)): In this work, we propose the first such algorithm, allowing applications to constrained deep RL.

- **p. 5 / 5.3. Trust Region Optimization for Constrained MDPs - extractive body cue:** Then, because the theoretically guaranteed update will take toosmall steps in practice, we propose CPO as a practical approximation based on trust region methods.
- **p. 5 / 5.3. Trust Region Optimization for Constrained MDPs - extractive body cue:** Inspired by trust region methods, we propose CPO, which uses a trust region instead of penalties on policy divergence to enable larger step sizes: πk+1 ...
- **p. 1 / 1. Introduction - extractive body cue:** Driving our approach is a new theoretical result that bounds the difference between the rewards or costs of two different policies.
- **p. 2 / 1. Introduction - extractive body cue:** In our experiments, we show that CPO can train neural network policies with thousands of parameters on highdimensional simulated robot locomotion tasks to maximize rewards ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | Sometimes (11) will still be feasible and CPO can automatically recover from its bad step, but for the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | We choose ∆to be the probability of entering an unsafe state within a fixed time horizon, according to ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

safety writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 6 (6.1. Approximately Solving the CPO Update), p. 1 (1. Introduction), p. 4 (5.2. Trust Region Methods), p. 1 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), interface p. 6 (6.1. Approximately Solving the CPO Update), p. 1 (1. Introduction), p. 4 (5.2. Trust Region Methods), p. 1 (1. Introduction), objective p. 5 (6.1. Approximately Solving the CPO Update), p. 5 (6.1. Approximately Solving the CPO Update), p. 3 (5. Constrained Policy Optimization), p. 3 (5. Constrained Policy Optimization), p. 6 (6.2. Feasibility), p. 6 (6.1. Approximately Solving the CPO Update).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** Although optimal policies for finite CMDPs with known models can be obtained by linear programming, methods for high-dimensional control are lacking. (p. 1, 1. Introduction).
- **Formulation-changing contribution:** In this work, we propose the first such algorithm, allowing applications to constrained deep RL. (p. 1, 1. Introduction).
- **Assumption/failure evidence:** Additionally, PDO is sensitive to the initialization of the dual variable. (p. 7, 8.1. Evaluating CPO and Comparison Analysis).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
