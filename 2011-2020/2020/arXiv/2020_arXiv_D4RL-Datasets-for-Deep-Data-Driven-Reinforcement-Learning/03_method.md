# D4RL: Datasets for Deep Data-Driven Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Method and Contribution

사람·규칙 controller·정책 혼합·멀티태스크 데이터를 포함하는 offline RL benchmark와 평가 프로토콜을 제시한다.

## Observation, State, and Action

고정 transition dataset → offline 정책 학습 → 환경별 평가.

## Objective and Training / Inference Boundary

초록에서 확인한 학습 구성이다. 정확한 loss·gradient 경로·학습/추론 차이·controller 또는 memory 시간 단위는 본문 확인이 필요하다.

점검 항목: dataset version·terminal/timeout·normalized score·현행 API와 원본 데이터 호환.

## Method-Specific Comparison — Researcher Interpretation

실제 데이터 subset의 coverage·성공률·정책 혼합을 분리해 같은 budget의 BC/RL을 비교한다.

이 비교는 제안이며 실행 결과나 논문의 ablation이 아니다.

## Evidence Boundary

[공식 paper/abstract](https://arxiv.org/abs/2004.07219). arXiv v4와 공식 유지 repository 확인. 확인되지 않은 conference venue를 부여하지 않으며 현행 라이브러리의 실행 호환성을 보장하지 않는다.
