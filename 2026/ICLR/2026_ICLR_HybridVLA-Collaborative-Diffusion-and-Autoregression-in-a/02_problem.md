# Problem - HybridVLA: Collaborative Diffusion and Autoregression in a Unified Vision-Language-Action Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=H1KDMNOKQn; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/245878. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION)): Unlike prior diffusion-based VLA methods (Black et al., 2024; Li et al., 2024a) that append an independent diffusion head after the LLM (Figure 1 (a)), we introduce a collaborative training ...

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive body cue:** A central objective of manipulation policy design is to enable robots to comprehend human instructions and predict generalized actions in unstructured environments.
- **p. 1 / ABSTRACT - extractive body cue:** Recent autoregressive vision-language-action (VLA) approaches discretize actions into bins to exploit the pretrained reasoning and generation paradigms of visionlanguage models (VLMs).
- **p. 1 / ABSTRACT - extractive body cue:** While these models achieve efficient and scalable training, the discretization undermines the continuity required for precise control.
- **p. 1 / ABSTRACT - extractive body cue:** In contrast, diffusion-based VLA methods incorporate an additional diffusion head to predict continuous actions, but they rely solely on feature representations extracted from the VLM, ...
- **p. 1 / ABSTRACT - extractive body cue:** To integrate the complementary strengths of autoregressive and diffusion generation, we introduce HybridVLA, which innovatively leverages a shared LLM backbone to perform iterative action prediction ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Unlike prior diffusion-based VLA methods (Black et al., 2024; Li et al., 2024a) that append an independent diffusion head after the LLM (Figure 1 (a)), ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Recent diffusion-based VLA methods (Black et al., 2024; Li et al., 2024a; Wen et al., 2024a; Bjorck et al., 2025) incorporate a diffusion head after ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Unlike prior diffusion-based VLA methods (Black et al., 2024; Li et al., 2024a) that append an independent diffusion head after the LLM ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | A central objective of manipulation policy design is to enable robots to comprehend human instructions and predict generalized actions in unstructured environments. | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | central, objective, manipulation, policy, design, enable, robots, comprehend, human, instructions | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | Building, success, several, studies, have, extended, VLMs, vision-language-action | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: central, objective, manipulation, policy, design, enable, robots, comprehend, human, instructions | p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |
| Decision / output variable | action, pose, option or chunk a; body terms: contributions, follows, HybridVLA, innovatively, leverages, single, LLM, backbone | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |
| Objective / loss / cost | policy/action modeling objective; cue terms: contributions, follows, HybridVLA, innovatively, leverages, single, LLM, backbone | p. 1 (ABSTRACT) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 1 (ABSTRACT), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION) |
| Success / guarantee | instruction-conditioned task success | p. 7 (4 EXPERIMENT), p. 7 (12.3 Hz), p. 8 (12.3 Hz) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Recent diffusion-based VLA methods (Black et al., 2024; Li et al., 2024a; Wen et al., 2024a; Bjorck et al., 2025) incorporate a diffusion head after ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** These methods enable generalized action prediction by quantizing continuous actions into discrete bins that occupy part of the LLM's original vocabulary.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** In dynamic and unstructured real-world environments, such policies need to interpret human instructions and generalize across a wide range of complex tasks.

## What the Paper Changes

PDF body contribution framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION)): Our contributions are as follows: • We propose HybridVLA, which innovatively leverages a single LLM backbone for iterative action prediction through both autoregressive and diffusion generation within a unified token ...

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Unlike prior diffusion-based VLA methods (Black et al., 2024; Li et al., 2024a) that append an independent diffusion head after the LLM (Figure 1 (a)), ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Developing intelligent robots capable of performing manipulation tasks demands robust policies (Driess et al., 2023; Huang et al., 2023).

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | Additional qualitative results and failure case analyses are provided in Appendix D and Appendix E, respectively, and execution ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 26 | Figure 9: Single-arm Execution Visualization. We visualize key frames of the agent's execution process from the front perspective. ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Due to space limitations, Appendix C.2 provides additional ablation studies on: (1) confidence thresholds in the collaborative action ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | One limitation of HybridVLA is that its inference speed is constrained by the slower autoregressive generation, similar to ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), interface p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), objective p. 1 (ABSTRACT).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
