# Insights — SeeGround: See and Ground for Zero-Shot Open-Vocabulary 3D Visual Grounding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Li_SeeGround_See_and_Ground_for_Zero-Shot_Open-Vocabulary_3D_Visual_Grounding_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Li_SeeGround_See_and_Ground_for_Zero-Shot_Open-Vocabulary_3D_Visual_Grounding_CVPR_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are as follows: • We introduce SeeGround, a training-free solution for zero-shot 3DVG.
- **p. 2 / 1. Introduction - extractive body cue:** Considering that 2D-VLMs cannot process 3D data directly, we introduce a cross-modal alignment representation that enables 2D-VLMs to interpret 3D scenes.
- **p. 3 / 3. Methodology - extractive body cue:** (1) In this work, we propose a novel method for 3DVG that integrates 2D-VLM with spatially enriched 3D scene representations.
- **p. 3 / 3. Methodology - extractive body cue:** This representation allows our framework to align the rich visual features from 2D renderings with the spatial context from 3D scene descriptions.
- **p. 4 / 3.2. Perspective Adaptation Module - extractive body cue:** To meet these needs, we propose a query-driven dynamic scene rendering method that aligns the rendered viewpoint with the query description, capturing more scene details, ...
- **p. 5 / 3.3. Fusion Alignment Module - extractive body cue:** To address this, we introduce the Fusion Alignment Module, which explicitly associates key visual features in the scene with the textual description, ensuring a clear ...
- **p. 4 / 3.1. Multimodal 3D Representation - extractive body cue:** Finally, the 2D-VLM outputs the target object's ID, which is then used to retrieve its 3D bounding box from the OLT , providing the final, ...
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Methodology), p. 3 (3. Methodology), p. 4 (3.2. Perspective Adaptation Module), p. 5 (3.3. Fusion Alignment Module)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** This approach avoids redundancy in multi-view methods and limitations of bird's-eye views, which lack height and orientation details.
- **p. 2 / 1. Introduction - extractive body cue:** However, when textual descriptions and images are processed separately by 2D-VLMs, the model cannot associate 3D spatial information from text to the object in the ...
- **p. 1 / 1. Introduction - extractive body cue:** Previous research has focused on specific scenarios, where models [5, 19, 41, 52, 59, 62, 63] are trained on small-scale datasets, limiting their scalability and ...
- **p. 7 / 4.3. Ablation Study - extractive body cue:** ZSVG3D [60] projects object centers onto a 2D image and uses predefined functions to infer spatial relations, but this approach lacks flexibility, omits visual cues, ...
- **p. 8 / 4.3. Ablation Study - extractive body cue:** Bird's Eye View, though comprehensive, cannot adjust to the query and misses key spatial details like object orientation and height.
- **p. 8 / 4.3. Ablation Study - extractive body cue:** Current viewpoint selection strategies also fall short in handling complex scenarios like "when the window is on the left" or "upon entering from the door".
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Overview of the SeeGround framework. We first use a 2D-VLM to interpret the query, identifying both the target object (e.g., "laptop") and a ...
- **Boundary to test:** ZSVG3D [60] projects object centers onto a 2D image and uses predefined functions to infer spatial relations, but this approach lacks flexibility, omits visual cues, and ignores contextual objects, risking misidentification if ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our contributions are as follows: • We introduce SeeGround, a training-free solution for zero-shot 3DVG. | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | Our method achieves 46.1% accuracy on Nr3D, which is a 18.2% improvement over the previous zero-shot baseline, ZSVG3D [60] (39.0%). | p. 7 (4.2. Comparative Study), p. 7 (4.2. Comparative Study) |
| Failure/limitation | ZSVG3D [60] projects object centers onto a 2D image and uses predefined functions to infer spatial relations, but this approach lacks flexibility, omits visual cues, and ignores contextual objects, risking misidentification if ... | p. 7 (4.3. Ablation Study), p. 8 (4.3. Ablation Study) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 ies [55, 60] attempt to reduce 3D-specific training requirements by reformatting 3D scenes and text descriptions for large language models (LLMs) [38, 39], but these methods primarily rely on text input, neglecting ...를 However, prior 3D scene representations - such as point clouds [14, 40], voxels [29], and implicit representations [22] - are not directly compatible with the input format required by 2D-VLM.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 ZSVG3D [60] projects object centers onto a 2D image and uses predefined functions to infer spatial relations, but this approach lacks flexibility, omits visual cues, and ignores contextual objects, risking misidentification if ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our contributions are as follows: • We introduce SeeGround, a training-free solution for zero-shot 3DVG.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Robotics-enabling 3D perception`; tags: `3D visual grounding, zero-shot, open-vocabulary`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** ZSVG3D [60] projects object centers onto a 2D image and uses predefined functions to infer spatial relations, but this approach lacks flexibility, omits visual cues, and ignores contextual objects, risking misidentification if ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We use two popular benchmark datasets to evaluate our 3DVG approach..
3. Compare against the body-reported baseline or a matched simpler baseline: 1 compares methods on the ScanRefer dataset. our method outperforms other zero-shot methods [55, 60] and the weakly supervised WS-3DVG [50], achieving competitive results with supervised methods..
4. Report the body metric and its denominator/aggregation: While fully supervised methods like MCLN [41] and ConcreteNet [47] achieve higher accuracy, our proposed SeeGround framework demonstrates competitive zero-shot performance, highlighting its potential for scalable, annotation-free 3D gro ....
5. Re-run the body-reported ablation/failure condition: Ablation study on different components in our framework on Nr3D [1]. "3D Pos.": 3D object coordinates; "Layout": Scene layout; "Texture": Object color/texture; "FAM": Fusion Alignment Module; and "PAM": Perspective Adaptation Module. # ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (3.3. Fusion Alignment Module), p. 4 (3.1. Multimodal 3D Representation), p. 3 (3. Methodology); the primary result is directionally consistent at p. 7 (4.2. Comparative Study), p. 7 (4.2. Comparative Study), p. 6 (4.2. Comparative Study); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 contributions, follows, introduce mechanism이 1 compares methods on the ScanRefer dataset. our method outperforms other zero-shot methods [55, 60] and ... 대비 While fully supervised methods like MCLN [41] and ConcreteNet [47] achieve higher accuracy, our proposed SeeGround framework demonstrates ...을 개선하고, ZSVG3D [60] projects object centers onto a 2D image and uses predefined functions to infer spatial ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
