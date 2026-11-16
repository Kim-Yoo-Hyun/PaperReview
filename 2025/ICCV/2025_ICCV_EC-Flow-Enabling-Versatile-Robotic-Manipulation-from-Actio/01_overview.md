# EC-Flow: Enabling Versatile Robotic Manipulation from Action-Unlabeled Videos via Embodiment-Centric Flow

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / ICCV
- Category: Manipulation, Contact, and Dexterity
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: embodiment, flow, video-pretraining, manipulation
- Aliases: EC-Flow
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Chen_EC-Flow_Enabling_Versatile_Robotic_Manipulation_from_Action-Unlabeled_Videos_via_Embodiment-Centric_ICCV_2025_paper.html
- Venue verification: https://openaccess.thecvf.com/content/ICCV2025/html/Chen_EC-Flow_Enabling_Versatile_Robotic_Manipulation_from_Action-Unlabeled_Videos_via_Embodiment-Centric_ICCV_2025_paper.html
- Code/Project: https://ec-flow1.github.io/
- Code: https://github.com/YixiangChen515/EC-Flow
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지.

## Problem and Importance

Object-centric flow만으로는 가려짐·변형 물체·변위 없는 조작을 표현하기 어렵다.

## Core Idea and Contribution

Embodiment-centric flow와 goal alignment를 학습하고 URDF 제약으로 행동에 변환한다.

## Observation–State–Action Interface

영상·지시 → embodiment flow → kinematic 제약 기반 robot action.

## Evaluation Scope and Claim Boundary

Meta-World와 실제 가림·변형·비변위 조작을 평가한다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/ICCV2025/html/Chen_EC-Flow_Enabling_Versatile_Robotic_Manipulation_from_Action-Unlabeled_Videos_via_Embodiment-Centric_ICCV_2025_paper.html) · [저자 project/code](https://ec-flow1.github.io/) · [공식 code](https://github.com/YixiangChen515/EC-Flow). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

행동 표현을 통합하는 연구에서 object motion과 robot motion의 차이를 보존할 대안이다.

## Verification Boundary

URDF만으로 해결되는 변환 범위, calibration, 동역학·접촉 정보 의존성을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
