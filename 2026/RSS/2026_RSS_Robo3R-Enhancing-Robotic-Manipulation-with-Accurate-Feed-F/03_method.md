# Robo3R: Enhancing Robotic Manipulation with Accurate Feed-Forward 3D Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

RGB와 robot state에서 local geometry·camera pose를 추정하고 robot frame의 metric geometry로 정렬한다.

## Observation–State–Action Interface

RGB/로봇 상태 → point map·camera pose·robot-frame scene geometry; 별도 downstream policy에 전달한다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: Robot state privilege·similarity transform·훈련 물체 중복·latency.

Source가 명시한 evaluation 범위: Robo3R-4M 합성 데이터로 학습하고 imitation·sim-to-real·grasp synthesis·collision-free planning의 downstream 효과를 평가한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

같은 policy와 RGB에서 local shape·scale·extrinsic 오류를 독립적으로 주입한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://roboticsproceedings.org/rss22/p056.html) · [저자 project/code](https://yangsizhe.github.io/robo3r/). 수식·세부 구현·코드 실행은 미검증이다.
