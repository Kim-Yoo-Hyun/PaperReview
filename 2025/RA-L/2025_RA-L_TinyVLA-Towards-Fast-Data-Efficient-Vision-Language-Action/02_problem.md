# Problem - TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2409.12514; PDF retrieval source: https://arxiv.org/pdf/2409.12514. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 6 (1 Background), p. 6 (1 Background), p. 1 (I. INTRODUCTION)): Our results show that TinyVLA-H outperforms OpenVLA, achieving superior performance with 20 times less inference latency. challenges due to limited data and the difficulty of learning physical motion [1], [2].

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Vision-Language-Action (VLA) models have shown remarkable potential in visuomotor control and instruction comprehension through end-to-end learning processes.
- **p. 1 / Abstract - extractive PDF cue:** However, current VLA models face significant challenges: they are slow during inference and require extensive pre-training on large amounts of robotic data, making real-world deployment ...
- **p. 1 / Abstract - extractive PDF cue:** In this paper, we introduce a new family of compact vision-languageaction models, called TinyVLA, which offers two key advantages over existing VLA models: (1) faster ...
- **p. 1 / Abstract - extractive PDF cue:** Our framework incorporates two essential components to build TinyVLA: (1) initializing the policy backbone with robust, highspeed multimodal models, and (2) integrating a diffusion policy ...
- **p. 1 / Abstract - extractive PDF cue:** We conducted extensive evaluations of TinyVLA in both simulation and on real robots, demonstrating that our approach significantly outperforms the state-of-the-art VLA model, OpenVLA, in ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Our results show that TinyVLA-H outperforms OpenVLA, achieving superior performance with 20 times less inference latency. challenges due to limited data and the difficulty of ...
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** Given these challenges, a natural question arises: How can we build VLA models that retain the advantages of existing VLA models while being both fast ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Our results show that TinyVLA-H outperforms OpenVLA, achieving superior performance with 20 times less inference latency. challenges due to limited data and ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | TinyVLA encompasses several crucial designs: 1) We adopt a pre-trained VLM as the initialization of a policy network; 2) During training the ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | TinyVLA, encompasses, several, crucial, designs, adopt, pre-trained, VLM, initialization, policy | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | Learning, action, diffusion, policy, decoder, Then, instead, next | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: TinyVLA, encompasses, several, crucial, designs, adopt, pre-trained, VLM, initialization, policy | p. 2 (III. METHOD), p. 3 (III. METHOD), p. 3 (III. METHOD) |
| Decision / output variable | action, pose, option or chunk a; body terms: contribution, three, folds, introduce, novel, VLA, architecture, combines | p. 2 (I. INTRODUCTION), p. 6 (1 Background), p. 2 (I. INTRODUCTION) |
| Objective / loss / cost | policy/action modeling objective; cue terms: adopt, diffusion, policy, head, limits, gradient, updates, low-dimensional | p. 3 (III. METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (III. METHOD) |
| Success / guarantee | instruction-conditioned task success | p. 4 (IV. EXPERIMENTS), p. 3 (IV. EXPERIMENTS), p. 3 (IV. EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / I. INTRODUCTION - extractive PDF cue:** Given these challenges, a natural question arises: How can we build VLA models that retain the advantages of existing VLA models while being both fast ...
- **p. 6 / 1 Background - extractive PDF cue:** In Figure 7 (top), we present the StackCube task featuring an additional distractor, categorized into two difficulty levels.
- **p. 6 / 1 Background - extractive PDF cue:** Our model effectively manages both types of distractors at each difficulty level, whereas the Diffusion Policy and OpenVLA struggles with both.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** In addition to the inference challenges, these models also require extensive pretraining on large-scale robotic datasets.

## What the Paper Changes

PDF contribution framing (p. 2 (I. INTRODUCTION), p. 6 (1 Background), p. 2 (I. INTRODUCTION), p. 3 (III. METHOD), p. 3 (III. METHOD)): Our contribution are the three folds: • We introduce a novel VLA architecture that combines lightweight vision-language models with a diffusion model, enabling fast inference, strong performance, and excellent generalization ...

- **p. 6 / 1 Background - extractive PDF cue:** In Figure 9, we present the spatial generalization performance of our methods.
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** In this work, we propose TinyVLA, a compact visionlanguage-action model designed for fast inference.
- **p. 3 / III. METHOD - extractive PDF cue:** We report the average success rate on multiple tasks, We use TinyVLA-H as our method.
- **p. 3 / III. METHOD - extractive PDF cue:** We posit that this approach enables the pre-trained model to process inputs with maximum linguistic fidelity while retaining flexibility.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | Our approach overcomes the limitations of previous methods by | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | We use a cross mark to denote the failure of the model and a checkmark to indicate successful ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Fig. 10: Types of failure for TinyVLA with different sizes of pre-trained vision-language models. | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Notably, the OpenVLA fails in every trial. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (III. METHOD), p. 3 (III. METHOD), p. 3 (III. METHOD), p. 2 (I. INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 6 (1 Background), p. 6 (1 Background), p. 1 (I. INTRODUCTION), interface p. 2 (III. METHOD), p. 3 (III. METHOD), p. 3 (III. METHOD), p. 2 (I. INTRODUCTION), objective p. 3 (III. METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
