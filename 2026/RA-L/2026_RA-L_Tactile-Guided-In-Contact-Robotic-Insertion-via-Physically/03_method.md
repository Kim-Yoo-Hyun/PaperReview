# Tactile-Guided In-Contact Robotic Insertion via Physically Consistent Force-Array Representation Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

접촉 후 시연에서 힘 분포 표현을 관측하는 diffusion policy를 학습하고 합력·모멘트만 쓰는 경우와 대조한다.

## Observation–State–Action Interface

접촉 중의 촉각 입력을 삽입 동작으로 바꾼다. 센서 배열은 국소 하중의 분포를 보존한다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 센서 교정, 커넥터별 시행 수, 실물 분포 신호를 재현할 수 있는 범위.

Source가 명시한 evaluation 범위: IEEE 초록은 학습 분포 안에서 합력·모멘트만 쓴 변형이 약간 우세했고, 새 2·3핀과 USB·HDMI 커넥터 전이에서는 분포 표현이 유리했다고 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

커넥터별로 하중을 맞춘 뒤 합력·분포 입력의 성공과 최대 하중을 분리해 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://ieeexplore.ieee.org/document/11692602/). 수식·세부 구현·코드 실행은 미검증이다.
