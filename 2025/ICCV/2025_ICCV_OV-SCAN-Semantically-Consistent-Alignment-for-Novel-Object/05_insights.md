# Insights — OV-SCAN: Semantically Consistent Alignment for Novel Object Discovery in Open-Vocabulary 3D Object Detection

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Chow_OV-SCAN_Semantically_Consistent_Alignment_for_Novel_Object_Discovery_in_Open-Vocabulary_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Chow_OV-SCAN_Semantically_Consistent_Alignment_for_Novel_Object_Discovery_in_Open-Vocabulary_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** We summarize our main contributions as follows: • We present OV-SCAN, an OV-3D object detector benefiting from improved cross-modal alignment, see Fig.
- **p. 2 / 1. Introduction - extractive body cue:** More specifically, we introduce the Semantically-Consistent Novel-Object Discovery (SCNOD) module to handle the inherent challenges of noisy cross-modal alignment.
- **p. 4 / 3.2. Semantically Consistent NOD (SC-NOD) - extractive body cue:** Our method relies on CLIP to classify the object into its corresponding novel class c.
- **p. 3 / 3. Method - extractive body cue:** In this section, we present the details of OV-SCAN.
- **p. 3 / 3.1. Notation and Preliminaries - extractive body cue:** Our method extends the traditional target pair of 3D bounding box and class label, into a triplet target denoted by !→= {(Bi, ci, A2D,i)}N i=1.
- **p. 4 / 3.1. Notation and Preliminaries - extractive body cue:** Cross-Modal Target Preparation 2D Image Features 3D Annotations CLIP Image Encoder Adaptive 3D Box Search Predicted Objects Selective Alignment Filter CLIP Image Encoder Adaptive 3D ...
- **p. 3 / 3.1. Notation and Preliminaries - extractive body cue:** These alignment features are then used for prompt-based classification by comparing them with text embeddings generated from class prompts, enabling fine-grained recognition of novel objects.
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.2. Semantically Consistent NOD (SC-NOD)), p. 3 (3. Method), p. 3 (3.1. Notation and Preliminaries), p. 4 (3.1. Notation and Preliminaries)

### Strongest assumption and failure boundary

- **p. 1 / 1. Introduction - extractive body cue:** Due to the aforementioned challenges with online methods, recent work has increasingly shifted toward offline approaches.
- **p. 1 / 1. Introduction - extractive body cue:** OV-3D object detection faces two main challenges: (1) novel object discovery (NOD), which involves generating 3D labels for novel objects in order to train an ...
- **p. 2 / 1. Introduction - extractive body cue:** However, existing methods often overlook common autonomous driving scenarios where objects are partially occluded (Fig.
- **p. 2 / 1. Introduction - extractive body cue:** In such cases, the 2D features become ambiguous or lack sufficient representation, leading to confusion during cross-modal alignment.
- **p. 8 / 4.4. Limitations - extractive body cue:** The primary limitation of SC-NOD is its limited annotation recovery (Fig.
- **p. 8 / 4.4. Limitations - extractive body cue:** These insights motivate future work exploring alternative methods less dependent on 2D proposals and anchor-free box-parameterization strategies.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. 3D Annotation Errors. Common 3D annotation errors during box parametrization, including but not limited to, poor L- shape fitting, misinterpreted surfaces, and misaligned ...
- **Boundary to test:** The primary limitation of SC-NOD is its limited annotation recovery (Fig.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We summarize our main contributions as follows: • We present OV-SCAN, an OV-3D object detector benefiting from improved cross-modal alignment, see Fig. | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | A simple occlusion filter with a fixed threshold ςocc yields a notable performance gain, while class-based thresholds achieve the highest improvement (+1.7 mAP). | p. 8 (4.3. Ablation Studies), p. 7 (4.2. Main Results) |
| Failure/limitation | The primary limitation of SC-NOD is its limited annotation recovery (Fig. | p. 8 (4.4. Limitations), p. 8 (4.4. Limitations) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 In addition, the proposed H2SA head effectively aligns 3D-to-2D alignment pairs by introducing a two-stage alignment process. • We validate OV-SCAN on the nuScenes [2] and KITTI [12] datasets, demonstrating that OV-SCAN ...를 In traditional LiDAR-based 3D object detection, the objective is to train a detector using inputtarget pairs D = {P, !}.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 The primary limitation of SC-NOD is its limited annotation recovery (Fig.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: We summarize our main contributions as follows: • We present OV-SCAN, an OV-3D object detector benefiting from improved cross-modal alignment, see Fig.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Robotics-enabling 3D perception`; tags: `3D Vision, semantic`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** The primary limitation of SC-NOD is its limited annotation recovery (Fig.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Our OV-3D object detection experiments are conducted on the nuScenes [2] and KITTI [12] datasets..
3. Compare against the body-reported baseline or a matched simpler baseline: OV-SCAN outperforms OV-3DET [25] and ImOV3D [42] in the overall metric, achieving comparable results to ImOV3D [42] in the car category while surpassing both in the other two classes..
4. Report the body metric and its denominator/aggregation: Figure 3. Sources of Semantic Discrepancies. (a) CLIP sim- ilarity scores for a truck reveal that occlusion cases result in an ambiguous 2D image feature. (b) CLIP similarity scores for a dis- ....
5. Re-run the body-reported ablation/failure condition: This variant removes the classification loss term, merges TransFusion-L's class heatmaps into a single class-agnostic heatmap, and replaces the text-guided alignment network with a simple feed-forward network..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (3.1. Notation and Preliminaries), p. 3 (3.1. Notation and Preliminaries), p. 5 (3.2. Semantically Consistent NOD (SC-NOD)); the primary result is directionally consistent at p. 8 (4.3. Ablation Studies), p. 7 (4.2. Main Results), p. 7 (4.2. Main Results); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summarize, main, contributions mechanism이 OV-SCAN outperforms OV-3DET [25] and ImOV3D [42] in the overall metric, achieving comparable results to ImOV3D ... 대비 Figure 3. Sources of Semantic Discrepancies. (a) CLIP sim- ilarity scores for a truck reveal that occlusion cases ...을 개선하고, The primary limitation of SC-NOD is its limited annotation recovery (Fig. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
