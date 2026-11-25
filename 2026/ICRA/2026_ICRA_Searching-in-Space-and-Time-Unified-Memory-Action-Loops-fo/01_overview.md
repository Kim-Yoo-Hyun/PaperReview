# Searching in Space and Time: Unified Memory-Action Loops for Open-World Object Retrieval

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ICRA
- Category: Embodied Navigation and Mapping
- Primary track: Planning and control
- Tier: REFERENCE
- Tags: mobile-manipulation, object-search, spatiotemporal-memory, Benchmark
- Aliases: STAR, STARBench
- Official paper: https://ieeexplore.ieee.org/document/11696368/
- Venue verification: https://ieeexplore.ieee.org/document/11696368/
- Code/Project: https://amrl.cs.utexas.edu/STAR/
- Code: https://github.com/ut-amrl/STARBench
- Source audit: ICRA 2026 IEEE 기탁 DOI와 저자 소속 연구실의 STARBench 설명, arXiv 초록을 확인했다. 코드 링크는 벤치마크 배포본이다.

## Problem and Importance

동적 환경에서 과거 위치나 속성으로 지칭한 물체를 현재 찾아야 한다.

## Core Idea and Contribution

장기 기억과 작업 기억을 이용해 과거 기록 조회와 물리적 탐색 중 다음 행동을 선택한다.

## Observation–State–Action Interface

공간·시간 표현이 포함된 지시와 관측 이력으로 기억 조회·탐색 행동을 선택한다.

## Evaluation Scope and Claim Boundary

저자는 STARBench와 Tiago 실기에서 비교했다. 프로젝트의 360개 과제는 3개 아파트와 3개 과제군을 포함한다.

근거: [공식 paper/abstract](https://ieeexplore.ieee.org/document/11696368/) · [저자 project/code](https://amrl.cs.utexas.edu/STAR/) · [공식 code](https://github.com/ut-amrl/STARBench). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

기억 조회와 로봇의 실제 이동을 구별하는 공개 탐색 프로토콜로 참조한다.

## Verification Boundary

실물과 시뮬레이션의 과제 수, 기억 관측 주체, 대상 이동 빈도을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
