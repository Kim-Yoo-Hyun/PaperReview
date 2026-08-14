# Method

- Year/Venue: 2019 / Technical Report
- Category: World Models, Safety, and Recovery
- Tags: Robotics, safe reinforcement learning, Safety Gym, Benchmark, constraints
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://github.com/openai/safety-gym
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- Towards standardizing safety specifications: Based on a range of prior work, we propose to standardize constrained RL [Altman, 1999] as the main formalism for incorporating safety specifications into ...
- First, building on a wide range of prior work on safe reinforcement learning, we propose to standardize constrained RL as the main formalism for safe exploration.
- To address the gap, we present Safety Gym: a set of tools for accelerating safe exploration research.

## 원리적 동기
- While “sim-to-real” transfer learning algorithms may mitigate this issue, we expect that in problems centered on AI-human interaction or very complex systems, challenges in building useful simulators will ...
- While RL is not yet fully mature or ready to serve as an “off-the-shelf” solution, it appears to offer a viable path to solving hard sequential decision-making problems ...
- Towards standardizing safety specifications: Based on a range of prior work, we propose to standardize constrained RL [Altman, 1999] as the main formalism for incorporating safety specifications into ...

## 핵심 방법론
- Towards standardizing safety specifications: Based on a range of prior work, we propose to standardize constrained RL [Altman, 1999] as the main formalism for incorporating safety specifications into ...
- To address the gap, we present Safety Gym: a set of tools for accelerating safe exploration research.
- While “sim-to-real” transfer learning algorithms may mitigate this issue, we expect that in problems centered on AI-human interaction or very complex systems, challenges in building useful simulators will ...
- We recommend a protocol for evaluating constrained RL algorithms on Safety Gym environments based on three metrics: task performance of the final policy, constraint satisfaction of the final ...
- When all training occurs in a simulator, this is usually not concerning, but exploration of this kind in the real world could produce unacceptable catastrophes.
