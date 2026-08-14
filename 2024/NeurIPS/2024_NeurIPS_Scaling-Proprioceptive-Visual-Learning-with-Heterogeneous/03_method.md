# Method

- Year/Venue: 2024 / NeurIPS
- Category: Robot Learning and Data
- Tags: Robotics, cross-embodiment, proprioception, visual representation, heterogeneous data, Transformer
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://liruiw.github.io/hpt/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- To handle the heterogeneity common in robotics, we propose HPT, a modular architecture and framework to embrace this heterogeneity through pre-training.
- We propose Heterogeneous Pre-trained Transformers (HPT), which pre-train a large, shareable trunk of a policy neural network to learn a task and embodiment agnostic shared representation.
- Although the model architecture and training procedure are modular and independent of embodiment setups, heterogeneous pre-training can converge slowly.

## 원리적 동기
- Recent progress in open-source large-scale data collection has made this path possible, but the heterogeneity (such as varying robot hardware and different environments) present in large-scale robotic data ...
- The heterogeneity in robotics presents a distinct challenge: different robots are physically different embodiments1 of hardware acting in different environments.
- To handle the heterogeneity common in robotics, we propose HPT, a modular architecture and framework to embrace this heterogeneity through pre-training.

## 핵심 방법론
- To handle the heterogeneity common in robotics, we propose HPT, a modular architecture and framework to embrace this heterogeneity through pre-training.
- Although the model architecture and training procedure are modular and independent of embodiment setups, heterogeneous pre-training can converge slowly.
- Also, this work has focused on supervised learning as the pre-training objective and the data size in tokens and training compute sizes in FLOPs only reach a moderate ...
