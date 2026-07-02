# OpenVLA: An Open-Source Vision-Language-Action Model

- Year/Venue: 2024 / CoRL
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Robotics, Imitation Learning
- Paper link: ./2024/CoRL/2024_CoRL_OpenVLA-An-Open-Source-Vision-Language-Action-Model/paper.pdf
- Code/Project: https://github.com/openvla/openvla
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- While reproducing this scale of pretraining for robotics is still an open challenge — even the largest robot manipulation datasets only have 100K to 1M examples – this ...
- A key weakness of learned policies for robotic manipulation is their inability to generalize beyond their training data: while existing policies trained for individual skills or language instructions ...
- Yet beyond robotics, existing foundation models for vision and language such as CLIP , SigLIP , and Llama 2 are capable of these types of generalization and more, ...

## Core Idea
- Yet, there are two key reasons preventing the widespread use of existing VLAs: 1) current models are closed, with limited visibility into model architecture, training procedures, and data ...
- To this end, we introduce OpenVLA, a 7B-parameter open-source VLA that establishes a new state of the art for generalist robot manipulation policies.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- As a product of the added data diversity and new model components, OpenVLA demonstrates strong results for generalist manipulation, outperforming closed models such as RT-2-X (55B) by 16.5% ...
- OpenVLA achieves highest overall performance and even outperforms closed-source model RT-2-X in all categories except for semantic generalization.
- Concretely, we aim to answer the following questions: (1) How does OpenVLA compare to prior generalist robot policies, when evaluating on multiple robots and various types of generalization? ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- As a product of the added data diversity and new model components, OpenVLA demonstrates strong results for generalist manipulation, outperforming closed models such as RT-2-X (55B) by 16.5% ...
- Addressing these challenges, we introduce OpenVLA, a 7B-parameter open-source VLA trained on a diverse collection of 970k real-world robot demonstrations.
- : Large policies pretrained on a combination of Internet-scale visionlanguage data and diverse robot demonstrations have the potential to change how we teach robots new skills: rather than ...

## Abstract Cue
- : Large policies pretrained on a combination of Internet-scale visionlanguage data and diverse robot demonstrations have the potential to change how we teach robots new skills: rather than training new behaviors from scratch, we can fine-tune such vision-language-action (VLA) models to obtain robust, generalizable policies ...
