# Learning from Hindsight for VLA Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

VLM으로 실패에서 달성한 행동을 보조 언어 목표로 붙이고 원 과제와 함께 정책을 학습한다.

## Observation–State–Action Interface

관측·원 지시 → VLA 행동; 수집 후 rollout을 VLM이 해석하여 보조 목표와 학습 신호를 만든다. 배포 제어기와 학습 relabeler를 구분한다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: v2의 importance correction·label filtering·모방 대조와 우리 selector의 정확한 차이, VLM 감독 비용과 rollout 분모, 원 지시 평가 독립성.

Source가 명시한 evaluation 범위: v2 abstract는 LIBERO-PRO의 분포 이동 조작과 실제 Franka 학습을 보고한다. 샘플 효율 개선은 해당 비교 조건의 저자 주장이다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

먼저 자연적으로 참인 관련/비관련 목표가 같은 실패에서 발생하는지 확인한다. 이후 고정 pool에서 균등·객체 일치·원 목표만 학습을 대조한다. 현재 주제의 P0/P1/P2 계약은 별도이며 이 노트는 실험 결과가 아니다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2607.09042) · [저자 project/code](https://iamxjy.github.io/lfh-website/). 수식·세부 구현·코드 실행은 미검증이다.
