# Universal Pose Pretraining for Generalizable Vision-Language-Action Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Camera-centric pose token으로 공간·trajectory 사전학습을 한 뒤 로봇 action space에 적응한다.

## Observation–State–Action Interface

3D pose·trajectory supervision으로 표현을 학습하고 embodiment별 행동을 출력한다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 3D 데이터 규모·pose supervision·camera convention·test object 중복.

Source가 명시한 evaluation 범위: 공식 초록은 RoboTwin 2.0·LIBERO 및 실세계 물체 일반화 실험을 명시한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

같은 robot demonstrations에서 pose pretraining 유무와 성공 head 공유 여부를 분리한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://roboticsproceedings.org/rss22/p145.html) · [저자 project/code](https://hetolin.github.io/PoseVLA/). 수식·세부 구현·코드 실행은 미검증이다.
