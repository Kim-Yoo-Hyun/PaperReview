# Method

- Year/Venue: 2021 / ICCV
- Category: Foundations: 3D Representation Learning
- Tags: 3D Vision, point cloud, representation, self-supervised
- Paper link: ./2021/ICCV/2021_ICCV_Self-Supervised-Pretraining-of-3D-Features-on-any-Point-Cl/paper.pdf
- Code/Project: https://github.com/facebookresearch/DepthContrast
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We use our data augmentation described in § 3.4 and use the training objectives from § 3.
- We present a simple self-supervised pretraining method that can work with any 3D data — single or multiview, indoor or outdoor, acquired by varied sensors, without 3D registration.
- 4.2.1 Training Higher Capacity Models We use DepthContrast for training higher capacity models.

## 원리적 동기
- A primary reason is the lack of large annotated datasets because 3D data is both difficult to acquire and time consuming to label.
- Pretraining on depth maps faces several challenges: first, the absence of any supervision at scale requires
- We use our data augmentation described in § 3.4 and use the training objectives from § 3.

## 핵심 방법론
- We use our data augmentation described in § 3.4 and use the training objectives from § 3.
- 4.2.1 Training Higher Capacity Models We use DepthContrast for training higher capacity models.
- We use diverse downstream datasets - full scenes/object centric; using different 3D sensors; single/multi-view; real/synthetic; indoor/outdoor.
- On these diverse datasets, we use three major tasks, which are classification, semantic segmentation, and object detection.
- 4.2.2 Using More Pretraining Data We increase the pretraining data by using readily available single-view 3D data from the Redwood-vid dataset .
