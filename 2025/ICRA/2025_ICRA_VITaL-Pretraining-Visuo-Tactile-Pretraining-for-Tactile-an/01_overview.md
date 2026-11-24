# VITaL Pretraining: Visuo-Tactile Pretraining for Tactile and Non-Tactile Manipulation Policies

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://api.crossref.org/works/10.1109/icra55743.2025.11128336.
> PDF retrieval source: https://arxiv.org/pdf/2403.11898v2. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICRA
- Authors: Abraham George, Selam Gano, Pranav Katragadda, Amir Barati Farimani
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: Robotics
- Official paper: https://api.crossref.org/works/10.1109/icra55743.2025.11128336
- Full-text retrieval: https://arxiv.org/pdf/2403.11898v2
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 요약과 핵심 기여 두 개를 각 문장에 연결한 판본에서 확인했다.

## Why This Paper Is Here

VITaL은 시연에 동기화된 영상과 촉각을 사전학습에 사용했을 때 실행 중 영상을 쓰는 조작 정책에도 이득이 전달되는지 검증한다. [PDF 1쪽](https://arxiv.org/pdf/2403.11898v2#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Tactile information is a critical tool for dexterous manipulation.
- **p. 1 / Abstract - extractive body cue:** As humans, we rely heavily on tactile information to understand objects in our environments and how to interact with them.
- **p. 1 / Abstract - extractive body cue:** We use touch not only to perform manipulation tasks but also to learn how to perform these tasks.
- **p. 1 / Abstract - extractive body cue:** Therefore, to create robotic agents that can learn to complete manipulation tasks at a human or super-human level of performance, we need to properly incorporate ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we investigate how we can incorporate tactile information into imitation learning platforms to improve performance on manipulation tasks.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Achieving proficiency in complex manipulation tasks remains a longstanding challenge in robotics, with applications ranging from industrial automation to clay sculpting [1], [2].
- **p. 1 / I. INTRODUCTION - extractive body cue:** Critical to addressing this challenge is the integration of tactile information, which provides both an understanding of the objects being interacted with and a detailed ...

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** Next, we propose a new methodology for using tactile data in imitation learning: VITaL (Vison-only Imitation using Tactile Latent) pretraining, in which we discard the ...
- **p. 3 / III. METHODS - extractive body cue:** A vision projection head, pϕV : Z →L, and a tactile projection head, qϕT : Z, P →L, each of which consists of a single ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Our primary contribution is a pretraining strategy for these SOTA imitation learning frameworks, leveraging the multimodal nature of our data to incorporate a temporalbased visual-tactile ...
- **p. 4 / III. METHODS - extractive body cue:** 2) Diffusion Policy: Our approach to diffusion policy was based on the implementation by [11] that generates action sequences conditioned on observations with DDPM.
- **p. 4 / III. METHODS - extractive body cue:** We used the Oculus Virtual Reality (VR) teleoperation pipeline developed by [38], which tracks the Quest's controller using the headset.
- **p. 3 / III. METHODS - extractive body cue:** First, we replaced the stock Resnet vision encoder with the vision encoder from the contrastive pretraining step and added a separate tactile encoder (also from ...
- **p. 2 / 1) Action - extractive body cue:** Chunking Transformers: Action Chunking Transformers (ACT) [10] train a Conditional Variational Auto Encoder (CVAE) built upon a transformer backbone to predict a series of actions ...
- **p. 2 / 1) Action - extractive body cue:** 2) Diffusion Policy: To address the challenge of complex multi-modal action spaces, Diffusion Policy [11] formulates control policies as Denoising Diffusion Probabilistic Models (DDPM) [35], ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Chunking Transformers: Action Chunking Transformers (ACT) [10] train a Conditional Variational Auto Encoder (CVAE) built upon a transformer backbone to predict a series of actions (in the form of goal positions) conditioned ... | tactile image/force, vision과 proprioceptive history | p. 2 (1) Action), p. 4 (III. METHODS) |
| State/latent | Chunking, Transformers, Action, ACT, train, Conditional, Variational, Auto, Encoder, CVAE, built, upon | contact geometry, force state 또는 latent dynamics | p. 2 (1) Action), p. 4 (III. METHODS), p. 2 (1) Action) |
| Output/action | 2) Diffusion Policy: Our approach to diffusion policy was based on the implementation by [11] that generates action sequences conditioned on observations with DDPM. | grasp/contact action, force command 또는 object motion | p. 4 (III. METHODS), p. 2 (1) Action), p. 1 (I. INTRODUCTION) |
| Objective/outcome | The encoders (and the projection heads) are then trained to maximize the cross-modality dot-product similarity of latent representations from the same scene while minimizing the crossmodality similarity of latent representations from di ... | slip/contact success, force/pose error와 robustness | p. 3 (III. METHODS), p. 2 (1) Action), p. 3 (III. METHODS) |

## Main Claims and Actual Contribution

- 시각·촉각을 함께 학습한 뒤 실행 시 촉각을 사용하는 정책과 사용하지 않는 정책을 나누어 모방학습의 효과를 비교했다. [PDF 3쪽](https://arxiv.org/pdf/2403.11898v2#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2403.11898v2#page=4)
- 실물 케이블 삽입에서 실행 시 촉각을 받지 않는 ACT의 성공률이 촉각 사전학습 후 20%에서 85%로 높아졌고, 같은 조건의 확산 정책은 45%에서 75%로 높아졌다. [PDF 5쪽](https://arxiv.org/pdf/2403.11898v2#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2403.11898v2#page=6)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 5 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION) |
| Embodiment/environment | In this task, the robot has to navigate to a USB cable, unplug it from its holder, and plug it into the last port of a USB hub. | hardware/simulator version and reset protocol | p. 5 (IV. EXPERIMENTAL EVALUATION), p. 5 (IV. EXPERIMENTAL EVALUATION) |
| Dataset/benchmark | For both pretrained and non-pretrained tactileonly diffusion policies, the robot would pick up the USB cable, but then would alternate between trying to move back to the USB holder, trying to move ... | role, split, size and leakage | p. 5 (IV. EXPERIMENTAL EVALUATION), p. 5 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION) |
| Metric | Comparing the two imitation learning methods, we found that Diffusion Policy's success rate was less sensitive than ACT, with a higher accuracy for the non-pretrained visiononly policy (where ACT did quite poorly), ... | definition, denominator, direction and uncertainty | p. 5 (IV. EXPERIMENTAL EVALUATION), p. 5 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION) |
| Baseline/ablation | Interestingly, the nonpretrained ACT model outperformed the pretrained model in this task. | fair input/data/compute/action matching | p. 5 (IV. EXPERIMENTAL EVALUATION), p. 5 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION) |

## Explicit Limitations and Failure Boundary

- **p. 6 / V. CONCLUSIONS - extractive body cue:** A major limitation of this work is that task-specific data was used for pretraining.
- **p. 5 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** Although this is relatively small in absolute terms, it corresponds to a 50% and 20% decrease in failures for ACT and Diffusion Policy, respectively.
- **p. 6 / V. CONCLUSIONS - extractive body cue:** Evaluating this alternative approach is left for future work.
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3. Imitation learning networks. ACT (left) is trained as an autoencoder, predicting a sequence of actions at each timestep (at). At inference, the latent ...
- **p. 5 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** To increase the task's difficulty, we added random noise with a standard deviation of 2.5mm to the agent's actions during inference.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 3 (III. METHODS), p. 2 (1) Action)이다.
