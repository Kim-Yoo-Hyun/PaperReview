# FoundationPose: Unified 6D Pose Estimation and Tracking of Novel Objects

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
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
- Source audit: 2026-11-18: 공식 초록·bibliographic record와 연결된 저자 자료 확인. Abstract 기반 등록이며 본문 전체·실험 재현은 미확인. 직접 HTML 접근 제한은 공식 사이트의 검색 색인 abstract/BibTeX 및 저자 abstract/project 자료로 교차 확인; HTML 전면 열람으로 기록하지 않음.

## Problem and Importance

미지 물체의 pose 추정과 추적에서 완전 CAD와 소수 reference 관측의 서로 다른 전제를 통합한다.

## Core Idea and Contribution

Neural implicit 표현으로 두 입력 조건을 연결해 동일 pose 모듈을 재사용한다. 새 물체별 fine-tuning 없이 적용하는 설정이다.

## Observation–State–Action Interface

RGB-D와 CAD 또는 reference 관측에서 물체 6D pose·tracking 출력을 얻는다. 행동 정책 자체는 아니다.

## Evaluation Scope and Claim Boundary

공식 project는 미지 물체 pose estimation/tracking의 일반화를 제시한다. 이번 등록에서는 세부 trial·로봇 성공률을 확정하지 않는다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2024/html/Wen_FoundationPose_Unified_6D_Pose_Estimation_and_Tracking_of_Novel_Objects_CVPR_2024_paper.html) · [저자 project/code](https://nvlabs.github.io/FoundationPose/) · [공식 code](https://github.com/NVlabs/FoundationPose). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

현재 능동 관측 후보의 pose baseline이며 CAD/reference·score·좌표 가정을 판단하는 직접 NEXT다.

## Verification Boundary

Model-free reference 요구·대칭 처리·ranking score와 보정 확률의 차이을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
