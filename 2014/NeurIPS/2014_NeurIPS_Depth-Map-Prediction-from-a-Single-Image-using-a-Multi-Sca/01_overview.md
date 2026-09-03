# Depth Map Prediction from a Single Image using a Multi-Scale Deep Network

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1406.2283.
> PDF retrieval source: https://arxiv.org/pdf/1406.2283. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2014 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Vision, monocular depth, geometry
- Official paper: https://arxiv.org/abs/1406.2283
- Full-text retrieval: https://arxiv.org/pdf/1406.2283
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Moreover, the task is inherently ambiguous, and a technically ill-posed problem: Given an image, an infinite number of possible world scenes may have produced it.를 문제로 두고, In this paper we present a new approach for estimating depth from a single image.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Predicting depth is an essential component in understanding the 3D geometry of a scene.
- **p. 1 / Abstract - extractive body cue:** While for stereo images local correspondence suffices for estimation, finding depth relations from a single image is less straightforward, requiring integration of both global and ...
- **p. 1 / Abstract - extractive body cue:** Moreover, the task is inherently ambiguous, with a large source of uncertainty coming from the overall scale.
- **p. 1 / Abstract - extractive body cue:** In this paper, we present a new method that addresses this task by employing two deep network stacks: one that makes a coarse global prediction ...
- **p. 1 / Abstract - extractive body cue:** We also apply a scale-invariant error to help measure depth relations rather than scale.
- **p. 1 / 1 Introduction - extractive body cue:** Moreover, the task is inherently ambiguous, and a technically ill-posed problem: Given an image, an infinite number of possible world scenes may have produced it.
- **p. 1 / 1 Introduction - extractive body cue:** While there is much prior work on estimating depth based on stereo images or motion [17], there has been relatively little on estimating depth from ...

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** In this paper we present a new approach for estimating depth from a single image.
- **p. 3 / 3 Approach - extractive body cue:** The fine-scale network stack consists of convolutional layers only, along with one pooling stage for the first layer edge features.
- **p. 4 / 3 Approach - extractive body cue:** In addition to the scale-invariant error, we also measure the performance of our method according to several error metrics have been proposed in prior works, ...
- **p. 1 / 1 Introduction - extractive body cue:** Thus, stereo depth estimation can be reduced to developing robust image point correspondences - which can often be found using local appearance features.
- **p. 2 / 3 Approach - extractive body cue:** Similarly, the lower and middle layers are designed to combine information from different parts of the image through max-pooling operations to a small spatial dimension.
- **p. 4 / 3 Approach - extractive body cue:** We train the coarse network first against the ground-truth targets, then train the fine-scale network keeping the coarse-scale output fixed (i.e. when training the fine ...
- **p. 2 / 3 Approach - extractive body cue:** Both stacks are applied to the original input, but in addition, the coarse network's output is passed to the fine network as additional first-layer image ...
- **p. 2 / 3 Approach - extractive body cue:** 3.1 Model Architecture Our network is made of two component stacks, shown in Fig.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Both stacks are applied to the original input, but in addition, the coarse network's output is passed to the fine network as additional first-layer image features. | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (3 Approach), p. 3 (3 Approach) |
| State/latent | stacks, applied, original, input, addition, coarse, network, output, passed, fine, additional, first-layer | geometry, map, object/relationship state | p. 2 (3 Approach), p. 3 (3 Approach), p. 3 (3 Approach) |
| Output/action | The input, feature map and output sizes are also given in Fig. | point map, pose, scene graph, affordance 또는 query result | p. 3 (3 Approach), p. 3 (3 Approach), p. 2 (1 Introduction) |
| Objective/outcome | 3, we set the per-sample training loss to 4 | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (3 Approach), p. 4 (3 Approach), p. 5 (3 Approach) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** In this paper we present a new approach for estimating depth from a single image.
- **p. 3 / 3 Approach - extractive body cue:** The fine-scale network stack consists of convolutional layers only, along with one pooling stage for the first layer edge features.
- **p. 4 / 3 Approach - extractive body cue:** In addition to the scale-invariant error, we also measure the performance of our method according to several error metrics have been proposed in prior works, ...
- **p. 1 / 1 Introduction - extractive body cue:** Thus, stereo depth estimation can be reduced to developing robust image point correspondences - which can often be found using local appearance features.
- **p. 2 / 3 Approach - extractive body cue:** Similarly, the lower and middle layers are designed to combine information from different parts of the image through max-pooling operations to a small spatial dimension.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3: Qualitative comparison of Make3D, our method trained with l2 loss (λ = 0), and our method trained with both l2 and scale-invariant loss ...
- **p. 6 / 5 Results - extractive body cue:** Our system achieves the best performance on all metrics, obtaining an average 35% relative gain compared to the runner-up.
- **p. 6 / 5 Results - extractive body cue:** While we did not observe numeric gains using λ = 0.5 over λ = 0, it did produce slight qualitative improvements in the more detailed ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 6 (5 Results) |
| Embodiment/environment | We use the official train/test split, using 249 scenes for training and 215 for testing, and construct our training set using the raw data for these scenes. | hardware/simulator version and reset protocol | p. 5 (4 Experiments), p. 5 (4 Experiments) |
| Dataset/benchmark | The depth for this dataset is sampled at irregularly spaced points, captured at different times using a rotating LIDAR scanner. | role, split, size and leakage | p. 5 (4 Experiments), p. 5 (4 Experiments), p. 6 (4 Experiments), p. 6 (4 Experiments) |
| Metric | These ratios were found by trial-and-error on a validation set (folded back into the training set for our final evaluations), and the global scale of all the rates was tuned to a ... | definition, denominator, direction and uncertainty | p. 5 (4 Experiments), p. 7 (5 Results), p. 6 (5 Results) |
| Baseline/ablation | 4.3 Baselines and Comparisons We compare our method against Make3D trained on the same datasets, as well as the published results of other current methods [12, 7]. | fair input/data/compute/action matching | p. 6 (4 Experiments), p. 6 (5 Results), p. 7 (5 Results) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 6 Discussion - extractive body cue:** In future work, we plan to extend our method to incorporate further 3D geometry information, such as surface normals.
- **p. 6 / 5 Results - extractive body cue:** Although the fine-scale network does not improve in the error measurements, its effect is clearly visible in the depth maps - surface boundaries have sharper ...
- **p. 7 / 5 Results - extractive body cue:** Again, the fine-scale network does not improve much over the coarse one in the error metrics, but differences between the two can be seen in ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Moreover, the task is inherently ambiguous, and a technically ill-posed problem: Given an image, an infinite number of possible world scenes may have produced it.를 문제로 두고, In this paper we present a new approach for estimating depth from a single image.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 1 (1 Introduction), p. 3 (3 Approach), p. 4 (3 Approach), p. 2 (3 Approach), p. 2 (3 Approach) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
