# Problem

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2018 / ICML
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, Reinforcement Learning, continuous control, maximum entropy
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://github.com/haarnoja/sac
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- However, these methods typically suffer from two major challenges: very high sample complexity and brittle convergence properties, which necessitate meticulous hyperparameter tuning.
- Both of these challenges severely limit the applicability of such methods to complex, real-world domains.
- Correspondence to: Tuomas Haarnoja <haarnoja@berkeley.edu>. of these methods in real-world domains has been hampered by two major challenges.

## 해결하려는 문제
- By combining off-policy updates with a stable stochastic actor-critic formulation, our method achieves state-of-the-art performance on a range of continuous control benchmark tasks, outperforming prior on-policy and off-policy ...
- Second, these methods are often brittle with respect to their hyperparameters: learning rates, exploration constants, and other settings must be set carefully for different problem settings to achieve ...
- Furthermore, we demonstrate that, in contrast to other off-policy algorithms, our approach is very stable, achieving very similar performance across different random seeds.

## 선행 연구 / 배경 단서
- UNVERIFIED — full text의 해당 section을 정독한 뒤 근거와 위치를 기록한다.
