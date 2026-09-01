# Method - CoA-VLA: Improving Vision-Language-Action Models via Visual-Text Chain-of-Affordance

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (4.1. Definition of Chain-of-Affordance), p. 3 (4. Methodology), p. 5 (4.1. Definition of Chain-of-Affordance), p. 3 (4.1. Definition of Chain-of-Affordance), p. 6 (4.3. Generating Chain-of-Affordance Data), p. 4 (4.1. Definition of Chain-of-Affordance)): This module bridges the gap between abstract language-based reasoning and pixel-level visual context, enabling the policy model to synergistically leverage both modalities for robust, context-aware action generation.

## Method Body Digest

- **p. 5 / 4.1. Definition of Chain-of-Affordance - extractive PDF cue:** This module bridges the gap between abstract language-based reasoning and pixel-level visual context, enabling the policy model to synergistically leverage both modalities for robust, context-aware ...
- **p. 3 / 4. Methodology - extractive PDF cue:** We then discuss how these representations can be integrated into the policy learning process.
- **p. 5 / 4.1. Definition of Chain-of-Affordance - extractive PDF cue:** For textual affordances, we use the last embedding from the VLM models and add an MLP layer to tokenize it.
- **p. 3 / 4.1. Definition of Chain-of-Affordance - extractive PDF cue:** In our approach, we model the robot affordance in the format of natural language as intermediate outputs.
- **p. 6 / 4.3. Generating Chain-of-Affordance Data - extractive PDF cue:** The spatial predictions from RoboPoint and GPT-4o are then combined, after which we cluster these points to form a coherent representation, eliminating any outliers to ...
- **p. 4 / 4.1. Definition of Chain-of-Affordance - extractive PDF cue:** Training on large-scale annotated datasets like Droid [21] enables our model to intelligently select relevant affordances at each time step.
- **p. 4 / 4.1. Definition of Chain-of-Affordance - extractive PDF cue:** For instance, if the proprioceptive state indicates a partially closed gripper and the wristmounted camera detects an object, the model can infer that 9762
- **p. 3 / 4.1. Definition of Chain-of-Affordance - extractive PDF cue:** Our objective is to learn an intermediate language output z : O ↑G ↓Z that maps observations and task descriptions to affordance reasoning in natural ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** In this work, we propose Chain-of-Affordance, namely CoA-VLA, a novel perspective on generalizing model reasoning at test-time, and leverage such generated reasoning to facilitate the ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Our method leverages visual affordance in robot learning, conceptualizing various actions and interactions with objects or the environment that a robot can perform based on ...
- **p. 3 / 4. Methodology - extractive PDF cue:** In Section 4.2, we present two formats for representing the chain of affordances: a text format and an image format.

## Source Evidence Cues

- **p. 5 / 4.1. Definition of Chain-of-Affordance - extractive PDF cue:** This module bridges the gap between abstract language-based reasoning and pixel-level visual context, enabling the policy model to synergistically leverage both modalities for robust, context-aware ...
- **p. 3 / 4. Methodology - extractive PDF cue:** We then discuss how these representations can be integrated into the policy learning process.
- **p. 5 / 4.1. Definition of Chain-of-Affordance - extractive PDF cue:** For textual affordances, we use the last embedding from the VLM models and add an MLP layer to tokenize it.
- **p. 3 / 4.1. Definition of Chain-of-Affordance - extractive PDF cue:** In our approach, we model the robot affordance in the format of natural language as intermediate outputs.
- **p. 6 / 4.3. Generating Chain-of-Affordance Data - extractive PDF cue:** The spatial predictions from RoboPoint and GPT-4o are then combined, after which we cluster these points to form a coherent representation, eliminating any outliers to ...
- **p. 4 / 4.1. Definition of Chain-of-Affordance - extractive PDF cue:** Training on large-scale annotated datasets like Droid [21] enables our model to intelligently select relevant affordances at each time step.
- **p. 4 / 4.1. Definition of Chain-of-Affordance - extractive PDF cue:** For instance, if the proprioceptive state indicates a partially closed gripper and the wristmounted camera detects an object, the model can infer that 9762
- **Detected method headings:** 4. Methodology (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | This module bridges the gap between abstract language-based reasoning and pixel-level visual context, enabling the policy model to synergistically leverage both modalities ... | p. 5 (4.1. Definition of Chain-of-Affordance), p. 3 (4. Methodology) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | We then discuss how these representations can be integrated into the policy learning process. | p. 3 (4. Methodology), p. 5 (4.1. Definition of Chain-of-Affordance) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | For textual affordances, we use the last embedding from the VLM models and add an MLP layer to tokenize it. | p. 5 (4.1. Definition of Chain-of-Affordance), p. 3 (4.1. Definition of Chain-of-Affordance) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 4.1. Definition of Chain-of-Affordance - extractive PDF cue:** Our objective is to learn an intermediate language output z : O ↑G ↓Z that maps observations and task descriptions to affordance reasoning in natural ...
- **p. 4 / 4.1. Definition of Chain-of-Affordance - extractive PDF cue:** Several methods can achieve this, such as gradient-based selection [48].
- **p. 4 / 4.1. Definition of Chain-of-Affordance - extractive PDF cue:** Therefore, we implement dynamic affordance selection, adaptively choosing the necessary affordances at both training and test times to reduce computational cost.
- **p. 5 / 4.1. Definition of Chain-of-Affordance - extractive PDF cue:** We found this strategy to be simple and useful, reducing the model's computational cost without hurting performance.
- **p. 5 / 4.3. Generating Chain-of-Affordance Data - extractive PDF cue:** While the standard approach typically relies on direct human labeling, this method is both costly and labor-intensive.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 3 (4.1. Definition of Chain-of-Affordance), p. 4 (4.1. Definition of Chain-of-Affordance), p. 5 (4.1. Definition of Chain-of-Affordance).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | objective, learn, intermediate, language, output, maps, observations, task, descriptions, affordance, reasoning, natural, module, bridges | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | objective, learn, intermediate, language, output, maps, observations, task, descriptions, affordance | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | Chain-of-Affordance, namely, CoA-VLA, novel, perspective, generalizing, model, reasoning, test-time, leverage | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | objective, learn, intermediate, language, output, maps, observations, task, descriptions, affordance | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 4.1. Definition of Chain-of-Affordance - extractive PDF cue:** Our objective is to learn an intermediate language output z : O ↑G ↓Z that maps observations and task descriptions to affordance reasoning in natural ...
- **p. 5 / 4.1. Definition of Chain-of-Affordance - extractive PDF cue:** This module bridges the gap between abstract language-based reasoning and pixel-level visual context, enabling the policy model to synergistically leverage both modalities for robust, context-aware ...
- **p. 5 / 4.1. Definition of Chain-of-Affordance - extractive PDF cue:** By embedding affordances directly into the visual input, we create an explicit structure that bridges the gap between abstract language and actionable visual context.For movement ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Recent advancements in Vision-Language-Action (VLA) models have shown that training with internet-scale data can empower end-to-end policy learning models to outperform non-VLA models.
- **p. 3 / 4.1. Definition of Chain-of-Affordance - extractive PDF cue:** This intermediate output provides specific guidance for action generation, enabling the generation of low-level actions a →A.
- **p. 4 / 4.1. Definition of Chain-of-Affordance - extractive PDF cue:** This affordance goes beyond visual characteristics, linking observations directly to actions, and is crucial for tasks requiring 6-DoF (degrees of freedom) grasping [18, 34, 43].
- **p. 4 / 4.1. Definition of Chain-of-Affordance - extractive PDF cue:** Proprioception refers to information about the robot's state, including joint angles and other movement data.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Training on large-scale annotated datasets like Droid [21] enables our model to intelligently select relevant affordances at each time step. | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | By employing a dynamic affordance selection mechanism, our method avoids generating redundant affordances at every timestep. object to interact with and where ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 4.1. Definition of Chain-of-Affordance - extractive PDF cue:** Training on large-scale annotated datasets like Droid [21] enables our model to intelligently select relevant affordances at each time step.
- **p. 7 / 5.1. Evaluation on Real Robot - extractive PDF cue:** All models are trained with the same number of iterations, and the last checkpoint is used for evaluation.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** module, bridges, between, abstract, language-based, reasoning, pixel-level, visual, context, enabling, policy, model, synergistically, leverage, modalities, robust, context-aware, action, generation, then.
- **Relevant PDF headings:** 4. Methodology (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | LIBERO is a robot learning benchmark comprising over 130 language-conditioned manipulation tasks. | p. 7 (5.2. Evaluation on Simulation), p. 7 (5. Experiments) |
| Action / skill decoding | Compared to our baseline model, which employs vanilla reasoning, our method achieves a 14.29% increase in accuracy. | p. 7 (5.1. Evaluation on Real Robot), p. 7 (5. Experiments) |
| Receding execution / feedback | Specifically, CoA-VLA achieves an overall success rate of 79.8%, outperforming OpenVLA, the previous best-performing method, by a margin of 3.3%. | p. 7 (5.2. Evaluation on Simulation), p. 7 (5.2. Evaluation on Simulation) |

## Failure and Ablation Link

- **p. 7 / 5.1. Evaluation on Real Robot - extractive PDF cue:** Detailed descriptions of each task and the experimental setup, and our ablation experiments are provided in the Appendix.
- **p. 7 / 5.1. Evaluation on Real Robot - extractive PDF cue:** We use the Droid dataset [21] as an external data source, filtering out samples without language annotations, leaving 39K trajectories.
- **p. 8 / 5.3. More Experiments - extractive PDF cue:** Our method successfully identifies open areas on the plate, allowing it to accurately position the bread without interference, thereby enabling CoA-VLA to complete all three ...
- **p. 8 / 5.3. More Experiments - extractive PDF cue:** Our approach successfully completed all three scenarios, demonstrating robust collision avoidance and spatial adaptability.
- **p. 8 / 5.3. More Experiments - extractive PDF cue:** Collision avoidance is essential for safe and effective physical interactions, as improper maneuvers can lead to significant damage or even catastrophic outcomes.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (4.1. Definition of Chain-of-Affordance), p. 3 (4. Methodology), p. 5 (4.1. Definition of Chain-of-Affordance), p. 3 (4.1. Definition of Chain-of-Affordance), p. 6 (4.3. Generating Chain-of-Affordance Data), p. 4 (4.1. Definition of Chain-of-Affordance), objective p. 3 (4.1. Definition of Chain-of-Affordance), p. 4 (4.1. Definition of Chain-of-Affordance), p. 4 (4.1. Definition of Chain-of-Affordance), p. 5 (4.1. Definition of Chain-of-Affordance), p. 5 (4.3. Generating Chain-of-Affordance Data), temporal p. 4 (4.1. Definition of Chain-of-Affordance), p. 4 (4.1. Definition of Chain-of-Affordance), p. 3 (4.1. Definition of Chain-of-Affordance), p. 3 (4. Methodology), p. 5 (4.1. Definition of Chain-of-Affordance), p. 5 (4.1. Definition of Chain-of-Affordance).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
