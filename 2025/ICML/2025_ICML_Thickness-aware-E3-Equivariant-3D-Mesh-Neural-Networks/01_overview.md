# Thickness-aware E(3)-Equivariant 3D Mesh Neural Networks

- Year/Venue: 2025 / ICML poster
- Category: 3D Equivariance, Calibration, and Registration
- Tags: 3D reconstruction, equivariant, 3D Vision
- Paper link: ./2025/ICML/2025_ICML_Thickness-aware-E3-Equivariant-3D-Mesh-Neural-Networks/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- This limitation arises from the disconnected nature of these surfaces and the absence of internal edge connections within the mesh.
- However, existing mesh-based methods focus solely on modeling the surfaces of 3D objects, overlooking their thickness.
- Mesh-based 3D static analysis methods have recently emerged as efficient alternatives to traditional computational numerical solvers, significantly reducing computational costs and runtime for various physics-based analyses.

## Core Idea
- In this work, we propose a novel framework, the Thickness-aware E(3)-Equivariant 3D Mesh Neural Network (T-EMNN), that effectively integrates the thickness of 3D objects while maintaining the computational ...
- Additionally, we introduce data-driven coordinates that encode spatial information while preserving E(3)-equivariance or invariance properties, ensuring consistent and robust analysis.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Evaluations on a real-world industrial dataset demonstrate the superior performance of T-EMNN in accurately predicting node-level 3D deformations, effectively capturing thickness effects while maintaining computational efficiency.
- The left figures show a mesh, with two different target nodes (•), their thickness paired nodes (•), thickness distance (−), and nearby nodes within a radius (•).

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- In this work, we propose a novel framework, the Thickness-aware E(3)-Equivariant 3D Mesh Neural Network (T-EMNN), that effectively integrates the thickness of 3D objects while maintaining the computational ...
- Additionally, we introduce data-driven coordinates that encode spatial information while preserving E(3)-equivariance or invariance properties, ensuring consistent and robust analysis.
- Evaluations on a real-world industrial dataset demonstrate the superior performance of T-EMNN in accurately predicting node-level 3D deformations, effectively capturing thickness effects while maintaining computational efficiency.

## Abstract Cue
- Mesh-based 3D static analysis methods have recently emerged as efficient alternatives to traditional computational numerical solvers, significantly reducing computational costs and runtime for various physics-based analyses.
