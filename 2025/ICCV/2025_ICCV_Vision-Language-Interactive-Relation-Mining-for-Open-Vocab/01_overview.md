# Vision-Language Interactive Relation Mining for Open-Vocabulary Scene Graph Generation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Min_Vision-Language_Interactive_Relation_Mining_for_Open-Vocabulary_Scene_Graph_Generation_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Min_Vision-Language_Interactive_Relation_Mining_for_Open-Vocabulary_Scene_Graph_Generation_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: Yukuan Min, Muli Yang, Jinhao Zhang, Yuxuan Wang, Aming Wu, Cheng Deng
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Vision-Language Model, Graph Reasoning, semantic
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Min_Vision-Language_Interactive_Relation_Mining_for_Open-Vocabulary_Scene_Graph_Generation_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Min_Vision-Language_Interactive_Relation_Mining_for_Open-Vocabulary_Scene_Graph_Generation_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 원문 해당 쪽과 대조했다. [본문](https://openaccess.thecvf.com/content/ICCV2025/papers/Min_Vision-Language_Interactive_Relation_Mining_for_Open-Vocabulary_Scene_Graph_Generation_ICCV_2025_paper.pdf)

## Why This Paper Is Here

VL-IRM은 2D 영상에서 물체 쌍을 연결하는 관계를 학습해 훈련 시 관계 라벨이 없던 술어도 장면 그래프로 예측한다. [PDF 1쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Min_Vision-Language_Interactive_Relation_Mining_for_Open-Vocabulary_Scene_Graph_Generation_ICCV_2025_paper.pdf#page=1) · [PDF 3쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Min_Vision-Language_Interactive_Relation_Mining_for_Open-Vocabulary_Scene_Graph_Generation_ICCV_2025_paper.pdf#page=3)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** To promote the deployment of scenario understanding in the real world, Open-Vocabulary Scene Graph Generation (OV-SGG) has attracted much attention recently, aiming to generalize beyond ...
- **p. 1 / Abstract - extractive body cue:** Towards OV-SGG, one feasible solution is to leverage the large-scale pre-trained vision-language models (VLMs) containing plentiful category-level content to capture accurate correspondences between images and ...
- **p. 1 / Abstract - extractive body cue:** However, due to the lack of quadratic relation-aware knowledge in VLMs, directly using the category-level correspondence in the base dataset could not sufficiently represent generalized ...
- **p. 1 / Abstract - extractive body cue:** Therefore, designing an effective open-vocabulary relation mining framework is challenging and meaningful.
- **p. 1 / Abstract - extractive body cue:** To this end, we propose a novel Vision-Language Interactive Relation Mining model (VL-IRM) for OV-SGG, which explores learning generalized relation-aware knowledge through multimodal interaction.
- **p. 2 / 1. Introduction - extractive body cue:** Since existing pre-trained VLMs lack relation-aware knowledge [5], directly building a VLM for OV-SGG is challenging.
- **p. 2 / 1. Introduction - extractive body cue:** Unlike existing methods, this approach does not rely on a large amount of additional pre-training data or carefully set instruction prompts. • We develop a ...

## Core Idea

- **p. 4 / 3.3. Hierarchical Relation Extension - extractive body cue:** To mitigate the overfitting of VLM to the base dataset from the semantical level, we propose to construct a semantic-unbiased VLM.
- **p. 4 / 3.2. Generative Relation Recognition - extractive body cue:** We propose directly linking the relation predictor with a language model, and activating both the image encoder and the language model as trainable components, as ...
- **p. 6 / Method - extractive body cue:** Our method achieves comparable performance to prior models, without requiring access to various instruction prompts or additional pretraining.
- **p. 6 / Method - extractive body cue:** Since the task evaluation of OV-SGG requires the score of relation triplets based on the relation logits for ranking [5, 43], to assess the effectiveness ...
- **p. 2 / 1. Introduction - extractive body cue:** The contributions can be summarized as follows, • We consider a new perspective for OV-SGG, i.e., optimizing the structure of the VLM.
- **p. 4 / 3.2. Generative Relation Recognition - extractive body cue:** As for the decoder, we use cross-attention layers to make the text embedding interface with the relation embedding from the encoder.
- **p. 5 / 3.4. Training Objectives - extractive body cue:** Specifically, we use cross-entropy loss for each word in the generated text, and the language modeling loss is: \ma t h c al {L } ...
- **p. 3 / 3.1. OV-SGG Architecture - extractive body cue:** 3, the OV-SGG architecture comprises three primary components: an image encoder EncI (e.g., Swin Transformer backbone [26]) for image feature extraction, a text encoder EncL ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Moreover, recent advancements propose using an instruction prompt sequence, thus the model could more efficiently utilize the image-text pair knowledge of pre-trained VLMs or Large Language Models (LLMs) [18, 21]. | camera/depth stream, pose, map와 language goal | p. 2 (1. Introduction), p. 3 (3.1. OV-SGG Architecture) |
| State/latent | Moreover, recent, advancements, instruction, prompt, sequence, thus, model, could, more, efficiently, utilize | robot pose, free-space/semantic map와 local goal | p. 2 (1. Introduction), p. 3 (3.1. OV-SGG Architecture), p. 4 (3.1. OV-SGG Architecture) |
| Output/action | 3, the OV-SGG architecture comprises three primary components: an image encoder EncI (e.g., Swin Transformer backbone [26]) for image feature extraction, a text encoder EncL (e.g., BERT [12]) for text feature extraction, ... | collision-free trajectory 또는 velocity command | p. 3 (3.1. OV-SGG Architecture), p. 4 (3.1. OV-SGG Architecture), p. 4 (3.2. Generative Relation Recognition) |
| Objective/outcome | Specifically, we use cross-entropy loss for each word in the generated text, and the language modeling loss is: \ma t h c al {L } _ {co ns} =\su m _{i =1 ... | goal reach, safety, localization error와 replanning latency | p. 5 (3.4. Training Objectives), p. 5 (3.4. Training Objectives), p. 4 (3.2. Generative Relation Recognition) |

## Main Claims and Actual Contribution

- 물체 쌍과 장면 문맥을 이용해 관계 텍스트를 생성하고 시각 단서로 관계 표현을 보완해 열린 술어 후보와 대응시킨다. [PDF 3쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Min_Vision-Language_Interactive_Relation_Mining_for_Open-Vocabulary_Scene_Graph_Generation_ICCV_2025_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Min_Vision-Language_Interactive_Relation_Mining_for_Open-Vocabulary_Scene_Graph_Generation_ICCV_2025_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Min_Vision-Language_Interactive_Relation_Mining_for_Open-Vocabulary_Scene_Graph_Generation_ICCV_2025_paper.pdf#page=5)
- VG150 기반 열린 어휘 평가에서 기존 술어와 새로운 술어의 관계 예측을 비교하고 문맥 프롬프트의 효과를 분석했다. [PDF 5쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Min_Vision-Language_Interactive_Relation_Mining_for_Open-Vocabulary_Scene_Graph_Generation_ICCV_2025_paper.pdf#page=5) · [PDF 6쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Min_Vision-Language_Interactive_Relation_Mining_for_Open-Vocabulary_Scene_Graph_Generation_ICCV_2025_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Min_Vision-Language_Interactive_Relation_Mining_for_Open-Vocabulary_Scene_Graph_Generation_ICCV_2025_paper.pdf#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (Figure/Table caption), p. 6 (Figure/Table caption) |
| Embodiment/environment | As for VG dataset, We considered two different settings in the PGSG [21] and OVSGTR [5]. | hardware/simulator version and reset protocol | p. 5 (4.1. Datasets and Experimental Settings), p. 5 (4.1. Datasets and Experimental Settings) |
| Dataset/benchmark | For example, our method captures a novel reasonable relation "putting on" beyond fixed vocabulary constraints on the VG dataset. | role, split, size and leakage | p. 5 (4.1. Datasets and Experimental Settings), p. 5 (4.1. Datasets and Experimental Settings), p. 8 (4.4. Qualitative Results), p. 8 (4.4. Qualitative Results) |
| Metric | These results demonstrate that our model has a more general relation recognition ability. | definition, denominator, direction and uncertainty | p. 8 (4.4. Qualitative Results), p. 8 (4.4. Qualitative Results), p. 7 (Figure/Table caption) |
| Baseline/ablation | Specifically, without the full supervision of novel categories, our model can provide novel relationship predictions (e.g., "from" and ‘part of'). | fair input/data/compute/action matching | p. 8 (4.4. Qualitative Results), p. 7 (Figure/Table caption), p. 6 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** This work proposes a novel vision-language interactive relation mining model for OV-SGG.
- **p. 8 / 5. Conclusion - extractive body cue:** Specifically, by introducing a generative relation recognition model, our model achieves generating open-vocabulary relation names.
- **p. 8 / 5. Conclusion - extractive body cue:** In addition, a hierarchical extension module is adopted to further extend the relations.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 1 (1. Introduction), p. 4 (3.2. Generative Relation Recognition), p. 5 (3.4. Training Objectives)이다.
