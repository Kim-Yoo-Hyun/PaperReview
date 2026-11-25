# PointWorld: Scaling 3D World Models for In-The-Wild Robotic Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / CVPR
- Authors: Wenlong Huang, Yu-Wei Chao, Arsalan Mousavian, Ming-Yu Liu, Dieter Fox, Kaichun Mo, Li Fei-Fei
- Category: World Models, Safety, and Recovery
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: 3D-point-flow, action-conditioned-dynamics, MPC
- Aliases: PointWorld
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Huang_PointWorld_Scaling_3D_World_Models_for_In-The-Wild_Robotic_Manipulation_CVPR_2026_paper.html
- Venue verification: https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_PointWorld_Scaling_3D_World_Models_for_In-The-Wild_Robotic_Manipulation_CVPR_2026_paper.pdf
- Code/Project: https://point-world.github.io/
- Code: https://github.com/NVlabs/PointWorld
- Source audit: 2026-10-19: 공식 paper abstract 및 저자 project/code README 확인; abstract 기반 — 본문 수동 확인 필요. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

PointWorld는 RGB-D 관측과 후보 행동으로부터 장면의 각 픽셀이 3D 공간에서 어디로 움직일지 예측한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_PointWorld_Scaling_3D_World_Models_for_In-The-Wild_Robotic_Manipulation_CVPR_2026_paper.pdf#page=1)

## Core Idea and Contribution

- 로봇 동작도 3차원 점들의 변위로 표현해 서로 다른 로봇의 행동과 장면 변화를 같은 좌표에서 학습한다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_PointWorld_Scaling_3D_World_Models_for_In-The-Wild_Robotic_Manipulation_CVPR_2026_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_PointWorld_Scaling_3D_World_Models_for_In-The-Wild_Robotic_Manipulation_CVPR_2026_paper.pdf#page=4)
- 한 체크포인트의 예측을 모델 예측 제어에 연결해 실제 Franka에서 밀기, 변형·관절 물체 조작, 도구 사용을 평가했다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_PointWorld_Scaling_3D_World_Models_for_In-The-Wild_Robotic_Manipulation_CVPR_2026_paper.pdf#page=1) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_PointWorld_Scaling_3D_World_Models_for_In-The-Wild_Robotic_Manipulation_CVPR_2026_paper.pdf#page=8)

## Observation–State–Action Interface

RGB-D capture + robot action의 point-flow 표현 → scene 3D point flow → MPC action selection.

## Evaluation Scope and Claim Boundary

CVF abstract/저자 project는 real/sim training data와 Franka의 pushing·deformable/articulated manipulation·tool use 평가를 설명한다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_PointWorld_Scaling_3D_World_Models_for_In-The-Wild_Robotic_Manipulation_CVPR_2026_paper.pdf) · [저자 project/code](https://point-world.github.io/). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

Current trend / action-relevant 3D. State와 action을 3D point flow로 표현하고 예측을 manipulation MPC에 연결한다. DP3/3D-VLA 이후 explicit geometry와 world model을 비교할 직접적인 연결이다. 본문 평가의 보장 범위와 calibration 의존성은 추가 확인 대상이다.

## Verification Boundary

RGB-D calibration, point-flow action 변환, partial observability와 MPC cost 정의을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 원문과 공개 자료

- 코드 — 행동 조건부 3D 점 흐름 모델 평가 · eval.py [배포 파일](https://raw.githubusercontent.com/NVlabs/PointWorld/05484826dfef74cbe278a3974179a5a16705d35d/eval.py)
- 가중치 — DROID와 BEHAVIOR로 학습한 PointWorld · large-droid+behavior/model-best.pt [배포 파일](https://huggingface.co/nvidia/PointWorld_models/blob/b9e2e19a4f2bd65922e1f6d70aa953fe70aa9dba/large-droid%2Bbehavior/model-best.pt)
- 데이터 — DROID에서 얻은 3D 주석 · droid/flows-fs-optimized/shard-000000/package.tar.zst.part-0000 [배포 파일](https://huggingface.co/datasets/nvidia/PointWorld-DROID/blob/dd9aaeec94bb14e27ab6b16b6e4aa0dbcf3ef56f/droid/flows-fs-optimized/shard-000000/package.tar.zst.part-0000)
