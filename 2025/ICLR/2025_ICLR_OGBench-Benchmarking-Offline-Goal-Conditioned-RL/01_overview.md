# OGBench: Benchmarking Offline Goal-Conditioned RL

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
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
- Source audit: 2026-10-19: 공식 paper abstract 및 저자 project/code README 확인; abstract 기반 — 본문 수동 확인 필요.

## Problem and Importance

Offline goal-conditioned RL 알고리즘의 stitching·long-horizon·pixel input 성능을 체계적으로 비교할 benchmark가 부족하다.

## Core Idea and Contribution

다양한 goal-conditioned environment/dataset와 reference algorithm 구현을 제공하여 능력별 차이를 드러낸다.

## Observation–State–Action Interface

Offline transition data + goal → policy/action; unlabeled data에서의 goal-conditioned 학습을 평가한다.

## Evaluation Scope and Claim Boundary

ICLR abstract는 8종 환경, 85 datasets 및 6 reference algorithm을 보고한다. Task/split별 정확한 성공 정의는 본문 확인 필요.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ecd92623ac899357312aaa8915853699-Abstract-Conference.html) · [저자 project/code](https://github.com/seohongpark/ogbench). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

Benchmark. Stitching·장기 horizon·pixel input 등의 능력을 구분하는 기준이다. FQL/Q-chunking/DQC 결과를 이해하는 prerequisite이며 LIBERO/CALVIN과 평가 목적을 구분한다. Language-conditioned real-robot benchmark는 아니다.

## Verification Boundary

Goal sampling, reward relabeling, split/dataset 품질과 성공률 aggregation을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
