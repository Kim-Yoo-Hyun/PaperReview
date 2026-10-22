# USER: A Unified and Extensible System for Online Real-World Policy Learning in Embodied AI

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Robot/GPU 추상화, adaptive communication 및 persistent buffer를 갖춘 asynchronous learning system을 제안한다.

## Observation–State–Action Interface

Robot observation/action/reward stream ↔ edge/cloud rollout·training workers ↔ policy weight synchronization.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: Weight version tagging, replay consistency, crash recovery와 실제 robot 시간 비용.

Source가 명시한 evaluation 범위: RSS abstract는 simulation과 실제 multi-robot·heterogeneous manipulator·edge-cloud·장기 비동기 학습 사례를 명시한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 policy와 robot task에서 sync/async 학습을 비교하고 policy lag·중단 복구·wall-clock learning·success를 기록한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://roboticsproceedings.org/rss22/p037.html) · [저자 project/code](https://github.com/RLinf/RLinf/blob/main/docs/source-zh/rst_source/resources/release_v0.3.rst). 수식·세부 구현·코드 실행은 미검증이다.
