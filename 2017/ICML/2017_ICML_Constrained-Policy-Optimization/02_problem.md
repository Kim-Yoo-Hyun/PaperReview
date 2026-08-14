# Problem

- Year/Venue: 2017 / ICML
- Category: World Models, Safety, and Recovery
- Tags: Robotics, safe reinforcement learning, constraints, policy optimization
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://github.com/jachiam/cpo
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- For many applications of reinforcement learning it can be more convenient to specify both a reward function and constraints, rather than trying to design behavior through the reward ...
- For example, systems that physically interact with or around humans should satisfy safety constraints.
- Recent advances in policy search algorithms (Mnih et al., 2016; Schulman et al., 2015; Lillicrap et al., 2016; Levine et al., 2016) have enabled new capabilities in highdimensional ...

## 해결하려는 문제
- Our method allows us to train neural network policies for high-dimensional control while making guarantees about policy behavior all throughout training.
- We demonstrate the effectiveness of our approach on simulated robot locomotion tasks where the agent must satisfy constraints motivated by safety.
- Introduction Recently, deep reinforcement learning has enabled neural network policies to achieve state-of-the-art performance on many high-dimensional control tasks, including Atari games (using pixels as inputs) (Mnih et ...

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
