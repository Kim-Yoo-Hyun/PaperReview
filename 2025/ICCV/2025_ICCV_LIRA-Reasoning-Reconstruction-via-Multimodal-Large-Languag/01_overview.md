# LIRA: Reasoning Reconstruction via Multimodal Large Language Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_LIRA_Reasoning_Reconstruction_via_Multimodal_Large_Language_Models_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhou_LIRA_Reasoning_Reconstruction_via_Multimodal_Large_Language_Models_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: Zhen Zhou, Tong Wang, Yunkai Ma, Xiao Tan, Fengshui Jing
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision, Vision-Language, 3D reconstruction
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_LIRA_Reasoning_Reconstruction_via_Multimodal_Large_Language_Models_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhou_LIRA_Reasoning_Reconstruction_via_Multimodal_Large_Language_Models_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 원문 해당 쪽과 대조했다. [본문](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhou_LIRA_Reasoning_Reconstruction_via_Multimodal_Large_Language_Models_ICCV_2025_paper.pdf)

## Why This Paper Is Here

LIRA는 실내 RGB-D 영상을 보면서 암시적인 지시가 가리키는 물체를 추론하고 그 물체의 3D 지도를 점진적으로 복원한다. [PDF 1쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhou_LIRA_Reasoning_Reconstruction_via_Multimodal_Large_Language_Models_ICCV_2025_paper.pdf#page=1) · [PDF 3쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhou_LIRA_Reasoning_Reconstruction_via_Multimodal_Large_Language_Models_ICCV_2025_paper.pdf#page=3)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Existing language instruction-guided online 3D reconstruction systems mainly rely on explicit instructions or queryable maps, showing inadequate capability to handle implicit and complex instructions.
- **p. 1 / Abstract - extractive body cue:** In this paper, we first introduce a reasoning reconstruction task.
- **p. 1 / Abstract - extractive body cue:** This task inputs an implicit instruction involving complex reasoning and an RGB-D sequence, and outputs incremental 3D reconstruction of instances that conform to the instruction.
- **p. 1 / Abstract - extractive body cue:** To handle this task, we propose LIRA: Language Instructed Reconstruction Assistant.
- **p. 1 / Abstract - extractive body cue:** It leverages a multimodal large language model to actively reason about the implicit instruction and obtain instruction-relevant 2D candidate instances and their attributes.
- **p. 1 / 1. Introduction - extractive body cue:** However, existing systems [15, 27, 46, 47] mainly rely on explicit instructions, such as explicitly indicating target objects or categories, to reconstruct instruction-relevant regions, while ...
- **p. 2 / 1. Introduction - extractive body cue:** Particularly for implicit instructions involving complex reasoning, they are more difficult to handle.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our major contributions are as follows: • We introduce the reasoning reconstruction task, which requires online 3D reconstruction guided by implicit and complex ...
- **p. 2 / 1. Introduction - extractive body cue:** To achieve higher-quality instance fusion, we propose TIFF, a Text-enhanced Instance Fusion module operating within a Fragment bounding volume (FBV), which is learning-based and fuses ...
- **p. 4 / 3.1.2. 2D Reasoning Segmentation within the FBV - extractive body cue:** (3) Then, fimg and ˆhseg (text feature prompt) are input into the mask decoder Fdec of the segmentation foundation model to output the binary mask ...
- **p. 7 / 4.5. Runtime Analysis - extractive body cue:** To achieve real-time inference, we propose LIRA-Fast.
- **p. 4 / 3.1.2. 2D Reasoning Segmentation within the FBV - extractive body cue:** The image features directly use the image embeddings fimg of the segmentation foundation model in the 2D reasoning segmentation module.
- **p. 5 / 3.1.2. 2D Reasoning Segmentation within the FBV - extractive body cue:** Current Instances Global Instances Mask Confidence Branch Similarity Matrix Calculation x y z w h l 3D Bounding Boxes Masked Cross-Attention MLP Add & Norm ...
- **p. 7 / 4.4. Explicit Instruction-Guided Reconstruction - extractive body cue:** For example, an inStage Method AP AP50 AP25 I Replace with SEEM [59] 3.68 11.00 19.57 Replace with Grounded-SAM [25] 3.06 10.12 18.26 Replace with ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Given an implicit and complex instruction L and posed RGB-D sequences as input, LIRA first incrementally performs geometric reconstruction, and leverages a MLLM to actively reason about L and obtain instruction-relevant 2D ... | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (3. Method), p. 4 (3.1.2. 2D Reasoning Segmentation within the FBV) |
| State/latent | Given, implicit, complex, instruction, posed, RGB-D, sequences, input, LIRA, first, incrementally, performs | geometry, map, object/relationship state | p. 3 (3. Method), p. 4 (3.1.2. 2D Reasoning Segmentation within the FBV), p. 1 (1. Introduction) |
| Output/action | An image can only provide instance information within a local field of view, and the complex language instruction requires reasoning based on the global map. | point map, pose, scene graph, affordance 또는 query result | p. 4 (3.1.2. 2D Reasoning Segmentation within the FBV), p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Objective/outcome | The perceptual information is progressively constructed into a global map containing multiple candidate instances in the brain. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 3 (3. Method), p. 4 (3.1.2. 2D Reasoning Segmentation within the FBV), p. 4 (3.1.1. Incremental Geometric Reconstruction) |

## Main Claims and Actual Contribution

- 2차원 후보 마스크를 3D로 역투영한 뒤 TIFF가 여러 키프레임의 언어·기하 단서를 함께 사용해 동일 인스턴스를 병합한다. [PDF 3쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhou_LIRA_Reasoning_Reconstruction_via_Multimodal_Large_Language_Models_ICCV_2025_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhou_LIRA_Reasoning_Reconstruction_via_Multimodal_Large_Language_Models_ICCV_2025_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhou_LIRA_Reasoning_Reconstruction_via_Multimodal_Large_Language_Models_ICCV_2025_paper.pdf#page=5)
- ReasonRecon에 장면과 추론이 필요한 지시를 연결하고, 명시적 지시와 암시적 지시에서 목표 물체 복원 성능을 비교했다. [PDF 6쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhou_LIRA_Reasoning_Reconstruction_via_Multimodal_Large_Language_Models_ICCV_2025_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhou_LIRA_Reasoning_Reconstruction_via_Multimodal_Large_Language_Models_ICCV_2025_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhou_LIRA_Reasoning_Reconstruction_via_Multimodal_Large_Language_Models_ICCV_2025_paper.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Embodiment/environment | To establish a comprehensive evaluation system suitable for the reasoning reconstruction task, a benchmark ReasonRecon is constructed and the data collection pipeline is shown in Fig. | hardware/simulator version and reset protocol | p. 5 (3.4. Benchmark), p. 6 (3.4. Benchmark) |
| Dataset/benchmark | The training set and test set are divided into 8: 2. | role, split, size and leakage | p. 5 (3.4. Benchmark), p. 6 (3.4. Benchmark), p. 6 (3.4. Benchmark), p. 5 (3.4. Benchmark) |
| Metric | We evaluate using standard Average Precision (AP) metrics at IoU thresholds of 50% and 25%, and also calculate mean score across IoU thresholds from 50% to 95% in 5% increments. | definition, denominator, direction and uncertainty | p. 6 (4.2. Evaluation Metrics), p. 7 (Figure/Table caption), p. 7 (4.5. Runtime Analysis) |
| Baseline/ablation | Table 4. Runtime analysis of reasoning reconstruction. comparison. VLMaps is extended to a 3D map by can- celing top-down projection. LIRA* represents that LIRA uses LLaVA-13B and applies ChatGPT-4o for reasoning in ... | fair input/data/compute/action matching | p. 7 (Figure/Table caption), p. 7 (4.5. Runtime Analysis), p. 8 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** One limitation is that LIRA exhibits relatively low performance in high-precision reconstruction.
- **p. 8 / 5. Conclusion - extractive body cue:** Future work will consider further optimization in 3D space.
- **p. 6 / 3.4. Benchmark - extractive body cue:** Erroneous projected pixels caused by occlusion are filtered out.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.1.2. 2D Reasoning Segmentation within the FBV), p. 7 (4.5. Runtime Analysis)이다.

## 검색 태그 근거

RGB-D 스트림에서 언어모델로 간접 지시를 해석해 후보를 만들고 시점별 인스턴스를 점진적으로 합친다. 참조 물체 분할과 대상의 3D 복원을 평가했다. [원문 3쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhou_LIRA_Reasoning_Reconstruction_via_Multimodal_Large_Language_Models_ICCV_2025_paper.pdf#page=3) · [원문 7쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhou_LIRA_Reasoning_Reconstruction_via_Multimodal_Large_Language_Models_ICCV_2025_paper.pdf#page=7)
