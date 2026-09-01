# Method - HAMSTER: Hierarchical Action Models for Open-World Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (30 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=h7aQxzKbq6; PDF retrieval source: https://openreview.net/pdf/eafdc79dd4a2aa8bac8cced6ed84a72b790f2bcd.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 21 (B.1 VLM IMPLEMENTATION DETAILS), p. 21 (B.2 LOW-LEVEL POLICY TRAINING DETAILS), p. 22 (B.2 LOW-LEVEL POLICY TRAINING DETAILS), p. 22 (B.2 LOW-LEVEL POLICY TRAINING DETAILS)): We condition the model on an image and the prompt, except when training on Pixel Point Prediction data (i.e., from Robopoint (Yuan et al., 2024b)) where we used the given ...

## Method Body Digest

- **p. 21 / B.1 VLM IMPLEMENTATION DETAILS - extractive PDF cue:** We condition the model on an image and the prompt, except when training on Pixel Point Prediction data (i.e., from Robopoint (Yuan et al., 2024b)) ...
- **p. 21 / B.2 LOW-LEVEL POLICY TRAINING DETAILS - extractive PDF cue:** For low-level policy training, we train the policies on ground truth paths constructed by projecting trajectory end-effector points to the camera image.
- **p. 22 / B.2 LOW-LEVEL POLICY TRAINING DETAILS - extractive PDF cue:** This is likely due to 3D-DA's visual attention mechanism which cross attends CLIP language token embeddings with CLIP visual features, therefore detailed language instructions are ...
- **p. 22 / B.2 LOW-LEVEL POLICY TRAINING DETAILS - extractive PDF cue:** The action tags indicate the gripper action.
- **p. 22 / B.2 LOW-LEVEL POLICY TRAINING DETAILS - extractive PDF cue:** In simulated experiments in Colosseum, no changes were needed.
- **p. 22 / B.2 LOW-LEVEL POLICY TRAINING DETAILS - extractive PDF cue:** In fact, we saw a performance drop for HAMSTER+3D-DA when removing language for Colosseum tasks and a small drop in performance when using simplified language ...
- **p. 21 / B.1 VLM IMPLEMENTATION DETAILS - extractive PDF cue:** During fine-tuning, the entire model-including the vision encoder-is updated.
- **p. 5 / 3 BACKGROUND - extractive PDF cue:** (a) VLM Path Prediction Policy Input Instruction: "Put the object in the bowl." z = Depth/3D Observation VLM response: [(0.25, 0.1, 0), (0.29, 0.3, 0), ...

## Design Rationale

- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** It is important to note that while we are certainly not the first to propose hierarchical VLA models (Gu et al., 2023; Nasiriany et al., ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** To this end, we propose a hierarchical architecture for VLAs, HAMSTER (Hierarchical Action Models with SeparaTEd Path Representations), where large fine-tuned VLMs are connected to ...
- **p. 5 / 3 BACKGROUND - extractive PDF cue:** It consists of two interconnected models: first, a higher-level VLM that is finetuned on large-scale, off-domain data to produce intermediate 2D path guidance (detailed in ...

## Source Evidence Cues

- **p. 21 / B.1 VLM IMPLEMENTATION DETAILS - extractive PDF cue:** We condition the model on an image and the prompt, except when training on Pixel Point Prediction data (i.e., from Robopoint (Yuan et al., 2024b)) ...
- **p. 21 / B.2 LOW-LEVEL POLICY TRAINING DETAILS - extractive PDF cue:** For low-level policy training, we train the policies on ground truth paths constructed by projecting trajectory end-effector points to the camera image.
- **p. 22 / B.2 LOW-LEVEL POLICY TRAINING DETAILS - extractive PDF cue:** This is likely due to 3D-DA's visual attention mechanism which cross attends CLIP language token embeddings with CLIP visual features, therefore detailed language instructions are ...
- **p. 22 / B.2 LOW-LEVEL POLICY TRAINING DETAILS - extractive PDF cue:** The action tags indicate the gripper action.
- **Detected method headings:** B IMPLEMENTATION AND ARCHITECTURE DETAILS (p. 21); B.2 LOW-LEVEL POLICY TRAINING DETAILS (p. 21); Method (p. 26)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | We condition the model on an image and the prompt, except when training on Pixel Point Prediction data (i.e., from Robopoint (Yuan ... | p. 21 (B.1 VLM IMPLEMENTATION DETAILS), p. 21 (B.2 LOW-LEVEL POLICY TRAINING DETAILS) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | For low-level policy training, we train the policies on ground truth paths constructed by projecting trajectory end-effector points to the camera image. | p. 21 (B.2 LOW-LEVEL POLICY TRAINING DETAILS), p. 22 (B.2 LOW-LEVEL POLICY TRAINING DETAILS) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | This is likely due to 3D-DA's visual attention mechanism which cross attends CLIP language token embeddings with CLIP visual features, therefore detailed ... | p. 22 (B.2 LOW-LEVEL POLICY TRAINING DETAILS), p. 22 (B.2 LOW-LEVEL POLICY TRAINING DETAILS) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 22 / B.2 LOW-LEVEL POLICY TRAINING DETAILS - extractive PDF cue:** In simulated experiments in Colosseum, no changes were needed.
- **p. 22 / B.2 LOW-LEVEL POLICY TRAINING DETAILS - extractive PDF cue:** In fact, we saw a performance drop for HAMSTER+3D-DA when removing language for Colosseum tasks and a small drop in performance when using simplified language ...
- **p. 21 / B.1 VLM IMPLEMENTATION DETAILS - extractive PDF cue:** During fine-tuning, the entire model-including the vision encoder-is updated.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 22 (B.2 LOW-LEVEL POLICY TRAINING DETAILS), p. 22 (B.2 LOW-LEVEL POLICY TRAINING DETAILS), p. 21 (B.1 VLM IMPLEMENTATION DETAILS).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | VLM, Path, Prediction, Policy, Input, Instruction, Put, object, bowl, Depth/3D, Observation, response, spicy, food | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | VLM, Path, Prediction, Policy, Input, Instruction, Put, object, bowl, Depth/3D | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | important, note, while, certainly, first, hierarchical, VLA, models, Nasiriany, novel | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | simulated, experiments, Colosseum, changes, needed, fact, performance, drop, HAMSTER, D-DA | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 3 BACKGROUND - extractive PDF cue:** (a) VLM Path Prediction Policy Input Instruction: "Put the object in the bowl." z = Depth/3D Observation VLM response: [(0.25, 0.1, 0), (0.29, 0.3, 0), ...
- **p. 4 / 3 BACKGROUND - extractive PDF cue:** Imitation learning trains a policy πθ(a / s, o, z) from expert demonstrations, where s denotes proprioceptive inputs, o includes perceptual observations (e.g., RGB images, ...
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** These VLA models, which we refer to in this work as monolithic VLA models, rely crucially on large robotics datasets, complete with on-robot observations, e.g., ...
- **p. 7 / 3 BACKGROUND - extractive PDF cue:** 4.2 PATH GUIDED LOW-LEVEL POLICY LEARNING The low-level policy of HAMSTER πθ(a / s, o, z, p) is conditioned on proprioceptive and perceptive observations, (optional) ...
- **p. 5 / 3 BACKGROUND - extractive PDF cue:** The primary advantages of finetuning such a hierarchical VLM that produces intermediate representations as opposed to directly producing actions a with a monolithic model (Kim ...
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** The 2D paths produced by high-level VLMs serve as guidance for a low-level policy that operates on rich 3D and proprioceptive inputs, allowing low-level policies ...
- **p. 4 / 3 BACKGROUND - extractive PDF cue:** 4 HAMSTER: HIERARCHICAL ACTION MODELS FOR ROBOTIC LEARNING In this work, we examine how VLA models can leverage relatively abundant data and demonstrate cross-domain transfer ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | In addition, we reduced the embedding dimension of the transformer to 60 from 120, removed proprioception information from past timesteps, and reduced ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | Provide a sequence of points denoting the trajectory of a robot gripper to achieve the goal. | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | We use tolerance ϵ = 0.05, resulting in paths that are around 2-5 points for each short horizon task. | hardware, batch and throughput |

## Training vs Inference

- **p. 21 / B.1 VLM IMPLEMENTATION DETAILS - extractive PDF cue:** We condition the model on an image and the prompt, except when training on Pixel Point Prediction data (i.e., from Robopoint (Yuan et al., 2024b)) ...
- **p. 21 / B.2 LOW-LEVEL POLICY TRAINING DETAILS - extractive PDF cue:** For low-level policy training, we train the policies on ground truth paths constructed by projecting trajectory end-effector points to the camera image.
- **p. 21 / B.1 VLM IMPLEMENTATION DETAILS - extractive PDF cue:** During fine-tuning, the entire model-including the vision encoder-is updated.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** condition, model, image, prompt, except, when, training, Pixel, Point, Prediction, data, Robopoint, Yuan, where, given, prompts, dataset, low-level, policy, train.
- **Relevant PDF headings:** B IMPLEMENTATION AND ARCHITECTURE DETAILS (p. 21); B.2 LOW-LEVEL POLICY TRAINING DETAILS (p. 21); Method (p. 26).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | Provide a sequence of points denoting the trajectory of a robot gripper to achieve the goal. | p. 21 (B IMPLEMENTATION AND ARCHITECTURE DETAILS), p. 21 (B.1 VLM IMPLEMENTATION DETAILS) |
| Action / skill decoding | Figure 4: Depiction of quantitative real-world policy execution results on a real-world robot, evaluated across different axes of generalization and across both ... | p. 8 (Figure/Table caption), p. 9 (Figure/Table caption) |
| Receding execution / feedback | Table 2: Real world results demonstrate HAMSTER general- izes to better to novel camera views (see Fig.Figure 6). We ran 10 trails ... | p. 9 (Figure/Table caption), p. 26 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 29 / Figure/Table caption - extractive PDF cue:** Table 7: Real world average success rates grouped by task type. G DIFFERENT WAYS OF REPRESENTING 2D PATHS To investigate the effect of the number ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4: Depiction of quantitative real-world policy execution results on a real-world robot, evaluated across different axes of generalization and across both prehensile and non-prehensile ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Table 4: Comparison across visual-language benchmarks, grouped into core VQA tasks (left of the vertical bar) and robustness/probing datasets (right). HAMSTER (ours) uses the same ...
- **p. 22 / B.2 LOW-LEVEL POLICY TRAINING DETAILS - extractive PDF cue:** We remove the language instruction for RVT-2 when conditioning on HAMSTER 2D paths.
- **p. 22 / B.2 LOW-LEVEL POLICY TRAINING DETAILS - extractive PDF cue:** In addition, we reduced the embedding dimension of the transformer to 60 from 120, removed proprioception information from past timesteps, and reduced the number of ...
- **p. 25 / Figure/Table caption - extractive PDF cue:** Figure 13: Human VLM evaluation example images and instructions along with corresponding trajectories from HAMSTER without any finetuning on (RLBench) simulation data, HAMSTER finetuned on ...
- **p. 21 / B.1 VLM IMPLEMENTATION DETAILS - extractive PDF cue:** During fine-tuning, the entire model-including the vision encoder-is updated.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 21 (B.1 VLM IMPLEMENTATION DETAILS), p. 21 (B.2 LOW-LEVEL POLICY TRAINING DETAILS), p. 22 (B.2 LOW-LEVEL POLICY TRAINING DETAILS), p. 22 (B.2 LOW-LEVEL POLICY TRAINING DETAILS), objective p. 22 (B.2 LOW-LEVEL POLICY TRAINING DETAILS), p. 22 (B.2 LOW-LEVEL POLICY TRAINING DETAILS), p. 21 (B.1 VLM IMPLEMENTATION DETAILS), temporal p. 22 (B.2 LOW-LEVEL POLICY TRAINING DETAILS), p. 21 (B IMPLEMENTATION AND ARCHITECTURE DETAILS), p. 21 (B.1 VLM IMPLEMENTATION DETAILS), p. 7 (3 BACKGROUND), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
