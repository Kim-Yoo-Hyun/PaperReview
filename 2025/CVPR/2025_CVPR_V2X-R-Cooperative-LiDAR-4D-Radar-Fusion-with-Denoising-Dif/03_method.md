# Method - V2X-R: Cooperative LiDAR-4D Radar Fusion with Denoising Diffusion for 3D Object Detection

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Huang_V2X-R_Cooperative_LiDAR-4D_Radar_Fusion_with_Denoising_Diffusion_for_3D_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Huang_V2X-R_Cooperative_LiDAR-4D_Radar_Fusion_with_Denoising_Diffusion_for_3D_CVPR_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 2 (1. Introduction), p. 5 (3) Modal fusion. The weather-induced noisy LiDAR fea), p. 5 (4.3. Multi-modal Denoising Diffusion (MDD)), p. 4 (3) Modal fusion. The weather-induced noisy LiDAR fea), p. 3 (3.1. Simulator Selection), p. 4 (3) Modal fusion. The weather-induced noisy LiDAR fea)): To address the challenge of agent-fused LiDAR features becoming noisy in adverse weather, we propose a novel Multi-modal Diffusion Denoising (MDD) module in the modal fusion stage of the pipeline.

## Method Body Digest

- **p. 2 / 1. Introduction - extractive PDF cue:** To address the challenge of agent-fused LiDAR features becoming noisy in adverse weather, we propose a novel Multi-modal Diffusion Denoising (MDD) module in the modal ...
- **p. 5 / 3) Modal fusion. The weather-induced noisy LiDAR fea - extractive PDF cue:** Specifically, we first extract multi-agent features from LiDAR and 4D radar point clouds individually and then concatenate BEV features in multi-modal fusion (3rd stage).
- **p. 5 / 4.3. Multi-modal Denoising Diffusion (MDD) - extractive PDF cue:** Specifically, drawing inspiration from DDPM [11] and Algorithm 1 Multi-modal Denoising Diffusion process Input: Training ∈{True, False}; Noisy LiDAR BEV feature FL A; Noise-masked LiDAR ...
- **p. 4 / 3) Modal fusion. The weather-induced noisy LiDAR fea - extractive PDF cue:** ture FL A will first be denoised to clear LiDAR feature ˜ FL A by MDD module (will be described in the next section).
- **p. 3 / 3.1. Simulator Selection - extractive PDF cue:** However, since CARLA lacks vehicleto-everything (V2X) communication and cooperative driving capabilities, we used OpenCDA [53] integrated with CARLA, a cooperative simulation platform that supports multiple ...
- **p. 4 / 3) Modal fusion. The weather-induced noisy LiDAR fea - extractive PDF cue:** Finally, we use the detector head to predict the 3D bounding box B by using the multi-agent multi-modal features FM A .
- **p. 6 / A Finit ←FL - extractive PDF cue:** It decreases nonlinearly with epoch so that the model pays full attention to the feature denoising task in the early period and the object detection ...
- **p. 6 / 4.4. Loss Function - extractive PDF cue:** We trained models with our MDD by the following losses: \l a bel {eq_ a ll} \mat h cal {L}_{all} = \beta _{cls}\mathcal {L}_{cls}+\beta _{loc} ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** Our contributions can be summarized in three key points: • We present V2X-R, the first simulated V2X dataset that not only includes LiDAR, cameras, but ...
- **p. 2 / 1. Introduction - extractive PDF cue:** To address the challenge of agent-fused LiDAR features becoming noisy in adverse weather, we propose a novel Multi-modal Diffusion Denoising (MDD) module in the modal ...
- **p. 1 / Abstract - extractive PDF cue:** Subsequently, we propose a novel cooperative LiDAR-4D radar fusion pipeline for 3D object detection and implement it with multiple fusion strategies.

## Source Evidence Cues

- **p. 2 / 1. Introduction - extractive PDF cue:** To address the challenge of agent-fused LiDAR features becoming noisy in adverse weather, we propose a novel Multi-modal Diffusion Denoising (MDD) module in the modal ...
- **p. 5 / 3) Modal fusion. The weather-induced noisy LiDAR fea - extractive PDF cue:** Specifically, we first extract multi-agent features from LiDAR and 4D radar point clouds individually and then concatenate BEV features in multi-modal fusion (3rd stage).
- **p. 5 / 4.3. Multi-modal Denoising Diffusion (MDD) - extractive PDF cue:** Specifically, drawing inspiration from DDPM [11] and Algorithm 1 Multi-modal Denoising Diffusion process Input: Training ∈{True, False}; Noisy LiDAR BEV feature FL A; Noise-masked LiDAR ...
- **p. 4 / 3) Modal fusion. The weather-induced noisy LiDAR fea - extractive PDF cue:** ture FL A will first be denoised to clear LiDAR feature ˜ FL A by MDD module (will be described in the next section).
- **p. 3 / 3.1. Simulator Selection - extractive PDF cue:** However, since CARLA lacks vehicleto-everything (V2X) communication and cooperative driving capabilities, we used OpenCDA [53] integrated with CARLA, a cooperative simulation platform that supports multiple ...
- **p. 4 / 3) Modal fusion. The weather-induced noisy LiDAR fea - extractive PDF cue:** Finally, we use the detector head to predict the 3D bounding box B by using the multi-agent multi-modal features FM A .
- **p. 6 / A Finit ←FL - extractive PDF cue:** It decreases nonlinearly with epoch so that the model pays full attention to the feature denoising task in the early period and the object detection ...
- **Detected method headings:** 5.2. Benchmark Models (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | To address the challenge of agent-fused LiDAR features becoming noisy in adverse weather, we propose a novel Multi-modal Diffusion Denoising (MDD) module ... | p. 2 (1. Introduction), p. 5 (3) Modal fusion. The weather-induced noisy LiDAR fea) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Specifically, we first extract multi-agent features from LiDAR and 4D radar point clouds individually and then concatenate BEV features in multi-modal fusion ... | p. 5 (3) Modal fusion. The weather-induced noisy LiDAR fea), p. 5 (4.3. Multi-modal Denoising Diffusion (MDD)) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Specifically, drawing inspiration from DDPM [11] and Algorithm 1 Multi-modal Denoising Diffusion process Input: Training ∈{True, False}; Noisy LiDAR BEV feature FL ... | p. 5 (4.3. Multi-modal Denoising Diffusion (MDD)), p. 4 (3) Modal fusion. The weather-induced noisy LiDAR fea) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 4.4. Loss Function - extractive PDF cue:** We trained models with our MDD by the following losses: \l a bel {eq_ a ll} \mat h cal {L}_{all} = \beta _{cls}\mathcal {L}_{cls}+\beta _{loc} ...
- **p. 5 / A Finit ←FL - extractive PDF cue:** 8 return Loss, ˜ FL A ▷Get loss and denoised feature else return ˜ FL A ▷Get denoised clear LiDAR feature end if MTL [63], ...
- **p. 5 / A Finit ←FL - extractive PDF cue:** And we compute the loss of MDD as : \l a bel { e q_ md d} \ m athc al {L}_{MDD} = \mathcal {L}_{MSE}(\tilde ...
- **p. 6 / A Finit ←FL - extractive PDF cue:** where FL l is the groundtruth feature extracted from the clear LiDAR point cloud after masking the weather noise, e is the epoch, ψ is ...
- **p. 1 / 1. Introduction - extractive PDF cue:** The advantages of the dense 4D radar point cloud in multi-agent view.
- **p. 1 / 1. Introduction - extractive PDF cue:** Benefiting from the information shared between agents, in complex outdoor scenarios, cooperative 3D object detection has natural advantages, such as long detection distance and multi-view ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (A Finit ←FL), p. 5 (A Finit ←FL), p. 6 (4.4. Loss Function), p. 6 (A Finit ←FL).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Specifically, drawing, inspiration, DDPM, Algorithm, Multi-modal, Denoising, Diffusion, process, Input, Training, True, False, Noisy | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Specifically, drawing, inspiration, DDPM, Algorithm, Multi-modal, Denoising, Diffusion, process, Input | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | contributions, summarized, three, points, present, V2X-R, first, simulated, V2X, dataset | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | trained, models, MDD, following, losses, beta, mathcal, where, hyper-parameters, Lcls | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 4.3. Multi-modal Denoising Diffusion (MDD) - extractive PDF cue:** Specifically, drawing inspiration from DDPM [11] and Algorithm 1 Multi-modal Denoising Diffusion process Input: Training ∈{True, False}; Noisy LiDAR BEV feature FL A; Noise-masked LiDAR ...
- **p. 4 / 4.2. Fusion Pipeline - extractive PDF cue:** Each agent collects LiDAR and 4D radar point cloud data, forming the multi-agent multi-modal input X = {XL C, XL E, XL I , XR ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Benefiting from the information shared between agents, in complex outdoor scenarios, cooperative 3D object detection has natural advantages, such as long detection distance and multi-view ...
- **p. 1 / 1. Introduction - extractive PDF cue:** However, both LiDAR point clouds and camera images are weather-sensitive.
- **p. 2 / 1. Introduction - extractive PDF cue:** V2X-R contains 12,079 scenarios with 37,727 frames of LiDAR and 4D radar point clouds, 150,908 images, and 170,859 annotated 3D vehicle bounding boxes.
- **p. 2 / 1. Introduction - extractive PDF cue:** The error-prone operations (view-transformation or depth-estimation) [1, 44, 45] are not involved in the process of 4D radar and LiDAR point cloud fusing.
- **p. 4 / 3.4. Adverse Weather Simulation - extractive PDF cue:** The input noisy LiDAR features are first subjected to a diffusion process, followed by T step denoising process with weather-robust 4D radar features as conditions ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Although MDD inevitably introduces an additional inference time of 32 ms, it significantly improves weather robustness and still maintains real-time (about 20 ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | The Sensors Details 4x Camera 4 units RGB,Positions: (2.5,0,1.0,0),(0.0,0.3,1.8,100), (0.0,-0.3,1.8,-100), (-2.0,0.0,1.5,180) 1x LiDAR 64 channels,120m range, -25◦to 2◦vertical FOV, 0.02 noise standard ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | Although MDD inevitably introduces an additional inference time of 32 ms, it significantly improves weather robustness and still maintains real-time (about 20 ... | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 4.3. Multi-modal Denoising Diffusion (MDD) - extractive PDF cue:** Specifically, drawing inspiration from DDPM [11] and Algorithm 1 Multi-modal Denoising Diffusion process Input: Training ∈{True, False}; Noisy LiDAR BEV feature FL A; Noise-masked LiDAR ...
- **p. 6 / A Finit ←FL - extractive PDF cue:** It decreases nonlinearly with epoch so that the model pays full attention to the feature denoising task in the early period and the object detection ...
- **p. 8 / 5.4. Multi-modal Diffusion Denoising Analysis - extractive PDF cue:** Although MDD inevitably introduces an additional inference time of 32 ms, it significantly improves weather robustness and still maintains real-time (about 20 FPS).

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** address, challenge, agent-fused, LiDAR, features, becoming, noisy, adverse, weather, novel, Multi-modal, Diffusion, Denoising, MDD, module, modal, fusion, stage, pipeline, Specifically.
- **Relevant PDF headings:** 5.2. Benchmark Models (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Performance comparison under different real-world weather on K-Radar dataset. | p. 8 (5.4. Multi-modal Diffusion Denoising Analysis), p. 8 (5.4. Multi-modal Diffusion Denoising Analysis) |
| Semantic / temporal fusion | We implement various state-of-the-art 3D object detectors on the V2X-R dataset, including different numbers of agents and different modalities. | p. 6 (5.2. Benchmark Models), p. 7 (5.3. Benchmark Analysis) |
| Robot query / planning handoff | Table 7. Effect of each component in MDD module, tested by AttFuse [55] on V2X-R testing with fog-simulation. SM2MM fusion strategies, to ... | p. 8 (Figure/Table caption), p. 2 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 8 / 5.4. Multi-modal Diffusion Denoising Analysis - extractive PDF cue:** We evaluated the effect of each component, as shown in Table 7.
- **p. 8 / 5.4. Multi-modal Diffusion Denoising Analysis - extractive PDF cue:** Effect of each component in MDD module, tested by AttFuse [55] on V2X-R testing with fog-simulation.
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2. The performance of different methods in our V2X-R dataset. (a) Performance comparison of different modalities (L and 4DR represent LiDAR and 4D radar ...
- **p. 7 / 5.3. Benchmark Analysis - extractive PDF cue:** This can be attributed to the significantly lower resolution of 4D radar than LiDAR, which is a limitation hindering the independent use of 4D radar ...
- **p. 7 / 5.3. Benchmark Analysis - extractive PDF cue:** The 3D mAP performance comparison under different weather conditions on the V2X-R dataset. 'L' and '4DR' represent LiDAR and 4D radar, respectively. '-' indicates that ...
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. The advantages of the dense 4D radar point cloud in multi-agent view. Including weather robustness, fewer spatial er- rors, Doppler information, and geometric ...
- **p. 8 / 6. Conclusion and Discussion - extractive PDF cue:** Moreover, we propose the MDD module to tackle dense noise in collaborative conditions.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 2 (1. Introduction), p. 5 (3) Modal fusion. The weather-induced noisy LiDAR fea), p. 5 (4.3. Multi-modal Denoising Diffusion (MDD)), p. 4 (3) Modal fusion. The weather-induced noisy LiDAR fea), p. 3 (3.1. Simulator Selection), p. 4 (3) Modal fusion. The weather-induced noisy LiDAR fea), objective p. 6 (4.4. Loss Function), p. 5 (A Finit ←FL), p. 5 (A Finit ←FL), p. 6 (A Finit ←FL), p. 1 (1. Introduction), p. 1 (1. Introduction), temporal p. 8 (5.4. Multi-modal Diffusion Denoising Analysis), p. 3 (3.2. Sensor configuration), p. 6 (5.1. Experimental Details and Metrics), p. 6 (5.1. Experimental Details and Metrics), p. 7 (5.4. Multi-modal Diffusion Denoising Analysis), p. 8 (5.4. Multi-modal Diffusion Denoising Analysis).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
