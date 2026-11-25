# InsertAnything: Generalizable Contact-Rich Precision Insertion from Simulation to Reality

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

시뮬레이션에서 정렬과 삽입을 나누어 보상하고 손끝 힘을 이용해 접촉 뒤의 수정 동작을 학습한다.

## Observation–State–Action Interface

목표 자세와 3차원 손끝 힘이 입력이며 정책은 삽입을 위한 움직임을 출력한다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 형상별 시행 수, 목표 자세의 취득 방식과 사람 개입 범위.

Source가 명시한 evaluation 범위: 저자는 실제 여러 형상에서 최소 공칭 간극 0.02 mm를 다뤘다. ManipulationNet의 20/20은 사람 개입을 허용한 프로토콜이며 다른 실험의 자율 지표와 구별한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일한 초기 오차에서 고정 하강과 힘 조건부 동작을 비교하며 최대 힘과 손을 뗀 뒤 안착을 함께 기록한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2609.24511) · [저자 project/code](https://mzhsoul.github.io/InsertAnything/) · [공식 code](https://github.com/mzhsoul/InsertAnything). 수식·세부 구현·코드 실행은 미검증이다.
