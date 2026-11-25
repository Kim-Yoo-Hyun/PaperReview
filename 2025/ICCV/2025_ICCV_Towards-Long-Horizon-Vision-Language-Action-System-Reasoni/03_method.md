# Method - Towards Long-Horizon Vision-Language-Action System: Reasoning, Acting and Memory

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Li_Towards_Long-Horizon_Vision-Language-Action_System_Reasoning_Acting_and_Memory_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Li_Towards_Long-Horizon_Vision-Language-Action_System_Reasoning_Acting_and_Memory_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Method in One Sentence

PDF body method statement (p. 5 (4.2.1. Multimodal Diffusion Policy), p. 5 (4.2.1. Multimodal Diffusion Policy)): Additionally, we propose a fusion adapters for both the sensor data and text, consisting of two linear layers, to map encoder outputs into an unified feature space.

## Method Body Digest

- **p. 5 / 4.2.1. Multimodal Diffusion Policy - extractive body cue:** Additionally, we propose a fusion adapters for both the sensor data and text, consisting of two linear layers, to map encoder outputs into an unified ...
- **원문 대조:** 학습 시 action에 더한 Gaussian noise ε^k와 denoising network의 예측 사이 MSE를 최소화한다. Denoiser는 noisy action과 diffusion step, RGB·depth·point cloud·instruction·robot state 조건을 사용한다. ([PDF p. 5](https://openaccess.thecvf.com/content/ICCV2025/papers/Li_Towards_Long-Horizon_Vision-Language-Action_System_Reasoning_Acting_and_Memory_ICCV_2025_paper.pdf#page=5), §4.2.1 Multimodal Diffusion Policy, Eq. (9)).
- **p. 2 / 1. Introduction - extractive body cue:** To achieve this, three key challenges must be addressed: (1) Task-oriented Chain of Thought (CoT) reasoning requires the hierarchical decomposition of coarse-grained human instructions into ...
- **p. 5 / 4.2.2. Mixture of Policy Experts - extractive body cue:** The acting layer needs to provide precise feedback to dynamic environmental changes with relatively low model complexity, we argue that a unified manipulation model and ...
- **p. 5 / 4.2.2. Mixture of Policy Experts - extractive body cue:** The arm expert performs meta-actions for grasping and placing, outputting only the pose and velocity parameters for arm manipulation.
- **p. 2 / 1. Introduction - extractive body cue:** On one hand we pursue task-oriented CoT in the Reasoning layer for effectively capturing meta-action sequences, while on the other hand we design a straightforward ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** Our key contributions are summarized as follows: • We propose MindExplore, a novel expert-level hierarchical embodied system to adapt long-horizon tasks in unstructured and dynamic ...
- **p. 2 / 1. Introduction - extractive body cue:** Our MindExplore is inspired by the discovery that continuous iterative alignment of the knowledge domain between task planning and action execution enables strong generalization across ...
- **p. 5 / 4.2.2. Mixture of Policy Experts - extractive body cue:** Therefore, we propose a Mixture of Policy Experts Model that decouples manipulation of the robot's base and arm.

## Source Evidence Cues

- **p. 5 / 4.2.1. Multimodal Diffusion Policy - extractive body cue:** Additionally, we propose a fusion adapters for both the sensor data and text, consisting of two linear layers, to map encoder outputs into an unified ...
- **원문 대조:** 학습 시 action에 더한 Gaussian noise ε^k와 denoising network의 예측 사이 MSE를 최소화한다. Denoiser는 noisy action과 diffusion step, RGB·depth·point cloud·instruction·robot state 조건을 사용한다. ([PDF p. 5](https://openaccess.thecvf.com/content/ICCV2025/papers/Li_Towards_Long-Horizon_Vision-Language-Action_System_Reasoning_Acting_and_Memory_ICCV_2025_paper.pdf#page=5), §4.2.1 Multimodal Diffusion Policy, Eq. (9)).
- **Detected method headings:** 4.2.1. Multimodal Diffusion Policy (p. 5); 4.2.2. Mixture of Policy Experts (p. 5)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Additionally, we propose a fusion adapters for both the sensor data and text, consisting of two linear layers, to map encoder outputs ... | p. 5 (4.2.1. Multimodal Diffusion Policy), p. 5 (4.2.1. Multimodal Diffusion Policy) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | The denoising network ϵθ is then used to predict the random noise ϵk, and the training loss function is as follows: L ... | p. 5 (4.2.1. Multimodal Diffusion Policy) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | Additionally, we propose a fusion adapters for both the sensor data and text, consisting of two linear layers, to map encoder outputs ... | p. 5 (4.2.1. Multimodal Diffusion Policy) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **원문 대조:** 학습 시 action에 더한 Gaussian noise ε^k와 denoising network의 예측 사이 MSE를 최소화한다. Denoiser는 noisy action과 diffusion step, RGB·depth·point cloud·instruction·robot state 조건을 사용한다. ([PDF p. 5](https://openaccess.thecvf.com/content/ICCV2025/papers/Li_Towards_Long-Horizon_Vision-Language-Action_System_Reasoning_Acting_and_Memory_ICCV_2025_paper.pdf#page=5), §4.2.1 Multimodal Diffusion Policy, Eq. (9)).
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 5 (4.2.1. Multimodal Diffusion Policy).

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | achieve, three, challenges, must, addressed, Task-oriented, Chain, Thought, CoT, reasoning, requires, hierarchical, decomposition, coarse-grained | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | achieve, three, challenges, must, addressed, Task-oriented, Chain, Thought, CoT, reasoning | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | contributions, summarized, follows, MindExplore, novel, expert-level, hierarchical, embodied, system, adapt | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | denoising, network, then, predict, random, noise, training, loss, function, follows | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive body cue:** To achieve this, three key challenges must be addressed: (1) Task-oriented Chain of Thought (CoT) reasoning requires the hierarchical decomposition of coarse-grained human instructions into ...
- **p. 5 / 4.2.2. Mixture of Policy Experts - extractive body cue:** The acting layer needs to provide precise feedback to dynamic environmental changes with relatively low model complexity, we argue that a unified manipulation model and ...
- **p. 5 / 4.2.2. Mixture of Policy Experts - extractive body cue:** The arm expert performs meta-actions for grasping and placing, outputting only the pose and velocity parameters for arm manipulation.
- **p. 2 / 1. Introduction - extractive body cue:** On one hand we pursue task-oriented CoT in the Reasoning layer for effectively capturing meta-action sequences, while on the other hand we design a straightforward ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | To achieve this, three key challenges must be addressed: (1) Task-oriented Chain of Thought (CoT) reasoning requires the hierarchical decomposition of coarse-grained ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | During long-horizon tasks, the reasoning layer decomposes the instruction into a structured sequence of executable steps. | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | Besides, the pioneering memory mechanism establishes feedback between the reasoning and acting layers, facilitating adaptive execution of long-horizon tasks and real-time replanning. | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | At a high execution frequency of 30 FPS, MindExplore is 3.01 × more successful than existing methods in unstructured and dynamic environments. | hardware, batch and throughput |

## Training vs Inference

- **원문 대조:** 학습 시 action에 더한 Gaussian noise ε^k와 denoising network의 예측 사이 MSE를 최소화한다. Denoiser는 noisy action과 diffusion step, RGB·depth·point cloud·instruction·robot state 조건을 사용한다. ([PDF p. 5](https://openaccess.thecvf.com/content/ICCV2025/papers/Li_Towards_Long-Horizon_Vision-Language-Action_System_Reasoning_Acting_and_Memory_ICCV_2025_paper.pdf#page=5), §4.2.1 Multimodal Diffusion Policy, Eq. (9)).

## Method-Specific Formal Details

- **Body-defined terms:** Additionally, fusion, adapters, sensor, data, text, consisting, linear, layers, encoder, outputs, unified, feature, space, denoising, network, then, predict, random, noise.
- **Relevant PDF headings:** 4.2.1. Multimodal Diffusion Policy (p. 5); 4.2.2. Mixture of Policy Experts (p. 5).

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | Compared to DeepSeek-VL2 and InternVL2.5, although they are on par with Qwen2-VL in some benchmark indicators, they lack scalability for real-world tasks ... | p. 8 (5.3. Ablation Study), p. 3 (3. The System Dataset) |
| Action / skill decoding | In terms of generalization, compared to end-to-end MLLM and VLAs without world knowledge, MindExplore demonstrates strong generalization capabilities in unseen scenarios. | p. 7 (5.2.1. Performance on Real World Tasks), p. 7 (5.2.1. Performance on Real World Tasks) |
| Receding execution / feedback | As shown in Table 6, the performance of the AE using pure vision declined due to the lack of spatial information, and ... | p. 8 (5.3. Ablation Study), p. 7 (5.2.1. Performance on Real World Tasks) |

## Failure and Ablation Link

- **p. 8 / 5.3. Ablation Study - extractive body cue:** To prove the effectiveness of the Reasoning Layer training method, we performed detailed ablation experiments on three tasks, which involved adding our training methods one ...
- **p. 8 / 5.3. Ablation Study - extractive body cue:** We conduct an ablation study on the core components of the MindExplore system.
- **p. 7 / 5.2.1. Performance on Real World Tasks - extractive body cue:** In terms of generalization, compared to end-to-end MLLM and VLAs without world knowledge, MindExplore demonstrates strong generalization capabilities in unseen scenarios.
- **p. 7 / 5.2.2. Performance of Different Components - extractive body cue:** We also assess the performance of the two key components, reasoning and acting layer.
- **p. 3 / 3. The System Dataset - extractive body cue:** The high dynamic fluidity of sand demands adaptive adjustments, while its visual noise complicates perception and calibration.
- **p. 3 / 3. The System Dataset - extractive body cue:** Enhancing generalization in unstructured environments remains a key challenge, and our experiments show that a system robust in sandy conditions can more easily generalize to ...
- **p. 8 / 5.3. Ablation Study - extractive body cue:** Similarly, the point-cloud-based BE also shows lower success rates, as point cloud data failed to align effectively with the semantic content of instructions.

## Reproduction Checklist

[공통 검토 기준](../../../research/READING_STATUS.md#note-checks)

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (4.2.1. Multimodal Diffusion Policy), p. 5 (4.2.1. Multimodal Diffusion Policy), objective p. 5 (4.2.1. Multimodal Diffusion Policy), temporal p. 2 (1. Introduction), p. 7 (5.2.1. Performance on Real World Tasks), p. 1 (Abstract), p. 7 (5.2.1. Performance on Real World Tasks), p. 1 (Abstract), p. 2 (2.1. Visual Chain-of-Thought).
