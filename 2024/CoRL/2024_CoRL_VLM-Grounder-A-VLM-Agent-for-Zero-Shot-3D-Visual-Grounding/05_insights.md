# Insights — VLM-Grounder: A VLM Agent for Zero-Shot 3D Visual Grounding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v270/xu25c.html; PDF retrieval source: https://raw.githubusercontent.com/mlresearch/v270/main/assets/xu25c/xu25c.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / 1 Introduction - extractive body cue:** While these methods achieve strong performance, they use only objectcentric information and often miss detailed scene context, making it challenging to handle queries like "find ...
- **p. 2 / 1 Introduction - extractive body cue:** Further, we propose a dynamic stitching strategy that dynamically uses the optimal layouts identified by the benchmark to stitch images, enhancing VLM's performance.
- **p. 3 / 3 Methodology - extractive body cue:** In this section, we present the overall framework of VLM-Grounder (Sec.
- **p. 4 / 3 Methodology - extractive body cue:** To study the effects of stitching, we designed a novel benchmark called the VisualRetrieval Benchmark, detailed in Sec.
- **p. 1 / 1 Introduction - extractive body cue:** Our approach involves a VLM that analyzes user queries and sequences of images capturing the scene to locate the target object, whose 2D mask is ...
- **p. 7 / 3 Methodology - extractive body cue:** Without model training, VLM-Grounder's overall performance also competes with supervised learning methods like InstanceRefer (38.8%) and 3DVG-Transformer (40.8%).
- **p. 8 / 3 Methodology - extractive body cue:** VLM-Grounder has several appealing properties: it leverages foundation models from the language and 2D domains without training, and offers a more transparent and explainable grounding ...
- **Contribution anchor:** p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (3 Methodology), p. 4 (3 Methodology), p. 1 (1 Introduction), p. 7 (3 Methodology)

### Strongest assumption and failure boundary

- **p. 1 / 1 Introduction - extractive body cue:** However, existing visual grounding datasets[1, 2] are scarce and limited to a pre-defined vocabulary, challenging the development of general models for open-world applications.
- **p. 1 / 1 Introduction - extractive body cue:** Since LLMs cannot directly process 3D environments, these methods employ a point cloud-based 3D localization module [10, 11] to detect objects and convert their attributes ...
- **p. 2 / 1 Introduction - extractive body cue:** Object 1 is a black cabinet at (x1, y1, z1).
- **p. 2 / 1 Introduction - extractive body cue:** However, estimating a 3D bounding box from a single image can be problematic due to limited field-of-view and inaccurate depth information.
- **p. 20 / Figure/Table caption - extractive body cue:** Figure 5: Failure cases of the VLM grounding module. 20
- **p. 21 / Figure/Table caption - extractive body cue:** Figure 8: A failure case of the projection module. 21
- **p. 6 / 3 Methodology - extractive body cue:** Although our multi-view ensemble projection module helps mitigate this issue, it cannot entirely eliminate it.
- **Boundary to test:** Figure 5: Failure cases of the VLM grounding module. 20

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | While these methods achieve strong performance, they use only objectcentric information and often miss detailed scene context, making it challenging to handle queries like "find the room with the most abundant natural ... | p. 1 (1 Introduction), p. 2 (1 Introduction) |
| Reported outcome | Table 1: 3D visual grounding results on ScanRefer. Without using geometric information from point clouds, VLM-Grounder outperforms previous zero-shot methods and achieves performance comparable to supervised learning baselines. * indica ... | p. 6 (Figure/Table caption), p. 8 (3 Methodology) |
| Failure/limitation | Figure 5: Failure cases of the VLM grounding module. 20 | p. 20 (Figure/Table caption), p. 21 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 2) Inputting many images quickly consumes the VLM's context length, limiting output content and potentially affecting performance.를 The target image and bounding box are input into the Segment Anything Model (SAM) [52] to obtain a fine-grained mask.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Figure 5: Failure cases of the VLM grounding module. 20에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: While these methods achieve strong performance, they use only objectcentric information and often miss detailed scene context, making it challenging to handle queries like "find the room with the most abundant natural ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Robotics-enabling 3D perception`; tags: `3D visual grounding, VLM, zero-shot`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 5: Failure cases of the VLM grounding module. 20; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We introduced a novel Visual-Retrieval benchmark to evaluate the impact of stitching operations on VLM's visual understanding..
3. Compare against the body-reported baseline or a matched simpler baseline: Table 1: 3D visual grounding results on ScanRefer. Without using geometric information from point clouds, VLM-Grounder outperforms previous zero-shot methods and achieves performance comparable to supervised learning baselines. * indica ....
4. Report the body metric and its denominator/aggregation: Table 10: Success rates of different modules. Query Analysis View Pre-Selection Image Selection by VLM OV-Detection 100% 96% 77%.
5. Re-run the body-reported ablation/failure condition: Without stitching, the system often encounters timeouts and fails to complete the task, underscoring the necessity of an effective stitching strategy..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 7 (3 Methodology), p. 8 (3 Methodology), p. 3 (3 Methodology); the primary result is directionally consistent at p. 6 (Figure/Table caption), p. 8 (3 Methodology), p. 8 (3 Methodology); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 While, methods, achieve mechanism이 Table 1: 3D visual grounding results on ScanRefer. Without using geometric information from point clouds, VLM-Grounder ... 대비 Table 10: Success rates of different modules. Query Analysis View Pre-Selection Image Selection by VLM OV-Detection 100% 96% ...을 개선하고, Figure 5: Failure cases of the VLM grounding module. 20 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
