# Method - SimULi: Real-Time LiDAR and Camera Simulation with Unscented Transforms

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=osxP6FafPZ; PDF retrieval source: https://openreview.net/pdf/ef221d27302d56bbadab6a1b5f71203b078ccc4f.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 7 (3 METHOD), p. 6 (3 METHOD), p. 6 (3 METHOD), p. 7 (3 METHOD), p. 4 (3 METHOD), p. 4 (3 METHOD)): As crosssensor data contains inconsistencies that are impossible to eliminate, this forces the representation to prioritize the reconstruction quality of one modality over the other based on loss weights (Fig.

## Method Body Digest

- **p. 7 / 3 METHOD - extractive PDF cue:** As crosssensor data contains inconsistencies that are impossible to eliminate, this forces the representation to prioritize the reconstruction quality of one modality over the other ...
- **p. 6 / 3 METHOD - extractive PDF cue:** Prior work encodes camera and LiDAR into the same representation constrained with a LiDAR-supervised depth loss.
- **p. 6 / 3 METHOD - extractive PDF cue:** As cross-sensor data is not fully consistent, this forces the representation to prioritize camera instead of LiDAR quality (left) or the inverse (middle), as shown ...
- **p. 7 / 3 METHOD - extractive PDF cue:** We minimize the K-distance loss at each training iteration, and update the camera-to-LiDAR assignments every 1000 iterations.
- **p. 4 / 3 METHOD - extractive PDF cue:** We describe our representation in Sec.
- **p. 4 / 3 METHOD - extractive PDF cue:** 3.1 REPRESENTATION Particle Representation.
- **p. 5 / 3 METHOD - extractive PDF cue:** We obtain the final color prediction c via an affine transformation from a learned bilateral grid A (Wang et al., 2024) that handles lighting variations ...
- **p. 6 / 3 METHOD - extractive PDF cue:** We minimize a reconstruction loss, an anchoring loss that encourages camera Gaussians in Gc to lie near the LiDAR-supervised scene geometry distilled into Gl, and ...

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** In this work, we propose a high-fidelity and efficient reconstruction pipeline that enables joint camera and LiDAR simulation for AV scenarios.
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** We make the following contributions: (1) we extend 3DGUT with LiDAR support and introduce an automated tiling scheme from which we derive optimal tiling parameters ...
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** Published as a conference paper at ICLR 2026 Contributions.

## Source Evidence Cues

- **p. 7 / 3 METHOD - extractive PDF cue:** As crosssensor data contains inconsistencies that are impossible to eliminate, this forces the representation to prioritize the reconstruction quality of one modality over the other ...
- **p. 6 / 3 METHOD - extractive PDF cue:** Prior work encodes camera and LiDAR into the same representation constrained with a LiDAR-supervised depth loss.
- **p. 6 / 3 METHOD - extractive PDF cue:** As cross-sensor data is not fully consistent, this forces the representation to prioritize camera instead of LiDAR quality (left) or the inverse (middle), as shown ...
- **p. 7 / 3 METHOD - extractive PDF cue:** We minimize the K-distance loss at each training iteration, and update the camera-to-LiDAR assignments every 1000 iterations.
- **p. 4 / 3 METHOD - extractive PDF cue:** We describe our representation in Sec.
- **p. 4 / 3 METHOD - extractive PDF cue:** 3.1 REPRESENTATION Particle Representation.
- **p. 5 / 3 METHOD - extractive PDF cue:** We obtain the final color prediction c via an affine transformation from a learned bilateral grid A (Wang et al., 2024) that handles lighting variations ...
- **Detected method headings:** 3 METHOD (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | As crosssensor data contains inconsistencies that are impossible to eliminate, this forces the representation to prioritize the reconstruction quality of one modality ... | p. 7 (3 METHOD), p. 6 (3 METHOD) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Prior work encodes camera and LiDAR into the same representation constrained with a LiDAR-supervised depth loss. | p. 6 (3 METHOD), p. 6 (3 METHOD) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | As cross-sensor data is not fully consistent, this forces the representation to prioritize camera instead of LiDAR quality (left) or the inverse ... | p. 6 (3 METHOD), p. 7 (3 METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 3 METHOD - extractive PDF cue:** We minimize a reconstruction loss, an anchoring loss that encourages camera Gaussians in Gc to lie near the LiDAR-supervised scene geometry distilled into Gl, and ...
- **p. 6 / 3 METHOD - extractive PDF cue:** We minimize Lrecon via L1 photometric loss Lphoto, SSIM loss LSSIM, L1 distance loss Ldist, L1 intensity loss Lint, and binary cross-entropy ray drop loss ...
- **p. 7 / 3 METHOD - extractive PDF cue:** We minimize the K-distance loss at each training iteration, and update the camera-to-LiDAR assignments every 1000 iterations.
- **p. 5 / 3 METHOD - extractive PDF cue:** We measure the particle response function of each Gaussian in 3D via the distance εmax := argmaxωϱi(o + εd) that maximizes ϱi along the ray ...
- **p. 7 / 3 METHOD - extractive PDF cue:** Camera losses only require rendering and backpropagating through particles in Gc (and LiDAR losses through Gl).
- **p. 5 / 3 METHOD - extractive PDF cue:** We decode beam intensity φ ↑R from the first channel of ς and derive a ray drop probability ↼↑R by applying the softmax function on ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 7 (3 METHOD), p. 7 (3 METHOD), p. 5 (3 METHOD), p. 6 (3 METHOD), p. 6 (3 METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | OPTIMIZATION, jointly, optimize, camera, particles, LiDAR, bilateral, grids, environment, sampling, random, input, image, scan | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | OPTIMIZATION, jointly, optimize, camera, particles, LiDAR, bilateral, grids, environment, sampling | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | high-fidelity, efficient, reconstruction, pipeline, enables, joint, camera, LiDAR, simulation, scenarios | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | minimize, reconstruction, loss, anchoring, encourages, camera, Gaussians, near, LiDAR-supervised, scene | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 6 / 3 METHOD - extractive PDF cue:** 3.4 OPTIMIZATION We jointly optimize the camera particles Gc, LiDAR particles Gl, bilateral grids A, and the environment map by sampling a random input image ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** With the rise of end-to-end policy models, accurate sensor simulation has become a critical component in the development and evaluation of autonomous vehicle (AV) systems.
- **p. 6 / 3 METHOD - extractive PDF cue:** We derive an automated strategy that takes elevation angles as input and computes an equalized elevation tiling and azimuth tile count such that each elevation ...
- **p. 7 / 3 METHOD - extractive PDF cue:** Projecting LiDAR as a sparse depth map causes inaccuracies that degrade 3DGUT's rendering of the pole (above), which we avoid by rendering LiDAR directly.
- **p. 7 / 3 METHOD - extractive PDF cue:** As crosssensor data contains inconsistencies that are impossible to eliminate, this forces the representation to prioritize the reconstruction quality of one modality over the other ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** As they are optimized to match real-world observations, they also exhibit a smaller domain gap compared to traditional artist-generated simulators.
- **p. 4 / 3 METHOD - extractive PDF cue:** Each object is associated with a 3D bounding box and a sequence of SE(3) poses adjusted with learnable offsets.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Each object is associated with a 3D bounding box and a sequence of SE(3) poses adjusted with learnable offsets. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Our goal is to learn a controllable scene representation that simulates camera and LiDAR renderings from novel viewpoints in real-time (Fig. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | We filter in constant time (4 memory reads + 3 arithmetic operations) via a 2D range query where we first construct a ... | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | We then compute an azimuth tile count such that the beam count per tile differs at most by 8 samples (right). | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 3 METHOD - extractive PDF cue:** Prior work encodes camera and LiDAR into the same representation constrained with a LiDAR-supervised depth loss.
- **p. 7 / 3 METHOD - extractive PDF cue:** We minimize the K-distance loss at each training iteration, and update the camera-to-LiDAR assignments every 1000 iterations.
- **p. 6 / 3 METHOD - extractive PDF cue:** We finally compute the azimuth tile count and the maximum point count per tile constraint M.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** crosssensor, data, contains, inconsistencies, impossible, eliminate, forces, representation, prioritize, reconstruction, quality, modality, over, other, loss, weights, Fig, Prior, encodes, camera.
- **Relevant PDF headings:** 3 METHOD (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We perform experiments on all four scenes of the Waymo Interp. benchmark (Huang et al., 2023) and follow the suggested protocol of ... | p. 8 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS) |
| Semantic / temporal fusion | Table 5. Not only does anchoring improve NVS compared to camera-only reconstruction (⇀d = 0), but it outperforms the unified strategy across ... | p. 10 (Figure/Table caption), p. 8 (4 EXPERIMENTS) |
| Robot query / planning handoff | Not only does anchoring improve NVS compared to camera-only reconstruction (⇀d = 0), but it outperforms the unified strategy across all metrics ... | p. 10 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |

## Failure and Ablation Link

- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** We evaluate image quality through PSNR, SSIM (Wang et al., 2004), and the AlexNet variant of LPIPS (Zhang et al., 2018).
- **p. 10 / 4 EXPERIMENTS - extractive PDF cue:** Compared to SplatAD (Hess et al., 2025), the method closest to ours, we improve PSNR by 0.4-1.7 dB without relying on CNNs for view dependence, ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Table 5: Ablations. NVS metrics averaged across PandaSet.
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** We validate the efficacy of our components in Sec.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5: Static NVS. Projecting LiDAR as a sparse depth map causes inaccuracies that degrade 3DGUT's rendering of the pole (above), which we avoid by ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 6: Dynamic Scenes. FPS numbers are averaged across Waymo Dynamic and PandaSet. Approaches that use CNNs for upsampling (Yang et al., 2023b; Tonderski et ...
- **p. 10 / 4 EXPERIMENTS - extractive PDF cue:** The choice M = 32, Nε = 16 gives the best LiDAR rendering speed (note that does not affect quality).

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 7 (3 METHOD), p. 6 (3 METHOD), p. 6 (3 METHOD), p. 7 (3 METHOD), p. 4 (3 METHOD), p. 4 (3 METHOD), objective p. 6 (3 METHOD), p. 6 (3 METHOD), p. 7 (3 METHOD), p. 5 (3 METHOD), p. 7 (3 METHOD), p. 5 (3 METHOD), temporal p. 4 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD), p. 5 (3 METHOD), p. 6 (3 METHOD), p. 6 (3 METHOD).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
