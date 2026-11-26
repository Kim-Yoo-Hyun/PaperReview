# FoundationPose: Unified 6D Pose Estimation and Tracking of Novel Objects

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2024 / CVPR
- Authors: Bowen Wen, Wei Yang, Jan Kautz, Stan Birchfield
- Category: Robotics-Enabling 3D Perception
- Primary track: Robotics-enabling 3D perception
- Tier: NEXT
- Tags: 6D pose, tracking, RGB-D, novel objects
- Aliases: FoundationPose
- Official paper: https://openaccess.thecvf.com/content/CVPR2024/html/Wen_FoundationPose_Unified_6D_Pose_Estimation_and_Tracking_of_Novel_Objects_CVPR_2024_paper.html
- Venue verification: https://openaccess.thecvf.com/content/CVPR2024/html/Wen_FoundationPose_Unified_6D_Pose_Estimation_and_Tracking_of_Novel_Objects_CVPR_2024_paper.html
- Code/Project: https://nvlabs.github.io/FoundationPose/
- Code: https://github.com/NVlabs/FoundationPose
- 방법·평가 확인 (2026-11-25): [원문 4, 5, 6, 7, 8쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Wen_FoundationPose_Unified_6D_Pose_Estimation_and_Tracking_of_Novel_Objects_CVPR_2024_paper.pdf#page=4) · [다축 분류와 공개 범위](../../../work/sources/batches/core_next_10.yaml)
- Source audit: 2026-11-18: 공식 초록·bibliographic record와 연결된 저자 자료 확인. Abstract 기반 등록이며 본문 전체·실험 재현은 미확인. 직접 HTML 접근 제한은 공식 사이트의 검색 색인 abstract/BibTeX 및 저자 abstract/project 자료로 교차 확인; HTML 전면 열람으로 기록하지 않음. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

FoundationPose는 새 물체의 CAD 모델이나 소수 참조 영상을 이용해 별도 미세조정 없이 6차원 자세를 추정하고 추적한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Wen_FoundationPose_Unified_6D_Pose_Estimation_and_Tracking_of_Novel_Objects_CVPR_2024_paper.pdf#page=1)

## Core Idea and Contribution

- CAD가 없는 경우 참조 영상으로 신경 암시적 물체 표현을 구성한 뒤, 두 설정에서 같은 모듈로 자세 후보를 보정하고 순위를 매긴다. [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Wen_FoundationPose_Unified_6D_Pose_Estimation_and_Tracking_of_Novel_Objects_CVPR_2024_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Wen_FoundationPose_Unified_6D_Pose_Estimation_and_Tracking_of_Novel_Objects_CVPR_2024_paper.pdf#page=5)
- 공개 데이터셋에서 CAD 사용 여부에 따른 초기 자세 추정과 비디오에서의 후속 추적을 따로 평가해 전용 기준선들과 비교했다. [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Wen_FoundationPose_Unified_6D_Pose_Estimation_and_Tracking_of_Novel_Objects_CVPR_2024_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Wen_FoundationPose_Unified_6D_Pose_Estimation_and_Tracking_of_Novel_Objects_CVPR_2024_paper.pdf#page=8)

## Observation–State–Action Interface

RGB-D와 CAD 또는 reference 관측에서 물체 6D pose·tracking 출력을 얻는다. 행동 정책 자체는 아니다.

## Evaluation Scope and Claim Boundary

공식 project는 미지 물체 pose estimation/tracking의 일반화를 제시한다. 이번 등록에서는 세부 trial·로봇 성공률을 확정하지 않는다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2024/html/Wen_FoundationPose_Unified_6D_Pose_Estimation_and_Tracking_of_Novel_Objects_CVPR_2024_paper.html) · [저자 project/code](https://nvlabs.github.io/FoundationPose/) · [공식 code](https://github.com/NVlabs/FoundationPose). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

현재 능동 관측 후보의 pose baseline이며 CAD/reference·score·좌표 가정을 판단하는 직접 NEXT다.

## Verification Boundary

Model-free reference 요구·대칭 처리·ranking score와 보정 확률의 차이을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 공개 자료의 확인 범위

- FoundationPose의 물체 자세 등록·추적 추론 · estimater.py [배포 파일](https://raw.githubusercontent.com/NVlabs/FoundationPose/a1b694b83e633c2cb6115b9063d940a687759392/estimater.py)
- FoundationPose의 자세 가설 점수 또는 보정 네트워크 체크포인트 · model_best.pth [배포 파일](https://drive.google.com/file/d/1E9FPB5WFIBMLrOJqZLpoVOK4Mjzrrxhv/view)
- FoundationPose 학습용 GSO 렌더 배포 자료 · 30602556.zip [배포 파일](https://drive.google.com/file/d/1_ctJIyrlsco7e6l975kgqFN2M9g-EIPi/view)
