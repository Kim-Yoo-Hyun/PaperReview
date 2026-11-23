# FMB: A functional manipulation benchmark for generalizable robotic learning

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / IJRR
- Authors: Jianlan Luo, Charles Xu, Fangchen Liu, Liam Tan, Zipeng Lin, Jeffrey Wu, Pieter Abbeel, Sergey Levine
- Category: Manipulation, Contact, and Dexterity
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, Benchmark, assembly, skill-composition
- Aliases: FMB, Functional Manipulation Benchmark
- Official paper: https://api.crossref.org/works/10.1177/02783649241276017
- Venue verification: https://journals.sagepub.com/doi/full/10.1177/02783649241276017
- Code/Project: https://functional-manipulation-benchmark.github.io/
- Code: https://github.com/rail-berkeley/fmb
- Source audit: 2026-10-25 공식 abstract/서지정보 및 명시된 저자 링크 확인. 이번 노트는 abstract 기반이며 본문 전체·코드 실행·payload는 미검증이다. 공식 journal abstract와 서지정보·저자 project 확인. Online-first 2024-09-22, 권호 출판 2025를 구분해 registry year는 2025다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

FMB는 표준화한 부품으로 실제 로봇의 개별 조작 기술과 여러 기술이 이어지는 조립 성능을 평가한다. [PDF 1쪽](https://arxiv.org/pdf/2401.08553v3#page=1)

## Core Idea and Contribution

- 절차적으로 변형하고 3D 프린터로 제작할 수 있는 부품과 파지·재배치·삽입 등을 포함하는 실제 작업 및 시연 자료를 제공한다. [PDF 4쪽](https://arxiv.org/pdf/2401.08553v3#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2401.08553v3#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2401.08553v3#page=6)
- 기술 단위 정책의 실행과 여러 단계의 조립을 비교해 개별 기술의 성공이 긴 작업 전체의 완수를 보장하기 어려운 조건을 조사했다. [PDF 9쪽](https://arxiv.org/pdf/2401.08553v3#page=9) · [PDF 12쪽](https://arxiv.org/pdf/2401.08553v3#page=12)

## Observation–State–Action Interface

물체/로봇 관측 → grasp·reorientation·assembly skill → 다단계 조립.

## Evaluation Scope and Claim Boundary

실로봇의 개별 skill과 조합 과제를 평가하는 데이터·CAD·정책 자산을 제공한다.

근거: [공식 paper/abstract](https://journals.sagepub.com/doi/full/10.1177/02783649241276017) · [저자 project/code](https://functional-manipulation-benchmark.github.io/) · [공식 code](https://github.com/rail-berkeley/fmb). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

범용 pick-and-place 성능과 접촉 조립 능력을 구분할 benchmark를 보완한다.

## Verification Boundary

skill/전체 과제 성공 정의, object split, reset과 force/torque 접근을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
