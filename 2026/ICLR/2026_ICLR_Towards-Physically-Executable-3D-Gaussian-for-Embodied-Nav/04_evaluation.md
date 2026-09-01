# Evaluation - Towards Physically Executable 3D Gaussian for Embodied Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=HB6KvsqcAn; PDF retrieval source: https://openreview.net/pdf/5cdfb5b83429401e057b422d807ffd76daa429d7.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS)): Even the recent SOTA model NaVILA achieves only a 0.39 success rate on high-level instructions, significantly lower than its 0.56 success rate on low-level instructions.

## Evaluation Body Digest

- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** Data in # Train SAGE-Bench VLN #Scenes #Samples SR ↑ OSR ↑ SPL ↑ CSR ↑ ICP ↓ PS ↑ 800 240k 0.42 0.47 0.42 ...
- **p. 10 / 4 EXPERIMENTS - extractive PDF cue:** Specifically, with the same number of augmented scenes (800), increasing the sampling density progressively improves the VLN model's performance on the val-unseen split.
- **p. 10 / 4 EXPERIMENTS - extractive PDF cue:** These findings indicate that the number of scenes (Scenes) has a greater impact than the number of samples (Samples), suggesting that diversity of environments is ...
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** 5 illustrate the influence of varying the number of scenes and the number of samples.
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** We selected 500k "trajectory-instruction" pairs from SAGE-Bench, with no overlap with the test set.
- **p. 15 / A IMPLEMENTATION DETAILS - extractive PDF cue:** To diversify the dataset, start-end pairs are sampled across different rooms, functional areas, and object instances, and a minimum safety distance is enforced to avoid ...
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** Notably, several baseline models with weak VLN performance (SR < 0.20) fail to understand navigation instructions or environmental information in our challenging tasks, behaving like ...
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** Insight 2: 3DGS scene data exhibits strong generalizability.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 4 EXPERIMENTS (p. 7); A IMPLEMENTATION DETAILS (p. 15).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Even the recent SOTA model NaVILA achieves only a 0.39 success rate on high-level instructions, significantly lower than its 0.56 success rate on low-level ... | p. 9 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | The results show that 3DGS scene data achieves a perframe rendering time of 6.2 ms and an average memory usage of 220 MB, outperforming ... | p. 8 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | 4, models trained entirely on SAGE-Bench data (without any VLN-CE data) achieved clear performance improvements over their respective baselines. | p. 9 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Specifically, with the same number of augmented scenes (800), increasing the sampling density progressively improves the VLN model's performance on the val-unseen split. | p. 10 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | In addition to the three novel metrics we proposed in Section 3.3 for evaluating the natural continuity of model navigation - CSR, ICP, and ... | p. 7 (4 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** Data in # Train SAGE-Bench VLN #Scenes #Samples SR ↑ OSR ↑ SPL ↑ CSR ↑ ICP ↓ PS ↑ 800 240k 0.42 0.47 0.42 ...
- **p. 10 / 4 EXPERIMENTS - extractive PDF cue:** Specifically, with the same number of augmented scenes (800), increasing the sampling density progressively improves the VLN model's performance on the val-unseen split.
- **p. 10 / 4 EXPERIMENTS - extractive PDF cue:** These findings indicate that the number of scenes (Scenes) has a greater impact than the number of samples (Samples), suggesting that diversity of environments is ...
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** 5 illustrate the influence of varying the number of scenes and the number of samples.
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** We selected 500k "trajectory-instruction" pairs from SAGE-Bench, with no overlap with the test set.
- **p. 15 / A IMPLEMENTATION DETAILS - extractive PDF cue:** To diversify the dataset, start-end pairs are sampled across different rooms, functional areas, and object instances, and a minimum safety distance is enforced to avoid ...
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** Notably, several baseline models with weak VLN performance (SR < 0.20) fail to understand navigation instructions or environmental information in our challenging tasks, behaving like ...
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** Insight 2: 3DGS scene data exhibits strong generalizability.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1: Traditional 3DGS vs. Our work. Compared with traditional 3DGS, our InteriorGS pro- vides object-level 3DGS annotations across diverse indoor and outdoor scenes, including ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Table 1: Comparisons with benchmarks for continuous navigation tasks. Here, "Instruction with Causality": tasks have causal dependencies rather than being mere "A-to-B" navigation; "Scene Geometry": ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2: Overview of SAGE-3D, which consists of two key components: (1) Object-Level Semantic Grounding, 3DGS data is annotated by expect at the object level, ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3: Overview of SAGE-Bench. SAGE-Bench includes a hierarchical instruction generation scheme, two major task types, two episode complexity categories, and three newly designed natural ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 3. It includes a hierarchical instruction generation scheme (Section 3.1), a three-axis evaluation framework (Section 3.2), and three navigation natural continuity metrics (Section 3.3). ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2: Comparison of different models on VLN and Visual Exploration tasks on SAGE-Bench. Bold values represent the best performance across all methods. Gray values ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3: Rendering speed and training convergence comparison. Environment Type Avg. Render Time / Frame (ms) ↓ Avg. Memory (MB) ↓ Iters to SR=40% (k) ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4: Visualization case study of navigation natural continuity. The red trajectory is the ground truth, and the blue Trajectory is the trajectory of NaVILA. ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Data in # Train SAGE-Bench VLN #Scenes #Samples SR ↑ OSR ↑ SPL ↑ CSR ↑ ICP ↓ PS ↑ 800 240k 0.42 0.47 ... | embodiment, simulator version and control stack | p. 9 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS) |
| Task/environment | Specifically, with the same number of augmented scenes (800), increasing the sampling density progressively improves the VLN model's performance on the val-unseen split. | reset, timeout, object/scene variation | p. 10 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| In addition to the three novel metrics we proposed in Section 3.3 for evaluating the natural continuity of model navigation - CSR, ICP, and ... | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |
| Even the recent SOTA model NaVILA achieves only a 0.39 success rate on high-level instructions, significantly lower than its 0.56 success rate on low-level ... | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| Methods Instruction Level SAGE-Bench VLN SR ↑ OSR ↑ SPL ↑ CSR ↑ ICP ↓ PS ↑ GPT-4.1 Low-level 0.22 0.37 0.19 0.27 0.60 ... | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| The results show that VLN models perform worse on the "Relative Relationship" and "Attribute-based" instruction types, with SR scores for both NaVILA and NaVid ... | definition/direction/unit from same section | p. 10 (4 EXPERIMENTS) |
| Figure 2: Overview of SAGE-3D, which consists of two key components: (1) Object-Level Semantic Grounding, 3DGS data is annotated by expect at the object ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| An episode is terminated immediately if a collision occurs, and the maximum episode time is set to 120 seconds. | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |
| Bold values represent the best performance across all methods. | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| Gray values indicate that these metrics lack comparative significance due to the low navigation performance of the models. | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 4, models trained entirely on SAGE-Bench data (without any VLN-CE data) achieved clear performance improvements over their respective baselines. | comparison identity and matched condition | p. 9 (4 EXPERIMENTS) |
| Notably, several baseline models with weak VLN performance (SR < 0.20) fail to understand navigation instructions or environmental information in our challenging tasks, behaving ... | comparison identity and matched condition | p. 7 (4 EXPERIMENTS) |
| In addition to the three novel metrics we proposed in Section 3.3 for evaluating the natural continuity of model navigation - CSR, ICP, and ... | comparison identity and matched condition | p. 7 (4 EXPERIMENTS) |
| The results show that 3DGS scene data achieves a perframe rendering time of 6.2 ms and an average memory usage of 220 MB, outperforming ... | comparison identity and matched condition | p. 8 (4 EXPERIMENTS) |
| 5 compares the performance of different models on high-level and low-level instructions in the VLN task.Compared with low-level instruction data, which are composed of ... | comparison identity and matched condition | p. 9 (4 EXPERIMENTS) |
| Figure 1: Traditional 3DGS vs. Our work. Compared with traditional 3DGS, our InteriorGS pro- vides object-level 3DGS annotations across diverse indoor and outdoor scenes, ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 4, models trained entirely on SAGE-Bench data (without any VLN-CE data) achieved clear performance improvements over their respective baselines. | component/input/data sensitivity | p. 9 (4 EXPERIMENTS) |
| We trained two models on this subset: one based on NaVILA's pre-trained model navila-siglip-llama3-8b-v1.5-pretrain (denoted as NaVILA-base), producing NaVILA-SAGE; and the other based on ... | component/input/data sensitivity | p. 7 (4 EXPERIMENTS) |
| Figure 2: Overview of SAGE-3D, which consists of two key components: (1) Object-Level Semantic Grounding, 3DGS data is annotated by expect at the object ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We introduce a 3DGS-Mesh Hybrid Representation: starting from our mesh scene data, we extract collision bodies for each object as the physics layer, while ... | Even the recent SOTA model NaVILA achieves only a 0.39 success rate on high-level instructions, significantly lower than its 0.56 success rate on low-level ... | PDF body cue; verify exact table/figure and matched conditions | p. 9 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Primary metric/result | The results show that 3DGS scene data achieves a perframe rendering time of 6.2 ms and an average memory usage of 220 MB, outperforming ... | numeric claim only at cited anchor | p. 8 (4 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** The results show that 3DGS scene data achieves a perframe rendering time of 6.2 ms and an average memory usage of 220 MB, outperforming the ...
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** However, in training, to reach the same 40% SR, the 3DGSbased model required about 160 iterations and 6.2 hours, while the scanned mesh-based model needed ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 3: Overview of SAGE-Bench. SAGE-Bench includes a hierarchical instruction generation scheme, two major task types, two episode complexity categories, and three newly designed ... | p. 5 (Figure/Table caption) |
| body limitation/failure cue | 4 corroborate this finding: the NaVILA model (blue trajectory) exhibits unsmooth movement and persistent collisions that conventional metrics fail to reveal. | p. 9 (4 EXPERIMENTS) |
| body limitation/failure cue | Figure 1: Traditional 3DGS vs. Our work. Compared with traditional 3DGS, our InteriorGS pro- vides object-level 3DGS annotations across diverse indoor and outdoor scenes, ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | Figure 2: Overview of SAGE-3D, which consists of two key components: (1) Object-Level Semantic Grounding, 3DGS data is annotated by expect at the object ... | p. 3 (Figure/Table caption) |
| body limitation/failure cue | An episode is terminated immediately if a collision occurs, and the maximum episode time is set to 120 seconds. | p. 7 (4 EXPERIMENTS) |
| body limitation/failure cue | In addition to the three novel metrics we proposed in Section 3.3 for evaluating the natural continuity of model navigation - CSR, ICP, and ... | p. 7 (4 EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Training was carried out on 8 NVIDIA Tesla H20 GPUs with a batch size of 256 and a learning rate of 2 × 10-5. | p. 15 (A IMPLEMENTATION DETAILS) |
| We randomly selected 10k training samples and 1k validation samples from both traditional scanned mesh data and our 3DGS data, and conducted experiments with ... | p. 8 (4 EXPERIMENTS) |
| We run A*-based shortest-path search to generate trajectories with a cost function that integrates free-space distance, narrow-passage penalties, and area preferences to ensure both ... | p. 15 (A IMPLEMENTATION DETAILS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3: Overview of SAGE-Bench. SAGE-Bench includes a hierarchical instruction generation scheme, two major task types, two episode complexity categories, and three newly designed natural ...
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** 4 corroborate this finding: the NaVILA model (blue trajectory) exhibits unsmooth movement and persistent collisions that conventional metrics fail to reveal.
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1: Traditional 3DGS vs. Our work. Compared with traditional 3DGS, our InteriorGS pro- vides object-level 3DGS annotations across diverse indoor and outdoor scenes, including ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2: Overview of SAGE-3D, which consists of two key components: (1) Object-Level Semantic Grounding, 3DGS data is annotated by expect at the object level, ...
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** An episode is terminated immediately if a collision occurs, and the maximum episode time is set to 120 seconds.
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** In addition to the three novel metrics we proposed in Section 3.3 for evaluating the natural continuity of model navigation - CSR, ICP, and PS ...

- **PDF anchors reviewed:** datasets p. 9 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 15 (A IMPLEMENTATION DETAILS), metrics p. 7 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 3 (Figure/Table caption), p. 7 (4 EXPERIMENTS), baselines p. 9 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 1 (Figure/Table caption), results p. 9 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
