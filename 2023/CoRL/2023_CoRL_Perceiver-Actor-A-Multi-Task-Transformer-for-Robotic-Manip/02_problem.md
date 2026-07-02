# Problem

- Year/Venue: 2023 / CoRL
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Robotics, Imitation Learning, 3D manipulation
- Paper link: ./2023/CoRL/2023_CoRL_Perceiver-Actor-A-Multi-Task-Transformer-for-Robotic-Manip/paper.pdf
- Code/Project: https://peract.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Can we still bring the power of Transformers to 6-DoF manipulation with the right problem formulation?
- Thus, while Transformers may be domain agnostic, they still require the right problem formulation to be data efficient.
- P ER ACT is essentially a classifier trained with supervised learning to detect actions akin to prior work like CLIPort , except our observations and actions are represented ...

## 해결하려는 문제
- Our results show that P ER ACT significantly outperforms unstructured image-to-action agents and 3D ConvNet baselines for a wide range of tabletop tasks.
- Can manipulation still benefit from Transformers with the right problem formulation?
- With this formulation, we train a single multi-task Transformer for 18 RLBench tasks (with 249 variations) and 7 real-world tasks (with 18 variations) from just a few demonstrations ...

## 선행 연구 / 배경 단서
- By framing problems as sequence modeling tasks, and training on large amounts of diverse data, Transformers have achieved groundbreaking results in several domains .
- Can we still bring the power of Transformers to 6-DoF manipulation with the right problem formulation?
- In summary, our contributions are as follows: • A novel problem formulation for perceiving, acting, and specifying goals with Transformers. • An efficient action-centric framework for grounding language ...
