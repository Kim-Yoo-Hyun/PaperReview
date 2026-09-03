# Evaluation - Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=zyMvoKYWMZ; PDF retrieval source: https://openreview.net/pdf/01fd7931fc7be08bf369b6a34264822e6d1de9b9.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (6.1.2. ZERO-SHOT COMPARISONS IN THE REAL WORLD), p. 8 (6.5. LIBERO and CALVIN Benchmarks), p. 7 (6.1.2. ZERO-SHOT COMPARISONS IN THE REAL WORLD), p. 21 (Figure/Table caption), p. 4 (3. Dataset and Benchmark), p. 8 (6.3. Diverse Point-Cloud Inputs as Data Augmentation)): In particular, the overall average success rate for (Setting 2, DA3) reaches 62.5%, representing a 29.2% improvement over the strongest baseline SpatialVLA, which achieves 33.3%.

## Evaluation Body Digest

- **p. 3 / 3. Dataset and Benchmark - extractive body cue:** This dataset includes 15 object categories that appeared in the pre-training data, while the layouts and backgrounds are randomly generated and unseen during pre-training, resulting ...
- **p. 3 / 3. Dataset and Benchmark - extractive body cue:** To validate the effectiveness of pre-training in simulation, we constructed an RGBD evaluation dataset as a benchmark using the same procedure.
- **p. 8 / 6.3. Diverse Point-Cloud Inputs as Data Augmentation - extractive body cue:** Simulator Only Hybrid Point Cloud Sensor Only Simulation (Test SR, %) Simulator 80.0 81.1 N/A DA3 78.9 82.1 N/A Real-World (Zero-Shot) (Average SR, %) RealSense ...
- **p. 6 / 6.1.1. REAL-WORLD SETUP - extractive body cue:** Real-world deployment details (hardware, camera setup, and workspace) are provided in Appendix I.
- **p. 6 / 6.1.2. ZERO-SHOT COMPARISONS IN THE REAL WORLD - extractive body cue:** To evaluate ANY3D-VLA's zero-shot generalization ability and robustness in the real world, we design four challenging test sets: (1) Standard: Relatively simple scenes, with no ...
- **p. 8 / 6.5. LIBERO and CALVIN Benchmarks - extractive body cue:** We evaluate on two public simulation benchmarks: LIBERO (Object, Goal, Long, and Spatial) (Liu et al., 2023) and CALVIN (ABC→D) (Mees et al., 2022).
- **p. 5 / 6. Experiments Centered on ANY3D-VLA - extractive body cue:** We conduct a series of experiments around ANY3D-VLA to evaluate its performance (1) in real-world and simulation settings, (2) under different point-cloud sources, and (3) ...
- **p. 7 / 6.1.3. REAL-WORLD POST-TRAINING - extractive body cue:** To adapt to more diverse real-world tasks, we employ a two-stage training paradigm: imitation learning pre-training on large-scale synthetic data, followed by fine-tuning on a ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 3. Dataset and Benchmark (p. 3); 6. Experiments Centered on ANY3D-VLA (p. 5); 6.1. Real-World Experiments (p. 6); 6.5. LIBERO and CALVIN Benchmarks (p. 8).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 6.1.2. ZERO-SHOT COMPARISONS IN THE REAL WORLD | EMPIRICAL / REAL-ROBOT OR HARDWARE | In particular, the overall average success rate for (Setting 2, DA3) reaches 62.5%, representing a 29.2% improvement over the strongest baseline SpatialVLA, which achieves ... | p. 7 (6.1.2. ZERO-SHOT COMPARISONS IN THE REAL WORLD) |
| 6.5. LIBERO and CALVIN Benchmarks | EMPIRICAL / REAL-ROBOT OR HARDWARE | ANY3D-VLA achieves good results: it improves over GraspVLA by 13.9% on LIBERO; on CALVIN, it increases the average length by 0.71 compared to GraspVLA; ... | p. 8 (6.5. LIBERO and CALVIN Benchmarks) |
| 6.1.2. ZERO-SHOT COMPARISONS IN THE REAL WORLD | EMPIRICAL / REAL-ROBOT OR HARDWARE | When the point-cloud source at inference is held fixed, hybrid point cloud training (Setting 2) typically achieves higher average success rates than training with ... | p. 7 (6.1.2. ZERO-SHOT COMPARISONS IN THE REAL WORLD) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 12. Performance improvements when introducing the 3D branch into the backbone π0.5 on the LIBERO and CALVIN benchmarks. LIBERO Benchmark (Success Rate %) | p. 21 (Figure/Table caption) |
| 3. Dataset and Benchmark | EMPIRICAL / REAL-ROBOT OR HARDWARE | Method Single-Trial Test Grasp SR (%) SR (%) SR (%) 2D-only 45.3 72.6 80.0 Implicit-depth RGB 55.8 78.9 85.3 Implicit-3D RGB 46.3 78.9 87.4 ... | p. 4 (3. Dataset and Benchmark) |

## Dataset / Benchmark Role

- **p. 3 / 3. Dataset and Benchmark - extractive body cue:** This dataset includes 15 object categories that appeared in the pre-training data, while the layouts and backgrounds are randomly generated and unseen during pre-training, resulting ...
- **p. 3 / 3. Dataset and Benchmark - extractive body cue:** To validate the effectiveness of pre-training in simulation, we constructed an RGBD evaluation dataset as a benchmark using the same procedure.
- **p. 8 / 6.3. Diverse Point-Cloud Inputs as Data Augmentation - extractive body cue:** Simulator Only Hybrid Point Cloud Sensor Only Simulation (Test SR, %) Simulator 80.0 81.1 N/A DA3 78.9 82.1 N/A Real-World (Zero-Shot) (Average SR, %) RealSense ...
- **p. 6 / 6.1.1. REAL-WORLD SETUP - extractive body cue:** Real-world deployment details (hardware, camera setup, and workspace) are provided in Appendix I.
- **p. 6 / 6.1.2. ZERO-SHOT COMPARISONS IN THE REAL WORLD - extractive body cue:** To evaluate ANY3D-VLA's zero-shot generalization ability and robustness in the real world, we design four challenging test sets: (1) Standard: Relatively simple scenes, with no ...
- **p. 8 / 6.5. LIBERO and CALVIN Benchmarks - extractive body cue:** We evaluate on two public simulation benchmarks: LIBERO (Object, Goal, Long, and Spatial) (Liu et al., 2023) and CALVIN (ABC→D) (Mees et al., 2022).
- **p. 5 / 6. Experiments Centered on ANY3D-VLA - extractive body cue:** We conduct a series of experiments around ANY3D-VLA to evaluate its performance (1) in real-world and simulation settings, (2) under different point-cloud sources, and (3) ...
- **p. 7 / 6.1.3. REAL-WORLD POST-TRAINING - extractive body cue:** To adapt to more diverse real-world tasks, we employ a two-stage training paradigm: imitation learning pre-training on large-scale synthetic data, followed by fine-tuning on a ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. We propose ANY3D-VLA. It unifies simulator, sensor, and model-estimated point clouds in the training pipeline (a), enabling diverse inputs and learning domain-agnostic 3D ...
- **p. 4 / Figure/Table caption - extractive body cue:** Table 1. Summary of the five settings. Let v be the view index, denoting the observation from the v-th camera (out of V views). Let ...
- **p. 4 / Figure/Table caption - extractive body cue:** Table 2. Comparison of different observation spaces and visual representations in the simulator. ‘Single-Trial SR' denotes success on the first attempt, ‘Test SR' within three ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 2. Zero-shot comparisons in the real world. For the training dataset, Setting 1 utilizes only the simulator point cloud, whereas Setting 2 incorporates both ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3. Example of Task 1: "Move pink tulip to vase".
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Example of Task 2: "Move condiment cup into right slot of cup carrier". To adapt to more diverse real-world tasks, we employ a ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Success rates of post-training tasks. During inference, Re- alSense refers to the sensor-based point cloud, while DA3 refers to the point cloud derived ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4. Efficiency-performance trade-off. Inference speeds are measured on a single NVIDIA RTX 3090 GPU. Depth Source Inference Speed Point Cloud Size Remarks 2D baseline ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | This dataset includes 15 object categories that appeared in the pre-training data, while the layouts and backgrounds are randomly generated and unseen during pre-training, ... | embodiment, simulator version and control stack | p. 3 (3. Dataset and Benchmark), p. 3 (3. Dataset and Benchmark) |
| Task/environment | To validate the effectiveness of pre-training in simulation, we constructed an RGBD evaluation dataset as a benchmark using the same procedure. | reset, timeout, object/scene variation | p. 3 (3. Dataset and Benchmark), p. 8 (6.3. Diverse Point-Cloud Inputs as Data Augmentation) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 5 (5.3. Training Strategy), p. 1 (1. Introduction) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 2 (1. Introduction), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We evaluate the models in simulation, training until the success rate converges, and then select the best-performing checkpoint for real-world testing. | definition/direction/unit from same section | p. 6 (6.1.1. REAL-WORLD SETUP) |
| Success rates of post-training tasks. | definition/direction/unit from same section | p. 7 (6.1.3. REAL-WORLD POST-TRAINING) |
| In particular, the overall average success rate for (Setting 2, DA3) reaches 62.5%, representing a 29.2% improvement over the strongest baseline SpatialVLA, which achieves ... | definition/direction/unit from same section | p. 7 (6.1.2. ZERO-SHOT COMPARISONS IN THE REAL WORLD) |
| Success rates of ANY3D-VLA across three different training configurations (simulator only, hybrid point cloud, sensor only). | definition/direction/unit from same section | p. 8 (6.3. Diverse Point-Cloud Inputs as Data Augmentation) |
| Method Single-Trial Test Grasp SR (%) SR (%) SR (%) 2D-only (DINOv2-L+SigLIP) 45.3 72.6 80.0 3D-only 44.2 64.2 91.6 3D + SigLIP 42.1 69.5 ... | definition/direction/unit from same section | p. 8 (6.4. Ablation Study) |
| Table 12. Performance improvements when introducing the 3D branch into the backbone π0.5 on the LIBERO and CALVIN benchmarks. LIBERO Benchmark (Success Rate %) | definition/direction/unit from same section | p. 21 (Figure/Table caption) |
| Table 8. Evaluation of ANY3D-VLA (trained purely on simulator point cloud) in the simulator using the same RGB input with point clouds from different ... | definition/direction/unit from same section | p. 18 (Figure/Table caption) |
| We jointly consider prediction accuracy and inference latency, and conduct a qualitative comparison via point-cloud visualizations, ultimately selecting Depth Anything 3 (Lin et al., ... | definition/direction/unit from same section | p. 6 (6.1.1. REAL-WORLD SETUP) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| ANY3DVLA outperforms the baselines on both tasks. | comparison identity and matched condition | p. 7 (6.1.3. REAL-WORLD POST-TRAINING) |
| ANY3D-VLA outperforms all baselines across four real-world evaluation scenarios. | comparison identity and matched condition | p. 7 (6.1.2. ZERO-SHOT COMPARISONS IN THE REAL WORLD) |
| We select π0.5 (Black et al., 2025a) and GraspVLA (Deng et al., 2025) as 2D VLA baselines, and SpatialVLA (Qu et al., 2025) as ... | comparison identity and matched condition | p. 6 (6.1.1. REAL-WORLD SETUP) |
| Furthermore, compared to higher-frequency policies, our model executes a larger motion per step (roughly 2-3× longer). | comparison identity and matched condition | p. 8 (0.3 FPS) |
| While estimating point clouds inherently introduces computational overhead compared to purely 2D approaches, we employ action chunking with a chunk size of 4, which ... | comparison identity and matched condition | p. 8 (0.3 FPS) |
| Method Single-Trial Test Grasp SR (%) SR (%) SR (%) 2D-only 45.3 72.6 80.0 Implicit-depth RGB 55.8 78.9 85.3 Implicit-3D RGB 46.3 78.9 87.4 ... | comparison identity and matched condition | p. 4 (3. Dataset and Benchmark) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Ablation study on the effect of 2D-3D fusion. | component/input/data sensitivity | p. 8 (6.4. Ablation Study) |
| Specifically, π0.5 and SpatialVLA are fine-tuned from their publicly released pretrained weights, whereas GraspVLA and our model are first pretrained on our synthetic RGBD ... | component/input/data sensitivity | p. 8 (6.5. LIBERO and CALVIN Benchmarks) |
| To adapt to more diverse real-world tasks, we employ a two-stage training paradigm: imitation learning pre-training on large-scale synthetic data, followed by fine-tuning on ... | component/input/data sensitivity | p. 7 (6.1.3. REAL-WORLD POST-TRAINING) |
| (2) We uniformly freeze the image encoder and only fine-tune the last four layers of the other branch (if present). | component/input/data sensitivity | p. 3 (3. Dataset and Benchmark) |
| Implicit-depth RGB oimpl-depth t = {I(v) t }v × × Two-branch encoders: (1) standard image encoder (DINOv2+SigLIP), (2) depthpretrained image encoder (Depth Anything v2 ... | component/input/data sensitivity | p. 4 (3. Dataset and Benchmark) |
| Point cloud-2D patch fusion opc t : {[I(v) t , D(v) t ]}v → Pt √ √ Lift RGBD to point cloud Pt = ... | component/input/data sensitivity | p. 4 (3. Dataset and Benchmark) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The contributions of this paper are summarized as follows: (1) We propose ANY3D-VLA. | In particular, the overall average success rate for (Setting 2, DA3) reaches 62.5%, representing a 29.2% improvement over the strongest baseline SpatialVLA, which achieves ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (6.1.2. ZERO-SHOT COMPARISONS IN THE REAL WORLD), p. 8 (6.5. LIBERO and CALVIN Benchmarks), p. 7 (6.1.2. ZERO-SHOT COMPARISONS IN THE REAL WORLD), p. 21 (Figure/Table caption), p. 4 (3. Dataset and Benchmark), p. 8 (6.3. Diverse Point-Cloud Inputs as Data Augmentation) |
| Primary metric/result | ANY3D-VLA achieves good results: it improves over GraspVLA by 13.9% on LIBERO; on CALVIN, it increases the average length by 0.71 compared to GraspVLA; ... | numeric claim only at cited anchor | p. 8 (6.5. LIBERO and CALVIN Benchmarks) |

- Numeric sentences retained from the body:
- **p. 3 / 3. Dataset and Benchmark - extractive body cue:** This dataset includes 15 object categories that appeared in the pre-training data, while the layouts and backgrounds are randomly generated and unseen during pre-training, resulting ...
- **p. 4 / 3. Dataset and Benchmark - extractive body cue:** Method Single-Trial Test Grasp SR (%) SR (%) SR (%) 2D-only 45.3 72.6 80.0 Implicit-depth RGB 55.8 78.9 85.3 Implicit-3D RGB 46.3 78.9 87.4 RGBD ...
- **p. 6 / 6.1.2. ZERO-SHOT COMPARISONS IN THE REAL WORLD - extractive body cue:** Each subtask is repeated twice, totaling 120 trials; each trial allows up to three grasping attempts.
- **p. 7 / 6.1.3. REAL-WORLD POST-TRAINING - extractive body cue:** During evaluation, we conduct 15 trials for each task, with three grasp attempts allowed per trial.
- **p. 7 / 6.2. Inference Efficiency and Latency - extractive body cue:** Inference speeds are measured on a single NVIDIA RTX 3090 GPU.
- **p. 8 / 0.3 FPS - extractive body cue:** As a result, an operating frequency of 1.7-2.0 FPS remains highly feasible for our target scenario of tabletop manipulation.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Although we have evaluated this work in both simulation and real-world manipulation settings, several limitations remain: (1) Our real-world experiments currently cover only a ... | p. 8 (7. Limitations and Future Work) |
| body limitation/failure cue | We also conduct a qualitative analysis to highlight the robustness of our method compared to baselines and to discuss shared limitations (Appendix J). | p. 7 (6.1.2. ZERO-SHOT COMPARISONS IN THE REAL WORLD) |
| body limitation/failure cue | Future work could extend to additional robot platforms and environments, and evaluate more complex, long-horizon tasks. | p. 8 (7. Limitations and Future Work) |
| body limitation/failure cue | Expert trajectories are produced by generating candidate grasp poses with BoDex (Chen et al., 2025b), performing oneshot collision-avoidance trajectory planning with CuRobo (Sundaralingam et ... | p. 3 (3. Dataset and Benchmark) |
| body limitation/failure cue | To isolate the impact of observation space design and visual representation construction on VLA performance, we adopt the following controlled settings: (1) We use ... | p. 3 (3. Dataset and Benchmark) |
| body limitation/failure cue | 2D backbones struggle to effectively infer occlusion relationships and absolute scales from flattened depth maps. | p. 4 (3. Dataset and Benchmark) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Under the same point-cloud source at inference time, hybrid point cloud training consistently performs better than training with RealSense point clouds only, achieving the ... | p. 7 (6.1.3. REAL-WORLD POST-TRAINING) |
| For Setting 2, the model is exposed to all point-cloud types throughout training, encouraging the 3D encoder and fusion layers to learn geometric patterns ... | p. 5 (5.3. Training Strategy) |
| Training hyperparameters for each model are provided in Table 9 (Appendix H). | p. 6 (6.1.1. REAL-WORLD SETUP) |
| Real-world deployment details (hardware, camera setup, and workspace) are provided in Appendix I. | p. 6 (6.1.1. REAL-WORLD SETUP) |
| Inference speeds are measured on a single NVIDIA RTX 3090 GPU. | p. 7 (6.2. Inference Efficiency and Latency) |
| After introducing full 2D-3D fusion, the Single-Trial SR improves from 45.3% (2D-only) and 44.2% (3D-only) to 61.1%, with the other two metrics improving accordingly. | p. 8 (6.4. Ablation Study) |
| To verify the necessity of our 2D-3D fusion design, we conduct an ablation study on the key components of the visual encoder under a ... | p. 8 (6.4. Ablation Study) |
| (2) We uniformly freeze the image encoder and only fine-tune the last four layers of the other branch (if present). | p. 3 (3. Dataset and Benchmark) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 7. Limitations and Future Work - extractive body cue:** Although we have evaluated this work in both simulation and real-world manipulation settings, several limitations remain: (1) Our real-world experiments currently cover only a single ...
- **p. 7 / 6.1.2. ZERO-SHOT COMPARISONS IN THE REAL WORLD - extractive body cue:** We also conduct a qualitative analysis to highlight the robustness of our method compared to baselines and to discuss shared limitations (Appendix J).
- **p. 8 / 7. Limitations and Future Work - extractive body cue:** Future work could extend to additional robot platforms and environments, and evaluate more complex, long-horizon tasks.
- **p. 3 / 3. Dataset and Benchmark - extractive body cue:** Expert trajectories are produced by generating candidate grasp poses with BoDex (Chen et al., 2025b), performing oneshot collision-avoidance trajectory planning with CuRobo (Sundaralingam et al., ...
- **p. 3 / 3. Dataset and Benchmark - extractive body cue:** To isolate the impact of observation space design and visual representation construction on VLA performance, we adopt the following controlled settings: (1) We use the ...
- **p. 4 / 3. Dataset and Benchmark - extractive body cue:** 2D backbones struggle to effectively infer occlusion relationships and absolute scales from flattened depth maps.

- **Evidence anchors reviewed:** datasets p. 3 (3. Dataset and Benchmark), p. 3 (3. Dataset and Benchmark), p. 8 (6.3. Diverse Point-Cloud Inputs as Data Augmentation), p. 6 (6.1.1. REAL-WORLD SETUP), p. 6 (6.1.2. ZERO-SHOT COMPARISONS IN THE REAL WORLD), p. 8 (6.5. LIBERO and CALVIN Benchmarks), metrics p. 6 (6.1.1. REAL-WORLD SETUP), p. 7 (6.1.3. REAL-WORLD POST-TRAINING), p. 7 (6.1.2. ZERO-SHOT COMPARISONS IN THE REAL WORLD), p. 8 (6.3. Diverse Point-Cloud Inputs as Data Augmentation), p. 8 (6.4. Ablation Study), p. 21 (Figure/Table caption), baselines p. 7 (6.1.3. REAL-WORLD POST-TRAINING), p. 7 (6.1.2. ZERO-SHOT COMPARISONS IN THE REAL WORLD), p. 6 (6.1.1. REAL-WORLD SETUP), p. 8 (0.3 FPS), p. 8 (0.3 FPS), p. 4 (3. Dataset and Benchmark), results p. 7 (6.1.2. ZERO-SHOT COMPARISONS IN THE REAL WORLD), p. 8 (6.5. LIBERO and CALVIN Benchmarks), p. 7 (6.1.2. ZERO-SHOT COMPARISONS IN THE REAL WORLD), p. 21 (Figure/Table caption), p. 4 (3. Dataset and Benchmark), p. 8 (6.3. Diverse Point-Cloud Inputs as Data Augmentation).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (21 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Method Single-Trial Test Grasp SR (%) SR (%) SR (%) 2D-only 45.3 72.6 80.0 Implicit-depth RGB 55.8 78.9 85.3 Implicit-3D RGB 46.3 78.9 87.4 RGBD image-plane 56.8 76.8 87.4 Point ... (p. 4, 3. Dataset and Benchmark).
- **Metric evidence:** Method Single-Trial Test Grasp SR (%) SR (%) SR (%) 2D-only 45.3 72.6 80.0 Implicit-depth RGB 55.8 78.9 85.3 Implicit-3D RGB 46.3 78.9 87.4 RGBD image-plane 56.8 76.8 87.4 Point ... (p. 4, 3. Dataset and Benchmark).
- **Baseline/ablation evidence:** ANY3DVLA outperforms the baselines on both tasks. (p. 7, 6.1.3. REAL-WORLD POST-TRAINING).
- **Failure/negative evidence:** Although we have evaluated this work in both simulation and real-world manipulation settings, several limitations remain: (1) Our real-world experiments currently cover only a single robotic arm and a limited ... (p. 8, 7. Limitations and Future Work).
