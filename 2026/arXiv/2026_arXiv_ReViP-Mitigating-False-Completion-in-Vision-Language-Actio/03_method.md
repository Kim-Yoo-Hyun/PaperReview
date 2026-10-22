# ReViP: Mitigating False Completion in Vision-Language-Action Models with Vision-Proprioception Rebalance

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

시각적 task-stage cue로 vision–proprioception 결합을 조정한다.

## Observation–State–Action Interface

영상·언어·state와 stage cue → corrective action.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: arXiv v3와 최신 project 방법 차이, observer latency, 공개 코드.

Source가 명시한 evaluation 범위: Object Drop, Distractor Swap, Relayout 및 robot manipulation 평가를 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

물체 이동과 카메라 오류를 구분하여 동일 observer 예산으로 평가한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2601.16667) · [저자 project/code](https://isee-laboratory.github.io/ReViP/). 수식·세부 구현·코드 실행은 미검증이다.
