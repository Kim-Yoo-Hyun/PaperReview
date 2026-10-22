# Active Offline Policy Selection

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

OPE로 초기화하고 policy similarity 기반 Bayesian 선택으로 다음 평가를 배분한다.

## Observation–State–Action Interface

Logged data·policy 후보·평가 결과 → 다음 policy 선택.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: kernel 입력, adaptive reuse, candidate chronology, online budget.

Source가 명시한 evaluation 범위: 여러 benchmark와 다수 후보 정책의 selection 효율을 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 후보 집합에서 OPE-only·uniform·AOPS 계열을 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://papers.nips.cc/paper_files/paper/2021/hash/cec2346566ba8ecd04bfd992fd193fb3-Abstract.html). 수식·세부 구현·코드 실행은 미검증이다.
