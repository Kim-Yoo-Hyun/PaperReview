# RehearseVLA: Simulated Post-Training for VLAs with Physically-Consistent World Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

물리 일관성을 지향한 world simulator와 보상·종료를 판단하는 VLM reflector를 구성한다.

## Observation–State–Action Interface

행동 → 미래 영상 예측 → 보상·종료 판단 → VLA 후학습.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 실제/가상 rollout 분모, 물리 일관성 검증, reflector의 감독 비용, 종료 오탐.

Source가 명시한 evaluation 범위: 소수 시연 조건의 복잡한 로봇 조작 개선을 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

같은 시연으로 world-model RL·추가 모방·종료 모듈만 적용한 정책을 각각 실제 환경에서 평가한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Xiao_RehearseVLA_Simulated_Post-Training_for_VLAs_with_Physically-Consistent_World_Model_CVPR_2026_paper.html) · [저자 project/code](https://github.com/iSEE-Laboratory/RehearseVLA). 수식·세부 구현·코드 실행은 미검증이다.
