# DUSt3R: Geometric 3D Vision Made Easy

- Year/Venue: 2024 / CVPR
- Category: 3D Reconstruction, Geometry, and SLAM
- Tags: 3D reconstruction, calibration, geometry
- Paper link: ./2024/CVPR/2024_CVPR_DUSt3R-Geometric-3D-Vision-Made-Easy/paper.pdf
- Code/Project: https://github.com/naver/dust3r
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- We cast the pairwise reconstruction problem as a regression of pointmaps, relaxing the hard constraints of usual projective camera models.
- This is possible because our network jointly processes the input images and the resulting 3D pointmaps, thus learning to associate 2D structures with 3D shapes, and having the ...

## Core Idea
- We base our network architecture on standard Transformer encoders and decoders, allowing us to leverage powerful pretrained models.
- Conclusion We presented a novel paradigm to solve not only 3D reconstruction in-the-wild without prior information about scene nor cameras, but a whole variety of 3D vision tasks ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Exhaustive experiments on all these tasks showcase that the proposed DUSt3R can unify various 3D vision tasks and set new SoTAs on monocular/multi-view depth estimation as well as ...
- We show 1 https://dust3r.europe.naverlabs.com 1.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We base our network architecture on standard Transformer encoders and decoders, allowing us to leverage powerful pretrained models.
- Exhaustive experiments on all these tasks showcase that the proposed DUSt3R can unify various 3D vision tasks and set new SoTAs on monocular/multi-view depth estimation as well as ...
- We drift away from the trend of integrating task-specific modules , and instead adopt a fully data-driven strategy based on a generic transformer a

## Abstract Cue
- that this formulation smoothly unifies the monocular and binocular reconstruction cases.
