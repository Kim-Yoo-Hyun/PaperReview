# A Generalist Pair-wise Progress Critic Model for Vision-Language-Action Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

단일 autoregressive 구조로 행동과 두 시점 사이의 진행 차이를 예측하고, 진행 판단을 RL 보상에 사용한다.

## Observation–State–Action Interface

시각·언어 조건의 행동 출력과 관측 쌍에 대한 progress 출력.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 최종 ICML 모델 크기·동일 weight 여부·reward/done model 및 PPO value의 분리. 2025 preprint 설정을 최종본에 전사하지 않음.

Source가 명시한 evaluation 범위: 공식 abstract는 실제 로봇 RL 평가를 보고한다. 정확한 trial·baseline·수치는 최종 본문 확인 필요.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

최종 학습 그래프의 weight sharing·freeze·reward 공급 경로를 확인한 뒤 독립 성공 판정과 자기 progress 점수의 변화를 분리한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v306/zhang26if.html) · [저자 project/code](https://github.com/InternRobotics/VLAC). 수식·세부 구현·코드 실행은 미검증이다.
