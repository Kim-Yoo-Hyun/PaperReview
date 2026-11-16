# PRIMT: Preference-based Reinforcement Learning with Multimodal Feedback and Trajectory Synthesis from Foundation Models

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / NeurIPS
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: preference-learning, multimodal-feedback, hindsight, reward-learning
- Aliases: PRIMT
- Official paper: https://proceedings.neurips.cc/paper_files/paper/2025/hash/e0d760e4495abf701b97c8acda111372-Abstract-Conference.html
- Venue verification: https://proceedings.neurips.cc/paper_files/paper/2025/hash/e0d760e4495abf701b97c8acda111372-Abstract-Conference.html
- Code/Project: https://primt25.github.io/
- Code: https://github.com/primt25/PRIMT
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지.

## Problem and Importance

Foundation model 선호 피드백은 판단 모호성과 credit assignment 문제를 함께 가진다.

## Core Idea and Contribution

VLM·LLM 피드백 결합, foresight trajectory 생성과 hindsight augmentation·causal auxiliary loss를 사용한다.

## Observation–State–Action Interface

행동 trajectory → multimodal preference/reward → RL; 합성 데이터가 학습 감독에 들어간다.

## Evaluation Scope and Claim Boundary

Locomotion과 manipulation benchmark에서 foundation-model 및 scripted 비교를 보고한다.

근거: [공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2025/hash/e0d760e4495abf701b97c8acda111372-Abstract-Conference.html) · [저자 project/code](https://primt25.github.io/) · [공식 code](https://github.com/primt25/PRIMT). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

Hindsight 재사용과 foundation reward 결합이 이미 연구되었음을 보여 주는 비교 선행이다.

## Verification Boundary

합성 trajectory 유효성, reward 누출, foundation model 호출 비용을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
