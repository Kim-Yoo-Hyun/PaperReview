# RealVLG-R1: A Large-Scale Real-World Visual-Language Grounding Benchmark for Robotic Perception and Manipulation

- Year/Venue: 2026 / CVPR
- Category: Benchmarks and Datasets
- Tags: Visual-Language Grounding, Benchmark, Robotics
- Paper link: ./2026/CVPR/2026_CVPR_RealVLG-R1-A-Large-Scale-Real-World-Visual-Language-Ground/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Existing VLG approaches focus on coarse-grained, object-level localization, while traditional robotic grasping methods rely predominantly on geometric cues and lack language guidance, which limits their applicability in language-driven ...
- To address these limitations, we propose the RealVLG framework, which integrates the RealVLG11B dataset and the RealVLG-R1 model to unify real-world visual-language grounding and grasping tasks.

## Core Idea
- To address these limitations, we propose the RealVLG framework, which integrates the RealVLG11B dataset and the RealVLG-R1 model to unify real-world visual-language grounding and grasping tasks.
- This comprehensive and integrated methodology establishes a unified, quantifiable standard for comparing model architectures across visual-language grounding and grasping tasks.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experimental results demonstrate that RealVLG supports zeroshot perception and manipulation in real-world unseen environments, establishing a unified semantic-visual multimodal benchmark that provides a comprehensive data and evaluation platform ...
- The predicted contact points P1p , P2p are first converted into a rectangular grasp pose Gp with fixed width, and then the rectangle alignment and point accuracy are ...
- Based on the annotation pipeline described above, RealVLG-11B achieves a unified integration of multiple real-world grasping datasets, producing high-quality, multigranularity visual-language annotations.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Experimental results demonstrate that RealVLG supports zeroshot perception and manipulation in real-world unseen environments, establishing a unified semantic-visual multimodal benchmark that provides a comprehensive data and evaluation platform ...
- To address these limitations, we propose the RealVLG framework, which integrates the RealVLG11B dataset and the RealVLG-R1 model to unify real-world visual-language grounding and grasping tasks.
- Existing VLG approaches focus on coarse-grained, object-level localization, while traditional robotic grasping methods rely predominantly on geometric cues and lack language guidance, which limits their applicability in language-driven ...

## Abstract Cue
- Visual-language grounding aims to establish semantic correspondences between natural language and visual entities, enabling models to accurately identify and localize target objects based on textual instructions.
