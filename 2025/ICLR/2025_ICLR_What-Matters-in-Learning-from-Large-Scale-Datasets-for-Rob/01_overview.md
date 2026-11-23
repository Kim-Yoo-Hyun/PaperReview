# What Matters in Learning from Large-Scale Datasets for Robot Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
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
- Source audit: 2026-10-25 공식 abstract와 publication metadata 및 명시된 project/code 공개 링크 확인. 본문 정독·코드 실행·payload 검증은 이번 등록 범위 밖이다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

이 연구는 대규모 조작 시연의 어떤 다양성을 수집하고 어떤 시연을 검색해야 목표 과제의 모방 정책에 도움이 되는지 조사했다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/16466b6c95c5924784486ac5a3feeb65-Paper-Conference.pdf#page=1)

## Core Idea and Contribution

- MimicLabs에서 카메라 자세와 물체 배치 등을 조절해 데이터의 양과 구성을 분리한 비교를 만들었다. [PDF 3쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/16466b6c95c5924784486ac5a3feeb65-Paper-Conference.pdf#page=3) · [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/16466b6c95c5924784486ac5a3feeb65-Paper-Conference.pdf#page=4)
- 시점과 공간 배치가 수집·검색 성능에 주는 영향을 분석하고 실제 DROID 자료에서 목표에 맞는 시연을 골라 학습한 정책을 평가했다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/16466b6c95c5924784486ac5a3feeb65-Paper-Conference.pdf#page=1) · [PDF 8쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/16466b6c95c5924784486ac5a3feeb65-Paper-Conference.pdf#page=8)

## Observation–State–Action Interface

시연 집합과 target 조건 → 데이터 구성/선택 → manipulation policy.

## Evaluation Scope and Claim Boundary

시뮬레이션 구성 실험과 DROID를 이용한 실로봇 학습을 보고한다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2025/hash/16466b6c95c5924784486ac5a3feeb65-Abstract-Conference.html). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

단순 시각·공간 정렬로 설명되는 이득을 제거하기 위한 DataMIL·GAP-N1의 비교 기준이다.

## Verification Boundary

camera와 task 분할, retrieval의 target 접근, 동일 학습 예산을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
