# Latent Theory of Mind: A Decentralized Diffusion Architecture for Cooperative Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.

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
- Source audit: 2026-11-05: 공식 proceedings abstract와 저자 project/code README. abstract 기반 — 본문 수동 확인 필요. Native 실행 0; 사용자 읽기 UNREAD. 공개 code/관측 설정 표기만 확인했으며 전체 source·데이터 검증 아님. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

LatentToM은 두 로봇이 각자 관찰한 장면에서 공유 표현과 각자의 표현을 학습해 분산된 확산 정책으로 협동 조작하게 한다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/he25a/he25a.pdf#page=1)

## Core Idea and Contribution

- 공통 표현을 중앙 훈련에서 정렬하고 각 로봇이 그 표현으로 상대의 개별 표현을 복원하게 하며 실행할 때의 통신은 선택 사항으로 둔다. [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/he25a/he25a.pdf#page=3) · [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/he25a/he25a.pdf#page=4) · [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/he25a/he25a.pdf#page=5)
- 두 실제 조작기의 협동 작업에서 중앙·분산 정책과 비교하고 상대의 일시적인 지연 또는 작동 중단에 대한 대응을 시험했다. [PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/he25a/he25a.pdf#page=6) · [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/he25a/he25a.pdf#page=7)

## Scope and Limitation

독립 학습한 생소한 파트너와의 cross-play 성능은 이번 abstract로 확정할 수 없다. 다수 로봇 확장 가능성과 실제 두 로봇 평가는 다르다.

## Why This Paper Is Here — Researcher Interpretation

CROSSPLAY의 decentralized 협력·상대 행동 모델링은 이미 존재함을 보여 주는 CoRL 직접 선행.

입력·행동은 [method](./03_method.md), 실제 평가 범위는 [evaluation](./04_evaluation.md)을 따른다. 자동 노트는 사용자의 읽기 완료 기록이 아니다.

근거: [확인한 원문](https://proceedings.mlr.press/v305/he25a.html), 공식 proceedings abstract.
