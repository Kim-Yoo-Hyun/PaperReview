# DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

소수 인간 시연을 재사용해 시뮬레이션의 양팔 dexterous trajectory를 생성한다.

## Observation–State–Action Interface

source demonstration·새 초기 상태 → 합성 trajectory → imitation policy.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: object-state/segmentation 접근, source-target task 대응, 생성 실패 및 sim-to-real 비용.

Source가 명시한 evaluation 범위: 양팔 조작 simulation과 real2sim2real 사례를 제시한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

원본 시연 수를 고정하고 reset 다양성과 양팔 동기화 조건별 실패를 분리한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2410.24185) · [저자 project/code](https://dexmimicgen.github.io/) · [공식 code](https://github.com/NVlabs/dexmimicgen). 수식·세부 구현·코드 실행은 미검증이다.
