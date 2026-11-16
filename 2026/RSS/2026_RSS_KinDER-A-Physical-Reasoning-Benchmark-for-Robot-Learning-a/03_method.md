# KinDER: A Physical Reasoning Benchmark for Robot Learning and Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

물리 추론 난점을 분리한 절차적 환경과 skill·시연·평가 baseline을 제공한다.

## Observation–State–Action Interface

기하·동역학 제약 → 계획 또는 학습된 행동 → 물리적 결과.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: skill 호출 권한, 관측 특권, baseline별 compute, 절차적 split.

Source가 명시한 evaluation 범위: 다양한 planning·IL·RL baseline 및 mobile manipulator 대응 실험을 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 초기 상태에서 구조화된 상태 baseline과 visual policy를 비교하고 실패 원인을 분리한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://roboticsproceedings.org/rss22/p184.html) · [저자 project/code](https://prpl-group.com/kinder-site/) · [공식 code](https://github.com/Princeton-Robot-Planning-and-Learning/kindergarden). 수식·세부 구현·코드 실행은 미검증이다.
