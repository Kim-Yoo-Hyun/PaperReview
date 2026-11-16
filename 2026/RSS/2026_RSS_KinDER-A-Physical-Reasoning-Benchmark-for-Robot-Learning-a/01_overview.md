# KinDER: A Physical Reasoning Benchmark for Robot Learning and Planning

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Category: Planning and Long-Horizon Reasoning
- Primary track: Planning and control
- Tier: NEXT
- Tags: Benchmark, physical-reasoning, Planning, manipulation
- Aliases: KinDER
- Official paper: https://roboticsproceedings.org/rss22/p184.html
- Venue verification: https://roboticsproceedings.org/rss22/p184.html
- Code/Project: https://prpl-group.com/kinder-site/
- Code: https://github.com/Princeton-Robot-Planning-and-Learning/kindergarden
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인. RSS와 최신 arXiv의 baseline 수가 다르므로 원 논문·후속 버전을 구별한다. 본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지.

## Problem and Importance

지각·언어 오류와 기하·동역학 추론 실패가 통합 과제에서 섞인다.

## Core Idea and Contribution

물리 추론 난점을 분리한 절차적 환경과 skill·시연·평가 baseline을 제공한다.

## Observation–State–Action Interface

기하·동역학 제약 → 계획 또는 학습된 행동 → 물리적 결과.

## Evaluation Scope and Claim Boundary

다양한 planning·IL·RL baseline 및 mobile manipulator 대응 실험을 보고한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p184.html) · [저자 project/code](https://prpl-group.com/kinder-site/) · [공식 code](https://github.com/Princeton-Robot-Planning-and-Learning/kindergarden). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

VLA의 실패가 언어 표현 문제인지 물리적 의사결정 문제인지 진단할 자원이다.

## Verification Boundary

skill 호출 권한, 관측 특권, baseline별 compute, 절차적 split을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
