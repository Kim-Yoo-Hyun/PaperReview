# Scaling Robot Policy Evaluation via Discrete Diffusion World Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Action을 unified token으로 다루는 discrete diffusion과 keyframe memory·progress 출력을 결합한다.

## Observation–State–Action Interface

관측·언어·action chunk → 미래 관측·성공 지표 → policy ranking.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 성공 평가기 독립성, 실패 데이터, final/preprint 차이.

Source가 명시한 evaluation 범위: LIBERO·RoboTwin 및 real-robot task 기반 평가를 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 초기 관측에서 후보별 predicted/native 결과를 맞춰 false positive와 순위 오류를 센다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v306/li26hi.html) · [저자 project/code](https://dworldeval.github.io/). 수식·세부 구현·코드 실행은 미검증이다.
