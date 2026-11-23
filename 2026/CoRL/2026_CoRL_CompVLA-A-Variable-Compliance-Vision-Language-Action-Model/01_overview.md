# CompVLA: A Variable Compliance Vision-Language-Action Model for Contact-rich Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / CoRL
- Authors: Jongmin Kim, Junsu Ha, Che-Sang Park, Minchang Song, Hyeokju Jeong, Himchan Hwang, Jianlong Fu, Frank C. Park
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, variable-impedance, contact, flow-matching
- Aliases: CompVLA
- Official paper: https://arxiv.org/abs/2609.23614
- Venue verification: https://www.corl.org/program/accepted-papers
- Code/Project: https://compvla.github.io/
- Code: not_identified
- Source audit: 2026-11-09: official abstract/project 및 metadata 확인. 최신 v2(2026-11-06) abstract 확인. 기존 N1 본문 대조는 v1이며 v2 본문을 확인한 것으로 승격하지 않는다. 저자 CoRL 2026 표기는 공식 승인 근거 미확인. Code 링크 404. 새 5-note는 abstract 기반이며 전체 본문/실행/사용자 정독을 뜻하지 않는다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

CompVLA는 접촉 조작에서 로봇이 움직일 방향과 외력에 얼마나 순응할지를 영상과 언어 지시에서 함께 예측한다. [PDF 1쪽](https://arxiv.org/pdf/2609.23614v2#page=1)

## Core Idea and Contribution

- 순응도를 담당하는 모듈이 시간에 따라 달라지는 축별 강성과 가상 변위를 내보내며 기하학적 임피던스 제어기가 이를 실행한다. [PDF 4쪽](https://arxiv.org/pdf/2609.23614v2#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2609.23614v2#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2609.23614v2#page=6)
- 실제 접촉 과제에서 고정 강성 및 다른 순응 제어 기준선과 비교하고 강성 추정·순응 모듈을 바꾼 실험으로 각각의 영향을 살폈다. [PDF 8쪽](https://arxiv.org/pdf/2609.23614v2#page=8) · [PDF 9쪽](https://arxiv.org/pdf/2609.23614v2#page=9)

## Observation–State–Action Interface

RGB·언어 → 동작과 시변 강성 행렬.

## Evaluation Scope and Claim Boundary

접촉 과제에서 vanilla/compliance-aware VLA 및 구성요소 ablation을 비교한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2609.23614) · [저자 project/code](https://compvla.github.io/). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

강성 출력을 VLA에 추가하는 것 자체의 신규성을 배제할 직접 선행이다.

## Verification Boundary

강성–displacement 식별성, force 입력 유무, 데이터·controller 공정성을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
