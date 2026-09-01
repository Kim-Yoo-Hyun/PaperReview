# Method - SSCNet: Semantic Scene Completion from a Single Depth Image

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1611.08974; PDF retrieval source: https://arxiv.org/pdf/1611.08974. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3.2. Network architecture), p. 4 (3.2. Network architecture), p. 5 (3.2. Network architecture), p. 5 (3.2. Network architecture)): Then, we use a dilation-based 3D context module to capture higher-level inter-object contextual information.

## Method Body Digest

- **p. 4 / 3.2. Network architecture - extractive PDF cue:** Then, we use a dilation-based 3D context module to capture higher-level inter-object contextual information.
- **p. 4 / 3.2. Network architecture - extractive PDF cue:** Taking a high-resolution 3D volume as input, the network first uses several 3D convolution layers to learn a local geometry representation.
- **p. 5 / 3.2. Network architecture - extractive PDF cue:** We implement our network architecture in Caffe [10].
- **p. 5 / 3.2. Network architecture - extractive PDF cue:** We collected a large-scale synthetic 3D scene dataset to train our network.
- **p. 4 / 3.2. Network architecture - extractive PDF cue:** The loss function of the network is the sum of voxel-wise softmax loss L(p, y) = P i,j,k wijkLsm(pijk, yijk), where Lsm is softmax loss, ...
- **p. 5 / 3.2. Network architecture - extractive PDF cue:** To obtain more stable gradient estimates, we accumulate gradients over four iterations and update the weights once afterwards.
- **p. 4 / 3.2. Network architecture - extractive PDF cue:** Several shortcut connections are added for better gradient propagation.
- **p. 1 / 1. Introduction - extractive PDF cue:** (a) Input single-view depth map (b) Visible surface from the depth map; color is for visualization only.

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** To provide the training data for our network, we introduce SUNCG, a manually created large-scale dataset of synthetic 3D scenes with dense occupancy and semantic ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Similarly, for a robot, the ability to infer complete 3D shape from partial observations is necessary for low-level tasks such as grasping and obstacle avoidance ...
- **p. 2 / 1. Introduction - extractive PDF cue:** In support of that goal, we design a dilation-based 3D context module that enables efficient context learning with large receptive fields.

## Source Evidence Cues

- **p. 4 / 3.2. Network architecture - extractive PDF cue:** Then, we use a dilation-based 3D context module to capture higher-level inter-object contextual information.
- **p. 4 / 3.2. Network architecture - extractive PDF cue:** Taking a high-resolution 3D volume as input, the network first uses several 3D convolution layers to learn a local geometry representation.
- **p. 5 / 3.2. Network architecture - extractive PDF cue:** We implement our network architecture in Caffe [10].
- **p. 5 / 3.2. Network architecture - extractive PDF cue:** We collected a large-scale synthetic 3D scene dataset to train our network.
- **Detected method headings:** 3.2. Network architecture (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Then, we use a dilation-based 3D context module to capture higher-level inter-object contextual information. | p. 4 (3.2. Network architecture), p. 4 (3.2. Network architecture) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Taking a high-resolution 3D volume as input, the network first uses several 3D convolution layers to learn a local geometry representation. | p. 4 (3.2. Network architecture), p. 5 (3.2. Network architecture) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | We implement our network architecture in Caffe [10]. | p. 5 (3.2. Network architecture), p. 5 (3.2. Network architecture) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.2. Network architecture - extractive PDF cue:** The loss function of the network is the sum of voxel-wise softmax loss L(p, y) = P i,j,k wijkLsm(pijk, yijk), where Lsm is softmax loss, ...
- **p. 5 / 3.2. Network architecture - extractive PDF cue:** To obtain more stable gradient estimates, we accumulate gradients over four iterations and update the weights once afterwards.
- **p. 4 / 3.2. Network architecture - extractive PDF cue:** Several shortcut connections are added for better gradient propagation.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (3.2. Network architecture), p. 4 (3.2. Network architecture), p. 4 (3.2. Network architecture).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Input, single-view, depth, Visible, surface, color, visualization, only, motivation, goal, have, model, predicts, volumetric | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Input, single-view, depth, Visible, surface, color, visualization, only, motivation, goal | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | provide, training, data, network, introduce, SUNCG, manually, created, large-scale, dataset | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | loss, function, network, voxel-wise, softmax, wijkLsm, pijk, yijk, where, Lsm | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1. Introduction - extractive PDF cue:** (a) Input single-view depth map (b) Visible surface from the depth map; color is for visualization only.
- **p. 1 / 1. Introduction - extractive PDF cue:** With this motivation, our goal is to have a model that predicts both volumetric occupancy (i.e., scene completion) and object category (i.e., scene labeling) from ...
- **p. 5 / 4.2. Synthetic depth map generation - extractive PDF cue:** We then choose camera poses based on the distribution of the NYU-Depth v2 dataset.1 Then, we render the depth map using the intrinsics and resolution ...
- **p. 4 / 3.2. Network architecture - extractive PDF cue:** In implementing this architecture, we made the following design decisions: Input volume generation.
- **p. 4 / 3.2. Network architecture - extractive PDF cue:** We use convolution layers with stride and pooling layers to reduce the resolution to one fourth of original input.
- **p. 5 / 4. Synthesizing training data - extractive PDF cue:** Existing RGB-D datasets with surface reconstructions are subject to occlusions or partial observations, and cannot provide the volumetric occupancy and semantic labels for the entire ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Most critically, this prediction extends beyond the projected surface implied by the depth map, thus providing occupancy information for the entire scene.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Both these algorithms take an RGB-D frame as input and produce object labels in the 3D scene. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Moreover, since our method does not require the model fitting step it is much faster at 7s compared to 127s per image ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | Secondly, due to the GPU memory constraints, our network output resolution is lower than that of input volume. | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | Moreover, since our method does not require the model fitting step it is much faster at 7s compared to 127s per image ... | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.2. Network architecture - extractive PDF cue:** We collected a large-scale synthetic 3D scene dataset to train our network.
- **p. 8 / 5.1. Experimental results - extractive PDF cue:** Secondly, due to the GPU memory constraints, our network output resolution is lower than that of input volume.
- **p. 5 / 3.2. Network architecture - extractive PDF cue:** During training, each mini-batch contains one 3D view volume, requiring 11 GB of GPU memory.
- **p. 5 / 3.2. Network architecture - extractive PDF cue:** Pre-training SSCNet on the SUNCG training set takes around a week on a Tesla K40 GPU, and fine-tuning on the NYU dataset takes 30 hours.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Then, dilation-based, context, module, capture, higher-level, inter-object, contextual, information, Taking, high-resolution, volume, input, network, first, uses, several, convolution, layers, learn.
- **Relevant PDF headings:** 3.2. Network architecture (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | The SUNCG test set consists of 500 depth images rendered from 184 scenes that are not in the training set. | p. 6 (5. Evaluation), p. 6 (5. Evaluation) |
| Semantic / temporal fusion | Figure 4. Comparison of receptive fields and voxel sizes between SSCNet and prior work. (a) Object centric networks such as [34] and ... | p. 4 (Figure/Table caption), p. 6 (5. Evaluation) |
| Robot query / planning handoff | Increasing the receptive field gives the network a opportunity to capture richer contextual information and significantly improve the network performance from 38.0% ... | p. 8 (5.1. Experimental results), p. 8 (5.1. Experimental results) |

## Failure and Ablation Link

- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 8. What 3D context does the network learn? The first fig- ure shows the input depth map (a desk) and the following figures show ...
- **p. 8 / 5.1. Experimental results - extractive PDF cue:** To investigate the effect of using synthetic training data, we compared models trained only with NYU and models pre-trained on SUNCG and then fine-tuned on ...
- **p. 6 / 5.1. Experimental results - extractive PDF cue:** Previous work has shown scene completion is possible without 6
- **p. 6 / 5. Evaluation - extractive PDF cue:** In this section, we evaluate our proposed methods with a comparison to alternative approaches and an ablation study to better understand the proposed model.
- **p. 7 / 5.1. Experimental results - extractive PDF cue:** [37] which both predict binary voxel occupancy based on a single depth map without semantic understanding of the scene.
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Semantic scene completion. (a) Input single-view depth map (b) Visible surface from the depth map; color is for visualiza- tion only. (c) Semantic ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 5. Different encodings for surface (a). The projective TSDF (b) is computed with respect to the camera and is therefore view-dependent. The accurate TSDF ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3.2. Network architecture), p. 4 (3.2. Network architecture), p. 5 (3.2. Network architecture), p. 5 (3.2. Network architecture), objective p. 4 (3.2. Network architecture), p. 5 (3.2. Network architecture), p. 4 (3.2. Network architecture), temporal p. 6 (5.1. Experimental results), p. 6 (5.1. Experimental results), p. 7 (5.1. Experimental results), p. 7 (5.1. Experimental results), p. 8 (5.1. Experimental results), p. 1 (Abstract).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
