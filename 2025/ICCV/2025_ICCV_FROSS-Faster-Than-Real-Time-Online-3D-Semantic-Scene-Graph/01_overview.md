# FROSS: Faster-Than-Real-Time Online 3D Semantic Scene Graph Generation from RGB-D Images

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (5 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Hou_FROSS_Faster-Than-Real-Time_Online_3D_Semantic_Scene_Graph_Generation_from_RGB-D_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Hou_FROSS_Faster-Than-Real-Time_Online_3D_Semantic_Scene_Graph_Generation_from_RGB-D_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: Hao-Yu Hou, Chun-Yi Lee, Motoharu Sonogashira, Yasutomo Kawanishi
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Vision, Graph Reasoning, semantic
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Hou_FROSS_Faster-Than-Real-Time_Online_3D_Semantic_Scene_Graph_Generation_from_RGB-D_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Hou_FROSS_Faster-Than-Real-Time_Online_3D_Semantic_Scene_Graph_Generation_from_RGB-D_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (5 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

FROSS는 순차 RGB-D 영상에서 얻은 2차원 장면 그래프를 3차원으로 올려 물체와 관계를 온라인으로 갱신한다. [PDF 1쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Hou_FROSS_Faster-Than-Real-Time_Online_3D_Semantic_Scene_Graph_Generation_from_RGB-D_ICCV_2025_paper.pdf#page=1)

## Problem and Motivation

- **p. 1 / Body text (section not recovered) - extractive body cue:** FROSS: Faster-than-Real-Time Online 3D Semantic Scene Graph Generation from RGB-D Images Supplementary Material
- **p. 1 / 6. Detailed Evaluation Metric - extractive body cue:** The evaluation procedure in this paper follows closely with Wu [35] to ensure a fair comparison.
- **p. 1 / 6. Detailed Evaluation Metric - extractive body cue:** The only difference is the exclusion of the ‘none' relationship category, as FROSS does not predict it.
- **p. 1 / 6. Detailed Evaluation Metric - extractive body cue:** Wu [35] also provided results evaluated under this protocol in their publicly released code.
- **p. 1 / 6. Detailed Evaluation Metric - extractive body cue:** Specifically, for a detected triplet in which both the subject and object match ground truth objects, only the predicted class labels for the subject, object, ...

## Core Idea

- **p. 2 / 7.3. 2D Scene Graph Generation Performance - extractive body cue:** In this section, we present the evaluation of two models: the original EGTR [12] 2D SG generation model and our modified version employed in FROSS, ...
- **p. 3 / 8. Statistics of the ReplicaSSG Dataset - extractive body cue:** Evaluation results of two 2D SG generation models across three datasets. ‘RT-DETR+EGTR' represents the EGTR model with RT-DETR as its object detector backbone.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | FROSS: Faster-than-Real-Time Online 3D Semantic Scene Graph Generation from RGB-D Images Supplementary Material | camera/depth stream, pose, map와 language goal | p. 1 (Body text (section not recovered)), p. 2 (8. Statistics of the ReplicaSSG Dataset) |
| State/latent | FROSS, Faster-than-Real-Time, Online, Semantic, Scene, Graph, Generation, RGB-D, Images, Supplementary, Material, statistics | robot pose, free-space/semantic map와 local goal | p. 1 (Body text (section not recovered)), p. 2 (8. Statistics of the ReplicaSSG Dataset), p. 3 (8. Statistics of the ReplicaSSG Dataset) |
| Output/action | The statistics of the proposed ReplicaSSG Dataset are presented in Figures 6-9. | collision-free trajectory 또는 velocity command | p. 2 (8. Statistics of the ReplicaSSG Dataset) |
| Objective/outcome | All relationship metrics are evaluated with graph constraints as described in [38]. | goal reach, safety, localization error와 replanning latency | p. 3 (8. Statistics of the ReplicaSSG Dataset) |

## Main Claims and Actual Contribution

- 물체를 3차원 Gaussian 분포로 나타내고 다른 프레임에서 관측한 물체와 관계를 기존 그래프에 연결한다. [PDF 3쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Hou_FROSS_Faster-Than-Real-Time_Online_3D_Semantic_Scene_Graph_Generation_from_RGB-D_ICCV_2025_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Hou_FROSS_Faster-Than-Real-Time_Online_3D_Semantic_Scene_Graph_Generation_from_RGB-D_ICCV_2025_paper.pdf#page=4)
- Replica에 물체 간 관계 주석을 추가한 ReplicaSSG를 만들고 3DSSG와 함께 그래프 정확도와 처리 시간을 평가했다. [PDF 5쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Hou_FROSS_Faster-Than-Real-Time_Online_3D_Semantic_Scene_Graph_Generation_from_RGB-D_ICCV_2025_paper.pdf#page=5) · [PDF 7쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Hou_FROSS_Faster-Than-Real-Time_Online_3D_Semantic_Scene_Graph_Generation_from_RGB-D_ICCV_2025_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Hou_FROSS_Faster-Than-Real-Time_Online_3D_Semantic_Scene_Graph_Generation_from_RGB-D_ICCV_2025_paper.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 2 (7.3. 2D Scene Graph Generation Performance), p. 2 (Figure/Table caption) |
| Embodiment/environment | Qualitative results of FROSS on four scenes in the ReplicaSSG dataset. | hardware/simulator version and reset protocol | p. 2 (7.1. Object and Predicate Performance per Class), p. 5 (8. Statistics of the ReplicaSSG Dataset) |
| Dataset/benchmark | For these evaluations, the models tested on ReplicaSSG received training on the Visual Genome dataset, whereas the models tested on the other two datasets used their respective training splits. | role, split, size and leakage | p. 2 (7.1. Object and Predicate Performance per Class), p. 5 (8. Statistics of the ReplicaSSG Dataset), p. 2 (7.3. 2D Scene Graph Generation Performance), p. 1 (7.1. Object and Predicate Performance per Class) |
| Metric | Specifically, for a detected triplet in which both the subject and object match ground truth objects, only the predicted class labels for the subject, object, and predicate with the highest confidence scores ... | definition, denominator, direction and uncertainty | p. 1 (6. Detailed Evaluation Metric), p. 1 (7.1. Object and Predicate Performance per Class), p. 2 (7.2. Additional Qualitative Results) |
| Baseline/ablation | The per-class performance comparison of FROSS and other baselines is presented in Tables 6 and 7. | fair input/data/compute/action matching | p. 1 (7.1. Object and Predicate Performance per Class), p. 1 (7.1. Object and Predicate Performance per Class), p. 3 (8. Statistics of the ReplicaSSG Dataset) |

## Explicit Limitations and Failure Boundary

- **p. 1 / 6. Detailed Evaluation Metric - extractive body cue:** The only difference is the exclusion of the ‘none' relationship category, as FROSS does not predict it.
- **p. 1 / 7.1. Object and Predicate Performance per Class - extractive body cue:** While addressing this issue could potentially enhance FROSS's performance, we leave it as future work, as class imbalance is not the primary focus of this ...
- **p. 2 / 7.2. Additional Qualitative Results - extractive body cue:** These results further demonstrate FROSS's robustness in diverse scene conditions.
- **p. 2 / 7.2. Additional Qualitative Results - extractive body cue:** Misclassified objects are likely caused by occlusions from certain viewpoints or unusual viewing angles.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 3 (8. Statistics of the ReplicaSSG Dataset), p. 2 (7.3. 2D Scene Graph Generation Performance), p. 2 (Figure/Table caption), p. 1 (7.1. Object and Predicate Performance per Class), p. 3 (Figure/Table caption)이다.
