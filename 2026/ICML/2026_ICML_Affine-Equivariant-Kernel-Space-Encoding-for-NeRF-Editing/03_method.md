# Method - Affine-Equivariant Kernel Space Encoding for NeRF Editing

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=fAj3MJghc0; PDF retrieval source: https://openreview.net/pdf/048e4b5756022f2faa8898f0f2d379b85079ab58.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (4. Proposed Method), p. 4 (4. Proposed Method), p. 5 (4. Proposed Method), p. 6 (4. Proposed Method), p. 5 (4. Proposed Method), p. 6 (4. Proposed Method)): Specifically, we use a set of Gaussian kernels, enhanced with a trainable latent feature vector v ∈Rn.

## Method Body Digest

- **p. 4 / 4. Proposed Method - extractive PDF cue:** Specifically, we use a set of Gaussian kernels, enhanced with a trainable latent feature vector v ∈Rn.
- **p. 4 / 4. Proposed Method - extractive PDF cue:** We use a NeRF-based neural network F to predict colour and opacity from the nearest Gaussian features.
- **p. 5 / 4. Proposed Method - extractive PDF cue:** To address this limitation, we introduce a Hash Grid Feature Distillation mechanism, which decouples the feature representation from the underlying grid vertices and transfers it ...
- **p. 6 / 4. Proposed Method - extractive PDF cue:** As a result, the latent features remain coherent after deformation, ensuring that modifications produce smooth, stable, and physically consistent updates in the rendered scene without ...
- **p. 5 / 4. Proposed Method - extractive PDF cue:** During training, both the hash-grid parameters Φ and the Gaussian positions µi are optimized jointly, allowing the Gaussians to explore the multi-resolution feature space and ...
- **p. 6 / 4. Proposed Method - extractive PDF cue:** Pruning and Densification To enable Gaussian kernels to better represent the latent feature space, we adopt densification and pruning strategies that regulate the number of ...
- **p. 5 / 4. Proposed Method - extractive PDF cue:** The Gaussian features v(x) are sampled from the hash-grid encoding at the kernel centres, formally described as: v (x) = k X i=1 wi(x, G) ...
- **p. 6 / 4. Proposed Method - extractive PDF cue:** For densification, we follow the approach of (Kerbl et al., 2023), tracking Gaussian means via their gradients and cloning or splitting Gaussians accordingly.

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** In this work, we introduce Affine-Equivariant Kernel Space Encoding (EKS), a novel positional encoding mechanism for NeRFs.
- **p. 6 / 4. Proposed Method - extractive PDF cue:** Interpolation between these modified Gaussians then enables the system to synthesize novel views of the edited scene.
- **p. 4 / 4. Proposed Method - extractive PDF cue:** Our method, called EKS, integrates affine-equvariant transformation properties of Gaussian kernels and a neural network-based rendering procedure into a single system.

## Source Evidence Cues

- **p. 4 / 4. Proposed Method - extractive PDF cue:** Specifically, we use a set of Gaussian kernels, enhanced with a trainable latent feature vector v ∈Rn.
- **p. 4 / 4. Proposed Method - extractive PDF cue:** We use a NeRF-based neural network F to predict colour and opacity from the nearest Gaussian features.
- **p. 5 / 4. Proposed Method - extractive PDF cue:** To address this limitation, we introduce a Hash Grid Feature Distillation mechanism, which decouples the feature representation from the underlying grid vertices and transfers it ...
- **p. 6 / 4. Proposed Method - extractive PDF cue:** As a result, the latent features remain coherent after deformation, ensuring that modifications produce smooth, stable, and physically consistent updates in the rendered scene without ...
- **p. 5 / 4. Proposed Method - extractive PDF cue:** During training, both the hash-grid parameters Φ and the Gaussian positions µi are optimized jointly, allowing the Gaussians to explore the multi-resolution feature space and ...
- **p. 6 / 4. Proposed Method - extractive PDF cue:** Pruning and Densification To enable Gaussian kernels to better represent the latent feature space, we adopt densification and pruning strategies that regulate the number of ...
- **Detected method headings:** 4. Proposed Method (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Specifically, we use a set of Gaussian kernels, enhanced with a trainable latent feature vector v ∈Rn. | p. 4 (4. Proposed Method), p. 4 (4. Proposed Method) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | We use a NeRF-based neural network F to predict colour and opacity from the nearest Gaussian features. | p. 4 (4. Proposed Method), p. 5 (4. Proposed Method) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | To address this limitation, we introduce a Hash Grid Feature Distillation mechanism, which decouples the feature representation from the underlying grid vertices ... | p. 5 (4. Proposed Method), p. 6 (4. Proposed Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 4. Proposed Method - extractive PDF cue:** The Gaussian features v(x) are sampled from the hash-grid encoding at the kernel centres, formally described as: v (x) = k X i=1 wi(x, G) ...
- **p. 6 / 4. Proposed Method - extractive PDF cue:** For densification, we follow the approach of (Kerbl et al., 2023), tracking Gaussian means via their gradients and cloning or splitting Gaussians accordingly.
- **p. 5 / 4. Proposed Method - extractive PDF cue:** During training, both the hash-grid parameters Φ and the Gaussian positions µi are optimized jointly, allowing the Gaussians to explore the multi-resolution feature space and ...
- **p. 6 / 4. Proposed Method - extractive PDF cue:** By monitoring these axes, we can both restore view-dependent features and update the anisotropic scales of the Gaussians consistently after deformation.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (4. Proposed Method), p. 6 (4. Proposed Method), p. 6 (4. Proposed Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | model, alongside, standard, NeRF, input, takes, trainable, Gaussians, outputs, colour, density, query, point, enabling | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | model, alongside, standard, NeRF, input, takes, trainable, Gaussians, outputs, colour | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | introduce, Affine-Equivariant, Kernel, Space, Encoding, EKS, novel, positional, mechanism, NeRFs | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Gaussian, features, sampled, hash-grid, encoding, kernel, centres, formally, described, Henc | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 4. Proposed Method - extractive PDF cue:** The model, alongside the standard NeRF input, takes a set of trainable Gaussians G and outputs colour c and density σ at any query point, ...
- **p. 4 / 3. Preliminary - extractive PDF cue:** The edited Gaussians are passed through the same rendering pipeline to generate the final image, with the view-direction input to F adjusted by the inverse ...
- **p. 3 / 3. Preliminary - extractive PDF cue:** For a query point x, the output feature vector v is obtained by concatenating trilinearly interpolated features from all levels, based on x's position within ...
- **p. 5 / 4. Proposed Method - extractive PDF cue:** Since interpolation operates solely over these Gaussian features, any adjustments to Gaussian positions, rotations, or scales directly modify the rendered output.
- **p. 3 / 3. Preliminary - extractive PDF cue:** The goal is to minimize the difference between the rendered and ground-truth images, allowing the MLP to implicitly encode both the geometry and appearance of ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Motivated by these observations, we address a fundamental limitation in NeRF editing task: the absence of a transformation-aware space encoding.
- **p. 2 / 1. Introduction - extractive PDF cue:** Recent advances in explicitly parametrized scene representations demonstrate that spatial locality and explicit structure can substantially improve editability and interaction (Kerbl et al., 2023; Malarz ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | This highlights the potential of EKS as a flexible framework for neural scene editing driven by physical interactions. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Several approaches focus on modeling deformation or displacement fields at a per-frame level (Park et al., 2021a;b; Tretschk et al., 2021; Weng ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 4. Proposed Method - extractive PDF cue:** Specifically, we use a set of Gaussian kernels, enhanced with a trainable latent feature vector v ∈Rn.
- **p. 6 / 4. Proposed Method - extractive PDF cue:** As a result, the latent features remain coherent after deformation, ensuring that modifications produce smooth, stable, and physically consistent updates in the rendered scene without ...
- **p. 5 / 4. Proposed Method - extractive PDF cue:** During training, both the hash-grid parameters Φ and the Gaussian positions µi are optimized jointly, allowing the Gaussians to explore the multi-resolution feature space and ...
- **p. 6 / 4. Proposed Method - extractive PDF cue:** Pruning and Densification To enable Gaussian kernels to better represent the latent feature space, we adopt densification and pruning strategies that regulate the number of ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Specifically, Gaussian, kernels, enhanced, trainable, latent, feature, vector, NeRF-based, neural, network, predict, colour, opacity, nearest, features, address, limitation, introduce, Hash.
- **Relevant PDF headings:** 4. Proposed Method (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Additionally to synthetic data we trained our NeRF model trained on the Mip-NeRF 360 dataset (Barron et al., 2022), comprising five outdoor ... | p. 6 (5. Experiments), p. 7 (5. Experiments) |
| Semantic / temporal fusion | We design our experiments to demonstrate that EKS maintains the reconstruction quality of state-of-the-art (SOTA) methods while enabling complex object modifications. | p. 6 (5. Experiments), p. 6 (5. Experiments) |
| Robot query / planning handoff | These baselines are selected to demonstrate that EKS not only achieves reconstruction quality comparable to or exceeding SOTA methods, while enabling editing ... | p. 6 (5. Experiments), p. 6 (5. Experiments) |

## Failure and Ablation Link

- **p. 8 / 5. Experiments - extractive PDF cue:** We evaluate variants that (1) replace RT-GPS with Euclidean KNN (w/o RT-GPS), (2) remove hash-grid feature distillation and use learned per-Gaussian features (w/o Henc), and ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 10. Ablation study. Qualitative comparison showing the effect of individual components on rendering quality. ized, and deformation-aware scene editing. By representing latent features with ...
- **p. 7 / 5. Experiments - extractive PDF cue:** In the Drums scene, the gong is consistently restored without visible holes.
- **p. 7 / 5. Experiments - extractive PDF cue:** Affine-Equivariant Kernel Space Encoding for NeRF Editing Chair Drums Lego Mic Materials Ship Hotdog Ficus Non Editable INGP 31.97 22.67 33.44 31.38 22.66 28.83 34.04 ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2. Physical simulations. From left to right: (1) Rigid body simulation of falling leaves. (2) Soft body simulation of the Lego dozer being squished. ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2. Physical simulations. From left to right: (1) Rigid body simulation of falling leaves. (2) Soft body simulation of the Lego dozer being squished. ...
- **p. 8 / 6. Conclusions - extractive PDF cue:** By representing latent features with anisotropic Gaussian kernels and aggregating them using Mahalanobis-distance-based neighbourhoods, our method preserves local feature structure under affine transformations, addressing a ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (4. Proposed Method), p. 4 (4. Proposed Method), p. 5 (4. Proposed Method), p. 6 (4. Proposed Method), p. 5 (4. Proposed Method), p. 6 (4. Proposed Method), objective p. 5 (4. Proposed Method), p. 6 (4. Proposed Method), p. 5 (4. Proposed Method), p. 6 (4. Proposed Method), temporal p. 7 (5. Experiments), p. 2 (2. Related Works), p. 2 (2. Related Works), p. 3 (3. Preliminary), p. 3 (2. Related Works).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
