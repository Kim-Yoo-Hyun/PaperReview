# KinDER: A Physical Reasoning Benchmark for Robot Learning and Planning

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Authors: Yixuan Huang, Bowen Li, Vaibhav Saxena, Yichao Liang, Utkarsh Aashu Mishra, Liang Ji, Lihan Zha, Jimmy Wu, Nishanth Kumar, Sebastian Scherer, Danfei Xu, Tom Silver
- Category: Planning and Long-Horizon Reasoning
- Primary track: Planning and control
- Tier: NEXT
- Tags: Benchmark, physical-reasoning, Planning, manipulation
- Aliases: KinDER
- Official paper: https://roboticsproceedings.org/rss22/p184.html
- Venue verification: https://roboticsproceedings.org/rss22/p184.html
- Code/Project: https://prpl-group.com/kinder-site/
- Code: https://github.com/Princeton-Robot-Planning-and-Learning/kindergarden
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인. RSS와 최신 arXiv의 baseline 수가 다르므로 원 논문·후속 버전을 구별한다. 본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

KinDER는 로봇이 지각이나 언어 인식의 어려움과 분리해 기구학·동역학적 제약을 고려하는지를 평가한다. [PDF 1쪽](https://roboticsproceedings.org/rss22/p184.pdf#page=1)

## Core Idea and Contribution

- 공간 관계·비파지 다물체 조작·도구 사용·조합적 기하 제약·동역학 제약을 분리하는 절차 생성 환경과 공통 평가 절차를 제공한다. [PDF 2쪽](https://roboticsproceedings.org/rss22/p184.pdf#page=2) · [PDF 4쪽](https://roboticsproceedings.org/rss22/p184.pdf#page=4) · [PDF 5쪽](https://roboticsproceedings.org/rss22/p184.pdf#page=5)
- 계획·모방·강화학습·기반 모델 계열 기준선을 비교하고 모바일 조작기의 실물 검증에서 시뮬레이션과 대응하는 물리 상호작용을 조사했다. [PDF 6쪽](https://roboticsproceedings.org/rss22/p184.pdf#page=6) · [PDF 7쪽](https://roboticsproceedings.org/rss22/p184.pdf#page=7) · [PDF 8쪽](https://roboticsproceedings.org/rss22/p184.pdf#page=8)

## Observation–State–Action Interface

기하·동역학 제약 → 계획 또는 학습된 행동 → 물리적 결과.

## Evaluation Scope and Claim Boundary

다양한 planning·IL·RL baseline 및 mobile manipulator 대응 실험을 보고한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p184.html) · [저자 project/code](https://prpl-group.com/kinder-site/) · [공식 code](https://github.com/Princeton-Robot-Planning-and-Learning/kindergarden). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

VLA의 실패가 언어 표현 문제인지 물리적 의사결정 문제인지 진단할 자원이다.

## Verification Boundary

skill 호출 권한, 관측 특권, baseline별 compute, 절차적 split을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
