# Method - D3D-VLP: Dynamic 3D Vision-Language-Planning Model for Embodied Grounding and Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Wang_D3D-VLP_Dynamic_3D_Vision-Language-Planning_Model_for_Embodied_Grounding_and_Navigation_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_D3D-VLP_Dynamic_3D_Vision-Language-Planning_Model_for_Embodied_Grounding_and_Navigation_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 2 (3. Our Method), p. 3 (3. Our Method), p. 8 (1. Synergistic Learning (SLFS) and Training Data), p. 7 (4.3. Long-Horizon Grounding and Planning), p. 7 (4.3. Long-Horizon Grounding and Planning), p. 8 (1. Synergistic Learning (SLFS) and Training Data)): At each timestep, we use the encoder of Dynam3D [57] to process streaming posed RGB-D images to update a dynamic Multi-level 3D 32464

## Method Body Digest

- **p. 2 / 3. Our Method - extractive PDF cue:** At each timestep, we use the encoder of Dynam3D [57] to process streaming posed RGB-D images to update a dynamic Multi-level 3D 32464
- **p. 3 / 3. Our Method - extractive PDF cue:** RGB images Depth images Dynam3D Encoder Waypoint Predictor D3D-VLP Model "Set up a nightlight in the bathroom." Instruction Historical plans, grounded targets, action, answer CoT ...
- **p. 8 / 1. Synergistic Learning (SLFS) and Training Data - extractive PDF cue:** Without it, the agent degenerates from a planning and stateful controller into a reactive and memory-less one, and the task-level accuracy t-ACC collapses from 9.3% ...
- **p. 7 / 4.3. Long-Horizon Grounding and Planning - extractive PDF cue:** The SG3D benchmark is specifically designed to evaluate planning, grounding, and memory capabilities in longhorizon stateful tasks of an agent.
- **p. 7 / 4.3. Long-Horizon Grounding and Planning - extractive PDF cue:** For example, the Dynam3D-VisTA modular baseline, which pairs the strong 3D perception and navigation baseline model [57] with a 3D grounding model [82] achieves a ...
- **p. 8 / 1. Synergistic Learning (SLFS) and Training Data - extractive PDF cue:** The ablation also reveals two complementary roles of SLFS: 1) SLFS enables the model to exploit massive partially annotated data (w/o Tplan, types 4-6) to ...
- **p. 1 / 1. Introduction - extractive PDF cue:** The end-to-end models directly map instructions to navigation actions, and modular systems assemble multiple specialized components.
- **p. 1 / 1. Introduction - extractive PDF cue:** On the one hand, most end-to-end embodied navigation models [12, 57, 60, 65, 66] directly output navigation actions, which bypasses explicit 3D grounding and reasoning ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** In summary, our main contributions are: • We propose D3D-VLP, a 3D vision-language-planning model that unifies multi-step planning, grounding, and navigation in unseen and dynamic ...
- **p. 2 / 1. Introduction - extractive PDF cue:** To address these limitations, we propose the Dynamic 3D Vision-Language-Planning Model (D3D-VLP).
- **p. 8 / 1. Synergistic Learning (SLFS) and Training Data - extractive PDF cue:** The ablation also reveals two complementary roles of SLFS: 1) SLFS enables the model to exploit massive partially annotated data (w/o Tplan, types 4-6) to ...

## Source Evidence Cues

- **p. 2 / 3. Our Method - extractive PDF cue:** At each timestep, we use the encoder of Dynam3D [57] to process streaming posed RGB-D images to update a dynamic Multi-level 3D 32464
- **p. 3 / 3. Our Method - extractive PDF cue:** RGB images Depth images Dynam3D Encoder Waypoint Predictor D3D-VLP Model "Set up a nightlight in the bathroom." Instruction Historical plans, grounded targets, action, answer CoT ...
- **p. 8 / 1. Synergistic Learning (SLFS) and Training Data - extractive PDF cue:** Without it, the agent degenerates from a planning and stateful controller into a reactive and memory-less one, and the task-level accuracy t-ACC collapses from 9.3% ...
- **p. 7 / 4.3. Long-Horizon Grounding and Planning - extractive PDF cue:** The SG3D benchmark is specifically designed to evaluate planning, grounding, and memory capabilities in longhorizon stateful tasks of an agent.
- **p. 7 / 4.3. Long-Horizon Grounding and Planning - extractive PDF cue:** For example, the Dynam3D-VisTA modular baseline, which pairs the strong 3D perception and navigation baseline model [57] with a 3D grounding model [82] achieves a ...
- **p. 8 / 1. Synergistic Learning (SLFS) and Training Data - extractive PDF cue:** The ablation also reveals two complementary roles of SLFS: 1) SLFS enables the model to exploit massive partially annotated data (w/o Tplan, types 4-6) to ...
- **Detected method headings:** 3. Our Method (p. 2); 4.2. Comparison with State-of-the-Art Methods (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | At each timestep, we use the encoder of Dynam3D [57] to process streaming posed RGB-D images to update a dynamic Multi-level 3D ... | p. 2 (3. Our Method), p. 3 (3. Our Method) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | RGB images Depth images Dynam3D Encoder Waypoint Predictor D3D-VLP Model "Set up a nightlight in the bathroom." Instruction Historical plans, grounded targets, ... | p. 3 (3. Our Method), p. 8 (1. Synergistic Learning (SLFS) and Training Data) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | Without it, the agent degenerates from a planning and stateful controller into a reactive and memory-less one, and the task-level accuracy t-ACC ... | p. 8 (1. Synergistic Learning (SLFS) and Training Data), p. 7 (4.3. Long-Horizon Grounding and Planning) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / 3. Our Method - extractive PDF cue:** At each timestep, we use the encoder of Dynam3D [57] to process streaming posed RGB-D images to update a dynamic Multi-level 3D 32464
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 2 (3. Our Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | RGB, images, Depth, Dynam3D, Encoder, Waypoint, Predictor, D3D-VLP, Model, Set, nightlight, bathroom, Instruction, Historical | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | RGB, images, Depth, Dynam3D, Encoder, Waypoint, Predictor, D3D-VLP, Model, Set | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | summary, main, contributions, D3D-VLP, vision-language-planning, model, unifies, multi-step, planning, grounding | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | timestep, encoder, Dynam3D, process, streaming, posed, RGB-D, images, update, dynamic | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3. Our Method - extractive PDF cue:** RGB images Depth images Dynam3D Encoder Waypoint Predictor D3D-VLP Model "Set up a nightlight in the bathroom." Instruction Historical plans, grounded targets, action, answer CoT ...
- **p. 1 / 1. Introduction - extractive PDF cue:** The end-to-end models directly map instructions to navigation actions, and modular systems assemble multiple specialized components.
- **p. 1 / 1. Introduction - extractive PDF cue:** On the one hand, most end-to-end embodied navigation models [12, 57, 60, 65, 66] directly output navigation actions, which bypasses explicit 3D grounding and reasoning ...
- **p. 2 / 1. Introduction - extractive PDF cue:** By using a masked autoregressive loss, the gradient from an available annotation such as a correct navigation action back-propagates through the shared 3D-VLM to implicitly ...
- **p. 2 / 3. Our Method - extractive PDF cue:** At each timestep, we use the encoder of Dynam3D [57] to process streaming posed RGB-D images to update a dynamic Multi-level 3D 32464
- **p. 7 / 4.3. Long-Horizon Grounding and Planning - extractive PDF cue:** The SG3D benchmark is specifically designed to evaluate planning, grounding, and memory capabilities in longhorizon stateful tasks of an agent.
- **p. 7 / 4.3. Long-Horizon Grounding and Planning - extractive PDF cue:** By feeding historical plans, grounded targets, and trajectories back into the VLM, our D3D-VLP maintains state, resolves temporal ambiguities, and possesses replanning capabilities that are ...
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | Instead of discarding the generated sequence St, we parse its components to update the historical CoT Memory for the next timestep: Ct ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | At each timestep, we use the encoder of Dynam3D [57] to process streaming posed RGB-D images to update a dynamic Multi-level 3D ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | Instead of discarding the generated sequence St, we parse its components to update the historical CoT Memory for the next timestep: Ct ... | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** timestep, encoder, Dynam3D, process, streaming, posed, RGB-D, images, update, dynamic, Multi-level, RGB, Depth, Waypoint, Predictor, D3D-VLP, Model, Set, nightlight, bathroom.
- **Relevant PDF headings:** 3. Our Method (p. 2); 4.2. Comparison with State-of-the-Art Methods (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | Grounding & Grasp Place Task OK-Robot [38] 11/32 4/16 3/16 0/10 DynaMem [37] 13/32 6/16 4/16 0/10 Dynam3D+OWLv2 [42, 57] 21/32 9/16 ... | p. 8 (4.5. Real-World Mobile Manipulation Experiments), p. 6 (4.1. Experimental Setup) |
| Global / local decision | Figure 1. Model Architecture Comparison. The end-to-end models directly map instructions to navigation actions, and modu- lar systems assemble multiple specialized components. ... | p. 1 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Motion execution / recovery | Future work could incorporate Reinforcement Learning to further enhance this framework. | p. 8 (5. Conclusion) |

## Failure and Ablation Link

- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 4. Ablation study on components and training data. Settings Training data R2R-CE Nav. SG3D Grounding OSR SR SPL
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Model Architecture Comparison. The end-to-end models directly map instructions to navigation actions, and modu- lar systems assemble multiple specialized components. Our D3D- VLP ...
- **p. 8 / 5. Conclusion - extractive PDF cue:** Future work could incorporate Reinforcement Learning to further enhance this framework.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 2 (3. Our Method), p. 3 (3. Our Method), p. 8 (1. Synergistic Learning (SLFS) and Training Data), p. 7 (4.3. Long-Horizon Grounding and Planning), p. 7 (4.3. Long-Horizon Grounding and Planning), p. 8 (1. Synergistic Learning (SLFS) and Training Data), objective p. 2 (3. Our Method), temporal p. 5 (2. Walk to the cabinet next to the bathtub), p. 2 (3. Our Method), p. 4 (2. Walk to the cabinet next to the bathtub), p. 2 (1. Introduction), p. 3 (3. Our Method), p. 6 (4.1. Experimental Setup).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
