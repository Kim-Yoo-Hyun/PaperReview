# Method - Vysics: Object Reconstruction Under Occlusion by Fusing Vision and Contact-Rich Physics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p034.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p034.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (IV. APPROACH), p. 2 (C. Simultaneous Tracking and Shape Reconstruction), p. 4 (IV. APPROACH), p. 2 (C. Simultaneous Tracking and Shape Reconstruction), p. 8 (A. Geometry Reconstruction), p. 3 (C. Simultaneous Tracking and Shape Reconstruction)): Beyond the insights that led to this systems integration, our main contribution lies in how Vysies incorporates these two powerful tools together such that they supervise ‘each other and output ...

## Method Body Digest

- **p. 4 / IV. APPROACH - extractive body cue:** Beyond the insights that led to this systems integration, our main contribution lies in how Vysies incorporates these two powerful tools together such that they ...
- **p. 2 / C. Simultaneous Tracking and Shape Reconstruction - extractive body cue:** Trajectory-Based Dynamics Model Learning
- **p. 4 / IV. APPROACH - extractive body cue:** ‘The basis of our contribution is in how we unify the visible and "physible" geometry measurements together. §IV-A di cusses how vision helps in the ...
- **p. 2 / C. Simultaneous Tracking and Shape Reconstruction - extractive body cue:** ‘System identification is an important robotics subfield that aims to build accurate system models, which can then be leveraged via model-based control techniques.
- **p. 8 / A. Geometry Reconstruction - extractive body cue:** We first compare the geometry reconstruction of our method with that of shape completion models and single-view 3D generation models.
- **p. 3 / C. Simultaneous Tracking and Shape Reconstruction - extractive body cue:** While [56] avoids the problematic gradients in contactrch scenarios by using a gradient-free search over a discrete set of hypothesized geometries, Vysics leverages smooth, implicit-based ...
- **p. 8 / 200.0 BundlesDF - extractive body cue:** The view of the object is heavily occluded by the obstacles (books/blanket), resulting in BundleSDF missing a significant portion of the object in its geometry ...
- **p. 1 / 1. INTRODUCTION - extractive body cue:** portions of its geometry, and observations of the object's state evolution can inject more geometric information when contact,

## Design Rationale

- **p. 1 / 1. INTRODUCTION - extractive body cue:** Fusing vision and contact rich physics, our method recovers the occluded geometry through object interactions with the robot and environment, The robot end effector in ...
- **p. 4 / IV. APPROACH - extractive body cue:** Beyond the insights that led to this systems integration, our main contribution lies in how Vysies incorporates these two powerful tools together such that they ...
- **p. 4 / IV. APPROACH - extractive body cue:** ‘The basis of our contribution is in how we unify the visible and "physible" geometry measurements together. §IV-A di cusses how vision helps in the ...

## Source Evidence Cues

- **p. 4 / IV. APPROACH - extractive body cue:** Beyond the insights that led to this systems integration, our main contribution lies in how Vysies incorporates these two powerful tools together such that they ...
- **p. 2 / C. Simultaneous Tracking and Shape Reconstruction - extractive body cue:** Trajectory-Based Dynamics Model Learning
- **p. 4 / IV. APPROACH - extractive body cue:** ‘The basis of our contribution is in how we unify the visible and "physible" geometry measurements together. §IV-A di cusses how vision helps in the ...
- **p. 2 / C. Simultaneous Tracking and Shape Reconstruction - extractive body cue:** ‘System identification is an important robotics subfield that aims to build accurate system models, which can then be leveraged via model-based control techniques.
- **p. 8 / A. Geometry Reconstruction - extractive body cue:** We first compare the geometry reconstruction of our method with that of shape completion models and single-view 3D generation models.
- **p. 3 / C. Simultaneous Tracking and Shape Reconstruction - extractive body cue:** While [56] avoids the problematic gradients in contactrch scenarios by using a gradient-free search over a discrete set of hypothesized geometries, Vysics leverages smooth, implicit-based ...
- **p. 8 / 200.0 BundlesDF - extractive body cue:** The view of the object is heavily occluded by the obstacles (books/blanket), resulting in BundleSDF missing a significant portion of the object in its geometry ...
- **Detected method headings:** IV. APPROACH (p. 4); model (p. 10)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Beyond the insights that led to this systems integration, our main contribution lies in how Vysies incorporates these two powerful tools together ... | p. 4 (IV. APPROACH), p. 2 (C. Simultaneous Tracking and Shape Reconstruction) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Trajectory-Based Dynamics Model Learning | p. 2 (C. Simultaneous Tracking and Shape Reconstruction), p. 4 (IV. APPROACH) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | ‘The basis of our contribution is in how we unify the visible and "physible" geometry measurements together. §IV-A di cusses how vision ... | p. 4 (IV. APPROACH), p. 2 (C. Simultaneous Tracking and Shape Reconstruction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / C. Simultaneous Tracking and Shape Reconstruction - extractive body cue:** While [56] avoids the problematic gradients in contactrch scenarios by using a gradient-free search over a discrete set of hypothesized geometries, Vysics leverages smooth, implicit-based ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 3 (C. Simultaneous Tracking and Shape Reconstruction).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | portions, geometry, observations, object, state, evolution, inject, more, geometric, information, when, contact, Moreover, advances | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | portions, geometry, observations, object, state, evolution, inject, more, geometric, information | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | Fusing, vision, contact, rich, physics, recovers, occluded, geometry, through, object | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | While, avoids, problematic, gradients, contactrch, scenarios, gradient-free, search, over, discrete | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1. INTRODUCTION - extractive body cue:** portions of its geometry, and observations of the object's state evolution can inject more geometric information when contact,
- **p. 2 / A. Vision-Based Geometry Reconstruction and Completion - extractive body cue:** Moreover, advances in image generation models [54], 3D scene representations [44, 32], and large-scale 3D object datasets [22, 21] have spurred 3D generative pipelines [39, ...
- **p. 4 / IV. APPROACH - extractive body cue:** Referring to the labeled arrows in Figure 3, we obtain the object trajectory (b) and the initial shape estimates (c) from masked input RGBD images ...
- **p. 2 / A. Vision-Based Geometry Reconstruction and Completion - extractive body cue:** prompted camera-frame shape completion from partial point clouds [63, 46] or RGBD observations (69, 37], with recent extensions to multi-object scenes [68, 30].
- **p. 1 / 1. INTRODUCTION - extractive body cue:** This work leverages recent results from visual tracking and object reconstruction [66] in combination with contact-implicit model learning [9, 53] vvia the shared connection of ...
- **p. 4 / IV. APPROACH - extractive body cue:** BundleSDF runs again, fusing both the visible (a) and "physible" data () into a geometric model consistent with both information streams, The final output of ...
- **p. 3 / C. Simultaneous Tracking and Shape Reconstruction - extractive body cue:** The most similar in spirit to Vysics is [56], as they reconstruct geometries with occlusions through physical robot and environment interactions.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | fon the first frame using XMem [17]. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | The third is the temporal IoV of contact activation, which measures the overlap of when the robot-object contact happens in the simulated ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Beyond, insights, systems, integration, main, contribution, lies, Vysies, incorporates, powerful, tools, together, they, supervise, other, output, object, dynamics, model, featuring.
- **Relevant PDF headings:** IV. APPROACH (p. 4); model (p. 10).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | These robot interactions were teleoperated via commanded end effector poses tracked with impedance control. ‘The dataset includes the RGBD videos of the ... | p. 6 (V. EXPERIMENTAL SETUP), p. 6 (V. EXPERIMENTAL SETUP) |
| Semantic / temporal fusion | Fig. 7: A qualitative comparison of the geometry reconstruc tion under heavy occlusion between our method and the vision-only baseline. In the ... | p. 7 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Robot query / planning handoff | Fig. 8: The quantitative comparison of the geometric recon- struction accuracy. Each dot is one session. The results of the | p. 8 (Figure/Table caption), p. 8 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 9 / B. Dynamics Predictions - extractive body cue:** A limitation of Vysics is that it does not incorporate notions of object elasticity or bounciness into the learning problem, ‘This shortcoming means the dynamics ...
- **p. 8 / A. Geometry Reconstruction - extractive body cue:** Under severe occlusion, while the shape completion ‘models can achieve similar or slightly lower chamfer distance than pure vision-based reconstruction, BundleSDF, they fall behind Vysics ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Vision-based shape reconstruction (projection shown in green) can be limited by occlusion. Fusing vision and contact rich physics, our method recovers the occluded ...
- **p. 6 / V. EXPERIMENTAL SETUP - extractive body cue:** There are substantial visual ‘occlusions preventing the camera from directly seeing much of the object geometry.
- **p. 6 / V. EXPERIMENTAL SETUP - extractive body cue:** In the evaluation, we excluded the sessions in which BundleSDF lost track of the object and failed to yield the object trajectory.
- **p. 7 / B. Metrics - extractive body cue:** 7: A qualitative comparison of the geometry reconstruc tion under heavy occlusion between our method and the vision-only baseline.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (IV. APPROACH), p. 2 (C. Simultaneous Tracking and Shape Reconstruction), p. 4 (IV. APPROACH), p. 2 (C. Simultaneous Tracking and Shape Reconstruction), p. 8 (A. Geometry Reconstruction), p. 3 (C. Simultaneous Tracking and Shape Reconstruction), objective p. 3 (C. Simultaneous Tracking and Shape Reconstruction), temporal p. 6 (V. EXPERIMENTAL SETUP), p. 7 (B. Metrics), p. 1 (Abstract), p. 2 (A. Vision-Based Geometry Reconstruction and Completion), p. 2 (B. Vision-Based Object Pose Estimation), p. 3 (B. Physics-Inspired Dynamics Learning).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
