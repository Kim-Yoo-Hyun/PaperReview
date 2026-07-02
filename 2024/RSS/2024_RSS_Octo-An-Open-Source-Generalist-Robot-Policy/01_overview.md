# Octo: An Open-Source Generalist Robot Policy

- Year/Venue: 2024 / RSS
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Robotics, generalist policy, Imitation Learning
- Paper link: ./2024/RSS/2024_RSS_Octo-An-Open-Source-Generalist-Robot-Policy/paper.pdf
- Code/Project: https://octo-models.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Correspondence to {dibya.ghosh, homer_walke, pertsch, kvablack, oier.mees}@berkeley.edu experience from other robots and tasks offers a possible particular combination of these components into a powerful solution, exposing models to ...

## Core Idea
- As a first step, we introduce Octo, a large transformer-based policy trained on 800k trajectories from the Open X-Embodiment dataset, the largest robot manipulation dataset to date.
- We also perform detailed ablations of design decisions for the Octo model, from architecture to training data, to guide future research on building generalist robot models.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Correspondence to {dibya.ghosh, homer_walke, pertsch, kvablack, oier.mees}@berkeley.edu experience from other robots and tasks offers a possible particular combination of these components into a powerful solution, exposing models to ...
- In experiments across 9 robotic platforms, we demonstrate that Octo serves as a versatile policy initialization that can be effectively finetuned to new observation and action spaces.
- We also perform detailed ablations of design decisions for the Octo model, from architecture to training data, to guide future research on building generalist robot models.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Correspondence to {dibya.ghosh, homer_walke, pertsch, kvablack, oier.mees}@berkeley.edu experience from other robots and tasks offers a possible particular combination of these components into a powerful solution, exposing models to ...
- We also perform detailed ablations of design decisions for the Octo model, from architecture to training data, to guide future research on building generalist robot models.
- As a first step, we introduce Octo, a large transformer-based policy trained on 800k trajectories from the Open X-Embodiment dataset, the largest robot manipulation dataset to date.

## Abstract Cue
- —Large policies pretrained on diverse robot datasets have the potential to transform robotic learning: instead of training new policies from scratch, such generalist robot policies may be finetuned with only a little in-domain data, yet generalize broadly.
