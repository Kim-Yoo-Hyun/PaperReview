# Problem - FD-VLA: Force-Distilled Vision-Language-Action Model for Contact-Rich Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_5.html; PDF retrieval source: https://arxiv.org/pdf/2602.02142. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): This enables practical deployment on a wide range of robot platforms that lack force sensors, reducing hardware cost and ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Force sensing is a crucial modality for VisionLanguage-Action (VLA) frameworks, as it enables fine-grained perception and dexterous manipulation in contact-rich tasks.
- **p. 1 / Abstract - extractive body cue:** We present Force-Distilled VLA (FD-VLA), a novel framework that integrates force awareness into contact-rich manipulation without relying on physical force sensors.
- **p. 1 / Abstract - extractive body cue:** The core of our approach is a Force Distillation Module (FDM), which distills force by mapping a learnable query token, conditioned on visual observations and ...
- **p. 1 / Abstract - extractive body cue:** During inference, this distilled force token is injected into the pretrained VLM, enabling force-aware reasoning while preserving the integrity of its vision-language semantics.
- **p. 1 / Abstract - extractive body cue:** This design provides two key benefits: first, it allows practical deployment across a wide range of robots that lack expensive or fragile force-torque sensors, thereby ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** This enables practical deployment on a wide range of robot platforms that lack force sensors, reducing hardware cost and ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Moreover, the late-fusion mechanism limits fine-grained forcevision-state interactions, reducing tight perception-action coupling and generalization.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | This enables practical deployment on a wide range of robot platforms that lack force sensors, reducing hardware cost and 20 ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | The multimodal inputs of VLA include language instruction L, visual observation Vt, robot state St, and force Ft, where t denotes the ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | multimodal, inputs, VLA, include, language, instruction, visual, observation, robot, state | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | summary, main, contributions, summarized, follows, FD-VLA, framework, injects | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: multimodal, inputs, VLA, include, language, instruction, visual, observation, robot, state | p. 3 (III. METHODOLOGY), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Decision / output variable | action, pose, option or chunk a; body terms: summary, main, contributions, summarized, follows, FD-VLA, framework, injects | p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (III. METHODOLOGY) |
| Objective / loss / cost | policy/action modeling objective; cue terms: Overall, Training, Objective, FD-VLA, framework, combines, complementary, components | p. 5 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 5 (III. METHODOLOGY) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 5 (III. METHODOLOGY) |
| Success / guarantee | instruction-conditioned task success | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 2 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** Moreover, the late-fusion mechanism limits fine-grained forcevision-state interactions, reducing tight perception-action coupling and generalization.

## What the Paper Changes

PDF body contribution framing (p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY)): In summary, the main contributions of this work are summarized as follows: • We propose the FD-VLA framework that injects a distilled force token into the VLA model to improve ...

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we propose a novel FD-VLA framework that incorporates a distilled force token, rather than raw sensor signals, into the VLA model to ...
- **p. 3 / III. METHODOLOGY - extractive body cue:** Motivated by these challenges, we propose FD-VLA guided by three design principles: (i) leverage predicted force tokens obtained through distillation with actual force signals during ...
- **p. 4 / III. METHODOLOGY - extractive body cue:** The realization of FDM consists of two parallel branches, i.e., the prediction branch and actual force branch.
- **p. 4 / III. METHODOLOGY - extractive body cue:** Rather than directly incorporating the raw force measurements into the VLM, we introduce the Force Distillation Module (FDM) that can predict a latent force representation ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 2 | Fig. 1: Overview of differentiate architectures of force VLAs. (Left) Tactile-VLA with tactile encoder directly encode tactile information. ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | This architecture allows our system to leverage the semantic richness of pretrained VLM while introducing stable, taskrelevant physical ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | Finally, FDM mitigates the noise and instability of raw sensor signals by learning a supervised latent embedding that ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Our model achieves consistently higher performance, which highlights the benefit of force distillation for accurate and robust manipulation. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (III. METHODOLOGY), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 4 (III. METHODOLOGY). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), interface p. 3 (III. METHODOLOGY), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 4 (III. METHODOLOGY), objective p. 5 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 5 (III. METHODOLOGY).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
