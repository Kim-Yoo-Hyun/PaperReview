# Learning Neural Network Policies with Guided Policy Search under Unknown Dynamics

> Evidence maturity: `FULL_TEXT_CHECKED`.
> 2026-11-20 게재본의 표제면·방법·평가 절 대조. [게재 정보](https://proceedings.neurips.cc/paper_files/paper/2014/hash/c7c9344b5a3c0533e29fa69ce807cf08-Abstract.html) · [원문](https://proceedings.neurips.cc/paper_files/paper/2014/file/c7c9344b5a3c0533e29fa69ce807cf08-Paper.pdf)

- Year/Venue: 2014 / NeurIPS
- Authors: Sergey Levine, Pieter Abbeel
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: Robotics, guided policy search, policy learning, manipulation
- Official paper: https://proceedings.neurips.cc/paper_files/paper/2014/hash/c7c9344b5a3c0533e29fa69ce807cf08-Abstract.html
- Code/Project: https://rll.berkeley.edu/nips2014gps/

## Why This Paper Is Here

전역 동역학 모델이 없는 연속 제어에서, 궤적 주변의 시변 선형 모델로 국소 제어기를 학습하고 그 행동을 신경망 정책에 전달한다.

## Main Claims and Actual Contribution

- 수집한 궤적 주변에서 시변 선형 동역학을 반복 적합한다. 이를 이용해 국소 선형 가우시안 제어기의 궤적 분포를 최적화하고, guided policy search로 여러 초기 조건을 처리하는 신경망 정책을 훈련한다. 훈련 중의 상태 정보와 실행 시 정책에 주어지는 관측을 구분한다. pp. 2–5.
- 시뮬레이션에서 삽입, 수영 등 비선형 제어를 비교한다. 그림 1은 궤적 제어기, 그림 2는 신경망 정책에서의 표본 수와 과제별 거리 지표를 비교한다. 그림 2의 삽입 과제에서는 슬롯 위치가 정책에 직접 주어지지 않는다. pp. 6–8.

## Evaluation Scope

물리 시뮬레이션의 접촉·부분관측에서 얻은 결과다. 실제 로봇에서 영상으로 병뚜껑을 조이는 실험은 별개 논문에 속한다.
