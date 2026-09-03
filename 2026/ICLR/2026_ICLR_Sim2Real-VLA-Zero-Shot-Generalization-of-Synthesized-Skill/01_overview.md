# Sim2Real VLA: Zero-Shot Generalization of Synthesized Skills to Realistic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=H4SyKHjd4c.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/247063. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, Robotics
- Official paper: https://openreview.net/forum?id=H4SyKHjd4c
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/247063
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, it lacks principled studies on redesigning VLA models to close the Sim2Real gap.를 문제로 두고, These findings call for an alternative approach: instead of focusing on generating high-fidelity data, we propose addressing the Sim2Real by redesigning the VLA architecture.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Vision-Language-Action (VLA) models represent a critical milestone toward embodied intelligence in robotic manipulation.
- **p. 1 / ABSTRACT - extractive body cue:** To support their training, recent research has developed high-performance simulation engines for data synthesis.
- **p. 1 / ABSTRACT - extractive body cue:** However, their effectiveness is still significantly limited by the simulation-to-reality (Sim2Real) gap, as policies trained on synthetic data often fail to generalize reliably to the ...
- **p. 1 / ABSTRACT - extractive body cue:** To address this challenge, we present Sim2Real-VLA, a generalist robot control model trained exclusively on synthetic data, yet capable of transferring seamlessly to real-world manipulation ...
- **p. 1 / ABSTRACT - extractive body cue:** Sim2Real-VLA features a dual-system architecture: a high-level planner that infers chains-ofaffordances, and a low-level actor that executes and validates these plans in real time via ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** However, it lacks principled studies on redesigning VLA models to close the Sim2Real gap.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** However, as demonstrated by prior studies (Nasiriany et al., 2024; Wang et al., 2024a), the discrepancy between the simulated environment c M and the real-world ...

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** These findings call for an alternative approach: instead of focusing on generating high-fidelity data, we propose addressing the Sim2Real by redesigning the VLA architecture.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this study, we introduce Sim2Real-VLA, which, despite being trained solely on synthetic data, demonstrates generalizable and sustained manipulation performance across diverse real-world environments.
- **p. 6 / 1 INTRODUCTION - extractive body cue:** We present more details in Appendix A.4.
- **p. 7 / 1 INTRODUCTION - extractive body cue:** In this study, we evaluate our method using the manipulation tasks summarized in Table 2.
- **p. 8 / 1 INTRODUCTION - extractive body cue:** In particular, our method attains an average real-world success rate of 60.8%, significantly outperforming the best baseline with an absolute improvement of over 35%.
- **p. 16 / A.1 MODEL ARCHITECTURE & KEY PARAMETERS - extractive body cue:** Utilizing a tokenize-thenconcatenate strategy, the model fuses these action embeddings with the predicted affordance outputs.
- **p. 16 / A.1 MODEL ARCHITECTURE & KEY PARAMETERS - extractive body cue:** This architecture is complemented by two additional transformer blocks of identical configuration dedicated to affordance inference and guidance, alongside multiple MLP adapters that facilitate dimensional ...
- **p. 17 / A.1 MODEL ARCHITECTURE & KEY PARAMETERS - extractive body cue:** Constructed as a regressive transformer classifier, the validtion modeal takes maksed visual observation and state as input, current target affordance as condation, and output a ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Constructed as a regressive transformer classifier, the validtion modeal takes maksed visual observation and state as input, current target affordance as condation, and output a validation signal to label if the target ... | image/video, language instruction, proprioception과 history | p. 17 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS), p. 3 (1 INTRODUCTION) |
| State/latent | Constructed, regressive, transformer, classifier, validtion, modeal, takes, maksed, visual, observation, state, input | language-grounded task state와 action-policy context | p. 17 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS), p. 3 (1 INTRODUCTION), p. 16 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS) |
| Output/action | Within the robot's operational environment, our objective is to learn a control policy π(at, . . . , at+M / ot-H, . . . , ot, l) that predicts a sequence of ... | continuous action, pose 또는 action chunk | p. 3 (1 INTRODUCTION), p. 16 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS), p. 16 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS) |
| Objective/outcome | When more detailed or nuanced reward structures are needed, AI agents can design sophisticated reward functions (Ma et al., 2024a). | instruction following, task success, generalization과 latency | p. 17 (A.2 CONFIGURING REWARDS IN VLA MODELS), p. 17 (A.2 CONFIGURING REWARDS IN VLA MODELS) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** These findings call for an alternative approach: instead of focusing on generating high-fidelity data, we propose addressing the Sim2Real by redesigning the VLA architecture.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this study, we introduce Sim2Real-VLA, which, despite being trained solely on synthetic data, demonstrates generalizable and sustained manipulation performance across diverse real-world environments.
- **p. 6 / 1 INTRODUCTION - extractive body cue:** We present more details in Appendix A.4.
- **p. 7 / 1 INTRODUCTION - extractive body cue:** In this study, we evaluate our method using the manipulation tasks summarized in Table 2.
- **p. 8 / 1 INTRODUCTION - extractive body cue:** In particular, our method attains an average real-world success rate of 60.8%, significantly outperforming the best baseline with an absolute improvement of over 35%.
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 4: Visualization of environment configurations under the domain gaps of background texture, object features, and table texture across different manipulation tasks. Table 4 illustrates ...
- **p. 24 / Figure/Table caption - extractive body cue:** Figure 8: Data Efficiency Scaling. Success rates (at 40k steps) vs. number of real demonstrations. Baselines improve monotonically. Our method shows a "dip" at 5 ...
- **p. 25 / Figure/Table caption - extractive body cue:** Figure 9: Analysis of Training Dynamics and Efficiency. (a-b) Training curves of Sim2Real VLA under different data strategies. The Sim-then-Real (10 eps) strategy yields the ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 9 (Figure/Table caption), p. 24 (Figure/Table caption) |
| Embodiment/environment | Given either an egocentric video of a human manipulating objects or teleoperated demonstrations performed in the real environment, we project both the actions and object interactions onto robot control signals within a ... | hardware/simulator version and reset protocol | p. 17 (A.3 DETAILS ON REAL2SIM DATA PROJECTION), p. 17 (A.3 DETAILS ON REAL2SIM DATA PROJECTION) |
| Dataset/benchmark | Through the implementation of joint training and domain randomization, the module ensures robust generalization across diverse objects and environmental conditions. | role, split, size and leakage | p. 17 (A.3 DETAILS ON REAL2SIM DATA PROJECTION), p. 17 (A.3 DETAILS ON REAL2SIM DATA PROJECTION), p. 16 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS), p. 18 (A.3 DETAILS ON REAL2SIM DATA PROJECTION) |
| Metric | Figure 4: Visualization of environment configurations under the domain gaps of background texture, object features, and table texture across different manipulation tasks. Table 4 illustrates the generalization ability of Sim2Real-VLA un ... | definition, denominator, direction and uncertainty | p. 9 (Figure/Table caption), p. 24 (Figure/Table caption), p. 25 (Figure/Table caption) |
| Baseline/ablation | Table 9: Success Rates with Few-Shot Real Data. Comparison across Sim Only, Real Only (10 demos), and Sim-then-Real (5/10 demos) strategies. Note the non-monotonic behavior ("dip") in our method at 5 eps ... | fair input/data/compute/action matching | p. 24 (Figure/Table caption), p. 9 (Figure/Table caption), p. 23 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 1 INTRODUCTION - extractive body cue:** For unsuccessful trials where the robot fails to complete the task, we report the predefined maximum step limit as an upper bound.
- **p. 17 / A.3 DETAILS ON REAL2SIM DATA PROJECTION - extractive body cue:** However, in cases where three-view images capture only partial scene information (e.g., occluded object surfaces), or when the retrieved scene fails to semantically align with ...
- **p. 8 / 1 INTRODUCTION - extractive body cue:** Besides, we also experiment Sim2Real-VLA robustness to the combination of these gaps.
- **p. 9 / 1 INTRODUCTION - extractive body cue:** These results indicate that the model maintains stable performance and demonstrates strong robustness to real-world differences.
- **p. 10 / 1 INTRODUCTION - extractive body cue:** These findings point toward a promising paradigm shift: building robotic foundation models that are trained entirely in simulation, yet are robust to realistic deployment.
- **p. 16 / A.1 MODEL ARCHITECTURE & KEY PARAMETERS - extractive body cue:** Through the implementation of joint training and domain randomization, the module ensures robust generalization across diverse objects and environmental conditions.
- **p. 20 / Figure/Table caption - extractive body cue:** Figure 7: Succees and fail cases of real2sim projection eamined by workspace analyzer and VLM respectively on asset and action level. 20

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, it lacks principled studies on redesigning VLA models to close the Sim2Real gap.를 문제로 두고, These findings call for an alternative approach: instead of focusing on generating high-fidelity data, we propose addressing the Sim2Real by redesigning the VLA architecture.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 8 (1 INTRODUCTION), p. 16 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
