# Method

- Year/Venue: 2025 / NeurIPS Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Robotics, Reinforcement Learning
- Paper link: ./2025/NeurIPS/2025_NeurIPS_DreamVLA-A-Vision-Language-Action-Model-Dreamed-with-Compr/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To address these limitations, we propose DreamVLA, a novel VLA framework that integrates comprehensive world knowledge forecasting to enable inverse dynamics modeling, thereby establishing a perceptionprediction-action loop for ...
- To mitigate interference among the dynamic, spatial and semantic information during training, we adopt a block-wise structured attention mechanism that masks their mutual attention, preventing information leakage and ...
- As illustrated in Figure 2, our DreamVLA framework comprises three core modules operating within a unified transformer architecture.

## 원리적 동기
- Despite early success in incorporating dense visual forecasting, these methods naturally exhibit limitations: (1) Redundant pixel information: There exists significant overlap between forecasted images and current observations, making ...
- Therefore, we argue that existing methods (Figure 1 (a-c)) are insufficient to forecast future states for a more comprehensive prediction-action loop in the context of world-level future knowledge.
- To address these limitations, we propose DreamVLA, a novel VLA framework that integrates comprehensive world knowledge forecasting to enable inverse dynamics modeling, thereby establishing a perceptionprediction-action loop for ...

## 핵심 방법론
- As illustrated in Figure 2, our DreamVLA framework comprises three core modules operating within a unified transformer architecture.
- We encode language instructions using CLIP text embeddings, visual frames through a Masked Autoencoder to obtain spatiotemporal patch representations, and proprioceptive signals via several convolutional and fully-connected layers.
- Firstly, heterogeneous inputs—including natural language l, visual observations ot , and proprioceptive states st —are individually processed by modality-specific encoders.
