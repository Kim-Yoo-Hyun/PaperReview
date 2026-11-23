# GeoPredict: Leveraging Predictive Kinematics and 3D Gaussian Geometry for Precise VLA Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
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
- Source audit: 2026-11-18: 공식 초록·bibliographic record와 연결된 저자 자료 확인. Abstract 기반 등록이며 본문 전체·실험 재현은 미확인. 직접 HTML 접근 제한은 공식 사이트의 검색 색인 abstract/BibTeX 및 저자 abstract/project 자료로 교차 확인; HTML 전면 열람으로 기록하지 않음.

## Problem and Importance

반응형 2D VLA가 정밀한 3D 상태 변화와 미래 움직임을 충분히 다루지 못한다.

## Core Idea and Contribution

로봇 keypoint trajectory와 3D Gaussian geometry 예측을 학습 supervision으로 사용한다.

## Observation–State–Action Interface

Motion history·영상에서 action을 생성하며 3D decoding은 학습용이다. 배포 query token과 native 3D reconstruction을 구별한다.

## Evaluation Scope and Claim Boundary

RoboCasa Human-50·LIBERO·실세계 조작에서 geometry 관련 이득을 평가한다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Qian_GeoPredict_Leveraging_Predictive_Kinematics_and_3D_Gaussian_Geometry_for_Precise_CVPR_2026_paper.html) · [저자 project/code](https://github.com/jingjingqian75/GeoPredict). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

3D reconstruction auxiliary loss 자체가 새 기여가 아님을 보여 주는 직접 VLA 비교다.

## Verification Boundary

Depth supervision·keypoint target·배포 추가 token 비용·baseline data fairness을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
