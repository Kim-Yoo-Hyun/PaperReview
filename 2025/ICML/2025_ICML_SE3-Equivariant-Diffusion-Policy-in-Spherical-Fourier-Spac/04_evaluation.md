# Evaluation - SE(3)-Equivariant Diffusion Policy in Spherical Fourier Space

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=U5nRMOs8Ed; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/167962. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (5.1. Simulation Experiments), p. 9 (Figure/Table caption), p. 6 (5.1. Simulation Experiments), p. 7 (Figure/Table caption), p. 8 (5.2. Physical Experiments), p. 9 (Figure/Table caption)): Notably, as the tilting range increases, SDP achieves a more significant relative performance improvement over the baselines.

## Evaluation Body Digest

- **p. 6 / 5.1. Simulation Experiments - extractive body cue:** To evaluate robustness, we modify four MimicGen tasks with SE(3) initialization by randomly tilting the table within a defined range and randomly placing objects on ...
- **p. 7 / 5.2. Physical Experiments - extractive body cue:** Training Dataset from Human Demonstrations We use Gello (Wu et al., 2023) to collect demonstrations with objects initialized in random SE(3) poses.
- **p. 6 / 5.1. Simulation Experiments - extractive body cue:** Experimental Settings We conduct simulation experiments using the MimicGen (Mandlekar et al., 2023) environment, built on the Mujoco simulator (Todorov et al., 2012), which features ...
- **p. 7 / 5.2. Physical Experiments - extractive body cue:** Five physical robotic manipulation tasks.
- **p. 8 / 5.2. Physical Experiments - extractive body cue:** Success rate (%) of 5 physical experiments over 20 evaluation episodes.
- **p. 8 / 5.2. Physical Experiments - extractive body cue:** The action space and number of training demonstrations are listed under each task.
- **p. 6 / 5.1. Simulation Experiments - extractive body cue:** We report the maximum test success rate throughout training, averaging results over 50 rollouts for each of the three seeds.
- **p. 7 / 5.2. Physical Experiments - extractive body cue:** Evaluation success rate on 12 MimicGen tasks with SE(2) initialization.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 5. Experiments (p. 6); 5.1. Simulation Experiments (p. 6); 5.2. Physical Experiments (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5.1. Simulation Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Notably, as the tilting range increases, SDP achieves a more significant relative performance improvement over the baselines. | p. 6 (5.1. Simulation Experiments) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 6. Impact of training dataset size on task success rates: in- creasing the number of demonstrations from 100 to 316 (a 3× increase) ... | p. 9 (Figure/Table caption) |
| 5.1. Simulation Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | We report the maximum test success rate throughout training, averaging results over 50 rollouts for each of the three seeds. | p. 6 (5.1. Simulation Experiments) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 2. Evaluation success rate on 12 MimicGen tasks with SE(2) initialization. We train all the baselines with 100 demonstrations. SDP demonstrates the best ... | p. 7 (Figure/Table caption) |
| 5.2. Physical Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Success rate (%) of 5 physical experiments over 20 evaluation episodes. | p. 8 (5.2. Physical Experiments) |

## Dataset / Benchmark Role

- **p. 6 / 5.1. Simulation Experiments - extractive body cue:** To evaluate robustness, we modify four MimicGen tasks with SE(3) initialization by randomly tilting the table within a defined range and randomly placing objects on ...
- **p. 7 / 5.2. Physical Experiments - extractive body cue:** Training Dataset from Human Demonstrations We use Gello (Wu et al., 2023) to collect demonstrations with objects initialized in random SE(3) poses.
- **p. 6 / 5.1. Simulation Experiments - extractive body cue:** Experimental Settings We conduct simulation experiments using the MimicGen (Mandlekar et al., 2023) environment, built on the Mujoco simulator (Todorov et al., 2012), which features ...
- **p. 7 / 5.2. Physical Experiments - extractive body cue:** Five physical robotic manipulation tasks.
- **p. 8 / 5.2. Physical Experiments - extractive body cue:** Success rate (%) of 5 physical experiments over 20 evaluation episodes.
- **p. 8 / 5.2. Physical Experiments - extractive body cue:** The action space and number of training demonstrations are listed under each task.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. SDP enforces that the policy is SO(3) equivariant. Specifically, in the second row, an SO(3) rotation that is applied to the scene leads ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Method overview. During inference, SDP first embeds state St into a spherical scene feature Ct by the encoder enc. Then, SDTU ϵθ estimates ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Spherical denoising temporal U-net (SDTU). Left: The SDTU ϵθ estimates the noise ϵ, based on the noisy actions Ak t , denoising step ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. MimicGen tasks with SE(3) initialization ((a)-(c), showing 1 of 4 tasks) and SE(2) initialization ((d)-(f), showing 3 of 12 tasks).
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Evaluation success rate on 4 MimicGen tasks with 3 levels of SE(3) initialization. We train all the baselines on progressively tilted environments with ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Evaluation success rate on 12 MimicGen tasks with SE(2) initialization. We train all the baselines with 100 demonstrations. SDP demonstrates the best performance ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. Five physical robotic manipulation tasks. Push Eraser we also tested 2048 points). The actions are the 6 DoF gripper poses for single-arm tasks ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Success rate (%) of 5 physical experiments over 20 evalu- ation episodes. The action space and number of training demon- strations are listed ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | To evaluate robustness, we modify four MimicGen tasks with SE(3) initialization by randomly tilting the table within a defined range and randomly placing objects ... | embodiment, simulator version and control stack | p. 6 (5.1. Simulation Experiments), p. 7 (5.2. Physical Experiments) |
| Task/environment | Training Dataset from Human Demonstrations We use Gello (Wu et al., 2023) to collect demonstrations with objects initialized in random SE(3) poses. | reset, timeout, object/scene variation | p. 7 (5.2. Physical Experiments), p. 6 (5.1. Simulation Experiments) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 4 (4.2. Representing State and Action by Spherical Signal), p. 4 (4.1. Method Overview) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 2 (2. Background), p. 2 (2. Background) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We report the maximum test success rate throughout training, averaging results over 50 rollouts for each of the three seeds. | definition/direction/unit from same section | p. 6 (5.1. Simulation Experiments) |
| Evaluation success rate on 12 MimicGen tasks with SE(2) initialization. | definition/direction/unit from same section | p. 7 (5.2. Physical Experiments) |
| Success rate (%) of 5 physical experiments over 20 evaluation episodes. | definition/direction/unit from same section | p. 8 (5.2. Physical Experiments) |
| Table 5. Success rate VS degree l of the spherical Fourier feature. Results from one seed. Degree l Coffee 15◦ Thr. Pc. As. 15◦ ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Figure 6. Impact of training dataset size on task success rates: in- creasing the number of demonstrations from 100 to 316 (a 3× increase) ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Despite the variations in SE(2), SDP still demonstrates a notable advantage, suggesting that its continuous SE(2) equivariance benefits learning more effectively than the discrete ... | definition/direction/unit from same section | p. 6 (5.1. Simulation Experiments) |
| SDP demonstrates the best performance on 10 tasks. | definition/direction/unit from same section | p. 7 (5.2. Physical Experiments) |
| Figure 1. SDP enforces that the policy is SO(3) equivariant. Specifically, in the second row, an SO(3) rotation that is applied to the scene ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Results on Tasks with SE(2) Initialization Table 2 shows that SDP outperforms all baselines across 10 tasks, except for Coffee and Coffee Preparation. | comparison identity and matched condition | p. 6 (5.1. Simulation Experiments) |
| Additionally, we also compare various baselines across all 12 original MimicGen tasks. | comparison identity and matched condition | p. 6 (5.1. Simulation Experiments) |
| We train all the baselines with 100 demonstrations. | comparison identity and matched condition | p. 7 (5.2. Physical Experiments) |
| As the degress of SE(3) initialization increases, SDP maintains reasonable performance while the performance of other baselines drop severely. | comparison identity and matched condition | p. 7 (5.2. Physical Experiments) |
| Table 4. Ablation study. The relative action space and the spherical representation are critical for the SE(3) generalization, while the latter one is more ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Table 6. Comparison of inference time. At the costs of 5× solver than DiffPo, SDP achieves continuous SE(3) equivariance and does not need preprocessing. ... | comparison identity and matched condition | p. 9 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 3) EquiBot (Yang et al., 2024a) - an SO(3)-equivariant diffusion policy with up to degree l = 1 representations. | component/input/data sensitivity | p. 6 (5.1. Simulation Experiments) |
| We compare several baselines in our experiments: 1) EquiDiff (Wang et al., 2024b) - an SO(2)-equivariant diffusion policy using either voxel or RGB image ... | component/input/data sensitivity | p. 6 (5.1. Simulation Experiments) |
| Figure 1. SDP enforces that the policy is SO(3) equivariant. Specifically, in the second row, an SO(3) rotation that is applied to the scene ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |
| Figure 3. Spherical denoising temporal U-net (SDTU). Left: The SDTU ϵθ estimates the noise ϵ, based on the noisy actions Ak t , denoising ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |
| Table 4. Ablation study. The relative action space and the spherical representation are critical for the SE(3) generalization, while the latter one is more ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The contributions of this work are: 1. a novel method, Spherical Diffusion Policy, which is equivariant to 3D rotations and invariant to 3D translations ... | Notably, as the tilting range increases, SDP achieves a more significant relative performance improvement over the baselines. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (5.1. Simulation Experiments), p. 9 (Figure/Table caption), p. 6 (5.1. Simulation Experiments), p. 7 (Figure/Table caption), p. 8 (5.2. Physical Experiments), p. 9 (Figure/Table caption) |
| Primary metric/result | Figure 6. Impact of training dataset size on task success rates: in- creasing the number of demonstrations from 100 to 316 (a 3× increase) ... | numeric claim only at cited anchor | p. 9 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 6 / 5.1. Simulation Experiments - extractive body cue:** The RGB images have a resolution of 84 × 84 × 3, while RGBD data can be used to reconstruct either 3D colored voxels (843) ...
- **p. 6 / 5.1. Simulation Experiments - extractive body cue:** We report the maximum test success rate throughout training, averaging results over 50 rollouts for each of the three seeds.
- **p. 6 / 5.1. Simulation Experiments - extractive body cue:** Results on Tasks with SE(2) Initialization Table 2 shows that SDP outperforms all baselines across 10 tasks, except for Coffee and Coffee Preparation.
- **p. 6 / 5.2. Physical Experiments - extractive body cue:** Point clouds with 1024 points are reconstructed from the RGBD images (for 6
- **p. 7 / 5.2. Physical Experiments - extractive body cue:** MimicGen tasks with SE(3) initialization ((a)-(c), showing 1 of 4 tasks) and SE(2) initialization ((d)-(f), showing 3 of 12 tasks).
- **p. 7 / 5.2. Physical Experiments - extractive body cue:** SDP demonstrates the best performance on 10 tasks.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | One limitation of the proposed method is that it operates in position control, ignoring contact forces, which leads to protective stops in the Flip ... | p. 9 (6. Conclusion and Limitations) |
| body limitation/failure cue | Another limitation is the lowresolution point cloud processing in the observation encoder, which struggles to capture fine details, such as these in the Push ... | p. 9 (6. Conclusion and Limitations) |
| body limitation/failure cue | Figure 2. Method overview. During inference, SDP first embeds state St into a spherical scene feature Ct by the encoder enc. Then, SDTU ϵθ ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | Figure 3. Spherical denoising temporal U-net (SDTU). Left: The SDTU ϵθ estimates the noise ϵ, based on the noisy actions Ak t , denoising ... | p. 5 (Figure/Table caption) |
| body limitation/failure cue | The observations are captured by two stationary RGBD cameras positioned above the workspace to minimize occlusion. | p. 6 (5.2. Physical Experiments) |
| body limitation/failure cue | We hypothesize that this drop is caused by pointcloud occlusion and object instability due to gravity, both of which disrupt SE(3) equivariance. | p. 6 (5.1. Simulation Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| A relevant baseline, ET-SEED (Tie et al., 2024), is not included because the code was unavailable before the initial submission. | p. 6 (5.1. Simulation Experiments) |
| For details on hyperparameters, see Appendix D. | p. 6 (5.1. Simulation Experiments) |
| Results from one seed. * using point clouds with 2048 points. | p. 8 (5.2. Physical Experiments) |
| First, the truncated spherical Fourier coefficients provide a compact approximation of spherical features and are compatible with SO(3) rotations, rather than computationally heavy SO(3) ... | p. 4 (4.2. Representing State and Action by Spherical Signal) |
| We model ϵθ using three components as shown in Figure 2: i) the spherical encoder embeds the state into a multichannel spherical scene feature ... | p. 4 (4.1. Method Overview) |
| The vector C encodes the state in spherical Fourier space up to degree L. | p. 5 (4.3. Spherical Denoising Temporal U-net) |
| The robot state e is concatenated to the output of the encoder yielding C. | p. 5 (4.2. Representing State and Action by Spherical Signal) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 6. Conclusion and Limitations - extractive body cue:** One limitation of the proposed method is that it operates in position control, ignoring contact forces, which leads to protective stops in the Flip Book ...
- **p. 9 / 6. Conclusion and Limitations - extractive body cue:** Another limitation is the lowresolution point cloud processing in the observation encoder, which struggles to capture fine details, such as these in the Push Eraser ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Method overview. During inference, SDP first embeds state St into a spherical scene feature Ct by the encoder enc. Then, SDTU ϵθ estimates ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Spherical denoising temporal U-net (SDTU). Left: The SDTU ϵθ estimates the noise ϵ, based on the noisy actions Ak t , denoising step ...
- **p. 6 / 5.2. Physical Experiments - extractive body cue:** The observations are captured by two stationary RGBD cameras positioned above the workspace to minimize occlusion.
- **p. 6 / 5.1. Simulation Experiments - extractive body cue:** We hypothesize that this drop is caused by pointcloud occlusion and object instability due to gravity, both of which disrupt SE(3) equivariance.

- **Evidence anchors reviewed:** datasets p. 6 (5.1. Simulation Experiments), p. 7 (5.2. Physical Experiments), p. 6 (5.1. Simulation Experiments), p. 7 (5.2. Physical Experiments), p. 8 (5.2. Physical Experiments), p. 8 (5.2. Physical Experiments), metrics p. 6 (5.1. Simulation Experiments), p. 7 (5.2. Physical Experiments), p. 8 (5.2. Physical Experiments), p. 9 (Figure/Table caption), p. 9 (Figure/Table caption), p. 6 (5.1. Simulation Experiments), baselines p. 6 (5.1. Simulation Experiments), p. 6 (5.1. Simulation Experiments), p. 7 (5.2. Physical Experiments), p. 7 (5.2. Physical Experiments), p. 8 (Figure/Table caption), p. 9 (Figure/Table caption), results p. 6 (5.1. Simulation Experiments), p. 9 (Figure/Table caption), p. 6 (5.1. Simulation Experiments), p. 7 (Figure/Table caption), p. 8 (5.2. Physical Experiments), p. 9 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
