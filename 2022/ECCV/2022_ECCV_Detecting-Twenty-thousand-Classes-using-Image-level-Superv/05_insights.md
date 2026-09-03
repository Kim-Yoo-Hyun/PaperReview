# Insights — Detecting Twenty-thousand Classes using Image-level Supervision

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2201.02605; PDF retrieval source: https://arxiv.org/pdf/2201.02605. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / X. Zhou et al - extractive body cue:** This also enables our method to learn detectors for new classes which would have been impossible to predict and assign.
- **p. 1 / 1 Introduction - extractive body cue:** Object detection consists of two sub-problems - finding the object (localization) and naming it (classification).
- **p. 1 / 1 Introduction - extractive body cue:** In this paper, we propose Detector with image classes (Detic) that uses image-level supervision in addition to detection supervision.
- **p. 2 / X. Zhou et al - extractive body cue:** Experiments on the open-vocabulary LVIS [17, 18] and the open-vocabulary COCO [2] benchmarks show that our method can significantly improve over a strong box-supervised baseline, ...
- **p. 3 / X. Zhou et al - extractive body cue:** Our contributions are summarized below: - We identify issues and propose a simpler alternative to existing weaklysupervised detection techniques in the open-vocabulary setting. - Our ...
- **p. 2 / X. Zhou et al - extractive body cue:** We propose a simple classification loss that applies the image-level supervision to the proposal with the largest size, and do not supervise other outputs for ...
- **p. 5 / 3 Preliminaries - extractive body cue:** We use the region proposal network to extract N object features {(b, f, o)j}N j=1.
- **Contribution anchor:** p. 2 (X. Zhou et al), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (X. Zhou et al), p. 3 (X. Zhou et al), p. 2 (X. Zhou et al)

### Strongest assumption and failure boundary

- **p. 5 / 3 Preliminaries - extractive body cue:** In our experiments, the proposal network and the bounding box regressors are not the current performance bottleneck, as modern detectors use an over-sufficient number of ...
- **p. 1 / 1 Introduction - extractive body cue:** We observe that the localization and classification sub-problems can be decoupled.
- **p. 1 / 1 Introduction - extractive body cue:** Traditional methods tightly couple these two subproblems and thus rely on box labels for all classes.
- **p. 4 / 3 Preliminaries - extractive body cue:** We first describe the object detection problem and then detail our approach.
- **p. 4 / 3 Preliminaries - extractive body cue:** Given an image I ∈R3×h×w, object detection solves the two subproblems of (1) localization: find all objects with their location, represented as a box bj ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: Left: Standard detection requires ground-truth labeled boxes and cannot lever- age image-level labels. Center: Existing prediction-based weakly supervised detection methods [3, 44, 45] ...
- **p. 13 / X. Zhou et al - extractive body cue:** By default, a trained classifier cannot recognize novel classes.
- **Boundary to test:** Fig. 2: Left: Standard detection requires ground-truth labeled boxes and cannot lever- age image-level labels. Center: Existing prediction-based weakly supervised detection methods [3, 44, 45] use image-level labels by assigning them to ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | This also enables our method to learn detectors for new classes which would have been impossible to predict and assign. | p. 2 (X. Zhou et al), p. 1 (1 Introduction) |
| Reported outcome | Table 5: Detic with different classifiers. We vary the classifier used with Detic and observe that it works well with different choices. While CLIP embeddings give the best performance (* indicates our ... | p. 13 (Figure/Table caption), p. 26 (Figure/Table caption) |
| Failure/limitation | Fig. 2: Left: Standard detection requires ground-truth labeled boxes and cannot lever- age image-level labels. Center: Existing prediction-based weakly supervised detection methods [3, 44, 45] use image-level labels by assigning them to ... | p. 3 (Figure/Table caption), p. 13 (X. Zhou et al) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `camera/depth stream, pose, map와 language goal → robot pose, free-space/semantic map와 local goal → collision-free trajectory 또는 velocity command`.
- 이 논문의 재사용 가능한 지점은 We propose a simple classification loss that applies the image-level supervision to the proposal with the largest size, and do not supervise other outputs for imagelabeled data.를 The second stage takes the object feature and outputs a classification score and a refined box location for each object, sj = Wfj, ˆbj = Bfj + bj, where W ∈R/Cdet/×D and ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 robot pose, free-space/semantic map와 local goal가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Fig. 2: Left: Standard detection requires ground-truth labeled boxes and cannot lever- age image-level labels. Center: Existing prediction-based weakly supervised detection methods [3, 44, 45] use image-level labels by assigning them to ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: This also enables our method to learn detectors for new classes which would have been impossible to predict and assign.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `Vision-Language Model, open-vocabulary, detection, semantic`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Fig. 2: Left: Standard detection requires ground-truth labeled boxes and cannot lever- age image-level labels. Center: Existing prediction-based weakly supervised detection methods [3, 44, 45] use image-level labels by assigning them to ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We evaluate Detic on the large-vocabulary object detection dataset LVIS [18]..
3. Compare against the body-reported baseline or a matched simpler baseline: Table 11: Ablations of the resolution change. We report mask mAP on the open- vocabulary LVIS following the setting of Table 1. Top: ImageNet as the image-labeled data. Bottom: CC as the ....
4. Report the body metric and its denominator/aggregation: Fig. 2: Left: Standard detection requires ground-truth labeled boxes and cannot lever- age image-level labels. Center: Existing prediction-based weakly supervised detection methods [3, 44, 45] use image-level labels by assigning them to ....
5. Re-run the body-reported ablation/failure condition: Following ViLD [17], we remove the labels of 337 rare-class from training and consider them as novel classes in testing..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 2 (X. Zhou et al), p. 5 (3 Preliminaries), p. 6 (X. Zhou et al); the primary result is directionally consistent at p. 13 (Figure/Table caption), p. 26 (Figure/Table caption), p. 7 (5 Experiments); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 enables, learn, detectors mechanism이 Table 11: Ablations of the resolution change. We report mask mAP on the open- vocabulary LVIS ... 대비 Fig. 2: Left: Standard detection requires ground-truth labeled boxes and cannot lever- age image-level labels. Center: Existing prediction-based ...을 개선하고, Fig. 2: Left: Standard detection requires ground-truth labeled boxes and cannot lever- age image-level labels. Center: ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
