# Problem - LAGEA: Language Guided Embodied Agents for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=watVfFbZGF; PDF retrieval source: https://openreview.net/pdf/28f8573440fbd9bb2ac48d0e31f3573d128fcf46.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction)): Yet converting such priors into reliable learning signals still hinges on reward design, which remains a bottleneck across tasks and scenes.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Robotic manipulation benefits from foundation models that describe goals, but today's agents still lack a principled way to learn from their own mistakes.
- **p. 1 / Abstract - extractive PDF cue:** We ask whether natural language can serve as feedback, an error-reasoning signal that helps embodied agents diagnose what went wrong and correct course.
- **p. 1 / Abstract - extractive PDF cue:** We introduce LAGEA (Language Guided Embodied Agents), a framework that turns episodic, schema-constrained reflections from a vision language model (VLM) into temporally grounded guidance for ...
- **p. 1 / Abstract - extractive PDF cue:** LAGEA summarizes each attempt in concise language, localizes the decisive moments in the trajectory, aligns feedback with visual state in a shared representation, and converts ...
- **p. 1 / Abstract - extractive PDF cue:** This design yields dense signals early when exploration needs direction and gracefully recedes as competence grows.
- **p. 1 / 1. Introduction - extractive PDF cue:** Yet converting such priors into reliable learning signals still hinges on reward design, which remains a bottleneck across tasks and scenes.
- **p. 1 / 1. Introduction - extractive PDF cue:** Learning from mistakes requires detecting failures and causal understanding.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Yet converting such priors into reliable learning signals still hinges on reward design, which remains a bottleneck across tasks and scenes. | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | We project images, instruction text, and feedback with Ei, Et, Ef and use unit-norm embeddings for the current state zt, the goal ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | project, images, instruction, text, feedback, unit-norm, embeddings, current, state, goal | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | Goal, Potential, formed, aligning, current, state, image, instruction | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: project, images, instruction, text, feedback, unit-norm, embeddings, current, state, goal | p. 4 (3.2. Reward Generation), p. 4 (3.1.3. FEEDBACK ALIGNMENT), p. 5 (3.2. Reward Generation) |
| Decision / output variable | action, pose, option or chunk a; body terms: purpose, present, framework, LAGEA, addresses, VLMs, generate, episodic | p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Methodology) |
| Objective / loss / cost | policy/action modeling objective; cue terms: shared, space, place, convert, progress, toward, task, movement | p. 4 (3.1.3. FEEDBACK ALIGNMENT), p. 4 (3.1.3. FEEDBACK ALIGNMENT), p. 3 (3.1.2. KEY FRAME GENERATION) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3.2. Reward Generation), p. 3 (3.1.1. STRUCTURED FEEDBACK), p. 3 (3.1.2. KEY FRAME GENERATION) |
| Success / guarantee | instruction-conditioned task success | p. 15 (Figure/Table caption), p. 7 (4.1.2. RESULTS ON FETCH TASKS), p. 6 (4. Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive PDF cue:** Learning from mistakes requires detecting failures and causal understanding.
- **p. 2 / 1. Introduction - extractive PDF cue:** Our core contributions are: • We present LAGEA, an embodied VLM-RL framework that generates causal episodic feedback which are localized in time to turn failures ...
- **p. 2 / 1. Introduction - extractive PDF cue:** The potential itself blends two agreements: how well the current state matches the instruction-defined goal, and how well the transition aligns with the VLM's diagnosis ...

## What the Paper Changes

PDF contribution framing (p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Methodology), p. 4 (3.1.2. KEY FRAME GENERATION)): For this purpose, we present our framework LAGEA, which addresses this by using VLMs to generate episodic natural-language reflections on a robot's 1 arXiv:2509.23155v3 [cs.RO] 24 Aug 2026

- **p. 2 / 1. Introduction - extractive PDF cue:** Our core contributions are: • We present LAGEA, an embodied VLM-RL framework that generates causal episodic feedback which are localized in time to turn failures ...
- **p. 3 / 3. Methodology - extractive PDF cue:** Our framework overview is given in Figure 1.
- **p. 4 / 3.1.2. KEY FRAME GENERATION - extractive PDF cue:** They are later used in feedback alignment, where each timestep's contribution is scaled by ˆwt so imagefeedback geometry is learned primarily from causal moments, and ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 3 | Figure 1. Overview of LAGEA framework. (a) After each rollout, key-frame selection identifies causal moments and computes per-step ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | This accelerated learning is driven by the dense, corrective signals from our feedback mechanism, which fosters a more ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Alignment enables control-relevant geometry: (a) success/failure logit margin increases over training, (b) policy success accelerates, and (c) BCE/InfoNCE ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 19 | Figure 9. Schema for structured feedback returned by the VLM Example structured feedback is shown for two Meta-World ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (3.2. Reward Generation), p. 4 (3.1.3. FEEDBACK ALIGNMENT), p. 5 (3.2. Reward Generation), p. 1 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 4 (3.2. Reward Generation), p. 4 (3.1.3. FEEDBACK ALIGNMENT), p. 5 (3.2. Reward Generation), p. 1 (1. Introduction), objective p. 4 (3.1.3. FEEDBACK ALIGNMENT), p. 4 (3.1.3. FEEDBACK ALIGNMENT), p. 3 (3.1.2. KEY FRAME GENERATION).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
