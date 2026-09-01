# Problem - Dynamic Safety in Complex Environments: Synthesizing Safety Filters with Poisson's Equation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (16 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p137.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p137.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. IyrRopUCTION), p. 3 (B. Ouputs and Relative Degree), p. 4 (A. Direct Assignment), p. 4 (A. Direct Assignment), p. 1 (Abstract)): which present challenges in synthesizing safe controllers.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Synthesizing safe sets for robotic systems oper ating in complex and dynamically changing environments is fa challenging. problem.
- **p. 1 / Abstract - extractive PDF cue:** Solving this problem can enable the construction of safety filters that guarantee safe control actions- ‘most notably by employing Control Barrier Functions (CBFS).
- **p. 1 / Abstract - extractive PDF cue:** This paper presents an algorithm for generating safe sets from perception data by leveraging elliptic partial differential equations, specifically Poisson's equation.
- **p. 1 / Abstract - extractive PDF cue:** Given a local occupancy ‘map, we solve Poisson's equation subject to Dirichlet boundary ‘a novel forcing function.
- **p. 1 / Abstract - extractive PDF cue:** Specifically, we design a smooth guidance vector field, which encodes gradient information required for safety.
- **p. 1 / 1. IyrRopUCTION - extractive PDF cue:** which present challenges in synthesizing safe controllers.
- **p. 3 / B. Ouputs and Relative Degree - extractive PDF cue:** In what follows, we demonstrate how Poisson's equation can be leveraged to overcome these challenges and generate a single smooth function /: for environments with ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | which present challenges in synthesizing safe controllers. | high-DoF humanoid whole-body dynamics와 contacts | body wording is the source claim |
| Observation / input | We focus on systems defined by integrator chains as (10), with the input appearing at the last layer-note that our method can ... | proprioception, reference pose/motion, visual or language command | exact sensor/frame/preprocessing from PDF |
| State / latent | focus, systems, defined, integrator, chains, input, appearing, last, layer-note, extended | whole-body pose, balance/contact state와 skill/mode | notation and tensor shape require body check |
| Output / action | where, state, control, input, function, denotes, drift, dynamics | joint/whole-body action, motion target 또는 task trajectory | exact unit/frame/decoder require body check |
| Target outcome | motion/task success and recovery | tracking, balance, skill/task success와 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | whole-body pose/contact/reference state; body terms: focus, systems, defined, integrator, chains, input, appearing, last, layer-note, extended | p. 6 (B. Indirect Assignment - Variational Approach), p. 1 (1. IyrRopUCTION), p. 2 (1. IyrRopUCTION) |
| Decision / output variable | joint/whole-body action; body terms: main, contributions, threefold, present, constructive, generating, safe, sets | p. 2 (1. IyrRopUCTION), p. 6 (B. Indirect Assignment - Variational Approach), p. 6 (B. Indirect Assignment - Variational Approach) |
| Objective / loss / cost | tracking/balance/task objective; cue terms: Specifically, minimizer, cost, functional, twice, differentiable, satisfies, associated | p. 4 (IV. FORCING FUNCTION CONSTRUCTION), p. 5 (B. Indirect Assignment - Variational Approach), p. 5 (B. Indirect Assignment - Variational Approach), p. 6 (B. Indirect Assignment - Variational Approach), p. 6 (B. Indirect Assignment - Variational Approach) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (IV. FORCING FUNCTION CONSTRUCTION), p. 6 (B. Indirect Assignment - Variational Approach), p. 6 (B. Indirect Assignment - Variational Approach) |
| Success / guarantee | motion/task success and recovery | p. 8 (B. Hardware Experiments), p. 8 (B. Hardware Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 3 / B. Ouputs and Relative Degree - extractive PDF cue:** In what follows, we demonstrate how Poisson's equation can be leveraged to overcome these challenges and generate a single smooth function /: for environments with ...
- **p. 4 / A. Direct Assignment - extractive PDF cue:** This limitation makes this choice of f unsuitable for control design for systems with outputs of relative degree > Las defined in Def.
- **p. 4 / A. Direct Assignment - extractive PDF cue:** Following from Theorem 1, the forcing function (19) yields a safety function h€ C2(O; Roo) that lacks orders of differentiability higher than 2.
- **p. 1 / Abstract - extractive PDF cue:** The result isa variational problem for which sta safety function-characterizes the sale set.

## What the Paper Changes

PDF contribution framing (p. 2 (1. IyrRopUCTION), p. 6 (B. Indirect Assignment - Variational Approach), p. 6 (B. Indirect Assignment - Variational Approach), p. 2 (1. IyrRopUCTION), p. 4 (IV. FORCING FUNCTION CONSTRUCTION)): The main contributions are threefold: (I) we present a constructive way of generating safe sets for complex environments from perception data via Poisson's equation, (2) we illustrate and prove how ...

- **p. 6 / B. Indirect Assignment - Variational Approach - extractive PDF cue:** However. the condition V-v(y) <0 may not necessarily hold for all y < ©, which is sufficient to guarantee h(y) > 0 in 2. ‘To ...
- **p. 6 / B. Indirect Assignment - Variational Approach - extractive PDF cue:** We focus on systems defined by integrator chains as (10), with the input appearing at the last layer-note that our method can be extended to ...
- **p. 2 / 1. IyrRopUCTION - extractive PDF cue:** We propose several methods for constructing the forcing function within Poisson's equation, including an average flux method and a guidance field method {26} that provides ...
- **p. 4 / IV. FORCING FUNCTION CONSTRUCTION - extractive PDF cue:** In this section, we present methods of designing forcing functions that ensure the solution to the boundary value problem for Poisson's equation (16) is a ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | ‘A fundamental limitation of the proposed algorithm (and a limitation of all non-predictive safety filters) is that such ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Simulations: Double Integrator We define a 2D occupancy map defined by an open, bounded and connected domain © ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | From these results, itis clear thatthe Poisson safety funetion enabled collision avoidance without hindering the nominal objective. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | ‘To demonstrate the practical performance of our proposed algorithm in synthesizing safe sets, we applied it to several ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

humanoid writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 6 (B. Indirect Assignment - Variational Approach), p. 1 (1. IyrRopUCTION), p. 2 (1. IyrRopUCTION), p. 3 (B. Ouputs and Relative Degree). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. IyrRopUCTION), p. 3 (B. Ouputs and Relative Degree), p. 4 (A. Direct Assignment), p. 4 (A. Direct Assignment), p. 1 (Abstract), interface p. 6 (B. Indirect Assignment - Variational Approach), p. 1 (1. IyrRopUCTION), p. 2 (1. IyrRopUCTION), p. 3 (B. Ouputs and Relative Degree), objective p. 4 (IV. FORCING FUNCTION CONSTRUCTION), p. 5 (B. Indirect Assignment - Variational Approach), p. 5 (B. Indirect Assignment - Variational Approach), p. 6 (B. Indirect Assignment - Variational Approach), p. 6 (B. Indirect Assignment - Variational Approach).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
