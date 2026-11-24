# Articulate-Anything: Automatic Modeling of Articulated Objects via a Vision-Language Foundation Model

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2025/hash/2c8047bf3ed8ef6905351608d641f02f-Abstract-Conference.html.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/114017. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICLR
- Authors: Long Le, Jason Xie, William Liang, Hung-Ju Wang, Yue Yang, Yecheng Jason Ma, Kyle Vedder, Arjun Krishna, Dinesh Jayaraman, ERIC EATON
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: Vision-Language Model, Robotics
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2025/hash/2c8047bf3ed8ef6905351608d641f02f-Abstract-Conference.html
- Full-text retrieval: https://proceedings.iclr.cc/paper_files/paper/2025/file/2c8047bf3ed8ef6905351608d641f02f-Paper-Conference.pdf
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 요약과 핵심 기여 두 개를 각 문장에 연결한 판본에서 확인했다.

## Why This Paper Is Here

Articulate-Anything은 영상·이미지·텍스트에 나타난 물체의 부품과 관절을 추론해 시뮬레이터에서 움직일 수 있는 객체 모델을 생성한다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/2c8047bf3ed8ef6905351608d641f02f-Paper-Conference.pdf#page=1)

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Interactive 3D simulated objects are crucial in AR/VR, animations, and robotics, driving immersive experiences and advanced automation.
- **p. 1 / ABSTRACT - extractive body cue:** However, creating these articulated objects requires extensive human effort and expertise, limiting their broader applications.
- **p. 1 / ABSTRACT - extractive body cue:** To overcome this challenge, we present ARTICULATEANYTHING, a system that automates the articulation of diverse, complex objects from many input modalities, including text, images, and ...
- **p. 1 / ABSTRACT - extractive body cue:** ARTICULATEANYTHING leverages vision-language models (VLMs) to generate code that can be compiled into an interactable digital twin for use in standard 3D simulators.
- **p. 1 / ABSTRACT - extractive body cue:** Our system exploits existing 3D asset datasets via a mesh retrieval mechanism, along with an actor-critic system that iteratively proposes, evaluates, and refines solutions for ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** ARTICULATE-ANYTHING represents a step function improvement in quality, accuracy (8.7-12.2% to 75%), and generalizability over prior art (Chen et al., 2024; Mandi et al., 2024), ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, a critical bottleneck in this research direction persists: the immense human labor required to construct realistic, interactable environments for these agents to learn within.

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address this challenge, we present ARTICULATE-ANYTHING, a novel approach in automatic articulation that harnesses the power of leading foundation vision-language models (VLMs) to articulate ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** ARTICULATE-ANYTHING: We present a vision-language actor-critic system that accurately articulates objects from diverse input modalities, including texts, images, and videos.
- **p. 16 / A.3 ROBOTIC TRAINING DETAILS - extractive body cue:** We train a Franka arm to perform four robotic manipulation tasks in the Robosuite simulator using PPO and our generated assets.The policy outputs joint and ...
- **p. 16 / A.3 ROBOTIC TRAINING DETAILS - extractive body cue:** We randomize physics (friction, damping, frictionloss ect), objects' scales and poses to obtain robust policies.
- **p. 23 / A.7 MESH RECONSTRUCTION - extractive body cue:** Chamfer distance is included (lower is better) for different models for in-the-wild results.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Beyond robotics, the flexibility of ARTICULATE-ANYTHING's inputs married with its high-quality outputs puts automatic generation of rich, high-quality, and diverse virtual environments within reach with broad-reaching applications to 3D ... | image/video, language instruction, proprioception과 history | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| State/latent | Beyond, robotics, flexibility, ARTICULATE-ANYTHING, inputs, married, high-quality, outputs, puts, automatic, generation, rich | language-grounded task state와 action-policy context | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 16 (A.3 ROBOTIC TRAINING DETAILS) |
| Output/action | ARTICULATE-ANYTHING: We present a vision-language actor-critic system that accurately articulates objects from diverse input modalities, including texts, images, and videos. | continuous action, pose 또는 action chunk | p. 2 (1 INTRODUCTION), p. 16 (A.3 ROBOTIC TRAINING DETAILS), p. 16 (A.3 ROBOTIC TRAINING DETAILS) |
| Objective/outcome | We randomize physics (friction, damping, frictionloss ect), objects' scales and poses to obtain robust policies. | instruction following, task success, generalization과 latency | p. 16 (A.3 ROBOTIC TRAINING DETAILS) |

## Main Claims and Actual Contribution

- 기존 메시에서 부품을 검색하고 VLM이 배치와 관절을 코드로 제안한 뒤, 렌더링 결과를 보고 오류를 수정하게 했다. [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/2c8047bf3ed8ef6905351608d641f02f-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/2c8047bf3ed8ef6905351608d641f02f-Paper-Conference.pdf#page=5) · [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/2c8047bf3ed8ef6905351608d641f02f-Paper-Conference.pdf#page=6)
- PartNet-Mobility에서 관절 모델링을 평가하고, 영상에서 만든 시뮬레이션 자산으로 조작 정책을 훈련해 실물로 옮기는 예를 제시했다. [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/2c8047bf3ed8ef6905351608d641f02f-Paper-Conference.pdf#page=6) · [PDF 7쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/2c8047bf3ed8ef6905351608d641f02f-Paper-Conference.pdf#page=7) · [PDF 10쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/2c8047bf3ed8ef6905351608d641f02f-Paper-Conference.pdf#page=10)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 9 (Figure/Table caption), p. 9 (5 EXPERIMENTS) |
| Embodiment/environment | Articulate real-world videos 1 RL training in simulation 2 Transfer to real 3 Figure 13: Robotic Application: ARTICULATE-ANYTHING can automatically generate assets given in-the-wild input videos. | hardware/simulator version and reset protocol | p. 10 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS) |
| Dataset/benchmark | Both methods were trained or fine-tuned on five object categories in the PartNet-Mobility dataset. | role, split, size and leakage | p. 10 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS) |
| Metric | In Appendix A.6, table 1 reveals the raw joint prediction errors behind the success rate of Fig. | definition, denominator, direction and uncertainty | p. 7 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS) |
| Baseline/ablation | Figure 7: In-the-wild Reconstruction. We demonstrate ARTICULATE-ANYTHING's performance input modalities compared to prior works URDFormer and Real2Code. Green and red borders denote correct and incorrect predictions with respect to the ... | fair input/data/compute/action matching | p. 8 (Figure/Table caption), p. 6 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 5 EXPERIMENTS - extractive body cue:** 8 breaks down the failure reasons for each method.
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 8: Breakdown of failure percentages in all classes. In ARTICULATE-ANYTHING, incorrect link placement leads to all predicted joints being marked incorrect. For baselines, 59.1% ...
- **p. 14 / Figure/Table caption - extractive body cue:** Figure 14: Joint prediction failure visualization. We visualize different types of joint failures, ranging from the most egregious, joint type, to the least, joint limit. ...
- **p. 6 / 5 EXPERIMENTS - extractive body cue:** Link placement: Success is determined by the pose difference between predicted and ground-truth links falling below a small threshold.
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** Prior works are also limited to simplified inputs as they cannot handle videos.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** Baseline limitations: URDFormer consistently predicts drawer-like structures and is sensitive to minor misalignments (e.g., slightly tilted drawers).
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 7: In-the-wild Reconstruction. We demonstrate ARTICULATE-ANYTHING's performance input modalities compared to prior works URDFormer and Real2Code. Green and red borders denote correct and incorrect ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 INTRODUCTION), p. 16 (A.3 ROBOTIC TRAINING DETAILS), p. 23 (A.7 MESH RECONSTRUCTION), p. 9 (Figure/Table caption)이다.
