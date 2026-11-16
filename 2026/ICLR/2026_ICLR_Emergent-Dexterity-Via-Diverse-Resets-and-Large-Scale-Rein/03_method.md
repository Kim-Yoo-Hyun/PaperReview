# Emergent Dexterity Via Diverse Resets and Large-Scale Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

다양한 robot-object 상호작용 reset을 프로그램으로 생성하고 공통 보상으로 RL을 학습한 뒤 visuomotor 정책으로 증류한다.

## Observation–State–Action Interface

다양한 simulator reset → RL 정책 → 시각 정책 증류 → 실제 로봇.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: reset 생성의 물리 유효성·특권 정보, 증류 비용, 초기 조건 분할.

Source가 명시한 evaluation 범위: 장기 dexterous manipulation과 넓은 초기 조건, zero-shot 실로봇 전이를 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

고정 reset 집합에서 방법을 비교하고 별도로 reset 다양성만 변화시켜 성공과 retry를 측정한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/8e3e3488623d64c493a7f11cf1f2e49f-Abstract-Conference.html) · [저자 project/code](https://omnireset.github.io/). 수식·세부 구현·코드 실행은 미검증이다.
