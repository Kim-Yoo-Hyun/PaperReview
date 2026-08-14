# Method

- Year/Venue: 2020 / CoRL
- Category: Robot Learning and Data
- Tags: Robotics, Imitation Learning, Reinforcement Learning, long-horizon manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://relay-policy-learning.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- : We present relay policy learning, a method for imitation and reinforcement learning that can solve multi-stage, long-horizon robotic tasks.
- Second, our method does not require any explicit form of skill segmentation or subgoal definition, which otherwise would need to be learned or explicitly provided.
- In contrast to HRL methods, our method takes advantage of unstructured demonstrations to bootstrap further fine-tuning, and in contrast to conventional HIL methods, it does not focus on ...

## 원리적 동기
- We can simplify the above-mentioned problems by utilizing extra supervision in the form of unstructured human demonstrations, in which case the question becomes: how should we best use ...
- Hierarchical reinforcement learning (HRL) has been proposed as a potential solution that should scale to challenging long-horizon problems, by explicitly introducing temporal abstraction.
- : We present relay policy learning, a method for imitation and reinforcement learning that can solve multi-stage, long-horizon robotic tasks.

## 핵심 방법론
- Second, our method does not require any explicit form of skill segmentation or subgoal definition, which otherwise would need to be learned or explicitly provided.
- In contrast to HRL methods, our method takes advantage of unstructured demonstrations to bootstrap further fine-tuning, and in contrast to conventional HIL methods, it does not focus on ...
