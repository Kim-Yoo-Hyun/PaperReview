# Real-World Reinforcement Learning of Active Perception Behaviors

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

훈련 때만 사용하는 추가 센서로 privileged value를 학습하고 advantage-weighted regression으로 정책을 개선한다.

## Observation–State–Action Interface

훈련 critic의 privileged 정보와 배포 actor의 제한된 관측을 구분하는 AAWR이다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 추가 센서 접근·초기 demonstrations·advantage 추정·배포 observation.

Source가 명시한 evaluation 범위: 공식 초록은 3개 로봇·8개 조작 과제 및 generalist 초기 정책의 능동 관측 개선을 명시한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

Actor 관측과 critic privilege를 분리하고 같은 초기 정책·interaction budget에서 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://papers.neurips.cc/paper_files/paper/2025/hash/aa1b1a959c80086cba61d0fd66de412f-Abstract-Conference.html) · [저자 project/code](https://penn-pal-lab.github.io/aawr/). 수식·세부 구현·코드 실행은 미검증이다.
