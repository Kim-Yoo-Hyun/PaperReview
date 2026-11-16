# TacCoRL: Integrating Tactile Feedback into VLA via Simulation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, tactile, sim-to-real, reinforcement-learning
- Aliases: TacCoRL
- Official paper: https://arxiv.org/abs/2606.11743
- Venue verification: https://arxiv.org/abs/2606.11743
- Code/Project: https://tac-corl.github.io/
- Code: not_identified
- Source audit: 2026-11-09: official abstract/project 및 metadata 확인. 저자 project는 CoRL 2026을 표기하지만 공식 proceedings/forum은 이번 검색에서 확인하지 못했다. arXiv 유지. 새 5-note는 abstract 기반이며 전체 본문/실행/사용자 정독을 뜻하지 않는다.

## Problem and Importance

시각 VLA가 놓치는 접촉 상태와 시연에 드문 실패 근방 행동을 학습한다.

## Core Idea and Contribution

촉각 VLA를 sim-real co-training으로 초기화하고 simulation RL과 실환경 supervised anchor로 개선한다.

## Observation–State–Action Interface

영상·언어·촉각 → VLA 행동; 배포 시 privileged simulation state를 쓰지 않는다고 보고한다.

## Evaluation Scope and Claim Boundary

실제 양팔 접촉 과제로 전이를 평가한다. 실제 로봇 online RL을 사용한 결과와 구별한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2606.11743) · [저자 project/code](https://tac-corl.github.io/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

촉각 추가와 단일 VLA RL 자체가 이미 선행임을 확인할 직접 비교다.

## Verification Boundary

촉각 합성 정합성, real anchor 비용, 물리 변화별 분할을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
