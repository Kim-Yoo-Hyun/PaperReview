# Insights — ReferSplat: Referring Segmentation in 3D Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=reuShgiHdg; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/165044. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / 1. Introduction - extractive body cue:** To bridge this gap, we introduce a new task: Referring 3D Gaussian Splatting Segmentation (R3DGS), which focuses on segmenting objects in a 3D Gaussian scene ...
- **p. 2 / 1. Introduction - extractive body cue:** To enhance spatial reasoning, we introduce a Position-aware Cross-Modal Interaction module that extracts position features for both Gaussians and language descriptions.
- **p. 2 / 1. Introduction - extractive body cue:** In this work, we propose ReferSplat, an end-to-end framework that models 3D Gaussian points with natural language expressions in a spatially aware paradigm for Referring ...
- **p. 3 / 3.2. Problem Statement and Method Overview - extractive body cue:** To infuse languageawareness into the 3D Gaussians, we introduce a new property called referring features.
- **p. 4 / 3.3. 3D Gaussian Referring Fields - extractive body cue:** 2, our method surpasses existing approaches, establishing a superior referring segmentation framework in 3D Gaussian scenes.
- **p. 5 / 3.4. Position-aware Cross-Modal Interaction - extractive body cue:** To address these issues, we propose a Position-aware CrossModal Interaction module that injects position information into the cross-modal attention mechanism to facilitate interactions between textual ...
- **p. 5 / 3.4. Position-aware Cross-Modal Interaction - extractive body cue:** To integrate position information, we first extract position features from 3D Gaussian representations.
- **Contribution anchor:** p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.2. Problem Statement and Method Overview), p. 4 (3.3. 3D Gaussian Referring Fields), p. 5 (3.4. Position-aware Cross-Modal Interaction)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** However, these methods face significant limitations when applied to R3DGS.
- **p. 1 / 1. Introduction - extractive body cue:** 1, R3DGS requires the model to identify newly described objects, even when occluded or not directly visible in the novel view, posing a significant challenge ...
- **p. 1 / 1. Introduction - extractive body cue:** To bridge this gap, we introduce a new task: Referring 3D Gaussian Splatting Segmentation (R3DGS), which focuses on segmenting objects in a 3D Gaussian scene ...
- **p. 2 / 1. Introduction - extractive body cue:** One major drawback is the lack of interaction between the text query and Gaussian representations during training.
- **p. 3 / 3.2. Problem Statement and Method Overview - extractive body cue:** The key challenge lies in segmenting the target object in this unseen view, where it may be partially occluded or even entirely invisible.
- **p. 9 / 6. Limitation and Future Work - extractive body cue:** 1) Our current method does not account for dynamic factors, which are crucial for real-world applications.
- **p. 9 / 6. Limitation and Future Work - extractive body cue:** 2) While we focus on 3D referring segmentation in Gaussian Splatting, our method does not incorporate 3D visual grounding.
- **Boundary to test:** Figure 2. Comparison of (a) existing open-vocabulary 3DGS seg- mentation pipeline and (b) the proposed ReferSplat for R3DGS. 3D scene representation learning. During inference, output masks are obtained by matching the input ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To bridge this gap, we introduce a new task: Referring 3D Gaussian Splatting Segmentation (R3DGS), which focuses on segmenting objects in a 3D Gaussian scene based on natural language expressions that typically ... | p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | Results show that ReferSplat achieves significantly lower computational complexity and faster inference speed than LangSplat (Qin et al., 2024). | p. 8 (4.6. Analysis of Computation Costs), p. 7 (4.3. Ablation Study) |
| Failure/limitation | Figure 2. Comparison of (a) existing open-vocabulary 3DGS seg- mentation pipeline and (b) the proposed ReferSplat for R3DGS. 3D scene representation learning. During inference, output masks are obtained by matching the input ... | p. 2 (Figure/Table caption), p. 9 (6. Limitation and Future Work) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 While the proposed Position-aware Cross-Modal Interaction module effectively captures the relationship between Gaussian representations and text descriptions, distinguishing between languages with similar meanings but referring to diffe ...를 During inference, output masks are obtained by matching the input open-vocabulary class names with the rendered feature, as shown in Fig.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Figure 2. Comparison of (a) existing open-vocabulary 3DGS seg- mentation pipeline and (b) the proposed ReferSplat for R3DGS. 3D scene representation learning. During inference, output masks are obtained by matching the input ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To bridge this gap, we introduce a new task: Referring 3D Gaussian Splatting Segmentation (R3DGS), which focuses on segmenting objects in a 3D Gaussian scene based on natural language expressions that typically ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `3D Vision, Gaussian Splatting`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 2. Comparison of (a) existing open-vocabulary 3DGS seg- mentation pipeline and (b) the proposed ReferSplat for R3DGS. 3D scene representation learning. During inference, output masks are obtained by matching the input ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: The LERF dataset (Kerr et al., 2023) is collected using the Polycam iPhone app and consists of four diverse, complex, real-world scenes..
3. Compare against the body-reported baseline or a matched simpler baseline: 1, incorporating PCMI (index 1) improves mIoU by 5.1% and 4.3%, respectively compared to the baseline, which is our constructed Referring Feature Fields..
4. Report the body metric and its denominator/aggregation: In contrast, alternative approaches-such as using the top-1 prediction, propagating the first-frame mask with SAM2 (Ravi et al., 2025), or selecting masks solely based on IoU without confidence weighting-yield inferior results..
5. Re-run the body-reported ablation/failure condition: We conduct ablation experiments to evaluate the effectiveness of different components..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (3.4. Position-aware Cross-Modal Interaction), p. 4 (3.2. Problem Statement and Method Overview), p. 3 (3.2. Problem Statement and Method Overview); the primary result is directionally consistent at p. 8 (4.6. Analysis of Computation Costs), p. 7 (4.3. Ablation Study), p. 7 (4.3. Ablation Study); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 bridge, introduce, task mechanism이 1, incorporating PCMI (index 1) improves mIoU by 5.1% and 4.3%, respectively compared to the baseline, ... 대비 In contrast, alternative approaches-such as using the top-1 prediction, propagating the first-frame mask with SAM2 (Ravi et al., ...을 개선하고, Figure 2. Comparison of (a) existing open-vocabulary 3DGS seg- mentation pipeline and (b) the proposed ReferSplat ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
