# Leave No Observation Behind: Real-time Correction for VLA Action Chunks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

새 관측과 base action 등에 조건화한 residual head로 chunk action을 수정한다.

## Observation–State–Action Interface

VLA chunk·fresh observation·chunk 정보 → residual → 실행.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: residual target, 추가 feature, checkpoint 공개, 관측 latency.

Source가 명시한 evaluation 범위: Kinetix와 LIBERO Spatial 평가를 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

Base 고정 후 residual 유무와 delay/horizon을 교차 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2509.23224) · [저자 project/code](https://github.com/k1000dai/a2c2-libero). 수식·세부 구현·코드 실행은 미검증이다.
