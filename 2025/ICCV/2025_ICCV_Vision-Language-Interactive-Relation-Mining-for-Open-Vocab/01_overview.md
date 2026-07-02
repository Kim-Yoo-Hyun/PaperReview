# Vision-Language Interactive Relation Mining for Open-Vocabulary Scene Graph Generation

- Year/Venue: 2025 / ICCV
- Category: 3D Scene Graphs and Graph Reasoning
- Tags: Vision-Language Model, Graph Reasoning, semantic
- Paper link: ./2025/ICCV/2025_ICCV_Vision-Language-Interactive-Relation-Mining-for-Open-Vocab/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Though existing methods have been verified to be effective, they usually follow a closed-set assumption, i.e., the training and testing data share the same predicate categories.
- Illustration of the interactive visual-language model for OV-SGG. (a) Previous methods directly use category-level correspondence to adapt the vision-language models to openvocabulary relations. (b) In this work, we ...
- However, due to the lack of quadratic relation-aware knowledge in VLMs, directly using the category-level correspondence in the base dataset could not sufficiently represent generalized relations involved in ...

## Core Idea
- To this end, we propose a novel Vision-Language Interactive Relation Mining model (VL-IRM) for OV-SGG, which explores learning generalized relation-aware knowledge through multimodal interaction.
- Since the task evaluation of OV-SGG requires the score of relation triplets based on the relation logits for ranking , to assess the effectiveness of the open-end generative ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments demonstrate the superior OV-SGG performance of our method.
- To this end, Open-Vocabulary Scene Graph Generation (OV-SGG) is proposed, whose goal is to leverage pre-trained models to extend the predicate space and improve the performance of identifying ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Extensive experiments demonstrate the superior OV-SGG performance of our method.
- To promote the deployment of scenario understanding in the real world, Open-Vocabulary Scene Graph Generation (OV-SGG) has attracted much attention recently, aiming to generalize beyond the limited number ...
- Though existing methods have been verified to be effective, they usually follow a closed-set assumption, i.e., the training and testing data share the same predicate categories.

## Abstract Cue
- To promote the deployment of scenario understanding in the real world, Open-Vocabulary Scene Graph Generation (OV-SGG) has attracted much attention recently, aiming to generalize beyond the limited number of relation categories labeled during training and detect those unseen relations during inference.
