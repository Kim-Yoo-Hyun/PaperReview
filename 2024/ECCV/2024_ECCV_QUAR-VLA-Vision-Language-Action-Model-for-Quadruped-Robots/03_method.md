# Method - QUAR-VLA: Vision-Language-Action Model for Quadruped Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/808_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/00808.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 8 (3 Method), p. 9 (3 Method), p. 5 (3 Method), p. 9 (3 Method), p. 5 (3 Method), p. 6 (3 Method)): Notably, QUART model takes a single image s and a natural language instruction w as input, which are first converted into corresponding tokens t through a tokenizer τ(t/s, w) and ...

## Method Body Digest

- **p. 8 / 3 Method - extractive PDF cue:** Notably, QUART model takes a single image s and a natural language instruction w as input, which are first converted into corresponding tokens t through ...
- **p. 9 / 3 Method - extractive PDF cue:** We use a standard categorical cross-entropy objective and causal masking that was utilized in prior Transformer-based controllers [18,29].
- **p. 5 / 3 Method - extractive PDF cue:** The policy is a mapping from images and instructions to actions, and can be written as µ : S × W →A, where the action ...
- **p. 9 / 3 Method - extractive PDF cue:** To directly convert models' output to valid robot actions for downstream control, we need detokenize the discrete action token ad into continuous representation ac (except ...
- **p. 5 / 3 Method - extractive PDF cue:** 3.1 Problem Setup The objective of QUAR-VLA is to construct a vision-language-action model learned from large-scale demonstration data and generate actions for closed-loop robot control.
- **p. 6 / 3 Method - extractive PDF cue:** The command output is sent to the low-level command tracking controller (pre-trained command-conditioned policy in [23]) to generate the actual joint action of the robot.
- **p. 8 / 3 Method - extractive PDF cue:** The policy QUART could be shown as follow: \begin {a li g ned} &\operat orname {QUART}(a_d/s, w) = p(a_d/t) \tau (t/s, w)\\ \end {aligned} (2) ...
- **p. 7 / 3 Method - extractive PDF cue:** A* algorithm seeks the most cost-effective path, while the D* algorithm adapts to changes in real time.

## Design Rationale

- **p. 3 / 1 Introduction - extractive PDF cue:** Our extensive evaluation shows that our approach leads to performant robotic policies and enables QUART to obtain a range of generalization capabilities.
- **p. 2 / 1 Introduction - extractive PDF cue:** To enable quadruped robots to autonomously navigate and manipulate various tasks, in this paper, we propose a new paradigm: Vision-Language-Action tasks for QUAdruped Robots (QUAR-VLA), ...
- **p. 4 / 1 Introduction - extractive PDF cue:** 2) We present a large-scale multi-task dataset, QUARD, and a Vision-Language-Action model, QUART to solve the QUAR-VLA tasks.

## Source Evidence Cues

- **p. 8 / 3 Method - extractive PDF cue:** Notably, QUART model takes a single image s and a natural language instruction w as input, which are first converted into corresponding tokens t through ...
- **p. 9 / 3 Method - extractive PDF cue:** We use a standard categorical cross-entropy objective and causal masking that was utilized in prior Transformer-based controllers [18,29].
- **p. 5 / 3 Method - extractive PDF cue:** The policy is a mapping from images and instructions to actions, and can be written as µ : S × W →A, where the action ...
- **p. 9 / 3 Method - extractive PDF cue:** To directly convert models' output to valid robot actions for downstream control, we need detokenize the discrete action token ad into continuous representation ac (except ...
- **p. 5 / 3 Method - extractive PDF cue:** 3.1 Problem Setup The objective of QUAR-VLA is to construct a vision-language-action model learned from large-scale demonstration data and generate actions for closed-loop robot control.
- **p. 6 / 3 Method - extractive PDF cue:** The command output is sent to the low-level command tracking controller (pre-trained command-conditioned policy in [23]) to generate the actual joint action of the robot.
- **p. 8 / 3 Method - extractive PDF cue:** The policy QUART could be shown as follow: \begin {a li g ned} &\operat orname {QUART}(a_d/s, w) = p(a_d/t) \tau (t/s, w)\\ \end {aligned} (2) ...
- **Detected method headings:** 3 Method (p. 5)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Command / terrain state | body state와 terrain/task context를 표현한다 | proprioception, terrain/perception, velocity command | history encoder, reference, terrain latent 또는 behavior mode를 구성 | locomotion context | Notably, QUART model takes a single image s and a natural language instruction w as input, which are first converted into corresponding ... | p. 8 (3 Method), p. 9 (3 Method) |
| Whole-body policy / controller | context에서 joint target 또는 torque를 만든다 | context, body state, contact | RL policy, reference tracking, inverse dynamics 또는 whole-body control을 적용 | joint action/torque | We use a standard categorical cross-entropy objective and causal masking that was utilized in prior Transformer-based controllers [18,29]. | p. 9 (3 Method), p. 5 (3 Method) |
| Adaptation / recovery | disturbance와 contact mismatch에 대응한다 | new observation/history와 failure signal | latent adaptation, foothold change, recovery 또는 replan을 수행 | updated command | The policy is a mapping from images and instructions to actions, and can be written as µ : S × W →A, ... | p. 5 (3 Method), p. 9 (3 Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 9 / 3 Method - extractive PDF cue:** We use a standard categorical cross-entropy objective and causal masking that was utilized in prior Transformer-based controllers [18,29].
- **p. 5 / 3 Method - extractive PDF cue:** 3.1 Problem Setup The objective of QUAR-VLA is to construct a vision-language-action model learned from large-scale demonstration data and generate actions for closed-loop robot control.
- **p. 7 / 3 Method - extractive PDF cue:** A* algorithm seeks the most cost-effective path, while the D* algorithm adapts to changes in real time.
- **p. 7 / 3 Method - extractive PDF cue:** To maintain consistency between simulation and reality, we've established constraints for data collection.
- **p. 9 / 3 Method - extractive PDF cue:** To directly convert models' output to valid robot actions for downstream control, we need detokenize the discrete action token ad into continuous representation ac (except ...
- **Formal bridge:** body/proprioceptive/terrain state -> joint action/torque/footstep -> return, tracking or stability objective -> progress, balance and terrain robustness.
- **Equation/algorithm anchors:** p. 5 (3 Method), p. 7 (3 Method), p. 9 (3 Method), p. 9 (3 Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | policy, QUART, could, follow, begin, operat, orname, a_d/s, a_d/t, aligned, where, input, images, language | proprioception, terrain/perception observation과 velocity command | body cue; exact tensor/frame verify |
| State/latent | policy, QUART, could, follow, begin, operat, orname, a_d/s, a_d/t, aligned | body/contact state, foothold 또는 behavior mode | body cue; notation verify |
| Action/output | extensive, evaluation, leads, performant, robotic, policies, enables, QUART, obtain, range | joint target, torque, footstep 또는 locomotion action | body cue; unit/decoder verify |
| Objective/constraint | standard, categorical, cross-entropy, objective, causal, masking, utilized, prior, Transformer-based, controllers | return, tracking or stability objective | equation anchor required |

## Observation–State–Action Interface

- **p. 8 / 3 Method - extractive PDF cue:** The policy QUART could be shown as follow: \begin {a li g ned} &\operat orname {QUART}(a_d/s, w) = p(a_d/t) \tau (t/s, w)\\ \end {aligned} (2) ...
- **p. 9 / 3 Method - extractive PDF cue:** Observation I Instruction W VLA De-Tokenize Deploy ··· Action ad Velocity Gait B-Pose Terminate vx vy wz θ1 θ2 θ3 f hz sy hz f ...
- **p. 9 / 3 Method - extractive PDF cue:** It receives visual information as observation, and outputs an action representing the actual action taken by the robot based on text-form instructions, and de-tokenizes it ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Ding et al. "Trot in place, with the front right leg move twice as fast as other legs" (a) QUAR-VA (b) QUAR-LA (c) QUAR-VLA Language ...
- **p. 5 / 3 Method - extractive PDF cue:** The policy is a mapping from images and instructions to actions, and can be written as µ : S × W →A, where the action ...
- **p. 8 / 3 Method - extractive PDF cue:** Notably, QUART model takes a single image s and a natural language instruction w as input, which are first converted into corresponding tokens t through ...
- **p. 2 / 1 Introduction - extractive PDF cue:** To enable quadruped robots to autonomously navigate and manipulate various tasks, in this paper, we propose a new paradigm: Vision-Language-Action tasks for QUAdruped Robots (QUAR-VLA), ...
- **Normalized interface:** observation=proprioception, terrain/perception observation과 velocity command; state=body/contact state, foothold 또는 behavior mode; output/action=joint target, torque, footstep 또는 locomotion action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | gait/skill episode horizon과 short-horizon body control이 계층적으로 분리된다. | \l eft [v _x, v_ y, \o meg a _z, \ th e ta _1, \theta _2, \theta _3, f, h_z, \phi ... | episode/sequence/action-chunk boundary |
| Rate / latency | high-level command, policy rate와 low-level torque rate를 구분; exact rate 확인 필요. | The "Episode" signifies the number of experiments conducted for each task, which also corresponds to the number of trajectories. | Hz/fps, inference time and control rate |
| Memory | proprioceptive history, terrain latent와 contact/body state. | not recovered | window and reset |
| Compute | policy inference, adaptation encoder와 whole-body/control solve가 latency를 결정한다. | QUART can generate a complete action sequence at a processing rate of 2Hz in actual scenarios, and hand it over to the ... | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 3 Method - extractive PDF cue:** The command output is sent to the low-level command tracking controller (pre-trained command-conditioned policy in [23]) to generate the actual joint action of the robot.
- **p. 10 / 4 Experiments - extractive PDF cue:** And we use learning rate 2e-5 and batch size 256 to fine-tune the model for 100K gradient steps.
- **p. 10 / 4 Experiments - extractive PDF cue:** 4.1 Implementation Details Training Details.
- **p. 9 / 3 Method - extractive PDF cue:** For QUART, the inference time could get 2Hz.
- **p. 9 / 3 Method - extractive PDF cue:** In contrast to many applications of large models, such as natural language or image generation, one of the unique requirements for a model that needs ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Notably, QUART, model, takes, single, image, natural, language, instruction, input, first, converted, corresponding, tokens, through, tokenizer, decoder-only, transformer, module, obtain.
- **Relevant PDF headings:** 3 Method (p. 5).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Command / terrain state | To tackle these two questions, we present the QUART models tailored for quadruped robots and the QUARD dataset, which includes diverse tasks ... | p. 14 (1. Comparison within VLM baselines. The experiment results reveal), p. 14 (1. Comparison within VLM baselines. The experiment results reveal) |
| Whole-body policy / controller | Ding et al. action architecture for multi-task quadruped task compared to previous VLM baselines? | p. 10 (4 Experiments), p. 10 (4 Experiments) |
| Adaptation / recovery | QUART has achieved success rates far exceeding those of the baselines in tasks of all difficulty levels, especially in the most challenging ... | p. 11 (4 Experiments), p. 12 (1. Comparison within VLM baselines. The experiment results reveal) |

## Failure and Ablation Link

- **p. 10 / 4 Experiments - extractive PDF cue:** In total, over 1500 episodes are tested in this evaluation, comprising 425 episodes for going to objects, 500 for going to objects without colliding with ...
- **p. 10 / 4 Experiments - extractive PDF cue:** And we use learning rate 2e-5 and batch size 256 to fine-tune the model for 100K gradient steps.
- **p. 9 / Figure/Table caption - extractive PDF cue:** Fig. 5: Architecture of QUART. It is designed to leverage the scene comprehension capability of a pretrained MLLM. It receives visual information as observation, and ...
- **p. 12 / 1. Comparison within VLM baselines. The experiment results reveal - extractive PDF cue:** This failure manifests in behaviors such as repetitive motion, misdirection, wrong terminate commands.
- **p. 12 / 1. Comparison within VLM baselines. The experiment results reveal - extractive PDF cue:** When confronted with unseen instructions, the alighment between the existing language and the integration of vision and action cues within the baselines is compromised, resulting ...
- **p. 11 / 1. Comparison within VLM baselines. The experiment results reveal - extractive PDF cue:** This observation suggests that while visual language models (VLMs) can grasp abstract principles of the world, directly applying VLMs does not readily translate to the ...
- **p. 14 / 1. Comparison within VLM baselines. The experiment results reveal - extractive PDF cue:** 5 Conclusion & Future Work This paper emphasizes the significance of deploying Vision-Language-Action models on quadruped robots.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 8 (3 Method), p. 9 (3 Method), p. 5 (3 Method), p. 9 (3 Method), p. 5 (3 Method), p. 6 (3 Method), objective p. 9 (3 Method), p. 5 (3 Method), p. 7 (3 Method), p. 7 (3 Method), p. 9 (3 Method), temporal p. 5 (3 Method), p. 6 (3 Method), p. 6 (3 Method), p. 8 (3 Method), p. 9 (3 Method), p. 9 (3 Method).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
