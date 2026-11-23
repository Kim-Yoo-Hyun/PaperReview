# ReinFlow: Fine-tuning Flow Matching Policy with Online Reinforcement Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / NeurIPS
- Authors: Tonghe Zhang, Chao Yu, Sichang Su, Yu Wang
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: flow-matching, online-RL, policy-likelihood, manipulation, locomotion
- Aliases: ReinFlow
- Official paper: https://proceedings.neurips.cc/paper_files/paper/2025/hash/98d6f928497d9eaad9f320fb2db3040d-Abstract-Conference.html
- Venue verification: https://proceedings.neurips.cc/paper_files/paper/2025/hash/98d6f928497d9eaad9f320fb2db3040d-Abstract-Conference.html
- Code/Project: https://reinflow.github.io/
- Code: https://github.com/ReinFlow/ReinFlow
- Source audit: 2026-11-07: 공식 metadata/abstract·저자 project/README 확인. NeurIPS2025 공식 proceedings metadata/abstract와 저자 project/README 확인. 본문 전체·공개 구현 실행은 미확인. 사용자 reading status UNREAD 유지. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

ReinFlow는 연속 행동을 생성하는 흐름 맞춤 정책의 생성 경로에 학습 가능한 잡음을 넣어 온라인 강화학습으로 미세조정한다. [PDF 1쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/98d6f928497d9eaad9f320fb2db3040d-Paper-Conference.pdf#page=1)

## Core Idea and Contribution

- 결정적 흐름을 이산시간 확률 전이로 바꿔 적은 생성 단계에서도 경로 우도를 계산하고 정책 기울기 학습에 활용한다. [PDF 4쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/98d6f928497d9eaad9f320fb2db3040d-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/98d6f928497d9eaad9f320fb2db3040d-Paper-Conference.pdf#page=5) · [PDF 6쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/98d6f928497d9eaad9f320fb2db3040d-Paper-Conference.pdf#page=6)
- 보행과 조작 과제에서 Rectified Flow와 Shortcut Model을 미세조정하고 생성 단계 수에 따른 보상·성공률과 계산 비용을 비교했다. [PDF 8쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/98d6f928497d9eaad9f320fb2db3040d-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/98d6f928497d9eaad9f320fb2db3040d-Paper-Conference.pdf#page=9) · [PDF 10쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/98d6f928497d9eaad9f320fb2db3040d-Paper-Conference.pdf#page=10)

## Observation–State–Action Interface

관측 → flow velocity와 학습용 noise → 생성된 연속 행동. 정책 생성 과정의 확률과 물리 행동의 주변 밀도를 구분해 읽어야 한다.

## Evaluation Scope and Claim Boundary

공식 abstract는 locomotion과 state/visual manipulation에서 Rectified Flow·Shortcut 정책 후학습을 보고한다. 최신 저장소의 VLA 지원을 원 논문 실험으로 소급하지 않는다.

근거: [공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2025/hash/98d6f928497d9eaad9f320fb2db3040d-Abstract-Conference.html) · [저자 project/code](https://reinflow.github.io/) · [공식 code](https://github.com/ReinFlow/ReinFlow). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

PPO·Flow Matching·DPPO를 로봇 flow-policy online RL로 연결하는 비교 방법. 단순 noise 학습을 새 VLA RL 기여로 주장하기 전에 읽어야 한다.

## Verification Boundary

생성 경로 likelihood와 action likelihood의 차이, DPPO 비교의 모델/자료/시간 통제, noise 학습과 step 축소 효과, 실제 로봇 평가 여부을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
