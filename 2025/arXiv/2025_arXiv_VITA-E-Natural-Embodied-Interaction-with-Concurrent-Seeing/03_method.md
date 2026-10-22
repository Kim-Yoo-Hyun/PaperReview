# VITA-E: Natural Embodied Interaction with Concurrent Seeing, Hearing, Speaking, and Acting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Active/Standby dual-model과 system command token을 사용한다.

## Observation–State–Action Interface

시각·음성·지시 → 발화와 system/action command.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 명령 token timing, rollback 범위, ICLR acceptance 미확인.

Source가 명시한 evaluation 범위: Humanoid platform의 동시 interaction을 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

중단 latency와 task 재개 성공을 별도 metric으로 측정한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2510.21817) · [저자 project/code](https://lxysl.github.io/VITA-E/). 수식·세부 구현·코드 실행은 미검증이다.
