# PROGRESSOR: A Perceptually Guided Reward Estimator with Self-Supervised Online Refinement

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

초기·현재·목표 관측으로 progress를 추정하고 online refinement한다.

## Observation–State–Action Interface

영상 triplet → progress 추정 → robot reward.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: goal image 정보, refinement 데이터, train/test overlap, reward scale.

Source가 명시한 evaluation 범위: Human video와 실제 로봇 offline RL 평가를 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 rollout에서 progress score와 독립 success label의 불일치를 검수한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://openaccess.thecvf.com/content/ICCV2025/html/Ayalew_PROGRESSOR_A_Perceptually_Guided_Reward_Estimator_with_Self-Supervised_Online_Refinement_ICCV_2025_paper.html). 수식·세부 구현·코드 실행은 미검증이다.
