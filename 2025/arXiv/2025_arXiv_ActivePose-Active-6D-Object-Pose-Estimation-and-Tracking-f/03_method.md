# ActivePose: Active 6D Object Pose Estimation and Tracking for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

CAD virtual view와 FoundationPose 기반 정보로 VLM이 모호성을 평가하고 다음 camera view를 선택한다.

## Observation–State–Action Interface

RGB 관측·CAD 기반 가상 시점 → ambiguity score·NBV·pose tracking으로 이어진다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: VLM score calibration·CAD render 조건·물리 camera 비용·task success 기준.

Source가 명시한 evaluation 범위: 공식 초록은 로봇 조작을 위한 active pose estimation/tracking을 다룬다. Task별 성공률과 camera 이동 비용은 본문 확인 필요다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

같은 후보 시점과 pose estimator에서 pose uncertainty와 성공 tolerance의 중단 판단을 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2509.11364). 수식·세부 구현·코드 실행은 미검증이다.
