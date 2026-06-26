# SSRFlow: Semantic-aware Fusion with Spatial Temporal Re-embedding for Real-world Scene Flow

- Year/Venue: 2025 / 3DV
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: sensor fusion, LiDAR, semantic, alignment, 3D Vision
- Authors: Zhiyang Lu, Qinghan Chen, Zhimin Yuan, Chenglu Wen, Ming Cheng, Cheng Wang
- Paper: https://3dvconf.github.io/2025/accepted-papers/
- PDF status: downloaded
- GitHub/Project: not identified

## Problem
3D semantic perception은 라벨 공간이 제한적이고 long-tail 객체/속성/affordance를 다루기 어려워 foundation model alignment가 필요하다.

## Core Idea
핵심은 foundation model feature와 3D 구조를 정렬하여 downstream task별 supervision 의존도를 줄이는 것이다.

## Paper-Specific Cues
- Topic cue: Scene flow, which provides the 3D motion field of the first frame from two consecutive point clouds, is vital for dynamic scene perception.
- Method cue: To address this issue, we propose a novel approach called Dual Cross Attentive (DCA) for the latent fusion and alignment between two frames based ...
- Result cue: Experiments demonstrate that our approach achieves state-of-the-art (SOTA) performance across various datasets, with particularly outstanding results in real-world LiDAR-scanned situations.

## Input / Output
Input/Output follows the paper task formulation; see PDF for the exact interface.

## Main Claims
- 논문은 `open-vocabulary 3D semantic understanding`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
2D foundation model에서 온 semantic feature가 3D geometry와 완벽히 정렬되지 않으며, long-tail 관계/속성 평가는 여전히 어렵다.

## Contribution
- open-vocabulary 3D semantic understanding 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: sensor fusion, LiDAR, semantic, alignment, 3D Vision.
- 초록에서 확인되는 주요 cue: Scene, However, Firstly, Dual, Cross, Attentive, DCA, This.
