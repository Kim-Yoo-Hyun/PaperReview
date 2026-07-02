# Method

- Year/Venue: 2024 / ECCV
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, geometry, 3D Vision
- Paper link: ./2024/ECCV/2024_ECCV_CG-SLAM-Efficient-Dense-RGB-D-SLAM-in-a-Consistent-Uncerta/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Through an in-depth analysis of Gaussian Splatting, we propose several techniques to construct a consistent and stable 3D Gaussian field suitable for tracking and mapping.
- We incorporated an uncertainty model that utilizes the geometry prior to attach the uncertainty property on rendered images and Gaussian primitives.
- We can obtain the corresponding 2D Gaussian distribution N (µ̂, Σ̂) as: \label {eq-2} \mathbf {\hat {\Sigma }} = \mathbf {J}\mathbf {W}\mathbf {\Sigma }\mathbf {W}^T\mathbf {J}^T~, (2) and ...

## 원리적 동기
- Dense visual Localization and Mapping (Visual SLAM) is a long-standing problem in 3D computer vision over recent decades, which targets performing pose tracking and scene mapping simultaneously with ...
- Despite their notable successes in surface modeling and novel view synthesis, existing NeRF-based methods are hindered by their computationally intensive and time-consuming volume rendering pipeline.
- Through an in-depth analysis of Gaussian Splatting, we propose several techniques to construct a consistent and stable 3D Gaussian field suitable for tracking and mapping.

## 핵심 방법론
- We incorporated an uncertainty model that utilizes the geometry prior to attach the uncertainty property on rendered images and Gaussian primitives.
- We can obtain the corresponding 2D Gaussian distribution N (µ̂, Σ̂) as: \label {eq-2} \mathbf {\hat {\Sigma }} = \mathbf {J}\mathbf {W}\mathbf {\Sigma }\mathbf {W}^T\mathbf {J}^T~, (2) and ...
- Given a set of RGB-D sequences, our system incrementally generates a stable, consistent, and uncertainty-aware Gaussian field, serving camera pose optimization and geometry reconstruction.
- 3.3, we detail the Gaussian primitive management strategy and some innovative loss terms that ensure geometry stability and accuracy.
- 3.1, we briefly introduce the 3D Gaussian splatting model and rasterization principles.
