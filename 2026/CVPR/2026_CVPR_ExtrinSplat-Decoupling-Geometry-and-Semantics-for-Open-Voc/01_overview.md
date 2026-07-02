# ExtrinSplat: Decoupling Geometry and Semantics for Open-Vocabulary Understanding in 3D Gaussian Splatting

- Year/Venue: 2026 / CVPR
- Category: 3D Semantic Understanding and Alignment
- Tags: Gaussian Splatting, semantic, alignment, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_ExtrinSplat-Decoupling-Geometry-and-Semantics-for-Open-Voc/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- To overcome these limitations, we introduce ExtrinSplat, a framework built on the extrinsic paradigm that decouples geometry from semantics.
- Lifting 2D open-vocabulary understanding into 3D Gaussian Splatting (3DGS) scenes is a critical challenge.
- By replacing costly feature embedding with lightweight indices, ExtrinSplat reduces scene adaptation time from hours to minutes and lowers storage overhead by several orders of magnitude.

## Core Idea
- To overcome these limitations, we introduce ExtrinSplat, a framework built on the extrinsic paradigm that decouples geometry from semantics.
- For a fair comparison, we use the same predefined query texts as in OpenGaussian.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- More recently, a few approaches have explored embedding semantic features into each Gaussian via matching, which optimizes costs and achieves strong results.
- On benchmark tasks for open-vocabulary 3D object selection and semantic segmentation, ExtrinSplat outperforms established embedding-based frameworks, validating the efficacy and efficiency of the proposed extrinsic paradigm. useful for ...
- Recently, 3D Gaussian Splatting (3DGS) has been proposed, which achieves high-fidelity modeling and rendering while maintaining high rendering speeds, making it an ideal foundation for next-generation 3D scene ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- More recently, a few approaches have explored embedding semantic features into each Gaussian via matching, which optimizes costs and achieves strong results.
- To overcome these limitations, we introduce ExtrinSplat, a framework built on the extrinsic paradigm that decouples geometry from semantics.
- While this paradigm has shown promising results, it suffers from three limitations: 1) Geom

## Abstract Cue
- Lifting 2D open-vocabulary understanding into 3D Gaussian Splatting (3DGS) scenes is a critical challenge.
