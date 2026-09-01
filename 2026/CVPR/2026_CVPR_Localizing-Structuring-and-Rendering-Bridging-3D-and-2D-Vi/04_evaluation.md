# Evaluation - Localizing, Structuring, and Rendering: Bridging 3D and 2D Vision-Language-Action Models for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Zhao_Localizing_Structuring_and_Rendering_Bridging_3D_and_2D_Vision-Language-Action_Models_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhao_Localizing_Structuring_and_Rendering_Bridging_3D_and_2D_Vision-Language-Action_Models_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (Figure/Table caption), p. 7 (4.1. Simulation Results), p. 7 (4.1. Simulation Results), p. 6 (Figure/Table caption), p. 8 (4.4. Parameter & Viewpoint Analysis), p. 1 (Figure/Table caption)): Figure 8. Beam parameters improvement for small objects. deployment confirm that color-encoded spatial beams and world-aligned cube markers generalize beyond synthetic environments. DiffRender-VLA substantially outperforms recent approa ...

## Evaluation Body Digest

- **p. 7 / 4. Experiments - extractive PDF cue:** Real-World Deployment Situation. lation heatmaps Qcoarse, world-aligned cube markers with adaptive sizing (ℓcube = 10-15cm, scaled to 0.8× object size for small targets); (3) We ...
- **p. 7 / 4. Experiments - extractive PDF cue:** Real-world: success rate, translation/rotation error, 20 trials/task.
- **p. 8 / 4.3. Ablation Studies - extractive PDF cue:** Condition DiffRender-VLA RVT-2 [14] OpenVLA-OFT [23] Gap In-Domain 80.5 68.4 53.4 12.1/27.1 Novel Objects 74.2 (-6.3) 60.1 (-8.3) 43.7 (-9.7) 14.1/30.5 Novel Scenes 71.8 (-8.7) ...
- **p. 6 / 4. Experiments - extractive PDF cue:** We deploy on an AgileX PIPER with Robotic 2F-85 gripper.
- **p. 6 / 4. Experiments - extractive PDF cue:** These tasks cover diverse challenges including multi-step planning, fine-grained spatial reasoning, and cluttered scene.
- **p. 8 / 4.2. Real-World Deployment Results - extractive PDF cue:** Beam parameters improvement for small objects. deployment confirm that color-encoded spatial beams and world-aligned cube markers generalize beyond synthetic environments.
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Simulation results on RLBench. Success rates (%) with standard deviation. Best results in bold, second best underlined.
- **p. 7 / 4.1. Simulation Results - extractive PDF cue:** Success rates (%) across 20 trials per task.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.1. Simulation Results (p. 7); 4.2. Real-World Deployment Results (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 8. Beam parameters improvement for small objects. deployment confirm that color-encoded spatial beams and world-aligned cube markers generalize beyond synthetic environments. DiffRender-VLA substantially ... | p. 8 (Figure/Table caption) |
| 4.1. Simulation Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | DiffRender-VLA significantly outperforms 2D visual prompting approaches: TraceVLA (63.9%, +16.6%) and VLA-adapter (60.6%, +19.9%). | p. 7 (4.1. Simulation Results) |
| 4.1. Simulation Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Task-specific improvements highlight spatial understanding capabilities: Occlusion Tasks: Average 91.7% success (+7.6% over GWM). | p. 7 (4.1. Simulation Results) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 1. Simulation results on RLBench. Success rates (%) with standard deviation. Best results in bold, second best underlined. | p. 6 (Figure/Table caption) |
| 4.4. Parameter & Viewpoint Analysis | EMPIRICAL / REAL-ROBOT OR HARDWARE | This sweet spot balances visual perceptibility of directional cues, (b) The 3D surface visualization confirms this trade-off, showing performance degradation (85%) when either parameter ... | p. 8 (4.4. Parameter & Viewpoint Analysis) |

## Dataset / Benchmark Role

- **p. 7 / 4. Experiments - extractive PDF cue:** Real-World Deployment Situation. lation heatmaps Qcoarse, world-aligned cube markers with adaptive sizing (ℓcube = 10-15cm, scaled to 0.8× object size for small targets); (3) We ...
- **p. 7 / 4. Experiments - extractive PDF cue:** Real-world: success rate, translation/rotation error, 20 trials/task.
- **p. 8 / 4.3. Ablation Studies - extractive PDF cue:** Condition DiffRender-VLA RVT-2 [14] OpenVLA-OFT [23] Gap In-Domain 80.5 68.4 53.4 12.1/27.1 Novel Objects 74.2 (-6.3) 60.1 (-8.3) 43.7 (-9.7) 14.1/30.5 Novel Scenes 71.8 (-8.7) ...
- **p. 6 / 4. Experiments - extractive PDF cue:** We deploy on an AgileX PIPER with Robotic 2F-85 gripper.
- **p. 6 / 4. Experiments - extractive PDF cue:** These tasks cover diverse challenges including multi-step planning, fine-grained spatial reasoning, and cluttered scene.
- **p. 8 / 4.2. Real-World Deployment Results - extractive PDF cue:** Beam parameters improvement for small objects. deployment confirm that color-encoded spatial beams and world-aligned cube markers generalize beyond synthetic environments.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. 2D VLA models (left-top) leverage intuitive semantic perception from multi-view transformers but struggle with explicit 3D spatial reasoning. 3D VLA models (left-bottom) achieve ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Overview of DiffRender-VLA. The framework bridges spatial and 2D VLA paradigms through differentiable rendering: localiz- ing anchors the next manipulation target, structuring encodes ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3. Visualization of differentiable point cloud rendered image. We use RLbench [19] and RH20T [10] dataset for display. Precision task: Place the stamp Occluded ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4. Visualization of our real-world tasks. For each task, we show several steps to understand the task process. We fuse VLA features with coarse ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Simulation results on RLBench. Success rates (%) with standard deviation. Best results in bold, second best underlined.
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 5. Simulation Tasks for Occlusion and Clutter enviroments.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 6. Real-World Deployment Situation. lation heatmaps Qcoarse, world-aligned cube markers with adaptive sizing (ℓcube = 10-15cm, scaled to 0.8× object size for small targets); ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Real-world results on AgileX PIPER. Success rates (%) across 20 trials per task.

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Real-World Deployment Situation. lation heatmaps Qcoarse, world-aligned cube markers with adaptive sizing (ℓcube = 10-15cm, scaled to 0.8× object size for small targets); (3) ... | embodiment, simulator version and control stack | p. 7 (4. Experiments), p. 7 (4. Experiments) |
| Task/environment | Real-world: success rate, translation/rotation error, 20 trials/task. | reset, timeout, object/scene variation | p. 7 (4. Experiments), p. 8 (4.3. Ablation Studies) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 3 (3.1. Localizing Coarse Target Region), p. 2 (1. Introduction) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 6 (3.4. Fine-Grained Action Prediction), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Real-world: success rate, translation/rotation error, 20 trials/task. | definition/direction/unit from same section | p. 7 (4. Experiments) |
| Table 1. Simulation results on RLBench. Success rates (%) with standard deviation. Best results in bold, second best underlined. | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Success rates (%) across 20 trials per task. | definition/direction/unit from same section | p. 7 (4.1. Simulation Results) |
| These results underscore that our differentiable rendering approach. | definition/direction/unit from same section | p. 8 (4.2. Real-World Deployment Results) |
| DiffRender-VLA maintains 73.6% average success under distribution shifts, degrading only 6.9% from indomain performance. | definition/direction/unit from same section | p. 8 (4.5. Generalization) |
| Figure 2. Overview of DiffRender-VLA. The framework bridges spatial and 2D VLA paradigms through differentiable rendering: localiz- ing anchors the next manipulation target, structuring ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Figure 3. Visualization of differentiable point cloud rendered image. We use RLbench [19] and RH20T [10] dataset for display. Precision task: Place the stamp ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Best Baseline +10.0 +10.0 +25.0 +20.0 +20.0 +20.0 +17.5 (b) Visibility improvements (a) Camera Pose Density Figure 7. | comparison identity and matched condition | p. 7 (4.1. Simulation Results) |
| This represents a +17.5% improvement over the best baseline (VLA-Adapter: 60.8%), validating real-world applicability. | comparison identity and matched condition | p. 7 (4.2. Real-World Deployment Results) |
| DiffRender-VLA substantially outperforms recent approaches: DP3 (33.3%, +45.0%), OpenVLA-OFT (58.5%, +19.8%), Pi0 (58.2%, +20.1%), and TraceVLA (43.3%, +35.0%). | comparison identity and matched condition | p. 8 (4.2. Real-World Deployment Results) |
| (3) Two-stage training: 76.2% (-4.3%)-without end-to-end gradient flow, stages cannot co-adapt. | comparison identity and matched condition | p. 8 (4.3. Ablation Studies) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 3. Component ablation. Trans./Rot. Error in cm/degrees. Variant Stack Blk Insert Peg Sort Shape | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| (3) Two-stage training: 76.2% (-4.3%)-without end-to-end gradient flow, stages cannot co-adapt. | component/input/data sensitivity | p. 8 (4.3. Ablation Studies) |
| Figure 2. Overview of DiffRender-VLA. The framework bridges spatial and 2D VLA paradigms through differentiable rendering: localiz- ing anchors the next manipulation target, structuring ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |
| We initialize from OpenVLA [22] (SigLIP [53] + DinoV2 [35], Llama-2-7B [42] backbone) pretrained on Open X-Embodiment [34] and RH20T [10]. | component/input/data sensitivity | p. 6 (4. Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our main contributions are as follows: • We propose DiffRender-VLA, a unified framework that bridges 3D spatial reasoning and 2D visual perception to transfer ... | Figure 8. Beam parameters improvement for small objects. deployment confirm that color-encoded spatial beams and world-aligned cube markers generalize beyond synthetic environments. DiffRender-VLA substantially ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (Figure/Table caption), p. 7 (4.1. Simulation Results), p. 7 (4.1. Simulation Results), p. 6 (Figure/Table caption), p. 8 (4.4. Parameter & Viewpoint Analysis), p. 1 (Figure/Table caption) |
| Primary metric/result | DiffRender-VLA significantly outperforms 2D visual prompting approaches: TraceVLA (63.9%, +16.6%) and VLA-adapter (60.6%, +19.9%). | numeric claim only at cited anchor | p. 7 (4.1. Simulation Results) |

- Numeric sentences retained from the body:
- **p. 6 / 4. Experiments - extractive PDF cue:** Each task runs 20 trials across varied poses and lighting.
- **p. 6 / 4. Experiments - extractive PDF cue:** Architecture: Our spatial reasoning module augments the VLA backbone with a voxel-based encoder: (1) Multiview RGB-D observations are fused into point clouds and voxelized into ...
- **p. 7 / 4. Experiments - extractive PDF cue:** Real-World Deployment Situation. lation heatmaps Qcoarse, world-aligned cube markers with adaptive sizing (ℓcube = 10-15cm, scaled to 0.8× object size for small targets); (3) We ...
- **p. 7 / 4. Experiments - extractive PDF cue:** Simulation: position error <2cm, rotation error <10°, 50 trials/task.
- **p. 7 / 4. Experiments - extractive PDF cue:** Real-world: success rate, translation/rotation error, 20 trials/task.
- **p. 7 / 4.1. Simulation Results - extractive PDF cue:** Success rates (%) across 20 trials per task.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | (3) Two-stage training: 76.2% (-4.3%)-without end-to-end gradient flow, stages cannot co-adapt. | p. 8 (4.3. Ablation Studies) |
| body limitation/failure cue | (1) Non-differentiable beams: 74.8% (-5.7%)-beams provide visual cues but cannot optimize placement. | p. 8 (4.3. Ablation Studies) |
| body limitation/failure cue | Figure 5. Simulation Tasks for Occlusion and Clutter enviroments. | p. 6 (Figure/Table caption) |
| body limitation/failure cue | Task-specific improvements highlight spatial understanding capabilities: Occlusion Tasks: Average 91.7% success (+7.6% over GWM). | p. 7 (4.1. Simulation Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Each task runs 20 trials across varied poses and lighting. | p. 6 (4. Experiments) |
| Architecture: Our spatial reasoning module augments the VLA backbone with a voxel-based encoder: (1) Multiview RGB-D observations are fused into point clouds and voxelized ... | p. 6 (4. Experiments) |
| Success rates (%) across 20 trials per task. | p. 7 (4.1. Simulation Results) |
| Real-world uses 50 demos/task with identical hyperparameters. | p. 7 (4. Experiments) |
| Beam parameters improvement for small objects. deployment confirm that color-encoded spatial beams and world-aligned cube markers generalize beyond synthetic environments. | p. 8 (4.2. Real-World Deployment Results) |
| As shown in Figure 6, Our method encodes spatial relationships through visual beams. providing more reliable spatial cues than implicit 3D representations or temporal ... | p. 8 (4.2. Real-World Deployment Results) |
| This alignment ensures rendered 2D projections encode spatial information through pure geometry: square 20814 | p. 3 (3.1. Localizing Coarse Target Region) |
| The highest confidence coarse location pcoarse ∈R3 is computed via a differentiable spatial expectation over Qcoarse. | p. 3 (3.1. Localizing Coarse Target Region) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 4.3. Ablation Studies - extractive PDF cue:** (3) Two-stage training: 76.2% (-4.3%)-without end-to-end gradient flow, stages cannot co-adapt.
- **p. 8 / 4.3. Ablation Studies - extractive PDF cue:** (1) Non-differentiable beams: 74.8% (-5.7%)-beams provide visual cues but cannot optimize placement.
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 5. Simulation Tasks for Occlusion and Clutter enviroments.
- **p. 7 / 4.1. Simulation Results - extractive PDF cue:** Task-specific improvements highlight spatial understanding capabilities: Occlusion Tasks: Average 91.7% success (+7.6% over GWM).

- **PDF anchors reviewed:** datasets p. 7 (4. Experiments), p. 7 (4. Experiments), p. 8 (4.3. Ablation Studies), p. 6 (4. Experiments), p. 6 (4. Experiments), p. 8 (4.2. Real-World Deployment Results), metrics p. 7 (4. Experiments), p. 6 (Figure/Table caption), p. 7 (4.1. Simulation Results), p. 8 (4.2. Real-World Deployment Results), p. 8 (4.5. Generalization), p. 3 (Figure/Table caption), baselines p. 7 (4.1. Simulation Results), p. 7 (4.2. Real-World Deployment Results), p. 8 (4.2. Real-World Deployment Results), p. 8 (4.3. Ablation Studies), results p. 8 (Figure/Table caption), p. 7 (4.1. Simulation Results), p. 7 (4.1. Simulation Results), p. 6 (Figure/Table caption), p. 8 (4.4. Parameter & Viewpoint Analysis), p. 1 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
