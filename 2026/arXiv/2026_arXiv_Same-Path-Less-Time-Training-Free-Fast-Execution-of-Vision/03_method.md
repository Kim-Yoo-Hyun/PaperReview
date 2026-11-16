# Same Path, Less Time: Training-Free Fast Execution of Vision-Language-Action Models under Inference Latency

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Frozen chunk policy에 경로 유지 time scaling을 적용해 비동기 추론과 실행 속도를 맞춘다.

## Observation–State–Action Interface

고정 VLA 행동 chunk·추론 지연 → 경로/진행도 정렬 → 속도 조절된 실행 명령.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 실제 지연과 주입 지연·동작 제한·gripper 동기화·실제 로봇 전이.

Source가 명시한 evaluation 범위: LIBERO와 LIBERO-Dynamic에서 지연을 주입해 성공률과 task throughput을 비교한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 frozen 정책에서 stop-and-wait·비동기1배속·PTS를 같은 지연과 성공/시간으로 대조한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2611.01390). 수식·세부 구현·코드 실행은 미검증이다.
