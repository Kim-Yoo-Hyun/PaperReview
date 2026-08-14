# Method

- Year/Venue: 2024 / CVPR
- Category: Manipulation, Contact, and Dexterity
- Tags: Robotics, tactile sensing, Vision-Language, multimodal representation, open-vocabulary
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://cfeng16.github.io/UniTouch/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- We use the same architectures to ensure a fair comparison.
- We use L = 5 learnable tokens for each sensor type in our pretraining datasets with K = 3 different sensors.
- We introduce UniTouch, a unified tactile model for vision-based touch sensors connected to multiple modalities, including vision, language, and sound.

## 원리적 동기
- However, multimodal learning with touch remains challenging due to the expensive data collection process and nonstandardized sensor outputs.
- We use the same architectures to ensure a fair comparison.

## 핵심 방법론
- We use the same architectures to ensure a fair comparison.
- We use L = 5 learnable tokens for each sensor type in our pretraining datasets with K = 3 different sensors.
- We adopt Vision Transformer (ViT) as the backbone for our touch encoder, which contains 24 multi-head attention blocks with 16 heads on each.
- We use the AdamW optimizer with the base learning rate of 1 × 10−5 and cosine decay learning rate scheduler.
- We compare our touch features with other methods and ImageNet pretraining.
