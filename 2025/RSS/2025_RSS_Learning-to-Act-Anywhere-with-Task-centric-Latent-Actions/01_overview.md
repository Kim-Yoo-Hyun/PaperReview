# Learning to Act Anywhere with Task-centric Latent Actions

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p014.html.
> PDF retrieval source: https://arxiv.org/pdf/2505.06111. Reading tracker status/evidence was not changed.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, cross-embodiment, latent action, human video, robot data, generalist policy
- Official paper: https://www.roboticsproceedings.org/rss21/p014.html
- Full-text retrieval: https://arxiv.org/pdf/2505.06111
- Code/Project: https://github.com/OpenDriveLab/UniVLA
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, they typically rely on groundtruth action labels for supervision, which limits their scalability in utilizing internet-scale data from diverse environments.를 문제로 두고, In summary, our main contributions are three-folds: • We propose UniVLA, a recipe towards generalist policy by planning in a unified, embodiment-agnostic action space, enabling scalable and efficient decision-making by learning from ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

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

- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, our main contributions are three-folds: • We propose UniVLA, a recipe towards generalist policy by planning in a unified, embodiment-agnostic action space, enabling ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** To address these challenges, we propose UniVLA, a generalist policy learning framework that enables scalable and efficient planning across various embodiments and environments.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Our recipe for generalist policy consists of three key stages: 1) Task-centric Latent Action Learning, where we extract task-relevant action representations from massive cross-embodiment videos ...
- **p. 3 / III. METHODOLOGY - extractive body cue:** Inspired by joint-embedding predictive architectures (JEPA) [5, 6, 96], we propose using DINOv2 [62] spatial patch features as semantically rich representations.
- **p. 3 / III. METHODOLOGY - extractive body cue:** III-C) To facilitate efficient adaptation to various robotic control systems, we introduce specialized policy heads that decode latent actions into executable control signals.
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: Oracle success rate on R2R in VLN-CE. With only a single-frame RGB input, UniVLA demonstrates performance on par with NaVid, a navigation model ...
- **p. 7 / 2) Navigation Benchmark on Room2Room - extractive body cue:** UniVLA significantly outperforms Seq2Seq and CMA, increasing the oracle success rate from 8.10% to 47.1%.
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 10: Data efficiency. We present the success rate of UniVLA across varying dataset proportions (10%, 20%, 50%, and the full dataset). Our policy can ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

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

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, they typically rely on groundtruth action labels for supervision, which limits their scalability in utilizing internet-scale data from diverse environments.를 문제로 두고, In summary, our main contributions are three-folds: • We propose UniVLA, a recipe towards generalist policy by planning in a unified, embodiment-agnostic action space, enabling scalable and efficient decision-making by learning from ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 5 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
