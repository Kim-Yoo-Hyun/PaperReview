# D4RL: Datasets for Deep Data-Driven Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Source-Supported Evaluation Scope

고정 데이터로 학습한 정책을 시뮬레이터에서 비교한다. Adroit의 사람 시연은 시뮬레이션 원격조작이고, CARLA의 운전 데이터는 규칙 제어기로 생성했다.

## Metrics, Baselines, and Generalization

dataset version·terminal/timeout·normalized score·현행 API와 원본 데이터 호환.

정확한 dataset/split·trial 수·baseline budget·metric 정의·ablation 수치는 이번 초록 정리에서 확정하지 않았다. 이는 원문에 미보고됐다는 뜻이 아니다.

## Reproducibility and Limitations

arXiv v4와 공식 유지 repository 확인. 확인되지 않은 conference venue를 부여하지 않으며 현행 라이브러리의 실행 호환성을 보장하지 않는다.

공개 code/project가 있어도 실행 재현을 뜻하지 않는다. 실제 로봇·simulation·이론/survey의 범위를 위 평가 설명대로 구별한다.

## Proposed Comparison — Researcher Interpretation

실제 데이터 subset의 coverage·성공률·정책 혼합을 분리해 같은 budget의 BC/RL을 비교한다.

아직 실행하지 않았으며 예상 이득을 측정 결과로 기록하지 않는다.

## Evidence

[공식 paper/abstract](https://arxiv.org/abs/2004.07219). Code/project·확인 날짜는 [overview](./01_overview.md)를 따른다.
