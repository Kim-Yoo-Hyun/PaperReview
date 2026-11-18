# Robotic task success evaluation under multi-modal non-parametric object pose uncertainty

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / Industrial Robot
- Category: Robotics-Enabling 3D Perception
- Primary track: Robotics-enabling 3D perception
- Tier: NEXT
- Tags: pose uncertainty, task success, mobile manipulation, tolerance
- Aliases:
- Official paper: https://www.emerald.com/ir/article-abstract/52/5/651/1254840/Robotic-task-success-evaluation-under-multi-modal?redirectedFrom=PDF
- Venue verification: https://www.emerald.com/ir/article-abstract/52/5/651/1254840/Robotic-task-success-evaluation-under-multi-modal?redirectedFrom=PDF
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-11-18: 공식 초록·bibliographic record와 연결된 저자 자료 확인. Abstract 기반 등록이며 본문 전체·실험 재현은 미확인. Industrial Robot 52(5), 651–662; top-tier로 표시하지 않는다. 2024 preprint와 2025 journal은 동일 entry로 관리.

## Problem and Importance

정확한 pose가 아니어도 task가 성공할 수 있으므로 pose error만으로 행동 여부를 결정하기 어렵다.

## Core Idea and Contribution

Simulation으로 허용 pose-error 공간을 미리 구하고 다봉 추정 오차 분포와 적분해 task 성공 가능성을 계산한다.

## Observation–State–Action Interface

Pose uncertainty와 task-specific acceptable-error 공간에서 성공 가능성을 얻는다. VLA 표현 학습은 별도다.

## Evaluation Scope and Claim Boundary

공식 publisher 초록은 두 mobile manipulation task의 성공/실패 평가를 명시한다.

근거: [공식 paper/abstract](https://www.emerald.com/ir/article-abstract/52/5/651/1254840/Robotic-task-success-evaluation-under-multi-modal?redirectedFrom=PDF). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

불확실성이 남아도 성공하면 행동한다는 원리를 신규성에서 제외하게 하는 직접 비교다.

## Verification Boundary

허용 오차 precompute 비용·동역학 전제·online pose distribution·최종본과 preprint 차이을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
