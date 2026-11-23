# LIBERO-RIG: A Hardware-Setup Robustness Benchmark for Vision-Language-Action Models

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Authors: Andrea Yaoyun Cui, Hanyu Wang, Xinyi Wang, Bangzheng Li, Lin Zhang, Zhenggang Tang, Shyamal Buch, Dejia Xu, Matthew Tancik
- Category: Benchmarks and Datasets
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: VLA, Benchmark, hardware-shift
- Aliases:
- Official paper: https://arxiv.org/abs/2610.18843
- Venue verification: https://arxiv.org/abs/2610.18843
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-10-21: official abstract / author project 확인. 5개 note는 abstract 기반이며 사용자 정독을 의미하지 않는다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

LIBERO-RIG는 같은 LIBERO 작업을 유지하면서 카메라 장착, 보정, 구동계, 그리퍼 등 하드웨어 설정 변화에 대한 강건성을 측정한다. [PDF 1쪽](https://arxiv.org/pdf/2610.18843v1#page=1)

## Core Idea and Contribution

- 장비 설정의 열한 축에 단계별 교란을 적용하고 각 시행의 고정된 교란 파라미터를 기록한다. [PDF 2쪽](https://arxiv.org/pdf/2610.18843v1#page=2) · [PDF 3쪽](https://arxiv.org/pdf/2610.18843v1#page=3)
- 모델과 교란 강도별 성공률을 비교했으며 시각 교란 학습이 영상에 나타나지 않는 고장까지 해결해 주지는 않았다고 보고했다. [PDF 4쪽](https://arxiv.org/pdf/2610.18843v1#page=4) · [PDF 8쪽](https://arxiv.org/pdf/2610.18843v1#page=8)

## Observation–State–Action Interface

Native VLA observation/action interface에 setup perturbation을 주입한다.

## Evaluation Scope and Claim Boundary

LIBERO 기반 여러 VLA와 hardware severity 조건을 평가한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2610.18843) · 저자 프로젝트·코드 주소 미확인. 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

D1의 fault taxonomy와 policy/controller 경계 진단에 필요한 NEXT benchmark다.

## Verification Boundary

native state 소비, fault axis와 onset, 공개 trial-level logs을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
