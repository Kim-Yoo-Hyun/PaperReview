# Problem

- Year/Venue: 2011 / AISTATS
- Category: Foundations: RL and Imitation Learning
- Tags: Robotics, Imitation Learning, policy learning
- Paper link: ./2011/AISTATS/2011_AISTATS_A-Reduction-of-Imitation-Learning-and-Structured-Predictio/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Sequence Prediction problems arise commonly in practice.
- In complex robotic systems where standard control methods fail, we must often resort to learning a controller that can make such predictions.
- Sequential prediction problems such as imitation learning, where future observations depend on previous predictions (actions), violate the common i.i.d. assumptions made in statistical learning.

## 해결하려는 문제
- We demonstrate that this new approach outperforms previous approaches on two challenging imitation learning problems and a benchmark sequence labeling problem.
- In this paper, we propose a new iterative algorithm, which trains a stationary deterministic policy, that can be seen as a no regret algorithm in an online learning ...
- We show that any such no regret algorithm, combined with additional reduction assumptions, must find a policy with good performance under the distribution of observations it induces in ...

## 선행 연구 / 배경 단서
- Sequence Prediction problems arise commonly in practice.
- In complex robotic systems where standard control methods fail, we must often resort to learning a controller that can make such predictions.
