# Method - Dense Object Nets: Learning Dense Visual Object Descriptors By and For Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v87/florence18a.html; PDF retrieval source: https://proceedings.mlr.press/v87/florence18a.html. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 2 (3 Methodology), p. 5 (3 Methodology), p. 3 (3 Methodology), p. 4 (3 Methodology), p. 5 (3 Methodology), p. 3 (3 Methodology)): 3.1 Preliminary: Self-Supervised Pixelwise Contrastive Loss We use self-supervised pixelwise contrastive loss, as developed in [7, 8].

## Method Body Digest

- **p. 2 / 3 Methodology - extractive body cue:** 3.1 Preliminary: Self-Supervised Pixelwise Contrastive Loss We use self-supervised pixelwise contrastive loss, as developed in [7, 8].
- **p. 5 / 3 Methodology - extractive body cue:** In this work, we use only static-scene reconstructions, so pixel matches between images can be easily found by raycasting and reprojecting against the dense 3D ...
- **p. 3 / 3 Methodology - extractive body cue:** Since we are trying to learn descriptors of objects that take up only a fraction of a full image, we observe significant improvements if the ...
- **p. 4 / 3 Methodology - extractive body cue:** When we began this work it wasn't obvious to us what scale of changes to our training procedure or model architecture would be required in ...
- **p. 5 / 3 Methodology - extractive body cue:** For training, at each iteration we randomly sample between some subset of specified image comparison types (Single Object Within Scene, Different Object Across Scene, Multi ...
- **p. 3 / 3 Methodology - extractive body cue:** (a) Robot-Automated Data Collection (b) 3D Reconstruction based Change Detection and Masked Sampling (d) Cross Object Loss (e) Direct Multi Object (f) Synthetic Multi Object ...
- **p. 4 / 3 Methodology - extractive body cue:** 3.3 Multi-Object Dense Descriptors We of course would like robots to have dense visual models of more than just one object.
- **p. 3 / 3 Methodology - extractive body cue:** The loss function aims to minimize the distance between descriptors corresponding to a match, while descriptors corresponding to a non-match should be at least a ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** We believe our largest contribution is that we introduce dense descriptors as a representation useful for robotic manipulation.
- **p. 1 / 1 Introduction - extractive body cue:** In this paper, we propose and demonstrate using dense visual description as a representation for robotic manipulation.
- **p. 4 / 3 Methodology - extractive body cue:** To achieve distinctness, we introduce three strategies: i.

## Source Evidence Cues

- **p. 2 / 3 Methodology - extractive body cue:** 3.1 Preliminary: Self-Supervised Pixelwise Contrastive Loss We use self-supervised pixelwise contrastive loss, as developed in [7, 8].
- **p. 5 / 3 Methodology - extractive body cue:** In this work, we use only static-scene reconstructions, so pixel matches between images can be easily found by raycasting and reprojecting against the dense 3D ...
- **p. 3 / 3 Methodology - extractive body cue:** Since we are trying to learn descriptors of objects that take up only a fraction of a full image, we observe significant improvements if the ...
- **p. 4 / 3 Methodology - extractive body cue:** When we began this work it wasn't obvious to us what scale of changes to our training procedure or model architecture would be required in ...
- **p. 5 / 3 Methodology - extractive body cue:** For training, at each iteration we randomly sample between some subset of specified image comparison types (Single Object Within Scene, Different Object Across Scene, Multi ...
- **p. 3 / 3 Methodology - extractive body cue:** (a) Robot-Automated Data Collection (b) 3D Reconstruction based Change Detection and Masked Sampling (d) Cross Object Loss (e) Direct Multi Object (f) Synthetic Multi Object ...
- **p. 4 / 3 Methodology - extractive body cue:** 3.3 Multi-Object Dense Descriptors We of course would like robots to have dense visual models of more than just one object.
- **Detected method headings:** 3 Methodology (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | 3.1 Preliminary: Self-Supervised Pixelwise Contrastive Loss We use self-supervised pixelwise contrastive loss, as developed in [7, 8]. | p. 2 (3 Methodology), p. 5 (3 Methodology) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | In this work, we use only static-scene reconstructions, so pixel matches between images can be easily found by raycasting and reprojecting against ... | p. 5 (3 Methodology), p. 3 (3 Methodology) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Since we are trying to learn descriptors of objects that take up only a fraction of a full image, we observe significant ... | p. 3 (3 Methodology), p. 4 (3 Methodology) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3 Methodology - extractive body cue:** The loss function aims to minimize the distance between descriptors corresponding to a match, while descriptors corresponding to a non-match should be at least a ...
- **p. 2 / 3 Methodology - extractive body cue:** 3.1 Preliminary: Self-Supervised Pixelwise Contrastive Loss We use self-supervised pixelwise contrastive loss, as developed in [7, 8].
- **p. 3 / 3 Methodology - extractive body cue:** The dense descriptor mapping is trained via pixelwise contrastive loss.
- **p. 4 / 3 Methodology - extractive body cue:** The most direct way to ensure that different objects occupy different subsets of descriptor space is to directly impose cross-object loss (Figure 1d).
- **p. 4 / 3 Methodology - extractive body cue:** With pixel-level data associations provided instead by 3D geometry, the sampling of matches and the loss function still makes sense, even in clutter. iii.
- **p. 5 / 3 Methodology - extractive body cue:** In this work, we use only static-scene reconstructions, so pixel matches between images can be easily found by raycasting and reprojecting against the dense 3D ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 3 (3 Methodology), p. 2 (3 Methodology), p. 3 (3 Methodology), p. 4 (3 Methodology), p. 4 (3 Methodology), p. 5 (3 Methodology).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Since, trying, learn, descriptors, objects, take, only, fraction, full, image, observe, significant, improvements, representational | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Since, trying, learn, descriptors, objects, take, only, fraction, full, image | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | believe, largest, contribution, introduce, dense, descriptors, representation, useful, robotic, manipulation | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | loss, function, aims, minimize, distance, between, descriptors, corresponding, match, while | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3 Methodology - extractive body cue:** Since we are trying to learn descriptors of objects that take up only a fraction of a full image, we observe significant improvements if the ...
- **p. 5 / 3 Methodology - extractive body cue:** For dense reconstruction we use TSDF fusion [27] of the depth images with camera poses provided by forward kinematics.
- **p. 4 / 3 Methodology - extractive body cue:** In order to provide autonomous object masking without any human input, we leverage our 3D reconstructions and results from the literature on 3D change detection ...
- **p. 3 / 3 Methodology - extractive body cue:** The dense descriptor mapping f(·) is used to map an image I ∈RW×H×3 to descriptor space f(I)∈RW×H×D.
- **p. 5 / 3 Methodology - extractive body cue:** We employ a Schunk two-finger gripper and plan grasps directly on the object point cloud (Appendix C).
- **p. 1 / 1 Introduction - extractive body cue:** Towards this goal, we also provide practical contributions to dense visual descriptor learning with general computer Code, data, and video available: github.com/RobotLocomotion/pytorch-dense-correspondence 2nd Conference on ...
- **p. 4 / 3 Methodology - extractive body cue:** We also applied synthetic 180-degree rotations randomly to our images.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Projecting this geometry into each camera frame yields object masks for each image. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | We employ a Schunk two-finger gripper and plan grasps directly on the object point cloud (Appendix C). | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3 Methodology - extractive body cue:** In this work, we use only static-scene reconstructions, so pixel matches between images can be easily found by raycasting and reprojecting against the dense 3D ...
- **p. 4 / 3 Methodology - extractive body cue:** When we began this work it wasn't obvious to us what scale of changes to our training procedure or model architecture would be required in ...
- **p. 5 / 3 Methodology - extractive body cue:** For training, at each iteration we randomly sample between some subset of specified image comparison types (Single Object Within Scene, Different Object Across Scene, Multi ...
- **p. 3 / 3 Methodology - extractive body cue:** (a) Robot-Automated Data Collection (b) 3D Reconstruction based Change Detection and Masked Sampling (d) Cross Object Loss (e) Direct Multi Object (f) Synthetic Multi Object ...
- **p. 6 / 5 Results - extractive body cue:** Our new standard single-object training procedure (standard-SO) performs significantly better than our implementation of prior work's training procedures (Schmidt), and we isolate and measure significant ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Preliminary, Self-Supervised, Pixelwise, Contrastive, Loss, developed, only, static-scene, reconstructions, pixel, matches, between, images, easily, found, raycasting, reprojecting, against, dense, reconstruction.
- **Relevant PDF headings:** 3 Methodology (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | The dataset used for (a) is of three objects, 4 scenes each. | p. 6 (5 Results), p. 8 (5 Results) |
| Semantic / temporal fusion | without cross-object loss with cross-object loss (a) (b) (c) Figure 5: Comparison of training without any distinct object loss (a) vs. using ... | p. 7 (5 Results), p. 6 (5 Results) |
| Robot query / planning handoff | For the most part, 3dimensional descriptor spaces were sufficient to achieve saturated (did not improve with higher-dimension) correspondence precision for single objects, ... | p. 7 (5 Results), p. 6 (5 Results) |

## Failure and Ablation Link

- **p. 5 / 5 Results - extractive body cue:** 5.1 Single-Object Dense Descriptors We observe that with our training procedures described in Section 3.2, for a wide variety of objects we can acquire dense ...
- **p. 6 / 5 Results - extractive body cue:** (b) shows that for a dataset containing 10 scenes of a drill, learned descriptors are inconsistent without background and orientation randomization during training (middle), but ...
- **p. 6 / 5 Results - extractive body cue:** Image #1 (cropped) (i) Without orientation and background randomization Image #2 (cropped) (ii) standard-SO inconsistent consistent (a) (b) Figure 4: (a), with same axes as ...
- **p. 7 / 5 Results - extractive body cue:** without cross-object loss with cross-object loss (a) (b) (c) Figure 5: Comparison of training without any distinct object loss (a) vs. using cross-object loss (b).
- **p. 7 / 5 Results - extractive body cue:** Networks with a number label were trained with cross object loss and the number denotes the descriptor dimension. no-cross-object is a network trained without cross ...
- **p. 8 / 5 Results - extractive body cue:** The particular novel components of these manipulation demonstrations are in grasping the visual corresponding points for arbitrary pixels that are either in different (potentially deformed) ...
- **p. 7 / 5 Results - extractive body cue:** The generalization extends to instances that a priori we thought would be failure modes: we expected the boot (Figure 6h) to be a failure mode ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 2 (3 Methodology), p. 5 (3 Methodology), p. 3 (3 Methodology), p. 4 (3 Methodology), p. 5 (3 Methodology), p. 3 (3 Methodology), objective p. 3 (3 Methodology), p. 2 (3 Methodology), p. 3 (3 Methodology), p. 4 (3 Methodology), p. 4 (3 Methodology), p. 5 (3 Methodology), temporal p. 4 (3 Methodology), p. 5 (3 Methodology), p. 5 (5 Results).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
