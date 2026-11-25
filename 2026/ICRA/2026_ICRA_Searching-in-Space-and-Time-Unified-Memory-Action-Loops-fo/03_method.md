# Searching in Space and Time: Unified Memory-Action Loops for Open-World Object Retrieval

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

장기 기억과 작업 기억을 이용해 과거 기록 조회와 물리적 탐색 중 다음 행동을 선택한다.

## Observation–State–Action Interface

공간·시간 표현이 포함된 지시와 관측 이력으로 기억 조회·탐색 행동을 선택한다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 실물과 시뮬레이션의 과제 수, 기억 관측 주체, 대상 이동 빈도.

Source가 명시한 evaluation 범위: 저자는 STARBench와 Tiago 실기에서 비교했다. 프로젝트의 360개 과제는 3개 아파트와 3개 과제군을 포함한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 초기 위치와 후보 지도를 사용하고 이동·조회 비용과 최초 회수 성공을 기록한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://ieeexplore.ieee.org/document/11696368/) · [저자 project/code](https://amrl.cs.utexas.edu/STAR/) · [공식 code](https://github.com/ut-amrl/STARBench). 수식·세부 구현·코드 실행은 미검증이다.
