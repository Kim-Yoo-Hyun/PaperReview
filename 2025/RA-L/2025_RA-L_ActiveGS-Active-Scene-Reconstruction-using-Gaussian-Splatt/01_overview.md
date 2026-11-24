# ActiveGS: Active Scene Reconstruction using Gaussian Splatting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2412.17769.
> PDF retrieval source: https://arxiv.org/pdf/2412.17769. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RA-L
- Authors: Liren Jin, Xingguang Zhong, Yue Pan, Jens Behley, Cyrill Stachniss, Marija Popović
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting
- Official paper: https://arxiv.org/abs/2412.17769
- Full-text retrieval: https://arxiv.org/pdf/2412.17769
- Code/Project: https://github.com/dmar-bonn/active-gs
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 원문 해당 쪽과 대조했다. [본문](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=10938898)

## Why This Paper Is Here

ActiveGS는 RGB-D 카메라가 미탐색 공간과 충분히 복원되지 않은 표면을 찾아 다음 관측 위치를 고르도록 가우시안 지도와 복셀 지도를 결합한다. [PDF 1쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=10938898#page=1) · [PDF 3쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=10938898#page=3)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Robotics applications often rely on scene reconstructions to enable downstream tasks.
- **p. 1 / Abstract - extractive body cue:** In this work, we tackle the challenge of actively building an accurate map of an unknown scene using an RGB-D camera on a mobile platform.
- **p. 1 / Abstract - extractive body cue:** We propose a hybrid map representation that combines a Gaussian splatting map with a coarse voxel map, leveraging the strengths of both representations: the high-fidelity ...
- **p. 1 / Abstract - extractive body cue:** At the core of our framework is an effective confidence modelling technique for the Gaussian splatting map to identify under-reconstructed areas, while utilising spatial information ...
- **p. 1 / Abstract - extractive body cue:** By actively collecting scene information in under-reconstructed and unexplored areas for map updates, our approach achieves superior Gaussian splatting reconstruction results compared to state-of-the-art approaches.
- **p. 2 / A CTIVE exploration and reconstruction of unknown - extractive body cue:** However, this is difficult without ground truth information at novel viewpoints.
- **p. 2 / A CTIVE exploration and reconstruction of unknown - extractive body cue:** Incorporating GS into an active scene reconstruction pipeline presents significant challenges.

## Core Idea

- **p. 3 / III. OUR APPROACH - extractive body cue:** We introduce ActiveGS, a novel framework for active scene reconstruction using GS for autonomous robotic tasks.
- **p. 3 / III. OUR APPROACH - extractive body cue:** An overview of our framework is shown in Fig.
- **p. 4 / III. OUR APPROACH - extractive body cue:** A candidate viewpoint pc i ∈R5 is defined by its 3D position, yaw, and pitch angles in our framework.
- **p. 4 / III. OUR APPROACH - extractive body cue:** To address this, we introduce additional candidate viewpoints based on regions of interest (ROI) defined in the voxel map.
- **p. 1 / Body text (section not recovered) - extractive body cue:** By integrating confidence modelling into the Gaussian splatting pipeline, our approach enables targeted view planning to build a high-fidelity Gaussian splatting map.
- **p. 4 / III. OUR APPROACH - extractive body cue:** The normal loss Ln = Dcos(N, eN) + TV (N) consists of the cosine distance Dcos between the rendered normal map and the normal map ...
- **p. 2 / A CTIVE exploration and reconstruction of unknown - extractive body cue:** To tackle the first challenge, we propose a simple yet effective confidence modelling technique for Gaussian primitives based on viewpoint distribution, enabling view planning for ...
- **p. 3 / III. OUR APPROACH - extractive body cue:** To actively guide view planning to reconstruct the scene in a targeted manner, we propose using our confidence modelling technique in the GS map and ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Given posed RGB-D measurements as input, we update a coarse voxel map to model the spatial occupancy and incrementally train a GS map for high-fidelity scene reconstruction. | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (III. OUR APPROACH), p. 3 (III. OUR APPROACH) |
| State/latent | Given, posed, RGB-D, measurements, input, update, coarse, voxel, model, spatial, occupancy, incrementally | geometry, map, object/relationship state | p. 3 (III. OUR APPROACH), p. 3 (III. OUR APPROACH), p. 4 (III. OUR APPROACH) |
| Output/action | Our GS map is based on Gaussian surfel [4], a state-ofthe-art 2D GS representation. | point map, pose, scene graph, affordance 또는 query result | p. 3 (III. OUR APPROACH), p. 4 (III. OUR APPROACH), p. 4 (III. OUR APPROACH) |
| Objective/outcome | While these approaches demonstrate promising results, the rather costly volumetric rendering procedure during online incremental mapping poses limitations for NeRF-based active scene reconstruction. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 2 (A CTIVE exploration and reconstruction of unknown), p. 3 (III. OUR APPROACH), p. 4 (III. OUR APPROACH) |

## Main Claims and Actual Contribution

- 가우시안별 관측 신뢰도로 표면을 다시 볼 가치를 추정하고, 복셀 지도로 알려지지 않은 공간과 충돌 없는 이동 경로를 계산한다. [PDF 3쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=10938898#page=3) · [PDF 4쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=10938898#page=4) · [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=10938898#page=5)
- 시뮬레이션에서 탐색에 따른 지도 품질을 비교하고 실내 무인기의 RGB-D·외부 자세 측정값으로 온라인 지도 갱신과 시점 계획을 시연했다. [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=10938898#page=5) · [PDF 6쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=10938898#page=6) · [PDF 7쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=10938898#page=7)

## Evaluation Scope

실내 무인기 시연은 OptiTrack으로 자세를 측정했다. 데스크톱에서 RGB-D와 자세를 받아 지도를 갱신하고 충돌 없는 웨이포인트를 기체로 전송했다. [PDF 7쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=10938898#page=7)

## Explicit Limitations and Failure Boundary

- **p. 7 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** Unlike simulation experiments, we do not account for the pitch angle of viewpoints in this experiment due to control limitations.
- **p. 7 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** Given the limited on-board resources, we run ActiveGS on our desktop PC, where it receives RGB-D and pose data from the UAV for map updates ...
- **p. 5 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** The camera has a depth sensing range of [0.1, 5.0] m and Gaussian noise in the depth measurements with linearly increased standard deviation σ = ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (A CTIVE exploration and reconstruction of unknown), p. 1 (Abstract), p. 1 (A CTIVE exploration and reconstruction of unknown), p. 3 (III. OUR APPROACH), p. 4 (III. OUR APPROACH)이다.
