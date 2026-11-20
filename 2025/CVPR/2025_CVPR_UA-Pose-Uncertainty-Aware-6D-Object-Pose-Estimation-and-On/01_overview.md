# UA-Pose: Uncertainty-Aware 6D Object Pose Estimation and Online Object Completion with Partial References

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Ming-Feng Li, Xin Yang, Fu-En Wang, Hritam Basak, Yuyin Sun, Shreekant Gayaka, Min Sun, Cheng-Hao Kuo
- Category: Robotics-Enabling 3D Perception
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 6D pose, partial references, uncertainty, object completion
- Aliases: UA-Pose
- Official paper: https://openaccess.thecvf.com/content/CVPR2025/html/Li_UA-Pose_Uncertainty-Aware_6D_Object_Pose_Estimation_and_Online_Object_Completion_CVPR_2025_paper.html
- Venue verification: https://openaccess.thecvf.com/content/CVPR2025/html/Li_UA-Pose_Uncertainty-Aware_6D_Object_Pose_Estimation_and_Online_Object_Completion_CVPR_2025_paper.html
- Code/Project: https://minfenli.github.io/UA-Pose/
- Code: https://github.com/minfenli/UA-Pose
- Source audit: 2026-11-18: 공식 초록·bibliographic record와 연결된 저자 자료 확인. Abstract 기반 등록이며 본문 전체·실험 재현은 미확인. 직접 HTML 접근 제한은 공식 사이트의 검색 색인 abstract/BibTeX 및 저자 abstract/project 자료로 교차 확인; HTML 전면 열람으로 기록하지 않음. Official GitHub root에는 README와 images만 확인됨; 구현 release로 세지 않는다.

## Problem and Importance

완전 CAD나 전체 표면 reference 없이 부분 관측만으로 미지 물체 pose를 추정해야 한다.

## Core Idea and Contribution

부분 3D 모델의 관측·미관측 영역 불확실성을 활용해 pose 신뢰도와 온라인 completion sampling을 다룬다.

## Observation–State–Action Interface

Known-pose RGB-D 소수 관측 또는 한 장의 reference 이미지에서 출발해 pose와 보완된 물체 표현을 출력한다.

## Evaluation Scope and Claim Boundary

YCB-Video·YCBInEOAT·HO3D의 로봇/손 조작 RGB-D 시퀀스를 평가한다. 제어 정책 성공의 실증과 구별한다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2025/html/Li_UA-Pose_Uncertainty-Aware_6D_Object_Pose_Estimation_and_Online_Object_Completion_CVPR_2025_paper.html) · [저자 project/code](https://minfenli.github.io/UA-Pose/) · [공식 저장소(구현 공개 미확인)](https://github.com/minfenli/UA-Pose). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

CAD 완전성 전제를 완화하는 geometry 대안으로 보존하되 첫 active-pose 비교의 필수 정독에서는 REFERENCE로 둔다.

## Verification Boundary

Image-to-3D 전제·미관측 uncertainty의 calibration·실세계 control 평가을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
