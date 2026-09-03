# Deep Closest Point: Learning Representations for Point Cloud Registration

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1905.03304.
> PDF retrieval source: https://arxiv.org/pdf/1905.03304. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2019 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Vision, registration, point cloud, alignment
- Official paper: https://arxiv.org/abs/1905.03304
- Full-text retrieval: https://arxiv.org/pdf/1905.03304
- Code/Project: https://github.com/WangYueFt/dcp
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Many modeling and computational challenges hamper the design of a stable and efficient registration method.를 문제로 두고, Contributions: Our contributions include the following: • We identify sub-network architectures designed to address difficulties in the classical ICP pipeline. • We propose a simple architecture to predict a rigid transformation alignin ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Point cloud registration is a key problem for computer vision applied to robotics, medical imaging, and other applications.
- **p. 1 / Abstract - extractive body cue:** This problem involves finding a rigid transformation from one point cloud into another so that they align.
- **p. 1 / Abstract - extractive body cue:** Iterative Closest Point (ICP) and its variants provide simple and easily-implemented iterative methods for this task, but these algorithms can converge to spurious local optima.
- **p. 1 / Abstract - extractive body cue:** To address local optima and other difficulties in the ICP pipeline, we propose a learning-based method, titled Deep Closest Point (DCP), inspired by recent techniques ...
- **p. 1 / Abstract - extractive body cue:** Our model consists of three parts: a point cloud embedding network, an attention-based module combined with a pointer generation layer, to approximate combinatorial matching, and ...
- **p. 1 / 1. Introduction - extractive body cue:** Many modeling and computational challenges hamper the design of a stable and efficient registration method.
- **p. 2 / 1. Introduction - extractive body cue:** Contributions: Our contributions include the following: • We identify sub-network architectures designed to address difficulties in the classical ICP pipeline. • We propose a simple ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Contributions: Our contributions include the following: • We identify sub-network architectures designed to address difficulties in the classical ICP pipeline. • We propose a simple ...
- **p. 1 / 1. Introduction - extractive body cue:** However, only our method achieve satisfying alignment for objects with sharp features and large transformation. globally optimal alignment; similarly, computing matchings becomes easier given some ...
- **p. 2 / 1. Introduction - extractive body cue:** Our model consists of three parts: (1) We map the input point clouds to permutation/rigid-invariant embeddings that help identify matching pairs of points (we compare ...
- **p. 5 / 4.5. Loss - extractive body cue:** The initial feature module (§4.1) and the attention module (§4.2) are both parameterized by a set of neural network weights, which must be learned during ...
- **p. 5 / 4.5. Loss - extractive body cue:** We use the following loss function to measure our model's agreement to the ground-truth rigid motions: Loss = ∥R⊤ XYRg XY -I∥2 + ∥tXY -tg ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Our model consists of three parts: (1) We map the input point clouds to permutation/rigid-invariant embeddings that help identify matching pairs of points (we compare PointNet [30] and DGCNN [48] for this ... | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1. Introduction), p. 1 (1. Introduction) |
| State/latent | model, consists, three, parts, input, point, clouds, permutation/rigid-invariant, embeddings, help, identify, matching | geometry, map, object/relationship state | p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Output/action | Given these two observations, most algorithms alternate between these two steps to try to obtain a better result. | point map, pose, scene graph, affordance 또는 query result | p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Problem Statement) |
| Objective/outcome | We use the following loss function to measure our model's agreement to the ground-truth rigid motions: Loss = ∥R⊤ XYRg XY -I∥2 + ∥tXY -tg XY∥2 + λ∥θ∥2 (11) Here, g denotes ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (4.5. Loss), p. 5 (4.5. Loss) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Contributions: Our contributions include the following: • We identify sub-network architectures designed to address difficulties in the classical ICP pipeline. • We propose a simple ...
- **p. 1 / 1. Introduction - extractive body cue:** However, only our method achieve satisfying alignment for objects with sharp features and large transformation. globally optimal alignment; similarly, computing matchings becomes easier given some ...
- **p. 2 / 1. Introduction - extractive body cue:** Our model consists of three parts: (1) We map the input point clouds to permutation/rigid-invariant embeddings that help identify matching pairs of points (we compare ...
- **p. 6 / 5. Experiments - extractive body cue:** DCP-v1 already outperforms other methods under all the performance metrics, and DCP-v2 exhibits even stronger performance.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4. Results of DCP-v2. Top: inputs. Bottom: outputs of DCP-v2. lems as a drop-in replacement for ICP with improved behav- ior. Beyond its direct ...
- **p. 6 / 5. Experiments - extractive body cue:** All angular measurements in our results are in units of degrees.
- **p. 7 / 5.5. Efficiency - extractive body cue:** Computational time is measured in seconds and is computed by averaging 100 results.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (5. Experiments), p. 8 (Figure/Table caption) |
| Embodiment/environment | ModelNet40: Full Dataset Train & Test In our first experiment, we randomly divide all the point clouds in the ModelNet40 dataset into training and test sets, with no knowledge of the category ... | hardware/simulator version and reset protocol | p. 6 (5. Experiments), p. 6 (5. Experiments) |
| Dataset/benchmark | ModelNet40: Full Dataset Train & Test In our first experiment, we randomly divide all the point clouds in the ModelNet40 dataset into training and test sets, with no knowledge of the category ... | role, split, size and leakage | p. 6 (5. Experiments), p. 6 (5. Experiments) |
| Metric | Ideally, all of these error metrics should be zero if the rigid alignment is perfect. | definition, denominator, direction and uncertainty | p. 6 (5. Experiments), p. 6 (5. Experiments), p. 7 (5.4. DCP Followed By ICP) |
| Baseline/ablation | DCP-v1 already outperforms other methods under all the performance metrics, and DCP-v2 exhibits even stronger performance. | fair input/data/compute/action matching | p. 6 (5. Experiments), p. 5 (5. Experiments), p. 6 (5. Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 5.4. DCP Followed By ICP - extractive body cue:** In large part, this failure is due to the lack of a good initial guess.
- **p. 6 / 5.4. DCP Followed By ICP - extractive body cue:** Since our experiments involve point clouds whose initial poses are far from aligned, ICP fails nearly every experiment we have presented so far.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 5. Ablation study: PointNet or DGCNN? use ICP as a local algorithm by initializing ICP with a rigid transformation output from our DCP model. ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Many modeling and computational challenges hamper the design of a stable and efficient registration method.를 문제로 두고, Contributions: Our contributions include the following: • We identify sub-network architectures designed to address difficulties in the classical ICP pipeline. • We propose a simple architecture to predict a rigid transformation alignin ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Problem Statement), p. 3 (3. Problem Statement), p. 5 (4.5. Loss) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
