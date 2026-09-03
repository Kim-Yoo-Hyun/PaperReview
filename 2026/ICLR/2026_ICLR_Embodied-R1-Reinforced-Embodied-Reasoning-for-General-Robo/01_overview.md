# Embodied-R1: Reinforced Embodied Reasoning for General Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=i5wlozMFsQ.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/245153. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: Vision-Language Model, Robotics, Reinforcement Learning
- Official paper: https://openreview.net/forum?id=i5wlozMFsQ
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/245153
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 This disparity is widely recognized as the "seeing-to-doing gap" (Yuan et al., 2025): a failure to reliably translate rich perceptual understanding into effective robotic actions.를 문제로 두고, To bridge this gap, we propose pointing as an intuitive and effective paradigm to connect high-level understanding with generalizable action.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Generalization in embodied AI is hindered by the "seeing-to-doing gap", stemming from data scarcity and embodiment heterogeneity.
- **p. 1 / ABSTRACT - extractive body cue:** To address this, we pioneer "pointing" as a unified, embodiment-agnostic intermediate representation, defining four core embodied pointing abilities that bridge high-level vision-language comprehension with low-level ...
- **p. 1 / ABSTRACT - extractive body cue:** We introduce Embodied-R1, a 3B Vision-Language Model (VLM) specifically designed for embodied reasoning and pointing.
- **p. 1 / ABSTRACT - extractive body cue:** We use a wide range of embodied and general visual reasoning datasets as sources to construct a large-scale dataset, Embodied-Points-200K, which supports key embodied pointing ...
- **p. 1 / ABSTRACT - extractive body cue:** Then we train Embodied-R1 using a two-stage Reinforced Fine-tuning (RFT) curriculum with specialized multi-task reward design.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** This disparity is widely recognized as the "seeing-to-doing gap" (Yuan et al., 2025): a failure to reliably translate rich perceptual understanding into effective robotic actions.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** This gap is largely attributed to two key challenges: (a) data scarcity, where limited embodied data prevents from sufficiently grounding language and vision with physical ...

## Core Idea

- **p. 1 / 1 INTRODUCTION - extractive body cue:** To bridge this gap, we propose pointing as an intuitive and effective paradigm to connect high-level understanding with generalizable action.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Simultaneously, its embodiment-agnostic nature enables knowledge transfer across diverse robot platforms, resolving the heterogeneity challenge.
- **p. 18 / B IMPLEMENTATION DETAILS OF EMBODIED-R1 - extractive body cue:** Second, for the VTG task, we introduced an additional constraint on the format: the generated visual trace must consist of exactly 8 points.
- **p. 18 / B IMPLEMENTATION DETAILS OF EMBODIED-R1 - extractive body cue:** As for Embodied-SFT, we used exactly the same data but trained with a supervised learning loss, kept the batch size at 128, and trained for ...
- **p. 18 / B IMPLEMENTATION DETAILS OF EMBODIED-R1 - extractive body cue:** Training Hyperparameters: We conducted model training on eight NVIDIA A100 40G GPUs.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | This gap is largely attributed to two key challenges: (a) data scarcity, where limited embodied data prevents from sufficiently grounding language and vision with physical actions (Walke et al., 2023; Lin et ... | image/video, language instruction, proprioception과 history | p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |
| State/latent | largely, attributed, challenges, data, scarcity, where, limited, embodied, prevents, sufficiently, grounding, language | language-grounded task state와 action-policy context | p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 18 (B IMPLEMENTATION DETAILS OF EMBODIED-R1) |
| Output/action | To bridge this gap, we propose pointing as an intuitive and effective paradigm to connect high-level understanding with generalizable action. | continuous action, pose 또는 action chunk | p. 1 (1 INTRODUCTION), p. 18 (B IMPLEMENTATION DETAILS OF EMBODIED-R1), p. 18 (B IMPLEMENTATION DETAILS OF EMBODIED-R1) |
| Objective/outcome | In practice, we found that without this constraint, the model in the VTG task was prone to reward hacking behavior. | instruction following, task success, generalization과 latency | p. 18 (B IMPLEMENTATION DETAILS OF EMBODIED-R1), p. 18 (B IMPLEMENTATION DETAILS OF EMBODIED-R1) |

## Main Claims and Actual Contribution

- **p. 1 / 1 INTRODUCTION - extractive body cue:** To bridge this gap, we propose pointing as an intuitive and effective paradigm to connect high-level understanding with generalizable action.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Simultaneously, its embodiment-agnostic nature enables knowledge transfer across diverse robot platforms, resolving the heterogeneity challenge.
- **p. 18 / B IMPLEMENTATION DETAILS OF EMBODIED-R1 - extractive body cue:** Second, for the VTG task, we introduced an additional constraint on the format: the generated visual trace must consist of exactly 8 points.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** 5, Embodied-R1 achieves an 87.5% zero-shot success rate, an improvement of over 60% compared to the RoboPoint and FSD baselines.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** We attribute this significant improvement to the baselines' poor performance on tasks requiring spatial reasoning (e.g., moving the nearest object) and their low success rates ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** It achieves an average rank of 2.1, significantly outperforming its variants trained without common-sense data (Embodied-R1 w/o CS, Rank 3.4) or with only SFT (Embodied-SFT, ...
- **p. 24 / Figure/Table caption - extractive body cue:** Figure 12: Case Analysis: Embodied-R1 possesses embodied reasoning capabilities. It can progressively locate relevant objects and infer spatial relationships according to task instructions, and ultimately ...
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** (O4) Embodied-R1 significantly outperforms models trained solely with SFT.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Embodiment/environment | Our evaluation encompassed 11 QA benchmarks, 4 simulated tasks (SIMPLEREnv) (Li et al., 2024b), and 8 real-world robot (xArm platform) tasks. | hardware/simulator version and reset protocol | p. 6 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Dataset/benchmark | The setup used a third-person Intel RealSense L515 camera (640×480), with all objects, scenes, and tasks being OOD to test generalization. | role, split, size and leakage | p. 6 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS) |
| Metric | We attribute this significant improvement to the baselines' poor performance on tasks requiring spatial reasoning (e.g., moving the nearest object) and their low success rates in grasping challenging rigid objects like a ... | definition, denominator, direction and uncertainty | p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 24 (Figure/Table caption) |
| Baseline/ablation | Figure 2: Overview of four embodied pointing abilities. a VLM trained with RFT to resolve the multi-solution dilemma for embodied pointing, delivering powerful reasoning. 4 With only 3B parameters, Embodied-R1 attains state-of-the-art ... | fair input/data/compute/action matching | p. 3 (Figure/Table caption), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 18 / B IMPLEMENTATION DETAILS OF EMBODIED-R1 - extractive body cue:** We would like to add two clarifying points: First, if the task output fails to meet the required parsing format, subsequent analysis cannot proceed successfully, ...
- **p. 10 / 5 CONCLUSION - extractive body cue:** A detailed discussion of limitations is provided in App.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** D, we conducted an in-depth analysis of failure cases and execution time.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** The score is the accuracy of points falling within the target region.
- **p. 10 / 5 CONCLUSION - extractive body cue:** Empirically, Embodied-R1 achieves state-of-the-art results across multiple benchmark tests and demonstrates robust zero-shot generalization in robotic manipulation tasks, offering a promising pathway toward more capable ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** Middle: Demonstration of the robustness under significant visual disturbances, such as background and lighting changes.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Overview of the Embodied-R1 framework and its zero-shot manipulation performance. Embodied-R1 performs explicit reasoning to generate "pointing" commands, enabling robust execution across a ...

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 This disparity is widely recognized as the "seeing-to-doing gap" (Yuan et al., 2025): a failure to reliably translate rich perceptual understanding into effective robotic actions.를 문제로 두고, To bridge this gap, we propose pointing as an intuitive and effective paradigm to connect high-level understanding with generalizable action.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 18 (B IMPLEMENTATION DETAILS OF EMBODIED-R1), p. 18 (B IMPLEMENTATION DETAILS OF EMBODIED-R1), p. 9 (4 EXPERIMENTS) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
