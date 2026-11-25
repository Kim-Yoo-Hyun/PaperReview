# Decoupled Q-Chunking

> Evidence maturity: `ABSTRACT_CHECKED`. 개요 전반은 초록 수준이며, 아래 요약과 두 기여에는 확인한 본문 위치를 표시했다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ICLR
- Authors: Qiyang Li, Seohong Park, Sergey Levine
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: chunked-critic, reactivity, long-horizon
- Aliases: DQC
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/eafa5259d9eabb1b501592475dbc82dd-Abstract-Conference.html
- Venue verification: https://openreview.net/pdf/bde79a617f6c016e2c51c7771416933c0646102c.pdf
- Code/Project: https://github.com/ColinQiyangLi/dqc
- Code: https://github.com/ColinQiyangLi/dqc
- Source audit: 2026-11-23 요약과 핵심 기여 두 개를 원문 본문에 대조했다. 나머지 세부 분석은 기존 초록·공식 자료에 근거한다.

## Problem and Importance

Decoupled Q-Chunking은 가치 함수가 평가하는 긴 행동 묶음과 정책이 실행하는 짧은 묶음을 분리해 재관측과 장기 가치 전파를 양립시킨다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/eafa5259d9eabb1b501592475dbc82dd-Paper-Conference.pdf#page=1)

## Core Idea and Contribution

- 긴 행동 묶음의 가치에서 짧은 앞부분을 실행한 뒤 얻을 수 있는 가치를 추정해 별도 가치 함수로 증류한다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/eafa5259d9eabb1b501592475dbc82dd-Paper-Conference.pdf#page=1) · [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/eafa5259d9eabb1b501592475dbc82dd-Paper-Conference.pdf#page=4)
- OGBench 장기 목표 조건부 오프라인 과제에서 정책과 가치 함수의 묶음 길이가 성능에 주는 영향을 비교했다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/eafa5259d9eabb1b501592475dbc82dd-Paper-Conference.pdf#page=1) · [PDF 8쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/eafa5259d9eabb1b501592475dbc82dd-Paper-Conference.pdf#page=8)

## Observation–State–Action Interface

State → 짧은 actor action chunk; 긴 critic horizon을 통한 value 학습. 실제 controller frequency는 본문 확인 필요.

## Evaluation Scope and Claim Boundary

최종 paper의 abstract와 공식 code는 장기 offline goal-conditioned task 평가를 설명한다. 실제 로봇 contact 평가 여부는 확인 필요.

근거: [공식 paper/abstract](https://openreview.net/pdf/bde79a617f6c016e2c51c7771416933c0646102c.pdf) · [저자 project/code](https://github.com/ColinQiyangLi/dqc). 그 밖의 수치, 기준선의 비교 조건, 실패 범위는 별도 대조가 필요하다.

## Why This Paper Is Here — Researcher Interpretation

Current trend. Critic과 actor의 chunk 길이를 분리한다. Q-chunking의 value propagation 이점과 짧은 action horizon의 반응성 사이의 설계 문제를 직접 다룬다. 실제 contact feedback 성능으로의 확장은 본문/실험 확인이 필요하다.

## Verification Boundary

부분 chunk value 추정, policy extraction objective, reactive 평가의 실제 포함 여부을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 원문과 공개 자료

- 코드 — 분리된 행동 묶음의 오프라인 학습과 평가 · main.py [배포 파일](https://raw.githubusercontent.com/ColinQiyangLi/dqc/df898256a77f3594b54a7268bd5f89915981da35/main.py)
- 데이터 — 저자 실험 집계 자료 · exp_data/dqc-exp-data.pkl [배포 파일](https://raw.githubusercontent.com/ColinQiyangLi/dqc/df898256a77f3594b54a7268bd5f89915981da35/exp_data/dqc-exp-data.pkl)
