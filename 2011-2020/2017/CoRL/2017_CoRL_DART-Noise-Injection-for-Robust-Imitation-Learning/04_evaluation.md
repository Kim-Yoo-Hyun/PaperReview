# DART: Noise Injection for Robust Imitation Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Source-Supported Evaluation Scope

MuJoCo locomotion과 실제 Toyota HSR의 clutter grasping을 평가한다.

## Metrics, Baselines, and Generalization

noise 분포·전문가 회복 능력·개입 비용·train-test 교란.

정확한 dataset/split·trial 수·baseline budget·metric 정의·ablation 수치는 이번 초록 정리에서 확정하지 않았다. 이는 원문에 미보고됐다는 뜻이 아니다.

## Reproducibility and Limitations

공식 CoRL abstract 및 저자 project/code 공개 확인. 공개 repository의 simulation 구현과 실제 HSR 재현 경로는 구별한다.

공개 code/project가 있어도 실행 재현을 뜻하지 않는다. 실제 로봇·simulation·이론/survey의 범위를 위 평가 설명대로 구별한다.

## Proposed Comparison — Researcher Interpretation

동일 전문가 개입·시연 수로 정상 BC·교란 BC·RL을 비교한다.

아직 실행하지 않았으며 예상 이득을 측정 결과로 기록하지 않는다.

## Evidence

[공식 paper/abstract](https://proceedings.mlr.press/v78/laskey17a.html). Code/project·확인 날짜는 [overview](./01_overview.md)를 따른다.
