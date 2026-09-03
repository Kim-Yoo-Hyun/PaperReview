# Evaluation - LaST$_{0}$: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=lwOoBzJykL; PDF retrieval source: https://openreview.net/pdf/0e9ec532d1e01f801ca9bc49e258c05cf3a207f5.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4.3. Real-World Experiment), p. 7 (15.4 Hz), p. 7 (15.4 Hz), p. 8 (4.2. Ablation Study), p. 6 (4.1. Simulation Experiment), p. 9 (4.3. Real-World Experiment)): As shown in Table 3, LaST0 achieves the best overall performance on realworld manipulation tasks, with a mean success rate of 72% (±3) on Franka platform (not including the long-horizon ...

## Evaluation Body Digest

- **p. 6 / 4.1. Simulation Experiment - extractive body cue:** For the LIBERO (Liu et al., 2024) benchmark, our evaluation leverages its four specialized dataset suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-Long.
- **p. 8 / 4.3. Real-World Experiment - extractive body cue:** We evaluated our method on a set of real-world manipulation tasks using both single-arm and dual-arm Franka robot setups, as well as AgileX mobile manipulation ...
- **p. 6 / 4.1. Simulation Experiment - extractive body cue:** For the RLBench benchmark, we evaluate on a diverse set of 10 tasks, conducted in the CoppeliaSim simulation environment.
- **p. 8 / 4.3. Real-World Experiment - extractive body cue:** In addition, we further evaluate a long-horizon setting on placing egg task, where the robot consecutively completes the full task three times while the positions ...
- **p. 7 / 15.4 Hz - extractive body cue:** While other methods fail to aggregate features from the manipulated objects and the robot, LaST0 exhibits a highly concentrated attention pattern, highlighting its superior spatio-temporal ...
- **p. 9 / 4.3. Real-World Experiment - extractive body cue:** Comparison across real-world manipulation tasks.
- **p. 9 / 4.3. Real-World Experiment - extractive body cue:** Visualization of Real-World Task Execution. success rates across all stages (0.66 →0.47 →0.33) compared to π0.5 (0.47 →0.20 →0.07), with the performance gap widening as ...
- **p. 7 / 15.4 Hz - extractive body cue:** Comparison of LaST0 and baselines on LIBERO benchmark.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4. Experiment (p. 6); 4.1. Simulation Experiment (p. 6); 4.3. Real-World Experiment (p. 8).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.3. Real-World Experiment | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Table 3, LaST0 achieves the best overall performance on realworld manipulation tasks, with a mean success rate of 72% (±3) on ... | p. 8 (4.3. Real-World Experiment) |
| 15.4 Hz | EMPIRICAL / REAL-ROBOT OR HARDWARE | In this suite, LaST0 achieves a 95.6% success rate, outperforming strong baselines such as OpenVLA-OFT (94.5%) and π0.5 (92.4%). | p. 7 (15.4 Hz) |
| 15.4 Hz | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Table 2, LaST0 consistently outperforms all baselines, achieving a SOTA mean success rate of 98.1%. | p. 7 (15.4 Hz) |
| 4.2. Ablation Study | EMPIRICAL / REAL-ROBOT OR HARDWARE | This configuration reach a 74% success rate, while our method achieves an 8% higher. | p. 8 (4.2. Ablation Study) |
| 4.1. Simulation Experiment | EMPIRICAL / REAL-ROBOT OR HARDWARE | Beyond the overall average, LaST0 attains the highest success rate on 7 out of 10 tasks, indicating consistent performance gains across diverse manipulation skills. | p. 6 (4.1. Simulation Experiment) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Simulation Experiment - extractive body cue:** For the LIBERO (Liu et al., 2024) benchmark, our evaluation leverages its four specialized dataset suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-Long.
- **p. 8 / 4.3. Real-World Experiment - extractive body cue:** We evaluated our method on a set of real-world manipulation tasks using both single-arm and dual-arm Franka robot setups, as well as AgileX mobile manipulation ...
- **p. 6 / 4.1. Simulation Experiment - extractive body cue:** For the RLBench benchmark, we evaluate on a diverse set of 10 tasks, conducted in the CoppeliaSim simulation environment.
- **p. 8 / 4.3. Real-World Experiment - extractive body cue:** In addition, we further evaluate a long-horizon setting on placing egg task, where the robot consecutively completes the full task three times while the positions ...
- **p. 7 / 15.4 Hz - extractive body cue:** While other methods fail to aggregate features from the manipulated objects and the robot, LaST0 exhibits a highly concentrated attention pattern, highlighting its superior spatio-temporal ...
- **p. 9 / 4.3. Real-World Experiment - extractive body cue:** Comparison across real-world manipulation tasks.
- **p. 9 / 4.3. Real-World Experiment - extractive body cue:** Visualization of Real-World Task Execution. success rates across all stages (0.66 →0.47 →0.33) compared to π0.5 (0.47 →0.20 →0.07), with the performance gap widening as ...
- **p. 7 / 15.4 Hz - extractive body cue:** Comparison of LaST0 and baselines on LIBERO benchmark.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Overview. (a) Unlike previous VLA methods that explicitly generate linguistic reasoning traces or future visual observations, (b) we propose LaST0, a framework that ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Framework. a) We propose LaST0, a unified VLA model with a dual-system architecture. The model is implemented via a MoT scheme with two ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. The reasoning expert performs low-frequency latent CoT reasoning to capture spatio-temporal dependencies, while the fast acting expert generates actions conditioned on high-frequency observations ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4. Attention heatmap visualizations from the last layer for three VLA models: (a) LaST0 without CoT reasoning, (b) the explicit CoT in CoT-VLA, and ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Comparison of LaST0 and baselines on RLBench benchmark. All methods are trained in the multi-task setting (Shridhar et al., 2022), and we report ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. Ablation study on key design choices of LaST0. We analyze (a) the importance of different latent modalities, (b) the number of tokens allocated ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Comparison of LaST0 and baselines on LIBERO benchmark. The best results are highlighted in bold. Models Spatial Object Goal Long Mean S.R. ↑
- **p. 9 / Figure/Table caption - extractive body cue:** Table 3. Comparison across real-world manipulation tasks. We report success rates (S.R.) for standard single-arm and dual-arm tasks (Franka), mobile manipulation (AgileX), and dexterous manipulation ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For the LIBERO (Liu et al., 2024) benchmark, our evaluation leverages its four specialized dataset suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-Long. | embodiment, simulator version and control stack | p. 6 (4.1. Simulation Experiment), p. 8 (4.3. Real-World Experiment) |
| Task/environment | We evaluated our method on a set of real-world manipulation tasks using both single-arm and dual-arm Franka robot setups, as well as AgileX mobile ... | reset, timeout, object/scene variation | p. 8 (4.3. Real-World Experiment), p. 6 (4.1. Simulation Experiment) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 4 (3.2. LaST0 Architecture), p. 4 (3.2. LaST0 Architecture) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 3 (3.1. Preliminaries), p. 5 (3.4. Dual-System Coordination) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Beyond the overall average, LaST0 attains the highest success rate on 7 out of 10 tasks, indicating consistent performance gains across diverse manipulation skills. | definition/direction/unit from same section | p. 6 (4.1. Simulation Experiment) |
| Following (Goyal et al., 2023), we perform 20 rollout trials per task using the final checkpoint, repeat the evaluation across three random seeds, and ... | definition/direction/unit from same section | p. 6 (4.1. Simulation Experiment) |
| In the Spatial and Object suites, which strictly evaluate generalization to novel layouts and objects, LaST0 nearly saturates the performance, reaching 99.2% and 99.6% ... | definition/direction/unit from same section | p. 7 (15.4 Hz) |
| As shown in Table 3, LaST0 achieves the best overall performance on realworld manipulation tasks, with a mean success rate of 72% (±3) on ... | definition/direction/unit from same section | p. 8 (4.3. Real-World Experiment) |
| Visualization of Real-World Task Execution. success rates across all stages (0.66 →0.47 →0.33) compared to π0.5 (0.47 →0.20 →0.07), with the performance gap widening ... | definition/direction/unit from same section | p. 9 (4.3. Real-World Experiment) |
| Results are reported as average success rates across 10 RLBench tasks. | definition/direction/unit from same section | p. 7 (15.4 Hz) |
| This configuration reach a 74% success rate, while our method achieves an 8% higher. | definition/direction/unit from same section | p. 8 (4.2. Ablation Study) |
| Mean S.R. denotes the average success rate. | definition/direction/unit from same section | p. 9 (4.3. Real-World Experiment) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| In this suite, LaST0 achieves a 95.6% success rate, outperforming strong baselines such as OpenVLA-OFT (94.5%) and π0.5 (92.4%). | comparison identity and matched condition | p. 7 (15.4 Hz) |
| We compare our method against three strong baselines: π0.5 (Black et al., 2024), a state-of-the-art 2D VLA model; SpatialVLA (Qu et al., 2025), a ... | comparison identity and matched condition | p. 8 (4.3. Real-World Experiment) |
| As shown in Table 2, LaST0 consistently outperforms all baselines, achieving a SOTA mean success rate of 98.1%. | comparison identity and matched condition | p. 7 (15.4 Hz) |
| For the LIBERO benchmark, we further augment the set of baselines with OpenVLA-OFT (Kim et al., 2025), a SOTA method for this benchmark. | comparison identity and matched condition | p. 6 (4.1. Simulation Experiment) |
| For RLBench benchmark, we benchmark LaST0 against six representative state-of-the-art (SOTA) VLA models: OpenVLA (Kim et al., 2024), π0.5 (Intelligence et al., 2025), CogACT ... | comparison identity and matched condition | p. 6 (4.1. Simulation Experiment) |
| Table 9. Action Inter-class Distance. Comparison of action feature separability with and without the proposed LaST0 framework. Model Architecture Action Inter-class Distance w/o LaST ... | comparison identity and matched condition | p. 19 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 10. Ablation on Latent Modalities. The effect of removing individual modalities on the action inter-class distance. Latent Modality Configuration Action Inter-class Distance w/o ... | component/input/data sensitivity | p. 19 (Figure/Table caption) |
| Models Spatial Object Goal Long Mean S.R. ↑ OpenVLA 84.7 88.4 79.2 53.7 76.5 SpatialVLA 88.2 89.9 84.6 55.5 78.1 CogACT 97.2 98.0 90.2 ... | component/input/data sensitivity | p. 7 (15.4 Hz) |
| Figure 9. Visualization of attention heatmaps. We visualize the attention heatmaps from the final layer of LaST0 on RLBench observations. The red area indicates ... | component/input/data sensitivity | p. 20 (Figure/Table caption) |
| Section 4.1 evaluates the manipulation performance and inference efficiency of LaST0 in simulation, while Section 4.2 conducts the ablation study of each component. | component/input/data sensitivity | p. 6 (4. Experiment) |
| 5 c), we investigate the effect of the temporal horizon used in latent reasoning by varying the number of future time steps encoded into ... | component/input/data sensitivity | p. 8 (4.2. Ablation Study) |
| Since the point cloud modality is unavailable in LIBERO, we remove it from the latent CoT content. | component/input/data sensitivity | p. 6 (4.1. Simulation Experiment) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions are summarized as follows: • We propose LaST0, a unified VLA model that enables efficient reason-before-act behavior through a Latent SpatioTemporal CoT, ... | As shown in Table 3, LaST0 achieves the best overall performance on realworld manipulation tasks, with a mean success rate of 72% (±3) on ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4.3. Real-World Experiment), p. 7 (15.4 Hz), p. 7 (15.4 Hz), p. 8 (4.2. Ablation Study), p. 6 (4.1. Simulation Experiment), p. 9 (4.3. Real-World Experiment) |
| Primary metric/result | In this suite, LaST0 achieves a 95.6% success rate, outperforming strong baselines such as OpenVLA-OFT (94.5%) and π0.5 (92.4%). | numeric claim only at cited anchor | p. 7 (15.4 Hz) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Simulation Experiment - extractive body cue:** For the RLBench benchmark, we evaluate on a diverse set of 10 tasks, conducted in the CoppeliaSim simulation environment.
- **p. 6 / 4.1. Simulation Experiment - extractive body cue:** Following the frame-sampling protocol adopted in (Shridhar et al., 2022), we construct a training dataset comprising 100 trajectories per task with keyframes.
- **p. 6 / 4.1. Simulation Experiment - extractive body cue:** We train LaST0 for 300 epochs during the Supervised Fine-Tuning (SFT) stage across both benchmarks, using the AdamW optimizer (Loshchilov & Hutter, 2017) on 8 ...
- **p. 6 / 4.1. Simulation Experiment - extractive body cue:** For LaST0, the single front-view RGB image is resized to 384 × 384, accompanied by a point cloud uniformly subsampled to 1024 points, task instructions, ...
- **p. 6 / 4.1. Simulation Experiment - extractive body cue:** Following (Goyal et al., 2023), we perform 20 rollout trials per task using the final checkpoint, repeat the evaluation across three random seeds, and report ...
- **p. 6 / 4.1. Simulation Experiment - extractive body cue:** In alignment with the official LIBERO protocol, each model is trained separately for each task suite, and we evaluate the final checkpoint on 500 trials ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We show more comprehensive visualizations in Appendix G and supplementary video, and failure cases in Appendix H. | p. 9 (4.3. Real-World Experiment) |
| body limitation/failure cue | Figure 11. Visualization of failure cases on different robot platforms, the task progresses from left to right, and red box highlights the failure positions. ... | p. 21 (Figure/Table caption) |
| body limitation/failure cue | Figure 12. Visualization of complete task execution processes by real-world tasks (from left to right). 3) The failure in the third case in the ... | p. 22 (Figure/Table caption) |
| body limitation/failure cue | Finally, we will explore reinforcement learning for post-training to enhance the robustness. | p. 9 (6. Limitations and Future Work) |
| body limitation/failure cue | Due to our fast-slow system design, extending the temporal horizon of the latent space does not significantly affect action generation speed. | p. 8 (4.2. Ablation Study) |
| body limitation/failure cue | Since adding further coverage beyond 4 steps does not significantly improve performance, we chose 4 steps as the final latent temporal coverage. | p. 8 (4.2. Ablation Study) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Following (Goyal et al., 2023), we perform 20 rollout trials per task using the final checkpoint, repeat the evaluation across three random seeds, and ... | p. 6 (4.1. Simulation Experiment) |
| In alignment with the official LIBERO protocol, each model is trained separately for each task suite, and we evaluate the final checkpoint on 500 ... | p. 6 (4.1. Simulation Experiment) |
| 5 c), we investigate the effect of the temporal horizon used in latent reasoning by varying the number of future time steps encoded into ... | p. 8 (4.2. Ablation Study) |
| The encoder yields a compact feature sequence fimg ∈RB×Nimg×dv, where B denotes the batch size, Nimg represents the sequence length, and dv is the ... | p. 3 (3.2. LaST0 Architecture) |
| Inference speed is evaluated on an NVIDIA 4090 GPU. | p. 7 (4.1. Simulation Experiment) |
| 2D 3D state 0 token 1 token 2 tokens 4 tokens 0 step 1 step 2 steps 4 steps 1:1 1:2 1:4 1:8 Mix ... | p. 7 (15.4 Hz) |
| Since adding further coverage beyond 4 steps does not significantly improve performance, we chose 4 steps as the final latent temporal coverage. | p. 8 (4.2. Ablation Study) |
| Point Cloud Encoder (training only). | p. 3 (3.2. LaST0 Architecture) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 4.3. Real-World Experiment - extractive body cue:** We show more comprehensive visualizations in Appendix G and supplementary video, and failure cases in Appendix H.
- **p. 21 / Figure/Table caption - extractive body cue:** Figure 11. Visualization of failure cases on different robot platforms, the task progresses from left to right, and red box highlights the failure positions. H. ...
- **p. 22 / Figure/Table caption - extractive body cue:** Figure 12. Visualization of complete task execution processes by real-world tasks (from left to right). 3) The failure in the third case in the dexterous ...
- **p. 9 / 6. Limitations and Future Work - extractive body cue:** Finally, we will explore reinforcement learning for post-training to enhance the robustness.
- **p. 8 / 4.2. Ablation Study - extractive body cue:** Due to our fast-slow system design, extending the temporal horizon of the latent space does not significantly affect action generation speed.
- **p. 8 / 4.2. Ablation Study - extractive body cue:** Since adding further coverage beyond 4 steps does not significantly improve performance, we chose 4 steps as the final latent temporal coverage.

- **Evidence anchors reviewed:** datasets p. 6 (4.1. Simulation Experiment), p. 8 (4.3. Real-World Experiment), p. 6 (4.1. Simulation Experiment), p. 8 (4.3. Real-World Experiment), p. 7 (15.4 Hz), p. 9 (4.3. Real-World Experiment), metrics p. 6 (4.1. Simulation Experiment), p. 6 (4.1. Simulation Experiment), p. 7 (15.4 Hz), p. 8 (4.3. Real-World Experiment), p. 9 (4.3. Real-World Experiment), p. 7 (15.4 Hz), baselines p. 7 (15.4 Hz), p. 8 (4.3. Real-World Experiment), p. 7 (15.4 Hz), p. 6 (4.1. Simulation Experiment), p. 6 (4.1. Simulation Experiment), p. 19 (Figure/Table caption), results p. 8 (4.3. Real-World Experiment), p. 7 (15.4 Hz), p. 7 (15.4 Hz), p. 8 (4.2. Ablation Study), p. 6 (4.1. Simulation Experiment), p. 9 (4.3. Real-World Experiment).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
