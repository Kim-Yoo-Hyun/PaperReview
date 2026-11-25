# SPACE: Enabling Learning from Cross-Robot Data Toward Generalist Policies

> Evidence maturity: `ABSTRACT_CHECKED`. 아래의 요약·기여는 인용한 원문 쪽에서 추가 대조했다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Authors: Haeone Lee, Byeongguk Jeon, Suchae Jeong, Jian Kim, Kimin Lee
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, action-interface, cross-embodiment
- Aliases:
- Official paper: https://arxiv.org/abs/2606.24049
- Venue verification: https://arxiv.org/abs/2606.24049
- Code/Project: https://haeone.site/space-website/
- Code: project_only
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다.

## Problem and Importance

SPACE는 서로 다른 로봇에서 관측된 작업 공간의 상태 변화를 공통 행동 목표로 학습한다. [PDF 3쪽](https://arxiv.org/pdf/2606.24049v1#page=3)

## Core Idea and Contribution

- 공통 좌표계에서 다음 상태 변화를 예측하고 기체별 실행기가 필요한 제어 명령으로 변환한다. [PDF 4쪽](https://arxiv.org/pdf/2606.24049v1#page=4)
- 서로 다른 팔과 휴대형 시연 수집 장치의 자료를 함께 썼을 때 실물 조작을 비교했다. [PDF 6쪽](https://arxiv.org/pdf/2606.24049v1#page=6)

## Observation–State–Action Interface

관측 → EEF state displacement → robot-specific adapter → 제어 명령.

## Evaluation Scope and Claim Boundary

Embodiment·동일 기종 개체·frequency/payload/gain 변화 평가를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2606.24049) · [저자 project/code](https://haeone.site/space-website/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

E1/E2에서 정상적인 state-effect 표현과 dynamics adapter의 강한 대안이다.

## Verification Boundary

state delta 계산, adapter supervision, online 적응 자료, 실제 시간을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
