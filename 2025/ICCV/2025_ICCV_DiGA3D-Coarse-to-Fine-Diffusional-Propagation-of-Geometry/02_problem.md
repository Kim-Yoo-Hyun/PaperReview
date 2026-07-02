# Problem

- Year/Venue: 2025 / ICCV
- Category: 3D Generative Modeling and Diffusion
- Tags: Diffusion, Generation, 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_DiGA3D-Coarse-to-Fine-Diffusional-Propagation-of-Geometry/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- However, there are still challenges in performing multiple 3D inpainting tasks within a unified framework: 1) Single reference inpainting methods lack robustness when dealing with views that are ...
- To tackle these challenges, we introduce DiGA3D, a novel and versatile 3D inpainting pipeline that leverages diffusion models to propagate consistent appearance and geometry in a coarse-tofine manner.
- Although several methods have explored unified pipelines for versatile 3D inpainting, they still face some challenges: First, some methods rely on a single reference image to guide the ...

## 해결하려는 문제
- To tackle these challenges, we introduce DiGA3D, a novel and versatile 3D inpainting pipeline that leverages diffusion models to propagate consistent appearance and geometry in a coarse-tofine manner.
- Extensive experiments on multiple 3D inpainting tasks demonstrate the effectiveness of our method.
- Next, DiGA3D designs an Attention Feature Propagation (AFP) mechanism that propagates attention features from the selected reference views to other views via diffusion models to maintain appearance consistency.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
