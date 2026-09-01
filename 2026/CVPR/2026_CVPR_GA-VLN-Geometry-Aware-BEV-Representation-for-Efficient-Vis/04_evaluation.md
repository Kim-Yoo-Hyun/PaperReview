# Evaluation - GA-VLN: Geometry-Aware BEV Representation for Efficient Vision-Language Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Yang_GA-VLN_Geometry-Aware_BEV_Representation_for_Efficient_Vision-Language_Navigation_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Yang_GA-VLN_Geometry-Aware_BEV_Representation_for_Efficient_Vision-Language_Navigation_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (4.1. Experimental Setup), p. 5 (4.2. Comparison with State-of-the-Art Methods), p. 6 (4.3. Ablation Study and Efficiency Analysis), p. 6 (4.3. Ablation Study and Efficiency Analysis), p. 7 (4.4. Design Analysis of GA-BEV), p. 7 (4.4. Design Analysis of GA-BEV)): Navigation performance is measured using four standard metrics: Navigation Error (NE), Success Rate (SR), Oracle Success Rate (OSR), and Success weighted by Path Length (SPL).

## Evaluation Body Digest

- **p. 5 / 4.1. Experimental Setup - extractive PDF cue:** We evaluate our approach on standard continuous-environment VLN-CE [15] benchmarks: R2R-CE [3], RxR-CE [16], and NavRAG-CE [38] val unseen split in the Habitat simulator [25].
- **p. 5 / 4.1. Experimental Setup - extractive PDF cue:** Our model is trained on a combination of navigation datasets collected in MP3D [5] and HM3D [23] environments, including: R2R-CE [3] (10,819 trajectories), RxR-CE [16] ...
- **p. 6 / 4.2. Comparison with State-of-the-Art Methods - extractive PDF cue:** Comparison with state-of-the-art VLN methods on R2R-CE, RxR-CE, and NavRAG-CE val unseen benchmarks. "System" groups methods into modular planners, 3D end-to-end agents, and Image-based MLLM ...
- **p. 6 / 4.3. Ablation Study and Efficiency Analysis - extractive PDF cue:** All the ablation and analysis experiments in this section and the following sections are conducted on the R2R-CE val unseen split.
- **p. 8 / 4.5. Real-World Robot Experiments - extractive PDF cue:** Detailed hardware setups and additional examples are provided in the Supplementary Material.
- **p. 8 / 4.5. Real-World Robot Experiments - extractive PDF cue:** To validate the zero-shot generalizability of GA-VLN, we deploy it on a physical Hello Robot Stretch 3 in a realworld room.
- **p. 7 / 4.4. Design Analysis of GA-BEV - extractive PDF cue:** The token numbers represent the average number of visual tokens required per navigation step, computed over 121 sampled navigation trajectories across 61 training scenes.
- **p. 7 / 4.4. Design Analysis of GA-BEV - extractive PDF cue:** Crucially, the consistent relative improvements observed both with the SRDF dataset (Table 2) and without it (Table 3) confirm that GA-VLN provides a robust spatial ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Experimental Setup (p. 5); 4.5. Real-World Robot Experiments (p. 8).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.1. Experimental Setup | EMPIRICAL / REAL-ROBOT OR HARDWARE | Navigation performance is measured using four standard metrics: Navigation Error (NE), Success Rate (SR), Oracle Success Rate (OSR), and Success weighted by Path Length ... | p. 5 (4.1. Experimental Setup) |
| 4.2. Comparison with State-of-the-Art Methods | EMPIRICAL / REAL-ROBOT OR HARDWARE | Across most metrics on these benchmarks, our GA-VLN achieves the best overall performance, consistently surpassing previous Image-based MLLM frameworks [10, 39, 41, 42] and ... | p. 5 (4.2. Comparison with State-of-the-Art Methods) |
| 4.3. Ablation Study and Efficiency Analysis | EMPIRICAL / REAL-ROBOT OR HARDWARE | Ultimately, GA-VLN outperforms the image-based baseline in both navigation performance and inference speed. | p. 6 (4.3. Ablation Study and Efficiency Analysis) |
| 4.3. Ablation Study and Efficiency Analysis | EMPIRICAL / REAL-ROBOT OR HARDWARE | By introducing explicit spatial information, the BEV features enable the agent to better capture the surrounding environment, resulting in improved spatial understanding and higher ... | p. 6 (4.3. Ablation Study and Efficiency Analysis) |
| 4.4. Design Analysis of GA-BEV | EMPIRICAL / REAL-ROBOT OR HARDWARE | The results show that a moderate resolution (0.25 m × 0.25 m) achieves the best trade-off between accuracy and efficiency. | p. 7 (4.4. Design Analysis of GA-BEV) |

## Dataset / Benchmark Role

- **p. 5 / 4.1. Experimental Setup - extractive PDF cue:** We evaluate our approach on standard continuous-environment VLN-CE [15] benchmarks: R2R-CE [3], RxR-CE [16], and NavRAG-CE [38] val unseen split in the Habitat simulator [25].
- **p. 5 / 4.1. Experimental Setup - extractive PDF cue:** Our model is trained on a combination of navigation datasets collected in MP3D [5] and HM3D [23] environments, including: R2R-CE [3] (10,819 trajectories), RxR-CE [16] ...
- **p. 6 / 4.2. Comparison with State-of-the-Art Methods - extractive PDF cue:** Comparison with state-of-the-art VLN methods on R2R-CE, RxR-CE, and NavRAG-CE val unseen benchmarks. "System" groups methods into modular planners, 3D end-to-end agents, and Image-based MLLM ...
- **p. 6 / 4.3. Ablation Study and Efficiency Analysis - extractive PDF cue:** All the ablation and analysis experiments in this section and the following sections are conducted on the R2R-CE val unseen split.
- **p. 8 / 4.5. Real-World Robot Experiments - extractive PDF cue:** Detailed hardware setups and additional examples are provided in the Supplementary Material.
- **p. 8 / 4.5. Real-World Robot Experiments - extractive PDF cue:** To validate the zero-shot generalizability of GA-VLN, we deploy it on a physical Hello Robot Stretch 3 in a realworld room.
- **p. 7 / 4.4. Design Analysis of GA-BEV - extractive PDF cue:** The token numbers represent the average number of visual tokens required per navigation step, computed over 121 sampled navigation trajectories across 61 training scenes.
- **p. 7 / 4.4. Design Analysis of GA-BEV - extractive PDF cue:** Crucially, the consistent relative improvements observed both with the SRDF dataset (Table 2) and without it (Table 3) confirm that GA-VLN provides a robust spatial ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Illustration of different representations for VLN. (A) Dense image-based representations contain heavy token redun- dancy and lack explicit spatial structure. (B) Our Geometry-Aware ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Overview of the proposed Geometry-Aware Vision-Language Navigation (GA-VLN) framework. Given RGB-D current and historical front views, our method constructs a Geometry-Aware BEV (GA-BEV) ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Comparison with state-of-the-art VLN methods on R2R-CE, RxR-CE, and NavRAG-CE val unseen benchmarks. "System" groups methods into modular planners, 3D end-to-end agents, and ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Ablation study of Geometry-Aware BEV representation and efficiency comparison per inference step.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Analysis of token efficiency and spatial resolution trade-offs of GA-BEV. The experiments compare different visual representations (rows 1-3), BEV grid size (rows 4-5), ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 3. An example of the GA-VLN real-world result.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 4. Robustness to Sensor Noise on R2R-CE val unseen. Noise N(0, σ2) NE↓ OSR↑ SR↑ SPL↑ w/o Noise

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We evaluate our approach on standard continuous-environment VLN-CE [15] benchmarks: R2R-CE [3], RxR-CE [16], and NavRAG-CE [38] val unseen split in the Habitat simulator ... | embodiment, simulator version and control stack | p. 5 (4.1. Experimental Setup), p. 5 (4.1. Experimental Setup) |
| Task/environment | Our model is trained on a combination of navigation datasets collected in MP3D [5] and HM3D [23] environments, including: R2R-CE [3] (10,819 trajectories), RxR-CE ... | reset, timeout, object/scene variation | p. 5 (4.1. Experimental Setup), p. 6 (4.2. Comparison with State-of-the-Art Methods) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 5 (3.3. Geometry-Aware VLN Framework), p. 1 (1. Introduction) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 4 (3.1. Preliminary), p. 4 (3.1. Preliminary) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Navigation performance is measured using four standard metrics: Navigation Error (NE), Success Rate (SR), Oracle Success Rate (OSR), and Success weighted by Path Length ... | definition/direction/unit from same section | p. 5 (4.1. Experimental Setup) |
| By introducing explicit spatial information, the BEV features enable the agent to better capture the surrounding environment, resulting in improved spatial understanding and higher ... | definition/direction/unit from same section | p. 6 (4.3. Ablation Study and Efficiency Analysis) |
| The results show that a moderate resolution (0.25 m × 0.25 m) achieves the best trade-off between accuracy and efficiency. | definition/direction/unit from same section | p. 7 (4.4. Design Analysis of GA-BEV) |
| Table 4. Robustness to Sensor Noise on R2R-CE val unseen. Noise N(0, σ2) NE↓ OSR↑ SR↑ SPL↑ w/o Noise | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Notably, unlike most recent methods that rely on DAgger augmentation, our framework achieves competitive performance using only high-quality curated data, without any DAgger-enhanced trajectories ... | definition/direction/unit from same section | p. 6 (4.2. Comparison with State-of-the-Art Methods) |
| Noise N(0, σ2) NE↓ OSR↑ SR↑ SPL↑ w/o Noise - 4.80 67.59 60.96 55.19 Depth σ = 0.05m 4.82 65.63 59.11 54.25 Pose σ ... | definition/direction/unit from same section | p. 8 (4.4. Design Analysis of GA-BEV) |
| The model is optimized using a cosine annealing schedule with a minimum learning rate. | definition/direction/unit from same section | p. 5 (4.1. Experimental Setup) |
| While performance slightly improves when extending the temporal window from 32 to 48 action steps, it saturates or even decreases with longer histories. | definition/direction/unit from same section | p. 7 (4.4. Design Analysis of GA-BEV) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Ultimately, GA-VLN outperforms the image-based baseline in both navigation performance and inference speed. | comparison identity and matched condition | p. 6 (4.3. Ablation Study and Efficiency Analysis) |
| Comparison with state-of-the-art VLN methods on R2R-CE, RxR-CE, and NavRAG-CE val unseen benchmarks. "System" groups methods into modular planners, 3D end-to-end agents, and Image-based ... | comparison identity and matched condition | p. 6 (4.2. Comparison with State-of-the-Art Methods) |
| Navigation performance is measured using four standard metrics: Navigation Error (NE), Success Rate (SR), Oracle Success Rate (OSR), and Success weighted by Path Length ... | comparison identity and matched condition | p. 5 (4.1. Experimental Setup) |
| We compare our approach with a comprehensive set of state-of-the-art monocular VLN methods in continuous environments, including modular planners, 3D end-toend agents, and recent ... | comparison identity and matched condition | p. 5 (4.2. Comparison with State-of-the-Art Methods) |
| This indicates that our architectural design and data scaling strategies act as complementary, rather than conflicting, drivers for achieving state-of-the-art performance. | comparison identity and matched condition | p. 7 (4.4. Design Analysis of GA-BEV) |
| 3, despite operating without any auxiliary obstacle avoidance or mapping modules, the agent successfully executes complex natural-language instructions and constructs meaningful geometric surrounding BEV ... | comparison identity and matched condition | p. 8 (4.5. Real-World Robot Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To rigorously demonstrate that the performance gains of our model are driven by fundamental architectural innovations rather than solely by data scaling, Rows #1-3 ... | component/input/data sensitivity | p. 7 (4.4. Design Analysis of GA-BEV) |
| Effect of the Number of Historical Frames. | component/input/data sensitivity | p. 7 (4.4. Design Analysis of GA-BEV) |
| All the ablation and analysis experiments in this section and the following sections are conducted on the R2R-CE val unseen split. | component/input/data sensitivity | p. 6 (4.3. Ablation Study and Efficiency Analysis) |
| Notably, unlike most recent methods that rely on DAgger augmentation, our framework achieves competitive performance using only high-quality curated data, without any DAgger-enhanced trajectories ... | component/input/data sensitivity | p. 6 (4.2. Comparison with State-of-the-Art Methods) |
| 3, despite operating without any auxiliary obstacle avoidance or mapping modules, the agent successfully executes complex natural-language instructions and constructs meaningful geometric surrounding BEV ... | component/input/data sensitivity | p. 8 (4.5. Real-World Robot Experiments) |
| All reported results are obtained using models pretrained for 2 epochs. | component/input/data sensitivity | p. 5 (4.1. Experimental Setup) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our main contributions are summarized as follows: • We propose Geometry-Aware BEV (GA-BEV), a compact and 3D-grounded representation that combines explicit depth-based projected features ... | Navigation performance is measured using four standard metrics: Navigation Error (NE), Success Rate (SR), Oracle Success Rate (OSR), and Success weighted by Path Length ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (4.1. Experimental Setup), p. 5 (4.2. Comparison with State-of-the-Art Methods), p. 6 (4.3. Ablation Study and Efficiency Analysis), p. 6 (4.3. Ablation Study and Efficiency Analysis), p. 7 (4.4. Design Analysis of GA-BEV), p. 7 (4.4. Design Analysis of GA-BEV) |
| Primary metric/result | Across most metrics on these benchmarks, our GA-VLN achieves the best overall performance, consistently surpassing previous Image-based MLLM frameworks [10, 39, 41, 42] and ... | numeric claim only at cited anchor | p. 5 (4.2. Comparison with State-of-the-Art Methods) |

- Numeric sentences retained from the body:
- **p. 5 / 4.1. Experimental Setup - extractive PDF cue:** Our model is trained on a combination of navigation datasets collected in MP3D [5] and HM3D [23] environments, including: R2R-CE [3] (10,819 trajectories), RxR-CE [16] ...
- **p. 5 / 4.1. Experimental Setup - extractive PDF cue:** For BEV representation settings, grid cell size ∆is 0.25 meters, BEV range is [-10 meters, 10 meters].
- **p. 5 / 4.1. Experimental Setup - extractive PDF cue:** All reported results are obtained using models pretrained for 2 epochs.
- **p. 7 / 4.4. Design Analysis of GA-BEV - extractive PDF cue:** Incorporating 3D-geometric priors via VGGT (Row #3) further pushes the SR to 53.56% with a manageable 514 tokens.
- **p. 7 / 4.4. Design Analysis of GA-BEV - extractive PDF cue:** Incorporating 3D-geometric priors via VGGT (Row #3) further pushes the SR to 53.56% with a manageable 514 tokens.
- **p. 8 / 4.6. Robustness to Noise - extractive PDF cue:** 4 evaluates GA-VLN under noise levels modeled after real-world error profiles of Stretch 3 robot.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | An overly fine grid (row #4) fails to effectively compress redundant features, while an overly coarse grid (row #5) leads to the loss of ... | p. 7 (4.4. Design Analysis of GA-BEV) |
| body limitation/failure cue | Robustness to Sensor Noise on R2R-CE val unseen. | p. 8 (4.4. Design Analysis of GA-BEV) |
| body limitation/failure cue | Their combination strengthens spatial reasoning, enhances data efficiency, and yields a more robust navigation representation. | p. 6 (4.3. Ablation Study and Efficiency Analysis) |
| body limitation/failure cue | Crucially, these consistent relative improvements across different data scales confirm that GAVLN provides a robust spatial inductive bias independent of data volume. | p. 7 (4.4. Design Analysis of GA-BEV) |
| body limitation/failure cue | Noise N(0, σ2) NE↓ OSR↑ SR↑ SPL↑ w/o Noise - 4.80 67.59 60.96 55.19 Depth σ = 0.05m 4.82 65.63 59.11 54.25 Pose σ ... | p. 8 (4.4. Design Analysis of GA-BEV) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We set the learning rate of the visual encoder to 5e-6 and that of all other components to 2e-5. | p. 5 (4.1. Experimental Setup) |
| The model is optimized using a cosine annealing schedule with a minimum learning rate. | p. 5 (4.1. Experimental Setup) |
| Furthermore, Table 2 reports the per-inference theoretical TFLOPs and model latency evaluated on identical samples and hardware to demonstrate the computational efficiency of our ... | p. 6 (4.3. Ablation Study and Efficiency Analysis) |
| Detailed hardware setups and additional examples are provided in the Supplementary Material. | p. 8 (4.5. Real-World Robot Experiments) |
| To achieve efficient and geometry-aware reasoning, we replace dense RGB video tokens with a compact spatial representation that explicitly encodes geometry in a BEV ... | p. 4 (3.2. Geometry-Aware BEV Representation) |
| To incorporate broader 3D geometric priors for better spatial reasoning, we introduce representation from a pretrained 3D foundation model (e.g., VGGT [27]) f3DFM(·), which ... | p. 4 (3.2. Geometry-Aware BEV Representation) |
| While performance slightly improves when extending the temporal window from 32 to 48 action steps, it saturates or even decreases with longer histories. | p. 7 (4.4. Design Analysis of GA-BEV) |
| The token numbers represent the average number of visual tokens required per navigation step, computed over 121 sampled navigation trajectories across 61 training scenes. | p. 7 (4.4. Design Analysis of GA-BEV) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 4.4. Design Analysis of GA-BEV - extractive PDF cue:** An overly fine grid (row #4) fails to effectively compress redundant features, while an overly coarse grid (row #5) leads to the loss of important ...
- **p. 8 / 4.4. Design Analysis of GA-BEV - extractive PDF cue:** Robustness to Sensor Noise on R2R-CE val unseen.
- **p. 6 / 4.3. Ablation Study and Efficiency Analysis - extractive PDF cue:** Their combination strengthens spatial reasoning, enhances data efficiency, and yields a more robust navigation representation.
- **p. 7 / 4.4. Design Analysis of GA-BEV - extractive PDF cue:** Crucially, these consistent relative improvements across different data scales confirm that GAVLN provides a robust spatial inductive bias independent of data volume.
- **p. 8 / 4.4. Design Analysis of GA-BEV - extractive PDF cue:** Noise N(0, σ2) NE↓ OSR↑ SR↑ SPL↑ w/o Noise - 4.80 67.59 60.96 55.19 Depth σ = 0.05m 4.82 65.63 59.11 54.25 Pose σ = ...

- **PDF anchors reviewed:** datasets p. 5 (4.1. Experimental Setup), p. 5 (4.1. Experimental Setup), p. 6 (4.2. Comparison with State-of-the-Art Methods), p. 6 (4.3. Ablation Study and Efficiency Analysis), p. 8 (4.5. Real-World Robot Experiments), p. 8 (4.5. Real-World Robot Experiments), metrics p. 5 (4.1. Experimental Setup), p. 6 (4.3. Ablation Study and Efficiency Analysis), p. 7 (4.4. Design Analysis of GA-BEV), p. 8 (Figure/Table caption), p. 6 (4.2. Comparison with State-of-the-Art Methods), p. 8 (4.4. Design Analysis of GA-BEV), baselines p. 6 (4.3. Ablation Study and Efficiency Analysis), p. 6 (4.2. Comparison with State-of-the-Art Methods), p. 5 (4.1. Experimental Setup), p. 5 (4.2. Comparison with State-of-the-Art Methods), p. 7 (4.4. Design Analysis of GA-BEV), p. 8 (4.5. Real-World Robot Experiments), results p. 5 (4.1. Experimental Setup), p. 5 (4.2. Comparison with State-of-the-Art Methods), p. 6 (4.3. Ablation Study and Efficiency Analysis), p. 6 (4.3. Ablation Study and Efficiency Analysis), p. 7 (4.4. Design Analysis of GA-BEV), p. 7 (4.4. Design Analysis of GA-BEV).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
