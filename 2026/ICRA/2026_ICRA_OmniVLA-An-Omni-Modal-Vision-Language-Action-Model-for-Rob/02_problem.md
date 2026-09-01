# Problem - OmniVLA: An Omni-Modal Vision-Language-Action Model for Robot Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html; PDF retrieval source: https://arxiv.org/pdf/2509.19480. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): However, prior work in robot navigation typically trains policies with single modalities based on narrow applications.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Humans can flexibly interpret and compose different goal specifications, such as language instructions, spatial coordinates, or visual references, when navigating to a destination.
- **p. 1 / Abstract - extractive PDF cue:** In contrast, most existing robotic navigation policies are trained on a single modality, limiting their adaptability to real-world scenarios where different forms of goal specification ...
- **p. 1 / Abstract - extractive PDF cue:** In this work, we present a training framework for robotic foundation models that enables omni-modal goal conditioning for vision-based navigation.
- **p. 1 / Abstract - extractive PDF cue:** Our approach leverages a high-capacity vision-language-action (VLA) backbone and trains with three primary goal modalities: 2D poses, egocentric images, and natural language, as well as ...
- **p. 1 / Abstract - extractive PDF cue:** This design not only expands the pool of usable datasets but also encourages the policy to develop richer geometric, semantic, and visual representations.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** However, prior work in robot navigation typically trains policies with single modalities based on narrow applications.
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** Additionally, we address the problem of modality imbalance and scarcity by using modality dropout during training, and modality masking during inference.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, prior work in robot navigation typically trains policies with single modalities based on narrow applications. | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | In this study, we propose a family of Omni-Modal VisionLanguage-Action Models (OmniVLA) for autonomous navigation that can ingest goals expressed in multiple ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF |
| State / latent | study, family, Omni-Modal, VisionLanguage-Action, Models, OmniVLA, autonomous, navigation, ingest, goals | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | state, lattice, motion, planner, then, generate, velocity, commands | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: study, family, Omni-Modal, VisionLanguage-Action, Models, OmniVLA, autonomous, navigation, ingest, goals | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 5 (Method) |
| Decision / output variable | path/waypoint/velocity; body terms: Moreover, allows, user, instruct, robot, multiple, modalities, making | p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 5 (Method) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: Prog, indicate, success, rate, partial, progress, towards, goal | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (Method) |
| Success / guarantee | goal reach with collision-free execution | p. 7 (Figure/Table caption), p. 4 (IV. EXPERIMENTAL SETUP), p. 2 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / I. INTRODUCTION - extractive PDF cue:** Additionally, we address the problem of modality imbalance and scarcity by using modality dropout during training, and modality masking during inference.
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** As a result, our policy exhibits strong generalization and fine-tuning capabilities, following language instructions not seen in the training data, and adapting to completely new ...

## What the Paper Changes

PDF contribution framing (p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 5 (Method), p. 1 (I. INTRODUCTION)): Moreover, our method allows the user to instruct the robot with multiple modalities, making it more user friendly and directly allowing the policy to leverage more than one kind of ...

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** In this study, we propose a family of Omni-Modal VisionLanguage-Action Models (OmniVLA) for autonomous navigation that can ingest goals expressed in multiple modalities, leveraging information ...
- **p. 5 / Method - extractive PDF cue:** To ensure fair comparison with our approach, which relies solely on a single RGB camera without depth or LiDAR, we estimate depth using Depth360 [37] ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** By training on omni-modal goals, we aim to enable stronger and more flexible policies, ultimately acquiring a foundation model that exhibits high adaptability to novel ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 3 | Since existing reannotation approaches cannot account for the large embodiment gap of the BDD-V [29] dataset (an autonomous ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | Since we cannot secure a sufficiently large batch size for some models even on a server with multiple ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | However, NaVILA fails, scoring 0.0 on all metrics, due to a domain gap in prompt style: it requires | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | The smaller OmniVLA variant fails to handle the language instructions due to limited modal capacity. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 5 (Method), p. 2 (I. INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 5 (Method), p. 2 (I. INTRODUCTION), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
