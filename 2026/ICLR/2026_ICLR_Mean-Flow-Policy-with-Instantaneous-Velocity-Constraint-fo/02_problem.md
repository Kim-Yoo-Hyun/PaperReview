# Problem - Mean Flow Policy with Instantaneous Velocity Constraint for One-step Action Generation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=mIeKe74W43; PDF retrieval source: https://arxiv.org/pdf/2602.13810. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION)): However, a key limitation of existing generative policies is their dependence on iterative multi-step refinement from noise to actions (Wang et al., 2024a; 2025; Ding et al., 2024).

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive body cue:** Learning expressive and efficient policy functions is a promising direction in reinforcement learning (RL).
- **p. 1 / ABSTRACT - extractive body cue:** While flow-based policies have recently proven effective in modeling complex action distributions with a fast deterministic sampling process, they still face a trade-off between expressiveness ...
- **p. 1 / ABSTRACT - extractive body cue:** In this work, we propose mean velocity policy (MVP), a new generative policy function that models the mean velocity field to achieve the fastest one-step ...
- **p. 1 / ABSTRACT - extractive body cue:** To ensure its high expressiveness, an instantaneous velocity constraint (IVC) is introduced on the mean velocity field during training.
- **p. 1 / ABSTRACT - extractive body cue:** We theoretically prove that this design explicitly serves as a crucial boundary condition, thereby improving learning accuracy and enhancing policy expressiveness.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, a key limitation of existing generative policies is their dependence on iterative multi-step refinement from noise to actions (Wang et al., 2024a; 2025; Ding ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, this ODE theoretically suffers from the problem of multiple solutions due to a lack of explicit boundary conditions, that is, the value at any ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, a key limitation of existing generative policies is their dependence on iterative multi-step refinement from noise to actions (Wang et al., ... | multi-robot demonstration/dataset ecosystem | body wording is the source claim |
| Observation / input | For standard flow-based policies, this mapping is framed as a generative process: a velocity model, v(a(t), t, s), transforms a standard Gaussian ... | multi-view observation, language/task label과 action trajectory | exact sensor/frame/preprocessing from PDF body |
| State / latent | standard, flow-based, policies, mapping, framed, generative, process, velocity, model, transforms | shared representation, embodiment/task identity와 data distribution | notation and tensor shape require body check |
| Output / action | policy, defines, distribution, over, actions, given, state, Then | dataset sample 또는 learned policy action | exact unit/frame/decoder require body check |
| Target outcome | cross-domain transfer and task performance | coverage, cross-embodiment transfer, data efficiency와 task success | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | trajectory D with task/embodiment metadata; body terms: standard, flow-based, policies, mapping, framed, generative, process, velocity, model, transforms | p. 3 (3 METHOD), p. 2 (2 PRELIMINARIES), p. 3 (3 METHOD) |
| Decision / output variable | normalized sample or downstream action; body terms: contributions, summarized, threefold, flow-based, policy, namely, mean, velocity | p. 2 (1 INTRODUCTION), p. 3 (3 METHOD), p. 1 (1 INTRODUCTION) |
| Objective / loss / cost | coverage/data efficiency/transfer objective; cue terms: Let, denote, learnable, parameters, training, objective, minimize, residual | p. 5 (3 METHOD), p. 5 (3 METHOD), p. 3 (3 METHOD), p. 4 (3 METHOD), p. 4 (3 METHOD), p. 6 (3 METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (3 METHOD), p. 6 (3 METHOD), p. 3 (3 METHOD) |
| Success / guarantee | cross-domain transfer and task performance | p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, this ODE theoretically suffers from the problem of multiple solutions due to a lack of explicit boundary conditions, that is, the value at any ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Although the time-efficiency gains of MVP are very promising, its learning difficulty is higher than that of a standard flow policy.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** While existing flow policies learn instantaneous velocities and require multistep iterative sampling (Lipman et al., 2023; Park et al., 2025; Bharadhwaj et al., 2024), MVP ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1 INTRODUCTION), p. 3 (3 METHOD), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 5 (3 METHOD)): Our contributions are summarized threefold: • We propose a new flow-based policy, namely mean velocity policy (MVP), that enables fastest one-step action generation.

- **p. 3 / 3 METHOD - extractive body cue:** First, we introduce the mean velocity policy (MVP), showing how its integration with a "generateand-select" mechanism enables a direct mapping from noise to optimal actions.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** In this paper, we propose the mean velocity policy (MVP) as an affirmative answer.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address this, we introduce an instantaneous velocity constraint (IVC) to compensate for the lack of boundary conditions.
- **p. 5 / 3 METHOD - extractive body cue:** Inspired by this, we introduce the instantaneous velocity constraint (IVC), a training objective that explicitly enforces a boundary condition at t.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 3 | Figure 2: Velocity field: blue arrows de- note the mean velocity over a time in- terval, with red ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | The poor performance of BFN and QC is primarily because they rely on a 10-step flow policy, which ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

robot_data writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (3 METHOD), p. 2 (2 PRELIMINARIES), p. 3 (3 METHOD), p. 4 (3 METHOD). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), interface p. 3 (3 METHOD), p. 2 (2 PRELIMINARIES), p. 3 (3 METHOD), p. 4 (3 METHOD), objective p. 5 (3 METHOD), p. 5 (3 METHOD), p. 3 (3 METHOD), p. 4 (3 METHOD), p. 4 (3 METHOD), p. 6 (3 METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
