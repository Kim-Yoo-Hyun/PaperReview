# Trajectory-Level Continuous Action Representation for Robotic Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ECCV
- Authors: Tong Yang, Jingkai Jia, Yuecheng Xu, Xueyao Chen, Chi Zhang, Wenqiang Zhang
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: action-representation, continuous-latent, control-frequency, manipulation
- Aliases: CAT
- Official paper: https://link.springer.com/chapter/10.1007/978-3-032-37369-4_24
- Venue verification: https://link.springer.com/chapter/10.1007/978-3-032-37369-4_24
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-11-12: 공식 abstract/metadata·명시한 project 확인. Springer ECCV 2026 chapter와 arXiv v2 abstract 확인. Code/project URL은 확인하지 못했다. 제어 주기 일반화와 통신 지연 강건성은 구별한다. 새 5-note는 초록 수준이며 과거 N1/N2의 지정 본문/source 검토는 work/sources/vla_masters_gap_scout_2026-11-12.json을 따른다. 사용자 정독·코드 재현을 뜻하지 않는다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

CAT는 동일한 실제 시간 동안의 로봇 궤적을 고정된 수의 연속 잠재 토큰으로 표현해 제어 주파수가 바뀌어도 움직임을 기술할 수 있게 한다. [PDF 1쪽](https://arxiv.org/pdf/2608.24111v2#page=1)

## Core Idea and Contribution

- 측정 시점을 공통 시간 좌표에 놓는 위치 부호화와 궤적 단위 정규화를 적용해 표본 수가 늘어도 같은 구간의 표현 크기를 유지한다. [PDF 4쪽](https://arxiv.org/pdf/2608.24111v2#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2608.24111v2#page=5)
- 시뮬레이션과 네 가지 실제 장기 조작에서 이산·연속 행동 표현을 비교하고 같은 학습 예산에서 제어 주파수와 표현 선택이 성능에 주는 영향을 평가했다. [PDF 8쪽](https://arxiv.org/pdf/2608.24111v2#page=8) · [PDF 12쪽](https://arxiv.org/pdf/2608.24111v2#page=12)

## Observation–State–Action Interface

시간 구간의 행동 궤적·control frequency ↔ 연속 latent token ↔ 실행 행동.

## Evaluation Scope and Claim Boundary

LIBERO·MimicGen·실제 장시간 조작에서 backbone과 control frequency를 바꿔 비교한다.

근거: [공식 paper/abstract](https://link.springer.com/chapter/10.1007/978-3-032-37369-4_24). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

제어 간격·물리 시간 조건부 행동 표현 자체를 새 공백으로 오인하지 않게 하는 기준이다.

## Verification Boundary

본문에서 확인할 항목: 시간 구간·normalizer·주파수 학습 노출·동일 episode 내 변경 평가 유무. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
