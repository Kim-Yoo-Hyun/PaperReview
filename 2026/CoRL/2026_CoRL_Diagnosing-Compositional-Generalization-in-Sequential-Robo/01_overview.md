# Diagnosing Compositional Generalization in Sequential Robot Tasks

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / CoRL
- Authors: Yixiao Wang, Cheng-En Wu, Lingfeng Sun, Pengcheng Wang, Xiang Ji, Boyuan Liang, Guojian Zhan, Masayoshi Tomizuka
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: sequential-manipulation, Imitation Learning, instruction-coverage, compositional-generalization
- Aliases:
- Official paper: https://arxiv.org/abs/2607.29687
- Venue verification: https://www.corl.org/program/accepted-papers
- Code/Project: https://yixiaowang7.github.io/Diagnosing_Compositional_Generalization_Robot_Page/
- Code: https://github.com/YixiaoWang7/Diagnosing_Compositional_Generalization_Robot
- Source audit: 2026-11-03 CoRL 공식 accepted list의 exact title와 OpenReview gQFYIM5dJy 연결을 확인해 기존 entry를 갱신했다. Spotlight는 별도로 승격하지 않는다. 분석은 11/01 확인한 arXiv v2(2026-10-15)·abstract/project 범위를 유지하며 conference final-text 동등성·정독·native 실행은 미확인이다. 기존 SET의 지정 본문/code 감사는 별도 source ledger를 따른다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

이 연구는 순차 로봇 과제의 일반화 실패가 새로운 지시 조합, 개별 지시의 분포, 상태와 행동의 관계 중 어디서 오는지 구분한다. [PDF 1쪽](https://arxiv.org/pdf/2607.29687v2#page=1)

## Core Idea and Contribution

- 훈련에서 바뀌는 지시의 빈도와 조합, 특정 상황에서 선택한 행동의 관계를 나누는 통제 실험을 설계했다. [PDF 3쪽](https://arxiv.org/pdf/2607.29687v2#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2607.29687v2#page=4)
- 조합을 모두 보여주지 않아도 과제 구조를 이용할 수 있는 경우와 드문 상황에서 이미 배운 기술을 잘못 선택하는 경우를 구별했다. [PDF 5쪽](https://arxiv.org/pdf/2607.29687v2#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2607.29687v2#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2607.29687v2#page=7)

## Observation–State–Action Interface

시각 관측·로봇 상태·지시 → transformer flow-matching 조작 정책. 현재 연구의 frozen VLA와 동일 checkpoint 실험이 아니다.

## Evaluation Scope and Claim Boundary

Pick-and-place, 후속 버튼 조작, 의존적인 두 단계 조작에서 coverage와 분해를 비교한다. 저자 공개 code는 개선된 pipeline이라 release 결과와 논문 결과가 다를 수 있다고 명시한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2607.29687) · [저자 project/code](https://yixiaowang7.github.io/Diagnosing_Compositional_Generalization_Robot_Page/) · [공식 code](https://github.com/YixiaoWang7/Diagnosing_Compositional_Generalization_Robot). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

DataMIL·ReMix의 데이터 선택 흐름과 SET의 단순 분해를 연결할 instruction-coverage 선행이다. 분해 자체를 신규 기여로 주장하지 않고 학습 support를 따질 NEXT로 등록한다.

## Verification Boundary

v1/v2 차이, 단계별 정책의 입력과 전환 신호, 종속 지시의 정보 병목, demonstration 예산, 공개 release와 논문 설정의 차이을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 공개 자료

- 코드 — 조합 일반화 통제 실험의 자료 준비 · projects/corl2026_cg/src/corl2026_cg/data/prepare.py [배포 파일](https://raw.githubusercontent.com/YixiaoWang7/Diagnosing_Compositional_Generalization_Robot/e29c44474495b341d19636bbf90f3cf0fcb1d2d2/projects/corl2026_cg/src/corl2026_cg/data/prepare.py)
- 데이터 — L4 단일 단계 조건의 훈련 궤적 · cross_into_bin/shards/shard_000.hdf5 [배포 파일](https://huggingface.co/datasets/yixiiiiii/cg_l4_1s/resolve/fabafb6e97e559af8c16d8dd06d09801beb3ddaa/cross_into_bin/shards/shard_000.hdf5)
