# CAST: Counterfactual Labels Improve Instruction Following in Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

VLM 기반 counterfactual 라벨과 대응 행동 자료로 기존 robot dataset의 지시·행동 다양성을 늘려 언어 추종을 학습한다.

## Observation–State–Action Interface

기존 trajectory와 counterfactual instruction/action 자료 → VLA 학습 → navigation 또는 manipulation 행동. 실제 수행된 실패의 hindsight 라벨과 합성 counterfactual을 구분한다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 합성 행동의 물리적 유효성, 원 데이터/평가 중복, language와 action 증강 기여 분리, 공개 모델/자료의 논문 version 대응.

Source가 명시한 evaluation 범위: v2 abstract는 실내외 3개 navigation 환경과 distractor가 있는 manipulation의 instruction following을 평가한다고 보고한다. 정확한 trial·split·수치는 본문 확인 필요다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

같은 관측별 원 지시·단순 paraphrase·counterfactual 지시/행동을 구분하고 계산량을 맞춰 새 명령 성공과 distractor 오선택을 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2508.13446) · [저자 project/code](https://cast-vla.github.io/) · [공식 code](https://github.com/catglossop/CAST). 수식·세부 구현·코드 실행은 미검증이다.
