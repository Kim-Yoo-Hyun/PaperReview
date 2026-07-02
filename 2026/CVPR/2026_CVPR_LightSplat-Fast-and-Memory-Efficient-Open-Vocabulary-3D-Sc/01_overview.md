# LightSplat: Fast and Memory-Efficient Open-Vocabulary 3D Scene Understanding in Five Seconds

- Year/Venue: 2026 / CVPR
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Gaussian Splatting, open-vocabulary, efficiency
- Paper link: ./2026/CVPR/2026_CVPR_LightSplat-Fast-and-Memory-Efficient-Open-Vocabulary-3D-Sc/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- However, existing approaches remain slow, memory-intensive, and overly complex due to iterative optimization and dense per-Gaussian feature assignments.
- Despite recent advances, existing methods still suffer from three major
- By assigning semantic indices only to salient regions and managing them with a lightweight index-feature mapping, LightSplat eliminates costly feature optimization and storage overhead.

## Core Idea
- To address this, we propose LightSplat, a fast and memory-efficient training-free framework that injects compact 2-byte semantic indices into 3D representations from multi-view images.
- To enable efficient language-to-3D alignment, 3D Gaussian Splatting (3DGS) provides an explicit representation with real-time rendering.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- As a result, LightSplat achieves state-of-the-art performance with up to 50-400× speedup and 64× lower memory, enabling scalable language-driven 3D understanding.
- LightSplat achieves 50× faster feature distillation, higher accuracy, and 64× lower memory usage.
- We evaluate our method on LERF-OVS, ScanNet, and DL3DV-OVS across complex indoor-outdoor scenes.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- To address this, we propose LightSplat, a fast and memory-efficient training-free framework that injects compact 2-byte semantic indices into 3D representations from multi-view images.
- We evaluate our method on LERF-OVS, ScanNet, and DL3DV-OVS across complex indoor-outdoor scenes.
- As a result, LightSplat achieves state-of-the-art performance with up to 50-400× speedup and 64× lower memory, enabling scalable language-driven 3D understanding.

## Abstract Cue
- Kyungdon Joo1† jh4011@postech.ac.kr x50 Faster Open-vocabulary 3D scene understanding enables users to segment novel objects in complex 3D environments through natural language.
