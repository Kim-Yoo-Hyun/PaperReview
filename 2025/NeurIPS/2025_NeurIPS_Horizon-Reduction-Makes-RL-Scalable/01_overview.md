# Horizon Reduction Makes RL Scalable

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / NeurIPS
- Authors: Seohong Park, Kevin Frans, Deepinder Mann, Benjamin Eysenbach, Aviral Kumar, Sergey Levine
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: offline-RL, scaling, temporal-abstraction, goal-conditioning
- Aliases: SHARSA
- Official paper: https://proceedings.neurips.cc/paper_files/paper/2025/hash/0c66099070429b9b49ad8bb19c740c22-Abstract-Conference.html
- Venue verification: https://proceedings.neurips.cc/paper_files/paper/2025/hash/0c66099070429b9b49ad8bb19c740c22-Abstract-Conference.html
- Code/Project: https://github.com/seohongpark/horizon-reduction
- Code: https://github.com/seohongpark/horizon-reduction
- Source audit: 2026-11-12: 공식 publication/초록 또는 저자 source 확인. 공식 초록과 metadata 수준의 정리다. 구체적 실험 조건·수치·본문 한계는 추가 확인이 필요하다. 초록·지정 project 범위이며 전체 정독·코드 실행·사용자 reading 완료를 뜻하지 않는다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

이 연구는 오프라인 강화학습에서 데이터와 계산을 늘려도 긴 의사결정 구간 때문에 성능 향상이 정체되는 조건을 분석한다. [PDF 1쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/0c66099070429b9b49ad8bb19c740c22-Paper-Conference.pdf#page=1)

## Core Idea and Contribution

- 가치 추정에서 보상을 거슬러 전달해야 하는 길이와 정책이 최종 목표까지 행동을 선택해야 하는 길이를 나눠 각각의 영향을 시험했다. [PDF 5쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/0c66099070429b9b49ad8bb19c740c22-Paper-Conference.pdf#page=5) · [PDF 7쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/0c66099070429b9b49ad8bb19c740c22-Paper-Conference.pdf#page=7)
- SHARSA는 다단계 가치 학습으로 평가한 중간 목표를 선택해 낮은 수준의 정책에 전달하며, 데이터 규모별 비교에서 두 구간을 줄인 효과를 측정했다. [PDF 8쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/0c66099070429b9b49ad8bb19c740c22-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/0c66099070429b9b49ad8bb19c740c22-Paper-Conference.pdf#page=9) · [PDF 10쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/0c66099070429b9b49ad8bb19c740c22-Paper-Conference.pdf#page=10)

## Observation–State–Action Interface

대규모 goal-conditioned data → horizon을 줄인 value/policy 학습 → 목표 행동.

## Evaluation Scope and Claim Boundary

다양한 긴 목표 과제의 scaling을 비교한다. 모든 online VLA RL의 원인으로 일반화하지 않는다.

근거: [공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2025/hash/0c66099070429b9b49ad8bb19c740c22-Abstract-Conference.html) · [저자 project/code](https://github.com/seohongpark/horizon-reduction). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

Chunk 길이·목표 분해와 데이터 scaling의 효과를 분리할 최신 기준 연구다.

## Verification Boundary

본문에서 확인할 항목: 유효 결정 길이·coverage·데이터 크기·학습 계산량·물리 시간. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 공개 자료

- 코드 · SHARSA 하위 목표 표집·선택 · agents/sharsa.py [배포 파일](https://raw.githubusercontent.com/seohongpark/horizon-reduction/c298aedcc505bc7a7b44b4d0c9318993f8b3f3fd/agents/sharsa.py)
- 가중치 · HumanoidMaze 자료 생성에 사용한 OGBench 전문가 정책. SHARSA 학습 결과와 구별함 · experts.tar.gz [배포 파일](https://rail.eecs.berkeley.edu/datasets/ogbench/experts.tar.gz)
- 데이터 · 저자가 공개한 100M 규모 cube-octuple-play의 한 분할 · cube-octuple-play-v0-000.npz [배포 파일](https://rail.eecs.berkeley.edu/datasets/ogbench/cube-octuple-play-100m-v0/cube-octuple-play-v0-000.npz)
