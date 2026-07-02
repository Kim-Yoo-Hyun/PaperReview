# Lookahead Exploration with Neural Radiance Representation for Continuous Vision-Language Navigation

- Year/Venue: 2024 / CVPR
- Category: Navigation and Embodied AI
- Tags: Vision-Language Navigation, NeRF, Planning
- Paper link: ./2024/CVPR/2024_CVPR_Lookahead-Exploration-with-Neural-Radiance-Representation/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- To this end, some existing works predict RGB images for future environments, while this strategy suffers from image distortion and high computational cost.
- This phenomenon raises a challenge to accurately represent future environments with visual occlusions, leading to incorrect action decisions.

## Core Idea
- To address these issues, we propose the pre-trained hierarchical neural radiance representation model (HNR) to produce multi-level semantic features for future environments, which are more robust and efficient ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments on the VLN-CE datasets confirm the effectiveness of our method.
- For better navigation planning, the lookahead exploration strategy aims to effectively evaluate the agent’s next action by accurately anticipating the future environment of candidate locations.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Extensive experiments on the VLN-CE datasets confirm the effectiveness of our method.
- To address these issues, we propose the pre-trained hierarchical neural radiance representation model (HNR) to produce multi-level semantic features for future environments, which are more robust and efficient ...
- For better navigation planning, the lookahead exploration strategy aims to effectively evaluate the agent’s next action by accurately anticipating the future environment of candidate locations.

## Abstract Cue
- Vision-and-language navigation (VLN) enables the agent to navigate to a remote location following the natural language instruction in 3D environments.
