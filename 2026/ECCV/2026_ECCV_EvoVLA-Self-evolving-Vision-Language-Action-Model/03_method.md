# EvoVLA: Self-evolving Vision-Language-Action Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Counterfactual hard negative 기반 stage reward, relative pose 탐색, 선택적 장기 memory를 결합한다.

## Observation–State–Action Interface

관측·지시 → VLA rollout; stage reward·pose exploration·memory가 RL 후학습을 지원한다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: pose·stage annotation의 특권 정보, hard-negative 생성 비용, 세 모듈별 기여.

Source가 명시한 evaluation 범위: Discoverse-L 장기 조작과 실제 로봇의 성공·stage hallucination을 평가한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 rollout에서 기본 보상·near-miss 보정·새 방법을 비교하고 독립 물리 완료 지표를 둔다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://link.springer.com/chapter/10.1007/978-3-032-37023-5_14) · [저자 project/code](https://aigeeksgroup.github.io/EvoVLA/) · [공식 code](https://github.com/AIGeeksGroup/EvoVLA). 수식·세부 구현·코드 실행은 미검증이다.
