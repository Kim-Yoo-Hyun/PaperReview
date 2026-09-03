# Method - CoE: Deep Coupled Embedding for Non-Rigid Point Cloud Correspondences

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/; PDF retrieval source: https://openreview.net/attachment?id=pIDl4wuZoG&name=pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (4.1. Network Architecture), p. 5 (4.1. Network Architecture), p. 5 (4.2. Unsupervised Loss), p. 4 (4.1. Network Architecture), p. 6 (4.2. Unsupervised Loss)): Our network architecture is simple, efficient and comprises two main building blocks: an embedding extractor fθ and a cross attention module hφ with learnable parameters θ and φ, which we ...

## Method Body Digest

- **p. 4 / 4.1. Network Architecture - extractive body cue:** Our network architecture is simple, efficient and comprises two main building blocks: an embedding extractor fθ and a cross attention module hφ with learnable parameters ...
- **p. 5 / 4.1. Network Architecture - extractive body cue:** It follows the Transformer architecture [51] and learns a non-linear mapping: hφ : { ˆΨS, ˆΨT } →{ΨS, ΨT } (3) The output ΨS and ...
- **p. 5 / 4.2. Unsupervised Loss - extractive body cue:** Our unsupervised loss is inspired by the work of classical geometry processing [16, 22] and consists of three terms.
- **p. 4 / 4.1. Network Architecture - extractive body cue:** Embedding Extractor Module computes per point intermediate embedding ˆΨ(·), which is a non-linear mapping:
- **p. 6 / 4.2. Unsupervised Loss - extractive body cue:** Finally, our full unsupervised loss is written as: Ltotal = µoffLoff + µoLo + µcLc (7) where µoff = 1, µo = 5e1 and µc ...
- **p. 5 / 4.2. Unsupervised Loss - extractive body cue:** Orthogonal Loss: The orthogonal constraint in Eq.
- **p. 5 / 4.2. Unsupervised Loss - extractive body cue:** Off-diagonal Loss: Similar as in Eq.
- **p. 6 / 4.2. Unsupervised Loss - extractive body cue:** All methods only take point clouds as input except the multimodal method SSMSM [7], which requires meshes.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are: • We propose a novel unsupervised way to learn per-point embeddings directly from raw point clouds under various non-rigid deformations.
- **p. 2 / 1. Introduction - extractive body cue:** Inspired by classical geometry processing technique, our method is effective and simple that only requires to train a single network. • In our learned embedding ...
- **p. 4 / 3. Background and Notation - extractive body cue:** To overcome these issues, we propose to directly learn coupled embeddings without any ground truth correspondences and without any subspace parameterisation.

## Source Evidence Cues

- **p. 4 / 4.1. Network Architecture - extractive body cue:** Our network architecture is simple, efficient and comprises two main building blocks: an embedding extractor fθ and a cross attention module hφ with learnable parameters ...
- **p. 5 / 4.1. Network Architecture - extractive body cue:** It follows the Transformer architecture [51] and learns a non-linear mapping: hφ : { ˆΨS, ˆΨT } →{ΨS, ΨT } (3) The output ΨS and ...
- **p. 5 / 4.2. Unsupervised Loss - extractive body cue:** Our unsupervised loss is inspired by the work of classical geometry processing [16, 22] and consists of three terms.
- **p. 4 / 4.1. Network Architecture - extractive body cue:** Embedding Extractor Module computes per point intermediate embedding ˆΨ(·), which is a non-linear mapping:
- **p. 6 / 4.2. Unsupervised Loss - extractive body cue:** Finally, our full unsupervised loss is written as: Ltotal = µoffLoff + µoLo + µcLc (7) where µoff = 1, µo = 5e1 and µc ...
- **Detected method headings:** 4.1. Network Architecture (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Our network architecture is simple, efficient and comprises two main building blocks: an embedding extractor fθ and a cross attention module hφ ... | p. 4 (4.1. Network Architecture), p. 5 (4.1. Network Architecture) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | It follows the Transformer architecture [51] and learns a non-linear mapping: hφ : { ˆΨS, ˆΨT } →{ΨS, ΨT } (3) The ... | p. 5 (4.1. Network Architecture), p. 5 (4.2. Unsupervised Loss) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Our unsupervised loss is inspired by the work of classical geometry processing [16, 22] and consists of three terms. | p. 5 (4.2. Unsupervised Loss), p. 4 (4.1. Network Architecture) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 4.2. Unsupervised Loss - extractive body cue:** Orthogonal Loss: The orthogonal constraint in Eq.
- **p. 5 / 4.2. Unsupervised Loss - extractive body cue:** Off-diagonal Loss: Similar as in Eq.
- **p. 6 / 4.2. Unsupervised Loss - extractive body cue:** Finally, our full unsupervised loss is written as: Ltotal = µoffLoff + µoLo + µcLc (7) where µoff = 1, µo = 5e1 and µc ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (4.2. Unsupervised Loss), p. 5 (4.2. Unsupervised Loss), p. 6 (4.2. Unsupervised Loss).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | methods, only, take, point, clouds, input, except, multimodal, SSMSM, requires, meshes, Due, insights, gained | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | methods, only, take, point, clouds, input, except, multimodal, SSMSM, requires | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | summary, contributions, novel, unsupervised, learn, per-point, embeddings, directly, point, clouds | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Orthogonal, Loss, constraint, Off-diagonal, Similar, Finally, full, unsupervised, written, Ltotal | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 6 / 4.2. Unsupervised Loss - extractive body cue:** All methods only take point clouds as input except the multimodal method SSMSM [7], which requires meshes.
- **p. 2 / 1. Introduction - extractive body cue:** Due to insights gained from the classical geometry processing, we can obtain high-quality dense correspondences directly via a simple proximity search in the embedding space ...
- **p. 2 / 1. Introduction - extractive body cue:** Inspired by classical geometry processing technique, our method is effective and simple that only requires to train a single network. • In our learned embedding ...
- **p. 1 / 1. Introduction - extractive body cue:** However, with the proliferation of low-cost sensors, the interest in methods that can directly deal with raw point clouds is expanding rapidly.
- **p. 3 / 3. Background and Notation - extractive body cue:** In this section, we briefly review coupled diagonalisation for a pair of input shapes and introduce our notations (Tab.
- **p. 5 / 4.1. Network Architecture - extractive body cue:** It follows the Transformer architecture [51] and learns a non-linear mapping: hφ : { ˆΨS, ˆΨT } →{ΨS, ΨT } (3) The output ΨS and ...
- **p. 5 / 4.1. Network Architecture - extractive body cue:** The core concept of cross attention is that it computes a similarity matrix between the key and query (transformed version of ˆΨS, ˆΨT ), and ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | It captures the local geometric information of different scales on the manifold by modelling a heat diffusion process with different timesteps and ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | DiffFmaps [28] proposes to learn a linearly invariant embedding from point clouds, which serves as a replacement for the pre-computed LBO eigenbasis ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 4.1. Network Architecture - extractive body cue:** It captures the local geometric information of different scales on the manifold by modelling a heat diffusion process with different timesteps and constrains the learned ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** network, architecture, simple, efficient, comprises, main, building, blocks, embedding, extractor, cross, attention, module, learnable, parameters, will, elaborate, next, follows, Transformer.
- **Relevant PDF headings:** 4.1. Network Architecture (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Datasets We employ the recent non-isometric benchmark DT4D-M [27] as the testbed for this task. | p. 7 (5.3. Non-isometric Shape Matching), p. 7 (5.2. Near-isometric Shape Matching) |
| Semantic / temporal fusion | Our method outperforms all learning based baselines. | p. 7 (5.3. Non-isometric Shape Matching), p. 7 (5.4. Generalisation) |
| Robot query / planning handoff | Extensive experiments showcase that our proposed method achieves superior results in a number of non-rigid matching benchmarks and is promising in other ... | p. 8 (5.7. Shape Segmentation), p. 7 (5.3. Non-isometric Shape Matching) |

## Failure and Ablation Link

- **p. 7 / 5.2. Near-isometric Shape Matching - extractive body cue:** Please refer to the supplementary for qualitative results and additional ablation experiments.
- **p. 8 / 5.7. Shape Segmentation - extractive body cue:** An interesting direction is to incorporate the advancement in SO(3)/SE(3) invariant architecture [12] to eliminate the necessity of pre-alignment.
- **p. 11 / Figure/Table caption - extractive body cue:** Table 4. Ablation study of our loss and pipeline. Each loss term and network component contributes to reduce matching errors. Finally, the eigenvalues Λ and ...
- **p. 7 / 5.2. Near-isometric Shape Matching - extractive body cue:** As an ablative study we disable the ASAP component hence employ the vanilla DiffusionNet as feature extractor and report its quantitative results in Tab.
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 16. Qualitative results on DT4D-M. More qualitative non-isometric matching results (top) . Failure cases mainly due to challenging topological noise (bottom) .
- **p. 8 / 5.7. Shape Segmentation - extractive body cue:** Limitations, Future Work and Conclusion In this paper, we proposed an unsupervised method to learn high-quality, well-generalised embeddings directly from raw point clouds.
- **p. 14 / Figure/Table caption - extractive body cue:** Figure 13. Failure cases on FAUST. All three failure examples relate to the touching hands, where the points of two hands are locally mixed and ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (4.1. Network Architecture), p. 5 (4.1. Network Architecture), p. 5 (4.2. Unsupervised Loss), p. 4 (4.1. Network Architecture), p. 6 (4.2. Unsupervised Loss), objective p. 5 (4.2. Unsupervised Loss), p. 5 (4.2. Unsupervised Loss), p. 6 (4.2. Unsupervised Loss), temporal p. 5 (4.1. Network Architecture), p. 2 (2.1. Pose Invariant Shape Representation), p. 3 (3. Background and Notation), p. 5 (4.1. Network Architecture).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
