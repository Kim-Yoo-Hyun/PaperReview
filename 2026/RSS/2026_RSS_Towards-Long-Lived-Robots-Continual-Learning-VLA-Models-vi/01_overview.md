# Towards Long-Lived Robots: Continual Learning VLA Models via Reinforcement Fine-Tuning

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, continual-learning, reward-modeling, action-chunking
- Aliases: LifeLong-RFT
- Official paper: https://roboticsproceedings.org/rss22/p086.html
- Venue verification: https://roboticsproceedings.org/rss22/p086.html
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지.

## Problem and Importance

VLA의 순차적 과제 적응에서 SFT 데이터 부담과 기존 능력 보존이 문제다.

## Core Idea and Contribution

행동 chunk의 이산 일치·연속 궤적 정렬·출력 형식 보상으로 reinforcement fine-tuning한다.

## Observation–State–Action Interface

관측·지시 → 행동 chunk; 참조 행동과의 일치도가 학습 보상.

## Evaluation Scope and Claim Boundary

SimplerEnv·LIBERO 및 실제 조작, LIBERO continual learning을 보고한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p086.html). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

환경 return 최적화와 참조 행동 기반 RLVR을 구별하기 위한 직접 비교다.

## Verification Boundary

참조 궤적 의존성, rehearsal 여부, 순차 task order, 보상별 효과을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
