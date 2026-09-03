# Problem - Sim2Real VLA: Zero-Shot Generalization of Synthesized Skills to Realistic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=H4SyKHjd4c; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/247063. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 8 (1 INTRODUCTION)): However, it lacks principled studies on redesigning VLA models to close the Sim2Real gap.

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive body cue:** Vision-Language-Action (VLA) models represent a critical milestone toward embodied intelligence in robotic manipulation.
- **p. 1 / ABSTRACT - extractive body cue:** To support their training, recent research has developed high-performance simulation engines for data synthesis.
- **p. 1 / ABSTRACT - extractive body cue:** However, their effectiveness is still significantly limited by the simulation-to-reality (Sim2Real) gap, as policies trained on synthetic data often fail to generalize reliably to the ...
- **p. 1 / ABSTRACT - extractive body cue:** To address this challenge, we present Sim2Real-VLA, a generalist robot control model trained exclusively on synthetic data, yet capable of transferring seamlessly to real-world manipulation ...
- **p. 1 / ABSTRACT - extractive body cue:** Sim2Real-VLA features a dual-system architecture: a high-level planner that infers chains-ofaffordances, and a low-level actor that executes and validates these plans in real time via ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** However, it lacks principled studies on redesigning VLA models to close the Sim2Real gap.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** However, as demonstrated by prior studies (Nasiriany et al., 2024; Wang et al., 2024a), the discrepancy between the simulated environment c M and the real-world ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, it lacks principled studies on redesigning VLA models to close the Sim2Real gap. | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | Constructed as a regressive transformer classifier, the validtion modeal takes maksed visual observation and state as input, current target affordance as condation, ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | Constructed, regressive, transformer, classifier, validtion, modeal, takes, maksed, visual, observation | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | pipeline, initiates, employing, diffusion-based, action, expert, generate, trajectories | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: Constructed, regressive, transformer, classifier, validtion, modeal, takes, maksed, visual, observation | p. 17 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS), p. 3 (1 INTRODUCTION), p. 16 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS) |
| Decision / output variable | action, pose, option or chunk a; body terms: findings, call, alternative, instead, focusing, generating, high-fidelity, data | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 6 (1 INTRODUCTION) |
| Objective / loss / cost | policy/action modeling objective; cue terms: When, more, detailed, nuanced, reward, structures, needed, agents | p. 17 (A.3 DETAILS ON REAL2SIM DATA PROJECTION) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 17 (A.2 CONFIGURING REWARDS IN VLA MODELS), p. 17 (A.2 CONFIGURING REWARDS IN VLA MODELS) |
| Success / guarantee | instruction-conditioned task success | p. 9 (Figure/Table caption), p. 24 (Figure/Table caption), p. 25 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 3 / 1 INTRODUCTION - extractive body cue:** However, as demonstrated by prior studies (Nasiriany et al., 2024; Wang et al., 2024a), the discrepancy between the simulated environment c M and the real-world ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, accurately modeling real-world dynamics remains a significant challenge that has yet to be solved (Bharadhwaj, 2024).
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address the enduring domain gap between synthesized and realistic data, Sim2Real-VLA integrates a generalization mechanism in model design.
- **p. 8 / 1 INTRODUCTION - extractive body cue:** 4) π0 (Black et al., 2024) serves as a strong pretrained policy prior that provides generalizable low-level skills across different domains.

## What the Paper Changes

PDF body contribution framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 6 (1 INTRODUCTION), p. 7 (1 INTRODUCTION), p. 8 (1 INTRODUCTION)): These findings call for an alternative approach: instead of focusing on generating high-fidelity data, we propose addressing the Sim2Real by redesigning the VLA architecture.

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this study, we introduce Sim2Real-VLA, which, despite being trained solely on synthetic data, demonstrates generalizable and sustained manipulation performance across diverse real-world environments.
- **p. 6 / 1 INTRODUCTION - extractive body cue:** We present more details in Appendix A.4.
- **p. 7 / 1 INTRODUCTION - extractive body cue:** In this study, we evaluate our method using the manipulation tasks summarized in Table 2.
- **p. 8 / 1 INTRODUCTION - extractive body cue:** In particular, our method attains an average real-world success rate of 60.8%, significantly outperforming the best baseline with an absolute improvement of over 35%.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | For unsuccessful trials where the robot fails to complete the task, we report the predefined maximum step limit ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 17 | However, in cases where three-view images capture only partial scene information (e.g., occluded object surfaces), or when the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Besides, we also experiment Sim2Real-VLA robustness to the combination of these gaps. | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | These results indicate that the model maintains stable performance and demonstrates strong robustness to real-world differences. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 17 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS), p. 3 (1 INTRODUCTION), p. 16 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS), p. 16 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 8 (1 INTRODUCTION), interface p. 17 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS), p. 3 (1 INTRODUCTION), p. 16 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS), p. 16 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS), objective p. 17 (A.3 DETAILS ON REAL2SIM DATA PROJECTION).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
