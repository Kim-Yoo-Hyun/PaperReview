# PoseIt: A Visual-Tactile Dataset of Holding Poses for Grasp Stability Analysis

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

집기·자세 이동·흔들기 전 과정의 시각과 촉각 관측을 수집하고 다중 모달 시계열 분류기를 비교한다.

## Observation–State–Action Interface

RGB-D, 손가락 촉각, 힘·토크와 로봇 상태가 자세별 안정성 예측의 입력이다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 물체 분할, 파지 명령이 변경된 시점과 단계별 실패 라벨의 의미.

Source가 명시한 evaluation 범위: 저자 자료는 26개 물체의 실물 기록을 제공하며 초록은 미관측 물체와 자세에 대한 예측을 평가한다. 자세 이동 중 실패와 마지막 흔들기 결과는 별개다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

물체를 분리한 검증에서 이동 중 실패와 흔들기 실패를 나누고 같은 힘 예산의 단순 대조를 포함한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://ieeexplore.ieee.org/document/9981562/) · [저자 project/code](https://publish.illinois.edu/robotouch/poseit-a-visual-tactile-dataset-of-holding-poses-for-grasp-stability-analysis/) · [공식 code](https://github.com/Robo-Touch/PoseIt). 수식·세부 구현·코드 실행은 미검증이다.
