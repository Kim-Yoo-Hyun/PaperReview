# AC2-VLA: Action-Context-Aware Adaptive Computation in Vision-Language-Action Models for Efficient Robotic Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
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
- Source audit: 2026-11-12: 공식 publication/초록 또는 저자 source 확인. 공식 초록과 metadata 수준의 정리다. 구체적 실험 조건·수치·본문 한계는 추가 확인이 필요하다. 초록·지정 project 범위이며 전체 정독·코드 실행·사용자 reading 완료를 뜻하지 않는다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

AC2-VLA는 현재 영상과 지시, 직전 행동을 보고 어느 시점에 시각언어 백본의 어떤 연산을 수행할지 조절한다. [PDF 1쪽](https://www.ijcai.org/proceedings/2026/0228.pdf#page=1)

## Core Idea and Contribution

- 이전 계산의 재사용, 토큰 제거, 일부 구성 요소의 선택적 실행을 결합하고 전체 모델의 행동 출력을 교사로 삼아 계산 정책을 학습한다. [PDF 3쪽](https://www.ijcai.org/proceedings/2026/0228.pdf#page=3) · [PDF 4쪽](https://www.ijcai.org/proceedings/2026/0228.pdf#page=4)
- SIMPLER의 Google Robot·WidowX 과제에서 성공률과 추론 비용을 함께 측정하고 각 연산 절감 전략을 제거한 경우와 비교했다. [PDF 5쪽](https://www.ijcai.org/proceedings/2026/0228.pdf#page=5) · [PDF 6쪽](https://www.ijcai.org/proceedings/2026/0228.pdf#page=6) · [PDF 7쪽](https://www.ijcai.org/proceedings/2026/0228.pdf#page=7)

## Observation–State–Action Interface

현재 관측·지시·이전 동작 → 계산 선택 → VLA action.

## Evaluation Scope and Claim Boundary

Robotic manipulation benchmark에서 계산량·속도와 성공을 비교한다. 초록만으로 real-robot trial 조건은 확정하지 않는다.

근거: [공식 paper/abstract](https://ijcai.org/proceedings/2026/228) · [저자 project/code](https://github.com/SunnyYWD/AC-2-VLA). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

RL 기반 시간 적응과 비교할 학습된 계산 절감 baseline이며 지연·feedback·성능의 비용 분리를 돕는다.

## Verification Boundary

본문에서 확인할 항목: 관측 age·cache invalidation·학습 추가 비용·FLOPs와 실측 latency. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
