# Self-Improving Robot Policy with Compositional World Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Multi-view controllable dynamics와 progress value model을 분리하여 imagined rollout에서 advantage를 만들고 policy를 개선한다.

## Observation–State–Action Interface

Observation/action → imagined multi-view future → progress value/advantage → policy update.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: Progress label 생성, failure coverage, value calibration과 real rollout 예산.

Source가 명시한 evaluation 범위: RSS abstract는 dynamic brick sorting, backpack packing, box closing의 세 real-world task 평가를 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

고정 dynamics 아래 progress-value 구성과 rollout horizon을 바꾸고 imagined score와 real success의 일치도를 측정한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://roboticsproceedings.org/rss22/p012.html) · [저자 project/code](https://github.com/OpenDriveLab/RISE). 수식·세부 구현·코드 실행은 미검증이다.
