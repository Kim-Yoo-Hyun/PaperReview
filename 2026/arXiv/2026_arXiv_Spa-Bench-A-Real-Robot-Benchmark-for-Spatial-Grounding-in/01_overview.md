# Spa-Bench: A Real-Robot Benchmark for Spatial Grounding in Vision-Language-Action Models

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Category: Benchmarks and Datasets
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Robotics, VLA, spatial-grounding, counting, real-robot-benchmark
- Aliases: Spa-Bench (robotics)
- Official paper: https://arxiv.org/abs/2610.12696
- Venue verification: https://arxiv.org/abs/2610.12696
- Code/Project: https://justintiensmith.github.io/Spa-Bench/
- Code: not_identified
- Source audit: 2026-11-01 공식 서지/abstract·project/code 소개 확인. arXiv v1 및 저자 project 확인. Robotics 논문이며 동명 ICLR 2025 smartphone-agent benchmark와 다르다. 학회 채택은 확인되지 않아 arXiv로 등록. 신규 노트는 보수적으로 abstract/project 범위이며, 기존 SET의 지정 본문/code 감사는 별도 source ledger를 따른다. 정독·native 실행을 뜻하지 않는다.

## Problem and Importance

조작 성공률만으로는 공간 표현을 이해했는지와 기본 운동 능력이 부족한지를 구별하기 어렵다.

## Core Idea and Contribution

SO-101의 공간 지시 과제에서 익숙한 객체·개념·행동을 유지한 배치 변화와 직접 지시·표현·무행동 진단을 비교한다.

## Observation–State–Action Interface

실제 로봇의 관측·공간 언어 지시 → VLA 행동 → 목표별 채점. Counting과 no-action을 별도 진단으로 포함한다.

## Evaluation Scope and Claim Boundary

저자는 여섯 tabletop task와 여러 VLA의 실제 rollout을 보고한다. 전체 protocol을 수행한 모델과 부분 baseline이 다르므로 분모를 섞지 않는다. 공개 project의 model/data 링크는 확인했으나 독립 실행 code URL은 확인하지 못했다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2610.12696) · [저자 project/code](https://justintiensmith.github.io/Spa-Bench/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

집합·수량 후보의 가장 직접적인 counting/직접 지시 비교 선행이다. 알려진 공간 grounding 실패를 새 공백으로 과장하지 않도록 NEXT에 등록하며 preprint 경계를 유지한다.

## Verification Boundary

ID/OOD support, 모델별 완료 범위와 trial 분모, 직접 지시의 정보량, 최종 수량·무행동 채점, 공개 data/코드의 실제 가용 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
