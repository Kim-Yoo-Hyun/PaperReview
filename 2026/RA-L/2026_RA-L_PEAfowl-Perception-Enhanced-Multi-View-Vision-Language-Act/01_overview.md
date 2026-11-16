# PEAfowl: Perception-Enhanced Multi-View Vision-Language-Action for Bimanual Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RA-L
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: multi-view, 3D-representation, bimanual, VLA
- Aliases: PEAfowl
- Official paper: https://ieeexplore.ieee.org/document/11661761/
- Venue verification: https://ieeexplore.ieee.org/document/11661761/
- Code/Project: https://peafowlvla.github.io/
- Code: https://github.com/Qingyu-Fan/PEAfowl
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인. RA-L 11(10), 11841–11848, October 2026; first online 2026-08-21. Crossref issue metadata checked 11/08. 본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지.

## Problem and Importance

양팔 조작에서 다중 시점 간 기하 정합과 언어 의미의 결합이 필요하다.

## Core Idea and Contribution

깊이 분포 기반 3D lifting·cross-view 이웃 집계·text-aware readout을 사용하고 학습 시 depth distillation을 적용한다.

## Observation–State–Action Interface

다중 시점 영상·지시 → 3D-aware VLA 표현 → 양팔 행동.

## Evaluation Scope and Claim Boundary

RoboTwin2.0과 실제 양팔 조작을 평가한다.

근거: [공식 paper/abstract](https://ieeexplore.ieee.org/document/11661761/) · [저자 project/code](https://peafowlvla.github.io/) · [공식 code](https://github.com/Qingyu-Fan/PEAfowl). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

VLA-RL 성능 병목이 reward보다 공간 지각에 있을 때 비교할 표현 대안이다.

## Verification Boundary

학습 depth 정답 비용, 추론 depth 필요 여부, unseen camera/object 전이을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
