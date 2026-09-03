# Problem - Multimodal LiDAR-Camera Novel View Synthesis with Unified Pose-free Neural Fields

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=GQHUET0V6f; PDF retrieval source: https://papers.neurips.cc/paper_files/paper/2025/file/70915b08a205ea5522528690d93518f6-Paper-Conference.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 3 (1 Introduction)): Nevertheless, prior research [37] has faced challenges due to the significant domain gap and uncoordinated convergence problems [27, 42, 34] between these modalities.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Pose-free Neural Radiance Field (NeRF) aims at novel view synthesis (NVS) without relying on accurate poses, exhibiting significant practical value.
- **p. 1 / Abstract - extractive body cue:** Image and LiDAR point cloud are two pivotal modalities in autonomous driving scenarios.
- **p. 1 / Abstract - extractive body cue:** While demonstrating impressive performance, single-modality pose-free NeRFs often suffer from local optima due to the limited geometric information provided by dense image textures or the ...
- **p. 1 / Abstract - extractive body cue:** Although prior methods have explored the complementary strengths of both modalities, they have only leveraged inherently sparse point clouds for discrete, nonpixel-wise depth supervision, and ...
- **p. 1 / Abstract - extractive body cue:** As a result, a Multimodal Unified Pose-free framework remains notably absent.
- **p. 2 / 1 Introduction - extractive body cue:** Nevertheless, prior research [37] has faced challenges due to the significant domain gap and uncoordinated convergence problems [27, 42, 34] between these modalities.
- **p. 2 / 1 Introduction - extractive body cue:** Compared to continuous LiDAR-Camera Fields, projecting LiDAR point clouds onto images as discrete depth priors fails to provide continuous, pixel-wise supervision.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Nevertheless, prior research [37] has faced challenges due to the significant domain gap and uncoordinated convergence problems [27, 42, 34] between these ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | For the image modality, we use a lightweight MLP to refine the geo-MLP output, helping reduce modality conflicts. | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | image, modality, lightweight, MLP, refine, geo-MLP, output, helping, reduce, conflicts | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Leveraging, multimodal, input, exploit, images, alleviate, impact, non-overlapping | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: image, modality, lightweight, MLP, refine, geo-MLP, output, helping, reduce, conflicts | p. 5 (4 Methodology), p. 5 (4 Methodology), p. 7 (4 Methodology) |
| Decision / output variable | geometry/map/query r; body terms: summary, primary, contributions, delineated, follows, MUP, unified, pose-free | p. 3 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: explore, modality, features, fused, independently, truncate, gradients, reconstruction | p. 5 (4 Methodology), p. 6 (4 Methodology), p. 5 (4 Methodology), p. 6 (4 Methodology), p. 7 (4 Methodology), p. 7 (4 Methodology) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (4 Methodology), p. 7 (4 Methodology), p. 7 (4 Methodology) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 6 (Figure/Table caption), p. 8 (5 Experiment), p. 8 (5 Experiment) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive body cue:** Compared to continuous LiDAR-Camera Fields, projecting LiDAR point clouds onto images as discrete depth priors fails to provide continuous, pixel-wise supervision.
- **p. 1 / 1 Introduction - extractive body cue:** However, existing pose-free NeRFs have largely concentrated on single modalities, particularly on images.
- **p. 1 / 1 Introduction - extractive body cue:** Nevertheless, due to the lack of geometric consistency, relying solely on rich texture with39th Conference on Neural Information Processing Systems (NeurIPS 2025).
- **p. 3 / 1 Introduction - extractive body cue:** Comprehensive experiments demonstrate that MUP significantly outperforms prior state-of-the-art techniques and single-modality approaches by a large margin in both registration and NVS.

## What the Paper Changes

PDF body contribution framing (p. 3 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 5 (4 Methodology)): In summary, our primary contributions can be delineated as follows: (1) We propose MUP, a unified pose-free framework that combines the advantages of two modalities for pose estimation and multimodal ...

- **p. 2 / 1 Introduction - extractive body cue:** Moreover, to enhance color-depth consistency, we introduce a consistency constraint by projecting image pixels onto adjacent frames using depth derived from NeRF.
- **p. 2 / 1 Introduction - extractive body cue:** To alleviate modality conflicts [37] and address the uncoordinated convergence problem, we introduce a multimodal-specific coarse-to-fine training approach [16], facilitating the utilization of a singular ...
- **p. 3 / 1 Introduction - extractive body cue:** We evaluate our method across diverse scenarios using the KITTI-360 [15] and NuScenes [4] autonomous driving datasets.
- **p. 5 / 4 Methodology - extractive body cue:** Finally, we present the proposed consistency constraint and the overall optimization pipeline in Section 4.3.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 10 | We revisit the limitations of single-modality pose-free methods in large-scale scenes. | reported limitation/failure wording; scope must be verified |
| body cue at p. 2 | Figure 1: NVS results w/ and w/o accurate poses. Compared to continuous LiDAR-Camera Fields, projecting LiDAR point clouds ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Alignmif [37] cannot be effectively used in ill-conditioned optimization. | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | Additionally, it is not designed to handle dynamic scenes, which is a non-negligible limitation in autonomous driving scenarios. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 5 (4 Methodology), p. 5 (4 Methodology), p. 7 (4 Methodology), p. 2 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 3 (1 Introduction), interface p. 5 (4 Methodology), p. 5 (4 Methodology), p. 7 (4 Methodology), p. 2 (1 Introduction), objective p. 5 (4 Methodology), p. 6 (4 Methodology), p. 5 (4 Methodology), p. 6 (4 Methodology), p. 7 (4 Methodology), p. 7 (4 Methodology).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
