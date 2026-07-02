# Problem

- Year/Venue: 2026 / ICML
- Category: 3D Semantic Understanding and Alignment
- Tags: semantic, alignment, depth, 3D Vision
- Paper link: ./2026/ICML/2026_ICML_PRISM-Learning-Realistic-Depth-via-Physics-Grounded-Noise/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Existing sensor modelings typically treat depth noise as a monolithic black-box process, overlooking the distinct physical mechanisms that govern different error modalities.
- The Anatomy of Depth Perception and Modeling. (a) The Reality Gap: Unlike pristine simulation, real-world physical sensing exhibits a bimodal noise distribution: black voids and gray residuals. (b) ...
- Depth (a) The Sim2Real Gap of Depth Perception Monolithic Black-box Noise Modeling Large-scale Dataset from Simulation PRISM via Noise Disentanglement (Ours) Noise Entangled Physics-agnostic One-size-fits-all Noise Disentangled Physics-grounded ...

## 해결하려는 문제
- Extensive benchmarks demonstrate that PRISM achieves state-of-the-art fidelity in noisy depth synthesis.
- Furthermore, downstream robotic experiments show that PRISM facilitates a 92.1% average success rate in the real world, marking a significant improvement over monolithic baselines.
- Building on this insight, we propose PRISM, a tripartite framework that distills 3D Visual Foundation Model features as rich spatialsemantic priors for physics-based reasoning.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
