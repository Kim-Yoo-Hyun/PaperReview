# Method - Human2LocoMan: Learning Versatile Quadrupedal Manipulation with Human Pretraining

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p122.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p122.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 5 (III. METHODOLOGY), p. 6 (III. METHODOLOGY), p. 6 (III. METHODOLOGY), p. 7 (III. METHODOLOGY)): Similar to the design in [78], we use a cross-attention layer to format observational features into a fixed number of tokens for each modality.

## Method Body Digest

- **p. 5 / III. METHODOLOGY - extractive PDF cue:** Similar to the design in [78], we use a cross-attention layer to format observational features into a fixed number of tokens for each modality.
- **p. 4 / III. METHODOLOGY - extractive PDF cue:** We adopt a two-stage training process: the modularized cross-embodiment model is first pretrained on easy-to-collect human data, and then finetuned on a small amount of ...
- **p. 5 / III. METHODOLOGY - extractive PDF cue:** For image inputs, the features are obtained from a pretrained ResNet encoder that can be finetuned during training; for proprioceptive or state-like inputs, the features ...
- **p. 6 / III. METHODOLOGY - extractive PDF cue:** The trunk is an encoder-decoder Transformer, where the input sequence length and the output sequence length are both fixed, as the number of tokens for ...
- **p. 6 / III. METHODOLOGY - extractive PDF cue:** We use the behavioral cloning objective for both pretraining and finetuning.
- **p. 7 / III. METHODOLOGY - extractive PDF cue:** Algorithm 1 Pretraining MXT on human data and finetuning on LocoMan data Input: Human dataset Dhuman, LocoMan dataset DLocoMan Output: Policy π for versatile LocoMan ...
- **p. 4 / III. METHODOLOGY - extractive PDF cue:** The dataset consists of aligned vision, proprioception, and actions from the human and the robot.
- **p. 6 / III. METHODOLOGY - extractive PDF cue:** In general, given a dataset De on an embodiment e and aligned action modalities m1, ..., mk, the total loss to optimize when training on ...

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive PDF cue:** In summary, our paper provides the following contributions: • We propose Human2LocoMan, a framework that enables flexible and scalable collection of human demonstrations and teleoperated ...
- **p. 6 / III. METHODOLOGY - extractive PDF cue:** This design preserves modality-specific distributions unique to each embodiment and enables the model to explicitly account for distributional gaps across embodiments, which is core to ...
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** To address these challenges, and drawing inspiration from the LocoMan platform [14]-a quadrupedal robot equipped with two leg-mounted loco-manipulators that offers a versatile foundation for ...

## Source Evidence Cues

- **p. 5 / III. METHODOLOGY - extractive PDF cue:** Similar to the design in [78], we use a cross-attention layer to format observational features into a fixed number of tokens for each modality.
- **p. 4 / III. METHODOLOGY - extractive PDF cue:** We adopt a two-stage training process: the modularized cross-embodiment model is first pretrained on easy-to-collect human data, and then finetuned on a small amount of ...
- **p. 5 / III. METHODOLOGY - extractive PDF cue:** For image inputs, the features are obtained from a pretrained ResNet encoder that can be finetuned during training; for proprioceptive or state-like inputs, the features ...
- **p. 6 / III. METHODOLOGY - extractive PDF cue:** The trunk is an encoder-decoder Transformer, where the input sequence length and the output sequence length are both fixed, as the number of tokens for ...
- **p. 6 / III. METHODOLOGY - extractive PDF cue:** We use the behavioral cloning objective for both pretraining and finetuning.
- **p. 7 / III. METHODOLOGY - extractive PDF cue:** Algorithm 1 Pretraining MXT on human data and finetuning on LocoMan data Input: Human dataset Dhuman, LocoMan dataset DLocoMan Output: Policy π for versatile LocoMan ...
- **p. 4 / III. METHODOLOGY - extractive PDF cue:** The dataset consists of aligned vision, proprioception, and actions from the human and the robot.
- **Detected method headings:** III. METHODOLOGY (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Command / terrain state | body state와 terrain/task context를 표현한다 | proprioception, terrain/perception, velocity command | history encoder, reference, terrain latent 또는 behavior mode를 구성 | locomotion context | Similar to the design in [78], we use a cross-attention layer to format observational features into a fixed number of tokens for ... | p. 5 (III. METHODOLOGY), p. 4 (III. METHODOLOGY) |
| Whole-body policy / controller | context에서 joint target 또는 torque를 만든다 | context, body state, contact | RL policy, reference tracking, inverse dynamics 또는 whole-body control을 적용 | joint action/torque | We adopt a two-stage training process: the modularized cross-embodiment model is first pretrained on easy-to-collect human data, and then finetuned on a ... | p. 4 (III. METHODOLOGY), p. 5 (III. METHODOLOGY) |
| Adaptation / recovery | disturbance와 contact mismatch에 대응한다 | new observation/history와 failure signal | latent adaptation, foothold change, recovery 또는 replan을 수행 | updated command | For image inputs, the features are obtained from a pretrained ResNet encoder that can be finetuned during training; for proprioceptive or state-like ... | p. 5 (III. METHODOLOGY), p. 6 (III. METHODOLOGY) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / III. METHODOLOGY - extractive PDF cue:** In general, given a dataset De on an embodiment e and aligned action modalities m1, ..., mk, the total loss to optimize when training on ...
- **p. 7 / III. METHODOLOGY - extractive PDF cue:** Pose Pose Pose Action Action Human-Unimanual (R) ✓ × ✓ ✓ × ✓ ✓ × ✓ × Human-Unimanual (L) ✓ × ✓ × ✓ ✓ ...
- **p. 6 / III. METHODOLOGY - extractive PDF cue:** We use the behavioral cloning objective for both pretraining and finetuning.
- **p. 7 / III. METHODOLOGY - extractive PDF cue:** Set finetuning learning rate ηfinetune for step = 1, 2, ... do ▷Finetuning Stage Sample a batch B from DLocoMan Compute LLocoMan(B) = P i ...
- **p. 5 / III. METHODOLOGY - extractive PDF cue:** We employ null-space projection for kinematic tracking and quadratic programming for dynamic optimization to compute the desired joint positions, velocities, and torques.
- **Formal bridge:** body/proprioceptive/terrain state -> joint action/torque/footstep -> return, tracking or stability objective -> progress, balance and terrain robustness.
- **Equation/algorithm anchors:** p. 6 (III. METHODOLOGY), p. 6 (III. METHODOLOGY), p. 7 (III. METHODOLOGY).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | trunk, encoder-decoder, Transformer, where, input, sequence, length, output, fixed, number, tokens, observation, action, modality | proprioception, terrain/perception observation과 velocity command | body cue; exact tensor/frame verify |
| State/latent | trunk, encoder-decoder, Transformer, where, input, sequence, length, output, fixed, number | body/contact state, foothold 또는 behavior mode | body cue; notation verify |
| Action/output | summary, provides, following, contributions, Human2LocoMan, framework, enables, flexible, scalable, collection | joint target, torque, footstep 또는 locomotion action | body cue; unit/decoder verify |
| Objective/constraint | general, given, dataset, embodiment, aligned, action, modalities, total, loss, optimize | return, tracking or stability objective | equation anchor required |

## Observation–State–Action Interface

- **p. 6 / III. METHODOLOGY - extractive PDF cue:** The trunk is an encoder-decoder Transformer, where the input sequence length and the output sequence length are both fixed, as the number of tokens for ...
- **p. 6 / III. METHODOLOGY - extractive PDF cue:** By explicitly decomposing the input and output modalities and encoding them separately, we are leveraging the innate structure of observations and actions and imposing such ...
- **p. 5 / III. METHODOLOGY - extractive PDF cue:** The tokenizers act as encoders and map embodiment-specific observation modalities to tokens in the latent space, and the detokenizers translate the output tokens from the ...
- **p. 7 / III. METHODOLOGY - extractive PDF cue:** Algorithm 1 Pretraining MXT on human data and finetuning on LocoMan data Input: Human dataset Dhuman, LocoMan dataset DLocoMan Output: Policy π for versatile LocoMan ...
- **p. 4 / III. METHODOLOGY - extractive PDF cue:** 𝓕𝒖 𝒙 𝒚 𝒛 Data Collection Training Deployment Dataset Pretraining Human Proprioception Human Observations Human Actions Robot Proprioception Robot Observations Robot Actions Finetuning Fig.
- **p. 4 / III. METHODOLOGY - extractive PDF cue:** The in-domain robotic data collected via teleoperation are used to finetune the pretrained model to learn a manipulation policy that predicts the 6D poses of ...
- **p. 5 / III. METHODOLOGY - extractive PDF cue:** For image inputs, the features are obtained from a pretrained ResNet encoder that can be finetuned during training; for proprioceptive or state-like inputs, the features ...
- **Normalized interface:** observation=proprioception, terrain/perception observation과 velocity command; state=body/contact state, foothold 또는 behavior mode; output/action=joint target, torque, footstep 또는 locomotion action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | gait/skill episode horizon과 short-horizon body control이 계층적으로 분리된다. | To reduce compounding errors and lower inference frequency, we adopt action chunking [18], where the detokenizers predict a sequence of h actions ... | episode/sequence/action-chunk boundary |
| Rate / latency | high-level command, policy rate와 low-level torque rate를 구분; exact rate 확인 필요. | Pose Pose Pose Action Action Human-Unimanual (R) ✓ × ✓ ✓ × ✓ ✓ × ✓ × Human-Unimanual (L) ✓ × ✓ ... | Hz/fps, inference time and control rate |
| Memory | proprioceptive history, terrain latent와 contact/body state. | not recovered | window and reset |
| Compute | policy inference, adaptation encoder와 whole-body/control solve가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / III. METHODOLOGY - extractive PDF cue:** We adopt a two-stage training process: the modularized cross-embodiment model is first pretrained on easy-to-collect human data, and then finetuned on a small amount of ...
- **p. 5 / III. METHODOLOGY - extractive PDF cue:** For image inputs, the features are obtained from a pretrained ResNet encoder that can be finetuned during training; for proprioceptive or state-like inputs, the features ...
- **p. 6 / III. METHODOLOGY - extractive PDF cue:** We use the behavioral cloning objective for both pretraining and finetuning.
- **p. 7 / III. METHODOLOGY - extractive PDF cue:** Algorithm 1 Pretraining MXT on human data and finetuning on LocoMan data Input: Human dataset Dhuman, LocoMan dataset DLocoMan Output: Policy π for versatile LocoMan ...
- **p. 5 / III. METHODOLOGY - extractive PDF cue:** For image inputs, the features are obtained from a pretrained ResNet encoder that can be finetuned during training; for proprioceptive or state-like inputs, the features ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Similar, design, cross-attention, layer, format, observational, features, fixed, number, tokens, modality, adopt, two-stage, training, process, modularized, cross-embodiment, model, first, pretrained.
- **Relevant PDF headings:** III. METHODOLOGY (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Command / terrain state | Both unimanual and bimanual toy collection tasks assess the robot's ability to grasp objects of varying shapes, colors, and positions. | p. 8 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |
| Whole-body policy / controller | (2) How does MXT compare to state-of-the-art imitation learning architectures? | p. 7 (IV. EXPERIMENTS), p. 10 (Figure/Table caption) |
| Adaptation / recovery | Fig. 6: Substep success rate. The success rate for some substep is calcuated as the percentage of trials where the robot success- ... | p. 10 (Figure/Table caption), p. 1 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 8 / IV. EXPERIMENTS - extractive PDF cue:** The unimanual variant emphasizes coordination between the torso and end-effector, while the bimanual variant highlights synchronized control of two loco-manipulators.
- **p. 8 / IV. EXPERIMENTS - extractive PDF cue:** The unimanual variant additionally requires torso articulation to reach shoes placed at different heights.
- **p. 10 / Figure/Table caption - extractive PDF cue:** Fig. 5: Ablation study on unimanual and bimanual toy collection. We compare MXT, its ablation MXT-Agg, and baseline HPT on SR and TS. Here, "L" ...
- **p. 7 / IV. EXPERIMENTS - extractive PDF cue:** We use 10 objects for robot finetuning, while all objects are included in human pretraining and real-robot evaluation.
- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1: Human2LocoMan provides a unified framework for collecting human demonstrations and teleoperated robot whole- body motions, along with cross-embodiment policy learning for quadrupedal manipulation. ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 2: Human2LocoMan framework. Our system uses an XR headset for data collection, capturing egocentric human data and teleoperated robot data, all mapped to a ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Fig. 6: Substep success rate. The success rate for some substep is calcuated as the percentage of trials where the robot success- fully completed the ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 5 (III. METHODOLOGY), p. 6 (III. METHODOLOGY), p. 6 (III. METHODOLOGY), p. 7 (III. METHODOLOGY), objective p. 6 (III. METHODOLOGY), p. 7 (III. METHODOLOGY), p. 6 (III. METHODOLOGY), p. 7 (III. METHODOLOGY), p. 5 (III. METHODOLOGY), temporal p. 5 (III. METHODOLOGY), p. 7 (III. METHODOLOGY), p. 5 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
