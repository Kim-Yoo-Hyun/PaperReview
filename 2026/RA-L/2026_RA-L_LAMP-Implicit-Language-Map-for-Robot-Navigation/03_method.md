# Method

- Year/Venue: 2026 / RA-L
- Category: Navigation and Embodied AI
- Tags: Robotics, Navigation
- Paper link: ./2026/RA-L/2026_RA-L_LAMP-Implicit-Language-Map-for-Robot-Navigation/paper.pdf
- Code/Project: https://lab-of-ai-and-robotics.github.io/LAMP/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We introduce LAMP (Language Map), a novel neural language field-based navigation framework that learns a continuous, language-driven map and directly leverages it for fine-grained path generation.
- Unlike prior approaches, our method encodes language features as an implicit neural field rather than storing them explicitly at every location.
- Our method addresses these issues, accurately detecting the objects and enabling fine-grained goal reaching through optimization.

## 원리적 동기
- However, existing methods that explicitly store language vectors in grid or node-based maps struggle to scale to large environments due to excessive memory requirements and limited resolution for ...
- By combining this implicit representation with a sparse graph, LAMP supports efficient coarse path planning and then performs gradient-based optimization in the learned field to refine poses near ...
- We introduce LAMP (Language Map), a novel neural language field-based navigation framework that learns a continuous, language-driven map and directly leverages it for fine-grained path generation.

## 핵심 방법론
- Our method addresses these issues, accurately detecting the objects and enabling fine-grained goal reaching through optimization.
- In the Extinguisher scene, the node-based method fails because it does not directly observe the goal, whereas our method correctly identifies the target by leveraging the implicit network ...
- In Table III, we compare our method against traditional sampling strategies: Random Node (RN) and Random Degree Node (RDN) , which select nodes uniformly at random and based ...
- Unlike conventional methods that rely solely on edge information, our approach leverages implicit information from each node in large graphs, specifically using a neural network to derive an ...
