# Evaluation - NaVILA: Legged Robot Vision-Language-Action Model for Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p018.html; PDF retrieval source: https://arxiv.org/pdf/2412.04453. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (III. EXPERIMENTS), p. 6 (III. EXPERIMENTS), p. 7 (III. EXPERIMENTS), p. 6 (III. EXPERIMENTS), p. 7 (III. EXPERIMENTS), p. 8 (III. EXPERIMENTS)): Workspace Home Outdoor Simple Complex Simple Complex Simple Complex NE↓SR↑NE↓SR↑NE↓SR↑NE↓SR↑NE↓SR↑NE↓SR↑ Unitree Go2 GPT-4o [28] 2.01 0.67 2.38 0.33 1.49 0.53 3.00 0.00 - 0.67 - 0.50 NaVILA † 2.00 0.60 ...

## Evaluation Body Digest

- **p. 6 / III. EXPERIMENTS - extractive body cue:** To evaluate NaVILA's capabilities in scene understanding, we conduct evaluations on the ScanQA Validation benchmark, a widely used dataset for 3D Question Answering.
- **p. 5 / III. EXPERIMENTS - extractive body cue:** We evaluate our VLA on the VLNCE benchmarks, which provide continuous environments for executing navigational actions in reconstructed photorealistic indoor scenes.
- **p. 7 / III. EXPERIMENTS - extractive body cue:** Legged Robot Navigation Performance in Simulation High-fidelity VLN-CE-Isaac Benchmark.
- **p. 7 / III. EXPERIMENTS - extractive body cue:** We incorporate the same scenes from R2R, with robots deployed in the environment, as shown in Fig.
- **p. 5 / III. EXPERIMENTS - extractive body cue:** We focus on the val-unseen split in both R2R (Room-to-Room) and RxR (Room-across-Room) datasets
- **p. 6 / III. EXPERIMENTS - extractive body cue:** To evaluate the cross-dataset performance, we follow [12] by training NaVILA exclusively on R2R samples, while leaving out the RxR training set.
- **p. 8 / III. EXPERIMENTS - extractive body cue:** These results highlight the effectiveness of NaVILA in bridging the gap between visionlanguage understanding and real-world navigation tasks.
- **p. 8 / III. EXPERIMENTS - extractive body cue:** Workspace Home Outdoor Simple Complex Simple Complex Simple Complex NE↓SR↑NE↓SR↑NE↓SR↑NE↓SR↑NE↓SR↑NE↓SR↑ Unitree Go2 GPT-4o [28] 2.01 0.67 2.38 0.33 1.49 0.53 3.00 0.00 - 0.67 - ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** legged robot, terrain과 contact dynamics.
- **Input boundary:** proprioception, terrain/perception observation과 velocity command.
- **Output/decision under evaluation:** joint target, torque, footstep 또는 locomotion action.
- **Primary target:** velocity/progress, stability, energy와 terrain generalization.
- **Detected evaluation headings:** III. EXPERIMENTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| III. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Workspace Home Outdoor Simple Complex Simple Complex Simple Complex NE↓SR↑NE↓SR↑NE↓SR↑NE↓SR↑NE↓SR↑NE↓SR↑ Unitree Go2 GPT-4o [28] 2.01 0.67 2.38 0.33 1.49 0.53 3.00 0.00 - 0.67 ... | p. 8 (III. EXPERIMENTS) |
| III. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Table II, our method significantly outperforms NaVid, the current state-of-the-art model, with a substantial 10% improvement in SR. | p. 6 (III. EXPERIMENTS) |
| III. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Error ↓ Collision Rate ↓ ROA(w/BCLoss) [68] 0.189 0.152 3.25 ROA [68] 0.161 0.152 3.09 NaVILA 0.066 0.113 0.81 the vision-based policy outperforms the ... | p. 7 (III. EXPERIMENTS) |
| III. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Table III, NaVILA significantly outperforms the previous state-of-the-art model, NaviLLM [60], by a substantial margin (20 points higher on the CIDEr ... | p. 6 (III. EXPERIMENTS) |
| III. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Additionally, we also observe that the success rate of NaVILA on the H1 robot is significantly lower than on the Go2, which is expected ... | p. 7 (III. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 6 / III. EXPERIMENTS - extractive body cue:** To evaluate NaVILA's capabilities in scene understanding, we conduct evaluations on the ScanQA Validation benchmark, a widely used dataset for 3D Question Answering.
- **p. 5 / III. EXPERIMENTS - extractive body cue:** We evaluate our VLA on the VLNCE benchmarks, which provide continuous environments for executing navigational actions in reconstructed photorealistic indoor scenes.
- **p. 7 / III. EXPERIMENTS - extractive body cue:** Legged Robot Navigation Performance in Simulation High-fidelity VLN-CE-Isaac Benchmark.
- **p. 7 / III. EXPERIMENTS - extractive body cue:** We incorporate the same scenes from R2R, with robots deployed in the environment, as shown in Fig.
- **p. 5 / III. EXPERIMENTS - extractive body cue:** We focus on the val-unseen split in both R2R (Room-to-Room) and RxR (Room-across-Room) datasets
- **p. 6 / III. EXPERIMENTS - extractive body cue:** To evaluate the cross-dataset performance, we follow [12] by training NaVILA exclusively on R2R samples, while leaving out the RxR training set.
- **p. 8 / III. EXPERIMENTS - extractive body cue:** These results highlight the effectiveness of NaVILA in bridging the gap between visionlanguage understanding and real-world navigation tasks.
- **p. 8 / III. EXPERIMENTS - extractive body cue:** Workspace Home Outdoor Simple Complex Simple Complex Simple Complex NE↓SR↑NE↓SR↑NE↓SR↑NE↓SR↑NE↓SR↑NE↓SR↑ Unitree Go2 GPT-4o [28] 2.01 0.67 2.38 0.33 1.49 0.53 3.00 0.00 - 0.67 - ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Real-world demonstration of NaVILA: Upon receiving human instructions, NaVILA uses a vision-language model to process RGB video frames and employs locomotion skills to ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: NaVILA is a two-level framework combining high-level visual language understanding with low-level locomotion control. Our VLA model processes single-view images to produce mid-level ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Overview of our VLA framework. We denote the purple blocks ( ) as memory tokens sampled from historical frames, and the red blocks ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: Data pipeline for transforming human touring videos in the wild into pairwise navigation data within a continuous environment. We begin by processing the ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 5: Height map reconstruction from point cloud. (a) Go2 robot follows velocity commands while avoiding obstacles in simulation. Red dots show LiDAR points raycasting ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: VLN-CE-Isaac Benchmark visualization. TABLE IV: VLN-CE-Isaac evaluation results. Low-level Observation VLN-CE-Isaac Proprio. LiDAR Height Scan NE ↓OS ↑SR ↑SPL ↑ Oracle 5.25
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 7: Qualitative results from the real-world deployment of NaVILA. (a) We integrate speech recognition [70] into NaVILA, allowing a human to control the robot ...
- **p. 14 / Figure/Table caption - extractive body cue:** Fig. 8: Comparison between Go2 blind policy and vision policy. The blind policy failed to avoid the obstacles and got stuck. The vision policy detected ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | To evaluate NaVILA's capabilities in scene understanding, we conduct evaluations on the ScanQA Validation benchmark, a widely used dataset for 3D Question Answering. | embodiment, simulator version and control stack | p. 6 (III. EXPERIMENTS), p. 5 (III. EXPERIMENTS) |
| Task/environment | We evaluate our VLA on the VLNCE benchmarks, which provide continuous environments for executing navigational actions in reconstructed photorealistic indoor scenes. | reset, timeout, object/scene variation | p. 5 (III. EXPERIMENTS), p. 7 (III. EXPERIMENTS) |
| Observation/sensor | proprioception, terrain/perception observation과 velocity command | calibration, preprocessing, privileged input | p. 2 (I. INTRODUCTION), p. 3 (II. METHOD) |
| Output/decision | joint target, torque, footstep 또는 locomotion action | action frame, controller and termination | p. 2 (I. INTRODUCTION), p. 5 (II. METHOD) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We employ the following widely used evaluation metrics for VLN tasks: Navigation Error (NE), Oracle Success Rate (OS), Success Rate (SR), Success-weighted Path Length ... | definition/direction/unit from same section | p. 6 (III. EXPERIMENTS) |
| Error ↓ Collision Rate ↓ ROA(w/BCLoss) [68] 0.189 0.152 3.25 ROA [68] 0.161 0.152 3.09 NaVILA 0.066 0.113 0.81 the vision-based policy outperforms the ... | definition/direction/unit from same section | p. 7 (III. EXPERIMENTS) |
| ScanQA Validation Bleu-4 ↑Rouge ↑Cider ↑Meteor ↑EM ↑ Task-specific Specialist VoteNet+MCAN [63] 6.2 29.8 54.7 11.4 17.3 ScanRefer+MCAN [63] 7.9 30.0 55.4 11.5 18.6 ... | definition/direction/unit from same section | p. 7 (III. EXPERIMENTS) |
| Workspace Home Outdoor Simple Complex Simple Complex Simple Complex NE↓SR↑NE↓SR↑NE↓SR↑NE↓SR↑NE↓SR↑NE↓SR↑ Unitree Go2 GPT-4o [28] 2.01 0.67 2.38 0.33 1.49 0.53 3.00 0.00 - 0.67 ... | definition/direction/unit from same section | p. 8 (III. EXPERIMENTS) |
| As shown in Table III, NaVILA significantly outperforms the previous state-of-the-art model, NaviLLM [60], by a substantial margin (20 points higher on the CIDEr ... | definition/direction/unit from same section | p. 6 (III. EXPERIMENTS) |
| Fig. 12: Obstacle avoidance screenshots. Locomotion policy can ensure collision-free in the face of high grass, certain transparent glass, and large objects under strong ... | definition/direction/unit from same section | p. 17 (Figure/Table caption) |
| Fig. 11: Random rough, obstacle and slope terrain. TABLE X: Reward function parameters for training RL policy. Reward Expression Weight Linear velocity tracking exp(-∥vcmd ... | definition/direction/unit from same section | p. 16 (Figure/Table caption) |
| Fig. 1: Real-world demonstration of NaVILA: Upon receiving human instructions, NaVILA uses a vision-language model to process RGB video frames and employs locomotion skills ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We also compare NaVILAs with a baseline using Oracle's low-level policy (assuming perfect command execution without realistic physics). | comparison identity and matched condition | p. 7 (III. EXPERIMENTS) |
| NaVILA significantly outperforms NaVid [12], the current single-view state-of-the-art. | comparison identity and matched condition | p. 6 (III. EXPERIMENTS) |
| As shown in Table II, our method significantly outperforms NaVid, the current state-of-the-art model, with a substantial 10% improvement in SR. | comparison identity and matched condition | p. 6 (III. EXPERIMENTS) |
| NaVILA outperforms current state-of-the-art VLA models and demonstrates superior performance to other 3D LMMs that require additional input, such as depth or camera pose. | comparison identity and matched condition | p. 7 (III. EXPERIMENTS) |
| Despite variations such as changes in camera height and camera view angle, NaVILA consistently outperformes the baselines, highlighting the strong generalization capabilities of our ... | comparison identity and matched condition | p. 8 (III. EXPERIMENTS) |
| Note that † indicates models trained without human touring videos. | comparison identity and matched condition | p. 8 (III. EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| All results are obtained without training on the RxRCE training set. | component/input/data sensitivity | p. 6 (III. EXPERIMENTS) |
| We also compare NaVILAs with a baseline using Oracle's low-level policy (assuming perfect command execution without realistic physics). | component/input/data sensitivity | p. 7 (III. EXPERIMENTS) |
| Existing benchmarks [29, 30] for vision-language navigation are based on the Habitat [69] simulator, which focuses on high-level planning without addressing precise low-level robotic ... | component/input/data sensitivity | p. 7 (III. EXPERIMENTS) |
| Note that † indicates models trained without human touring videos. | component/input/data sensitivity | p. 8 (III. EXPERIMENTS) |
| To demonstrate the flexibility of our two-level approach, we also evaluated it on a Booster Dynamics T1 humanoid robot, using the same VLA model ... | component/input/data sensitivity | p. 8 (III. EXPERIMENTS) |
| Notably, this also marks the first time a VLN agent, trained solely on single-view RGB input, achieves comparable or superior results to models that ... | component/input/data sensitivity | p. 6 (III. EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To better simulate the challenges of locomotion navigation in VLN, we introduce a new benchmark, VLN-CE-Isaac, using Isaac Sim. | Workspace Home Outdoor Simple Complex Simple Complex Simple Complex NE↓SR↑NE↓SR↑NE↓SR↑NE↓SR↑NE↓SR↑NE↓SR↑ Unitree Go2 GPT-4o [28] 2.01 0.67 2.38 0.33 1.49 0.53 3.00 0.00 - 0.67 ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (III. EXPERIMENTS), p. 6 (III. EXPERIMENTS), p. 7 (III. EXPERIMENTS), p. 6 (III. EXPERIMENTS), p. 7 (III. EXPERIMENTS), p. 8 (III. EXPERIMENTS) |
| Primary metric/result | As shown in Table II, our method significantly outperforms NaVid, the current state-of-the-art model, with a substantial 10% improvement in SR. | numeric claim only at cited anchor | p. 6 (III. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 6 / III. EXPERIMENTS - extractive body cue:** As shown in Table III, NaVILA significantly outperforms the previous state-of-the-art model, NaviLLM [60], by a substantial margin (20 points higher on the CIDEr score).
- **p. 6 / III. EXPERIMENTS - extractive body cue:** Moreover, when using 64 frames, NaVILA's performance demonstrates superior performance compared to state-of-the-art 3D-based large multimodal models [61, 62].
- **p. 7 / III. EXPERIMENTS - extractive body cue:** ScanQA Validation Bleu-4 ↑Rouge ↑Cider ↑Meteor ↑EM ↑ Task-specific Specialist VoteNet+MCAN [63] 6.2 29.8 54.7 11.4 17.3 ScanRefer+MCAN [63] 7.9 30.0 55.4 11.5 18.6 ScanQA ...
- **p. 7 / III. EXPERIMENTS - extractive body cue:** From the 1,839 trajectories in the R2R Val-Unseen split, we select 1,077 traversable trajectories with high-quality meshes to ensure realistic navigation scenarios.
- **p. 3 / II. METHOD - extractive body cue:** Therefore, we first extract the most recent frame t as the current observation and then uniformly sample frames from the preceding t-1 frames, ensuring the ...
- **p. 4 / II. METHOD - extractive body cue:** In our experiments, we tested configurations with 8 to 64 frames for t. trajectories using entropy-based sampling [26].

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | While NaVILA demonstrates strong performance, it fails in some real-world cases (see Appx. | p. 9 (V. CONCLUSION AND LIMITATIONS) |
| body limitation/failure cue | Fig. 12: Obstacle avoidance screenshots. Locomotion policy can ensure collision-free in the face of high grass, certain transparent glass, and large objects under strong ... | p. 17 (Figure/Table caption) |
| body limitation/failure cue | To overcome this limitation, we introduce a new benchmark VLN-CE-Isaac built on Isaac Sim. | p. 7 (III. EXPERIMENTS) |
| body limitation/failure cue | As shown in Table V, our low-level policy outperforms ROA in all three metrics, particularly achieving a significantly lower collision rate, demonstrating the effectiveness ... | p. 7 (III. EXPERIMENTS) |
| body limitation/failure cue | NaVILA generates high-level language commands while a realtime locomotion policy handles obstacle avoidance, enhancing robustness across robots. | p. 9 (V. CONCLUSION AND LIMITATIONS) |
| body limitation/failure cue | Fig. 8: Comparison between Go2 blind policy and vision policy. The blind policy failed to avoid the obstacles and got stuck. The vision policy ... | p. 14 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| In ROA training, the model first learns a privileged encoder that processes height scan points and other privileged observations. | p. 6 (III. EXPERIMENTS) |
| This privileged encoder then supervises an adaptation encoder, which takes the same 2.5D heightmap as our low-level policy as input. | p. 6 (III. EXPERIMENTS) |
| With the support of ray-casting in Isaac Lab, our vision-based RL policy training achieves a high throughput over 60K FPS on an RTX 4090 ... | p. 5 (II. METHOD) |
| A common approach to handling video inputs in VLMs is through video encoders [12]. | p. 3 (II. METHOD) |
| VILA consists of three main components: a vision encoder, a projector, and an LLM. | p. 3 (II. METHOD) |
| During this training, all three components-vision encoder, connector, and LLM-are unfrozen. | p. 4 (II. METHOD) |
| History Views Current View Vision Encoder 🔥 Down Sample & Projector 🔥 The next action is Walk forward and turn right. | p. 4 (II. METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / V. CONCLUSION AND LIMITATIONS - extractive body cue:** While NaVILA demonstrates strong performance, it fails in some real-world cases (see Appx.
- **p. 17 / Figure/Table caption - extractive body cue:** Fig. 12: Obstacle avoidance screenshots. Locomotion policy can ensure collision-free in the face of high grass, certain transparent glass, and large objects under strong sunlight. ...
- **p. 7 / III. EXPERIMENTS - extractive body cue:** To overcome this limitation, we introduce a new benchmark VLN-CE-Isaac built on Isaac Sim.
- **p. 7 / III. EXPERIMENTS - extractive body cue:** As shown in Table V, our low-level policy outperforms ROA in all three metrics, particularly achieving a significantly lower collision rate, demonstrating the effectiveness of ...
- **p. 9 / V. CONCLUSION AND LIMITATIONS - extractive body cue:** NaVILA generates high-level language commands while a realtime locomotion policy handles obstacle avoidance, enhancing robustness across robots.
- **p. 14 / Figure/Table caption - extractive body cue:** Fig. 8: Comparison between Go2 blind policy and vision policy. The blind policy failed to avoid the obstacles and got stuck. The vision policy detected ...

- **Evidence anchors reviewed:** datasets p. 6 (III. EXPERIMENTS), p. 5 (III. EXPERIMENTS), p. 7 (III. EXPERIMENTS), p. 7 (III. EXPERIMENTS), p. 5 (III. EXPERIMENTS), p. 6 (III. EXPERIMENTS), metrics p. 6 (III. EXPERIMENTS), p. 7 (III. EXPERIMENTS), p. 7 (III. EXPERIMENTS), p. 8 (III. EXPERIMENTS), p. 6 (III. EXPERIMENTS), p. 17 (Figure/Table caption), baselines p. 7 (III. EXPERIMENTS), p. 6 (III. EXPERIMENTS), p. 6 (III. EXPERIMENTS), p. 7 (III. EXPERIMENTS), p. 8 (III. EXPERIMENTS), p. 8 (III. EXPERIMENTS), results p. 8 (III. EXPERIMENTS), p. 6 (III. EXPERIMENTS), p. 7 (III. EXPERIMENTS), p. 6 (III. EXPERIMENTS), p. 7 (III. EXPERIMENTS), p. 8 (III. EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** As shown in Table II, our method significantly outperforms NaVid, the current state-of-the-art model, with a substantial 10% improvement in SR. (p. 6, III. EXPERIMENTS).
- **Metric evidence:** Error ↓ Collision Rate ↓ ROA(w/BCLoss) [68] 0.189 0.152 3.25 ROA [68] 0.161 0.152 3.09 NaVILA 0.066 0.113 0.81 the vision-based policy outperforms the blind policy by 14% in Success ... (p. 7, III. EXPERIMENTS).
- **Baseline/ablation evidence:** We also compare NaVILAs with a baseline using Oracle's low-level policy (assuming perfect command execution without realistic physics). (p. 7, III. EXPERIMENTS).
- **Failure/negative evidence:** While NaVILA demonstrates strong performance, it fails in some real-world cases (see Appx. (p. 9, V. CONCLUSION AND LIMITATIONS).
