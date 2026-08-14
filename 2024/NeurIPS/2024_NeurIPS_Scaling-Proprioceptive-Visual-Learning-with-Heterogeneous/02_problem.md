# Problem

- Year/Venue: 2024 / NeurIPS
- Category: Robot Learning and Data
- Tags: Robotics, cross-embodiment, proprioception, visual representation, heterogeneous data, Transformer
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://liruiw.github.io/hpt/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- Recent progress in open-source large-scale data collection has made this path possible, but the heterogeneity (such as varying robot hardware and different environments) present in large-scale robotic data ...
- The heterogeneity in robotics presents a distinct challenge: different robots are physically different embodiments1 of hardware acting in different environments.
- Previous works have made significant progress in pre-training only the vision part of the policy on human videos and pre-training the full policy with a unified model and ...

## 해결하려는 문제
- We conduct experiments to investigate the scaling behaviors of training objectives, to the extent of 52 datasets.
- We propose Heterogeneous Pre-trained Transformers (HPT), which pre-train a large, shareable trunk of a policy neural network to learn a task and embodiment agnostic shared representation.
- This work studies the problem of learning policy representations through heterogeneous pretraining on robot data across different embodiments and tasks at scale.

## 선행 연구 / 배경 단서
- Previous works have made significant progress in pre-training only the vision part of the policy on human videos and pre-training the full policy with a unified model and ...
- Recent progress in open-source large-scale data collection has made this path possible, but the heterogeneity (such as varying robot hardware and different environments) present in large-scale robotic data ...
- The heterogeneity in robotics presents a distinct challenge: different robots are physically different embodiments1 of hardware acting in different environments.
