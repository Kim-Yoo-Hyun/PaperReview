# WCM: A World Critic Model for Vision-Language-Action Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Problem and Bottleneck

한 장면이나 scalar-return만으로 학습한 critic이 로봇 제어의 시간 구조를 놓칠 수 있다.

## Formulation and Robotics Loop

관측 이력 → future-latent/value 공동 critic → on/off-policy VLA RL.

LeJEPA 기반 critic이 미래 latent state와 value를 함께 학습하여 시간 정보를 표현하도록 한다.

## Assumptions to Verify

critic/actor 가중치 공유·history 접근·latent target·on/off-policy 차이.

위 항목은 연구자의 확인 질문이며 논문이 명시한 가정·실패로 확정한 것이 아니다.

## Prior Work and Why It Matters

GAE·value representation → WCM ↔ VLAC·단일 VLA 공동 학습 후보.

공유 표현·가치 공동 학습 후보의 직접 경쟁 선행이므로 단순 world-model 보조 loss를 신규 기여로 재제안하지 않게 한다.

## Evidence Boundary

[공식 paper/abstract](https://arxiv.org/abs/2607.29613). arXiv v1와 공식 repository의 configs/scripts/world_critic 존재 확인. 학회 acceptance 및 실제 구현 재현은 확인하지 않았다.
