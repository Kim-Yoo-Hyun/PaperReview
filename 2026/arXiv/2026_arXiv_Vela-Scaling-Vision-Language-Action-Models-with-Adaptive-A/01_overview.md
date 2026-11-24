# Vela: Scaling Vision-Language-Action Models with Adaptive Action Curve Parametrization

> Evidence maturity: `FULL_TEXT_CHECKED`. 아래에 쪽수를 붙인 문장을 원문과 대조했다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Authors: Yifan Li, Jiaxu Wang, Dongming Wu, Yicheng Jiang, Ryan Ji, Xiangyu Yue, Yanwei Fu
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, action-chunking, feedback, control-frequency
- Aliases:
- Official paper: https://arxiv.org/abs/2610.05230
- Full-text retrieval: https://arxiv.org/pdf/2610.05230v1
- Venue verification: https://arxiv.org/abs/2610.05230
- Code/Project: https://clementine24.github.io/Vela/
- Code: not_released
- Source audit: 2026-11-24에 한 줄 요약과 핵심 기여 두 개를 아래 PDF 쪽수에 대조했다.

## Problem and Importance

Vela는 미래 행동을 시간 간격을 조정할 수 있는 연속 스플라인 궤적으로 표현해 다양한 로봇의 동작을 공통 인터페이스로 생성한다. [PDF 1쪽](https://arxiv.org/pdf/2610.05230v1#page=1)

## Core Idea and Contribution

- 고정된 출력 예산 안에서 동작에 따른 시간 구간과 궤적 매개변수를 함께 예측해 국소적인 움직임의 해상도를 조절한다. [PDF 3쪽](https://arxiv.org/pdf/2610.05230v1#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2610.05230v1#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2610.05230v1#page=5)
- LIBERO-X와 EBench, 두 실물 장기 조작에서 평가하고 기존 행동열에 사후 궤적 적합을 적용한 경우와 비교했다. [PDF 7쪽](https://arxiv.org/pdf/2610.05230v1#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2610.05230v1#page=8) · [PDF 9쪽](https://arxiv.org/pdf/2610.05230v1#page=9)

## Observation–State–Action Interface

관측·지시 → action curve → 실행 시 sampling.

## Evaluation Scope and Claim Boundary

Simulation benchmark와 실제 long-horizon manipulation을 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2610.05230) · [저자 project/code](https://clementine24.github.io/Vela/). 추가 수치와 실패 조건은 해당 실험의 표·설정을 확인해야 한다.

## Why This Paper Is Here — Researcher Interpretation

E2에서 연속 행동 곡선 자체를 신규 기여로 재주장하지 않기 위한 REFERENCE다.

## Verification Boundary

spline fitting, horizon-matched 학습, controller tracking, code 공개 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
