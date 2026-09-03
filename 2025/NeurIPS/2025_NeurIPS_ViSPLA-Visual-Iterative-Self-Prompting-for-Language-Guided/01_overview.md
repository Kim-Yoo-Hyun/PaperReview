# ViSPLA: Visual Iterative Self-Prompting for Language-Guided 3D Affordance Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=EyNzLH7BZK.
> PDF retrieval source: https://papers.nips.cc/paper_files/paper/2025/file/5eee634cb9729b8bcc2ec9f2a46a74ae-Paper-Conference.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: Vision-Language Model, Robotics, 3D Vision
- Official paper: https://openreview.net/forum?id=EyNzLH7BZK
- Full-text retrieval: https://papers.nips.cc/paper_files/paper/2025/file/5eee634cb9729b8bcc2ec9f2a46a74ae-Paper-Conference.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 This approach addresses several critical challenges in the field: (1) Existing single-pass inference methods lack the ability to iteratively refine predictions, often leading to suboptimal segmentation, especially on complex geometries; ...를 문제로 두고, In summary, our contributions are: • We introduce Visual Iterative Self-Prompting for 3D Affordance Learning (ViSPLA), which leverages geometric features from predicted masks as visual prompts for progressive refinement.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

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

- **p. 3 / 1 Introduction - extractive body cue:** In summary, our contributions are: • We introduce Visual Iterative Self-Prompting for 3D Affordance Learning (ViSPLA), which leverages geometric features from predicted masks as visual ...
- **p. 3 / 1 Introduction - extractive body cue:** Unlike existing single-pass methods, our approach establishes a self-improving cycle that enhances precision across multiple object geometries. • We propose a novel Differential Geometric Self-Prompting ...
- **p. 2 / 1 Introduction - extractive body cue:** Unlike prior approaches that perform singlepass inference, our method implements a closed-loop system where each predicted affordance mask is used to generate geometric self-prompts that ...
- **p. 2 / 1 Introduction - extractive body cue:** To this end, we propose an iterative self-prompting-based 3D affordance detection paradigm that bridges the gap between language understanding and affordance segmentation through geometric feedback-driven ...
- **p. 1 / Abstract - extractive body cue:** In this work, we introduce ViSPLA, a novel iterative selfprompting framework that leverages the intrinsic geometry of predicted masks for continual refinement.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: Qualitative comparison of our affor- dance segmentation results with GEAL [5]. Our proposed framework achieves consistent and sub- stantial performance improvements across the ...
- **p. 1 / Abstract - extractive body cue:** Extensive experiments demonstrate that ViSPLA achieves state-of-the-art results on both seen and unseen objects on two benchmark datasets.
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 4. (3) The most substantial gains come from incorporating Iterative Differential Geometry-Based Self-Prompting (IDGSP), which provides a significant boost on LASO seen (+2.5 aIoU) ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

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

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 This approach addresses several critical challenges in the field: (1) Existing single-pass inference methods lack the ability to iteratively refine predictions, often leading to suboptimal segmentation, especially on complex geometries; ...를 문제로 두고, In summary, our contributions are: • We introduce Visual Iterative Self-Prompting for 3D Affordance Learning (ViSPLA), which leverages geometric features from predicted masks as visual prompts for progressive refinement.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 3 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
