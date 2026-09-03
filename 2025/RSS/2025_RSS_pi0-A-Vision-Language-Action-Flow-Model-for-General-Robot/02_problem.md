# Problem - π0: A Vision-Language-Action Flow Model for General Robot Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p010.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p010.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 3 (1. INTRODUCTION), p. 3 (1. INTRODUCTION), p. 4 (1. INTRODUCTION)): However, developing such generalist robot policies - ie., robot foundation models - involves a number of major challenges.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Robot learning holds tremendous promise to untock the full potential of flexible, general, and dexterous robot systems, as well as to address some of the ...
- **p. 1 / Abstract - extractive body cue:** However, bringing robot learning to the level of generality required for effective real-world systems faces major ‘obstacles in terms of data, gener m, and robustness.
- **p. 1 / Abstract - extractive body cue:** In this paper, we discuss how generalist robot policies (i., robot foundation models) can address these challenges, and how we ean ‘design effective generalist robot ...
- **p. 1 / Abstract - extractive body cue:** We propose a novel flow matching architecture
- **p. 1 / Abstract - extractive body cue:** Physical Intelligence, San Francisco, California, USA.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** However, developing such generalist robot policies - ie., robot foundation models - involves a number of major challenges.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** Flexible and general-purpose models that can be tasked variety of robot behaviors have tremendous fications, but they may also offer solutions to some of the ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, developing such generalist robot policies - ie., robot foundation models - involves a number of major challenges. | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | Formally, we want to model the data distribution p(A,/o,), where Ar = [ar,r¢1,.rs 11-1] corresponds to an action chunk of future actions ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | Formally, want, model, data, distribution, where, corresponds, action, chunk, future | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | evaluate, model, language, commands, fine-tuning, downstream, tasks, combination | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: Formally, want, model, data, distribution, where, corresponds, action, chunk, future | p. 5 (IV. THE x MODEL), p. 4 (IV. THE x MODEL), p. 3 (1. INTRODUCTION) |
| Decision / output variable | action, pose, option or chunk a; body terms: more, complex, dexterous, behaviors, tying, shoelaces, cooking, shrimp | p. 4 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 3 (1. INTRODUCTION) |
| Objective / loss / cost | policy/action modeling objective; cue terms: architecture, inspired, Transfusion, trains, single, transformer, multiple, objectives | p. 4 (IV. THE x MODEL), p. 5 (IV. THE x MODEL), p. 7 (A. Evaluating the base model), p. 8 (A. Evaluating the base model) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 7 (A. Evaluating the base model), p. 5 (IV. THE x MODEL), p. 8 (A. Evaluating the base model) |
| Success / guarantee | instruction-conditioned task success | p. 9 (Figure/Table caption), p. 7 (VI. EXPERIMENTAL EVALUATION), p. 1 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. INTRODUCTION - extractive body cue:** Flexible and general-purpose models that can be tasked variety of robot behaviors have tremendous fications, but they may also offer solutions to some of the ...
- **p. 3 / 1. INTRODUCTION - extractive body cue:** In contrast, our model employs a novel design that fine-tunes a VLM to produce actions via flow matching (52, 28], a variant of diffusion [20, ...
- **p. 3 / 1. INTRODUCTION - extractive body cue:** ‘The complexity of the tasks we illustrate goes significantly beyond prior work.
- **p. 4 / 1. INTRODUCTION - extractive body cue:** The pre-training phase (Section V-A) also uses diverse language labels, combining rask names and segment annotations (fine-grained labels for sub-trajectories, typically about 2 seconds in ...

## What the Paper Changes

PDF body contribution framing (p. 4 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 3 (1. INTRODUCTION), p. 3 (1. INTRODUCTION), p. 4 (1. INTRODUCTION)): ‘of more complex and dexterous behaviors, such as tying shoelaces [58] or cooking shrimp [17], we show that our framework can leam very long tasks, sometimes tens of, minutes in ...

- **p. 2 / 1. INTRODUCTION - extractive body cue:** In this paper, we present a prototype model and learning framework, which we call zo, that illustrates how each of these three bottlenecks could be ...
- **p. 3 / 1. INTRODUCTION - extractive body cue:** The contributions of our work consist of a novel generalist robot policy architecture based on VLM pre-training and flow matching, and an empirical investigation of ...
- **p. 3 / 1. INTRODUCTION - extractive body cue:** This enables our model to control robots at frequencies of up to 50 Hz for dexterous tasks such as laundry folding (see Figure 1), To ...
- **p. 4 / 1. INTRODUCTION - extractive body cue:** Note that we use PaliGemma for convenience and because of its comparatively small size (which is useful for real-time control), but our framework is compatible ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 11 | DISCUSSION, LIMITATIONS, AND FUTURE WORK | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | This presents challenges due to the egg shape, slipperiness, and the need for careful placement. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 5 (IV. THE x MODEL), p. 4 (IV. THE x MODEL), p. 3 (1. INTRODUCTION), p. 2 (1. INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 3 (1. INTRODUCTION), p. 3 (1. INTRODUCTION), p. 4 (1. INTRODUCTION), interface p. 5 (IV. THE x MODEL), p. 4 (IV. THE x MODEL), p. 3 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), objective p. 4 (IV. THE x MODEL), p. 5 (IV. THE x MODEL), p. 7 (A. Evaluating the base model), p. 8 (A. Evaluating the base model).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** However, developing such generalist robot policies - ie., robot foundation models - involves a number of major challenges. (p. 2, 1. INTRODUCTION).
- **Formulation-changing contribution:** The contributions of our work consist of a novel generalist robot policy architecture based on VLM pre-training and flow matching, and an empirical investigation of pre-training/posttraining recipes for such robot ... (p. 3, 1. INTRODUCTION).
- **Assumption/failure evidence:** OpenVLA struggles on these tasks because its autoregressive diseretization architecture does not support action chunks. (p. 7, A. Evaluating the base model).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
