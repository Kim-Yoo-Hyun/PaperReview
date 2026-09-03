# Insights — CCL-LGS: Contrastive Codebook Learning for 3D Language Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Tian_CCL-LGS_Contrastive_Codebook_Learning_for_3D_Language_Gaussian_Splatting_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Tian_CCL-LGS_Contrastive_Codebook_Learning_for_3D_Language_Gaussian_Splatting_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** The main contributions of our work can be summarized as follows: • We propose a novel framework, CCL-LGS, which integrates view-consistent semantic supervision to enable ...
- **p. 2 / 1. Introduction - extractive body cue:** Owing to its proficiency in 3D open-vocabulary scene understanding, our method could benefit a variety of downstream applications.
- **p. 3 / 3. Method - extractive body cue:** In this section, we present our proposed framework, CCLLGS, for view-consistent 3D semantic reconstruction.
- **p. 4 / 3.2. Two-Level Semantic Feature Extraction - extractive body cue:** In our method, a uniform 32×32 point prompt is provided to SAM to generate three types of masks corresponding to the semantic scales of subparts, ...
- **p. 5 / 3.3. Contrastive Codebook Learning - extractive body cue:** To mitigate the limitations of directly using features derived from imperfect masks, we introduce a codebookbased contrastive learning approach.
- **p. 5 / 3.3. Contrastive Codebook Learning - extractive body cue:** This approach consists of two key steps: (1) mask association via IoU matching and (2) applying contrastive losses to improve feature representation.
- **p. 4 / 3.2. Two-Level Semantic Feature Extraction - extractive body cue:** Although LangSplat [20] extracts object-level features with clear boundaries by generating masks for subparts, parts, and whole objects, its dependence on multiple models increases data ...
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Method), p. 4 (3.2. Two-Level Semantic Feature Extraction), p. 5 (3.3. Contrastive Codebook Learning), p. 5 (3.3. Contrastive Codebook Learning)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** However, their reliance on exhaustive multi-scale rendering leads to inefficiency, and patch-based feature extraction often fails to capture precise object boundaries, resulting in scale misalignment ...
- **p. 2 / 1. Introduction - extractive body cue:** This makes it difficult to maintain semantic coherence across views and often leads to artifacts in the rendered novel views.
- **p. 8 / 5. Conclusion - extractive body cue:** Limitations remain due to inherent capabilities of SAM and SAM2, as imperfect masks still affect results.
- **p. 8 / 5. Conclusion - extractive body cue:** Future work will refine masks for greater robustness.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Quantitative comparison of our method and LangSplat under three challenging scenarios: Occlusion, Image Blur, and View- Dependent Variations. The results clearly demonstrate the ...
- **p. 6 / 4. Experiments - extractive body cue:** The dataset's real-world imaging conditions, including severe occlusions and motion blur, make it particularly suited for testing segmentation robustness in complex environments.
- **p. 6 / 4.1. Experiments on LERF - extractive body cue:** In the kitchen scene, we specifically focus on the cabinet, a challenging object that other methods frequently fail to segment correctly.
- **Boundary to test:** Limitations remain due to inherent capabilities of SAM and SAM2, as imperfect masks still affect results.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | The main contributions of our work can be summarized as follows: • We propose a novel framework, CCL-LGS, which integrates view-consistent semantic supervision to enable the reconstruction of 3D Gaussian semantic fields. ... | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | We observed that our method achieved an IoU result of 65.6 in 3D semantic segmentation, ranking either first or second across all four scenes, outperforming the state-ofthe-art 3D Vision-Language GS by 3.6. | p. 6 (4.1. Experiments on LERF), p. 7 (4.1. Experiments on LERF) |
| Failure/limitation | Limitations remain due to inherent capabilities of SAM and SAM2, as imperfect masks still affect results. | p. 8 (5. Conclusion), p. 8 (5. Conclusion) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 For each pixel v, its semantic feature Fi(v) can be expressed as: F_i ( v) = \t e xt {CLIP}(I_t \odot M_i(v)), \label {supervised_f} (3) where It is the input image, and ...를 The main contributions of our work can be summarized as follows: • We propose a novel framework, CCL-LGS, which integrates view-consistent semantic supervision to enable the reconstruction of 3D Gaussian semantic fields. ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Limitations remain due to inherent capabilities of SAM and SAM2, as imperfect masks still affect results.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: The main contributions of our work can be summarized as follows: • We propose a novel framework, CCL-LGS, which integrates view-consistent semantic supervision to enable the reconstruction of 3D Gaussian semantic fields. ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `3D Vision, Gaussian Splatting`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Limitations remain due to inherent capabilities of SAM and SAM2, as imperfect masks still affect results.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: The dataset's real-world imaging conditions, including severe occlusions and motion blur, make it particularly suited for testing segmentation robustness in complex environments..
3. Compare against the body-reported baseline or a matched simpler baseline: Our method achieves consistent multi-view segmentation and accurately captures challenging objects like the cabinet, outperforming prior approaches. glass of water kamaboko RGB GT Ours w/ 𝓛𝓛𝒑𝒑𝒑𝒑𝒍𝒍𝒍𝒍 w/ 𝓛𝓛𝒑𝒑𝒑𝒑𝒔𝒔𝒔𝒔 baseline Figure 5..
4. Report the body metric and its denominator/aggregation: Note that the Room scene contains a significant annotation error; thus, we exclude it from quantitative evaluation and provide qualitative results only in the supplementary material..
5. Re-run the body-reported ablation/failure condition: To validate the effectiveness of our Contrastive Codebook Learning (CCL) module, we conduct experiments, including visual analysis of 2D supervision features and ablation studies on 3D semantic segmentation..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (3.3. Contrastive Codebook Learning), p. 4 (3.2. Two-Level Semantic Feature Extraction), p. 5 (3.4. 3D Gaussian Semantic Field); the primary result is directionally consistent at p. 6 (4.1. Experiments on LERF), p. 7 (4.1. Experiments on LERF), p. 8 (4.2. Experiments on 3D-OVS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 main, contributions, summarized mechanism이 Our method achieves consistent multi-view segmentation and accurately captures challenging objects like the cabinet, outperforming prior ... 대비 Note that the Room scene contains a significant annotation error; thus, we exclude it from quantitative evaluation and ...을 개선하고, Limitations remain due to inherent capabilities of SAM and SAM2, as imperfect masks still affect results. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
