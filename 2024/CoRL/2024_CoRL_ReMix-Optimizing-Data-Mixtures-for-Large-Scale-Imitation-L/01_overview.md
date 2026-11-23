# ReMix: Optimizing Data Mixtures for Large Scale Imitation Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2024 / CoRL
- Authors: Joey Hejna, Chethan Anand Bhateja, Yichen Jiang, Karl Pertsch, Dorsa Sadigh
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, Imitation Learning, data-mixture, distributional-robustness
- Aliases: ReMix, Re-Mix
- Official paper: https://proceedings.mlr.press/v270/hejna25a.html
- Venue verification: https://proceedings.mlr.press/v270/hejna25a.html
- Conference edition: 2024 · https://proceedings.mlr.press/v270/
- Code/Project: https://github.com/jhejna/remix
- Code: https://github.com/jhejna/remix
- Source audit: 2026-10-25 공식 abstract/서지정보 및 명시된 저자 링크 확인. 이번 노트는 abstract 기반이며 본문 전체·코드 실행·payload는 미검증이다. CoRL 개최 2024, PMLR 출판 2025. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

Re-Mix는 여러 로봇 데이터셋으로 모방학습을 할 때 데이터셋별 학습 비중을 자동으로 정한다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/hejna25a/hejna25a.pdf#page=1)

## Core Idea and Contribution

- 분포 강건 최적화로 데이터셋별 가중치를 추정하고 행동 공간과 기록 조건의 차이가 손실 비교를 왜곡하는 문제를 다룬다. [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/hejna25a/hejna25a.pdf#page=3) · [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/hejna25a/hejna25a.pdf#page=4) · [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/hejna25a/hejna25a.pdf#page=5)
- Open X-Embodiment 데이터 조합에서 학습한 가중치로 정책을 훈련하고 균일 혼합 및 사람이 정한 혼합과 비교했다. [PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/hejna25a/hejna25a.pdf#page=6) · [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/hejna25a/hejna25a.pdf#page=7) · [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/hejna25a/hejna25a.pdf#page=8)

## Observation–State–Action Interface

이질적 demonstration domain → mixture weights → downstream imitation policy.

## Evaluation Scope and Claim Boundary

Bridge·Open X-Embodiment 기반 데이터 혼합과 후속 정책 성능을 비교한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v270/hejna25a.html) · [저자 project/code](https://github.com/jhejna/remix). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

DataMIL의 subset 선택과 domain-level mixture 최적화를 구분하는 필수 비교군이다.

## Verification Boundary

domain 정의, proxy/target 접근, normalization, selection 계산 비용을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
