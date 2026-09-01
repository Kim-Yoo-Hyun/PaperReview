# Problem - VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (26 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=QZYZ0Xm58q; PDF retrieval source: https://openreview.net/pdf/ab187b19e4f174f9a6c3f7d82d52c8f6f1abfafb.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction)): While effective to some extent, these methods often require architectural modifications or retraining, and more importantly, they lack task-specific design tailored to the intrinsic characteristics of VLA tasks.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Vision-Language-Action (VLA) models have demonstrated strong multi-modal reasoning capabilities, enabling direct action generation from visual perception and language instructions in an end-to-end manner.
- **p. 1 / Abstract - extractive PDF cue:** However, their substantial computational cost poses a challenge for real-time robotic control, where rapid decision-making is essential.
- **p. 1 / Abstract - extractive PDF cue:** This paper introduces VLA-Cache, a training-free inference acceleration method that reduces computational overhead by adaptively caching and reusing static visual tokens across frames.
- **p. 1 / Abstract - extractive PDF cue:** Exploiting the temporal continuity in robotic manipulation, VLA-Cache identifies minimally changed tokens between adjacent frames and reuses their cached key-value representations, thereby circumventing redundant computations.
- **p. 1 / Abstract - extractive PDF cue:** Additionally, to maintain action precision, VLA-Cache selectively re-computes task-relevant tokens that are environmentally sensitive, ensuring the fidelity of critical visual information.
- **p. 1 / 1 Introduction - extractive PDF cue:** While effective to some extent, these methods often require architectural modifications or retraining, and more importantly, they lack task-specific design tailored to the intrinsic characteristics ...
- **p. 1 / 1 Introduction - extractive PDF cue:** Learning a robust and generalizable policy for robotic manipulation through policy learning has long been a challenging problem [1], with traditional reinforcement learning approaches [2, ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | While effective to some extent, these methods often require architectural modifications or retraining, and more importantly, they lack task-specific design tailored to ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | However, most existing Vision-Language-Action (VLA) 3 | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | However, most, existing, Vision-Language-Action, VLA, While, caching, effective, language, decoding | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | Leveraging, large-scale, real-world, robotic, datasets, pioneering, works, have | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: However, most, existing, Vision-Language-Action, VLA, While, caching, effective, language, decoding | p. 3 (3 Methodology), p. 3 (3 Methodology), p. 1 (1 Introduction) |
| Decision / output variable | action, pose, option or chunk a; body terms: address, inefficiency, introduced, repeatedly, processing, static, visual, information | p. 2 (1 Introduction), p. 3 (3 Methodology), p. 3 (3 Methodology) |
| Objective / loss / cost | policy/action modeling objective; cue terms: robotic, action, prediction, most, visual, tokens, remain, static | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (3 Methodology), p. 3 (3 Methodology) |
| Success / guarantee | instruction-conditioned task success | p. 9 (Figure/Table caption), p. 7 (5 Experiment), p. 9 (5 Experiment) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive PDF cue:** Learning a robust and generalizable policy for robotic manipulation through policy learning has long been a challenging problem [1], with traditional reinforcement learning approaches [2, ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Action (T) LLM Decoder Current Step (T) Tokenize Previous Step (T-1) Action (T-1) Update & Caching LLM Decoder Static Dynamic Tokenize Pick up the gray ...
- **p. 2 / 1 Introduction - extractive PDF cue:** To further optimize reuse, VLA-Cache employs a layer-adaptive caching strategy that dynamically adjusts the reuse ratio per layer based on attention entropy, prioritizing precise updates ...

## What the Paper Changes

PDF contribution framing (p. 2 (1 Introduction), p. 3 (3 Methodology), p. 3 (3 Methodology), p. 2 (1 Introduction)): To address the inefficiency introduced by repeatedly processing static visual information, we present VLA-Cache, a training-free inference acceleration method that exploits temporal continuity in robotic perception.

- **p. 3 / 3 Methodology - extractive PDF cue:** To address this, we propose a method that identifies visually static tokens and filters out semantically important ones based on attention scores from the VLA ...
- **p. 3 / 3 Methodology - extractive PDF cue:** In the following sections, we introduce its core mechanisms: static token selection, task-relevance filtering, and layer-adaptive reuse to accelerate VLA inference while preserving action accuracy.
- **p. 2 / 1 Introduction - extractive PDF cue:** This consistency allows for caching the computations of these tokens from the previous step.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 25 | Table 11: Real-world results with trial counts and success rates. Results with Counts and Rates. Table 11 reports ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | In contrast, FastV and SparseVLM fail to improve inference speed and often degrade task performance. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | It performs robustly across tasks and exceeds the baseline on goal-oriented manipulation. | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | As shown in Table 7, success rate of baseline dropped from 95% to 80% under noise. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (3 Methodology), p. 3 (3 Methodology), p. 1 (1 Introduction), p. 1 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), interface p. 3 (3 Methodology), p. 3 (3 Methodology), p. 1 (1 Introduction), p. 1 (1 Introduction), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
