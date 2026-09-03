# Method - Lift, Splat, Shoot: Encoding Images from Arbitrary Camera Rigs by Implicitly Unprojecting to 3D

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2008.05711; PDF retrieval source: https://arxiv.org/pdf/2008.05711. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (3 Method), p. 7 (3 Method), p. 8 (3 Method), p. 6 (3 Method), p. 8 (3 Method), p. 5 (3 Method)): 3.1 Lift: Latent Depth Distribution The first stage of our model operates on each image in the camera rig in isolation.

## Method Body Digest

- **p. 5 / 3 Method - extractive body cue:** 3.1 Lift: Latent Depth Distribution The first stage of our model operates on each image in the camera rig in isolation.
- **p. 7 / 3 Method - extractive body cue:** For labels, given a ground-truth trajectory, we compute the nearest neighbor in L2 distance to the template trajectories T then train with the cross entropy ...
- **p. 8 / 3 Method - extractive body cue:** The "cumulative sum trick" is the observation that sum pooling can be performed by sorting all points according to bin id, performing a cumulative sum ...
- **p. 6 / 3 Method - extractive body cue:** 4: Lift-Splat-Shoot Outline Our model takes as input n images (left) and their corresponding extrinsic and intrinsic parameters.
- **p. 8 / 3 Method - extractive body cue:** For our bird's-eye-view network, we use a combination of ResNet blocks similar to PointPillars [18].
- **p. 5 / 3 Method - extractive body cue:** The feature cd ∈RC associated to point pd is then defined as the context vector for pixel p scaled by αd: cd = αdc.
- **p. 6 / 3 Method - extractive body cue:** At test time, planning using the inferred cost map can be achieved by "shooting" different trajectories, scoring their cost, then acting according to lowest cost ...
- **p. 7 / 3 Method - extractive body cue:** This definition of p(τi/o) enables us to learn an interpretable spatial cost function without defining a hard-margin loss as in NMP [41].

## Design Rationale

- **p. 4 / 3 Method - extractive body cue:** In this section, we present our approach for learning bird's-eye-view representations of scenes from image data captured by an arbitrary camera rig.
- **p. 2 / 1 Introduction - extractive body cue:** We propose a model named "Lift-Splat" that preserves the 3 symmetries identified above by design while also being end-to-end differentiable.
- **p. 2 / 1 Introduction - extractive body cue:** In Section 3.3, we propose a method for "shooting" proposal trajectories into this reference plane for interpretable end-to-end motion planning.

## Source Evidence Cues

- **p. 5 / 3 Method - extractive body cue:** 3.1 Lift: Latent Depth Distribution The first stage of our model operates on each image in the camera rig in isolation.
- **p. 7 / 3 Method - extractive body cue:** For labels, given a ground-truth trajectory, we compute the nearest neighbor in L2 distance to the template trajectories T then train with the cross entropy ...
- **p. 8 / 3 Method - extractive body cue:** The "cumulative sum trick" is the observation that sum pooling can be performed by sorting all points according to bin id, performing a cumulative sum ...
- **p. 6 / 3 Method - extractive body cue:** 4: Lift-Splat-Shoot Outline Our model takes as input n images (left) and their corresponding extrinsic and intrinsic parameters.
- **p. 8 / 3 Method - extractive body cue:** For our bird's-eye-view network, we use a combination of ResNet blocks similar to PointPillars [18].
- **p. 5 / 3 Method - extractive body cue:** The feature cd ∈RC associated to point pd is then defined as the context vector for pixel p scaled by αd: cd = αdc.
- **p. 6 / 3 Method - extractive body cue:** At test time, planning using the inferred cost map can be achieved by "shooting" different trajectories, scoring their cost, then acting according to lowest cost ...
- **Detected method headings:** 3 Method (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | 3.1 Lift: Latent Depth Distribution The first stage of our model operates on each image in the camera rig in isolation. | p. 5 (3 Method), p. 7 (3 Method) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | For labels, given a ground-truth trajectory, we compute the nearest neighbor in L2 distance to the template trajectories T then train with ... | p. 7 (3 Method), p. 8 (3 Method) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | The "cumulative sum trick" is the observation that sum pooling can be performed by sorting all points according to bin id, performing ... | p. 8 (3 Method), p. 6 (3 Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 7 / 3 Method - extractive body cue:** This definition of p(τi/o) enables us to learn an interpretable spatial cost function without defining a hard-margin loss as in NMP [41].
- **p. 7 / 3 Method - extractive body cue:** (2) where co(x, y) is defined by indexing into the cost map predicted given observations o at location x, y and can therefore be trained ...
- **p. 6 / 3 Method - extractive body cue:** This operation has an analytic gradient that can be calculated efficiently to speed up autograd as explained in subsection 4.2.
- **p. 6 / 3 Method - extractive body cue:** 3.3 Shoot: Motion Planning Key aspect of our Lift-Splat model is that it enables end-to-end cost map learning for motion planning from camera-only input.
- **p. 8 / 3 Method - extractive body cue:** Instead of relying on autograd to backprop through all three steps, the analytic gradient for the module as a whole can be derived, speeding up ...
- **p. 5 / 3 Method - extractive body cue:** To take advantage of discrete convolutions, we choose to discretize space.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 6 (3 Method), p. 7 (3 Method), p. 7 (3 Method), p. 8 (3 Method), p. 8 (3 Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Computer, vision, algorithms, generally, take, input, image, output, either, prediction, coordinate-frame, agnostic, classification, same | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Computer, vision, algorithms, generally, take, input, image, output, either, prediction | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | section, present, learning, bird, s-eye-view, representations, scenes, image, data, captured | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | definition, enables, learn, interpretable, spatial, cost, function, without, defining, hard-margin | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 Introduction - extractive body cue:** Computer vision algorithms generally take as input an image and output either a prediction that is coordinate-frame agnostic - such as in classification [19,30,16,17] - ...
- **p. 2 / 1 Introduction - extractive body cue:** An equivalent way to state this property is that the definition of the ego-frame can be rotated/translated and the output will rotate/translate with it.
- **p. 5 / 3 Method - extractive body cue:** 3.2 Splat: Pillar Pooling We follow the pointpillars [18] architecture to convert the large point cloud output by the "lift" step. "Pillars" are voxels with ...
- **p. 6 / 3 Method - extractive body cue:** 4: Lift-Splat-Shoot Outline Our model takes as input n images (left) and their corresponding extrinsic and intrinsic parameters.
- **p. 6 / 3 Method - extractive body cue:** 3.3 Shoot: Motion Planning Key aspect of our Lift-Splat model is that it enables end-to-end cost map learning for motion planning from camera-only input.
- **p. 7 / 3 Method - extractive body cue:** (2) where co(x, y) is defined by indexing into the cost map predicted given observations o at location x, y and can therefore be trained ...
- **p. 8 / 3 Method - extractive body cue:** First, there is the size of the input images H × W.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | In order to meet and possibly surpass the performance of similar networks that exclusively use ground truth depth data from pointclouds, future ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Lift, Splat, Shoot 5 rasterized representation of the scene in the BEV coordinate frame y ∈RC×X×Y . | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | With these hyperparameters and architectural design choices, the forward pass of the model runs at 35 hz on a Titan V GPU. | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / 3 Method - extractive body cue:** For labels, given a ground-truth trajectory, we compute the nearest neighbor in L2 distance to the template trajectories T then train with the cross entropy ...
- **p. 9 / 6 DOF localization and rasterize - extractive body cue:** In all cases, we train for 300k steps using Adam [14] with learning rate 1e -3 and weight decay 1e -7.
- **p. 7 / 3 Method - extractive body cue:** During training, the cost of each template trajectory is computed and interpreted as a 1K-dimensional Boltzman distribution over the templates.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Lift, Latent, Depth, Distribution, first, stage, model, operates, image, camera, isolation, labels, given, ground-truth, trajectory, compute, nearest, neighbor, distance, template.
- **Relevant PDF headings:** 3 Method (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | 5 Experiments and Results We use the nuScenes [2] and Lyft Level 5 [13] datasets to evaluate our approach. nuScenes is a ... | p. 8 (3 Method), p. 10 (6 DOF localization and rasterize) |
| Semantic / temporal fusion | We outperform these baselines on all tasks, as shown in Tables 1 and 2. | p. 9 (6 DOF localization and rasterize), p. 10 (6 DOF localization and rasterize) |
| Robot query / planning handoff | Table 2: Map IOU in BEV frame 5.2 Segmentation We demonstrate that our Lift-Splat model is able to learn semantic 3D repre- ... | p. 10 (Figure/Table caption), p. 4 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 12 / 6 DOF localization and rasterize - extractive body cue:** 8: For a single time stamp, we remove each of the cameras and visualize how the loss the cameras effects the prediction of the network.
- **p. 7 / 3 Method - extractive body cue:** This definition of p(τi/o) enables us to learn an interpretable spatial cost function without defining a hard-margin loss as in NMP [41].
- **p. 10 / 6 DOF localization and rasterize - extractive body cue:** We reason that sensor dropout forces the model to learn the correlation between images on different cameras, similar to other variants of dropout [33] [5].
- **p. 10 / 6 DOF localization and rasterize - extractive body cue:** For low amounts of noise at test-time, models that are trained without any noise in the extrinsics perform the best because the BEV CNN can ...
- **p. 11 / 6 DOF localization and rasterize - extractive body cue:** In Table 3, we show that the performance of our model for car segmentation improves when additional cameras are available at test time without any ...
- **p. 12 / 6 DOF localization and rasterize - extractive body cue:** When the front camera is removed (top middle), the network extrapolates the lane and drivable area in front of the ego and extrapolates the body ...
- **p. 14 / Figure/Table caption - extractive body cue:** Table 6: Since planning is framed as classification among a set of 1K template trajectories, we measure top-5, top-10, and top-20 accuracy. We find that ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (3 Method), p. 7 (3 Method), p. 8 (3 Method), p. 6 (3 Method), p. 8 (3 Method), p. 5 (3 Method), objective p. 7 (3 Method), p. 7 (3 Method), p. 6 (3 Method), p. 6 (3 Method), p. 8 (3 Method), p. 5 (3 Method), temporal p. 14 (6 Conclusion), p. 5 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 6 (3 Method), p. 7 (3 Method).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
