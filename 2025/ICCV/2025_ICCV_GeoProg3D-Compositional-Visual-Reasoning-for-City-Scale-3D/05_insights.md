# Insights — GeoProg3D: Compositional Visual Reasoning for City-Scale 3D Language Fields

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Yasuki_GeoProg3D_Compositional_Visual_Reasoning_for_City-Scale_3D_Language_Fields_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Yasuki_GeoProg3D_Compositional_Visual_Reasoning_for_City-Scale_3D_Language_Fields_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are threefold: • We propose GeoProg3D, a framework for compositional reasoning over city-scale 3D language fields, where visual programming can perform ...
- **p. 2 / 1. Introduction - extractive body cue:** To validate the effectiveness, we introduce novel tasks designed to assess urban-scale geographic visual reasoning capabilities and present GeoEval3D, a benchmark dataset specifically developed for ...
- **p. 6 / 4.1. Task Definition - extractive body cue:** The task set Qi = {(qk, ak)}Ki k=1 consists of pairs of queries qk and the corresponding ground truth answers ak.
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 6 (4.1. Task Definition)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** However, when extending conventional 3D language fields for large-scale urban 3D scenes, two fundamental difficulties emerge: (1) Scalability for city-scale 3D data: Since existing methods ...
- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are threefold: • We propose GeoProg3D, a framework for compositional reasoning over city-scale 3D language fields, where visual programming can perform ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 7. Qualitative results and failure cases. The Ground Truth region for the GRD task is delineated by the yellow frame. localization that is independent ...
- **p. 8 / 5.2. Experimental results - extractive body cue:** Ablation study of different Geographical Vision APIs. itative examples and failure cases.
- **p. 7 / 5.1. Evaluation metrics - extractive body cue:** Note that MES-H and CMP are not evaluated in UrbanScene3D because Ground Truth for height cannot be obtained.
- **p. 7 / 5.2. Experimental results - extractive body cue:** These results demonstrate the limitations of localization using 3D language fields alone in 3D urban scenes and the effectiveness of GV-APIs and visual programming in ...
- **Boundary to test:** Figure 7. Qualitative results and failure cases. The Ground Truth region for the GRD task is delineated by the yellow frame. localization that is independent of the viewpoint, taking into account the ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In summary, our contributions are threefold: • We propose GeoProg3D, a framework for compositional reasoning over city-scale 3D language fields, where visual programming can perform various 3D geographic vision tasks via image ... | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | GeoProg3D further improved accuracy on both GoolgeEarth and UrbanScene3D. | p. 7 (5.2. Experimental results), p. 7 (5.2. Experimental results) |
| Failure/limitation | Figure 7. Qualitative results and failure cases. The Ground Truth region for the GRD task is delineated by the yellow frame. localization that is independent of the viewpoint, taking into account the ... | p. 8 (Figure/Table caption), p. 8 (5.2. Experimental results) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 In summary, our contributions are threefold: • We propose GeoProg3D, a framework for compositional reasoning over city-scale 3D language fields, where visual programming can perform various 3D geographic vision tasks via image ...를 However, intuitive and efficient interaction with these detailed 3D city models using natural language remains largely unexplored.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Figure 7. Qualitative results and failure cases. The Ground Truth region for the GRD task is delineated by the yellow frame. localization that is independent of the viewpoint, taking into account the ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In summary, our contributions are threefold: • We propose GeoProg3D, a framework for compositional reasoning over city-scale 3D language fields, where visual programming can perform various 3D geographic vision tasks via image ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 7. Qualitative results and failure cases. The Ground Truth region for the GRD task is delineated by the yellow frame. localization that is independent of the viewpoint, taking into account the ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: The dataset B = {(Di, Qi)}S i=1 consists of pairs multi-view image sets Di and task sets Qi, where S is the number of outdoor scenes..
3. Compare against the body-reported baseline or a matched simpler baseline: We observed that GCLF outperforms baselines on GoogleEarth..
4. Report the body metric and its denominator/aggregation: Localization accuracy is measured at an IoU threshold of 0.15..
5. Re-run the body-reported ablation/failure condition: To assess the impact of each component of GeoProg3D, we conducted an ablation study to investigate the three tasks of GoogleEarth's GRD, SPR, and CMP..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at method anchor 없음; the primary result is directionally consistent at p. 7 (5.2. Experimental results), p. 7 (5.2. Experimental results), p. 5 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summary, contributions, threefold mechanism이 We observed that GCLF outperforms baselines on GoogleEarth. 대비 Localization accuracy is measured at an IoU threshold of 0.15.을 개선하고, Figure 7. Qualitative results and failure cases. The Ground Truth region for the GRD task is ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
