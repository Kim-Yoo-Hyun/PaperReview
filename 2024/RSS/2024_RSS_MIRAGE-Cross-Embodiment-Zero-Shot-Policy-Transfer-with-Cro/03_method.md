# Method - MIRAGE: Cross-Embodiment Zero-Shot Policy Transfer with Cross-Painting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p069.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p069.html. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (4) We assume that the background and lighting conditions), p. 4 (4) We assume that the background and lighting conditions), p. 2 (I. INTRODUCTION), p. 1 (2 Google DeepMind), p. 8 (2) Can Mirage successfully zero-shot transfer trained vision), p. 6 (2) Can Mirage successfully zero-shot transfer trained vision)): Given a source policy action aS t+1 = πS(sS t , oS t ), we would like to transform it into a target policy action aT t+1 = πT (sT ...

## Method Body Digest

- **p. 4 / 4) We assume that the background and lighting conditions - extractive body cue:** Given a source policy action aS t+1 = πS(sS t , oS t ), we would like to transform it into a target policy action ...
- **p. 4 / 4) We assume that the background and lighting conditions - extractive body cue:** We consider the setting where there is a policy πS trained on a dataset of the source robot D = {(sS 1 , oS 1 ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** To handle differences in control gains, Mirage pairs the source robot policy with a forward dynamics model and executes the action predicted by the policy ...
- **p. 1 / 2 Google DeepMind - extractive body cue:** The target robot then uses a forward dynamics model to obtain the desired end effector pose in the target robot frame and executes the steps ...
- **p. 8 / 2) Can Mirage successfully zero-shot transfer trained vision - extractive body cue:** We use a per-dimension linear forward dynamics model and use the demonstration data to fit the regression coefficients.
- **p. 6 / 2) Can Mirage successfully zero-shot transfer trained vision - extractive body cue:** IV, we first train the source robot policies with behavior cloning (BC-RNN) on the provided demonstration data for each task (200 demos for Lift and ...
- **p. 8 / 2) Can Mirage successfully zero-shot transfer trained vision - extractive body cue:** Policies Tasks Tiger (Robotiq) Drawer (Franka) Source T Grip Source T Grip Wrist Camera Only: πS (Diffusion Policy) 90% 0% 70% 0% πS + Cross-Painting ...
- **p. 1 / Abstract - extractive body cue:** Focusing on common robot arms with similar workspaces and 2-jaw grippers, we investigate the feasibility of zero-shot transfer.

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** To summarize, our key contributions are:
- **p. 1 / Abstract - extractive body cue:** To address robot visual disparities for vision-based policies, we introduce Mirage, which uses "cross-painting"-masking out the unseen target robot and inpainting the seen source robot-during ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Through extensive experiments on 9 manipulation tasks in both simulation and real across 6 different robot and gripper setups, we show that Mirage, despite its ...

## Source Evidence Cues

- **p. 4 / 4) We assume that the background and lighting conditions - extractive body cue:** Given a source policy action aS t+1 = πS(sS t , oS t ), we would like to transform it into a target policy action ...
- **p. 4 / 4) We assume that the background and lighting conditions - extractive body cue:** We consider the setting where there is a policy πS trained on a dataset of the source robot D = {(sS 1 , oS 1 ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** To handle differences in control gains, Mirage pairs the source robot policy with a forward dynamics model and executes the action predicted by the policy ...
- **p. 1 / 2 Google DeepMind - extractive body cue:** The target robot then uses a forward dynamics model to obtain the desired end effector pose in the target robot frame and executes the steps ...
- **p. 8 / 2) Can Mirage successfully zero-shot transfer trained vision - extractive body cue:** We use a per-dimension linear forward dynamics model and use the demonstration data to fit the regression coefficients.
- **p. 6 / 2) Can Mirage successfully zero-shot transfer trained vision - extractive body cue:** IV, we first train the source robot policies with behavior cloning (BC-RNN) on the provided demonstration data for each task (200 demos for Lift and ...
- **p. 8 / 2) Can Mirage successfully zero-shot transfer trained vision - extractive body cue:** Policies Tasks Tiger (Robotiq) Drawer (Franka) Source T Grip Source T Grip Wrist Camera Only: πS (Diffusion Policy) 90% 0% 70% 0% πS + Cross-Painting ...
- **Detected method headings:** VI. VISION-BASED POLICY TRANSFER EXPERIMENTS (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Given a source policy action aS t+1 = πS(sS t , oS t ), we would like to transform it into a ... | p. 4 (4) We assume that the background and lighting conditions), p. 4 (4) We assume that the background and lighting conditions) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | We consider the setting where there is a policy πS trained on a dataset of the source robot D = {(sS 1 ... | p. 4 (4) We assume that the background and lighting conditions), p. 2 (I. INTRODUCTION) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | To handle differences in control gains, Mirage pairs the source robot policy with a forward dynamics model and executes the action predicted ... | p. 2 (I. INTRODUCTION), p. 1 (2 Google DeepMind) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / Abstract - extractive body cue:** Focusing on common robot arms with similar workspaces and 2-jaw grippers, we investigate the feasibility of zero-shot transfer.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Given, source, policy, action, would, like, transform, target, takes, inputs, states, observations, robot, without | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | Given, source, policy, action, would, like, transform, target, takes, inputs | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | summarize, contributions, address, robot, visual, disparities, vision-based, policies, introduce, Mirage | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | Focusing, common, robot, arms, similar, workspaces, grippers, investigate, feasibility, zero-shot | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 4) We assume that the background and lighting conditions - extractive body cue:** Given a source policy action aS t+1 = πS(sS t , oS t ), we would like to transform it into a target policy action ...
- **p. 4 / 4) We assume that the background and lighting conditions - extractive body cue:** We consider the setting where there is a policy πS trained on a dataset of the source robot D = {(sS 1 , oS 1 ...
- **p. 3 / III. PROBLEM STATEMENT - extractive body cue:** Prior work [108] has found aligning the action and observation spaces can facilitate policy transfer.
- **p. 7 / 2) Can Mirage successfully zero-shot transfer trained vision - extractive body cue:** For each task and robot arm combination, the source BC-RNN policy uses only the images as inputs. "Oracle" assumes access to a ground truth rendering ...
- **p. 8 / 2) Can Mirage successfully zero-shot transfer trained vision - extractive body cue:** Policies Tasks Tiger in Bowl (Robotiq) Open Drawer (Franka) Stack Cup (Franka) Toaster (Robotiq) Source T Grip T Rob Source T Grip T Rob Source ...
- **p. 7 / 2) Can Mirage successfully zero-shot transfer trained vision - extractive body cue:** For each task, the top row shows the actual observations of the target robot during the trajectory rollout, and the bottom row shows the cross-painted ...
- **p. 1 / Abstract - extractive body cue:** Mirage applies to both first-person and third-person camera views and policies that take in both states and images as inputs or only images as inputs.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | As the coordinate frames between robots are not necessarily the same, we use the known rigid transform T S T between the ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | At each timestep, the source robot sees the world state (pr, po) of the target environment, where pr and po are the ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | Implementation Details For Robosuite, we choose 5 tasks: Lift, Stack, Can, Two Piece Assembly, and Square. | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 4) We assume that the background and lighting conditions - extractive body cue:** We consider the setting where there is a policy πS trained on a dataset of the source robot D = {(sS 1 , oS 1 ...
- **p. 6 / 2) Can Mirage successfully zero-shot transfer trained vision - extractive body cue:** IV, we first train the source robot policies with behavior cloning (BC-RNN) on the provided demonstration data for each task (200 demos for Lift and ...
- **p. 6 / 2) Can Mirage successfully zero-shot transfer trained vision - extractive body cue:** IV, we first train the source robot policies with behavior cloning (BC-RNN) on the provided demonstration data for each task (200 demos for Lift and ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Given, source, policy, action, would, like, transform, target, takes, inputs, states, observations, robot, without, demonstration, finetuning, trajectory, data, consider, setting.
- **Relevant PDF headings:** VI. VISION-BASED POLICY TRANSFER EXPERIMENTS (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | For simulation experiments, we take into account potential occlusions between the robot and objects by comparing the pixel-wise depth values between the ... | p. 6 (IV. STATE-BASED TRANSFER EXPERIMENTS), p. 4 (IV. STATE-BASED TRANSFER EXPERIMENTS) |
| Action / skill decoding | that Mirage successfully transfers between robots and grippers on 4 manipulation tasks, suffering only minimal performance degradation from the source policy and ... | p. 2 (3) Physical experiments with Franka and UR5 demonstrating), p. 9 (Figure/Table caption) |
| Receding execution / feedback | Study Results Table I shows that when the target robots have the same gripper as the source robot, most unseen target robots ... | p. 5 (IV. STATE-BASED TRANSFER EXPERIMENTS), p. 9 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 5 / IV. STATE-BASED TRANSFER EXPERIMENTS - extractive body cue:** Bridging the Visual Gap To replace the robots, we leverage the knowledge of the robot URDFs and camera poses to perform cross-painting at test time.
- **p. 5 / IV. STATE-BASED TRANSFER EXPERIMENTS - extractive body cue:** Less robust source policies leave little room for error, while more robust ones tend to retry even if the target robot fails to grasp the ...
- **p. 9 / 2) Can Mirage successfully zero-shot transfer trained vision - extractive body cue:** On the other hand, the failure modes we observe on the different robots or grippers are all very similar to those from the source policy ...
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 6: (a) An example of camera calibration error resulting in failure to mask all of the target robot out; (b) An example of the ...
- **p. 5 / IV. STATE-BASED TRANSFER EXPERIMENTS - extractive body cue:** We see that there is a significant drop in performance, indicating that the difference in the forward dynamics between robots cannot be ignored when transferring ...
- **p. 9 / 2) Can Mirage successfully zero-shot transfer trained vision - extractive body cue:** This is not surprising as the policy is trained with matching proprioceptive values and image observations, and large offsets in the proprioceptive values correspond to ...
- **p. 2 / 3) Physical experiments with Franka and UR5 demonstrating - extractive body cue:** that Mirage successfully transfers between robots and grippers on 4 manipulation tasks, suffering only minimal performance degradation from the source policy and significantly outperforming a ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (4) We assume that the background and lighting conditions), p. 4 (4) We assume that the background and lighting conditions), p. 2 (I. INTRODUCTION), p. 1 (2 Google DeepMind), p. 8 (2) Can Mirage successfully zero-shot transfer trained vision), p. 6 (2) Can Mirage successfully zero-shot transfer trained vision), objective p. 1 (Abstract), temporal p. 4 (IV. STATE-BASED TRANSFER EXPERIMENTS), p. 4 (IV. STATE-BASED TRANSFER EXPERIMENTS), p. 1 (2 Google DeepMind), p. 5 (IV. STATE-BASED TRANSFER EXPERIMENTS), p. 6 (IV. STATE-BASED TRANSFER EXPERIMENTS), p. 6 (IV. STATE-BASED TRANSFER EXPERIMENTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (16 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Given a source policy action aS t+1 = πS(sS t , oS t ), we would like to transform it into a target policy action aT t+1 = πT (sT ... (p. 4, 4) We assume that the background and lighting conditions).
- **Objective/update evidence:** Focusing on common robot arms with similar workspaces and 2-jaw grippers, we investigate the feasibility of zero-shot transfer. (p. 1, Abstract).
- **Temporal/runtime evidence:** As the coordinate frames between robots are not necessarily the same, we use the known rigid transform T S T between the frames to convert the end-effector and object poses ... (p. 4, IV. STATE-BASED TRANSFER EXPERIMENTS).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
