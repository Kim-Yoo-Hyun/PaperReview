# GravMAD: Grounded Spatial Value Maps Guided Action Diffusion for Generalized 3D Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (33 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2025/hash/fce176458ff542940fa3ed16e6f9c852-Abstract-Conference.html.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/114266. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICLR
- Authors: Yangtao Chen, Zixuan Chen, Junhui Yin, Jing Huo, Pinzhuo Tian, Jieqi Shi, Yang Gao
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: Robotics, 3D Vision, Diffusion, Imitation Learning
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2025/hash/fce176458ff542940fa3ed16e6f9c852-Abstract-Conference.html
- Full-text retrieval: https://proceedings.iclr.cc/paper_files/paper/2025/file/fce176458ff542940fa3ed16e6f9c852-Paper-Conference.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (33 pages; PyMuPDF text; title-token overlap first two pages=1.0)

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Why This Paper Is Here

문제 관련 발췌 — However, these policies often lack the language understanding and generalization abilities of foundation models.

방법 관련 발췌 — In summary, our contributions are: 1) We propose leveraging key sub-goals in 3D manipulation tasks to bridge the gap between foundation models and learned policies.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Robots' ability to follow language instructions and execute diverse 3D manipulation tasks is vital in robot learning.
- **p. 1 / ABSTRACT - extractive body cue:** Traditional imitation learning-based methods perform well on seen tasks but struggle with novel, unseen ones due to variability.
- **p. 1 / ABSTRACT - extractive body cue:** Recent approaches leverage large foundation models to assist in understanding novel tasks, thereby mitigating this issue.
- **p. 1 / ABSTRACT - extractive body cue:** However, these methods lack a taskspecific learning process, which is essential for an accurate understanding of 3D environments, often leading to execution failures.
- **p. 1 / ABSTRACT - extractive body cue:** In this paper, we introduce GravMAD, a sub-goal-driven, language-conditioned action diffusion framework that combines the strengths of imitation learning and foundation models.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** However, these policies often lack the language understanding and generalization abilities of foundation models.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, this decoupling often leads to a limited understanding of scenes and manipulation tasks (Huang et al., 2024), allowing robots to conceptually grasp tasks but ...

## Core Idea

- **p. 3 / 1 INTRODUCTION - extractive body cue:** In summary, our contributions are: 1) We propose leveraging key sub-goals in 3D manipulation tasks to bridge the gap between foundation models and learned policies.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To this end, inspired by the approach of introducing task sub-goals to achieve efficient execution in robotic manipulation (Black et al., 2024; Kang et al., ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** 3) We propose a new action diffusion framework, GravMAD, guided by GravMaps.
- **p. 4 / 1 INTRODUCTION - extractive body cue:** Our method combines the learning power of diffusion architectures with the generalization of VLMs.
- **p. 4 / 3 METHOD - extractive body cue:** In this section, we introduce GravMAD, a multi-task, sub-goal-driven, language-conditioned diffusion framework for 3D manipulation, as shown in Fig.
- **원문 대조:** 세 번째 prediction head는 gripper의 open/close 상태를 예측하며 ground-truth openness에 대한 binary cross-entropy로 학습한다. Position·rotation noise head의 L1 loss 및 subgoal auxiliary head와 구분된다. ([PDF p. 7](https://arxiv.org/pdf/2409.20154#page=7), §3, Eq. (3)).
- **p. 7 / 3 METHOD - extractive body cue:** A self-attention layer then refines this representation to produce end-effector contextual features.
- **p. 18 / A.4 DETAIL OF MODEL ARCHITECTURE AND HYPER-PARAMETERS FOR GRAVMAD - extractive body cue:** First, the visual input is processed by a 2D Visual Encoder, transforming image data into feature representations.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Our goal is to learn a policy π : (O, L, G) 7→A, which maps observations ot, sub-goals gt, and instructions ℓto actions at. | image/video, language instruction, proprioception과 history | p. 5 (3 METHOD), p. 6 (3 METHOD) |
| State/latent | goal, learn, policy, maps, observations, sub-goals, instructions, actions, keypose, corresponding, observation-action, pair | language-grounded task state와 action-policy context | p. 5 (3 METHOD), p. 6 (3 METHOD), p. 2 (1 INTRODUCTION) |
| Output/action | For each keypose, the corresponding observation-action pair (oKip, aKip) is passed to the function SK, which outputs a Boolean value to determine whether the given keypose should be discovered as a sub-goal ... | continuous action, pose 또는 action chunk | p. 6 (3 METHOD), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Objective/outcome | The loss maximizes similarity between positive pairs and minimizes it between negative pairs: Lcon = -1 N N X i=1 log exp(fgi · fg + i /T) PN j=1 exp(fgi · fgj/T) ... | instruction following, task success, generalization과 latency | p. 7 (3 METHOD), p. 7 (3 METHOD), p. 5 (3 METHOD) |

## Main Claims and Actual Contribution

- **p. 3 / 1 INTRODUCTION - extractive body cue:** In summary, our contributions are: 1) We propose leveraging key sub-goals in 3D manipulation tasks to bridge the gap between foundation models and learned policies.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To this end, inspired by the approach of introducing task sub-goals to achieve efficient execution in robotic manipulation (Black et al., 2024; Kang et al., ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** 3) We propose a new action diffusion framework, GravMAD, guided by GravMaps.
- **p. 4 / 1 INTRODUCTION - extractive body cue:** Our method combines the learning power of diffusion architectures with the generalization of VLMs.
- **p. 4 / 3 METHOD - extractive body cue:** In this section, we introduce GravMAD, a multi-task, sub-goal-driven, language-conditioned diffusion framework for 3D manipulation, as shown in Fig.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** GravMAD (Manual) outperforms Act3D and Voxposer across all tasks and exceeds the best baseline, 3D Diffuser Actor, in 9 out of 12 tasks, with an ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** Despite the Detector's coarse SoM positioning affecting GravMAD (VLM)'s performance, it still outperforms Act3D and Voxposer on all tasks, with a 0.91% higher average success ...
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 4: Ablation Studies. We evaluate the impact of key design elements by reporting the average success rates across 12 base tasks and 8 novel ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Embodiment/environment | Additionally, we further validate GravMAD on 10 real-world robotic tasks, with details provided in Appendix D.6. | hardware/simulator version and reset protocol | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Dataset/benchmark | Final checkpoints are evaluated across 3 seeds with 25 test episodes per task. | role, split, size and leakage | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Metric | Despite the Detector's coarse SoM positioning affecting GravMAD (VLM)'s performance, it still outperforms Act3D and Voxposer on all tasks, with a 0.91% higher average success rate than 3D Diffuser Actor. | definition, denominator, direction and uncertainty | p. 9 (4 EXPERIMENTS), p. 10 (Figure/Table caption), p. 8 (4 EXPERIMENTS) |
| Baseline/ablation | Performance gains are compared to the best-performing baselines, indicated by underlines. | fair input/data/compute/action matching | p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 26 / Figure/Table caption - extractive body cue:** Figure 11: Failure cause analysis, including (a) visualization of failure examples; (b) comparison of imprecise labels and expected labels. identify ideal areas, leading to imprecise ...
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** During testing, except for the novel task "push buttons light", which must be completed in 3 time steps, all other tasks must be completed in ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** For further analysis of failure cases, please refer to Appendix B.3.
- **p. 10 / 8 Novel Tasks - extractive body cue:** In contrast, omitting the cost map causes zero-gradient issues during training, leading to incorrect predictions and task failure.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** GravMAD (VLM) also struggles in tasks like "Place Wine" due to inaccuracies in the object positions provided by the Detector, especially when Semantic SAM fails ...
- **p. 10 / 8 Novel Tasks - extractive body cue:** This occurs because the encoder cannot process such input.
- **p. 16 / A.2 HEURISTICS FOR SUB-GOAL KEYPOSE DISCOVERY - extractive body cue:** One current limitation of the Sub-goal Keypose Discovery method is its inability to effectively handle tasks involving tool use, which we plan to address in ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 7 (3 METHOD)이다.
