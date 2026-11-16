# SPRINT: Scalable Policy Pre-Training via Language Instruction Relabeling

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

LLM을 이용한 지시 재라벨과 서로 다른 궤적의 기술 연결을 offline RL 사전학습에 사용한다.

## Observation–State–Action Interface

기존 trajectory·언어 지시 → 재라벨/연결된 기술 자료 → 정책 사전학습 → 새 과제 적응. 단일 VLA online RL이라고 가정하지 않는다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: cross-trajectory 연결의 유효성, downstream adaptation 예산, 시뮬레이터와 실로봇의 서로 다른 행동 interface, code의 실제 공개 범위.

Source가 명시한 evaluation 범위: 저자 abstract는 가정용 시뮬레이터와 실제 로봇 주방 조작의 장기 과제 적응을 보고한다. 공개 저장소는 ALFRED-RL simulation 경로를 안내한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 원 trajectory와 학습 예산에서 기존 라벨·재라벨만·chaining만·둘 모두를 대조하고 새 장기 과제 성공과 사용 데이터량을 함께 평가한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://doi.org/10.1109/ICRA57147.2024.10610606) · [저자 project/code](https://clvrai.github.io/sprint/) · [공식 code](https://github.com/clvrai/sprint). 수식·세부 구현·코드 실행은 미검증이다.
