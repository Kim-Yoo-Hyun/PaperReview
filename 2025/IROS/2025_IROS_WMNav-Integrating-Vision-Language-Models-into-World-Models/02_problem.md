# Problem - WMNav: Integrating Vision-Language Models into World Models for Object Goal Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2503.02247; PDF retrieval source: https://arxiv.org/pdf/2503.02247. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): However, due to the limited field of view of egocentric images, capturing environmental information outside the immediate perspective remains a significant challenge.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Object Goal Navigation--requiring an agent to locate a specific object in an unseen environment--remains a core challenge in embodied AI.
- **p. 1 / Abstract - extractive body cue:** Although recent progress in Vision-Language Model (VLM)--based agents has demonstrated promising perception and decision-making abilities through prompting, none has yet established a fully modular world ...
- **p. 1 / Abstract - extractive body cue:** We introduce WMNav, a novel World Model-based Navigation framework powered by Vision-Language Models (VLMs).
- **p. 1 / Abstract - extractive body cue:** It predicts possible outcomes of decisions and builds memories to provide feedback to the policy module.
- **p. 1 / Abstract - extractive body cue:** To retain the predicted state of the environment, WMNav proposes the online maintained Curiosity Value Map as part of the world model memory to provide ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, due to the limited field of view of egocentric images, capturing environmental information outside the immediate perspective remains a significant challenge.
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, the true challenge lies in creating a versatile world model that can faithfully capture the landscape of an indoor environment.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, due to the limited field of view of egocentric images, capturing environmental information outside the immediate perspective remains a significant challenge. | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | Our contributions can be summarized as follows: • We introduce a new direction for object goal navigation in a complex, unknown environment ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF body |
| State / latent | contributions, summarized, follows, introduce, direction, object, goal, navigation, complex, unknown | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | PlanVLM, ReasonVLM, policy, module, cost, previous, step, subtask | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: contributions, summarized, follows, introduce, direction, object, goal, navigation, complex, unknown | p. 2 (I. INTRODUCTION), p. 5 (III. WMNAV APPROACH), p. 3 (III. WMNAV APPROACH) |
| Decision / output variable | path/waypoint/velocity; body terms: contributions, summarized, follows, introduce, direction, object, goal, navigation | p. 2 (I. INTRODUCTION), p. 3 (III. WMNAV APPROACH), p. 2 (I. INTRODUCTION) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: Then, Figure, updated, combining, curiosity, value, previous, step | p. 5 (III. WMNAV APPROACH), p. 4 (III. WMNAV APPROACH), p. 4 (III. WMNAV APPROACH), p. 5 (III. WMNAV APPROACH) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (III. WMNAV APPROACH), p. 5 (III. WMNAV APPROACH), p. 5 (III. WMNAV APPROACH) |
| Success / guarantee | goal reach with collision-free execution | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 3 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / I. INTRODUCTION - extractive body cue:** However, the true challenge lies in creating a versatile world model that can faithfully capture the landscape of an indoor environment.
- **p. 1 / I. INTRODUCTION - extractive body cue:** The primary difficulty in ZSON stems from the need to employ broad semantic knowledge to direct movement with optimal efficiency while precisely identifying previously unencountered ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Still, it uses BLIP-2[15], which pays more attention to the relevance of image-text pairs and has limited interaction and reasoning capabilities, which makes it difficult ...

## What the Paper Changes

PDF body contribution framing (p. 2 (I. INTRODUCTION), p. 3 (III. WMNAV APPROACH), p. 2 (I. INTRODUCTION), p. 3 (III. WMNAV APPROACH)): Our contributions can be summarized as follows: • We introduce a new direction for object goal navigation in a complex, unknown environment using a world model consisting of VLMs and ...

- **p. 3 / III. WMNAV APPROACH - extractive body cue:** In our framework, the world model consists of PredictVLM and the memory constructed by curiosity value map and cost.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Building on the key insight that VLMs inherently encode comprehensive knowledge about indoor layout and spatial relationships of objects, we propose WMNav as shown in ...
- **p. 3 / III. WMNAV APPROACH - extractive body cue:** To guide the VLM to make reasonable predictions about the indoor scene, we design a novel prompting strategy as illustrated in Figure 3 (a).

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 5 | If there is no sofa, then return failure message. | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | 2) Goal-approaching Stage: Due to the limitations of the existing VLMs' capability, we do not rely on the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | But textual information cannot accurately describe the spatial relationships in the scene, and it is difficult for LLM ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | However, since VLM is trained on egocentric image data, it does not take advantage of VLM's powerful egocentric ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (I. INTRODUCTION), p. 5 (III. WMNAV APPROACH), p. 3 (III. WMNAV APPROACH), p. 4 (III. WMNAV APPROACH). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 2 (I. INTRODUCTION), p. 5 (III. WMNAV APPROACH), p. 3 (III. WMNAV APPROACH), p. 4 (III. WMNAV APPROACH), objective p. 5 (III. WMNAV APPROACH), p. 4 (III. WMNAV APPROACH), p. 4 (III. WMNAV APPROACH), p. 5 (III. WMNAV APPROACH).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** However, due to the limited field of view of egocentric images, capturing environmental information outside the immediate perspective remains a significant challenge. (p. 1, I. INTRODUCTION).
- **Formulation-changing contribution:** Our contributions can be summarized as follows: • We introduce a new direction for object goal navigation in a complex, unknown environment using a world model consisting of VLMs and ... (p. 2, I. INTRODUCTION).
- **Assumption/failure evidence:** 2) Goal-approaching Stage: Due to the limitations of the existing VLMs' capability, we do not rely on the VLM to estimate the stopping condition directly from the observed image. (p. 5, III. WMNAV APPROACH).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
