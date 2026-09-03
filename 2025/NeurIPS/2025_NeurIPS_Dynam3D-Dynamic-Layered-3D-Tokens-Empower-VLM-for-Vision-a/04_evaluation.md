# Evaluation - Dynam3D: Dynamic Layered 3D Tokens Empower VLM for Vision-and-Language Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=s6k9l5yX8e; PDF retrieval source: https://arxiv.org/pdf/2505.11383. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments)): Our Dynam3D still demonstrates substantial improvements, outperforming NaVid by over 13% in Success Rate (SR) on REVERIE-CE and by over 5% on NavRAG-CE.

## Evaluation Body Digest

- **p. 8 / 4 Experiments - extractive body cue:** Methods Pre-exploration Lifelong Memory R2R-CE Val REVERIE-CE Val NE↓OSR↑SR↑SPL↑NE↓OSR↑SR↑SPL↑ NaVid [5] × × 5.47 49.1 37.4 35.9 6.74 36.3 26.6 20.8 g3D-LF [14] × × ...
- **p. 8 / 4 Experiments - extractive body cue:** For each scene, previously stored 3D representations can be leveraged in subsequent episodes to simulate gradual familiarization of the agent with the environment during task ...
- **p. 7 / 4 Experiments - extractive body cue:** To ensure a fair comparison on the more challenging and realistic benchmarks such as REVERIE-CE which use coarse-grained and high-level destination description, and NavRAG-CE which ...
- **p. 14 / A.1 Datasets and Experimental Details - extractive body cue:** We pre-train our Dynam3D representation model on the aforementioned dataset for 100K episodes (approximately 8 days) using four RTX 6000 Ada GPUs.
- **p. 14 / A.1 Datasets and Experimental Details - extractive body cue:** We employ the Hello Robot Stretch 3 for real-world navigation experiments, leveraging its real-time localization and pose estimation capabilities.
- **p. 9 / 4 Experiments - extractive body cue:** Target Target Target Target Target Step 1 Step 2 Step 3 Step 4 Step 5 Figure 4: A demonstration of navigation in a dynamic real-world ...
- **p. 7 / 4 Experiments - extractive body cue:** 4.1 Comparison with SOTA Methods As shown in Tables 1 and 2, we evaluate the navigation performance of our Dynam3D across three distinct continuous-environment VLN ...
- **p. 9 / 4 Experiments - extractive body cue:** Instruction: "Please bring me the white fruit bowl filled with apples from the chair." Dynamic environment: During the robot's navigation process, the white fruit bowl ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 4 Experiments (p. 7); A.1 Datasets and Experimental Details (p. 14).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our Dynam3D still demonstrates substantial improvements, outperforming NaVid by over 13% in Success Rate (SR) on REVERIE-CE and by over 5% on NavRAG-CE. | p. 7 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Compared to prior state-of-the-art methods, e.g., g3D-LF and Uni-NaVid, our Dynam3D achieves an improvement of nearly 5% in navigation success rate (SR). | p. 7 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Under the Lifelong Memory setting, our Dynam3D also achieves performance gains, with a 2.7% SR improvement on R2R-CE and a 4.9% SR improvement on ... | p. 8 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | In the static environment (Table 4) Dynam3D achieves a 20% higher success rate than baselines, reaching 70% after pre-exploration. | p. 8 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | The navigation performance significantly decreases without Subspace Alignment supervision (Table 6, row 3), highlighting the limitations of naive CLIP feature distillation for 3D instance ... | p. 9 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 8 / 4 Experiments - extractive body cue:** Methods Pre-exploration Lifelong Memory R2R-CE Val REVERIE-CE Val NE↓OSR↑SR↑SPL↑NE↓OSR↑SR↑SPL↑ NaVid [5] × × 5.47 49.1 37.4 35.9 6.74 36.3 26.6 20.8 g3D-LF [14] × × ...
- **p. 8 / 4 Experiments - extractive body cue:** For each scene, previously stored 3D representations can be leveraged in subsequent episodes to simulate gradual familiarization of the agent with the environment during task ...
- **p. 7 / 4 Experiments - extractive body cue:** To ensure a fair comparison on the more challenging and realistic benchmarks such as REVERIE-CE which use coarse-grained and high-level destination description, and NavRAG-CE which ...
- **p. 14 / A.1 Datasets and Experimental Details - extractive body cue:** We pre-train our Dynam3D representation model on the aforementioned dataset for 100K episodes (approximately 8 days) using four RTX 6000 Ada GPUs.
- **p. 14 / A.1 Datasets and Experimental Details - extractive body cue:** We employ the Hello Robot Stretch 3 for real-world navigation experiments, leveraging its real-time localization and pose estimation capabilities.
- **p. 9 / 4 Experiments - extractive body cue:** Target Target Target Target Target Step 1 Step 2 Step 3 Step 4 Step 5 Figure 4: A demonstration of navigation in a dynamic real-world ...
- **p. 7 / 4 Experiments - extractive body cue:** 4.1 Comparison with SOTA Methods As shown in Tables 1 and 2, we evaluate the navigation performance of our Dynam3D across three distinct continuous-environment VLN ...
- **p. 9 / 4 Experiments - extractive body cue:** Instruction: "Please bring me the white fruit bowl filled with apples from the chair." Dynamic environment: During the robot's navigation process, the white fruit bowl ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Different vision-language large models for monocular VLN tasks. Compared to previous video-based representations (a), our Dynam3D (b) adopts dynamic hierarchical 3D representations offering ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: The architecture of our Dynam3D framework. Our Dynam3D takes posed monocular RGB and depth images as input and outputs atomic navigation actions. It ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Left: Illustration of the feature points update and frustum culling strategy. Right: The supervision of feature distillation and 3D-language contrastive learning for our ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Evaluation of VLN on R2R-CE with monocular setting. ∗denotes zero-shot method. Methods LLM Scene Representation R2R-CE Val R2R-CE Test NE↓OSR↑SR↑SPL↑NE↓OSR↑SR↑SPL↑ CM2 [50]
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: Evaluation of VLN on REVERIE-CE and NavRAG-CE with monocular setting. ∗denotes zero-shot method. Methods LLM Scene Representation REVERIE-CE Val NavRAG-CE Val NE↓OSR↑SR↑SPL↑NE↓OSR↑SR↑SPL↑
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3: Evaluation of VLN for Pre-exploration and Lifelong Memory. Pre-exploration allows agents to scan and encode environmental representations before evaluation, while Lifelong Memory enables ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4: Real-world navigation experiments in static environments. Methods NE↓OSR↑SR↑ NaVid 2.2 45 35
- **p. 8 / Figure/Table caption - extractive body cue:** Table 5: Real-world navigation experiments in dynamic environments. Methods NE↓OSR↑SR↑ NaVid 3.6 45 20

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Methods Pre-exploration Lifelong Memory R2R-CE Val REVERIE-CE Val NE↓OSR↑SR↑SPL↑NE↓OSR↑SR↑SPL↑ NaVid [5] × × 5.47 49.1 37.4 35.9 6.74 36.3 26.6 20.8 g3D-LF [14] × ... | embodiment, simulator version and control stack | p. 8 (4 Experiments), p. 8 (4 Experiments) |
| Task/environment | For each scene, previously stored 3D representations can be leveraged in subsequent episodes to simulate gradual familiarization of the agent with the environment during ... | reset, timeout, object/scene variation | p. 8 (4 Experiments), p. 7 (4 Experiments) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 1 (Abstract), p. 2 (1 Introduction) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 1 (1 Introduction), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Our Dynam3D still demonstrates substantial improvements, outperforming NaVid by over 13% in Success Rate (SR) on REVERIE-CE and by over 5% on NavRAG-CE. | definition/direction/unit from same section | p. 7 (4 Experiments) |
| Compared to prior state-of-the-art methods, e.g., g3D-LF and Uni-NaVid, our Dynam3D achieves an improvement of nearly 5% in navigation success rate (SR). | definition/direction/unit from same section | p. 7 (4 Experiments) |
| In the static environment (Table 4) Dynam3D achieves a 20% higher success rate than baselines, reaching 70% after pre-exploration. | definition/direction/unit from same section | p. 8 (4 Experiments) |
| Compared to NaVid [5] which uses a video-based large model, our Dynam3D employing both the Pre-exploration and Lifelong Memory achieves over a 20% increase ... | definition/direction/unit from same section | p. 8 (4 Experiments) |
| We utilize the DAgger strategy [57, 17] to enhance error correction by deliberately introducing probabilistic deviations that mislead the agent towards incorrect waypoints. | definition/direction/unit from same section | p. 14 (A.1 Datasets and Experimental Details) |
| Instance Subspace Alignment Zone R2R-CE Val REVERIE-CE Val NE↓OSR↑SR↑SPL↑NE↓OSR↑SR↑SPL↑ × × × 5.63 51.1 45.7 40.2 6.89 34.8 25.7 17.8 ✓ ✓ × 5.26 ... | definition/direction/unit from same section | p. 9 (4 Experiments) |
| The agent is then guided back to the correct path, thereby strengthening its ability to recover from navigation errors. | definition/direction/unit from same section | p. 14 (A.1 Datasets and Experimental Details) |
| Figure 1: Different vision-language large models for monocular VLN tasks. Compared to previous video-based representations (a), our Dynam3D (b) adopts dynamic hierarchical 3D representations ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Compared to prior state-of-the-art methods, e.g., g3D-LF and Uni-NaVid, our Dynam3D achieves an improvement of nearly 5% in navigation success rate (SR). | comparison identity and matched condition | p. 7 (4 Experiments) |
| In the dynamic setting (Figure 4 and Table 5), the target is manually moved to another location once the robot reach within two meters ... | comparison identity and matched condition | p. 8 (4 Experiments) |
| Our Dynam3D still demonstrates substantial improvements, outperforming NaVid by over 13% in Success Rate (SR) on REVERIE-CE and by over 5% on NavRAG-CE. | comparison identity and matched condition | p. 7 (4 Experiments) |
| In the static environment (Table 4) Dynam3D achieves a 20% higher success rate than baselines, reaching 70% after pre-exploration. | comparison identity and matched condition | p. 8 (4 Experiments) |
| Figure 1: Different vision-language large models for monocular VLN tasks. Compared to previous video-based representations (a), our Dynam3D (b) adopts dynamic hierarchical 3D representations ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |
| 4.5 Ablation Study Table 6 reports our ablation results. | comparison identity and matched condition | p. 9 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 4.5 Ablation Study Table 6 reports our ablation results. | component/input/data sensitivity | p. 9 (4 Experiments) |
| The navigation performance significantly decreases without Subspace Alignment supervision (Table 6, row 3), highlighting the limitations of naive CLIP feature distillation for 3D instance ... | component/input/data sensitivity | p. 9 (4 Experiments) |
| After removing samples with impassable paths, we obtain 4M+ instruction-trajectory pairs in continuous settings. | component/input/data sensitivity | p. 14 (A.1 Datasets and Experimental Details) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our main contributions include: • We propose Dynam3D, a multi-level patch-instance-zone 3D representation model that performs online 3D instance and zone-level encoding ... | Our Dynam3D still demonstrates substantial improvements, outperforming NaVid by over 13% in Success Rate (SR) on REVERIE-CE and by over 5% on NavRAG-CE. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments) |
| Primary metric/result | Compared to prior state-of-the-art methods, e.g., g3D-LF and Uni-NaVid, our Dynam3D achieves an improvement of nearly 5% in navigation success rate (SR). | numeric claim only at cited anchor | p. 7 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 8 / 4 Experiments - extractive body cue:** Each setting includes 20 test cases, and navigation is deemed successful if the robot stops within 1 meter of the target.
- **p. 8 / 4 Experiments - extractive body cue:** Methods NE↓OSR↑SR↑ NaVid 3.6 45 20 g3D-LF 4.6 35 10 Dynam3D 1.9 60 45 + Pre-exploration 1.4 75 45 4.4 Computational Cost and Real-Time Analysis ...
- **p. 8 / 4 Experiments - extractive body cue:** During training, each navigation step takes 455ms (∼0.46 seconds) on average: 83ms for 3D representation updates, 315ms for large language model, and 57ms for other ...
- **p. 9 / 4 Experiments - extractive body cue:** Target Target Target Target Target Step 1 Step 2 Step 3 Step 4 Step 5 Figure 4: A demonstration of navigation in a dynamic real-world ...
- **p. 14 / A.1 Datasets and Experimental Details - extractive body cue:** The model is deployed on a workstation equipped with an NVIDIA RTX 4090 GPU and 64GB of RAM, and communicates with the robot over a ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 1: Different vision-language large models for monocular VLN tasks. Compared to previous video-based representations (a), our Dynam3D (b) adopts dynamic hierarchical 3D representations ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | The navigation performance significantly decreases without Subspace Alignment supervision (Table 6, row 3), highlighting the limitations of naive CLIP feature distillation for 3D instance ... | p. 9 (4 Experiments) |
| body limitation/failure cue | In the dynamic setting (Figure 4 and Table 5), the target is manually moved to another location once the robot reach within two meters ... | p. 8 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The training is performed with a batch size of 4 and a learning rate of 1e-4. | p. 14 (A.1 Datasets and Experimental Details) |
| Pre-exploration allows agents to scan and encode environmental representations before evaluation, while Lifelong Memory enables agents to retain the environmental representations of previous episodes ... | p. 8 (4 Experiments) |
| Methods NE↓OSR↑SR↑ NaVid 3.6 45 20 g3D-LF 4.6 35 10 Dynam3D 1.9 60 45 + Pre-exploration 1.4 75 45 4.4 Computational Cost and Real-Time ... | p. 8 (4 Experiments) |
| Most navigation episodes can be completed within 20 to 40 navigation steps, our navigation system supports real-time 3D representation updates and navigation action prediction ... | p. 9 (4 Experiments) |
| To mitigate memory consumption and enable efficient training of large models, we employ the Adafactor optimizer [58] in conjunction with Gradient Checkpointing [59]. | p. 14 (A.1 Datasets and Experimental Details) |
| To encode 3D environments, we extract patch-level 2D features using CLIP [11] and project them into 3D space via depth maps and camera poses. | p. 2 (1 Introduction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Different vision-language large models for monocular VLN tasks. Compared to previous video-based representations (a), our Dynam3D (b) adopts dynamic hierarchical 3D representations offering ...
- **p. 9 / 4 Experiments - extractive body cue:** The navigation performance significantly decreases without Subspace Alignment supervision (Table 6, row 3), highlighting the limitations of naive CLIP feature distillation for 3D instance supervision.
- **p. 8 / 4 Experiments - extractive body cue:** In the dynamic setting (Figure 4 and Table 5), the target is manually moved to another location once the robot reach within two meters of ...

- **Evidence anchors reviewed:** datasets p. 8 (4 Experiments), p. 8 (4 Experiments), p. 7 (4 Experiments), p. 14 (A.1 Datasets and Experimental Details), p. 14 (A.1 Datasets and Experimental Details), p. 9 (4 Experiments), metrics p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 14 (A.1 Datasets and Experimental Details), p. 9 (4 Experiments), baselines p. 7 (4 Experiments), p. 8 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 2 (Figure/Table caption), p. 9 (4 Experiments), results p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
