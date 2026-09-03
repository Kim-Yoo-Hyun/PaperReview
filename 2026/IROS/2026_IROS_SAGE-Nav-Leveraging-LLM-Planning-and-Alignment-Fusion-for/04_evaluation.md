# Evaluation - SAGE-Nav: Leveraging LLM Planning and Alignment Fusion for Hierarchical Scene Graph-Guided Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2606.25497; PDF retrieval source: https://arxiv.org/pdf/2606.25497. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS)): In iTHOR, SAGE-Nav achieves state-of-the-art Success Rates (SR) of 82.47% overall and 77.22% in challenging long-horizon scenarios (L ≥5), outperforming TSOG and CGI-GAIL by absolute margins of 3.76 and 8.04 ...

## Evaluation Body Digest

- **p. 5 / V. EXPERIMENTS - extractive body cue:** Experimental Setup 1) Datasets: We evaluate the proposed framework across two widely used embodied simulation datasets: iTHOR [45] and RoboTHOR [46]. iTHOR comprises 120 photorealistic ...
- **p. 5 / V. EXPERIMENTS - extractive body cue:** Furthermore, in the structurally complex RoboTHOR environment, SAGE-Nav establishes a new state-of-the-art across all metrics, notably reaching 40.82% SR and 22.95% SPL in long-horizon tasks.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** 4: Visualization of the agent trajectories in unfamiliar scenes in the AI2-THOR environment.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** Furthermore, they are prone to getting stuck in rotational loops or prematurely terminating episodes when targets are occluded.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** EFFICIENCY TRADEOFF IN ROBOTHOR Method SR↑(%) SPL↑(%) Latency↓(s) LLM Calls↓ CogNav [27] 54.6 24.3 2.20 15 SG-Nav [16] 47.5 24.0 0.85 32 SAGE-Nav (Ours) 52.4 ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** The full SAGE-Nav (ID 7) achieves the best SR, particularly in long-horizon tasks (L ≥5).
- **p. 5 / V. EXPERIMENTS - extractive body cue:** 2) Evaluation Metrics: To comprehensively assess navigation performance, we adopt three standard Object-Goal Navigation metrics [2]: Success Rate (SR), Success weighted by Path Length (SPL), ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** Crucially, leveraging waypoint guidance for hardto-find targets, our method improves both the navigation success rate and overall robustness.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** V. EXPERIMENTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| V. EXPERIMENTS | EMPIRICAL / SIMULATION | In iTHOR, SAGE-Nav achieves state-of-the-art Success Rates (SR) of 82.47% overall and 77.22% in challenging long-horizon scenarios (L ≥5), outperforming TSOG and CGI-GAIL by ... | p. 5 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / SIMULATION | Crucially, leveraging waypoint guidance for hardto-find targets, our method improves both the navigation success rate and overall robustness. | p. 6 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / SIMULATION | These results show that decoupling high-level semantic planning from local reactive control improves inference efficiency while preserving navigation performance. | p. 6 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / SIMULATION | 2) Evaluation Metrics: To comprehensively assess navigation performance, we adopt three standard Object-Goal Navigation metrics [2]: Success Rate (SR), Success weighted by Path Length ... | p. 5 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / SIMULATION | Incremental integration (IDs 1-3) confirms that hierarchical planning and encoding significantly improve SR and DTS, emphasizing the synergy of structural reasoning. | p. 7 (V. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 5 / V. EXPERIMENTS - extractive body cue:** Experimental Setup 1) Datasets: We evaluate the proposed framework across two widely used embodied simulation datasets: iTHOR [45] and RoboTHOR [46]. iTHOR comprises 120 photorealistic ...
- **p. 5 / V. EXPERIMENTS - extractive body cue:** Furthermore, in the structurally complex RoboTHOR environment, SAGE-Nav establishes a new state-of-the-art across all metrics, notably reaching 40.82% SR and 22.95% SPL in long-horizon tasks.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** 4: Visualization of the agent trajectories in unfamiliar scenes in the AI2-THOR environment.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** Furthermore, they are prone to getting stuck in rotational loops or prematurely terminating episodes when targets are occluded.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** EFFICIENCY TRADEOFF IN ROBOTHOR Method SR↑(%) SPL↑(%) Latency↓(s) LLM Calls↓ CogNav [27] 54.6 24.3 2.20 15 SG-Nav [16] 47.5 24.0 0.85 32 SAGE-Nav (Ours) 52.4 ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** The full SAGE-Nav (ID 7) achieves the best SR, particularly in long-horizon tasks (L ≥5).

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 1: Pipeline Overview: (i) LLM-Guided Hierarchical Global Planner (H-GP) generates semantic waypoint sequences; (ii) Hierarchical Scene Graph Encoder (HSGE) grounds the plan in structured ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: HSGE Architecture. A multi-layer R-GCN encodes structural relations, a residual attention module for task align- ment and level-wise pooling produces the final structure- ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: The asynchronous A3C training architecture. Par- allel workers collect trajectories to compute losses. A shared optimizer backpropagates gradients-visually denoted by the fire symbol-to ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 4: Visualization of the agent trajectories in unfamiliar scenes in the AI2-THOR environment. TABLE IV: IMPACTS OF DIFFERENT MODULES ID
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5: Failure case visualizations. The target object is high- lighted with a red bounding box, while the agent-detected target is marked in green across ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Experimental Setup 1) Datasets: We evaluate the proposed framework across two widely used embodied simulation datasets: iTHOR [45] and RoboTHOR [46]. iTHOR comprises 120 ... | embodiment, simulator version and control stack | p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Task/environment | Furthermore, in the structurally complex RoboTHOR environment, SAGE-Nav establishes a new state-of-the-art across all metrics, notably reaching 40.82% SR and 22.95% SPL in long-horizon ... | reset, timeout, object/scene variation | p. 5 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 2 (IV. PROPOSED METHOD), p. 2 (I. INTRODUCTION) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 1 (I. INTRODUCTION), p. 3 (IV. PROPOSED METHOD) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 2) Evaluation Metrics: To comprehensively assess navigation performance, we adopt three standard Object-Goal Navigation metrics [2]: Success Rate (SR), Success weighted by Path Length ... | definition/direction/unit from same section | p. 5 (V. EXPERIMENTS) |
| Crucially, leveraging waypoint guidance for hardto-find targets, our method improves both the navigation success rate and overall robustness. | definition/direction/unit from same section | p. 6 (V. EXPERIMENTS) |
| In iTHOR, SAGE-Nav achieves state-of-the-art Success Rates (SR) of 82.47% overall and 77.22% in challenging long-horizon scenarios (L ≥5), outperforming TSOG and CGI-GAIL by ... | definition/direction/unit from same section | p. 5 (V. EXPERIMENTS) |
| Eliminating the HSGE (ID 5) leads to a notable drop in success rates, confirming that multi-scale structural embeddings are vital for capturing scene-level global ... | definition/direction/unit from same section | p. 7 (V. EXPERIMENTS) |
| It achieves the lowest latency (0.42 s), the highest SPL (30.1%), and a competitive SR (52.4%). | definition/direction/unit from same section | p. 6 (V. EXPERIMENTS) |
| Notably, when GAFN is removed and substituted with simple feature concatenation (ID 6), the model exhibits a marginal SPL gain but a concurrent deterioration ... | definition/direction/unit from same section | p. 7 (V. EXPERIMENTS) |
| Fig. 1: Pipeline Overview: (i) LLM-Guided Hierarchical Global Planner (H-GP) generates semantic waypoint sequences; (ii) Hierarchical Scene Graph Encoder (HSGE) grounds the plan in ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| In iTHOR, SAGE-Nav achieves state-of-the-art Success Rates (SR) of 82.47% overall and 77.22% in challenging long-horizon scenarios (L ≥5), outperforming TSOG and CGI-GAIL by ... | comparison identity and matched condition | p. 5 (V. EXPERIMENTS) |
| As shown in Table II, SAGE-Nav outperforms all baseline methods across all metrics, achieving a 75.05% SR, 34.05% SPL and 0.38 m DTS. | comparison identity and matched condition | p. 6 (V. EXPERIMENTS) |
| Furthermore, in the structurally complex RoboTHOR environment, SAGE-Nav establishes a new state-of-the-art across all metrics, notably reaching 40.82% SR and 22.95% SPL in long-horizon ... | comparison identity and matched condition | p. 5 (V. EXPERIMENTS) |
| The baseline algorithms exhibit suboptimal path planning, resulting in redundant paths and detours. | comparison identity and matched condition | p. 6 (V. EXPERIMENTS) |
| Specifically, the inclusion of H-GP (ID 2) provides crucial commonsense priors for target localization, improving SR by 2.59% over the baseline. | comparison identity and matched condition | p. 7 (V. EXPERIMENTS) |
| Ablation Studies Table IV summarizes the ablation study of proposed modules. | comparison identity and matched condition | p. 7 (V. EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Ablation Study on Zero-shot Generalization. | component/input/data sensitivity | p. 6 (V. EXPERIMENTS) |
| Ablation Studies Table IV summarizes the ablation study of proposed modules. | component/input/data sensitivity | p. 7 (V. EXPERIMENTS) |
| Notably, when GAFN is removed and substituted with simple feature concatenation (ID 6), the model exhibits a marginal SPL gain but a concurrent deterioration ... | component/input/data sensitivity | p. 7 (V. EXPERIMENTS) |
| Consequently, the optimization exclusively focuses on tuning the learnable components, namely the Hierarchical Scene Graph Encoder (HSGE) and the LSTM-based policy network. | component/input/data sensitivity | p. 5 (V. EXPERIMENTS) |
| Component analysis further elucidates the hierarchical contributions of each module to the zero-shot capability. | component/input/data sensitivity | p. 6 (V. EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, the contributions of this work are threefold: • We propose SAGE-Nav, a hierarchical navigation | In iTHOR, SAGE-Nav achieves state-of-the-art Success Rates (SR) of 82.47% overall and 77.22% in challenging long-horizon scenarios (L ≥5), outperforming TSOG and CGI-GAIL by ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS) |
| Primary metric/result | Crucially, leveraging waypoint guidance for hardto-find targets, our method improves both the navigation success rate and overall robustness. | numeric claim only at cited anchor | p. 6 (V. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 5 / V. EXPERIMENTS - extractive body cue:** We use the first 20 scenes of each category for training, the next 5 for validation, and the remaining 5 for testing.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** We consider 22 object categories as targets, ensuring at least four objects per room type.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** We report these metrics across all trajectories (ALL) and challenging long-horizon scenarios with optimal path lengths of at least 5 meters (L ≥5).
- **p. 5 / V. EXPERIMENTS - extractive body cue:** Notably, all experiments run on a single NVIDIA RTX 3090 GPU, ensuring the high-frequency reactive control loop remains strictly decoupled from asynchronous LLM planning overhead.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** While CogNav achieves the highest SR (54.6%), its reliance on heavy visual and multimodal foundation models at each step leads to high action latency (2.20 ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** SG-Nav reduces this latency to 0.85 s but requires frequent LLM queries (32 calls per episode).

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Limitations We analyze the failure cases (Fig. | p. 7 (V. EXPERIMENTS) |
| body limitation/failure cue | 5), which fall into four categories: (a) Target Visibility Failure, where the agent terminates despite the target (e.g., plates on high shelves) being outside ... | p. 7 (V. EXPERIMENTS) |
| body limitation/failure cue | This performance comprehensively validates the robustness of our hierarchical priors and dynamic scheduling mechanism. | p. 5 (V. EXPERIMENTS) |
| body limitation/failure cue | Crucially, leveraging waypoint guidance for hardto-find targets, our method improves both the navigation success rate and overall robustness. | p. 6 (V. EXPERIMENTS) |
| body limitation/failure cue | Replacing the LLM with heuristic rules that select waypoints based solely on graph scores highlights the critical role of commonsense priors, which rigid graph ... | p. 6 (V. EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Notably, all experiments run on a single NVIDIA RTX 3090 GPU, ensuring the high-frequency reactive control loop remains strictly decoupled from asynchronous LLM planning ... | p. 5 (V. EXPERIMENTS) |
| The A3C [6] policy is trained for 6 million episodes using Adam (learning rate 1 × 10-4). | p. 5 (V. EXPERIMENTS) |
| AKGVP-CI TSOG Ours Kitchen Living room Bedroom Bathroom Pan Television Laptop Success (30 steps) Fail (99 steps) Fail (99 steps) Success (40 steps) Fail ... | p. 7 (V. EXPERIMENTS) |
| 5), which fall into four categories: (a) Target Visibility Failure, where the agent terminates despite the target (e.g., plates on high shelves) being outside ... | p. 7 (V. EXPERIMENTS) |
| Specifically, the abstract waypoint sequence generated by the LLM-driven Hierarchical Global Planner (H-GP) is structurally encoded into topology-aware embeddings by the Hierarchical Scene Graph ... | p. 2 (IV. PROPOSED METHOD) |
| This multi-relational connectivity explicitly encodes relation types and metric distances, providing a structural foundation for downstream R-GCN encoding (Sec. | p. 3 (IV. PROPOSED METHOD) |
| 1: Pipeline Overview: (i) LLM-Guided Hierarchical Global Planner (H-GP) generates semantic waypoint sequences; (ii) Hierarchical Scene Graph Encoder (HSGE) grounds the plan in structured ... | p. 3 (IV. PROPOSED METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / V. EXPERIMENTS - extractive body cue:** Limitations We analyze the failure cases (Fig.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** 5), which fall into four categories: (a) Target Visibility Failure, where the agent terminates despite the target (e.g., plates on high shelves) being outside the ...
- **p. 5 / V. EXPERIMENTS - extractive body cue:** This performance comprehensively validates the robustness of our hierarchical priors and dynamic scheduling mechanism.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** Crucially, leveraging waypoint guidance for hardto-find targets, our method improves both the navigation success rate and overall robustness.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** Replacing the LLM with heuristic rules that select waypoints based solely on graph scores highlights the critical role of commonsense priors, which rigid graph searches ...

- **Evidence anchors reviewed:** datasets p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), metrics p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), baselines p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), results p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
