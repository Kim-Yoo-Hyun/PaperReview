# Method - Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2026/hash/d676c05a8fb93ad9231508d95567c498-Abstract-Conference.html; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/248008. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Method in One Sentence

- **원문 대조:** Preliminary formulation에서 action token은 visual token, language token, 앞선 action token에 조건화해 생성된다. 이는 VLA 기본 interface 설명이며 Spatial Forcing의 representation-alignment objective 자체와 구분한다. ([PDF p. 3](https://arxiv.org/pdf/2510.12276#page=3), §2.1 Preliminaries, Eq. (1)).

## Method Body Digest

- **원문 대조:** Preliminary formulation에서 action token은 visual token, language token, 앞선 action token에 조건화해 생성된다. 이는 VLA 기본 interface 설명이며 Spatial Forcing의 representation-alignment objective 자체와 구분한다. ([PDF p. 3](https://arxiv.org/pdf/2510.12276#page=3), §2.1 Preliminaries, Eq. (1)).
- **p. 4 / 2.1 PRELIMINARIES - extractive body cue:** To provide the signals with rich spatial information, we first input a set of multi-view images I into the pretrained 3D foundation model VGGT f ...
- **p. 5 / 2.1 PRELIMINARIES - extractive body cue:** The final training objective combines both the standard training loss for action generation and the 3D foundation model alignment loss with a weighting factor α: ...
- **p. 4 / 2.1 PRELIMINARIES - extractive body cue:** To align the VLA's per-pixel visual tokens with this 3D foundation model, we first process each xi with batch normalization Γ followed by a two-layer ...
- **p. 3 / 2.1 PRELIMINARIES - extractive body cue:** It is composed of a transformer backbone and multiple prediction heads.
- **p. 8 / 2.1 PRELIMINARIES - extractive body cue:** To ensure fairness, we use the cosine-annealing rather than a multi-step training scheduler.
- **p. 7 / 2.1 PRELIMINARIES - extractive body cue:** In contrast, constraining shallow features may cause the already aligned representations to gradually lose spatial information in subsequent layers.
- **p. 3 / 2.1 PRELIMINARIES - extractive body cue:** L1, L2, or cross-entropy loss), G denotes the trainable action expert (e.g. two-layer MLP or flow-matching head (Lipman et al., 2022)).

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To bridge the gap, we propose Spatial Forcing (SF), a simple yet effective alignment strategy that implicitly forces VLA models to acquire spatial-aware knowledge.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Additional experiments on training iterations and dataset sizes indicate that our method realizes 3.8× training while also exhibiting data efficiency with significantly less data.
- **p. 3 / 2.1 PRELIMINARIES - extractive body cue:** The text modality consists of task instructions, which are converted into M linguistic tokens {xL t }M t=1 by a text tokenizer.

## Source Evidence Cues

- **원문 대조:** Preliminary formulation에서 action token은 visual token, language token, 앞선 action token에 조건화해 생성된다. 이는 VLA 기본 interface 설명이며 Spatial Forcing의 representation-alignment objective 자체와 구분한다. ([PDF p. 3](https://arxiv.org/pdf/2510.12276#page=3), §2.1 Preliminaries, Eq. (1)).
- **p. 4 / 2.1 PRELIMINARIES - extractive body cue:** To provide the signals with rich spatial information, we first input a set of multi-view images I into the pretrained 3D foundation model VGGT f ...
- **p. 5 / 2.1 PRELIMINARIES - extractive body cue:** The final training objective combines both the standard training loss for action generation and the 3D foundation model alignment loss with a weighting factor α: ...
- **p. 4 / 2.1 PRELIMINARIES - extractive body cue:** To align the VLA's per-pixel visual tokens with this 3D foundation model, we first process each xi with batch normalization Γ followed by a two-layer ...
- **p. 3 / 2.1 PRELIMINARIES - extractive body cue:** It is composed of a transformer backbone and multiple prediction heads.
- **p. 8 / 2.1 PRELIMINARIES - extractive body cue:** To ensure fairness, we use the cosine-annealing rather than a multi-step training scheduler.
- **p. 7 / 2.1 PRELIMINARIES - extractive body cue:** In contrast, constraining shallow features may cause the already aligned representations to gradually lose spatial information in subsequent layers.
- **Detected method headings:** 2 METHOD (p. 3); A THE USE OF LARGE LANGUAGE MODELS (LLMS) (p. 15)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Then, the VLA models generate K action tokens {xA t }K t=1 conditioned on the preceding visual and linguistic tokens: xA t ... | p. 3 (2.1 PRELIMINARIES), p. 4 (2.1 PRELIMINARIES) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | To provide the signals with rich spatial information, we first input a set of multi-view images I into the pretrained 3D foundation ... | p. 4 (2.1 PRELIMINARIES), p. 5 (2.1 PRELIMINARIES) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | The final training objective combines both the standard training loss for action generation and the 3D foundation model alignment loss with a ... | p. 5 (2.1 PRELIMINARIES), p. 4 (2.1 PRELIMINARIES) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 2.1 PRELIMINARIES - extractive body cue:** The final training objective combines both the standard training loss for action generation and the 3D foundation model alignment loss with a weighting factor α: ...
- **p. 3 / 2.1 PRELIMINARIES - extractive body cue:** L1, L2, or cross-entropy loss), G denotes the trainable action expert (e.g. two-layer MLP or flow-matching head (Lipman et al., 2022)).
- **원문 대조:** Preliminary formulation에서 action token은 visual token, language token, 앞선 action token에 조건화해 생성된다. 이는 VLA 기본 interface 설명이며 Spatial Forcing의 representation-alignment objective 자체와 구분한다. ([PDF p. 3](https://arxiv.org/pdf/2510.12276#page=3), §2.1 Preliminaries, Eq. (1)).
- **p. 4 / 2.1 PRELIMINARIES - extractive body cue:** Then we employ a cosine similarity score to maximize the alignment between the visual tokens of VLA and the spatial representation signals: Lalign = -1 ...
- **p. 4 / 2.1 PRELIMINARIES - extractive body cue:** Additionally, as there are multiple causal attention layers in the VLA model, there are multiple xV that can be gained after different layers.
- **p. 7 / 2.1 PRELIMINARIES - extractive body cue:** Our VLM backbone (Karamcheti et al., 2024) contains 32 causal attention layers.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 5 (2.1 PRELIMINARIES), p. 3 (2.1 PRELIMINARIES), p. 3 (2.1 PRELIMINARIES).

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | provide, signals, rich, spatial, information, first, input, multi-view, images, pretrained, foundation, model, VGGT, outputs | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | provide, signals, rich, spatial, information, first, input, multi-view, images, pretrained | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | bridge, Spatial, Forcing, simple, effective, alignment, strategy, implicitly, forces, VLA | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | final, training, objective, combines, standard, loss, action, generation, foundation, model | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 2.1 PRELIMINARIES - extractive body cue:** To provide the signals with rich spatial information, we first input a set of multi-view images I into the pretrained 3D foundation model VGGT f ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Recently, vision-language-action (VLA) models (Brohan et al., 2022; Zitkovich et al., 2023; Bjorck et al., 2025; Black et al., 2024), capable of instruction following and ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Most VLA models are built upon vision-language models (VLMs) (Liu et al., 2023b; Chen et al., 2023; Karamcheti et al., 2024) to inherit semantic understanding ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Text Tokenizer Image Tokenizer VLA Layer i VLA Layer i+1 Action … … w/o SF w/ SF GT Figure 1: Our proposed method, Spatial Forcing ...
- **p. 3 / 2.1 PRELIMINARIES - extractive body cue:** 2(b)) attempt to estimate 3D information from 2D images, but their capabilities are limited by the performance of the depth estimators, which makes the policy ...
- **p. 3 / 2.1 PRELIMINARIES - extractive body cue:** VGGT (Wang et al., 2025b) is a feedforward model that directly outputs various 3D attributes of a scene, including camera parameters, point maps, depth maps, ...
- **p. 4 / 2.1 PRELIMINARIES - extractive body cue:** 3, the probing results show that visual embeddings learned solely from 2D images do not produce meaningful spatial structures, suggesting a limited capacity of the ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | For each frame, local and global features are integrated into a unified latent representation, which is subsequently processed by a set of ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | A θ-parameterized VLM model employs multiple causal attention layers in an auto-regressive manner to generate the next tokens, formed as xt ∼pθ(xt ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | Each task suite contains 500 expert demonstrations across 10 tasks to investigate policy generalization to different spatial layouts, objects, goals, and long-horizon ... | hardware, batch and throughput |

## Training vs Inference

- **원문 대조:** Preliminary formulation에서 action token은 visual token, language token, 앞선 action token에 조건화해 생성된다. 이는 VLA 기본 interface 설명이며 Spatial Forcing의 representation-alignment objective 자체와 구분한다. ([PDF p. 3](https://arxiv.org/pdf/2510.12276#page=3), §2.1 Preliminaries, Eq. (1)).
- **p. 4 / 2.1 PRELIMINARIES - extractive body cue:** To provide the signals with rich spatial information, we first input a set of multi-view images I into the pretrained 3D foundation model VGGT f ...
- **p. 5 / 2.1 PRELIMINARIES - extractive body cue:** The final training objective combines both the standard training loss for action generation and the 3D foundation model alignment loss with a weighting factor α: ...
- **p. 8 / 2.1 PRELIMINARIES - extractive body cue:** To ensure fairness, we use the cosine-annealing rather than a multi-step training scheduler.
- **p. 7 / 2.1 PRELIMINARIES - extractive body cue:** In contrast, constraining shallow features may cause the already aligned representations to gradually lose spatial information in subsequent layers.
- **p. 3 / 2.1 PRELIMINARIES - extractive body cue:** The vision modality consists of multi-view images captured by robots, which are transformed into N visual tokens {xV t }N t=1 through pretrained visual encoders ...

## Method-Specific Formal Details

- **Body-defined terms:** Then, VLA, models, generate, action, tokens, conditioned, preceding, visual, linguistic, Laction, Agt, where, denotes, training, loss, provide, signals, rich, spatial.
- **Relevant PDF headings:** 2 METHOD (p. 3); A THE USE OF LARGE LANGUAGE MODELS (LLMS) (p. 15).

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | Given the scarcity of real-world data, this capability is particularly valuable for robotic applications. | p. 8 (2.1 PRELIMINARIES), p. 8 (2.1 PRELIMINARIES) |
| Action / skill decoding | Figure 4: Comparisons with state-of-the-art methods on RoboTwin 2.0 benchmark. LIBERO. Each task is evaluated for 500 trials under random seeds. Tab. ... | p. 6 (Figure/Table caption), p. 5 (Figure/Table caption) |
| Receding execution / feedback | 6 shows that our SF achieves higher success rates across all tasks, showing considerable improvements in data efficiency. | p. 9 (2.1 PRELIMINARIES), p. 6 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: Depth probing of the visual embeddings of VLAs. Embeddings learned solely from 2D images without alignment do not produce meaningful spatial structures. The ...
- **p. 7 / 2.1 PRELIMINARIES - extractive body cue:** We further investigate the effect of supervising different transformer layers of VLA, shown in Tab.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Our proposed method, Spatial Forcing (SF), implicitly forces VLA models to acquire spatial-aware knowledge. (a) SF aligns intermediate visual embeddings of VLAs with ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1: Comparisons with state-of-the-art methods on LIBERO benchmark. Please note that methods in gray font incorporate extra depth or point cloud information from other ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: Comparisons with state-of-the-art methods on RoboTwin 2.0 benchmark. LIBERO. Each task is evaluated for 500 trials under random seeds. Tab. 1 shows that ...
- **p. 19 / Figure/Table caption - extractive body cue:** Table 4: The Ablation of Supervising Different Transformer Layers of VLA. Aligned Layerth Spatial Object Goal Long Average 1
- **p. 21 / Figure/Table caption - extractive body cue:** Figure 9: Additional ablation experiments for more complex spatial tasks. Then, the visual tokens of VLA are fed into the trainable VLA downstream heads to ...

## Reproduction Checklist

[공통 검토 기준](../../../research/READING_STATUS.md#note-checks)

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (2.1 PRELIMINARIES), p. 4 (2.1 PRELIMINARIES), p. 5 (2.1 PRELIMINARIES), p. 4 (2.1 PRELIMINARIES), p. 3 (2.1 PRELIMINARIES), p. 8 (2.1 PRELIMINARIES), objective p. 5 (2.1 PRELIMINARIES), p. 3 (2.1 PRELIMINARIES), p. 3 (2.1 PRELIMINARIES), p. 4 (2.1 PRELIMINARIES), p. 4 (2.1 PRELIMINARIES), p. 7 (2.1 PRELIMINARIES), temporal p. 3 (2.1 PRELIMINARIES), p. 3 (2.1 PRELIMINARIES), p. 5 (2.1 PRELIMINARIES), p. 6 (2.1 PRELIMINARIES), p. 6 (2.1 PRELIMINARIES), p. 8 (2.1 PRELIMINARIES).
