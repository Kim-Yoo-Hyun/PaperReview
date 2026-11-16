# Difference-Aware Retrieval Policies for Imitation Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

시연의 가까운 상태·행동 및 query와의 상대 차이를 이용하는 semi-parametric policy를 학습한다.

## Observation–State–Action Interface

Query state·이웃 시연·상대 벡터 → action prediction.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 이웃 수, history 사용, retrieval 지연과 rollout split.

Source가 명시한 evaluation 범위: Continuous control과 manipulation, 고차원 시각 표현에서 BC와 비교한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

같은 시연·encoder에서 BC와 DARP를 비교하고 retrieval 시간까지 센다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/8c2ecd140ebe227a531edc9a0c3b69d4-Abstract-Conference.html) · [저자 project/code](https://weirdlabuw.github.io/darp-site/) · [공식 code](https://github.com/WEIRDLabUW/darp). 수식·세부 구현·코드 실행은 미검증이다.
