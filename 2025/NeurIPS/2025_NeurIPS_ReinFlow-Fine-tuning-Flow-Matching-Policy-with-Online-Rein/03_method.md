# ReinFlow: Fine-tuning Flow Matching Policy with Online Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Flow 경로에 학습 가능한 잡음을 넣어 이산 시간 확률 과정으로 바꾸고 정책 likelihood를 사용해 online RL 후학습한다.

## Observation–State–Action Interface

관측 → flow velocity와 학습용 noise → 생성된 연속 행동. 정책 생성 과정의 확률과 물리 행동의 주변 밀도를 구분해 읽어야 한다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 생성 경로 likelihood와 action likelihood의 차이, DPPO 비교의 모델/자료/시간 통제, noise 학습과 step 축소 효과, 실제 로봇 평가 여부.

Source가 명시한 evaluation 범위: 공식 abstract는 locomotion과 state/visual manipulation에서 Rectified Flow·Shortcut 정책 후학습을 보고한다. 최신 저장소의 VLA 지원을 원 논문 실험으로 소급하지 않는다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

하나의 공개 task에서 같은 초기 flow 정책과 생성 step 수로 고정/학습 noise를 비교하고 성공률·return·전체 rollout/학습 wall time을 함께 기록한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2025/hash/98d6f928497d9eaad9f320fb2db3040d-Abstract-Conference.html) · [저자 project/code](https://reinflow.github.io/) · [공식 code](https://github.com/ReinFlow/ReinFlow). 수식·세부 구현·코드 실행은 미검증이다.
