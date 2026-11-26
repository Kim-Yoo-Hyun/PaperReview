# Method - Flying Hand: End-Effector-Centric Framework for Versatile Aerial Manipulation Teleoperation and Policy Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p130.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p130.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 7 (B. EE-Centrie Policy Learning), p. 10 (B. Implementation Details), p. 7 (B. EE-Centrie Policy Learning), p. 10 (B. Implementation Details), p. 6 (A. End-Effector-Centric Model Predictive Controller), p. 6 (A. End-Effector-Centric Model Predictive Controller)): The transformerbased decoder generates action sequences from the latent variable (only during training and set to be the mean of the prior during testing), current joint observations, and encoded image ...

## Method Body Digest

- **p. 7 / B. EE-Centrie Policy Learning - extractive body cue:** The transformerbased decoder generates action sequences from the latent variable (only during training and set to be the mean of the prior during testing), current ...
- **p. 10 / B. Implementation Details - extractive body cue:** ‘To show the advantage of leaming from an ee-centric demonstration compared to a joint space demonstration, we use the same demonstration trajectory but change the ...
- **p. 7 / B. EE-Centrie Policy Learning - extractive body cue:** ACT utilizes a Conditional Variational Autoencoder (CVAE) where the encoder compresses action sequences and Joint observations into a latent style variable.
- **p. 10 / B. Implementation Details - extractive body cue:** After that, we train a joint space ACT policy with the same training setting as the ee-centric ACT policy, except that the end-effector pose in ...
- **p. 6 / A. End-Effector-Centric Model Predictive Controller - extractive body cue:** Eq, (10a) defines the optimization objective, where HT represents the discrete prediction horizon.
- **p. 6 / A. End-Effector-Centric Model Predictive Controller - extractive body cue:** Eq, (106) enforces the discrete-time system dynamics, incorporating the fully actuated UAV dynamics Eq.
- **p. 8 / B. Implementation Details - extractive body cue:** Ll (green) exhibits overshoot in the X and Z axes and bias in Y, indicating that the L1 controller effectively mitigates both transient and steady-state ...
- **p. 6 / A. End-Effector-Centric Model Predictive Controller - extractive body cue:** ‘The MPC formulation minimizes a cost function over a finite time horizon H while subject to system dynamics and constraints:

## Design Rationale

- **p. 1 / Abstract - extractive body cue:** Our framework consists of a fully-actuated hexarotor with a 4:DoF robotic arm, an end-effector-centrie whole-body: model predictive controller, and a high-level po is end-effector controller ...
- **p. 7 / VII. EE-CENTRIC TELEOPERATION AND POLICY - extractive body cue:** [As we mentioned, our framework enables the decoupling between the high-level policy and low-level controller, with the ee-centric interface serving asthe sole connection between them.
- **p. 2 / B. Mobile Manipulation Framework and EE-Centric Interface - extractive body cue:** [25] proposed a framework that consists of a robust humanoid whole-body controller with a high-level policy, either an autonomous agent like GPT-40 or an imitation ...

## Source Evidence Cues

- **p. 7 / B. EE-Centrie Policy Learning - extractive body cue:** The transformerbased decoder generates action sequences from the latent variable (only during training and set to be the mean of the prior during testing), current ...
- **p. 10 / B. Implementation Details - extractive body cue:** ‘To show the advantage of leaming from an ee-centric demonstration compared to a joint space demonstration, we use the same demonstration trajectory but change the ...
- **p. 7 / B. EE-Centrie Policy Learning - extractive body cue:** ACT utilizes a Conditional Variational Autoencoder (CVAE) where the encoder compresses action sequences and Joint observations into a latent style variable.
- **p. 10 / B. Implementation Details - extractive body cue:** After that, we train a joint space ACT policy with the same training setting as the ee-centric ACT policy, except that the end-effector pose in ...
- **p. 6 / A. End-Effector-Centric Model Predictive Controller - extractive body cue:** Eq, (10a) defines the optimization objective, where HT represents the discrete prediction horizon.
- **p. 6 / A. End-Effector-Centric Model Predictive Controller - extractive body cue:** Eq, (106) enforces the discrete-time system dynamics, incorporating the fully actuated UAV dynamics Eq.
- **p. 8 / B. Implementation Details - extractive body cue:** Ll (green) exhibits overshoot in the X and Z axes and bias in Y, indicating that the L1 controller effectively mitigates both transient and steady-state ...
- **Detected method headings:** A. End-Effector-Centric Model Predictive Controller (p. 6); VII. EE-CENTRIC TELEOPERATION AND POLICY (p. 7); B. EE-Centrie Policy Learning (p. 7); B. Policy Learning with Less Accurate State Estimation (p. 16)

## Pipeline

말단 상태와 기체·말단의 RGB 영상 → 말단 목표 자세와 결합 기체·팔 동역학 → ACT의 목표 말단 자세와 MPC의 기체·팔 명령. [방법·평가의 원문 근거](./01_overview.md#observation-state-and-output-interface)

## Objective / Update Rule

- **p. 6 / A. End-Effector-Centric Model Predictive Controller - extractive body cue:** ‘The MPC formulation minimizes a cost function over a finite time horizon H while subject to system dynamics and constraints:
- **p. 6 / A. End-Effector-Centric Model Predictive Controller - extractive body cue:** Eq, (10a) defines the optimization objective, where HT represents the discrete prediction horizon.
- **p. 8 / B. Implementation Details - extractive body cue:** ‘We also investigate the contribution of arm flexibility to endeffector tracking performance by increasing the arm control cost 5 times.
- **p. 9 / B. Implementation Details - extractive body cue:** 11, human teleoperators can easily achieve all aerial manipulation tasks with little learning and operation cost.
- **p. 10 / B. Implementation Details - extractive body cue:** After training, wwe choose the policy with the least validation loss to perform 50 evaluation trials.
- **p. 11 / B. Implementation Details - extractive body cue:** After training through 100,000 epochs, the policy with the least validation loss is selected.
- **Formal bridge:** 말단 상태와 기체·말단의 RGB 영상 → 말단 목표 자세와 결합 기체·팔 동역학 → ACT의 목표 말단 자세와 MPC의 기체·팔 명령.
- **Equation/algorithm anchors:** p. 6 (A. End-Effector-Centric Model Predictive Controller), p. 6 (A. End-Effector-Centric Model Predictive Controller), p. 10 (B. Implementation Details), p. 11 (B. Implementation Details).

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | After, train, joint, space, ACT, policy, same, training, setting, ee-centric, except, end-effector, pose, observation | 말단 상태와 기체·말단의 RGB 영상 | body cue; exact tensor/frame verify |
| State/latent | After, train, joint, space, ACT, policy, same, training, setting, ee-centric | 말단 목표 자세와 결합 기체·팔 동역학 | body cue; notation verify |
| Action/output | framework, consists, fully-actuated, hexarotor, DoF, robotic, end-effector-centrie, whole-body, model, predictive | ACT의 목표 말단 자세와 MPC의 기체·팔 명령 | body cue; unit/decoder verify |
| Objective/constraint | MPC, formulation, minimizes, cost, function, over, finite, time, horizon, while | tracking/balance/task objective | equation anchor required |

## Observation–State–Action Interface

- **p. 10 / B. Implementation Details - extractive body cue:** After that, we train a joint space ACT policy with the same training setting as the ee-centric ACT policy, except that the end-effector pose in ...
- **p. 4 / C. Teleportation and Imitation Learning - extractive body cue:** At the most highlevel, the ee-centric policy module gets current observations and generates the target end-effector states online without the need to consider the specific ...
- **p. 2 / B. Mobile Manipulation Framework and EE-Centric Interface - extractive body cue:** [57] proposed a hierarchical framework that consists of the understanding module, a pre~ trained large visual-language model running in low-frequency. and the execution modale, a ...
- **p. 7 / B. EE-Centrie Policy Learning - extractive body cue:** The transformerbased decoder generates action sequences from the latent variable (only during training and set to be the mean of the prior during testing), current ...
- **p. 8 / B. Implementation Details - extractive body cue:** ‘To further analyze the contribution of the L adaptive control, specifically its effectiveness in handling model mismatch and interaction disturbance, we visualized the base external ...
- **p. 2 / 1. Iyrropuction - extractive body cue:** The framework consists of a versatile aerial manipulation platform capable ‘of executing multiple tasks, a policy-agnostic controller that precisely tracks the target end-effector state, and ...
- **p. 3 / C. Teleportation and Imitation Learning - extractive body cue:** the Human teleoperation of learned autonemnous policy. sends the target eadetfector state to eecentic MPC, which then generates
- **Normalized interface:** observation=말단 상태와 기체·말단의 RGB 영상; state=말단 목표 자세와 결합 기체·팔 동역학; output/action=ACT의 목표 말단 자세와 MPC의 기체·팔 명령.

## Temporal and Runtime Contract

| Contract | PDF body cue | Unresolved detail |
|---|---|---|
| Horizon | ‘The optimal control problem in the ee-centric MPC is implemented using ACADOS [51] with a 25ms discretisation step and a 2.5s constant ... | episode/sequence/action-chunk boundary |
| Rate / latency | Horizon Length Horizoa Steps NV State Cost Qy Rotation Cost Qe. | Hz/fps, inference time and control rate |
| Memory | not stated or recoverable in the selected PDF body | window and reset |
| Compute | ‘The optimal control problem in the ee-centric MPC is implemented using ACADOS [51] with a 25ms discretisation step and a 2.5s constant ... | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / B. EE-Centrie Policy Learning - extractive body cue:** The transformerbased decoder generates action sequences from the latent variable (only during training and set to be the mean of the prior during testing), current ...
- **p. 10 / B. Implementation Details - extractive body cue:** After that, we train a joint space ACT policy with the same training setting as the ee-centric ACT policy, except that the end-effector pose in ...
- **p. 10 / B. Implementation Details - extractive body cue:** After training, wwe choose the policy with the least validation loss to perform 50 evaluation trials.
- **p. 11 / B. Implementation Details - extractive body cue:** After training through 100,000 epochs, the policy with the least validation loss is selected.

## Method-Specific Formal Details

- **Body-defined terms:** transformerbased, decoder, generates, action, sequences, latent, variable, only, during, training, mean, prior, testing, current, joint, observations, encoded, image, features, advantage.
- **Relevant PDF headings:** A. End-Effector-Centric Model Predictive Controller (p. 6); VII. EE-CENTRIC TELEOPERATION AND POLICY (p. 7); B. EE-Centrie Policy Learning (p. 7); B. Policy Learning with Less Accurate State Estimation (p. 16).

## Evaluation Link

| 평가 근거 | 원문에서 추출한 내용 | 원문 위치 |
|---|---|---|
| 원문 대조 | Some work also showed amazing results, achieving high-speed grasping, or grasping moving objects [50], but sacrificed payload capacity or precision due to ... | p. 2 (4) Rich real-world experiments demonstrated the versatility), p. 2 (4) Rich real-world experiments demonstrated the versatility) |
| 원문 대조 | 4, compared with our method (blue), the baseline wo. | p. 8 (B. Implementation Details), p. 7 (A. Experimental Setup) |
| 원문 대조 | improvements can be achieved through more accurate system modeling and higher-precision hardware to enhance tracking accuracy. | p. 9 (B. Implementation Details), p. 10 (B. Implementation Details) |

## Failure and Ablation Link

- **p. 7 / A. Experimental Setup - extractive body cue:** MPC: This baseline replaces the ee-centric MPC with the Direct Force Feedback Control(DEFC) method from [38]. which directly controls the end-effector acceleration based on the ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3. UAM hardware system design, ilustaing the key components: () faly-scusted hexaroor as the base sructre, (2) 4 Dof manialator, (3) Intel RealSease cameras ...
- **p. 9 / B. Implementation Details - extractive body cue:** 6 Arm flexibility ablation study for MPC contol.
- **p. 10 / B. Implementation Details - extractive body cue:** with our ee-centric interface, we do not consider any joint configuration when collecting demonstrations, which allows us to efficiently collect smooth demonstrations without tediously adjusting ...
- **p. 10 / B. Implementation Details - extractive body cue:** After that, we train a joint space ACT policy with the same training setting as the ee-centric ACT policy, except that the end-effector pose in ...
- **p. 7 / A. Experimental Setup - extractive body cue:** LI: This baseline excludes the L1 adaptive component, leaving disturbances from UAV and manipulator interactions and modeling uncertainties uncompensated during control execution.
- **p. 11 / IX. LIMITATIONS - extractive body cue:** Although we have demonstrated the proposed framework through various real-world experiments, there are still several limitations due to time constraints and methodological limitations.

## Reproduction Checklist

[공통 검토 기준](../../../research/READING_STATUS.md#note-checks)

## Verification Questions

- **Evidence anchors reviewed:** method p. 7 (B. EE-Centrie Policy Learning), p. 10 (B. Implementation Details), p. 7 (B. EE-Centrie Policy Learning), p. 10 (B. Implementation Details), p. 6 (A. End-Effector-Centric Model Predictive Controller), p. 6 (A. End-Effector-Centric Model Predictive Controller), objective p. 6 (A. End-Effector-Centric Model Predictive Controller), p. 6 (A. End-Effector-Centric Model Predictive Controller), p. 8 (B. Implementation Details), p. 9 (B. Implementation Details), p. 10 (B. Implementation Details), p. 11 (B. Implementation Details), temporal p. 8 (B. Implementation Details), p. 8 (A. Experimental Setup), p. 10 (B. Implementation Details), p. 10 (B. Implementation Details), p. 2 (4) Rich real-world experiments demonstrated the versatility), p. 2 (4) Rich real-world experiments demonstrated the versatility).

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (16 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** The transformerbased decoder generates action sequences from the latent variable (only during training and set to be the mean of the prior during testing), current joint observations, and encoded image ... (p. 7, B. EE-Centrie Policy Learning).
- **Objective/update evidence:** Eq, (10a) defines the optimization objective, where HT represents the discrete prediction horizon. (p. 6, A. End-Effector-Centric Model Predictive Controller).
- **Temporal/runtime evidence:** ‘The optimal control problem in the ee-centric MPC is implemented using ACADOS [51] with a 25ms discretisation step and a 2.5s constant prediction horizon, running in 100 Hz, and other ... (p. 8, B. Implementation Details).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
