# Learning to Act Anywhere with Task-centric Latent Actions

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p014.html.
> PDF retrieval source: https://arxiv.org/pdf/2505.06111. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RSS
- Authors: Qingwen Bu, Yanting Yang, Jisong Cai, Shenyuan Gao, Guanghui Ren, Maoqing Yao, Ping Luo, Hongyang Li
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, cross-embodiment, latent action, human video, robot data, generalist policy
- Official paper: https://www.roboticsproceedings.org/rss21/p014.html
- Full-text retrieval: https://arxiv.org/pdf/2505.06111
- Code/Project: https://github.com/OpenDriveLab/UniVLA
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

UniVLA는 다양한 환경과 신체의 영상에서 과제와 관련된 잠재 행동을 배워 로봇별 행동으로 해독한다. [PDF 1쪽](https://www.roboticsproceedings.org/rss21/p014.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** A generalist robot should perform effectively across various environments.
- **p. 1 / Abstract - extractive body cue:** However, most existing approaches heavily rely on scaling action-annotated data to enhance their capabilities.
- **p. 1 / Abstract - extractive body cue:** Consequently, they are often limited to single physical specification and struggle to learn transferable knowledge across different embodiments and environments.
- **p. 1 / Abstract - extractive body cue:** To confront these limitations, we propose UniVLA, a new framework for learning cross-embodiment vision-language-action (VLA) policies.
- **p. 1 / Abstract - extractive body cue:** Our key innovation is to derive task-centric action representations from videos with a latent action model.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, they typically rely on groundtruth action labels for supervision, which limits their scalability in utilizing internet-scale data from diverse environments.
- **p. 1 / I. INTRODUCTION - extractive body cue:** To address these challenges, we propose UniVLA, a generalist policy learning framework that enables scalable and efficient planning across various embodiments and environments.

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, our main contributions are three-folds: • We propose UniVLA, a recipe towards generalist policy by planning in a unified, embodiment-agnostic action space, enabling ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** To address these challenges, we propose UniVLA, a generalist policy learning framework that enables scalable and efficient planning across various embodiments and environments.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Our recipe for generalist policy consists of three key stages: 1) Task-centric Latent Action Learning, where we extract task-relevant action representations from massive cross-embodiment videos ...
- **p. 3 / III. METHODOLOGY - extractive body cue:** Inspired by joint-embedding predictive architectures (JEPA) [5, 6, 96], we propose using DINOv2 [62] spatial patch features as semantically rich representations.
- **p. 3 / III. METHODOLOGY - extractive body cue:** III-C) To facilitate efficient adaptation to various robotic control systems, we introduce specialized policy heads that decode latent actions into executable control signals.
- **p. 5 / III. METHODOLOGY - extractive body cue:** Drawing inspiration from the wellestablished Chain-of-Thought (CoT) reasoning paradigm [80] in large language models (LLMs), which generates intermediate reasoning steps to address complex tasks, we ...
- **p. 3 / III. METHODOLOGY - extractive body cue:** To mitigate the unfavorable effect of task-irrelevant dynamics, we incorporate readily available language instructions into the first training stage of latent action model (Fig.
- **p. 3 / III. METHODOLOGY - extractive body cue:** To derive latent actions from videos, our latent action model is constructed around an Inverse Dynamics Model (IDM) based encoder I(at/ot, ot+k) and a Forward ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | III-B) Based on this, we train an auto-regressive transformer-based vision-language-action model, which takes visual observations and task instructions as inputs to predict latent action tokens in a unified latent space; 3) (Sec. | image/video, language instruction, proprioception과 history | p. 3 (III. METHODOLOGY), p. 5 (III. METHODOLOGY) |
| State/latent | III-B, train, auto-regressive, transformer-based, vision-language-action, model, takes, visual, observations, task, instructions, inputs | language-grounded task state와 action-policy context | p. 3 (III. METHODOLOGY), p. 5 (III. METHODOLOGY), p. 4 (III. METHODOLOGY) |
| Output/action | Our policy architecture is founded on the Prismatic-7B Vision-Language Model (VLM) [37], which processes projected visual embeddings and tokenized task instructions as inputs to predict latent action tokens in an auto-regressive manner. | continuous action, pose 또는 action chunk | p. 5 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY) |
| Objective/outcome | Our selfsupervised objective minimizes the embedding reconstruction error: ∥ˆOt+k -Ot+k∥2. | instruction following, task success, generalization과 latency | p. 3 (III. METHODOLOGY), p. 5 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) |

## Main Claims and Actual Contribution

- 언어 지시를 조건으로 DINO 특징 공간의 변화를 모델링해 과제와 무관한 영상 움직임의 영향을 줄인다. [PDF 1쪽](https://www.roboticsproceedings.org/rss21/p014.pdf#page=1) · [PDF 3쪽](https://www.roboticsproceedings.org/rss21/p014.pdf#page=3)
- 조작·내비게이션과 실물 전이를 평가하고 LIBERO에서 잠재 행동 표현과 디코더 설계가 성능에 주는 영향을 비교했다. [PDF 5쪽](https://www.roboticsproceedings.org/rss21/p014.pdf#page=5) · [PDF 10쪽](https://www.roboticsproceedings.org/rss21/p014.pdf#page=10)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 7 (2) Navigation Benchmark on Room2Room) |
| Embodiment/environment | These benchmarks offer a set of languageguided navigation tasks and continuous environments for executing low-level actions in reconstructed photorealistic indoor scenes. | hardware/simulator version and reset protocol | p. 7 (2) Navigation Benchmark on Room2Room), p. 6 (1) Manipulation Benchmark on LIBERO) |
| Dataset/benchmark | In this experiment, we evaluate UniVLA on the VLN-CE benchmarks [41] to assess its performance on navigation tasks. | role, split, size and leakage | p. 7 (2) Navigation Benchmark on Room2Room), p. 6 (1) Manipulation Benchmark on LIBERO), p. 7 (2) Navigation Benchmark on Room2Room), p. 5 (IV. EVALUATIONS) |
| Metric | Fig. 5: Real-world robot experiments. We propose four different tasks: "Store the screwdriver", "Clean the cutting board", "Fold towel twice", and "Stack tower of hanoi", towards the evaluation of four axis of ... | definition, denominator, direction and uncertainty | p. 7 (Figure/Table caption), p. 7 (2) Navigation Benchmark on Room2Room), p. 10 (Figure/Table caption) |
| Baseline/ablation | Fig. 4: Task setup on the LIBERO benchmark. TABLE I: Results on LIBERO benchmark across four evaluation suites. Our proposed UniVLA exhibits superior performance across all benchmarked tasks compared to existing baseline ... | fair input/data/compute/action matching | p. 6 (Figure/Table caption), p. 7 (2) Navigation Benchmark on Room2Room), p. 7 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 2) Navigation Benchmark on Room2Room - extractive body cue:** UniVLA demonstrates superior performance across all evaluated tasks, showcasing its exceptional ability to generalize from high-level semantic comprehension to low-level visual robustness.
- **p. 9 / 3) Real-world Robot Deployment - extractive body cue:** It achieves a 66.7% success rate under varying lighting conditions, surpassing Diffusion Policy (20.0%), OpenVLA (13.3%), and LAPA (26.7%), demonstrating robustness to environmental change.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 5 (III. METHODOLOGY), p. 3 (III. METHODOLOGY)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, they typically rely on groundtruth action labels for supervision, which limits their scalability in utilizing internet-scale data from diverse environments. (p. 1, I. INTRODUCTION).
- **Actual contribution:** In summary, our main contributions are three-folds: • We propose UniVLA, a recipe towards generalist policy by planning in a unified, embodiment-agnostic action space, enabling scalable and efficient decision-making by ... (p. 2, I. INTRODUCTION).
- **Evaluation boundary:** Fig. 4: Task setup on the LIBERO benchmark. TABLE I: Results on LIBERO benchmark across four evaluation suites. Our proposed UniVLA exhibits superior performance across all benchmarked tasks compared to ... (p. 6, Figure/Table caption).
- **Explicit failure boundary:** While UniVLA advances generalist robotic policies, several limitations remain. (p. 11, VI. LIMITATIONS AND FUTURE WORK).

## 원문과 공개 자료

- 가중치 · UniVLA 7B 기본 모델의 첫 가중치 샤드 · model-00001-of-00003.safetensors [배포 파일](https://huggingface.co/qwbu/univla-7b/blob/968e2896809c00968e8fd936e052476ce5ac1bd0/model-00001-of-00003.safetensors)
- 코드 · UniVLA 잠재 행동 정책 훈련 구현 · vla-scripts/train.py [배포 파일](https://raw.githubusercontent.com/OpenDriveLab/UniVLA/0ab9e9dd3074ffa14fdd1a00aa2aa84e4f8e1352/vla-scripts/train.py)
