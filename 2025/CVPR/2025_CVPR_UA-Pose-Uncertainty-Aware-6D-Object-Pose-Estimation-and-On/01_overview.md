# UA-Pose: Uncertainty-Aware 6D Object Pose Estimation and Online Object Completion with Partial References

> Evidence maturity: `FULL_TEXT_CHECKED`. 요약과 기여를 아래 쪽수에서 확인했다.

- Year/Venue: 2025 / CVPR
- Authors: Ming-Feng Li, Xin Yang, Fu-En Wang, Hritam Basak, Yuyin Sun, Shreekant Gayaka, Min Sun, Cheng-Hao Kuo
- Category: Robotics-Enabling 3D Perception
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 6D pose, partial references, uncertainty, object completion, RGB-D
- Aliases: UA-Pose
- Official paper: https://openaccess.thecvf.com/content/CVPR2025/html/Li_UA-Pose_Uncertainty-Aware_6D_Object_Pose_Estimation_and_Online_Object_Completion_CVPR_2025_paper.html
- Venue verification: https://openaccess.thecvf.com/content/CVPR2025/html/Li_UA-Pose_Uncertainty-Aware_6D_Object_Pose_Estimation_and_Online_Object_Completion_CVPR_2025_paper.html
- Code/Project: https://minfenli.github.io/UA-Pose/
- Code: https://github.com/minfenli/UA-Pose
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2025/papers/Li_UA-Pose_Uncertainty-Aware_6D_Object_Pose_Estimation_and_Online_Object_Completion_CVPR_2025_paper.pdf
- Source audit: 2026-11-24에 요약과 핵심 기여 두 개를 원문과 대조했다. 평가 조건은 04_evaluation.md에 쪽수와 함께 기록했다. 11월 18일 저자 저장소에서는 README와 이미지만 확인했다.

## Problem and Importance

UA-Pose는 일부 시점만 주어진 물체의 6자유도 자세를 추정하면서 관찰되지 않은 표면의 불확실성을 이용해 물체 모형을 온라인으로 보완한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Li_UA-Pose_Uncertainty-Aware_6D_Object_Pose_Estimation_and_Online_Object_Completion_CVPR_2025_paper.pdf#page=1) · [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Li_UA-Pose_Uncertainty-Aware_6D_Object_Pose_Estimation_and_Online_Object_Completion_CVPR_2025_paper.pdf#page=3)

## Core Idea and Contribution

- 알려진 자세의 RGB-D 참조 또는 단일 이미지에서 초기 모형을 만들고, 관측 여부에 따른 불확실성을 자세 후보 평가와 표면 갱신에 사용한다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Li_UA-Pose_Uncertainty-Aware_6D_Object_Pose_Estimation_and_Online_Object_Completion_CVPR_2025_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Li_UA-Pose_Uncertainty-Aware_6D_Object_Pose_Estimation_and_Online_Object_Completion_CVPR_2025_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Li_UA-Pose_Uncertainty-Aware_6D_Object_Pose_Estimation_and_Online_Object_Completion_CVPR_2025_paper.pdf#page=5) · [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Li_UA-Pose_Uncertainty-Aware_6D_Object_Pose_Estimation_and_Online_Object_Completion_CVPR_2025_paper.pdf#page=6)
- YCB-Video, 로봇이 물체를 조작한 YCBInEOAT, 사람이 물체를 쥔 HO3D에서 부분 참조 조건의 자세 추정과 모형 완성 품질을 평가했다. [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Li_UA-Pose_Uncertainty-Aware_6D_Object_Pose_Estimation_and_Online_Object_Completion_CVPR_2025_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Li_UA-Pose_Uncertainty-Aware_6D_Object_Pose_Estimation_and_Online_Object_Completion_CVPR_2025_paper.pdf#page=8)

## Observation–State–Action Interface

Known-pose RGB-D 소수 관측 또는 한 장의 reference 이미지에서 출발해 pose와 보완된 물체 표현을 출력한다.

## Evaluation Scope and Claim Boundary

평가는 RGB-D 시퀀스의 6D 자세 정확도와 온라인 형상 완성도다. 자세에는 ADD·ADD-S의 곡선 아래 면적을, 형상에는 Chamfer 거리를 사용했다. [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Li_UA-Pose_Uncertainty-Aware_6D_Object_Pose_Estimation_and_Online_Object_Completion_CVPR_2025_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Li_UA-Pose_Uncertainty-Aware_6D_Object_Pose_Estimation_and_Online_Object_Completion_CVPR_2025_paper.pdf#page=8)

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2025/html/Li_UA-Pose_Uncertainty-Aware_6D_Object_Pose_Estimation_and_Online_Object_Completion_CVPR_2025_paper.html) · [저자 project/code](https://minfenli.github.io/UA-Pose/) · [공식 저장소(구현 공개 미확인)](https://github.com/minfenli/UA-Pose).

## 검색 태그 근거

참조에서 관측한 표면을 렌더링해 영상 마스크와의 겹침으로 자세 신뢰도를 계산한다. 이미 촬영된 시퀀스에서 보관할 프레임을 선별해 형상을 보완한다. 평가 지표는 물체 자세 오차와 복원 형상의 거리다. [원문 5쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Li_UA-Pose_Uncertainty-Aware_6D_Object_Pose_Estimation_and_Online_Object_Completion_CVPR_2025_paper.pdf#page=5) · [원문 6쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Li_UA-Pose_Uncertainty-Aware_6D_Object_Pose_Estimation_and_Online_Object_Completion_CVPR_2025_paper.pdf#page=6) · [원문 7쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Li_UA-Pose_Uncertainty-Aware_6D_Object_Pose_Estimation_and_Online_Object_Completion_CVPR_2025_paper.pdf#page=7)

## Why This Paper Is Here — Researcher Interpretation

CAD 완전성 전제를 완화하는 geometry 대안으로 보존하되 첫 active-pose 비교의 필수 정독에서는 REFERENCE로 둔다.

## Verification Boundary

Image-to-3D 전제·미관측 uncertainty의 calibration·실세계 control 평가을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
