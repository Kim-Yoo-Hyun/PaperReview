# Scaling Verification Can Be More Effective than Scaling Policy Learning for Vision-Language-Action Alignment

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ECCV
- Authors: Jacky Kwok, Xilun Zhang, Mengdi Xu, Yuejiang Liu, Azalia Mirhoseini, Chelsea Finn, Marco Pavone
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: test-time-scaling, verification, instruction-following
- Aliases: CoVer, CoVer-VLA
- Official paper: https://arxiv.org/abs/2602.12281
- Venue verification: https://api.crossref.org/works/10.1007/978-3-032-37016-7_3
- Code/Project: https://cover-vla.github.io/
- Code: https://github.com/cover-vla/cover-vla
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

CoVer-VLA는 같은 의도를 여러 문장으로 표현하고 각 문장에서 행동을 여러 번 표집한 뒤, 지시와 행동의 일치도를 검증해 실행할 후보를 고른다. [PDF 1쪽](https://arxiv.org/pdf/2602.12281v2#page=1)

## Core Idea and Contribution

- 행동·지시 쌍을 구별하는 대조 검증기를 학습하고, 실행 시 상위 지시 선택과 하위 행동 묶음 선택에 이를 사용한다. [PDF 4쪽](https://arxiv.org/pdf/2602.12281v2#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2602.12281v2#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2602.12281v2#page=6)
- SIMPLER와 실물 조작에서 데이터를 기본 정책 학습과 검증기 학습에 각각 투입했을 때의 지시 이행을 비교했다. [PDF 8쪽](https://arxiv.org/pdf/2602.12281v2#page=8) · [PDF 9쪽](https://arxiv.org/pdf/2602.12281v2#page=9)

## Observation–State–Action Interface

VLM instruction rephrasing → VLA action candidates → verifier selection; 계층형 test-time pipeline.

## Evaluation Scope and Claim Boundary

SIMPLER·PolaRiS와 실로봇의 in/out-of-distribution 지시 실행을 평가한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2602.12281) · [저자 project/code](https://cover-vla.github.io/) · [공식 code](https://github.com/cover-vla/cover-vla). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

정책 RL 갱신의 필요성을 검증할 강한 추론 계산량·검증 대안이다.

## Verification Boundary

재표현의 의미 보존, verifier 감독량, rollout-independent evaluation을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
