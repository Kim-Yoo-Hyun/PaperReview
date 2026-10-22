# Leave No Observation Behind: Real-time Correction for VLA Action Chunks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Chunk 실행 도중 들어오는 관측을 frozen VLA의 보정에 사용한다.

## Bottleneck and Changed Formulation

새 관측과 base action 등에 조건화한 residual head로 chunk action을 수정한다.

## System and Robotics Loop

VLA chunk·fresh observation·chunk 정보 → residual → 실행.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

residual target, 추가 feature, checkpoint 공개, 관측 latency.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Kinetix와 LIBERO Spatial 평가를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2509.23224) · [저자 project/code](https://github.com/k1000dai/a2c2-libero). Exact objective, constraints, success definition은 본문 수동 확인 필요.
