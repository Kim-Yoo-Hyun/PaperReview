# Problem - LaViRA: Language-Vision-Robot Actions Translation for Zero-Shot Vision Language Navigation in Continuous Environments

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html; PDF retrieval source: https://arxiv.org/pdf/2510.19655. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): To bridge the gap to the real world, Vision-and-Language Navigation in Continuous Environments (VLN-CE) [2] was introduced, removing the reliance on connectivity graphs and forcing agents to contend

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Zero-shot Vision-and-Language Navigation in Continuous Environments (VLN-CE) requires an agent to navigate unseen environments based on natural language instructions without any prior training.
- **p. 1 / Abstract - extractive body cue:** Current methods face a critical trade-off: either rely on environment-specific waypoint predictors that limit scene generalization, or underutilize the reasoning capabilities of large models during ...
- **p. 1 / Abstract - extractive body cue:** We introduce LaViRA, a simple yet effective zero-shot framework that addresses this dilemma by decomposing action into a coarse-to-fine hierarchy: Language Action for high-level planning, ...
- **p. 1 / Abstract - extractive body cue:** This modular decomposition allows us to leverage the distinct strengths of different scales of Multimodal Large Language Models (MLLMs) at each stage, creating a system ...
- **p. 1 / Abstract - extractive body cue:** LaViRA significantly outperforms existing state-of-the-art methods on the VLN-CE benchmark, demonstrating superior generalization capabilities in unseen environments, while maintaining transparency and efficiency for real-world deployment.
- **p. 1 / I. INTRODUCTION - extractive body cue:** To bridge the gap to the real world, Vision-and-Language Navigation in Continuous Environments (VLN-CE) [2] was introduced, removing the reliance on connectivity graphs and forcing ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Vision-and-Language Navigation (VLN) presents the challenge of grounding natural language instructions within visual observations to enable an embodied agent to navigate through previously unseen environments ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | To bridge the gap to the real world, Vision-and-Language Navigation in Continuous Environments (VLN-CE) [2] was introduced, removing the reliance on connectivity ... | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | Specifically, the model receives three types of input: • Language Instruction I: The given natural language instruction provided at the start of ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF body |
| State / latent | Specifically, model, receives, three, types, input, Language, Instruction, given, natural | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | model, prompted, Language, Instruction, original, Progress, Estimation, text | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: Specifically, model, receives, three, types, input, Language, Instruction, given, natural | p. 3 (III. PROPOSED METHOD), p. 2 (I. INTRODUCTION), p. 4 (III. PROPOSED METHOD) |
| Decision / output variable | path/waypoint/velocity; body terms: contributions, follows, general, action, decomposition, strategy, zero-shot, VLN-CE | p. 2 (I. INTRODUCTION), p. 3 (III. PROPOSED METHOD), p. 3 (III. PROPOSED METHOD) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: explicit, reasoning, step, forces, model, track, progress, against | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (III. PROPOSED METHOD), p. 4 (III. PROPOSED METHOD), p. 4 (III. PROPOSED METHOD) |
| Success / guarantee | goal reach with collision-free execution | p. 5 (IV. SIMULATION EXPERIMENTS), p. 6 (IV. SIMULATION EXPERIMENTS), p. 6 (IV. SIMULATION EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** Vision-and-Language Navigation (VLN) presents the challenge of grounding natural language instructions within visual observations to enable an embodied agent to navigate through previously unseen environments ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** grounded but lack dynamic, high-level reasoning during navigation.
- **p. 2 / I. INTRODUCTION - extractive body cue:** 1) Language Action: A powerful MLLM acts as a highlevel planner, analyzing the instruction, history, and current observation to produce a coarse strategic decision, such ...

## What the Paper Changes

PDF body contribution framing (p. 2 (I. INTRODUCTION), p. 3 (III. PROPOSED METHOD), p. 3 (III. PROPOSED METHOD)): Our contributions are as follows: • We propose a general action decomposition strategy for zero-shot VLN-CE that separates navigation into language-level planning, vision-level grounding, and robot-level control, enabling flexible integ ...

- **p. 3 / III. PROPOSED METHOD - extractive body cue:** Language Action: High-Level Planning The first stage of our framework addresses the question: Where should I generally go next?
- **p. 3 / III. PROPOSED METHOD - extractive body cue:** To address this, our method decomposes the navigation process into a sequence of three hierarchical actions: a high-level directional plan (Language Action), the grounding of ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | Its performance ceiling is bounded by off-the-shelf models, as seen in failures on ambiguous instructions and large-area grounding. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | (Right) Failure cases visualization: Language Action misjudges direction due to ambiguous instructions; Vision Action selects the wrong region ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Qualitative Analysis To offer qualitative insights into LaViRA's decisionmaking, Figure 4 shows a successful navigation run and common ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | The failure cases illustrate three common errors: (1) A Language Action error from ambiguous instructions, e.g., failing to ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (III. PROPOSED METHOD), p. 2 (I. INTRODUCTION), p. 4 (III. PROPOSED METHOD), p. 2 (I. INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 3 (III. PROPOSED METHOD), p. 2 (I. INTRODUCTION), p. 4 (III. PROPOSED METHOD), p. 2 (I. INTRODUCTION), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
