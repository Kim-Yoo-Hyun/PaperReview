# Can Vision-Language-Action Models Learn from Real-World Data Continually without Forgetting?

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: continual-learning, replay, robot-learning
- Aliases: Real-world Continual VLA
- Official paper: https://arxiv.org/abs/2605.26820
- Venue verification: https://arxiv.org/abs/2605.26820
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다. arXiv v3를 확인했다.

## Problem and Importance

실제 로봇 VLA를 순차적으로 적응시킬 때 망각과 성능을 함께 평가한다.

## Core Idea and Contribution

실환경 continual 학습에서 replay와 데이터 정규화 등 기본 recipe를 비교한다.

## Observation–State–Action Interface

순차 task demonstration → VLA update → 기존/신규 task 실행.

## Evaluation Scope and Claim Boundary

단일 팔과 양팔 실환경 continual learning을 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2605.26820). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

E1의 실환경 단순 baseline과 compute-matched 비교에 필요한 연구다.

## Verification Boundary

v3 변경점, normalization 범위, joint training compute, trial 수을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
