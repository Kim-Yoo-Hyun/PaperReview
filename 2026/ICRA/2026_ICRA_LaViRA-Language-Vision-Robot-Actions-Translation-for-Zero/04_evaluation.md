# Evaluation - LaViRA: Language-Vision-Robot Actions Translation for Zero-Shot Vision Language Navigation in Continuous Environments

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html; PDF retrieval source: https://arxiv.org/pdf/2510.19655. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 5 (IV. SIMULATION EXPERIMENTS), p. 5 (IV. SIMULATION EXPERIMENTS), p. 6 (IV. SIMULATION EXPERIMENTS), p. 6 (IV. SIMULATION EXPERIMENTS)): Fig. 5: Real-world experiment examples. LaViRA guides a Unitree Go1 quadruped (top) and an Agilex Cobot Magic wheeled robot (bottom) in an office. The visualization shows the third-person view of ...

## Evaluation Body Digest

- **p. 5 / IV. SIMULATION EXPERIMENTS - extractive body cue:** We use the Habitat simulator [34] with the VLN-CE dataset [2], which extends the R2R benchmark from Matterport3D (MP3D) [10] for continuous navigation.
- **p. 6 / V. REAL-WORLD EXPERIMENTS - extractive body cue:** To validate LaViRA's practicality beyond simulation, we deployed it on two distinct real-world robots: a Unitree Go1 quadruped and an Agilex Cobot Magic wheeled platform.
- **p. 5 / IV. SIMULATION EXPERIMENTS - extractive body cue:** Following recent zero-shot works [3], [4], we report results on a standard 100-episode subset from the validation unseen split.
- **p. 6 / V. REAL-WORLD EXPERIMENTS - extractive body cue:** These qualitative results confirm that LaViRA's hierarchical reasoning generalizes effectively from simulation to physical hardware without any training.
- **p. 5 / IV. SIMULATION EXPERIMENTS - extractive body cue:** We use standard VLN metrics: Navigation Error (NE), the final distance to goal; Success Rate (SR), our primary metric for stopping within 3m; Oracle Success ...
- **p. 6 / IV. SIMULATION EXPERIMENTS - extractive body cue:** The failure cases illustrate three common errors: (1) A Language Action error from ambiguous instructions, e.g., failing to identify the correct door when multiple doors ...
- **p. 6 / IV. SIMULATION EXPERIMENTS - extractive body cue:** 6.96±0.24 35.7±4.0 27.7±2.5 21.8±1.8 w/o history 6.90±0.46 36.3±7.0 27.0±5.6 19.4±7.3 Backtracking Mechanism w/o backtrack 6.92±0.32 42.0±3.0 30.0±4.4 22.2±4.0 last waypoint only 6.65±0.16 41.7±6.0 31.7±1.5 23.5±1.0 ...
- **p. 5 / IV. SIMULATION EXPERIMENTS - extractive body cue:** Using a powerful MLLM (e.g., GPT-4o) for high-level Language Action (LA) is key; replacing it with the smaller Qwen2.5-VL-72B leads to a 7.0-point drop in ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** IV. SIMULATION EXPERIMENTS (p. 5); V. REAL-WORLD EXPERIMENTS (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 5: Real-world experiment examples. LaViRA guides a Unitree Go1 quadruped (top) and an Agilex Cobot Magic wheeled robot (bottom) in an office. The ... | p. 7 (Figure/Table caption) |
| IV. SIMULATION EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | LaViRA significantly outperforms all previous zero-shot methods. | p. 5 (IV. SIMULATION EXPERIMENTS) |
| IV. SIMULATION EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | We use standard VLN metrics: Navigation Error (NE), the final distance to goal; Success Rate (SR), our primary metric for stopping within 3m; Oracle ... | p. 5 (IV. SIMULATION EXPERIMENTS) |
| IV. SIMULATION EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our full framework outperforms the latter by 14.4 points, confirming the effectiveness of coarse-to-fine decomposition. | p. 6 (IV. SIMULATION EXPERIMENTS) |
| IV. SIMULATION EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Removing the highlevel planner ("w/o LA") yields 4.4% SPL, while removing the perceptual grounding module ("w/o VA") achieves 13.9% SPL. | p. 6 (IV. SIMULATION EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 5 / IV. SIMULATION EXPERIMENTS - extractive body cue:** We use the Habitat simulator [34] with the VLN-CE dataset [2], which extends the R2R benchmark from Matterport3D (MP3D) [10] for continuous navigation.
- **p. 6 / V. REAL-WORLD EXPERIMENTS - extractive body cue:** To validate LaViRA's practicality beyond simulation, we deployed it on two distinct real-world robots: a Unitree Go1 quadruped and an Agilex Cobot Magic wheeled platform.
- **p. 5 / IV. SIMULATION EXPERIMENTS - extractive body cue:** Following recent zero-shot works [3], [4], we report results on a standard 100-episode subset from the validation unseen split.
- **p. 6 / V. REAL-WORLD EXPERIMENTS - extractive body cue:** These qualitative results confirm that LaViRA's hierarchical reasoning generalizes effectively from simulation to physical hardware without any training.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Prior methods rely on pre-trained waypoint prediction or value mapping with limited online planning. Our LaViRA framework instead decomposes navigation into language- level ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: The LaViRA Pipeline. Our framework decomposes navigation into three sequential stages. (1) Language Action: A large MLLM processes the instruction, history, and current ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Prompts for Language and Vision Actions. (Left) The prompt for the Language Action model, which takes in full context to decide on a ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 4: Visualization examples. (Left) Navigation visualization: Language Action outputs are in blue text. Vision Action outputs bounding boxes in green and target descriptions in ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5: Real-world experiment examples. LaViRA guides a Unitree Go1 quadruped (top) and an Agilex Cobot Magic wheeled robot (bottom) in an office. The visualization ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We use the Habitat simulator [34] with the VLN-CE dataset [2], which extends the R2R benchmark from Matterport3D (MP3D) [10] for continuous navigation. | embodiment, simulator version and control stack | p. 5 (IV. SIMULATION EXPERIMENTS), p. 6 (V. REAL-WORLD EXPERIMENTS) |
| Task/environment | To validate LaViRA's practicality beyond simulation, we deployed it on two distinct real-world robots: a Unitree Go1 quadruped and an Agilex Cobot Magic wheeled ... | reset, timeout, object/scene variation | p. 6 (V. REAL-WORLD EXPERIMENTS), p. 5 (IV. SIMULATION EXPERIMENTS) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 3 (III. PROPOSED METHOD), p. 2 (I. INTRODUCTION) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 4 (III. PROPOSED METHOD), p. 2 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We use standard VLN metrics: Navigation Error (NE), the final distance to goal; Success Rate (SR), our primary metric for stopping within 3m; Oracle ... | definition/direction/unit from same section | p. 5 (IV. SIMULATION EXPERIMENTS) |
| The failure cases illustrate three common errors: (1) A Language Action error from ambiguous instructions, e.g., failing to identify the correct door when multiple ... | definition/direction/unit from same section | p. 6 (IV. SIMULATION EXPERIMENTS) |
| 6.96±0.24 35.7±4.0 27.7±2.5 21.8±1.8 w/o history 6.90±0.46 36.3±7.0 27.0±5.6 19.4±7.3 Backtracking Mechanism w/o backtrack 6.92±0.32 42.0±3.0 30.0±4.4 22.2±4.0 last waypoint only 6.65±0.16 41.7±6.0 31.7±1.5 ... | definition/direction/unit from same section | p. 6 (IV. SIMULATION EXPERIMENTS) |
| Using a powerful MLLM (e.g., GPT-4o) for high-level Language Action (LA) is key; replacing it with the smaller Qwen2.5-VL-72B leads to a 7.0-point drop ... | definition/direction/unit from same section | p. 5 (IV. SIMULATION EXPERIMENTS) |
| Fig. 4: Visualization examples. (Left) Navigation visualization: Language Action outputs are in blue text. Vision Action outputs bounding boxes in green and target descriptions ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Fig. 2: The LaViRA Pipeline. Our framework decomposes navigation into three sequential stages. (1) Language Action: A large MLLM processes the instruction, history, and ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Fig. 5: Real-world experiment examples. LaViRA guides a Unitree Go1 quadruped (top) and an Agilex Cobot Magic wheeled robot (bottom) in an office. The ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Fig. 5: Real-world experiment examples. LaViRA guides a Unitree Go1 quadruped (top) and an Agilex Cobot Magic wheeled robot (bottom) in an office. The ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| LaViRA significantly outperforms all previous zero-shot methods. | comparison identity and matched condition | p. 5 (IV. SIMULATION EXPERIMENTS) |
| Our baseline for these studies is LaViRA (GPT-4o + Qwen2.5-VL-32B). | comparison identity and matched condition | p. 5 (IV. SIMULATION EXPERIMENTS) |
| An end-to-end baseline ("w/o LA+VA") fails with 0% SPL. | comparison identity and matched condition | p. 6 (IV. SIMULATION EXPERIMENTS) |
| Our full framework outperforms the latter by 14.4 points, confirming the effectiveness of coarse-to-fine decomposition. | comparison identity and matched condition | p. 6 (IV. SIMULATION EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Although the Gemini-2.5-Pro variant delivered superior performance, we used the GPT4o variant for ablations due to documented stability issues with the Gemini-2.5-Pro API during ... | component/input/data sensitivity | p. 5 (IV. SIMULATION EXPERIMENTS) |
| These qualitative results confirm that LaViRA's hierarchical reasoning generalizes effectively from simulation to physical hardware without any training. | component/input/data sensitivity | p. 6 (V. REAL-WORLD EXPERIMENTS) |
| Ablation Studies We performed a series of ablation studies to analyze LaViRA's performance and quantify the contribution of its core components. | component/input/data sensitivity | p. 5 (IV. SIMULATION EXPERIMENTS) |
| We conducted further ablations on key design choices, as shown in Table III. | component/input/data sensitivity | p. 6 (IV. SIMULATION EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions are as follows: • We propose a general action decomposition strategy for zero-shot VLN-CE that separates navigation into language-level planning, vision-level grounding, ... | Fig. 5: Real-world experiment examples. LaViRA guides a Unitree Go1 quadruped (top) and an Agilex Cobot Magic wheeled robot (bottom) in an office. The ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 5 (IV. SIMULATION EXPERIMENTS), p. 5 (IV. SIMULATION EXPERIMENTS), p. 6 (IV. SIMULATION EXPERIMENTS), p. 6 (IV. SIMULATION EXPERIMENTS) |
| Primary metric/result | LaViRA significantly outperforms all previous zero-shot methods. | numeric claim only at cited anchor | p. 5 (IV. SIMULATION EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 5 / IV. SIMULATION EXPERIMENTS - extractive body cue:** An episode is successful if the agent stops within 3 meters of the target.
- **p. 5 / IV. SIMULATION EXPERIMENTS - extractive body cue:** The agent's observation is composed of posed 640×480 RGB-D images, low-level path planning is executed using the Fast Marching Method (FMM) on a global map ...
- **p. 5 / IV. SIMULATION EXPERIMENTS - extractive body cue:** All experiments were conducted on 8 NVIDIA RTX 4090 GPUs for parallel evaluation.
- **p. 5 / IV. SIMULATION EXPERIMENTS - extractive body cue:** On average, each trajectory required approximately 32,682 tokens with 7.93 calls for the high-level planner (GPT-4o) and 8,050 tokens with 7.50 calls for the grounding ...
- **p. 5 / IV. SIMULATION EXPERIMENTS - extractive body cue:** Method NE↓ OSR↑ SR↑ SPL↑ Supervised Learning CMA [35] 6.92 45 37 32.2 RecBERT [35] 5.80 57 48 43.2 ETPNav [21] 5.15 58 52 52.2 ...
- **p. 5 / IV. SIMULATION EXPERIMENTS - extractive body cue:** The Gemini-2.5-Pro variant achieves SR of 38.3% and SPL of 28.3%, improving over the prior best zero-shot method InstructNav [6] by 7.3 points in SR ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Its performance ceiling is bounded by off-the-shelf models, as seen in failures on ambiguous instructions and large-area grounding. | p. 7 (VI. CONCLUSION) |
| body limitation/failure cue | (Right) Failure cases visualization: Language Action misjudges direction due to ambiguous instructions; Vision Action selects the wrong region despite correct target description; simulation reconstruction ... | p. 7 (VI. CONCLUSION) |
| body limitation/failure cue | Qualitative Analysis To offer qualitative insights into LaViRA's decisionmaking, Figure 4 shows a successful navigation run and common failures. | p. 6 (IV. SIMULATION EXPERIMENTS) |
| body limitation/failure cue | The failure cases illustrate three common errors: (1) A Language Action error from ambiguous instructions, e.g., failing to identify the correct door when multiple ... | p. 6 (IV. SIMULATION EXPERIMENTS) |
| body limitation/failure cue | Fig. 2: The LaViRA Pipeline. Our framework decomposes navigation into three sequential stages. (1) Language Action: A large MLLM processes the instruction, history, and ... | p. 3 (Figure/Table caption) |
| body limitation/failure cue | Low standard deviations across runs highlight the framework's robustness and stability, a key advantage for real-world applications. | p. 5 (IV. SIMULATION EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Qualitative Analysis To offer qualitative insights into LaViRA's decisionmaking, Figure 4 shows a successful navigation run and common failures. | p. 6 (IV. SIMULATION EXPERIMENTS) |
| These qualitative results confirm that LaViRA's hierarchical reasoning generalizes effectively from simulation to physical hardware without any training. | p. 6 (V. REAL-WORLD EXPERIMENTS) |
| Given the target position pworld, the agent computes a short-term path using the Fast Marching Method (FMM). | p. 5 (III. PROPOSED METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / VI. CONCLUSION - extractive body cue:** Its performance ceiling is bounded by off-the-shelf models, as seen in failures on ambiguous instructions and large-area grounding.
- **p. 7 / VI. CONCLUSION - extractive body cue:** (Right) Failure cases visualization: Language Action misjudges direction due to ambiguous instructions; Vision Action selects the wrong region despite correct target description; simulation reconstruction errors ...
- **p. 6 / IV. SIMULATION EXPERIMENTS - extractive body cue:** Qualitative Analysis To offer qualitative insights into LaViRA's decisionmaking, Figure 4 shows a successful navigation run and common failures.
- **p. 6 / IV. SIMULATION EXPERIMENTS - extractive body cue:** The failure cases illustrate three common errors: (1) A Language Action error from ambiguous instructions, e.g., failing to identify the correct door when multiple doors ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: The LaViRA Pipeline. Our framework decomposes navigation into three sequential stages. (1) Language Action: A large MLLM processes the instruction, history, and current ...
- **p. 5 / IV. SIMULATION EXPERIMENTS - extractive body cue:** Low standard deviations across runs highlight the framework's robustness and stability, a key advantage for real-world applications.

- **Evidence anchors reviewed:** datasets p. 5 (IV. SIMULATION EXPERIMENTS), p. 6 (V. REAL-WORLD EXPERIMENTS), p. 5 (IV. SIMULATION EXPERIMENTS), p. 6 (V. REAL-WORLD EXPERIMENTS), metrics p. 5 (IV. SIMULATION EXPERIMENTS), p. 6 (IV. SIMULATION EXPERIMENTS), p. 6 (IV. SIMULATION EXPERIMENTS), p. 5 (IV. SIMULATION EXPERIMENTS), p. 7 (Figure/Table caption), p. 3 (Figure/Table caption), baselines p. 7 (Figure/Table caption), p. 5 (IV. SIMULATION EXPERIMENTS), p. 5 (IV. SIMULATION EXPERIMENTS), p. 6 (IV. SIMULATION EXPERIMENTS), p. 6 (IV. SIMULATION EXPERIMENTS), results p. 7 (Figure/Table caption), p. 5 (IV. SIMULATION EXPERIMENTS), p. 5 (IV. SIMULATION EXPERIMENTS), p. 6 (IV. SIMULATION EXPERIMENTS), p. 6 (IV. SIMULATION EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
