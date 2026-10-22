# Restoring the Right Stream: Training-Free OOD Robustness for Vision–Language–Action Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Gated Per-Stream Manifold Restoration으로 visual/state 입력을 따로 복원한다.

## Observation–State–Action Interface

영상·proprioception·언어 → gated restoration → frozen policy.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: native state interface, gate oracle leakage, code·trial manifest 공개.

Source가 명시한 evaluation 범위: OpenVLA-OFT와 LIBERO-Plus 평가를 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

물리적 이동과 state reporting offset을 나누어 보정의 이득·손해를 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://www.mdpi.com/1099-4300/28/9/975) · [저자 project/code](https://www.mdpi.com/1099-4300/28/9/975). 수식·세부 구현·코드 실행은 미검증이다.
