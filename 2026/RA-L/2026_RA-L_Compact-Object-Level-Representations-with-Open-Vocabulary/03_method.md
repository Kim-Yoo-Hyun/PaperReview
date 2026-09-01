# Method - Compact Object-Level Representations with Open-Vocabulary Understanding for Indoor Visual Relocalization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2606.24767; PDF retrieval source: https://arxiv.org/pdf/2606.24767. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (III. METHOD), p. 5 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD), p. 5 (III. METHOD)): In this section, we introduce an object-oriented mapping workflow and the principles behind each module.

## Method Body Digest

- **p. 3 / III. METHOD - extractive PDF cue:** In this section, we introduce an object-oriented mapping workflow and the principles behind each module.
- **p. 5 / III. METHOD - extractive PDF cue:** To ensure more robust and accurate pose estimation, we use a Huber kernel H with a threshold δ on the 2D ICP loss to suppress ...
- **p. 3 / III. METHOD - extractive PDF cue:** Object-oriented Mapping (Sec III-A): Given a set of posed RGBD images from a scene, this step is to process these RGBD observations and build an ...
- **p. 4 / III. METHOD - extractive PDF cue:** Recent progress suggested that the advanced CLIP model can work as an effective object descriptor encoder [7].
- **p. 4 / III. METHOD - extractive PDF cue:** Top-k patches with maximal visibility are input into a CLIP visual encoder and an average pooling layer to obtain a multiview CLIP feature f 3d: ...
- **p. 5 / III. METHOD - extractive PDF cue:** Benefiting from this loss, we can achieve stable pose optimization.
- **p. 4 / III. METHOD - extractive PDF cue:** Our object-level tracker improves relocalization performance relying on a coarse-to-fine strategy and a novel loss.
- **p. 4 / III. METHOD - extractive PDF cue:** The goal is to solve an optimal assignment from Gq to Gl so that the total matching score is maximized, as shown in Fig.

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive PDF cue:** Overall, our contributions can be summarized as follows: • We introduce a multi-modal landmark association module that combines open-vocabulary object descriptors with a global scene ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** We construct an objectoriented map suite that consists of a global scene graph, openvocabulary object descriptors, object geometry, and reference frames.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** In response to these challenges, we propose OpenReLoc, a semantic-aware, memory-efficient, and scalable camera relocalization framework based on object-level representations with open-vocabulary understanding.

## Source Evidence Cues

- **p. 3 / III. METHOD - extractive PDF cue:** In this section, we introduce an object-oriented mapping workflow and the principles behind each module.
- **p. 5 / III. METHOD - extractive PDF cue:** To ensure more robust and accurate pose estimation, we use a Huber kernel H with a threshold δ on the 2D ICP loss to suppress ...
- **p. 3 / III. METHOD - extractive PDF cue:** Object-oriented Mapping (Sec III-A): Given a set of posed RGBD images from a scene, this step is to process these RGBD observations and build an ...
- **p. 4 / III. METHOD - extractive PDF cue:** Recent progress suggested that the advanced CLIP model can work as an effective object descriptor encoder [7].
- **p. 4 / III. METHOD - extractive PDF cue:** Top-k patches with maximal visibility are input into a CLIP visual encoder and an average pooling layer to obtain a multiview CLIP feature f 3d: ...
- **p. 5 / III. METHOD - extractive PDF cue:** Benefiting from this loss, we can achieve stable pose optimization.
- **Detected method headings:** III. METHOD (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | In this section, we introduce an object-oriented mapping workflow and the principles behind each module. | p. 3 (III. METHOD), p. 5 (III. METHOD) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | To ensure more robust and accurate pose estimation, we use a Huber kernel H with a threshold δ on the 2D ICP ... | p. 5 (III. METHOD), p. 3 (III. METHOD) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Object-oriented Mapping (Sec III-A): Given a set of posed RGBD images from a scene, this step is to process these RGBD observations ... | p. 3 (III. METHOD), p. 4 (III. METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / III. METHOD - extractive PDF cue:** Benefiting from this loss, we can achieve stable pose optimization.
- **p. 4 / III. METHOD - extractive PDF cue:** Our object-level tracker improves relocalization performance relying on a coarse-to-fine strategy and a novel loss.
- **p. 4 / III. METHOD - extractive PDF cue:** The goal is to solve an optimal assignment from Gq to Gl so that the total matching score is maximized, as shown in Fig.
- **p. 5 / III. METHOD - extractive PDF cue:** To ensure more robust and accurate pose estimation, we use a Huber kernel H with a threshold δ on the 2D ICP loss to suppress ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (III. METHOD), p. 5 (III. METHOD), p. 5 (III. METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Object-oriented, Mapping, Sec, III-A, Given, posed, RGBD, images, scene, step, process, observations, build, object-centric | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Object-oriented, Mapping, Sec, III-A, Given, posed, RGBD, images, scene, step | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | Overall, contributions, summarized, follows, introduce, multi-modal, landmark, association, module, combines | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Benefiting, loss, achieve, stable, pose, optimization, object-level, tracker, improves, relocalization | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / III. METHOD - extractive PDF cue:** Object-oriented Mapping (Sec III-A): Given a set of posed RGBD images from a scene, this step is to process these RGBD observations and build an ...
- **p. 3 / III. METHOD - extractive PDF cue:** Based on depth observations, we can reconstruct the scene mesh by TSDF-Fusion [20] and convert vertices into the scene point cloud P.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** The goal is to estimate the 6-DOF camera pose given a visual observation in a known map.
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** ACCEPTED JUNE 2026 2 Input Multi-floor Scene Object-level Mapping and Matching Pose Estimation Third floor Second floor First floor Query Image Fig.
- **p. 4 / III. METHOD - extractive PDF cue:** Top-k patches with maximal visibility are input into a CLIP visual encoder and an average pooling layer to obtain a multiview CLIP feature f 3d: ...
- **p. 5 / III. METHOD - extractive PDF cue:** Li forward = 1 Npi X n∈pi H(//pn i -ψ(pn i , mi)//2, δ) , (7a) Li backward = 1 Nmi X n∈mi H(//mn i ...
- **p. 4 / III. METHOD - extractive PDF cue:** We project point clouds Pi on the image plane to find patches S of the same landmark in different views.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Notably, in our system, GPT analysis is a major efficiency bottleneck, accounting for about 80% of the per-frame runtime due to the ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Object-oriented Mapping Object-oriented mapping is the first and pivotal step in our framework, where a well-structured map suite and highquality reconstruction form ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | In response to these challenges, we propose OpenReLoc, a semantic-aware, memory-efficient, and scalable camera relocalization framework based on object-level representations with open-vocabulary ... | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | We run our system on a desktop equipped with an NVIDIA RTX 4090 GPU. | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** section, introduce, object-oriented, mapping, workflow, principles, behind, module, ensure, more, robust, accurate, pose, estimation, Huber, kernel, threshold, ICP, loss, suppress.
- **Relevant PDF headings:** III. METHOD (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Experiments on these two datasets illustrate the capability of our system in handling complex real-world scenes, boosting the practicality of object-level camera ... | p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Semantic / temporal fusion | Therefore, our main comparison is to GoReloc [6], an open-source and SOTA object-level baseline, which shares the most relevant problem formulation with ... | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Robot query / planning handoff | V, it can be seen that our method can still outperform GoReloc in both success rate and accuracy. | p. 6 (IV. EXPERIMENTS), p. 7 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** They contain rich object categories and diverse scenes without temporal changes, but only provide sequential frames with high visual overlap.
- **p. 7 / 3.5 MB - extractive PDF cue:** Ablation Study To verify the rationality of our main module designs, we conduct ablation studies on different datasets in Tab.
- **p. 7 / 3.5 MB - extractive PDF cue:** Removing either stage inevitably degrades performance, highlighting contributions and complementary roles of these two stages.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 6: Open-vocabulary Object Matching. Open-vocabulary object-level mapping allows us to recognize diverse objects. methods achieve comparable efficiency. The relocalization module typically serves as an ...
- **p. 7 / IV. EXPERIMENTS - extractive PDF cue:** Such a distribution falls beyond the scope of closed-vocabulary methods, leading to their failure.
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** IV show that ORB-SLAM2 experienced failure, succeeding on very few frames, despite achieving better accuracy.
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** As a result, GoReloc fails to identify valid matching objects in many observations.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (III. METHOD), p. 5 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD), p. 5 (III. METHOD), objective p. 5 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD), p. 5 (III. METHOD), temporal p. 7 (IV. EXPERIMENTS), p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 5 (IV. EXPERIMENTS), p. 1 (I. INTRODUCTION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
