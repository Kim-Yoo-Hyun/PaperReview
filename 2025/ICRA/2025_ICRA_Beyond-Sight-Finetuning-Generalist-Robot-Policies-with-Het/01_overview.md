# Beyond Sight: Finetuning Generalist Robot Policies with Heterogeneous Sensors via Language Grounding

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / ICRA
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
- Source audit: 2026-10-25 공식 abstract와 publication metadata 및 명시된 project/code 공개 링크 확인. 본문 정독·코드 실행·payload 검증은 이번 등록 범위 밖이다. IEEE 페이지 challenge; IEEE가 기탁한 Crossref DOI metadata로 ICRA 2025를 확인했다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

FuSe는 로봇이 시각·촉각·소리에서 얻은 정보를 언어와 연결해 여러 감각을 요구하는 조작 지시에 따르도록 학습한다. [PDF 1쪽](https://arxiv.org/pdf/2501.04693v3#page=1)

## Core Idea and Contribution

- 감각과 문장의 대응을 학습하는 대조 손실과 관측의 감각적 특성을 문장으로 생성하는 목표를 결합한다. [PDF 2쪽](https://arxiv.org/pdf/2501.04693v3#page=2) · [PDF 3쪽](https://arxiv.org/pdf/2501.04693v3#page=3)
- 확산 기반 범용 정책과 VLA에 이 학습 방식을 적용해 실제 조작에서 감각 정보를 지정한 지시에 대한 반응을 비교했다. [PDF 4쪽](https://arxiv.org/pdf/2501.04693v3#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2501.04693v3#page=5)

## Observation–State–Action Interface

Vision·touch·audio·언어 → generalist policy → 조작 action.

## Evaluation Scope and Claim Boundary

Diffusion generalist와 VLA의 실세계 manipulation 및 cross-modal prompting을 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2501.04693) · [저자 project/code](https://fuse-model.github.io/) · [공식 code](https://github.com/fuse-model/FuSe). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

새 sensor 결합을 연구할 때 naive finetuning·masked training과 함께 대조할 직접 기준이다.

## Verification Boundary

센서 동기화, 모달별 annotation 비용, 입력 결손과 추가 정보의 구별을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
