# Learning to Look: Seeking Information for Decision Making via Policy Factorization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

정보 탐색과 조작 정책을 분리하고 조작 정책에서 탐색 reward를 구성하는 DISaM을 제안한다.

## Observation–State–Action Interface

관측·context에서 정보 수집 또는 조작으로 전환한다. 두 정책 분해를 단일 VLA 공동 학습으로 부르지 않는다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: Context privilege·KL 대상 분포·학습 reward·전환 threshold.

Source가 명시한 evaluation 범위: 공식 초록은 simulation·실세계의 정보 탐색이 필요한 조작 과제 5개를 평가한다고 명시한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 context·행동 후보·관측 예산에서 분포 간 KL과 성공 lookup을 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v270/dass25a.html) · [저자 project/code](https://robin-lab.cs.utexas.edu/learning2look/) · [공식 code](https://github.com/UT-Austin-RobIn/l2l). 수식·세부 구현·코드 실행은 미검증이다.
