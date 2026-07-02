# PRISM: Learning Realistic Depth via Physics-Grounded Noise Disentanglement with Semantic-Geometric Collaboration

- Year/Venue: 2026 / ICML
- Category: 3D Semantic Understanding and Alignment
- Tags: semantic, alignment, depth, 3D Vision
- Paper link: ./2026/ICML/2026_ICML_PRISM-Learning-Realistic-Depth-via-Physics-Grounded-Noise/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Existing sensor modelings typically treat depth noise as a monolithic black-box process, overlooking the distinct physical mechanisms that govern different error modalities.
- The Anatomy of Depth Perception and Modeling. (a) The Reality Gap: Unlike pristine simulation, real-world physical sensing exhibits a bimodal noise distribution: black voids and gray residuals. (b) ...
- Depth (a) The Sim2Real Gap of Depth Perception Monolithic Black-box Noise Modeling Large-scale Dataset from Simulation PRISM via Noise Disentanglement (Ours) Noise Entangled Physics-agnostic One-size-fits-all Noise Disentangled Physics-grounded ...

## Core Idea
- Building on this insight, we propose PRISM, a tripartite framework that distills 3D Visual Foundation Model features as rich spatialsemantic priors for physics-based reasoning.
- In this work, we introduce a physics-grounded paradigm that disentangles monolithic noise into two complementary modalities: sensing invalidation and measurement inaccuracy, enabling a tailored treatment of noise sources ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive benchmarks demonstrate that PRISM achieves state-of-the-art fidelity in noisy depth synthesis.
- Furthermore, downstream robotic experiments show that PRISM facilitates a 92.1% average success rate in the real world, marking a significant improvement over monolithic baselines.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Extensive benchmarks demonstrate that PRISM achieves state-of-the-art fidelity in noisy depth synthesis.
- Furthermore, downstream robotic experiments show that PRISM facilitates a 92.1% average success rate in the real world, marking a significant improvement over monolithic baselines.
- Building on this insight, we propose PRISM, a tripartite framework that distills 3D Visual Foundation Model features as rich spatialsemantic priors for physics-based reasoning.

## Abstract Cue
- Idealized Artifact-free Real-world physical sensing exhibits complex, heterogeneous noise patterns that deviate significantly from idealized simulation, posing a fundamental bottleneck for sim-to-real transfer.
