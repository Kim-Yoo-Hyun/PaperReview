# Method - Towards CLIP-driven Language-free 3D Visual Grounding via 2D-3D Relational Enhancement and Consistency

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_Towards_CLIP-driven_Language-free_3D_Visual_Grounding_via_2D-3D_Relational_Enhancement_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Zhang_Towards_CLIP-driven_Language-free_3D_Visual_Grounding_via_2D-3D_Relational_Enhancement_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (3.4. Training and Inference), p. 4 (3.3. Relation Injection), p. 3 (3.1. Overview), p. 3 (3.1. Overview), p. 4 (3.3. Relation Injection), p. 5 (3.4. Training and Inference)): Here we first detail the network training objectives of learning with pseudolanguage features, and then outline the inference process using point clouds with authentic language queries.

## Method Body Digest

- **p. 5 / 3.4. Training and Inference - extractive body cue:** Here we first detail the network training objectives of learning with pseudolanguage features, and then outline the inference process using point clouds with authentic language ...
- **p. 4 / 3.3. Relation Injection - extractive body cue:** (2) Since there is no supervision of this relation during our training process, we introduce the proxy task of predicting the target object to achieve ...
- **p. 3 / 3.1. Overview - extractive body cue:** Our language-free 3DVG training framework comprises three key modules: Pseudo-Language Feature Generation (PFG), Neighboring Relation-aware Modeling (NRM), and Cross-modality Relation Consistency (CRC).
- **p. 3 / 3.1. Overview - extractive body cue:** The objective of our method is to train a model to localize specified objects without using any language queries during training, yet capable of identifying ...
- **p. 4 / 3.3. Relation Injection - extractive body cue:** To bridge this gap and enhance the relation representation ability of our CLIP-driven pseudo-language features, we further introduce a neighboring relation-aware module and a cross-modality ...
- **p. 5 / 3.4. Training and Inference - extractive body cue:** To minimize the discrepancy between training and inference, we also utilize CLIP to extract both local and global text features.
- **p. 3 / 3. Methodology - extractive body cue:** 3.3, we describe the methods for augmenting the pseudo-language features with more neighboring relation information and the construction of 2D and 3D relational consistency constraints.
- **p. 5 / 3.4. Training and Inference - extractive body cue:** We train the point cloud encoder with a detection loss LDet and a matching loss LVG as in [43].

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** Overall, our contributions can be summarized as follows: • We introduce a CLIP-driven language-free 3DVG framework, which requires no manually annotated texts to effectively achieve ...
- **p. 2 / 1. Introduction - extractive body cue:** To address the above issues, we propose a LanguageFree training method for 3D Visual Grounding, named 3DLFVG.
- **p. 3 / 3.1. Overview - extractive body cue:** The objective of our method is to train a model to localize specified objects without using any language queries during training, yet capable of identifying ...

## Source Evidence Cues

- **p. 5 / 3.4. Training and Inference - extractive body cue:** Here we first detail the network training objectives of learning with pseudolanguage features, and then outline the inference process using point clouds with authentic language ...
- **p. 4 / 3.3. Relation Injection - extractive body cue:** (2) Since there is no supervision of this relation during our training process, we introduce the proxy task of predicting the target object to achieve ...
- **p. 3 / 3.1. Overview - extractive body cue:** Our language-free 3DVG training framework comprises three key modules: Pseudo-Language Feature Generation (PFG), Neighboring Relation-aware Modeling (NRM), and Cross-modality Relation Consistency (CRC).
- **p. 3 / 3.1. Overview - extractive body cue:** The objective of our method is to train a model to localize specified objects without using any language queries during training, yet capable of identifying ...
- **p. 4 / 3.3. Relation Injection - extractive body cue:** To bridge this gap and enhance the relation representation ability of our CLIP-driven pseudo-language features, we further introduce a neighboring relation-aware module and a cross-modality ...
- **p. 5 / 3.4. Training and Inference - extractive body cue:** To minimize the discrepancy between training and inference, we also utilize CLIP to extract both local and global text features.
- **Detected method headings:** 3. Methodology (p. 3); 4.3. Compared Methods (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Here we first detail the network training objectives of learning with pseudolanguage features, and then outline the inference process using point clouds ... | p. 5 (3.4. Training and Inference), p. 4 (3.3. Relation Injection) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | (2) Since there is no supervision of this relation during our training process, we introduce the proxy task of predicting the target ... | p. 4 (3.3. Relation Injection), p. 3 (3.1. Overview) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Our language-free 3DVG training framework comprises three key modules: Pseudo-Language Feature Generation (PFG), Neighboring Relation-aware Modeling (NRM), and Cross-modality Relation Consistency (CRC). | p. 3 (3.1. Overview), p. 3 (3.1. Overview) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3. Methodology - extractive body cue:** 3.3, we describe the methods for augmenting the pseudo-language features with more neighboring relation information and the construction of 2D and 3D relational consistency constraints.
- **p. 3 / 3.1. Overview - extractive body cue:** The objective of our method is to train a model to localize specified objects without using any language queries during training, yet capable of identifying ...
- **p. 5 / 3.4. Training and Inference - extractive body cue:** We train the point cloud encoder with a detection loss LDet and a matching loss LVG as in [43].
- **p. 5 / 3.4. Training and Inference - extractive body cue:** To minimize the discrepancy between training and inference, we also utilize CLIP to extract both local and global text features.
- **p. 4 / 3.3. Relation Injection - extractive body cue:** (2) Since there is no supervision of this relation during our training process, we introduce the proxy task of predicting the target object to achieve ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 3 (3. Methodology), p. 3 (3.1. Overview), p. 5 (3.4. Training and Inference), p. 5 (3.3. Relation Injection).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | During, training, phase, inputs, consist, parts, point, cloud, coordinates, F-dimensional, auxiliary, features, points, corresponding | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | During, training, phase, inputs, consist, parts, point, cloud, coordinates, F-dimensional | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | Overall, contributions, summarized, follows, introduce, CLIP-driven, language-free, DVG, framework, requires | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | describe, methods, augmenting, pseudo-language, features, more, neighboring, relation, information, construction | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3.1. Overview - extractive body cue:** During training phase, the inputs consist of two parts: a point cloud P ∈RN×(3+F ) (with 3D coordinates and F-dimensional auxiliary features) of N points, ...
- **p. 3 / 3.1. Overview - extractive body cue:** At inference stage, the inputs shift to include a point cloud P ∈RN×(3+F ) and a sentence query Q ∈RL designed to describe the target ...
- **p. 5 / 3.4. Training and Inference - extractive body cue:** Different from the training process, at the inference stage, an input is a point cloud and its corresponding complete sentences from the test set.
- **p. 2 / 1. Introduction - extractive body cue:** 1, our key idea is to use multiview images which are readily available in existing datasets, e.g., ScanNet [8], as input to generate pseudo-language features ...
- **p. 1 / 1. Introduction - extractive body cue:** 3D Visual Grounding (3DVG) [1, 3-6, 25, 36, 42, 43], also known as referring 3D object localization, aims to accurately locate and identify specific objects ...
- **p. 4 / 3.1. Overview - extractive body cue:** It produces mask relation features by facilitating interactions between the main object and its adjacent objects.
- **p. 2 / 1. Introduction - extractive body cue:** Overall, our contributions can be summarized as follows: • We introduce a CLIP-driven language-free 3DVG framework, which requires no manually annotated texts to effectively achieve ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | 3.1 introduces the language-free training paradigm, along with an overview of the proposed framework. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Our language-free 3DVG training framework comprises three key modules: Pseudo-Language Feature Generation (PFG), Neighboring Relation-aware Modeling (NRM), and Cross-modality Relation Consistency (CRC). | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | We follow the ScanRefer benchmark to divide our dataset into the train/val/test set with 36,655, 9,508, and 5,410 samples respectively, and utilize ... | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.4. Training and Inference - extractive body cue:** Here we first detail the network training objectives of learning with pseudolanguage features, and then outline the inference process using point clouds with authentic language ...
- **p. 4 / 3.3. Relation Injection - extractive body cue:** (2) Since there is no supervision of this relation during our training process, we introduce the proxy task of predicting the target object to achieve ...
- **p. 3 / 3.1. Overview - extractive body cue:** Our language-free 3DVG training framework comprises three key modules: Pseudo-Language Feature Generation (PFG), Neighboring Relation-aware Modeling (NRM), and Cross-modality Relation Consistency (CRC).
- **p. 3 / 3.1. Overview - extractive body cue:** The objective of our method is to train a model to localize specified objects without using any language queries during training, yet capable of identifying ...
- **p. 5 / 3.4. Training and Inference - extractive body cue:** To minimize the discrepancy between training and inference, we also utilize CLIP to extract both local and global text features.
- **p. 5 / 4.2. Implementation Details - extractive body cue:** The model is trained with the AdamW [24] optimizer and a batch size of 8.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Here, first, detail, network, training, objectives, learning, pseudolanguage, features, then, outline, inference, process, point, clouds, authentic, language, queries, Since, there.
- **Relevant PDF headings:** 3. Methodology (p. 3); 4.3. Compared Methods (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We follow the ScanRefer benchmark to divide our dataset into the train/val/test set with 36,655, 9,508, and 5,410 samples respectively, and utilize ... | p. 5 (4.1. Datasets), p. 5 (4.1. Datasets) |
| Semantic / temporal fusion | Without language supervision, our method significantly outperforms previous methods. † indicates our re-implemented method on 3D. | p. 6 (4.2. Implementation Details), p. 5 (4.2. Implementation Details) |
| Robot query / planning handoff | Table 1. Quantitative comparison of language-free (LF) 3DVG on ScanRefer [4] dataset. Results of relevant fully supervised (Fully) meth- ods are also ... | p. 6 (Figure/Table caption), p. 6 (4.3. Compared Methods) |

## Failure and Ablation Link

- **p. 6 / 4.2. Implementation Details - extractive body cue:** Without language supervision, our method significantly outperforms previous methods. † indicates our re-implemented method on 3D.
- **p. 6 / 4.3. Compared Methods - extractive body cue:** Given its ability to perform 3DVG without text-based training, akin to our proposed paradigm, OpenScene serves as a benchmark for comparison.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Ablation study on main components of our method. We report the "overall" results in terms of Acc@0.25 and Acc@0.5. PFG Relation Acc@0.25 Acc@0.5 ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 5. Ablation study on different numbers (k) of neighboring objects in the NRM module. Here A refers to Acc. k Unique Multiple Overall A@0.25 ...
- **p. 8 / 5. Conclusion - extractive body cue:** Extensive experiments conducted on mainstream datasets demonstrate the robustness and efficiency of our approach.
- **p. 7 / 4.3. Compared Methods - extractive body cue:** It does not have a red chair near it.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Ablation study on main components of our method. We report the "overall" results in terms of Acc@0.25 and Acc@0.5. PFG Relation Acc@0.25 Acc@0.5 ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (3.4. Training and Inference), p. 4 (3.3. Relation Injection), p. 3 (3.1. Overview), p. 3 (3.1. Overview), p. 4 (3.3. Relation Injection), p. 5 (3.4. Training and Inference), objective p. 3 (3. Methodology), p. 3 (3.1. Overview), p. 5 (3.4. Training and Inference), p. 5 (3.4. Training and Inference), p. 4 (3.3. Relation Injection), temporal p. 3 (3. Methodology), p. 3 (3.1. Overview), p. 4 (3.3. Relation Injection), p. 5 (4.1. Datasets), p. 1 (Abstract), p. 2 (2.1. 3D Visual Grounding).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
