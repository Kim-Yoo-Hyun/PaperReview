# Method - Gemini Robotics: Bringing AI into the Physical World

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (64 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2503.20020; PDF retrieval source: https://arxiv.org/abs/2503.20020. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 14 (3. Robot Actions with Gemini Robotics), p. 13 (3. Robot Actions with Gemini Robotics), p. 14 (3. Robot Actions with Gemini Robotics), p. 17 (3.3. Gemini Robotics can closely follow language instructions), p. 16 (3. Robot Actions with Gemini Robotics), p. 22 (4.1. Long-horizon dexterity)): backbone dns Local action decoder computer Robot images & state image Figure 14 / Overview of the architecture, input and output of the Gemini Robotics model.

## Method Body Digest

- **p. 14 / 3. Robot Actions with Gemini Robotics - extractive body cue:** backbone dns Local action decoder computer Robot images & state image Figure 14 / Overview of the architecture, input and output of the Gemini Robotics ...
- **p. 13 / 3. Robot Actions with Gemini Robotics - extractive body cue:** We first study the model after training on a large and diverse dataset consisting of action-labeled robot data as well as other multimodal data.
- **p. 14 / 3. Robot Actions with Gemini Robotics - extractive body cue:** It consists of two components: a VLA backbone hosted in the cloud (Gemini Robotics backbone) and a local action decoder running on the robot's onboard ...
- **p. 17 / 3.3. Gemini Robotics can closely follow language instructions - extractive body cue:** This benchmark consists of 85 tasks in total, of which 20% are within the training distribution, 28% evaluate visual generalization, 28% evaluate instruction generalization, and ...
- **p. 16 / 3. Robot Actions with Gemini Robotics - extractive body cue:** For the more challenging tasks, (e.g., "open pink folder", "insert red block", "wrap the wire around the headphone"), we find that Gemini Robotics is the ...
- **p. 22 / 4.1. Long-horizon dexterity - extractive body cue:** 23), suggesting that in addition to the high-capacity model architecture, the representation, or the physical common sense, learned from diverse robot action datasets in Section ...
- **p. 15 / 3. Robot Actions with Gemini Robotics - extractive body cue:** We compare Gemini Robotics to two state-of-the-art models: The first one is 𝜋0 reimplement, which is our re-implementation of the open-weights state-of-the-art 𝜋0 VLA model ...
- **p. 22 / 4.2. Enhanced reasoning and generalization - extractive body cue:** To this end, we study a fine-tuning process that utilizes a re-labeled version of the robot action dataset in Section 3.1, bringing action prediction closer ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** To this end, we introduce the Gemini Robotics family of embodied AI models, built on top of Gemini 2.0, our most advanced multimodal foundation model.
- **p. 4 / 2.1. Embodied Reasoning Question Answering (ERQA) Benchmark - extractive body cue:** To capture progress in embodied reasoning for VLMs, we introduce ERQA, short for Embodied Reasoning Question Answering, a benchmark that focuses specifically on capabilities likely ...
- **p. 4 / 2.1. Embodied Reasoning Question Answering (ERQA) Benchmark - extractive body cue:** ERQA consists of 400 multiple choice Visual Question Answering (VQA)-style questions across a wide variety of categories, including spatial reasoning, trajectory reasoning, action reasoning, state ...

## Source Evidence Cues

- **p. 14 / 3. Robot Actions with Gemini Robotics - extractive body cue:** backbone dns Local action decoder computer Robot images & state image Figure 14 / Overview of the architecture, input and output of the Gemini Robotics ...
- **p. 13 / 3. Robot Actions with Gemini Robotics - extractive body cue:** We first study the model after training on a large and diverse dataset consisting of action-labeled robot data as well as other multimodal data.
- **p. 14 / 3. Robot Actions with Gemini Robotics - extractive body cue:** It consists of two components: a VLA backbone hosted in the cloud (Gemini Robotics backbone) and a local action decoder running on the robot's onboard ...
- **p. 17 / 3.3. Gemini Robotics can closely follow language instructions - extractive body cue:** This benchmark consists of 85 tasks in total, of which 20% are within the training distribution, 28% evaluate visual generalization, 28% evaluate instruction generalization, and ...
- **p. 16 / 3. Robot Actions with Gemini Robotics - extractive body cue:** For the more challenging tasks, (e.g., "open pink folder", "insert red block", "wrap the wire around the headphone"), we find that Gemini Robotics is the ...
- **p. 22 / 4.1. Long-horizon dexterity - extractive body cue:** 23), suggesting that in addition to the high-capacity model architecture, the representation, or the physical common sense, learned from diverse robot action datasets in Section ...
- **p. 15 / 3. Robot Actions with Gemini Robotics - extractive body cue:** We compare Gemini Robotics to two state-of-the-art models: The first one is 𝜋0 reimplement, which is our re-implementation of the open-weights state-of-the-art 𝜋0 VLA model ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | backbone dns Local action decoder computer Robot images & state image Figure 14 / Overview of the architecture, input and output of ... | p. 14 (3. Robot Actions with Gemini Robotics), p. 13 (3. Robot Actions with Gemini Robotics) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | We first study the model after training on a large and diverse dataset consisting of action-labeled robot data as well as other ... | p. 13 (3. Robot Actions with Gemini Robotics), p. 14 (3. Robot Actions with Gemini Robotics) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | It consists of two components: a VLA backbone hosted in the cloud (Gemini Robotics backbone) and a local action decoder running on ... | p. 14 (3. Robot Actions with Gemini Robotics), p. 17 (3.3. Gemini Robotics can closely follow language instructions) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 22 / 4.2. Enhanced reasoning and generalization - extractive body cue:** To this end, we study a fine-tuning process that utilizes a re-labeled version of the robot action dataset in Section 3.1, bringing action prediction closer ...
- **p. 23 / 4.2. Enhanced reasoning and generalization - extractive body cue:** After fine-tuning on a re-labeled action dataset that bridges action prediction to the embodied reasoning capabilities, the model can generalize to novel situations combining multiple ...
- **p. 14 / 3. Robot Actions with Gemini Robotics - extractive body cue:** The Gemini Robotics backbone is formed by a distilled version of Gemini Robotics-ER and its query-to-response latency has been optimized from seconds to under 160ms.
- **p. 17 / 3.3. Gemini Robotics can closely follow language instructions - extractive body cue:** 21 reports average progress scores.
- **p. 17 / 3.3. Gemini Robotics can closely follow language instructions - extractive body cue:** This metric provides a more continuous measure than the binary task success, and gives us the finer granularity to visualize the policies' progress of each ...
- **p. 19 / 3.3. Gemini Robotics can closely follow language instructions - extractive body cue:** Gemini Robotics: Bringing AI into the Physical World 0.0 0.2 0.4 0.6 0.8 1.0 Progress In-distribution avg.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | backbone, Local, action, decoder, computer, Robot, images, state, image, Figure, Overview, architecture, input, output | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | backbone, Local, action, decoder, computer, Robot, images, state, image, Figure | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | introduce, Gemini, Robotics, family, embodied, models, built, most, advanced, multimodal | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | study, fine-tuning, process, utilizes, re-labeled, version, robot, action, dataset, Section | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 14 / 3. Robot Actions with Gemini Robotics - extractive body cue:** backbone dns Local action decoder computer Robot images & state image Figure 14 / Overview of the architecture, input and output of the Gemini Robotics ...
- **p. 7 / 2.0 Flash. Predicted point labels are not visualized - extractive body cue:** While it is possible to create expert models for each of these tasks individually, fusing them in a single foundation model, such as Gemini 2.0, ...
- **p. 11 / 2.3. Gemini 2.0 Enables Zero and Few-Shot Robot Control - extractive body cue:** Then Gemini 2.0 iteratively takes in images that show the current state of the scene, the robot state, and execution feedback, and outputs code that ...
- **p. 13 / 2.0 Flash - extractive body cue:** Gemini Robotics: Bringing AI into the Physical World Prompt Few shot examples Observations Inference time: Environment Model output Poses to actions code_blocks precision_manufacturing Few Shot ...
- **p. 13 / 2.0 Flash - extractive body cue:** Gemini can receive observations, language instructions and trajectories in the prompt, and generate new language reasoning and trajectories for unseen instances of the tasks. is ...
- **p. 14 / 3. Robot Actions with Gemini Robotics - extractive body cue:** The model ingests a multimodal prompt consisting of a set of images of the current status of the scene and a text instruction of the ...
- **p. 11 / 2.3. Gemini 2.0 Enables Zero and Few-Shot Robot Control - extractive body cue:** Abbreviated example: class RobotApi: def get_grasp_pose(object_name, gripper): ... def detect_object(object_name, gripper): ... def open_gripper(): ... def close_gripper(): ... def move_gripper(gripper, position, orientation): ... termi ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Gemini Robotics: Bringing AI into the Physical World to capture performance across a spectrum of difficulty and objects: from simple grasping (lift ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | With multiple actions in the chunk (Zhao et al., 2023), the effective control frequency is 50Hz. | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | With multiple actions in the chunk (Zhao et al., 2023), the effective control frequency is 50Hz. | hardware, batch and throughput |

## Training vs Inference

- **p. 13 / 3. Robot Actions with Gemini Robotics - extractive body cue:** We first study the model after training on a large and diverse dataset consisting of action-labeled robot data as well as other multimodal data.
- **p. 17 / 3.3. Gemini Robotics can closely follow language instructions - extractive body cue:** This benchmark consists of 85 tasks in total, of which 20% are within the training distribution, 28% evaluate visual generalization, 28% evaluate instruction generalization, and ...
- **p. 19 / 3.3. Gemini Robotics can closely follow language instructions - extractive body cue:** We speculate that these improvements result from the larger and more powerful VLM backbone, including the state-of-the-art vision encoder used in Gemini 2.0, combined with ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** backbone, Local, action, decoder, computer, Robot, images, state, image, Figure, Overview, architecture, input, output, Gemini, Robotics, model, first, study, after.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | Gemini Robotics: Bringing AI into the Physical World Gemini GPT Claude Benchmark | p. 5 (2.1. Embodied Reasoning Question Answering (ERQA) Benchmark), p. 4 (2.1. Embodied Reasoning Question Answering (ERQA) Benchmark) |
| Action / skill decoding | For each image pair, the left image with the point coordinates and the right image without coordinates are given, and the model ... | p. 10 (2.0 Pro Experimental), p. 10 (2.0 Pro Experimental) |
| Receding execution / feedback | (* ImVoxelNet (Rukhovich et al., 2022) performance measured on an easier set of 10 categories). | p. 10 (2.0 Pro Experimental), p. 28 (6. Discussion) |

## Failure and Ablation Link

- **p. 10 / 2.0 Pro Experimental - extractive body cue:** For each image pair, the left image with the point coordinates and the right image without coordinates are given, and the model predicts which of ...
- **p. 28 / 6. Discussion - extractive body cue:** In addition, while our initial results with Gemini Robotics demonstrate promising generalization capabilities, future work will focus on several key areas.
- **p. 28 / 6. Discussion - extractive body cue:** Robust human-level embodied reasoning is critical for robots and other physically grounded agents.
- **p. 29 / 6. Discussion - extractive body cue:** This involves developing techniques to seamlessly integrate abstract reasoning with precise execution, leading to more robust and generalizable performance.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 14 (3. Robot Actions with Gemini Robotics), p. 13 (3. Robot Actions with Gemini Robotics), p. 14 (3. Robot Actions with Gemini Robotics), p. 17 (3.3. Gemini Robotics can closely follow language instructions), p. 16 (3. Robot Actions with Gemini Robotics), p. 22 (4.1. Long-horizon dexterity), objective p. 22 (4.2. Enhanced reasoning and generalization), p. 23 (4.2. Enhanced reasoning and generalization), p. 14 (3. Robot Actions with Gemini Robotics), p. 17 (3.3. Gemini Robotics can closely follow language instructions), p. 17 (3.3. Gemini Robotics can closely follow language instructions), p. 19 (3.3. Gemini Robotics can closely follow language instructions), temporal p. 12 (2.3. Gemini 2.0 Enables Zero and Few-Shot Robot Control), p. 14 (3. Robot Actions with Gemini Robotics), p. 14 (3. Robot Actions with Gemini Robotics), p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)), p. 2 (1. Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (64 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** backbone dns Local action decoder computer Robot images & state image Figure 14 / Overview of the architecture, input and output of the Gemini Robotics model. (p. 14, 3. Robot Actions with Gemini Robotics).
- **Objective/update evidence:** The Gemini Robotics backbone is formed by a distilled version of Gemini Robotics-ER and its query-to-response latency has been optimized from seconds to under 160ms. (p. 14, 3. Robot Actions with Gemini Robotics).
- **Temporal/runtime evidence:** Gemini Robotics: Bringing AI into the Physical World to capture performance across a spectrum of difficulty and objects: from simple grasping (lift a banana) to long horizon multi-step, multi-task manipulation ... (p. 12, 2.3. Gemini 2.0 Enables Zero and Few-Shot Robot Control).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
