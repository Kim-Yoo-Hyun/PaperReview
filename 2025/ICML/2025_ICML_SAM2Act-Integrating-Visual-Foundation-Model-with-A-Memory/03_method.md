# Method - SAM2Act: Integrating Visual Foundation Model with A Memory Architecture for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v267/fang25c.html; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/168185. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Method in One Sentence

PDF body method statement (p. 6 (4. Method), p. 6 (4. Method), p. 4 (4. Method), p. 4 (4. Method), p. 5 (4. Method), p. 5 (4. Method)): SAM2Act: Integrating Visual Foundation Model with A Memory Architecture for Robotic Manipulation Algorithm 1 Forward Pass of SAM2Act+ Module Initialize: Number of steps N, number of views V , empty ...

## Method Body Digest

- **p. 6 / 4. Method - extractive body cue:** SAM2Act: Integrating Visual Foundation Model with A Memory Architecture for Robotic Manipulation Algorithm 1 Forward Pass of SAM2Act+ Module Initialize: Number of steps N, number ...
- **p. 6 / 4. Method - extractive body cue:** SAM2Act+: Action Memory Architecture for Improved Spatial Awareness in Past Observations To extend the SAM2Act architecture (Section 4.1) with memory-based capabilities inspired by SAM2, we ...
- **p. 4 / 4. Method - extractive body cue:** These include Memory Bank, Memory Encoder, and Memory Attention, enabling the model to encode historical actions and condition current observations.
- **p. 4 / 4. Method - extractive body cue:** The coarse and fine SAM2Act Modules share the same architecture, with the fine branch generating additional features to predict actions beyond translation, while the coarse ...
- **p. 5 / 4. Method - extractive body cue:** SAM2Act+ extends this architecture by incorporating memory-based components, including the Memory Encoder, Memory Attention, and Memory Bank, into the coarse branch.
- **p. 5 / 4. Method - extractive body cue:** At each stage, the output of the upsampler is combined with the corresponding multi-resolution embedding El from the SAM2 encoder, ensuring alignment between the multiresolution ...
- **p. 4 / 4. Method - extractive body cue:** To adapt the SAM2 image encoder to our domain, we finetune it using Low-Rank Adaptation (LoRA) (Hu et al., 2021) with a default rank of ...
- **p. 4 / 4. Method - extractive body cue:** SAM2Act leverages the pre-trained SAM2 encoder (Ravi et al., 2024) to extract multi-resolution image embeddings, which are further refined through the multi-resolution upsampling technique to ...

## Design Rationale

- **p. 3 / 4. Method - extractive body cue:** Our method, SAM2Act, enables precise 3D manipulation with strong generalization across environmental and objectlevel variations.
- **p. 2 / 1. Introduction - extractive body cue:** First, we introduce a novel model formulation that leverages visual foundation models to solve high-precision, memorydependent manipulation tasks.
- **p. 6 / 4. Method - extractive body cue:** SAM2Act+: Action Memory Architecture for Improved Spatial Awareness in Past Observations To extend the SAM2Act architecture (Section 4.1) with memory-based capabilities inspired by SAM2, we ...

## Source Evidence Cues

- **p. 6 / 4. Method - extractive body cue:** SAM2Act: Integrating Visual Foundation Model with A Memory Architecture for Robotic Manipulation Algorithm 1 Forward Pass of SAM2Act+ Module Initialize: Number of steps N, number ...
- **p. 6 / 4. Method - extractive body cue:** SAM2Act+: Action Memory Architecture for Improved Spatial Awareness in Past Observations To extend the SAM2Act architecture (Section 4.1) with memory-based capabilities inspired by SAM2, we ...
- **p. 4 / 4. Method - extractive body cue:** These include Memory Bank, Memory Encoder, and Memory Attention, enabling the model to encode historical actions and condition current observations.
- **p. 4 / 4. Method - extractive body cue:** The coarse and fine SAM2Act Modules share the same architecture, with the fine branch generating additional features to predict actions beyond translation, while the coarse ...
- **p. 5 / 4. Method - extractive body cue:** SAM2Act+ extends this architecture by incorporating memory-based components, including the Memory Encoder, Memory Attention, and Memory Bank, into the coarse branch.
- **p. 5 / 4. Method - extractive body cue:** At each stage, the output of the upsampler is combined with the corresponding multi-resolution embedding El from the SAM2 encoder, ensuring alignment between the multiresolution ...
- **Detected method headings:** 4. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | SAM2Act: Integrating Visual Foundation Model with A Memory Architecture for Robotic Manipulation Algorithm 1 Forward Pass of SAM2Act+ Module Initialize: Number of ... | p. 6 (4. Method), p. 6 (4. Method) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | SAM2Act+: Action Memory Architecture for Improved Spatial Awareness in Past Observations To extend the SAM2Act architecture (Section 4.1) with memory-based capabilities inspired ... | p. 6 (4. Method), p. 4 (4. Method) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | These include Memory Bank, Memory Encoder, and Memory Attention, enabling the model to encode historical actions and condition current observations. | p. 4 (4. Method), p. 4 (4. Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 4. Method - extractive body cue:** To adapt the SAM2 image encoder to our domain, we finetune it using Low-Rank Adaptation (LoRA) (Hu et al., 2021) with a default rank of ...
- **p. 4 / 4. Method - extractive body cue:** SAM2Act leverages the pre-trained SAM2 encoder (Ravi et al., 2024) to extract multi-resolution image embeddings, which are further refined through the multi-resolution upsampling technique to ...
- **원문 대조:** 각 단계의 feature update는 X^{l+1}=LayerNorm(U(X^l) ⊕ E^l)이다. U는 spatial upsampling, ⊕는 element-wise addition이며 SAM2의 multi-resolution embedding을 결합한다. 이번 공개본의 해당 위치는 PDF p. 6이다. ([PDF p. 6](https://arxiv.org/pdf/2501.18564#page=6), §4.1 SAM2Act, Figure 4).
- **p. 5 / 4. Method - extractive body cue:** The multi-resolution upsampling mechanism, also detailed in Figure 4, leverages cascaded convex upsamplers to progressively refine feature maps across resolutions.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 4 (4. Method), p. 5 (4. Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | embeddings, generated, three, resolution, levels, combined, virtual, images, containing, RGB, depth, translation, coordinates, language | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | embeddings, generated, three, resolution, levels, combined, virtual, images, containing, RGB | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | SAM2Act, enables, precise, manipulation, strong, generalization, across, environmental, objectlevel, variations | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | adapt, SAM2, image, encoder, domain, finetune, Low-Rank, Adaptation, LoRA, default | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 4. Method - extractive body cue:** These embeddings, generated at three resolution levels, are combined with virtual images containing RGB, depth, 3D translation coordinates, and language instructions before being fed into ...
- **p. 4 / 4. Method - extractive body cue:** These include Memory Bank, Memory Encoder, and Memory Attention, enabling the model to encode historical actions and condition current observations.
- **p. 5 / 4. Method - extractive body cue:** These components enable memory-driven reasoning by processing historical heatmaps and integrating prior observations, allowing the agent to predict actions based on stored contextual information.
- **p. 6 / 4. Method - extractive body cue:** During fine-tuning, consecutive action keyframes are sampled as input, training the multiresolution upsampler to predict new translations conditioned on memory.
- **p. 6 / 4. Method - extractive body cue:** Originally developed for object tracking in SAM2, these components are adapted to align with the needs of SAM2Act+, enabling the agent to retain prior actions ...
- **p. 5 / 4. Method - extractive body cue:** Observations are reconstructed into point clouds, rendered into three virtual images, and lifted into 3D translation points, enabling precise spatial reasoning across both architectures.
- **p. 2 / 1. Introduction - extractive body cue:** SAM2Act is a multi-view, language-conditioned behavior cloning policy trained with fewer demonstrations.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | During fine-tuning, consecutive action keyframes are sampled as input, training the multiresolution upsampler to predict new translations conditioned on memory. | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | In SAM2, the Memory Encoder processes predicted object masks, while the Memory Attention module fuses image embeddings with positional information from previous ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | During fine-tuning, consecutive action keyframes are sampled as input, training the multiresolution upsampler to predict new translations conditioned on memory. | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 4. Method - extractive body cue:** The SAM2Act architecture leverages the SAM2 image encoder to generate prompt-conditioned, multi-resolution embeddings, fine-tuned with LoRA for efficient adaptation to manipulation tasks.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** SAM2Act, Integrating, Visual, Foundation, Model, Memory, Architecture, Robotic, Manipulation, Algorithm, Forward, Pass, Module, Initialize, Number, steps, views, empty, bank, separate.
- **Relevant PDF headings:** 4. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | We benchmark SAM2Act in both simulated and real-world environments. | p. 6 (5.1. Experimental Setup), p. 6 (5. Experiments) |
| Action / skill decoding | Our method, SAM2Act, outperforms all baselines, achieving a significant performance margin of 5.8% over RVT-2 (Goyal et al., 2024), the prior state-of-the-art ... | p. 7 (5.1. Experimental Setup), p. 6 (5. Experiments) |
| Receding execution / feedback | Table 3. Performance on MemoryBench. We report the success rates for the three spatial memory tasks in MemoryBench. Our method, SAM2Act+, significantly ... | p. 8 (Figure/Table caption), p. 7 (5.2. Performances Across 18 RLBench Tasks) |

## Failure and Ablation Link

- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3. After pretraining SAM2Act in Stage 1, we freeze the SAM2 image encoder and the multi-view transformer in the coarse branch, as these components ...
- **p. 7 / 5.2. Performances Across 18 RLBench Tasks - extractive body cue:** Ablation studies are performed on SAM2Act in Appendix E.
- **p. 8 / 5.4. Performance on MemoryBench - extractive body cue:** It outperforms SAM2Act (without memory) by a huge margin of 39.3% on MemoryBench, highlighting the significant impact of explicit memory modeling.
- **p. 8 / 5.3. Semantic Generalization across Tasks - extractive body cue:** Task-average success rate percentage change for SAM2Act and other baselines across 13 perturbation factors from The Colosseum, relative to evaluations without perturbations.
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Overview of the SAM2Act (top) and SAM2Act+ (bottom) architectures. The SAM2Act architecture leverages the SAM2 image encoder to generate prompt-conditioned, multi-resolution embeddings, fine-tuned ...
- **p. 8 / 5.4. Performance on MemoryBench - extractive body cue:** In Table 3, we evaluate SAM2Act+ against SoTA 3D BC model, RVT-2 on MemoryBench, training all models in a single-task setting to isolate memory-related challenges ...
- **p. 6 / 5. Experiments - extractive body cue:** Specifically, we are interested in answering the following questions: § 5.2 How does SAM2Act compare with state-of-the-art 3D manipulation policies? § 5.3 Can SAM2Act generalize ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 6 (4. Method), p. 6 (4. Method), p. 4 (4. Method), p. 4 (4. Method), p. 5 (4. Method), p. 5 (4. Method), objective p. 4 (4. Method), p. 4 (4. Method), p. 5 (4. Method), p. 5 (4. Method), temporal p. 6 (4. Method), p. 6 (4. Method), p. 3 (4. Method), p. 4 (4. Method), p. 4 (4. Method), p. 5 (4. Method).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
