# Dr. Splat: Directly Referring 3D Gaussian Splatting via Direct Language Embedding Registration

- Year/Venue: 2025 / CVPR
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Gaussian Splatting, language embedding, grounding
- Paper link: ./2025/CVPR/2025_CVPR_Dr.-Splat-Directly-Referring-3D-Gaussian-Splatting-via-Dir/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Unlike existing language-embedded 3DGS methods, which rely on a rendering process, our method directly associates language-aligned CLIP embeddings with 3D Gaussians for holistic 3D scene understanding.
- Open-vocabulary 3D scene understanding represents a significant challenge in the field of computer vision, with applications spanning autonomous navigation, robotics, and augmented reality.
- The 2D approach relies on multiview rendering, incurring high computational costs.

## Core Idea
- In contrast, we propose to use Product Quantization (PQ) on a large-scale image dataset, eliminating per-scene training.
- Unlike existing language-embedded 3DGS methods, which rely on a rendering process, our method directly associates language-aligned CLIP embeddings with 3D Gaussians for holistic 3D scene understanding.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experiments demonstrate that our approach significantly outperforms existing approaches in 3D perception benchmarks, such as openvocabulary 3D semantic segmentation, 3D object localization, and 3D object selection tasks.
- For video results, please visit : https://drsplat.github.io/ 3D search scheme (ours) Chair Render 2D images ‘Direct’ 3D Search Search all images: B×H×W → Slow #Gaussians → Fast W ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Experiments demonstrate that our approach significantly outperforms existing approaches in 3D perception benchmarks, such as openvocabulary 3D semantic segmentation, 3D object localization, and 3D object selection tasks.
- Unlike existing language-embedded 3DGS methods, which rely on a rendering process, our method directly associates language-aligned CLIP embeddings with 3D Gaussians for holistic 3D scene understanding.
- The key of our method is a language feature registration technique where CLIP embeddings are assigned to the dominant Gaussians intersected by each pixel-ray.

## Abstract Cue
- Splat, a novel approach for openvocabulary 3D scene understanding leveraging 3D Gaussian Splatting.
