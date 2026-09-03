# Problem - VLMaps: Visual-Language Maps for Robot Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2210.05714; PDF retrieval source: https://arxiv.org/pdf/2210.05714. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): A key aspect of VLMaps is that they are spatial, which enables them to: • Localize spatial goals beyond object-centric ones, e.g., "in between the TV and sofa" or "to ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Grounding language to the visual observations of a navigating agent can be performed using off-the-shelf visuallanguage models pretrained on Internet-scale data (e.g., image captions).
- **p. 1 / Abstract - extractive body cue:** While this is useful for matching images to natural language descriptions of object goals, it remains disjoint from the process of mapping the environment, so ...
- **p. 1 / Abstract - extractive body cue:** To address this problem, we propose VLMaps, a spatial map representation that directly fuses pretrained visual-language features with a 3D reconstruction of the physical world.
- **p. 1 / Abstract - extractive body cue:** VLMaps can be autonomously built from video feed on robots using standard exploration approaches and enables natural language indexing of the map without additional labeled ...
- **p. 1 / Abstract - extractive body cue:** Specifically, when combined with large language models (LLMs), VLMaps can be used to (i) translate natural language commands into a sequence of open-vocabulary navigation goals ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** A key aspect of VLMaps is that they are spatial, which enables them to: • Localize spatial goals beyond object-centric ones, e.g., "in between the ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** VLMaps with different language models as well as a discussion on limitations, which point to areas for future work.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | A key aspect of VLMaps is that they are spatial, which enables them to: • Localize spatial goals beyond object-centric ones, e.g., ... | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | Zero-Shot Spatial Goal Navigation from Language In this section, we describe our approach to long-horizon (spatial) goal navigation, given a set of ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF body |
| State / latent | Zero-Shot, Spatial, Goal, Navigation, Language, section, describe, long-horizon, given, landmark | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | re-purpose, models, mobile, robot, planning, priming, them, several | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: Zero-Shot, Spatial, Goal, Navigation, Language, section, describe, long-horizon, given, landmark | p. 4 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD) |
| Decision / output variable | path/waypoint/velocity; body terms: VLMaps, representation, constructed, off-the-shelf, visual-language, models, VLMs, standard | p. 2 (III. METHOD), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: applying, argmax, operator, along, direction, reshaping, resulting, vector | p. 3 (III. METHOD), p. 3 (III. METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | 본문 anchor 없음 |
| Success / guarantee | goal reach with collision-free execution | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / I. INTRODUCTION - extractive body cue:** VLMaps with different language models as well as a discussion on limitations, which point to areas for future work.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Existing VLM-based solutions generalize to new object goals, but lose the spatial precision of classic geometric maps - is it possible to get the best ...

## What the Paper Changes

PDF body contribution framing (p. 2 (III. METHOD), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHOD)): We propose VLMaps as one such representation, which can be constructed using off-the-shelf visual-language models (VLMs) and standard 3D reconstruction libraries.

- **p. 1 / I. INTRODUCTION - extractive body cue:** Extensive experiments show that using VLMaps enables more effective long-horizon multi-object goal navigation than baseline alternatives, e.g., CoW [12] and LM-Nav [13], and, in particular, ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** A key aspect of VLMaps is that they are spatial, which enables them to: • Localize spatial goals beyond object-centric ones, e.g., "in between the ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** 2: VLMaps enables a robot to perform complex zero-shot spatial goal navigation tasks given natural language commands, without additional data collection or model finetuning.
- **p. 3 / III. METHOD - extractive body cue:** Generating Open-Vocabulary Obstacle Maps Building a VLMap enables us to generate obstacle maps that inherit the open-vocabulary nature of the VLMs used (LSeg and CLIP).

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | We observe that failure cases are caused by: 1) inaccurate depth, which introduces noise during the map creation ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 2 | Fig. 2: VLMaps enables a robot to perform complex zero-shot spatial goal navigation tasks given natural language commands, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | This is because when the drone does not have access to a customized obstacle map, it fails to ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 1 (I. INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), interface p. 4 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 1 (I. INTRODUCTION), objective p. 3 (III. METHOD), p. 3 (III. METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (11 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** A key aspect of VLMaps is that they are spatial, which enables them to: • Localize spatial goals beyond object-centric ones, e.g., "in between the TV and sofa" or "to ... (p. 1, I. INTRODUCTION).
- **Formulation-changing contribution:** Extensive experiments show that using VLMaps enables more effective long-horizon multi-object goal navigation than baseline alternatives, e.g., CoW [12] and LM-Nav [13], and, in particular, excels at enabling spatial open-vocabulary ... (p. 1, I. INTRODUCTION).
- **Assumption/failure evidence:** We observe that failure cases are caused by: 1) inaccurate depth, which introduces noise during the map creation and decreases the landmark indexing accuracy and 2) action noise, which can ... (p. 6, IV. EXPERIMENTS).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
