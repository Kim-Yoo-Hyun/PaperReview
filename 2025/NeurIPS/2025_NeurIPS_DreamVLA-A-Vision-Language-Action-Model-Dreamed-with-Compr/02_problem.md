# Problem

- Year/Venue: 2025 / NeurIPS Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Robotics, Reinforcement Learning
- Paper link: ./2025/NeurIPS/2025_NeurIPS_DreamVLA-A-Vision-Language-Action-Model-Dreamed-with-Compr/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Despite early success in incorporating dense visual forecasting, these methods naturally exhibit limitations: (1) Redundant pixel information: There exists significant overlap between forecasted images and current observations, making ...
- Therefore, we argue that existing methods (Figure 1 (a-c)) are insufficient to forecast future states for a more comprehensive prediction-action loop in the context of world-level future knowledge.
- To incorporate future knowledge prediction into VLA, most existing methods [45, 5, 46–57] leverage a copilot generation model to generate future frames/keypoints, then predict action sequences conditioned on ...

## 해결하려는 문제
- Extensive experiments on both real-world and simulation environments demonstrate that DreamVLA achieves 76.7% success rate on real robot tasks and 4.44 average length on the CALVIN ABC-D benchmarks.
- To mitigate interference among the dynamic, spatial and semantic information during training, we adopt a block-wise structured attention mechanism that masks their mutual attention, preventing information leakage and ...
- Moreover, to model the conditional distribution over future actions, we employ a diffusion-based transformer that disentangles action representations from shared latent features.

## 선행 연구 / 배경 단서
- Despite early success in incorporating dense visual forecasting, these methods naturally exhibit limitations: (1) Redundant pixel information: There exists significant overlap between forecasted images and current observations, making ...
- Therefore, we argue that existing methods (Figure 1 (a-c)) are insufficient to forecast future states for a more comprehensive prediction-action loop in the context of world-level future knowledge.
- To incorporate future knowledge prediction into VLA, most existing methods [45, 5, 46–57] leverage a copilot generation model to generate future frames/keypoints, then predict action sequences conditioned on ...
