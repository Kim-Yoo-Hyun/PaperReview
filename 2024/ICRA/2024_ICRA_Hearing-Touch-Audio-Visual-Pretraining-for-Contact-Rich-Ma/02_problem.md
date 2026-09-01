# Problem - Hearing Touch: Audio-Visual Pretraining for Contact-Rich Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2405.08576; PDF retrieval source: https://arxiv.org/pdf/2405.08576. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): This gap arises due to the lack of relevant data at a comparable scale for tactile sensing.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Although pre-training on a large amount of data is beneficial for robot learning, current paradigms only perform large-scale pretraining for visual representations, whereas representations for ...
- **p. 1 / Abstract - extractive PDF cue:** In contrast to the abundance of visual data, it is unclear what relevant internet-scale data may be used for pretraining other modalities such as tactile ...
- **p. 1 / Abstract - extractive PDF cue:** Such pretraining becomes increasingly crucial in the low-data regimes common in robotics applications.
- **p. 1 / Abstract - extractive PDF cue:** In this paper, we address this gap by using contact microphones as an alternative tactile sensor.
- **p. 1 / Abstract - extractive PDF cue:** Our key insight is that contact microphones capture inherently audio-based information, allowing us to leverage large-scale audio-visual pretraining to obtain representations that boost the performance ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** This gap arises due to the lack of relevant data at a comparable scale for tactile sensing.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** As a result, current approaches using non-visual sensory modalities are restricted to learning from a limited amount of task-specific data [10], [12].

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | This gap arises due to the lack of relevant data at a comparable scale for tactile sensing. | contact-rich manipulation scene | body wording is the source claim |
| Observation / input | Initializing our encoder with AVID weights, we train a policy with behavior cloning that fuses visual and audio inputs with self-attention in ... | tactile image/force, vision과 proprioceptive history | exact sensor/frame/preprocessing from PDF |
| State / latent | Initializing, encoder, AVID, weights, train, policy, behavior, cloning, fuses, visual | contact geometry, force state 또는 latent dynamics | notation and tensor shape require body check |
| Output / action | particular, final, component, network, multi-layer, perceptron, outputs, actions | grasp/contact action, force command 또는 object motion | exact unit/frame/decoder require body check |
| Target outcome | slip/contact success and safe interaction | slip/contact success, force/pose error와 robustness | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | visual/tactile/proprioceptive contact history; body terms: Initializing, encoder, AVID, weights, train, policy, behavior, cloning, fuses, visual | p. 1 (I. INTRODUCTION), p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING), p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING) |
| Decision / output variable | contact-aware action/force; body terms: makes, Audio-Visual, Instance, Discrimination, AVID, selfsupervised, learning, learn | p. 1 (I. INTRODUCTION), p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING), p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING) |
| Objective / loss / cost | contact prediction/control error; cue terms: optimize, network, minimize, standard, MSE, loss, vt-i, Following | p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING), p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING), p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING) |
| Success / guarantee | slip/contact success and safe interaction | p. 5 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** As a result, current approaches using non-visual sensory modalities are restricted to learning from a limited amount of task-specific data [10], [12].

## What the Paper Changes

PDF contribution framing (p. 1 (I. INTRODUCTION), p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING), p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING), p. 1 (I. INTRODUCTION), p. 2 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING)): Our method makes use of Audio-Visual Instance Discrimination (AVID) [14], a selfsupervised learning approach to learn audio-visual representations, pre-trained on Audioset [15], a dataset containing 1Robotics Institute, Carnegie Mellon ...

- **p. 3 / III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING - extractive PDF cue:** Similar to [41], [42] our method is quasi open-loop-at time step t the policy predicts H steps of actions, of which h ≤H steps of ...
- **p. 3 / III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING - extractive PDF cue:** Audio and Visual Representation Pretraining Our method uses large-scale audio-visual pre-training to initialize our audio encoder and large-scale visual pretraining to initialize our visual encoder.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Furthermore, our approach outperforms equivalent policies with audio encoders trained from scratch.
- **p. 2 / III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING - extractive PDF cue:** We outline further details of our approach in the following sections.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | Future work may investigate which properties of pre-training datasets are most conducive to learning audio-visual representations for manipulation ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | As a result, the baselines suffer heavily from the domain shift and fail to generalize, often moving in ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | Further, our method outperforms or matches the performance of all baselines in 8/9 tasks, displaying a lower variation ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Despite having access to the same information as our method, the BYOL-A and Scratch baselines fail to reason ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

tactile writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 1 (I. INTRODUCTION), p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING), p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING), p. 2 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), interface p. 1 (I. INTRODUCTION), p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING), p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING), p. 2 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING), objective p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING), p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
