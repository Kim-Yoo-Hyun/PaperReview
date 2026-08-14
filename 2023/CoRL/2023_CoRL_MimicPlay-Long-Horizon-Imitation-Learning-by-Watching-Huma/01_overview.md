# MimicPlay: Long-Horizon Imitation Learning by Watching Human Play

- Year/Venue: 2023 / CoRL
- Category: Robot Learning and Data
- Tags: Robotics, Imitation Learning, human video, cross-embodiment, hierarchical policy, long-horizon manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://mimic-play.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- Such latent plans provide rich 3D guidance (what to do and where to interact) at each time step, tackling the challenging long-horizon manipulation problem by converting it into ...
- Efficiently teaching robots to perform general-purpose manipulation tasks is a long-standing challenge.
- In this work, we argue that the data required for learning high-level plan and low-level control can come in different forms, and doing so could substantially reduce the ...

## Core Idea
- To scale imitation learning to long-horizon manipulation tasks, we present MIMICPLAY, a new imitation learning algorithm that leverages the complementary strengths of two data sources mentioned above: human ...
- Motivated by this, we introduce a hierarchical learning framework named MIMICPLAY that learns latent plans from human play data to guide low-level visuomotor control trained on a small ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- With systematic evaluations of 14 longhorizon manipulation tasks in the real world, we show that MIMICPLAY outperforms state-of-the-art imitation learning methods in task success rate, generalization ability, and ...
- Our method outperforms Ours (0% human) by more than 23% in long-horizon task settings over all trained tasks, as shown in both Tab.
- Ours (0% human) trained with our two-stage framework outperform prior end-to-end learning methods in the long-horizon task settings by more than 15%, as is shown in Tab.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- With systematic evaluations of 14 longhorizon manipulation tasks in the real world, we show that MIMICPLAY outperforms state-of-the-art imitation learning methods in task success rate, generalization ability, and ...
- Motivated by this, we introduce a hierarchical learning framework named MIMICPLAY that learns latent plans from human play data to guide low-level visuomotor control trained on a small ...

## Abstract Cue
- : Imitation learning from human demonstrations is a promising paradigm for teaching robots manipulation skills in the real world.
