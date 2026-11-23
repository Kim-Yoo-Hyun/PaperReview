# Real-World Reinforcement Learning of Active Perception Behaviors

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / NeurIPS
- Authors: Edward Hu, Jie Wang, Xingfang Yuan, Fiona Luo, Muyao Li, Gaspard Lambrechts, Oleh Rybkin, Dinesh Jayaraman
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: active perception, real-world RL, privileged value, partial observability
- Aliases: AAWR
- Official paper: https://papers.neurips.cc/paper_files/paper/2025/hash/aa1b1a959c80086cba61d0fd66de412f-Abstract-Conference.html
- Venue verification: https://papers.neurips.cc/paper_files/paper/2025/hash/aa1b1a959c80086cba61d0fd66de412f-Abstract-Conference.html
- Code/Project: https://penn-pal-lab.github.io/aawr/
- Code: https://github.com/penn-pal-lab/aawr
- Source audit: 2026-11-18: 공식 초록·bibliographic record와 연결된 저자 자료 확인. Abstract 기반 등록이며 본문 전체·실험 재현은 미확인. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

AAWR은 학습 때만 이용할 수 있는 추가 센서로 가치 함수를 훈련해, 실행 때에는 로봇이 스스로 부족한 정보를 얻는 행동을 배우게 한다. [PDF 1쪽](https://papers.neurips.cc/paper_files/paper/2025/file/aa1b1a959c80086cba61d0fd66de412f-Paper-Conference.pdf#page=1)

## Core Idea and Contribution

- 추가 관측으로 추정한 어드밴티지를 이용해 제한된 관측만 받는 정책을 갱신하며 소량 시연과 초기 정책으로 실물 학습을 시작한다. [PDF 4쪽](https://papers.neurips.cc/paper_files/paper/2025/file/aa1b1a959c80086cba61d0fd66de412f-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://papers.neurips.cc/paper_files/paper/2025/file/aa1b1a959c80086cba61d0fd66de412f-Paper-Conference.pdf#page=5)
- 세 로봇의 여덟 가지 부분 관측 조작 과제에서 능동 지각 행동과 성공률을 측정하고 추가 센서 없는 학습 및 시연 모방과 비교했다. [PDF 7쪽](https://papers.neurips.cc/paper_files/paper/2025/file/aa1b1a959c80086cba61d0fd66de412f-Paper-Conference.pdf#page=7) · [PDF 8쪽](https://papers.neurips.cc/paper_files/paper/2025/file/aa1b1a959c80086cba61d0fd66de412f-Paper-Conference.pdf#page=8)

## Observation–State–Action Interface

훈련 critic의 privileged 정보와 배포 actor의 제한된 관측을 구분하는 AAWR이다.

## Evaluation Scope and Claim Boundary

공식 초록은 3개 로봇·8개 조작 과제 및 generalist 초기 정책의 능동 관측 개선을 명시한다.

근거: [공식 paper/abstract](https://papers.neurips.cc/paper_files/paper/2025/hash/aa1b1a959c80086cba61d0fd66de412f-Abstract-Conference.html) · [저자 project/code](https://penn-pal-lab.github.io/aawr/). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

VLA+RL로 관측 행동을 만든다는 넓은 주장을 제한하는 핵심 실세계 기준이다.

## Verification Boundary

추가 센서 접근·초기 demonstrations·advantage 추정·배포 observation을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
