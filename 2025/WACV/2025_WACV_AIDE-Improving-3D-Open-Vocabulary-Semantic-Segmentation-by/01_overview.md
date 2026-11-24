# AIDE: Improving 3D Open-Vocabulary Semantic Segmentation by Aligned Vision-Language Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/WACV2025/html/Wang_AIDE_Improving_3D_Open-Vocabulary_Semantic_Segmentation_by_Aligned_Vision-Language_Learning_WACV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/WACV2025/papers/Wang_AIDE_Improving_3D_Open-Vocabulary_Semantic_Segmentation_by_Aligned_Vision-Language_Learning_WACV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / WACV
- Authors: Yimu Wang, Krzysztof Czarnecki
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: open-vocabulary, semantic, alignment
- Official paper: https://openaccess.thecvf.com/content/WACV2025/html/Wang_AIDE_Improving_3D_Open-Vocabulary_Semantic_Segmentation_by_Aligned_Vision-Language_Learning_WACV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/WACV2025/papers/Wang_AIDE_Improving_3D_Open-Vocabulary_Semantic_Segmentation_by_Aligned_Vision-Language_Learning_WACV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://openaccess.thecvf.com/content/WACV2025/papers/Wang_AIDE_Improving_3D_Open-Vocabulary_Semantic_Segmentation_by_Aligned_Vision-Language_Learning_WACV_2025_paper.pdf)

## Why This Paper Is Here

AIDE는 실내 점군과 뷰별 캡션의 정렬을 개선하고 텍스트 인코더를 3차원 의미 분할에 적응시킨다. [PDF 1쪽](https://openaccess.thecvf.com/content/WACV2025/papers/Wang_AIDE_Improving_3D_Open-Vocabulary_Semantic_Segmentation_by_Aligned_Vision-Language_Learning_WACV_2025_paper.pdf#page=1) · [PDF 4쪽](https://openaccess.thecvf.com/content/WACV2025/papers/Wang_AIDE_Improving_3D_Open-Vocabulary_Semantic_Segmentation_by_Aligned_Vision-Language_Learning_WACV_2025_paper.pdf#page=4)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** 3D open-vocabulary semantic segmentation aims at recognizing countless categories beyond the limited set of annotations used in traditional settings.
- **p. 1 / Abstract - extractive body cue:** Due to the lack of large-scale 3D-vision-language segmentation data, instead of training models from scratch, the current solutions distill knowledge from pre-trained 2D vision-language models ...
- **p. 1 / Abstract - extractive body cue:** However, this distillation is supervised by misaligned 3D-scene-image-to-text data pairs, consequently leading to suboptimal performance.
- **p. 1 / Abstract - extractive body cue:** Moreover, as 2D VLMs are trained on 2D datasets, text encoders of VLMs, which serve as the bridge between 3D models and an unbounded set ...
- **p. 1 / Abstract - extractive body cue:** In this paper, to address these issues and improve generalization performance, we propose an AlIgned 3D Open-Vocabulary SEmantic Segmentation framework, called AIDE, with two novel ...
- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are as follows, • We identify two significant challenges within existing methods, i.e., the misalignment in 3D-scene-image-totext data pairs and the ...
- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, we propose AIDE, including the CLIP-rewarded alignment and adaptive segmentation modules. • In the CLIP-rewarded alignment module, we generate high-quality 3D-scene-image-to-text ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** To address these issues, we propose a novel AlIgned 3D Open-Vocabulary SEmantic Segmentation framework, called AIDE.
- **p. 2 / 1. Introduction - extractive body cue:** Then, to encourage rich associations between 3D and text, we propose the CLIP-rewarded sampling method, which samples captions based on their similarity to the 3D-scene ...
- **p. 4 / 3.1. Problem Definition - extractive body cue:** Our solution: To generate aligned data, we propose the CLIP-rewarded alignment module in Sec.
- **p. 4 / 3.1. Problem Definition - extractive body cue:** Our solution: To solve this issue and adapt text encoders by automatically finding the most suitable prompt, we propose the adaptive segmentation module elaborated in ...
- **p. 5 / 3.4. Adaptive Segmentation-Text Modeling - extractive body cue:** To better adapt the text encoder to 3D scenarios, we introduce a small number of learnable tokens TOKENS at the input and every transformer layer ...
- **p. 5 / 3.4. Adaptive Segmentation-Text Modeling - extractive body cue:** During inference, we use the trainable tokens and the category names as the input of the text encoder ftext(·) to generate the category embedding C ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Sequentially, for each transformer layer, trainable tokens are merged with the output of the previous layer as the input of the current layer, i.e., concat([TOKENSi, Ftext, i-1]), where concat is the concatenation ... | camera/depth stream, pose, map와 language goal | p. 5 (3.4. Adaptive Segmentation-Text Modeling), p. 4 (3.1. Problem Definition) |
| State/latent | Sequentially, transformer, layer, trainable, tokens, merged, output, previous, input, current, concat, TOKENSi | robot pose, free-space/semantic map와 local goal | p. 5 (3.4. Adaptive Segmentation-Text Modeling), p. 4 (3.1. Problem Definition), p. 4 (3.1. Problem Definition) |
| Output/action | To automatically find the most suitable prompt for adapting text encoders into 3D scenarios, AIDE extends prompt tuning [38] by incorporating learnable tokens in the input space and each layer of the ... | collision-free trajectory 또는 velocity command | p. 4 (3.1. Problem Definition), p. 4 (3.1. Problem Definition), p. 1 (1. Introduction) |
| Objective/outcome | The training objective of our proposed AIDE is a weighted linear combination of segmentation loss (Eq. | goal reach, safety, localization error와 replanning latency | p. 5 (3.5. Training Objective), p. 5 (3.5. Training Objective) |

## Main Claims and Actual Contribution

- 여러 샘플링 온도로 영상 설명을 생성한 뒤 CLIP 유사도로 설명을 선택해 영상·점군·텍스트의 감독 쌍을 구성한다. [PDF 3쪽](https://openaccess.thecvf.com/content/WACV2025/papers/Wang_AIDE_Improving_3D_Open-Vocabulary_Semantic_Segmentation_by_Aligned_Vision-Language_Learning_WACV_2025_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/WACV2025/papers/Wang_AIDE_Improving_3D_Open-Vocabulary_Semantic_Segmentation_by_Aligned_Vision-Language_Learning_WACV_2025_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/WACV2025/papers/Wang_AIDE_Improving_3D_Open-Vocabulary_Semantic_Segmentation_by_Aligned_Vision-Language_Learning_WACV_2025_paper.pdf#page=5)
- 고정한 텍스트 인코더의 입력과 내부 층에 학습 토큰을 넣고 여러 개방 어휘 분할 자료에서 각 구성 요소의 효과를 평가했다. [PDF 5쪽](https://openaccess.thecvf.com/content/WACV2025/papers/Wang_AIDE_Improving_3D_Open-Vocabulary_Semantic_Segmentation_by_Aligned_Vision-Language_Learning_WACV_2025_paper.pdf#page=5) · [PDF 6쪽](https://openaccess.thecvf.com/content/WACV2025/papers/Wang_AIDE_Improving_3D_Open-Vocabulary_Semantic_Segmentation_by_Aligned_Vision-Language_Learning_WACV_2025_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/WACV2025/papers/Wang_AIDE_Improving_3D_Open-Vocabulary_Semantic_Segmentation_by_Aligned_Vision-Language_Learning_WACV_2025_paper.pdf#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (4.4. Qualitative Results-Generalization), p. 7 (Figure/Table caption) |
| Embodiment/environment | To validate the effectiveness of AIDE, we conducted extensive experiments on three popular 3D benchmarks: ScanNet [20], S3DIS [2], and one outdoor dataset (nuScenes [7]). | hardware/simulator version and reset protocol | p. 5 (4. Experiments), p. 6 (4.2. Quantative Results) |
| Dataset/benchmark | Benchmarks, Baselines, and Implementation Benchmarks and category partitions. | role, split, size and leakage | p. 5 (4. Experiments), p. 6 (4.2. Quantative Results), p. 5 (4. Experiments), p. 6 (4. Experiments) |
| Metric | These results underscore the importance of the CLIP-rewarded alignment and adaptive segmentation modules in enhancing open-vocabulary segmentation models' transferability to novel categories and scenarios. | definition, denominator, direction and uncertainty | p. 8 (4.4. Qualitative Results-Generalization), p. 2 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Baseline/ablation | Compared to our baseline, PLA, AIDE improves hIoU by 7.6 and 4.0 for each split. | fair input/data/compute/action matching | p. 6 (4.2. Quantative Results), p. 8 (4.4. Qualitative Results-Generalization), p. 8 (4.4. Qualitative Results-Generalization) |

## Explicit Limitations and Failure Boundary

- **p. 5 / 4. Experiments - extractive body cue:** Due to space limitations, the details of benchmarks and partitions are deferred to Appendix C.1.
- **p. 6 / 4.3. Ablation Studies - extractive body cue:** Due to the space limitation, ablation studies on the choice of temperatures (Tab.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 7. Ablation studies on using different text encoders of AIDE on ScanNet (B15/N4). this phenomenon. As generating over 30 captions per tem- perature will ...
- **p. 8 / 4.4. Qualitative Results-Generalization - extractive body cue:** On the other side, AIDE still maintains a lead over the baseline, demonstrating its robustness to variations in vocabulary.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 1 (1. Introduction), p. 4 (3.1. Problem Definition), p. 3 (3.1. Problem Definition), p. 5 (3.4. Adaptive Segmentation-Text Modeling)이다.
