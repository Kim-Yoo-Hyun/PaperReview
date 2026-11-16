# When Vision Overrides Language: Evaluating and Mitigating Counterfactual Failures in VLAs

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

LIBERO-CF로 반사실적 지시 수행을 평가하고 언어 조건부·비조건부 분기의 차이로 행동을 유도한다.

## Observation–State–Action Interface

같은 LIBERO 장면의 대체 지시 → VLA/VA 분기 → 조작 행동.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: focused suite의 장면 변경·OR/target-only 종료·두 목표의 기본 능력·guidance 비용.

Source가 명시한 evaluation 범위: LIBERO-CF와 실제 로봇에서 언어 grounding과 task success를 구별해 평가한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

Prompt·목표 predicate를 일치시키고 두 유효 목표의 첫 사건과 지정 목표 성공을 따로 기록한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2602.17659) · [저자 project/code](https://vla-cf.github.io/) · [공식 code](https://github.com/yuffish/VLA-CF). 수식·세부 구현·코드 실행은 미검증이다.
