# SPACE: Enabling Learning from Cross-Robot Data Toward Generalist Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Cartesian state delta를 예측하고 action adapter로 robot command로 변환한다.

## Observation–State–Action Interface

관측 → EEF state displacement → robot-specific adapter → 제어 명령.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: state delta 계산, adapter supervision, online 적응 자료, 실제 시간.

Source가 명시한 evaluation 범위: Embodiment·동일 기종 개체·frequency/payload/gain 변화 평가를 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 Cartesian displacement에서 direct command와 adapter를 비교하고 gain/frequency를 통제한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2606.24049) · [저자 project/code](https://haeone.site/space-website/). 수식·세부 구현·코드 실행은 미검증이다.
