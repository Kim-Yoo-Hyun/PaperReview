# Method - DemoGen: Synthetic Demonstration Generation for Data-Efficient Visuomotor Policy Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (20 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p157.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p157.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 17 (A. Policy Training and Implementation Details), p. 17 (A. Policy Training and Implementation Details), p. 4 (A. Problem Formulation), p. 4 (A. Problem Formulation), p. 5 (A. Problem Formulation), p. 6 (C. TAMP-based Action Generation)): In real-world experiments, we use the DBSCAN [15] elustering algorithm to discard the outlier points and downsample the number of points in the point cloud observations to 1024 In the ...

## Method Body Digest

- **p. 17 / A. Policy Training and Implementation Details - extractive body cue:** In real-world experiments, we use the DBSCAN [15] elustering algorithm to discard the outlier points and downsample the number of points in the point cloud ...
- **p. 17 / A. Policy Training and Implementation Details - extractive body cue:** 1) Details for Policy Training: Fora fair comparison, we fix the total training steps counted by observation-action pairs to be 2M for all evaluated settings, ...
- **p. 4 / A. Problem Formulation - extractive body cue:** The action a, consists of the robot arm and robot hhand commands, represented as a - (a""a!!™), where a7" © AP" is the target SE(3) ...
- **p. 4 / A. Problem Formulation - extractive body cue:** A visuomotor policy + : O +> A directly maps the visual observations 0 < © to the predicted actions « cA.
- **p. 5 / A. Problem Formulation - extractive body cue:** The observation: or includes both the point cloud data and the proprioceptive feedback from the robot: 0 = (of, of", of), where of?" and 0} ...
- **p. 6 / C. TAMP-based Action Generation - extractive body cue:** It is noteworthy that we found directly replacing the current state with the next target pose action (ie., 07°" < aj) ‘may impair performance, asthe ...
- **p. 6 / C. TAMP-based Action Generation - extractive body cue:** The observations consist of point cloud data and proprioceptive states.
- **p. 6 / C. TAMP-based Action Generation - extractive body cue:** Empirically, these adjustments are found to help minimize compounding control errors, contributing to the successful execution of the generated actions.

## Design Rationale

- **p. 4 / A. Problem Formulation - extractive body cue:** The action a, consists of the robot arm and robot hhand commands, represented as a - (a""a!!™), where a7" © AP" is the target SE(3) ...

## Source Evidence Cues

- **p. 17 / A. Policy Training and Implementation Details - extractive body cue:** In real-world experiments, we use the DBSCAN [15] elustering algorithm to discard the outlier points and downsample the number of points in the point cloud ...
- **p. 17 / A. Policy Training and Implementation Details - extractive body cue:** 1) Details for Policy Training: Fora fair comparison, we fix the total training steps counted by observation-action pairs to be 2M for all evaluated settings, ...
- **p. 4 / A. Problem Formulation - extractive body cue:** The action a, consists of the robot arm and robot hhand commands, represented as a - (a""a!!™), where a7" © AP" is the target SE(3) ...
- **p. 4 / A. Problem Formulation - extractive body cue:** A visuomotor policy + : O +> A directly maps the visual observations 0 < © to the predicted actions « cA.
- **p. 5 / A. Problem Formulation - extractive body cue:** The observation: or includes both the point cloud data and the proprioceptive feedback from the robot: 0 = (of, of", of), where of?" and 0} ...
- **p. 6 / C. TAMP-based Action Generation - extractive body cue:** It is noteworthy that we found directly replacing the current state with the next target pose action (ie., 07°" < aj) ‘may impair performance, asthe ...
- **p. 6 / C. TAMP-based Action Generation - extractive body cue:** The observations consist of point cloud data and proprioceptive states.
- **Detected method headings:** A. Policy Training and Implementation Details (p. 17)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Demonstration representation | expert trajectory를 training pair/context로 정렬한다 | observation history, goal, expert action | temporal alignment, relabeling 또는 latent context construction을 수행 | training sample/context | In real-world experiments, we use the DBSCAN [15] elustering algorithm to discard the outlier points and downsample the number of points in ... | p. 17 (A. Policy Training and Implementation Details), p. 17 (A. Policy Training and Implementation Details) |
| Policy fitting | expert action distribution을 학습한다 | context와 action target | behavior cloning, adversarial, sequence, diffusion 또는 flow objective를 최적화 | policy/action distribution | 1) Details for Policy Training: Fora fair comparison, we fix the total training steps counted by observation-action pairs to be 2M for ... | p. 17 (A. Policy Training and Implementation Details), p. 4 (A. Problem Formulation) |
| Closed-loop rollout | distribution shift와 recovery를 확인한다 | current observation/history | action/chunk을 실행하고 feedback으로 다음 prediction을 갱신 | trajectory/failure signal | The action a, consists of the robot arm and robot hhand commands, represented as a - (a""a!!™), where a7" © AP" is ... | p. 4 (A. Problem Formulation), p. 4 (A. Problem Formulation) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 17 / A. Policy Training and Implementation Details - extractive body cue:** 1) Details for Policy Training: Fora fair comparison, we fix the total training steps counted by observation-action pairs to be 2M for all evaluated settings, ...
- **p. 6 / C. TAMP-based Action Generation - extractive body cue:** Empirically, these adjustments are found to help minimize compounding control errors, contributing to the successful execution of the generated actions.
- **p. 17 / A. Policy Training and Implementation Details - extractive body cue:** To stabilize the training process, we use AdamW [32] optimizer and set the learning rate to be Le with a 500 step warmup.
- **Formal bridge:** observation history o_{t−H:t} -> expert-like action/chunk a_{t:t+H} -> imitation or action-distribution loss -> closed-loop task success and robustness.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | observation, includes, point, cloud, data, proprioceptive, feedback, robot, where, reflect, current, state, end-effector, same | observation history와 expert trajectory/action | body cue; exact tensor/frame verify |
| State/latent | observation, includes, point, cloud, data, proprioceptive, feedback, robot, where, reflect | behavior policy와 temporal action context | body cue; notation verify |
| Action/output | action, consists, robot, hhand, commands, represented, where, target, end-effector, pose | predicted action 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | Details, Policy, Training, Fora, fair, comparison, total, steps, counted, observation-action | imitation or action-distribution loss | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / A. Problem Formulation - extractive body cue:** The observation: or includes both the point cloud data and the proprioceptive feedback from the robot: 0 = (of, of", of), where of?" and 0} ...
- **p. 4 / A. Problem Formulation - extractive body cue:** A visuomotor policy + : O +> A directly maps the visual observations 0 < © to the predicted actions « cA.
- **p. 17 / A. Policy Training and Implementation Details - extractive body cue:** 1) Details for Policy Training: Fora fair comparison, we fix the total training steps counted by observation-action pairs to be 2M for all evaluated settings, ...
- **p. 17 / A. Policy Training and Implementation Details - extractive body cue:** We follow the notation in the Diffusion Policy [8] paper, where T, denotes the observation horizon, 7; as the action pre~ diction horizon, and T, ...
- **p. 6 / C. TAMP-based Action Generation - extractive body cue:** The observations consist of point cloud data and proprioceptive states.
- **p. 6 / C. TAMP-based Action Generation - extractive body cue:** It is noteworthy that we found directly replacing the current state with the next target pose action (ie., 07°" < aj) ‘may impair performance, asthe ...
- **p. 4 / A. Problem Formulation - extractive body cue:** The action a, consists of the robot arm and robot hhand commands, represented as a - (a""a!!™), where a7" © AP" is the target SE(3) ...
- **Normalized interface:** observation=observation history와 expert trajectory/action; state=behavior policy와 temporal action context; output/action=predicted action 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single-step 또는 action chunk/trajectory horizon; exact chunk length는 exact value not recovered from the selected body cues. | Since Ts indicates the steps of actions executed on the robot without re-planning, our horizon settings result in a closed-loop re-planning latency ... | episode/sequence/action-chunk boundary |
| Rate / latency | training inference와 deployed control tick을 분리; action chunk면 receding execution 여부 확인. | Specifically, assuming the task involves the sequential manipulation of A' objects {O1,O2,...,Ox}. the initial object configuration sp is defined as the set ... | Hz/fps, inference time and control rate |
| Memory | current observation, temporal history 또는 recurrent/sequence context. | not recovered | window and reset |
| Compute | backbone/decoder inference, sampling steps와 action horizon이 latency를 결정한다. | To stabilize the training process, we use AdamW [32] optimizer and set the learning rate to be Le with a 500 step ... | hardware, batch and throughput |

## Training vs Inference

- **p. 17 / A. Policy Training and Implementation Details - extractive body cue:** 1) Details for Policy Training: Fora fair comparison, we fix the total training steps counted by observation-action pairs to be 2M for all evaluated settings, ...
- **p. 17 / A. Policy Training and Implementation Details - extractive body cue:** To stabilize the training process, we use AdamW [32] optimizer and set the learning rate to be Le with a 500 step warmup.
- **p. 17 / A. Policy Training and Implementation Details - extractive body cue:** We list the training and ‘implementation details as follows,
- **p. 4 / B. Benchmarking Spatial Generalization Capability - extractive body cue:** On the other hand, both 3D representations and pre-trained 2D visual encoders contribute to improved spatial generalization capabilities.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** real-world, experiments, DBSCAN, elustering, algorithm, discard, outlier, points, downsample, number, point, cloud, observations, simulator, skip, clustering, stage, clouds, Details, Policy.
- **Relevant PDF headings:** A. Policy Training and Implementation Details (p. 17).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Demonstration representation | In the following benchmarking, we explore the relationship between the number of demonstrations and policy performance to determine how many demonstrations are ... | p. 4 (B. Benchmarking Spatial Generalization Capability), p. 4 (B. Benchmarking Spatial Generalization Capability) |
| Policy fitting | Fig. 22: Raw evaluation results in the Sauce-Spreading task. (Top) Examples of the processing results for metric calculation. (Bottom) Compared with the ... | p. 18 (Figure/Table caption), p. 17 (A. Policy Training and Implementation Details) |
| Closed-loop rollout | We report the relationship between the agent's performance Jn success rates and the number of demonstrations used for traning ‘when different visuomotor ... | p. 4 (B. Benchmarking Spatial Generalization Capability), p. 18 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 17 / A. Policy Training and Implementation Details - extractive body cue:** Since Ts indicates the steps of actions executed on the robot without re-planning, our horizon settings result in a closed-loop re-planning latency of 0.5 seconds. ...
- **p. 4 / B. Benchmarking Spatial Generalization Capability - extractive body cue:** Specifically, we replace the train-fromscratch ResNet [21] encoder in DP with pre-trained encoders including R3M [35], DINOv2 [36], and CLIP [41].
- **p. 17 / A. Policy Training and Implementation Details - extractive body cue:** 2) Pre-Trained Encoders for Diffusion Policies: To replace the train-from-scratch ResNetl8 [21] visual encoder in the original Diffusion Policy architecture, we consider 3. representative pre-trained ...
- **p. 12 / B. Obstacle Avoidance - extractive body cue:** Trained on the source demonstrations without obstacles, the visuomotor policy fails to account for potential collisions, e.g., it might knock over the coffee cup placed ...
- **p. 12 / B. Obstacle Avoidance - extractive body cue:** Obstacle-avoiding trajectories are generated by a motion planning tool [28], ensuring collision-free actions.
- **p. 11 / B. Cluttered Scene - extractive body cue:** When the scene becomes even more complex, e.g. clutter, DemoGen does not necessarily work well.
- **p. 4 / B. Benchmarking Spatial Generalization Capability - extractive body cue:** We vary the number of demonstrations from 25 to 400, The object configurations are randomly sampled from a slightly larger range than the evaluation workspace ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 17 (A. Policy Training and Implementation Details), p. 17 (A. Policy Training and Implementation Details), p. 4 (A. Problem Formulation), p. 4 (A. Problem Formulation), p. 5 (A. Problem Formulation), p. 6 (C. TAMP-based Action Generation), objective p. 17 (A. Policy Training and Implementation Details), p. 6 (C. TAMP-based Action Generation), p. 17 (A. Policy Training and Implementation Details), temporal p. 17 (A. Policy Training and Implementation Details), p. 4 (A. Problem Formulation), p. 11 (B. Cluttered Scene), p. 17 (A. Policy Training and Implementation Details), p. 1 (Abstract), p. 2 (Abstract).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
