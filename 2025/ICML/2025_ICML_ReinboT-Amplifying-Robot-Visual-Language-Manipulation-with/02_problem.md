# Problem

- Year/Venue: 2025 / ICML Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Robotics, Reinforcement Learning
- Paper link: ./2025/ICML/2025_ICML_ReinboT-Amplifying-Robot-Visual-Language-Manipulation-with/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- In terms of ReinboT algorithm design, we consider that accurate estimation of the value function in RL algorithms has always been a thorny problem, especially in the Transformer ...
- However, these reward designs face the credit assignment problem that has not been fully solved in RL (Sutton, 1984), or are limited by the hallucination problem of LLM ...
- In terms of combining with RL algorithms, these works mainly fine-tune existing VLA models that have undergone imitation learning, including introducing Q-functions to correct action distribution (Nakamoto et ...

## 해결하려는 문제
- Different from these studies, we aim to propose a new end-to-end reinforced VLA model based on dense rewards that capture the characteristics of manipulation tasks. • We propose ...
- Extensive experiments show that ReinboT achieves state-of-the-art performance on the CALVIN mixed-quality dataset and exhibits superior few-shot learning and out-of-distribution generalization capabilities in real-world tasks.
- In terms of ReinboT algorithm design, we consider that accurate estimation of the value function in RL algorithms has always been a thorny problem, especially in the Transformer ...

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
