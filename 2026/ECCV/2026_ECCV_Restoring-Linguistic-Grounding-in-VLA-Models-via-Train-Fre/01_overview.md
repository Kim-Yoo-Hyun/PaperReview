# Restoring Linguistic Grounding in VLA Models via Train-Free Attention Recalibration

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ECCV
- Authors: Ninghao Zhang, Bin Zhu, Shijie Zhou, Jingjing Chen
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: language-grounding, OOD-instructions, attention, diagnostic-benchmark
- Aliases: IGAR, ICBench, Instruction-Guided Attention Recalibration
- Official paper: https://link.springer.com/chapter/10.1007/978-3-032-37152-2_3
- Venue verification: https://link.springer.com/chapter/10.1007/978-3-032-37152-2_3
- Code/Project: https://ray-nh.github.io/igar/
- Code: project_only
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인. 모순 지시에서는 기존 시각 task의 낮은 성공률이 바람직할 수 있다. 정상 지시 성공 지표와 방향을 혼동하지 않는다. 본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지.

## Problem and Importance

지시가 장면과 모순되어도 VLA가 시각적으로 익숙한 행동을 계속할 수 있다.

## Core Idea and Contribution

ICBench로 같은 장면의 모순 지시를 진단하고 추론 시 attention을 재조정하여 언어 영향을 복원한다.

## Observation–State–Action Interface

고정 장면·변경 instruction → attention recalibration → VLA action; 재학습은 하지 않는다.

## Evaluation Scope and Claim Boundary

π0·π0.5·OpenVLA-OFT, LIBERO task와 실제 Franka에서 지시 모순에 따른 잘못된 실행을 평가한다.

근거: [공식 paper/abstract](https://link.springer.com/chapter/10.1007/978-3-032-37152-2_3) · [저자 project/code](https://ray-nh.github.io/igar/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

RL 이후 성공률이 언어 grounding을 보장하지 않는다는 직접 평가·간단 대안이다.

## Verification Boundary

모순의 정답 정의, 무조건 정지 대조, 정상 지시 성능 trade-off을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
