# Problem

- Year/Venue: 2025 / ICCV
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, point cloud, 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_RayletDF-Raylet-Distance-Fields-for-Generalizable-3D-Surfa/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Nevertheless, due to the limitation of existing ray parametrizations such as Plucker and spherical coordinates, they are often limited to recovering object-level surfac
- Unlike existing coordinate-based methods which are often computationally intensive when rendering explicit surfaces, our proposed method, named RayletDF, introduces a new technique called raylet distance field, which aims ...
- However, it still falls short in rendering high-quality depth views, due to its failure in capturing fine-grained surface geometry, though various constraints such as depth priors , local ...

## 해결하려는 문제
- We extensively evaluate our method on multiple public real-world datasets, demonstrating superior performance in surface reconstruction from point clouds or 3D Gaussians.
- In this paper, we present a generalizable method for 3D surface reconstruction from raw point clouds or pre-estimated 3D Gaussians by 3DGS from RGB images.
- Most notably, our method achieves exceptional generalization ability, successfully recovering 3D surfaces in a single-forward pass across unseen datasets in testing.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
