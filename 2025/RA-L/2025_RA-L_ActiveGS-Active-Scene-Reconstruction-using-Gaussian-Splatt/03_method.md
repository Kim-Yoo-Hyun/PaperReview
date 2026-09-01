# Method - ActiveGS: Active Scene Reconstruction using Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2412.17769; PDF retrieval source: https://arxiv.org/pdf/2412.17769. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (III. OUR APPROACH), p. 2 (A CTIVE exploration and reconstruction of unknown), p. 3 (III. OUR APPROACH), p. 5 (III. OUR APPROACH), p. 3 (III. OUR APPROACH), p. 4 (III. OUR APPROACH)): The normal loss Ln = Dcos(N, eN) + TV (N) consists of the cosine distance Dcos between the rendered normal map and the normal map eN derived from the rendered ...

## Method Body Digest

- **p. 4 / III. OUR APPROACH - extractive PDF cue:** The normal loss Ln = Dcos(N, eN) + TV (N) consists of the cosine distance Dcos between the rendered normal map and the normal map ...
- **p. 2 / A CTIVE exploration and reconstruction of unknown - extractive PDF cue:** To tackle the first challenge, we propose a simple yet effective confidence modelling technique for Gaussian primitives based on viewpoint distribution, enabling view planning for ...
- **p. 3 / III. OUR APPROACH - extractive PDF cue:** To actively guide view planning to reconstruct the scene in a targeted manner, we propose using our confidence modelling technique in the GS map and ...
- **p. 5 / III. OUR APPROACH - extractive PDF cue:** We use the A∗algorithm [8] to find the shortest traversable path from the current viewpoint position to all candidate viewpoint positions.
- **p. 3 / III. OUR APPROACH - extractive PDF cue:** Our GS map is based on Gaussian surfel [4], a state-ofthe-art 2D GS representation.
- **p. 4 / III. OUR APPROACH - extractive PDF cue:** Note that the training process involves only a subset of the Gaussian primitive parameters (xi, qi, si, ci, oi), while the modelling of non-trainable ki ...
- **p. 1 / A CTIVE exploration and reconstruction of unknown - extractive PDF cue:** Achieving this requires two key components: high-fidelity map representations for modelling fine-grained geometric and textural details of the scenes and adaptive view planning strategies for ...
- **p. 2 / A CTIVE exploration and reconstruction of unknown - extractive PDF cue:** While these approaches demonstrate promising results, the rather costly volumetric rendering procedure during online incremental mapping poses limitations for NeRF-based active scene reconstruction.

## Design Rationale

- **p. 3 / III. OUR APPROACH - extractive PDF cue:** We introduce ActiveGS, a novel framework for active scene reconstruction using GS for autonomous robotic tasks.
- **p. 3 / III. OUR APPROACH - extractive PDF cue:** An overview of our framework is shown in Fig.
- **p. 4 / III. OUR APPROACH - extractive PDF cue:** A candidate viewpoint pc i ∈R5 is defined by its 3D position, yaw, and pitch angles in our framework.

## Source Evidence Cues

- **p. 4 / III. OUR APPROACH - extractive PDF cue:** The normal loss Ln = Dcos(N, eN) + TV (N) consists of the cosine distance Dcos between the rendered normal map and the normal map ...
- **p. 2 / A CTIVE exploration and reconstruction of unknown - extractive PDF cue:** To tackle the first challenge, we propose a simple yet effective confidence modelling technique for Gaussian primitives based on viewpoint distribution, enabling view planning for ...
- **p. 3 / III. OUR APPROACH - extractive PDF cue:** To actively guide view planning to reconstruct the scene in a targeted manner, we propose using our confidence modelling technique in the GS map and ...
- **p. 5 / III. OUR APPROACH - extractive PDF cue:** We use the A∗algorithm [8] to find the shortest traversable path from the current viewpoint position to all candidate viewpoint positions.
- **p. 3 / III. OUR APPROACH - extractive PDF cue:** Our GS map is based on Gaussian surfel [4], a state-ofthe-art 2D GS representation.
- **p. 4 / III. OUR APPROACH - extractive PDF cue:** Note that the training process involves only a subset of the Gaussian primitive parameters (xi, qi, si, ci, oi), while the modelling of non-trainable ki ...
- **p. 1 / A CTIVE exploration and reconstruction of unknown - extractive PDF cue:** Achieving this requires two key components: high-fidelity map representations for modelling fine-grained geometric and textural details of the scenes and adaptive view planning strategies for ...
- **Detected method headings:** III. OUR APPROACH (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | The normal loss Ln = Dcos(N, eN) + TV (N) consists of the cosine distance Dcos between the rendered normal map and ... | p. 4 (III. OUR APPROACH), p. 2 (A CTIVE exploration and reconstruction of unknown) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | To tackle the first challenge, we propose a simple yet effective confidence modelling technique for Gaussian primitives based on viewpoint distribution, enabling ... | p. 2 (A CTIVE exploration and reconstruction of unknown), p. 3 (III. OUR APPROACH) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | To actively guide view planning to reconstruct the scene in a targeted manner, we propose using our confidence modelling technique in the ... | p. 3 (III. OUR APPROACH), p. 5 (III. OUR APPROACH) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / A CTIVE exploration and reconstruction of unknown - extractive PDF cue:** While these approaches demonstrate promising results, the rather costly volumetric rendering procedure during online incremental mapping poses limitations for NeRF-based active scene reconstruction.
- **p. 3 / III. OUR APPROACH - extractive PDF cue:** Without loss of generality, the rendering function for a pixel u on the view is formulated as: O(u) = n X i=1 wi , M(u) ...
- **p. 4 / III. OUR APPROACH - extractive PDF cue:** The loss for a frame {ˆI , ˆD} in the training batch is formulated as the weighted sum of individual loss terms: L = wcLc ...
- **p. 4 / III. OUR APPROACH - extractive PDF cue:** The normal loss Ln = Dcos(N, eN) + TV (N) consists of the cosine distance Dcos between the rendered normal map and the normal map ...
- **p. 5 / III. OUR APPROACH - extractive PDF cue:** Uview(pc i) PNtotal i=1 Uview(pc i) -δ Upath(pc i) PNtotal i=1 Upath(pc i) ! , (10) where Ntotal = Nrandom + NROI; Upath is the ...
- **p. 5 / III. OUR APPROACH - extractive PDF cue:** Taking travel distance into account, we select the next best viewpoint p⋆by: p⋆= arg max pc i
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 3 (III. OUR APPROACH), p. 4 (III. OUR APPROACH), p. 4 (III. OUR APPROACH), p. 2 (A CTIVE exploration and reconstruction of unknown), p. 3 (III. OUR APPROACH), p. 5 (III. OUR APPROACH).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Given, posed, RGB-D, measurements, input, update, coarse, voxel, model, spatial, occupancy, incrementally, train, high-fidelity | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Given, posed, RGB-D, measurements, input, update, coarse, voxel, model, spatial | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | introduce, ActiveGS, novel, framework, active, scene, reconstruction, autonomous, robotic, tasks | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | While, approaches, demonstrate, promising, rather, costly, volumetric, rendering, procedure, during | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / III. OUR APPROACH - extractive PDF cue:** Given posed RGB-D measurements as input, we update a coarse voxel map to model the spatial occupancy and incrementally train a GS map for high-fidelity ...
- **p. 3 / III. OUR APPROACH - extractive PDF cue:** Our GS map is based on Gaussian surfel [4], a state-ofthe-art 2D GS representation.
- **p. 4 / III. OUR APPROACH - extractive PDF cue:** ACCEPTED MARCH, 2025 areas into 3D space, with initial parameters defined by the corresponding point cloud position, pixel colour, and normal estimated by applying central ...
- **p. 4 / III. OUR APPROACH - extractive PDF cue:** The normal loss Ln = Dcos(N, eN) + TV (N) consists of the cosine distance Dcos between the rendered normal map and the normal map ...
- **p. 1 / Abstract - extractive PDF cue:** By actively collecting scene information in under-reconstructed and unexplored areas for map updates, our approach achieves superior Gaussian splatting reconstruction results compared to state-of-the-art approaches.
- **p. 2 / A CTIVE exploration and reconstruction of unknown - extractive PDF cue:** We make the following three claims: (i) our ActiveGS framework achieves superior reconstruction performance compared to state-of-the-art NeRF-based approach and GS-based baselines; (ii) our explicit ...
- **p. 1 / A CTIVE exploration and reconstruction of unknown - extractive PDF cue:** Existing active scene reconstruction frameworks mainly rely on conventional map representations such as voxel grids, meshes, or point clouds [2, 17, 30, 31, 32, 39, ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | The whole framework consumes 4 -5 GB GPU RAM during an online mission, with approximately 10% allocated to the voxel map update. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | We use the collected RGB-D data to update the GS map, similar to our framework. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | We test our implementation on a desktop PC with an Intel Core i9-10940X CPU and an NVIDIA RTX A5000 GPU. | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / III. OUR APPROACH - extractive PDF cue:** Note that the training process involves only a subset of the Gaussian primitive parameters (xi, qi, si, ci, oi), while the modelling of non-trainable ki ...
- **p. 1 / A CTIVE exploration and reconstruction of unknown - extractive PDF cue:** For scenarios, including search and rescue, agricultural robotics, and industrial inspection, online active reconstruction using mobile robots demands both mission efficiency and reconstruction quality.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** normal, loss, Dcos, consists, cosine, distance, between, rendered, derived, depth, along, total, variation, enforce, smooth, rendering, neighbouring, pixels, tackle, first.
- **Relevant PDF headings:** III. OUR APPROACH (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Our experimental results support our three claims: (i) we show that our ActiveGS framework outperforms state-of-theart NeRF-based and GS-based active scene reconstruction ... | p. 5 (IV. EXPERIMENTAL EVALUATION), p. 7 (IV. EXPERIMENTAL EVALUATION) |
| Semantic / temporal fusion | Our ActiveGS outperforms baselines in all test scenes. | p. 6 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION) |
| Robot query / planning handoff | Our approach achieves the best performance in both rendering and mesh quality across all test scenes, supporting our first claim that it ... | p. 6 (IV. EXPERIMENTAL EVALUATION), p. 5 (IV. EXPERIMENTAL EVALUATION) |

## Failure and Ablation Link

- **p. 5 / IV. EXPERIMENTAL EVALUATION - extractive PDF cue:** III-E. • Ours (w/o ROI): A variant of our ActiveGS that leverages only local random sampling, with NROI = 0. • Ours†: A variant of ...
- **p. 7 / IV. EXPERIMENTAL EVALUATION - extractive PDF cue:** Our confidence formulation also outperforms the variant in Ours† by considering viewpoint distribution.
- **p. 7 / IV. EXPERIMENTAL EVALUATION - extractive PDF cue:** The ablation study comparing Ours and Ours (w/o ROI) demonstrates the benefits of ROI-based sampling for targeted inspection, reflected by higher means and smaller standard ...
- **p. 6 / IV. EXPERIMENTAL EVALUATION - extractive PDF cue:** We replace its 3D GS map with our 2D GS. • NARUTO [5]: A state-of-the-art NeRF-based active scene reconstruction pipeline.
- **p. 7 / IV. EXPERIMENTAL EVALUATION - extractive PDF cue:** Unlike simulation experiments, we do not account for the pitch angle of viewpoints in this experiment due to control limitations.
- **p. 7 / IV. EXPERIMENTAL EVALUATION - extractive PDF cue:** Given the limited on-board resources, we run ActiveGS on our desktop PC, where it receives RGB-D and pose data from the UAV for map updates ...
- **p. 5 / IV. EXPERIMENTAL EVALUATION - extractive PDF cue:** The camera has a depth sensing range of [0.1, 5.0] m and Gaussian noise in the depth measurements with linearly increased standard deviation σ = ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (III. OUR APPROACH), p. 2 (A CTIVE exploration and reconstruction of unknown), p. 3 (III. OUR APPROACH), p. 5 (III. OUR APPROACH), p. 3 (III. OUR APPROACH), p. 4 (III. OUR APPROACH), objective p. 2 (A CTIVE exploration and reconstruction of unknown), p. 3 (III. OUR APPROACH), p. 4 (III. OUR APPROACH), p. 4 (III. OUR APPROACH), p. 5 (III. OUR APPROACH), p. 5 (III. OUR APPROACH), temporal p. 5 (IV. EXPERIMENTAL EVALUATION), p. 5 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION), p. 7 (IV. EXPERIMENTAL EVALUATION), p. 7 (IV. EXPERIMENTAL EVALUATION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
