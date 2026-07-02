# CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models

- Year/Venue: 2025 / CVPR
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Chain-of-Thought, Robotics
- Paper link: ./2025/CVPR/2025_CVPR_CoT-VLA-Visual-Chain-of-Thought-Reasoning-for-Vision-Langu/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- As a result, existing VLAs lack temporal planning or reasoning capabilities.
- While this paradigm effectively utilizes largescale data from both robotic and non-robotic sources, current VLAs primarily focus on direct input–output mappings, lacking the intermediate reasoning steps crucial for ...

## Core Idea
- We introduce CoT-VLA, a state-ofthe-art 7B VLA that can understand and generate visual and action tokens.
- In this paper, we introduce a method that incorporates explicit visual chain-ofthought (CoT) reasoning into vision-language-action models (VLAs) by predicting future image frames autoregressively as visual goals before ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Our experimental results demonstrate that CoT-VLA achieves strong performance, outperforming the state-of-the-art VLA model by 17% in real-world manipulation tasks and 6% in simulation benchmarks.
- In this paper, we introduce a method that incorporates explicit visual chain-ofthought (CoT) reasoning into vision-language-action models (VLAs) by predicting future image frames autoregressively as visual goals before ...
- CoT-VLA first generates a subgoal image as an intermediate reasoning step, and then generate a short action sequence to achieve the subgoal.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Our experimental results demonstrate that CoT-VLA achieves strong performance, outperforming the state-of-the-art VLA model by 17% in real-world manipulation tasks and 6% in simulation benchmarks.
- In this paper, we introduce a method that incorporates explicit visual chain-ofthought (CoT) reasoning into vision-language-action models (VLAs) by predicting future image frames autoregressively as visual goals before ...
- Introduction Recent advances in robot learning have demonstrated impressive progress in training policies that can act across diverse tasks and environments .

## Abstract Cue
- Vision-language-action models (VLAs) have shown potential in leveraging pretrained vision-language models and diverse robot demonstrations for learning generalizable sensorimotor control.
