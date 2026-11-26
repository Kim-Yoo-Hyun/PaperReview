# PEAfowl: Perception-Enhanced Multi-View Vision-Language-Action for Bimanual Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

깊이 분포 기반 3D lifting·cross-view 이웃 집계·text-aware readout을 사용하고 학습 시 depth distillation을 적용한다.

## Observation–State–Action Interface

여러 시점의 원시 RGB-D, 언어 지시와 로봇 관절 상태로 양팔 관절 궤적을 예측한다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 깊이 교사 정답 생성 비용과 새로운 시점·물체에서의 일반화.

Source가 명시한 evaluation 범위: RoboTwin2.0과 실제 양팔 조작을 평가한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 시점·데이터·depth supervision 예산에서 2D/3D 표현과 RL 유무를 교차 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://ieeexplore.ieee.org/document/11661761/) · [저자 project/code](https://peafowlvla.github.io/) · [공식 code](https://github.com/Qingyu-Fan/PEAfowl). 수식·세부 구현·코드 실행은 미검증이다.
