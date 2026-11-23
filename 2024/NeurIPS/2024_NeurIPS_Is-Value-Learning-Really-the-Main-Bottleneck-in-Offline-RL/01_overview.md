# Is Value Learning Really the Main Bottleneck in Offline RL?

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2024 / NeurIPS
- Authors: Seohong Park, Kevin Frans, Sergey Levine, Aviral Kumar
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: offline-RL, policy-extraction, generalization, diagnosis
- Aliases: Offline RL bottlenecks
- Official paper: https://proceedings.neurips.cc/paper_files/paper/2024/hash/8ffb4e3118280a66b192b6f06e0e2596-Abstract-Conference.html
- Venue verification: https://proceedings.neurips.cc/paper_files/paper/2024/hash/8ffb4e3118280a66b192b6f06e0e2596-Abstract-Conference.html
- Code/Project:
- Code: not_identified
- Source audit: 2026-11-12: 공식 publication/초록 또는 저자 source 확인. 공식 초록과 metadata 수준의 정리다. 구체적 실험 조건·수치·본문 한계는 추가 확인이 필요하다. 초록·지정 project 범위이며 전체 정독·코드 실행·사용자 reading 완료를 뜻하지 않는다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

이 연구는 오프라인 강화학습의 성능 한계를 가치 추정, 가치에서 정책을 얻는 과정, 훈련 자료 밖 상태에 대한 일반화로 나누어 비교한다. [PDF 1쪽](https://proceedings.neurips.cc/paper_files/paper/2024/file/8ffb4e3118280a66b192b6f06e0e2596-Paper-Conference.pdf#page=1)

## Core Idea and Contribution

- 같은 가치 학습 조건에서도 어드밴티지 가중 행동 복제와 행동 제약을 둔 정책 기울기가 서로 다른 성능을 낼 수 있음을 보였다. [PDF 4쪽](https://proceedings.neurips.cc/paper_files/paper/2024/file/8ffb4e3118280a66b192b6f06e0e2596-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.neurips.cc/paper_files/paper/2024/file/8ffb4e3118280a66b192b6f06e0e2596-Paper-Conference.pdf#page=5)
- 훈련 상태에서의 성능과 배포 중 방문하는 상태에서의 성능을 분리하고, 상태 범위가 넓은 자료와 실행 시 정책 개선이 일반화에 미치는 효과를 시험했다. [PDF 6쪽](https://proceedings.neurips.cc/paper_files/paper/2024/file/8ffb4e3118280a66b192b6f06e0e2596-Paper-Conference.pdf#page=6) · [PDF 7쪽](https://proceedings.neurips.cc/paper_files/paper/2024/file/8ffb4e3118280a66b192b6f06e0e2596-Paper-Conference.pdf#page=7) · [PDF 8쪽](https://proceedings.neurips.cc/paper_files/paper/2024/file/8ffb4e3118280a66b192b6f06e0e2596-Paper-Conference.pdf#page=8)

## Observation–State–Action Interface

같은 offline data·가치함수 → 서로 다른 policy extraction → ID/OOD 상태 행동.

## Evaluation Scope and Claim Boundary

Offline RL의 extraction 선택과 데이터 coverage·test-time 정책 개선을 실증 비교한다.

근거: [공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2024/hash/8ffb4e3118280a66b192b6f06e0e2596-Abstract-Conference.html). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

단일 VLA critic 개선 후보가 actor 학습·coverage 효과를 놓치지 않도록 하는 핵심 원인 분석이다.

## Verification Boundary

본문에서 확인할 항목: critic 고정·extraction 예산·평가 state coverage·test-time 최적화 비용. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
