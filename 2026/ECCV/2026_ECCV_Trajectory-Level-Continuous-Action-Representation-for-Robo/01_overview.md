# Trajectory-Level Continuous Action Representation for Robotic Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
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
- Source audit: 2026-11-12: 공식 abstract/metadata·명시한 project 확인. Springer ECCV 2026 chapter와 arXiv v2 abstract 확인. Code/project URL은 확인하지 못했다. 제어 주기 일반화와 통신 지연 강건성은 구별한다. 새 5-note는 초록 수준이며 과거 N1/N2의 지정 본문/source 검토는 work/sources/vla_masters_gap_scout_2026-11-12.json을 따른다. 사용자 정독·코드 재현을 뜻하지 않는다.

## Problem and Importance

제어 주기에 묶인 행동 표현은 높은 샘플링 빈도에서 길어지고 시간적 일관성을 잃기 쉽다.

## Core Idea and Contribution

고정된 실제 시간 구간의 궤적을 continuous latent token으로 압축하고 주파수를 고려한 위치 표현을 사용한다.

## Observation–State–Action Interface

시간 구간의 행동 궤적·control frequency ↔ 연속 latent token ↔ 실행 행동.

## Evaluation Scope and Claim Boundary

LIBERO·MimicGen·실제 장시간 조작에서 backbone과 control frequency를 바꿔 비교한다.

근거: [공식 paper/abstract](https://link.springer.com/chapter/10.1007/978-3-032-37369-4_24). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

제어 간격·물리 시간 조건부 행동 표현 자체를 새 공백으로 오인하지 않게 하는 기준이다.

## Verification Boundary

본문에서 확인할 항목: 시간 구간·normalizer·주파수 학습 노출·동일 episode 내 변경 평가 유무. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
