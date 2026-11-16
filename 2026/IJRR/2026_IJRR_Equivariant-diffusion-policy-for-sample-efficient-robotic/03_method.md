# Equivariant diffusion policy for sample-efficient robotic manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

조작의 기하학적 대칭성을 denoising에 반영해 데이터 효율을 높인다.

## Observation–State–Action Interface

관측·noisy action trajectory → equivariant denoiser → action trajectory.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 적용 가능한 symmetry, 절대/상대 action, RGB/point-cloud 정보량, checkpoint 선택.

Source가 명시한 evaluation 범위: MimicGen simulation과 실로봇 manipulation에서 소량 시연 학습을 비교한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

같은 입력·시연·action 좌표계에서 augmentation과 equivariant denoising을 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://journals.sagepub.com/doi/10.1177/02783649261424445) · [저자 project/code](https://equidiff.github.io/) · [공식 code](https://github.com/pointW/equidiff). 수식·세부 구현·코드 실행은 미검증이다.
