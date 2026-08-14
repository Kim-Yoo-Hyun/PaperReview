# Problem

- Year/Venue: 2023 / CoRL
- Category: Robot Learning and Data
- Tags: Robotics, cross-embodiment, skill discovery, human video, Imitation Learning, Diffusion
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://xskill.cs.columbia.edu/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- Meanwhile, our approach differs from existing work on single-embodiment skill discovery , which solely relies on on-robot demonstration data.
- By learning cross-embodiment skill prototypes, our framework can use direct human demonstration, which is more cost-effective and scalable, even for non-expert demonstrators.
- With the proposed skill alignment transformer, the algorithm can robustly align skills in the human video to the robot visual observation, despite the embodiment difference and unexpected execution ...

## 해결하려는 문제
- Our experiments in simulation and real-world environments show that the discovered skill prototypes facilitate both skill transfer and composition for unseen tasks, resulting in a more general and ...
- The benchmark, code, and qualitative results are on project website.
- To bridge this embodiment gap, this paper introduces XSkill, an imitation learning framework that 1) discovers a cross-embodiment representation called skill prototypes purely from unlabeled human and robot ...

## 선행 연구 / 배경 단서
- Meanwhile, our approach differs from existing work on single-embodiment skill discovery , which solely relies on on-robot demonstration data.
- With the proposed skill alignment transformer, the algorithm can robustly align skills in the human video to the robot visual observation, despite the embodiment difference and unexpected execution ...
- By learning cross-embodiment skill prototypes, our framework can use direct human demonstration, which is more cost-effective and scalable, even for non-expert demonstrators.
