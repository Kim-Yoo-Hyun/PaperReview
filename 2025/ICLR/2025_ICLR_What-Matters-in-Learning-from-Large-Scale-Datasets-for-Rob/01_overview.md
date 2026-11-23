# What Matters in Learning from Large-Scale Datasets for Robot Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / ICLR
- Authors: Vaibhav Saxena, Matthew Bronars, Nadun Ranawaka Arachchige, Kuancheng Wang, Woo Shin, Soroush Nasiriany, Ajay Mandlekar, Danfei Xu
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, evaluation, data-selection
- Aliases:
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2025/hash/16466b6c95c5924784486ac5a3feeb65-Abstract-Conference.html
- Venue verification: https://proceedings.iclr.cc/paper_files/paper/2025/hash/16466b6c95c5924784486ac5a3feeb65-Abstract-Conference.html
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-10-25 공식 abstract와 publication metadata 및 명시된 project/code 공개 링크 확인. 본문 정독·코드 실행·payload 검증은 이번 등록 범위 밖이다.

## Problem and Importance

다양한 robot demonstration을 늘릴 때 어떤 다양성을 수집하고 어떤 데이터를 조회해야 하는지 불명확하다.

## Core Idea and Contribution

통제 가능한 데이터 생성으로 카메라·물체·배치 다양성과 retrieval 정렬을 비교한다.

## Observation–State–Action Interface

시연 집합과 target 조건 → 데이터 구성/선택 → manipulation policy.

## Evaluation Scope and Claim Boundary

시뮬레이션 구성 실험과 DROID를 이용한 실로봇 학습을 보고한다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2025/hash/16466b6c95c5924784486ac5a3feeb65-Abstract-Conference.html). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

단순 시각·공간 정렬로 설명되는 이득을 제거하기 위한 DataMIL·GAP-N1의 비교 기준이다.

## Verification Boundary

camera와 task 분할, retrieval의 target 접근, 동일 학습 예산을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
