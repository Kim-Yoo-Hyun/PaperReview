# Method

- Year/Venue: 2023 / CoRL
- Category: Robot Learning and Data
- Tags: Robotics, cross-embodiment, skill discovery, human video, Imitation Learning, Diffusion
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://xskill.cs.columbia.edu/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- The XSkill framework consists of three phases: Discover §3.1, Transfer §3.2, and Compose §3.3 that uses three different data sources.
- To ensure that the skill representation focuses on underlying skills rather than embodiment and is aligned across embodiments, XSkill employs a combination of data sampling and entropy regularization ...
- Then, we extract the skill representation zij = ftemporal (vij ) from each video clip with a temporal skill encoder consisting of a vision backbone and a transformer ...

## 원리적 동기
- Meanwhile, our approach differs from existing work on single-embodiment skill discovery , which solely relies on on-robot demonstration data.
- By learning cross-embodiment skill prototypes, our framework can use direct human demonstration, which is more cost-effective and scalable, even for non-expert demonstrators.
- The XSkill framework consists of three phases: Discover §3.1, Transfer §3.2, and Compose §3.3 that uses three different data sources.

## 핵심 방법론
- The XSkill framework consists of three phases: Discover §3.1, Transfer §3.2, and Compose §3.3 that uses three different data sources.
- To ensure that the skill representation focuses on underlying skills rather than embodiment and is aligned across embodiments, XSkill employs a combination of data sampling and entropy regularization ...
- Then, we extract the skill representation zij = ftemporal (vij ) from each video clip with a temporal skill encoder consisting of a vision backbone and a transformer ...
- In each training iteration, XSkill samples video clips from the same embodiment and constructs a batch.
- 3 • Regularizing the training process using Sinkhorn-Knopp clustering within singleembodiment batches.
