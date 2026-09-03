# Method - CordViP: Correspondence-based Visuomotor Policy for Dexterous Manipulation in Real-World

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p110.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p110.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (C. Comact and Coordination-Enhanced Feature Extraction), p. 5 (C. Comact and Coordination-Enhanced Feature Extraction), p. 14 (B. Implementation Details), p. 14 (B. Implementation Details), p. 3 (A. Problem Formulation), p. 15 (B. Implementation Details)): Similarly, we also predict the action sequence of the hand using point clouds and the arm state, We use MSE loss to compute the loss between the reconstructed and original ...

## Method Body Digest

- **p. 5 / C. Comact and Coordination-Enhanced Feature Extraction - extractive body cue:** Similarly, we also predict the action sequence of the hand using point clouds and the arm state, We use MSE loss to compute the loss ...
- **p. 5 / C. Comact and Coordination-Enhanced Feature Extraction - extractive body cue:** To help the robot system learn the features of hand-arm coordination, we also propose & correspondence-based design for action prediction. ‘The arm and hand states ...
- **p. 14 / B. Implementation Details - extractive body cue:** The features are then processed through the same Transformer architecture for cross-attention, enabling feature fusion.
- **p. 14 / B. Implementation Details - extractive body cue:** Network Architecture, For point cloud encoding, we first use PointNetl41] to process point cloud data without RGB information, outputting a set of point feature vectors ...
- **p. 3 / A. Problem Formulation - extractive body cue:** In our approach, each observation o, is composed. of the object's point cloud P..), the hand's point cloud Phands and the robot's joint states, including ...
- **p. 15 / B. Implementation Details - extractive body cue:** We collect both the robot's state and actions using joint angles in radians, including the 6-DOF joints of the robotic the 16-DOF joints of the ...
- **p. 3 / A. Problem Formulation - extractive body cue:** Furthermore, leveraging these observations, we compute contact maps between the robotic hhand and the manipulated objects, as well as capture col laborative interaction information between ...
- **p. 3 / B. Interaction-aware Generation of 3D Point Clouds - extractive body cue:** On the one hand, real-world point cloud data, typically captured using stereo cameras or low-cost RGB-D scanners, suffers from geometric and semantic loss due to ...

## Design Rationale

- **p. 3 / B. Interaction-aware Generation of 3D Point Clouds - extractive body cue:** To this end, we propose the interaction-aware generation of 3D point clouds, enabling the reconstruction of crucial spatial information,
- **p. 14 / B. Implementation Details - extractive body cue:** The PointNet consists of three fully connected layers, each followed by LayerNorm for normalization and ReLU activation
- **p. 15 / B. Implementation Details - extractive body cue:** For our method, we use only RGB and depth data to track the ‘object's pose.

## Source Evidence Cues

- **p. 5 / C. Comact and Coordination-Enhanced Feature Extraction - extractive body cue:** Similarly, we also predict the action sequence of the hand using point clouds and the arm state, We use MSE loss to compute the loss ...
- **p. 5 / C. Comact and Coordination-Enhanced Feature Extraction - extractive body cue:** To help the robot system learn the features of hand-arm coordination, we also propose & correspondence-based design for action prediction. ‘The arm and hand states ...
- **p. 14 / B. Implementation Details - extractive body cue:** The features are then processed through the same Transformer architecture for cross-attention, enabling feature fusion.
- **p. 14 / B. Implementation Details - extractive body cue:** Network Architecture, For point cloud encoding, we first use PointNetl41] to process point cloud data without RGB information, outputting a set of point feature vectors ...
- **p. 3 / A. Problem Formulation - extractive body cue:** In our approach, each observation o, is composed. of the object's point cloud P..), the hand's point cloud Phands and the robot's joint states, including ...
- **p. 15 / B. Implementation Details - extractive body cue:** We collect both the robot's state and actions using joint angles in radians, including the 6-DOF joints of the robotic the 16-DOF joints of the ...
- **p. 3 / A. Problem Formulation - extractive body cue:** Furthermore, leveraging these observations, we compute contact maps between the robotic hhand and the manipulated objects, as well as capture col laborative interaction information between ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / affordance state | object와 contact-relevant scene을 표현한다 | RGB-D, point cloud, object/task observation | pose, affordance, grasp/contact graph 또는 SE(3) descriptor를 구성 | object/contact state | Similarly, we also predict the action sequence of the hand using point clouds and the arm state, We use MSE loss to ... | p. 5 (C. Comact and Coordination-Enhanced Feature Extraction), p. 5 (C. Comact and Coordination-Enhanced Feature Extraction) |
| Grasp / trajectory generation | goal을 feasible manipulation candidate로 바꾼다 | geometry/contact state와 task goal | grasp sampling, pose planning, trajectory optimization 또는 policy decoding을 적용 | grasp, pose, force 또는 trajectory | To help the robot system learn the features of hand-arm coordination, we also propose & correspondence-based design for action prediction. ‘The arm ... | p. 5 (C. Comact and Coordination-Enhanced Feature Extraction), p. 14 (B. Implementation Details) |
| Contact execution / correction | interaction outcome으로 action을 닫힌 loop로 수정한다 | candidate와 visual/force/tactile feedback | tracking, regrasp, correction, termination 또는 recovery를 수행 | next action/task state | The features are then processed through the same Transformer architecture for cross-attention, enabling feature fusion. | p. 14 (B. Implementation Details), p. 14 (B. Implementation Details) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / B. Interaction-aware Generation of 3D Point Clouds - extractive body cue:** On the one hand, real-world point cloud data, typically captured using stereo cameras or low-cost RGB-D scanners, suffers from geometric and semantic loss due to ...
- **p. 5 / C. Comact and Coordination-Enhanced Feature Extraction - extractive body cue:** Given the aforementioned losses, our overall training objective during the pre-training phase is defined as:
- **p. 3 / B. Interaction-aware Generation of 3D Point Clouds - extractive body cue:** On the other hand, during. dexterous manipulation with multi-fingered hands, occlusions frequently occur, resulting in the loss of critical contact and interaction information, which is ...
- **p. 5 / C. Comact and Coordination-Enhanced Feature Extraction - extractive body cue:** The MSE loss is calculated between C and cvred.
- **p. 15 / B. Implementation Details - extractive body cue:** Contact map size rose ‘Loss weight 0 1 horizon 2 nob steps 4 action steps 6
- **Formal bridge:** object geometry/contact state -> grasp/pose/force/trajectory -> task/contact/pose objective -> completion, contact success and robustness.
- **Equation/algorithm anchors:** p. 5 (C. Comact and Coordination-Enhanced Feature Extraction), p. 3 (B. Interaction-aware Generation of 3D Point Clouds), p. 3 (B. Interaction-aware Generation of 3D Point Clouds), p. 5 (C. Comact and Coordination-Enhanced Feature Extraction), p. 15 (B. Implementation Details).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | observation, composed, object, point, cloud, hand, Phands, robot, joint, states, including, Dof, configuration, BCRNNSD | RGB-D/point cloud, object state와 contact/task observation | body cue; exact tensor/frame verify |
| State/latent | observation, composed, object, point, cloud, hand, Phands, robot, joint, states | object geometry, affordance, contact mode 또는 end-effector state | body cue; notation verify |
| Action/output | interaction-aware, generation, point, clouds, enabling, reconstruction, crucial, spatial, information, PointNet | grasp, pose, force 또는 end-effector trajectory | body cue; unit/decoder verify |
| Objective/constraint | hand, real-world, point, cloud, data, typically, captured, stereo, cameras, low-cost | task/contact/pose objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / A. Problem Formulation - extractive body cue:** In our approach, each observation o, is composed. of the object's point cloud P..), the hand's point cloud Phands and the robot's joint states, including ...
- **p. 15 / B. Implementation Details - extractive body cue:** ‘The BCRNNSD is trained for 3000 epochs with horizon=10, n_obs_steps=1, n_action_steps=l, where the observations are replaced from images to point clouds.
- **p. 4 / C. Comact and Coordination-Enhanced Feature Extraction - extractive body cue:** Interaction-aware Generation of 3D Point Clouds provides us with accurate and complete point cloud observation.
- **p. 5 / C. Comact and Coordination-Enhanced Feature Extraction - extractive body cue:** We predict, the action sequence of the robot arm based on the point clouds and the state of the hand.
- **p. 15 / B. Implementation Details - extractive body cue:** The 3D Diffusion Policy is trained for $000 epochs with horizon=12, n_obs_steps=4, n_action_steps=8, Ituses DP3 Encoder as the point cloud encoder.
- **p. 3 / A. Problem Formulation - extractive body cue:** robot's observations and A represents the corresponding actions, allowing the robot to generalize beyond the taining data distribution.
- **p. 5 / C. Comact and Coordination-Enhanced Feature Extraction - extractive body cue:** To help the robot system learn the features of hand-arm coordination, we also propose & correspondence-based design for action prediction. ‘The arm and hand states ...
- **Normalized interface:** observation=RGB-D/point cloud, object state와 contact/task observation; state=object geometry, affordance, contact mode 또는 end-effector state; output/action=grasp, pose, force 또는 end-effector trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | grasp/pose proposal에서 contact episode까지의 task horizon; trajectory chunk 여부 확인 필요. | The episode length of each task will be limited to a maximum of 500 steps and ‘each task is evaluated with 20 ... | episode/sequence/action-chunk boundary |
| Rate / latency | perception/planning rate와 low-level contact control rate가 분리된다. | Contact map size rose ‘Loss weight 0 1 horizon 2 nob steps 4 action steps 6 | Hz/fps, inference time and control rate |
| Memory | object/contact state, current pose와 tactile/force history; exact window 확인 필요. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | point/pose encoding, candidate sampling/optimization과 collision/contact checking이 결정한다. | The episode length of each task will be limited to a maximum of 500 steps and ‘each task is evaluated with 20 ... | hardware, batch and throughput |

## Training vs Inference

- **p. 15 / B. Implementation Details - extractive body cue:** The 3D Diffusion Policy is trained for $000 epochs with horizon=12, n_obs_steps=4, n_action_steps=8, Ituses DP3 Encoder as the point cloud encoder.
- **p. 15 / B. Implementation Details - extractive body cue:** For BCRNN, we train the model for 1500 epochs with horizon=10, n_obs_steps=1, n_action_ste}

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Similarly, predict, action, sequence, hand, point, clouds, state, MSE, loss, compute, between, reconstructed, original, further, predicting, respectively, encoder, able, learn.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / affordance state | ‘We conduct comprehensive real-world experiments to answer the following questions: | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Grasp / trajectory generation | The Diffusion Policy baseline utilizes ResNetI8 as the visual encoder and employs CNN-based backbones. | p. 15 (B. Implementation Details), p. 15 (B. Implementation Details) |
| Contact execution / correction | Fig. 1: We propose CordViP, a correspondence-based visuomotor policy for dexterous manipulation in the real world. (a) Left: We present the interaction-aware ... | p. 1 (Figure/Table caption), p. 5 (IV. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 14 / B. Implementation Details - extractive body cue:** Network Architecture, For point cloud encoding, we first use PointNetl41] to process point cloud data without RGB information, outputting a set of point feature vectors ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** ‘+ What role does each of the system components play enhancing its overall performance (Section IV-E, IV-F)?
- **p. 15 / B. Implementation Details - extractive body cue:** Point clouds are used to replace the original image inputs.
- **p. 15 / B. Implementation Details - extractive body cue:** ‘The BCRNNSD is trained for 3000 epochs with horizon=10, n_obs_steps=1, n_action_steps=l, where the observations are replaced from images to point clouds.
- **p. 10 / V. CONCLUSIONS AND LimiTATIONS - extractive body cue:** Despite the exceptional performance demonstrated by CordViP, there are still certain limitations that could be explored in future work.
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 8: Failure case. (a) Case / is a failure case from the
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We propose CordViP, a correspondence-based visuomotor policy for dexterous manipulation in the real world. (a) Left: We present the interaction-aware point clouds, which ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (C. Comact and Coordination-Enhanced Feature Extraction), p. 5 (C. Comact and Coordination-Enhanced Feature Extraction), p. 14 (B. Implementation Details), p. 14 (B. Implementation Details), p. 3 (A. Problem Formulation), p. 15 (B. Implementation Details), objective p. 3 (B. Interaction-aware Generation of 3D Point Clouds), p. 5 (C. Comact and Coordination-Enhanced Feature Extraction), p. 3 (B. Interaction-aware Generation of 3D Point Clouds), p. 5 (C. Comact and Coordination-Enhanced Feature Extraction), p. 15 (B. Implementation Details), temporal p. 6 (A. Experiment Setup), p. 15 (B. Implementation Details), p. 15 (B. Implementation Details), p. 5 (IV. EXPERIMENTS), p. 6 (6) LongHforiManip. ‘This task involves four sequential), p. 10 (C. Efficiency).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Similarly, we also predict the action sequence of the hand using point clouds and the arm state, We use MSE loss to compute the loss between the reconstructed and original ... (p. 5, C. Comact and Coordination-Enhanced Feature Extraction).
- **Objective/update evidence:** On the one hand, real-world point cloud data, typically captured using stereo cameras or low-cost RGB-D scanners, suffers from geometric and semantic loss due to factors such as light reflection, ... (p. 3, B. Interaction-aware Generation of 3D Point Clouds).
- **Temporal/runtime evidence:** The episode length of each task will be limited to a maximum of 500 steps and ‘each task is evaluated with 20 trials by default. (p. 6, A. Experiment Setup).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
