# Method

- Year/Venue: 2026 / ICRA
- Category: Navigation and Embodied AI
- Tags: Vision-Language Model, Navigation
- Paper link: ./2026/ICRA/2026_ICRA_TagaVLM-Topology-Aware-Global-Action-Reasoning-for-Vision/paper.pdf
- Code/Project: not identified from venue audit
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To bridge this gap, we propose TagaVLM (Topology-Aware Global Action reasoning), an endto-end framework that explicitly injects topological structures into the VLM backbone.
- To introduce topological edge information, Spatial Topology Aware Residual Attention (STAR-Att) directly integrates it into the VLM’s self-attention mechanism, enabling intrinsic spatial reasoning while preserving pretrained knowledge.
- Val Seen Backbone Val Unseen TL NE↓ OSR↑ SR↑ SPL↑ TL NE↓ OSR↑ SR↑ SPL↑ Seq2Seq Speaker Follower HAMT DUET BEVBert ScaleVLN LSTM LSTM Cross-Modal Transformer Cross-Modal Transformer ...

## 원리적 동기
- — Vision-Language Navigation (VLN) presents a unique challenge for Large Vision-Language Models (VLMs) due to their inherent architectural mismatch: VLMs are primarily pretrained on static, disembodied vision-language tasks, ...
- Existing largemodel-based methods often resort to converting rich visual and spatial information into text, forcing models to implicitly infer complex visual-topological relationships or limiting their global action capabilities.
- To bridge this gap, we propose TagaVLM (Topology-Aware Global Action reasoning), an endto-end framework that explicitly injects topological structures into the VLM backbone.

## 핵심 방법론
- Val Seen Backbone Val Unseen TL NE↓ OSR↑ SR↑ SPL↑ TL NE↓ OSR↑ SR↑ SPL↑ Seq2Seq Speaker Follower HAMT DUET BEVBert ScaleVLN LSTM LSTM Cross-Modal Transformer Cross-Modal Transformer ...
