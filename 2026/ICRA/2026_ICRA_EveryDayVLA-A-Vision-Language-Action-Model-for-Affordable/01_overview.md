# EveryDayVLA: A Vision-Language-Action Model for Affordable Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://api.crossref.org/works/10.1109/icra57385.2026.11696905.
> PDF retrieval source: https://arxiv.org/pdf/2511.05397. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICRA
- Authors: Samarth Chopra, Alex McMoil, Ben Carnovale, Evan Sokolson, Rajkumar Kubendran, Samuel Dickerson
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, Robotics
- Official paper: https://api.crossref.org/works/10.1109/icra57385.2026.11696905
- Full-text retrieval: https://arxiv.org/pdf/2511.05397
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Why This Paper Is Here

EveryDayVLA는 저비용 6자유도 로봇팔에 이산·연속 행동을 함께 예측하는 정책과 동작 중 재계획을 결합한다. [PDF 1쪽](https://arxiv.org/pdf/2511.05397v1#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** While Vision-Language-Action (VLA) models map visual inputs and language instructions directly to robot actions, they often rely on costly hardware and struggle in novel or ...
- **p. 1 / Abstract - extractive body cue:** We introduce EverydayVLA, a 6DOF manipulator that can be assembled for $300, capable of modest payloads and workspaces.
- **p. 1 / Abstract - extractive body cue:** A single unified model jointly outputs discrete and continuous actions, and our adaptivehorizon ensembler monitors motion uncertainty to trigger onthe-fly replanning for safe, reliable operation.
- **p. 1 / Abstract - extractive body cue:** On LIBERO, EverydayVLA matches state-of-the-art success rates, and in realworld tests it outperforms prior methods by 49% in-distribution and 34.9% out-of-distribution.
- **p. 1 / Abstract - extractive body cue:** By combining a state-of-the-art VLA with cost-effective hardware, EverydayVLA democratizes access to a robotic foundation model, and paves the way for economical use in homes ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** To address these challenges, we present a full-stack system, and present three distinct contributions. • Collaborative training with adaptive horizon control (AdaHorizon).
- **p. 1 / I. INTRODUCTION - extractive body cue:** Yet, even with internet-scale pretraining, they remain brittle under unfamiliar lighting [3], novel objects [4], and visual distractors [5], and often fail to generalize to ...

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** To address these challenges, we present a full-stack system, and present three distinct contributions. • Collaborative training with adaptive horizon control (AdaHorizon).
- **p. 3 / III. METHOD - extractive body cue:** We term our method AdaHorizon, and find that it enables discrete actions to match or exceed the precision of continuous controls, even on dexterous tasks ...
- **p. 2 / III. METHOD - extractive body cue:** To further improve performance, we introduce a novel adaptive horizon module, allowing the
- **p. 3 / III. METHOD - extractive body cue:** To harness both strengths, we introduce a more robust uncertainty metric: the mean absolute difference between the continuous and discrete action predictions, which outperforms the ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Yet, even with internet-scale pretraining, they remain brittle under unfamiliar lighting [3], novel objects [4], and visual distractors [5], and often fail to generalize to ...
- **p. 2 / III. METHOD - extractive body cue:** Instead, EveryDayVLA takes advantage of action chunking, parallel decoding, and a collaborative training recipe, predicting discrete autoregressive and continuous action chunks, using an L1-regression objective, ...
- **원문 대조:** Discrete action에는 cross-entropy, continuous action에는 L1 loss를 사용하며 두 항을 결합해 학습한다. 식 (1)의 log 항은 예측한 discrete-action probability에 적용된다. ([PDF p. 3](https://arxiv.org/pdf/2511.05397#page=3), §III-A Collaborative Training, Eqs. (1)–(3)).
- **p. 3 / III. METHOD - extractive body cue:** The VLA takes as input an image and natural language instruction and these are tokenized via the vision and language encoders, and sent to the ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | EveryDayVLA EveryDayVLA ingests as input a demonstration consisting of an image observation ot and a language instruction lt. | image/video, language instruction, proprioception과 history | p. 3 (III. METHOD), p. 3 (III. METHOD) |
| State/latent | EveryDayVLA, ingests, input, demonstration, consisting, image, observation, language, instruction, VLA, takes, natural | language-grounded task state와 action-policy context | p. 3 (III. METHOD), p. 3 (III. METHOD), p. 1 (I. INTRODUCTION) |
| Output/action | The VLA takes as input an image and natural language instruction and these are tokenized via the vision and language encoders, and sent to the Llama 2 LLM, which produces continuous and ... | continuous action, pose 또는 action chunk | p. 3 (III. METHOD), p. 1 (I. INTRODUCTION), p. 4 (III. METHOD) |
| Objective/outcome | Hardware We built a $300 6-DOF robotic manipulator (see Figure 3), using brackets on online marketplaces due to cost constraints. | instruction following, task success, generalization과 latency | p. 3 (III. METHOD), p. 2 (III. METHOD), p. 3 (III. METHOD) |

## Main Claims and Actual Contribution

- 이산 행동과 연속 행동 예측의 평균 절대 차이를 불확실성으로 삼아, 예측한 행동 중 몇 단계까지 실행할지 조절한다. [PDF 2쪽](https://arxiv.org/pdf/2511.05397v1#page=2) · [PDF 3쪽](https://arxiv.org/pdf/2511.05397v1#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2511.05397v1#page=4)
- LIBERO와 실제 저비용 팔에서 조작을 시험하고, 실물에서는 익숙한 조건과 물체·장면 등이 바뀐 조건의 성공률을 구분했다. [PDF 4쪽](https://arxiv.org/pdf/2511.05397v1#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2511.05397v1#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2511.05397v1#page=6)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 4 (IV. EXPERIMENTS), p. 6 (V. RESULTS) |
| Embodiment/environment | Baselines On the LIBERO simulation benchmark, we report success rates across all four task suites, comparing against Diffusion Policy [3], Octo [5], DiT Policy [48], OpenVLA [19], and OpenVLA-OFT [35]. | hardware/simulator version and reset protocol | p. 4 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS) |
| Dataset/benchmark | Real-world evaluation results on in-distribution tasks, including picking a block, ball and rock. | role, split, size and leakage | p. 4 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Metric | For all experiments, we use the discrete actions, with the adaptive horizon ensembler (AdaHorizon), which yields higher success rates and improved grasp accuracy compared to continuous-action baselines. | definition, denominator, direction and uncertainty | p. 4 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Baseline/ablation | For all experiments, we use the discrete actions, with the adaptive horizon ensembler (AdaHorizon), which yields higher success rates and improved grasp accuracy compared to continuous-action baselines. | fair input/data/compute/action matching | p. 4 (IV. EXPERIMENTS), p. 6 (V. RESULTS), p. 4 (IV. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 6 / VI. CONCLUSIONS - extractive body cue:** We also experience limitations in executing fine-grained manipulation, which is due to the limited servo precision as well as relatively low number of expert demonstrations ...
- **p. 6 / V. RESULTS - extractive body cue:** The primary failure mode for EverydayVLA is delayed object release and not finishing the task in a timely manner.
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. EveryDayVLA system. Top: EveryDayVLA finetunes a VLA for a low-cost manipulator to generate continuous and discrete actions, which are passed to an adaptive ...
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** In real-world trials, we evaluate both in-distribution and out-of-distribution scenarios against OpenVLA and OpenVLA-OFT.
- **p. 5 / V. RESULTS - extractive body cue:** Method Inference Rate (Hz) ↑ Latency (sec) ↓ OpenVLA [19] 4.2 0.2396 OpenVLA-OFT [35] 109.7 0.0729 Oursli 54.2-108.4 0.0738 TABLE IV GENERALIZATION AND ROBUSTNESS TO ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 2 (III. METHOD), p. 3 (III. METHOD)이다.
