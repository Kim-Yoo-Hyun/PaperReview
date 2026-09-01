# Problem - CoA-VLA: Improving Vision-Language-Action Models via Visual-Text Chain-of-Affordance

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction)): However, current approaches often rely heavily on high-level planning or task decomposition by off-the-shelf Large language models(LLMs) or Vision language models (VLMs), limiting models from developing implicit reasoning on their ...

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Robot foundation models, particularly Vision-LanguageAction (VLA) models, have garnered significant attention for their ability to enhance robot policy learning, greatly improving robot's generalization and robustness.
- **p. 1 / Abstract - extractive PDF cue:** OpenAI's recent model, O1, showcased impressive capabilities in solving complex problems by utilizing extensive reasoning chains.
- **p. 1 / Abstract - extractive PDF cue:** This prompts an important question: can robot models achieve better performance in multi-task, complex environments by reviewing prior observations and then providing task-specific reasoning to ...
- **p. 1 / Abstract - extractive PDF cue:** In this paper, we introduce Chain-of-Affordance (CoAVLA), a novel approach to scaling robot models by incorporating reasoning in the format of sequential robot affordances to ...
- **p. 1 / Abstract - extractive PDF cue:** Specifically, we prompt the model to consider the following four types of affordances before taking action: (1) object affordance - what object to manipulate and ...
- **p. 2 / 1. Introduction - extractive PDF cue:** However, current approaches often rely heavily on high-level planning or task decomposition by off-the-shelf Large language models(LLMs) or Vision language models (VLMs), limiting models from ...
- **p. 2 / 1. Introduction - extractive PDF cue:** In this work, we propose Chain-of-Affordance, namely CoA-VLA, a novel perspective on generalizing model reasoning at test-time, and leverage such generated reasoning to facilitate the ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, current approaches often rely heavily on high-level planning or task decomposition by off-the-shelf Large language models(LLMs) or Vision language models (VLMs), ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | Our objective is to learn an intermediate language output z : O ↑G ↓Z that maps observations and task descriptions to affordance ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | objective, learn, intermediate, language, output, maps, observations, task, descriptions, affordance | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | embedding, affordances, directly, visual, input, create, explicit, structure | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: objective, learn, intermediate, language, output, maps, observations, task, descriptions, affordance | p. 3 (4.1. Definition of Chain-of-Affordance), p. 5 (4.1. Definition of Chain-of-Affordance), p. 5 (4.1. Definition of Chain-of-Affordance) |
| Decision / output variable | action, pose, option or chunk a; body terms: Chain-of-Affordance, namely, CoA-VLA, novel, perspective, generalizing, model, reasoning | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (4. Methodology) |
| Objective / loss / cost | policy/action modeling objective; cue terms: objective, learn, intermediate, language, output, maps, observations, task | p. 3 (4.1. Definition of Chain-of-Affordance), p. 4 (4.1. Definition of Chain-of-Affordance), p. 5 (4.1. Definition of Chain-of-Affordance) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (4.1. Definition of Chain-of-Affordance), p. 5 (4.1. Definition of Chain-of-Affordance), p. 5 (4.3. Generating Chain-of-Affordance Data) |
| Success / guarantee | instruction-conditioned task success | p. 8 (5.3. More Experiments), p. 7 (5.2. Evaluation on Simulation), p. 8 (5.3. More Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive PDF cue:** However, current approaches often rely heavily on high-level planning or task decomposition by off-the-shelf Large language models(LLMs) or Vision language models (VLMs), limiting models from ...

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (4. Methodology), p. 4 (4.1. Definition of Chain-of-Affordance), p. 4 (4.1. Definition of Chain-of-Affordance)): In this work, we propose Chain-of-Affordance, namely CoA-VLA, a novel perspective on generalizing model reasoning at test-time, and leverage such generated reasoning to facilitate the policy learning process.

- **p. 2 / 1. Introduction - extractive PDF cue:** Our method leverages visual affordance in robot learning, conceptualizing various actions and interactions with objects or the environment that a robot can perform based on ...
- **p. 3 / 4. Methodology - extractive PDF cue:** In Section 4.2, we present two formats for representing the chain of affordances: a text format and an image format.
- **p. 4 / 4.1. Definition of Chain-of-Affordance - extractive PDF cue:** In our framework, spatial affordance is operationalized as actionable destinations-discrete 2D coordinates representing feasible interaction zones.
- **p. 4 / 4.1. Definition of Chain-of-Affordance - extractive PDF cue:** By employing a dynamic affordance selection mechanism, our method avoids generating redundant affordances at every timestep. object to interact with and where it is located, ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Our approach successfully completed all three scenarios, demonstrating robust collision avoidance and spatial adaptability. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Collision avoidance is essential for safe and effective physical interactions, as improper maneuvers can lead to significant damage ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (4.1. Definition of Chain-of-Affordance), p. 5 (4.1. Definition of Chain-of-Affordance), p. 5 (4.1. Definition of Chain-of-Affordance), p. 2 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. Introduction), interface p. 3 (4.1. Definition of Chain-of-Affordance), p. 5 (4.1. Definition of Chain-of-Affordance), p. 5 (4.1. Definition of Chain-of-Affordance), p. 2 (1. Introduction), objective p. 3 (4.1. Definition of Chain-of-Affordance), p. 4 (4.1. Definition of Chain-of-Affordance), p. 5 (4.1. Definition of Chain-of-Affordance).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
