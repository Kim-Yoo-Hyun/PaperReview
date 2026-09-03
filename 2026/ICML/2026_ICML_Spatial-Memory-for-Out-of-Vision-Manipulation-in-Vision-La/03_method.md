# Method - Spatial Memory for Out-of-Vision Manipulation in Vision-Language-Action

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=5i888dLp8N; PDF retrieval source: https://openreview.net/pdf/95685162fa940bca32702d659b96eebf84138a75.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (3.1. Spatial Memory Construction), p. 3 (3. Method), p. 4 (3.1. Spatial Memory Construction), p. 6 (3.3. Contextual Memory Retrieval), p. 6 (3.3. Contextual Memory Retrieval), p. 4 (3.1. Spatial Memory Construction)): Each sampled frame fi ∈˜V is processed by a unified perception pipeline consisting of: (1) a geometry prior network (VGGT (Wang et al., 2025b)) for camera pose and coarse scene ...

## Method Body Digest

- **p. 3 / 3.1. Spatial Memory Construction - extractive body cue:** Each sampled frame fi ∈˜V is processed by a unified perception pipeline consisting of: (1) a geometry prior network (VGGT (Wang et al., 2025b)) for ...
- **p. 3 / 3. Method - extractive body cue:** During manipulation, the model receives the current observation ot c, the user instruction, robot states, and a noised action sequence, where c ∈{l, r, h} ...
- **p. 4 / 3.1. Spatial Memory Construction - extractive body cue:** Dynamic Memory Refinement ··· ··· ··· Instruction: "Pick the pink cup and place it in the basket." Text Tokenizer VLM Robot State: {%% ", %& ...
- **p. 6 / 3.3. Contextual Memory Retrieval - extractive body cue:** Through these DiT blocks, the model fuses current observations with the structured scene memory, producing refined state and action tokens.
- **p. 6 / 3.3. Contextual Memory Retrieval - extractive body cue:** Each memory token mt k is first projected into the same latent space as the VLM features via an alignment function: ˜mt k = Φalign( ...
- **p. 4 / 3.1. Spatial Memory Construction - extractive body cue:** The object features fk are then projected into a shared embedding space through a learnable mapping Φmem(·), and combined with their corresponding spatial descriptors to ...
- **p. 5 / 3.2. Dynamic Memory Refinement - extractive body cue:** Behavioral Analysis on Real-World Out-of-Vision Tasks Model Task 1 Task 2 Task 3 Task 4 Task 5 First-Fixation Time (s) ↓ GR00T-N1.5 7.6 21.0 14.8 ...
- **p. 3 / 3. Method - extractive body cue:** New observations from the head view ot h are incorporated to update M0 into ˆ Mt through Dynamic Memory Refinement, which performs similarity-aware fusion to ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** Based on these insights, we introduce SOMA, a VLA framework for out-of-vision manipulation that equips the robot with persistent spatial memory for reasoning and action.
- **p. 2 / 1. Introduction - extractive body cue:** In particular, integrating angular-wise observations into a coherent spatial-semantic memory enables globally consistent reasoning and effective manipulation even when task-relevant objects are temporarily out of ...
- **p. 3 / 3. Method - extractive body cue:** By maintaining a globally consistent spatial memory, SOMA enables robust reasoning and manipulation even when task-relevant objects lie outside the current field of view.

## Source Evidence Cues

- **p. 3 / 3.1. Spatial Memory Construction - extractive body cue:** Each sampled frame fi ∈˜V is processed by a unified perception pipeline consisting of: (1) a geometry prior network (VGGT (Wang et al., 2025b)) for ...
- **p. 3 / 3. Method - extractive body cue:** During manipulation, the model receives the current observation ot c, the user instruction, robot states, and a noised action sequence, where c ∈{l, r, h} ...
- **p. 4 / 3.1. Spatial Memory Construction - extractive body cue:** Dynamic Memory Refinement ··· ··· ··· Instruction: "Pick the pink cup and place it in the basket." Text Tokenizer VLM Robot State: {%% ", %& ...
- **p. 6 / 3.3. Contextual Memory Retrieval - extractive body cue:** Through these DiT blocks, the model fuses current observations with the structured scene memory, producing refined state and action tokens.
- **p. 6 / 3.3. Contextual Memory Retrieval - extractive body cue:** Each memory token mt k is first projected into the same latent space as the VLM features via an alignment function: ˜mt k = Φalign( ...
- **p. 4 / 3.1. Spatial Memory Construction - extractive body cue:** The object features fk are then projected into a shared embedding space through a learnable mapping Φmem(·), and combined with their corresponding spatial descriptors to ...
- **p. 5 / 3.2. Dynamic Memory Refinement - extractive body cue:** Behavioral Analysis on Real-World Out-of-Vision Tasks Model Task 1 Task 2 Task 3 Task 4 Task 5 First-Fixation Time (s) ↓ GR00T-N1.5 7.6 21.0 14.8 ...
- **Detected method headings:** 3. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Each sampled frame fi ∈˜V is processed by a unified perception pipeline consisting of: (1) a geometry prior network (VGGT (Wang et ... | p. 3 (3.1. Spatial Memory Construction), p. 3 (3. Method) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | During manipulation, the model receives the current observation ot c, the user instruction, robot states, and a noised action sequence, where c ... | p. 3 (3. Method), p. 4 (3.1. Spatial Memory Construction) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | Dynamic Memory Refinement ··· ··· ··· Instruction: "Pick the pink cup and place it in the basket." Text Tokenizer VLM Robot State: ... | p. 4 (3.1. Spatial Memory Construction), p. 6 (3.3. Contextual Memory Retrieval) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3. Method - extractive body cue:** New observations from the head view ot h are incorporated to update M0 into ˆ Mt through Dynamic Memory Refinement, which performs similarity-aware fusion to ...
- **p. 4 / 3.1. Spatial Memory Construction - extractive body cue:** Similarity EMA Update ℳ! ℳ" ℳ"" ℳ" ℳ, Query Key/Value 2 1 3 Can not find the pick cup.
- **p. 4 / 3.1. Spatial Memory Construction - extractive body cue:** (B) Dynamic Memory Refinement: During interaction, newly perceived information Mt is adaptively fused into the initial overview scene memory M0 through similarity-weighted updates, yielding a ...
- **p. 5 / 3.2. Dynamic Memory Refinement - extractive body cue:** The two scores jointly determine an adaptive update coefficient αt kj = gt kj · st kj.
- **p. 5 / 3.2. Dynamic Memory Refinement - extractive body cue:** The updated memory is denoted as ˆ Mt = { ˆmt k}NM t k=1, where N M t is the number of memory entries.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 3 (3. Method), p. 4 (3.1. Spatial Memory Construction), p. 4 (3.1. Spatial Memory Construction), p. 5 (3.2. Dynamic Memory Refinement), p. 5 (3.2. Dynamic Memory Refinement).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | systems, typically, extend, large-scale, pre-trained, Multimodal, Large, Language, Models, MLLMs, Bjorck, Yang, action, head | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | systems, typically, extend, large-scale, pre-trained, Multimodal, Large, Language, Models, MLLMs | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | insights, introduce, SOMA, VLA, framework, out-of-vision, manipulation, equips, robot, persistent | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | New, observations, head, view, incorporated, update, through, Dynamic, Memory, Refinement | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1. Introduction - extractive body cue:** These systems typically extend large-scale pre-trained Multimodal Large Language Models (MLLMs) (Bjorck et al., 2025; Yang et al., 2025a) with an action head or specialized ...
- **p. 3 / 3. Method - extractive body cue:** During manipulation, the model receives the current observation ot c, the user instruction, robot states, and a noised action sequence, where c ∈{l, r, h} ...
- **p. 4 / 3.1. Spatial Memory Construction - extractive body cue:** Dynamic Memory Refinement ··· ··· ··· Instruction: "Pick the pink cup and place it in the basket." Text Tokenizer VLM Robot State: {%% ", %& ...
- **p. 6 / 3.3. Contextual Memory Retrieval - extractive body cue:** Through these DiT blocks, the model fuses current observations with the structured scene memory, producing refined state and action tokens.
- **p. 3 / 3. Method - extractive body cue:** The resulting memory-enhanced vision-language tokens, together with robot states and noised action embeddings, are processed by DiT blocks and an action decoder to predict the ...
- **p. 6 / 3.3. Contextual Memory Retrieval - extractive body cue:** The original vision-language tokens, robot state, and noised action embeddings are directly fed into the DiT, where Xboost serves as global context that modulates token ...
- **p. 4 / 3.1. Spatial Memory Construction - extractive body cue:** Spatial Memory for Out-of-Vision Manipulation in Vision-Language-Action 1 2 3 Before Manipulation: Head Scanning A.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Each observation is associated to at most one memory instance, and each memory entry is updated by at most one observation per ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | Given a scanning video sequence V = {fi}Nv i=1, we uniformly sample one frame every N frames to obtain a subset ˜V ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | Each observation is associated to at most one memory instance, and each memory entry is updated by at most one observation per ... | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | During training, all components are optimized except the VLM language decoder, using multi-task learning with a batch size of 60 for 30,000 ... | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 4.2. Implementation - extractive body cue:** During training, all components are optimized except the VLM language decoder, using multi-task learning with a batch size of 60 for 30,000 steps on 32 ...
- **p. 6 / 4.2. Implementation - extractive body cue:** All inference are executed on a server equipped with an NVIDIA RTX 4090 GPU.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** sampled, frame, processed, unified, perception, pipeline, consisting, geometry, prior, network, VGGT, Wang, camera, pose, coarse, scene, estimation, semantic, module, YOLO.
- **Relevant PDF headings:** 3. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | SimplerEnv offers a standardized real-to-sim benchmark for evaluating policy success rates across simulated environments reflecting real-world robotic systems (Zitkovich et al., 2023). | p. 6 (4.1. Benchmarks), p. 6 (4.1. Benchmarks) |
| Action / skill decoding | Table 5. Ablation study on different components of the proposed memory design. "Geo." and "Obj." denote Geometric cues and object semantics, respectively. ... | p. 8 (Figure/Table caption), p. 8 (4.4. Simulation Results) |
| Receding execution / feedback | In Figure 4, SOMA achieves the highest success rates across all five real-world out-of-vision (OOV) manipulation tasks. | p. 7 (4.3. Real World Results), p. 7 (4.3. Real World Results) |

## Failure and Ablation Link

- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Ablation study on scan-based exploration and spatial mem- ory for real-world OOV manipulation. Scan+GR00T performs head scanning and uses the detected target frame ...
- **p. 18 / Figure/Table caption - extractive body cue:** Table 10. Detailed Ablation studies on Robocasa Tabletop GR-1 benchmark. We compare different Update Strategies, Retrieval Modules, and Memory Representations. Reported values are success rates ...
- **p. 8 / 4.5. Ablation Study - extractive body cue:** As shown in Table 5, we conduct the ablation study on different components of the overview scene memory.
- **p. 8 / 4.4. Simulation Results - extractive body cue:** Ablation study on different components of the proposed memory design. "Geo." and "Obj." denote Geometric cues and object semantics, respectively.
- **p. 7 / 4.3. Real World Results - extractive body cue:** The fixed-head variant fails once either the target or the goal leaves the field of view, confirming the brittleness of view-bound policies under partial observability.
- **p. 7 / 4.3. Real World Results - extractive body cue:** No-Scan SOMA slightly outperforms Scan+GR00T despite using only a single-view initialization, highlighting the benefit of an explicit memory structure even without multi-view coverage.
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 8. Analysis about time and gpu cost per demo of different component choice in the memory preprocess stage. raw 3D bounding box bk ∈R8×3 ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (3.1. Spatial Memory Construction), p. 3 (3. Method), p. 4 (3.1. Spatial Memory Construction), p. 6 (3.3. Contextual Memory Retrieval), p. 6 (3.3. Contextual Memory Retrieval), p. 4 (3.1. Spatial Memory Construction), objective p. 3 (3. Method), p. 4 (3.1. Spatial Memory Construction), p. 4 (3.1. Spatial Memory Construction), p. 5 (3.2. Dynamic Memory Refinement), p. 5 (3.2. Dynamic Memory Refinement), temporal p. 5 (3.2. Dynamic Memory Refinement), p. 3 (3.1. Spatial Memory Construction), p. 3 (3. Method), p. 5 (3.2. Dynamic Memory Refinement), p. 6 (4.1. Benchmarks), p. 6 (4.1. Benchmarks).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (24 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** The resulting memory-enhanced vision-language tokens, together with robot states and noised action embeddings, are processed by DiT blocks and an action decoder to predict the next action chunk. (p. 3, 3. Method).
- **Objective/update evidence:** New observations from the head view ot h are incorporated to update M0 into ˆ Mt through Dynamic Memory Refinement, which performs similarity-aware fusion to preserve global consistency while accommodating ... (p. 3, 3. Method).
- **Temporal/runtime evidence:** Given a scanning video sequence V = {fi}Nv i=1, we uniformly sample one frame every N frames to obtain a subset ˜V , which is used to construct the overview ... (p. 3, 3.1. Spatial Memory Construction).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
