# Method - GeoPurify: A Data-Efficient Geometric Distillation Framework for Open-Vocabulary 3D Segmentation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=mN49LupE8l; PDF retrieval source: https://openreview.net/pdf/57fa2e7334b7e5972b3c62c83d3aecf630a1f0e3.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (3 METHODOLOGY), p. 3 (3 METHODOLOGY), p. 4 (3 METHODOLOGY), p. 4 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 5 (3 METHODOLOGY)): 3.1 OVERALL ARCHITECTURE As illustrated in Figure 2, our proposed GeoPurify first leverages a frozen Vision-Language Model (Ψ2D) to transfer and merge multi-view RGB images into an initial 3D feature ...

## Method Body Digest

- **p. 3 / 3 METHODOLOGY - extractive PDF cue:** 3.1 OVERALL ARCHITECTURE As illustrated in Figure 2, our proposed GeoPurify first leverages a frozen Vision-Language Model (Ψ2D) to transfer and merge multi-view RGB images ...
- **p. 3 / 3 METHODOLOGY - extractive PDF cue:** To address this, we introduce a 3D student affinity network ϕS that learns geometric affinities from the point cloud using a self-supervised 3D geometric model ...
- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** 3.3 GEOMETRIC CONTRASTIVE DISTILLATION To rectify the geometric inconsistencies within the initial semantic features Fsem, we introduce a contrastive purification module trained via knowledge distillation.
- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** The pre-trained student network then applies a geometry-aware pooling, using its learned affinities to refine the initial features.
- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** We then curate a set of hard negatives comprising two distinct types: macronegatives, which are the points globally most dissimilar to pa in the feature ...
- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** The student network, ϕS, which maps the point cloud P to a set of geometric embeddings Ggeo ∈RN×Dgeo, is then optimized to organize its embedding ...
- **p. 3 / 3 METHODOLOGY - extractive PDF cue:** Specifically, ϕS learns to recover the latent geometric structure embedded in Fsem and approximate the teacher's geometric representation by minimizing an InfoNCE contrastive loss over ...
- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** By optimizing this objective, ϕS learns to encode the intrinsic geometric structure of the scene, producing a representation capable of enforcing structural coherence upon the ...

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** In summary, our contributions are: • We introduce GeoPurify, a data-efficient framework built on the hypothesis that beyond their semantic richness, VLM-projected features also embed ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Motivated by this hypothesis, we present GeoPurify, a data-efficient framework designed to recover latent geometric structure from noisy semantic features and produce robust 3D representations.
- **p. 3 / 3 METHODOLOGY - extractive PDF cue:** To address this, we introduce a 3D student affinity network ϕS that learns geometric affinities from the point cloud using a self-supervised 3D geometric model ...

## Source Evidence Cues

- **p. 3 / 3 METHODOLOGY - extractive PDF cue:** 3.1 OVERALL ARCHITECTURE As illustrated in Figure 2, our proposed GeoPurify first leverages a frozen Vision-Language Model (Ψ2D) to transfer and merge multi-view RGB images ...
- **p. 3 / 3 METHODOLOGY - extractive PDF cue:** To address this, we introduce a 3D student affinity network ϕS that learns geometric affinities from the point cloud using a self-supervised 3D geometric model ...
- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** 3.3 GEOMETRIC CONTRASTIVE DISTILLATION To rectify the geometric inconsistencies within the initial semantic features Fsem, we introduce a contrastive purification module trained via knowledge distillation.
- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** The pre-trained student network then applies a geometry-aware pooling, using its learned affinities to refine the initial features.
- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** We then curate a set of hard negatives comprising two distinct types: macronegatives, which are the points globally most dissimilar to pa in the feature ...
- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** The student network, ϕS, which maps the point cloud P to a set of geometric embeddings Ggeo ∈RN×Dgeo, is then optimized to organize its embedding ...
- **Detected method headings:** 3 METHODOLOGY (p. 3); A.1 NETWORK ARCHITECTURES (p. 14)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | 3.1 OVERALL ARCHITECTURE As illustrated in Figure 2, our proposed GeoPurify first leverages a frozen Vision-Language Model (Ψ2D) to transfer and merge ... | p. 3 (3 METHODOLOGY), p. 3 (3 METHODOLOGY) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | To address this, we introduce a 3D student affinity network ϕS that learns geometric affinities from the point cloud using a self-supervised ... | p. 3 (3 METHODOLOGY), p. 4 (3 METHODOLOGY) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | 3.3 GEOMETRIC CONTRASTIVE DISTILLATION To rectify the geometric inconsistencies within the initial semantic features Fsem, we introduce a contrastive purification module trained ... | p. 4 (3 METHODOLOGY), p. 4 (3 METHODOLOGY) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** The student network, ϕS, which maps the point cloud P to a set of geometric embeddings Ggeo ∈RN×Dgeo, is then optimized to organize its embedding ...
- **p. 3 / 3 METHODOLOGY - extractive PDF cue:** Specifically, ϕS learns to recover the latent geometric structure embedded in Fsem and approximate the teacher's geometric representation by minimizing an InfoNCE contrastive loss over ...
- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** By optimizing this objective, ϕS learns to encode the intrinsic geometric structure of the scene, producing a representation capable of enforcing structural coherence upon the ...
- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** The resulting feature space is inherently generative and associative, optimized to answer the holistic question: What is depicted, where is it located, and how can ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 3 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 5 (3 METHODOLOGY).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | OVERALL, ARCHITECTURE, illustrated, Figure, GeoPurify, first, leverages, frozen, Vision-Language, Model, transfer, merge, multi-view, RGB | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | OVERALL, ARCHITECTURE, illustrated, Figure, GeoPurify, first, leverages, frozen, Vision-Language, Model | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | summary, contributions, introduce, GeoPurify, data-efficient, framework, built, hypothesis, beyond, semantic | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | student, network, maps, point, cloud, geometric, embeddings, Ggeo, Dgeo, then | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3 METHODOLOGY - extractive PDF cue:** 3.1 OVERALL ARCHITECTURE As illustrated in Figure 2, our proposed GeoPurify first leverages a frozen Vision-Language Model (Ψ2D) to transfer and merge multi-view RGB images ...
- **p. 3 / 3 METHODOLOGY - extractive PDF cue:** 3.2 SEMANTIC INITIALIZATION FROM A GENERALIST VLM To obtain 3D representations enriched with semantic priors, we project RGB inputs into the 3D point space (constructed ...
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** Training-free methods directly exploit 2D VLMs for segmentation, projecting multi-view 2D predictions onto 3D point clouds, and merging them to obtain final outputs.
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** As a result, current approaches are constrained by an unfavorable tradeoff: either accept noisy and fragmented outputs from training-free projection or incur the heavy data ...
- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** Follow this pipeline, to produce a 3D point cloud P = {pi}N i=1 with its corresponding multi-view images {Iv}V v=1, we first compute dense feature ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Experiments on multiple popular 3D semantic segmentation datasets demonstrate that GeoPurify achieves comparable or superior performance to state-of-the-art methods while using only ∼1.5% of the ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** It then introduces a Geometric Contrastive Distillation mechanism to learn latent geometric affinities from unlabeled 3D scans and a GeometryGuided Pooling module that uses these ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | OpenSeg (Ghiasi et al., 2022), and SAM+CLIP frameworks (Wang et al., 2024a), which adopt a Localize then Recognize pipeline. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Initializing with the voxel-aggregated semantic features F (0), we update the features for T steps: F (t+1) = AF (t) (4) Finally, ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | The student network is trained for 50 epochs using the AdamW optimizer with a learning rate of 1 × 10-3, which is ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** 3.3 GEOMETRIC CONTRASTIVE DISTILLATION To rectify the geometric inconsistencies within the initial semantic features Fsem, we introduce a contrastive purification module trained via knowledge distillation.
- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** The pre-trained student network then applies a geometry-aware pooling, using its learned affinities to refine the initial features.
- **p. 6 / 4 EXPERIMENTS - extractive PDF cue:** The student network is trained for 50 epochs using the AdamW optimizer with a learning rate of 1 × 10-3, which is decayed using a ...
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** During inference, the Geometry-Guided Pooling leverages this unbiased structural knowledge to propagate the VLM's semantic seeds across entire geometrically coherent instances.
- **p. 14 / A EXPERIMENTAL SETUP AND IMPLEMENTATION DETAILS - extractive PDF cue:** Our code and pre-trained models will be made publicly available upon publication.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** OVERALL, ARCHITECTURE, illustrated, Figure, GeoPurify, first, leverages, frozen, Vision-Language, Model, transfer, merge, multi-view, RGB, images, initial, feature, Fsem, Dsem, address.
- **Relevant PDF headings:** 3 METHODOLOGY (p. 3); A.1 NETWORK ARCHITECTURES (p. 14).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Published as a conference paper at ICLR 2026 2017), a large-scale dataset of over 1,500 RGB-D scans from diverse indoor environments, and ... | p. 6 (4 EXPERIMENTS), p. 15 (A.2 DATASET DETAILS AND SUBSET SELECTION) |
| Semantic / temporal fusion | Our data-efficient GeoPurify is compared against other zero-shot baselines. | p. 8 (4 EXPERIMENTS), p. 20 (Figure/Table caption) |
| Robot query / planning handoff | The efficacy of these features is demonstrated on the ScanNet benchmark, where they achieve 72.5% mIoU with linear probing, substantially outperforming 2D-lifted ... | p. 14 (A.1 NETWORK ARCHITECTURES), p. 8 (4 EXPERIMENTS) |

## Failure and Ablation Link

- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** Models are trained on the source dataset and evaluated directly on the target without fine-tuning.
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** Method ScanNetV2 →Matterport3D Matterport3D →ScanNetV2 mIoU (%) mAcc (%) mIoU (%) mAcc (%) OpenScene (Peng et al., 2023) 36.0 48.0 36.5 44.0 CUA-O3D (Li et ...
- **p. 6 / 4 EXPERIMENTS - extractive PDF cue:** Once this compact subset is selected, the subsequent distillation training is performed without using any 3D semantic labels, relying only on the raw point cloud ...
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** Standard methods typically attempt to learn entangled geo-semantic representations from scratch, failing to generalize without sufficient data.
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** Published as a conference paper at ICLR 2026 subset (∼1.5%), GeoPurify achieves competitive, and in some cases state-of-the-art, performance without requiring large-scale 3D semantic annotations.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** A variant trained using only macro-negatives results in a 1.6 mIoU performance drop to 53.5 mIoU.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** Without them, the model learns the global scene layout but fails to disentangle co-located surfaces.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (3 METHODOLOGY), p. 3 (3 METHODOLOGY), p. 4 (3 METHODOLOGY), p. 4 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), objective p. 5 (3 METHODOLOGY), p. 3 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 4 (3 METHODOLOGY), temporal p. 4 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
