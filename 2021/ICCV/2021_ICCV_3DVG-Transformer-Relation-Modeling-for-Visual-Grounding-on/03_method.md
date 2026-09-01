# Method - 3DVG-Transformer: Relation Modeling for Visual Grounding on Point Clouds

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2021/html/Zhao_3DVG-Transformer_Relation_Modeling_for_Visual_Grounding_on_Point_Clouds_ICCV_2021_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2021/papers/Zhao_3DVG-Transformer_Relation_Modeling_for_Visual_Grounding_on_Point_Clouds_ICCV_2021_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3.2. Relation-enhanced Proposal Generation), p. 4 (3.2. Relation-enhanced Proposal Generation), p. 5 (3.3. Cross-modal Proposal Disambiguation), p. 5 (3.3. Cross-modal Proposal Disambiguation), p. 3 (3. Methodology), p. 3 (3.1. Overview)): The network structure of our coordinate-guided contextual aggregation module (a), which consists of 2 transformer layers (the multi-level feature fusion module is omitted here).

## Method Body Digest

- **p. 4 / 3.2. Relation-enhanced Proposal Generation - extractive PDF cue:** The network structure of our coordinate-guided contextual aggregation module (a), which consists of 2 transformer layers (the multi-level feature fusion module is omitted here).
- **p. 4 / 3.2. Relation-enhanced Proposal Generation - extractive PDF cue:** The first one is a self-attention block that exploits the relations among the spatial neighbors of the input clusters, which is then followed by an ...
- **p. 5 / 3.3. Cross-modal Proposal Disambiguation - extractive PDF cue:** After feeding the word features Fword into an independent self-attention module, we propose a multiplex attention module to fuse the word features and the proposal ...
- **p. 5 / 3.3. Cross-modal Proposal Disambiguation - extractive PDF cue:** In each pair, a self-attention block is firstly used to exploit the contextual relationships among the selected proposals and enhance the distinctiveness (a.k.a. disambiguation) of ...
- **p. 3 / 3. Methodology - extractive PDF cue:** 3.4, we introduce the objective function of our method, which also includes a pair of feature augmentation strategies for alleviating overfitting.
- **p. 3 / 3.1. Overview - extractive PDF cue:** The overall framework of our 3DVG-Transformer consists of three modules at three stages, including the object proposal generation module, the language encoding module, and the ...
- **p. 5 / 3.4. Loss Function - extractive PDF cue:** Note that the object detection loss exactly follows the loss used in Qi et al.
- **p. 5 / 3.4. Loss Function - extractive PDF cue:** The final loss is a linear combination of these terms, i.e., L = 0.3Lloc + 10Ldet + 0.1Lcls.

## Design Rationale

- **p. 3 / 3. Methodology - extractive PDF cue:** 3.1, we present an overview of our method.
- **p. 3 / 3. Methodology - extractive PDF cue:** 3.4, we introduce the objective function of our method, which also includes a pair of feature augmentation strategies for alleviating overfitting.
- **p. 2 / 1. Introduction - extractive PDF cue:** The contribution of this work is three-fold: (1) A simple and strong visual grounding framework (referred to as 3DVG-Transformer) specifically designed for point clouds, which ...

## Source Evidence Cues

- **p. 4 / 3.2. Relation-enhanced Proposal Generation - extractive PDF cue:** The network structure of our coordinate-guided contextual aggregation module (a), which consists of 2 transformer layers (the multi-level feature fusion module is omitted here).
- **p. 4 / 3.2. Relation-enhanced Proposal Generation - extractive PDF cue:** The first one is a self-attention block that exploits the relations among the spatial neighbors of the input clusters, which is then followed by an ...
- **p. 5 / 3.3. Cross-modal Proposal Disambiguation - extractive PDF cue:** After feeding the word features Fword into an independent self-attention module, we propose a multiplex attention module to fuse the word features and the proposal ...
- **p. 5 / 3.3. Cross-modal Proposal Disambiguation - extractive PDF cue:** In each pair, a self-attention block is firstly used to exploit the contextual relationships among the selected proposals and enhance the distinctiveness (a.k.a. disambiguation) of ...
- **p. 3 / 3. Methodology - extractive PDF cue:** 3.4, we introduce the objective function of our method, which also includes a pair of feature augmentation strategies for alleviating overfitting.
- **p. 3 / 3.1. Overview - extractive PDF cue:** The overall framework of our 3DVG-Transformer consists of three modules at three stages, including the object proposal generation module, the language encoding module, and the ...
- **Detected method headings:** 3. Methodology (p. 3); 4.2. Comparisons with the state-of-the-art methods (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | The network structure of our coordinate-guided contextual aggregation module (a), which consists of 2 transformer layers (the multi-level feature fusion module is ... | p. 4 (3.2. Relation-enhanced Proposal Generation), p. 4 (3.2. Relation-enhanced Proposal Generation) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | The first one is a self-attention block that exploits the relations among the spatial neighbors of the input clusters, which is then ... | p. 4 (3.2. Relation-enhanced Proposal Generation), p. 5 (3.3. Cross-modal Proposal Disambiguation) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | After feeding the word features Fword into an independent self-attention module, we propose a multiplex attention module to fuse the word features ... | p. 5 (3.3. Cross-modal Proposal Disambiguation), p. 5 (3.3. Cross-modal Proposal Disambiguation) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3. Methodology - extractive PDF cue:** 3.4, we introduce the objective function of our method, which also includes a pair of feature augmentation strategies for alleviating overfitting.
- **p. 5 / 3.4. Loss Function - extractive PDF cue:** Note that the object detection loss exactly follows the loss used in Qi et al.
- **p. 5 / 3.4. Loss Function - extractive PDF cue:** The final loss is a linear combination of these terms, i.e., L = 0.3Lloc + 10Ldet + 0.1Lcls.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 3 (3. Methodology), p. 5 (3.4. Loss Function), p. 5 (3.4. Loss Function).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | goal, visual, grounding, point, clouds, localize, object, interest, target, cloud, output, axis-aligned, bounding, center | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | goal, visual, grounding, point, clouds, localize, object, interest, target, cloud | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | present, overview, introduce, objective, function, includes, pair, feature, augmentation, strategies | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | introduce, objective, function, includes, pair, feature, augmentation, strategies, alleviating, overfitting | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3.1. Overview - extractive PDF cue:** The goal of visual grounding on 3D point clouds is to localize the object of interest (i.e., the target object) in each point cloud, and ...
- **p. 3 / 3.2. Relation-enhanced Proposal Generation - extractive PDF cue:** However, these intermediate outputs only capture local point cloud features that describe the candidate objects, so they are not aware of the relations with other ...
- **p. 1 / 1. Introduction - extractive PDF cue:** As one emerging 3D visual understanding task, visual grounding on point clouds, also called as referring 3D object localization, aims to locate the desired objects ...
- **p. 1 / 1. Introduction - extractive PDF cue:** To be specific, they first use the state-of-theart (SOTA) 3D object detector [8] or the ground-truth (GT) bounding boxes to generate object proposals, whose features ...
- **p. 4 / 3.2. Relation-enhanced Proposal Generation - extractive PDF cue:** Each coordinate-guided transformer layer refines its input cluster centers and cluster features.
- **p. 4 / 3.2. Relation-enhanced Proposal Generation - extractive PDF cue:** 2 (a), we use the initial cluster center xi, and the initial cluster feature fi as the input of this CCA module.
- **p. 5 / 3.4. Loss Function - extractive PDF cue:** In detail, we randomly erase 20% words of the input sentences, and we also have 50% of chances to erase the target object nouns with ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | The overall framework of our 3DVG-Transformer consists of three modules at three stages, including the object proposal generation module, the language encoding ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | To fully evaluate our method, we compare our method with the baseline methods on both the validation set and the online test ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | The network is trained for 120, 000 iterations, with a batch size of 8, in which each scene is paired with 8 ... | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 4.1. Datasets and Implementation Details - extractive PDF cue:** The network is trained for 120, 000 iterations, with a batch size of 8, in which each scene is paired with 8 sentences, thus there ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** network, structure, coordinate-guided, contextual, aggregation, module, consists, transformer, layers, multi-level, feature, fusion, omitted, here, first, self-attention, block, exploits, relations, among.
- **Relevant PDF headings:** 3. Methodology (p. 3); 4.2. Comparisons with the state-of-the-art methods (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | To fully evaluate our method, we compare our method with the baseline methods on both the validation set and the online test ... | p. 5 (4.1. Datasets and Implementation Details), p. 5 (4.1. Datasets and Implementation Details) |
| Semantic / temporal fusion | In Table 1 and Table 2, our 3DVG-Transformer is compared with several baseline methods on both ScanRefer and Nr3D/Sr3D datasets, which include ... | p. 6 (4.2. Comparisons with the state-of-the-art methods), p. 7 (4.2. Comparisons with the state-of-the-art methods) |
| Robot query / planning handoff | Figure 3. Qualitative results from ScanRefer [6] and our 3DVG-Transformer. The GT boxes are marked in blue. If one predicted box has ... | p. 7 (Figure/Table caption), p. 7 (4.2. Comparisons with the state-of-the-art methods) |

## Failure and Ablation Link

- **p. 8 / 4.3. Ablation Study and Analysis - extractive PDF cue:** We take the ScanRefer validation set [6] as an example to perform a comprehensive ablation study and analyze different components in our 3DVGTransformer.
- **p. 7 / 4.2. Comparisons with the state-of-the-art methods - extractive PDF cue:** Ablation study on the ScanRefer validation set [6] under the "2D+3D" setting.
- **p. 8 / 4.3. Ablation Study and Analysis - extractive PDF cue:** Results of our 3DVG-Transformer (i.e. "Add SPM") and two variants (i.e. "w/o SPM" and "Mul SPM") on the Nr3D validation set [7].
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 1. The pipeline of our 3DVG-Transformer, which includes an object proposal generation module, a language encoding module, and a cross-modal fusion module. The input ...
- **p. 7 / 4.2. Comparisons with the state-of-the-art methods - extractive PDF cue:** The failure cases of ScanRefer indicate that this baseline method cannot well model complex relations and distinguish ambiguous objects.
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. The network structure of our coordinate-guided contex- tual aggregation module (a), which consists of 2 transformer lay- ers (the multi-level feature fusion module ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3.2. Relation-enhanced Proposal Generation), p. 4 (3.2. Relation-enhanced Proposal Generation), p. 5 (3.3. Cross-modal Proposal Disambiguation), p. 5 (3.3. Cross-modal Proposal Disambiguation), p. 3 (3. Methodology), p. 3 (3.1. Overview), objective p. 3 (3. Methodology), p. 5 (3.4. Loss Function), p. 5 (3.4. Loss Function), temporal p. 3 (3.1. Overview), p. 5 (4.1. Datasets and Implementation Details), p. 7 (4.2. Comparisons with the state-of-the-art methods), p. 2 (2. Related Work), p. 2 (1. Introduction), p. 3 (2. Related Work).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
