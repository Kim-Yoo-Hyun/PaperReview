# Mobi-π: Mobilizing Your Robot Learning Policy

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

정책을 다시 학습하는 대신 실행할 base pose를 찾는 policy mobilization을 정식화한다. 3D Gaussian Splatting의 새 시점 영상, pose 적합도와 sampling 기반 최적화를 연결한다.

## Observation–State–Action Interface

현재 장면과 사전 학습 조작 정책의 데이터 → 장면 표현·후보 pose 점수 → 조작을 시작할 base pose → 기존 정책 실행.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: pose 후보와 collision/reachability 처리, 정책별 학습 시야와 데이터 접근, 장면 구축 비용, 실제 도착 상태·평가 분모.

Source가 명시한 evaluation 범위: RoboCasa 기반 simulated mobile manipulation과 실로봇에서 pose 선택을 비교한다. 이 비교만으로 다른 정책에 선택된 pose를 재사용할 때의 성능을 확정할 수 없다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 scene·도착 후보·navigation·비용에서 A 선택 재사용, 정책 무관 고정 pose, 제한된 B validation 재선택을 비교한다. 실제 이동 후 상태를 분기하고 전체 시도 분모를 보존한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v305/yang25b.html) · [저자 project/code](https://mobipi.github.io/) · [공식 code](https://github.com/yjy0625/mobipi). 수식·세부 구현·코드 실행은 미검증이다.
