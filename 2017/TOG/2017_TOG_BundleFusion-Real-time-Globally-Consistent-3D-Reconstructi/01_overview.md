# BundleFusion: Real-time Globally Consistent 3D Reconstruction using On-the-fly Surface Reintegration

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=0.889); canonical paper source: https://arxiv.org/abs/1604.01093.
> PDF retrieval source: https://arxiv.org/pdf/1604.01093. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2017 / TOG
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Vision, SLAM, RGB-D, 3D reconstruction
- Official paper: https://arxiv.org/abs/1604.01093
- Full-text retrieval: https://arxiv.org/pdf/1604.01093
- Code/Project: https://graphics.stanford.edu/projects/bundlefusion/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=0.889)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 Many existing approaches rely heavily on proximity to the previous frame, limiting fast camera motion and recovery from tracking failure.를 문제로 두고, Tis enables our method to be extremely robust to tracking failures, with tracking far less britle than existing frame-to-frame or frame-to-model RGB-D approaches.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / 1 INTRODUCTION - extractive body cue:** We are seeing a renaissance in 3D scanning, fueled both by applications such as fabrication, augmented and virtual reality, gaming and robotics, and by the ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Tis has opened up the need for real-time scanning at scale.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Here, the user or robot must scan an entire room (or several spaces) in real-time, with instantaneous and continual integration of the accumulated 3D model ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, despite the plethora of reconstruction systems, we have yet to see a single holistic solution for the problem of real-time 3D reconstruction at scale ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Tis is due to the many requirements that such a solution needs to fulfill: High-quality surface modeling.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Many existing approaches rely heavily on proximity to the previous frame, limiting fast camera motion and recovery from tracking failure.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Tis enables our method to be extremely robust to tracking failures, with tracking far less britle than existing frame-to-frame or frame-to-model RGB-D approaches.

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Tis enables our method to be extremely robust to tracking failures, with tracking far less britle than existing frame-to-frame or frame-to-model RGB-D approaches.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In summary, the main contributions of our work are as follows: (1) A novel, real-time global pose alignment framework which considers the complete history of ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** At the core of our method is a robust pose estimation strategy, which globally optimizes for the camera trajectory per frame, considering the complete history ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** Our framework leads to a comprehensive online scanning solution for large indoor environments, enabling ease of use and high-quality results1.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Key to our work is a new fully parallelizable sparse-then-dense global pose optimization framework: sparse RGB features are used for coarse global pose estimation, ensuring ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Tis requires a high-quality representation that can model continuous surfaces rather than discrete points.
- **p. 1 / Body text (section not recovered) - extractive body cue:** We contribute a parallelizable optimization framework, which employs correspondences based on sparse features and dense geometric and photometric matching.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To achieve the corresponding model correction, we extend a scalable variant of real-time volumetric fusion [37], but importantly support model updates based on refined poses ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | At its core is a robust pose estimation strategy, optimizing per frame for a global set of camera poses by considering the complete history of RGB-D input with an efficient hierarchical approach. | camera/depth stream, pose, map와 language goal | p. 1 (Body text (section not recovered)), p. 2 (1 INTRODUCTION) |
| State/latent | core, robust, pose, estimation, strategy, optimizing, frame, global, camera, poses, considering, complete | robot pose, free-space/semantic map와 local goal | p. 1 (Body text (section not recovered)), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |
| Output/action | In summary, the main contributions of our work are as follows: (1) A novel, real-time global pose alignment framework which considers the complete history of input frames, removing the brittle and imprecise ... | collision-free trajectory 또는 velocity command | p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Objective/outcome | To achieve the corresponding model correction, we extend a scalable variant of real-time volumetric fusion [37], but importantly support model updates based on refined poses from our global optimization. | goal reach, safety, localization error와 replanning latency | p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (Body text (section not recovered)) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Tis enables our method to be extremely robust to tracking failures, with tracking far less britle than existing frame-to-frame or frame-to-model RGB-D approaches.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In summary, the main contributions of our work are as follows: (1) A novel, real-time global pose alignment framework which considers the complete history of ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** At the core of our method is a robust pose estimation strategy, which globally optimizes for the camera trajectory per frame, considering the complete history ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** Our framework leads to a comprehensive online scanning solution for large indoor environments, enabling ease of use and high-quality results1.
- **p. 12 / 6 RESULTS - extractive body cue:** While online alignment based on sparse features only (Ours (s)) achieves reasonable results, using dense matching only in per chunk alignment further increases accuracy (Ours ...
- **p. 9 / 6 RESULTS - extractive body cue:** Large-scale reconstruction results: our proposed real-time global pose optimization outperforms current state-of-the-art online reconstruction systems.
- **p. 10 / 6 RESULTS - extractive body cue:** We achieve this real-time performance with the combination of our tailored data-parallel Gauss-Newton solver (efficiently handling millions of residuals and solving for over a hundred ...
- **p. 10 / 6 RESULTS - extractive body cue:** Dense Alignment: the proposed dense intra- and inter- chunk alignment (top) leads to higher quality reconstructions than only the sparse alignment step (botom). their approach ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 12 (6 RESULTS), p. 9 (6 RESULTS) |
| Embodiment/environment | Te SUN3D dataset also contains eight scenes which contain manual object-correspondence annotations in order to guide their reconstructions; we show reconstruction results using our method (without annotation information) on these scenes ... | hardware/simulator version and reset protocol | p. 13 (6 RESULTS), p. 13 (6 RESULTS) |
| Dataset/benchmark | Reconstruction results on scenes from the SUN3D dataset [57], using SUN3Dsfm and our approach. | role, split, size and leakage | p. 13 (6 RESULTS), p. 13 (6 RESULTS), p. 14 (6 RESULTS), p. 15 (6 RESULTS) |
| Metric | In addition to the camera tracking evaluation provided in Section 6 of the paper, we evaluate surface reconstruction accuracy (mean distance of the model to the ground truth surface) for the living ... | definition, denominator, direction and uncertainty | p. 13 (6 RESULTS), p. 17 (6 RESULTS), p. 9 (6 RESULTS) |
| Baseline/ablation | Large-scale reconstruction results: our proposed real-time global pose optimization outperforms current state-of-the-art online reconstruction systems. | fair input/data/compute/action matching | p. 9 (6 RESULTS), p. 11 (6 RESULTS), p. 9 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1. Our novel real-time 3D reconstruction approach solves for global pose alignment and obtains dense volumetric reconstructions at a level of quality and completeness ...
- **p. 8 / 6 RESULTS - extractive body cue:** Recovery from tracking failure: our method is able to detect (gray overlay) and recover from tracking failure; i.e., if the sensor is occluded or observes ...
- **p. 11 / 6 RESULTS - extractive body cue:** [37]: in contrast to the frame-to-model tracking of VoxelHashing, our novel global pose optimization implicitly handles loop closure (top), robustly detects and recovers from tracking ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 7. Our proposed real-time global pose optimization (top) outperforms the method of Whelan et al. [54] (botom) in terms of scan completeness and alignment ...
- **p. 11 / 6 RESULTS - extractive body cue:** To indicate tracking failure, the reconstruction is shown with a gray overlay.
- **p. 13 / 6 RESULTS - extractive body cue:** Te relocalization (due to sensor occlusion) in the sequence Apt 2 cannot be handled by state-of-theart methods such as ElasticFusion and Redwood.
- **p. 9 / 6 RESULTS - extractive body cue:** Note, we do not compare to their newer non-rigid approach, since it fails on most of our dataset sequences.

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 Many existing approaches rely heavily on proximity to the previous frame, limiting fast camera motion and recovery from tracking failure.를 문제로 두고, Tis enables our method to be extremely robust to tracking failures, with tracking far less britle than existing frame-to-frame or frame-to-model RGB-D approaches.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
