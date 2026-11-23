# DataMIL: Selecting Data for Robot Imitation Learning with Datamodels

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ICLR
- Authors: Shivin Dass, Alaa Khaddaj, Logan Engstrom, Aleksander Madry, Andrew Ilyas, Roberto Martín-Martín
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, evaluation, data-selection
- Aliases:
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/033d9e8dbbbc0ad90e59222cf1db0fc2-Abstract-Conference.html
- Venue verification: https://proceedings.iclr.cc/paper_files/paper/2026/hash/033d9e8dbbbc0ad90e59222cf1db0fc2-Abstract-Conference.html
- Code/Project: https://github.com/UT-Austin-RobIn/datamil
- Code: https://github.com/UT-Austin-RobIn/datamil
- Source audit: 2026-10-25 공식 abstract와 publication metadata 및 명시된 project/code 공개 링크 확인. 본문 정독·코드 실행·payload 검증은 이번 등록 범위 밖이다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

DataMIL은 기존 로봇 자료 중에서 목표 과제의 모방 정책 성능에 도움이 될 시연을 추정해 공동 학습에 사용한다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/033d9e8dbbbc0ad90e59222cf1db0fc2-Paper-Conference.pdf#page=1)

## Core Idea and Contribution

- 데이터 부분집합과 정책 성능의 관계를 모델링하고 실물 실행을 반복할 필요가 없도록 목표 과제 자료에서 대리 손실을 계산한다. [PDF 3쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/033d9e8dbbbc0ad90e59222cf1db0fc2-Paper-Conference.pdf#page=3) · [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/033d9e8dbbbc0ad90e59222cf1db0fc2-Paper-Conference.pdf#page=5) · [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/033d9e8dbbbc0ad90e59222cf1db0fc2-Paper-Conference.pdf#page=6)
- 시뮬레이션과 실물 조작에서 선별한 자료로 학습할 때의 성공률을 비교하고 Open X-Embodiment 자료에도 적용했다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/033d9e8dbbbc0ad90e59222cf1db0fc2-Paper-Conference.pdf#page=1) · [PDF 7쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/033d9e8dbbbc0ad90e59222cf1db0fc2-Paper-Conference.pdf#page=7)

## Observation–State–Action Interface

Prior 시연·target 데이터·policy surrogate → subset → target imitation policy.

## Evaluation Scope and Claim Boundary

OXE 선택을 포함한 simulation 및 실로봇 manipulation 평가를 보고한다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/033d9e8dbbbc0ad90e59222cf1db0fc2-Abstract-Conference.html) · [저자 project/code](https://github.com/UT-Austin-RobIn/datamil). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

현재 proxy→target 데이터 전이 질문에서 반드시 대조할 performance-aware 선택 방법이다.

## Verification Boundary

surrogate 정의, target 데이터 누설, policy family 및 selector 비용을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
