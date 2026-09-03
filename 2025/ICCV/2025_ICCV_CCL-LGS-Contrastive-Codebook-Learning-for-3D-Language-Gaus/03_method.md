# Method - CCL-LGS: Contrastive Codebook Learning for 3D Language Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Tian_CCL-LGS_Contrastive_Codebook_Learning_for_3D_Language_Gaussian_Splatting_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Tian_CCL-LGS_Contrastive_Codebook_Learning_for_3D_Language_Gaussian_Splatting_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (3.3. Contrastive Codebook Learning), p. 4 (3.2. Two-Level Semantic Feature Extraction), p. 5 (3.4. 3D Gaussian Semantic Field), p. 3 (3. Method), p. 3 (3. Method), p. 4 (3.2. Two-Level Semantic Feature Extraction)): This approach consists of two key steps: (1) mask association via IoU matching and (2) applying contrastive losses to improve feature representation.

## Method Body Digest

- **p. 5 / 3.3. Contrastive Codebook Learning - extractive body cue:** This approach consists of two key steps: (1) mask association via IoU matching and (2) applying contrastive losses to improve feature representation.
- **p. 4 / 3.2. Two-Level Semantic Feature Extraction - extractive body cue:** Although LangSplat [20] extracts object-level features with clear boundaries by generating masks for subparts, parts, and whole objects, its dependence on multiple models increases data ...
- **p. 5 / 3.4. 3D Gaussian Semantic Field - extractive body cue:** To jointly optimize the semantic features of 3D Gaussians and the parameters of the MLP decoder, we minimize the cross-entropy loss: \ m ath c ...
- **p. 3 / 3. Method - extractive body cue:** 2, we first extract two-level semantic features from multi-view images (Sec.
- **p. 3 / 3. Method - extractive body cue:** 3.2), then perform mask association and contrastive codebook learning to organize and refine these features (Sec.
- **p. 4 / 3.2. Two-Level Semantic Feature Extraction - extractive body cue:** The optimization is driven by supervision using cross-entropy loss.
- **p. 6 / 3.4. 3D Gaussian Semantic Field - extractive body cue:** \tau , we compute its embedding \varphi (\tau ) via the text encoder of the vision-language model to compute the relevance map. p ( \t ...
- **p. 5 / 3.3. Contrastive Codebook Learning - extractive body cue:** (5) Contrastive losses are then applied based on the assigned mask labels.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** The main contributions of our work can be summarized as follows: • We propose a novel framework, CCL-LGS, which integrates view-consistent semantic supervision to enable ...
- **p. 2 / 1. Introduction - extractive body cue:** Owing to its proficiency in 3D open-vocabulary scene understanding, our method could benefit a variety of downstream applications.
- **p. 3 / 3. Method - extractive body cue:** In this section, we present our proposed framework, CCLLGS, for view-consistent 3D semantic reconstruction.

## Source Evidence Cues

- **p. 5 / 3.3. Contrastive Codebook Learning - extractive body cue:** This approach consists of two key steps: (1) mask association via IoU matching and (2) applying contrastive losses to improve feature representation.
- **p. 4 / 3.2. Two-Level Semantic Feature Extraction - extractive body cue:** Although LangSplat [20] extracts object-level features with clear boundaries by generating masks for subparts, parts, and whole objects, its dependence on multiple models increases data ...
- **p. 5 / 3.4. 3D Gaussian Semantic Field - extractive body cue:** To jointly optimize the semantic features of 3D Gaussians and the parameters of the MLP decoder, we minimize the cross-entropy loss: \ m ath c ...
- **p. 3 / 3. Method - extractive body cue:** 2, we first extract two-level semantic features from multi-view images (Sec.
- **p. 3 / 3. Method - extractive body cue:** 3.2), then perform mask association and contrastive codebook learning to organize and refine these features (Sec.
- **p. 4 / 3.2. Two-Level Semantic Feature Extraction - extractive body cue:** The optimization is driven by supervision using cross-entropy loss.
- **p. 6 / 3.4. 3D Gaussian Semantic Field - extractive body cue:** \tau , we compute its embedding \varphi (\tau ) via the text encoder of the vision-language model to compute the relevance map. p ( \t ...
- **Detected method headings:** 3. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | This approach consists of two key steps: (1) mask association via IoU matching and (2) applying contrastive losses to improve feature representation. | p. 5 (3.3. Contrastive Codebook Learning), p. 4 (3.2. Two-Level Semantic Feature Extraction) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Although LangSplat [20] extracts object-level features with clear boundaries by generating masks for subparts, parts, and whole objects, its dependence on multiple ... | p. 4 (3.2. Two-Level Semantic Feature Extraction), p. 5 (3.4. 3D Gaussian Semantic Field) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | To jointly optimize the semantic features of 3D Gaussians and the parameters of the MLP decoder, we minimize the cross-entropy loss: \ ... | p. 5 (3.4. 3D Gaussian Semantic Field), p. 3 (3. Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.4. 3D Gaussian Semantic Field - extractive body cue:** To jointly optimize the semantic features of 3D Gaussians and the parameters of the MLP decoder, we minimize the cross-entropy loss: \ m ath c ...
- **p. 4 / 3.2. Two-Level Semantic Feature Extraction - extractive body cue:** The optimization is driven by supervision using cross-entropy loss.
- **p. 4 / 3.2. Two-Level Semantic Feature Extraction - extractive body cue:** Although LangSplat [20] extracts object-level features with clear boundaries by generating masks for subparts, parts, and whole objects, its dependence on multiple models increases data ...
- **p. 5 / 3.3. Contrastive Codebook Learning - extractive body cue:** (5) Contrastive losses are then applied based on the assigned mask labels.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (3.2. Two-Level Semantic Feature Extraction), p. 4 (3.2. Two-Level Semantic Feature Extraction), p. 5 (3.3. Contrastive Codebook Learning), p. 5 (3.3. Contrastive Codebook Learning).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | pixel, semantic, feature, expressed, F_i, CLIP, I_t, odot, M_i, label, supervised_f, where, input, image | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | pixel, semantic, feature, expressed, F_i, CLIP, I_t, odot, M_i, label | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | main, contributions, summarized, follows, novel, framework, CCL-LGS, integrates, view-consistent, semantic | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | jointly, optimize, semantic, features, Gaussians, parameters, MLP, decoder, minimize, cross-entropy | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.2. Two-Level Semantic Feature Extraction - extractive body cue:** For each pixel v, its semantic feature Fi(v) can be expressed as: F_i ( v) = \t e xt {CLIP}(I_t \odot M_i(v)), \label {supervised_f} (3) ...
- **p. 2 / 1. Introduction - extractive body cue:** The main contributions of our work can be summarized as follows: • We propose a novel framework, CCL-LGS, which integrates view-consistent semantic supervision to enable ...
- **p. 3 / 3.2. Two-Level Semantic Feature Extraction - extractive body cue:** However, some methods [8, 25] rely on multi-scale patch averaging for pixellevel semantic feature extraction, which often leads to blurred boundaries.
- **p. 4 / 3.2. Two-Level Semantic Feature Extraction - extractive body cue:** By integrating mask generation and feature extraction within a unified framework, our approach reduces computational overhead while ensuring high semantic accuracy and precise boundary delineation.
- **p. 5 / 3.4. 3D Gaussian Semantic Field - extractive body cue:** 2, by converting per-pixel semantic features into discrete indices and aligning these indices with the outputs of 3D Gaussian Splatting.
- **p. 5 / 3.3. Contrastive Codebook Learning - extractive body cue:** Specifically, N represents a fixed capacity for scene-specific feature learning, while K refers to the number of object categories observed in the current scene subset, ...
- **p. 6 / 3.4. 3D Gaussian Semantic Field - extractive body cue:** \tau , we compute its embedding \varphi (\tau ) via the text encoder of the vision-language model to compute the relevance map. p ( \t ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | In this section, we present our proposed framework, CCLLGS, for view-consistent 3D semantic reconstruction. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | By integrating mask generation and feature extraction within a unified framework, our approach reduces computational overhead while ensuring high semantic accuracy and ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.2. Two-Level Semantic Feature Extraction - extractive body cue:** Although LangSplat [20] extracts object-level features with clear boundaries by generating masks for subparts, parts, and whole objects, its dependence on multiple models increases data ...
- **p. 5 / 3.4. 3D Gaussian Semantic Field - extractive body cue:** To jointly optimize the semantic features of 3D Gaussians and the parameters of the MLP decoder, we minimize the cross-entropy loss: \ m ath c ...
- **p. 6 / 4. Experiments - extractive body cue:** The training is performed over 30,000 iterations using the Adam optimizer [10], with a learning rate of 0.001 and beta parameters set to (0.9, 0.999).
- **p. 4 / 3.2. Two-Level Semantic Feature Extraction - extractive body cue:** Although LangSplat [20] extracts object-level features with clear boundaries by generating masks for subparts, parts, and whole objects, its dependence on multiple models increases data ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** consists, steps, mask, association, IoU, matching, applying, contrastive, losses, improve, feature, representation, Although, LangSplat, extracts, object-level, features, clear, boundaries, generating.
- **Relevant PDF headings:** 3. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | The dataset's real-world imaging conditions, including severe occlusions and motion blur, make it particularly suited for testing segmentation robustness in complex environments. | p. 6 (4. Experiments), p. 6 (4. Experiments) |
| Semantic / temporal fusion | Our method achieves consistent multi-view segmentation and accurately captures challenging objects like the cabinet, outperforming prior approaches. glass of water kamaboko RGB ... | p. 7 (4.1. Experiments on LERF), p. 7 (Figure/Table caption) |
| Robot query / planning handoff | We observed that our method achieved an IoU result of 65.6 in 3D semantic segmentation, ranking either first or second across all ... | p. 6 (4.1. Experiments on LERF), p. 7 (4.1. Experiments on LERF) |

## Failure and Ablation Link

- **p. 6 / 4.1. Experiments on LERF - extractive body cue:** To validate the effectiveness of our Contrastive Codebook Learning (CCL) module, we conduct experiments, including visual analysis of 2D supervision features and ablation studies on ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. Qualitative comparison of different loss configurations. The pull loss improves intra-class consistency (e.g., for "glass of water"), while the push loss reduces false ...
- **p. 7 / 4.1. Experiments on LERF - extractive body cue:** 2, both losses are essential for optimal performance-removing either causes noticeable degradation, though all variants still surpass the baseline.
- **p. 6 / 4.1. Experiments on LERF - extractive body cue:** Qualitative comparison of 2D feature maps with and without CCL module.
- **p. 8 / 5. Conclusion - extractive body cue:** Limitations remain due to inherent capabilities of SAM and SAM2, as imperfect masks still affect results.
- **p. 8 / 5. Conclusion - extractive body cue:** Future work will refine masks for greater robustness.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Quantitative comparison of our method and LangSplat under three challenging scenarios: Occlusion, Image Blur, and View- Dependent Variations. The results clearly demonstrate the ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (3.3. Contrastive Codebook Learning), p. 4 (3.2. Two-Level Semantic Feature Extraction), p. 5 (3.4. 3D Gaussian Semantic Field), p. 3 (3. Method), p. 3 (3. Method), p. 4 (3.2. Two-Level Semantic Feature Extraction), objective p. 5 (3.4. 3D Gaussian Semantic Field), p. 4 (3.2. Two-Level Semantic Feature Extraction), p. 4 (3.2. Two-Level Semantic Feature Extraction), p. 5 (3.3. Contrastive Codebook Learning), temporal p. 3 (3. Method), p. 4 (3.2. Two-Level Semantic Feature Extraction), p. 4 (3.2. Two-Level Semantic Feature Extraction), p. 5 (3.3. Contrastive Codebook Learning), p. 5 (3.3. Contrastive Codebook Learning), p. 6 (4.1. Experiments on LERF).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
