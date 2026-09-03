# Method - UW-GS: Distractor-Aware 3D Gaussian Splatting for Enhanced Underwater Scene Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/WACV2025/html/Wang_UW-GS_Distractor-Aware_3D_Gaussian_Splatting_for_Enhanced_Underwater_Scene_Reconstruction_WACV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/WACV2025/papers/Wang_UW-GS_Distractor-Aware_3D_Gaussian_Splatting_for_Enhanced_Underwater_Scene_Reconstruction_WACV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (3.1. Problem formulation), p. 4 (3.1. Problem formulation), p. 5 (3.5. Binary Motion Mask), p. 6 (3.6. Loss Function), p. 4 (3.3. Color Appearance Model), p. 3 (3.1. Problem formulation)): Therefore, we propose a new color appearance model and a physical-based density control module in UW-GS.

## Method Body Digest

- **p. 3 / 3.1. Problem formulation - extractive body cue:** Therefore, we propose a new color appearance model and a physical-based density control module in UW-GS.
- **p. 4 / 3.1. Problem formulation - extractive body cue:** In the splatting process, the physical-based density control module addresses densification failures and the binary motion mask handle distractors. we propose a pixel-level mask, named ...
- **p. 5 / 3.5. Binary Motion Mask - extractive body cue:** Inspired by RobustNeRF [35], we introduce a Binary Motion Mask (BMM) ω into our reconstruction loss function to eliminate the distractors as the follows: LRec ...
- **p. 6 / 3.6. Loss Function - extractive body cue:** We use a synthetic ground truth depth map D that is predicted by DepthAnything [47], a novel monocular depth estimation model that can adapt to ...
- **p. 4 / 3.3. Color Appearance Model - extractive body cue:** The modified color for Gaussians is then sent to 3DGS module.
- **p. 3 / 3.1. Problem formulation - extractive body cue:** Recent studies [31, 44, 48] have utilized temporal information to achieve 4D rendering; however, these methods typically model foreground motions with predictable motion trajectory and ...
- **p. 5 / 3.6. Loss Function - extractive body cue:** The final loss function, L, used for optimization, comprises a reconstruction loss LRec (see subsection 3.5), a 3284
- **p. 4 / 3.4. Physical-based Density Control - extractive body cue:** However, in underwater scenes, Equation 3 suggests that δLRec δcolor is calculated from T D · δLRec δcolorobject so that each Gaussian color gradient has ...

## Design Rationale

- **p. 4 / 3.3. Color Appearance Model - extractive body cue:** To address this issue, we propose a novel approach for color appearance formation.
- **p. 1 / 1. Introduction - extractive body cue:** To address the aforementioned issues, we propose a new Gaussian Splatting (GS)-based method, UW-GS, specifically for underwater scenes.
- **p. 2 / 1. Introduction - extractive body cue:** We also incorporated pseudo-depth maps generated from DepthAnything [47], trained with more general scenes, to enhance the robustness of our method.

## Source Evidence Cues

- **p. 3 / 3.1. Problem formulation - extractive body cue:** Therefore, we propose a new color appearance model and a physical-based density control module in UW-GS.
- **p. 4 / 3.1. Problem formulation - extractive body cue:** In the splatting process, the physical-based density control module addresses densification failures and the binary motion mask handle distractors. we propose a pixel-level mask, named ...
- **p. 5 / 3.5. Binary Motion Mask - extractive body cue:** Inspired by RobustNeRF [35], we introduce a Binary Motion Mask (BMM) ω into our reconstruction loss function to eliminate the distractors as the follows: LRec ...
- **p. 6 / 3.6. Loss Function - extractive body cue:** We use a synthetic ground truth depth map D that is predicted by DepthAnything [47], a novel monocular depth estimation model that can adapt to ...
- **p. 4 / 3.3. Color Appearance Model - extractive body cue:** The modified color for Gaussians is then sent to 3DGS module.
- **p. 3 / 3.1. Problem formulation - extractive body cue:** Recent studies [31, 44, 48] have utilized temporal information to achieve 4D rendering; however, these methods typically model foreground motions with predictable motion trajectory and ...
- **p. 5 / 3.6. Loss Function - extractive body cue:** The final loss function, L, used for optimization, comprises a reconstruction loss LRec (see subsection 3.5), a 3284
- **Detected method headings:** 3. Method (p. 3); 3.3. Color Appearance Model (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Therefore, we propose a new color appearance model and a physical-based density control module in UW-GS. | p. 3 (3.1. Problem formulation), p. 4 (3.1. Problem formulation) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | In the splatting process, the physical-based density control module addresses densification failures and the binary motion mask handle distractors. we propose a ... | p. 4 (3.1. Problem formulation), p. 5 (3.5. Binary Motion Mask) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Inspired by RobustNeRF [35], we introduce a Binary Motion Mask (BMM) ω into our reconstruction loss function to eliminate the distractors as ... | p. 5 (3.5. Binary Motion Mask), p. 6 (3.6. Loss Function) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.4. Physical-based Density Control - extractive body cue:** However, in underwater scenes, Equation 3 suggests that δLRec δcolor is calculated from T D · δLRec δcolorobject so that each Gaussian color gradient has ...
- **p. 6 / 3.6. Loss Function - extractive body cue:** This loss is developed based on the underwater image formation model Equation 3, resulting in the approximate depth per Gaussian can be calculated in the ...
- **p. 5 / 3.6. Loss Function - extractive body cue:** The final loss function, L, used for optimization, comprises a reconstruction loss LRec (see subsection 3.5), a 3284
- **p. 5 / 3.4. Physical-based Density Control - extractive body cue:** Furthermore, by adjusting the 2D position gradient, this method optimizes regions where object color information is substantially attenuated, thereby enhancing 3DGS performance in areas characterized ...
- **p. 3 / 3.1. Problem formulation - extractive body cue:** However, Equation 2 is insufficient for representing the underwater scenes [39].
- **p. 3 / 3.1. Problem formulation - extractive body cue:** During training, the 2D position gradient, an intermediate result in backward propagation, is used as evidence to indicate "color under-represented" issues [23].
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (3.4. Physical-based Density Control), p. 6 (3.6. Loss Function), p. 3 (3.1. Problem formulation), p. 3 (3.1. Problem formulation), p. 4 (3.4. Physical-based Density Control), p. 5 (3.4. Physical-based Density Control).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Gaussians, modified, color, will, sent, projection, then, generate, pixel, rasterization, module, output, final, underwater | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Gaussians, modified, color, will, sent, projection, then, generate, pixel, rasterization | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | address, issue, novel, color, appearance, formation, aforementioned, issues, Gaussian, Splatting | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | However, underwater, scenes, Equation, suggests, LRec, color, calculated, colorobject, Gaussian | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.2. Overview of UW-GS - extractive body cue:** The 3D Gaussians with modified color will be sent to do 2D projection and then generate pixel color in rasterization module to output the final ...
- **p. 4 / 3.3. Color Appearance Model - extractive body cue:** Similar to [25], we use an additional MLP f with positon encoded depth and viewing direction input to estimate medium properties: (T D i , ...
- **p. 6 / 3.6. Loss Function - extractive body cue:** Lca imposes restrictions on T D and T B, which are closely related to the depth.
- **p. 6 / 3.6. Loss Function - extractive body cue:** In 3DGS, we can render depth maps in a similar way as image: ˆD = X i∈N αizi i-1 Y j=1 (1 -αj).
- **p. 3 / 3.1. Problem formulation - extractive body cue:** 3D Gaussian Splatting (3DGS) is a point-based approach that uses discrete Gaussian point clouds to represent a 3D scene.
- **p. 3 / 3.1. Problem formulation - extractive body cue:** Based on its average value, the sparse point cloud obtained from COLMAP [36] is adaptively grown by splitting and cloning.
- **p. 5 / 3.4. Physical-based Density Control - extractive body cue:** As a result, the point clouds at larger scales exhibit improved representational capability, thereby reducing both blur and needle-like artifacts.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Recent studies [31, 44, 48] have utilized temporal information to achieve 4D rendering; however, these methods typically model foreground motions with predictable ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | In the standard 3DGS framework, the Gaussian point cloud is densified adaptively to acquire better representation capability. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | Moreover, to avoid high-frequency content being treated as outliers, every 8 × 8 patch R8×8 is classified according to the average value ... | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 4. Experiment Configuration - extractive body cue:** For training, we carried out 15,000 iterations in a single RTX3090 GPU.
- **p. 6 / 4. Experiment Configuration - extractive body cue:** We used their official implementation, but trained on the same sequence using the same dataset split strategy.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Therefore, color, appearance, model, physical-based, density, control, module, UW-GS, splatting, process, addresses, densification, failures, binary, motion, mask, handle, distractors, pixel-level.
- **Relevant PDF headings:** 3. Method (p. 3); 3.3. Color Appearance Model (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | On the other hand, we will also use these three metrics in dynamic scenes after using motion mask provided from dataset to ... | p. 7 (4. Experiment Configuration), p. 6 (4. Experiment Configuration) |
| Semantic / temporal fusion | We tested our method and compared with three state of the arts: Instant-NGP [33], SeaThru-NeRF [26], and original 3DGS [22]. | p. 6 (4. Experiment Configuration), p. 7 (5. Results and Discussion) |
| Robot query / planning handoff | For the SeaThru-NeRF dataset, our method shows the best overall performance and achieves average 2.09dB and 2.70dB PSNR improvement compared to 3DGS ... | p. 7 (5. Results and Discussion), p. 8 (5. Results and Discussion) |

## Failure and Ablation Link

- **p. 8 / Figure/Table caption - extractive body cue:** Figure 7. Examples of rendering results from Composite and Sar- dine scenes. From left to right: raw videos, results without and with BMM, respectively. restored ...
- **p. 8 / 5. Results and Discussion - extractive body cue:** We isolate our contributions using a set of modified architectures: (V1) solely using spherical harmonics to represent view-dependent color (note that MLP will also assist ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Additionally, underwater scenes typically contain moving elements, such as fish and floating debris, increas- ing complexity. These elements are frequently referred to as ...
- **p. 8 / 5. Results and Discussion - extractive body cue:** The improvement of our method is not obvious in the shallow underwater scene because the disturbance of light from above the water cannot be neglected.
- **p. 7 / 5. Results and Discussion - extractive body cue:** The limited improvement compared to 3DGS can be attributed to the unstable lighting from above the water surface.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. The diagram of our proposed UW-GS approach, combining a novel color appearance model, physical-based density control and binary motion mask to 3DGS. Our ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Left: Diagram of 2D Position gradient calculation. Right: Illustration of densification failures (G2 highlighted in orange) that appear to be not cloned or ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (3.1. Problem formulation), p. 4 (3.1. Problem formulation), p. 5 (3.5. Binary Motion Mask), p. 6 (3.6. Loss Function), p. 4 (3.3. Color Appearance Model), p. 3 (3.1. Problem formulation), objective p. 4 (3.4. Physical-based Density Control), p. 6 (3.6. Loss Function), p. 5 (3.6. Loss Function), p. 5 (3.4. Physical-based Density Control), p. 3 (3.1. Problem formulation), p. 3 (3.1. Problem formulation), temporal p. 3 (3.1. Problem formulation), p. 4 (3.4. Physical-based Density Control), p. 5 (3.5. Binary Motion Mask), p. 6 (4. Experiment Configuration), p. 6 (4. Experiment Configuration), p. 1 (Abstract).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
