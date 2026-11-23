# GeoPredict: Leveraging Predictive Kinematics and 3D Gaussian Geometry for Precise VLA Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / CVPR
- Authors: Jingjing Qian, Boyao Han, Chen Shi, Lei Xiao, Long Yang, Shaoshuai Shi, Li Jiang
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, 3D Gaussian, predictive geometry, kinematics
- Aliases: GeoPredict
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Qian_GeoPredict_Leveraging_Predictive_Kinematics_and_3D_Gaussian_Geometry_for_Precise_CVPR_2026_paper.html
- Venue verification: https://openaccess.thecvf.com/content/CVPR2026/html/Qian_GeoPredict_Leveraging_Predictive_Kinematics_and_3D_Gaussian_Geometry_for_Precise_CVPR_2026_paper.html
- Code/Project: https://github.com/jingjingqian75/GeoPredict
- Code: https://github.com/jingjingqian75/GeoPredict
- Source audit: 2026-11-18: 공식 초록·bibliographic record와 연결된 저자 자료 확인. Abstract 기반 등록이며 본문 전체·실험 재현은 미확인. 직접 HTML 접근 제한은 공식 사이트의 검색 색인 abstract/BibTeX 및 저자 abstract/project 자료로 교차 확인; HTML 전면 열람으로 기록하지 않음. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

GeoPredict는 미래 로봇 관절부의 3차원 이동과 작업 공간의 기하를 학습 신호로 삼아 연속 행동을 내는 VLA의 정밀 조작을 개선한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Qian_GeoPredict_Leveraging_Predictive_Kinematics_and_3D_Gaussian_Geometry_for_Precise_CVPR_2026_paper.pdf#page=1)

## Core Idea and Contribution

- 로봇팔 키포인트의 미래 궤적과 주변 3차원 가우시안을 예측해 깊이 렌더링으로 감독하고, 실행 시에는 기하 복호화 없이 추가 질의 토큰만 쓴다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Qian_GeoPredict_Leveraging_Predictive_Kinematics_and_3D_Gaussian_Geometry_for_Precise_CVPR_2026_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Qian_GeoPredict_Leveraging_Predictive_Kinematics_and_3D_Gaussian_Geometry_for_Precise_CVPR_2026_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Qian_GeoPredict_Leveraging_Predictive_Kinematics_and_3D_Gaussian_Geometry_for_Precise_CVPR_2026_paper.pdf#page=5)
- RoboCasa·LIBERO와 실제 조작에서 작업 성공을 비교하고 운동학 예측과 기하 감독을 각각 제거해 기여를 평가했다. [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Qian_GeoPredict_Leveraging_Predictive_Kinematics_and_3D_Gaussian_Geometry_for_Precise_CVPR_2026_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Qian_GeoPredict_Leveraging_Predictive_Kinematics_and_3D_Gaussian_Geometry_for_Precise_CVPR_2026_paper.pdf#page=8)

## Observation–State–Action Interface

Motion history·영상에서 action을 생성하며 3D decoding은 학습용이다. 배포 query token과 native 3D reconstruction을 구별한다.

## Evaluation Scope and Claim Boundary

RoboCasa Human-50·LIBERO·실세계 조작에서 geometry 관련 이득을 평가한다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Qian_GeoPredict_Leveraging_Predictive_Kinematics_and_3D_Gaussian_Geometry_for_Precise_CVPR_2026_paper.html) · [저자 project/code](https://github.com/jingjingqian75/GeoPredict). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

3D reconstruction auxiliary loss 자체가 새 기여가 아님을 보여 주는 직접 VLA 비교다.

## Verification Boundary

Depth supervision·keypoint target·배포 추가 token 비용·baseline data fairness을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
