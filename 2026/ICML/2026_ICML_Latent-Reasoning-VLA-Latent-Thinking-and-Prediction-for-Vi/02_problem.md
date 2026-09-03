# Problem - Latent Reasoning VLA: Latent Thinking and Prediction for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=P64X2q1n1H; PDF retrieval source: https://openreview.net/pdf/d1d48bb8ae32dab3bc513e65d14fb7fc84c438ea.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction)): Despite their effectiveness, existing CoT-based methods face two fundamental challenges.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Vision-Language-Action (VLA) models benefit from chain-of-thought (CoT) reasoning, but existing approaches incur high inference overhead and rely on discrete reasoning representations that mismatch continuous perception ...
- **p. 1 / Abstract - extractive body cue:** We propose Latent Reasoning VLA (LaRA-VLA), a unified VLA framework that internalizes multimodal CoT reasoning into continuous latent representations for embodied action.
- **p. 1 / Abstract - extractive body cue:** LaRA-VLA performs unified reasoning and prediction in latent space, eliminating explicit CoT generation at inference time and enabling efficient, actionoriented control.
- **p. 1 / Abstract - extractive body cue:** To realize latent embodied reasoning, we introduce a curriculum-based training paradigm that progressively transitions from explicit textual and visual CoT supervision to latent reasoning, and ...
- **p. 1 / Abstract - extractive body cue:** We construct two structured CoT datasets and evaluate LaRA-VLA on both simulation benchmarks and long-horizon real-robot manipulation tasks.
- **p. 2 / 1. Introduction - extractive body cue:** Despite their effectiveness, existing CoT-based methods face two fundamental challenges.
- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, we propose Latent Reasoning VLA (LaRA-VLA), a unified latent-reasoning VLA framework that performs reasoning and prediction entirely in latent space for ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Despite their effectiveness, existing CoT-based methods face two fundamental challenges. | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | Vision-Language-Action (VLA) models have emerged as a promising direction for scalable, general-purpose robotic manipulation (Kim et al., 2025b; Bai et al., 2025b), ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | Vision-Language-Action, VLA, models, have, emerged, promising, direction, scalable, general-purpose, robotic | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | Specifically, employ, inverse, dynamics, function, estimates, action, induces | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: Vision-Language-Action, VLA, models, have, emerged, promising, direction, scalable, general-purpose, robotic | p. 1 (1. Introduction), p. 4 (3.3. Training Procedures), p. 5 (3.3. Training Procedures) |
| Decision / output variable | action, pose, option or chunk a; body terms: contributions, threefold, introduce, latent-reasoning, paradigm, VisionLanguage-Action, models, chain-of-thought | p. 2 (1. Introduction), p. 4 (3.2. Model Architecture), p. 2 (1. Introduction) |
| Objective / loss / cost | policy/action modeling objective; cue terms: Concretely, action, tokens, trained, autoregressive, objective, similar, Equation | p. 5 (3.3. Training Procedures), p. 5 (3.3. Training Procedures), p. 4 (3.3. Training Procedures), p. 6 (3.3. Training Procedures), p. 6 (3.3. Training Procedures) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (3.3. Training Procedures), p. 6 (3.3. Training Procedures), p. 4 (3.2. Model Architecture) |
| Success / guarantee | instruction-conditioned task success | p. 7 (4.1. Simulation Experiments), p. 9 (Figure/Table caption), p. 7 (4.1. Simulation Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, we propose Latent Reasoning VLA (LaRA-VLA), a unified latent-reasoning VLA framework that performs reasoning and prediction entirely in latent space for ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 4 (3.2. Model Architecture), p. 2 (1. Introduction), p. 4 (3. Method), p. 6 (3.3. Training Procedures)): Our contributions are threefold: • We introduce a latent-reasoning paradigm for VisionLanguage-Action models, in which chain-of-thought reasoning is internalized into continuous latent representations across textual and visual modalitie ...

- **p. 4 / 3.2. Model Architecture - extractive body cue:** To predict visual goal information, we introduce a dedicated <img next> token to represent predicted visual latents, which enables explicit supervision and alignment during early-stage ...
- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, we propose Latent Reasoning VLA (LaRA-VLA), a unified latent-reasoning VLA framework that performs reasoning and prediction entirely in latent space for ...
- **p. 4 / 3. Method - extractive body cue:** In this section, we present the complete pipeline of our Latent Reasoning VLA (LaRA-VLA) framework.
- **p. 6 / 3.3. Training Procedures - extractive body cue:** We introduce an attention mechanism tailored to our three-stage training paradigm, as illustrated in Figure 3.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | This suggests that the learned latent space does not collapse or become highly unstable under visual perturbations. | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Although LaRA-VLA achieves fast inference and strong performance through latent chain-of-thought reasoning, several limitations remain and warrant further ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Improving training efficiency while preserving stable latent reasoning remains an important direction for future work. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Table 4. Robustness under visual perturbations. We report task success rates under Gaussian blur and Gaussian noise with ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 1 (1. Introduction), p. 4 (3.3. Training Procedures), p. 5 (3.3. Training Procedures), p. 5 (3.3. Training Procedures). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 1 (1. Introduction), p. 4 (3.3. Training Procedures), p. 5 (3.3. Training Procedures), p. 5 (3.3. Training Procedures), objective p. 5 (3.3. Training Procedures), p. 5 (3.3. Training Procedures), p. 4 (3.3. Training Procedures), p. 6 (3.3. Training Procedures), p. 6 (3.3. Training Procedures).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
