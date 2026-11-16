# MolmoSpaces: Large-Scale Open Ecosystem for Robot Manipulation and Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

다양한 실내 환경·상호작용 객체·grasp 자산과 통합 benchmark를 제공한다.

## Observation–State–Action Interface

장면·객체·로봇 설정 → simulator 기반 조작·항법 과제.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: asset license, 실제 지원 simulator별 기능, 장면 split, 정책별 co-training 여부.

Source가 명시한 evaluation 범위: 조작·항법을 포함한 8개 benchmark task와 sim-to-real 상관을 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

학습 장면을 고정하고 세 변이를 독립적으로 바꾼 held-out 평가를 설계한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://roboticsproceedings.org/rss22/p091.html) · [저자 project/code](https://github.com/allenai/molmospaces). 수식·세부 구현·코드 실행은 미검증이다.
