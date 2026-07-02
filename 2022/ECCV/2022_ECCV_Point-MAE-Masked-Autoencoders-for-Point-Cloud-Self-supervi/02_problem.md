# Problem

- Year/Venue: 2022 / ECCV
- Category: Foundations: 3D Representation Learning
- Tags: point cloud, 3D Vision
- Paper link: ./2022/ECCV/2022_ECCV_Point-MAE-Masked-Autoencoders-for-Point-Cloud-Self-supervi/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Inspired by this, we propose a neat scheme of masked autoencoders for point cloud self-supervised learning, addressing the challenges posed by point cloud’s properties, including leakage of location ...

## 해결하려는 문제
- Extensive experiments show that our approach is efficient during pre-training and generalizes well on various downstream tasks.
- Inspired by this, we propose a neat scheme of masked autoencoders for point cloud self-supervised learning, addressing the challenges posed by point cloud’s properties, including leakage of location ...
- We show with our scheme, a simple architecture entirely based on standard Transformers can surpass dedicated Transformer models from supervised learning.

## 선행 연구 / 배경 단서
- Self-supervised learning learns latent features from unlabeled data instead of building representations based on human-defined annotations.
- It is usually done by designing a pretext task to pre-train the model, then fine-tune on downstream tasks.
