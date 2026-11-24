# ViSPLA: Visual Iterative Self-Prompting for Language-Guided 3D Affordance Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://neurips.cc/virtual/2025/poster/119081.
> PDF retrieval source: https://papers.nips.cc/paper_files/paper/2025/file/5eee634cb9729b8bcc2ec9f2a46a74ae-Paper-Conference.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / NeurIPS
- Authors: Hritam Basak, Zhaozheng Yin
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: Vision-Language Model, Robotics, 3D Vision
- Official paper: https://neurips.cc/virtual/2025/poster/119081
- Full-text retrieval: https://papers.nips.cc/paper_files/paper/2025/file/5eee634cb9729b8bcc2ec9f2a46a74ae-Paper-Conference.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 요약과 핵심 기여 두 개를 각 문장에 연결한 판본에서 확인했다.

## Why This Paper Is Here

ViSPLA는 점군에서 언어 지시에 맞는 행동 가능 영역을 분할하고, 예측 마스크의 기하를 다음 단계의 입력으로 써서 영역을 다듬는다. [PDF 1쪽](https://papers.nips.cc/paper_files/paper/2025/file/5eee634cb9729b8bcc2ec9f2a46a74ae-Paper-Conference.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We address the problem of language-guided 3D affordance prediction, a core capability for embodied agents interacting with unstructured environments.
- **p. 1 / Abstract - extractive body cue:** Existing methods often rely on fixed affordance categories or require external expert prompts, limiting their ability to generalize across different objects and interpret multi-step instructions.
- **p. 1 / Abstract - extractive body cue:** In this work, we introduce ViSPLA, a novel iterative selfprompting framework that leverages the intrinsic geometry of predicted masks for continual refinement.
- **p. 1 / Abstract - extractive body cue:** We redefine affordance detection as a language-conditioned segmentation task: given a 3D point cloud and language instruction, our model predicts a sequence of refined affordance ...
- **p. 1 / Abstract - extractive body cue:** This feedback is encoded into visual prompts that drive a multi-stage refinement decoder, enabling the model to self-correct and adapt to complex spatial structures.
- **p. 2 / 1 Introduction - extractive body cue:** This approach addresses several critical challenges in the field: (1) Existing single-pass inference methods lack the ability to iteratively refine predictions, often leading to suboptimal ...
- **p. 3 / 1 Introduction - extractive body cue:** accuracy, especially in complex or ambiguous settings; (3) the disconnect between high-level language semantics and low-level geometric features, hindering precise and context-aware affordance prediction across ...

## Core Idea

- **p. 3 / 1 Introduction - extractive body cue:** In summary, our contributions are: • We introduce Visual Iterative Self-Prompting for 3D Affordance Learning (ViSPLA), which leverages geometric features from predicted masks as visual ...
- **p. 3 / 1 Introduction - extractive body cue:** Unlike existing single-pass methods, our approach establishes a self-improving cycle that enhances precision across multiple object geometries. • We propose a novel Differential Geometric Self-Prompting ...
- **p. 2 / 1 Introduction - extractive body cue:** Unlike prior approaches that perform singlepass inference, our method implements a closed-loop system where each predicted affordance mask is used to generate geometric self-prompts that ...
- **p. 2 / 1 Introduction - extractive body cue:** To this end, we propose an iterative self-prompting-based 3D affordance detection paradigm that bridges the gap between language understanding and affordance segmentation through geometric feedback-driven ...
- **p. 1 / Abstract - extractive body cue:** In this work, we introduce ViSPLA, a novel iterative selfprompting framework that leverages the intrinsic geometry of predicted masks for continual refinement.
- **p. 3 / 1 Introduction - extractive body cue:** By injecting LLM reasoning into dense point features, our approach bridges high-level semantic understanding with low-level geometric representation. • We introduce an Implicit Neural Affordance ...
- **p. 1 / Abstract - extractive body cue:** This feedback is encoded into visual prompts that drive a multi-stage refinement decoder, enabling the model to self-correct and adapt to complex spatial structures.
- **p. 1 / 1 Introduction - extractive body cue:** Although conventional methodologies have predominantly focused on visual modalities, attempting to infer functionality from geometric structures or 2D visual features, such approaches inherently lack the ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We redefine affordance detection as a language-conditioned segmentation task: given a 3D point cloud and language instruction, our model predicts a sequence of refined affordance masks, each guided by differential geometric feedback ... | image/video, language instruction, proprioception과 history | p. 1 (Abstract), p. 2 (1 Introduction) |
| State/latent | redefine, affordance, detection, language-conditioned, segmentation, task, given, point, cloud, language, instruction, model | language-grounded task state와 action-policy context | p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Output/action | To this end, we propose an iterative self-prompting-based 3D affordance detection paradigm that bridges the gap between language understanding and affordance segmentation through geometric feedback-driven refinement, as shown in Figure ... | continuous action, pose 또는 action chunk | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction) |
| Objective/outcome | Recent progress in Large Language Models (LLMs) has shown impressive capabilities in sequential reasoning and knowledge grounding [7], but these models are often decoupled from 3D perception. | instruction following, task success, generalization과 latency | p. 2 (1 Introduction), p. 3 (1 Introduction) |

## Main Claims and Actual Contribution

- 표면 곡률과 법선 변화 등 마스크의 기하 특징을 시각 프롬프트로 만들고 여러 해상도에서 예측을 반복 갱신한다. [PDF 4쪽](https://papers.nips.cc/paper_files/paper/2025/file/5eee634cb9729b8bcc2ec9f2a46a74ae-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://papers.nips.cc/paper_files/paper/2025/file/5eee634cb9729b8bcc2ec9f2a46a74ae-Paper-Conference.pdf#page=5) · [PDF 6쪽](https://papers.nips.cc/paper_files/paper/2025/file/5eee634cb9729b8bcc2ec9f2a46a74ae-Paper-Conference.pdf#page=6)
- 연속적인 표면 위의 행동 가능 확률을 학습하고, 학습 때 본 물체와 새로운 물체에서 마스크 정확도 및 구성요소의 영향을 평가했다. [PDF 7쪽](https://papers.nips.cc/paper_files/paper/2025/file/5eee634cb9729b8bcc2ec9f2a46a74ae-Paper-Conference.pdf#page=7) · [PDF 8쪽](https://papers.nips.cc/paper_files/paper/2025/file/5eee634cb9729b8bcc2ec9f2a46a74ae-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://papers.nips.cc/paper_files/paper/2025/file/5eee634cb9729b8bcc2ec9f2a46a74ae-Paper-Conference.pdf#page=9) · [PDF 10쪽](https://papers.nips.cc/paper_files/paper/2025/file/5eee634cb9729b8bcc2ec9f2a46a74ae-Paper-Conference.pdf#page=10)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (Figure/Table caption), p. 1 (Abstract) |
| Embodiment/environment | Extensive experiments demonstrate that ViSPLA achieves state-of-the-art results on both seen and unseen objects on two benchmark datasets. | hardware/simulator version and reset protocol | p. 1 (Abstract), p. 1 (1 Introduction) |
| Dataset/benchmark | Details can be found in section 3. limitation that inhibits the deployment of autonomous agents in real-world contexts. | role, split, size and leakage | p. 1 (Abstract), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Metric | accuracy, especially in complex or ambiguous settings; (3) the disconnect between high-level language semantics and low-level geometric features, hindering precise and context-aware affordance prediction across multiple scales; and (4) ... | definition, denominator, direction and uncertainty | p. 3 (1 Introduction), p. 3 (1 Introduction), p. 1 (Abstract) |
| Baseline/ablation | Extensive experiments demonstrate that ViSPLA achieves state-of-the-art results on both seen and unseen objects on two benchmark datasets. | fair input/data/compute/action matching | p. 1 (Abstract), p. 1 (Abstract), p. 3 (1 Introduction) |

## Explicit Limitations and Failure Boundary

- **p. 2 / 1 Introduction - extractive body cue:** Details can be found in section 3. limitation that inhibits the deployment of autonomous agents in real-world contexts.
- **p. 2 / 1 Introduction - extractive body cue:** The final refined mask MT integrates both semantic guidance and geometric consistency, enabling robust and generalizable affordance segmentation across varying levels of granularity and complexity.
- **p. 3 / 1 Introduction - extractive body cue:** In tandem, our Spectral Convolutional Self-Prompting module analyzes and enhances affordance predictions at multiple structural scales, enabling the model to capture both broad shapes and ...
- **p. 6 / 2 Related Work - extractive body cue:** 3.5 Overall Learning Strategy To effectively address data scarcity and ensure robust affordance understanding, we adopt a multistage training strategy inspired by 3D-AffordanceLLM [6].
- **p. 7 / 2 Related Work - extractive body cue:** This design enables evaluation of our model's robustness in both instruction-conditioned and shape-driven generalization scenarios.
- **p. 8 / 2 Related Work - extractive body cue:** Earlier fusion-based approaches like [33-38] exhibit significantly inferior performance due to their generic multimodal architectures that fail to model the specialized nature of affordance relationships.
- **p. 9 / 2 Related Work - extractive body cue:** to bridge the geometric-semantic gap, resulting in substantial performance degradation (relative aIoU dropping by more than 50% compared to our method).

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 Introduction), p. 3 (1 Introduction), p. 1 (1 Introduction)이다.
