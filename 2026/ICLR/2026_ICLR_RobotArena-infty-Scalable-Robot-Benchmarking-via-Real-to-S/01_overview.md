# RobotArena $\infty$: Scalable Robot Benchmarking via Real-to-Sim Translation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; title-token overlap first two pages=0.875); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2026/hash/2aa3da3c1463ee2cdaaee94be4f8ba3f-Abstract-Conference.html.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/245501. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: Yash Jangir, Yidi Zhang, Kashu Yamazaki, Chenyu Zhang, Kuan-Hsun Tu, Tsung-Wei Ke, Lei Ke, Yonatan Bisk, Katerina Fragkiadaki
- Primary track: Benchmarks and Datasets
- Tier: REFERENCE
- Tags: Robotics, Benchmark
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/2aa3da3c1463ee2cdaaee94be4f8ba3f-Abstract-Conference.html
- Full-text retrieval: https://proceedings.iclr.cc/paper_files/paper/2026/file/2aa3da3c1463ee2cdaaee94be4f8ba3f-Paper-Conference.pdf
- Code/Project: not identified
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; title-token overlap first two pages=0.875) 2026-11-24 요약과 핵심 기여 두 개를 각 문장에 연결한 판본에서 확인했다.

## Why This Paper Is Here

RobotArena ∞는 실제 로봇 시연 영상을 시뮬레이션 장면으로 변환한 뒤 여러 정책의 실행 영상을 공통 환경에서 비교하는 평가 체계다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/2aa3da3c1463ee2cdaaee94be4f8ba3f-Paper-Conference.pdf#page=1)

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** The pursuit of robot generalists, instructable agents capable of performing diverse tasks across diverse environments, demands rigorous and scalable evaluation.
- **p. 1 / ABSTRACT - extractive body cue:** Yet real-world testing of robot policies remains fundamentally constrained: it is laborintensive, slow, unsafe at scale, and difficult to reproduce.
- **p. 1 / ABSTRACT - extractive body cue:** As policies expand in scope and complexity, these barriers only intensify, since defining "success" in robotics often hinges on nuanced human judgments of execution quality.
- **p. 1 / ABSTRACT - extractive body cue:** We introduce RobotArena ∞, a new benchmarking framework that overcomes these challenges by shifting VLA evaluation into large-scale simulated environments augmented with online human feedback.
- **p. 1 / ABSTRACT - extractive body cue:** Leveraging advances in vision-language models, 2D-to-3D generative modeling, and differentiable rendering, our approach automatically converts video demonstrations from widely used robot datasets into simulated counterparts.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** While recent years have witnessed substantial progress in developing more capable and general robot policies, their evaluation remains a persistent challenge and lacks standardization.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Notable examples include the Amazon Picking Challenge Correll et al.

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** RobotArena ∞: We introduce RobotArena ∞, a new benchmarking framework that scales robot evaluation by deploying policies in automatically constructed simulated environments and assessing them ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** We present key evaluation results that reveal how current robot policies generalize-or fail to-under distribution shifts.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** We introduce a fully automated reality-to-simulation translation pipeline built upon VLMs, 2D-to-3D generative models and differentiable rendering.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** RobotArena ∞is inspired by prior efforts to design scalable robot benchmarks, particularly the seminal contributions of BEHAVIOR (Li et al., 2024) and SIMPLER (Li et ...
- **p. 1 / ABSTRACT - extractive body cue:** We introduce RobotArena ∞, a new benchmarking framework that overcomes these challenges by shifting VLA evaluation into large-scale simulated environments augmented with online human feedback.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** First, vision-language-action (VLA) models are highly sensitive to dataset differences: performance drops when they are tested in environments outside their training distribution, indicating that current ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We first automatically translate real videos into corresponding simulation environments, building upon recent advances in vision-language models for scene understanding, 2D-to-3D generative models for asset ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Such manual oversight also raises concerns about consistency and fairness, particularly when baselines and new models are compared under slightly different conditions.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | First, vision-language-action (VLA) models are highly sensitive to dataset differences: performance drops when they are tested in environments outside their training distribution, indicating that current models are not true generalists ... | standardized observation, action, task state와 evaluation split | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| State/latent | First, vision-language-action, VLA, models, highly, sensitive, dataset, differences, performance, drops, when, they | benchmark state/goal와 method decision | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT) |
| Output/action | We first automatically translate real videos into corresponding simulation environments, building upon recent advances in vision-language models for scene understanding, 2D-to-3D generative models for asset creation, and differentiable ... | policy/controller trajectory 또는 measured result | p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 1 (ABSTRACT) |
| Objective/outcome | However, the high cost for both organizers and participants means such events occur infrequently, often no more than once a year. | success metric, robustness, generalization과 reproducibility | p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |

## Main Claims and Actual Contribution

- 영상의 물체와 장면을 3차원 자산으로 복원해 시뮬레이터에 배치하고 원래 작업과 대응하는 정책 평가 환경을 구성했다. [PDF 3쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/2aa3da3c1463ee2cdaaee94be4f8ba3f-Paper-Conference.pdf#page=3) · [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/2aa3da3c1463ee2cdaaee94be4f8ba3f-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/2aa3da3c1463ee2cdaaee94be4f8ba3f-Paper-Conference.pdf#page=5)
- 시뮬레이션 실행에 대한 VLM의 진행도 채점과 사람의 쌍별 선호를 함께 수집해 정책별 수행 품질을 비교했다. [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/2aa3da3c1463ee2cdaaee94be4f8ba3f-Paper-Conference.pdf#page=5) · [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/2aa3da3c1463ee2cdaaee94be4f8ba3f-Paper-Conference.pdf#page=6) · [PDF 7쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/2aa3da3c1463ee2cdaaee94be4f8ba3f-Paper-Conference.pdf#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 9 (Figure/Table caption), p. 6 (Figure/Table caption) |
| Embodiment/environment | The result is a continuously evolving, reproducible, and scalable benchmark for real-world-trained robot manipulation policies, addressing a critical missing capability in today's robotics landscape. | hardware/simulator version and reset protocol | p. 1 (ABSTRACT), p. 1 (ABSTRACT) |
| Dataset/benchmark | BEHAVIOR boasts an impressive manual effort of asset and environment creation, while SIMPLER reconstructs four real-world Bridge scenes and includes hand-designed reward functions. | role, split, size and leakage | p. 1 (ABSTRACT), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Metric | Figure 19: Example VLM-generated task evaluation curves on perturbed environments. Top: A successful pick-and-place execution-after the object lift the VLM score climbs steadily and correctly shows task completion. Bottom: An unsuccessf ... | definition, denominator, direction and uncertainty | p. 24 (Figure/Table caption), p. 22 (Figure/Table caption), p. 24 (Figure/Table caption) |
| Baseline/ablation | Such manual oversight also raises concerns about consistency and fairness, particularly when baselines and new models are compared under slightly different conditions. | fair input/data/compute/action matching | p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 2 RELATED WORK - extractive body cue:** Intuitively, this focuses evaluation on the terminal phase of execution, where task completion (or failure) is most evident.
- **p. 24 / Figure/Table caption - extractive body cue:** Figure 19: Example VLM-generated task evaluation curves on perturbed environments. Top: A successful pick-and-place execution-after the object lift the VLM score climbs steadily and correctly ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Our benchmark is not without limitations.
- **p. 8 / 2 RELATED WORK - extractive body cue:** For example, in RH20TSim, RoboVLM (19.05%) achieves a substantially higher score than all other models, while X-VLA fails (0.00%).
- **p. 9 / 2 RELATED WORK - extractive body cue:** 6 LIMITATIONS AND FUTURE DIRECTIONS By leveraging recent advances in reality-to-simulation translation and crowdsourced evaluation, RobotArena ∞provides a scalable and extensible robot benchmark.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Second, even within the same environment, performance degrades under perturbations, showing that robustness to distribution shifts remains an open challenge.
- **p. 1 / ABSTRACT - extractive body cue:** Yet real-world testing of robot policies remains fundamentally constrained: it is laborintensive, slow, unsafe at scale, and difficult to reproduce.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION)이다.
