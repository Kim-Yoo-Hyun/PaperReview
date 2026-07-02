# Problem

- Year/Venue: 2021 / ICCV
- Category: Foundations: Vision Foundation Models
- Tags: Vision Foundation Model, self-supervised, representation
- Paper link: ./2021/ICCV/2021_ICCV_Emerging-Properties-in-Self-Supervised-Vision-Transformers/paper.pdf
- Code/Project: https://github.com/facebookresearch/dino
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Introduction Transformers have recently emerged as an alternative to convolutional neural networks (convnets) for visual recognition .
- Their adoption has been coupled with a training strategy inspired by natural language processing (NLP), that is, pretraining on large quantities of data and finetuning on the target ...
- The resulting Vision Transformers (ViT) are competitive with convnets but, they have not yet delivered clear benefits over them: they are computationally more demanding, require more training data, ...

## 해결하려는 문제
- In this paper, we question whether the muted success of Transformers in vision can be explained by the use of supervision in their pretraining.
- Our motivation is that one of the main ingredients for the success of Transformers in NLP was the use of self-supervised pretraining, in the form of close procedure ...
- These self-supervised pretraining objectives use the words in a sentence to create pretext tasks that provide a richer learning signal than the supervised objective of predicting a single ...

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
