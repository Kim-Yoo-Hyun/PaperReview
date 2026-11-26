# VoLo: A Physical Orchestrator for Open-Vocabulary Long-Horizon Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`. 아래에 쪽수를 붙인 문장을 원문과 대조했다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / CoRL
- Authors: Siyi Chen, Hugo Hadfield, Alex Zook, Mikaela Angelina Uy, Chan Hee Song, Erwin Coumans, Xuning Yang, Faisal Ladhak, Qing Qu, Stan Birchfield, Jonathan Tremblay, Valts Blukis
- Category: Planning and Long-Horizon Reasoning
- Primary track: Planning and control
- Tier: REFERENCE
- Tags: Planning, language, execution, VLA, failure recovery
- Aliases:
- Official paper: https://arxiv.org/abs/2606.07723
- Full-text retrieval: https://arxiv.org/pdf/2606.07723v1
- Venue verification: https://www.corl.org/program/accepted-papers
- Code/Project: https://chicychen.github.io/VoLo/
- Code: https://github.com/NVlabs/VoLoAgent
- Source audit: 2026-11-24에 한 줄 요약과 핵심 기여 두 개를 아래 PDF 쪽수에 대조했다.

## Problem and Importance

VoLoAgent는 시각언어모형이 로봇 정책과 인식·동작 도구를 호출하고 실행 중에도 진행을 감시해 장기 조작의 계획을 바꿀 수 있게 한다. [PDF 1쪽](https://arxiv.org/pdf/2606.07723v1#page=1)

## Core Idea and Contribution

- 열린 어휘 지시를 갖는 RoboVoLo 벤치마크를 구성하고 하위 정책의 실행을 중단·재지시할 수 있는 인터페이스를 제시했다. [PDF 4쪽](https://arxiv.org/pdf/2606.07723v1#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2606.07723v1#page=5)
- 시뮬레이션에서 작업 성공과 실패 단계를 분석하고 실물 과제에서 진행 감시와 실패 복구를 시험했다. [PDF 6쪽](https://arxiv.org/pdf/2606.07723v1#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2606.07723v1#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2606.07723v1#page=8) · [PDF 9쪽](https://arxiv.org/pdf/2606.07723v1#page=9)

## Observation–State–Action Interface

언어·영상·도구 결과 → skill 호출/중단 → action.

## Evaluation Scope and Claim Boundary

RoboVoLo와 실제 open-vocabulary long-horizon manipulation 평가를 보고한다.

근거: [공식 paper/abstract](https://openreview.net/forum?id=sF3YZbbTNX) · [저자 project/code](https://chicychen.github.io/VoLo/). 추가 수치와 실패 조건은 해당 실험의 표·설정을 확인해야 한다.

## 검색 태그 근거

VoLo의 감독 VLM이 도구 결과와 장면을 보고 다음 행동 호출·중단·복구를 정한다. 저수준 VLA와 파지·배치 도구를 선택해 사용하며, RoboVoLo와 실물 장기 조작에서 진행 감시를 평가한다. [원문 5쪽](https://arxiv.org/pdf/2606.07723v1#page=5) · [원문 8쪽](https://arxiv.org/pdf/2606.07723v1#page=8)

## Why This Paper Is Here — Researcher Interpretation

D3에서 단순 switching 방법과 추가 도구 정보의 효과를 구분할 기준이다.

## Verification Boundary

tool별 privileged input, interrupt semantics, checkpoint·evaluator 공개을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
