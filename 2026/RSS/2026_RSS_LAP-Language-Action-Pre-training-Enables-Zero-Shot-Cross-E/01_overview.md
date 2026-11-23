# LAP: Language-Action Pre-training Enables Zero-Shot Cross-Embodiment Transfer

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Authors: Lihan Zha, Asher James Hancock, Mingtong Zhang, Tenny Yin, Yixuan Huang, Dhruv Shah, Allen Z. Ren, Anirudha Majumdar
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, action-interface, cross-embodiment
- Aliases:
- Official paper: https://www.roboticsproceedings.org/rss22/p203.html
- Venue verification: https://www.roboticsproceedings.org/rss22/p203.html
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다.

## Problem and Importance

Embodiment별 action interface가 새 로봇 전이를 제한한다.

## Core Idea and Contribution

언어 action 표현으로 사전학습하고 새로운 embodiment로의 zero-shot 전이를 탐색한다.

## Observation–State–Action Interface

영상·지시 → 언어 action → 로봇별 실행.

## Evaluation Scope and Claim Boundary

새 embodiment 전이와 robot adaptation 평가를 보고한다.

근거: [공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p203.html). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

Cross-embodiment VLA interface를 비교할 최신 직접 선행이다.

## Verification Boundary

zero-shot 정의, robot-specific mapping, pretraining 중복을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
