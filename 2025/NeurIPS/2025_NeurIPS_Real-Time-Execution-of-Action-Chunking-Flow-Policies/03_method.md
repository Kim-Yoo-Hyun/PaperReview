# Real-Time Execution of Action Chunking Flow Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

실행이 확정된 prefix를 보존하며 남은 action을 inpainting하는 비동기 추론을 사용한다.

## Observation–State–Action Interface

새 관측·이전 chunk·지연 → prefix 제약 → 다음 chunk.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: prefix 길이, delay estimate, inpainting cost, simulator와 VLA 범위.

Source가 명시한 evaluation 범위: Kinetix 실험과 실제 π0.5 양팔 평가를 구분해 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동기 실행과 RTC를 동일 checkpoint·latency injection·controller로 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://papers.nips.cc/paper_files/paper/2025/hash/300ccb2187dedd4edcc07f7e76d8e553-Abstract-Conference.html) · [저자 project/code](https://pi.website/research/real_time_chunking). 수식·세부 구현·코드 실행은 미검증이다.
