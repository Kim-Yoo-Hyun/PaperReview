# DataMIL: Selecting Data for Robot Imitation Learning with Datamodels

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
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
- Source audit: 2026-10-25 공식 abstract와 publication metadata 및 명시된 project/code 공개 링크 확인. 본문 정독·코드 실행·payload 검증은 이번 등록 범위 밖이다.

## Problem and Importance

대규모 prior 데이터의 무차별 co-training이 개별 target task를 악화시킬 수 있다.

## Core Idea and Contribution

Datamodel로 policy 성능에 기여하는 데이터를 선택하며 task-specific surrogate로 선택 중 rollout 비용을 줄인다.

## Observation–State–Action Interface

Prior 시연·target 데이터·policy surrogate → subset → target imitation policy.

## Evaluation Scope and Claim Boundary

OXE 선택을 포함한 simulation 및 실로봇 manipulation 평가를 보고한다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/033d9e8dbbbc0ad90e59222cf1db0fc2-Abstract-Conference.html) · [저자 project/code](https://github.com/UT-Austin-RobIn/datamil). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

현재 proxy→target 데이터 전이 질문에서 반드시 대조할 performance-aware 선택 방법이다.

## Verification Boundary

surrogate 정의, target 데이터 누설, policy family 및 selector 비용을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
