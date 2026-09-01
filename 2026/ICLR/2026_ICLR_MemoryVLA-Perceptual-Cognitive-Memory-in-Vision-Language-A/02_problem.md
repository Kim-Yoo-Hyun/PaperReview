# Problem - MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (36 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=54U3XHf7qq; PDF retrieval source: https://openreview.net/pdf/df1ca9dfbbf5ff164113332379a9cfa71dbf1958.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION)): However, mainstream VLA models such as OpenVLA (Kim et al., 2024) and π0 (Black et al., 2024) rely solely on the current observation, thereby overlooking temporal dependencies and performing poorly ...

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive PDF cue:** Temporal context is essential for robotic manipulation because such tasks are inherently non-Markovian, yet mainstream VLA models typically overlook it and struggle with long-horizon, temporally ...
- **p. 1 / ABSTRACT - extractive PDF cue:** Cognitive science suggests that humans rely on working memory to buffer short-lived representations for immediate control, while the hippocampal system preserves verbatim episodic details and ...
- **p. 1 / ABSTRACT - extractive PDF cue:** Inspired by these mechanisms, we propose MemoryVLA, a Cognition-Memory-Action framework for long-horizon robotic manipulation.
- **p. 1 / ABSTRACT - extractive PDF cue:** A pretrained VLM encodes the observation into perceptual and cognitive tokens that form working memory, while a Perceptual-Cognitive Memory Bank stores low-level details and highlevel ...
- **p. 1 / ABSTRACT - extractive PDF cue:** Working memory retrieves decision-relevant entries from the bank, adaptively fuses them with current tokens, and updates the bank by merging redundancies.
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** However, mainstream VLA models such as OpenVLA (Kim et al., 2024) and π0 (Black et al., 2024) rely solely on the current observation, thereby overlooking ...
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** However, it faces two critical limitations: (1) The quadratic complexity of self-attention severely limits the usable temporal context length; (2) Sequential frame inputs are misaligned ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, mainstream VLA models such as OpenVLA (Kim et al., 2024) and π0 (Black et al., 2024) rely solely on the current ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | Given the current RGB image I ∈RH×W ×3 and a language instruction L, a parameterized policy π outputs a sequence of future ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | Given, current, RGB, image, language, instruction, parameterized, policy, outputs, sequence | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | First, vision, encoder, extracts, perceptual, tokens, observation, while | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: Given, current, RGB, image, language, instruction, parameterized, policy, outputs, sequence | p. 4 (3 METHOD), p. 4 (3 METHOD), p. 2 (1 INTRODUCTION) |
| Decision / output variable | action, pose, option or chunk a; body terms: contributions, summarized, follows, Inspired, human, memory, systems, cognitive | p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION) |
| Objective / loss / cost | policy/action modeling objective; cue terms: model, trained, mean, squared, error, MSE, loss, between | p. 5 (3 METHOD), p. 6 (3 METHOD), p. 5 (3 METHOD), p. 6 (3 METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (3 METHOD), p. 6 (3 METHOD), p. 5 (3 METHOD) |
| Success / guarantee | instruction-conditioned task success | p. 19 (Figure/Table caption), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** However, it faces two critical limitations: (1) The quadratic complexity of self-attention severely limits the usable temporal context length; (2) Sequential frame inputs are misaligned ...
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** Robotic manipulation is inherently non-Markovian, and neglecting history leads to failures on long-horizon temporal tasks.
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** In contrast, π0 (Black et al., 2024), CogACT (Li et al., 2024a), DexVLA (Wen et al., 2025) and HybridVLA (Liu et al., 2025c) adopt diffusion-based ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** First, a vision encoder extracts perceptual tokens from observation, while a large language model (LLM) processes them together with the language instruction, leveraging commonsense priors ...

## What the Paper Changes

PDF contribution framing (p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 4 (3 METHOD), p. 4 (3 METHOD)): Our contributions are summarized as follows: • Inspired by human memory systems from cognitive science, we propose MemoryVLA, a Cognition-Memory-Action framework that leverages VLM commonsense priors, a perceptualcognitive memory mechan ...

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Drawing on cognitive science insights, we propose MemoryVLA (Fig.
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** For real-world evaluations, we introduce 12 tasks across Franka and WidowX robots, spanning 6 general tasks and 6 long-horizon temporal tasks.
- **p. 4 / 3 METHOD - extractive PDF cue:** To complement this short-term store, we introduce the Perceptual-Cognitive Memory Bank (PCMB), inspired by the hippocampus, which maintains long-term high-level semantics and fine-grained perceptual details.
- **p. 4 / 3 METHOD - extractive PDF cue:** Given the current RGB image I ∈RH×W ×3 and a language instruction L, a parameterized policy π outputs a sequence of future actions A = ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 18 | Figure 5: Robustness and generalization under out-of-distribution (OOD) conditions in real- world. (a,b) Examples of OOD variants for ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 19 | Figure 6: Robustness and generalization under out-of-distribution (OOD) variants in simula- tion: Pick and Move tasks. (a) Pick ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 20 | Figure 7: Robustness and generalization under out-of-distribution (OOD) variants in simu- lation: Hinge-like object manipulation. (a) OOD variants ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 25 | Table 11: Ablation on the Number of Cognitive Tokens. Increasing the number of cognitive tokens from 1 to ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (3 METHOD), p. 4 (3 METHOD), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), interface p. 4 (3 METHOD), p. 4 (3 METHOD), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), objective p. 5 (3 METHOD), p. 6 (3 METHOD), p. 5 (3 METHOD), p. 6 (3 METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
