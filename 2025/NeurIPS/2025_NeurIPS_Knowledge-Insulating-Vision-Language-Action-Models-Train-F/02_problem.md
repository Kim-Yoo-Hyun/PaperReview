# Problem

- Year/Venue: 2025 / NeurIPS Spotlight
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Robotics
- Paper link: ./2025/NeurIPS/2025_NeurIPS_Knowledge-Insulating-Vision-Language-Action-Models-Train-F/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- To address this challenge, we propose a training recipe that addresses these issues, which we refer to as knowledge insulation.
- LLMs can be prompted to solve all sorts of tasks, from writing poems and code to solving competition-level math problems, and can further be adapted to solve visual ...
- However, adapting LLMs and VLMs to real-world control requires addressing a number of new challenges.

## 해결하려는 문제
- In this paper, we study this question in the context of VLAs that include a continuous diffusion or flow matching action expert, showing that naively including such experts ...
- While these modules improve real-time and control capabilities, it remains an open question whether they preserve or degrade the semantic knowledge contained in the pretrained VLM, and what ...
- We provide an extensive analysis of various design choices, their impact on performance and knowledge transfer, and propose a technique for insulating the VLM backbone during VLA training ...

## 선행 연구 / 배경 단서
- To address this challenge, we propose a training recipe that addresses these issues, which we refer to as knowledge insulation.
- As experiments show, having both action representations at training time is crucial. autoregressive decoding with large models, a challenge only exacerbated by ever larger models.
- Autoregressive decoding of discrete tokens is poorly suited to this kind of high-frequency continuous control, both because of the limited resolution of discretized actions and because of the ...
