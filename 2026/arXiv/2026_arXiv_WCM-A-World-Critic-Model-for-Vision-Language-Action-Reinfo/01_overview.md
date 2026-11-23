# WCM: A World Critic Model for Vision-Language-Action Reinforcement Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
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
- Source audit: 2026-11-12: 공식 publication/초록 또는 저자 source 확인. arXiv v1와 공식 repository의 configs/scripts/world_critic 존재 확인. 학회 acceptance 및 실제 구현 재현은 확인하지 않았다. 초록·지정 project 범위이며 전체 정독·코드 실행·사용자 reading 완료를 뜻하지 않는다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

WCM은 부분적으로 관측되는 조작에서 단일 영상의 수익을 회귀하는 비평가에 미래 잠재 상태 예측을 더해 행동의 가치를 추정한다. [PDF 1쪽](https://arxiv.org/pdf/2607.29613v1#page=1)

## Core Idea and Contribution

- 경량 LeJEPA 모형이 관측 이력에서 미래 표현과 가치를 함께 학습하도록 구성해 온폴리시 및 오프폴리시 VLA 강화학습에 적용했다. [PDF 4쪽](https://arxiv.org/pdf/2607.29613v1#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2607.29613v1#page=5)
- 시뮬레이션의 분포 변화와 일곱 가지 실물 조작에서 기존 비평가와 비교하고 OpenVLA-OFT와 π0.5의 실물 오프폴리시 학습 결과를 보고했다. [PDF 8쪽](https://arxiv.org/pdf/2607.29613v1#page=8) · [PDF 9쪽](https://arxiv.org/pdf/2607.29613v1#page=9)

## Observation–State–Action Interface

관측 이력 → future-latent/value 공동 critic → on/off-policy VLA RL.

## Evaluation Scope and Claim Boundary

여러 VLA backbone과 simulation benchmark·실물 조작에서 평가한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2607.29613) · [저자 project/code](https://github.com/sylvestf/WCM). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

공유 표현·가치 공동 학습 후보의 직접 경쟁 선행이므로 단순 world-model 보조 loss를 신규 기여로 재제안하지 않게 한다.

## Verification Boundary

본문에서 확인할 항목: critic/actor 가중치 공유·history 접근·latent target·on/off-policy 차이. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
