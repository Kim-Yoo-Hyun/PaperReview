# Body Transformer: Leveraging Robot Embodiment for Policy Learning

- Year/Venue: 2024 / CoRL
- Category: Robot Learning and Data
- Tags: Robotics, embodiment, graph neural network, policy learning
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://sferrazza.cc/bot_site/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- Then, it applies a highly sparse mask at the attention layers, preventing each node from attending beyond its direct neighbors.
- Despite notable evidence of successful deployment of this architecture in the context of robot learning, we claim that vanilla transformers do not fully exploit the structure of the ...

## Core Idea
- Our contributions are listed below: • We propose the BoT architecture, which augments the transformer architecture with a novel masking that leverages the morphology of the robot body. ...
- In contrast, we propose Body Transformer (BoT), an architecture that augments the attention mechanism of transformers by taking into account the spatial placement of sensors and actuators across ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We report results in the table shown in Figure 3a, where BoT consistently outperforms the MLP and transformer baselines.
- While the multi-clip policy is competitive with the vanilla transformer baseline, it is strongly outperformed by our architecture.
- 5.1 Imitation Learning Experiments We evaluate the imitation learning performance of the BoT architecture in a body-tracking task defined through the MoCapAct dataset , which comprises action-labeled humanoid ...

## Limitation
- We leave the extension of BoT to the temporal dimension as future work, as it promises to further improve real world deployment of robot policies, such as the ...

## Contribution
- Therefore, we propose Body Transformer (BoT), an architecture that leverages the robot embodiment by providing an inductive bias that guides the learning process.
- The resulting architecture outperforms the vanilla transformer, as well as the classical multilayer perceptron, in terms of task completion, scaling properties, and computational efficiency when representing either imitation ...
- Despite notable evidence of successful deployment of this architecture in the context of robot learning, we claim that vanilla transformers do not fully exploit the structure of the ...

## Abstract Cue
- : In recent years, the transformer architecture has become the de facto standard for machine learning algorithms applied to natural language processing and computer vision.
