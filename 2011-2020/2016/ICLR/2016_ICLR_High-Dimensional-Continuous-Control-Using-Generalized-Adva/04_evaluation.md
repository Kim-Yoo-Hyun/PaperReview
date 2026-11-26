# High-Dimensional Continuous Control Using Generalized Advantage Estimation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Source-Supported Evaluation Scope

시뮬레이션의 이족·사족 보행과 기립 과제를 평가한다. 실제 로봇 검증으로 확대하지 않는다.

## Metrics, Baselines, and Generalization

λ·γ의 시간 단위, truncation bootstrap, 가치함수 오차.

정확한 dataset/split·trial 수·baseline budget·metric 정의·ablation 수치는 이번 초록 정리에서 확정하지 않았다. 이는 원문에 미보고됐다는 뜻이 아니다.

## Reproducibility and Limitations

ICLR 2016 공식 accepted conference list로 게재 확인. 2015 최초 preprint와 2018 v6를 별도 논문으로 만들지 않는다.

공개 code/project가 있어도 실행 재현을 뜻하지 않는다. 실제 로봇·simulation·이론/survey의 범위를 위 평가 설명대로 구별한다.

## Proposed Comparison — Researcher Interpretation

같은 trajectory에서 step/chunk bootstrap과 종료 mask를 고정해 advantage 및 gradient 차이를 비교한다.

아직 실행하지 않았으며 예상 이득을 측정 결과로 기록하지 않는다.

## Evidence

[공식 paper/abstract](https://arxiv.org/abs/1506.02438). Code/project·확인 날짜는 [overview](./01_overview.md)를 따른다.
