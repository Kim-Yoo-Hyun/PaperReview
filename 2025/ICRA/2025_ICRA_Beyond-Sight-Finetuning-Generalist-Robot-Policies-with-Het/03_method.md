# Beyond Sight: Finetuning Generalist Robot Policies with Heterogeneous Sensors via Language Grounding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Language grounding과 multimodal contrastive·language generation loss로 새 sensor 의미를 연결한다.

## Observation–State–Action Interface

Vision·touch·audio·언어 → generalist policy → 조작 action.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 센서 동기화, 모달별 annotation 비용, 입력 결손과 추가 정보의 구별.

Source가 명시한 evaluation 범위: Diffusion generalist와 VLA의 실세계 manipulation 및 cross-modal prompting을 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

같은 데이터로 naive finetuning·masked training·FuSe를 가림 조건별 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2501.04693) · [저자 project/code](https://fuse-model.github.io/) · [공식 code](https://github.com/fuse-model/FuSe). 수식·세부 구현·코드 실행은 미검증이다.
