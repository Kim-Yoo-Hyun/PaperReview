# Method

- Year/Venue: 2025 / CoRL
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, grasping, synthetic data
- Paper link: ./2025/CoRL/2025_CoRL_GraspVLA-a-Grasping-Foundation-Model-Pre-trained-on-Billio/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- In summary, our contributions are as follows: a) we introduce a novel pretraining paradigm that relies entirely on synthetic action data, significantly reducing the real world action data ...
- To efficiently learn from this dataset, we propose GraspVLA, an end-to-end network that integrates autoregressive perception tasks and flow-matching-based action generation into a unified Chainof-Thought (CoT) process, named ...
- Building on this, we present GraspVLA, a VLA model pretrained on large-scale synthetic action data as a foundational model for grasping tasks.

## 원리적 동기
- However, unlike vision and language modalities, action data is absent from existing Internet datasets, demanding a new paradigm for data collection.
- However, gathering real-world data at a large scale is both labor-intensive and costly, requiring a large number of robots and human operators, as well as diverse physical setups.
- In summary, our contributions are as follows: a) we introduce a novel pretraining paradigm that relies entirely on synthetic action data, significantly reducing the real world action data ...

## 핵심 방법론
- In summary, our contributions are as follows: a) we introduce a novel pretraining paradigm that relies entirely on synthetic action data, significantly reducing the real world action data ...
- To efficiently learn from this dataset, we propose GraspVLA, an end-to-end network that integrates autoregressive perception tasks and flow-matching-based action generation into a unified Chainof-Thought (CoT) process, named ...
- To this end, we systematically explore the potential of synthetic data for training VLA models.
- To the best of our knowledge, this is the first work to reveal the significant potential of synthetic data in training VLA models for manipulation.
- This design enables joint training on synthetic and Internet data in a unified framework, where Internet data is used to train the perception tasks (partial CoT process), and ...
