# DART: Noise Injection for Robust Imitation Learning

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Michael Laskey, Jonathan Lee, Roy Fox, Anca Dragan, Ken Goldberg
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: imitation-learning, covariate-shift, recovery, noise-injection
- Aliases: DART, Disturbances for Augmenting Robot Trajectories
- Official paper: https://proceedings.mlr.press/v78/laskey17a.html
- Venue verification: https://proceedings.mlr.press/v78/laskey17a.html
- Code/Project: https://berkeleyautomation.github.io/DART/
- Code: https://github.com/BerkeleyAutomation/DART
- Source audit: 2026-11-12: 공식 publication/초록 또는 저자 source 확인. 공식 CoRL abstract 및 저자 project/code 공개 확인. 공개 repository의 simulation 구현과 실제 HSR 재현 경로는 구별한다. 초록·지정 project 범위이며 전체 정독·코드 실행·사용자 reading 완료를 뜻하지 않는다.

## Problem and Importance

시연 분포를 벗어난 BC 정책의 오류 누적과 사람이 제공하는 corrective data 비용을 다룬다.

## Core Idea and Contribution

전문가가 시연할 때 noise를 주입하고 학습 정책의 오류에 맞춰 noise 수준을 조절한다.

## Observation–State–Action Interface

교란된 시연 상황 → 전문가 복구 행동 → offline imitation 정책.

## Evaluation Scope and Claim Boundary

MuJoCo locomotion과 실제 Toyota HSR의 clutter grasping을 평가한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v78/laskey17a.html) · [저자 project/code](https://berkeleyautomation.github.io/DART/) · [공식 code](https://github.com/BerkeleyAutomation/DART). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

복구 성공을 RL 고유 이득으로 해석하기 전 넘어야 할 강한 데이터 수집·모방 대안이다.

## Verification Boundary

본문에서 확인할 항목: noise 분포·전문가 회복 능력·개입 비용·train-test 교란. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
