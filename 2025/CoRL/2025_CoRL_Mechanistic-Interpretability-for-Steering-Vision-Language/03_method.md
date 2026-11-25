# Mechanistic Interpretability for Steering Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Transformer activation의 semantic 방향을 찾고 inference 때 activation steering으로 행동을 조절한다.

## Observation–State–Action Interface

VLA 내부 activation·semantic 방향 → 개입된 action.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 방향 추출 데이터, 개입 강도, 속도와 성공의 trade-off.

Source가 명시한 evaluation 범위: LIBERO-Long 시뮬레이션에서 OpenVLA-7B를, 실물 UR5의 두 집기·놓기 과제에서 π0-FAST를 평가했다. [시뮬레이션 · PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/haon25a/haon25a.pdf#page=6) · [실물 · PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/haon25a/haon25a.pdf#page=7)

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 checkpoint에서 semantic·random direction의 task/control 변화를 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v305/haon25a.html). 수식·세부 구현·코드 실행은 미검증이다.
