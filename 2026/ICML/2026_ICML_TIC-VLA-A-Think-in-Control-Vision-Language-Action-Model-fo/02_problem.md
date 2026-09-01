# Problem - TIC-VLA: A Think-in-Control Vision-Language-Action Model for Robot Navigation in Dynamic Environments

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=9wYjjPydfe; PDF retrieval source: https://openreview.net/pdf/111f8ac3ef90d847bb2191b2bd71a573458c6810.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 3 (3.1. Problem Formulation), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction)): However, existing VLA systems rely on a hidden and impractical assumption: reasoning and control are temporally aligned.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Robots in dynamic, human-centric environments must follow language instructions while maintaining real-time reactive control.
- **p. 1 / Abstract - extractive PDF cue:** Vision-languageaction (VLA) models offer a promising framework, but they assume temporally aligned reasoning and control, despite semantic inference being inherently delayed relative to real-time action.
- **p. 1 / Abstract - extractive PDF cue:** We introduce Think-in-Control (TIC)-VLA, a latency-aware framework that explicitly models delayed semantic reasoning during action generation.
- **p. 1 / Abstract - extractive PDF cue:** TIC-VLA defines a delayed semanticcontrol interface that conditions action generation on delayed vision-language semantic states and explicit latency metadata, in addition to current observations, enabling ...
- **p. 1 / Abstract - extractive PDF cue:** We further propose a latency-consistent training pipeline that injects reasoning inference delays during imitation learning and online reinforcement learning, aligning training with asynchronous deployment.
- **p. 1 / 1. Introduction - extractive PDF cue:** However, existing VLA systems rely on a hidden and impractical assumption: reasoning and control are temporally aligned.
- **p. 3 / 3.1. Problem Formulation - extractive PDF cue:** As a result, semantic outputs may become temporally misaligned with the agent's current observations and state, creating a key challenge for real-time navigation.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, existing VLA systems rely on a hidden and impractical assumption: reasoning and control are temporally aligned. | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | Specifically, we sample reasoning delays ∆t uniformly from [0, 10] seconds and condition the policy on: (1) the current image input and ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF |
| State / latent | Specifically, sample, reasoning, delays, uniformly, seconds, condition, policy, current, image | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | value, network, Figure, takes, input, current, image, tokens | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: Specifically, sample, reasoning, delays, uniformly, seconds, condition, policy, current, image | p. 5 (3.3. Latency-Consistent Training Pipeline), p. 3 (3.1. Problem Formulation), p. 5 (3.3. Latency-Consistent Training Pipeline) |
| Decision / output variable | path/waypoint/velocity; body terms: introduce, Think-in-Control, TIC, VLA, latency-aware, framework, explicitly, exposes | p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: optimize, standard, autoregressive, crossentropy, loss, over, target, token | p. 5 (3.3. Latency-Consistent Training Pipeline), p. 5 (3.3. Latency-Consistent Training Pipeline), p. 4 (3.2. Think-in-Control VLA), p. 4 (3.2. Think-in-Control VLA) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (3.1. Problem Formulation), p. 4 (3.2. Think-in-Control VLA), p. 4 (3.2. Think-in-Control VLA) |
| Success / guarantee | goal reach with collision-free execution | p. 7 (4.1. Experimental Setup), p. 9 (4.4. Ablation Study), p. 9 (4.4. Ablation Study) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 3 / 3.1. Problem Formulation - extractive PDF cue:** As a result, semantic outputs may become temporally misaligned with the agent's current observations and state, creating a key challenge for real-time navigation.
- **p. 1 / 1. Introduction - extractive PDF cue:** As a result, semantic representations frequently correspond to past world states, yet are consumed by the policy as if they were current, introducing systematic misalignment ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Most prior work on embodied navigation sidesteps this issue.
- **p. 2 / 1. Introduction - extractive PDF cue:** We argue that latency in reasoning is not merely an engineering inefficiency but a fundamental modeling problem.

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.2. Think-in-Control VLA)): To this end, we introduce Think-in-Control (TIC)-VLA, a latency-aware framework that explicitly exposes inference delay to the control policy.

- **p. 1 / 1. Introduction - extractive PDF cue:** Vision- *Equal contribution 1University of California, Los Angeles.
- **p. 1 / 1. Introduction - extractive PDF cue:** TIC-VLA enables real-time, language-conditioned navigation by decoupling slow vision-language reasoning from fast reactive control via a delayed semantic-control interface.
- **p. 2 / 1. Introduction - extractive PDF cue:** The primary contributions can be summarized as:
- **p. 4 / 3.2. Think-in-Control VLA - extractive PDF cue:** This latency-aware semantic-control coupling enables robust navigation despite asynchronous and delayed reasoning updates.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | An episode is considered a failure if manual intervention is required to prevent collisions. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Although the non-reasoning variant has a lower collision rate, this mainly reflects reduced activity and more frequent failure ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Figure 5. The effect of VLM asynchronous reasoning inference latency in TIC-VLA on task performance. fine-tuned policy maintains ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | TIC-VLA has three main limitations. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 5 (3.3. Latency-Consistent Training Pipeline), p. 3 (3.1. Problem Formulation), p. 5 (3.3. Latency-Consistent Training Pipeline), p. 3 (3.1. Problem Formulation). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 3 (3.1. Problem Formulation), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 5 (3.3. Latency-Consistent Training Pipeline), p. 3 (3.1. Problem Formulation), p. 5 (3.3. Latency-Consistent Training Pipeline), p. 3 (3.1. Problem Formulation), objective p. 5 (3.3. Latency-Consistent Training Pipeline), p. 5 (3.3. Latency-Consistent Training Pipeline), p. 4 (3.2. Think-in-Control VLA), p. 4 (3.2. Think-in-Control VLA).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
