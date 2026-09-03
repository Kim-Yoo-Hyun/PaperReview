# Problem - RynnVLA-001: Using Human Demonstrations to Improve Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_3.html; PDF retrieval source: https://arxiv.org/pdf/2509.15212v1. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 2 (1 INTRODUCTION), p. 1 (1 Introduction), p. 2 (1 INTRODUCTION)): Another line of studies works on exploiting massive prior knowledge from pretrained generative models (Cheang et al., 2024; Hu et al., 2024) or VLMs (Zitkovich et al., 2023; Kim et ...

## PDF Body Digest

- **p. 1 / 1 Introduction - extractive body cue:** The past few years have witnessed rapid progress in large language models (Comanici et al., 2025; Anthropic; OpenAI, 2025; Grattafiori et al., 2024; Guo et ...
- **p. 1 / 1 Introduction - extractive body cue:** The success in these fields is attributed to the availability of large-scale datasets.
- **p. 1 / 1 Introduction - extractive body cue:** For instance, large language models benefit from abundant training data readily accessible from web sources.
- **p. 1 / 1 Introduction - extractive body cue:** In contrast, progress in Vision-Language-Action (VLA) models is constrained by the scarcity of large-scale robot manipulation data.
- **p. 1 / 1 Introduction - extractive body cue:** Collecting such data typically relies on human teleoperation on physical robots to record manipulation trajectories, making large-scale dataset construction both labor-intensive and costly.
- **p. 1 / 1 Introduction - extractive body cue:** Another line of studies works on exploiting massive prior knowledge from pretrained generative models (Cheang et al., 2024; Hu et al., 2024) or VLMs (Zitkovich ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, a gap remains between the high-level visual observations and the low-level action spaces required to control real robots.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Another line of studies works on exploiting massive prior knowledge from pretrained generative models (Cheang et al., 2024; Hu et al., 2024) ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | In a typical VLA setting, actions are predicted conditioned on current observations (e.g., visual inputs and robot states) and a language instruction. | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | typical, VLA, setting, actions, predicted, conditioned, current, observations, visual, inputs | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | Robot-Centric, Vision-Language-Action, Modeling, employs, robot, datasets, paired, language | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: typical, VLA, setting, actions, predicted, conditioned, current, observations, visual, inputs | p. 4 (3 Methodology), p. 4 (3 Methodology), p. 2 (1 INTRODUCTION) |
| Decision / output variable | action, pose, option or chunk a; body terms: RynnVLA-001, VLA, model, enhanced, video, generation, pretraining, ensure | p. 1 (1 Introduction), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Objective / loss / cost | policy/action modeling objective; cue terms: During, training, model, optimized, concurrent, objectives, Robot, Action | p. 4 (3 Methodology), p. 5 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 6 (3 METHODOLOGY), p. 6 (3 METHODOLOGY) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3 Methodology), p. 5 (3 METHODOLOGY), p. 4 (3 Methodology) |
| Success / guarantee | instruction-conditioned task success | p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, a gap remains between the high-level visual observations and the low-level action spaces required to control real robots.
- **p. 1 / 1 Introduction - extractive body cue:** There have been some early attempts to address the challenges of data scarcity.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Grab the flower and put it in the vase Put the black objects on the tabletop in the open drawer and then close the drawer ...

## What the Paper Changes

PDF body contribution framing (p. 1 (1 Introduction), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 4 (3 METHODOLOGY), p. 5 (3 METHODOLOGY)): In this work, we propose RynnVLA-001, a VLA model enhanced by video generation pretraining.

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To ensure the smoothness and temporal coherence of predicted actions, we propose ActionVAE, a variational autoencoder that encodes action chunks into compact embeddings.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our framework leverages three types of training data: (1) Ego-Centric Video Generative Pretraining uses millions of ego-centric human manipulation videos for future frame prediction.
- **p. 4 / 3 METHODOLOGY - extractive body cue:** The training consists of three stages: (1) Ego-Centric Video Generative Pretraining trains a transformer-based Image-to-Video (I2V) model for future frame prediction.
- **p. 5 / 3 METHODOLOGY - extractive body cue:** To provide the model with proprioceptive information, we introduce state embeddings (blue blocks in Fig.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 10 | At a lower resolution of 256 × 256, the VQGAN's reconstruction quality degrades, the VQGAN fails to generate ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | A trial is marked as a failure under any of the following conditions: 1) The time limit is ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 12 | A total of 5 failure cases of the 10 trials consistently select a distractor object. | reported limitation/failure wording; scope must be verified |
| body cue at p. 12 | However, when we elevate the front camera, altering the scene's projective geometry, the model fails to insert 12 | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (3 Methodology), p. 4 (3 Methodology), p. 2 (1 INTRODUCTION), p. 6 (3 METHODOLOGY). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1 Introduction), p. 2 (1 INTRODUCTION), p. 1 (1 Introduction), p. 2 (1 INTRODUCTION), interface p. 4 (3 Methodology), p. 4 (3 Methodology), p. 2 (1 INTRODUCTION), p. 6 (3 METHODOLOGY), objective p. 4 (3 Methodology), p. 5 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 6 (3 METHODOLOGY), p. 6 (3 METHODOLOGY).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
