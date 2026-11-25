# CLIP-RT: Learning Language-Conditioned Robotic Policies from Natural Language Supervision

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p016.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p016.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RSS
- Authors: Gi-Cheon Kang, Junghyun Kim, Kyuhwan Shim, Jun Ki Lee, Byoung-Tak Zhang
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, language supervision, motion primitives, contrastive imitation, Open X-Embodiment, real-world manipulation
- Official paper: https://www.roboticsproceedings.org/rss21/p016.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p016.pdf
- Code/Project: https://clip-rt.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

CLIP-RT는 사람이 말로 지정한 기본 동작을 시연 수집과 정책 학습에 함께 사용하는 시각언어행동 모델이다. [PDF 1쪽](https://www.roboticsproceedings.org/rss21/p016.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Teaching robots desired skills in real-world environments remains challenging, especially for non-experts.
- **p. 1 / Abstract - extractive body cue:** A key bottleneck is that collecting robotic data offen requires expertise
- **p. 1 / Abstract - extractive body cue:** To this end, we stody two aspects: (1) enabling non-experts to collect robotic data through natural e supervision (et, "move the arm to the right") ...
- **p. 1 / Abstract - extractive body cue:** Specifically, we introduce a data collection framework that collects robot demonstrations based on natural language supervision fand further augments these demonstrations.
- **p. 1 / Abstract - extractive body cue:** We then present CLIP-RT, a new vision-language-action (VLA) model that learns language-conditioned visuomotor polices from this supervision.
- **p. 2 / A. Preliminaries - extractive body cue:** To ‘maintain consistency with the pretraining setup of the VLMs, existing VLA models (7, 29, 3] typically use a single-image observation v, rather than utilizing ...

## Core Idea

- **p. 2 / Abstract - extractive body cue:** Sec- ‘ond, we propose a data collection framework that enables non-experts to collect robot data only through natural language and augment the human-collected demonstration data, ...
- **p. 1 / Abstract - extractive body cue:** We thus explore a method for training robotic skills through natural language. ‘To this tend, we propose a data collection framework that enables non-experts to ...
- **p. 1 / Abstract - extractive body cue:** It consists of two steps: Ianguage-based teleoperation and stochastic trajectory augmentation (STA).
- **p. 2 / A. Preliminaries - extractive body cue:** A robot dataset D = {(rafn)}Xa consists of a demonstration trajectory + paired with language instruction f.
- **p. 2 / Abstract - extractive body cue:** First, we propose CLIP-RT, 4 vision-language-action (VLA) model that learns languageconditioned policies from natural language supervision.
- **p. 2 / Abstract - extractive body cue:** We introduce a vision-language-action (VLA) model that Jearns language-conditioned visuomotor policies from natural language supervision, which we call CLIP-RT (CLIP-based Robotics Transformer).
- **p. 4 / B. CLIP-Based Robotics Transformer (CLIP-RT) - extractive body cue:** It consists of an image encoder {12] and a text encoder [44], both built on Transformer [57].
- **p. 1 / Abstract - extractive body cue:** We then present CLIP-RT, a new vision-language-action (VLA) model that learns language-conditioned visuomotor polices from this supervision.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The goal of languageconditioned imitation learning is minimizing the negative loglikelihood of the expert action «, given the observation history Diy = (Uieoe-s U4) and language instruction f: | image/video, language instruction, proprioception과 history | p. 2 (A. Preliminaries), p. 2 (A. Preliminaries) |
| State/latent | goal, languageconditioned, imitation, learning, minimizing, negative, loglikelihood, expert, action, given, observation, history | language-grounded task state와 action-policy context | p. 2 (A. Preliminaries), p. 2 (A. Preliminaries), p. 7 (256 33%) |
| Output/action | To ‘maintain consistency with the pretraining setup of the VLMs, existing VLA models (7, 29, 3] typically use a single-image observation v, rather than utilizing the full observations v1. ‘At test time, ... | continuous action, pose 또는 action chunk | p. 2 (A. Preliminaries), p. 7 (256 33%), p. 3 (B. CLIP-Based Robotics Transformer (CLIP-RT)) |
| Objective/outcome | The loss function maximizes the cosine similarity between context and language supervision for positive pairs, while minimizing it for negative pairs. | instruction following, task success, generalization과 latency | p. 3 (B. CLIP-Based Robotics Transformer (CLIP-RT)), p. 3 (A. Preliminaries), p. 2 (A. Preliminaries) |

## Main Claims and Actual Contribution

- 영상·과제 지시와 동작 문구를 대조적으로 정렬해 수행할 동작을 선택하고 수집한 시연을 확장한다. [PDF 1쪽](https://www.roboticsproceedings.org/rss21/p016.pdf#page=1) · [PDF 3쪽](https://www.roboticsproceedings.org/rss21/p016.pdf#page=3)
- 실물에서 새 조작 기술의 습득을 평가하고 LIBERO에서는 성공률과 추론 처리량을 측정했다. [PDF 5쪽](https://www.roboticsproceedings.org/rss21/p016.pdf#page=5) · [PDF 8쪽](https://www.roboticsproceedings.org/rss21/p016.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 9 (B. Adapting CLIP-RT to the LIBERO Benchmark), p. 9 (B. Adapting CLIP-RT to the LIBERO Benchmark) |
| Embodiment/environment | This set of tasks serves as a benchmark for evaluating the model's ability to acquire new skills using in-domain data, We first collect indomain data through language-based teleoperation, gathering 10 episodes per ... | hardware/simulator version and reset protocol | p. 5 (A. Tasks & Dataset), p. 9 (B. Adapting CLIP-RT to the LIBERO Benchmark) |
| Dataset/benchmark | Leveraging stochastic trajectory augmentation (STA), we augment each demonstration with 3 additional trajectories across all tasks. ‘This augmentation increases the dataset size to approximately 11K transitions for Common tasks and 10K ... | role, split, size and leakage | p. 5 (A. Tasks & Dataset), p. 9 (B. Adapting CLIP-RT to the LIBERO Benchmark), p. 5 (A. Tasks & Dataset), p. 9 (B. Adapting CLIP-RT to the LIBERO Benchmark) |
| Metric | As shown in Table I, the recent state-of-the-art VLA model, OpenVLA-OFT [30], achieves the highest average success rate of 95.3%. | definition, denominator, direction and uncertainty | p. 9 (B. Adapting CLIP-RT to the LIBERO Benchmark), p. 9 (B. Adapting CLIP-RT to the LIBERO Benchmark), p. 7 (Figure/Table caption) |
| Baseline/ablation | We introduce baseline ‘models and then discuss the results in detail | fair input/data/compute/action matching | p. 5 (C. Experiments on Common and Novel Tasks), p. 5 (C. Experiments on Common and Novel Tasks), p. 9 (B. Adapting CLIP-RT to the LIBERO Benchmark) |

## Explicit Limitations and Failure Boundary

- **p. 9 / B. Limitations and Future Work - extractive body cue:** Inherent Limitations in Human Language Supervision.
- **p. 9 / B. Limitations and Future Work - extractive body cue:** Without incorporating action history into the context, the model cannot make informed
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 9: Example failure cases of CLIP-RT. (a) CLIP-RT
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: A simplified 2D example of stochastic trajectory augmentation (STA). (a): a demonstration trajectory from the starts to the endpoint ¢, passing through a ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (A. Preliminaries), p. 4 (C. In-Domain Data Collection), p. 2 (Abstract), p. 4 (B. CLIP-Based Robotics Transformer (CLIP-RT)), p. 1 (Abstract)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** A key bottleneck is that collecting robotic data offen requires expertise (p. 1, Abstract).
- **Actual contribution:** Sec- ‘ond, we propose a data collection framework that enables non-experts to collect robot data only through natural language and augment the human-collected demonstration data, Third, experiments demonstrate that CLIP-RT ... (p. 2, Abstract).
- **Evaluation boundary:** [30], we measure the throughput and latency on an NVIDIA A100 GPU, As shown in Table I, CLIP-RT+ achieves 39% improved throughput (4.2Hz~>163.8H7) compared with OpenVLA based on its lightweight ... (p. 9, B. Adapting CLIP-RT to the LIBERO Benchmark).
- **Explicit failure boundary:** This is particularly evident in sce requiring recovery from failure states, such as when an object, slips from the gripper, as shown in Figure 9-(d), The heuristies does not adequately ... (p. 8, 256 33%).

## 원문과 공개 자료

- 가중치 · Open X-Embodiment로 사전학습한 CLIP-RT 체크포인트 · cliprt-oxe-pretrained.pt [배포 파일](https://huggingface.co/clip-rt/clip-rt-oxe-pretrained/blob/82c9f47ebb761d48fb04d612f9ecc075388c1bd4/cliprt-oxe-pretrained.pt)
- 코드 · CLIP-RT 시각·언어·동작 정렬 학습 구현 · open_clip/src/training/train.py [배포 파일](https://raw.githubusercontent.com/clip-rt/clip-rt/0b781442f4783709bddcb7b19943baf5517cb46e/open_clip/src/training/train.py)
