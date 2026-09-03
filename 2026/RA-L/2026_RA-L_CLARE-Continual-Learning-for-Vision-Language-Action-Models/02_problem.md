# Problem - CLARE: Continual Learning for Vision-Language-Action Models via Autonomous Adapter Routing and Expansion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2601.09512; PDF retrieval source: https://arxiv.org/pdf/2601.09512. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (III. PROBLEM SETUP), p. 3 (III. PROBLEM SETUP)): However, state-of-the-art VLAs still cannot adapt reliably to unseen tasks without fine-tuning on task-specific data [6]- [8].

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** To teach robots complex manipulation tasks, a common approach is to fine-tune a pre-trained vision-languageaction model (VLA) on task-specific data.
- **p. 1 / Abstract - extractive body cue:** However, since this recipe updates existing representations, it is unsuitable for longterm operation in the real world, where robots must continually adapt to new tasks ...
- **p. 1 / Abstract - extractive body cue:** Existing continual learning methods for robotics commonly require storing previous data (exemplars), struggle with long task sequences, or rely on task identifiers for deployment.
- **p. 1 / Abstract - extractive body cue:** To address these limitations, we propose CLARE, a general, parameter-efficient framework for exemplar-free continual learning with VLAs.
- **p. 1 / Abstract - extractive body cue:** CLARE introduces lightweight modular adapters into selected VLA modules and autonomously expands the model only where necessary when learning a new task, guided by layer-wise ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, state-of-the-art VLAs still cannot adapt reliably to unseen tasks without fine-tuning on task-specific data [6]- [8].
- **p. 1 / I. INTRODUCTION - extractive body cue:** This long-term adaptability, known as continual or lifelong learning [1], remains an open challenge in robotics despite decades of research [2]-[4].

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, state-of-the-art VLAs still cannot adapt reliably to unseen tasks without fine-tuning on task-specific data [6]- [8]. | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | 23: Train Dn ℓof all layers ℓ∈E from Dn via (5). consisting of camera images I1 t , . . . , ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | Train, layers, consisting, camera, images, INc, proprioceptive, state, language, command | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | Specifically, given, expert, demonstration, dataset, observation-action, pairs, task | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: Train, layers, consisting, camera, images, INc, proprioceptive, state, language, command | p. 3 (III. PROBLEM SETUP), p. 2 (III. PROBLEM SETUP), p. 3 (III. PROBLEM SETUP) |
| Decision / output variable | action, pose, option or chunk a; body terms: architecture-agnostic, keep, following, sections, general, found, introducing, least | p. 3 (IV. METHODOLOGY), p. 5 (IV. METHODOLOGY) |
| Objective / loss / cost | policy/action modeling objective; cue terms: adopt, standard, conditional, flow, matching, loss, First, jointly | p. 3 (IV. METHODOLOGY), p. 4 (IV. METHODOLOGY), p. 4 (IV. METHODOLOGY), p. 5 (IV. METHODOLOGY) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (IV. METHODOLOGY), p. 4 (IV. METHODOLOGY), p. 5 (IV. METHODOLOGY) |
| Success / guarantee | instruction-conditioned task success | p. 10 (Figure/Table caption), p. 6 (V. EVALUATION), p. 6 (V. EVALUATION) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** This long-term adaptability, known as continual or lifelong learning [1], remains an open challenge in robotics despite decades of research [2]-[4].
- **p. 3 / III. PROBLEM SETUP - extractive body cue:** Pre-training has provided the base VLA with general visual, language, and action representations, but it cannot solve new tasks zero-shot [6], [7].
- **p. 3 / III. PROBLEM SETUP - extractive body cue:** 17: else 18: Link Dn ℓto an existing adapter via (8).

## What the Paper Changes

PDF body contribution framing (p. 3 (IV. METHODOLOGY), p. 5 (IV. METHODOLOGY)): As our method is architecture-agnostic, we keep the following sections general.

- **p. 5 / IV. METHODOLOGY - extractive body cue:** We found that introducing at least some new parameters per task is essential for the policy to acquire and retain novel skills.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | In contrast, ER cannot avoid catastrophic forgetting of several tasks (e.g., T1 and T7), yielding an NBT of ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | SeqFFT and SeqLoRA achieve high performance on new tasks, but cannot sufficiently retain the relevant representations from previous ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | 5: Increasing the dynamic expansion threshold γ reduces the number of added adapters and, consequently, the capability to ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | As shown in Figure 4, CLARE can sequentially learn and retain 40 distinct tasks, demonstrating the scalability and ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (III. PROBLEM SETUP), p. 2 (III. PROBLEM SETUP), p. 3 (III. PROBLEM SETUP), p. 2 (III. PROBLEM SETUP). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (III. PROBLEM SETUP), p. 3 (III. PROBLEM SETUP), interface p. 3 (III. PROBLEM SETUP), p. 2 (III. PROBLEM SETUP), p. 3 (III. PROBLEM SETUP), p. 2 (III. PROBLEM SETUP), objective p. 3 (IV. METHODOLOGY), p. 4 (IV. METHODOLOGY), p. 4 (IV. METHODOLOGY), p. 5 (IV. METHODOLOGY).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
