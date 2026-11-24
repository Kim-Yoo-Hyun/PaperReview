# Leave No Observation Behind: Real-time Correction for VLA Action Chunks

> Evidence maturity: `FULL_TEXT_CHECKED`. 아래에 쪽수를 붙인 문장을 원문과 대조했다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / arXiv
- Authors: Kohei Sendai, Maxime Alvarez, Tatsuya Matsushima, Yutaka Matsuo, Yusuke Iwasawa
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, action-chunking, feedback, control-frequency
- Aliases: A2C2
- Official paper: https://arxiv.org/abs/2509.23224
- Full-text retrieval: https://arxiv.org/pdf/2509.23224v1
- Venue verification: https://arxiv.org/abs/2509.23224
- Code/Project: https://github.com/k1000dai/a2c2-libero
- Code: https://github.com/k1000dai/a2c2-libero
- Source audit: 2026-11-24에 한 줄 요약과 핵심 기여 두 개를 아래 PDF 쪽수에 대조했다.

## Problem and Importance

A2C2는 VLA가 미리 출력한 행동 묶음을 실행하는 동안 최신 관측으로 매 제어 단계의 행동을 보정해 반응 지연을 줄인다. [PDF 1쪽](https://arxiv.org/pdf/2509.23224v1#page=1)

## Core Idea and Contribution

- 기반 정책을 고정하고 행동 묶음 안의 위치, 현재 관측과 기반 정책의 정보를 이용해 단계별 보정량을 학습한다. [PDF 3쪽](https://arxiv.org/pdf/2509.23224v1#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2509.23224v1#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2509.23224v1#page=5)
- KINETIX와 LIBERO Spatial에서 추론 지연과 행동 실행 구간을 바꾸어 보정에 따른 성공률 차이를 측정했다. [PDF 6쪽](https://arxiv.org/pdf/2509.23224v1#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2509.23224v1#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2509.23224v1#page=8)

## Observation–State–Action Interface

VLA chunk·fresh observation·chunk 정보 → residual → 실행.

## Evaluation Scope and Claim Boundary

Kinetix와 LIBERO Spatial 평가를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2509.23224) · [저자 project/code](https://github.com/k1000dai/a2c2-libero). 추가 수치와 실패 조건은 해당 실험의 표·설정을 확인해야 한다.

## Why This Paper Is Here — Researcher Interpretation

E2의 fresh feedback correction·delay/horizon 분리가 이미 존재함을 보여준다.

## Verification Boundary

residual target, 추가 feature, checkpoint 공개, 관측 latency을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
