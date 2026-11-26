# Enhancing Tactile-based Reinforcement Learning for Robotic Control

> Evidence maturity: `FULL_TEXT_CHECKED`. 요약과 기여를 아래 쪽수에서 확인했다.

- Year/Venue: 2025 / NeurIPS
- Authors: Elle Miller, Trevor McInroe, David Abel, Oisin Mac Aodha, Sethu Vijayakumar
- Category: Manipulation, Contact, and Dexterity
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: tactile-RL, binary-contact, self-supervised-learning, dexterity, Benchmark
- Aliases: RoTO, Robot Tactile Olympiad
- Official paper: https://proceedings.neurips.cc/paper_files/paper/2025/hash/bc09efb501c801ed92e181e26a885c2d-Abstract-Conference.html
- Venue verification: https://proceedings.neurips.cc/paper_files/paper/2025/hash/bc09efb501c801ed92e181e26a885c2d-Abstract-Conference.html
- Code/Project: https://elle-miller.github.io/tactile_rl/
- Code: https://github.com/elle-miller/roto
- Full-text retrieval: https://proceedings.neurips.cc/paper_files/paper/2025/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf
- Source audit: 2026-11-24에 요약과 핵심 기여 두 개를 원문과 대조했다. 평가 조건은 04_evaluation.md에 쪽수와 함께 기록했다.

## Problem and Importance

고유수용감각과 희소한 이진 접촉 신호만으로 조작을 학습할 때 어떤 자기지도 목표와 기억 구조가 촉각 활용을 돕는지 조사했다. [PDF 1쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf#page=1) · [PDF 4쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf#page=4)

## Core Idea and Contribution

- 촉각을 포함한 시퀀스의 재구성·예측 보조 목표를 도입하고 자기지도용 기억을 온폴리시 제어용 기억과 분리한 구조를 비교한다. [PDF 4쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf#page=5)
- Isaac Lab의 RoTO 조작 과제에서 촉각 유무와 보조 학습을 바꿔 보상과 공 튀기기·손안 회전의 물리 성과 지표를 비교했다. [PDF 6쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf#page=6) · [PDF 7쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf#page=7) · [PDF 9쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf#page=9)

## Observation–State–Action Interface

Binary contact·proprioception → 표현/memory → contact-rich control.

## Evaluation Scope and Claim Boundary

RoTO 실험은 Isaac Lab의 세 과제로 구성된다. 10초 동안 공을 88번 튀긴 수치와 보정구를 25번 회전시킨 수치는 시뮬레이션 에이전트의 최고 기록이다. [PDF 6쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf#page=6) · [PDF 9쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf#page=9)

근거: [공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2025/hash/bc09efb501c801ed92e181e26a885c2d-Abstract-Conference.html) · [저자 project/code](https://elle-miller.github.io/tactile_rl/) · [공식 code](https://github.com/elle-miller/roto).

## 검색 태그 근거

정책은 고유수용 상태와 접촉의 유무를 받는다. PPO에 접촉 복원·다음 상태 예측 등의 자기지도 목표를 더해 비교했다. Isaac Lab에서 Franka의 구 찾기와 Shadow Hand의 공 튀기기·두 공 돌리기를 평가했다. [원문 4쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf#page=4) · [원문 6쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf#page=6) · [원문 9쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf#page=9)

## Why This Paper Is Here — Researcher Interpretation

시각 VLA에 촉각을 넣기 전에 입력 유용성과 표현 학습을 분리할 진단 자원이다.

## Verification Boundary

센서 노이즈·빈도, sim contact의 현실성, 실물 센서 전이을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
