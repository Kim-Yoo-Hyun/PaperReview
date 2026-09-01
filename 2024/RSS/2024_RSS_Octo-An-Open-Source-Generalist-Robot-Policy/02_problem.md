# Problem - Octo: An Open-Source Generalist Robot Policy

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2405.12213; PDF retrieval source: https://arxiv.org/pdf/2405.12213. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): Training a unified control policy in robotics presents unique challenges, requiring handling different robot embodiments, sensor setups, action spaces, task specifications, environments, and compute budgets.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Large policies pretrained on diverse robot datasets have the potential to transform robotic learning: instead of training new policies from scratch, such generalist robot policies ...
- **p. 1 / Abstract - extractive body cue:** However, to be widely applicable across a range of robotic learning scenarios, environments, and tasks, such policies need to handle diverse sensors and action spaces, ...
- **p. 1 / Abstract - extractive body cue:** In this work, we aim to lay the groundwork for developing open-source, widely applicable, generalist policies for robotic manipulation.
- **p. 1 / Abstract - extractive body cue:** As a first step, we introduce Octo, a large transformer-based policy trained on 800k trajectories from the Open X-Embodiment dataset, the largest robot manipulation dataset ...
- **p. 1 / Abstract - extractive body cue:** It can be instructed via language commands or goal images and can be effectively finetuned to robot setups with new sensory inputs and action spaces ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Training a unified control policy in robotics presents unique challenges, requiring handling different robot embodiments, sensor setups, action spaces, task specifications, environments, and compute budgets.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Although these models represent significant steps toward a true "general-purpose robot model," they have been limited in multiple important aspects: they typically constrain downstream users ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Training a unified control policy in robotics presents unique challenges, requiring handling different robot embodiments, sensor setups, action spaces, task specifications, environments, ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | It also supports natural language instructions, goal images, observation histories, and multi-modal, chunked action prediction via diffusion decoding [17]. | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | supports, natural, language, instructions, goal, images, observation, histories, multi-modal, chunked | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | design, allows, flexibly, task, observation, inputs, action, output | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: supports, natural, language, instructions, goal, images, observation, histories, multi-modal, chunked | p. 3 (III. THE OCTO MODEL), p. 2 (I. INTRODUCTION), p. 4 (III. THE OCTO MODEL) |
| Decision / output variable | action, pose, option or chunk a; body terms: principle, collected, Lead, authors, ordered, alphabetically, Section, list | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. THE OCTO MODEL) |
| Objective / loss / cost | policy/action modeling objective; cue terms: AdamW, optimizer, inverse, square, root, decay, learning, rate | p. 5 (III. THE OCTO MODEL), p. 3 (III. THE OCTO MODEL), p. 4 (III. THE OCTO MODEL), p. 5 (III. THE OCTO MODEL) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (III. THE OCTO MODEL), p. 3 (III. THE OCTO MODEL), p. 4 (III. THE OCTO MODEL) |
| Success / guarantee | instruction-conditioned task success | p. 8 (Figure/Table caption), p. 6 (1) Can Octo control multiple robot embodiments and solve), p. 7 (1) Can Octo control multiple robot embodiments and solve) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / I. INTRODUCTION - extractive body cue:** Although these models represent significant steps toward a true "general-purpose robot model," they have been limited in multiple important aspects: they typically constrain downstream users ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Learning from scratch in this way requires significant data collection effort for each task, and the resulting policies usually exhibit only narrow generalization.

## What the Paper Changes

PDF contribution framing (p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. THE OCTO MODEL), p. 4 (III. THE OCTO MODEL), p. 5 (III. THE OCTO MODEL)): In principle, collected ∗Lead authors, ordered alphabetically, see Section A for list of contributions.

- **p. 2 / I. INTRODUCTION - extractive body cue:** Our primary contribution is Octo, a transformer-based policy pretrained on the largest robot manipulation dataset to date: 800k robot demonstrations from the Open X-Embodiment dataset ...
- **p. 3 / III. THE OCTO MODEL - extractive body cue:** It consists of three key parts: input tokenizers that transform
- **p. 4 / III. THE OCTO MODEL - extractive body cue:** This modular design enables us to add and remove observations or tasks during finetuning (see below).
- **p. 5 / III. THE OCTO MODEL - extractive body cue:** This enables our model to learn control mostly from self-supervised visual observations and reduces the burden on language annotation, similar to prior work on multi-context ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | While the Octo model achieves high success on novel objects, zero-shot performance slightly degrades in a new scene, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Finally, we zero-pad any missing camera channels and align the gripper action spaces between the datasets such that ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | (1) The hyperparameters α, γ, and σ correspond to the noise schedule: we use the standard cosine schedule ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (III. THE OCTO MODEL), p. 2 (I. INTRODUCTION), p. 4 (III. THE OCTO MODEL), p. 3 (III. THE OCTO MODEL). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), interface p. 3 (III. THE OCTO MODEL), p. 2 (I. INTRODUCTION), p. 4 (III. THE OCTO MODEL), p. 3 (III. THE OCTO MODEL), objective p. 5 (III. THE OCTO MODEL), p. 3 (III. THE OCTO MODEL), p. 4 (III. THE OCTO MODEL), p. 5 (III. THE OCTO MODEL).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
