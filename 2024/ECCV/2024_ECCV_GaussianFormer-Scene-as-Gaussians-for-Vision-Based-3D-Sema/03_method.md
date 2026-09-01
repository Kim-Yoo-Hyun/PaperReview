# Method - GaussianFormer: Scene as Gaussians for Vision-Based 3D Semantic Occupancy Prediction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3958_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03958.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction)): In this paper, we propose the first object-centric representation for 3D semantic occupancy prediction.

## Method Body Digest

- **p. 2 / 1 Introduction - extractive PDF cue:** In this paper, we propose the first object-centric representation for 3D semantic occupancy prediction.
- **p. 2 / 1 Introduction - extractive PDF cue:** We propose a GaussianFormer model to effectively obtain 3D semantic Gaussians from image inputs.
- **p. 3 / 1 Introduction - extractive PDF cue:** The proposed 3D Gaussian representation uses a sparse and adaptive set of features to describe a 3D scene but can still model the fine-grained structure ...
- **p. 3 / 1 Introduction - extractive PDF cue:** We then decode the properties of 3D semantic Gaussians from the updated queries as the scene representation.
- **p. 2 / 1 Introduction - extractive PDF cue:** We iteratively refine the properties of the 3D Gaussians for smoother optimizations.
- **p. 2 / 1 Introduction - extractive PDF cue:** While vision-centric systems share an economical advantage, their inability to capture obstacles of arbitrary shapes hinders driving safety and robustness [14,18,26,27].
- **p. 2 / 1 Introduction - extractive PDF cue:** To efficiently incorporate interactions among 3D Gaussians, we treat them as point clouds located at the Gaussian means and
- **p. 3 / 1 Introduction - extractive PDF cue:** GaussianFormer achieves comparable performance with existing state-of-the-art methods with only 17.8% - 24.8% of their memory consumption.

## Design Rationale

- **p. 2 / 1 Introduction - extractive PDF cue:** We propose a GaussianFormer model to effectively obtain 3D semantic Gaussians from image inputs.
- **p. 2 / 1 Introduction - extractive PDF cue:** In this paper, we propose the first object-centric representation for 3D semantic occupancy prediction.

## Source Evidence Cues

- **p. 2 / 1 Introduction - extractive PDF cue:** In this paper, we propose the first object-centric representation for 3D semantic occupancy prediction.
- **p. 2 / 1 Introduction - extractive PDF cue:** We propose a GaussianFormer model to effectively obtain 3D semantic Gaussians from image inputs.
- **p. 3 / 1 Introduction - extractive PDF cue:** The proposed 3D Gaussian representation uses a sparse and adaptive set of features to describe a 3D scene but can still model the fine-grained structure ...
- **p. 3 / 1 Introduction - extractive PDF cue:** We then decode the properties of 3D semantic Gaussians from the updated queries as the scene representation.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | In this paper, we propose the first object-centric representation for 3D semantic occupancy prediction. | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | We propose a GaussianFormer model to effectively obtain 3D semantic Gaussians from image inputs. | p. 2 (1 Introduction), p. 3 (1 Introduction) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | The proposed 3D Gaussian representation uses a sparse and adaptive set of features to describe a 3D scene but can still model ... | p. 3 (1 Introduction), p. 3 (1 Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / 1 Introduction - extractive PDF cue:** We iteratively refine the properties of the 3D Gaussians for smoother optimizations.
- **p. 2 / 1 Introduction - extractive PDF cue:** While vision-centric systems share an economical advantage, their inability to capture obstacles of arbitrary shapes hinders driving safety and robustness [14,18,26,27].
- **p. 3 / 1 Introduction - extractive PDF cue:** We then decode the properties of 3D semantic Gaussians from the updated queries as the scene representation.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 3 (1 Introduction).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | GaussianFormer, model, effectively, obtain, semantic, Gaussians, image, inputs, efficiently, incorporate, interactions, among, treat, them | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | GaussianFormer, model, effectively, obtain, semantic, Gaussians, image, inputs, efficiently, incorporate | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | GaussianFormer, model, effectively, obtain, semantic, Gaussians, image, inputs, first, object-centric | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | iteratively, refine, properties, Gaussians, smoother, optimizations, While, vision-centric, systems, share | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 Introduction - extractive PDF cue:** We propose a GaussianFormer model to effectively obtain 3D semantic Gaussians from image inputs.
- **p. 2 / 1 Introduction - extractive PDF cue:** To efficiently incorporate interactions among 3D Gaussians, we treat them as point clouds located at the Gaussian means and
- **p. 3 / 1 Introduction - extractive PDF cue:** GaussianFormer achieves comparable performance with existing state-of-the-art methods with only 17.8% - 24.8% of their memory consumption.
- **p. 3 / 1 Introduction - extractive PDF cue:** The proposed 3D Gaussian representation uses a sparse and adaptive set of features to describe a 3D scene but can still model the fine-grained structure ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | It provides ground truth labels for 9 long sequences with a total of 12865 key frames, which are officially split into 7/1/1 ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Methods Query Form Query Resolution Latency ↓Memory ↓ BEVFormer [27] 2D BEV 200×200 302 ms | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | Methods Query Form Query Resolution Latency ↓Memory ↓ BEVFormer [27] 2D BEV 200×200 302 ms | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | Methods Query Form Query Resolution Latency ↓Memory ↓ BEVFormer [27] 2D BEV 200×200 302 ms | hardware, batch and throughput |

## Training vs Inference

- **p. 10 / 4 Experiments - extractive PDF cue:** We train our models for 20 epochs with a batch size of 8, and employ random flip and photometric distortion augmentations.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** first, object-centric, representation, semantic, occupancy, prediction, GaussianFormer, model, effectively, obtain, Gaussians, image, inputs, Gaussian, uses, sparse, adaptive, features, describe, scene.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | 4.1 Datasets NuScenes [3] consists of 1000 sequences of various driving scenes collected in Boston and Singapore, which are officially split into ... | p. 9 (4 Experiments), p. 9 (4 Experiments) |
| Semantic / temporal fusion | Even compared with dense grid representations, GaussianFormer performs on par with OccFormer [58] and SurroundOcc [51]. | p. 10 (4 Experiments), p. 11 (4 Experiments) |
| Robot query / planning handoff | Our GaussianFormer achieves notable improvements over methods based on planar representations, such as BEVFormer [27] and TPVFormer [17]. | p. 10 (4 Experiments), p. 14 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 12 / Figure/Table caption - extractive PDF cue:** Table 4: Ablation on the components of GaussianFormer. Deep Supervision represents supervising the output of each refinement module. Residual Refine means on which properties of ...
- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1: Considering the universal approximating ability of Gaussian mixture [9, 12], we propose an object-centric 3D semantic Gaussian representation to describe the fine- grained ...
- **p. 13 / Figure/Table caption - extractive PDF cue:** Table 5: Ablation on the number of Gaussians. The latency and memory are tested on an NVIDIA 4090 GPU with batch size one during inference. ...
- **p. 14 / Figure/Table caption - extractive PDF cue:** Fig. 5: Visualization results for 3D semantic occupancy prediction on nuScenes. We visualize the 3D Gaussians by treating them as ellipsoids centered at the Gaussian ...
- **p. 10 / 4 Experiments - extractive PDF cue:** We employ ResNet101-DCN [13] initialized from FCOS3D [48] checkpoint as the image backbone for nuScenes and ResNet50 [13] pretrained with ImageNet [10] for KITTI-360.
- **p. 12 / 26500 M - extractive PDF cue:** This is because the positions of Gaussians are sensitive to noise which quickly converge to a trivial solution without regularization for coherence during refinement.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), objective p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), temporal p. 10 (4 Experiments), p. 12 (4 Experiments), p. 12 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments), p. 13 (26500 M).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
