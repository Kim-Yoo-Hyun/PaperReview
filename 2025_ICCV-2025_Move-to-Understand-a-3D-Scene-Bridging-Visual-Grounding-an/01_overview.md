# Move to Understand a 3D Scene: Bridging Visual Grounding and Exploration for Efficient and Versatile Embodied Navigation

- Year/Venue: 2025 / ICCV 2025
- Category: Navigation and Embodied AI
- Tags: Navigation, grounding, exploration
- Authors: Ziyu Zhu, Xilin Wang, Yixuan Li, Zhuofan Zhang, Xiaojian Ma, Yixin Chen, Baoxiong Jia, Wei Liang, Qian Yu, Zhidong Deng, Siyuan Huang, Qing Li ; Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV), 2025, pp. 8120-8132
- Paper: https://openaccess.thecvf.com/content/ICCV2025/html/Zhu_Move_to_Understand_a_3D_Scene_Bridging_Visual_Grounding_and_ICCV_2025_paper.html
- PDF status: downloaded
- GitHub/Project: not identified from primary page

## Problem
실내/실외 이동 에이전트는 언어 목표와 3D 공간 구조를 연결해야 하며, partial observation과 탐색-활용 균형 때문에 단순 2D 인식만으로는 안정적이지 않다.

## Core Idea
핵심은 metric/semantic map, 3D scene graph, neural field, 또는 VLM reasoning을 이용해 언어 목표를 이동 가능한 공간 의사결정으로 바꾸는 것이다.

## Paper-Specific Cues
- Topic cue: Embodied scene understanding requires not only comprehending visual-spatial information that has been observed but also determining where to explore next in the 3D physical ...
- Method cue: To address this limitation, we introduce Move to Understand (MTU3D), a unified framework that integrates active perception with 3D vision-language learning, enabling embodied agents ...
- Result cue: This is achieved by three key innovations 1) Online query-based representation learning, enabling direct spatial memory construction from RGB-D frames, eliminating the need for ...

## Input / Output
Input: language/navigation goal plus egocentric observations or 3D maps. Output: waypoint, action, route, or grounded target decision.

## Main Claims
- 논문은 `embodied navigation and spatial planning`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
실제 로봇 배치에서는 센서 calibration, latency, safety, embodiment mismatch, 실패 복구가 추가 변수다.

## Contribution
- embodied navigation and spatial planning 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: Navigation, grounding, exploration.
- 초록에서 확인되는 주요 cue: Embodied, Existing, Vision-Language, Move, Understand, MTU3D, This, Online.
