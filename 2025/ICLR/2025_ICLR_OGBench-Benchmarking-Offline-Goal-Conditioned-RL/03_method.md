# OGBench: Benchmarking Offline Goal-Conditioned RL

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

다양한 goal-conditioned environment/dataset와 reference algorithm 구현을 제공하여 능력별 차이를 드러낸다.

## Observation–State–Action Interface

Offline transition data + goal → policy/action; unlabeled data에서의 goal-conditioned 학습을 평가한다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: Goal sampling, reward relabeling, split/dataset 품질과 성공률 aggregation.

Source가 명시한 evaluation 범위: ICLR abstract는 8종 환경, 85 datasets 및 6 reference algorithm을 보고한다. Task/split별 정확한 성공 정의는 본문 확인 필요.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 data budget으로 FQL/IQL 계열을 manipulation 및 maze task에서 비교하고 능력별 점수를 분리한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ecd92623ac899357312aaa8915853699-Abstract-Conference.html) · [저자 project/code](https://github.com/seohongpark/ogbench). 수식·세부 구현·코드 실행은 미검증이다.
