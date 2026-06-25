# RegionPLC: Regional Point-Language Contrastive Learning for Open-World 3D Scene Understanding

- Year/Venue: 2024 / CVPR
- Category: Open-Vocabulary 3D Mapping
- Tags: point-language, open-world, semantic
- Authors: Jihan Yang, Runyu Ding, Weipeng Deng, Zhe Wang, Xiaojuan Qi ; Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2024, pp. 19823-19832
- Paper: https://openaccess.thecvf.com/content/CVPR2024/html/Yang_RegionPLC_Regional_Point-Language_Contrastive_Learning_for_Open-World_3D_Scene_Understanding_CVPR_2024_paper.html
- PDF status: downloaded
- GitHub/Project: not identified from primary page

## Problem
3D semantic perception은 라벨 공간이 제한적이고 long-tail 객체/속성/affordance를 다루기 어려워 foundation model alignment가 필요하다.

## Core Idea
핵심은 foundation model feature와 3D 구조를 정렬하여 downstream task별 supervision 의존도를 줄이는 것이다.

## Paper-Specific Cues
- Topic cue: We propose a lightweight and scalable Regional Point-Language Contrastive learning framework namely RegionPLC for open-world 3D scene understanding aiming to identify and recognize open-set ...
- Method cue: We propose a lightweight and scalable Regional Point-Language Contrastive learning framework namely RegionPLC for open-world 3D scene understanding aiming to identify and recognize open-set ...
- Result cue: We carry out extensive experiments on ScanNet ScanNet200 and nuScenes datasets and our model outperforms prior 3D open-world scene understanding approaches by an average ...

## Input / Output
Input/Output follows the paper task formulation; see PDF for the exact interface.

## Main Claims
- 논문은 `open-vocabulary 3D semantic understanding`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
2D foundation model에서 온 semantic feature가 3D geometry와 완벽히 정렬되지 않으며, long-tail 관계/속성 평가는 여전히 어렵다.

## Contribution
- open-vocabulary 3D semantic understanding 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: point-language, open-world, semantic.
- 초록에서 확인되는 주요 cue: Regional, Point-Language, Contrastive, RegionPLC, Specifically, SFusion, Subsequently, ScanNet.
