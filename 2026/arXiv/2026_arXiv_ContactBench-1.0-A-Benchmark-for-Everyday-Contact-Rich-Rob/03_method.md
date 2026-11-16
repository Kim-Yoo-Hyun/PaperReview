# ContactBench 1.0: A Benchmark for Everyday Contact-Rich Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

접촉 skill taxonomy와 제작 가능한 물체·대응 simulation asset을 제공한다.

## Observation–State–Action Interface

물체·task variation → 실제/시뮬레이션 접촉 과제.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: task별 success 판정, asset version, 정책용 reset/step와 scripted helper 분리.

Source가 명시한 evaluation 범위: 36개 reference task 중 6개에서 vision-only와 visual-tactile 정책을 비교한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

한 task의 nominal/변형 asset에서 force-rule·motion-only·joint-gain 조건을 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2610.24512) · [저자 project/code](https://jingyi-xiang.github.io/contactbench/) · [공식 code](https://github.com/Michaelwyx/contactbench-sim). 수식·세부 구현·코드 실행은 미검증이다.
