# Problem - Long-VLA: Unleashing Long-Horizon Capability of Vision Language Action Model for Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v305/fan25a.html; PDF retrieval source: https://raw.githubusercontent.com/mlresearch/v305/main/assets/fan25a/fan25a.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 2 (1 Introduction)): However, most existing VLA frameworks are tailored for short-horizon tasks, leaving the challenge of long-horizon task execution largely unresolved.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Vision-Language-Action (VLA) models have become a cornerstone in robotic policy learning, leveraging large-scale multimodal data for robust and scalable control.
- **p. 1 / Abstract - extractive body cue:** However, existing VLA frameworks primarily address short-horizon tasks, and their effectiveness on long-horizon, multi-step robotic manipulation remains limited due to challenges in skill chaining and ...
- **p. 1 / Abstract - extractive body cue:** In this work, we introduce Long-VLA, the first end-to-end VLA model specifically designed for long-horizon robotic tasks.
- **p. 1 / Abstract - extractive body cue:** Our approach features a novel phase-aware input masking strategy that adaptively segments each subtask into moving and interaction phases, enabling the model to focus on ...
- **p. 1 / Abstract - extractive body cue:** This unified strategy preserves the scalability and data efficiency of VLA training, and our architecture-agnostic module can be seamlessly integrated into existing VLA models.
- **p. 2 / 1 Introduction - extractive body cue:** However, most existing VLA frameworks are tailored for short-horizon tasks, leaving the challenge of long-horizon task execution largely unresolved.
- **p. 2 / 1 Introduction - extractive body cue:** Therefore, solving the skill chaining problem in long-horizon tasks while preserving the scalability and data efficiency of VLA models remains a fundamental and open challenge.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, most existing VLA frameworks are tailored for short-horizon tasks, leaving the challenge of long-horizon task execution largely unresolved. | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | Static Cam 𝒔𝒔𝒃𝒃 𝒕𝒕 Gripper Cam 𝒔𝒔𝒈𝒈𝒕𝒕 … … Multimodal Transformer Encoder … Noise 𝝈𝝈 𝛥𝛥𝑇𝑇 𝛥𝛥𝑅𝑅 𝑠𝑠𝑔𝑔 𝑠𝑠𝑝𝑝 Detection 𝒅𝒅𝒕𝒕 … ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | Static, Cam, Gripper, Multimodal, Transformer, Encoder, Noise, Detection, Action, masking | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | leverage, unlabeled, play, data, follow, strategy, similar, where | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: Static, Cam, Gripper, Multimodal, Transformer, Encoder, Noise, Detection, Action, masking | p. 4 (3 Method), p. 5 (3 Method), p. 5 (3 Method) |
| Decision / output variable | action, pose, option or chunk a; body terms: Long-VLA, first, end-to-end, VLA, model, specifically, designed, longhorizon | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (3 Method) |
| Objective / loss / cost | policy/action modeling objective; cue terms: decomposition, dataset, model, trained, single, score, matching, loss | p. 4 (3 Method), p. 4 (3 Method) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3 Method), p. 3 (3 Method), p. 5 (3 Method) |
| Success / guarantee | instruction-conditioned task success | p. 6 (4 Experiment), p. 13 (Figure/Table caption), p. 7 (4 Experiment) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive body cue:** Therefore, solving the skill chaining problem in long-horizon tasks while preserving the scalability and data efficiency of VLA models remains a fundamental and open challenge.

## What the Paper Changes

PDF body contribution framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (3 Method), p. 3 (3 Method), p. 4 (3 Method)): To this end, we propose Long-VLA, the first end-to-end VLA model specifically designed for longhorizon robotic manipulation.

- **p. 2 / 1 Introduction - extractive body cue:** Finally, we present L-CALVIN and show that Long-VLA outperforms state-of-the-art methods on simulated and real-world robotic tasks, with robust performance on diverse long-horizon tasks.
- **p. 3 / 3 Method - extractive body cue:** To address this limitation, we propose Long-VLA, a unified end-to-end VLA model that leverages phase-specific data more effectively.
- **p. 3 / 3 Method - extractive body cue:** 3.1 Revisiting Decomposition Strategy Before introducing our method, we first investigate whether decomposition is essential for VLA models.
- **p. 4 / 3 Method - extractive body cue:** Based on these observations, we propose an input-level adaptation strategy that dynamically adjusts visual inputs according to the current task phase.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 19 | Figure 12: Failure case of π0. Base Policy LongVLA Press blue button Grab the corn Put in the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 1 | Figure 1: In contrast to previous methods that (a) adopt a unified model but are limited to short- ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | By segmenting each subtask into movement and interaction phases with targeted masking, Long-VLA mitigates distribution shifts and enhances ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | This demonstrates the robustness of our method in handling long-horizon tasks. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 4 (3 Method). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1 Introduction), p. 2 (1 Introduction), interface p. 4 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 4 (3 Method), objective p. 4 (3 Method), p. 4 (3 Method).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (20 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** However, most existing VLA frameworks are tailored for short-horizon tasks, leaving the challenge of long-horizon task execution largely unresolved. (p. 2, 1 Introduction).
- **Formulation-changing contribution:** To this end, we propose Long-VLA, the first end-to-end VLA model specifically designed for longhorizon robotic manipulation. (p. 2, 1 Introduction).
- **Assumption/failure evidence:** While our model mitigates the initial state gap, it does not address execution failures under precise initial conditions. (p. 9, Limitation).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
