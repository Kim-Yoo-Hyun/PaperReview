# Problem

- Year/Venue: 2024 / NeurIPS
- Category: Foundations: Monocular Geometry
- Tags: depth, 3D Vision
- Paper link: ./2024/NeurIPS/2024_NeurIPS_Depth-Anything-V2/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Monocular depth estimation (MDE) is gaining increasing attention, due to its fundamental role in widespread downstream tasks.
- Precise depth information is not only favorable in classical applications, such as 3D reconstruction , navigation , and autonomous driving , but is also preferable in modern scenarios, ...
- Therefore, there have been numerous MDE models emerging recently, which are all capable of addressing open-world images.

## 해결하려는 문제
- Compared with the latest models built on Stable Diffusion, our models are significantly more efficient (more than 10× faster) and more accurate.
- In addition to our models, considering the limited diversity and frequent noise in current test sets, we construct a versatile evaluation benchmark with precise annotations and diverse scenes ...

## 선행 연구 / 배경 단서
- From the aspect of model architecture, these works can be divided into two groups.
- Monocular depth estimation (MDE) is gaining increasing attention, due to its fundamental role in widespread downstream tasks.
- One group is based on discriminative models, e.g., BEiT and DINOv2 , while the other is based on generative models, e.g., Stable Diffusion (SD) .
