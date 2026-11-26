# Reinforcement Learning for Real-Time Vision-Language-Action Policies

> Evidence maturity: `ABSTRACT_CHECKED`. 최초 등록은 초록에 근거하며, 아래에 별도 인용한 방법과 평가는 원문 해당 쪽에서 확인했다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Authors: Perry Dong, Kuo-Han Hung, Dorsa Sadigh, Chelsea Finn
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, reinforcement-learning, latency, reactive-control
- Aliases: Real-Time EXPO-FT
- Official paper: https://arxiv.org/abs/2609.18207
- Venue verification: https://arxiv.org/abs/2609.18207
- Code/Project: https://pd-perry.github.io/real-time-expo-ft/
- Code: https://github.com/pd-perry/expo-ft
- 방법·평가 확인 (2026-11-25): [원문 4, 5, 6, 7, 8, 14쪽](https://arxiv.org/pdf/2609.18207#page=4) · [다축 분류와 공개 범위](../../../work/sources/batches/core_next_10.yaml)
- Source audit: 2026-11-12: 공식 publication/초록 또는 저자 source 확인. arXiv v1와 저자 project/code에서 EXPO-FT 원 방법과 real-time branch의 구분 확인. 공식 conference acceptance는 확인하지 않았다. 초록·지정 project 범위이며 전체 정독·코드 실행·사용자 reading 완료를 뜻하지 않는다.

## Problem and Importance

VLA 계산 중 늦어진 관측으로 행동하면 동적 과제에서 분포 이동이 생긴다.

## Core Idea and Contribution

느린 VLA chunk 생성과 최신 관측을 사용하는 빠른 action edit를 분리해 EXPO-FT를 실시간 RL로 확장한다.

## Observation–State–Action Interface

느린 VLA action chunk + 최신 관측 → 경량 edit policy → 즉시 로봇 행동.

## Evaluation Scope and Claim Boundary

Kinetix와 실제 물체 전달·공 균형·테이블 축구·동적 pick을 평가한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2609.18207) · [저자 project/code](https://pd-perry.github.io/real-time-expo-ft/) · [공식 code](https://github.com/pd-perry/expo-ft). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

지연·feedback 공백의 직접 선행이자 단일 정책 선호와 별도로 보존할 강한 editor pipeline baseline이다.

## Verification Boundary

본문에서 확인할 항목: edit 주파수·관측 timestamp·동기화·robot interaction 비용·단일 정책 여부. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 원문에서 확인한 방법과 평가

Real-Time EXPO-FT는 비동기 VLA가 미리 낸 행동 청크를 더 최근 관측에서 편집하고 비평가로 선택한다. 편집 정책과 VLA를 함께 갱신하며 늦게 도착한 후보를 현재의 상태에서 비교한다. Kinetix 시뮬레이션 10개 과제와 빠른 반응이 필요한 실물 조작 4개 과제에서 지연 조건을 비교했다. [방법·평가 · PDF 4, 5, 6, 7, 8, 14쪽](https://arxiv.org/pdf/2609.18207#page=4)

## 공개 자료의 확인 범위

- 로봇 정책의 비동기 온라인 학습 진입점 · train_pi_robo_async.py [배포 파일](https://raw.githubusercontent.com/pd-perry/expo-ft/21fe3d3b7d913c80836496817965932f49e0aedf/train_pi_robo_async.py)
