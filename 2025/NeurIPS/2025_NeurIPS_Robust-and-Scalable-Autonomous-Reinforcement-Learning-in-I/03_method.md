# Robust and Scalable Autonomous Reinforcement Learning in Irreversible Environments

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

학습 진전에 따른 curriculum과 행동 기반 비가역성 식별을 결합한다.

## Observation–State–Action Interface

Forward/reset 경험 → informative state 선택·위험 회피.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: irreversibility 정의, behavior encoding, task-specific 정보, reset 비용.

Source가 명시한 evaluation 범위: 가역/비가역 환경에서 성능과 manual reset 감소를 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 위험 event에서 task predicate와 행동 기반 탐지를 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2025/hash/56d748a1d7128158681280be7668e0d3-Abstract-Conference.html). 수식·세부 구현·코드 실행은 미검증이다.
