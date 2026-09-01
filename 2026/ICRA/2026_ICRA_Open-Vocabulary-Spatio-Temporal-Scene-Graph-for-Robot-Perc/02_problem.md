# Problem - Open-Vocabulary Spatio-Temporal Scene Graph for Robot Perception and Teleoperation Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_5.html; PDF retrieval source: https://arxiv.org/pdf/2509.23107. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): Taken together, these challenges reveal a fundamental gap: latency distorts the temporal alignment between operator intent and robot execution, while static representations fail to capture evolving events or filter redundant ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Teleoperation via natural-language reduces operator workload and enhances safety in high-risk or remote settings.
- **p. 1 / Abstract - extractive body cue:** However, in dynamic remote scenes, transmission latency during bidirectional communication creates gaps between remote perceived states and operator intent, leading to command misunderstanding and incorrect ...
- **p. 1 / Abstract - extractive body cue:** To mitigate this, we introduce the Spatio-Temporal Open-Vocabulary Scene Graph (ST-OVSG), a representation that enriches openvocabulary perception with temporal dynamics and lightweight latency annotations.
- **p. 1 / Abstract - extractive body cue:** ST-OVSG leverages LVLMs to construct open-vocabulary 3D object representations, and extends them into the temporal domain via Hungarian assignment with our temporal matching cost, yielding ...
- **p. 1 / Abstract - extractive body cue:** A latency tag is embedded to enable LVLM planners to retrospectively query past scene states, thereby resolving local-remote state mismatches caused by transmission delays.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Taken together, these challenges reveal a fundamental gap: latency distorts the temporal alignment between operator intent and robot execution, while static representations fail to capture ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, directly applying these models to teleoperation robotics still faces several challenges.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Taken together, these challenges reveal a fundamental gap: latency distorts the temporal alignment between operator intent and robot execution, while static representations ... | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | The planner outputs a sequence of high-level actions π = (a1, . . . , aM) with grounded arguments (e.g., centroids and ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF |
| State / latent | planner, outputs, sequence, high-level, actions, grounded, arguments, centroids, sizes, parsed | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | Problem, Formulation, construct, temporally, indexed, semantically, enriched, representation | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: planner, outputs, sequence, high-level, actions, grounded, arguments, centroids, sizes, parsed | p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 2 (III. METHODOLOGY) |
| Decision / output variable | path/waypoint/velocity; body terms: main, contributions, summarized, follows, ST-OVSG, novel, spatio-temporal, openvocabulary | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHODOLOGY) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: However, when, multiple, candidate, pairs, overlap, ambiguous, resolve | p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY) |
| Success / guarantee | goal reach with collision-free execution | p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** However, directly applying these models to teleoperation robotics still faces several challenges.
- **p. 1 / I. INTRODUCTION - extractive body cue:** The second challenge is the static nature of current scene representations.

## What the Paper Changes

PDF contribution framing (p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY)): The main contributions of this work can be summarized as follows: 1) We propose ST-OVSG, a novel spatio-temporal openvocabulary scene graph, which explicitly models both the spatial structure and temporal ...

- **p. 2 / I. INTRODUCTION - extractive body cue:** To address this, we propose Spatio-Temporal OpenVocabulary Scene Graph (ST-OVSG), an open-vocabulary spatio-temporal scene graph designed for teleoperation.
- **p. 3 / III. METHODOLOGY - extractive body cue:** To address this, we propose ST-OVSG that integrates object nodes, spatial relations, and temporal correspondences.
- **p. 3 / III. METHODOLOGY - extractive body cue:** Formally, the challenge is to maintain a representation that allows the system to (i) recover the scene as it existed at the command-issue time, (ii) ...
- **p. 4 / III. METHODOLOGY - extractive body cue:** This allows the planner to interpret userissued commands with respect to the scene state observed by the operator.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | Failure cases were dominated by residual identity switches under long occlusions, missed detections of small or subtle objects, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | In practice, many predicted actions were semantically correct but expressed with different phrasing or level of detail, which ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Because our representation is designed for openvocabulary settings, automated evaluation of nodes and edges is unreliable: object categories ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Motion blur, viewpoint shifts, and occlusions destabilize open-vocabulary detections. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 2 (III. METHODOLOGY), p. 1 (I. INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), interface p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 2 (III. METHODOLOGY), p. 1 (I. INTRODUCTION), objective p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
