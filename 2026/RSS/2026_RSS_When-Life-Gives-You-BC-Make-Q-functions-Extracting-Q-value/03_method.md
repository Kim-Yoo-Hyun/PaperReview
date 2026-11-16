# When Life Gives You BC, Make Q-functions: Extracting Q-values from Behavior Cloning for On-Robot Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

BC로부터 Q를 추정하고 BC·RL 행동을 가치에 따라 선택하며 online 학습한다.

## Observation–State–Action Interface

BC 정책·학습 정책 → Q-Gating → 실제 상호작용·RL 갱신.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: Q 초기화에 필요한 상호작용, 두 정책 유지 비용, gating의 행동 분포 변화.

Source가 명시한 evaluation 범위: D4RL·robomimic과 실제 pipe assembly·kitting을 평가한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

초기 BC와 환경 예산을 고정하고 gating 유무 및 BC 유지 regularization을 교차 대조한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://roboticsproceedings.org/rss22/p153.html) · [저자 project/code](https://pages.rai-inst.com/q2rl_website/) · [공식 code](https://github.com/rai-opensource/q2rl). 수식·세부 구현·코드 실행은 미검증이다.
