# Method - QuickSplat: Fast 3D Surface Reconstruction via Learned Gaussian Initialization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Liu_QuickSplat_Fast_3D_Surface_Reconstruction_via_Learned_Gaussian_Initialization_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Liu_QuickSplat_Fast_3D_Surface_Reconstruction_via_Learned_Gaussian_Initialization_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3.3. Iterative Gaussian Optimization), p. 3 (3.2. Initialization Prior), p. 4 (3.3. Iterative Gaussian Optimization), p. 3 (3.2. Initialization Prior), p. 5 (3.3. Iterative Gaussian Optimization), p. 5 (3.3. Iterative Gaussian Optimization)): Top: the densifier network predicts a pool of additional voxel features in an encoder-decoder architecture from the current Gaussians and their gradients as input.

## Method Body Digest

- **p. 4 / 3.3. Iterative Gaussian Optimization - extractive body cue:** Top: the densifier network predicts a pool of additional voxel features in an encoder-decoder architecture from the current Gaussians and their gradients as input.
- **p. 3 / 3.2. Initialization Prior - extractive body cue:** In contrast to SGNN, which produces sparse voxel outputs, we employ a decoder MLP to interpret the densified voxel latent features as output Gaussian primitives.
- **p. 4 / 3.3. Iterative Gaussian Optimization - extractive body cue:** To this end, we introduce another learnable component, the densifier network θD, that predicts additional voxel features in free space.
- **p. 3 / 3.2. Initialization Prior - extractive body cue:** Inspired by SGNN [14], this network comprises sparse 3D convolutions in an encoder-decoder architecture.
- **p. 5 / 3.3. Iterative Gaussian Optimization - extractive body cue:** Densification-Optimization Loop We utilize both networks, θD and θO, in our proposed densificationoptimization loop, that grows and improves the latent voxel features over multiple timesteps.
- **p. 5 / 3.3. Iterative Gaussian Optimization - extractive body cue:** By training the densifier network end-to-end with the optimizer, we instead learn to map the current state of Gaussians and their gradients into new, high-contribution ...
- **p. 8 / 4.3. Limitations - extractive body cue:** First, our method struggles with mirror reflections, since the photometric loss encourages to reconstruct the reflected geometry behind the mirror, which leads to noisy artifacts.
- **p. 3 / 3. Method - extractive body cue:** Initializer SfM points New GS Densifier Optimizer Gradients Rendering loss Update Gaussian parameters iteratively Gaussians Gradients Updates Concat new GS with Before After Figure 2.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** To summarize, our contributions are: • We propose a learned, generalized initializer network, that leverages scene priors to create effective Gaussian initializations for more efficient ...
- **p. 2 / 1. Introduction - extractive body cue:** To this end, we propose a novel generalized prior for 3D surface reconstruction.
- **p. 3 / 3.2. Initialization Prior - extractive body cue:** The first step in our method is to create an initialization of all Gaussians G.

## Source Evidence Cues

- **p. 4 / 3.3. Iterative Gaussian Optimization - extractive body cue:** Top: the densifier network predicts a pool of additional voxel features in an encoder-decoder architecture from the current Gaussians and their gradients as input.
- **p. 3 / 3.2. Initialization Prior - extractive body cue:** In contrast to SGNN, which produces sparse voxel outputs, we employ a decoder MLP to interpret the densified voxel latent features as output Gaussian primitives.
- **p. 4 / 3.3. Iterative Gaussian Optimization - extractive body cue:** To this end, we introduce another learnable component, the densifier network θD, that predicts additional voxel features in free space.
- **p. 3 / 3.2. Initialization Prior - extractive body cue:** Inspired by SGNN [14], this network comprises sparse 3D convolutions in an encoder-decoder architecture.
- **p. 5 / 3.3. Iterative Gaussian Optimization - extractive body cue:** Densification-Optimization Loop We utilize both networks, θD and θO, in our proposed densificationoptimization loop, that grows and improves the latent voxel features over multiple timesteps.
- **p. 5 / 3.3. Iterative Gaussian Optimization - extractive body cue:** By training the densifier network end-to-end with the optimizer, we instead learn to map the current state of Gaussians and their gradients into new, high-contribution ...
- **p. 8 / 4.3. Limitations - extractive body cue:** First, our method struggles with mirror reflections, since the photometric loss encourages to reconstruct the reflected geometry behind the mirror, which leads to noisy artifacts.
- **Detected method headings:** 3. Method (p. 2); Method (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Top: the densifier network predicts a pool of additional voxel features in an encoder-decoder architecture from the current Gaussians and their gradients ... | p. 4 (3.3. Iterative Gaussian Optimization), p. 3 (3.2. Initialization Prior) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | In contrast to SGNN, which produces sparse voxel outputs, we employ a decoder MLP to interpret the densified voxel latent features as ... | p. 3 (3.2. Initialization Prior), p. 4 (3.3. Iterative Gaussian Optimization) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | To this end, we introduce another learnable component, the densifier network θD, that predicts additional voxel features in free space. | p. 4 (3.3. Iterative Gaussian Optimization), p. 3 (3.2. Initialization Prior) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3. Method - extractive body cue:** Initializer SfM points New GS Densifier Optimizer Gradients Rendering loss Update Gaussian parameters iteratively Gaussians Gradients Updates Concat new GS with Before After Figure 2.
- **p. 5 / 3.3. Iterative Gaussian Optimization - extractive body cue:** Similarly to G3R [10], we detach the gradient of the losses for the subsequent timesteps, i.e., we optimize them separately.
- **p. 4 / 3.3. Iterative Gaussian Optimization - extractive body cue:** Concretely, we render the training images and compute the gradients of the rendering loss Eq.
- **p. 3 / 3.1. Surface Representation - extractive body cue:** (2) Regularizers like normal, or distortion loss [4] are also applied in addition to Lc.
- **p. 4 / 3.2. Initialization Prior - extractive body cue:** It comprises a binary cross-entropy loss on the occupancy of each voxel.
- **p. 5 / 3.3. Iterative Gaussian Optimization - extractive body cue:** We run the densification-optimization loop for T=5 timesteps and calculate the losses after each timestep.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 3 (3. Method), p. 4 (3.3. Iterative Gaussian Optimization), p. 5 (3.3. Iterative Gaussian Optimization), p. 5 (3.3. Iterative Gaussian Optimization), p. 3 (3. Method), p. 4 (3.2. Initialization Prior).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | reconstructs, surface, large-scale, indoor, scenes, posed, images, input, learn, several, sparse, CNN-based, networks, jointly | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | reconstructs, surface, large-scale, indoor, scenes, posed, images, input, learn, several | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | summarize, contributions, learned, generalized, initializer, network, leverages, scene, priors, create | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Initializer, SfM, points, New, Densifier, Optimizer, Gradients, Rendering, loss, Update | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 3. Method - extractive body cue:** Our method reconstructs the surface of large-scale indoor scenes from posed images as input.
- **p. 2 / 1. Introduction - extractive body cue:** We learn several sparse 3D CNN-based networks that jointly produce Gaussian parameters from the input posed multi-view images.
- **p. 3 / 3. Method - extractive body cue:** From the SfM points of input multi-view images, our initializer network predicts an initial set of Gaussians G0.
- **p. 5 / 3.3. Iterative Gaussian Optimization - extractive body cue:** By training the densifier network end-to-end with the optimizer, we instead learn to map the current state of Gaussians and their gradients into new, high-contribution ...
- **p. 1 / 1. Introduction - extractive body cue:** Recently, 3D Gaussian Splatting (3DGS) [27] achieves photorealistic novel-view-synthesis from multi-view images as input.
- **p. 1 / 1. Introduction - extractive body cue:** Additionally, the surface is only optimized from the observed input images, but capturing sufficiently many diverse images remains challenging for large scenes.
- **p. 3 / 3.2. Initialization Prior - extractive body cue:** In contrast to SGNN, which produces sparse voxel outputs, we employ a decoder MLP to interpret the densified voxel latent features as output Gaussian primitives.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Similar to G3R [10], we frame this process over multiple timesteps t, i.e., we iteratively calculate ∇Gt, predict ∆Gt, and update our ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | In other words, we densify more for earlier timesteps and then gradually reduce the number of new voxels. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.3. Iterative Gaussian Optimization - extractive body cue:** By training the densifier network end-to-end with the optimizer, we instead learn to map the current state of Gaussians and their gradients into new, high-contribution ...
- **p. 5 / 4. Experiments - extractive body cue:** We set the learning rate to 1e-4 and train the networks for 3 days on a single Nvidia RTX A6000.
- **p. 4 / 3.3. Iterative Gaussian Optimization - extractive body cue:** Concretely, we render the training images and compute the gradients of the rendering loss Eq.
- **p. 6 / Method - extractive body cue:** Both our method without post-training ("w/o opt") and with additional SGD iterations ("w/ opt") obtain better geometry while achieving orders of magnitude faster runtime. # ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Top, densifier, network, predicts, pool, additional, voxel, features, encoder-decoder, architecture, current, Gaussians, gradients, input, contrast, SGNN, produces, sparse, outputs, employ.
- **Relevant PDF headings:** 3. Method (p. 2); Method (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We evaluate our method on 20 unseen test scenes and report averaged metrics. | p. 5 (4. Experiments), p. 5 (4. Experiments) |
| Semantic / temporal fusion | Fig. 4. In general, our proposed QuickSplat achieves better performance: it reconstructs scenes with cleaner structures and flat surfaces that matches the ... | p. 6 (Figure/Table caption), p. 6 (Figure/Table caption) |
| Robot query / planning handoff | PGSR renders unbiased depth maps from flattened 3D Gaussians and introduces both single-view and multi-view regularization losses to improve geometric reconstruction. | p. 5 (4. Experiments), p. 6 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6. Visualization of ablations. (a) Without our initializer and densification priors during optimization, surface reconstruc- tion of untextured regions such as walls is challenging ...
- **p. 5 / 4. Experiments - extractive body cue:** After running our iterative optimization for t=5 timesteps, we optionally refine the Gaussians for another 2000 steps of gradient descent (without adaptive density control).
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Quantitative comparison against baselines. We compare the quality and optimization runtime of our reconstructed surfaces against baseline methods, and show averaged results on ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Ablation study. We ablate the impact of our learned priors for initialization, densification, and optimization updates. Only using our optimizer network does not ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Qualitative comparison against baselines. We show top-down views of reconstructed mesh geometries (with and without vertex colors) in comparison to the ground-truth meshes ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Initializer output ablation study. We evaluate the im- pact of predicting different Gaussian attributes from the SfM point cloud with our initializer network. ...
- **p. 8 / 4.3. Limitations - extractive body cue:** Second, we assume static environments and therefore cannot reconstruct dynamic scenes (e.g., people walking inside of a room).

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3.3. Iterative Gaussian Optimization), p. 3 (3.2. Initialization Prior), p. 4 (3.3. Iterative Gaussian Optimization), p. 3 (3.2. Initialization Prior), p. 5 (3.3. Iterative Gaussian Optimization), p. 5 (3.3. Iterative Gaussian Optimization), objective p. 3 (3. Method), p. 5 (3.3. Iterative Gaussian Optimization), p. 4 (3.3. Iterative Gaussian Optimization), p. 3 (3.1. Surface Representation), p. 4 (3.2. Initialization Prior), p. 5 (3.3. Iterative Gaussian Optimization), temporal p. 4 (3.3. Iterative Gaussian Optimization), p. 5 (3.3. Iterative Gaussian Optimization), p. 5 (3.3. Iterative Gaussian Optimization), p. 2 (2.3. Meta learning), p. 3 (3.2. Initialization Prior), p. 3 (3. Method).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
