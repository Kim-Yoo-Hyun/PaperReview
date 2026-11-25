# CoRE-VLA: Towards Scalable and Robust Vision-Language-Action Modeling via Conditional Routing of Experts

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / CoRL
- Authors: Haozhe Zhang, Sixian Li, Yifei Zhang, Zezheng Huai, Hao Chen, Chunhua Shen, Jingjing Gong, Xipeng Qiu
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, mixture of experts, depth, missing modality
- Aliases:
- Official paper: https://arxiv.org/abs/2607.03693
- Venue verification: https://www.corl.org/program/accepted-papers
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-10-21: official abstract / author project 확인. 5개 note는 abstract 기반이며 사용자 정독을 의미하지 않는다. arXiv v2 저자는 CoRL 2026 채택을 표기하지만 공식 proceedings 확인 전까지 arXiv로 등록. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

조건부 전문가 라우팅을 쓰는 CoRE-VLA는 센서 가용성과 작업 지시에 따라 행동 생성에 참여할 모듈을 고른다. [PDF 1쪽](https://arxiv.org/pdf/2607.03693v2#page=1)

## Core Idea and Contribution

- 사용 가능한 모달리티로 센서 전문가를 선택하고 과제 문맥으로 행동 전문가를 선택해 한 정책을 여러 조건에서 사용한다. [PDF 4쪽](https://arxiv.org/pdf/2607.03693v2#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2607.03693v2#page=5)
- 보조 센서로 깊이를 사용한 실험에서 깊이 입력이 빠지거나 열화될 때의 성능을 측정하고 실물 양팔 조작도 평가했다. [PDF 8쪽](https://arxiv.org/pdf/2607.03693v2#page=8) · [PDF 9쪽](https://arxiv.org/pdf/2607.03693v2#page=9)

## Observation–State–Action Interface

RGB·언어·proprioception·optional depth → action.

## Evaluation Scope and Claim Boundary

LIBERO, RoboCasa GR1, 실제 dual-arm 평가를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2607.03693) · 저자 프로젝트·코드 주소 미확인. 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

D1의 modality robustness와 직접 겹치는 NEXT다. 카메라 복원 CoRe-VLA와 다른 논문이다.

## Verification Boundary

v2 depth degradation 평가, availability indicator, 공식 CoRL 채택 확인을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
