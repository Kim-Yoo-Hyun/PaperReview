# Moto: Latent Motion Token as the Bridging Language for Learning Robot Manipulation from Videos

- Year/Venue: 2025 / ICCV
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Robotics
- Paper link: ./2025/ICCV/2025_ICCV_Moto-Latent-Motion-Token-as-the-Bridging-Language-for-Lear/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- The key challenge is to identify an effective representation for autoregressive pre-training that benefits robot manipulation tasks.
- This success offers new promise for robotics, which has long been constrained by the high cost of action-labeled data.
- This success opens new opportunity for robotics, which has been limited by the high costs of action-labeled data.

## Core Idea
- Inspired by the way humans learn new skills through observing dynamic environments, we propose that effective robotic learning should emphasize motion-related knowledge, which is closely tied to low-level ...
- To this end, we introduce Moto, which converts video content into latent Motion Token sequences by a Latent Motion Tokenizer, learning a bridging “language” of motion from videos ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments show that the fine-tuned Moto-GPT exhibits superior robustness and efficiency on robot manipulation benchmarks, underscoring its effectiveness in transferring knowledge from video data to downstream visual ...
- After pre-training, Moto-GPT demonstrates the promising ability to produce semantically interpretable motion tokens, predict plausible motion trajectories, and assess trajectory rationality through output likelihood.
- Recent developments in Large Language Models (LLMs) pre-trained on extensive corpora have shown significant success in various natural language processing (NLP) tasks with minimal fine-tuning.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Extensive experiments show that the fine-tuned Moto-GPT exhibits superior robustness and efficiency on robot manipulation benchmarks, underscoring its effectiveness in transferring knowledge from video data to downstream visual ...
- After pre-training, Moto-GPT demonstrates the promising ability to produce semantically interpretable motion tokens, predict plausible motion trajectories, and assess trajectory rationality through output likelihood.
- The key challenge is to identify an effective representation for autoregressive pre-training that benefits robot manipulation tasks.

## Abstract Cue
- Recent developments in Large Language Models (LLMs) pre-trained on extensive corpora have shown significant success in various natural language processing (NLP) tasks with minimal fine-tuning.
