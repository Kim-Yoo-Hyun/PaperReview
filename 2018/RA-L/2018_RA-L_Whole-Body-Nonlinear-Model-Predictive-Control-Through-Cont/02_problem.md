# Problem - Whole-Body Nonlinear Model Predictive Control Through Contacts for Quadrupeds

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1712.02889; PDF retrieval source: https://arxiv.org/pdf/1712.02889. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): Also, especially interesting tasks such as periodic gaits could not be transferred to hardware due to model mismatches and lack of robustness of the plans.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** In this work we present a whole-body Nonlinear Model Predictive Control approach for Rigid Body Systems subject to contacts.
- **p. 1 / Abstract - extractive body cue:** We use a full dynamic system model which also includes explicit contact dynamics.
- **p. 1 / Abstract - extractive body cue:** Therefore, contact locations, sequences and timings are not prespecified but optimized by the solver.
- **p. 1 / Abstract - extractive body cue:** Yet, thorough numerical and software engineering allows for running the nonlinear Optimal Control solver at rates up to 190 Hz on a quadruped for a ...
- **p. 1 / Abstract - extractive body cue:** This outperforms the state of the art by at least one order of magnitude.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Also, especially interesting tasks such as periodic gaits could not be transferred to hardware due to model mismatches and lack of robustness of the plans.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this field, centroidal dynamics approaches [5]-[9] become increasingly popular as they capture the core dynamics of the problem.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Also, especially interesting tasks such as periodic gaits could not be transferred to hardware due to model mismatches and lack of robustness ... | high-DoF humanoid whole-body dynamics와 contacts | body wording is the source claim |
| Observation / input | It designs time-varying state-feedback controllers of the form un(x) = uff n + Kn(xn -xref n ) (8) where uff n is ... | proprioception, reference pose/motion, visual or language command | exact sensor/frame/preprocessing from PDF |
| State / latent | designs, time-varying, state-feedback, controllers, form, xref, where, feedforward, control, action | whole-body pose, balance/contact state와 skill/mode | notation and tensor shape require body check |
| Output / action | contrast, GNMS-NMPC, algorithm, summarized, designs, state, reference, trajectory | joint/whole-body action, motion target 또는 task trajectory | exact unit/frame/decoder require body check |
| Target outcome | motion/task success and recovery | tracking, balance, skill/task success와 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | whole-body pose/contact/reference state; body terms: designs, time-varying, state-feedback, controllers, form, xref, where, feedforward, control, action | p. 3 (III. NMPC APPROACH), p. 4 (IV. SOFTWARE IMPLEMENTATION), p. 3 (III. NMPC APPROACH) |
| Decision / output variable | joint/whole-body action; body terms: present, whole-body, Nonlinear, Model, Predictive, Control, NMPC, Rigid | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 4 (IV. SOFTWARE IMPLEMENTATION) |
| Objective / loss / cost | tracking/balance/task objective; cue terms: AN-1, BN-1, quadratize, cost, function, around, multiple-shooting, intervals | p. 3 (IV. SOFTWARE IMPLEMENTATION), p. 3 (III. NMPC APPROACH), p. 4 (IV. SOFTWARE IMPLEMENTATION) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (IV. SOFTWARE IMPLEMENTATION), p. 4 (IV. SOFTWARE IMPLEMENTATION), p. 4 (IV. SOFTWARE IMPLEMENTATION) |
| Success / guarantee | motion/task success and recovery | p. 5 (VI. RESULTS), p. 7 (VI. RESULTS), p. 7 (VI. RESULTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this field, centroidal dynamics approaches [5]-[9] become increasingly popular as they capture the core dynamics of the problem.
- **p. 1 / I. INTRODUCTION - extractive body cue:** We summarize our solver framework, which uses Auto-Differentiation and code generation to achieve high computational performance exceeding the current state of the art in robotics ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** In Section III we describe our approach of solving the problem.

## What the Paper Changes

PDF contribution framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 4 (IV. SOFTWARE IMPLEMENTATION), p. 2 (I. INTRODUCTION), p. 3 (IV. SOFTWARE IMPLEMENTATION)): In this paper, we present a whole-body Nonlinear Model Predictive Control (NMPC) approach for Rigid Body Dynamics (RBD) systems subject to contacts.

- **p. 1 / I. INTRODUCTION - extractive body cue:** Contributions In this work, we demonstrate whole-body, contact invariant nonlinear MPC for highly dynamic motions that require explicit reasoning about the full dynamics of the ...
- **p. 4 / IV. SOFTWARE IMPLEMENTATION - extractive body cue:** Since our code mostly consists of matrix and vector manipulations and register sizes of AVX are doubled over SSE, we obtained an additional speedup of ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** In Section III we describe our approach of solving the problem.
- **p. 3 / IV. SOFTWARE IMPLEMENTATION - extractive body cue:** While the development of processors with faster clock speed has stalled in recent years, processing power instead foremost grows due to higher computation core counts ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 3 | However, both parallel execution and vectorization cannot be leveraged automatically by standard compilers. | reported limitation/failure wording; scope must be verified |
| body cue at p. 3 | Also, many computational routines such as integrating a differential equation over time, are naturally sequential operations that cannot ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Furthermore, while most tasks by design stayed within the physical limitations of the platforms, GNMS would allow us ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | The resulting overall controller is stable and can robustly handle aforementioned disturbances. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

humanoid writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (III. NMPC APPROACH), p. 4 (IV. SOFTWARE IMPLEMENTATION), p. 3 (III. NMPC APPROACH), p. 4 (IV. SOFTWARE IMPLEMENTATION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 3 (III. NMPC APPROACH), p. 4 (IV. SOFTWARE IMPLEMENTATION), p. 3 (III. NMPC APPROACH), p. 4 (IV. SOFTWARE IMPLEMENTATION), objective p. 3 (IV. SOFTWARE IMPLEMENTATION), p. 3 (III. NMPC APPROACH), p. 4 (IV. SOFTWARE IMPLEMENTATION).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
