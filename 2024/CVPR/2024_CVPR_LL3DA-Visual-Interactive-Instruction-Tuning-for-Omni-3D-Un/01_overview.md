# LL3DA: Visual Interactive Instruction Tuning for Omni-3D Understanding, Reasoning, and Planning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2311.18651.
> PDF retrieval source: https://arxiv.org/pdf/2311.18651. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CVPR
- Authors: Sijin Chen, Xin Chen, Chi Zhang, Mingsheng Li, Gang Yu, Hao Fei, Hongyuan Zhu, Jiayuan Fan, Tao Chen
- Primary track: Planning and control
- Tier: ARCHIVE
- Tags: LLM, 3D Vision, 3D reasoning
- Official paper: https://arxiv.org/abs/2311.18651
- Full-text retrieval: https://arxiv.org/pdf/2311.18651
- Code/Project: https://github.com/Open3DA/LL3DA
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

LL3DA는 점군과 사용자의 언어·시각 지시를 받아 3D 장면에 대한 텍스트를 생성한다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Recent advances in Large Multimodal Models (LMM) have made it possible for various applications in humanmachine interactions.
- **p. 1 / Abstract - extractive body cue:** However, developing LMMs that can comprehend, reason, and plan in complex and diverse 3D environments remains a challenging topic, especially considering the demand for understanding ...
- **p. 1 / Abstract - extractive body cue:** Existing works seek help from multi-view images, and project 2D features to 3D space as 3D scene representations.
- **p. 1 / Abstract - extractive body cue:** This, however, leads to huge computational overhead and performance degradation.
- **p. 1 / Abstract - extractive body cue:** In this paper, we present LL3DA, a Large Language 3D Assistant that takes point cloud as direct input and respond to both textualinstructions and visual-prompts.
- **p. 2 / 1. Introduction - extractive body cue:** Though these methods have achieved remarkable success addressing different challenges in understanding 3D worlds with natural language, there are certain limitations.
- **p. 1 / 1. Introduction - extractive body cue:** During this LLM carnival, researchers are also seeking generalized LLM solutions to various vision language tasks [16, 54, 59].

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** To summarize, our key contributions lie in: • We present a LLM-based solution for understanding, reasoning, and planning in complex 3D environments. • Our model ...
- **p. 2 / 1. Introduction - extractive body cue:** Additionally, by introducing additional visual interactions, our method could further remove the ambiguities within the vague textual instructions.
- **p. 3 / 3. Methodology - extractive body cue:** Next, we introduce our model design in details (Sec.
- **p. 3 / 3.1. Problem Formatting - extractive body cue:** 2 (a), the input of our model consists of a 3D scene represented by a set of points PC, the textual instruction It, and potential ...
- **p. 4 / 3.2. Model Design - extractive body cue:** (1) Here, fenc consists of d-dimensioned features for M points uniformly down-sampled from the input 3D scene through the Farthest Point Sampling (FPS) algorithm.
- **p. 3 / 3.2. Model Design - extractive body cue:** 2 (b), which consists of a frozen 3D scene encoder E3D, a visual prompt encoder, and a Q-Former to transform the permutation-invariant 3D embeddings into ...
- **p. 4 / 3.2. Model Design - extractive body cue:** We consider the decoder-only generative pre-trained transformers [49, 58] as our large language model backbone, which are sensitive to the input orders because of the ...

## Observation, State, and Output Interface

| 항목 | 원문에서 확인한 범위 |
|---|---|
| 입력 | 장면 점군, 자연어와 선택적 클릭·상자 |
| 표현 | 장면과 사용자 위치 지시를 인코딩한 토큰 |
| 출력 | 장면 설명·질문 답변·텍스트 과제 계획 |
| 평가 | 장면 단위 지시 수행과 3D 질문 응답 |

[방법 3쪽](https://arxiv.org/pdf/2311.18651#page=3) · [평가 6쪽](https://arxiv.org/pdf/2311.18651#page=6)

## Main Claims and Actual Contribution

- 장면의 점군을 직접 입력받고 시각적 단서로 어떤 물체를 가리키는지 지정한다.
- 출력을 3D 장면 설명과 시각 질의응답에서 평가한다.

[원문 초록](https://arxiv.org/abs/2311.18651)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 5 (5.2. Comparison with SoTA Specialists), p. 7 (5.3. Ablation Studies) |
| Embodiment/environment | In this paper, we experiment with 3D data from ScanNet [15], a 3D dataset covering 1,201 and 312 diverse and complex indoor 3D scenes for training and validation. | hardware/simulator version and reset protocol | p. 5 (5. Experiments), p. 5 (5.2. Comparison with SoTA Specialists) |
| Dataset/benchmark | However, the generalist model achieves poor results on Nr3D [1], which is because we did not try to differentiate between Nr3D and ScanRefer during training as these two datasets are used for ... | role, split, size and leakage | p. 5 (5. Experiments), p. 5 (5.2. Comparison with SoTA Specialists), p. 7 (5.3. Ablation Studies), p. 6 (5.3. Ablation Studies) |
| Metric | Here, m ∈{C, B-4, M, R}, and the m score of a caption is set to 0 if the IoU between the predicted box and the object is less than the given ... | definition, denominator, direction and uncertainty | p. 5 (5.2. Comparison with SoTA Specialists), p. 17 (Figure/Table caption), p. 5 (5.2. Comparison with SoTA Specialists) |
| Baseline/ablation | The baseline method directly generates the captions given the input 3D scene and visual prompts without any textual instructions. | fair input/data/compute/action matching | p. 7 (5.3. Ablation Studies), p. 5 (5.2. Comparison with SoTA Specialists), p. 5 (5.2. Comparison with SoTA Specialists) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 6. Conclusions - extractive body cue:** In this paper, we present LL3DA, a large language 3D assistant that could take both textual- and visual- interactions from human for understanding, reasoning, and ...
- **p. 8 / 6. Conclusions - extractive body cue:** Our model directly encodes 3D point cloud for scene representations, and aggregates information from scenes and human interactions with the atten8

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 1 (1. Introduction), p. 3 (3.1. Problem Formatting)이다.

## 검색 태그 근거

장면 점군과 텍스트, 사용자 클릭이나 3D 상자 같은 위치 지시를 받아 응답한다. 장면에 관한 질문과 텍스트로 작성한 과제 계획이 평가 범위다. [원문 3쪽](https://arxiv.org/pdf/2311.18651#page=3) · [원문 6쪽](https://arxiv.org/pdf/2311.18651#page=6)
