# ReinFlow: Fine-tuning Flow Matching Policy with Online Reinforcement Learning

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / NeurIPS
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: flow-matching, online-RL, policy-likelihood, manipulation, locomotion
- Aliases: ReinFlow
- Official paper: https://proceedings.neurips.cc/paper_files/paper/2025/hash/98d6f928497d9eaad9f320fb2db3040d-Abstract-Conference.html
- Venue verification: https://proceedings.neurips.cc/paper_files/paper/2025/hash/98d6f928497d9eaad9f320fb2db3040d-Abstract-Conference.html
- Code/Project: https://reinflow.github.io/
- Code: https://github.com/ReinFlow/ReinFlow
- Source audit: 2026-11-07: 공식 metadata/abstract·저자 project/README 확인. NeurIPS2025 공식 proceedings metadata/abstract와 저자 project/README 확인. 본문 전체·공개 구현 실행은 미확인. 사용자 reading status UNREAD 유지.

## Problem and Importance

결정론적 flow 생성 경로를 online policy-gradient 학습과 탐색에 연결할 때 확률 계산과 적은 생성 step의 안정성이 필요하다.

## Core Idea and Contribution

Flow 경로에 학습 가능한 잡음을 넣어 이산 시간 확률 과정으로 바꾸고 정책 likelihood를 사용해 online RL 후학습한다.

## Observation–State–Action Interface

관측 → flow velocity와 학습용 noise → 생성된 연속 행동. 정책 생성 과정의 확률과 물리 행동의 주변 밀도를 구분해 읽어야 한다.

## Evaluation Scope and Claim Boundary

공식 abstract는 locomotion과 state/visual manipulation에서 Rectified Flow·Shortcut 정책 후학습을 보고한다. 최신 저장소의 VLA 지원을 원 논문 실험으로 소급하지 않는다.

근거: [공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2025/hash/98d6f928497d9eaad9f320fb2db3040d-Abstract-Conference.html) · [저자 project/code](https://reinflow.github.io/) · [공식 code](https://github.com/ReinFlow/ReinFlow). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

PPO·Flow Matching·DPPO를 로봇 flow-policy online RL로 연결하는 비교 방법. 단순 noise 학습을 새 VLA RL 기여로 주장하기 전에 읽어야 한다.

## Verification Boundary

생성 경로 likelihood와 action likelihood의 차이, DPPO 비교의 모델/자료/시간 통제, noise 학습과 step 축소 효과, 실제 로봇 평가 여부을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
