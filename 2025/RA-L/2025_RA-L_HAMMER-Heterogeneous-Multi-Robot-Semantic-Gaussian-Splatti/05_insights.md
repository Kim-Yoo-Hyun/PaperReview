# Insights — HAMMER: Heterogeneous, Multi-Robot Semantic Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2501.14147; PDF retrieval source: https://arxiv.org/pdf/2501.14147. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / I. INTRODUCTION - extractive body cue:** A server-based architecture allows our method to be used with existing robot and edge device hardware without highpowered GPUs, while leveraging typical communication infrastructure (e.g.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we propose HAMMER, Heterogeneous Asynchronous Multi-robot Mapping of Environmental Radiance.
- **p. 1 / I. INTRODUCTION - extractive body cue:** HAMMER enables a server communicating with a team of robots to construct a joint 3DGS map of an unknown environment.
- **p. 2 / I. INTRODUCTION - extractive body cue:** A shared map enables these robots to have comprehensive spatial awareness compared to their own local maps.
- **p. 3 / III. METHOD - extractive body cue:** If the fraction of matched features exceeds a fixed ratio ξ = 0.25 then the image pair is accepted as a potential inter-robot correspondence.
- **p. 3 / III. METHOD - extractive body cue:** To perform SfM, we use the COLMAP backend [18] with SuperPoint features and the SuperGlue matcher [28], which have exhibited robustness in aligning images from ...
- **p. 4 / III. METHOD - extractive body cue:** 1) Representation: 3DGS models the opacity and color of the environment using explicit Gaussian primitives, which are optimized based on a differentiable, tile-based rasterization process ...
- **Contribution anchor:** p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHOD), p. 3 (III. METHOD)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** Multi-robot mapping is useful for rapidly exploring new environments, but when combined with traditional 3D reconstruction methods, can be difficult to scale efficiently, especially for ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Alternatively, 3DGS is a promising representation for multi-robot mapping because of its scalability to large environments [8], modeling fidelity, and generalization to a broad range ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Computing requirements for 3DGS training are currently beyond the on-board compute capabilities of most robots and wearables.
- **p. 2 / I. INTRODUCTION - extractive body cue:** HAMMER is designed to generalize to a wide range of robots and devices, combining the advantages of each device into a single map.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** 4) compared to Di-NeRF*, which fails to resolve robot alignments and therefore cannot accurately match the ground-truth images.
- **p. 5 / III. METHOD - extractive body cue:** 3) Pose Refinement: Although the alignment module produces robust estimates of the local-to-world transforms, it cannot account for gradual drift or other temporal noise.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** HAMMER dramatically outperforms Di-NeRF* which fails to converge to accurate inter-robot alignments.
- **Boundary to test:** 4) compared to Di-NeRF*, which fails to resolve robot alignments and therefore cannot accurately match the ground-truth images.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | A server-based architecture allows our method to be used with existing robot and edge device hardware without highpowered GPUs, while leveraging typical communication infrastructure (e.g. | p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Reported outcome | HAMMER dramatically outperforms Di-NeRF* which fails to converge to accurate inter-robot alignments. | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Failure/limitation | 4) compared to Di-NeRF*, which fails to resolve robot alignments and therefore cannot accurately match the ground-truth images. | p. 6 (IV. EXPERIMENTS), p. 5 (III. METHOD) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 During runtime, HAMMER rejects alignments where the localized SfM fails to estimate poses for all 2W input images or alignments that have high translation (0.1m in the map frame) or rotation errors ...를 Each robot produces color images, geometric information (e.g. depth images or point clouds), and camera pose estimates in SE(3) with respect to an arbitrary local coordinate frame T i.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 4) compared to Di-NeRF*, which fails to resolve robot alignments and therefore cannot accurately match the ground-truth images.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: A server-based architecture allows our method to be used with existing robot and edge device hardware without highpowered GPUs, while leveraging typical communication infrastructure (e.g.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Robotics-enabling 3D perception`; tags: `Robotics, Gaussian Splatting, semantic`.
- **Reading predecessor in the generated track queue:** Clio: Real-time Task-Driven Open-Set 3D Scene Graphs (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** VISTA: Open-Vocabulary, Task-Relevant Robot Exploration with Online Semantic Gaussian Splatting (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** 4) compared to Di-NeRF*, which fails to resolve robot alignments and therefore cannot accurately match the ground-truth images.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: However, ReplicaMultiAgent only contains scenes from simulated environments, and lacks heterogeneous robots/sensing devices and challenging real-world scene conditions (e.g. motion blur, diverse lighting)..
3. Compare against the body-reported baseline or a matched simpler baseline: Fig. 5: Map quality over time for HAMMER and baselines in two scenes. HAMMER outperforms Di-NeRF*, demonstrating the necessity of accurate robot alignment. It also outperforms Individuals, highlighting the benefits of collaboration. ....
4. Report the body metric and its denominator/aggregation: First, we compare HAMMER to state-of-the-art baselines [13], [14] by assessing their reconstruction accuracy on the ReplicaMultiAgent dataset [14], [15]..
5. Re-run the body-reported ablation/failure condition: 4) compared to Di-NeRF*, which fails to resolve robot alignments and therefore cannot accurately match the ground-truth images..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD); the primary result is directionally consistent at p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 server-based, architecture, allows mechanism이 Fig. 5: Map quality over time for HAMMER and baselines in two scenes. HAMMER outperforms Di-NeRF*, ... 대비 First, we compare HAMMER to state-of-the-art baselines [13], [14] by assessing their reconstruction accuracy on the ReplicaMultiAgent dataset ...을 개선하고, 4) compared to Di-NeRF*, which fails to resolve robot alignments and therefore cannot accurately match the ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
