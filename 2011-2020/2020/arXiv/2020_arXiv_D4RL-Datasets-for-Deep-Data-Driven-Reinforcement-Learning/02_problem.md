# D4RL: Datasets for Deep Data-Driven Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Problem and Bottleneck

온라인 학습용 benchmark만으로는 offline 데이터의 이질성과 실패를 평가하기 어렵다.

## Formulation and Robotics Loop

고정 transition dataset → offline 정책 학습 → 환경별 평가.

사람·규칙 controller·정책 혼합·멀티태스크 데이터를 포함하는 offline RL benchmark와 평가 프로토콜을 제시한다.

## Assumptions to Verify

dataset version·terminal/timeout·normalized score·현행 API와 원본 데이터 호환.

위 항목은 연구자의 확인 질문이며 논문이 명시한 가정·실패로 확정한 것이 아니다.

## Prior Work and Why It Matters

Batch RL 평가 → D4RL → CQL/IQL·OGBench와 robot data 조건 비교.

CQL·IQL·Cal-QL의 데이터 조건과 결과를 읽기 위한 표준 benchmark의 누락을 보완한다.

## Evidence Boundary

[공식 paper/abstract](https://arxiv.org/abs/2004.07219). arXiv v4와 공식 유지 repository 확인. 확인되지 않은 conference venue를 부여하지 않으며 현행 라이브러리의 실행 호환성을 보장하지 않는다.
