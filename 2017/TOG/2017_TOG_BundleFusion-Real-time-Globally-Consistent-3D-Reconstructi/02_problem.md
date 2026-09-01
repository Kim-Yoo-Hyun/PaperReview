# Problem - BundleFusion: Real-time Globally Consistent 3D Reconstruction using On-the-fly Surface Reintegration

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1604.01093; PDF retrieval source: https://arxiv.org/pdf/1604.01093. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION)): Many existing approaches rely heavily on proximity to the previous frame, limiting fast camera motion and recovery from tracking failure.

## PDF Body Digest

- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** We are seeing a renaissance in 3D scanning, fueled both by applications such as fabrication, augmented and virtual reality, gaming and robotics, and by the ...
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** Tis has opened up the need for real-time scanning at scale.
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** Here, the user or robot must scan an entire room (or several spaces) in real-time, with instantaneous and continual integration of the accumulated 3D model ...
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** However, despite the plethora of reconstruction systems, we have yet to see a single holistic solution for the problem of real-time 3D reconstruction at scale ...
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** Tis is due to the many requirements that such a solution needs to fulfill: High-quality surface modeling.
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** Many existing approaches rely heavily on proximity to the previous frame, limiting fast camera motion and recovery from tracking failure.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Tis enables our method to be extremely robust to tracking failures, with tracking far less britle than existing frame-to-frame or frame-to-model RGB-D approaches.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Many existing approaches rely heavily on proximity to the previous frame, limiting fast camera motion and recovery from tracking failure. | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | At the core of our method is a robust pose estimation strategy, which globally optimizes for the camera trajectory per frame, considering ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF |
| State / latent | core, robust, pose, estimation, strategy, globally, optimizes, camera, trajectory, frame | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | ability, react, instantaneous, feedback, crucial, scanning, obtaining, high-quality | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: core, robust, pose, estimation, strategy, globally, optimizes, camera, trajectory, frame | p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |
| Decision / output variable | path/waypoint/velocity; body terms: Tis, enables, extremely, robust, tracking, failures, less, britle | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: achieve, corresponding, model, correction, extend, scalable, variant, real-time | p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Success / guarantee | goal reach with collision-free execution | p. 13 (6 RESULTS), p. 17 (6 RESULTS), p. 9 (6 RESULTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Tis enables our method to be extremely robust to tracking failures, with tracking far less britle than existing frame-to-frame or frame-to-model RGB-D approaches.
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** Te challenge is to update the model afer data has been integrated, in accordance with the newest pose estimates.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Tis allows for a robust scanning experience, where even novice users can perform large-scale scans without failure.

## What the Paper Changes

PDF contribution framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION)): Tis enables our method to be extremely robust to tracking failures, with tracking far less britle than existing frame-to-frame or frame-to-model RGB-D approaches.

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** In summary, the main contributions of our work are as follows: (1) A novel, real-time global pose alignment framework which considers the complete history of ...
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** At the core of our method is a robust pose estimation strategy, which globally optimizes for the camera trajectory per frame, considering the complete history ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 2 | Fig. 1. Our novel real-time 3D reconstruction approach solves for global pose alignment and obtains dense volumetric reconstructions ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Recovery from tracking failure: our method is able to detect (gray overlay) and recover from tracking failure; i.e., ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 11 | [37]: in contrast to the frame-to-model tracking of VoxelHashing, our novel global pose optimization implicitly handles loop closure ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Fig. 7. Our proposed real-time global pose optimization (top) outperforms the method of Whelan et al. [54] (botom) ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), interface p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), objective p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
