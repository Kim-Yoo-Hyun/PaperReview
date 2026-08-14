# Problem

- Year/Venue: 2026 / CVPR
- Category: VLA and Generalist Robot Policies
- Tags: Robotics, VLA, atomic skills, skill composition, long-horizon manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_AtomicVLA_Unlocking_the_Potential_of_Atomic_Skill_Learning_in_Robots_CVPR_2026_paper.html
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- These challenges present significant barriers for existing VLA models, which use monolithic action decoders trained on aggregated data, resulting in poor scalability.
- To address these challenges, we propose AtomicVLA, a unified planning-and-execution framework that jointly generates task-level plans, atomic skill abstractions, and fine-grained actions.
- However, real-world robotic tasks often involve longhorizon, multi-step problem-solving and require generalization for continual skill acquisition, extending beyond single actions or skills.

## 해결하려는 문제
- Furthermore, we introduce a flexible routing encoder that automatically assigns dedicated atomic experts to new skills, enabling continual learning.
- We validate our approach through extensive experiments.
- To address these challenges, we propose AtomicVLA, a unified planning-and-execution framework that jointly generates task-level plans, atomic skill abstractions, and fine-grained actions.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
