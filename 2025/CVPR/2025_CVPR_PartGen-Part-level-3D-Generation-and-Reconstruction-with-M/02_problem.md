# Problem

- Year/Venue: 2025 / CVPR
- Category: 3D Generative Modeling and Diffusion
- Tags: 3D reconstruction, Diffusion, Generation, 3D Vision
- Paper link: ./2025/CVPR/2025_CVPR_PartGen-Part-level-3D-Generation-and-Reconstruction-with-M/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Introduction view-consistent coloring problem, fine-tuning a multi-view image generator to produce several color-coded segmentation maps of the given 3D object.
- Text- or image-to-3D generators and 3D scanners can now produce 3D assets with high-quality shapes and textures, but as single, fused entities lacking meaningful structure.

## 해결하려는 문제
- Our method leverages a multi-view diffusion model to extract plausible and view-consistent part segmentations from multiple views of a Work completed during Minghao Chen’s internship at Meta.
- To bridge this gap, we introduce PartGen, a novel approach for generating, from text, images, or unstructured 3D objects, 3D objects composed of meaningful parts.
- We assess our method empirically on a large collection of 3D assets produced by 3D artists or scanned, both quantitatively and qualitatively.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
