# Problem

- Year/Venue: 2025 / CVPR
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Gaussian Splatting, grounding, LVLM
- Paper link: ./2025/CVPR/2025_CVPR_ReasonGrounder-LVLM-Guided-Hierarchical-Feature-Splatting/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Open-vocabulary 3D visual grounding and reasoning aim to localize objects in a scene based on implicit language descriptions, even when they are occluded.
- This ability is crucial for tasks such as vision-language navigation and autonomous robotics.
- However, current methods struggle because they rely heavily on fine-tuning with 3D annotations and mask proposals, which limits their ability to handle diverse semantics and common knowledge required ...

## 해결하려는 문제
- In this work, we propose ReasonGrounder, an LVLM-guided framework that uses hierarchical 3D feature Gaussian fields for adaptive grouping based on physical scale, enabling open-vocabulary 3D grounding and ...
- Experiments show that ReasonGrounder significantly improves 3D grounding accuracy in real-world scenarios.
- ReasonGrounder interprets implicit instructions using large vision-language models (LVLM) and localizes occluded objects through 3D Gaussian splatting.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
