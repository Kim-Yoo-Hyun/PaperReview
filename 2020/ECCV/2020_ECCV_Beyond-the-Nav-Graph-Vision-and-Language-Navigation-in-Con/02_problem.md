# Problem - Beyond the Nav-Graph: Vision-and-Language Navigation in Continuous Environments

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2004.02857; PDF retrieval source: https://arxiv.org/pdf/2004.02857. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 3 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction)): However, these techniques are each independently far from perfect and such an agent would need to learn the limitations of these lowerlevel control systems - facing consequences when proposed waypoints ...

## PDF Body Digest

- **p. 1 / 1 Introduction - extractive PDF cue:** Springing forth from the pages of science fiction and capturing the daydreams of weary chore-doers everywhere, the promise and potential of general-purpose robotic assistants that ...
- **p. 1 / 1 Introduction - extractive PDF cue:** Taking a small step towards this goal, recent work has begun developing artificial agents that follow natural language navigation instructions in perceptually-rich, simulated environments [4,6].
- **p. 1 / 1 Introduction - extractive PDF cue:** An example instruction might be "Go down the hall and turn left at the wooden desk.
- **p. 1 / 1 Introduction - extractive PDF cue:** Continue until you reach the kitchen and then stop by the kettle." and agents are evaluated by their ability to follow the described path in ...
- **p. 1 / 1 Introduction - extractive PDF cue:** Many of these tasks have been developed from datasets of panoramic images captured in real scenes - e.g.
- **p. 3 / 1 Introduction - extractive PDF cue:** However, these techniques are each independently far from perfect and such an agent would need to learn the limitations of these lowerlevel control systems - ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Taken together, these assumptions make current settings poor reflections of the real world both in terms of control (ignoring actuation, navigation, and localization error) and ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, these techniques are each independently far from perfect and such an agent would need to learn the limitations of these lowerlevel ... | defined robot simulator/hardware task suite | body wording is the source claim |
| Observation / input | Our VLN-CE setting (b) lifts these assumptions by instantiating the task in continuous environments with low-level actions - providing a more realistic ... | standardized observation, action, task state와 evaluation split | exact sensor/frame/preprocessing from PDF |
| State / latent | VLN-CE, setting, lifts, assumptions, instantiating, task, continuous, environments, low-level, actions | benchmark state/goal와 method decision | notation and tensor shape require body check |
| Output / action | Taking, small, step, towards, goal, recent, begun, developing | policy/controller trajectory 또는 measured result | exact unit/frame/decoder require body check |
| Target outcome | comparable score and protocol validity | success metric, robustness, generalization과 reproducibility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | standardized episode e and interface; body terms: VLN-CE, setting, lifts, assumptions, instantiating, task, continuous, environments, low-level, actions | p. 2 (1 Introduction), p. 3 (1 Introduction), p. 1 (1 Introduction) |
| Decision / output variable | method trajectory/action; body terms: develop, continuous, setting, enables, types, studies, take, first | p. 3 (1 Introduction), p. 1 (1 Introduction), p. 4 (1 Introduction) |
| Objective / loss / cost | benchmark score and failure cost; cue terms: How, actual, agent, might, acquire, update, topology, environments | p. 2 (1 Introduction) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (1 Introduction), p. 4 (1 Introduction) |
| Success / guarantee | comparable score and protocol validity | p. 11 (5 Experiments), p. 11 (5 Experiments), p. 12 (5 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive PDF cue:** Taken together, these assumptions make current settings poor reflections of the real world both in terms of control (ignoring actuation, navigation, and localization error) and ...
- **p. 3 / 1 Introduction - extractive PDF cue:** This setting introduces many challenges ignored in prior work.
- **p. 2 / 1 Introduction - extractive PDF cue:** However, precise localization indoors is still a challenging problem.
- **p. 4 / 1 Introduction - extractive PDF cue:** We find significant gaps in performance between these settings indicative of the strong prior provided by the nav-graph.

## What the Paper Changes

PDF contribution framing (p. 3 (1 Introduction), p. 1 (1 Introduction), p. 4 (1 Introduction), p. 1 (1 Introduction), p. 3 (1 Introduction)): In this work, we develop a continuous setting that enables these types of studies and take a first step towards integrating VLN agents with control via low-level actions.

- **p. 1 / 1 Introduction - extractive PDF cue:** This paradigm enables efficient data collection and high visual fidelity compared to 3D scanning or creating synthetic environments; however, scenes are only observed from a ...
- **p. 4 / 1 Introduction - extractive PDF cue:** To summarize our contributions, we: - Lift the VLN task to continuous 3D environments - removing many unrealistic assumptions imposed by the nav-graph-based representation.
- **p. 1 / 1 Introduction - extractive PDF cue:** Many of these tasks have been developed from datasets of panoramic images captured in real scenes - e.g.
- **p. 3 / 1 Introduction - extractive PDF cue:** We develop agent architectures for this task and explore how popular mechanisms for VLN transfer to the VLN-CE setting.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 14 | The second example shows a failure of the agent - it navigates towards the wrong windows and fails ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 14 | We also observe failures when the agent never sees the object(s) referred to by the instruction in the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 15 | In models presented here, we took an approach where observations were mapped directly to low-level control in an ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 12 | We believe that depth enable agents to quickly begin traversing environments effectively (e.g. without collisions) and without this ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

benchmark writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (1 Introduction), p. 3 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 3 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction), interface p. 2 (1 Introduction), p. 3 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction), objective p. 2 (1 Introduction).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
