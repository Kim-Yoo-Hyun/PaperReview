# Embodied-R1: Reinforced Embodied Reasoning for General Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2026/hash/0f7ad318868d228b980b13cf827e85f4-Abstract-Conference.html.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/245153. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: Yifu Yuan, Haiqin Cui, Yaoting Huang, Yibin Chen, Fei Ni, Zibin Dong, Pengyi Li, YAN ZHENG, Hongyao Tang, Jianye Hao
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: Vision-Language Model, Robotics, Reinforcement Learning
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/0f7ad318868d228b980b13cf827e85f4-Abstract-Conference.html
- Full-text retrieval: https://proceedings.iclr.cc/paper_files/paper/2026/file/0f7ad318868d228b980b13cf827e85f4-Paper-Conference.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 요약과 핵심 기여 두 개를 각 문장에 연결한 판본에서 확인했다.

## Why This Paper Is Here

Embodied-R1은 영상의 점을 가리키는 표현으로 언어 지시와 로봇별 동작을 연결하고 이 공간 추론 능력을 강화학습으로 개선한다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/0f7ad318868d228b980b13cf827e85f4-Paper-Conference.pdf#page=1)

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

- 네 종류의 위치 지시 능력을 구분해 Embodied-Points-200K를 구성하고, 과제별 보상을 둔 두 단계 후학습을 적용했다. [PDF 3쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/0f7ad318868d228b980b13cf827e85f4-Paper-Conference.pdf#page=3) · [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/0f7ad318868d228b980b13cf827e85f4-Paper-Conference.pdf#page=5) · [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/0f7ad318868d228b980b13cf827e85f4-Paper-Conference.pdf#page=6)
- 공간 위치 추론의 정답률을 비교한 뒤 예측한 점을 동작에 연결해 SimplerEnv와 실제 xArm 여덟 과제에서 과제별 추가 학습 없이 평가했다. [PDF 7쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/0f7ad318868d228b980b13cf827e85f4-Paper-Conference.pdf#page=7) · [PDF 8쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/0f7ad318868d228b980b13cf827e85f4-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/0f7ad318868d228b980b13cf827e85f4-Paper-Conference.pdf#page=9)

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

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 18 (B IMPLEMENTATION DETAILS OF EMBODIED-R1), p. 9 (4 EXPERIMENTS)이다.
