# Problem

- Year/Venue: 2024 / CoRL
- Category: Robot Learning and Data
- Tags: Robotics, embodiment, graph neural network, policy learning
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://sferrazza.cc/bot_site/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- Then, it applies a highly sparse mask at the attention layers, preventing each node from attending beyond its direct neighbors.
- Despite notable evidence of successful deployment of this architecture in the context of robot learning, we claim that vanilla transformers do not fully exploit the structure of the ...

## 해결하려는 문제
- Therefore, we propose Body Transformer (BoT), an architecture that leverages the robot embodiment by providing an inductive bias that guides the learning process.
- The resulting architecture outperforms the vanilla transformer, as well as the classical multilayer perceptron, in terms of task completion, scaling properties, and computational efficiency when representing either imitation ...
- Despite notable evidence of successful deployment of this architecture in the context of robot learning, we claim that vanilla transformers do not fully exploit the structure of the ...

## 선행 연구 / 배경 단서
- In contrast, we propose Body Transformer (BoT), an architecture that augments the attention mechanism of transformers by taking into account the spatial placement of sensors and actuators across ...
- Our contributions are listed below: • We propose the BoT architecture, which augments the transformer architecture with a novel masking that leverages the morphology of the robot body. ...
- Then, it applies a highly sparse mask at the attention layers, preventing each node from attending beyond its direct neighbors.
