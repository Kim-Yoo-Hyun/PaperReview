# EvoVLA: Self-evolving Vision-Language-Action Model

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
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
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지.

## Problem and Importance

Frozen VLM reward가 그럴듯한 관측을 실제 단계 완료와 혼동할 수 있다.

## Core Idea and Contribution

Counterfactual hard negative 기반 stage reward, relative pose 탐색, 선택적 장기 memory를 결합한다.

## Observation–State–Action Interface

관측·지시 → VLA rollout; stage reward·pose exploration·memory가 RL 후학습을 지원한다.

## Evaluation Scope and Claim Boundary

Discoverse-L 장기 조작과 실제 로봇의 성공·stage hallucination을 평가한다.

근거: [공식 paper/abstract](https://link.springer.com/chapter/10.1007/978-3-032-37023-5_14) · [저자 project/code](https://aigeeksgroup.github.io/EvoVLA/) · [공식 code](https://github.com/AIGeeksGroup/EvoVLA). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

VLA+RL 보상 개선에서 이미 다룬 near-miss 구분과 실제 물리 완료의 선행이다.

## Verification Boundary

pose·stage annotation의 특권 정보, hard-negative 생성 비용, 세 모듈별 기여을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
