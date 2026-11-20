# SPRINT: Scalable Policy Pre-Training via Language Instruction Relabeling

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Jesse Zhang, Karl Pertsch, Jiahui Zhang, Joseph J. Lim
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: offline-RL, language-relabeling, skill-chaining, long-horizon
- Aliases: SPRINT, SPRINT: Scalable Semantic Policy Pre-training via Language Instruction Relabeling
- Official paper: https://api.crossref.org/works/10.1109/ICRA57147.2024.10610606
- Venue verification: https://api.crossref.org/works/10.1109/ICRA57147.2024.10610606
- Code/Project: https://clvrai.github.io/sprint/
- Code: https://github.com/clvrai/sprint
- Source audit: 2026-11-07: 공식 metadata/abstract·저자 project/README 확인. IEEE-deposited Crossref metadata로 ICRA 2024 title/DOI 확인; arXiv abstract·저자 README 검토. 저장소 heading의 Semantic은 alias로만 보존한다. 사용자 reading status UNREAD 유지.

## Problem and Importance

다양한 언어 조건 기술을 사전학습하려면 사람이 많은 과제 지시를 작성해야 한다.

## Core Idea and Contribution

LLM을 이용한 지시 재라벨과 서로 다른 궤적의 기술 연결을 offline RL 사전학습에 사용한다.

## Observation–State–Action Interface

기존 trajectory·언어 지시 → 재라벨/연결된 기술 자료 → 정책 사전학습 → 새 과제 적응. 단일 VLA online RL이라고 가정하지 않는다.

## Evaluation Scope and Claim Boundary

저자 abstract는 가정용 시뮬레이터와 실제 로봇 주방 조작의 장기 과제 적응을 보고한다. 공개 저장소는 ALFRED-RL simulation 경로를 안내한다.

근거: [공식 paper/abstract](https://doi.org/10.1109/ICRA57147.2024.10610606) · [저자 project/code](https://clvrai.github.io/sprint/) · [공식 code](https://github.com/clvrai/sprint). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

언어 재라벨·기술 조합을 최근 VLA RL만의 신규성으로 오인하지 않게 하는 offline 학습 선행이다.

## Verification Boundary

cross-trajectory 연결의 유효성, downstream adaptation 예산, 시뮬레이터와 실로봇의 서로 다른 행동 interface, code의 실제 공개 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
