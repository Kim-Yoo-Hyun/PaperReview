# Method

- Year/Venue: 2025 / IROS
- Category: Navigation and Embodied AI
- Tags: Navigation, Gaussian Splatting
- Paper link: ./2025/IROS/2025_IROS_GSplatVNM-Point-of-View-Synthesis-for-Visual-Navigation-Mo/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To address these challenges, we propose a 3DGS-based viewpoint synthesis framework for VNMs that synthesizes intermediate viewpoints to seamlessly bridge gaps in sparse data while significantly reducing storage ...
- VNMs offer a promising paradigm for image-goal navigation by guiding a robot through a sequence of point-of-view images without requiring metrical localization or environment-specific training.
- — This paper presents a novel approach to imagegoal navigation by integrating 3D Gaussian Splatting (3DGS) with Visual Navigation Models (VNMs), a method we refer to as GSplatVNM.

## 원리적 동기
- To address these challenges, we propose a 3DGS-based viewpoint synthesis framework for VNMs that synthesizes intermediate viewpoints to seamlessly bridge gaps in sparse data while significantly reducing storage ...
- However, constructing a dense and traversable sequence of target viewpoints from start to goal remains a central challenge, particularly when the available image database is sparse.
- To address these challenges, we propose a 3DGS-based viewpoint synthesis framework for VNMs that synthesizes intermediate viewpoints to seamlessly bridge gaps in sparse data while significantly reducing storage ...

## 핵심 방법론
- SR PE-SR VF-SR Greigsville NoMaD w/o ITG NoMaD w/ ITG GSplatVNM 0.47 0.42 0.55 0.27 0.27 0.39 0.22 0.48 0.38 Ribera NoMaD w/o ITG NoMaD w/ ITG GSplatVNM ...
