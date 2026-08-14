# Method

- Year/Venue: 2024 / CoRL
- Category: Robot Learning and Data
- Tags: Robotics, embodiment, graph neural network, policy learning
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://sferrazza.cc/bot_site/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- Our contributions are listed below: • We propose the BoT architecture, which augments the transformer architecture with a novel masking that leverages the morphology of the robot body. ...
- In contrast, we propose Body Transformer (BoT), an architecture that augments the attention mechanism of transformers by taking into account the spatial placement of sensors and actuators across ...
- Therefore, we propose Body Transformer (BoT), an architecture that leverages the robot embodiment by providing an inductive bias that guides the learning process.

## 원리적 동기
- Then, it applies a highly sparse mask at the attention layers, preventing each node from attending beyond its direct neighbors.
- Despite notable evidence of successful deployment of this architecture in the context of robot learning, we claim that vanilla transformers do not fully exploit the structure of the ...
- Our contributions are listed below: • We propose the BoT architecture, which augments the transformer architecture with a novel masking that leverages the morphology of the robot body. ...

## 핵심 방법론
- Our contributions are listed below: • We propose the BoT architecture, which augments the transformer architecture with a novel masking that leverages the morphology of the robot body. ...
- In contrast, we propose Body Transformer (BoT), an architecture that augments the attention mechanism of transformers by taking into account the spatial placement of sensors and actuators across ...
- The transformer architecture has been developed for unstructured natural language processing (NLP) tasks, e.g., language translations, where the input sequences often map to reshuffled output sequences.
- This is particularly important for robots too, where however, learning architectures do not typically exploit spatial interrelations between sensors and actuators.
- In fact, robot policies have mostly been exploiting the same architectures developed for natural language or computer vision, without effectively leveraging the structure of the robot body.
