# MolmoSpaces: Large-Scale Open Ecosystem for Robot Manipulation and Navigation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Benchmark, Dataset, manipulation, Navigation
- Aliases: MolmoSpaces, MolmoSpaces: A Large-Scale Open Ecosystem for Robot Navigation and Manipulation
- Official paper: https://roboticsproceedings.org/rss22/p091.html
- Venue verification: https://roboticsproceedings.org/rss22/p091.html
- Code/Project: https://github.com/allenai/molmospaces
- Code: https://github.com/allenai/molmospaces
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인. RSS title와 arXiv의 navigation/manipulation 순서가 다르지만 같은 연구다. Simulator-agnostic assets와 모든 backend의 실행 지원을 구분한다. 본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지.

## Problem and Importance

실험실의 제한된 장면으로 generalist 정책의 생활환경 변이를 측정하기 어렵다.

## Core Idea and Contribution

다양한 실내 환경·상호작용 객체·grasp 자산과 통합 benchmark를 제공한다.

## Observation–State–Action Interface

장면·객체·로봇 설정 → simulator 기반 조작·항법 과제.

## Evaluation Scope and Claim Boundary

조작·항법을 포함한 8개 benchmark task와 sim-to-real 상관을 보고한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p091.html) · [저자 project/code](https://github.com/allenai/molmospaces). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

현재 후보의 한 benchmark 의존을 줄일 추가 환경·데이터 자원이다.

## Verification Boundary

asset license, 실제 지원 simulator별 기능, 장면 split, 정책별 co-training 여부을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
