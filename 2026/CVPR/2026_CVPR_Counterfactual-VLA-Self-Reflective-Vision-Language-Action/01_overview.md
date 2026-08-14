# Counterfactual VLA: Self-Reflective Vision-Language-Action Model with Adaptive Reasoning

- Year/Venue: 2026 / CVPR
- Category: World Models, Safety, and Recovery
- Tags: Robotics, VLA, self-reflection, failure recovery, test-time reasoning
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://openaccess.thecvf.com/content/CVPR2026/html/Peng_Counterfactual_VLA_Self-Reflective_Vision-Language-Action_Model_with_Adaptive_Reasoning_CVPR_2026_paper.html
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- 0.16 Think Rate Recent reasoning-augmented Vision-Language-Action (VLA) models have improved the interpretability of end-toend autonomous driving by generating intermediate reasoning traces.
- Yet these models primarily describe what they perceive and intend to do, rarely questioning whether their planned actions are safe or appropriate.
- This work introduces Counterfactual VLA (CF-VLA), a self-reflective VLA framework that enables the model to reason about and revise its planned actions before execution.

## Core Idea
- To efficiently obtain such self-reflective capabilities, we propose a rollout–filter–label pipeline that mines high-value scenes from a base (noncounterfactual) VLA’s rollouts and labels counterfactual reasoning traces for subsequent ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experiments on large-scale driving datasets show that CF-VLA improves trajectory accuracy by up to 17.6%, enhances safety metrics by 20.5%, and exhibits adaptive thinking: it only enables counterfactual ...
- The model engages in reasoning more frequently and achieves mor
- Trajectory error before counterfactual training Task Improvement Trajectory error after counterfactual training Think Rate 0.8 0.12 0.6 0.08 0.4 0.04 0.2 ) s g RU urve win ario ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- To efficiently obtain such self-reflective capabilities, we propose a rollout–filter–label pipeline that mines high-value scenes from a base (noncounterfactual) VLA’s rollouts and labels counterfactual reasoning traces for subsequent ...
- Experiments on large-scale driving datasets show that CF-VLA improves trajectory accuracy by up to 17.6%, enhances safety metrics by 20.5%, and exhibits adaptive thinking: it only enables counterfactual ...
- Trajectory error before counterfactual training Task Improvement Trajectory error after counterfactual training Think Rate 0.8 0.12 0.6 0.08 0.4 0.04 0.2 ) s g RU urve win ario ...

## Abstract Cue
- 0.16 Think Rate Recent reasoning-augmented Vision-Language-Action (VLA) models have improved the interpretability of end-toend autonomous driving by generating intermediate reasoning traces.
