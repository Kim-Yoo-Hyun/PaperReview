# PRIMT: Preference-based Reinforcement Learning with Multimodal Feedback and Trajectory Synthesis from Foundation Models

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / NeurIPS
- Authors: Ruiqi Wang, Dezhong Zhao, Ziqin Yuan, Tianyu Shao, Guohua Chen, Dominic Kao, Sungeun Hong, Byung-Cheol Min
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: preference-learning, multimodal-feedback, hindsight-counterfactual-trajectories, reward-learning
- Aliases: PRIMT
- Official paper: https://proceedings.neurips.cc/paper_files/paper/2025/hash/e0d760e4495abf701b97c8acda111372-Abstract-Conference.html
- Venue verification: https://proceedings.neurips.cc/paper_files/paper/2025/hash/e0d760e4495abf701b97c8acda111372-Abstract-Conference.html
- Code/Project: https://primt25.github.io/
- Code: https://github.com/primt25/PRIMT
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

PRIMT는 사람의 반복적인 선호 판단을 줄이기 위해 언어 모델과 시각언어 모델의 피드백으로 로봇 행동의 보상을 학습한다. [PDF 1쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/e0d760e4495abf701b97c8acda111372-Paper-Conference.pdf#page=1)

## Core Idea and Contribution

- 두 모델의 평가를 결합하고 초기에 비교할 궤적을 합성하며, 이후에는 궤적을 반사실적으로 바꿔 어떤 동작이 선호를 결정했는지 학습한다. [PDF 4쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/e0d760e4495abf701b97c8acda111372-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/e0d760e4495abf701b97c8acda111372-Paper-Conference.pdf#page=5) · [PDF 6쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/e0d760e4495abf701b97c8acda111372-Paper-Conference.pdf#page=6)
- 시뮬레이션 보행 두 과제와 조작 여섯 과제에서 기초 모델 기반·규칙 기반 평가와 비교하고 궤적 합성의 영향을 조사했다. [PDF 7쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/e0d760e4495abf701b97c8acda111372-Paper-Conference.pdf#page=7) · [PDF 8쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/e0d760e4495abf701b97c8acda111372-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/e0d760e4495abf701b97c8acda111372-Paper-Conference.pdf#page=9)

## Observation–State–Action Interface

행동 trajectory → multimodal preference/reward → RL; 합성 데이터가 학습 감독에 들어간다.

## Evaluation Scope and Claim Boundary

Locomotion과 manipulation benchmark에서 foundation-model 및 scripted 비교를 보고한다.

근거: [공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2025/hash/e0d760e4495abf701b97c8acda111372-Abstract-Conference.html) · [저자 project/code](https://primt25.github.io/) · [공식 code](https://github.com/primt25/PRIMT). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

Hindsight 재사용과 foundation reward 결합이 이미 연구되었음을 보여 주는 비교 선행이다.

## Verification Boundary

합성 trajectory 유효성, reward 누출, foundation model 호출 비용을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 공개 자료

- 코드 · PRIMT 선호 보상 학습 · primt_reward_model.py [배포 파일](https://raw.githubusercontent.com/primt25/PRIMT/a88ab92d7570ab67c0690a549b836a9501c64384/primt_reward_model.py)
