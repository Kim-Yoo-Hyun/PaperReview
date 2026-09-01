# Method - PointVLA: Injecting the 3D World into Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2503.07511; PDF retrieval source: https://arxiv.org/pdf/2503.07511. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3.2. Injecting Point Cloud into VLA), p. 3 (3. Methodology), p. 4 (3.2. Injecting Point Cloud into VLA), p. 5 (3.3. Which Blocks to Inject Point Cloud? A Skip), p. 3 (3. Methodology), p. 5 (3.2. Injecting Point Cloud into VLA)): For selected blocks in the action expert, we first apply an MLP layer as an adapter for each block, followed by an addition operation to inject the point cloud embedding ...

## Method Body Digest

- **p. 4 / 3.2. Injecting Point Cloud into VLA - extractive body cue:** For selected blocks in the action expert, we first apply an MLP layer as an adapter for each block, followed by an addition operation to ...
- **p. 3 / 3. Methodology - extractive body cue:** Subsequently, an 'action expert' module translates the VLM's state information into robot actions.
- **p. 4 / 3.2. Injecting Point Cloud into VLA - extractive body cue:** The vanilla action expert remains frozen, while the new point cloud representation is integrated into the action expert through a modular network.
- **p. 5 / 3.3. Which Blocks to Inject Point Cloud? A Skip - extractive body cue:** Our experiment reveals that the first 11 blocks are crucial for the model-skipping any of them leads to a significant drop in performance.
- **p. 3 / 3. Methodology - extractive body cue:** This training enables effective alignment of image and text representations within a shared embedding space.
- **p. 5 / 3.2. Injecting Point Cloud into VLA - extractive body cue:** Skip block analysis for action expert in VLA model.
- **p. 4 / 3.2. Injecting Point Cloud into VLA - extractive body cue:** First, the computational cost would be prohibitively high due to the required conditioning blocks.
- **p. 4 / 3.2. Injecting Point Cloud into VLA - extractive body cue:** Given that we aimed to minimize interference from the limited 3D visual knowledge on the pre-trained action embedding derived from 2D visual input, we conducted ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we introduce PointVLA, a novel framework that integrates point clouds into pre-trained visionlanguage-action models.
- **p. 2 / 1. Introduction - extractive body cue:** To address this, we propose a 3D modular block that injects point cloud information directly into the action expert.
- **p. 4 / 3.2. Injecting Point Cloud into VLA - extractive body cue:** To circumvent these issues, we propose a paradigm that treats 3D point cloud data as a complementary conditioning signal rather than a primary input modality.

## Source Evidence Cues

- **p. 4 / 3.2. Injecting Point Cloud into VLA - extractive body cue:** For selected blocks in the action expert, we first apply an MLP layer as an adapter for each block, followed by an addition operation to ...
- **p. 3 / 3. Methodology - extractive body cue:** Subsequently, an 'action expert' module translates the VLM's state information into robot actions.
- **p. 4 / 3.2. Injecting Point Cloud into VLA - extractive body cue:** The vanilla action expert remains frozen, while the new point cloud representation is integrated into the action expert through a modular network.
- **p. 5 / 3.3. Which Blocks to Inject Point Cloud? A Skip - extractive body cue:** Our experiment reveals that the first 11 blocks are crucial for the model-skipping any of them leads to a significant drop in performance.
- **p. 3 / 3. Methodology - extractive body cue:** This training enables effective alignment of image and text representations within a shared embedding space.
- **p. 5 / 3.2. Injecting Point Cloud into VLA - extractive body cue:** Skip block analysis for action expert in VLA model.
- **Detected method headings:** 3. Methodology (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | For selected blocks in the action expert, we first apply an MLP layer as an adapter for each block, followed by an ... | p. 4 (3.2. Injecting Point Cloud into VLA), p. 3 (3. Methodology) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | Subsequently, an 'action expert' module translates the VLM's state information into robot actions. | p. 3 (3. Methodology), p. 4 (3.2. Injecting Point Cloud into VLA) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | The vanilla action expert remains frozen, while the new point cloud representation is integrated into the action expert through a modular network. | p. 4 (3.2. Injecting Point Cloud into VLA), p. 5 (3.3. Which Blocks to Inject Point Cloud? A Skip) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.2. Injecting Point Cloud into VLA - extractive body cue:** First, the computational cost would be prohibitively high due to the required conditioning blocks.
- **p. 4 / 3.2. Injecting Point Cloud into VLA - extractive body cue:** Given that we aimed to minimize interference from the limited 3D visual knowledge on the pre-trained action embedding derived from 2D visual input, we conducted ...
- **p. 5 / 3.3. Which Blocks to Inject Point Cloud? A Skip - extractive body cue:** Ultimately, we only train five additional injection blocks, which are lightweight and fast during inference, making our approach highly cost-efficient.
- **p. 5 / 3.3. Which Blocks to Inject Point Cloud? A Skip - extractive body cue:** Block Analysis As mentioned earlier, injecting the point cloud into every block of the action expert is not ideal, as it increases computational cost and ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 4 (3.2. Injecting Point Cloud into VLA).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | PointVLA, Framework, Vision-Language, Model, Action, Expert, Point, Cloud, Injector, Robot, Block_12, Block_13, Block_16, Block_1 | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | PointVLA, Framework, Vision-Language, Model, Action, Expert, Point, Cloud, Injector, Robot | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | introduce, PointVLA, novel, framework, integrates, point, clouds, pre-trained, visionlanguage-action, models | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | First, computational, cost, would, prohibitively, high, required, conditioning, blocks, Given | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.2. Injecting Point Cloud into VLA - extractive body cue:** PointVLA Framework Vision-Language Model Action Expert Point Cloud Injector Robot Action Block_12 Block_13 Block_16 Block_1 Injection Block_1 Injection Block_2 Injection Block_5 Zero Linear Adapter Zero ...
- **p. 3 / 3. Methodology - extractive body cue:** The VLM acts as the model's 'brain,' processing instructions and current visual input to understand the task state.
- **p. 4 / 3.2. Injecting Point Cloud into VLA - extractive body cue:** Left: The 2D image observation and instruction are processed by the vision-language model.
- **p. 3 / 3. Methodology - extractive body cue:** Subsequently, an 'action expert' module translates the VLM's state information into robot actions.
- **p. 5 / 3.3. Which Blocks to Inject Point Cloud? A Skip - extractive body cue:** We freeze all modules in the vanilla action expert except for the final layers, which are adjusted to fit the embodiment's output.
- **p. 2 / 1. Introduction - extractive body cue:** To address this, we propose a 3D modular block that injects point cloud information directly into the action expert.
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we introduce PointVLA, a novel framework that integrates point clouds into pre-trained visionlanguage-action models.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | PointVLA Framework Vision-Language Model Action Expert Point Cloud Injector Robot Action Block_12 Block_13 Block_16 Block_1 Injection Block_1 Injection Block_2 Injection Block_5 Zero ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | The evaluation follows the same metrics-average score, a standard measure for long-horizon tasks [4, 31, 46]-by dividing the task into multiple steps ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 3. Methodology - extractive body cue:** This training enables effective alignment of image and text representations within a shared embedding space.
- **p. 5 / 4.1. Implementation Details - extractive body cue:** We use the same training hyperparameters as the stage 2 training in DexVLA, and use the 5

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** selected, blocks, action, expert, first, apply, MLP, layer, adapter, block, followed, addition, operation, inject, point, cloud, embedding, model, Subsequently, module.
- **Relevant PDF headings:** 3. Methodology (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | Following the training setup in RoboTwin, the policy was trained using three random seeds (0, 1, 2) without cherry picking for each ... | p. 8 (4.6. Experimental Results on Simulation Bench), p. 5 (4. Experiment) |
| Action / skill decoding | Figure 6. Experimental results on few-shot multi-tasking on bimanual AgileX. last checkpoint for evaluation to avoid cherry picking. We set chunk size ... | p. 6 (Figure/Table caption), p. 6 (4.1. Implementation Details) |
| Receding execution / feedback | Notably, across all tasks and diverse settings, our proposed PointVLA achieves the highest average success rate, regardless of whether it is trained ... | p. 8 (4.6. Experimental Results on Simulation Bench), p. 8 (4.6. Experimental Results on Simulation Bench) |

## Failure and Ablation Link

- **p. 6 / 4.1. Implementation Details - extractive body cue:** Note that since PointVLA is built on top of DexVLA, the DexVLA can be viewed as an ablation of our proposed PointVLA without the incorporation ...
- **p. 6 / 4.1. Implementation Details - extractive body cue:** In our experiments, we compared with many state-of-the-art model, including the Diffusion Policy (DP) [9], 3D Diffusion Policy (DP3) [51], ScaleDP-1B [57], a variant of ...
- **p. 8 / 4.6. Experimental Results on Simulation Bench - extractive body cue:** Following the training setup in RoboTwin, the policy was trained using three random seeds (0, 1, 2) without cherry picking for each experiment.
- **p. 5 / 4.1. Implementation Details - extractive body cue:** For both experiments, we use stage 1 pre-trained weights from DexVLA [46] and fine-tune for our model.
- **p. 7 / 4.4. Real-vs-Photo Discrimination - extractive body cue:** Specifically, we replace the real object with a picture of the object.
- **p. 7 / 4.2. Few-Shot Multi-Tasking - extractive body cue:** We replace the real laundry detergent with its photo displayed on a screen placed on the conveyor belt.
- **p. 7 / 4.2. Few-Shot Multi-Tasking - extractive body cue:** Notably, the Diffusion Policy fails in most cases, likely because the sample size for each task is too small, causing the action representation space to ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3.2. Injecting Point Cloud into VLA), p. 3 (3. Methodology), p. 4 (3.2. Injecting Point Cloud into VLA), p. 5 (3.3. Which Blocks to Inject Point Cloud? A Skip), p. 3 (3. Methodology), p. 5 (3.2. Injecting Point Cloud into VLA), objective p. 4 (3.2. Injecting Point Cloud into VLA), p. 4 (3.2. Injecting Point Cloud into VLA), p. 5 (3.3. Which Blocks to Inject Point Cloud? A Skip), p. 5 (3.3. Which Blocks to Inject Point Cloud? A Skip), temporal p. 4 (3.2. Injecting Point Cloud into VLA), p. 5 (3.3. Which Blocks to Inject Point Cloud? A Skip), p. 3 (3. Methodology), p. 3 (3.2. Injecting Point Cloud into VLA), p. 4 (3.2. Injecting Point Cloud into VLA), p. 5 (4. Experiment).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
