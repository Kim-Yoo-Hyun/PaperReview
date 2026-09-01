# Method - PALM: Progress-Aware Policy Learning via Affordance Reasoning for Long-Horizon Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Liu_PALM_Progress-Aware_Policy_Learning_via_Affordance_Reasoning_for_Long-Horizon_Robotic_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_PALM_Progress-Aware_Policy_Learning_via_Affordance_Reasoning_for_Long-Horizon_Robotic_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (3.1. Problem Formulation), p. 3 (3.2. PALM Architecture), p. 5 (3.4. Progress-aware Policy via Inverse Dynamics), p. 4 (3.2. PALM Architecture), p. 5 (3.4. Progress-aware Policy via Inverse Dynamics)): At time t, given observations ot "O, and task specification ⌧"T , and conditioned on the predicted affordance latent, the policy jointly decodes an action at " A alongside a ...

## Method Body Digest

- **p. 3 / 3.1. Problem Formulation - extractive body cue:** At time t, given observations ot "O, and task specification ⌧"T , and conditioned on the predicted affordance latent, the policy jointly decodes an action ...
- **p. 3 / 3.2. PALM Architecture - extractive body cue:** Building on prior inverse-dynamics formulations [18, 38, 112], these queries aggregate current observations with the predicted affordance latent to infer action sequences that align with ...
- **p. 5 / 3.4. Progress-aware Policy via Inverse Dynamics - extractive body cue:** This explicit progress signal reduces ambiguity in long-horizon control: visually similar observations may correspond to different actions depending on stage, and pt disambiguates these cases ...
- **p. 4 / 3.2. PALM Architecture - extractive body cue:** Affordance Queries Action-progress Queries Multi-Modal Encoders Affordance prediction Frozen Trainable Unidirectional Attention Action-progress <Global> <Local> <Spatial> <Dynamic> T S V G
- **p. 5 / 3.4. Progress-aware Policy via Inverse Dynamics - extractive body cue:** We instantiate finv as a denoising diffusion transformer that conditions on the current observation ot, the instruction l, the robot state st, and the predicted ...
- **p. 5 / 3.4. Progress-aware Policy via Inverse Dynamics - extractive body cue:** Training follows the standard diffusion objective: ˜yt⇥t+n-1,td = ‘ ¯↵td yt⇥t+n-1 + ‘ 1 -¯↵td ✏ (9) LDiT = Etd, ✏æ✏-✏✓(˜yt⇥t+n-1,td ∑l, ot, st, ˆFt+n, ...
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** Each task ⌧" T defines an observation-action distribution p (ot, at ∂⌧) and an implicit temporal phase progression.
- **p. 5 / 3.4. Progress-aware Policy via Inverse Dynamics - extractive body cue:** We extend this to predict an n-step action-progress sequence conditioned on the current inputs and a single-step affordance latent.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are as follows: • We introduce PALM, a unified VLA framework that integrates structured affordance reasoning and progress-aware policy generation to enable reliable ...
- **p. 2 / 1. Introduction - extractive body cue:** To address these gaps, we introduce PALM, a novel end-to-end framework for learning scalable, long-horizon manipulation.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** At time t, given observations ot "O, and task specification ⌧"T , and conditioned on the predicted affordance latent, the policy jointly decodes an action ...

## Source Evidence Cues

- **p. 3 / 3.1. Problem Formulation - extractive body cue:** At time t, given observations ot "O, and task specification ⌧"T , and conditioned on the predicted affordance latent, the policy jointly decodes an action ...
- **p. 3 / 3.2. PALM Architecture - extractive body cue:** Building on prior inverse-dynamics formulations [18, 38, 112], these queries aggregate current observations with the predicted affordance latent to infer action sequences that align with ...
- **p. 5 / 3.4. Progress-aware Policy via Inverse Dynamics - extractive body cue:** This explicit progress signal reduces ambiguity in long-horizon control: visually similar observations may correspond to different actions depending on stage, and pt disambiguates these cases ...
- **p. 4 / 3.2. PALM Architecture - extractive body cue:** Affordance Queries Action-progress Queries Multi-Modal Encoders Affordance prediction Frozen Trainable Unidirectional Attention Action-progress <Global> <Local> <Spatial> <Dynamic> T S V G
- **p. 5 / 3.4. Progress-aware Policy via Inverse Dynamics - extractive body cue:** We instantiate finv as a denoising diffusion transformer that conditions on the current observation ot, the instruction l, the robot state st, and the predicted ...
- **Detected method headings:** 3. Method (p. 3); 3.2. PALM Architecture (p. 3); 3.4. Progress-aware Policy via Inverse Dynamics (p. 5)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | At time t, given observations ot "O, and task specification ⌧"T , and conditioned on the predicted affordance latent, the policy jointly ... | p. 3 (3.1. Problem Formulation), p. 3 (3.2. PALM Architecture) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | Building on prior inverse-dynamics formulations [18, 38, 112], these queries aggregate current observations with the predicted affordance latent to infer action sequences ... | p. 3 (3.2. PALM Architecture), p. 5 (3.4. Progress-aware Policy via Inverse Dynamics) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | This explicit progress signal reduces ambiguity in long-horizon control: visually similar observations may correspond to different actions depending on stage, and pt ... | p. 5 (3.4. Progress-aware Policy via Inverse Dynamics), p. 4 (3.2. PALM Architecture) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.4. Progress-aware Policy via Inverse Dynamics - extractive body cue:** Training follows the standard diffusion objective: ˜yt⇥t+n-1,td = ‘ ¯↵td yt⇥t+n-1 + ‘ 1 -¯↵td ✏ (9) LDiT = Etd, ✏æ✏-✏✓(˜yt⇥t+n-1,td ∑l, ot, st, ˆFt+n, ...
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** At time t, given observations ot "O, and task specification ⌧"T , and conditioned on the predicted affordance latent, the policy jointly decodes an action ...
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** Each task ⌧" T defines an observation-action distribution p (ot, at ∂⌧) and an implicit temporal phase progression.
- **p. 4 / 3.2. PALM Architecture - extractive body cue:** Affordance Queries Action-progress Queries Multi-Modal Encoders Affordance prediction Frozen Trainable Unidirectional Attention Action-progress <Global> <Local> <Spatial> <Dynamic> T S V G
- **p. 5 / 3.4. Progress-aware Policy via Inverse Dynamics - extractive body cue:** We extend this to predict an n-step action-progress sequence conditioned on the current inputs and a single-step affordance latent.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 5 (3.4. Progress-aware Policy via Inverse Dynamics).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | PALM, processes, three, synchronized, inputs, language, instruction, image, observation, robot, state, explicit, progress, signal | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | PALM, processes, three, synchronized, inputs, language, instruction, image, observation, robot | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | contributions, follows, introduce, PALM, unified, VLA, framework, integrates, structured, affordance | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | Training, follows, standard, diffusion, objective, LDiT, Etd, where, target, action-progress | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3.2. PALM Architecture - extractive body cue:** PALM processes three synchronized inputs: a language instruction l, an image observation ot, and a robot state st.
- **p. 5 / 3.4. Progress-aware Policy via Inverse Dynamics - extractive body cue:** This explicit progress signal reduces ambiguity in long-horizon control: visually similar observations may correspond to different actions depending on stage, and pt disambiguates these cases ...
- **p. 2 / 1. Introduction - extractive body cue:** Much of this progress is driven by Vision-Language-Action (VLA) models, which leverage pre-trained vision-language backbones to map visual observations and language instructions directly to robot ...
- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are as follows: • We introduce PALM, a unified VLA framework that integrates structured affordance reasoning and progress-aware policy generation to enable reliable ...
- **p. 3 / 3.2. PALM Architecture - extractive body cue:** Building on prior inverse-dynamics formulations [18, 38, 112], these queries aggregate current observations with the predicted affordance latent to infer action sequences that align with ...
- **p. 5 / 3.4. Progress-aware Policy via Inverse Dynamics - extractive body cue:** We append this scalar to the action output so the policy jointly predicts (at, pt) under a shared multimodal context.
- **p. 4 / 3.2. PALM Architecture - extractive body cue:** Affordance Queries Action-progress Queries Multi-Modal Encoders Affordance prediction Frozen Trainable Unidirectional Attention Action-progress <Global> <Local> <Spatial> <Dynamic> T S V G
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Our contributions are as follows: • We introduce PALM, a unified VLA framework that integrates structured affordance reasoning and progress-aware policy generation ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | The action head is a denoising diffusion transformer [96] that conditions on the action-progress queries and the affordance latent to generate a ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | We group the baselines into four types and report the average success rate of the top three checkpoints, computed over 1,000 rollouts ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.2. PALM Architecture - extractive body cue:** Affordance Queries Action-progress Queries Multi-Modal Encoders Affordance prediction Frozen Trainable Unidirectional Attention Action-progress <Global> <Local> <Spatial> <Dynamic> T S V G
- **p. 6 / 4.1. Simulation Experiments - extractive body cue:** We group the baselines into four types and report the average success rate of the top three checkpoints, computed over 1,000 rollouts per task, as ...
- **p. 5 / 4. Experiments - extractive body cue:** For pre-training, we utilize a mixed dataset from the DROID [54] and BridgeData V2 [113] datasets, which together provide large-scale, in-the-wild robotic arm demonstrations to ...
- **p. 8 / 4.3. Real-World Experiments - extractive body cue:** To ensure fairness, all models are fine-tuned on our training dataset, trained for an equal number of iterations, and evaluated with the final checkpoint.
- **p. 4 / 3.2. PALM Architecture - extractive body cue:** Affordance Queries Action-progress Queries Multi-Modal Encoders Affordance prediction Frozen Trainable Unidirectional Attention Action-progress <Global> <Local> <Spatial> <Dynamic> T S V G
- **p. 5 / 3.4. Progress-aware Policy via Inverse Dynamics - extractive body cue:** Training follows the standard diffusion objective: ˜yt⇥t+n-1,td = ‘ ¯↵td yt⇥t+n-1 + ‘ 1 -¯↵td ✏ (9) LDiT = Etd, ✏æ✏-✏✓(˜yt⇥t+n-1,td ∑l, ot, st, ˆFt+n, ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** time, given, observations, task, specification, conditioned, predicted, affordance, latent, policy, jointly, decodes, action, alongside, scalar, encodes, progress, within, current, subtask.
- **Relevant PDF headings:** 3. Method (p. 3); 3.2. PALM Architecture (p. 3); 3.4. Progress-aware Policy via Inverse Dynamics (p. 5).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | For pre-training, we utilize a mixed dataset from the DROID [54] and BridgeData V2 [113] datasets, which together provide large-scale, in-the-wild robotic ... | p. 5 (4. Experiments), p. 8 (4.3. Real-World Experiments) |
| Action / skill decoding | PALM consistently and substantially outperforms all baselines. | p. 6 (4.1. Simulation Experiments), p. 6 (4.1. Simulation Experiments) |
| Receding execution / feedback | Moreover, as shown in Table 2, across all four LIBERO suites, PALM achieves state-of-the-art performance with an average success rate of 94.5%. | p. 6 (4.1. Simulation Experiments), p. 7 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 6 / 4.1. Simulation Experiments - extractive body cue:** Ablation studies of affordance components on CALVIN ABC→D and LIBERO-LONG benchmarks demonstrate the effectiveness of the four components of affordance prediction. increases (e.g., 82.0% for ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Ablation studies of PALM components. Results on the CALVIN ABC→D benchmark demonstrate the effectiveness of each training module under both pre-training and fine-tuning. ...
- **p. 5 / 4. Experiments - extractive body cue:** Our training process consists of a pretraining and a fine-tuning stage.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. PALM Overview. (a) Model Architecture: Given a language instruction l, observation ot, and robot state st, PALM encodes each modality using frozen encoders ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4. Ablation studies on training data composition. Re- sults on the CALVIN ABC→D and LIBERO-LONG benchmarks demonstrate the data efficiency of each source type. ...
- **p. 5 / 4. Experiments - extractive body cue:** For fine-tuning, we select 942 trajectories from robot data and annotate them with affordance data and continuous progress labels using a semi-automated method.
- **p. 6 / 4.2. Ablation Studies - extractive body cue:** How do the components of the fine-grained affordance module affect performance?

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (3.1. Problem Formulation), p. 3 (3.2. PALM Architecture), p. 5 (3.4. Progress-aware Policy via Inverse Dynamics), p. 4 (3.2. PALM Architecture), p. 5 (3.4. Progress-aware Policy via Inverse Dynamics), objective p. 5 (3.4. Progress-aware Policy via Inverse Dynamics), p. 3 (3.1. Problem Formulation), p. 3 (3.1. Problem Formulation), p. 4 (3.2. PALM Architecture), p. 5 (3.4. Progress-aware Policy via Inverse Dynamics), temporal p. 2 (1. Introduction), p. 3 (3.2. PALM Architecture), p. 1 (Front matter), p. 3 (3.1. Problem Formulation), p. 5 (4. Experiments), p. 8 (4.3. Real-World Experiments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
