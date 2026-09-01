# Problem - RoboOmni: Actions Are Just Another Modality for Vision-Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=qdXOfyGMuB; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/326105. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction)): However, a critical challenge has emerged: while built upon highly capable VLMs, many current VLA implementations struggle to retain the broad generalization abilities inherent in their parent models.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Integrating Vision-Language Models (VLMs) into robotics has facilitated the development of generalizable Vision-Language Action (VLA) policies.
- **p. 1 / Abstract - extractive PDF cue:** However, unified discrete frameworks lag behind decoupled continuous designs due to limitations in action chunking and temporal modeling.
- **p. 1 / Abstract - extractive PDF cue:** To address this, we introduce RoboOmni, a unified multi-modal next-token prediction framework.
- **p. 1 / Abstract - extractive PDF cue:** Challenging the assumption that continuous modeling is essential for high-performance manipulation, RoboOmni demonstrates that actions are just another modality capable of being effectively modeled discretely.
- **p. 1 / Abstract - extractive PDF cue:** At the core of our method is Multi-Token Action Prediction (MTAP), which integrates action chunking directly into the discrete tokenizer.
- **p. 1 / 1. Introduction - extractive PDF cue:** However, a critical challenge has emerged: while built upon highly capable VLMs, many current VLA implementations struggle to retain the broad generalization abilities inherent in ...
- **p. 1 / 1. Introduction - extractive PDF cue:** The generalization gap between the VLM backbone and the downstream VLA is tied to the underlying architectural design and training paradigm (Li et al., 2026).

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, a critical challenge has emerged: while built upon highly capable VLMs, many current VLA implementations struggle to retain the broad generalization ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | The model processes multi-modal interleaved input sequences comprising visual observations (V ), text instructions (T), robot states (S), and actions (A). | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | model, processes, multi-modal, interleaved, input, sequences, comprising, visual, observations, text | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | RoboOmni, preserves, standard, VLM-style, next-token, prediction, backbone, where | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: model, processes, multi-modal, interleaved, input, sequences, comprising, visual, observations, text | p. 4 (3.1. MTAP for Action Chunking), p. 5 (3.2. Multi-Modal Action Co-Training), p. 5 (3.3. Training VLA as VLM) |
| Decision / output variable | action, pose, option or chunk a; body terms: overcome, challenges, introduce, versatile, Multi-Token, Action, Prediction, MTAP | p. 3 (3.1. MTAP for Action Chunking), p. 2 (1. Introduction), p. 1 (1. Introduction) |
| Objective / loss / cost | policy/action modeling objective; cue terms: jointly, optimizing, diverse, objectives, alongside, primary, action, prediction | p. 4 (3.1. MTAP for Action Chunking), p. 3 (3.1. MTAP for Action Chunking), p. 4 (3.1. MTAP for Action Chunking), p. 5 (3.2. Multi-Modal Action Co-Training), p. 5 (3.3. Training VLA as VLM) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3.2. Multi-Modal Action Co-Training), p. 4 (3.1. MTAP for Action Chunking), p. 3 (3.1. MTAP for Action Chunking) |
| Success / guarantee | instruction-conditioned task success | p. 8 (4.4. Ablation Study), p. 7 (4.3. Real Robot Experiments), p. 7 (4.2. Evaluation on SimplerEnv) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive PDF cue:** The generalization gap between the VLM backbone and the downstream VLA is tied to the underlying architectural design and training paradigm (Li et al., 2026).
- **p. 2 / 1. Introduction - extractive PDF cue:** Our experiments show that such interleaved, long-context multi-modal training significantly improves performance and generalization, highlighting the importance of both temporal context and cross-modal fusion.

## What the Paper Changes

PDF contribution framing (p. 3 (3.1. MTAP for Action Chunking), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.2. Multi-Modal Action Co-Training)): To overcome these challenges, we introduce a versatile Multi-Token Action Prediction (MTAP) framework that enables efficient, parallelized action prediction within a unified discrete architecture.

- **p. 2 / 1. Introduction - extractive PDF cue:** This design enables long-context, multimodal co-training and allows the model to explicitly reason over historical observations and actions.
- **p. 1 / 1. Introduction - extractive PDF cue:** To overcome these limitations, we present RoboOmni, a 1
- **p. 2 / 1. Introduction - extractive PDF cue:** Specifically, we introduce Multi-Token Action Prediction (MTAP), which performs parallel decoding of H actions by repeating only the last layer for action tokens, inspired by ...
- **p. 5 / 3.2. Multi-Modal Action Co-Training - extractive PDF cue:** To encourage short-horizon temporal reasoning and motion understanding, we introduce a 2D end-effector trace prediction task inspired by (Li et al., 2025).

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | The table evaluates models on two settings: in-distribution performance (Train: ABCD, Eval: D) and out-of-distribution generalization (Train: ABC, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Notably, the FAST variant exhibits superior out-of-distribution generalization (ABC→D), suggesting the frequency-domain representation effectively offloads temporal modeling pressure ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Robust Generalization to Novel Scenarios. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | RoboOmni demonstrates superior robustness to visual domain shifts compared to baselines. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (3.1. MTAP for Action Chunking), p. 5 (3.2. Multi-Modal Action Co-Training), p. 5 (3.3. Training VLA as VLM), p. 2 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), interface p. 4 (3.1. MTAP for Action Chunking), p. 5 (3.2. Multi-Modal Action Co-Training), p. 5 (3.3. Training VLA as VLM), p. 2 (1. Introduction), objective p. 4 (3.1. MTAP for Action Chunking), p. 3 (3.1. MTAP for Action Chunking), p. 4 (3.1. MTAP for Action Chunking), p. 5 (3.2. Multi-Modal Action Co-Training), p. 5 (3.3. Training VLA as VLM).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
