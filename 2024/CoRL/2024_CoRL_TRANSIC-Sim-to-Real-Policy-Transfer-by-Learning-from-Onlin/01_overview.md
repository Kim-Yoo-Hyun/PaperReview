# TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Yunfan Jiang, Chen Wang, Ruohan Zhang, Jiajun Wu, Li Fei-Fei
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, sim-to-real, human-in-the-loop, residual-policy
- Aliases: TRANSIC
- Official paper: https://proceedings.mlr.press/v270/jiang25a.html
- Venue verification: https://proceedings.mlr.press/v270/jiang25a.html
- Conference edition: 2024 · https://proceedings.mlr.press/v270/
- Code/Project: https://transic-robot.github.io/
- Code: https://github.com/transic-robot/transic
- Source audit: 2026-10-25 공식 abstract/서지정보 및 명시된 저자 링크 확인. 이번 노트는 abstract 기반이며 본문 전체·코드 실행·payload는 미검증이다. CoRL 개최 2024, PMLR 출판 2025.

## Problem and Importance

Simulation 정책은 모델에 없는 실환경 차이를 모두 다루기 어렵다.

## Core Idea and Contribution

사람의 online correction으로 residual policy를 학습해 simulation 정책과 결합한다.

## Observation–State–Action Interface

point-cloud 기반 base policy + 인간 correction으로 학습한 residual → 실행 action.

## Evaluation Scope and Claim Boundary

가구 조립 등 실로봇 접촉 조작의 sim-to-real 전이를 보고한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v270/jiang25a.html) · [저자 project/code](https://transic-robot.github.io/) · [공식 code](https://github.com/transic-robot/transic). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

새 RL/VLA 적응 기여를 주장하기 전에 인간 개입·residual 학습으로 설명되는 이득을 대조한다.

## Verification Boundary

개입 시점/시간 비용, residual 제어 권한, correction과 평가 분할을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
