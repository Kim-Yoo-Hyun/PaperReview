# Problem

- Year/Venue: 2024 / ECCV
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D Vision
- Paper link: ./2024/ECCV/2024_ECCV_GeoGaussian-Geometry-aware-Gaussian-Splatting-for-Scene-Re/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Due to the impressive rendering quality of Neural Radiance Fields (NeRF) , the area of photo-realistic novel view synthesis (NVS) has become a popular research topic in the ...
- While NeRFs offer high-quality rendering, 3D Gaussian Splatting ( ) shows better performance in terms of training speed and rendering quality.
- 3D Gaussian Splatting is explicitly represented by a set of Gaussian points parameterized by its position, orientation, and spherical harmonics parameters.

## 해결하려는 문제
- To mitigate this issue, we propose a novel approach called GeoGaussian.
- Our proposed pipeline achieves state-of-the-art performance in novel view synthesis and geometric reconstruction, as evaluated qualitatively and quantitatively on public datasets.
- Benefiting from the proposed architecture, the generative ability of 3D Gaussians is enhanced, especially in structured regions.

## 선행 연구 / 배경 단서
- While NeRFs offer high-quality rendering, 3D Gaussian Splatting ( ) shows better performance in terms of training speed and rendering quality.
- An additional rasterization step re-projects these 3D Gaussians back to training images to capture ⋆ Equal senior author
- 3D Gaussian Splatting is explicitly represented by a set of Gaussian points parameterized by its position, orientation, and spherical harmonics parameters.
