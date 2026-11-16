# Universal Value Function Approximators

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Source-Supported Evaluation Scope

학습하지 않은 목표로 가치와 정책을 일반화하는 실험을 보고한다. 언어 지시나 다중 embodiment 보장은 아니다.

## Metrics, Baselines, and Generalization

목표 표현·목표 holdout·목표별 coverage·value와 policy 일반화의 구분.

정확한 dataset/split·trial 수·baseline budget·metric 정의·ablation 수치는 이번 초록 정리에서 확정하지 않았다. 이는 원문에 미보고됐다는 뜻이 아니다.

## Reproducibility and Limitations

공식 초록과 metadata 수준의 정리다. 구체적 실험 조건·수치·본문 한계는 추가 확인이 필요하다.

공개 code/project가 있어도 실행 재현을 뜻하지 않는다. 실제 로봇·simulation·이론/survey의 범위를 위 평가 설명대로 구별한다.

## Proposed Comparison — Researcher Interpretation

같은 상태의 두 목표에서 분리·공유 value와 목표별 행동 선택을 비교한다.

아직 실행하지 않았으며 예상 이득을 측정 결과로 기록하지 않는다.

## Evidence

[공식 paper/abstract](https://proceedings.mlr.press/v37/schaul15.html). Code/project·확인 날짜는 [overview](./01_overview.md)를 따른다.
