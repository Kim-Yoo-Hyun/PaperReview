# RL's Razor: Why Online Reinforcement Learning Forgets Less

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

같은 신규 과제 성능에서 RL과 SFT의 망각·정책 KL을 비교하고 on-policy RL의 작은 분포 변화 편향을 분석한다.

## Observation–State–Action Interface

기존 정책 → RL/SFT 후학습 정책 → 신규·기존 과제 행동 평가.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: KL 방향·평가 관측 분포·기존 능력 정의·단순 학습률/모방 대안.

Source가 명시한 evaluation 범위: 언어 모델과 로봇 foundation model에서 적응 성능과 기존 능력 보존을 평가한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

같은 초기 정책·적응 성능·비용에서 목표별 행동 변화와 관측별 KL의 관계를 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/618c95f4557c15b253fb0e6f548ea0c0-Abstract-Conference.html) · [저자 project/code](https://jyopari.github.io/posts/rl_razor). 수식·세부 구현·코드 실행은 미검증이다.
