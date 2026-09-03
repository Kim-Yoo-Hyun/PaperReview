# Insights — OpenMask3D: Open-Vocabulary 3D Instance Segmentation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2306.13631; PDF retrieval source: https://arxiv.org/pdf/2306.13631. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 Introduction - extractive body cue:** Our contributions are three-fold: • We introduce the open-vocabulary 3D instance segmentation task in which the object instances that are similar to a given text-query ...
- **p. 2 / 1 Introduction - extractive body cue:** Our approach is intrinsically different from the existing 3D open-vocabulary scene understanding approaches [24, 32, 52] as we propose an instance-based feature computation approach instead ...
- **p. 4 / 3 Method - extractive body cue:** Our pipeline consists of four subsequent steps: 1⃝Our approach takes as input posed RGB-D images of a 3D indoor scene along with its reconstructed point ...
- **p. 3 / 3 Method - extractive body cue:** The key novelty of our method is that it follows an instance-mask oriented approach, contrary to existing 3D open-vocabulary scene understanding models which typically compute ...
- **p. 4 / 3 Method - extractive body cue:** 3, the mask-feature computation module consists of several steps.
- **p. 4 / 3 Method - extractive body cue:** The architecture consists of a sparse convolutional backbone based on the MinkowskiUNet [9], and a transformer decoder.
- **p. 7 / Model - extractive body cue:** In order to compute image features on the mask-crops, we use CLIP [55] visual encoder from the ViT-L/14 model pre-trained at a 336 pixel resolution, ...
- **Contribution anchor:** p. 2 (1 Introduction), p. 2 (1 Introduction), p. 4 (3 Method), p. 3 (3 Method), p. 4 (3 Method), p. 4 (3 Method)

### Strongest assumption and failure boundary

- **p. 2 / 1 Introduction - extractive body cue:** Hence, the second key problem with closed-vocabulary approaches is their inherent limitation to recognize only object classes that are predefined at training time.
- **p. 2 / 1 Introduction - extractive body cue:** In an attempt to address and overcome the limitations of a closed-vocabulary setting, there has been a growing interest in open-vocabulary approaches.
- **p. 1 / 1 Introduction - extractive body cue:** We argue that there are two key problems with closed-vocabulary 3D instance segmentation.
- **p. 18 / Figure/Table caption - extractive body cue:** Figure 9: Output of SAM, using only 5 randomly sampled points (visualized as green dots) of the projected 3D mask as input. A.2.4 Why do ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: 3D instance segmentation results on the ScanNet200 validation set. Metrics are respectively: AP averaged over an overlap range, and AP evaluated at 50% ...
- **p. 18 / Figure/Table caption - extractive body cue:** Figure 10: Output of SAM, using only 5 randomly sampled points of the mask as input. Here the sampled points (the green points visualized in ...
- **p. 17 / Figure/Table caption - extractive body cue:** Figure 7: Difference between the bounding boxes obtained by tightly cropping around the projected points from the 3D instance mask (left), and the bounding box ...
- **Boundary to test:** Figure 9: Output of SAM, using only 5 randomly sampled points (visualized as green dots) of the projected 3D mask as input. A.2.4 Why do we need to run SAM for multiple ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our contributions are three-fold: • We introduce the open-vocabulary 3D instance segmentation task in which the object instances that are similar to a given text-query are identified. • We propose OpenMask3D, which ... | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Reported outcome | Figure 10: Output of SAM, using only 5 randomly sampled points of the mask as input. Here the sampled points (the green points visualized in the image) are concentrated in a small ... | p. 18 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Failure/limitation | Figure 9: Output of SAM, using only 5 randomly sampled points (visualized as green dots) of the projected 3D mask as input. A.2.4 Why do we need to run SAM for multiple ... | p. 18 (Figure/Table caption), p. 7 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `camera/depth stream, pose, map와 language goal → robot pose, free-space/semantic map와 local goal → collision-free trajectory 또는 velocity command`.
- 이 논문의 재사용 가능한 지점은 Our pipeline takes as input a collection of posed RGB-D images captured in an indoor scene, and the reconstructed point cloud representation of the scene.를 3.2.3 CLIP feature extraction and mask-feature aggregation For each instance mask, we collect k ⋅L images by selecting top-k views and obtaining L multi-level crops as described in Sec.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 robot pose, free-space/semantic map와 local goal가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Figure 9: Output of SAM, using only 5 randomly sampled points (visualized as green dots) of the projected 3D mask as input. A.2.4 Why do we need to run SAM for multiple ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our contributions are three-fold: • We introduce the open-vocabulary 3D instance segmentation task in which the object instances that are similar to a given text-query are identified. • We propose OpenMask3D, which ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `open-vocabulary, 3D segmentation, CLIP`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 9: Output of SAM, using only 5 randomly sampled points (visualized as green dots) of the projected 3D mask as input. A.2.4 Why do we need to run SAM for multiple ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: To assess the generalization capability of our method, we further experiment with the Replica [61] dataset, and evaluate on the office0, office1, office2, office3, office4, room0, room1, room2 scenes..
3. Compare against the body-reported baseline or a matched simpler baseline: Table 5: 3D instance segmentation results on the ScanNet200 validation set, using oracle masks. We use ground truth instance masks for computing the per-mask features. We also report results from the fully- ....
4. Report the body metric and its denominator/aggregation: Figure 10: Output of SAM, using only 5 randomly sampled points of the mask as input. Here the sampled points (the green points visualized in the image) are concentrated in a small ....
5. Re-run the body-reported ablation/failure condition: Table 7: Ablation study of the multi-scale cropping hyperparameters on the Replica dataset. We analyze the effect of varying number of levels, and the ratio of expansion. B.2 Evaluation on Replica without ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (3 Method), p. 7 (Model), p. 4 (3 Method); the primary result is directionally consistent at p. 18 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 contributions, three-fold, introduce mechanism이 Table 5: 3D instance segmentation results on the ScanNet200 validation set, using oracle masks. We use ... 대비 Figure 10: Output of SAM, using only 5 randomly sampled points of the mask as input. Here the ...을 개선하고, Figure 9: Output of SAM, using only 5 randomly sampled points (visualized as green dots) of ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
