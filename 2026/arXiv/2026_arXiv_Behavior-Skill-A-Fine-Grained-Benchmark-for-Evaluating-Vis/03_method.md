# Behavior-Skill: A Fine-Grained Benchmark for Evaluating Vision-Language-Action Policies in Long-Horizon Tasks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

시연을 실행 가능한 skill로 나누고 instruction·observation/action segment·복원 가능한 중간 상태·skill 성공 조건을 연결하여 개별 skill 평가를 지원한다.

## Observation–State–Action Interface

Skill instruction와 복원된 시작 상태의 관측 → VLA action → skill 성공 판단 및 trajectory/skill 단위 지표.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 공개 release와 논문 정책 쌍의 일치, 시연 reset과 continuation의 차이, 학습/평가 instance 분리, normalizer와 controller·queue·종료 정의.

Source가 명시한 evaluation 범위: 50개 household task의 시연으로 구성한 benchmark에서 π0.5와 GR00T 등 정책을 평가한다. 복원된 유효 시작 상태의 개별 능력은 이전 정책이 실제 도달한 상태에서의 연결 실행 성능과 구분한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

같은 task·정책·success checker에서 시연 복원 시작과 실제 navigation 도착 시작을 비교하고, 정책 교체·도착 설정·reset 차이를 분리한다. 현재 P0는 실행 준비 단계이며 실측 효과가 없다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2608.30536) · [저자 project/code](https://github.com/nubot-nudt/Behavior-Skill). 수식·세부 구현·코드 실행은 미검증이다.
