# A Generalist Pair-wise Progress Critic Model for Vision-Language-Action Robots

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ICML
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, progress-critic, dense-reward, real-robot-RL
- Aliases: VLAC, A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning
- Official paper: https://proceedings.mlr.press/v306/zhang26if.html
- Venue verification: https://proceedings.mlr.press/v306/zhang26if.html
- Code/Project: https://github.com/InternRobotics/VLAC
- Code: https://github.com/InternRobotics/VLAC
- Source audit: 2026-11-06: 공식 proceedings metadata·abstract 확인. 이 5개 노트는 abstract 범위이며 최종 본문 정독/실행 완료가 아니다. 주제 dossier의 지정 preprint/code 읽기와 구별한다.

## Problem and Importance

실제 로봇에서 행동 생성과 과업 진행 판단을 함께 다루려는 연구다.

## Core Idea and Contribution

단일 autoregressive 구조로 행동과 두 시점 사이의 진행 차이를 예측하고, 진행 판단을 RL 보상에 사용한다.

## Observation–State–Action Interface

시각·언어 조건의 행동 출력과 관측 쌍에 대한 progress 출력.

## Evaluation Scope and Claim Boundary

공식 abstract는 실제 로봇 RL 평가를 보고한다. 정확한 trial·baseline·수치는 최종 본문 확인 필요.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v306/zhang26if.html) · [저자 project/code](https://github.com/InternRobotics/VLAC). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

단일 VLA의 행동/가치/보상을 구분할 직접 선행이다. U2의 구조 통합 주장을 제한하며 U1의 state-value와 다른 target을 제공하므로 NEXT에 추가한다.

## Verification Boundary

최종 ICML 모델 크기·동일 weight 여부·reward/done model 및 PPO value의 분리를 확인해야 한다. 2025 preprint 설정을 최종본에 전사하지 않는다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
