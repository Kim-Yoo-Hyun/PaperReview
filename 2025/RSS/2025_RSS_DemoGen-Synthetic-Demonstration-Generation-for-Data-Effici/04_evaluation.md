# Evaluation - DemoGen: Synthetic Demonstration Generation for Data-Efficient Visuomotor Policy Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p157.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p157.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 4 (B. Benchmarking Spatial Generalization Capability), p. 18 (Figure/Table caption), p. 4 (B. Benchmarking Spatial Generalization Capability), p. 3 (Figure/Table caption), p. 7 (Figure/Table caption), p. 17 (A. Policy Training and Implementation Details)): We report the relationship between the agent's performance Jn success rates and the number of demonstrations used for traning ‘when different visuomotor policies and object randomization ranges are adopted, The ...

## Evaluation Body Digest

- **p. 4 / B. Benchmarking Spatial Generalization Capability - extractive body cue:** In the following benchmarking, we explore the relationship between the number of demonstrations and policy performance to determine how many demonstrations are sufficient for effective ...
- **p. 4 / B. Benchmarking Spatial Generalization Capability - extractive body cue:** 3: Quantitative benchmarking on the spatial generalization spacity.
- **p. 17 / A. Policy Training and Implementation Details - extractive body cue:** R3M utilizes a ResNet [21] architecture and is pre-trained on roboties-specific tasks.
- **p. 17 / A. Policy Training and Implementation Details - extractive body cue:** In real-world experiments, we use the DBSCAN [15] elustering algorithm to discard the outlier points and downsample the number of points in the point cloud ...
- **p. 4 / B. Benchmarking Spatial Generalization Capability - extractive body cue:** We report the relationship between the agent's performance Jn success rates and the number of demonstrations used for traning ‘when different visuomotor policies and object ...
- **p. 18 / Figure/Table caption - extractive body cue:** Fig. 20: Visualization of the policy performance trained on human-collected datasets. (Upper row) The demonstrated configurations. (Bottom row) The spatial heatmaps with success rates averaged ...
- **p. 4 / B. Benchmarking Spatial Generalization Capability - extractive body cue:** To suppress the occurrence of inaccurate but successful policy rollouts, we design a Precise-Peg-Insertion task that enforces a strict fault tolerance of 1 em during ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: Qualitative visualization of the spatial effective range. The grid maps display discretized tabletop workspaces from a bird's-eye view under different demonstration configurations. Dark ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** demonstration으로 정의된 robot task distribution.
- **Input boundary:** observation history와 expert trajectory/action.
- **Output/decision under evaluation:** predicted action 또는 action chunk.
- **Primary target:** imitation error, task success, robustness와 compounding error.
- **Detected evaluation headings:** B. Benchmarking Spatial Generalization Capability (p. 4); V. PRELIMINARY EXPERIMENTS IN THE SIMULATOR (p. 6); A. Policy Training and Implementation Details (p. 17).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| B. Benchmarking Spatial Generalization Capability | EMPIRICAL / REAL-ROBOT OR HARDWARE | We report the relationship between the agent's performance Jn success rates and the number of demonstrations used for traning ‘when different visuomotor policies and ... | p. 4 (B. Benchmarking Spatial Generalization Capability) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 20: Visualization of the policy performance trained on human-collected datasets. (Upper row) The demonstrated configurations. (Bottom row) The spatial heatmaps with success rates ... | p. 18 (Figure/Table caption) |
| B. Benchmarking Spatial Generalization Capability | EMPIRICAL / REAL-ROBOT OR HARDWARE | On the other hand, both 3D representations and pre-trained 2D visual encoders contribute to improved spatial generalization capabilities. | p. 4 (B. Benchmarking Spatial Generalization Capability) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 2: Qualitative visualization of the spatial effective range. The grid maps display discretized tabletop workspaces from a bird's-eye view under different demonstration configurations. ... | p. 3 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 9: Performance Saturation. We report the policy performance boost wart. the increase of synthetic demonstrations over 3 seeds. | p. 7 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 4 / B. Benchmarking Spatial Generalization Capability - extractive body cue:** In the following benchmarking, we explore the relationship between the number of demonstrations and policy performance to determine how many demonstrations are sufficient for effective ...
- **p. 4 / B. Benchmarking Spatial Generalization Capability - extractive body cue:** 3: Quantitative benchmarking on the spatial generalization spacity.
- **p. 17 / A. Policy Training and Implementation Details - extractive body cue:** R3M utilizes a ResNet [21] architecture and is pre-trained on roboties-specific tasks.
- **p. 17 / A. Policy Training and Implementation Details - extractive body cue:** In real-world experiments, we use the DBSCAN [15] elustering algorithm to discard the outlier points and downsample the number of points in the point cloud ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: DemoGen isa fully synthetic approach for a ‘of visuomotor policies and can facilitate one-shot i
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: Qualitative visualization of the spatial effective range. The grid maps display discretized tabletop workspaces from a bird's-eye view under different demonstration configurations. Dark ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Quantitative benchmarking on the spatial generalization spacity. We report the relationship between the agent's performance Jn success rates and the number of demonstrations ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: Pre-processing the source demonstration. The raw point cloud observations are processed by cropping, clustering, and down- sampling. The source action tajectory is parsed ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 5: Mustrations for action generation. (Left) Actions in the ‘motion stage are planned to connect the neighboring skill segments, (Right) Actions in the skill ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 6: [ustrations for synthetic visual observation generation. Objects in the to-da slage are segmented and transformed by the target ‘object configurations. Objects in the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 7: Tasks for simulated evaluation on spatial generalization. Pape a sky-blue recunpen sa he wns cispce for conan generation and evaluation, respectively. The detailed ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 8: Mlustration for the visual mismatch problem. As objects ‘move through 3D space, their appearance changes due to variations in perspective. Under the constraint ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | In the following benchmarking, we explore the relationship between the number of demonstrations and policy performance to determine how many demonstrations are sufficient for ... | embodiment, simulator version and control stack | p. 4 (B. Benchmarking Spatial Generalization Capability), p. 4 (B. Benchmarking Spatial Generalization Capability) |
| Task/environment | 3: Quantitative benchmarking on the spatial generalization spacity. | reset, timeout, object/scene variation | p. 4 (B. Benchmarking Spatial Generalization Capability), p. 17 (A. Policy Training and Implementation Details) |
| Observation/sensor | observation history와 expert trajectory/action | calibration, preprocessing, privileged input | p. 5 (A. Problem Formulation), p. 4 (A. Problem Formulation) |
| Output/decision | predicted action 또는 action chunk | action frame, controller and termination | p. 17 (A. Policy Training and Implementation Details), p. 17 (A. Policy Training and Implementation Details) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We report the relationship between the agent's performance Jn success rates and the number of demonstrations used for traning ‘when different visuomotor policies and ... | definition/direction/unit from same section | p. 4 (B. Benchmarking Spatial Generalization Capability) |
| Fig. 20: Visualization of the policy performance trained on human-collected datasets. (Upper row) The demonstrated configurations. (Bottom row) The spatial heatmaps with success rates ... | definition/direction/unit from same section | p. 18 (Figure/Table caption) |
| To suppress the occurrence of inaccurate but successful policy rollouts, we design a Precise-Peg-Insertion task that enforces a strict fault tolerance of 1 em ... | definition/direction/unit from same section | p. 4 (B. Benchmarking Spatial Generalization Capability) |
| Fig. 2: Qualitative visualization of the spatial effective range. The grid maps display discretized tabletop workspaces from a bird's-eye view under different demonstration configurations. ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Fig. 9: Performance Saturation. We report the policy performance boost wart. the increase of synthetic demonstrations over 3 seeds. | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Fig. 15: ‘demonstrated in a cluttered scene and tested in another scene where the jar is placed on a shelf | definition/direction/unit from same section | p. 11 (Figure/Table caption) |
| Fig. 17: Mlustration for the ADR strategy. Asynchronous transfor ‘mations are applied tothe disturbed object and the robot end-effector to simulate the disturbance resistance ... | definition/direction/unit from same section | p. 11 (Figure/Table caption) |
| Fig. 18: DemoGen for obstacle avoidance. (ab) Policy trained on the source demonstration collides with the unseen obstacle. (ed) Policy trained on the generated ... | definition/direction/unit from same section | p. 12 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Fig. 22: Raw evaluation results in the Sauce-Spreading task. (Top) Examples of the processing results for metric calculation. (Bottom) Compared with the regular DemoGen, ... | comparison identity and matched condition | p. 18 (Figure/Table caption) |
| 1) Details for Policy Training: Fora fair comparison, we fix the total training steps counted by observation-action pairs to be 2M for all evaluated ... | comparison identity and matched condition | p. 17 (A. Policy Training and Implementation Details) |
| Since Ts indicates the steps of actions executed on the robot without re-planning, our horizon settings result in a closed-loop re-planning latency of 0.5 ... | comparison identity and matched condition | p. 17 (A. Policy Training and Implementation Details) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Since Ts indicates the steps of actions executed on the robot without re-planning, our horizon settings result in a closed-loop re-planning latency of 0.5 ... | component/input/data sensitivity | p. 17 (A. Policy Training and Implementation Details) |
| Specifically, we replace the train-fromscratch ResNet [21] encoder in DP with pre-trained encoders including R3M [35], DINOv2 [36], and CLIP [41]. | component/input/data sensitivity | p. 4 (B. Benchmarking Spatial Generalization Capability) |
| 2) Pre-Trained Encoders for Diffusion Policies: To replace the train-from-scratch ResNetl8 [21] visual encoder in the original Diffusion Policy architecture, we consider 3. representative ... | component/input/data sensitivity | p. 17 (A. Policy Training and Implementation Details) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The action a, consists of the robot arm and robot hhand commands, represented as a - (a""a!!™), where a7" © AP" is the target ... | We report the relationship between the agent's performance Jn success rates and the number of demonstrations used for traning ‘when different visuomotor policies and ... | PDF body cue; verify exact table/figure and matched conditions | p. 4 (B. Benchmarking Spatial Generalization Capability), p. 18 (Figure/Table caption), p. 4 (B. Benchmarking Spatial Generalization Capability), p. 3 (Figure/Table caption), p. 7 (Figure/Table caption), p. 17 (A. Policy Training and Implementation Details) |
| Primary metric/result | Fig. 20: Visualization of the policy performance trained on human-collected datasets. (Upper row) The demonstrated configurations. (Bottom row) The spatial heatmaps with success rates ... | numeric claim only at cited anchor | p. 18 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 4 / B. Benchmarking Spatial Generalization Capability - extractive body cue:** We report the relationship between the agent's performance Jn success rates and the number of demonstrations used for traning ‘when different visuomotor policies and object ...
- **p. 17 / A. Policy Training and Implementation Details - extractive body cue:** To stabilize the training process, we use AdamW [32] optimizer and set the learning rate to be Le with a 500 step warmup.
- **p. 17 / A. Policy Training and Implementation Details - extractive body cue:** In real-world experiments, we use the DBSCAN [15] elustering algorithm to discard the outlier points and downsample the number of points in the point cloud ...
- **p. 17 / A. Policy Training and Implementation Details - extractive body cue:** To stabilize the training process, we use AdamW [32] optimizer and set the learning rate to be Le with a 500 step warmup.
- **p. 17 / A. Policy Training and Implementation Details - extractive body cue:** In real-world experiments, we use the DBSCAN [15] elustering algorithm to discard the outlier points and downsample the number of points in the point cloud ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Trained on the source demonstrations without obstacles, the visuomotor policy fails to account for potential collisions, e.g., it might knock over the coffee cup ... | p. 12 (B. Obstacle Avoidance) |
| body limitation/failure cue | Obstacle-avoiding trajectories are generated by a motion planning tool [28], ensuring collision-free actions. | p. 12 (B. Obstacle Avoidance) |
| body limitation/failure cue | When the scene becomes even more complex, e.g. clutter, DemoGen does not necessarily work well. | p. 11 (B. Cluttered Scene) |
| body limitation/failure cue | We vary the number of demonstrations from 25 to 400, The object configurations are randomly sampled from a slightly larger range than the evaluation ... | p. 4 (B. Benchmarking Spatial Generalization Capability) |
| body limitation/failure cue | 16: DemoGen for disturbance resistance. | p. 11 (B. Cluttered Scene) |
| body limitation/failure cue | Since Ts indicates the steps of actions executed on the robot without re-planning, our horizon settings result in a closed-loop re-planning latency of 0.5 ... | p. 17 (A. Policy Training and Implementation Details) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| To stabilize the training process, we use AdamW [32] optimizer and set the learning rate to be Le with a 500 step warmup. | p. 17 (A. Policy Training and Implementation Details) |
| We list the training and ‘implementation details as follows, | p. 17 (A. Policy Training and Implementation Details) |
| Detailed implementations are provided in Appendix A2. | p. 4 (B. Benchmarking Spatial Generalization Capability) |
| On the other hand, both 3D representations and pre-trained 2D visual encoders contribute to improved spatial generalization capabilities. | p. 4 (B. Benchmarking Spatial Generalization Capability) |
| Under the 4x4 homogeneous matrix representation, the spatial transformation between the target and source configurations is computed as: | p. 5 (C. TAMP-based Action Generation) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 12 / B. Obstacle Avoidance - extractive body cue:** Trained on the source demonstrations without obstacles, the visuomotor policy fails to account for potential collisions, e.g., it might knock over the coffee cup placed ...
- **p. 12 / B. Obstacle Avoidance - extractive body cue:** Obstacle-avoiding trajectories are generated by a motion planning tool [28], ensuring collision-free actions.
- **p. 11 / B. Cluttered Scene - extractive body cue:** When the scene becomes even more complex, e.g. clutter, DemoGen does not necessarily work well.
- **p. 4 / B. Benchmarking Spatial Generalization Capability - extractive body cue:** We vary the number of demonstrations from 25 to 400, The object configurations are randomly sampled from a slightly larger range than the evaluation workspace ...
- **p. 11 / B. Cluttered Scene - extractive body cue:** 16: DemoGen for disturbance resistance.
- **p. 17 / A. Policy Training and Implementation Details - extractive body cue:** Since Ts indicates the steps of actions executed on the robot without re-planning, our horizon settings result in a closed-loop re-planning latency of 0.5 seconds. ...

- **Evidence anchors reviewed:** datasets p. 4 (B. Benchmarking Spatial Generalization Capability), p. 4 (B. Benchmarking Spatial Generalization Capability), p. 17 (A. Policy Training and Implementation Details), p. 17 (A. Policy Training and Implementation Details), metrics p. 4 (B. Benchmarking Spatial Generalization Capability), p. 18 (Figure/Table caption), p. 4 (B. Benchmarking Spatial Generalization Capability), p. 3 (Figure/Table caption), p. 7 (Figure/Table caption), p. 11 (Figure/Table caption), baselines p. 18 (Figure/Table caption), p. 17 (A. Policy Training and Implementation Details), p. 17 (A. Policy Training and Implementation Details), results p. 4 (B. Benchmarking Spatial Generalization Capability), p. 18 (Figure/Table caption), p. 4 (B. Benchmarking Spatial Generalization Capability), p. 3 (Figure/Table caption), p. 7 (Figure/Table caption), p. 17 (A. Policy Training and Implementation Details).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (20 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** 1) Details for Policy Training: Fora fair comparison, we fix the total training steps counted by observation-action pairs to be 2M for all evaluated settings, resulting in an equal training ... (p. 17, A. Policy Training and Implementation Details).
- **Metric evidence:** We report the relationship between the agent's performance Jn success rates and the number of demonstrations used for traning ‘when different visuomotor policies and object randomization ranges are adopted, The ... (p. 4, B. Benchmarking Spatial Generalization Capability).
- **Baseline/ablation evidence:** 1) Details for Policy Training: Fora fair comparison, we fix the total training steps counted by observation-action pairs to be 2M for all evaluated settings, resulting in an equal training ... (p. 17, A. Policy Training and Implementation Details).
- **Failure/negative evidence:** Failure-free action execution, ‘To ensure the validity of synthetic demonstrations without on-robot rollouts to filter ut failed trajectories, we require failure-Free action execution Unlike previous works (3, 20] that rely ... (p. 6, C. TAMP-based Action Generation).
