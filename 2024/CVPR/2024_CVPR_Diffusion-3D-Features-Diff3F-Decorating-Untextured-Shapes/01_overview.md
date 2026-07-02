# Diffusion 3D Features (Diff3F): Decorating Untextured Shapes with Distilled Semantic Features

- Year/Venue: 2024 / CVPR
- Category: 3D Generative Modeling and Diffusion
- Tags: semantic, alignment, Diffusion, Generation, 3D Vision
- Paper link: ./2024/CVPR/2024_CVPR_Diffusion-3D-Features-Diff3F-Decorating-Untextured-Shapes/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- We present D IFF 3F as a simple, robust, and classagnostic feature descriptor that can be computed for untextured input shapes (meshes or point clouds).
- Our method distills diffusion features from image foundational models onto input shapes.
- Specifically, we use the input shapes to produce depth and normal maps as guidance for conditional image synthesis.

## Core Idea
- Since our method operates in the domain of point clouds, we use a Euclideanbased measure, as used in previous works .
- TOSCA consists of highly isomteric shapes, therefore we also evaluate our method on SHREC’20, which consists of highly non-isometric pairs of animals.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We perform extensive experiments on multiple benchmarks (SHREC’19, SHREC’20, FAUST, and TOSCA) and demonstrate that our features, being semantic instead of geometric, produce reliable correspondence across both isometric ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Our method distills diffusion features from image foundational models onto input shapes.
- For instance, DINO features and diffusion features extract dense semantic image features from photo-realistic images without additional training.
- We perform extensive experiments on multiple benchmarks (SHREC’19, SHREC’20, FAUST, and TOSCA) and demonstrate that our features, being semantic instead of geometric, produce reliable correspondence across both isometric ...

## Abstract Cue
- We present D IFF 3F as a simple, robust, and classagnostic feature descriptor that can be computed for untextured input shapes (meshes or point clouds).
