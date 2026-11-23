# VoLo: A Physical Orchestrator for Open-Vocabulary Long-Horizon Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / CoRL
- Authors: Siyi Chen, Hugo Hadfield, Alex Zook, Mikaela Angelina Uy, Chan Hee Song, Erwin Coumans, Xuning Yang, Faisal Ladhak, Qing Qu, Stan Birchfield, Jonathan Tremblay, Valts Blukis
- Category: Planning and Long-Horizon Reasoning
- Primary track: Planning and control
- Tier: REFERENCE
- Tags: Planning, language, execution
- Aliases:
- Official paper: https://arxiv.org/abs/2606.07723
- Venue verification: https://www.corl.org/program/accepted-papers
- Code/Project: https://chicychen.github.io/VoLo/
- Code: https://github.com/NVlabs/VoLoAgent
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다. 공식 OpenReview 검색 API의 Conference venueid·CoRL 2026 Poster를 확인했다.

## Problem and Importance

다양한 저수준 도구를 long-horizon 언어 계획에 연결한다.

## Core Idea and Contribution

VLM orchestrator가 interruptible VLA/WAM·perception/action 도구를 조정한다.

## Observation–State–Action Interface

언어·영상·도구 결과 → skill 호출/중단 → action.

## Evaluation Scope and Claim Boundary

RoboVoLo와 실제 open-vocabulary long-horizon manipulation 평가를 보고한다.

근거: [공식 paper/abstract](https://openreview.net/forum?id=sF3YZbbTNX) · [저자 project/code](https://chicychen.github.io/VoLo/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

D3에서 단순 switching 방법과 추가 도구 정보의 효과를 구분할 기준이다.

## Verification Boundary

tool별 privileged input, interrupt semantics, checkpoint·evaluator 공개을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
