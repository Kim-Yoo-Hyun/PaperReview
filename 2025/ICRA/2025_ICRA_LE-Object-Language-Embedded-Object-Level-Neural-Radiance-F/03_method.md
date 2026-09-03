# Method - LE-Object: Language Embedded Object-Level Neural Radiance Fields for Open-Vocabulary Scene

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.proceedings.com/content/081/081087webtoc.pdf; PDF retrieval source: https://arxiv.org/pdf/2406.08009v1. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (III. OPENOBJ), p. 5 (III. OPENOBJ), p. 2 (I. INTRODUCTION), p. 3 (III. OPENOBJ), p. 4 (III. OPENOBJ), p. 4 (III. OPENOBJ)): In this paper, we use the visual encoder of CLIP [4] to encode images cropped according to the mask mobj t,i as VLM feature f clip t,i .

## Method Body Digest

- **p. 3 / III. OPENOBJ - extractive body cue:** In this paper, we use the visual encoder of CLIP [4] to encode images cropped according to the mask mobj t,i as VLM feature f ...
- **p. 5 / III. OPENOBJ - extractive body cue:** Next, we superimpose the features of these masks mpart t,j and perform normalization: If t = P j  mpart t,j · f clip t,j ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, Our contributions are summarized as follows: • We present OpenObj, the open-vocabulary object-level neural radiance fields with fine-grained understanding, supporting downstream tasks at ...
- **p. 3 / III. OPENOBJ - extractive body cue:** Specifically, we use the bounding boxes of the masks mobj t,i as prompts and use the TAP (Tokenize Anything via Prompting) model [29] to generate ...
- **p. 4 / III. OPENOBJ - extractive body cue:** Part-level Fine-Grained Feature Extraction Both of the above modules operate at the instance level and do not perceive the interior details of the object.
- **p. 4 / III. OPENOBJ - extractive body cue:** To address this, the Part-level Fine-Grained Feature Extraction module is designed to generate dense feature images, which represent a refined, part-level understanding of the object.
- **p. 5 / III. OPENOBJ - extractive body cue:** NeRF Rendering and Training In OpenObj, each object is modeled as a NeRF network with a uniform structure, enabling multi-model vectorized training similar to [27].
- **p. 5 / III. OPENOBJ - extractive body cue:** (6d) The overall loss function is obtained by summing the losses of all objects: L = X k (λ1Lk occ + λ2Lk depth + λ3Lk ...

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, Our contributions are summarized as follows: • We present OpenObj, the open-vocabulary object-level neural radiance fields with fine-grained understanding, supporting downstream tasks at ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Following this inspiration, we proposed OpenObj, an innovative approach to build open-vocabulary objectlevel neural radiance fields with fine-grained understanding.
- **p. 1 / Abstract - extractive body cue:** To address these challenges, we introduce OpenObj, an innovative approach to build openvocabulary object-level Neural Radiance Fields (NeRF) with fine-grained understanding.

## Source Evidence Cues

- **p. 3 / III. OPENOBJ - extractive body cue:** In this paper, we use the visual encoder of CLIP [4] to encode images cropped according to the mask mobj t,i as VLM feature f ...
- **p. 5 / III. OPENOBJ - extractive body cue:** Next, we superimpose the features of these masks mpart t,j and perform normalization: If t = P j  mpart t,j · f clip t,j ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, Our contributions are summarized as follows: • We present OpenObj, the open-vocabulary object-level neural radiance fields with fine-grained understanding, supporting downstream tasks at ...
- **p. 3 / III. OPENOBJ - extractive body cue:** Specifically, we use the bounding boxes of the masks mobj t,i as prompts and use the TAP (Tokenize Anything via Prompting) model [29] to generate ...
- **p. 4 / III. OPENOBJ - extractive body cue:** Part-level Fine-Grained Feature Extraction Both of the above modules operate at the instance level and do not perceive the interior details of the object.
- **p. 4 / III. OPENOBJ - extractive body cue:** To address this, the Part-level Fine-Grained Feature Extraction module is designed to generate dense feature images, which represent a refined, part-level understanding of the object.
- **p. 5 / III. OPENOBJ - extractive body cue:** NeRF Rendering and Training In OpenObj, each object is modeled as a NeRF network with a uniform structure, enabling multi-model vectorized training similar to [27].
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | In this paper, we use the visual encoder of CLIP [4] to encode images cropped according to the mask mobj t,i as ... | p. 3 (III. OPENOBJ), p. 5 (III. OPENOBJ) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Next, we superimpose the features of these masks mpart t,j and perform normalization: If t = P j  mpart t,j · ... | p. 5 (III. OPENOBJ), p. 2 (I. INTRODUCTION) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | In summary, Our contributions are summarized as follows: • We present OpenObj, the open-vocabulary object-level neural radiance fields with fine-grained understanding, supporting ... | p. 2 (I. INTRODUCTION), p. 3 (III. OPENOBJ) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / III. OPENOBJ - extractive body cue:** (6d) The overall loss function is obtained by summing the losses of all objects: L = X k (λ1Lk occ + λ2Lk depth + λ3Lk ...
- **p. 5 / III. OPENOBJ - extractive body cue:** Based on this, we can render the occupancy, depth, color, and feature as: ˆO(r[u,v]) = X m Tm, ˆD(r[u,v]) = X m Tmdm ˆC(r[u,v]) = ...
- **p. 3 / III. OPENOBJ - extractive body cue:** Given the strong advantages of LLMs in natural language processing tasks, we encode these captions using LLMs to obtain their caption features f cap t,i ...
- **p. 3 / III. OPENOBJ - extractive body cue:** The backbone of NeRF is a small MLP (Multilayer Perceptron) that takes 3D point coordinates x, y, z, and outputs color c, occupancy probability σ, ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (III. OPENOBJ), p. 5 (III. OPENOBJ).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | render, occupancy, depth, color, feature, Tmdm, Tmcm, Tmfm, Loss, Function, Supervised, training, conducted, input | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | render, occupancy, depth, color, feature, Tmdm, Tmcm, Tmfm, Loss, Function | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | summary, contributions, summarized, follows, present, OpenObj, open-vocabulary, object-level, neural, radiance | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | overall, loss, function, obtained, summing, losses, objects, depth, color, feat | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / III. OPENOBJ - extractive body cue:** Based on this, we can render the occupancy, depth, color, and feature as: ˆO(r[u,v]) = X m Tm, ˆD(r[u,v]) = X m Tmdm ˆC(r[u,v]) = ...
- **p. 3 / III. OPENOBJ - extractive body cue:** Framework Overview OpenObj processes a series of multi-view color images I = {Ic 1, Ic 2, ..., Ic t } and depth images I = ...
- **p. 3 / III. OPENOBJ - extractive body cue:** Finally, the NeRF Rendering and Training module vectorizes the training of NeRFs for all objects based on the masks, input RGBD images, and dense VLM ...
- **p. 4 / III. OPENOBJ - extractive body cue:** Taking the color images Ic t as input, SAM segments all the dense masks {mpart t,j / j = 1, 2, . . . , ...
- **p. 4 / III. OPENOBJ - extractive body cue:** To address this, the Part-level Fine-Grained Feature Extraction module is designed to generate dense feature images, which represent a refined, part-level understanding of the object.
- **p. 5 / III. OPENOBJ - extractive body cue:** Next, we superimpose the features of these masks mpart t,j and perform normalization: If t = P j  mpart t,j · f clip t,j ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** These maps facilitate human interaction and support higher-level cognitive navigation, e.g., ‘Please find a soft piece of furniture.' or ‘Please find me a place to ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | 2: The framework of OpenObj consists of four main modules: Object Segmentation and Understanding, Mask Clustering, Part-level Fine-Grained Feature Extraction, and Hierarchical ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | In essence, OpenObj establishes a robust framework for efficient and watertight scene modeling and comprehension at the object-level. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | 2: The framework of OpenObj consists of four main modules: Object Segmentation and Understanding, Mask Clustering, Part-level Fine-Grained Feature Extraction, and Hierarchical ... | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / III. OPENOBJ - extractive body cue:** Next, we superimpose the features of these masks mpart t,j and perform normalization: If t = P j  mpart t,j · f clip t,j ...
- **p. 5 / III. OPENOBJ - extractive body cue:** NeRF Rendering and Training In OpenObj, each object is modeled as a NeRF network with a uniform structure, enabling multi-model vectorized training similar to [27].

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** visual, encoder, CLIP, encode, images, cropped, according, mask, mobj, VLM, feature, Next, superimpose, features, masks, mpart, perform, normalization, manner, generate.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Datasets and Metrics: The experiments are conducted on four scenes in Replica [32], each featuring a diverse array of objects. | p. 7 (2) Are OpenObj's open-vocabulary object-level and part), p. 6 (2) Are OpenObj's open-vocabulary object-level and part) |
| Semantic / temporal fusion | 2D & 3D Zero-shot Semantic Segmentation Baseline: For 2D semantic segmentation, we compare OpenObj with the language-driven image segmentation method LSeg [31], ... | p. 6 (2) Are OpenObj's open-vocabulary object-level and part), p. 6 (2) Are OpenObj's open-vocabulary object-level and part) |
| Robot query / planning handoff | In this section, we aim to use experiments to validate OpenObj, through the following specific questions: 1) Without fine-tuning any model, can ... | p. 5 (IV. EXPERIMENTAL RESULTS), p. 6 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 5 / IV. EXPERIMENTAL RESULTS - extractive body cue:** In this section, we aim to use experiments to validate OpenObj, through the following specific questions: 1) Without fine-tuning any model, can OpenObj achieve 2D ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: The framework of OpenObj consists of four main modules: Object Segmentation and Understanding, Mask Clustering, Part-level Fine-Grained Feature Extraction, and Hierarchical Graph Representation ...
- **p. 6 / 2) Are OpenObj's open-vocabulary object-level and part - extractive body cue:** However, this sensitivity comes at the cost of losing the capacity to recover complex concepts.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Upon closer observation, they then derive a detailed description of the individual components of specific objects (e.g., ‘this cup has a square handle and a ...
- **p. 6 / 2) Are OpenObj's open-vocabulary object-level and part - extractive body cue:** LSeg, as a fine-tuned model of CLIP, TABLE II: 3D Zero-shot Segmentation Results mIoU mAcc Scene LERF 3DOVS Con.G.
- **p. 7 / 2) Are OpenObj's open-vocabulary object-level and part - extractive body cue:** 7: OpenObj's multi-granularity scene understanding supports multi-granularity downstream tasks, including object-oriented global movement and part-oriented local manipulation. a marked advantage in handling patterns, components, and ...
- **p. 5 / III. OPENOBJ - extractive body cue:** This approach helps to mitigate the effects of outliers caused by poor observation viewpoints or model failures.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (III. OPENOBJ), p. 5 (III. OPENOBJ), p. 2 (I. INTRODUCTION), p. 3 (III. OPENOBJ), p. 4 (III. OPENOBJ), p. 4 (III. OPENOBJ), objective p. 5 (III. OPENOBJ), p. 5 (III. OPENOBJ), p. 3 (III. OPENOBJ), p. 3 (III. OPENOBJ), temporal p. 3 (II. RELATED WORKS), p. 1 (Abstract), p. 1 (I. INTRODUCTION), p. 2 (II. RELATED WORKS), p. 2 (II. RELATED WORKS), p. 3 (III. OPENOBJ).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
