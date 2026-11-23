# Adaptive Action Chunking at Inference-time for Vision-Language-Action Models

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / CVPR
- Authors: Yuanchang Liang, Xiaobo Wang, Kai Wang, Shuo Wang, Xiaojiang Peng, Haoyu Chen, David Kim Huat Chua, Prahlad Vadakkepat
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, action-chunking, feedback, control-frequency
- Aliases: AAC
- Official paper: https://arxiv.org/abs/2604.04161
- Venue verification: https://openaccess.thecvf.com/CVPR2026?day=2026-06-06
- Code/Project: https://lance-lot.github.io/adaptive-chunking.github.io/
- Code: project_only
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

AAC는 현재 정책의 행동 예측에서 구한 엔트로피를 이용해 다음 관측 전까지 실행할 행동 묶음 길이를 추론 시점에 선택한다. [PDF 1쪽](https://arxiv.org/pdf/2604.04161v2#page=1)

## Core Idea and Contribution

- 행동 예측의 불확실성을 묶음 길이 결정에 사용해 반응성과 연속 동작 사이의 균형을 조절한다. [PDF 3쪽](https://arxiv.org/pdf/2604.04161v2#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2604.04161v2#page=4)
- LIBERO 계열에서 기준선과 비교하고 실제 조작에서도 고정 묶음 길이와 적응형 선택의 성능을 평가했다. [PDF 6쪽](https://arxiv.org/pdf/2604.04161v2#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2604.04161v2#page=7)

## Observation–State–Action Interface

VLA 예측 sample → uncertainty cue → 실행 길이 → 다음 관측.

## Evaluation Scope and Claim Boundary

Simulation과 real-robot manipulation 비교를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2604.04161) · [저자 project/code](https://lance-lot.github.io/adaptive-chunking.github.io/). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

E2의 adaptive horizon 주장에 대한 직접 baseline이다.

## Verification Boundary

entropy 추정 sample 수, 최소 이동량, sensor/inference timing을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
