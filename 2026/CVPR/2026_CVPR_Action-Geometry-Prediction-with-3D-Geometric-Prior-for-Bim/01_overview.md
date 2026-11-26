# Action-Geometry Prediction with 3D Geometric Prior for Bimanual Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / CVPR
- Authors: Chongyang Xu, Haipeng Li, Shen Cheng, Haoqiang Fan, Ziliang Feng, Shuaicheng Liu
- Category: Manipulation, Contact, and Dexterity
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: bimanual manipulation, 3D geometry, diffusion policy, action chunk
- Aliases: GAP
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Xu_Action-Geometry_Prediction_with_3D_Geometric_Prior_for_Bimanual_Manipulation_CVPR_2026_paper.html
- Venue verification: https://openaccess.thecvf.com/CVPR2026?day=2026-06-07
- Code/Project: https://github.com/Chongyang-99/GAP
- Code: https://github.com/Chongyang-99/GAP
- 방법·평가 확인 (2026-11-25): [원문 3, 4, 5, 6, 7, 8쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_Action-Geometry_Prediction_with_3D_Geometric_Prior_for_Bimanual_Manipulation_CVPR_2026_paper.pdf#page=3) · [다축 분류와 공개 범위](../../../work/sources/batches/core_next_10.yaml)
- Source audit: 2026-11-18: 공식 초록·bibliographic record와 연결된 저자 자료 확인. Abstract 기반 등록이며 본문 전체·실험 재현은 미확인. 직접 HTML 접근 제한은 공식 사이트의 검색 색인 abstract/BibTeX 및 저자 abstract/project 자료로 교차 확인; HTML 전면 열람으로 기록하지 않음. GAP는 공식 CVF PDF의 색인 abstract/header 및 CVF 일자별 BibTeX로 확인했다. PDF local cache는 만들지 않았다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

이 연구는 RGB에서 얻은 기하 특징과 로봇의 고유수용감각으로 두 팔의 다음 행동 묶음과 그 뒤의 3차원 장면을 함께 예측한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_Action-Geometry_Prediction_with_3D_Geometric_Prior_for_Bimanual_Manipulation_CVPR_2026_paper.pdf#page=1)

## Core Idea and Contribution

- 사전학습된 3차원 모델의 잠재 표현에 2차원 의미 특징을 결합하고, 확산 모형이 예측한 미래 기하를 조밀한 점 지도로 복호화한다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_Action-Geometry_Prediction_with_3D_Geometric_Prior_for_Bimanual_Manipulation_CVPR_2026_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_Action-Geometry_Prediction_with_3D_Geometric_Prior_for_Bimanual_Manipulation_CVPR_2026_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_Action-Geometry_Prediction_with_3D_Geometric_Prior_for_Bimanual_Manipulation_CVPR_2026_paper.pdf#page=5)
- RoboTwin에서 양팔의 역할·동시성·순서가 다른 과제를 나눠 비교하고 실제 로봇에서도 정책의 손 협응과 조작 성공을 평가했다. [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_Action-Geometry_Prediction_with_3D_Geometric_Prior_for_Bimanual_Manipulation_CVPR_2026_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_Action-Geometry_Prediction_with_3D_Geometric_Prior_for_Bimanual_Manipulation_CVPR_2026_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_Action-Geometry_Prediction_with_3D_Geometric_Prior_for_Bimanual_Manipulation_CVPR_2026_paper.pdf#page=8)

## Observation–State–Action Interface

RGB·proprioception → action chunk 및 dense point map으로 해석할 미래 latent. RL exploration covariance와 별개다.

## Evaluation Scope and Claim Boundary

RoboTwin simulation과 실세계 양팔 조작에서 성공·협응·공간 예측을 비교한다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_Action-Geometry_Prediction_with_3D_Geometric_Prior_for_Bimanual_Manipulation_CVPR_2026_paper.pdf) · [저자 project/code](https://github.com/Chongyang-99/GAP). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

관계 기반 탐색 후보에서 geometry representation 이득과 exploration 변경의 이득을 구별하는 직접 비교다.

## Verification Boundary

미래 geometry target·3D foundation freeze 여부·양팔 action frame·data budget을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 공개 자료의 확인 범위

- RoboTwin용 GAP 양팔 정책 배포 모듈 · deploy_policy.py [배포 파일](https://raw.githubusercontent.com/Chongyang-99/GAP/dc6591904f564354b8cb2aeb3f016bdfc75ca5f5/deploy_policy.py)
