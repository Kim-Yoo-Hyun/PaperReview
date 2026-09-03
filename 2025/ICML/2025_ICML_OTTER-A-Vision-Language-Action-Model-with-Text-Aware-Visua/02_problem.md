# Problem - OTTER: A Vision-Language-Action Model with Text-Aware Visual Feature Extraction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=UHF0km7R5M; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/167304. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction)): This approach requires the policy network to connect the vision and language information and conduct precise robot control, which often presents significant challenges, especially in unseen environments.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Vision-Language-Action (VLA) models aim to predict robotic actions based on visual observations and language instructions.
- **p. 1 / Abstract - extractive body cue:** Existing approaches require fine-tuning pre-trained visionlanguage models (VLMs) as visual and language features are independently fed into downstream policies, degrading the pre-trained semantic alignments.
- **p. 1 / Abstract - extractive body cue:** We propose OTTER, a novel VLA architecture that leverages these existing alignments through explicit, text-aware visual feature extraction.
- **p. 1 / Abstract - extractive body cue:** Instead of processing all visual features, OTTER selectively extracts and passes only task-relevant visual features that are semantically aligned with the language instruction to the ...
- **p. 1 / Abstract - extractive body cue:** This allows OTTER to keep the pre-trained vision-language encoders frozen.
- **p. 1 / 1. Introduction - extractive body cue:** This approach requires the policy network to connect the vision and language information and conduct precise robot control, which often presents significant challenges, especially in ...
- **p. 2 / 1. Introduction - extractive body cue:** Both physical and simulation experiments demonstrate that OTTER outperforms existing VLA models, showing strong generalization to novel objects and environments with less performance degradation (Figure ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | This approach requires the policy network to connect the vision and language information and conduct precise robot control, which often presents significant ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | Different input modalities are usually encoded into separate tokens: multi-view images encoded via visual feature extractors, along with tokenized language instructions, optionally ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | Different, input, modalities, usually, encoded, separate, tokens, multi-view, images, visual | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | OTTER, vision-language-action, model, learning, robot, manipulation, policy, through | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: Different, input, modalities, usually, encoded, separate, tokens, multi-view, images, visual | p. 1 (1. Introduction), p. 4 (3.2. Model Architecture), p. 3 (3. Method) |
| Decision / output variable | action, pose, option or chunk a; body terms: OTTER, novel, VLA, architecture, freezes, pre-trained, vision, language | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Method) |
| Objective / loss / cost | policy/action modeling objective; cue terms: Specifically, similarity, scores, select, combine, visual, features, best | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (3.1. Text-Aware Visual Feature Extraction), p. 4 (3.2. Model Architecture) |
| Success / guarantee | instruction-conditioned task success | p. 5 (4.1. Environment Setup), p. 7 (5.1. Real-world Experiments), p. 6 (5.1. Real-world Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** Both physical and simulation experiments demonstrate that OTTER outperforms existing VLA models, showing strong generalization to novel objects and environments with less performance degradation (Figure ...
- **p. 1 / 1. Introduction - extractive body cue:** OTTER exhibits better zero-shot generalization to unseen objects, maintaining strong performance across a variety of novel tasks.
- **p. 2 / 1. Introduction - extractive body cue:** We propose OTTER, a VLA model that leverages the semantic alignment capabilities of pre-trained VLMs for better generalization.

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Method), p. 1 (1. Introduction)): To this end, we propose OTTER, a novel VLA architecture that freezes pre-trained vision and language encoders and extracts taskrelevant visual features guided by language instructions.

- **p. 2 / 1. Introduction - extractive body cue:** We propose OTTER, a VLA model that leverages the semantic alignment capabilities of pre-trained VLMs for better generalization.
- **p. 3 / 3. Method - extractive body cue:** We propose OTTER, a vision-language-action model for learning a robot manipulation policy through extraction of text-aware vision features from a pre-trained VLM.
- **p. 1 / 1. Introduction - extractive body cue:** OTTER exhibits better zero-shot generalization to unseen objects, maintaining strong performance across a variety of novel tasks.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | As OpenVLA has many tokens per timestep, its context length cannot be extended and we use its default ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | For a fair comparison, we extended the context history length of Octo to 10 (Octo cannot exceed a ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Finetuned π0-Fast-Droid achieves non-zero success rate on Drawer and Poking primitives, but still fails on the pouring primitive. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | While π0-Fast-Droid achieves decent performance on the pick and place primitives, it fails on all the other three ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 1 (1. Introduction), p. 4 (3.2. Model Architecture), p. 3 (3. Method), p. 1 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), interface p. 1 (1. Introduction), p. 4 (3.2. Model Architecture), p. 3 (3. Method), p. 1 (1. Introduction), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
