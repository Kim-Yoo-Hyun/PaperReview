# EC-Flow: Enabling Versatile Robotic Manipulation from Action-Unlabeled Videos via Embodiment-Centric Flow

> Evidence maturity: `FULL_TEXT_CHECKED`. 요약과 기여를 아래 쪽수에서 확인했다.

- Year/Venue: 2025 / ICCV
- Authors: Yixiang Chen, Peiyan Li, Yan Huang, Jiabing Yang, Kehan Chen, Liang Wang
- Category: Manipulation, Contact, and Dexterity
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: embodiment, flow, video-pretraining, manipulation, diffusion model
- Aliases: EC-Flow
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Chen_EC-Flow_Enabling_Versatile_Robotic_Manipulation_from_Action-Unlabeled_Videos_via_Embodiment-Centric_ICCV_2025_paper.html
- Venue verification: https://openaccess.thecvf.com/content/ICCV2025/html/Chen_EC-Flow_Enabling_Versatile_Robotic_Manipulation_from_Action-Unlabeled_Videos_via_Embodiment-Centric_ICCV_2025_paper.html
- Code/Project: https://ec-flow1.github.io/
- Code: https://github.com/YixiangChen515/EC-Flow
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Chen_EC-Flow_Enabling_Versatile_Robotic_Manipulation_from_Action-Unlabeled_Videos_via_Embodiment-Centric_ICCV_2025_paper.pdf
- Source audit: 2026-11-24에 요약과 핵심 기여 두 개를 원문과 대조했다.

## Problem and Importance

EC-Flow는 저수준 행동 라벨이 없는 조작 영상에서 로봇 자체의 움직임을 예측하고, 로봇의 기구학으로 실행할 행동을 계산한다. [PDF 1쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Chen_EC-Flow_Enabling_Versatile_Robotic_Manipulation_from_Action-Unlabeled_Videos_via_Embodiment-Centric_ICCV_2025_paper.pdf#page=1) · [PDF 3쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Chen_EC-Flow_Enabling_Versatile_Robotic_Manipulation_from_Action-Unlabeled_Videos_via_Embodiment-Centric_ICCV_2025_paper.pdf#page=3)

## Core Idea and Contribution

- 언어 지시와 흐름을 목표 이미지 예측 및 움직임 일관성으로 정렬하고, URDF에 기술된 관절 제약을 이용해 흐름을 행동으로 변환한다. [PDF 3쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Chen_EC-Flow_Enabling_Versatile_Robotic_Manipulation_from_Action-Unlabeled_Videos_via_Embodiment-Centric_ICCV_2025_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Chen_EC-Flow_Enabling_Versatile_Robotic_Manipulation_from_Action-Unlabeled_Videos_via_Embodiment-Centric_ICCV_2025_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Chen_EC-Flow_Enabling_Versatile_Robotic_Manipulation_from_Action-Unlabeled_Videos_via_Embodiment-Centric_ICCV_2025_paper.pdf#page=5)
- Meta-World와 실물 조작에서 물체가 가려지거나 변형되는 과제, 물체 변위가 작은 과제를 물체 중심 흐름 방법과 비교했다. [PDF 6쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Chen_EC-Flow_Enabling_Versatile_Robotic_Manipulation_from_Action-Unlabeled_Videos_via_Embodiment-Centric_ICCV_2025_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Chen_EC-Flow_Enabling_Versatile_Robotic_Manipulation_from_Action-Unlabeled_Videos_via_Embodiment-Centric_ICCV_2025_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Chen_EC-Flow_Enabling_Versatile_Robotic_Manipulation_from_Action-Unlabeled_Videos_via_Embodiment-Centric_ICCV_2025_paper.pdf#page=8)

## Observation–State–Action Interface

영상·지시 → embodiment flow → kinematic 제약 기반 robot action.

## Evaluation Scope and Claim Boundary

Meta-World와 실제 가림·변형·비변위 조작을 평가한다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/ICCV2025/html/Chen_EC-Flow_Enabling_Versatile_Robotic_Manipulation_from_Action-Unlabeled_Videos_via_Embodiment-Centric_ICCV_2025_paper.html) · [저자 project/code](https://ec-flow1.github.io/) · [공식 code](https://github.com/YixiangChen515/EC-Flow).

## 검색 태그 근거

조건부 확산 모델이 영상·지시에서 로봇 표면점의 2D 이동을 예측한다. URDF와 관절 투영으로 행동을 복원하고 Meta-World 및 실물 Franka에서 평가한다. flow는 예측하는 점의 움직임을 뜻한다. [원문 3쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Chen_EC-Flow_Enabling_Versatile_Robotic_Manipulation_from_Action-Unlabeled_Videos_via_Embodiment-Centric_ICCV_2025_paper.pdf#page=3) · [원문 6쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Chen_EC-Flow_Enabling_Versatile_Robotic_Manipulation_from_Action-Unlabeled_Videos_via_Embodiment-Centric_ICCV_2025_paper.pdf#page=6)

## Why This Paper Is Here — Researcher Interpretation

행동 표현을 통합하는 연구에서 object motion과 robot motion의 차이를 보존할 대안이다.

## Verification Boundary

URDF만으로 해결되는 변환 범위, calibration, 동역학·접촉 정보 의존성을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
