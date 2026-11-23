# AutoEval: Autonomous Evaluation of Generalist Robot Manipulation Policies in the Real World

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / CoRL
- Authors: Zhiyuan Zhou, Pranav Atreya, You Liang Tan, Karl Pertsch, Sergey Levine
- Category: Benchmarks and Datasets
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: robot-evaluation, Benchmark, policy-comparison
- Aliases:
- Official paper: https://proceedings.mlr.press/v305/zhou25a.html
- Venue verification: https://proceedings.mlr.press/v305/zhou25a.html
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

AutoEval은 실제 로봇의 성공 검출과 장면 초기화를 자동화해 여러 일반 조작 정책을 같은 장면에서 반복 평가한다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/zhou25a/zhou25a.pdf#page=1)

## Core Idea and Contribution

- 평가 요청을 스케줄링하고 성공 분류기, 초기화 정책, 초기화 확인 절차를 결합해 다음 시행을 준비한다. [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/zhou25a/zhou25a.pdf#page=4) · [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/zhou25a/zhou25a.pdf#page=5)
- WidowX 기반 장면에서 자동 판정과 수작업 평가의 일치 및 사람의 개입 부담·평가 처리량을 측정했다. [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/zhou25a/zhou25a.pdf#page=7) · [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/zhou25a/zhou25a.pdf#page=8)

## Observation–State–Action Interface

Submitted policy → scene 실행/성공 판정/reset → 평가 결과.

## Evaluation Scope and Claim Boundary

WidowX/BridgeData 계열 실제 평가와 수동 판정을 비교한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v305/zhou25a.html). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

C5/C6의 reset ledger와 반복 평가를 설계할 핵심 system 기준이다.

## Verification Boundary

target start distribution, 자동 judge 오류, 제외 trial, human 비용을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
