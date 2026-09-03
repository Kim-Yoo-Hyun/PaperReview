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

- **Paper-specific interface:** Specifically, if a depth image is received, then the camera intrinsics and pose are used to project random pixels into 3D to create a sparse point cloud. (p. 4, III. METHOD).
- **Paper-specific mechanism:** In this work, we propose HAMMER, Heterogeneous Asynchronous Multi-robot Mapping of Environmental Radiance. (p. 1, I. INTRODUCTION).
- **Evidence boundary:** the reported outcome is Therefore, to showcase the generalizability of HAMMER and its real-time deployment in real-world environments, we also assess its performance in two different hardware trials with data collected using real robots. (p. 5, IV. EXPERIMENTS); the relevant task/metric cue is Therefore, to showcase the generalizability of HAMMER and its real-time deployment in real-world environments, we also assess its performance in two different hardware trials with data collected using real robots. (p. 5, IV. EXPERIMENTS). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** 4) compared to Di-NeRF*, which fails to resolve robot alignments and therefore cannot accurately match the ground-truth images. (p. 6, IV. EXPERIMENTS).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Robotics-enabling 3D perception`; tags: `Robotics, Gaussian Splatting, semantic`.
- **Reading predecessor in the generated track queue:** Clio: Real-time Task-Driven Open-Set 3D Scene Graphs (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** VISTA: Open-Vocabulary, Task-Relevant Robot Exploration with Online Semantic Gaussian Splatting (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** 4) compared to Di-NeRF*, which fails to resolve robot alignments and therefore cannot accurately match the ground-truth images.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Specifically, if a depth image is received, then the camera intrinsics and pose are used to project random pixels into 3D to create a sparse point cloud. (p. 4, III. METHOD); preserve the objective/update rule: Equation (1) optimizes the scaling, rotation, and translation (s, R, t) between the two frames with a small regularization term on the rotation to address degenerate data. (p. 3, III. METHOD).
2. Use the paper-reported task/data/environment cue: Therefore, to showcase the generalizability of HAMMER and its real-time deployment in real-world environments, we also assess its performance in two different hardware trials with data collected using real robots. (p. 5, IV. EXPERIMENTS).
3. Compare against the reported or matched baseline: HAMMER outperforms both baselines on all averaged metrics, and does so at least 25× faster than CPSLAM and 16× faster than MAGiC-SLAM. (p. 6, IV. EXPERIMENTS).
4. Report the body metric with its denominator and aggregation: Therefore, to showcase the generalizability of HAMMER and its real-time deployment in real-world environments, we also assess its performance in two different hardware trials with data collected using real robots. (p. 5, IV. EXPERIMENTS).
5. Re-run the reported ablation or stress/failure condition: Therefore, to showcase the generalizability of HAMMER and its real-time deployment in real-world environments, we also assess its performance in two different hardware trials with data collected using real robots. (p. 5, IV. EXPERIMENTS); if none is reported, design one around: 4) compared to Di-NeRF*, which fails to resolve robot alignments and therefore cannot accurately match the ground-truth images. (p. 6, IV. EXPERIMENTS).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), match the reported outcome at p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), and measure the boundary at p. 6 (IV. EXPERIMENTS), p. 7 (V. CONCLUSION AND LIMITATIONS).

## Falsifiable research question

Under the paper's stated interface (Specifically, if a depth image is received, then the camera intrinsics and pose are used to project random pixels into 3D to ...), does the paper-specific mechanism (In this work, we propose HAMMER, Heterogeneous Asynchronous Multi-robot Mapping of Environmental Radiance.) retain the reported evaluation outcome (Therefore, to showcase the generalizability of HAMMER and its real-time deployment in real-world environments, we also assess its ...) when tested against the paper's strongest explicit boundary (4) compared to Di-NeRF*, which fails to resolve robot alignments and therefore cannot accurately match the ground-truth images.)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Therefore, to showcase the generalizability of HAMMER and its real-time deployment in real-world environments, we also assess its ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** In this work, we propose HAMMER, Heterogeneous Asynchronous Multi-robot Mapping of Environmental Radiance. (p. 1, I. INTRODUCTION).
- **Paper-supported outcome:** Therefore, to showcase the generalizability of HAMMER and its real-time deployment in real-world environments, we also assess its performance in two different hardware trials with data collected using real robots. (p. 5, IV. EXPERIMENTS).
- **Strongest explicit boundary:** 4) compared to Di-NeRF*, which fails to resolve robot alignments and therefore cannot accurately match the ground-truth images. (p. 6, IV. EXPERIMENTS).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
