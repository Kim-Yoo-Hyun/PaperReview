# MonoScene: Monocular 3D Semantic Scene Completion

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2112.00726.
> PDF retrieval source: https://arxiv.org/pdf/2112.00726. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2022 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Vision, semantic, occupancy, monocular geometry
- Official paper: https://arxiv.org/abs/2112.00726
- Full-text retrieval: https://arxiv.org/pdf/2112.00726
- Code/Project: https://github.com/cv-rits/MonoScene
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 The SSC literature mainly relies on cross-entropy loss which considers each voxel independently, lacking context awareness.를 문제로 두고, Our framework infers dense semantic scenes, hallucinating scenery outside the field of view of the image (dark voxels, right). and outdoor scenes.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** MonoScene proposes a 3D Semantic Scene Completion (SSC) framework, where the dense geometry and semantics of a scene are inferred from a single monocular RGB ...
- **p. 1 / Abstract - extractive body cue:** Different from the SSC literature, relying on 2.5 or 3D input, we solve the complex problem of 2D to 3D scene reconstruction while jointly inferring ...
- **p. 1 / Abstract - extractive body cue:** Our framework relies on successive 2D and 3D UNets, bridged by a novel 2D3D features projection inspired by optics, and introduces a 3D context relation ...
- **p. 1 / Abstract - extractive body cue:** Along with architectural contributions, we introduce novel global scene and local frustums losses.
- **p. 1 / Abstract - extractive body cue:** Experiments show we outperform the literature on all metrics and datasets while hallucinating plausible scenery even beyond the camera field of view.
- **p. 1 / 1. Introduction - extractive body cue:** The SSC literature mainly relies on cross-entropy loss which considers each voxel independently, lacking context awareness.

## Core Idea

- **p. 1 / 1. Introduction - extractive body cue:** Our framework infers dense semantic scenes, hallucinating scenery outside the field of view of the image (dark voxels, right). and outdoor scenes.
- **p. 1 / 1. Introduction - extractive body cue:** Here, we present MonoScene which - unlike the literature - relies on a single RGB image to infer the dense 3D voxelized semantic scene working ...
- **p. 2 / 3. Method - extractive body cue:** To guide the SSC training, we introduce new complementary losses.
- **p. 3 / 3.2. 3D Context Relation Prior (3D CRP) - extractive body cue:** As voxels relations are greedy with N 2 relations for N voxels, we present the lighter supervoxel↔voxel relations.
- **p. 3 / 3.2. 3D Context Relation Prior (3D CRP) - extractive body cue:** Here, we propose a 3D Context Relation Prior (3D CRP) layer, inserted at the 3D UNet bottleneck, which learns n-way voxel↔voxel semantic scene-wise relation maps.
- **p. 3 / 3.1. Features Line of Sight Projection (FLoSP) - extractive body cue:** We argue this enables 2D-3D disentangled representations, providing the 3D network with the freedom to use high-level 2D features for fine-grained 3D disambiguation.
- **p. 2 / 3. Method - extractive body cue:** First, a Scene-Class Affinity Loss (Sec.
- **p. 3 / 3.2. 3D Context Relation Prior (3D CRP) - extractive body cue:** We then optimize a weighted multilabel binary cross entropy loss: Lrel=- X m∈M,i [(1-Am i ) log(1- ˆAm i )+wmAm i log ˆAm i ], ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The output map F3D is used as 3D UNet input. | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (3.1. Features Line of Sight Projection (FLoSP)), p. 2 (3. Method) |
| State/latent | output, F3D, UNet, input, been, almost, exclusively, addressed, inputs, point, cloud, depth | geometry, map, object/relationship state | p. 3 (3.1. Features Line of Sight Projection (FLoSP)), p. 2 (3. Method), p. 2 (3. Method) |
| Output/action | This has been almost exclusively addressed with 2.5D or 3D inputs [56], such as point cloud, depth or else, which act as strong geometrical cues. | point map, pose, scene graph, affordance 또는 query result | p. 2 (3. Method), p. 2 (3. Method), p. 3 (3.2. 3D Context Relation Prior (3D CRP)) |
| Objective/outcome | For more generality, our loss Lscal maximizes the above class-wise metrics with: Lscal(ˆp, p) = -1 | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (3.3. Losses), p. 3 (3.2. 3D Context Relation Prior (3D CRP)), p. 4 (3.4. Training strategy) |

## Main Claims and Actual Contribution

- **p. 1 / 1. Introduction - extractive body cue:** Our framework infers dense semantic scenes, hallucinating scenery outside the field of view of the image (dark voxels, right). and outdoor scenes.
- **p. 1 / 1. Introduction - extractive body cue:** Here, we present MonoScene which - unlike the literature - relies on a single RGB image to infer the dense 3D voxelized semantic scene working ...
- **p. 2 / 3. Method - extractive body cue:** To guide the SSC training, we introduce new complementary losses.
- **p. 3 / 3.2. 3D Context Relation Prior (3D CRP) - extractive body cue:** As voxels relations are greedy with N 2 relations for N voxels, we present the lighter supervoxel↔voxel relations.
- **p. 3 / 3.2. 3D Context Relation Prior (3D CRP) - extractive body cue:** Here, we propose a 3D Context Relation Prior (3D CRP) layer, inserted at the 3D UNet bottleneck, which learns n-way voxel↔voxel semantic scene-wise relation maps.
- **p. 6 / 4.2.1 Evaluation - extractive body cue:** Despite the various indoor and outdoor setups, we significantly outperform other RGB-inferred baselines, in both mIoU and IoU.
- **p. 5 / 4.2.1 Evaluation - extractive body cue:** On both datasets we outperform all methods by a significant mIoU margin of +4.03 on NYUv2 (Tab.
- **p. 5 / 4. Experiments - extractive body cue:** Note the strong interaction between IoU and mIoU since better geometry estimation (i.e. high IoU) can be achieved by invalidating semantic labels (i.e. low mIoU).

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (4.2.1 Evaluation), p. 5 (4.2.1 Evaluation) |
| Embodiment/environment | We evaluate MonoScene on popular real-world SSC datasets being, indoor NYUv2 [58] and outdoor Se4 | hardware/simulator version and reset protocol | p. 4 (4. Experiments), p. 5 (4.2.1 Evaluation) |
| Dataset/benchmark | On individual classes, MonoScene performs either best or second, excelling on large structural classes for both datasets (e.g. floor, wall ; road, building). | role, split, size and leakage | p. 4 (4. Experiments), p. 5 (4.2.1 Evaluation), p. 5 (4.2.1 Evaluation), p. 7 (4.2.1 Evaluation) |
| Metric | We report the performance on semantic scene completion (SSC - mIoU) and scene completion (SC - IoU) for RGB-inferred baselines and our method. | definition, denominator, direction and uncertainty | p. 6 (4.2.1 Evaluation), p. 5 (4.2.1 Evaluation), p. 5 (4. Experiments) |
| Baseline/ablation | 7b), compared to baselines, MonoScene evidently captures better the scene layout, e.g. cross-roads (rows 1,3). | fair input/data/compute/action matching | p. 5 (4.2.1 Evaluation), p. 6 (4.2.1 Evaluation), p. 6 (4.2.1 Evaluation) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 5. Discussion - extractive body cue:** Compared to the Whole Scene, the in-FOV performance is higher since it considers visible surfaces, whereas the out-FOV performance is significantly lower since the image ...
- **p. 8 / 5. Discussion - extractive body cue:** Due to the single viewpoint, occlusion artefacts such as distortions are visible along the line of sight in outdoor scenes.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. MonoScene framework. We infer 3D SSC from a single RGB image, leveraging 2D and 3D UNets, bridged by our Features Line of Sight ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 6. Frustum Proportion Loss. Considering an image di- vided into same-size 2D patches (here, 2×2), each corresponds to a 3D frustum in the scene, ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 The SSC literature mainly relies on cross-entropy loss which considers each voxel independently, lacking context awareness.를 문제로 두고, Our framework infers dense semantic scenes, hallucinating scenery outside the field of view of the image (dark voxels, right). and outdoor scenes.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (3. Method), p. 3 (3.1. Features Line of Sight Projection (FLoSP)), p. 2 (3. Method), p. 3 (3.2. 3D Context Relation Prior (3D CRP)) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
