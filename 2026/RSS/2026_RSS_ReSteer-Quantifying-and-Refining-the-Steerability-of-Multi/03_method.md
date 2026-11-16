# ReSteer: Quantifying and Refining the Steerability of Multitask Robot Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

상태별 task steerability를 측정하고, 전환이 어려운 상태의 추정·전환 구간 데이터 생성·정책 self-refinement를 연결한다.

## Observation–State–Action Interface

현재 관측과 새 언어 지시 → multitask policy의 행동. 중간 상태에서의 전환 능력과 초기 상태의 작업 능력을 구별한다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: steerability score의 분모·switch timing·초기 능력, estimator와 실제 성공의 관계, 데이터 생성 비용, 제약 유지·철회가 평가에 포함되는 범위.

Source가 명시한 evaluation 범위: LIBERO와 실제 로봇의 지시 전환을 평가한다. 공개 repository는 LIBERO 평가·데이터 생성 경로를 제공하지만 로컬 native 실행은 아직 확인하지 않았다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

기존 R8 단일 지시 전환 IO를 Docker에서 먼저 확인한다. 이후 같은 상태에서 전체 재명시·규칙 갱신·oracle 지시를 비교하는 것은 별도 연구 설계이며 아직 실행하지 않았다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://roboticsproceedings.org/rss22/p143.html) · [저자 project/code](https://resteer-vla.github.io/) · [공식 code](https://github.com/ChenZhenY/ReSteer). 수식·세부 구현·코드 실행은 미검증이다.
