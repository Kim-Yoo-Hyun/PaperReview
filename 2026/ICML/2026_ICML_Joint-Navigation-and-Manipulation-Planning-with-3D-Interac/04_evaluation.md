# Evaluation - Joint Navigation and Manipulation Planning with 3D Interaction Chains

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=oVB2xYWvpv; PDF retrieval source: https://openreview.net/pdf/fa35fc3f33ae33100b9b86126d95a99def1057d8.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (5.2. Evaluation Results), p. 9 (Figure/Table caption), p. 9 (5.4. Comparison with SOTA Methods), p. 8 (5.3. Real-world Evaluation), p. 7 (5.2. Evaluation Results), p. 8 (5.2. Evaluation Results)): Experimental results validate improvements in both success rate and efficiency (SPL).

## Evaluation Body Digest

- **p. 6 / 5.1. Experimental Setup - extractive body cue:** In the OVMM benchmark, the "steps" metric calculates the average number of steps across all episodes where the agent actively terminates, including failed episodes.
- **p. 7 / 5.1. Experimental Setup - extractive body cue:** For real-world experiments, we use the Hello Robot Stretch 3 as the experimental platform.
- **p. 8 / 5.2. Evaluation Results - extractive body cue:** Real-world Experiment. "Intra" denotes intra-room tasks where the object and goal receptacle are co-located in the same room. "Cross" refers to cross-room tasks where they ...
- **p. 8 / 5.3. Real-world Evaluation - extractive body cue:** For each method, we conducted a total of 35 evaluation episodes, comprising 25 intra-room and 10 cross-room tasks.
- **p. 9 / 5.3. Real-world Evaluation - extractive body cue:** Demonstration of real-world experiments and the decision-making process.
- **p. 9 / 5.3. Real-world Evaluation - extractive body cue:** The bottom-left visualizes the robot's actual trajectory and the selection of interaction waypoints, identifying both candidates (blue) and the selected target (red); note that the ...
- **p. 7 / 5.1. Experimental Setup - extractive body cue:** To determine li, we utilize the simulator's ground truth to calculate the minimum number of steps required to complete the tasks in each stage via ...
- **p. 6 / 5.1. Experimental Setup - extractive body cue:** To provide a more robust assessment of execution efficiency, we employ the standard Success weighted by normalized inverse Path Length (SPL) (Anderson et al., 2018) ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mobile base와 one/two-arm manipulation environment.
- **Input boundary:** egocentric RGB-D, language/task goal, base-arm proprioception.
- **Output/decision under evaluation:** base motion plus arm/gripper action.
- **Primary target:** long-horizon task success, reachability, collision과 recovery.
- **Detected evaluation headings:** 5. Experiment (p. 6); 5.1. Experimental Setup (p. 6); 5.2. Evaluation Results (p. 7); 5.3. Real-world Evaluation (p. 8).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5.2. Evaluation Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Experimental results validate improvements in both success rate and efficiency (SPL). | p. 7 (5.2. Evaluation Results) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 5. Comparisons with the related works. We report Success Rate (SR) and Success weighted by Path Length (SPL) across all four stages. Note ... | p. 9 (Figure/Table caption) |
| 5.4. Comparison with SOTA Methods | EMPIRICAL / REAL-ROBOT OR HARDWARE | Notably, while our method is built upon the OVMM (Heuristic) baseline, which originally exhibited significantly lower Overall Success Rate (SR) compared to the OVMM ... | p. 9 (5.4. Comparison with SOTA Methods) |
| 5.3. Real-world Evaluation | EMPIRICAL / REAL-ROBOT OR HARDWARE | Experimental results demonstrate that our method yields significant performance improvements, particularly in long-horizon cross-room tasks and during the Place stage. | p. 8 (5.3. Real-world Evaluation) |
| 5.2. Evaluation Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our approach, which utilizes a 3D feature map to construct interaction point representations, achieves the highest performance (Row 4). | p. 7 (5.2. Evaluation Results) |

## Dataset / Benchmark Role

- **p. 6 / 5.1. Experimental Setup - extractive body cue:** In the OVMM benchmark, the "steps" metric calculates the average number of steps across all episodes where the agent actively terminates, including failed episodes.
- **p. 7 / 5.1. Experimental Setup - extractive body cue:** For real-world experiments, we use the Hello Robot Stretch 3 as the experimental platform.
- **p. 8 / 5.2. Evaluation Results - extractive body cue:** Real-world Experiment. "Intra" denotes intra-room tasks where the object and goal receptacle are co-located in the same room. "Cross" refers to cross-room tasks where they ...
- **p. 8 / 5.3. Real-world Evaluation - extractive body cue:** For each method, we conducted a total of 35 evaluation episodes, comprising 25 intra-room and 10 cross-room tasks.
- **p. 9 / 5.3. Real-world Evaluation - extractive body cue:** Demonstration of real-world experiments and the decision-making process.
- **p. 9 / 5.3. Real-world Evaluation - extractive body cue:** The bottom-left visualizes the robot's actual trajectory and the selection of interaction waypoints, identifying both candidates (blue) and the selected target (red); note that the ...
- **p. 7 / 5.1. Experimental Setup - extractive body cue:** To determine li, we utilize the simulator's ground truth to calculate the minimum number of steps required to complete the tasks in each stage via ...
- **p. 6 / 5.1. Experimental Setup - extractive body cue:** To provide a more robust assessment of execution efficiency, we employ the standard Success weighted by normalized inverse Path Length (SPL) (Anderson et al., 2018) ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. (a) Existing methods for OVMM typically plan navi- gation and manipulation as separate stages, which can result in navigation endpoints that are suboptimal ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. The framework of 3D-IC. Patch features are extracted from RGB images and projected to establish a 3D feature map. Candidate interaction waypoints are ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Comparison with other 3D Interaction Point Represen- tations. "PCD Feat." relies solely on geometric features extracted from point clouds. "PCD Feat. + Label" ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3. Qualitative comparison between the baseline and our method. Each column represents a distinct evaluation case. For each case, Row 1 displays the 2D ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2. Ablation study on multi stage planning. S1,2,3,4 denotes performing independent decision-making at each stage. S1-2,3,4 and S1,2,3-4 involve joint planning for the FindObj-Pick ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Ablation study on fine-tuning. TI denotes token inter- pretation, TP denotes token preference learning and TS denotes trajectory selection. TI TP TS FindObj. ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4. Real-world Experiment. "Intra" denotes intra-room tasks where the object and goal receptacle are co-located in the same room. "Cross" refers to cross-room tasks ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 4. Demonstration of real-world experiments and the decision-making process. The top row displays RGB images from the agent's egocentric view and the third-person view ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | In the OVMM benchmark, the "steps" metric calculates the average number of steps across all episodes where the agent actively terminates, including failed episodes. | embodiment, simulator version and control stack | p. 6 (5.1. Experimental Setup), p. 7 (5.1. Experimental Setup) |
| Task/environment | For real-world experiments, we use the Hello Robot Stretch 3 as the experimental platform. | reset, timeout, object/scene variation | p. 7 (5.1. Experimental Setup), p. 8 (5.2. Evaluation Results) |
| Observation/sensor | egocentric RGB-D, language/task goal, base-arm proprioception | calibration, preprocessing, privileged input | p. 3 (3. Preliminaries of Mobile Manipulation), p. 2 (1. Introduction) |
| Output/decision | base motion plus arm/gripper action | action frame, controller and termination | p. 2 (1. Introduction), p. 3 (4.1. Unified Modeling of Multi-stage Interaction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Experimental results validate improvements in both success rate and efficiency (SPL). | definition/direction/unit from same section | p. 7 (5.2. Evaluation Results) |
| We report Success Rate (SR) and Success weighted by Path Length (SPL) across all four stages. | definition/direction/unit from same section | p. 9 (5.3. Real-world Evaluation) |
| Success rates (SR) are reported for each stage independently. | definition/direction/unit from same section | p. 6 (5.1. Experimental Setup) |
| Notably, the success rate of the final Place stage serves as the overall success rate. | definition/direction/unit from same section | p. 6 (5.1. Experimental Setup) |
| Notably, while our method is built upon the OVMM (Heuristic) baseline, which originally exhibited significantly lower Overall Success Rate (SR) compared to the OVMM ... | definition/direction/unit from same section | p. 9 (5.4. Comparison with SOTA Methods) |
| This underscores the critical importance of chain-based decision-making in OVMM, a domain inherently characterized by cross-stage dependencies and heterogeneous task types (i.e., navigation and ... | definition/direction/unit from same section | p. 8 (5.2. Evaluation Results) |
| SR SR SPL SR SPL SR SPL SR SPL Heuristic 54.1 16.7 48.5 16.6 31.3 4.8 5.1 0.8 34.8 S1,2,3,4 66.1 23.5 62.6 23.2 ... | definition/direction/unit from same section | p. 8 (5.2. Evaluation Results) |
| Figure 5. Failure cases of 3D-IC on OVMM Dataset. The failure cases are categorized according to the four standard stages of the Open Vocabulary ... | definition/direction/unit from same section | p. 13 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our method consistently outperforms prior works, establishing new state-of-the-art performance across all metrics. | comparison identity and matched condition | p. 9 (5.3. Real-world Evaluation) |
| The first column demonstrates that 3D-IC selects a superior docking point during the third stage compared to the baseline. | comparison identity and matched condition | p. 8 (5.2. Evaluation Results) |
| Notably, while our method is built upon the OVMM (Heuristic) baseline, which originally exhibited significantly lower Overall Success Rate (SR) compared to the OVMM ... | comparison identity and matched condition | p. 9 (5.4. Comparison with SOTA Methods) |
| Qualitative comparison between the baseline and our method. | comparison identity and matched condition | p. 7 (5.2. Evaluation Results) |
| 3, we adopt the standard Open-Vocabulary Mobile Manipulation (OVMM) baseline setting (Yenamandra et al., 2023). | comparison identity and matched condition | p. 6 (5.1. Experimental Setup) |
| For each case, Row 1 displays the 2D semantic map from the Heuristic baseline, and Row 2 shows the third-person view at the episode's ... | comparison identity and matched condition | p. 7 (5.2. Evaluation Results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Ablation on 3D Interaction Point Representations. | component/input/data sensitivity | p. 7 (5.2. Evaluation Results) |
| Ablation study on multi stage planning. | component/input/data sensitivity | p. 8 (5.2. Evaluation Results) |
| 8, we find that adding TI consistently improves performance over training without it. | component/input/data sensitivity | p. 8 (5.2. Evaluation Results) |
| The decision-making component employs a fine-tuned Qwen2.5-VL-7B model. | component/input/data sensitivity | p. 7 (5.1. Experimental Setup) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, we propose 3D Interaction Chains (3D-IC) for the OVMM task in this paper. | Experimental results validate improvements in both success rate and efficiency (SPL). | PDF body cue; verify exact table/figure and matched conditions | p. 7 (5.2. Evaluation Results), p. 9 (Figure/Table caption), p. 9 (5.4. Comparison with SOTA Methods), p. 8 (5.3. Real-world Evaluation), p. 7 (5.2. Evaluation Results), p. 8 (5.2. Evaluation Results) |
| Primary metric/result | Table 5. Comparisons with the related works. We report Success Rate (SR) and Success weighted by Path Length (SPL) across all four stages. Note ... | numeric claim only at cited anchor | p. 9 (Figure/Table caption) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Each Move tomato from table to counter Move apple from couch to table Move knife from cabinet to table baseline baseline 3D-IC 3D-IC High ... | p. 7 (5.2. Evaluation Results) |
| body limitation/failure cue | Consequently, the agent navigated back to a nightstand in the initial room to complete the placement, thereby avoiding a potential failure. | p. 8 (5.3. Real-world Evaluation) |
| body limitation/failure cue | The consistently high SPL scores indicate that our method achieves efficient trajectory, rather than merely reducing step counts through premature termination or failure cases ... | p. 9 (5.4. Comparison with SOTA Methods) |
| body limitation/failure cue | Figure 5. Failure cases of 3D-IC on OVMM Dataset. The failure cases are categorized according to the four standard stages of the Open Vocabulary ... | p. 13 (Figure/Table caption) |
| body limitation/failure cue | These examples highlight the advantages of 3D-IC over the baseline, specifically in considering optimal docking orientation, avoiding obstacle occlusion during placement, and generating more ... | p. 7 (5.2. Evaluation Results) |
| body limitation/failure cue | In the OVMM benchmark, the "steps" metric calculates the average number of steps across all episodes where the agent actively terminates, including failed episodes. | p. 6 (5.1. Experimental Setup) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| In the OVMM benchmark, the "steps" metric calculates the average number of steps across all episodes where the agent actively terminates, including failed episodes. | p. 6 (5.1. Experimental Setup) |
| Row 3 presents the 2D projection of our 3D feature map (where color intensity encodes height), and Row 4 depicts the final third-person view ... | p. 7 (5.2. Evaluation Results) |
| For the 3D feature map, we leverage the visual encoder from Qwen2.5-VL-7B (Bai et al., 2025) to obtain patch features, and the voxel resolution ... | p. 7 (5.1. Experimental Setup) |
| Concretely, the RGB image is encoded into patch-level semantic features {zt,i} = ViT(Ir t ) using a Vision Transformer (ViT). | p. 4 (4.2. 3D-IC Construction) |
| To further compute the term 1 K PK k=1 P(wk), local features surrounding each waypoint wk are queried from Mt and organized via a ... | p. 5 (4.3. Joint Planning with 3D-IC) |
| The policy is optimized using a standard autoregressive cross-entropy loss: L(θ) = -PT t=1 log pθ (xt / xprompt, x<t), where the loss is ... | p. 6 (4.3. Joint Planning with 3D-IC) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 5.2. Evaluation Results - extractive body cue:** Each Move tomato from table to counter Move apple from couch to table Move knife from cabinet to table baseline baseline 3D-IC 3D-IC High Navigation ...
- **p. 8 / 5.3. Real-world Evaluation - extractive body cue:** Consequently, the agent navigated back to a nightstand in the initial room to complete the placement, thereby avoiding a potential failure.
- **p. 9 / 5.4. Comparison with SOTA Methods - extractive body cue:** The consistently high SPL scores indicate that our method achieves efficient trajectory, rather than merely reducing step counts through premature termination or failure cases (i.e., ...
- **p. 13 / Figure/Table caption - extractive body cue:** Figure 5. Failure cases of 3D-IC on OVMM Dataset. The failure cases are categorized according to the four standard stages of the Open Vocabulary Mobile ...
- **p. 7 / 5.2. Evaluation Results - extractive body cue:** These examples highlight the advantages of 3D-IC over the baseline, specifically in considering optimal docking orientation, avoiding obstacle occlusion during placement, and generating more efficient ...
- **p. 6 / 5.1. Experimental Setup - extractive body cue:** In the OVMM benchmark, the "steps" metric calculates the average number of steps across all episodes where the agent actively terminates, including failed episodes.

- **Evidence anchors reviewed:** datasets p. 6 (5.1. Experimental Setup), p. 7 (5.1. Experimental Setup), p. 8 (5.2. Evaluation Results), p. 8 (5.3. Real-world Evaluation), p. 9 (5.3. Real-world Evaluation), p. 9 (5.3. Real-world Evaluation), metrics p. 7 (5.2. Evaluation Results), p. 9 (5.3. Real-world Evaluation), p. 6 (5.1. Experimental Setup), p. 6 (5.1. Experimental Setup), p. 9 (5.4. Comparison with SOTA Methods), p. 8 (5.2. Evaluation Results), baselines p. 9 (5.3. Real-world Evaluation), p. 8 (5.2. Evaluation Results), p. 9 (5.4. Comparison with SOTA Methods), p. 7 (5.2. Evaluation Results), p. 6 (5.1. Experimental Setup), p. 7 (5.2. Evaluation Results), results p. 7 (5.2. Evaluation Results), p. 9 (Figure/Table caption), p. 9 (5.4. Comparison with SOTA Methods), p. 8 (5.3. Real-world Evaluation), p. 7 (5.2. Evaluation Results), p. 8 (5.2. Evaluation Results).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
