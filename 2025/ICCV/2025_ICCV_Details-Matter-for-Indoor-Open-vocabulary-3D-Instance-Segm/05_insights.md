# Insights — Details Matter for Indoor Open-vocabulary 3D Instance Segmentation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Jung_Details_Matter_for_Indoor_Open-vocabulary_3D_Instance_Segmentation_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Jung_Details_Matter_for_Indoor_Open-vocabulary_3D_Instance_Segmentation_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are summarized as follows: • We carefully combine the existing concepts and refine 3D proposal generation by removing overlaps in 2D predictions and ...
- **p. 1 / 1. Introduction - extractive body cue:** Examples of open-vocabulary predictions from our method in the ScanNet200 dataset [7].
- **p. 1 / 1. Introduction - extractive body cue:** Our method effectively retrieves instances based on functional descriptions (e.g., drink water, heat mac & cheese) and object attributes (e.g., red chair). dicted proposals into ...
- **p. 4 / 3.1. Image-based Proposal Generation - extractive body cue:** With refinement, irrelevant 3D superpoints are removed, and our method successfully removes 3D superpoints that do not belong to the object, resulting in geometrically consistent ...
- **p. 3 / 3.1. Image-based Proposal Generation - extractive body cue:** Leveraging VFMs [28, 35, 43], image-based proposals provide a complementary approach for detecting novel classes not covered during the training of the 3D instance segmentation ...
- **p. 5 / 3.2. Open-Vocabulary Instance Classification - extractive body cue:** Given a 3D proposal and the visual encoder from Alpha-CLIP, we project the proposal onto all 2D images and select a subset of images with ...
- **p. 5 / 3.2. Open-Vocabulary Instance Classification - extractive body cue:** Alpha-CLIP incorporates object masks as an additional input to guide the model's attention.
- **Contribution anchor:** p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 4 (3.1. Image-based Proposal Generation), p. 3 (3.1. Image-based Proposal Generation), p. 5 (3.2. Open-Vocabulary Instance Classification)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** However, ours has unique features to improve the limitations of existing works.
- **p. 1 / 1. Introduction - extractive body cue:** This paper carefully combines the concepts and refines each step to address key challenges, achieving state-of-theart (SoTA) performance in existing benchmarks.
- **p. 1 / 1. Introduction - extractive body cue:** While we adopt this general paradigm, we refine each stage to effectively handle missing details in the existing literature.
- **p. 2 / 1. Introduction - extractive body cue:** Following existing works [39, 60, 63], we use 3D superpoints [13] as a basic unit of point cloud operations.
- **p. 8 / 5. Conclusion - extractive body cue:** Improving such limitations remains our future work.
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 6. Failure cases of using CLIP for instance classification. CLIP fails when the shape of the object gets distorted or when other objects are ...
- **p. 8 / 5. Conclusion - extractive body cue:** Also, we found that our method fails to improve performance on small objects (e.g., ScanNet++ in the supplementary) but rather remain similar to existing approaches.
- **Boundary to test:** Improving such limitations remains our future work.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our contributions are summarized as follows: • We carefully combine the existing concepts and refine 3D proposal generation by removing overlaps in 2D predictions and applying robust 3D tracking for aggregation. • ... | p. 2 (1. Introduction), p. 1 (1. Introduction) |
| Reported outcome | These visual results are consistent with the recall metrics: Open3DIS and OpenYOLO3D achieve the mAR of 43.3% and 47.7%, respectively, whereas our method significantly outperforms both with an mAR of 61.4%. | p. 7 (4.3. Qualitative Results), p. 6 (Figure/Table caption) |
| Failure/limitation | Improving such limitations remains our future work. | p. 8 (5. Conclusion), p. 5 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 Given a 3D proposal and the visual encoder from Alpha-CLIP, we project the proposal onto all 2D images and select a subset of images with the highest visibility for multiscale visual feature ...를 Matching tracklets with a new observation.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Improving such limitations remains our future work.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our contributions are summarized as follows: • We carefully combine the existing concepts and refine 3D proposal generation by removing overlaps in 2D predictions and applying robust 3D tracking for aggregation. • ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Robotics-enabling 3D perception`; tags: `3D Vision, semantic`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Improving such limitations remains our future work.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Replica is a synthetic dataset created from digital replicas of real-world scenes, featuring 48 object classes across 8 different scenes..
3. Compare against the body-reported baseline or a matched simpler baseline: As reported in Table 2, our method consistently outperforms the baselines by a large margin in each experiment setting: 2D-only, 3D-only, and 2D+3D..
4. Report the body metric and its denominator/aggregation: We measure mean average precision (mAP) and mean average recall (mAR) at IOU thresholds of 25% and 50%..
5. Re-run the body-reported ablation/failure condition: Figure 4. Effectiveness of 3D proposal refinement. Red boxes indicate the object of interest, and segments of different colors de- note 3D superpoints. Without refinement, the 3D instance proposal often extends beyond ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (3.2. Open-Vocabulary Instance Classification), p. 3 (3.1. Image-based Proposal Generation), p. 5 (3.2. Open-Vocabulary Instance Classification); the primary result is directionally consistent at p. 7 (4.3. Qualitative Results), p. 6 (Figure/Table caption), p. 8 (4.4. Ablation Study); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 contributions, summarized, follows mechanism이 As reported in Table 2, our method consistently outperforms the baselines by a large margin in ... 대비 We measure mean average precision (mAP) and mean average recall (mAR) at IOU thresholds of 25% and 50%.을 개선하고, Improving such limitations remains our future work. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
