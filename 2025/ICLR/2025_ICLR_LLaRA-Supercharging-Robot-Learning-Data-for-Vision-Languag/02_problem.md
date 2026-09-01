# Problem - LLaRA: Supercharging Robot Learning Data for Vision-Language Policy

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (47 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=iVxxgZlXh6; PDF retrieval source: https://openreview.net/pdf/88e833c98e7c9f665ef182cf0d30f65c58655784.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION)): The resulting VLMs exhibit strong vision-language skills, but not without limitations such as spatial awareness (Chen et al., 2023; Ranasinghe et al., 2024b) or niche-domain understanding.

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive PDF cue:** Vision Language Models (VLMs) have recently been leveraged to generate robotic actions, forming Vision-Language-Action (VLA) models.
- **p. 1 / ABSTRACT - extractive PDF cue:** However, directly adapting a pretrained VLM for robotic control remains challenging, particularly when constrained by a limited number of robot demonstrations.
- **p. 1 / ABSTRACT - extractive PDF cue:** In this work, we introduce LLaRA: Large Language and Robotics Assistant, a framework that formulates robot action policy as visuo-textual conversations and enables an efficient ...
- **p. 1 / ABSTRACT - extractive PDF cue:** First, we present an automated pipeline to generate conversation-style instruction tuning data for robots from existing behavior cloning datasets, aligning robotic actions with image pixel ...
- **p. 1 / ABSTRACT - extractive PDF cue:** Further, we enhance this dataset in a self-supervised manner by defining six auxiliary tasks, without requiring any additional action annotations.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** The resulting VLMs exhibit strong vision-language skills, but not without limitations such as spatial awareness (Chen et al., 2023; Ranasinghe et al., 2024b) or niche-domain ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Motivated by the promising attributes of VLMs, we explore a process, called Visuomotor Instruction Tuning, of adapting a VLM to a robot action policy that ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | The resulting VLMs exhibit strong vision-language skills, but not without limitations such as spatial awareness (Chen et al., 2023; Ranasinghe et al., ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | We formulate the dataset in a single-image single-turn conversation setting to emulate a policy where the user queries the Vision Language Model ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | formulate, dataset, single-image, single-turn, conversation, setting, emulate, policy, where, user | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | formulation, conversation-style, instruction-response, data, enables, convert, VLM, robot | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: formulate, dataset, single-image, single-turn, conversation, setting, emulate, policy, where, user | p. 16 (A.1.1 BUILD inBC DATASET FROM EXPERT TRAJECTORIES), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Decision / output variable | action, pose, option or chunk a; body terms: formulation, conversation-style, instruction-response, data, enables, convert, VLM, robot | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 16 (A.1.1 BUILD inBC DATASET FROM EXPERT TRAJECTORIES) |
| Objective / loss / cost | policy/action modeling objective; cue terms: enhances, VLM, understanding, task, context, within, constraints, single-turn | p. 16 (A.1.1 BUILD inBC DATASET FROM EXPERT TRAJECTORIES), p. 17 (A.1.1 BUILD inBC DATASET FROM EXPERT TRAJECTORIES), p. 21 (A.3 INFERENCE) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 21 (A.3 INFERENCE), p. 16 (A.1.1 BUILD inBC DATASET FROM EXPERT TRAJECTORIES), p. 17 (A.1.1 BUILD inBC DATASET FROM EXPERT TRAJECTORIES) |
| Success / guarantee | instruction-conditioned task success | p. 7 (6 EXPERIMENTS), p. 7 (6 EXPERIMENTS), p. 8 (6 EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Motivated by the promising attributes of VLMs, we explore a process, called Visuomotor Instruction Tuning, of adapting a VLM to a robot action policy that ...

## What the Paper Changes

PDF contribution framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 16 (A.1.1 BUILD inBC DATASET FROM EXPERT TRAJECTORIES), p. 17 (A.1.2 BUILD D-inBC FROM inBC), p. 17 (A.1.1 BUILD inBC DATASET FROM EXPERT TRAJECTORIES)): Such a formulation based on conversation-style instruction-response data enables us to convert a VLM into a robot action policy effortlessly.

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Formulating robot manipulation tasks into instruction-response pairs described in natural language, which enables successful instruction tuning of a VLM as a policy.
- **p. 16 / A.1.1 BUILD inBC DATASET FROM EXPERT TRAJECTORIES - extractive PDF cue:** Given the current limitations of LLaVA (Liu et al., 2023a), to optimize performance, we propose two techniques: • Action history in query.
- **p. 17 / A.1.2 BUILD D-inBC FROM inBC - extractive PDF cue:** We present the performance of D-inBC (L) at Tab.
- **p. 17 / A.1.1 BUILD inBC DATASET FROM EXPERT TRAJECTORIES - extractive PDF cue:** The action space consists of two poses: for the robot equipped with a spatula, these poses indicate the start and end points of a push; ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 27 | Table 17: Robostness evaluation results of D-inBC + Aux (B) + Oracle (VIMA-80k, 8 epochs) Prob. of Failure ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 16 | Given the current limitations of LLaVA (Liu et al., 2023a), to optimize performance, we propose two techniques: • ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 17 | 8 has shown its great power in many aspects when the reference image contains a scene that has ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 16 (A.1.1 BUILD inBC DATASET FROM EXPERT TRAJECTORIES), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 16 (A.1.1 BUILD inBC DATASET FROM EXPERT TRAJECTORIES). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), interface p. 16 (A.1.1 BUILD inBC DATASET FROM EXPERT TRAJECTORIES), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 16 (A.1.1 BUILD inBC DATASET FROM EXPERT TRAJECTORIES), objective p. 16 (A.1.1 BUILD inBC DATASET FROM EXPERT TRAJECTORIES), p. 17 (A.1.1 BUILD inBC DATASET FROM EXPERT TRAJECTORIES), p. 21 (A.3 INFERENCE).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
