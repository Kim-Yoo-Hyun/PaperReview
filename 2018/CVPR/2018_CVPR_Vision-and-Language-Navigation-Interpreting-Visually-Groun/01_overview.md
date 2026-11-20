# Vision-and-Language Navigation: Interpreting Visually-Grounded Navigation Instructions in Real Environments

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1711.07280.
> PDF retrieval source: https://arxiv.org/pdf/1711.07280. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2018 / CVPR
- Authors: Peter Anderson, Qi Wu, Damien Teney, Jake Bruce, Mark Johnson, Niko Sünderhauf, Ian Reid, Stephen Gould, Anton van den Hengel
- Primary track: Robotics-enabling 3D perception
- Tier: NEXT
- Tags: Vision-Language Navigation, Robotics, Navigation, Benchmark
- Official paper: https://arxiv.org/abs/1711.07280
- Full-text retrieval: https://arxiv.org/pdf/1711.07280
- Code/Project: https://bringmeaspoon.org/
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

실내 스캔의 경로와 사람이 작성한 지시를 대응시켜 언어 지시 내비게이션 과제를 정의한다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** A robot that can carry out a natural-language instruction has been a dream since before the Jetsons cartoon series imagined a life of leisure mediated ...
- **p. 1 / Abstract - extractive body cue:** It is a dream that remains stubbornly distant.
- **p. 1 / Abstract - extractive body cue:** However, recent advances in vision and language methods have made incredible progress in closely related areas.
- **p. 1 / Abstract - extractive body cue:** This is significant because a robot interpreting a naturallanguage navigation instruction on the basis of what it sees is carrying out a vision and language ...
- **p. 1 / Abstract - extractive body cue:** Both tasks can be interpreted as visually grounded sequence-to-sequence translation problems, and many of the same methods are applicable.
- **p. 2 / 1. Introduction - extractive body cue:** We investigate the difficulty of this task, and particularly the difficulty of operating in unseen environments, using several baselines and a sequence-to-sequence model based on ...
- **p. 1 / 1. Introduction - extractive body cue:** Blue discs indicate nearby (discretized) navigation options. of this challenge that we refer to as Vision-and-Language Navigation (VLN).

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** To enable the reproducible evaluation of VLN methods, we present the Matterport3D Simulator.
- **p. 2 / 1. Introduction - extractive body cue:** We introduce the Matterport3D Simulator, a software framework for visual reinforcement learning using the Matterport3D panoramic RGB-D dataset [11]; 2.
- **p. 1 / 1. Introduction - extractive body cue:** The dataset particularly has been designed to simplify the application of vision and language methods to what might otherwise seem a distant problem.
- **p. 6 / 5.1. Sequence-to-Sequence Model - extractive body cue:** At each step t, the decoder observes representations of the current image ot and the previous action at-1 as input, applies an attention mechanism to ...
- **p. 6 / 5.1. Sequence-to-Sequence Model - extractive body cue:** Image and action embedding For each image observation ot, we use a ResNet-152 [22] CNN pretrained on ImageNet [46] to extract a mean-pooled feature vector.
- **p. 7 / 5.1. Sequence-to-Sequence Model - extractive body cue:** When then compute an attentional hidden state ˜ht = tanh (Wc[ct; h ′ t]), and calculate the predictive distribution over the next action as at ...
- **p. 7 / 5.2. Training - extractive body cue:** We use dropout of 0.5 on embeddings, CNN features and within the attention model.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | At each step t, the decoder observes representations of the current image ot and the previous action at-1 as input, applies an attention mechanism to the hidden states of the language encoder, ... | standardized observation, action, task state와 evaluation split | p. 6 (5.1. Sequence-to-Sequence Model), p. 2 (1. Introduction) |
| State/latent | step, decoder, observes, representations, current, image, previous, action, at-1, input, applies, attention | benchmark state/goal와 method decision | p. 6 (5.1. Sequence-to-Sequence Model), p. 2 (1. Introduction), p. 6 (5.1. Sequence-to-Sequence Model) |
| Output/action | However, VLN sequences are much longer and, uniquely among vision and language benchmark tasks using real images, the model outputs actions ⟨a0, a1, . . . aT ⟩that manipulate the camera viewpoint. ... | policy/controller trajectory 또는 measured result | p. 2 (1. Introduction), p. 6 (5.1. Sequence-to-Sequence Model), p. 7 (5.2. Training) |
| Objective/outcome | In both cases, we use cross entropy loss at each step to maximize the likelihood of the ground-truth target action a∗ t given the previous state-action sequence ⟨s0, a0, s1, a1, . ... | success metric, robustness, generalization과 reproducibility | p. 7 (5.2. Training), p. 7 (5.2. Training), p. 6 (5.1. Sequence-to-Sequence Model) |

## Main Claims and Actual Contribution

- Matterport3D의 파노라마 연결 그래프에서 이동하는 시뮬레이터와 R2R 데이터를 구축한다.
- 시각·언어 시퀀스 정책의 익숙한 건물과 새로운 건물에서의 경로 추종을 비교한다.

[검증한 원문](https://openaccess.thecvf.com/content_cvpr_2018/html/Anderson_Vision-and-Language_Navigation_Interpreting_CVPR_2018_paper.html)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 7 (6. Results), p. 8 (6. Results) |
| Embodiment/environment | These datasets typically offer only one or two paths through a scene, making them inadequate for simulating robot motion. | hardware/simulator version and reset protocol | p. 3 (3.1. Matterport3D Dataset), p. 3 (3.1. Matterport3D Dataset) |
| Dataset/benchmark | We reserve an additional 11 scenes and 2,349 instructions for validating in unseen environments (val unseen). | role, split, size and leakage | p. 3 (3.1. Matterport3D Dataset), p. 3 (3.1. Matterport3D Dataset), p. 6 (4.4. Evaluation Protocol), p. 6 (4.4. Evaluation Protocol) |
| Metric | Validation loss, navigation error and success rate during training. | definition, denominator, direction and uncertainty | p. 8 (6. Results), p. 7 (6. Results), p. 8 (6. Results) |
| Baseline/ablation | To disentangle the problem of recognizing the goal location, we also report success for each agent under an oracle stopping rule, i.e. if the agent stopped at the closest point to the ... | fair input/data/compute/action matching | p. 6 (4.4. Evaluation Protocol), p. 8 (6. Results), p. 7 (6. Results) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 6. Results - extractive body cue:** Nevertheless, people are not infallible when it comes to navigation.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 1 (1. Introduction), p. 6 (5.1. Sequence-to-Sequence Model)이다.
