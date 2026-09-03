# Insights — SoFar: Language-Grounded Orientation Bridges Spatial Reasoning and Object Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (46 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=kmv7yg6QXv; PDF retrieval source: https://arxiv.org/pdf/2502.13143. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 Introduction - extractive body cue:** We propose PointSO, a generalizable cross-modal 3D Transformer [114, 26, 89, 91] for semantic orientation prediction.
- **p. 2 / 1 Introduction - extractive body cue:** In addition, we introduce Open6DOR V2, a large-scale benchmark for 6-DoF object rearrangement in simulation, which supports both open-loop and closed-loop control.
- **p. 3 / 1 Introduction - extractive body cue:** Finally, we present two new benchmarks, Open6DOR V2 and 6-DoF SpatialBench, to evaluate 6-DoF rearrangement and spatial reasoning.
- **p. 3 / 1 Introduction - extractive body cue:** To support this, we introduce OrienText300K, a curated dataset of 3D models annotated with diverse language-guided orientation labels.
- **p. 5 / 1 Introduction - extractive body cue:** This enriched spatial representation enables the VLM to perform accurate spatial reasoning by leveraging its visual and linguistic understanding.
- **p. 4 / 1 Introduction - extractive body cue:** For the 3D point clouds, we follow [26, 136, 89] to first sample Ns seed points using farthest point sampling (FPS) and then group inputs ...
- **p. 5 / 1 Introduction - extractive body cue:** Position & Orientation Information Extraction Given a language query Q, we first prompt a visionlanguage model FVLM to extract a task-relevant set of object phrases ...
- **Contribution anchor:** p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 5 (1 Introduction), p. 4 (1 Introduction)

### Strongest assumption and failure boundary

- **p. 2 / 1 Introduction - extractive body cue:** However, translating a specific language description into a desired orientation is challenging for existing VLMs.
- **p. 4 / 1 Introduction - extractive body cue:** Data Annotation As mentioned in the introduction, VLMs struggle to produce accurate object orientation values, which presents a significant challenge for data generation.
- **p. 5 / 1 Introduction - extractive body cue:** To bridge this gap, we build an integrated reasoning system where a powerful VLM acts as an agent and reasons about the scene while communicating ...
- **p. 2 / 1 Introduction - extractive body cue:** We observe that current VLMs struggle with understanding object orientation, making them insufficient for 6-DoF robot manipulation planning.
- **p. 3 / 1 Introduction - extractive body cue:** We develop the SOFAR system, which enhances spatial reasoning with 6-DoF scene graph and achieves SOTA performance on Open6DOR, SimplerEnv, and generalizes across embodiments (e.g., ...
- **p. 9 / 4 Experiments - extractive body cue:** 5 Limitations & Conclusions One notable limitation for decoupled systems like SOFAR is that the execution may fail due to a sub-module error, as shown ...
- **p. 8 / 4 Experiments - extractive body cue:** Furthermore, leveraging the error detection and re-planning capabilities of VLMs [48, 1], we can make multiple attempts following a single-step execution failure to approximately achieve ...
- **Boundary to test:** 5 Limitations & Conclusions One notable limitation for decoupled systems like SOFAR is that the execution may fail due to a sub-module error, as shown in Section B.8, i.e., robots may place ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We propose PointSO, a generalizable cross-modal 3D Transformer [114, 26, 89, 91] for semantic orientation prediction. | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Reported outcome | SOFAR consistently outperforms other methods across both tracks, achieving over 18% improvement. | p. 9 (4 Experiments), p. 8 (4 Experiments) |
| Failure/limitation | 5 Limitations & Conclusions One notable limitation for decoupled systems like SOFAR is that the execution may fail due to a sub-module error, as shown in Section B.8, i.e., robots may place ... | p. 9 (4 Experiments), p. 8 (4 Experiments) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 X Y Z Pose Estimation Category / Instance Template Needed Only axis, the relationship with instruction is unclear "Blow Wind" "Top" "Back" "Pick up" "Fan" "Front" Semantic Orientation Without any template Training ...를 For the 3D point clouds, we follow [26, 136, 89] to first sample Ns seed points using farthest point sampling (FPS) and then group inputs with KNN for point feature embedding with ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 5 Limitations & Conclusions One notable limitation for decoupled systems like SOFAR is that the execution may fail due to a sub-module error, as shown in Section B.8, i.e., robots may place ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: We propose PointSO, a generalizable cross-modal 3D Transformer [114, 26, 89, 91] for semantic orientation prediction.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `Robotics, 3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** 5 Limitations & Conclusions One notable limitation for decoupled systems like SOFAR is that the execution may fail due to a sub-module error, as shown in Section B.8, i.e., robots may place ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We migrate its scenes into a robosuite-based simulation environment [151], following the task interface defined by LIBERO [64], and name this new benchmark Open6DOR V2..
3. Compare against the body-reported baseline or a matched simpler baseline: 7, SOFAR consistently outperforms baselines across all tracks, especially on orientation and 6-DoF tasks, while maintaining low planning overhead..
4. Report the body metric and its denominator/aggregation: We present success rates for the "Variant Aggregation" and "Visual Matching" approaches..
5. Re-run the body-reported ablation/failure condition: Table 11: Ablation study of multi-modal fusion in PointSO. All experiments are conducted with the PointSO-Base variant. Fusion Method 45° 30° 15° 5°.
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction); the primary result is directionally consistent at p. 9 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 PointSO, generalizable, cross-modal mechanism이 7, SOFAR consistently outperforms baselines across all tracks, especially on orientation and 6-DoF tasks, while maintaining ... 대비 We present success rates for the "Variant Aggregation" and "Visual Matching" approaches.을 개선하고, 5 Limitations & Conclusions One notable limitation for decoupled systems like SOFAR is that the execution ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
