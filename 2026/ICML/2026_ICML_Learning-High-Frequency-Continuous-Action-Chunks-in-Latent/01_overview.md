# Learning High-Frequency Continuous Action Chunks in Latent Space

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ICML
- Authors: Kunyun Wang, Yuhang Zheng, Yupeng Zheng, Jieru Zhao, Wenchao Ding
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, action-chunking, feedback, control-frequency
- Aliases: RTR
- Official paper: https://proceedings.mlr.press/v306/wang26lj.html
- Venue verification: https://proceedings.mlr.press/v306/wang26lj.html
- Code/Project: https://github.com/tars-robotics/RTR
- Code: https://github.com/tars-robotics/RTR
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다.

## Problem and Importance

고주파 action의 학습·추론과 chunk 경계 연속성을 함께 다룬다.

## Core Idea and Contribution

VAE latent action chunk와 Reuse-then-Refine 실행을 결합한다.

## Observation–State–Action Interface

관측 → latent chunk → 고주파 action decoding·경계 보정.

## Evaluation Scope and Claim Boundary

실제 contact manipulation과 여러 policy backbone 비교를 보고한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v306/wang26lj.html) · [저자 project/code](https://github.com/tars-robotics/RTR). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

E2에서 고주파 표현과 controller 변경을 분리할 직접 기준이다.

## Verification Boundary

controller mode, interpolation baseline, VAE 데이터, refinement timing을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
