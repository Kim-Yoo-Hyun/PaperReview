# Method

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2022 / CoRL
- Category: Robot Learning and Data
- Tags: Robotics, Imitation Learning, energy-based model, multimodal actions
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://implicitbc.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- We present extensive experiments on this finding, and we provide both intuitive insight and theoretical arguments distinguishing the properties of implicit models compared to their explicit counterparts, particularly ...
- For the image-based inputs, we also test two types of encoders with different forms of dimensionality reduction: spatial soft(arg)max and average pooling over dense features (see Appendix for ...
- The results in Table 4 (averaged # ResNet layers over 3 training runs with differMethod Input & Encoder 8 14

## 원리적 동기
- Although considerable research has been devoted to developing new imitation learning methods to address BC’s known limitations, here we investigate a fundamental design decision that has largely been ...
- 2 for definition) to represent the policy πθ : â=argmin Eθ (o,a) instead of â=Fθ (o) . a∈A This formulates imitation as a conditional energy-based modeling (EBM) problem ...
- We present extensive experiments on this finding, and we provide both intuitive insight and theoretical arguments distinguishing the properties of implicit models compared to their explicit counterparts, particularly ...

## 핵심 방법론
- For the image-based inputs, we also test two types of encoders with different forms of dimensionality reduction: spatial soft(arg)max and average pooling over dense features (see Appendix for ...
- The results in Table 4 (averaged # ResNet layers over 3 training runs with differMethod Input & Encoder 8 14
- Simulated Pushing consists of a simulated 6DoF robot Method Single Target, Multi Target, Single Target, xArm6 in PyBullet equipped with a small cylindrical states states pixels end effector.
- Planar Sweeping is a 2D environment that consists of an agent (in the form of a blue stick) where the task is to push a pile of 50 ...
- N-D Particle Integrator is a simple environment with linear dynamics but where a discontinuous oracle policy is used to generate training demonstrations: once within the vicinity of goal-conditioned ...
