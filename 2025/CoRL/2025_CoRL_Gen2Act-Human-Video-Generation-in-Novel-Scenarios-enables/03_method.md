# Gen2Act: Human Video Generation in Novel Scenarios enables Generalizable Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

고정된 생성 모델의 인간 영상을 조건으로 공통 robot policy를 실행한다.

## Observation–State–Action Interface

장면·언어 → 생성 인간 영상 → 영상 조건 closed-loop robot action.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: robot-data holdout, video 사전학습 중복, motion conditioning과 실행 latency.

Source가 명시한 evaluation 범위: 새 물체 종류·동작을 포함한 실환경 manipulation을 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 정책에서 생성 video·정지 keyframe·time-shuffled video를 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v305/bharadhwaj25a.html) · [저자 project/code](https://homangab.github.io/gen2act/). 수식·세부 구현·코드 실행은 미검증이다.
