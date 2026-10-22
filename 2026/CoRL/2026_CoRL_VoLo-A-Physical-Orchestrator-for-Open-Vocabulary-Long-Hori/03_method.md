# VoLo: A Physical Orchestrator for Open-Vocabulary Long-Horizon Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

VLM orchestrator가 interruptible VLA/WAM·perception/action 도구를 조정한다.

## Observation–State–Action Interface

언어·영상·도구 결과 → skill 호출/중단 → action.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: tool별 privileged input, interrupt semantics, checkpoint·evaluator 공개.

Source가 명시한 evaluation 범위: RoboVoLo와 실제 open-vocabulary long-horizon manipulation 평가를 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

도구·skill 능력을 고정하고 정적 계획과 event 기반 중단을 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://openreview.net/forum?id=sF3YZbbTNX) · [저자 project/code](https://chicychen.github.io/VoLo/). 수식·세부 구현·코드 실행은 미검증이다.
