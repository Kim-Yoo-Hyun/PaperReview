# Method

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2022 / CoRL
- Category: World Models, Safety, and Recovery
- Tags: Robotics, world model, real robot, model-based reinforcement learning
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://danijar.com/project/daydreamer/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- This section summarizes the general algorithm, as well as details on the training architecture and sensor fusion needed for the robotics experiments.
- The world model is based on the Recurrent State-Space Model (RSSM; Hafner et al., 2018), which consists of four components: Encoder Network: encθ (st | st−1 , at−1 ...
- We decouple learning updates from data collection to meet latency requirements and to enable fast training without waiting for the environment.

## 원리적 동기
- In this paper, we leverage recent advances of the Dreamer world model for training a variety of robots in the most straight-forward and fundamental problem setting: online reinforcement ...
- The tasks cover a range of challenges, including different action spaces, sensory modalities, and reward structures. • Walking in 1 Hour We teach a quadruped from scratch in ...
- This section summarizes the general algorithm, as well as details on the training architecture and sensor fusion needed for the robotics experiments.

## 핵심 방법론
- This section summarizes the general algorithm, as well as details on the training architecture and sensor fusion needed for the robotics experiments.
- The world model is based on the Recurrent State-Space Model (RSSM; Hafner et al., 2018), which consists of four components: Encoder Network: encθ (st | st−1 , at−1 ...
- We decouple learning updates from data collection to meet latency requirements and to enable fast training without waiting for the environment.
- This reduces accumulating errors and enables massively parallel training with a large batch size.
- The encoder network fuses all sensory inputs xt together into the stochastic representations zt .
