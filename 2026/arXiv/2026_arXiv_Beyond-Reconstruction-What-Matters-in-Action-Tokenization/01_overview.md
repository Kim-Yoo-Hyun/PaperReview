# Beyond Reconstruction: What Matters in Action Tokenization for Robot Policies?

> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

- Year/Venue: 2026 / arXiv
- Authors: Haoran Chen, Jingtian Ji, Samuel Wheeler, Kaylene Caswell Stocking, Matthew Walter
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, action-tokenization, autoregressive-policy, control-horizon
- Official paper: https://arxiv.org/abs/2610.09170
- Venue verification: main-conference acceptance unverified; preprint으로 등록
- Code/Project: https://ripl.github.io/action-tokenization-web/proact/
- Code: not_released
- Source audit: 2026-11-05: §1, §4, §6, Appendix B.2/C.3. 지정 본문 절만 확인; 전체 정독·수식 검증 아님. Venue와 읽은 preprint version을 구별. Native 실행 0; 사용자 읽기 UNREAD. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

ProAct는 행동을 토큰으로 바꿀 때 복원 오차와 함께 정책의 토큰 예측 가능성 및 낯선 토큰 조합의 복호화 안정성을 고려한다. [PDF 1쪽](https://arxiv.org/pdf/2610.09170v1#page=1)

## Core Idea and Contribution

- 행동 데이터만으로 토큰 균형 정규화와 토큰 교란을 학습해 다음 토큰의 예측 가능성과 잘못 예측한 토큰의 복호화 안정성을 개선한다. [PDF 5쪽](https://arxiv.org/pdf/2610.09170v1#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2610.09170v1#page=6)
- 여러 시뮬레이션 벤치마크와 실물 UR5에서 토크나이저를 바꿔 동작 재현 오차와 실제 과제 성공이 얼마나 달라지는지 비교했다. [PDF 7쪽](https://arxiv.org/pdf/2610.09170v1#page=7) · [PDF 9쪽](https://arxiv.org/pdf/2610.09170v1#page=9)

## Scope and Limitation

일반 reconstruction/control 불일치와 horizon 효과는 이미 다룬다. Code soon으로 표기되어 실행 검증되지 않았다. 저자 NeurIPS 표기는 exact 공식 listing을 확인하지 못해 arXiv 유지.

## Why This Paper Is Here — Researcher Interpretation

CODEC1의 broad motivation과 prefix/replanning confound를 가장 직접적으로 제한하는 선행.

입력·행동은 [method](./03_method.md), 실제 평가 범위는 [evaluation](./04_evaluation.md)을 따른다. 자동 노트는 사용자의 읽기 완료 기록이 아니다.

근거: [확인한 원문](https://arxiv.org/pdf/2610.09170v1), §1, §4, §6, Appendix B.2/C.3.
