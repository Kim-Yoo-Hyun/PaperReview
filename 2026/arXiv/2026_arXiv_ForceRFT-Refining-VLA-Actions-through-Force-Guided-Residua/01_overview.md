# ForceRFT: Refining VLA Actions through Force-Guided Residual Reinforcement Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Authors: Yichen Wang, Chaoyang Zhang, Xuqi Su, Jun Ma, Haiyue Zhu, Xiaocong Li
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, residual-RL, force-feedback, contact
- Aliases: ForceRFT
- Official paper: https://arxiv.org/abs/2609.22840
- Venue verification: https://arxiv.org/abs/2609.22840
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-11-09: official abstract/project 및 metadata 확인. v1 abstract 확인. 공식 code/project는 이번 확인에서 식별하지 못했다. 새 5-note는 abstract 기반이며 전체 본문/실행/사용자 정독을 뜻하지 않는다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

ForceRFT는 고정한 VLA가 행동 묶음을 실행하는 도중 손목에서 새로 측정한 힘·토크로 말단 자세를 매 단계 보정한다. [PDF 1쪽](https://arxiv.org/pdf/2609.22840v1#page=1)

## Core Idea and Contribution

- 사람이 수정한 행동으로 잔차 정책을 지도하고, 자율 실행 구간 안에서만 가치 표적을 이어 계산해 같은 정책을 강화학습으로 개선한다. [PDF 3쪽](https://arxiv.org/pdf/2609.22840v1#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2609.22840v1#page=4)
- 실물 플러그 삽입·링 조립·화이트보드 닦기에서 자율 성공률을 측정하고 플러그 삽입에서는 손목 피드백과 그 시간 변화의 효과를 따로 평가했다. [PDF 5쪽](https://arxiv.org/pdf/2609.22840v1#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2609.22840v1#page=6)

## Observation–State–Action Interface

Wrist wrench·변화량·base motion → pose residual; critic은 autonomous 구간을 사용한다.

## Evaluation Scope and Claim Boundary

실제 plug·ring-on-peg·wiping에서 residual imitation을 포함한 기준선과 비교한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2609.22840). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

RL 이득이 성공 데이터 선택·추가 imitation으로 설명되는지 판단할 직접 선행이다.

## Verification Boundary

개입 경계, 데이터 예산, force 관측 주기와 base chunk 비용을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
