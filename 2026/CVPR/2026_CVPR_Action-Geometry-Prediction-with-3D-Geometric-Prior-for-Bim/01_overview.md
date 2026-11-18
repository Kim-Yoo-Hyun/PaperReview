# Action-Geometry Prediction with 3D Geometric Prior for Bimanual Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / CVPR
- Category: Manipulation, Contact, and Dexterity
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: bimanual manipulation, 3D geometry, diffusion policy, action chunk
- Aliases: GAP
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_Action-Geometry_Prediction_with_3D_Geometric_Prior_for_Bimanual_Manipulation_CVPR_2026_paper.pdf
- Venue verification: https://openaccess.thecvf.com/CVPR2026?day=2026-06-07
- Code/Project: https://github.com/Chongyang-99/GAP
- Code: https://github.com/Chongyang-99/GAP
- Source audit: 2026-11-18: 공식 초록·bibliographic record와 연결된 저자 자료 확인. Abstract 기반 등록이며 본문 전체·실험 재현은 미확인. 직접 HTML 접근 제한은 공식 사이트의 검색 색인 abstract/BibTeX 및 저자 abstract/project 자료로 교차 확인; HTML 전면 열람으로 기록하지 않음. GAP는 공식 CVF PDF의 색인 abstract/header 및 CVF 일자별 BibTeX로 확인했다. PDF local cache는 만들지 않았다.

## Problem and Importance

양팔 조작은 물체와 두 팔의 geometry 변화를 함께 예측해야 한다.

## Core Idea and Contribution

3D foundation latent·2D semantic feature·proprioception을 합쳐 action chunk와 미래 3D latent를 공동 예측한다.

## Observation–State–Action Interface

RGB·proprioception → action chunk 및 dense point map으로 해석할 미래 latent. RL exploration covariance와 별개다.

## Evaluation Scope and Claim Boundary

RoboTwin simulation과 실세계 양팔 조작에서 성공·협응·공간 예측을 비교한다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_Action-Geometry_Prediction_with_3D_Geometric_Prior_for_Bimanual_Manipulation_CVPR_2026_paper.pdf) · [저자 project/code](https://github.com/Chongyang-99/GAP). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

관계 기반 탐색 후보에서 geometry representation 이득과 exploration 변경의 이득을 구별하는 직접 비교다.

## Verification Boundary

미래 geometry target·3D foundation freeze 여부·양팔 action frame·data budget을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
