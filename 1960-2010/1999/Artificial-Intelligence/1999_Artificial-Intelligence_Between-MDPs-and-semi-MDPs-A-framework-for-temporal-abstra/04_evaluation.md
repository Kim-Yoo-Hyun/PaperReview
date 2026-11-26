# Between MDPs and semi-MDPs: A framework for temporal abstraction in reinforcement learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Source-Supported Evaluation Scope

시간 추상화의 이론과 학습·계획 예제를 다룬다. VLA chunk가 자동으로 option이라는 주장은 없다.

## Metrics, Baselines, and Generalization

initiation·termination·closed-loop 조건·물리 시간 할인.

정확한 dataset/split·trial 수·baseline budget·metric 정의·ablation 수치는 이번 초록 정리에서 확정하지 않았다. 이는 원문에 미보고됐다는 뜻이 아니다.

## Reproducibility and Limitations

공식 초록과 metadata 수준의 정리다. 구체적 실험 조건·수치·본문 한계는 추가 확인이 필요하다.

공개 code/project가 있어도 실행 재현을 뜻하지 않는다. 실제 로봇·simulation·이론/survey의 범위를 위 평가 설명대로 구별한다.

## Proposed Comparison — Researcher Interpretation

같은 행동열에서 고정 chunk와 상태 의존 종료를 분리해 discount·return의 정의를 대조한다.

아직 실행하지 않았으며 예상 이득을 측정 결과로 기록하지 않는다.

## Evidence

[공식 paper/abstract](https://www.sciencedirect.com/science/article/pii/S0004370299000521). Code/project·확인 날짜는 [overview](./01_overview.md)를 따른다.
