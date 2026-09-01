# Method - Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (18 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p052.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p052.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (B. Slow-Fast Policy Learning), p. 7 (architecture), p. 7 (architecture), p. 6 (B. Slow-Fast Policy Learning), p. 5 (B. Slow-Fast Policy Learning), p. 6 (B. Slow-Fast Policy Learning)): 1 policy learning, a slow Latent Diffusion Policy (LDP) is trained to predict the latent action chuck according to the observation in a way similar to Diffusion Policy [10 During ...

## Method Body Digest

- **p. 5 / B. Slow-Fast Policy Learning - extractive body cue:** 1 policy learning, a slow Latent Diffusion Policy (LDP) is trained to predict the latent action chuck according to the observation in a way similar ...
- **p. 7 / architecture - extractive body cue:** We calculate the latency caused by policy inference and action execution, and discard the first few action steps predicted by the model to send the ...
- **p. 7 / architecture - extractive body cue:** We use relative end-effector (EE) trajectory for action representation, which has been proven to be effective even in complex tasks by UMI [//].
- **p. 6 / B. Slow-Fast Policy Learning - extractive body cue:** an action chunk A € R™*? in the policy leaming Dpotiey: the encoder downsamples it to a latent one Z = &(A) CR We choose ...
- **p. 5 / B. Slow-Fast Policy Learning - extractive body cue:** 1) Fast Policy: The fast asymmetric tokenizer (AT) consists of a ID-CNN encoder & and a GRU [12] decoder 7.
- **p. 6 / B. Slow-Fast Policy Learning - extractive body cue:** To transform the model to Tatent space, we use the latent action chunk Z? ~ &(A®).
- **p. 4 / A. 3D Deformation Field Extraction - extractive body cue:** We use a score-based tracking algorithm [21] to calculate 2D optical flow between the initial frame Dp and the current frame Dy: Fi = [dey]
- **p. 6 / B. Slow-Fast Policy Learning - extractive body cue:** During training, given the observation (including image, tactlity and propri- ‘oception), the gradient field is leamed by ep and the DDPM training objective can be ...

## Design Rationale

- **p. 1 / Abstract - extractive body cue:** To address these challenges, we introduce TactAR, 4 low-cost tleoperation system that provides real-time tactile feedback through Augmented Reality (AR), along with Reactive Diffusion Policy ...
- **p. 2 / I. Ivrropucrion - extractive body cue:** In this work, we propose two critical components to solve the above issues of visual-tactile imitation learning:
- **p. 2 / I. Ivrropucrion - extractive body cue:** To leverage the high-quality visual tactile data collected by the TactAR system, we propose an imitation learning algorithm called Reactive Diffusion Policy (RDP) (Fig. / ...

## Source Evidence Cues

- **p. 5 / B. Slow-Fast Policy Learning - extractive body cue:** 1 policy learning, a slow Latent Diffusion Policy (LDP) is trained to predict the latent action chuck according to the observation in a way similar ...
- **p. 7 / architecture - extractive body cue:** We calculate the latency caused by policy inference and action execution, and discard the first few action steps predicted by the model to send the ...
- **p. 7 / architecture - extractive body cue:** We use relative end-effector (EE) trajectory for action representation, which has been proven to be effective even in complex tasks by UMI [//].
- **p. 6 / B. Slow-Fast Policy Learning - extractive body cue:** an action chunk A € R™*? in the policy leaming Dpotiey: the encoder downsamples it to a latent one Z = &(A) CR We choose ...
- **p. 5 / B. Slow-Fast Policy Learning - extractive body cue:** 1) Fast Policy: The fast asymmetric tokenizer (AT) consists of a ID-CNN encoder & and a GRU [12] decoder 7.
- **p. 6 / B. Slow-Fast Policy Learning - extractive body cue:** To transform the model to Tatent space, we use the latent action chunk Z? ~ &(A®).
- **p. 4 / A. 3D Deformation Field Extraction - extractive body cue:** We use a score-based tracking algorithm [21] to calculate 2D optical flow between the initial frame Dp and the current frame Dy: Fi = [dey]
- **Detected method headings:** B. Slow-Fast Policy Learning (p. 5); architecture (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multi-modal contact encoding | vision과 touch를 contact feature로 결합한다 | tactile image/force, vision, proprioception | tactile encoder, calibration, fusion 또는 temporal feature extraction을 수행 | contact feature/state | 1 policy learning, a slow Latent Diffusion Policy (LDP) is trained to predict the latent action chuck according to the observation in ... | p. 5 (B. Slow-Fast Policy Learning), p. 7 (architecture) |
| Contact / dynamics inference | contact mode와 object response를 추정한다 | contact feature와 action history | mode classifier, force/dynamics model 또는 state estimator를 update | contact/force prediction | We calculate the latency caused by policy inference and action execution, and discard the first few action steps predicted by the model ... | p. 7 (architecture), p. 7 (architecture) |
| Force-aware action correction | interaction feedback으로 command를 보정한다 | predicted contact와 current wrench/touch | policy/control law가 action, force 또는 grasp를 재계산 | contact-safe action/torque | We use relative end-effector (EE) trajectory for action representation, which has been proven to be effective even in complex tasks by UMI ... | p. 7 (architecture), p. 6 (B. Slow-Fast Policy Learning) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / B. Slow-Fast Policy Learning - extractive body cue:** During training, given the observation (including image, tactlity and propri- ‘oception), the gradient field is leamed by ep and the DDPM training objective can be ...
- **p. 5 / A. 3D Deformation Field Extraction - extractive body cue:** Compared to force/torque sensors like ATI mini45 [3] which costs about $3000, the optical tactile sensors offer a significant cost advantage.
- **p. 4 / A. 3D Deformation Field Extraction - extractive body cue:** (2) Our customized MCTuc [48] costs, around $50 in lab fabrication, and there is large potential
- **p. 4 / A. 3D Deformation Field Extraction - extractive body cue:** Our TactAR system is built with low-cost hhardwares. ‘The Meta Quest3 VR heaset used for teleoperation and AR feedbacks costs $199.
- **p. 5 / A. 3D Deformation Field Extraction - extractive body cue:** for lower cost in industrial manufacturing in the future.
- **p. 6 / B. Slow-Fast Policy Learning - extractive body cue:** On the one hand, the downsampled latent representation reduces computational costs.
- **Formal bridge:** visual/tactile/proprioceptive contact history -> contact-aware action/force -> contact prediction/control error -> slip/contact success and safe interaction.
- **Equation/algorithm anchors:** p. 6 (B. Slow-Fast Policy Learning), p. 6 (B. Slow-Fast Policy Learning).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | ForceMimiec, adds, force, sensor, handheld, device, feedback, suffers, inaccuracy, pose, estimation, thus, cannot, directly | tactile image/force, vision과 proprioceptive history | body cue; exact tensor/frame verify |
| State/latent | ForceMimiec, adds, force, sensor, handheld, device, feedback, suffers, inaccuracy, pose | contact geometry, force state 또는 latent dynamics | body cue; notation verify |
| Action/output | address, challenges, introduce, TactAR, low-cost, tleoperation, system, provides, real-time, tactile | grasp/contact action, force command 또는 object motion | body cue; unit/decoder verify |
| Objective/constraint | During, training, given, observation, including, image, tactlity, propri-, oception, gradient | contact prediction/control error | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / B. Robot Data Collection System - extractive body cue:** ForceMimiec [1] adds a force sensor on a handheld device [11] to get force feedback, but suffers from the inaccuracy of pose estimation, and thus ...
- **p. 1 / Front matter - extractive body cue:** action trajectories with a slow policy network and achieve closed-loop control based on high-frequency tactile / force feedback
- **p. 6 / B. Slow-Fast Policy Learning - extractive body cue:** an action chunk A € R™*? in the policy leaming Dpotiey: the encoder downsamples it to a latent one Z = &(A) CR We choose ...
- **p. 2 / I. Ivrropucrion - extractive body cue:** state during the execution of action chunks, which makes the policy unable to respond instantly to environment changes in ccontact-rich tasks.
- **p. 2 / I. Ivrropucrion - extractive body cue:** Real-world experiments. have shown that our Reactive Diffusion Policy algorithm can model complex actions while maintaining very fast reactive behavior, achieving a significant performance improvement ...
- **p. 5 / B. Slow-Fast Policy Learning - extractive body cue:** 1 policy learning, a slow Latent Diffusion Policy (LDP) is trained to predict the latent action chuck according to the observation in a way similar ...
- **p. 5 / B. Slow-Fast Policy Learning - extractive body cue:** Previous works [10, 71] have demonstrated that predicting action sequences or action chunks [36] effectively preserves temporal action consistency and handles non-Markovian or idle actions, ...
- **Normalized interface:** observation=tactile image/force, vision과 proprioceptive history; state=contact geometry, force state 또는 latent dynamics; output/action=grasp/contact action, force command 또는 object motion.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | contact episode 또는 action chunk horizon; contact event timing이 핵심이다. | Previous works [10, 71] have demonstrated that predicting action sequences or action chunks [36] effectively preserves temporal action consistency and handles non-Markovian ... | episode/sequence/action-chunk boundary |
| Rate / latency | tactile sampling/control loop가 visual policy rate와 다를 수 있다; numeric values 확인 필요. | Why can't ‘we simply use small chunk size o temporal ensemble to increase closed-loop control frequency? | Hz/fps, inference time and control rate |
| Memory | recent tactile/force history와 visual state; recurrent memory 여부 확인 필요. | not recovered | window and reset |
| Compute | sensor fusion, contact inference와 high-frequency correction이 latency를 결정한다. | 5) Implementation Details: ‘The Diffusion Policy and our slow policy (LDP) predict open-loop 12 FPS action sequences for each action chunk. | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / B. Slow-Fast Policy Learning - extractive body cue:** 1 policy learning, a slow Latent Diffusion Policy (LDP) is trained to predict the latent action chuck according to the observation in a way similar ...
- **p. 7 / architecture - extractive body cue:** We calculate the latency caused by policy inference and action execution, and discard the first few action steps predicted by the model to send the ...
- **p. 9 / V. EXPERIMENTS - extractive body cue:** Please see Appendix D, F and I for more details on data collection, the inference process and the hyperparameters.
- **p. 6 / architecture - extractive body cue:** ‘TABLE I: Inference Time of Different Modules on RTX 4090

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** policy, learning, slow, Latent, Diffusion, LDP, trained, predict, action, chuck, according, observation, similar, During, inference, sample, chunks, lower, frequency, within.
- **Relevant PDF headings:** B. Slow-Fast Policy Learning (p. 5); architecture (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multi-modal contact encoding | 1) Hardware: ‘The experimental platform consists of two Flexiv Rizon 4 [19] robotic arms with joint torque sensors and two Flexiv Grav ... | p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS) |
| Contact / dynamics inference | All devices are connected to a workstation with an Intel Core i9-14900K CPU and an NVIDIA RTX 4090 GPU for both data ... | p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS) |
| Force-aware action correction | + Ql: Does tactile signals improve policy performance in contact-rich tasks? | p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 8 / V. EXPERIMENTS - extractive body cue:** the handlers, approach the paper cup, clamp the paper cup with the two handlers, carefully lift the cup along the trajectory of the curve without ...
- **p. 8 / V. EXPERIMENTS - extractive body cue:** For Bimanual Lifting task, if the paper cup is lifted into the air following the designated trajectory without significant compression, the score will be 1; ...
- **p. 9 / B. Results - extractive body cue:** Although the performance of both methods is similar, low-dimensional tactile embedding demonstrates greater robustness to texture ‘changes resulting from gel damage or gel replacements during ...
- **p. 16 / Figure/Table caption - extractive body cue:** Fig. 15: Improved MCTuc Sensor for our task, The left part is the gripper integrated illustration, and the right part is the detailed structure and ...
- **p. 9 / B. Results - extractive body cue:** It may get stuck when making contact with the object (e.2., failure case 2 in Fig.
- **p. 9 / B. Results - extractive body cue:** However, despite similar performance, these two DP baselines exhibit different failure modes.
- **p. 10 / 056 O58 om - extractive body cue:** 8: Evaluation results and failure cases of baselines.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (B. Slow-Fast Policy Learning), p. 7 (architecture), p. 7 (architecture), p. 6 (B. Slow-Fast Policy Learning), p. 5 (B. Slow-Fast Policy Learning), p. 6 (B. Slow-Fast Policy Learning), objective p. 6 (B. Slow-Fast Policy Learning), p. 5 (A. 3D Deformation Field Extraction), p. 4 (A. 3D Deformation Field Extraction), p. 4 (A. 3D Deformation Field Extraction), p. 5 (A. 3D Deformation Field Extraction), p. 6 (B. Slow-Fast Policy Learning), temporal p. 5 (B. Slow-Fast Policy Learning), p. 7 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS), p. 9 (V. EXPERIMENTS), p. 5 (B. Slow-Fast Policy Learning), p. 1 (I. Ivrropucrion).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
