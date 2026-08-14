# Method

- Year/Venue: 2026 / ICLR Oral
- Category: Robot Learning and Data
- Tags: Robotics, kinematics, action representation, Imitation Learning
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- Additionally, we introduce a cross-attention layer following the self-attention layer to enable interactions between joint and link features and the input image tokens.
- To this end, we propose the Neural Rodrigues Operator, a learnable generalization of the classical forward kinematics operation, designed to inject kinematics-aware inductive bias into neural computation.
- Specifically, we apply our method to 3D hand reconstruction from single-view RGB images, which involves predicting the rotations and positions of hand joints based on the kinematic structure ...

## 원리적 동기
- I NTRODUCTION We study the problem of understanding and predicting the actions of articulated actors.
- However, common architectures such as MLPs and Transformers lack inductive biases that reflect the underlying kinematic structure of articulated systems.
- Additionally, we introduce a cross-attention layer following the self-attention layer to enable interactions between joint and link features and the input image tokens.

## 핵심 방법론
- Additionally, we introduce a cross-attention layer following the self-attention layer to enable interactions between joint and link features and the input image tokens.
- Specifically, we apply our method to 3D hand reconstruction from single-view RGB images, which involves predicting the rotations and positions of hand joints based on the kinematic structure ...
- Therefore, our approach is not limited to robotic applications, demonstrating its versatility and applicability to graphics-related tasks as well.
- We use the standard protocol and report metrics on 3D joint and 3D mesh accuracy.
- Our network builds upon HaMeR (Pavlakos et al., 2024) by replacing its vanilla transformer with the proposed Rodrigues Network (with modifications to suit MANO’s configuration representation).
