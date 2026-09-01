# Method - Persistent Object Gaussian Splat (POGS) for Tracking Human and Robot Manipulation of Irregularly Shaped Objects

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.proceedings.com/content/081/081087webtoc.pdf; PDF retrieval source: https://arxiv.org/pdf/2503.05189v1. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3) Persistent Object Tracking phase for online tracking), p. 4 (3) Persistent Object Tracking phase for online tracking), p. 2 (Abstract), p. 3 (3) Persistent Object Tracking phase for online tracking), p. 1 (Abstract), p. 1 (Abstract)): We use Nerfstudio's [55] Splatfacto implementation of Gaussian Splatting with the gsplat [53] backend and modify it with the aforementioned image encoders and feature supervision losses.

## Method Body Digest

- **p. 4 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** We use Nerfstudio's [55] Splatfacto implementation of Gaussian Splatting with the gsplat [53] backend and modify it with the aforementioned image encoders and feature supervision ...
- **p. 4 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** These features are then supervised into the gaussians, enabling the model to render them at deployment time for optimizing object tracking objectives, similar to the ...
- **p. 2 / Abstract - extractive body cue:** Training images are used to optimize a 3DGS, and features extracted from 2D foundation models are distilled into feature fields, producing our POGS unified representation.
- **p. 3 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** 3D grouping features are then supervised with the contrastive objective from Bhalgat et al.
- **p. 1 / Abstract - extractive body cue:** After an initial multi-view scene capture and training phase, POGS uses a single stereo camera to integrate depth estimates along with self-supervised vision encoder features ...
- **p. 1 / Abstract - extractive body cue:** To enable online state estimation, tracking, and manipulation of unseen objects in dynamic environments, we present Persistent Object Gaussian Splat (POGS), an editable objectcentric feature ...
- **p. 2 / Abstract - extractive body cue:** However, NeRF-based representations are limited by NeRF's training speed and implicit spatial representation, making it impossible to update when objects move without further scene-scale optimization.
- **p. 3 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** [50], which operates through two complementary mechanisms: (1) attracting features that belong to the same object mask by minimizing their distance in embedding space, and ...

## Design Rationale

- **p. 2 / Abstract - extractive body cue:** This paper makes the following contributions: • Persistent Object Gaussian Splat (POGS), a novel feature field representation for tracking and manipulating previously unseen irregularly shaped ...
- **p. 1 / Abstract - extractive body cue:** To enable online state estimation, tracking, and manipulation of unseen objects in dynamic environments, we present Persistent Object Gaussian Splat (POGS), an editable objectcentric feature ...
- **p. 1 / Abstract - extractive body cue:** (Bottom) A POGS unified representation enables language querying, grasp sampling, and continuous tracking of irregular objects as they move.

## Source Evidence Cues

- **p. 4 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** We use Nerfstudio's [55] Splatfacto implementation of Gaussian Splatting with the gsplat [53] backend and modify it with the aforementioned image encoders and feature supervision ...
- **p. 4 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** These features are then supervised into the gaussians, enabling the model to render them at deployment time for optimizing object tracking objectives, similar to the ...
- **p. 2 / Abstract - extractive body cue:** Training images are used to optimize a 3DGS, and features extracted from 2D foundation models are distilled into feature fields, producing our POGS unified representation.
- **p. 3 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** 3D grouping features are then supervised with the contrastive objective from Bhalgat et al.
- **p. 1 / Abstract - extractive body cue:** After an initial multi-view scene capture and training phase, POGS uses a single stereo camera to integrate depth estimates along with self-supervised vision encoder features ...
- **p. 1 / Abstract - extractive body cue:** To enable online state estimation, tracking, and manipulation of unseen objects in dynamic environments, we present Persistent Object Gaussian Splat (POGS), an editable objectcentric feature ...
- **p. 2 / Abstract - extractive body cue:** However, NeRF-based representations are limited by NeRF's training speed and implicit spatial representation, making it impossible to update when objects move without further scene-scale optimization.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | We use Nerfstudio's [55] Splatfacto implementation of Gaussian Splatting with the gsplat [53] backend and modify it with the aforementioned image encoders ... | p. 4 (3) Persistent Object Tracking phase for online tracking), p. 4 (3) Persistent Object Tracking phase for online tracking) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | These features are then supervised into the gaussians, enabling the model to render them at deployment time for optimizing object tracking objectives, ... | p. 4 (3) Persistent Object Tracking phase for online tracking), p. 2 (Abstract) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Training images are used to optimize a 3DGS, and features extracted from 2D foundation models are distilled into feature fields, producing our ... | p. 2 (Abstract), p. 3 (3) Persistent Object Tracking phase for online tracking) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** [50], which operates through two complementary mechanisms: (1) attracting features that belong to the same object mask by minimizing their distance in embedding space, and ...
- **p. 3 / Abstract - extractive body cue:** Given a single stereo camera, the objective is to track the 6D pose of each object over time and update the 3D scene models.
- **p. 4 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** For each new frame captured by the camera, POGS repeats the rendering, feature extraction, loss computation, and optimization steps.
- **p. 4 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** The total loss is a weighted sum of the feature loss and depth loss, guiding the optimization to adjust per-object pose parameters until convergence.
- **p. 2 / Abstract - extractive body cue:** However, NeRF-based representations are limited by NeRF's training speed and implicit spatial representation, making it impossible to update when objects move without further scene-scale optimization.
- **p. 1 / Abstract - extractive body cue:** POGS updates object states without requiring expensive rescanning or prior CAD models of objects.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 3 (Abstract), p. 3 (3) Persistent Object Tracking phase for online tracking), p. 4 (3) Persistent Object Tracking phase for online tracking), p. 4 (3) Persistent Object Tracking phase for online tracking), p. 1 (Abstract), p. 1 (Abstract).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | objects, moved, humans, robots, POGS, update, state, online, allowing, flexible, multi-step, tasks, require, continuous | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | objects, moved, humans, robots, POGS, update, state, online, allowing, flexible | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | makes, following, contributions, Persistent, Object, Gaussian, Splat, POGS, novel, feature | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | operates, through, complementary, mechanisms, attracting, features, belong, same, object, mask | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / Abstract - extractive body cue:** As such objects are moved by humans or robots, POGS can update their state online, allowing for flexible, multi-step tasks that require continuous interaction with ...
- **p. 3 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** To distill 2D object masks into 3D gaussian partitions, we borrow principles from [49, 50] and train a feature embedding encoder Femb that passes an ...
- **p. 4 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** Unlike the object grouping features and language features where we learn embedding functions to map inputs into feature space, the supervision of DINO visual features ...
- **p. 1 / Abstract - extractive body cue:** Traditional and deep RGBD or point cloud object tracking methods are attractive as components of state estimators for robotic manipulation because they do not require ...
- **p. 1 / Abstract - extractive body cue:** 1: Autonomous Object Manipulation and Tracking with POGS Unified Representation (Top) A robot autonomously performs a pick and place primitive to move the shoe onto ...
- **p. 2 / Abstract - extractive body cue:** However, these works focus on offline processing and pose interpolation rather than tracking and estimating object states online for manipulation tasks.
- **p. 4 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** As in LERF, during deployment we use the CLIP text encoder to obtain embedding vectors for arbitrary natural language input queries.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | This includes approximately 140ms latency for DINO feature extraction using a ViT-S, and multiple steps of optimization necessary per frame iteration to ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | However, many of these approaches fail to effectively integrate geometric information across multiple object viewpoints or timesteps, and do not address the ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | This includes approximately 140ms latency for DINO feature extraction using a ViT-S, and multiple steps of optimization necessary per frame iteration to ... | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / Abstract - extractive body cue:** Training images are used to optimize a 3DGS, and features extracted from 2D foundation models are distilled into feature fields, producing our POGS unified representation.
- **p. 1 / Abstract - extractive body cue:** After an initial multi-view scene capture and training phase, POGS uses a single stereo camera to integrate depth estimates along with self-supervised vision encoder features ...
- **p. 1 / Abstract - extractive body cue:** To enable online state estimation, tracking, and manipulation of unseen objects in dynamic environments, we present Persistent Object Gaussian Splat (POGS), an editable objectcentric feature ...
- **p. 2 / Abstract - extractive body cue:** However, NeRF-based representations are limited by NeRF's training speed and implicit spatial representation, making it impossible to update when objects move without further scene-scale optimization.
- **p. 1 / Abstract - extractive body cue:** After an initial multi-view scene capture and training phase, POGS uses a single stereo camera to integrate depth estimates along with self-supervised vision encoder features ...
- **p. 2 / Abstract - extractive body cue:** By embedding features from encoders and detectors pretrained on internet-scale datasets such as CLIP [8], DINO [9], and Detic [10], POGS can respond to open-vocabulary ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Nerfstudio, Splatfacto, implementation, Gaussian, Splatting, gsplat, backend, modify, aforementioned, image, encoders, feature, supervision, losses, features, then, supervised, gaussians, enabling, model.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | As such objects are moved by humans or robots, POGS can update their state online, allowing for flexible, multi-step tasks that require ... | p. 2 (Abstract), p. 2 (Abstract) |
| Semantic / temporal fusion | Similar performance trends were observed in the other tasks, where POGS consistently outperformed ablations that either had depth perception turned off or ... | p. 5 (3) Persistent Object Tracking phase for online tracking), p. 4 (3) Persistent Object Tracking phase for online tracking) |
| Robot query / planning handoff | Tier 1 Tier 2 Perturbations Success Rate Time (s) Success Rate Time (s) Clockwise 24/25 6.30 20/25 12.26 CCW 24/25 5.72 20/25 ... | p. 6 (3) Persistent Object Tracking phase for online tracking), p. 5 (3) Persistent Object Tracking phase for online tracking) |

## Failure and Ablation Link

- **p. 6 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** Jigsaw to Shelf Clothes Iron to Shelf Shoe to Shoerack Tier 1 Tier 2 Tier 1 Tier 2 Tier 1 Tier 2 No Depth No ...
- **p. 2 / Abstract - extractive body cue:** By embedding features from encoders and detectors pretrained on internet-scale datasets such as CLIP [8], DINO [9], and Detic [10], POGS can respond to open-vocabulary ...
- **p. 2 / Abstract - extractive body cue:** In this work, we develop a method capable of updating the scene where a human can also move the objects repeatedly without any partial re-scans ...
- **p. 4 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** Without dimensionality reduction, storing per-Gaussian feature vectors would be computationally prohibitive.
- **p. 4 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** Each Gaussian cluster pose parameter is optimized independently, allowing POGS to track multiple moving objects, without imposing constraints on their relative movements. unlike prior work ...
- **p. 5 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** The ablations highlight the critical role that both depth perception and robust visual features play in achieving accurate object localization and successful sequential object resets.
- **p. 5 / 3) Persistent Object Tracking phase for online tracking - extractive body cue:** Similar performance trends were observed in the other tasks, where POGS consistently outperformed ablations that either had depth perception turned off or were optimized with ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3) Persistent Object Tracking phase for online tracking), p. 4 (3) Persistent Object Tracking phase for online tracking), p. 2 (Abstract), p. 3 (3) Persistent Object Tracking phase for online tracking), p. 1 (Abstract), p. 1 (Abstract), objective p. 3 (3) Persistent Object Tracking phase for online tracking), p. 3 (Abstract), p. 4 (3) Persistent Object Tracking phase for online tracking), p. 4 (3) Persistent Object Tracking phase for online tracking), p. 2 (Abstract), p. 1 (Abstract), temporal p. 6 (3) Persistent Object Tracking phase for online tracking), p. 1 (Abstract), p. 2 (Abstract), p. 4 (3) Persistent Object Tracking phase for online tracking), p. 4 (3) Persistent Object Tracking phase for online tracking), p. 6 (3) Persistent Object Tracking phase for online tracking).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
