# Problem - ImagineNav: Prompting Vision-Language Models as Embodied Navigator through Scene Imagination

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=vQFw9ryKyK; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/114907. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 3 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION)): However, one limitation of LLMs is their difficulty in embedding the robot's state directly into the planning process.

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive body cue:** Visual navigation is an essential skill for home-assistance robots, providing the object-searching ability to accomplish long-horizon daily tasks.
- **p. 1 / ABSTRACT - extractive body cue:** Many recent approaches use Large Language Models (LLMs) for commonsense inference to improve exploration efficiency.
- **p. 1 / ABSTRACT - extractive body cue:** However, the planning process of LLMs is limited within texts and it is difficult to represent the spatial occupancy and geometry layout only by texts.
- **p. 1 / ABSTRACT - extractive body cue:** Both are important for making rational navigation decisions.
- **p. 1 / ABSTRACT - extractive body cue:** In this work, we seek to unleash the spatial perception and planning ability of VisionLanguage Models (VLMs), and explore whether the VLM, with only on-board ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** However, one limitation of LLMs is their difficulty in embedding the robot's state directly into the planning process.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Although such a pipeline achieves great success in recent years (Zhou et al., 2023; Kuang et al., 2024; Wu et al., 2024b; Zhang et al., ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, one limitation of LLMs is their difficulty in embedding the robot's state directly into the planning process. | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | As illustrated in Figure 3, the VLM receives the synthesized observations at future navigation waypoints and the navigation goal as inputs. | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF body |
| State / latent | illustrated, Figure, VLM, receives, synthesized, observations, future, navigation, waypoints, goal | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | Subsequently, system, executes, PointNav, policy, determine, next, navigational | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: illustrated, Figure, VLM, receives, synthesized, observations, future, navigation, waypoints, goal | p. 5 (3 METHODOLOGY), p. 3 (1 INTRODUCTION), p. 4 (3 METHODOLOGY) |
| Decision / output variable | path/waypoint/velocity; body terms: summary, contributions, mapless, navigation, ImagineNav, provide, detailed, ablation | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: Compared, larger, models, GPT-4o, GPT-4o-mini, lightweight, cost-effective, providing | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 6 (3 METHODOLOGY) |
| Success / guarantee | goal reach with collision-free execution | p. 6 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 INTRODUCTION - extractive body cue:** Although such a pipeline achieves great success in recent years (Zhou et al., 2023; Kuang et al., 2024; Wu et al., 2024b; Zhang et al., ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** As most VLMs cannot understand the continuous physical world, it is infeasible to directly ask VLMs to generate navigable 3D waypoints.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Thirdly, although the semantic information stored on the map can be easily expressed by text (e.g., list the categories of the observed objects), such pure ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Although previous works (Yadav et al., 2022; Ramrakhya et al., 2023; Chaplot et al., 2020; Ramakrishnan et al., 2022) can achieve high success rate in ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 4 (3 METHODOLOGY), p. 5 (3 METHODOLOGY)): In summary, our contributions are: • We propose a mapless navigation approach ImagineNav.

- **p. 2 / 1 INTRODUCTION - extractive body cue:** We also provide a detailed ablation analysis to help understand the important conclusions in our framework.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** We propose a new decision-making paradigm based on imagined imagery, wherein decisions are made on imaginations, enabling more nuanced, context-aware interactions that better harness VLMs' ...
- **p. 4 / 3 METHODOLOGY - extractive body cue:** The discrete action space consists of the following commands: {Stop, MoveAhead, TurnLeft, TurnRight, LookUp, LookDown}.
- **p. 5 / 3 METHODOLOGY - extractive body cue:** 3.2 FUTURE-VIEW IMAGINATION To better leverage the spatial perception and reasoning capabilities of VLMs for open-vocabulary object navigation in unknown environments, we propose an future-view ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | We also present some failure examples at the bottom of Figure 8 | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | We identified three key factors contributing to these navigation failures. | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | First, some object instances are neglected for marking by the simulator, and therefore a successfully trajectory is wrongly ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | Moving forward, we aim to enhance the quality of viewpoint generation and optimize the use of historical memory ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 5 (3 METHODOLOGY), p. 3 (1 INTRODUCTION), p. 4 (3 METHODOLOGY), p. 4 (3 METHODOLOGY). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 3 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), interface p. 5 (3 METHODOLOGY), p. 3 (1 INTRODUCTION), p. 4 (3 METHODOLOGY), p. 4 (3 METHODOLOGY), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
