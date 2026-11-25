# Exploring the Limits of Combinatorial Generalization in Embodied Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

RoboCombine은 단계 순서에 맞는 성공과 단계 간 전환을 측정한다. HSE는 계획·전환·행동을 나누며 PRTI는 개별 기술의 시작 상태를 확장한다.

## Observation–State–Action Interface

전체 지시 또는 하위 지시와 전환 신호가 실행 정책에 전달된다. 정답 전환을 제공하는 평가 트랙이 따로 있다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 각 트랙의 정답 신호, 단계별 분모, 자세 초기화 비용.

Source가 명시한 evaluation 범위: 공개 저장소의 19개 조합 과제와 세 트랙을 확인했다. 초록에 보고된 PRTI 비교는 정답 전환 시각을 준 조건이다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

같은 두 기술에서 정답 전환과 동일 정책을 고정하고 앞 단계가 남긴 자세와 표준 시작 자세를 대조한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2610.15425) · [저자 project/code](https://github.com/AutoLab-SAI-SJTU/RoboCombine). 수식·세부 구현·코드 실행은 미검증이다.
