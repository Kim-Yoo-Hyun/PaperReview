# Evaluation - Object-centric 3D Motion Field for Robot Learning from Human Videos

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=kp9B9iQDIt; PDF retrieval source: https://arxiv.org/pdf/2506.04227. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (Figure/Table caption), p. 9 (5 Experiments), p. 9 (5 Experiments), p. 7 (Figure/Table caption), p. 8 (5 Experiments), p. 7 (Figure/Table caption)): Figure 8: (Left) SE3 motion estimation performance in real world. Our method achieves lower error compared to baseline. (Middle) Intrinsics Map Ablation Studies. Both inverse focal length and coordinate map ...

## Evaluation Body Digest

- **p. 8 / 5 Experiments - extractive PDF cue:** We use an XArm7 robot arm with a parallel-jaw gripper for the test dataset collection and robot experiments.
- **p. 8 / 5 Experiments - extractive PDF cue:** This task is considered successful if the robot can finish the tracking trajectory with spotlight focusing on the cable in the process.
- **p. 9 / 5 Experiments - extractive PDF cue:** In this task, the robot is required to pick, rotate, and insert an item into a slot (hole).
- **p. 9 / 5 Experiments - extractive PDF cue:** Finally, we find it important to apply object masking augmentation during training, as the object's silhouette under the robot gripper differs from that under a ...
- **p. 7 / 5 Experiments - extractive PDF cue:** System Setup We use a widely-used Intel D435 RGBD camera at 640 × 480 resolution for video dataset collection at 30Hz (Figure 6).
- **p. 8 / 5 Experiments - extractive PDF cue:** Focal Len Ours (Full) 0.0 0.5 1.0 1.5 2.0 2.5 ×10 6 3D Motion Field Error ( ) Motion (train) Motion (sim-test) Depth (train) Depth ...
- **p. 8 / 5 Experiments - extractive PDF cue:** (Right) Real world Task Success Rate (3 seeds).
- **p. 9 / 5 Experiments - extractive PDF cue:** Main Results We show the success rate of different methods in Figure 8 Right.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** multi-robot demonstration/dataset ecosystem.
- **Input boundary:** multi-view observation, language/task label과 action trajectory.
- **Output/decision under evaluation:** dataset sample 또는 learned policy action.
- **Primary target:** coverage, cross-embodiment transfer, data efficiency와 task success.
- **Detected evaluation headings:** 5 Experiments (p. 7); B Further Details on the Simulation Dataset (p. 14); C Further Details on Real World Experiments (p. 15).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 8: (Left) SE3 motion estimation performance in real world. Our method achieves lower error compared to baseline. (Middle) Intrinsics Map Ablation Studies. Both ... | p. 8 (Figure/Table caption) |
| 5 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Main Results We show the success rate of different methods in Figure 8 Right. | p. 9 (5 Experiments) |
| 5 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | We find that our method significantly outperformed the other evaluated methods. | p. 9 (5 Experiments) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 7: A rollout of fine-grained insertion. Our method can achieve high precision, even if we are observing the motion from 40cm away without ... | p. 7 (Figure/Table caption) |
| 5 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | We introduce the following tasks to benchmark the performance: 1. | p. 8 (5 Experiments) |

## Dataset / Benchmark Role

- **p. 8 / 5 Experiments - extractive PDF cue:** We use an XArm7 robot arm with a parallel-jaw gripper for the test dataset collection and robot experiments.
- **p. 8 / 5 Experiments - extractive PDF cue:** This task is considered successful if the robot can finish the tracking trajectory with spotlight focusing on the cable in the process.
- **p. 9 / 5 Experiments - extractive PDF cue:** In this task, the robot is required to pick, rotate, and insert an item into a slot (hole).
- **p. 9 / 5 Experiments - extractive PDF cue:** Finally, we find it important to apply object masking augmentation during training, as the object's silhouette under the robot gripper differs from that under a ...
- **p. 7 / 5 Experiments - extractive PDF cue:** System Setup We use a widely-used Intel D435 RGBD camera at 640 × 480 resolution for video dataset collection at 30Hz (Figure 6).

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1: We propose a novel framework for robot learning from human demonstration videos without relying on any robot-collected data. Our approach learns to control ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2: Overview of proposed learning framework. We first pretrain a 3D motion field estimator in simulation (Phase I) and use it to estimate the ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3: (Left) Phase I Synthetic Data Generation. We randomly generate object and 3D motions, and use ray casting and projection to obtain 3D pixel ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4: Model Architecture. The most important design is a dense intrinsics map feature concate- nated to the input, which contains key information for reconstructing ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 5: Guess what is there? Object tracks can be used to recover missing or wrong depth values. Discussion I: Motion and Geometry Synergy A ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 6: (Left) Experimental Setup. (Right) Qualitative Results on "Pen" (Left Figure). Our method produces smoother motion field and depth compared to baseline. This is ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 7: A rollout of fine-grained insertion. Our method can achieve high precision, even if we are observing the motion from 40cm away without a ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 8: (Left) SE3 motion estimation performance in real world. Our method achieves lower error compared to baseline. (Middle) Intrinsics Map Ablation Studies. Both inverse ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We use an XArm7 robot arm with a parallel-jaw gripper for the test dataset collection and robot experiments. | embodiment, simulator version and control stack | p. 8 (5 Experiments), p. 8 (5 Experiments) |
| Task/environment | This task is considered successful if the robot can finish the tracking trajectory with spotlight focusing on the cable in the process. | reset, timeout, object/scene variation | p. 8 (5 Experiments), p. 9 (5 Experiments) |
| Observation/sensor | multi-view observation, language/task label과 action trajectory | calibration, preprocessing, privileged input | p. 5 (2 Preliminaries), p. 2 (1 Introduction) |
| Output/decision | dataset sample 또는 learned policy action | action frame, controller and termination | p. 3 (2 Preliminaries), p. 5 (2 Preliminaries) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Focal Len Ours (Full) 0.0 0.5 1.0 1.5 2.0 2.5 ×10 6 3D Motion Field Error ( ) Motion (train) Motion (sim-test) Depth (train) ... | definition/direction/unit from same section | p. 8 (5 Experiments) |
| (Right) Real world Task Success Rate (3 seeds). | definition/direction/unit from same section | p. 8 (5 Experiments) |
| Main Results We show the success rate of different methods in Figure 8 Right. | definition/direction/unit from same section | p. 9 (5 Experiments) |
| We attribute its success to accurate and smooth motion estimation. | definition/direction/unit from same section | p. 9 (5 Experiments) |
| In this section, we demonstrate the effectiveness of our 3D motion field estimator and our control policy through real world experiments. | definition/direction/unit from same section | p. 7 (5 Experiments) |
| Figure 4: Model Architecture. The most important design is a dense intrinsics map feature concate- nated to the input, which contains key information for ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Figure 7: A rollout of fine-grained insertion. Our method can achieve high precision, even if we are observing the motion from 40cm away without ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 2: Overview of proposed learning framework. We first pretrain a 3D motion field estimator in simulation (Phase I) and use it to estimate ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our method achieves lower error compared to baseline. | comparison identity and matched condition | p. 8 (5 Experiments) |
| We find that our approach has significantly lower error compared to the baseline. | comparison identity and matched condition | p. 8 (5 Experiments) |
| Figure 6: (Left) Experimental Setup. (Right) Qualitative Results on "Pen" (Left Figure). Our method produces smoother motion field and depth compared to baseline. This ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| We find that our method significantly outperformed the other evaluated methods. | comparison identity and matched condition | p. 9 (5 Experiments) |
| During the deployment, the baseline method will quickly deviate from the correct moving direction/trajectory. | comparison identity and matched condition | p. 9 (5 Experiments) |
| Figure 1: We propose a novel framework for robot learning from human demonstration videos without relying on any robot-collected data. Our approach learns to ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| (Middle) Intrinsics Map Ablation Studies. | component/input/data sensitivity | p. 8 (5 Experiments) |
| 5.0% Full 35.0% Ablation Studies We also study the design choices of our policy architecture and training. | component/input/data sensitivity | p. 9 (5 Experiments) |
| Figure 1: We propose a novel framework for robot learning from human demonstration videos without relying on any robot-collected data. Our approach learns to ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |
| Figure 7: A rollout of fine-grained insertion. Our method can achieve high precision, even if we are observing the motion from 40cm away without ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Table 1: Policy Learning Ablation for Fine-grained Tasks. Setting Success w/o Diffusion (Diff.) 0.0% w/o Diff. Masking. 0.0% | component/input/data sensitivity | p. 9 (Figure/Table caption) |
| Figure 2: Overview of proposed learning framework. We first pretrain a 3D motion field estimator in simulation (Phase I) and use it to estimate ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We present a simple and novel architecture that can learn to see and predict object-centric 3D motion field in the real world for control. | Figure 8: (Left) SE3 motion estimation performance in real world. Our method achieves lower error compared to baseline. (Middle) Intrinsics Map Ablation Studies. Both ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (Figure/Table caption), p. 9 (5 Experiments), p. 9 (5 Experiments), p. 7 (Figure/Table caption), p. 8 (5 Experiments), p. 7 (Figure/Table caption) |
| Primary metric/result | Main Results We show the success rate of different methods in Figure 8 Right. | numeric claim only at cited anchor | p. 9 (5 Experiments) |

- Numeric sentences retained from the body:
- **p. 7 / 5 Experiments - extractive PDF cue:** System Setup We use a widely-used Intel D435 RGBD camera at 640 × 480 resolution for video dataset collection at 30Hz (Figure 6).
- **p. 8 / 5 Experiments - extractive PDF cue:** Focal Len Ours (Full) 0.0 0.5 1.0 1.5 2.0 2.5 ×10 6 3D Motion Field Error ( ) Motion (train) Motion (sim-test) Depth (train) Depth ...
- **p. 8 / 5 Experiments - extractive PDF cue:** (Right) Real world Task Success Rate (3 seeds).
- **p. 8 / 5 Experiments - extractive PDF cue:** Surprisingly, the focal length value plays a critical role in motion prediction even for a relatively small FoV variation around 10 degrees.
- **p. 8 / 5 Experiments - extractive PDF cue:** 5.2 Robot Learning from Videos Real world Tasks In this section, we test if our method can acquire object manipulation skills from human videos.
- **p. 4 / 2 Preliminaries - extractive PDF cue:** The problem is that ∆xp might be noisy in practice and it can lead to huge estimation error in ∆Z due to the large slope ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Other recent methods fail on our setup due to their limitations (Table 2). to 256 × 256. | p. 8 (5 Experiments) |
| body limitation/failure cue | Our method is free from many limitations of existing works. | p. 9 (5 Experiments) |
| body limitation/failure cue | While these approaches offer certain advantages, each has notable limitations, as previously discussed. | p. 9 (5 Experiments) |
| body limitation/failure cue | Adversarial Robustness We test robustness further through adversarial attack in real world experiments by injecting Gaussian noise of different intensities into the depth observation ... | p. 8 (5 Experiments) |
| body limitation/failure cue | Table 3: Data Noise Simulation. We highlight several key randomization strategies. Type Setup Depth White Noise Gaussian, σ = Log-Uniform [0.01, 1]× 0.2mm Depth ... | p. 14 (Figure/Table caption) |
| body limitation/failure cue | Figure 14: Motion Field Comparison (1.5/2.5cm-wide pen motion): Our method produces a smoother motion field than the direct method, which exhibits noticeable noise. 18 | p. 18 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| (Right) Real world Task Success Rate (3 seeds). | p. 8 (5 Experiments) |
| Adversarial Robustness We test robustness further through adversarial attack in real world experiments by injecting Gaussian noise of different intensities into the depth observation ... | p. 8 (5 Experiments) |
| During the evaluation, we ensure that the grasping and the object segmentation is correct for each of the evaluated method (otherwise we restart that ... | p. 9 (5 Experiments) |
| Deployment In the inference time, we need to convert the predicted 3D motion field F to the robot action. | p. 7 (2 Preliminaries) |
| We introduce two novel components in its implementation. | p. 1 (Abstract) |
| Therefore in the long run, besides object motion, we also need to consider extracting contact (semantical affordance). | p. 3 (2 Preliminaries) |
| The discussion below assumes the depth observation of two consecutive images I0 and I1, and a dense pixel correspondence computed by a video tracker. | p. 4 (2 Preliminaries) |
| Given the camera intrinsics and the 3D flow, we can reconstruct the position of every pixel in the 3D space, so this representation fully ... | p. 4 (2 Preliminaries) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5 Experiments - extractive PDF cue:** Other recent methods fail on our setup due to their limitations (Table 2). to 256 × 256.
- **p. 9 / 5 Experiments - extractive PDF cue:** Our method is free from many limitations of existing works.
- **p. 9 / 5 Experiments - extractive PDF cue:** While these approaches offer certain advantages, each has notable limitations, as previously discussed.
- **p. 8 / 5 Experiments - extractive PDF cue:** Adversarial Robustness We test robustness further through adversarial attack in real world experiments by injecting Gaussian noise of different intensities into the depth observation (which ...
- **p. 14 / Figure/Table caption - extractive PDF cue:** Table 3: Data Noise Simulation. We highlight several key randomization strategies. Type Setup Depth White Noise Gaussian, σ = Log-Uniform [0.01, 1]× 0.2mm Depth Correlated ...
- **p. 18 / Figure/Table caption - extractive PDF cue:** Figure 14: Motion Field Comparison (1.5/2.5cm-wide pen motion): Our method produces a smoother motion field than the direct method, which exhibits noticeable noise. 18

- **PDF anchors reviewed:** datasets p. 8 (5 Experiments), p. 8 (5 Experiments), p. 9 (5 Experiments), p. 9 (5 Experiments), p. 7 (5 Experiments), metrics p. 8 (5 Experiments), p. 8 (5 Experiments), p. 9 (5 Experiments), p. 9 (5 Experiments), p. 7 (5 Experiments), p. 5 (Figure/Table caption), baselines p. 8 (5 Experiments), p. 8 (5 Experiments), p. 7 (Figure/Table caption), p. 9 (5 Experiments), p. 9 (5 Experiments), p. 1 (Figure/Table caption), results p. 8 (Figure/Table caption), p. 9 (5 Experiments), p. 9 (5 Experiments), p. 7 (Figure/Table caption), p. 8 (5 Experiments), p. 7 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
