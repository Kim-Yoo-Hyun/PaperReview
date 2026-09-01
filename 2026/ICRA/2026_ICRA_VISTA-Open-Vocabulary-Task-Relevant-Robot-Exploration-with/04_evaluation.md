# Evaluation - VISTA: Open-Vocabulary, Task-Relevant Robot Exploration with Online Semantic Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html; PDF retrieval source: https://arxiv.org/pdf/2507.01125. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (V. RESULTS), p. 6 (V. RESULTS), p. 5 (V. RESULTS), p. 5 (V. RESULTS)): On the more challenging map domain, we find that our method has a significant improvement over the baseline methods, where our method has a 100% success rate while both baselines ...

## Evaluation Body Digest

- **p. 5 / V. RESULTS - extractive body cue:** We evaluate each method across six scenes: three benchmark scenes in Nerfstudio (Plane, Kitchen, and Poster) and three additional datasets (Flight, Clutter, and Adirondacks), shown ...
- **p. 5 / V. RESULTS - extractive body cue:** Lastly, we demonstrate our full pipeline in hardware on a Boston Dynamics Spot quadruped robot to show the versatility of our method to different types ...
- **p. 6 / V. RESULTS - extractive body cue:** Spot Quadruped Hardware Experiments For our second hardware platform, we use a Boston Dynamics Spot quadruped robot fitted with RGB-D cameras and onboard odometry.
- **p. 6 / V. RESULTS - extractive body cue:** Six real scenes were used in this comparison, three from the Nerfstudio dataset {Plane, Kitchen, Poster} and three additional datasets {Flight, Clutter, Adirondacks}. and Adirondacks ...
- **p. 6 / V. RESULTS - extractive body cue:** We evaluate all methods on success rate (SR), time to reach (TTR), and success weighted by inverse path length (SPL), as done in [43] and ...
- **p. 6 / V. RESULTS - extractive body cue:** Our method has the highest success rate on this map with an 83.33% success rate over the RT-Guide baseline success rate of 66.67%, and semantic ...
- **p. 5 / V. RESULTS - extractive body cue:** We find that VISTA achieves the highest PSNR and SSIM scores and the lowest LPIPS score across all scenes.
- **p. 5 / V. RESULTS - extractive body cue:** For example, the best-competing method, FisherRF, requires almost twice as many training iterations to achieve the same photometric scores as VISTA, in the Poster

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** V. RESULTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| V. RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | On the more challenging map domain, we find that our method has a significant improvement over the baseline methods, where our method has a ... | p. 6 (V. RESULTS) |
| V. RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our geometric information gain metric significantly outperforms baselines FisherRF and Bayes Rays in the next best view selection task for about 50K iterations in ... | p. 6 (V. RESULTS) |
| V. RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | We find that VISTA achieves the highest PSNR and SSIM scores and the lowest LPIPS score across all scenes. | p. 5 (V. RESULTS) |
| V. RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | For example, the best-competing method, FisherRF, requires almost twice as many training iterations to achieve the same photometric scores as VISTA, in the Poster | p. 5 (V. RESULTS) |

## Dataset / Benchmark Role

- **p. 5 / V. RESULTS - extractive body cue:** We evaluate each method across six scenes: three benchmark scenes in Nerfstudio (Plane, Kitchen, and Poster) and three additional datasets (Flight, Clutter, and Adirondacks), shown ...
- **p. 5 / V. RESULTS - extractive body cue:** Lastly, we demonstrate our full pipeline in hardware on a Boston Dynamics Spot quadruped robot to show the versatility of our method to different types ...
- **p. 6 / V. RESULTS - extractive body cue:** Spot Quadruped Hardware Experiments For our second hardware platform, we use a Boston Dynamics Spot quadruped robot fitted with RGB-D cameras and onboard odometry.
- **p. 6 / V. RESULTS - extractive body cue:** Six real scenes were used in this comparison, three from the Nerfstudio dataset {Plane, Kitchen, Poster} and three additional datasets {Flight, Clutter, Adirondacks}. and Adirondacks ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. System overview of VISTA. Real-time sensor data is gathered from a robot hardware platform to train a semantic 3DGS map. The semantic and ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2. Geometric information gain based on view diversity coverage. Given a point cloud, voxels are characterized as free, occupied, and unobserved. These categories are ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3. Our geometric information gain metric significantly outperforms baselines FisherRF and Bayes Rays in the next best view selection task for about 50K iterations ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 4. The top row shows our three environments and two robots, with the search object in a green circle. The second row shows an ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We evaluate each method across six scenes: three benchmark scenes in Nerfstudio (Plane, Kitchen, and Poster) and three additional datasets (Flight, Clutter, and Adirondacks), ... | embodiment, simulator version and control stack | p. 5 (V. RESULTS), p. 5 (V. RESULTS) |
| Task/environment | Lastly, we demonstrate our full pipeline in hardware on a Boston Dynamics Spot quadruped robot to show the versatility of our method to different ... | reset, timeout, object/scene variation | p. 5 (V. RESULTS), p. 6 (V. RESULTS) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (III. PROBLEM FORMULATION), p. 2 (I. INTRODUCTION) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (III. PROBLEM FORMULATION), p. 2 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We evaluate all methods on success rate (SR), time to reach (TTR), and success weighted by inverse path length (SPL), as done in [43] ... | definition/direction/unit from same section | p. 6 (V. RESULTS) |
| Our method has the highest success rate on this map with an 83.33% success rate over the RT-Guide baseline success rate of 66.67%, and ... | definition/direction/unit from same section | p. 6 (V. RESULTS) |
| We find that VISTA achieves the highest PSNR and SSIM scores and the lowest LPIPS score across all scenes. | definition/direction/unit from same section | p. 5 (V. RESULTS) |
| For example, the best-competing method, FisherRF, requires almost twice as many training iterations to achieve the same photometric scores as VISTA, in the Poster | definition/direction/unit from same section | p. 5 (V. RESULTS) |
| Fig. 4. The top row shows our three environments and two robots, with the search object in a green circle. The second row shows ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Fig. 1. System overview of VISTA. Real-time sensor data is gathered from a robot hardware platform to train a semantic 3DGS map. The semantic ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| The results suggest that our method is able to outperform both baselines on both maps because we reason about both semantic and geometric information ... | comparison identity and matched condition | p. 6 (V. RESULTS) |
| Our geometric information gain metric significantly outperforms baselines FisherRF and Bayes Rays in the next best view selection task for about 50K iterations in ... | comparison identity and matched condition | p. 6 (V. RESULTS) |
| In our baseline comparisons, we train a radiance field using a predetermined set of training views for a fixed number of iterations (1000). | comparison identity and matched condition | p. 5 (V. RESULTS) |
| Next Best View Selection Baseline Comparisons To evaluate our geometric information gain metric, we compare against baseline approaches FisherRF [17] and Bayes' Rays [33]. | comparison identity and matched condition | p. 5 (V. RESULTS) |
| Fig. 4. The top row shows our three environments and two robots, with the search object in a green circle. The second row shows ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| no ablation sentence selected | not reported; proposed stress test only | verify ablation section |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We present VISTA, an algorithm for Viewpoint-based Image Selection with Semantic Task Awareness. | On the more challenging map domain, we find that our method has a significant improvement over the baseline methods, where our method has a ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (V. RESULTS), p. 6 (V. RESULTS), p. 5 (V. RESULTS), p. 5 (V. RESULTS) |
| Primary metric/result | Our geometric information gain metric significantly outperforms baselines FisherRF and Bayes Rays in the next best view selection task for about 50K iterations in ... | numeric claim only at cited anchor | p. 6 (V. RESULTS) |

- Numeric sentences retained from the body:
- **p. 6 / V. RESULTS - extractive body cue:** For pose feedback, we use an OptiTrack external motion capture system, and all 3DGS training and planning is done on a desktop computer that has ...
- **p. 6 / V. RESULTS - extractive body cue:** Each method is tested on a query and map for two trials, totaling 12 trials for each method, six on each map.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We evaluate each method using the standard metrics: Peak-Signal-Noise-Ratio (PSNR), Learned Perceptuation Image Patch Similarity (LPIPS), and Structural Similarity Index Measure (SSIM). | p. 5 (V. RESULTS) |
| body limitation/failure cue | Through these experiments, we find that all methods have some successes on the easy low-occlusion map domain. | p. 6 (V. RESULTS) |
| body limitation/failure cue | Fig. 4. The top row shows our three environments and two robots, with the search object in a green circle. The second row shows ... | p. 7 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For pose feedback, we use an OptiTrack external motion capture system, and all 3DGS training and planning is done on a desktop computer that ... | p. 6 (V. RESULTS) |
| The offboard computer is equipped with a 4.2 GHz AMD Ryzen 7 7800X3D CPU and an NVIDIA GeForce RTX 4090 (24GB memory). | p. 6 (V. RESULTS) |
| We then incorporate semantic information and our proposed planning approach to implement the full pipeline in hardware on a quadrotor platform. | p. 5 (V. RESULTS) |
| Lastly, we demonstrate our full pipeline in hardware on a Boston Dynamics Spot quadruped robot to show the versatility of our method to different ... | p. 5 (V. RESULTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / V. RESULTS - extractive body cue:** We evaluate each method using the standard metrics: Peak-Signal-Noise-Ratio (PSNR), Learned Perceptuation Image Patch Similarity (LPIPS), and Structural Similarity Index Measure (SSIM).
- **p. 6 / V. RESULTS - extractive body cue:** Through these experiments, we find that all methods have some successes on the easy low-occlusion map domain.
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 4. The top row shows our three environments and two robots, with the search object in a green circle. The second row shows an ...

- **PDF anchors reviewed:** datasets p. 5 (V. RESULTS), p. 5 (V. RESULTS), p. 6 (V. RESULTS), p. 6 (V. RESULTS), metrics p. 6 (V. RESULTS), p. 6 (V. RESULTS), p. 5 (V. RESULTS), p. 5 (V. RESULTS), p. 7 (Figure/Table caption), p. 1 (Figure/Table caption), baselines p. 6 (V. RESULTS), p. 6 (V. RESULTS), p. 5 (V. RESULTS), p. 5 (V. RESULTS), p. 7 (Figure/Table caption), results p. 6 (V. RESULTS), p. 6 (V. RESULTS), p. 5 (V. RESULTS), p. 5 (V. RESULTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
