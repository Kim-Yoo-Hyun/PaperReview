# A Generalist Pair-wise Progress Critic Model for Vision-Language-Action Robots

> Evidence maturity: `ABSTRACT_CHECKED`. 요약·기여와 아래에 인용한 방법·평가를 원문에서 대조했다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ICML
- Authors: Qi Zhang, Shaopeng Zhai, Shengzhe Zhang, Litao Liu, Tianyi Zhang, Fuxian Huang, Ming Zhou
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, progress-critic, dense-reward, real-robot-RL
- Aliases: VLAC, A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning
- Official paper: https://proceedings.mlr.press/v306/zhang26if.html
- Venue verification: https://proceedings.mlr.press/v306/zhang26if.html
- Code/Project: https://github.com/InternRobotics/VLAC
- Code: https://github.com/InternRobotics/VLAC
- Source audit: 2026-11-25 게재본에서 아래에 인용한 요약·기여와 평가 조건을 대조했다. [평가 노트](./04_evaluation.md)

## Problem and Importance

실제 로봇에서 행동 생성과 과업 진행 판단을 함께 다루려는 연구다.

## Core Idea and Contribution

단일 autoregressive 구조로 행동과 두 시점 사이의 진행 차이를 예측하고, 진행 판단을 RL 보상에 사용한다.

## Observation–State–Action Interface

시각·언어 조건의 행동 출력과 관측 쌍에 대한 progress 출력.

## Evaluation Scope and Claim Boundary

게재본은 AGILE PiPER의 실물 RL과 진행도 예측을 평가했다. [평가 조건](./04_evaluation.md)

근거: [공식 paper/abstract](https://proceedings.mlr.press/v306/zhang26if.html) · [저자 project/code](https://github.com/InternRobotics/VLAC). 확인한 조건은 [평가 노트](./04_evaluation.md)에 기록했다.

## Why This Paper Is Here — Researcher Interpretation

단일 VLA의 행동/가치/보상을 구분할 직접 선행이다. U2의 구조 통합 주장을 제한하며 U1의 state-value와 다른 target을 제공하므로 NEXT에 추가한다.

## Verification Boundary

추가 확인 항목은 각 공개 가중치와 실물 실험의 정확한 대응 및 보상·종료 판정·PPO 가치 함수의 분리다. 2025 preprint 설정을 최종본에 전사하지 않는다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 공개 자료

- 코드 — 기존 VLAC의 행동 생성 사용례 · evo_vlac/examples/vla_example.py [배포 파일](https://raw.githubusercontent.com/InternRobotics/VLAC/0f302d020555e320347c55b09431afe17ef5cdd4/evo_vlac/examples/vla_example.py)
- 가중치·학습 파라미터 — 원 VLAC 행동·진행도 모델 · model.safetensors [배포 파일](https://huggingface.co/InternRobotics/VLAC/resolve/f44e552324944f80a63ab0083879f0bfafe01516/model.safetensors)
- 데이터 — 원 VLAC의 그릇 집기 진행도 추론 예제 영상 · evo_vlac/examples/videos/pick-bowl-test.mp4 [배포 파일](https://raw.githubusercontent.com/InternRobotics/VLAC/0f302d020555e320347c55b09431afe17ef5cdd4/evo_vlac/examples/videos/pick-bowl-test.mp4)

## 원문 대조

VLAC는 두 시점의 영상과 지시로 진행도 차이를 예측하면서 같은 자기회귀 모델로 로봇 행동도 생성한다. [게재본](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/zhang26if/zhang26if.pdf#page=4)

- 사람·로봇 궤적에서 진행도 감독을 구성하고 참조 시연을 조건으로 쓰는 평가를 포함한다. [원문](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/zhang26if/zhang26if.pdf#page=5)
- 실제 AGILE PiPER에서 진행도 출력을 보상으로 이용한 강화학습과 직접 행동 생성의 역할을 나눠 평가했다. [원문](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/zhang26if/zhang26if.pdf#page=7)

## 판본과 출처

이전 공개 자료 감사가 연결한 VLAC-Cut-Benchmark는 후속 모델의 데이터다. 원 VLAC에 해당하는 배포 근거는 추론 예제 영상까지다. [원문](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/zhang26if/zhang26if.pdf)
