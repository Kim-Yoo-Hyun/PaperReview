# ActMem-VLA: Action-History Memory with Dual-Expert Denoising for Long-Horizon Vision-Language-Action Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Mamba 행동 이력 memory와 PreAction Expert를 학습하고 frozen action expert에 denoising을 넘긴다.

## Observation–State–Action Interface

실행 행동 이력·현재 맥락 → memory/PAE → frozen AE의 행동 refinement.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: memory reset·실제 실행 이력의 정의·효과 피드백 접근권·분할과 예산.

Source가 명시한 evaluation 범위: LIBERO-Mem과 네 실제 조작 과제에서 memory 및 기존 VLA와 비교한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

같은 명령 이력에서 실제 접촉/효과가 달라지는 자연 사례로 관측·이력 의존성을 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2609.37307). 수식·세부 구현·코드 실행은 미검증이다.
