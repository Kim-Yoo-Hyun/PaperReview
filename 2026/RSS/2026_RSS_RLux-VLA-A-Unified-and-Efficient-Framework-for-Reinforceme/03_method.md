# RLinf-VLA: A Unified and Efficient Framework for Reinforcement Learning of Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

VLA/RL/simulator 공통 interface와 rendering·inference·training 자원 할당 구조를 제공한다.

## Observation–State–Action Interface

Simulator observation/reward → VLA rollout → training worker; resource allocation과 policy interface를 분리한다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: Model별 action interface, GPU utilization 산정, asynchronous policy lag.

Source가 명시한 evaluation 범위: RSS abstract는 LIBERO, ManiSkill, RoboTwin simulation에서 training efficiency와 policy 성능을 비교한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 policy/algorithm/task에서 scheduling만 바꾸고 samples/sec·wall-clock time·고정 step 성공률을 보고한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p089.html) · [저자 project/code](https://github.com/RLinf/RLinf/blob/main/docs/source-zh/rst_source/resources/release_v0.3.rst). 수식·세부 구현·코드 실행은 미검증이다.
