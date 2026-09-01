# Method - PhysSplat: Efficient Physics Simulation for 3D Scenes via MLLM-Guided Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Zhao_PhysSplat_Efficient_Physics_Simulation_for_3D_Scenes_via_MLLM-Guided_Gaussian_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhao_PhysSplat_Efficient_Physics_Simulation_for_3D_Scenes_via_MLLM-Guided_Gaussian_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (4.2. MLLM-based Physical Property Perception), p. 3 (4. Our Methodology), p. 3 (4.1. 3D Open-vocabulary Segmentation), p. 4 (4.1. 3D Open-vocabulary Segmentation), p. 5 (4.3. Physics-Based Dynamics), p. 5 (4.3. Physics-Based Dynamics)): Then we use a VQA model, such as BLIP [19] to produce a text description of the image.

## Method Body Digest

- **p. 4 / 4.2. MLLM-based Physical Property Perception - extractive PDF cue:** Then we use a VQA model, such as BLIP [19] to produce a text description of the image.
- **p. 3 / 4. Our Methodology - extractive PDF cue:** We then use the Material Property Distribution Prediction (MPDP) model to estimate the full distribution, simulating object dynamics with driving particles sampled using the Physical-Geometric ...
- **p. 3 / 4.1. 3D Open-vocabulary Segmentation - extractive PDF cue:** For each scene, we first train a 3DGS model on given images and camera poses.
- **p. 4 / 4.1. 3D Open-vocabulary Segmentation - extractive PDF cue:** We obtain the mean physical properties of the object from the proposed MLLM-P3, and based on this and the object's geometry, we then derive the ...
- **p. 5 / 4.3. Physics-Based Dynamics - extractive PDF cue:** To model physical properties, we employ MLS-MPM [12] as our simulator.
- **p. 5 / 4.3. Physics-Based Dynamics - extractive PDF cue:** Our observation is that softer objects and those with complex shapes require more driving particles to accurately simulate their dynamics.
- **p. 8 / Method - extractive PDF cue:** This demonstrates PGAS's enhanced capability in reconstructing photorealistic 4D dynamics.
- **p. 3 / 3.1. Material Point Method - extractive PDF cue:** Following PhysGaussian[42], we define each Gaussian kernel's time-dependent state as: x_i ( t) = \De lta ( x _i, t), \ \Si gma _i(t) = ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** Our method is the only one that can simulate the entire scene at a much faster speed. priors into 3D object representations using physical simulators ...
- **p. 2 / 1. Introduction - extractive PDF cue:** In this paper, we propose PhysSplat, a physics-based method that efficiently transforms static 3D objects into interactive ones capable of responding to new interactions, as ...
- **p. 3 / 4. Our Methodology - extractive PDF cue:** We propose MLLM-based Physical Property Perception (MLLM-P3) to predict the mean values of these properties (Section 4.2).

## Source Evidence Cues

- **p. 4 / 4.2. MLLM-based Physical Property Perception - extractive PDF cue:** Then we use a VQA model, such as BLIP [19] to produce a text description of the image.
- **p. 3 / 4. Our Methodology - extractive PDF cue:** We then use the Material Property Distribution Prediction (MPDP) model to estimate the full distribution, simulating object dynamics with driving particles sampled using the Physical-Geometric ...
- **p. 3 / 4.1. 3D Open-vocabulary Segmentation - extractive PDF cue:** For each scene, we first train a 3DGS model on given images and camera poses.
- **p. 4 / 4.1. 3D Open-vocabulary Segmentation - extractive PDF cue:** We obtain the mean physical properties of the object from the proposed MLLM-P3, and based on this and the object's geometry, we then derive the ...
- **p. 5 / 4.3. Physics-Based Dynamics - extractive PDF cue:** To model physical properties, we employ MLS-MPM [12] as our simulator.
- **p. 5 / 4.3. Physics-Based Dynamics - extractive PDF cue:** Our observation is that softer objects and those with complex shapes require more driving particles to accurately simulate their dynamics.
- **p. 8 / Method - extractive PDF cue:** This demonstrates PGAS's enhanced capability in reconstructing photorealistic 4D dynamics.
- **Detected method headings:** 3.1. Material Point Method (p. 3); 4. Our Methodology (p. 3); 5.3. Comparison with SOTA Methods (p. 6); Method (p. 8)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Then we use a VQA model, such as BLIP [19] to produce a text description of the image. | p. 4 (4.2. MLLM-based Physical Property Perception), p. 3 (4. Our Methodology) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | We then use the Material Property Distribution Prediction (MPDP) model to estimate the full distribution, simulating object dynamics with driving particles sampled ... | p. 3 (4. Our Methodology), p. 3 (4.1. 3D Open-vocabulary Segmentation) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | For each scene, we first train a 3DGS model on given images and camera poses. | p. 3 (4.1. 3D Open-vocabulary Segmentation), p. 4 (4.1. 3D Open-vocabulary Segmentation) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3.1. Material Point Method - extractive PDF cue:** Following PhysGaussian[42], we define each Gaussian kernel's time-dependent state as: x_i ( t) = \De lta ( x _i, t), \ \Si gma _i(t) = ...
- **p. 4 / 4.2. MLLM-based Physical Property Perception - extractive PDF cue:** This enables the model to return a list of physical properties for the object, M = ρ, E, ν, where ρ represents the density, E ...
- **p. 4 / 4.2. MLLM-based Physical Property Perception - extractive PDF cue:** This description, along with the image, are then passed to a Multi-modal Large Language Model (MLLM) such as GPT-4V [43], prompting it to return a ...
- **p. 5 / 4.3. Physics-Based Dynamics - extractive PDF cue:** In MPM, a continuum is represented by particles distributed in a grid-based space, offering a distinct advantage over mesh-based methods.
- **p. 5 / 4.3. Physics-Based Dynamics - extractive PDF cue:** The network predicts the geometry-aware probability distribution P of physical properties across particles, P = Dθ(X). where X is the position of 3D Gaussians of ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 3 (3.1. Material Point Method), p. 5 (4.3. Physics-Based Dynamics).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Finally, selected, material, name, image, text, description, provide, structured, input, MLLM, grounding, outputs, reliable | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Finally, selected, material, name, image, text, description, provide, structured, input | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | only, simulate, entire, scene, much, faster, speed, priors, object, representations | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Following, PhysGaussian, define, Gaussian, kernel, time-dependent, state, F_i, Sigma, where | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 4.2. MLLM-based Physical Property Perception - extractive PDF cue:** Finally, the selected material name, image, and text description provide a structured input to the MLLM, grounding its outputs in a reliable context.
- **p. 5 / 4.3. Physics-Based Dynamics - extractive PDF cue:** We train a network Dθ using part of the synthesized dataset, with the object's point cloud and predicted mean values (Section 4.2) as input.
- **p. 3 / 4.1. 3D Open-vocabulary Segmentation - extractive PDF cue:** These models automatically segment objects in images without textual input.
- **p. 1 / 1. Introduction - extractive PDF cue:** However, these approaches are unable to simulate interactions with 3D assets in simulation environments [32, 41], which is s critical for generating realistic object responses ...
- **p. 2 / 1. Introduction - extractive PDF cue:** In this paper, we propose PhysSplat, a physics-based method that efficiently transforms static 3D objects into interactive ones capable of responding to new interactions, as ...
- **p. 3 / 3.1. Material Point Method - extractive PDF cue:** The Material Point Method (MPM)[12] is a popular simulation framework for multi-physics phenomena due to its capability to handle topology changes and frictional interactions.
- **p. 5 / 4.3. Physics-Based Dynamics - extractive PDF cue:** Our observation is that softer objects and those with complex shapes require more driving particles to accurately simulate their dynamics.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Following PhysGaussian[42], we define each Gaussian kernel's time-dependent state as: x_i ( t) = \De lta ( x _i, t), \ \Si ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Our PhysSplat produces more realistic damping, closely matching real-world capture. sub-steps per interval between video frames, resulting in a sub-step duration of ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | All experiments are conducted on a single NVIDIA 3090 GPU. | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 4.1. 3D Open-vocabulary Segmentation - extractive PDF cue:** For each scene, we first train a 3DGS model on given images and camera poses.
- **p. 6 / 5.3. Comparison with SOTA Methods - extractive PDF cue:** Since PhysDreamer [47] has not released its training code, we only compare the four evaluation scene and are unable to report its inference time.
- **p. 8 / Method - extractive PDF cue:** Time measures the inference speed for physics-based 4D generation on an single RTX 4090 GPU.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Then, VQA, model, BLIP, produce, text, description, image, Material, Property, Distribution, Prediction, MPDP, estimate, full, simulating, object, dynamics, driving, particles.
- **Relevant PDF headings:** 3.1. Material Point Method (p. 3); 4. Our Methodology (p. 3); 5.3. Comparison with SOTA Methods (p. 6); Method (p. 8).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We also conduct experiments on the physical simulation of single objects on four real-world static scenes from PhysDreamer [47] for fair comparison. | p. 6 (5.2. Datasets), p. 6 (5.3. Comparison with SOTA Methods) |
| Semantic / temporal fusion | Figure 7. Ablation study. Visualization of space-time slices for ablation study on PhysDreamer [47]. Our method can generate closer content compared with ... | p. 8 (Figure/Table caption), p. 1 (Figure/Table caption) |
| Robot query / planning handoff | Our PhysSplat achieves better performance in both metrics, which demonstrates that PhysSplat generates videos that are both realistic and physically plausible, with ... | p. 6 (5.3. Comparison with SOTA Methods), p. 8 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 7 / 5.4. Ablation study - extractive PDF cue:** In this section, we conduct ablation experiments using PhysDreamer [47] dataset to evaluate the effectiveness of our proposed modules.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3. Ablation Study on PhysDreamer [47] dataset. AS denotes the average aesthetic quality score predicted using the LAION aesthetic predictor. property distribution prediction is ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 7. Ablation study. Visualization of space-time slices for ablation study on PhysDreamer [47]. Our method can generate closer content compared with the real capture. ...
- **p. 8 / 7. Conclusion - extractive PDF cue:** Future work will explore to reconstruct occluded parts, further enhancing realism and expanding applications in interactive virtual experiences.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (4.2. MLLM-based Physical Property Perception), p. 3 (4. Our Methodology), p. 3 (4.1. 3D Open-vocabulary Segmentation), p. 4 (4.1. 3D Open-vocabulary Segmentation), p. 5 (4.3. Physics-Based Dynamics), p. 5 (4.3. Physics-Based Dynamics), objective p. 3 (3.1. Material Point Method), p. 4 (4.2. MLLM-based Physical Property Perception), p. 4 (4.2. MLLM-based Physical Property Perception), p. 5 (4.3. Physics-Based Dynamics), p. 5 (4.3. Physics-Based Dynamics), temporal p. 3 (3.1. Material Point Method), p. 6 (5.1. Implementation Details), p. 3 (3.1. Material Point Method), p. 6 (5.3. Comparison with SOTA Methods), p. 8 (Method), p. 8 (7. Conclusion).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
