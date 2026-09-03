# Method - SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (39 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://research.nvidia.com/labs/dair/publication/sonic2026/; PDF retrieval source: https://research.nvidia.com/labs/dair/publication/sonic2026/. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 15 (3.2. Universal Humanoid Motion Tracking), p. 15 (3.2. Universal Humanoid Motion Tracking), p. 16 (3.2. Universal Humanoid Motion Tracking), p. 16 (3.2. Universal Humanoid Motion Tracking), p. 14 (3.2. Universal Humanoid Motion Tracking), p. 14 (3.2. Universal Humanoid Motion Tracking)): Specialized encoders map heterogeneous human and robot motion inputs into a shared latent representation, which is quantized into a universal token that drives a common robot control decoder; an auxiliary ...

## Method Body Digest

- **p. 15 / 3.2. Universal Humanoid Motion Tracking - extractive body cue:** Specialized encoders map heterogeneous human and robot motion inputs into a shared latent representation, which is quantized into a universal token that drives a common ...
- **p. 15 / 3.2. Universal Humanoid Motion Tracking - extractive body cue:** First, a robot control decoder 𝒟𝑐transforms the universal token into motor commands that control the robot's joints. 𝒟𝑐takes as input the concatenation of the universal ...
- **p. 16 / 3.2. Universal Humanoid Motion Tracking - extractive body cue:** We used asymmetric actor-critic training [63]: the critic observes privileged simulation state (base linear velocity, full body link positions and orientations, and noise-free observations) during ...
- **p. 16 / 3.2. Universal Humanoid Motion Tracking - extractive body cue:** In practice, the auxiliary losses regularize the latent space and stabilize rather than destabilize PPO optimization, and we observed no training instabilities from coupling quantization ...
- **p. 14 / 3.2. Universal Humanoid Motion Tracking - extractive body cue:** The policy 𝜋outputs target joint positions 𝑎𝑡as actions, which are tracked by proportional-derivative (PD) controllers at each joint.
- **p. 14 / 3.2. Universal Humanoid Motion Tracking - extractive body cue:** Quantizer Robot Motion Decoder Robot Control Decoder Encoders Decoders Motion Generators Hybrid Encoder Robot Encoder Human Encoder GEM Human Motion Generator PICO VR Toolkit Kinematic ...
- **p. 18 / 3.5. Deployment - extractive body cue:** The encoderdecoder design allowed seamless switching between input interfaces (keyboard, gamepad, VR, network streams) by changing the active encoder, with no retraining required.
- **p. 14 / 3.2. Universal Humanoid Motion Tracking - extractive body cue:** We defined the reward as 𝑟𝑡= ℛ(𝑠p 𝑡, 𝑠g 𝑡) + 𝒫(𝑠p 𝑡, 𝑎𝑡), combining a tracking term that minimizes root and body-link pose and ...

## Design Rationale

- **p. 3 / 1. Introduction - extractive body cue:** We propose Supersizing mOtion tracking for Natural humanoId Control (SONIC), a framework that enables natural humanoid control across a wide range of applications (Movie S1).
- **p. 2 / 1. Introduction - extractive body cue:** In addition, we show how such a motion tracker can be applied to meaningful downstream tasks, and introduce two key contributions.
- **p. 3 / 1. Introduction - extractive body cue:** Third, we provide a comprehensive evaluation demonstrating humanoid control scaling trends, zero-shot transfer to unseen motions, robust simto-real deployment on physical humanoid robots, and successful ...

## Source Evidence Cues

- **p. 15 / 3.2. Universal Humanoid Motion Tracking - extractive body cue:** Specialized encoders map heterogeneous human and robot motion inputs into a shared latent representation, which is quantized into a universal token that drives a common ...
- **p. 15 / 3.2. Universal Humanoid Motion Tracking - extractive body cue:** First, a robot control decoder 𝒟𝑐transforms the universal token into motor commands that control the robot's joints. 𝒟𝑐takes as input the concatenation of the universal ...
- **p. 16 / 3.2. Universal Humanoid Motion Tracking - extractive body cue:** We used asymmetric actor-critic training [63]: the critic observes privileged simulation state (base linear velocity, full body link positions and orientations, and noise-free observations) during ...
- **p. 16 / 3.2. Universal Humanoid Motion Tracking - extractive body cue:** In practice, the auxiliary losses regularize the latent space and stabilize rather than destabilize PPO optimization, and we observed no training instabilities from coupling quantization ...
- **p. 14 / 3.2. Universal Humanoid Motion Tracking - extractive body cue:** The policy 𝜋outputs target joint positions 𝑎𝑡as actions, which are tracked by proportional-derivative (PD) controllers at each joint.
- **p. 14 / 3.2. Universal Humanoid Motion Tracking - extractive body cue:** Quantizer Robot Motion Decoder Robot Control Decoder Encoders Decoders Motion Generators Hybrid Encoder Robot Encoder Human Encoder GEM Human Motion Generator PICO VR Toolkit Kinematic ...
- **p. 18 / 3.5. Deployment - extractive body cue:** The encoderdecoder design allowed seamless switching between input interfaces (keyboard, gamepad, VR, network streams) by changing the active encoder, with no retraining required.
- **Detected method headings:** 2.5. Foundation-Model-Driven Loco-manipulation (p. 9); 3. Materials and Methods (p. 12)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Reference / embodiment interface | human/task reference를 robot-compatible state로 바꾼다 | reference motion, visual/language input, body state | retargeting, pose/skill conditioning 또는 multimodal encoding을 수행 | whole-body context | Specialized encoders map heterogeneous human and robot motion inputs into a shared latent representation, which is quantized into a universal token that ... | p. 15 (3.2. Universal Humanoid Motion Tracking), p. 15 (3.2. Universal Humanoid Motion Tracking) |
| Balance-aware whole-body execution | reference를 contact·balance-aware command로 변환한다 | context, body state, contact | policy, WBC, inverse dynamics 또는 hierarchical control을 적용 | joint target/torque | First, a robot control decoder 𝒟𝑐transforms the universal token into motor commands that control the robot's joints. 𝒟𝑐takes as input the concatenation ... | p. 15 (3.2. Universal Humanoid Motion Tracking), p. 16 (3.2. Universal Humanoid Motion Tracking) |
| Recovery / adaptation | mismatch·disturbance·fall 뒤 behavior를 복구한다 | feedback/history와 failure state | adaptation, motion completion, reinitialization 또는 safe stop을 수행 | recovery command | We used asymmetric actor-critic training [63]: the critic observes privileged simulation state (base linear velocity, full body link positions and orientations, and ... | p. 16 (3.2. Universal Humanoid Motion Tracking), p. 16 (3.2. Universal Humanoid Motion Tracking) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 14 / 3.2. Universal Humanoid Motion Tracking - extractive body cue:** We defined the reward as 𝑟𝑡= ℛ(𝑠p 𝑡, 𝑠g 𝑡) + 𝒫(𝑠p 𝑡, 𝑎𝑡), combining a tracking term that minimizes root and body-link pose and ...
- **p. 14 / 3.2. Universal Humanoid Motion Tracking - extractive body cue:** We trained the policy using proximal policy optimization (PPO) [58] to maximize the expected cumulative discounted return E [︁∑︀𝑇 𝑡=1 𝛾𝑡-1𝑟𝑡 ]︁ .
- **p. 16 / 3.2. Universal Humanoid Motion Tracking - extractive body cue:** In practice, the auxiliary losses regularize the latent space and stabilize rather than destabilize PPO optimization, and we observed no training instabilities from coupling quantization ...
- **p. 17 / 3.3. Generative Kinematic Motion Planner - extractive body cue:** Rather than training the network to predict the entire sequence of tokens from these sparse constraints in a single pass, we adopted a masked token ...
- **p. 16 / 3.2. Universal Humanoid Motion Tracking - extractive body cue:** All four losses are optimized jointly in a single end-to-end training loop.
- **p. 15 / 3.2. Universal Humanoid Motion Tracking - extractive body cue:** The total loss comprises: ℒ= ℒppo + ℒrecon + ℒtoken + ℒcycle (1) ℒrecon = ‖𝒟𝑟(𝑧𝑟) -𝑔𝑟‖2 + ‖𝒟𝑟(𝑧ℎ) -𝑔𝑟‖2 + ‖𝒟𝑟(𝑧𝑚) -𝑔𝑟‖2 (2) ℒtoken ...
- **Formal bridge:** whole-body pose/contact/reference state -> joint/whole-body action -> tracking/balance/task objective -> motion/task success and recovery.
- **Equation/algorithm anchors:** p. 16 (3.2. Universal Humanoid Motion Tracking), p. 15 (3.2. Universal Humanoid Motion Tracking), p. 15 (3.2. Universal Humanoid Motion Tracking), p. 16 (3.2. Universal Humanoid Motion Tracking), p. 17 (3.3. Generative Kinematic Motion Planner), p. 17 (3.3. Generative Kinematic Motion Planner).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Notably, when, input, command, human, motion, encoder-decoder, acts, retargeting, pipeline, robot, recon, serves, loss | proprioception, reference pose/motion, visual or language command | body cue; exact tensor/frame verify |
| State/latent | Notably, when, input, command, human, motion, encoder-decoder, acts, retargeting, pipeline | whole-body pose, balance/contact state와 skill/mode | body cue; notation verify |
| Action/output | Supersizing, mOtion, tracking, Natural, humanoId, Control, SONIC, framework, enables, across | joint/whole-body action, motion target 또는 task trajectory | body cue; unit/decoder verify |
| Objective/constraint | defined, reward, combining, tracking, term, minimizes, root, body-link, pose, velocity | tracking/balance/task objective | equation anchor required |

## Observation–State–Action Interface

- **p. 15 / 3.2. Universal Humanoid Motion Tracking - extractive body cue:** Notably, when the input command is human motion 𝑔ℎ, the encoder-decoder acts as a retargeting pipeline from human to robot motion, and ℒrecon serves as ...
- **p. 14 / 3.2. Universal Humanoid Motion Tracking - extractive body cue:** The policy 𝜋outputs target joint positions 𝑎𝑡as actions, which are tracked by proportional-derivative (PD) controllers at each joint.
- **p. 16 / 3.3. Generative Kinematic Motion Planner - extractive body cue:** The context keyframes capture historical robot states, such as joint positions and root positions, whereas target keyframes are either navigation guidance keyframes generated from user ...
- **p. 16 / 3.2. Universal Humanoid Motion Tracking - extractive body cue:** We used asymmetric actor-critic training [63]: the critic observes privileged simulation state (base linear velocity, full body link positions and orientations, and noise-free observations) during ...
- **p. 13 / 3.2. Universal Humanoid Motion Tracking - extractive body cue:** 6 provides an overview of our approach, SONIC, a universal humanoid motion tracking framework that employs a unified control policy to track diverse motion commands ...
- **p. 15 / 3.2. Universal Humanoid Motion Tracking - extractive body cue:** First, a robot control decoder 𝒟𝑐transforms the universal token into motor commands that control the robot's joints. 𝒟𝑐takes as input the concatenation of the universal ...
- **p. 18 / 3.5. Deployment - extractive body cue:** The system used a multi-rate architecture with four concurrent loops: policy inference at 50 Hz, command streaming at 500 Hz, operator input at 100 Hz, ...
- **Normalized interface:** observation=proprioception, reference pose/motion, visual or language command; state=whole-body pose, balance/contact state와 skill/mode; output/action=joint/whole-body action, motion target 또는 task trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | reference motion/skill horizon과 high-frequency whole-body control horizon이 분리된다. | We concatenated a 10-step history of all proprioceptive quantities and actions into 𝑠p 𝑡, that is, 𝑠p 𝑡≜(𝑞𝑡, ˙𝑞𝑡, 𝜔𝑡, 𝑔𝑡, 𝑎𝑡-1)𝑡-9:𝑡, ... | episode/sequence/action-chunk boundary |
| Rate / latency | motion policy/WBC/torque loop의 계층별 rate; numeric value 확인 필요. | Unlike traditional planners that rely on complex target keyframe generation (such as detailed footstep planning), our system specifies keyframes intuitively and with ... | Hz/fps, inference time and control rate |
| Memory | body pose, contact, reference/history와 fall/recovery state. | We concatenated a 10-step history of all proprioceptive quantities and actions into 𝑠p 𝑡, that is, 𝑠p 𝑡≜(𝑞𝑡, ˙𝑞𝑡, 𝜔𝑡, 𝑔𝑡, 𝑎𝑡-1)𝑡-9:𝑡, ... | window and reset |
| Compute | high-DOF policy, retargeting과 inverse-dynamics/QP solve가 latency를 결정한다. | We supersize physics-based motion tracking to 100 million frames (at 50 Hz) with 128-GPU training, achieving universal tracking capabilities across diverse human ... | hardware, batch and throughput |

## Training vs Inference

- **p. 16 / 3.2. Universal Humanoid Motion Tracking - extractive body cue:** We used asymmetric actor-critic training [63]: the critic observes privileged simulation state (base linear velocity, full body link positions and orientations, and noise-free observations) during ...
- **p. 16 / 3.2. Universal Humanoid Motion Tracking - extractive body cue:** In practice, the auxiliary losses regularize the latent space and stabilize rather than destabilize PPO optimization, and we observed no training instabilities from coupling quantization ...
- **p. 18 / 3.5. Deployment - extractive body cue:** The encoderdecoder design allowed seamless switching between input interfaces (keyboard, gamepad, VR, network streams) by changing the active encoder, with no retraining required.
- **p. 6 / 2.2. Interactive Motion Control - extractive body cue:** The planner achieved inference times under 5 ms on a standard laptop and ∼12 ms on a Jetson Orin GPU.
- **p. 5 / 2.1. Motion Tracking - extractive body cue:** For compute, we trained on 2, 4, and 16 nodes (16, 32, and 128 GPUs), all to 50k iterations, yielding approximately 2k, 9k, and 21k ...
- **p. 15 / 3.2. Universal Humanoid Motion Tracking - extractive body cue:** We chose FSQ over the vector-quantized variational autoencoder (VQ-VAE) [62] for training stability under joint PPO optimization (the Implementation Details section), and validated this and ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Specialized, encoders, heterogeneous, human, robot, motion, inputs, shared, latent, representation, quantized, universal, token, drives, common, control, decoder, auxiliary, facilitates, feature.
- **Relevant PDF headings:** 2.5. Foundation-Model-Driven Loco-manipulation (p. 9); 3. Materials and Methods (p. 12).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Reference / embodiment interface | 14,513 701 253 Dance 9,689 504 485 Injured 9,386 1,167 528 Action / Tool use 9,920 228 322 Others (10+ main cat.) ... | p. 13 (3.1. Humanoid Motion Dataset), p. 3 (2.1. Motion Tracking) |
| Balance-aware whole-body execution | We compared against state-of-the-art trackers: GMT [33], Any2Track [30], and BeyondMimic [29]. | p. 5 (2.1. Motion Tracking), p. 5 (2.1. Motion Tracking) |
| Recovery / adaptation | Table 3: Ablation studies. SR denotes success rate. Each entry reports a single evaluation per configuration on the full test split (descriptive; ... | p. 19 (Figure/Table caption), p. 4 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 11 / Figure/Table caption - extractive body cue:** Table 1: Vision-language-action (VLA) control through the universal token interface. (A) Task success rates. A GR00T N1.5 model, fine-tuned on teleoperated data, is evaluated across ...
- **p. 19 / 3.7. Statistical Analysis - extractive body cue:** Ablation tables report a single evaluation per configuration and are therefore descriptive.
- **p. 4 / 2.1. Motion Tracking - extractive body cue:** (A to C) Effect of scaling data size, model size, and compute on test-content (unseen motion content, OOD) and test-repetition (held-out takes of seen motion ...
- **p. 6 / 2.2. Interactive Motion Control - extractive body cue:** Utilizing the scalable nature of SONIC, we noted that all the applications above were specified after training, without retraining the planner or the tracking policy.
- **p. 9 / 2.3. Video Teleoperation and Multi-Modal Control - extractive body cue:** Human motion was estimated at ≥60 frames per second (fps), enabling interactive teleoperation without specialized motion-capture hardware.
- **p. 9 / 2.5. Foundation-Model-Driven Loco-manipulation - extractive body cue:** We observed that predicting universal tokens produced smoother and safer behavior than predicting explicit SMPL poses, which resulted in jerky motions and poor directional control ...
- **p. 12 / 2.6. Discussion - extractive body cue:** These findings support motion tracking as a practical route to acquire broad, transferable whole-body priors without per-task reward engineering.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 15 (3.2. Universal Humanoid Motion Tracking), p. 15 (3.2. Universal Humanoid Motion Tracking), p. 16 (3.2. Universal Humanoid Motion Tracking), p. 16 (3.2. Universal Humanoid Motion Tracking), p. 14 (3.2. Universal Humanoid Motion Tracking), p. 14 (3.2. Universal Humanoid Motion Tracking), objective p. 14 (3.2. Universal Humanoid Motion Tracking), p. 14 (3.2. Universal Humanoid Motion Tracking), p. 16 (3.2. Universal Humanoid Motion Tracking), p. 17 (3.3. Generative Kinematic Motion Planner), p. 16 (3.2. Universal Humanoid Motion Tracking), p. 15 (3.2. Universal Humanoid Motion Tracking), temporal p. 14 (3.2. Universal Humanoid Motion Tracking), p. 17 (3.3. Generative Kinematic Motion Planner), p. 2 (1. Introduction), p. 13 (3.1. Humanoid Motion Dataset), p. 13 (3.1. Humanoid Motion Dataset), p. 15 (3.2. Universal Humanoid Motion Tracking).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (39 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Notably, when the input command is human motion 𝑔ℎ, the encoder-decoder acts as a retargeting pipeline from human to robot motion, and ℒrecon serves as a retargeting loss that enables ... (p. 15, 3.2. Universal Humanoid Motion Tracking).
- **Objective/update evidence:** All four losses are optimized jointly in a single end-to-end training loop. (p. 16, 3.2. Universal Humanoid Motion Tracking).
- **Temporal/runtime evidence:** After retargeting to the Unitree G1 using General Motion Retargeting (GMR) [54] and PyRoki [55], we filtered out physically implausible motions (such as stair climbing and seated activities) that cannot ... (p. 13, 3.1. Humanoid Motion Dataset).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
