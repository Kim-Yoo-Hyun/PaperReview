# Towards Long-Horizon Vision-Language-Action System: Reasoning, Acting and Memory

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Li_Towards_Long-Horizon_Vision-Language-Action_System_Reasoning_Acting_and_Memory_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Li_Towards_Long-Horizon_Vision-Language-Action_System_Reasoning_Acting_and_Memory_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: Daixun Li, Yusi Zhang, Mingxiang Cao, Donglai Liu, Weiying Xie, Tianlin Hui, Lunkai Lin, Zhiqiang Xie, Yunsong Li
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Li_Towards_Long-Horizon_Vision-Language-Action_System_Reasoning_Acting_and_Memory_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Li_Towards_Long-Horizon_Vision-Language-Action_System_Reasoning_Acting_and_Memory_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: system
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Why This Paper Is Here

문제 관련 발췌 — Consequently, this remains an open and worthwhile challenge so far.

방법 관련 발췌 — Our key contributions are summarized as follows: • We propose MindExplore, a novel expert-level hierarchical embodied system to adapt long-horizon tasks in unstructured and dynamic environments.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Vision-Language-Action (VLA) is crucial for autonomous decision-making in embodied systems.
- **p. 1 / Abstract - extractive body cue:** While current methods have advanced single-skill abilities, their short-horizon capability limits applicability in real-world scenarios.
- **p. 1 / Abstract - extractive body cue:** To address this challenge, we innovatively propose MindExplore, a general hierarchical VLA system with cross-skill for long-horizon tasks in highly dynamic sand.
- **p. 1 / Abstract - extractive body cue:** The key insight is to iteratively align the knowledge domain of task planning and action execution.
- **p. 1 / Abstract - extractive body cue:** Thus, this task-oriented action enables outstanding generalization across a wide range of real-world scenarios.
- **p. 2 / 1. Introduction - extractive body cue:** Consequently, this remains an open and worthwhile challenge so far.
- **p. 2 / 1. Introduction - extractive body cue:** However, these approaches fail to generalize for long-horizon tasks in real-world scenarios, particularly in complex terrain action [14, 33].

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our key contributions are summarized as follows: • We propose MindExplore, a novel expert-level hierarchical embodied system to adapt long-horizon tasks in unstructured and dynamic ...
- **p. 2 / 1. Introduction - extractive body cue:** Our MindExplore is inspired by the discovery that continuous iterative alignment of the knowledge domain between task planning and action execution enables strong generalization across ...
- **p. 5 / 4.2.2. Mixture of Policy Experts - extractive body cue:** Therefore, we propose a Mixture of Policy Experts Model that decouples manipulation of the robot's base and arm.
- **p. 5 / 4.2.1. Multimodal Diffusion Policy - extractive body cue:** To address these, we propose a multimodal diffusion Policy model (MMDP) that jointly exploits information of multi-sensor data and textual instructions.
- **p. 5 / 4.2.1. Multimodal Diffusion Policy - extractive body cue:** Additionally, we propose a fusion adapters for both the sensor data and text, consisting of two linear layers, to map encoder outputs into an unified ...
- **원문 대조:** 학습 시 action에 더한 Gaussian noise ε^k와 denoising network의 예측 사이 MSE를 최소화한다. Denoiser는 noisy action과 diffusion step, RGB·depth·point cloud·instruction·robot state 조건을 사용한다. ([PDF p. 5](https://openaccess.thecvf.com/content/ICCV2025/papers/Li_Towards_Long-Horizon_Vision-Language-Action_System_Reasoning_Acting_and_Memory_ICCV_2025_paper.pdf#page=5), §4.2.1 Multimodal Diffusion Policy, Eq. (9)).

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | To achieve this, three key challenges must be addressed: (1) Task-oriented Chain of Thought (CoT) reasoning requires the hierarchical decomposition of coarse-grained human instructions into executable sequences of metaactions, ensuring ... | image/video, language instruction, proprioception과 history | p. 2 (1. Introduction), p. 5 (4.2.2. Mixture of Policy Experts) |
| State/latent | achieve, three, challenges, must, addressed, Task-oriented, Chain, Thought, CoT, reasoning, requires, hierarchical | language-grounded task state와 action-policy context | p. 2 (1. Introduction), p. 5 (4.2.2. Mixture of Policy Experts), p. 5 (4.2.2. Mixture of Policy Experts) |
| Output/action | The acting layer needs to provide precise feedback to dynamic environmental changes with relatively low model complexity, we argue that a unified manipulation model and unfiltered sensor inputs may interfere with the ... | continuous action, pose 또는 action chunk | p. 5 (4.2.2. Mixture of Policy Experts), p. 5 (4.2.2. Mixture of Policy Experts), p. 2 (1. Introduction) |
| Training objective | 원문 대조: 학습 시 action에 더한 Gaussian noise ε^k와 denoising network의 예측 사이 MSE를 최소화한다. Denoiser는 noisy action과 diffusion step, RGB·depth·point cloud·instruction·robot state 조건을 사용한다. ([PDF p. 5](https://openaccess.thecvf.com/content/ICCV2025/papers/Li_Towards_Long-Horizon_Vision-Language-Action_System_Reasoning_Acting_and_Memory_ICCV_2025_paper.pdf#page=5), §4.2.1 Multimodal Diffusion Policy, Eq. (9)) | Action noise MSE; task success 수치와 구분 | [PDF p. 5](https://openaccess.thecvf.com/content/ICCV2025/papers/Li_Towards_Long-Horizon_Vision-Language-Action_System_Reasoning_Acting_and_Memory_ICCV_2025_paper.pdf#page=5), §4.2.1 Multimodal Diffusion Policy, Eq. (9) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Our key contributions are summarized as follows: • We propose MindExplore, a novel expert-level hierarchical embodied system to adapt long-horizon tasks in unstructured and dynamic ...
- **p. 2 / 1. Introduction - extractive body cue:** Our MindExplore is inspired by the discovery that continuous iterative alignment of the knowledge domain between task planning and action execution enables strong generalization across ...
- **p. 5 / 4.2.2. Mixture of Policy Experts - extractive body cue:** Therefore, we propose a Mixture of Policy Experts Model that decouples manipulation of the robot's base and arm.
- **p. 5 / 4.2.1. Multimodal Diffusion Policy - extractive body cue:** To address these, we propose a multimodal diffusion Policy model (MMDP) that jointly exploits information of multi-sensor data and textual instructions.
- **p. 8 / 5.3. Ablation Study - extractive body cue:** As shown in Table 6, the performance of the AE using pure vision declined due to the lack of spatial information, and the RGB-based BE ...
- **p. 7 / 5.2.1. Performance on Real World Tasks - extractive body cue:** In multi-skill coordination, MindExplore outperforms single-expert models with a higher success rate due to the MoPE.
- **p. 8 / 5.2.2. Performance of Different Components - extractive body cue:** By combining spatial information with color and texture information from RGB images, the BE and AE achieve better alignment between object semantics and text instructions ...
- **p. 7 / 5.2.1. Performance on Real World Tasks - extractive body cue:** As shown in Table 1, in instruction-following, MindExplore's performance improves as instruction granularity increases, whereas OpenVLA and RDT perform better with coarse-grained instructions than with ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (5.3. Ablation Study), p. 7 (5.2.1. Performance on Real World Tasks) |
| Embodiment/environment | Compared to DeepSeek-VL2 and InternVL2.5, although they are on par with Qwen2-VL in some benchmark indicators, they lack scalability for real-world tasks in embodied systems, such as spatial calibration, semantic perception, and ... | hardware/simulator version and reset protocol | p. 8 (5.3. Ablation Study), p. 3 (3. The System Dataset) |
| Dataset/benchmark | To address Challenge 3, we collect a multi-task embodied operation dataset SandGo-1k, using a tracked mobile robot with a single-arm manipulator (as shown in Figure 2) in a real sand. | role, split, size and leakage | p. 8 (5.3. Ablation Study), p. 3 (3. The System Dataset), p. 3 (3. The System Dataset), p. 6 (5.2.1. Performance on Real World Tasks) |
| Metric | However, without timely state feedback and error correction from acting layer, the system is highly susceptible to error accumulation, resulting in a decrease in success rate. | definition, denominator, direction and uncertainty | p. 8 (5.3. Ablation Study), p. 8 (5.3. Ablation Study), p. 6 (5.1. Implementation Details) |
| Baseline/ablation | In terms of generalization, compared to end-to-end MLLM and VLAs without world knowledge, MindExplore demonstrates strong generalization capabilities in unseen scenarios. | fair input/data/compute/action matching | p. 7 (5.2.1. Performance on Real World Tasks), p. 7 (5.2.1. Performance on Real World Tasks), p. 8 (5.3. Ablation Study) |

## Explicit Limitations and Failure Boundary

- **p. 3 / 3. The System Dataset - extractive body cue:** The high dynamic fluidity of sand demands adaptive adjustments, while its visual noise complicates perception and calibration.
- **p. 3 / 3. The System Dataset - extractive body cue:** Enhancing generalization in unstructured environments remains a key challenge, and our experiments show that a system robust in sandy conditions can more easily generalize to ...
- **p. 8 / 5.3. Ablation Study - extractive body cue:** Similarly, the point-cloud-based BE also shows lower success rates, as point cloud data failed to align effectively with the semantic content of instructions.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 5 (4.2.1. Multimodal Diffusion Policy), p. 8 (5.3. Ablation Study), p. 7 (5.2.1. Performance on Real World Tasks)이다.
