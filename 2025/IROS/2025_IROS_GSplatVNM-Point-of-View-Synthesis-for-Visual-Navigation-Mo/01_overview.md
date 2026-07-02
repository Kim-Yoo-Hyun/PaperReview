# GSplatVNM: Point-of-View Synthesis for Visual Navigation Models Using Gaussian Splatting

- Year/Venue: 2025 / IROS
- Category: Navigation and Embodied AI
- Tags: Navigation, Gaussian Splatting
- Paper link: ./2025/IROS/2025_IROS_GSplatVNM-Point-of-View-Synthesis-for-Visual-Navigation-Mo/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- To address these challenges, we propose a 3DGS-based viewpoint synthesis framework for VNMs that synthesizes intermediate viewpoints to seamlessly bridge gaps in sparse data while significantly reducing storage ...
- However, constructing a dense and traversable sequence of target viewpoints from start to goal remains a central challenge, particularly when the available image database is sparse.
- Existing methods construct an Image-based Topological Graph (ITG) to describe the traversability between randomly sampled images in the environment , which necessitates collecting a sufficient number of images ...

## Core Idea
- To address these challenges, we propose a 3DGS-based viewpoint synthesis framework for VNMs that synthesizes intermediate viewpoints to seamlessly bridge gaps in sparse data while significantly reducing storage ...
- VNMs offer a promising paradigm for image-goal navigation by guiding a robot through a sequence of point-of-view images without requiring metrical localization or environment-specific training.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experimental results in a photorealistic simulator demonstrate that our approach not only enhances navigation efficiency but also exhibits robustness under varying levels of image database sparsity.
- In particular, recent advances in image-to-waypoints Visual Navigation Models (VNMs) – have demonstrated zeroshot navigation capabilities without precise self-localization using dense point clouds , , thereby reducing the ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Experimental results in a photorealistic simulator demonstrate that our approach not only enhances navigation efficiency but also exhibits robustness under varying levels of image database sparsity.
- To address these challenges, we propose a 3DGS-based viewpoint synthesis framework for VNMs that synthesizes intermediate viewpoints to seamlessly bridge gaps in sparse data while significantly reducing storage ...
- VNMs offer a promising paradigm for image-goal navigation by guiding a robot through a sequence of point-of-view images without requiring metrical localization or environment-specific training.

## Abstract Cue
- — This paper presents a novel approach to imagegoal navigation by integrating 3D Gaussian Splatting (3DGS) with Visual Navigation Models (VNMs), a method we refer to as GSplatVNM.
