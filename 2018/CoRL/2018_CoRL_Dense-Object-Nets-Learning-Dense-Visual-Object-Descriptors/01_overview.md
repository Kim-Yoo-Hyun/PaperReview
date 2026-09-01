# Dense Object Nets: Learning Dense Visual Object Descriptors By and For Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v87/florence18a.html.
> PDF retrieval source: https://proceedings.mlr.press/v87/florence18a.html. Reading tracker status/evidence was not changed.

- Year/Venue: 2018 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, manipulation, Dense Descriptors, representation learning
- Official paper: https://proceedings.mlr.press/v87/florence18a.html
- Full-text retrieval: https://proceedings.mlr.press/v87/florence18a.html
- Code/Project: https://dense-object-nets.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 At a coarse level the task of identifying individual objects to manipulate can be solved by instance segmentation, as demonstrated in the Amazon Robotics Challenge (ARC) [4, 5] or [6].를 문제로 두고, We believe our largest contribution is that we introduce dense descriptors as a representation useful for robotic manipulation.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** What is the right object representation for manipulation?
- **p. 1 / Abstract - extractive body cue:** We would like robots to visually perceive scenes and learn an understanding of the objects in them that (i) is task-agnostic and can be used ...
- **p. 1 / Abstract - extractive body cue:** This is hard to achieve with previous methods: much recent work in grasping does not extend to grasping specific objects or other tasks, whereas task-specific ...
- **p. 1 / Abstract - extractive body cue:** In this paper we present Dense Object Nets, which build on recent developments in self-supervised dense descriptor learning, as a consistent object representation for visual ...
- **p. 1 / Abstract - extractive body cue:** We demonstrate they can be trained quickly (approximately 20 minutes) for a wide variety of previously unseen and potentially non-rigid objects.
- **p. 1 / 1 Introduction - extractive body cue:** At a coarse level the task of identifying individual objects to manipulate can be solved by instance segmentation, as demonstrated in the Amazon Robotics Challenge ...
- **p. 1 / 1 Introduction - extractive body cue:** Achieving specificity, the ability to accomplish specific tasks with specific objects, may require solving the data association problem.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** We believe our largest contribution is that we introduce dense descriptors as a representation useful for robotic manipulation.
- **p. 1 / 1 Introduction - extractive body cue:** In this paper, we propose and demonstrate using dense visual description as a representation for robotic manipulation.
- **p. 4 / 3 Methodology - extractive body cue:** To achieve distinctness, we introduce three strategies: i.
- **p. 1 / 1 Introduction - extractive body cue:** Towards this goal, we also provide practical contributions to dense visual descriptor learning with general computer Code, data, and video available: github.com/RobotLocomotion/pytorch-dense-correspondence 2nd Conference on ...
- **p. 4 / 3 Methodology - extractive body cue:** We want to emphasize that automatic object masking enables many other techniques in this paper, including: background domain randomization, cross-object loss, and synthetic multi-object scenes.
- **p. 2 / 3 Methodology - extractive body cue:** 3.1 Preliminary: Self-Supervised Pixelwise Contrastive Loss We use self-supervised pixelwise contrastive loss, as developed in [7, 8].
- **p. 5 / 3 Methodology - extractive body cue:** In this work, we use only static-scene reconstructions, so pixel matches between images can be easily found by raycasting and reprojecting against the dense 3D ...
- **p. 3 / 3 Methodology - extractive body cue:** Since we are trying to learn descriptors of objects that take up only a fraction of a full image, we observe significant improvements if the ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Since we are trying to learn descriptors of objects that take up only a fraction of a full image, we observe significant improvements if the representational power of the models are focused ... | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (3 Methodology), p. 5 (3 Methodology) |
| State/latent | Since, trying, learn, descriptors, objects, take, only, fraction, full, image, observe, significant | geometry, map, object/relationship state | p. 3 (3 Methodology), p. 5 (3 Methodology), p. 4 (3 Methodology) |
| Output/action | For dense reconstruction we use TSDF fusion [27] of the depth images with camera poses provided by forward kinematics. | point map, pose, scene graph, affordance 또는 query result | p. 5 (3 Methodology), p. 4 (3 Methodology), p. 3 (3 Methodology) |
| Objective/outcome | The loss function aims to minimize the distance between descriptors corresponding to a match, while descriptors corresponding to a non-match should be at least a distance M apart, where M is a ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 3 (3 Methodology), p. 2 (3 Methodology), p. 3 (3 Methodology) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** We believe our largest contribution is that we introduce dense descriptors as a representation useful for robotic manipulation.
- **p. 1 / 1 Introduction - extractive body cue:** In this paper, we propose and demonstrate using dense visual description as a representation for robotic manipulation.
- **p. 4 / 3 Methodology - extractive body cue:** To achieve distinctness, we introduce three strategies: i.
- **p. 1 / 1 Introduction - extractive body cue:** Towards this goal, we also provide practical contributions to dense visual descriptor learning with general computer Code, data, and video available: github.com/RobotLocomotion/pytorch-dense-correspondence 2nd Conference on ...
- **p. 4 / 3 Methodology - extractive body cue:** We want to emphasize that automatic object masking enables many other techniques in this paper, including: background domain randomization, cross-object loss, and synthetic multi-object scenes.
- **p. 7 / 5 Results - extractive body cue:** For the most part, 3dimensional descriptor spaces were sufficient to achieve saturated (did not improve with higher-dimension) correspondence precision for single objects, yet this is ...
- **p. 6 / 5 Results - extractive body cue:** Our new standard single-object training procedure (standard-SO) performs significantly better than our implementation of prior work's training procedures (Schmidt), and we isolate and measure significant ...
- **p. 7 / 5 Results - extractive body cue:** Given that we can separate objects in descriptor space, we next investigate: does the introduction of object distinctness significantly limit the ability of the models ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (5 Results), p. 6 (5 Results) |
| Embodiment/environment | The dataset used for (a) is of three objects, 4 scenes each. | hardware/simulator version and reset protocol | p. 6 (5 Results), p. 8 (5 Results) |
| Dataset/benchmark | (b) shows that for a dataset containing 10 scenes of a drill, learned descriptors are inconsistent without background and orientation randomization during training (middle), but consistent with them (right). the same network ... | role, split, size and leakage | p. 6 (5 Results), p. 8 (5 Results), p. 6 (5 Results), p. 8 (5 Results) |
| Metric | By applying cross-object loss (Section 3.3.i, training mode specific in Figure 3a), we can convincingly separate multiple objects such that they each occupy distinct subsets of descriptor space (Figure 5b). | definition, denominator, direction and uncertainty | p. 7 (5 Results), p. 7 (5 Results), p. 5 (5 Results) |
| Baseline/ablation | without cross-object loss with cross-object loss (a) (b) (c) Figure 5: Comparison of training without any distinct object loss (a) vs. using cross-object loss (b). | fair input/data/compute/action matching | p. 7 (5 Results), p. 6 (5 Results), p. 6 (5 Results) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 5 Results - extractive body cue:** The generalization extends to instances that a priori we thought would be failure modes: we expected the boot (Figure 6h) to be a failure mode ...
- **p. 8 / 6 Conclusion - extractive body cue:** In future work we are interested to explore new approaches to solving manipulation problems that exploit the dense visual information that learned dense descriptors provide, ...

## Why Read It

Manipulation, contact, tactile, and dexterity의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 At a coarse level the task of identifying individual objects to manipulate can be solved by instance segmentation, as demonstrated in the Amazon Robotics Challenge (ARC) [4, 5] or [6].를 문제로 두고, We believe our largest contribution is that we introduce dense descriptors as a representation useful for robotic manipulation.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 2 (3 Methodology), p. 5 (3 Methodology) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
