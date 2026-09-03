# Problem - SAGE-Nav: Leveraging LLM Planning and Alignment Fusion for Hierarchical Scene Graph-Guided Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2606.25497; PDF retrieval source: https://arxiv.org/pdf/2606.25497. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): Large Language Models (LLMs) offer this capability through the vast commonsense priors, yet they lack spatial grounding required for navigation.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Object-Goal Navigation (ObjNav) requires embodied agents to autonomously locate specified targets using only egocentric visual observations.
- **p. 1 / Abstract - extractive body cue:** Existing monolithic methods struggle with long-horizon reasoning and generalize poorly to novel environments.
- **p. 1 / Abstract - extractive body cue:** To address these limitations, we propose SAGE-Nav, a novel hierarchical framework that integrates the reasoning capabilities of Large Language Models (LLMs) with dynamic scene graphs.
- **p. 1 / Abstract - extractive body cue:** Crucially, it decouples asynchronous global semantic planning from the high-frequency reactive control loop.
- **p. 1 / Abstract - extractive body cue:** The LLM serves as a global planner, decomposing abstract instructions into a sequence of semantically grounded waypoints.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Large Language Models (LLMs) offer this capability through the vast commonsense priors, yet they lack spatial grounding required for navigation.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This challenge has also motivated recent efforts toward unified embodied navigation paradigms [7], which emphasize the importance of data generation, simulation, evaluation, and policy learning ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Large Language Models (LLMs) offer this capability through the vast commonsense priors, yet they lack spatial grounding required for navigation. | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | Finally, the unified state representation is fed into an attentive Actor-Critic [6] network featuring a two-layer LSTM [40] to maintain temporal coherence ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF body |
| State / latent | Finally, unified, state, representation, attentive, Actor-Critic, network, featuring, two-layer, LSTM | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | Deep, Reinforcement, Learning, DRL, empowered, agents, learn, end-to-end | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: Finally, unified, state, representation, attentive, Actor-Critic, network, featuring, two-layer, LSTM | p. 2 (IV. PROPOSED METHOD), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Decision / output variable | path/waypoint/velocity; body terms: summary, contributions, threefold, SAGE-Nav, hierarchical, navigation, arXiv, Jun | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: Upon, merging, cluster, spatial, visual, attributes, updated, online | p. 2 (IV. PROPOSED METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (IV. PROPOSED METHOD) |
| Success / guarantee | goal reach with collision-free execution | p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** This challenge has also motivated recent efforts toward unified embodied navigation paradigms [7], which emphasize the importance of data generation, simulation, evaluation, and policy learning ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** By leveraging relational graph convolutions, it produces structure-aware embeddings designed to capture both semantic and spatial hierarchies. • We develop the Goal-aware Alignment-Fusion Network (GAFN) ...

## What the Paper Changes

PDF body contribution framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (IV. PROPOSED METHOD)): In summary, the contributions of this work are threefold: • We propose SAGE-Nav, a hierarchical navigation.

- **p. 1 / I. INTRODUCTION - extractive body cue:** In contrast, our method constructs a hierarchical scene graph as an explicit environment prior.
- **p. 2 / I. INTRODUCTION - extractive body cue:** By leveraging relational graph convolutions, it produces structure-aware embeddings designed to capture both semantic and spatial hierarchies. • We develop the Goal-aware Alignment-Fusion Network (GAFN) ...
- **p. 2 / IV. PROPOSED METHOD - extractive body cue:** LLM-Guided Global Planning over Hierarchical Scene Graphs Inspired by recent advances that extend RAG to embodied environments [41, 42], we develop an LLM-driven global planner ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | Limitations We analyze the failure cases (Fig. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | 5), which fall into four categories: (a) Target Visibility Failure, where the agent terminates despite the target (e.g., ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | This performance comprehensively validates the robustness of our hierarchical priors and dynamic scheduling mechanism. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Crucially, leveraging waypoint guidance for hardto-find targets, our method improves both the navigation success rate and overall robustness. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (IV. PROPOSED METHOD), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (IV. PROPOSED METHOD). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 2 (IV. PROPOSED METHOD), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (IV. PROPOSED METHOD), objective p. 2 (IV. PROPOSED METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
