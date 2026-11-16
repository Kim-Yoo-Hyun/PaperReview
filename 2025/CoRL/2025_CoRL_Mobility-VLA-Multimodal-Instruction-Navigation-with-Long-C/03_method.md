# Mobility VLA: Multimodal Instruction Navigation with Long-Context VLMs and Topological Graphs

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

장문맥 VLM의 goal-frame 선택과 topological graph 기반 하위 navigation을 결합한다.

## Observation–State–Action Interface

tour video·multimodal instruction → goal frame → graph/low-level policy → 이동 action.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: tour/graph 구축 비용, goal 후보 접근, online 관측과 planner timing.

Source가 명시한 evaluation 범위: 기록된 tour를 제공한 실환경의 multimodal instruction navigation을 평가한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

같은 graph/controller에서 retrieval과 VLM goal selection만 바꾸어 평가한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v270/xu25b.html). 수식·세부 구현·코드 실행은 미검증이다.
