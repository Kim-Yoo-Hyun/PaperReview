# OGBench: Benchmarking Offline Goal-Conditioned RL

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / ICLR
- Authors: Seohong Park, Kevin Frans, Benjamin Eysenbach, Sergey Levine
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: goal-conditioned-RL, long-horizon, Benchmark
- Aliases: OGBench
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2025/hash/ecd92623ac899357312aaa8915853699-Abstract-Conference.html
- Venue verification: https://proceedings.iclr.cc/paper_files/paper/2025/hash/ecd92623ac899357312aaa8915853699-Abstract-Conference.html
- Code/Project: https://github.com/seohongpark/ogbench
- Code: https://github.com/seohongpark/ogbench
- Source audit: 2026-10-19: 공식 paper abstract 및 저자 project/code README 확인; abstract 기반 — 본문 수동 확인 필요. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

OGBench는 보상 라벨이 없는 오프라인 데이터에서 목표 도달 정책을 배울 때 어떤 능력이 성능을 좌우하는지 비교하는 벤치마크다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/ecd92623ac899357312aaa8915853699-Paper-Conference.pdf#page=1)

## Core Idea and Contribution

- 궤적 조각을 이어야 하는 문제, 장기 목표, 고차원 관측, 확률적 전이를 구분해 시험할 환경과 데이터를 구성했다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/ecd92623ac899357312aaa8915853699-Paper-Conference.pdf#page=1) · [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/ecd92623ac899357312aaa8915853699-Paper-Conference.pdf#page=4)
- 여섯 대표 알고리즘을 비교해 기존 평가에서 비슷한 점수를 받는 방법도 요구되는 능력에 따라 강점이 달라짐을 보였다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/ecd92623ac899357312aaa8915853699-Paper-Conference.pdf#page=1) · [PDF 9쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/ecd92623ac899357312aaa8915853699-Paper-Conference.pdf#page=9)

## Observation–State–Action Interface

Offline transition data + goal → policy/action; unlabeled data에서의 goal-conditioned 학습을 평가한다.

## Evaluation Scope and Claim Boundary

ICLR abstract는 8종 환경, 85 datasets 및 6 reference algorithm을 보고한다. Task/split별 정확한 성공 정의는 본문 확인 필요.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ecd92623ac899357312aaa8915853699-Abstract-Conference.html) · [저자 project/code](https://github.com/seohongpark/ogbench). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

Benchmark. Stitching·장기 horizon·pixel input 등의 능력을 구분하는 기준이다. FQL/Q-chunking/DQC 결과를 이해하는 prerequisite이며 LIBERO/CALVIN과 평가 목적을 구분한다. Language-conditioned real-robot benchmark는 아니다.

## Verification Boundary

Goal sampling, reward relabeling, split/dataset 품질과 성공률 aggregation을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
