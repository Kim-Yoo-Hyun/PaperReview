# Method - OmniEVA: Embodied Versatile Planner via Task-Adaptive 3D-Grounded and Embodiment-aware Reasoning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (52 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=tkEmIJv1tB; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/247599. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (3 METHODOLOGY), p. 4 (3 METHODOLOGY), p. 17 (A.1 MODEL ARCHITECTURE AND TRAINING CONFIGURATIONS), p. 3 (3 METHODOLOGY), p. 17 (A.1 MODEL ARCHITECTURE AND TRAINING CONFIGURATIONS), p. 4 (3 METHODOLOGY)): 3.1 OVERVIEW OmniEVA builds on pretrained MLLMs which typically comprises three principal components: 1) A vision transformer encoder Eimg that converts each RGB image into a sequence of discrete visual ...

## Method Body Digest

- **p. 3 / 3 METHODOLOGY - extractive body cue:** 3.1 OVERVIEW OmniEVA builds on pretrained MLLMs which typically comprises three principal components: 1) A vision transformer encoder Eimg that converts each RGB image into ...
- **p. 4 / 3 METHODOLOGY - extractive body cue:** Examples of the Activation of Gated Router Task‐Adaptive Gated Router Sentence Transformer 384 concatenate MLP Network Gumbel Softmax Task Condition Scene Condition Plus 𝒈ൌ𝟎 𝒈ൌ𝟏 ...
- **p. 17 / A.1 MODEL ARCHITECTURE AND TRAINING CONFIGURATIONS - extractive body cue:** Detailed hyper-parameters as given in Table 7 TAGR Pretraining During TAGR pretraining, we freeze the sentence transformer and train the MLP encoder with a learning ...
- **p. 3 / 3 METHODOLOGY - extractive body cue:** For N frames, the encoder outputs V I ∈RN×Hp×Wp×dv, where dv denodes the embedding dimension.
- **p. 17 / A.1 MODEL ARCHITECTURE AND TRAINING CONFIGURATIONS - extractive body cue:** Each training group generates 8 candidate outputs.
- **p. 4 / 3 METHODOLOGY - extractive body cue:** For task conditioning, a lightweight sentence transformer (Reimers & Gurevych, 2019) encodes the instruction T into a latent vector V T ∈Rdst.
- **p. 18 / A.2.1 VISUAL INPUT MODALITIES - extractive body cue:** These parameters allow the model to transform depth maps into structured 3D representations, forming the foundation for geometry-aware decision-making.
- **p. 18 / A.3 IMPLEMENTATION DETAIL OF EMBODIMENT-AWARE REASONING - extractive body cue:** Given a reward for the i-th response: ri,t(q, oi) = rformat i (oi) + racc i,t (q, oi) (11) 18

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address these limitations, we introduce OmniEVA (Embodied Versatile Planner), a novel architecture that pioneers Task-Adaptive 3D Grounding and Embodiment-aware Reasoning.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** OmniEVA is the first framework to dynamically integrate 2D and 3D inputs via taskconditioned feature selection, enabling versatile and executable embodied reasoning through two key ...
- **p. 3 / 3 METHODOLOGY - extractive body cue:** Dynamic 3D Injection via Gated Routing Rather than applying 3D positional encoding uniformly for all tasks, we propose a Task-Adaptive Gated Router (TAGR) that selectively ...

## Source Evidence Cues

- **p. 3 / 3 METHODOLOGY - extractive body cue:** 3.1 OVERVIEW OmniEVA builds on pretrained MLLMs which typically comprises three principal components: 1) A vision transformer encoder Eimg that converts each RGB image into ...
- **p. 4 / 3 METHODOLOGY - extractive body cue:** Examples of the Activation of Gated Router Task‐Adaptive Gated Router Sentence Transformer 384 concatenate MLP Network Gumbel Softmax Task Condition Scene Condition Plus 𝒈ൌ𝟎 𝒈ൌ𝟏 ...
- **p. 17 / A.1 MODEL ARCHITECTURE AND TRAINING CONFIGURATIONS - extractive body cue:** Detailed hyper-parameters as given in Table 7 TAGR Pretraining During TAGR pretraining, we freeze the sentence transformer and train the MLP encoder with a learning ...
- **p. 3 / 3 METHODOLOGY - extractive body cue:** For N frames, the encoder outputs V I ∈RN×Hp×Wp×dv, where dv denodes the embedding dimension.
- **p. 17 / A.1 MODEL ARCHITECTURE AND TRAINING CONFIGURATIONS - extractive body cue:** Each training group generates 8 candidate outputs.
- **p. 4 / 3 METHODOLOGY - extractive body cue:** For task conditioning, a lightweight sentence transformer (Reimers & Gurevych, 2019) encodes the instruction T into a latent vector V T ∈Rdst.
- **p. 18 / A.2.1 VISUAL INPUT MODALITIES - extractive body cue:** These parameters allow the model to transform depth maps into structured 3D representations, forming the foundation for geometry-aware decision-making.
- **Detected method headings:** 3 METHODOLOGY (p. 3); A.1 MODEL ARCHITECTURE AND TRAINING CONFIGURATIONS (p. 17)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | 3.1 OVERVIEW OmniEVA builds on pretrained MLLMs which typically comprises three principal components: 1) A vision transformer encoder Eimg that converts each ... | p. 3 (3 METHODOLOGY), p. 4 (3 METHODOLOGY) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Examples of the Activation of Gated Router Task‐Adaptive Gated Router Sentence Transformer 384 concatenate MLP Network Gumbel Softmax Task Condition Scene Condition ... | p. 4 (3 METHODOLOGY), p. 17 (A.1 MODEL ARCHITECTURE AND TRAINING CONFIGURATIONS) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Detailed hyper-parameters as given in Table 7 TAGR Pretraining During TAGR pretraining, we freeze the sentence transformer and train the MLP encoder ... | p. 17 (A.1 MODEL ARCHITECTURE AND TRAINING CONFIGURATIONS), p. 3 (3 METHODOLOGY) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 18 / A.3 IMPLEMENTATION DETAIL OF EMBODIMENT-AWARE REASONING - extractive body cue:** Given a reward for the i-th response: ri,t(q, oi) = rformat i (oi) + racc i,t (q, oi) (11) 18
- **p. 17 / A.1 MODEL ARCHITECTURE AND TRAINING CONFIGURATIONS - extractive body cue:** The ViT encoder is frozen, while the LLM backbone is updated with a reduced learning rate of 5e -7 to prioritize learning within the TAGR ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 17 (A.1 MODEL ARCHITECTURE AND TRAINING CONFIGURATIONS).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | OVERVIEW, OmniEVA, builds, pretrained, MLLMs, typically, comprises, three, principal, components, vision, transformer, encoder, Eimg | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | OVERVIEW, OmniEVA, builds, pretrained, MLLMs, typically, comprises, three, principal, components | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | address, limitations, introduce, OmniEVA, Embodied, Versatile, Planner, novel, architecture, pioneers | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Given, reward, i-th, response, rformat, racc, ViT, encoder, frozen, while | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3 METHODOLOGY - extractive body cue:** 3.1 OVERVIEW OmniEVA builds on pretrained MLLMs which typically comprises three principal components: 1) A vision transformer encoder Eimg that converts each RGB image into ...
- **p. 3 / 3 METHODOLOGY - extractive body cue:** The model accepts a natural language instruction T, a sequence of RGB images or video frames (I1, I2, . . . , IN), and optionally, ...
- **p. 17 / A.2 INPUT MODALITIES AND OUTPUT REPRESENTATIONS - extractive body cue:** OmniEVA is designed to accommodate a wide range of input modalities and output formats, enabling versatile interaction across visual and textual domains.
- **p. 18 / A.2.2 TEXTUAL AND COORDINATE-BASED OUTPUTS - extractive body cue:** OmniEVA accommodates a range of textual and spatial formats for both input queries and output responses, enabling flexible interaction across semantic and geometric dimensions.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Spatial reasoning serves as a core bridge between perception and action, transforming sensory inputs into structured representations that support long-horizon planning and rational decision-making.
- **p. 4 / 3 METHODOLOGY - extractive body cue:** Right: Illustrative examples of the gated router's activation state across different tasks. task to be performed, and 2) the scene condition, reflecting the structural complexity ...
- **p. 18 / A.2.2 TEXTUAL AND COORDINATE-BASED OUTPUTS - extractive body cue:** 2D Spatial Annotations For tasks such as 2D visual grounding and image captioning, inputs and outputs can be expressed using normalized pixel coordinates within the ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Conventional MLLMs such as QwenVL and InternVL split each frame into Hp × Wp patches, augment them with 2D positional encodings, and ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | The model accepts a natural language instruction T, a sequence of RGB images or video frames (I1, I2, . . . , ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | For video-based inputs, we uniformly sample 16 frames during training and 32 frames during inference, striking a balance between temporal granularity and ... | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 3 METHODOLOGY - extractive body cue:** 3.1 OVERVIEW OmniEVA builds on pretrained MLLMs which typically comprises three principal components: 1) A vision transformer encoder Eimg that converts each RGB image into ...
- **p. 17 / A.1 MODEL ARCHITECTURE AND TRAINING CONFIGURATIONS - extractive body cue:** Detailed hyper-parameters as given in Table 7 TAGR Pretraining During TAGR pretraining, we freeze the sentence transformer and train the MLP encoder with a learning ...
- **p. 17 / A.1 MODEL ARCHITECTURE AND TRAINING CONFIGURATIONS - extractive body cue:** Each training group generates 8 candidate outputs.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** OVERVIEW, OmniEVA, builds, pretrained, MLLMs, typically, comprises, three, principal, components, vision, transformer, encoder, Eimg, converts, RGB, image, sequence, discrete, visual.
- **Relevant PDF headings:** 3 METHODOLOGY (p. 3); A.1 MODEL ARCHITECTURE AND TRAINING CONFIGURATIONS (p. 17).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | For example: RT-1 (Brohan et al., 2022) dataset comprises over 130,000 real-world robotic demonstrations (episodes), covering more than 700 different tasks. | p. 27 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING), p. 30 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING) |
| Semantic / temporal fusion | Figure 9: Case study illustrating OmniEVA's reasoning process under embodiment-aware constraints. C ABLATION STUDY IMPLEMENTATION DETAILS C.1 IMPLEMENTATION OF CROSS-ATTENTION BASED 3D ... | p. 23 (Figure/Table caption), p. 24 (C.1 IMPLEMENTATION OF CROSS-ATTENTION BASED 3D FUSION) |
| Robot query / planning handoff | Figure 5: Ablation Results of the proposed TE-GRPO Method on Local Mobile-Manipulation Tasks As shown in Figure 5, OmniEVA-ER-jointly optimized with rtask ... | p. 9 (Figure/Table caption), p. 10 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 23 / Figure/Table caption - extractive body cue:** Figure 9: Case study illustrating OmniEVA's reasoning process under embodiment-aware constraints. C ABLATION STUDY IMPLEMENTATION DETAILS C.1 IMPLEMENTATION OF CROSS-ATTENTION BASED 3D FUSION To rigorously ...
- **p. 22 / Figure/Table caption - extractive body cue:** Figure 6: Case Study of Gate Activation State. Selected examples from the validation dataset illustrate the most prominently activated and deactivated words within the input ...
- **p. 23 / C.1 IMPLEMENTATION OF CROSS-ATTENTION BASED 3D FUSION - extractive body cue:** The architectural details are illustrated in Figure 10. • Separate Tokens Arrangement: In this variant, the sequences of visual tokens (V I) and 3D positional ...
- **p. 24 / C.1 IMPLEMENTATION OF CROSS-ATTENTION BASED 3D FUSION - extractive body cue:** As discussed in Section 4.2, both cross-attention variants led to significant performance drops compared to our gated fusion.
- **p. 24 / C.1 IMPLEMENTATION OF CROSS-ATTENTION BASED 3D FUSION - extractive body cue:** A standard cross-attention layer is then employed to enable interaction between these two modalities. • Interleaved Tokens Arrangement: In this variant, tokens are grouped and ...
- **p. 28 / C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING - extractive body cue:** It poses a significant challenge for MLLMs, which often struggle to generate accurate 3D bounding boxes without priors from off-the28
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 5: Ablation Results of the proposed TE-GRPO Method on Local Mobile-Manipulation Tasks As shown in Figure 5, OmniEVA-ER-jointly optimized with rtask and rembod -demonstrates ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (3 METHODOLOGY), p. 4 (3 METHODOLOGY), p. 17 (A.1 MODEL ARCHITECTURE AND TRAINING CONFIGURATIONS), p. 3 (3 METHODOLOGY), p. 17 (A.1 MODEL ARCHITECTURE AND TRAINING CONFIGURATIONS), p. 4 (3 METHODOLOGY), objective p. 18 (A.3 IMPLEMENTATION DETAIL OF EMBODIMENT-AWARE REASONING), p. 17 (A.1 MODEL ARCHITECTURE AND TRAINING CONFIGURATIONS), temporal p. 3 (3 METHODOLOGY), p. 3 (3 METHODOLOGY), p. 17 (A.1 MODEL ARCHITECTURE AND TRAINING CONFIGURATIONS), p. 18 (A.2.1 VISUAL INPUT MODALITIES), p. 18 (A.2.1 VISUAL INPUT MODALITIES), p. 17 (A.1 MODEL ARCHITECTURE AND TRAINING CONFIGURATIONS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
