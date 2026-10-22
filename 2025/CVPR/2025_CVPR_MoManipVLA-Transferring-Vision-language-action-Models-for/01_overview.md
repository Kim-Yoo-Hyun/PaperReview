# MoManipVLA: Transferring Vision-language-action Models for General Mobile Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / CVPR
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: NEXT
- Tags: VLA, mobile-manipulation, control-interface
- Aliases:
- Official paper: https://openaccess.thecvf.com/content/CVPR2025/html/Wu_MoManipVLA_Transferring_Vision-language-action_Models_for_General_Mobile_Manipulation_CVPR_2025_paper.html
- Venue verification: https://openaccess.thecvf.com/content/CVPR2025/html/Wu_MoManipVLA_Transferring_Vision-language-action_Models_for_General_Mobile_Manipulation_CVPR_2025_paper.html
- Code/Project: https://gary3410.github.io/momanipVLA/
- Code: not_released
- Source audit: 2026-10-21: official abstract / author project 확인. 5개 note는 abstract 기반이며 사용자 정독을 의미하지 않는다.

## Problem and Importance

Fixed-base VLA의 도달 범위를 mobile manipulation으로 확장한다.

## Core Idea and Contribution

VLA의 end-effector waypoint와 base–arm bi-level trajectory optimization을 연결한다.

## Observation–State–Action Interface

언어·관측 → waypoint → base/arm trajectory.

## Evaluation Scope and Claim Boundary

OVMM 및 실제 로봇 평가를 보고한다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2025/html/Wu_MoManipVLA_Transferring_Vision-language-action_Models_for_General_Mobile_Manipulation_CVPR_2025_paper.html) · [저자 project/code](https://gary3410.github.io/momanipVLA/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

NaVILA·MoTo와 함께 VLA와 기하학적 실행 가능성의 경계를 비교하는 NEXT다.

## Verification Boundary

waypoint frame, solver budget, controller, real-robot split을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
