# Method - ThermalGaussian: Thermal 3D Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=ybFRoGxZjs; PDF retrieval source: https://openreview.net/pdf/4daa89ce065b5e5cc408ac37b25bc7f3c49e924d.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 7 (3 METHOD), p. 5 (3 METHOD), p. 4 (3 METHOD), p. 6 (3 METHOD), p. 7 (3 METHOD), p. 4 (3 METHOD)): The final design of this loss is: L = γLRGB + (1 -γ)Lthermal (12) 4 SELF-COLLECTED THERAML DATASET We introduce a new dataset, named RGBT-Scenes, which consists of aligned collections ...

## Method Body Digest

- **p. 7 / 3 METHOD - extractive PDF cue:** The final design of this loss is: L = γLRGB + (1 -γ)Lthermal (12) 4 SELF-COLLECTED THERAML DATASET We introduce a new dataset, named RGBT-Scenes, ...
- **p. 5 / 3 METHOD - extractive PDF cue:** Multimodal Fine-Tuning Gaussians (MFTG): Inspired by the fine-tuning approach used in largescale models, our first multimodal training strategy is training a basic Gaussian with RGB ...
- **p. 4 / 3 METHOD - extractive PDF cue:** Then, we provide a detailed description of our method's specific implementation details, including multimodal initialization, three types of multimodal thermal Gaussians, thermal loss, and multimodal ...
- **p. 6 / 3 METHOD - extractive PDF cue:** However, because thermal images exhibit unique low-texture and ghosting characteristics, we design a specific thermal loss function to better accommodate these features.
- **p. 7 / 3 METHOD - extractive PDF cue:** Therefore, a regularization strategy is needed to dynamically adjust the weight of each modality's loss during training.
- **p. 4 / 3 METHOD - extractive PDF cue:** All attributes of the 3D Gaussians are learnable and optimized directly in an end-to-end manner during training.
- **p. 5 / 3 METHOD - extractive PDF cue:** 3.3 THERMAL GAUSSIAN We utilize three different multimodal training strategies to construct the thermal Gaussian.
- **p. 6 / 3 METHOD - extractive PDF cue:** RGB rendering is achieved using Formula 3, while thermal rendering follows the equation below: T (x′) = X k∈N tkαk k-1 Y j=1 (1 -αj) ...

## Design Rationale

- **p. 7 / 3 METHOD - extractive PDF cue:** The final design of this loss is: L = γLRGB + (1 -γ)Lthermal (12) 4 SELF-COLLECTED THERAML DATASET We introduce a new dataset, named RGBT-Scenes, ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** In summary, the main contributions as follows: (1)We propose ThermalGaussian, the first multimodal 3DGS capable of simultaneously rendering photorealistic thermal and RGB images of a ...
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** Published as a conference paper at ICLR 2025 (3)We introduce RGBT-Scenes, a new dataset designed for thermal 3D reconstruction and novelview synthesis.

## Source Evidence Cues

- **p. 7 / 3 METHOD - extractive PDF cue:** The final design of this loss is: L = γLRGB + (1 -γ)Lthermal (12) 4 SELF-COLLECTED THERAML DATASET We introduce a new dataset, named RGBT-Scenes, ...
- **p. 5 / 3 METHOD - extractive PDF cue:** Multimodal Fine-Tuning Gaussians (MFTG): Inspired by the fine-tuning approach used in largescale models, our first multimodal training strategy is training a basic Gaussian with RGB ...
- **p. 4 / 3 METHOD - extractive PDF cue:** Then, we provide a detailed description of our method's specific implementation details, including multimodal initialization, three types of multimodal thermal Gaussians, thermal loss, and multimodal ...
- **p. 6 / 3 METHOD - extractive PDF cue:** However, because thermal images exhibit unique low-texture and ghosting characteristics, we design a specific thermal loss function to better accommodate these features.
- **p. 7 / 3 METHOD - extractive PDF cue:** Therefore, a regularization strategy is needed to dynamically adjust the weight of each modality's loss during training.
- **p. 4 / 3 METHOD - extractive PDF cue:** All attributes of the 3D Gaussians are learnable and optimized directly in an end-to-end manner during training.
- **p. 5 / 3 METHOD - extractive PDF cue:** 3.3 THERMAL GAUSSIAN We utilize three different multimodal training strategies to construct the thermal Gaussian.
- **Detected method headings:** 3 METHOD (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | The final design of this loss is: L = γLRGB + (1 -γ)Lthermal (12) 4 SELF-COLLECTED THERAML DATASET We introduce a new ... | p. 7 (3 METHOD), p. 5 (3 METHOD) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Multimodal Fine-Tuning Gaussians (MFTG): Inspired by the fine-tuning approach used in largescale models, our first multimodal training strategy is training a basic ... | p. 5 (3 METHOD), p. 4 (3 METHOD) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Then, we provide a detailed description of our method's specific implementation details, including multimodal initialization, three types of multimodal thermal Gaussians, thermal ... | p. 4 (3 METHOD), p. 6 (3 METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 3 METHOD - extractive PDF cue:** RGB rendering is achieved using Formula 3, while thermal rendering follows the equation below: T (x′) = X k∈N tkαk k-1 Y j=1 (1 -αj) ...
- **p. 6 / 3 METHOD - extractive PDF cue:** One Multi-Modal Gaussian(OMMG): OMMG extends MSMG by not only employing dualmodal loss constraints in Eq.
- **p. 4 / 3 METHOD - extractive PDF cue:** Then, we provide a detailed description of our method's specific implementation details, including multimodal initialization, three types of multimodal thermal Gaussians, thermal loss, and multimodal ...
- **p. 7 / 3 METHOD - extractive PDF cue:** Therefore, a regularization strategy is needed to dynamically adjust the weight of each modality's loss during training.
- **p. 5 / 3 METHOD - extractive PDF cue:** The second approach, illustrated in Fig.2(c), involves blending registered color and thermal images using the following formula: Imix = βITh + (1 -β)IRGB (5) where ...
- **p. 7 / 3 METHOD - extractive PDF cue:** The final design of this loss is: L = γLRGB + (1 -γ)Lthermal (12) 4 SELF-COLLECTED THERAML DATASET We introduce a new dataset, named RGBT-Scenes, ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 6 (3 METHOD), p. 6 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD), p. 7 (3 METHOD), p. 7 (3 METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Published, conference, ICLR, point, clouds, obtained, multimodal, initialization, inputs, capture, simultaneous, color, thermal, images | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Published, conference, ICLR, point, clouds, obtained, multimodal, initialization, inputs, capture | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | final, design, loss, LRGB, Lthermal, SELF-COLLECTED, THERAML, DATASET, introduce, named | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | RGB, rendering, achieved, Formula, while, thermal, follows, equation, below, LOSS | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 6 / 3 METHOD - extractive PDF cue:** Published as a conference paper at ICLR 2025 point clouds obtained from multimodal initialization as inputs.
- **p. 5 / 3 METHOD - extractive PDF cue:** We capture simultaneous color and thermal images before thermal equilibrium, which occurs when two systems reach a balanced state with equal temperatures, halting heat flow.
- **p. 6 / 3 METHOD - extractive PDF cue:** Subsequently, these rendered images of both modalities are compared separately with the ground truth of their respective inputs using loss functions: L = LRGB + ...
- **p. 4 / 3 METHOD - extractive PDF cue:** Initially, a set of unordered images of objects to be reconstructed is processed using SfM to obtain the camera poses and sparse point clouds.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Bottom: input images for SfM. geometry methods (Newcombe et al., 2011) are used to achieve a 3D geometric reconstruction.
- **p. 4 / 3 METHOD - extractive PDF cue:** 3 shows the overview of the proposed ThermalGaussian, which is based on the 3DGS (Kerbl et al., 2023), aiming to extend its capability to simultaneously ...
- **p. 5 / 3 METHOD - extractive PDF cue:** The first utilizes registered high-texture RGB images directly for camera pose estimation.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | The third strategy, depicted in Fig.2(d), maps highfrequency color variations from the color images onto the thermal images. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | 5.1 IMPLEMENTATION DETAILS Our method is an improvement upon the 3DGS framework, with all experimental settings (e.g., λ) remaining consistent with the ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | We then performed a comprehensive comparison across various dimensions, including rendering capability, the quality of rendered color and thermal images, training time, ... | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | All experiments are conducted on a single NVIDIA 3090 GPU. | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3 METHOD - extractive PDF cue:** Multimodal Fine-Tuning Gaussians (MFTG): Inspired by the fine-tuning approach used in largescale models, our first multimodal training strategy is training a basic Gaussian with RGB ...
- **p. 7 / 3 METHOD - extractive PDF cue:** Therefore, a regularization strategy is needed to dynamically adjust the weight of each modality's loss during training.
- **p. 4 / 3 METHOD - extractive PDF cue:** All attributes of the 3D Gaussians are learnable and optimized directly in an end-to-end manner during training.
- **p. 5 / 3 METHOD - extractive PDF cue:** 3.3 THERMAL GAUSSIAN We utilize three different multimodal training strategies to construct the thermal Gaussian.
- **p. 10 / 5 EXPERIMENTS - extractive PDF cue:** We then performed a comprehensive comparison across various dimensions, including rendering capability, the quality of rendered color and thermal images, training time, model memory usage, ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** final, design, loss, LRGB, Lthermal, SELF-COLLECTED, THERAML, DATASET, introduce, named, RGBT-Scenes, consists, aligned, collections, thermal, RGB, images, captured, various, viewpoints.
- **Relevant PDF headings:** 3 METHOD (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | As shown in Table 2, even in scenes with pronounced thermal variations, specifically targeting lowtexture thermal characteristics, direct application of thermal data ... | p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |
| Semantic / temporal fusion | We conducted ablation experiments by gradually adding each component to the baseline 3DGS model. | p. 10 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |
| Robot query / planning handoff | We not only achieve simultaneous rendering of thermal and RGB images but also significantly improve the rendering quality of both color and ... | p. 10 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |

## Failure and Ablation Link

- **p. 10 / 5 EXPERIMENTS - extractive PDF cue:** 5.4 ABLATION STUDY We separate different contributions and algorithm choices to test their effectiveness.
- **p. 10 / 5 EXPERIMENTS - extractive PDF cue:** We conducted ablation experiments by gradually adding each component to the baseline 3DGS model.
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2: Top: camera poses and point cloud generated by SfM. Bottom: input images for SfM. geometry methods (Newcombe et al., 2011) are used to ...
- **p. 8 / 5 EXPERIMENTS - extractive PDF cue:** Published as a conference paper at ICLR 2025 Table 2: Quantitative evaluation of thermal image using our method compared to previous work from test views. ...
- **p. 10 / 5 EXPERIMENTS - extractive PDF cue:** We then performed a comprehensive comparison across various dimensions, including rendering capability, the quality of rendered color and thermal images, training time, model memory usage, ...
- **p. 9 / 5 EXPERIMENTS - extractive PDF cue:** Our results demonstrate that, under multimodal constraints, when one modality fails, our approach leverages accurate information from the other modality to enhance the model's understanding ...
- **p. 10 / 5 EXPERIMENTS - extractive PDF cue:** In the appendix, we discuss the limitations of this work and potential directions for future research.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 7 (3 METHOD), p. 5 (3 METHOD), p. 4 (3 METHOD), p. 6 (3 METHOD), p. 7 (3 METHOD), p. 4 (3 METHOD), objective p. 6 (3 METHOD), p. 6 (3 METHOD), p. 4 (3 METHOD), p. 7 (3 METHOD), p. 5 (3 METHOD), p. 7 (3 METHOD), temporal p. 5 (3 METHOD), p. 7 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 1 (ABSTRACT), p. 3 (2 RELATED WORK).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
