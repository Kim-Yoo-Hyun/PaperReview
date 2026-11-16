# Fast-ThinkAct: Efficient Vision-Language-Action Reasoning via Verbalizable Latent Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Teacher의 언어·시각 계획을 preference-guided distillation으로 압축하여 verbalizable latent reasoning을 학습한다.

## Observation–State–Action Interface

관측·지시 → compact latent plan → action model. 압축된 추론과 action model의 연결을 구분한다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: teacher 감독 비용, action model 별도 학습 여부, end-to-end latency.

Source가 명시한 evaluation 범위: Embodied manipulation·reasoning benchmark의 latency와 장기 계획·적응·복구를 평가한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 teacher 데이터로 reasoning 제거·latent reasoning·명시 reasoning을 대조한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_Fast-ThinkAct_Efficient_Vision-Language-Action_Reasoning_via_Verbalizable_Latent_Planning_CVPR_2026_paper.html) · [저자 project/code](https://jasper0314-huang.github.io/fast-thinkact/). 수식·세부 구현·코드 실행은 미검증이다.
