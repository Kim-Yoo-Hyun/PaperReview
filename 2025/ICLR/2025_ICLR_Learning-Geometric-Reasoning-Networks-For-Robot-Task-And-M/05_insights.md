# Insights — Learning Geometric Reasoning Networks For Robot Task And Motion Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2025/hash/561dd71d04695c85e1c0f6a0fbe0bd85-Abstract-Conference.html; PDF retrieval source: https://openreview.net/pdf/4c142fb0625912332eff11ad284991e6692f7016.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA2 targeted source review: 2026-10-23; PDF pp. 4. 손상 구간·직접 연결된 표 분류만 원문 이미지와 대조했다. 전체 주장 정독·실험 검증·reading status 승격을 뜻하지 않는다. [URL·PDF hash·수정 기록](../../../work/sources/pdf_note_review_followup_2026-10-23.json).

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 INTRODUCTION - extractive body cue:** The contributions of this paper are threefold: (1) We propose a novel GNN-based model for efficient and accurate action and grasp feasibility prediction in complex ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** To address these limitations, we propose a novel approach that leverages a GNN-based model for robot action and grasp feasibility prediction.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Our method constructs a graph representation of 3D environments, where fixed and movable objects are represented as nodes, and edges capture spatial relationships and interaction ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** (3) We provide comprehensive experiments showcasing our method's state-of-the-art (SOTA) performance, including evaluations of its interpretability and generalization capabilities.
- **PDF p. 4, §3 / Eq. (2) (DOC-QA2 원문 대조):** GRN은 feasibility classifier f_F와 IK classifier f_κ, obstruction regressor f_ρ를 학습한다. f_F는 object/environment와 예측 κ_G, ρ_G를 사용해 action·grasp feasibility 벡터 [F_a,F_G]ᵀ를 출력한다.
- **p. 14 / A IMPLEMENTATION DETAILS - extractive body cue:** Exceptionally, when training on the PR2-3D-4 dataset, we use a hidden size of 256 for the GO module as it yields better results.
- **p. 14 / A IMPLEMENTATION DETAILS - extractive body cue:** During the pre-training stage, each module is trained for 100 epochs.
- **Contribution anchor:** p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 14 (A IMPLEMENTATION DETAILS)

### Strongest assumption and failure boundary

- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, action feasibility prediction presents several challenges.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** These methods, however, lack interpretability and can not provide feedback on why actions are infeasible.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Later, multi-modal motion planning (Hauser & Latombe, 2010; Hauser & Ng-Thow-Hing, 2011) generalized these methods using constraint-based graphs, but the complexity of constructing these graphs ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Existing approaches to action feasibility prediction often struggle with interpretability, scalability, and generalization across diverse environments.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** These interpretable features not only allow us to predict action infeasibility, they also explain why a specific action fails, enabling more efficient planning.
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 5: Annotations statistics for the Panda-3D-4 training set. (a) Number of feasible and infeasi- ble actions (b) Number of feasible and infeasi- ble cases ...
- **p. 8 / 6 RESULTS - extractive body cue:** CNN-based methods, DVH and AGFP-Net, fall short compared to our approach, with a difference in F1 score on the Panda-3D-4 of 10% (resp.
- **Boundary to test:** Figure 5: Annotations statistics for the Panda-3D-4 training set. (a) Number of feasible and infeasi- ble actions (b) Number of feasible and infeasi- ble cases per grasp type (c) Distribution of failure ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | The contributions of this paper are threefold: (1) We propose a novel GNN-based model for efficient and accurate action and grasp feasibility prediction in complex 3D environments. | p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |
| Reported outcome | The results show that GRN achieves a better performance than the state-of-the-art on robots with various kinematics. | p. 9 (6 RESULTS), p. 8 (6 RESULTS) |
| Failure/limitation | Figure 5: Annotations statistics for the Panda-3D-4 training set. (a) Number of feasible and infeasi- ble actions (b) Number of feasible and infeasi- ble cases per grasp type (c) Distribution of failure ... | p. 16 (Figure/Table caption), p. 8 (6 RESULTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- **Researcher interpretation (DOC-QA2):** PDF p. 4 Eq. (2)의 IK·obstruction 예측이 action/grasp feasibility 판단에 주는 효과를 분리해 비교할 수 있다. 입력 graph와 supervision을 고정한 ablation이 필요하며, 해당 식이나 annotation 통계만으로 feedback/recovery 효과를 주장하지 않는다.
- The paper-specific mechanism to preserve in a reproduction is: The contributions of this paper are threefold: (1) We propose a novel GNN-based model for efficient and accurate action and grasp feasibility prediction in complex 3D environments.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- 현재 등급·주 트랙·태그는 [논문 개요](./01_overview.md)에서 확인한다.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 5: Annotations statistics for the Panda-3D-4 training set. (a) Number of feasible and infeasi- ble actions (b) Number of feasible and infeasi- ble cases per grasp type (c) Distribution of failure ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Panda-3D-4: This is dataset is composed of 3D environments containing 4 movable objects, 1 to 4 structures and 0 to 4 obstacles and is annotated using a Panda robot..
3. Compare against the body-reported baseline or a matched simpler baseline: 6.1 COMPARISON TO PRIOR WORK Table 1 shows that our proposed model outperforms all prior works on both action feasibility and grasp types feasibility predictions, and on all datasets..
4. Report the body metric and its denominator/aggregation: Comparing the standard deviations across F1 scores of each grasp type shows that our proposed method has a more consistent performance across the different grasp types than other models..
5. Re-run the body-reported ablation/failure condition: We conduct two ablations to demonstrate the effectiveness of our training strategy..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 14 (A IMPLEMENTATION DETAILS), p. 14 (A IMPLEMENTATION DETAILS); the primary result is directionally consistent at p. 9 (6 RESULTS), p. 8 (6 RESULTS), p. 9 (6 RESULTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 contributions, threefold, novel mechanism이 6.1 COMPARISON TO PRIOR WORK Table 1 shows that our proposed model outperforms all prior works ... 대비 Comparing the standard deviations across F1 scores of each grasp type shows that our proposed method has a ...을 개선하고, Figure 5: Annotations statistics for the Panda-3D-4 training set. (a) Number of feasible and infeasi- ble ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
