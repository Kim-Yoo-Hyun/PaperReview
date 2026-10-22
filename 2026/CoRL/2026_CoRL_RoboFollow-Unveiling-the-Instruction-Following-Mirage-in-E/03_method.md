# RoboFollow: Unveiling the Instruction Following Mirage in Embodied Agents

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

같은 scene의 여러 지시 등으로 instruction following을 단계별 평가한다.

## Observation–State–Action Interface

Scene·다양한 instruction → policy rollout → intent/execution 판정.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: scene entropy, evaluator oracle, task infeasibility, real-robot coverage.

Source가 명시한 evaluation 범위: Simulation benchmark와 제한된 실제 검증을 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 scene·task 능력에서 지시만 바꿔 순응·실행 성공을 별도 측정한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://openreview.net/forum?id=A9AQjk3dAt) · [저자 project/code](https://github.com/AutoLab-SAI-SJTU/RoboFollow). 수식·세부 구현·코드 실행은 미검증이다.
