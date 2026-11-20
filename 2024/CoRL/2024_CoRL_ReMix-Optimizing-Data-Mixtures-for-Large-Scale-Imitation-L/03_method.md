# ReMix: Optimizing Data Mixtures for Large Scale Imitation Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

DRO 기반 domain 가중치 학습에 action 정규화·이산화와 early stopping을 적용한다.

## Observation–State–Action Interface

이질적 demonstration domain → mixture weights → downstream imitation policy.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: domain 정의, proxy/target 접근, normalization, selection 계산 비용.

Source가 명시한 evaluation 범위: Bridge·Open X-Embodiment 기반 데이터 혼합과 후속 정책 성능을 비교한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 데이터·학습 budget에서 uniform·ReMix·target subset을 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v270/hejna25a.html) · [저자 project/code](https://github.com/jhejna/remix). 수식·세부 구현·코드 실행은 미검증이다.
