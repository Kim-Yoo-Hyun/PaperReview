# DEAS: DEtached value learning with Action Sequence for Scalable Offline RL

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

행동 sequence 기반 가치 학습에 detached value learning을 적용하여 데이터 안의 고수익 행동으로 추정을 유도한다.

## Observation–State–Action Interface

Offline observation/action sequence → value estimation → sequence policy; VLA action chunk와 연결한다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: value target gradient 경계, OOD action 처리, 실로봇 데이터·환경 예산.

Source가 명시한 evaluation 범위: OGBench, RoboCasa Kitchen과 실세계 조작의 VLA 확장을 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

같은 chunk·데이터에서 single-step critic, sequence critic, detached sequence critic을 대조한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/68b7f71467c83d5d32275c5acbf6b588-Abstract-Conference.html) · [저자 project/code](https://changyeon.site/deas/) · [공식 code](https://github.com/csmile-1006/DEAS-Isaac-GR00T). 수식·세부 구현·코드 실행은 미검증이다.
