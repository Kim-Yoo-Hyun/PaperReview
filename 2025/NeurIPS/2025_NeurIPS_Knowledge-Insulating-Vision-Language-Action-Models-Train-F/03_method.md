# Method

- Year/Venue: 2025 / NeurIPS Spotlight
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Robotics
- Paper link: ./2025/NeurIPS/2025_NeurIPS_Knowledge-Insulating-Vision-Language-Action-Models-Train-F/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To address this challenge, we propose a training recipe that addresses these issues, which we refer to as knowledge insulation.
- The success of large language models (LLMs) can be attributed to the availability of large-scale datasets combined with powerful model architectures such as transformers that are trained with ...
- In this work, we observe that prior approaches for finetuning VLMs with continuous outputs can, perhaps unsurprisingly, lead to significantly worse training dynamics, as they rely on gradients ...

## 원리적 동기
- To address this challenge, we propose a training recipe that addresses these issues, which we refer to as knowledge insulation.
- LLMs can be prompted to solve all sorts of tasks, from writing poems and code to solving competition-level math problems, and can further be adapted to solve visual ...
- To address this challenge, we propose a training recipe that addresses these issues, which we refer to as knowledge insulation.

## 핵심 방법론
- To address this challenge, we propose a training recipe that addresses these issues, which we refer to as knowledge insulation.
- The success of large language models (LLMs) can be attributed to the availability of large-scale datasets combined with powerful model architectures such as transformers that are trained with ...
- In this work, we observe that prior approaches for finetuning VLMs with continuous outputs can, perhaps unsurprisingly, lead to significantly worse training dynamics, as they rely on gradients ...
- Autoregressive decoding of discrete tokens is poorly suited to this kind of high-frequency continuous control, both because of the limited resolution of discretized actions and because of the ...
- Our experimental evaluation provides an extensive analysis of the various modeling choices in continuous-action VLAs, building on the π0 model architecture .
