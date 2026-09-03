# Method - Robot Learning with Super-Linear Scaling

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p025.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p025.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 12 (IX. IMPLEMENTATION DETAILS), p. 12 (IX. IMPLEMENTATION DETAILS)): To encode the point cloud observation, we use the volumetric 3D point cloud encoder proposed in Convolutional Occupancy Networks [31], which consists ofa local point net that converts the point ...

## Method Body Digest

- **p. 12 / IX. IMPLEMENTATION DETAILS - extractive body cue:** To encode the point cloud observation, we use the volumetric 3D point cloud encoder proposed in Convolutional Occupancy Networks [31], which consists ofa local point ...
- **p. 12 / IX. IMPLEMENTATION DETAILS - extractive body cue:** The poticy model is a simple Multi-Layer Perceptron (MLP) network, with input as the privileged state in simulation as specified in VII and outputs a ...
- **p. 12 / IX. IMPLEMENTATION DETAILS - extractive body cue:** To implement PPO with the BC loss algorithm, we built upon the Stable Baselines 3 repository [33].
- **p. 12 / IX. IMPLEMENTATION DETAILS - extractive body cue:** We train an MLP network of size 256,256, that takes the embedding of the point cloud observation, which has 128 ‘dimensions, together With the state ...
- **p. 4 / B. Amortized Data Collection - extractive body cue:** We do so by deploying the visuomotor policy (aro) using perceptual observations o, such as RGB point clouds, but since we are in the simulation ...
- **p. 4 / B. Amortized Data Collection - extractive body cue:** T can be used to obtain a single robust, statecovering optimal multi-environment policy xs3(as/s¢) for all Ex :1,-++»€2x Via demonstration-bootstrapped reinforcement learning.
- **p. 3 / B. Amortized Data Collection - extractive body cue:** ‘Rigorithm T CASHIER: Amorized Data Collection for Gen= eralist Policies 1: Input: Human demonstrator 7, erowdsource humans © 2 Initialize vision-based generalist policy 7 3: ...
- **p. 3 / 1. Iyrropucrion - extractive body cue:** Other research has tackled various challenges in realto-sim-to-real, such as enhancing simulator accuracy with real- ‘world interaction data [23, 35,3], and automatically generating aniculations from ...

## Design Rationale

- **p. 1 / Abstract - extractive body cue:** We show that CASHER enables fine-tuning of prestrained to a target scenario using a video sean without any additional hbuman effort.
- **p. 1 / 1. Iyrropucrion - extractive body cue:** Our contributions include 1) a novel continual data collection system based on real-to-sim-to-real for training generalist policies, 2) a novel scanned deployment fine-tuning technique for ...
- **p. 2 / 1. Iyrropucrion - extractive body cue:** Overview of CASHER, we propose « system for taining generalist policies leveraging real-o-sim simulation on crowdsouced scans.

## Source Evidence Cues

- **p. 12 / IX. IMPLEMENTATION DETAILS - extractive body cue:** To encode the point cloud observation, we use the volumetric 3D point cloud encoder proposed in Convolutional Occupancy Networks [31], which consists ofa local point ...
- **p. 12 / IX. IMPLEMENTATION DETAILS - extractive body cue:** The poticy model is a simple Multi-Layer Perceptron (MLP) network, with input as the privileged state in simulation as specified in VII and outputs a ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Demonstration representation | expert trajectory를 training pair/context로 정렬한다 | observation history, goal, expert action | temporal alignment, relabeling 또는 latent context construction을 수행 | training sample/context | To encode the point cloud observation, we use the volumetric 3D point cloud encoder proposed in Convolutional Occupancy Networks [31], which consists ... | p. 12 (IX. IMPLEMENTATION DETAILS), p. 12 (IX. IMPLEMENTATION DETAILS) |
| Policy fitting | expert action distribution을 학습한다 | context와 action target | behavior cloning, adversarial, sequence, diffusion 또는 flow objective를 최적화 | policy/action distribution | The poticy model is a simple Multi-Layer Perceptron (MLP) network, with input as the privileged state in simulation as specified in VII ... | p. 12 (IX. IMPLEMENTATION DETAILS) |
| Closed-loop rollout | distribution shift와 recovery를 확인한다 | current observation/history | action/chunk을 실행하고 feedback으로 다음 prediction을 갱신 | trajectory/failure signal | To encode the point cloud observation, we use the volumetric 3D point cloud encoder proposed in Convolutional Occupancy Networks [31], which consists ... | p. 12 (IX. IMPLEMENTATION DETAILS) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 12 / IX. IMPLEMENTATION DETAILS - extractive body cue:** To implement PPO with the BC loss algorithm, we built upon the Stable Baselines 3 repository [33].
- **p. 12 / IX. IMPLEMENTATION DETAILS - extractive body cue:** The poticy model is a simple Multi-Layer Perceptron (MLP) network, with input as the privileged state in simulation as specified in VII and outputs a ...
- **Formal bridge:** observation history o_{t−H:t} -> expert-like action/chunk a_{t:t+H} -> imitation or action-distribution loss -> closed-loop task success and robustness.
- **Equation/algorithm anchors:** p. 12 (IX. IMPLEMENTATION DETAILS), p. 12 (IX. IMPLEMENTATION DETAILS).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | train, MLP, network, size, takes, embedding, point, cloud, observation, dimensions, together, state, robot, end-effector | observation history와 expert trajectory/action | body cue; exact tensor/frame verify |
| State/latent | train, MLP, network, size, takes, embedding, point, cloud, observation, dimensions | behavior policy와 temporal action context | body cue; notation verify |
| Action/output | CASHER, enables, fine-tuning, prestrained, target, scenario, video, sean, without, additional | predicted action 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | implement, PPO, loss, algorithm, built, upon, Stable, Baselines, repository, poticy | imitation or action-distribution loss | equation anchor required |

## Observation–State–Action Interface

- **p. 12 / IX. IMPLEMENTATION DETAILS - extractive body cue:** We train an MLP network of size 256,256, that takes the embedding of the point cloud observation, which has 128 ‘dimensions, together With the state ...
- **p. 12 / IX. IMPLEMENTATION DETAILS - extractive body cue:** The poticy model is a simple Multi-Layer Perceptron (MLP) network, with input as the privileged state in simulation as specified in VII and outputs a ...
- **p. 4 / B. Amortized Data Collection - extractive body cue:** We do so by deploying the visuomotor policy (aro) using perceptual observations o, such as RGB point clouds, but since we are in the simulation ...
- **p. 4 / B. Amortized Data Collection - extractive body cue:** T can be used to obtain a single robust, statecovering optimal multi-environment policy xs3(as/s¢) for all Ex :1,-++»€2x Via demonstration-bootstrapped reinforcement learning.
- **p. 3 / B. Amortized Data Collection - extractive body cue:** ‘Rigorithm T CASHIER: Amorized Data Collection for Gen= eralist Policies 1: Input: Human demonstrator 7, erowdsource humans © 2 Initialize vision-based generalist policy 7 3: ...
- **p. 3 / 1. Iyrropucrion - extractive body cue:** Other research has tackled various challenges in realto-sim-to-real, such as enhancing simulator accuracy with real- ‘world interaction data [23, 35,3], and automatically generating aniculations from ...
- **p. 1 / Abstract - extractive body cue:** As the training of a generalist policy progresses across environments, its generalization capabilities ‘can be used to replace human effort with model-generated tions.
- **Normalized interface:** observation=observation history와 expert trajectory/action; state=behavior policy와 temporal action context; output/action=predicted action 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single-step 또는 action chunk/trajectory horizon; exact chunk length는 exact value not recovered from the selected body cues. | Additionally, while traditional teleoperation data, collection scales linearly with human effort, CASHER reduces, the human effort needed for subsequent learning steps by ... | episode/sequence/action-chunk boundary |
| Rate / latency | training inference와 deployed control tick을 분리; action chunk면 receding execution 여부 확인. | & T&T UFilterSuccessfulRollouts(T.) 9m, © RLFinetuning(T, {Exe 1.E¥v2 wo The} | Hz/fps, inference time and control rate |
| Memory | current observation, temporal history 또는 recurrent/sequence context. | not recovered | window and reset |
| Compute | backbone/decoder inference, sampling steps와 action horizon이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** encode, point, cloud, observation, volumetric, encoder, Convolutional, Occupancy, Networks, consists, local, converts, features, followed, U-Net, output, dense, voxel, then, pooled.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Demonstration representation | The first experiment involves a thorough real-world evaluation of these policies across two institutions, using three different kitchens and six different objects, ... | p. 6 (A. Zero-Shot Scaling Laws Analysis), p. 12 (IX. IMPLEMENTATION DETAILS) |
| Policy fitting | In Section IV-B, ‘we compare this baseline to the autonomous data collection system presented in Section III-B. | p. 6 (A. Zero-Shot Scaling Laws Analysis), p. 12 (IX. IMPLEMENTATION DETAILS) |
| Closed-loop rollout | To verify the robustness of the learned policies, we ran evaluation on eight additional kitchens, ‘The results highlight an improvement of 16% ... | p. 6 (A. Zero-Shot Scaling Laws Analysis), p. 6 (A. Zero-Shot Scaling Laws Analysis) |

## Failure and Ablation Link

- **p. 6 / A. Zero-Shot Scaling Laws Analysis - extractive body cue:** lef: results fr few-sot fine-tuning on the ask of pick and place « box om a shelf middle: results opening a cabinet right: muli-object evaluation
- **p. 12 / IX. IMPLEMENTATION DETAILS - extractive body cue:** 2) Point cloud policy: As mentioned in Section II-C, when distilling the state-based teacher policy t0 a fine-tuned visuomotor policy, we will train a point ...
- **p. 4 / B. Amortized Data Collection - extractive body cue:** For these environments F, we fall back to querying the human demonstrator for high-quality demonstrations and learn a second state-based policy *+a(a,/s) using demonstration-bootstrapped reinforcement ...
- **p. 5 / B. Amortized Data Collection - extractive body cue:** This reduces the amount of human effort required for data collection as training progresses, Importantly, the generalization across environments does not need to achieve perfect ...
- **p. 4 / B. Amortized Data Collection - extractive body cue:** T can be used to obtain a single robust, statecovering optimal multi-environment policy xs3(as/s¢) for all Ex :1,-++»€2x Via demonstration-bootstrapped reinforcement learning.
- **p. 5 / C. Fine-uning of Generalist Policies on Deployment - extractive body cue:** This model-generated data can then be used to train a robust, high-coverage statebased policy 4(a/s+) using demonstration-bootstrapped re
- **p. 6 / A. Zero-Shot Scaling Laws Analysis - extractive body cue:** To verify the robustness of the learned policies, we ran evaluation on eight additional kitchens, ‘The results highlight an improvement of 16% to 60% rate ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 12 (IX. IMPLEMENTATION DETAILS), p. 12 (IX. IMPLEMENTATION DETAILS), objective p. 12 (IX. IMPLEMENTATION DETAILS), p. 12 (IX. IMPLEMENTATION DETAILS), temporal p. 2 (1. Iyrropucrion), p. 3 (B. Amortized Data Collection), p. 3 (A. Real-to-Sim Scene Synthesis), p. 4 (B. Amortized Data Collection), p. 5 (C. Fine-uning of Generalist Policies on Deployment), p. 5 (C. Fine-uning of Generalist Policies on Deployment).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
