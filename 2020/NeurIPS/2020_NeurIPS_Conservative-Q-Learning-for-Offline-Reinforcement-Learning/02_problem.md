# Problem

- Year/Venue: 2020 / NeurIPS
- Category: Robot Learning and Data
- Tags: Robotics, offline reinforcement learning, conservative learning, Q-learning
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://github.com/aviralkumar2907/CQL
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- However, applying RL to real-world problems consistently poses practical challenges: in contrast to the kinds of data-driven methods that have been successful in supervised learning , RL is ...
- If we can instead learn a conservative estimate of the value function, which provides a lower bound on the true values, this overestimation problem could be addressed.
- This in principle can make it possible to leverage large datasets, but in practice fully offline RL methods pose major technical difficulties, stemming from the distributional shift between ...

## 해결하려는 문제
- On both discrete and continuous control domains, we show that CQL substantially outperforms existing offline RL methods, often learning policies that attain 2-5 times higher final return, especially ...
- In this paper, we propose conservative Q-learning (CQL), which aims to address these limitations by learning a conservative Q-function such that the expected value of a policy under ...
- However, in practice, offline RL presents a major challenge, and standard off-policy RL methods can fail due to overestimation of values induced by the distributional shift between the ...

## 선행 연구 / 배경 단서
- However, applying RL to real-world problems consistently poses practical challenges: in contrast to the kinds of data-driven methods that have been successful in supervised learning , RL is ...
- If we can instead learn a conservative estimate of the value function, which provides a lower bound on the true values, this overestimation problem could be addressed.
- Directly utilizing existing value-based off-policy RL algorithms in an offline setting generally results in poor performance, due to issues with bootstrapping from out-of-distribution actions and overfitting .
