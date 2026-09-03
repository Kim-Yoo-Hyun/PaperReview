# Method - From Seeing to Doing: Bridging Reasoning and Decision for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (34 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=yngvAamNQi; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/245158. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 6 (4. How to avoid collisions?), p. 5 (4. How to avoid collisions?), p. 1 (ABSTRACT), p. 6 (4. How to avoid collisions?), p. 2 (1 INTRODUCTION), p. 5 (4. How to avoid collisions?)): The training process unfolds in two stages: General Spatial Reasoning Enhancement: In the first stage, we use our Level 1-3 data to cultivate the model's core embodied spatial reasoning.

## Method Body Digest

- **p. 6 / 4. How to avoid collisions? - extractive body cue:** The training process unfolds in two stages: General Spatial Reasoning Enhancement: In the first stage, we use our Level 1-3 data to cultivate the model's ...
- **p. 5 / 4. How to avoid collisions? - extractive body cue:** For visual trace generation (Level 5 Dataset), we employ a two-stage approach: first applying self-supervised keypoint extraction (Huang et al., 2024) to identify grasp points ...
- **p. 1 / ABSTRACT - extractive body cue:** To address these limitations, we propose FSD (From Seeing to Doing), a novel vision-language model that generates intermediate representations through spatial relationship reasoning, providing fine-grained ...
- **p. 6 / 4. How to avoid collisions? - extractive body cue:** FSD's architecture features a frozen CLIP-ViT-L (Gao et al., 2024) image encoder and a Vicuna-13B (Zheng et al., 2023b) LLM, which are connected by a ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We argue that the key to generalization lies not merely in predicting visual aids, but in first conducting explicit reasoning over the spatial and semantic ...
- **p. 5 / 4. How to avoid collisions? - extractive body cue:** It first produces grounding data (Level 1 ) by using a VLM to nominate objects and a vision model to extract their bounding boxes.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Current approaches (Kim et al., 2024; Brohan et al., 2023; Ni et al., 2025) leverage pre-trained Vision-Language Models (VLMs) and transform them into Vision-Language-Action Models ...
- **p. 6 / 4. How to avoid collisions? - extractive body cue:** Subsequently, we optimize the path trajectory using gradient descent-based interpolation, generating complete motion trajectories in SE(3) space, enabling the robotic arm to follow the 3D ...

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To this end, we propose FSD (From Seeing to Doing), a novel framework that generates these visual intermediate representations through structured spatial reasoning (Fig.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our contributions include: 1) A novel paradigm where VLM reasoning generates versatile visual aids, enabling either direct open-loop control or serving as the high-level planner ...
- **p. 4 / 4. How to avoid collisions? - extractive body cue:** Based on these considerations, we introduce Spatial Relationship-Focused Visual Chain-of-thought (SrCoT).

## Source Evidence Cues

- **p. 6 / 4. How to avoid collisions? - extractive body cue:** The training process unfolds in two stages: General Spatial Reasoning Enhancement: In the first stage, we use our Level 1-3 data to cultivate the model's ...
- **p. 5 / 4. How to avoid collisions? - extractive body cue:** For visual trace generation (Level 5 Dataset), we employ a two-stage approach: first applying self-supervised keypoint extraction (Huang et al., 2024) to identify grasp points ...
- **p. 1 / ABSTRACT - extractive body cue:** To address these limitations, we propose FSD (From Seeing to Doing), a novel vision-language model that generates intermediate representations through spatial relationship reasoning, providing fine-grained ...
- **p. 6 / 4. How to avoid collisions? - extractive body cue:** FSD's architecture features a frozen CLIP-ViT-L (Gao et al., 2024) image encoder and a Vicuna-13B (Zheng et al., 2023b) LLM, which are connected by a ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We argue that the key to generalization lies not merely in predicting visual aids, but in first conducting explicit reasoning over the spatial and semantic ...
- **p. 5 / 4. How to avoid collisions? - extractive body cue:** It first produces grounding data (Level 1 ) by using a VLM to nominate objects and a vision model to extract their bounding boxes.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Current approaches (Kim et al., 2024; Brohan et al., 2023; Ni et al., 2025) leverage pre-trained Vision-Language Models (VLMs) and transform them into Vision-Language-Action Models ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | The training process unfolds in two stages: General Spatial Reasoning Enhancement: In the first stage, we use our Level 1-3 data to ... | p. 6 (4. How to avoid collisions?), p. 5 (4. How to avoid collisions?) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | For visual trace generation (Level 5 Dataset), we employ a two-stage approach: first applying self-supervised keypoint extraction (Huang et al., 2024) to ... | p. 5 (4. How to avoid collisions?), p. 1 (ABSTRACT) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | To address these limitations, we propose FSD (From Seeing to Doing), a novel vision-language model that generates intermediate representations through spatial relationship ... | p. 1 (ABSTRACT), p. 6 (4. How to avoid collisions?) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 4. How to avoid collisions? - extractive body cue:** Subsequently, we optimize the path trajectory using gradient descent-based interpolation, generating complete motion trajectories in SE(3) space, enabling the robotic arm to follow the 3D ...
- **p. 4 / 4. How to avoid collisions? - extractive body cue:** 3 (Top)), when executing tasks like "putting broccoli into a pot," humans first locate relevant objects, then plan movement paths based on relative positions while ...
- **p. 5 / 4. How to avoid collisions? - extractive body cue:** To address this, we developed a progressive, weakto-strong data pipeline to cultivate these abilities hierarchically.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 6 (4. How to avoid collisions?).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | driving, force, behind, robotics, research, pursuit, generalization, creating, agents, capable, versatile, action, across, diverse | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | driving, force, behind, robotics, research, pursuit, generalization, creating, agents, capable | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | FSD, Seeing, Doing, novel, framework, generates, visual, intermediate, representations, through | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | Subsequently, optimize, path, trajectory, gradient, descent-based, interpolation, generating, complete, motion | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1 INTRODUCTION - extractive body cue:** A driving force behind robotics research is the pursuit of generalization: creating agents capable of versatile action across diverse robotic platforms, extending beyond familiar tasks, ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** End-to-end VLAs (Black et al., 2024; Brohan et al., 2023) attempt a direct mapping from multimodal inputs to low-level actions, but the disconnect between pre-trained ...
- **p. 6 / 4. How to avoid collisions? - extractive body cue:** 4 TRAINING AND ACTION EXECUTION OF FSD Training: We adopt the instruction tuning pipeline from LLaVA-1.5 (Liu et al., 2024c), as illustrated in Fig.
- **p. 4 / 4. How to avoid collisions? - extractive body cue:** While VLMs struggle to directly map future actions to image coordinates, our method leverages known object relationships as reference points for multi-hop analysis, simplifying the ...
- **p. 6 / 4. How to avoid collisions? - extractive body cue:** VABench requires models to infer visual aids from natural language instructions that mimic everyday commands and is evaluated across two main tasks.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** FSD is an enhanced affordance-based VLA that generalizes effectively to new instructions and scenes through its reasoning abilities.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, they remain limited, often providing aids that are not comprehensive enough for complex decision-making and predicting raw coordinates without an explicit reasoning process, which ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Reasoning Step 1: First, lift the carrot slightly upwards to <point>[[663, 663]]</point> to clear any obstacles. | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | Reasoning Step 2: … Finally, place the carrot on the plate at <point>[[390, 416]]</point>, within the final bounding box <box>[[208, 437, 440, ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 4. How to avoid collisions? - extractive body cue:** The training process unfolds in two stages: General Spatial Reasoning Enhancement: In the first stage, we use our Level 1-3 data to cultivate the model's ...
- **p. 6 / 4. How to avoid collisions? - extractive body cue:** FSD's architecture features a frozen CLIP-ViT-L (Gao et al., 2024) image encoder and a Vicuna-13B (Zheng et al., 2023b) LLM, which are connected by a ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Current approaches (Kim et al., 2024; Brohan et al., 2023; Ni et al., 2025) leverage pre-trained Vision-Language Models (VLMs) and transform them into Vision-Language-Action Models ...
- **p. 8 / 6 EXPERIMENTS - extractive body cue:** (a) VABench-Point Model Accuracy ↑ GPT4o 9.30 ASMv2 10.07 RoboPoint 19.09 RoboBrain 7.00 FSD 61.82 w/o SrCoT 26.21 w/o Alignment 55.92 (b) VABench-VisualTrace Model RMSE↓ ...
- **p. 6 / 4. How to avoid collisions? - extractive body cue:** FSD's architecture features a frozen CLIP-ViT-L (Gao et al., 2024) image encoder and a Vicuna-13B (Zheng et al., 2023b) LLM, which are connected by a ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** training, process, unfolds, stages, General, Spatial, Reasoning, Enhancement, first, stage, Level, data, cultivate, model, core, embodied, visual, trace, generation, Dataset.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | For Doing, we conducted zero-shot manipulation experiments in both SimplerEnv (Li et al., 2024c) simulation and real-world xArm robotic platforms to assess ... | p. 7 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS) |
| Action / skill decoding | 3, FSD significantly outperforms all baselines in generating precise spatial affordances and visual traces. | p. 8 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS) |
| Receding execution / feedback | Type Model Put Spoon on Towel Put Carrot on Plate Stack Green Block on Yellow Block Put Eggplant in Yellow Basket Avg ... | p. 9 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS) |

## Failure and Ablation Link

- **p. 33 / Figure/Table caption - extractive body cue:** Table 8: Ablation study on the impact of Stage 1 training. We compare the full FSD model against a variant trained without the foundational spatial ...
- **p. 9 / 6 EXPERIMENTS - extractive body cue:** Without dedicated fine-tuning, end-to-end VLAs may suffer from severe performance breakdowns (with success rates approaching zero) when faced with substantial variations in backgrounds and instructions.
- **p. 34 / Figure/Table caption - extractive body cue:** Figure 17: Visual comparison demonstrating the effectiveness of Self-Consistency Alignment. It is worth noting that without self-consistent alignment, the model's textual reasoning process is logically ...
- **p. 7 / 6 EXPERIMENTS - extractive body cue:** For models without point output support, we asked models to output bounding boxes of target regions, then sampled evenly within these bounding boxes.
- **p. 8 / 6 EXPERIMENTS - extractive body cue:** Ablation studies validate the critical contributions of both SrCoT and self-consistency alignment, confirming that our reasoning-based approach enables more accurate predictions than purely data-driven methods.
- **p. 9 / 6 EXPERIMENTS - extractive body cue:** Pick up strawberry Place egg in green pot Remove egg from plate Fold the towel Move cucumber between pot and bowl Move strawberry left of ...
- **p. 10 / 6 EXPERIMENTS - extractive body cue:** This approach avoids both the costly fine-tuning and step-by-step inference required by OpenVLA and the system overhead of a multicomponent pipeline like MOKA.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 6 (4. How to avoid collisions?), p. 5 (4. How to avoid collisions?), p. 1 (ABSTRACT), p. 6 (4. How to avoid collisions?), p. 2 (1 INTRODUCTION), p. 5 (4. How to avoid collisions?), objective p. 6 (4. How to avoid collisions?), p. 4 (4. How to avoid collisions?), p. 5 (4. How to avoid collisions?), temporal p. 9 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS), p. 10 (6 EXPERIMENTS), p. 10 (6 EXPERIMENTS), p. 3 (2 RELATED WORK), p. 5 (4. How to avoid collisions?).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
