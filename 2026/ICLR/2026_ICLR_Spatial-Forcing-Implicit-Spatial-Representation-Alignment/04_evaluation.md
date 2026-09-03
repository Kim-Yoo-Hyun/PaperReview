# Evaluation - Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=euMVC1DO4k; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/248008. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (2.1 PRELIMINARIES), p. 6 (Figure/Table caption), p. 8 (2.1 PRELIMINARIES), p. 8 (2.1 PRELIMINARIES), p. 9 (2.1 PRELIMINARIES), p. 2 (Figure/Table caption)): 6 shows that our SF achieves higher success rates across all tasks, showing considerable improvements in data efficiency.

## Evaluation Body Digest

- **p. 8 / 2.1 PRELIMINARIES - extractive body cue:** Given the scarcity of real-world data, this capability is particularly valuable for robotic applications.
- **p. 8 / 2.1 PRELIMINARIES - extractive body cue:** 4 REAL-WORLD EXPERIMENTS Action Sequenace Task Variation SR (%) Stack Glass Cups (light variation) Grasp Right-side Vegetable (target object variation) Place Green Block (height variation) ...
- **p. 9 / 2.1 PRELIMINARIES - extractive body cue:** This ability is critical for real-world deployment.
- **p. 9 / 2.1 PRELIMINARIES - extractive body cue:** In the grasp right-side vegetable task, different target objects require distinct gripper poses and clamping widths.
- **p. 7 / 2.1 PRELIMINARIES - extractive body cue:** We report the task success rates vs. training iterations before and after representation (b) Data efficiency (c) t-SNE visualization (a) Training efficiency Training iterations 3.8x ...
- **p. 8 / 2.1 PRELIMINARIES - extractive body cue:** SF reaches 75.8% success rates with only 5% data.
- **p. 8 / 2.1 PRELIMINARIES - extractive body cue:** For each task, we train a unified model to face all variations and report the success rate.
- **p. 9 / 2.1 PRELIMINARIES - extractive body cue:** We report the success rate (SR) of each task as the evaluation metric.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 2.1 PRELIMINARIES | EMPIRICAL / REAL-ROBOT OR HARDWARE | 6 shows that our SF achieves higher success rates across all tasks, showing considerable improvements in data efficiency. | p. 9 (2.1 PRELIMINARIES) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 4: Comparisons with state-of-the-art methods on RoboTwin 2.0 benchmark. LIBERO. Each task is evaluated for 500 trials under random seeds. Tab. 1 shows ... | p. 6 (Figure/Table caption) |
| 2.1 PRELIMINARIES | EMPIRICAL / REAL-ROBOT OR HARDWARE | It also achieves 25.8% higher success rates in terms of the same data amounts and reaches 5.9× more efficient in terms of the same ... | p. 8 (2.1 PRELIMINARIES) |
| 2.1 PRELIMINARIES | EMPIRICAL / REAL-ROBOT OR HARDWARE | The results illustrate that training with alignment significantly speeds up the convergence, achieving the same success rates 3.8× more quickly than the base model. | p. 8 (2.1 PRELIMINARIES) |
| 2.1 PRELIMINARIES | EMPIRICAL / REAL-ROBOT OR HARDWARE | Benefit from spatial feature learning, SF achieves an 85% success rate. | p. 9 (2.1 PRELIMINARIES) |

## Dataset / Benchmark Role

- **p. 8 / 2.1 PRELIMINARIES - extractive body cue:** Given the scarcity of real-world data, this capability is particularly valuable for robotic applications.
- **p. 8 / 2.1 PRELIMINARIES - extractive body cue:** 4 REAL-WORLD EXPERIMENTS Action Sequenace Task Variation SR (%) Stack Glass Cups (light variation) Grasp Right-side Vegetable (target object variation) Place Green Block (height variation) ...
- **p. 9 / 2.1 PRELIMINARIES - extractive body cue:** This ability is critical for real-world deployment.
- **p. 9 / 2.1 PRELIMINARIES - extractive body cue:** In the grasp right-side vegetable task, different target objects require distinct gripper poses and clamping widths.
- **p. 7 / 2.1 PRELIMINARIES - extractive body cue:** We report the task success rates vs. training iterations before and after representation (b) Data efficiency (c) t-SNE visualization (a) Training efficiency Training iterations 3.8x ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Our proposed method, Spatial Forcing (SF), implicitly forces VLA models to acquire spatial-aware knowledge. (a) SF aligns intermediate visual embeddings of VLAs with ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Comparison among different paradigms for 3D VLAs. Primary Wrist LIBERO Simulation Real-world Robot Images w/o Alignment w/ Alignment GT
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: Depth probing of the visual embeddings of VLAs. Embeddings learned solely from 2D images without alignment do not produce meaningful spatial structures. The ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1: Comparisons with state-of-the-art methods on LIBERO benchmark. Please note that methods in gray font incorporate extra depth or point cloud information from other ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: Comparisons with state-of-the-art methods on RoboTwin 2.0 benchmark. LIBERO. Each task is evaluated for 500 trials under random seeds. Tab. 1 shows that ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Component Analysis on LIBERO benchmark. PE denotes positional embedding. Bold means the best performance. Experiments are conducted on 1×H100. Target Representation Aligned Layerth ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: (a) We report the success rates vs. training iterations before and after representation alignment. (b) We report the success rate vs. training data ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6: Real-world Experiments. (a) A set of single-arm tasks across various visual and spatial conditions. For each task, we train a unified model to ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Given the scarcity of real-world data, this capability is particularly valuable for robotic applications. | embodiment, simulator version and control stack | p. 8 (2.1 PRELIMINARIES), p. 8 (2.1 PRELIMINARIES) |
| Task/environment | 4 REAL-WORLD EXPERIMENTS Action Sequenace Task Variation SR (%) Stack Glass Cups (light variation) Grasp Right-side Vegetable (target object variation) Place Green Block (height ... | reset, timeout, object/scene variation | p. 8 (2.1 PRELIMINARIES), p. 9 (2.1 PRELIMINARIES) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 4 (2.1 PRELIMINARIES), p. 1 (1 INTRODUCTION) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| (b) We report the success rate vs. training data before and after representation alignment. | definition/direction/unit from same section | p. 7 (2.1 PRELIMINARIES) |
| SF reaches 75.8% success rates with only 5% data. | definition/direction/unit from same section | p. 8 (2.1 PRELIMINARIES) |
| For each task, we train a unified model to face all variations and report the success rate. | definition/direction/unit from same section | p. 8 (2.1 PRELIMINARIES) |
| We report the success rate (SR) of each task as the evaluation metric. | definition/direction/unit from same section | p. 9 (2.1 PRELIMINARIES) |
| Benefit from spatial feature learning, SF achieves an 85% success rate. | definition/direction/unit from same section | p. 9 (2.1 PRELIMINARIES) |
| Figure 1: Our proposed method, Spatial Forcing (SF), implicitly forces VLA models to acquire spatial-aware knowledge. (a) SF aligns intermediate visual embeddings of VLAs ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Figure 7: The MOE gating score distribution histograms on the LIBERO benchmark of adaptive layer selection strategy. | definition/direction/unit from same section | p. 20 (Figure/Table caption) |
| Table 1: Comparisons with state-of-the-art methods on LIBERO benchmark. Please note that methods in gray font incorporate extra depth or point cloud information from ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 4: Comparisons with state-of-the-art methods on RoboTwin 2.0 benchmark. LIBERO. Each task is evaluated for 500 trials under random seeds. Tab. 1 shows ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Table 1: Comparisons with state-of-the-art methods on LIBERO benchmark. Please note that methods in gray font incorporate extra depth or point cloud information from ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |
| Figure 2: Comparison among different paradigms for 3D VLAs. Primary Wrist LIBERO Simulation Real-world Robot Images w/o Alignment w/ Alignment GT | comparison identity and matched condition | p. 4 (Figure/Table caption) |
| Figure 3: Depth probing of the visual embeddings of VLAs. Embeddings learned solely from 2D images without alignment do not produce meaningful spatial structures. ... | comparison identity and matched condition | p. 4 (Figure/Table caption) |
| Table 4: The Ablation of Supervising Different Transformer Layers of VLA. Aligned Layerth Spatial Object Goal Long Average 1 | comparison identity and matched condition | p. 19 (Figure/Table caption) |
| Figure 9: Additional ablation experiments for more complex spatial tasks. Then, the visual tokens of VLA are fed into the trainable VLA downstream heads ... | comparison identity and matched condition | p. 21 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 3: Depth probing of the visual embeddings of VLAs. Embeddings learned solely from 2D images without alignment do not produce meaningful spatial structures. ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |
| We further investigate the effect of supervising different transformer layers of VLA, shown in Tab. | component/input/data sensitivity | p. 7 (2.1 PRELIMINARIES) |
| Figure 1: Our proposed method, Spatial Forcing (SF), implicitly forces VLA models to acquire spatial-aware knowledge. (a) SF aligns intermediate visual embeddings of VLAs ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |
| Table 1: Comparisons with state-of-the-art methods on LIBERO benchmark. Please note that methods in gray font incorporate extra depth or point cloud information from ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |
| Figure 4: Comparisons with state-of-the-art methods on RoboTwin 2.0 benchmark. LIBERO. Each task is evaluated for 500 trials under random seeds. Tab. 1 shows ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| Table 4: The Ablation of Supervising Different Transformer Layers of VLA. Aligned Layerth Spatial Object Goal Long Average 1 | component/input/data sensitivity | p. 19 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To bridge the gap, we propose Spatial Forcing (SF), a simple yet effective alignment strategy that implicitly forces VLA models to acquire spatial-aware knowledge. | 6 shows that our SF achieves higher success rates across all tasks, showing considerable improvements in data efficiency. | PDF body cue; verify exact table/figure and matched conditions | p. 9 (2.1 PRELIMINARIES), p. 6 (Figure/Table caption), p. 8 (2.1 PRELIMINARIES), p. 8 (2.1 PRELIMINARIES), p. 9 (2.1 PRELIMINARIES), p. 2 (Figure/Table caption) |
| Primary metric/result | Figure 4: Comparisons with state-of-the-art methods on RoboTwin 2.0 benchmark. LIBERO. Each task is evaluated for 500 trials under random seeds. Tab. 1 shows ... | numeric claim only at cited anchor | p. 6 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 7 / 2.1 PRELIMINARIES - extractive body cue:** Experiments are conducted on 1×H100.
- **p. 7 / 2.1 PRELIMINARIES - extractive body cue:** We report the task success rates vs. training iterations before and after representation (b) Data efficiency (c) t-SNE visualization (a) Training efficiency Training iterations 3.8x ...
- **p. 9 / 2.1 PRELIMINARIES - extractive body cue:** For evaluation, we test 10 trials per variation (40 trials in total) for each single-arm task, and 20 trials for the dual-arm task.
- **p. 4 / 2.1 PRELIMINARIES - extractive body cue:** Then we employ a cosine similarity score to maximize the alignment between the visual tokens of VLA and the spatial representation signals: Lalign = -1 ...
- **p. 5 / 2.1 PRELIMINARIES - extractive body cue:** Each task suite contains 500 expert demonstrations across 10 tasks to investigate policy generalization to different spatial layouts, objects, goals, and long-horizon tasks.
- **p. 6 / 2.1 PRELIMINARIES - extractive body cue:** Each task is evaluated for 500 trials under random seeds.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We take OpenVLA-OFT (Kim et al., 2025) as the base model and conduct experiments on the LIBERO benchmark with a single H100 because of ... | p. 6 (2.1 PRELIMINARIES) |
| body limitation/failure cue | However, the reconstruction supervision may not be suitable for VLAs to learn effective representations, as it fails to filter out redundant details (LeCun, 2022; ... | p. 9 (5 RELATED WORK) |
| body limitation/failure cue | SigLIP excels at semantic understanding through robust imagetext alignment, whereas DINOv2 offers stronger visual grounding owing to its fine-grained spatial representations. | p. 6 (2.1 PRELIMINARIES) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Each task is evaluated for 500 trials under random seeds. | p. 6 (2.1 PRELIMINARIES) |
| In our work, we argue that the latent representation extracted from the VGGT transformer backbone inherently encodes rich spatial information and is sufficient to ... | p. 3 (2.1 PRELIMINARIES) |
| The vision modality consists of multi-view images captured by robots, which are transformed into N visual tokens {xV t }N t=1 through pretrained visual ... | p. 3 (2.1 PRELIMINARIES) |
| 3, the probing results show that visual embeddings learned solely from 2D images do not produce meaningful spatial structures, suggesting a limited capacity of ... | p. 4 (2.1 PRELIMINARIES) |
| Base Models and Implementation Details. | p. 5 (2.1 PRELIMINARIES) |
| For evaluation, we test 10 trials per variation (40 trials in total) for each single-arm task, and 20 trials for the dual-arm task. | p. 9 (2.1 PRELIMINARIES) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 2.1 PRELIMINARIES - extractive body cue:** We take OpenVLA-OFT (Kim et al., 2025) as the base model and conduct experiments on the LIBERO benchmark with a single H100 because of limitations ...
- **p. 9 / 5 RELATED WORK - extractive body cue:** However, the reconstruction supervision may not be suitable for VLAs to learn effective representations, as it fails to filter out redundant details (LeCun, 2022; Assran ...
- **p. 6 / 2.1 PRELIMINARIES - extractive body cue:** SigLIP excels at semantic understanding through robust imagetext alignment, whereas DINOv2 offers stronger visual grounding owing to its fine-grained spatial representations.

- **Evidence anchors reviewed:** datasets p. 8 (2.1 PRELIMINARIES), p. 8 (2.1 PRELIMINARIES), p. 9 (2.1 PRELIMINARIES), p. 9 (2.1 PRELIMINARIES), p. 7 (2.1 PRELIMINARIES), metrics p. 7 (2.1 PRELIMINARIES), p. 8 (2.1 PRELIMINARIES), p. 8 (2.1 PRELIMINARIES), p. 9 (2.1 PRELIMINARIES), p. 9 (2.1 PRELIMINARIES), p. 2 (Figure/Table caption), baselines p. 6 (Figure/Table caption), p. 5 (Figure/Table caption), p. 4 (Figure/Table caption), p. 4 (Figure/Table caption), p. 19 (Figure/Table caption), p. 21 (Figure/Table caption), results p. 9 (2.1 PRELIMINARIES), p. 6 (Figure/Table caption), p. 8 (2.1 PRELIMINARIES), p. 8 (2.1 PRELIMINARIES), p. 9 (2.1 PRELIMINARIES), p. 2 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
