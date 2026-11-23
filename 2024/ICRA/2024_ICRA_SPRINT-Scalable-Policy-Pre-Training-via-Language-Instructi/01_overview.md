# SPRINT: Scalable Policy Pre-Training via Language Instruction Relabeling

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2024 / ICRA
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
- Source audit: 2026-11-07: 공식 metadata/abstract·저자 project/README 확인. IEEE-deposited Crossref metadata로 ICRA 2024 title/DOI 확인; arXiv abstract·저자 README 검토. 저장소 heading의 Semantic은 alias로만 보존한다. 사용자 reading status UNREAD 유지. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

SPRINT는 적은 수의 지시와 기존 오프라인 궤적으로 더 다양한 언어 조건부 조작 기술을 사전학습한다. [PDF 1쪽](https://arxiv.org/pdf/2306.11886v3#page=1)

## Core Idea and Contribution

- 언어 모델로 지시를 다시 붙이고 오프라인 강화학습으로 서로 다른 궤적의 기술을 연결해 사전학습 과제를 늘린다. [PDF 3쪽](https://arxiv.org/pdf/2306.11886v3#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2306.11886v3#page=4)
- 가정 환경 시뮬레이터와 실제 주방 조작에서 새 장기 과제에 필요한 후속 학습량과 각 사전학습 요소의 효과를 비교했다. [PDF 5쪽](https://arxiv.org/pdf/2306.11886v3#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2306.11886v3#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2306.11886v3#page=7)

## Observation–State–Action Interface

기존 trajectory·언어 지시 → 재라벨/연결된 기술 자료 → 정책 사전학습 → 새 과제 적응. 단일 VLA online RL이라고 가정하지 않는다.

## Evaluation Scope and Claim Boundary

저자 abstract는 가정용 시뮬레이터와 실제 로봇 주방 조작의 장기 과제 적응을 보고한다. 공개 저장소는 ALFRED-RL simulation 경로를 안내한다.

근거: [공식 paper/abstract](https://doi.org/10.1109/ICRA57147.2024.10610606) · [저자 project/code](https://clvrai.github.io/sprint/) · [공식 code](https://github.com/clvrai/sprint). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

언어 재라벨·기술 조합을 최근 VLA RL만의 신규성으로 오인하지 않게 하는 offline 학습 선행이다.

## Verification Boundary

cross-trajectory 연결의 유효성, downstream adaptation 예산, 시뮬레이터와 실로봇의 서로 다른 행동 interface, code의 실제 공개 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
