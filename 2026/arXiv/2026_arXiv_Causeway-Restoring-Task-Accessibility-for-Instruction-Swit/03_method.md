# Causeway: Restoring Task Accessibility for Instruction Switching in VLA Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

목표 작업의 re-entry pose를 조건으로 frozen decoder를 통한 gradient를 이용해 action-stream 표현을 수정하고, 정책 자체가 복귀 행동을 생성하는 inference-time 개입을 제안한다.

## Observation–State–Action Interface

현재 상태·새 목표·re-entry pose → 동결 VLA 내부 표현 개입 → 복귀 행동과 목표 작업 실행. 재진술만 사용하는 언어 조건과 정보·개입 위치가 다르다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: re-entry pose 획득과 관측 접근, decoder별 개입 위치·계산 비용, 복귀/인계 조건, 실제 로봇 평가 범위.

Source가 명시한 evaluation 범위: LIBERO-Goal, LIBERO-Object와 실제 xArm에서 instruction switching과 복구를 보고한다. 정확한 비교 수치·시행 수·특권 정보 조건은 신규 노트에서 본문 정독 완료로 표시하지 않는다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

같은 시작·수정 상태에서 원자 목표와 oracle 복합 지시의 능력을 먼저 구분한다. Causeway 개입을 비교하려면 re-entry 정보와 추가 계산 비용을 별도로 맞추며 현재 P0에 자동 추가하지 않는다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2609.30913). 수식·세부 구현·코드 실행은 미검증이다.
