# Problem

- Year/Venue: 2025 / CVPR
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Gaussian Splatting, language embedding, grounding
- Paper link: ./2025/CVPR/2025_CVPR_Dr.-Splat-Directly-Referring-3D-Gaussian-Splatting-via-Dir/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Unlike existing language-embedded 3DGS methods, which rely on a rendering process, our method directly associates language-aligned CLIP embeddings with 3D Gaussians for holistic 3D scene understanding.
- Open-vocabulary 3D scene understanding represents a significant challenge in the field of computer vision, with applications spanning autonomous navigation, robotics, and augmented reality.
- The 2D approach relies on multiview rendering, incurring high computational costs.

## 해결하려는 문제
- Experiments demonstrate that our approach significantly outperforms existing approaches in 3D perception benchmarks, such as openvocabulary 3D semantic segmentation, 3D object localization, and 3D object selection tasks.
- Unlike existing language-embedded 3DGS methods, which rely on a rendering process, our method directly associates language-aligned CLIP embeddings with 3D Gaussians for holistic 3D scene understanding.
- The key of our method is a language feature registration technique where CLIP embeddings are assigned to the dominant Gaussians intersected by each pixel-ray.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
