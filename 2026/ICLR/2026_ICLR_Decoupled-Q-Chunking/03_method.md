# Decoupled Q-Chunking

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Critic이 평가하는 chunk 길이와 actor가 출력하는 chunk 길이를 분리한다.

## Observation–State–Action Interface

State → 짧은 actor action chunk; 긴 critic horizon을 통한 value 학습. 실제 controller frequency는 본문 확인 필요.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 부분 chunk value 추정, policy extraction objective, reactive 평가의 실제 포함 여부.

Source가 명시한 evaluation 범위: 최종 paper의 abstract와 공식 code는 장기 offline goal-conditioned task 평가를 설명한다. 실제 로봇 contact 평가 여부는 확인 필요.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

Q-chunking과 DQC의 critic horizon·data를 맞추고 actor chunk만 변경해 성공률 및 관측 외란 이후 회복을 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://openreview.net/pdf/bde79a617f6c016e2c51c7771416933c0646102c.pdf) · [저자 project/code](https://github.com/ColinQiyangLi/dqc). 수식·세부 구현·코드 실행은 미검증이다.
