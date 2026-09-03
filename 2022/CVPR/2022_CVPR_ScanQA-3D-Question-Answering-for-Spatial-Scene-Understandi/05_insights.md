# Insights — ScanQA: 3D Question Answering for Spatial Scene Understanding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2112.10482; PDF retrieval source: https://arxiv.org/pdf/2112.10482. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / 1. Introduction - extractive body cue:** We introduce the new task of question answering for 3D modeling.
- **p. 2 / 1. Introduction - extractive body cue:** We present the overview of the task in Fig.
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we propose a 3D question answering (3DQA) task that uses 3D spatial information instead of 2D images to comprehend real-world information through ...
- **p. 4 / 4. ScanQA Model - extractive body cue:** We introduce the baseline model of ScanQA for the 3DQA task.
- **p. 5 / 4. ScanQA Model - extractive body cue:** This layer consists of object localization, object classification, and answer classification modules.
- **p. 4 / 4. ScanQA Model - extractive body cue:** Inspired by the architecture of deep modular co-attention networks of MCAN [51], often used for VQA, we use transformer blocks [44] to represent the relationships ...
- **p. 5 / 4. ScanQA Model - extractive body cue:** In addition, we use transformer decoder layers to represent the features of object proposals related to the question words by using the final output of ...
- **Contribution anchor:** p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (4. ScanQA Model), p. 5 (4. ScanQA Model), p. 4 (4. ScanQA Model)

### Strongest assumption and failure boundary

- **p. 1 / 1. Introduction - extractive body cue:** For example, 2D images lack an accurate sense of the relative directions and distances in the 3D scenes, i.e., the stereoscopic attribute-perception problem.
- **p. 1 / 1. Introduction - extractive body cue:** When multiple images are used in 2Dimage-based question answering models, such models often encounter difficulties in tracking and recognizing whether some objects are the same ...
- **p. 2 / 1. Introduction - extractive body cue:** are still limited in terms of dataset size and question variety because existing datasets often rely on template-based question-answer collections.
- **p. 2 / 1. Introduction - extractive body cue:** We assume that this is plausible when the model can use the preliminarily captured visual information from the 3D scene because of prior navigation in ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 5. Feature ablation results ground-truth answers. We also included sentence evalua- tion metrics frequently used for image captioning models because some of the questions ...
- **Boundary to test:** Table 5. Feature ablation results ground-truth answers. We also included sentence evalua- tion metrics frequently used for image captioning models because some of the questions had multiple possible an- swer expressions, as ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We introduce the new task of question answering for 3D modeling. | p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | The results indicated that our ScanQA method significantly outperformed all baselines across all data splits over all evaluation metrics. | p. 7 (5.2. Quantitative Analysis), p. 7 (5.2. Quantitative Analysis) |
| Failure/limitation | Table 5. Feature ablation results ground-truth answers. We also included sentence evalua- tion metrics frequently used for image captioning models because some of the questions had multiple possible an- swer expressions, as ... | p. 6 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 The 3D-QA is formalized as follows: given inputs of the point cloud p ∈P and question q ∈Q about the 3D scene, the 3D-QA model aims to output ˆa that semantically matches ...를 We project a series of output states from the LSTM using a nonlinear layer with GELUs [21] activation to obtain the contextualized word representation Q′ ∈Rnq×d, where d is the hidden size ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Table 5. Feature ablation results ground-truth answers. We also included sentence evalua- tion metrics frequently used for image captioning models because some of the questions had multiple possible an- swer expressions, as ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: We introduce the new task of question answering for 3D modeling.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `3D Vision, Vision-Language, grounding, 3D QA`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Table 5. Feature ablation results ground-truth answers. We also included sentence evalua- tion metrics frequently used for image captioning models because some of the questions had multiple possible an- swer expressions, as ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: However, as the object IDs for the test set of ScanRefer are not publicly available, we further split the validation set of ScanRefer into two-holds as the validation set and test set ....
3. Compare against the body-reported baseline or a matched simpler baseline: We compared our ScanQA model with competitive baselines VoteNet+MCAN, ScanRefer+MCAN (pipeline), and ScanRefer+MCAN (end-to-end)..
4. Report the body metric and its denominator/aggregation: Table 7. Feature ablation results on ScanQA (multiple) calization scores with the ground true boxes and consider positive predictions for the box with the highest IoU.) We observed that RGB values were ....
5. Re-run the body-reported ablation/failure condition: Table 7. Feature ablation results on ScanQA (multiple) calization scores with the ground true boxes and consider positive predictions for the box with the highest IoU.) We observed that RGB values were ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (4. ScanQA Model), p. 5 (4. ScanQA Model), p. 5 (4. ScanQA Model); the primary result is directionally consistent at p. 7 (5.2. Quantitative Analysis), p. 7 (5.2. Quantitative Analysis), p. 8 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 introduce, task, question mechanism이 We compared our ScanQA model with competitive baselines VoteNet+MCAN, ScanRefer+MCAN (pipeline), and ScanRefer+MCAN (end-to-end). 대비 Table 7. Feature ablation results on ScanQA (multiple) calization scores with the ground true boxes and consider positive ...을 개선하고, Table 5. Feature ablation results ground-truth answers. We also included sentence evalua- tion metrics frequently used ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
