# Insights — FM-Fusion: Instance-aware Semantic Mapping Boosted by Vision-Language Foundation Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2402.04555; PDF retrieval source: https://arxiv.org/pdf/2402.04555. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / I. INTRODUCTION - extractive body cue:** Our method incrementally fuses the object detections from foundation models into an instance-aware semantic map.
- **p. 2 / I. INTRODUCTION - extractive body cue:** To address such challenges, we propose a probabilistic label fusion method following the Bayes filter algorithm.
- **p. 6 / 6 Method - extractive body cue:** Compared with Kimera using RAM-GroundedSAM, our method achieved +15.6 mAP50.
- **p. 6 / 6 Method - extractive body cue:** The rest of the ScanNet experiment focus on evaluating each module of our method through an ablation study.
- **p. 7 / 6 Method - extractive body cue:** As shown in Figure 10(b), our method detects the table correctly.
- **p. 6 / 6 Method - extractive body cue:** Our instance refinement module merges over-segmented instances caused by inconsistent instance masks at changed viewpoints.
- **p. 7 / 6 Method - extractive body cue:** We consider those limitations of foundation models.
- **Contribution anchor:** p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 6 (6 Method), p. 6 (6 Method), p. 7 (6 Method), p. 6 (6 Method)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** However, the supervised object detectors are trained in specific data distribution and lack generalization ability.
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, these challenges have not been considered in traditional semantic mapping works.
- **p. 2 / I. INTRODUCTION - extractive body cue:** IEEE ROBOTICS AND AUTOMATION LETTERS, VOL.9, NO.3, MARCH 2024 2 challenges should be addressed.
- **p. 1 / I. INTRODUCTION - extractive body cue:** All of these foundation models are trained using large-scale data and demonstrate strong zero-shot generalization ability in various image distributions.
- **p. 7 / 6 Method - extractive body cue:** As shown in Figure 10(a), RAM fails to recognize a table due to the extreme viewpoint, and GroundingDINO cannot detect it either.
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 6: The visualization shows instance voxel grid map (a) before and (b) after the merge. The inconsistent instance mask is a natural limitation for ...
- **p. 7 / 6 Method - extractive body cue:** We consider those limitations of foundation models.
- **Boundary to test:** As shown in Figure 10(a), RAM fails to recognize a table due to the extreme viewpoint, and GroundingDINO cannot detect it either.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our method incrementally fuses the object detections from foundation models into an instance-aware semantic map. | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Reported outcome | Even for those predictable semantic classes, the pretrained Mask R-CNN suffers from the issue of generalization and achieve low AP50 scores. | p. 5 (V. EXPERIMENT), p. 5 (V. EXPERIMENT) |
| Failure/limitation | As shown in Figure 10(a), RAM fails to recognize a table due to the extreme viewpoint, and GroundingDINO cannot detect it either. | p. 7 (6 Method), p. 5 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `camera/depth stream, pose, map와 language goal → robot pose, free-space/semantic map와 local goal → collision-free trajectory 또는 velocity command`.
- The paper-specific mechanism to preserve in a reproduction is: Our method incrementally fuses the object detections from foundation models into an instance-aware semantic map.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Robotics-enabling 3D perception`; tags: `Vision-Language Model, semantic`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** As shown in Figure 10(a), RAM fails to recognize a table due to the extreme viewpoint, and GroundingDINO cannot detect it either.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We chose the public dataset ScanNet and SceneNN to evaluate the semantic mapping quality..
3. Compare against the body-reported baseline or a matched simpler baseline: We compared our method with Kimera 2 and a selfimplemented Fusion++..
4. Report the body metric and its denominator/aggregation: Even for those predictable semantic classes, the pretrained Mask R-CNN suffers from the issue of generalization and achieve low AP50 scores..
5. Re-run the body-reported ablation/failure condition: Fig. 10: An image of object detection from Ablation-B and our method are shown in (a) and (b). The labels incorporated by text prompt augmentation are highlighted in red. The images are ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 6 (6 Method), p. 6 (6 Method), p. 7 (6 Method); the primary result is directionally consistent at p. 5 (V. EXPERIMENT), p. 5 (V. EXPERIMENT), p. 8 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 incrementally, fuses, object mechanism이 We compared our method with Kimera 2 and a selfimplemented Fusion++. 대비 Even for those predictable semantic classes, the pretrained Mask R-CNN suffers from the issue of generalization and achieve ...을 개선하고, As shown in Figure 10(a), RAM fails to recognize a table due to the extreme viewpoint, ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
