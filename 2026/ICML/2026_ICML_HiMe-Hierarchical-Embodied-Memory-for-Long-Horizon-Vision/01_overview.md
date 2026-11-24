# HiMe: Hierarchical Embodied Memory for Long-Horizon Vision-Language-Action Control

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://icml.cc/virtual/2026/poster/60897.
> PDF retrieval source: https://openreview.net/pdf/1158a6b1525482f72ae519b3be5d06e0abef1732.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICML
- Authors: Li Ji, Siyin Wang, Pengfang Qian, Xiaopeng Yu, Yihai Tian, Zhaoye Fei, Jingjing Gong, Xipeng Qiu
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, Robotics
- Official paper: https://icml.cc/virtual/2026/poster/60897
- Full-text retrieval: https://arxiv.org/pdf/2607.03449.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 요약과 핵심 기여 두 개를 각 문장에 연결한 판본에서 확인했다.

## Why This Paper Is Here

HiMe는 장기 조작에서 즉시 동작을 실행하는 정책, 작업 기억을 갱신하는 모듈, 장기 전략을 세우는 모듈을 나누어 운영한다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/ji26k/ji26k.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Current Vision-Language-Action (VLA) models excel at robotic manipulation but often struggle with non-Markovian tasks requiring long-term memory and reasoning due to their reliance on immediate ...
- **p. 1 / Abstract - extractive body cue:** Existing solutions face a "frequency-competence paradox," where stronger reasoning models are too slow for real-time control, while faster models lack sufficient reasoning capabilities.
- **p. 1 / Abstract - extractive body cue:** To resolve this architectural misalignment, we propose HiMe, a Hierarchical Embodied Memory framework that decouples embodied intelligence into a high-frequency Executor for execution, a Sentry ...
- **p. 1 / Abstract - extractive body cue:** We also introduce a dynamic knowledge system based on cross-modal semantic schemas and active management mechanisms, allowing robots to maintain memory plasticity through "Add, Update, ...
- **p. 1 / Abstract - extractive body cue:** This hierarchical design effectively balances the conflict between real-time execution and slow thinking planning, significantly improving success rates in long-horizon tasks.
- **p. 2 / 1 Introduction - extractive body cue:** However, these training-based methods are often constrained by limited context windows and the inherent difficulty of optimizing long-range causal dependencies over hundreds of steps.
- **p. 1 / 1 Introduction - extractive body cue:** This inherent limitation prevents them from maintaining a persistent belief of the environment in non-Markovian settings.

## Core Idea

- **p. 3 / 1 Introduction - extractive body cue:** Our core contributions are summarized as follows: • We propose a Hierarchical Memory Management framework that decouples robotic control into transient (Executor), working (Sentry), and ...
- **p. 2 / 1 Introduction - extractive body cue:** 1, motivated by this temporal and scale mismatch, we introduce HiMe, a Hierarchical Embodied Memory framework that decouples embodied intelligence into three functional layers with ...
- **p. 3 / 1 Introduction - extractive body cue:** In contrast to passive storage, we introduce explicit Add, Update, and Delete operations to grant the robot knowledge plasticity.
- **p. 1 / Abstract - extractive body cue:** To resolve this architectural misalignment, we propose HiMe, a Hierarchical Embodied Memory framework that decouples embodied intelligence into a high-frequency Executor for execution, a Sentry ...
- **p. 2 / 1 Introduction - extractive body cue:** This organization allows the Planner to retrieve not only vi2
- **p. 1 / 1 Introduction - extractive body cue:** Most existing architectures rely on the Markov assumption, where the policy 𝑝(𝑎𝑡/𝑜𝑡, 𝑙) predicts the action 𝑎𝑡at time step 𝑡conditioned only on the transient observation ...
- **p. 2 / 1 Introduction - extractive body cue:** To overcome these limitations, one intuitive approach is to imbue VLA models with native memory capabilities through specialized training or auxiliary losses [3, 4].
- **p. 2 / 1 Introduction - extractive body cue:** However, a static memory hierarchy alone is insufficient for the complexities of real-world human-robot interaction, which is characterized by: (1) multimodal richness, where human instructions ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Most existing architectures rely on the Markov assumption, where the policy 𝑝(𝑎𝑡/𝑜𝑡, 𝑙) predicts the action 𝑎𝑡at time step 𝑡conditioned only on the transient observation 𝑜𝑡at the current time step and the ... | image/video, language instruction, proprioception과 history | p. 1 (1 Introduction), p. 2 (1 Introduction) |
| State/latent | Most, existing, architectures, rely, Markov, assumption, where, policy, predicts, action, time, step | language-grounded task state와 action-policy context | p. 1 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract) |
| Output/action | However, a static memory hierarchy alone is insufficient for the complexities of real-world human-robot interaction, which is characterized by: (1) multimodal richness, where human instructions carry dense logical constraints and latent ... | continuous action, pose 또는 action chunk | p. 2 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction) |
| Objective/outcome | This scale constraint, in turn, limits the internal world knowledge and generalization capabilities of the VLM, weakening its zero-shot performance. | instruction following, task success, generalization과 latency | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract) |

## Main Claims and Actual Contribution

- 관측과 언어에서 얻은 기억 항목을 추가·수정·삭제할 수 있게 하고, 각 모듈이 역할에 맞는 주기로 기억을 읽거나 갱신하게 했다. [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/ji26k/ji26k.pdf#page=3) · [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/ji26k/ji26k.pdf#page=4) · [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/ji26k/ji26k.pdf#page=5)
- 긴 조작 과제에서 단일 기억 구조와 비교하고, 사람의 선호가 달라질 때 그에 맞춰 이전에 저장한 지식을 수정하는지 검사했다. [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/ji26k/ji26k.pdf#page=7) · [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/ji26k/ji26k.pdf#page=8) · [PDF 9쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/ji26k/ji26k.pdf#page=9)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 9 (4 Experiments), p. 9 (4 Experiments) |
| Embodiment/environment | After a temporal interval, the robot is tasked with restoring the items to the environment. | hardware/simulator version and reset protocol | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Dataset/benchmark | Without the Sentry, the Planner operates on a frame-by-frame style, and this high-frequency re-evaluation makes the robot hypersensitive to transient visual noise, leading to frequent, erratic switching between subtasks. | role, split, size and leakage | p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments) |
| Metric | HiMe significantly outperforms all baselines, achieving a 90% average success rate. | definition, denominator, direction and uncertainty | p. 9 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments) |
| Baseline/ablation | HiMe significantly outperforms all baselines, achieving a 90% average success rate. | fair input/data/compute/action matching | p. 9 (4 Experiments), p. 10 (4 Experiments), p. 8 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 4 Experiments - extractive body cue:** The fundamental limitation of such contextual memory is the lack of consolidation: a simple FIFO queue cannot distinguish between truly critical frames and redundant observations.
- **p. 9 / 4 Experiments - extractive body cue:** In Counting, even with Sentry stabilization (Transient Memory w/ Sentry), the robot still fails (23%) due to the lack of persistence: without an explicit memory ...
- **p. 12 / 4 Experiments - extractive body cue:** It ensures that execution loops are eventually broken even when the Sentry fails to trigger.
- **p. 12 / 4 Experiments - extractive body cue:** Since the Sentry is prone to False Negatives (missing the "Done" event), we design a fixed-interval Planner fallback.
- **p. 8 / 4 Experiments - extractive body cue:** Without the Sentry, the Planner operates on a frame-by-frame style, and this high-frequency re-evaluation makes the robot hypersensitive to transient visual noise, leading to frequent, ...
- **p. 10 / 4 Experiments - extractive body cue:** HiMe consistently outperforms both text-only and image-only baselines across all three tasks, verifying the robustness of our cross-modal memory mechanism.
- **p. 10 / 4 Experiments - extractive body cue:** Without Update/Delete, memory stores obsolete states (e.g., prior object locations) alongside current ones, introducing noise during Query and potentially confusing the Planner.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 Introduction), p. 1 (1 Introduction), p. 3 (1 Introduction)이다.
