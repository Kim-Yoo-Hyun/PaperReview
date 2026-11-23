# A Taxonomy for Evaluating Generalist Robot Manipulation Policies

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RA-L
- Authors: Jensen Gao, Suneel Belkhale, Sudeep Dasari, Ashwin Balakrishna, Dhruv Shah, Dorsa Sadigh
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Robotics, Benchmark, generalization, semantic-grounding
- Aliases: STAR-Gen, ★-Gen
- Official paper: https://arxiv.org/abs/2503.01238
- Venue verification: https://api.crossref.org/works/10.1109/LRA.2026.3656785
- Code/Project: https://stargen-taxonomy.github.io/
- Code: project_only
- Source audit: 2026-10-25 공식 abstract/서지정보 및 명시된 저자 링크 확인. 이번 노트는 abstract 기반이며 본문 전체·코드 실행·payload는 미검증이다. IEEE 페이지 접근 제한으로 publisher-deposited Crossref metadata와 저자 project·arXiv의 RA-L 표기를 대조했다. 본문은 정독하지 않았다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

이 연구는 로봇 조작 정책의 일반화를 시각·의미·행동 변화로 나누어 현재 평가에서 어떤 능력을 확인할 수 있는지 정리한다. [PDF 1쪽](https://arxiv.org/pdf/2503.01238v3#page=1)

## Core Idea and Contribution

- 물체나 장면이 달라지는 경우와 새로운 개념·행동이 필요한 경우를 구별하는 분류와 평가 설계 지침을 제시했다. [PDF 3쪽](https://arxiv.org/pdf/2503.01238v3#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2503.01238v3#page=4)
- Bridge V2와 ALOHA 2에 기반한 실물 사례에 지침을 적용해 정책의 의미 일반화가 취약한 조건을 분석했다. [PDF 6쪽](https://arxiv.org/pdf/2503.01238v3#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2503.01238v3#page=7)

## Observation–State–Action Interface

기본 과제 → 입력/필요 행동의 변화 축 → 축별 정책 평가.

## Evaluation Scope and Claim Boundary

Bridge V2 기반 정책과 ALOHA 2의 실로봇 사례를 비교한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2503.01238) · [저자 project/code](https://stargen-taxonomy.github.io/). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

VLA 일반화 주장을 시각 변화·언어 이해·행동 변화로 분해할 평가 formulation이다.

## Verification Boundary

각 축의 동시 변화, base competence, in-domain adaptation과 평가 분할을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
