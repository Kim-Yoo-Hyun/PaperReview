# Method - In-Place Scene Labelling and Understanding with Implicit Scene Representation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2103.15875; PDF retrieval source: https://arxiv.org/pdf/2103.15875. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (3.4. Implementation), p. 3 (3.4. Implementation), p. 4 (3.4. Implementation)): Specifically, we use hierarchical volume sampling to jointly optimise coarse and fine networks, where the former provides importance sampling bias so that the latter can distribute more samples to positions ...

## Method Body Digest

- **p. 3 / 3.4. Implementation - extractive body cue:** Specifically, we use hierarchical volume sampling to jointly optimise coarse and fine networks, where the former provides importance sampling bias so that the latter can ...
- **p. 3 / 3.4. Implementation - extractive body cue:** A scene-specific semantic representation is obtained by training the network from scratch for each scene individually.
- **p. 4 / 3.4. Implementation - extractive body cue:** We train the neural network using the Adam optimiser [7] with a learning rate of 5e-4 for 200,000 iterations.
- **p. 3 / 3.3. Network Training - extractive body cue:** Ls is chosen as a multi-class cross-entropy loss to encourage the rendered semantic labels to be consistent with the provided labels, whether these are ground-truth, ...
- **p. 3 / 3.3. Network Training - extractive body cue:** We train the whole network from scratch under photometric loss Lp and semantic loss Ls: Lp = X r∈R 
- **p. 2 / 3.1. Preliminaries - extractive body cue:** Given multiple images of a static scene with known camera intrinsics and extrinsics, NeRF [16] uses MLPs to implicitly represent the continuous 3D scene density ...
- **p. 2 / 1. Introduction - extractive body cue:** Our system takes as input a set of RGB images with associated known camera poses.
- **p. 1 / 1. Introduction - extractive body cue:** Enabling intelligent agents, such as indoor mobile robots, to plan context-sensitive actions in their environment requires both a geometric and semantic understanding of the scene.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** In addition, multi-view consistency is inherent to the training process and enables the network to produce accurate semantic labels of the scene, including for views ...
- **p. 1 / 1. Introduction - extractive body cue:** In this paper, we show how to design a scene-specific network for joint geometric and semantic prediction and train it on images from a single ...
- **p. 1 / 1. Introduction - extractive body cue:** Unlike scene geometry, however, semantic classes are a human-defined concept and it is not possible to semantically label a novel scene in a purely self-supervised ...

## Source Evidence Cues

- **p. 3 / 3.4. Implementation - extractive body cue:** Specifically, we use hierarchical volume sampling to jointly optimise coarse and fine networks, where the former provides importance sampling bias so that the latter can ...
- **p. 3 / 3.4. Implementation - extractive body cue:** A scene-specific semantic representation is obtained by training the network from scratch for each scene individually.
- **p. 4 / 3.4. Implementation - extractive body cue:** We train the neural network using the Adam optimiser [7] with a learning rate of 5e-4 for 200,000 iterations.
- **Detected method headings:** 3. Method (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Specifically, we use hierarchical volume sampling to jointly optimise coarse and fine networks, where the former provides importance sampling bias so that ... | p. 3 (3.4. Implementation), p. 3 (3.4. Implementation) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | A scene-specific semantic representation is obtained by training the network from scratch for each scene individually. | p. 3 (3.4. Implementation), p. 4 (3.4. Implementation) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | We train the neural network using the Adam optimiser [7] with a learning rate of 5e-4 for 200,000 iterations. | p. 4 (3.4. Implementation) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3.3. Network Training - extractive body cue:** Ls is chosen as a multi-class cross-entropy loss to encourage the rendered semantic labels to be consistent with the provided labels, whether these are ground-truth, ...
- **p. 3 / 3.3. Network Training - extractive body cue:** We train the whole network from scratch under photometric loss Lp and semantic loss Ls: Lp = X r∈R 
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 3 (3.3. Network Training), p. 3 (3.1. Preliminaries).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Given, multiple, images, static, scene, known, camera, intrinsics, extrinsics, NeRF, uses, MLPs, implicitly, represent | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Given, multiple, images, static, scene, known, camera, intrinsics, extrinsics, NeRF | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | addition, multi-view, consistency, inherent, training, process, enables, network, produce, accurate | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | chosen, multi-class, cross-entropy, loss, encourage, rendered, semantic, labels, consistent, provided | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 3.1. Preliminaries - extractive body cue:** Given multiple images of a static scene with known camera intrinsics and extrinsics, NeRF [16] uses MLPs to implicitly represent the continuous 3D scene density ...
- **p. 2 / 1. Introduction - extractive body cue:** Our system takes as input a set of RGB images with associated known camera poses.
- **p. 3 / 3.3. Network Training - extractive body cue:** Ls is chosen as a multi-class cross-entropy loss to encourage the rendered semantic labels to be consistent with the provided labels, whether these are ground-truth, ...
- **p. 1 / 1. Introduction - extractive body cue:** Enabling intelligent agents, such as indoor mobile robots, to plan context-sensitive actions in their environment requires both a geometric and semantic understanding of the scene.
- **p. 1 / 1. Introduction - extractive body cue:** NeRF [16]) that represent the shape and radiance of a single scene with a neural network trained from scratch using only images and associated camera ...
- **p. 3 / 3.4. Implementation - extractive body cue:** Training images are resized to 320x240 for all the experiments.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | The sequences in each scene are evenly sampled so that the total amount of training data is roughly 300 frames. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | We sample every 5th frame from the sequence to compose the training set and also sample intermediate frames to make the test ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | We implement our model in PyTorch [20] and train it on a single RTX2080-Ti GPU with 11GB memory. | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | The sequences in each scene are evenly sampled so that the total amount of training data is roughly 300 frames. | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 3.4. Implementation - extractive body cue:** A scene-specific semantic representation is obtained by training the network from scratch for each scene individually.
- **p. 4 / 3.4. Implementation - extractive body cue:** We train the neural network using the Adam optimiser [7] with a learning rate of 5e-4 for 200,000 iterations.
- **p. 4 / 3.4. Implementation - extractive body cue:** We train the neural network using the Adam optimiser [7] with a learning rate of 5e-4 for 200,000 iterations.
- **p. 3 / 3.4. Implementation - extractive body cue:** We implement our model in PyTorch [20] and train it on a single RTX2080-Ti GPU with 11GB memory.
- **p. 6 / 4.4. Semantic Fusion - extractive body cue:** Both tables are computed against clean training labels. to randomly perturb each instance: (1) Sort: Select label maps with the least occupied area ratio.
- **p. 8 / 4.4. Semantic Fusion - extractive body cue:** We train Semantic-NeRF using posed colour images together with CNN-predicted labels for 200,000 steps and then re-render the fused semantic labels back to the training ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Specifically, hierarchical, volume, sampling, jointly, optimise, coarse, fine, networks, where, former, provides, importance, bias, latter, distribute, more, samples, positions, likely.
- **Relevant PDF headings:** 3. Method (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | ScanNet ScanNet [3] is a large-scale real-world indoor RGB-D video dataset of 2.5M views in 1513 scenes with rich annotations including semantic ... | p. 4 (4.1. Indoor Scene Datasets and Data Preparation), p. 4 (4.1. Indoor Scene Datasets and Data Preparation) |
| Semantic / temporal fusion | Our approach relying on consistency of scene representations outperforms baselines aided with depth maps. posed images. | p. 8 (4.4. Semantic Fusion), p. 5 (4.4. Semantic Fusion) |
| Robot query / planning handoff | Our method achieves the highest improvement across all metrics, showing the effectiveness of our joint representation in label fusion. | p. 8 (4.4. Semantic Fusion), p. 4 (4.2. Semantic Neural Radiance Fields) |

## Failure and Ablation Link

- **p. 4 / 4.2. Semantic Neural Radiance Fields - extractive body cue:** We check the influence of semantics on appearance and geometry by quantitatively computing the quality of rendered RGB images and depth maps on Replica scenes ...
- **p. 6 / 4.4. Semantic Fusion - extractive body cue:** We test two different strategies to generate low-resolution training labels, with and without interpolation as shown in Figure 7.
- **p. 3 / 3.4. Implementation - extractive body cue:** In addition, since we have no depth information, we set the bounds of ray sampling to 0.1m and 10m respectively across experiments without careful tuning ...
- **p. 8 / 4.4. Semantic Fusion - extractive body cue:** We repeat this fine-tuning process and train one individual DeepLab CNN model for each test scene.
- **p. 8 / 4.4. Semantic Fusion - extractive body cue:** To generate decent monocular CNN predictions and avoid over-fitting, we train DeepLab on SUN-RGBD [26], and then fine-tune it using data from all Replica scenes ...
- **p. 4 / 3.4. Implementation - extractive body cue:** batch size of rays is set to 1024 due to memory limitations.
- **p. 4 / 4.4. Semantic Fusion - extractive body cue:** Given multiple noisy or partial semantic labels, the network can fuse them into a joint implicit 3D space so that we can extract a denoised ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (3.4. Implementation), p. 3 (3.4. Implementation), p. 4 (3.4. Implementation), objective p. 3 (3.3. Network Training), p. 3 (3.3. Network Training), temporal p. 4 (4.1. Indoor Scene Datasets and Data Preparation), p. 4 (4.1. Indoor Scene Datasets and Data Preparation), p. 5 (4.4. Semantic Fusion), p. 5 (4.4. Semantic Fusion), p. 8 (4.4. Semantic Fusion), p. 3 (3.4. Implementation).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
