# PRISM: Precision Forcing for Generalist Vision-Language-Action Policies

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
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
- 방법·평가 확인 (2026-11-25): [원문 1, 5, 6, 7, 8, 9쪽](https://arxiv.org/pdf/2610.14704v1#page=1) · [다축 분류와 공개 범위](../../../work/sources/batches/core_next_10.yaml)
- Source audit: 2026-11-18: arXiv 초록·공식 publication/project를 확인한 등록. Abstract 기반 — 본문 수동 확인 필요. 연구 dossier의 지정 절 검토와 paper별 5-note의 evidence를 구별하며 사용자 읽기 상태는 변경하지 않음. Author project는 research manuscript 2026으로 표시. GitHub root의 prism/openpi/starvla/configs/scripts를 확인했으나 설치·실행은 하지 않음. 동명 depth 논문과 identifier/제목으로 구별. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

PRISM은 정밀 조작 성패를 가르는 문맥과 흐름 생성 시점에 더 많은 학습 신호를 배분해 범용 VLA의 연속 행동을 미세조정한다. [PDF 1쪽](https://arxiv.org/pdf/2610.14704v1#page=1)

## Core Idea and Contribution

- 훈련 궤적에서 정밀도가 필요한 정도를 추정해 흐름 오차의 가중치를 바꾸고 시각언어 표현이 그 요구 수준을 예측하도록 보조 학습한다. [PDF 5쪽](https://arxiv.org/pdf/2610.14704v1#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2610.14704v1#page=6)
- 실물 드라이브 커넥터 삽입·양팔 커넥터 결합·나사 조임에서 과제 전체 성공률의 평균이 기본 π0.5의 38.3%에서 PRISM의 86.7%로 높아졌다. [PDF 1쪽](https://arxiv.org/pdf/2610.14704v1#page=1) · [PDF 9쪽](https://arxiv.org/pdf/2610.14704v1#page=9)

## Observation–State–Action Interface

VLM condition과 flow action expert의 학습을 조정한다. 정밀도 점수는 학습 신호이며 별도 센서나 test-time oracle 입력으로 설명하지 않는다.

## Evaluation Scope and Claim Boundary

초록·project는 simulation과 실제 로봇의 connector insertion, 양팔 connector mating, screw tightening을 보고한다. Trial 수·task별 분모·성공 정의와 수치 비교는 본문 대조 전 미확정이다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2610.14704) · [저자 project/code](https://seen-e.github.io/PRISM/) · [공식 code](https://github.com/seen-e/PRISM). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

작업 허용 오차에 따른 학습 가중과 표현 내재화를 이미 다룬 직접 NEXT다. 일반 tolerance-weighted VLA 학습을 새 기여로 주장하지 않도록 한다.

## Verification Boundary

정밀도 proxy와 실제 공차의 차이·flow-time weighting·SNR gate·auxiliary loss·task별 trial·공개 구현의 논문 일치을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 공개 자료의 확인 범위

- PRISM용 시연 데이터와 정밀도 학습 신호 처리 · prism/data.py [배포 파일](https://raw.githubusercontent.com/seen-e/PRISM/5a84f5a9e69bbbb5e64b45c999adc9a532219928/prism/data.py)
