# Method - EmbodiedOcc: Embodied 3D Occupancy Prediction for Vision-based Online Scene Understanding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Wu_EmbodiedOcc_Embodied_3D_Occupancy_Prediction_for_Vision-based_Online_Scene_Understanding_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_EmbodiedOcc_Embodied_3D_Occupancy_Prediction_for_Vision-based_Online_Scene_Understanding_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (3.2. Local Refinement Module), p. 3 (3.2. Local Refinement Module)): In this subsection, we will first explain our local refinement module, which extracts semantic and structural features from the monocular input and integrates them to update the Gaussian-based representation of ...

## Method Body Digest

- **p. 3 / 3.2. Local Refinement Module - extractive PDF cue:** In this subsection, we will first explain our local refinement module, which extracts semantic and structural features from the monocular input and integrates them to ...
- **p. 3 / 3.2. Local Refinement Module - extractive PDF cue:** Different from conventional methods that conducted feature integration in a voxelized space, we use a set of 3D semantic Gaussians to represent an indoor scene ...
- **p. 3 / 3.1. Embodied 3D Occupancy Prediction - extractive PDF cue:** Then we detach and put these updated Gaussians back into the memory.
- **p. 3 / 3.1. Embodied 3D Occupancy Prediction - extractive PDF cue:** Different subscripts may correspond to similar positions and perspectives, indicating that the agent has returned to a previously explored location.
- **p. 3 / 3.1. Embodied 3D Occupancy Prediction - extractive PDF cue:** Depth Aware Predicted Depth Map … … Input T-1 Input T … … … … Gaussian Memory T Gaussian Memory T-1 Occupancy T Occupancy T-1 ...
- **p. 2 / 3.1. Embodied 3D Occupancy Prediction - extractive PDF cue:** Conventional methods in indoor scenarios for occupancy prediction accepted RGB-D as inputs to predict the semantic occupancy of a 3D scene which requires depth sensors.
- **p. 3 / 3.1. Embodied 3D Occupancy Prediction - extractive PDF cue:** Recent methods begin to consider endowing models with the same competence, which accept a monocular RGB image as input and derive a 3D occupancy prediction ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Most existing methods [2, 54, 56] still focus on local 3D occupancy prediction by integrating semantic and depth information extracted from the visual inputs.

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** Specifically, we propose a structure-aware local refinement module to update the relevant Gaussians within the current frustum.
- **p. 2 / 1. Introduction - extractive PDF cue:** We propose an EmbodiedOcc framework based on Gaussian memories to accomplish this task, considering the explicity and structural nature of 3D Gaussians.
- **p. 3 / 3.1. Embodied 3D Occupancy Prediction - extractive PDF cue:** Motivated by this, we propose an embodied 3D occupancy prediction task in this paper.

## Source Evidence Cues

- **p. 3 / 3.2. Local Refinement Module - extractive PDF cue:** In this subsection, we will first explain our local refinement module, which extracts semantic and structural features from the monocular input and integrates them to ...
- **p. 3 / 3.2. Local Refinement Module - extractive PDF cue:** Different from conventional methods that conducted feature integration in a voxelized space, we use a set of 3D semantic Gaussians to represent an indoor scene ...
- **Detected method headings:** 3. Proposed Approach (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | In this subsection, we will first explain our local refinement module, which extracts semantic and structural features from the monocular input and ... | p. 3 (3.2. Local Refinement Module), p. 3 (3.2. Local Refinement Module) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Different from conventional methods that conducted feature integration in a voxelized space, we use a set of 3D semantic Gaussians to represent ... | p. 3 (3.2. Local Refinement Module) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | In this subsection, we will first explain our local refinement module, which extracts semantic and structural features from the monocular input and ... | p. 3 (3.2. Local Refinement Module) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3.1. Embodied 3D Occupancy Prediction - extractive PDF cue:** Then we detach and put these updated Gaussians back into the memory.
- **p. 3 / 3.1. Embodied 3D Occupancy Prediction - extractive PDF cue:** Different subscripts may correspond to similar positions and perspectives, indicating that the agent has returned to a previously explored location.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 3 (3.1. Embodied 3D Occupancy Prediction), p. 3 (3.1. Embodied 3D Occupancy Prediction).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Depth, Aware, Predicted, Map, Input, T-1, Gaussian, Memory, Occupancy, Load, Update, Image, Encoder, Multi-Scale | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Depth, Aware, Predicted, Map, Input, T-1, Gaussian, Memory, Occupancy, Load | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | Specifically, structure-aware, local, refinement, module, update, relevant, Gaussians, within, current | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Then, detach, updated, Gaussians, back, memory, Different, subscripts, correspond, similar | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3.1. Embodied 3D Occupancy Prediction - extractive PDF cue:** Depth Aware Predicted Depth Map … … Input T-1 Input T … … … … Gaussian Memory T Gaussian Memory T-1 Occupancy T Occupancy T-1 ...
- **p. 2 / 3.1. Embodied 3D Occupancy Prediction - extractive PDF cue:** Conventional methods in indoor scenarios for occupancy prediction accepted RGB-D as inputs to predict the semantic occupancy of a 3D scene which requires depth sensors.
- **p. 3 / 3.1. Embodied 3D Occupancy Prediction - extractive PDF cue:** Recent methods begin to consider endowing models with the same competence, which accept a monocular RGB image as input and derive a 3D occupancy prediction ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Most existing methods [2, 54, 56] still focus on local 3D occupancy prediction by integrating semantic and depth information extracted from the visual inputs.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | To achieve online perception, Online3D [49] introduced an adapter-based model that equips mainstream offline frameworks with the competence to perform online scene ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Embodied occupancy prediction accepts real-time visual inputs continuously and updates the occupancy of the current scene online. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | 6.626 Occ head 39.635 Frame level (ms) Load memory 0.973 Depth aware 1.816 Img backbone 61.478 GS Encoder 14.761 Depthanything 34.687 Update ... | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | 6.626 Occ head 39.635 Frame level (ms) Load memory 0.973 Depth aware 1.816 Img backbone 61.478 GS Encoder 14.761 Depthanything 34.687 Update ... | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** subsection, will, first, explain, local, refinement, module, extracts, semantic, structural, features, monocular, input, integrates, them, update, Gaussian-based, representation, current, frustum.
- **Relevant PDF headings:** 3. Proposed Approach (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Apart from Occ-ScanNet and EmbodiedOcc-ScanNet datasets in the original scale, we sampled a small set from the EmbodiedOcc-ScanNet dataset as the EmbodiedOccScanNet-mini ... | p. 6 (4.1. EmbodiedOcc-ScanNet Benchmark), p. 6 (4.1. EmbodiedOcc-ScanNet Benchmark) |
| Semantic / temporal fusion | We also implemented several state-of-the-art driving scene methods [11, 13, 46] on this benchmark and our local refinement module outperforms them by ... | p. 7 (4.3. Main Results), p. 5 (4.1. EmbodiedOcc-ScanNet Benchmark) |
| Robot query / planning handoff | As shown in Table 1, the results indicate that our local refinement module outperforms ISO [56]. | p. 7 (4.3. Main Results), p. 7 (4.3. Main Results) |

## Failure and Ablation Link

- **p. 7 / 4.4. Experimental Analysis - extractive PDF cue:** Effect of Continuous Online Updating.
- **p. 7 / 4.4. Experimental Analysis - extractive PDF cue:** We analyze the effect of our depth-aware branch in Table 5 using the 26366
- **p. 8 / 4.4. Experimental Analysis - extractive PDF cue:** We analyze the effect of different Gaussian parameters in Table 6 using the Occ-ScanNet-mini2 and the EmbodiedOcc-ScanNet-mini datasets.
- **p. 8 / 4.4. Experimental Analysis - extractive PDF cue:** Due to space limitations, we will use a more diverse set of samples to further show the visual effect of our EmbodiedOcc in the supplementary ...
- **p. 6 / 4.2. Implementation Details - extractive PDF cue:** The depth prediction network used in the depth-aware branch is a fine-tuned DepthAnything-V2 model [51] that remains frozen during the training, and the depth-aware layer ...
- **p. 8 / 4.4. Experimental Analysis - extractive PDF cue:** Due to space limitations, we will use a more diverse set of samples to further show the visual effect of our EmbodiedOcc in the supplementary ...
- **p. 8 / 4.4. Experimental Analysis - extractive PDF cue:** Besides, we replaced DepthAnything-V2 with IndoorDepth [6] in the last row to prove that our depth-aware branch does not rely on a specific depth prediction ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (3.2. Local Refinement Module), p. 3 (3.2. Local Refinement Module), objective p. 3 (3.1. Embodied 3D Occupancy Prediction), p. 3 (3.1. Embodied 3D Occupancy Prediction), temporal p. 2 (2. Related Work), p. 5 (4.1. EmbodiedOcc-ScanNet Benchmark), p. 7 (4.4. Experimental Analysis), p. 8 (4.4. Experimental Analysis), p. 4 (3.3. Gaussian Memory Updated Online), p. 5 (4.1. EmbodiedOcc-ScanNet Benchmark).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
