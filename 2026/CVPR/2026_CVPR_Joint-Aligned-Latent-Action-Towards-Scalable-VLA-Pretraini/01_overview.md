# Joint-Aligned Latent Action: Towards Scalable VLA Pretraining in the Wild

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / CVPR
- Authors: Hao Luo, Ye Wang, Wanpeng Zhang, Haoqi Yuan, Yicheng Feng, Haiweng Xu, Sipeng Zheng, Zongqing Lu
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, latent-action, human-video, pretraining
- Aliases: JALA
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Luo_Joint-Aligned_Latent_Action_Towards_Scalable_VLA_Pretraining_in_the_Wild_CVPR_2026_paper.html
- Venue verification: https://openaccess.thecvf.com/content/CVPR2026/html/Luo_Joint-Aligned_Latent_Action_Towards_Scalable_VLA_Pretraining_in_the_Wild_CVPR_2026_paper.html
- Code/Project: https://research.beingbeyond.com/jala
- Code: https://github.com/BeingBeyond/JALA
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인. 저자 GitHub는 README/docs 공개 상태로 확인; 실행 구현 공개로 표시하지 않는다. 본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지.

## Problem and Importance

비정형 사람 영상에서 정확한 robot action supervision을 확보하기 어렵다.

## Core Idea and Contribution

역동역학과 실제 행동에 함께 정렬한 latent action을 학습한다.

## Observation–State–Action Interface

사람 영상 전이 → 행동 중심 embedding → VLA 사전학습.

## Evaluation Scope and Claim Boundary

사람 동작 및 simulation·실제 robot manipulation 전이를 평가한다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Luo_Joint-Aligned_Latent_Action_Towards_Scalable_VLA_Pretraining_in_the_Wild_CVPR_2026_paper.html) · [저자 project/code](https://research.beingbeyond.com/jala) · [공식 code](https://github.com/BeingBeyond/JALA). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

Unified VLA-RL의 action representation 기여를 판단할 사전학습 비교 기준이다.

## Verification Boundary

실제 action label 요구량, 인간 손과 robot action 대응, 비정형 영상 split을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
