# LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

물체·초기 상태·지시·환경 perturbation으로 일반화와 지시 의존성을 점검한다.

## Observation–State–Action Interface

변형 task/지시 → VLA → 실행 결과.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 변경된 목표의 타당성, 언어 교란의 의미, v1/v2 차이.

Source가 명시한 evaluation 범위: LIBERO 기반 변형 평가를 보고한다. 극단적 저하 수치의 task validity는 별도 본문 감사가 필요하다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

Goal/planner/evaluator를 먼저 맞춘 뒤 원본과 변형 task 성공을 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2510.03827) · [저자 project/code](https://github.com/Zxy-MLlab/LIBERO-PRO). 수식·세부 구현·코드 실행은 미검증이다.
