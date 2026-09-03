# Method - SpatioLM: Towards General Physical Spatial Intelligence in Vision-Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=CHavqrN1X9; PDF retrieval source: https://openreview.net/pdf/04fc204cb3233c6ac9f5867e72c861a9e835bc65.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (3.3. Loss Design), p. 5 (3.3. Loss Design), p. 3 (3. Method), p. 3 (3.1. Problem definition and notation), p. 4 (3.2. Spatio-Vision Module), p. 4 (3.2. Spatio-Vision Module)): The overall training objective is a weighted sum of a language modeling loss and mixed geometric losses.

## Method Body Digest

- **p. 5 / 3.3. Loss Design - extractive body cue:** The overall training objective is a weighted sum of a language modeling loss and mixed geometric losses.
- **p. 5 / 3.3. Loss Design - extractive body cue:** To align the SV-Block features with robust 3D representations, we apply Vision Token Supervision (VTS) by distilling them toward the latent features of a pretrained ...
- **p. 3 / 3. Method - extractive body cue:** 3, SpatioLM freezes a pretrained VLM backbone and introduces a parameter-efficient runtime plugand-play Spatio-Vision Module (SV-Module, which consists of stacked Spatio-Vision Blocks) to elicit the ...
- **p. 3 / 3.1. Problem definition and notation - extractive body cue:** During training, SpatioLM additionally predicts dense geometric outputs Y g = ( ¯D, ¯R), (2) where ¯D and ¯R serve as the pseudo-labels for the ...
- **p. 4 / 3.2. Spatio-Vision Module - extractive body cue:** To elicit spatial representations, in the i-th Spatio-Vision Block, we process the hidden features input to the j-th LM block, thereby extracting geometry-aware tokens Hg ...
- **p. 4 / 3.2. Spatio-Vision Module - extractive body cue:** The Spatio-Vision Module elicits geometry-aware features from visual tokens and injects them into language blocks via zero-initialized projections, enabling visual spatial reasoning while preserving VLM's ...
- **p. 6 / 3.3. Loss Design - extractive body cue:** During training, only SV-Module and projection layers are updated, with the VLM backbone frozen.
- **p. 3 / 3.2. Spatio-Vision Module - extractive body cue:** To leverage the strong semantic capacity of VLMs while minimizing computational overhead, we adopt a parameterefficient, ControlNet-inspired side-tuning strategy.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are summarized as follows: • We propose SpatioLM, a purely 2D vision-language framework that elicits implicit 3D geometric structure from pretrained VLM ...
- **p. 3 / 3. Method - extractive body cue:** We propose SpatioLM, a unified framework that enhances VLMs with general physical spatial intelligence.
- **p. 3 / 3. Method - extractive body cue:** 3, SpatioLM freezes a pretrained VLM backbone and introduces a parameter-efficient runtime plugand-play Spatio-Vision Module (SV-Module, which consists of stacked Spatio-Vision Blocks) to elicit the ...

## Source Evidence Cues

- **p. 5 / 3.3. Loss Design - extractive body cue:** The overall training objective is a weighted sum of a language modeling loss and mixed geometric losses.
- **p. 5 / 3.3. Loss Design - extractive body cue:** To align the SV-Block features with robust 3D representations, we apply Vision Token Supervision (VTS) by distilling them toward the latent features of a pretrained ...
- **p. 3 / 3. Method - extractive body cue:** 3, SpatioLM freezes a pretrained VLM backbone and introduces a parameter-efficient runtime plugand-play Spatio-Vision Module (SV-Module, which consists of stacked Spatio-Vision Blocks) to elicit the ...
- **p. 3 / 3.1. Problem definition and notation - extractive body cue:** During training, SpatioLM additionally predicts dense geometric outputs Y g = ( ¯D, ¯R), (2) where ¯D and ¯R serve as the pseudo-labels for the ...
- **p. 4 / 3.2. Spatio-Vision Module - extractive body cue:** To elicit spatial representations, in the i-th Spatio-Vision Block, we process the hidden features input to the j-th LM block, thereby extracting geometry-aware tokens Hg ...
- **p. 4 / 3.2. Spatio-Vision Module - extractive body cue:** The Spatio-Vision Module elicits geometry-aware features from visual tokens and injects them into language blocks via zero-initialized projections, enabling visual spatial reasoning while preserving VLM's ...
- **p. 6 / 3.3. Loss Design - extractive body cue:** During training, only SV-Module and projection layers are updated, with the VLM backbone frozen.
- **Detected method headings:** 3. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | The overall training objective is a weighted sum of a language modeling loss and mixed geometric losses. | p. 5 (3.3. Loss Design), p. 5 (3.3. Loss Design) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | To align the SV-Block features with robust 3D representations, we apply Vision Token Supervision (VTS) by distilling them toward the latent features ... | p. 5 (3.3. Loss Design), p. 3 (3. Method) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | 3, SpatioLM freezes a pretrained VLM backbone and introduces a parameter-efficient runtime plugand-play Spatio-Vision Module (SV-Module, which consists of stacked Spatio-Vision Blocks) ... | p. 3 (3. Method), p. 3 (3.1. Problem definition and notation) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.3. Loss Design - extractive body cue:** The overall training objective is a weighted sum of a language modeling loss and mixed geometric losses.
- **p. 3 / 3.2. Spatio-Vision Module - extractive body cue:** To leverage the strong semantic capacity of VLMs while minimizing computational overhead, we adopt a parameterefficient, ControlNet-inspired side-tuning strategy.
- **p. 5 / 3.3. Loss Design - extractive body cue:** The final training loss is L = αLL + βLd + γLg, (10) 5
- **p. 6 / 3.4. Unified Task Formulation - extractive body cue:** Spatial perception tasks in SpatioLM are depth-centric, with metric depth estimation as the core objective.
- **p. 6 / 3.4. Unified Task Formulation - extractive body cue:** SpatioLM frames diverse spatial tasks as conditional language modeling, using prompt design to specify tasks and next-token prediction in the vocabulary space.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (3.3. Loss Design), p. 5 (3.3. Loss Design), p. 6 (3.4. Unified Task Formulation), p. 6 (3.3. Loss Design).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | input, sequence, model, defined, following, tuple, format, where, denotes, visual, images, videos, corresponding, textual | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | input, sequence, model, defined, following, tuple, format, where, denotes, visual | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | main, contributions, summarized, follows, SpatioLM, purely, vision-language, framework, elicits, implicit | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | overall, training, objective, weighted, language, modeling, loss, mixed, geometric, losses | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3.1. Problem definition and notation - extractive body cue:** The input sequence of the model is defined as the following tuple format: X =  Xv, Xt , (1) where Xv ∈RT ×H×W ×3 denotes ...
- **p. 4 / 3.2. Spatio-Vision Module - extractive body cue:** Subsequently, we fuse the extracted Hg i with the output of the vision-language tokens by the j-th LM block, which then serves as input to ...
- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are summarized as follows: • We propose SpatioLM, a purely 2D vision-language framework that elicits implicit 3D geometric structure from pretrained VLM ...
- **p. 3 / 3.1. Problem definition and notation - extractive body cue:** During training, SpatioLM additionally predicts dense geometric outputs Y g = ( ¯D, ¯R), (2) where ¯D and ¯R serve as the pseudo-labels for the ...
- **p. 5 / 3.2. Spatio-Vision Module - extractive body cue:** To enforce explicit geometric learning, the output features Hg are fed into a dual-branch Dense Prediction Transformer (DPT) head adopted from Depth Anything V3 (Lin ...
- **p. 4 / 3.2. Spatio-Vision Module - extractive body cue:** Training incorporates auxiliary pseudo depth and camera supervision, while inference requires no additional 3D priors and is conducted through a unified text generation interface. et ...
- **p. 6 / 3.4. Unified Task Formulation - extractive body cue:** Visual markers are overlaid on the input image, and the prompt asks for the distance at the marked location.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | We propose SpatioLM, a unified framework that enhances VLMs with general physical spatial intelligence. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | The model generates a textual response Y t = (y1, . . . , yL), where L is the generated sequence length. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | Training is conducted for 600 epochs on spatial perception tasks and 2 epochs on spatial understanding tasks. | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.3. Loss Design - extractive body cue:** The overall training objective is a weighted sum of a language modeling loss and mixed geometric losses.
- **p. 5 / 3.3. Loss Design - extractive body cue:** To align the SV-Block features with robust 3D representations, we apply Vision Token Supervision (VTS) by distilling them toward the latent features of a pretrained ...
- **p. 3 / 3. Method - extractive body cue:** 3, SpatioLM freezes a pretrained VLM backbone and introduces a parameter-efficient runtime plugand-play Spatio-Vision Module (SV-Module, which consists of stacked Spatio-Vision Blocks) to elicit the ...
- **p. 3 / 3.1. Problem definition and notation - extractive body cue:** During training, SpatioLM additionally predicts dense geometric outputs Y g = ( ¯D, ¯R), (2) where ¯D and ¯R serve as the pseudo-labels for the ...
- **p. 6 / 3.3. Loss Design - extractive body cue:** During training, only SV-Module and projection layers are updated, with the VLM backbone frozen.
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** All models are trained on 64 NVIDIA H200 GPUs using AdamW (β1 = 0.9, β2 = 0.95, weight decay = 0.1), with a cosine learning ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** overall, training, objective, weighted, language, modeling, loss, mixed, geometric, losses, align, SV-Block, features, robust, representations, apply, Vision, Token, Supervision, VTS.
- **Relevant PDF headings:** 3. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | To ensure rigorous evaluation and prevent data leakage, all training samples are strictly sourced from the official training splits of the respective ... | p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup) |
| Semantic / temporal fusion | It significantly outperforms strong baselines on both single-image and multi-image metric depth, attains the highest accuracy on DA-2K, and demonstrates more stable ... | p. 7 (4.2.1. SPATIAL PERCEPTION), p. 7 (4.2.1. SPATIAL PERCEPTION) |
| Robot query / planning handoff | Figure 1. We propose SpatioLM, a parameter-efficient framework that improves spatial intelligence in VLMs without extra 3D prior inputs or external spatial ... | p. 1 (Figure/Table caption), p. 7 (4.2.1. SPATIAL PERCEPTION) |

## Failure and Ablation Link

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. We propose SpatioLM, a parameter-efficient framework that improves spatial intelligence in VLMs without extra 3D prior inputs or external spatial encoders. SpatioLM achieves ...
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** During evaluation, the Dual DPT Head can be removed.
- **p. 7 / 4.2.2. SPATIAL UNDERSTANDING - extractive body cue:** ScanQA is evaluated with BLEU-1 (B1), BLEU-4 (B4), METEOR (M), ROUGE-L (R), and CIDEr (C), while SQA3D uses exact match accuracy (E1) and its refined ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. (a) Methods that explicitly leverage 3D priors, such as depth maps, point clouds, or camera parameters. (b) Methods that introduce an additional spatial ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 5. Ablation study on the SV-Module, VTS, and DGS. SV-Module VTS DGS MD-S DA-2K VSI-Bench ✗ ✗ ✗ 52.6 71.8 68.7
- **p. 9 / Figure/Table caption - extractive body cue:** Table 6. Sensitivity analysis on loss weights. α β γ VSI-Bench ScanQA(C) SQA3D(ER1) 0.4
- **p. 9 / Figure/Table caption - extractive body cue:** Table 7. Ablation on attention mechanism. Mechanism VSI-Bench ScanQA(C) SQA3D(ER1) Self-Attention 70.4 98.7 56.8 Alt.-Attention (Ours)

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (3.3. Loss Design), p. 5 (3.3. Loss Design), p. 3 (3. Method), p. 3 (3.1. Problem definition and notation), p. 4 (3.2. Spatio-Vision Module), p. 4 (3.2. Spatio-Vision Module), objective p. 5 (3.3. Loss Design), p. 3 (3.2. Spatio-Vision Module), p. 5 (3.3. Loss Design), p. 6 (3.4. Unified Task Formulation), p. 6 (3.4. Unified Task Formulation), temporal p. 3 (3. Method), p. 3 (3.1. Problem definition and notation), p. 4 (3.2. Spatio-Vision Module), p. 4 (3.2. Spatio-Vision Module), p. 6 (3.4. Unified Task Formulation), p. 1 (0.00 0.20 0.92 0.00 0.07 -0.02 1.00 …).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
