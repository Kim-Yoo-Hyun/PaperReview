# ReinboT: Amplifying Robot Visual-Language Manipulation with Reinforcement Learning

- Year/Venue: 2025 / ICML Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Robotics, Reinforcement Learning
- Paper link: ./2025/ICML/2025_ICML_ReinboT-Amplifying-Robot-Visual-Language-Manipulation-with/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- In terms of ReinboT algorithm design, we consider that accurate estimation of the value function in RL algorithms has always been a thorny problem, especially in the Transformer ...
- However, these reward designs face the credit assignment problem that has not been fully solved in RL (Sutton, 1984), or are limited by the hallucination problem of LLM ...
- In terms of combining with RL algorithms, these works mainly fine-tune existing VLA models that have undergone imitation learning, including introducing Q-functions to correct action distribution (Nakamoto et ...

## Core Idea
- Different from these studies, we aim to propose a new end-to-end reinforced VLA model based on dense rewards that capture the characteristics of manipulation tasks. • We propose ...
- Moreover, based on the GPT-style transformer (Radford, 2018), we introduce three prediction token embeddings ([RTG], [ACTION] and [IMAGE]) to predict ReturnToGo, robot action, and future image state respectively.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments show that ReinboT achieves state-of-the-art performance on the CALVIN mixed-quality dataset and exhibits superior few-shot learning and out-of-distribution generalization capabilities in real-world tasks.
- Different from these studies, we aim to propose a new end-to-end reinforced VLA model based on dense rewards that capture the characteristics of manipulation tasks. • We propose ...
- Specifically, we utilize expectile regression (Aigner et al., 1976; Sobotka & Kneib, 2012) to make the predicted return as close as possible to the maximum return that can ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Different from these studies, we aim to propose a new end-to-end reinforced VLA model based on dense rewards that capture the characteristics of manipulation tasks. • We propose ...
- Extensive experiments show that ReinboT achieves state-of-the-art performance on the CALVIN mixed-quality dataset and exhibits superior few-shot learning and out-of-distribution generalization capabilities in real-world tasks.
- In terms of ReinboT algorithm design, we consider that accurate estimation of the value function in RL algorithms has always been a thorny problem, especially in the Transformer ...

## Abstract Cue
- An important reason that limits the performance of VLA models is that the quality of training data sources is usually uneven, even if they come from successful demonstrations (Hejna et al.).
