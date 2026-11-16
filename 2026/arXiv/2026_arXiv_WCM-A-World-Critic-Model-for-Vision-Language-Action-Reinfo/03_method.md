# WCM: A World Critic Model for Vision-Language-Action Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Method and Contribution

LeJEPA 기반 critic이 미래 latent state와 value를 함께 학습하여 시간 정보를 표현하도록 한다.

## Observation, State, and Action

관측 이력 → future-latent/value 공동 critic → on/off-policy VLA RL.

## Objective and Training / Inference Boundary

초록에서 확인한 학습 구성이다. 정확한 loss·gradient 경로·학습/추론 차이·controller 또는 memory 시간 단위는 본문 확인이 필요하다.

점검 항목: critic/actor 가중치 공유·history 접근·latent target·on/off-policy 차이.

## Method-Specific Comparison — Researcher Interpretation

History·모델 크기·데이터를 맞춰 value-only, future-latent 보조, actor-shared gradient를 분리한다.

이 비교는 제안이며 실행 결과나 논문의 ablation이 아니다.

## Evidence Boundary

[공식 paper/abstract](https://arxiv.org/abs/2607.29613). arXiv v1와 공식 repository의 configs/scripts/world_critic 존재 확인. 학회 acceptance 및 실제 구현 재현은 확인하지 않았다.
