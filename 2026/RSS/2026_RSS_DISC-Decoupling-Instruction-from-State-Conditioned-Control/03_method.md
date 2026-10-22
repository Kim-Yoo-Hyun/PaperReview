# DISC: Decoupling Instruction from State-Conditioned Control via Policy Generation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Instruction-only hypernetwork가 task-specific visuomotor policy의 파라미터를 생성한다.

## Observation–State–Action Interface

언어 → policy weights; 생성된 policy는 관측 → action.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: generated parameter 수, training budget, 동일 장면 통제.

Source가 명시한 evaluation 범위: LIBERO-90, Meta-World 및 동일 visual context의 실제 로봇 비교를 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

장면을 고정하고 목표 지시만 바꾸는 paired evaluation을 한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p147.html) · [저자 project/code](https://github.com/ReNginx/DISC). 수식·세부 구현·코드 실행은 미검증이다.
