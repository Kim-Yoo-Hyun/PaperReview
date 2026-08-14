# Method

- Year/Venue: 2025 / NeurIPS Spotlight
- Category: Robot Learning and Data
- Tags: Robotics, learning from human videos, 3D motion field, cross-embodiment
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- Ablation Studies We also study the design choices of our Table 1: Policy Learning Ablation policy architecture and training.
- In this paper, we propose to use object-centric 3D motion field to represent actions for robot learning from human videos, and present a novel framework for extracting this ...
- We introduce two novel components in its implementation.

## 원리적 동기
- Recently, human-object interaction videos stand out as a particularly promising avenue to overcome this challenge.
- Unlike existing 3D tracking works that assume depth as a groundtruth reference, we recover accurate 3D object motion from noisy depth. amount of footage available from internet or ...
- Ablation Studies We also study the design choices of our Table 1: Policy Learning Ablation policy architecture and training.

## 핵심 방법론
- Ablation Studies We also study the design choices of our Table 1: Policy Learning Ablation policy architecture and training.
- Finally, we find it important to apply object masking augmentation during training, as the object’s silhouette under the robot gripper differs from that under a human hand, which ...
- Otherwise, the Full 35.0% irrelevant noise in non-object regions can slow down training and harm performance.
- Compared to Setting Success the Gaussian policy head, the diffusion policy can produce highw/o Diffusion (Diff.) 0.0% quality, accurate motion fields which is important for success. w/o Diff.
- We find that for fine-grained for Fine-grained Tasks. tasks, it is important to apply a diffusion model even if the human has tried to act as consistently as ...
