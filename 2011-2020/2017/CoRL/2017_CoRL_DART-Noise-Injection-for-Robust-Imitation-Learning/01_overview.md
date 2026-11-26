# DART: Noise Injection for Robust Imitation Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2017 / CoRL
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
- Source audit: 2026-11-12: 공식 publication/초록 또는 저자 source 확인. 공식 CoRL abstract 및 저자 project/code 공개 확인. 공개 repository의 simulation 구현과 실제 HSR 재현 경로는 구별한다. 초록·지정 project 범위이며 전체 정독·코드 실행·사용자 reading 완료를 뜻하지 않는다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

DART는 전문가가 시연할 때 학습 정책이 낼 법한 오차를 주입해 그 오차에서 복구하는 행동을 훈련 자료에 포함한다. [PDF 1쪽](https://proceedings.mlr.press/v78/laskey17a/laskey17a.pdf#page=1)

## Core Idea and Contribution

- 현재 모방 정책과 전문가 사이의 행동 오차에 맞춰 시연 중 주입할 잡음 분포를 조정하는 방법을 제시했다. [PDF 4쪽](https://proceedings.mlr.press/v78/laskey17a/laskey17a.pdf#page=4) · [PDF 5쪽](https://proceedings.mlr.press/v78/laskey17a/laskey17a.pdf#page=5)
- MuJoCo 보행 과제의 알고리즘 전문가와 Toyota HSR의 혼잡한 장면 파지에서 일반 행동 복제 및 DAgger와 비교했다. [PDF 7쪽](https://proceedings.mlr.press/v78/laskey17a/laskey17a.pdf#page=7) · [PDF 8쪽](https://proceedings.mlr.press/v78/laskey17a/laskey17a.pdf#page=8) · [PDF 9쪽](https://proceedings.mlr.press/v78/laskey17a/laskey17a.pdf#page=9)

## Observation–State–Action Interface

교란된 시연 상황 → 전문가 복구 행동 → offline imitation 정책.

## Evaluation Scope and Claim Boundary

MuJoCo locomotion과 실제 Toyota HSR의 clutter grasping을 평가한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v78/laskey17a.html) · [저자 project/code](https://berkeleyautomation.github.io/DART/) · [공식 code](https://github.com/BerkeleyAutomation/DART). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

복구 성공을 RL 고유 이득으로 해석하기 전 넘어야 할 강한 데이터 수집·모방 대안이다.

## Verification Boundary

본문에서 확인할 항목: noise 분포·전문가 회복 능력·개입 비용·train-test 교란. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 공개 자료

- 코드 · DART의 모방학습 실험 · experiments/test_dart.py [배포 파일](https://raw.githubusercontent.com/BerkeleyAutomation/DART/c6b2a860f393d274da20c0df8be06154b99070f8/experiments/test_dart.py)
- 가중치 · DART가 시연자로 사용하는 Hopper 전문가 정책 · experts/Hopper-v1.pkl [배포 파일](https://raw.githubusercontent.com/BerkeleyAutomation/DART/c6b2a860f393d274da20c0df8be06154b99070f8/experts/Hopper-v1.pkl)
