# Insights — Vysics: Object Reconstruction Under Occlusion by Fusing Vision and Contact-Rich Physics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p034.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p034.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / 1. INTRODUCTION - extractive body cue:** Fusing vision and contact rich physics, our method recovers the occluded geometry through object interactions with the robot and environment, The robot end effector in ...
- **p. 4 / IV. APPROACH - extractive body cue:** Beyond the insights that led to this systems integration, our main contribution lies in how Vysies incorporates these two powerful tools together such that they ...
- **p. 4 / IV. APPROACH - extractive body cue:** ‘The basis of our contribution is in how we unify the visible and "physible" geometry measurements together. §IV-A di cusses how vision helps in the ...
- **p. 8 / A. Geometry Reconstruction - extractive body cue:** We first compare the geometry reconstruction of our method with that of shape completion models and single-view 3D generation models.
- **p. 8 / 200.0 BundlesDF - extractive body cue:** Our method recovers the occluded geometry through physics-based reasoning over the observed trajectories, substantially and consistently improving the geometric accuracy in both metrics.
- **p. 2 / C. Simultaneous Tracking and Shape Reconstruction - extractive body cue:** Trajectory-Based Dynamics Model Learning
- **p. 2 / C. Simultaneous Tracking and Shape Reconstruction - extractive body cue:** ‘System identification is an important robotics subfield that aims to build accurate system models, which can then be leveraged via model-based control techniques.
- **Contribution anchor:** p. 1 (1. INTRODUCTION), p. 4 (IV. APPROACH), p. 4 (IV. APPROACH), p. 8 (A. Geometry Reconstruction), p. 8 (200.0 BundlesDF), p. 2 (C. Simultaneous Tracking and Shape Reconstruction)

### Strongest assumption and failure boundary

- **p. 1 / 1. INTRODUCTION - extractive body cue:** Estimating geometry through contact-rich interactions is not a trivial problem.
- **p. 1 / 1. INTRODUCTION - extractive body cue:** While some might be recognized from an existing database, others will require physical interaction to be newly understood on the spot.
- **p. 9 / B. Dynamics Predictions - extractive body cue:** A limitation of Vysics is that it does not incorporate notions of object elasticity or bounciness into the learning problem, ‘This shortcoming means the dynamics ...
- **p. 8 / A. Geometry Reconstruction - extractive body cue:** Under severe occlusion, while the shape completion ‘models can achieve similar or slightly lower chamfer distance than pure vision-based reconstruction, BundleSDF, they fall behind Vysics ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Vision-based shape reconstruction (projection shown in green) can be limited by occlusion. Fusing vision and contact rich physics, our method recovers the occluded ...
- **p. 6 / V. EXPERIMENTAL SETUP - extractive body cue:** There are substantial visual ‘occlusions preventing the camera from directly seeing much of the object geometry.
- **p. 6 / V. EXPERIMENTAL SETUP - extractive body cue:** In the evaluation, we excluded the sessions in which BundleSDF lost track of the object and failed to yield the object trajectory.
- **Boundary to test:** A limitation of Vysics is that it does not incorporate notions of object elasticity or bounciness into the learning problem, ‘This shortcoming means the dynamics predictions of our earned models could deviate ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Fusing vision and contact rich physics, our method recovers the occluded geometry through object interactions with the robot and environment, The robot end effector in yellow shows the robot-object interaction, | p. 1 (1. INTRODUCTION), p. 4 (IV. APPROACH) |
| Reported outcome | Fig. 8: The quantitative comparison of the geometric recon- struction accuracy. Each dot is one session. The results of the | p. 8 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Failure/limitation | A limitation of Vysics is that it does not incorporate notions of object elasticity or bounciness into the learning problem, ‘This shortcoming means the dynamics predictions of our earned models could deviate ... | p. 9 (B. Dynamics Predictions), p. 8 (A. Geometry Reconstruction) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 portions of its geometry, and observations of the object's state evolution can inject more geometric information when contact,를 Moreover, advances in image generation models [54], 3D scene representations [44, 32], and large-scale 3D object datasets [22, 21] have spurred 3D generative pipelines [39, 42, 27, 38, 71, 76), though these ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 A limitation of Vysics is that it does not incorporate notions of object elasticity or bounciness into the learning problem, ‘This shortcoming means the dynamics predictions of our earned models could deviate ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Fusing vision and contact rich physics, our method recovers the occluded geometry through object interactions with the robot and environment, The robot end effector in yellow shows the robot-object interaction,
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Robotics-enabling 3D perception`; tags: `Robotics, 3D perception, object reconstruction, contact-rich manipulation, dynamics, occlusion`.
- **Reading predecessor in the generated track queue:** PointVLA: Injecting the 3D World into Vision-Language-Action Models (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Act the Part: Learning Interaction Strategies for Articulated Object Part Discovery (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** A limitation of Vysics is that it does not incorporate notions of object elasticity or bounciness into the learning problem, ‘This shortcoming means the dynamics predictions of our earned models could deviate ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: These robot interactions were teleoperated via commanded end effector poses tracked with impedance control. ‘The dataset includes the RGBD videos of the objects in interactions with object ‘mask annotations, as well as ....
3. Compare against the body-reported baseline or a matched simpler baseline: Fig. 7: A qualitative comparison of the geometry reconstruc tion under heavy occlusion between our method and the vision-only baseline. In the image view, the mesh projection is shown in green, and ....
4. Report the body metric and its denominator/aggregation: Fig. 9: The quantitative comparison of the dynamics prediction accuracy in pose error. Trajectories are predicted by replaying the robot interaction with the estimated geometry in simula- tion.
5. Re-run the body-reported ablation/failure condition: A limitation of Vysics is that it does not incorporate notions of object elasticity or bounciness into the learning problem, ‘This shortcoming means the dynamics predictions of our earned models could deviate ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (IV. APPROACH), p. 2 (C. Simultaneous Tracking and Shape Reconstruction), p. 4 (IV. APPROACH); the primary result is directionally consistent at p. 8 (Figure/Table caption), p. 8 (Figure/Table caption), p. 9 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Fusing, vision, contact mechanism이 Fig. 7: A qualitative comparison of the geometry reconstruc tion under heavy occlusion between our method ... 대비 Fig. 9: The quantitative comparison of the dynamics prediction accuracy in pose error. Trajectories are predicted by replaying ...을 개선하고, A limitation of Vysics is that it does not incorporate notions of object elasticity or bounciness ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
