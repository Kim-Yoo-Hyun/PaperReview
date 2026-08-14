# Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained Transformers

- Year/Venue: 2024 / NeurIPS
- Category: Robot Learning and Data
- Tags: Robotics, cross-embodiment, proprioception, visual representation, heterogeneous data, Transformer
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://liruiw.github.io/hpt/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- Recent progress in open-source large-scale data collection has made this path possible, but the heterogeneity (such as varying robot hardware and different environments) present in large-scale robotic data ...
- The heterogeneity in robotics presents a distinct challenge: different robots are physically different embodiments1 of hardware acting in different environments.
- Previous works have made significant progress in pre-training only the vision part of the policy on human videos and pre-training the full policy with a unified model and ...

## Core Idea
- To handle the heterogeneity common in robotics, we propose HPT, a modular architecture and framework to embrace this heterogeneity through pre-training.
- We propose Heterogeneous Pre-trained Transformers (HPT), which pre-train a large, shareable trunk of a policy neural network to learn a task and embodiment agnostic shared representation.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- HPTs outperform several baselines and enhance the fine-tuned policy performance by over 20% on unseen tasks in multiple simulator benchmarks and real-world settings.
- We conduct experiments to investigate the scaling behaviors of training objectives, to the extent of 52 datasets.

## Limitation
- See Appendix §C for some failure modes.
- We hope this perspective will inspire future work in handling the heterogeneous nature of robotic data for robotic foundation models.
- We would like to thank Russ Tedrake for discussions and suggestions, Liane Xu for helping with real-world experiments, Tianhong Li for helping with cluster experiments, and Remi Cadene ...

## Contribution
- We conduct experiments to investigate the scaling behaviors of training objectives, to the extent of 52 datasets.
- We propose Heterogeneous Pre-trained Transformers (HPT), which pre-train a large, shareable trunk of a policy neural network to learn a task and embodiment agnostic shared representation.
- This work studies the problem of learning policy representations through heterogeneous pretraining on robot data across different embodiments and tasks at scale.

## Abstract Cue
- One of the roadblocks for training generalist robotic models today is heterogeneity.
