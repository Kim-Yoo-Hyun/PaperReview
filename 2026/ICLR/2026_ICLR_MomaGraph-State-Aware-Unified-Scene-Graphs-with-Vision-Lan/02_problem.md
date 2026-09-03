# Problem - MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Models for Embodied Task Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=3eTr9dGwJv; PDF retrieval source: https://openreview.net/pdf/3f888689e829f4172ae97d1dfac5f1b62ddb30c3.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 4 (1 INTRODUCTION)): However, existing scene graphs suffer from notable limitations.

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive body cue:** Mobile manipulators in households must both navigate and manipulate.
- **p. 1 / ABSTRACT - extractive body cue:** This requires a compact, semantically rich scene representation that captures where objects are, how they function, and which parts are actionable.
- **p. 1 / ABSTRACT - extractive body cue:** Scene graphs are a natural choice, yet prior work often separates spatial and functional relations, treats scenes as static snapshots without object states or temporal ...
- **p. 1 / ABSTRACT - extractive body cue:** To address these limitations, we introduce MomaGraph, a unified scene representation for embodied agents that integrates spatial-functional relationships and part-level interactive elements.
- **p. 1 / ABSTRACT - extractive body cue:** However, advancing such a representation requires both suitable data and rigorous evaluation, which have been largely missing.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, existing scene graphs suffer from notable limitations.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** However, when directly used as task planners, VLMs (Huang et al., 2023; 2024; Ahn et al., 2022; Zheng et al., 2025a; Yang et al., 2025) ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, existing scene graphs suffer from notable limitations. | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | In this work, we do not focus on the agent's interaction policy; instead, our emphasis lies on how to capture and incorporate ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF body |
| State / latent | focus, agent, interaction, policy, instead, emphasis, lies, capture, incorporate, observed | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | VLMS, LEARN, SCENE, GRAPH, REPRESENTATIONS, REINFORCEMENT, LEARNING, Existing | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: focus, agent, interaction, policy, instead, emphasis, lies, capture, incorporate, observed | p. 6 (4 METHOD), p. 5 (4 METHOD), p. 5 (4 METHOD) |
| Decision / output variable | path/waypoint/velocity; body terms: summary, makes, following, contributions, MomaGraph, first, scene, graph | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 6 (4 METHOD) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: objective, construct, instruction-conditioned, task-oriented, scene, graph, final, reward | p. 5 (4 METHOD), p. 5 (4 METHOD), p. 6 (4 METHOD), p. 6 (4 METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 19 (A.3 TRAINING CURVE), p. 19 (A.3 TRAINING CURVE), p. 6 (4 METHOD) |
| Success / guarantee | goal reach with collision-free execution | p. 11 (6 EXPERIMENTS), p. 20 (Figure/Table caption), p. 11 (6 EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 3 / 1 INTRODUCTION - extractive body cue:** However, when directly used as task planners, VLMs (Huang et al., 2023; 2024; Ahn et al., 2022; Zheng et al., 2025a; Yang et al., 2025) ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** (3) They lack task relevance, as they fail to emphasize information directly tied to task execution, thereby reducing efficiency and effectiveness.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** However, existing works often focus on a single type of scene graphs.
- **p. 4 / 1 INTRODUCTION - extractive body cue:** To ensure this finding generalizes beyond one specific architecture, we evaluate this comparison across different base models using the same dataset and experimental configurations.

## What the Paper Changes

PDF body contribution framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 6 (4 METHOD), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION)): In summary, our work makes the following key contributions: • We propose MomaGraph, the first scene graph representation that jointly models spatial and functional relationships while incorporating part-level interactive nodes, ...

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To achieve this goal, we present MomaGraph, a novel scene representation specifically designed for embodied agents.
- **p. 6 / 4 METHOD - extractive body cue:** To address these limitations, we introduce MomaGraph-Scenes, the first dataset designed to provide a more comprehensive and task-relevant scene representation.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Unlike prior graph-then-plan methods (Dai et al., 2024; Ekpo et al., 2024) that either assume reliable scene graphs or treat graph construction and planning as ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** To overcome this gap, we propose the Graph-then-Plan strategy, which first generates task-specific scene graphs as an intermediate structured representation before high-level planning.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 11 | Figure 6: Quantitative real-robot evaluation. (a) Environment setup of the real-robot experiment. (b) Failure analysis illustrating success/failure rates ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 11 | This work addresses to the fundamental limitations of existing scene graphs for embodied agents: reliance on a single ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | Figure 2: Direct planning often fails even for strong closed-source models like GPT-5, producing wrong actions or missing ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 20 | Moreover, since the benchmark is formulated as a multi-choice VQA task with clearly defined correct answers, it does ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 6 (4 METHOD), p. 5 (4 METHOD), p. 5 (4 METHOD), p. 3 (1 INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), interface p. 6 (4 METHOD), p. 5 (4 METHOD), p. 5 (4 METHOD), p. 3 (1 INTRODUCTION), objective p. 5 (4 METHOD), p. 5 (4 METHOD), p. 6 (4 METHOD), p. 6 (4 METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (26 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** However, existing scene graphs suffer from notable limitations. (p. 2, 1 INTRODUCTION).
- **Formulation-changing contribution:** In summary, our work makes the following key contributions: • We propose MomaGraph, the first scene graph representation that jointly models spatial and functional relationships while incorporating part-level interactive nodes, ... (p. 2, 1 INTRODUCTION).
- **Assumption/failure evidence:** (b) Failure analysis illustrating success/failure rates across different reasoning stages. (p. 11, 6 EXPERIMENTS).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
