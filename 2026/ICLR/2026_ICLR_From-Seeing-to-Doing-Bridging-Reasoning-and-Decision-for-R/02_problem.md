# Problem - From Seeing to Doing: Bridging Reasoning and Decision for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (34 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=yngvAamNQi; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/245158. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION)): FSD unlocks visual aids reasoning and generation through Spatial RelationshipFocused CoT, demonstrating exceptional generalization capabilities that enable zero-shot robot manipulation and achieving remarkable performance across multipl ...

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive body cue:** Achieving generalization in robotic manipulation remains a critical challenge, particularly for unseen scenarios and novel tasks.
- **p. 1 / ABSTRACT - extractive body cue:** Current Vision-Language-Action (VLA) models, while building on top of general Vision-Language Models (VLMs), still fall short of achieving robust zero-shot performance due to the scarcity ...
- **p. 1 / ABSTRACT - extractive body cue:** To address these limitations, we propose FSD (From Seeing to Doing), a novel vision-language model that generates intermediate representations through spatial relationship reasoning, providing fine-grained ...
- **p. 1 / ABSTRACT - extractive body cue:** Our approach combines a hierarchical data construction pipeline for training with a self-consistency mechanism that aligns spatial coordinates with visual signals.
- **p. 1 / ABSTRACT - extractive body cue:** Through extensive experiments, we comprehensively validated FSD's capabilities in both "seeing" and "doing", achieving outstanding performance across 8 benchmarks for general spatial reasoning and embodied ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** FSD unlocks visual aids reasoning and generation through Spatial RelationshipFocused CoT, demonstrating exceptional generalization capabilities that enable zero-shot robot manipulation and achieving remarkable performance across ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** We attribute the limited generalization in existing VLA-based systems to two fundamental challenges: data scarcity and heterogeneity.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | FSD unlocks visual aids reasoning and generation through Spatial RelationshipFocused CoT, demonstrating exceptional generalization capabilities that enable zero-shot robot manipulation and achieving ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | A driving force behind robotics research is the pursuit of generalization: creating agents capable of versatile action across diverse robotic platforms, extending ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | driving, force, behind, robotics, research, pursuit, generalization, creating, agents, capable | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | TRAINING, ACTION, EXECUTION, FSD, adopt, instruction, tuning, pipeline | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: driving, force, behind, robotics, research, pursuit, generalization, creating, agents, capable | p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 6 (4. How to avoid collisions?) |
| Decision / output variable | action, pose, option or chunk a; body terms: FSD, Seeing, Doing, novel, framework, generates, visual, intermediate | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 4 (4. How to avoid collisions?) |
| Objective / loss / cost | policy/action modeling objective; cue terms: Subsequently, optimize, path, trajectory, gradient, descent-based, interpolation, generating | p. 6 (4. How to avoid collisions?) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (4. How to avoid collisions?), p. 4 (4. How to avoid collisions?), p. 5 (4. How to avoid collisions?) |
| Success / guarantee | instruction-conditioned task success | p. 8 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 INTRODUCTION - extractive body cue:** We attribute the limited generalization in existing VLA-based systems to two fundamental challenges: data scarcity and heterogeneity.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** To bridge this generalization gap, the community has explored several paradigms.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** FSD is an enhanced affordance-based VLA that generalizes effectively to new instructions and scenes through its reasoning abilities.

## What the Paper Changes

PDF body contribution framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 4 (4. How to avoid collisions?), p. 4 (4. How to avoid collisions?), p. 5 (4. How to avoid collisions?)): To this end, we propose FSD (From Seeing to Doing), a novel framework that generates these visual intermediate representations through structured spatial reasoning (Fig.

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our contributions include: 1) A novel paradigm where VLM reasoning generates versatile visual aids, enabling either direct open-loop control or serving as the high-level planner ...
- **p. 4 / 4. How to avoid collisions? - extractive body cue:** Based on these considerations, we introduce Spatial Relationship-Focused Visual Chain-of-thought (SrCoT).
- **p. 4 / 4. How to avoid collisions? - extractive body cue:** While VLMs struggle to directly map future actions to image coordinates, our method leverages known object relationships as reference points for multi-hop analysis, simplifying the ...
- **p. 5 / 4. How to avoid collisions? - extractive body cue:** Therefore, we propose a self-consistency mechanism to further align FSD capabilities in 5

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 10 | More limitations and future works are in App.J. | reported limitation/failure wording; scope must be verified |
| body cue at p. 34 | Figure 17: Visual comparison demonstrating the effectiveness of Self-Consistency Alignment. It is worth noting that without self-consistent alignment, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 2 | Figure 1: Overview of FSD. FSD unlocks visual aids reasoning and generation through Spatial Relationship- Focused CoT, demonstrating ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | We acknowledge limitations, such as the reliance on 2D trajectory generation and constraints from training data quality. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 6 (4. How to avoid collisions?), p. 4 (4. How to avoid collisions?). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), interface p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 6 (4. How to avoid collisions?), p. 4 (4. How to avoid collisions?), objective p. 6 (4. How to avoid collisions?).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
