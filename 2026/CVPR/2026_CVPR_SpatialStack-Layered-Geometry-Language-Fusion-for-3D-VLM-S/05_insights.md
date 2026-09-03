# Insights — SpatialStack: Layered Geometry-Language Fusion for 3D VLM Spatial Reasoning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_SpatialStack_Layered_Geometry-Language_Fusion_for_3D_VLM_Spatial_Reasoning_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_SpatialStack_Layered_Geometry-Language_Fusion_for_3D_VLM_Spatial_Reasoning_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** We summarize our contributions as follows: • We present the first systematic analysis of how fusion layers across vision encoders, geometry encoders, and LLM decoders ...
- **p. 2 / 1. Introduction - extractive body cue:** Building on these insights, we introduce SpatialStack, a general hierarchical fusion framework that integrates multi-level geometric features into multimodal LLMs.
- **p. 8 / Model - extractive body cue:** 5 shows that our method maintains robust general capabilities while specializing in spatial-temporal tasks, confirming no catastrophic forgetting.
- **p. 8 / Model - extractive body cue:** 4, our two versions of SpatialStack surpass all baselines of similar scale and same base models on both 2D and 3D subsets, demonstrating the benefits ...
- **p. 8 / Model - extractive body cue:** (%) Proprietary Models (API) GPT-4o [14] 74.8 83.0 78.9 Open-source Models Mini-Gemini-HD-34B [22] 71.5 79.2 75.4 LLaVA-NeXT-34B [19] 73.0 74.8 73.9 Cambrian-1-34B [40] 74.0 79.7 ...
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 8 (Model), p. 8 (Model), p. 8 (Model)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** Noticing these limitations of conventional VLMs, many recent works still prioritize image-level semantic alignment over the understanding of spatial and geometric structures [17, 32, 37].
- **p. 2 / 1. Introduction - extractive body cue:** Bridging this gap requires unifying geometric awareness with vision-language reasoning within a single framework, which is a key step toward reliable spatial intelligence.
- **p. 8 / 6. Conclusion - extractive body cue:** We introduced SpatialStack, a hierarchical fusion framework bridging the gap between vision, geometry, and language for robust 3D spatial reasoning.
- **p. 7 / 5.2. Evaluation - extractive body cue:** Notably, despite lacking route-planning data during training, it still surpasses all open-source systems on this task, demonstrating robust zero-shot generalization for highlevel spatial reasoning.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 5. General Capabilities Evaluation. Our SpatialStack-5B maintains robust general multimodal and spatial-temporal reason- ing capabilities, demonstrating no catastrophic forgetting. Evaluation on CV-Bench. To assess ...
- **Boundary to test:** We introduced SpatialStack, a hierarchical fusion framework bridging the gap between vision, geometry, and language for robust 3D spatial reasoning.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We summarize our contributions as follows: • We present the first systematic analysis of how fusion layers across vision encoders, geometry encoders, and LLM decoders affect the granularity of spatial reasoning. | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | Furthermore, under a fair comparison using the identical Qwen2.5 base model, SpatialStack significantly outperforms other concurrent geometry-aware MLLMs, such as Spatial-MLLM [45], VG-LLM [53], and Cambrian-S [48]. | p. 7 (5.2. Evaluation), p. 5 (Figure/Table caption) |
| Failure/limitation | We introduced SpatialStack, a hierarchical fusion framework bridging the gap between vision, geometry, and language for robust 3D spatial reasoning. | p. 8 (6. Conclusion), p. 7 (5.2. Evaluation) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 An initial line of work sought to compensate for these weaknesses by integrating explicit geometric inputs (e.g., precomputed point clouds or depth maps) into VLMs.를 Despite remarkable progress in large vision-language models (VLMs), reliable spatial reasoning remains challenging, as these models often fail to effectively encode 3D geometry and spatial relationships and to associate them with langua ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 We introduced SpatialStack, a hierarchical fusion framework bridging the gap between vision, geometry, and language for robust 3D spatial reasoning.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: We summarize our contributions as follows: • We present the first systematic analysis of how fusion layers across vision encoders, geometry encoders, and LLM decoders affect the granularity of spatial reasoning.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Robotics-enabling 3D perception`; tags: `geometry, VLM, spatial reasoning`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** We introduced SpatialStack, a hierarchical fusion framework bridging the gap between vision, geometry, and language for robust 3D spatial reasoning.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: VLM-3R reformulates spatial question-answer pairs in a VSI-Bench-style format, producing diverse reasoning tasks such as relative direction, object counting, and absolute distance estimation from real-world 3D-annotated scenes..
3. Compare against the body-reported baseline or a matched simpler baseline: Table 4. Comparison on CV-Bench. Built on Qwen2.5, SpatialStack-4B outperforms its base model alongside VG-LLM and Cambrian-S. Scaling to Qwen3.5, SpatialStack-5B further im- proves upon its baseline to set a new state-of-the-art..
4. Report the body metric and its denominator/aggregation: Following the official protocol, we report mean MCA accuracy and Mean Relative Accuracy for NA across confidence thresholds C = 0.5, 0.55, . . . , 0.95..
5. Re-run the body-reported ablation/failure condition: 5.2, and provide extensive ablation studies in Sec..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 8 (Model), p. 8 (Model); the primary result is directionally consistent at p. 7 (5.2. Evaluation), p. 5 (Figure/Table caption), p. 5 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summarize, contributions, follows mechanism이 Table 4. Comparison on CV-Bench. Built on Qwen2.5, SpatialStack-4B outperforms its base model alongside VG-LLM and ... 대비 Following the official protocol, we report mean MCA accuracy and Mean Relative Accuracy for NA across confidence thresholds ...을 개선하고, We introduced SpatialStack, a hierarchical fusion framework bridging the gap between vision, geometry, and language for ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
