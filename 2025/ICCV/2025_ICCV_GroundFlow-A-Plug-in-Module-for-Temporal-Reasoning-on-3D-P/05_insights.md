# Insights — GroundFlow: A Plug-in Module for Temporal Reasoning on 3D Point Cloud Sequential Grounding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Lin_GroundFlow_A_Plug-in_Module_for_Temporal_Reasoning_on_3D_Point_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Lin_GroundFlow_A_Plug-in_Module_for_Temporal_Reasoning_on_3D_Point_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** In summary, we make the following contributions: • We propose the GroundFlow module with a recurrent framework, which can be integrated into previous 3DVG baselines ...
- **p. 2 / 1. Introduction - extractive body cue:** In addition, we propose GroundFlow module, which can be built on top of the existing 3DVG methods to perform temporal fusion with previous step embeddings, ...
- **p. 5 / 3.3. Training Objective - extractive body cue:** Detailed illustration of Memory component in GroundFlow, which enables the module to extract relevant information of both short-term ( ˆJt-1) and long-term ( ˆJm) effectively.
- **p. 5 / 3.3. Training Objective - extractive body cue:** Following the SG3D benchmark [52], we use the same cross-entropy loss to optimize the dual-stream model and the query-based model.
- **p. 5 / 3.3. Training Objective - extractive body cue:** In addition to the loss of token predictions when pre-trained on other datasets, an extra cross-entropy loss is incorporated to fine-tune the model on SG3D ...
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.3. Training Objective), p. 5 (3.3. Training Objective), p. 5 (3.3. Training Objective)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** While 3D LLMs achieve state-of-the-art results in various 3D tasks, they still face significant difficulty adapting to the complex SG3D problem [52].
- **p. 2 / 1. Introduction - extractive body cue:** The main reason for the huge performance gap between the two tasks is that current 3DVG methods are not designed to reason over historical information.
- **p. 1 / 1. Introduction - extractive body cue:** S3 : Sit on the black office chair under that same desk to enjoy your drink O2 : Cup O3 : Chair_2 Chair_1 Grounding Sequences ...
- **p. 1 / 1. Introduction - extractive body cue:** An example of SG3D task (above) and a comparison between previous visual grounding framework (bottom left) and our recurrent framework (bottom right) integrated with GroundFlow ...
- **p. 6 / 4.3. Comparison on SG3D Benchmark - extractive body cue:** Their degraded performance is particularly reflected in their overall task accuracy, with three of the models are falling below 30%.
- **p. 7 / 4.4. Ablation Study - extractive body cue:** This advantage could stem from the limitations of existing methods: LSTM or GRU tends to forget longterm information.
- **p. 7 / 4.4. Ablation Study - extractive body cue:** Since previous step embeddings do not attend to this lost information, it cannot be carried forward to subsequent steps, even if it is essential for ...
- **Boundary to test:** Their degraded performance is particularly reflected in their overall task accuracy, with three of the models are falling below 30%.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In summary, we make the following contributions: • We propose the GroundFlow module with a recurrent framework, which can be integrated into previous 3DVG baselines and introduce important temporal reasoning capabilities to ... | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | On the other hand, significant performance improvements can be observed when these models are integrated with GroundFlow, as shown in the rows highlighted in orange. | p. 6 (4.3. Comparison on SG3D Benchmark), p. 6 (4.3. Comparison on SG3D Benchmark) |
| Failure/limitation | Their degraded performance is particularly reflected in their overall task accuracy, with three of the models are falling below 30%. | p. 6 (4.3. Comparison on SG3D Benchmark), p. 7 (4.4. Ablation Study) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 As shown, GroundFlow module's output ˆJt will be treated as input in the next step t + 1. studied task that requires the agent to locate the target objects in 3D scenes ...를 This framework sequentially takes each step instruction and processes only the current step instruction as input rather than handling all prior text instructions simultaneously.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Their degraded performance is particularly reflected in their overall task accuracy, with three of the models are falling below 30%.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In summary, we make the following contributions: • We propose the GroundFlow module with a recurrent framework, which can be integrated into previous 3DVG baselines and introduce important temporal reasoning capabilities to ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Their degraded performance is particularly reflected in their overall task accuracy, with three of the models are falling below 30%.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: The benchmark utilizes real-world scenes from the SceneVerse [26], incorporating indoor scans from 5 different datasets - ScanNet [11], 3RScan [40], MultiScan [31], ARKitScenes [3] and HM3D [36]..
3. Compare against the body-reported baseline or a matched simpler baseline: However, the 3DVG methods combined with our proposed GroundFlow module outperform LEO across all five datasets, setting new state-of-the-art performance on SG3D benchmark..
4. Report the body metric and its denominator/aggregation: To address these limitations, the memory component in GroundFlow computes similarity scores to selectively retrieve and integrate context-specific past information based on its relevance to the current step, leading to superior performa ....
5. Re-run the body-reported ablation/failure condition: In Table 3, the performance without one of the memory parts is presented in the first and second rows..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (3.3. Training Objective), p. 5 (3.3. Training Objective); the primary result is directionally consistent at p. 6 (4.3. Comparison on SG3D Benchmark), p. 6 (4.3. Comparison on SG3D Benchmark), p. 7 (4.4. Ablation Study); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summary, make, following mechanism이 However, the 3DVG methods combined with our proposed GroundFlow module outperform LEO across all five datasets, ... 대비 To address these limitations, the memory component in GroundFlow computes similarity scores to selectively retrieve and integrate context-specific ...을 개선하고, Their degraded performance is particularly reflected in their overall task accuracy, with three of the models ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
