# CE-Nav: Flow-Guided Reinforcement Refinement for Cross-Embodiment Local Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Planner 데이터로 embodiment-agnostic flow expert를 학습하고 이를 고정한 채 로봇별 경량 refiner를 online RL로 적응한다.

## Observation–State–Action Interface

기하 행동 prior → dynamics-aware refiner → 로봇 제어. 언어 VLA나 단일 공동 갱신 정책과 구분한다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: planner 관측 접근, dynamics별 상호작용 분모, morphology별 평가 조건.

Source가 명시한 evaluation 범위: 사족·이족·쿼드로터의 국소 항법은 시뮬레이션에서 비교했다. 실물 배포 대상은 Unitree Go2와 MagicDog다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

같은 planner 데이터·online budget에서 frozen prior+refiner와 공동 정책 갱신을 대조한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/514bdfb12b318ad02c6f28dc68f2feea-Abstract-Conference.html) · [저자 project/code](https://github.com/amap-cvlab/CE-Nav). 수식·세부 구현·코드 실행은 미검증이다.
