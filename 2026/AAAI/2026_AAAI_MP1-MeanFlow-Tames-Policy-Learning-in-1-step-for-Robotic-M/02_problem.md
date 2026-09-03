# Problem - MP1: MeanFlow Tames Policy Learning in 1-step for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ojs.aaai.org/index.php/AAAI/article/view/38919; PDF retrieval source: https://ojs.aaai.org/index.php/AAAI/article/view/38919. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (Abstract), p. 2 (Abstract), p. 1 (Abstract), p. 1 (Abstract), p. 3 (Abstract)): However, diffusion still faces challenges related to inference time.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** In robot manipulation, robot learning has become a prevailing approach.
- **p. 1 / Abstract - extractive body cue:** However, generative models within this field face a fundamental trade-off between the slow, iterative sampling of diffusion models and the architectural constraints of faster Flow-based ...
- **p. 1 / Abstract - extractive body cue:** To address these limitations, we introduce MP1, which pairs 3D point-cloud inputs with the MeanFlow paradigm to generate action trajectories in one network function evaluation ...
- **p. 1 / Abstract - extractive body cue:** By directly learning the interval-averaged velocity via the "MeanFlow Identity", our policy avoids any additional consistency constraints.
- **p. 1 / Abstract - extractive body cue:** This formulation eliminates numerical ODE-solver errors during inference, yielding more precise trajectories.
- **p. 2 / Abstract - extractive body cue:** However, diffusion still faces challenges related to inference time.
- **p. 2 / Abstract - extractive body cue:** However, 2D inputs often lack depth information, which limits the accuracy in completing tasks.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, diffusion still faces challenges related to inference time. | demonstration으로 정의된 robot task distribution | body wording is the source claim |
| Observation / input | MP1: One-Step Trajectory Generation In the context of robot learning, the policy's task is to map a sequence of observations, including 3D ... | observation history와 expert trajectory/action | exact sensor/frame/preprocessing from PDF body |
| State / latent | MP1, One-Step, Trajectory, Generation, context, robot, learning, policy, task, sequence | behavior policy와 temporal action context | notation and tensor shape require body check |
| Output / action | lead, form, feature, collapse, where, policy, network, maps | predicted action 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | closed-loop task success and robustness | imitation error, task success, robustness와 compounding error | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | observation history o_{t−H:t}; body terms: MP1, One-Step, Trajectory, Generation, context, robot, learning, policy, task, sequence | p. 3 (Abstract), p. 3 (Abstract), p. 4 (Abstract) |
| Decision / output variable | expert-like action/chunk a_{t:t+H}; body terms: contributions, follows, introduce, MP1, first, MeanFlow-based, robot, learning | p. 2 (Abstract), p. 1 (Abstract), p. 1 (Abstract) |
| Objective / loss / cost | imitation or action-distribution loss; cue terms: However, generative, models, within, field, face, fundamental, trade-off | p. 1 (Abstract), p. 4 (Abstract), p. 4 (Abstract), p. 1 (Abstract), p. 2 (Abstract), p. 2 (Abstract) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (Abstract), p. 2 (Abstract), p. 3 (Abstract) |
| Success / guarantee | closed-loop task success and robustness | p. 6 (Figure/Table caption), p. 7 (Abstract), p. 7 (Abstract) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / Abstract - extractive body cue:** However, 2D inputs often lack depth information, which limits the accuracy in completing tasks.
- **p. 1 / Abstract - extractive body cue:** To address these limitations, we introduce MP1, which pairs 3D point-cloud inputs with the MeanFlow paradigm to generate action trajectories in one network function evaluation ...
- **p. 1 / Abstract - extractive body cue:** Since action generation requires multiple time steps to denoise, the inference process can be time-consuming, which may become a bottleneck in applications that demand real-time ...
- **p. 3 / Abstract - extractive body cue:** To address these challenges, we propose the MP1 (Fig.

## What the Paper Changes

PDF body contribution framing (p. 2 (Abstract), p. 1 (Abstract), p. 1 (Abstract), p. 2 (Abstract), p. 3 (Abstract)): Our contributions are as follows: • We introduce MP1, the first MeanFlow-based robot learning framework.

- **p. 1 / Abstract - extractive body cue:** We validate our method on the Adroit and Meta-World benchmarks, as well as in real-world scenarios.
- **p. 1 / Abstract - extractive body cue:** To address these limitations, we introduce MP1, which pairs 3D point-cloud inputs with the MeanFlow paradigm to generate action trajectories in one network function evaluation ...
- **p. 2 / Abstract - extractive body cue:** We present the first adaptation of the MeanFlow (Geng et al.
- **p. 3 / Abstract - extractive body cue:** To address these challenges, we propose the MP1 (Fig.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 4 | MP1 FlowPolicy Adroit: Hammer (FlowPolicy: 15.3ms/ MP1:7.1ms) Real-world: Hammer (FlowPolicy: 22.3s/ MP1:18.6s) failure success Figure 3: Qualitative comparison ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 2 | 3D Input Robot Learning To overcome the limitations of 2D inputs, 3D inputs have gained prominence. | reported limitation/failure wording; scope must be verified |
| body cue at p. 2 | However, a purely regression-based objective fails to impose explicit regularization on the policy's internal feature space (Wang and ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | Moreover, our method successfully completes the real-world hammer task, whereas FlowPolicy fails. estimate of the total derivative, with ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

il writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (Abstract), p. 3 (Abstract), p. 4 (Abstract), p. 4 (Abstract). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (Abstract), p. 2 (Abstract), p. 1 (Abstract), p. 1 (Abstract), p. 3 (Abstract), interface p. 3 (Abstract), p. 3 (Abstract), p. 4 (Abstract), p. 4 (Abstract), objective p. 1 (Abstract), p. 4 (Abstract), p. 4 (Abstract), p. 1 (Abstract), p. 2 (Abstract), p. 2 (Abstract).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** However, diffusion still faces challenges related to inference time. (p. 2, Abstract).
- **Formulation-changing contribution:** Our contributions are as follows: • We introduce MP1, the first MeanFlow-based robot learning framework. (p. 2, Abstract).
- **Assumption/failure evidence:** However, a purely regression-based objective fails to impose explicit regularization on the policy's internal feature space (Wang and He 2025). (p. 2, Abstract).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
