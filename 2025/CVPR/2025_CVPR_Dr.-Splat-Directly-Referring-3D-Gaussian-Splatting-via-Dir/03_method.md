# Method

- Year/Venue: 2025 / CVPR
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Gaussian Splatting, language embedding, grounding
- Paper link: ./2025/CVPR/2025_CVPR_Dr.-Splat-Directly-Referring-3D-Gaussian-Splatting-via-Dir/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- In contrast, we propose to use Product Quantization (PQ) on a large-scale image dataset, eliminating per-scene training.
- Unlike existing language-embedded 3DGS methods, which rely on a rendering process, our method directly associates language-aligned CLIP embeddings with 3D Gaussians for holistic 3D scene understanding.
- The key of our method is a language feature registration technique where CLIP embeddings are assigned to the dominant Gaussians intersected by each pixel-ray.

## 원리적 동기
- Unlike existing language-embedded 3DGS methods, which rely on a rendering process, our method directly associates language-aligned CLIP embeddings with 3D Gaussians for holistic 3D scene understanding.
- Open-vocabulary 3D scene understanding represents a significant challenge in the field of computer vision, with applications spanning autonomous navigation, robotics, and augmented reality.
- In contrast, we propose to use Product Quantization (PQ) on a large-scale image dataset, eliminating per-scene training.

## 핵심 방법론
- In contrast, we propose to use Product Quantization (PQ) on a large-scale image dataset, eliminating per-scene training.
- We visualize rendering of selected 3D Gaussians for LangSplat , OpenGaussian , and ours.
- To measure 3D object selection performance, we calculate 2D segmentation accuracy on rendering of selected 3D Gaussians.
- Splat (ours) LangSplat-m OpenGaussian Dr.
- OpenGaussian often struggles to distinguish closely situated objects.
