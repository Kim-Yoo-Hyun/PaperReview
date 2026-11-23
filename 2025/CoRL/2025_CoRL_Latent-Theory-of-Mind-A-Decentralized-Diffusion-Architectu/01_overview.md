# Latent Theory of Mind: A Decentralized Diffusion Architecture for Cooperative Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.

- Year/Venue: 2025 / CoRL
- Authors: Chengyang He, Gadiel Mark Sznaier Camps, Xu Liu, Mac Schwager, Guillaume Adrien Sartoretti
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: cooperative-manipulation, diffusion-policy, decentralized-control, partner-modeling
- Official paper: https://proceedings.mlr.press/v305/he25a.html
- Venue verification: https://proceedings.mlr.press/v305/he25a.html
- Code/Project: https://stanfordmsl.github.io/LatentToM/
- Code: https://github.com/StanfordMSL/LatentToM
- Source audit: 2026-11-05: 공식 proceedings abstract와 저자 project/code README. abstract 기반 — 본문 수동 확인 필요. Native 실행 0; 사용자 읽기 UNREAD. 공개 code/관측 설정 표기만 확인했으며 전체 source·데이터 검증 아님.

## Problem and Contribution

각 로봇이 자기 관측·계산만으로 공동 조작을 수행하는 문제.

Ego/consensus embedding과 상대 ego decoder를 학습한다. 중앙 학습의 sheaf-inspired 정렬 후 분산 실행하며 통신은 선택적이다.

## Scope and Limitation

독립 학습한 생소한 파트너와의 cross-play 성능은 이번 abstract로 확정할 수 없다. 다수 로봇 확장 가능성과 실제 두 로봇 평가는 다르다.

## Why This Paper Is Here — Researcher Interpretation

CROSSPLAY의 decentralized 협력·상대 행동 모델링은 이미 존재함을 보여 주는 CoRL 직접 선행.

입력·행동은 [method](./03_method.md), 실제 평가 범위는 [evaluation](./04_evaluation.md)을 따른다. 자동 노트는 사용자의 읽기 완료 기록이 아니다.

근거: [확인한 원문](https://proceedings.mlr.press/v305/he25a.html), 공식 proceedings abstract.
