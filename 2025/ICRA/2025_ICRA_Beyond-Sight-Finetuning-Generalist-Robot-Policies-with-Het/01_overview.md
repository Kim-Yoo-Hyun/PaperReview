# Beyond Sight: Finetuning Generalist Robot Policies with Heterogeneous Sensors via Language Grounding

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Joshua Jones, Oier Mees, Carmelo Sferrazza, Kyle Stachowicz, Pieter Abbeel, Sergey Levine
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, evaluation, generalization
- Aliases: FuSe
- Official paper: https://arxiv.org/abs/2501.04693
- Venue verification: https://api.crossref.org/works/10.1109/ICRA55743.2025.11127987
- Code/Project: https://fuse-model.github.io/
- Code: https://github.com/fuse-model/FuSe
- Source audit: 2026-10-25 공식 abstract와 publication metadata 및 명시된 project/code 공개 링크 확인. 본문 정독·코드 실행·payload 검증은 이번 등록 범위 밖이다. IEEE 페이지 challenge; IEEE가 기탁한 Crossref DOI metadata로 ICRA 2025를 확인했다.

## Problem and Importance

시각·proprio 중심 generalist policy에 적은 촉각·음향 데이터를 통합하기 어렵다.

## Core Idea and Contribution

Language grounding과 multimodal contrastive·language generation loss로 새 sensor 의미를 연결한다.

## Observation–State–Action Interface

Vision·touch·audio·언어 → generalist policy → 조작 action.

## Evaluation Scope and Claim Boundary

Diffusion generalist와 VLA의 실세계 manipulation 및 cross-modal prompting을 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2501.04693) · [저자 project/code](https://fuse-model.github.io/) · [공식 code](https://github.com/fuse-model/FuSe). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

새 sensor 결합을 연구할 때 naive finetuning·masked training과 함께 대조할 직접 기준이다.

## Verification Boundary

센서 동기화, 모달별 annotation 비용, 입력 결손과 추가 정보의 구별을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
