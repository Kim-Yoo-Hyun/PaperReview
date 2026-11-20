# Leave No Observation Behind: Real-time Correction for VLA Action Chunks

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Kohei Sendai, Maxime Alvarez, Tatsuya Matsushima, Yutaka Matsuo, Yusuke Iwasawa
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, action-chunking, feedback, control-frequency
- Aliases: A2C2
- Official paper: https://arxiv.org/abs/2509.23224
- Venue verification: https://arxiv.org/abs/2509.23224
- Code/Project: https://github.com/k1000dai/a2c2-libero
- Code: https://github.com/k1000dai/a2c2-libero
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다. OpenReview ICLR 2026 Rejected_Submission 확인; arXiv로 등록하며 학회 채택으로 표기하지 않는다.

## Problem and Importance

Chunk 실행 도중 들어오는 관측을 frozen VLA의 보정에 사용한다.

## Core Idea and Contribution

새 관측과 base action 등에 조건화한 residual head로 chunk action을 수정한다.

## Observation–State–Action Interface

VLA chunk·fresh observation·chunk 정보 → residual → 실행.

## Evaluation Scope and Claim Boundary

Kinetix와 LIBERO Spatial 평가를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2509.23224) · [저자 project/code](https://github.com/k1000dai/a2c2-libero). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

E2의 fresh feedback correction·delay/horizon 분리가 이미 존재함을 보여준다.

## Verification Boundary

residual target, 추가 feature, checkpoint 공개, 관측 latency을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
