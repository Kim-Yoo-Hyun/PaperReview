# Long-Context Robot Imitation Learning by Focusing on Key History Frames

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

VLM이 선택한 소수의 의미 있는 keyframe으로 정책 history를 압축한다.

## Observation–State–Action Interface

관측 이력 → 의미 keyframe → history-conditioned 로봇 행동.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: VLM 호출 비용, event 검출의 미래 정보 누출, history 길이별 평가.

Source가 명시한 evaluation 범위: 기억이 필요한 실제 조작과 simulation 과제를 평가한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

추가 distractor history와 실패 후 회복 이력을 넣고 균일·최근·의미 keyframe을 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://roboticsproceedings.org/rss22/p201.html). 수식·세부 구현·코드 실행은 미검증이다.
