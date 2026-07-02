# Method

- Year/Venue: 2021 / ICCV
- Category: Foundations: Vision Foundation Models
- Tags: Vision Foundation Model, self-supervised, representation
- Paper link: ./2021/ICCV/2021_ICCV_Emerging-Properties-in-Self-Supervised-Vision-Transformers/paper.pdf
- Code/Project: https://github.com/facebookresearch/dino
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- These self-supervised pretraining objectives use the words in a sentence to create pretext tasks that provide a richer learning signal than the supervised objective of predicting a single ...
- Our motivation is that one of the main ingredients for the success of Transformers in NLP was the use of self-supervised pretraining, in the form of close procedure ...
- In this paper, we question whether the muted success of Transformers in vision can be explained by the use of supervision in their pretraining.

## 원리적 동기
- Introduction Transformers have recently emerged as an alternative to convolutional neural networks (convnets) for visual recognition .
- Their adoption has been coupled with a training strategy inspired by natural language processing (NLP), that is, pretraining on large quantities of data and finetuning on the target ...
- These self-supervised pretraining objectives use the words in a sentence to create pretext tasks that provide a richer learning signal than the supervised objective of predicting a single ...

## 핵심 방법론
- When we switch to a ViT architecture, DINO outperforms BYOL, MoCov2 and SwAV by +3.5% with linear classification and by +7.9% with k-NN evaluation.
- On the bottom panel of Table 2, we compare the best performance obtained across architectures.
- In top panel of Table 2, we compare DINO with other self-supervised methods with the same architecture, either a ResNet-50 or a ViT-small (which follows the design of ...
- Comparing with SSL frameworks on ImageNet We consider two different settings: comparison with the same architecture and across architectures.
- This property emerges only when using DINO with ViT architectures, and does not appear with other existing self-supervised methods nor with a ResNet-50.
