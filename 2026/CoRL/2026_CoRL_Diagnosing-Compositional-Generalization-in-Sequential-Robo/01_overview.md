# Diagnosing Compositional Generalization in Sequential Robot Tasks

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Yixiao Wang, Cheng-En Wu, Lingfeng Sun, Pengcheng Wang, Xiang Ji, Boyuan Liang, Guojian Zhan, Masayoshi Tomizuka
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, imitation-learning, instruction-coverage, compositional-generalization
- Aliases:
- Official paper: https://arxiv.org/abs/2607.29687
- Venue verification: https://www.corl.org/program/accepted-papers
- Code/Project: https://yixiaowang7.github.io/Diagnosing_Compositional_Generalization_Robot_Page/
- Code: https://github.com/YixiaoWang7/Diagnosing_Compositional_Generalization_Robot
- Source audit: 2026-11-03 CoRL 공식 accepted list의 exact title와 OpenReview gQFYIM5dJy 연결을 확인해 기존 entry를 갱신했다. Spotlight는 별도로 승격하지 않는다. 분석은 11/01 확인한 arXiv v2(2026-10-15)·abstract/project 범위를 유지하며 conference final-text 동등성·정독·native 실행은 미확인이다. 기존 SET의 지정 본문/code 감사는 별도 source ledger를 따른다.

## Problem and Importance

순차 조작의 모든 지시 조합을 수집하기 어려울 때 어떤 training coverage가 새로운 조합에 필요한지 묻는다.

## Core Idea and Contribution

지시 marginal·지시 조합·context–action 변화를 분리하고, 데이터 coverage와 단계별 정책을 비교한다.

## Observation–State–Action Interface

시각 관측·로봇 상태·지시 → transformer flow-matching 조작 정책. 현재 연구의 frozen VLA와 동일 checkpoint 실험이 아니다.

## Evaluation Scope and Claim Boundary

Pick-and-place, 후속 버튼 조작, 의존적인 두 단계 조작에서 coverage와 분해를 비교한다. 저자 공개 code는 개선된 pipeline이라 release 결과와 논문 결과가 다를 수 있다고 명시한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2607.29687) · [저자 project/code](https://yixiaowang7.github.io/Diagnosing_Compositional_Generalization_Robot_Page/) · [공식 code](https://github.com/YixiaoWang7/Diagnosing_Compositional_Generalization_Robot). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

DataMIL·ReMix의 데이터 선택 흐름과 SET의 단순 분해를 연결할 instruction-coverage 선행이다. 분해 자체를 신규 기여로 주장하지 않고 학습 support를 따질 NEXT로 등록한다.

## Verification Boundary

v1/v2 차이, 단계별 정책의 입력과 전환 신호, 종속 지시의 정보 병목, demonstration 예산, 공개 release와 논문 설정의 차이을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
