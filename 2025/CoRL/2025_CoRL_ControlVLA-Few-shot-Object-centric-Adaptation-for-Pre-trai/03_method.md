# ControlVLA: Few-shot Object-centric Adaptation for Pre-trained Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Zero-initialized projection을 가진 ControlNet 형태로 object-centric 조건을 주입한다.

## Observation–State–Action Interface

장면·객체 중심 표현 → 사전학습 VLA → 조작 행동.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 객체 mask 감독 비용, base model 학습 데이터, 표준·장기 task 구분.

Source가 명시한 evaluation 범위: 실제 조작과 새 객체·배경 및 long-horizon 확장을 평가한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

기본 SFT와 object-centric SFT를 먼저 맞춘 뒤 동일한 online RL budget을 적용한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v305/li25c.html) · [저자 project/code](https://controlvla.github.io/) · [공식 code](https://github.com/ControlVLA/ControlVLA). 수식·세부 구현·코드 실행은 미검증이다.
