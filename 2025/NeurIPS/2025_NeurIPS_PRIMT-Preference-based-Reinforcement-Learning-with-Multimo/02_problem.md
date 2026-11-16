# PRIMT: Preference-based Reinforcement Learning with Multimodal Feedback and Trajectory Synthesis from Foundation Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Foundation model 선호 피드백은 판단 모호성과 credit assignment 문제를 함께 가진다.

## Bottleneck and Changed Formulation

VLM·LLM 피드백 결합, foresight trajectory 생성과 hindsight augmentation·causal auxiliary loss를 사용한다.

## System and Robotics Loop

행동 trajectory → multimodal preference/reward → RL; 합성 데이터가 학습 감독에 들어간다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

합성 trajectory 유효성, reward 누출, foundation model 호출 비용.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Locomotion과 manipulation benchmark에서 foundation-model 및 scripted 비교를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2025/hash/e0d760e4495abf701b97c8acda111372-Abstract-Conference.html) · [저자 project/code](https://primt25.github.io/) · [공식 code](https://github.com/primt25/PRIMT). Exact objective, constraints, success definition은 본문 수동 확인 필요.
