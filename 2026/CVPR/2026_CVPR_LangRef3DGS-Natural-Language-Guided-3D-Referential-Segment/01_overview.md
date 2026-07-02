# LangRef3DGS: Natural Language-Guided 3D Referential Segmentation from Partial Observations via 3D Gaussian Splatting

- Year/Venue: 2026 / CVPR
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Gaussian Splatting, referring segmentation, language
- Paper link: ./2026/CVPR/2026_CVPR_LangRef3DGS-Natural-Language-Guided-3D-Referential-Segment/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Despite significant progress in 3D semantic segmentation, existing methods remain constrained by several inherent limitations.
- These limitations originate from two intertwined factors.
- Unsupervised or self-supervised approaches attempt to mitigate this issue by leveraging geometric consistency or contrastive learning, yet they often assume a fixed data distribution and fail to generalize ...

## Core Idea
- To overcome this, we present a real-time framework that leverages 3D Gaussian Splatting (3DGS) to build a semantically continuous and differentiable embedding field from partial observations.
- Despite significant missing data (e.g., the stuffed bear, plate, and cookies are partially unobserved), our method accurately segments objects of varying scales—from the large tea glass to the ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments on challenging benchmarks demonstrate that our method achieves strong performance, exhibiting superior accuracy, robustness to partial inputs, and a powerful capacity for novel class discovery.Our code ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Extensive experiments on challenging benchmarks demonstrate that our method achieves strong performance, exhibiting superior accuracy, robustness to partial inputs, and a powerful capacity for novel class discovery.Our code ...
- To overcome this, we present a real-time framework that leverages 3D Gaussian Splatting (3DGS) to build a semantically continuous and differentiable embedding field from partial observations.
- Despite significant missing data (e.g., the stuffed bear, plate, and cookies are partially unobserved), our method accurately segments objects of varying scales—from the large tea glass to the ...

## Abstract Cue
- ng ssi i M Language-guided 3D segmentation is crucial for linking 3D perception with semantic understanding, yet it remains vulnerable to the sparse and occluded views common in real-world RGB-D data.
