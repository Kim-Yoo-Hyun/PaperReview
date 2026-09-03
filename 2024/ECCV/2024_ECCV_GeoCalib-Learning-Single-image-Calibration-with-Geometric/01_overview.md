# GeoCalib: Learning Single-image Calibration with Geometric Optimization

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5636_ECCV_2024_paper.php.
> PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05636.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ECCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: geometry, 3D Vision
- Official paper: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5636_ECCV_2024_paper.php
- Full-text retrieval: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05636.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Veicht et al. ✓accurate ✗not robust man-made natural input image classical geometry lines & vanishing points black-box learning end-to-end training GeoCalib learning & optimization FAILURE horizon line estimated gravity & camera intrins ...를 문제로 두고, Camera calibration consists of estimating the intrinsic and extrinsic parameters of a camera.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / 1 Introduction - extractive body cue:** Camera calibration consists of estimating the intrinsic and extrinsic parameters of a camera.
- **p. 1 / 1 Introduction - extractive body cue:** This information is required for most image-based 3D applications, including metrology, 3D reconstruction, and novel view synthesis.
- **p. 1 / 1 Introduction - extractive body cue:** This problem has been extensively studied, and many tools based on 3D geometry are available [49,56,69].
- **p. 1 / 1 Introduction - extractive body cue:** Since the process of image formation is well-understood, such tools can very accurately calibrate a camera from images taken in controlled lab conditions.
- **p. 1 / 1 Introduction - extractive body cue:** The calibration can also be estimated in uncontrolled conditions, which generally requires additional sensors or multiple images observing the same scene, using structure-from-motion [5,54,57,70] or ...
- **p. 2 / 1 Introduction - extractive body cue:** Veicht et al. ✓accurate ✗not robust man-made natural input image classical geometry lines & vanishing points black-box learning end-to-end training GeoCalib learning & optimization FAILURE ...
- **p. 2 / 1 Introduction - extractive body cue:** To generalize well to different environment, they however require large amounts of training data that is costly to acquire.

## Core Idea

- **p. 1 / 1 Introduction - extractive body cue:** Camera calibration consists of estimating the intrinsic and extrinsic parameters of a camera.
- **p. 2 / 1 Introduction - extractive body cue:** In this work, we introduce GeoCalib, a deep neural network (DNN) that leverages our knowledge of projective geometry through an optimization process.
- **p. 2 / 1 Introduction - extractive body cue:** Our approach can thus learn the right visual cues without explicit supervision but does not need to learn the process of estimating camera parameters, which ...
- **p. 3 / 1 Introduction - extractive body cue:** To support this, we show that GeoCalib can readily improve the accuracy of visual positioning.
- **p. 1 / 1 Introduction - extractive body cue:** This information is required for most image-based 3D applications, including metrology, 3D reconstruction, and novel view synthesis.
- **p. 2 / 1 Introduction - extractive body cue:** Given finite model capacity, this can only be approximated within the domain of the training data, without any guarantee outside.
- **p. 2 / 1 Introduction - extractive body cue:** Veicht et al. ✓accurate ✗not robust man-made natural input image classical geometry lines & vanishing points black-box learning end-to-end training GeoCalib learning & optimization FAILURE ...
- **p. 3 / 1 Introduction - extractive body cue:** This makes it possible to handle different camera models, such as pinhole and fisheye, without any retraining.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Veicht et al. ✓accurate ✗not robust man-made natural input image classical geometry lines & vanishing points black-box learning end-to-end training GeoCalib learning & optimization FAILURE horizon line estimated gravity & camera intrins ... | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1 Introduction), p. 1 (1 Introduction) |
| State/latent | Veicht, accurate, robust, man-made, natural, input, image, classical, geometry, lines, vanishing, points | geometry, map, object/relationship state | p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (2 Microsoft Mixed Reality & AI Lab) |
| Output/action | The calibration can also be estimated in uncontrolled conditions, which generally requires additional sensors or multiple images observing the same scene, using structure-from-motion [5,54,57,70] or SLAM [32,39,91]. | point map, pose, scene graph, affordance 또는 query result | p. 1 (1 Introduction), p. 1 (2 Microsoft Mixed Reality & AI Lab), p. 2 (1 Introduction) |
| Objective/outcome | We hypothesize that they lack the constraints that 3D geometry provides. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 1 (2 Microsoft Mixed Reality & AI Lab), p. 1 (1 Introduction), p. 2 (1 Introduction) |

## Main Claims and Actual Contribution

- **p. 1 / 1 Introduction - extractive body cue:** Camera calibration consists of estimating the intrinsic and extrinsic parameters of a camera.
- **p. 2 / 1 Introduction - extractive body cue:** In this work, we introduce GeoCalib, a deep neural network (DNN) that leverages our knowledge of projective geometry through an optimization process.
- **p. 2 / 1 Introduction - extractive body cue:** Our approach can thus learn the right visual cues without explicit supervision but does not need to learn the process of estimating camera parameters, which ...
- **p. 3 / 1 Introduction - extractive body cue:** To support this, we show that GeoCalib can readily improve the accuracy of visual positioning.
- **p. 1 / 1 Introduction - extractive body cue:** This information is required for most image-based 3D applications, including metrology, 3D reconstruction, and novel view synthesis.
- **p. 11 / 5 Experiments - extractive body cue:** Results: Table 1 shows that GeoCalib largely improves on top of all deep singleimage calibration networks, and outperforms classical methods in all metrics, except for ...
- **p. 12 / 5 Experiments - extractive body cue:** Simultaneously optimizing multiple images with shared intrinsic parameters improves the estimation accuracy of both field of view (left) and gravity direction (right).
- **p. 12 / 5 Experiments - extractive body cue:** GeoCalib-pinhole already improves over all baselines, suggesting that the model can zero-shot generalize to radial distortion through optimization.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 11 (5 Experiments), p. 12 (5 Experiments) |
| Embodiment/environment | We align the respective 3D models to gravity using COLMAP [70] and sample a total of 2k images with varying intrinsics from the scenes in the IMC 2021 test set [36]. iv) ... | hardware/simulator version and reset protocol | p. 10 (5 Experiments), p. 9 (5 Experiments) |
| Dataset/benchmark | Datasets: We conduct this experiment on four popular datasets not seen during training. i) Stanford2D3D [8] consists of images samples from 360° panoramas captured inside university buildings. ii) TartanAir [82] provides images ... | role, split, size and leakage | p. 10 (5 Experiments), p. 9 (5 Experiments), p. 10 (5 Experiments), p. 13 (13 Dataset) |
| Metric | Fig. 8: Multi-image optimization. Simultaneously optimizing multiple images with shared intrinsic parameters improves the estimation accuracy of both field of view (left) and gravity direction (right). This is useful for calibrating an ... | definition, denominator, direction and uncertainty | p. 12 (Figure/Table caption), p. 14 (13 Dataset), p. 9 (5 Experiments) |
| Baseline/ablation | Baselines: We benchmark our method against the deep methods DeepCalib [50], CTRL-C [44], Perceptual [35], MSCC [73] and ParamNet [37]. | fair input/data/compute/action matching | p. 11 (5 Experiments), p. 11 (5 Experiments), p. 12 (5 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 11 / 5 Experiments - extractive body cue:** UVP [58] assumes a Manhattan world, and this stronger assumption about scene configuration enables slightly more accurate predictions on easy samples, but completely fails in ...
- **p. 14 / 13 Dataset - extractive body cue:** In contrast, simply averaging the independently-estimated FoVs over all images is less effective and cannot benefit the gravity estimation.
- **p. 14 / 6 Conclusion - extractive body cue:** Thanks to its differentiable optimization, it learns strong priors that make it both more accurate and more robust than existing approaches, with a strong generalization ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: Architecture of GeoCalib. A DNN predicts a Perspectivel Field with confi- dences, to which camera parameters are fitted with a Levenberg-Marquardt optimization. GeoCalib ...
- **p. 10 / 5 Experiments - extractive body cue:** GeoCalib is more accurate than approaches based on learning and more robust than those based on lines and vanishing points.
- **p. 11 / 5 Experiments - extractive body cue:** GeoCalib can robustly predict lens distortion from a single image (left), which can be used to rectify images (right) in the wild.
- **p. 13 / 13 Dataset - extractive body cue:** (4) Supervising the result of the optimization and (5) learning uncertainties significantly boost the accuracy across the board as this i) allows GeoCalib to increase ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Veicht et al. ✓accurate ✗not robust man-made natural input image classical geometry lines & vanishing points black-box learning end-to-end training GeoCalib learning & optimization FAILURE horizon line estimated gravity & camera intrins ...를 문제로 두고, Camera calibration consists of estimating the intrinsic and extrinsic parameters of a camera.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 1 (1 Introduction), p. 1 (2 Microsoft Mixed Reality & AI Lab) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
