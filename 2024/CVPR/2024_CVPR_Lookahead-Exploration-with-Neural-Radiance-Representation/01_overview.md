# Lookahead Exploration with Neural Radiance Representation for Continuous Vision-Language Navigation

- Year/Venue: 2024 / CVPR
- Category: Navigation and Embodied AI
- Tags: Vision-Language Navigation, NeRF, Planning
- Authors: Zihan Wang, Xiangyang Li, Jiahao Yang, Yeqi Liu, Junjie Hu, Ming Jiang, Shuqiang Jiang ; Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2024, pp. 13753-13762
- Paper: https://openaccess.thecvf.com/content/CVPR2024/html/Wang_Lookahead_Exploration_with_Neural_Radiance_Representation_for_Continuous_Vision-Language_Navigation_CVPR_2024_paper.html
- PDF status: downloaded
- GitHub/Project: not identified from primary page

## Problem
NeRF/3DGS는 장면을 잘 렌더링하지만 언어 질의, open-vocabulary semantics, instance-level grounding을 직접 지원하지 않는 경우가 많다.

## Core Idea
핵심은 radiance field의 공간 좌표/뷰 의존 표현에 CLIP/VLM feature를 결합해 3D 위치에서 언어적 의미를 조회할 수 있게 하는 것이다.

## Paper-Specific Cues
- Topic cue: Vision-and-language navigation (VLN) enables the agent to navigate to a remote location following the natural language instruction in 3D environments.
- Method cue: To address these issues we propose the pre-trained hierarchical neural radiance representation model (HNR) to produce multi-level semantic features for future environments which are ...
- Result cue: 초록에서 result claim 문장을 자동 추출하지 못함.

## Input / Output
Input: language/navigation goal plus egocentric observations or 3D maps. Output: waypoint, action, route, or grounded target decision.

## Main Claims
- 논문은 `language-aware neural radiance field representation`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
3DGS/NeRF 기반 방법은 scene reconstruction 품질, 카메라 포즈, memory/runtime, dynamic scene 처리에 민감하다.

## Contribution
- language-aware neural radiance field representation 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: Vision-Language Navigation, NeRF, Planning.
- 초록에서 확인되는 주요 cue: Vision-and-language, VLN, For, RGB, HNR, Furthermore, Extensive, VLN-CE.
