# MolmoSpaces: Large-Scale Open Ecosystem for Robot Manipulation and Navigation

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Authors: Yejin Kim, Wilbert Pumacay, Omar Rayyan, Max Argus, Winson Han, Eli VanderBilt, Jordi Salvador, Abhay Deshpande, Rose Hendrix, Snehal Jauhri, Shuo Liu, Nur Muhammad Mahi Shafiullah, Maya Guru, Arjun Guru, Ainaz Eftekhar, Karen Farley, Donovan Clay, Jiafei Duan, Piper Wolters, Alvaro Herrasti, Ying-Chun Lee, Georgia Chalvatzaki, Yuchen Cui, Ali Farhadi, Dieter Fox, Ranjay Krishna
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Benchmark, Dataset, manipulation, Navigation
- Aliases: MolmoSpaces, MolmoSpaces: A Large-Scale Open Ecosystem for Robot Navigation and Manipulation
- Official paper: https://roboticsproceedings.org/rss22/p091.html
- Venue verification: https://roboticsproceedings.org/rss22/p091.html
- Code/Project: https://github.com/allenai/molmospaces
- Code: https://github.com/allenai/molmospaces
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인. RSS title와 arXiv의 navigation/manipulation 순서가 다르지만 같은 연구다. Simulator-agnostic assets와 모든 backend의 실행 지원을 구분한다. 본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

MolmoSpaces는 실내 이동·고정형 및 이동 조작 정책을 다양한 장면과 물체에 걸쳐 평가할 수 있는 시뮬레이션 환경과 벤치마크를 제공한다. [PDF 1쪽](https://roboticsproceedings.org/rss22/p091.pdf#page=1)

## Core Idea and Contribution

- 절차 생성 실내 공간과 물체·파지 주석을 여러 물리 엔진에서 이용할 수 있는 공통 자원으로 구성했다. [PDF 3쪽](https://roboticsproceedings.org/rss22/p091.pdf#page=3) · [PDF 4쪽](https://roboticsproceedings.org/rss22/p091.pdf#page=4) · [PDF 5쪽](https://roboticsproceedings.org/rss22/p091.pdf#page=5)
- MolmoSpaces-Bench에서 시뮬레이션과 실물의 정책 순위를 비교하고 지시 표현·초기 관절 자세·카메라 가림에 따른 민감도를 측정했다. [PDF 6쪽](https://roboticsproceedings.org/rss22/p091.pdf#page=6) · [PDF 7쪽](https://roboticsproceedings.org/rss22/p091.pdf#page=7) · [PDF 8쪽](https://roboticsproceedings.org/rss22/p091.pdf#page=8)

## Observation–State–Action Interface

장면·객체·로봇 설정 → simulator 기반 조작·항법 과제.

## Evaluation Scope and Claim Boundary

조작·항법을 포함한 8개 benchmark task와 sim-to-real 상관을 보고한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p091.html) · [저자 project/code](https://github.com/allenai/molmospaces). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

현재 후보의 한 benchmark 의존을 줄일 추가 환경·데이터 자원이다.

## Verification Boundary

asset license, 실제 지원 simulator별 기능, 장면 split, 정책별 co-training 여부을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 공개 자료

- 코드 — 시뮬레이션 문 열기 과제의 계획기 · molmo_spaces/policy/solvers/opening_solver.py [배포 파일](https://raw.githubusercontent.com/allenai/molmospaces/67acef9a17bb8212a18aadfc8f62ff6171d84891/molmo_spaces/policy/solvers/opening_solver.py)
- 데이터 — Isaac용 iTHOR 시뮬레이션 장면 자산 · isaac/scenes/ithor/20260121/shards/00000.tar [배포 파일](https://huggingface.co/datasets/allenai/molmospaces/resolve/5f802a46816ffc3520e59b5ef49fa8dafee8eeca/isaac/scenes/ithor/20260121/shards/00000.tar)

## 판본과 출처

저자 표기·순서는 표제면 기준이다. [표제면](https://www.roboticsproceedings.org/rss22/p091.pdf#page=1)
