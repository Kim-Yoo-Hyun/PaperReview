# Policy invariance under reward transformations: Theory and application to reward shaping

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Source-Supported Evaluation Scope

정책 불변성 분석과 거리·부분 목표 potential의 학습 예제를 제시한다. VLA 평가 논문은 아니다.

## Metrics, Baselines, and Generalization

할인율·종료 potential·Markov 상태·history 의존 보상.

정확한 dataset/split·trial 수·baseline budget·metric 정의·ablation 수치는 이번 초록 정리에서 확정하지 않았다. 이는 원문에 미보고됐다는 뜻이 아니다.

## Reproducibility and Limitations

저자 원문 abstract와 Russell의 ICML-99 publication 기록 확인. PDF는 웹에서 확인했으며 local cache는 저장하지 않았다. ACM endpoint는 403으로 접근 실패해 DOI를 추정하지 않았다.

공개 code/project가 있어도 실행 재현을 뜻하지 않는다. 실제 로봇·simulation·이론/survey의 범위를 위 평가 설명대로 구별한다.

## Proposed Comparison — Researcher Interpretation

작은 명시적 MDP에서 원 보상·potential 차이·그냥 progress 점수의 최적 행동을 대조한다.

아직 실행하지 않았으며 예상 이득을 측정 결과로 기록하지 않는다.

## Evidence

[공식 paper/abstract](https://people.eecs.berkeley.edu/~russell/papers/icml99-shaping.pdf). Code/project·확인 날짜는 [overview](./01_overview.md)를 따른다.
