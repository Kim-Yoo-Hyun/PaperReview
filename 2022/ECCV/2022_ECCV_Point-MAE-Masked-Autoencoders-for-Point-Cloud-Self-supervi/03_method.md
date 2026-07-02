# Method

- Year/Venue: 2022 / ECCV
- Category: Foundations: 3D Representation Learning
- Tags: point cloud, 3D Vision
- Paper link: ./2022/ECCV/2022_ECCV_Point-MAE-Masked-Autoencoders-for-Point-Cloud-Self-supervi/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Inspired by this, we propose a neat scheme of masked autoencoders for point cloud self-supervised learning, addressing the challenges posed by point cloud’s properties, including leakage of location ...
- We show with our scheme, a simple architecture entirely based on standard Transformers can surpass dedicated Transformer models from supervised learning.
- Furthermore, our work inspires the feasibility of applying unified architectures from languages and images to the point cloud.

## 원리적 동기
- Inspired by this, we propose a neat scheme of masked autoencoders for point cloud self-supervised learning, addressing the challenges posed by point cloud’s properties, including leakage of location ...
- Inspired by this, we propose a neat scheme of masked autoencoders for point cloud self-supervised learning, addressing the challenges posed by point cloud’s properties, including leakage of location ...

## 핵심 방법론
- We follow standard protocols to split ModelNet40 into 9843 instances for the training set and 2468 for the testing set.
- ModelNet40 consists of 12,311 clean 3D CAD models, covering 40 object categories.
- Standard random scaling and random translation are applied for data augmentation during training.
