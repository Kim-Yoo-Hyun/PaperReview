# A process-centric manipulation taxonomy for the organization, classification and synthesis of tactile robot skills

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

전문가의 process specification을 taxonomy와 parametric tactile skill로 연결한다.

## Observation–State–Action Interface

공정 요구 → skill specification → policy/controller → 접촉 feedback.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 전문가 specification 비용, grasp/접촉 가정, skill 선택과 저수준 controller 기여.

Source가 명시한 evaluation 범위: 산업 응용의 여러 tactile skill과 목표 pose 교란을 실로봇에서 평가한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 skill/controller에 process 조건과 언어 selector를 각각 연결해 전환 오류를 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://www.nature.com/articles/s42256-025-01045-3). 수식·세부 구현·코드 실행은 미검증이다.
