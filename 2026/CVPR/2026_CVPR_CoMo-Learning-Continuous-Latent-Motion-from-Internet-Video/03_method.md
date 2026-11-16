# CoMo: Learning Continuous Latent Motion from Internet Videos for Scalable Robot Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

시간 차분과 temporal contrastive 학습으로 연속 motion latent를 얻는다.

## Observation–State–Action Interface

인터넷 영상 → motion pseudo-label → robot policy 공동 학습.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 정적 배경 shortcut, reverse-video negative의 유효성, action-label 없이 가능한 범위.

Source가 명시한 evaluation 범위: Diffusion·autoregressive 정책의 simulation·실제 조작을 평가한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

Pseudo-label 생성 데이터와 policy 용량을 맞춰 discrete/continuous latent 후학습을 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_CoMo_Learning_Continuous_Latent_Motion_from_Internet_Videos_for_Scalable_CVPR_2026_paper.html) · [저자 project/code](https://github.com/MCG-NJU/CoMo). 수식·세부 구현·코드 실행은 미검증이다.
