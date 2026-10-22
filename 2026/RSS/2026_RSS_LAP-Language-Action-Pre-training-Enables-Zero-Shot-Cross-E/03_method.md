# LAP: Language-Action Pre-training Enables Zero-Shot Cross-Embodiment Transfer

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

언어 action 표현으로 사전학습하고 새로운 embodiment로의 zero-shot 전이를 탐색한다.

## Observation–State–Action Interface

영상·지시 → 언어 action → 로봇별 실행.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: zero-shot 정의, robot-specific mapping, pretraining 중복.

Source가 명시한 evaluation 범위: 새 embodiment 전이와 robot adaptation 평가를 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

같은 task의 기존/새 embodiment에서 adapter·data 노출을 고정해 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p203.html). 수식·세부 구현·코드 실행은 미검증이다.
