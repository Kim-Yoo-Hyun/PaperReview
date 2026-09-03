# Method - Spatially Guided Training for Vision-Language-Action Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (40 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=eKhOrQWAVJ; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/247957. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 4 (1 INTRODUCTION)): We propose a new a dual-system, end-to-end VLA framework based on Qwen2.5-VL, which can foster alignment between the optimization dynamics of the spatial grounding objective and the action policy objective.

## Method Body Digest

- **p. 3 / 1 INTRODUCTION - extractive body cue:** We propose a new a dual-system, end-to-end VLA framework based on Qwen2.5-VL, which can foster alignment between the optimization dynamics of the spatial grounding objective ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** In contrast, simple spatial prompting effectively mitigates these issues (Section 3.1). • We propose ST4VLA, a spatially guided training framework that explicitly aligns action optimization ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Given a task instruction, the VLM planner produces latent plans through explicit spatial prompting, which then effectively guides the action expert to generate control signals. ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Spatial Planning Prompt VL-Input Sub-Task Planning Action Action VLM Planner DiT Actor Latent Planning Data Model Deployment Point Grounding A: The image shows a person ...
- **p. 4 / 1 INTRODUCTION - extractive body cue:** (2025) showing that direct gradient flow between action and VLM modules may distort multimodal knowledge, we introduce a gradient decay factor within the querying transformer.
- **p. 4 / 1 INTRODUCTION - extractive body cue:** By reformatting all robotic data into a unified QA structure consistent with web-scale pre-training, we enable the VLM to develop a spatially-aware representation space under ...
- **p. 1 / ABSTRACT - extractive body cue:** We introduce ST4VLA, a dual-system Vision-Language-Action framework that leverages Spatial Guided Training to align action learning with spatial priors in VLMs.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** This work makes the following contributions: • We observe that directly fine-tuning a VLM with an action expert as a VLA model leads to a ...

## Design Rationale

- **p. 3 / 1 INTRODUCTION - extractive body cue:** In contrast, simple spatial prompting effectively mitigates these issues (Section 3.1). • We propose ST4VLA, a spatially guided training framework that explicitly aligns action optimization ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** 2 METHODS We propose ST4VLA, a spatially guided training framework that bridges spatial understanding with embodied control through a novel two-stage training recipe 2.2.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address the fundamental gap between multimodal understanding and embodied control, we propose ST4VLA, a dual-system vision-language-action framework that explicitly integrates spatial priors into robot ...

## Source Evidence Cues

- **p. 3 / 1 INTRODUCTION - extractive body cue:** We propose a new a dual-system, end-to-end VLA framework based on Qwen2.5-VL, which can foster alignment between the optimization dynamics of the spatial grounding objective ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** In contrast, simple spatial prompting effectively mitigates these issues (Section 3.1). • We propose ST4VLA, a spatially guided training framework that explicitly aligns action optimization ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Given a task instruction, the VLM planner produces latent plans through explicit spatial prompting, which then effectively guides the action expert to generate control signals. ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Spatial Planning Prompt VL-Input Sub-Task Planning Action Action VLM Planner DiT Actor Latent Planning Data Model Deployment Point Grounding A: The image shows a person ...
- **p. 4 / 1 INTRODUCTION - extractive body cue:** (2025) showing that direct gradient flow between action and VLM modules may distort multimodal knowledge, we introduce a gradient decay factor within the querying transformer.
- **p. 4 / 1 INTRODUCTION - extractive body cue:** By reformatting all robotic data into a unified QA structure consistent with web-scale pre-training, we enable the VLM to develop a spatially-aware representation space under ...
- **p. 1 / ABSTRACT - extractive body cue:** We introduce ST4VLA, a dual-system Vision-Language-Action framework that leverages Spatial Guided Training to align action learning with spatial priors in VLMs.
- **Detected method headings:** C.3 Backbone-Agnostic Generalization and Training Method Contribution (p. 18); C.3 BACKBONE-AGNOSTIC GENERALIZATION AND TRAINING METHOD CONTRIBUTION (p. 22)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | We propose a new a dual-system, end-to-end VLA framework based on Qwen2.5-VL, which can foster alignment between the optimization dynamics of the ... | p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | In contrast, simple spatial prompting effectively mitigates these issues (Section 3.1). • We propose ST4VLA, a spatially guided training framework that explicitly ... | p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | Given a task instruction, the VLM planner produces latent plans through explicit spatial prompting, which then effectively guides the action expert to ... | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 1 INTRODUCTION - extractive body cue:** This work makes the following contributions: • We observe that directly fine-tuning a VLM with an action expert as a VLA model leads to a ...
- **p. 1 / ABSTRACT - extractive body cue:** This design preserves spatial grounding during policy learning and promotes consistent optimization across spatial and action objectives.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Second, it aligns the optimization dynamics of multimodal perception and action objectives, resulting in more stable and robust learning.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** We propose a new a dual-system, end-to-end VLA framework based on Qwen2.5-VL, which can foster alignment between the optimization dynamics of the spatial grounding objective ...
- **p. 4 / 1 INTRODUCTION - extractive body cue:** This attenuates the gradients propagated from the Action Expert back to the VLM (e.g., by a factor of 0.5), thereby preserving the Planner's semantic reasoning ...
- **p. 4 / 1 INTRODUCTION - extractive body cue:** Beyond co-training with spatial grounding data, where the VLM backbone is updated via next-token prediction on image-prompt pairs, we further introduce spatial prompting for action ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 3 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 4 (1 INTRODUCTION).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Noisy, Actions, DiT, Actor, Conditioned, State, Your, task, instruction, Spatial, Planning, Prompt, VL-Input, Sub-Task | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | Noisy, Actions, DiT, Actor, Conditioned, State, Your, task, instruction, Spatial | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | contrast, simple, spatial, prompting, effectively, mitigates, issues, Section, ST4VLA, spatially | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | makes, following, contributions, observe, directly, fine-tuning, VLM, action, expert, VLA | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 1 INTRODUCTION - extractive body cue:** Noisy Actions Actions DiT - Actor Conditioned State (opt) Your task is to {instruction}.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Spatial Planning Prompt VL-Input Sub-Task Planning Action Action VLM Planner DiT Actor Latent Planning Data Model Deployment Point Grounding A: The image shows a person ...
- **p. 1 / ABSTRACT - extractive body cue:** Large vision-language models (VLMs) excel at multimodal understanding but fall short when extended to embodied tasks, where instructions must be transformed into low-level motor actions.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** We propose a new a dual-system, end-to-end VLA framework based on Qwen2.5-VL, which can foster alignment between the optimization dynamics of the spatial grounding objective ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, textual instruction is sparse, whereas real-world actions demand continuous, embodied interactions.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Given a task instruction, the VLM planner produces latent plans through explicit spatial prompting, which then effectively guides the action expert to generate control signals. ...
- **p. 4 / 1 INTRODUCTION - extractive body cue:** For action sequences, we augment the standard task instruction with a spatial prompt that elicits the VLM's internal reasoning about scene geometry; for example, the ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | A key strength of our dual-system framework is its ability to leverage the high-level planner System 2 to decompose complex, reasoning-heavy tasks ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | Finally, we examine real-robot performance on both short-horizon and long-horizon tasks to validate practical deployment capabilities (Section 3.5). | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 1 INTRODUCTION - extractive body cue:** In contrast, simple spatial prompting effectively mitigates these issues (Section 3.1). • We propose ST4VLA, a spatially guided training framework that explicitly aligns action optimization ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Spatial Planning Prompt VL-Input Sub-Task Planning Action Action VLM Planner DiT Actor Latent Planning Data Model Deployment Point Grounding A: The image shows a person ...
- **p. 4 / 1 INTRODUCTION - extractive body cue:** By reformatting all robotic data into a unified QA structure consistent with web-scale pre-training, we enable the VLM to develop a spatially-aware representation space under ...
- **p. 1 / ABSTRACT - extractive body cue:** We introduce ST4VLA, a dual-system Vision-Language-Action framework that leverages Spatial Guided Training to align action learning with spatial priors in VLMs.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** dual-system, end-to-end, VLA, framework, Qwen2, foster, alignment, between, optimization, dynamics, spatial, grounding, objective, action, policy, contrast, simple, prompting, effectively, mitigates.
- **Relevant PDF headings:** C.3 Backbone-Agnostic Generalization and Training Method Contribution (p. 18); C.3 BACKBONE-AGNOSTIC GENERALIZATION AND TRAINING METHOD CONTRIBUTION (p. 22).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | 3.4 EVALUATION IN REAL-WORLD CLUTTERED-SCENE PICK-AND-PLACE We use the Franka Research 3 robot to evaluate the generalization performance of our model and ... | p. 7 (3 EXPERIMENTS), p. 6 (3 EXPERIMENTS) |
| Action / skill decoding | Figure 4: Success rate (%) across different generalization settings on 200 simulated instruction- following pick-and-place tasks. Results. Since both baseline methods, π0 ... | p. 7 (Figure/Table caption), p. 20 (Figure/Table caption) |
| Receding execution / feedback | Figure 4: Success rate (%) across different generalization settings on 200 simulated instruction- following pick-and-place tasks. Results. Since both baseline methods, π0 ... | p. 7 (Figure/Table caption), p. 20 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Ablation study on the effect of auxiliary spatial prompting during co-training. From left to right: (a) perception performance (IoU@0.5 on RefCOCO-g); (b) manipulation ...
- **p. 6 / 3 EXPERIMENTS - extractive body cue:** (2025a) ✓ 83.7 65.4 56.0 6.4 52.9 Vanilla VLA ✗ 90.0 69.8 52.5 52.2 66.1 Vanilla Co-training VLA ✓ 91.3 75.1 55.0 59.4 70.2 ST4VLA ...
- **p. 5 / 3 EXPERIMENTS - extractive body cue:** We compare three distinct training strategies using the OXE dataset for action data and a curated set of spatial grounding datasets for multimodal co-training: • ...
- **p. 22 / Figure/Table caption - extractive body cue:** Table 9: Ablation on the scaling of Spatial Grounding Pre-training data volume. Pre-training Scale Google Robot VM Google Robot VA WidowX VM Average
- **p. 23 / Figure/Table caption - extractive body cue:** Table 10: Ablation analysis of different spatial prompt formulations on SimplerEnv, comparing the default Unified Prompt against non-semantic and explicit formatting constraints. Prompt Type Google ...
- **p. 32 / Figure/Table caption - extractive body cue:** Figure 17: Showcases for real-world large scale pick-and-place manipulation w/wo co-training. We further evaluate our framework in real-world cluttered tabletop environments. As shown in Figure ...
- **p. 7 / 3 EXPERIMENTS - extractive body cue:** (2025), underwent extensive pretraining on large corpora of action data, we ensured a fair comparison by post-training our model on a large-scale dataset of 244K ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), objective p. 3 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), temporal p. 8 (3 EXPERIMENTS), p. 4 (3 EXPERIMENTS), p. 5 (3 EXPERIMENTS), p. 5 (3 EXPERIMENTS), p. 6 (3 EXPERIMENTS), p. 8 (3 EXPERIMENTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
