# Contact-Anchored Policies: Contact Conditioning Creates Strong Robot Utility Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Contact point로 조건화한 modular utility policies와 EgoGym 반복 평가를 제안한다.

## Observation–State–Action Interface

접촉 anchor·관측 → skill action; language-conditioned VLA 자체는 아니다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: anchor 획득 비용, embodiment split, 실제 checkpoint release.

Source가 명시한 evaluation 범위: Pick/Open/Close와 새 환경·embodiment 평가를 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

GT contact anchor와 추정 anchor를 분리하고 동일 정보의 VLA와 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p141.html) · [저자 project/code](https://cap-policy.github.io/). 수식·세부 구현·코드 실행은 미검증이다.
