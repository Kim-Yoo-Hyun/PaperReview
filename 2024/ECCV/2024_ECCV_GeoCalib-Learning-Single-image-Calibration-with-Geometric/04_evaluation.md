# Evaluation - GeoCalib: Learning Single-image Calibration with Geometric Optimization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5636_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05636.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 11 (5 Experiments), p. 12 (5 Experiments), p. 12 (5 Experiments), p. 13 (Figure/Table caption), p. 14 (13 Dataset), p. 13 (13 Dataset)): Results: Table 1 shows that GeoCalib largely improves on top of all deep singleimage calibration networks, and outperforms classical methods in all metrics, except for the finest threshold on FoV ...

## Evaluation Body Digest

- **p. 10 / 5 Experiments - extractive body cue:** We align the respective 3D models to gravity using COLMAP [70] and sample a total of 2k images with varying intrinsics from the scenes in ...
- **p. 9 / 5 Experiments - extractive body cue:** 5.1 Gravity and Field-of-View estimation We first compare GeoCalib to existing deep and classical approaches with pinhole images from four real-world datasets.
- **p. 10 / 5 Experiments - extractive body cue:** Datasets: We conduct this experiment on four popular datasets not seen during training. i) Stanford2D3D [8] consists of images samples from 360° panoramas captured inside ...
- **p. 13 / 13 Dataset - extractive body cue:** (1) While OpenPano is about 5 times smaller than 360 Cities, it is more balanced across different domains, resulting in improvements on the test set ...
- **p. 9 / 5 Experiments - extractive body cue:** Experiments are performed on a diverse range of real-world images (indoor, outdoor, and natural environments), and we analyze the impacts of our design decisions.
- **p. 11 / 5 Experiments - extractive body cue:** For fairness, we also retrain DeepCalib [50] and ParamNet [37] on our dataset.
- **p. 11 / 5 Experiments - extractive body cue:** Setup: We evaluate camera distortion estimation on the MegaDepth dataset [46] with crowd-sourced, distorted images.
- **p. 12 / 5 Experiments - extractive body cue:** We average the pixel distortion errors over each image and compute the recall of the average distortion error within an image over the entire dataset.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5 Experiments (p. 9); 13 Dataset (p. 13).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Results: Table 1 shows that GeoCalib largely improves on top of all deep singleimage calibration networks, and outperforms classical methods in all metrics, except ... | p. 11 (5 Experiments) |
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Simultaneously optimizing multiple images with shared intrinsic parameters improves the estimation accuracy of both field of view (left) and gravity direction (right). | p. 12 (5 Experiments) |
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | GeoCalib-pinhole already improves over all baselines, suggesting that the model can zero-shot generalize to radial distortion through optimization. | p. 12 (5 Experiments) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 4: Visual Localization on InLoc [74]. The gravity prior estimated by GeoCalib improves pose estimation and is more effective than the estimate of ... | p. 13 (Figure/Table caption) |
| 13 Dataset | EMPIRICAL / REAL-ROBOT OR HARDWARE | Adding the gravity constraint in both RANSAC and pose refinement improves localization accuracy. | p. 14 (13 Dataset) |

## Dataset / Benchmark Role

- **p. 10 / 5 Experiments - extractive body cue:** We align the respective 3D models to gravity using COLMAP [70] and sample a total of 2k images with varying intrinsics from the scenes in ...
- **p. 9 / 5 Experiments - extractive body cue:** 5.1 Gravity and Field-of-View estimation We first compare GeoCalib to existing deep and classical approaches with pinhole images from four real-world datasets.
- **p. 10 / 5 Experiments - extractive body cue:** Datasets: We conduct this experiment on four popular datasets not seen during training. i) Stanford2D3D [8] consists of images samples from 360° panoramas captured inside ...
- **p. 13 / 13 Dataset - extractive body cue:** (1) While OpenPano is about 5 times smaller than 360 Cities, it is more balanced across different domains, resulting in improvements on the test set ...
- **p. 9 / 5 Experiments - extractive body cue:** Experiments are performed on a diverse range of real-world images (indoor, outdoor, and natural environments), and we analyze the impacts of our design decisions.
- **p. 11 / 5 Experiments - extractive body cue:** For fairness, we also retrain DeepCalib [50] and ParamNet [37] on our dataset.
- **p. 11 / 5 Experiments - extractive body cue:** Setup: We evaluate camera distortion estimation on the MegaDepth dataset [46] with crowd-sourced, distorted images.
- **p. 12 / 5 Experiments - extractive body cue:** We average the pixel distortion errors over each image and compute the recall of the average distortion error within an image over the entire dataset.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1: Learning vs. geometry? To estimate the camera calibration from a single image, classical approaches struggle with environments devoid of lines while deep networks ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: Architecture of GeoCalib. A DNN predicts a Perspectivel Field with confi- dences, to which camera parameters are fitted with a Levenberg-Marquardt optimization. GeoCalib ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: Good features to calibrate. We show the confidences learned by GeoCalib for both components of the Perspective Field. The up-vector is most confident ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 4: Ranking images by uncertainty. We report the gravity error / uncertainty for 8 outdoor (top) and indoor (bottom) images from left-to-right, sorted by ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 5: Qualitative results. We show five examples of GeoCalib's prediction on Stanford2D3D [8], TartanAir [82], MegaDepth [46] and LaMAR [66] (x2). a-b) depict the ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 1: Evaluation on diverse datasets. Approaches marked as * were retrained on our dataset OpenPano. We color the best and second best results for ...
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 6: Image undistortion. GeoCalib can robustly predict lens distortion from a single image (left), which can be used to rectify images (right) in the ...
- **p. 11 / Figure/Table caption - extractive body cue:** Table 2: Calibration of distorted images. On Internet images from the MegaDepth [46] dataset with radial distortion [27], GeoCalib estimates a more ac- curate distortion ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We align the respective 3D models to gravity using COLMAP [70] and sample a total of 2k images with varying intrinsics from the scenes ... | embodiment, simulator version and control stack | p. 10 (5 Experiments), p. 9 (5 Experiments) |
| Task/environment | 5.1 Gravity and Field-of-View estimation We first compare GeoCalib to existing deep and classical approaches with pinhole images from four real-world datasets. | reset, timeout, object/scene variation | p. 9 (5 Experiments), p. 10 (5 Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 1 (1 Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (2 Microsoft Mixed Reality & AI Lab), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Fig. 8: Multi-image optimization. Simultaneously optimizing multiple images with shared intrinsic parameters improves the estimation accuracy of both field of view (left) and gravity ... | definition/direction/unit from same section | p. 12 (Figure/Table caption) |
| In RANSAC, we add a constant reward to the MSAC score if the estimated gravity is within 2σ of our estimated gravity uncertainty. | definition/direction/unit from same section | p. 14 (13 Dataset) |
| For each metric, we report the median error and the Area Under the recall Curve (AUC) up to 1/5/10°. | definition/direction/unit from same section | p. 9 (5 Experiments) |
| We also report the pixel distortion error, defined as the Euclidean distance between the pixel distorted by the ground truth camera | definition/direction/unit from same section | p. 11 (5 Experiments) |
| In contrast, GeoCalib is the first deep method that consistently matches or surpasses the accuracy of classical methods without any assumption on the scene, ... | definition/direction/unit from same section | p. 11 (5 Experiments) |
| (4) Supervising the result of the optimization and (5) learning uncertainties significantly boost the accuracy across the board as this i) allows GeoCalib to ... | definition/direction/unit from same section | p. 13 (13 Dataset) |
| For each image, we evaluate the gravity estimation in terms of angular roll and pitch errors (in degrees), and the focal length in terms ... | definition/direction/unit from same section | p. 9 (5 Experiments) |
| Training our model on distorted images further boosts the accuracy. | definition/direction/unit from same section | p. 12 (5 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Baselines: We benchmark our method against the deep methods DeepCalib [50], CTRL-C [44], Perceptual [35], MSCC [73] and ParamNet [37]. | comparison identity and matched condition | p. 11 (5 Experiments) |
| Results: Table 1 shows that GeoCalib largely improves on top of all deep singleimage calibration networks, and outperforms classical methods in all metrics, except ... | comparison identity and matched condition | p. 11 (5 Experiments) |
| We start from the closest baseline PerspectiveNet | comparison identity and matched condition | p. 12 (5 Experiments) |
| GeoCalib-pinhole already improves over all baselines, suggesting that the model can zero-shot generalize to radial distortion through optimization. | comparison identity and matched condition | p. 12 (5 Experiments) |
| Approach DUC 1 DUC2 Recall at (0.25m,10°) / (0.5m,10°) / (1.0m,10°) ↑ Baseline (SP+SG) 43.4 66.7 78.3 51.9 74.8 78.6 + gravity in refinement ... | comparison identity and matched condition | p. 13 (13 Dataset) |
| As a baseline, we use the gravity estimated by UVP [58]. | comparison identity and matched condition | p. 14 (13 Dataset) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| In contrast, GeoCalib is the first deep method that consistently matches or surpasses the accuracy of classical methods without any assumption on the scene, ... | component/input/data sensitivity | p. 11 (5 Experiments) |
| We evaluate both variants of GeoCalib trained with pinhole and distorted images. | component/input/data sensitivity | p. 12 (5 Experiments) |
| 5.3 Insights Ablation study: We perform an extensive ablation study to verify the design decisions of our method. | component/input/data sensitivity | p. 12 (5 Experiments) |
| Fig. 1: Learning vs. geometry? To estimate the camera calibration from a single image, classical approaches struggle with environments devoid of lines while deep ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |
| Fig. 2: Architecture of GeoCalib. A DNN predicts a Perspectivel Field with confi- dences, to which camera parameters are fitted with a Levenberg-Marquardt optimization. ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |
| Fig. 3: Good features to calibrate. We show the confidences learned by GeoCalib for both components of the Perspective Field. The up-vector is most ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Camera calibration consists of estimating the intrinsic and extrinsic parameters of a camera. | Results: Table 1 shows that GeoCalib largely improves on top of all deep singleimage calibration networks, and outperforms classical methods in all metrics, except ... | PDF body cue; verify exact table/figure and matched conditions | p. 11 (5 Experiments), p. 12 (5 Experiments), p. 12 (5 Experiments), p. 13 (Figure/Table caption), p. 14 (13 Dataset), p. 13 (13 Dataset) |
| Primary metric/result | Simultaneously optimizing multiple images with shared intrinsic parameters improves the estimation accuracy of both field of view (left) and gravity direction (right). | numeric claim only at cited anchor | p. 12 (5 Experiments) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | UVP [58] assumes a Manhattan world, and this stronger assumption about scene configuration enables slightly more accurate predictions on easy samples, but completely fails ... | p. 11 (5 Experiments) |
| body limitation/failure cue | In contrast, simply averaging the independently-estimated FoVs over all images is less effective and cannot benefit the gravity estimation. | p. 14 (13 Dataset) |
| body limitation/failure cue | Thanks to its differentiable optimization, it learns strong priors that make it both more accurate and more robust than existing approaches, with a strong ... | p. 14 (6 Conclusion) |
| body limitation/failure cue | Fig. 2: Architecture of GeoCalib. A DNN predicts a Perspectivel Field with confi- dences, to which camera parameters are fitted with a Levenberg-Marquardt optimization. ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | GeoCalib is more accurate than approaches based on learning and more robust than those based on lines and vanishing points. | p. 10 (5 Experiments) |
| body limitation/failure cue | GeoCalib can robustly predict lens distortion from a single image (left), which can be used to rectify images (right) in the wild. | p. 11 (5 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We average the pixel distortion errors over each image and compute the recall of the average distortion error within an image over the entire ... | p. 12 (5 Experiments) |
| The code and trained models will be released publicly. | p. 3 (1 Introduction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 11 / 5 Experiments - extractive body cue:** UVP [58] assumes a Manhattan world, and this stronger assumption about scene configuration enables slightly more accurate predictions on easy samples, but completely fails in ...
- **p. 14 / 13 Dataset - extractive body cue:** In contrast, simply averaging the independently-estimated FoVs over all images is less effective and cannot benefit the gravity estimation.
- **p. 14 / 6 Conclusion - extractive body cue:** Thanks to its differentiable optimization, it learns strong priors that make it both more accurate and more robust than existing approaches, with a strong generalization ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: Architecture of GeoCalib. A DNN predicts a Perspectivel Field with confi- dences, to which camera parameters are fitted with a Levenberg-Marquardt optimization. GeoCalib ...
- **p. 10 / 5 Experiments - extractive body cue:** GeoCalib is more accurate than approaches based on learning and more robust than those based on lines and vanishing points.
- **p. 11 / 5 Experiments - extractive body cue:** GeoCalib can robustly predict lens distortion from a single image (left), which can be used to rectify images (right) in the wild.

- **Evidence anchors reviewed:** datasets p. 10 (5 Experiments), p. 9 (5 Experiments), p. 10 (5 Experiments), p. 13 (13 Dataset), p. 9 (5 Experiments), p. 11 (5 Experiments), metrics p. 12 (Figure/Table caption), p. 14 (13 Dataset), p. 9 (5 Experiments), p. 11 (5 Experiments), p. 11 (5 Experiments), p. 13 (13 Dataset), baselines p. 11 (5 Experiments), p. 11 (5 Experiments), p. 12 (5 Experiments), p. 12 (5 Experiments), p. 13 (13 Dataset), p. 14 (13 Dataset), results p. 11 (5 Experiments), p. 12 (5 Experiments), p. 12 (5 Experiments), p. 13 (Figure/Table caption), p. 14 (13 Dataset), p. 13 (13 Dataset).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
