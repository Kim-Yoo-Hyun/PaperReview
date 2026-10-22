# Semantic Contact Fields for Category-Level Generalizable Tool Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

3D semantic-contact field를 sim pretraining과 real pseudo-label 조정으로 학습한다.

## Observation–State–Action Interface

시각 의미·접촉 추정 → 3D field → diffusion policy.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 촉각 입력 종류, pseudo-label 정확도, unseen-tool split.

Source가 명시한 evaluation 범위: 서로 다른 도구를 사용하는 contact-rich 작업 평가를 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 demonstration에서 semantic-only와 contact 추가 조건을 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p004.html) · [저자 project/code](https://github.com/Kevinskwk/SCFields). 수식·세부 구현·코드 실행은 미검증이다.
