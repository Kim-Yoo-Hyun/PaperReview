# Method - BundleFusion: Real-time Globally Consistent 3D Reconstruction using On-the-fly Surface Reintegration

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1604.01093; PDF retrieval source: https://arxiv.org/pdf/1604.01093. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (Body text (section not recovered)), p. 2 (1 INTRODUCTION)): Key to our work is a new fully parallelizable sparse-then-dense global pose optimization framework: sparse RGB features are used for coarse global pose estimation, ensuring proposals fall within the basin ...

## Method Body Digest

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Key to our work is a new fully parallelizable sparse-then-dense global pose optimization framework: sparse RGB features are used for coarse global pose estimation, ensuring ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Tis requires a high-quality representation that can model continuous surfaces rather than discrete points.
- **p. 1 / Body text (section not recovered) - extractive body cue:** We contribute a parallelizable optimization framework, which employs correspondences based on sparse features and dense geometric and photometric matching.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To achieve the corresponding model correction, we extend a scalable variant of real-time volumetric fusion [37], but importantly support model updates based on refined poses ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Te challenge is to update the model afer data has been integrated, in accordance with the newest pose estimates.
- **p. 1 / Body text (section not recovered) - extractive body cue:** We remove the heavy reliance on temporal tracking, and continually localize to the globally optimized frames instead.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** (3) A new RGB-D re-integration strategy to enable on-the-fly and continuous 3D model updates when refined global pose estimates are available.
- **p. 1 / Body text (section not recovered) - extractive body cue:** At its core is a robust pose estimation strategy, optimizing per frame for a global set of camera poses by considering the complete history of ...

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Tis enables our method to be extremely robust to tracking failures, with tracking far less britle than existing frame-to-frame or frame-to-model RGB-D approaches.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In summary, the main contributions of our work are as follows: (1) A novel, real-time global pose alignment framework which considers the complete history of ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** At the core of our method is a robust pose estimation strategy, which globally optimizes for the camera trajectory per frame, considering the complete history ...

## Source Evidence Cues

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Key to our work is a new fully parallelizable sparse-then-dense global pose optimization framework: sparse RGB features are used for coarse global pose estimation, ensuring ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Tis requires a high-quality representation that can model continuous surfaces rather than discrete points.
- **p. 1 / Body text (section not recovered) - extractive body cue:** We contribute a parallelizable optimization framework, which employs correspondences based on sparse features and dense geometric and photometric matching.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To achieve the corresponding model correction, we extend a scalable variant of real-time volumetric fusion [37], but importantly support model updates based on refined poses ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | Key to our work is a new fully parallelizable sparse-then-dense global pose optimization framework: sparse RGB features are used for coarse global ... | p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | Tis requires a high-quality representation that can model continuous surfaces rather than discrete points. | p. 1 (1 INTRODUCTION), p. 1 (Body text (section not recovered)) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | We contribute a parallelizable optimization framework, which employs correspondences based on sparse features and dense geometric and photometric matching. | p. 1 (Body text (section not recovered)), p. 2 (1 INTRODUCTION) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To achieve the corresponding model correction, we extend a scalable variant of real-time volumetric fusion [37], but importantly support model updates based on refined poses ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Te challenge is to update the model afer data has been integrated, in accordance with the newest pose estimates.
- **p. 1 / Body text (section not recovered) - extractive body cue:** We remove the heavy reliance on temporal tracking, and continually localize to the globally optimized frames instead.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** (3) A new RGB-D re-integration strategy to enable on-the-fly and continuous 3D model updates when refined global pose estimates are available.
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 1 (1 INTRODUCTION), p. 1 (Body text (section not recovered)), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | core, robust, pose, estimation, strategy, optimizing, frame, global, camera, poses, considering, complete, history, RGB-D | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | core, robust, pose, estimation, strategy, optimizing, frame, global, camera, poses | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | Tis, enables, extremely, robust, tracking, failures, less, britle, existing, frame-to-frame | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | achieve, corresponding, model, correction, extend, scalable, variant, real-time, volumetric, fusion | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / Body text (section not recovered) - extractive body cue:** At its core is a robust pose estimation strategy, optimizing per frame for a global set of camera poses by considering the complete history of ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In summary, the main contributions of our work are as follows: (1) A novel, real-time global pose alignment framework which considers the complete history of ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Te ability to react to instantaneous feedback is crucial to 3D scanning and key to obtaining high-quality results.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We demonstrate how our approach outperforms current state-of-the-art online systems at unprecedented speed and scan completeness, and even surpasses the accuracy and robustness of offline ...
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | In summary, the main contributions of our work are as follows: (1) A novel, real-time global pose alignment framework which considers the ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | Dense Alignment: the proposed dense intra- and inter- chunk alignment (top) leads to higher quality reconstructions than only the sparse alignment step ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | In summary, the main contributions of our work are as follows: (1) A novel, real-time global pose alignment framework which considers the ... | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Key, fully, parallelizable, sparse-then-dense, global, pose, optimization, framework, sparse, RGB, features, coarse, estimation, ensuring, proposals, fall, within, basin, convergence, following.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | Te SUN3D dataset also contains eight scenes which contain manual object-correspondence annotations in order to guide their reconstructions; we show reconstruction results ... | p. 13 (6 RESULTS), p. 13 (6 RESULTS) |
| Global / local decision | Large-scale reconstruction results: our proposed real-time global pose optimization outperforms current state-of-the-art online reconstruction systems. | p. 9 (6 RESULTS), p. 11 (6 RESULTS) |
| Motion execution / recovery | While online alignment based on sparse features only (Ours (s)) achieves reasonable results, using dense matching only in per chunk alignment further ... | p. 12 (6 RESULTS), p. 9 (6 RESULTS) |

## Failure and Ablation Link

- **p. 8 / 6 RESULTS - extractive body cue:** Recovery from tracking failure: our method is able to detect (gray overlay) and recover from tracking failure; i.e., if the sensor is occluded or observes ...
- **p. 9 / 6 RESULTS - extractive body cue:** We additionally compare to the offline Redwood approach [4], using their rigid variant, see Fig.
- **p. 9 / 6 RESULTS - extractive body cue:** Note the completeness of the scans, the global alignment without noticeable camera drif and the high local quality of the reconstructions in both geometry and ...
- **p. 11 / 6 RESULTS - extractive body cue:** While our solver takes a couple more iterations to converge without the Levenberg-Marquardt damping strategy, it still runs ≈20 times faster than Ceres while converging ...
- **p. 12 / 6 RESULTS - extractive body cue:** Note that for Redwood, we show results for the rigid variant, which produced beter camera tracking results.
- **p. 13 / 6 RESULTS - extractive body cue:** Te SUN3D dataset also contains eight scenes which contain manual object-correspondence annotations in order to guide their reconstructions; we show reconstruction results using our method ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1. Our novel real-time 3D reconstruction approach solves for global pose alignment and obtains dense volumetric reconstructions at a level of quality and completeness ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (Body text (section not recovered)), p. 2 (1 INTRODUCTION), objective p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (Body text (section not recovered)), p. 2 (1 INTRODUCTION), temporal p. 2 (1 INTRODUCTION), p. 10 (6 RESULTS), p. 1 (Body text (section not recovered)), p. 3 (2 RELATED WORK), p. 3 (2 RELATED WORK), p. 4 (2 RELATED WORK).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
