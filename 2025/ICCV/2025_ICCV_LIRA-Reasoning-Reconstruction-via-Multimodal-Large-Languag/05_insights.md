# Insights — LIRA: Reasoning Reconstruction via Multimodal Large Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_LIRA_Reasoning_Reconstruction_via_Multimodal_Large_Language_Models_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhou_LIRA_Reasoning_Reconstruction_via_Multimodal_Large_Language_Models_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our major contributions are as follows: • We introduce the reasoning reconstruction task, which requires online 3D reconstruction guided by implicit and complex ...
- **p. 2 / 1. Introduction - extractive body cue:** To achieve higher-quality instance fusion, we propose TIFF, a Text-enhanced Instance Fusion module operating within a Fragment bounding volume (FBV), which is learning-based and fuses ...
- **p. 4 / 3.1.2. 2D Reasoning Segmentation within the FBV - extractive body cue:** (3) Then, fimg and ˆhseg (text feature prompt) are input into the mask decoder Fdec of the segmentation foundation model to output the binary mask ...
- **p. 7 / 4.5. Runtime Analysis - extractive body cue:** To achieve real-time inference, we propose LIRA-Fast.
- **p. 4 / 3.1.2. 2D Reasoning Segmentation within the FBV - extractive body cue:** The image features directly use the image embeddings fimg of the segmentation foundation model in the 2D reasoning segmentation module.
- **p. 5 / 3.1.2. 2D Reasoning Segmentation within the FBV - extractive body cue:** Current Instances Global Instances Mask Confidence Branch Similarity Matrix Calculation x y z w h l 3D Bounding Boxes Masked Cross-Attention MLP Add & Norm ...
- **p. 7 / 4.4. Explicit Instruction-Guided Reconstruction - extractive body cue:** For example, an inStage Method AP AP50 AP25 I Replace with SEEM [59] 3.68 11.00 19.57 Replace with Grounded-SAM [25] 3.06 10.12 18.26 Replace with ...
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.1.2. 2D Reasoning Segmentation within the FBV), p. 7 (4.5. Runtime Analysis), p. 4 (3.1.2. 2D Reasoning Segmentation within the FBV), p. 5 (3.1.2. 2D Reasoning Segmentation within the FBV)

### Strongest assumption and failure boundary

- **p. 1 / 1. Introduction - extractive body cue:** However, existing systems [15, 27, 46, 47] mainly rely on explicit instructions, such as explicitly indicating target objects or categories, to reconstruct instruction-relevant regions, while ...
- **p. 2 / 1. Introduction - extractive body cue:** Particularly for implicit instructions involving complex reasoning, they are more difficult to handle.
- **p. 2 / 1. Introduction - extractive body cue:** Since geometric reconstruction can be accurately obtained by systems such as Simultaneous Localization and Mapping (SLAM) [12, 16, 17, 55], the main challenge in reasoning ...
- **p. 1 / 1. Introduction - extractive body cue:** The target instance based on the current map is within the red box.
- **p. 8 / 5. Conclusion - extractive body cue:** One limitation is that LIRA exhibits relatively low performance in high-precision reconstruction.
- **p. 8 / 5. Conclusion - extractive body cue:** Future work will consider further optimization in 3D space.
- **p. 6 / 3.4. Benchmark - extractive body cue:** Erroneous projected pixels caused by occlusion are filtered out.
- **Boundary to test:** One limitation is that LIRA exhibits relatively low performance in high-precision reconstruction.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In summary, our major contributions are as follows: • We introduce the reasoning reconstruction task, which requires online 3D reconstruction guided by implicit and complex instructions. | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | Table 5. Ablation studies of the three stages of LIRA. struction "Appliances or furniture used to store food" is replaced with "Cabinet, Refrigerator". The generated ex- plicit instruction format is consistent with ... | p. 7 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Failure/limitation | One limitation is that LIRA exhibits relatively low performance in high-precision reconstruction. | p. 8 (5. Conclusion), p. 8 (5. Conclusion) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 Given an implicit and complex instruction L and posed RGB-D sequences as input, LIRA first incrementally performs geometric reconstruction, and leverages a MLLM to actively reason about L and obtain instruction-relevant 2D ...를 An image can only provide instance information within a local field of view, and the complex language instruction requires reasoning based on the global map.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 One limitation is that LIRA exhibits relatively low performance in high-precision reconstruction.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In summary, our major contributions are as follows: • We introduce the reasoning reconstruction task, which requires online 3D reconstruction guided by implicit and complex instructions.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `3D Vision, Vision-Language`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** One limitation is that LIRA exhibits relatively low performance in high-precision reconstruction.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: To establish a comprehensive evaluation system suitable for the reasoning reconstruction task, a benchmark ReasonRecon is constructed and the data collection pipeline is shown in Fig..
3. Compare against the body-reported baseline or a matched simpler baseline: Table 4. Runtime analysis of reasoning reconstruction. comparison. VLMaps is extended to a 3D map by can- celing top-down projection. LIRA* represents that LIRA uses LLaVA-13B and applies ChatGPT-4o for reasoning in ....
4. Report the body metric and its denominator/aggregation: We evaluate using standard Average Precision (AP) metrics at IoU thresholds of 50% and 25%, and also calculate mean score across IoU thresholds from 50% to 95% in 5% increments..
5. Re-run the body-reported ablation/failure condition: Table 5. Ablation studies of the three stages of LIRA. struction "Appliances or furniture used to store food" is replaced with "Cabinet, Refrigerator". The generated ex- plicit instruction format is consistent with ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (3.1.2. 2D Reasoning Segmentation within the FBV), p. 7 (4.5. Runtime Analysis), p. 4 (3.1.2. 2D Reasoning Segmentation within the FBV); the primary result is directionally consistent at p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 6 (4.3. Reasoning Reconstruction Results); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summary, major, contributions mechanism이 Table 4. Runtime analysis of reasoning reconstruction. comparison. VLMaps is extended to a 3D map by ... 대비 We evaluate using standard Average Precision (AP) metrics at IoU thresholds of 50% and 25%, and also calculate ...을 개선하고, One limitation is that LIRA exhibits relatively low performance in high-precision reconstruction. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
