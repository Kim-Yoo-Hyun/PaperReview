# Difference-Aware Retrieval Policies for Imitation Learning

> Evidence maturity: `FULL_TEXT_CHECKED`. 요약과 기여를 아래 쪽수에서 확인했다.

- Year/Venue: 2026 / ICLR
- Authors: Quinn Pfeifer, Ethan Pronovost, Paarth Shah, Khimya Khetarpal, Siddhartha Srinivasa, Abhishek Gupta
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: Robotics, evaluation, retrieval, imitation-learning
- Aliases:
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/8c2ecd140ebe227a531edc9a0c3b69d4-Abstract-Conference.html
- Venue verification: https://proceedings.iclr.cc/paper_files/paper/2026/hash/8c2ecd140ebe227a531edc9a0c3b69d4-Abstract-Conference.html
- Code/Project: https://weirdlabuw.github.io/darp-site/
- Code: https://github.com/WEIRDLabUW/darp
- Full-text retrieval: https://proceedings.iclr.cc/paper_files/paper/2026/file/8c2ecd140ebe227a531edc9a0c3b69d4-Paper-Conference.pdf
- Source audit: 2026-11-24에 요약과 핵심 기여 두 개를 원문과 대조했다.

## Problem and Importance

DARP는 모방 정책이 낯선 상태를 만났을 때 전문가 자료에서 가까운 상태·행동을 검색하고 현재 상태와의 차이를 이용해 행동을 예측한다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/8c2ecd140ebe227a531edc9a0c3b69d4-Paper-Conference.pdf#page=1) · [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/8c2ecd140ebe227a531edc9a0c3b69d4-Paper-Conference.pdf#page=4)

## Core Idea and Contribution

- 전문가 상태에서 질의 상태를 뺀 벡터와 해당 전문가 행동을 이웃별 입력으로 사용해 예측기를 학습한다. [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/8c2ecd140ebe227a531edc9a0c3b69d4-Paper-Conference.pdf#page=6) · [PDF 7쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/8c2ecd140ebe227a531edc9a0c3b69d4-Paper-Conference.pdf#page=7)
- 연속제어와 RoboCasa 조작에서 행동 복제 및 검색 기준선과 비교하고, 시각 특징 입력과 차이 벡터 제거 조건을 따로 평가했다. [PDF 8쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/8c2ecd140ebe227a531edc9a0c3b69d4-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/8c2ecd140ebe227a531edc9a0c3b69d4-Paper-Conference.pdf#page=9)

## Observation–State–Action Interface

Query state·이웃 시연·상대 벡터 → action prediction.

## Evaluation Scope and Claim Boundary

Continuous control과 manipulation, 고차원 시각 표현에서 BC와 비교한다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/8c2ecd140ebe227a531edc9a0c3b69d4-Abstract-Conference.html) · [저자 project/code](https://weirdlabuw.github.io/darp-site/) · [공식 code](https://github.com/WEIRDLabUW/darp).

## 검색 태그 근거

DARP는 행동 예측 시 질의 상태와 가까운 시연 상태·행동을 검색한다. 이웃과 질의의 차이로 후보 행동을 만든 뒤 통합하며, 연속 제어·조작에서 행동 복제와 비교한다. [원문 7쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/8c2ecd140ebe227a531edc9a0c3b69d4-Paper-Conference.pdf#page=7) · [원문 9쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/8c2ecd140ebe227a531edc9a0c3b69d4-Paper-Conference.pdf#page=9)

## Why This Paper Is Here — Researcher Interpretation

학습 전 subset 선택과 실행 중 retrieval의 효과를 분리할 직접 대안이다.

## Verification Boundary

이웃 수, history 사용, retrieval 지연과 rollout split을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
