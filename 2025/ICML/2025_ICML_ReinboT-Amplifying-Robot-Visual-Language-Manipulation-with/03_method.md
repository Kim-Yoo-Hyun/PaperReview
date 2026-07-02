# Method

- Year/Venue: 2025 / ICML Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Robotics, Reinforcement Learning
- Paper link: ./2025/ICML/2025_ICML_ReinboT-Amplifying-Robot-Visual-Language-Manipulation-with/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Different from these studies, we aim to propose a new end-to-end reinforced VLA model based on dense rewards that capture the characteristics of manipulation tasks. • We propose ...
- Moreover, based on the GPT-style transformer (Radford, 2018), we introduce three prediction token embeddings ([RTG], [ACTION] and [IMAGE]) to predict ReturnToGo, robot action, and future image state respectively.
- To this end, we propose Reinforced robot GPT (ReinboT), a novel end-to-end VLA model to implement the RL concept of maximizing dense returns.

## 원리적 동기
- In terms of ReinboT algorithm design, we consider that accurate estimation of the value function in RL algorithms has always been a thorny problem, especially in the Transformer ...
- However, these reward designs face the credit assignment problem that has not been fully solved in RL (Sutton, 1984), or are limited by the hallucination problem of LLM ...
- Different from these studies, we aim to propose a new end-to-end reinforced VLA model based on dense rewards that capture the characteristics of manipulation tasks. • We propose ...

## 핵심 방법론
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
