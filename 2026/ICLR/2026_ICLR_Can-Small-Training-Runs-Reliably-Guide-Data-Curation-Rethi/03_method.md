# Can Small Training Runs Reliably Guide Data Curation? Rethinking Proxy-Model Practice

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Data-dependent tuning에 따라 순위가 바뀌는 문제를 분석하고 작은 learning rate를 쓰는 평가 보정을 제안한다.

## Observation–State–Action Interface

Data recipe·proxy 학습 설정 → 상대 loss 순위; 로봇 행동 평가는 아니다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 이론 적용 범위, loss와 task success 차이, tuning 총비용.

Source가 명시한 evaluation 범위: LLM pretraining recipe와 random-feature model 이론을 다룬다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 정보의 proxy에서 LR 민감도를 먼저 확인하고 이후 cue 조건을 바꾼다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/c7d04ce5e71efdfc7a4a78f7161238a9-Abstract-Conference.html). 수식·세부 구현·코드 실행은 미검증이다.
