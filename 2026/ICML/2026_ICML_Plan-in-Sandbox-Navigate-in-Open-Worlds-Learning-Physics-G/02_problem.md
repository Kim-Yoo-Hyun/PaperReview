# Problem - Plan in Sandbox, Navigate in Open Worlds: Learning Physics-Grounded Abstracted Experience for Embodied Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (28 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=W5e8c9nwNo; PDF retrieval source: https://openreview.net/pdf/27299763732e881621b2b6f37e47e47722f2e575.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 3 (2. Problem Formulation)): In summary, the key contributions of our work are: • We introduce a novel Generative Experience-Driven Learning paradigm to address the severe data scarcity and real-world transfer challenges in embodied ...

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Vision-Language Models (VLMs) have demonstrated exceptional general reasoning capabilities.
- **p. 1 / Abstract - extractive PDF cue:** However, their performance in embodied navigation remains hindered by a scarcity of aligned open-world vision and robot control data.
- **p. 1 / Abstract - extractive PDF cue:** Despite simulators providing a cost-effective alternative for data collection, the inherent reliance on photorealistic simulations often limits the transferability of learned policies.
- **p. 1 / Abstract - extractive PDF cue:** To this end, we propose Sandbox-Abstracted Grounded Experience (SAGE), a framework that enables agents to learn within a physics-grounded semantic abstraction rather than a photorealistic ...
- **p. 1 / Abstract - extractive PDF cue:** SAGE system operates via three synergistic phases: (1) Genesis: constructing diverse, physics-constrained semantic environments to bootstrap experience; (2) Evolution: distilling experiences through Reinforcement Learning (RL), ...
- **p. 2 / 1. Introduction - extractive PDF cue:** In summary, the key contributions of our work are: • We introduce a novel Generative Experience-Driven Learning paradigm to address the severe data scarcity and ...
- **p. 1 / 1. Introduction - extractive PDF cue:** However, fully unleashing the potential of VLMs within embodied environments remains fraught with challenges.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | In summary, the key contributions of our work are: • We introduce a novel Generative Experience-Driven Learning paradigm to address the severe ... | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | A represents the agent's action space, which we decompose into the selection of discrete intermediate observations and their corresponding navigable waypoints. | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF |
| State / latent | represents, agent, action, space, decompose, selection, discrete, intermediate, observations, corresponding | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | Physics-Grounded, Sandbox, Optimized, Policy, Hybrid, Sampling, Observations, Augmented | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: represents, agent, action, space, decompose, selection, discrete, intermediate, observations, corresponding | p. 3 (2.1. Physics-Grounded Interaction Sandbox), p. 3 (2.3. Navigation Task), p. 2 (1. Introduction) |
| Decision / output variable | path/waypoint/velocity; body terms: summary, contributions, introduce, novel, Generative, Experience-Driven, Learning, paradigm | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (2.3. Navigation Task) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: within, abstracted, sandbox, agent, progressively, acquires, robust, priors | p. 3 (2.3. Navigation Task), p. 3 (2. Problem Formulation) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (2.3. Navigation Task), p. 3 (2.3. Navigation Task) |
| Success / guarantee | goal reach with collision-free execution | p. 6 (4.1. Experimental Settings), p. 6 (4.1. Experimental Settings), p. 7 (4.3. Analysis on Sandbox Data) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive PDF cue:** However, fully unleashing the potential of VLMs within embodied environments remains fraught with challenges.
- **p. 2 / 1. Introduction - extractive PDF cue:** Simulator Env Frontier Node Memory Node Sandbox Open-world Experience Question Observation w/ exp Optimized Policy 1 2 1 2 3 Frontier 2 3 2 Memory ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Specifically, the huge modality gap between the semantic reasoning space of VLMs and the continuous actuation space of robots often renders learned policies brittle.
- **p. 3 / 2. Problem Formulation - extractive PDF cue:** Our objective is to bridge the gap between the unsupervised sandbox S and the high-level navigation task N by maximizing a surrogate objective over O.

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (2.3. Navigation Task), p. 1 (1. Introduction), p. 3 (2.3. Navigation Task)): In summary, the key contributions of our work are: • We introduce a novel Generative Experience-Driven Learning paradigm to address the severe data scarcity and real-world transfer challenges in embodied ...

- **p. 2 / 1. Introduction - extractive PDF cue:** Instead of relying on difficult exploration in the real world, we propose operating the VLM within a physics-grounded sandbox to synthesize diverse tasks and proactively ...
- **p. 3 / 2.3. Navigation Task - extractive PDF cue:** To address this, we propose approximating the optimal behavior by maximizing a surrogate objective Jϕ(θ) within the sandbox task distribution O.
- **p. 1 / 1. Introduction - extractive PDF cue:** Motivated by these strides, the research community has increasingly focused on developing general-purpose embodied navigation agents.
- **p. 3 / 2.3. Navigation Task - extractive PDF cue:** Intuitively, the core objective is to optimize the policy against the synthesized experiences: Jϕ(θ) = E o∼O, at∼πθ(·/st,o), st+1∼P(·/st,at) "X t=0 γtrϕ(st, at, o) # ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | (15) In cases of navigation failure, the agent defaults to blind guessing; the contribution to SPL† is set ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 17 | Figure 7. Visualization of the word cloud. rules using regular expressions. The entire trajectory is discarded if the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Furthermore, we demonstrate the system's practical robustness via Real-World Deployment in Appendix J. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | All experiments use the model with 2B parameters on A-EQA. ing complementary environments during the Genesis phase, the ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (2.1. Physics-Grounded Interaction Sandbox), p. 3 (2.3. Navigation Task), p. 2 (1. Introduction), p. 2 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 3 (2. Problem Formulation), interface p. 3 (2.1. Physics-Grounded Interaction Sandbox), p. 3 (2.3. Navigation Task), p. 2 (1. Introduction), p. 2 (1. Introduction), objective p. 3 (2.3. Navigation Task), p. 3 (2. Problem Formulation).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
