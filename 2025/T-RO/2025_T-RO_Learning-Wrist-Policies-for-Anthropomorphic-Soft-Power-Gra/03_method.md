# Learning Wrist Policies for Anthropomorphic Soft Power Grasping in Handle and Door Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

손·팔을 하나의 임피던스 제어기로 다루며, 손목 임피던스와 손바닥·손가락 힘을 함께 조절하는 정책을 학습한다.

## Observation–State–Action Interface

손과 팔 기구의 제어 설정을 하나의 정책에서 정해 손잡이 잡기와 회전에 사용한다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 손의 구동 형태와 문 유형별 시험 조건 및 힘·속도 제어 기준선.

Source가 명시한 evaluation 범위: 시뮬레이션에서 학습하고 완전 구동 손과 부족 구동 손을 장착한 서비스 휴머노이드에서 손잡이·문 조작을 검증했다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

손잡이 초기 자세 오류를 독립적으로 바꿔 일정 손목 강성과 순응 정책의 손잡이 파지 유지율을 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://portal.fis.tum.de/en/publications/learning-wrist-policies-for-anthropomorphic-soft-power-grasping-i/). 수식·세부 구현·코드 실행은 미검증이다.
