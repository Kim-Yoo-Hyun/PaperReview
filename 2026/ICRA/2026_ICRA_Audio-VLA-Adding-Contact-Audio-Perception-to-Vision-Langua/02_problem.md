# Problem - Audio-VLA: Adding Contact Audio Perception to Vision-Language-Action Model for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html; PDF retrieval source: https://arxiv.org/pdf/2511.09958v1. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): Despite these promising capabilities, integrating acoustic information into existing VLA frameworks presents technical challenges, such as extracting contact event information from high-frequency contact audio, and the lack of audio-enh ...

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** The Vision-Language-Action models (VLA) have achieved significant advances in robotic manipulation recently.
- **p. 1 / Abstract - extractive PDF cue:** However, vision-only VLA models create fundamental limitations, particularly in perceiving interactive and manipulation dynamic processes.
- **p. 1 / Abstract - extractive PDF cue:** This paper proposes Audio-VLA, a multimodal manipulation policy that leverages contact audio to perceive contact events and dynamic process feedback.
- **p. 1 / Abstract - extractive PDF cue:** AudioVLA overcomes the vision-only constraints of VLA models.
- **p. 1 / Abstract - extractive PDF cue:** Additionally, this paper introduces the Task Completion Rate (TCR) metric to systematically evaluate dynamic operational processes.
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** Despite these promising capabilities, integrating acoustic information into existing VLA frameworks presents technical challenges, such as extracting contact event information from high-frequency contact audio, and ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** However, current VLA methods exhibit a fundamental limitation as they rely exclusively on visual perception [6]- [10].

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Despite these promising capabilities, integrating acoustic information into existing VLA frameworks presents technical challenges, such as extracting contact event information from high-frequency ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | Furthermore, recognizing the limitations of existing evaluation metrics that focus primarily on final task outcomes, the Task Completion Rate (TCR) evaluation metric ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | Furthermore, recognizing, limitations, existing, evaluation, metrics, focus, primarily, final, task | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | Unlike, VLA, models, Audio-VLA, incorporates, audio, perception, enabling | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: Furthermore, recognizing, limitations, existing, evaluation, metrics, focus, primarily, final, task | p. 2 (I. INTRODUCTION), p. 4 (III. METHOD), p. 1 (I. INTRODUCTION) |
| Decision / output variable | action, pose, option or chunk a; body terms: Audio-VLA, consists, four, components, including, multi-modal, encoder, multi | p. 2 (III. METHOD), p. 2 (I. INTRODUCTION), p. 3 (III. METHOD) |
| Objective / loss / cost | policy/action modeling objective; cue terms: achieved, through, minimization, mean, loss, function, K-1, Training | p. 2 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (III. METHOD), p. 3 (III. METHOD), p. 3 (III. METHOD) |
| Success / guarantee | instruction-conditioned task success | p. 6 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** However, current VLA methods exhibit a fundamental limitation as they rely exclusively on visual perception [6]- [10].
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Prior works [15], [16], [19] have attempted to use tactile signals to compensate for VLA's limited perception of dynamic information such as contact events and ...
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** Furthermore, recognizing the limitations of existing evaluation metrics that focus primarily on final task outcomes, the Task Completion Rate (TCR) evaluation metric is proposed to ...

## What the Paper Changes

PDF contribution framing (p. 2 (III. METHOD), p. 2 (I. INTRODUCTION), p. 3 (III. METHOD), p. 3 (III. METHOD), p. 1 (I. INTRODUCTION)): 2, the proposed Audio-VLA consists of four components including a multi-modal encoder, multi

- **p. 2 / I. INTRODUCTION - extractive PDF cue:** In this paper, we propose Audio-VLA, a multimodal manipulation policy that combines acoustic and visual perception.
- **p. 3 / III. METHOD - extractive PDF cue:** It consists of two powerful vision transformers, DINOv2 [23] and SigLIP [24], pre-trained on Internet-scale image data to capture rich visual features and comprehensive spatial ...
- **p. 3 / III. METHOD - extractive PDF cue:** The model consists of multi-modal encoders including audio, vision, and proprioceptive modules, multi-modal Projector that map heterogeneous features to a unified representation space, a 7B-parameter ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Large-scale vision-language pretraining [4] enables VLA models to achieve generalizable manipulation capabilities across diverse scenarios.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | Our proposed Audio-VLA demonstrates that acoustic perception addresses fundamental limitations of vision-only approaches in manipulation tasks, providing irreplaceable ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | This paper presents Audio-VLA, a multimodal manipulation policy that integrates acoustic perception into VLA models to overcome vision-only ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Experimental results demonstrate that Audio-VLA achieves superior performance in both simulation environments and real-world tasks, proving the contribution ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Audio-VLA overcomes these limitations through acoustic signatures of interaction physics. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (I. INTRODUCTION), p. 4 (III. METHOD), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 2 (I. INTRODUCTION), p. 4 (III. METHOD), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), objective p. 2 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
