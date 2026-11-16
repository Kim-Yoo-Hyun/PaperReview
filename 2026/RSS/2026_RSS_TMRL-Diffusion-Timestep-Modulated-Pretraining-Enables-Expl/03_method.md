# TMRL: Diffusion Timestep-Modulated Pretraining Enables Exploration for Efficient Policy Finetuning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

입력에 diffusion noise를 넣어 사전학습하고 RL이 조건화 noise 수준을 선택한다.

## Observation–State–Action Interface

관측·noise 수준 → 사전학습 정책의 행동; RL이 timestep을 조절.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: pretraining 추가 비용, high-level action 주기, baseline 탐색 분산, 로봇별 학습 시간.

Source가 명시한 evaluation 범위: 항법·조작 평가를 보고하며 project는 실제 VLA 후학습도 설명한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 CSP checkpoint에서 고정 noise, 무작위 noise, 학습된 noise 선택을 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://roboticsproceedings.org/rss22/p208.html) · [저자 project/code](https://weirdlabuw.github.io/tmrl/) · [공식 code](https://github.com/matthewh6/tmrl). 수식·세부 구현·코드 실행은 미검증이다.
