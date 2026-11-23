# EvoVLA: Self-evolving Vision-Language-Action Model

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ECCV
- Authors: Zeting Liu, Zida Yang, Zeyu Zhang, Hao Tang
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, reward-hacking, reinforcement-learning, long-horizon
- Aliases: EvoVLA
- Official paper: https://link.springer.com/chapter/10.1007/978-3-032-37023-5_14
- Venue verification: https://link.springer.com/chapter/10.1007/978-3-032-37023-5_14
- Code/Project: https://aigeeksgroup.github.io/EvoVLA/
- Code: https://github.com/AIGeeksGroup/EvoVLA
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

EvoVLA는 긴 조작의 중간 단계에서 겉모습만 보고 진척을 잘못 인정하는 문제를 줄이도록 보상과 탐색을 설계한다. [PDF 1쪽](https://arxiv.org/pdf/2511.16166v1#page=1)

## Core Idea and Contribution

- 달성하지 않은 단계를 성공처럼 보이게 하는 반례로 보상 모델을 학습하고 물체와 그리퍼의 상대 자세로 탐색을 유도하며 과거 관측을 선택해 이용한다. [PDF 3쪽](https://arxiv.org/pdf/2511.16166v1#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2511.16166v1#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2511.16166v1#page=5)
- Discoverse-L의 세 다단계 과제와 실물 조작에서 정책을 평가하고 단계 보상·자세 기반 탐색·기억을 제거한 조건의 차이를 측정했다. [PDF 6쪽](https://arxiv.org/pdf/2511.16166v1#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2511.16166v1#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2511.16166v1#page=8)

## Observation–State–Action Interface

관측·지시 → VLA rollout; stage reward·pose exploration·memory가 RL 후학습을 지원한다.

## Evaluation Scope and Claim Boundary

Discoverse-L 장기 조작과 실제 로봇의 성공·stage hallucination을 평가한다.

근거: [공식 paper/abstract](https://link.springer.com/chapter/10.1007/978-3-032-37023-5_14) · [저자 project/code](https://aigeeksgroup.github.io/EvoVLA/) · [공식 code](https://github.com/AIGeeksGroup/EvoVLA). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

VLA+RL 보상 개선에서 이미 다룬 near-miss 구분과 실제 물리 완료의 선행이다.

## Verification Boundary

pose·stage annotation의 특권 정보, hard-negative 생성 비용, 세 모듈별 기여을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
