# Method - 3D Geometry-Aware Deformable Gaussian Splatting for Dynamic View Synthesis

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Lu_3D_Geometry-Aware_Deformable_Gaussian_Splatting_for_Dynamic_View_Synthesis_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Lu_3D_Geometry-Aware_Deformable_Gaussian_Splatting_for_Dynamic_View_Synthesis_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3.2. Gaussian Canonical Field), p. 5 (3.5. Optimization), p. 5 (3.5. Optimization), p. 4 (3.2. Gaussian Canonical Field), p. 3 (3. Method)): Then, we propose a geometric branch, which enables geometry feature learning of the 3D Gaussian distributions for the subsequent deformation field.

## Method Body Digest

- **p. 4 / 3.2. Gaussian Canonical Field - extractive body cue:** Then, we propose a geometric branch, which enables geometry feature learning of the 3D Gaussian distributions for the subsequent deformation field.
- **p. 5 / 3.5. Optimization - extractive body cue:** To optimize the model, we use the photometric loss, and a motion loss, and also adapt the density control from 3DGS [21] with our modifications.
- **p. 5 / 3.5. Optimization - extractive body cue:** The photometric loss consists of the L1 loss and structural similarity loss LD-SSIM between the rendered image ˆCt and ground truth image Ct.
- **p. 4 / 3.2. Gaussian Canonical Field - extractive body cue:** Compared with the quaternion representation used in 3D-GS, the 6D rotation representation can benefit our method in estimating the deformation of each Gaussian from canonical ...
- **p. 3 / 3. Method - extractive body cue:** Finally, we present our losses and density control modifications in Sec.
- **p. 5 / 3.4. Rasterization - extractive body cue:** Gaussian Canonical Field Deformation Field RGB Gradient 𝑓𝑡 -1(Δ𝑥𝑡, Δ𝑟𝑡, Δ𝑠𝑡) (𝑥𝑡,𝑐, 𝑟𝑡,𝑠𝑡, o) 𝑓𝑡(Δ𝑥𝑡, Δ𝑟𝑡,Δ𝑠𝑡) Deformation Transformation Inverse Deformation Transformation Loss Density Control Figure ...
- **p. 4 / 3.2. Gaussian Canonical Field - extractive body cue:** Taking V as input, we perform sparse 3D U-Net to aggregate local features (dubbed as Fv ∈RM×C) of the point clouds.
- **p. 3 / 3. Method - extractive body cue:** Given a set of images or monocular video of a dynamic scene with frames with corresponding time labels and known camera intrinsic and extrinsic parameters, ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are summarized as: • We propose a geometry-aware feature extraction network based on 3D Gaussian distribution to better utilize local geometric information. ...
- **p. 3 / 3. Method - extractive body cue:** Our method mainly consists of two core components: the Gaussian canonical field is used to learn the reconstruction of static scenes, while the deformation field ...
- **p. 4 / 3.2. Gaussian Canonical Field - extractive body cue:** Then, we propose a geometric branch, which enables geometry feature learning of the 3D Gaussian distributions for the subsequent deformation field.

## Source Evidence Cues

- **p. 4 / 3.2. Gaussian Canonical Field - extractive body cue:** Then, we propose a geometric branch, which enables geometry feature learning of the 3D Gaussian distributions for the subsequent deformation field.
- **p. 5 / 3.5. Optimization - extractive body cue:** To optimize the model, we use the photometric loss, and a motion loss, and also adapt the density control from 3DGS [21] with our modifications.
- **p. 5 / 3.5. Optimization - extractive body cue:** The photometric loss consists of the L1 loss and structural similarity loss LD-SSIM between the rendered image ˆCt and ground truth image Ct.
- **p. 4 / 3.2. Gaussian Canonical Field - extractive body cue:** Compared with the quaternion representation used in 3D-GS, the 6D rotation representation can benefit our method in estimating the deformation of each Gaussian from canonical ...
- **p. 3 / 3. Method - extractive body cue:** Finally, we present our losses and density control modifications in Sec.
- **Detected method headings:** 3. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Then, we propose a geometric branch, which enables geometry feature learning of the 3D Gaussian distributions for the subsequent deformation field. | p. 4 (3.2. Gaussian Canonical Field), p. 5 (3.5. Optimization) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | To optimize the model, we use the photometric loss, and a motion loss, and also adapt the density control from 3DGS [21] ... | p. 5 (3.5. Optimization), p. 5 (3.5. Optimization) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | The photometric loss consists of the L1 loss and structural similarity loss LD-SSIM between the rendered image ˆCt and ground truth image ... | p. 5 (3.5. Optimization), p. 4 (3.2. Gaussian Canonical Field) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.4. Rasterization - extractive body cue:** Gaussian Canonical Field Deformation Field RGB Gradient 𝑓𝑡 -1(Δ𝑥𝑡, Δ𝑟𝑡, Δ𝑠𝑡) (𝑥𝑡,𝑐, 𝑟𝑡,𝑠𝑡, o) 𝑓𝑡(Δ𝑥𝑡, Δ𝑟𝑡,Δ𝑠𝑡) Deformation Transformation Inverse Deformation Transformation Loss Density Control Figure ...
- **p. 5 / 3.5. Optimization - extractive body cue:** To optimize the model, we use the photometric loss, and a motion loss, and also adapt the density control from 3DGS [21] with our modifications.
- **p. 3 / 3. Method - extractive body cue:** Finally, we present our losses and density control modifications in Sec.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (3.4. Rasterization), p. 3 (3. Method), p. 5 (3.5. Optimization).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Taking, input, perform, sparse, U-Net, aggregate, local, features, dubbed, point, clouds, Given, images, monocular | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Taking, input, perform, sparse, U-Net, aggregate, local, features, dubbed, point | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | main, contributions, summarized, geometry-aware, feature, extraction, network, Gaussian, distribution, better | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Gaussian, Canonical, Field, Deformation, RGB, Gradient, Transformation, Inverse, Loss, Density | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.2. Gaussian Canonical Field - extractive body cue:** Taking V as input, we perform sparse 3D U-Net to aggregate local features (dubbed as Fv ∈RM×C) of the point clouds.
- **p. 3 / 3. Method - extractive body cue:** Given a set of images or monocular video of a dynamic scene with frames with corresponding time labels and known camera intrinsic and extrinsic parameters, ...
- **p. 1 / 1. Introduction - extractive body cue:** Due to the inherent motion/shape ambiguity in monocular dynamic 3D representation, dynamic scene modeling and synthesis are more challenging, especially for monocular video with limited ...
- **p. 1 / 1. Introduction - extractive body cue:** Dynamic View Synthesis (DVS) aims at rendering novel photorealistic views at arbitrary viewpoints and any input time step given a monocular video of a dynamic ...
- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are summarized as: • We propose a geometry-aware feature extraction network based on 3D Gaussian distribution to better utilize local geometric information. ...
- **p. 4 / 3.2. Gaussian Canonical Field - extractive body cue:** The identity branch uses a multi-layer perception (MLP) to map the 3D coordinate of the point cloud into the embedding space (dubbed as Fp ∈RN×C) ...
- **p. 2 / 1. Introduction - extractive body cue:** We introduce the continuous 6D rotation [68] to ensure that the network learns a continuous function in the parameter space, which accurately represents the rotational ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | 3.3, we propose a 3D geometry-aware deformation field to learn transformations for given time steps, which transform our canonical 3D Gaussian distributions ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Dynamic View Synthesis (DVS) aims at rendering novel photorealistic views at arbitrary viewpoints and any input time step given a monocular video ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / 4.3. Quantitative Results - extractive body cue:** The computational costs are: training time around 2h (avg. on D-NeRF dataset), render FPS 12 (fixed viewpoint), model size (34MB points cloud + 14MB network).

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Then, geometric, branch, enables, geometry, feature, learning, Gaussian, distributions, subsequent, deformation, field, optimize, model, photometric, loss, motion, adapt, density, control.
- **Relevant PDF headings:** 3. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | The synthetic dataset D-NeRF [37] contains 8 dynamic scenes, including Hell Warrior, Mutant, Hook, Bouncing Balls, Lego, T-Rex, Stand Up, and Jumping ... | p. 6 (4.1. Dataset), p. 6 (4.1. Dataset) |
| Semantic / temporal fusion | It can be observed that our method achieves good performance compared with other state-of-the-art methods. | p. 7 (4.3. Quantitative Results), p. 7 (4.3. Quantitative Results) |
| Robot query / planning handoff | Compared with the results (dubbed as "PointNet feat." and "Plane feat.") in Table 4, it can be observed that our method achieves ... | p. 8 (4.5. Ablation Study), p. 7 (4.3. Quantitative Results) |

## Failure and Ablation Link

- **p. 8 / 4.5. Ablation Study - extractive body cue:** We conduct ablation studies on the synthetic dataset (800× 800) to verify the effectiveness of our proposed components.
- **p. 8 / 4.5. Ablation Study - extractive body cue:** To study the effect of 6D representation of the rotation parameters of the 3D Gaussian, we conduct an experiment that replaces the 6D vector with ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. The pipeline of our proposed 3D geometry-aware deformable Gaussian splitting. In the Gaussian canonical field, we reconstruct a static scene in canonical space ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2. Given a set of images or monocular video of a dy- namic scene with frames with corresponding time labels and known camera intrinsic ...
- **p. 8 / 5. Conclusion - extractive body cue:** We addressed the limitations of existing approaches from two perspectives: 1) we introduced 3D sparse convolution to extract local structural information effectively and efficiently for ...
- **p. 7 / 4.4. Visualization Results - extractive body cue:** Since 3D-DS cannot model dynamic scenes, the quality of the point cloud is poor.
- **p. 7 / 4.3. Quantitative Results - extractive body cue:** Since it inherently cannot model the deformation of the dynamic scene, 3D-GS performs poorly in dynamic view synthesis.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3.2. Gaussian Canonical Field), p. 5 (3.5. Optimization), p. 5 (3.5. Optimization), p. 4 (3.2. Gaussian Canonical Field), p. 3 (3. Method), objective p. 5 (3.4. Rasterization), p. 5 (3.5. Optimization), p. 3 (3. Method), temporal p. 3 (3. Method), p. 1 (1. Introduction), p. 3 (3. Method), p. 7 (4.3. Quantitative Results), p. 2 (2.2. Dynamic View Synthesis), p. 2 (2.1. Novel View Synthesis).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
