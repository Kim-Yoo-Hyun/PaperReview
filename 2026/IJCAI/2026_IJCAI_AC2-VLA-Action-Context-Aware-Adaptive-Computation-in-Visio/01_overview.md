# AC2-VLA: Action-Context-Aware Adaptive Computation in Vision-Language-Action Models for Efficient Robotic Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / IJCAI
- Authors: Wenda Yu, Tianshi Wang, Fengling Li, Jingjing Li, Lei Zhu
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, adaptive-computation, latency, action-context
- Aliases: AC2-VLA, AC^2-VLA, AC²-VLA
- Official paper: https://ijcai.org/proceedings/2026/228
- Venue verification: https://ijcai.org/proceedings/2026/228
- Code/Project: https://github.com/SunnyYWD/AC-2-VLA
- Code: https://github.com/SunnyYWD/AC-2-VLA
- Source audit: 2026-11-12: 공식 publication/초록 또는 저자 source 확인. 공식 초록과 metadata 수준의 정리다. 구체적 실험 조건·수치·본문 한계는 추가 확인이 필요하다. 초록·지정 project 범위이며 전체 정독·코드 실행·사용자 reading 완료를 뜻하지 않는다.

## Problem and Importance

큰 VLA backbone의 반복 계산이 closed-loop 행동을 지연시킨다.

## Core Idea and Contribution

영상·지시·이전 행동 context로 cache 재사용·token pruning·layer 실행을 조절하고 action-guided distillation으로 학습한다.

## Observation–State–Action Interface

현재 관측·지시·이전 동작 → 계산 선택 → VLA action.

## Evaluation Scope and Claim Boundary

Robotic manipulation benchmark에서 계산량·속도와 성공을 비교한다. 초록만으로 real-robot trial 조건은 확정하지 않는다.

근거: [공식 paper/abstract](https://ijcai.org/proceedings/2026/228) · [저자 project/code](https://github.com/SunnyYWD/AC-2-VLA). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

RL 기반 시간 적응과 비교할 학습된 계산 절감 baseline이며 지연·feedback·성능의 비용 분리를 돕는다.

## Verification Boundary

본문에서 확인할 항목: 관측 age·cache invalidation·학습 추가 비용·FLOPs와 실측 latency. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
