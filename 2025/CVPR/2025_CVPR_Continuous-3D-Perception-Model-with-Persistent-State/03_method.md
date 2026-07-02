# Method

- Year/Venue: 2025 / CVPR
- Category: 3D Reconstruction, Geometry, and SLAM
- Tags: 3D reconstruction, SLAM, representation
- Paper link: ./2025/CVPR/2025_CVPR_Continuous-3D-Perception-Model-with-Persistent-State/paper.pdf
- Code/Project: https://cut3r.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We present a unified framework capable of solving a broad range of 3D tasks.
- We use a ViT-Large model for the image encoder Encoderi , initialized with DUSt3R encoder pretrained weights, and ViT-Base for the decoders.
- The data-driven nature of our method enables it to address challenging cases of degeneracy, make predictions from as few as a single image, and infer structures that are ...

## 원리적 동기
- The tabula rasa nature of these approaches poses challenges in handling scenarios with sparse observations or ill-posed conditions.
- We present a unified framework capable of solving a broad range of 3D tasks.

## 핵심 방법론
- We use a ViT-Large model for the image encoder Encoderi , initialized with DUSt3R encoder pretrained weights, and ViT-Base for the decoders.
- The state consists of 768 tokens, each with a dimensionality of 768.
- Both the encoder and decoders operate on 16×16 pixel patches.
