# Evaluation - ConsisVLA-4D: Advancing Spatiotemporal Consistency in Efficient 3D-Perception and 4D-Reasoning for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Li_ConsisVLA-4D_Advancing_Spatiotemporal_Consistency_in_Efficient_3D-Perception_and_4D-Reasoning_for_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_ConsisVLA-4D_Advancing_Spatiotemporal_Consistency_in_Efficient_3D-Perception_and_4D-Reasoning_for_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (5.2. Overall Performance & Efficiency), p. 7 (5.2. Overall Performance & Efficiency), p. 8 (5.3. Ablation Studies), p. 8 (5.4. Qualitative Analysis), p. 3 (Figure/Table caption), p. 6 (5.1. Experimental Setup)): Particularly, it achieves exceptional success rates of 98.8% and 99.8% in the Spatial and Object suites, which assess spatial perception and object recognition, respectively.

## Evaluation Body Digest

- **p. 6 / 5.1. Experimental Setup - extractive body cue:** We conduct evaluations across multiple simulation benchmarks, including: 1) the four task suites of LIBERO [44]-Spatial, Object, Goal, and Long; 2) three pick-and-place tasks emphasizing ...
- **p. 7 / 5.1. Experimental Setup - extractive body cue:** Simulation Results on RoboTwin 2.0 Benchmark.
- **p. 7 / 5.3. Ablation Studies - extractive body cue:** 5, for both simulation and real-world results: 1) Removing ES-Sel. and S-Fus. from CV-Aligner prevents the filtering of redundant visual inputs and fails to align ...
- **p. 6 / 5.1. Experimental Setup - extractive body cue:** ConsisVLA-4D is deployed on both the AgileX Cobot Magic [16] and Galaxea R1 Lite [17] platforms for real-world evaluations, covering four categories of long-horizon tasks: ...
- **p. 8 / 5.4. Qualitative Analysis - extractive body cue:** 6 illustrates the model's ability to execute manipulation tasks smoothly and accurately across four long-horizon real-world scenarios.
- **p. 8 / 5.3. Ablation Studies - extractive body cue:** Visualization of ConsisVLA-4D performing four long-horizon real-world manipulation tasks on the Galaxea R1 Lite platform, illustrating key execution-stage observations.
- **p. 7 / 5.1. Experimental Setup - extractive body cue:** Decimal values indicate averages over 15 trials, and the average success rate reflects complete task completion.
- **p. 7 / 5.2. Overall Performance & Efficiency - extractive body cue:** ConsisVLA-4D leads significantly in both phased and final success rates across 4 diverse long-horizon bimanual tasks, with strong performance stably maintained across deployment platforms (±1.7%).

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 5. Experiments (p. 6); 5.1. Experimental Setup (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5.2. Overall Performance & Efficiency | EMPIRICAL / REAL-ROBOT OR HARDWARE | Particularly, it achieves exceptional success rates of 98.8% and 99.8% in the Spatial and Object suites, which assess spatial perception and object recognition, respectively. | p. 7 (5.2. Overall Performance & Efficiency) |
| 5.2. Overall Performance & Efficiency | EMPIRICAL / REAL-ROBOT OR HARDWARE | ConsisVLA-4D leads significantly in both phased and final success rates across 4 diverse long-horizon bimanual tasks, with strong performance stably maintained across deployment platforms ... | p. 7 (5.2. Overall Performance & Efficiency) |
| 5.3. Ablation Studies | EMPIRICAL / REAL-ROBOT OR HARDWARE | The R = 1/8 setting achieves a favorable balance between performance and efficiency. | p. 8 (5.3. Ablation Studies) |
| 5.4. Qualitative Analysis | EMPIRICAL / REAL-ROBOT OR HARDWARE | Based on this correlation, ConsisVLA-4D achieves state-of-the-art performance with only 1/8 of the visual tokens (see Tab. | p. 8 (5.4. Qualitative Analysis) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 2. Efficient 3D-Perception ensures spatial consistency through the Cross-View Aligner (red) and Cross-Object Fuser (or- ange). The former employs an Explicit Semantic Object ... | p. 3 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 5.1. Experimental Setup - extractive body cue:** We conduct evaluations across multiple simulation benchmarks, including: 1) the four task suites of LIBERO [44]-Spatial, Object, Goal, and Long; 2) three pick-and-place tasks emphasizing ...
- **p. 7 / 5.1. Experimental Setup - extractive body cue:** Simulation Results on RoboTwin 2.0 Benchmark.
- **p. 7 / 5.3. Ablation Studies - extractive body cue:** 5, for both simulation and real-world results: 1) Removing ES-Sel. and S-Fus. from CV-Aligner prevents the filtering of redundant visual inputs and fails to align ...
- **p. 6 / 5.1. Experimental Setup - extractive body cue:** ConsisVLA-4D is deployed on both the AgileX Cobot Magic [16] and Galaxea R1 Lite [17] platforms for real-world evaluations, covering four categories of long-horizon tasks: ...
- **p. 8 / 5.4. Qualitative Analysis - extractive body cue:** 6 illustrates the model's ability to execute manipulation tasks smoothly and accurately across four long-horizon real-world scenarios.
- **p. 8 / 5.3. Ablation Studies - extractive body cue:** Visualization of ConsisVLA-4D performing four long-horizon real-world manipulation tasks on the Galaxea R1 Lite platform, illustrating key execution-stage observations.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Comparison with Existing Paradigms. Beyond con- ventional 2D visual inputs, Para. A employs explicit 3D/4D in- puts (e.g., point clouds, depth maps, historical ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Efficient 3D-Perception ensures spatial consistency through the Cross-View Aligner (red) and Cross-Object Fuser (or- ange). The former employs an Explicit Semantic Object Selec- ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. The Mechanism from 3D-Perception to 4D-Reasoning. The Cross-View Aligner selects spatial objects with matching identities across different views, and through 4D-Reasoning, further predicts ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. Efficient 4D-Reasoning. IK (implicit knowledge). Cross-Scene Thinker with Spatiotemporal Consistency Attention (SC-Attn) ensures: 1) Three sets of initialized dynamic tokens de- code dynamic ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Simulation Results on LIBERO Benchmark. Task suc- cess rates across four suites and their overall average.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Simulation Results on ManiSkill2 Benchmark. "†" denotes results reproduced under identical settings as ConsisVLA- 4D. The results are averaged over 20 or 100 ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 3. Efficiency Optimization Results. "†" denotes re- sults reproduced under identical settings as ConsisVLA-4D. La- tency and Throughput (T-put) represent the inference delay and ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. Simulation Results on RoboTwin 2.0 Benchmark. The tasks cover diverse scenarios, with each task conducted in 100 trials.

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We conduct evaluations across multiple simulation benchmarks, including: 1) the four task suites of LIBERO [44]-Spatial, Object, Goal, and Long; 2) three pick-and-place tasks ... | embodiment, simulator version and control stack | p. 6 (5.1. Experimental Setup), p. 7 (5.1. Experimental Setup) |
| Task/environment | Simulation Results on RoboTwin 2.0 Benchmark. | reset, timeout, object/scene variation | p. 7 (5.1. Experimental Setup), p. 7 (5.3. Ablation Studies) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 1 (Abstract), p. 1 (1. Introduction) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 4 (4.1. Proposed Framework), p. 3 (3. Preliminary & Problem Definition) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Decimal values indicate averages over 15 trials, and the average success rate reflects complete task completion. | definition/direction/unit from same section | p. 7 (5.1. Experimental Setup) |
| ConsisVLA-4D leads significantly in both phased and final success rates across 4 diverse long-horizon bimanual tasks, with strong performance stably maintained across deployment platforms ... | definition/direction/unit from same section | p. 7 (5.2. Overall Performance & Efficiency) |
| D. from SC-Attn causes success rate drops of 2.7%- 4.8% in simulation and 5.7%-11.6% in the real world. | definition/direction/unit from same section | p. 8 (5.3. Ablation Studies) |
| 2) Removing G-Fus. and IG-Agg. from CO-Fuser causes visual ambiguities in spatial relationships between objects, resulting in success rate drops of 8.2% and 13.3%. | definition/direction/unit from same section | p. 8 (5.3. Ablation Studies) |
| Each task includes 60, 60, 60, and 45 human-teleoperated demonstrations across both platforms. | definition/direction/unit from same section | p. 6 (5.1. Experimental Setup) |
| In real-world, we reproduce three representative models, including OpenVLA (base model), and OpenVLAOFT (the best 7B baseline in performance and efficiency), with training and ... | definition/direction/unit from same section | p. 6 (5.1. Experimental Setup) |
| Figure 2. Efficient 3D-Perception ensures spatial consistency through the Cross-View Aligner (red) and Cross-Object Fuser (or- ange). The former employs an Explicit Semantic Object ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 3, despite adding approximately 2B parameters (mainly from VGGT), ConsisVLA-4D achieves 2.31× and 1.25× speedups in inference latency and 1.36× and 1.43× speedups in ... | comparison identity and matched condition | p. 7 (5.2. Overall Performance & Efficiency) |
| For efficiency, we conduct fair comparisons between these three baselines with ConsisVLA-4D on the LIBERO and Galaxea R1 Lite platforms. | comparison identity and matched condition | p. 6 (5.1. Experimental Setup) |
| In simulation, ConsisVLA-4D is compared with multiple SOTA methods, including OpenVLA [28], SpatialVLA [54], π0 [4], CoT-VLA [85], and OpenVLAOFT [29]. | comparison identity and matched condition | p. 6 (5.1. Experimental Setup) |
| 1, ConsisVLA-4D outperforms all methods across the four LIBERO suites. | comparison identity and matched condition | p. 7 (5.2. Overall Performance & Efficiency) |
| Furthermore, compared to other general sparsification methods, such as FastV [11] and Table 7. | comparison identity and matched condition | p. 8 (5.3. Ablation Studies) |
| Based on this correlation, ConsisVLA-4D achieves state-of-the-art performance with only 1/8 of the visual tokens (see Tab. | comparison identity and matched condition | p. 8 (5.4. Qualitative Analysis) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Ablation components include ES-Selection, Single-Fusion from CVAligner, and Group-Fusion, IG-Aggregation from CO-Fuser. | component/input/data sensitivity | p. 7 (5.1. Experimental Setup) |
| Ablation Study on CV-Aligner and CO-Fuser. | component/input/data sensitivity | p. 7 (5.1. Experimental Setup) |
| Ablation Study on sparsification ratio (Spf.Ratio). "†" denotes reproduced results of FastV and SliME. | component/input/data sensitivity | p. 8 (5.3. Ablation Studies) |
| Table 6. Ablation Study on CS-Thinker. Dyn. O. and Glob. D. represent the training-only dynamic objects and global depth representations in 4D-Reasoning, respectively. Dyn. ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions are summarized as follows: • We propose ConsisVLA-4D, an efficient and innovative framework that advances spatiotemporal consistency in 3D-Perception and 4D-Reasoning. • ... | Particularly, it achieves exceptional success rates of 98.8% and 99.8% in the Spatial and Object suites, which assess spatial perception and object recognition, respectively. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (5.2. Overall Performance & Efficiency), p. 7 (5.2. Overall Performance & Efficiency), p. 8 (5.3. Ablation Studies), p. 8 (5.4. Qualitative Analysis), p. 3 (Figure/Table caption), p. 6 (5.1. Experimental Setup) |
| Primary metric/result | ConsisVLA-4D leads significantly in both phased and final success rates across 4 diverse long-horizon bimanual tasks, with strong performance stably maintained across deployment platforms ... | numeric claim only at cited anchor | p. 7 (5.2. Overall Performance & Efficiency) |

- Numeric sentences retained from the body:
- **p. 7 / 5.1. Experimental Setup - extractive body cue:** The tasks cover diverse scenarios, with each task conducted in 100 trials.
- **p. 7 / 5.1. Experimental Setup - extractive body cue:** Decimal values indicate averages over 15 trials, and the average success rate reflects complete task completion.
- **p. 7 / 5.2. Overall Performance & Efficiency - extractive body cue:** The significant throughput improvement by 33.4 Hz enables real-time, smooth operation of large VLA models on real hardware.
- **p. 7 / 5.3. Ablation Studies - extractive body cue:** Two tasks (Microwave Operation, T-shirt Folding) are selected, with 15 trials per task extended to 30 to ensure stable ablation results.
- **p. 6 / 4.4. Cross-Scene Spatiotemporal Consistency - extractive body cue:** The results are averaged over 20 or 100 trials.
- **p. 6 / 4.4. Cross-Scene Spatiotemporal Consistency - extractive body cue:** Method Latency ↓T-put ↑FLOPs ↓Cost ↓ Simulation: Unimanual tasks RT-2-X [PMLR'23] [6] 0.200 s

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | 5, for both simulation and real-world results: 1) Removing ES-Sel. and S-Fus. from CV-Aligner prevents the filtering of redundant visual inputs and fails to ... | p. 7 (5.3. Ablation Studies) |
| body limitation/failure cue | Through the integration of CVAligner, CO-Fuser, and CS-Thinker, it achieves cross-view, cross-object, and cross-scene consistency, enabling robust and efficient understanding of dynamic environments. | p. 8 (6. Conclusion) |
| body limitation/failure cue | Notably, its realworld results are nearly consistent with those on RoboTwin 2.0 (ALOHA manipulator), demonstrating robust sim-toreal transfer capability. | p. 7 (5.2. Overall Performance & Efficiency) |
| body limitation/failure cue | Moreover, all modules are adaptively designed, and swapping them with counterparts in SigLIP and DINOv2 degrades performance. | p. 8 (5.3. Ablation Studies) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The significant throughput improvement by 33.4 Hz enables real-time, smooth operation of large VLA models on real hardware. | p. 7 (5.2. Overall Performance & Efficiency) |
| Compared to simulation, the real-world setup adds a new viewpoint input, increases the action chunk size from 8 to 25, and reduces the training ... | p. 7 (5.2. Overall Performance & Efficiency) |
| Latency and Throughput (T-put) represent the inference delay and the number of predicted actions per second, while Cost indicates the time required for every ... | p. 6 (4.4. Cross-Scene Spatiotemporal Consistency) |
| This CVPR paper is the Open Access version, provided by the Computer Vision Foundation. | p. 1 (1. Introduction) |
| To address this, tri-view features are integrated for depth completion at each encoder layer. | p. 3 (4.1. Proposed Framework) |
| 3 left, multi-view observations I = {M, L, R} (Main, Left, Right) are encoded by SigLIP into semantic representations zsem M , zsem R ... | p. 3 (4.1. Proposed Framework) |
| (5) On the other hand, we use the aggregated geometric relation zagg-3D L′ to infer the depth representations of future multiview perspectives as actions ... | p. 4 (4.1. Proposed Framework) |
| We achieve concise spatial geometric relation aggregation through in-depth feature fusion within the encoder of DINOv2 and VGGT, performed block by block. | p. 5 (4.3. Cross-Object Spatial Geometric Consistency) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 5.3. Ablation Studies - extractive body cue:** 5, for both simulation and real-world results: 1) Removing ES-Sel. and S-Fus. from CV-Aligner prevents the filtering of redundant visual inputs and fails to align ...
- **p. 8 / 6. Conclusion - extractive body cue:** Through the integration of CVAligner, CO-Fuser, and CS-Thinker, it achieves cross-view, cross-object, and cross-scene consistency, enabling robust and efficient understanding of dynamic environments.
- **p. 7 / 5.2. Overall Performance & Efficiency - extractive body cue:** Notably, its realworld results are nearly consistent with those on RoboTwin 2.0 (ALOHA manipulator), demonstrating robust sim-toreal transfer capability.
- **p. 8 / 5.3. Ablation Studies - extractive body cue:** Moreover, all modules are adaptively designed, and swapping them with counterparts in SigLIP and DINOv2 degrades performance.

- **Evidence anchors reviewed:** datasets p. 6 (5.1. Experimental Setup), p. 7 (5.1. Experimental Setup), p. 7 (5.3. Ablation Studies), p. 6 (5.1. Experimental Setup), p. 8 (5.4. Qualitative Analysis), p. 8 (5.3. Ablation Studies), metrics p. 7 (5.1. Experimental Setup), p. 7 (5.2. Overall Performance & Efficiency), p. 8 (5.3. Ablation Studies), p. 8 (5.3. Ablation Studies), p. 6 (5.1. Experimental Setup), p. 6 (5.1. Experimental Setup), baselines p. 7 (5.2. Overall Performance & Efficiency), p. 6 (5.1. Experimental Setup), p. 6 (5.1. Experimental Setup), p. 7 (5.2. Overall Performance & Efficiency), p. 8 (5.3. Ablation Studies), p. 8 (5.4. Qualitative Analysis), results p. 7 (5.2. Overall Performance & Efficiency), p. 7 (5.2. Overall Performance & Efficiency), p. 8 (5.3. Ablation Studies), p. 8 (5.4. Qualitative Analysis), p. 3 (Figure/Table caption), p. 6 (5.1. Experimental Setup).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
