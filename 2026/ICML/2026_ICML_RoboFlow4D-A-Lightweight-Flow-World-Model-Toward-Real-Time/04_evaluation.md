# Evaluation - RoboFlow4D: A Lightweight Flow World Model Toward Real-Time Flow-Guided Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=fh6XBnjFlv; PDF retrieval source: https://openreview.net/pdf/17509091f9a7574439da683639d4af0b20b10d5e.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.2. Main Results), p. 8 (Figure/Table caption), p. 8 (4.4. Real-World Experiments), p. 6 (4.2. Main Results), p. 7 (4.3. Ablation Study), p. 7 (4.3. Ablation Study)): DP achieves substantial improvements in success rates of 8.2%, 8.0%, and 6.2% on Spatial, Long, and average, respectively.

## Evaluation Body Digest

- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** We evaluate our method on two widely recognized robotic benchmarks: (1) LIBERO (Liu et al., 2023), a lifelong learning benchmark with 5 suites spanning 130 ...
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** For LIBERO, we follow the standard benchmark setup and use multi-view observations from a third-view camera and a wrist-mounted camera, training on the official demonstration ...
- **p. 7 / 4.2. Main Results - extractive PDF cue:** Quantitative results of VLAs for fine-tuned robotic manipulation tasks on the LIBERO benchmark.
- **p. 8 / 4.4. Real-World Experiments - extractive PDF cue:** Real-world robot platform. consistently improves success rates by a large margin and reduces task completion time across various policies, including DP and DiT.
- **p. 8 / 4.4. Real-World Experiments - extractive PDF cue:** This can be attributed to the benefits of goal-oriented flow plan guidance for the action policy, which provides more efficient and accurate trajectories that mitigate ...
- **p. 7 / 4.4. Real-World Experiments - extractive PDF cue:** We validate the generalization of our approach on 4 representative real-world tasks.
- **p. 8 / 4.4. Real-World Experiments - extractive PDF cue:** Real-world performance in terms of Success rate (%) and efficiency (completion time (seconds)).
- **p. 7 / 4.3. Ablation Study - extractive PDF cue:** We evaluate the robustness of our dual-system on LIBERO-10 and report the average success rate (%).

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.1. Experimental Setup (p. 6); 4.2. Main Results (p. 6); 4.4. Real-World Experiments (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Main Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | DP achieves substantial improvements in success rates of 8.2%, 8.0%, and 6.2% on Spatial, Long, and average, respectively. | p. 6 (4.2. Main Results) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 4. Real-world robot platform. consistently improves success rates by a large margin and reduces task completion time across various policies, includ- ing DP ... | p. 8 (Figure/Table caption) |
| 4.4. Real-World Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Generally, both DP and DiT equipped with RoboFlow4D achieve better or competitive success rates and less task completion time compared to other approaches. | p. 8 (4.4. Real-World Experiments) |
| 4.2. Main Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | All baselines exhibit low success rates in such a difficult setting. | p. 6 (4.2. Main Results) |
| 4.3. Ablation Study | EMPIRICAL / REAL-ROBOT OR HARDWARE | We evaluate the robustness of our dual-system on LIBERO-10 and report the average success rate (%). | p. 7 (4.3. Ablation Study) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** We evaluate our method on two widely recognized robotic benchmarks: (1) LIBERO (Liu et al., 2023), a lifelong learning benchmark with 5 suites spanning 130 ...
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** For LIBERO, we follow the standard benchmark setup and use multi-view observations from a third-view camera and a wrist-mounted camera, training on the official demonstration ...
- **p. 7 / 4.2. Main Results - extractive PDF cue:** Quantitative results of VLAs for fine-tuned robotic manipulation tasks on the LIBERO benchmark.
- **p. 8 / 4.4. Real-World Experiments - extractive PDF cue:** Real-world robot platform. consistently improves success rates by a large margin and reduces task completion time across various policies, including DP and DiT.
- **p. 8 / 4.4. Real-World Experiments - extractive PDF cue:** This can be attributed to the benefits of goal-oriented flow plan guidance for the action policy, which provides more efficient and accurate trajectories that mitigate ...
- **p. 7 / 4.4. Real-World Experiments - extractive PDF cue:** We validate the generalization of our approach on 4 representative real-world tasks.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Top left: System-level comparison of various flow-based planning. (a) 2D flow-based planning (Vecerik et al., 2024; Xu et al., 2024) predicts pixel-level flow ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. Overview of robotic manipulation. Top left (Sec. 3.2): Given an RGB image sequence, optional gripper query points, and a task instruction, the proposed ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3. Data generation pipeline. Stage one: We track the flows of the grounded gripper from diverse real-world and simulated robot videos. (Khazatsky et al., ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1. Success rates (%). Quantitative results of VLAs for fine-tuned robotic manipulation tasks on the LIBERO benchmark. Best results are in bold and second-best ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Success rates (%). Each task is evaluated over 100 trials. Best results are in bold and second-best results are underlined.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Ablation on Modular Design. Experiments are con- ducted in the same inference settings.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 4. Ablation on Dual-System Frequency. We evaluate the robustness of our dual-system on LIBERO-10 and report the average success rate (%). The fast system ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 5. Real-world performance in terms of Success rate (%) and efficiency (completion time (seconds)). Each task is evaluated over an average of 20 trials. ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We evaluate our method on two widely recognized robotic benchmarks: (1) LIBERO (Liu et al., 2023), a lifelong learning benchmark with 5 suites spanning ... | embodiment, simulator version and control stack | p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup) |
| Task/environment | For LIBERO, we follow the standard benchmark setup and use multi-view observations from a third-view camera and a wrist-mounted camera, training on the official ... | reset, timeout, object/scene variation | p. 6 (4.1. Experimental Setup), p. 7 (4.2. Main Results) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 3 (3.1. Overview), p. 2 (1. Introduction) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 4 (3.2. RoboFlow4D), p. 4 (3.2. RoboFlow4D) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Real-world performance in terms of Success rate (%) and efficiency (completion time (seconds)). | definition/direction/unit from same section | p. 8 (4.4. Real-World Experiments) |
| We evaluate the robustness of our dual-system on LIBERO-10 and report the average success rate (%). | definition/direction/unit from same section | p. 7 (4.3. Ablation Study) |
| Generally, both DP and DiT equipped with RoboFlow4D achieve better or competitive success rates and less task completion time compared to other approaches. | definition/direction/unit from same section | p. 8 (4.4. Real-World Experiments) |
| All baselines exhibit low success rates in such a difficult setting. | definition/direction/unit from same section | p. 6 (4.2. Main Results) |
| DP achieves substantial improvements in success rates of 8.2%, 8.0%, and 6.2% on Spatial, Long, and average, respectively. | definition/direction/unit from same section | p. 6 (4.2. Main Results) |
| As shown in the table, the success rate remains steady across different r ∈{4, 2, 1} for both DP and DiT controllers, indicating that ... | definition/direction/unit from same section | p. 7 (4.3. Ablation Study) |
| Figure 8. Real-world Visualization. Diffusion Loss. It computes a visibility-weighted mean-squared error: Ldiff = Et,ϵ " 1 P k,n wk,n K | definition/direction/unit from same section | p. 16 (Figure/Table caption) |
| Figure 2. Overview of robotic manipulation. Top left (Sec. 3.2): Given an RGB image sequence, optional gripper query points, and a task instruction, the ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| All baselines exhibit low success rates in such a difficult setting. | comparison identity and matched condition | p. 6 (4.2. Main Results) |
| RoboFlow4D strengthens efficient controllers competitive with large VLA baselines. | comparison identity and matched condition | p. 6 (4.2. Main Results) |
| We compare our method with two open-source state-of-the-art methods for real-world experiments, including π0 (Black et al., 2026) and π0-Fast (Pertsch et al., 2025). | comparison identity and matched condition | p. 7 (4.4. Real-World Experiments) |
| Similar results from DiT can also be observed, such as 43.8% SR, 38.3 s in Avg., notably surpassing the state-of-the-art approach π0's 41.3% and ... | comparison identity and matched condition | p. 8 (4.4. Real-World Experiments) |
| Generally, both DP and DiT equipped with RoboFlow4D achieve better or competitive success rates and less task completion time compared to other approaches. | comparison identity and matched condition | p. 8 (4.4. Real-World Experiments) |
| Method ℓ2 Error ↓ RoboFlow4D 0.0142 w/o Context Token 0.0152 w/o Query Points 0.0158 w/o 3D Alignment 0.0160 Dual-System Frequency Ablation. | comparison identity and matched condition | p. 7 (4.3. Ablation Study) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Method ℓ2 Error ↓ RoboFlow4D 0.0142 w/o Context Token 0.0152 w/o Query Points 0.0158 w/o 3D Alignment 0.0160 Dual-System Frequency Ablation. | component/input/data sensitivity | p. 7 (4.3. Ablation Study) |
| In contrast, our lightweight (0.76B-parameter) RoboFlow4D directly predicts the 4D motion prior in a single forward pass within 1 s without video synthesis, enabling ... | component/input/data sensitivity | p. 8 (4.4. Real-World Experiments) |
| Table 3. Ablation on Modular Design. Experiments are con- ducted in the same inference settings. | component/input/data sensitivity | p. 7 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| As an important cornerstone toward developing embodied generalist agents, recent learning-based manipulation ap- *Equal contribution †Corresponding authors. | DP achieves substantial improvements in success rates of 8.2%, 8.0%, and 6.2% on Spatial, Long, and average, respectively. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.2. Main Results), p. 8 (Figure/Table caption), p. 8 (4.4. Real-World Experiments), p. 6 (4.2. Main Results), p. 7 (4.3. Ablation Study), p. 7 (4.3. Ablation Study) |
| Primary metric/result | Figure 4. Real-world robot platform. consistently improves success rates by a large margin and reduces task completion time across various policies, includ- ing DP ... | numeric claim only at cited anchor | p. 8 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** We evaluate our method on two widely recognized robotic benchmarks: (1) LIBERO (Liu et al., 2023), a lifelong learning benchmark with 5 suites spanning 130 ...
- **p. 7 / 4.2. Main Results - extractive PDF cue:** Each task is evaluated over 100 trials.
- **p. 7 / 4.4. Real-World Experiments - extractive PDF cue:** A single NVIDIA RTX 6000 GPU is used for all experiments.
- **p. 8 / 4.4. Real-World Experiments - extractive PDF cue:** Each task is evaluated over an average of 20 trials.
- **p. 8 / 4.4. Real-World Experiments - extractive PDF cue:** For example, DP achieves a 12.5% higher average success rate (SR) while reducing completion time (s) by an average of 1.4 s, as evidenced by ...
- **p. 8 / 4.4. Real-World Experiments - extractive PDF cue:** Similar results from DiT can also be observed, such as 43.8% SR, 38.3 s in Avg., notably surpassing the state-of-the-art approach π0's 41.3% and 40.7 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Bottom: In the observation-planning-execution closed loop, when errors occur (e.g., grasp failure), RoboFlow4D correctively re-plans flows to re-align the policy (recovery), such that the ... | p. 8 (4.4. Real-World Experiments) |
| body limitation/failure cue | We evaluate the robustness of our dual-system on LIBERO-10 and report the average success rate (%). | p. 7 (4.3. Ablation Study) |
| body limitation/failure cue | As shown in the table, the success rate remains steady across different r ∈{4, 2, 1} for both DP and DiT controllers, indicating that ... | p. 7 (4.3. Ablation Study) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| BC and ACT follow the official ManiSkill3 implementations, while OpenVLA follows the implementation of (Liu et al., 2024a). | p. 6 (4.1. Experimental Setup) |
| Each task is evaluated over 100 trials. | p. 7 (4.2. Main Results) |
| A single NVIDIA RTX 6000 GPU is used for all experiments. | p. 7 (4.4. Real-World Experiments) |
| Specifically, RoboFlow4D extracts visual, 2D point (optional), and textual features with their respective encoders. | p. 3 (3.1. Overview) |
| We leverage a Vision Encoder, a Point Encoder, and a Text Encoder to extract the corresponding tokens of each input modality. | p. 3 (3.2. RoboFlow4D) |
| We first use the Resampler to encode 3D geometry from context 4 | p. 4 (3.2. RoboFlow4D) |
| The task instruction is encoded by the Text Encoder (i.e., the text encoder of SigLip) into the text token Ttext ∈R1×C. | p. 4 (3.2. RoboFlow4D) |
| The multimodal condition is augmented with timestep information encoded by MLP. | p. 5 (3.2. RoboFlow4D) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 4.4. Real-World Experiments - extractive PDF cue:** Bottom: In the observation-planning-execution closed loop, when errors occur (e.g., grasp failure), RoboFlow4D correctively re-plans flows to re-align the policy (recovery), such that the robot ...
- **p. 7 / 4.3. Ablation Study - extractive PDF cue:** We evaluate the robustness of our dual-system on LIBERO-10 and report the average success rate (%).
- **p. 7 / 4.3. Ablation Study - extractive PDF cue:** As shown in the table, the success rate remains steady across different r ∈{4, 2, 1} for both DP and DiT controllers, indicating that our ...

- **PDF anchors reviewed:** datasets p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 7 (4.2. Main Results), p. 8 (4.4. Real-World Experiments), p. 8 (4.4. Real-World Experiments), p. 7 (4.4. Real-World Experiments), metrics p. 8 (4.4. Real-World Experiments), p. 7 (4.3. Ablation Study), p. 8 (4.4. Real-World Experiments), p. 6 (4.2. Main Results), p. 6 (4.2. Main Results), p. 7 (4.3. Ablation Study), baselines p. 6 (4.2. Main Results), p. 6 (4.2. Main Results), p. 7 (4.4. Real-World Experiments), p. 8 (4.4. Real-World Experiments), p. 8 (4.4. Real-World Experiments), p. 7 (4.3. Ablation Study), results p. 6 (4.2. Main Results), p. 8 (Figure/Table caption), p. 8 (4.4. Real-World Experiments), p. 6 (4.2. Main Results), p. 7 (4.3. Ablation Study), p. 7 (4.3. Ablation Study).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
