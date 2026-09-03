# Problem - 3D-VLA: A 3D Vision-Language-Action Generative World Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://icml.cc/virtual/2024/poster/34575; PDF retrieval source: https://icml.cc/virtual/2024/poster/34575. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction)): Another challenge for building such a generative world model lies in the lack of data.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Recent vision-language-action (VLA) models rely on 2D inputs, lacking integration with the broader realm of the 3D physical world.
- **p. 1 / Abstract - extractive body cue:** Furthermore, they perform action prediction by learning a direct mapping from perception to action, neglecting the vast dynamics of the world and the relations between ...
- **p. 1 / Abstract - extractive body cue:** In contrast, human beings are endowed with world models that depict imagination about future scenarios to plan actions accordingly.
- **p. 1 / Abstract - extractive body cue:** To this end, we propose 3D-VLA by introducing a new family of embodied foundation models that seamlessly link 3D perception, reasoning, and action through a ...
- **p. 1 / Abstract - extractive body cue:** Specifically, 3D-VLA is built on top of a 3D-based large language model (LLM), and a set of interaction tokens is introduced to engage with the ...
- **p. 2 / 1. Introduction - extractive body cue:** Another challenge for building such a generative world model lies in the lack of data.
- **p. 1 / 1. Introduction - extractive body cue:** Secondly, existing embodied datasets mainly contain 2D images or videos, lacking 3D-related annotations for reasoning and planning in the 3D space.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Another challenge for building such a generative world model lies in the lack of data. | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | 3D-VLA: A 3D Vision-Language-Action Generative World Model Robot: Actions are: [action tokens] Robot Control Projector Image / Point Cloud Diffusion Model Initial ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | D-VLA, Vision-Language-Action, Generative, World, Model, Robot, Actions, action, tokens, Control | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | utilize, curated, D-language, video, data, train, conditional, diffusion | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: D-VLA, Vision-Language-Action, Generative, World, Model, Robot, Actions, action, tokens, Control | p. 3 (1. Introduction), p. 3 (1. Introduction), p. 5 (4.3.1. PRETRAINING EMBODIED DIFFUSION MODELS) |
| Decision / output variable | action, pose, option or chunk a; body terms: Thirdly, better, encode, dynamics, framework, introduce, scene, tokens | p. 5 (4.2.2. INTERACTION TOKENS), p. 2 (1. Introduction), p. 5 (4.2.2. INTERACTION TOKENS) |
| Objective / loss / cost | policy/action modeling objective; cue terms: minimize, LLM, denoising, loss, Human, beings, pre-visualize, final | p. 6 (4.3.2. BRIDGING LLM AND GOAL GENERATION) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (4.3. Injecting Goal Generation Ability into 3D-VLA), p. 7 (5.3. Embodied Action Planning), p. 8 (5.3. Embodied Action Planning) |
| Success / guarantee | instruction-conditioned task success | p. 7 (5.1. 3D Reasoning and Localization), p. 6 (5. Experiments), p. 7 (5.1. 3D Reasoning and Localization) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** Secondly, existing embodied datasets mainly contain 2D images or videos, lacking 3D-related annotations for reasoning and planning in the 3D space.
- **p. 1 / 1. Introduction - extractive body cue:** Challenges inevitably exist for building such human-like 3D world models.
- **p. 2 / 1. Introduction - extractive body cue:** For datasets lacking depth data, we utilize a depth estimator to append necessary 3D details and project them to 3D point clouds.

## What the Paper Changes

PDF body contribution framing (p. 5 (4.2.2. INTERACTION TOKENS), p. 2 (1. Introduction), p. 5 (4.2.2. INTERACTION TOKENS), p. 1 (1. Introduction), p. 2 (1. Introduction)): Thirdly, to better encode dynamics with our framework, we introduce the <scene> </scene> tokens to enclose the embeddings of a static scene.

- **p. 2 / 1. Introduction - extractive body cue:** To sum up, we have the following contributions: • We propose 3D-VLA, a new family of 3D vision-languageaction embodied foundation models that unify 3D perception, ...
- **p. 5 / 4.2.2. INTERACTION TOKENS - extractive body cue:** To enhance the model's comprehension of 3D scenes and facilitate interaction within these environments, we introduce a novel set of interaction tokens.
- **p. 1 / 1. Introduction - extractive body cue:** To this end, we propose 3D-VLA by introducing a new family of embodied foundation models that seamlessly link 3D perception, reasoning, and action through a ...
- **p. 2 / 1. Introduction - extractive body cue:** Recognizing the inadequacy of multimodal generation ability in embodied foundation models, we propose to inject the goal generation ability into 3D-VLA.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 5 | FOR GOAL GENERATION To address the limitations of current diffusion models for goal generation in an embodied environment, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | Thus, for video segments where the camera pose does not change, we use optical flow to estimate which ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | We randomly sample 4000 episodes from the Open-X test set which 3D-VLA does not see in the training ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | In these diverse and uncontrolled environments, our 3D-VLA model consistently and robustly demonstrated its efficacy. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (1. Introduction), p. 3 (1. Introduction), p. 5 (4.3.1. PRETRAINING EMBODIED DIFFUSION MODELS), p. 8 (5.3. Embodied Action Planning). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), interface p. 3 (1. Introduction), p. 3 (1. Introduction), p. 5 (4.3.1. PRETRAINING EMBODIED DIFFUSION MODELS), p. 8 (5.3. Embodied Action Planning), objective p. 6 (4.3.2. BRIDGING LLM AND GOAL GENERATION).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** Another challenge for building such a generative world model lies in the lack of data. (p. 2, 1. Introduction).
- **Formulation-changing contribution:** To sum up, we have the following contributions: • We propose 3D-VLA, a new family of 3D vision-languageaction embodied foundation models that unify 3D perception, reasoning, and action with a ... (p. 2, 1. Introduction).
- **Assumption/failure evidence:** We randomly sample 4000 episodes from the Open-X test set which 3D-VLA does not see in the training process. (p. 7, 5.2. Multi-modal Goal Generation).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
