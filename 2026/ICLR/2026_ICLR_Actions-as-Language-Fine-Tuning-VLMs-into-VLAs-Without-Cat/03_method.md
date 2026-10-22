# Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

자연어로 low-level action을 표현하고 parameter-efficient adaptation을 사용한다.

## Observation–State–Action Interface

영상·언어 → 언어형 action 표현 → robot 명령.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: action decoding, LoRA 범위, VQA/robot split과 robot controller.

Source가 명시한 evaluation 범위: Robot manipulation과 VQA 능력 보존을 함께 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

같은 데이터·backbone으로 VQA 보존과 instruction-conditioned 성공률을 따로 측정한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/7a0f8055c838df8e62329a76c7c6403d-Abstract-Conference.html). 수식·세부 구현·코드 실행은 미검증이다.
