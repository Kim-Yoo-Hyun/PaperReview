# Problem - Interleave-VLA: Enhancing Robot Manipulation with Image-Text Interleaved Instructions

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (31 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=ULTWUuGhC3; PDF retrieval source: https://openreview.net/pdf/ef985dc6079e883f0130a114f04e69fdf820e23f.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION)): In order to bridge the gap of the lack of image-text interleaved datasets in robotic manipulation, we develop a pipeline to automatically construct interleaved instructions from existing datasets.

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive PDF cue:** The rise of foundation models paves the way for generalist robot policies in the physical world.
- **p. 1 / ABSTRACT - extractive PDF cue:** Existing methods relying on text-only instructions often struggle to generalize to unseen scenarios.
- **p. 1 / ABSTRACT - extractive PDF cue:** We argue that interleaved image-text inputs offer richer and less biased context and enable robots to better handle unseen tasks with in-context visual grounding.
- **p. 1 / ABSTRACT - extractive PDF cue:** Building on this insight, we introduce Interleave-VLA, a robot learning paradigm extending interleaved image-text instructions from digital world to directly generating continuous action sequences in ...
- **p. 1 / ABSTRACT - extractive PDF cue:** It offers a natural, flexible, and model-agnostic paradigm that extends state-of-the-art vision-language-action (VLA) models with minimal modifications while achieving strong zero-shot generalization.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** In order to bridge the gap of the lack of image-text interleaved datasets in robotic manipulation, we develop a pipeline to automatically construct interleaved instructions ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** However, current VLA models (Brohan et al., 2023; Kim et al., 2024; Black et al., 2024) remain predominantly trained on text-only instructions-a setting we refer ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | In order to bridge the gap of the lack of image-text interleaved datasets in robotic manipulation, we develop a pipeline to automatically ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | To develop a general and practical robot policy capable of acting on interleaved image-text instructions in the real world, a straightforward solution ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | develop, general, practical, robot, policy, capable, acting, interleaved, image-text, instructions | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | Building, insight, introduce, Interleave-VLA, robot, learning, paradigm, extending | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: develop, general, practical, robot, policy, capable, acting, interleaved, image-text, instructions | p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 1 (ABSTRACT) |
| Decision / output variable | action, pose, option or chunk a; body terms: illustrated, Figure, Interleave-VLA, consists, three, components, lightweight, adaptation | p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION) |
| Objective / loss / cost | policy/action modeling objective; cue terms: illustrated, Figure, Interleave-VLA, consists, three, components, lightweight, adaptation | p. 2 (1 INTRODUCTION) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Success / guarantee | instruction-conditioned task success | p. 18 (Figure/Table caption), p. 18 (Figure/Table caption), p. 24 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** However, current VLA models (Brohan et al., 2023; Kim et al., 2024; Black et al., 2024) remain predominantly trained on text-only instructions-a setting we refer ...
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** We summarize our key takeaways below: • Generalization failures in VLAs often stem from attentional hallucinations, which we summarized as attentional bias, diffused attention, and ...
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** (1) We introduce Interleave-VLA: a lightweight, transferable paradigm that enhances the generalization capability of current text input VLA models with interleaved image-text instructions.

## What the Paper Changes

PDF contribution framing (p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT)): As illustrated in Figure 2, Interleave-VLA consists of three key components: (1) a lightweight adaptation module that introduces special separator tokens into the tokenizer, enabling existing VLAs to process interleaved ...

- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** The interleaved format enables robust zeroshot generalization to novel objects and user-provided sketches unseen during training.
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** (1) We introduce Interleave-VLA: a lightweight, transferable paradigm that enhances the generalization capability of current text input VLA models with interleaved image-text instructions.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** This enables training Interleave-VLA with real-world interaction data and diverse visual instruction types.
- **p. 1 / ABSTRACT - extractive PDF cue:** Building on this insight, we introduce Interleave-VLA, a robot learning paradigm extending interleaved image-text instructions from digital world to directly generating continuous action sequences in ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 22 | Figure 9: Interleave-VLA Inference time w.r.t number of images. When number of images is 1 - 2, it ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | (2) What are the common failure modes of Text-VLA, and how does Interleave-VLA address them? | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | For quantitative breakdown of failure modes, please refer to Figure 11. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | These failures can be attributed to semantic ambiguity in cluttered visual contexts and distributional bias in the training ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), interface p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), objective p. 2 (1 INTRODUCTION).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
