# Evaluation - ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (30 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v270/huang25g.html; PDF retrieval source: https://raw.githubusercontent.com/mlresearch/v270/main/assets/huang25g/huang25g.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 27 (A.12 Simulation Experiments), p. 8 (Figure/Table caption), p. 22 (A.5 Implementation Details of Keypoint Proposal)): Folding 0/10 4/10 7/10 Total (%) 10.0% 44.3% 68.6% Table 1: Success rate on wheeled singlearm and stationary bimanual platforms.

## Evaluation Body Digest

- **p. 8 / 4 Experiments - extractive body cue:** 5 Conclusion & Limitations In this work, we presented Relational Keypoint Constraints (ReKep), a structural task representation using constraints that operates on semantic keypoints to ...
- **p. 8 / 4 Experiments - extractive body cue:** Results are shown on two robot platforms and on a variety of tasks featuring multi-stage, in-the-wild, bimanual, and reactive behaviors, all without task-specific data, additional ...
- **p. 7 / 4 Experiments - extractive body cue:** For example, it can formulate correct temporal dependency in multi-stage tasks (e.g., spout needs to be aligned with the cup before pouring), leverage commonsense knowledge ...
- **p. 7 / 4 Experiments - extractive body cue:** We validate ReKep on two real robot platforms: a wheeled single-arm platform, and a stationary dual-arm platform (Figure.
- **p. 25 / A.8 Implementation Details of Sub-Goal Solver - extractive body cue:** depth maps from all available cameras and excludes robot arms using cuRobo and any grasped rigid objects (tracked via a masked tracker model Cutie [136]).
- **p. 26 / A.9 Implementation Details of Path Solver - extractive body cue:** For example, in the "pouring tea" task, the robot can only start tilting the teapot when the teapot spout is aligned with the cup opening.
- **p. 27 / A.12 Simulation Experiments - extractive body cue:** Seen Poses Unseen Poses Unseen Objects Monolithic Policy 0.93 0.31 0.14 ReKep (Zero-Shot) 0.75 0.68 0.72
- **p. 27 / A.12 Simulation Experiments - extractive body cue:** The baseline is trained via imitation learning on 100 expert demonstrations, where demonstrations are from scripted policies using privileged simulation information.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4 Experiments (p. 6); A.4 Evaluation Details (p. 20); A.5 Implementation Details of Keypoint Proposal (p. 22); A.7 Implementation Details of Point Tracker (p. 24); A.8 Implementation Details of Sub-Goal Solver (p. 24); A.9 Implementation Details of Path Solver (p. 25); A.12 Simulation Experiments (p. 27).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Folding 0/10 4/10 7/10 Total (%) 10.0% 44.3% 68.6% Table 1: Success rate on wheeled singlearm and stationary bimanual platforms. | p. 7 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Folding 0/10 3/10 5/10 Total (%) 6.7% 26.7% 46.7% Table 2: Success rate under external disturbances across both robot platforms. | p. 7 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Garment ReKep sweater shirt hoodie vest dress pants shorts scarf sweater shirt hoodie vest dress pants shorts scarf Total Strategy Success 6/10 4/10 4/10 ... | p. 8 (4 Experiments) |
| A.12 Simulation Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Success rates are averaged across 100 trials and reported below. | p. 27 (A.12 Simulation Experiments) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 5: Novel bimanual strategies of ReKep for folding different categories of garments and their success rates. Since ReKep in this task always associates ... | p. 8 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 8 / 4 Experiments - extractive body cue:** 5 Conclusion & Limitations In this work, we presented Relational Keypoint Constraints (ReKep), a structural task representation using constraints that operates on semantic keypoints to ...
- **p. 8 / 4 Experiments - extractive body cue:** Results are shown on two robot platforms and on a variety of tasks featuring multi-stage, in-the-wild, bimanual, and reactive behaviors, all without task-specific data, additional ...
- **p. 7 / 4 Experiments - extractive body cue:** For example, it can formulate correct temporal dependency in multi-stage tasks (e.g., spout needs to be aligned with the cup before pouring), leverage commonsense knowledge ...
- **p. 7 / 4 Experiments - extractive body cue:** We validate ReKep on two real robot platforms: a wheeled single-arm platform, and a stationary dual-arm platform (Figure.
- **p. 25 / A.8 Implementation Details of Sub-Goal Solver - extractive body cue:** depth maps from all available cameras and excludes robot arms using cuRobo and any grasped rigid objects (tracked via a masked tracker model Cutie [136]).
- **p. 26 / A.9 Implementation Details of Path Solver - extractive body cue:** For example, in the "pouring tea" task, the robot can only start tilting the teapot when the teapot spout is aligned with the cup opening.
- **p. 27 / A.12 Simulation Experiments - extractive body cue:** Seen Poses Unseen Poses Unseen Objects Monolithic Policy 0.93 0.31 0.14 ReKep (Zero-Shot) 0.75 0.68 0.72
- **p. 27 / A.12 Simulation Experiments - extractive body cue:** The baseline is trained via imitation learning on 100 expert demonstrations, where demonstrations are from scripted policies using privileged simulation information.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Relational Keypoint Constraints (ReKep) specify diverse manipulation behaviors as an opti- mizable spatio-temporal series of constraint functions operating on semantic keypoints. In the ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Overview of ReKep. DINOv2 [5] first proposes keypoints in the scene, which are overlaid on the original RGB image. The image and an ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: Experiment tasks and visualization of optimization results. Seven tasks are designed to validate different aspects of our system, including in-the-wild specification with commonsense ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Success rate on wheeled single- arm and stationary bimanual platforms. ReKep Task (Dist.) VoxPoser Auto Annot. Pour Tea 0/10 2/10
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Success rate under external dis- turbances across both robot platforms.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: System error breakdown. Tasks. We purposefully select a set of tasks (shown in Fig. 3) with the goal of examining the multi-stage (m), ...
- **p. 7 / Figure/Table caption - extractive body cue:** Tab. 1. We compare to VoxPoser [106] as a baseline. We evaluate two variants of the system: "Auto" uses foundation models to automatically generate ReKep, ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Novel bimanual strategies of ReKep for folding different categories of garments and their success rates. Since ReKep in this task always associates two ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 5 Conclusion & Limitations In this work, we presented Relational Keypoint Constraints (ReKep), a structural task representation using constraints that operates on semantic keypoints ... | embodiment, simulator version and control stack | p. 8 (4 Experiments), p. 8 (4 Experiments) |
| Task/environment | Results are shown on two robot platforms and on a variety of tasks featuring multi-stage, in-the-wild, bimanual, and reactive behaviors, all without task-specific data, ... | reset, timeout, object/scene variation | p. 8 (4 Experiments), p. 7 (4 Experiments) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 3 (3 Method) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 4 (3 Method), p. 22 (A.6 Querying Vision-Language Model) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Folding 0/10 4/10 7/10 Total (%) 10.0% 44.3% 68.6% Table 1: Success rate on wheeled singlearm and stationary bimanual platforms. | definition/direction/unit from same section | p. 7 (4 Experiments) |
| Folding 0/10 3/10 5/10 Total (%) 6.7% 26.7% 46.7% Table 2: Success rate under external disturbances across both robot platforms. | definition/direction/unit from same section | p. 7 (4 Experiments) |
| Garment ReKep sweater shirt hoodie vest dress pants shorts scarf sweater shirt hoodie vest dress pants shorts scarf Total Strategy Success 6/10 4/10 4/10 ... | definition/direction/unit from same section | p. 8 (4 Experiments) |
| Success rates are averaged across 100 trials and reported below. | definition/direction/unit from same section | p. 27 (A.12 Simulation Experiments) |
| Figure 5: Novel bimanual strategies of ReKep for folding different categories of garments and their success rates. Since ReKep in this task always associates ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Scene Collision Avoidance: We use nvblox [149] with the PyTorch wrapper [58] to compute the ESDF of the scene in a separate node that ... | definition/direction/unit from same section | p. 24 (A.8 Implementation Details of Sub-Goal Solver) |
| (Dual-Arm only) Self-Collision Avoidance: To avoid two arms collide with each other, we compute the pairwise distance between the two point sets, each including ... | definition/direction/unit from same section | p. 25 (A.8 Implementation Details of Sub-Goal Solver) |
| Figure 2: Overview of ReKep. DINOv2 [5] first proposes keypoints in the scene, which are overlaid on the original RGB image. The image and ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Compared to baselines, ReKep can effectively handle core challenges of each task. | comparison identity and matched condition | p. 7 (4 Experiments) |
| It is compared to a monolithic learning-based baseline based on the transformer architecture [154] adopted from RVT [155, 156]. | comparison identity and matched condition | p. 27 (A.12 Simulation Experiments) |
| We compare to VoxPoser [106] as a baseline. | comparison identity and matched condition | p. 7 (4 Experiments) |
| Other modules, such as segmentation, 3D reconstruction, and low-level controller, also contribute to some failure cases, but they are relatively insignificant compared to other ... | comparison identity and matched condition | p. 8 (4 Experiments) |
| The baseline is trained via imitation learning on 100 expert demonstrations, where demonstrations are from scripted policies using privileged simulation information. | comparison identity and matched condition | p. 27 (A.12 Simulation Experiments) |
| A.10 Comparisons with Prior Works on Visual Prompting for Manipulation There has been several concurrent works investigating the application of visual prompting of VLMs ... | comparison identity and matched condition | p. 26 (A.9 Implementation Details of Path Solver) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We evaluate two variants of the system: "Auto" uses foundation models to automatically generate ReKep, and "Annotated (Annot.)" uses human-annotated ReKep. | component/input/data sensitivity | p. 7 (4 Experiments) |
| Results are shown on two robot platforms and on a variety of tasks featuring multi-stage, in-the-wild, bimanual, and reactive behaviors, all without task-specific data, ... | component/input/data sensitivity | p. 8 (4 Experiments) |
| Although the monolithic policy excels in training scenarios given its access to expert demonstrations, we observe that ReKep performs significantly stronger in unseen settings, ... | component/input/data sensitivity | p. 27 (A.12 Simulation Experiments) |
| We find that applying PCA improves the clustering as it often removes details and artifacts related to texture that are not useful for our ... | component/input/data sensitivity | p. 22 (A.5 Implementation Details of Keypoint Proposal) |
| (3) How do the individual components contribute to the failure cases of the system (Sec. | component/input/data sensitivity | p. 7 (4 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions are summarized as follows: 1) We formulate manipulation tasks as a hierarchical optimization problem with Relational Keypoint Constraints; 2) We devise a ... | Folding 0/10 4/10 7/10 Total (%) 10.0% 44.3% 68.6% Table 1: Success rate on wheeled singlearm and stationary bimanual platforms. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 27 (A.12 Simulation Experiments), p. 8 (Figure/Table caption), p. 22 (A.5 Implementation Details of Keypoint Proposal) |
| Primary metric/result | Folding 0/10 3/10 5/10 Total (%) 6.7% 26.7% 46.7% Table 2: Success rate under external disturbances across both robot platforms. | numeric claim only at cited anchor | p. 7 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 7 / 4 Experiments - extractive body cue:** Each setting has 10 trials, in which object poses are randomized.
- **p. 24 / A.7 Implementation Details of Point Tracker - extractive body cue:** The entire procedure runs at a fixed frequency of 20 Hz.
- **p. 24 / A.8 Implementation Details of Sub-Goal Solver - extractive body cue:** Scene Collision Avoidance: We use nvblox [149] with the PyTorch wrapper [58] to compute the ESDF of the scene in a separate node that runs ...
- **p. 25 / A.8 Implementation Details of Sub-Goal Solver - extractive body cue:** In the sub-goal solver module, we first downsample the gripper points and the grasped object points to have a maximum of 30 points using farthest ...
- **p. 25 / A.9 Implementation Details of Path Solver - extractive body cue:** Specifically, we define a fixed step size (20cm and 45 degree) and linearly approximate the desired number of "intermediate poses", which are used as decision ...
- **p. 27 / A.12 Simulation Experiments - extractive body cue:** Success rates are averaged across 100 trials and reported below.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The optimization module, on the other hand, does not contribute as much to the failures despite given limited time budget, since there often exist ... | p. 8 (4 Experiments) |
| body limitation/failure cue | Figure 7: Stationary Dual-Arm Platform. A.2 Wheeled Single-Arm Platform One of our investigated platform is a Franka arm mounted on a wheeled base built ... | p. 19 (Figure/Table caption) |
| body limitation/failure cue | Herein we present additional limitations of the existing system. | p. 27 (A.11 Extended Discusssions on Limitations) |
| body limitation/failure cue | Bimanual Coordination: Although we demonstrate the application of ReKep to bimanual manipulation, we also identify several important limitations in this domain. | p. 27 (A.11 Extended Discusssions on Limitations) |
| body limitation/failure cue | (3) How do the individual components contribute to the failure cases of the system (Sec. | p. 7 (4 Experiments) |
| body limitation/failure cue | In this section, we perform an empirical investigation by manually inspecting the failure cases of the experiments reported in Tab. | p. 8 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| To address this while ensuring efficiency, future works can consider using hardware-accelerated implementations to solve the problems in joint space [58]. | p. 25 (A.8 Implementation Details of Sub-Goal Solver) |
| Each setting has 10 trials, in which object poses are randomized. | p. 7 (4 Experiments) |
| Additional implementation details can be found in Appendix, including keypoint proposal (A.5), VLM querying (A.6), point trackers (A.7), sub-goal solver (A.8), and path solver ... | p. 7 (4 Experiments) |
| However, we do observe that the VLM may miss certain steps to complete the folding as the operator expected, but we recognize that this ... | p. 8 (4 Experiments) |
| Scene Collision Avoidance: We use nvblox [149] with the PyTorch wrapper [58] to compute the ESDF of the scene in a separate node that ... | p. 24 (A.8 Implementation Details of Sub-Goal Solver) |
| We implement a simple point tracker following [121] based on DINOv2 (ViT-S14) [5] that leverages the fact that multiple RGB-D cameras are present and ... | p. 24 (A.7 Implementation Details of Point Tracker) |
| (Dual-Arm only) Self-Collision Avoidance: To avoid two arms collide with each other, we compute the pairwise distance between the two point sets, each including ... | p. 25 (A.8 Implementation Details of Sub-Goal Solver) |
| (Dual-Arm only) Self-Collision Avoidance: We similarly compute self-collision avoidance for the dual-arm platform as in the sub-goal problem. | p. 26 (A.9 Implementation Details of Path Solver) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 4 Experiments - extractive body cue:** The optimization module, on the other hand, does not contribute as much to the failures despite given limited time budget, since there often exist many ...
- **p. 19 / Figure/Table caption - extractive body cue:** Figure 7: Stationary Dual-Arm Platform. A.2 Wheeled Single-Arm Platform One of our investigated platform is a Franka arm mounted on a wheeled base built with ...
- **p. 27 / A.11 Extended Discusssions on Limitations - extractive body cue:** Herein we present additional limitations of the existing system.
- **p. 27 / A.11 Extended Discusssions on Limitations - extractive body cue:** Bimanual Coordination: Although we demonstrate the application of ReKep to bimanual manipulation, we also identify several important limitations in this domain.
- **p. 7 / 4 Experiments - extractive body cue:** (3) How do the individual components contribute to the failure cases of the system (Sec.
- **p. 8 / 4 Experiments - extractive body cue:** In this section, we perform an empirical investigation by manually inspecting the failure cases of the experiments reported in Tab.

- **PDF anchors reviewed:** datasets p. 8 (4 Experiments), p. 8 (4 Experiments), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 25 (A.8 Implementation Details of Sub-Goal Solver), p. 26 (A.9 Implementation Details of Path Solver), metrics p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 27 (A.12 Simulation Experiments), p. 8 (Figure/Table caption), p. 24 (A.8 Implementation Details of Sub-Goal Solver), baselines p. 7 (4 Experiments), p. 27 (A.12 Simulation Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 27 (A.12 Simulation Experiments), p. 26 (A.9 Implementation Details of Path Solver), results p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 27 (A.12 Simulation Experiments), p. 8 (Figure/Table caption), p. 22 (A.5 Implementation Details of Keypoint Proposal).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
