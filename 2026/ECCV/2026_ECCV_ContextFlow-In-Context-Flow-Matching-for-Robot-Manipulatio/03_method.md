# ContextFlow: In-Context Flow Matching for Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

시연의 시각·proprioception·행동을 압축하는 perceiver와 in-context 조건부 flow matching을 결합한다.

## Observation–State–Action Interface

현재 관측과 demonstration context → continuous action flow; 새 context로 행동을 조건화한다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: context 길이·선정 비용, 미관측 task 정의, bimanual action 정규화.

Source가 명시한 evaluation 범위: LIBERO의 미관측 구성과 실제 단일팔·양팔 조작을 평가한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 정책 규모와 새 시연으로 context-only·gradient adaptation을 대조한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://link.springer.com/chapter/10.1007/978-3-032-37531-5_16) · [저자 project/code](https://dingjiansw101.github.io/contextflow-page/) · [공식 code](https://github.com/dingjiansw101/ContextFlow). 수식·세부 구현·코드 실행은 미검증이다.
