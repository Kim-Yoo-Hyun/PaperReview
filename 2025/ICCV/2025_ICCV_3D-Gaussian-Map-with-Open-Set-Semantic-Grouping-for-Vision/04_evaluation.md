# Evaluation - 3D Gaussian Map with Open-Set Semantic Grouping for Vision-Language Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Gao_3D_Gaussian_Map_with_Open-Set_Semantic_Grouping_for_Vision-Language_Navigation_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Gao_3D_Gaussian_Map_with_Open-Set_Semantic_Grouping_for_Vision-Language_Navigation_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.2. Comparison to State-of-the-Arts), p. 6 (4.2. Comparison to State-of-the-Arts), p. 8 (4.3. Diagnostic Experiment), p. 7 (4.2. Comparison to State-of-the-Arts), p. 7 (4.2. Comparison to State-of-the-Arts), p. 8 (4.3. Diagnostic Experiment)): Our agent achieves consistent improvements across all splits, which outperforms BEVBert [1] by 2% in both SR and SPL on the val unseen split.

## Evaluation Body Digest

- **p. 6 / 4.1. Experimental Setup - extractive body cue:** We evaluate our method on three benchmark datasets: R2R [3], R4R [32], and REVERIE [56].
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** R2R contains 7,189 trajectories, each paired with three natural language instructions, split into train, val seen, val unseen, and test unseen sets spanning 61, 56, ...
- **p. 7 / 4.2. Comparison to State-of-the-Arts - extractive body cue:** Qualitative results on R2R [3] val unseen split.
- **p. 7 / 4.2. Comparison to State-of-the-Arts - extractive body cue:** Visualization of 3D Gaussian Maps on R2R [3] val unseen split.
- **p. 8 / 4.3. Diagnostic Experiment - extractive body cue:** Ablation studies of MAP strategy on val unseen split of R2R [3] and REVERIE [56].
- **p. 8 / 4.3. Diagnostic Experiment - extractive body cue:** To evaluate each component, we conduct diagnostic studies on val unseen splits of both R2R [3] and REVERIE [56].
- **p. 5 / 3.5. Implementation Details - extractive body cue:** Optimal iterations are determined based on peak performance on val unseen splits.
- **p. 5 / 3.5. Implementation Details - extractive body cue:** In addition, during navigation, constructing the 3D Gaussian Map at each time step takes approximately 0.07 seconds, ensuring compatibility with real-time robotic execution (see more ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 3.5. Implementation Details (p. 5); 4. Experiment (p. 6); 4.1. Experimental Setup (p. 6); 4.3. Diagnostic Experiment (p. 8).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Comparison to State-of-the-Arts | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our agent achieves consistent improvements across all splits, which outperforms BEVBert [1] by 2% in both SR and SPL on the val unseen split. | p. 6 (4.2. Comparison to State-of-the-Arts) |
| 4.2. Comparison to State-of-the-Arts | EMPIRICAL / SOURCE-REPORTED EVALUATION | Specifically, compared to HAMT [12], our approach achieves improvements of 2% in SR, CLS, and nDTW, with 3% gain in SDTW. | p. 6 (4.2. Comparison to State-of-the-Arts) |
| 4.3. Diagnostic Experiment | EMPIRICAL / SOURCE-REPORTED EVALUATION | From Table 5, we can observe that: i) Row #1 vs #2 vs #3 vs #4: Each level contributes to performance gain, and the ... | p. 8 (4.3. Diagnostic Experiment) |
| 4.2. Comparison to State-of-the-Arts | EMPIRICAL / SOURCE-REPORTED EVALUATION | This success highlights the advantage of our 3D Gaussian Map in capturing detailed scene information, thereby enabling the agent to achieve accurate navigation. | p. 7 (4.2. Comparison to State-of-the-Arts) |
| 4.2. Comparison to State-of-the-Arts | EMPIRICAL / SOURCE-REPORTED EVALUATION | Benefiting from the geometric priors and open-set semantics of the 3D Gaussian Map, our agent achieves a comprehensive understanding of spatial structures and semantic ... | p. 7 (4.2. Comparison to State-of-the-Arts) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Experimental Setup - extractive body cue:** We evaluate our method on three benchmark datasets: R2R [3], R4R [32], and REVERIE [56].
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** R2R contains 7,189 trajectories, each paired with three natural language instructions, split into train, val seen, val unseen, and test unseen sets spanning 61, 56, ...
- **p. 7 / 4.2. Comparison to State-of-the-Arts - extractive body cue:** Qualitative results on R2R [3] val unseen split.
- **p. 7 / 4.2. Comparison to State-of-the-Arts - extractive body cue:** Visualization of 3D Gaussian Maps on R2R [3] val unseen split.
- **p. 8 / 4.3. Diagnostic Experiment - extractive body cue:** Ablation studies of MAP strategy on val unseen split of R2R [3] and REVERIE [56].
- **p. 8 / 4.3. Diagnostic Experiment - extractive body cue:** To evaluate each component, we conduct diagnostic studies on val unseen splits of both R2R [3] and REVERIE [56].
- **p. 5 / 3.5. Implementation Details - extractive body cue:** Optimal iterations are determined based on peak performance on val unseen splits.
- **p. 5 / 3.5. Implementation Details - extractive body cue:** In addition, during navigation, constructing the 3D Gaussian Map at each time step takes approximately 0.07 seconds, ensuring compatibility with real-time robotic execution (see more ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Dense Features vs 3D Gaussians. Recent VLN meth- ods [1, 47, 49, 78] rely on dense sampling to construct scene maps, which often ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overview of our method. At each node, our agent leverages egocentric RGB-D observations to generate pseudo-lidar point clouds, which are then used to ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. 3D Gaussian Map Optimization. Gaussian parameters (position µ, scale s, rotation r, opacity α, color c, and semantic σ) are optimized through the ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Quantitative results on REVERIE [56]. ‘-': unavailable statistics. See §4.2 for more details. R2R val unseen test unseen Models TL↓ NE↓SR↑SPL↑ TL↓
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Quantitative results on R2R [3] (§4.2).
- **p. 6 / Figure/Table caption - extractive body cue:** Table 3. Quantitative results on R4R [32] (§4.2). Success-weighted Dynamic Time Warping (SDTW) for bal- ancing accuracy with SR. On REVERIE, Remote Ground- ing Success ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Qualitative results on R2R [3] val unseen split. (a) Our agent successfully navigates through multiple rooms and recognizes key landmarks, such as the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. Visualization of 3D Gaussian Maps on R2R [3] val unseen split. Benefiting from the geometric priors and open-set semantics of the 3D Gaussian ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We evaluate our method on three benchmark datasets: R2R [3], R4R [32], and REVERIE [56]. | embodiment, simulator version and control stack | p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup) |
| Task/environment | R2R contains 7,189 trajectories, each paired with three natural language instructions, split into train, val seen, val unseen, and test unseen sets spanning 61, ... | reset, timeout, object/scene variation | p. 6 (4.1. Experimental Setup), p. 7 (4.2. Comparison to State-of-the-Arts) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 4 (3.3. Multi-Level Action Prediction (MAP)), p. 3 (3. Method) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 3 (3. Method), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The performance is evaluated using Trajectory Length (TL), Navigation Error (NE), Success Rate (SR), and Success-weighted Path Length (SPL), following [46]. | definition/direction/unit from same section | p. 6 (4.1. Experimental Setup) |
| Table 3. Quantitative results on R4R [32] (§4.2). Success-weighted Dynamic Time Warping (SDTW) for bal- ancing accuracy with SR. On REVERIE, Remote Ground- ing ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| This success highlights the advantage of our 3D Gaussian Map in capturing detailed scene information, thereby enabling the agent to achieve accurate navigation. | definition/direction/unit from same section | p. 7 (4.2. Comparison to State-of-the-Arts) |
| 6) to demonMAP Levels R2R [3] REVERIE [56] # Scene View Instance SR↑ SPL↑ SR↑ RGS↑ RGSPL↑ 1 - - - 72 60 46.98 ... | definition/direction/unit from same section | p. 8 (4.3. Diagnostic Experiment) |
| This demonstrates that our 3D Gaussian Map enables the agent to recognize and integrate semantic and geometric information from the environment, leading to more ... | definition/direction/unit from same section | p. 7 (4.2. Comparison to State-of-the-Arts) |
| Ablation studies of MAP strategy on val unseen split of R2R [3] and REVERIE [56]. | definition/direction/unit from same section | p. 8 (4.3. Diagnostic Experiment) |
| Figure 3. 3D Gaussian Map Optimization. Gaussian parameters (position µ, scale s, rotation r, opacity α, color c, and semantic σ) are optimized through ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| The multi-level navigation scores, combined with the traditional 2D action score [13], jointly evaluate and rank these transitions. | definition/direction/unit from same section | p. 5 (3.5. Implementation Details) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| As shown in Table 3, our method maintains a strong performance on R4R, consistently outperforming existing approaches. | comparison identity and matched condition | p. 6 (4.2. Comparison to State-of-the-Arts) |
| Specifically, compared to HAMT [12], our approach achieves improvements of 2% in SR, CLS, and nDTW, with 3% gain in SDTW. | comparison identity and matched condition | p. 6 (4.2. Comparison to State-of-the-Arts) |
| We first assess the contributions of each component by progressively incorporating ESM (§3.1), OSG (§3.2), and MAP (§3.3) into the baseline model (row #1). | comparison identity and matched condition | p. 8 (4.3. Diagnostic Experiment) |
| Rows #1 and #5 show that combining all components together results in the largest gain over the baseline (e.g., 72% →77% for SR on ... | comparison identity and matched condition | p. 8 (4.3. Diagnostic Experiment) |
| Following prior works [13, 49], to support long-time and context-aware navigation, we adopt a topological memory mechanism that dynamically updates as the agent explores ... | comparison identity and matched condition | p. 5 (3.5. Implementation Details) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| On REVERIE, Remote Grounding Success (RGS) and its SPL-weighted variant (RGSPL) evaluate object grounding accuracy. | component/input/data sensitivity | p. 6 (4.1. Experimental Setup) |
| Ablation studies of MAP strategy on val unseen split of R2R [3] and REVERIE [56]. | component/input/data sensitivity | p. 8 (4.3. Diagnostic Experiment) |
| To evaluate each component, we conduct diagnostic studies on val unseen splits of both R2R [3] and REVERIE [56]. | component/input/data sensitivity | p. 8 (4.3. Diagnostic Experiment) |
| Following classical paradigm [13], the pretrained model is finetuned using DAgger [62]. | component/input/data sensitivity | p. 5 (3.5. Implementation Details) |
| Offline pretraining is conducted on a single NVIDIA RTX 4090 GPU for 15 iterations (see more details in Appendix). | component/input/data sensitivity | p. 5 (3.5. Implementation Details) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In contrast, our method introduces a set of sparse and adaptive 3D Gaussians to model the 3D scene, efficiently capturing spatial structures and integrating ... | Our agent achieves consistent improvements across all splits, which outperforms BEVBert [1] by 2% in both SR and SPL on the val unseen split. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.2. Comparison to State-of-the-Arts), p. 6 (4.2. Comparison to State-of-the-Arts), p. 8 (4.3. Diagnostic Experiment), p. 7 (4.2. Comparison to State-of-the-Arts), p. 7 (4.2. Comparison to State-of-the-Arts), p. 8 (4.3. Diagnostic Experiment) |
| Primary metric/result | Specifically, compared to HAMT [12], our approach achieves improvements of 2% in SR, CLS, and nDTW, with 3% gain in SDTW. | numeric claim only at cited anchor | p. 6 (4.2. Comparison to State-of-the-Arts) |

- Numeric sentences retained from the body:
- **p. 5 / 3.5. Implementation Details - extractive body cue:** Offline pretraining is conducted on a single NVIDIA RTX 4090 GPU for 15 iterations (see more details in Appendix).
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** R2R contains 7,189 trajectories, each paired with three natural language instructions, split into train, val seen, val unseen, and test unseen sets spanning 61, 56, ...
- **p. 3 / 3. Method - extractive body cue:** The action space At comprises Nt neighboring nodes Vt = {Vt,n}Nt n=1, other observed nodes V∗ t (through backtrack [13, 69]), and a [STOP] option.
- **p. 5 / 3.5. Implementation Details - extractive body cue:** Offline pretraining is conducted on a single NVIDIA RTX 4090 GPU for 15 iterations (see more details in Appendix).

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | (b) Our agent precisely identifies and localizes the "bathroom" and "rug", while BEVBert [1] stops in the wrong place since critical landmarks cannot be ... | p. 7 (4.2. Comparison to State-of-the-Arts) |
| body limitation/failure cue | Figure 1. Dense Features vs 3D Gaussians. Recent VLN meth- ods [1, 47, 49, 78] rely on dense sampling to construct scene maps, which ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | These results further demonstrate the robustness of our method in main9257 | p. 6 (4.2. Comparison to State-of-the-Arts) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Finetuning is performed over 25k iterations with a batch size of 8 and a learning rate of 1e-5. | p. 5 (3.5. Implementation Details) |
| Offline pretraining is conducted on a single NVIDIA RTX 4090 GPU for 15 iterations (see more details in Appendix). | p. 5 (3.5. Implementation Details) |
| 5 (a), we explicitly synthesize view-level 3D Gaussian Maps at different waypoints, showing that our method naturally encodes rich 3D spatial information, which previous ... | p. 7 (4.2. Comparison to State-of-the-Arts) |
| Specifically, Σi = RSS⊤R⊤encodes scale and orientation, where the rotation matrix R and the scale matrix S are stored as a 3D vector si ... | p. 4 (3.1. Egocentric Scene Map (ESM)) |
| Similarly, an analogous differentiable rendering process is applied to compute the depth ˆDt(u, v) at each pixel of the specific camera pose: ˆDt(u, v) ... | p. 4 (3.1. Egocentric Scene Map (ESM)) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 4.2. Comparison to State-of-the-Arts - extractive body cue:** (b) Our agent precisely identifies and localizes the "bathroom" and "rug", while BEVBert [1] stops in the wrong place since critical landmarks cannot be identified, ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Dense Features vs 3D Gaussians. Recent VLN meth- ods [1, 47, 49, 78] rely on dense sampling to construct scene maps, which often ...
- **p. 6 / 4.2. Comparison to State-of-the-Arts - extractive body cue:** These results further demonstrate the robustness of our method in main9257

- **Evidence anchors reviewed:** datasets p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 7 (4.2. Comparison to State-of-the-Arts), p. 7 (4.2. Comparison to State-of-the-Arts), p. 8 (4.3. Diagnostic Experiment), p. 8 (4.3. Diagnostic Experiment), metrics p. 6 (4.1. Experimental Setup), p. 6 (Figure/Table caption), p. 7 (4.2. Comparison to State-of-the-Arts), p. 8 (4.3. Diagnostic Experiment), p. 7 (4.2. Comparison to State-of-the-Arts), p. 8 (4.3. Diagnostic Experiment), baselines p. 6 (4.2. Comparison to State-of-the-Arts), p. 6 (4.2. Comparison to State-of-the-Arts), p. 8 (4.3. Diagnostic Experiment), p. 8 (4.3. Diagnostic Experiment), p. 5 (3.5. Implementation Details), results p. 6 (4.2. Comparison to State-of-the-Arts), p. 6 (4.2. Comparison to State-of-the-Arts), p. 8 (4.3. Diagnostic Experiment), p. 7 (4.2. Comparison to State-of-the-Arts), p. 7 (4.2. Comparison to State-of-the-Arts), p. 8 (4.3. Diagnostic Experiment).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
