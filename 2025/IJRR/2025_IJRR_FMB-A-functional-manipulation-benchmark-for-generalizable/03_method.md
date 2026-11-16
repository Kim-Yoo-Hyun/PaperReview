# FMB: A functional manipulation benchmark for generalizable robotic learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

복제 가능한 3D 프린트 물체·조립 과제와 imitation baseline을 구성한다.

## Observation–State–Action Interface

물체/로봇 관측 → grasp·reorientation·assembly skill → 다단계 조립.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: skill/전체 과제 성공 정의, object split, reset과 force/torque 접근.

Source가 명시한 evaluation 범위: 실로봇의 개별 skill과 조합 과제를 평가하는 데이터·CAD·정책 자산을 제공한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

같은 object split에서 고정 skill 순서와 feedback 기반 전환을 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://journals.sagepub.com/doi/full/10.1177/02783649241276017) · [저자 project/code](https://functional-manipulation-benchmark.github.io/) · [공식 code](https://github.com/rail-berkeley/fmb). 수식·세부 구현·코드 실행은 미검증이다.
