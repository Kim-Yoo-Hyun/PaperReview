# OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction

- Year/Venue: 2026 / ICRA
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, humanoid, loco-manipulation, motion retargeting
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://omniretarget.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- However, existing retargeting pipelines often struggle with the significant embodiment gap between humans and robots, producing physically implausible artifacts like foot-skating and penetration.

## Core Idea
- RL T RAINING WITH M INIMAL F ORMULATION Having established our method for generating high-quality kinematic references, we use RL to bridge the gap to dynamics by training ...
- To showcase the full capabilities of our framework, we present a long-horizon, dynamic sequence inspired by the Boston Dynamics Atlas tool-use demo .

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We comprehensively evaluate O MNI R ETARGET by retargeting motions from OMOMO , LAFAN1 , and our in-house MoCap datasets, generating over 8-hour trajectories that achieve better kinematic ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We comprehensively evaluate O MNI R ETARGET by retargeting motions from OMOMO , LAFAN1 , and our in-house MoCap datasets, generating over 8-hour trajectories that achieve better kinematic ...
- To address this, we introduce O MNI R ETARGET, an interactionpreserving data generation engine based on an interaction mesh that explicitly models and preserves the crucial spatial and ...
- However, existing retargeting pipelines often struggle with the significant embodiment gap between humans and robots, producing physically implausible artifacts like foot-skating and penetration.

## Abstract Cue
- — A dominant paradigm for teaching humanoid robots complex skills is to retarget human motions as kinematic references to train reinforcement learning (RL) policies.
