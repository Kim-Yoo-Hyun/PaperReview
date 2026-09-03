# Method - ConsisVLA-4D: Advancing Spatiotemporal Consistency in Efficient 3D-Perception and 4D-Reasoning for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Li_ConsisVLA-4D_Advancing_Spatiotemporal_Consistency_in_Efficient_3D-Perception_and_4D-Reasoning_for_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_ConsisVLA-4D_Advancing_Spatiotemporal_Consistency_in_Efficient_3D-Perception_and_4D-Reasoning_for_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (3) Cross-Scene), p. 4 (4.1. Proposed Framework), p. 5 (4.4. Cross-Scene Spatiotemporal Consistency), p. 1 (Abstract), p. 5 (4.4. Cross-Scene Spatiotemporal Consistency), p. 3 (3. Preliminary & Problem Definition)): Our contributions are summarized as follows: • We propose ConsisVLA-4D, an efficient and innovative framework that advances spatiotemporal consistency in 3D-Perception and 4D-Reasoning. • We introduce CV-Aligner and CO-Fuser to ...

## Method Body Digest

- **p. 2 / 3) Cross-Scene - extractive body cue:** Our contributions are summarized as follows: • We propose ConsisVLA-4D, an efficient and innovative framework that advances spatiotemporal consistency in 3D-Perception and 4D-Reasoning. • We ...
- **p. 4 / 4.1. Proposed Framework - extractive body cue:** (5) On the other hand, we use the aggregated geometric relation zagg-3D L′ to infer the depth representations of future multiview perspectives as actions unfold: ...
- **p. 5 / 4.4. Cross-Scene Spatiotemporal Consistency - extractive body cue:** In the SC-Attn module, each dynamic token 0dyn-4D i is independently guided by its corresponding object representation zobj-3D i and the instruction embedding t: \ ...
- **p. 1 / Abstract - extractive body cue:** Current Vision-Language-Action (VLA) models primarily focus on mapping 2D observations to actions but exhibit notable limitations in spatiotemporal perception and reasoning: 1) spatial representations often ...
- **p. 5 / 4.4. Cross-Scene Spatiotemporal Consistency - extractive body cue:** Cross-Scene Thinker with Spatiotemporal Consistency Attention (SC-Attn) ensures: 1) Three sets of initialized dynamic tokens decode dynamic object representations for one view (CoTracker [26, 27] ...
- **p. 3 / 3. Preliminary & Problem Definition - extractive body cue:** 3) VGGT [64] takes M RGB images (xi)M i=1 from the same 3D scene and outputs depth maps Di, point maps Pi, and feature grids ...
- **p. 1 / Abstract - extractive body cue:** Building upon these, we introduce 3) CS-Thinker to achieve Cross-Scene spatiotemporal consistency as actions unfold.
- **p. 6 / 4.4. Cross-Scene Spatiotemporal Consistency - extractive body cue:** During this process, the initialized action tokens 0A are decoded in parallel to yield ˆA, optimized using the L1 loss Laction.

## Design Rationale

- **p. 2 / 3) Cross-Scene - extractive body cue:** Our contributions are summarized as follows: • We propose ConsisVLA-4D, an efficient and innovative framework that advances spatiotemporal consistency in 3D-Perception and 4D-Reasoning. • We ...
- **p. 2 / 1. Introduction - extractive body cue:** To this end, we propose ConsisVLA-4D, a unified and efficient framework that enhances spatiotemporal consistency in 3D-perception and 4D-reasoning, as shown in Fig.
- **p. 1 / Abstract - extractive body cue:** Building upon these, we introduce 3) CS-Thinker to achieve Cross-Scene spatiotemporal consistency as actions unfold.

## Source Evidence Cues

- **p. 2 / 3) Cross-Scene - extractive body cue:** Our contributions are summarized as follows: • We propose ConsisVLA-4D, an efficient and innovative framework that advances spatiotemporal consistency in 3D-Perception and 4D-Reasoning. • We ...
- **p. 4 / 4.1. Proposed Framework - extractive body cue:** (5) On the other hand, we use the aggregated geometric relation zagg-3D L′ to infer the depth representations of future multiview perspectives as actions unfold: ...
- **p. 5 / 4.4. Cross-Scene Spatiotemporal Consistency - extractive body cue:** In the SC-Attn module, each dynamic token 0dyn-4D i is independently guided by its corresponding object representation zobj-3D i and the instruction embedding t: \ ...
- **p. 1 / Abstract - extractive body cue:** Current Vision-Language-Action (VLA) models primarily focus on mapping 2D observations to actions but exhibit notable limitations in spatiotemporal perception and reasoning: 1) spatial representations often ...
- **p. 5 / 4.4. Cross-Scene Spatiotemporal Consistency - extractive body cue:** Cross-Scene Thinker with Spatiotemporal Consistency Attention (SC-Attn) ensures: 1) Three sets of initialized dynamic tokens decode dynamic object representations for one view (CoTracker [26, 27] ...
- **p. 3 / 3. Preliminary & Problem Definition - extractive body cue:** 3) VGGT [64] takes M RGB images (xi)M i=1 from the same 3D scene and outputs depth maps Di, point maps Pi, and feature grids ...
- **p. 1 / Abstract - extractive body cue:** Building upon these, we introduce 3) CS-Thinker to achieve Cross-Scene spatiotemporal consistency as actions unfold.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Our contributions are summarized as follows: • We propose ConsisVLA-4D, an efficient and innovative framework that advances spatiotemporal consistency in 3D-Perception and ... | p. 2 (3) Cross-Scene), p. 4 (4.1. Proposed Framework) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | (5) On the other hand, we use the aggregated geometric relation zagg-3D L′ to infer the depth representations of future multiview perspectives ... | p. 4 (4.1. Proposed Framework), p. 5 (4.4. Cross-Scene Spatiotemporal Consistency) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | In the SC-Attn module, each dynamic token 0dyn-4D i is independently guided by its corresponding object representation zobj-3D i and the instruction ... | p. 5 (4.4. Cross-Scene Spatiotemporal Consistency), p. 1 (Abstract) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 4.4. Cross-Scene Spatiotemporal Consistency - extractive body cue:** During this process, the initialized action tokens 0A are decoded in parallel to yield ˆA, optimized using the L1 loss Laction.
- **p. 2 / 1. Introduction - extractive body cue:** 2) How can we enhance spatiotemporal consistency to optimize action prediction through 4D visual reasoning?
- **p. 3 / 3. Preliminary & Problem Definition - extractive body cue:** 2) DINOv2 [48] aligns augmented different views of the same image using contrastive loss, allowing zgeo = f DINOv2 v (x) to capture geometric consistency.
- **p. 3 / 3. Preliminary & Problem Definition - extractive body cue:** 2, this establishes the foundation for feature selection and fusion design: 1) SigLIP [74] employs visual and text encoders f SigLIP v (·) and f ...
- **p. 5 / 4.4. Cross-Scene Spatiotemporal Consistency - extractive body cue:** The dynamic-object loss is formulated as: \smal l \mathcal { L} _{\text {d yn-4D}} = \b ig \/ (\ ha t {\ mathbf {z}}_{i^*}^{\text {dyn-4D}} ...
- **p. 6 / 4.4. Cross-Scene Spatiotemporal Consistency - extractive body cue:** The global-depth loss is defined as: \smal l \ m ath cal {L}_{ \ te x t { dep-4D}} =
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 3 (3. Preliminary & Problem Definition), p. 3 (3. Preliminary & Problem Definition), p. 5 (4.4. Cross-Scene Spatiotemporal Consistency), p. 6 (4.4. Cross-Scene Spatiotemporal Consistency), p. 6 (4.4. Cross-Scene Spatiotemporal Consistency).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Current, Vision-Language-Action, VLA, models, primarily, focus, mapping, observations, actions, exhibit, notable, limitations, spatiotemporal, perception | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | Current, Vision-Language-Action, VLA, models, primarily, focus, mapping, observations, actions, exhibit | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | contributions, summarized, follows, ConsisVLA-4D, efficient, innovative, framework, advances, spatiotemporal, consistency | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | During, process, initialized, action, tokens, decoded, parallel, yield, optimized, loss | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / Abstract - extractive body cue:** Current Vision-Language-Action (VLA) models primarily focus on mapping 2D observations to actions but exhibit notable limitations in spatiotemporal perception and reasoning: 1) spatial representations often ...
- **p. 1 / 1. Introduction - extractive body cue:** D): 1) CV-Aligner extracts instructionrelated and cross-correlated spatial objects; 2) CO-Fuser aggregates multi-view geometric relation; 3) CS-Thinker infers actions based on implicit knowledge of future ...
- **p. 4 / 4.1. Proposed Framework - extractive body cue:** We concatenate the initialized action chunk 0A at the end of the sequence and apply our proposed Spatiotemporal Consistency Attention (SC-Attn) to ultimately obtain the ...
- **p. 3 / 3. Preliminary & Problem Definition - extractive body cue:** 3) VGGT [64] takes M RGB images (xi)M i=1 from the same 3D scene and outputs depth maps Di, point maps Pi, and feature grids ...
- **p. 2 / 3) Cross-Scene - extractive body cue:** During inference, these pre-learned knowledge sets account for less than 10% of the observation-instruction sequence, enabling efficient 4D visual reasoning.
- **p. 5 / 4.4. Cross-Scene Spatiotemporal Consistency - extractive body cue:** In the SC-Attn module, each dynamic token 0dyn-4D i is independently guided by its corresponding object representation zobj-3D i and the instruction embedding t: \ ...
- **p. 3 / 3. Preliminary & Problem Definition - extractive body cue:** Analogous to how the human retina captures 2D images while the brain integrates spatial cues and predicts future states during manipulation, VLA models should inherit ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | The significant throughput improvement by 33.4 Hz enables real-time, smooth operation of large VLA models on real hardware. | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | We concatenate the initialized action chunk 0A at the end of the sequence and apply our proposed Spatiotemporal Consistency Attention (SC-Attn) to ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | The significant throughput improvement by 33.4 Hz enables real-time, smooth operation of large VLA models on real hardware. | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / 5.2. Overall Performance & Efficiency - extractive body cue:** Compared to simulation, the real-world setup adds a new viewpoint input, increases the action chunk size from 8 to 25, and reduces the training batch ...
- **p. 6 / 4.4. Cross-Scene Spatiotemporal Consistency - extractive body cue:** Latency and Throughput (T-put) represent the inference delay and the number of predicted actions per second, while Cost indicates the time required for every 10k ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** contributions, summarized, follows, ConsisVLA-4D, efficient, innovative, framework, advances, spatiotemporal, consistency, D-Perception, D-Reasoning, introduce, CV-Aligner, CO-Fuser, ensure, crossview, object, semantic, cross-object.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | We conduct evaluations across multiple simulation benchmarks, including: 1) the four task suites of LIBERO [44]-Spatial, Object, Goal, and Long; 2) three ... | p. 6 (5.1. Experimental Setup), p. 7 (5.1. Experimental Setup) |
| Action / skill decoding | 3, despite adding approximately 2B parameters (mainly from VGGT), ConsisVLA-4D achieves 2.31× and 1.25× speedups in inference latency and 1.36× and 1.43× ... | p. 7 (5.2. Overall Performance & Efficiency), p. 6 (5.1. Experimental Setup) |
| Receding execution / feedback | Particularly, it achieves exceptional success rates of 98.8% and 99.8% in the Spatial and Object suites, which assess spatial perception and object ... | p. 7 (5.2. Overall Performance & Efficiency), p. 7 (5.2. Overall Performance & Efficiency) |

## Failure and Ablation Link

- **p. 7 / 5.1. Experimental Setup - extractive body cue:** Ablation components include ES-Selection, Single-Fusion from CVAligner, and Group-Fusion, IG-Aggregation from CO-Fuser.
- **p. 7 / 5.1. Experimental Setup - extractive body cue:** Ablation Study on CV-Aligner and CO-Fuser.
- **p. 8 / 5.3. Ablation Studies - extractive body cue:** Ablation Study on sparsification ratio (Spf.Ratio). "†" denotes reproduced results of FastV and SliME.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 6. Ablation Study on CS-Thinker. Dyn. O. and Glob. D. represent the training-only dynamic objects and global depth representations in 4D-Reasoning, respectively. Dyn. O. ...
- **p. 7 / 5.3. Ablation Studies - extractive body cue:** 5, for both simulation and real-world results: 1) Removing ES-Sel. and S-Fus. from CV-Aligner prevents the filtering of redundant visual inputs and fails to align ...
- **p. 8 / 6. Conclusion - extractive body cue:** Through the integration of CVAligner, CO-Fuser, and CS-Thinker, it achieves cross-view, cross-object, and cross-scene consistency, enabling robust and efficient understanding of dynamic environments.
- **p. 7 / 5.2. Overall Performance & Efficiency - extractive body cue:** Notably, its realworld results are nearly consistent with those on RoboTwin 2.0 (ALOHA manipulator), demonstrating robust sim-toreal transfer capability.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (3) Cross-Scene), p. 4 (4.1. Proposed Framework), p. 5 (4.4. Cross-Scene Spatiotemporal Consistency), p. 1 (Abstract), p. 5 (4.4. Cross-Scene Spatiotemporal Consistency), p. 3 (3. Preliminary & Problem Definition), objective p. 6 (4.4. Cross-Scene Spatiotemporal Consistency), p. 2 (1. Introduction), p. 3 (3. Preliminary & Problem Definition), p. 3 (3. Preliminary & Problem Definition), p. 5 (4.4. Cross-Scene Spatiotemporal Consistency), p. 6 (4.4. Cross-Scene Spatiotemporal Consistency), temporal p. 7 (5.2. Overall Performance & Efficiency), p. 4 (4.1. Proposed Framework), p. 6 (4.4. Cross-Scene Spatiotemporal Consistency), p. 1 (Abstract), p. 1 (Abstract), p. 2 (3) Cross-Scene).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
