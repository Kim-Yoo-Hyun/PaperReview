# Method - JanusVLN: Decoupling Semantics and Spatiality with Dual Implicit Memory for Vision-Language Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (26 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=RnuB0Nlbd5; PDF retrieval source: https://openreview.net/pdf/3a4cf4bcb2788c66a1d7b5ee498986d37ab4fa87.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3 METHOD), p. 5 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD), p. 6 (3 METHOD), p. 6 (3 METHOD)): VGGT (Wang et al., 2025a), which is based on a transformer feed-forward architecture, comprises three key components: an encoder for extracting single-image feature, a fusion decoder for cross-frame interaction to ...

## Method Body Digest

- **p. 4 / 3 METHOD - extractive PDF cue:** VGGT (Wang et al., 2025a), which is based on a transformer feed-forward architecture, comprises three key components: an encoder for extracting single-image feature, a fusion ...
- **p. 5 / 3 METHOD - extractive PDF cue:** These KV, derived from the output of attention modules such as transformers, constitute high-level semantic abstractions and structured representations of the past environment.
- **p. 4 / 3 METHOD - extractive PDF cue:** As our focus is on feature extraction, which embeds 3D geometry prior information, rather than directly outputting 3D attributes, we leverage the encoder and the ...
- **p. 5 / 3 METHOD - extractive PDF cue:** Finally, these two complementary features are fused and fed into LLM to predict the next action. representations by respectively leveraging the history initial and sliding ...
- **p. 6 / 3 METHOD - extractive PDF cue:** For 3D spatial-geometric encoder, we employ the pre-trained encoder and fusion decoder from VGGT (Wang et al., 2025a) model to interactively encode the input frame ...
- **p. 6 / 3 METHOD - extractive PDF cue:** Upon acquiring the semantic features S1 t and spatial geometric features Gt, we first employ the spatial merging strategy from Qwen2.5-VL (Bai et al., 2025).
- **p. 4 / 3 METHOD - extractive PDF cue:** 3.2 DUAL IMPLICIT MEMORY The limitations of traditional explicit semantic memory, including memory inflation, computational redundancy, and the loss of spatial information, coupled with the ...
- **p. 5 / 3 METHOD - extractive PDF cue:** It enables the agent to retrieve and reason over information with minimal computational cost.

## Design Rationale

- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** In summary, our contributions are as follows: • We introduce a novel dual implicit memory paradigm for VLN.
- **p. 4 / 3 METHOD - extractive PDF cue:** To address these challenges, we introduce the VGGT as a spatial geometry encoder and propose a novel dual implicit memory paradigm for VLN research in ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** To this end, we introduce JanusVLN, a dual implicit memory framework for VLN that features both spatialgeometric and visual-semantic memory in Figure 1.

## Source Evidence Cues

- **p. 4 / 3 METHOD - extractive PDF cue:** VGGT (Wang et al., 2025a), which is based on a transformer feed-forward architecture, comprises three key components: an encoder for extracting single-image feature, a fusion ...
- **p. 5 / 3 METHOD - extractive PDF cue:** These KV, derived from the output of attention modules such as transformers, constitute high-level semantic abstractions and structured representations of the past environment.
- **p. 4 / 3 METHOD - extractive PDF cue:** As our focus is on feature extraction, which embeds 3D geometry prior information, rather than directly outputting 3D attributes, we leverage the encoder and the ...
- **p. 5 / 3 METHOD - extractive PDF cue:** Finally, these two complementary features are fused and fed into LLM to predict the next action. representations by respectively leveraging the history initial and sliding ...
- **p. 6 / 3 METHOD - extractive PDF cue:** For 3D spatial-geometric encoder, we employ the pre-trained encoder and fusion decoder from VGGT (Wang et al., 2025a) model to interactively encode the input frame ...
- **p. 6 / 3 METHOD - extractive PDF cue:** Upon acquiring the semantic features S1 t and spatial geometric features Gt, we first employ the spatial merging strategy from Qwen2.5-VL (Bai et al., 2025).
- **Detected method headings:** 3 METHOD (p. 4); A THE USE OF LARGE LANGUAGE MODELS (LLMS) (p. 18); B MODEL STRUCTURE DETAILS (p. 18)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | VGGT (Wang et al., 2025a), which is based on a transformer feed-forward architecture, comprises three key components: an encoder for extracting single-image ... | p. 4 (3 METHOD), p. 5 (3 METHOD) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | These KV, derived from the output of attention modules such as transformers, constitute high-level semantic abstractions and structured representations of the past ... | p. 5 (3 METHOD), p. 4 (3 METHOD) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | As our focus is on feature extraction, which embeds 3D geometry prior information, rather than directly outputting 3D attributes, we leverage the ... | p. 4 (3 METHOD), p. 5 (3 METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3 METHOD - extractive PDF cue:** 3.2 DUAL IMPLICIT MEMORY The limitations of traditional explicit semantic memory, including memory inflation, computational redundancy, and the loss of spatial information, coupled with the ...
- **p. 5 / 3 METHOD - extractive PDF cue:** It enables the agent to retrieve and reason over information with minimal computational cost.
- **p. 6 / 3 METHOD - extractive PDF cue:** Building upon the dual implicit memory paradigm, we propose JanusVLN in Figure 2, enhances the spatial understanding capabilities without requiring costly 3D data (e.g., depth).
- **p. 6 / 3 METHOD - extractive PDF cue:** (3) Additionally, Qwen2.5-VL (Bai et al., 2025) groups spatially adjacent 2ˆ2 patches into a single image token to reduce computational cost, yielding S1 t P ...
- **p. 5 / 3 METHOD - extractive PDF cue:** For the implicit neural representation, we employ a hybrid cache update strategy instead of caching all historical KV.
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 4 (3 METHOD), p. 5 (3 METHOD), p. 5 (3 METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Published, conference, ICLR, Record, Instruction, Turn, right, walk, towards, door, Large, Language, Model, Action | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | Published, conference, ICLR, Record, Instruction, Turn, right, walk, towards, door | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | summary, contributions, follows, introduce, novel, dual, implicit, memory, paradigm, VLN | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | DUAL, IMPLICIT, MEMORY, limitations, traditional, explicit, semantic, including, inflation, computational | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 3 METHOD - extractive PDF cue:** Published as a conference paper at ICLR 2026 Record Instruction: Turn right and walk towards the door… Large Language Model Action: 3D Spatial Geometry Encoder ...
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** Vision-and-Language Navigation (VLN) is a foundational task in embodied AI, requiring an agent to navigate through unseen environments guided by visual inputs and natural language ...
- **p. 4 / 3 METHOD - extractive PDF cue:** Upon executing the action at`1, the agent receives a new observation xt`1.
- **p. 4 / 3 METHOD - extractive PDF cue:** This process iterates until the agent executes the Stop action at the target location as specified by the instruction.
- **p. 5 / 3 METHOD - extractive PDF cue:** These KV, derived from the output of attention modules such as transformers, constitute high-level semantic abstractions and structured representations of the past environment.
- **p. 6 / 3 METHOD - extractive PDF cue:** Subsequently, the final visual features, along with the text embedding of instruction I, are fed into the backbone of the MLLM to generate the next ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Another class of methods (Cheng et al., 2025; Xiang et al., 2025; Yang et al., 2025c; Li et al., 2025a) stores historical observation frames, which ...
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | 3.2 DUAL IMPLICIT MEMORY The limitations of traditional explicit semantic memory, including memory inflation, computational redundancy, and the loss of spatial information, ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | Encoder NEÓ OSÒ SRÒ SPLÒ JanusVLN w/o extra encoder 6.58 54.3 47.0 40.9 JanusVLN w/ extra DINOv2 6.44 55.4 47.5 41.5 JanusVLN ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | 3.2 DUAL IMPLICIT MEMORY The limitations of traditional explicit semantic memory, including memory inflation, computational redundancy, and the loss of spatial information, ... | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | Published as a conference paper at ICLR 2026 As shown in Figure 3, VGGT's inference time grows exponentially with each new frame ... | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 3 METHOD - extractive PDF cue:** For 3D spatial-geometric encoder, we employ the pre-trained encoder and fusion decoder from VGGT (Wang et al., 2025a) model to interactively encode the input frame ...
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** The model is trained for one epoch, during which we exclusively fine-tune the LLM and the projection layer with learning rates of 2e-5 and 1e-5, ...
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** Encoder NEÓ OSÒ SRÒ SPLÒ JanusVLN w/o extra encoder 6.58 54.3 47.0 40.9 JanusVLN w/ extra DINOv2 6.44 55.4 47.5 41.5 JanusVLN w/ extra SigLIP ...
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** Memory Size Inference Time NEÓ OSÒ SRÒ SPLÒ VGGT (8) 268 ms 5.99 56.2 50.2 45.0 VGGT (32) 1549 ms 5.66 56.8 51.2 47.6 Cached ...
- **p. 6 / 3 METHOD - extractive PDF cue:** Published as a conference paper at ICLR 2026 As shown in Figure 3, VGGT's inference time grows exponentially with each new frame due to its ...
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** JanusVLN runs on a remote server with an A10 GPU to continuously process RGB and instructions, returning the inference results to the robot for action ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** VGGT, Wang, transformer, feed-forward, architecture, comprises, three, components, encoder, extracting, single-image, feature, fusion, decoder, cross-frame, interaction, generate, geometric, tokens, where.
- **Relevant PDF headings:** 3 METHOD (p. 4); A THE USE OF LARGE LANGUAGE MODELS (LLMS) (p. 18); B MODEL STRUCTURE DETAILS (p. 18).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | These datasets comprise trajectories collected from Matterport3D (Chang et al., 2017) scenes using the Habitat simulator (Savva et al., 2019). | p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS) |
| Global / local decision | Consistent with prior work (Cheng et al., 2025; Dai et al., 2025; Yin et al., 2025; Lu et al., 2024), we report ... | p. 6 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Motion execution / recovery | Compared to methods utilizing multiple input types like panoramic views and odometry, JanusVLN achieves a 10.5-35.5 improvement in SR using only a ... | p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |

## Failure and Ablation Link

- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** We provide an ablation study in Table 4 to investigate the effect of introducing additional encoders.
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** This suggests that the dual implicit memory, as a novel memory paradigm, can effectively replace conventional textual cognitive maps and historical frames.
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** Notably, even without any additional data, JanusVLN* still outperforms the aforementioned methods that rely on partial extra data by a margin of 3.7-18.8 in SPL.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** The ablation study for dual implicit memory is presented in Table 3.
- **p. 10 / 4 EXPERIMENTS - extractive PDF cue:** We present the ablation studies on memory size in Table 5.
- **p. 10 / 4 EXPERIMENTS - extractive PDF cue:** Published as a conference paper at ICLR 2026 Ablation on memory size.
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: JanusVLN, using RGB-only video, decouples visual semantics and spatial geometry to construct novel, fixed-size dual implicit memory. This memory is incrementally updated during ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3 METHOD), p. 5 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD), p. 6 (3 METHOD), p. 6 (3 METHOD), objective p. 4 (3 METHOD), p. 5 (3 METHOD), p. 6 (3 METHOD), p. 6 (3 METHOD), p. 5 (3 METHOD), temporal p. 4 (3 METHOD), p. 9 (4 EXPERIMENTS), p. 4 (3 METHOD), p. 6 (3 METHOD), p. 10 (4 EXPERIMENTS), p. 2 (1 INTRODUCTION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
