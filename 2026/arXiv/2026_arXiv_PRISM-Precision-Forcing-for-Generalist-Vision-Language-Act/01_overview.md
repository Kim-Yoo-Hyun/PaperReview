# PRISM: Precision Forcing for Generalist Vision-Language-Action Policies

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Authors: Chenghao Yue, Peiyan Li, Hao Wang, Lei Lv, Jiahao Chen, Huaping Liu, Yu Luo, Yuanlong Zhang
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, Flow Matching, precision manipulation, representation learning
- Aliases: PRISM Precision Forcing
- Official paper: https://arxiv.org/abs/2610.14704
- Venue verification: https://arxiv.org/abs/2610.14704
- Code/Project: https://seen-e.github.io/PRISM/
- Code: https://github.com/seen-e/PRISM
- Source audit: 2026-11-18: arXiv 초록·공식 publication/project를 확인한 등록. Abstract 기반 — 본문 수동 확인 필요. 연구 dossier의 지정 절 검토와 paper별 5-note의 evidence를 구별하며 사용자 읽기 상태는 변경하지 않음. Author project는 research manuscript 2026으로 표시. GitHub root의 prism/openpi/starvla/configs/scripts를 확인했으나 설치·실행은 하지 않음. 동명 depth 논문과 identifier/제목으로 구별.

## Problem and Importance

정밀 조작에서는 모든 context와 flow time의 오류를 동일하게 다루는 학습이 중요한 구간의 supervision을 충분히 배분하지 못할 수 있다.

## Core Idea and Contribution

시연의 proprioception으로 정밀도 요구를 점수화하고 flow supervision과 VLM 조건 표현 학습에 반영한다. 저자 project는 학습용 보조 head/label을 추론에서 제거한다고 설명한다.

## Observation–State–Action Interface

VLM condition과 flow action expert의 학습을 조정한다. 정밀도 점수는 학습 신호이며 별도 센서나 test-time oracle 입력으로 설명하지 않는다.

## Evaluation Scope and Claim Boundary

초록·project는 simulation과 실제 로봇의 connector insertion, 양팔 connector mating, screw tightening을 보고한다. Trial 수·task별 분모·성공 정의와 수치 비교는 본문 대조 전 미확정이다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2610.14704) · [저자 project/code](https://seen-e.github.io/PRISM/) · [공식 code](https://github.com/seen-e/PRISM). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

작업 허용 오차에 따른 학습 가중과 표현 내재화를 이미 다룬 직접 NEXT다. 일반 tolerance-weighted VLA 학습을 새 기여로 주장하지 않도록 한다.

## Verification Boundary

정밀도 proxy와 실제 공차의 차이·flow-time weighting·SNR gate·auxiliary loss·task별 trial·공개 구현의 논문 일치을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
