# Evaluation - Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p052.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p052.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 16 (B. Implementation Details of TactR), p. 16 (B. Implementation Details of TactR), p. 8 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS)): + Ql: Does tactile signals improve policy performance in contact-rich tasks?

## Evaluation Body Digest

- **p. 7 / V. EXPERIMENTS - extractive body cue:** 1) Hardware: ‘The experimental platform consists of two Flexiv Rizon 4 [19] robotic arms with joint torque sensors and two Flexiv Grav [17] grippers.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** Please see the Appendix A for the hardware details of the improved MCTac sensor. + Built-in joint torque sensors in Flexiv Rizon 4 [19] robotic ...
- **p. 8 / V. EXPERIMENTS - extractive body cue:** 7, in the expert data, there are two upward lift trajectories, indicating the presence of multi-mosalty 4) Evaluation Protocols: We use similar initial states across ...
- **p. 8 / V. EXPERIMENTS - extractive body cue:** The two robots must apply precise force during the task execution.
- **p. 16 / B. Implementation Details of TactR - extractive body cue:** Then, we ‘convert the 3D arrows from the robot TCP coordinate system to the world coordinate system in AR by Eq.
- **p. 16 / B. Implementation Details of TactR - extractive body cue:** ‘The VR headset will receive the latest robot TCP pose transformation matrix W,°C?, the 3D deformation field V; and the undeformed marker locations Do.
- **p. 9 / B. Results - extractive body cue:** ‘TABLE Il: Policy Performance for Peeling Task
- **p. 9 / B. Results - extractive body cue:** It may get stuck when making contact with the object (e.2., failure case 2 in Fig.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** contact-rich manipulation scene.
- **Input boundary:** tactile image/force, vision과 proprioceptive history.
- **Output/decision under evaluation:** grasp/contact action, force command 또는 object motion.
- **Primary target:** slip/contact success, force/pose error와 robustness.
- **Detected evaluation headings:** V. EXPERIMENTS (p. 7); B. Results (p. 9); B. Implementation Details of TactR (p. 16).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | + Ql: Does tactile signals improve policy performance in contact-rich tasks? | p. 7 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | We have improved the original design of MCTac [4], including increasing the size of the marker, reducing the | p. 7 (V. EXPERIMENTS) |
| B. Implementation Details of TactR | EMPIRICAL / REAL-ROBOT OR HARDWARE | 16: The example image of our improved MCTae optical tactile sensor. | p. 16 (B. Implementation Details of TactR) |
| B. Implementation Details of TactR | EMPIRICAL / REAL-ROBOT OR HARDWARE | ur system can achieve low-latency feedback for tactle/- force sensors. | p. 16 (B. Implementation Details of TactR) |
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | For Bimanual Lifting task, if the paper cup is lifted into the air following the designated trajectory without significant compression, the score will be ... | p. 8 (V. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 7 / V. EXPERIMENTS - extractive body cue:** 1) Hardware: ‘The experimental platform consists of two Flexiv Rizon 4 [19] robotic arms with joint torque sensors and two Flexiv Grav [17] grippers.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** Please see the Appendix A for the hardware details of the improved MCTac sensor. + Built-in joint torque sensors in Flexiv Rizon 4 [19] robotic ...
- **p. 8 / V. EXPERIMENTS - extractive body cue:** 7, in the expert data, there are two upward lift trajectories, indicating the presence of multi-mosalty 4) Evaluation Protocols: We use similar initial states across ...
- **p. 8 / V. EXPERIMENTS - extractive body cue:** The two robots must apply precise force during the task execution.
- **p. 16 / B. Implementation Details of TactR - extractive body cue:** Then, we ‘convert the 3D arrows from the robot TCP coordinate system to the world coordinate system in AR by Eq.
- **p. 16 / B. Implementation Details of TactR - extractive body cue:** ‘The VR headset will receive the latest robot TCP pose transformation matrix W,°C?, the 3D deformation field V; and the undeformed marker locations Do.
- **p. 9 / B. Results - extractive body cue:** ‘TABLE Il: Policy Performance for Peeling Task
- **p. 9 / B. Results - extractive body cue:** It may get stuck when making contact with the object (e.2., failure case 2 in Fig.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: TactAR is a low-cost and versatile teleoperation system which can provide real-time tactile / force feedback via
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: Overview of TactAR teleoperation system. It can provide real-time tactile / force feedback via Augmented Reality (AR). The tactile feedback is represented as ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Examples of marker deformation field in GelSight Mini [20] during different contact modes.
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 4: Calibration process in AR. ‘The user adjust the transla- tion and rotation of the virtual coordinate system such that it can align with ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 5: Comparison among various pipelines. (a) Vanilla action ‘chunking [10] with open-loop control during the chunk execu- tion. (b) Action chunking enhanced with temporal ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 6: Overview of Reactive Diffusion Policy (RDP) framework. (a) The training pipeline of RDP, comprising the first stage for training the fast policy (Asymmetric ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 7: Three experiment tasks including Peeling, Wiping and Bimanual Lifting
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 9. We have observed that RDP indeed learns reactive behaviors similar to those of humans. For instance, in Case Study 1, when a peeler ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 1) Hardware: ‘The experimental platform consists of two Flexiv Rizon 4 [19] robotic arms with joint torque sensors and two Flexiv Grav [17] grippers. | embodiment, simulator version and control stack | p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS) |
| Task/environment | Please see the Appendix A for the hardware details of the improved MCTac sensor. + Built-in joint torque sensors in Flexiv Rizon 4 [19] ... | reset, timeout, object/scene variation | p. 7 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS) |
| Observation/sensor | tactile image/force, vision과 proprioceptive history | calibration, preprocessing, privileged input | p. 3 (B. Robot Data Collection System), p. 1 (Body text (section boundary not confidently recovered)) |
| Output/decision | grasp/contact action, force command 또는 object motion | action frame, controller and termination | p. 6 (B. Slow-Fast Policy Learning), p. 2 (I. Ivrropucrion) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Although the performance of both methods is similar, low-dimensional tactile embedding demonstrates greater robustness to texture ‘changes resulting from gel damage or gel replacements ... | definition/direction/unit from same section | p. 9 (B. Results) |
| For Bimanual Lifting task, if the paper cup is lifted into the air following the designated trajectory without significant compression, the score will be ... | definition/direction/unit from same section | p. 8 (V. EXPERIMENTS) |
| For Peeling task, we calculate the score based on the proportion of the peeled cucumber skin to the total length of the cucumber, normalized ... | definition/direction/unit from same section | p. 8 (V. EXPERIMENTS) |
| ATI mini 45[31) due to inaccurate dynamics model, which further challenges the learning algorithm, In order to evaluate policy performance under different tactile 1 ... | definition/direction/unit from same section | p. 7 (V. EXPERIMENTS) |
| This task requires the following capabilities: (1) Precision. | definition/direction/unit from same section | p. 7 (V. EXPERIMENTS) |
| ‘TABLE Il: Policy Performance for Peeling Task | definition/direction/unit from same section | p. 9 (B. Results) |
| Fig. 15: Improved MCTuc Sensor for our task, The left part is the gripper integrated illustration, and the right part is the detailed structure ... | definition/direction/unit from same section | p. 16 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| All devices are connected to a workstation with an Intel Core i9-14900K CPU and an NVIDIA RTX 4090 GPU for both data collection and ... | comparison identity and matched condition | p. 7 (V. EXPERIMENTS) |
| Note that the estimated TCP force / torque Signals have relatively larger noise compared tothe force sensor mounted on the robot end effector (e.g. | comparison identity and matched condition | p. 7 (V. EXPERIMENTS) |
| For Peeling task, we calculate the score based on the proportion of the peeled cucumber skin to the total length of the cucumber, normalized ... | comparison identity and matched condition | p. 8 (V. EXPERIMENTS) |
| However, despite similar performance, these two DP baselines exhibit different failure modes. | comparison identity and matched condition | p. 9 (B. Results) |
| We have compared the performance of Diffusion Policy using raw tactile images (DP w. tactile img.) v.s. low-dim tactile embedding (DP w. tactile emb,) ... | comparison identity and matched condition | p. 9 (B. Results) |
| Fig. 8: Evaluation results and failure cases of baselines. Please see the website for more details. | comparison identity and matched condition | p. 10 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| the handlers, approach the paper cup, clamp the paper cup with the two handlers, carefully lift the cup along the trajectory of the curve ... | component/input/data sensitivity | p. 8 (V. EXPERIMENTS) |
| For Bimanual Lifting task, if the paper cup is lifted into the air following the designated trajectory without significant compression, the score will be ... | component/input/data sensitivity | p. 8 (V. EXPERIMENTS) |
| Although the performance of both methods is similar, low-dimensional tactile embedding demonstrates greater robustness to texture ‘changes resulting from gel damage or gel replacements ... | component/input/data sensitivity | p. 9 (B. Results) |
| Fig. 15: Improved MCTuc Sensor for our task, The left part is the gripper integrated illustration, and the right part is the detailed structure ... | component/input/data sensitivity | p. 16 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To address these challenges, we introduce TactAR, 4 low-cost tleoperation system that provides real-time tactile feedback through Augmented Reality (AR), along with Reactive Diffusion ... | + Ql: Does tactile signals improve policy performance in contact-rich tasks? | PDF body cue; verify exact table/figure and matched conditions | p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 16 (B. Implementation Details of TactR), p. 16 (B. Implementation Details of TactR), p. 8 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS) |
| Primary metric/result | We have improved the original design of MCTac [4], including increasing the size of the marker, reducing the | numeric claim only at cited anchor | p. 7 (V. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 7 / V. EXPERIMENTS - extractive body cue:** + GelSight Mini [20] (Robotics Package) optical tactile sensor with SMP resolution at 25 FPS, and it has a 7 <9 ‘marker dot array on ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** « MCTac [48] optical tactile sensor with 2MP resolution at 30 FPS, and it has a 5x7 marker dot array on the surface.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** We stream the sensor data at 120Hz and downsample it 0 24 FPS.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** All devices are connected to a workstation with an Intel Core i9-14900K CPU and an NVIDIA RTX 4090 GPU for both data collection and evaluation ...
- **p. 8 / V. EXPERIMENTS - extractive body cue:** We run 10 trials for each test-time variation
- **p. 8 / V. EXPERIMENTS - extractive body cue:** 5) Implementation Details: ‘The Diffusion Policy and our slow policy (LDP) predict open-loop 12 FPS action sequences for each action chunk.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | It may get stuck when making contact with the object (e.2., failure case 2 in Fig. | p. 9 (B. Results) |
| body limitation/failure cue | However, despite similar performance, these two DP baselines exhibit different failure modes. | p. 9 (B. Results) |
| body limitation/failure cue | 8: Evaluation results and failure cases of baselines. | p. 10 (056 O58 om) |
| body limitation/failure cue | V that when the action chunk size is reduced from 8 to 2, the DP baseline tends to get stuck before grasping (failure case ... | p. 10 (056 O58 om) |
| body limitation/failure cue | It is crucial to avoid exerting excessive force that could squeeze the cup while also ensuring that the force is sufficient to prevent the ... | p. 8 (V. EXPERIMENTS) |
| body limitation/failure cue | Note that the estimated TCP force / torque Signals have relatively larger noise compared tothe force sensor mounted on the robot end effector (e.g. | p. 7 (V. EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| All devices are connected to a workstation with an Intel Core i9-14900K CPU and an NVIDIA RTX 4090 GPU for both data collection and ... | p. 7 (V. EXPERIMENTS) |
| We run 10 trials for each test-time variation | p. 8 (V. EXPERIMENTS) |
| + Diffusion Policy: vanilla implementation of Diffusion Policy {10} with only visual input (RGB images) and ‘open-loop action chunking. | p. 7 (V. EXPERIMENTS) |
| 5) Implementation Details: ‘The Diffusion Policy and our slow policy (LDP) predict open-loop 12 FPS action sequences for each action chunk. | p. 8 (V. EXPERIMENTS) |
| Please see Appendix D, F and I for more details on data collection, the inference process and the hyperparameters. | p. 9 (V. EXPERIMENTS) |
| ‘TABLE I: Inference Time of Different Modules on RTX 4090 | p. 6 (architecture) |
| Our TactAR system is built with low-cost hhardwares. ‘The Meta Quest3 VR heaset used for teleoperation and AR feedbacks costs $199. | p. 4 (A. 3D Deformation Field Extraction) |
| We also support both single-arm and, bimanual arm control, Thus, TactAR will not be limited by specific hardware configuration parameters and de- ‘grees of ... | p. 4 (A. 3D Deformation Field Extraction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / B. Results - extractive body cue:** It may get stuck when making contact with the object (e.2., failure case 2 in Fig.
- **p. 9 / B. Results - extractive body cue:** However, despite similar performance, these two DP baselines exhibit different failure modes.
- **p. 10 / 056 O58 om - extractive body cue:** 8: Evaluation results and failure cases of baselines.
- **p. 10 / 056 O58 om - extractive body cue:** V that when the action chunk size is reduced from 8 to 2, the DP baseline tends to get stuck before grasping (failure case 4 ...
- **p. 8 / V. EXPERIMENTS - extractive body cue:** It is crucial to avoid exerting excessive force that could squeeze the cup while also ensuring that the force is sufficient to prevent the cup ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** Note that the estimated TCP force / torque Signals have relatively larger noise compared tothe force sensor mounted on the robot end effector (e.g.

- **Evidence anchors reviewed:** datasets p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS), p. 16 (B. Implementation Details of TactR), p. 16 (B. Implementation Details of TactR), metrics p. 9 (B. Results), p. 8 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 9 (B. Results), baselines p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS), p. 9 (B. Results), p. 9 (B. Results), p. 10 (Figure/Table caption), results p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 16 (B. Implementation Details of TactR), p. 16 (B. Implementation Details of TactR), p. 8 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** All devices are connected to a workstation with an Intel Core i9-14900K CPU and an NVIDIA RTX 4090 GPU for both data collection and evaluation 2) Baselines: We use the ... (p. 7, V. EXPERIMENTS).
- **Metric evidence:** Although the performance of both methods is similar, low-dimensional tactile embedding demonstrates greater robustness to texture ‘changes resulting from gel damage or gel replacements during the evaluation process. (p. 9, B. Results).
- **Baseline/ablation evidence:** All devices are connected to a workstation with an Intel Core i9-14900K CPU and an NVIDIA RTX 4090 GPU for both data collection and evaluation 2) Baselines: We use the ... (p. 7, V. EXPERIMENTS).
- **Failure/negative evidence:** We ‘observe that DP with pure visual input frequently predicts inaccurate trajectories and results in large contact forces (e.g. failure case 2 in Fig. (p. 9, B. Results).
