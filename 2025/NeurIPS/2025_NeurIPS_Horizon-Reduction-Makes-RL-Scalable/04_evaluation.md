# Horizon Reduction Makes RL Scalable

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Source-Supported Evaluation Scope

다양한 긴 목표 과제의 scaling을 비교한다. 모든 online VLA RL의 원인으로 일반화하지 않는다.

## Metrics, Baselines, and Generalization

유효 결정 길이·coverage·데이터 크기·학습 계산량·물리 시간.

정확한 dataset/split·trial 수·baseline budget·metric 정의·ablation 수치는 이번 초록 정리에서 확정하지 않았다. 이는 원문에 미보고됐다는 뜻이 아니다.

## Reproducibility and Limitations

공식 초록과 metadata 수준의 정리다. 구체적 실험 조건·수치·본문 한계는 추가 확인이 필요하다.

공개 code/project가 있어도 실행 재현을 뜻하지 않는다. 실제 로봇·simulation·이론/survey의 범위를 위 평가 설명대로 구별한다.

## Proposed Comparison — Researcher Interpretation

데이터·물리 시간·모델 크기를 맞춰 n-step return과 정책 chunk를 독립 변화시킨다.

아직 실행하지 않았으며 예상 이득을 측정 결과로 기록하지 않는다.

## Evidence

[공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2025/hash/0c66099070429b9b49ad8bb19c740c22-Abstract-Conference.html). Code/project·확인 날짜는 [overview](./01_overview.md)를 따른다.
