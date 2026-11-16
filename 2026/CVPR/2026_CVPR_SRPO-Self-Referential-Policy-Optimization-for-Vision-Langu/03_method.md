# SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

같은 batch의 성공 궤적을 기준으로 world-model latent에서 실패의 진행 보상을 만든다.

## Observation–State–Action Interface

성공·실패 rollout → latent 진행 비교 → VLA 정책 갱신.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 성공 없는 batch 처리, world-model 사전학습 비용, 진행 측정 오류, reward scale.

Source가 명시한 evaluation 범위: LIBERO와 LIBERO-Plus에서 학습 효율·견고성을 평가한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 실패 pool·성공 참조·원 목표 평가에서 relabeling, self-reference shaping, 둘의 결합을 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Fei_SRPO_Self-Referential_Policy_Optimization_for_Vision-Language-Action_Models_CVPR_2026_paper.html). 수식·세부 구현·코드 실행은 미검증이다.
