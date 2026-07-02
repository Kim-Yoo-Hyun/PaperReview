# Problem

- Year/Venue: 2026 / ICRA
- Category: Navigation and Embodied AI
- Tags: Vision-Language Model, Navigation
- Paper link: ./2026/ICRA/2026_ICRA_TagaVLM-Topology-Aware-Global-Action-Reasoning-for-Vision/paper.pdf
- Code/Project: not identified from venue audit
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- — Vision-Language Navigation (VLN) presents a unique challenge for Large Vision-Language Models (VLMs) due to their inherent architectural mismatch: VLMs are primarily pretrained on static, disembodied vision-language tasks, ...
- Existing largemodel-based methods often resort to converting rich visual and spatial information into text, forcing models to implicitly infer complex visual-topological relationships or limiting their global action capabilities.

## 해결하려는 문제
- On the R2R benchmark, TagaVLM achieves state-of-the-art performance among large-model-based methods, with a Success Rate (SR) of 51.09% and SPL of 47.18 in unseen environments, outperforming prior work ...
- To bridge this gap, we propose TagaVLM (Topology-Aware Global Action reasoning), an endto-end framework that explicitly injects topological structures into the VLM backbone.
- To introduce topological edge information, Spatial Topology Aware Residual Attention (STAR-Att) directly integrates it into the VLM’s self-attention mechanism, enabling intrinsic spatial reasoning while preserving pretrained knowledge.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
