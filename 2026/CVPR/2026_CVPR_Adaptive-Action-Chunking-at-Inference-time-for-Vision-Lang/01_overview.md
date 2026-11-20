# Adaptive Action Chunking at Inference-time for Vision-Language-Action Models

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
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
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다.

## Problem and Importance

고정 action chunk 길이가 반응성과 일관성의 균형을 제한한다.

## Core Idea and Contribution

Action entropy를 이용해 추론 중 실행할 chunk 길이를 조정한다.

## Observation–State–Action Interface

VLA 예측 sample → uncertainty cue → 실행 길이 → 다음 관측.

## Evaluation Scope and Claim Boundary

Simulation과 real-robot manipulation 비교를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2604.04161) · [저자 project/code](https://lance-lot.github.io/adaptive-chunking.github.io/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

E2의 adaptive horizon 주장에 대한 직접 baseline이다.

## Verification Boundary

entropy 추정 sample 수, 최소 이동량, sensor/inference timing을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
