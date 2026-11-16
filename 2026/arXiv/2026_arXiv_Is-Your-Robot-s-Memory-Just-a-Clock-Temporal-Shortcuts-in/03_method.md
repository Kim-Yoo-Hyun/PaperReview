# Is Your Robot's Memory Just a Clock? Temporal Shortcuts in Memory-Augmented VLA Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

무효 pause/fidget과 memory/timestamp 대조로 temporal shortcut을 진단하고 event-indexed memory를 비교한다.

## Observation–State–Action Interface

관측 memory·시간/사건 index → VLA 행동 → 반복 조작과 종료 판단.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: event 기준의 관측 접근권·counting task 외 전이·제어 개입과 memory 효과의 분리.

Source가 명시한 evaluation 범위: RoboMME counting task에서 무효 사건·시간표식·memory 입력을 통제해 성공 변화를 측정한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

무효 사건·같은 관측의 memory withholding·event index를 먼저 대조하고 잔여 오류를 분리한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2611.14488) · [저자 project/code](https://github.com/bennidict23/memory-clock). 수식·세부 구현·코드 실행은 미검증이다.
