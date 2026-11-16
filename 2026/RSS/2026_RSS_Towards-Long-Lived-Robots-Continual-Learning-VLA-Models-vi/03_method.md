# Towards Long-Lived Robots: Continual Learning VLA Models via Reinforcement Fine-Tuning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

행동 chunk의 이산 일치·연속 궤적 정렬·출력 형식 보상으로 reinforcement fine-tuning한다.

## Observation–State–Action Interface

관측·지시 → 행동 chunk; 참조 행동과의 일치도가 학습 보상.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 참조 궤적 의존성, rehearsal 여부, 순차 task order, 보상별 효과.

Source가 명시한 evaluation 범위: SimplerEnv·LIBERO 및 실제 조작, LIBERO continual learning을 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 참조 데이터로 SFT, 동일 가중 회귀, chunk RL을 비교하고 새·기존 과제를 함께 평가한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://roboticsproceedings.org/rss22/p086.html). 수식·세부 구현·코드 실행은 미검증이다.
