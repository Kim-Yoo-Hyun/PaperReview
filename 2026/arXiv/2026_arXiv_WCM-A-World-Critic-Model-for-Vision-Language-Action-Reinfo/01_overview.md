# WCM: A World Critic Model for Vision-Language-Action Reinforcement Learning

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Authors: Senyu Fei, Xiaopeng Yu, Siyin Wang, Xianzhong Zhao, Jingjing Gong, Xipeng Qiu
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, reinforcement-learning, critic, world-model, partial-observability
- Aliases: WCM
- Official paper: https://arxiv.org/abs/2607.29613
- Venue verification: https://arxiv.org/abs/2607.29613
- Code/Project: https://github.com/sylvestf/WCM
- Code: https://github.com/sylvestf/WCM
- Source audit: 2026-11-12: 공식 publication/초록 또는 저자 source 확인. arXiv v1와 공식 repository의 configs/scripts/world_critic 존재 확인. 학회 acceptance 및 실제 구현 재현은 확인하지 않았다. 초록·지정 project 범위이며 전체 정독·코드 실행·사용자 reading 완료를 뜻하지 않는다.

## Problem and Importance

한 장면이나 scalar-return만으로 학습한 critic이 로봇 제어의 시간 구조를 놓칠 수 있다.

## Core Idea and Contribution

LeJEPA 기반 critic이 미래 latent state와 value를 함께 학습하여 시간 정보를 표현하도록 한다.

## Observation–State–Action Interface

관측 이력 → future-latent/value 공동 critic → on/off-policy VLA RL.

## Evaluation Scope and Claim Boundary

여러 VLA backbone과 simulation benchmark·실물 조작에서 평가한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2607.29613) · [저자 project/code](https://github.com/sylvestf/WCM). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

공유 표현·가치 공동 학습 후보의 직접 경쟁 선행이므로 단순 world-model 보조 loss를 신규 기여로 재제안하지 않게 한다.

## Verification Boundary

본문에서 확인할 항목: critic/actor 가중치 공유·history 접근·latent target·on/off-policy 차이. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
