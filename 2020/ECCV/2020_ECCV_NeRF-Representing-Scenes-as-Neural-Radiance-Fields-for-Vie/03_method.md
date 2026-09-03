# Method - NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2003.08934; PDF retrieval source: https://arxiv.org/pdf/2003.08934. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 17 (A Additional Implementation Details), p. 18 (A Additional Implementation Details), p. 18 (A Additional Implementation Details), p. 14 (9) Complete Model), p. 17 (A Additional Implementation Details)): Training Details For real scene data, we regularize our network by adding random Gaussian noise with zero mean and unit variance to the output σ values (before passing them through ...

## Method Body Digest

- **p. 17 / A Additional Implementation Details - extractive body cue:** Training Details For real scene data, we regularize our network by adding random Gaussian noise with zero mean and unit variance to the output σ ...
- **p. 18 / A Additional Implementation Details - extractive body cue:** An additional layer outputs the volume density σ (which is rectified using a ReLU to ensure that the output volume density is nonnegative) and a ...
- **p. 18 / A Additional Implementation Details - extractive body cue:** A final layer (with a sigmoid activation) outputs the emitted RGB radiance at position x, as viewed by a ray with direction d. dataset requires ...
- **p. 14 / 9) Complete Model - extractive body cue:** xyzθφ 100 10 (64, 128) 31.01 0.947 0.081 Table 2: An ablation study of our model.
- **p. 17 / A Additional Implementation Details - extractive body cue:** We implement our model in Tensorflow [1].
- **p. 2 / 1 Introduction - extractive body cue:** Here, we visualize the set of 100 input views of the synthetic Drums scene randomly captured on a surrounding hemisphere, and we show two novel ...
- **p. 18 / A Additional Implementation Details - extractive body cue:** Input vectors are shown in green, intermediate hidden layers are shown in blue, output vectors are shown in red, and the number inside each block ...
- **p. 2 / 1 Introduction - extractive body cue:** Input Images Optimize NeRF Render new views Fig.

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** We address these issues by transforming input 5D coordinates with a positional encoding that enables the MLP to represent higher frequency functions, and we propose ...
- **p. 1 / 1 Introduction - extractive body cue:** Our method optimizes a deep fully-connected neural network without any convolutional layers (often referred to as a multilayer perceptron or MLP) to represent this function ...
- **p. 2 / 1 Introduction - extractive body cue:** Crucially, our method overcomes the prohibitive storage costs of discretized voxel grids when modeling complex scenes at high-resolutions.

## Source Evidence Cues

- **p. 17 / A Additional Implementation Details - extractive body cue:** Training Details For real scene data, we regularize our network by adding random Gaussian noise with zero mean and unit variance to the output σ ...
- **p. 18 / A Additional Implementation Details - extractive body cue:** An additional layer outputs the volume density σ (which is rectified using a ReLU to ensure that the output volume density is nonnegative) and a ...
- **p. 18 / A Additional Implementation Details - extractive body cue:** A final layer (with a sigmoid activation) outputs the emitted RGB radiance at position x, as viewed by a ray with direction d. dataset requires ...
- **p. 14 / 9) Complete Model - extractive body cue:** xyzθφ 100 10 (64, 128) 31.01 0.947 0.081 Table 2: An ablation study of our model.
- **p. 17 / A Additional Implementation Details - extractive body cue:** We implement our model in Tensorflow [1].
- **Detected method headings:** 9) Complete Model (p. 14); B Additional Baseline Method Details (p. 18)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Training Details For real scene data, we regularize our network by adding random Gaussian noise with zero mean and unit variance to ... | p. 17 (A Additional Implementation Details), p. 18 (A Additional Implementation Details) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | An additional layer outputs the volume density σ (which is rectified using a ReLU to ensure that the output volume density is ... | p. 18 (A Additional Implementation Details), p. 18 (A Additional Implementation Details) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | A final layer (with a sigmoid activation) outputs the emitted RGB radiance at position x, as viewed by a ray with direction ... | p. 18 (A Additional Implementation Details), p. 14 (9) Complete Model) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 17 / A Additional Implementation Details - extractive body cue:** Training Details For real scene data, we regularize our network by adding random Gaussian noise with zero mean and unit variance to the output σ ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Here, visualize, input, views, synthetic, Drums, scene, randomly, captured, surrounding, hemisphere, novel, rendered, optimized | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Here, visualize, input, views, synthetic, Drums, scene, randomly, captured, surrounding | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | address, issues, transforming, input, coordinates, positional, encoding, enables, MLP, represent | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Training, Details, real, scene, data, regularize, network, adding, random, Gaussian | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 Introduction - extractive body cue:** Here, we visualize the set of 100 input views of the synthetic Drums scene randomly captured on a surrounding hemisphere, and we show two novel ...
- **p. 18 / A Additional Implementation Details - extractive body cue:** Input vectors are shown in green, intermediate hidden layers are shown in blue, output vectors are shown in red, and the number inside each block ...
- **p. 2 / 1 Introduction - extractive body cue:** Input Images Optimize NeRF Render new views Fig.
- **p. 14 / 9) Complete Model - extractive body cue:** We believe the benefit of increasing L is limited once 2L exceeds the maximum frequency present in the sampled input images (roughly 1024 in our ...
- **p. 18 / A Additional Implementation Details - extractive body cue:** A final layer (with a sigmoid activation) outputs the emitted RGB radiance at position x, as viewed by a ray with direction d. dataset requires ...
- **p. 17 / A Additional Implementation Details - extractive body cue:** Our dataset of real images contains content that can exist anywhere between the closest point and infinity, so we use normalized device coordinates to map ...
- **p. 1 / 1 Introduction - extractive body cue:** We represent a static scene as a continuous 5D function that outputs the radiance emitted in each direction (θ, φ) at each point (x, y, ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | On an NVIDIA V100, this takes approximately 30 seconds per frame. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | We address these issues by transforming input 5D coordinates with a positional encoding that enables the MLP to represent higher frequency functions, ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 17 / A Additional Implementation Details - extractive body cue:** Training Details For real scene data, we regularize our network by adding random Gaussian noise with zero mean and unit variance to the output σ ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Training, Details, real, scene, data, regularize, network, adding, random, Gaussian, noise, zero, mean, unit, variance, output, values, before, passing, them.
- **Relevant PDF headings:** 9) Complete Model (p. 14); B Additional Baseline Method Details (p. 18).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | This dataset consists of 8 scenes captured with a handheld cellphone (5 taken from the LLFF paper and 3 that we capture), ... | p. 10 (6 Results), p. 10 (6 Results) |
| Semantic / temporal fusion | We thoroughly outperform both baselines that also optimize a separate network per scene (NV and SRN) in all scenarios. | p. 13 (6.3 Discussion), p. 9 (6 Results) |
| Robot query / planning handoff | Table 1: Our method quantitatively outperforms prior work on datasets of both synthetic and real images. We report PSNR/SSIM (higher is better) ... | p. 10 (Figure/Table caption), p. 9 (6 Results) |

## Failure and Ablation Link

- **p. 13 / 6.3 Discussion - extractive body cue:** In rows 2-4 we remove these three components one at a time from the full model, observing that positional encoding (row 2) and view-dependence (row ...
- **p. 9 / 6 Results - extractive body cue:** 8 and 6) show that our method outperforms prior work, and provide extensive ablation studies to validate our design choices (Table 2).
- **p. 10 / 6 Results - extractive body cue:** Neural Volumes (NV) [24] synthesizes novel views of objects that lie entirely within a bounded volume in front of a distinct background (which must be ...
- **p. 13 / 6.3 Discussion - extractive body cue:** 6.4 Ablation studies We validate our algorithm's design choices and parameters with an extensive ablation study in Table 2.
- **p. 14 / Figure/Table caption - extractive body cue:** Table 2: An ablation study of our model. Metrics are averaged over the 8 scenes from our realistic synthetic dataset. See Sec. 6.4 for detailed ...
- **p. 25 / Figure/Table caption - extractive body cue:** Table 6: Per-scene quantitative results from our ablation study. The scenes used here are the same as in Table 4.
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 4: Here we visualize how our full model benefits from representing view- dependent emitted radiance and from passing our input coordinates through a high-frequency ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 17 (A Additional Implementation Details), p. 18 (A Additional Implementation Details), p. 18 (A Additional Implementation Details), p. 14 (9) Complete Model), p. 17 (A Additional Implementation Details), objective p. 17 (A Additional Implementation Details), temporal p. 18 (A Additional Implementation Details), p. 2 (1 Introduction), p. 7 (2 Related Work), p. 7 (2 Related Work), p. 8 (2 Related Work), p. 8 (2 Related Work).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
